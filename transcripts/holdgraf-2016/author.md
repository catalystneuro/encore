# crcns-ac-4 · author · run 42582043075

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls paper claims/crcns-ac-4
```

```
<persisted-output>
Output too large (36.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/52702bf5-4f99-417b-984a-d20e8f06f7e6/tool-results/bi4k6uiui.txt

Preview (first 2KB):
Mon Nov  9 07:57:16 UTC 2026
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

**Agent calls Bash**

```bash
ls paper claims/crcns-ac-4 entries/001453-fouke-2025 claims/001453; cat claims/crcns-ac-4/*
```

```
<persisted-output>
Output too large (43.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/52702bf5-4f99-417b-984a-d20e8f06f7e6/tool-results/bexbmsght.txt

Preview (first 2KB):
claims/001453:
10.1016-j.cub.2025.04.027.yaml

claims/crcns-ac-4:
10.1038-ncomms13654.yaml

entries/001453-fouke-2025:
README.md
entry.yaml
omr.py
reproduce_fouke_2025.ipynb
requirements.in
requirements.lock.txt

paper:
10.1038-ncomms13654.pdf
[... 26 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/crcns-ac-4/10.1038-ncomms13654.yaml"
}
```

```
1	# Claims for Holdgraf, de Heer, Pasley, Rieger, Crone, Lin, Knight & Theunissen (2016), "Rapid
2	# tuning shifts in human auditory cortex enhance speech intelligibility", Nat Commun 7:13654, on
3	# CRCNS data set ac-4.
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-09,
5	# protocol as stated in docs/protocol.md (Reader).
6	#
7	# Text read: the version of record, as supplied under paper/ (PyMuPDF text of the journal PDF:
8	# Results, Discussion, Methods and the legends of Figures 1 to 10), with its Supplementary
9	# Information (Supplementary Figures 1 to 7 with legends, and Supplementary Methods). The
10	# Supplementary Audio and Movies were not supplied; no claim rests on them. Figure 4 was read from
11	# the PDF page, as the text loses which P-value belongs to which panel (panel a, raw coherence,
12	# P = 0.924, 0.000 and 0.001 for -1 to 0 s, 0 to 1 s and 1 to 3 s; panel b, after subtracting the
13	# mean response, P = 0.920, 0.241 and 0.006). The extracted text prints "=" as "1⁄4" and the
14	# minus sign as a replacement character; the behavioural t-test reads "P 1⁄4 1e �5", that is
15	# P = 1e-5, which the quote checker cannot find and was confirmed by reading. The data descriptor (paper/ac-4.data-description.txt)
16	# was read only to know what the data set holds.
17	#
18	# Code read: the paper links github.com/choldgraf/ecogtools ("Code for model fitting, feature
19	# extraction, statistics, and visualization"). Read at commit 7d1030e (2016-11-03), the last
20	# before publication; the modules strf.py, audio.py, connectivity.py and mpspack.py were removed
[... 683 more lines not kept]
```

**Agent calls Bash**

```bash
cat paper/ac-4.data-description.txt; grep -n -A60 "^## CRCNS" docs/archives.md
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=ac-4/" -o l1.xml; python -c "
import re
t=open('l1.xml').read()
for k,s in re.findall(r'<Key>(.*?)</Key>.*?<Size>(\d+)</Size>',t): print(s,k)
print(re.findall(r'<IsTruncated>(.*?)<',t))
"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; B=https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-4/live; curl -s $B/checksums.md5; curl -s $B/filelist.txt; python -c "
import fsspec,zipfile
f=fsspec.open('$B/data.zip',block_size=2**20).open()
z=zipfile.ZipFile(f)
for i in z.infolist(): print(i.file_size,i.compress_size,i.filename)
"
```

```
Exit code 1
a3f4fc4396018c4336289aeae07f3a24  data.zip
e5fada4a35959c02599388fa667f9629  docs/crcns_ac-4_data_description.docx
5967170cec24533198d9a116e0ac34bf  docs/crcns_ac-4_data_description.pdf
03c6756f455486e0cc0169a76f48df3e  filelist.txt
# CRCNS.org 'ac-4' dataset files
# To use this for fetching files, comment out files that are
# not needed by putting a '#' as the first character on the line (default mode)
# or put a '+' as the first character to specifiy files to be fetched (+ mode).
# mode='default' (change to '+' for + mode).
 data.zip	1640174084 (1.5 GB)
 docs/crcns_ac-4_data_description.docx	24886 (24.3 KB)
 docs/crcns_ac-4_data_description.pdf	68377 (66.7 KB)
 checksums.md5	233
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import fsspec,zipfile
ModuleNotFoundError: No module named 'fsspec'
```

**Agent calls Bash**

```bash
cd $TMPDIR; uv venv -q dev && . dev/bin/activate && uv pip install -q fsspec aiohttp requests numpy scipy pandas mne matplotlib statsmodels nbformat ipykernel 2>&1 | tail -2; B=https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-4/live; python -c "
import fsspec,zipfile
f=fsspec.open('$B/data.zip',block_size=2**20).open()
z=zipfile.ZipFile(f)
for i in z.infolist(): print(i.file_size,i.compress_size,i.filename)
"
```

```
0 0 data/
0 0 data/sub-S13/
0 0 data/sub-S13/ieeg/
55601 52813 data/sub-S13/ieeg/sub-S13_space-2DImage_photo.jpg
11013 2515 data/sub-S13/ieeg/sub-S13_task-FilteredSpeech_events.tsv
0 0 data/sub-S13/ieeg/.ipynb_checkpoints/
55601 52813 data/sub-S13/ieeg/.ipynb_checkpoints/sub-S13_space-2DImage_photo-checkpoint.jpg
2837 987 data/sub-S13/ieeg/sub-S13_task-FilteredSpeech_electrodes.tsv
507 343 data/sub-S13/ieeg/sub-S13_task-FilteredSpeech_ieeg.vmrk
4992 499 data/sub-S13/ieeg/sub-S13_task-FilteredSpeech_channels.tsv
594 277 data/sub-S13/ieeg/sub-S13_task-FilteredSpeech_events.json
444 223 data/sub-S13/ieeg/sub-S13_ieeg.json
251395072 234110830 data/sub-S13/ieeg/sub-S13_task-FilteredSpeech_ieeg.eeg
131 100 data/sub-S13/ieeg/sub-S13_space-2DImage_coordsystem.json
1582 737 data/sub-S13/ieeg/sub-S13_task-FilteredSpeech_ieeg.vhdr
3446 1637 data/README
0 0 data/sub-S07/
0 0 data/sub-S07/ieeg/
1585 721 data/sub-S07/ieeg/sub-S07_task-FilteredSpeech_ieeg.vhdr
2086 611 data/sub-S07/ieeg/sub-S07_task-FilteredSpeech_electrodes.tsv
[... 113 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . dev/bin/activate; B=https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-4/live; python -c "
import fsspec,zipfile
f=fsspec.open('$B/data.zip',block_size=2**20).open()
z=zipfile.ZipFile(f)
for n in ['data/README','data/participants.tsv','data/participants.json','data/dataset_description.json','data/code/README.md','data/code/requirements.txt','data/sub-S01/ieeg/sub-S01_ieeg.json','data/sub-S01/ieeg/sub-S01_task-FilteredSpeech_events.json','data/sub-S01/ieeg/sub-S01_task-FilteredSpeech_ieeg.vhdr','data/sub-S01/ieeg/sub-S01_task-FilteredSpeech_ieeg.vmrk','data/sub-S01/ieeg/sub-S01_space-2DImage_coordsystem.json']:
  print('=====',n); print(z.read(n).decode())
for n in ['events','channels','electrodes']:
  t=z.read('data/sub-S01/ieeg/sub-S01_task-FilteredSpeech_%s.tsv'%n).decode().splitlines(); print('=====',n,len(t)); print('\n'.join(t[:25]))
"
```

```
===== data/README
Information
===========

This folder contains the data for the publication Holdgraf et al, "Rapid tuning shifts in human auditory cortex enhance speech intelligibility".
It contains the raw data files for 7 subjects performing a passive listening "degraded speech popout" task.

Contact: Chris Holdgraf ([removed: an e-mail address])

If you use this data as a part of any publications, please use the following citation:

Holdgraf, Christopher R., Wendy de Heer, Brian Pasley, Jochem Rieger, Nathan Crone, Jack J. Lin, Robert T. Knight,
and Frédéric E. Theunissen. “Rapid Tuning Shifts in Human Auditory Cortex Enhance Speech Intelligibility.”
Nature Communications 7, no. 1 (December 2016). https://doi.org/10.1038/ncomms13654.

and also cite the dataset using:

Holdgraf, C.R.H., de Heer, W., Pasley, B., Rieger, J., Crone, N., Lin, J.J., Knight, R.T., Theunissen, F.E. (2019).
Electrocorticography recordings from patients during a passive listening task of degraded and intact English speech.
CRCNS.org.  http://dx.doi.org/10.6080/K08S4N4J
[... 274 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . dev/bin/activate; B=https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-4/live; python -c "
import fsspec,zipfile,io,pandas as pd,struct
f=fsspec.open('$B/data.zip',block_size=2**20).open()
z=zipfile.ZipFile(f)
tot=0;good=0
for s in ['S01','S02','S03','S04','S07','S08','S13']:
  p='data/sub-%s/ieeg/sub-%s_'%(s,s)
  ev=pd.read_csv(io.BytesIO(z.read(p+'task-FilteredSpeech_events.tsv')),sep='\t')
  ch=pd.read_csv(io.BytesIO(z.read(p+'task-FilteredSpeech_channels.tsv')),sep='\t')
  import json; js=json.loads(z.read(p+'ieeg.json'))
  print('=====',s,js['SamplingFrequency'],js['RecordingDuration'],len(ch),ch.status.value_counts().to_dict(), ch.type.unique(), ch.units.unique(), ch.low_cutoff.unique(), ch.high_cutoff.unique(), ch.sampling_frequency.unique(), ch.reference.unique())
  tot+=len(ch); good+=(ch.status=='good').sum()
  print(ch.description.value_counts().to_dict())
  print(ev.groupby(['trial_type','trial_phase','filt_type','noise_stim'],dropna=False).size().to_dict())
  t=ev[ev.trial_type=='trial']; print('trialnums',t.trial_num.nunique(), t.trial_num.min(), t.trial_num.max(), 'dur',t.duration.min(),t.duration.max(), t.stim_file.unique(), 'onset range',t.onset.min(),t.onset.max())
  w=z.open('data/stimuli/%s_audio.wav'%s).read(64); print('wav hdr',w[:4],struct.unpack('<HHIIHH',w[20:36]))
print(tot,good)
"
```

```
===== S01 1000.0 1204.041 64 {'good': 61, 'bad': 3} <StringArray>
['ECOG']
Length: 1, dtype: str <StringArray>
['milliV']
Length: 1, dtype: str [0.01] [nan] [1000.] <StringArray>
['CAR']
Length: 1, dtype: str
{'temporal-superior': 9, 'premotor-medial': 7, 'motor-medial': 7, 'temporal-medial': 7, 'parietal-superior': 6, 'parietal-medial': 6, 'premotor-superior': 4, 'motor-superior': 4, 'parietal-inferior': 3, 'motor-inferior': 3, 'temporal-posterior': 3, 'frontal-superior': 2, 'frontal-inferior': 2, 'frontal-medial': 1}
{('bad', nan, nan, 'none'): 9, ('trial', 'aft', 'freq', 'none'): 28, ('trial', 'aft', 'temp', 'none'): 28, ('trial', 'bef', 'freq', 'none'): 28, ('trial', 'bef', 'temp', 'none'): 28, ('trial', 'mid', 'norm', 'none'): 62}
trialnums 57 -1.0 56.0 dur 1.5199999999999818 3.391999999999939 <StringArray>
['S01_audio.wav']
Length: 1, dtype: str onset range 49.033 1165.233
wav hdr b'RIFF' (3, 1, 16000, 128000, 8, 64)
===== S02 1000.0 815.0 64 {'good': 59, 'bad': 5} <StringArray>
['ECOG']
Length: 1, dtype: str <StringArray>
['milliV']
Length: 1, dtype: str [0.01] [nan] [1000.] <StringArray>
['CAR']
Length: 1, dtype: str
[... 73 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l paper/*.txt; grep -n -i "data availab\|github\|behavio" paper/10.1038-ncomms13654.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-ncomms13654.txt",
 "offset": 1100,
 "limit": 490
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-ncomms13654.txt",
 "offset": 225,
 "limit": 180
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "Figure [3-7] |" paper/10.1038-ncomms13654.txt; sed -n 470,560p paper/10.1038-ncomms13654.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
date -u; cat entries/001453-fouke-2025/entry.yaml entries/001453-fouke-2025/requirements.in entries/001453-fouke-2025/README.md; head -c 5000 attempts/001453-fouke-2025-01.yaml; grep -n "^  [a-z_]*:\|^[a-z_]*:" attempts/001453-fouke-2025-01.yaml | sort -u -k2 | head -60
```

```
Mon Nov  9 07:58:31 UTC 2026
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
[... 195 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 195,330p attempts/001453-fouke-2025-01.yaml; ls tools; python tools/entry.py --help 2>&1 | head -20; ls schemas 2>/dev/null
```

```
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
  outcome: blocked
[... 168 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . dev/bin/activate; python -c "
import fsspec,zipfile,numpy as np,time,resource
B='https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-4/live'
t=time.time()
f=fsspec.open(B+'/data.zip',block_size=2**24).open()
z=zipfile.ZipFile(f)
b=z.read('data/sub-S04/ieeg/sub-S04_task-FilteredSpeech_ieeg.eeg')
x=np.frombuffer(b,dtype='<f4').reshape(-1,48).T
print(time.time()-t, x.shape, x.dtype)
print(np.percentile(x,[0,1,50,99,100],axis=1)[:,:6])
print('car check: mean over chans std', x.mean(0).std(), 'chan std', x.std(1)[:6])
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
"
```

```
4.537627696990967 (48, 660212) float32
[[-4.52050371e+10 -3.27272673e+10 -1.22899622e+09 -1.60991334e+10
  -1.83375642e+09 -1.68628224e+09]
 [-3.88242624e+09 -1.46139531e+09 -5.31125024e+08 -6.64179196e+09
  -7.81625263e+08 -8.29263132e+08]
 [-3.91428662e+06 -2.63847538e+06 -4.65641660e+04  1.06624484e+08
   2.49972188e+06  2.09815138e+06]
 [ 4.06173107e+09  1.63653613e+09  5.39373727e+08  5.80278412e+09
   7.71069058e+08  8.18557340e+08]
 [ 4.28558090e+10  3.22044723e+10  1.20094042e+09  1.38356388e+10
   1.68857306e+09  1.53737446e+09]]
car check: mean over chans std 1.1769977e+08 chan std [1.5090661e+09 7.7956365e+08 2.2313707e+08 2.4567552e+09 3.2239690e+08
 3.4800602e+08]
0.548852
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; . dev/bin/activate; python -c "
import fsspec,zipfile,json
B='https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-4/live'
z=zipfile.ZipFile(fsspec.open(B+'/data.zip',block_size=2**22).open())
for n in ['data/code/explore_data.ipynb','data/code/results/results_S04.ipynb','data/code/run_pm.ipynb']:
  nb=json.loads(z.read(n))
  print('#########',n)
  for c in nb['cells']:
    if c['cell_type']=='code': print('--- code'); print(''.join(c['source']))
    else: print('--- md'); print(''.join(c['source'])[:600])
    for o in c.get('outputs',[]):
      if 'text' in o: print('>>',''.join(o['text'])[:500])
"
```

```
######### data/code/explore_data.ipynb
--- code
# These are the required packages to load this tutorial
import mne
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
import pybv as bv
from bids import BIDSLayout
import json
import librosa as lr

%matplotlib inline
--- code
# Parameters we'll use in the notebook
subject = "S01"
--- md
# Explore and load what's in the bids dataset
--- code
[... 421 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 2120,2309p paper/10.1038-ncomms13654.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
date -u; sed -n 1,60p tools/entry.py | head -80; grep -n "tag\|sanity\|claim:" tools/entry.py | head -40
```

```
Mon Nov  9 08:00:39 UTC 2026
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
[... 48 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/crcns-ac-4-holdgraf-2016/ac4.py",
 "content": "\"\"\"Loading and measures for CRCNS ac-4 (Holdgraf et al. 2016, Nat Commun 7:13654).\n\nThe data set is a single zip, ``ac-4/live/data.zip`` in the public S3 bucket ``crcnsarchive``.\nIt is read in place over HTTP range requests (fsspec + zipfile); nothing is written to disk.\nCRCNS data sets are unversioned; the MD5 of data.zip from the data set's checksums.md5 is\n``DATA_ZIP_MD5`` and is checked against the archive's listing in the notebook.\n\nWhere each parameter comes from is said where it is defined:\n- \"claims\" : the claim's criterion in claims/crcns-ac-4/10.1038-ncomms13654.yaml\n- \"Methods, <section>\" : the paper's passage (author, step 1.6)\n- \"assumption\" : a choice the paper leaves open that could change a result (stated in the record)\n- \"standard\" : a choice that cannot change a result, or the claims file's named standard choice\n\"\"\"\n\nfrom __future__ import annotations\n\nimport io\nimport json\n\nimport fsspec\nimport numpy as np\nimport pandas as pd\nimport scipy.signal as ss\nfrom scipy.fft import next_fast_len\n\nDATASET = \"crcns:ac-4/unversioned\"\nDOI = \"10.6080/K08S4N4J\"\nBASE = \"https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-4/live\"\nZIP_URL = f\"{BASE}/data.zip\"\nDATA_ZIP_MD5 = \"a3f4fc4396018c4336289aeae07f3a24\"\nSUBJECTS = [\"S01\", \"S02\", \"S03\", \"S04\", \"S07\", \"S08\", \"S13\"]\n\nFS = 1000.0          # ECoG sampling rate (ieeg.json; checked in the notebook)\nFS_OUT = 50.0        # Methods, Neural and auditory feature extraction: \"down-sampled to 50 Hz\"\nBASELINE = (-0.8, -0.1)   # Methods, Evoked HFB: \"times -800 to -100 ms relative to sound onset\"\nEPOCH = (-1.0, 3.5)       # window kept around each sound, s (standard: covers every window used)\n\n# HFB: Methods, Neural and auditory feature extraction: 21 centre frequencies 70 to 140 Hz,\n# zero-phase IIR band-pass, Hilbert modulus, averaged. Band edges are open (claims, open detail\n# 4); standard choice: log-spaced centres, band width 10% of the centre, 2nd-order Butterworth\n# applied forwards and backwards (its squared magnitude, applied in the frequency domain).\nHFB_CENTRES = np.geomspace(70, 140, 21)\nHFB_REL_WIDTH = 0.10\n# Methods, Participants: band-pass 0.5 to 200 Hz, notch 60, 120, 180 Hz, zero-phase IIR,\n# common average reference. Filter orders are a standard choice (4th-order Butterworth,\n# notch stop band +/- 1 Hz).\nPRE_BAND = (0.5, 200.0)\nNOTCHES = (60.0, 120.0, 180.0)\n\n# Auditory spectrogram: Methods, Neural and auditory feature extraction: 128 ERB-spaced\n# gammatone bands 180 to 7000 Hz, half-wave rectification, compression, spectral sharpening,\n# 8 ms leaky integrator, reduced to 32 bands, 50 Hz. Compression exponent (cube root) and the\n# sharpening (rectified difference with the next lower band, as in the NSL model the Methods\n# cite, ref. 3) are standard choices.\nN_BANDS_FULL = 128\nN_BANDS = 32\nF_LO, F_HI = 180.0, 7000.0\nTAU_LEAK = 0.008\nMAX_LAG = 20         # Methods, eSTRF model formulation: lags 0 to 400 ms at 50 Hz -> 0..20\n\n\ndef open_zip():\n    import zipfile\n    f = fsspec.open(ZIP_URL, block_size=2**24).open()\n    return zipfile.ZipFile(f)\n\n\ndef _p(subject, suffix):\n    return f\"data/sub-{subject}/ieeg/sub-{subject}_{suffix}\"\n\n\ndef read_tables(z, subject):\n    \"\"\"Events, channels and electrodes tables and the sidecar json of one subject.\"\"\"\n    ev = pd.read_csv(io.BytesIO(z.read(_p(subject, \"task-FilteredSpeech_events.tsv\"))), sep=\"\\t\")\n    ch = pd.read_csv(io.BytesIO(z.read(_p(subject, \"task-FilteredSpeech_channels.tsv\"))), sep=\"\\t\")\n    el = pd.read_csv(io.BytesIO(z.read(_p(subject, \"task-FilteredSpeech_electrodes.tsv\"))), sep=\"\\t\")\n    js = json.loads(z.read(_p(subject, \"ieeg.json\")))\n    hdr = z.read(_p(subject, \"task-FilteredSpeech_ieeg.vhdr\")).decode()\n    return ev, ch, el, js, hdr\n\n\ndef header_channels(hdr):\n    names = []\n    for line in hdr.splitlines():\n        if line.startswith(\"Ch\") and \"=\" in line and line.split(\"=\")[0][2:].isdigit():\n            names.append(line.split(\"=\")[1].split(\",\")[0])\n    return names\n\n\ndef read_eeg(z, subject, n_channels):\n    \"\"\"The raw float32 multiplexed BrainVision data, as (channels, samples).\"\"\"\n    b = z.read(_p(subject, \"task-FilteredSpeech_ieeg.eeg\"))\n    x = np.frombuffer(b, dtype=\"<f4\").reshape(-1, n_channels).T\n    return x\n\n\ndef trials(ev):\n    \"\"\"The sound events of the task, with their phase, triplet number, filter and pink noise flag.\n\n    noise_stim == 'mid' marks triplets whose MIDDLE sound was pink noise (events.json:\n    \"Whether the middle sound was noise ... or unfiltered speech\"). Sounds with trial_num -1\n    are unfiltered sentences outside any triplet; they are kept apart.\n    \"\"\"\n    t = ev[ev.trial_type == \"trial\"].copy()\n    t[\"trial_num\"] = t.trial_num.astype(float).astype(int)\n    t[\"noise\"] = t.noise_stim == \"mid\"\n    t = t.sort_values(\"onset\").reset_index(drop=True)\n    bad = ev[ev.trial_type == \"bad\"][[\"onset\", \"duration\"]].to_numpy(float)\n    ov = np.zeros(len(t), bool)\n    for o, d in bad:\n        ov |= (t.onset + EPOCH[0] < o + d) & (t.onset + t.duration + 0.5 > o)\n    t[\"overlaps_bad\"] = ov\n    return t\n\n\n# ---------------------------------------------------------------- filters in the frequency domain\n\ndef _butter_gain(freqs, order, band, btype):\n    sos = ss.butter(order, band, btype=btype, fs=FS, output=\"sos\")\n    _, h = ss.sosfreqz(sos, worN=freqs, fs=FS)\n    return np.abs(h) ** 2          # forward-backward (zero-phase) application\n\n\ndef preprocess_hfb(x, chunk=8):\n    \"\"\"CAR, pre-filter, then HFB amplitude at 1 kHz averaged over the 21 bands, down to 50 Hz.\n\n    Returns (hfb50, raw) with raw the pre-filtered, re-referenced signal at 1 kHz (float32).\n    \"\"\"\n    x = np.asarray(x, dtype=np.float64)\n    x = x - x.mean(0, keepdims=True)                        # common average reference\n    n = x.shape[1]\n    nf = next_fast_len(n)\n    freqs = np.fft.rfftfreq(nf, 1 / FS)\n    g = _butter_gain(freqs, 4, PRE_BAND, \"bandpass\")\n    for f0 in NOTCHES:\n        g = g * _butter_gain(freqs, 2, (f0 - 1, f0 + 1), \"bandstop\")\n    gains = [_butter_gain(freqs, 2, (c * (1 - HFB_REL_WIDTH / 2), c * (1 + HFB_REL_WIDTH / 2)),\n                          \"bandpass\") for c in HFB_CENTRES]\n    raw = np.empty(x.shape, np.float32)\n    hfb = []\n    for i in range(0, x.shape[0], chunk):\n        X = np.fft.rfft(x[i:i + chunk], n=nf) * g\n        raw[i:i + chunk] = np.fft.irfft(X, n=nf)[:, :n]\n        env = np.zeros((X.shape[0], n))\n        for gb in gains:\n            Z = np.zeros((X.shape[0], nf), complex)\n            Z[:, :len(freqs)] = X * gb\n            Z[:, 1:(nf + 1) // 2] *= 2                    # analytic signal\n            env += np.abs(np.fft.ifft(Z, axis=1)[:, :n])\n        env /= len(gains)\n        hfb.append(ss.resample_poly(env, 1, int(FS / FS_OUT), axis=1))\n    return np.concatenate(hfb).astype(np.float32), raw\n\n\ndef hfb_amplitude(x, centres, fs=FS):\n    \"\"\"Mean Hilbert amplitude over bands (for PAC: 10 log-spaced bands, Supplementary Methods).\"\"\"\n    n = x.shape[-1]\n    nf = next_fast_len(n)\n    freqs = np.fft.rfftfreq(nf, 1 / fs)\n    X = np.fft.rfft(x, n=nf, axis=-1)\n    env = 0\n    for c in centres:\n        gb = _butter_gain(freqs, 2, (c * (1 - HFB_REL_WIDTH / 2), c * (1 + HFB_REL_WIDTH / 2)), \"bandpass\")\n        Z = np.zeros(X.shape[:-1] + (nf,), complex)\n        Z[..., :len(freqs)] = X * gb\n        Z[..., 1:(nf + 1) // 2] *= 2\n        env = env + np.abs(np.fft.ifft(Z, axis=-1)[..., :n])\n    return env / len(centres)\n\n\ndef band_phase(x, lo, hi, fs=FS):\n    \"\"\"Hilbert phase of a zero-phase band-passed signal (2nd-order Butterworth, standard).\"\"\"\n    sos = ss.butter(2, (lo, hi), btype=\"bandpass\", fs=fs, output=\"sos\")\n    return np.angle(ss.hilbert(ss.sosfiltfilt(sos, x, axis=-1), axis=-1))\n\n\n# ---------------------------------------------------------------- audio\n\ndef read_audio(z, subject):\n    \"\"\"The subject's stimulus track (float64 WAV, mono), on the recording's clock.\"\"\"\n    from scipy.io import wavfile\n    b = z.read(f\"data/stimuli/{subject}_audio.wav\")\n    sr, a = wavfile.read(io.BytesIO(b))\n    return sr, np.asarray(a, dtype=np.float64)\n\n\ndef erb_space(lo, hi, n):\n    e = lambda f: 21.4 * np.log10(1 + 0.00437 * f)\n    ie = lambda v: (10 ** (v / 21.4) - 1) / 0.00437\n    return ie(np.linspace(e(lo), e(hi), n))\n\n\ndef auditory_spectrogram(seg, sr):\n    \"\"\"Auditory spectrogram of one audio segment, (32 bands, samples at 50 Hz).\"\"\"\n    cfs = erb_space(F_LO, F_HI, N_BANDS_FULL)\n    n = len(seg)\n    nf = next_fast_len(n + int(0.05 * sr))\n    S = np.fft.rfft(seg, n=nf)\n    freqs = np.fft.rfftfreq(nf, 1 / sr)\n    out = np.empty((N_BANDS_FULL, n))\n    for k, cf in enumerate(cfs):\n        b, a = ss.gammatone(cf, \"iir\", fs=sr)\n        _, h = ss.freqz(b, a, worN=freqs, fs=sr)\n        out[k] = np.fft.irfft(S * h, n=nf)[:n]\n    out = np.maximum(out, 0) ** (1 / 3)                    # half-wave rectify, compress\n    out = np.vstack([out[:1], np.maximum(np.diff(out, axis=0), 0)])   # spectral sharpening\n    alpha = np.exp(-1 / (TAU_LEAK * sr))\n    out = ss.lfilter([1 - alpha], [1, -alpha], out, axis=1)          # leaky integrator\n    out = out.reshape(N_BANDS, N_BANDS_FULL // N_BANDS, n).mean(1)\n    step = sr / FS_OUT\n    m = int(n // step)\n    idx = (np.arange(m)[:, None] * step + np.arange(int(step))[None]).astype(int)\n    return out[:, idx].mean(-1)                           # boxcar average to 50 Hz\n\n\ndef speech_envelope(seg, sr, fs_out=FS):\n    \"\"\"Supplementary Methods, Electrode coherence with speech envelope: 64 log-spaced Gabor\n    wavelets 500 to 2000 Hz, rectified, averaged. Wavelet width 7 cycles (standard).\"\"\"\n    n = len(seg)\n    nf = next_fast_len(n)\n    S = np.fft.rfft(seg, n=nf)\n    freqs = np.fft.rfftfreq(nf, 1 / sr)\n    env = np.zeros(n)\n    for f0 in np.geomspace(500, 2000, 64):\n        sd = f0 / 7\n        g = np.exp(-0.5 * ((freqs - f0) / sd) ** 2)\n        Z = np.zeros(nf, complex)\n        Z[:len(freqs)] = S * g * 2\n        env += np.abs(np.fft.ifft(Z)[:n])\n    env /= 64\n    return ss.resample_poly(env, int(fs_out), int(sr))\n\n\n# ---------------------------------------------------------------- per subject loading\n\ndef load_subject(z, subject, keep_raw=True):\n    \"\"\"Everything later analyses need from one subject, reduced as it loads.\"\"\"\n    ev, ch, el, js, hdr = read_tables(z, subject)\n    names = header_channels(hdr)\n    x = read_eeg(z, subject, len(names))\n    good = ch.status.eq(\"good\").to_numpy()\n    assert list(ch.name) == names\n    xg = x[good]\n    stats = dict(n_samples=x.shape[1], raw_abs_median=float(np.median(np.abs(xg))),\n                 car_residual=float(np.abs(xg.mean(0)).mean() / np.abs(xg).mean()))\n    del x\n    hfb, raw = preprocess_hfb(xg)\n    del xg\n    tr = trials(ev)\n    sr, audio = read_audio(z, subject)\n    # spectrogram and speech envelope per sound, from 0.5 s before onset to 0.5 s after offset\n    spec, envs = [], []\n    for _, r in tr.iterrows():\n        a0 = int(round((r.onset - 0.5) * sr))\n        a1 = int(round((r.onset + r.duration + 0.5) * sr))\n        seg = audio[max(a0, 0):a1]\n        spec.append(auditory_spectrogram(seg, sr))\n        envs.append(speech_envelope(audio[int(round(r.onset * sr)):int(round((r.onset + 3) * sr))], sr))\n    # audio clock check: rectified audio around onsets\n    win = np.arange(int(-0.5 * sr), int(1.0 * sr))\n    on = np.round(tr.onset.to_numpy() * sr).astype(int)\n    aud = np.abs(audio[on[:, None] + win[None]]).mean(0)\n    aud_t = win / sr\n    # raw epochs at 1 kHz around each sound (for PAC, wavelet power, envelope coherence)\n    e0, e1 = int(EPOCH[0] * FS), int(EPOCH[1] * FS)\n    on1 = np.round(tr.onset.to_numpy() * FS).astype(int)\n    raw_ep = None\n    if keep_raw:\n        raw_ep = np.stack([raw[:, o + e0:o + e1] for o in on1])\n    del raw\n    chg = ch[good].reset_index(drop=True)\n    chg[\"subject\"] = subject\n    chg = chg.merge(el[[\"name\", \"x\", \"y\"]], on=\"name\", how=\"left\")\n    return dict(subject=subject, events=ev, trials=tr, channels=ch, good=chg, electrodes=el,\n                json=js, hfb=hfb, spec=spec, env=envs, audio_sr=sr, audio_len=len(audio),\n                audio_onset_profile=(aud_t, aud), raw_ep=raw_ep, stats=stats)\n\n\n# ---------------------------------------------------------------- HFB epochs and z-scores\n\ndef hfb_epochs(d, t0=EPOCH[0], t1=EPOCH[1]):\n    \"\"\"(trials, channels, time) HFB at 50 Hz around each sound onset, and its times.\"\"\"\n    i0, i1 = int(round(t0 * FS_OUT)), int(round(t1 * FS_OUT))\n    on = np.round(d[\"trials\"].onset.to_numpy() * FS_OUT).astype(int)\n    ep = np.stack([d[\"hfb\"][:, o + i0:o + i1] for o in on])\n    return ep, np.arange(i0, i1) / FS_OUT\n\n\ndef zscore_epochs(d, ep, times, mode):\n    \"\"\"z-score HFB over baseline (claims, open detail 3):\n    'trial'  each trial by the mean and s.d. of its own -800 to -100 ms baseline;\n    'pooled' by the mean and s.d. of all baseline samples of the electrode;\n    'nonevent' the whole series z-scored by its samples outside any sound (ecogtools\n               zscore_by_non_events), then epoched.\n    \"\"\"\n    b = (times >= BASELINE[0]) & (times <= BASELINE[1])\n    if mode == \"trial\":\n        m = ep[..., b].mean(-1, keepdims=True)\n        s = ep[..., b].std(-1, keepdims=True)\n        return (ep - m) / s\n    if mode == \"pooled\":\n        m = ep[..., b].mean((0, 2), keepdims=True)\n        s = ep[..., b].std((0, 2), keepdims=True)\n        return (ep - m) / s\n    if mode == \"nonevent\":\n        h = d[\"hfb\"]\n        mask = np.ones(h.shape[1], bool)\n        for _, r in d[\"trials\"].iterrows():\n            mask[int(r.onset * FS_OUT):int((r.onset + r.duration) * FS_OUT) + 1] = False\n        m = h[:, mask].mean(1)[None, :, None]\n        s = h[:, mask].std(1)[None, :, None]\n        return (ep - m) / s\n    raise ValueError(mode)\n\n\ndef post_mean(zep, times, durations, window):\n    \"\"\"Mean post-stimulus HFB per trial and channel (claims, open detail 2):\n    'sound' onset to the end of each sound; '2.5' 0 to 2.5 s.\"\"\"\n    out = np.empty(zep.shape[:2])\n    for i, dur in enumerate(durations):\n        end = dur if window == \"sound\" else 2.5\n        sel = (times >= 0) & (times < end)\n        out[i] = zep[i][:, sel].mean(-1)\n    return out\n\n\ndef bootstrap_lower(vals, rng, n_boot=10000, q=0.5):\n    \"\"\"0.5th percentile of the bootstrap distribution of the mean over trials, per channel.\n    Methods, Evoked HFB: 99% interval, lower bound the 0.5th percentile. 10,000 resamples:\n    claims, open detail 5 (standard).\"\"\"\n    n = vals.shape[0]\n    idx = rng.integers(0, n, size=(n_boot, n))\n    means = vals[idx].mean(1)                           # (n_boot, channels)\n    return np.percentile(means, q, axis=0)\n\n\ndef signflip_test(diff, rng, n_perm=10000):\n    \"\"\"Methods, Between-condition permutation test statistics: signs flipped at random 10,000\n    times, the mean as statistic, two-sided P from the null quantile of the true mean.\"\"\"\n    diff = np.asarray(diff, float)\n    diff = diff[np.isfinite(diff)]\n    signs = rng.choice([-1.0, 1.0], size=(n_perm, len(diff)))\n    null = (signs * diff).mean(1)\n    obs = diff.mean()\n    p = (np.sum(np.abs(null) >= abs(obs)) + 1) / (n_perm + 1)\n    return obs, p\n\n\n# ---------------------------------------------------------------- eSTRF (ridge, leave-one-trial-out)\n\ndef lagged(spec_seg, start, stop, max_lag=MAX_LAG):\n    \"\"\"Design rows for samples start..stop-1 of a spectrogram segment, lags 0..max_lag.\"\"\"\n    rows = [spec_seg[:, start - l:stop - l] for l in range(max_lag + 1)]\n    return np.concatenate(rows, axis=0).T          # (samples, bands*lags), lag-major\n\n\ndef trial_design(d, idx, window=\"sound\", tmax_extra=0.4):\n    \"\"\"X, y blocks per trial for the trials idx (claims, open detail 7):\n    'sound' samples from onset to offset; 'plus' onset to offset + 400 ms.\"\"\"\n    Xs, ys = [], []\n    on = np.round(d[\"trials\"].onset.to_numpy() * FS_OUT).astype(int)\n    for i in idx:\n        r = d[\"trials\"].iloc[i]\n        n = int(np.floor(r.duration * FS_OUT)) + (int(tmax_extra * FS_OUT) if window == \"plus\" else 0)\n        s0 = int(0.5 * FS_OUT)                       # segment starts 0.5 s before onset\n        seg = d[\"spec\"][i]\n        n = min(n, seg.shape[1] - s0)\n        Xs.append(lagged(seg, s0, s0 + n))\n        ys.append(d[\"hfb\"][:, on[i]:on[i] + n].T)\n    return Xs, ys\n\n\ndef ridge_loto(Xs, ys, alphas):\n    \"\"\"Leave-one-trial-out ridge for all channels at once, inputs and outputs z-scored with\n    the training trials' statistics (Methods, eSTRF model formulation).\n\n    Returns coefs (folds, alphas, features, channels) and r2 (folds, alphas, channels), R2\n    on the held-out trial (coefficient of determination, as sklearn's r2_score).\n    \"\"\"\n    n_tr = len(Xs)\n    XtX = [X.T @ X for X in Xs]\n    Xty = [X.T @ y for X, y in zip(Xs, ys)]\n    sx = [X.sum(0) for X in Xs]\n    sy = [y.sum(0) for y in ys]\n    sxx = [(X ** 2).sum(0) for X in Xs]\n    syy = [(y ** 2).sum(0) for y in ys]\n    nn = np.array([len(X) for X in Xs])\n    T = dict(XtX=sum(XtX), Xty=sum(Xty), sx=sum(sx), sy=sum(sy), sxx=sum(sxx), syy=sum(syy), n=nn.sum())\n    p, c = Xs[0].shape[1], ys[0].shape[1]\n    coefs = np.empty((n_tr, len(alphas), p, c), np.float32)\n    r2 = np.empty((n_tr, len(alphas), c))\n    for k in range(n_tr):\n        n = T[\"n\"] - nn[k]\n        mx = (T[\"sx\"] - sx[k]) / n\n        my = (T[\"sy\"] - sy[k]) / n\n        vx = (T[\"sxx\"] - sxx[k]) / n - mx ** 2\n        vy = (T[\"syy\"] - syy[k]) / n - my ** 2\n        dx = np.sqrt(np.maximum(vx, 1e-20))\n        dy = np.sqrt(np.maximum(vy, 1e-20))\n        C = (T[\"XtX\"] - XtX[k]) - n * np.outer(mx, mx)\n        C = C / np.outer(dx, dx)\n        B = (T[\"Xty\"] - Xty[k]) - n * np.outer(mx, my)\n        B = B / np.outer(dx, dy)\n        w, V = np.linalg.eigh(C)\n        VB = V.T @ B\n        Xt = (Xs[k] - mx) / dx\n        yt = (ys[k] - my) / dy\n        XV = Xt @ V\n        sst = ((yt - yt.mean(0)) ** 2).sum(0)\n        for a, al in enumerate(alphas):\n            Wt = VB / (w + al)[:, None]\n            coefs[k, a] = V @ Wt\n            pred = XV @ Wt\n            r2[k, a] = 1 - ((yt - pred) ** 2).sum(0) / sst\n    return coefs, r2\n\n\ndef predict(coef, X, y):\n    \"\"\"Prediction of z-scored y from z-scored X (each by its own statistics), and R2 per channel.\"\"\"\n    Xz = (X - X.mean(0)) / X.std(0)\n    yz = (y - y.mean(0)) / y.std(0)\n    pred = Xz @ coef\n    r2 = 1 - ((yz - pred) ** 2).sum(0) / ((yz - yz.mean(0)) ** 2).sum(0)\n    return pred, r2\n\n\ndef partial_corr(a, b, c, intercept=False):\n    \"\"\"pcorr(a, b | c) = corr(a - a_hat_c, b) as in the Methods (eSTRF linear overlap) and the\n    code's partial_corr (least squares on c, no intercept by default).\"\"\"\n    C = np.column_stack([c, np.ones_like(c)]) if intercept else c[:, None]\n    beta = np.linalg.lstsq(C, a, rcond=None)[0]\n    res = a - C @ beta\n    return np.corrcoef(res, b)[0, 1]\n\n\ndef mtf(strf, n_bands=N_BANDS, n_lags=MAX_LAG + 1):\n    \"\"\"Modulation transfer function: amplitude of the 2-D FFT of the eSTRF (bands x lags),\n    centred. Methods, MTF of eSTRFs.\"\"\"\n    s = strf.reshape(n_lags, n_bands).T\n    return np.abs(np.fft.fftshift(np.fft.fft2(s)))\n\n\n# ---------------------------------------------------------------- multitaper coherence\n\ndef mt_coherence(x, y, fs, nw=2.0, jackknife=True):\n    \"\"\"Multitaper coherence of two 1-D signals over the last axis, with tapers DPSS(nw, 2nw-1).\n    With jackknife=True the jackknife bias-corrected estimate over tapers (Thomson & Chave)\n    on the Fisher-transformed coherency magnitude. Returns freqs, coherence (..., freqs).\"\"\"\n    n = x.shape[-1]\n    k = int(2 * nw - 1)\n    tap = ss.windows.dpss(n, nw, k)\n    X = np.fft.rfft(tap * x[..., None, :], axis=-1)\n    Y = np.fft.rfft(tap * y[..., None, :], axis=-1)\n    freqs = np.fft.rfftfreq(n, 1 / fs)\n\n    def coh(sel):\n        sxy = (X[..., sel, :] * np.conj(Y[..., sel, :])).mean(-2)\n        sxx = (np.abs(X[..., sel, :]) ** 2).mean(-2)\n        syy = (np.abs(Y[..., sel, :]) ** 2).mean(-2)\n        return np.abs(sxy) ** 2 / (sxx * syy)\n\n    full = coh(np.arange(k))\n    if not jackknife:\n        return freqs, full\n    ft = lambda c: np.arctanh(np.sqrt(np.clip(c, 0, 1 - 1e-12)))\n    loo = np.stack([ft(coh(np.delete(np.arange(k), i))) for i in range(k)])\n    z = k * ft(full) - (k - 1) * loo.mean(0)\n    return freqs, np.tanh(np.maximum(z, 0)) ** 2\n\n\ndef coh_to_bits(coh, freqs, fmax=None):\n    \"\"\"Normal mutual information, the integral over frequency of -log2(1 - coh) (Methods,\n    Between-condition coherence; coh_to_bits in ecogtools), in bits/s.\"\"\"\n    sel = freqs > 0 if fmax is None else (freqs > 0) & (freqs <= fmax)\n    df = freqs[1] - freqs[0]\n    return (-np.log2(1 - np.clip(coh[..., sel], 0, 1 - 1e-9))).sum(-1) * df\n"
}
```

```
File created successfully at: entries/crcns-ac-4-holdgraf-2016/ac4.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/crcns-ac-4-holdgraf-2016 && python - <<'EOF'
import re
s=open('ac4.py').read()
s=s.replace("""    coefs = np.empty((n_tr, len(alphas), p, c), np.float32)""","""    keep = len(alphas) == 1
    coefs = np.empty((n_tr, len(alphas), p, c), np.float32) if keep else None""")
s=s.replace("""            coefs[k, a] = V @ Wt
""","""            if keep:
                coefs[k, a] = V @ Wt
""")
s=s.replace("""    Returns coefs (folds, alphas, features, channels) and r2""","""    Returns coefs (folds, alphas, features, channels; only when one alpha is given) and r2""")
open('ac4.py','w').write(s)
EOF
cd $TMPDIR; . dev/bin/activate; cd entries/crcns-ac-4-holdgraf-2016; python -c "
import time,resource,ac4,numpy as np
t=time.time(); z=ac4.open_zip()
d=ac4.load_subject(z,'S04')
print('load',time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,'GB')
print(d['stats'], d['hfb'].shape, d['raw_ep'].shape, len(d['spec']), d['spec'][0].shape, d['audio_sr'])
t_,a=d['audio_onset_profile']; print('audio pre',a[t_<-0.05].mean(),'post',a[(t_>0.05)&(t_<0.5)].mean())
print(d['trials'].overlaps_bad.sum())
"
```

```
load 51.56219458580017 1.077792 GB
{'n_samples': 660212, 'raw_abs_median': 205752032.0, 'car_residual': 1.601340748891289e-08} (40, 33011) (102, 40, 4500) 102 (32, 208) 16000
audio pre 0.0007102582058365825 post 0.011461619155535379
4
```

**Agent calls Bash**

```bash
cd $TMPDIR; . dev/bin/activate; cd entries/crcns-ac-4-holdgraf-2016; python -c "
import time,resource,ac4,pickle,os
z=ac4.open_zip()
for s in ac4.SUBJECTS:
  t=time.time(); d=ac4.load_subject(z,s)
  pickle.dump(d,open(os.environ['TMPDIR']+'/'+s+'.pkl','wb'))
  print(s,round(time.time()-t),resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6, d['stats'], d['trials'].overlaps_bad.sum(), flush=True)
  del d
" 2>&1 | grep -v Warn
```

```
S01 98 2.230796 {'n_samples': 1204042, 'raw_abs_median': 315.1260681152344, 'car_residual': 1.910911429092721e-08} 7
S02 72 2.230796 {'n_samples': 815001, 'raw_abs_median': 210374528.0, 'car_residual': 1.8940450985382995e-08} 0
S03 58 2.230796 {'n_samples': 780167, 'raw_abs_median': 624460992.0, 'car_residual': 1.2341814681349206e-08} 10
S04 50 2.230796 {'n_samples': 660212, 'raw_abs_median': 205752032.0, 'car_residual': 1.601340748891289e-08} 4
S07 87 2.230796 {'n_samples': 988914, 'raw_abs_median': 272256832.0, 'car_residual': 1.5803372832579043e-08} 1
S08 77 2.230796 {'n_samples': 942244, 'raw_abs_median': 370338624.0, 'car_residual': 1.1969168767222982e-08} 0
S13 87 2.230796 {'n_samples': 982012, 'raw_abs_median': 174729040.0, 'car_residual': 1.891247514151928e-08} 0
```

**Agent calls Bash**

```bash
cd $TMPDIR; . dev/bin/activate; cd entries/crcns-ac-4-holdgraf-2016; cat > $TMPDIR/dev_load.py <<'EOF'
import pickle,os,ac4
D={s:pickle.load(open(os.environ['TMPDIR']+'/'+s+'.pkl','rb')) for s in ac4.SUBJECTS}
EOF
python -c "
exec(open('$TMPDIR/dev_load.py').read())
import numpy as np, itertools
rng=np.random.default_rng(0)
for s,d in D.items():
  tr=d['trials']; print(s, tr.phase.value_counts().to_dict() if 'phase' in tr else tr.trial_phase.value_counts().to_dict(), 'tn-1', (tr.trial_num==-1).sum(), 'noise', tr.noise.sum())
res={}
for s,d in D.items():
  ep,times=ac4.hfb_epochs(d); tr=d['trials']
  for z in ['trial','pooled','nonevent']:
    zep=ac4.zscore_epochs(d,ep,times,z)
    for w in ['sound','2.5']:
      pm=ac4.post_mean(zep,times,tr.duration.to_numpy(),w)
      for tsel in ['mid','all']:
        sel=(tr.trial_num>=0)&(~tr.noise | (tr.trial_phase!='mid'))
        sel = sel&(tr.trial_phase=='mid') if tsel=='mid' else sel
        lb=ac4.bootstrap_lower(pm[sel.to_numpy()],rng,2000)
        res.setdefault((z,w,tsel),[]).append((lb>0).sum())
for k,v in res.items(): print(k,v,sum(v))
"
```

```
S01 {'mid': 62, 'bef': 56, 'aft': 56} tn-1 6 noise 0
S02 {'mid': 53, 'bef': 47, 'aft': 46} tn-1 6 noise 0
S03 {'mid': 44, 'bef': 39, 'aft': 38} tn-1 6 noise 0
S04 {'mid': 38, 'bef': 32, 'aft': 32} tn-1 6 noise 0
S07 {'bef': 57, 'mid': 57, 'aft': 57} tn-1 0 noise 84
S08 {'bef': 57, 'mid': 57, 'aft': 57} tn-1 0 noise 84
S13 {'bef': 57, 'mid': 57, 'aft': 57} tn-1 0 noise 84
('trial', 'sound', 'mid') [np.int64(34), np.int64(30), np.int64(11), np.int64(20), np.int64(19), np.int64(22), np.int64(11)] 147
('trial', 'sound', 'all') [np.int64(47), np.int64(35), np.int64(20), np.int64(22), np.int64(22), np.int64(33), np.int64(19)] 198
('trial', '2.5', 'mid') [np.int64(31), np.int64(28), np.int64(12), np.int64(19), np.int64(19), np.int64(22), np.int64(11)] 142
('trial', '2.5', 'all') [np.int64(46), np.int64(35), np.int64(19), np.int64(20), np.int64(22), np.int64(32), np.int64(18)] 192
('pooled', 'sound', 'mid') [np.int64(29), np.int64(27), np.int64(15), np.int64(23), np.int64(18), np.int64(11), np.int64(13)] 136
('pooled', 'sound', 'all') [np.int64(40), np.int64(27), np.int64(15), np.int64(21), np.int64(20), np.int64(19), np.int64(16)] 158
('pooled', '2.5', 'mid') [np.int64(28), np.int64(26), np.int64(14), np.int64(22), np.int64(18), np.int64(11), np.int64(12)] 131
('pooled', '2.5', 'all') [np.int64(41), np.int64(28), np.int64(14), np.int64(19), np.int64(19), np.int64(19), np.int64(14)] 154
('nonevent', 'sound', 'mid') [np.int64(19), np.int64(23), np.int64(8), np.int64(16), np.int64(14), np.int64(10), np.int64(15)] 105
('nonevent', 'sound', 'all') [np.int64(19), np.int64(20), np.int64(8), np.int64(12), np.int64(11), np.int64(16), np.int64(15)] 101
('nonevent', '2.5', 'mid') [np.int64(19), np.int64(22), np.int64(8), np.int64(16), np.int64(15), np.int64(10), np.int64(12)] 102
('nonevent', '2.5', 'all') [np.int64(19), np.int64(21), np.int64(8), np.int64(12), np.int64(11), np.int64(17), np.int64(16)] 104
```

**Agent calls Bash**

```bash
cd $TMPDIR; . dev/bin/activate; cd entries/crcns-ac-4-holdgraf-2016; date -u; python -c "
import pickle,os,ac4,time,numpy as np
d=pickle.load(open(os.environ['TMPDIR']+'/S04.pkl','rb'))
tr=d['trials']
idx=np.where((tr.trial_phase=='mid')&(tr.trial_num>=0)&~tr.noise)[0]
t=time.time()
Xs,ys=ac4.trial_design(d,idx)
print('design',time.time()-t, len(Xs), Xs[0].shape, ys[0].shape)
al=np.logspace(0,6,13)
t=time.time(); c,r2=ac4.ridge_loto(Xs,ys,al); print('ridge',time.time()-t)
best=al[r2.argmax(1)]
print(np.unique(best,return_counts=True))
m=r2.max(1).mean(0); print(np.round(np.sort(m)[::-1][:10],3))
print(np.round(r2.mean(0).max(1),3))
"
```

```
Mon Nov  9 08:12:26 UTC 2026
design 0.009172201156616211 32 (119, 672) (119, 40)
ridge 1.0277976989746094
(array([1.00000000e+00, 3.16227766e+00, 1.00000000e+01, 3.16227766e+01,
       1.00000000e+02, 3.16227766e+02, 1.00000000e+03, 3.16227766e+03,
       1.00000000e+04, 3.16227766e+04, 1.00000000e+05, 3.16227766e+05,
       1.00000000e+06]), array([ 12,   3,   5,   7,  12,  28,  52, 102, 161, 176, 145, 134, 443]))
[ 0.276  0.26   0.25   0.15   0.125  0.091  0.081  0.042  0.041 -0.001]
[0.118 0.119 0.122 0.129 0.146 0.173 0.205 0.232 0.242 0.234 0.226 0.193
 0.106]
```

**Agent calls Bash**

```bash
grep -n -i "supplementary figure 5\|Supplementary Figure 3\|Supplementary Figure 4\|Supplementary Figure 6\|Supplementary Figure 7\|Supplementary Figure 2" paper/10.1038-ncomms13654.txt 2>/dev/null; cd  grep -n "HFB and trial\|trial number\|Supplementary Figure [2-7]" paper/10.1038-ncomms13654.txt | head; sed -n 1950,1975p paper/10.1038-ncomms13654.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1866,1950p paper/10.1038-ncomms13654.txt; sed -n 1982,2060p paper/10.1038-ncomms13654.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude/nb_src.py",
 "content": "# %% md\n# Reproducing Holdgraf et al. (2016) from CRCNS ac-4\n\nPaper: Holdgraf, de Heer, Pasley, Rieger, Crone, Lin, Knight & Theunissen (2016), \"Rapid tuning\nshifts in human auditory cortex enhance speech intelligibility\", Nat Commun 7:13654,\ndoi:10.1038/ncomms13654.\n\nDataset: CRCNS ac-4 (doi:10.6080/K08S4N4J), \"Electrocorticography recordings from patients during\na passive listening task of degraded and intact English speech\", read in place from\n`ac-4/live/data.zip` in the public S3 bucket `crcnsarchive`.\n\nVersion: CRCNS data sets are not versioned, so the version is recorded as `unversioned`. The\nbucket holds one copy of the data set (`ac-4/live/`, no `old/` folder), the data descriptor's\nversion 0.6 of 28 May 2019, which is the only published version and the one the paper's\ndata availability statement points to. The MD5 of `data.zip` in the data set's `checksums.md5`\nis printed below, so a later change is detectable.\n\nClaims: `claims/crcns-ac-4/10.1038-ncomms13654.yaml`, written from the version of record with its\nSupplementary Information. The claims file decides what is tested; method details it lacks are\ntaken from the paper and cited where they are used (in this notebook or in `ac4.py`).\n\n| Claim | Tested here |\n|---|---|\n| behav-no-context-baseline, behav-context-enhancement, supp1a-linguistic-context, supp1a-speaker-no-difference, supp1b-filter-type, supp5a-behaviour-over-trials | Blocked: the behavioural control data are not in the data set |\n| speech-r-count | Tested |\n| fig3b-hfb-increase-after | Tested |\n| supp3a-pink-noise-no-hfb-change | Tested |\n| supp5b-hfb-stable-over-session | Tested |\n| fig4a-coherence-after-higher, fig4b-coherence-sentence-specific | Tested |\n| strf-r-count, included-electrode-count | Tested |\n| fig8-mtf-matches-filter | Tested |\n| fig9-rms-increase, fig9-middle-generalizes-after | Tested |\n| fig10-partial-correlation, fig10b-similarity-correlates, fig10c-stg-location | Tested |\n| supp3b-pink-noise-no-pcorr-change | Tested |\n| supp6a-connectivity-increase, supp6a-after-closer-to-middle, supp6b-no-pac-change | Tested |\n| supp7-envelope-coherence | Tested |\n| supp4-hfb-power-increase | Tested |\n\nThe whole notebook streams about 1.6 GB and takes about 20 minutes, most of it loading.\n\n# %%\nimport os\nos.environ.setdefault(\"OMP_NUM_THREADS\", \"4\")\nimport time\nimport resource\nimport urllib.request\nimport numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nimport mne\nfrom scipy import stats\nimport ac4\n\nmne.set_log_level(\"ERROR\")\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 40)\nprint(ac4.DATASET, \"doi:\" + ac4.DOI)\nprint(urllib.request.urlopen(ac4.BASE + \"/checksums.md5\").read().decode())\n\n# %%\n# LOAD: stream each subject, reduce it to HFB at 50 Hz, the auditory spectrograms and speech\n# envelopes of every sound, and the re-referenced signal around each sound (see ac4.load_subject)\nt0 = time.time()\nz = ac4.open_zip()\nD = {}\nfor s in ac4.SUBJECTS:\n    D[s] = ac4.load_subject(z, s)\n    print(s, f\"{time.time() - t0:.0f} s\", f\"peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.1f} GB\")\n\n# %% md\n## Data check\n\n# %% tags=sanity\ndef region(desc):\n    if desc.startswith(\"temporal\") or desc == \"sub_temporal\":\n        return \"temporal\"\n    if desc.endswith(\"-inferior\"):\n        return \"perisylvian\"          # inferior frontal, premotor, motor, parietal\n    if desc.startswith(\"frontal\") or desc.startswith(\"premotor\"):\n        return \"frontal\"\n    return \"other\"\n\nrows = []\nfor s, d in D.items():\n    ch, tr, js = d[\"channels\"], d[\"trials\"], d[\"json\"]\n    rows.append(dict(subject=s, channels=len(ch), good=int((ch.status == \"good\").sum()),\n                     fs=js[\"SamplingFrequency\"], duration_json=js[\"RecordingDuration\"],\n                     duration_samples=d[\"stats\"][\"n_samples\"] / ac4.FS,\n                     audio_sr=d[\"audio_sr\"], audio_s=d[\"audio_len\"] / d[\"audio_sr\"],\n                     triplets=tr.loc[tr.trial_num >= 0, \"trial_num\"].nunique(),\n                     noise_triplets=tr.loc[tr.noise, \"trial_num\"].nunique(),\n                     lone_unfiltered=int((tr.trial_num < 0).sum()),\n                     sound_s=f\"{tr.duration.min():.2f}-{tr.duration.max():.2f}\",\n                     bad_spans=int((d[\"events\"].trial_type == \"bad\").sum()),\n                     sounds_overlapping_bad=int(tr.overlaps_bad.sum()),\n                     raw_abs_median=d[\"stats\"][\"raw_abs_median\"],\n                     car_residual=d[\"stats\"][\"car_residual\"]))\nsummary = pd.DataFrame(rows)\nprint(summary.to_string())\nprint(\"total channels\", summary.channels.sum(), \"good\", summary.good.sum(), \"(paper: 468 kept of 524)\")\nprint(\"units in channels.tsv:\", {s: d[\"channels\"].units.unique().tolist() for s, d in D.items()})\nprint(\"reference in channels.tsv:\", {s: d[\"channels\"].reference.unique().tolist() for s, d in D.items()})\n\nE = pd.concat([d[\"good\"] for d in D.values()], ignore_index=True)\nE[\"region\"] = E.description.map(region)\nE[\"stg\"] = E.description.eq(\"temporal-superior\")\nprint(pd.crosstab(E.subject, E.region, margins=True))\nprint(E.description.value_counts().to_string())\n\ncond = pd.concat([d[\"trials\"].assign(subject=s) for s, d in D.items()])\nprint(pd.crosstab([cond.subject, cond.noise], [cond.trial_phase, cond.filt_type]))\n# every triplet has one sound of each phase, the same filter BEFORE and AFTER, and similar durations\nfor s, d in D.items():\n    t = d[\"trials\"][d[\"trials\"].trial_num >= 0]\n    g = t.groupby(\"trial_num\")\n    ok_phase = (g.trial_phase.apply(lambda x: sorted(x) == [\"aft\", \"bef\", \"mid\"])).sum()\n    filt_same = g.apply(lambda x: x.loc[x.trial_phase == \"bef\", \"filt_type\"].tolist() == x.loc[x.trial_phase == \"aft\", \"filt_type\"].tolist()).sum()\n    order = g.apply(lambda x: list(x.sort_values(\"onset\").trial_phase) == [\"bef\", \"mid\", \"aft\"]).sum()\n    print(s, \"triplets\", g.ngroups, \"complete\", ok_phase, \"same filter BEFORE/AFTER\", filt_same, \"in order BEFORE-MIDDLE-AFTER\", order)\n\n# HFB range\nfor s, d in D.items():\n    h = d[\"hfb\"]\n    print(s, \"HFB shape\", h.shape, \"at\", ac4.FS_OUT, \"Hz;\", f\"range {h.min():.3g} to {h.max():.3g} (stored units)\")\n\n# %% md\nThe checks above, stated:\n\n- Sampling rate 1000 Hz in every `ieeg.json`, and sample counts give the stated recording\n  durations (columns `duration_json` and `duration_samples`).\n- The stored values are not in the stated millivolts: the median absolute value is about 300 in\n  S01 and 1.7e8 to 6.2e8 in the other subjects. The analysis uses only z-scored or normalized\n  measures, so the scale does not enter any result; it is recorded as a finding.\n- The good channels are already re-referenced to their common average (the mean over good\n  channels is about 1e-8 of the signal), as `channels.tsv` says (`CAR`).\n- The paper reports 7 subjects with grids of 48, 64, 68, 68, 62, 110 and 104 channels and 468\n  electrodes kept; the data set has 7 subjects with 416 channels, 377 marked good.\n- Three subjects (S07, S08, S13) have pink noise triplets, about half of their triplets, as the\n  paper says.\n\nClock checks follow: the audio track against the event onsets, and the HFB against the onsets,\nwith the onsets shifted as the contrast.\n\n# %% tags=sanity\nfig, ax = plt.subplots(1, 2, figsize=(10, 3))\nfor s, d in D.items():\n    t, a = d[\"audio_onset_profile\"]\n    pre, post = a[(t < -0.05)].mean(), a[(t > 0.05) & (t < 0.5)].mean()\n    ax[0].plot(t, a / post, lw=0.8, label=s)\n    print(s, f\"mean |audio| before onsets {pre:.2e}, 0.05-0.5 s after {post:.2e}, ratio {post / pre:.1f}\")\nax[0].set(xlabel=\"time from sound onset (s)\", ylabel=\"mean |audio| (relative)\", title=\"audio at event onsets\")\nax[0].legend(fontsize=6)\n\n# HFB clock check: on temporal electrodes, mean HFB 0.1-0.5 s after onset minus -0.4-0 s,\n# at the true onsets and at onsets shifted by -2 to +2 s\nshifts = np.arange(-2.0, 2.01, 0.1)\nfor s, d in D.items():\n    temp = (d[\"good\"].description.map(region) == \"temporal\").to_numpy()\n    h = d[\"hfb\"][temp]\n    on = d[\"trials\"].onset.to_numpy()\n    con = []\n    for sh in shifts:\n        i = np.round((on + sh) * ac4.FS_OUT).astype(int)\n        post = np.mean([h[:, j + 5:j + 25].mean() for j in i])\n        pre = np.mean([h[:, j - 20:j].mean() for j in i])\n        con.append((post - pre) / h.std())\n    con = np.array(con)\n    ax[1].plot(shifts, con, lw=0.8)\n    print(s, f\"HFB contrast at true onsets {con[np.argmin(np.abs(shifts))]:.3f}; largest at shift {shifts[np.argmax(con)]:+.1f} s; range {con.min():.3f} to {con.max():.3f}\")\nax[1].set(xlabel=\"onset shift (s)\", ylabel=\"HFB post minus pre (s.d.)\", title=\"HFB at shifted onsets\")\nplt.tight_layout()\n\n# %% md\n## Electrode selection (Speech-R)\n\nMethods, Evoked HFB and speech-responsive electrodes: each trial baselined at -800 to -100 ms,\nthe mean post-stimulus activity per trial, a bootstrap 99% interval of the mean over trials, and\nSpeech-R when its 0.5th percentile is above 0 in response to unfiltered speech. The claims file\nnames three open details (1 trials, 2 window, 3 z-score); every combination is run.\n\nTriplets with pink noise are left out of every speech analysis (Figure 3 heading \"MIDDLE\n(context) unfiltered speech only\"). The six unfiltered sentences outside any triplet in S01 to\nS04 (trial number -1) are left out too: they are not MIDDLE sounds of the task.\n\n> speech-r-count: 92 of the 468 electrodes (19.6%) responded to speech above baseline (Speech-R),\n> generally centred on perisylvian regions.\n\n# %% tags=claim:speech-r-count\nrng = np.random.default_rng(101)\nEP = {}\nfor s, d in D.items():\n    EP[s] = ac4.hfb_epochs(d)\nPOST = {}\nreadings = []\nfor zmode in [\"trial\", \"pooled\", \"nonevent\"]:\n    for win in [\"sound\", \"2.5\"]:\n        for tsel in [\"mid\", \"all\"]:\n            lbs = []\n            for s, d in D.items():\n                ep, times = EP[s]\n                tr = d[\"trials\"]\n                zep = ac4.zscore_epochs(d, ep, times, zmode)\n                pm = ac4.post_mean(zep, times, tr.duration.to_numpy(), win)\n                POST[(s, zmode, win)] = pm\n                sel = (tr.trial_num >= 0) & ~tr.noise\n                if tsel == \"mid\":\n                    sel &= tr.trial_phase == \"mid\"\n                lbs.append(ac4.bootstrap_lower(pm[sel.to_numpy()], rng))\n            lb = np.concatenate(lbs)\n            E[f\"lb_{zmode}_{win}_{tsel}\"] = lb\n            n = int((lb > 0).sum())\n            readings.append(dict(zscore=zmode, window=win, trials=tsel, speech_r=n,\n                                 pct_of_good=100 * n / len(E), within_92_tol=abs(n - 92) <= 9.2,\n                                 **{s: int((lb[E.subject.eq(s).to_numpy()] > 0).sum()) for s in D}))\nR_speech = pd.DataFrame(readings)\nprint(R_speech.to_string())\nprint(f\"electrodes: {len(E)} good of {summary.channels.sum()} in the data set; paper 468 (tolerance 421.2-514.8)\")\nprint(\"readings within 92 +/- 9.2:\", int(R_speech.within_92_tol.sum()), \"of\", len(R_speech))\n\nMAIN = (\"nonevent\", \"sound\", \"mid\")\nE[\"speech_r\"] = E[f\"lb_{MAIN[0]}_{MAIN[1]}_{MAIN[2]}\"] > 0\nprint(\"adopted reading\", MAIN, \"Speech-R\", int(E.speech_r.sum()))\nprint(pd.crosstab(E.region, E.speech_r))\n\n# %% md\nThe reading carried into the later claims is the z-score by non-event times (the code's\n`zscore_by_non_events`), the window to the end of each sound, and MIDDLE trials (the Methods).\nOf the three z-scores only this one gives counts near the paper's; see the record's assumptions.\n\n**Result: speech-r-count.** RESULT_SPEECH_R\n\n# %% md\n## HFB increase AFTER against BEFORE\n\n> fig3b-hfb-increase-after: Across Speech-R electrodes, HFB activity is higher in the AFTER\n> condition than in the BEFORE condition (cluster-based permutation test, P = 0.003, n = 92).\n\nPer electrode, the trial-averaged AFTER minus BEFORE time course of z-scored HFB (Methods, Evoked\nHFB: \"the difference in time-varying HFB activity in each trial was calculated and then averaged\nacross trials\"), from -0.5 to 3 s (the Figure 3b axis), and MNE's one-sample cluster permutation\ntest across electrodes (claims, open detail 11: default threshold, 10,000 permutations).\n\n# %% tags=claim:fig3b-hfb-increase-after\ndef diff_timecourse(zmode, sel_fn, t0=-0.5, t1=3.0):\n    \"\"\"(electrodes, time) of mean AFTER minus mean BEFORE z-HFB, for the electrodes of E in order.\"\"\"\n    out = []\n    for s, d in D.items():\n        ep, times = EP[s]\n        zep = ac4.zscore_epochs(d, ep, times, zmode)\n        tr = d[\"trials\"]\n        keep = (times >= t0) & (times <= t1)\n        b = sel_fn(tr) & (tr.trial_phase == \"bef\")\n        a = sel_fn(tr) & (tr.trial_phase == \"aft\")\n        out.append(zep[a.to_numpy()][..., keep].mean(0) - zep[b.to_numpy()][..., keep].mean(0))\n    return np.concatenate(out), times[keep]\n\ndef cluster_report(X, label, seed, times=None, n_perm=10000):\n    T, clusters, pv, _ = mne.stats.permutation_cluster_1samp_test(X, n_permutations=n_perm, tail=0, seed=seed, out_type=\"mask\")\n    rows = []\n    for c, p in zip(clusters, pv):\n        idx = np.where(c)[0] if c.ndim == 1 else None\n        rows.append(dict(set=label, n=X.shape[0], p=p, sign=\"+\" if T[c].mean() > 0 else \"-\",\n                         start=None if idx is None or times is None else times[idx[0]],\n                         end=None if idx is None or times is None else times[idx[-1]],\n                         size=int(c.sum())))\n    return pd.DataFrame(rows) if rows else pd.DataFrame([dict(set=label, n=X.shape[0], p=np.nan, sign=\"none\", start=None, end=None, size=0)])\n\nspeech = lambda tr: (tr.trial_num >= 0) & ~tr.noise\nout = []\nfor zmode in [\"nonevent\", \"trial\"]:\n    DIF, tt = diff_timecourse(zmode, speech)\n    for label, m in [(\"(a) all Speech-R\", E.speech_r), (\"(b) Speech-R temporal+perisylvian\", E.speech_r & E.region.isin([\"temporal\", \"perisylvian\"]))]:\n        r = cluster_report(DIF[m.to_numpy()], label, 3, tt)\n        r[\"zscore\"] = zmode\n        out.append(r)\n        if zmode == \"nonevent\" and label.startswith(\"(a)\"):\n            DIF_main = DIF[m.to_numpy()]\nR3b = pd.concat(out, ignore_index=True)\nprint(R3b.to_string())\nmean_d = DIF_main.mean(0)\nprint(f\"mean AFTER-BEFORE over electrodes (a): range {mean_d.min():.3f} to {mean_d.max():.3f} z; 0-1 s mean {mean_d[(tt>=0)&(tt<1)].mean():.3f}, 1-3 s mean {mean_d[tt>=1].mean():.3f}\")\nfor s in D:\n    m = (E.subject.eq(s) & E.speech_r).to_numpy()\n    sub = DIF_main[(E.subject[E.speech_r] == s).to_numpy()]\n    print(s, \"Speech-R\", int(m.sum()), \"mean AFTER-BEFORE 0-3 s\", f\"{sub[:, tt >= 0].mean():.3f}\" if len(sub) else \"n/a\")\nfig, ax = plt.subplots(figsize=(6, 3))\nse = DIF_main.std(0) / np.sqrt(len(DIF_main))\nax.plot(tt, mean_d, color=\"purple\")\nax.fill_between(tt, mean_d - se, mean_d + se, color=\"purple\", alpha=0.3)\nax.axhline(0, color=\"k\", lw=0.5)\nax.set(xlabel=\"time (s)\", ylabel=\"AFTER - BEFORE HFB (z)\", title=f\"Speech-R electrodes, n = {len(DIF_main)}\")\n\n# %% md\n**Result: fig3b-hfb-increase-after.** RESULT_FIG3B\n\n## Pink noise triplets: no HFB change\n\n> supp3a-pink-noise-no-hfb-change: In the three subjects with pink noise trials, evoked HFB does\n> not differ between AFTER and BEFORE when the MIDDLE sound was pink noise.\n\nThe same test on the pink noise triplets of S07, S08 and S13. The electrode set (a), the\nelectrodes included in the eSTRF analyses, is computed below with the eSTRF selection; it is\nreported in that section. Set (b), the Speech-R electrodes of the three subjects, is here.\n\n# %% tags=claim:supp3a-pink-noise-no-hfb-change\nnoise_tr = lambda tr: (tr.trial_num >= 0) & tr.noise\nnoise_subjects = [\"S07\", \"S08\", \"S13\"]\ndef noise_diff(zmode=\"nonevent\"):\n    out = []\n    for s in noise_subjects:\n        d = D[s]\n        ep, times = EP[s]\n        zep = ac4.zscore_epochs(d, ep, times, zmode)\n        tr = d[\"trials\"]\n        keep = (times >= -0.5) & (times <= 3.0)\n        b = (noise_tr(tr) & (tr.trial_phase == \"bef\")).to_numpy()\n        a = (noise_tr(tr) & (tr.trial_phase == \"aft\")).to_numpy()\n        out.append(zep[a][..., keep].mean(0) - zep[b][..., keep].mean(0))\n    return np.concatenate(out), times[keep]\nDIFN, ttn = noise_diff()\nEN = E[E.subject.isin(noise_subjects)].reset_index(drop=True)\nr = cluster_report(DIFN[EN.speech_r.to_numpy()], \"(b) Speech-R of S07, S08, S13\", 5, ttn)\nprint(r.to_string())\nprint(\"speech triplets of the same subjects and electrodes, for comparison:\")\nDIFS = diff_timecourse(\"nonevent\", speech)[0][E.subject.isin(noise_subjects).to_numpy()]\nprint(cluster_report(DIFS[EN.speech_r.to_numpy()], \"(b) speech triplets\", 5, ttn).to_string())\nprint(f\"pink noise AFTER-BEFORE mean over (b), 0-3 s: {DIFN[EN.speech_r.to_numpy()][:, ttn >= 0].mean():.3f} z; speech: {DIFS[EN.speech_r.to_numpy()][:, ttn >= 0].mean():.3f} z\")\n\n# %% md\n## HFB over the session\n\n> supp5b-hfb-stable-over-session: Mean HFB activity of Speech-R electrodes shows no significant\n> relation to trial number over a session.\n\nThe paper's test is a bootstrap of the regression slope on trial number (ecogtools\n`bootstrap_coefficients`, 1000 resamples, as the claims file gives it). The value is the mean\npost-stimulus HFB of each speech sound (all three phases, the adopted z-score and window), and\ntrial number the triplet number. Two units, as the criterion names: (a) every Speech-R\nelectrode's value per sound, pooled; (b) the mean over Speech-R electrodes per sound and subject.\n\n# %% tags=claim:supp5b-hfb-stable-over-session\nrng = np.random.default_rng(505)\ndef boot_slope(x, y, rng, n=1000):\n    x, y = np.asarray(x, float), np.asarray(y, float)\n    slopes = np.empty(n)\n    for i in range(n):\n        j = rng.integers(0, len(x), len(x))\n        slopes[i] = np.polyfit(x[j], y[j], 1)[0]\n    return np.polyfit(x, y, 1)[0], np.percentile(slopes, [2.5, 97.5])\nxa, ya, xb, yb, rows = [], [], [], [], []\nfor s, d in D.items():\n    tr = d[\"trials\"]\n    sel = speech(tr).to_numpy()\n    pm = POST[(s, MAIN[0], MAIN[1])][sel][:, E.loc[E.subject.eq(s), \"speech_r\"].to_numpy()]\n    tn = tr.trial_num.to_numpy()[sel]\n    if pm.shape[1] == 0:\n        continue\n    xa.append(np.repeat(tn, pm.shape[1])); ya.append(pm.ravel())\n    xb.append(tn); yb.append(pm.mean(1))\n    sl, ci = boot_slope(tn, pm.mean(1), rng)\n    rows.append(dict(subject=s, sounds=len(tn), speech_r=pm.shape[1], slope=sl, lo=ci[0], hi=ci[1]))\nfor lab, x, y in [(\"(a) electrode x sound\", xa, ya), (\"(b) mean over electrodes per sound\", xb, yb)]:\n    sl, ci = boot_slope(np.concatenate(x), np.concatenate(y), rng)\n    print(f\"{lab}: slope {sl:.4f} z per trial, 95% bootstrap interval {ci[0]:.4f} to {ci[1]:.4f}, includes 0: {ci[0] <= 0 <= ci[1]}\")\nprint(\"per subject (mean over electrodes):\")\nprint(pd.DataFrame(rows).to_string())\n\n# %% md\n**Result: supp5b-hfb-stable-over-session.** RESULT_SUPP5B\n\n## Between-condition coherence\n\n> fig4a-coherence-after-higher / fig4b-coherence-sentence-specific\n\nMethods, Between-condition coherence: per sentence, the coherence of the HFB time course between\nBEFORE and MIDDLE and between AFTER and MIDDLE, in 400 ms windows stepped by 200 ms from -500 to\n2500 ms, jackknife-corrected, converted to bits/s, averaged over trials; then the sign-flip test\nof AFTER/MIDDLE minus BEFORE/MIDDLE across electrodes for the windows of Figure 4 (-1 to 0, 0 to\n1, 1 to 2.5 s; a window is assigned by its centre). The multitaper bandwidth is open (claims,\nopen detail 10): a 400 ms window at 50 Hz holds 20 samples, and MNE's default bandwidth (4 Hz)\ngives a single taper, for which single-trial coherence is 1. The choice here is NW = 2 (three\ntapers, 10 Hz bandwidth), jackknife over tapers, and the integral over 2.5 to 25 Hz. Electrode\nsets: (a) Speech-R on temporal or perisylvian cortex, (b) all temporal or perisylvian electrodes.\nPanel b subtracts from each trial the electrode's mean time course, (a) over all trials of all\nthree conditions, (b) per condition.\n\n# %% tags=claim:fig4a-coherence-after-higher\nWIN_STARTS = np.round(np.arange(-0.5, 2.1001, 0.2), 1)\nWIN_CENTRES = WIN_STARTS + 0.2\ndef coherence_bits(subtract=None):\n    \"\"\"(electrodes of E, 2 pairs, windows) mean over triplets of integrated coherence in bits/s.\"\"\"\n    out = []\n    for s, d in D.items():\n        ep, times = EP[s]\n        zep = ac4.zscore_epochs(d, ep, times, MAIN[0])\n        tr = d[\"trials\"]\n        tsel = speech(tr)\n        trip = sorted(tr.loc[tsel, \"trial_num\"].unique())\n        ix = {ph: [tr.index[(tr.trial_num == n) & (tr.trial_phase == ph)][0] for n in trip] for ph in [\"bef\", \"mid\", \"aft\"]}\n        X = {ph: zep[ix[ph]] for ph in ix}\n        if subtract == \"all\":\n            m = zep[tsel.to_numpy()].mean(0)\n            X = {ph: X[ph] - m for ph in X}\n        elif subtract == \"condition\":\n            X = {ph: X[ph] - X[ph].mean(0) for ph in X}\n        res = np.empty((zep.shape[1], 2, len(WIN_STARTS)))\n        for w, ws in enumerate(WIN_STARTS):\n            sel = (times >= ws - 1e-9) & (times < ws + 0.4 - 1e-9)\n            for k, ph in enumerate([\"bef\", \"aft\"]):\n                f, c = ac4.mt_coherence(X[ph][..., sel], X[\"mid\"][..., sel], ac4.FS_OUT, nw=2.0)\n                res[:, k, w] = ac4.coh_to_bits(c, f).mean(0)\n        out.append(res)\n    return np.concatenate(out), f\n\ndef window_tests(C, mask, rng, label):\n    rows = []\n    for name, lo, hi in [(\"-1 to 0 s\", -1, 0), (\"0 to 1 s\", 0, 1), (\"1 to 2.5 s\", 1, 2.6)]:\n        w = (WIN_CENTRES >= lo) & (WIN_CENTRES < hi)\n        diff = (C[mask][:, 1, w] - C[mask][:, 0, w]).mean(1)\n        obs, p = ac4.signflip_test(diff, rng)\n        rows.append(dict(set=label, window=name, n=int(mask.sum()), windows=int(w.sum()),\n                         bef_mid=C[mask][:, 0, w].mean(), aft_mid=C[mask][:, 1, w].mean(),\n                         diff=obs, se=diff.std(ddof=1) / np.sqrt(len(diff)), p=p))\n    return rows\n\nrng = np.random.default_rng(404)\nC4a, fr = coherence_bits(None)\nprint(\"coherence frequencies (Hz):\", fr)\nperi = E.region.isin([\"temporal\", \"perisylvian\"]).to_numpy()\nsets4 = {\"(a) Speech-R temporal+perisylvian\": peri & E.speech_r.to_numpy(), \"(b) all temporal+perisylvian\": peri}\nR4a = pd.DataFrame(sum([window_tests(C4a, m, rng, k) for k, m in sets4.items()], []))\nprint(R4a.to_string())\nprint(\"per subject, set (a), 0-2.5 s AFTER/MIDDLE minus BEFORE/MIDDLE (bits/s):\")\nfor s in D:\n    m = sets4[\"(a) Speech-R temporal+perisylvian\"] & E.subject.eq(s).to_numpy()\n    w = WIN_CENTRES >= 0\n    print(\" \", s, int(m.sum()), f\"{(C4a[m][:, 1, w] - C4a[m][:, 0, w]).mean():.3f}\" if m.any() else \"n/a\")\nm = sets4[\"(a) Speech-R temporal+perisylvian\"]\nfig, ax = plt.subplots(figsize=(6, 3))\nfor k, lab in enumerate([\"BEFORE/MIDDLE\", \"AFTER/MIDDLE\"]):\n    ax.plot(WIN_CENTRES, C4a[m][:, k].mean(0), label=lab)\nax.set(xlabel=\"window centre (s)\", ylabel=\"coherence (bits/s)\")\nax.legend()\nprint(f\"plotted range {C4a[m].mean(0).min():.3f} to {C4a[m].mean(0).max():.3f} bits/s\")\n\n# %% md\n**Result: fig4a-coherence-after-higher.** RESULT_FIG4A\n\n# %% tags=claim:fig4b-coherence-sentence-specific\nrng = np.random.default_rng(405)\nrows = []\nfor sub in [\"all\", \"condition\"]:\n    C4b, _ = coherence_bits(sub)\n    for r in sum([window_tests(C4b, m, rng, k) for k, m in sets4.items()], []):\n        r[\"subtracted\"] = \"(a) mean over all trials\" if sub == \"all\" else \"(b) mean per condition\"\n        rows.append(r)\nR4b = pd.DataFrame(rows)\nprint(R4b.to_string())\n\n# %% md\n**Result: fig4b-coherence-sentence-specific.** RESULT_FIG4B\n\n## eSTRF fits\n\nMethods, eSTRF model formulation: ridge regression of HFB on the auditory spectrogram at lags 0\nto 400 ms, inputs and outputs z-scored (with the training trials' statistics here), one trial\nleft out per split, R2 on the held-out trial; the ridge parameter is the mode of the per-split\nbest values over active (Speech-R) electrodes and all conditions, and every model is re-fit with\nit; coefficients averaged over splits, and their mean over s.d. across splits where the paper\nsays so. The ridge grid is a standard choice (log-spaced, 1 to 1e8), checked below to have its\nmode inside the grid. Samples per trial (claims, open detail 7): (a) onset to offset, the main\nreading; (b) onset to 400 ms after offset, run for the selection counts.\n\n# %%\nALPHAS = np.logspace(0, 8, 17)\ndef cond_idx(tr, phase, noise=False, filt=None):\n    sel = (tr.trial_num >= 0) & (tr.noise == noise) & (tr.trial_phase == phase)\n    if filt is not None:\n        sel &= tr.filt_type == filt\n    return np.where(sel.to_numpy())[0]\n\nt0 = time.time()\nbest = []\nfor s, d in D.items():\n    sr = E.loc[E.subject.eq(s), \"speech_r\"].to_numpy()\n    for ph in [\"bef\", \"mid\", \"aft\"]:\n        Xs, ys = ac4.trial_design(d, cond_idx(d[\"trials\"], ph))\n        _, r2 = ac4.ridge_loto(Xs, ys, ALPHAS)\n        best.append(ALPHAS[r2.argmax(1)][:, sr].ravel())\nbest = np.concatenate(best)\nvals, counts = np.unique(best, return_counts=True)\nALPHA = vals[np.argmax(counts)]\nprint(pd.Series(counts, index=[f\"{v:.0e}\" for v in vals]).to_string())\nprint(f\"mode {ALPHA:.0e} (grid {ALPHAS[0]:.0e} to {ALPHAS[-1]:.0e}); {len(best)} split x electrode values; {time.time() - t0:.0f} s\")\n\nFITS = {}\ndef fit(s, key, idx, window=\"sound\"):\n    d = D[s]\n    Xs, ys = ac4.trial_design(d, idx, window)\n    coefs, r2 = ac4.ridge_loto(Xs, ys, [ALPHA])\n    coefs, r2 = coefs[:, 0], r2[:, 0]\n    FITS[(s, key)] = dict(mean=coefs.mean(0), z=coefs.mean(0) / coefs.std(0), r2=r2, n_trials=len(idx))\nt0 = time.time()\nfor s, d in D.items():\n    tr = d[\"trials\"]\n    for ph in [\"bef\", \"mid\", \"aft\"]:\n        fit(s, ph, cond_idx(tr, ph))\n    fit(s, \"mid_plus\", cond_idx(tr, \"mid\"), \"plus\")\n    for ph in [\"bef\", \"aft\"]:\n        for fl in [\"temp\", \"freq\"]:\n            fit(s, f\"{ph}_{fl}\", cond_idx(tr, ph, filt=fl))\n    if tr.noise.any():\n        for ph in [\"bef\", \"mid\", \"aft\"]:\n            fit(s, f\"noise_{ph}\", cond_idx(tr, ph, noise=True))\nprint(f\"fits done in {time.time() - t0:.0f} s\")\nprint(pd.DataFrame([dict(subject=s, fit=k, trials=v[\"n_trials\"], median_r2=np.median(v[\"r2\"])) for (s, k), v in FITS.items()]).pivot(index=\"subject\", columns=\"fit\", values=\"trials\").to_string())\n\n# %% md\n## STRF-R electrodes\n\n> strf-r-count: 53 of 468 electrodes (11.3%) were well modelled by the eSTRF (STRF-R), generally\n> on perisylvian temporal lobe.\n\nMethods, STRF-responsive electrode selection: the lower bound of the R2 over cross-validation\nsplits of the MIDDLE model above 0. Readings (claims, open detail 8): (a) 0.5th percentile of a\nbootstrap of the mean R2 over splits, (b) 1st percentile of the per-split R2, (c) 0.5th\npercentile of the per-split R2; with the samples of open detail 7, (a) and (b).\n\n# %% tags=claim:strf-r-count\nrng = np.random.default_rng(606)\nrows = []\nfor key, wlab in [(\"mid\", \"(a) onset-offset\"), (\"mid_plus\", \"(b) to offset+400 ms\")]:\n    lb = {\"a\": [], \"b\": [], \"c\": []}\n    for s in D:\n        r2 = FITS[(s, key)][\"r2\"]\n        lb[\"a\"].append(ac4.bootstrap_lower(r2, rng))\n        lb[\"b\"].append(np.percentile(r2, 1, axis=0))\n        lb[\"c\"].append(np.percentile(r2, 0.5, axis=0))\n    for k in lb:\n        v = np.concatenate(lb[k])\n        E[f\"strf_{key}_{k}\"] = v > 0\n        rows.append(dict(samples=wlab, bound=k, strf_r=int((v > 0).sum()), within_53_tol=abs((v > 0).sum() - 53) <= 5.3,\n                         **{s: int((v[E.subject.eq(s).to_numpy()] > 0).sum()) for s in D}))\nR_strf = pd.DataFrame(rows)\nprint(R_strf.to_string())\nE[\"mid_r2\"] = np.concatenate([FITS[(s, \"mid\")][\"r2\"].mean(0) for s in D])\nE[\"strf_r\"] = E[\"strf_mid_a\"]\nprint(\"adopted: samples (a), bound (a); STRF-R\", int(E.strf_r.sum()))\nprint(pd.crosstab(E.region, E.strf_r))\nprint(f\"mean held-out R2 of MIDDLE models over STRF-R electrodes: {E.loc[E.strf_r, 'mid_r2'].mean():.3f} (range {E.loc[E.strf_r, 'mid_r2'].min():.3f} to {E.loc[E.strf_r, 'mid_r2'].max():.3f})\")\n\n# %% md\n**Result: strf-r-count.** RESULT_STRF\n\n## Electrodes included in the eSTRF analyses\n\n> included-electrode-count: 41 of 468 electrodes (8.76%) were Speech-R, STRF-R and on the temporal\n> lobe or perisylvian cortex, and enter the eSTRF analyses.\n\nLocation from the anatomical label of each channel in `channels.tsv` (claims, open detail 6):\ntemporal lobe (`temporal-*`, `sub_temporal`) and perisylvian (`*-inferior` frontal, premotor,\nmotor and parietal). The paper's Figure 10c legend restricts the model results to the temporal\nlobe; that set is shown too.\n\n# %% tags=claim:included-electrode-count\nrows = []\nfor zr in R_speech.itertuples():\n    sr = E[f\"lb_{zr.zscore}_{zr.window}_{zr.trials}\"] > 0\n    for key in [\"mid_a\", \"mid_b\", \"mid_c\", \"mid_plus_a\", \"mid_plus_b\", \"mid_plus_c\"]:\n        st = E[f\"strf_{key}\"]\n        rows.append(dict(speech_r=f\"{zr.zscore}/{zr.window}/{zr.trials}\", strf=key,\n                         temporal_perisylvian=int((sr & st & E.region.isin([\"temporal\", \"perisylvian\"])).sum()),\n                         temporal_only=int((sr & st & E.region.eq(\"temporal\")).sum())))\nR_inc = pd.DataFrame(rows)\nR_inc[\"within_41_tol\"] = (R_inc.temporal_perisylvian - 41).abs() <= 4.1\nprint(R_inc.to_string())\nprint(\"readings within 41 +/- 4.1:\", int(R_inc.within_41_tol.sum()), \"of\", len(R_inc))\nE[\"included\"] = E.speech_r & E.strf_r & E.region.isin([\"temporal\", \"perisylvian\"])\nprint(\"adopted reading: included\", int(E.included.sum()))\nprint(E[E.included].groupby([\"subject\", \"region\"]).size().unstack(fill_value=0))\n\n# %% md\n**Result: included-electrode-count.** RESULT_INCLUDED\n\n### Pink noise HFB on the included electrodes (supp3a, set (a))\n\n# %% tags=claim:supp3a-pink-noise-no-hfb-change\nprint(cluster_report(DIFN[EN.subject.map(lambda s: True).to_numpy() & E.loc[E.subject.isin(noise_subjects), \"included\"].to_numpy()],\n                     \"(a) included electrodes of S07, S08, S13\", 5, ttn).to_string())\nm_inc_n = E.loc[E.subject.isin(noise_subjects), \"included\"].to_numpy()\nprint(f\"pink noise AFTER-BEFORE mean over (a), 0-3 s: {DIFN[m_inc_n][:, ttn >= 0].mean():.3f} z (n = {m_inc_n.sum()})\")\nprint(cluster_report(DIFS[m_inc_n], \"(a) speech triplets, same electrodes\", 5, ttn).to_string())\n\n# %% md\n**Result: supp3a-pink-noise-no-hfb-change.** RESULT_SUPP3A\n\n## MTF of eSTRFs against filter type\n\n> fig8-mtf-matches-filter: the MTFs of the eSTRFs match the filter type of the stimuli they were\n> fit on, in BEFORE, AFTER and in the AFTER minus BEFORE shift.\n\neSTRFs fit apart on temporal-filtered and spectral-filtered triplets (Figure 8 legend), the MTF\nas the amplitude of the 2-D FFT of the mean eSTRF (32 bands x 21 lags), the temporal minus\nspectral MTF difference per included electrode, and MNE's cluster permutation test over the\nmodulation plane (the half plane of non-negative spectral modulation; the amplitude spectrum of a\nreal eSTRF is symmetric). The criterion's region test: a positive cluster (temporal-filter MTF\nhigher) must lie at low temporal and high spectral modulation, a negative one at high temporal\nand low spectral modulation; \"low\" and \"high\" are taken here as below and above the median of\nthe plane's absolute modulations, measured at the cluster's centre (mean over its bins).\n\n# %% tags=claim:fig8-mtf-matches-filter\ninc = E.included.to_numpy()\ndef strf_of(s, key, ch):\n    return FITS[(s, key)][\"mean\"][:, ch]\ntm = np.fft.fftshift(np.fft.fftfreq(ac4.MAX_LAG + 1, 1 / ac4.FS_OUT))      # Hz\nsm = np.fft.fftshift(np.fft.fftfreq(ac4.N_BANDS, 1.0))                     # cycles per band\nhalf = sm >= 0\ndef mtf_diffs(kind):\n    out = []\n    for s in D:\n        chs = np.where(E.loc[E.subject.eq(s), \"included\"].to_numpy())[0]\n        for c in chs:\n            if kind in (\"bef\", \"aft\"):\n                mt = ac4.mtf(strf_of(s, f\"{kind}_temp\", c)); ms = ac4.mtf(strf_of(s, f\"{kind}_freq\", c))\n            elif kind == \"shift_a\":    # MTF of the AFTER minus BEFORE eSTRF\n                mt = ac4.mtf(strf_of(s, \"aft_temp\", c) - strf_of(s, \"bef_temp\", c))\n                ms = ac4.mtf(strf_of(s, \"aft_freq\", c) - strf_of(s, \"bef_freq\", c))\n            else:                      # difference of MTFs\n                mt = ac4.mtf(strf_of(s, \"aft_temp\", c)) - ac4.mtf(strf_of(s, \"bef_temp\", c))\n                ms = ac4.mtf(strf_of(s, \"aft_freq\", c)) - ac4.mtf(strf_of(s, \"bef_freq\", c))\n            out.append((mt - ms)[half])\n    return np.array(out)\nTMg, SMg = np.meshgrid(np.abs(tm), sm[half])\nmed_t, med_s = np.median(TMg), np.median(SMg)\nrows = []\nfor kind in [\"bef\", \"aft\", \"shift_a\", \"shift_b\"]:\n    X = mtf_diffs(kind)\n    T, clusters, pv, _ = mne.stats.permutation_cluster_1samp_test(X, n_permutations=10000, tail=0, seed=8, out_type=\"mask\")\n    for c, p in zip(clusters, pv):\n        sign = \"+\" if T[c].mean() > 0 else \"-\"\n        ct, cs = TMg[c].mean(), SMg[c].mean()\n        match = (sign == \"+\" and ct < med_t and cs > med_s) or (sign == \"-\" and ct > med_t and cs < med_s)\n        rows.append(dict(kind=kind, n=len(X), p=p, sign=sign, bins=int(c.sum()), centre_temporal_Hz=ct,\n                         centre_spectral_cyc_per_band=cs, in_filter_region=match))\n    if not len(clusters):\n        rows.append(dict(kind=kind, n=len(X), p=np.nan, sign=\"none\"))\nR8 = pd.DataFrame(rows)\nprint(f\"median |temporal modulation| {med_t:.2f} Hz, median spectral modulation {med_s:.3f} cycles/band\")\nprint(R8.sort_values([\"kind\", \"p\"]).to_string())\n\n# %% md\n**Result: fig8-mtf-matches-filter.** RESULT_FIG8\n\n## eSTRF output power to unfiltered speech\n\n> fig9-rms-increase: Filtered speech eSTRFs from AFTER give larger predicted responses to\n> unfiltered speech than those from BEFORE (mean RMS increase 0.12 plus/minus 0.03, P = 0.0001,\n> n = 41).\n\nMethods, eSTRF unfiltered speech output power analysis: each eSTRF standardized to zero mean and\nunit s.d., the subject's MIDDLE spectrograms (z-scored as model inputs) passed through the BEFORE\nand the AFTER eSTRF, and the RMS of the output compared. Readings: the eSTRF as (a) mean\ncoefficients over splits or (b) their z-score over splits; the RMS (a) over all MIDDLE sounds\nconcatenated or (b) per sound then averaged.\n\n# %% tags=claim:fig9-rms-increase\nrng = np.random.default_rng(909)\nrows = []\nfor strf_kind in [\"mean\", \"z\"]:\n    for rms_kind in [\"concat\", \"per_sound\"]:\n        diffs = []\n        for s, d in D.items():\n            chs = np.where(E.loc[E.subject.eq(s), \"included\"].to_numpy())[0]\n            if not len(chs):\n                continue\n            Xs, _ = ac4.trial_design(d, cond_idx(d[\"trials\"], \"mid\"))\n            Xa = np.concatenate(Xs)\n            mu, sd = Xa.mean(0), Xa.std(0)\n            for c in chs:\n                v = {}\n                for ph in [\"bef\", \"aft\"]:\n                    w = FITS[(s, ph)][strf_kind][:, c]\n                    w = (w - w.mean()) / w.std()\n                    if rms_kind == \"concat\":\n                        v[ph] = np.sqrt(np.mean((((Xa - mu) / sd) @ w) ** 2))\n                    else:\n                        v[ph] = np.mean([np.sqrt(np.mean((((X - mu) / sd) @ w) ** 2)) for X in Xs])\n                diffs.append(v[\"aft\"] - v[\"bef\"])\n        diffs = np.array(diffs)\n        obs, p = ac4.signflip_test(diffs, rng)\n        rows.append(dict(strf=strf_kind, rms=rms_kind, n=len(diffs), mean_increase=obs,\n                         se=diffs.std(ddof=1) / np.sqrt(len(diffs)), sd=diffs.std(ddof=1), p=p,\n                         within_tol=abs(obs - 0.12) <= 0.03, frac_positive=(diffs > 0).mean()))\nR9a = pd.DataFrame(rows)\nprint(R9a.to_string())\n\n# %% md\n**Result: fig9-rms-increase.** RESULT_FIG9A\n\n## MIDDLE eSTRFs predict AFTER better than BEFORE\n\n> fig9-middle-generalizes-after: eSTRFs fit on unfiltered speech predict HFB activity better in\n> AFTER than in BEFORE (mean R2 improvement 0.05 plus/minus 0.01, P = 0.0001, n = 41).\n\nMethods, MIDDLE condition coefficients generalization: the MIDDLE eSTRF (mean coefficients)\nconvolved with the BEFORE and AFTER spectrograms, and R2 against the HFB. Spectrograms and HFB of\neach condition are z-scored by that condition's own statistics (Methods: inputs and outputs\nz-scored). R2 (a) per trial then averaged, (b) over all trials concatenated.\n\n# %% tags=claim:fig9-middle-generalizes-after\nrng = np.random.default_rng(910)\nrows = []\nfor r2_kind in [\"per_trial\", \"concat\"]:\n    diffs, vals = [], []\n    for s, d in D.items():\n        chs = np.where(E.loc[E.subject.eq(s), \"included\"].to_numpy())[0]\n        if not len(chs):\n            continue\n        W = FITS[(s, \"mid\")][\"mean\"][:, chs]\n        r = {}\n        for ph in [\"bef\", \"aft\"]:\n            Xs, ys = ac4.trial_design(d, cond_idx(d[\"trials\"], ph))\n            Xa, ya = np.concatenate(Xs), np.concatenate(ys)[:, chs]\n            mu, sd, my, sy = Xa.mean(0), Xa.std(0), ya.mean(0), ya.std(0)\n            if r2_kind == \"concat\":\n                pred = ((Xa - mu) / sd) @ W\n                yz = (ya - my) / sy\n                r[ph] = 1 - ((yz - pred) ** 2).sum(0) / ((yz - yz.mean(0)) ** 2).sum(0)\n            else:\n                rr = []\n                for X, y in zip(Xs, ys):\n                    pred = ((X - mu) / sd) @ W\n                    yz = (y[:, chs] - my) / sy\n                    rr.append(1 - ((yz - pred) ** 2).sum(0) / ((yz - yz.mean(0)) ** 2).sum(0))\n                r[ph] = np.mean(rr, 0)\n        diffs.append(r[\"aft\"] - r[\"bef\"]); vals.append(np.column_stack([r[\"bef\"], r[\"aft\"]]))\n    diffs = np.concatenate(diffs); vals = np.concatenate(vals)\n    obs, p = ac4.signflip_test(diffs, rng)\n    rows.append(dict(r2=r2_kind, n=len(diffs), r2_before=vals[:, 0].mean(), r2_after=vals[:, 1].mean(),\n                     mean_improvement=obs, se=diffs.std(ddof=1) / np.sqrt(len(diffs)), sd=diffs.std(ddof=1),\n                     p=p, within_tol=abs(obs - 0.05) <= 0.01, frac_positive=(diffs > 0).mean()))\nR9b = pd.DataFrame(rows)\nprint(R9b.to_string())\n\n# %% md\n**Result: fig9-middle-generalizes-after.** RESULT_FIG9B\n\n## Partial correlation of eSTRFs\n\n> fig10-partial-correlation: Partial correlations of eSTRFs between AFTER and MIDDLE (controlling\n> for BEFORE) exceed those between BEFORE and MIDDLE (controlling for AFTER), a mean improvement\n> of 0.18 (P = 0.001, n = 41).\n\nMethods, eSTRF linear overlap partial correlation analysis: each eSTRF as the z-score of each\ncoefficient across CV splits; sim(aft, mid) = pcorr(after, middle | before), sim(bef, mid) =\npcorr(before, middle | after); sign-flip test of the difference. Regression without (a) and with\n(b) an intercept.\n\n# %% tags=claim:fig10-partial-correlation\nrng = np.random.default_rng(1010)\ndef pcorr_table(keys=(\"bef\", \"mid\", \"aft\"), mask_col=\"included\", subjects=None):\n    rows = []\n    for s in (subjects or list(D)):\n        chs = np.where(E.loc[E.subject.eq(s), mask_col].to_numpy())[0]\n        for c in chs:\n            b, m, a = (FITS[(s, k)][\"z\"][:, c] for k in keys)\n            row = dict(subject=s, ch=c)\n            for icpt in [False, True]:\n                tag = \"b\" if icpt else \"a\"\n                row[f\"aft_mid_{tag}\"] = ac4.partial_corr(a, m, b, icpt)\n                row[f\"bef_mid_{tag}\"] = ac4.partial_corr(b, m, a, icpt)\n                row[f\"diff_{tag}\"] = row[f\"aft_mid_{tag}\"] - row[f\"bef_mid_{tag}\"]\n            rows.append(row)\n    return pd.DataFrame(rows)\nPC = pcorr_table()\nrows = []\nfor tag in [\"a\", \"b\"]:\n    obs, p = ac4.signflip_test(PC[f\"diff_{tag}\"], rng)\n    rows.append(dict(intercept=tag, n=len(PC), bef_mid=PC[f\"bef_mid_{tag}\"].mean(), aft_mid=PC[f\"aft_mid_{tag}\"].mean(),\n                     mean_diff=obs, median_diff=PC[f\"diff_{tag}\"].median(), se=PC[f\"diff_{tag}\"].std(ddof=1) / np.sqrt(len(PC)),\n                     p=p, within_tol=abs(obs - 0.18) <= 0.018, frac_positive=(PC[f\"diff_{tag}\"] > 0).mean()))\nR10 = pd.DataFrame(rows)\nprint(R10.to_string())\nprint(PC.groupby(\"subject\")[[\"diff_a\"]].agg([\"count\", \"mean\"]))\nprint(\"temporal-lobe electrodes only (Figure 10c legend):\")\nPCt = PC.merge(E.reset_index()[[\"subject\", \"region\"]].assign(ch=E.groupby(\"subject\").cumcount().to_numpy()), on=[\"subject\", \"ch\"])\nobs, p = ac4.signflip_test(PCt.loc[PCt.region.eq(\"temporal\"), \"diff_a\"], rng)\nprint(f\"  n = {PCt.region.eq('temporal').sum()}, mean difference {obs:.3f}, P = {p:.4f}\")\n\n# %% md\n**Result: fig10-partial-correlation.** RESULT_FIG10\n\n> fig10b-similarity-correlates: the increase in eSTRF similarity correlates with the electrode's\n> evoked HFB amplitude or model score (Pearson r = 0.42, P = 0.007).\n\n# %% tags=claim:fig10b-similarity-correlates\nEinc = E[E.included].copy()\nEinc[\"ch\"] = E.groupby(\"subject\").cumcount()[E.included].to_numpy()\nEinc[\"evoked\"] = [POST[(s, MAIN[0], MAIN[1])][speech(D[s][\"trials\"]).to_numpy() & (D[s][\"trials\"].trial_phase == \"mid\").to_numpy()][:, c].mean()\n                  for s, c in zip(Einc.subject, Einc.ch)]\nM = PC.merge(Einc[[\"subject\", \"ch\", \"evoked\", \"mid_r2\", \"description\"]], on=[\"subject\", \"ch\"])\nfor x in [\"evoked\", \"mid_r2\"]:\n    for tag in [\"a\", \"b\"]:\n        r, p = stats.pearsonr(M[x], M[f\"diff_{tag}\"])\n        print(f\"({'a' if x == 'evoked' else 'b'}) {x} vs partial correlation difference (intercept {tag}): r = {r:.3f}, P = {p:.4f}, n = {len(M)}, within 0.42 +/- 0.042: {abs(r - 0.42) <= 0.042}\")\nprint(f\"evoked range {M.evoked.min():.2f} to {M.evoked.max():.2f} z; mid_r2 range {M.mid_r2.min():.3f} to {M.mid_r2.max():.3f}\")\n\n# %% md\n**Result: fig10b-similarity-correlates.** RESULT_FIG10B\n\n> fig10c-stg-location: Most of the increase in partial correlation lies around the superior\n> temporal gyrus.\n\nSTG electrodes are those labelled `temporal-superior` in `channels.tsv`.\n\n# %% tags=claim:fig10c-stg-location\nM[\"stg\"] = M.description.eq(\"temporal-superior\")\npos = M[M.diff_a > 0]\nprint(\"included electrodes by label:\", M.description.value_counts().to_dict())\nprint(f\"(a) share of the summed positive differences on STG: {pos.loc[pos.stg, 'diff_a'].sum() / pos.diff_a.sum():.3f} ({pos.loc[pos.stg, 'diff_a'].sum():.2f} of {pos.diff_a.sum():.2f})\")\nprint(f\"(b) share of electrodes with a positive difference on STG: {pos.stg.mean():.3f} ({int(pos.stg.sum())} of {len(pos)})\")\nprint(f\"reference: share of included electrodes on STG {M.stg.mean():.3f} ({int(M.stg.sum())} of {len(M)})\")\n\n# %% md\n**Result: fig10c-stg-location.** RESULT_FIG10C\n\n> supp3b-pink-noise-no-pcorr-change: In pink noise trials the partial correlations of\n> BEFORE/MIDDLE and AFTER/MIDDLE eSTRFs do not differ (permutation test, n = 12).\n\neSTRFs fit on the pink noise triplets (the MIDDLE eSTRF on the pink noise), with the same ridge\nparameter, for the included electrodes of S07, S08 and S13.\n\n# %% tags=claim:supp3b-pink-noise-no-pcorr-change\nrng = np.random.default_rng(303)\nPCn = pcorr_table(keys=(\"noise_bef\", \"noise_mid\", \"noise_aft\"), subjects=noise_subjects)\nfor tag in [\"a\", \"b\"]:\n    obs, p = ac4.signflip_test(PCn[f\"diff_{tag}\"], rng)\n    print(f\"intercept {tag}: n = {len(PCn)}, mean AFTER/MIDDLE {PCn[f'aft_mid_{tag}'].mean():.3f}, BEFORE/MIDDLE {PCn[f'bef_mid_{tag}'].mean():.3f}, difference {obs:.3f}, P = {p:.4f}\")\nprint(PCn.groupby(\"subject\").size().to_string())\nprint(f\"MIDDLE pink noise model R2, median over these electrodes: {np.median([FITS[(s, 'noise_mid')]['r2'].mean(0)[c] for s, c in zip(PCn.subject, PCn.ch)]):.3f}\")\n\n# %% md\n**Result: supp3b-pink-noise-no-pcorr-change.** RESULT_SUPP3B\n\n## Connectivity\n\n> supp6a-connectivity-increase: HFB amplitude coherence between eSTRF seed electrodes and frontal\n> and temporal target electrodes rises slightly in AFTER against BEFORE (temporal-frontal p =\n> 0.025, temporal-temporal p = 0.043, n = 39).\n\nSupplementary Methods, Inter- and Intra-regional Coherence Analysis: seeds are the included\nelectrodes on the temporal lobe; targets all other temporal electrodes, or the frontal/premotor\nelectrodes (`frontal-*`, `premotor-*` labels); per trial the multitaper coherence of the HFB\namplitude (\"similar to that described above\": the 400 ms windows of Figure 4, here the\npost-stimulus windows 0 to 2.5 s), averaged over targets, then over trials, integrated over\nfrequency in bits/s, AFTER minus BEFORE per seed, and MNE's permutation t-test across seeds.\n\n# %% tags=claim:supp6a-connectivity-increase\ndef seed_coherence(target_region):\n    rows = []\n    for s, d in D.items():\n        g = E[E.subject.eq(s)].reset_index(drop=True)\n        seeds = np.where((g.included & g.region.eq(\"temporal\")).to_numpy())[0]\n        if target_region == \"frontal\":\n            targ_all = np.where(g.description.str.startswith((\"frontal\", \"premotor\")).to_numpy())[0]\n        else:\n            targ_all = np.where(g.region.eq(\"temporal\").to_numpy())[0]\n        ep, times = EP[s]\n        zep = ac4.zscore_epochs(d, ep, times, MAIN[0])\n        tr = d[\"trials\"]\n        for c in seeds:\n            targ = targ_all[targ_all != c]\n            if not len(targ):\n                continue\n            row = dict(subject=s, seed=c, n_targets=len(targ))\n            for ph in [\"bef\", \"mid\", \"aft\"]:\n                X = zep[cond_idx(tr, ph)]\n                bits = []\n                for ws in WIN_STARTS[WIN_STARTS >= 0]:\n                    sel = (times >= ws - 1e-9) & (times < ws + 0.4 - 1e-9)\n                    f, coh = ac4.mt_coherence(X[:, [c]][..., sel], X[:, targ][..., sel], ac4.FS_OUT, nw=2.0)\n                    bits.append(ac4.coh_to_bits(coh.mean(1), f).mean())   # mean over targets, then trials\n                row[ph] = np.mean(bits)\n            rows.append(row)\n    return pd.DataFrame(rows)\nCOH6 = {}\nfor reg in [\"frontal\", \"temporal\"]:\n    t = seed_coherence(reg)\n    COH6[reg] = t\n    diff = (t.aft - t.bef).to_numpy()\n    T, p, _ = mne.stats.permutation_t_test(diff[:, None], n_permutations=10000, seed=6, tail=0)\n    print(f\"temporal seeds to {reg} targets: seeds {len(t)} (subjects {t.subject.nunique()}), BEFORE {t.bef.mean():.3f}, MIDDLE {t.mid.mean():.3f}, AFTER {t.aft.mean():.3f} bits/s; AFTER-BEFORE mean {diff.mean():.4f}, t = {T[0]:.2f}, P = {p[0]:.4f}\")\nincluded_temporal = int((E.included & E.region.eq(\"temporal\")).sum())\nprint(\"included temporal seeds:\", included_temporal, \"; seeds with frontal targets:\", len(COH6[\"frontal\"]))\n\n# %% md\n**Result: supp6a-connectivity-increase.** RESULT_SUPP6A\n\n> supp6a-after-closer-to-middle: the seed to target coherence in AFTER is closer than in BEFORE to\n> that obtained with unfiltered speech. Measure (criterion): the mean over seeds of |AFTER minus\n> MIDDLE| against that of |BEFORE minus MIDDLE|.\n\n# %% tags=claim:supp6a-after-closer-to-middle\nfor reg, t in COH6.items():\n    da, db = (t.aft - t.mid).abs().mean(), (t.bef - t.mid).abs().mean()\n    print(f\"{reg} targets: mean |AFTER-MIDDLE| {da:.4f}, mean |BEFORE-MIDDLE| {db:.4f}, AFTER closer: {da < db}; means BEFORE {t.bef.mean():.3f}, MIDDLE {t.mid.mean():.3f}, AFTER {t.aft.mean():.3f}\")\n\n# %% md\n**Result: supp6a-after-closer-to-middle.** RESULT_SUPP6A2\n\n> supp6b-no-pac-change: Phase-amplitude coupling between 3 to 8 Hz phase in frontal/premotor\n> electrodes and HFB amplitude in the eSTRF electrodes does not change from BEFORE to AFTER.\n\nSupplementary Methods, Theta Connectivity Phase-Amplitude Coupling Analysis: phase from 3 to 10\nHz in 0.5 Hz steps (band-pass of +/- 1 Hz around each, a standard choice) on the frontal/premotor\nelectrodes, HFB amplitude from 10 log-spaced bands 70 to 140 Hz on the included electrodes, the\npost-stimulus samples (onset to sound end) concatenated over trials per condition, PAC as in\nOzkurt and Schnitzler (2011), averaged over phases 3 to 8 Hz (variants 4 to 8 and 2 to 12 Hz,\nthe legend's), then over phase electrodes; AFTER minus BEFORE; permutation t-test against 0.\n\n# %% tags=claim:supp6b-no-pac-change\nPH_F = np.arange(2.0, 12.01, 0.5)\ndef ozkurt(amp, ph):\n    n = amp.shape[-1]\n    return np.abs((amp * np.exp(1j * ph)).sum(-1)) / (np.sqrt(n) * np.sqrt((amp ** 2).sum(-1)))\nrows = []\nfor s, d in D.items():\n    g = E[E.subject.eq(s)].reset_index(drop=True)\n    amp_ch = np.where(g.included.to_numpy())[0]\n    ph_ch = np.where(g.description.str.startswith((\"frontal\", \"premotor\")).to_numpy())[0]\n    if not len(amp_ch) or not len(ph_ch):\n        continue\n    tr = d[\"trials\"]\n    t_ep = np.arange(int(ac4.EPOCH[0] * ac4.FS), int(ac4.EPOCH[1] * ac4.FS)) / ac4.FS\n    res = {}\n    for ph in [\"bef\", \"aft\"]:\n        idx = cond_idx(tr, ph)\n        raw = d[\"raw_ep\"][idx].astype(np.float64)\n        amp = ac4.hfb_amplitude(raw[:, amp_ch], np.geomspace(70, 140, 10))\n        phases = np.stack([ac4.band_phase(raw[:, ph_ch], f - 1, f + 1) for f in PH_F])  # (freq, trials, ch, t)\n        masks = [(t_ep >= 0) & (t_ep < dur) for dur in tr.duration.to_numpy()[idx]]\n        A = np.concatenate([amp[i][:, m] for i, m in enumerate(masks)], axis=-1)          # (amp_ch, samples)\n        P = np.concatenate([phases[:, i][..., m] for i, m in enumerate(masks)], axis=-1)  # (freq, ph_ch, samples)\n        res[ph] = ozkurt(A[None, None], P[:, :, None])                                    # (freq, ph_ch, amp_ch)\n    for j, c in enumerate(amp_ch):\n        row = dict(subject=s, ch=c, n_phase_ch=len(ph_ch))\n        for lab, lo, hi in [(\"3-8\", 3, 8), (\"4-8\", 4, 8), (\"2-12\", 2, 12)]:\n            fm = (PH_F >= lo) & (PH_F <= hi)\n            row[f\"bef_{lab}\"] = res[\"bef\"][fm][:, :, j].mean()\n            row[f\"aft_{lab}\"] = res[\"aft\"][fm][:, :, j].mean()\n        rows.append(row)\nPAC = pd.DataFrame(rows)\nfor lab in [\"3-8\", \"4-8\", \"2-12\"]:\n    diff = (PAC[f\"aft_{lab}\"] - PAC[f\"bef_{lab}\"]).to_numpy()\n    T, p, _ = mne.stats.permutation_t_test(diff[:, None], n_permutations=10000, seed=7, tail=0)\n    print(f\"phase {lab} Hz: n = {len(diff)} amplitude electrodes ({PAC.subject.nunique()} subjects), BEFORE {PAC[f'bef_{lab}'].mean():.4f}, AFTER {PAC[f'aft_{lab}'].mean():.4f}, AFTER-BEFORE {diff.mean():.5f}, t = {T[0]:.2f}, P = {p[0]:.4f}\")\n\n# %% md\n**Result: supp6b-no-pac-change.** RESULT_SUPP6B\n\n## Coherence with the speech envelope\n\n> supp7-envelope-coherence: In temporal electrodes, theta coherence with the speech envelope is\n> higher for unfiltered speech than for BEFORE (p = 0.001, n = 72), but does not differ between\n> BEFORE and AFTER; frontal electrodes show no effects.\n\nSupplementary Methods and Supplementary Figure 7: the speech envelope from 64 log-spaced\nwavelets 500 to 2000 Hz, rectified and averaged; multitaper coherence of the re-referenced ECoG\nwith the envelope over 0 to 3 s per trial (both resampled to 100 Hz; NW = 3, five tapers,\njackknife, a standard choice), converted to normal mutual information per frequency\n(-log2(1 - coh)), averaged over trials; the MIDDLE minus BEFORE and AFTER minus BEFORE differences\nper frequency, and MNE's cluster permutation test over frequency (1 to 30 Hz) across the Speech-R\nelectrodes of the temporal lobe and of frontal/premotor cortex.\n\n# %% tags=claim:supp7-envelope-coherence\nimport scipy.signal as ss\nNMI = []\nfor s, d in D.items():\n    tr = d[\"trials\"]\n    t_ep = np.arange(int(ac4.EPOCH[0] * ac4.FS), int(ac4.EPOCH[1] * ac4.FS)) / ac4.FS\n    sel = (t_ep >= 0) & (t_ep < 3.0)\n    out = {}\n    for ph in [\"bef\", \"mid\", \"aft\"]:\n        idx = cond_idx(tr, ph)\n        x = ss.resample_poly(d[\"raw_ep\"][idx][..., sel].astype(np.float64), 1, 10, axis=-1)       # (trials, ch, 300)\n        env = np.stack([ss.resample_poly(d[\"env\"][i][:3000], 1, 10) for i in idx])                # (trials, 300)\n        f, coh = ac4.mt_coherence(x, np.broadcast_to(env[:, None], x.shape), 100.0, nw=3.0)\n        out[ph] = (-np.log2(1 - np.clip(coh, 0, 1 - 1e-9))).mean(0)                                # (ch, freqs)\n    NMI.append(out)\nNMI = {ph: np.concatenate([o[ph] for o in NMI]) for ph in [\"bef\", \"mid\", \"aft\"]}\nfsel = (f >= 1) & (f <= 30)\nprint(\"frequencies tested:\", f[fsel])\nrows = []\ngroups = {\"temporal\": (E.speech_r & E.region.eq(\"temporal\")).to_numpy(),\n          \"frontal\": (E.speech_r & E.description.str.startswith((\"frontal\", \"premotor\"))).to_numpy()}\nfor gname, m in groups.items():\n    for comp in [\"mid\", \"aft\"]:\n        X = (NMI[comp] - NMI[\"bef\"])[m][:, fsel]\n        if len(X) < 3:\n            rows.append(dict(electrodes=gname, comparison=f\"{comp}-bef\", n=len(X), p=np.nan, sign=\"too few\"))\n            continue\n        T, clusters, pv, _ = mne.stats.permutation_cluster_1samp_test(X, n_permutations=10000, tail=0, seed=77, out_type=\"mask\")\n        if not len(clusters):\n            rows.append(dict(electrodes=gname, comparison=f\"{comp}-bef\", n=len(X), p=np.nan, sign=\"no cluster\"))\n        for c, p in zip(clusters, pv):\n            fc = f[fsel][c]\n            rows.append(dict(electrodes=gname, comparison=f\"{comp}-bef\", n=len(X), p=p, sign=\"+\" if T[c].mean() > 0 else \"-\",\n                             f_lo=fc.min(), f_hi=fc.max(), overlaps_3_8=(fc.min() <= 8) and (fc.max() >= 3),\n                             overlaps_2_12=(fc.min() <= 12) and (fc.max() >= 2)))\nR7 = pd.DataFrame(rows)\nprint(R7.to_string())\nfor gname, m in groups.items():\n    th = (f >= 3) & (f <= 8)\n    print(f\"{gname} Speech-R (n = {m.sum()}): mean NMI 3-8 Hz BEFORE {NMI['bef'][m][:, th].mean():.4f}, MIDDLE {NMI['mid'][m][:, th].mean():.4f}, AFTER {NMI['aft'][m][:, th].mean():.4f} bits\")\n\n# %% md\n**Result: supp7-envelope-coherence.** RESULT_SUPP7\n\n## HFB power by wavelets\n\n> supp4-hfb-power-increase: Power in the HFB range rises in AFTER against BEFORE in frontal (p =\n> 0.001, n = 75) and temporal (p = 0.002, n = 217) electrodes, and power below 25 Hz falls in\n> frontal electrodes (p = 0.001).\n\nSupplementary Figure 4 legend: 100 log-spaced Morlet wavelets of 5 cycles, post-stimulus power\naveraged over time, AFTER minus BEFORE, cluster permutation test over frequency across frontal\nand across temporal electrodes. The claims file's standard choice is 1 to 200 Hz with power in\ndecibels against the -800 to -100 ms baseline; the kept epochs (-1 to 3.5 s) are too short for\na 5-cycle wavelet below about 3 Hz, so the range here is 3 to 200 Hz. Post-stimulus is 0 to 2.5\ns (claims, open detail 2, reading b). Frontal electrodes are the `frontal-*` and `premotor-*`\nlabels, temporal the temporal lobe labels; all good electrodes.\n\n# %% tags=claim:supp4-hfb-power-increase\nWF = np.geomspace(3, 200, 100)\nPOW = []\nfor s, d in D.items():\n    tr = d[\"trials\"]\n    t_ep = np.arange(int(ac4.EPOCH[0] * ac4.FS), int(ac4.EPOCH[1] * ac4.FS)) / ac4.FS\n    td = t_ep[::10]\n    base = (td >= -0.8) & (td <= -0.1)\n    post = (td >= 0) & (td <= 2.5)\n    out = {}\n    for ph in [\"bef\", \"aft\"]:\n        x = d[\"raw_ep\"][cond_idx(tr, ph)].astype(np.float64)\n        acc = []\n        for fchunk in np.array_split(WF, 10):\n            p = mne.time_frequency.tfr_array_morlet(x, ac4.FS, fchunk, n_cycles=5, output=\"power\", decim=10)\n            acc.append(10 * np.log10(p[..., post].mean(-1) / p[..., base].mean(-1)).mean(0))     # (ch, f)\n        out[ph] = np.concatenate(acc, axis=1)\n    POW.append(out[\"aft\"] - out[\"bef\"])\nPOW = np.concatenate(POW)\nrows = []\nfor gname, m in [(\"frontal\", E.description.str.startswith((\"frontal\", \"premotor\")).to_numpy()), (\"temporal\", E.region.eq(\"temporal\").to_numpy())]:\n    T, clusters, pv, _ = mne.stats.permutation_cluster_1samp_test(POW[m], n_permutations=10000, tail=0, seed=44, out_type=\"mask\")\n    for c, p in zip(clusters, pv):\n        rows.append(dict(electrodes=gname, n=int(m.sum()), p=p, sign=\"+\" if T[c].mean() > 0 else \"-\", f_lo=WF[c].min(), f_hi=WF[c].max(),\n                         hfb_overlap=(WF[c].max() >= 70) and (WF[c].min() <= 150), below_25=WF[c].min() < 25))\n    hf = (WF >= 70) & (WF <= 150)\n    print(f\"{gname}: n = {m.sum()}, mean AFTER-BEFORE 70-150 Hz {POW[m][:, hf].mean():.3f} dB, below 25 Hz {POW[m][:, WF < 25].mean():.3f} dB\")\nR4 = pd.DataFrame(rows)\nprint(R4.to_string())\n\n# %% md\n**Result: supp4-hfb-power-increase.** RESULT_SUPP4\n\n## Summary\n\nSUMMARY\n"
}
```

```
File created successfully at: /tmp/claude/nb_src.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
echo $TMPDIR; cd entries/crcns-ac-4-holdgraf-2016 && python - <<'EOF'
s=open('ac4.py').read()
old=s[s.index("    n = vals.shape[0]\n    idx = rng.integers"):s.index("    return np.percentile(means, q, axis=0)")]
s=s.replace(old,"""    n = vals.shape[0]
    counts = rng.multinomial(n, np.full(n, 1 / n), size=n_boot)   # resampling with replacement
    means = counts @ vals / n                                     # (n_boot, channels)
""")
open('ac4.py','w').write(s)
EOF
cat > $TMPDIR/build.py <<'EOF'
import sys, re, nbformat
src = open(sys.argv[1]).read()
parts = re.split(r'^# %%(.*)$', src, flags=re.M)
cells = []
for hdr, body in zip(parts[1::2], parts[2::2]):
    body = body.strip('\n')
    hdr = hdr.strip()
    if hdr.startswith('md'):
        c = nbformat.v4.new_markdown_cell(body)
    else:
        c = nbformat.v4.new_code_cell(body)
        m = re.search(r'tags=(\S+)', hdr)
        if m: c.metadata['tags'] = m.group(1).split(',')
    cells.append(c)
nb = nbformat.v4.new_notebook(cells=cells)
nb.metadata['kernelspec'] = {'name': 'python3', 'display_name': 'Python 3', 'language': 'python'}
nbformat.write(nb, sys.argv[2])
EOF
cat > $TMPDIR/devrun.py <<'EOF'
import sys, re, time, os
import matplotlib; matplotlib.use('Agg')
src = open(sys.argv[1]).read()
upto = sys.argv[2] if len(sys.argv) > 2 else None
parts = re.split(r'^# %%(.*)$', src, flags=re.M)
ns = {}
for hdr, body in zip(parts[1::2], parts[2::2]):
    if hdr.strip().startswith('md'): continue
    if body.lstrip().startswith('# LOAD'):
        body = "import pickle\nD={s:pickle.load(open(os.environ['TMPDIR']+'/'+s+'.pkl','rb')) for s in ac4.SUBJECTS}\n"
    t = time.time()
    print('=====', hdr.strip(), flush=True)
    exec(compile(body, 'cell', 'exec'), ns)
    print(f'[{time.time()-t:.0f} s]', flush=True)
    if upto and upto in hdr: break
import pickle
EOF
echo ok
```

```
/tmp/claude-1001
ok
```

**Agent calls Bash**

```bash
cd entries/crcns-ac-4-holdgraf-2016; . $TMPDIR/dev/bin/activate; date -u; python $TMPDIR/devrun.py /tmp/claude/nb_src.py claim:fig4b 2>&1 | grep -v Warning | cut -c1-250
```

```
Mon Nov  9 08:17:11 UTC 2026
===== 
Traceback (most recent call last):
  File "/tmp/claude-1001/devrun.py", line 13, in <module>
    exec(compile(body, 'cell', 'exec'), ns)
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "cell", line 12, in <module>
ModuleNotFoundError: No module named 'ac4'
```

**Agent calls Bash**

```bash
cd entries/crcns-ac-4-holdgraf-2016; . $TMPDIR/dev/bin/activate; PYTHONPATH=. python $TMPDIR/devrun.py /tmp/claude/nb_src.py claim:fig4b 2>&1 | grep -v Warning | cut -c1-250
```

```
===== 
crcns:ac-4/unversioned doi:10.6080/K08S4N4J
a3f4fc4396018c4336289aeae07f3a24  data.zip
e5fada4a35959c02599388fa667f9629  docs/crcns_ac-4_data_description.docx
5967170cec24533198d9a116e0ac34bf  docs/crcns_ac-4_data_description.pdf
03c6756f455486e0cc0169a76f48df3e  filelist.txt

[1 s]
===== 
[0 s]
===== tags=sanity
  subject  channels  good      fs  duration_json  duration_samples  audio_sr      audio_s  triplets  noise_triplets  lone_unfiltered    sound_s  bad_spans  sounds_overlapping_bad  raw_abs_median  car_residual
0     S01        64    61  1000.0       1204.041          1204.042     16000  1204.042000        56               0                6  1.52-3.39          9                       7    3.151261e+02  1.910911e-08
1     S02        64    59  1000.0        815.000           815.001     16000   815.001062        47               0                6  1.79-4.08          0                       0    2.103745e+08  1.894045e-08
2     S03        64    52  1000.0        780.166           780.167     16000   780.622125        39               0                6  1.53-3.21         12                      10    6.244610e+08  1.234181e-08
3     S04        48    40  1000.0        660.211           660.212     16000   660.249312        32               0                6  1.92-4.05          6                       4    2.057520e+08  1.601341e-08
4     S07        60    60  1000.0        988.913           988.914     16000  1015.170687        57              28                0  1.45-3.21          1                       1    2.722568e+08  1.580337e-08
5     S08        52    52  1000.0        942.243           942.244     16000   943.364375        57              28                0  1.60-3.52          0                       0    3.703386e+08  1.196917e-08
6     S13        64    53  1000.0        982.011           982.012     20000   983.183100        57              28                0  1.52-3.24          0                       0    1.747290e+08  1.891248e-08
total 
[... 107 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/claude && python - <<'EOF'
s=open('nb_src.py').read()
s=s.replace('''def cluster_report(X, label, seed, times=None, n_perm=10000):
    T, clusters, pv, _ = mne.stats.permutation_cluster_1samp_test(X, n_permutations=n_perm, tail=0, seed=seed, out_type="mask")''','''def as_mask(cl, shape):
    m = np.zeros(shape, bool)
    m[cl] = True
    return m

def clusters_of(X, seed, n_perm=10000):
    """MNE's one-sample cluster permutation test (default threshold, two-tailed); masks."""
    T, clusters, pv, _ = mne.stats.permutation_cluster_1samp_test(X, n_permutations=n_perm, tail=0, seed=seed, out_type="mask")
    return T, [as_mask(c, X.shape[1:]) for c in clusters], pv

def cluster_report(X, label, seed, times=None, n_perm=10000):
    T, clusters, pv = clusters_of(X, seed, n_perm)''')
s=s.replace('''    T, clusters, pv, _ = mne.stats.permutation_cluster_1samp_test(X, n_permutations=10000, tail=0, seed=8, out_type="mask")''','''    T, clusters, pv = clusters_of(X, 8)''')
s=s.replace('''        T, clusters, pv, _ = mne.stats.permutation_cluster_1samp_test(X, n_permutations=10000, tail=0, seed=77, out_type="mask")''','''        T, clusters, pv = clusters_of(X, 77)''')
s=s.replace('''    T, clusters, pv, _ = mne.stats.permutation_cluster_1samp_test(POW[m], n_permutations=10000, tail=0, seed=44, out_type="mask")''','''    T, clusters, pv = clusters_of(POW[m], 44)''')
s=s.replace('''        trip = sorted(tr.loc[tsel, "trial_num"].unique())''','''        trip = complete_triplets(tr)''')
s=s.replace('''WIN_STARTS = np.round''','''def complete_triplets(tr):
    """Speech triplets with one BEFORE, one MIDDLE and one AFTER sound."""
    t = tr[speech(tr)]
    g = t.groupby("trial_num").trial_phase.apply(lambda x: sorted(x) == ["aft", "bef", "mid"])
    return sorted(g.index[g])

WIN_STARTS = np.round''')
s=s.replace('''print(cluster_report(DIFN[EN.subject.map(lambda s: True).to_numpy() & E.loc[E.subject.isin(noise_subjects), "included"].to_numpy()],
                     "(a) included electrodes of S07, S08, S13", 5, ttn).to_string())
m_inc_n = E.loc[E.subject.isin(noise_subjects), "included"].to_numpy()''','''m_inc_n = E.loc[E.subject.isin(noise_subjects), "included"].to_numpy()
print(cluster_report(DIFN[m_inc_n], "(a) included electrodes of S07, S08, S13", 5, ttn).to_string())''')
open('nb_src.py','w').write(s)
EOF
cd entries/crcns-ac-4-holdgraf-2016; . $TMPDIR/dev/bin/activate; PYTHONPATH=. python $TMPDIR/devrun.py /tmp/claude/nb_src.py claim:fig4b 2>&1 | grep -v Warning | cut -c1-250 | sed -n '/fig3b/,$p'
```

```
===== tags=claim:fig3b-hfb-increase-after
                                  set    n       p sign  start   end  size    zscore
0                    (a) all Speech-R  104  0.0001    +   0.36  1.42    54  nonevent
1                    (a) all Speech-R  104  0.0018    +   1.58  2.02    23  nonevent
2                    (a) all Speech-R  104  0.8405    -  -0.18 -0.18     1  nonevent
3                    (a) all Speech-R  104  0.4038    -  -0.06  0.00     4  nonevent
4                    (a) all Speech-R  104  0.4497    -   2.58  2.64     4  nonevent
5                    (a) all Speech-R  104  0.0108    -   2.74  3.00    14  nonevent
6   (b) Speech-R temporal+perisylvian   86  0.8621    +   0.08  0.08     1  nonevent
7   (b) Speech-R temporal+perisylvian   86  0.0001    +   0.34  1.42    55  nonevent
8   (b) Speech-R temporal+perisylvian   86  0.4411    +   1.58  1.64     4  nonevent
9   (b) Speech-R temporal+perisylvian   86  0.0110    +   1.74  2.00    14  nonevent
10  (b) Speech-R temporal+perisylvian   86  0.8992    +   2.10  2.10     1  nonevent
11  (b) Speech-R temporal+perisylvian   86  0.7618    -  -0.18 -0.16     2  nonevent
12  (b) Speech-R temporal+perisylvian   86  0.6906    -  -0.04 -0.02     2  nonevent
13  (b) Speech-R temporal+perisylvian   86  0.6849    -   2.58  2.62     3  nonevent
14  (b) Speech-R temporal+perisylvian   86  0.1500    -   2.76  2.86     6  nonevent
15  (b) Speech-R temporal+perisylvian   86  0.3915    -   2.92  2.98     4  nonevent
16                   (a) all Speech-R  104  0.8169    +   0.08  0.08     1     trial
17                   (a) all Speech-R  104  0.0001    +   0.28  1.42    58     trial
[... 90 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-ac-4-holdgraf-2016; . $TMPDIR/dev/bin/activate; date -u; PYTHONPATH=. python $TMPDIR/devrun.py /tmp/claude/nb_src.py claim:included 2>&1 | grep -v Warning | cut -c1-250 | sed -n '/fig4b/,$p' | sed -n '/=====/,$p' | tail -n +2 | sed -n '/=====/,$p'
```

```
Mon Nov  9 08:18:11 UTC 2026
===== 
1e+00     230
3e+00      30
1e+01      74
3e+01     151
1e+02     316
3e+02     434
1e+03     713
3e+03    1003
1e+04    1236
3e+04    1343
1e+05    1434
3e+05    1097
1e+06     722
3e+06     308
1e+07     133
3e+07      53
1e+08    2844
mode 1e+08 (grid 1e+00 to 1e+08); 12121 split x electrode values; 20 s
[... 108 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-ac-4-holdgraf-2016; . $TMPDIR/dev/bin/activate; cat > $TMPDIR/t1.py <<'EOF'
exec(open('/tmp/claude-1001/dev_load.py').read())
import numpy as np, pandas as pd
exec(compile(open('/tmp/claude/snip.py').read(),'s','exec'))
EOF
python - <<'EOF'
s=open('/tmp/claude/nb_src.py').read()
# extract helper defs needed
start=s.index('def region(desc)'); end=s.index('rows = []\nfor s, d in D.items():\n    ch, tr, js')
reg=s[start:end]
open('/tmp/claude/snip.py','w').write(reg+'''
import ac4
E = pd.concat([d["good"] for d in D.values()], ignore_index=True)
E["region"]=E.description.map(region)
rng=np.random.default_rng(0)
sr=[]
for s,d in D.items():
    ep,times=ac4.hfb_epochs(d); tr=d["trials"]
    zep=ac4.zscore_epochs(d,ep,times,"nonevent"); pm=ac4.post_mean(zep,times,tr.duration.to_numpy(),"sound")
    sel=((tr.trial_num>=0)&~tr.noise&(tr.trial_phase=="mid")).to_numpy()
    sr.append(ac4.bootstrap_lower(pm[sel],rng)>0)
E["speech_r"]=np.concatenate(sr)
ALPHAS=np.logspace(0,8,17)
R=[]
for s,d in D.items():
    tr=d["trials"]
    idx=np.where(((tr.trial_num>=0)&~tr.noise&(tr.trial_phase=="mid")).to_numpy())[0]
    Xs,ys=ac4.trial_design(d,idx)
    _,r2=ac4.ridge_loto(Xs,ys,ALPHAS)
    R.append(r2)
r2all=np.concatenate(R,axis=2)  # folds differ per subject -> can't concat on axis 0
EOF
EOF
sed -i 's/^r2all=.*$/import pickle; pickle.dump((R,E),open("\/tmp\/claude-1001\/r2mid.pkl","wb"))/' /tmp/claude/snip.py
PYTHONPATH=. python $TMPDIR/t1.py 2>&1 | grep -v Warn | tail -5
python - <<'EOF'
import pickle,numpy as np
R,E=pickle.load(open('/tmp/claude-1001/r2mid.pkl','rb'))
A=np.logspace(0,8,17)
rng=np.random.default_rng(0)
import sys; sys.path.insert(0,'.')
import ac4
best_el=np.concatenate([A[r.mean(0).argmax(0)] for r in R])
sr=E.speech_r.to_numpy()
v,c=np.unique(best_el[sr],return_counts=True); print('per-electrode best alpha over SpeechR', dict(zip(v,c)))
for ai,a in enumerate(A):
    lbA=np.concatenate([ac4.bootstrap_lower(r[:,ai],rng,2000) for r in R])
    lbB=np.concatenate([np.percentile(r[:,ai],1,axis=0) for r in R])
    m=np.concatenate([r[:,ai].mean(0) for r in R])
    print(f"{a:.0e} meanR2>0 {int((m>0).sum())} bootLB>0 {int((lbA>0).sum())} p1>0 {int((lbB>0).sum())}  incl {int(((lbA>0)&sr&E.region.isin(['temporal','perisylvian']).to_numpy()).sum())} max mean {m.max():.3f}")
EOF
```

```
Exit code 1
  File "<stdin>", line 5
    open('/tmp/claude/snip.py','w').write(reg+'''
                                              ^
SyntaxError: unterminated triple-quoted string literal (detected at line 25)
/bin/bash: line 33: EOF: command not found
sed: can't read /tmp/claude/snip.py: No such file or directory
Traceback (most recent call last):
  File "/tmp/claude-1001/t1.py", line 3, in <module>
    exec(compile(open('/tmp/claude/snip.py').read(),'s','exec'))
                 ~~~~^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/claude/snip.py'
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/claude-1001/r2mid.pkl'
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude/t2.py",
 "content": "import pickle, os, sys\nimport numpy as np, pandas as pd\nsys.path.insert(0, '.')\nimport ac4\nD = {s: pickle.load(open(os.environ['TMPDIR'] + '/' + s + '.pkl', 'rb')) for s in ac4.SUBJECTS}\ndef region(desc):\n    if desc.startswith(\"temporal\") or desc == \"sub_temporal\":\n        return \"temporal\"\n    if desc.endswith(\"-inferior\"):\n        return \"perisylvian\"\n    if desc.startswith(\"frontal\") or desc.startswith(\"premotor\"):\n        return \"frontal\"\n    return \"other\"\nE = pd.concat([d[\"good\"] for d in D.values()], ignore_index=True)\nE[\"region\"] = E.description.map(region)\nrng = np.random.default_rng(0)\nsr = []\nfor s, d in D.items():\n    ep, times = ac4.hfb_epochs(d); tr = d[\"trials\"]\n    zep = ac4.zscore_epochs(d, ep, times, \"nonevent\"); pm = ac4.post_mean(zep, times, tr.duration.to_numpy(), \"sound\")\n    sel = ((tr.trial_num >= 0) & ~tr.noise & (tr.trial_phase == \"mid\")).to_numpy()\n    sr.append(ac4.bootstrap_lower(pm[sel], rng) > 0)\nE[\"speech_r\"] = np.concatenate(sr)\nA = np.logspace(0, 8, 17)\nR = []\nfor s, d in D.items():\n    tr = d[\"trials\"]\n    idx = np.where(((tr.trial_num >= 0) & ~tr.noise & (tr.trial_phase == \"mid\")).to_numpy())[0]\n    Xs, ys = ac4.trial_design(d, idx, sys.argv[1] if len(sys.argv) > 1 else \"sound\")\n    _, r2 = ac4.ridge_loto(Xs, ys, A)\n    R.append(r2)\nbest_el = np.concatenate([A[r.mean(0).argmax(0)] for r in R])\nsrm = E.speech_r.to_numpy()\nv, c = np.unique(best_el[srm], return_counts=True); print('per-electrode best alpha over SpeechR', dict(zip(v, c)))\nbs = np.concatenate([A[r.argmax(1)][:, sr_] .ravel() for r, sr_ in zip(R, [E.speech_r[E.subject.eq(s)].to_numpy() for s in D])])\nv, c = np.unique(bs, return_counts=True); print('per-split best over SpeechR (MIDDLE only)', dict(zip(v, c)))\nperi = E.region.isin(['temporal', 'perisylvian']).to_numpy()\nfor ai, a in enumerate(A):\n    lbA = np.concatenate([ac4.bootstrap_lower(r[:, ai], rng, 2000) for r in R])\n    lbB = np.concatenate([np.percentile(r[:, ai], 1, axis=0) for r in R])\n    m = np.concatenate([r[:, ai].mean(0) for r in R])\n    print(f\"{a:.0e} meanR2>0 {int((m > 0).sum())} bootLB>0 {int((lbA > 0).sum())} p1>0 {int((lbB > 0).sum())}  incl {int(((lbA > 0) & srm & peri).sum())} max mean {m.max():.3f}\")\n"
}
```

```
File created successfully at: /tmp/claude/t2.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/crcns-ac-4-holdgraf-2016; . $TMPDIR/dev/bin/activate; python /tmp/claude/t2.py 2>&1 | grep -v Warn
```

```
per-electrode best alpha over SpeechR {np.float64(10000.0): np.int64(4), np.float64(31622.776601683792): np.int64(13), np.float64(100000.0): np.int64(40), np.float64(316227.7660168379): np.int64(25), np.float64(1000000.0): np.int64(11), np.float64(3162277.660168379): np.int64(2), np.float64(10000000.0): np.int64(1), np.float64(100000000.0): np.int64(7)}
per-split best over SpeechR (MIDDLE only) {np.float64(1.0): np.int64(79), np.float64(3.1622776601683795): np.int64(10), np.float64(10.0): np.int64(21), np.float64(31.622776601683793): np.int64(43), np.float64(100.0): np.int64(65), np.float64(316.2277660168379): np.int64(117), np.float64(1000.0): np.int64(223), np.float64(3162.2776601683795): np.int64(343), np.float64(10000.0): np.int64(470), np.float64(31622.776601683792): np.int64(509), np.float64(100000.0): np.int64(557), np.float64(316227.7660168379): np.int64(405), np.float64(1000000.0): np.int64(213), np.float64(3162277.660168379): np.int64(85), np.float64(10000000.0): np.int64(35), np.float64(31622776.60168379): np.int64(13), np.float64(100000000.0): np.int64(828)}
1e+00 meanR2>0 4 bootLB>0 1 p1>0 0  incl 1 max mean 0.118
3e+00 meanR2>0 4 bootLB>0 0 p1>0 0  incl 0 max mean 0.119
1e+01 meanR2>0 4 bootLB>0 1 p1>0 0  incl 1 max mean 0.122
3e+01 meanR2>0 4 bootLB>0 1 p1>0 0  incl 1 max mean 0.129
1e+02 meanR2>0 5 bootLB>0 1 p1>0 0  incl 1 max mean 0.146
3e+02 meanR2>0 6 bootLB>0 1 p1>0 0  incl 1 max mean 0.173
1e+03 meanR2>0 8 bootLB>0 2 p1>0 0  incl 2 max mean 0.205
3e+03 meanR2>0 15 bootLB>0 3 p1>0 0  incl 3 max mean 0.232
1e+04 meanR2>0 17 bootLB>0 6 p1>0 0  incl 6 max mean 0.242
3e+04 meanR2>0 19 bootLB>0 7 p1>0 0  incl 7 max mean 0.234
1e+05 meanR2>0 19 bootLB>0 8 p1>0 0  incl 8 max mean 0.226
3e+05 meanR2>0 17 bootLB>0 7 p1>0 0  incl 7 max mean 0.193
1e+06 meanR2>0 9 bootLB>0 3 p1>0 0  incl 3 max mean 0.106
3e+06 meanR2>0 1 bootLB>0 0 p1>0 0  incl 0 max mean 0.015
1e+07 meanR2>0 0 bootLB>0 0 p1>0 0  incl 0 max mean -0.030
3e+07 meanR2>0 0 bootLB>0 0 p1>0 0  i
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-ac-4-holdgraf-2016; . $TMPDIR/dev/bin/activate; cat > /tmp/claude/t3.py <<'EOF'
import pickle, os, sys
import numpy as np
sys.path.insert(0, '.')
import ac4
d = pickle.load(open(os.environ['TMPDIR'] + '/S04.pkl', 'rb'))
tr = d['trials']
idx = np.where(((tr.trial_num >= 0) & ~tr.noise & (tr.trial_phase == "mid")).to_numpy())[0]
Xs, ys = ac4.trial_design(d, idx)
A = np.logspace(2, 7, 11)
_, r2 = ac4.ridge_loto(Xs, ys, A)
print('base: top mean R2', np.round(np.sort(r2.mean(0).max(0))[::-1][:8], 3))
# leak-free correlation score: concatenated predictions over folds at best alpha 1e5
ai = 6
# variant: log spectrogram
d2 = dict(d); d2['spec'] = [np.log(s + 1e-3) for s in d['spec']]
Xs2, _ = ac4.trial_design(d2, idx)
_, r2b = ac4.ridge_loto(Xs2, ys, A)
print('log spec: top mean R2', np.round(np.sort(r2b.mean(0).max(0))[::-1][:8], 3))
# variant: lags shifted, check alignment by shifting y
for sh in [-10, -5, 0, 5, 10]:
    on = np.round(tr.onset.to_numpy() * 50).astype(int)
    ys3 = []
    for i, X in zip(idx, Xs):
        ys3.append(d['hfb'][:, on[i] + sh:on[i] + sh + len(X)].T)
    _, r2c = ac4.ridge_loto(Xs, ys3, A)
    print('shift', sh, np.round(np.sort(r2c.mean(0).max(0))[::-1][:5], 3))
EOF
python /tmp/claude/t3.py 2>&1 | grep -v Warn
```

```
base: top mean R2 [0.242 0.226 0.226 0.123 0.086 0.051 0.036 0.014]
log spec: top mean R2 [0.267 0.242 0.239 0.123 0.099 0.057 0.046 0.016]
shift -10 [0.285 0.262 0.241 0.13  0.11 ]
shift -5 [0.253 0.249 0.24  0.124 0.101]
shift 0 [0.242 0.226 0.226 0.123 0.086]
shift 5 [0.199 0.169 0.102 0.089 0.045]
shift 10 [0.113 0.053 0.043 0.041 0.008]
```

**Agent calls Bash**

```bash
cd /tmp/claude && python - <<'EOF'
s=open('nb_src.py').read()
old='''best = np.concatenate(best)
vals, counts = np.unique(best, return_counts=True)
ALPHA = vals[np.argmax(counts)]
print(pd.Series(counts, index=[f"{v:.0e}" for v in vals]).to_string())
print(f"mode {ALPHA:.0e} (grid {ALPHAS[0]:.0e} to {ALPHAS[-1]:.0e}); {len(best)} split x electrode values; {time.time() - t0:.0f} s")'''
new='''        best_el.append(ALPHAS[r2.mean(0).argmax(0)][sr])
best = np.concatenate(best)
vals, counts = np.unique(best, return_counts=True)
print(pd.Series(counts, index=[f"{v:.0e}" for v in vals]).to_string())
print(f"mode of all split values {vals[np.argmax(counts)]:.0e}, the top of the grid: in these splits no alpha predicts the held-out trial better than the null model")
inner = best[best < ALPHAS[-1]]
vals_i, counts_i = np.unique(inner, return_counts=True)
ALPHA = vals_i[np.argmax(counts_i)]
v_el, c_el = np.unique(np.concatenate(best_el), return_counts=True)
print(f"adopted: mode over split values below the top of the grid {ALPHA:.0e} ({len(inner)} of {len(best)} values)")
print(f"variant: mode of each electrode's best alpha (mean R2 over splits) {v_el[np.argmax(c_el)]:.0e}")
print(f"{time.time() - t0:.0f} s")'''
assert old in s
s=s.replace(old,new)
s=s.replace('''t0 = time.time()
best = []
for s, d in D.items():''','''t0 = time.time()
best, best_el = [], []
for s, d in D.items():''')
open('nb_src.py','w').write(s)
EOF
cd entries/crcns-ac-4-holdgraf-2016; . $TMPDIR/dev/bin/activate; date -u; PYTHONPATH=. python $TMPDIR/devrun.py /tmp/claude/nb_src.py 2>&1 | grep -v Warning | cut -c1-250 | sed -n '/fig4b/,$p' | sed -n '/=====/,$p' | tail -n +2 | sed -n '/=====/,$p'
```

```
Mon Nov  9 08:20:54 UTC 2026
===== 
1e+00     230
3e+00      30
1e+01      74
3e+01     151
1e+02     316
3e+02     434
1e+03     713
3e+03    1003
1e+04    1236
3e+04    1343
1e+05    1434
3e+05    1097
1e+06     722
3e+06     308
1e+07     133
3e+07      53
1e+08    2844
mode of all split values 1e+08, the top of the grid: in these splits no alpha predicts the held-out trial better than the null model
[... 138 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/claude && python - <<'EOF'
s=open('nb_src.py').read()
old='''m_inc_n = E.loc[E.subject.isin(noise_subjects), "included"].to_numpy()
print(cluster_report(DIFN[m_inc_n], "(a) included electrodes of S07, S08, S13", 5, ttn).to_string())
print(f"pink noise AFTER-BEFORE mean over (a), 0-3 s: {DIFN[m_inc_n][:, ttn >= 0].mean():.3f} z (n = {m_inc_n.sum()})")
print(cluster_report(DIFS[m_inc_n], "(a) speech triplets, same electrodes", 5, ttn).to_string())'''
new='''m_inc_n = E.loc[E.subject.isin(noise_subjects), "included"].to_numpy()
print("included electrodes in S07, S08, S13:", int(m_inc_n.sum()))
if m_inc_n.sum() >= 2:
    print(cluster_report(DIFN[m_inc_n], "(a) included electrodes of S07, S08, S13", 5, ttn).to_string())
    print(f"pink noise AFTER-BEFORE mean over (a), 0-3 s: {DIFN[m_inc_n][:, ttn >= 0].mean():.3f} z (n = {m_inc_n.sum()})")
else:
    print("set (a) is empty or a single electrode: no test; the claim is judged on set (b)")'''
assert old in s; s=s.replace(old,new)
old='''PCn = pcorr_table(keys=("noise_bef", "noise_mid", "noise_aft"), subjects=noise_subjects)
for tag in ["a", "b"]:'''
new='''PCn = pcorr_table(keys=("noise_bef", "noise_mid", "noise_aft"), subjects=noise_subjects)
print("included electrodes in S07, S08, S13:", len(PCn), "(paper: 12)")
for tag in (["a", "b"] if len(PCn) >= 2 else []):'''
assert old in s; s=s.replace(old,new)
s=s.replace('''print(PCn.groupby("subject").size().to_string())
print(f"MIDDLE pink noise''','''if len(PCn):
    print(PCn.groupby("subject").size().to_string())
    print(f"MIDDLE pink noise''')
open('nb_src.py','w').write(s)
EOF
grep -n "MIDDLE pink noise" /tmp/claude/nb_src.py
```

```
867:    print(f"MIDDLE pink noise model R2, median over these electrodes: {np.median([FITS[(s, 'noise_mid')]['r2'].mean(0)[c] for s, c in zip(PCn.subject, PCn.ch)]):.3f}")
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/crcns-ac-4-holdgraf-2016; . $TMPDIR/dev/bin/activate; date -u; PYTHONPATH=. python $TMPDIR/devrun.py /tmp/claude/nb_src.py 2>&1 | grep -v Warning | cut -c1-250 | sed -n '/claim:supp3a/,$p' | grep -v "^[0-9]* *[a-z]*/[a-z0-9.]*/[a-z]* "
```

```
Mon Nov  9 08:22:32 UTC 2026
===== tags=claim:supp3a-pink-noise-no-hfb-change
                             set   n       p sign  start   end  size
0  (b) Speech-R of S07, S08, S13  39  0.0598    +   0.32  0.44     7
1  (b) Speech-R of S07, S08, S13  39  0.2071    +   0.56  0.64     5
2  (b) Speech-R of S07, S08, S13  39  0.7852    +   0.78  0.80     2
3  (b) Speech-R of S07, S08, S13  39  0.0939    +   1.32  1.42     6
4  (b) Speech-R of S07, S08, S13  39  0.7693    +   1.52  1.54     2
5  (b) Speech-R of S07, S08, S13  39  0.8557    +   2.34  2.36     2
6  (b) Speech-R of S07, S08, S13  39  0.1083    +   2.52  2.60     5
7  (b) Speech-R of S07, S08, S13  39  0.8367    +   2.78  2.80     2
8  (b) Speech-R of S07, S08, S13  39  0.6861    -  -0.50 -0.48     2
9  (b) Speech-R of S07, S08, S13  39  0.4587    -   1.66  1.70     3
speech triplets of the same subjects and electrodes, for comparison:
                   set   n       p sign  start   end  size
0  (b) speech triplets  39  0.0035    +   0.50  0.74    13
1  (b) speech triplets  39  0.1426    +   0.90  1.02     7
2  (b) speech triplets  39  0.9141    +   1.26  1.26     1
3  (b) speech triplets  39  0.7797    +   1.34  1.36     2
4  (b) speech triplets  39  0.0197    +   1.78  1.94     9
[... 278 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/claude && python - <<'EOF'
s=open('nb_src.py').read()
s=s.replace('MAIN = ("nonevent", "sound", "mid")','MAIN = ("nonevent", "2.5", "mid")')
old='''The reading carried into the later claims is the z-score by non-event times (the code's
`zscore_by_non_events`), the window to the end of each sound, and MIDDLE trials (the Methods).
Of the three z-scores only this one gives counts near the paper's; see the record's assumptions.'''
new='''The reading carried into the later claims is the z-score by non-event times (the code's
`zscore_by_non_events`), the 0 to 2.5 s window, and MIDDLE trials (the Methods): of the readings
within the paper's count, it is the first in the order the claims file lists them. Only the
non-event z-score gives counts near the paper's; see the record's assumptions. Sounds that
overlap a span marked `bad` in the events table are kept, as the paper does not mention such
spans (column `sounds_overlapping_bad` above).'''
assert old in s; s=s.replace(old,new)
old='''        diffs = []
        for s, d in D.items():
            chs = np.where(E.loc[E.subject.eq(s), "included"].to_numpy())[0]
            if not len(chs):
                continue
            Xs, _ = ac4.trial_design(d, cond_idx(d["trials"], "mid"))'''
new='''        diffs, befs = [], []
        for s, d in D.items():
            chs = np.where(E.loc[E.subject.eq(s), "included"].to_numpy())[0]
            if not len(chs):
                continue
            Xs, _ = ac4.trial_design(d, cond_idx(d["trials"], "mid"))'''
assert old in s; s=s.replace(old,new)
s=s.replace('''                diffs.append(v["aft"] - v["bef"])
        diffs = np.array(diffs)''','''                diffs.append(v["aft"] - v["bef"]); befs.append(v["bef"])
        diffs, befs = np.array(diffs), np.array(befs)''')
s=s.replace('''        rows.append(dict(strf=strf_kind, rms=rms_kind, n=len(diffs), mean_increase=obs,''','''        rows.append(dict(strf=strf_kind, rms=rms_kind, n=len(diffs), rms_before=befs.mean(), relative_increase=(diffs / befs).mean(), mean_increase=obs,''')
open('nb_src.py','w').write(s)
EOF
grep -n "relative_increase\|befs" /tmp/claude/nb_src.py | head
```

```
699:        diffs, befs = [], []
716:                diffs.append(v["aft"] - v["bef"]); befs.append(v["bef"])
717:        diffs, befs = np.array(diffs), np.array(befs)
719:        rows.append(dict(strf=strf_kind, rms=rms_kind, n=len(diffs), rms_before=befs.mean(), relative_increase=(diffs / befs).mean(), mean_increase=obs,
Shell cwd was reset to
```

**Agent**

Now the entry files, then build the notebook and run the whole thing.

**Agent calls Bash**

```bash
cd entries/crcns-ac-4-holdgraf-2016; cat > requirements.in <<'EOF'
fsspec
aiohttp
requests
numpy
scipy
pandas
matplotlib
mne
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: crcns-ac-4-holdgraf-2016
type: reproduction
title: Rapid tuning shifts in human auditory cortex (Holdgraf et al. 2016)
description: Tests the ECoG findings of Holdgraf, de Heer, Pasley, Rieger, Crone, Lin, Knight and
  Theunissen (2016) on CRCNS data set ac-4, which holds the raw ECoG of seven patients listening to
  filtered, unfiltered and again filtered sentences, with the stimulus audio. It tests the selection
  of speech-responsive and spectrotemporally tuned electrodes, the HFB increase and the coherence
  change from BEFORE to AFTER, the eSTRF comparisons, and the connectivity and spectral analyses of
  the supplement. The behavioural control data are not in the data set.
license: Apache-2.0
notebooks:
- path: reproduce_holdgraf_2016.ipynb
  title: Reproducing Holdgraf et al. (2016) from CRCNS ac-4
  runtime_minutes: 20
helpers:
- ac4.py
related:
- id: crcns:ac-4/unversioned
  relation: uses_data
- id: doi:10.1038/ncomms13654
  relation: reproduces
EOF
. $TMPDIR/dev/bin/activate; python $TMPDIR/build.py /tmp/claude/nb_src.py reproduce_holdgraf_2016.ipynb; cd ../..; python tools/entry.py lock entries/crcns-ac-4-holdgraf-2016 2>&1 | tail -3; python tools/entry.py check entries/crcns-ac-4-holdgraf-2016 2>&1 | tail -15; date -u
```

```
File "tools/entry.py", line 55, in <module>
    import yaml
ModuleNotFoundError: No module named 'yaml'
Traceback (most recent call last):
  File "tools/entry.py", line 55, in <module>
    import yaml
ModuleNotFoundError: No module named 'yaml'
Mon Nov  9 08:26:50 UTC 2026
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; uv pip install -q pyyaml jsonschema nbformat; python tools/entry.py lock entries/crcns-ac-4-holdgraf-2016 2>&1 | tail -3; python tools/entry.py check entries/crcns-ac-4-holdgraf-2016 2>&1 | tail -15
```

```
wrote entries/crcns-ac-4-holdgraf-2016/requirements.lock.txt
0 error(s)
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; date -u; time python tools/entry.py all entries/crcns-ac-4-holdgraf-2016 2>&1 | tail -15; date -u
```

```
Mon Nov  9 08:26:58 UTC 2026
Installed kernelspec registry-crcns-ac-4-holdgraf-2016 in executed/crcns-ac-4-holdgraf-2016/.venv/share/jupyter/kernels/registry-crcns-ac-4-holdgraf-2016
0 error(s)
pass  reproduce_holdgraf_2016.ipynb  (737 s)

real	12m23.355s
user	13m58.412s
sys	1m6.402s
Mon Nov  9 08:39:21 UTC 2026
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; python - <<'EOF' | grep -v "^[0-9]* *[a-z]*/[a-z0-9.]*/[a-z]* " | cut -c1-260
import nbformat
nb=nbformat.read('executed/crcns-ac-4-holdgraf-2016/reproduce_holdgraf_2016.ipynb',4)
for c in nb.cells:
    if c.cell_type!='code': continue
    tags=c.metadata.get('tags',[])
    if not tags or tags==['sanity']:
        if c.source.startswith('# LOAD') or 'ALPHAS' in c.source[:30] or tags==['sanity']:
            pass
        else: continue
    print('=====',tags)
    for o in c.outputs:
        if o.get('name')=='stdout': print(o['text'][:6000])
        elif o.output_type=='error': print('ERR',o.ename,o.evalue)
EOF
```

```
<persisted-output>
Output too large (31.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/52702bf5-4f99-417b-984a-d20e8f06f7e6/tool-results/bl2taton0.txt

Preview (first 2KB):
===== []
S01 98 s peak memory 2.3 GB

S02 167 s peak memory 2.3 GB

S03 222 s peak memory 2.3 GB

S04 269 s peak memory 2.3 GB

S07 352 s peak memory 2.6 GB

S08 426 s peak memory 2.6 GB

S13 508 s peak memory 2.9 GB

===== ['sanity']
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/claim:speech-r-count/,$p' /home/runner/.claude/projects/-home-runner-work-encore-encore/52702bf5-4f99-417b-984a-d20e8f06f7e6/tool-results/bl2taton0.txt | grep -v "frequencies tested" | grep -v "^ [0-9. ]*$" | grep -v "^ *[0-9]*  *(b) \|^ *[0-9]* *(a) all Speech-R  1[0-9]*  0\.[2-9]\|0\.[3-9][0-9]* *[+-] .*\(False\|True\)$" | head -230
```

```
Permission for this tool use was denied. It requires approval, and this session has no approval surface — nobody can answer a permission prompt here — so it was denied automatically. The action was NOT performed; do not claim it succeeded, and do not retry it: this action, and anything else that requires approval, will be denied the same way for the rest of this session. Tell the user what was blocked and why you needed it, then continue with the parts of the task that do not require approval. What required approval: This Bash command contains multiple operations. The following parts require approval: sed -n '/claim:speech-r-count/,$p' /home/runner/.claude/projects/-home-runner-work-encore-encore/52702bf5-4f99-417b-984a-d20e8f06f7e6/tool-results/bl2taton0.txt, grep -v "^ [0-9. ]*$", grep -v "^ *[0-9]*  *(b) \|^ *[0-9]* *(a) all Speech-R  1[0-9]*  0\.[2-9]\|0\.[3-9][0-9]* *[+-] .*\(False\|True\)$"
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/52702bf5-4f99-417b-984a-d20e8f06f7e6/tool-results/bl2taton0.txt",
 "offset": 95,
 "limit": 420
}
```

```
95	S02 HFB contrast at true onsets 0.120; largest at shift +0.2 s; range -0.038 to 0.163
96	
97	S03 HFB contrast at true onsets 0.029; largest at shift +0.1 s; range -0.016 to 0.032
98	S04 HFB contrast at true onsets 0.160; largest at shift +0.1 s; range -0.049 to 0.200
99	
100	S07 HFB contrast at true onsets 0.112; largest at shift +0.0 s; range -0.043 to 0.112
101	
102	S08 HFB contrast at true onsets 0.094; largest at shift +0.1 s; range -0.041 to 0.112
103	S13 HFB contrast at true onsets 0.072; largest at shift +0.0 s; range -0.032 to 0.072
104	
105	===== ['claim:speech-r-count']
106	      zscore window trials  speech_r  pct_of_good  within_92_tol  S01  S02  S03  S04  S07  S08  S13
107	0      trial  sound    mid       145    38.461538          False   33   29   11   20   19   22   11
108	1      trial  sound    all       185    49.071618          False   47   35   19   23   19   29   13
109	2      trial    2.5    mid       141    37.400531          False   30   29   12   19   18   22   11
110	3      trial    2.5    all       182    48.275862          False   46   35   20   20   19   29   13
111	4     pooled  sound    mid       138    36.604775          False   29   28   15   23   18   11   14
112	5     pooled  sound    all       150    39.787798          False   40   27   15   21   18   18   11
113	6     pooled    2.5    mid       131    34.748011          False   28   26   14   22   18   11   12
114	7     pooled    2.5    all       145    38.461538          False   39   27   15   20   16   17   11
[... 353 more lines not kept]
```

**Agent**

Full run passes in about 12 minutes. Now writing the conclusions, summary, README and attempt record.

**Agent calls Bash**

```bash
cd /tmp/claude && cat > results.py <<'PYEOF'
R = {
"RESULT_SPEECH_R": "Three of the twelve readings give a count within 92 +/- 9.2, all with the z-score by non-event times: 96 (onset to sound end, all speech trials), 101 (0 to 2.5 s, MIDDLE trials) and 99 (0 to 2.5 s, all trials). The z-score by each trial's own baseline or by the pooled baseline gives 131 to 185. The data set holds 377 good electrodes (416 in all), against the paper's 468, so 101 is 26.8% of the electrodes against the paper's 19.6%. Speech-R electrodes lie mostly on temporal (66) and perisylvian (18) sites. The count is reproduced under the non-event z-score; the electrode total differs.",
"RESULT_FIG3B": "Over the 101 Speech-R electrodes, AFTER is higher than BEFORE in a cluster from 0.36 to 1.28 s (P = 0.0001) and in a second from 1.72 to 2.02 s (P = 0.0072); the 84 Speech-R electrodes on temporal or perisylvian cortex give a cluster from 0.40 to 1.42 s (P = 0.0001), and the per-trial baseline z-score gives the same (P = 0.0002). The mean difference is 0.084 z over 0 to 1 s. Two of seven subjects (S02, S13) have a slightly negative mean difference. Reproduced.",
"RESULT_SUPP3A": "On the pink noise triplets, no cluster of AFTER minus BEFORE reaches P < 0.05 over the 36 Speech-R electrodes of S07, S08 and S13 (smallest P = 0.0895), so the claim of absence is reproduced on set (b). Set (a) is empty: none of these subjects' electrodes is included in the eSTRF analyses here. The mean AFTER minus BEFORE difference over 0 to 3 s is the same in pink noise and speech triplets (0.041 z in both), and the speech triplets of the same electrodes do give significant clusters (P = 0.0013), so the absence here reflects less power more than a smaller effect.",
"RESULT_SUPP5B": "The slope of mean HFB on trial number is negative and its 95% bootstrap interval excludes 0 under both units: -0.0022 z per trial (-0.0028 to -0.0017) for electrode values pooled, and -0.0019 (-0.0029 to -0.0009) for the mean over electrodes. Six of seven subjects have an interval below 0. Over a session of 57 triplets this is a decrease of about 0.1 z. The paper's test finds the effect here, so the claim of absence is not reproduced.",
"RESULT_FIG4A": "Over the 84 Speech-R electrodes on temporal or perisylvian cortex, AFTER/MIDDLE coherence is higher than BEFORE/MIDDLE in both post-stimulus windows (0 to 1 s: +0.40 bits/s, P = 0.0023; 1 to 2.5 s: +0.29 bits/s, P = 0.0053) and not before the sound (P = 0.137). Over all 251 temporal or perisylvian electrodes only the late window differs (P = 0.032; 0 to 1 s P = 0.65). All seven subjects have a positive mean difference on set (a). Reproduced on the Speech-R set, with a multitaper bandwidth the paper does not give.",
"RESULT_FIG4B": "After subtracting the mean time course, the 1 to 2.5 s window still shows higher AFTER/MIDDLE coherence on the Speech-R set, with the mean over all trials subtracted (+0.20 bits/s, P = 0.038) and with the mean per condition (+0.29, P = 0.0025). Unlike the paper (P = 0.241), the 0 to 1 s window is also significant here (P = 0.0057 and 0.0056). On all temporal or perisylvian electrodes the late window gives P = 0.106 and 0.016. Reproduced on the Speech-R set.",
"RESULT_STRF": "The MIDDLE eSTRFs predict held-out trials in few electrodes: 9 electrodes are STRF-R under the bootstrap bound (13 with samples to 400 ms after offset), and 0 or 1 under the per-split percentiles, against the paper's 53. Their mean held-out R2 ranges from 0.044 to 0.226, and five subjects contribute at most one electrode each. Not reproduced.",
"RESULT_INCLUDED": "The STRF-R electrodes are all Speech-R and on temporal or perisylvian cortex, so the included count follows the STRF-R count: 9 under the adopted readings and at most 13 under any, against 41. They come from three subjects (S01, S02, S04); none from the pink noise subjects. Not reproduced.",
"RESULT_FIG8": "With 9 electrodes, the temporal minus spectral MTF difference has a positive cluster in the region the temporal filter keeps (low temporal, high spectral modulation) in BEFORE (centre 2.1 Hz, P = 0.0078) and in AFTER (centre 2.0 Hz, P = 0.043). The larger positive clusters lie at high temporal modulations (16 to 19 Hz, P = 0.0039 to 0.031), outside both filter regions. For the AFTER minus BEFORE shift, the only significant cluster (P = 0.0039) lies at 15.3 Hz, outside the regions, with the MTF of the difference, and no cluster reaches P < 0.05 with the difference of MTFs. The match holds in BEFORE and AFTER and not in the shift: partially reproduced, on far fewer electrodes than the paper's 41.",
"RESULT_FIG9A": "Over the 9 included electrodes, the AFTER eSTRF gives a larger RMS output to unfiltered speech than the BEFORE eSTRF under every reading (mean increase 11.4 to 12.0, 8 of 9 electrodes positive with mean coefficients), with P = 0.034 and 0.031 for mean coefficients and 0.077 and 0.073 for z-scored coefficients. The RMS is about 105 here, against about 4 on the paper's axis, so the increase cannot be compared with 0.12 on the paper's scale; as a fraction of the BEFORE RMS it is 0.12 to 0.13. The direction holds; the stated value does not: partially reproduced.",
"RESULT_FIG9B": "Over the 9 included electrodes, the MIDDLE eSTRF predicts AFTER better than BEFORE: with R2 over concatenated trials the improvement is 0.051 (P = 0.021), within 0.05 +/- 0.01; with R2 per trial it is 0.089 (P = 0.020). Reproduced under reading (b), on 9 electrodes against the paper's 41.",
"RESULT_FIG10": "Over the 9 included electrodes, AFTER/MIDDLE partial correlation exceeds BEFORE/MIDDLE by a mean 0.308 (P = 0.011) without an intercept and 0.305 (P = 0.0042) with one; 8 of 9 electrodes are positive. The mean is outside 0.18 +/- 0.018 (the median is 0.16). The effect is present and larger: partially reproduced.",
"RESULT_FIG10B": "Across the 9 included electrodes, the partial correlation difference correlates with the mean evoked HFB at r = 0.63 (P = 0.072) and with the MIDDLE model score at r = 0.55 (P = 0.126). Neither r is within 0.42 +/- 0.042 and neither P is below 0.05. Not reproduced.",
"RESULT_FIG10C": "Of the summed positive partial correlation differences, 51.7% lie on the 4 electrodes labelled temporal-superior (reading a), and 4 of 8 electrodes with a positive difference are STG (50%, reading b, not more than half). Reading (a) holds, by a small margin on 9 electrodes: reproduced.",
"RESULT_SUPP3B": "No electrode of S07, S08 or S13 is included in the eSTRF analyses here, so there is nothing to test; the claim is blocked.",
"RESULT_SUPP6A": "With the 6 included temporal electrodes as seeds (three subjects), HFB coherence with frontal/premotor targets rises from BEFORE to AFTER (+0.173 bits/s, t = 3.24, P = 0.031), and with temporal targets rises without significance (+0.110, t = 2.05, P = 0.094). The frontal part is reproduced and the temporal part not: partially reproduced.",
"RESULT_SUPP6A2": "For both target regions the AFTER coherence is closer to MIDDLE than BEFORE is: mean |AFTER - MIDDLE| 0.089 against |BEFORE - MIDDLE| 0.156 bits/s for frontal targets, and 0.207 against 0.214 for temporal targets (6 seeds). Reproduced under the criterion's measure, by a small margin for temporal targets.",
"RESULT_SUPP6B": "PAC between 3 to 8 Hz frontal/premotor phase and HFB amplitude of the 9 included electrodes does not change from BEFORE to AFTER (difference 0.00058, t = 1.63, P = 0.141); the variants give P = 0.055 (4 to 8 Hz) and 0.54 (2 to 12 Hz). Reproduced.",
"RESULT_SUPP7": "In the 66 temporal Speech-R electrodes, no cluster of MIDDLE minus BEFORE envelope coherence reaches P < 0.05 (the smallest, 1.7 to 2.3 Hz, P = 0.093), and none of AFTER minus BEFORE. In the 19 frontal/premotor Speech-R electrodes, MIDDLE exceeds BEFORE from 6.7 to 8.3 Hz (P = 0.0012), where the paper reports no effect. Only the absence of an AFTER minus BEFORE effect holds: not reproduced.",
"RESULT_SUPP4": "AFTER minus BEFORE wavelet power has a positive cluster covering the HFB range in frontal/premotor electrodes (26 to 200 Hz, P = 0.0001, n = 90) and in temporal electrodes (51 to 200 Hz, P = 0.0005, n = 192), and a negative cluster below 25 Hz in frontal electrodes (4.2 to 19.4 Hz, P = 0.0001). Reproduced, with electrode counts that differ from the paper's 75 and 217.",
}
s = open('nb_src.py').read()
for k, v in R.items():
    assert k in s, k
    s = s.replace(k, v)
summary = '''| Claim | Outcome |
|---|---|
| behav-no-context-baseline, behav-context-enhancement, supp1a-linguistic-context, supp1a-speaker-no-difference, supp1b-filter-type, supp5a-behaviour-over-trials | Blocked: data missing |
| speech-r-count | Reproduced (101 under the non-event z-score; 377 electrodes against 468) |
| fig3b-hfb-increase-after | Reproduced |
| supp3a-pink-noise-no-hfb-change | Reproduced |
| supp5b-hfb-stable-over-session | Not reproduced |
| fig4a-coherence-after-higher | Reproduced (assumption) |
| fig4b-coherence-sentence-specific | Reproduced (assumption) |
| strf-r-count | Not reproduced (9 against 53) |
| included-electrode-count | Not reproduced (9 against 41) |
| fig8-mtf-matches-filter | Partially reproduced (assumption) |
| fig9-rms-increase | Partially reproduced |
| fig9-middle-generalizes-after | Reproduced |
| fig10-partial-correlation | Partially reproduced |
| fig10b-similarity-correlates | Not reproduced |
| fig10c-stg-location | Reproduced |
| supp3b-pink-noise-no-pcorr-change | Blocked: no included electrode in the pink noise subjects |
| supp6a-connectivity-increase | Partially reproduced (assumption) |
| supp6a-after-closer-to-middle | Reproduced (assumption) |
| supp6b-no-pac-change | Reproduced |
| supp7-envelope-coherence | Not reproduced |
| supp4-hfb-power-increase | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

How the analysis differs from the paper's: the HFB band edges, the filter orders, the
auditory spectrogram's compression and sharpening, the multitaper bandwidths and the wavelet
range are standard choices the paper does not fix; the z-score that defines Speech-R is the
code's z-score by non-event times, the only one of three readings that gives counts near the
paper's; the ridge parameter is the mode of the per-split best values below the top of the grid,
since the mode over all values falls at the top of any grid. The eSTRFs predict held-out trials
in far fewer electrodes than the paper reports (9 against 53), so every eSTRF claim rests on 9
electrodes from three subjects, and the pink noise eSTRF claim cannot be tested.

What was found about the data set: it holds 7 subjects with 416 channels (377 marked good)
against the paper's 524 recorded and 468 kept, with no mapping between its subject names and
the paper's S1 to S7; the stored values are not in the stated millivolts and their scale
differs by six orders of magnitude between S01 and the other subjects; the behavioural control
data are not included; the stimulus audio is included although the data set's own notebook says
it is not; events marked `bad` are not described.'''
s = s.replace('SUMMARY', summary)
open('nb_final.py', 'w').write(s)
PYEOF
python results.py && grep -c "RESULT_" nb_final.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude/results.py", line 25, in <module>
    assert k in s, k
           ^^^^^^
AssertionError: RESULT_FIG10B
```

**Agent calls Bash**

```bash
cd /tmp/claude && sed -i 's/^for k, v in R.items():/for k, v in sorted(R.items(), key=lambda kv: -len(kv[0])):/' results.py && python results.py && grep -c "RESULT_" nb_final.py; grep -n "Result: fig10\|Result: supp6a" nb_final.py | cut -c1-120
```

```
0
819:**Result: fig10-partial-correlation.** Over the 9 included electrodes, AFTER/MIDDLE partial correlation exceeds BEFO
837:**Result: fig10b-similarity-correlates.** Across the 9 included electrodes, the partial correlation difference corre
853:**Result: fig10c-stg-location.** Of the summed positive partial correlation differences, 51.7% lie on the 4 electrod
927:**Result: supp6a-connectivity-increase.** With the 6 included temporal electrodes as seeds (three subjects), HFB coh
939:**Result: supp6a-after-closer-to-middle.** For both target regions the AFTER coherence is closer to MIDDLE than BEFO
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd /tmp/claude && python - <<'EOF'
s=open('nb_final.py').read()
s=s.replace("| supp3b-pink-noise-no-pcorr-change | Tested |","| supp3b-pink-noise-no-pcorr-change | Run, but no electrode of the pink noise subjects is included, so it is blocked |")
s=s.replace("The whole notebook streams about 1.6 GB and takes about 20 minutes, most of it loading.","The whole notebook streams about 1.6 GB and takes about 13 minutes, most of it loading.")
open('nb_final.py','w').write(s)
EOF
cd  . $TMPDIR/dev/bin/activate; python $TMPDIR/build.py /tmp/claude/nb_final.py entries/crcns-ac-4-holdgraf-2016/reproduce_holdgraf_2016.ipynb; sed -i 's/runtime_minutes: 20/runtime_minutes: 13/' entries/crcns-ac-4-holdgraf-2016/entry.yaml; ls questions | head; date -u
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
Mon Nov  9 08:40:55 UTC 2026
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
print(json.dumps(s,indent=0)[:6000])"
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
[... 258 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
p=s['properties']
for k in ['inputs','findings','verifications']:
  print(k, json.dumps(p.get(k),indent=0)[:1500])
print(list(p))"
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
[... 111 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude/attempt.py",
 "content": "import yaml\n\nNB = \"reproduce_holdgraf_2016.ipynb\"\nBEHAV_NOTE = (\"The behavioural control groups (5, 9 and 15 undergraduate students who typed the words \"\n              \"they understood) are not in the data set, which holds only the patients' ECoG, events, \"\n              \"electrode positions and stimulus audio (data.zip listing and data descriptor). The paper's \"\n              \"data availability statement names only the CRCNS data set, and its code repository \"\n              \"(ecogtools) holds analysis code, not data. No other public copy was found.\")\n\ndef blocked_behav(cid):\n    return dict(claim=cid, outcome=\"blocked\", blocked_by=\"data_missing\", notes=BEHAV_NOTE)\n\nHFB_DEV = (\"HFB band edges and filter orders are not given (claims, open detail 4); 21 log-spaced centres \"\n           \"70 to 140 Hz, each band 10% of its centre wide, 2nd-order Butterworth applied forwards and \"\n           \"backwards, as a standard choice.\")\nSPEECHR_DEV = (\"Speech-R carried into this claim is the reading z-score by non-event times, 0 to 2.5 s, \"\n               \"MIDDLE trials (101 electrodes), the first reading within the paper's count in the claims \"\n               \"file's order (see speech-r-count).\")\nESTRF_DEV = [\n    \"Every eSTRF claim rests on the 9 included electrodes found here (S01 4, S02 1, S04 4), against the \"\n    \"paper's 41 (see strf-r-count and included-electrode-count).\",\n    \"The ridge parameter is the mode of the per-split best values over Speech-R electrodes and the three \"\n    \"conditions, leaving out values at the top of the grid (1e8). Assumed. The Methods take the mode of \"\n    \"the selected values, but 2751 of 11860 values sit at the top of any grid, where no alpha predicts \"\n    \"the held-out trial better than the null model, so the plain mode is the grid edge; the claims file \"\n    \"asks for a grid whose mode is not at an edge. Both this mode and the mode of each electrode's best \"\n    \"alpha give 1e5.\",\n    \"Auditory spectrogram compression (cube root) and spectral sharpening (rectified difference with the \"\n    \"next lower band, as in the NSL model of the Methods' ref. 3) are standard choices; the gammatone \"\n    \"filters are applied in the frequency domain.\",\n]\n\noutcomes = [\n    blocked_behav(\"behav-no-context-baseline\"),\n    blocked_behav(\"behav-context-enhancement\"),\n    blocked_behav(\"supp1a-linguistic-context\"),\n    blocked_behav(\"supp1a-speaker-no-difference\"),\n    blocked_behav(\"supp1b-filter-type\"),\n    blocked_behav(\"supp5a-behaviour-over-trials\"),\n    dict(claim=\"speech-r-count\", outcome=\"reproduced\", notebook=NB, output=\"claim:speech-r-count\",\n         measured=[101, 377],\n         notes=(\"Three of twelve readings (open details 1, 2 and 3) give a count within 92 +/- 9.2, all with \"\n                \"the z-score by non-event times (the code's zscore_by_non_events). Onset to sound end with \"\n                \"all speech trials gives 96, 0 to 2.5 s with MIDDLE trials 101 (recorded as measured, the \"\n                \"first matching reading in the criterion's order), 0 to 2.5 s with all trials 99. The \"\n                \"per-trial baseline z-score gives 141 to 185 and the pooled baseline 131 to 150. The data \"\n                \"set holds 377 good electrodes of 416, against the paper's 468, so 101 is 26.8% of \"\n                \"electrodes against 19.6%; the criterion reports the total and does not judge it. Speech-R \"\n                \"electrodes are mostly temporal (66) and perisylvian (18), as the statement says.\"),\n         deviations=[HFB_DEV,\n                     \"The z-score, window and trials are open details the claims file lists; the result \"\n                     \"matches under 3 of 12 combinations, all with the non-event z-score.\",\n                     \"Electrodes are those marked good in channels.tsv (377); the paper's 468 come from \"\n                     \"channels the data set does not hold.\",\n                     \"Pink noise triplets and the six unfiltered sentences outside any triplet in S01 to \"\n                     \"S04 are left out.\"]),\n    dict(claim=\"fig3b-hfb-increase-after\", outcome=\"reproduced\", notebook=NB, output=\"claim:fig3b-hfb-increase-after\",\n         notes=(\"Over 101 Speech-R electrodes, AFTER exceeds BEFORE in a cluster from 0.36 to 1.28 s (P = \"\n                \"0.0001) and from 1.72 to 2.02 s (P = 0.0072). The 84 Speech-R electrodes on temporal or \"\n                \"perisylvian cortex give 0.40 to 1.42 s (P = 0.0001); the per-trial baseline z-score gives \"\n                \"P = 0.0002 for both sets. Mean difference 0.084 z over 0 to 1 s. S02 and S13 have a \"\n                \"slightly negative mean difference over 0 to 3 s.\"),\n         deviations=[SPEECHR_DEV, HFB_DEV,\n                     \"Cluster test with MNE defaults (two-tailed t threshold for p = 0.05) and 10,000 \"\n                     \"permutations, -0.5 to 3 s (claims, open detail 11).\"]),\n    dict(claim=\"supp3a-pink-noise-no-hfb-change\", outcome=\"reproduced\", notebook=NB, output=\"claim:supp3a-pink-noise-no-hfb-change\",\n         notes=(\"On the pink noise triplets of S07, S08 and S13, no AFTER minus BEFORE cluster reaches P < \"\n                \"0.05 over their 36 Speech-R electrodes (smallest P = 0.0895). Set (a), the included \"\n                \"electrodes of these subjects, is empty here. The mean AFTER minus BEFORE over 0 to 3 s is \"\n                \"0.041 z in both the pink noise and the speech triplets of these electrodes, and the speech \"\n                \"triplets do give significant clusters (P = 0.0013), so the absence comes with an effect \"\n                \"of the same size and less data.\"),\n         deviations=[SPEECHR_DEV, \"Judged on electrode set (b) alone, as set (a) is empty.\"]),\n    dict(claim=\"supp5b-hfb-stable-over-session\", outcome=\"not_reproduced\", notebook=NB, output=\"claim:supp5b-hfb-stable-over-session\",\n         notes=(\"The slope of mean post-stimulus HFB on triplet number is negative with a 95% bootstrap \"\n                \"interval excluding 0, for electrode values pooled (-0.0022 z per trial, -0.0028 to \"\n                \"-0.0017) and for the mean over electrodes per sound (-0.0019, -0.0029 to -0.0009). Six of \"\n                \"seven subjects have an interval below 0 (S04 includes 0). About -0.1 z over 57 triplets.\"),\n         deviations=[SPEECHR_DEV,\n                     \"The value is the mean HFB of every speech sound (BEFORE, MIDDLE and AFTER) and trial \"\n                     \"number the triplet number; the legend does not say which sounds are used.\"]),\n    dict(claim=\"fig4a-coherence-after-higher\", outcome=\"reproduced\", assumed=True, notebook=NB, output=\"claim:fig4a-coherence-after-higher\",\n         notes=(\"On the 84 Speech-R electrodes on temporal or perisylvian cortex (set a), AFTER/MIDDLE minus \"\n                \"BEFORE/MIDDLE coherence is +0.40 bits/s over 0 to 1 s (P = 0.0023) and +0.29 over 1 to 2.5 s \"\n                \"(P = 0.0053); before the sound +0.27 (P = 0.137). All seven subjects are positive. On all \"\n                \"251 temporal or perisylvian electrodes (set b) only 1 to 2.5 s differs (P = 0.032; 0 to 1 s \"\n                \"P = 0.65). Set (a) is adopted, as the Results compute it on speech-responsive electrodes \"\n                \"and its 84 is close to the paper's 78. The integrated coherence is about 14 bits/s in both \"\n                \"conditions, mostly the bias of single-trial coherence from three tapers, which is the same \"\n                \"for both conditions.\"),\n         deviations=[SPEECHR_DEV,\n                     \"Assumed. The multitaper bandwidth is not given; a 400 ms window at 50 Hz has 20 samples \"\n                     \"and MNE's default bandwidth gives one taper, for which single-trial coherence is 1. \"\n                     \"NW = 2 (three tapers) with a jackknife over tapers, integrated from 2.5 to 25 Hz.\",\n                     \"Windows are assigned to the -1 to 0, 0 to 1 and 1 to 2.5 s ranges by their centre; the \"\n                     \"-1 to 0 s range holds two windows.\"]),\n    dict(claim=\"fig4b-coherence-sentence-specific\", outcome=\"reproduced\", assumed=True, notebook=NB, output=\"claim:fig4b-coherence-sentence-specific\",\n         notes=(\"On set (a), 1 to 2.5 s gives AFTER/MIDDLE higher with the mean over all trials subtracted \"\n                \"(+0.20 bits/s, P = 0.038) and with the mean per condition (+0.29, P = 0.0025). Unlike the \"\n                \"paper (P = 0.241), 0 to 1 s is also significant (P = 0.0057 and 0.0056). On set (b) the late \"\n                \"window gives P = 0.106 and 0.016.\"),\n         deviations=[\"The multitaper choice of fig4a-coherence-after-higher (assumed).\"]),\n    dict(claim=\"strf-r-count\", outcome=\"not_reproduced\", notebook=NB, output=\"claim:strf-r-count\", measured=9,\n         notes=(\"With leave-one-trial-out ridge on the MIDDLE trials, 9 electrodes are STRF-R under the \"\n                \"bootstrap bound (a), 0 under the per-split percentiles (b, c); with samples to 400 ms after \"\n                \"offset, 13, 1 and 1. The paper reports 53. Only about 19 electrodes have a mean held-out R2 \"\n                \"above 0 at any ridge value; the STRF-R electrodes have mean R2 0.044 to 0.226. They come \"\n                \"from S01 (4), S02 (1) and S04 (4); none from S03, S07, S08 or S13.\"),\n         deviations=ESTRF_DEV[1:] + [HFB_DEV,\n                     \"Inputs and outputs are z-scored with each fold's training statistics; R2 is the \"\n                     \"coefficient of determination on the held-out trial, as the criterion says.\"]),\n    dict(claim=\"included-electrode-count\", outcome=\"not_reproduced\", notebook=NB, output=\"claim:included-electrode-count\", measured=9,\n         notes=(\"Every STRF-R electrode is Speech-R and temporal or perisylvian under every reading, so the \"\n                \"count follows strf-r-count: 9 under the adopted readings, at most 13, against 41. 6 are \"\n                \"temporal and 3 perisylvian. Location comes from the anatomical labels in channels.tsv.\"),\n         deviations=[\"Temporal lobe is the labels temporal-* and sub_temporal; perisylvian the *-inferior \"\n                     \"frontal, premotor, motor and parietal labels (claims, open detail 6), read from \"\n                     \"channels.tsv, not from the brain images.\"]),\n    dict(claim=\"fig8-mtf-matches-filter\", outcome=\"partially_reproduced\", assumed=True, notebook=NB, output=\"claim:fig8-mtf-matches-filter\",\n         notes=(\"On 9 electrodes, temporal minus spectral MTF has a positive cluster in the region the \"\n                \"temporal filter keeps in BEFORE (centre 2.1 Hz and 0.30 cycles per band, P = 0.0078) and in \"\n                \"AFTER (2.0 Hz, 0.40, P = 0.043). The larger positive clusters lie at 16 to 19 Hz (P = 0.0039 \"\n                \"to 0.031), outside both regions. For the shift, the MTF of the difference has one \"\n                \"significant cluster, at 15.3 Hz (P = 0.0039), outside the regions, and the difference of \"\n                \"MTFs none. With 9 electrodes the smallest possible P is 0.0039.\"),\n         deviations=ESTRF_DEV + [\n             \"Assumed (from the criterion, and made concrete here). Low and high modulation are below and \"\n             \"above the median of the plane's absolute temporal (11.9 Hz) and spectral (0.234 cycles per \"\n             \"band) modulations, measured at the cluster's mean position.\",\n             \"The cluster test runs on the half plane of non-negative spectral modulation, as the amplitude \"\n             \"spectrum of a real eSTRF is symmetric.\"]),\n    dict(claim=\"fig9-rms-increase\", outcome=\"partially_reproduced\", notebook=NB, output=\"claim:fig9-rms-increase\",\n         measured=12.03,\n         notes=(\"On 9 electrodes, the AFTER eSTRF gives a larger RMS output to the MIDDLE spectrograms under \"\n                \"every reading: mean increase 12.0 (P = 0.034) and 11.8 (P = 0.031) with mean coefficients, \"\n                \"11.5 (P = 0.077) and 11.4 (P = 0.073) with z-scored coefficients; 8 of 9 electrodes are \"\n                \"positive with mean coefficients. The output RMS is about 105 here against about 4 on the \"\n                \"paper's Figure 9c axis, so the paper's 0.12 is on a different scale the paper does not \"\n                \"define; as a fraction of the BEFORE RMS the increase is 0.12 to 0.13. The direction and \"\n                \"significance hold under two readings; the stated value does not.\"),\n         deviations=ESTRF_DEV + [\n             \"The MIDDLE spectrograms are z-scored as model inputs (with the MIDDLE statistics) before the \"\n             \"convolution; the Methods do not give their scale, which sets the scale of the RMS.\"]),\n    dict(claim=\"fig9-middle-generalizes-after\", outcome=\"reproduced\", notebook=NB, output=\"claim:fig9-middle-generalizes-after\",\n         measured=0.051,\n         notes=(\"On 9 electrodes, the MIDDLE eSTRF predicts AFTER better than BEFORE. With R2 over \"\n                \"concatenated trials (reading b) the improvement is 0.051 (R2 0.013 to 0.064, P = 0.021), \"\n                \"within 0.05 +/- 0.01; with R2 per trial (reading a) 0.089 (P = 0.020). 7 or 8 of 9 \"\n                \"electrodes are positive.\"),\n         deviations=ESTRF_DEV + [\n             \"Spectrograms and HFB of BEFORE and AFTER are z-scored with each condition's own statistics \"\n             \"(Methods, inputs and outputs z-scored); the Methods do not say which statistics.\"]),\n    dict(claim=\"fig10-partial-correlation\", outcome=\"partially_reproduced\", notebook=NB, output=\"claim:fig10-partial-correlation\",\n         measured=0.308,\n         notes=(\"On 9 electrodes, AFTER/MIDDLE partial correlation exceeds BEFORE/MIDDLE by a mean 0.308 \"\n                \"(P = 0.011) without an intercept and 0.305 (P = 0.0042) with one; medians 0.16; 8 of 9 \"\n                \"positive. The mean is outside 0.18 +/- 0.018. On the 6 temporal-lobe electrodes the mean is \"\n                \"0.43 (P = 0.032).\"),\n         deviations=ESTRF_DEV),\n    dict(claim=\"fig10b-similarity-correlates\", outcome=\"not_reproduced\", notebook=NB, output=\"claim:fig10b-similarity-correlates\",\n         measured=0.625,\n         notes=(\"Across 9 electrodes, the partial correlation difference correlates with mean evoked MIDDLE \"\n                \"HFB at r = 0.63 (P = 0.072) and with the MIDDLE model score at r = 0.55 (P = 0.126). Neither \"\n                \"is within 0.42 +/- 0.042 nor significant.\"),\n         deviations=ESTRF_DEV + [SPEECHR_DEV]),\n    dict(claim=\"fig10c-stg-location\", outcome=\"reproduced\", notebook=NB, output=\"claim:fig10c-stg-location\",\n         notes=(\"Of the summed positive differences, 51.7% (1.44 of 2.78) lie on the 4 electrodes labelled \"\n                \"temporal-superior (reading a, above one half); 4 of 8 electrodes with a positive difference \"\n                \"are STG (reading b, not above one half). 4 of 9 included electrodes are STG. The margin is \"\n                \"small and rests on 9 electrodes.\"),\n         deviations=ESTRF_DEV + [\"STG is the label temporal-superior in channels.tsv.\"]),\n    dict(claim=\"supp3b-pink-noise-no-pcorr-change\", outcome=\"blocked\", blocked_by=\"other\", notebook=NB,\n         output=\"claim:supp3b-pink-noise-no-pcorr-change\",\n         notes=(\"Too few units under the claim's rule. No electrode of S07, S08 or S13 is included in the \"\n                \"eSTRF analyses here (the paper has 12), so there is nothing to test. The eSTRFs on the pink \"\n                \"noise triplets were fit.\"),\n         deviations=ESTRF_DEV[:1]),\n    dict(claim=\"supp6a-connectivity-increase\", outcome=\"partially_reproduced\", assumed=True, notebook=NB, output=\"claim:supp6a-connectivity-increase\",\n         notes=(\"With the 6 included temporal electrodes as seeds (S01, S02, S04), coherence with frontal and \"\n                \"premotor targets rises from BEFORE to AFTER (+0.173 bits/s, t = 3.24, P = 0.031) and with \"\n                \"temporal targets rises without significance (+0.110, t = 2.05, P = 0.094). The paper has 39 \"\n                \"seeds.\"),\n         deviations=ESTRF_DEV + [\n             \"Assumed. The Supplementary Methods say the coherence is computed like that of Figure 4; the \"\n             \"400 ms windows and three tapers of fig4a are used, over 0 to 2.5 s.\",\n             \"Frontal targets are the frontal-* and premotor-* labels; temporal targets the other temporal \"\n             \"electrodes, good channels only.\"]),\n    dict(claim=\"supp6a-after-closer-to-middle\", outcome=\"reproduced\", assumed=True, notebook=NB, output=\"claim:supp6a-after-closer-to-middle\",\n         notes=(\"Mean |AFTER - MIDDLE| is 0.089 against |BEFORE - MIDDLE| 0.156 bits/s for frontal targets, \"\n                \"and 0.207 against 0.214 for temporal targets, on 6 seeds. The temporal margin is small.\"),\n         deviations=[\"The measure of closeness is the criterion's, which it states as an assumption.\",\n                     \"The coherence choices of supp6a-connectivity-increase.\"]),\n    dict(claim=\"supp6b-no-pac-change\", outcome=\"reproduced\", notebook=NB, output=\"claim:supp6b-no-pac-change\",\n         notes=(\"PAC of 3 to 8 Hz frontal/premotor phase with the HFB amplitude of the 9 included electrodes \"\n                \"changes by 0.00058 from BEFORE to AFTER (t = 1.63, P = 0.141). Variants give P = 0.055 (4 to \"\n                \"8 Hz) and 0.54 (2 to 12 Hz).\"),\n         deviations=ESTRF_DEV[:1] + [\n             \"Phase bands are +/- 1 Hz around each frequency, 2nd-order Butterworth, a standard choice; the \"\n             \"post-stimulus samples from onset to the end of each sound are concatenated.\"]),\n    dict(claim=\"supp7-envelope-coherence\", outcome=\"not_reproduced\", notebook=NB, output=\"claim:supp7-envelope-coherence\",\n         notes=(\"In 66 temporal Speech-R electrodes no MIDDLE minus BEFORE cluster reaches P < 0.05 (smallest \"\n                \"1.7 to 2.3 Hz, P = 0.093; 3 to 8 Hz NMI 0.187 BEFORE, 0.201 MIDDLE, 0.186 AFTER bits). No \"\n                \"AFTER minus BEFORE cluster reaches P < 0.05 in either region. In 19 frontal/premotor \"\n                \"Speech-R electrodes MIDDLE exceeds BEFORE from 6.7 to 8.3 Hz (P = 0.0012), where the paper \"\n                \"reports no effect. The paper has 72 temporal electrodes.\"),\n         deviations=[SPEECHR_DEV,\n                     \"Signal and envelope resampled to 100 Hz; multitaper NW = 3 (five tapers) with a \"\n                     \"jackknife, 1 to 30 Hz tested, Gabor wavelets of 7 cycles for the envelope; standard \"\n                     \"choices the paper does not fix.\"]),\n    dict(claim=\"supp4-hfb-power-increase\", outcome=\"reproduced\", notebook=NB, output=\"claim:supp4-hfb-power-increase\",\n         notes=(\"AFTER minus BEFORE power has a positive cluster over the HFB range in frontal/premotor \"\n                \"electrodes (26 to 200 Hz, P = 0.0001, n = 90) and in temporal electrodes (51 to 200 Hz, P = \"\n                \"0.0005, n = 192), and a negative cluster in frontal electrodes from 4.2 to 19.4 Hz (P = \"\n                \"0.0001). Mean change 70 to 150 Hz, 0.23 dB frontal and 0.16 dB temporal; below 25 Hz, -0.33 \"\n                \"dB frontal.\"),\n         deviations=[\"Wavelets from 3 Hz, not the claims file's standard 1 Hz, as the kept epochs (-1 to 3.5 \"\n                     \"s) are too short for 5 cycles below about 3 Hz; post-stimulus 0 to 2.5 s, dB against \"\n                     \"-800 to -100 ms.\",\n                     \"Electrode groups from the channels.tsv labels (frontal-* and premotor-*, 90; temporal, \"\n                     \"192) against the paper's 75 and 217.\"]),\n]\n\nfindings = [\n    dict(kind=\"data_missing\", statement=(\n        \"The behavioural control data (three groups of 5, 9 and 15 listeners) behind Figure 2b and \"\n        \"Supplementary Figures 1 and 5A are not in the data set, and the paper names no other place for \"\n        \"them. Six of the paper's claims cannot be tested.\")),\n    dict(kind=\"selection_undocumented\", statement=(\n        \"The data set holds 416 channels (377 marked good) for its 7 subjects, at most 64 per subject, \"\n        \"while the paper reports grids of 48, 64, 68, 68, 62, 110 and 104 channels and 468 electrodes \"\n        \"kept. The data set does not say which channels were left out or why.\")),\n    dict(kind=\"identifier_missing\", statement=(\n        \"The subjects are named S01, S02, S03, S04, S07, S08 and S13, the paper's S1 to S7, with no \"\n        \"mapping between them, so per-subject results cannot be compared with the paper's figures.\")),\n    dict(kind=\"metadata_error\", statement=(\n        \"channels.tsv gives the unit as milliV and the header a resolution of 0.1, but the stored float32 \"\n        \"values have a median absolute value of about 315 in S01 and 1.7e8 to 6.2e8 in the other six \"\n        \"subjects, so the scale is neither millivolts nor the same across subjects.\")),\n    dict(kind=\"metadata_error\", statement=(\n        \"The data set's explore_data notebook and its per-subject copies say the audio files are not \"\n        \"available for privacy reasons, and the README says subject folders are named like ir-07; the \"\n        \"zip holds a stimulus track per subject (stimuli/<subject>_audio.wav) and folders named sub-S01. \"\n        \"The audio tracks are on the recording's clock (sound onsets in the events table match the audio \"\n        \"onsets in all subjects), but S07's track is 1015 s for a 989 s recording, and S13's is at 20 kHz \"\n        \"against 16 kHz in the others; neither is documented.\")),\n    dict(kind=\"metadata_insufficient\", statement=(\n        \"The events tables of S01, S03, S04 and S07 hold spans with trial_type 'bad' (1 to 12 per subject) \"\n        \"that events.json does not describe, and 22 sounds overlap them; the paper does not mention them. \"\n        \"They were kept here.\")),\n    dict(kind=\"other\", statement=(\n        \"One triplet in S02 and one in S03 lack a sound (46 of 47 and 38 of 39 complete), and S01 to S04 \"\n        \"each have six unfiltered sentences outside any triplet (trial_num -1), which the data set does \"\n        \"not explain.\")),\n    dict(kind=\"methods_unavailable\", statement=(\n        \"Question for the paper's authors. How was HFB z-scored to select Speech-R electrodes? With each \"\n        \"trial's own -800 to -100 ms baseline or a pooled baseline, 131 to 185 electrodes pass here; with \"\n        \"the whole series z-scored by its non-event times (ecogtools zscore_by_non_events) 96 to 104, \"\n        \"near the paper's 92. This attempt assumed the latter.\")),\n    dict(kind=\"methods_unavailable\", statement=(\n        \"Question for the paper's authors. How were the ridge parameter's mode and the STRF-R bound \"\n        \"computed? Over Speech-R electrodes, a quarter of the per-split best values sit at the top of any \"\n        \"grid, so the mode of all values is the grid edge; this attempt took the mode below the edge \"\n        \"(1e5). With the held-out trial's coefficient of determination, only 9 electrodes pass the bound \"\n        \"(the paper has 53). Was R2 computed per held-out trial, over a block of trials, or as a squared \"\n        \"correlation?\")),\n    dict(kind=\"methods_unavailable\", statement=(\n        \"Question for the paper's authors. What multitaper bandwidth was used for the 400 ms coherence \"\n        \"windows of Figure 4 and Supplementary Figure 6A, and over which frequencies was the coherence \"\n        \"integrated? With 20 samples per window, MNE's default bandwidth gives one taper; this attempt \"\n        \"used three (NW = 2), 2.5 to 25 Hz.\")),\n    dict(kind=\"methods_unavailable\", statement=(\n        \"Question for the paper's authors. On what scale is the RMS of Figure 9c (axis about 3.6 to 5.0) \"\n        \"and the mean increase of 0.12? With standardized eSTRFs applied to z-scored spectrograms the RMS \"\n        \"is about 105 here; the relative increase is 0.12 to 0.13.\")),\n]\n\nrec = dict(\n    schema_version=2,\n    id=\"crcns-ac-4-holdgraf-2016-01\",\n    dataset=dict(archive=\"crcns\", id=\"ac-4\", version=\"unversioned\", doi=\"10.6080/K08S4N4J\"),\n    paper=\"doi:10.1038/ncomms13654\",\n    date=\"2026-11-09\",\n    entry=\"crcns-ac-4-holdgraf-2016\",\n    provenance=dict(kind=\"agent\", accountable=dict(name=\"CatalystNeuro\"),\n                    agent=dict(harness=\"Claude Code\", model=\"claude-opus-5-5\", protocol=\"pilot-13\"),\n                    runner=dict(platform=\"GitHub Actions\",\n                                url=\"https://github.com/catalystneuro/encore/actions/runs/42582043075\")),\n    outcomes=outcomes,\n    findings=findings,\n)\nwith open(\"attempts/crcns-ac-4-holdgraf-2016-01.yaml\", \"w\") as f:\n    yaml.dump(rec, f, sort_keys=False, width=100, allow_unicode=True, default_flow_style=False)\n"
}
```

```
File created successfully at: /tmp/claude/attempt.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  sed -i 's/(sound onsets in the events table match the audio "\n/X/' /tmp/claude/attempt.py; python - <<'EOF'
s=open('/tmp/claude/attempt.py').read()
old='''"The audio tracks are on the recording's clock (sound onsets in the events table match the audio "
        "onsets in all subjects), but'''
new='''"The audio tracks are on the recording's clock (the mean audio amplitude rises 2.7 to 211 times "
        "at the event onsets in every subject), but'''
assert old in s; s=s.replace(old,new); open('/tmp/claude/attempt.py','w').write(s)
EOF
. $TMPDIR/dev/bin/activate; python /tmp/claude/attempt.py && grep -n ": .*: " attempts/crcns-ac-4-holdgraf-2016-01.yaml | head -5; head -30 attempts/crcns-ac-4-holdgraf-2016-01.yaml
```

```
schema_version: 2
id: crcns-ac-4-holdgraf-2016-01
dataset:
  archive: crcns
  id: ac-4
  version: unversioned
  doi: 10.6080/K08S4N4J
paper: doi:10.1038/ncomms13654
date: '2026-11-09'
entry: crcns-ac-4-holdgraf-2016
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-13
  runner:
    platform: GitHub Actions
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
s=open('/tmp/claude/attempt.py').read()
old='''"data availability statement names only the CRCNS data set, and its code repository "
              "(ecogtools) holds analysis code, not data. No other public copy was found.")'''
new='''"data availability statement names only the CRCNS data set for data, and the code repository it "
              "links (github.com/choldgraf/ecogtools) is a library of analysis code, as the claims file "
              "describes it. No other place for these data is named.")'''
assert old in s; s=s.replace(old,new); open('/tmp/claude/attempt.py','w').write(s)
EOF
. $TMPDIR/dev/bin/activate; python /tmp/claude/attempt.py; cat > entries/crcns-ac-4-holdgraf-2016/README.md <<'EOF'
# Holdgraf et al. (2016) from CRCNS ac-4

Tests the findings of [Holdgraf et al. (2016)](https://doi.org/10.1038/ncomms13654), "Rapid tuning
shifts in human auditory cortex enhance speech intelligibility", on
[CRCNS ac-4](https://doi.org/10.6080/K08S4N4J), which holds the raw ECoG of seven patients who
heard filtered, unfiltered and again filtered sentences, with the events, channel labels and the
stimulus audio. The behavioural control data are not in it.

| Claim | Outcome |
|---|---|
| Behavioural control results (six claims) | Blocked: data missing |
| 92 of 468 electrodes are speech-responsive | Reproduced (101 of 377, under one z-score) |
| HFB is higher in AFTER than BEFORE | Reproduced |
| No HFB change after pink noise | Reproduced |
| HFB is stable over the session | Not reproduced |
| AFTER/MIDDLE coherence exceeds BEFORE/MIDDLE | Reproduced (assumption) |
| The coherence change remains after removing the mean response | Reproduced (assumption) |
| 53 electrodes are well fit by eSTRFs | Not reproduced (9) |
| 41 electrodes enter the eSTRF analyses | Not reproduced (9) |
| eSTRF MTFs match the filter type | Partially reproduced (assumption) |
| AFTER eSTRFs respond more to unfiltered speech | Partially reproduced |
| MIDDLE eSTRFs predict AFTER better than BEFORE | Reproduced |
| AFTER eSTRFs shift towards MIDDLE (partial correlation) | Partially reproduced |
| The shift correlates with response strength | Not reproduced |
| The shift lies mostly on the STG | Reproduced |
| No eSTRF shift after pink noise | Blocked: no electrode qualifies |
| Seed to target coherence rises after context | Partially reproduced (assumption) |
| AFTER coherence is closer to MIDDLE | Reproduced (assumption) |
| No change in theta to HFB coupling | Reproduced |
| Envelope coherence: theta rise for unfiltered speech in temporal electrodes only | Not reproduced |
| Wavelet HFB power rises, low frequencies fall in frontal electrodes | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The eSTRFs predict held-out trials in far fewer electrodes than the paper reports, so the eSTRF
claims rest on 9 electrodes from three subjects. The data set holds 416 channels against the
paper's 524, its stored values are not in the stated units, and its subjects cannot be matched to
the paper's. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/crcns-ac-4-holdgraf-2016-01.yaml`](../../attempts/crcns-ac-4-holdgraf-2016-01.yaml).

