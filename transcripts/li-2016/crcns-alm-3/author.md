# crcns-alm-3 · author · run 42405983796

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls
```

```
<persisted-output>
Output too large (36.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/cd3f680f-52cd-4720-ac5a-4020bfe48f6a/tool-results/bks09qadi.txt

Preview (first 2KB):
Sat Nov  7 19:28:47 UTC 2026
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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/cd3f680f-52cd-4720-ac5a-4020bfe48f6a/tool-results/bks09qadi.txt"
}
```

```
1	Sat Nov  7 19:28:47 UTC 2026
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
cat README.md | head -150; echo ====; wc -l docs/design.md docs/archives.md; ls paper claims/crcns-alm-3 entries/001453-fouke-2025 claims/001453; ls questions | head
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
[... 151 more lines not kept]
```

**Agent calls Bash**

```bash
cat docs/design.md; grep -n -A80 "## CRCNS" docs/archives.md
```

```
# Reproduction registry: design

Status: draft for discussion. "Reproduction registry" is a working name.

## Goal

Agents work through the dandisets on the DANDI Archive that have an associated
paper. For each one, an agent tries to reproduce the paper's key findings and
figures from the open data, writes the analysis as a notebook, and registers it
here. People can deposit too, but most deposits are expected to come from
agents.

This serves two purposes:

1. **Check the data.** A finding that can be reproduced shows the dandiset is
   complete and accurate enough to support it. A finding that cannot be
   reproduced, with the reason, tells the data owner and the archive what is
   missing.
2. **Give analysts a starting point.** Someone who wants to test a new
   hypothesis on a dandiset starts from notebooks that already load the data
[... 332 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/crcns-alm-3/10.1038-nature17643.yaml
```

```
<persisted-output>
Output too large (53.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/cd3f680f-52cd-4720-ac5a-4020bfe48f6a/tool-results/b1olwgn5f.txt

Preview (first 2KB):
# Claims for Li, Daie, Svoboda & Druckmann (2016), Nature 532, 459-464, "Robust neuronal dynamics
# in premotor cortex during motor planning", doi:10.1038/nature17643, on CRCNS data set alm-3
# (doi:10.6080/K0RB72JW).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-07,
# protocol as stated in docs/protocol.md (Reader), version pilot-13.
#
# Text read: the accepted author manuscript in PubMed Central (PMC5081260, NIHMS767125), as supplied
# under paper/ (Europe PMC): main text, Methods, and the legends of Figures 1 to 6 and Extended Data
# Figures 1 to 10. The paper has no separate Supplementary Information. No PDF of the paper was
# supplied, so values printed only inside figures (per-condition performance in Fig. 1d and 5b,
# fractions in ED Fig. 8a and 8b) were not read; claims on those panels rest on the text and
# legends. The version of record was not read. The record lists a corrigendum
# (doi:10.1038/nature18623) whose text was not supplied or read.
#
# Code. The paper links no analysis or simulation code. The CRCNS data set's description says it
# holds MATLAB analysis scripts that reproduce the paper's figures; they are files of the data set
[... 11 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/cd3f680f-52cd-4720-ac5a-4020bfe48f6a/tool-results/b1olwgn5f.txt"
}
```

```
1	# Claims for Li, Daie, Svoboda & Druckmann (2016), Nature 532, 459-464, "Robust neuronal dynamics
2	# in premotor cortex during motor planning", doi:10.1038/nature17643, on CRCNS data set alm-3
3	# (doi:10.6080/K0RB72JW).
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-07,
5	# protocol as stated in docs/protocol.md (Reader), version pilot-13.
6	#
7	# Text read: the accepted author manuscript in PubMed Central (PMC5081260, NIHMS767125), as supplied
8	# under paper/ (Europe PMC): main text, Methods, and the legends of Figures 1 to 6 and Extended Data
9	# Figures 1 to 10. The paper has no separate Supplementary Information. No PDF of the paper was
10	# supplied, so values printed only inside figures (per-condition performance in Fig. 1d and 5b,
11	# fractions in ED Fig. 8a and 8b) were not read; claims on those panels rest on the text and
12	# legends. The version of record was not read. The record lists a corrigendum
13	# (doi:10.1038/nature18623) whose text was not supplied or read.
14	#
15	# Code. The paper links no analysis or simulation code. The CRCNS data set's description says it
16	# holds MATLAB analysis scripts that reproduce the paper's figures; they are files of the data set
17	# and were not read here. Every method below is from the paper's text.
18	#
19	# Data the paper used. 33 mice (age > P60). Electrophysiology during behaviour, left ALM, 12 mice
20	# (5 VGAT-ChR2-EYFP, 7 PV-ires-cre x ReaChR), NeuroNexus 32-channel probes: 1012 single units in 58
[... 836 more lines not kept]
```

**Agent calls Bash**

```bash
cat paper/alm-3.data-description.txt; wc -c paper/10.1038-nature17643.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=alm-3/" > l1.xml; python3 -c "
import re
t=open('l1.xml').read()
ks=re.findall(r'<Key>(.*?)</Key><LastModified>(.*?)</LastModified><ETag>(.*?)</ETag><Size>(\d+)</Size>',t)
for k in ks: print(k[0],k[1],k[3])
print(len(ks), 'IsTruncated' , re.findall('<IsTruncated>(.*?)<',t))
"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; head -c 3000 l1.xml
```

```
<?xml version="1.0" encoding="UTF-8"?>
<ListBucketResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/"><Name>crcnsarchive</Name><Prefix>alm-3/</Prefix><KeyCount>224</KeyCount><MaxKeys>1000</MaxKeys><IsTruncated>false</IsTruncated><Contents><Key>alm-3/</Key><LastModified>2026-02-11T00:41:29.000Z</LastModified><ETag>&quot;d41d8cd98f00b204e9800998ecf8427e&quot;</ETag><ChecksumAlgorithm>CRC64NVME</ChecksumAlgorithm><ChecksumType>FULL_OBJECT</ChecksumType><Size>0</Size><StorageClass>STANDARD</StorageClass></Contents><Contents><Key>alm-3/live/</Key><LastModified>2026-02-11T00:41:29.000Z</LastModified><ETag>&quot;d41d8cd98f00b204e9800998ecf8427e&quot;</ETag><ChecksumAlgorithm>CRC64NVME</ChecksumAlgorithm><ChecksumType>FULL_OBJECT</ChecksumType><Size>0</Size><StorageClass>STANDARD</StorageClass></Contents><Contents><Key>alm-3/live/analyses_scripts/</Key><LastModified>2026-02-11T00:41:39.000Z</LastModified><ETag>&quot;d41d8cd98f00b204e9800998ecf8427e&quot;</ETag><ChecksumAlgorithm>CRC64NVME</ChecksumAlgorithm><ChecksumType>FULL_OBJECT</ChecksumType><Size>0</Size><StorageClass>STANDARD</StorageClass></Contents><Contents><Key>alm-3/live/analyses_scripts/ALM_compiled_all_data_bilateral.mat</Key><LastModified>2026-02-11T01:09:33.000Z</LastModified><ETag>&quot;d8a5a7f08ea20ba43b9ec6de5127db69&quot;</ETag><ChecksumAlgorithm>CRC64NVME</ChecksumAlgorithm><ChecksumType>FULL_OBJECT</ChecksumType><Size>49223137</Size><StorageClass>INTELLIGENT_TIERING</StorageClass></Contents><Contents><Key>alm-3/live/analyses_scripts/ALM_compiled_all_data_bilateralCCX.mat</Key><LastModified>2026-02-11T01:09:36.000Z</LastModified><ETag>&quot;4b1b00529f170e5b35be7a80be9a0d53&quot;</ETag><ChecksumAlgorithm>CRC64NVME</ChecksumAlgorithm><ChecksumType>FULL_OBJECT</ChecksumType><Size>41246824</Size><StorageClass>INTELLIGENT_TIERING</StorageClass></Contents><Contents><Key>alm-3/live/analyses_scripts/ALM_compiled_all_data_bilateralCCX_FR.mat</Key><LastModified>2026-02-11T01:09:41.000Z</LastModified><ETag>&quo
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; python3 -c "
import re
t=open('l1.xml').read()
for c in re.findall(r'<Contents>(.*?)</Contents>',t):
  k=re.search('<Key>(.*?)</Key>',c).group(1); s=re.search('<Size>(.*?)</Size>',c).group(1)
  print(k,s)
"
```

```
alm-3/ 0
alm-3/live/ 0
alm-3/live/analyses_scripts/ 0
alm-3/live/analyses_scripts/ALM_compiled_all_data_bilateral.mat 49223137
alm-3/live/analyses_scripts/ALM_compiled_all_data_bilateralCCX.mat 41246824
alm-3/live/analyses_scripts/ALM_compiled_all_data_bilateralCCX_FR.mat 32421918
alm-3/live/analyses_scripts/ALM_compiled_all_data_bilateral_FR.mat 35164479
alm-3/live/analyses_scripts/ALM_compiled_all_data_bilateral_activityModes.mat 6192530
alm-3/live/analyses_scripts/ALM_compiled_all_data_bilateral_activityModesCCX.mat 9017638
alm-3/live/analyses_scripts/ALM_compiled_all_data_bilateral_predictBehavior.mat 7767156
alm-3/live/analyses_scripts/ALM_compiled_all_data_unilateral.mat 30624878
alm-3/live/analyses_scripts/analysis_compile_all_data_bilateral.m 45152
alm-3/live/analyses_scripts/analysis_compile_all_data_bilateralCCX.m 45184
alm-3/live/analyses_scripts/analysis_compile_all_data_bilateralCCX_FR.m 35172
alm-3/live/analyses_scripts/analysis_compile_all_data_bilateral_FR.m 43253
alm-3/live/analyses_scripts/analysis_compile_all_data_bilateral_activityModes.m 63055
alm-3/live/analyses_scripts/analysis_compile_all_data_bilateral_activityModesCCX.m 22659
alm-3/live/analyses_scripts/analysis_compile_all_data_bilateral_predictBehavior.m 28392
alm-3/live/analyses_scripts/analysis_compile_all_data_unilateral.m 45871
alm-3/live/analyses_scripts/helper_functions/ 0
[... 205 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; B=https://crcnsarchive.s3-us-west-2.amazonaws.com/alm-3/live; curl -s -r 0-200 $B/data/data_structure_files/data_structure_ANM255200_20140910.mat | head -c 140; echo; mkdir -p scripts; for f in analysis_compile_all_data_bilateral.m analysis_compile_all_data_bilateralCCX.m analysis_compile_all_data_bilateralCCX_FR.m analysis_compile_all_data_bilateral_FR.m analysis_compile_all_data_bilateral_activityModes.m analysis_compile_all_data_bilateral_activityModesCCX.m analysis_compile_all_data_bilateral_predictBehavior.m analysis_compile_all_data_unilateral.m helper_functions/func_discriminant.m helper_functions/func_getPSTH.m helper_functions/func_getPSTH_smallBin.m helper_functions/Gram_Schmidt_process.m; do curl -s $B/analyses_scripts/$f -o scripts/$(basename $f); done; curl -s $B/docs/Demo_get_performance.m -o scripts/Demo_get_performance.m; curl -s $B/docs/Demo_get_trial_aligned_raster_PSTH.m -o scripts/Demo_psth.m; curl -s $B/checksums.md5 -o checksums.md5; curl -s $B/filelist.txt -o filelist.txt; ls -la scripts; head -5 checksums.md5; head -20 filelist.txt; python3 -c "import scipy,h5py,fsspec;print('ok')"
```

```
Exit code 1
MATLAB 5.0 MAT-file, Platform: PCWIN64, Created on: Thu Mar 10 15:56:16 2016                                                 IM   ZqCx��
total 376
drwxr-xr-x 2 runner runner  4096 Nov  7 19:33 .
drwx------ 6 runner runner  4096 Nov  7 19:33 ..
-rw-r--r-- 1 runner runner  3485 Nov  7 19:33 Demo_get_performance.m
-rw-r--r-- 1 runner runner  4216 Nov  7 19:33 Demo_psth.m
-rw-r--r-- 1 runner runner  1704 Nov  7 19:33 Gram_Schmidt_process.m
-rw-r--r-- 1 runner runner 45152 Nov  7 19:32 analysis_compile_all_data_bilateral.m
-rw-r--r-- 1 runner runner 45184 Nov  7 19:32 analysis_compile_all_data_bilateralCCX.m
-rw-r--r-- 1 runner runner 35172 Nov  7 19:32 analysis_compile_all_data_bilateralCCX_FR.m
-rw-r--r-- 1 runner runner 43253 Nov  7 19:33 analysis_compile_all_data_bilateral_FR.m
-rw-r--r-- 1 runner runner 63055 Nov  7 19:33 analysis_compile_all_data_bilateral_activityModes.m
-rw-r--r-- 1 runner runner 22659 Nov  7 19:33 analysis_compile_all_data_bilateral_activityModesCCX.m
-rw-r--r-- 1 runner runner 28392 Nov  7 19:33 analysis_compile_all_data_bilateral_predictBehavior.m
-rw-r--r-- 1 runner runner 45871 Nov  7 19:33 analysis_compile_all_data_unilateral.m
-rw-r--r-- 1 runner runner   745 Nov  7 19:33 func_discriminant.m
-rw-r--r-- 1 runner runner   780 Nov  7 19:33 func_getPSTH.m
-rw-r--r-- 1 runner runner   527 Nov  7 19:33 func_getPSTH_smallBin.m
6c7233665f26b26ba5de3588b06c5e92  analyses_scripts/ALM_compiled_all_data_bilateral_activityModesCCX.mat
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q v && . v/bin/activate && uv pip install -q scipy numpy fsspec aiohttp requests h5py pandas statsmodels matplotlib 2>&1 | tail -2; python -c "import scipy;print(scipy.__version__)"
```

**Agent calls Bash**

```bash
cat $TMPDIR/scripts/analysis_compile_all_data_unilateral.m
```

```
1.18.1
Shell cwd was reset to
```

```
<persisted-output>
Output too large (44.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/cd3f680f-52cd-4720-ac5a-4020bfe48f6a/tool-results/bmux2b0w7.txt

Preview (first 2KB):
clear all
close all

addpath('.\helper_functions\')


%% list of animals to analyze
animals_list = {
    'ANM255200';...  % ReachR
    'ANM255203';...  % ReachR
    'ANM255201';...  % ReachR
    'ANM257772';...  % ReachR
    'ANM258250';...  % VGAT
    };

if ~exist('ALM_compiled_all_data_unilateral.mat')
[... 55 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/cd3f680f-52cd-4720-ac5a-4020bfe48f6a/tool-results/bmux2b0w7.txt",
 "offset": 60,
 "limit": 420
}
```

```
60	        
61	        for i_file = 1:n_file
62	            
63	            % --------------- load 'obj' and 'meta_data' -------------------
64	            clear obj meta_data
65	            disp([animals_list{i_animal},'  File #',num2str(i_file),'/',num2str(n_file)]);
66	            load([dir_tmp,file_list(i_file).name]);
67	            load([dir_tmp,file_meta_data_list(i_file).name]);
68	            
69	            
70	            % get mouse ID
71	            n_file_count = n_file_count+1;
72	            animal_ID{n_file_count,1} = animals_list{i_animal};
73	            animal_ID{n_file_count,2} = file_list(i_file).name;
74	            animal_ID{n_file_count,3} = file_meta_data_list(i_file).name;
75	            
76	            
77	            
78	            % --------------- get behavioral data -----------------
79	            clear trialID i_Hit* i_Err* i_NoLick* i_LickEarly* i_StimTrials* i_GoodTrials
[... 400 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/cd3f680f-52cd-4720-ac5a-4020bfe48f6a/tool-results/bmux2b0w7.txt",
 "offset": 480,
 "limit": 900
}
```

```
480	                            t_tmp(end+1,:) = t_bin;
481	                        end
482	                        
483	                        p_stim3(n_unit,:,1) = p_tmp(:,1);
484	                        
485	                    else
486	                        p_stim3(n_unit,:,1) = nan(size(t_stim));
487	                    end
488	                    
489	                    
490	                    
491	                    
492	                    
493	                    
494	                    
495	                    % ============ select screen and test trials ============
496	                    n_trials_tmp = length(i_yes_trial);
497	                    i_yes_trial = i_yes_trial(randsample(n_trials_tmp,n_trials_tmp));
498	                    i_yes_trial_screen = i_yes_trial(1:5);
499	                    i_yes_trial = i_yes_trial(6:end);
[... 485 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . v/bin/activate && cat > t1.py <<'EOF'
import time, resource, fsspec, scipy.io as sio, io
t=time.time()
url='https://crcnsarchive.s3-us-west-2.amazonaws.com/alm-3/live/data/data_structure_files/data_structure_ANM255200_20140910.mat'
with fsspec.open(url,'rb',block_size=2**24) as f: b=f.read()
print('read',time.time()-t, len(b))
t=time.time()
m=sio.loadmat(io.BytesIO(b),squeeze_me=True,struct_as_record=False)
print('load',time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,'GB')
print(m.keys())
o=m['obj']
print(o._fieldnames)
for k in o._fieldnames:
    v=getattr(o,k); print(k, type(v), getattr(v,'shape',None))
print(o.trialTypeStr, o.trialTypeMat.shape)
tp=o.trialPropertiesHash; print(tp._fieldnames, tp.keyNames, tp.descr)
for v in tp.value: print(getattr(v,'shape',None), v[:5])
ts=o.timeSeriesArrayHash; print(ts._fieldnames, ts.keyNames, ts.descr)
v=ts.value; print(v._fieldnames, v.idStr, v.idStrDetailed, v.valueMatrix.shape, v.time[:3], v.timeUnit)
es=o.eventSeriesHash; print(es._fieldnames, len(es.value), es.keyNames[:3], es.descr[:3])
u=es.value[0]; print(u._fieldnames)
for k in u._fieldnames: x=getattr(u,k); print(k, type(x), getattr(x,'shape',None), x if not hasattr(x,'shape') or x.size<5 else x[:3])
print(o.descrHash._fieldnames, o.descrHash.keyNames, o.descrHash.value)
print(o.timeUnitIds, o.timeUnitNames, o.trialTimeUnit)
EOF
python t1.py
```

```
read 2.9687931537628174 121860578
load 1.0354340076446533 0.81754 GB
dict_keys(['__header__', '__version__', '__globals__', 'obj'])
['timeUnitIds', 'timeUnitNames', 'descrHash', 'trialTimeUnit', 'trialTypeStr', 'trialIds', 'trialStartTimes', 'trialTypeMat', 'trialPropertiesHash', 'timeSeriesHash', 'timeSeriesArrayHash', 'eventSeriesHash']
timeUnitIds <class 'numpy.ndarray'> (5,)
timeUnitNames <class 'numpy.ndarray'> (5,)
descrHash <class 'scipy.io.matlab._mio5_params.mat_struct'> None
trialTimeUnit <class 'int'> None
trialTypeStr <class 'numpy.ndarray'> (8,)
trialIds <class 'numpy.ndarray'> (288,)
trialStartTimes <class 'numpy.ndarray'> (288,)
trialTypeMat <class 'numpy.ndarray'> (8, 288)
trialPropertiesHash <class 'scipy.io.matlab._mio5_params.mat_struct'> None
timeSeriesHash <class 'numpy.ndarray'> (0,)
timeSeriesArrayHash <class 'scipy.io.matlab._mio5_params.mat_struct'> None
eventSeriesHash <class 'scipy.io.matlab._mio5_params.mat_struct'> None
['HitR' 'HitL' 'ErrR' 'ErrL' 'NoLickR' 'NoLickL' 'LickEarly' 'StimTrials'] (8, 288)
['keyNames', 'descr', 'value'] ['PoleInTime' 'PoleOutTime' 'CueTime' 'GoodTrials' 'PhotostimulationType'] ['Start of Sample period (in seconds, relative to trial start time)'
 'Start of Delay period (in seconds, relative to trial start time)'
 'Start of Response period (in seconds, relative to trial start time)'
[... 158 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . v/bin/activate && cat > t2.py <<'EOF'
import fsspec, scipy.io as sio, io, numpy as np
url='https://crcnsarchive.s3-us-west-2.amazonaws.com/alm-3/live/data/data_structure_files/data_structure_ANM255200_20140910.mat'
with fsspec.open(url,'rb',block_size=2**24) as f: b=f.read()
o=sio.loadmat(io.BytesIO(b),squeeze_me=True,struct_as_record=False)['obj']
v=o.timeSeriesArrayHash.value
tp=o.trialPropertiesHash.value
st=tp[4]; print(np.unique(st[~np.isnan(st.astype(float))],return_counts=True))
print('trial col', v.trial[:5], np.unique(np.diff(v.time))[:5])
vm=v.valueMatrix
for c in range(3): print(c, np.percentile(vm[:,c],[0,1,50,99,100]))
good=tp[3]==1
for i in np.where((st==2)&good)[0][:2].tolist()+np.where((st==0)&good)[0][:1].tolist():
    tid=o.trialIds[i]; m=v.trial==tid
    t=v.time[m]-o.trialStartTimes[i]
    L=vm[m,2]; on=t[L>0.1*L.max()] if L.max()>0 else []
    print('trial',tid,'pole',tp[0][i],tp[1][i],'cue',tp[2][i],'tlen',t.min(),t.max(),'laser on',(on[0],on[-1]) if len(on) else None, 'Lmax',L.max())
    lk=vm[m,0]; print(' lick pct', np.percentile(lk,[1,50,99,100]))
    thr=lk>np.percentile(vm[:,0],50)+1; 
    ac=t[1:][np.diff(thr.astype(int))==1]; print(' lick onsets', ac[:10])
EOF
python t2.py
```

```
/tmp/claude-1001/v/lib/python3.13/site-packages/numpy/lib/_function_base_impl.py:4609: RuntimeWarning: invalid value encountered in subtract
  diff_b_a = b - a
(array([-3, -2, -1,  0], dtype=int16), array([ 35,  35,  32, 186]))
trial col [5 5 5 5 5] [9.99999993e-05 9.99999997e-05 1.00000000e-04 3.62406600e+00
 3.63206500e+00]
0 [0.18379518 0.18605293 0.18831068 0.19056843 0.19863183]
1 [       nan 0.00027234 0.00575544        nan        nan]
2 [       nan        nan 0.         2.66048266        nan]
trial 18 pole 0.5721650000000409 2.530323999999928 cue 3.8308179999999084 tlen 0.0 4.999899999999798 laser on None Lmax 0.0
 lick pct [0.1857304  0.18798815 0.18992336 0.19121351]
 lick onsets []
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/001453-fouke-2025; cat entry.yaml requirements.in README.md; head -c 1500 omr.py; python3 -c "
import json;nb=json.load(open('reproduce_fouke_2025.ipynb'))
for c in nb['cells'][:6]: print(c['cell_type'],c.get('metadata'),''.join(c['source'])[:1200]);print('----')
"; ls ../; grep -n "crcns" -ri ../../tools/entry.py | head
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
[... 387 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/001453-fouke-2025-01.yaml | head -150; ls schemas
```

```
schema_version: 2
id: 001453-fouke-2025-01
dataset:
  archive: dandi
  id: "001453"
  version: 0.250518.1950
  doi: 10.48324/dandi.001453/0.250518.1950
paper: doi:10.1016/j.cub.2025.04.027
date: 2026-10-14
entry: 001453-fouke-2025
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
[... 134 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 150,400p attempts/001453-fouke-2025-01.yaml | grep -n -A12 "^findings\|^- claim: fig2\|blocked" | head -80; python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s,indent=0)[:6000])"
```

```
49:  outcome: blocked
50:  blocked_by: metadata_insufficient
51-  notes: The numbers come from single representative fish and trials. Fig1-S1.ipynb selects them
52-    by the index of a data folder and a trial number (for example DC folder 29, trial 79), and the
53-    dandiset gives no mapping from those folders to its subjects, nor the original file names.
54:- claim: fig2d-shared-architecture
55:  outcome: blocked
56:  blocked_by: data_missing
57-  notes: The two-photon imaging data are not in the dandiset, which holds only freely swimming
58-    tracking. The GitLab repository the paper names for "all behavioral and imaging data" holds
59-    notebooks only, and no other dandiset of this lab or paper was found on the archive.
60:- claim: fig2g-dsi-similar
61:  outcome: blocked
62:  blocked_by: data_missing
63-  notes: Imaging data not in the dandiset, nor found elsewhere (see fig2d-shared-architecture).
64:- claim: fig2h-fewer-motion-responsive
65:  outcome: blocked
66:  blocked_by: data_missing
67-  notes: Imaging data not in the dandiset, nor found elsewhere (see fig2d-shared-architecture).
68:- claim: fig2k-more-monocular
[... 316 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p entries/crcns-alm-3-li-2016 && cat > entries/crcns-alm-3-li-2016/alm3.py <<'EOF'
"""Loading and measures for CRCNS data set alm-3 (Li, Daie, Svoboda & Druckmann 2016, Nature 532,
459-464, doi:10.1038/nature17643).

The data set holds one MATLAB file per recording session (`data/data_structure_files/`), each a
structure `obj` with the trial table, the photostimulus type of each trial, the lick and laser
traces, and the spike times of the sorted single units. Files are streamed from the public S3
bucket `crcnsarchive` into memory and reduced as they load; nothing is written to disk. CRCNS data
sets are not versioned; the files read are those under `alm-3/live/` with the MD5 sums of the data
set's `checksums.md5`.

Where the parameters come from. "Code" is the authors' MATLAB analysis scripts deposited in the
data set (`alm-3/live/analyses_scripts/`), which the data set's description says reproduce the
paper's figures; the claims file did not read them. They are cited by file name.

- Trials (`trial_mask`): correct and error trials grouped by instructed movement (HitR or ErrR is
  lick right, HitL or ErrL lick left), lick-early trials and trials marked GoodTrials = 0 dropped,
  and only trials between the unit's first and last trial with a spike (the unit's stable
  trials). Code, analysis_compile_all_data_unilateral.m, "index the behavioral trials" and "index
  stable trials"; the Methods, Electrophysiology data analysis, say selectivity under
  photoinhibition uses "all trials, correct and incorrect, grouped by instructed movement".
- Epochs: sample from PoleInTime to PoleOutTime, delay from PoleOutTime to CueTime, response the
  1.3 s after CueTime (code, same file, "significant selectivity").
- Cell type: the `cellType` label of each unit ("pyramidal", "FS" or empty), which the data
  description says comes from the spike-width bounds of the Methods. The trough-to-peak width of
  the mean waveform is also computed, to check the label.
- PSTH: spike counts in 200 ms windows moved in 1 ms steps... see `psth`, which follows
  func_getPSTH.m of the code.
- Licks: the first lick after the go cue is the first upward crossing of the lick trace (a
  photodiode signal) over a threshold set per session halfway between the trace's median and its
  99.9th percentile; a standard choice, as neither the paper nor the code defines it.
"""
import io
import re
import time
import xml.etree.ElementTree as ET

import fsspec
import numpy as np
import requests
import scipy.io as sio

BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com"
PREFIX = "alm-3/live/"
DATASET_DOI = "10.6080/K0RB72JW"

STIM_LABELS = {
    0: "control",
    1: "ipsi 1 spot sample (0.5 s)",
    2: "ipsi 1 spot early delay (0.5 s)",
    3: "ipsi 1 spot middle delay (0.5 s)",
    -1: "no ramp sample (do not analyse)",
    -2: "no ramp early delay (do not analyse)",
    -3: "no ramp middle delay (do not analyse)",
    4: "ipsi 1 spot (0.8 s)",
    5: "contra 1 spot (0.8 s)",
    6: "bilateral 4 spots (0.8 s)",
    7: "bilateral 1 spot (0.8 s)",
    8: "ipsi 4 spots (0.8 s)",
    9: "contra 4 spots (0.8 s)",
    10: "CCX ipsi 1 spot (0.8 s)",
    11: "CCX contra 1 spot (0.8 s)",
    12: "CCX bilateral 4 spots (0.8 s)",
}

SAMPLE_RATE_WAVEFORM = 19531.25  # Hz, data description ("Each snippets is 29 samples long")


def list_files():
    """List the data set's files under alm-3/ with their sizes, from the bucket's listing."""
    r = requests.get(f"{BUCKET}/?list-type=2&prefix=alm-3/", timeout=60)
    r.raise_for_status()
    ns = {"s": "http://s3.amazonaws.com/doc/2006-03-01/"}
    root = ET.fromstring(r.content)
    if root.find("s:IsTruncated", ns).text != "false":
        raise RuntimeError("bucket listing truncated")
    out = {}
    for c in root.findall("s:Contents", ns):
        out[c.find("s:Key", ns).text] = int(c.find("s:Size", ns).text)
    return out


def checksums():
    """MD5 sums from the data set's checksums.md5, keyed by path under alm-3/live/."""
    r = requests.get(f"{BUCKET}/{PREFIX}checksums.md5", timeout=60)
    r.raise_for_status()
    out = {}
    for line in r.text.splitlines():
        parts = line.split()
        if len(parts) == 2:
            out[parts[1]] = parts[0]
    return out


def session_names():
    """The sessions: one per data_structure_<ANM>_<date>.mat file."""
    keys = list_files()
    names = []
    for k in keys:
        m = re.match(r"alm-3/live/data/data_structure_files/data_structure_(ANM\d+_\d+)\.mat$", k)
        if m:
            names.append(m.group(1))
    return sorted(names)


def _first_crossings(x, thr):
    above = x > thr
    return np.flatnonzero(above[1:] & ~above[:-1]) + 1


def _reduce(obj, name):
    tp = obj.trialPropertiesHash
    keys = list(tp.keyNames)
    val = {k: np.asarray(tp.value[i], dtype=float) for i, k in enumerate(keys)}
    types = {str(s): np.asarray(obj.trialTypeMat[i], dtype=bool) for i, s in enumerate(obj.trialTypeStr)}
    trial_ids = np.asarray(obj.trialIds, dtype=int)
    t0 = np.asarray(obj.trialStartTimes, dtype=float)
    n = len(trial_ids)
    s = {
        "name": name,
        "mouse": name.split("_")[0],
        "date": name.split("_")[1],
        "trial_ids": trial_ids,
        "trial_start": t0,
        "pole_in": val["PoleInTime"],
        "pole_out": val["PoleOutTime"],
        "cue": val["CueTime"],
        "good": val["GoodTrials"] == 1,
        "stim_type": val["PhotostimulationType"],
        "trial_types": types,
        "trial_type_names": [str(x) for x in obj.trialTypeStr],
        "trial_property_names": keys,
        "time_unit": int(obj.trialTimeUnit),
    }
    # Lick and laser traces, reduced per trial.
    ts = obj.timeSeriesArrayHash.value
    s["ts_channels"] = [str(x) for x in ts.idStr]
    vm = ts.valueMatrix
    tt = np.asarray(ts.trial, dtype=int)
    tm = np.asarray(ts.time, dtype=float)
    lick = vm[:, list(ts.idStr).index("lick_trace")]
    laser_col = list(ts.idStr).index("laser_power") if "laser_power" in list(ts.idStr) else None
    aom_col = list(ts.idStr).index("aom_input_trace") if "aom_input_trace" in list(ts.idStr) else None
    finite = np.isfinite(lick)
    med = np.median(lick[finite])
    hi = np.percentile(lick[finite], 99.9)
    s["lick_median"], s["lick_p999"] = float(med), float(hi)
    thr = med + 0.5 * (hi - med)
    s["dt_trace"] = float(np.median(np.diff(tm[:1000])))
    order = np.argsort(tt, kind="stable")
    tt_sorted = tt[order]
    bounds = np.searchsorted(tt_sorted, trial_ids, side="left"), np.searchsorted(tt_sorted, trial_ids, side="right")
    first_lick = np.full(n, np.nan)
    first_lick_any = np.full(n, np.nan)
    laser_on = np.full(n, np.nan)
    laser_off = np.full(n, np.nan)
    laser_max = np.full(n, np.nan)
    aom_on = np.full(n, np.nan)
    aom_off = np.full(n, np.nan)
    trace_end = np.full(n, np.nan)
    for i in range(n):
        idx = order[bounds[0][i]:bounds[1][i]]
        if len(idx) == 0:
            continue
        t = tm[idx] - t0[i]
        trace_end[i] = t[-1]
        lk = lick[idx]
        cr = _first_crossings(lk, thr)
        if len(cr):
            first_lick_any[i] = t[cr[0]]
            if np.isfinite(s["cue"][i]):
                after = t[cr][t[cr] > s["cue"][i]]
                if len(after):
                    first_lick[i] = after[0]
        if laser_col is not None:
            L = vm[idx, laser_col]
            if np.nanmax(L) > 0:
                laser_max[i] = np.nanmax(L)
                on = t[L > 0.05 * np.nanmax(L)]
                laser_on[i], laser_off[i] = on[0], on[-1]
        if aom_col is not None:
            A = vm[idx, aom_col]
            if np.nanmax(A) > 0.05:
                on = t[A > 0.05 * np.nanmax(A)]
                aom_on[i], aom_off[i] = on[0], on[-1]
    s.update(first_lick=first_lick, first_lick_any=first_lick_any, laser_on=laser_on, laser_off=laser_off,
             laser_max=laser_max, aom_on=aom_on, aom_off=aom_off, trace_end=trace_end, lick_threshold=thr)
    # Units.
    es = obj.eventSeriesHash
    vals = es.value if isinstance(es.value, np.ndarray) else [es.value]
    units = []
    id_to_index = {int(tid): i for i, tid in enumerate(trial_ids)}
    for k, u in enumerate(vals):
        et = np.atleast_1d(np.asarray(u.eventTimes, dtype=float))
        etr = np.atleast_1d(np.asarray(u.eventTrials, dtype=int))
        wf = np.atleast_2d(np.asarray(u.waveforms, dtype=float))
        mw = wf.mean(axis=0) if wf.size else np.full(29, np.nan)
        trough = int(np.argmin(mw))
        peak = trough + int(np.argmax(mw[trough:]))
        ct = u.cellType
        if isinstance(ct, np.ndarray):
            ct = [str(x) for x in ct.ravel()]
        else:
            ct = [str(ct)] if str(ct) else []
        ti = np.array([id_to_index.get(int(x), -1) for x in etr])
        ok = ti >= 0
        rel = et[ok] - t0[ti[ok]]
        units.append({
            "key": str(np.atleast_1d(es.keyNames)[k]),
            "descr": str(np.atleast_1d(es.descr)[k]),
            "fields": list(u._fieldnames),
            "cell_type": ct,
            "spike_width_ms": (peak - trough) / SAMPLE_RATE_WAVEFORM * 1e3,
            "mean_waveform": mw.astype(np.float32),
            "channel": float(np.median(np.atleast_1d(u.channel))),
            "n_spikes": len(et),
            "n_spikes_outside_trials": int((~ok).sum()),
            "spike_trial_index": ti[ok].astype(np.int32),
            "spike_time": rel.astype(np.float64),
            "first_trial": int(etr.min()) if len(etr) else -1,
            "last_trial": int(etr.max()) if len(etr) else -1,
            "time_unit": int(u.timeUnit),
            "spikes_sorted": bool(np.all(np.diff(et) >= 0)),
        })
    s["units"] = units
    return s


def load_session(name, retries=3):
    """Stream one session file into memory and reduce it."""
    url = f"{BUCKET}/{PREFIX}data/data_structure_files/data_structure_{name}.mat"
    for attempt in range(retries):
        try:
            with fsspec.open(url, "rb", block_size=2**24) as f:
                raw = f.read()
            break
        except Exception:
            if attempt == retries - 1:
                raise
            time.sleep(5)
    obj = sio.loadmat(io.BytesIO(raw), squeeze_me=True, struct_as_record=False)["obj"]
    del raw
    return _reduce(obj, name)


def load_all(names=None, workers=3):
    """Load the sessions, a few at a time in separate processes, in name order."""
    from concurrent.futures import ProcessPoolExecutor
    names = session_names() if names is None else names
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(load_session, names))
EOF
cd $TMPDIR && . v/bin/activate && cat > t3.py <<'EOF'
import sys, time, pickle, resource
sys.path.insert(0,'entries/crcns-alm-3-li-2016')
import alm3
t=time.time()
s=alm3.load_session('ANM257772_20141121')
print(time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
import numpy as np
print(np.unique(s['stim_type'][s['good']],return_counts=True))
g=s['good']&(s['stim_type']==4)
print('laser on-cue', (s['laser_on']-s['pole_out'])[g][:10], (s['laser_off']-s['pole_out'])[g][:10])
print('aom', (s['aom_on']-s['pole_out'])[g][:5], (s['aom_off']-s['pole_out'])[g][:5])
print('lick', s['lick_median'], s['lick_p999'], (s['first_lick']-s['cue'])[s['good']][:20])
print('trace_end-cue', np.nanpercentile(s['trace_end']-s['cue'],[0,50,100]))
print(len(s['units']), [ (u['cell_type'], round(u['spike_width_ms'],2)) for u in s['units']][:20])
EOF
python t3.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/t3.py", line 5, in <module>
    s=alm3.load_session('ANM257772_20141121')
  File "entries/crcns-alm-3-li-2016/alm3.py", line 242, in load_session
    return _reduce(obj, name)
  File "entries/crcns-alm-3-li-2016/alm3.py", line 179, in _reduce
    laser_on[i], laser_off[i] = on[0], on[-1]
                                ~~^^^
IndexError: index 0 is out of bounds for axis 0 with size 0
```

**Agent calls Bash**

```bash
cd entries/crcns-alm-3-li-2016 && python3 - <<'EOF'
p='alm3.py'; s=open(p).read()
s=s.replace("""            L = vm[idx, laser_col]
            if np.nanmax(L) > 0:
                laser_max[i] = np.nanmax(L)
                on = t[L > 0.05 * np.nanmax(L)]""","""            L = vm[idx, laser_col]
            L = np.where(np.isfinite(L), L, 0.0)
            if L.max() > 0:
                laser_max[i] = L.max()
                on = t[L > 0.05 * L.max()]""")
s=s.replace("""            A = vm[idx, aom_col]
            if np.nanmax(A) > 0.05:
                on = t[A > 0.05 * np.nanmax(A)]""","""            A = vm[idx, aom_col]
            A = np.where(np.isfinite(A), A, 0.0)
            if A.max() > 0.05:
                on = t[A > 0.05 * A.max()]""")
open(p,'w').write(s)
EOF
cd $TMPDIR && . v/bin/activate && python t3.py
```

```
6.177186965942383 1.446296
(array([0., 4., 5., 6.]), array([202,  42,  51,  43]))
laser on-cue [ 4.85100e-03  4.50700e-03  4.54100e-03 -6.90554e+00  4.34100e-03
  4.30800e-03  4.57400e-03  4.54000e-03  4.64100e-03  4.50700e-03] [ 0.413751  0.792107  0.791941 -1.90584   0.791941  0.792208  0.792274
  0.79214   0.791941  0.792107]
aom [0.002551 0.002207 0.001941      nan 0.002041] [0.413751 1.300707 1.300641      nan 1.300641]
lick 0.19089097031486615 0.1928261849896049 [           nan 6.74700000e-03 6.14700000e-03 7.54800000e-03
 4.15140000e-02 4.87480000e-02 1.54480000e-02            nan
 3.35100000e-03 1.51140000e-02 1.11810000e-02            nan
 1.69160000e-02 1.39150000e-02            nan 7.54800000e-03
 5.18100000e-03            nan 8.09999999e-05            nan]
trace_end-cue [-8.076881  1.426581  1.427415]
29 [(['pyramidal'], 0.67), (['pyramidal'], 0.61), (['pyramidal'], 0.56), (['pyramidal'], 0.67), (['pyramidal'], 0.61), (['pyramidal'], 0.67), (['FS'], 0.15), (['pyramidal'], 0.61), (['pyramidal'], 0.67), (['pyramidal'], 0.61), (['pyramidal'], 0.61), (['pyramidal'], 0.67), (['pyramidal'], 0.56), (['pyramidal'], 0.61), (['pyramidal'], 0.56), (['pyramidal'], 0.67), (['pyramidal'], 0.61), (['FS'], 0.15), ([], 0.31), (['pyramidal'], 0.61)]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . v/bin/activate && cat > cache.py <<'EOF'
import sys, time, pickle, resource
sys.path.insert(0,'entries/crcns-alm-3-li-2016')
import alm3
t=time.time()
S=alm3.load_all(workers=3)
print(len(S), time.time()-t)
pickle.dump(S, open('sessions.pkl','wb'))
EOF
python cache.py; ls -la sessions.pkl; date -u
```

```
91 125.60261297225952
-rw-r--r-- 1 runner runner 106126424 Nov  7 19:37 sessions.pkl
Sat Nov  7 19:37:34 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . v/bin/activate && cat > survey.py <<'EOF'
import pickle, numpy as np, collections
S=pickle.load(open('sessions.pkl','rb'))
rows=[]
for s in S:
    st=s['stim_type']; g=s['good']
    vals,c=np.unique(st[g & np.isfinite(st)],return_counts=True)
    ct=collections.Counter(tuple(u['cell_type']) for u in s['units'])
    print(s['name'], len(st), int(g.sum()), dict(zip(vals.astype(int).tolist(),c.tolist())), 'nan:',int(np.isnan(st[g]).sum()), 'units',len(s['units']), dict(ct), s['trial_type_names'] if s['trial_type_names']!=['HitR','HitL','ErrR','ErrL','NoLickR','NoLickL','LickEarly','StimTrials'] else '')
print(len(set(s['mouse'] for s in S)),'mice')
EOF
python survey.py
```

```
ANM255200_20140910 288 254 {-3: 34, -2: 32, -1: 31, 0: 157} nan: 0 units 15 {('pyramidal',): 14, ('FS',): 1} 
ANM255200_20140911 340 300 {-3: 38, -2: 35, -1: 36, 0: 191} nan: 0 units 14 {('pyramidal',): 13, (): 1} 
ANM255200_20140912 336 276 {-3: 39, -2: 25, -1: 43, 0: 169} nan: 0 units 20 {('pyramidal',): 17, ('FS',): 2, (): 1} 
ANM255200_20140913 413 388 {0: 235, 1: 58, 2: 46, 3: 49} nan: 0 units 12 {('pyramidal',): 9, ('FS',): 2, (): 1} 
ANM255200_20140914 404 384 {0: 236, 1: 46, 2: 53, 3: 49} nan: 0 units 10 {('FS',): 2, ('pyramidal',): 8} 
ANM255200_20140915 279 263 {0: 166, 1: 33, 2: 34, 3: 30} nan: 0 units 11 {('pyramidal',): 11} 
ANM255200_20140916 354 334 {0: 183, 1: 41, 2: 53, 3: 57} nan: 0 units 2 {('pyramidal',): 2} 
ANM255201_20141120 351 304 {0: 175, 1: 46, 2: 41, 3: 42} nan: 0 units 16 {('pyramidal',): 13, ('FS',): 2, (): 1} 
ANM255201_20141121 270 246 {0: 155, 4: 37, 5: 27, 6: 27} nan: 0 units 17 {('pyramidal',): 16, ('FS',): 1} 
ANM255201_20141122 317 291 {0: 159, 1: 34, 2: 50, 3: 48} nan: 0 units 22 {('pyramidal',): 21, ('FS',): 1} 
ANM255201_20141123 253 209 {0: 133, 4: 21, 5: 16, 6: 39} nan: 0 units 29 {(): 1, ('FS',): 6, ('pyramidal',): 22} 
ANM255201_20141124 319 271 {0: 161, 1: 32, 2: 35, 3: 43} nan: 0 units 12 {('FS',): 2, ('pyramidal',): 10} 
ANM255201_20141125 230 190 {0: 120, 1: 28, 2: 18, 3: 24} nan: 0 units 16 {('pyramidal',): 15, ('FS',): 1} 
ANM255203_20141112 211 138 {0: 85, 1: 17, 2: 16, 3: 20} nan: 0 units 35 {('pyramidal',): 30, ('FS',): 2, (): 3} 
ANM255203_20141113 233 58 {0: 28, 1: 7, 2: 10, 3: 13} nan: 0 units 24 {('pyramidal',): 21, ('FS',): 2, (): 1} 
ANM255203_20141114 306 246 {0: 144, 1: 35, 2: 41, 3: 26} nan: 0 units 22 {('pyramidal',): 19, ('FS',): 2, (): 1} 
ANM255203_20141115 347 173 {0: 101, 1: 24, 2: 19, 3: 29} nan: 0 units 8 {('pyramidal',): 7, (): 1} 
ANM255203_20141116 304 249 {0: 145, 1: 41, 2: 30, 3: 33} nan: 0 units 16 {('pyramidal',): 13, (): 2, ('FS',): 1} 
ANM257636_20150330 249 159 {0: 87, 4: 24, 5: 27, 7: 2
[... 74 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/scripts; grep -n "animals_list\|ANM\|i_yes_trial = find\|i_no_trial = find\|stim1 = find\|Photostim_type==\|length(i_yes_trial)>\|%% \|i_selective =\|i_n_trial =\|i_cell =\|t_recovered = \|T_recovery(i\|mean(T_recovery)\|func_getPSTH\|randsample" analysis_compile_all_data_bilateral.m | head -120
```

```
7:%% list of animals to analyze
8:animals_list = {
10:    'ANM255201';...  % ReachR
11:    'ANM257772';...  % ReachR
12:    'ANM258250';...  % VGAT
14:    'ANM257637';...  % VGAT
15:    'ANM264411';...  % VGAT
17:    'ANM263808';...  % ReachR
18:    'ANM263810';...  % ReachR
23:    %% establish variables to compute and save
52:    %% go through the files and compute the variables
53:    n_animals = length(animals_list);
61:        file_list = dir([dir_tmp, 'data_structure_', animals_list{i_animal},'_*.mat']);
62:        file_meta_data_list = dir([dir_tmp, 'meta_data_', animals_list{i_animal},'_*.mat']);
70:            disp([animals_list{i_animal},'  File #',num2str(i_file),'/',num2str(n_file)]);
77:            animal_ID{n_file_count,1} = animals_list{i_animal};
167:                i_yes_trial = find((HitR==1 | ErrR==1) & Photostim_type==0 & unit_stable_trials_tmp==1 & LickEarly==0 & GoodTrials==1);
168:                i_no_trial = find((HitL==1 | ErrL==1) & Photostim_type==0 & unit_stable_trials_tmp==1 & LickEarly==0 & GoodTrials==1);
170:                i_yes_trial_ipsi = find((HitR==1 | ErrR==1) & Photostim_type==4 & unit_stable_trials_tmp==1 & LickEarly==0 & GoodTrials==1);
171:                i_no_trial_ipsi = find((HitL==1 | ErrL==1) & Photostim_type==4 & unit_stable_trials_tmp==1 & LickEarly==0 & GoodTrials==1);
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/scripts; cat func_getPSTH.m func_getPSTH_smallBin.m func_discriminant.m; sed -n 180,200p analysis_compile_all_data_bilateral.m; sed -n 495,560p analysis_compile_all_data_bilateral.m; sed -n 940,1200p analysis_compile_all_data_bilateral.m
```

```
function [PSTH time] = func_getPSTH(SpikeTimes, PSTH_StartTime, PSTH_EndTime)

% 
% SpikeTimes -- {n_rep,1}
% 

if nargin == 1
    PSTH_StartTime = -.52;
    PSTH_EndTime = 5.020;
end

time = PSTH_StartTime:.001:PSTH_EndTime;


n_rep = size(SpikeTimes,1);
total_counts = 0;
for i_rep = 1:n_rep
    
    [counts] = hist(SpikeTimes{i_rep,1},PSTH_StartTime:0.001:PSTH_EndTime);
    total_counts = total_counts+counts/n_rep;
[... 188 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR/scripts; grep -n "animals_list = \|'ANM\|>=\|>5\|> 5\|%% \|roc\|ROC\|auc\|i_t_\|t_bin\|t_window\|cd_\|w_t\|mode\b\|Gram\|svd\|decision\|boundary\|offset\|randsample\|i_t\b" analysis_compile_all_data_bilateral_activityModes.m | head -150
```

```
Sat Nov  7 19:38:01 UTC 2026
7:%% list of animals to analyze
8:animals_list = {
10:    'ANM255201';...  % ReachR
11:    'ANM257772';...  % ReachR
12:    'ANM258250';...  % VGAT
14:    'ANM257637';...  % VGAT
15:    'ANM264411';...  % VGAT
17:    'ANM263808';...  % ReachR
18:    'ANM263810';...  % ReachR
23:    %% establish variables to compute and save    
57:    %% go through the files and compute the variables
133:            %     '"1"--  Left ALM (ipsilateral); Sample; 1 spot, 500ms (100ms ramp offset);';...
134:            %     '"2"--  Left ALM (ipsilateral); Early delay; 1 spot, 500ms (100ms ramp offset);';...
135:            %     '"3"--  Left ALM (ipsilateral); Middle delay; 1 spot, 500ms (100ms ramp offset);';...
137:            %     '"-1"-- Left ALM (ipsilateral); Sample; 1 spot, 500ms (No ramp offset, DO NOT ANALYZE);';...
138:            %     '"-2"-- Left ALM (ipsilateral); Early delay; 1 spot, 500ms (No ramp offset, DO NOT ANALYZE);';...
139:            %     '"-3"-- Left ALM (ipsilateral); Middle delay; 1 spot, 500ms (No ramp offset, DO NOT ANALYZE);';...
141:            %     '"4"--  Left ALM (ipsilateral); Early delay; 1 spot, 800ms (200ms ramp offset);';...
142:            %     '"5"--  Right ALM (contralateral); Early delay; 1 spot, 800ms (200ms ramp offset);';...
[... 132 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/scripts; sed -n 158,450p analysis_compile_all_data_bilateral_activityModes.m
```

```
% -------------- process single unit data --------------
            neuron_list = [];
            population_stable_trials = [];
            for i_unit = 1:length(obj.eventSeriesHash.value)
                
                unit = obj.eventSeriesHash.value{i_unit};
                
                % ---------- trial selection -----------------
                % index stable trials
                unit_stable_trials_tmp = zeros(trialID(end),1);
                i_stable_trials = min(unit.eventTrials):min([max(unit.eventTrials) trialID(end)]);
                unit_stable_trials_tmp(i_stable_trials) = 1;
                
                if unit_stable_trials_tmp(end-50)==1 & unit_stable_trials_tmp(50)==1 & (sum(strcmp(unit.cellType,'pyramidal'))>0 & sum(strcmp(unit.cellType,'FS'))==0)
                    neuron_list(end+1) = i_unit;
                    population_stable_trials(end+1,:) = unit_stable_trials_tmp;
                end
                
            end
            population_stable_trials_tmp = (sum(population_stable_trials)==size(population_stable_trials,1))';
[... 274 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/scripts; grep -n -i "perfcurve\|auc\|roc\|ranksum\|signrank\|ttest\|corr(\|explained\|var(\|sqrt(mean" *.m | grep -v "^analysis_compile_all_data_unilateral.m.*ttest2\|bilateral.m.*ttest2" | head -60
```

```
Gram_Schmidt_process.m:1:function orthonormal_basis = Gram_Schmidt_process(A)
Gram_Schmidt_process.m:3:% Gram-Schmidt Process
Gram_Schmidt_process.m:5:% Gram_Schmidt_process(A) produces an orthonormal basis for the subspace of
analysis_compile_all_data_bilateral.m:152:            % -------------- process single unit data --------------
analysis_compile_all_data_bilateral.m:681:                        error('cell type could not be processed')
analysis_compile_all_data_bilateralCCX.m:150:            % -------------- process single unit data --------------
analysis_compile_all_data_bilateralCCX.m:210:                        sample_selective = ttest2(spk_count_yes,spk_count_no);
analysis_compile_all_data_bilateralCCX.m:228:                        delay_selective = ttest2(spk_count_yes,spk_count_no);
analysis_compile_all_data_bilateralCCX.m:246:                        response_selective = ttest2(spk_count_yes,spk_count_no);
analysis_compile_all_data_bilateralCCX.m:336:                            [h p] = ttest2(spk_count_tmp(i_nonstim),spk_count_tmp(i_stim));
analysis_compile_all_data_bilateralCCX.m:408:                            [h p] = ttest2(spk_count_tmp(i_nonstim),spk_count_tmp(i_stim));
analysis_compile_all_data_bilateralCCX.m:480:                            [h p] = ttest2(spk_count_tmp(i_nonstim),spk_count_tmp(i_stim));
analysis_compile_all_data_bilateralCCX.m:679:                        error('cell type could not be processed')
analysis_compile_all_data_bilateralCCX_FR.m:159:            % -------------- process single unit data --------------
analysis_compile_all_data_bilateralCCX_FR.m:442:                        sig_yes_ipsi(n_unit,:) = ttest2(spk_count_yes,spk_count_yes_ipsi);
analysis_compile_all_data_bilateralCCX_FR.m:443:                        sig_no_ipsi(n_unit,:) = ttest2(spk_count_no,spk_count_no_ipsi);
analysis_compile_all_data_bilateralCCX_FR.m:500:                        sig_yes_contra(n_unit,:) = ttest2(spk_count_yes,spk_count_yes_contra);
analysis_c
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/scripts; sed -n 1090,1330p analysis_compile_all_data_bilateral_activityModes.m
```

```
ylim([-8 8])





%% variance in unperturbed responses captured by each mode,  Extended Data Fig 8
var_final_modes_all = [];
for i_session = 1:size(activity_matrix_allSession,1)
    
    activity_matrix_tmp = activity_matrix_allSession{i_session};
    i_yes_training_trial_tmp = i_yes_training_allSession{i_session};
    i_no_training_trial_tmp = i_no_training_allSession{i_session};
    
    
    i_timebin = find(time_bins>-3 & time_bins<=-.4);
    R = mean(activity_matrix_tmp(:,i_timebin,i_yes_training_trial_tmp),3);
    L = mean(activity_matrix_tmp(:,i_timebin,i_no_training_trial_tmp),3);
    activityRL = [R L];
    i_timebin = find(time_bins<=-3.4);
[... 222 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/scripts; grep -n "length(i_yes_trial)>=\|Photostim_type==1[012]\|i_selective =\|i_n_trial =\|i_cell =\|t_recovered = t(" analysis_compile_all_data_bilateralCCX.m analysis_compile_all_data_bilateral_FR.m analysis_compile_all_data_bilateralCCX_FR.m | head -40; grep -n "animals_list = {" -A12 analysis_compile_all_data_bilateralCCX.m | head -14; cd $TMPDIR && . v/bin/activate && python -c "
import pickle,numpy as np
S=pickle.load(open('sessions.pkl','rb'))
print(all((s['trial_ids']==np.arange(1,len(s['trial_ids'])+1)).all() for s in S))
"
```

```
analysis_compile_all_data_bilateralCCX.m:168:                i_yes_trial_ipsi = find((HitR==1 | ErrR==1) & Photostim_type==10 & unit_stable_trials_tmp==1 & LickEarly==0 & GoodTrials==1);
analysis_compile_all_data_bilateralCCX.m:169:                i_no_trial_ipsi = find((HitL==1 | ErrL==1) & Photostim_type==10 & unit_stable_trials_tmp==1 & LickEarly==0 & GoodTrials==1);
analysis_compile_all_data_bilateralCCX.m:171:                i_yes_trial_contra = find((HitR==1 | ErrR==1) & Photostim_type==11 & unit_stable_trials_tmp==1 & LickEarly==0 & GoodTrials==1);
analysis_compile_all_data_bilateralCCX.m:172:                i_no_trial_contra = find((HitL==1 | ErrL==1) & Photostim_type==11 & unit_stable_trials_tmp==1 & LickEarly==0 & GoodTrials==1);
analysis_compile_all_data_bilateralCCX.m:174:                i_yes_trial_bilat = find((HitR==1 | ErrR==1) & Photostim_type==12 & unit_stable_trials_tmp==1 & LickEarly==0 & GoodTrials==1);
analysis_compile_all_data_bilateralCCX.m:175:                i_no_trial_bilat = find((HitL==1 | ErrL==1) & Photostim_type==12 & unit_stable_trials_tmp==1 & LickEarly==0 & GoodTrials==1);
analysis_compile_all_data_bilateralCCX.m:180:                if length(i_yes_trial)>=15 & length(i_no_trial)>=15
analysis_compile_all_data_bilateralCCX.m:719:i_cell = (cellType_all(:,1)==1 & FR_mean_all>1);
analysis_compile_all_data_bilateralCCX.m:720:i_n_trial = (N_trials_all(:,1)>8 & N_trials_all(:,2)>8 & N_trials_all(:,3)>3 & N_trials_all(:,4)>3);
analysis_compile_all_data_bilateralCCX.m:753:i_n_trial = (N_trials_all(:,1)>8 & N_trials_all(:,2)>8 & N_trials_all(:,5)>3 & N_trials_all(:,6)>3);
analysis_compile_all_data_bilateralCCX.m:782:i_n_trial = (N_trials_all(:,1)>8 & N_trials_all(:,2)>8 & N_trials_all(:,7)>3 & N_trials_all(:,8)>3);
analysis_compile_all_data_bilateralCCX.m:830:i_selective = (sig_selective(:,1)|sig_selective(:,2)) & cellType_all(:,1)==1 & abs(FR_pref(:,1))>1;
analysis_compile_all_data_bilateralCCX.m:831:i_n_trial = N_trials_all(:,1)>5 & N_tria
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/scripts; sed -n 160,200p analysis_compile_all_data_bilateral_FR.m; sed -n 400,450p analysis_compile_all_data_bilateral_FR.m; sed -n 615,660p analysis_compile_all_data_bilateral_FR.m; sed -n 790,860p analysis_compile_all_data_bilateral_FR.m
```

```
% -------------- process single unit data --------------
            for i_unit = 1:length(obj.eventSeriesHash.value)
                
                unit = obj.eventSeriesHash.value{i_unit};
                
                
                % ---------- trial selection -----------------
                % index stable trials
                unit_stable_trials_tmp = zeros(trialID(end),1);
                i_stable_trials = min(unit.eventTrials):min([max(unit.eventTrials) trialID(end)]);
                unit_stable_trials_tmp(i_stable_trials) = 1;
                
                
                
                % index the behavioral trials
                i_control = find(Photostim_type==0 & unit_stable_trials_tmp==1 & LickEarly==0 & GoodTrials==1);
                i_ipsi = find(Photostim_type==4 & unit_stable_trials_tmp==1 & LickEarly==0 & GoodTrials==1);
                i_contra = find(Photostim_type==5 & unit_stable_trials_tmp==1 & LickEarly==0 & GoodTrials==1);
                i_bilat = find(Photostim_type==6 & unit_stable_trials_tmp==1 & LickEarly==0 & GoodTrials==1);
                
[... 145 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-alm-3-li-2016 && python3 - <<'EOF'
p='alm3.py'; s=open(p).read()
s=s.replace("""- PSTH: spike counts in 200 ms windows moved in 1 ms steps... see `psth`, which follows
  func_getPSTH.m of the code.""","""- PSTH (`psth`): mean spike rate in a 200 ms boxcar centred on each time point, as
  func_getPSTH.m of the code (1 ms bins convolved with a 200 ms window); it is evaluated here
  every 5 ms, a sampling step that cannot change a recovery time by more than 5 ms (a standard
  choice).
- Rate test (`rate_pvalues`): two-tailed t-test of spike counts in 400 ms windows centred every
  50 ms from 3 s before to 2 s after the cue, control against photoinhibition trials, lick right
  and lick left pooled (Methods, Electrophysiology data analysis; code, "t-test on firing rate").""")
s += '''

# ---------------------------------------------------------------- experiments and trials

def experiment(s):
    """The experiment a session belongs to, from the photostimulus types it holds.

    unilateral: types 1 to 3 (or -1 to -3); exp2: types 4, 5, 6 (ipsilateral 1 spot,
    contralateral 1 spot, bilateral 4 spots, Experiment 2 of the Methods); exp2b: types 4, 5, 7;
    exp3: types 7, 8, 9 (Experiment 3); ccx: types 10 to 12 (callosotomy).
    """
    st = set(np.unique(s["stim_type"][s["good"] & np.isfinite(s["stim_type"])]).astype(int).tolist())
    if st & {10, 11, 12} or s["mouse"] in CCX_MICE:
        return "ccx"
    if st & {1, 2, 3, -1, -2, -3}:
        return "unilateral"
    if st & {8, 9}:
        return "exp3"
    if 6 in st:
        return "exp2"
    if 7 in st:
        return "exp2b"
    return "none"


# The seven callosotomy mice, named in analysis_compile_all_data_bilateralCCX.m (code); their
# sessions are also the only ones with photostimulus types 10 to 12.
CCX_MICE = {"ANM278733", "ANM270340", "ANM298738", "ANM298740", "ANM291063", "ANM291064", "ANM297634"}

# Mouse lines, from the comments of the code's animal lists (analysis_compile_all_data_*.m); the
# data files do not say which line a mouse is.
MOUSE_LINE = {
    "ANM255200": "PV x ReaChR", "ANM255201": "PV x ReaChR", "ANM255203": "PV x ReaChR",
    "ANM257772": "PV x ReaChR", "ANM258250": "VGAT-ChR2", "ANM257637": "VGAT-ChR2",
    "ANM264411": "VGAT-ChR2", "ANM263808": "PV x ReaChR", "ANM263810": "PV x ReaChR",
    "ANM278733": "VGAT-ChR2", "ANM270340": "VGAT-ChR2", "ANM298738": "VGAT-ChR2",
    "ANM298740": "VGAT-ChR2", "ANM291063": "VGAT-ChR2", "ANM291064": "VGAT-ChR2",
    "ANM297634": "PV x ReaChR",
}


def side(s):
    """+1 for instructed lick right (HitR, ErrR, NoLickR), -1 for lick left, 0 otherwise."""
    tt = s["trial_types"]
    r = tt["HitR"] | tt["ErrR"] | tt.get("NoLickR", False)
    l = tt["HitL"] | tt["ErrL"] | tt.get("NoLickL", False)
    return np.where(r, 1, np.where(l, -1, 0))


def base_trials(s, include_lick_early=False):
    """Trials usable for analysis: performing (GoodTrials), with epoch times, a response
    (correct or error), and, unless asked otherwise, not lick-early (code; FAQ of the data set)."""
    tt = s["trial_types"]
    ok = s["good"] & np.isfinite(s["cue"]) & np.isfinite(s["pole_in"]) & np.isfinite(s["pole_out"])
    ok &= tt["HitR"] | tt["ErrR"] | tt["HitL"] | tt["ErrL"]
    if not include_lick_early:
        ok &= ~tt["LickEarly"]
    return ok


def stable_trials(s, u):
    """The unit's stable trials: from its first to its last trial with a spike (code)."""
    ids = s["trial_ids"]
    return (ids >= u["first_trial"]) & (ids <= u["last_trial"])


# ---------------------------------------------------------------- spike counts

T0, T1 = -3.6, 2.3  # s from the go cue; 1 ms bins
NB = int(round((T1 - T0) * 1000))


def cum_counts(s, u, trials):
    """Cumulative 1 ms spike counts, cue aligned, for the given trial indices: (n, NB + 1)."""
    trials = np.asarray(trials, dtype=int)
    row = np.full(len(s["trial_ids"]), -1)
    row[trials] = np.arange(len(trials))
    ti = u["spike_trial_index"]
    r = row[ti]
    keep = r >= 0
    t = u["spike_time"][keep] - s["cue"][ti[keep]]
    r = r[keep]
    b = np.floor((t - T0) * 1000).astype(int)
    ok = (b >= 0) & (b < NB)
    M = np.zeros((len(trials), NB), dtype=np.int32)
    np.add.at(M, (r[ok], b[ok]), 1)
    C = np.zeros((len(trials), NB + 1), dtype=np.int32)
    np.cumsum(M, axis=1, out=C[:, 1:])
    return C


def window_counts(C, start, stop):
    """Spike counts in [start, stop) s from the cue, per trial; start and stop may be arrays."""
    a = np.clip(np.round((np.asarray(start) - T0) * 1000).astype(int), 0, NB)
    b = np.clip(np.round((np.asarray(stop) - T0) * 1000).astype(int), 0, NB)
    if a.ndim == 0:
        return C[:, b] - C[:, a]
    return C[np.arange(len(C)), b] - C[np.arange(len(C)), a]


PSTH_T = np.round(np.arange(-3.4, 2.0 + 1e-9, 0.005), 3)


def psth(C, width=0.2, times=PSTH_T):
    """Mean rate (spikes/s) in a boxcar of `width` s centred on each time, over the trials of C."""
    if len(C) == 0:
        return np.full(len(times), np.nan)
    a = np.round((times - width / 2 - T0) * 1000).astype(int)
    b = np.round((times + width / 2 - T0) * 1000).astype(int)
    return (C[:, b] - C[:, a]).mean(axis=0) / width


RATE_T = np.round(np.arange(-3.0, 2.0 + 1e-9, 0.05), 3)


def rate_pvalues(C_ctrl, C_stim, times=RATE_T, width=0.4):
    """Two-tailed t-test p-value per window (counts in `width` s centred on each time)."""
    from scipy import stats
    a = np.round((times - width / 2 - T0) * 1000).astype(int)
    b = np.round((times + width / 2 - T0) * 1000).astype(int)
    x = C_ctrl[:, b] - C_ctrl[:, a]
    y = C_stim[:, b] - C_stim[:, a]
    with np.errstate(invalid="ignore", divide="ignore"):
        p = stats.ttest_ind(x, y, axis=0).pvalue
    return p


def epoch_rates(s, C, trials):
    """Rates (spikes/s) in the sample, delay and response epochs for each trial of C.

    Response epoch: the 1.3 s after the cue (code). Epoch bounds per trial from the trial table.
    """
    cue = s["cue"][trials]
    pin = s["pole_in"][trials] - cue
    pout = s["pole_out"][trials] - cue
    sample = window_counts(C, pin, pout) / (pout - pin)
    delay = window_counts(C, pout, np.zeros_like(pout)) / (-pout)
    resp = window_counts(C, 0.0, 1.3) / 1.3
    return np.vstack([sample, delay, resp]).T


def recovery_time(sel_ctrl, sel_stim, times, t_off, t_end, rng, n_boot=1000, frac=0.2):
    """Bootstrap recovery time of selectivity (code, Fig. 1g and 2e sections).

    sel_ctrl, sel_stim: neurons x time selectivity (preferred minus non-preferred) on control
    and photoinhibition trials. For each bootstrap resample of neurons, the first time after
    photoinhibition offset `t_off` (and before `t_end`) at which the mean of (control minus
    photoinhibition) over the mean control selectivity is below `frac` (i.e. 80% recovered).
    Returns (mean, std over resamples, fraction of resamples that recover), times from offset.
    """
    n = len(sel_ctrl)
    win = (times > t_off) & (times < t_end)
    out = []
    for _ in range(n_boot):
        i = rng.integers(0, n, n)
        r = (sel_ctrl[i] - sel_stim[i]).mean(0) / sel_ctrl[i].mean(0)
        hit = np.flatnonzero((r < frac) & win)
        out.append(times[hit[0]] - t_off if len(hit) else np.nan)
    out = np.array(out)
    ok = np.isfinite(out)
    if not ok.any():
        return np.nan, np.nan, 0.0
    return float(out[ok].mean()), float(out[ok].std(ddof=1)), float(ok.mean())
'''
open(p,'w').write(s)
EOF
date -u
```

```
Sat Nov  7 19:39:33 UTC 2026
```

**Agent calls Bash**

```bash
cat >> alm3.py <<'EOF'


# ---------------------------------------------------------------- per-session tables

BIN = 0.01  # s; counts are kept in 10 ms bins from T0 to T1 (cue aligned)
NB10 = int(round((T1 - T0) / BIN))
BIN_T = np.round(T0 + BIN * np.arange(NB10 + 1), 3)  # bin edges


def trial_table(s):
    """One row per trial with its side, outcome, photostimulus type and epoch times."""
    import pandas as pd
    tt = s["trial_types"]
    return pd.DataFrame({
        "session": s["name"], "mouse": s["mouse"], "trial": np.arange(len(s["trial_ids"])),
        "side": side(s), "hit": tt["HitR"] | tt["HitL"], "err": tt["ErrR"] | tt["ErrL"],
        "nolick": tt.get("NoLickR", np.zeros(len(side(s)), bool)) | tt.get("NoLickL", np.zeros(len(side(s)), bool)),
        "lick_early": tt["LickEarly"], "good": s["good"], "stim": s["stim_type"],
        "pole_in": s["pole_in"], "pole_out": s["pole_out"], "cue": s["cue"],
        "laser_on": s["laser_on"], "laser_off": s["laser_off"], "laser_max": s["laser_max"],
        "first_lick": s["first_lick"],
    })


def reduce_units(s):
    """Per unit: 10 ms binned counts and epoch rates on the session's usable trials.

    The trials kept are base_trials(s, include_lick_early=True), so that lick-early trials can be
    shown as a reading; `lick_early` marks them. `stable` marks the unit's stable trials.
    """
    trials = np.flatnonzero(base_trials(s, include_lick_early=True))
    out = []
    for k, u in enumerate(s["units"]):
        C = cum_counts(s, u, trials)
        edges = np.round((BIN_T - T0) * 1000).astype(int)
        binned = np.diff(C[:, edges], axis=1).astype(np.uint8 if C[:, -1].max() < 255 else np.uint16)
        out.append({
            "session": s["name"], "mouse": s["mouse"], "unit": k, "experiment": experiment(s),
            "cell_type": "pyramidal" if u["cell_type"] == ["pyramidal"] else ("FS" if u["cell_type"] == ["FS"] else ("none" if not u["cell_type"] else "/".join(u["cell_type"]))),
            "spike_width_ms": u["spike_width_ms"], "n_spikes": u["n_spikes"], "channel": u["channel"],
            "trials": trials, "stable": stable_trials(s, u)[trials], "binned": binned,
            "epoch_rates": epoch_rates(s, C, trials),
            "response_rate_1p5": window_counts(C, 0.0, 1.5) / 1.5,
        })
    return out
EOF
cd $TMPDIR && . v/bin/activate && cat > red.py <<'EOF'
import sys, time, pickle, resource
sys.path.insert(0,'entries/crcns-alm-3-li-2016')
import importlib, alm3
S=pickle.load(open('sessions.pkl','rb'))
t=time.time()
U=[]
for s in S: U+=alm3.reduce_units(s)
print(len(U), time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
pickle.dump(U, open('units.pkl','wb'))
EOF
python red.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/red.py", line 7, in <module>
    for s in S: U+=alm3.reduce_units(s)
                   ~~~~~~~~~~~~~~~~~^^^
  File "entries/crcns-alm-3-li-2016/alm3.py", line 456, in reduce_units
    binned = np.diff(C[:, edges], axis=1).astype(np.uint8 if C[:, -1].max() < 255 else np.uint16)
                                                             ~~~~~~~~~~~~^^
  File "/tmp/claude-1001/v/lib/python3.13/site-packages/numpy/_core/_methods.py", line 41, in _amax
    return umr_maximum(a, axis, None, out, keepdims, initial, where)
ValueError: zero-size array to reduction operation maximum which has no identity
```

**Agent calls Bash**

```bash
sed -i 's/        binned = np.diff(C\[:, edges\], axis=1).astype(np.uint8 if C\[:, -1\].max() < 255 else np.uint16)/        binned = np.diff(C[:, edges], axis=1)\n        assert binned.size == 0 or binned.max() < 256\n        binned = binned.astype(np.uint8)/' alm3.py && cd $TMPDIR && . v/bin/activate && python red.py && ls -la units.pkl
```

```
1579 2.2045443058013916 0.443828
-rw-r--r-- 1 runner runner 246256009 Nov  7 19:40 units.pkl
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . v/bin/activate && cat > a1.py <<'EOF'
import sys, pickle, numpy as np, pandas as pd
sys.path.insert(0,'entries/crcns-alm-3-li-2016')
import alm3
S=pickle.load(open('sessions.pkl','rb')); U=pickle.load(open('units.pkl','rb'))
SD={s['name']:s for s in S}
df=pd.DataFrame([{k:u[k] for k in ['session','mouse','unit','experiment','cell_type','spike_width_ms','n_spikes']} for u in U])
print(df.groupby('experiment').agg(n=('unit','size'), sessions=('session','nunique'), mice=('mouse','nunique')))
nc=df[df.experiment!='ccx']
print('non-ccx units', len(nc), nc.cell_type.value_counts().to_dict(), 'sessions', nc.session.nunique(), 'mice', nc.mouse.nunique())
cc=df[df.experiment=='ccx']; print('ccx', len(cc), cc.cell_type.value_counts().to_dict())
df['wclass']=np.where(df.spike_width_ms>0.45,'pyramidal',np.where(df.spike_width_ms<0.35,'FS','none'))
print(pd.crosstab(df.cell_type, df.wclass))
print(df.groupby('cell_type').spike_width_ms.describe())
# code inclusion: >=8 control trials per side (unilateral), >=15 (bilateral)
def ntr(u):
    s=SD[u['session']]; sd=alm3.side(s)[u['trials']]; st=s['stim_type'][u['trials']]; le=s['trial_types']['LickEarly'][u['trials']]
    m=u['stable']&~le&(st==0)
    return (m&(sd==1)).sum(), (m&(sd==-1)).sum()
df[['nR','nL']]=[ntr(u) for u in U]
for thr in [8,15]:
    d=nc[(df.loc[nc.index,'nR']>=thr)&(df.loc[nc.index,'nL']>=thr)]
    print(thr, len(d), d.cell_type.value_counts().to_dict())
EOF
python a1.py
```

```
n  sessions  mice
experiment                     
ccx         567        33     7
exp2        488        26     7
exp2b        88         6     3
exp3        102         6     3
unilateral  334        20     4
non-ccx units 1012 {'pyramidal': 890, 'FS': 89, 'none': 33} sessions 58 mice 12
ccx 567 {'pyramidal': 519, 'FS': 45, 'none': 3}
wclass     FS  none  pyramidal
cell_type                     
FS         89    45          0
none       24    10          2
pyramidal   0     0       1409
            count      mean       std     min     25%     50%     75%     max
cell_type                                                                    
FS          134.0  0.270519  0.072574  0.1536  0.2048  0.2560  0.3584  0.3584
none         36.0  0.347022  0.068267  0.3072  0.3072  0.3072  0.4096  0.5632
pyramidal  1409.0  0.746706  0.117855  0.4608  0.6656  0.6656  0.8704  0.9216
8 1008 {'pyramidal': 887, 'FS': 88, 'none': 33}
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . v/bin/activate && cat >> a1.py <<'EOF'
print(pd.crosstab(nc.cell_type, df.loc[nc.index,'wclass']))
print(sorted(df.spike_width_ms.round(4).unique()))
EOF
python a1.py | tail -12
```

```
cell_type                                                                    
FS          134.0  0.270519  0.072574  0.1536  0.2048  0.2560  0.3584  0.3584
none         36.0  0.347022  0.068267  0.3072  0.3072  0.3072  0.4096  0.5632
pyramidal  1409.0  0.746706  0.117855  0.4608  0.6656  0.6656  0.8704  0.9216
8 1008 {'pyramidal': 887, 'FS': 88, 'none': 33}
15 981 {'pyramidal': 862, 'FS': 87, 'none': 32}
wclass     FS  none  pyramidal
cell_type                     
FS         74    15          0
none       24     9          0
pyramidal   0     0        890
[np.float64(0.1536), np.float64(0.2048), np.float64(0.256), np.float64(0.3072), np.float64(0.3584), np.float64(0.4096), np.float64(0.4608), np.float64(0.512), np.float64(0.5632), np.float64(0.6144), np.float64(0.6656), np.float64(0.7168), np.float64(0.768), np.float64(0.8192), np.float64(0.8704), np.float64(0.9216)]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/dev && cat > $TMPDIR/dev/run.py <<'EOF'
"""Dev runner: execute nb.py cells, replacing the loading cell by the cached pickle.
usage: python run.py nb.py [first_cell_substring ...]  runs cells whose text matches, after setup."""
import sys, re, pickle, time
src=open(sys.argv[1]).read()
cells=re.split(r'^# %%.*$', src, flags=re.M)
g={}
sys.path.insert(0,'entries/crcns-alm-3-li-2016')
import pickle
for i,c in enumerate(cells):
    if 'LOAD-CELL' in c:
        c = "import pickle\nsessions=pickle.load(open('/tmp/claude-1001/sessions.pkl','rb'))\nunits=pickle.load(open('/tmp/claude-1001/units.pkl','rb'))\n"
    if i>0 and len(sys.argv)>2 and not any(k in c for k in sys.argv[2:]) and 'SETUP' not in c and 'LOAD-CELL' not in cells[i]:
        continue
    t=time.time()
    exec(compile(c, f'cell{i}', 'exec'), g)
    print(f'--- cell {i} {time.time()-t:.1f}s', file=sys.stderr)
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cat >> entries/crcns-alm-3-li-2016/alm3.py <<'EOF'


# ---------------------------------------------------------------- per-unit measures from 10 ms bins

GRID_T = np.round(np.arange(-3.5, 2.2 + 1e-9, 0.01), 3)  # time points for rates and PSTHs


def binned_window(binned, times, width):
    """Counts in windows of `width` s centred on `times` (multiples of 10 ms), per trial."""
    cs = np.zeros((binned.shape[0], binned.shape[1] + 1), dtype=np.int32)
    np.cumsum(binned, axis=1, out=cs[:, 1:])
    a = np.round((np.asarray(times) - width / 2 - T0) / BIN).astype(int)
    b = np.round((np.asarray(times) + width / 2 - T0) / BIN).astype(int)
    return cs[:, b] - cs[:, a]


def unit_measures(u, s, n_screen, conditions, seed, width_psth=0.2):
    """Measures of one unit used by the selectivity and rate analyses (code; see module doc).

    n_screen: control trials per side drawn at random to set the preferred trial type (5 in the
    unilateral code, 10 in the bilateral and callosotomy code; the Methods say "a subset of 10
    trials"). Preference from the spike count from sample onset to 1.3 s after the cue (code,
    first column of spk_count_*_screen). Selectivity traces on the remaining control trials.
    """
    from scipy import stats
    tr = u["trials"]
    sd = side(s)[tr]
    st = s["stim_type"][tr]
    le = s["trial_types"]["LickEarly"][tr]
    hit = (s["trial_types"]["HitR"] | s["trial_types"]["HitL"])[tr]
    ok = u["stable"] & ~le
    b = u["binned"]
    ctrl = ok & (st == 0)
    iR, iL = np.flatnonzero(ctrl & (sd == 1)), np.flatnonzero(ctrl & (sd == -1))
    out = {"nR": len(iR), "nL": len(iL)}
    rate = binned_window(b, GRID_T, width_psth) / width_psth
    out["fr_mean"] = float(binned_window(b[np.r_[iR, iL]], [-0.5], 5.0).mean() / 5.0) if len(iR) + len(iL) else np.nan
    rng = np.random.default_rng(seed)
    if len(iR) > n_screen and len(iL) > n_screen:
        pR, pL = rng.permutation(iR), rng.permutation(iL)
        sR, sL, tR, tL = pR[:n_screen], pL[:n_screen], pR[n_screen:], pL[n_screen:]
        er = u["epoch_rates"]
        cue = s["cue"][tr]
        whole = (s["pole_in"][tr] - cue)
        # spike count from sample onset to 1.3 s after the cue: the rates times epoch lengths
        dur = np.vstack([s["pole_out"][tr] - s["pole_in"][tr], cue - s["pole_out"][tr], np.full(len(tr), 1.3)]).T
        counts = er * dur
        whole_count = counts.sum(1)
        out["pref_counts"] = np.r_[whole_count[sR].mean() - whole_count[sL].mean(), (counts[sR].mean(0) - counts[sL].mean(0))]
        out["psth_ctrl"] = {1: rate[tR].mean(0), -1: rate[tL].mean(0)}
        out["n_test"] = (len(tR), len(tL))
    else:
        out["pref_counts"] = None
    out["psth_ctrl_all"] = {1: rate[iR].mean(0) if len(iR) else None, -1: rate[iL].mean(0) if len(iL) else None}
    out["cond"] = {}
    for c in conditions:
        m = ok & (st == c)
        cR, cL = np.flatnonzero(m & (sd == 1)), np.flatnonzero(m & (sd == -1))
        d = {"nR": len(cR), "nL": len(cL),
             "psth": {1: rate[cR].mean(0) if len(cR) else None, -1: rate[cL].mean(0) if len(cL) else None}}
        if len(cR) > 3 and len(cL) > 3 and len(iR) + len(iL) > 1:
            x = binned_window(b[np.r_[iR, iL]], RATE_T, 0.4)
            y = binned_window(b[np.r_[cR, cL]], RATE_T, 0.4)
            with np.errstate(invalid="ignore", divide="ignore"):
                d["p_rate"] = stats.ttest_ind(x, y, axis=0).pvalue
        else:
            d["p_rate"] = None
        out["cond"][c] = d
    # selectivity tests (Methods; code): epoch rates, lick right against lick left
    er = u["epoch_rates"]
    with np.errstate(invalid="ignore", divide="ignore"):
        for name, trials_ok in (("all", ctrl), ("correct", ctrl & hit), ("all_le", u["stable"] & (st == 0))):
            r_, l_ = np.flatnonzero(trials_ok & (sd == 1)), np.flatnonzero(trials_ok & (sd == -1))
            if len(r_) > 1 and len(l_) > 1:
                p = stats.ttest_ind(er[r_], er[l_], axis=0).pvalue
                p15 = stats.ttest_ind(u["response_rate_1p5"][r_], u["response_rate_1p5"][l_]).pvalue
                # response epoch read as the first 400 ms after the cue
                b4 = binned_window(b, [0.2], 0.4)[:, 0] / 0.4
                p04 = stats.ttest_ind(b4[r_], b4[l_]).pvalue
                out[f"p_sel_{name}"] = np.r_[p, p04, p15]
            else:
                out[f"p_sel_{name}"] = np.full(5, np.nan)
    return out
EOF
date -u
```

```
Sat Nov  7 19:41:09 UTC 2026
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/dev && cat > $TMPDIR/dev/nb.py <<'EOF'
# %% SETUP
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
import time
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

import alm3

warnings.filterwarnings("ignore", category=RuntimeWarning)
pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 40)
pd.set_option("display.max_rows", 300)

# %% LOAD-CELL
started = time.time()
files = alm3.list_files()
md5 = alm3.checksums()
names = alm3.session_names()
sessions = alm3.load_all(names, workers=3)
units = [u for s in sessions for u in alm3.reduce_units(s)]
print(f"loaded {len(sessions)} sessions and {len(units)} units in {time.time() - started:.0f} s")

# %% SETUP2
SD = {s["name"]: s for s in sessions}
EXP = {s["name"]: alm3.experiment(s) for s in sessions}
CONDS = {"unilateral": [1, 2, 3], "exp2": [4, 5, 6], "exp2b": [4, 5, 7], "exp3": [7, 8, 9], "ccx": [10, 11, 12], "none": []}
N_SCREEN = {"unilateral": 5, "exp2": 10, "exp2b": 10, "exp3": 10, "ccx": 10, "none": 10}
trials = pd.concat([alm3.trial_table(s).assign(experiment=EXP[s["name"]]) for s in sessions], ignore_index=True)
info = pd.DataFrame([{k: u[k] for k in ["session", "mouse", "unit", "experiment", "cell_type", "spike_width_ms", "n_spikes"]} for u in units])
EOF
echo
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/dev/nb.py <<'EOF'
# %% SANITY tags=sanity
read = sorted(k for k in files if k.startswith("alm-3/live/data/data_structure_files/"))
print(f"Files read: {len(read)} session files, {sum(files[k] for k in read) / 1e9:.2f} GB in the bucket listing.")
miss = [k for k in read if k.replace("alm-3/live/data/", "") not in md5 and k.replace("alm-3/live/", "") not in md5]
print("Session files without an MD5 sum in checksums.md5:", len(miss))
print("MD5 sums of the files read (checksums.md5):")
for k in read:
    key = k.replace("alm-3/live/", "")
    print(" ", key.split("/")[-1], md5.get(key, md5.get(key.replace("data/", ""), "missing")))

# %% SANITY tags=sanity
ses = pd.DataFrame([{
    "session": s["name"], "mouse": s["mouse"], "experiment": EXP[s["name"]],
    "line": alm3.MOUSE_LINE.get(s["mouse"], "?"), "trials": len(s["trial_ids"]), "good": int(s["good"].sum()),
    "units": len(s["units"]),
    "stim_types": " ".join(str(int(x)) for x in sorted(np.unique(s["stim_type"][s["good"] & np.isfinite(s["stim_type"])]))),
} for s in sessions])
print(ses.groupby("experiment").agg(sessions=("session", "size"), mice=("mouse", "nunique"), units=("units", "sum"), good_trials=("good", "sum")).to_string())
print("\nSessions per mouse and experiment:")
print(pd.crosstab(ses.mouse, ses.experiment).to_string())
print("\nPhotostimulus types present (good trials), by experiment:")
print(ses.groupby(["experiment", "stim_types"]).size().to_string())
print("\nSessions with no good trials:", ses[ses.good == 0].session.tolist())
print("Trial ids are 1..n in every session:", all((s["trial_ids"] == np.arange(1, len(s["trial_ids"]) + 1)).all() for s in sessions))
print("Trial types:", sorted({tuple(s["trial_type_names"]) for s in sessions}))
print("Time units (2 = second):", sorted({s["time_unit"] for s in sessions}), sorted({u["time_unit"] for s in sessions for u in s["units"]}))

# %% SANITY tags=sanity
g = trials[trials.good & trials.cue.notna()].copy()
g["sample"] = g.pole_out - g.pole_in
g["delay"] = g.cue - g.pole_out
print("Epoch durations (s) on good trials, by experiment, excluding lick-early trials:")
print(g[~g.lick_early].groupby("experiment")[["sample", "delay"]].describe(percentiles=[0.01, 0.5, 0.99]).round(3).to_string())
print("\nLick-early trials: delay duration quantiles", g[g.lick_early].delay.quantile([0.01, 0.5, 0.99]).round(2).tolist(),
      "; sample", g[g.lick_early]["sample"].quantile([0.01, 0.5, 0.99]).round(2).tolist())
print("\nOutcomes on good trials (fractions):")
print(g.assign(outcome=np.select([g.hit, g.err, g.nolick], ["hit", "err", "nolick"], "other")).groupby("experiment").outcome.value_counts(normalize=True).unstack().round(3).to_string())
print("Trials with both or no side:", int((g.side == 0).sum()))

# %% SANITY tags=sanity
# Laser timing against the trial table: onset and offset of the laser power trace (above 5% of
# its maximum), relative to the sample onset, delay onset and cue, per photostimulus type.
gl = g[~g.lick_early].copy()
gl["on_from_delay"] = gl.laser_on - gl.pole_out
gl["off_from_cue"] = gl.laser_off - gl.cue
gl["on_from_sample"] = gl.laser_on - gl.pole_in
lt = gl.groupby("stim").agg(n=("trial", "size"), with_laser=("laser_max", lambda x: int(x.notna().sum())),
                            power_mW=("laser_max", "median"), on_from_sample=("on_from_sample", "median"),
                            on_from_delay=("on_from_delay", "median"), off_from_cue=("off_from_cue", "median"),
                            duration=("laser_off", lambda x: np.nan))
lt["duration"] = gl.groupby("stim").apply(lambda d: (d.laser_off - d.laser_on).median())
print(lt.round(3).to_string())
print("Control trials with laser power above 0:", int(gl[(gl.stim == 0)].laser_max.gt(0).sum()), "of", int((gl.stim == 0).sum()))
EOF
cd $TMPDIR/dev && . ../v/bin/activate && python run.py nb.py SANITY 2>&1 | grep -v "^  data_structure" | head -150
```

```
--- cell 0 0.0s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev && python3 - <<'EOF'
s=open('run.py').read()
s=s.replace("cells=re.split(r'^# %%.*$', src, flags=re.M)","cells=re.split(r'(?m)^(?=# %%)', src)")
s=s.replace("and 'SETUP' not in c and 'LOAD-CELL' not in cells[i]:","and 'SETUP' not in c.splitlines()[0] and 'LOAD-CELL' not in cells[i]:")
open('run.py','w').write(s)
EOF
. ../v/bin/activate && python run.py nb.py SANITY 2>&1 | grep -v "^  data_structure" | head -150
```

```
--- cell 0 0.0s
--- cell 1 2.3s
--- cell 2 0.2s
--- cell 3 0.0s
Traceback (most recent call last):
  File "/tmp/claude-1001/dev/run.py", line 15, in <module>
    exec(compile(c, f'cell{i}', 'exec'), g)
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "cell4", line 2, in <module>
NameError: name 'files' is not defined. Did you mean: 'filter'?
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev && python3 - <<'EOF'
s=open('run.py').read()
s=s.replace('''units=pickle.load(open('/tmp/claude-1001/units.pkl','rb'))\\n"''','''units=pickle.load(open('/tmp/claude-1001/units.pkl','rb'))\\nfiles=alm3.list_files(); md5=alm3.checksums()\\n"''')
open('run.py','w').write(s)
EOF
. ../v/bin/activate && python run.py nb.py SANITY 2>&1 | grep -v "^  data_structure" | head -150
```

```
--- cell 0 0.0s
--- cell 1 1.0s
--- cell 2 0.8s
--- cell 3 0.0s
--- cell 4 0.0s
Files read: 92 session files, 12.26 GB in the bucket listing.
Session files without an MD5 sum in checksums.md5: 1
MD5 sums of the files read (checksums.md5):
   missing
            sessions  mice  units  good_trials
experiment                                    
ccx               33     7    567         7306
exp2              26     7    488         6958
exp2b              6     3     88         1521
exp3               6     3    102         1715
unilateral        20     4    334         5292

Sessions per mouse and experiment:
experiment  ccx  exp2  exp2b  exp3  unilateral
mouse                                         
[... 78 more lines not kept]
```

**Agent calls Bash**

```bash
grep -m3 "data_structure" $TMPDIR/checksums.md5; date -u
```

```
c87235d095840620e37afa15737d1f1d  data/data_structure_files/data_structure_ANM255200_20140910.mat
5e3beb9aca6b2e63e67d751c93362742  data/data_structure_files/data_structure_ANM255200_20140911.mat
b00303d7bea983db9aae18adc330e312  data/data_structure_files/data_structure_ANM255200_20140912.mat
Sat Nov  7 19:41:54 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev && python3 - <<'EOF'
s=open('nb.py').read()
s=s.replace('read = sorted(k for k in files if k.startswith("alm-3/live/data/data_structure_files/"))','read = sorted(k for k in files if k.startswith("alm-3/live/data/data_structure_files/") and k.endswith(".mat"))')
s=s.replace('''miss = [k for k in read if k.replace("alm-3/live/data/", "") not in md5 and k.replace("alm-3/live/", "") not in md5]
print("Session files without an MD5 sum in checksums.md5:", len(miss))
print("MD5 sums of the files read (checksums.md5):")
for k in read:
    key = k.replace("alm-3/live/", "")
    print(" ", key.split("/")[-1], md5.get(key, md5.get(key.replace("data/", ""), "missing")))''','''print("Session files without an MD5 sum in checksums.md5:", sum(k.replace("alm-3/live/", "") not in md5 for k in read))
print("MD5 sums of the files read (from checksums.md5):")
for k in read:
    print(" ", k.split("/")[-1], md5.get(k.replace("alm-3/live/", ""), "missing"))''')
open('nb.py','w').write(s)
EOF
cat >> $TMPDIR/dev/nb.py <<'EOF'
# %% SANITY tags=sanity
# Clock check. (1) Spikes against the laser trace: the mean rate of putative pyramidal neurons in
# 20 ms bins around the laser onset measured on each trial's own laser trace, ipsilateral
# photoinhibition trials against control trials aligned to the same nominal time. (2) Spikes
# against the trial table: decoding the instructed side from population counts in 200 ms windows
# around sample onset, with the true labels and with labels shuffled within session.
def onset_aligned(u, s, times):
    tr = u["trials"]
    st = s["stim_type"][tr]
    ok = u["stable"] & ~s["trial_types"]["LickEarly"][tr]
    res = {}
    for name, m in (("stim", ok & np.isin(st, [2, 4, 10])), ("control", ok & (st == 0))):
        idx = np.flatnonzero(m)
        if len(idx) < 3:
            return None
        if name == "stim":
            ref = (s["laser_on"] - s["cue"])[tr[idx]]
            ok2 = np.isfinite(ref)
            idx, ref = idx[ok2], ref[ok2]
        else:
            ref = (s["pole_out"] - s["cue"])[tr[idx]] + 0.004
        # counts in 20 ms bins at times relative to ref, from the 10 ms bins (rounded to 10 ms)
        t = np.round((ref[:, None] + times[None, :]) / 0.01) * 0.01
        cs = np.concatenate([np.zeros((len(idx), 1)), np.cumsum(u["binned"][idx], 1)], 1)
        a = np.clip(np.round((t - alm3.T0) / 0.01).astype(int), 0, alm3.NB10)
        b = np.clip(a + 2, 0, alm3.NB10)
        res[name] = (np.take_along_axis(cs, b, 1) - np.take_along_axis(cs, a, 1)).mean(0) / 0.02
    return res

tt_on = np.round(np.arange(-0.2, 0.3, 0.02), 3)
acc = {"stim": [], "control": []}
for u in units:
    s = SD[u["session"]]
    if u["cell_type"] != "pyramidal" or EXP[u["session"]] == "exp3":
        continue
    r = onset_aligned(u, s, tt_on)
    if r is None:
        continue
    for k in acc:
        acc[k].append(r[k])
on_tab = pd.DataFrame({"t_from_laser_onset_s": tt_on, "control": np.mean(acc["control"], 0), "photoinhibition": np.mean(acc["stim"], 0)})
on_tab["ratio"] = on_tab.photoinhibition / on_tab.control
print(f"{len(acc['stim'])} pyramidal neurons; mean rate (spikes/s) in 20 ms bins starting at each time from laser onset:")
print(on_tab.round(2).to_string(index=False))
EOF
cd $TMPDIR/dev && . ../v/bin/activate && python run.py nb.py "Clock check" 2>&1 | tail -30
```

```
--- cell 2 0.8s
--- cell 3 0.0s
--- cell 8 0.3s
1250 pyramidal neurons; mean rate (spikes/s) in 20 ms bins starting at each time from laser onset:
 t_from_laser_onset_s  control  photoinhibition  ratio
                -0.20     3.18             3.04   0.95
                -0.18     3.13             3.00   0.96
                -0.16     3.09             3.03   0.98
                -0.14     3.20             3.07   0.96
                -0.12     3.17             3.05   0.96
                -0.10     3.12             3.08   0.99
                -0.08     3.08             2.94   0.96
                -0.06     3.23             3.05   0.95
                -0.04     3.30             3.15   0.96
                -0.02     3.42             3.25   0.95
                -0.00     3.36             1.96   0.58
                 0.02     3.36             0.30   0.09
                 0.04     3.30             0.20   0.06
                 0.06     3.41             0.31   0.09
                 0.08     3.36             0.29   0.09
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev && python3 - <<'EOF'
s=open('nb.py').read()
s=s.replace('''# photoinhibition trials against control trials aligned to the same nominal time. (2) Spikes
# against the trial table: decoding the instructed side from population counts in 200 ms windows
# around sample onset, with the true labels and with labels shuffled within session.''','''# photoinhibition trials (types 2, 4 and 10, which start at delay onset) against control trials
# aligned to the same nominal time (delay onset + 4 ms). The spike times are aligned through the
# trial table's cue time, so a drop that starts at the laser onset shows that spikes, laser trace
# and trial table share one clock. (2) The same, per session, over all its photostimulus types.''')
s+='''
sess_rows = []
for name in ses.session:
    s = SD[name]
    us = [u for u in units if u["session"] == name and u["cell_type"] == "pyramidal"]
    pre, post = [], []
    for u in us:
        tr = u["trials"]
        st = s["stim_type"][tr]
        ok = u["stable"] & ~s["trial_types"]["LickEarly"][tr] & (st > 0) & np.isfinite((s["laser_on"])[tr])
        idx = np.flatnonzero(ok)
        if len(idx) < 5:
            continue
        ref = (s["laser_on"] - s["cue"])[tr[idx]]
        cs = np.concatenate([np.zeros((len(idx), 1)), np.cumsum(u["binned"][idx], 1)], 1)
        a0 = np.round((ref - 0.2 - alm3.T0) / 0.01).astype(int)
        a1 = np.round((ref - alm3.T0) / 0.01).astype(int)
        a2 = np.round((ref + 0.2 - alm3.T0) / 0.01).astype(int)
        r = np.arange(len(idx))
        pre.append((cs[r, a1] - cs[r, a0]).mean() / 0.2)
        post.append((cs[r, a2] - cs[r, a1 + 2]).mean() / 0.18)
    if pre:
        sess_rows.append({"session": name, "experiment": EXP[name], "neurons": len(pre), "rate_before": np.mean(pre), "rate_after_onset": np.mean(post)})
clk = pd.DataFrame(sess_rows)
clk["ratio"] = clk.rate_after_onset / clk.rate_before
print("\\nPer session (photostimulus types > 0): pyramidal rate 0.2 s before laser onset against 0.02 to 0.2 s after it")
print(clk.ratio.describe().round(3).to_string())
print("Sessions with ratio above 0.5:", clk[clk.ratio > 0.5][["session", "experiment", "neurons", "ratio"]].round(2).to_dict("records"))
print("Sessions with photostimulation but no pyramidal neuron to check:", sorted(set(ses[ses.stim_types.str.len() > 1].session) - set(clk.session)))
'''
open('nb.py','w').write(s)
EOF
cd $TMPDIR/dev && . ../v/bin/activate && python run.py nb.py "Clock check" 2>&1 | tail -16
```

```
0.10     3.46             0.28   0.08
                 0.12     3.40             0.27   0.08
                 0.14     3.37             0.19   0.06
                 0.16     3.37             0.29   0.09
                 0.18     3.30             0.27   0.08
                 0.20     3.29             0.29   0.09
                 0.22     3.28             0.27   0.08
                 0.24     3.29             0.21   0.06
                 0.26     3.26             0.24   0.07
                 0.28     3.26             0.32   0.10
Traceback (most recent call last):
  File "/tmp/claude-1001/dev/run.py", line 15, in <module>
    exec(compile(c, f'cell{i}', 'exec'), g)
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "cell8", line 48, in <module>
NameError: name 'ses' is not defined. Did you mean: 'set'?
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev && . ../v/bin/activate && python run.py nb.py "SANITY" 2>&1 | tail -12
```

```
Per session (photostimulus types > 0): pyramidal rate 0.2 s before laser onset against 0.02 to 0.2 s after it
count    87.000
mean      0.303
std       0.294
min       0.000
25%       0.180
50%       0.296
75%       0.371
max       2.169
Sessions with ratio above 0.5: [{'session': 'ANM257636_20150404', 'experiment': 'exp2b', 'neurons': 6, 'ratio': 1.59}, {'session': 'ANM264411_20141224', 'experiment': 'exp2', 'neurons': 21, 'ratio': 0.82}, {'session': 'ANM273657_20150325', 'experiment': 'exp2b', 'neurons': 13, 'ratio': 0.77}, {'session': 'ANM298738_20150727', 'experiment': 'ccx', 'neurons': 19, 'ratio': 2.17}]
Sessions with photostimulation but no pyramidal neuron to check: ['ANM255200_20140910', 'ANM255200_20140911', 'ANM255200_20140912']
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev && python3 - <<'EOF'
s=open('nb.py').read()
s=s.replace('ok = u["stable"] & ~s["trial_types"]["LickEarly"][tr] & (st > 0) & np.isfinite((s["laser_on"])[tr])','ok = u["stable"] & ~s["trial_types"]["LickEarly"][tr] & np.isin(st, [1, 2, 3, -1, -2, -3, 4, 6, 7, 8, 10, 12]) & np.isfinite((s["laser_on"])[tr])')
s=s.replace("over all its photostimulus types.","over its photostimulus types that\n# include the left (recorded) ALM, that is all but the contralateral ones (5, 9, 11).")
s=s.replace('print("\\nPer session (photostimulus types > 0)','print("\\nPer session (types including left ALM)')
open('nb.py','w').write(s)
EOF
cd $TMPDIR/dev && . ../v/bin/activate && python run.py nb.py "SANITY" 2>&1 | tail -12
```

```
Per session (types including left ALM): pyramidal rate 0.2 s before laser onset against 0.02 to 0.2 s after it
count    90.000
mean      0.108
std       0.327
min       0.000
25%       0.009
50%       0.028
75%       0.069
max       2.181
Sessions with ratio above 0.5: [{'session': 'ANM257636_20150404', 'experiment': 'exp2b', 'neurons': 6, 'ratio': 2.04}, {'session': 'ANM264411_20141224', 'experiment': 'exp2', 'neurons': 21, 'ratio': 0.82}, {'session': 'ANM273657_20150325', 'experiment': 'exp2b', 'neurons': 13, 'ratio': 0.71}, {'session': 'ANM298738_20150727', 'experiment': 'ccx', 'neurons': 19, 'ratio': 2.18}]
Sessions with photostimulation but no pyramidal neuron to check: []
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . v/bin/activate && cat > shift.py <<'EOF'
import sys,pickle,numpy as np
sys.path.insert(0,'entries/crcns-alm-3-li-2016'); import alm3
S=pickle.load(open('sessions.pkl','rb')); SD={s['name']:s for s in S}
for name in ['ANM257636_20150404','ANM264411_20141224','ANM273657_20150325','ANM298738_20150727','ANM263808_20150121']:
    s=SD[name]; res={}
    for sh in [-2,-1,0,1,2]:
        st=np.roll(s['stim_type'],sh); lon=np.roll(s['laser_on'],sh)
        st_ok=np.isin(st,[1,2,3,4,6,7,8,10,12])&s['good']&np.isfinite(s['cue'])&np.isfinite(lon)
        pre=post=0;n=0
        for u in s['units']:
            if u['cell_type']!=['pyramidal']: continue
            ti=u['spike_trial_index']; t=u['spike_time']
            for i in np.flatnonzero(st_ok):
                x=t[ti==i]-lon[i]; pre+=((x>-0.2)&(x<0)).sum(); post+=((x>0.02)&(x<0.2)).sum(); n+=1
        res[sh]=round(post/0.18/(pre/0.2),2)
    print(name,res, 'units',len(s['units']))
EOF
python shift.py
```

```
ANM257636_20150404 {-2: np.float64(1.36), -1: np.float64(1.18), 0: np.float64(1.29), 1: np.float64(1.14), 2: np.float64(1.26)} units 8
ANM264411_20141224 {-2: np.float64(1.05), -1: np.float64(1.02), 0: np.float64(0.82), 1: np.float64(0.97), 2: np.float64(0.97)} units 22
ANM273657_20150325 {-2: np.float64(1.11), -1: np.float64(1.14), 0: np.float64(1.02), 1: np.float64(1.06), 2: np.float64(1.17)} units 14
ANM298738_20150727 {-2: np.float64(1.44), -1: np.float64(1.38), 0: np.float64(2.14), 1: np.float64(1.38), 2: np.float64(1.18)} units 22
ANM263808_20150121 {-2: np.float64(0.83), -1: np.float64(0.74), 0: np.float64(0.02), 1: np.float64(0.73), 2: np.float64(0.84)} units 43
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/dev/nb.py <<'EOF'
# %% SETUP3
# Per-unit measures used by the selectivity and rate claims. The screening trials that set each
# neuron's preferred trial type are drawn with a generator seeded from the unit's position.
t_m = time.time()
M = []
for k, u in enumerate(units):
    e = EXP[u["session"]]
    M.append(alm3.unit_measures(u, SD[u["session"]], N_SCREEN[e], CONDS[e], seed=1000 + k))
info["nR"] = [m["nR"] for m in M]
info["nL"] = [m["nL"] for m in M]
info["fr_mean"] = [m["fr_mean"] for m in M]
print(f"measures for {len(M)} units in {time.time() - t_m:.0f} s")
EOF
cat >> $TMPDIR/dev/nb.py <<'EOF'
# %% [markdown]
# ## units-and-sessions
#
# Claim: "1012 single units were recorded in left ALM during behaviour across 58 sessions (20
# unilateral, 38 bilateral) from 12 mice; 72 are fast-spiking, 890 putative pyramidal and 50 of
# intermediate width are excluded." Criterion: counts over the non-callosotomy sessions, units
# classed by the spike-width bounds of the Methods. The data set gives each unit a `cellType`
# label; the trough-to-peak width of the mean of the 29-sample waveforms (19.53 kHz, so widths
# come in steps of 0.051 ms) is computed as a second reading, and a third reading upsamples the
# mean waveform 10 times by cubic spline before measuring.

# %% tags=claim:units-and-sessions
from scipy.interpolate import CubicSpline

def width_upsampled(mw, factor=10):
    x = np.arange(len(mw))
    xs = np.linspace(0, len(mw) - 1, (len(mw) - 1) * factor + 1)
    y = CubicSpline(x, mw)(xs)
    tr = int(np.argmin(y))
    pk = tr + int(np.argmax(y[tr:]))
    return (xs[pk] - xs[tr]) / alm3.SAMPLE_RATE_WAVEFORM * 1e3

info["width_up_ms"] = [width_upsampled(SD[u["session"]]["units"][u["unit"]]["mean_waveform"].astype(float)) for u in units]
def width_class(w):
    return np.where(w > 0.45, "pyramidal", np.where(w < 0.35, "FS", "intermediate"))
info["class_width"] = width_class(info.spike_width_ms)
info["class_width_up"] = width_class(info.width_up_ms)
nc = info[info.experiment != "ccx"]
print("Non-callosotomy sessions:", nc.session.nunique(), "with units;", (ses.experiment != "ccx").sum(), "in all;",
      "unilateral", (ses.experiment == "unilateral").sum(), "; bilateral (exp2, exp2b, exp3)",
      ses.experiment.isin(["exp2", "exp2b", "exp3"]).sum(), "; mice", nc.mouse.nunique())
print("Single units:", len(nc))
print("\nBy the data set's cellType label:", nc.cell_type.value_counts().to_dict())
print("By the width of the mean waveform:", nc.class_width.value_counts().to_dict())
print("By the width of the upsampled mean waveform:", nc.class_width_up.value_counts().to_dict())
print("\nLabel against width class (mean waveform):")
print(pd.crosstab(nc.cell_type, nc.class_width).to_string())
print("\nLabel against width class (upsampled):")
print(pd.crosstab(nc.cell_type, nc.class_width_up).to_string())
print("\nWidth (ms) by label, mean waveform:")
print(nc.groupby("cell_type").spike_width_ms.describe().round(3).to_string())
print("\nPaper: 1012 units, 20 + 38 sessions, 12 mice, 890 pyramidal, 72 FS, 50 intermediate.")
print("Units per experiment:", nc.experiment.value_counts().to_dict())
EOF
cd $TMPDIR/dev && . ../v/bin/activate && python run.py nb.py "SANITY" "SETUP3" "units-and-sessions" 2>&1 | tail -42
```

```
Per session (types including left ALM): pyramidal rate 0.2 s before laser onset against 0.02 to 0.2 s after it
count    90.000
mean      0.108
std       0.327
min       0.000
25%       0.009
50%       0.028
75%       0.069
max       2.181
Sessions with ratio above 0.5: [{'session': 'ANM257636_20150404', 'experiment': 'exp2b', 'neurons': 6, 'ratio': 2.04}, {'session': 'ANM264411_20141224', 'experiment': 'exp2', 'neurons': 21, 'ratio': 0.82}, {'session': 'ANM273657_20150325', 'experiment': 'exp2b', 'neurons': 13, 'ratio': 0.71}, {'session': 'ANM298738_20150727', 'experiment': 'ccx', 'neurons': 19, 'ratio': 2.18}]
Sessions with photostimulation but no pyramidal neuron to check: []
measures for 1579 units in 10 s
Non-callosotomy sessions: 58 with units; 58 in all; unilateral 20 ; bilateral (exp2, exp2b, exp3) 38 ; mice 12
Single units: 1012

By the data set's cellType label: {'pyramidal': 890, 'FS': 89, 'none': 33}
By the width of the mean waveform: {'pyramidal': 890, 'FS': 98, 'intermediate': 24}
By the width of the upsampled mean waveform: {'pyramidal': 889, 'FS': 104, 'intermediate': 19}

Label against width class (mean waveform):
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/dev/nb.py <<'EOF'
# %% [markdown]
# ## ed1-selective-fraction
#
# Claim: "Most ALM pyramidal neurons distinguish trial types (634 of 890), 176 during the sample,
# 337 during the delay and 493 during the response epoch." Two-tailed t-test of epoch spike rates,
# lick right against lick left control trials, p < 0.05. Readings: trials (a) correct only,
# (b) correct and error grouped by instructed movement (the code's choice, `i_yes_trial` in
# analysis_compile_all_data_unilateral.m), each with lick-early trials excluded or included (M1);
# response epoch the 1.3 s after the cue (code), the first 400 ms, or 1.5 s (M2).

# %% tags=claim:ed1-selective-fraction
pyr = (info.cell_type == "pyramidal") & (info.experiment != "ccx")
rows = []
for trials_name, label in (("correct", "correct, lick-early excluded"), ("all", "correct+error, lick-early excluded"), ("all_le", "correct+error, lick-early included")):
    P = np.array([M[i][f"p_sel_{trials_name}"] for i in np.flatnonzero(pyr)])
    for j, resp in ((2, "1.3 s"), (3, "0.4 s"), (4, "1.5 s")):
        sig = P[:, [0, 1, j]] < 0.05
        rows.append({"trials": label, "response epoch": resp, "any": int(sig.any(1).sum()), "sample": int(sig[:, 0].sum()),
                     "delay": int(sig[:, 1].sum()), "response": int(sig[:, 2].sum()), "n": int(len(P)),
                     "untestable": int(np.isnan(P[:, 0]).sum())})
ed1 = pd.DataFrame(rows)
exp_ = {"any": 634, "sample": 176, "delay": 337, "response": 493}
for k, v in exp_.items():
    ed1[f"{k}_ok"] = (ed1[k] - v).abs() <= 0.1 * v
print(ed1.to_string(index=False))
print("Paper: 634 any, 176 sample, 337 delay, 493 response of 890; tolerance 10%.")
print("Readings with all four counts within tolerance:", int(ed1[[f"{k}_ok" for k in exp_]].all(1).sum()))
print("\nBy mouse (code reading: correct+error, lick-early excluded, 1.3 s):")
P = np.array([M[i]["p_sel_all"] for i in np.flatnonzero(pyr)])
bym = pd.DataFrame({"mouse": info[pyr].mouse.values, "any": (P[:, [0, 1, 2]] < 0.05).any(1)}).groupby("mouse")["any"].agg(["sum", "size", "mean"])
print(bym.round(2).to_string())
EOF
cd $TMPDIR/dev && . ../v/bin/activate && python run.py nb.py "SETUP3" "ed1-selective" 2>&1 | tail -32
```

```
--- cell 9 9.8s
--- cell 12 0.0s
--- cell 13 0.0s
measures for 1579 units in 10 s
                            trials response epoch  any  sample  delay  response   n  untestable  any_ok  sample_ok  delay_ok  response_ok
      correct, lick-early excluded          1.3 s  633     176    336       493 890           1    True       True      True         True
      correct, lick-early excluded          0.4 s  582     176    336       411 890           1    True       True      True        False
      correct, lick-early excluded          1.5 s  635     176    336       490 890           1    True       True      True         True
correct+error, lick-early excluded          1.3 s  571     152    287       404 890           1    True      False     False        False
correct+error, lick-early excluded          0.4 s  532     152    287       364 890           1   False      False     False        False
correct+error, lick-early excluded          1.5 s  572     152    287       408 890           1    True      False     False        False
correct+error, lick-early included          1.3 s  596     161    315       433 890           1    True       True      True        False
correct+error, lick-early included          0.4 s  550     161    315       382 890           1   False       True      True        False
correct+error, lick-early included          1.5 s  591     161    315       422 890           1    True       True      True        False
Paper: 634 any, 176 sample, 337 delay, 493 response of 890; tolerance 10%.
Readings with all four counts within tolerance: 2

By mouse (code reading: correct+error, lick-early excluded, 1.3 s):
           sum  size  mean
mouse                     
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cat >> $TMPDIR/dev/nb.py <<'EOF'
# %% SETUP4
# Shared pieces for the rate and selectivity recovery claims.
GT = alm3.GRID_T
# Photoinhibition offsets from the cue (end of the ramp), as the code uses them and as the laser
# trace shows (data check above): unilateral sample -1.6 s, early delay -0.8 s, middle delay
# -0.3 s; all 0.8 s conditions -0.9 s.
OFFSET = {1: -1.6, 2: -0.8, 3: -0.3, 4: -0.9, 5: -0.9, 6: -0.9, 7: -0.9, 8: -0.9, 9: -0.9, 10: -0.9, 11: -0.9, 12: -0.9}
ONSET = {1: -2.1, 2: -1.3, 3: -0.8, 4: -1.7, 5: -1.7, 6: -1.7, 7: -1.7, 8: -1.7, 9: -1.7, 10: -1.7, 11: -1.7, 12: -1.7}
RAMP = {1: 0.1, 2: 0.1, 3: 0.1}
M400 = {}

def measures_400(k):
    """Unit measures with 400 ms windows for the selectivity trace (reading b of M4)."""
    if k not in M400:
        u = units[k]
        e = EXP[u["session"]]
        M400[k] = alm3.unit_measures(u, SD[u["session"]], N_SCREEN[e], CONDS[e], seed=1000 + k, width_psth=0.4)
    return M400[k]

def selective(k, trials="all"):
    p = M[k][f"p_sel_{trials}"]
    return bool(np.nan_to_num(p[0], nan=1) < 0.05 or np.nan_to_num(p[1], nan=1) < 0.05)

def selection(exp, conds, sel_trials="all", min_stim=2, min_ctrl=5, fr_min=None, pref_min=1.0, experiments=None):
    """Indices of the neurons of the selectivity recovery figures (code, Fig. 1g and 2e sections):
    putative pyramidal, selective in the sample or delay epoch, |preference count| > 1, more than
    `min_ctrl` control and more than `min_stim` trials of each type in every condition."""
    exps = experiments or [exp]
    out = []
    for k, u in enumerate(units):
        if EXP[u["session"]] not in exps or u["cell_type"] != "pyramidal":
            continue
        m = M[k]
        if m["pref_counts"] is None or abs(m["pref_counts"][0]) <= pref_min:
            continue
        if not selective(k, sel_trials):
            continue
        if m["nR"] <= min_ctrl or m["nL"] <= min_ctrl:
            continue
        if any(c not in m["cond"] or m["cond"][c]["nR"] <= min_stim or m["cond"][c]["nL"] <= min_stim for c in conds):
            continue
        if fr_min is not None and not (m["fr_mean"] > fr_min):
            continue
        out.append(k)
    return out

def sel_traces(ks, cond, width=0.2):
    """Selectivity (preferred minus non-preferred, spikes/s) on control test trials and on
    photoinhibition trials of `cond`, neurons x time."""
    ctrl, stim = [], []
    for k in ks:
        m = M[k] if width == 0.2 else measures_400(k)
        sgn = 1 if M[k]["pref_counts"][0] >= 0 else -1
        ctrl.append(sgn * (m["psth_ctrl"][1] - m["psth_ctrl"][-1]))
        c = m["cond"][cond]["psth"]
        stim.append(sgn * (c[1] - c[-1]))
    return np.array(ctrl), np.array(stim)
EOF
echo
```

```
Sat Nov  7 19:44:03 UTC 2026
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/dev/nb.py <<'EOF'
# %% [markdown]
# ## fig1f-rate-recovery
#
# Claim: "Within 400 ms after unilateral photoinhibition, spike rates are indistinguishable from
# control in 90% of neurons; only 10% keep a sustained change." Per neuron and condition of
# Experiment 1, the rate test (400 ms windows every 50 ms, control against photoinhibition, lick
# right and lick left pooled, p < 0.01). Neurons: putative pyramidal, mean rate > 1 spike/s, more
# than 8 control trials of each type and more than 3 photoinhibition trials of each type (code,
# Fig. 1f section: `i_cell`, `i_n_trial`); without the rate exclusion as a reading (M3). "Within
# 400 ms after" read as (a) the 400 ms window starting at offset (centre offset + 0.2 s) and (b)
# the window centred 400 ms after offset. The code's own measure, the fraction in the window
# centred 0.25 s before the cue (`frac_persist`), is shown too.

# %% tags=claim:fig1f-rate-recovery
def rate_fraction_table(exp, conds, fr_min=1.0, min_ctrl=8, min_stim=3):
    rows = []
    for c in conds:
        ks = [k for k, u in enumerate(units) if EXP[u["session"]] == exp and u["cell_type"] == "pyramidal"
              and M[k]["nR"] > min_ctrl and M[k]["nL"] > min_ctrl and c in M[k]["cond"]
              and M[k]["cond"][c]["nR"] > min_stim and M[k]["cond"][c]["nL"] > min_stim
              and M[k]["cond"][c]["p_rate"] is not None and (fr_min is None or M[k]["fr_mean"] > fr_min)]
        P = np.array([M[k]["cond"][c]["p_rate"] for k in ks])
        frac = (P < 0.01).mean(0)
        def at(t):
            return float(frac[np.argmin(np.abs(alm3.RATE_T - t))])
        rows.append({"condition": c, "label": alm3.STIM_LABELS[c], "neurons": len(ks), "mice": len({units[k]["mouse"] for k in ks}),
                     "during": at(OFFSET[c] - 0.25), "a_window_from_offset": at(OFFSET[c] + 0.2),
                     "b_centre_offset+0.4": at(OFFSET[c] + 0.4), "code_frac_persist(-0.25)": at(-0.25),
                     "before_onset": at(ONSET[c] - 0.25)})
    return pd.DataFrame(rows), ks

for fr_min in (1.0, None):
    tab, _ = rate_fraction_table("unilateral", [1, 2, 3], fr_min=fr_min)
    print(f"Rate exclusion: {'mean rate > 1 spike/s' if fr_min else 'none'}")
    print(tab.round(3).to_string(index=False))
    for col in ("a_window_from_offset", "b_centre_offset+0.4"):
        v = tab[col].values
        print(f"  {col}: per condition within 0.1 +- 0.01: {list(np.abs(v - 0.1) <= 0.01)}; mean {v.mean():.3f}; all below 0.2: {bool((v < 0.2).all())}")
    print()
print("Paper: 168, 168, 175 neurons; 10% with a sustained change. 'during' is the window centred 0.25 s before offset; 'before_onset' the window centred 0.25 s before onset (the false-positive level of the test).")

# %% [markdown]
# ## fig1g-selectivity-recovery
#
# Claim: recovery of > 80% of control selectivity within 514 ms; recovery times 373 +- 260 ms
# (sample), 510 +- 218 ms (early delay) and 327 +- 112 ms (window ending 0.3 s before the cue);
# 55 selective neurons. Method of the code (Fig. 1g section of analysis_compile_all_data_unilateral.m),
# which fills the open details of M4: preference from 5 control trials of each type drawn at
# random (10 in total, the Methods' "subset of 10 trials"), on the spike count from sample onset to
# 1.3 s after the cue; selectivity traces on the remaining trials, 200 ms boxcar centred on each
# time; recovery time the mean over 1000 bootstrap resamples of neurons of the first time after
# offset (and before 1 s after the cue) at which (control minus photoinhibition) / control mean
# selectivity < 0.2, +- the standard deviation over resamples. Readings shown: trials of the
# selectivity test (all, the code's, or correct, M3), more than 2 (code) or more than 3 (legend)
# trials per condition, 200 ms windows stamped at their centre or 400 ms windows stamped at their
# end (M4).

# %% tags=claim:fig1g-selectivity-recovery
def recovery_table(exp, conds, t_end, sel_trials, min_stim, width, stamp_shift, seed, experiments=None, min_ctrl=5):
    ks = selection(exp, conds, sel_trials=sel_trials, min_stim=min_stim, min_ctrl=min_ctrl, experiments=experiments)
    rng = np.random.default_rng(seed)
    rows = []
    for c in conds:
        ctrl, stim = sel_traces(ks, c, width=width)
        mean, sd, frac = alm3.recovery_time(ctrl, stim, GT + stamp_shift, OFFSET[c], t_end, rng)
        ratio = (ctrl - stim).mean(0) / ctrl.mean(0)
        late = float(ratio[np.argmin(np.abs(GT + stamp_shift - (-0.2)))])
        rows.append({"condition": c, "label": alm3.STIM_LABELS[c], "neurons": len(ks), "mice": len({units[k]["mouse"] for k in ks}),
                     "recovery_ms": mean * 1000, "sd_ms": sd * 1000, "frac_boot_recovered": frac,
                     "deficit_at_-0.2s": late})
    return pd.DataFrame(rows), ks

rows = []
for sel_trials in ("all", "correct"):
    for min_stim in (2, 3):
        for width, shift, lab in ((0.2, 0.0, "200 ms, centre"), (0.4, 0.2, "400 ms, end")):
            tab, ks = recovery_table("unilateral", [1, 2, 3], 1.0, sel_trials, min_stim, width, shift, seed=11)
            for r in tab.to_dict("records"):
                rows.append({"selective_on": sel_trials, "min_trials": f">{min_stim}", "window": lab, **r})
f1g = pd.DataFrame(rows)
expected = {1: (373, 260), 2: (510, 218), 3: (327, 112)}
f1g["within_tol"] = [abs(r.recovery_ms - expected[r.condition][0]) <= expected[r.condition][1] for r in f1g.itertuples()]
print(f1g.drop(columns="label").round(3).to_string(index=False))
ok = f1g.groupby(["selective_on", "min_trials", "window"]).agg(all_within=("within_tol", "all"), all_recover=("frac_boot_recovered", lambda x: bool((x > 0.5).all())), neurons=("neurons", "first"))
print("\nPer reading: all three recovery times within tolerance; each condition recovers before the cue in most resamples")
print(ok.to_string())
print("Paper: 55 neurons; 373 +- 260, 510 +- 218, 327 +- 112 ms. 'deficit_at_-0.2s' is (control - photoinhibition) / control at 0.2 s before the cue.")
EOF
cd $TMPDIR/dev && . ../v/bin/activate && python run.py nb.py "SETUP3" "fig1f-rate" "fig1g-sel" 2>&1 | tail -60
```

```
--- cell 0 0.0s
--- cell 1 1.0s
--- cell 2 0.7s
--- cell 3 0.0s
--- cell 9 10.0s
--- cell 14 0.0s
--- cell 15 0.0s
--- cell 16 0.0s
--- cell 17 0.0s
measures for 1579 units in 10 s
Rate exclusion: mean rate > 1 spike/s
 condition                            label  neurons  mice  during  a_window_from_offset  b_centre_offset+0.4  code_frac_persist(-0.25)  before_onset
         1       ipsi 1 spot sample (0.5 s)      168     4   0.720                 0.179                0.131                     0.054         0.000
         2  ipsi 1 spot early delay (0.5 s)      168     4   0.702                 0.196                0.143                     0.125         0.006
         3 ipsi 1 spot middle delay (0.5 s)      175     4   0.714                 0.109                0.091                     0.383         0.011
  a_window_from_offset: per condition within 0.1 +- 0.01: [np.False_, np.False_, np.True_]; mean 0.161; all below 0.2: True
  b_centre_offset+0.4: per condition within 0.1 +- 0.01: [np.False_, np.False_, np.True_]; mean 0.122; all below 0.2: True

Rate exclusion: none
 condition                            label  neurons  mice  during  a_window_from_offset  b_centre_offset+0.4  code_frac_persist(-0.25)  before_onset
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-alm-3-li-2016 && python3 - <<'EOF'
p='alm3.py'; s=open(p).read()
s=s.replace("""    a = np.round((np.asarray(times) - width / 2 - T0) / BIN).astype(int)
    b = np.round((np.asarray(times) + width / 2 - T0) / BIN).astype(int)
    return cs[:, b] - cs[:, a]""","""    a = np.clip(np.round((np.asarray(times) - width / 2 - T0) / BIN).astype(int), 0, NB10)
    b = np.clip(np.round((np.asarray(times) + width / 2 - T0) / BIN).astype(int), 0, NB10)
    return cs[:, b] - cs[:, a]""")
s=s.replace('"""Counts in windows of `width` s centred on `times` (multiples of 10 ms), per trial."""','"""Counts in windows of `width` s centred on `times` (multiples of 10 ms), per trial; windows\n    are cut at the ends of the binned range (3.6 s before to 2.3 s after the cue)."""')
open(p,'w').write(s)
EOF
cd $TMPDIR/dev && . ../v/bin/activate && python run.py nb.py "SETUP3" "fig1g-sel" 2>&1 | tail -40
```

```
--- cell 18 2.1s
measures for 1579 units in 10 s
selective_on min_trials         window  condition  neurons  mice  recovery_ms   sd_ms  frac_boot_recovered  deficit_at_-0.2s  within_tol
         all         >2 200 ms, centre          1       72     4      347.340 250.850                1.000            -0.191        True
         all         >2 200 ms, centre          2       72     4      420.321 256.913                0.997             0.280        True
         all         >2 200 ms, centre          3       72     4      235.536  97.253                0.999             0.637        True
         all         >2    400 ms, end          1       72     4      627.610 317.162                1.000            -0.306        True
         all         >2    400 ms, end          2       72     4      759.969 282.500                0.979             0.449       False
         all         >2    400 ms, end          3       72     4      448.148 109.281                0.999             0.957       False
         all         >3 200 ms, centre          1       70     4      315.710 255.561                1.000            -0.175        True
         all         >3 200 ms, centre          2       70     4      391.555 232.930                0.997             0.212        True
         all         >3 200 ms, centre          3       70     4      234.770  97.429                1.000             0.617        True
         all         >3    400 ms, end          1       70     4      605.848 322.292                0.997            -0.293        True
         all         >3    400 ms, end          2       70     4      707.972 266.165                0.986             0.432        True
         all         >3    400 ms, end          3       70     4      449.140 110.949                1.000             0.960       False
     correct         >2 200 ms, centre          1       87     4      386.370 257.109                1.000            -0.093        True
     correct         >2 200 ms, c
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/dev/nb.py <<'EOF'
# %% SETUP5
def mean_rate_traces(exp, conds, fr_min=1.0, min_ctrl=8, min_stim=3, experiments=None):
    """Population mean rate (spikes/s, 200 ms boxcar) on control and photoinhibition trials, lick
    right and lick left averaged per neuron; neurons as in the code's Fig. 1f and 2d sections."""
    exps = experiments or [exp]
    out = {}
    for c in conds:
        ks = [k for k, u in enumerate(units) if EXP[u["session"]] in exps and u["cell_type"] == "pyramidal"
              and M[k]["nR"] > min_ctrl and M[k]["nL"] > min_ctrl and c in M[k]["cond"]
              and M[k]["cond"][c]["nR"] > min_stim and M[k]["cond"][c]["nL"] > min_stim and M[k]["fr_mean"] > fr_min]
        ctrl = np.array([(M[k]["psth_ctrl_all"][1] + M[k]["psth_ctrl_all"][-1]) / 2 for k in ks])
        stim = np.array([(M[k]["cond"][c]["psth"][1] + M[k]["cond"][c]["psth"][-1]) / 2 for k in ks])
        P = np.array([M[k]["cond"][c]["p_rate"] for k in ks])
        out[c] = {"ks": ks, "ctrl": ctrl, "stim": stim, "p": P}
    return out

def rate_summary(R, times):
    rows = []
    for c, d in R.items():
        r = {"condition": c, "label": alm3.STIM_LABELS[c], "neurons": len(d["ks"])}
        for t in times:
            i = np.argmin(np.abs(GT - t))
            j = np.argmin(np.abs(alm3.RATE_T - t))
            r[f"rate_ratio@{t:+.2f}"] = d["stim"][:, i].mean() / d["ctrl"][:, i].mean()
            r[f"frac_changed@{t:+.2f}"] = (d["p"][:, j] < 0.01).mean()
        rows.append(r)
    return pd.DataFrame(rows)

def recovery_readings(exp, conds, t_end, expected, seed, experiments=None):
    rows = []
    for sel_trials in ("all", "correct"):
        for min_stim in (2, 3):
            for width, shift, lab in ((0.2, 0.0, "200 ms, centre"), (0.4, 0.2, "400 ms, end")):
                tab, ks = recovery_table(exp, conds, t_end, sel_trials, min_stim, width, shift, seed=seed, experiments=experiments)
                for r in tab.to_dict("records"):
                    rows.append({"selective_on": sel_trials, "min_trials": f">{min_stim}", "window": lab, **r})
    t = pd.DataFrame(rows)
    t["within_tol"] = [abs(r.recovery_ms - expected[r.condition][0]) <= expected[r.condition][1] if r.condition in expected else np.nan for r in t.itertuples()]
    return t

# %% [markdown]
# ## fig2-bilateral-recovery
#
# Claim: spike rate and selectivity of left ALM neurons recover within 600 ms after ipsilateral
# photoinhibition, contralateral photoinhibition hardly affects activity, and after bilateral
# photoinhibition the rate recovers on average but selectivity does not; recovery 538 +- 178 ms
# (ipsilateral), 192 +- 114 ms (contralateral), none (bilateral); 143 selective neurons.
# Experiment 2 sessions (types 4, 5, 6). Method of the code (analysis_compile_all_data_bilateral.m,
# Fig. 2e section): as for fig1g, with 10 screening trials of each type and the recovery searched
# from offset (0.9 s before the cue) up to the cue. "Spike rate (> 90 %)" read as (a) more than 90%
# of neurons without a significant rate change in the window centred 600 ms after offset, or (b)
# population mean rate within 10% of control there. Rate neurons as in the code's Fig. 2d
# section (pyramidal, mean rate > 1 spike/s, > 8 control and > 3 photoinhibition trials per type).

# %% tags=claim:fig2-bilateral-recovery
R2 = mean_rate_traces("exp2", [4, 5, 6])
rs2 = rate_summary(R2, [-1.3, -0.3, -0.05])
print("Rates: ratio of photoinhibition to control population mean rate and fraction of neurons with a significant change (p < 0.01),")
print("at 0.4 s after onset (-1.3), 0.6 s after offset (-0.3) and just before the cue (-0.05):")
print(rs2.drop(columns="label").round(3).to_string(index=False))
f2 = recovery_readings("exp2", [4, 5, 6], 0.0, {4: (538, 178), 5: (192, 114)}, seed=21)
print("\nSelectivity recovery (bootstrap over neurons), all readings:")
print(f2.drop(columns="label").round(3).to_string(index=False))
print("\nPaper: 143 neurons; ipsilateral 538 +- 178 ms, contralateral 192 +- 114 ms, bilateral no recovery.")
print("'frac_boot_recovered' is the fraction of resamples that reach 80% before the cue.")
EOF
cd $TMPDIR/dev && . ../v/bin/activate && python run.py nb.py "SETUP3" "fig2-bilateral-recovery" 2>&1 | tail -45
```

```
--- cell 0 0.0s
--- cell 1 0.9s
--- cell 2 0.7s
--- cell 3 0.0s
--- cell 9 10.0s
--- cell 14 0.0s
--- cell 19 0.0s
--- cell 20 0.0s
measures for 1579 units in 10 s
Rates: ratio of photoinhibition to control population mean rate and fraction of neurons with a significant change (p < 0.01),
at 0.4 s after onset (-1.3), 0.6 s after offset (-0.3) and just before the cue (-0.05):
 condition  neurons  rate_ratio@-1.30  frac_changed@-1.30  rate_ratio@-0.30  frac_changed@-0.30  rate_ratio@-0.05  frac_changed@-0.05
         4      267             0.094               0.663             0.958               0.094             0.990               0.090
         5      273             0.901               0.165             1.057               0.051             1.052               0.029
         6      320             0.031               0.797             1.164               0.322             1.114               0.328
Traceback (most recent call last):
  File "/tmp/claude-1001/dev/run.py", line 15, in <module>
    exec(compile(c, f'cell{i}', 'exec'), g)
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "cell21", line 7, in <module>
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev && python3 - <<'EOF'
s=open('nb.py').read()
a=s.index("def recovery_table(")
b=s.index("rows = []\nfor sel_trials in (\"all\", \"correct\"):")
func=s[a:b]
s=s[:a]+s[b:]
s=s.replace("# %% SETUP5\n","# %% SETUP5\n"+func)
open('nb.py','w').write(s)
EOF
. ../v/bin/activate && python run.py nb.py "SETUP3" "fig2-bilateral-recovery" 2>&1 | tail -42
```

```
--- cell 9 10.2s
--- cell 14 0.0s
--- cell 19 0.0s
--- cell 20 0.0s
--- cell 21 3.6s
measures for 1579 units in 10 s
Rates: ratio of photoinhibition to control population mean rate and fraction of neurons with a significant change (p < 0.01),
at 0.4 s after onset (-1.3), 0.6 s after offset (-0.3) and just before the cue (-0.05):
 condition  neurons  rate_ratio@-1.30  frac_changed@-1.30  rate_ratio@-0.30  frac_changed@-0.30  rate_ratio@-0.05  frac_changed@-0.05
         4      267             0.094               0.663             0.958               0.094             0.990               0.090
         5      273             0.901               0.165             1.057               0.051             1.052               0.029
         6      320             0.031               0.797             1.164               0.322             1.114               0.328

Selectivity recovery (bootstrap over neurons), all readings:
selective_on min_trials         window  condition  neurons  mice  recovery_ms   sd_ms  frac_boot_recovered  deficit_at_-0.2s within_tol
         all         >2 200 ms, centre          4      146     7      716.335 143.072                0.251             0.475      False
         all         >2 200 ms, centre          5      146     7      240.338 180.229                0.977             0.188       True
         all         >2 200 ms, centre          6      146     7          NaN     NaN                0.000             0.763        NaN
         all         >2    400 ms, end          4      146     7      822.727  50.632                0.022             0.531      False
         all         >2    400 ms, end          5      146     7      489.943 184.148                0.877             0.170      False
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,200p $TMPDIR/scripts/Demo_get_performance.m | grep -v "^\s*$" | head -60
```

```
function [fracCorrect fracCorrectR fracCorrectL fracEarlyLick] = Demo_get_performance(obj) 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% [fracCorrect fracCorrectR fracCorrectL fracEarlyLick] = Demo_get_performance(obj) 
%
%
% this script extracts behavioral data from session object
% it plots the performance 
% it returns FractionCorrect, %correct for lick right trials, %correct for lick
% left trials, %early lick
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% get the raw data
trialID = obj.trialIds;
i_HitR = find(strcmp(obj.trialTypeStr,'HitR'));
i_HitL = find(strcmp(obj.trialTypeStr,'HitL'));
i_ErrR = find(strcmp(obj.trialTypeStr,'ErrR'));
i_ErrL = find(strcmp(obj.trialTypeStr,'ErrL'));
i_NoLickR = find(strcmp(obj.trialTypeStr,'NoLickR'));
i_NoLickL = find(strcmp(obj.trialTypeStr,'NoLickL'));
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-alm-3-li-2016 && python3 - <<'EOF'
p='alm3.py'; s=open(p).read()
s=s.replace("""    Returns (mean, std over resamples, fraction of resamples that recover), times from offset.
    \"\"\"""","""    Returns (mean, std over the resamples that recover, fraction of resamples that recover, mean
    with resamples that do not recover counted at `t_end`), times from offset. The last is how
    the code's MATLAB arrays behave: a resample that does not recover leaves a zero (the cue
    time) in T_recovery when a later resample recovers.
    \"\"\"""")
s=s.replace("""    out = np.array(out)
    ok = np.isfinite(out)
    if not ok.any():
        return np.nan, np.nan, 0.0
    return float(out[ok].mean()), float(out[ok].std(ddof=1)), float(ok.mean())""","""    out = np.array(out)
    ok = np.isfinite(out)
    censored = float(np.where(ok, out, t_end - t_off).mean())
    if not ok.any():
        return np.nan, np.nan, 0.0, censored
    sd = float(out[ok].std(ddof=1)) if ok.sum() > 1 else np.nan
    return float(out[ok].mean()), sd, float(ok.mean()), censored""")
open(p,'w').write(s)
EOF
cd $TMPDIR/dev && python3 - <<'EOF'
s=open('nb.py').read()
s=s.replace("""        mean, sd, frac = alm3.recovery_time(ctrl, stim, GT + stamp_shift, OFFSET[c], t_end, rng)""","""        mean, sd, frac, cens = alm3.recovery_time(ctrl, stim, GT + stamp_shift, OFFSET[c], t_end, rng)""")
s=s.replace(""""recovery_ms": mean * 1000, "sd_ms": sd * 1000, "frac_boot_recovered": frac,""",""""recovery_ms": mean * 1000, "sd_ms": sd * 1000, "frac_boot_recovered": frac, "censored_ms": cens * 1000,""")
open('nb.py','w').write(s)
EOF
date -u
```

```
Sat Nov  7 19:46:27 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/dev/nb.py <<'EOF'
# %% [markdown]
# ## ed7-unilateral-4-spots-bilateral-1-spot
#
# Claim: bilateral photoinhibition with one spot per side causes a larger persistent change in
# selectivity than unilateral photoinhibition with four spots; recovery 490 +- 280 ms (ipsilateral
# 4 spots), 235 +- 156 ms (contralateral 4 spots), none (bilateral 1 spot); 40 selective neurons.
# Experiment 3 sessions (types 7, 8, 9), method as fig2-bilateral-recovery. The "persistent
# change" is the mean delta selectivity (photoinhibition minus control, spikes/s) in the last
# 400 ms of the delay (criterion).

# %% tags=claim:ed7-unilateral-4-spots-bilateral-1-spot
e7 = recovery_readings("exp3", [7, 8, 9], 0.0, {8: (490, 280), 9: (235, 156)}, seed=31)
print(e7.drop(columns="label").round(3).to_string(index=False))
print("\nMean delta selectivity (photoinhibition minus control, spikes/s) in the last 400 ms of the delay, code reading:")
ks7 = selection("exp3", [7, 8, 9], sel_trials="all", min_stim=2)
win = (GT > -0.4) & (GT <= 0)
for c in (7, 8, 9):
    ctrl, stim = sel_traces(ks7, c)
    d = (stim - ctrl)[:, win].mean(1)
    print(f"  {c} {alm3.STIM_LABELS[c]:28s} n={len(d)} mean {d.mean():+.2f} (s.e.m. {d.std(ddof=1) / np.sqrt(len(d)):.2f}); control selectivity {ctrl[:, win].mean():.2f}")
ctrl, s7 = sel_traces(ks7, 7)
_, s8 = sel_traces(ks7, 8)
d7, d8 = (s7 - ctrl)[:, win].mean(1), (s8 - ctrl)[:, win].mean(1)
print(f"  bilateral 1 spot minus ipsilateral 4 spots, paired over neurons: {np.mean(d7 - d8):+.2f} spikes/s, t-test p = {stats.ttest_rel(d7, d8).pvalue:.3g}")
print("Paper: 40 neurons; 490 +- 280 and 235 +- 156 ms; bilateral 1 spot does not recover.")

# %% [markdown]
# ## ed2b-silencing
#
# Claim: photoinhibition silences more than 90% of putative pyramidal activity, similarly with
# ipsilateral and bilateral photoinhibition and in both mouse lines, while contralateral
# photoinhibition barely changes the average rate. Per neuron, spike rate during photoinhibition
# over the rate in the same window of control trials, neurons with mean rate < 1 spike/s excluded
# (criterion). Window (a) photoinhibition before the ramp, (b) the whole period with the ramp.
# Reduction = 1 minus the mean normalized rate. Neurons need at least 3 photoinhibition trials and
# 5 control trials (a standard choice). Mouse lines from the code's comments.

# %% tags=claim:ed2b-silencing
def silencing_rows(window):
    rows = []
    for k, u in enumerate(units):
        e = EXP[u["session"]]
        if u["cell_type"] != "pyramidal" or not (M[k]["fr_mean"] >= 1) or e == "none":
            continue
        s = SD[u["session"]]
        tr = u["trials"]
        st = s["stim_type"][tr]
        ok = u["stable"] & ~s["trial_types"]["LickEarly"][tr]
        for c in CONDS[e]:
            a = ONSET[c]
            b = OFFSET[c] - (RAMP.get(c, 0.2) if window == "a" else 0.0)
            ci, si = np.flatnonzero(ok & (st == 0)), np.flatnonzero(ok & (st == c))
            if len(si) < 3 or len(ci) < 5:
                continue
            cnt = alm3.binned_window(u["binned"], [(a + b) / 2], b - a)[:, 0]
            rc, rs = cnt[ci].mean(), cnt[si].mean()
            if rc > 0:
                rows.append({"experiment": e, "condition": c, "label": alm3.STIM_LABELS[c], "mouse": u["mouse"],
                             "line": alm3.MOUSE_LINE.get(u["mouse"], "?"), "norm_rate": rs / rc})
    return pd.DataFrame(rows)

for window in ("a", "b"):
    sil = silencing_rows(window)
    print(f"Window ({window}): {'onset to start of ramp' if window == 'a' else 'onset to end of ramp'}")
    t = sil.groupby(["experiment", "condition", "label"]).norm_rate.agg(["size", "mean", "median"])
    t["reduction"] = 1 - t["mean"]
    print(t.round(3).to_string())
    print("By mouse line, ipsilateral and bilateral conditions (types 1-4, 6-8):")
    t2 = sil[sil.condition.isin([1, 2, 3, 4, 6, 7, 8])].groupby(["line", "experiment"]).norm_rate.agg(["size", "mean"])
    t2["reduction"] = 1 - t2["mean"]
    print(t2.round(3).to_string())
    print("By mouse, Experiment 2 ipsilateral (type 4):")
    print(sil[(sil.condition == 4) & (sil.experiment == "exp2")].groupby("mouse").norm_rate.agg(["size", "mean"]).round(3).to_string())
    print()
print("Criterion: reduction at least 0.81 for ipsilateral and bilateral photoinhibition in each experiment and each line; contralateral mean normalized rate within 0.8 to 1.2.")

# %% [markdown]
# ## ed2e-no-rebound
#
# Claim: no rebound excitation on average after photoinhibition offset; a small proportion of
# neurons show rebound, balanced by low-level sustained inhibition in a larger proportion.
# Experiment 2, lick right trials, ipsilateral photoinhibition (type 4); windows 0 to 400 ms and
# 400 to 800 ms after offset; per neuron two-tailed t-test of counts, control against
# photoinhibition, p < 0.01; population test a paired t-test over neurons of the mean rates
# (criterion). Neurons: pyramidal with more than 3 lick right photoinhibition trials, with and
# without the 1 spike/s exclusion (M3).

# %% tags=claim:ed2e-no-rebound
for fr_min in (1.0, None):
    rows = []
    for k, u in enumerate(units):
        if EXP[u["session"]] != "exp2" or u["cell_type"] != "pyramidal":
            continue
        if fr_min is not None and not (M[k]["fr_mean"] > fr_min):
            continue
        s = SD[u["session"]]
        tr = u["trials"]
        st, sd_ = s["stim_type"][tr], alm3.side(s)[tr]
        ok = u["stable"] & ~s["trial_types"]["LickEarly"][tr] & (sd_ == 1)
        ci, si = np.flatnonzero(ok & (st == 0)), np.flatnonzero(ok & (st == 4))
        if len(si) <= 3 or len(ci) <= 3:
            continue
        r = {}
        for name, (a, b) in (("w1", (-0.9, -0.5)), ("w2", (-0.5, -0.1))):
            cnt = alm3.binned_window(u["binned"], [(a + b) / 2], b - a)[:, 0]
            r[name + "_ctrl"], r[name + "_stim"] = cnt[ci].mean() / 0.4, cnt[si].mean() / 0.4
            r[name + "_p"] = stats.ttest_ind(cnt[ci], cnt[si]).pvalue
        rows.append(r)
    rb = pd.DataFrame(rows)
    print(f"Rate exclusion: {'> 1 spike/s' if fr_min else 'none'}; neurons {len(rb)}")
    for w, lab in (("w1", "0-400 ms after offset"), ("w2", "400-800 ms after offset")):
        d = rb[w + "_stim"] - rb[w + "_ctrl"]
        t = stats.ttest_rel(rb[w + "_stim"], rb[w + "_ctrl"])
        exc = int(((rb[w + "_p"] < 0.01) & (d > 0)).sum())
        sup = int(((rb[w + "_p"] < 0.01) & (d < 0)).sum())
        print(f"  {lab}: mean control {rb[w + '_ctrl'].mean():.2f}, photoinhibition {rb[w + '_stim'].mean():.2f} spikes/s; "
              f"difference {d.mean():+.2f}, paired t = {t.statistic:.2f}, p = {t.pvalue:.3g}; excited {exc}, suppressed {sup} (p < 0.01)")
EOF
cd $TMPDIR/dev && . ../v/bin/activate && python run.py nb.py "SETUP3" "ed7-unilateral" "ed2b-silencing" "ed2e-no-rebound" 2>&1 | grep -v "^---" | tail -120
```

```
measures for 1579 units in 10 s
selective_on min_trials         window  condition  neurons  mice  recovery_ms   sd_ms  frac_boot_recovered  censored_ms  deficit_at_-0.2s within_tol
         all         >2 200 ms, centre          7       32     3      334.769 183.210                0.801       447.25             0.253        NaN
         all         >2 200 ms, centre          8       32     3      530.443 173.966                0.993       533.03             0.020       True
         all         >2 200 ms, centre          9       32     3      119.169 177.986                0.999       119.95            -0.014       True
         all         >2    400 ms, end          7       32     3      543.412 169.114                0.633       674.28             0.207        NaN
         all         >2    400 ms, end          8       32     3      773.527  71.771                0.845       793.13             0.372      False
         all         >2    400 ms, end          9       32     3      466.256 250.599                0.967       480.57             0.133      False
         all         >3 200 ms, centre          7       32     3      334.769 183.210                0.801       447.25             0.253        NaN
         all         >3 200 ms, centre          8       32     3      530.443 173.966                0.993       533.03             0.020       True
         all         >3 200 ms, centre          9       32     3      119.169 177.986                0.999       119.95            -0.014       True
         all         >3    400 ms, end          7       32     3      543.412 169.114                0.633       674.28             0.207        NaN
         all         >3    400 ms, end          8       32     3      773.527  71.771                0.845       793.13             0.372      False
         all         >3    400 ms, end          9       32     3      466.256 250.599                0.967       480.57             0.133      False
     correct         >2 200 ms,
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cat >> $TMPDIR/dev/nb.py <<'EOF'
# %% [markdown]
# ## ed4-return-to-trajectory
#
# Claim: neurons whose rates decrease during the delay epoch also recover after unilateral
# photoinhibition, returning to the time-matched control trajectory and not decaying to the
# end-point rate (27 neurons from 6 mice; paired t-test p < 0.001). Criterion: Experiment 1
# pyramidal neurons with a lower rate at the end of the delay than at its start (two-tailed
# t-test, 400 ms windows, trial types pooled, p < 0.05); rates normalized to each neuron's mean
# rate, preferred and non-preferred types separately; per neuron, RMS over the time from
# photoinhibition offset to the cue of (perturbed minus time-matched control) and of (perturbed
# minus the control rate in the last 400 ms of the delay). Conditions (a) early delay (type 2),
# (b) the three conditions pooled per neuron. The windows "start" and "end" of the delay are
# read as its first and last 400 ms. Increasing neurons are shown as a variant.

# %% tags=claim:ed4-return-to-trajectory
def ed4_rows(direction):
    rows = []
    for k, u in enumerate(units):
        if EXP[u["session"]] != "unilateral" or u["cell_type"] != "pyramidal" or M[k]["pref_counts"] is None:
            continue
        m = M[k]
        s = SD[u["session"]]
        tr = u["trials"]
        st = s["stim_type"][tr]
        ok = u["stable"] & ~s["trial_types"]["LickEarly"][tr] & (st == 0)
        if ok.sum() < 10:
            continue
        early = alm3.binned_window(u["binned"][ok], [-1.1], 0.4)[:, 0]
        late = alm3.binned_window(u["binned"][ok], [-0.2], 0.4)[:, 0]
        p = stats.ttest_ind(early, late).pvalue
        if not (p < 0.05) or (late.mean() < early.mean()) != (direction == "decrease"):
            continue
        norm = m["fr_mean"] if m["fr_mean"] > 0 else np.nan
        sgn = 1 if m["pref_counts"][0] >= 0 else -1
        r = {"k": k, "mouse": u["mouse"]}
        for c in (1, 2, 3):
            cd = m["cond"].get(c)
            if cd is None or cd["psth"][1] is None or cd["psth"][-1] is None or cd["nR"] < 3 or cd["nL"] < 3:
                r[c] = None
                continue
            win = (GT > OFFSET[c]) & (GT <= -0.1)
            vals_tm, vals_ep = [], []
            for typ in (sgn, -sgn):
                ctrl = m["psth_ctrl_all"][typ] / norm
                pert = cd["psth"][typ] / norm
                endpoint = ctrl[np.argmin(np.abs(GT + 0.2))]
                vals_tm.append(pert[win] - ctrl[win])
                vals_ep.append(pert[win] - endpoint)
            r[c] = (np.sqrt(np.mean(np.concatenate(vals_tm) ** 2)), np.sqrt(np.mean(np.concatenate(vals_ep) ** 2)))
        rows.append(r)
    return rows

for direction in ("decrease", "increase"):
    rows = ed4_rows(direction)
    print(f"{direction}: {len(rows)} neurons from {len({r['mouse'] for r in rows})} mice")
    for lab, conds in (("(a) early delay", [2]), ("(b) pooled", [1, 2, 3])):
        tm, ep = [], []
        for r in rows:
            v = [r[c] for c in conds if r.get(c) is not None]
            if v:
                tm.append(np.mean([x[0] for x in v]))
                ep.append(np.mean([x[1] for x in v]))
        tm, ep = np.array(tm), np.array(ep)
        t = stats.ttest_rel(tm, ep)
        print(f"  {lab}: n = {len(tm)}; RMS to time-matched control {tm.mean():.3f}, to end point {ep.mean():.3f}; "
              f"paired t = {t.statistic:.2f}, p = {t.pvalue:.3g}; smaller to time-matched in {(tm < ep).sum()} of {len(tm)}")
print("RMS is computed on the 200 ms boxcar rate from offset to 0.1 s before the cue, in units of the neuron's mean rate.")
EOF
cd $TMPDIR/dev && . ../v/bin/activate && python run.py nb.py "SETUP3" "ed4-return" 2>&1 | grep -v "^---" | tail -12
```

```
Sat Nov  7 19:47:30 UTC 2026
measures for 1579 units in 10 s
decrease: 55 neurons from 4 mice
  (a) early delay: n = 47; RMS to time-matched control 0.526, to end point 0.463; paired t = 2.43, p = 0.0192; smaller to time-matched in 14 of 47
  (b) pooled: n = 47; RMS to time-matched control 0.551, to end point 0.526; paired t = 1.35, p = 0.184; smaller to time-matched in 14 of 47
increase: 44 neurons from 4 mice
  (a) early delay: n = 34; RMS to time-matched control 1.068, to end point 1.230; paired t = -3.68, p = 0.000822; smaller to time-matched in 29 of 34
  (b) pooled: n = 34; RMS to time-matched control 1.062, to end point 1.214; paired t = -4.10, p = 0.000253; smaller to time-matched in 30 of 34
RMS is computed on the 200 ms boxcar rate from offset to 0.1 s before the cue, in units of the neuron's mean rate.
Shell cwd was reset to
```

**Agent calls Bash**

```bash
grep -n -i "Extended Data Fig. 4\|Extended Data Figure 4\|end point\|decreas" paper/10.1038-nature17643.txt | head -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
import re
t=open('paper/10.1038-nature17643.txt').read()
for kw in ['end point','Extended Data Fig. 4','27 neurons','time-matched']:
    for m in re.finditer(re.escape(kw),t):
        print('>>',kw, t[max(0,m.start()-700):m.start()+500].replace('\n',' '));print()
" | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR/dev && python3 - <<'EOF'
s=open('nb.py').read()
s=s.replace('def ed4_rows(direction):','def ed4_rows(direction, exp="unilateral", conds=(1, 2, 3)):')
s=s.replace('''        if EXP[u["session"]] != "unilateral" or u["cell_type"] != "pyramidal" or M[k]["pref_counts"] is None:''','''        if EXP[u["session"]] != exp or u["cell_type"] != "pyramidal" or M[k]["pref_counts"] is None:''')
s=s.replace('''        early = alm3.binned_window(u["binned"][ok], [-1.1], 0.4)[:, 0]''','''        d0 = -1.3 if exp == "unilateral" else -1.7
        early = alm3.binned_window(u["binned"][ok], [d0 + 0.2], 0.4)[:, 0]''')
s=s.replace('''        for c in (1, 2, 3):
            cd = m["cond"].get(c)
            if cd is None or cd["psth"][1] is None''','''        for c in conds:
            cd = m["cond"].get(c)
            if cd is None or cd["psth"][1] is None''')
s=s.replace('''for direction in ("decrease", "increase"):
    rows = ed4_rows(direction)
    print(f"{direction}: {len(rows)} neurons from {len({r['mouse'] for r in rows})} mice")
    for lab, conds in (("(a) early delay", [2]), ("(b) pooled", [1, 2, 3])):''','''for direction, exp, readings in (("decrease", "unilateral", (("(a) early delay", [2]), ("(b) pooled", [1, 2, 3]))),
                                 ("increase", "unilateral", (("(a) early delay", [2]), ("(b) pooled", [1, 2, 3]))),
                                 ("decrease", "exp2", (("variant, Experiment 2 ipsilateral", [4]),))):
    rows = ed4_rows(direction, exp, sorted({c for _, cs in readings for c in cs}))
    print(f"{direction}, {exp}: {len(rows)} neurons from {len({r['mouse'] for r in rows})} mice")
    for lab, conds in readings:''')
open('nb.py','w').write(s)
EOF
. ../v/bin/activate && python run.py nb.py "SETUP3" "ed4-return" 2>&1 | grep -v "^---" | tail -12
```

```
measures for 1579 units in 10 s
decrease, unilateral: 55 neurons from 4 mice
  (a) early delay: n = 47; RMS to time-matched control 0.526, to end point 0.463; paired t = 2.43, p = 0.0192; smaller to time-matched in 14 of 47
  (b) pooled: n = 47; RMS to time-matched control 0.551, to end point 0.526; paired t = 1.35, p = 0.184; smaller to time-matched in 14 of 47
increase, unilateral: 44 neurons from 4 mice
  (a) early delay: n = 34; RMS to time-matched control 1.068, to end point 1.230; paired t = -3.68, p = 0.000822; smaller to time-matched in 29 of 34
  (b) pooled: n = 34; RMS to time-matched control 1.062, to end point 1.214; paired t = -4.10, p = 0.000253; smaller to time-matched in 30 of 34
decrease, exp2: 111 neurons from 7 mice
  variant, Experiment 2 ipsilateral: n = 106; RMS to time-matched control 0.739, to end point 0.743; paired t = -0.29, p = 0.773; smaller to time-matched in 55 of 106
RMS is computed on the 200 ms boxcar rate from offset to 0.1 s before the cue, in units of the neuron's mean rate.
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/dev/nb.py <<'EOF'
# %% [markdown]
# ## ed10e-callosotomy-preparatory-activity
#
# Claim: preparatory activity after callosotomy is similar to that of control mice, with 254 of 496
# putative pyramidal neurons selective. Selectivity test of M3 on callosotomy control trials,
# under the same readings as ed1-selective-fraction; "similar" read as the selective fraction
# within 10 percentage points of the control mice's fraction under the same reading, and the
# population delay selectivity present and rising toward the cue (criterion).

# %% tags=claim:ed10e-callosotomy-preparatory-activity
pyr_c = (info.cell_type == "pyramidal") & (info.experiment == "ccx")
print("Callosotomy putative pyramidal neurons:", int(pyr_c.sum()), "(paper 496) from", info[pyr_c].mouse.nunique(), "mice,", info[pyr_c].session.nunique(), "sessions")
rows = []
for trials_name, label in (("correct", "correct"), ("all", "correct+error")):
    for mask, grp in ((pyr_c, "callosotomy"), (pyr, "control mice")):
        P = np.array([M[i][f"p_sel_{trials_name}"] for i in np.flatnonzero(mask)])
        sig = P[:, [0, 1, 2]] < 0.05
        rows.append({"trials": label, "group": grp, "n": len(P), "selective": int(sig.any(1).sum()), "fraction": sig.any(1).mean(),
                     "sample": int(sig[:, 0].sum()), "delay": int(sig[:, 1].sum()), "response": int(sig[:, 2].sum())})
e10 = pd.DataFrame(rows)
print(e10.round(3).to_string(index=False))
print("Paper: 254 of 496 callosotomy pyramidal neurons selective; control 634 of 890.")
# population delay selectivity (preferred minus non-preferred, control test trials), selective neurons
for grp, exps in (("callosotomy", ["ccx"]), ("control mice, 1.7 s delay", ["exp2", "exp2b", "exp3"])):
    ks = [k for k, u in enumerate(units) if EXP[u["session"]] in exps and u["cell_type"] == "pyramidal" and M[k]["pref_counts"] is not None
          and selective(k, "correct")]
    sel = np.array([(1 if M[k]["pref_counts"][0] >= 0 else -1) * (M[k]["psth_ctrl"][1] - M[k]["psth_ctrl"][-1]) for k in ks])
    pts = [-1.5, -1.0, -0.5, -0.1]
    print(f"{grp}: {len(ks)} selective neurons; mean selectivity (spikes/s) at " + ", ".join(f"{t:+.1f} s: {sel[:, np.argmin(np.abs(GT - t))].mean():.2f}" for t in pts))

# %% [markdown]
# ## fig5-callosotomy-recovery
#
# Claim: after callosotomy, ALM neurons recover their average spike rate after ipsilateral
# photoinhibition but not their selectivity; selectivity recovers after contralateral
# photoinhibition (217 +- 228 ms) and not after bilateral; selectivity along cd is reduced; 129
# selective neurons, 16 sessions. Method of the code (analysis_compile_all_data_bilateralCCX.m) as
# for fig2-bilateral-recovery; conditions as the data set labels them (types 10, 11, 12). The cd
# part is tested in the population section below.

# %% tags=claim:fig5-callosotomy-recovery
R5 = mean_rate_traces("ccx", [10, 11, 12])
rs5 = rate_summary(R5, [-1.3, -0.5, -0.3, -0.05])
print("Rates: photoinhibition over control population mean rate, and fraction of neurons with a significant change:")
print(rs5.drop(columns="label").round(3).to_string(index=False))
f5 = recovery_readings("ccx", [10, 11, 12], 0.0, {11: (217, 228)}, seed=51)
print("\nSelectivity recovery, all readings:")
print(f5.drop(columns="label").round(3).to_string(index=False))
print("Paper: 129 neurons; contralateral 217 +- 228 ms; ipsilateral and bilateral selectivity do not recover.")
EOF
cd $TMPDIR/dev && . ../v/bin/activate && python run.py nb.py "SETUP3" "ed1-selective" "ed10e-callosotomy" "fig5-callosotomy-recovery" 2>&1 | grep -v "^---" | tail -45
```

```
ANM264411   24    44  0.55
ANM270337   58    66  0.88
ANM273657   36    67  0.54
Callosotomy putative pyramidal neurons: 519 (paper 496) from 7 mice, 33 sessions
       trials        group   n  selective  fraction  sample  delay  response
      correct  callosotomy 519        303     0.584      66    137       222
      correct control mice 890        633     0.711     176    336       493
correct+error  callosotomy 519        259     0.499      50    122       179
correct+error control mice 890        571     0.642     152    287       404
Paper: 254 of 496 callosotomy pyramidal neurons selective; control 634 of 890.
callosotomy: 176 selective neurons; mean selectivity (spikes/s) at -1.5 s: 1.08, -1.0 s: 1.61, -0.5 s: 2.25, -0.1 s: 2.44
control mice, 1.7 s delay: 284 selective neurons; mean selectivity (spikes/s) at -1.5 s: 1.60, -1.0 s: 1.93, -0.5 s: 1.99, -0.1 s: 1.96
Rates: photoinhibition over control population mean rate, and fraction of neurons with a significant change:
 condition  neurons  rate_ratio@-1.30  frac_changed@-1.30  rate_ratio@-0.50  frac_changed@-0.50  rate_ratio@-0.30  frac_changed@-0.30  rate_ratio@-0.05  frac_changed@-0.05
        10      311             0.121               0.643             1.106               0.174             1.081               0.145             1.053               0.087
        11      308             0.963               0.081             0.956               0.062             0.998               0.032             0.969               0.013
        12      300             0.091               0.700             1.027               0.273             1.034               0.230             1.062               0.180

Selectivity recovery, all readings:
selective_on min_trials         window  condition  neurons  mice  recovery_ms   sd_ms  frac_boot_recovered  censored_ms  deficit_at_-0.2s within_tol
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cat >> $TMPDIR/dev/nb.py <<'EOF'
# %% SETUP6
def performance_table(exps, conds, by="mouse_pooled"):
    """Fraction correct (hits over hits and errors; lick-early and no-lick trials excluded, as in
    the data set's Demo_get_performance.m and the Methods) per mouse and condition, on performing
    trials. by = "mouse_pooled": trials pooled over a mouse's sessions (M7 a); "session_mean": the
    mean of its session values (M7 b)."""
    g = trials[trials.experiment.isin(exps) & trials.good & ~trials.lick_early & (trials.hit | trials.err) & trials.stim.isin([0] + conds)]
    if by == "mouse_pooled":
        t = g.groupby(["mouse", "stim"]).hit.mean().unstack()
    else:
        t = g.groupby(["mouse", "session", "stim"]).hit.mean().unstack().groupby("mouse").mean()
    n = g.groupby(["mouse", "stim"]).size().unstack()
    return t * 100, n

def perf_tests(t, conds, paired=True):
    rows = []
    for c in conds:
        d = t[[0, c]].dropna()
        test = stats.ttest_rel(d[c], d[0]) if paired else stats.ttest_ind(t[c].dropna(), t[0].dropna())
        rows.append({"condition": c, "label": alm3.STIM_LABELS[c], "mice": len(d), "control_%": d[0].mean(), "photoinhibition_%": d[c].mean(),
                     "drop": d[0].mean() - d[c].mean(), "t": test.statistic, "p": test.pvalue})
    return pd.DataFrame(rows)

# %% [markdown]
# ## fig1d-earlier-photoinhibition-minimal
#
# Claim: unilateral photoinhibition ending at least 0.3 s before the go cue (early and middle
# delay) has minimal behavioural effect (p > 0.1). A claim of absence, judged on the paper's test:
# per condition, performance with photoinhibition against control, two-tailed t-test across mice,
# paired (M7 a; unpaired as a variant), at p < 0.05 (criterion). The paper's Fig. 1d comes from
# behaviour-only sessions, which the data set does not hold; this uses the recording sessions of
# Experiment 1 (types 1, 2, 3; the sessions with the no-ramp types -1 to -3 are left out, as the
# data set says not to analyse them). The sample condition is reported as well.

# %% tags=claim:fig1d-earlier-photoinhibition-minimal
for by in ("mouse_pooled", "session_mean"):
    t, n = performance_table(["unilateral"], [1, 2, 3], by=by)
    print(f"Performance (% correct) per mouse, {by}:")
    print(t.round(1).to_string())
    for paired in (True, False):
        print(f"  {'paired' if paired else 'unpaired'} t-test against control:")
        print(perf_tests(t, [2, 3, 1], paired=paired).round(4).to_string(index=False))
print("\nTrials per mouse and condition:")
print(n.to_string())

# %% [markdown]
# ## fig2b-bilateral-behaviour
#
# Claim: unilateral photoinhibition in the early delay reduces performance only slightly (1 spot
# 70.3%, 4 spots 67.7%), bilateral photoinhibition severely (1 spot per side 58.0%) or to near
# chance (4 spots per side 51.4%). Performance per condition over mice, tests of M7. The paper's
# values come from 13 mice including behaviour-only sessions; here the recording sessions of the
# bilateral experiments (types 4, 8, 7, 6), 0.8 s photoinhibition from delay onset.

# %% tags=claim:fig2b-bilateral-behaviour
exps_b = ["exp2", "exp2b", "exp3"]
cmap = {4: 70.3, 8: 67.7, 7: 58.0, 6: 51.4}
for by in ("mouse_pooled", "session_mean"):
    t, n = performance_table(exps_b, [4, 8, 7, 6], by=by)
    print(f"Performance (% correct) per mouse, {by}:")
    print(t.round(1).to_string())
    for paired in (True, False):
        r = perf_tests(t, [4, 8, 7, 6], paired=paired)
        r["paper_%"] = r.condition.map(cmap)
        r["within_10%"] = (r["photoinhibition_%"] - r["paper_%"]).abs() <= 0.1 * r["paper_%"]
        print(f"  {'paired' if paired else 'unpaired'} t-tests against control:")
        print(r.round(4).to_string(index=False))
        d = t[[7, 8]].dropna()
        tt = stats.ttest_rel(d[7], d[8]) if paired else stats.ttest_ind(t[7].dropna(), t[8].dropna())
        print(f"  bilateral 1 spot against unilateral 4 spots: {d[7].mean():.1f} vs {d[8].mean():.1f} % over {len(d)} mice with both, t = {tt.statistic:.2f}, p = {tt.pvalue:.4f}")
print("\nTrials per mouse and condition:")
print(n.to_string())

# %% [markdown]
# ## fig5b-callosotomy-behaviour
#
# Claim: callosotomy leaves performance unaffected but makes it highly sensitive to unilateral
# photoinhibition, with a significant interaction, dropping to the level of bilateral
# photoinhibition in control mice (58.0%). The data set holds only sessions after the cut, so the
# before-and-after comparison and the interaction cannot be tested; the after-cut test is
# unilateral photoinhibition (type 10) against control (p < 0.01) and its performance against
# 58.0 +- 5.8% (criterion).

# %% tags=claim:fig5b-callosotomy-behaviour
print("Callosotomy sessions per mouse with dates:", ses[ses.experiment == "ccx"].groupby("mouse").session.apply(lambda x: f"{len(x)}: {x.str[-8:].min()} to {x.str[-8:].max()}").to_dict())
for by in ("mouse_pooled", "session_mean"):
    t, n = performance_table(["ccx"], [10, 11, 12], by=by)
    print(f"\nPerformance (% correct) per mouse, {by}:")
    print(t.round(1).to_string())
    for paired in (True, False):
        print(f"  {'paired' if paired else 'unpaired'} t-tests against control:")
        print(perf_tests(t, [10, 11, 12], paired=paired).round(4).to_string(index=False))
tc, _ = performance_table(exps_b, [4], by="mouse_pooled")
t5, _ = performance_table(["ccx"], [10], by="mouse_pooled")
print(f"\nControl-trial performance, control mice (bilateral experiments) {tc[0].mean():.1f}% over {tc[0].notna().sum()} mice; callosotomy mice {t5[0].mean():.1f}% over {t5[0].notna().sum()} mice; "
      f"unpaired t-test p = {stats.ttest_ind(tc[0].dropna(), t5[0].dropna()).pvalue:.3f} (different mice; not the paper's before/after test)")
print(f"Ipsilateral 1 spot: control mice {tc[4].mean():.1f}%, callosotomy mice {t5[10].mean():.1f}%")
EOF
cd $TMPDIR/dev && . ../v/bin/activate && python run.py nb.py "fig1d-earlier" "fig2b-bilateral" "fig5b-call" 2>&1 | grep -v "^---" | tail -150
```

```
Sat Nov  7 19:49:09 UTC 2026
measures for 1579 units in 10 s
Performance (% correct) per mouse, mouse_pooled:
stim        0.0   1.0   2.0   3.0
mouse                            
ANM255200  79.2  78.3  73.8  80.9
ANM255201  85.1  90.9  83.5  81.0
ANM255203  74.2  69.0  60.0  70.8
ANM257772  79.5  82.2  80.6  66.9
  paired t-test against control:
 condition                            label  mice  control_%  photoinhibition_%    drop       t      p
         2  ipsi 1 spot early delay (0.5 s)     4    79.4999            74.4574  5.0425 -1.5123 0.2277
         3 ipsi 1 spot middle delay (0.5 s)     4    79.4999            74.8932  4.6068 -1.5588 0.2169
         1       ipsi 1 spot sample (0.5 s)     4    79.4999            80.1359 -0.6360  0.2678 0.8062
  unpaired t-test against control:
 condition                            label  mice  control_%  photoinhibition_%    drop       t      p
         2  ipsi 1 spot early delay (0.5 s)     4    79.4999            74.4574  5.0425 -0.8886 0.4084
         3 ipsi 1 spot middle delay (0.5 s)     4    79.4999            74.8932  4.6068 -1.0973 0.3146
         1       ipsi 1 spot sample (0.5 s)     4    79.4999            80.1359 -0.6360  0.1261 0.9038
Performance (% correct) per mouse, session_mean:
[... 99 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev && . ../v/bin/activate && python run.py nb.py "SANITY" "fig5b-call" 2>&1 | grep -v "^---" | tail -36
```

```
condition                         label  mice  control_%  photoinhibition_%    drop        t      p
        10       CCX ipsi 1 spot (0.8 s)     7    74.5779            59.1038 15.4741  -4.7084 0.0033
        11     CCX contra 1 spot (0.8 s)     7    74.5779            64.2254 10.3526  -4.3732 0.0047
        12 CCX bilateral 4 spots (0.8 s)     7    74.5779            51.4775 23.1004 -15.0276 0.0000
  unpaired t-tests against control:
 condition                         label  mice  control_%  photoinhibition_%    drop       t      p
        10       CCX ipsi 1 spot (0.8 s)     7    74.5779            59.1038 15.4741 -3.9667 0.0019
        11     CCX contra 1 spot (0.8 s)     7    74.5779            64.2254 10.3526 -3.1705 0.0081
        12 CCX bilateral 4 spots (0.8 s)     7    74.5779            51.4775 23.1004 -9.7941 0.0000

Performance (% correct) per mouse, session_mean:
stim       0.0   10.0  11.0  12.0
mouse                            
ANM270340  69.3  69.9  61.8  53.0
ANM278733  76.1  67.1  72.6  57.2
ANM291063  74.2  60.8  66.1  55.1
ANM291064  68.8  38.7  57.9  45.7
ANM297634  71.2  46.8  49.9  42.9
ANM298738  80.0  56.9  62.2  49.8
ANM298740  77.5  65.4  67.5  56.0
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . v/bin/activate && python -c "
import pickle,numpy as np
S=pickle.load(open('sessions.pkl','rb'))
for s in S[::9]:
    g=s['good']&np.isfinite(s['cue'])&(s['trial_types']['HitR']|s['trial_types']['HitL'])
    rt=(s['first_lick']-s['cue'])[g]
    g2=s['good']&s['trial_types']['NoLickR']
    print(s['name'], round(s['lick_median'],3), round(s['lick_p999'],3), 'RT pct', np.round(np.nanpercentile(rt,[5,25,50,75,95]),3), 'nan',np.isnan(rt).mean().round(2), 'first_any-cue on hits', np.round(np.nanpercentile((s['first_lick_any']-s['cue'])[g],[5,50,95]),2))
"
```

```
/tmp/claude-1001/v/lib/python3.13/site-packages/numpy/lib/_nanfunctions_impl.py:1592: RuntimeWarning: Mean of empty slice
  return np.nanmean(a, axis, out=out, keepdims=keepdims)
<string>:8: RuntimeWarning: Mean of empty slice
/tmp/claude-1001/v/lib/python3.13/site-packages/numpy/_core/_methods.py:142: RuntimeWarning: invalid value encountered in scalar divide
  ret = ret.dtype.type(ret / rcount)
ANM255200_20140910 0.188 0.191 RT pct [0.    0.    0.001 0.002 0.009] nan 0.01 first_any-cue on hits [-3.62 -3.17 -3.17]
ANM255201_20141122 0.194 0.196 RT pct [0.    0.001 0.002 0.006 0.022] nan 0.0 first_any-cue on hits [-3.23 -3.17 -3.07]
ANM257636_20150330 0.097 0.177 RT pct [0.072 0.085 0.179 0.196 0.55 ] nan 0.11 first_any-cue on hits [0.07 0.18 0.54]
ANM257772_20141121 0.191 0.193 RT pct [0.    0.001 0.002 0.006 0.018] nan 0.05 first_any-cue on hits [-4.8  -3.57 -3.54]
ANM263808_20150121 0.176 0.178 RT pct [0.    0.    0.001 0.002 0.005] nan 0.12 first_any-cue on hits [-5.95 -3.57 -3.57]
ANM263810_20150124 0.178 0.18 RT pct [0.    0.    0.001 0.002 0.004] nan 0.0 first_any-cue on hits [-3.57 -3.57 -3.56]
ANM270340_20150618 0.153 0.163 RT pct nan nan nan first_any-cue on hits nan
ANM278733_20150528 0.108 0.163 RT pct [0.089 0.138 0.182 0.2   0.233] nan 0.02 first_any-cue on hits [-3.56  0.18  0.23]
ANM291063_20150907 0.165 0.167 RT pct [0.    0.001 0.004 0.011 0.029] nan 0.01 first_any-cue on hits [-4.29 -3.57 -3.54]
ANM297634_20150911 0.154 0.161 RT pct [0.186 0.208 0.287 0.423 0.63 ] nan 0.02 first_any-cue on hits [-3.57 -2.83  0.35]
ANM298740_20150729 0.058 0.162 RT pct [0.192 0.43  0.558 0.704 1.184] nan 0.27 first_any-cue on hits [-9.47  0.43  1.06]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat >> entries/crcns-alm-3-li-2016/alm3.py <<'EOF'


# ---------------------------------------------------------------- population analyses

POP_T = np.round(np.arange(-3.5, 1.0 + 1e-9, 0.01), 3)  # window starts; windows [t, t + 0.4]


def population_session(s, sess_units, conds, cell_types=("pyramidal",), seed=0, split="code"):
    """Trials x neurons x windows rates for one session, with the code's trial selection.

    Neurons: units of `cell_types` whose stable trials include trial 50 and the 50th from the end
    (code, analysis_compile_all_data_bilateral_activityModes.m). Trials: performing, not
    lick-early, stable for every neuron, correct and error grouped by instructed movement.
    Rates: spike counts in 400 ms windows starting every 10 ms from 3.5 s before to 1 s after the
    cue, over 0.4 s (Methods; code). Control trials are split into a training set (for cd, the
    decision boundary and the offset) and a test set: split = "code", as many test trials of each
    type as the mean number of photoinhibition trials per type and condition (code); split =
    "half", one random half of each type (M6 reading a).
    Returns None when the session has 5 or fewer neurons or fewer than 5 trials in a group (code).
    """
    n_tr = len(s["trial_ids"])
    keep = []
    for u in sess_units:
        su = s["units"][u["unit"]]
        if u["cell_type"] not in cell_types:
            continue
        ids = s["trial_ids"]
        if not (su["first_trial"] <= 50 <= su["last_trial"] and su["first_trial"] <= ids[-1] - 50 <= su["last_trial"]):
            continue
        keep.append(u)
    if not keep:
        return None
    trials = keep[0]["trials"]
    stable = np.all([u["stable"] for u in keep], axis=0)
    sd = side(s)[trials]
    st = s["stim_type"][trials]
    le = s["trial_types"]["LickEarly"][trials]
    hit = (s["trial_types"]["HitR"] | s["trial_types"]["HitL"])[trials]
    ok = stable & ~le & (sd != 0)
    groups = {(c, d): np.flatnonzero(ok & (st == c) & (sd == d)) for c in [0] + list(conds) for d in (1, -1)}
    rng = np.random.default_rng(seed)
    n_test = int(round(np.mean([len(groups[(c, d)]) for c in conds for d in (1, -1)])))
    train, test = {}, {}
    for d in (1, -1):
        g = rng.permutation(groups[(0, d)])
        n_t = n_test if split == "code" else len(g) // 2
        test[d], train[d] = g[len(g) - n_t:], g[:len(g) - n_t]
    counts = [len(train[1]), len(train[-1]), len(test[1]), len(test[-1])] + [len(groups[(c, d)]) for c in conds for d in (1, -1)]
    if len(keep) <= 5 or min(counts) < 5:
        return None
    X = np.stack([binned_window(u["binned"], POP_T + 0.2, 0.4) / 0.4 for u in keep], axis=1)  # trials x neurons x windows
    return {"session": s["name"], "mouse": s["mouse"], "X": X, "side": sd, "hit": hit, "stim": st,
            "train": train, "test": test, "groups": groups, "n_neurons": len(keep), "counts": counts,
            "trials": trials}


def lda_direction(XR, XL):
    """Fisher discriminant direction (code, func_discriminant.m), sign so that R projects higher."""
    x = np.vstack([XL, XR])
    xm = x.mean(0)
    xc = x - xm
    T = xc.T @ xc
    W = np.zeros_like(T)
    for g in (XL, XR):
        z = g - g.mean(0)
        W += z.T @ z
    B = T - W
    _, _, vt = np.linalg.svd(np.linalg.pinv(W) @ B)
    v = vt[0]
    if (XR @ v).mean() < (XL @ v).mean():
        v = -v
    return v


def boundary(pR, pL):
    """Decision boundary: inverse-variance weighted mean of the two class means (Methods; code)."""
    vR, vL = np.var(pR, ddof=1), np.var(pL, ddof=1)
    return (pR.mean() / vR + pL.mean() / vL) / (1 / vR + 1 / vL)


def auc(a, b):
    """Area under the ROC curve for separating a (positive) from b."""
    from scipy.stats import mannwhitneyu
    if len(a) == 0 or len(b) == 0:
        return np.nan
    return mannwhitneyu(a, b).statistic / (len(a) * len(b))
EOF
date -u
```

```
Sat Nov  7 19:50:24 UTC 2026
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/dev/nb.py <<'EOF'
# %% SETUP7
# Population analyses (Methods, Analysis of population dynamics in the activity space; code,
# analysis_compile_all_data_bilateral_activityModes.m).
def tidx(t):
    return int(np.argmin(np.abs(alm3.POP_T - t)))

I_LATE = tidx(-0.4)   # window [-0.4, 0]: last 400 ms of the delay

def cd_windows(reading):
    """Windows (by start time) counted as in the sample and delay epochs (-3.0 to 0 s from the
    cue, 1.3 s sample and 1.7 s delay): (b) wholly inside, as the code (start > -3, <= -0.4);
    (a) centre inside."""
    if reading == "inside":
        return np.flatnonzero((alm3.POP_T > -3.0 - 1e-9) & (alm3.POP_T <= -0.4 + 1e-9))
    return np.flatnonzero((alm3.POP_T + 0.2 >= -3.0 - 1e-9) & (alm3.POP_T + 0.2 <= 0 + 1e-9))

def cd_vector(P, train_R, train_L, kind, win_reading):
    X = P["X"]
    win = cd_windows(win_reading)
    if kind == "meandiff":
        w = (X[train_R][:, :, win].mean(0) - X[train_L][:, :, win].mean(0)).mean(1)
    else:  # the code's LDA per window, averaged
        w = np.mean([alm3.lda_direction(X[train_R][:, :, i], X[train_L][:, :, i]) for i in win[::5]], axis=0)
    return w / np.linalg.norm(w)

def cd_projections(P, kind="meandiff", win_reading="inside", w=None):
    """Projection of every trial on cd at every window, minus the decision boundary in the last
    400 ms of the delay, from correct training trials."""
    hit = P["hit"]
    tR = P["train"][1][hit[P["train"][1]]]
    tL = P["train"][-1][hit[P["train"][-1]]]
    if w is None:
        w = cd_vector(P, tR, tL, kind, win_reading)
    proj = np.einsum("tnw,n->tw", P["X"], w)
    b = alm3.boundary(proj[tR, I_LATE], proj[tL, I_LATE])
    return proj - b, w, (tR, tL)

def session_rocs(P, proj, conds, t_index=I_LATE, average=None):
    out = {}
    def val(idx):
        return proj[idx][:, average].mean(1) if average is not None else proj[idx, t_index]
    out[0] = alm3.auc(val(P["test"][1]), val(P["test"][-1]))
    for c in conds:
        out[c] = alm3.auc(val(P["groups"][(c, 1)]), val(P["groups"][(c, -1)]))
    return out

def build_population(exp, conds, cell_types=("pyramidal",), split="code", seed=7):
    pops = []
    for i, name in enumerate(ses[ses.experiment == exp].session):
        su = [u for u in units if u["session"] == name]
        if not su:
            continue
        P = alm3.population_session(SD[name], su, conds, cell_types=cell_types, seed=seed + i, split=split)
        if P is not None:
            pops.append(P)
    return pops

POP = {}
for exp, conds in (("exp2", [4, 5, 6]), ("exp3", [7, 8, 9]), ("ccx", [10, 11, 12])):
    for cells in ("pyramidal", "all"):
        for split in ("code", "half"):
            ct = ("pyramidal",) if cells == "pyramidal" else ("pyramidal", "FS", "none")
            POP[(exp, cells, split)] = build_population(exp, conds, ct, split)
for k, v in POP.items():
    print(k, "sessions", len(v), "mice", len({p["mouse"] for p in v}), "neurons", sum(p["n_neurons"] for p in v))

# %% [markdown]
# ## fig3-cd-roc
#
# Claim: along the coding direction, trajectories recover after ipsilateral photoinhibition (ROC
# at the end of the delay 0.73 +- 0.02 against control 0.76 +- 0.03), are little affected by
# contralateral photoinhibition (0.74 +- 0.03) and stay collapsed after bilateral photoinhibition
# (0.58 +- 0.03); 16 sessions. Readings run: neurons pyramidal only (code) or all units; split of
# control trials as the code or random halves (M6 a); cd as the mean difference of the Methods
# with windows wholly inside (code) or centred in the sample and delay, and the code's LDA as a
# variant. ROC: area under the ROC curve of lick right against lick left projections in the last
# 400 ms of the delay, control test trials and each photoinhibition condition, per session,
# mean +- s.e.m. over sessions.

# %% tags=claim:fig3-cd-roc
def roc_table(exp, conds, kinds=(("meandiff", "inside"), ("meandiff", "centre"), ("lda", "inside")), **kw):
    rows = []
    for (e, cells, split), pops in POP.items():
        if e != exp:
            continue
        for kind, wr in kinds:
            R = []
            for P in pops:
                proj, w, _ = cd_projections(P, kind, wr)
                R.append(session_rocs(P, proj, conds, **kw))
            R = pd.DataFrame(R)
            r = {"cells": cells, "split": split, "cd": f"{kind}/{wr}", "sessions": len(R)}
            for c in [0] + conds:
                r[f"roc_{c}"] = R[c].mean()
                r[f"sem_{c}"] = R[c].std(ddof=1) / np.sqrt(len(R))
            rows.append(r)
    return pd.DataFrame(rows)

rt3 = roc_table("exp2", [4, 5, 6])
exp3v = {0: (0.76, 0.03), 4: (0.73, 0.02), 5: (0.74, 0.03), 6: (0.58, 0.03)}
rt3["all_within"] = np.all([(rt3[f"roc_{c}"] - v).abs() <= tol for c, (v, tol) in exp3v.items()], axis=0)
rt3["order"] = (rt3[["roc_0", "roc_4", "roc_5"]].min(1) - rt3["roc_6"]) > 0.1
print(rt3.round(3).to_string(index=False))
print("Paper: 16 sessions; control 0.76 +- 0.03, ipsilateral 0.73 +- 0.02, contralateral 0.74 +- 0.03, bilateral 0.58 +- 0.03.")
P0 = POP[("exp2", "pyramidal", "code")]
print("\nSessions (code selection, pyramidal):", [(p["session"], p["n_neurons"]) for p in P0])
R = pd.DataFrame([session_rocs(P, cd_projections(P)[0], [4, 5, 6]) for P in P0])
R["mouse"] = [p["mouse"] for p in P0]
print("Per mouse (mean over sessions), mean-difference cd, code split:")
print(R.groupby("mouse").mean().round(3).to_string())
EOF
cd $TMPDIR/dev && . ../v/bin/activate && python run.py nb.py "SANITY" "SETUP7" "fig3-cd-roc" 2>&1 | grep -v "^---" | tail -45
```

```
50%       0.028
75%       0.069
max       2.181
Sessions with ratio above 0.5: [{'session': 'ANM257636_20150404', 'experiment': 'exp2b', 'neurons': 6, 'ratio': 2.04}, {'session': 'ANM264411_20141224', 'experiment': 'exp2', 'neurons': 21, 'ratio': 0.82}, {'session': 'ANM273657_20150325', 'experiment': 'exp2b', 'neurons': 13, 'ratio': 0.71}, {'session': 'ANM298738_20150727', 'experiment': 'ccx', 'neurons': 19, 'ratio': 2.18}]
Sessions with photostimulation but no pyramidal neuron to check: []
measures for 1579 units in 10 s
('exp2', 'pyramidal', 'code') sessions 16 mice 7 neurons 175
('exp2', 'pyramidal', 'half') sessions 16 mice 7 neurons 175
('exp2', 'all', 'code') sessions 17 mice 7 neurons 211
('exp2', 'all', 'half') sessions 17 mice 7 neurons 211
('exp3', 'pyramidal', 'code') sessions 4 mice 3 neurons 48
('exp3', 'pyramidal', 'half') sessions 4 mice 3 neurons 48
('exp3', 'all', 'code') sessions 5 mice 3 neurons 58
('exp3', 'all', 'half') sessions 5 mice 3 neurons 58
('ccx', 'pyramidal', 'code') sessions 16 mice 7 neurons 259
('ccx', 'pyramidal', 'half') sessions 16 mice 7 neurons 259
('ccx', 'all', 'code') sessions 17 mice 7 neurons 290
('ccx', 'all', 'half') sessions 17 mice 7 neurons 290
    cells split              cd  sessions  roc_0  sem_0  roc_4  sem_4  roc_5  sem_5  roc_6  sem_6  all_within  order
pyramidal  code meandiff/inside        16  0.719  0.033  0.706  0.024  0.738  0.033  0.595  0.036       False   True
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/dev/nb.py <<'EOF'
# %% [markdown]
# ## ed8-roc-during-photoinhibition
#
# Claim: during photoinhibition the cd separation falls (ROC 0.54 +- 0.03 ipsilateral, 0.64 +- 0.03
# contralateral, 0.54 +- 0.01 bilateral, against control 0.72 +- 0.02). Window (a) the 400 ms
# window ending at the start of the offset ramp (1.5 to 1.1 s before the cue), (b) the projection
# averaged over the windows inside the 0.8 s photoinhibition (criterion). Other readings as fig3-cd-roc.

# %% tags=claim:ed8-roc-during-photoinhibition
exp8 = {0: (0.72, 0.02), 4: (0.54, 0.03), 5: (0.64, 0.03), 6: (0.54, 0.01)}
during_avg = np.flatnonzero((alm3.POP_T >= -1.7 - 1e-9) & (alm3.POP_T <= -1.3 + 1e-9))
tabs = []
for lab, kw in (("(a) 400 ms ending at ramp start", {"t_index": tidx(-1.5)}), ("(b) average over photoinhibition", {"average": during_avg})):
    t = roc_table("exp2", [4, 5, 6], **kw)
    t.insert(0, "window", lab)
    tabs.append(t)
rt8 = pd.concat(tabs, ignore_index=True)
rt8["all_within"] = np.all([(rt8[f"roc_{c}"] - v).abs() <= tol for c, (v, tol) in exp8.items()], axis=0)
print(rt8.round(3).to_string(index=False))
print("Paper: control 0.72 +- 0.02, ipsilateral 0.54 +- 0.03, contralateral 0.64 +- 0.03, bilateral 0.54 +- 0.01.")

# %% [markdown]
# ## ed7e-size-and-roc
#
# Claim: recovery of selectivity after unilateral photoinhibition is less robust with larger
# photoinhibition, and cd trajectories separate at the end of the delay with ROC 0.80 +- 0.08
# (control), 0.64 +- 0.10 (ipsilateral 4 spots), 0.68 +- 0.15 (contralateral 4 spots) and 0.54
# (bilateral 1 spot; tolerance 0.054, 0.08 as a variant). Experiment 3 sessions with > 5 neurons
# and enough trials (the session rule of fig3-cd-roc); "less robust" judged by the ipsilateral 4-spot
# ROC below the Experiment 2 ipsilateral 1-spot ROC.

# %% tags=claim:ed7e-size-and-roc
rt7 = roc_table("exp3", [7, 8, 9])
exp7 = {0: (0.80, 0.08), 8: (0.64, 0.10), 9: (0.68, 0.15), 7: (0.54, 0.054)}
rt7["all_within"] = np.all([(rt7[f"roc_{c}"] - v).abs() <= tol for c, (v, tol) in exp7.items()], axis=0)
rt7["all_within_bilat_tol_0.08"] = np.all([(rt7[f"roc_{c}"] - v).abs() <= (0.08 if c == 7 else tol) for c, (v, tol) in exp7.items()], axis=0)
print(rt7.round(3).to_string(index=False))
m = rt3.set_index(["cells", "split", "cd"])["roc_4"]
rt7["exp2_ipsi_1spot"] = [m.get((r.cells, r.split, r.cd)) for r in rt7.itertuples()]
print("\nIpsilateral 4 spots (Experiment 3) against ipsilateral 1 spot (Experiment 2):")
print(rt7[["cells", "split", "cd", "roc_8", "exp2_ipsi_1spot"]].round(3).to_string(index=False))
print("Sessions (code selection, pyramidal):", [(p["session"], p["n_neurons"], p["counts"]) for p in POP[("exp3", "pyramidal", "code")]])
print("Experiment 3 sessions in the data set:", ses[ses.experiment == "exp3"].session.tolist())
EOF
cd $TMPDIR/dev && . ../v/bin/activate && python run.py nb.py "SANITY" "SETUP7" "fig3-cd-roc" "ed8-roc" "ed7e-size" 2>&1 | grep -v "^---" | tail -50
```

```
(a) 400 ms ending at ramp start pyramidal  half      lda/inside        16  0.713  0.025  0.490  0.034  0.617  0.041  0.488  0.020       False
 (a) 400 ms ending at ramp start       all  code meandiff/inside        17  0.692  0.036  0.521  0.044  0.631  0.035  0.505  0.024       False
 (a) 400 ms ending at ramp start       all  code meandiff/centre        17  0.694  0.036  0.518  0.045  0.627  0.035  0.506  0.024       False
 (a) 400 ms ending at ramp start       all  code      lda/inside        17  0.692  0.035  0.529  0.044  0.631  0.039  0.526  0.023       False
 (a) 400 ms ending at ramp start       all  half meandiff/inside        17  0.702  0.023  0.522  0.042  0.608  0.039  0.508  0.025       False
 (a) 400 ms ending at ramp start       all  half meandiff/centre        17  0.707  0.023  0.510  0.045  0.608  0.038  0.505  0.026       False
 (a) 400 ms ending at ramp start       all  half      lda/inside        17  0.708  0.021  0.534  0.044  0.605  0.042  0.514  0.025       False
(b) average over photoinhibition pyramidal  code meandiff/inside        16  0.714  0.036  0.590  0.041  0.631  0.031  0.509  0.019       False
(b) average over photoinhibition pyramidal  code meandiff/centre        16  0.718  0.036  0.583  0.040  0.632  0.031  0.508  0.017       False
(b) average over photoinhibition pyramidal  code      lda/inside        16  0.717  0.035  0.561  0.038  0.630  0.031  0.526  0.020       False
(b) average over photoinhibition pyramidal  half meandiff/inside        16  0.714  0.025  0.595  0.041  0.617  0.039  0.515  0.023       False
(b) average over photoinhibition pyramidal  half meandiff/centre        16  0.717  0.025  0.589  0.041  0.613  0.037  0.515  0.023       False
(b) average over photoinhibition pyramidal  half      lda/inside        16  0.719  0.027  0.561  0.035  0.614  0.041  0.515  0.023       False
(b) average over photoinhibition       all  code meandiff/inside        17  0.703  0.038  0.534  0.043  0.642  0.036  0.539  0.023        True
[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cat >> $TMPDIR/dev/nb.py <<'EOF'
# %% [markdown]
# ## ed9b-cd-stability
#
# Claim: the direction of the lick right minus lick left response difference is stable through the
# sample and delay epochs (correlation between late sample and late delay 0.61 +- 0.05). Per
# session of fig3-cd-roc, Pearson correlation of w in the last 400 ms of the sample epoch (1.7 to
# 2.1 s before the cue) and in the last 400 ms of the delay, correct control trials (criterion);
# all correct control trials (a reading) or the correct training trials (as for cd).

# %% tags=claim:ed9b-cd-stability
rows = []
for (e, cells, split), pops in POP.items():
    if e != "exp2" or split != "code":
        continue
    for trial_set in ("all correct control", "correct training"):
        rr = []
        for P in pops:
            hit = P["hit"]
            if trial_set == "all correct control":
                R_ = np.r_[P["train"][1], P["test"][1]]
                L_ = np.r_[P["train"][-1], P["test"][-1]]
            else:
                R_, L_ = P["train"][1], P["train"][-1]
            R_, L_ = R_[hit[R_]], L_[hit[L_]]
            X = P["X"]
            w1 = X[R_][:, :, tidx(-2.1)].mean(0) - X[L_][:, :, tidx(-2.1)].mean(0)
            w2 = X[R_][:, :, I_LATE].mean(0) - X[L_][:, :, I_LATE].mean(0)
            rr.append(np.corrcoef(w1, w2)[0, 1])
        rr = np.array(rr)
        rows.append({"cells": cells, "trials": trial_set, "sessions": len(rr), "mean_r": np.nanmean(rr), "sem": np.nanstd(rr, ddof=1) / np.sqrt(np.isfinite(rr).sum()),
                     "within_0.61+-0.05": abs(np.nanmean(rr) - 0.61) <= 0.05})
print(pd.DataFrame(rows).round(3).to_string(index=False))
print("Paper: 0.61 +- 0.05.")

# %% [markdown]
# ## ed8a-mode-variance
#
# Claim: the projection on cd captures 65.6 +- 5.1% of population selectivity and 36.4 +- 6.3% of
# task-related activity variance over the sample and delay epochs; modes 1 to 5 together explain
# 98.5 +- 0.5% of the variance and 95.8 +- 1.2% of the selectivity. Modes as in the Methods and
# the code: mode 1 cd; modes 2 and 3 the ipsilateral perturbed minus unperturbed mean response in
# the last 400 ms of the delay, lick right and lick left; modes 4 and 5 the first singular vectors
# of the baseline-subtracted lick right and lick left mean responses concatenated over the sample
# and delay windows; each Gram-Schmidt orthogonal to the earlier ones. Training control trials
# (code). Baseline (a) the window before the sample (3.4 to 3.0 s before the cue, the code's
# `time_bins <= -3.4`), (b) the mean over the trial. Share (a) RMS ratio, (b) squared norms (the
# code). Total variance and selectivity: the squared norm over the full neuron space (code). cd
# as the mean difference (Methods) or LDA (code).

# %% tags=claim:ed8a-mode-variance
def gram_schmidt(vs):
    out = []
    for v in vs:
        v = v.astype(float).copy()
        for o in out:
            v -= (v @ o) * o
        n = np.linalg.norm(v)
        if n > 1e-12:
            out.append(v / n)
    return out

SD_WIN = np.flatnonzero((alm3.POP_T > -3.0 - 1e-9) & (alm3.POP_T <= -0.4 + 1e-9))

def modes_for(P, kind="meandiff", baseline="pre"):
    X = P["X"]
    trR, trL = P["train"][1], P["train"][-1]
    _, w1, _ = cd_projections(P, kind, "inside")
    iR, iL = P["groups"][(4, 1)], P["groups"][(4, -1)]
    w2 = X[iR][:, :, I_LATE].mean(0) - X[trR][:, :, I_LATE].mean(0)
    w3 = X[iL][:, :, I_LATE].mean(0) - X[trL][:, :, I_LATE].mean(0)
    R = X[trR][:, :, SD_WIN].mean(0)
    L = X[trL][:, :, SD_WIN].mean(0)
    if baseline == "pre":
        base = X[np.r_[trR, trL]][:, :, tidx(-3.4)].mean(0)
    else:
        base = X[np.r_[trR, trL]].mean(axis=(0, 2))
    A = np.concatenate([R, L], axis=1) - base[:, None]
    u, sv, vt = np.linalg.svd(A, full_matrices=False)
    basis = gram_schmidt([w1, w2, w3] + [u[:, i] for i in range(u.shape[1])])
    return basis, A, R - L

rows = []
for cells in ("pyramidal", "all"):
    pops = POP[("exp2", cells, "code")]
    for kind in ("meandiff", "lda"):
        for baseline in ("pre", "trial"):
            vals = []
            for P in pops:
                basis, A, S = modes_for(P, kind, baseline)
                tot_v, tot_s = (A ** 2).sum(), (S ** 2).sum()
                pv = [((A.T @ b) ** 2).sum() / tot_v for b in basis[:5]]
                ps = [((S.T @ b) ** 2).sum() / tot_s for b in basis[:5]]
                vals.append({"var_cd": pv[0], "sel_cd": ps[0], "var_1_5": sum(pv), "sel_1_5": sum(ps),
                             "var_cd_rms": np.sqrt(pv[0]), "sel_cd_rms": np.sqrt(ps[0]), "var_1_5_rms": np.sqrt(sum(pv)), "sel_1_5_rms": np.sqrt(sum(ps)),
                             "var_mode4": pv[3], "n": P["n_neurons"]})
            v = pd.DataFrame(vals)
            for share in ("squared", "rms"):
                suf = "" if share == "squared" else "_rms"
                r = {"cells": cells, "cd": kind, "baseline": baseline, "share": share, "sessions": len(v)}
                for q in ("sel_cd", "var_cd", "var_1_5", "sel_1_5"):
                    r[q] = 100 * v[q + suf].mean()
                    r[q + "_sem"] = 100 * v[q + suf].std(ddof=1) / np.sqrt(len(v))
                rows.append(r)
e8a = pd.DataFrame(rows)
expa = {"sel_cd": (65.6, 5.1), "var_cd": (36.4, 6.3), "var_1_5": (98.5, 0.5), "sel_1_5": (95.8, 1.2)}
e8a["all_within"] = np.all([(e8a[q] - v).abs() <= t for q, (v, t) in expa.items()], axis=0)
e8a["cd_within"] = np.all([(e8a[q] - v).abs() <= t for q, (v, t) in list(expa.items())[:2]], axis=0)
print(e8a.round(1).to_string(index=False))
print("Paper: selectivity on cd 65.6 +- 5.1%, variance on cd 36.4 +- 6.3%, modes 1-5: variance 98.5 +- 0.5%, selectivity 95.8 +- 1.2%.")
print("Neurons per session (pyramidal):", [p["n_neurons"] for p in POP[("exp2", "pyramidal", "code")]])
EOF
cd $TMPDIR/dev && . ../v/bin/activate && python run.py nb.py "SANITY" "SETUP7" "ed9b-cd" "ed8a-mode" 2>&1 | grep -v "^---" | tail -28
```

```
Sat Nov  7 19:52:05 UTC 2026
('ccx', 'all', 'code') sessions 17 mice 7 neurons 290
('ccx', 'all', 'half') sessions 17 mice 7 neurons 290
    cells              trials  sessions  mean_r   sem  within_0.61+-0.05
pyramidal all correct control        16   0.590 0.075               True
pyramidal    correct training        16   0.520 0.081              False
      all all correct control        17   0.622 0.060               True
      all    correct training        17   0.570 0.057               True
Paper: 0.61 +- 0.05.
    cells       cd baseline   share  sessions  sel_cd  sel_cd_sem  var_cd  var_cd_sem  var_1_5  var_1_5_sem  sel_1_5  sel_1_5_sem  all_within  cd_within
pyramidal meandiff      pre squared        16    72.5         3.6    39.5         6.2     97.1          0.6     93.9          1.2       False      False
pyramidal meandiff      pre     rms        16    84.7         2.2    60.3         4.6     98.5          0.3     96.9          0.6       False      False
pyramidal meandiff    trial squared        16    72.5         3.6    40.7         5.6     95.5          0.9     93.7          1.4       False      False
pyramidal meandiff    trial     rms        16    84.7         2.2    61.7         4.2     97.7          0.5     96.8          0.7       False      False
pyramidal      lda      pre squared        16    66.1         4.1    36.6         5.9     96.9          0.7     93.4          1.4       False       True
pyramidal      lda      pre     rms        16    80.7         2.5    57.8         4.6     98.4          0.3     96.6          0.7       False      False
pyramidal      lda    trial squared        16    66.1         4.1    37.6         5.5     95.2          1.0     93.0          1.6       False       True
pyramidal      lda    trial     rms        16    80.7         2.5    59.0         4.3     97.6          0.5     96.4          0.9       False      False
      all meandiff      pre squared        17    73.2         3.5    41.2         5.5     97.3      
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/dev/nb.py <<'EOF'
# %% [markdown]
# ## fig3-cd-predicts-movement
#
# Claim: deviations along the coding direction predict the upcoming movement trial by trial, in
# control trials and after unilateral and bilateral perturbation. Trials pooled over the sessions
# of fig3-cd-roc (Methods); per condition, the fraction of trials whose lick (the instructed side
# on correct trials, the other side on errors) is on the side of the decision boundary where the
# projection lies, with a binomial test against 0.5, and a logistic regression of lick right on
# the signed projection (criterion). Control trials are the test trials. cd of unit length
# (reading b of the scaling; the tests do not depend on the scale).

# %% tags=claim:fig3-cd-predicts-movement
import statsmodels.api as sm

def pooled_projections(pops, conds, kind="meandiff", which="cd", t_index=I_LATE):
    rows = []
    for P in pops:
        if which == "cd":
            proj, _, _ = cd_projections(P, kind, "inside")
        else:
            proj = which(P)
        lick_right = np.where(P["hit"], P["side"] == 1, P["side"] == -1)
        for c in [0] + conds:
            idx = np.r_[P["test"][1], P["test"][-1]] if c == 0 else np.r_[P["groups"][(c, 1)], P["groups"][(c, -1)]]
            for i in idx:
                rows.append({"session": P["session"], "mouse": P["mouse"], "condition": c, "proj": proj[i, t_index],
                             "lick_right": bool(lick_right[i]), "instructed_right": P["side"][i] == 1, "hit": bool(P["hit"][i])})
    return pd.DataFrame(rows)

def prediction_table(df):
    rows = []
    for c, d in df.groupby("condition"):
        pred = d.proj > 0
        correct = int((pred == d.lick_right).sum())
        b = stats.binomtest(correct, len(d), 0.5, alternative="greater")
        lr = sm.Logit(d.lick_right.astype(float), sm.add_constant(d.proj.values)).fit(disp=0)
        rows.append({"condition": c, "label": "control" if c == 0 else alm3.STIM_LABELS[c], "trials": len(d), "accuracy": correct / len(d),
                     "binom_p": b.pvalue, "logit_slope": lr.params[1], "logit_p": lr.pvalues[1],
                     "accuracy_error_trials": ((d.proj > 0) == d.lick_right)[~d.hit].mean(), "error_trials": int((~d.hit).sum())})
    return pd.DataFrame(rows)

for cells in ("pyramidal", "all"):
    dfp = pooled_projections(POP[("exp2", cells, "code")], [4, 5, 6])
    print(f"Neurons: {cells}")
    print(prediction_table(dfp).round(4).to_string(index=False))
dfp = pooled_projections(POP[("exp2", "pyramidal", "code")], [4, 5, 6])
print("\nFraction of lick right responses by projection bin (control and bilateral, pyramidal):")
dfp["bin"] = pd.cut(dfp.proj, [-np.inf, -10, -5, -2, 0, 2, 5, 10, np.inf])
print(dfp[dfp.condition.isin([0, 6])].groupby(["condition", "bin"], observed=True).lick_right.agg(["mean", "size"]).round(2).to_string())
print("Projection range (spikes/s along unit-length cd):", round(dfp.proj.min(), 1), "to", round(dfp.proj.max(), 1))

# %% [markdown]
# ## fig3-other-modes
#
# Claim: the persistent mode is altered by perturbation but neither discriminates trial type nor
# predicts behaviour; the ramping mode shows non-selective ramping, is resistant to perturbation
# and does not predict behaviour. Modes 2 (persistent, lick right) and 4 (ramping) of
# ed8a-mode-variance, mean-difference cd, pre-sample baseline; decision boundaries as for cd and
# signs so that lick right projects higher on training trials (code). Criterion: ROC in the last
# 400 ms of the delay within 0.5 +- 0.1 over sessions and control prediction accuracy with binomial
# p > 0.05; ramping-mode projection for ipsilateral and bilateral trials within the s.e.m. band of
# the control projection over sessions, persistent-mode projection outside it for ipsilateral.

# %% tags=claim:fig3-other-modes
def mode_projection(P, mode_index, kind="meandiff"):
    basis, _, _ = modes_for(P, kind, "pre")
    w = basis[mode_index]
    proj = np.einsum("tnw,n->tw", P["X"], w)
    hit = P["hit"]
    tR = P["train"][1][hit[P["train"][1]]]
    tL = P["train"][-1][hit[P["train"][-1]]]
    if proj[tR, I_LATE].mean() < proj[tL, I_LATE].mean():
        proj = -proj
    return proj - alm3.boundary(proj[tR, I_LATE], proj[tL, I_LATE]), proj

for cells in ("pyramidal", "all"):
    pops = POP[("exp2", cells, "code")]
    print(f"Neurons: {cells}")
    for mi, name in ((1, "persistent (mode 2)"), (3, "ramping (mode 4)"), (0, "cd (mode 1), for comparison")):
        rocs, raw = [], []
        for P in pops:
            pr, praw = mode_projection(P, mi)
            rocs.append(session_rocs(P, pr, [4, 5, 6]))
            # mean raw projection in the last 400 ms of the delay, per condition, both trial types
            r = {0: praw[np.r_[P["test"][1], P["test"][-1]], I_LATE].mean()}
            for c in (4, 5, 6):
                r[c] = praw[np.r_[P["groups"][(c, 1)], P["groups"][(c, -1)]], I_LATE].mean()
            raw.append(r)
        rocs, raw = pd.DataFrame(rocs), pd.DataFrame(raw)
        dfm = pooled_projections(pops, [4, 5, 6], which=lambda P, mi=mi: mode_projection(P, mi)[0])
        pt = prediction_table(dfm).set_index("condition")
        diff = raw[[4, 5, 6]].sub(raw[0], axis=0)
        sem0 = raw[0].std(ddof=1) / np.sqrt(len(raw))
        print(f"  {name}: ROC control {rocs[0].mean():.3f} +- {rocs[0].std(ddof=1) / np.sqrt(len(rocs)):.3f}, ipsi {rocs[4].mean():.3f}, contra {rocs[5].mean():.3f}, bilateral {rocs[6].mean():.3f}; "
              f"control accuracy {pt.loc[0, 'accuracy']:.3f} (binomial p {pt.loc[0, 'binom_p']:.3g}); "
              f"perturbed minus control projection (mean over sessions): ipsi {diff[4].mean():+.2f}, contra {diff[5].mean():+.2f}, bilateral {diff[6].mean():+.2f}; "
              f"control s.e.m. band {sem0:.2f}")
EOF
cd $TMPDIR/dev && . ../v/bin/activate && python run.py nb.py "SANITY" "SETUP7" "fig3-cd-predicts" "ed8a-mode" "fig3-other-modes" 2>&1 | grep -v "^---" | tail -42 | grep -v "^pyramidal \|^      all "
```

```
Paper: selectivity on cd 65.6 +- 5.1%, variance on cd 36.4 +- 6.3%, modes 1-5: variance 98.5 +- 0.5%, selectivity 95.8 +- 1.2%.
Neurons per session (pyramidal): [13, 16, 16, 13, 20, 6, 10, 9, 6, 12, 9, 9, 9, 7, 6, 14]
Neurons: pyramidal
Traceback (most recent call last):
  File "/tmp/claude-1001/v/lib/python3.13/site-packages/pandas/core/indexes/base.py", line 3816, in get_loc
    return self._engine.get_loc(casted_key)
           ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "pandas/_libs/index.pyx", line 172, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 180, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 671, in pandas._libs.index.StringObjectEngine._check_type
KeyError: 1

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/tmp/claude-1001/dev/run.py", line 15, in <module>
    exec(compile(c, f'cell{i}', 'exec'), g)
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "cell53", line 34, in <module>
  File "cell53", line 27, in prediction_table
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev && sed -i 's/"binom_p": b.pvalue, "logit_slope": lr.params\[1\], "logit_p": lr.pvalues\[1\],/"binom_p": b.pvalue, "logit_slope": np.asarray(lr.params)[1], "logit_p": np.asarray(lr.pvalues)[1],/' nb.py && . ../v/bin/activate && python run.py nb.py "SANITY" "SETUP7" "fig3-cd-predicts" "ed8a-mode" "fig3-other-modes" 2>&1 | grep -v "^---" | tail -52 | grep -v "^pyramidal \|^      all "
```

```
Paper: selectivity on cd 65.6 +- 5.1%, variance on cd 36.4 +- 6.3%, modes 1-5: variance 98.5 +- 0.5%, selectivity 95.8 +- 1.2%.
Neurons per session (pyramidal): [13, 16, 16, 13, 20, 6, 10, 9, 6, 12, 9, 9, 9, 7, 6, 14]
Neurons: pyramidal
 condition                     label  trials  accuracy  binom_p  logit_slope  logit_p  accuracy_error_trials  error_trials
         0                   control     412    0.7282      0.0       0.1454      0.0                 0.6747            83
         4       ipsi 1 spot (0.8 s)     328    0.6860      0.0       0.1381      0.0                 0.5806            93
         5     contra 1 spot (0.8 s)     351    0.6838      0.0       0.1052      0.0                 0.5288           104
         6 bilateral 4 spots (0.8 s)     566    0.6714      0.0       0.1047      0.0                 0.6407           231
Neurons: all
 condition                     label  trials  accuracy  binom_p  logit_slope  logit_p  accuracy_error_trials  error_trials
         0                   control     444    0.7387      0.0       0.1226      0.0                 0.6593            91
         4       ipsi 1 spot (0.8 s)     354    0.7090      0.0       0.0899      0.0                 0.6733           101
         5     contra 1 spot (0.8 s)     379    0.6860      0.0       0.0864      0.0                 0.5315           111
         6 bilateral 4 spots (0.8 s)     611    0.6530      0.0       0.0684      0.0                 0.6342           257

Fraction of lick right responses by projection bin (control and bilateral, pyramidal):
                         mean  size
condition bin                      
0         (-inf, -10.0]  0.03    72
          (-10.0, -5.0]  0.23    56
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/dev/nb.py <<'EOF'
# %% [markdown]
# ## ed6-bilateral-bias-inconsistent
#
# Claim: bilateral photoinhibition biases movements inconsistently across mice and sessions, and
# the direction of a session's bias follows which control trajectory its perturbed cd
# trajectories approach. Sessions of fig3-cd-roc, bilateral photoinhibition (type 6). Per session,
# bias = performance on lick right minus lick left trials under photoinhibition; biased when
# Fisher's exact test of the two performances gives p < 0.05; side of the mean perturbed
# projection in the last 400 ms of the delay (a) relative to the decision boundary, (b) nearer of
# the mean control lick right and lick left projections. Reproduced when biased sessions of both
# signs occur and the sign agrees with the side in at least 80% of biased sessions (criterion).

# %% tags=claim:ed6-bilateral-bias-inconsistent
for cells in ("pyramidal", "all"):
    rows = []
    for P in POP[("exp2", cells, "code")]:
        proj, _, _ = cd_projections(P)
        gR, gL = P["groups"][(6, 1)], P["groups"][(6, -1)]
        hR, hL = P["hit"][gR], P["hit"][gL]
        bias = hR.mean() - hL.mean()
        p = stats.fisher_exact([[hR.sum(), (~hR).sum()], [hL.sum(), (~hL).sum()]]).pvalue
        mp = proj[np.r_[gR, gL], I_LATE].mean()
        cR, cL = proj[P["test"][1], I_LATE].mean(), proj[P["test"][-1], I_LATE].mean()
        rows.append({"session": P["session"], "mouse": P["mouse"], "perf_R": hR.mean(), "perf_L": hL.mean(), "bias": bias, "fisher_p": p,
                     "mean_proj": mp, "side_a": np.sign(mp), "side_b": 1 if abs(mp - cR) < abs(mp - cL) else -1})
    b6 = pd.DataFrame(rows)
    biased = b6[b6.fisher_p < 0.05]
    print(f"Neurons: {cells}")
    print(b6.round(3).to_string(index=False))
    for s_ in ("side_a", "side_b"):
        agree = (np.sign(biased.bias) == biased[s_]).mean() if len(biased) else np.nan
        print(f"  biased sessions {len(biased)} (lick right bias {int((biased.bias > 0).sum())}, lick left bias {int((biased.bias < 0).sum())}); sign agrees with {s_}: {agree:.2f}")
    allc = (np.sign(b6.bias) == b6.side_a).mean()
    print(f"  all sessions: sign of bias agrees with side (a) in {allc:.2f}; Spearman of bias with mean projection r = {stats.spearmanr(b6.bias, b6.mean_proj).statistic:.2f}, p = {stats.spearmanr(b6.bias, b6.mean_proj).pvalue:.3g}")

# %% [markdown]
# ## fig5-callosotomy-recovery: selectivity along cd
#
# The cd part of fig5-callosotomy-recovery: the ipsilateral cd ROC at the end of the delay in the
# callosotomy sessions (session rule of fig3-cd-roc), against (a) the callosotomy control ROC and
# (b) the Experiment 2 ipsilateral ROC; reduced read as lower by a paired (a) or unpaired (b)
# t-test over sessions at p < 0.05, a standard choice.

# %% tags=claim:fig5-callosotomy-recovery
rt5 = roc_table("ccx", [10, 11, 12])
print(rt5.round(3).to_string(index=False))
for cells in ("pyramidal", "all"):
    P5 = POP[("ccx", cells, "code")]
    R5c = pd.DataFrame([session_rocs(P, cd_projections(P)[0], [10, 11, 12]) for P in P5])
    R2c = pd.DataFrame([session_rocs(P, cd_projections(P)[0], [4, 5, 6]) for P in POP[("exp2", cells, "code")]])
    ta = stats.ttest_rel(R5c[10], R5c[0])
    tb = stats.ttest_ind(R5c[10], R2c[4])
    print(f"{cells}: callosotomy sessions {len(R5c)}; ipsilateral ROC {R5c[10].mean():.3f} against callosotomy control {R5c[0].mean():.3f} (paired t = {ta.statistic:.2f}, p = {ta.pvalue:.3g}); "
          f"against Experiment 2 ipsilateral {R2c[4].mean():.3f} (t = {tb.statistic:.2f}, p = {tb.pvalue:.3g})")
print("Paper: 16 callosotomy sessions in Fig. 5f.")
EOF
cd $TMPDIR/dev && . ../v/bin/activate && python run.py nb.py "SANITY" "SETUP7" "ed6-bilateral" "selectivity along cd" 2>&1 | grep -v "^---" | tail -62
```

```
50%       0.028
75%       0.069
max       2.181
Sessions with ratio above 0.5: [{'session': 'ANM257636_20150404', 'experiment': 'exp2b', 'neurons': 6, 'ratio': 2.04}, {'session': 'ANM264411_20141224', 'experiment': 'exp2', 'neurons': 21, 'ratio': 0.82}, {'session': 'ANM273657_20150325', 'experiment': 'exp2b', 'neurons': 13, 'ratio': 0.71}, {'session': 'ANM298738_20150727', 'experiment': 'ccx', 'neurons': 19, 'ratio': 2.18}]
Sessions with photostimulation but no pyramidal neuron to check: []
measures for 1579 units in 10 s
('exp2', 'pyramidal', 'code') sessions 16 mice 7 neurons 175
('exp2', 'pyramidal', 'half') sessions 16 mice 7 neurons 175
('exp2', 'all', 'code') sessions 17 mice 7 neurons 211
('exp2', 'all', 'half') sessions 17 mice 7 neurons 211
('exp3', 'pyramidal', 'code') sessions 4 mice 3 neurons 48
('exp3', 'pyramidal', 'half') sessions 4 mice 3 neurons 48
('exp3', 'all', 'code') sessions 5 mice 3 neurons 58
('exp3', 'all', 'half') sessions 5 mice 3 neurons 58
('ccx', 'pyramidal', 'code') sessions 16 mice 7 neurons 259
('ccx', 'pyramidal', 'half') sessions 16 mice 7 neurons 259
('ccx', 'all', 'code') sessions 17 mice 7 neurons 290
('ccx', 'all', 'half') sessions 17 mice 7 neurons 290
Neurons: pyramidal
           session     mouse  perf_R  perf_L   bias  fisher_p  mean_proj  side_a  side_b
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev && . ../v/bin/activate && python run.py nb.py "SANITY" "SETUP7" "rt5 = roc_table" 2>&1 | grep -v "^---" | tail -17
```

```
('exp2', 'pyramidal', 'half') sessions 16 mice 7 neurons 175
('exp2', 'all', 'code') sessions 17 mice 7 neurons 211
('exp2', 'all', 'half') sessions 17 mice 7 neurons 211
('exp3', 'pyramidal', 'code') sessions 4 mice 3 neurons 48
('exp3', 'pyramidal', 'half') sessions 4 mice 3 neurons 48
('exp3', 'all', 'code') sessions 5 mice 3 neurons 58
('exp3', 'all', 'half') sessions 5 mice 3 neurons 58
('ccx', 'pyramidal', 'code') sessions 16 mice 7 neurons 259
('ccx', 'pyramidal', 'half') sessions 16 mice 7 neurons 259
('ccx', 'all', 'code') sessions 17 mice 7 neurons 290
('ccx', 'all', 'half') sessions 17 mice 7 neurons 290
Traceback (most recent call last):
  File "/tmp/claude-1001/dev/run.py", line 15, in <module>
    exec(compile(c, f'cell{i}', 'exec'), g)
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "cell59", line 2, in <module>
NameError: name 'roc_table' is not defined
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev && . ../v/bin/activate && python run.py nb.py "SANITY" "SETUP7" "def roc_table" "rt5 = roc_table" 2>&1 | grep -v "^---" | tail -17
```

```
ANM264411  0.723  0.705  0.714  0.511
    cells split              cd  sessions  roc_0  sem_0  roc_10  sem_10  roc_11  sem_11  roc_12  sem_12
pyramidal  code meandiff/inside        16  0.718  0.046   0.566   0.036   0.660   0.044   0.549   0.035
pyramidal  code meandiff/centre        16  0.716  0.047   0.571   0.034   0.669   0.044   0.552   0.035
pyramidal  code      lda/inside        16  0.710  0.046   0.559   0.032   0.662   0.044   0.544   0.034
pyramidal  half meandiff/inside        16  0.707  0.040   0.567   0.036   0.649   0.044   0.538   0.036
pyramidal  half meandiff/centre        16  0.704  0.042   0.579   0.034   0.647   0.044   0.542   0.035
pyramidal  half      lda/inside        16  0.699  0.040   0.558   0.035   0.645   0.046   0.540   0.034
      all  code meandiff/inside        17  0.718  0.039   0.605   0.030   0.656   0.044   0.562   0.025
      all  code meandiff/centre        17  0.716  0.041   0.607   0.030   0.660   0.044   0.570   0.024
      all  code      lda/inside        17  0.712  0.036   0.597   0.028   0.657   0.044   0.565   0.024
      all  half meandiff/inside        17  0.715  0.034   0.605   0.032   0.643   0.048   0.563   0.026
      all  half meandiff/centre        17  0.715  0.034   0.605   0.031   0.641   0.050   0.567   0.026
      all  half      lda/inside        17  0.712  0.033   0.606   0.031   0.648   0.048   0.566   0.026
pyramidal: callosotomy sessions 16; ipsilateral ROC 0.566 against callosotomy control 0.718 (paired t = -3.19, p = 0.00609); against Experiment 2 ipsilateral 0.706 (t = -3.27, p = 0.00272)
all: callosotomy sessions 17; ipsilateral ROC 0.605 against callosotomy control 0.718 (paired t = -2.67, p = 0.0168); against Experiment 2 ipsilateral 0.672 (t = -1.67, p = 0.105)
Paper: 16 callosotomy sessions in Fig. 5f.
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  python3 -c "
t=open('paper/10.1038-nature17643.txt').read()
i=t.find('Modeling and simulation'); 
j=t.find('Modeling and simulation', i+100)
print(i,j)
k = j if j>0 else i
print(t[k:k+9000])
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
t=open('paper/10.1038-nature17643.txt').read()
i=t.find('Silencing was simulated by holding the activity of a randomly-selected population of 50 neurons')
print(t[i:i+5000])
"; python3 -c "
t=open('paper/10.1038-nature17643.txt').read()
i=t.find('Figure 6 ')
print(t[i:i+2500])
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "def handover" -A60 tools/entry.py | head -90; grep -n "Result:\|summary\|Summary" tools/entry.py | head -30
```

```
400:def handover(entry_dir: Path, output_dir: Path) -> int:
401-    entry = yaml.safe_load((entry_dir / "entry.yaml").read_text())
402-    target = output_dir / "handover"
403-    target.mkdir(parents=True, exist_ok=True)
404-    for notebook in entry["notebooks"]:
405-        executed = output_dir / notebook["path"]
406-        if not executed.is_file():
407-            print(f"error: no executed copy of {notebook['path']} in {output_dir}; run the entry first",
408-                  file=sys.stderr)
409-            return 1
410-        nb = strip_conclusions(nbformat.read(executed, as_version=4))
411-        nbformat.write(nb, target / notebook["path"])
412-    for helper in entry.get("helpers", []):
413-        shutil.copy(entry_dir / helper, target / helper)
414-    papers = {r["id"] for r in entry.get("related", []) if r["relation"] == "reproduces"}
415-    dandisets = {r["id"].split(":", 1)[1].split("/")[0]
416-                 for r in entry.get("related", []) if not r["id"].startswith(("doi:", "entry:"))}
417-    for path in sorted((ROOT / "claims").glob("*/*.yaml")):
418-        claims = yaml.safe_load(path.read_text()) or {}
419-        if dataset_id(claims) in dandisets and claims.get("paper") in papers:
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,60p tools/entry.py; grep -n "errors.append\|report.error\|def check" tools/entry.py | head -60
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
[... 84 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 176,210p tools/entry.py; sed -n 310,335p tools/entry.py
```

```
# Datasets are related as <archive>:<id>/<version> (docs/archives.md); papers as doi:, entries as entry:.
    used = [r["id"].split(":", 1)[1].partition("/")
            for r in entry.get("related", []) if not r["id"].startswith(("doi:", "entry:"))]
    archives = {r["id"].split(":", 1)[1].partition("/")[0]: r["id"].split(":", 1)[0]
                for r in entry.get("related", []) if not r["id"].startswith(("doi:", "entry:"))}
    dandisets = [d for d, _, _ in used]
    versions = {d: v for d, _, v in used}
    if entry.get("type") in ("orientation", "reproduction"):
        if not dandisets:
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
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-alm-3-li-2016 && python3 - <<'EOF'
p='alm3.py'; s=open(p).read()
s=s.replace('DATASET_DOI = "10.6080/K0RB72JW"','DATASET_ID = "alm-3"\nDATASET_VERSION = "unversioned"  # CRCNS data sets have no versions (docs/archives.md)\nDATASET_DOI = "10.6080/K0RB72JW"')
open(p,'w').write(s)
EOF
cat >> $TMPDIR/dev/nb.py <<'EOF'
# %% SANITY tags=sanity
# The lick trace (channel "lick_trace", a photodiode signal). The first lick after the cue is the
# first upward crossing of a threshold halfway between the trace's median and its 99.9th
# percentile (helper). On correct trials a lick follows the cue within the 1.4 s the trace covers.
lk = []
for s in sessions:
    g = s["good"] & np.isfinite(s["cue"]) & (s["trial_types"]["HitR"] | s["trial_types"]["HitL"]) & ~s["trial_types"]["LickEarly"]
    if g.sum() == 0:
        continue
    rt = (s["first_lick"] - s["cue"])[g]
    lk.append({"session": s["name"], "experiment": EXP[s["name"]], "trace_range": s["lick_p999"] - s["lick_median"],
               "median_first_lick_s": np.nanmedian(rt) if np.isfinite(rt).any() else np.nan, "frac_first_lick_under_20ms": np.nanmean(rt < 0.02),
               "trace_seconds_after_cue": np.nanmedian((s["trace_end"] - s["cue"])[g])})
lk = pd.DataFrame(lk)
usable = (lk.median_first_lick_s > 0.05) & (lk.frac_first_lick_under_20ms < 0.2)
print("Sessions with correct trials:", len(lk), "; sessions whose first threshold crossing after the cue looks like a lick (median > 50 ms, < 20% within 20 ms):", int(usable.sum()))
print(lk.groupby(usable.map({True: "lick-like", False: "noise-like"})).agg(sessions=("session", "size"), trace_range=("trace_range", "median"),
      median_first_lick_s=("median_first_lick_s", "median")).round(4).to_string())
print("Trace length after the cue (s), median over sessions:", round(lk.trace_seconds_after_cue.median(), 3))
EOF
cd $TMPDIR/dev && . ../v/bin/activate && python run.py nb.py "lick trace (channel" 2>&1 | grep -v "^---" | tail -8; date -u
```

```
measures for 1579 units in 10 s
Traceback (most recent call last):
  File "/tmp/claude-1001/dev/run.py", line 15, in <module>
    exec(compile(c, f'cell{i}', 'exec'), g)
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "cell41", line 63, in <module>
  File "cell41", line 49, in build_population
NameError: name 'ses' is not defined. Did you mean: 'set'?
Sat Nov  7 19:55:58 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev && . ../v/bin/activate && python run.py nb.py "SANITY" 2>&1 | grep -v "^---" | tail -7
```

```
('ccx', 'all', 'code') sessions 17 mice 7 neurons 290
('ccx', 'all', 'half') sessions 17 mice 7 neurons 290
Sessions with correct trials: 90 ; sessions whose first threshold crossing after the cue looks like a lick (median > 50 ms, < 20% within 20 ms): 42
            sessions  trace_range  median_first_lick_s
lick-like         42       0.0513               0.1938
noise-like        48       0.0018               0.0017
Trace length after the cue (s), median over sessions: 1.427
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/dev/nb.py <<'EOF'
# %% [markdown]
# ## ed9f-reaction-time
#
# Claim: reaction times are faster on trials whose cd trajectory lies far from the decision
# boundary at the go cue. Sessions of fig3-cd-roc whose lick trace shows licks (data check
# above); reaction time the first lick after the cue (criterion's reading), relative to the
# session mean, lick right and lick left trials pooled, correct and error trials; Spearman
# correlation with the absolute projection in the last 400 ms of the delay, negative with p < 0.05
# (criterion). Trials (a) control test trials, (b) all conditions.

# %% tags=claim:ed9f-reaction-time
ok_sessions = set(lk[usable].session)
for cells in ("pyramidal", "all"):
    rows = []
    for P in POP[("exp2", cells, "code")]:
        if P["session"] not in ok_sessions:
            continue
        s = SD[P["session"]]
        proj, _, _ = cd_projections(P)
        rt = (s["first_lick"] - s["cue"])[P["trials"]]
        for c in (0, 4, 5, 6):
            idx = np.r_[P["test"][1], P["test"][-1]] if c == 0 else np.r_[P["groups"][(c, 1)], P["groups"][(c, -1)]]
            for i in idx:
                if np.isfinite(rt[i]):
                    rows.append({"session": P["session"], "mouse": P["mouse"], "condition": c, "rt": rt[i], "dist": abs(proj[i, I_LATE])})
    d9 = pd.DataFrame(rows)
    d9["rt_rel"] = d9.rt - d9.groupby("session").rt.transform("mean")
    print(f"Neurons: {cells}; sessions with lick-like traces among the population sessions: {d9.session.nunique()} ({d9.mouse.nunique()} mice); trials {len(d9)}")
    print("  reaction time (s) median", round(d9.rt.median(), 3), "range", round(d9.rt.min(), 3), "to", round(d9.rt.max(), 3))
    for lab, m in (("(a) control", d9.condition == 0), ("(b) all conditions", d9.condition >= 0)):
        r = stats.spearmanr(d9[m].dist, d9[m].rt_rel)
        print(f"  {lab}: n = {int(m.sum())}, Spearman r = {r.statistic:.3f}, p = {r.pvalue:.3g}")
    print("  per session (b):", {k: round(stats.spearmanr(g.dist, g.rt_rel).statistic, 2) for k, g in d9.groupby("session")})
EOF
cd $TMPDIR/dev && . ../v/bin/activate && python run.py nb.py "SANITY" "def roc_table" "ok_sessions = set" 2>&1 | grep -v "^---" | tail -12
```

```
lick-like         42       0.0513               0.1938
noise-like        48       0.0018               0.0017
Trace length after the cue (s), median over sessions: 1.427
Traceback (most recent call last):
  File "/tmp/claude-1001/dev/run.py", line 15, in <module>
    exec(compile(c, f'cell{i}', 'exec'), g)
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "cell62", line 17, in <module>
  File "/tmp/claude-1001/v/lib/python3.13/site-packages/pandas/core/generic.py", line 6434, in __getattr__
    return object.__getattribute__(self, name)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
AttributeError: 'DataFrame' object has no attribute 'rt'. Did you mean: 'at'?
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev && cat >> nb.py <<'EOF'
EOF
cd $TMPDIR/dev && . ../v/bin/activate && python - <<'EOF' 2>&1 | tail -5
import re
src=open('nb.py').read()
src=src.replace("# %% [markdown]\n# ## ed9f-reaction-time","print(pd.crosstab(lk.experiment, usable))\n# %% [markdown]\n# ## ed9f-reaction-time",1)
open('nb_tmp.py','w').write(src)
EOF
python run.py nb_tmp.py "SANITY" "print(pd.crosstab(lk" 2>&1 | grep -v "^---" | tail -8
```

```
Trace length after the cue (s), median over sessions: 1.427
col_0       False  True 
experiment              
ccx             3     29
exp2           26      0
exp2b           0      6
exp3            0      6
unilateral     19      1
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev && python3 - <<'EOF'
s=open('nb.py').read()
a=s.index("# %% tags=claim:ed9f-reaction-time")
s=s[:a]+'''# %% tags=claim:ed9f-reaction-time
print("Sessions whose lick trace shows licks, by experiment:")
print(pd.crosstab(lk.experiment, usable.map({True: "lick-like", False: "noise-like"})).to_string())
ok_sessions = set(lk[usable].session)
for exp, conds in (("exp2", (4, 5, 6)), ("ccx", (10, 11, 12))):
    rows = []
    for P in POP[(exp, "pyramidal", "code")]:
        if P["session"] not in ok_sessions:
            continue
        s = SD[P["session"]]
        proj, _, _ = cd_projections(P)
        rt = (s["first_lick"] - s["cue"])[P["trials"]]
        for c in (0,) + conds:
            idx = np.r_[P["test"][1], P["test"][-1]] if c == 0 else np.r_[P["groups"][(c, 1)], P["groups"][(c, -1)]]
            for i in idx:
                if np.isfinite(rt[i]):
                    rows.append({"session": P["session"], "mouse": P["mouse"], "condition": c, "rt": rt[i], "dist": abs(proj[i, I_LATE])})
    print(f"\\n{exp}: population sessions with lick-like traces: {len({r['session'] for r in rows})}")
    if not rows:
        continue
    d9 = pd.DataFrame(rows)
    d9["rt_rel"] = d9.rt - d9.groupby("session").rt.transform("mean")
    print(f"  {d9.mouse.nunique()} mice, {len(d9)} trials; reaction time (s) median {d9.rt.median():.3f}, range {d9.rt.min():.3f} to {d9.rt.max():.3f}")
    for lab, m in (("(a) control", d9.condition == 0), ("(b) all conditions", d9.condition >= 0)):
        r = stats.spearmanr(d9[m].dist, d9[m].rt_rel)
        print(f"  {lab}: n = {int(m.sum())}, Spearman r = {r.statistic:.3f}, p = {r.pvalue:.3g}")
'''
open('nb.py','w').write(s)
EOF
. ../v/bin/activate && python run.py nb.py "SANITY" "def roc_table" "ok_sessions = set" 2>&1 | grep -v "^---" | tail -14
```

```
col_0       lick-like  noise-like
experiment                       
ccx                29           3
exp2                0          26
exp2b               6           0
exp3                6           0
unilateral          1          19

exp2: population sessions with lick-like traces: 0

ccx: population sessions with lick-like traces: 15
  7 mice, 1223 trials; reaction time (s) median 0.181, range 0.000 to 1.311
  (a) control: n = 319, Spearman r = -0.025, p = 0.655
  (b) all conditions: n = 1223, Spearman r = -0.025, p = 0.376
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat > $TMPDIR/dev/header.md <<'EOF'
# Reproducing Li, Daie, Svoboda & Druckmann (2016) from CRCNS alm-3

**Paper.** Li N, Daie K, Svoboda K, Druckmann S (2016). Robust neuronal dynamics in premotor cortex
during motor planning. *Nature* 532, 459-464.
[doi:10.1038/nature17643](https://doi.org/10.1038/nature17643). The claims file was written from the
accepted author manuscript in PubMed Central (PMC5081260): main text, Methods and the legends of
Figures 1 to 6 and Extended Data Figures 1 to 10.

**Data set.** CRCNS alm-3, [doi:10.6080/K0RB72JW](https://doi.org/10.6080/K0RB72JW), "Data and
simulations related to: Robust neuronal dynamics in premotor cortex during motor planning",
data description version 0.71 (April 19, 2018). Files are streamed from the public S3 bucket
`crcnsarchive`, under `alm-3/live/`. Version: `unversioned`. CRCNS data sets have no versions, and
the paper cites none, so the pinned version is the live copy, the only copy of the data files
(`alm-3/orig/` holds only documentation); the MD5 sums of the 91 session files read, from the
data set's `checksums.md5`, are printed in the data check, so that a later change can be
detected. The raw voltage traces (`data/RawVoltageTraces/`, 6 to 12 GB per session) are not used.

**Methods from the authors' code.** The data set holds the authors' MATLAB analysis scripts
(`alm-3/live/analyses_scripts/`), which its description says reproduce the paper's figures. The
claims file did not read them. Where the claims file leaves a detail open, this notebook takes it
from the Methods, and where the Methods leave it open, from these scripts, citing the file and
section; where the scripts disagree with the Methods (cd as a linear discriminant in place of
the mean difference), the Methods give the main result and the scripts a variant. The helper
module `alm3.py` says where each parameter comes from.

**Claims.**

| Claim | Tested here |
|---|---|
| units-and-sessions | tested |
| ed1-selective-fraction | tested |
| fig1d-late-delay-ipsilateral-bias | blocked: no condition ending at the go cue in the recording sessions; the behaviour-only sessions are not in the data set |
| fig1d-earlier-photoinhibition-minimal | tested, on the recording sessions of Experiment 1 |
| ed3-recovery-interval | blocked: behaviour-only sessions not in the data set |
| ed2b-silencing | tested |
| ed2d-spatial-extent | blocked: recordings in untrained mice not in the data set |
| ed2e-no-rebound | tested |
| fig1f-rate-recovery | tested |
| fig1g-selectivity-recovery | tested |
| ed4-return-to-trajectory | tested |
| ed5-photoactivation | blocked: photoactivation data not in the data set |
| fig2b-bilateral-behaviour | tested, on the recording sessions |
| ed6-bilateral-bias-inconsistent | tested |
| fig2-bilateral-recovery | tested |
| ed7-unilateral-4-spots-bilateral-1-spot | tested |
| ed7e-size-and-roc | tested |
| fig3-cd-roc | tested |
| ed8-roc-during-photoinhibition | tested |
| ed9b-cd-stability | tested |
| ed8a-mode-variance | tested |
| fig3-cd-predicts-movement | tested |
| fig3-other-modes | tested |
| ed9f-reaction-time | blocked: the lick trace shows no licks in any Experiment 2 session (data check) |
| fig5b-callosotomy-behaviour | tested, after the cut only (no sessions before the cut) |
| fig5-callosotomy-recovery | tested |
| ed10e-callosotomy-preparatory-activity | tested |
| models-monolithic-fail | see its section |
| fig6-modular-models-robust | see its section |
EOF
cat > $TMPDIR/dev/convert.py <<'EOF'
import re, sys, nbformat
src = open(sys.argv[1]).read()
header = open(sys.argv[2]).read()
tail = open(sys.argv[3]).read() if len(sys.argv) > 4 else ""
out = sys.argv[-1]
cells = [nbformat.v4.new_markdown_cell(header.strip())]
for chunk in re.split(r'(?m)^(?=# %%)', src):
    if not chunk.strip():
        continue
    first, _, body = chunk.partition("\n")
    body = body.strip("\n")
    if "[markdown]" in first:
        text = "\n".join(l[2:] if l.startswith("# ") else l.lstrip("#") for l in body.splitlines())
        cells.append(nbformat.v4.new_markdown_cell(text.strip()))
        continue
    if "LOAD-CELL" in first:
        pass
    m = re.search(r"tags=(\S+)", first)
    c = nbformat.v4.new_code_cell(body)
    if m:
        c.metadata["tags"] = m.group(1).split(",")
    cells.append(c)
if tail:
    for part in tail.split("\n<<<CELL>>>\n"):
        cells.append(nbformat.v4.new_markdown_cell(part.strip()))
nb = nbformat.v4.new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nbformat.write(nb, out)
print("cells", len(cells))
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev && python3 - <<'EOF'
s=open('nb.py').read()
a=s.index('# %% SANITY tags=sanity\n# The lick trace (channel')
b=s.index('# %% [markdown]\n# ## ed9f-reaction-time')
lick=s[a:b]
s=s[:a]+s[b:]
s=s.replace('# %% SETUP3\n', lick+'# %% SETUP3\n',1)
open('nb.py','w').write(s)
EOF
cd entries/crcns-alm-3-li-2016 && cat > requirements.in <<'EOF'
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
name: crcns-alm-3-li-2016
type: reproduction
title: Robust preparatory activity in mouse premotor cortex (Li, Daie, Svoboda and Druckmann 2016)
description: Tests the findings of Li, Daie, Svoboda and Druckmann (2016) on CRCNS data set alm-3,
  which holds the sorted single units, trial tables, photostimulus types and lick and laser traces
  of 91 recording sessions from 19 mice performing a delayed response task with transient
  unilateral or bilateral photoinhibition of the anterior lateral motor cortex, with and without
  callosotomy. It covers unit counts and selectivity, silencing and recovery of rates and
  selectivity, behaviour in the recording sessions, and the population analyses along the coding
  direction.
license: Apache-2.0
notebooks:
- path: reproduce_li_2016.ipynb
  title: Reproducing Li et al. (2016) from CRCNS alm-3
  runtime_minutes: 8
helpers:
- alm3.py
related:
- id: crcns:alm-3/unversioned
  relation: uses_data
- id: doi:10.1038/nature17643
  relation: reproduces
EOF
cd $TMPDIR/dev && . ../v/bin/activate && python convert.py nb.py header.md entries/crcns-alm-3-li-2016/reproduce_li_2016.ipynb && cd  && python3 -c "import nbformat,yaml,jsonschema" 2>&1; python tools/entry.py lock entries/crcns-alm-3-li-2016 2>&1 | tail -3; python tools/entry.py check entries/crcns-alm-3-li-2016 2>&1 | tail -8
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/dev/convert.py", line 1, in <module>
    import re, sys, nbformat
ModuleNotFoundError: No module named 'nbformat'
python: can't open file '/tmp/claude-1001/dev/tools/entry.py': [Errno 2] No such file or directory
python: can't open file '/tmp/claude-1001/dev/tools/entry.py': [Errno 2] No such file or directory
Shell cwd was reset to
```

**Agent calls Bash**

```bash
python3 -c "import nbformat,yaml,jsonschema; print('sys ok')" ; which python3 python
```

```
sys ok
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python3
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
```

**Agent calls Bash**

```bash
python3 $TMPDIR/dev/convert.py $TMPDIR/dev/nb.py $TMPDIR/dev/header.md entries/crcns-alm-3-li-2016/reproduce_li_2016.ipynb && python3 tools/entry.py lock entries/crcns-alm-3-li-2016 2>&1 | tail -3; python3 tools/entry.py check entries/crcns-alm-3-li-2016 2>&1 | tail -8
```

```
cells 63
wrote entries/crcns-alm-3-li-2016/requirements.lock.txt
0 error(s)
```

**Agent calls Bash**

```bash
date -u && time python3 tools/entry.py run entries/crcns-alm-3-li-2016 2>&1 | tail -15; date -u
```

```
Sat Nov  7 19:58:15 UTC 2026
[31mNameError[39m                                 Traceback (most recent call last)
[36mCell[39m[36m [39m[32mIn[15][39m[32m, line 5[39m
[32m      1[39m rows = []
[32m      2[39m [38;5;28;01mfor[39;00m sel_trials [38;5;28;01min[39;00m ([33m"all"[39m, [33m"correct"[39m):
[32m      3[39m     [38;5;28;01mfor[39;00m min_stim [38;5;28;01min[39;00m ([32m2[39m, [32m3[39m):
[32m      4[39m         [38;5;28;01mfor[39;00m width, shift, lab [38;5;28;01min[39;00m (([32m0.2[39m, [32m0.0[39m, [33m"200 ms, centre"[39m), ([32m0.4[39m, [32m0.2[39m, [33m"400 ms, end"[39m)):
[32m----> [39m[32m5[39m             tab, ks = recovery_table([33m"unilateral"[39m, [[32m1[39m, [32m2[39m, [32m3[39m], [32m1.0[39m, sel_trials, min_stim, width, shift, seed=[32m11[39m)
[32m      6[39m             [38;5;28;01mfor[39;00m r [38;5;28;01min[39;00m tab.to_dict([33m"records"[39m):
[32m      7[39m                 rows.append({[33m"selective_on"[39m: sel_trials, [33m"min_trials"[39m: f">{min_stim}", [33m"window"[39m: lab, **r})
[32m      8[39m f1g = pd.DataFrame(rows)

[31mNameError[39m: name 'recovery_table' is not defined


FAIL  reproduce_li_2016.ipynb  (149 s)

real	2m33.763s
user	2m38.915s
sys	0m47.348s
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev && python3 - <<'EOF'
import re
s=open('nb.py').read()
chunks=re.split(r'(?m)^(?=# %%)', s)
i5=[i for i,c in enumerate(chunks) if c.startswith('# %% SETUP5')][0]
c5=chunks.pop(i5)
i4=[i for i,c in enumerate(chunks) if c.startswith('# %% SETUP4')][0]
chunks.insert(i4+1,c5)
open('nb.py','w').write(''.join(chunks))
print([c.splitlines()[0] for c in chunks if 'SETUP' in c.splitlines()[0] or 'LOAD' in c.splitlines()[0]])
EOF
python3 $TMPDIR/dev/convert.py $TMPDIR/dev/nb.py $TMPDIR/dev/header.md entries/crcns-alm-3-li-2016/reproduce_li_2016.ipynb && date -u && python3 tools/entry.py run entries/crcns-alm-3-li-2016 2>&1 | tail -15; date -u
```

```
Traceback (most recent call last):
  File "<stdin>", line 9, in <module>
IndexError: list index out of range
Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/nbformat/__init__.py", line 204, in write
    fp.write(s)
    ^^^^^^^^
AttributeError: 'str' object has no attribute 'write'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/tmp/claude-1001/dev/convert.py", line 28, in <module>
    nbformat.write(nb, out)
    ~~~~~~~~~~~~~~^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/nbformat/__init__.py", line 208, in write
    with Path(fp).open("w", encoding="utf8") as f:
         ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/pathlib/_local.py", line 537, in open
    return io.open(self, mode, buffering, encoding, errors, newline)
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev && grep -n "^# %%" nb.py | head -30
```

```
1:# %% SETUP
19:# %% LOAD-CELL
28:# %% SETUP2
35:# %% SANITY tags=sanity
43:# %% SANITY tags=sanity
60:# %% SANITY tags=sanity
72:# %% SANITY tags=sanity
86:# %% SANITY tags=sanity
161:# %% SANITY tags=sanity
180:# %% SETUP3
192:# %% [markdown]
203:# %% tags=claim:units-and-sessions
235:# %% [markdown]
245:# %% tags=claim:ed1-selective-fraction
266:# %% SETUP4
323:# %% SETUP5
377:# %% [markdown]
390:# %% tags=claim:fig1f-rate-recovery
418:# %% [markdown]
434:# %% tags=claim:fig1g-selectivity-recovery
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
python3 $TMPDIR/dev/convert.py $TMPDIR/dev/nb.py $TMPDIR/dev/header.md entries/crcns-alm-3-li-2016/reproduce_li_2016.ipynb && date -u && python3 tools/entry.py run entries/crcns-alm-3-li-2016 2>&1 | tail -15; date -u
```

```
cells 63
Sat Nov  7 20:01:06 UTC 2026
Installed kernelspec registry-crcns-alm-3-li-2016 in executed/crcns-alm-3-li-2016/.venv/share/jupyter/kernels/registry-crcns-alm-3-li-2016
pass  reproduce_li_2016.ipynb  (231 s)
Sat Nov  7 20:05:03 UTC 2026
```

**Agent calls Bash**

```bash
cat > entries/crcns-alm-3-li-2016/models.py <<'EOF'
"""Network models of Li, Daie, Svoboda & Druckmann (2016), Methods, "Modeling and simulation",
and Extended Data Fig. 1f-i. No recorded data are used.

Every network follows tau dr/dt = -r + W f(r) + I(t) + T + xi(t), simulated for 2 s by Euler
steps; photoinhibition holds the silenced neurons at zero for 0.2 s < t < 1.0 s (Methods).
Parameters are the Methods' unless said otherwise:

- Modular attractor (Fig. 6b): two modules of two neurons; self weight 0.5235, within-module
  -0.5235, each neuron coupled to its same-preference partner in the other module with 0.3;
  tau = 100 ms; f(x) = g(x) - g(0), g(x) = 1.4 / (1 + exp(-(x - 0.5) / 0.3)); transient input
  0.1 to the neurons preferring the trial type for 0.05 s < t < 0.1 s; tonic input 0.5; noise of
  variance 0.01. Whether the variance is per step or per unit time is not stated; both are run
  (`noise="step"`: xi drawn each step with variance 0.01; `noise="time"`: white noise of
  intensity 0.01 per second). That the partner is the same-preference neuron is an assumption
  (the Methods say "one partner").
- Modular integrator (Fig. 6c): the printed 8 x 8 matrix, linear synapses, rates kept
  non-negative, tau = 10 ms, input +-0.04 to the right and left preferring neurons of both
  modules for 0.1 s < t < 1.9 s (persistent input, Methods), tonic 40 to the four integrator
  neurons, no noise.
- Simple integrator (ED Fig. 1f): N = 100, tau = 100 ms, linear, connectivity with one non-zero
  eigenvalue 0.99; the matrix is taken as 0.99 u u^T with u a random unit vector (the Methods fix
  only the spectrum; three draws), input a persistent current along u with sign by trial type,
  output u^T r, 50 random neurons silenced.
- Monolithic attractor: one module of the modular attractor without inter-module connections
  (the claims file's reading; the paper gives no parameters for it); "half the neurons" is one
  of its two neurons, either one.
- Trained recurrent network (ED Fig. 1h): FORCE learning (Sussillo and Abbott 2009) with
  tau = 200 ms, tanh, N = 400, connection probability 0.1, weights with variance 1.5^2 / (p N),
  transient input for 0.05 s < t < 0.1 s with Gaussian weights of variance 1 and opposite signs
  for the two trial types, 30 training trials. Open details, standard choices: the target is a
  linear ramp of the output from 0 at 0.1 s to +-1 at 2 s, the output is fed back through random
  weights uniform in [-1, 1], the recursive least squares rule starts from P = I and updates
  every 2 ms, Euler step 1 ms. 200 random neurons silenced.

Integration step 1 ms (0.1 ms for the 10 ms integrator), a standard choice.
"""
import numpy as np

T_END = 2.0
SIL = (0.2, 1.0)


def _g(x):
    return 1.4 / (1 + np.exp(-(x - 0.5) / 0.3))


def attractor_f(x):
    return _g(x) - _g(0.0)


def attractor_weights(inter=0.3, self_w=0.5235):
    """Neurons [R1, L1, R2, L2]."""
    W = np.array([[self_w, -self_w, 0, 0], [-self_w, self_w, 0, 0], [0, 0, self_w, -self_w], [0, 0, -self_w, self_w]], float)
    W[0, 2] = W[2, 0] = inter
    W[1, 3] = W[3, 1] = inter
    return W


def run_attractor(trial, silence, rng, W=None, noise="step", dt=0.001, tau=0.1, var=0.01):
    """Simulate the attractor; trial +1 (right) or -1 (left); silence: indices held at zero."""
    W = attractor_weights() if W is None else W
    n = W.shape[0]
    pref = np.array([1, -1, 1, -1][:n])
    steps = int(round(T_END / dt))
    r = np.zeros(n)
    out = np.zeros((steps, n))
    for k in range(steps):
        t = k * dt
        I = 0.1 * (pref == trial) if 0.05 <= t < 0.1 else np.zeros(n)
        xi = rng.normal(0, np.sqrt(var), n)
        drive = -r + W @ attractor_f(r) + I + 0.5
        if noise == "step":
            r = r + dt / tau * (drive + xi)
        else:
            r = r + dt / tau * drive + np.sqrt(dt) / tau * xi
        if silence is not None and len(silence) and SIL[0] < t < SIL[1]:
            r[list(silence)] = 0.0
        out[k] = r
    return out


INTEGRATOR_W = np.array([
    [0, -1, 0, 0, 0, 0, 0.5, 0],
    [-1, 0, 0, 0, 0, 0, -0.5, 0],
    [1, -1, 0, 0, 0, 0, 0, -6],
    [1, -1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0.5, 0, 0, -1, 0, 0],
    [0, 0, -0.5, 0, -1, 0, 0, 0],
    [0, 0, 0, -6, 1, -1, 0, 0],
    [0, 0, 0, 0, 1, -1, 0, 0],
], float)


def run_integrator(trial, silence, dt=0.0001, tau=0.01, amp=0.04, tonic=40.0):
    """The modular integrator (Methods matrix); returns rates every 1 ms."""
    W = INTEGRATOR_W
    steps = int(round(T_END / dt))
    every = int(round(0.001 / dt))
    r = np.zeros(8)
    r[[0, 1, 4, 5]] = tonic / 2
    out = []
    T = np.zeros(8)
    T[[0, 1, 4, 5]] = tonic
    for k in range(steps):
        t = k * dt
        I = np.zeros(8)
        if 0.1 <= t < 1.9:
            I[[0, 4]] = amp * trial
            I[[1, 5]] = -amp * trial
        r = r + dt / tau * (-r + W @ r + I + T)
        r = np.maximum(r, 0.0)
        if silence is not None and len(silence) and SIL[0] < t < SIL[1]:
            r[list(silence)] = 0.0
        if k % every == 0:
            out.append(r.copy())
    return np.array(out)


def run_simple_integrator(trial, silence, u, dt=0.001, tau=0.1, amp=1.0):
    """Rank-one linear integrator 0.99 u u^T with persistent input along u; returns u^T r."""
    W = 0.99 * np.outer(u, u)
    steps = int(round(T_END / dt))
    r = np.zeros(len(u))
    out = np.zeros(steps)
    for k in range(steps):
        t = k * dt
        I = amp * trial * u if 0.1 <= t < 1.9 else 0.0
        r = r + dt / tau * (-r + W @ r + I)
        if silence is not None and len(silence) and SIL[0] < t < SIL[1]:
            r[silence] = 0.0
        out[k] = u @ r
    return out


class Force:
    """A FORCE-trained rate network (Sussillo and Abbott 2009) producing a ramp."""

    def __init__(self, rng, N=400, p=0.1, g=1.5, tau=0.2, dt=0.001):
        self.N, self.tau, self.dt = N, tau, dt
        mask = rng.random((N, N)) < p
        self.J = np.where(mask, rng.normal(0, g / np.sqrt(p * N), (N, N)), 0.0)
        self.w_in = rng.normal(0, 1.0, N)
        self.w_fb = rng.uniform(-1, 1, N)
        self.w_out = np.zeros(N)
        self.P = np.eye(N)
        self.x0 = rng.normal(0, 0.5, N)

    def target(self, t, trial):
        return trial * np.clip((t - 0.1) / 1.9, 0, 1)

    def run(self, trial, silence=None, train=False, every=2):
        steps = int(round(T_END / self.dt))
        x = self.x0.copy()
        r = np.tanh(x)
        z = self.w_out @ r
        zs = np.zeros(steps)
        for k in range(steps):
            t = k * self.dt
            u = trial if 0.05 <= t < 0.1 else 0.0
            x = x + self.dt / self.tau * (-x + self.J @ r + self.w_fb * z + self.w_in * u)
            r = np.tanh(x)
            if silence is not None and len(silence) and SIL[0] < t < SIL[1]:
                r[silence] = 0.0
            z = self.w_out @ r
            if train and k % every == 0:
                Pr = self.P @ r
                c = 1.0 / (1.0 + r @ Pr)
                self.P -= c * np.outer(Pr, Pr)
                e = z - self.target(t, trial)
                self.w_out -= c * e * Pr
                z = self.w_out @ r
            zs[k] = z
        return zs

    def train(self, n_trials=30, rng=None):
        for i in range(n_trials):
            self.run(1 if i % 2 == 0 else -1, train=True)
EOF
cd $TMPDIR && . v/bin/activate && cat > sim.py <<'EOF'
import sys, time, numpy as np
sys.path.insert(0,'entries/crcns-alm-3-li-2016'); import models as md
rng=np.random.default_rng(0)
t=time.time()
for noise in ("step","time"):
    o=md.run_attractor(1,None,rng,noise=noise); print(noise,'unpert end',o[-1].round(3), 'sel', (o[-1,0]-o[-1,1]).round(3))
    o=md.run_attractor(-1,None,rng,noise=noise); print(noise,'left end',o[-1].round(3))
    o=md.run_attractor(1,[0,1],rng,noise=noise); print(noise,'unilat end',o[-1].round(3), 'at 1.0', o[1000].round(3))
    o=md.run_attractor(1,[0,1,2,3],rng,noise=noise); print(noise,'bilat end',o[-1].round(3))
print(time.time()-t)
for tr in (1,-1):
    o=md.run_integrator(tr,None); p=md.run_integrator(tr,[0,1,2,3]); q=md.run_integrator(tr,[4,5,6,7])
    print('integ',tr,'unpert',o[-1].round(2),'\n   sil1',p[-1].round(2),'\n   sil2',q[-1].round(2))
u=rng.normal(size=100); u/=np.linalg.norm(u)
o=md.run_simple_integrator(1,None,u); p=md.run_simple_integrator(1,rng.choice(100,50,replace=False),u)
print('simple', o[-1], p[-1])
EOF
python sim.py
```

```
step unpert end [ 1.461 -0.156  1.487 -0.15 ] sel 1.617
step left end [-0.154  1.459 -0.153  1.466]
step unilat end [ 1.45  -0.137  1.464 -0.147] at 1.0 [0.008 0.007 0.775 0.207]
step bilat end [0.544 0.868 0.537 0.895]
time unpert end [ 1.518 -0.409  1.417 -0.455] sel 1.927
time left end [ 1.624 -0.371  1.743 -0.193]
time unilat end [ 0.423  0.612  1.216 -0.166] at 1.0 [ 0.003  0.002  1.409 -0.217]
time bilat end [1.517 0.33  1.547 0.525]
0.15557432174682617
integ 1 unpert [27.2 12.8  0.  14.4 27.2 12.8  0.  14.4] 
   sil1 [26.81 13.19  0.   13.62 27.2  12.8   0.   14.4 ] 
   sil2 [27.2  12.8   0.   14.4  26.81 13.19  0.   13.62]
integ -1 unpert [12.8 27.2  0.   0.  12.8 27.2  0.   0. ] 
   sil1 [16.4 23.6  0.   0.  12.8 27.2  0.   0. ] 
   sil2 [12.8 27.2  0.   0.  16.4 23.6  0.   0. ]
simple 16.309806134623965 9.175259124577405
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . v/bin/activate && cat > sim2.py <<'EOF'
import sys, time, numpy as np
sys.path.insert(0,'entries/crcns-alm-3-li-2016'); import models as md
for d in range(1):
    rng=np.random.default_rng(100+d)
    t=time.time(); net=md.Force(rng); net.train(30); print('train',time.time()-t)
    zR=net.run(1); zL=net.run(-1)
    sil=rng.choice(400,200,replace=False)
    pR=net.run(1,sil); pL=net.run(-1,sil)
    print('ramp R at 0.5,1,1.5,2', zR[[499,999,1499,1999]].round(3), 'L', zL[[499,999,1499,1999]].round(3))
    print('pert R', pR[[999,1499,1999]].round(3), 'L', pL[[999,1499,1999]].round(3))
EOF
python sim2.py
```

```
train 29.452054738998413
ramp R at 0.5,1,1.5,2 [0.21  0.473 0.736 0.998] L [-0.21  -0.473 -0.736 -0.998]
pert R [0.095 0.189 0.098] L [0.087 0.344 0.364]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/dev/nb.py <<'EOF'
# %% [markdown]
# ## models-monolithic-fail
#
# Claim: monolithic network models (fixed-point attractor, integrators, trained recurrent
# networks) do not recover their unperturbed trajectory after transient silencing of half of their
# neurons. A simulation that uses no recorded data; parameters from the Methods and the ED Fig. 1
# legend, open details as stated in `models.py`. Criterion: in each model, the output at t = 2 s
# after perturbation differs from the unperturbed output by more than 20% of the unperturbed
# selectivity in at least two of three draws. Run here: the simple integrator (three draws of its
# connectivity), the monolithic attractor (one module of Fig. 6b; either neuron silenced; noise
# realizations as draws) and the FORCE-trained network (three draws). Not run: the integrator with
# corrective feedback (ED Fig. 1g), whose weights the paper does not give, and the tamed-chaos
# network (ED Fig. 1i), whose pruning threshold and retuning the paper does not give.

# %% tags=claim:models-monolithic-fail
import models

rng_m = np.random.default_rng(2016)
rows = []
for d in range(3):
    u = rng_m.normal(size=100)
    u /= np.linalg.norm(u)
    sil = rng_m.choice(100, 50, replace=False)
    o = {tr: models.run_simple_integrator(tr, None, u)[-1] for tr in (1, -1)}
    p = {tr: models.run_simple_integrator(tr, sil, u)[-1] for tr in (1, -1)}
    sel = o[1] - o[-1]
    rows.append({"model": "simple integrator", "draw": d, "unperturbed_out": o[1], "perturbed_out": p[1],
                 "deviation_over_selectivity": max(abs(p[1] - o[1]), abs(p[-1] - o[-1])) / abs(sel)})
W1 = models.attractor_weights()[:2, :2]
for d in range(3):
    for silenced in ([0], [1]):
        seed = int(rng_m.integers(1e9))
        o = {tr: models.run_attractor(tr, None, np.random.default_rng(seed + tr), W=W1)[-1] for tr in (1, -1)}
        p = {tr: models.run_attractor(tr, silenced, np.random.default_rng(seed + tr), W=W1)[-1] for tr in (1, -1)}
        sel = (o[1][0] - o[1][1]) - (o[-1][0] - o[-1][1])
        dev = max(abs((p[tr][0] - p[tr][1]) - (o[tr][0] - o[tr][1])) for tr in (1, -1))
        rows.append({"model": f"monolithic attractor, neuron {silenced[0] + 1} silenced", "draw": d, "unperturbed_out": o[1][0] - o[1][1],
                     "perturbed_out": p[1][0] - p[1][1], "deviation_over_selectivity": dev / abs(sel)})
t_f = time.time()
for d in range(3):
    net = models.Force(np.random.default_rng(300 + d))
    net.train(30)
    sil = np.random.default_rng(400 + d).choice(400, 200, replace=False)
    o = {tr: net.run(tr) for tr in (1, -1)}
    p = {tr: net.run(tr, sil) for tr in (1, -1)}
    sel = o[1][-1] - o[-1][-1]
    rows.append({"model": "FORCE network", "draw": d, "unperturbed_out": o[1][-1], "perturbed_out": p[1][-1],
                 "deviation_over_selectivity": max(abs(p[tr][-1] - o[tr][-1]) for tr in (1, -1)) / abs(sel),
                 "train_error_rms": float(np.sqrt(np.mean((o[1] - net.target(np.arange(2000) * 0.001, 1)) ** 2)))})
print(f"FORCE networks trained and run in {time.time() - t_f:.0f} s")
mono = pd.DataFrame(rows)
mono["not_recovered"] = mono.deviation_over_selectivity > 0.2
print(mono.round(3).to_string(index=False))
print("\nDraws not recovered (deviation > 20% of selectivity), per model:")
print(mono.groupby("model").not_recovered.agg(["sum", "size"]).to_string())

# %% [markdown]
# ## fig6-modular-models-robust
#
# Claim: modular networks of two coupled modules restore activity after transient silencing of
# one module but drift to a random fixed point when both are silenced. Modular attractor and
# modular integrator with the Methods' parameters (`models.py`); the modular FORCE network is not
# run, as its training of the inter-module weights is not specified. Criterion: for the attractor
# and the integrator, the silenced module returns within 10% of its unperturbed state by t = 2 s in
# at least 90% of 100 noisy runs, and after bilateral silencing the attractor ends at the wrong
# fixed point in 25% to 75% of runs. The module's state is read as its selectivity (right minus
# left preferring neuron), compared with the same noise realization without silencing; the fixed
# point at t = 2 s by the sign of that selectivity. The integrator has no noise, so one run per
# trial type stands for all.

# %% tags=claim:fig6-modular-models-robust
rows = []
for noise in ("step", "time"):
    for tr in (1, -1):
        rec, wrong, wrong_ctrl, undecided = [], [], [], []
        for i in range(100):
            seed = 10_000 * (1 if noise == "step" else 2) + 100 * (tr + 1) + i
            o = models.run_attractor(tr, None, np.random.default_rng(seed), noise=noise)
            p = models.run_attractor(tr, [0, 1], np.random.default_rng(seed), noise=noise)
            b = models.run_attractor(tr, [0, 1, 2, 3], np.random.default_rng(seed), noise=noise)
            so, sp, sb = o[-1, 0] - o[-1, 1], p[-1, 0] - p[-1, 1], b[-1, 0] - b[-1, 1]
            rec.append(abs(sp - so) <= 0.1 * abs(so))
            wrong.append(np.sign(sb) != tr)
            wrong_ctrl.append(np.sign(so) != tr)
            undecided.append(abs(sb) < 0.5 * abs(so))
        rows.append({"model": "modular attractor", "noise": noise, "trial": tr, "runs": 100,
                     "unilateral_recovered": np.mean(rec), "bilateral_wrong_fixed_point": np.mean(wrong),
                     "bilateral_not_settled_at_2s": np.mean(undecided), "control_wrong": np.mean(wrong_ctrl)})
for tr in (1, -1):
    o = models.run_integrator(tr, None)
    p = models.run_integrator(tr, [0, 1, 2, 3])
    b = models.run_integrator(tr, list(range(8)))
    so, sp, sb = o[-1, 0] - o[-1, 1], p[-1, 0] - p[-1, 1], b[-1, 0] - b[-1, 1]
    rows.append({"model": "modular integrator", "noise": "none", "trial": tr, "runs": 1,
                 "unilateral_recovered": float(abs(sp - so) <= 0.1 * abs(so)), "bilateral_wrong_fixed_point": float(np.sign(sb) != tr),
                 "selectivity_unperturbed": so, "selectivity_after_unilateral": sp, "selectivity_after_bilateral": sb})
m6 = pd.DataFrame(rows)
print(m6.round(3).to_string(index=False))
EOF
python3 - <<'EOF'
p='entries/crcns-alm-3-li-2016/entry.yaml'
s=open(p).read(); s=s.replace("helpers:\n- alm3.py","helpers:\n- alm3.py\n- models.py"); open(p,'w').write(s)
EOF
cd $TMPDIR/dev && . ../v/bin/activate && python run.py nb.py "import models" "rows = []\nfor noise in" 2>&1 | grep -v "^---" | tail -40
```

```
measures for 1579 units in 10 s
Traceback (most recent call last):
  File "/tmp/claude-1001/dev/run.py", line 15, in <module>
    exec(compile(c, f'cell{i}', 'exec'), g)
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "cell42", line 63, in <module>
  File "cell42", line 49, in build_population
NameError: name 'ses' is not defined. Did you mean: 'set'?
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev && . ../v/bin/activate && python run.py nb.py "SANITY" "import models" "for noise in (\"step\"" 2>&1 | grep -v "^---" | tail -36
```

```
('exp3', 'all', 'code') sessions 5 mice 3 neurons 58
('exp3', 'all', 'half') sessions 5 mice 3 neurons 58
('ccx', 'pyramidal', 'code') sessions 16 mice 7 neurons 259
('ccx', 'pyramidal', 'half') sessions 16 mice 7 neurons 259
('ccx', 'all', 'code') sessions 17 mice 7 neurons 290
('ccx', 'all', 'half') sessions 17 mice 7 neurons 290
FORCE networks trained and run in 17 s
                                  model  draw  unperturbed_out  perturbed_out  deviation_over_selectivity  train_error_rms  not_recovered
                      simple integrator     0           16.310          9.387                       0.212              NaN           True
                      simple integrator     1           16.310          9.400                       0.212              NaN           True
                      simple integrator     2           16.310          9.321                       0.214              NaN           True
monolithic attractor, neuron 1 silenced     0            0.932         -1.020                       1.079              NaN           True
monolithic attractor, neuron 2 silenced     0            0.903          0.992                       1.071              NaN           True
monolithic attractor, neuron 1 silenced     1            0.973         -0.994                       1.030              NaN           True
monolithic attractor, neuron 2 silenced     1            0.835          0.992                       1.093              NaN           True
monolithic attractor, neuron 1 silenced     2            0.944         -0.977                       1.023              NaN           True
monolithic attractor, neuron 2 silenced     2            0.917          1.018                       1.047              NaN           True
                          FORCE network     0            0.998          0.915                       0.247              0.0           True
                          FORCE network     1            0.998          0.351                       0.475    
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev && python3 - <<'EOF'
s=open('header.md').read()
s=s.replace("| models-monolithic-fail | see its section |","| models-monolithic-fail | tested in part: three of the five models are simulated |")
s=s.replace("| fig6-modular-models-robust | see its section |","| fig6-modular-models-robust | tested in part: the attractor and the integrator are simulated |")
open('header.md','w').write(s)
EOF
python3 $TMPDIR/dev/convert.py $TMPDIR/dev/nb.py $TMPDIR/dev/header.md entries/crcns-alm-3-li-2016/reproduce_li_2016.ipynb && cd  && python3 tools/entry.py lock entries/crcns-alm-3-li-2016 | tail -1 && python3 tools/entry.py run entries/crcns-alm-3-li-2016 2>&1 | tail -3; date -u
```

```
cells 67
wrote entries/crcns-alm-3-li-2016/requirements.lock.txt
Installed kernelspec registry-crcns-alm-3-li-2016 in executed/crcns-alm-3-li-2016/.venv/share/jupyter/kernels/registry-crcns-alm-3-li-2016
pass  reproduce_li_2016.ipynb  (240 s)
Sat Nov  7 20:12:31 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'EOF' > $TMPDIR/out.txt
import nbformat
nb=nbformat.read('executed/crcns-alm-3-li-2016/reproduce_li_2016.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    tags=c.metadata.get('tags',[])
    txt=''.join(o.get('text','') for o in c.outputs if o.output_type=='stream')
    print(f'=== cell {i} {tags}'); print(txt)
EOF
wc -l $TMPDIR/out.txt; grep -n "=== cell" $TMPDIR/out.txt | head -50
```

```
1041 /tmp/claude-1001/out.txt
1:=== cell 1 []
3:=== cell 2 []
6:=== cell 3 []
8:=== cell 4 ['sanity']
104:=== cell 5 ['sanity']
151:=== cell 6 ['sanity']
174:=== cell 7 ['sanity']
195:=== cell 8 ['sanity']
236:=== cell 9 ['sanity']
243:=== cell 10 []
246:=== cell 12 ['claim:units-and-sessions']
278:=== cell 14 ['claim:ed1-selective-fraction']
310:=== cell 15 []
312:=== cell 16 []
314:=== cell 18 ['claim:fig1f-rate-recovery']
333:=== cell 20 ['claim:fig1g-selectivity-recovery']
373:=== cell 22 ['claim:fig2-bilateral-recovery']
411:=== cell 24 ['claim:ed7-unilateral-4-spots-bilateral-1-spot']
445:=== cell 26 ['claim:ed2b-silencing']
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,10p $TMPDIR/out.txt; sed -n 236,445p $TMPDIR/out.txt
```

```
=== cell 1 []

=== cell 2 []
loaded 91 sessions and 1579 units in 159 s

=== cell 3 []

=== cell 4 ['sanity']
Files read: 91 session files, 12.26 GB in the bucket listing.
Session files without an MD5 sum in checksums.md5: 0
=== cell 9 ['sanity']
Sessions with correct trials: 90 ; sessions whose first threshold crossing after the cue looks like a lick (median > 50 ms, < 20% within 20 ms): 42
            sessions  trace_range  median_first_lick_s
lick-like         42       0.0513               0.1938
noise-like        48       0.0018               0.0017
Trace length after the cue (s), median over sessions: 1.427

=== cell 10 []
measures for 1579 units in 10 s

[... 201 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 445,560p $TMPDIR/out.txt | head -30; sed -n 919,1041p $TMPDIR/out.txt | grep -v "^ANM\|^  *session" | head -60
```

```
=== cell 26 ['claim:ed2b-silencing']
Window (a): onset to start of ramp
                                                       size   mean  median  reduction
experiment condition label                                                           
ccx        10        CCX ipsi 1 spot (0.8 s)            317  0.120   0.036      0.880
           11        CCX contra 1 spot (0.8 s)          317  0.959   0.911      0.041
           12        CCX bilateral 4 spots (0.8 s)      322  0.236   0.048      0.764
exp2       4         ipsi 1 spot (0.8 s)                322  0.084   0.014      0.916
           5         contra 1 spot (0.8 s)              319  0.945   0.809      0.055
           6         bilateral 4 spots (0.8 s)          323  0.076   0.029      0.924
exp2b      4         ipsi 1 spot (0.8 s)                 61  0.115   0.000      0.885
           5         contra 1 spot (0.8 s)               61  0.986   0.893      0.014
           7         bilateral 1 spot (0.8 s)            61  0.114   0.000      0.886
exp3       7         bilateral 1 spot (0.8 s)            56  0.060   0.024      0.940
           8         ipsi 4 spots (0.8 s)                56  0.038   0.000      0.962
           9         contra 4 spots (0.8 s)              56  1.152   0.819     -0.152
unilateral 1         ipsi 1 spot sample (0.5 s)         180  0.062   0.019      0.938
           2         ipsi 1 spot early delay (0.5 s)    180  0.069   0.017      0.931
           3         ipsi 1 spot middle delay (0.5 s)   180  0.090   0.017      0.910
By mouse line, ipsilateral and bilateral conditions (types 1-4, 6-8):
[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . v/bin/activate && python - <<'EOF'
import fsspec, zipfile, io, scipy.io as sio
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/alm-3/live/data/meta_data_files.zip','rb').open()
z=zipfile.ZipFile(f); n=z.namelist(); print(len(n), n[:3])
for name in [x for x in n if x.endswith('.mat')][:1]+[x for x in n if '257636' in x][:1]:
    m=sio.loadmat(io.BytesIO(z.read(name)),squeeze_me=True,struct_as_record=False)['meta_data']
    def show(o,ind=''):
        for k in o._fieldnames:
            v=getattr(o,k)
            if hasattr(v,'_fieldnames'): print(ind+k+':'); show(v,ind+'  ')
            else: print(ind+k, repr(v)[:120])
    print('==',name); show(m)
EOF
```

```
92 ['meta_data_files/', 'meta_data_files/meta_data_ANM255200_20140910.mat', 'meta_data_files/meta_data_ANM255200_20140911.mat']
== meta_data_files/meta_data_ANM255200_20140910.mat
species 'Mus musculus'
animalStrain array(['008069', '026294'], dtype=object)
animalGeneModification array(['PV-ires-Cre', 'rosa-Cag-lsl-ReaChR-mCitrine'], dtype=object)
animalSource array(['JAX', 'JAX'], dtype=object)
animalGeneCopy array([1, 1], dtype=object)
animalGeneticBackground 'unidentified'
animalID 'anm00255200'
sex 'm'
dateOfBirth 'not recorded'
dateOfExperiment '20140910'
timeOfExperiment '095836'
experimenters 'Nuo Li'
citation '**PMID currently not avaliable'
whiskerConfig 'full'
weightBefore array([], dtype=object)
weightAfter array([], dtype=object)
experimentType array(['behavior', 'extracellular', 'photostim'], dtype=object)
referenceAtlas 'Allen Reference Atlas'
[... 76 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-alm-3-li-2016 && python3 - <<'EOF'
p='alm3.py'; s=open(p).read()
a=s.index("# Mouse lines, from the comments")
b=s.index("def side(s):")
s=s[:a]+'''def load_meta():
    """Per session, the fields of meta_data_<session>.mat (in data/meta_data_files.zip, read in
    place) that the analysis uses: the mouse's gene modification, sex, and the recording
    coordinates."""
    import zipfile
    url = f"{BUCKET}/{PREFIX}data/meta_data_files.zip"
    out = {}
    with fsspec.open(url, "rb", block_size=2**20) as f:
        z = zipfile.ZipFile(f)
        for name in z.namelist():
            m = re.search(r"meta_data_(ANM\\d+_\\d+)\\.mat$", name)
            if not m:
                continue
            md = sio.loadmat(io.BytesIO(z.read(name)), squeeze_me=True, struct_as_record=False)["meta_data"]
            gm = md.animalGeneModification
            gm = " x ".join(str(x) for x in np.atleast_1d(gm))
            out[m.group(1)] = {"gene_modification": gm, "sex": str(md.sex),
                               "recording_coordinates": np.atleast_1d(md.extracellular.recordingCoordinates).astype(float).tolist(),
                               "photostim_wavelength": " ".join(str(x) for x in np.atleast_1d(md.photostim.photostimWavelength))}
    return out


def mouse_line(gene_modification):
    """VGAT-ChR2 or PV x ReaChR, from the meta data's gene modification."""
    if "VGAT" in gene_modification:
        return "VGAT-ChR2"
    if "PV" in gene_modification and "ReaChR" in gene_modification:
        return "PV x ReaChR"
    return gene_modification


'''+s[b:]
s=s.replace('''- Cell type: the `cellType` label''','''- Mouse line: the gene modification in the session's meta data file (`load_meta`).
- Cell type: the `cellType` label''')
open(p,'w').write(s)
EOF
grep -n "MOUSE_LINE" $TMPDIR/dev/nb.py
```

```
46:    "line": alm3.MOUSE_LINE.get(s["mouse"], "?"), "trials": len(s["trial_ids"]), "good": int(s["good"].sum()),
533:                             "line": alm3.MOUSE_LINE.get(u["mouse"], "?"), "norm_rate": rs / rc})
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev && python3 - <<'EOF'
s=open('nb.py').read()
s=s.replace('''units = [u for s in sessions for u in alm3.reduce_units(s)]
''','''units = [u for s in sessions for u in alm3.reduce_units(s)]
meta = alm3.load_meta()
''')
s=s.replace('''    "line": alm3.MOUSE_LINE.get(s["mouse"], "?"), "trials"''','''    "line": alm3.mouse_line(meta[s["name"]]["gene_modification"]), "trials"''')
s=s.replace('''"line": alm3.MOUSE_LINE.get(u["mouse"], "?"), "norm_rate"''','''"line": LINE[u["mouse"]], "norm_rate"''')
s=s.replace('''print("Time units (2 = second):",''','''LINE = ses.groupby("mouse").line.first().to_dict()
print("\\nMouse lines from the meta data files (gene modification), by experiment group:")
print(ses.assign(group=np.where(ses.experiment == "ccx", "callosotomy", "control")).groupby(["group", "line"]).mouse.nunique().to_string())
print("Mice whose sessions disagree on the line:", [m for m, g in ses.groupby("mouse") if g.line.nunique() > 1])
print("Data description: 5 VGAT-ChR2-EYFP and 7 PV x ReaChR mice for electrophysiology; callosotomy 6 VGAT-ChR2-EYFP and 1 PV x ReaChR.")
print("Time units (2 = second):",''')
open('nb.py','w').write(s)
s=open('run.py').read()
s=s.replace("files=alm3.list_files(); md5=alm3.checksums()","files=alm3.list_files(); md5=alm3.checksums(); meta=alm3.load_meta()")
open('run.py','w').write(s)
EOF
grep -n "LINE\[" $TMPDIR/dev/nb.py | head; cd $TMPDIR/dev && . ../v/bin/activate && python run.py nb.py "SANITY" "ed2b-silencing" 2>&1 | grep -A8 "Mouse lines from" ; python run.py nb.py "SANITY" "def silencing_rows" 2>&1 | grep -B2 -A12 "By mouse line" | head -40
```

```
539:                             "line": LINE[u["mouse"]], "norm_rate": rs / rc})
Mouse lines from the meta data files (gene modification), by experiment group:
group        line       
callosotomy  PV x ReaChR    1
             VGAT-ChR2      6
control      PV x ReaChR    7
             VGAT-ChR2      5
Mice whose sessions disagree on the line: []
Data description: 5 VGAT-ChR2-EYFP and 7 PV x ReaChR mice for electrophysiology; callosotomy 6 VGAT-ChR2-EYFP and 1 PV x ReaChR.
Time units (2 = second): [2] [2]
           2         ipsi 1 spot early delay (0.5 s)    180  0.069   0.017      0.931
           3         ipsi 1 spot middle delay (0.5 s)   180  0.090   0.017      0.910
By mouse line, ipsilateral and bilateral conditions (types 1-4, 6-8):
                        size   mean  reduction
line        experiment                        
PV x ReaChR exp2         433  0.052      0.948
            exp2b         70  0.014      0.986
            exp3          34  0.068      0.932
            unilateral   540  0.074      0.926
VGAT-ChR2   exp2         212  0.137      0.863
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev && python3 - <<'EOF'
s=open('nb.py').read()
s=s.replace('''    print("By mouse, Experiment 2 ipsilateral (type 4):")''','''    t3 = sil[(sil.condition == 4) & (sil.experiment == "exp2")].groupby("line").norm_rate.agg(["size", "mean"])
    t3["reduction"] = 1 - t3["mean"]
    print("By mouse line, Experiment 2 ipsilateral (type 4), as ED Fig. 2b right:")
    print(t3.round(3).to_string())
    print("By mouse, Experiment 2 ipsilateral (type 4):")''')
open('nb.py','w').write(s)
EOF
cd $TMPDIR/dev && . ../v/bin/activate && python run.py nb.py "SANITY" "def silencing_rows" 2>&1 | grep -A5 "as ED Fig. 2b right"
```

```
By mouse line, Experiment 2 ipsilateral (type 4), as ED Fig. 2b right:
             size   mean  reduction
line                               
PV x ReaChR   216  0.049      0.951
VGAT-ChR2     106  0.155      0.845
By mouse, Experiment 2 ipsilateral (type 4):
--
By mouse line, Experiment 2 ipsilateral (type 4), as ED Fig. 2b right:
             size   mean  reduction
line                               
PV x ReaChR   216  0.047      0.953
VGAT-ChR2     106  0.169      0.831
By mouse, Experiment 2 ipsilateral (type 4):
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat > $TMPDIR/dev/results.md <<'EOF'
### units-and-sessions
**Result: not reproduced.** The non-callosotomy sessions hold 1012 single units in 58 sessions (20 unilateral, 38 bilateral) from 12 mice, and 890 are labelled pyramidal, all as the paper reports. The FS count differs: 89 units are labelled FS and 33 carry no label, against 72 and 50 in the paper; by the width of the deposited mean waveforms there are 98 FS and 24 intermediate units, and 104 and 19 after upsampling. Five of the six counts match exactly; the criterion needs all of them, or the class counts within 10%, and the FS count is 24% above the paper's.

### ed1-selective-fraction
**Result: reproduced.** With correct control trials, lick-early trials excluded and the 1.3 s response epoch, 633 of 890 pyramidal neurons are selective in some epoch, 176 in the sample, 336 in the delay and 493 in the response epoch, against 634, 176, 337 and 493. The 1.5 s response epoch also matches (635, 490 in the response epoch). With correct and error trials, the reading of the deposited code, the counts are lower (571, 152, 287, 404).

### fig1f-rate-recovery
**Result: partially reproduced.** The code's selection gives exactly the paper's 168, 168 and 175 neurons. In the window centred 400 ms after offset (reading b), 13.1%, 14.3% and 9.1% of neurons still have a significant rate change (mean 12.2%), and in the window starting at offset (reading a) 17.9%, 19.6% and 10.9%; only the third condition is within 10 +- 1%, and all are below 20%, the criterion's bound for partial reproduction. Before photoinhibition the test flags 0 to 1.1% of neurons.

### fig1g-selectivity-recovery
**Result: reproduced.** Under the code's method (selective on all trials, more than 2 trials per condition, 200 ms windows), selectivity recovers to 80% of control 347 +- 251 ms after the sample photoinhibition, 420 +- 257 ms after the early delay one and 236 +- 97 ms after the middle delay one, all within the paper's 373 +- 260, 510 +- 218 and 327 +- 112 ms, and over 99% of bootstrap resamples recover before the cue in each condition. All four readings with 200 ms windows match; the readings with 400 ms windows stamped at their end do not. The selection has 72 neurons (70 to 87 across readings) against the paper's 55.

### fig2-bilateral-recovery
**Result: partially reproduced.** After ipsilateral photoinhibition the population rate is back to 0.96 of control 600 ms after offset and 9.4% of neurons have a significant change there, so the rate recovers under both readings. Contralateral photoinhibition leaves the rate at 0.90 of control during photoinhibition, and its selectivity recovers in 240 +- 180 ms (code reading), within 192 +- 114 ms. Bilateral selectivity never reaches 80% before the cue (0 of 1000 resamples), and the bilateral rate is 1.11 of control just before the cue, just outside the criterion's 10%. Ipsilateral selectivity recovers only partly: 0.2 s before the cue it is still 48% below control (code reading), and only 25% of resamples reach 80% before the cue; the mean over those, 716 ms, is outside 538 +- 178 ms, and among all readings only the conditional means of the correct-trial readings (637 and 533 ms, from 30% and 16% of resamples) fall within. The selection has 146 neurons against 143.

### ed7-unilateral-4-spots-bilateral-1-spot
**Result: partially reproduced.** In the six Experiment 3 sessions, selectivity recovers 530 +- 174 ms after ipsilateral 4-spot photoinhibition and 119 +- 178 ms after contralateral 4-spot photoinhibition (code reading), within 490 +- 280 and 235 +- 156 ms. Bilateral 1-spot photoinhibition leaves a larger change in the last 400 ms of the delay than ipsilateral 4 spots (-0.55 against -0.21 spikes/s, paired difference p = 0.53), but its selectivity reaches 80% of control before the cue in 80% of resamples (335 ms), where the paper reports no recovery. The selection has 32 neurons against 40.

### ed2b-silencing
**Result: reproduced.** With the window before the offset ramp (reading a), the mean normalized rate of pyramidal neurons gives a reduction of 0.91 to 0.94 for ipsilateral and bilateral photoinhibition in Experiment 1 (0.910 to 0.938), Experiment 2 (0.916, 0.924) and Experiment 3 (0.962, 0.940), and in Experiment 2 ipsilateral 0.951 in PV x ReaChR and 0.845 in VGAT-ChR2 mice, all at least 0.81. Contralateral photoinhibition leaves the mean normalized rate at 0.945 (Experiment 2) and 1.152 (Experiment 3), within 0.8 to 1.2. With the whole period (reading b) the Experiment 3 contralateral value is 1.222, outside.

### ed2e-no-rebound
**Result: partially reproduced.** On lick right trials after ipsilateral photoinhibition (306 neurons above 1 spike/s), the population rate is not higher than control in the first 400 ms after offset (difference -0.14 spikes/s, p = 0.565) or the next 400 ms (+0.10, p = 0.617), so there is no rebound on average. But more neurons are significantly excited (24) than suppressed (9) in the first 400 ms, the opposite of the claim's balance; without the rate exclusion the counts are 30 and 9.

### ed4-return-to-trajectory
**Result: not reproduced.** 55 Experiment 1 pyramidal neurons (4 mice) decrease their rate through the delay, against 27 from 6 mice. For the 47 with enough photoinhibition trials, the RMS distance to the time-matched control (0.526 of the mean rate) is larger than to the end point (0.463) after early-delay photoinhibition (paired p = 0.019, the opposite direction), and not different with the three conditions pooled (0.551 against 0.526, p = 0.18). In Experiment 2 (111 neurons, 7 mice) the two are equal (p = 0.77). For neurons with increasing rates the time-matched distance is smaller (p = 0.0008 and 0.0003), as for Fig. 1e.

### ed10e-callosotomy-preparatory-activity
**Result: partially reproduced.** The callosotomy sessions hold 519 putative pyramidal neurons, against 496. With correct and error trials, 259 are selective, within 254 +- 25; with correct trials only, 303. The selective fraction is 0.50 against 0.64 in control mice under the same reading (0.58 against 0.71 with correct trials), more than the criterion's 10 points lower. Delay selectivity is present and rises toward the cue (1.08 spikes/s 1.5 s before the cue, 2.44 at 0.1 s before).

### fig5-callosotomy-recovery
**Result: reproduced.** In the callosotomy sessions the population rate is back to 1.05 of control just before the cue after ipsilateral photoinhibition, while ipsilateral selectivity stays 67% below control 0.2 s before the cue and recovers in under 1% of resamples. Contralateral selectivity recovers in 297 +- 251 ms (code reading), within 217 +- 228 ms, and bilateral selectivity does not recover (0 of 1000 resamples). The selection has 125 neurons against 129. The session rule gives 16 callosotomy sessions, as Fig. 5f, and the ipsilateral cd ROC at the end of the delay is 0.566, lower than the callosotomy control (0.718, paired p = 0.006) and the Experiment 2 ipsilateral ROC (0.706, p = 0.003).

### fig1d-earlier-photoinhibition-minimal
**Result: reproduced.** In the Experiment 1 recording sessions (4 mice), early delay photoinhibition lowers performance by 5.0 points (paired t-test p = 0.23) and middle delay photoinhibition by 4.6 points (p = 0.22), neither significant at p < 0.05; both p-values are above the paper's 0.1. The other readings give p from 0.18 to 0.41. Sample photoinhibition changes performance by +0.6 points (p = 0.81). With four mice the test has little power.

### fig2b-bilateral-behaviour
**Result: partially reproduced.** In the bilateral recording sessions, performance (pooled per mouse) is 69.3% with unilateral 1-spot photoinhibition (10 mice, within 70.3 +- 7.0), 75.6% with unilateral 4 spots (3 mice, paper 67.7%), 65.8% with bilateral 1 spot (3 mice, paper 58.0%) and 58.1% with bilateral 4 spots (7 mice, paper 51.4%), against control 78.0%. Every condition is below control; the paired tests give p = 0.025, 0.15, 0.045 and 0.0001, and bilateral 1 spot against unilateral 4 spots p = 0.12. The order unilateral above bilateral 1 spot above bilateral 4 spots holds, but three values are outside tolerance and two tests are not significant.

### fig5b-callosotomy-behaviour
**Result: partially reproduced.** The data set holds only sessions after the cut, so the before-and-after comparison and the interaction cannot be tested. After the cut, unilateral (ipsilateral 1 spot) photoinhibition lowers performance from 74.6% to 59.1% (7 mice, paired p = 0.0033), and 59.1% is within 58.0 +- 5.8%.

### fig3-cd-roc
**Result: partially reproduced.** The session rule gives the paper's 16 sessions from 7 mice. With the mean-difference cd, pyramidal neurons and the code's split, the end-of-delay ROC is 0.719 +- 0.033 (control), 0.706 +- 0.024 (ipsilateral), 0.738 +- 0.033 (contralateral) and 0.595 +- 0.036 (bilateral); the contralateral and bilateral values are within tolerance, the control and ipsilateral values just below (0.76 +- 0.03 and 0.73 +- 0.02). No reading puts all four within tolerance; control, ipsilateral and contralateral each exceed bilateral by more than 0.1 in the main reading.

### ed8-roc-during-photoinhibition
**Result: reproduced.** With projections averaged over the photoinhibition period (reading b), all units and the code's split, the ROC is 0.703 (control), 0.534 (ipsilateral), 0.642 (contralateral) and 0.539 (bilateral), all within the paper's 0.72 +- 0.02, 0.54 +- 0.03, 0.64 +- 0.03 and 0.54 +- 0.01; three of the 24 readings match. With pyramidal neurons only the bilateral value is 0.51 and outside its narrow tolerance.

### ed7e-size-and-roc
**Result: partially reproduced.** Four of the six Experiment 3 sessions pass the session rule. With the mean-difference cd and pyramidal neurons, the ROC is 0.762 (control), 0.621 (ipsilateral 4 spots) and 0.702 (contralateral 4 spots), within tolerance, and 0.604 for bilateral 1 spot, outside 0.54 +- 0.054 and within the 0.08 variant. The ipsilateral 4-spot ROC is below the Experiment 2 ipsilateral 1-spot ROC (0.621 against 0.706), so recovery is less robust with the larger photoinhibition.

### ed9b-cd-stability
**Result: reproduced.** Over all correct control trials, the correlation of the lick right minus lick left difference between the last 400 ms of the sample and of the delay is 0.590 +- 0.075 over 16 sessions (0.622 with all units), within 0.61 +- 0.05.

### ed8a-mode-variance
**Result: not reproduced.** With the mean-difference cd of the Methods, cd captures 72.5% of the selectivity (paper 65.6 +- 5.1) and 39.5% of the variance (36.4 +- 6.3), and modes 1 to 5 capture 97.1% of the variance (98.5 +- 0.5) and 93.9% of the selectivity (95.8 +- 1.2); no reading puts all four, or both cd values, within tolerance. With the code's discriminant as cd, the cd values are 66.1% and 36.6%, both within tolerance.

### fig3-cd-predicts-movement
**Result: reproduced.** On trials pooled over the 16 sessions, the side of the decision boundary predicts the lick on 72.8% of control, 68.6% of ipsilateral, 68.4% of contralateral and 67.1% of bilateral trials (binomial p below 1e-10 in each), and the logistic regression slope of lick right on the projection is positive with p below 1e-10 in each condition. After bilateral photoinhibition the fraction of lick right responses rises from 0.33 to 0.77 across projection bins.

### fig3-other-modes
**Result: not reproduced.** The persistent and ramping modes discriminate trial type only weakly (control ROC 0.567 and 0.577), within 0.5 +- 0.1, but both predict the lick on control trials above chance (accuracy 0.568 and 0.570, binomial p = 0.003 and 0.002). The ramping mode is little changed by ipsilateral and bilateral photoinhibition (+0.51 and -0.48 against a control band of 1.00), but the persistent mode's ipsilateral change (-2.09) is also inside its band (2.17).

### ed6-bilateral-bias-inconsistent
**Result: reproduced.** Under bilateral photoinhibition 8 of 16 sessions are biased (Fisher p < 0.05), 6 toward lick right and 2 toward lick left. The sign of the bias agrees with the nearer control trajectory (reading b) in 88% of biased sessions, and with the side of the decision boundary (reading a) in 62%.

### ed9f-reaction-time
**Result: blocked.** None of the 26 Experiment 2 sessions has a lick trace with detectable licks, so the claim's reaction times cannot be measured. In the 15 callosotomy population sessions whose traces show licks, shown as a variant, reaction time does not correlate with the distance from the boundary (Spearman r = -0.025, p = 0.66 on control trials).

### models-monolithic-fail
**Result: partially reproduced.** Each of the three simulated monolithic models fails to recover in all three draws: the simple integrator ends 21% of its selectivity from the unperturbed output, the single-module attractor switches to the other fixed point (deviation 1.02 to 1.09 of its selectivity), and the FORCE-trained networks end 25% to 87% away. The corrective-feedback integrator and the tamed-chaos network were not simulated, as the paper does not give their weights or retuning.

### fig6-modular-models-robust
**Result: partially reproduced.** With noise drawn each step, the modular attractor recovers after unilateral silencing in 100% and 98% of runs (lick right and lick left) and ends at the wrong fixed point after bilateral silencing in 45% and 63% of runs, within 25% to 75%. With noise of the same intensity per unit time the unperturbed attractor already ends at the wrong fixed point in 45% to 49% of runs. The modular integrator with the printed matrix recovers on lick right trials (selectivity 13.6 against 14.4) but not on lick left trials (-7.2 against -14.4).
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev && python3 - <<'EOF'
s=open('results.md').read()
s=s.replace("gives a reduction of 0.91 to 0.94 for ipsilateral and bilateral photoinhibition in Experiment 1 (0.910 to 0.938), Experiment 2 (0.916, 0.924) and Experiment 3 (0.962, 0.940)","gives a reduction of at least 0.91 for ipsilateral and bilateral photoinhibition in Experiment 1 (0.910 to 0.938), Experiment 2 (0.916, 0.924) and Experiment 3 (0.962, 0.940), and 0.885 and 0.886 in the six sessions with types 4, 5 and 7")
s=s.replace("(binomial p below 1e-10 in each), and the logistic regression slope of lick right on the projection is positive with p below 1e-10 in each condition. After bilateral photoinhibition the fraction of lick right responses rises from 0.33 to 0.77 across projection bins.","(binomial p below 1e-6 in each), and the logistic regression slope of lick right on the projection is positive with p below 1e-6 in each condition. After bilateral photoinhibition the fraction of lick right responses is 0.33 in the most negative projection bin and 0.77 in the most positive.")
open('results.md','w').write(s)
s=open('nb.py').read()
s=s.replace('''    print(prediction_table(dfp).round(4).to_string(index=False))''','''    print(prediction_table(dfp).to_string(index=False, float_format=lambda x: f"{x:.3g}"))''')
open('nb.py','w').write(s)
EOF
cat > $TMPDIR/dev/summary.md <<'EOF'
## Summary

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

| Claim | Outcome |
|---|---|
| units-and-sessions | not reproduced (FS count 89 against 72; the other five counts exact) |
| ed1-selective-fraction | reproduced |
| fig1d-late-delay-ipsilateral-bias | blocked: data missing |
| fig1d-earlier-photoinhibition-minimal | reproduced |
| ed3-recovery-interval | blocked: data missing |
| ed2b-silencing | reproduced |
| ed2d-spatial-extent | blocked: data missing |
| ed2e-no-rebound | partially reproduced |
| fig1f-rate-recovery | partially reproduced |
| fig1g-selectivity-recovery | reproduced |
| ed4-return-to-trajectory | not reproduced |
| ed5-photoactivation | blocked: data missing |
| fig2b-bilateral-behaviour | partially reproduced |
| ed6-bilateral-bias-inconsistent | reproduced |
| fig2-bilateral-recovery | partially reproduced |
| ed7-unilateral-4-spots-bilateral-1-spot | partially reproduced |
| ed7e-size-and-roc | partially reproduced |
| fig3-cd-roc | partially reproduced |
| ed8-roc-during-photoinhibition | reproduced |
| ed9b-cd-stability | reproduced |
| ed8a-mode-variance | not reproduced |
| fig3-cd-predicts-movement | reproduced |
| fig3-other-modes | not reproduced |
| ed9f-reaction-time | blocked: data missing (no licks in the Experiment 2 lick traces) |
| fig5b-callosotomy-behaviour | partially reproduced (after the cut only) |
| fig5-callosotomy-recovery | reproduced |
| ed10e-callosotomy-preparatory-activity | partially reproduced |
| models-monolithic-fail | partially reproduced (three of five models simulated) |
| fig6-modular-models-robust | partially reproduced |

**How the analysis differs from the paper's.** Open method details are taken from the authors'
MATLAB scripts deposited in the data set: trial selection (correct and error trials, stable trials,
lick-early trials dropped), the preference screening, the recovery-time bootstrap, the neuron
selections and the population session rule. The scripts reproduce several of the paper's counts
exactly (168, 168 and 175 neurons in Fig. 1f; 16 sessions in Fig. 3 and Fig. 5f). The coding
direction is the mean difference of the Methods; the scripts' linear discriminant is shown as a
variant. Rates and PSTHs are computed from 10 ms bins, and recovery times are resolved to 10 ms.
Behavioural claims use the recording sessions, as the behaviour-only sessions are not in the data
set. The network simulations use standard choices where the Methods leave details open
(`models.py`).

**What was found about the data set.** It holds what its description says: 91 sessions from 19
mice, 1012 single units in the 58 non-callosotomy sessions and 567 in the 33 callosotomy
sessions, with trial tables, photostimulus types whose laser timing matches their description,
and the gene modification of each mouse in the meta data files. The FS labels do not match the
paper's count (89 against 72) or the deposited waveforms' widths. The units have no `depth`
field, which the description lists. The lick trace shows no licks in 48 of 90 sessions, all 26
Experiment 2 sessions among them, so reaction times cannot be measured there. In four sessions
photoinhibition does not reduce activity, so the clock check by the laser fails there. Type 9 is
still described in the files as "Right ALM (ipsilateral)", which the FAQ says is contralateral.
One callosotomy session has no performing trials. The behaviour-only sessions, the photoactivation
data, the recordings in untrained mice and the simulations named in the title are not in the data
set.
EOF
python3 - <<'EOF'
# converter: insert results after last claim cell
import re
p='/tmp/claude-1001/dev/convert.py'
s=open(p).read()
s=s.replace('''if tail:
    for part in tail.split("\\n<<<CELL>>>\\n"):
        cells.append(nbformat.v4.new_markdown_cell(part.strip()))''','''if len(sys.argv) > 5:
    res = {}
    for block in open(sys.argv[4]).read().split("### ")[1:]:
        cid, _, text = block.partition("\\n")
        res[cid.strip()] = text.strip()
    last = {}
    for i, c in enumerate(cells):
        for t in c.metadata.get("tags", []):
            if t.startswith("claim:"):
                last[t[6:]] = i
    for cid in sorted(res, key=lambda k: -last[k]):
        cells.insert(last[cid] + 1, nbformat.v4.new_markdown_cell(res[cid]))
    missing = set(last) - set(res)
    print("claims without a result:", missing)
if tail:
    cells.append(nbformat.v4.new_markdown_cell(tail.strip()))''')
s=s.replace('tail = open(sys.argv[3]).read() if len(sys.argv) > 4 else ""','tail = open(sys.argv[3]).read() if len(sys.argv) > 4 else ""')
open(p,'w').write(s)
EOF
python3 $TMPDIR/dev/convert.py $TMPDIR/dev/nb.py $TMPDIR/dev/header.md $TMPDIR/dev/summary.md $TMPDIR/dev/results.md entries/crcns-alm-3-li-2016/reproduce_li_2016.ipynb
```

```
claims without a result: set()
cells 93
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; python3 tools/entry.py all entries/crcns-alm-3-li-2016 2>&1 | tail -4; date -u
```

```
Sat Nov  7 20:15:55 UTC 2026
Installed kernelspec registry-crcns-alm-3-li-2016 in executed/crcns-alm-3-li-2016/.venv/share/jupyter/kernels/registry-crcns-alm-3-li-2016
0 error(s)
pass  reproduce_li_2016.ipynb  (209 s)
Sat Nov  7 20:19:32 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'EOF' > $TMPDIR/out2.txt
import nbformat
nb=nbformat.read('executed/crcns-alm-3-li-2016/reproduce_li_2016.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    txt=''.join(o.get('text','') for o in c.outputs if o.output_type=='stream')
    err=[o for o in c.outputs if o.output_type=='error']
    print(f'=== cell {i} {c.metadata.get("tags",[])}', 'ERROR' if err else ''); print(txt)
EOF
diff <(grep -v "loaded 91\|FORCE networks trained\|measures for" $TMPDIR/out.txt) <(grep -v "loaded 91\|FORCE networks trained\|measures for" $TMPDIR/out2.txt) | head -80
```

```
1c1
< === cell 1 []
---
> === cell 1 [] 
3c3
< === cell 2 []
---
> === cell 2 [] 
5c5
< === cell 3 []
---
> === cell 3 [] 
7c7
< === cell 4 ['sanity']
---
> === cell 4 ['sanity'] 
103c103
< === cell 5 ['sanity']
---
> === cell 5 ['sanity'] 
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
diff <(grep -v "loaded 91\|FORCE networks trained\|measures for\|=== cell\|ipykernel" $TMPDIR/out.txt) <(grep -v "loaded 91\|FORCE networks trained\|measures for\|=== cell\|ipykernel" $TMPDIR/out2.txt) | grep -v "^[<>] *$" | head -60; grep -c ERROR $TMPDIR/out2.txt
```

```
142a143,151
> Mouse lines from the meta data files (gene modification), by experiment group:
> group        line       
> callosotomy  PV x ReaChR    1
>              VGAT-ChR2      6
> control      PV x ReaChR    7
>              VGAT-ChR2      5
> Mice whose sessions disagree on the line: []
> Data description: 5 VGAT-ChR2-EYFP and 7 PV x ReaChR mice for electrophysiology; callosotomy 6 VGAT-ChR2-EYFP and 1 PV x ReaChR.
445,446d453
< ?           exp2b        122  0.115      0.885
<             exp3         112  0.049      0.951
447a455,456
>             exp2b         70  0.014      0.986
>             exp3          34  0.068      0.932
449a459,465
>             exp2b         52  0.250      0.750
>             exp3          78  0.041      0.959
> By mouse line, Experiment 2 ipsilateral (type 4), as ED Fig. 2b right:
>              size   mean  reduction
[... 38 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,40p attempts/001453-fouke-2025-01.yaml | head -5; grep -n "^findings\|^verifications\|^  found\|^- kind" -A3 attempts/001453-fouke-2025-01.yaml | head -20; python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s['properties']['findings'],indent=0)[:1500]); print(list(s['properties'].keys()))"
```

```
schema_version: 2
id: 001453-fouke-2025-01
dataset:
  archive: dandi
  id: "001453"
243:findings:
244:- kind: data_missing
245-  statement: The dandiset holds only the freely swimming tracking of Figure 1 and Figure S1. The
246-    two-photon imaging and the head-fixed tail tracking behind Figures 2 to 4 are not in it, and
247-    the GitLab repository the paper names for all behavioural and imaging data holds analysis
--
249:- kind: metadata_insufficient
250-  statement: The stimulus codes 0 to 20 have no names or description in the files or the
251-    dandiset metadata. They can be named only from the paper's analysis notebook and the protocol
252-    file of its stimulus software.
253:- kind: code_mismatch
254-  statement: The paper's analysis notebook labels code 9 as lateral right and 11 as lateral left,
255-    while its conversion of the stimulus software's names gives the reverse (it carries a remap
256-    that swaps them). The data do not settle which is right; zebrafish barely turn to either, and
--
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/dev/attempt.py <<'PYEOF'
import yaml
NB = "reproduce_li_2016.ipynb"
CODE = ("The authors' MATLAB scripts deposited in the data set (alm-3/live/analyses_scripts/), which "
        "the data description says reproduce the paper's figures, are used as the paper's analysis code "
        "for details the claims file and the Methods leave open; the paper itself links no code.")
def o(claim, outcome, notes, deviations=None, measured=None, blocked_by=None, assumed=None, output=True):
    d = {"claim": claim, "outcome": outcome}
    if blocked_by:
        d["blocked_by"] = blocked_by
    if output:
        d["notebook"] = NB
        d["output"] = f"claim:{claim}"
    if measured is not None:
        d["measured"] = measured
    d["notes"] = notes
    if deviations:
        d["deviations"] = deviations
    if assumed:
        d["assumed"] = True
    return d

outcomes = [
o("units-and-sessions", "not_reproduced",
  "The 58 non-callosotomy sessions (20 unilateral, 38 bilateral) from 12 mice hold 1012 single units, 890 "
  "labelled pyramidal, all as the paper reports. 89 units are labelled FS and 33 carry no cell-type label, "
  "against 72 FS and 50 intermediate in the paper. By the trough-to-peak width of the deposited mean "
  "waveform (29 samples at 19.53 kHz, steps of 0.051 ms) there are 890 pyramidal, 98 FS and 24 "
  "intermediate units, and 889, 104 and 19 after tenfold spline upsampling. 15 units labelled FS have a "
  "width of 0.358 ms, inside the excluded range. Five of six counts match exactly; the FS count is 24% "
  "above the paper's, so neither the criterion's full nor its partial rule holds.",
  ["Cell classes are read from the data set's cellType labels, with the width of the deposited mean "
   "waveform as a second reading; the paper's width measurement (interpolation, filtering) is not "
   "described beyond trough to peak."],
  [1012, 20, 38, 890, 89, 12]),
o("ed1-selective-fraction", "reproduced",
  "Correct control trials, lick-early trials excluded, 1.3 s response epoch (reading a of M3 and M1, "
  "the code's response window): 633 of 890 pyramidal neurons selective in some epoch, 176 in the sample, "
  "336 in the delay and 493 in the response epoch (paper 634, 176, 337, 493). The 1.5 s response epoch "
  "also matches (635 and 490). With correct and error trials, the trials the deposited script selects, "
  "the counts are 571, 152, 287 and 404; with lick-early trials included 596, 161, 315 and 433. The "
  "first 400 ms after the cue gives 411 response-selective neurons. 1 neuron could not be tested.",
  ["Response epoch taken as the 1.3 s after the cue, from the deposited script "
   "(analysis_compile_all_data_unilateral.m, significant selectivity); the 0.4 s and 1.5 s readings of M2 "
   "are shown. " + CODE],
  [633, 176, 336, 493]),
o("fig1d-late-delay-ipsilateral-bias", "blocked",
  "The recording sessions hold photoinhibition in the sample, early delay and middle delay windows "
  "(types 1 to 3, ending 1.6, 0.8 and 0.3 s before the cue by the laser trace); none ends at the go cue. "
  "The behaviour-only sessions of Fig. 1d are not in the data set; its FAQ says the published data cover "
  "only the electrophysiology sessions. No other public copy was found.",
  blocked_by="data_missing", output=False),
o("fig1d-earlier-photoinhibition-minimal", "reproduced",
  "Recording sessions of Experiment 1, 4 mice (paper 5, behaviour sessions). Performance pooled per "
  "mouse: control 79.5%, early delay 74.5% (drop 5.0 points, paired t-test p = 0.23), middle delay 74.9% "
  "(drop 4.6, p = 0.22). Unpaired tests and per-session means give p from 0.18 to 0.41. No condition "
  "reaches p < 0.05, and all p-values are above the paper's 0.1. Sample photoinhibition +0.6 points "
  "(p = 0.81). With four mice the test has little power; the drops are about five points.",
  ["Tested on the recording sessions of Experiment 1 (4 mice, 0.5 s photoinhibition with 100 ms ramp), "
   "as the behaviour-only sessions of Fig. 1d are not in the data set; the three sessions with the "
   "no-ramp types -1 to -3 are left out, as the data set says not to analyse them.",
   "Performance is hits over hits and errors on performing trials, no-lick and lick-early trials "
   "excluded, as the data set's Demo_get_performance.m computes it."]),
o("ed3-recovery-interval", "blocked",
  "Behaviour-only experiments (ED Fig. 3); the data set's FAQ says they are not included, and only types "
  "1 to 3 of ED Fig. 3a are in the recording sessions (see fig1d-earlier-photoinhibition-minimal). The "
  "1.3 s whole-delay photoinhibition and the other recovery intervals are absent.",
  blocked_by="data_missing", output=False),
o("ed2b-silencing", "reproduced",
  "Window (a), onset to the start of the offset ramp; pyramidal neurons with mean rate of at least 1 "
  "spike/s. Reduction (1 minus mean normalized rate): Experiment 1 0.938, 0.931, 0.910; Experiment 2 "
  "ipsilateral 0.916 and bilateral 0.924; Experiment 3 ipsilateral 4 spots 0.962 and bilateral 1 spot "
  "0.940; sessions with types 4, 5, 7 0.885 and 0.886. Experiment 2 ipsilateral by line 0.951 (PV x "
  "ReaChR, 216 neurons) and 0.845 (VGAT-ChR2, 106). Contralateral mean normalized rate 0.945 (Experiment "
  "2), 1.152 (Experiment 3), 0.986 (types 4, 5, 7). With window (b), the whole period, the Experiment 3 "
  "contralateral value is 1.222, outside 0.8 to 1.2, and the VGAT reduction 0.831. The callosotomy "
  "sessions, not part of the claim, give 0.880 (ipsilateral) and 0.764 (bilateral).",
  ["Mouse lines are read from the gene modification in the data set's meta data files.",
   "Neurons need at least 3 photoinhibition and 5 control trials, a standard choice; the paper's n "
   "(300, 294, 301 in Experiment 2) are close to the 322, 319, 323 here."],
  0.916),
o("ed2d-spatial-extent", "blocked",
  "Measured in 4 untrained mice (ED Fig. 2d); the data set's 19 mice are the behaving electrophysiology "
  "and callosotomy mice, and no recordings at varying distance from the light are included.",
  blocked_by="data_missing", output=False),
o("ed2e-no-rebound", "partially_reproduced",
  "Experiment 2, lick right trials, ipsilateral photoinhibition, 306 pyramidal neurons above 1 spike/s. "
  "0 to 400 ms after offset, photoinhibition minus control -0.14 spikes/s (paired t = -0.58, p = 0.565); "
  "400 to 800 ms +0.10 (p = 0.617): no rebound on average. In the first window 24 neurons are "
  "significantly excited and 9 suppressed (p < 0.01), the opposite of the claim's balance; without the "
  "rate exclusion (408 neurons) 30 and 9. The average part holds, the proportion part does not.",
  ["The population test (paired t-test over neurons) is the criterion's standard choice."]),
o("fig1f-rate-recovery", "partially_reproduced",
  "The deposited script's selection (pyramidal, mean rate above 1 spike/s, more than 8 control and more "
  "than 3 photoinhibition trials of each type) gives 168, 168 and 175 neurons, as Fig. 1f. Fraction with "
  "a significant change: reading (a), window starting at offset, 0.179, 0.196, 0.109 (mean 0.161); "
  "reading (b), window centred 400 ms after offset, 0.131, 0.143, 0.091 (mean 0.122). Only the middle "
  "delay condition is within 0.1 +- 0.01; all are below 0.2. Without the rate exclusion (224, 225, 241 "
  "neurons) reading (b) gives 0.121, 0.124, 0.087. The test flags 0 to 1.1% of neurons before onset. "
  "The script's own measure, the fraction 0.25 s before the cue, is 0.054, 0.125 and 0.383, the last "
  "inside the middle-delay photoinhibition.",
  ["Neuron selection from the deposited script (analysis_compile_all_data_unilateral.m, Fig. 1f "
   "section), which fills M3's open inclusion rule. " + CODE],
  [0.161, 168, 168, 175]),
o("fig1g-selectivity-recovery", "reproduced",
  "Method of the deposited script (5 screening trials per type, preference on the count from sample "
  "onset to 1.3 s after the cue, 200 ms boxcar, bootstrap of the first time after offset where the "
  "deficit is below 20%, mean +- s.d. over 1000 resamples). Selective on all trials, more than 2 trials "
  "per condition: 347 +- 251 ms (sample), 420 +- 257 ms (early delay), 236 +- 97 ms (middle delay), "
  "within 373 +- 260, 510 +- 218 and 327 +- 112 ms; over 99% of resamples recover before the cue. The "
  "other 200 ms readings (correct trials, more than 3 trials) also match; the 400 ms readings stamped at "
  "their end do not (628, 760, 448 ms). 72 neurons against 55 (outside the 10% tolerance of that "
  "expected value; 70 to 87 across readings).",
  ["Screening, selection and the bootstrap recovery rule from the deposited script "
   "(analysis_compile_all_data_unilateral.m, Fig. 1g section): 5 control trials of each type set the "
   "preference (the Methods' subset of 10 trials), the recovery time is searched from offset to 1 s "
   "after the cue. " + CODE,
   "PSTHs are evaluated every 10 ms (the script uses 1 ms), so recovery times are resolved to 10 ms."],
  [347, 420, 236, 72]),
o("ed4-return-to-trajectory", "not_reproduced",
  "55 Experiment 1 pyramidal neurons from 4 mice have a significantly lower rate in the last than in "
  "the first 400 ms of the delay (paper 27 from 6 mice). For the 47 tested, RMS (in units of the "
  "neuron's mean rate, offset to 0.1 s before the cue) to the time-matched control is 0.526 and to the "
  "end point 0.463 after early-delay photoinhibition (paired t = 2.43, p = 0.019, larger to the "
  "time-matched control), and 0.551 against 0.526 with the three conditions pooled (p = 0.18). In "
  "Experiment 2 (111 neurons, 7 mice, ipsilateral photoinhibition) 0.739 against 0.743 (p = 0.77). "
  "Neurons with increasing rates show the expected order (1.068 against 1.230, p = 0.0008).",
  ["The start and end of the delay are read as its first and last 400 ms; the RMS ends 0.1 s before "
   "the cue, where the 200 ms boxcar stops before the response epoch.",
   "The paper's 6 mice cannot come from Experiment 1, which has 4 mice in the data set; Experiment 2 is "
   "shown as a variant."],
  [55]),
o("ed5-photoactivation", "blocked",
  "The photoactivation data (Tlx_PL56-cre x Ai32 mice) are not in the data set; its FAQ says they were "
  "not published and would be added. No other public copy was found.",
  blocked_by="data_missing", output=False),
o("fig2b-bilateral-behaviour", "partially_reproduced",
  "Bilateral recording sessions, performance pooled per mouse: control 78.0%; unilateral 1 spot 69.3% "
  "(10 mice, paired p = 0.025, within 70.3 +- 7.0); unilateral 4 spots 75.6% (3 mice, p = 0.15; paper "
  "67.7%); bilateral 1 spot 65.8% (3 mice, p = 0.045; paper 58.0%); bilateral 4 spots 58.1% (7 mice, "
  "p = 0.0001; paper 51.4%). Bilateral 1 spot against unilateral 4 spots 65.8 against 75.6% (3 mice, "
  "p = 0.12). The order unilateral, bilateral 1 spot, bilateral 4 spots holds with each below control; "
  "three values are outside tolerance and two tests not significant.",
  ["Recording sessions only (0.8 s photoinhibition from delay onset, 10 mice); the paper's values come "
   "from 13 mice including behaviour-only sessions with 0.8 and 1.3 s photoinhibition."]),
o("ed6-bilateral-bias-inconsistent", "reproduced",
  "16 sessions of fig3-cd-roc. 8 sessions are biased under bilateral photoinhibition (Fisher p < 0.05), "
  "6 toward lick right and 2 toward lick left. The sign of the bias agrees with the nearer control "
  "trajectory (reading b) in 7 of 8 (0.88) and with the side of the decision boundary (reading a) in 5 "
  "of 8 (0.62). With all units, 0.75 and 0.62. Over all 16 sessions the bias and the mean perturbed "
  "projection correlate with Spearman r = 0.34 (p = 0.20).",
  ["The claim is reproduced under reading (b) of the criterion and not under reading (a)."]),
o("fig2-bilateral-recovery", "partially_reproduced",
  "Experiment 2 (types 4, 5, 6). Rates: ipsilateral 0.958 of control 600 ms after offset with 9.4% of "
  "neurons significantly changed (both readings recover); contralateral 0.901 during photoinhibition; "
  "bilateral 1.164 at 600 ms after offset and 1.114 just before the cue (outside the criterion's 10%). "
  "Selectivity (code reading, 146 neurons against 143): contralateral 240 +- 180 ms, within 192 +- 114; "
  "bilateral reaches 80% in 0 of 1000 resamples. Ipsilateral selectivity is still 48% below control 0.2 s "
  "before the cue, and 25% of resamples reach 80% before the cue, at 716 ms on average (outside 538 +- "
  "178); counting the others at the cue, as the script's arrays do, gives 854 ms. Of the other readings "
  "only the correct-trial 200 ms ones give conditional means within tolerance (637 and 533 ms) from 30% "
  "and 16% of resamples.",
  ["Selection, screening (10 trials per type) and the recovery rule (searched from offset to the cue) "
   "from the deposited script analysis_compile_all_data_bilateral.m, Fig. 2e section. " + CODE],
  [716, 240, 146]),
o("ed7-unilateral-4-spots-bilateral-1-spot", "partially_reproduced",
  "Experiment 3 sessions (types 7, 8, 9), code reading, 32 neurons (paper 40). Ipsilateral 4 spots "
  "530 +- 174 ms and contralateral 4 spots 119 +- 178 ms, within 490 +- 280 and 235 +- 156 ms. Bilateral "
  "1 spot reaches 80% of control before the cue in 80% of resamples (335 ms), where the paper reports no "
  "recovery; 63% with 400 ms windows. Delta selectivity in the last 400 ms of the delay: bilateral 1 spot "
  "-0.55 spikes/s, ipsilateral 4 spots -0.21 (larger in magnitude for bilateral; paired p = 0.53).",
  ["Method of fig2-bilateral-recovery on the Experiment 3 sessions; the deposited scripts contain none "
   "for Experiment 3."],
  [530, 119, 32]),
o("ed7e-size-and-roc", "partially_reproduced",
  "4 of the 6 Experiment 3 sessions pass the session rule. Mean-difference cd, pyramidal neurons, code "
  "split: ROC 0.762 (control), 0.621 (ipsilateral 4 spots), 0.702 (contralateral 4 spots), within "
  "tolerance, and 0.604 (bilateral 1 spot), outside 0.54 +- 0.054 and within the 0.08 variant. No "
  "reading puts the bilateral value within 0.054 (0.598 to 0.642). Ipsilateral 4 spots 0.621 against "
  "Experiment 2 ipsilateral 1 spot 0.706, so recovery is less robust with larger photoinhibition.",
  ["Three of the six Experiment 3 sessions, and one of them only in part, carry the paper's ROC; with "
   "4 sessions the s.e.m. of the control ROC is 0.14."],
  [0.762, 0.621, 0.702, 0.604]),
o("fig3-cd-roc", "partially_reproduced",
  "The session rule of the deposited script (pyramidal neurons stable at trial 50 and 50 before the "
  "end, more than 5 neurons, at least 5 trials per group) gives the paper's 16 sessions from 7 mice "
  "(175 neurons). Mean-difference cd, code split: ROC 0.719 +- 0.033 (control), 0.706 +- 0.024 "
  "(ipsilateral), 0.738 +- 0.033 (contralateral), 0.595 +- 0.036 (bilateral); contralateral and "
  "bilateral within tolerance, control and ipsilateral just below. No reading of the 12 run puts all "
  "four within tolerance. Control, ipsilateral and contralateral each exceed bilateral by more than 0.1 "
  "in the main reading.",
  ["The control/test split follows the deposited script (as many control test trials of each type as "
   "the mean number of photoinhibition trials per type); random halves (M6 a) are shown. The "
   "leave-one-out split (M6 b) was not run.",
   "cd is the mean difference of the Methods; the deposited script's linear discriminant is shown as a "
   "variant (0.721, 0.710, 0.745, 0.584)."],
  [16, 0.719, 0.706, 0.738, 0.595]),
o("ed8-roc-during-photoinhibition", "reproduced",
  "Reading (b), projections averaged over the photoinhibition period, with all single units and the "
  "code split: ROC 0.703 (control), 0.534 (ipsilateral), 0.642 (contralateral), 0.539 (bilateral), all "
  "within tolerance (0.72 +- 0.02, 0.54 +- 0.03, 0.64 +- 0.03, 0.54 +- 0.01). 3 of 24 readings match. "
  "With pyramidal neurons the bilateral value is 0.51 and outside its tolerance of 0.01; with window (a) "
  "the ipsilateral and bilateral values are 0.48 to 0.53.",
  ["The matching reading uses all single units (M6 reading b) and the window average (reading b)."],
  [0.703, 0.534, 0.642, 0.539]),
o("ed9b-cd-stability", "reproduced",
  "All correct control trials: Pearson correlation of w between the last 400 ms of the sample and of "
  "the delay 0.590 +- 0.075 over 16 sessions (pyramidal), 0.622 +- 0.060 over 17 (all units); within "
  "0.61 +- 0.05. With the correct training trials only, 0.520 and 0.570.",
  measured=0.590),
o("ed8a-mode-variance", "not_reproduced",
  "Mean-difference cd (Methods), pre-sample baseline, squared-norm shares (the script's): selectivity "
  "on cd 72.5% (paper 65.6 +- 5.1), variance on cd 39.5% (36.4 +- 6.3), modes 1 to 5 variance 97.1% "
  "(98.5 +- 0.5) and selectivity 93.9% (95.8 +- 1.2). RMS shares give 84.7%, 60.3%, 98.5% and 96.9%. No "
  "reading puts all four, or both cd values, within tolerance with the mean-difference cd. With the "
  "script's linear discriminant as cd, the cd values are 66.1% and 36.6%, both within tolerance, and the "
  "mode 1 to 5 values 96.9% and 93.4%, outside.",
  ["Modes, baseline (the window 3.4 to 3.0 s before the cue) and the squared-norm shares from the "
   "deposited script (analysis_compile_all_data_bilateral_activityModes.m, ED Fig. 8 sections), with "
   "the mean-difference cd of the Methods; the script's discriminant cd is a variant. The modes are "
   "fully Gram-Schmidt orthogonalized (Methods); the script orthogonalizes the persistent modes "
   "against the singular vectors only."],
  [72.5, 39.5, 97.1, 93.9]),
o("fig3-cd-predicts-movement", "reproduced",
  "Trials pooled over 16 sessions. Prediction accuracy from the side of the boundary: control 0.728 "
  "(412 trials, binomial p = 3.2e-21), ipsilateral 0.686 (p = 6.9e-12), contralateral 0.684 (p = 2.4e-12), "
  "bilateral 0.671 (p = 1.3e-16); logistic slopes 0.145, 0.138, 0.105, 0.105, p below 2.5e-10. On error "
  "trials alone accuracy is 0.53 to 0.67. After bilateral photoinhibition the fraction of lick right "
  "responses is 0.33 in the most negative and 0.77 in the most positive projection bin."),
o("fig3-other-modes", "not_reproduced",
  "Persistent mode (mode 2): control ROC 0.567, prediction accuracy 0.568 (binomial p = 0.003), "
  "ipsilateral change -2.09 against a control s.e.m. band of 2.17. Ramping mode (mode 4): control ROC "
  "0.577, accuracy 0.570 (p = 0.002), ipsilateral +0.51 and bilateral -0.48 against a band of 1.00. "
  "The ROCs are within 0.5 +- 0.1 and the ramping mode is robust, but both modes predict the lick above "
  "chance and the persistent mode's ipsilateral change lies inside its band. With all units the ramping "
  "accuracy is 0.529 (p = 0.12) and the persistent accuracy 0.547 (p = 0.026).",
  ["Modes from ed8a-mode-variance with the mean-difference cd."]),
o("ed9f-reaction-time", "blocked",
  "The reaction time needs lick times. The data set has no lick events, and its lick trace shows "
  "detectable licks in 42 of 90 sessions and in none of the 26 Experiment 2 sessions, where the first "
  "threshold crossing after the cue falls within 2 ms of it (trace range 0.002 against 0.05 in sessions "
  "with licks). As a variant, in the 15 callosotomy population sessions with licks, reaction time does "
  "not correlate with the distance from the boundary (Spearman r = -0.025, p = 0.66, control trials).",
  blocked_by="data_missing"),
o("fig5b-callosotomy-behaviour", "partially_reproduced",
  "Only sessions after the cut are in the data set (5 to 6 daily sessions per mouse), so the "
  "before-and-after comparison and the interaction cannot be tested. After the cut, ipsilateral 1-spot "
  "photoinhibition lowers performance from 74.6% to 59.1% (7 mice, paired p = 0.0033; per-session means "
  "73.9% to 57.9%, p = 0.0071), and 59.1% is within 58.0 +- 5.8%. Control-trial performance of the "
  "callosotomy mice and of the control mice (different animals) is shown for context.",
  ["Judged on the after-cut test alone, as the criterion says when no sessions before the cut exist."]),
o("fig5-callosotomy-recovery", "reproduced",
  "Callosotomy sessions (types 10, 11, 12), code reading, 125 neurons (paper 129). Ipsilateral rate 1.053 "
  "of control just before the cue (1.081 at 600 ms after offset); ipsilateral selectivity 67% below "
  "control 0.2 s before the cue, reaching 80% in 0.3% of resamples. Contralateral 297 +- 251 ms, within "
  "217 +- 228. Bilateral selectivity reaches 80% in 0 of 1000 resamples. The session rule gives 16 "
  "callosotomy sessions (Fig. 5f: 16). Ipsilateral cd ROC 0.566 against the callosotomy control 0.718 "
  "(paired p = 0.006) and the Experiment 2 ipsilateral ROC 0.706 (p = 0.003).",
  ["Conditions as the data set labels them; selection and recovery rule from the deposited script "
   "analysis_compile_all_data_bilateralCCX.m. " + CODE,
   "Reduced read as lower by a t-test over sessions at p < 0.05, a standard choice."],
  [297, 125, 16]),
o("ed10e-callosotomy-preparatory-activity", "partially_reproduced",
  "519 putative pyramidal neurons in the callosotomy sessions (paper 496). Selective: 259 with correct "
  "and error trials (within 254 +- 25.4), 303 with correct trials. Fraction 0.499 against 0.642 in "
  "control mice under the same reading (0.584 against 0.711 with correct trials), more than 10 points "
  "lower. Delay selectivity of selective neurons rises from 1.08 spikes/s 1.5 s before the cue to 2.44 "
  "0.1 s before. The selective count and the rising delay selectivity hold; the neuron count and the "
  "similarity of fractions do not.",
  measured=[259, 519]),
o("models-monolithic-fail", "partially_reproduced",
  "Simulated: the simple integrator (three connectivity draws) ends 21% of its selectivity away from "
  "the unperturbed output; the single-module attractor switches fixed point (deviation 1.02 to 1.09 of "
  "its selectivity) with either neuron silenced; the FORCE-trained networks (three draws, ramp learned "
  "with RMS error near 0) end 25% to 87% away. All draws of all three exceed the 20% criterion. Not "
  "simulated: the integrator with corrective feedback (ED Fig. 1g), whose weights the paper does not "
  "give, and the tamed-chaos network (ED Fig. 1i), whose pruning threshold and retuning it does not "
  "give.",
  ["The simple integrator's matrix is taken as 0.99 u u^T with random u, the FORCE target as a linear "
   "ramp, with output feedback and an RLS update every 2 ms (standard choices; see models.py).",
   "Two of the five model classes could not be simulated for lack of parameters."],
  assumed=True),
o("fig6-modular-models-robust", "partially_reproduced",
  "Modular attractor, noise drawn each step: recovery after unilateral silencing in 100% and 98% of "
  "runs (lick right, lick left); wrong fixed point after bilateral silencing in 45% and 63% (within 25% "
  "to 75%), though 80% of bilateral runs have not settled by 2 s. With noise of the same intensity per "
  "unit time the unperturbed attractor already ends at the wrong fixed point in 45% to 49% of runs, so "
  "that reading is not a working model. Modular integrator with the printed matrix: after silencing "
  "module 1 its selectivity returns to 13.6 against 14.4 on lick right trials, but to -7.2 against -14.4 "
  "on lick left trials, as its recovery neuron is driven only by right-preferring activity. The modular "
  "FORCE network was not simulated.",
  ["Noise taken as variance 0.01 per integration step (1 ms), the reading under which the attractor "
   "holds its choice; the per-unit-time reading is shown.",
   "The inter-module partner of each attractor neuron is taken to share its preference."],
  assumed=True),
]

findings = [
 {"kind": "metadata_error", "statement": "The cell-type labels do not match the paper's classes. In the "
  "58 non-callosotomy sessions 89 units are labelled FS and 33 have no label, where the paper reports 72 FS "
  "and 50 excluded units of intermediate width (0.35 to 0.45 ms); 890 pyramidal agree. 15 units labelled FS "
  "have a trough-to-peak width of 0.358 ms in their deposited mean waveform, and 24 unlabelled units are "
  "narrower than 0.35 ms."},
 {"kind": "metadata_error", "statement": "The data description lists a depth field for each unit; the "
  "files have none (fields timeUnit, eventTimes, eventTrials, waveforms, channel, cellType), and the "
  "waveform field is named waveforms."},
 {"kind": "metadata_error", "statement": "Photostimulation type 9 is still described in the files and "
  "the data description as \"Right ALM (ipsilateral)\"; the data set's FAQ says it is contralateral."},
 {"kind": "data_missing", "statement": "The lick trace shows detectable licks in only 42 of 90 sessions "
  "with performing trials, and in none of the 26 Experiment 2 sessions, where it is flat (range about "
  "0.002 against 0.05 elsewhere). The files hold no lick event times, so reaction times cannot be measured "
  "for the paper's population analyses."},
 {"kind": "data_missing", "statement": "The behaviour-only sessions (Fig. 1d, Fig. 2b, ED Fig. 3), the "
  "photoactivation recordings (ED Fig. 5), the recordings in untrained mice (ED Fig. 2d), sessions before "
  "callosotomy (Fig. 5b) and the simulations named in the data set's title are not in the data set. The "
  "FAQ says the photoactivation data would be added."},
 {"kind": "other", "statement": "In four sessions (ANM257636_20150404, ANM264411_20141224, "
  "ANM273657_20150325, ANM298738_20150727) photoinhibition of the left ALM does not reduce pyramidal "
  "activity (rate after laser onset 0.71 to 2.18 times the rate before), where every other session drops "
  "to a median of 0.03. That spikes, laser trace and trial table share a clock could not be shown for "
  "these sessions."},
 {"kind": "metadata_insufficient", "statement": "Nothing in the files says which experiment a session "
  "belongs to. Six sessions from three mice hold types 4, 5 and 7 (ipsilateral 1 spot, contralateral 1 "
  "spot, bilateral 1 spot), a combination the Methods do not describe for either bilateral experiment, "
  "and the deposited scripts analyse neither these nor the Experiment 3 sessions."},
 {"kind": "code_mismatch", "statement": "The deposited analysis scripts differ from the Methods. The "
  "coding direction is a Fisher discriminant averaged over time (func_discriminant.m), where the Methods "
  "define it as the mean difference of the response vectors. The selectivity test uses correct and error "
  "trials although its comment says correct trials; the paper's ED Fig. 1 counts (634, 176, 337, 493) "
  "are matched by correct trials (633, 176, 336, 493) and not by the script's trials (571, 152, 287, 404). "
  "The unilateral script screens 5 trials per type for the preference, the bilateral ones 10, where the "
  "Methods say 10 trials."},
 {"kind": "other", "statement": "Session ANM270340_20150618 has no performing trials (GoodTrials is 0 "
  "for all 322 trials)."},
 {"kind": "methods_unavailable", "statement": "Questions for the authors. (1) Fig. 6b: is the noise "
  "variance of 0.01 per integration step, and what step was used? Per unit time the attractor does not "
  "hold its choice. (2) Fig. 6c: with the printed matrix the recovery neuron restores only "
  "right-preferring activity, so lick left trials do not recover; is the matrix complete? (3) ED Fig. 4: "
  "the 27 neurons come from 6 mice, but Experiment 1 has 4 mice in the data set; which sessions and "
  "photoinhibition conditions were used? (4) Fig. 2e: how were bootstrap resamples that never reach 80% "
  "before the cue counted in the recovery time? In this data set most ipsilateral resamples do not."},
]

rec = {
 "schema_version": 2,
 "id": "crcns-alm-3-li-2016-01",
 "dataset": {"archive": "crcns", "id": "alm-3", "version": "unversioned", "doi": "10.6080/K0RB72JW"},
 "paper": "doi:10.1038/nature17643",
 "date": "2026-11-07",
 "entry": "crcns-alm-3-li-2016",
 "provenance": {"kind": "agent", "accountable": {"name": "CatalystNeuro"},
                "agent": {"harness": "Claude Code", "model": "claude-opus-5-5", "protocol": "pilot-13"},
                "runner": {"platform": "GitHub Actions", "url": "https://github.com/catalystneuro/encore/actions/runs/42405983796"}},
 "outcomes": outcomes,
 "findings": findings,
}
out = yaml.safe_dump(rec, sort_keys=False, width=100, allow_unicode=True)
open("attempts/crcns-alm-3-li-2016-01.yaml", "w").write(out)
import re
bad = [l for l in out.splitlines() if re.search(r"^\s*(- )?\w+: [^'\"].*: ", l)]
print("lines with colon-space in plain scalars:", bad[:5])
PYEOF
python3 $TMPDIR/dev/attempt.py && python3 tools/entry.py check entries/crcns-alm-3-li-2016 2>&1 | tail -5
```

```
lines with colon-space in plain scalars: []
0 error(s)
```

**Agent calls Bash**

```bash
cd  grep -n -i "rather\|—" attempts/crcns-alm-3-li-2016-01.yaml entries/crcns-alm-3-li-2016/*.py $TMPDIR/dev/*.md $TMPDIR/dev/nb.py | head; grep -c "" attempts/crcns-alm-3-li-2016-01.yaml
```

```
499
```

**Agent calls Bash**

```bash
cat > entries/crcns-alm-3-li-2016/README.md <<'EOF'
# Li, Daie, Svoboda & Druckmann (2016) from CRCNS alm-3

Tests the findings of [Li et al. (2016)](https://doi.org/10.1038/nature17643) that can be tested
on CRCNS data set [alm-3](https://doi.org/10.6080/K0RB72JW), which holds the sorted single units,
trial tables, photostimulus types and lick and laser traces of 91 recording sessions from 19 mice:
unilateral photoinhibition (Experiment 1), bilateral experiments (Experiments 2 and 3) and
callosotomy. CRCNS data sets are not versioned; the files are streamed from the public bucket and
their MD5 sums printed in the notebook.

| Claim | Outcome |
|---|---|
| Unit and session counts | Not reproduced (FS count 89 against 72; the other counts exact) |
| Selective fraction of pyramidal neurons (ED Fig. 1) | Reproduced |
| Earlier photoinhibition has minimal behavioural effect (Fig. 1d) | Reproduced |
| Photoinhibition silences more than 90% of activity (ED Fig. 2b) | Reproduced |
| No rebound after photoinhibition (ED Fig. 2e) | Partially reproduced |
| Rate recovery in 90% of neurons (Fig. 1f) | Partially reproduced |
| Selectivity recovery times after unilateral photoinhibition (Fig. 1g) | Reproduced |
| Decreasing neurons return to their trajectory (ED Fig. 4) | Not reproduced |
| Behaviour under unilateral and bilateral photoinhibition (Fig. 2b) | Partially reproduced |
| Bilateral bias follows the cd trajectory (ED Fig. 6) | Reproduced |
| Recovery after ipsilateral, contralateral and bilateral photoinhibition (Fig. 2) | Partially reproduced |
| Experiment 3 recovery (ED Fig. 7d) | Partially reproduced |
| Experiment 3 cd ROC (ED Fig. 7e) | Partially reproduced |
| cd ROC at the end of the delay (Fig. 3) | Partially reproduced |
| cd ROC during photoinhibition (ED Fig. 8) | Reproduced |
| Stability of the coding direction (ED Fig. 9b) | Reproduced |
| Variance and selectivity captured by the modes (ED Fig. 8a) | Not reproduced |
| cd predicts the movement trial by trial (Fig. 3, 4) | Reproduced |
| Persistent and ramping modes (Fig. 3d, e) | Not reproduced |
| Callosotomy behaviour (Fig. 5b) | Partially reproduced (after the cut only) |
| Callosotomy recovery (Fig. 5) | Reproduced |
| Callosotomy preparatory activity (ED Fig. 10) | Partially reproduced |
| Monolithic models fail to recover (ED Fig. 1) | Partially reproduced (three of five models simulated) |
| Modular models are robust (Fig. 6) | Partially reproduced |
| Late-delay bias, recovery interval, spatial extent, photoactivation (Fig. 1d, ED Fig. 2d, 3, 5) | Blocked: data missing |
| Reaction time and distance from the boundary (ED Fig. 9f) | Blocked: data missing (no licks in the Experiment 2 lick traces) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Method details the claims file leaves open are taken from the Methods and, where those leave them
open, from the authors' MATLAB analysis scripts deposited in the data set. The attempt record, with
the reasons and the differences from the paper's method, is
[`attempts/crcns-alm-3-li-2016-01.yaml`](../../attempts/crcns-alm-3-li-2016-01.yaml).

- `reproduce_li_2016.ipynb`: the analysis. It takes about four minutes, most of it streaming the
  12 GB of session files.
- `alm3.py`: streaming and reducing the session files, trial selection, spike counts, the rate
  test, selectivity recovery and the population analyses. Other notebooks on this data set can
  import it.
- `models.py`: the network models of the Methods.
EOF
cd  && python3 tools/entry.py check entries/crcns-alm-3-li-2016 | tail -2; date -u
```

```
0 error(s)
Sat Nov  7 20:22:20 UTC 2026
```

**Agent calls Bash**

```bash
sed -i 's/  runtime_minutes: 8/  runtime_minutes: 4/' entries/crcns-alm-3-li-2016/entry.yaml && cd entries/crcns-alm-3-li-2016 && python3 - <<'EOF'
p='alm3.py'; s=open(p).read()
s=s.replace('''    "half", one random half of each type (M6 reading a).''','''    "half", one random half of each type (M6 reading a); split = "loo", every control trial is both
    a training and a test trial, and the analysis leaves the test trial out of the training set
    (M6 reading b).''')
s=s.replace('''        n_t = n_test if split == "code" else len(g) // 2
        test[d], train[d] = g[len(g) - n_t:], g[:len(g) - n_t]''','''        if split == "loo":
            test[d], train[d] = g, g
            continue
        n_t = n_test if split == "code" else len(g) // 2
        test[d], train[d] = g[len(g) - n_t:], g[:len(g) - n_t]''')
s=s.replace('''    return {"session": s["name"], "mouse": s["mouse"], "X": X,''','''    return {"session": s["name"], "mouse": s["mouse"], "X": X, "split": split,''')
open(p,'w').write(s)
EOF
cd $TMPDIR/dev && python3 - <<'EOF'
s=open('nb.py').read()
# LOO projections
s=s.replace('''def session_rocs(P, proj, conds, t_index=I_LATE, average=None):''','''def cd_projections_loo(P, win_reading="inside"):
    """Leave-one-out projections (M6 reading b): each control trial is projected on a cd and a
    boundary computed without it; photoinhibition trials on the cd of all correct control trials."""
    X = P["X"]
    hit = P["hit"]
    win = cd_windows(win_reading)
    tR = P["train"][1][hit[P["train"][1]]]
    tL = P["train"][-1][hit[P["train"][-1]]]
    proj, w, _ = cd_projections(P, "meandiff", win_reading)
    mR = X[tR][:, :, win].mean(axis=(0, 2)) * len(tR)
    mL = X[tL][:, :, win].mean(axis=(0, 2)) * len(tL)
    xi_win = X[:, :, win].mean(2)
    for i in np.r_[P["test"][1], P["test"][-1]]:
        r_, l_ = tR, tL
        sR, sL = mR, mL
        if i in set(tR):
            r_ = tR[tR != i]
            sR = mR - xi_win[i]
        elif i in set(tL):
            l_ = tL[tL != i]
            sL = mL - xi_win[i]
        wi = sR / len(r_) - sL / len(l_)
        wi /= np.linalg.norm(wi)
        b = alm3.boundary(X[r_][:, :, I_LATE] @ wi, X[l_][:, :, I_LATE] @ wi)
        proj[i] = X[i].T @ wi - b
    return proj

def session_rocs(P, proj, conds, t_index=I_LATE, average=None):''')
s=s.replace('''for exp, conds in (("exp2", [4, 5, 6]), ("exp3", [7, 8, 9]), ("ccx", [10, 11, 12])):
    for cells in ("pyramidal", "all"):
        for split in ("code", "half"):''','''for exp, conds in (("exp2", [4, 5, 6]), ("exp3", [7, 8, 9]), ("ccx", [10, 11, 12])):
    for cells in ("pyramidal", "all"):
        for split in ("code", "half", "loo"):''')
s=s.replace('''        for kind, wr in kinds:
            R = []
            for P in pops:
                proj, w, _ = cd_projections(P, kind, wr)
                R.append(session_rocs(P, proj, conds, **kw))''','''        for kind, wr in kinds:
            if split == "loo" and kind != "meandiff":
                continue
            R = []
            for P in pops:
                proj = cd_projections_loo(P, wr) if split == "loo" else cd_projections(P, kind, wr)[0]
                R.append(session_rocs(P, proj, conds, **kw))''')
open('nb.py','w').write(s)
EOF
grep -n 'POP\[("exp2", cells, "code")\]\|POP.items()' $TMPDIR/dev/nb.py | head -20
```

```
908:for k, v in POP.items():
927:    for (e, cells, split), pops in POP.items():
1011:for (e, cells, split), pops in POP.items():
1083:    pops = POP[("exp2", cells, "code")]
1152:    dfp = pooled_projections(POP[("exp2", cells, "code")], [4, 5, 6])
1186:    pops = POP[("exp2", cells, "code")]
1222:    for P in POP[("exp2", cells, "code")]:
1256:    R2c = pd.DataFrame([session_rocs(P, cd_projections(P)[0], [4, 5, 6]) for P in POP[("exp2", cells, "code")]])
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev && . ../v/bin/activate && python run.py nb.py "SANITY" "SETUP7" "def roc_table" "exp8 = " "rt7 = roc_table" "rt5 = roc_table" 2>&1 | grep -i "loo\|Error\|Trace" | head -40
```

```
Sessions with correct trials: 90 ; sessions whose first threshold crossing after the cue looks like a lick (median > 50 ms, < 20% within 20 ms): 42
            sessions  trace_range  median_first_lick_s
Trace length after the cue (s), median over sessions: 1.427
('exp2', 'pyramidal', 'loo') sessions 16 mice 7 neurons 175
('exp2', 'all', 'loo') sessions 17 mice 7 neurons 211
('exp3', 'pyramidal', 'loo') sessions 4 mice 3 neurons 48
('exp3', 'all', 'loo') sessions 5 mice 3 neurons 58
('ccx', 'pyramidal', 'loo') sessions 16 mice 7 neurons 259
('ccx', 'all', 'loo') sessions 17 mice 7 neurons 290
pyramidal   loo meandiff/inside        16  0.731  0.025  0.713  0.023  0.742  0.033  0.592  0.033        True   True
pyramidal   loo meandiff/centre        16  0.733  0.025  0.712  0.022  0.749  0.032  0.593  0.034        True   True
      all   loo meandiff/inside        17  0.743  0.023  0.675  0.025  0.744  0.037  0.585  0.026       False  False
      all   loo meandiff/centre        17  0.745  0.023  0.673  0.027  0.752  0.035  0.586  0.026       False  False--- cell 44 3.4s
 (a) 400 ms ending at ramp start pyramidal   loo meandiff/inside        16  0.686  0.021  0.520  0.035  0.620  0.030  0.483  0.017       False
 (a) 400 ms ending at ramp start pyramidal   loo meandiff/centre        16  0.688  0.022  0.527  0.036  0.624  0.030  0.478  0.017       False
 (a) 400 ms ending at ramp start       all   loo meandiff/inside        17  0.684  0.022  0.544  0.044  0.625  0.034  0.498  0.027       False
 (a) 400 ms ending at ramp start       all   loo meandiff/centre        17  0.685  0.022  0.526  0.044  0.630  0.034  0.509  0.024       False
(b) average over photoinhibition pyramidal   loo meandiff/inside        16  0.694  0.022  0.596  0.041  0.618  0.030  0.510  0.019       False
(b) average over photoinhibition pyramidal   loo meandiff/centre        16  0.695  0.023  0.595  0.041  0.619  0.030  0.506  0.018       False
(b) average over photoinhibition       all   loo meandiff/i
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev && python3 - <<'EOF'
s=open('nb.py').read()
old='''rows = []
for cells in ("pyramidal", "all"):
    pops = POP[("exp2", cells, "code")]
    for kind in ("meandiff", "lda"):'''
new='''rows = []
for cells, split in [(c, sp) for c in ("pyramidal", "all") for sp in ("code", "half", "loo")]:
    pops = POP[("exp2", cells, split)]
    for kind in ("meandiff", "lda"):'''
assert old in s; s=s.replace(old,new)
s=s.replace('''                r = {"cells": cells, "cd": kind, "baseline": baseline, "share": share, "sessions": len(v)}''','''                r = {"cells": cells, "split": split, "cd": kind, "baseline": baseline, "share": share, "sessions": len(v)}''')
s=s.replace('''# code). Total variance and selectivity: the squared norm over the full neuron space (code). cd
# as the mean difference (Methods) or LDA (code).''','''# code). Total variance and selectivity: the squared norm over the full neuron space (code). cd
# as the mean difference (Methods) or LDA (code). The shares use only the training trials, so the
# leave-one-out split (M6 b) amounts to using all control trials.''')
old2='''for cells in ("pyramidal", "all"):
    pops = POP[("exp2", cells, "code")]
    print(f"Neurons: {cells}")
    for mi, name in'''
new2='''for cells, split in (("pyramidal", "code"), ("all", "code"), ("pyramidal", "half"), ("all", "half")):
    pops = POP[("exp2", cells, split)]
    print(f"Neurons: {cells}, split: {split}")
    for mi, name in'''
assert old2 in s; s=s.replace(old2,new2)
s=s.replace('''# the control projection over sessions, persistent-mode projection outside it for ipsilateral.''','''# the control projection over sessions, persistent-mode projection outside it for ipsilateral.
# Splits: the code's and random halves (M6 a); the leave-one-out split (M6 b) is not run here, as
# it needs all five modes recomputed for every control trial.''')
open('nb.py','w').write(s)
EOF
cd $TMPDIR/dev && . ../v/bin/activate && python run.py nb.py "SANITY" "SETUP7" "def roc_table" "rows = []\nfor cells, split in" "def mode_projection" 2>&1 | grep -v "^---" | sed -n '/ed8a\|cells split/,$p' | grep -v "^('" | tail -60
```

```
cells split              cd  sessions  roc_0  sem_0  roc_4  sem_4  roc_5  sem_5  roc_6  sem_6  all_within  order
pyramidal  code meandiff/inside        16  0.719  0.033  0.706  0.024  0.738  0.033  0.595  0.036       False   True
pyramidal  code meandiff/centre        16  0.723  0.035  0.710  0.023  0.744  0.032  0.597  0.036       False   True
pyramidal  code      lda/inside        16  0.721  0.030  0.710  0.024  0.745  0.033  0.584  0.035       False   True
pyramidal  half meandiff/inside        16  0.716  0.030  0.702  0.030  0.684  0.039  0.596  0.036       False  False
pyramidal  half meandiff/centre        16  0.721  0.030  0.705  0.029  0.683  0.039  0.596  0.037       False  False
pyramidal  half      lda/inside        16  0.718  0.030  0.705  0.032  0.683  0.039  0.595  0.037       False  False
pyramidal   loo meandiff/inside        16  0.731  0.025  0.713  0.023  0.742  0.033  0.592  0.033        True   True
pyramidal   loo meandiff/centre        16  0.733  0.025  0.712  0.022  0.749  0.032  0.593  0.034        True   True
      all  code meandiff/inside        17  0.740  0.028  0.672  0.027  0.745  0.035  0.587  0.026       False  False
      all  code meandiff/centre        17  0.746  0.029  0.671  0.028  0.754  0.035  0.587  0.026       False  False
      all  code      lda/inside        17  0.735  0.028  0.678  0.024  0.742  0.037  0.574  0.025       False   True
      all  half meandiff/inside        17  0.731  0.027  0.667  0.034  0.703  0.039  0.587  0.027       False  False
      all  half meandiff/centre        17  0.729  0.028  0.668  0.035  0.707  0.037  0.588  0.027       False  False
      all  half      lda/inside        17  0.723  0.026  0.681  0.033  0.702  0.042  0.578  0.026       False   True
      all   loo meandiff/inside        17  0.743  0.023  0.675  0.025  0.744  0.037  0.585  0.026       False  False
      all   loo meandiff/centre        17  0.745  0.023  0.673  0.027  0.752  0.035  0.586  0.026       False  False--- cell 44 3.5s
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev && . ../v/bin/activate && python run.py nb.py "SANITY" "SETUP7" "def roc_table" "def gram_schmidt" "def pooled_projections" "def mode_projection" 2>&1 | grep -v "^---" | sed -n '/^    cells     split/,$p' | grep -v "^('" | head -80
```

```
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev && . ../v/bin/activate && python run.py nb.py "SANITY" "SETUP7" "def roc_table" "def gram_schmidt" "def pooled_projections" "def mode_projection" > o3.txt 2>&1; grep -n "Traceback\|Error" o3.txt | head; grep -A40 "share  sessions" o3.txt | head -42; grep -A3 "Neurons: .*split" o3.txt
```

```
cells split       cd baseline   share  sessions  sel_cd  sel_cd_sem  var_cd  var_cd_sem  var_1_5  var_1_5_sem  sel_1_5  sel_1_5_sem  all_within  cd_within
pyramidal  code meandiff      pre squared        16    72.5         3.6    39.5         6.2     97.1          0.6     93.9          1.2       False      False
pyramidal  code meandiff      pre     rms        16    84.7         2.2    60.3         4.6     98.5          0.3     96.9          0.6       False      False
pyramidal  code meandiff    trial squared        16    72.5         3.6    40.7         5.6     95.5          0.9     93.7          1.4       False      False
pyramidal  code meandiff    trial     rms        16    84.7         2.2    61.7         4.2     97.7          0.5     96.8          0.7       False      False
pyramidal  code      lda      pre squared        16    66.1         4.1    36.6         5.9     96.9          0.7     93.4          1.4       False       True
pyramidal  code      lda      pre     rms        16    80.7         2.5    57.8         4.6     98.4          0.3     96.6          0.7       False      False
pyramidal  code      lda    trial squared        16    66.1         4.1    37.6         5.5     95.2          1.0     93.0          1.6       False       True
pyramidal  code      lda    trial     rms        16    80.7         2.5    59.0         4.3     97.6          0.5     96.4          0.9       False      False
pyramidal  half meandiff      pre squared        16    67.1         4.4    39.9         5.9     96.3          0.8     92.5          1.7       False       True
pyramidal  half meandiff      pre     rms        16    81.2         2.7    61.0         4.3     98.1          0.4     96.1          0.9       False      False
pyramidal  half meandiff    trial squared        16    67.1         4.4    41.3         5.7     94.7          1.0     92.4          1.8       False       True
pyramidal  half meandiff    trial     rms        16    81.2         2.7    62.0         4.4     
[... 45 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev && python3 - <<'EOF'
s=open('results.md').read()
a=s.index("### fig3-cd-roc"); b=s.index("### ed8-roc-during")
s=s[:a]+'''### fig3-cd-roc
**Result: reproduced.** The session rule gives the paper's 16 sessions from 7 mice. With the leave-one-out split of control trials (M6 reading b), the mean-difference cd and pyramidal neurons, the end-of-delay ROC is 0.731 +- 0.025 (control), 0.713 +- 0.023 (ipsilateral), 0.742 +- 0.033 (contralateral) and 0.592 +- 0.033 (bilateral), all within the paper's 0.76 +- 0.03, 0.73 +- 0.02, 0.74 +- 0.03 and 0.58 +- 0.03; windows centred in the epochs give the same. With the code's split the control and ipsilateral values fall just below tolerance (0.719 and 0.706), and with random halves the contralateral value is 0.684; with all units the ipsilateral value is 0.672 to 0.681 in every split.

'''+s[b:]
a=s.index("### ed8a-mode-variance"); b=s.index("### fig3-cd-predicts-movement")
s=s[:a]+'''### ed8a-mode-variance
**Result: partially reproduced.** With the mean-difference cd of the Methods and random halves of the control trials (M6 reading a), cd captures 67.1% of the selectivity and 39.9% of the variance (pyramidal neurons, pre-sample baseline, squared-norm shares), both within the paper's 65.6 +- 5.1% and 36.4 +- 6.3%. Modes 1 to 5 capture 96.3% of the variance and 92.5% of the selectivity, outside 98.5 +- 0.5% and 95.8 +- 1.2%; no reading puts all four values within tolerance. With the code's split the cd selectivity share is 72.5%, outside; with the code's discriminant as cd it is 66.1%.

'''+s[b:]
open('results.md','w').write(s)
s=open('summary.md').read()
s=s.replace("| fig3-cd-roc | partially reproduced |","| fig3-cd-roc | reproduced |")
s=s.replace("| ed8a-mode-variance | not reproduced |","| ed8a-mode-variance | partially reproduced |")
open('summary.md','w').write(s)
EOF
python3 - <<'EOF'
p='entries/crcns-alm-3-li-2016/README.md'
s=open(p).read()
s=s.replace("| cd ROC at the end of the delay (Fig. 3) | Partially reproduced |","| cd ROC at the end of the delay (Fig. 3) | Reproduced |")
s=s.replace("| Variance and selectivity captured by the modes (ED Fig. 8a) | Not reproduced |","| Variance and selectivity captured by the modes (ED Fig. 8a) | Partially reproduced |")
open(p,'w').write(s)
EOF
cd $TMPDIR/dev && python3 - <<'EOF'
s=open('attempt.py').read()
a=s.index('o("fig3-cd-roc"'); b=s.index('o("ed8-roc-during-photoinhibition"')
s=s[:a]+'''o("fig3-cd-roc", "reproduced",
  "The session rule of the deposited script (pyramidal neurons stable at trial 50 and 50 before the "
  "end, more than 5 neurons, at least 5 trials per group) gives the paper's 16 sessions from 7 mice "
  "(175 neurons). Leave-one-out split (M6 reading b), mean-difference cd, pyramidal neurons: ROC "
  "0.731 +- 0.025 (control), 0.713 +- 0.023 (ipsilateral), 0.742 +- 0.033 (contralateral), 0.592 +- "
  "0.033 (bilateral), all within tolerance; windows centred in the epochs give 0.733, 0.712, 0.749, "
  "0.593. Other readings miss: the code's split gives 0.719 and 0.706 for control and ipsilateral, just "
  "below tolerance; random halves give a contralateral 0.684; all units give an ipsilateral 0.667 to "
  "0.681. Control, ipsilateral and contralateral exceed bilateral by more than 0.1 in the matching "
  "reading.",
  ["cd is the mean difference of the Methods; the deposited script's linear discriminant is shown as a "
   "variant with the code's split and random halves (not with leave-one-out).",
   "The reproduced outcome rests on one of the criterion's readings (leave-one-out, pyramidal "
   "neurons); the control and ipsilateral values lie near the edge of their tolerance in all readings."],
  [16, 0.731, 0.713, 0.742, 0.592]),
'''+s[b:]
a=s.index('o("ed8a-mode-variance"'); b=s.index('o("fig3-cd-predicts-movement"')
s=s[:a]+'''o("ed8a-mode-variance", "partially_reproduced",
  "Mean-difference cd (Methods), random halves of the control trials (M6 reading a), pyramidal "
  "neurons, pre-sample baseline, squared-norm shares (the script's): selectivity on cd 67.1% (paper "
  "65.6 +- 5.1), variance on cd 39.9% (36.4 +- 6.3), both within tolerance; modes 1 to 5 variance 96.3% "
  "(98.5 +- 0.5) and selectivity 92.5% (95.8 +- 1.2), outside. No reading puts all four within "
  "tolerance. With the code's split the cd selectivity share is 72.5% and with leave-one-out (all "
  "control trials) 74.7%, outside; RMS shares give cd values near 81% and 61%, outside, and mode 1 to 5 "
  "values near 98% and 96%. With the script's discriminant cd and its split, 66.1% and 36.6%.",
  ["Modes, baseline (the window 3.4 to 3.0 s before the cue) and the squared-norm shares from the "
   "deposited script (analysis_compile_all_data_bilateral_activityModes.m, ED Fig. 8 sections), with "
   "the mean-difference cd of the Methods; the script's discriminant cd is a variant. The modes are "
   "fully Gram-Schmidt orthogonalized (Methods); the script orthogonalizes the persistent modes "
   "against the singular vectors only. The shares use only training trials, so leave-one-out amounts to "
   "using all control trials."],
  [67.1, 39.9, 96.3, 92.5]),
'''+s[b:]
s=s.replace('''  ["Modes from ed8a-mode-variance with the mean-difference cd."]),''','''  ["Modes from ed8a-mode-variance with the mean-difference cd; the code's split and random halves are "
   "run, the leave-one-out split is not (it needs all modes recomputed for every control trial). With "
   "random halves both modes still predict the lick above chance (p = 1e-05 and 0.002)."]),''')
open('attempt.py','w').write(s)
EOF
python3 $TMPDIR/dev/attempt.py && python3 $TMPDIR/dev/convert.py $TMPDIR/dev/nb.py $TMPDIR/dev/header.md $TMPDIR/dev/summary.md $TMPDIR/dev/results.md entries/crcns-alm-3-li-2016/reproduce_li_2016.ipynb; date -u
```

```
lines with colon-space in plain scalars: []
claims without a result: set()
cells 93
Sat Nov  7 20:25:22 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
sed -i 's/with all units the ipsilateral value is 0.672 to 0.681 in every split/with all units the ipsilateral value is 0.667 to 0.681 in every split/' $TMPDIR/dev/results.md && python3 $TMPDIR/dev/convert.py $TMPDIR/dev/nb.py $TMPDIR/dev/header.md $TMPDIR/dev/summary.md $TMPDIR/dev/results.md entries/crcns-alm-3-li-2016/reproduce_li_2016.ipynb && python3 tools/entry.py lock entries/crcns-alm-3-li-2016 | tail -1 && python3 tools/entry.py all entries/crcns-alm-3-li-2016 2>&1 | tail -3; date -u
```

```
claims without a result: set()
cells 93
wrote entries/crcns-alm-3-li-2016/requirements.lock.txt
Installed kernelspec registry-crcns-alm-3-li-2016 in executed/crcns-alm-3-li-2016/.venv/share/jupyter/kernels/registry-crcns-alm-3-li-2016
0 error(s)
pass  reproduce_li_2016.ipynb  (262 s)
Sat Nov  7 20:29:59 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'EOF' > $TMPDIR/out3.txt
import nbformat
nb=nbformat.read('executed/crcns-alm-3-li-2016/reproduce_li_2016.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    txt=''.join(o.get('text','') for o in c.outputs if o.output_type=='stream')
    err=[o for o in c.outputs if o.output_type=='error']
    print(f'=== cell {c.metadata.get("tags",[])}', 'ERROR' if err else ''); print(txt)
EOF
grep -c ERROR $TMPDIR/out3.txt; grep "loo meandiff/inside        16\|half meandiff      pre squared" $TMPDIR/out3.txt; grep "loaded" $TMPDIR/out3.txt
```

```
0
pyramidal   loo meandiff/inside        16  0.731  0.025  0.713  0.023  0.742  0.033  0.592  0.033        True   True
 (a) 400 ms ending at ramp start pyramidal   loo meandiff/inside        16  0.686  0.021  0.520  0.035  0.620  0.030  0.483  0.017       False
(b) average over photoinhibition pyramidal   loo meandiff/inside        16  0.694  0.022  0.596  0.041  0.618  0.030  0.510  0.019       False
pyramidal  half meandiff      pre squared        16    67.1         4.4    39.9         5.9     96.3          0.8     92.5          1.7       False       True
      all  half meandiff      pre squared        17    68.2         4.1    42.6         5.3     96.7          0.6     91.9          1.7       False       True
pyramidal   loo meandiff/inside        16  0.711  0.039   0.574   0.035   0.673   0.042   0.547   0.038
loaded 91 sessions and 1579 units in 167 s
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev && python3 - <<'EOF'
s=open('nb.py').read()
s=s.replace('''print(f"loaded {len(sessions)} sessions and {len(units)} units in {time.time() - started:.0f} s")''','''import resource
print(f"loaded {len(sessions)} sessions and {len(units)} units in {time.time() - started:.0f} s; "
      f"peak memory of this process {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB "
      f"(each of the 3 loading processes holds one session file, about 1.5 GB at most)")''')
open('nb.py','w').write(s)
EOF
python3 $TMPDIR/dev/convert.py $TMPDIR/dev/nb.py $TMPDIR/dev/header.md $TMPDIR/dev/summary.md $TMPDIR/dev/results.md entries/crcns-alm-3-li-2016/reproduce_li_2016.ipynb && python3 tools/entry.py all entries/crcns-alm-3-li-2016 2>&1 | tail -2 && python3 tools/entry.py handover entries/crcns-alm-3-li-2016 2>&1 | tail -2; ls executed/crcns-alm-3-li-2016/handover/; date -u
```

```
claims without a result: set()
cells 93
python3: can't open file '/tmp/claude-1001/dev/tools/entry.py': [Errno 2] No such file or directory
python3: can't open file '/tmp/claude-1001/dev/tools/entry.py': [Errno 2] No such file or directory
ls: cannot access 'executed/crcns-alm-3-li-2016/handover/': No such file or directory
Sat Nov  7 20:30:14 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
python3 tools/entry.py all entries/crcns-alm-3-li-2016 2>&1 | tail -2 && python3 tools/entry.py handover entries/crcns-alm-3-li-2016 2>&1 | tail -2; ls executed/crcns-alm-3-li-2016/handover/; date -u
```

```
0 error(s)
pass  reproduce_li_2016.ipynb  (226 s)
wrote executed/crcns-alm-3-li-2016/handover
10.1038-nature17643.yaml
alm3.py
models.py
reproduce_li_2016.ipynb
Sat Nov  7 20:34:20 UTC 2026
```

**Agent calls Bash**

```bash
python3 -c "
import nbformat
nb=nbformat.read('executed/crcns-alm-3-li-2016/handover/reproduce_li_2016.ipynb',4)
print(len(nb.cells), sum(1 for c in nb.cells if c.cell_type=='markdown' and c.source.startswith('**Result')), any(c.source.startswith('## Summary') for c in nb.cells))
nb=nbformat.read('executed/crcns-alm-3-li-2016/reproduce_li_2016.ipynb',4)
print([''.join(o.get('text','') for o in c.outputs) for c in nb.cells if c.cell_type=='code'][1])
"; git status --short
```

```
67 0 False
loaded 91 sessions and 1579 units in 127 s; peak memory of this process 0.59 GB (each of the 3 loading processes holds one session file, about 1.5 GB at most)

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
?? attempts/crcns-alm-3-li-2016-01.yaml
?? entries/crcns-alm-3-li-2016/
?? scripts
```

**Agent calls Bash**

```bash
sed -n 1,40p attempts/crcns-alm-3-li-2016-01.yaml; grep -n "outcome:" attempts/crcns-alm-3-li-2016-01.yaml | awk '{print $3}' | sort | uniq -c
```

```
schema_version: 2
id: crcns-alm-3-li-2016-01
dataset:
  archive: crcns
  id: alm-3
  version: unversioned
  doi: 10.6080/K0RB72JW
paper: doi:10.1038/nature17643
date: '2026-11-07'
entry: crcns-alm-3-li-2016
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
[... 24 more lines not kept]
```

**Agent**

I've finished steps 1 to 6 of the Author section for CRCNS alm-3 against Li et al. (2016). The entry passes `tools/entry.py all` (0 check errors; the notebook runs in about 4 minutes) and the handover package is built. Nothing is committed.

## 1. Outcomes (29 claims)

| Claim | Outcome |
|---|---|
| units-and-sessions | not reproduced: 1012 units, 20 + 38 sessions, 12 mice and 890 pyramidal all match exactly, but 89 FS against the paper's 72 |
| ed1-selective-fraction | reproduced (633 / 176 / 336 / 493 against 634 / 176 / 337 / 493, correct trials only) |
| fig1d-late-delay-ipsilateral-bias | blocked: data_missing |
| fig1d-earlier-photoinhibition-minimal | reproduced (p = 0.23 and 0.22; only 4 mice, recording sessions) |
| ed3-recovery-interval | blocked: data_missing |
| ed2b-silencing | reproduced |
| ed2d-spatial-extent | blocked: data_missing |
| ed2e-no-rebound | partially reproduced: no rebound on average, but more neurons excited (24) than suppressed (9) |
| fig1f-rate-recovery | partially reproduced (exactly 168 / 168 / 175 neurons; fractions 9 to 20%) |
| fig1g-selectivity-recovery | reproduced (347, 420, 236 ms) |
| ed4-return-to-trajectory | not reproduced |
| ed5-photoactivation | blocked: data_missing |
| fig2b-bilateral-behaviour | partially reproduced |
| ed6-bilateral-bias-inconsistent | reproduced (under the criterion's second reading only) |
| fig2-bilateral-recovery | partially reproduced: ipsilateral selectivity reaches 80% before the cue in only 25% of bootstrap resamples |
| ed7-unilateral-4-spots-bilateral-1-spot | partially reproduced: bilateral 1-spot selectivity recovers in 80% of resamples, where the paper says it does not |
| ed7e-size-and-roc | partially reproduced |
| fig3-cd-roc | reproduced (exactly 16 sessions; only under the leave-one-out reading) |
| ed8-roc-during-photoinhibition | reproduced (3 of 24 readings match) |
| ed9b-cd-stability | reproduced |
| ed8a-mode-variance | partially reproduced |
| fig3-cd-predicts-movement | reproduced |
| fig3-other-modes | not reproduced |
| ed9f-reaction-time | blocked: data_missing (no licks in the Experiment 2 lick traces) |
| fig5b-callosotomy-behaviour | partially reproduced (only after-cut sessions exist) |
| fig5-callosotomy-recovery | reproduced |
| ed10e-callosotomy-preparatory-activity | partially reproduced |
| models-monolithic-fail | partially reproduced (3 of 5 models simulated; marked assumed) |
| fig6-modular-models-robust | partially reproduced (attractor works; the printed integrator matrix recovers lick-right trials only; marked assumed) |

Totals: 10 reproduced, 11 partially reproduced, 3 not reproduced, 5 blocked.

## 2. Dataset, assumptions and questions

**What the dataset holds.** 91 sessions from 19 mice, and the trial tables and laser timing match the description. The authors' MATLAB scripts in the dataset reproduce several of the paper's counts exactly.

**Findings recorded:**
- **FS labels:** 89 units are labelled FS against the paper's 72, and the labels don't follow the waveform widths.
- **Missing `depth` field:** the description lists one; the files have none.
- **Type 9 mislabelled:** still described as "ipsilateral"; the FAQ says contralateral.
- **Lick trace:** shows no licks in 48 of 90 sessions, including all 26 Experiment 2 sessions.
- **No silencing in four sessions:** photoinhibition doesn't reduce activity there, so the spike/laser/trial clock can't be confirmed for them.
- **Session with no performing trials:** ANM270340_20150618.
- **Experiment not labelled:** nothing says which experiment a session belongs to, and six sessions hold a condition mix the Methods don't describe.
- **Not deposited:** the behaviour-only sessions, photoactivation data, untrained-mouse recordings, pre-callosotomy sessions and the simulations named in the title.
- **Scripts against Methods:** the deposited scripts disagree with the Methods. cd is a Fisher discriminant there, not the mean difference. The selectivity test uses correct plus error trials, yet the paper's counts match correct trials only.

**Version.** CRCNS has no versions, so I pinned the `live/` copy as `unversioned`. The notebook header says why and prints the MD5 sums of the files read.

**Assumptions** (outcomes marked `assumed: true`):
- fig6: noise variance taken per integration step, and the inter-module partner taken to share its neuron's preference.
- models-monolithic-fail: the simple integrator is a random rank-one matrix, and the FORCE network uses standard choices for target, feedback and update rate.

**Questions for the paper's authors** (one `methods_unavailable` finding):
1. Is the Fig. 6b noise variance per step?
2. Is the Fig. 6c matrix complete? As printed, lick-left trials don't recover.
3. ED Fig. 4 has 6 mice, but Experiment 1 has 4. Which sessions were used?
4. How were bootstrap resamples that never recover counted in Fig. 2e?

**Questions to a reader:** none.

## 3. Protocol gaps

1. **Code in the dataset, not linked by the paper.** The protocol only covers "code it links". I treated the deposited scripts as the paper's code, Methods first, and recorded each use.
2. **Readers can't see dataset files,** so the claims file was written without those scripts. Reader and author then work from different method sources (cd definition, trial sets).
3. **Every reading must be run, and any match counts.** Readings multiply into large grids, and one reading moved fig3-cd-roc from partial to reproduced. I ran the grids and reported how many readings match. The leave-one-out split for fig3-other-modes was not run because of its cost; I said so.
4. **Criteria without a partial rule** (ed2e, ed7, ed7e, ed10e, models). I used the protocol's general definition of partially reproduced.
5. **Claims that use no recorded data** (the simulations). It is unclear whether they should be tested. I tested them.
6. **`measured` when no reading matches** is not specified. I recorded the main reading (the script's, or the first listed).
7. **Peak memory:** `ru_maxrss` doesn't count worker processes. I printed the main process and stated the per-worker bound.
8. **"Use a pinned published version"** doesn't apply to CRCNS. I followed docs/archives.md.

## 4. Runtime and failures

- Work ran from about 19:24 to 20:35 UTC (about 1 h 10 min). The final notebook run took 226 s, with peak memory 0.59 GB in the main process.
- Two early notebook runs failed on cell ordering and were fixed; nothing is outstanding.
- Untracked dotfiles (`.bashrc`, `.gitconfig`, `.idea` and others) are at the repository root. I did not create them and left them alone; the workflow may pick them up when it commits.

Files are in `entries/crcns-alm-3-li-2016` and `attempts`:
- `reproduce_li_2016.ipynb`
- `alm3.py`
- `models.py`
- `entry.yaml`
- `README.md`
- `requirements.in`
- `requirements.lock.txt`
- `crcns-alm-3-li-2016-01.yaml`

## End of run

128 turns, 66 minutes, $13.22 at API prices, result: success.
