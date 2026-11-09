# crcns-fcx-3 · author · run 42513613232

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls
```

```
<persisted-output>
Output too large (36.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/4af94460-6faa-4b11-996a-7573bacdf1a3/tool-results/bpqnedxfi.txt

Preview (first 2KB):
Sun Nov  8 19:15:30 UTC 2026
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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/4af94460-6faa-4b11-996a-7573bacdf1a3/tool-results/bpqnedxfi.txt"
}
```

```
1	Sun Nov  8 19:15:30 UTC 2026
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
[... 633 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md | head -150; wc -l docs/design.md; sed -n '/CRCNS/,/^## [A-Z]/p' docs/archives.md
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
[... 148 more lines not kept]
```

**Agent calls Bash**

```bash
ls paper claims/crcns-fcx-3 entries/001453-fouke-2025 claims/001453; cat claims/crcns-fcx-3/*.yaml
```

```
<persisted-output>
Output too large (37.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/4af94460-6faa-4b11-996a-7573bacdf1a3/tool-results/bnn3b3oco.txt

Preview (first 2KB):
claims/001453:
10.1016-j.cub.2025.04.027.yaml

claims/crcns-fcx-3:
10.3389-fnsys.2018.00065.yaml

entries/001453-fouke-2025:
README.md
entry.yaml
omr.py
reproduce_fouke_2025.ipynb
requirements.in
requirements.lock.txt

paper:
10.3389-fnsys.2018.00065.txt
[... 25 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/4af94460-6faa-4b11-996a-7573bacdf1a3/tool-results/bnn3b3oco.txt"
}
```

```
1	claims/001453:
2	10.1016-j.cub.2025.04.027.yaml
3	
4	claims/crcns-fcx-3:
5	10.3389-fnsys.2018.00065.yaml
6	
7	entries/001453-fouke-2025:
8	README.md
9	entry.yaml
10	omr.py
11	reproduce_fouke_2025.ipynb
12	requirements.in
13	requirements.lock.txt
14	
15	paper:
16	10.3389-fnsys.2018.00065.txt
17	fcx-3.data-description.pdf
18	fcx-3.data-description.txt
19	# Claims for Johnson, King-Stephens, Weber, Laxer, Lin & Knight (2019), Front. Syst. Neurosci. 12,
20	# 65, "Spectral Imprints of Working Memory for Everyday Associations in the Frontoparietal Network",
[... 610 more lines not kept]
```

**Agent calls Bash**

```bash
cat paper/fcx-3.data-description.txt; wc -c paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.3389-fnsys.2018.00065.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Now the example entry formats and the bucket listing.

**Agent calls Bash**

```bash
cd entries/001453-fouke-2025; cat entry.yaml requirements.in README.md; head -c 3000 omr.py; cd ../..; cat attempts/001453-fouke-2025-01.yaml | head -150
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
[... 248 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=fcx-3/" | python -c "
import sys,re
x=sys.stdin.read()
for k,s,m,e in re.findall(r'<Key>(.*?)</Key><LastModified>(.*?)</LastModified><ETag>(.*?)</ETag><Size>(.*?)</Size>',x): print(k,e,s)
print(x[:300] if 'Key' not in x else '')"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=fcx-3/" | head -c 3000
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=fcx-3/" | python -c "
import sys,re
x=sys.stdin.read()
for c in re.findall(r'<Contents>(.*?)</Contents>',x):
  print(re.search('<Key>(.*?)</Key>',c).group(1), re.search('<Size>(.*?)</Size>',c).group(1), re.search('<LastModified>(.*?)</LastModified>',c).group(1))"
curl -s https://crcnsarchive.s3-us-west-2.amazonaws.com/fcx-3/live/checksums.md5
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
B=https://crcnsarchive.s3-us-west-2.amazonaws.com/fcx-3/live; curl -s $B/filelist.txt; echo; curl -s $B/docs/summary_file.csv; echo; curl -s $B/docs/summary_channel_analysis.csv; echo; python -c "
import fsspec,zipfile
z=zipfile.ZipFile(fsspec.open('$B/analysis_scripts.zip').open())
for i in z.infolist(): print(i.filename,i.file_size)
"
```

```
Exit code 1
# CRCNS.org 'fcx-3' dataset files
# To use this for fetching files, comment out files that are
# not needed by putting a '#' as the first character on the line (default mode)
# or put a '+' as the first character to specifiy files to be fetched (+ mode).
# mode='default' (change to '+' for + mode).
 analysis_scripts.zip	6372 (6.2 KB)
 data/s1.tar.gz	1144345044 (1.0 GB)
 data/s2.tar.gz	1491455501 (1.3 GB)
 data/s3.tar.gz	3592865513 (3.3 GB)
 data/s4.tar.gz	836483844 (797.7 MB)
 data/s5.tar.gz	2815586456 (2.6 GB)
 data/s6.tar.gz	1329654513 (1.2 GB)
 data/s7.tar.gz	553878785 (528.2 MB)
 docs/crcns_fcx-3_data_description.docx	29876 (29.1 KB)
 docs/crcns_fcx-3_data_description.pdf	91343 (89.2 KB)
 docs/summary_channel_analysis.csv	1558 (1.5 KB)
 docs/summary_file.csv	382
 checksums.md5	714

[... 133 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && source dev/bin/activate && uv pip install -q fsspec aiohttp requests numpy scipy pandas h5py statsmodels matplotlib jupyter nbformat nbclient ipykernel pymatreader 2>&1 | tail -2; python -c "
import fsspec,zipfile
B='https://crcnsarchive.s3-us-west-2.amazonaws.com/fcx-3/live'
z=zipfile.ZipFile(fsspec.open(B+'/analysis_scripts.zip').open())
for i in z.infolist(): print(i.filename,i.file_size)
"
```

```
analysis_scripts/ 0
analysis_scripts/power_compute.m 2103
analysis_scripts/erp_compute.m 2376
analysis_scripts/subfunctions/ 0
analysis_scripts/subfunctions/psianalysis.m 4200
analysis_scripts/subfunctions/subtracterp.m 2066
analysis_scripts/subfunctions/zbaseline.m 969
analysis_scripts/psi_compute.m 2400
Shell cwd was reset to
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; python -c "
import fsspec,zipfile
B='https://crcnsarchive.s3-us-west-2.amazonaws.com/fcx-3/live'
z=zipfile.ZipFile(fsspec.open(B+'/analysis_scripts.zip').open())
for i in z.infolist():
  if i.file_size: print('=====',i.filename); print(z.read(i).decode('latin1'))
"
```

```
===== analysis_scripts/power_compute.m
% Compute task-induced power and compare conditions. Requires fieldtrip 
% toolbox.
%
% Key:
% subid = 's1' (required)
% elecs = {'LOF1','LOF2','LHH1'} (optional)
%
% E. L. Johnson, PhD
% Copyright (c) 2017
% UC Berkeley
% [removed: an e-mail address]

function [] = power_compute(subid, elecs)
% power_compute('s1', {'LOF1','LOF2','LHH1'});

% INPUT PATH TO DIRECTORY CONTAINING DIRECTORY 'data'
path = %%INSERT%%

dataDir = [path '/data/'];
[... 525 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; cd $TMPDIR; cat > t.py <<'EOF'
import fsspec, tarfile, time, sys
B='https://crcnsarchive.s3-us-west-2.amazonaws.com/fcx-3/live/data/'
s=sys.argv[1]
t=time.time()
f=fsspec.open(B+s+'.tar.gz', block_size=2**24).open()
tf=tarfile.open(fileobj=f, mode='r|gz')
for m in tf:
    print(m.name, m.size, round(time.time()-t,1), f.tell(), flush=True)
EOF
timeout 600 python t.py s7
```

```
s7 0 1.1 10240
s7/data_primary.mat 346985597 1.1 10240
s7/elec_labels.mat 44456 16.8 346859520
s7/s7_MNI_grid.csv 49396 16.8 346859520
s7/data_derived.mat 209628022 16.8 346869760
s7/summary_file_trial.csv 3544 25.8 553878785
Shell cwd was reset to
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; cd $TMPDIR; cat > t2.py <<'EOF'
import fsspec, tarfile, time, io, scipy.io as sio, numpy as np, pandas as pd
B='https://crcnsarchive.s3-us-west-2.amazonaws.com/fcx-3/live/data/'
s='s7'
f=fsspec.open(B+s+'.tar.gz', block_size=2**24).open()
tf=tarfile.open(fileobj=f, mode='r|gz')
for m in tf:
    if m.name.endswith('.csv') or m.name.endswith('elec_labels.mat') or m.name.endswith('derived.mat'):
        b=tf.extractfile(m).read()
        print('====',m.name, b[:120])
        if m.name.endswith('.csv'):
            print(b.decode()[:1500])
        else:
            d=sio.loadmat(io.BytesIO(b), squeeze_me=True, struct_as_record=False)
            for k,v in d.items():
                if k.startswith('__'): continue
                print(k, type(v))
                if hasattr(v,'_fieldnames'):
                    for fn in v._fieldnames:
                        x=getattr(v,fn); print('  ',fn, type(x), getattr(x,'shape',None), x if np.ndim(x)==0 or (hasattr(x,'size') and x.size<10) else '')
                    print('  label', list(v.label))
                    print('  trialinfo', v.trialinfo[:5], v.trialinfo.shape)
                    tt=v.time; print('  time', tt[0][[0,-1]], len(tt[0]), set(len(t) for t in tt))
                    print('  trial0', v.trial[0].shape, v.trial[0].dtype)
                    print('  hdr', v.hdr._fieldnames if hasattr(v.hdr,'_fieldnames') else v.hdr)
                else: print(v if np.size(v)<300 else np.shape(v))
EOF
python t2.py 2>&1 | head -150
```

```
==== s7/elec_labels.mat b'MATLAB 7.3 MAT-file, Platform: GLNXA64, Created on: Tue Aug 23 12:46:38 2016 HDF5 schema 1.00 .                     \x00\x00\x00\x00'
Traceback (most recent call last):
  File "/tmp/claude-1001/t2.py", line 13, in <module>
    d=sio.loadmat(io.BytesIO(b), squeeze_me=True, struct_as_record=False)
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/scipy/io/matlab/_mio.py", line 241, in loadmat
    MR, _ = mat_reader_factory(f, **kwargs)
            ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/scipy/io/matlab/_mio.py", line 76, in mat_reader_factory
    raise NotImplementedError('Please use HDF reader for matlab v7.3 '
                              'files, e.g. h5py')
NotImplementedError: Please use HDF reader for matlab v7.3 files, e.g. h5py
Shell cwd was reset to
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; cd $TMPDIR; cat > t2.py <<'EOF'
import fsspec, tarfile, time, io, h5py, numpy as np, scipy.io as sio
B='https://crcnsarchive.s3-us-west-2.amazonaws.com/fcx-3/live/data/'
s='s7'
f=fsspec.open(B+s+'.tar.gz', block_size=2**24).open()
tf=tarfile.open(fileobj=f, mode='r|gz')
def show(h, pre=''):
    for k in h:
        x=h[k]
        if isinstance(x,h5py.Group): print(pre+k,'/', dict(x.attrs)); show(x,pre+'  ')
        else: print(pre+k, x.shape, x.dtype, dict(x.attrs).get('MATLAB_class'))
for m in tf:
    if m.name.endswith('.csv'):
        b=tf.extractfile(m).read(); print('====',m.name); print(b.decode()[:1200])
    elif m.name.endswith('.mat') and 'primary' not in m.name:
        b=tf.extractfile(m).read(); print('====',m.name, b[:80])
        try:
            h=h5py.File(io.BytesIO(b),'r'); show(h)
        except Exception as e:
            print(e); d=sio.loadmat(io.BytesIO(b)); print(d.keys())
EOF
python t2.py 2>&1 | grep -v '^      ' | head -120
```

```
==== s7/elec_labels.mat b'MATLAB 7.3 MAT-file, Platform: GLNXA64, Created on: Tue Aug 23 12:46:38 2016 HDF'
#refs# / {'H5PATH': np.bytes_(b'/#refs#')}
  0 (7, 1) uint16 b'char'
  1 (7, 1) uint16 b'char'
  2 (7, 1) uint16 b'char'
  3 (7, 1) uint16 b'char'
  4 (7, 1) uint16 b'char'
  5 (7, 1) uint16 b'char'
  6 (7, 1) uint16 b'char'
  7 (7, 1) uint16 b'char'
  8 (7, 1) uint16 b'char'
  9 (7, 1) uint16 b'char'
  A (5, 1) uint16 b'char'
  Ab (5, 1) uint16 b'char'
  B (5, 1) uint16 b'char'
  Bb (5, 1) uint16 b'char'
  C (5, 1) uint16 b'char'
  Cb (5, 1) uint16 b'char'
  D (5, 1) uint16 b'char'
  Db (5, 1) uint16 b'char'
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; cd $TMPDIR; python t2.py 2>&1 | grep -v '^  [ #a-zA-Z0-9]*(' | grep -v "^  .* (.*uint16" | head -150
```

```
==== s7/elec_labels.mat b'MATLAB 7.3 MAT-file, Platform: GLNXA64, Created on: Tue Aug 23 12:46:38 2016 HDF'
#refs# / {'H5PATH': np.bytes_(b'/#refs#')}
elec_labels (1, 101) object b'cell'
==== s7/s7_MNI_grid.csv
#vtkpxElectrodeMultiGridSource File
#Description
patient
#Comment
no additional comment
#Number of Grids
 12
#- - - - - - - - - - - - - - - - - - -
# Electrode Grid 11
- - - - - - - - - - - - - - - - - - -
#vtkpxElectrodeGridSource File v2
#Description
AL
#Dimensions
 1 12
#Electrode Spacing
[... 122 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; cd $TMPDIR; cat > t3.py <<'EOF'
import fsspec, tarfile, time, io, h5py, numpy as np, pandas as pd
B='https://crcnsarchive.s3-us-west-2.amazonaws.com/fcx-3/live/data/'
s='s7'
f=fsspec.open(B+s+'.tar.gz', block_size=2**24).open()
tf=tarfile.open(fileobj=f, mode='r|gz')
def cellstr(h, ds):
    return [''.join(map(chr, h[r][()].ravel())) for r in ds[()].ravel()]
for m in tf:
    if m.name.endswith('.csv') and 'trial' in m.name:
        df=pd.read_csv(io.BytesIO(tf.extractfile(m).read()),header=None); print(df.shape); print(df.describe().T)
        print(df[1].value_counts(), pd.crosstab(df[1],df[3]))
    elif m.name.endswith('labels.mat'):
        h=h5py.File(io.BytesIO(tf.extractfile(m).read()),'r'); print(cellstr(h,h['elec_labels']))
    elif m.name.endswith('derived.mat'):
        h=h5py.File(io.BytesIO(tf.extractfile(m).read()),'r')
        for k in ['data_pre','data_encmain','data_proc']:
            g=h[k]; print(k, list(g.keys()))
            print(' label', cellstr(h,g['label']))
            print(' fsample', g['fsample'][()])
            ti=g['trialinfo'][()]; print(' trialinfo', ti.shape, ti[:,:4].T if ti.shape[0]==6 else ti[:4])
            tr=g['trial'][()].ravel(); tm=g['time'][()].ravel()
            x=h[tr[0]][()]; t=h[tm[0]][()].ravel()
            print(' ntrials', len(tr), 'trial0', x.shape, x.dtype, 'time', t[0], t[-1], len(t))
            print(' lens', sorted(set(h[r].shape for r in tr)), 'time starts', sorted(set(round(h[r][()].ravel()[0],4) for r in tm)))
            print(' hdr', list(g['hdr'].keys()))
            for kk in g['hdr']: 
                try: print('   ',kk, g['hdr'][kk][()].ravel()[:5])
                except Exception as e: print('   ',kk,e)
            if 'cfg' in g: print(' cfg keys', list(g['cfg'].keys())[:50])
EOF
python t3.py 2>&1 | head -120
```

```
['TOL_01', 'TOL_02', 'TOL_03', 'TOL_04', 'TOL_05', 'AL_01', 'AL_02', 'AL_03', 'AL_04', 'AL_05', 'AL_06', 'AL_07', 'AL_08', 'AL_09', 'AL_10', 'AL_11', 'AL_12', 'CL_01', 'CL_02', 'CL_03', 'CL_04', 'CL_05', 'CL_06', 'CL_07', 'CL_08', 'CL_09', 'CL_10', 'CL_11', 'CL_12', 'BL_01', 'BL_02', 'BL_03', 'BL_04', 'BL_05', 'BL_06', 'BL_07', 'BL_08', 'BL_09', 'BL_10', 'BL_11', 'BL_12', 'FOAL_01', 'FOAL_02', 'FOAL_03', 'FOAL_04', 'FOAL_05', 'FOPL_01', 'FOPL_02', 'FOPL_03', 'FOPL_04', 'FOPL_05', 'POAL_01', 'POAL_02', 'POAL_03', 'POAL_04', 'POAL_05', 'POAL_06', 'POAL_07', 'POAL_08', 'POPL_01', 'POPL_02', 'POPL_03', 'POPL_04', 'POPL_05', 'WL_01', 'WL_02', 'WL_03', 'WL_04', 'WL_05', 'AR_01', 'AR_02', 'AR_03', 'AR_04', 'AR_05', 'AR_06', 'AR_07', 'AR_08', 'AR_09', 'AR_10', 'AR_11', 'AR_12', 'CR_01', 'CR_02', 'CR_03', 'CR_04', 'CR_05', 'CR_06', 'CR_07', 'CR_08', 'CR_09', 'CR_10', 'BR_01', 'BR_02', 'BR_03', 'BR_04', 'BR_05', 'BR_06', 'BR_07', 'BR_08', 'BR_09', 'BR_10']
data_pre ['fsample', 'hdr', 'label', 'time', 'trial', 'trialinfo']
 label ['TOL_02', 'TOL_03', 'TOL_04', 'TOL_05', 'AL_09', 'AL_10', 'AL_11', 'AL_12', 'CL_02', 'CL_03', 'CL_04', 'CL_10', 'CL_11', 'CL_12', 'BL_10', 'BL_11', 'BL_12', 'FOAL_04', 'FOAL_05', 'FOPL_04', 'FOPL_05', 'POAL_06', 'POAL_07', 'POPL_02', 'POPL_03', 'POPL_04', 'POPL_05', 'WL_03', 'WL_04', 'WL_05', 'AR_01', 'AR_09', 'AR_10', 'AR_11', 'AR_12', 'CR_09', 'CR_10', 'BR_03', 'BR_04', 'BR_05', 'BR_06', 'BR_09', 'BR_10']
 fsample [[512.]]
 trialinfo (6, 90) [[1.000e+00 1.000e+00 1.000e+00 1.000e+00 9.000e+02 9.060e+02]
 [2.000e+00 1.000e+00 2.000e+00 3.000e+00 1.150e+03 7.240e+02]
 [3.000e+00 1.000e+00 2.000e+00 3.000e+00 1.150e+03 2.052e+03]
 [4.000e+00 1.000e+00 2.000e+00 3.000e+00 1.150e+03 7.370e+02]]
 ntrials 90 trial0 (2305, 43) float64 time -1.5 3.0 2305
 lens [(2305, 43)] time starts [np.float64(-1.5)]
 hdr ['Fs', 'label', 'nChans', 'nSamples', 'nSamplesPre', 'nTrials']
    Fs [512.]
    label [<HDF5 object reference> <HDF5 object reference> <HDF5 object r
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; source $TMPDIR/dev/bin/activate; cd $TMPDIR; cat > t4.py <<'EOF'
import fsspec, tarfile, io, h5py, numpy as np, pandas as pd
B='https://crcnsarchive.s3-us-west-2.amazonaws.com/fcx-3/live/data/'
s='s7'
f=fsspec.open(B+s+'.tar.gz', block_size=2**24).open()
tf=tarfile.open(fileobj=f, mode='r|gz')
def cellstr(h, ds):
    return [''.join(map(chr, h[r][()].ravel())) for r in ds[()].ravel()]
for m in tf:
    b=tf.extractfile(m).read() if m.isfile() else None
    if m.name.endswith('primary.mat'):
        hp=h5py.File(io.BytesIO(b),'r'); 
        def show(g,p=''):
            for k in g:
                x=g[k]
                if isinstance(x,h5py.Group): print(p+k,'/'); show(x,p+' ') if k!='#refs#' else None
                else: print(p+k,x.shape,x.dtype)
        show(hp)
    elif m.name.endswith('labels.mat'):
        h=h5py.File(io.BytesIO(b),'r'); lab=cellstr(h,h['elec_labels'])
    elif m.name.endswith('derived.mat'):
        hd=h5py.File(io.BytesIO(b),'r')
    elif 'trial' in m.name:
        df=pd.read_csv(io.BytesIO(b),header=None)
gd=hp['gdat_clean_filt'][()] if 'gdat_clean_filt' in hp else None
print(gd.shape)
if gd.shape[0]!=len(lab): gd=gd.T
g=hd['data_proc']; dl=cellstr(hd,g['label'])
tr=g['trial'][()].ravel()
x=hd[tr[0]][()]  # time x chan
I=df.iloc[0,8]; G=df.iloc[0,6]; H=df.iloc[0,7]
ch=dl.index('FOAL_04'); i=lab.index('FOAL_04'); j=lab.index('FOAL_05')
y=x[:,ch]
for name,sig in [('mono',gd[i]),('bip',gd[i]-gd[j]),('bip2',gd[j]-gd[i])]:
    best=None
    for start in range(int(I)-2000,int(I)+2000):
        seg=sig[start:start+len(y)]
        c=np.corrcoef(seg,y)[0,1]
        if best is None or c>best[0]: best=(c,start)
    print(name,best, 'offset from I (s)', (best[1]-I)/512, 'max abs diff', np.abs(sig[best[1]:best[1]+len(y)]-y).max(), np.abs(y).max())
EOF
python t4.py
```

```
Sun Nov  8 19:20:50 UTC 2026
gdat_clean_filt (445952, 101) float64
(445952, 101)
mono (np.float64(0.3429940715344265), 8804) offset from I (s) 2.076171875 max abs diff 95.3228844831449 41.162914189408426
bip (np.float64(0.5134387393270312), 6830) offset from I (s) -1.779296875 max abs diff 48.319399155657806 41.162914189408426
bip2 (np.float64(0.38349531919268154), 8749) offset from I (s) 1.96875 max abs diff 47.06238783384677 41.162914189408426
Shell cwd was reset to
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; cd $TMPDIR; cat >> t4.py <<'EOF'
from scipy.signal import fftconvolve
def best(sig, y):
    sig=sig-sig.mean(); yy=(y-y.mean())
    num=fftconvolve(sig, yy[::-1], mode='valid')
    c2=np.cumsum(np.r_[0,sig**2]); n=len(y)
    den=np.sqrt(c2[n:]-c2[:-n])*np.linalg.norm(yy)
    r=num/den; k=np.nanargmax(r); return r[k], k
print('ratio nsamples', 445952/431506)
for cand in [('FOAL_04',None),('FOAL_04','FOAL_05'),('FOAL_04','FOAL_03'),('FOAL_05',None)]:
    sig=gd[lab.index(cand[0])]-(gd[lab.index(cand[1])] if cand[1] else 0)
    r,k=best(sig,y); print(cand, r, k, (k-I)/512)
EOF
python t4.py 2>&1 | tail -6
```

```
bip2 (np.float64(0.38349531919268154), 8749) offset from I (s) 1.96875 max abs diff 47.06238783384677 41.162914189408426
ratio nsamples 1.0334780976394302
('FOAL_04', None) 0.5463600938095642 134870 248.298828125
('FOAL_04', 'FOAL_05') 0.5315745662001695 396934 760.142578125
('FOAL_04', 'FOAL_03') 0.9988041784249817 6818 -1.802734375
('FOAL_05', None) 0.5219262163524114 295376 561.787109375
Shell cwd was reset to
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; cd $TMPDIR; python - <<'EOF'
import fsspec,tarfile,io,re
B='https://crcnsarchive.s3-us-west-2.amazonaws.com/fcx-3/live/data/'
f=fsspec.open(B+'s7.tar.gz', block_size=2**24).open()
tf=tarfile.open(fileobj=f, mode='r|gz')
for m in tf:
    if m.name.endswith('grid.csv'):
        t=tf.extractfile(m).read().decode(); break
lines=t.splitlines()
for i,l in enumerate(lines):
    if l.startswith('#Description') or l.startswith('#Dimensions') or l.startswith('#Electrode Spacing') or l.startswith('# Electrode Grid'): print(l, '|', lines[i+1])
print(len(lines))
EOF
```

```
#Description | patient
# Electrode Grid 11 | - - - - - - - - - - - - - - - - - - -
#Description | AL
#Dimensions |  1 12
#Electrode Spacing |  10.0000 10.0000
# Electrode Grid 11 | - - - - - - - - - - - - - - - - - - -
#Description | AR
#Dimensions |  1 12
#Electrode Spacing |  10.0000 10.0000
# Electrode Grid 11 | - - - - - - - - - - - - - - - - - - -
#Description | BL
#Dimensions |  1 12
#Electrode Spacing |  10.0000 10.0000
# Electrode Grid 11 | - - - - - - - - - - - - - - - - - - -
#Description | BR
#Dimensions |  1 10
#Electrode Spacing |  10.0000 10.0000
# Electrode Grid 11 | - - - - - - - - - - - - - - - - - - -
#Description | CL
#Dimensions |  1 12
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; ls tools; python tools/entry.py --help 2>&1 | head -20; cat entries/001453-fouke-2025/requirements.in; ls schemas
```

```
Sun Nov  8 19:24:46 UTC 2026
__pycache__
agent_run.py
archive_transcripts.sh
archives
backfill_summaries.py
blind.sh
build_dryad_targets.py
build_figshare_targets.py
build_openneuro_targets.py
build_site.py
build_targets.py
claims_check.py
conversion_issue.py
datasets.py
entry.py
flagged.py
get_papers.sh
notify.py
paper_match.py
[... 41 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/crcns-fcx-3-johnson-2019/fcx3.py",
 "content": "\"\"\"Loading and measures for CRCNS data set fcx-3 (Johnson et al. 2019, Front. Syst. Neurosci. 12, 65,\ndoi:10.3389/fnsys.2018.00065).\n\nThe data set (doi:10.6080/K06971S9) holds, per subject, a tar.gz with the filtered continuous iEEG\n(data_primary.mat), the channel names (elec_labels.mat), electrode positions (s<n>_MNI_grid.csv),\nthe preprocessed epochs (data_derived.mat, FieldTrip structures data_pre, data_encmain and\ndata_proc, MATLAB 7.3) and a trial table (summary_file_trial.csv). The tar files are streamed from\nthe public bucket and decompressed in memory, one subject at a time; nothing is written to disk.\nA tar.gz cannot be read at random, so each subject's file is read once, start to end.\n\nWhere the parameters come from:\n\n- Channels analysed, by region and hemisphere: docs/summary_channel_analysis.csv of the data set.\n  The derived epochs carry more channels; only the listed ones are kept.\n- Analysis windows, in the time axis of the derived epochs: processing [0.3, 1.2] s of data_proc,\n  maintenance [0.6, 1.5] s of data_encmain, baseline [0.65, 0.85] s of data_pre. These are the\n  latencies of the paper's deposited scripts (power_compute.m, erp_compute.m, psi_compute.m); the\n  notebook checks them against the trial table and the continuous data.\n- Power: Hanning-tapered windows of 3 cycles (3/f s), 2 to 40 Hz in 1-Hz steps, 10-ms steps\n  (Methods, Spectral Decomposition; power_compute.m). The derived epochs run from -1.5 to 3.0 s,\n  so every window of the analysis windows lies inside recorded data and no zero padding enters a\n  window. The baseline z-score of zbaseline.m (mean and SD of the means of r baseline points drawn\n  without replacement, r the number of correct trials) is computed in closed form, as the limit of\n  the code's 1000 draws (a standard choice, which cannot change a result: the z-score is the same\n  affine map for every trial at a channel and frequency, so the condition t-tests do not change).\n- ERP: 30-Hz low-pass FIR, zero padded to 7.5 s, baseline the pretrial temporal mean over trials\n  (Methods, Event-Related Potentials; erp_compute.m). The FIR order 3*fix(fs/30), applied forwards\n  and backwards, is FieldTrip's default for a 'fir' low-pass, which the script uses (standard\n  choice).\n- Cluster test: independent-samples t per point, threshold two-tailed 0.05, cluster mass the sum\n  of t, 1000 shuffles of the condition labels, connectivity across time and frequency within a\n  channel and across neighbouring channels at the same time and frequency (Methods, ERPs,\n  paragraph 2, and Spectral Decomposition, paragraph 3). Neighbours are not stated; the readings\n  are in `neighbours`.\n- PSI: ERP subtracted (mean over all correct trials for the task-induced PSI, per condition for the\n  time-resolved PSI: psi_compute.m and subtracterp.m), one Hanning-tapered FFT of each 900-ms\n  segment padded to 7.5 s read at the bins nearest to the integer frequencies (task-induced,\n  psi_compute.m 'mtmfft'), or the 3-cycle windows at 10-ms steps (time-resolved, 'mtmconvol').\n  Bands 2 to 7 and 9 to 24 Hz (Methods, Task-Induced PSI). The surrogate null follows\n  psianalysis.m: the trial-mean normalised cross-spectrum with its frequencies shuffled, the slope\n  summed over all bins, 1000 shuffles, one shuffle for all pairs; z per pair is the mean over the\n  band's bins of the z against each bin's null (time-resolved: one null of 1000 shuffles per time\n  point, a standard choice that changes only the Monte Carlo noise of the null).\n\"\"\"\n\nfrom __future__ import annotations\n\nimport io\nimport re\nimport tarfile\n\nimport fsspec\nimport h5py\nimport numpy as np\nimport pandas as pd\nfrom scipy import ndimage, signal, stats\nfrom scipy.sparse import coo_matrix\nfrom scipy.sparse.csgraph import connected_components\n\nBUCKET = \"https://crcnsarchive.s3-us-west-2.amazonaws.com/fcx-3/live\"\nSUBJECTS = [f\"s{i}\" for i in range(1, 8)]\nBLOCK = 2**24\n\nPROC_WIN = (0.3, 1.2)\nMAIN_WIN = (0.6, 1.5)\nBASE_WIN = (0.65, 0.85)\nFOI = np.arange(2, 41)\nTOI_STEP = 0.01\nBANDS = {\"delta-theta\": (2, 7), \"alpha-beta\": (9, 24)}\nPAD_S = 7.5\nN_PERM = 1000\n\n\n# --------------------------------------------------------------------------- archive files\n\ndef read_bytes(path):\n    with fsspec.open(f\"{BUCKET}/{path}\", block_size=BLOCK) as f:\n        return f.read()\n\n\ndef checksums():\n    out = {}\n    for line in read_bytes(\"checksums.md5\").decode().splitlines():\n        if line.strip():\n            md5, name = line.split()\n            out[name] = md5\n    return out\n\n\ndef bucket_listing():\n    \"\"\"Keys and sizes of the data set's files, from the bucket's listing.\"\"\"\n    import urllib.request\n    url = \"https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=fcx-3/\"\n    x = urllib.request.urlopen(url).read().decode()\n    rows = re.findall(r\"<Key>(.*?)</Key><LastModified>(.*?)</LastModified><ETag>(.*?)</ETag>.*?<Size>(\\d+)</Size>\", x)\n    return pd.DataFrame([(k, int(s), lm, e.replace(\"&quot;\", \"\")) for k, lm, e, s in rows],\n                        columns=[\"key\", \"size\", \"modified\", \"etag\"])\n\n\ndef summary_file():\n    \"\"\"docs/summary_file.csv: per subject age, sex, accuracy and mean correct RT per condition.\"\"\"\n    cols = [\"subject\", \"age\", \"sex\", \"acc_identity\", \"acc_spatial\", \"acc_temporal\",\n            \"rt_identity\", \"rt_spatial\", \"rt_temporal\"]\n    return pd.read_csv(io.BytesIO(read_bytes(\"docs/summary_file.csv\")), header=None, names=cols)\n\n\ndef channel_table():\n    \"\"\"docs/summary_channel_analysis.csv as one row per analysed channel.\"\"\"\n    rows = []\n    text = read_bytes(\"docs/summary_channel_analysis.csv\").decode()\n    cols = [(\"PFC\", \"L\"), (\"PFC\", \"R\"), (\"parietal\", \"L\"), (\"parietal\", \"R\")]\n    subj = None\n    for line in text.splitlines()[2:]:\n        parts = line.split(\",\")\n        if parts[0].strip():\n            subj = parts[0].strip().lower()\n        for (region, hemi), lab in zip(cols, parts[1:5]):\n            if lab.strip():\n                rows.append((subj, lab.strip(), region, hemi))\n    return pd.DataFrame(rows, columns=[\"subject\", \"label\", \"region\", \"hemisphere\"])\n\n\n# --------------------------------------------------------------------------- MATLAB 7.3 helpers\n\ndef _cellstr(h, ds):\n    return [\"\".join(map(chr, h[r][()].ravel())) for r in ds[()].ravel()]\n\n\ndef parse_grid(text):\n    \"\"\"Electrode positions of an s<n>_MNI_grid.csv (vtkpx multi-grid): {grid name: (dims, spacing, positions)}.\"\"\"\n    lines = text.splitlines()\n    grids, name = {}, None\n    for i, line in enumerate(lines):\n        if line.startswith(\"#vtkpxElectrodeGridSource\"):\n            name = None\n        elif line.startswith(\"#Description\") and i + 1 < len(lines) and lines[i - 1].startswith(\"#vtkpxElectrodeGridSource\"):\n            name = lines[i + 1].strip()\n            grids[name] = {\"dims\": None, \"spacing\": None, \"pos\": []}\n        elif name and line.startswith(\"#Dimensions\"):\n            grids[name][\"dims\"] = tuple(int(v) for v in lines[i + 1].split())\n        elif name and line.startswith(\"#Electrode Spacing\"):\n            grids[name][\"spacing\"] = float(lines[i + 1].split()[0])\n        elif name and line.startswith(\"#Position\"):\n            grids[name][\"pos\"].append([float(v) for v in lines[i + 1].split()])\n    for g in grids.values():\n        g[\"pos\"] = np.array(g[\"pos\"])\n    return grids\n\n\ndef split_label(lab):\n    m = re.match(r\"^(.*?)_?(\\d+)$\", lab)\n    return m.group(1), int(m.group(2))\n\n\n# --------------------------------------------------------------------------- streaming one subject\n\ndef stream_subject(sid, analysed, check_channels=2, check_trials=8, rng=None):\n    \"\"\"Stream one subject's tar.gz and return its trial table, the derived epochs of the analysed\n    channels, and a check of the derived epochs against the continuous data.\n\n    analysed: list of the subject's analysed channel labels, in the order to keep.\n    \"\"\"\n    rng = rng or np.random.default_rng(0)\n    out = {\"subject\": sid, \"members\": []}\n    primary = None\n    with fsspec.open(f\"{BUCKET}/data/{sid}.tar.gz\", block_size=BLOCK) as f:\n        with tarfile.open(fileobj=f, mode=\"r|gz\") as tf:\n            for m in tf:\n                if not m.isfile():\n                    continue\n                name = m.name.split(\"/\")[-1]\n                out[\"members\"].append((name, m.size))\n                b = tf.extractfile(m).read()\n                if name == \"data_primary.mat\":\n                    with h5py.File(io.BytesIO(b), \"r\") as h:\n                        ds = h[\"gdat_clean_filt\"]\n                        out[\"primary_keys\"] = [k for k in h.keys() if not k.startswith(\"#\")]\n                        out[\"primary_shape\"] = ds.shape\n                        primary = ds.astype(\"float32\")[()]\n                elif name == \"elec_labels.mat\":\n                    with h5py.File(io.BytesIO(b), \"r\") as h:\n                        out[\"elec_labels\"] = _cellstr(h, h[\"elec_labels\"])\n                elif name.endswith(\"_MNI_grid.csv\"):\n                    out[\"grid\"] = parse_grid(b.decode(errors=\"replace\"))\n                elif name == \"data_derived.mat\":\n                    out.update(_read_derived(b, analysed))\n                elif name == \"summary_file_trial.csv\":\n                    out[\"trials\"] = pd.read_csv(io.BytesIO(b), header=None, names=[\n                        \"trial\", \"correct\", \"type\", \"condition\", \"jitter\", \"rt\",\n                        \"pre_start\", \"encmain_start\", \"proc_start\"])\n                del b\n    if primary is not None:\n        if primary.shape[0] != len(out[\"elec_labels\"]):\n            primary = primary.T\n        out[\"clock\"] = _clock_check(out, primary, analysed, check_channels, check_trials, rng)\n        out[\"primary_samples\"] = primary.shape[1]\n        del primary\n    return out\n\n\ndef _read_derived(b, analysed):\n    res = {}\n    with h5py.File(io.BytesIO(b), \"r\") as h:\n        for key in [\"data_pre\", \"data_encmain\", \"data_proc\"]:\n            g = h[key]\n            labels = _cellstr(h, g[\"label\"])\n            idx = [labels.index(lab) for lab in analysed]\n            refs = g[\"trial\"][()].ravel()\n            trefs = g[\"time\"][()].ravel()\n            x = np.stack([h[r][()][:, idx].T for r in refs]).astype(\"float32\")  # trials x ch x time\n            times = np.stack([h[r][()].ravel() for r in trefs])\n            res[key] = {\"x\": x, \"time\": times[0], \"time_all_equal\": bool(np.allclose(times, times[0])),\n                        \"trialinfo\": g[\"trialinfo\"][()].T, \"labels_all\": labels,\n                        \"fs\": float(g[\"fsample\"][()].ravel()[0]),\n                        \"hdr_nSamples\": float(g[\"hdr\"][\"nSamples\"][()].ravel()[0])}\n    res[\"fs\"] = res[\"data_proc\"][\"fs\"]\n    return res\n\n\ndef _best_lag(sig, y):\n    sig = sig - sig.mean()\n    yy = y - y.mean()\n    num = signal.fftconvolve(sig, yy[::-1], mode=\"valid\")\n    c2 = np.cumsum(np.r_[0, sig.astype(float) ** 2])\n    n = len(y)\n    den = np.sqrt(c2[n:] - c2[:-n]) * np.linalg.norm(yy)\n    r = num / np.where(den > 0, den, np.inf)\n    k = int(np.argmax(r))\n    return float(r[k]), k\n\n\ndef _clock_check(sub, primary, analysed, n_ch, n_tr, rng):\n    \"\"\"Find, for a few analysed channels and trials, where each derived epoch lies in the continuous\n    data (as the bipolar difference of the channel's contact and the one before or after it), and\n    its offset from the trial table's epoch start column.\"\"\"\n    fs = sub[\"fs\"]\n    labs = sub[\"elec_labels\"]\n    rows = []\n    cols = {\"data_pre\": \"pre_start\", \"data_encmain\": \"encmain_start\", \"data_proc\": \"proc_start\"}\n    chans = list(rng.choice(len(analysed), size=min(n_ch, len(analysed)), replace=False))\n    tt = sub[\"trials\"]\n    for key, col in cols.items():\n        ep = sub[key]\n        trials = rng.choice(len(tt), size=min(n_tr, len(tt)), replace=False)\n        for c in chans:\n            lab = analysed[c]\n            pre, num = split_label(lab)\n            sep = \"_\" if \"_\" in lab else \"\"\n            width = len(lab) - len(pre) - len(sep)\n            cand = {}\n            for d in (-1, 1):\n                other = f\"{pre}{sep}{num + d:0{width}d}\"\n                if other in labs:\n                    cand[d] = primary[labs.index(lab)] - primary[labs.index(other)]\n            for t in trials:\n                y = ep[\"x\"][t, c].astype(float)\n                start = int(tt[col].iloc[t])\n                lo = max(0, start - int(4 * fs))\n                hi = min(primary.shape[1], start + int(4 * fs) + len(y))\n                best = None\n                for d, sig in cand.items():\n                    r, k = _best_lag(sig[lo:hi], y)\n                    if best is None or r > best[0]:\n                        best = (r, d, lo + k)\n                if best:\n                    rows.append({\"epoch\": key, \"channel\": lab, \"trial\": int(tt[\"trial\"].iloc[t]),\n                                 \"r\": best[0], \"reference\": best[1],\n                                 \"offset_s\": (best[2] - start) / fs})\n    return pd.DataFrame(rows)\n\n\n# --------------------------------------------------------------------------- neighbours\n\ndef neighbours(labels, grid=None, reading=\"adjacent\"):\n    \"\"\"Pairs of neighbouring channels (indices into labels), under the readings of the claims file\n    (header S2): 'adjacent', contacts with consecutive numbers on the same lead or strip (an\n    assumption: the paper says only \"neighboring electrodes\"); 'distance', bipolar midpoints within\n    1.5 times the lead's stated contact spacing in the s<n>_MNI_grid.csv positions (an assumption);\n    'none', no spatial clustering.\"\"\"\n    pairs = []\n    if reading == \"none\":\n        return np.zeros((0, 2), int)\n    parsed = [split_label(lab) for lab in labels]\n    if reading == \"adjacent\":\n        for i in range(len(labels)):\n            for j in range(i + 1, len(labels)):\n                if parsed[i][0] == parsed[j][0] and abs(parsed[i][1] - parsed[j][1]) == 1:\n                    pairs.append((i, j))\n        return np.array(pairs, int).reshape(-1, 2)\n    pos, spacing = bipolar_positions(labels, grid)\n    for i in range(len(labels)):\n        for j in range(i + 1, len(labels)):\n            if np.isfinite(pos[i]).all() and np.isfinite(pos[j]).all():\n                lim = 1.5 * max(spacing[i], spacing[j])\n                if np.linalg.norm(pos[i] - pos[j]) <= lim:\n                    pairs.append((i, j))\n    return np.array(pairs, int).reshape(-1, 2)\n\n\ndef bipolar_positions(labels, grid):\n    \"\"\"Midpoint of a bipolar channel's two contacts (the channel's contact and the one numbered\n    before it, as the clock check finds), taking contact n as the n-th electrode of the grid with the\n    label's prefix in the MNI file.\"\"\"\n    pos = np.full((len(labels), 3), np.nan)\n    spacing = np.full(len(labels), np.nan)\n    for i, lab in enumerate(labels):\n        pre, num = split_label(lab)\n        g = grid.get(pre) if grid else None\n        if g is None or num - 1 >= len(g[\"pos\"]) or num - 2 < 0:\n            continue\n        pos[i] = (g[\"pos\"][num - 1] + g[\"pos\"][num - 2]) / 2\n        spacing[i] = g[\"spacing\"]\n    return pos, spacing\n\n\n# --------------------------------------------------------------------------- spectral measures\n\ndef hanning_ft(n):\n    \"\"\"MATLAB hanning(n), as FieldTrip uses: 0.5*(1-cos(2*pi*k/(n+1))), k = 1..n.\"\"\"\n    k = np.arange(1, n + 1)\n    return 0.5 * (1 - np.cos(2 * np.pi * k / (n + 1)))\n\n\ndef win_index(time, win):\n    return np.where((time >= win[0] - 1e-9) & (time <= win[1] + 1e-9))[0]\n\n\ndef toi_index(time, win, step=TOI_STEP):\n    toi = np.arange(win[0], win[1] + step / 2, step)\n    return np.array([int(np.argmin(np.abs(time - t))) for t in toi]), toi\n\n\ndef tfr_fourier(x, time, fs, foi, toi_idx):\n    \"\"\"Complex 3-cycle Hanning spectra (mtmconvol) at the samples toi_idx: trials x ch x f x t.\"\"\"\n    n_tr, n_ch, n_t = x.shape\n    nfft = int(2 ** np.ceil(np.log2(n_t + int(3 / foi.min() * fs) + 1)))\n    X = np.fft.fft(x.reshape(-1, n_t).astype(\"float64\"), n=nfft, axis=1)\n    out = np.empty((n_tr * n_ch, len(foi), len(toi_idx)), np.complex64)\n    for fi, f in enumerate(foi):\n        n = int(round(3 / f * fs))\n        tap = hanning_ft(n)\n        tk = (np.arange(n) - (n - 1) / 2) / fs\n        kern = tap * np.exp(-2j * np.pi * f * tk)\n        # correlation with the window centred at each sample\n        K = np.fft.fft(kern[::-1], n=nfft)\n        y = np.fft.ifft(X * K[None, :], axis=1)\n        shift = (n - 1) // 2\n        out[:, fi, :] = y[:, toi_idx + shift]\n    return out.reshape(n_tr, n_ch, len(foi), len(toi_idx))\n\n\ndef fft_segment(x, time, fs, win, foi, pad=PAD_S):\n    \"\"\"Hanning-tapered FFT of one window, zero padded to pad s, at the bins nearest to foi\n    (FieldTrip mtmfft): trials x ch x f.\"\"\"\n    idx = win_index(time, win)\n    seg = x[:, :, idx].astype(\"float64\")\n    seg = seg * hanning_ft(len(idx))[None, None, :]\n    nfft = int(round(pad * fs))\n    F = np.fft.rfft(seg, n=nfft, axis=2)\n    freqs = np.fft.rfftfreq(nfft, 1 / fs)\n    bins = [int(np.floor(f * pad + 0.5)) for f in foi]\n    return F[:, :, bins], freqs[bins]\n\n\ndef lowpass_fir(x, fs, fc=30.0, pad=PAD_S):\n    \"\"\"FieldTrip-style FIR low-pass: order 3*fix(fs/fc), applied forwards and backwards, on the epoch\n    zero padded to pad s.\"\"\"\n    order = 3 * int(fs // fc)\n    b = signal.firwin(order + 1, fc / (fs / 2))\n    n = x.shape[-1]\n    tot = int(round(pad * fs))\n    left = max(0, (tot - n) // 2)\n    xp = np.zeros(x.shape[:-1] + (n + 2 * left,))\n    xp[..., left:left + n] = x\n    y = signal.filtfilt(b, [1.0], xp, axis=-1, padtype=None)\n    return y[..., left:left + n]\n\n\n# --------------------------------------------------------------------------- cluster test\n\ndef _tstat(Xc, Xc2, g, n1, n2, S, Q):\n    S1 = g @ Xc\n    Q1 = g @ Xc2\n    S2 = S - S1\n    Q2 = Q - Q1\n    m1, m2 = S1 / n1, S2 / n2\n    v1 = (Q1 - n1 * m1 ** 2) / (n1 - 1)\n    v2 = (Q2 - n2 * m2 ** 2) / (n2 - 1)\n    sp = ((n1 - 1) * v1 + (n2 - 1) * v2) / (n1 + n2 - 2)\n    with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n        return (m1 - m2) / np.sqrt(sp * (1 / n1 + 1 / n2))\n\n\n_STRUCT = np.zeros((3, 3, 3), bool)\n_STRUCT[1] = ndimage.generate_binary_structure(2, 1)\n\n\ndef _clusters(t, thr, sign, nb):\n    \"\"\"Clusters of t*sign > thr in a ch x f x time array; returns (label array, masses).\"\"\"\n    mask = (sign * t) > thr\n    lab, n = ndimage.label(mask, structure=_STRUCT)\n    if n == 0:\n        return lab, np.zeros(0)\n    if len(nb):\n        a = lab[nb[:, 0]].ravel()\n        b = lab[nb[:, 1]].ravel()\n        keep = (a > 0) & (b > 0)\n        if keep.any():\n            g = coo_matrix((np.ones(keep.sum()), (a[keep], b[keep])), shape=(n + 1, n + 1))\n            _, comp = connected_components(g, directed=False)\n            comp = comp - comp[0]\n            # renumber so that background stays 0\n            uniq, comp = np.unique(comp, return_inverse=True)\n            comp = comp - comp[0]\n            lab = comp[lab]\n            n = comp.max()\n    mass = np.bincount(lab.ravel(), weights=t.ravel(), minlength=n + 1)[1:]\n    return lab, mass\n\n\ndef cluster_test(X, groups, nb_readings, rng, n_perm=N_PERM, alpha=0.05):\n    \"\"\"Per-subject cluster-based permutation test of two groups of trials.\n\n    X: trials x ch x f x time (f may be 1). groups: bool array, True for the first condition.\n    nb_readings: {name: neighbour pairs}. Positive t means first condition > second.\n    Returns {reading: {'pos': [(mass, p, mask)], 'neg': [...]}} and the observed t.\n    \"\"\"\n    n_tr = X.shape[0]\n    shape = X.shape[1:]\n    Xf = X.reshape(n_tr, -1).astype(\"float32\")\n    Xf = Xf - Xf.mean(0, keepdims=True)\n    Xc2 = Xf ** 2\n    S, Q = Xf.sum(0), Xc2.sum(0)\n    g = groups.astype(\"float32\")\n    n1, n2 = groups.sum(), (~groups).sum()\n    df = n1 + n2 - 2\n    thr = stats.t.ppf(1 - alpha / 2, df)\n    t_obs = _tstat(Xf, Xc2, g, n1, n2, S, Q).reshape(shape)\n    obs = {k: {s: _clusters(t_obs, thr, sg, nb) for s, sg in ((\"pos\", 1), (\"neg\", -1))}\n           for k, nb in nb_readings.items()}\n    null = {k: {\"pos\": np.zeros(n_perm), \"neg\": np.zeros(n_perm)} for k in nb_readings}\n    for p in range(n_perm):\n        gp = rng.permutation(groups).astype(\"float32\")\n        tp = _tstat(Xf, Xc2, gp, n1, n2, S, Q).reshape(shape)\n        for k, nb in nb_readings.items():\n            _, mp = _clusters(tp, thr, 1, nb)\n            _, mn = _clusters(tp, thr, -1, nb)\n            null[k][\"pos\"][p] = mp.max() if len(mp) else 0.0\n            null[k][\"neg\"][p] = mn.min() if len(mn) else 0.0\n    res = {}\n    for k in nb_readings:\n        res[k] = {}\n        for s in (\"pos\", \"neg\"):\n            lab, mass = obs[k][s]\n            cl = []\n            for i, m in enumerate(mass):\n                if s == \"pos\":\n                    pv = np.mean(null[k][\"pos\"] >= m)\n                else:\n                    pv = np.mean(null[k][\"neg\"] <= m)\n                cl.append((float(m), float(pv), lab == i + 1))\n            cl.sort(key=lambda c: c[1])\n            res[k][s] = cl\n    return res, t_obs\n\n\n# --------------------------------------------------------------------------- PSI\n\ndef pairs_same_hemisphere(chan):\n    \"\"\"PFC-parietal pairs within a hemisphere: list of (pfc index, parietal index) into chan rows.\"\"\"\n    out = []\n    for i, a in chan.iterrows():\n        if a.region != \"PFC\":\n            continue\n        for j, b in chan.iterrows():\n            if b.region == \"parietal\" and b.hemisphere == a.hemisphere:\n                out.append((i, j))\n    return out\n\n\ndef _slope(c):\n    \"\"\"Sum over adjacent bins of Im(conj(c_f) c_{f+1}), over the last axis.\"\"\"\n    return np.imag(np.conj(c[..., :-1]) * c[..., 1:]).sum(-1)\n\n\ndef psi_measures(Fa, Fb, rng, n_perm=N_PERM, null_per_bin=True, deposited=False):\n    \"\"\"PSI z per pair, A = PFC (positive: PFC leads), B = parietal.\n\n    Fa, Fb: trials x pairs x f (x time) complex spectra, ERP already removed.\n    Returns {'a': z, 'b': z} for the readings of the claims file (header P1): (a) PSI from the\n    trial-averaged coherency (Nolte et al. 2008); (b) PSI per trial from the per-trial normalised\n    cross-spectrum, averaged over trials (psianalysis.m, with the conjugate the Methods' cross-\n    spectral density implies). The null shuffles the bins of the trial-mean normalised spectrum\n    (psianalysis.m): coherency for (a), the mean per-trial phasor for (b). With deposited=True also\n    'code': psianalysis.m as deposited, whose cross-spectrum lacks the conjugate.\n    \"\"\"\n    # move frequency to the last axis\n    Fa = np.moveaxis(Fa, 2, -1)\n    Fb = np.moveaxis(Fb, 2, -1)\n    S_ab = (Fa * np.conj(Fb)).mean(0)\n    S_aa = (np.abs(Fa) ** 2).mean(0)\n    S_bb = (np.abs(Fb) ** 2).mean(0)\n    C = S_ab / np.sqrt(S_aa * S_bb)\n    ptr = Fa * np.conj(Fb)\n    ptr = ptr / np.abs(ptr)\n    pp = ptr.mean(0)\n    obs = {\"a\": _slope(C), \"b\": _slope(ptr).mean(0)}\n    ref = {\"a\": C, \"b\": pp}\n    if deposited:\n        cs = Fa * Fb\n        den = np.sqrt((Fa ** 2) * np.conj(Fb ** 2))\n        ptr_c = cs / den\n        obs[\"code\"] = _slope(ptr_c).mean(0)\n        ref[\"code\"] = ptr_c.mean(0)\n    nf = Fa.shape[-1]\n    n_sets = nf if null_per_bin else 1\n    out = {}\n    for k in obs:\n        zs = []\n        for _ in range(n_sets):\n            nd = np.empty((n_perm,) + obs[k].shape)\n            for p in range(n_perm):\n                p1 = rng.permutation(nf)\n                p2 = rng.permutation(nf)\n                nd[p] = np.imag(np.conj(ref[k][..., p1]) * ref[k][..., p2]).sum(-1)\n            zs.append((obs[k] - nd.mean(0)) / nd.std(0, ddof=1))\n        out[k] = np.mean(zs, axis=0)\n    return out\n\n\n# --------------------------------------------------------------------------- group models\n\ndef paired_lme(y1, y2, subject):\n    \"\"\"Linear mixed model y ~ condition + (1|subject) + (1|pair) on two values per pair.\n\n    With every pair holding both values, the REML estimate of the condition effect is the mean of\n    the paired differences and its test the paired t-test over pairs (the subject and pair\n    intercepts cancel in the differences); the F is reported with the residual degrees of freedom\n    2n - 2, as MATLAB's fitlme does. The notebook checks this against statsmodels' MixedLM.\n    Returns (effect y2 - y1, F, p, n pairs).\n    \"\"\"\n    d = np.asarray(y2) - np.asarray(y1)\n    n = len(d)\n    t = d.mean() / (d.std(ddof=1) / np.sqrt(n))\n    F = t ** 2\n    p = stats.f.sf(F, 1, 2 * n - 2)\n    return float(d.mean()), float(F), float(p), n\n\n\ndef mixedlm_check(y1, y2, subject, pair):\n    \"\"\"statsmodels MixedLM fit of y ~ condition with subject groups and a pair variance component.\"\"\"\n    import statsmodels.formula.api as smf\n    df = pd.DataFrame({\"y\": np.r_[y1, y2], \"cond\": np.r_[np.zeros(len(y1)), np.ones(len(y2))],\n                       \"subject\": np.r_[subject, subject], \"pair\": np.r_[pair, pair]})\n    m = smf.mixedlm(\"y ~ cond\", df, groups=\"subject\", vc_formula={\"pair\": \"0 + C(pair)\"})\n    r = m.fit(reml=True)\n    t = r.tvalues[\"cond\"]\n    return float(r.params[\"cond\"]), float(t ** 2), float(stats.f.sf(t ** 2, 1, len(df) - 2))\n\n\ndef fdr_bh(p, q=0.05):\n    p = np.asarray(p)\n    n = len(p)\n    order = np.argsort(p)\n    ranked = p[order] * n / np.arange(1, n + 1)\n    crit = np.where(ranked <= q)[0]\n    sig = np.zeros(n, bool)\n    if len(crit):\n        sig[order[:crit.max() + 1]] = True\n    return sig\n\n\ndef runs(mask, times):\n    \"\"\"Runs of True in mask: list of (start, end) times.\"\"\"\n    out = []\n    i = 0\n    while i < len(mask):\n        if mask[i]:\n            j = i\n            while j + 1 < len(mask) and mask[j + 1]:\n                j += 1\n            out.append((times[i], times[j]))\n            i = j + 1\n        else:\n            i += 1\n    return out\n\n\ndef logit_mixed(k, n, cond_codes, subject, n_quad=30):\n    \"\"\"Random-intercept logistic model fitted by maximum likelihood with Gauss-Hermite quadrature.\n\n    k successes of n trials per row; fixed effects: intercept and the columns of cond_codes.\n    Returns (beta, se, loglik).\n    \"\"\"\n    from scipy.optimize import minimize\n    X = np.column_stack([np.ones(len(k)), cond_codes])\n    subs = pd.factorize(subject)[0]\n    xs, ws = np.polynomial.hermite.hermgauss(n_quad)\n\n    def nll(theta):\n        beta, ls = theta[:-1], theta[-1]\n        s = np.exp(ls)\n        eta = X @ beta\n        tot = 0.0\n        for g in np.unique(subs):\n            m = subs == g\n            u = np.sqrt(2) * s * xs\n            e = eta[m][:, None] + u[None, :]\n            ll = (k[m][:, None] * e - n[m][:, None] * np.logaddexp(0, e)).sum(0)\n            mx = ll.max()\n            tot += mx + np.log((ws * np.exp(ll - mx)).sum() / np.sqrt(np.pi))\n        return -tot\n\n    x0 = np.zeros(X.shape[1] + 1)\n    x0[-1] = np.log(0.5)\n    r = minimize(nll, x0, method=\"BFGS\")\n    # numerical Hessian for standard errors\n    h = 1e-4\n    p = len(r.x)\n    H = np.zeros((p, p))\n    for i in range(p):\n        for j in range(p):\n            e_i = np.eye(p)[i] * h\n            e_j = np.eye(p)[j] * h\n            H[i, j] = (nll(r.x + e_i + e_j) - nll(r.x + e_i - e_j) - nll(r.x - e_i + e_j)\n                       + nll(r.x - e_i - e_j)) / (4 * h * h)\n    cov = np.linalg.inv(H)\n    return r.x[:-1], np.sqrt(np.diag(cov))[:-1], -r.fun\n"
}
```

```
File created successfully at: entries/crcns-fcx-3-johnson-2019/fcx3.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/crcns-fcx-3-johnson-2019 && python - <<'EOF'
import re
s=open('fcx3.py').read()
old=s[s.index("            g = coo_matrix"):s.index("    mass = np.bincount")]
new='''            g = coo_matrix((np.ones(keep.sum()), (a[keep], b[keep])), shape=(n + 1, n + 1))
            k, comp = connected_components(g, directed=False)
            remap = np.arange(k)
            remap[comp[0]], remap[0] = 0, comp[0]
            lab = remap[comp][lab]
            n = k - 1
'''
s=s.replace(old,new)
s=s.replace("        shift = (n - 1) // 2\n        out[:, fi, :] = y[:, toi_idx + shift]","        shift = (n - 1) // 2\n        out[:, fi, :] = y[:, toi_idx - shift + n - 1]")
open('fcx3.py','w').write(s)
EOF
grep -n "remap\|toi_idx - shift" fcx3.py
```

```
348:        out[:, fi, :] = y[:, toi_idx - shift + n - 1]
411:            remap = np.arange(k)
412:            remap[comp[0]], remap[0] = 0, comp[0]
413:            lab = remap[comp][lab]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && python - <<'EOF'
import numpy as np, fcx3, time
fs=1000.; t=np.arange(-1.5,3.0+1e-9,1/fs)
x=np.sin(2*np.pi*6*t)*(t>0.5)
X=x[None,None,:]
idx,toi=fcx3.toi_index(t,(0.3,1.2))
F=fcx3.tfr_fourier(X,t,fs,np.array([4,6,10]),idx)
print(np.abs(F[0,0,:,::10]).round(1))
# delay test for psi sign: b lags a by 20ms
rng=np.random.default_rng(1)
n=60; a=rng.standard_normal((n,len(t))); 
from scipy.signal import butter, filtfilt
bb,aa=butter(4,[2,24],btype='band',fs=fs); a=filtfilt(bb,aa,a)
b=np.roll(a,20,axis=1)+0.5*rng.standard_normal(a.shape)
X=np.stack([a,b],1)
Fs,fr=fcx3.fft_segment(X,t,fs,(0.3,1.2),np.arange(2,8))
print(fr)
z=fcx3.psi_measures(Fs[:,[0]],Fs[:,[1]],rng,n_perm=200,deposited=True)
print({k:v for k,v in z.items()})
# cluster test synthetic
Xp=rng.standard_normal((80,5,10,30)); g=np.arange(80)<40; Xp[:40,1:3,2:5,10:20]+=0.8
t0=time.time()
res,tobs=fcx3.cluster_test(Xp,g,{'adj':np.array([[0,1],[1,2],[2,3],[3,4]]),'none':np.zeros((0,2),int)},rng,n_perm=200)
for k in res: print(k,[(round(m,1),p,mk.sum()) for m,p,mk in res[k]['pos'][:3]],[(round(m,1),p) for m,p,mk in res[k]['neg'][:2]])
print(time.time()-t0)
EOF
```

```
[[ 14.8  42.   65.8  66.7  46.2  31.9  31.6  31.5  31.6  31.8]
 [  0.7  18.8  63.3 107.5 124.8 125.2 125.3 125.3 125.3 125.2]
 [  0.    1.6  23.5  27.3  26.4  26.4  26.5  26.6  26.5  26.4]]
[2.         3.06666667 4.         5.06666667 6.         7.06666667]
{'a': array([15.91482912]), 'b': array([9.09237009]), 'code': array([22.22426815])}
adj [(215.0, 0.0, np.int64(59)), (3.2, 0.96, np.int64(1)), (3.0, 0.995, np.int64(1))] [(-8.5, 0.02), (-4.6, 0.76)]
none [(108.9, 0.0, np.int64(29)), (101.2, 0.0, np.int64(28)), (4.9, 0.49, np.int64(2))] [(-5.7, 0.205), (-4.6, 0.65)]
0.112274169921875
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && cat > $TMPDIR/dev7.py <<'EOF'
import numpy as np, fcx3, time, resource, pandas as pd
t0=time.time()
ch=fcx3.channel_table()
print(ch.groupby(['subject','region','hemisphere']).size().unstack([1,2]))
sid='s7'
c=ch[ch.subject==sid].reset_index(drop=True)
S=fcx3.stream_subject(sid, list(c.label))
print('stream', time.time()-t0, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,'GB')
print(S['members']); print(S['primary_shape'], S['fs'])
print(S['clock'].groupby(['epoch']).agg({'r':['min','median'],'offset_s':['min','max'],'reference':['min','max']}))
for k in ['data_pre','data_encmain','data_proc']:
    e=S[k]; print(k, e['x'].shape, e['time'][[0,-1]], e['time_all_equal'], e['hdr_nSamples'])
tt=S['trials']; ti=S['data_proc']['trialinfo']
print('trialinfo == table', np.array_equal(ti, tt.iloc[:,:6].values))
print(fcx3.neighbours(list(c.label),S['grid'],'adjacent'), fcx3.neighbours(list(c.label),S['grid'],'distance'))
print(fcx3.bipolar_positions(list(c.label),S['grid']))
import pickle
EOF
cd entries/crcns-fcx-3-johnson-2019 && python $TMPDIR/dev7.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/dev7.py", line 1, in <module>
    import numpy as np, fcx3, time, resource, pandas as pd
ModuleNotFoundError: No module named 'fcx3'
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && cd entries/crcns-fcx-3-johnson-2019 && PYTHONPATH=. python $TMPDIR/dev7.py
```

```
region       PFC       parietal      
hemisphere     L     R        L     R
subject                              
s1          10.0  11.0      1.0   1.0
s2           7.0  17.0      2.0   6.0
s3           NaN  54.0      NaN  14.0
s4           6.0   6.0      NaN   5.0
s5          10.0   NaN     16.0   NaN
s6           8.0   NaN      4.0   NaN
s7           4.0   NaN      5.0   NaN
stream 27.009835243225098 1.242964 GB
[('data_primary.mat', 346985597), ('elec_labels.mat', 44456), ('s7_MNI_grid.csv', 49396), ('data_derived.mat', 209628022), ('summary_file_trial.csv', 3544)]
(445952, 101) 512.0
                     r            offset_s           reference    
                   min    median       min       max       min max
epoch                                                             
data_encmain  0.997479  0.999900 -1.501953 -1.501953        -1  -1
data_pre      0.998469  0.999727 -1.402344 -1.402344        -1  -1
data_proc     0.999350  0.999882 -1.802734 -1.802734        -1  -1
data_pre (90, 9, 2305) [-1.5  3. ] True 431506.0
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> fcx3.py <<'EOF'


# --------------------------------------------------------------------------- one subject, all measures

NB_READINGS = ("adjacent", "distance", "none")


def seed(*keys):
    """A fixed seed per claim section and subject, so that each has its own generator."""
    import zlib
    return zlib.crc32("/".join(map(str, keys)).encode())


def jitter_check(S):
    """Timing contrast: the response to the next screen follows the delay jitter. In data_encmain the
    test cue appears 0.6 s + jitter after time 0, in data_proc the response screen 0.3 s + jitter
    after time 0. For each epoch, the mean over channels of the rectified, low-passed trial-mean
    signal of the 1150-ms trials is cross-correlated with that of the 900-ms trials; the lag that
    maximises it should be 0.25 s, and near 0 with the jitter labels shuffled."""
    out = {}
    fs = S["fs"]
    jit = S["data_proc"]["trialinfo"][:, 4]
    for key, onset in (("data_encmain", 0.6), ("data_proc", 0.3)):
        e = S[key]
        x = lowpass_fir(e["x"].astype("float64"), fs)
        x = x - x[:, :, win_index(e["time"], (onset - 0.3, onset))].mean(-1, keepdims=True)
        w = win_index(e["time"], (onset + 0.7, onset + 1.6))

        def env(m):
            return np.abs(x[m].mean(0)).mean(0)[w]

        def lag(m1, m2):
            a, b = env(m1), env(m2)
            a, b = a - a.mean(), b - b.mean()
            cc = signal.correlate(b, a, mode="full")
            lags = signal.correlation_lags(len(b), len(a), mode="full") / fs
            ok = np.abs(lags) <= 0.45
            return float(lags[ok][np.argmax(cc[ok])])

        rng = np.random.default_rng(seed("jitter", S["subject"], key))
        shuffled = [lag(*(lambda p: (p == 900, p == 1150))(rng.permutation(jit))) for _ in range(20)]
        out[key] = {"lag_s": lag(jit == 900, jit == 1150), "shuffled_median_abs_s": float(np.median(np.abs(shuffled)))}
    return out


def analyse_subject(S, chan, n_perm=N_PERM, do_time_resolved=True):
    """All per-subject measures used by the claims. chan: the subject's rows of channel_table()."""
    sid = S["subject"]
    fs = S["fs"]
    labels = list(chan.label)
    info = S["data_proc"]["trialinfo"]
    correct = info[:, 1] == 1
    cond = info[:, 3]
    R = {"subject": sid, "fs": fs, "labels": labels, "n_trials": len(info),
         "n_correct": int(correct.sum()), "n_incorrect": int((~correct).sum()),
         "n_correct_by_cond": {c: int((correct & (cond == c)).sum()) for c in (1, 2, 3)}}
    nb = {k: neighbours(labels, S.get("grid"), k) for k in NB_READINGS}
    R["neighbours"] = {k: len(v) for k, v in nb.items()}
    ccond = cond[correct]
    contrasts = {"spatial": 2, "temporal": 3}

    # ERP: low-pass the whole epoch, baseline on the pretrial mean, processing window
    pre, proc = S["data_pre"], S["data_proc"]
    base = lowpass_fir(pre["x"][correct].astype("float64"), fs)[:, :, win_index(pre["time"], BASE_WIN)]
    erp = lowpass_fir(proc["x"][correct].astype("float64"), fs)[:, :, win_index(proc["time"], PROC_WIN)]
    erp = erp - base.mean(axis=(0, 2))[None, :, None]
    R["erp"] = {}
    for name, c2 in contrasts.items():
        m = (ccond == 1) | (ccond == c2)
        rng = np.random.default_rng(seed("erp", sid, name))
        res, _ = cluster_test(erp[m][:, :, None, :], ccond[m] == 1, nb, rng, n_perm)
        R["erp"][name] = {k: {s: [(mm, p) for mm, p, _ in v[s]] for s in v} for k, v in res.items()}
    del erp, base

    # Power: 3-cycle Hanning windows, 10-ms steps
    tidx, toi = toi_index(proc["time"], PROC_WIN)
    Fp = tfr_fourier(proc["x"][correct], proc["time"], fs, FOI, tidx)
    bidx, _ = toi_index(pre["time"], BASE_WIN)
    Fb = tfr_fourier(pre["x"][correct], pre["time"], fs, FOI, bidx)
    pw = np.abs(Fp) ** 2
    bp = (np.abs(Fb) ** 2).transpose(1, 2, 0, 3).reshape(len(labels), len(FOI), -1)
    r = int(correct.sum())
    N = bp.shape[-1]
    bmean = bp.mean(-1)
    bsd = bp.std(-1, ddof=1) * np.sqrt((N - r) / (N - 1)) / np.sqrt(r)
    pz = (pw - bmean[None, :, :, None]) / bsd[None, :, :, None]
    R["power_toi"] = toi - toi[0]
    R["power"] = {}
    for name, c2 in contrasts.items():
        m = (ccond == 1) | (ccond == c2)
        rng = np.random.default_rng(seed("power", sid, name))
        res, t_obs = cluster_test(pz[m], ccond[m] == 1, nb, rng, n_perm)
        out = {}
        for k, v in res.items():
            out[k] = {}
            for s in ("pos", "neg"):
                out[k][s] = [{"mass": mm, "p": p,
                              "elec_mask": mk.any(axis=(1, 2)),
                              "tsum_by_elec": np.where(mk, t_obs, 0).sum(axis=(1, 2)),
                              "t_masked": np.where(mk, t_obs, 0).astype("float32")} for mm, p, mk in v[s] if p < 0.05]
                out[k][s + "_minp"] = min([p for _, p, _ in v[s]], default=1.0)
        R["power"][name] = {"clusters": out, "t": t_obs.astype("float32")}
    del pw, pz, Fb

    # PSI
    pairs = pairs_same_hemisphere(chan)
    R["pairs"] = [(labels[i], labels[j], chan.hemisphere[i]) for i, j in pairs]
    ia = [i for i, _ in pairs]
    ib = [j for _, j in pairs]
    enc = S["data_encmain"]
    R["psi"] = {}
    for band, (lo, hi) in BANDS.items():
        foi = np.arange(lo, hi + 1)
        res = {}
        for interval, (ep, win) in {"maintenance": (enc, MAIN_WIN), "processing": (proc, PROC_WIN)}.items():
            F, freqs = fft_segment(ep["x"][correct], ep["time"], fs, win, foi)
            F = F - F.mean(0, keepdims=True)  # ERP (mean over all correct trials) removed
            rng = np.random.default_rng(seed("psi", sid, band, interval))
            res[interval] = psi_measures(F[:, ia], F[:, ib], rng, deposited=True)
        res["freqs"] = freqs
        R["psi"][band] = res
    # time-resolved PSI per condition (ERP of the condition removed), mtmconvol
    if do_time_resolved:
        R["psi_t"] = {}
        for band, (lo, hi) in BANDS.items():
            fsel = [list(FOI).index(f) for f in range(lo, hi + 1)]
            R["psi_t"][band] = {}
            for c in (1, 2, 3):
                F = Fp[ccond == c][:, :, fsel, :]
                F = F - F.mean(0, keepdims=True)
                rng = np.random.default_rng(seed("psi_t", sid, band, c))
                R["psi_t"][band][c] = psi_measures(F[:, ia], F[:, ib], rng, null_per_bin=False)
    del Fp
    return R
EOF
cat > $TMPDIR/dev7b.py <<'EOF'
import numpy as np, fcx3, time, resource, pandas as pd, pickle, os
t0=time.time()
ch=fcx3.channel_table()
sid=os.environ.get('SID','s7')
c=ch[ch.subject==sid].reset_index(drop=True)
S=fcx3.stream_subject(sid, list(c.label))
print('stream', time.time()-t0, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,'GB', flush=True)
print(fcx3.jitter_check(S), time.time()-t0)
t0=time.time()
R=fcx3.analyse_subject(S,c,n_perm=int(os.environ.get('NP','100')))
print('analyse', time.time()-t0, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,'GB')
for k in ['n_trials','n_correct','n_incorrect','n_correct_by_cond','neighbours','pairs']: print(k,R[k])
for name in R['erp']: print('erp',name,{k:(v['pos'][:1],v['neg'][:1]) for k,v in R['erp'][name].items()})
for name in R['power']:
    for k,v in R['power'][name]['clusters'].items():
        print('power',name,k,[(round(x['mass']),x['p'],x['elec_mask'].sum()) for x in v['pos']],[(round(x['mass']),x['p'],x['elec_mask'].sum()) for x in v['neg']], v['pos_minp'], v['neg_minp'])
for band in R['psi']:
    for iv in ['maintenance','processing']:
        print(band, iv, {k:(np.round(v.mean(),2), np.round(v.min(),1), np.round(v.max(),1)) for k,v in R['psi'][band][iv].items()})
for band in R['psi_t']:
    for c in R['psi_t'][band]:
        print(band,c,{k:(v.shape, np.round(v.mean(0)[::10],2)) for k,v in R['psi_t'][band][c].items()})
EOF
source $TMPDIR/dev/bin/activate && PYTHONPATH=. python $TMPDIR/dev7b.py
```

```
stream 27.041661500930786 1.242724 GB
{'data_encmain': {'lag_s': 0.33203125, 'shuffled_median_abs_s': 0.0791015625}, 'data_proc': {'lag_s': -0.080078125, 'shuffled_median_abs_s': 0.267578125}} 27.31129813194275
analyse 6.050475597381592 1.242724 GB
n_trials 90
n_correct 86
n_incorrect 4
n_correct_by_cond {1: 26, 2: 28, 3: 32}
neighbours {'adjacent': 5, 'distance': 6, 'none': 0}
pairs [('FOPL_04', 'WL_03', 'L'), ('FOPL_04', 'WL_04', 'L'), ('FOPL_04', 'WL_05', 'L'), ('FOPL_04', 'POPL_02', 'L'), ('FOPL_04', 'POPL_03', 'L'), ('FOPL_05', 'WL_03', 'L'), ('FOPL_05', 'WL_04', 'L'), ('FOPL_05', 'WL_05', 'L'), ('FOPL_05', 'POPL_02', 'L'), ('FOPL_05', 'POPL_03', 'L'), ('FOAL_04', 'WL_03', 'L'), ('FOAL_04', 'WL_04', 'L'), ('FOAL_04', 'WL_05', 'L'), ('FOAL_04', 'POPL_02', 'L'), ('FOAL_04', 'POPL_03', 'L'), ('FOAL_05', 'WL_03', 'L'), ('FOAL_05', 'WL_04', 'L'), ('FOAL_05', 'WL_05', 'L'), ('FOAL_05', 'POPL_02', 'L'), ('FOAL_05', 'POPL_03', 'L')]
erp spatial {'adjacent': ([(114.51091536576442, 0.25)], [(-69.41612235909604, 0.55)]), 'distance': ([(114.51091536576442, 0.26)], [(-69.41612235909604, 0.55)]), 'none': ([(114.51091536576442, 0.14)], [(-69.41612235909604, 0.46)])}
erp temporal {'adjacent': ([(112.07880660661037, 0.21)], [(-141.78480849988057, 0.13)]), 'distance': ([(112.07880660661037, 0.21)], [(-141.78480849988057, 0.13)]), 'none': ([(103.16135739876334, 0.15)], [(-141.78480849988057, 0.05)])}
power spatial adjacent [(1017, 0.01, np.int64(3))] [] 0.01 0.61
power spatial distance [(1017, 0.02, np.int64(3))] [] 0.02 0.62
power spatial none [] [] 0.14 0.44
power temporal adjacent [(2708, 0.0, np.int64(3))] [(-709, 0.01, np.int64(3))] 0.0 0.01
power temporal distance [(2708, 0.0, np.int64(3))] [(-709, 0.01, np.int64(3))] 0.0 0.01
power temporal none [(1111, 0.0, np.int64(1)), (645, 0.02, np.int64(1))] [(-520, 0.01, np.int64(1))] 0.0 0.01
delta-theta maintenance {'a': (np.float64(-0.52), np.float64(-2.9), np.float64(1.8)), 'b': (np.float64(12.55), np.float64(-17.2), np.float64(
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('fcx3.py').read()
old=s[s.index("    out = {}\n    for k in obs:\n        zs = []"):s.index("        out[k] = np.mean(zs, axis=0)")]
new='''    out = {}
    for k in obs:
        zs = []
        for _ in range(n_sets):
            s1 = np.zeros(obs[k].shape)
            s2 = np.zeros(obs[k].shape)
            for p in range(n_perm):
                p1 = rng.permutation(nf)
                p2 = rng.permutation(nf)
                v = np.imag(np.conj(ref[k][..., p1]) * ref[k][..., p2]).sum(-1)
                s1 += v
                s2 += v * v
            mean = s1 / n_perm
            sd = np.sqrt((s2 - n_perm * mean ** 2) / (n_perm - 1))
            zs.append((obs[k] - mean) / sd)
'''
s=s.replace(old,new)
open('fcx3.py','w').write(s)
EOF
cat > $TMPDIR/devall.py <<'EOF'
import numpy as np, fcx3, time, resource, pandas as pd, pickle, os, sys
ch=fcx3.channel_table()
subs=sys.argv[1:] or fcx3.SUBJECTS
for sid in subs:
    t0=time.time()
    c=ch[ch.subject==sid].reset_index(drop=True)
    S=fcx3.stream_subject(sid, list(c.label))
    t1=time.time()
    J=fcx3.jitter_check(S)
    R=fcx3.analyse_subject(S,c)
    meta={k:S[k] for k in ['members','primary_shape','primary_keys','fs','trials','clock','elec_labels','primary_samples']}
    meta['grid']=list(S['grid'].keys())
    meta['epochs']={k:{'shape':S[k]['x'].shape,'t0':S[k]['time'][0],'t1':S[k]['time'][-1],'eq':S[k]['time_all_equal'],'nlab':len(S[k]['labels_all']),'hdr':S[k]['hdr_nSamples'],'min':float(S[k]['x'].min()),'max':float(S[k]['x'].max()),'sd':float(S[k]['x'].std()),'ti_eq_table':bool(np.array_equal(S[k]['trialinfo'],S['trials'].iloc[:,:6].values))} for k in ['data_pre','data_encmain','data_proc']}
    meta['jitter']=J
    del S
    pickle.dump((meta,R),open(os.environ['TMPDIR']+f'/res_{sid}.pkl','wb'))
    print(sid,'stream',round(t1-t0),'analyse',round(time.time()-t1),'maxrss GB',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6, flush=True)
EOF
date -u; source $TMPDIR/dev/bin/activate && PYTHONPATH=. python $TMPDIR/devall.py s7 s4
```

```
Exit code 1
Sun Nov  8 19:29:03 UTC 2026
s7 stream 26 analyse 17 maxrss GB 1.242908
Traceback (most recent call last):
  File "/tmp/claude-1001/devall.py", line 7, in <module>
    S=fcx3.stream_subject(sid, list(c.label))
  File "entries/crcns-fcx-3-johnson-2019/fcx3.py", line 186, in stream_subject
    out.update(_read_derived(b, analysed))
               ~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "entries/crcns-fcx-3-johnson-2019/fcx3.py", line 210, in _read_derived
    x = np.stack([h[r][()][:, idx].T for r in refs]).astype("float32")  # trials x ch x time
        ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/numpy/_core/shape_base.py", line 458, in stack
    raise ValueError('all input arrays must have the same shape')
ValueError: all input arrays must have the same shape
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('fcx3.py').read()
old='''            x = np.stack([h[r][()][:, idx].T for r in refs]).astype("float32")  # trials x ch x time
            times = np.stack([h[r][()].ravel() for r in trefs])
            res[key] = {"x": x, "time": times[0], "time_all_equal": bool(np.allclose(times, times[0])),'''
new='''            times = [h[r][()].ravel() for r in trefs]
            fs = float(g["fsample"][()].ravel()[0])
            # trials can differ by a sample or so in length: keep the samples common to all
            t0 = max(t[0] for t in times)
            t1 = min(t[-1] for t in times)
            lens = sorted({len(t) for t in times})
            x = np.stack([h[r][()][:, idx].T[:, (t >= t0 - 0.5 / fs) & (t <= t1 + 0.5 / fs)]
                          for r, t in zip(refs, times)]).astype("float32")  # trials x ch x time
            tm = times[0][(times[0] >= t0 - 0.5 / fs) & (times[0] <= t1 + 0.5 / fs)]
            res[key] = {"x": x, "time": tm, "lengths": lens, "starts": sorted({round(t[0], 6) for t in times}),
                        "time_all_equal": len(lens) == 1,'''
assert old in s
s=s.replace(old,new)
open('fcx3.py','w').write(s)
EOF
sed -i "s/'eq':S\[k\]\['time_all_equal'\]/'eq':S[k]['time_all_equal'],'lengths':S[k]['lengths'],'starts':S[k]['starts']/" $TMPDIR/devall.py
date -u; source $TMPDIR/dev/bin/activate && PYTHONPATH=. python $TMPDIR/devall.py s4 && python -c "
import pickle,os; m,R=pickle.load(open(os.environ['TMPDIR']+'/res_s4.pkl','rb')); print(m['epochs'])"
```

```
Sun Nov  8 19:30:35 UTC 2026
s4 stream 66 analyse 38 maxrss GB 1.702372
{'data_pre': {'shape': (120, 17, 4501), 't0': np.float64(-1.5), 't1': np.float64(3.0), 'eq': True, 'lengths': [4501], 'starts': [np.float64(-1.5)], 'nlab': 29, 'hdr': 793027.0, 'min': -286.5367126464844, 'max': 230.1662139892578, 'sd': 18.271690368652344, 'ti_eq_table': True}, 'data_encmain': {'shape': (120, 17, 4499), 't0': np.float64(-1.5), 't1': np.float64(2.998), 'eq': False, 'lengths': [4499, 4500], 'starts': [np.float64(-1.5)], 'nlab': 29, 'hdr': 793027.0, 'min': -235.59646606445312, 'max': 151.93641662597656, 'sd': 18.063974380493164, 'ti_eq_table': True}, 'data_proc': {'shape': (120, 17, 4501), 't0': np.float64(-1.5), 't1': np.float64(3.0), 'eq': True, 'lengths': [4501], 'starts': [np.float64(-1.5)], 'nlab': 29, 'hdr': 793027.0, 'min': -252.48289489746094, 'max': 230.1662139892578, 'sd': 18.175256729125977, 'ti_eq_table': True}}
```

**Agent calls Bash**

```bash
date -u; source $TMPDIR/dev/bin/activate && cd entries/crcns-fcx-3-johnson-2019 && PYTHONPATH=. python $TMPDIR/devall.py s1 s2 s6 s5 s3; date -u
```

```
Sun Nov  8 19:32:24 UTC 2026
s1 stream 55 analyse 46 maxrss GB 2.275872
s2 stream 81 analyse 64 maxrss GB 3.004708
s6 stream 64 analyse 26 maxrss GB 3.004708
s5 stream 137 analyse 55 maxrss GB 5.345308
Traceback (most recent call last):
  File "/tmp/claude-1001/devall.py", line 7, in <module>
    S=fcx3.stream_subject(sid, list(c.label))
  File "entries/crcns-fcx-3-johnson-2019/fcx3.py", line 181, in stream_subject
    with h5py.File(io.BytesIO(b), "r") as h:
         ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/h5py/_hl/files.py", line 555, in __init__
    fid = make_fid(name, mode, userblock_size, fapl, fcpl, swmr=swmr)
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/h5py/_hl/files.py", line 232, in make_fid
    fid = h5f.open(name, flags, fapl=fapl)
  File "h5py/_objects.pyx", line 54, in h5py._objects.with_phil.wrapper
  File "h5py/_objects.pyx", line 55, in h5py._objects.with_phil.wrapper
  File "h5py/h5f.pyx", line 106, in h5py.h5f.open
OSError: Unable to synchronously open file (file signature not found)
Sun Nov  8 19:42:31 UTC 2026
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; cd $TMPDIR; python - <<'EOF'
import fsspec, tarfile
B='https://crcnsarchive.s3-us-west-2.amazonaws.com/fcx-3/live/data/'
f=fsspec.open(B+'s3.tar.gz', block_size=2**24).open()
tf=tarfile.open(fileobj=f, mode='r|gz')
for m in tf:
    if m.isfile():
        x=tf.extractfile(m); print(m.name, m.size, x.read(140))
EOF
```

```
s3/data_primary.mat 1655986355 b'MATLAB 7.3 MAT-file, Platform: GLNXA64, Created on: Mon Jun  6 16:17:01 2016 HDF5 schema 1.00 .                     \x00\x00\x00\x00\x00\x00\x00\x00\x00\x02IM\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
s3/elec_labels.mat 920 b'MATLAB 5.0 MAT-file, Platform: GLNXA64, Created on: Tue Sep  8 13:14:43 2015                                        \x00\x00\x00\x00\x00\x00\x00\x00\x00\x01IM\x0f\x00\x00\x00\x10\x03\x00\x00x\x9c\xa4\xd8'
s3/s3_MNI_grid.csv 121234 b'#vtkpxElectrodeMultiGridSource File\n#Description\npatient\n#Comment\nno additional comment\n#Number of Grids\n 3 \n#- - - - - - - - - - - - - - - '
s3/data_derived.mat 1944998005 b'MATLAB 7.3 MAT-file, Platform: GLNXA64, Created on: Tue Dec 18 16:00:14 2018 HDF5 schema 1.00 .                     \x00\x00\x00\x00\x00\x00\x00\x00\x00\x02IM\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
s3/summary_file_trial.csv 4758 b'1,1,2,2,1150,420,23330,25232,27784\r\n2,1,2,3,1150,574,29390,31292,33844\r\n3,1,1,1,1150,1445,35600,37501,40054\r\n4,0,2,3,1150,862,42694,44596,47'
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/crcns-fcx-3-johnson-2019 && python - <<'EOF'
s=open('fcx3.py').read()
old='''                elif name == "elec_labels.mat":
                    with h5py.File(io.BytesIO(b), "r") as h:
                        out["elec_labels"] = _cellstr(h, h["elec_labels"])'''
new='''                elif name == "elec_labels.mat":
                    out["elec_labels_format"] = b[:19].decode()
                    if b.startswith(b"MATLAB 7.3"):
                        with h5py.File(io.BytesIO(b), "r") as h:
                            out["elec_labels"] = _cellstr(h, h["elec_labels"])
                    else:  # s3 stores this file as a MATLAB 5 file
                        from scipy.io import loadmat
                        out["elec_labels"] = [str(v) for v in loadmat(io.BytesIO(b), squeeze_me=True)["elec_labels"]]'''
assert old in s; s=s.replace(old,new); open('fcx3.py','w').write(s)
EOF
sed -i "s/meta={k:S\[k\] for k in \['members'/meta={k:S[k] for k in ['elec_labels_format','members'/" $TMPDIR/devall.py
date -u; source $TMPDIR/dev/bin/activate && PYTHONPATH=. python $TMPDIR/devall.py s3; date -u
```

```
Sun Nov  8 19:45:11 UTC 2026
s3 stream 169 analyse 151 maxrss GB 6.8534
Sun Nov  8 19:50:33 UTC 2026
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && cat > $TMPDIR/look.py <<'EOF'
import pickle,os,numpy as np,pandas as pd
D={s:pickle.load(open(os.environ['TMPDIR']+f'/res_{s}.pkl','rb')) for s in [f's{i}' for i in range(1,8)]}
for s,(m,R) in D.items():
    print(s, 'fs',m['fs'],'members',m['members'],'prim',m['primary_shape'],'labels',len(m['elec_labels']),'grid',m['grid'])
    print('   epochs',{k:(v['shape'],v['lengths'],v['nlab'],v['hdr'],v['ti_eq_table']) for k,v in m['epochs'].items()})
    print('   clock', m['clock'].groupby('epoch').agg(rmin=('r','min'),omin=('offset_s','min'),omax=('offset_s','max'),ref=('reference','mean')).round(4).to_dict('index'))
    print('   jitter', m['jitter'])
    tt=m['trials']; print('   trials',len(tt),'correct',R['n_correct'],'incorrect',R['n_incorrect'],R['n_correct_by_cond'],'trial range',tt.trial.min(),tt.trial.max(),'pairs',len(R['pairs']),'nb',R['neighbours'])
EOF
python $TMPDIR/look.py
```

```
Exit code 1
s1 fs 1000.0 members [('s1_MNI_grid.csv', 36725), ('data_primary.mat', 570399399), ('elec_labels.mat', 31408), ('data_derived.mat', 580473307), ('summary_file_trial.csv', 4826)] prim (1140000, 72) labels 72 grid ['LIHA', 'LIHP', 'LLFP', 'LLTA', 'LLTP', 'LMT', 'LOF', 'RIHA', 'RIHP', 'RLFP', 'RLTA', 'RLTP', 'RMT', 'ROF']
   epochs {'data_pre': ((120, 23, 4501), [4501], 46, 1140000.0, True), 'data_encmain': ((120, 23, 4498), [4498, 4499, 4500], 46, 1140000.0, True), 'data_proc': ((120, 23, 4501), [4501], 46, 1140000.0, True)}
   clock {'data_encmain': {'rmin': 0.9986, 'omin': -1.501, 'omax': -1.501, 'ref': 1.0}, 'data_pre': {'rmin': 0.9994, 'omin': -1.401, 'omax': -1.401, 'ref': 1.0}, 'data_proc': {'rmin': 0.9993, 'omin': -1.801, 'omax': -1.801, 'ref': 1.0}}
   jitter {'data_encmain': {'lag_s': -0.008, 'shuffled_median_abs_s': 0.10500000000000001}, 'data_proc': {'lag_s': -0.344, 'shuffled_median_abs_s': 0.20850000000000002}}
   trials 120 correct 102 incorrect 18 {1: 33, 2: 36, 3: 33} trial range 1 120 pairs 21 nb {'adjacent': 13, 'distance': 13, 'none': 0}
s2 fs 1000.0 members [('data_primary.mat', 693471765), ('elec_labels.mat', 42064), ('data_derived.mat', 804363187), ('summary_file_trial.csv', 4807), ('s2_MNI_grid.csv', 49877)] prim (940001, 96) labels 96 grid ['CI', 'CS', 'G', 'LLF', 'LLP', 'RFP', 'RMT', 'RSF', 'RSP']
   epochs {'data_pre': ((120, 32, 4501), [4501], 64, 940001.0, True), 'data_encmain': ((120, 32, 4498), [4498, 4499], 64, 940001.0, True), 'data_proc': ((120, 32, 4501), [4501], 64, 940001.0, True)}
   clock {'data_encmain': {'rmin': 0.9992, 'omin': -1.501, 'omax': -1.501, 'ref': 1.0}, 'data_pre': {'rmin': 0.999, 'omin': -1.401, 'omax': -1.401, 'ref': 1.0}, 'data_proc': {'rmin': 0.9987, 'omin': -1.801, 'omax': -1.801, 'ref': 1.0}}
   jitter {'data_encmain': {'lag_s': 0.402, 'shuffled_median_abs_s': 0.082}, 'data_proc': {'lag_s': -0.419, 'shuffled_median_abs_s': 0.233}}
   trials 120 correct 95 incorrect 25 {1: 35, 2: 35, 3: 25} trial rang
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && cat > $TMPDIR/s6.py <<'EOF'
import numpy as np, fcx3, pandas as pd
from scipy import signal
ch=fcx3.channel_table(); c=ch[ch.subject=='s6'].reset_index(drop=True)
import fcx3 as F
# monkeypatch to keep primary
orig=F._clock_check
keep={}
def cc(sub, primary, *a): keep['p']=primary; return orig(sub, primary, *a)
F._clock_check=cc
S=F.stream_subject('s6', list(c.label))
P=keep['p']; labs=S['elec_labels']; print(labs)
print(S['data_proc']['labels_all'])
tt=S['trials']; print(tt.head()); fs=S['fs']
y=S['data_proc']['x'][0,0].astype(float); lab=c.label[0]; print('label',lab)
i=labs.index(lab)
best=[]
for j in range(len(labs)):
    for sig,name in [(P[i]-P[j],'i-j')] if j!=i else [(P[i],'mono')]:
        r,k=F._best_lag(sig,y); best.append((r,labs[j],name,k,(k-tt.proc_start[0])/fs))
best.sort(reverse=True); print(best[:5])
# primary vs trial table: check jitter ERP
EOF
cd entries/crcns-fcx-3-johnson-2019 && PYTHONPATH=. python $TMPDIR/s6.py
```

```
['PT1', 'PT2', 'PT3', 'PT4', 'PT5', 'PT6', 'PT7', 'PT8', 'PT9', 'PT10', 'PT11', 'PT12', 'OF1', 'OF2', 'OF3', 'OF4', 'OF5', 'OF6', 'OF7', 'OF8', 'OF9', 'OF10', 'OF11', 'OF12', 'OF13', 'OF14', 'OF15', 'OF16', 'ID1', 'ID2', 'ID3', 'ID4', 'ID5', 'ID6', 'ID7', 'ID8', 'ID9', 'ID10', 'CD1', 'CD2', 'CD3', 'CD4', 'CD5', 'CD6', 'FG1', 'FG2', 'FG3', 'FG4', 'FG5', 'FG6', 'FG7', 'FG8', 'FG9', 'FG10', 'FG11', 'FG12', 'FG13', 'FG14', 'FG15', 'FG16', 'FG17', 'FG18', 'FG19', 'FG20', 'FG21', 'FG22', 'FG23', 'FG24', 'FG25', 'FG26', 'FG27', 'FG28', 'FG29', 'FG30', 'FG31', 'FG32', 'FG33', 'FG34', 'FG35', 'FG36', 'FG37', 'FG38', 'FG39', 'FG40', 'FG41', 'FG42', 'FG43', 'FG44', 'FG45', 'FG46', 'FG47', 'FG48', 'FG49', 'FG50', 'FG51', 'FG52', 'FG53', 'FG54', 'FG55', 'FG56', 'FG57', 'FG58', 'FG59', 'FG60', 'FG61', 'FG62', 'FG63', 'FG64']
['PT2', 'PT3', 'PT4', 'PT5', 'PT6', 'PT12', 'OF2', 'OF3', 'OF5', 'OF6', 'OF7', 'OF9', 'OF10', 'OF11', 'OF13', 'OF14', 'OF15', 'FG19', 'FG20', 'FG21', 'FG22', 'FG26', 'FG27', 'FG28', 'FG29', 'FG30', 'FG31', 'FG32', 'FG33', 'FG34', 'FG35', 'FG36', 'FG37', 'FG38', 'FG39', 'FG40', 'FG41', 'FG42', 'FG43', 'FG44', 'FG45', 'FG46', 'FG47', 'FG48', 'FG49', 'FG50', 'FG51', 'FG52', 'FG53', 'FG54', 'FG55', 'FG56', 'FG57', 'FG58', 'FG59', 'FG60', 'FG61', 'FG62', 'FG63', 'FG64']
   trial  correct  type  ...  pre_start  encmain_start  proc_start
0      1        0     2  ...       8852          10753       13053
1      2        1     2  ...      18267          20168       22718
2      3        0     2  ...      28249          30151       32450
3      4        0     1  ...      35277          37179       39728
4      5        1     1  ...      52254          54156       56705

[5 rows x 9 columns]
label FG27
[(0.9999973503791254, 'FG19', 'i-j', 11252, np.float64(-1.801)), (0.5332944957682003, 'FG20', 'i-j', 11251, np.float64(-1.802)), (0.44787158194450166, 'FG22', 'i-j', 556429, np.float64(543.376)), (0.4304606011930198, 'FG12', 'i-j', 11252, np.float64(-1.801)), (0.430042560
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('fcx3.py').read()
a=s.index("def jitter_check(S):"); b=s.index("def analyse_subject(")
new='''def jitter_check(S, max_lag=0.45):
    """Timing contrast: the response to the test cue follows the delay jitter. In data_encmain the
    test cue appears 0.6 s + jitter after time 0 (0.6 s is the end of the second stimulus in the
    scripts' maintenance window, 900 or 1150 ms the jitter). The trial-mean signals of the 1150-ms
    trials, low-passed at 30 Hz, are shifted against those of the 900-ms trials, and the shift that
    best aligns them over all channels (window 1.3 to 2.3 s of the 900-ms trials, covering the cue
    onset at 1.5 s) should be 0.25 s; with the jitter labels shuffled it should not."""
    fs = S["fs"]
    e = S["data_encmain"]
    jit = S["data_encmain"]["trialinfo"][:, 4]
    x = lowpass_fir(e["x"].astype("float64"), fs)
    w = win_index(e["time"], (1.3, 2.3))
    lags = np.arange(-int(max_lag * fs), int(max_lag * fs) + 1)

    def best(j):
        a = x[j == 900].mean(0)[:, w]
        a = (a - a.mean(1, keepdims=True)).ravel()
        b_all = x[j == 1150].mean(0)
        r = []
        for L in lags:
            b = b_all[:, w + L]
            b = (b - b.mean(1, keepdims=True)).ravel()
            r.append(a @ b / np.sqrt((a @ a) * (b @ b)))
        r = np.array(r)
        return float(lags[np.argmax(r)] / fs), float(r.max())

    rng = np.random.default_rng(seed("jitter", S["subject"]))
    lag, r = best(jit)
    shuffled = [best(rng.permutation(jit))[0] for _ in range(20)]
    return {"lag_s": lag, "r": r, "shuffled_lags_s": shuffled,
            "n_900": int((jit == 900).sum()), "n_1150": int((jit == 1150).sum())}


'''
s=s[:a]+new+s[b:]
open('fcx3.py','w').write(s)
EOF
source $TMPDIR/dev/bin/activate && cat > $TMPDIR/jt.py <<'EOF'
import numpy as np, fcx3, sys
ch=fcx3.channel_table()
for sid in sys.argv[1:]:
    c=ch[ch.subject==sid].reset_index(drop=True)
    S=fcx3.stream_subject(sid, list(c.label), check_channels=0)
    print(sid, fcx3.jitter_check(S), flush=True)
EOF
PYTHONPATH=. python $TMPDIR/jt.py s7 s4
```

```
s7 {'lag_s': -0.203125, 'r': 0.31163642918211465, 'shuffled_lags_s': [-0.158203125, -0.154296875, 0.158203125, -0.138671875, 0.16796875, 0.13671875, 0.06640625, 0.13671875, 0.17578125, 0.146484375, 0.2421875, 0.109375, 0.1875, 0.224609375, 0.255859375, 0.1640625, 0.20703125, 0.1484375, -0.12890625, 0.244140625], 'n_900': 46, 'n_1150': 44}
s4 {'lag_s': 0.45, 'r': 0.3934724467498991, 'shuffled_lags_s': [0.005, -0.001, -0.001, -0.001, 0.006, -0.003, -0.002, -0.006, 0.0, 0.006, -0.001, 0.008, -0.007, 0.005, -0.001, 0.004, -0.001, 0.002, 0.009, -0.003], 'n_900': 60, 'n_1150': 60}
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && cat > $TMPDIR/jt2.py <<'EOF'
import numpy as np, fcx3, sys
from scipy import signal
ch=fcx3.channel_table()
for sid in sys.argv[1:]:
    c=ch[ch.subject==sid].reset_index(drop=True)
    S=fcx3.stream_subject(sid, list(c.label), check_channels=0)
    e=S['data_encmain']; fs=S['fs']; t=e['time']; jit=e['trialinfo'][:,4]
    x=e['x'].astype(float)
    hi=min(150, fs/2-10)
    b,a=signal.butter(4,[70,hi],btype='band',fs=fs)
    env=np.abs(signal.hilbert(signal.filtfilt(b,a,x,axis=-1),axis=-1))
    env=signal.filtfilt(*signal.butter(2,10,fs=fs),env,axis=-1)
    env=np.log(env+1e-9)
    env=env-env[:,:,fcx3.win_index(t,(0.9,1.4))].mean(-1,keepdims=True)
    lp=fcx3.lowpass_fir(x,fs,fc=15); lp=lp-lp[:,:,fcx3.win_index(t,(1.2,1.45))].mean(-1,keepdims=True)
    for name,y in [('hfa',env),('erp',lp)]:
        w=fcx3.win_index(t,(1.3,2.3)); lags=np.arange(-int(.45*fs),int(.45*fs)+1)
        def best(j):
            A=y[j==900].mean(0)[:,w]; A=(A-A.mean(1,keepdims=True)).ravel(); B=y[j==1150].mean(0); r=[]
            for L in lags:
                Bb=B[:,w+L]; Bb=(Bb-Bb.mean(1,keepdims=True)).ravel(); r.append(A@Bb/np.sqrt(A@A*Bb@Bb))
            return lags[np.argmax(r)]/fs, max(r)
        rng=np.random.default_rng(0)
        print(sid,name,best(jit),[round(best(rng.permutation(jit))[0],2) for _ in range(8)],flush=True)
EOF
PYTHONPATH=. python $TMPDIR/jt2.py s7 s4
```

```
/tmp/claude-1001/jt2.py:13: RuntimeWarning: invalid value encountered in log
  env=np.log(env+1e-9)
s7 hfa (np.float64(0.328125), np.float64(0.23819111815184876)) [np.float64(0.28), np.float64(-0.4), np.float64(-0.0), np.float64(-0.43), np.float64(-0.24), np.float64(0.27), np.float64(0.44), np.float64(-0.22)]
s7 erp (np.float64(-0.201171875), np.float64(0.32907253519395885)) [np.float64(0.19), np.float64(0.15), np.float64(0.3), np.float64(-0.15), np.float64(0.3), np.float64(0.0), np.float64(-0.15), np.float64(0.2)]
/tmp/claude-1001/jt2.py:13: RuntimeWarning: invalid value encountered in log
  env=np.log(env+1e-9)
s4 hfa (np.float64(0.45), np.float64(0.7342720136182739)) [np.float64(0.04), np.float64(-0.03), np.float64(0.0), np.float64(-0.01), np.float64(-0.01), np.float64(0.05), np.float64(-0.02), np.float64(-0.04)]
s4 erp (np.float64(0.45), np.float64(0.4132613245957741)) [np.float64(-0.0), np.float64(0.0), np.float64(-0.0), np.float64(0.01), np.float64(0.01), np.float64(0.0), np.float64(0.0), np.float64(-0.0)]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && cat > $TMPDIR/jt3.py <<'EOF'
import numpy as np, fcx3, sys
from scipy import signal
ch=fcx3.channel_table()
for sid in sys.argv[1:]:
    c=ch[ch.subject==sid].reset_index(drop=True)
    S=fcx3.stream_subject(sid, list(c.label), check_channels=0)
    for key in ['data_encmain','data_proc']:
        e=S[key]; fs=S['fs']; t=e['time']; jit=e['trialinfo'][:,4]
        x=e['x'].astype(float)
        b,a=signal.butter(4,[70,150],btype='band',fs=fs)
        env=np.abs(signal.hilbert(signal.filtfilt(b,a,x,axis=-1),axis=-1))
        env=signal.filtfilt(*signal.butter(2,10,fs=fs),env,axis=-1)
        env=env/env.mean(-1,keepdims=True)
        ts=np.arange(-1.4,3.0,0.1); idx=[np.argmin(abs(t-v)) for v in ts]
        for j in (900,1150):
            print(sid,key,j,' '.join(f'{v:.2f}' for v in env[jit==j].mean((0,1))[idx]))
        print('t', ' '.join(f'{v:.1f}' for v in ts))
EOF
PYTHONPATH=. python $TMPDIR/jt3.py s4
```

```
s4 data_encmain 900 0.98 0.98 0.98 0.98 0.99 0.98 1.00 0.99 1.00 0.98 0.98 1.01 1.00 1.00 0.99 1.01 1.06 1.08 1.08 1.07 1.02 1.01 1.01 0.99 0.97 0.98 0.96 0.96 0.98 0.96 0.97 0.99 1.02 1.08 1.09 1.05 1.04 1.01 0.99 0.97 0.99 0.99 0.98 0.97
s4 data_encmain 1150 0.97 0.98 0.98 0.98 0.99 1.00 1.02 0.99 0.99 0.98 0.99 0.99 0.98 0.97 1.00 1.00 0.99 0.98 1.02 1.07 1.08 1.07 1.04 1.02 1.01 0.99 0.99 0.99 0.97 0.97 0.97 0.96 0.97 0.98 0.97 0.98 0.98 1.02 1.07 1.09 1.07 1.04 1.00 0.99
t -1.4 -1.3 -1.2 -1.1 -1.0 -0.9 -0.8 -0.7 -0.6 -0.5 -0.4 -0.3 -0.2 -0.1 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0 1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9 2.0 2.1 2.2 2.3 2.4 2.5 2.6 2.7 2.8 2.9
s4 data_proc 900 1.04 1.02 1.02 1.01 0.98 0.99 0.97 0.98 0.99 0.97 0.98 1.00 1.04 1.10 1.11 1.06 1.05 1.03 1.00 0.99 1.00 1.00 0.99 0.98 0.98 0.99 0.99 0.97 0.98 0.99 0.99 0.97 0.96 0.98 1.01 0.99 0.99 1.00 1.00 0.98 1.02 1.01 1.00 1.00
s4 data_proc 1150 1.05 1.03 1.02 1.03 1.00 0.99 1.00 0.99 0.99 0.99 0.98 0.99 1.01 1.00 1.02 1.09 1.11 1.11 1.04 1.05 1.01 1.04 0.98 1.01 0.98 0.99 0.96 0.97 0.97 0.97 0.99 1.00 0.96 0.98 0.98 0.98 0.97 0.99 0.97 0.97 0.99 0.98 0.99 1.01
t -1.4 -1.3 -1.2 -1.1 -1.0 -0.9 -0.8 -0.7 -0.6 -0.5 -0.4 -0.3 -0.2 -0.1 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0 1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9 2.0 2.1 2.2 2.3 2.4 2.5 2.6 2.7 2.8 2.9
```

**Agent calls Bash**

```bash
date -u; source $TMPDIR/dev/bin/activate && cat > $TMPDIR/jt4.py <<'EOF'
import numpy as np, fcx3, sys
from scipy import signal
ch=fcx3.channel_table()
W={'data_pre':(0.6,1.6),'data_encmain':(-0.3,1.0),'data_proc':(-0.9,0.7)}
for sid in sys.argv[1:]:
    c=ch[ch.subject==sid].reset_index(drop=True)
    S=fcx3.stream_subject(sid, list(c.label), check_channels=0)
    for key in W:
        e=S[key]; fs=S['fs']; t=e['time']; jit=e['trialinfo'][:,4]
        x=e['x'].astype(float)
        b,a=signal.butter(4,[70,min(150,fs/2-20)],btype='band',fs=fs)
        env=np.abs(signal.hilbert(signal.filtfilt(b,a,x,axis=-1),axis=-1))
        env=signal.filtfilt(*signal.butter(2,10,fs=fs),env,axis=-1)
        env=env/env.mean(-1,keepdims=True)
        w=fcx3.win_index(t,W[key]); lags=np.arange(-int(.4*fs),int(.4*fs)+1)
        def best(j):
            A=env[j==900].mean(0)[:,w]; A=(A-A.mean(1,keepdims=True)).ravel(); B=env[j==1150].mean(0); r=[]
            for L in lags:
                Bb=B[:,w+L]; Bb=(Bb-Bb.mean(1,keepdims=True)).ravel(); r.append(A@Bb/np.sqrt(A@A*Bb@Bb))
            return round(lags[np.argmax(r)]/fs,3), round(max(r),2)
        rng=np.random.default_rng(0)
        print(sid,key,best(jit),[best(rng.permutation(jit))[0] for _ in range(6)],flush=True)
EOF
PYTHONPATH=. python $TMPDIR/jt4.py s4 s7 s1
```

```
Sun Nov  8 19:56:28 UTC 2026
s4 data_pre (np.float64(0.009), np.float64(0.32)) [np.float64(0.014), np.float64(-0.048), np.float64(-0.041), np.float64(-0.052), np.float64(-0.004), np.float64(0.037)]
s4 data_encmain (np.float64(0.263), np.float64(0.65)) [np.float64(0.093), np.float64(-0.089), np.float64(-0.102), np.float64(-0.083), np.float64(0.105), np.float64(-0.081)]
s4 data_proc (np.float64(0.256), np.float64(0.76)) [np.float64(0.062), np.float64(-0.079), np.float64(0.006), np.float64(-0.038), np.float64(-0.018), np.float64(-0.024)]
s7 data_pre (np.float64(0.383), np.float64(0.24)) [np.float64(-0.398), np.float64(-0.092), np.float64(-0.088), np.float64(-0.398), np.float64(0.088), np.float64(0.082)]
s7 data_encmain (np.float64(-0.023), np.float64(0.24)) [np.float64(0.135), np.float64(0.037), np.float64(0.166), np.float64(-0.043), np.float64(-0.045), np.float64(0.09)]
s7 data_proc (np.float64(-0.016), np.float64(0.22)) [np.float64(0.012), np.float64(0.006), np.float64(-0.088), np.float64(-0.301), np.float64(-0.004), np.float64(0.107)]
s1 data_pre (np.float64(-0.396), np.float64(0.05)) [np.float64(-0.289), np.float64(0.4), np.float64(-0.374), np.float64(-0.2), np.float64(-0.065), np.float64(-0.305)]
s1 data_encmain (np.float64(-0.146), np.float64(0.05)) [np.float64(-0.075), np.float64(0.387), np.float64(0.184), np.float64(-0.239), np.float64(0.368), np.float64(0.151)]
s1 data_proc (np.float64(0.29), np.float64(0.15)) [np.float64(-0.306), np.float64(0.168), np.float64(0.388), np.float64(0.073), np.float64(0.267), np.float64(-0.304)]
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('fcx3.py').read()
a=s.index("def _clock_check("); b=s.index("# --------------------------------------------------------------------------- neighbours")
new='''def _clock_check(sub, primary, analysed, n_ch, n_tr, rng):
    """Where the derived epochs lie in the continuous data.

    1. For n_ch analysed channels and the first trial of each epoch, the derived trace is searched
       for within 4 s of the trial table's start column, against the difference of the channel's
       contact with every other contact; this gives the offset of each epoch from its column.
    2. At that offset, every analysed channel is matched, on n_tr random trials, against the
       difference with every other contact: the best one is the channel's bipolar reference, and
       its correlation shows whether the derived trace is that difference.
    """
    fs = sub["fs"]
    labs = sub["elec_labels"]
    cols = {"data_pre": "pre_start", "data_encmain": "encmain_start", "data_proc": "proc_start"}
    tt = sub["trials"]
    found = []
    offsets = {}
    for key, col in cols.items():
        ep = sub[key]
        for c in list(rng.choice(len(analysed), size=min(n_ch, len(analysed)), replace=False)):
            i = labs.index(analysed[c])
            y = ep["x"][0, c].astype(float)
            start = int(tt[col].iloc[0])
            lo = max(0, start - int(4 * fs))
            hi = min(primary.shape[1], start + int(4 * fs) + len(y))
            best = None
            for j in range(len(labs)):
                sig = primary[i, lo:hi] - (primary[j, lo:hi] if j != i else 0)
                r, k = _best_lag(sig, y)
                if best is None or r > best[0]:
                    best = (r, labs[j], lo + k)
            found.append({"epoch": key, "channel": analysed[c], "trial": int(tt["trial"].iloc[0]),
                          "r": best[0], "reference": best[1], "offset_s": (best[2] - start) / fs})
        offsets[key] = int(round(np.median([f["offset_s"] for f in found if f["epoch"] == key]) * fs))
    rows = []
    trials = rng.choice(len(tt), size=min(n_tr, len(tt)), replace=False)
    for c, lab in enumerate(analysed):
        i = labs.index(lab)
        rs = np.zeros(len(labs))
        n_ok = 0
        for key, col in cols.items():
            ep = sub[key]
            for t in trials:
                start = int(tt[col].iloc[t]) + offsets[key]
                y = ep["x"][t, c].astype(float)
                seg = primary[:, start:start + len(y)].astype(float)
                if seg.shape[1] != len(y):
                    continue
                d = seg[i][None, :] - seg
                d[i] = seg[i]
                d = d - d.mean(1, keepdims=True)
                yy = y - y.mean()
                rs += d @ yy / (np.linalg.norm(d, axis=1) * np.linalg.norm(yy) + 1e-12)
                n_ok += 1
        rs /= max(n_ok, 1)
        j = int(np.argmax(rs))
        rows.append({"channel": lab, "reference": labs[j], "r": float(rs[j]), "n_traces": n_ok})
    return {"search": pd.DataFrame(found), "offsets_s": {k: v / fs for k, v in offsets.items()},
            "channels": pd.DataFrame(rows)}


'''
s=s[:a]+new+s[b:]
# jitter check: HFA based
a=s.index("def jitter_check("); b=s.index("def analyse_subject(")
new='''JITTER_WINDOWS = {"data_pre": (0.6, 1.6), "data_encmain": (-0.3, 1.0), "data_proc": (-0.9, 0.7)}


def jitter_check(S, max_lag=0.4, n_shuffle=20):
    """Timing contrast between the trials with 900-ms and 1150-ms delays.

    The trial table puts the encoding epoch (data_encmain) at a fixed 1.9 s after the pretrial start
    and the processing epoch at 0.6 s + jitter + 0.8 s after the encoding start, so if the columns
    mark the events, the responses inside each window below occur at the same times in both groups:
    the start screen (data_pre, 0.6 to 1.6 s), the two stimuli (data_encmain, -0.3 to 1.0 s) and
    the test cue and its offset (data_proc, -0.9 to 0.7 s; the cue is on from -0.5 to 0.3 s). The
    measure is the 70-150 Hz amplitude (Hilbert envelope of a 4th-order Butterworth band, smoothed at
    10 Hz, each trace divided by its mean), averaged over trials per group; the shift of the
    1150-ms group that best aligns it with the 900-ms group over all channels is reported, with
    the shifts found for shuffled jitter labels as the reference. (A check, not a method of the
    paper; the band and windows are standard choices.)"""
    out = {}
    fs = S["fs"]
    for key, win in JITTER_WINDOWS.items():
        e = S[key]
        jit = e["trialinfo"][:, 4]
        x = e["x"].astype("float64")
        b, a = signal.butter(4, [70, min(150, fs / 2 - 20)], btype="band", fs=fs)
        env = np.abs(signal.hilbert(signal.filtfilt(b, a, x, axis=-1), axis=-1))
        env = signal.filtfilt(*signal.butter(2, 10, fs=fs), env, axis=-1)
        env = env / env.mean(-1, keepdims=True)
        w = win_index(e["time"], win)
        lags = np.arange(-int(max_lag * fs), int(max_lag * fs) + 1)

        def best(j):
            A = env[j == 900].mean(0)[:, w]
            A = (A - A.mean(1, keepdims=True)).ravel()
            B = env[j == 1150].mean(0)
            r = []
            for L in lags:
                Bb = B[:, w + L]
                Bb = (Bb - Bb.mean(1, keepdims=True)).ravel()
                r.append(A @ Bb / np.sqrt((A @ A) * (Bb @ Bb)))
            k = int(np.argmax(r))
            return float(lags[k] / fs), float(r[k])

        rng = np.random.default_rng(seed("jitter", S["subject"], key))
        lag, r = best(jit)
        sh = [best(rng.permutation(jit)) for _ in range(n_shuffle)]
        out[key] = {"lag_s": lag, "r": r, "shuffled_abs_lag_max_s": max(abs(v[0]) for v in sh),
                    "shuffled_r_max": max(v[1] for v in sh)}
        del env, x
    return out


'''
s=s[:a]+new+s[b:]
# grid alias + positions from found references
old='''def bipolar_positions(labels, grid):'''
new='''GRID_ALIAS = {"RH": "HD_Grid"}  # s3: contacts RH1..RH256 are the 256-contact grid 'HD_Grid' of its MNI file


def bipolar_positions(labels, grid, references=None):'''
s=s.replace(old,new)
old='''    pos = np.full((len(labels), 3), np.nan)
    spacing = np.full(len(labels), np.nan)
    for i, lab in enumerate(labels):
        pre, num = split_label(lab)
        g = grid.get(pre) if grid else None
        if g is None or num - 1 >= len(g["pos"]) or num - 2 < 0:
            continue
        pos[i] = (g["pos"][num - 1] + g["pos"][num - 2]) / 2
        spacing[i] = g["spacing"]
    return pos, spacing'''
new='''    pos = np.full((len(labels), 3), np.nan)
    spacing = np.full(len(labels), np.nan)

    def contact(lab):
        pre, num = split_label(lab)
        g = grid.get(pre, grid.get(GRID_ALIAS.get(pre, ""))) if grid else None
        if g is None or not 1 <= num <= len(g["pos"]):
            return None, None
        return g["pos"][num - 1], g["spacing"]

    for i, lab in enumerate(labels):
        p1, sp = contact(lab)
        ref = references[i] if references is not None else None
        p2, _ = contact(ref) if ref else (None, None)
        if p1 is None or p2 is None:
            continue
        pos[i] = (p1 + p2) / 2
        spacing[i] = sp
    return pos, spacing'''
assert old in s; s=s.replace(old,new)
old='''def neighbours(labels, grid=None, reading="adjacent"):'''
new='''def neighbours(labels, grid=None, reading="adjacent", references=None):'''
s=s.replace(old,new)
s=s.replace("    pos, spacing = bipolar_positions(labels, grid)\n","    pos, spacing = bipolar_positions(labels, grid, references)\n")
s=s.replace('''    nb = {k: neighbours(labels, S.get("grid"), k) for k in NB_READINGS}''','''    refs = list(S["clock"]["channels"].reference) if "clock" in S else None
    nb = {k: neighbours(labels, S.get("grid"), k, refs) for k in NB_READINGS}''')
open('fcx3.py','w').write(s)
EOF
grep -n "1.5 times\|contact numbered" fcx3.py
```

```
311:    1.5 times the lead's stated contact spacing in the s<n>_MNI_grid.csv positions (an assumption);
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && cat > $TMPDIR/ck.py <<'EOF'
import numpy as np, fcx3, sys, time
ch=fcx3.channel_table()
for sid in sys.argv[1:]:
    t0=time.time()
    c=ch[ch.subject==sid].reset_index(drop=True)
    S=fcx3.stream_subject(sid, list(c.label))
    t1=time.time()
    ck=S['clock']; print(sid, round(t1-t0), ck['offsets_s']); print(ck['search'].to_string()); print(ck['channels'].to_string())
    print(fcx3.jitter_check(S), round(time.time()-t1))
    refs=list(ck['channels'].reference)
    for k in fcx3.NB_READINGS: print(k, fcx3.neighbours(list(c.label),S['grid'],k,refs).tolist())
    print({g:(v['dims'],v['spacing'],len(v['pos'])) for g,v in S['grid'].items()})
EOF
PYTHONPATH=. python $TMPDIR/ck.py s7 s6 2>&1 | tail -60
```

```
s7 27 {'data_pre': -1.40234375, 'data_encmain': -1.501953125, 'data_proc': -1.802734375}
          epoch  channel  trial         r reference  offset_s
0      data_pre  FOAL_05      1  0.999987   FOAL_04 -1.402344
1      data_pre    WL_05      1  0.999995     WL_04 -1.402344
2  data_encmain  POPL_03      1  0.999823   POPL_02 -1.501953
3  data_encmain  FOPL_05      1  0.999984   FOPL_04 -1.501953
4     data_proc  POPL_03      1  0.999930   POPL_02 -1.802734
5     data_proc  FOPL_04      1  0.998947   FOPL_03 -1.802734
   channel reference    r  n_traces
0  FOPL_04   FOPL_03  1.0        24
1    WL_03     WL_02  1.0        24
2  FOPL_05   FOPL_04  1.0        24
3    WL_04     WL_03  1.0        24
4  FOAL_04   FOAL_03  1.0        24
5    WL_05     WL_04  1.0        24
6  FOAL_05   FOAL_04  1.0        24
7  POPL_02   POPL_01  1.0        24
8  POPL_03   POPL_02  1.0        24
{'data_pre': {'lag_s': 0.3828125, 'r': 0.24295239927751605, 'shuffled_abs_lag_max_s': 0.357421875, 'shuffled_r_max': 0.29588502510897446}, 'data_encmain': {'lag_s': -0.0234375, 'r': 0.24052523732013395, 'shuffled_abs_lag_max_s': 0.3984375, 'shuffled_r_max': 0.3129853864102657}, 'data_proc': {'lag_s': -0.015625, 'r': 0.21965151394424648, 'shuffled_abs_lag_max_s': 0.345703125, 'shuffled_r_max': 0.3003456022086861}} 2
adjacent [[0, 2], [1, 3], [3, 5], [4, 6], [7, 8]]
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && cat > $TMPDIR/look2.py <<'EOF'
import pickle,os,numpy as np,pandas as pd
D={s:pickle.load(open(os.environ['TMPDIR']+f'/res_{s}.pkl','rb'))[1] for s in [f's{i}' for i in range(1,8)]}
for s,R in D.items():
    print(s, 'ERP', {n:{k:(round(v['pos'][0][1],3) if v['pos'] else None, round(v['neg'][0][1],3) if v['neg'] else None) for k,v in R['erp'][n].items()} for n in R['erp']})
    for n in R['power']:
        for k,v in R['power'][n]['clusters'].items():
            nel=len(R['labels'])
            pe=np.zeros(nel,bool); ne=np.zeros(nel,bool)
            for x in v['pos']: pe|=x['elec_mask']
            for x in v['neg']: ne|=x['elec_mask']
            print('  power',n,k,'pos %d/%d'%(pe.sum(),nel),'neg %d'%ne.sum(), 'minp',v['pos_minp'],v['neg_minp'])
    for band in R['psi']:
        print('  psi',band,{iv:{k:round(float(np.mean(v)),2) for k,v in R['psi'][band][iv].items()} for iv in ['maintenance','processing']})
EOF
python $TMPDIR/look2.py
```

```
s1 ERP {'spatial': {'adjacent': (0.49, 0.108), 'distance': (0.519, 0.137), 'none': (0.478, 0.343)}, 'temporal': {'adjacent': (0.396, 0.863), 'distance': (0.438, 0.875), 'none': (0.385, 0.852)}}
  power spatial adjacent pos 0/23 neg 0 minp 0.633 0.333
  power spatial distance pos 0/23 neg 0 minp 0.626 0.316
  power spatial none pos 0/23 neg 0 minp 0.472 0.848
  power temporal adjacent pos 3/23 neg 0 minp 0.004 0.699
  power temporal distance pos 3/23 neg 0 minp 0.004 0.68
  power temporal none pos 1/23 neg 0 minp 0.001 0.763
  psi delta-theta {'maintenance': {'a': 0.22, 'b': -5.79, 'code': 64.49}, 'processing': {'a': -0.43, 'b': -18.86, 'code': 66.65}}
  psi alpha-beta {'maintenance': {'a': -0.31, 'b': 1.97, 'code': 68.97}, 'processing': {'a': -0.14, 'b': -11.8, 'code': 91.84}}
s2 ERP {'spatial': {'adjacent': (0.589, 0.368), 'distance': (0.405, 0.441), 'none': (0.574, 0.344)}, 'temporal': {'adjacent': (0.053, 0.628), 'distance': (0.09, 0.698), 'none': (0.033, 0.607)}}
  power spatial adjacent pos 0/32 neg 8 minp 0.563 0.0
  power spatial distance pos 0/32 neg 10 minp 0.405 0.004
  power spatial none pos 0/32 neg 3 minp 0.284 0.0
  power temporal adjacent pos 0/32 neg 0 minp 0.977 0.059
  power temporal distance pos 0/32 neg 3 minp 0.972 0.016
  power temporal none pos 0/32 neg 1 minp 0.955 0.022
  psi delta-theta {'maintenance': {'a': -0.04, 'b': -10.13, 'code': 62.18}, 'processing': {'a': 0.11, 'b': 5.24, 'code': 37.59}}
  psi alpha-beta {'maintenance': {'a': -0.08, 'b': 2.22, 'code': 79.07}, 'processing': {'a': -0.01, 'b': -1.96, 'code': 69.89}}
s3 ERP {'spatial': {'adjacent': (0.839, 0.963), 'distance': (0.968, 0.847), 'none': (0.968, 0.847)}, 'temporal': {'adjacent': (0.273, 0.373), 'distance': (0.254, 0.973), 'none': (0.254, 0.973)}}
  power spatial adjacent pos 0/68 neg 31 minp 0.157 0.0
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> fcx3.py <<'EOF'


def load_subject(sid, chan):
    """Stream one subject and reduce it to what the claims use: (meta, results)."""
    S = stream_subject(sid, list(chan.label))
    meta = {k: S[k] for k in ["members", "primary_keys", "primary_shape", "primary_samples", "fs",
                              "trials", "clock", "elec_labels", "elec_labels_format"]}
    meta["grid"] = {g: (v["dims"], v["spacing"], len(v["pos"])) for g, v in S["grid"].items()}
    meta["epochs"] = {}
    for k in ["data_pre", "data_encmain", "data_proc"]:
        e = S[k]
        meta["epochs"][k] = {"shape": e["x"].shape, "t0": float(e["time"][0]), "t1": float(e["time"][-1]),
                             "lengths": e["lengths"], "starts": e["starts"], "n_labels": len(e["labels_all"]),
                             "fs": e["fs"], "hdr_nSamples": e["hdr_nSamples"],
                             "min": float(e["x"].min()), "max": float(e["x"].max()), "sd": float(e["x"].std()),
                             "trialinfo_equals_table": bool(np.array_equal(e["trialinfo"], S["trials"].iloc[:, :6].values))}
    meta["jitter"] = jitter_check(S)
    R = analyse_subject(S, chan)
    del S
    return meta, R
EOF
cat > $TMPDIR/devall2.py <<'EOF'
import fcx3, pickle, os, sys, time, resource
ch=fcx3.channel_table()
for sid in (sys.argv[1:] or fcx3.SUBJECTS):
    t0=time.time()
    m,R=fcx3.load_subject(sid, ch[ch.subject==sid].reset_index(drop=True))
    pickle.dump((m,R),open(os.environ['TMPDIR']+f'/res2_{sid}.pkl','wb'))
    print(sid, round(time.time()-t0), resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6, flush=True)
EOF
date -u; source $TMPDIR/dev/bin/activate && PYTHONPATH=. python $TMPDIR/devall2.py s7
```

```
Sun Nov  8 20:02:26 UTC 2026
s7 46 1.241784
```

**Agent calls Bash**

```bash
cat entries/001453-fouke-2025/reproduce_fouke_2025.ipynb | python -c "
import json,sys; nb=json.load(sys.stdin)
for c in nb['cells'][:4]: print(c['cell_type'], c.get('metadata'), ''.join(c['source'])[:1500]); print('-----')
print([c.get('metadata',{}).get('tags') for c in nb['cells']])
print(nb['metadata'])"
```

```
markdown {} # Reproducing Fouke et al. (2025) from dandiset 001453

**Paper.** Fouke KE, He Z, Loring MD, Naumann EA (2025). Neural circuits underlying divergent
visuomotor strategies of zebrafish and *Danionella cerebrum*. *Current Biology*.
[doi:10.1016/j.cub.2025.04.027](https://doi.org/10.1016/j.cub.2025.04.027). This attempt used the
full text of the accepted author manuscript in PubMed Central (PMC12218792); the version of record
is not open access.

**Dandiset.** [DANDI:001453](https://dandiarchive.org/dandiset/001453/0.250518.1950), version
0.250518.1950. The paper cites no DANDI version (its data statement points to a GitLab repository
that holds code only). This is the only published version. The draft holds the same 37 files
(same blobs and sizes); it differs only in metadata added later (authors, keywords, and a
`relatedResource` link to the paper), none of which the analysis uses.

**What the dandiset holds.** Freely swimming tracking of 25 zebrafish (ZF) and 12 *D. cerebrum*
(DC) larvae during the optomotor protocol of Figure 1 and Figure S1. The two-photon imaging and the
head-fixed tail tracking of Figures 2 to 4 are not in it.

**Outside inputs.** The stimulus codes in the files have no names. The names come from the paper's
analysis notebook `Fig1-S1.ipynb` (GitLab `ean26/danionella_omr_neuralcircuits2025`, commit
[... 48 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "Result\|summary\|conclusion" tools/entry.py | head -40
```

```
32:(docs/protocol.md): the executed notebooks with the conclusions removed (every
33:markdown cell that begins "**Result:" and everything from the "## Summary"
386:def strip_conclusions(nb):
387:    """The notebook without the author's conclusions, for a verifier's first round."""
393:        if cell.cell_type == "markdown" and text.startswith("**Result:"):
410:        nb = strip_conclusions(nbformat.read(executed, as_version=4))
```

**Agent calls Bash**

```bash
cd entries/crcns-fcx-3-johnson-2019; source $TMPDIR/dev/bin/activate && timeout 600 python -c "
import numpy as np, fcx3, time
rng=np.random.default_rng(0)
sub=np.repeat(np.arange(7),[21,116,756,30,160,32,20]); n=len(sub)
u=rng.normal(0,2,7)[sub]; v=rng.normal(0,1,n)
y1=u+v+rng.normal(0,1,n); y2=u+v+0.3+rng.normal(0,1,n)
print(fcx3.paired_lme(y1,y2,sub))
t=time.time(); print(fcx3.mixedlm_check(y1,y2,sub,np.arange(n)), time.time()-t)
"
```

```
(0.300249986003868, 48.35488160555007, 4.633831433933146e-12, 1135)
(0.3002499860038676, 48.35470884039223, 4.634231171348391e-12) 2.893522024154663
```

**Agent calls Write**

```json
{
 "file_path": "entries/crcns-fcx-3-johnson-2019/build_notebook.py",
 "content": "\"\"\"Writes reproduce_johnson_2019.ipynb (cells below). Kept with the entry so the notebook's source is reviewable as text.\"\"\"\nimport nbformat as nbf\n\ncells = []\n\n\ndef md(s, tags=None):\n    cells.append(nbf.v4.new_markdown_cell(s.strip(), metadata={\"tags\": tags} if tags else {}))\n\n\ndef code(s, tags=None):\n    cells.append(nbf.v4.new_code_cell(s.strip(), metadata={\"tags\": tags} if tags else {}))\n\n\nRESULTS = {}\ntry:\n    import results_text\n    RESULTS = results_text.RESULTS\nexcept ImportError:\n    pass\n\n\ndef result(claim):\n    md(RESULTS.get(claim, \"**Result: pending.**\"))\n\n\nmd(r\"\"\"\n# Reproducing Johnson et al. (2019) from CRCNS data set fcx-3\n\n**Paper.** Johnson EL, King-Stephens D, Weber PB, Laxer KD, Lin JJ, Knight RT (2019). Spectral\nimprints of working memory for everyday associations in the frontoparietal network. *Frontiers in\nSystems Neuroscience* 12, 65. [doi:10.3389/fnsys.2018.00065](https://doi.org/10.3389/fnsys.2018.00065).\nThe claims file was written from the version of record (PMC6333050, open access); the paper has no\nsupplement.\n\n**Data set.** CRCNS fcx-3, [doi:10.6080/K06971S9](https://doi.org/10.6080/K06971S9), read from the\npublic bucket `crcnsarchive` under `fcx-3/live/`. CRCNS data sets are not versioned, so the version\nis recorded as `unversioned` (docs/archives.md). The paper cites no version; `live/` is the only\ncopy the bucket holds (there is no `old/`), with its files dated 2026-02-11 and the data\ndescription version 0.5 of 2019-01-04, the original version. The MD5 sums of the files read, from\nthe data set's `checksums.md5`, are printed below, so that a later change is detectable.\n\n**What the data set holds.** For each of the 7 subjects: the filtered continuous iEEG\n(`data_primary.mat`), channel names, electrode positions, the preprocessed epochs\n(`data_derived.mat`: pretrial, encoding and maintenance, and processing epochs of every channel\nkept, with a per-trial table of accuracy, condition, delay and RT) and a trial table with the epoch\nstart samples. The docs list the analysed channels and give per-subject accuracy and RT. The\npaper's MATLAB scripts (`analysis_scripts.zip`) are deposited with the data and are read here for\nmethod details the paper leaves open (cited by file name).\n\n**Claims** (`claims/crcns-fcx-3/10.3389-fnsys.2018.00065.yaml`), all tested:\n\n| Claim | Tested on |\n|---|---|\n| table1-electrodes | channel list of the docs and the derived epochs |\n| trial-counts | derived epochs and trial tables |\n| fig1b-accuracy, fig1b-rt-identity-slower | docs/summary_file.csv and trial tables |\n| erp-no-condition-difference | derived processing epochs |\n| fig2-spatial-power, fig3-temporal-power, power-difficulty-subjects, power-low-frequencies | derived processing epochs |\n| fig4-maintenance-parietal-led, fig4a-delta-theta-shift, fig4c-alpha-beta-shift, directional-pairs | derived maintenance and processing epochs |\n| fig5a-delta-theta-epochs, fig5a-identity-direction, fig5a-spatiotemporal-bidirectional, fig5b-alpha-beta-no-sustained | derived processing epochs |\n\nThe data set's files are tar.gz archives (0.5 to 3.6 GB each), which cannot be read at random:\neach is streamed once, decompressed in memory, reduced to what the claims use, and released. This\ntakes most of the run time (about 20 minutes).\n\"\"\")\n\ncode(r\"\"\"\nimport time\nimport warnings\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\n\nimport fcx3\n\npd.set_option(\"display.width\", 220)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 300)\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nlisting = fcx3.bucket_listing()\nmd5 = fcx3.checksums()\nprint(listing.to_string(index=False))\nprint(\"\\nMD5 (checksums.md5) of the files read:\")\nfor k in [\"docs/summary_file.csv\", \"docs/summary_channel_analysis.csv\", \"analysis_scripts.zip\"] + [f\"data/{s}.tar.gz\" for s in fcx3.SUBJECTS]:\n    print(f\"  {md5[k]}  {k}\")\n\"\"\")\n\ncode(r\"\"\"\nCHAN = fcx3.channel_table()\nSUMMARY = fcx3.summary_file()\nMETA, RES = {}, {}\nstarted = time.time()\nfor sid in fcx3.SUBJECTS:\n    t0 = time.time()\n    chan = CHAN[CHAN.subject == sid].reset_index(drop=True)\n    META[sid], RES[sid] = fcx3.load_subject(sid, chan)\n    print(f\"{sid}: streamed and analysed in {time.time() - t0:.0f} s\", flush=True)\nprint(f\"all subjects in {(time.time() - started) / 60:.1f} min\")\n\"\"\")\n\nmd(r\"\"\"\n## Data check\n\nEach check of the description against the values is stated under its output.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor sid in fcx3.SUBJECTS:\n    m = META[sid]\n    ep = m[\"epochs\"]\n    rows.append({\"subject\": sid, \"fs\": m[\"fs\"], \"primary (samples, channels)\": m[\"primary_shape\"],\n                 \"elec_labels\": len(m[\"elec_labels\"]), \"elec_labels file\": m[\"elec_labels_format\"],\n                 \"derived channels\": ep[\"data_proc\"][\"n_labels\"], \"analysed\": ep[\"data_proc\"][\"shape\"][1],\n                 \"trials (derived)\": ep[\"data_proc\"][\"shape\"][0], \"trials (table)\": len(m[\"trials\"]),\n                 \"trialinfo = table\": all(e[\"trialinfo_equals_table\"] for e in ep.values()),\n                 \"hdr nSamples\": int(ep[\"data_proc\"][\"hdr_nSamples\"])})\nprint(pd.DataFrame(rows).to_string(index=False))\nprint(\"\\nDescription: 7 subjects; S1-6 at 1 kHz, S7 at 512 Hz; derived 'fsample: 1000'; trialinfo 6 columns as listed.\")\nprint(\"\\nEpoch time axes (s), samples per trial, value ranges (microvolts as stored; the files give no unit):\")\nrows = []\nfor sid in fcx3.SUBJECTS:\n    for k, e in META[sid][\"epochs\"].items():\n        rows.append({\"subject\": sid, \"epoch\": k, \"fs\": e[\"fs\"], \"t0\": e[\"t0\"], \"t1\": e[\"t1\"], \"lengths\": e[\"lengths\"],\n                     \"starts\": e[\"starts\"], \"min\": round(e[\"min\"], 1), \"max\": round(e[\"max\"], 1), \"sd\": round(e[\"sd\"], 2)})\nprint(pd.DataFrame(rows).to_string(index=False))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nThe description says the derived structures have `fsample: 1000`; S7's say 512, as its sampling rate.\nThe derived epochs carry every channel kept after preprocessing (29 to 155 per subject), of which the\ndocs' channel list names 192 analysed channels in all (Table 1); only those are kept here. The\ncontinuous data (`hdr nSamples`) of the derived files have a different length from the deposited\n`data_primary` in S7 only. S3's `elec_labels.mat` is a MATLAB 5 file, the others MATLAB 7.3.\n\"\"\")\n\ncode(r\"\"\"\nprint(\"Trial tables: rows, trial numbers, accuracy, condition and jitter codes\")\nrows = []\nfor sid in fcx3.SUBJECTS:\n    t = META[sid][\"trials\"]\n    rows.append({\"subject\": sid, \"rows\": len(t), \"trial numbers\": f\"{t.trial.min()}-{t.trial.max()}\",\n                 \"unique\": t.trial.is_unique, \"correct\": int(t.correct.sum()), \"incorrect\": int((t.correct == 0).sum()),\n                 \"type codes\": sorted(t.type.unique()), \"condition codes\": sorted(t.condition.unique()),\n                 \"type matches condition\": bool(((t.type == 1) == (t.condition == 1)).all()),\n                 \"jitter\": sorted(t.jitter.unique()), \"rt range ms\": (int(t.rt.min()), int(t.rt.max())),\n                 \"H-G (s)\": sorted(set(np.round((t.encmain_start - t.pre_start) / META[sid][\"fs\"], 2))),\n                 \"I-H-jitter (s)\": sorted(set(np.round((t.proc_start - t.encmain_start) / META[sid][\"fs\"] - t.jitter / 1000, 2)))})\nprint(pd.DataFrame(rows).to_string(index=False))\nprint(\"\\nTask timing (Methods, Behavioral Task): pretrial 1 s, start screen 0.8 s, fixation 0.1 s, stimuli 2 x 0.2 s,\"\n      \" delay 0.9 or 1.15 s, cue 0.8 s.\")\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nThe description says the trial table lists each trial; in S6 and S7 it lists only the trials kept\nafter artifact rejection (101 and 90 of 120, numbered up to 120), and in S1 to S5 all 120. The\npretrial start (G) precedes the encoding start (H) by 1.9 s in every trial, the pretrial fixation\nand start screen and fixation of the Methods (1.0 + 0.8 + 0.1 s). The processing start (I) follows\nH by 1.4 s plus the delay, which fits an encoding epoch of 0.6 s (the description's \"600 ms + jitter\")\nand a 0.8-s cue.\n\"\"\")\n\ncode(r\"\"\"\nprint(\"Derived epochs located in the continuous data (step 1: search; step 2: every analysed channel at the found offset).\")\nrows = []\nfor sid in fcx3.SUBJECTS:\n    ck = META[sid][\"clock\"]\n    ch = ck[\"channels\"]\n    num = ch.apply(lambda r: fcx3.split_label(r.channel)[1] - fcx3.split_label(r.reference)[1]\n                   if fcx3.split_label(r.channel)[0] == fcx3.split_label(r.reference)[0] else None, axis=1)\n    rows.append({\"subject\": sid, **{f\"offset {k[5:]} (s)\": round(v, 3) for k, v in ck[\"offsets_s\"].items()},\n                 \"search r min\": round(ck[\"search\"].r.min(), 4),\n                 \"channels\": len(ch), \"r min\": round(ch.r.min(), 4), \"r median\": round(ch.r.median(), 5),\n                 \"traces per channel\": int(ch.n_traces.min()),\n                 \"reference = contact - k, k\": dict(pd.Series(num).value_counts())})\nprint(pd.DataFrame(rows).to_string(index=False))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nEach derived trace is the difference of the channel's contact and one other contact of the\ncontinuous data (correlation at least the minimum printed, over 8 random trials and all three\nepochs), so the derived channels are bipolar, labelled by their first contact. The reference is the\ncontact numbered one below on strips and depth leads, and the next row of the grid (8 below) on S6's\n8 x 8 grid. The derived epochs start 1.4 s (pretrial), 1.5 s (encoding) and 1.8 s (processing)\nbefore the trial table's columns, in every subject, so their time axes are: pretrial, 0 at G + 0.1\ns; encoding, 0 at H; processing, 0 at I - 0.3 s. The deposited scripts' windows are therefore the\npaper's: baseline [0.65, 0.85] s of the pretrial epoch is G + 0.75 to G + 0.95 s, 250 to 50 ms before\nthe start screen; maintenance [0.6, 1.5] s of the encoding epoch is 0.9 s from H + 0.6 s; processing\n[0.3, 1.2] s is the 0.9 s from I. This shows that the derived data, the continuous data and the trial\ntable share one clock. Whether the table's columns mark the screen events is checked next.\n\"\"\")\n\ncode(r\"\"\"\nprint(\"Timing contrast between 900-ms and 1150-ms delay trials (70-150 Hz amplitude; see fcx3.jitter_check).\")\nprint(\"If the columns mark the events, the best shift is near 0 in every window; a shift beyond the shuffled maximum, with r\")\nprint(\"above the shuffled maximum, means the events lie at different times relative to the column in the two groups.\")\nrows = []\nfor sid in fcx3.SUBJECTS:\n    for k, v in META[sid][\"jitter\"].items():\n        rows.append({\"subject\": sid, \"epoch\": k, \"window (s)\": fcx3.JITTER_WINDOWS[k], \"shift 1150 vs 900 (s)\": round(v[\"lag_s\"], 3),\n                     \"r\": round(v[\"r\"], 2), \"shuffled max |shift|\": round(v[\"shuffled_abs_lag_max_s\"], 3),\n                     \"shuffled max r\": round(v[\"shuffled_r_max\"], 2)})\njit = pd.DataFrame(rows)\njit[\"clear\"] = (jit[\"r\"] > jit[\"shuffled max r\"]) & (jit[\"shift 1150 vs 900 (s)\"].abs() > jit[\"shuffled max |shift|\"])\nprint(jit.to_string(index=False))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nThe test is weak where the 70-150 Hz response is small; the column \"clear\" marks the windows where\nthe shift found exceeds every shuffled one and the alignment is better than every shuffled one.\nHow this bears on the processing window is in the Summary.\n\"\"\")\n\ncode(r\"\"\"\ngrid = pd.DataFrame([{\"subject\": sid, \"grids (dims, spacing mm, contacts)\": META[sid][\"grid\"]} for sid in fcx3.SUBJECTS])\nprint(grid.to_string(index=False))\nprint(\"\\nNeighbour pairs per reading of the cluster test's 'neighboring electrodes':\")\nprint(pd.DataFrame({sid: RES[sid][\"neighbours\"] for sid in fcx3.SUBJECTS}).to_string())\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nThe 'distance' reading places each bipolar channel at the midpoint of its two contacts, taking\ncontact n as the n-th electrode of the grid named by the label's prefix in the subject's\n`_MNI_grid.csv` (S3's RH1 to RH256 are its 256-contact grid `HD_Grid`); the files do not say how\ncontacts are numbered on a grid, so this placement is an assumption, and with the stated 10-mm\nspacings 1.5 x spacing takes in diagonal neighbours on a grid.\n\"\"\")\n\n# ------------------------------------------------------------------ table1\nmd(r\"\"\"\n## table1-electrodes\n\n> The analysed data comprise 192 bipolar virtual electrodes in seven subjects, 4 to 54 (mean 19) in\n> PFC and 2 to 16 (mean 8) in parietal cortex per subject, as listed per subject in Table 1, forming\n> 1129 same-hemisphere PFC-parietal pairs.\n\nCounted from `docs/summary_channel_analysis.csv` (every listed channel is in the derived epochs, or\nloading would have failed), with Table 1 typed from the paper for the comparison.\n\"\"\")\n\ncode(r\"\"\"\nTABLE1 = {\"s1\": (21, \"L+R\", 2, \"L+R\"), \"s2\": (24, \"L+R\", 8, \"L+R\"), \"s3\": (54, \"R\", 14, \"R\"), \"s4\": (12, \"L+R\", 10, \"R\"),\n          \"s5\": (10, \"L\", 16, \"L\"), \"s6\": (8, \"L\", 4, \"L\"), \"s7\": (4, \"L\", 5, \"L\")}\nrows = []\nfor sid in fcx3.SUBJECTS:\n    c = CHAN[CHAN.subject == sid]\n    hemi = lambda r: \"+\".join(sorted(c[c.region == r].hemisphere.unique()))\n    rows.append({\"subject\": sid, \"PFC\": int((c.region == \"PFC\").sum()), \"PFC hemi\": hemi(\"PFC\"),\n                 \"parietal\": int((c.region == \"parietal\").sum()), \"parietal hemi\": hemi(\"parietal\"),\n                 \"Table 1 PFC\": TABLE1[sid][0], \"T1 PFC hemi\": TABLE1[sid][1], \"Table 1 parietal\": TABLE1[sid][2],\n                 \"T1 par hemi\": TABLE1[sid][3], \"pairs\": len(RES[sid][\"pairs\"])})\nt1 = pd.DataFrame(rows)\nprint(t1.to_string(index=False))\nn_el = int(t1.PFC.sum() + t1.parietal.sum())\nn_pairs = int(t1.pairs.sum())\nprint(f\"\\nanalysed channels {n_el} (paper 192); PFC per subject {t1.PFC.min()}-{t1.PFC.max()} mean {t1.PFC.mean():.2f} (paper 4-54, 19);\"\n      f\" parietal {t1.parietal.min()}-{t1.parietal.max()} mean {t1.parietal.mean():.2f} (paper 2-16, 8)\")\nprint(f\"same-hemisphere PFC-parietal pairs {n_pairs} (paper 1129); difference {n_pairs - 1129} ({(n_pairs - 1129) / 1129:+.1%});\"\n      f\" channels {(n_el - 192) / 192:+.1%}\")\nmism = t1[(t1.PFC != t1[\"Table 1 PFC\"]) | (t1.parietal != t1[\"Table 1 parietal\"]) | (t1[\"PFC hemi\"] != t1[\"T1 PFC hemi\"]) | (t1[\"parietal hemi\"] != t1[\"T1 par hemi\"])]\nprint(\"subjects differing from Table 1:\", list(mism.subject))\ns4 = t1.set_index(\"subject\").loc[\"s4\"]\nprint(f\"With Table 1's 10 right parietal channels in s4, its pairs would be 6 x 10 = 60, total {n_pairs - s4.pairs + 60}.\")\n\"\"\", tags=[\"claim:table1-electrodes\"])\nresult(\"table1-electrodes\")\n\n# ------------------------------------------------------------------ trial counts\nmd(r\"\"\"\n## trial-counts\n\n> After artifact rejection subjects kept on average 96 correct trials, 32 +- 3 (26 to 35) identity,\n> 33 +- 4 (27 to 39) spatial and 31 +- 6 (20 to 39) temporal, and had 17 +- 8 (4 to 25) incorrect\n> trials per subject.\n\nCorrect trials kept are those of the derived epochs with accuracy 1 (`trialinfo` column 2, the\nselection of the deposited scripts). The incorrect count is read (a) of all 120 trials, from the\nper-subject accuracy of `docs/summary_file.csv` (over all 120 trials, by the data description;\n40 trials per condition, Methods), and (b) of the trials kept.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor sid in fcx3.SUBJECTS:\n    R = RES[sid]\n    s = SUMMARY[SUMMARY.subject.str.lower() == sid].iloc[0]\n    corr_all = int(round(40 * (s.acc_identity + s.acc_spatial + s.acc_temporal)))\n    rows.append({\"subject\": sid, \"trials kept\": R[\"n_trials\"], \"correct kept\": R[\"n_correct\"],\n                 \"identity\": R[\"n_correct_by_cond\"][1], \"spatial\": R[\"n_correct_by_cond\"][2], \"temporal\": R[\"n_correct_by_cond\"][3],\n                 \"incorrect (a) of 120\": 120 - corr_all, \"incorrect (b) kept\": R[\"n_incorrect\"], \"correct of 120\": corr_all})\ntc = pd.DataFrame(rows)\nprint(tc.to_string(index=False))\nsumm = tc.drop(columns=\"subject\").agg([\"mean\", \"std\", \"min\", \"max\"]).round(2)\nprint(\"\\n\", summ.to_string())\nexp = {\"correct kept\": (96, None), \"identity\": (32, (26, 35)), \"spatial\": (33, (27, 39)), \"temporal\": (31, (20, 39)),\n       \"incorrect (a) of 120\": (17, (4, 25)), \"incorrect (b) kept\": (17, (4, 25))}\nfor k, (v, rg) in exp.items():\n    m = tc[k].mean()\n    within = abs(m - v) <= 0.1 * v\n    rg_ok = None if rg is None else (tc[k].min() >= rg[0] - 0.1 * rg[0] and tc[k].max() <= rg[1] + 0.1 * rg[1])\n    print(f\"{k}: mean {m:.2f} vs {v} (within 10%: {within}); range {tc[k].min()}-{tc[k].max()} vs {rg} widened 10%: {rg_ok}\")\nprint(\"\\nCorrect trials kept equal all correct trials of 120 in:\", [r.subject for r in tc.itertuples() if r._3 == r._9])\n\"\"\", tags=[\"claim:trial-counts\"])\nresult(\"trial-counts\")\n\n# ------------------------------------------------------------------ behaviour\nmd(r\"\"\"\n## fig1b-accuracy\n\n> All subjects were proficient at the task (accuracy 0.63 to 0.98, chance 0.5), and accuracy did not\n> differ between conditions.\n\nAccuracy per subject and condition is in `docs/summary_file.csv`, over all 120 trials (data\ndescription), which is reading (a) of B1's \"all trials\" question; the trial tables of S6 and S7\nlist only kept trials, so single-trial accuracy over all 120 is rebuilt as counts out of 40 per\ncondition (Methods: \"120 trials divided evenly\"). The logit mixed model (condition fixed, subject\nrandom intercept) is fitted by maximum likelihood with Gauss-Hermite quadrature\n(`fcx3.logit_mixed`; the paper names the model, not the software), with condition as one\nnumeric term (the single degree of freedom of the paper's F(1,19) for RT) and, as a variant, as\ntwo dummy terms. Reading (b) of B1 (accuracy over kept trials) is shown as a variant.\n\"\"\")\n\ncode(r\"\"\"\nacc = SUMMARY[[\"subject\", \"acc_identity\", \"acc_spatial\", \"acc_temporal\"]].copy()\nacc[\"overall\"] = acc[[\"acc_identity\", \"acc_spatial\", \"acc_temporal\"]].mean(1)\nprint(acc.round(3).to_string(index=False))\nlo, hi = 0.63, 0.98\nfor name, vals in [(\"(a) per subject over conditions\", acc.overall.values),\n                   (\"(b) per subject and condition\", acc[[\"acc_identity\", \"acc_spatial\", \"acc_temporal\"]].values.ravel())]:\n    print(f\"{name}: min {vals.min():.3f} (expected 0.63 +- 0.063: {abs(vals.min() - lo) <= 0.063}), max {vals.max():.3f} \"\n          f\"(expected 0.98 +- 0.098: {abs(vals.max() - hi) <= 0.098}); all inside [{lo - 0.063:.3f}, {hi + 0.098:.3f}]: \"\n          f\"{bool(((vals >= lo - 0.063) & (vals <= hi + 0.098)).all())}\")\n\nlong = acc.melt(id_vars=\"subject\", value_vars=[\"acc_identity\", \"acc_spatial\", \"acc_temporal\"], var_name=\"cond\", value_name=\"acc\")\nlong[\"cond_code\"] = long.cond.map({\"acc_identity\": 1, \"acc_spatial\": 2, \"acc_temporal\": 3})\nlong[\"k\"] = np.round(long.acc * 40).astype(int)\nlong[\"n\"] = 40\nbeta, se, ll1 = fcx3.logit_mixed(long.k.values, long.n.values, long.cond_code.values[:, None].astype(float), long.subject.values)\n_, _, ll0 = fcx3.logit_mixed(long.k.values, long.n.values, np.zeros((len(long), 0)), long.subject.values)\nz = beta[1] / se[1]\nprint(f\"\\n(a) all 120 trials, condition as one term: slope {beta[1]:.3f} (SE {se[1]:.3f}), Wald z {z:.2f}, p {2 * stats.norm.sf(abs(z)):.3f};\"\n      f\" likelihood ratio chi2(1) {2 * (ll1 - ll0):.2f}, p {stats.chi2.sf(2 * (ll1 - ll0), 1):.3f}\")\nD = np.column_stack([(long.cond_code == 2).astype(float), (long.cond_code == 3).astype(float)])\n_, _, ll2 = fcx3.logit_mixed(long.k.values, long.n.values, D, long.subject.values)\nprint(f\"(a) condition as two dummy terms: likelihood ratio chi2(2) {2 * (ll2 - ll0):.2f}, p {stats.chi2.sf(2 * (ll2 - ll0), 2):.3f}\")\n\nkept = pd.concat([META[s][\"trials\"].assign(subject=s) for s in fcx3.SUBJECTS])\nkk = kept.groupby([\"subject\", \"condition\"]).correct.agg([\"sum\", \"count\"]).reset_index()\nb2, se2, l1 = fcx3.logit_mixed(kk[\"sum\"].values, kk[\"count\"].values, kk.condition.values[:, None].astype(float), kk.subject.values)\n_, _, l0 = fcx3.logit_mixed(kk[\"sum\"].values, kk[\"count\"].values, np.zeros((len(kk), 0)), kk.subject.values)\nprint(f\"(b) kept trials, condition as one term: slope {b2[1]:.3f}, likelihood ratio chi2(1) {2 * (l1 - l0):.2f}, p {stats.chi2.sf(2 * (l1 - l0), 1):.3f}\")\nprint(\"accuracy over kept trials per subject:\", kept.groupby(\"subject\").correct.mean().round(3).to_dict())\n\"\"\", tags=[\"claim:fig1b-accuracy\"])\nresult(\"fig1b-accuracy\")\n\nmd(r\"\"\"\n## fig1b-rt-identity-slower\n\n> Response times differed by condition, being longer on identity than on spatial and temporal\n> trials, with no difference between spatial and temporal trials.\n\nReading (a) of B1: one mean correct-trial RT per subject and condition (`docs/summary_file.csv`,\n\"calculated on all correct trials\"), a linear mixed model with condition as one numeric term and a\nsubject random intercept (REML, statsmodels), F = t^2 on the residual degrees of freedom (21 - 2 =\n19; pairs 14 - 2 = 12), as fitlme reports. Reading (b): single correct trials; only the kept trials\nare in the trial tables (all correct trials in S1 to S5), so (b) is on those. Cohen's d is given as\nthe mean paired difference over its SD across subjects, one common definition (the paper does not\nsay which it used; d is reported, not judged).\n\"\"\")\n\ncode(r\"\"\"\nimport statsmodels.formula.api as smf\n\nrt = SUMMARY.melt(id_vars=\"subject\", value_vars=[\"rt_identity\", \"rt_spatial\", \"rt_temporal\"], var_name=\"cond\", value_name=\"rt\")\nrt[\"c\"] = rt.cond.map({\"rt_identity\": 1, \"rt_spatial\": 2, \"rt_temporal\": 3})\nprint(SUMMARY[[\"subject\", \"rt_identity\", \"rt_spatial\", \"rt_temporal\"]].round(0).to_string(index=False))\n\n\ndef lme_f(df, y, groups):\n    r = smf.mixedlm(f\"{y} ~ c\", df, groups=df[groups]).fit(reml=True)\n    t = r.tvalues[\"c\"]\n    return r.params[\"c\"], t ** 2, stats.f.sf(t ** 2, 1, len(df) - 2), len(df) - 2\n\n\ndef report(df, y, groups, label):\n    out = {}\n    b, F, p, dfr = lme_f(df, y, groups)\n    out[\"all\"] = (b, F, p)\n    print(f\"{label} omnibus: slope {b:.1f} ms per condition step, F(1,{dfr}) = {F:.2f}, p = {p:.4f}\")\n    for a, bb, name in [(1, 2, \"identity vs spatial\"), (1, 3, \"identity vs temporal\"), (2, 3, \"spatial vs temporal\")]:\n        sub = df[df.c.isin([a, bb])].copy()\n        b2, F2, p2, dfr2 = lme_f(sub, y, groups)\n        out[name] = (b2, F2, p2)\n        print(f\"   {name}: difference {b2 * (bb - a):.1f} ms ({'first longer' if b2 < 0 else 'second longer'}), F(1,{dfr2}) = {F2:.2f}, p = {p2:.4f}\")\n    return out\n\n\nrt_a = report(rt, \"rt\", \"subject\", \"(a) subject-condition means\")\nw = SUMMARY.set_index(\"subject\")\nfor a, b in [(\"rt_identity\", \"rt_spatial\"), (\"rt_identity\", \"rt_temporal\"), (\"rt_spatial\", \"rt_temporal\")]:\n    d = w[a] - w[b]\n    print(f\"   d ({a[3:]} - {b[3:]}): {d.mean() / d.std(ddof=1):.2f}; identity longer in {int((d > 0).sum())}/7 subjects\")\ntr = kept[kept.correct == 1].rename(columns={\"condition\": \"c\"})\nrt_b = report(tr, \"rt\", \"subject\", \"(b) single kept correct trials\")\n\"\"\", tags=[\"claim:fig1b-rt-identity-slower\"])\nresult(\"fig1b-rt-identity-slower\")\n\n# ------------------------------------------------------------------ ERP\nmd(r\"\"\"\n## erp-no-condition-difference\n\n> ERPs over the processing interval did not differ between identity and spatial or temporal trials\n> in any subject.\n\nERPs per erp_compute.m (30-Hz FIR low-pass with 7.5-s zero padding, baseline the pretrial temporal\nmean over trials), tested per subject by the cluster test of S2 over channels and time (900 or 461\nsamples), identity against spatial and against temporal, 1000 shuffles. Readings of the\nneighbours: adjacent, distance, none; readings of the threshold: a cluster's p below 0.05 per tail\n(FieldTrip's default, and the Methods' \"fewer than 5% of randomizations yielded a larger effect\"),\nor below 0.025. The smallest cluster p per subject and contrast is printed for each.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor sid in fcx3.SUBJECTS:\n    for con, res in RES[sid][\"erp\"].items():\n        for nb, v in res.items():\n            pmin = min([p for _, p in v[\"pos\"]] + [p for _, p in v[\"neg\"]] + [1.0])\n            rows.append({\"subject\": sid, \"contrast\": con, \"neighbours\": nb, \"min cluster p\": pmin})\nerp = pd.DataFrame(rows)\ntab = erp.pivot_table(index=[\"subject\", \"contrast\"], columns=\"neighbours\", values=\"min cluster p\")\nprint(tab.round(3).to_string())\nfor nb in fcx3.NB_READINGS:\n    e = erp[erp.neighbours == nb]\n    print(f\"{nb}: subject-contrasts with a cluster p < 0.05: {int((e['min cluster p'] < 0.05).sum())}, < 0.025: \"\n          f\"{int((e['min cluster p'] < 0.025).sum())}; smallest p {e['min cluster p'].min():.3f}; \"\n          f\"subject-contrasts with p <= 0.10 (paper: all p > 0.10): {int((e['min cluster p'] <= 0.10).sum())} of 14\")\n\"\"\", tags=[\"claim:erp-no-condition-difference\"])\nresult(\"erp-no-condition-difference\")\n\n# ------------------------------------------------------------------ power\nmd(r\"\"\"\n## fig2-spatial-power and fig3-temporal-power\n\n> In the identity against spatial contrast of processing-interval power, 5 of 7 subjects showed\n> spatial > identity effects (54 +- 22% of electrodes per subject) and 2 of 7 showed identity >\n> spatial effects (36 +- 12%).\n\n> In the identity against temporal contrast of processing-interval power, 4 of 7 subjects showed\n> temporal > identity effects (68 +- 30% of electrodes per subject) and 2 of 7 showed identity >\n> temporal effects (37 +- 10%).\n\nPower per power_compute.m: 3-cycle Hanning windows, 2 to 40 Hz, 10-ms steps over the 900-ms\nprocessing window, z-scored on the bootstrapped pretrial baseline of all correct trials (zbaseline.m;\nr = all correct trials, settling S1's open r). The derived epochs extend 1.5 s beyond the windows,\nso every window is filled with data (S1's padding readings do not arise). The cluster test of S2\nover channel, frequency and time, 1000 shuffles. An electrode shows an effect of a sign when any of\nits points lies in a significant cluster of that sign (S2 reading (a)); reading (b) assigns an\nelectrode in both to the sign with the larger summed t. Every combination of neighbour reading,\nthreshold and assignment is shown.\n\"\"\")\n\ncode(r\"\"\"\ndef power_effects(contrast, nb, alpha=0.05, assign=\"a\"):\n    out = []\n    for sid in fcx3.SUBJECTS:\n        cl = RES[sid][\"power\"][contrast][\"clusters\"][nb]\n        n = len(RES[sid][\"labels\"])\n        ident, other = np.zeros(n, bool), np.zeros(n, bool)\n        ts_i, ts_o = np.zeros(n), np.zeros(n)\n        for c in cl[\"pos\"]:  # positive t: identity > other\n            if c[\"p\"] < alpha:\n                ident |= c[\"elec_mask\"]\n                ts_i += c[\"tsum_by_elec\"]\n        for c in cl[\"neg\"]:\n            if c[\"p\"] < alpha:\n                other |= c[\"elec_mask\"]\n                ts_o += -c[\"tsum_by_elec\"]\n        if assign == \"b\":\n            both = ident & other\n            ident = ident & ~(both & (ts_o >= ts_i))\n            other = other & ~(both & (ts_i > ts_o))\n        out.append({\"subject\": sid, \"n\": n, \"other>identity\": int(other.sum()), \"identity>other\": int(ident.sum()),\n                    \"p other>identity\": cl[\"neg_minp\"], \"p identity>other\": cl[\"pos_minp\"]})\n    return pd.DataFrame(out)\n\n\nEXPECTED = {\"spatial\": (5, 2, 54, 36), \"temporal\": (4, 2, 68, 37)}\nPOWER_SUMMARY = []\nfor contrast in [\"spatial\", \"temporal\"]:\n    print(f\"==== identity against {contrast}\")\n    print(power_effects(contrast, \"adjacent\").to_string(index=False))\n    for nb in fcx3.NB_READINGS:\n        for alpha in (0.05, 0.025):\n            for assign in (\"a\", \"b\"):\n                e = power_effects(contrast, nb, alpha, assign)\n                po = 100 * e[\"other>identity\"] / e.n\n                pi = 100 * e[\"identity>other\"] / e.n\n                so, si = po[po > 0], pi[pi > 0]\n                ex = EXPECTED[contrast]\n                row = {\"contrast\": contrast, \"neighbours\": nb, \"alpha per tail\": alpha, \"assign\": assign,\n                       \"subjects other>id\": len(so), \"subjects id>other\": len(si),\n                       \"% other>id\": f\"{so.mean():.1f} +- {so.std(ddof=1):.1f}\" if len(so) > 1 else (f\"{so.mean():.1f}\" if len(so) else \"-\"),\n                       \"% id>other\": f\"{si.mean():.1f} +- {si.std(ddof=1):.1f}\" if len(si) > 1 else (f\"{si.mean():.1f}\" if len(si) else \"-\"),\n                       \"subjects other>id (list)\": list(e.subject[po > 0]), \"subjects id>other (list)\": list(e.subject[pi > 0])}\n                row[\"match\"] = (len(so) == ex[0] and len(si) == ex[1] and len(so) > 0 and len(si) > 0\n                                and abs(so.mean() - ex[2]) <= 0.1 * ex[2] and abs(si.mean() - ex[3]) <= 0.1 * ex[3])\n                row[\"counts within 1\"] = abs(len(so) - ex[0]) <= 1 and abs(len(si) - ex[1]) <= 1\n                POWER_SUMMARY.append(row)\nPOWER_SUMMARY = pd.DataFrame(POWER_SUMMARY)\nprint(POWER_SUMMARY.drop(columns=[\"subjects other>id (list)\", \"subjects id>other (list)\"]).to_string(index=False))\nprint(\"\\nSubjects per effect, adjacent neighbours, 0.05 per tail, reading (a):\")\nprint(POWER_SUMMARY[(POWER_SUMMARY.neighbours == \"adjacent\") & (POWER_SUMMARY[\"alpha per tail\"] == 0.05) & (POWER_SUMMARY.assign == \"a\")][\n    [\"contrast\", \"subjects other>id (list)\", \"subjects id>other (list)\"]].to_string(index=False))\n\"\"\", tags=[\"claim:fig2-spatial-power\", \"claim:fig3-temporal-power\"])\n\ncode(r\"\"\"\nprint(\"Smallest cluster p of each sign and subject (adjacent neighbours); paper: all p < 0.04 for the effects it reports\")\nrows = []\nfor contrast in [\"spatial\", \"temporal\"]:\n    for sid in fcx3.SUBJECTS:\n        cl = RES[sid][\"power\"][contrast][\"clusters\"]\n        rows.append({\"contrast\": contrast, \"subject\": sid, **{f\"{nb} other>id\": round(cl[nb][\"neg_minp\"], 3) for nb in fcx3.NB_READINGS},\n                     **{f\"{nb} id>other\": round(cl[nb][\"pos_minp\"], 3) for nb in fcx3.NB_READINGS}})\nprint(pd.DataFrame(rows).to_string(index=False))\n\"\"\", tags=[\"claim:fig2-spatial-power\", \"claim:fig3-temporal-power\"])\nresult(\"fig2-spatial-power\")\nresult(\"fig3-temporal-power\")\n\nmd(r\"\"\"\n## power-difficulty-subjects\n\n> The subjects with identity > spatial or temporal power effects were the same subjects who had both\n> longer RTs and lower accuracy on identity trials.\n\nSubjects with an identity > spatial or identity > temporal effect are taken from the power claims\n(each neighbour reading at 0.05 per tail, reading (a)); accuracy (all 120 trials) and mean correct RT\nper condition from `docs/summary_file.csv`.\n\"\"\")\n\ncode(r\"\"\"\nw = SUMMARY.copy()\nw[\"subject\"] = w.subject.str.lower()\nw = w.set_index(\"subject\")\nbeh = pd.DataFrame({\n    \"RT id > sp\": w.rt_identity > w.rt_spatial, \"acc id < sp\": w.acc_identity < w.acc_spatial,\n    \"RT id > tp\": w.rt_identity > w.rt_temporal, \"acc id < tp\": w.acc_identity < w.acc_temporal,\n    \"RT id > mean(sp,tp)\": w.rt_identity > (w.rt_spatial + w.rt_temporal) / 2,\n    \"acc id < mean(sp,tp)\": w.acc_identity < (w.acc_spatial + w.acc_temporal) / 2})\nbeh[\"both (a) spatial\"] = beh[\"RT id > sp\"] & beh[\"acc id < sp\"]\nbeh[\"both (a) temporal\"] = beh[\"RT id > tp\"] & beh[\"acc id < tp\"]\nbeh[\"both (b)\"] = beh[\"RT id > mean(sp,tp)\"] & beh[\"acc id < mean(sp,tp)\"]\nprint(beh.to_string())\nfor nb in fcx3.NB_READINGS:\n    sel = POWER_SUMMARY[(POWER_SUMMARY.neighbours == nb) & (POWER_SUMMARY[\"alpha per tail\"] == 0.05) & (POWER_SUMMARY.assign == \"a\")].set_index(\"contrast\")\n    sp_ = set(sel.loc[\"spatial\", \"subjects id>other (list)\"])\n    tp_ = set(sel.loc[\"temporal\", \"subjects id>other (list)\"])\n    effect = sorted(sp_ | tp_)\n    ok_a = all((s not in sp_ or beh.loc[s, \"both (a) spatial\"]) and (s not in tp_ or beh.loc[s, \"both (a) temporal\"]) for s in effect)\n    ok_b = all(beh.loc[s, \"both (b)\"] for s in effect)\n    others_a = [s for s in beh.index if s not in effect and (beh.loc[s, \"both (a) spatial\"] or beh.loc[s, \"both (a) temporal\"])]\n    others_b = [s for s in beh.index if s not in effect and beh.loc[s, \"both (b)\"]]\n    print(f\"{nb}: identity>spatial {sorted(sp_)}, identity>temporal {sorted(tp_)}; every one has both under (a): {ok_a}, under (b): {ok_b};\"\n          f\" other subjects with both, (a): {others_a}, (b): {others_b}\")\n\"\"\", tags=[\"claim:power-difficulty-subjects\"])\nresult(\"power-difficulty-subjects\")\n\nmd(r\"\"\"\n## power-low-frequencies\n\n> Significant processing-interval power effects were most prominent at low frequencies, in distinct\n> delta-theta (2 to 7 Hz) and alpha-beta (9 to 24 Hz) ranges, whatever the contrast.\n\nPer subject and effect, the t values inside significant clusters (adjacent neighbours, 0.05 per\ntail; the other readings below) are averaged over electrodes and time per frequency, (a) over the\nmasked points only, (b) over all points with the unmasked as zero; then averaged, in absolute\nvalue, over the subjects with the effect. The rule (2-24 Hz larger than 25-40 Hz, local maxima in\n2-7 and 9-24 Hz) is the claims file's.\n\"\"\")\n\ncode(r\"\"\"\ndef density(nb, effect, reading, alpha=0.05):\n    out = {}\n    for sid in fcx3.SUBJECTS:\n        R = RES[sid]\n        dens = []\n        for contrast in ([\"spatial\"] if effect == \"spatial>identity\" else [\"temporal\"] if effect == \"temporal>identity\" else [\"spatial\", \"temporal\"]):\n            cl = R[\"power\"][contrast][\"clusters\"][nb]\n            sign = \"neg\" if effect != \"identity>other\" else \"pos\"\n            cs = [c for c in cl[sign] if c[\"p\"] < alpha]\n            if not cs:\n                continue\n            tm = sum(c[\"t_masked\"].astype(float) for c in cs)  # ch x f x t\n            if reading == \"a\":\n                cnt = (tm != 0).sum(axis=(0, 2))\n                dens.append(np.where(cnt > 0, tm.sum(axis=(0, 2)) / np.maximum(cnt, 1), 0))\n            else:\n                dens.append(tm.mean(axis=(0, 2)))\n        if dens:\n            out[sid] = np.abs(np.mean(dens, axis=0))\n    return out\n\n\nf = fcx3.FOI\nLF = []\nfor nb in fcx3.NB_READINGS:\n    for reading in (\"a\", \"b\"):\n        for effect in [\"spatial>identity\", \"temporal>identity\", \"identity>other\"]:\n            d = density(nb, effect, reading)\n            if not d:\n                LF.append({\"neighbours\": nb, \"reading\": reading, \"effect\": effect, \"subjects\": 0})\n                continue\n            m = np.mean(list(d.values()), axis=0)\n            low, high = m[(f >= 2) & (f <= 24)].mean(), m[(f >= 25) & (f <= 40)].mean()\n            peaks = [int(f[i]) for i in range(len(f)) if (i == 0 or m[i] > m[i - 1]) and (i == len(f) - 1 or m[i] >= m[i + 1])]\n            LF.append({\"neighbours\": nb, \"reading\": reading, \"effect\": effect, \"subjects\": len(d), \"2-24 Hz\": round(low, 3),\n                       \"25-40 Hz\": round(high, 3), \"low > high\": low > high, \"local maxima (Hz)\": peaks,\n                       \"max in 2-7\": any(2 <= p <= 7 for p in peaks), \"max in 9-24\": any(9 <= p <= 24 for p in peaks),\n                       \"peak Hz\": int(f[np.argmax(m)])})\nLF = pd.DataFrame(LF)\nprint(LF.to_string(index=False))\nfig, axes = plt.subplots(1, 3, figsize=(12, 3), sharey=False)\nfor ax, effect in zip(axes, [\"spatial>identity\", \"temporal>identity\", \"identity>other\"]):\n    for sid, v in density(\"adjacent\", effect, \"a\").items():\n        ax.plot(f, v, lw=0.8, label=sid)\n    ax.set_title(effect + \" (adjacent, a)\")\n    ax.set_xlabel(\"Hz\")\naxes[0].set_ylabel(\"|mean significant t|\")\naxes[0].legend(fontsize=7)\nplt.tight_layout()\nplt.show()\nprint(\"All densities plotted are within the axes (autoscaled).\")\n\"\"\", tags=[\"claim:power-low-frequencies\"])\nresult(\"power-low-frequencies\")\n\n# ------------------------------------------------------------------ PSI task-induced\nmd(r\"\"\"\n## Task-induced PSI: fig4-maintenance-parietal-led, fig4a-delta-theta-shift, fig4c-alpha-beta-shift, directional-pairs\n\n> During maintenance, PFC-parietal connectivity was unidirectional, parietal to PFC, in both the\n> delta-theta (z < -40.03 +- 8.73) and alpha-beta (z < -30.37 +- 2.60) ranges.\n\n> After the test cue, delta-theta directionality shifted from a unidirectional parietal-led network\n> to a bidirectional frontoparietal one, with net PFC-led connectivity above zero in 6 of 7 subjects\n> during processing (z > 6.01 +- 6.42).\n\n> Alpha-beta directionality also shifted with the test cue, but all subjects remained net\n> parietal-led during processing (z < -12.60 +- 7.51).\n\n> During processing, 1008 pairs were significantly directional in the delta-theta range and 984 in\n> the alpha-beta range.\n\nPSI per P1, with the details psi_compute.m and psianalysis.m settle: the ERP subtracted is the mean\nover all correct trials (P1 \"raw trial-wise mean\", reading (a); subtracterp.m with one condition);\nspectra are one Hanning-tapered FFT of each 900-ms segment padded to 7.5 s ('mtmfft', P1 spectra\nreading (a)); PSI is one value per band summed over all its 1-Hz bins (band reading (a)); one\nshuffle serves all pairs (null reading (a)). P1's last question, PSI from trial-averaged\ncross-spectra or per trial, is not settled the same way: psianalysis.m computes PSI per trial from\nthe per-trial normalised cross-spectrum and averages it over trials (reading (b)), but as deposited\nit multiplies the Fourier coefficients without the conjugate, so its \"cross-spectrum\" does not\nmeasure a phase difference between the two channels (a code mismatch with the Methods'\ncross-spectral density and Nolte et al. 2008). Both readings are run with the conjugate, and the\ndeposited code as a variant. Positive z: PFC leads.\n\"\"\")\n\ncode(r\"\"\"\nREAD = {\"a\": \"(a) trial-averaged coherency\", \"b\": \"(b) per-trial PSI averaged\", \"code\": \"deposited code (no conjugate)\"}\npsi_rows = []\nfor sid in fcx3.SUBJECTS:\n    for band in fcx3.BANDS:\n        for iv in (\"maintenance\", \"processing\"):\n            for k, z in RES[sid][\"psi\"][band][iv].items():\n                for (pfc, par, hemi), v in zip(RES[sid][\"pairs\"], z):\n                    psi_rows.append({\"subject\": sid, \"band\": band, \"interval\": iv, \"reading\": k, \"pair\": f\"{sid}:{pfc}-{par}\", \"z\": v})\nPSI = pd.DataFrame(psi_rows)\nprint(\"Pairs per subject:\", PSI[(PSI.band == \"delta-theta\") & (PSI.interval == \"maintenance\") & (PSI.reading == \"a\")].groupby(\"subject\").size().to_dict())\nprint(\"Frequencies read (Hz):\", {b: np.round(RES['s1']['psi'][b]['freqs'], 3).tolist() for b in fcx3.BANDS})\npersub = PSI.groupby([\"band\", \"interval\", \"reading\", \"subject\"]).z.mean().unstack(\"subject\")\nprint(\"\\nPer-subject mean PSI z over pairs:\")\nprint(persub.round(2).to_string())\ngrp = PSI.groupby([\"band\", \"interval\", \"reading\", \"subject\"]).z.mean().groupby([\"band\", \"interval\", \"reading\"]).agg([\"mean\", \"std\", \"min\", \"max\"])\ngrp.columns = [\"mean over subjects\", \"SD over subjects\", \"min subject\", \"max subject\"]\npairs_ = PSI.groupby([\"band\", \"interval\", \"reading\"]).z.agg([\"mean\", \"std\", \"min\", \"max\"])\npairs_.columns = [\"mean over pairs\", \"SD over pairs\", \"min pair\", \"max pair\"]\nprint(\"\\n\", pd.concat([grp, pairs_], axis=1).round(2).to_string())\n\"\"\", tags=[\"claim:fig4-maintenance-parietal-led\", \"claim:fig4a-delta-theta-shift\", \"claim:fig4c-alpha-beta-shift\", \"claim:directional-pairs\"])\n\ncode(r\"\"\"\nprint(\"fig4-maintenance-parietal-led: expected delta-theta -40.03 (tol 4.0 or more negative), alpha-beta -30.37 (tol 3.04 or more negative)\")\nfor k in (\"a\", \"b\", \"code\"):\n    m = persub.xs((\"maintenance\", k), level=(\"interval\", \"reading\"))\n    for band, exp, tol in [(\"delta-theta\", -40.03, 4.0), (\"alpha-beta\", -30.37, 3.04)]:\n        v = m.loc[band]\n        pooled = PSI[(PSI.band == band) & (PSI.interval == \"maintenance\") & (PSI.reading == k)].z\n        print(f\"  {READ[k]}, {band}: subjects below -1.96: {int((v < -1.96).sum())}/7; mean over subjects {v.mean():.2f} +- {v.std(ddof=1):.2f};\"\n              f\" pooled pairs {pooled.mean():.2f} +- {pooled.std(ddof=1):.2f}; pairs below -1.96 {int((pooled < -1.96).sum())}/{len(pooled)},\"\n              f\" above 1.96 {int((pooled > 1.96).sum())}; within tolerance or beyond: (a) {v.mean() <= exp + tol}, (b) {pooled.mean() <= exp + tol}\")\n\"\"\", tags=[\"claim:fig4-maintenance-parietal-led\"])\nresult(\"fig4-maintenance-parietal-led\")\n\ncode(r\"\"\"\nLME = {}\nfor band in fcx3.BANDS:\n    for k in (\"a\", \"b\", \"code\"):\n        d = PSI[(PSI.band == band) & (PSI.reading == k)].pivot_table(index=[\"subject\", \"pair\"], columns=\"interval\", values=\"z\").reset_index()\n        eff, F, p, n = fcx3.paired_lme(d.maintenance.values, d.processing.values, d.subject.values)\n        LME[(band, k)] = (eff, F, p, n)\n        line = f\"{band}, {READ[k]}: processing - maintenance {eff:.2f}, F(1,{2 * n - 2}) = {F:.1f}, p = {p:.3g} (pairs {n})\"\n        if k in (\"a\", \"b\"):\n            e2, F2, p2 = fcx3.mixedlm_check(d.maintenance.values, d.processing.values, d.subject.values, d.pair.values)\n            line += f\"; statsmodels MixedLM: {e2:.2f}, F {F2:.1f}, p {p2:.3g}\"\n        print(line)\nprint(\"Paper: delta-theta F(1,2256) = 1936.10, p < 8e-306; alpha-beta F(1,2256) = 2302.30, p = 0 (processing > maintenance).\")\n\"\"\", tags=[\"claim:fig4a-delta-theta-shift\", \"claim:fig4c-alpha-beta-shift\"])\n\ncode(r\"\"\"\nprint(\"fig4a-delta-theta-shift: expected 6 subjects with processing z > 0, mean 6.01 (tol 0.6 or larger), F 1936.10 +- 193.6\")\nfor k in (\"a\", \"b\", \"code\"):\n    v = persub.xs((\"delta-theta\", \"processing\", k), level=(\"band\", \"interval\", \"reading\"))\n    pos = v[v > 0]\n    eff, F, p, n = LME[(\"delta-theta\", k)]\n    print(f\"  {READ[k]}: subjects above 0: {int((v > 0).sum())}/7 {list(v[v > 0].index)}; mean of 7 {v.mean():.2f} +- {v.std(ddof=1):.2f};\"\n          f\" mean of those above 0 {pos.mean() if len(pos) else float('nan'):.2f}; model effect {eff:+.2f}, F {F:.1f}, p {p:.3g}\")\nprint(\"fig4c-alpha-beta-shift: expected every subject below 0 in processing, mean -12.60 (tol 1.26 or more negative), F 2302.30 +- 230.2\")\nfor k in (\"a\", \"b\", \"code\"):\n    v = persub.xs((\"alpha-beta\", \"processing\", k), level=(\"band\", \"interval\", \"reading\"))\n    eff, F, p, n = LME[(\"alpha-beta\", k)]\n    print(f\"  {READ[k]}: subjects below 0: {int((v < 0).sum())}/7; mean {v.mean():.2f} +- {v.std(ddof=1):.2f}; model effect {eff:+.2f}, F {F:.1f}, p {p:.3g}\")\n\"\"\", tags=[\"claim:fig4a-delta-theta-shift\", \"claim:fig4c-alpha-beta-shift\"])\nresult(\"fig4a-delta-theta-shift\")\nresult(\"fig4c-alpha-beta-shift\")\n\ncode(r\"\"\"\nprint(\"directional-pairs: pairs with processing |z| > 1.96, expected delta-theta 1008 (+-100.8), alpha-beta 984 (+-98.4), of all pairs\")\nSEL = {}\nfor k in (\"a\", \"b\", \"code\"):\n    for band, exp in [(\"delta-theta\", 1008), (\"alpha-beta\", 984)]:\n        p = PSI[(PSI.band == band) & (PSI.interval == \"processing\") & (PSI.reading == k)]\n        n = int((p.z.abs() > 1.96).sum())\n        SEL[(band, k)] = set(p.pair[p.z.abs() > 1.96])\n        print(f\"  {READ[k]}, {band}: {n} of {len(p)} ({n / len(p):.1%}); within tolerance {abs(n - exp) <= 0.1 * exp};\"\n              f\" by subject {p[p.z.abs() > 1.96].groupby('subject').size().to_dict()}\")\nprint(\"Expected under a null with |z| > 1.96 at 5%:\", round(0.05 * len(p)))\n\"\"\", tags=[\"claim:directional-pairs\"])\nresult(\"directional-pairs\")\n\n# ------------------------------------------------------------------ time-resolved\nmd(r\"\"\"\n## Time-resolved PSI: fig5a-delta-theta-epochs, fig5a-identity-direction, fig5a-spatiotemporal-bidirectional, fig5b-alpha-beta-no-sustained\n\n> Time-resolved delta-theta PSI differed between conditions in sustained epochs at 0 to 120 ms and\n> 470 to 610 ms (identity against spatial) and at 0 to 170 ms and 660 to 860 ms (identity against\n> temporal) after the test cue, the spatial late epoch ending about 50 ms before the temporal one\n> begins.\n\n> In identity trials the PFC led parietal sites early in processing (z > 2.62 and z > 2.35 in the\n> two contrasts' early epochs) and the parietal cortex led later (z < -3.04 and z < -3.57).\n\n> Delta-theta PSI during the selection of spatial and of temporal information stayed bidirectional\n> (net near zero) throughout the processing interval.\n\n> Time-resolved alpha-beta PSI showed significant condition differences at some time points but no\n> sustained effect for either condition in either contrast.\n\nPer P2 and psi_compute.m: per condition, the condition's ERP removed (subtracterp.m with three\nconditions), 3-cycle Hanning windows at 10-ms steps ('mtmconvol'), PSI z per pair and time point\nagainst its own surrogate null, on the pairs with processing |z| > 1.96 under the same reading (the\nselection of directional-pairs). subtracterp.m selects the temporal trials with `trialinfo(:,5)==2`,\nthe delay column, which selects none; the condition column (4) is used here. At each time point the\nmixed model (condition fixed, subject and pair random) is computed as the paired test over pairs\n(`fcx3.paired_lme`, checked against statsmodels below), FDR (Benjamini-Hochberg) over the 91 time\npoints at 0.05, sustained when a run of significant points of one sign spans at least 100 ms.\n\"\"\")\n\ncode(r\"\"\"\nTIMES = np.round(RES[\"s1\"][\"power_toi\"] * 1000).astype(int)\nTR = {}\nfor band in fcx3.BANDS:\n    for k in (\"a\", \"b\"):\n        z = {c: [] for c in (1, 2, 3)}\n        subj, pair = [], []\n        for sid in fcx3.SUBJECTS:\n            names = [f\"{sid}:{a}-{b}\" for a, b, _ in RES[sid][\"pairs\"]]\n            keep = np.array([nm in SEL[(band, k)] for nm in names])\n            for c in (1, 2, 3):\n                z[c].append(RES[sid][\"psi_t\"][band][c][k][keep])\n            subj += [sid] * int(keep.sum())\n            pair += [nm for nm, kk in zip(names, keep) if kk]\n        TR[(band, k)] = {\"z\": {c: np.concatenate(v) for c, v in z.items()}, \"subject\": np.array(subj), \"pair\": np.array(pair)}\n\n\ndef contrast_stats(band, k, other):\n    d = TR[(band, k)]\n    p, eff = [], []\n    for ti in range(len(TIMES)):\n        e, F, pv, n = fcx3.paired_lme(d[\"z\"][other][:, ti], d[\"z\"][1][:, ti], d[\"subject\"])\n        p.append(pv)\n        eff.append(e)  # identity minus other\n    p, eff = np.array(p), np.array(eff)\n    sig = fcx3.fdr_bh(p)\n    runs = []\n    for sign in (1, -1):\n        for a, b in fcx3.runs(sig & (np.sign(eff) == sign), TIMES):\n            runs.append((int(a), int(b), sign, int(b - a) >= 100))\n    return p, eff, sig, sorted(runs)\n\n\ndef grand(band, k, c):\n    d = TR[(band, k)]\n    per = pd.DataFrame(d[\"z\"][c]).groupby(d[\"subject\"]).mean()\n    return per.mean(0).values, per.std(0, ddof=1).values / np.sqrt(len(per)), per\n\n\nSTATS = {}\nfor band in fcx3.BANDS:\n    for k in (\"a\", \"b\"):\n        for other, name in [(2, \"spatial\"), (3, \"temporal\")]:\n            STATS[(band, k, name)] = contrast_stats(band, k, other)\n            p, eff, sig, runs = STATS[(band, k, name)]\n            print(f\"{band}, {READ[k]}, identity vs {name}: pairs {len(TR[(band, k)]['pair'])}; FDR-significant points {int(sig.sum())}/91;\"\n                  f\" runs (start ms, end ms, sign of identity - other, sustained) {runs}\")\n\nd = TR[(\"delta-theta\", \"a\")]\nfor ti in (0, 45, 90):\n    e2, F2, p2 = fcx3.mixedlm_check(d[\"z\"][2][:, ti], d[\"z\"][1][:, ti], d[\"subject\"], d[\"pair\"])\n    e1, F1, p1, _ = fcx3.paired_lme(d[\"z\"][2][:, ti], d[\"z\"][1][:, ti], d[\"subject\"])\n    print(f\"check at {TIMES[ti]} ms (delta-theta, a, identity vs spatial): paired {e1:.3f}, F {F1:.2f}, p {p1:.3g}; MixedLM {e2:.3f}, F {F2:.2f}, p {p2:.3g}\")\n\"\"\", tags=[\"claim:fig5a-delta-theta-epochs\", \"claim:fig5a-identity-direction\", \"claim:fig5a-spatiotemporal-bidirectional\", \"claim:fig5b-alpha-beta-no-sustained\"])\n\ncode(r\"\"\"\nfig, axes = plt.subplots(2, 2, figsize=(12, 6), sharex=True)\nfor i, band in enumerate(fcx3.BANDS):\n    for j, (other, name) in enumerate([(2, \"spatial\"), (3, \"temporal\")]):\n        ax = axes[i, j]\n        for c, col, lab in [(1, \"tab:blue\", \"identity\"), (other, \"tab:orange\" if other == 2 else \"tab:pink\", name)]:\n            m, se, _ = grand(band, \"a\", c)\n            ax.plot(TIMES, m, color=col, label=lab)\n            ax.fill_between(TIMES, m - se, m + se, color=col, alpha=0.2)\n        sig = STATS[(band, \"a\", name)][2]\n        ax.plot(TIMES[sig], np.full(sig.sum(), ax.get_ylim()[0]), \"k|\")\n        ax.axhline(0, color=\"grey\", lw=0.5)\n        ax.set_title(f\"{band}, identity vs {name}, reading (a)\")\n        ax.legend(fontsize=7)\naxes[1, 0].set_xlabel(\"ms after processing start\")\naxes[1, 1].set_xlabel(\"ms after processing start\")\nplt.tight_layout()\nplt.show()\nprint(\"Grand mean +- SEM over subjects; black marks: FDR-significant time points. Axes autoscaled, every point shown.\")\n\"\"\", tags=[\"claim:fig5a-delta-theta-epochs\"])\n\ncode(r\"\"\"\nEXP_EPOCH = {\"spatial\": [(0, 120), (470, 610)], \"temporal\": [(0, 170), (660, 860)]}\nTOL = {\"spatial\": [(None, 12), (47, 61)], \"temporal\": [(None, 17), (66, 86)]}\nfor k in (\"a\", \"b\"):\n    print(f\"{READ[k]}:\")\n    late_end = {}\n    for name in (\"spatial\", \"temporal\"):\n        runs = [r for r in STATS[(\"delta-theta\", k, name)][3] if r[3]]\n        early = [r for r in runs if r[0] <= 10]\n        late = [r for r in runs if r[0] > 10]\n        print(f\"  identity vs {name}: sustained runs {runs}; early (start within one step of 0): {early}; later: {late}\")\n        (e0, e1), (l0, l1) = EXP_EPOCH[name]\n        (_, te1), (tl0, tl1) = TOL[name]\n        ok_e = len(early) == 1 and abs(early[0][1] - e1) <= te1 and early[0][2] == 1\n        ok_l = len(late) == 1 and abs(late[0][0] - l0) <= tl0 and abs(late[0][1] - l1) <= tl1 and late[0][2] == -1\n        print(f\"    one early epoch, positive, end within tolerance: {ok_e}; one late epoch, negative, bounds within tolerance: {ok_l}\")\n        late_end[name] = late\n    if late_end[\"spatial\"] and late_end[\"temporal\"]:\n        print(f\"  gap spatial late end to temporal late start: {late_end['temporal'][0][0] - late_end['spatial'][0][1]} ms (expected 50 +- 20)\")\n\"\"\", tags=[\"claim:fig5a-delta-theta-epochs\"])\nresult(\"fig5a-delta-theta-epochs\")\n\ncode(r\"\"\"\nEPOCHS = [(\"spatial\", (0, 120), 2.62, \">\"), (\"temporal\", (0, 170), 2.35, \">\"), (\"spatial\", (470, 610), -3.04, \"<\"), (\"temporal\", (660, 860), -3.57, \"<\")]\nfor k in (\"a\", \"b\"):\n    print(f\"{READ[k]}:\")\n    mi, _, per = grand(\"delta-theta\", k, 1)\n    d = TR[(\"delta-theta\", k)]\n    for name, (a, b), exp, rel in EPOCHS:\n        m = (TIMES >= a) & (TIMES <= b)\n        other = 2 if name == \"spatial\" else 3\n    # readings: (a) grand mean over subjects averaged over the epoch; (b) all pairs pooled; (c) least extreme point; (B) identity - other\n        mo, _, _ = grand(\"delta-theta\", k, other)\n        ra = mi[m].mean()\n        rb = d[\"z\"][1][:, m].mean()\n        rc = mi[m].min() if rel == \">\" else mi[m].max()\n        rB = (mi - mo)[m].mean()\n        ok = lambda v: (v > 1.96 and (v >= exp - 0.1 * abs(exp))) if rel == \">\" else (v < -1.96 and (v <= exp + 0.1 * abs(exp)))\n        print(f\"  identity, {a}-{b} ms (expected {rel} {exp}): (a) {ra:.2f} {ok(ra)}, (b) pooled pairs {rb:.2f} {ok(rb)},\"\n              f\" (c) least extreme point {rc:.2f} {ok(rc)}, (B) identity - {name} {rB:.2f} {ok(rB)}\")\n    print(\"  per-subject identity mean z over the four epochs:\")\n    print(\"  \", {name + f\" {a}-{b}\": per.loc[:, (TIMES >= a) & (TIMES <= b)].mean(1).round(2).to_dict() for name, (a, b), _, _ in EPOCHS})\n\"\"\", tags=[\"claim:fig5a-identity-direction\"])\nresult(\"fig5a-identity-direction\")\n\ncode(r\"\"\"\nfor k in (\"a\", \"b\"):\n    for c, name in [(2, \"spatial\"), (3, \"temporal\")]:\n        m, se, per = grand(\"delta-theta\", k, c)\n        pooled = TR[(\"delta-theta\", k)][\"z\"][c].mean(0)\n        print(f\"{READ[k]}, {name}: grand mean max |z| {np.abs(m).max():.2f} at {TIMES[np.argmax(np.abs(m))]} ms;\"\n              f\" points with |z| >= 1.96: {int((np.abs(m) >= 1.96).sum())}/91; >= 1.60: {int((np.abs(m) >= 1.60).sum())};\"\n              f\" pooled pairs max |z| {np.abs(pooled).max():.2f}; per-subject max |z| {per.abs().max(1).round(2).to_dict()}\")\n\"\"\", tags=[\"claim:fig5a-spatiotemporal-bidirectional\"])\nresult(\"fig5a-spatiotemporal-bidirectional\")\n\ncode(r\"\"\"\nfor k in (\"a\", \"b\"):\n    for name in (\"spatial\", \"temporal\"):\n        p, eff, sig, runs = STATS[(\"alpha-beta\", k, name)]\n        longest = max([r[1] - r[0] for r in runs], default=None)\n        print(f\"alpha-beta, {READ[k]}, identity vs {name}: FDR-significant points {int(sig.sum())}/91 (smallest p {p.min():.3g});\"\n              f\" runs {runs}; longest {longest} ms; sustained (>= 100 ms): {[r for r in runs if r[3]]}\")\n\"\"\", tags=[\"claim:fig5b-alpha-beta-no-sustained\"])\nresult(\"fig5b-alpha-beta-no-sustained\")\n\nmd(RESULTS.get(\"summary\", \"## Summary\\n\\npending\"))\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata = {\"kernelspec\": {\"display_name\": \"Python 3\", \"language\": \"python\", \"name\": \"python3\"}}\nnbf.write(nb, \"reproduce_johnson_2019.ipynb\")\nprint(len(cells), \"cells\")\n"
}
```

```
File created successfully at: entries/crcns-fcx-3-johnson-2019/build_notebook.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
mv build_notebook.py $TMPDIR/ && python - <<'EOF'
import os
p=os.environ['TMPDIR']+'/build_notebook.py'
s=open(p).read()
s=s.replace('print("\\nCorrect trials kept equal all correct trials of 120 in:", [r.subject for r in tc.itertuples() if r._3 == r._9])',
 'print("\\nCorrect trials kept equal all correct trials of 120 in:", list(tc.subject[tc["correct kept"] == tc["correct of 120"]]))')
s=s.replace('import results_text','import sys, os\n    sys.path.insert(0, os.environ.get("TMPDIR", "."))\n    import results_text')
s=s.replace('nbf.write(nb, "reproduce_johnson_2019.ipynb")','nbf.write(nb, "entries/crcns-fcx-3-johnson-2019/reproduce_johnson_2019.ipynb")')
open(p,'w').write(s)
EOF
source $TMPDIR/dev/bin/activate && python $TMPDIR/build_notebook.py && cat > $TMPDIR/harness.py <<'EOF'
import nbformat, pickle, os, sys, time
sys.path.insert(0,'.')
import matplotlib; matplotlib.use('Agg')
nb=nbformat.read('reproduce_johnson_2019.ipynb',4)
pref=sys.argv[1] if len(sys.argv)>1 else 'res2_'
g={}
cells=[c for c in nb.cells if c.cell_type=='code']
exec(cells[0].source.replace('listing = fcx3.bucket_listing()','listing=None').split('print(listing')[0], g)
exec("CHAN = fcx3.channel_table()\nSUMMARY = fcx3.summary_file()\nMETA, RES = {}, {}", g)
for s in g['fcx3'].SUBJECTS:
    g['META'][s], g['RES'][s] = pickle.load(open(os.environ['TMPDIR']+f'/{pref}{s}.pkl','rb'))
for c in cells[2:]:
    tags=c.metadata.get('tags',[])
    if 'sanity' in tags and pref!='res2_': continue
    print('=====', tags); t=time.time()
    exec(c.source, g)
    print('[%.1fs]'%(time.time()-t))
EOF
date -u; timeout 1200 python $TMPDIR/harness.py res_ 2>&1 | tail -150
```

```
62 cells
Sun Nov  8 20:06:55 UTC 2026
(a) all 120 trials, condition as one term: slope -0.128 (SE 0.120), Wald z -1.07, p 0.283; likelihood ratio chi2(1) 1.15, p 0.283
(a) condition as two dummy terms: likelihood ratio chi2(2) 3.66, p 0.160
(b) kept trials, condition as one term: slope -0.134, likelihood ratio chi2(1) 1.18, p 0.276
accuracy over kept trials per subject: {'s1': 0.85, 's2': 0.792, 's3': 0.858, 's4': 0.933, 's5': 0.792, 's6': 0.762, 's7': 0.956}
[0.1s]
===== ['claim:fig1b-rt-identity-slower']
subject  rt_identity  rt_spatial  rt_temporal
     S1       1942.0      1129.0       1442.0
     S2       2462.0      1291.0       1473.0
     S3        888.0       868.0        798.0
     S4       1110.0       947.0        985.0
     S5       3175.0      2535.0       3142.0
     S6       2965.0      2611.0       2440.0
     S7       1469.0      1037.0        989.0
(a) subject-condition means omnibus: slope -195.8 ms per condition step, F(1,19) = 6.04, p = 0.0238
   identity vs spatial: difference -513.1 ms (first longer), F(1,12) = 11.81, p = 0.0049
   identity vs temporal: difference -391.5 ms (first longer), F(1,12) = 9.39, p = 0.0098
   spatial vs temporal: difference 121.6 ms (second longer), F(1,12) = 1.43, p = 0.2544
[... 132 more lines not kept]
```

**Agent calls Bash**

```bash
sed -i 's/POWER_SUMMARY\.assign == "a"/POWER_SUMMARY["assign"] == "a"/g' $TMPDIR/build_notebook.py && grep -c '\["assign"\] == "a"' $TMPDIR/build_notebook.py && source $TMPDIR/dev/bin/activate && python $TMPDIR/build_notebook.py && timeout 1800 python $TMPDIR/harness.py res_ 2>&1 | sed -n '/power-difficulty/,$p' | tail -120
```

```
2
62 cells
===== ['claim:power-difficulty-subjects']
         RT id > sp  acc id < sp  RT id > tp  acc id < tp  RT id > mean(sp,tp)  acc id < mean(sp,tp)  both (a) spatial  both (a) temporal  both (b)
subject                                                                                                                                            
s1             True         True        True        False                 True                  True              True              False      True
s2             True        False        True        False                 True                 False             False              False     False
s3             True        False        True         True                 True                  True             False               True      True
s4             True         True        True         True                 True                  True              True               True      True
s5             True        False        True        False                 True                 False             False              False     False
s6             True        False        True        False                 True                 False             False              False     False
s7             True         True        True         True                 True                  True              True               True      True
adjacent: identity>spatial ['s4', 's7'], identity>temporal ['s1', 's4', 's7']; every one has both under (a): False, under (b): True; other subjects with both, (a): ['s3'], (b): ['s3']
distance: identity>spatial ['s4', 's7'], identity>temporal ['s1', 's7']; every one has both under (a): False, under (b): True; other subjects with both, (a): ['s3'], (b): ['s3']
none: identity>spatial ['s4'], identity>temporal ['s1', 's4', 's7']; every one has both under (a): False, under (b): True; other subjects with both, (a): ['s3'], (b): ['s3']
[0.0s]
===== ['claim:power-low-frequencies']
neighbours reading            effe
[... 95 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import os
p=os.environ['TMPDIR']+'/build_notebook.py'
s=open(p).read()
s=s.replace('v = persub.xs(("delta-theta", "processing", k), level=("band", "interval", "reading"))','v = persub.loc[("delta-theta", "processing", k)]')
s=s.replace('v = persub.xs(("alpha-beta", "processing", k), level=("band", "interval", "reading"))','v = persub.loc[("alpha-beta", "processing", k)]')
open(p,'w').write(s)
EOF
source $TMPDIR/dev/bin/activate && python $TMPDIR/build_notebook.py && sed -i 's/e2, F2, p2 = fcx3.mixedlm_check(d.maintenance/e2, F2, p2 = (0,0,0) if os.environ.get("SKIPLME") else fcx3.mixedlm_check(d.maintenance/' reproduce_johnson_2019.ipynb && SKIPLME=1 timeout 1800 python -c "
import os; exec(open(os.environ['TMPDIR']+'/harness.py').read().replace('g={}','g={\"os\":os}'))" res_ 2>&1 | sed -n '/fig4a-delta-theta-shift: expected/,$p' | grep -v Warning | grep -v "r = m.fit\|return -self" | tail -80
```

```
62 cells
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && SKIPLME=1 timeout 1800 python -c "
import os,sys; sys.argv=['h','res_']; exec(open(os.environ['TMPDIR']+'/harness.py').read().replace('g={}','g={\"os\":os}'))" 2>&1 | grep -v Warning | grep -v "r = m.fit\|return -self" | tail -60
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/nbformat/__init__.py", line 169, in read
    buf = fp.read()
          ^^^^^^^
AttributeError: 'str' object has no attribute 'read'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/nbformat/reader.py", line 19, in parse_json
    nb_dict = json.loads(s, **kwargs)
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/json/__init__.py", line 352, in loads
    return _default_decoder.decode(s)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/json/decoder.py", line 345, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/json/decoder.py", line 361, in raw_decode
    obj, end = self.scan_once(s, idx)
               ~~~~~~~~~~~~~~^^^^^^^^
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && python $TMPDIR/build_notebook.py && sed -i "s/^for s in g\['fcx3'\].SUBJECTS:/if os.environ.get('SKIPLME'): g['fcx3'].mixedlm_check=lambda *a: (0,0,1)\nfor s in g['fcx3'].SUBJECTS:/" $TMPDIR/harness.py && sed -i 's/^import nbformat, pickle, os, sys, time/import nbformat, pickle, os, sys, time/' $TMPDIR/harness.py && SKIPLME=1 timeout 1800 python $TMPDIR/harness.py res_ 2>&1 | grep -v Warning | grep -v "r = m.fit\|return -self" | sed -n '/fig4a-delta-theta-shift: expected/,$p'
```

```
62 cells
fig4a-delta-theta-shift: expected 6 subjects with processing z > 0, mean 6.01 (tol 0.6 or larger), F 1936.10 +- 193.6
  (a) trial-averaged coherency: subjects above 0: 2/7 ['s2', 's5']; mean of 7 -0.15 +- 0.20; mean of those above 0 0.09; model effect +0.07, F 1.2, p 0.272
  (b) per-trial PSI averaged: subjects above 0: 4/7 ['s2', 's3', 's6', 's7']; mean of 7 -0.17 +- 9.53; mean of those above 0 6.26; model effect +9.18, F 59.1, p 2.22e-14
  deposited code (no conjugate): subjects above 0: 7/7 ['s1', 's2', 's3', 's4', 's5', 's6', 's7']; mean of 7 50.82 +- 12.31; mean of those above 0 50.82; model effect -8.96, F 26.2, p 3.34e-07
fig4c-alpha-beta-shift: expected every subject below 0 in processing, mean -12.60 (tol 1.26 or more negative), F 2302.30 +- 230.2
  (a) trial-averaged coherency: subjects below 0: 5/7; mean -0.03 +- 0.26; model effect +0.12, F 6.2, p 0.0125
  (b) per-trial PSI averaged: subjects below 0: 5/7; mean -1.89 +- 10.43; model effect +8.83, F 115.2, p 3.04e-26
  deposited code (no conjugate): subjects below 0: 0/7; mean 71.37 +- 10.45; model effect -7.13, F 44.4, p 3.29e-11
[0.0s]
===== ['claim:directional-pairs']
directional-pairs: pairs with processing |z| > 1.96, expected delta-theta 1008 (+-100.8), alpha-beta 984 (+-98.4), of all pairs
  (a) trial-averaged coherency, delta-theta: 264 of 1135 (23.3%); within tolerance False; by subject {'s1': 6, 's2': 31, 's3': 171, 's4': 16, 's5': 26, 's6': 10, 's7': 4}
  (a) trial-averaged coherency, alpha-beta: 118 of 1135 (10.4%); within tolerance False; by subject {'s1': 2, 's2': 13, 's3': 81, 's4': 4, 's5': 17, 's7': 1}
  (b) per-trial PSI averaged, delta-theta: 1014 of 1135 (89.3%); within tolerance True; by subject {'s1': 20, 's2': 95, 's3': 679, 's4': 27, 's5': 142, 's6': 31, 's7': 20}
  (b) per-trial PSI averaged, alpha-beta: 1043 of 1135 (91.9%); within tolerance True; by subject {'s1': 20, 's2': 105, 's3': 704, 's4': 27, 's5': 137, 's6': 31, 's7': 19}
  deposited code (no conjugate), delta-th
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,80p tools/entry.py; grep -n "def \|hash\|executed" tools/entry.py | head -80
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
[... 89 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-fcx-3-johnson-2019 && python - <<'EOF'
s=open('fcx3.py').read()
old='''    if deposited:
        cs = Fa * Fb
        den = np.sqrt((Fa ** 2) * np.conj(Fb ** 2))
        ptr_c = cs / den
        obs["code"] = _slope(ptr_c).mean(0)
        ref["code"] = ptr_c.mean(0)'''
new='''    if deposited:
        for key, (X, Y) in {"code": (Fa, Fb), "code_rev": (Fb, Fa)}.items():
            cs = X * Y
            den = np.sqrt((X ** 2) * np.conj(Y ** 2))
            ptr_c = cs / den
            obs[key] = _slope(ptr_c).mean(0)
            ref[key] = ptr_c.mean(0)'''
assert old in s; s=s.replace(old,new)
s=s.replace('''    out = {}
    for k in obs:
        zs = []''','''    out = {}
    for k in obs:
        zs = []''')
# negate code_rev at the end
old='''        out[k] = np.mean(zs, axis=0)'''
new='''        out[k] = np.mean(zs, axis=0) * (-1 if k == "code_rev" else 1)'''
assert old in s; s=s.replace(old,new)
s=s.replace("""    'code': psianalysis.m as deposited, whose cross-spectrum lacks the conjugate.""","""    'code': psianalysis.m as deposited, whose cross-spectrum lacks the conjugate, with PFC as its first
    channel, and 'code_rev' the same with parietal as its first channel, sign reversed so that
    positive still means PFC leads.""")
open('fcx3.py','w').write(s)
EOF
grep -n "code_rev" fcx3.py; date -u; source $TMPDIR/dev/bin/activate && PYTHONPATH=. python $TMPDIR/devall2.py s7 s1 s2 s4 s5 s6 s3; date -u
```

```
539:    channel, and 'code_rev' the same with parietal as its first channel, sign reversed so that
555:        for key, (X, Y) in {"code": (Fa, Fb), "code_rev": (Fb, Fa)}.items():
578:        out[k] = np.mean(zs, axis=0) * (-1 if k == "code_rev" else 1)
Sun Nov  8 20:08:55 UTC 2026
s7 46 1.243492
s1 114 2.303156
s2 150 3.009232
s4 91 3.009232
s5 208 5.347684
s6 98 5.347684
s3 359 6.868948
Sun Nov  8 20:26:42 UTC 2026
```

**Agent calls Bash**

```bash
python - <<'EOF'
import os
p=os.environ['TMPDIR']+'/build_notebook.py'
s=open(p).read()
s=s.replace('READ = {"a": "(a) trial-averaged coherency", "b": "(b) per-trial PSI averaged", "code": "deposited code (no conjugate)"}',
 'READ = {"a": "(a) trial-averaged coherency", "b": "(b) per-trial PSI averaged", "code": "deposited code (no conjugate)",\n        "code_rev": "deposited code, parietal first, sign reversed"}')
s=s.replace('for k in ("a", "b", "code"):','for k in ("a", "b", "code", "code_rev"):')
s=s.replace("cross-spectral density and Nolte et al. 2008). Both readings are run with the conjugate, and the\ndeposited code as a variant. Positive z: PFC leads.",
 "cross-spectral density and Nolte et al. 2008). Both readings are run with the conjugate, and the\ndeposited code as a variant, with either channel first (its measure is not antisymmetric). Positive z: PFC leads.")
open(p,'w').write(s)
print(s.count('"code", "code_rev"'))
EOF
source $TMPDIR/dev/bin/activate && python $TMPDIR/build_notebook.py && timeout 1800 python $TMPDIR/harness.py res2_ 2>&1 | grep -v Warning | grep -v "r = m.fit\|return -self" > $TMPDIR/out2.txt; date -u; head -c 9000 $TMPDIR/out2.txt
```

```
5
62 cells
Sun Nov  8 20:27:49 UTC 2026
===== ['sanity']
subject     fs primary (samples, channels)  elec_labels    elec_labels file  derived channels  analysed  trials (derived)  trials (table)  trialinfo = table  hdr nSamples
     s1 1000.0               (1140000, 72)           72 MATLAB 7.3 MAT-file                46        23               120             120               True       1140000
     s2 1000.0                (940001, 96)           96 MATLAB 7.3 MAT-file                64        32               120             120               True        940001
     s3 1000.0               (840656, 256)          256 MATLAB 5.0 MAT-file               155        68               120             120               True        840656
     s4 1000.0               (793027, 116)          116 MATLAB 7.3 MAT-file                29        17               120             120               True        793027
     s5 1000.0              (1017999, 172)          172 MATLAB 7.3 MAT-file               118        26               120             120               True       1017999
     s6 1000.0               (985999, 108)          108 MATLAB 7.3 MAT-file                60        12               101             101               True        985999
     s7  512.0               (445952, 101)          101 MATLAB 7.3 MAT-file                43         9                90              90               True        431506

Description: 7 subjects; S1-6 at 1 kHz, S7 at 512 Hz; derived 'fsample: 1000'; trialinfo 6 columns as listed.

Epoch time axes (s), samples per trial, value ranges (microvolts as stored; the files give no unit):
subject        epoch     fs   t0       t1            lengths starts    min   max    sd
     s1     data_pre 1000.0 -1.5 3.000000             [4501] [-1.5] -242.6 313.3 31.21
     s1 data_encmain 1000.0 -1.5 2.997000 [4498, 4499, 4500] [-1.5] -257.1 313.3 31.37
     s1    data_proc 1000.0 -1.5 3.000000             [4501] [-1.5] -257.1 313.3 31.41
[... 67 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/s7     data_pre/,/claim:fig1b-accuracy/p' $TMPDIR/out2.txt | head -60
```

```
s7     data_pre  512.0 -1.5 3.000000             [2305] [-1.5]  -81.4  55.9  7.56
     s7 data_encmain  512.0 -1.5 2.998047             [2304] [-1.5]  -81.4  57.4  7.60
     s7    data_proc  512.0 -1.5 3.000000             [2305] [-1.5]  -83.5  57.4  7.58
[0.0s]
===== ['sanity']
Trial tables: rows, trial numbers, accuracy, condition and jitter codes
subject  rows trial numbers  unique  correct  incorrect type codes condition codes  type matches condition      jitter  rt range ms                             H-G (s) I-H-jitter (s)
     s1   120         1-120    True      102         18     [1, 2]       [1, 2, 3]                    True [900, 1150] (349, 11416)                               [1.9]          [1.4]
     s2   120         1-120    True       95         25     [1, 2]       [1, 2, 3]                    True [900, 1150] (519, 25044)                               [1.9]          [1.4]
     s3   120         1-120    True      103         17     [1, 2]       [1, 2, 3]                    True [900, 1150]  (394, 2300)                               [1.9]          [1.4]
     s4   120         1-120    True      112          8     [1, 2]       [1, 2, 3]                    True [900, 1150]  (384, 3102)                               [1.9]          [1.4]
     s5   120         1-120    True       95         25     [1, 2]       [1, 2, 3]                    True [900, 1150] (435, 27953)                               [1.9]          [1.4]
     s6   101         1-120    True       77         24     [1, 2]       [1, 2, 3]                    True [900, 1150] (952, 11331)                               [1.9]          [1.4]
     s7    90         1-120    True       86          4     [1, 2]       [1, 2, 3]                    True [900, 1150]  (499, 4529) [1.87, 1.88, 1.89, 1.9, 1.91, 1.92]          [1.4]

Task timing (Methods, Behavioral Task): pretrial 1 s, start screen 0.8 s, fixation 0.1 s, stimuli 2 x 0.2 s, delay 0.9 or 1.15 s, cue 0.8 s.
[0.0s]
===== ['sanity']
Derived epochs loc
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/Neighbour pairs per reading/,/claim:fig1b-accuracy/p' $TMPDIR/out2.txt; sed -n "/claim:table1-electrodes/,/claim:fig2-spatial-power', 'claim:fig3-temporal-power'\]/p" $TMPDIR/out2.txt
```

```
Neighbour pairs per reading of the cluster test's 'neighboring electrodes':
          s1  s2   s3  s4  s5  s6  s7
adjacent  13  21   56  11  19   8   5
distance  14  41  112  17  48  18   6
none       0   0    0   0   0   0   0
[0.0s]
===== ['claim:table1-electrodes']
subject  PFC PFC hemi  parietal parietal hemi  Table 1 PFC T1 PFC hemi  Table 1 parietal T1 par hemi  pairs
     s1   21      L+R         2           L+R           21         L+R                 2         L+R     21
     s2   24      L+R         8           L+R           24         L+R                 8         L+R    116
     s3   54        R        14             R           54           R                14           R    756
     s4   12      L+R         5             R           12         L+R                10           R     30
     s5   10        L        16             L           10           L                16           L    160
     s6    8        L         4             L            8           L                 4           L     32
     s7    4        L         5             L            4           L                 5           L     20

analysed channels 187 (paper 192); PFC per subject 4-54 mean 19.00 (paper 4-54, 19); parietal 2-16 mean 7.71 (paper 2-16, 8)
same-hemisphere PFC-parietal pairs 1135 (paper 1129); difference 6 (+0.5%); channels -2.6%
subjects differing from Table 1: ['s4']
With Table 1's 10 right parietal channels in s4, its pairs would be 6 x 10 = 60, total 1165.
[... 125 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n "/claim:fig2-spatial-power', 'claim:fig3-temporal-power'\]/,/claim:fig4-maintenance-parietal-led'\]/p" $TMPDIR/out2.txt | grep -v "^ spatial\|^temporal" | head -120; grep -n "^ spatial \|^temporal " $TMPDIR/out2.txt | head -60
```

```
===== ['claim:fig2-spatial-power', 'claim:fig3-temporal-power']
==== identity against spatial
subject  n  other>identity  identity>other  p other>identity  p identity>other
     s1 23               0               0             0.333             0.633
     s2 32               8               0             0.000             0.563
     s3 68              31               0             0.000             0.157
     s4 17               4               2             0.000             0.024
     s5 26              12               0             0.009             0.996
     s6 12               7               0             0.000             0.997
     s7  9               0               3             0.644             0.008
==== identity against temporal
subject  n  other>identity  identity>other  p other>identity  p identity>other
     s1 23               0               3             0.699             0.004
     s2 32               0               0             0.059             0.977
     s3 68              34               0             0.000             0.462
     s4 17               4               1             0.000             0.049
     s5 26              15               0             0.000             0.695
     s6 12               3               0             0.010             0.751
     s7  9               3               3             0.013             0.000
contrast neighbours  alpha per tail assign  subjects other>id  subjects id>other   % other>id   % id>other  match  counts within 1
[... 128 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json; s=json.load(open('schemas/attempt.schema.json'))
print(json.dumps(s,indent=0)[:7000])"; sed -n 150,330p attempts/001453-fouke-2025-01.yaml | grep -n "findings\|kind:\|statement\|claim:\|  - \|question\|verif" | head -40
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
"dataset",
"paper",
"date",
"provenance",
"outcomes"
],
"properties": {
"schema_version": {
"const": 2
},
"id": {
[... 396 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json; s=json.load(open('schemas/attempt.schema.json'))
p=s['properties']
for k in ['inputs','findings']: print(k, json.dumps(p.get(k),indent=0)[:1500])
print([k for k in p])"; sed -n '/^findings:/,$p' attempts/001453-fouke-2025-01.yaml | tail -30; cat entries/001453-fouke-2025/entry.yaml | head -3; python -c "
import json; s=json.load(open('schemas/entry.schema.json')); print(json.dumps(s['properties'],indent=0)[:2500])"
```

```
inputs {
"description": "Everything the attempt used that is not in the dataset.",
"type": "array",
"items": {
"type": "object",
"additionalProperties": false,
"required": [
"what",
"source"
],
"properties": {
"what": {
"type": "string",
"minLength": 1
},
"source": {
"description": "A DOI, or a repository URL with the commit read.",
"type": "string",
"minLength": 1
}
[... 166 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 143,312p tools/entry.py | grep -n "version\|names\|related\|crcns\|unversioned" | head -30
```

```
34:    # Datasets are related as <archive>:<id>/<version> (docs/archives.md); papers as doi:, entries as entry:.
36:            for r in entry.get("related", []) if not r["id"].startswith(("doi:", "entry:"))]
38:                for r in entry.get("related", []) if not r["id"].startswith(("doi:", "entry:"))}
40:    versions = {d: v for d, _, v in used}
44:        for d, v in versions.items():
46:                report.error(rel / "entry.yaml", f"pin the version of dataset {d}, as {archives[d]}:{d}/<version>")
51:        nb = nbformat.read(path, as_version=4)
59:                report.error(rel / name, f"neither the notebook nor a helper names dataset {dandiset}")
60:            version = versions[dandiset]
61:            if version and version not in code and version not in helper_code:
62:                report.error(rel / name, f"neither the notebook nor a helper names version {version} "
91:        pinned = versions.get(dataset_id(attempt))
92:        version = (attempt.get("dataset") or {}).get("version")
93:        # The entry streams the version of its latest attempt; earlier attempts keep the version they used.
94:        if pinned and path == mine[-1] and version != pinned:
95:            report.error(where, f"dataset version {version!r} differs from {pinned!r} in entry.yaml")
123:                report.error(where, "claims take names for the dataset's codes from elsewhere (`with_labels`), so "
124:                                    "list the source under `inputs` and record the missing names as a finding "
142:            # A claim on data in another archive names where they are, so it is never blocked for missing data,
165:                nb = nbformat.read(entry_dir / notebook, as_version=4)
```

**Agent calls Bash**

```bash
sed -n "/claim:fig4-maintenance-parietal-led'\]/,\$p" $TMPDIR/out2.txt | cut -c1-400
```

```
===== ['claim:fig4-maintenance-parietal-led']
fig4-maintenance-parietal-led: expected delta-theta -40.03 (tol 4.0 or more negative), alpha-beta -30.37 (tol 3.04 or more negative)
  (a) trial-averaged coherency, delta-theta: subjects below -1.96: 0/7; mean over subjects 0.03 +- 0.36; pooled pairs -0.17 +- 1.64; pairs below -1.96 170/1135, above 1.96 116; within tolerance or beyond: (a) False, (b) False
  (a) trial-averaged coherency, alpha-beta: subjects below -1.96: 0/7; mean over subjects -0.12 +- 0.23; pooled pairs 0.02 +- 1.19; pairs below -1.96 49/1135, above 1.96 58; within tolerance or beyond: (a) False, (b) False
  (b) per-trial PSI averaged, delta-theta: subjects below -1.96: 4/7; mean over subjects -0.31 +- 10.67; pooled pairs -4.38 +- 28.71; pairs below -1.96 563/1135, above 1.96 458; within tolerance or beyond: (a) False, (b) False
  (b) per-trial PSI averaged, alpha-beta: subjects below -1.96: 0/7; mean over subjects 2.12 +- 2.07; pooled pairs 0.59 +- 17.42; pairs below -1.96 493/1135, above 1.96 538; within tolerance or beyond: (a) False, (b) False
  deposited code (no conjugate), delta-theta: subjects below -1.96: 0/7; mean over subjects 58.54 +- 11.36; pooled pairs 58.05 +- 46.00; pairs below -1.96 0/1135, above 1.96 1134; within tolerance or beyond: (a) False, (b) False
  deposited code (no conjugate), alpha-beta: subjects below -1.96: 0/7; mean over subjects 69.33 +- 9.67; pooled pairs 75.35 +- 26.85; pairs below -1.96 0/1135, above 1.96 1135; within tolerance or beyond: (a) False, (b) False
  deposited code, parietal first, sign reversed, delta-theta: subjects below -1.96: 7/7; mean over subjects -55.56 +- 6.79; pooled pairs -57.02 +- 45.90; pairs below -1.96 1135/1135, above 1.96 0; within tolerance or beyond: (a) True, (b) True
  deposited code, parietal first, sign reversed, alpha-beta: subjects below -1.96: 7/7; mean over subjects -69.73 +- 9.98; pooled pairs -77.92 +- 25.85; pairs below -1.96 1135/1135, above 1.96 0; within tolerance or beyond
[... 93 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/results_text.py",
 "content": "RESULTS = {}\n\nRESULTS[\"table1-electrodes\"] = \"\"\"**Result: partially reproduced.** The data set's channel list holds 187 analysed channels, not\n192: S4 has 5 right parietal channels where Table 1 gives 10; every other subject's counts and\nhemispheres equal Table 1. PFC counts per subject are 4 to 54 (mean 19.00) and parietal 2 to 16\n(mean 7.71), both within tolerance. The list gives 1135 same-hemisphere pairs, 6 more than the\npaper's 1129 (+0.5%); with Table 1's 10 parietal channels in S4 it would give 1165. The totals\ndiffer by no more than 10% (channels -2.6%), the criterion's partial match.\"\"\"\n\nRESULTS[\"trial-counts\"] = \"\"\"**Result: reproduced.** Correct trials kept average 95.71 per subject (paper 96); identity\n32.14 +- 3.13 (26 to 35), spatial 32.86 +- 4.30 (27 to 39), temporal 30.71 +- 6.47 (20 to 39), the\npaper's means and ranges. Incorrect trials kept (reading (b)) average 17.29 +- 8.44 (4 to 25),\nthe paper's 17 +- 8 (4 to 25); incorrect trials of all 120 (reading (a)) average 18.29 (6 to 29),\noutside the widened range. In S1 to S5 every correct trial of the 120 was kept.\"\"\"\n\nRESULTS[\"fig1b-accuracy\"] = \"\"\"**Result: reproduced.** Under reading (b), per subject and condition, accuracy runs from 0.625 to\n0.975, the paper's 0.63 to 0.98; under reading (a), per subject, it runs from 0.758 to 0.950, and the\nlowest value is outside 0.63 +- 0.063. The logit mixed model on all 120 trials finds no effect of\ncondition (likelihood ratio p = 0.283 with condition as one term, p = 0.160 as two terms; kept\ntrials p = 0.276), so the absence holds by the criterion (p > 0.05). The paper reports p > 0.50;\nthe p obtained here is lower than that.\"\"\"\n\nRESULTS[\"fig1b-rt-identity-slower\"] = \"\"\"**Result: reproduced.** On subject-condition means (reading (a)), condition affects RT\n(F(1,19) = 6.04, p = 0.024), identity RT is longer than spatial (by 513 ms, F(1,12) = 11.81, p =\n0.005) and temporal (by 392 ms, F(1,12) = 9.39, p = 0.010), and spatial and temporal do not differ\n(p = 0.254). Identity RT is the longest in all 7 subjects. The F values are below the paper's\nbounds (F > 6.50, > 13.78, > 10.95), and the d values (1.30, 1.16, by the definition used here)\nbelow its 2.14 and 1.91. Single kept trials (reading (b)) give the same pattern (p = 0.018, 0.037,\n0.004 and 0.844).\"\"\"\n\nRESULTS[\"erp-no-condition-difference\"] = \"\"\"**Result: reproduced, resting on an assumption.** With neighbours adjacent by contact number\nand clusters judged at 0.05 per tail, no subject has a significant ERP cluster in either contrast\n(smallest p 0.053, S2 identity against temporal). The neighbour rule is not stated; the adjacency\nreading is adopted (see the Summary). Under the distance reading S5 has a cluster at p = 0.028\n(identity against spatial), and with no spatial clustering S2 has one at p = 0.033; neither is\nbelow 0.025. The paper reports all p > 0.10; 2 of the 14 subject-contrasts have p <= 0.10 under\nthe adopted reading.\"\"\"\n\nRESULTS[\"fig2-spatial-power\"] = \"\"\"**Result: partially reproduced.** Under the adopted reading (adjacent neighbours, 0.05 per tail,\nreading (a) of the assignment), 5 subjects show spatial > identity effects (S2, S3, S4, S5, S6) and\n2 show identity > spatial effects (S4, S7), the paper's counts. The percentages of electrodes are\n39.7 +- 15.0% and 22.5 +- 15.3%, below the paper's 54 +- 22% and 36 +- 12%. No reading of neighbours,\nthreshold or assignment matches both percentages: the distance reading gives 49.7% (within\ntolerance) and 28.4% (outside). The significant clusters have p <= 0.024.\"\"\"\n\nRESULTS[\"fig3-temporal-power\"] = \"\"\"**Result: partially reproduced.** Under the adopted reading, 5 subjects show temporal > identity\neffects (paper 4) and 3 show identity > temporal effects (paper 2), each within one subject;\nadjacent neighbours at 0.025 per tail with reading (b) of the assignment give the paper's 4 and 2.\nThe percentages, 37.9 +- 15.3% and 17.4 +- 14.2% (adopted reading), are below the paper's 68 +- 30%\nand 37 +- 10% under every reading. S4's identity > temporal cluster has p = 0.049, above the paper's\n\"all p < 0.04\".\"\"\"\n\nRESULTS[\"power-difficulty-subjects\"] = \"\"\"**Result: reproduced.** The subjects with identity > spatial or temporal effects are S1, S4 and\nS7 (adjacent neighbours; S1 and S7, or S1, S4 and S7, under the other neighbour readings). Under\nreading (b), identity against the mean of spatial and temporal, each of them has longer identity\nRT and lower identity accuracy. Under reading (a) S1 fails for the temporal contrast, where its\nidentity and temporal accuracy are equal (0.825). One other subject, S3, also has both under either\nreading without an identity > effect, so the converse (\"the same subjects\") does not hold. Identity\nRT is the longest in all 7 subjects, so only accuracy separates subjects here.\"\"\"\n\nRESULTS[\"power-low-frequencies\"] = \"\"\"**Result: reproduced, resting on an assumption.** With neighbours by distance and the density\nover all points (reading (b)), each of the three effects is larger over 2 to 24 Hz than over 25 to\n40 Hz (0.127 against 0.032, 0.115 against 0.037, 0.045 against 0.016) and has local maxima in 2 to 7\nHz and in 9 to 24 Hz. With adjacent neighbours, reading (b), the first part holds for all three, but\nthe spatial > identity density has one maximum (14 Hz) and none in 2 to 7 Hz. Over masked points\nonly (reading (a)) the identity > other density is larger above 24 Hz under every neighbour\nreading. The distance reading places contacts on the grids by an assumption (Data check).\"\"\"\n\nRESULTS[\"fig4-maintenance-parietal-led\"] = \"\"\"**Result: not reproduced.** Under neither PSI reading is maintenance parietal-led in every\nsubject. Reading (a) gives subject means from -0.52 to 0.56 (delta-theta) and -0.45 to 0.21\n(alpha-beta), with no subject below -1.96; reading (b) gives 4 of 7 subjects below -1.96 in\ndelta-theta (mean -0.31 +- 10.67) and none in alpha-beta (mean 2.12 +- 2.07). The paper reports\n-40.03 +- 8.73 and -30.37 +- 2.60. The deposited code, without the conjugate and with the parietal\nchannel first, gives every subject below -1.96 (means -55.56 and -69.73); with the PFC channel first\nthe same code gives +58.54 and +69.33, so its sign depends on the order of the channels and does\nnot measure direction.\"\"\"\n\nRESULTS[\"fig4a-delta-theta-shift\"] = \"\"\"**Result: partially reproduced.** Under reading (b), processing delta-theta PSI z is higher than\nmaintenance (by 9.18, F(1,2268) = 59.1, p = 2.2e-14; the paper's F is 1936.10), and 4 subjects\n(S2, S3, S6, S7) have net z above 0 in processing, the criterion's partial match; the paper has 6.\nTheir mean is 6.26 (all seven -0.17 +- 9.53; paper 6.01 +- 6.42). Under reading (a) the interval\neffect is absent (0.07, p = 0.272) and 2 subjects are above 0. The deposited code with either channel\norder puts every subject on one side of zero, 0 of 7 above 0 with the parietal channel first.\"\"\"\n\nRESULTS[\"fig4c-alpha-beta-shift\"] = \"\"\"**Result: not reproduced.** Processing alpha-beta PSI z is higher than maintenance under both\nreadings ((a) 0.12, p = 0.013; (b) 8.83, F = 115.2, p = 3.0e-26; paper F = 2302.30), but only 5 of 7\nsubjects stay below 0 in processing under either reading (criterion: all 7, or at least 6 for a\npartial match), and the means (-0.03 and -1.89) are far from -12.60. The deposited code with the\nparietal channel first gives all 7 below 0 (mean -73.15), with a shift of 5.12 (p = 2.6e-06).\"\"\"\n\nRESULTS[\"directional-pairs\"] = \"\"\"**Result: reproduced.** Under reading (b), 1014 of 1135 pairs are directional in delta-theta\n(paper 1008) and 1043 in alpha-beta (paper 984), both within tolerance. Under reading (a) the counts\nare 264 and 118. Under reading (b) the null is the frequency-shuffled trial-mean spectrum, as in\npsianalysis.m, while the observed value is the mean of per-trial PSI; with 1135 pairs a null at 5%\nwould give about 57, and 89 to 92% of pairs pass, so the count reflects how this z is scaled as much\nas directionality.\"\"\"\n\nRESULTS[\"fig5a-delta-theta-epochs\"] = \"\"\"**Result: not reproduced.** Under reading (a) no time point differs between conditions after FDR.\nUnder reading (b) there are sustained differences, but not the paper's: identity against spatial at\n110-230 ms (identity higher), 300-400 ms (lower) and 460-600 ms (higher); identity against temporal\nat 120-250, 290-390 and 680-840 ms with the same signs. Neither contrast has an epoch starting at 0\nms, and the late epochs have the opposite sign to the paper's (identity higher, not lower).\"\"\"\n\nRESULTS[\"fig5a-identity-direction\"] = \"\"\"**Result: not reproduced.** In the paper's four epochs, identity-trial delta-theta PSI z is\nbelow 1.96 in absolute value under every reading of the averaging and of what is measured, except\nreading (b) of PSI in the last epoch, where it is positive (4.44, the paper's sign is negative).\nUnder PSI reading (a) the grand means are 0.35, 0.38, -0.25 and -0.21; under (b) 0.82, 1.25, 1.33 and\n4.44 (paper > 2.62, > 2.35, < -3.04, < -3.57).\"\"\"\n\nRESULTS[\"fig5a-spatiotemporal-bidirectional\"] = \"\"\"**Result: not reproduced, resting on an assumption.** On the grand mean, with PSI reading (b)\nadopted (see the Summary), spatial-trial delta-theta PSI z reaches |z| = 5.44 (110 ms) and\ntemporal-trial 6.36 (630 ms), with 42 and 40 of 91 time points at |z| >= 1.96; the paper reports\nall |z| < 1.60. Under reading (a), where few pairs are directional, the grand means stay below 0.35\nand 0.72 at every point, which would meet the criterion.\"\"\"\n\nRESULTS[\"fig5b-alpha-beta-no-sustained\"] = \"\"\"**Result: reproduced, resting on an assumption.** With PSI reading (b) adopted, 66 (identity\nagainst spatial) and 75 (against temporal) of 91 time points differ after FDR, and the longest run\nof one sign lasts 80 and 90 ms, below 100 ms, so no difference is sustained. Under reading (a) no\ntime point is significant after FDR (smallest p 0.0048 and 0.0016), the criterion's partial\nmatch.\"\"\"\n\nRESULTS[\"summary\"] = \"\"\"## Summary\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\n| Claim | Outcome |\n|---|---|\n| table1-electrodes | partially reproduced |\n| trial-counts | reproduced |\n| fig1b-accuracy | reproduced |\n| fig1b-rt-identity-slower | reproduced |\n| erp-no-condition-difference | reproduced (assumption: neighbours adjacent by contact number) |\n| fig2-spatial-power | partially reproduced |\n| fig3-temporal-power | partially reproduced |\n| power-difficulty-subjects | reproduced |\n| power-low-frequencies | reproduced (assumption: contact placement on the grids, distance reading) |\n| fig4-maintenance-parietal-led | not reproduced |\n| fig4a-delta-theta-shift | partially reproduced |\n| fig4c-alpha-beta-shift | not reproduced |\n| directional-pairs | reproduced |\n| fig5a-delta-theta-epochs | not reproduced |\n| fig5a-identity-direction | not reproduced |\n| fig5a-spatiotemporal-bidirectional | not reproduced (assumption: PSI reading (b)) |\n| fig5b-alpha-beta-no-sustained | reproduced (assumption: PSI reading (b)) |\n\n**How the analysis differs from the paper's.** Everything is computed in Python from the derived\nepochs, following the deposited MATLAB scripts for windows, trial selection, spectral parameters and\nthe PSI null; FieldTrip itself was not run. Three details are open in the paper and the scripts. (1)\nWhich electrodes are neighbours in the cluster test: three readings are run; for the claim of\nabsence (ERPs) the adjacency of contact numbers is adopted, since it uses only the labels, while the\ndistance reading rests on placing numbered contacts on the grids, which the files do not document.\nClusters are judged at 0.05 per tail, FieldTrip's default and the Methods' wording. (2) PSI from\ntrial-averaged cross-spectra (reading (a), Nolte et al. 2008) or per trial (reading (b), the\nstructure of psianalysis.m): the deposited psianalysis.m multiplies Fourier coefficients without the\nconjugate, so it settles neither; both are run with the conjugate, and the deposited code as a\nvariant. For the claims of absence on time-resolved PSI, reading (b) is adopted: it is the structure\nof the deposited code, and it gives the paper's counts of directional pairs (1014 and 1043 against\n1008 and 984), which reading (a) does not (264 and 118). (3) The baseline z-score of power is\ncomputed in closed form; it cannot change the condition t-tests. The mixed models are computed as\npaired tests over pairs, which equal them when every pair has both values (checked against\nstatsmodels; they differ slightly where the pair variance is estimated at zero, F 59.1 against 61.5).\n\n**What was found about the data set.** The derived epochs, the continuous data and the trial\ntables share one clock: every analysed channel's derived trace is a bipolar difference of two\ncontacts of the continuous data (r >= 0.9998), at fixed offsets from the table's columns that put the\nscripts' windows where the Methods put them. The data set lists 187 analysed channels where the paper\nreports 192 (S4 has 5 parietal channels, Table 1 10), and 1135 same-hemisphere pairs where the paper\nreports 1129. The trial tables of S6 and S7 hold only the kept trials (101 and 90), unlike the\ndescription. A timing contrast between trials with 900-ms and 1150-ms delays shows, where the\n70-150 Hz response is clear (S2, S3, S4), that the responses in the processing epoch of the 1150-ms\ntrials occur 0.21 to 0.26 s later relative to the processing column than in the 900-ms trials, and\nin S4 the same in the encoding epoch, while the pretrial epoch shows no shift; this is consistent with\nthe encoding and processing columns being about 0.25 s early in 1150-ms trials, so that their\nprocessing window would include the end of the cue, but the test does not prove it and is weak in\nthe other subjects. The deposited psi_compute.m does not run as written (an undefined `freq` and\n`savDir`, and an electrode argument tested with `nargin > 2`), subtracterp.m selects temporal trials\nby the delay column, which selects none, and psianalysis.m omits the conjugate of the\ncross-spectrum.\"\"\"\n"
}
```

```
File created successfully at: /tmp/claude-1001/results_text.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
date -u
```

```
Sun Nov  8 20:30:21 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('results_text.py').read()
old='''The subjects with identity > spatial or temporal effects are S1, S4 and
S7 (adjacent neighbours; S1 and S7, or S1, S4 and S7, under the other neighbour readings).'''
new='''The subjects with identity > spatial or temporal effects are S1, S4 and
S7 under every neighbour reading.'''
assert old in s; s=s.replace(old,new)
old='''**Result: not reproduced.** In the paper's four epochs, identity-trial delta-theta PSI z is
below 1.96 in absolute value under every reading of the averaging and of what is measured, except
reading (b) of PSI in the last epoch, where it is positive (4.44, the paper's sign is negative).
Under PSI reading (a) the grand means are 0.35, 0.38, -0.25 and -0.21; under (b) 0.82, 1.25, 1.33 and
4.44 (paper > 2.62, > 2.35, < -3.04, < -3.57).'''
new='''**Result: not reproduced.** Under PSI reading (a), identity-trial delta-theta PSI z in the
paper's four epochs is below 1.96 in absolute value under every reading of the averaging and of what
is measured (grand means 0.35, 0.38, -0.25 and -0.21; paper > 2.62, > 2.35, < -3.04, < -3.57). Under
PSI reading (b) the early values are below 1.96 (largest 1.58) and every late value is positive (up
to 7.61), the opposite sign to the paper's.'''
assert old in s; s=s.replace(old,new)
old='''in S4 the same in the encoding epoch, while the pretrial epoch shows no shift;'''
new='''in S4 the same in the encoding epoch, while the pretrial epochs of these subjects show shifts of
0.03 s or less;'''
assert old in s; s=s.replace(old,new)
open('results_text.py','w').write(s)
EOF
cd entries/crcns-fcx-3-johnson-2019 && python - <<'EOF'
s=open('fcx3.py').read()
s=s.replace('''BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/fcx-3/live"''','''DATASET = "crcns:fcx-3/unversioned"  # CRCNS data sets are not versioned (docs/archives.md)
BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/fcx-3/live"''')
open('fcx3.py','w').write(s)
EOF
cat > requirements.in <<'EOF'
aiohttp
fsspec
h5py
matplotlib
numpy
pandas
requests
scipy
statsmodels
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: crcns-fcx-3-johnson-2019
type: reproduction
title: Frontoparietal working memory iEEG (Johnson et al. 2019) from CRCNS fcx-3
description: Tests the findings of Johnson, King-Stephens, Weber, Laxer, Lin and Knight (2019) on
  CRCNS data set fcx-3, which holds intracranial recordings from prefrontal and parietal cortex of 7
  patients doing a visuospatial working memory task. It checks the channel and trial counts, the
  behaviour, ERPs and power between identity, spatial and temporal trials with per-subject cluster
  tests, and the phase slope index between prefrontal and parietal channels over the delay and in
  time.
license: Apache-2.0
notebooks:
- path: reproduce_johnson_2019.ipynb
  title: Reproducing Johnson et al. (2019) from CRCNS fcx-3
  runtime_minutes: 25
helpers:
- fcx3.py
related:
- id: crcns:fcx-3/unversioned
  relation: uses_data
- id: doi:10.3389/fnsys.2018.00065
  relation: reproduces
EOF
source $TMPDIR/dev/bin/activate && python $TMPDIR/build_notebook.py && cd  && python tools/entry.py lock entries/crcns-fcx-3-johnson-2019 2>&1 | tail -3 && python tools/entry.py check entries/crcns-fcx-3-johnson-2019 2>&1 | tail -20
```

```
62 cells
wrote entries/crcns-fcx-3-johnson-2019/requirements.lock.txt
0 error(s)
```

**Agent calls Bash**

```bash
date -u && python tools/entry.py all entries/crcns-fcx-3-johnson-2019 2>&1 | tail -15; date -u
```

```
Sun Nov  8 20:31:05 UTC 2026
Installed kernelspec registry-crcns-fcx-3-johnson-2019 in executed/crcns-fcx-3-johnson-2019/.venv/share/jupyter/kernels/registry-crcns-fcx-3-johnson-2019
0 error(s)
pass  reproduce_johnson_2019.ipynb  (1151 s)
Sun Nov  8 20:50:24 UTC 2026
```

**Agent calls Bash**

```bash
cd  source $TMPDIR/dev/bin/activate; python - <<'EOF' > $TMPDIR/exec.txt
import nbformat
nb=nbformat.read('executed/crcns-fcx-3-johnson-2019/reproduce_johnson_2019.ipynb',4)
for c in nb.cells:
    if c.cell_type=='code':
        print('=====', c.metadata.get('tags'))
        for o in c.get('outputs',[]):
            if o.get('name')=='stdout': print(o['text'])
            elif o.output_type=='error': print('ERROR', o.ename)
EOF
grep -v Warning $TMPDIR/out2.txt | grep -v "^\[" > $TMPDIR/a.txt; grep -v "^\[" $TMPDIR/exec.txt > $TMPDIR/b.txt
diff <(grep -v "^=====\|^$" $TMPDIR/a.txt) <(sed -n '/claim:table1/,$p;' $TMPDIR/b.txt | grep -v "^=====\|^$") | head -40; grep -n "ERROR\|streamed" $TMPDIR/exec.txt | head
```

```
1,89d0
< subject     fs primary (samples, channels)  elec_labels    elec_labels file  derived channels  analysed  trials (derived)  trials (table)  trialinfo = table  hdr nSamples
<      s1 1000.0               (1140000, 72)           72 MATLAB 7.3 MAT-file                46        23               120             120               True       1140000
<      s2 1000.0                (940001, 96)           96 MATLAB 7.3 MAT-file                64        32               120             120               True        940001
<      s3 1000.0               (840656, 256)          256 MATLAB 5.0 MAT-file               155        68               120             120               True        840656
<      s4 1000.0               (793027, 116)          116 MATLAB 7.3 MAT-file                29        17               120             120               True        793027
<      s5 1000.0              (1017999, 172)          172 MATLAB 7.3 MAT-file               118        26               120             120               True       1017999
<      s6 1000.0               (985999, 108)          108 MATLAB 7.3 MAT-file                60        12               101             101               True        985999
<      s7  512.0               (445952, 101)          101 MATLAB 7.3 MAT-file                43         9                90              90               True        431506
< Description: 7 subjects; S1-6 at 1 kHz, S7 at 512 Hz; derived 'fsample: 1000'; trialinfo 6 columns as listed.
< Epoch time axes (s), samples per trial, value ranges (microvolts as stored; the files give no unit):
< subject        epoch     fs   t0       t1            lengths starts    min   max    sd
<      s1     data_pre 1000.0 -1.5 3.000000             [4501] [-1.5] -242.6 313.3 31.21
<      s1 data_encmain 1000.0 -1.5 2.997000 [4498, 4499, 4500] [-1.5] -257.1 313.3 31.37
<      s1    data_proc 1000.0 -1.5 3.000000             [4501] [-1.5] -257.1 313.3 31.41
<      s2     data_pre 1000.0 -1.5 3.0
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
diff <(grep -v "^=====\|^$" $TMPDIR/a.txt) <(sed -n '/Description: 7 subjects/,$p' $TMPDIR/b.txt | grep -v "^=====\|^$") | head; diff <(grep -v "^=====\|^$" $TMPDIR/a.txt | sed -n '/Description: 7/,$p') <(sed -n '/subject     fs primary/,$p' $TMPDIR/b.txt | grep -v "^=====\|^$" | sed -n '/Description: 7/,$p') | head -30
```

```
1,8d0
< subject     fs primary (samples, channels)  elec_labels    elec_labels file  derived channels  analysed  trials (derived)  trials (table)  trialinfo = table  hdr nSamples
<      s1 1000.0               (1140000, 72)           72 MATLAB 7.3 MAT-file                46        23               120             120               True       1140000
<      s2 1000.0                (940001, 96)           96 MATLAB 7.3 MAT-file                64        32               120             120               True        940001
<      s3 1000.0               (840656, 256)          256 MATLAB 5.0 MAT-file               155        68               120             120               True        840656
<      s4 1000.0               (793027, 116)          116 MATLAB 7.3 MAT-file                29        17               120             120               True        793027
<      s5 1000.0              (1017999, 172)          172 MATLAB 7.3 MAT-file               118        26               120             120               True       1017999
<      s6 1000.0               (985999, 108)          108 MATLAB 7.3 MAT-file                60        12               101             101               True        985999
<      s7  512.0               (445952, 101)          101 MATLAB 7.3 MAT-file                43         9                90              90               True        431506
306a299
298a299
>                         code_rev              -52.22             12.29       -74.11       -39.37           -50.83          49.40   -652.99      3.67
342a344
> alpha-beta, (b) per-trial PSI averaged, identity vs spatial: pairs 1043; FDR-significant points 66/91; runs (start ms, end ms, sign of identity - other, sustained) [(0, 20, -1, False), (40, 40, -1, False), (60, 70, 1, False), (90, 110, -1, False), (130, 140, 1, False), (160, 240, 1, False), (260, 280, 1, False), (300, 300, -1, False), (340, 350, -1, False), (370, 400, 1, False), (410, 460, -1, False), (490, 500, 1, False), (520, 
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls questions | head; ls attempts | grep -i crcns; sed -n '/^verifications/,/^findings/p' attempts/001453-fouke-2025-01.yaml | head -5; grep -n "^provenance" -A12 attempts/001453-fouke-2025-01.yaml
```

```
000005.yaml
000006.yaml
000008.yaml
000009.yaml
000010.yaml
000011.yaml
000013.yaml
000015.yaml
000019.yaml
000023.yaml
crcns-ac-2-deweese-2004-01.yaml
crcns-alm-1-li-2015-01.yaml
crcns-alm-3-li-2016-01.yaml
crcns-bf-1-nair-2018-01.yaml
crcns-bf-3-moaddab-2021-01.yaml
crcns-ear-1-farrell-2020-01.yaml
crcns-fcx-1-watson-2016-01.yaml
crcns-hc-10-lee-2014-01.yaml
crcns-hc-13-yu-2017-01.yaml
crcns-hc-14-girardeau-2017-01.yaml
[... 35 more lines not kept]
```

**Agent**

Now the attempt record.

**Agent calls Write**

```json
{
 "file_path": "attempts/crcns-fcx-3-johnson-2019-01.yaml",
 "content": "schema_version: 2\nid: crcns-fcx-3-johnson-2019-01\ndataset:\n  archive: crcns\n  id: fcx-3\n  version: unversioned\n  doi: 10.6080/K06971S9\npaper: doi:10.3389/fnsys.2018.00065\ndate: 2026-11-08\nentry: crcns-fcx-3-johnson-2019\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-13\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/42513613232\noutcomes:\n- claim: table1-electrodes\n  outcome: partially_reproduced\n  notebook: reproduce_johnson_2019.ipynb\n  output: claim:table1-electrodes\n  measured:\n  - 187\n  - 1135\n  - 19.0\n  - 7.71\n  notes: The data set's list of analysed channels (docs/summary_channel_analysis.csv) holds 187\n    channels, not 192. S4 has 5 right parietal channels where Table 1 gives 10; every other\n    subject's PFC and parietal counts and hemispheres equal Table 1. PFC counts per subject are 4 to\n    54 (mean 19.00) and parietal 2 to 16 (mean 7.71). The list gives 1135 same-hemisphere\n    PFC-parietal pairs, 6 more than 1129 (+0.5%); with 10 parietal channels in S4 it would give 1165,\n    so neither count yields 1129. The totals differ by less than 10% (channels -2.6%), the\n    criterion's partial match.\n  deviations:\n  - Counted from the data set's channel list, which every analysis here uses; all listed channels are\n    present in the derived epochs.\n- claim: trial-counts\n  outcome: reproduced\n  notebook: reproduce_johnson_2019.ipynb\n  output: claim:trial-counts\n  measured:\n  - 95.71\n  - 32.14\n  - 32.86\n  - 30.71\n  - 17.29\n  notes: Correct trials kept average 95.71 per subject; identity 32.14 +- 3.13 (26 to 35), spatial\n    32.86 +- 4.30 (27 to 39), temporal 30.71 +- 6.47 (20 to 39). Incorrect trials kept (reading (b))\n    average 17.29 +- 8.44 (4 to 25), the paper's values. Incorrect trials of all 120 (reading (a), from\n    the per-subject accuracy of docs/summary_file.csv) average 18.29 with range 6 to 29, outside the\n    widened range, so (b) is the matching reading and its mean is recorded. In S1 to S5 every correct\n    trial of the 120 was kept.\n  deviations:\n  - Correct trials are those of the derived epochs with accuracy 1, the selection of the deposited\n    scripts (power_compute.m, erp_compute.m).\n- claim: fig1b-accuracy\n  outcome: reproduced\n  notebook: reproduce_johnson_2019.ipynb\n  output: claim:fig1b-accuracy\n  measured:\n  - 0.625\n  - 0.975\n  notes: Under reading (b), per subject and condition, accuracy runs from 0.625 to 0.975; under\n    reading (a), per subject over conditions, from 0.758 to 0.950, whose lowest value is outside 0.63\n    +- 0.063. All values lie inside the widened range under both readings. The logit mixed model on\n    all 120 trials finds no effect of condition (likelihood ratio p = 0.283 with condition as one\n    term, p = 0.160 as two terms; kept trials p = 0.276). The paper reports p > 0.50; the p here is\n    lower but above 0.05.\n  deviations:\n  - Accuracy over all 120 trials comes from docs/summary_file.csv (per subject and condition, over all\n    trials by the data description), rebuilt as counts out of 40 per condition (Methods, \"120 trials\n    divided evenly\"); the trial tables of S6 and S7 list only the kept trials.\n  - The logit mixed model is fitted by maximum likelihood with Gauss-Hermite quadrature in Python;\n    the paper names the model, not the software. Condition enters as one numeric term (the single\n    degree of freedom of the paper's F(1,19)), with two dummy terms as a variant.\n- claim: fig1b-rt-identity-slower\n  outcome: reproduced\n  notebook: reproduce_johnson_2019.ipynb\n  output: claim:fig1b-rt-identity-slower\n  notes: On subject-condition mean RTs (reading (a)), condition affects RT (F(1,19) = 6.04, p =\n    0.024); identity RT is longer than spatial (by 513 ms, F(1,12) = 11.81, p = 0.005) and temporal\n    (by 392 ms, F(1,12) = 9.39, p = 0.010); spatial and temporal do not differ (p = 0.254). Identity\n    RT is the longest in all 7 subjects. The F values are below the paper's bounds (F > 6.50, >\n    13.78, > 10.95) and the d values (1.30 and 1.16, mean paired difference over its SD) below its\n    2.14 and 1.91. Single kept correct trials (reading (b)) give p = 0.018, 0.037, 0.004 and 0.844.\n  deviations:\n  - Mean correct RT per subject and condition from docs/summary_file.csv (all correct trials, by the\n    data description). Reading (b) uses the kept trials only, as the trial tables of S6 and S7 hold\n    no others.\n  - The paper does not say how Cohen's d was computed; d is reported, not judged.\n- claim: erp-no-condition-difference\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_johnson_2019.ipynb\n  output: claim:erp-no-condition-difference\n  notes: With neighbours adjacent by contact number and clusters judged at 0.05 per tail, no subject\n    has a significant cluster in either contrast (smallest p 0.053, S2 identity against temporal).\n    Under the distance reading of neighbours S5 has a cluster at p = 0.028 (identity against\n    spatial); with no spatial clustering S2 has one at p = 0.033; at 0.025 per tail no reading has a\n    significant cluster. The paper reports all p > 0.10; 2 of the 14 subject-contrasts have p <= 0.10\n    under the adopted reading. The question of the neighbour rule is put to the paper's authors (see\n    findings).\n  deviations:\n  - Assumption. The paper says only that clusters were formed over \"neighboring electrodes\". The\n    readings give different outcomes, so neighbours adjacent by contact number on the same lead or\n    strip are adopted. This uses only the channel labels and follows the bipolar montage, which\n    re-references each electrode \"to the next adjacent electrode\" (Methods, Data Acquisition and\n    Preprocessing); the distance reading rests on placing numbered contacts on the grids of the\n    MNI files, whose numbering the files do not document.\n  - Clusters are judged at 0.05 per tail (the Methods' \"fewer than 5% of randomizations yielded a\n    larger effect\", and FieldTrip's default); 0.025 is shown as a variant.\n  - Filter, padding and baseline follow erp_compute.m (30-Hz FIR, 7.5-s padding, pretrial\n    [0.65, 0.85] s mean); the FIR order 3*fix(fs/30), forwards and backwards, is FieldTrip's default\n    for the script's settings, implemented in scipy (a standard choice). FieldTrip itself was not run.\n- claim: fig2-spatial-power\n  outcome: partially_reproduced\n  notebook: reproduce_johnson_2019.ipynb\n  output: claim:fig2-spatial-power\n  measured:\n  - 5\n  - 2\n  - 39.7\n  - 22.5\n  notes: With adjacent neighbours, 0.05 per tail and reading (a) of the assignment, 5 subjects show\n    spatial > identity effects (S2, S3, S4, S5, S6) and 2 identity > spatial (S4, S7), the paper's\n    counts; the percentages of electrodes are 39.7 +- 15.0% and 22.5 +- 15.3% (paper 54 +- 22% and 36\n    +- 12%). No reading matches both percentages; the distance reading gives 49.7% (within tolerance)\n    and 28.4%. The significant clusters have p <= 0.024.\n  deviations:\n  - Power follows power_compute.m (3-cycle Hanning windows, 2 to 40 Hz, 10-ms steps, processing\n    [0.3, 1.2] s of the derived epoch), computed in numpy; the derived epochs extend 1.5 s beyond the\n    windows, so no window holds padding and the S1 padding readings do not arise.\n  - The baseline z-score of zbaseline.m (r = all correct trials) is computed in closed form, the limit\n    of its 1000 draws; it is the same affine map for every trial at a channel and frequency, so it\n    cannot change the condition t-tests.\n  - Neighbour rule and threshold as in erp-no-condition-difference; every reading is shown.\n- claim: fig3-temporal-power\n  outcome: partially_reproduced\n  notebook: reproduce_johnson_2019.ipynb\n  output: claim:fig3-temporal-power\n  measured:\n  - 5\n  - 3\n  - 37.9\n  - 17.4\n  notes: With adjacent neighbours, 0.05 per tail and reading (a), 5 subjects show temporal > identity\n    effects (paper 4) and 3 identity > temporal (paper 2), each within one subject; adjacent\n    neighbours at 0.025 per tail with reading (b) of the assignment give the paper's 4 and 2. The\n    percentages (37.9 +- 15.3% and 17.4 +- 14.2%) are below the paper's 68 +- 30% and 37 +- 10% under\n    every reading. S4's identity > temporal cluster has p = 0.049, above the paper's \"all p < 0.04\".\n  deviations:\n  - As fig2-spatial-power.\n- claim: power-difficulty-subjects\n  outcome: reproduced\n  notebook: reproduce_johnson_2019.ipynb\n  output: claim:power-difficulty-subjects\n  notes: The subjects with identity > spatial or temporal effects are S1, S4 and S7 under every\n    neighbour reading. Under reading (b), identity against the mean of spatial and temporal, each has\n    longer identity RT and lower identity accuracy; under reading (a) S1 fails for the temporal\n    contrast, where its identity and temporal accuracy are equal (0.825). S3 also has both without\n    an identity > effect, so the converse does not hold. Identity RT is the longest in all 7\n    subjects, so only accuracy separates subjects.\n  deviations:\n  - Accuracy (all 120 trials) and RT from docs/summary_file.csv.\n- claim: power-low-frequencies\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_johnson_2019.ipynb\n  output: claim:power-low-frequencies\n  notes: With neighbours by distance and the density over all points (reading (b)), each effect is\n    larger over 2 to 24 Hz than over 25 to 40 Hz (0.127 against 0.032, 0.115 against 0.037, 0.045\n    against 0.016) and has local maxima in 2 to 7 Hz and in 9 to 24 Hz. With adjacent neighbours,\n    reading (b), the first part holds for all three, but the spatial > identity density has one\n    maximum (14 Hz), none in 2 to 7 Hz (a partial match). Over masked points only (reading (a)) the\n    identity > other density is larger above 24 Hz under every neighbour reading.\n  deviations:\n  - The match rests on the distance reading of neighbours, which places bipolar channels at the\n    midpoint of their two contacts, contact n being the n-th electrode of the grid named by the\n    label in the subject's MNI file (S3's RH labels on its grid HD_Grid); this placement is an\n    assumption, as the files do not document how grid contacts are numbered.\n- claim: fig4-maintenance-parietal-led\n  outcome: not_reproduced\n  notebook: reproduce_johnson_2019.ipynb\n  output: claim:fig4-maintenance-parietal-led\n  measured:\n  - 0.03\n  - -0.12\n  notes: Under reading (a) of P1 (trial-averaged coherency) subject means are -0.52 to 0.56\n    (delta-theta) and -0.45 to 0.21 (alpha-beta), none below -1.96 (group 0.03 +- 0.36 and -0.12 +-\n    0.23, recorded as measured). Under reading (b) (per-trial PSI averaged over trials) 4 of 7\n    subjects are below -1.96 in delta-theta (mean -0.31 +- 10.67) and none in alpha-beta (2.12 +-\n    2.07). The paper reports -40.03 +- 8.73 and -30.37 +- 2.60. The deposited psianalysis.m, run as\n    written (no conjugate) with the parietal channel first and the sign reversed, gives every subject\n    below -1.96 (means -55.56 and -69.73), which would meet the criterion; with the PFC channel first\n    the same code gives +58.54 and +69.33, so its sign follows the channel order and it does not\n    measure direction.\n  deviations:\n  - P1 details taken from psi_compute.m and subtracterp.m, ERP removed as the mean over all correct\n    trials (\"raw trial-wise mean\", reading (a)); one Hanning-tapered FFT of each 900-ms segment\n    padded to 7.5 s, read at the nearest bins to the integer frequencies ('mtmfft', spectra reading\n    (a)); one PSI per band over all its bins; one shuffle for all pairs; the null shuffles the bins\n    of the trial-mean normalised spectrum (psianalysis.m).\n  - P1's last reading (PSI from trial-averaged cross-spectra or per trial) is not settled by\n    psianalysis.m, which computes per-trial PSI but omits the conjugate of the cross-spectrum; both\n    readings are run with the conjugate, and the deposited code as a variant.\n  - The time-resolved null uses one set of 1000 shuffles per time point, the task-induced one a set\n    per frequency bin averaged as psianalysis.m does (a standard choice; it changes only Monte Carlo\n    noise).\n- claim: fig4a-delta-theta-shift\n  outcome: partially_reproduced\n  notebook: reproduce_johnson_2019.ipynb\n  output: claim:fig4a-delta-theta-shift\n  measured:\n  - 4\n  - -0.17\n  - 59.1\n  notes: Under reading (b), processing delta-theta PSI z exceeds maintenance (by 9.18, F(1,2268) =\n    59.1, p = 2.2e-14; paper F = 1936.10) and 4 subjects (S2, S3, S6, S7) have net z above 0 (paper\n    6), the criterion's partial match; mean of seven -0.17 +- 9.53, of the four above 0 6.26 (paper\n    6.01 +- 6.42). Under reading (a) the interval effect is absent (0.07, p = 0.272) with 2 subjects\n    above 0. The deposited code puts all 7 subjects above 0 with PFC first and none with parietal\n    first.\n  deviations:\n  - As fig4-maintenance-parietal-led. The mixed model is computed as the paired test over pairs,\n    which equals it when each pair has both intervals (checked against statsmodels MixedLM; F 61.5\n    against 59.1 under reading (b), where the pair variance is estimated at zero). Degrees of freedom\n    2268 follow from 1135 pairs.\n- claim: fig4c-alpha-beta-shift\n  outcome: not_reproduced\n  notebook: reproduce_johnson_2019.ipynb\n  output: claim:fig4c-alpha-beta-shift\n  measured:\n  - -0.03\n  - 6.2\n  notes: Processing alpha-beta PSI z exceeds maintenance under both readings ((a) 0.12, F = 6.2, p =\n    0.013; (b) 8.83, F = 115.2, p = 3.0e-26; paper F = 2302.30), but only 5 of 7 subjects stay below 0\n    in processing under either reading (criterion all 7, or 6 for a partial match), with means -0.03\n    and -1.89 (paper -12.60). The deposited code with the parietal channel first gives all 7 below 0\n    (mean -73.15).\n  deviations:\n  - As fig4a-delta-theta-shift.\n- claim: directional-pairs\n  outcome: reproduced\n  notebook: reproduce_johnson_2019.ipynb\n  output: claim:directional-pairs\n  measured:\n  - 1014\n  - 1043\n  notes: Under reading (b), 1014 of 1135 pairs have processing |z| > 1.96 in delta-theta and 1043 in\n    alpha-beta, within tolerance of 1008 and 984. Reading (a) gives 264 and 118. Under reading (b) the\n    observed per-trial PSI is z-scored against a null built from the trial-mean spectrum (as in\n    psianalysis.m); a 5% null would give about 57 pairs, and 89 to 92% pass, so the count reflects\n    this scaling as much as directionality.\n  deviations:\n  - As fig4-maintenance-parietal-led; 1135 pairs, not 1129 (table1-electrodes).\n- claim: fig5a-delta-theta-epochs\n  outcome: not_reproduced\n  notebook: reproduce_johnson_2019.ipynb\n  output: claim:fig5a-delta-theta-epochs\n  notes: Under reading (a) no time point differs between conditions after FDR (264 directional\n    pairs). Under reading (b) (1014 pairs) the sustained differences are, identity against spatial,\n    110-230 ms (identity higher), 300-400 ms (lower) and 460-600 ms (higher), and identity against\n    temporal 120-250, 290-390 and 680-840 ms with the same signs. Neither contrast has an epoch from 0\n    ms, and the late epochs have the opposite sign to the paper's.\n  deviations:\n  - Time-resolved PSI per psi_compute.m ('mtmconvol', per-condition ERP removed by subtracterp.m with\n    three conditions). subtracterp.m selects temporal trials by trialinfo column 5 (the delay), which\n    selects none; the condition column is used.\n  - The per-time-point mixed model is computed as the paired test over pairs (checked against\n    statsmodels at three time points); FDR is Benjamini-Hochberg over the 91 points; a run is\n    sustained when it spans at least 100 ms.\n- claim: fig5a-identity-direction\n  outcome: not_reproduced\n  notebook: reproduce_johnson_2019.ipynb\n  output: claim:fig5a-identity-direction\n  measured:\n  - 0.35\n  - 0.38\n  - -0.25\n  - -0.21\n  notes: Under PSI reading (a), identity-trial delta-theta z in the paper's four epochs is below 1.96\n    in absolute value under every averaging reading and under the identity-minus-other reading\n    (grand means 0.35, 0.38, -0.25, -0.21; paper > 2.62, > 2.35, < -3.04, < -3.57). Under reading (b)\n    the early values are below 1.96 (largest 1.58) and every late value is positive (up to 7.61), the\n    opposite sign to the paper's.\n  deviations:\n  - As fig5a-delta-theta-epochs; the paper's epochs are used.\n- claim: fig5a-spatiotemporal-bidirectional\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_johnson_2019.ipynb\n  output: claim:fig5a-spatiotemporal-bidirectional\n  notes: With PSI reading (b), the grand mean of spatial-trial delta-theta PSI z reaches |z| = 5.44\n    (110 ms) and temporal-trial 6.36 (630 ms), with 42 and 40 of 91 time points at |z| >= 1.96\n    (paper, all |z| < 1.60). Under reading (a) the grand means stay at or below 0.35 and 0.72, which\n    would meet the criterion.\n  deviations:\n  - Assumption. For this claim of absence one PSI reading must be chosen; reading (b) is adopted\n    because it is the structure of the deposited psianalysis.m (per-trial PSI averaged over trials)\n    and it gives the paper's counts of directional pairs (1014 and 1043 against 1008 and 984), which\n    reading (a) does not (264 and 118).\n- claim: fig5b-alpha-beta-no-sustained\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_johnson_2019.ipynb\n  output: claim:fig5b-alpha-beta-no-sustained\n  notes: With PSI reading (b), 66 (identity against spatial) and 75 (against temporal) of 91 time\n    points differ after FDR, and the longest run of one sign lasts 80 and 90 ms, so no difference is\n    sustained. Under reading (a) no point is significant after FDR (smallest p 0.0048 and 0.0016),\n    the criterion's partial match.\n  deviations:\n  - Assumption, PSI reading (b), as in fig5a-spatiotemporal-bidirectional.\nfindings:\n- kind: metadata_error\n  statement: The data set's list of analysed channels (docs/summary_channel_analysis.csv) holds 187\n    channels where the paper reports 192 (Table 1). S4 has 5 right parietal channels (RLD6 to RLD8,\n    RC10, RC11) where Table 1 gives 10. The list yields 1135 same-hemisphere PFC-parietal pairs,\n    where the paper reports 1129; Table 1's counts would give 1165.\n- kind: metadata_error\n  statement: The description says summary_file_trial.csv holds information about each trial, with\n    120 trials per subject. In S6 and S7 it holds only the trials kept after artifact rejection (101\n    and 90 rows, numbered up to 120), matching their derived epochs; in S1 to S5 it holds all 120.\n    Single-trial accuracy over all 120 trials cannot be rebuilt for S6 and S7 (summary_file.csv gives\n    it per condition).\n- kind: other\n  statement: A timing contrast between trials with 900-ms and 1150-ms delays (70-150 Hz amplitude)\n    shows, in S2, S3 and S4, responses in the processing epoch of the 1150-ms trials 0.21 to 0.26 s\n    later relative to the trial table's processing column than in the 900-ms trials, and in S4 the\n    same shift in the encoding epoch, while the pretrial epochs show shifts of 0.03 s or less. This is\n    consistent with the encoding and processing columns (computed at fixed offsets from the pretrial\n    start) lying about 0.25 s before the events in 1150-ms trials, which would put the end of the cue\n    in their processing window. The test is weak in the other subjects and does not prove it.\n- kind: code_mismatch\n  statement: The deposited psianalysis.m computes the cross-spectrum as the product of the two\n    channels' Fourier coefficients without the conjugate, unlike the cross-spectral density of the\n    Methods and of Nolte et al. (2008). The resulting normalised spectrum depends essentially on one\n    channel's phase, and the PSI z it gives is not antisymmetric; on these data it is +58.5\n    (delta-theta maintenance, mean over subjects) with the PFC channel first and -55.6 (sign\n    reversed) with the parietal channel first.\n- kind: code_mismatch\n  statement: The deposited psi_compute.m does not run as written. It uses an undefined `freq` (the\n    signature takes subid and elecs only), saves to an undefined `savDir`, and tests the electrode\n    argument with `nargin > 2`. Its subfunction subtracterp.m selects temporal trials with\n    `trialinfo(:,5)==2`, the delay column, which selects no trial.\n- kind: other\n  statement: S7's derived epochs record a continuous recording of 431506 samples (hdr.nSamples)\n    while the deposited data_primary.mat of S7 has 445952; the derived traces still match the\n    deposited continuous data at the trial table's samples (r >= 0.9989). S3's elec_labels.mat is a\n    MATLAB 5 file, the others MATLAB 7.3.\n- kind: metadata_insufficient\n  statement: The electrode position files (s<n>_MNI_grid.csv) name grids and list positions in\n    order, but do not say how the contact numbers of the channel labels map to grid positions, and\n    S3's labels (RH1 to RH256) do not match the name of its grid (HD_Grid). The derived channels are\n    bipolar, labelled by one contact, with the reference contact found here only from the data (the\n    next contact on strips and depth leads, the next grid row on S3's and S6's grids).\n- kind: methods_unavailable\n  statement: Question for the paper's authors. Which electrodes were neighbours in the per-subject\n    cluster tests (Methods, Event-Related Potentials, \"neighboring electrodes\"), and were clusters of\n    each sign judged at 0.05 or 0.025? The outcome of the ERP test depends on it here (adjacent\n    contacts, smallest p 0.053; positions within 1.5 contact spacings, S5 p = 0.028). This attempt\n    assumed contacts adjacent on the same lead and 0.05 per tail.\n- kind: methods_unavailable\n  statement: Question for the paper's authors. Was task-induced and time-resolved PSI computed from\n    cross-spectra averaged over trials (Nolte et al. 2008) or per trial and averaged, as\n    psianalysis.m does, and with which channel first, given that the deposited code omits the\n    conjugate? The readings differ in every PSI claim (directional pairs 264 and 118 against 1014 and\n    1043; the paper reports 1008 and 984). This attempt adopted the per-trial reading, with the\n    conjugate, for the claims of absence.\n"
}
```

```
File created successfully at: attempts/crcns-fcx-3-johnson-2019-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='build_notebook.py'
s=open(p).read()
old='''pretrial start (G) precedes the encoding start (H) by 1.9 s in every trial, the pretrial fixation'''
new='''pretrial start (G) precedes the encoding start (H) by 1.9 s in every trial (1.87 to 1.92 s in S7,
sampled at 512 Hz), the pretrial fixation'''
assert old in s; s=s.replace(old,new)
old='''epochs), so the derived channels are bipolar, labelled by their first contact. The reference is the
contact numbered one below on strips and depth leads, and the next row of the grid (8 below) on S6's
8 x 8 grid.'''
new='''epochs), so the derived channels are bipolar, labelled by one of their contacts. The reference is
the contact numbered one above or below on strips and depth leads, and the next row of the grid on
S3's 16 x 16 grid (16 below) and S6's 8 x 8 grid (8 below).'''
assert old in s; s=s.replace(old,new)
open(p,'w').write(s)
EOF
cd  && python - <<'EOF'
import yaml,re
t=open('attempts/crcns-fcx-3-johnson-2019-01.yaml').read()
d=yaml.safe_load(t)
# find plain scalars with ': ' inside
for i,l in enumerate(t.splitlines()):
    body=l.strip()
    if body.startswith('- '): body=body[2:]
    m=re.match(r'^[A-Za-z_]+: (.*)$',body)
    rest=m.group(1) if m else body
    if ': ' in rest: print(i+1,l)
print('ok', len(d['outcomes']))
EOF
```

```
ok 17
```

**Agent calls Write**

```json
{
 "file_path": "entries/crcns-fcx-3-johnson-2019/README.md",
 "content": "# Johnson, King-Stephens, Weber, Laxer, Lin & Knight (2019) from CRCNS fcx-3\n\nTests the findings of [Johnson et al. (2019)](https://doi.org/10.3389/fnsys.2018.00065) on CRCNS\ndata set [fcx-3](https://doi.org/10.6080/K06971S9), which holds intracranial recordings from\nprefrontal and parietal cortex of 7 patients doing a visuospatial working memory task, with the\npreprocessed epochs and the paper's MATLAB scripts.\n\n| Claim | Outcome |\n|---|---|\n| 192 analysed electrodes and 1129 pairs (Table 1) | Partially reproduced |\n| Trials kept per subject and condition | Reproduced |\n| Accuracy 0.63 to 0.98, no effect of condition | Reproduced |\n| Identity RT longer than spatial and temporal | Reproduced |\n| No ERP difference between conditions | Reproduced (assumption) |\n| Power, identity against spatial (Figure 2) | Partially reproduced |\n| Power, identity against temporal (Figure 3) | Partially reproduced |\n| Identity > effects in the subjects with lower identity accuracy | Reproduced |\n| Power effects at 2-7 and 9-24 Hz | Reproduced (assumption) |\n| Parietal-led maintenance (Figure 4) | Not reproduced |\n| Delta-theta shift with the test cue | Partially reproduced |\n| Alpha-beta shift, still parietal-led | Not reproduced |\n| 1008 and 984 directional pairs | Reproduced |\n| Time-resolved delta-theta epochs (Figure 5A) | Not reproduced |\n| Identity PFC-led early, parietal-led late | Not reproduced |\n| Spatial and temporal PSI bidirectional | Not reproduced (assumption) |\n| No sustained alpha-beta effect (Figure 5B) | Reproduced (assumption) |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe phase slope index results depend on how PSI is computed, which the paper leaves open and the\ndeposited code does not settle, as it omits the conjugate of the cross-spectrum. The data set lists\n187 analysed channels where the paper reports 192. The attempt record, with the reasons and the\ndifferences from the paper's method, is\n[`attempts/crcns-fcx-3-johnson-2019-01.yaml`](../../attempts/crcns-fcx-3-johnson-2019-01.yaml).\n\n- `reproduce_johnson_2019.ipynb`: the analysis. It takes about 20 minutes, most of it streaming\n  the 11.8 GB of tar.gz files, one subject at a time, with a peak of about 7 GB of memory.\n- `fcx3.py`: streaming the files, the clock and timing checks, the power, ERP and PSI measures and\n  the cluster test. Other notebooks on this data set can import it.\n"
}
```

```
File created successfully at: entries/crcns-fcx-3-johnson-2019/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && python $TMPDIR/build_notebook.py && deactivate; cd  && date -u && python tools/entry.py all entries/crcns-fcx-3-johnson-2019 2>&1 | tail -4; date -u
```

```
62 cells
Sun Nov  8 20:52:28 UTC 2026
Installed kernelspec registry-crcns-fcx-3-johnson-2019 in executed/crcns-fcx-3-johnson-2019/.venv/share/jupyter/kernels/registry-crcns-fcx-3-johnson-2019
0 error(s)
pass  reproduce_johnson_2019.ipynb  (1150 s)
Sun Nov  8 21:11:47 UTC 2026
```

**Agent calls Bash**

```bash
cd  source $TMPDIR/dev/bin/activate; python - <<'EOF' > $TMPDIR/exec2.txt
import nbformat
nb=nbformat.read('executed/crcns-fcx-3-johnson-2019/reproduce_johnson_2019.ipynb',4)
for c in nb.cells:
    if c.cell_type=='code':
        print('=====', c.metadata.get('tags'))
        for o in c.get('outputs',[]):
            if o.get('name')=='stdout': print(o['text'])
            elif o.output_type=='error': print('ERROR', o.ename)
EOF
deactivate
diff <(grep -v "streamed and analysed\|all subjects in" $TMPDIR/exec.txt) <(grep -v "streamed and analysed\|all subjects in" $TMPDIR/exec2.txt) && echo IDENTICAL; python tools/entry.py handover entries/crcns-fcx-3-johnson-2019 2>&1 | tail -3; python tools/entry.py check entries/crcns-fcx-3-johnson-2019 | tail -3; git status --short
```

```
201d200
< 
wrote executed/crcns-fcx-3-johnson-2019/handover
0 error(s)
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
?? attempts/crcns-fcx-3-johnson-2019-01.yaml
?? entries/crcns-fcx-3-johnson-2019/
?? scripts
```

**Agent calls Bash**

```bash
cd  ls -la scripts .idea .vscode | head; ls -la .bashrc .mcp.json; git log -1 --format=%cd; ls entries/crcns-fcx-3-johnson-2019/
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  8 19:09 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  8 19:09 .vscode
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  8 19:09 scripts
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  8 19:09 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  8 19:09 .mcp.json
Sun Nov 8 19:08:23 2026 +0000
README.md
__pycache__
entry.yaml
fcx3.py
reproduce_johnson_2019.ipynb
requirements.in
requirements.lock.txt
```

**Agent calls Bash**

```bash
cd entries/crcns-fcx-3-johnson-2019; rm -rf __pycache__; grep -n -A6 "def bipolar_positions" fcx3.py; grep -n "BLOCK\|def jitter_check" fcx3.py | head -3; date -u
```

```
337:def bipolar_positions(labels, grid, references=None):
338-    """Midpoint of a bipolar channel's two contacts (the channel's contact and the one numbered
339-    before it, as the clock check finds), taking contact n as the n-th electrode of the grid with the
340-    label's prefix in the MNI file."""
341-    pos = np.full((len(labels), 3), np.nan)
342-    spacing = np.full(len(labels), np.nan)
343-
63:BLOCK = 2**24
78:    with fsspec.open(f"{BUCKET}/{path}", block_size=BLOCK) as f:
167:    with fsspec.open(f"{BUCKET}/data/{sid}.tar.gz", block_size=BLOCK) as f:
Sun Nov  8 21:12:20 UTC 2026
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('fcx3.py').read()
old='''    """Midpoint of a bipolar channel's two contacts (the channel's contact and the one numbered
    before it, as the clock check finds), taking contact n as the n-th electrode of the grid with the
    label's prefix in the MNI file."""'''
new='''    """Midpoint of a bipolar channel's two contacts (the channel's contact and the reference contact
    the clock check finds in the continuous data), taking contact n as the n-th electrode of the grid
    with the label's prefix in the MNI file (an assumption: the files do not say how grid contacts are
    numbered)."""'''
assert old in s; s=s.replace(old,new); open('fcx3.py','w').write(s)
EOF
cd  && python tools/entry.py check entries/crcns-fcx-3-johnson-2019 | tail -1 && python tools/entry.py handover entries/crcns-fcx-3-johnson-2019 | tail -1 && ls executed/crcns-fcx-3-johnson-2019/handover/
```

```
0 error(s)
wrote executed/crcns-fcx-3-johnson-2019/handover
10.3389-fnsys.2018.00065.yaml
fcx3.py
reproduce_johnson_2019.ipynb
```

**Agent calls Bash**

```bash
cd  grep -c '\*\*Result' executed/crcns-fcx-3-johnson-2019/handover/reproduce_johnson_2019.ipynb; grep -c '## Summary' executed/crcns-fcx-3-johnson-2019/handover/reproduce_johnson_2019.ipynb; date -u
```

```
0
0
Sun Nov  8 21:12:47 UTC 2026
```

**Agent**

I did steps 1 to 5 of the Author section and built the handover. The entry `entries/crcns-fcx-3-johnson-2019/` passes `entry.py all` (0 errors; the notebook runs in 19 min, about 7 GB peak memory), and two full runs gave identical outputs. The record is `attempts/crcns-fcx-3-johnson-2019-01.yaml`. Nothing is committed.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| table1-electrodes | partially reproduced (187 channels, 1135 pairs) |
| trial-counts | reproduced |
| fig1b-accuracy | reproduced |
| fig1b-rt-identity-slower | reproduced |
| erp-no-condition-difference | reproduced, rests on an assumption |
| fig2-spatial-power | partially reproduced (counts 5 and 2 match; percentages low) |
| fig3-temporal-power | partially reproduced |
| power-difficulty-subjects | reproduced |
| power-low-frequencies | reproduced, rests on an assumption |
| fig4-maintenance-parietal-led | not reproduced |
| fig4a-delta-theta-shift | partially reproduced |
| fig4c-alpha-beta-shift | not reproduced |
| directional-pairs | reproduced (1014 and 1043 against 1008 and 984) |
| fig5a-delta-theta-epochs | not reproduced |
| fig5a-identity-direction | not reproduced |
| fig5a-spatiotemporal-bidirectional | not reproduced, rests on an assumption |
| fig5b-alpha-beta-no-sustained | reproduced, rests on an assumption |

**2. Dataset, assumptions and questions**

What the dataset shows:
- **Version.** It is pinned as `unversioned` with the DOI; the notebook header prints the MD5 sums. Only `live/` exists in the bucket.
- **Epochs and clock.** The derived epochs are bipolar differences of the continuous data (r ≥ 0.9998). They sit at fixed offsets from the trial table, which puts the deposited scripts' windows where the Methods put them.
- **Channels.** The channel list has 187 analysed channels, not 192: S4 has 5 parietal channels where Table 1 has 10. The list gives 1135 pairs, not 1129.
- **Trial tables.** In S6 and S7 they hold only the kept trials (101 and 90 rows), not all 120.
- **Timing.** In S2, S3 and S4, responses in the 1150-ms-delay trials come about 0.25 s later relative to the processing column than in the 900-ms trials. This is consistent with those columns being early, but the test does not prove it.
- **Deposited code.**
  - `psianalysis.m` omits the conjugate of the cross-spectrum, so its sign follows the channel order.
  - `psi_compute.m` does not run as written.
  - `subtracterp.m` selects temporal trials by the delay column, which selects none.

Assumptions:
- **Cluster neighbours** (ERP claim): adopted contacts adjacent on the same lead, judged at 0.05 per tail.
- **Electrode positions** (power-low-frequencies): matches only under the distance reading of neighbours, which assumes how numbered contacts sit on the grids.
- **PSI computed per trial** (the code's structure), adopted for the two claims of absence. It is the only reading that gives the paper's directional-pair counts.

Two questions for the paper's authors are recorded as `methods_unavailable` findings: which electrodes were neighbours and the per-tail alpha, and how PSI was computed.

I asked no reader any question.

**3. Where the protocol was unclear**
1. **Analysis code inside the dataset.** The scripts are among the dataset's files, so the reader never read them, and it is unclear whether they count as an outside input. I took details from them, cited by file name, and did not list them under `inputs`.
2. **Code that disagrees with the Methods and cannot run as written.** The order "Methods, then code" does not say what to do when the code is also buggy. I ran the Methods' readings with the conjugate fixed, and the deposited code as a variant.
3. **Claims of absence with several readings.** Absence is judged "on the paper's test alone", but the paper's test is itself underspecified. I applied step 1.6: adopted one reading as an assumption and showed the others.
4. **Clock check.** CRCNS data come pre-epoched in tar.gz files, which the decoding suggestion does not fit. I matched the derived epochs to the continuous data and added a delay-jitter contrast on high-frequency amplitude.
5. **Streaming.** tar.gz files cannot be opened in place the way docs/archives.md describes for zip. I streamed each file sequentially, with decompression in memory.

**4. Runtime and failures**

The run took about 2 h 5 min (19:11 to 21:13 UTC); the notebook takes 19 min per run. My first loader failed on S4's unequal trial lengths and on S3's labels file, which is in MATLAB 5 format; both are fixed. A first timing check based on low-frequency signals did not work and was replaced. Nothing is blocked.

## End of run

80 turns, 118 minutes, $8.63 at API prices, result: success.