- `reproduce_holdgraf_2016.ipynb`: the analysis. It takes about 13 minutes, most of it streaming
  and reducing the 1.6 GB zip.
- `ac4.py`: reading the zip in place, HFB extraction, the auditory spectrogram, epochs and
  z-scores, the leave-one-trial-out ridge eSTRF, partial correlation, MTF and multitaper
  coherence. Other notebooks on this data set can import it.
EOF
date -u; python tools/entry.py all entries/crcns-ac-4-holdgraf-2016 2>&1 | tail -8; date -u
```

```
Mon Nov  9 08:42:41 UTC 2026
Installed kernelspec registry-crcns-ac-4-holdgraf-2016 in executed/crcns-ac-4-holdgraf-2016/.venv/share/jupyter/kernels/registry-crcns-ac-4-holdgraf-2016
0 error(s)
pass  reproduce_holdgraf_2016.ipynb  (762 s)
Mon Nov  9 08:55:31 UTC 2026
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; python - <<'EOF'
import nbformat,re
nb=nbformat.read('executed/crcns-ac-4-holdgraf-2016/reproduce_holdgraf_2016.ipynb',4)
txt='\n'.join(o.get('text','') for c in nb.cells if c.cell_type=='code' for o in c.outputs if o.get('name')=='stdout')
for pat in ['adopted reading.*','0.36  1.28.*','pink noise AFTER-BEFORE.*','\\(a\\) electrode x sound.*','0 to 1 s   84.*','adopted: samples.*','adopted reading: included.*','mean     concat.*','concat  9.*','\\(a\\) evoked.*intercept a.*','\\(a\\) share.*','temporal seeds to frontal.*','phase 3-8.*','frontal    mid-bef  19  0.0012.*','temporal  192  0.0005.*']:
    m=re.findall(pat,txt); print(m[:2])
print(any(o.output_type=='error' for c in nb.cells if c.cell_type=='code' for o in c.outputs))
EOF
```

```
["adopted reading ('nonevent', '2.5', 'mid') Speech-R 101", 'adopted reading: included 9']
['0.36  1.28    47  nonevent']
['pink noise AFTER-BEFORE mean over (b), 0-3 s: 0.041 z; speech: 0.041 z']
['(a) electrode x sound: slope -0.0022 z per trial, 95% bootstrap interval -0.0028 to -0.0017, includes 0: False']
['0 to 1 s   84        5  15.224524  15.623717  0.399192  0.127009  0.002300', '0 to 1 s   84        5  14.246155  14.540035  0.293880  0.104145  0.005699  (a) mean over all trials']
['adopted: samples (a), bound (a); STRF-R 9']
['adopted reading: included 9']
['mean     concat  9  105.106058           0.126502      12.031495  4.521158  13.563473  0.034197       False       0.888889']
['concat  9  105.106058           0.126502      12.031495  4.521158  13.563473  0.034197       False       0.888889', 'concat  9  108.732078           0.124512      11.486921  5.492542  16.477626  0.076692       False       0.777778']
['(a) evoked vs partial correlation difference (intercept a): r = 0.625, P = 0.0719, n = 9, within 0.42 +/- 0.042: False']
['(a) share of the summed positive differences on STG: 0.517 (1.44 of 2.78)']
['temporal seeds to frontal targets: seeds 6 (subjects 3), BEFORE 9.336, MIDDLE 9.464, AFTER 9.509 bits/s; AFTER-BEFORE mean 0.1730, t = 3.24, P = 0.0312']
['phase 3-8 Hz: n = 9 amplitude electrodes (3 subjects), BEFORE 0.0054, AFTER 0.0060, AFTER-BEFORE 0.00058, t = 1.63, P = 0.1406']
['frontal    mid-bef  19  0.0012    +   6.666667   8.333333          True           True']
['temporal  192  0.0005    +  51.461653  200.000000         True     False']
False
```

**Agent**

Numbers match the conclusions. Handover and final check:

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; python tools/entry.py handover entries/crcns-ac-4-holdgraf-2016 2>&1 | tail -3; python tools/entry.py check entries/crcns-ac-4-holdgraf-2016 2>&1 | tail -3; git status --short; date -u
```

```
wrote executed/crcns-ac-4-holdgraf-2016/handover
0 error(s)
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
?? attempts/crcns-ac-4-holdgraf-2016-01.yaml
?? entries/crcns-ac-4-holdgraf-2016/
?? scripts
Mon Nov  9 08:55:50 UTC 2026
```

**Agent calls Bash**

```bash
ls -a entries/crcns-ac-4-holdgraf-2016; ls executed/crcns-ac-4-holdgraf-2016/handover
```

```
.
..
.claude
README.md
__pycache__
ac4.py
entry.yaml
reproduce_holdgraf_2016.ipynb
requirements.in
requirements.lock.txt
10.1038-ncomms13654.yaml
ac4.py
reproduce_holdgraf_2016.ipynb
```

**Agent calls Bash**

```bash
ls -la entries/crcns-ac-4-holdgraf-2016/.claude; git check-ignore -v entries/crcns-ac-4-holdgraf-2016/__pycache__ entries/crcns-ac-4-holdgraf-2016/.claude
```

```
total 12
drwxr-xr-x 3 runner runner 4096 Nov  9 08:03 .
drwxr-xr-x 4 runner runner 4096 Nov  9 08:42 ..
drwx------ 2 runner runner 4096 Nov  9 08:03 .cc-writes
.gitignore:1:__pycache__/	entries/crcns-ac-4-holdgraf-2016/__pycache__
```

**Agent**

I finished steps 1 to 6 of the Author section: the entry is `entries/crcns-ac-4-holdgraf-2016/`, the record is `attempts/crcns-ac-4-holdgraf-2016-01.yaml`, and `entry.py check` and `all` pass. The handover is built. Nothing is committed and I did not verify my own work.

Of 26 claims, 10 are reproduced, 5 partially reproduced, 5 not reproduced and 6 blocked. The biggest gap is the eSTRF electrode selection: only 9 electrodes qualify against the paper's 53, so every eSTRF claim rests on 9 electrodes from three subjects. That may be a failure of this attempt, not of the paper.

### 1. Outcomes

| Claim | Outcome |
|---|---|
| behav-no-context-baseline, behav-context-enhancement, supp1a-linguistic-context, supp1a-speaker-no-difference, supp1b-filter-type, supp5a-behaviour-over-trials | blocked, `data_missing` |
| speech-r-count | reproduced (101 Speech-R; 3 of 12 readings match; 377 electrodes against the paper's 468) |
| fig3b-hfb-increase-after | reproduced (cluster 0.36 to 1.28 s, P = 0.0001) |
| supp3a-pink-noise-no-hfb-change | reproduced (smallest cluster P = 0.09; but the effect size equals the speech triplets', 0.041 z) |
| supp5b-hfb-stable-over-session | not reproduced (negative slope, interval excludes 0) |
| fig4a-coherence-after-higher | reproduced, rests on an assumption |
| fig4b-coherence-sentence-specific | reproduced, rests on an assumption (0 to 1 s also significant, unlike the paper) |
| strf-r-count | not reproduced (9 against 53) |
| included-electrode-count | not reproduced (9 against 41) |
| fig8-mtf-matches-filter | partially reproduced, rests on an assumption (holds in BEFORE and AFTER, not in the shift) |
| fig9-rms-increase | partially reproduced (direction and P < 0.05 hold; the paper's scale is unknown) |
| fig9-middle-generalizes-after | reproduced (0.051, P = 0.021, n = 9) |
| fig10-partial-correlation | partially reproduced (0.31 against 0.18, P = 0.011) |
| fig10b-similarity-correlates | not reproduced (r = 0.63, P = 0.07) |
| fig10c-stg-location | reproduced (51.7% on STG, a small margin) |
| supp3b-pink-noise-no-pcorr-change | blocked, `other` (no included electrode in the pink noise subjects) |
| supp6a-connectivity-increase | partially reproduced, rests on an assumption (frontal P = 0.031, temporal P = 0.094) |
| supp6a-after-closer-to-middle | reproduced, rests on an assumption |
| supp6b-no-pac-change | reproduced (P = 0.14) |
| supp7-envelope-coherence | not reproduced (no temporal theta effect; a frontal effect, P = 0.0012) |
| supp4-hfb-power-increase | reproduced |

### 2. Dataset, assumptions, questions

**What the dataset holds:**
- 7 subjects with 416 channels (377 good). The paper has 524 recorded and 468 kept, and nothing says which channels were dropped.
- The subject names (S01 to S13) have no mapping to the paper's S1 to S7.
- Stored values are not in the stated millivolts: about 300 in S01 and about 1e8 in the others.
- The behavioural control data are absent.
- The stimulus audio is included and on the recording clock, although the dataset's own notebook says it is not available. S07's audio track is longer than its recording.
- `bad` spans in the events tables are undocumented, and two triplets are incomplete.
- Version: unversioned, the single `live/` copy (descriptor v0.6), with the MD5s printed in the notebook header.

**Assumptions:**
- The Speech-R z-score is the code's z-score by non-event times. It is the only one of three readings that gives counts near 92.
- The ridge parameter is the mode below the top of the grid: the plain mode always falls on the grid edge.
- Coherence uses three tapers (NW = 2), because MNE's default gives one taper on 400 ms windows.
- For fig8, "low" and "high" modulation regions are split at the plane's median.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- How HFB was z-scored for the Speech-R selection.
- How the ridge mode and the STRF-R R2 bound were computed.
- What multitaper bandwidth the coherence used.
- What scale the RMS in Figure 9c is on.

**Questions for a reader:** none.

### 3. Where the protocol was unclear or missing something
1. The `methods_unavailable` finding kind is for the dataset, but the questions are about the paper. I used it as the protocol says.
2. It does not say what happens when a dependent claim's selection, here `included-electrode-count`, is not reproduced but not blocked. I tested the dependents on this attempt's 9 electrodes and said so in their notes.
3. A criterion's readings (z-score, window, trials) gave different outcomes. I followed "reproduced if any reading matches" and used the first matching reading in the criterion's order for the later claims.
4. "Too few units under the claim's own rule" only names `other` as an example. I used `other` for supp3b, where zero units qualified.
5. It does not say how to report a selection threshold whose dataset total differs (377 against 468 electrodes). I reported the total and did not judge it, as the criterion says.

### 4. Runtime and failures
- About 65 minutes in all (07:53 to 08:56 UTC). The notebook runs in 12.7 minutes with a peak of about 2.9 GB.
- Nothing failed in the final run.
- One command, reading a saved output file through sed and grep, was denied for lack of approval. I read the file with the Read tool instead.
- The working tree also has untracked dotfiles at the repo root (`.bashrc`, `.gitconfig` and others) and a modified `tools/build_site.py`. They were there before this run and I left them alone; the workflow should keep them out of the commit.

## End of run

60 turns, 59 minutes, $6.17 at API prices, result: success.
