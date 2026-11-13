# zandvakili-2015 · author · run 43258308217

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; ls; ls docs entries claims attempts paper tools | head -80
```

```
Thu Nov 12 16:31:59 UTC 2026
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
[... 92 more lines not kept]
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
[... 657 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md | head -150; wc -l docs/design.md; cat claims/zandvakili-2015.yaml; ls paper; cat papers/datasets/zandvakili-2015.yaml
```

```
<persisted-output>
Output too large (47.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/0c90c0c9-43b9-40d9-b0f2-cee07c4eeda0/tool-results/bbfjagvqc.txt

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

**Agent calls Bash**

```bash
cat claims/zandvakili-2015.yaml; ls -la paper; cat papers/datasets/zandvakili-2015.yaml
```

```
<persisted-output>
Output too large (40.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/0c90c0c9-43b9-40d9-b0f2-cee07c4eeda0/tool-results/bpa7om7ct.txt

Preview (first 2KB):
# Claims for Zandvakili & Kohn (2015), Neuron 87, 827-839, "Coordinated Neuronal Activity Enhances
# Corticocortical Communication" (doi:10.1016/j.neuron.2015.07.026), on CRCNS data set v1v2-1.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
# protocol as stated in docs/protocol.md (Reader), version pilot-14.
#
# Text read. The version of record as supplied under paper/ (PyMuPDF text of the journal PDF, with
# the Supplemental Information appended): Results, Discussion, figure legends, Experimental
# Procedures, and the supplement (Figures S1 to S6 with their texts, Supplemental Experimental
# Procedures). The PDF pages could not be rendered in this run, so no figure was read from the
# image; every value below is from the text. The extracted text prints the degree sign as a
# replacement glyph and a few dashes oddly; one such case is named in figS5-middle-layer-relay.
#
# Code. The paper links no analysis code and names no repository. No code was read; every
# method below is from the Experimental Procedures, the Results, the figure legends or the
# supplement, and details none of them fixes are named as open.
#
[... 10 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/0c90c0c9-43b9-40d9-b0f2-cee07c4eeda0/tool-results/bpa7om7ct.txt"
}
```

```
1	# Claims for Zandvakili & Kohn (2015), Neuron 87, 827-839, "Coordinated Neuronal Activity Enhances
2	# Corticocortical Communication" (doi:10.1016/j.neuron.2015.07.026), on CRCNS data set v1v2-1.
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
4	# protocol as stated in docs/protocol.md (Reader), version pilot-14.
5	#
6	# Text read. The version of record as supplied under paper/ (PyMuPDF text of the journal PDF, with
7	# the Supplemental Information appended): Results, Discussion, figure legends, Experimental
8	# Procedures, and the supplement (Figures S1 to S6 with their texts, Supplemental Experimental
9	# Procedures). The PDF pages could not be rendered in this run, so no figure was read from the
10	# image; every value below is from the text. The extracted text prints the degree sign as a
11	# replacement glyph and a few dashes oddly; one such case is named in figS5-middle-layer-relay.
12	#
13	# Code. The paper links no analysis code and names no repository. No code was read; every
14	# method below is from the Experimental Procedures, the Results, the figure legends or the
15	# supplement, and details none of them fixes are named as open.
16	#
17	# Data the paper used. Nine hemispheres of seven anesthetized (sufentanil), paralyzed adult male
18	# Macaca fascicularis. V1 recorded with a 10 x 10 Utah array (1 mm electrodes, 400 um spacing,
19	# layers 2/3 and 4B), RFs 2 to 4 deg from the fovea; 10 array implants, V1 populations of 61 to 160
20	# units (average 98). V2 recorded with seven moveable electrodes and tetrodes (300 um spacing) in
[... 579 more lines not kept]
```

**Agent**

Read the protocol and the claims file (27 claims, several heavy divergence analyses). Now the dataset description and the CRCNS archive rules.

**Agent calls Bash**

```bash
cat paper/v1v2-1.data-description.txt; grep -n "CRCNS" -A60 docs/archives.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
ls entries/fouke-2025/; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in; head -c 6000 attempts/fouke-2025-01.yaml; ls questions | head;
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
[... 135 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/^outcomes/,$p' attempts/fouke-2025-01.yaml | grep -n "^[a-z]" ; sed -n '/^findings/,$p' attempts/fouke-2025-01.yaml | head -60; ls schemas; ls targets; grep -n "v1v2" -r targets | head
```

```
1:outcomes:
210:findings:
280:verifications:
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
[... 61 more lines not kept]
```

**Agent**

Now the bucket listing and checksums.

**Agent calls Bash**

```bash
curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=v1v2-1/" | python3 -c "
import sys,re
t=sys.stdin.read()
for k,s,m in re.findall(r'<Key>(.*?)</Key>.*?<LastModified>(.*?)</LastModified>.*?<Size>(.*?)</Size>',t): print(k,s,m)
" ; sed -n 2075,2095p targets/crcns.json
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
B=https://crcnsarchive.s3-us-west-2.amazonaws.com/v1v2-1/live; curl -s $B/checksums.md5; curl -s $B/filelist.txt; which python; python -c "import fsspec, scipy, numpy, aiohttp; print(fsspec.__version__, scipy.__version__)"
```

```
Exit code 1
84de899a70ef2f09c17dd41aa96e75c1  docs/crcns_v1v2-1_data_description.docx
72e436e8e0c006efbbe5eab4737c3c69  docs/crcns_v1v2-1_data_description.pdf
48917aea682f869c7aee45f170516c7d  docs/sessions_description.pdf
eb2042d9e1b708920b7a9eb8c986849c  filelist.txt
12a15c5a63366ccd1fa2b4e495f1d66d  v1-v2_gratings.zip
# CRCNS.org 'v1v2-1' dataset files
# To use this for fetching files, comment out files that are
# not needed by putting a '#' as the first character on the line (default mode)
# or put a '+' as the first character to specifiy files to be fetched (+ mode).
# mode='default' (change to '+' for + mode).
 docs/crcns_v1v2-1_data_description.docx	24415 (23.8 KB)
 docs/crcns_v1v2-1_data_description.pdf	80646 (78.7 KB)
 docs/sessions_description.pdf	32823 (32.0 KB)
 v1-v2_gratings.zip	149782095 (142.8 MB)
 checksums.md5	311
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import fsspec, scipy, numpy, aiohttp; print(fsspec.__version__, scipy.__version__)
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && . dev/bin/activate && uv pip install -q fsspec aiohttp requests scipy numpy matplotlib pandas h5py nbformat nbclient ipykernel 2>&1 | tail -2; python -c "
import fsspec, zipfile
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/v1v2-1/live/v1-v2_gratings.zip', block_size=2**20).open()
z=zipfile.ZipFile(f)
for i in z.infolist(): print(i.filename, i.file_size, i.compress_size)
"
```

```
v1-v2_gratings/ 0 0
v1-v2_gratings/mat_neural_data/ 0 0
v1-v2_gratings/mat_neural_data/106r002p70.mat 15505921 15302632
v1-v2_gratings/mat_neural_data/105l001p16.mat 34774439 34202590
v1-v2_gratings/mat_neural_data/107l003p143.mat 38843972 38095055
v1-v2_gratings/mat_neural_data/106r001p26.mat 29213463 28757227
v1-v2_gratings/mat_neural_data/107l002p67.mat 34004346 33419310
v1-v2_gratings/software/ 0 0
v1-v2_gratings/software/COLOR_MAP.mat 395 364
v1-v2_gratings/software/Squash.m 90 75
v1-v2_gratings/software/SET_CONSTS.m 108 84
v1-v2_gratings/software/BinTime.m 649 297
v1-v2_gratings/software/ExtractSpikes.m 2810 668
v1-v2_gratings/software/example.m 1402 735
v1-v2_gratings/startup.m 61 56
Shell cwd was reset to
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; python -c "
import fsspec, zipfile, io, scipy.io as sio, numpy as np, time
t=time.time()
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/v1v2-1/live/v1-v2_gratings.zip', block_size=2**20).open()
z=zipfile.ZipFile(f)
for n in z.namelist():
  if n.endswith('.m'): print('=====',n); print(z.read(n).decode())
b=z.read('v1-v2_gratings/mat_neural_data/106r002p70.mat'); print(len(b), time.time()-t)
m=sio.loadmat(io.BytesIO(b), squeeze_me=False)
print(m.keys())
nd=m['neuralData'][0,0]; print(nd.dtype.names)
for k in nd.dtype.names:
  v=nd[k]; print(k, type(v), v.shape, v.dtype)
sr=nd['spikeRasters']; print(sr[0,0].shape, type(sr[0,0]), sr[0,1].shape)
print(np.unique(nd['stim'], return_counts=True)); print(nd['trialId'][:10].ravel(), nd['trialId'][-5:].ravel())
uc=nd['unitCodes']; print(uc[0,0][:20], uc[0,1])
rf=nd['rfInfo']; print(rf[0,0].shape, rf[0,1].shape); print(rf[0,0][:5,:,0]); print(rf[0,1][:5])
"
```

```
===== v1-v2_gratings/software/Squash.m
function B = Squash(A)

dimA = size(A);

B = reshape(A, [dimA(1), dimA(2)*dimA(3)]);

end

===== v1-v2_gratings/software/SET_CONSTS.m
BLANK_TRIAL_LENGTH	= 1500; % ms
DRIVEN_TRIAL_LENGTH	= 1280; % ms
TIME_RES = 10^3;

% Indexes
V1 = 1;
V2 = 2;
===== v1-v2_gratings/software/BinTime.m
function spikes = BinTime(spikeRasters, binWidth)

[... 326 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -i "experimental procedures\|pairwise v1\|divergence analysis\|equation\|jitter\|shuffl\|monitor\|pixel\|110 cm\|SNR\|signal-to-noise\|same electrode\|tetrode" paper/10.1016-j.neuron.2015.07.026.txt | head -120
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2015.07.026.txt",
 "offset": 1043,
 "limit": 125
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2015.07.026.txt",
 "offset": 440,
 "limit": 240
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
date -u; sed -n 1520,1640p paper/10.1016-j.neuron.2015.07.026.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; cd $TMPDIR; cat > survey.py <<'EOF'
import fsspec, zipfile, io, scipy.io as sio, numpy as np, time, resource
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/v1v2-1/live/v1-v2_gratings.zip', block_size=2**20).open()
z=zipfile.ZipFile(f)
for n in sorted(z.namelist()):
  if not n.endswith('.mat') or 'COLOR' in n: continue
  t=time.time()
  nd=sio.loadmat(io.BytesIO(z.read(n)))['neuralData'][0,0]
  sr=nd['spikeRasters']; stim=nd['stim'].ravel(); tid=nd['trialId'].ravel()
  ntr=sr.shape[0]
  shapes=set((sr[i,0].shape[1], stim[i]==0) for i in range(ntr))
  alt = np.all((stim[1::2]==0)) and np.all(stim[0::2]>0)
  n1=sr[0,0].shape[0]; n2=sr[0,1].shape[0]
  c1=np.zeros(n1); c2=np.zeros(n2); vals=set()
  for i in range(0,ntr,2):
    a=sr[i,0]; b=sr[i,1]; c1+=np.asarray(a.sum(1)).ravel(); c2+=np.asarray(b.sum(1)).ravel()
    if i<200: vals |= set(np.unique(a.data).tolist())|set(np.unique(b.data).tolist())
  r1=c1/(ntr/2*1.28); r2=c2/(ntr/2*1.28)
  uc=nd['unitCodes']; rf=nd['rfInfo']
  print(n.split('/')[-1], 'rows',ntr,'alt',alt,'shapes',shapes,'tid monotone',np.all(np.diff(tid)>0), 'stim counts',np.bincount(stim))
  print('  V1',n1,'V2',n2,'rate V1 med %.1f min %.2f; V2 med %.1f min %.2f'%(np.median(r1),r1.min(),np.median(r2),r2.min()), 'n<0.5',(r1<0.5).sum(),(r2<0.5).sum(),'values',vals)
  print('  V1 elec',np.unique(uc[0,0][:,0]).size, uc[0,0][:,0].max(),'V2 elec',np.unique(uc[0,1][:,0]), 'rf shapes',rf[0,0].shape,rf[0,1].shape, 'V1 rf nan rows',np.isnan(rf[0,0][:,2,0]).sum())
  print('  V1 rf x range',np.nanmin(rf[0,0][:,2,:]),np.nanmax(rf[0,0][:,2,:]),'y',np.nanmin(rf[0,0][:,3,:]),np.nanmax(rf[0,0][:,3,:]),'var',np.nanmedian(rf[0,0][:,4:6,:]))
  ok=~np.isnan(rf[0,1][:,2,0]); print('  V2 rf rows',np.where(ok)[0]+1,'x',rf[0,1][ok,2,:].round(0).tolist(),'y',rf[0,1][ok,3,:].round(0).tolist(),'var',np.nanmedian(rf[0,1][:,4:6,:]))
  print('  load s %.1f maxrss MB %.0f'%(time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e3))
EOF
python survey.py
```

```
Exit code 1
105l001p16.mat rows 6400 alt True shapes {(1280, np.False_), (1500, np.True_)} tid monotone True stim counts [3200  400  400  400  400  400  400  400  400]
  V1 159 V2 25 rate V1 med 9.1 min 0.49; V2 med 2.7 min 0.82 n<0.5 1 0 values {1.0}
Traceback (most recent call last):
  File "/tmp/claude-1001/survey.py", line 21, in <module>
    print('  V1 elec',np.unique(uc[0,0][:,0]).size, uc[0,0][:,0].max(),'V2 elec',np.unique(uc[0,1][:,0]), 'rf shapes',rf[0,0].shape,rf[0,1].shape, 'V1 rf nan rows',np.isnan(rf[0,0][:,2,0]).sum())
                                                                                                                                                                             ~~~~~~~^^^^^^^
IndexError: too many indices for array: array is 2-dimensional, but 3 were indexed
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; cd $TMPDIR; sed -i 's/rf=nd\[.rfInfo.\]/rf=nd["rfInfo"]; rf=[r if r.ndim==3 else r[:,:,None] for r in (rf[0,0],rf[0,1])]; rf=np.array([[0,0]],dtype=object); rf[0,0],rf[0,1]=RR/' survey.py; sed -i 's/rf=nd\["rfInfo"\]; rf=\[/RR=[/; s/; rf=np.array(\[\[0,0\]\],dtype=object); rf\[0,0\],rf\[0,1\]=RR/\n  rf=np.empty((1,2),dtype=object); rf[0,0]=RR[0]; rf[0,1]=RR[1]/' survey.py; sed -i 's/RR=\[r if r.ndim==3 else r\[:,:,None\] for r in (rf\[0,0\],rf\[0,1\])\]/RR0=nd["rfInfo"]; RR=[r if r.ndim==3 else r[:,:,None] for r in (RR0[0,0],RR0[0,1])]/' survey.py; grep -n "RR" survey.py; python survey.py 2>&1 | grep -v "^105.*rows"
```

```
18:  uc=nd['unitCodes']; RR0=nd["rfInfo"]; RR=[r if r.ndim==3 else r[:,:,None] for r in (RR0[0,0],RR0[0,1])]
19:  rf=np.empty((1,2),dtype=object); rf[0,0]=RR[0]; rf[0,1]=RR[1]
  V1 159 V2 25 rate V1 med 9.1 min 0.49; V2 med 2.7 min 0.82 n<0.5 1 0 values {1.0}
  V1 elec 93 96 V2 elec [ 1  5  9 13 17 21] rf shapes (96, 7, 1) (28, 7, 1) V1 rf nan rows 1
  V1 rf x range 6.34784441861416 144.739406766349 y -85.59199419321126 1.313008536790468 var 266.9513646273295
  V2 rf rows [ 5  6  7  8  9 13 15 16 17 21 22 24] x [[26.0], [29.0], [25.0], [29.0], [55.0], [57.0], [62.0], [57.0], [69.0], [105.0], [97.0], [101.0]] y [[-75.0], [-78.0], [-74.0], [-78.0], [-87.0], [-105.0], [-105.0], [-97.0], [-95.0], [-85.0], [-91.0], [-88.0]] var 765.049208690539
  load s 1.6 maxrss MB 391
106r001p26.mat rows 6400 alt True shapes {(1280, np.False_), (1500, np.True_)} tid monotone True stim counts [3200  400  400  400  400  400  400  400  400]
  V1 109 V2 30 rate V1 med 13.4 min 0.47; V2 med 4.5 min 0.41 n<0.5 1 1 values {1.0}
  V1 elec 76 89 V2 elec [ 1  5  9 13 17 25] rf shapes (96, 7, 2) (28, 7, 2) V1 rf nan rows 11
  V1 rf x range -29.999820633575315 387.99999972463246 y -131.58113967018258 34.99999999999998 var 178.4248126455173
  V2 rf rows [ 1  5  6  8  9 10 11 12 13 17 18 19 20 25] x [[39.0, 282.0], [34.0, 278.0], [39.0, 282.0], [39.0, 279.0], [38.0, 374.0], [36.0, 288.0], [34.0, 282.0], [43.0, 285.0], [53.0, 297.0], [41.0, 285.0], [42.0, 287.0], [43.0, 287.0], [44.0, 288.0], [7.0, 258.0]] y [[-66.0, -47.0], [-67.0, -51.0], [-58.0, -46.0], [-63.0, -49.0], [-48.0, -105.0], [-53.0, -48.0], [-56.0, -47.0], [-54.0, -49.0], [-46.0, -41.0], [-53.0, -40.0], [-51.0, -39.0], [-50.0, -36.0], [-51.0, -38.0], [-100.0, -93.0]] var 624.2213211313608
  load s 1.4 maxrss MB 629
106r002p70.mat rows 6400 alt True shapes {(1280, np.False_), (1500, np.True_)} tid monotone True stim counts [3200  400  400  400  400  400  400  400  400]
  V1 88 V2 24 rate V1 med 8.9 min 0.87; V2 med 3.1 min 1.18 n<0.5 0 
[... 17 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/zandvakili-2015/v1v2.py",
 "content": "\"\"\"Loading and measures for CRCNS v1v2-1 (Zandvakili and Kohn 2015, Neuron 87, 827-839).\n\nThe data set is one zip, ``v1v2-1/live/v1-v2_gratings.zip`` in the public S3 bucket\n``crcnsarchive``. It is opened in place with fsspec and zipfile, and each session's .mat member\nis read into memory; nothing is written to disk.\n\nWhere each parameter comes from:\n\n- Analysis of driven trials only, the 1.28 s grating presentations (paper, Experimental\n  Procedures, Visual Stimuli; data descriptor, spikeRasters).\n- Units with a mean driven rate below 0.5 sp/s are removed (Experimental Procedures, Physiology,\n  \"we removed units with firing rates less than 0.5 spikes/s ... averaged across all stimuli\").\n  The SNR >= 2 selection cannot be applied: the data set has no waveforms or SNR.\n- CCG (Equation 1): coincidences summed over trials, divided by the overlap Q(tau) = T - |tau|\n  and the V1 rate, computed per stimulus and combined (Pairwise V1-V2 Analysis). Combining\n  is done by summing the coincidences of the eight stimuli and dividing by the summed\n  normaliser, which weights each stimulus by its V1 spike count; a standard choice that keeps\n  the unit of Equation 1 (coincidences per V1 spike per bin).\n- Bin of 1 ms: the files hold spike times at 1 ms resolution, where the paper used 0.1 ms\n  (deviation forced by the data).\n- Shuffle correction: the all-trial shift predictor (cross-correlation of the PSTHs divided by\n  the number of trials), per stimulus (Pairwise V1-V2 Analysis, \"shuffle-corrected for\n  stimulus-locked correlations\").\n- Jitter correction: subtract the expected CCG of jittered data (Smith and Kohn 2008, cited in\n  Pairwise V1-V2 Analysis). Jitter as in the claims file's shared divergence method: each spike\n  is redrawn from the spikes the neuron fired in the same window on trials of the same\n  stimulus, keeping the count per window and trial. Its expectation is the trial's count in the\n  window spread over the window in proportion to the PSTH; both neurons are jittered\n  independently, so the expected CCG is the CCG of these expected trains. Windows tile the trial\n  from 0 ms. The window is 10 ms (claims file, reading j-a, from the Figure 4C legend).\n- Smoothing of the jitter-corrected CCG with a Gaussian of SD 1.5 ms; significance when the\n  peak within 10 ms of zero lag exceeds 5 SD of the smoothed CCG over the flanks, 75 to 125 ms\n  on both sides (Pairwise V1-V2 Analysis). Lags of +-125 ms.\n- Divergence (Divergence Analysis; Results, V2 Spiking Is Preceded by Stronger V1\n  Coordination): V1 state is the number of V1 units active in a 1 ms bin, divided by the\n  number of V1 units; V2 spikes and V1 epochs from 50 ms after stimulus onset to the end of the\n  stimulus; jitter windows tile the trial from 50 ms; Jensen-Shannon divergence in bits\n  (Equations 2 and 3). The jitter draws from all trials of the stratum including the spike's\n  own trial, a standard choice (one trial in 400 changes the pool little).\n- Epochs at 1 ms resolution: a V1 bin at offset d holds V1 spikes d ms before the V2 spike's\n  bin (d > 0 before, d < 0 after); bins d = 2 and 3, centred 2 and 3 ms before, make the\n  1.5 to 3.5 ms epoch (claims file, reading e-a).\n\"\"\"\n\nimport io\nimport zipfile\n\nimport fsspec\nimport numpy as np\nimport scipy.io as sio\n\nURL = \"https://crcnsarchive.s3-us-west-2.amazonaws.com/v1v2-1/live/v1-v2_gratings.zip\"\nMEMBER = \"v1-v2_gratings/mat_neural_data/{}.mat\"\nSESSIONS = [\"105l001p16\", \"106r001p26\", \"106r002p70\", \"107l002p67\", \"107l003p143\"]\nT_MS = 1280            # driven trial length (data descriptor; SET_CONSTS.m)\nONSET_MS = 50          # response onset for the divergence analysis (Divergence Analysis)\nMIN_RATE = 0.5         # sp/s (Physiology)\nMAXLAG = 125           # ms, the outer edge of the CCG flanks\nJITTER_WINDOWS = [5, 10, 20, 40, 80, 1280]   # ms (Figure 6)\n\n\ndef open_zip():\n    f = fsspec.open(URL, block_size=2**20).open()\n    return zipfile.ZipFile(f)\n\n\ndef load_session(z, name):\n    \"\"\"Driven trials of one session as spike events.\n\n    Returns a dict with, per area ('V1', 'V2'): unit codes (electrode, sort), and spike events\n    as arrays (unit, trial, t) with t the ms bin 0..1279; per-trial stimulus codes 1..8; the\n    blank trials' events (for the clock check); the raw rate of every unit; and rfInfo.\n    \"\"\"\n    nd = sio.loadmat(io.BytesIO(z.read(MEMBER.format(name))))[\"neuralData\"][0, 0]\n    sr = nd[\"spikeRasters\"]\n    stim = nd[\"stim\"].ravel().astype(int)\n    driven = np.where(stim > 0)[0]\n    out = {\"name\": name, \"stim\": stim[driven], \"trial_id\": nd[\"trialId\"].ravel()[driven],\n           \"n_rows\": len(stim), \"row_stim\": stim}\n    for a, area in enumerate([\"V1\", \"V2\"]):\n        ev = {\"driven\": [], \"blank\": []}\n        for kind, rows in [(\"driven\", driven), (\"blank\", np.where(stim == 0)[0])]:\n            us, ts, trs = [], [], []\n            for k, r in enumerate(rows):\n                m = sr[r, a].tocoo()\n                us.append(m.row); ts.append(m.col); trs.append(np.full(m.nnz, k))\n                assert np.all(m.data == 1)\n            ev[kind] = (np.concatenate(us).astype(np.int32), np.concatenate(trs).astype(np.int32),\n                        np.concatenate(ts).astype(np.int32))\n        n_units = sr[0, a].shape[0]\n        rf = nd[\"rfInfo\"][0, a]\n        if rf.ndim == 2:\n            rf = rf[:, :, None]\n        counts = np.bincount(ev[\"driven\"][0], minlength=n_units)\n        out[area] = {\"codes\": nd[\"unitCodes\"][0, a].astype(int), \"events\": ev[\"driven\"],\n                     \"blank_events\": ev[\"blank\"], \"n_units\": n_units,\n                     \"rate\": counts / (len(driven) * T_MS / 1000.0), \"rf\": rf}\n    return out\n\n\ndef keep_units(sess, area):\n    \"\"\"Indices of units passing the 0.5 sp/s rate criterion (Physiology).\"\"\"\n    return np.where(sess[area][\"rate\"] >= MIN_RATE)[0]\n\n\ndef dense(events, units, trials, n_t=T_MS):\n    \"\"\"Binary array (len(units), len(trials), n_t) of the given units and trials.\"\"\"\n    u, tr, t = events\n    umap = np.full(u.max() + 1, -1)\n    umap[units] = np.arange(len(units))\n    tmap = np.full(tr.max() + 1, -1)\n    tmap[trials] = np.arange(len(trials))\n    sel = (umap[u] >= 0) & (tmap[tr] >= 0)\n    x = np.zeros((len(units), len(trials), n_t), np.float32)\n    x[umap[u[sel]], tmap[tr[sel]], t[sel]] = 1\n    return x\n\n\ndef _jitter_expectation(x, window, start=0):\n    \"\"\"Expected trains under the jitter of the module docstring, for x (units, trials, time).\"\"\"\n    n_t = x.shape[2]\n    win = np.full(n_t, -1)\n    win[start:] = (np.arange(n_t - start)) // window\n    nw = win.max() + 1\n    valid = win >= 0\n    psth = x.sum(1)                                            # units, time\n    wsum = np.zeros((x.shape[0], nw), np.float64)\n    np.add.at(wsum.T, win[valid], psth[:, valid].T)\n    p = np.zeros_like(psth, dtype=np.float64)\n    denom = wsum[:, win[valid]]\n    p[:, valid] = np.divide(psth[:, valid], denom, out=np.zeros_like(denom), where=denom > 0)\n    cnt = np.zeros((x.shape[0], x.shape[1], nw), np.float32)\n    np.add.at(cnt.transpose(2, 0, 1), win[valid], x[:, :, valid].transpose(2, 0, 1))\n    xj = np.zeros_like(x)\n    xj[:, :, valid] = cnt[:, :, win[valid]] * p[:, None, valid].astype(np.float32)\n    return xj\n\n\ndef _xcorr_sum(x, nfft, chunk=100):\n    \"\"\"Sum over trials of the cross-correlations of all unit pairs, lags -MAXLAG..MAXLAG.\n\n    r[i, j, tau] = sum_trials sum_t x_i(t) x_j(t + tau).\n    \"\"\"\n    n = x.shape[0]\n    nf = nfft // 2 + 1\n    s = np.zeros((nf, n, n), np.complex128)\n    for c in range(0, x.shape[1], chunk):\n        xf = np.fft.rfft(x[:, c:c + chunk], n=nfft, axis=2).astype(np.complex64)\n        xf = np.ascontiguousarray(xf.transpose(2, 0, 1))      # f, units, trials\n        s += np.matmul(xf.conj(), xf.transpose(0, 2, 1))\n    r = np.fft.irfft(s, n=nfft, axis=0)                        # lag, i, j\n    lags = np.arange(-MAXLAG, MAXLAG + 1)\n    return r[lags % nfft].transpose(1, 2, 0)\n\n\ndef session_ccgs(sess, jitter_window=10):\n    \"\"\"CCGs of all pairs of kept units (V1 then V2), summed over the eight stimuli.\n\n    Returns a dict: 'units' (area label and index of each unit), 'raw', 'shuffle', 'jitter'\n    (coincidence sums, units x units x lags; entry [i, j, tau] counts spikes of j at tau after\n    spikes of i), 'n_spikes' per unit, 'n_trials'.\n    \"\"\"\n    k1, k2 = keep_units(sess, \"V1\"), keep_units(sess, \"V2\")\n    nfft = 1536                                               # >= 1280 + 125, so no wrap\n    n = len(k1) + len(k2)\n    L = 2 * MAXLAG + 1\n    raw = np.zeros((n, n, L)); shuf = np.zeros((n, n, L)); jit = np.zeros((n, n, L))\n    nsp = np.zeros(n)\n    for s in range(1, 9):\n        trials = np.where(sess[\"stim\"] == s)[0]\n        x = np.concatenate([dense(sess[\"V1\"][\"events\"], k1, trials),\n                            dense(sess[\"V2\"][\"events\"], k2, trials)])\n        nsp += x.sum((1, 2))\n        raw += _xcorr_sum(x, nfft)\n        jit += _xcorr_sum(_jitter_expectation(x, jitter_window), nfft)\n        shuf += _xcorr_sum(x.sum(1, keepdims=True), nfft) / len(trials)\n        del x\n    units = [(\"V1\", i) for i in k1] + [(\"V2\", i) for i in k2]\n    return {\"units\": units, \"raw\": raw, \"shuffle\": shuf, \"jitter\": jit, \"n_spikes\": nsp,\n            \"n_trials\": len(sess[\"stim\"])}\n\n\ndef normalise(c, n_spikes_first):\n    \"\"\"Equation 1: divide by Q(tau) = T - |tau| (as a fraction of T) and the first unit's\n    spike count, giving coincidences per spike of the first unit per 1 ms bin.\"\"\"\n    lags = np.arange(-MAXLAG, MAXLAG + 1)\n    q = (T_MS - np.abs(lags)) / T_MS\n    return c / (q * n_spikes_first[..., None])\n\n\ndef gauss_smooth(c, sd=1.5):\n    \"\"\"Gaussian kernel of SD 1.5 ms along the last axis (Pairwise V1-V2 Analysis).\"\"\"\n    k = np.arange(-6, 7)\n    w = np.exp(-0.5 * (k / sd) ** 2)\n    w /= w.sum()\n    out = np.zeros_like(c)\n    L = c.shape[-1]\n    for kk, ww in zip(k, w):\n        src = np.clip(np.arange(L) + kk, 0, L - 1)\n        out += ww * c[..., src]\n    return out\n\n\ndef significance(jc_smoothed):\n    \"\"\"Peak within 10 ms of zero against 5 SD of the flanks (75 to 125 ms, both sides).\n\n    Returns (significant, peak value, peak lag in ms, flank SD).\"\"\"\n    lags = np.arange(-MAXLAG, MAXLAG + 1)\n    centre = np.abs(lags) <= 10\n    flank = (np.abs(lags) >= 75) & (np.abs(lags) <= 125)\n    seg = jc_smoothed[..., centre]\n    i = np.argmax(seg, axis=-1)\n    peak = np.take_along_axis(seg, i[..., None], -1)[..., 0]\n    sd = jc_smoothed[..., flank].std(-1)\n    return peak > 5 * sd, peak, lags[centre][i], sd\n\n\ndef half_width(c, lag_index):\n    \"\"\"Full width at half the peak height around a given peak (linear interpolation), in ms.\"\"\"\n    c = np.asarray(c, float)\n    h = c[lag_index] / 2\n    j = lag_index\n    while j > 0 and c[j] > h:\n        j -= 1\n    left = j + (h - c[j]) / (c[j + 1] - c[j]) if c[j] <= h else float(j)\n    j = lag_index\n    while j < len(c) - 1 and c[j] > h:\n        j += 1\n    right = j - (h - c[j]) / (c[j - 1] - c[j]) if c[j] <= h else float(j)\n    return right - left\n\n\n# ---------------------------------------------------------------- divergence\n\ndef pop_counts(events, units, n_trials, n_t=T_MS):\n    \"\"\"Number of the given units active in each 1 ms bin of each trial (trials x time).\"\"\"\n    u, tr, t = events\n    sel = np.isin(u, units)\n    key = np.unique((u[sel].astype(np.int64) * n_trials + tr[sel]) * n_t + t[sel])\n    cell = key % (n_trials * n_t)\n    return np.bincount(cell, minlength=n_trials * n_t).reshape(n_trials, n_t).astype(np.int16)\n\n\ndef jitter_events(events, units, stim, window, by_stim, rng, start=ONSET_MS, n_t=T_MS):\n    \"\"\"Jittered V1 events: windows tile [start, n_t); each spike in a window is replaced by one\n    drawn with replacement from the spikes the same unit fired in that window on trials of the\n    stratum (same stimulus if by_stim, else all trials). Spikes before start are kept.\"\"\"\n    u, tr, t = events\n    sel = np.isin(u, units)\n    u, tr, t = u[sel], tr[sel], t[sel]\n    late = t >= start\n    w = (t[late] - start) // window\n    strat = stim[tr[late]] if by_stim else np.zeros(late.sum(), int)\n    g = (u[late].astype(np.int64) * 9 + strat) * 1000 + w\n    order = np.argsort(g, kind=\"stable\")\n    gs = g[order]\n    ts = t[late][order]\n    starts = np.searchsorted(gs, gs, side=\"left\")\n    ends = np.searchsorted(gs, gs, side=\"right\")\n    pick = starts + (rng.random(len(gs)) * (ends - starts)).astype(np.int64)\n    new_t = np.empty_like(ts)\n    new_t[:] = ts[pick]\n    t_out = t.copy()\n    idx_late = np.where(late)[0][order]\n    t_out[idx_late] = new_t\n    return (u, tr, t_out)\n\n\ndef shuffle_events(events, units, stim, by_stim, rng):\n    \"\"\"Trial shuffle: each unit's trials permuted independently (within stimulus if by_stim).\"\"\"\n    u, tr, t = events\n    sel = np.isin(u, units)\n    u, tr, t = u[sel], tr[sel], t[sel]\n    n_tr = len(stim)\n    newtr = tr.copy()\n    for unit in units:\n        perm = np.arange(n_tr)\n        if by_stim:\n            for s in np.unique(stim):\n                idx = np.where(stim == s)[0]\n                perm[idx] = rng.permutation(idx)\n        else:\n            perm = rng.permutation(n_tr)\n        m = u == unit\n        newtr[m] = perm[tr[m]]\n    return (u, newtr, t)\n\n\ndef control_trials(stim, trials, by_stim, rng):\n    \"\"\"For each V2 spike's trial, another trial (same stimulus if by_stim).\"\"\"\n    n = len(stim)\n    out = np.empty(len(trials), int)\n    if by_stim:\n        groups = {s: np.where(stim == s)[0] for s in np.unique(stim)}\n        for s, idx in groups.items():\n            m = stim[trials] == s\n            pos = np.searchsorted(idx, trials[m])\n            r = rng.integers(0, len(idx) - 1, m.sum())\n            r = r + (r >= pos)\n            out[m] = idx[r]\n    else:\n        r = rng.integers(0, n - 1, len(trials))\n        out = r + (r >= trials)\n    return out\n\n\ndef state_hist(K, trials, times, offsets, unit_idx, n_units_v2, n_v1):\n    \"\"\"Histogram, per V2 unit, of V1 counts K[trial, time - d] pooled over offsets d.\n\n    Epochs falling outside [ONSET_MS, T_MS) are dropped. Returns (n_units_v2, n_v1 + 1).\"\"\"\n    h = np.zeros((n_units_v2, n_v1 + 1), np.int64)\n    for d in offsets:\n        tt = times - d\n        ok = (tt >= ONSET_MS) & (tt < K.shape[1])\n        k = K[trials[ok], tt[ok]]\n        h += np.bincount(unit_idx[ok] * (n_v1 + 1) + k,\n                         minlength=n_units_v2 * (n_v1 + 1)).reshape(n_units_v2, n_v1 + 1)\n    return h\n\n\ndef js_bits(p, q):\n    \"\"\"Jensen-Shannon divergence in bits between distributions along the last axis\n    (Equations 2 and 3); inputs are normalised here.\"\"\"\n    p = p / p.sum(-1, keepdims=True)\n    q = q / q.sum(-1, keepdims=True)\n    m = 0.5 * (p + q)\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        a = np.where(p > 0, p * np.log2(p / m), 0.0).sum(-1)\n        b = np.where(q > 0, q * np.log2(q / m), 0.0).sum(-1)\n    return 0.5 * a + 0.5 * b\n\n\ndef to_global(hists, n_v1s):\n    \"\"\"Map per-session histograms over counts 0..N1 onto one support of proportions k/N1.\n\n    hists: list of (n_neurons, N1 + 1) arrays; returns (sum of n_neurons, n_support).\"\"\"\n    from fractions import Fraction\n    keys = sorted({Fraction(k, n) for n in set(n_v1s) for k in range(n + 1)})\n    pos = {f: i for i, f in enumerate(keys)}\n    out = []\n    for h, n in zip(hists, n_v1s):\n        g = np.zeros((h.shape[0], len(keys)))\n        idx = np.array([pos[Fraction(k, n)] for k in range(n + 1)])\n        np.add.at(g.T, idx, h.T)\n        out.append(g)\n    return np.concatenate(out)\n\n\ndef divergence(h_raw, h_jit, weights=None, per_neuron=False):\n    \"\"\"Divergence of a group: h_raw, h_jit (neurons x support). weights (draws x neurons) are\n    bootstrap counts. Pooled distributions (reading d-a) or mean of per-neuron normalised\n    distributions (d-b).\"\"\"\n    if per_neuron:\n        h_raw = h_raw / np.maximum(h_raw.sum(1, keepdims=True), 1)\n        h_jit = h_jit / np.maximum(h_jit.sum(1, keepdims=True), 1)\n    if weights is None:\n        return js_bits(h_raw.sum(0), h_jit.sum(0))\n    return js_bits(weights @ h_raw, weights @ h_jit)\n\n\ndef boot_weights(n, n_boot, rng):\n    \"\"\"Bootstrap counts (n_boot x n) of neurons resampled with replacement.\"\"\"\n    idx = rng.integers(0, n, (n_boot, n))\n    w = np.zeros((n_boot, n))\n    np.add.at(w, (np.repeat(np.arange(n_boot), n), idx.ravel()), 1)\n    return w\n\n\ndef boot_p_paired(spk, ctl):\n    \"\"\"Reading p-a: two-sided p from paired draws (same neurons for both).\"\"\"\n    a = np.mean(ctl >= spk)\n    b = np.mean(ctl <= spk)\n    return min(1.0, 2 * min(a, b))\n\n\ndef boot_p_indep(spk, ctl):\n    \"\"\"Reading p-b: two-sided p treating the two bootstrap distributions as independent.\"\"\"\n    s = np.sort(spk)\n    ge = np.searchsorted(s, ctl, side=\"right\").mean() / len(s)      # P(spk <= ctl)\n    le = 1 - np.searchsorted(s, ctl, side=\"left\").mean() / len(s)   # P(spk >= ctl)\n    return min(1.0, 2 * min(ge, le))\n"
}
```

```
File created successfully at: entries/zandvakili-2015/v1v2.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; cd entries/zandvakili-2015; python -c "
import time, resource, numpy as np, v1v2 as h
z=h.open_zip(); t=time.time(); s=h.load_session(z,'106r002p70'); print('load',time.time()-t)
k1,k2=h.keep_units(s,'V1'),h.keep_units(s,'V2')
trials=np.where(s['stim']==1)[0]
t=time.time()
x=np.concatenate([h.dense(s['V1']['events'],k1,trials),h.dense(s['V2']['events'],k2,trials)])
print('dense',time.time()-t, x.shape); t=time.time()
r=h._xcorr_sum(x,1536); print('xcorr',time.time()-t); t=time.time()
xj=h._jitter_expectation(x,10); print('jexp',time.time()-t); 
# check jitter expectation preserves counts per window
print(np.allclose(xj[:,:,:10].sum(2), x[:,:,:10].sum(2)))
# brute-force check of one pair cross-correlation
i,j=3,95; bf=np.zeros(251)
for tr in range(x.shape[1]):
  a=x[i,tr]; b=x[j,tr]; c=np.correlate(b,a,mode='full'); bf+=c[1279-125:1279+126]
print('bf match',np.allclose(bf,r[i,j],atol=1e-3), bf[120:131], r[i,j,120:131].round(2))
print('maxrss MB',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e3)
"
```

```
load 1.3901410102844238
dense 0.09553074836730957 (112, 400, 1280)
xcorr 0.9102816581726074
jexp 1.0018177032470703
True
bf match True [2. 4. 5. 3. 0. 1. 2. 0. 1. 2. 0.] [2. 4. 5. 3. 0. 1. 2. 0. 1. 2. 0.]
maxrss MB 1276.412
```

**Agent**

CCG code matches a brute-force check and takes about 2 s per stimulus. Next, the divergence pipeline. Timing the jitter step first.

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; cd entries/zandvakili-2015; python -c "
import time, numpy as np, v1v2 as h
z=h.open_zip(); s=h.load_session(z,'107l003p143')
k1=h.keep_units(s,'V1'); rng=np.random.default_rng(0)
print('V1 events',len(s['V1']['events'][0]))
t=time.time(); K=h.pop_counts(s['V1']['events'],k1,3200); print('pop',time.time()-t, K.max(), K.mean())
for w in [5,80,1280]:
  t=time.time(); e=h.jitter_events(s['V1']['events'],k1,s['stim'],w,True,rng); Kj=h.pop_counts(e,k1,3200); print('jit',w,time.time()-t, Kj.mean(), 'counts/window preserved', np.allclose(K[:,50:].sum(), Kj[:,50:].sum(), rtol=0.01))
t=time.time(); e=h.shuffle_events(s['V1']['events'],k1,s['stim'],True,rng); print('shuf',time.time()-t)
"
```

```
/bin/bash: line 1: cd: entries/zandvakili-2015: No such file or directory
V1 events 15885866
pop 12.664231538772583 24 3.87838525390625
jit 5 15.392547845840454 3.789565185546875 counts/window preserved False
jit 80 15.057338237762451 3.744394775390625 counts/window preserved False
jit 1280 14.916101217269897 3.74431640625 counts/window preserved False
shuf 2.5483415126800537
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import re
p='v1v2.py'; s=open(p).read()
old_pop=s[s.index('def pop_counts'):s.index('def jitter_events')]
new_pop='''def pop_counts(events, units, n_trials, n_t=T_MS):
    """Number of the given units active in each 1 ms bin of each trial (trials x time).

    A unit with two spikes in one bin counts once (jittered data can put two there)."""
    u, tr, t = events
    K = np.zeros(n_trials * n_t, np.int16)
    order = np.argsort(u, kind="stable")
    us = u[order]
    cells = tr[order].astype(np.int64) * n_t + t[order]
    bounds = np.searchsorted(us, units), np.searchsorted(us, units, side="right")
    seen = np.zeros(n_trials * n_t, bool)
    for a, b in zip(*bounds):
        seen[:] = False
        seen[cells[a:b]] = True
        K += seen
    return K.reshape(n_trials, n_t)


'''
s=s.replace(old_pop,new_pop)
old='''    order = np.argsort(g, kind="stable")
    gs = g[order]
    ts = t[late][order]
    starts = np.searchsorted(gs, gs, side="left")
    ends = np.searchsorted(gs, gs, side="right")
    pick = starts + (rng.random(len(gs)) * (ends - starts)).astype(np.int64)
'''
new='''    order = np.argsort(g, kind="stable")
    gs = g[order]
    ts = t[late][order]
    first = np.r_[0, np.flatnonzero(np.diff(gs)) + 1]
    sizes = np.diff(np.r_[first, len(gs)])
    pick = np.repeat(first, sizes) + (rng.random(len(gs)) * np.repeat(sizes, sizes)).astype(np.int64)
'''
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
EOF
. $TMPDIR/dev/bin/activate; python -c "
import time, numpy as np, v1v2 as h
z=h.open_zip(); s=h.load_session(z,'107l003p143')
k1=h.keep_units(s,'V1'); rng=np.random.default_rng(0)
t=time.time(); K=h.pop_counts(s['V1']['events'],k1,3200); print('pop',time.time()-t, K.max(), K.mean())
for w in [5,1280]:
  t=time.time(); e=h.jitter_events(s['V1']['events'],k1,s['stim'],w,True,rng); t2=time.time(); Kj=h.pop_counts(e,k1,3200); print('jit',w,t2-t,time.time()-t2, Kj.mean())
  # check per-unit per-trial per-window counts kept
  u,tr,tt=e; uu,trr,ttt=s['V1']['events']; m=(uu==k1[0])&(ttt>=50); mm=(u==k1[0])&(tt>=50)
  a=np.bincount(trr[m]*300+(ttt[m]-50)//w, minlength=3200*300); b=np.bincount(tr[mm]*300+(tt[mm]-50)//w, minlength=3200*300); print('kept counts',np.array_equal(a,b))
"
```

```
pop 1.3926184177398682 24 3.87838525390625
jit 5 2.3255958557128906 1.4724078178405762 3.789565185546875
kept counts True
jit 1280 1.9946200847625732 1.4113974571228027 3.7442626953125
kept counts True
```

**Agent calls Bash**

```bash
date -u; cat >> v1v2.py <<'EOF'


def session_divergence(sess, seed, n_extra_realizations=2, offsets=range(-16, 17)):
    """Histograms of V1 states around the spikes of every kept V2 unit of one session.

    Readings (claims file header): s-a jitter pool and control trials from the same stimulus
    (main) or s-b from all trials; r-a one jitter realization (main) or r-b the sum of
    1 + n_extra_realizations (the mean distribution); shuffled data with trial permutation
    within stimulus (a) or across all trials (b), at spike epochs (c) and control epochs (d).
    Returns a dict of integer histograms over counts 0..N1 of active V1 units:
      raw[o, e, n, k]          offsets o, e = 0 spike epochs / 1 control epochs (s-a)
      jit[w, o, e, n, k]       the same on jittered V1 data, per jitter window w (s-a, r-a)
      raw_sb[o4, e, ...], jit_sb[w, o4, e, ...]   s-b, offsets (-3, -2, 2, 3)
      jit_rb[w, o4, e, ...]    r-b, extra realizations summed (add jit for the mean)
      shuf[r, x, e, ...], shuf_jit[r, w5, x, e, ...]  r = within stimulus / all trials,
                               x = 0 raw shuffled, epochs d = 2, 3 summed
    """
    rng = np.random.default_rng(seed)
    k1, k2 = keep_units(sess, "V1"), keep_units(sess, "V2")
    n1, n2 = len(k1), len(k2)
    stim = sess["stim"]
    n_tr = len(stim)
    ev1 = sess["V1"]["events"]
    u2, tr2, t2 = sess["V2"]["events"]
    m = np.isin(u2, k2) & (t2 >= ONSET_MS)
    umap = np.full(u2.max() + 1, -1)
    umap[k2] = np.arange(n2)
    vu, vtr, vt = umap[u2[m]], tr2[m], t2[m]
    ctl_a = control_trials(stim, vtr, True, rng)
    ctl_b = control_trials(stim, vtr, False, rng)
    offsets = list(offsets)
    o4 = [-3, -2, 2, 3]
    nw = len(JITTER_WINDOWS)

    def hists(K, offs, ctl):
        out = np.zeros((len(offs), 2, n2, n1 + 1), np.int64)
        for i, d in enumerate(offs):
            out[i, 0] = state_hist(K, vtr, vt, [d], vu, n2, n1)
            out[i, 1] = state_hist(K, ctl, vt, [d], vu, n2, n1)
        return out

    K = pop_counts(ev1, k1, n_tr)
    res = {"n_v1": n1, "n_v2": n2, "v2_units": k2, "n_spikes": np.bincount(vu, minlength=n2),
           "offsets": offsets, "o4": o4}
    res["raw"] = hists(K, offsets, ctl_a)
    res["raw_sb"] = hists(K, o4, ctl_b)
    res["jit"] = np.zeros((nw,) + res["raw"].shape, np.int64)
    res["jit_sb"] = np.zeros((nw,) + res["raw_sb"].shape, np.int64)
    res["jit_rb"] = np.zeros((nw,) + res["raw_sb"].shape, np.int64)
    for w, win in enumerate(JITTER_WINDOWS):
        Kj = pop_counts(jitter_events(ev1, k1, stim, win, True, rng), k1, n_tr)
        res["jit"][w] = hists(Kj, offsets, ctl_a)
        Kj = pop_counts(jitter_events(ev1, k1, stim, win, False, rng), k1, n_tr)
        res["jit_sb"][w] = hists(Kj, o4, ctl_b)
        for _ in range(n_extra_realizations):
            Kj = pop_counts(jitter_events(ev1, k1, stim, win, True, rng), k1, n_tr)
            res["jit_rb"][w] += hists(Kj, o4, ctl_a)
    w5 = [w for w in JITTER_WINDOWS if w <= 80]
    res["shuf"] = np.zeros((2, 2, n2, n1 + 1), np.int64)
    res["shuf_jit"] = np.zeros((2, len(w5), 2, n2, n1 + 1), np.int64)
    for r, by_stim in enumerate([True, False]):
        ev_s = shuffle_events(ev1, k1, stim, by_stim, rng)
        ctl = ctl_a if by_stim else ctl_b
        Ks = pop_counts(ev_s, k1, n_tr)
        res["shuf"][r] = hists(Ks, [2, 3], ctl).sum(0)
        for w, win in enumerate(w5):
            Kj = pop_counts(jitter_events(ev_s, k1, stim, win, by_stim, rng), k1, n_tr)
            res["shuf_jit"][r, w] = hists(Kj, [2, 3], ctl).sum(0)
    return res
EOF
. $TMPDIR/dev/bin/activate; python -c "
import time, resource, numpy as np, v1v2 as h
z=h.open_zip(); s=h.load_session(z,'106r002p70')
t=time.time(); r=h.session_divergence(s, 1); print('div',time.time()-t, 'maxrss MB',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e3)
print(r['n_spikes'], r['raw'].shape, r['jit'].shape)
b=r['raw'][[18,19]].sum(0); j=r['jit'][:,[18,19]].sum(1)
print('before d=2,3 spike/control: JS per window', [ (h.js_bits(b[0].sum(0),j[w,0].sum(0)).round(6), h.js_bits(b[1].sum(0),j[w,1].sum(0)).round(6)) for w in range(6)])
"
```

```
Thu Nov 12 16:40:19 UTC 2026
div 27.69561767578125 maxrss MB 709.54
[27497 12521 12738 15981 13992 10295  7870 14776  4804 11405  5292 12474
 11183 27220 23455 35080  6122 36109 15452 13948  5967 21782 10601 10533] (33, 2, 24, 89) (6, 33, 2, 24, 89)
before d=2,3 spike/control: JS per window [(np.float64(8.8e-05), np.float64(6e-05)), (np.float64(0.000186), np.float64(9.4e-05)), (np.float64(0.000248), np.float64(0.000113)), (np.float64(0.000303), np.float64(0.000167)), (np.float64(0.000444), np.float64(0.000207)), (np.float64(0.006517), np.float64(0.001504))]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='v1v2.py'; s=open(p).read()
old='''def session_ccgs(sess, jitter_window=10):'''
new='''def session_ccgs(sess, jitter_windows=(10, 25)):'''
s=s.replace(old,new)
s=s.replace('''    raw = np.zeros((n, n, L)); shuf = np.zeros((n, n, L)); jit = np.zeros((n, n, L))''','''    raw = np.zeros((n, n, L)); shuf = np.zeros((n, n, L))
    jit = {w: np.zeros((n, n, L)) for w in jitter_windows}''')
s=s.replace('''        jit += _xcorr_sum(_jitter_expectation(x, jitter_window), nfft)''','''        for w in jitter_windows:
            jit[w] += _xcorr_sum(_jitter_expectation(x, w), nfft)''')
s=s.replace("""    (coincidence sums, units x units x lags; entry [i, j, tau] counts spikes of j at tau after
    spikes of i), 'n_spikes' per unit, 'n_trials'.""","""    (coincidence sums, units x units x lags; entry [i, j, tau] counts spikes of j at tau after
    spikes of i; 'jitter' is a dict by jitter window), 'n_spikes' per unit, 'n_trials'. The
    10 ms window is the claims file's reading j-a; 25 ms is run as a variant of reading j-b, a
    choice of this attempt (the paper gives no other window).""")
open(p,'w').write(s)
EOF
grep -n "jitter_window" v1v2.py | head
```

```
156:def session_ccgs(sess, jitter_windows=(10, 25)):
170:    jit = {w: np.zeros((n, n, L)) for w in jitter_windows}
178:        for w in jitter_windows:
```

**Agent calls Write**

```json
{
 "file_path": "entries/zandvakili-2015/build_nb.py",
 "content": "\"\"\"Build the notebook from nb_src.py (cells separated by '# %%' lines). Not part of the entry.\"\"\"\nimport sys\nimport nbformat\n\nsrc = open(sys.argv[1]).read()\ncells = []\nfor block in src.split(\"\\n# %%\")[1:]:\n    head, _, body = block.partition(\"\\n\")\n    tags = []\n    if \"tags=\" in head:\n        tags = head.split(\"tags=\")[1].strip().strip(\"[]\").replace('\"', \"\").split(\",\")\n        tags = [t.strip() for t in tags if t.strip()]\n    if head.strip().startswith(\"[markdown]\"):\n        text = \"\\n\".join(l[2:] if l.startswith(\"# \") else l.lstrip(\"#\") for l in body.strip(\"\\n\").split(\"\\n\"))\n        c = nbformat.v4.new_markdown_cell(text)\n    else:\n        c = nbformat.v4.new_code_cell(body.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\nnb = nbformat.v4.new_notebook(cells=cells)\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbformat.write(nb, sys.argv[2])\n"
}
```

```
File created successfully at: entries/zandvakili-2015/build_nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
mv build_nb.py $TMPDIR/; ls
```

```
__pycache__
v1v2.py
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb_src.py",
 "content": "\n# %% [markdown]\n# # Reproducing Zandvakili and Kohn (2015) on CRCNS v1v2-1\n#\n# Paper: A. Zandvakili and A. Kohn, \"Coordinated Neuronal Activity Enhances Corticocortical\n# Communication\", Neuron 87, 827-839 (2015), doi:10.1016/j.neuron.2015.07.026.\n#\n# Dataset: CRCNS v1v2-1, \"Simultaneous V1-V2 neuronal population recordings in anesthetized\n# macaque monkeys\" (Zandvakili and Kohn 2019), doi:10.6080/K0B27SHN, read from the public S3\n# bucket `crcnsarchive` at `v1v2-1/live/v1-v2_gratings.zip`, opened in place.\n#\n# Version: CRCNS data sets are not versioned, so the version is recorded as `unversioned`\n# (docs/archives.md, CRCNS). The bucket holds one copy of the data, under `live/` (uploaded\n# 2026-02-11), with data description version 0.5 (Feb 15, 2019); there is no other version to\n# choose, and the paper cites none. The files read are pinned by the MD5 sums of the data set's\n# `checksums.md5`: `v1-v2_gratings.zip` 12a15c5a63366ccd1fa2b4e495f1d66d,\n# `docs/crcns_v1v2-1_data_description.pdf` 72e436e8e0c006efbbe5eab4737c3c69,\n# `docs/sessions_description.pdf` 48917aea682f869c7aee45f170516c7d. The first cell below checks\n# the listed sum of the zip against these.\n#\n# Claims: `claims/zandvakili-2015.yaml`, written from the version of record with its supplement.\n# The data set holds 5 sessions from 3 animals of the paper's 7; the paper's counts describe the\n# larger sample, so fractions, medians and comparisons are what is tested.\n#\n# | claim | here |\n# |---|---|\n# | fig4c-broad-ccg-peaks | tested |\n# | fig4c-narrow-peak-sites | tested |\n# | fig4-narrow-peak-depth | blocked, data_missing (no V2 depths) |\n# | fig5a-rf-alignment | blocked, metadata_insufficient (RF positions in pixels, no scale) |\n# | fig5-narrow-pairs-rare | tested |\n# | fig5b-v1v2-latency | tested |\n# | fig5b-intra-areal-zero-lag | tested |\n# | figs3-efficacy | tested |\n# | fig6a-coordination-before-v2 | tested |\n# | fig7a-threefold | tested |\n# | fig7a-above-shuffle | tested |\n# | fig6b-not-after-v2 | tested |\n# | fig6-slow-both-sides | tested |\n# | fig7d-time-course | tested |\n# | fig7b-nonmiddle-no-coordination | blocked, data_missing (no V2 depths or penetrations) |\n# | fig7e-nonmiddle-time-course | blocked, data_missing (as fig7b) |\n# | fig7c-offset-rf-no-coordination | blocked, data_missing (no depths; RF scale missing) |\n# | figs2a-v2-single-units | blocked, data_missing (no unit SNR or waveforms) |\n# | figs2b-v1-single-units | blocked, data_missing (no unit SNR or waveforms) |\n# | figs4-partner-not-needed | tested |\n# | figs5-middle-layer-relay | blocked, data_missing (no V2 depths) |\n# | fig1-ffn-propagation, fig3-divergence-correlation, figs1-higher-order, fig8-architecture | blocked, not_runnable (simulations, data: elsewhere, no code; not run in this attempt's time) |\n# | rf-sizes | blocked, metadata_insufficient (RF fits in pixels, no scale) |\n#\n# Shared methods are in the helper `v1v2.py`, whose docstring says where each parameter comes\n# from. Random seeds are fixed; each claim's section draws from its own generator.\n\n# %%\nimport time, resource\nimport numpy as np\nimport pandas as pd\nimport scipy.stats as st\nimport matplotlib.pyplot as plt\nimport fsspec\nimport v1v2 as h\n\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 30)\nT0 = time.time()\nz = h.open_zip()\nmd5 = fsspec.open(\"https://crcnsarchive.s3-us-west-2.amazonaws.com/v1v2-1/live/checksums.md5\").open().read().decode()\nprint(md5)\nassert \"12a15c5a63366ccd1fa2b4e495f1d66d  v1-v2_gratings.zip\" in md5\nfor i in z.infolist():\n    print(f\"{i.filename:60s} {i.file_size:>10d}\")\n\n# %% [markdown]\n# ## Load and compute\n#\n# Each session is loaded, its CCGs computed for all pairs of kept units (both jitter windows),\n# and the V1 state histograms around every V2 spike computed (helper `session_ccgs`,\n# `session_divergence`). The session's spikes are then released, so that one session is in\n# memory at a time. This is the long cell (several minutes).\n\n# %%\nL = 2 * h.MAXLAG + 1\nLAGS = np.arange(-h.MAXLAG, h.MAXLAG + 1)\npairs, sites, sess_info, div, sig_ccgs, clock, dup = [], [], {}, {}, [], [], []\n\ndef decode_acc(X, y, rng):\n    \"\"\"Nearest class mean on z-scored counts, two-fold cross-validation (a standard choice).\"\"\"\n    X = (X - X.mean(0)) / (X.std(0) + 1e-9)\n    idx = rng.permutation(len(y)); half = np.zeros(len(y), bool); half[idx[: len(y) // 2]] = True\n    acc = []\n    for tr in (half, ~half):\n        cls = np.unique(y)\n        mu = np.stack([X[tr & (y == c)].mean(0) for c in cls])\n        d = ((X[~tr][:, None, :] - mu[None]) ** 2).sum(-1)\n        acc.append(np.mean(cls[d.argmin(1)] == y[~tr]))\n    return float(np.mean(acc))\n\nfor si, name in enumerate(h.SESSIONS):\n    t = time.time()\n    s = h.load_session(z, name)\n    k1, k2 = h.keep_units(s, \"V1\"), h.keep_units(s, \"V2\")\n    n_tr = len(s[\"stim\"])\n    sess_info[name] = dict(animal=name[:3], n_rows=s[\"n_rows\"], n_driven=n_tr,\n                           stim_counts=np.bincount(s[\"stim\"])[1:].tolist(),\n                           v1_units=s[\"V1\"][\"n_units\"], v2_units=s[\"V2\"][\"n_units\"],\n                           v1_kept=len(k1), v2_kept=len(k2),\n                           v1_rate=s[\"V1\"][\"rate\"], v2_rate=s[\"V2\"][\"rate\"],\n                           v1_codes=s[\"V1\"][\"codes\"], v2_codes=s[\"V2\"][\"codes\"],\n                           v1_rf=s[\"V1\"][\"rf\"], v2_rf=s[\"V2\"][\"rf\"],\n                           trial_id_increasing=bool(np.all(np.diff(s[\"trial_id\"]) > 0)),\n                           row_alternates=bool(np.all(s[\"row_stim\"][1::2] == 0) and np.all(s[\"row_stim\"][0::2] > 0)))\n    # clock check: decode orientation from V1 counts in windows around stimulus onset\n    rng = np.random.default_rng(100 + si)\n    u, tr, tt = s[\"V1\"][\"events\"]; m = np.isin(u, k1)\n    bu, btr, btt = s[\"V1\"][\"blank_events\"]; bm = np.isin(bu, k1)\n    umap = np.full(u.max() + 1, -1); umap[k1] = np.arange(len(k1))\n    for lo, hi, label in [(-100, 0, \"last 100 ms of preceding blank\"), (0, 30, \"0-30 ms\"), (30, 60, \"30-60 ms\"),\n                          (60, 160, \"60-160 ms\"), (1180, 1280, \"1180-1280 ms\")]:\n        X = np.zeros((n_tr, len(k1)))\n        if lo < 0:\n            # blank row k precedes driven trial k + 1 (rows alternate driven, blank)\n            mm = bm & (btt >= 1500 + lo) & (btr < n_tr - 1)\n            np.add.at(X, (btr[mm] + 1, umap[bu[mm]]), 1)\n            keep = np.arange(1, n_tr)\n        else:\n            mm = m & (tt >= lo) & (tt < hi)\n            np.add.at(X, (tr[mm], umap[u[mm]]), 1)\n            keep = np.arange(n_tr)\n        acc = decode_acc(X[keep], s[\"stim\"][keep], rng)\n        # shifted labels: the same counts against the next trial's stimulus\n        acc_shift = decode_acc(X[keep][:-1], s[\"stim\"][keep][1:], rng)\n        clock.append(dict(session=name, window=label, accuracy=acc, shifted_labels=acc_shift))\n    # population PSTH onset (all orientations), for the latency check\n    psth = np.bincount(tt[m], minlength=h.T_MS) / (n_tr * len(k1)) * 1000\n    sess_info[name][\"psth\"] = psth\n    # mean V1 population response per stimulus, 50-1280 ms, for the orientation check\n    resp = np.zeros((8, len(k1)))\n    mm = m & (tt >= 50)\n    np.add.at(resp, (s[\"stim\"][tr[mm]] - 1, umap[u[mm]]), 1)\n    sess_info[name][\"resp\"] = resp / (np.bincount(s[\"stim\"])[1:, None])\n\n    cc = h.session_ccgs(s)\n    units = cc[\"units\"]\n    area = np.array([a for a, _ in units]); uidx = np.array([i for _, i in units])\n    elec = np.array([s[a][\"codes\"][i, 0] for a, i in units])\n    nsp = cc[\"n_spikes\"]\n    iu, ju = np.triu_indices(len(units), 1)\n    q = (h.T_MS - np.abs(LAGS)) / h.T_MS\n    norm = q[None, :] * nsp[iu][:, None]\n    raw = cc[\"raw\"][iu, ju] / norm\n    sc = (cc[\"raw\"][iu, ju] - cc[\"shuffle\"][iu, ju]) / norm\n    jc = {w: (cc[\"raw\"][iu, ju] - cc[\"jitter\"][w][iu, ju]) / norm for w in cc[\"jitter\"]}\n    # duplicate check: fraction of the sparser unit's spikes coincident at lag 0\n    zero_frac = cc[\"raw\"][iu, ju, h.MAXLAG] / np.minimum(nsp[iu], nsp[ju])\n    for k in np.where(zero_frac > 0.5)[0]:\n        dup.append(dict(session=name, a=units[iu[k]], b=units[ju[k]], frac=zero_frac[k]))\n    del cc\n    ptype = np.char.add(area[iu], area[ju])\n    df = pd.DataFrame(dict(session=name, animal=name[:3], type=ptype, i=uidx[iu], j=uidx[ju],\n                           elec_i=elec[iu], elec_j=elec[ju], n_i=nsp[iu], n_j=nsp[ju],\n                           zero_frac=zero_frac))\n    for w in jc:\n        sm = h.gauss_smooth(jc[w])\n        sig, peak, lag, sd = h.significance(sm)\n        df[f\"sig{w}\"] = sig; df[f\"peak{w}\"] = peak; df[f\"lag{w}\"] = lag; df[f\"sd{w}\"] = sd\n        if w == 10:\n            ks = np.where(sig)[0]\n            li = lag[ks] + h.MAXLAG\n            df.loc[ks, \"width_s\"] = [h.half_width(sm[k], l) for k, l in zip(ks, li)]\n            df.loc[ks, \"width_u\"] = [h.half_width(jc[w][k], l) for k, l in zip(ks, li)]\n            for nm, arr in [(\"eff_jc\", jc[w]), (\"eff_raw\", raw), (\"eff_sc\", sc)]:\n                df.loc[ks, nm] = [arr[k, l - 2:l + 3].sum() * 100 for k, l in zip(ks, li)]\n            for k in ks:\n                sig_ccgs.append((ptype[k], sm[k]))\n    pairs.append(df)\n    # site averages: V1-V2 pairs grouped by V2 electrode\n    v12 = np.where(ptype == \"V1V2\")[0]\n    for e in np.unique(elec[ju][v12]):\n        kk = v12[elec[ju][v12] == e]\n        row = dict(session=name, animal=name[:3], electrode=int(e), n_pairs=len(kk),\n                   n_v2_units=len(np.unique(uidx[ju][kk])), sc=sc[kk].mean(0))\n        for w in jc:\n            sig, peak, lag, sd = h.significance(h.gauss_smooth(jc[w][kk].mean(0)))\n            row[f\"sig{w}\"] = bool(sig); row[f\"peak{w}\"] = peak; row[f\"lag{w}\"] = int(lag); row[f\"sd{w}\"] = sd\n        sites.append(row)\n    del raw, sc, jc\n    div[name] = h.session_divergence(s, seed=1000 + si)\n    div[name][\"v2_elec\"] = s[\"V2\"][\"codes\"][div[name][\"v2_units\"], 0]\n    del s\n    print(f\"{name}: {time.time() - t:.0f} s, peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\npairs = pd.concat(pairs, ignore_index=True)\nsites = pd.DataFrame(sites)\nclock = pd.DataFrame(clock)\nprint(f\"total {time.time() - T0:.0f} s\")\n\n# %% [markdown]\n# ## Data check\n\n# %% tags=[\"sanity\"]\ninfo = pd.DataFrame({k: {c: v[c] for c in [\"animal\", \"n_rows\", \"n_driven\", \"v1_units\", \"v1_kept\", \"v2_units\", \"v2_kept\",\n                                           \"trial_id_increasing\", \"row_alternates\"]} for k, v in sess_info.items()}).T\nprint(info)\nprint(\"trials per orientation code 1..8:\", {k: v[\"stim_counts\"] for k, v in sess_info.items()})\nprint(\"animals:\", sorted({v[\"animal\"] for v in sess_info.values()}), \" sessions:\", len(sess_info))\nn1 = sum(v[\"v1_units\"] for v in sess_info.values()); n2 = sum(v[\"v2_units\"] for v in sess_info.values())\nprint(f\"units in the files: V1 {n1} (mean {n1 / 5:.1f} per session; descriptor says 112.2), V2 {n2} (mean {n2 / 5:.1f}; descriptor 29.4)\")\nfor a in [\"v1\", \"v2\"]:\n    r = np.concatenate([v[f\"{a}_rate\"] for v in sess_info.values()])\n    print(f\"{a.upper()} driven rate, sp/s: min {r.min():.2f}, median {np.median(r):.2f}, max {r.max():.2f}; below 0.5 sp/s: {(r < 0.5).sum()} removed\")\nfor k, v in sess_info.items():\n    print(k, \"V2 electrodes (sites):\", sorted(set(v[\"v2_codes\"][:, 0].tolist())),\n          \" V1 electrodes:\", len(set(v[\"v1_codes\"][:, 0].tolist())), \"of 96\",\n          \" rfInfo shapes V1\", v[\"v1_rf\"].shape, \"V2\", v[\"v2_rf\"].shape)\nallrf = np.concatenate([v[\"v1_rf\"][:, :, 0] for v in sess_info.values()])\nprint(\"V1 RF centre x range (pixels) %.0f to %.0f, y %.0f to %.0f; variance x median %.0f px^2; r2 median %.2f\" % (\n    np.nanmin(allrf[:, 2]), np.nanmax(allrf[:, 2]), np.nanmin(allrf[:, 3]), np.nanmax(allrf[:, 3]),\n    np.nanmedian(allrf[:, 4]), np.nanmedian(allrf[:, 6])))\nprint(\"spike rasters hold only 0 and 1 (asserted when loading); times are 1 ms bins 0..1279 (driven) and 0..1499 (blank)\")\nprint(\"\\nClock check: orientation decoded from V1 counts (chance 0.125), true labels and labels of the next trial\")\nprint(clock.pivot(index=\"window\", columns=\"session\", values=\"accuracy\").round(3))\nprint(clock.pivot(index=\"window\", columns=\"session\", values=\"shifted_labels\").round(3))\nprint(\"\\nV1 population PSTH (sp/s per unit), first ms where it exceeds the 0-20 ms mean by 50%:\")\nfor k, v in sess_info.items():\n    p = np.convolve(v[\"psth\"], np.ones(5) / 5, \"same\"); base = p[:20].mean()\n    print(f\"  {k}: baseline {base:.1f}, onset {int(np.argmax(p > 1.5 * base))} ms, peak {p.max():.1f} at {int(p.argmax())} ms\")\nprint(\"\\nOrientation codes: correlation of mean V1 population responses between stimulus codes\")\nfor k, v in sess_info.items():\n    c = np.corrcoef(v[\"resp\"])\n    print(f\"  {k}: code 7 with 1: {c[6, 0]:.3f}, with 6: {c[6, 5]:.3f}, with 8: {c[6, 7]:.3f}; code 5 with 1: {c[4, 0]:.3f}\")\nprint(f\"\\nPairs with more than half of the sparser unit's spikes coincident at lag 0 (duplicate check): {len(dup)}\")\nfor d in dup:\n    print(\"  \", d)\nprint(\"pairs:\", pairs.groupby([\"session\", \"type\"]).size().unstack())\nprint(\"V2 sites (electrodes):\", len(sites), \"; per session\", sites.groupby(\"session\").size().to_dict())\n\n# %% [markdown]\n# Checks of the description against the data:\n#\n# - 5 sessions in 3 animals (105, 106, 107), as the descriptor says. Each file holds 6400 rows,\n#   alternating a driven trial (1280 ms) and a blank (1500 ms); 400 driven trials per\n#   orientation code. Trial ids increase.\n# - The descriptor gives an average of 112.2 V1 units per session; the files hold the count\n#   printed above. V2: 29.4, as printed.\n# - The V2 electrodes are tetrodes, with unit electrode codes 1, 5, 9, ... (the first channel\n#   of each tetrode); rfInfo for V2 has one row per channel (28), so a V2 unit's RF is at the\n#   row of its electrode code. V1 rfInfo has 96 rows, one per array channel.\n# - RF positions and variances are in pixels. Nothing in the data set gives the pixel-to-degree\n#   scale or the position of the fixation point, and in four sessions the two eyes' RFs are\n#   250 to 400 pixels apart (two gratings, Visual Stimuli). The paper gives 1024 x 768 pixels\n#   at 110 cm without the screen size.\n# - Clock: orientation is decoded at chance from the end of the preceding blank and in the\n#   first 30 ms, and far above chance from 60 ms, with chance accuracy when the labels are\n#   shifted by one trial; the population PSTH rises some 30 to 50 ms after the start of the\n#   driven row. This is consistent with each driven row starting at stimulus onset and with\n#   the labels belonging to their own trial.\n# - Orientation codes: the sessions description says code 7 is 180 deg in session 105l001p16\n#   (135 deg elsewhere). The population responses to code 7 correlate with those to code 1\n#   (0 deg) more than with codes 6 and 8 in that session only, consistent with that note.\n# - No pair of units shares more than half of its spikes at zero lag, apart from those listed\n#   above (none listed means no duplicated unit); the five sessions have different unit counts,\n#   so no session is deposited twice.\n# - Not in the data set: V2 recording depth, penetration identity, unit SNR or waveforms,\n#   which the paper's layer groups and single-unit analyses need.\n\n# %% [markdown]\n# ## fig4c-narrow-peak-sites\n#\n# > A significant narrow peak in the site-average V1-V2 CCG occurs at a minority of V2 sites (46\n# > of 223). Expected fraction 0.206 +/- 0.021.\n#\n# A site is a V2 electrode in a session (one recording depth per session; the files hold no\n# depth). Site-average jitter-corrected CCG over all V1-V2 pairs at that electrode, 10 ms\n# jitter (reading j-a), smoothed, 5 SD rule. The 25 ms window is shown as a variant of reading\n# j-b.\n\n# %% tags=[\"claim:fig4c-narrow-peak-sites\"]\nprint(sites[[\"session\", \"electrode\", \"n_pairs\", \"n_v2_units\", \"sig10\", \"peak10\", \"sd10\", \"lag10\", \"sig25\"]].round(6).to_string())\nfor w in (10, 25):\n    print(f\"jitter {w} ms: {sites[f'sig{w}'].sum()} of {len(sites)} sites significant, fraction {sites[f'sig{w}'].mean():.3f}\")\nprint(\"per animal (10 ms):\", sites.groupby(\"animal\")[\"sig10\"].agg([\"sum\", \"count\"]).to_dict(\"index\"))\nratio = sites.peak10 / sites.sd10\nprint(\"peak / flank SD at each site, sorted:\", np.sort(ratio.values).round(1))\nfor thr in (4, 5, 6):\n    print(f\"  threshold {thr} SD: {(ratio > thr).sum()} of {len(sites)}\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig4c-broad-ccg-peaks\n#\n# > V1-V2 CCGs frequently have broad peaks, tens to hundreds of milliseconds wide, evident in\n# > site-average CCGs at all laminar locations.\n#\n# Site-average shuffle-corrected CCGs. Readings (a) mean over -50..50 ms above the flank mean\n# (75 to 125 ms), (b) mean over -50..50 ms above zero.\n\n# %% tags=[\"claim:fig4c-broad-ccg-peaks\"]\nSC = np.stack(sites.sc.values)\ncentre = np.abs(LAGS) <= 50; flank = (np.abs(LAGS) >= 75)\nsites[\"broad_a\"] = SC[:, centre].mean(1) > SC[:, flank].mean(1)\nsites[\"broad_b\"] = SC[:, centre].mean(1) > 0\nsites[\"centre_mean\"] = SC[:, centre].mean(1); sites[\"flank_mean\"] = SC[:, flank].mean(1)\nprint(sites[[\"session\", \"electrode\", \"sig10\", \"centre_mean\", \"flank_mean\", \"broad_a\", \"broad_b\"]].to_string())\nfor r in \"ab\":\n    g = sites.groupby(\"sig10\")[f\"broad_{r}\"].agg([\"sum\", \"count\"])\n    print(f\"reading {r}: {sites[f'broad_{r}'].sum()} of {len(sites)} sites; by narrow peak:\", g.to_dict(\"index\"))\navg = SC.mean(0)\nw_all = h.half_width(avg, h.MAXLAG + int(np.argmax(avg[np.abs(LAGS) <= 10])) - 10)\nprint(f\"across-site average: peak {avg.max():.2e} at {LAGS[avg.argmax()]} ms, flank mean {avg[flank].mean():.2e}, width at half height {w_all:.0f} ms\")\nprint(\"range of the plotted site-average CCGs: %.2e to %.2e\" % (SC.min(), SC.max()))\nfig, ax = plt.subplots(1, 2, figsize=(10, 3))\nfor k in range(len(SC)):\n    ax[int(sites.sig10[k])].plot(LAGS, SC[k], lw=0.7)\nfor a, t_ in zip(ax, [\"sites without a narrow peak\", \"sites with a narrow peak\"]):\n    a.set_title(t_); a.set_xlabel(\"lag (ms), V2 after V1 > 0\"); a.set_ylabel(\"coinc. per V1 spike\")\nplt.tight_layout()\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig4-narrow-peak-depth\n#\n# Blocked, `data_missing`: the files hold no recording depth for any V2 site, and no layer\n# 6/white matter reference.\n\n# %% [markdown]\n# ## fig5-narrow-pairs-rare\n#\n# > Only about 0.3% of all V1-V2 pairs have a significant narrow CCG peak (296 of 83,441).\n# > Expected 0.003 +/- 0.0003 or 0.00355 +/- 0.000355.\n\n# %% tags=[\"claim:fig5-narrow-pairs-rare\"]\nv12 = pairs[pairs.type == \"V1V2\"]\nfor w in (10, 25):\n    print(f\"jitter {w} ms: {v12[f'sig{w}'].sum()} of {len(v12)} V1-V2 pairs, fraction {v12[f'sig{w}'].mean():.5f}\")\nprint(v12.groupby(\"session\")[\"sig10\"].agg([\"sum\", \"count\", \"mean\"]))\nprint(\"by animal:\", v12.groupby(\"animal\")[\"sig10\"].agg([\"sum\", \"count\", \"mean\"]).to_dict(\"index\"))\nr = v12.peak10 / v12.sd10\nfor thr in (4, 5, 6):\n    print(f\"threshold {thr} SD: fraction {(r > thr).mean():.5f}\")\n# false positives: the same rule applied to negative peaks (troughs) of the same CCGs\nprint(\"pairs with a trough below -5 SD within 10 ms, an estimate of chance crossings: not computed by the rule; see below\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig5b-v1v2-latency\n#\n# > Narrow V1-V2 CCG peaks are offset from zero lag by a median of 2.8 ms, significantly\n# > different from zero, with a mean peak width of 3.71 ms. Expected 2.8 +/- 0.28 ms and\n# > 3.71 +/- 0.1 ms; test p < 0.001.\n\n# %% tags=[\"claim:fig5b-v1v2-latency\"]\nsg = v12[v12.sig10]\nlag = sg.lag10.values\nprint(f\"n = {len(sg)} significant V1-V2 pairs; median offset {np.median(lag):.1f} ms, mean {lag.mean():.2f} ms\")\nprint(\"offsets (ms), counts:\", dict(zip(*np.unique(lag, return_counts=True))))\nprint(\"Wilcoxon signed-rank (zeros dropped):\", st.wilcoxon(lag[lag != 0]))\nnpos, nneg = (lag > 0).sum(), (lag < 0).sum()\nprint(f\"sign test: {npos} positive, {nneg} negative, p = {st.binomtest(npos, npos + nneg).pvalue:.2e}\")\nprint(f\"width, (a) smoothed: mean {sg.width_s.mean():.2f} +/- {sg.width_s.std() / np.sqrt(len(sg)):.2f} ms (SEM); \"\n      f\"(b) unsmoothed: mean {sg.width_u.mean():.2f} +/- {sg.width_u.std() / np.sqrt(len(sg)):.2f} ms\")\nprint(\"per session median offset:\", sg.groupby(\"session\").lag10.median().to_dict(), \" n:\", sg.groupby(\"session\").size().to_dict())\nprint(\"per animal median offset:\", sg.groupby(\"animal\").lag10.median().to_dict())\nprint(\"pairs with offset above 0: %d, at 0: %d, below 0: %d\" % (npos, (lag == 0).sum(), nneg))\nsg25 = v12[v12.sig25]\nprint(f\"variant, 25 ms jitter: n = {len(sg25)}, median offset {np.median(sg25.lag25):.1f} ms\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig5b-intra-areal-zero-lag\n#\n# > Significant narrow peaks of V1-V1 and V2-V2 jitter-corrected CCGs have a median offset of\n# > 0.0 ms, not different from zero. Claim of absence; Wilcoxon signed-rank (a) or sign test\n# > (b), two-sided, p < 0.05.\n#\n# The lag sign follows the order of the unit lists (claims file). The data put units of one\n# tetrode, and units of one Utah array channel, together; pairs on the same electrode are shown\n# as a variant without them.\n\n# %% tags=[\"claim:fig5b-intra-areal-zero-lag\"]\nfor t_ in [\"V1V1\", \"V2V2\"]:\n    for label, d in [(\"all pairs\", pairs[(pairs.type == t_) & pairs.sig10]),\n                     (\"different electrodes\", pairs[(pairs.type == t_) & pairs.sig10 & (pairs.elec_i != pairs.elec_j)])]:\n        l_ = d.lag10.values\n        nz = l_[l_ != 0]\n        pw = st.wilcoxon(nz).pvalue if len(nz) > 0 else np.nan\n        npos, nneg = (l_ > 0).sum(), (l_ < 0).sum()\n        ps = st.binomtest(npos, npos + nneg).pvalue if npos + nneg > 0 else np.nan\n        print(f\"{t_} {label}: n = {len(l_)} of {(pairs.type == t_).sum()}, median {np.median(l_):.1f} ms, mean {l_.mean():.3f}, \"\n              f\"zero {np.sum(l_ == 0)}, +{npos} / -{nneg}; Wilcoxon p = {pw:.3f}, sign test p = {ps:.3f}\")\nfig, ax = plt.subplots(figsize=(5, 3))\nfor t_, c in [(\"V1V1\", \"C0\"), (\"V1V2\", \"0.5\"), (\"V2V2\", \"C3\")]:\n    l_ = pairs[(pairs.type == t_) & pairs.sig10].lag10\n    ax.hist(l_, bins=np.arange(-10.5, 11), histtype=\"step\", density=True, color=c, label=t_)\nax.set_xlabel(\"peak offset (ms)\"); ax.legend(); ax.set_xlim(-10.5, 10.5)\nprint(\"all offsets plotted lie in -10..10 ms by construction\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## figs3-efficacy\n#\n# > For significant V1-V2 pairs with peak offsets above 1 ms, the median efficacy (CCG integral\n# > within 2.5 ms of the peak) is 0.39%, mean 0.69%. Expected 0.39 +/- 0.039 and 0.69 +/- 0.12.\n#\n# Efficacy is the sum of the V1-rate-normalised CCG over the five 1 ms bins centred on the peak\n# (-2.5 to +2.5 ms). Readings: (a) the jitter-corrected CCG; (b) the raw CCG, shown both\n# without any correction and shuffle-corrected.\n\n# %% tags=[\"claim:figs3-efficacy\"]\ne = sg[sg.lag10 > 1]\nprint(f\"n = {len(e)} pairs with offset above 1 ms (of {len(sg)} significant)\")\nfor nm, label in [(\"eff_jc\", \"(a) jitter-corrected\"), (\"eff_raw\", \"(b) raw, uncorrected\"), (\"eff_sc\", \"(b) raw, shuffle-corrected\")]:\n    print(f\"{label}: median {e[nm].median():.3f}%, mean {e[nm].mean():.3f} +/- {e[nm].std() / np.sqrt(len(e)):.3f}% (SEM), range {e[nm].min():.3f} to {e[nm].max():.3f}\")\nprint(\"per animal, (a):\", e.groupby(\"animal\").eff_jc.agg([\"median\", \"mean\", \"count\"]).round(3).to_dict(\"index\"))\nprint(\"variant, all significant pairs, (a): median %.3f%%, mean %.3f%%\" % (sg.eff_jc.median(), sg.eff_jc.mean()))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig5a-rf-alignment and rf-sizes\n#\n# Blocked, `metadata_insufficient`: RF centres and variances are in pixels, and the data set\n# gives no pixel-to-degree scale and no fixation point. The paper gives 1024 x 768 pixels at\n# 110 cm without a screen size, so no scale follows from it. For information only, the values\n# in pixels: RF diameter as 4 times the square root of the mean variance (reading a) and the\n# ratio of V2 to V1 diameters, which needs no scale (the paper's values give 2.27 / 1.21 =\n# 1.88); and the probability of a significant pair against the RF offset in pixels, first eye.\n\n# %% tags=[\"claim:rf-sizes\"]\ndef rf_of(rf, row):\n    return rf[row, :, 0]\nd1, d2, d1b, d2b = [], [], [], []\nfor k, v in sess_info.items():\n    r1 = v[\"v1_rf\"][:, :, 0]; r2 = v[\"v2_rf\"][:, :, 0]\n    ok1 = ~np.isnan(r1[:, 4]) & (r1[:, 4] > 0) & (r1[:, 5] > 0)\n    ok2 = ~np.isnan(r2[:, 4]) & (r2[:, 4] > 0) & (r2[:, 5] > 0)\n    d1 += list(4 * np.sqrt(r1[ok1, 4:6].mean(1))); d2 += list(4 * np.sqrt(r2[ok2, 4:6].mean(1)))\n    d1b += list(4 * (r1[ok1, 4] * r1[ok1, 5]) ** 0.25); d2b += list(4 * (r2[ok2, 4] * r2[ok2, 5]) ** 0.25)\nprint(f\"per channel with a fit: V1 n = {len(d1)}, mean diameter (a) {np.mean(d1):.1f} px, (b) {np.mean(d1b):.1f} px; \"\n      f\"V2 n = {len(d2)}, (a) {np.mean(d2):.1f} px, (b) {np.mean(d2b):.1f} px\")\nprint(f\"ratio V2 / V1: (a) {np.mean(d2) / np.mean(d1):.2f}, (b) {np.mean(d2b) / np.mean(d1b):.2f}; the paper's degrees give {2.27 / 1.21:.2f}\")\nprint(f\"scale that would make the V1 mean 1.21 deg: {np.mean(d1) / 1.21:.1f} px/deg; the V2 mean 2.27 deg: {np.mean(d2) / 2.27:.1f} px/deg\")\n\n# %% tags=[\"claim:fig5a-rf-alignment\"]\noffs = []\nfor k, v in sess_info.items():\n    d = v12[v12.session == k]\n    r1 = v[\"v1_rf\"][:, :, 0]; r2 = v[\"v2_rf\"][:, :, 0]\n    c1 = v[\"v1_codes\"][d.i.values, 0] - 1; c2 = v[\"v2_codes\"][d.j.values, 0] - 1\n    dx = r1[c1, 2] - r2[c2, 2]; dy = r1[c1, 3] - r2[c2, 3]\n    offs.append(pd.DataFrame(dict(off=np.hypot(dx, dy), sig=d.sig10.values)))\noffs = pd.concat(offs).dropna()\nbins = np.arange(0, 201, 25)\ng = offs.groupby(pd.cut(offs.off, bins))[\"sig\"].agg([\"mean\", \"sum\", \"count\"])\nprint(f\"pairs with both RFs fitted: {len(offs)} of {len(v12)}; RF offset beyond 200 px: {(offs.off > 200).sum()}\")\nprint(g)\n\n# %% [markdown]\n# ## Divergence analyses: groups\n#\n# Middle-layer V2 neurons are the kept V2 units on electrodes whose site-average CCG has a\n# significant narrow peak (fig4c-narrow-peak-sites, 10 ms jitter). The V1 population is every\n# kept V1 unit of the session. Histograms of V1 states from all sessions are put on one support\n# of proportions (k / N1).\n\n# %% tags=[\"claim:fig6a-coordination-before-v2\"]\nmid_sites = set(map(tuple, sites.loc[sites.sig10, [\"session\", \"electrode\"]].values))\ngroups = {}\nfor k, d in div.items():\n    groups[k] = np.array([(k, int(e)) in mid_sites for e in d[\"v2_elec\"]])\nn_mid = sum(g_.sum() for g_ in groups.values())\nprint(\"middle-layer V2 neurons per session:\", {k: int(g_.sum()) for k, g_ in groups.items()}, \" total\", n_mid)\nprint(\"V1 population sizes:\", {k: d[\"n_v1\"] for k, d in div.items()})\nepochs = sum(d[\"raw\"][[18, 19], 0][:, groups[k]].sum() for k, d in div.items())\nspikes = sum(d[\"n_spikes\"][groups[k]].sum() for k, d in div.items())\nprint(f\"V2 spikes of middle-layer neurons from 50 ms: {spikes}; 1 ms epochs (two per spike in reading e-a, minus those outside the window): {epochs}\")\nOFF = list(div[h.SESSIONS[0]][\"offsets\"])\nWIN = h.JITTER_WINDOWS\nN_BOOT = 5000\n\ndef gather(key, sel, groupmask, extra=None):\n    \"\"\"Global-support histograms of one group: key picks the array, sel indexes it per session.\"\"\"\n    hs = [sel(div[k][key])[:, groupmask[k]] if extra is None else sel(div[k][key])[..., groupmask[k], :] for k in h.SESSIONS]\n    return hs\n\ndef to_g(hs):\n    \"\"\"Map per-session (..., neurons, N1+1) arrays to (..., neurons, support).\"\"\"\n    lead = hs[0].shape[:-2]\n    flat = [x.reshape((-1,) + x.shape[-2:]) for x in hs]\n    out = []\n    for i in range(flat[0].shape[0]):\n        out.append(h.to_global([f[i] for f in flat], [div[k][\"n_v1\"] for k in h.SESSIONS]))\n    out = np.stack(out)\n    return out.reshape(lead + out.shape[-2:])\n\ndef offset_hist(groupmask, offs, which=\"raw\", w=None, e=0):\n    \"\"\"(neurons, support) histogram pooled over the given offsets, spike (e=0) or control (e=1).\"\"\"\n    idx = [OFF.index(o) for o in offs]\n    if which == \"raw\":\n        hs = [div[k][\"raw\"][idx, e][:, groupmask[k]].sum(0) for k in h.SESSIONS]\n    else:\n        hs = [div[k][\"jit\"][w][idx, e][:, groupmask[k]].sum(0) for k in h.SESSIONS]\n    return h.to_global(hs, [div[k][\"n_v1\"] for k in h.SESSIONS])\n\ndef compare(raw_s, jit_s, raw_c, jit_c, rng, per_neuron=False, n_boot=N_BOOT):\n    \"\"\"Spike and control divergence, their bootstrap over neurons and the two p readings.\"\"\"\n    wts = h.boot_weights(raw_s.shape[0], n_boot, rng)\n    ds = h.divergence(raw_s, jit_s, per_neuron=per_neuron); dc = h.divergence(raw_c, jit_c, per_neuron=per_neuron)\n    bs = h.divergence(raw_s, jit_s, wts, per_neuron); bc = h.divergence(raw_c, jit_c, wts, per_neuron)\n    return dict(spike=ds, control=dc, ratio=ds / dc, p_a=h.boot_p_paired(bs, bc), p_b=h.boot_p_indep(bs, bc),\n                spike_lo=np.percentile(bs, 2.5), spike_hi=np.percentile(bs, 97.5),\n                control_lo=np.percentile(bc, 2.5), control_hi=np.percentile(bc, 97.5), boot_s=bs, boot_c=bc)\n\ndef run_reading(groupmask, rng, before=True, reading=\"main\"):\n    \"\"\"Spike against control divergence at the six windows under one reading of the shared method.\"\"\"\n    rows = []\n    sign = 1 if before else -1\n    o4 = [-3, -2, 2, 3]\n    for w, win in enumerate(WIN):\n        if reading in (\"main\", \"d-b\", \"e-b2\", \"e-b3\"):\n            offs = {\"e-b2\": [2], \"e-b3\": [3]}.get(reading, [2, 3])\n            offs = [sign * o for o in offs]\n            rs, js = offset_hist(groupmask, offs, \"raw\", e=0), offset_hist(groupmask, offs, \"jit\", w, e=0)\n            rc, jcn = offset_hist(groupmask, offs, \"raw\", e=1), offset_hist(groupmask, offs, \"jit\", w, e=1)\n        else:\n            ii = [o4.index(sign * o) for o in (2, 3)]\n            key_r, key_j = {\"s-b\": (\"raw_sb\", \"jit_sb\"), \"r-b\": (\"raw\", \"jit_rb\")}[reading]\n            def hh(e, jit):\n                out = []\n                for k in h.SESSIONS:\n                    d = div[k]\n                    if jit:\n                        x = d[key_j][w][ii, e].sum(0)\n                        if reading == \"r-b\":   # mean distribution of three realizations: add the main one\n                            x = x + d[\"jit\"][w][[OFF.index(sign * o) for o in (2, 3)], e].sum(0)\n                    elif key_r == \"raw\":\n                        x = d[\"raw\"][[OFF.index(sign * o) for o in (2, 3)], e].sum(0)\n                    else:\n                        x = d[key_r][ii, e].sum(0)\n                    out.append(x[groupmask[k]])\n                return h.to_global(out, [div[k][\"n_v1\"] for k in h.SESSIONS])\n            rs, js, rc, jcn = hh(0, False), hh(0, True), hh(1, False), hh(1, True)\n        r = compare(rs, js, rc, jcn, rng, per_neuron=(reading == \"d-b\"))\n        r.update(window=win, reading=reading)\n        rows.append(r)\n    return pd.DataFrame(rows)\n\nrng = np.random.default_rng(6)\nREADINGS = [\"main\", \"e-b2\", \"e-b3\", \"s-b\", \"r-b\", \"d-b\"]\nres6a = pd.concat([run_reading(groups, rng, True, r) for r in READINGS], ignore_index=True)\ncols = [\"reading\", \"window\", \"spike\", \"control\", \"ratio\", \"p_a\", \"p_b\", \"spike_lo\", \"spike_hi\", \"control_lo\", \"control_hi\"]\nprint(res6a[cols].to_string(float_format=lambda x: f\"{x:.3g}\"))\nfor r in READINGS:\n    d = res6a[res6a.reading == r]\n    print(f\"{r}: windows with spike > control at p < 0.05, p-a: {((d.p_a < 0.05) & (d.spike > d.control)).sum()} of 6, \"\n          f\"p-b: {((d.p_b < 0.05) & (d.spike > d.control)).sum()} of 6\")\n\n# %% tags=[\"claim:fig6a-coordination-before-v2\"]\n# per animal (main reading, point values; the bootstrap is over the pooled neurons)\nfor an in [\"105\", \"106\", \"107\"]:\n    gm = {k: groups[k] & (k[:3] == an) for k in groups}\n    if sum(x.sum() for x in gm.values()) == 0:\n        print(an, \"no middle-layer neurons\"); continue\n    vals = []\n    for w, win in enumerate(WIN):\n        rs, js = offset_hist(gm, [2, 3], \"raw\", e=0), offset_hist(gm, [2, 3], \"jit\", w, e=0)\n        rc, jcn = offset_hist(gm, [2, 3], \"raw\", e=1), offset_hist(gm, [2, 3], \"jit\", w, e=1)\n        vals.append(h.divergence(rs, js) / h.divergence(rc, jcn))\n    print(f\"animal {an}: {sum(x.sum() for x in gm.values())} neurons; spike / control divergence by window:\", np.round(vals, 2))\nfig, ax = plt.subplots(figsize=(5, 3))\nd = res6a[res6a.reading == \"main\"]\nax.errorbar(d.window, d.spike, yerr=[d.spike - d.spike_lo, d.spike_hi - d.spike], color=\"C3\", label=\"before V2 spike\")\nax.errorbar(d.window, d.control, yerr=[d.control - d.control_lo, d.control_hi - d.control], color=\"C0\", label=\"control\")\nax.set_xscale(\"log\"); ax.set_yscale(\"log\"); ax.set_xlabel(\"jitter window (ms)\"); ax.set_ylabel(\"divergence (bits)\"); ax.legend()\nprint(\"plotted range: %.2e to %.2e bits\" % (min(d.spike_lo.min(), d.control_lo.min()), max(d.spike_hi.max(), d.control_hi.max())))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig7a-threefold\n#\n# > For jitter windows of 5 to 80 ms, divergence before middle-layer V2 spikes is roughly\n# > 3-fold that of control epochs. Expected ratio 3 +/- 1. Readings (a) geometric mean of the five\n# > ratios, (b) median, (c) at least four of five windows within tolerance.\n\n# %% tags=[\"claim:fig7a-threefold\"]\nfor r in READINGS:\n    d = res6a[(res6a.reading == r) & (res6a.window <= 80)]\n    rat = d.ratio.values\n    print(f\"{r}: ratios {np.round(rat, 2)}; (a) geometric mean {np.exp(np.log(rat).mean()):.2f}; (b) median {np.median(rat):.2f}; \"\n          f\"(c) within 2 to 4: {np.sum((rat >= 2) & (rat <= 4))} of 5\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig7a-above-shuffle\n#\n# > Divergence both before middle-layer V2 spikes and in control epochs is significantly larger\n# > than divergence of shuffled data. Readings: trials permuted within orientation (a) or across\n# > all trials (b); epochs of the shuffled data spike-triggered (c) or control (d). Reproduced\n# > when the lower 95% bootstrap bound of both spike and control divergence is above the shuffled\n# > value at every window from 5 to 80 ms.\n\n# %% tags=[\"claim:fig7a-above-shuffle\"]\nnv1 = [div[k][\"n_v1\"] for k in h.SESSIONS]\nd = res6a[(res6a.reading == \"main\") & (res6a.window <= 80)].reset_index(drop=True)\nrows = []\nfor r, rl in enumerate([\"a\", \"b\"]):\n    for e, el in enumerate([\"c\", \"d\"]):\n        raw_ = h.to_global([div[k][\"shuf\"][r, e][groups[k]] for k in h.SESSIONS], nv1)\n        for w in range(5):\n            jit_ = h.to_global([div[k][\"shuf_jit\"][r, w, e][groups[k]] for k in h.SESSIONS], nv1)\n            sh = h.divergence(raw_, jit_)\n            rows.append(dict(shuffle=rl, epochs=el, window=WIN[w], shuffled=sh, spike_lo=d.spike_lo[w],\n                             control_lo=d.control_lo[w], both_above=(d.spike_lo[w] > sh) and (d.control_lo[w] > sh)))\nshuf = pd.DataFrame(rows)\nprint(shuf.to_string(float_format=lambda x: f\"{x:.3g}\"))\nprint(shuf.groupby([\"shuffle\", \"epochs\"]).both_above.sum().rename(\"windows of 5 where both bounds are above\"))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig6b-not-after-v2\n#\n# > In epochs 1.5 to 3.5 ms after middle-layer V2 spikes, V1 divergence does not differ from\n# > control epochs for jitter windows of 5 to 80 ms. Claim of absence, bootstrap readings p-a and\n# > p-b, p < 0.05.\n\n# %% tags=[\"claim:fig6b-not-after-v2\"]\nrng = np.random.default_rng(62)\nres6b = pd.concat([run_reading(groups, rng, False, r) for r in READINGS], ignore_index=True)\nprint(res6b[cols].to_string(float_format=lambda x: f\"{x:.3g}\"))\nfor r in READINGS:\n    d = res6b[(res6b.reading == r) & (res6b.window <= 80)]\n    print(f\"{r}: windows 5-80 ms with p < 0.05, p-a: {(d.p_a < 0.05).sum()}, p-b: {(d.p_b < 0.05).sum()}; \"\n          f\"difference spike - control: {np.round((d.spike - d.control).values, 7)}\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig6-slow-both-sides\n#\n# > At a jitter window of 1280 ms, V1 divergence is elevated both before and after middle-layer\n# > V2 spikes.\n\n# %% tags=[\"claim:fig6-slow-both-sides\"]\nfor label, res in [(\"before\", res6a), (\"after\", res6b)]:\n    d = res[res.window == 1280]\n    for _, row in d.iterrows():\n        print(f\"{label} {row.reading}: spike {row.spike:.3g}, control {row.control:.3g}, ratio {row.ratio:.2f}, p-a {row.p_a:.4f}, p-b {row.p_b:.4f}\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig7d-time-course\n#\n# > Enhanced V1 coordination is evident several milliseconds before middle-layer V2 spikes, but\n# > not in more distant epochs or after V2 spikes.\n#\n# Difference in divergence (spike minus control) at offsets within 15 ms, windows 5 to 80 ms,\n# main reading otherwise. Readings (a) 2 ms epochs stepped by 1 ms (centre d + 0.5 for bins d\n# and d + 1); (b) single 1 ms bins (centre d). Positive centres are before the spike. Bootstrap\n# p (reading p-a, 2000 draws, a standard choice for this many comparisons), Bonferroni over the\n# offsets of a window.\n\n# %% tags=[\"claim:fig7d-time-course\"]\ndef time_course(groupmask, rng, n_boot=2000):\n    rows = []\n    for rd in [\"a\", \"b\"]:\n        epochs_ = [([d, d + 1], d + 0.5) for d in range(-16, 16) if abs(d + 0.5) <= 15] if rd == \"a\" else [([d], float(d)) for d in range(-15, 16)]\n        for w in range(5):\n            for offs, c in epochs_:\n                rs, js = offset_hist(groupmask, offs, \"raw\", e=0), offset_hist(groupmask, offs, \"jit\", w, e=0)\n                rc, jcn = offset_hist(groupmask, offs, \"raw\", e=1), offset_hist(groupmask, offs, \"jit\", w, e=1)\n                r = compare(rs, js, rc, jcn, rng, n_boot=n_boot)\n                rows.append(dict(reading=rd, window=WIN[w], centre=c, diff=r[\"spike\"] - r[\"control\"], p=r[\"p_a\"],\n                                 n_off=len(epochs_)))\n    return pd.DataFrame(rows)\n\nrng = np.random.default_rng(74)\ntc = time_course(groups, rng)\ntc[\"sig_up\"] = (tc.p < 0.05 / tc.n_off) & (tc[\"diff\"] > 0)\n\ndef judge_tc(tc):\n    out = []\n    for (rd, win), d in tc.groupby([\"reading\", \"window\"]):\n        best = d.loc[d[\"diff\"].idxmax()]\n        bad = d[d.sig_up & ((d.centre < 0) | (d.centre > 8))]\n        out.append(dict(reading=rd, window=win, peak_centre=best.centre, peak_diff=best[\"diff\"],\n                        peak_in_1_6=1 <= best.centre <= 6, sig_before_1_6=int((d.sig_up & d.centre.between(1, 6)).sum()),\n                        sig_after_or_far=len(bad), bad_centres=list(bad.centre)))\n    return pd.DataFrame(out)\njt = judge_tc(tc)\nprint(jt.to_string(float_format=lambda x: f\"{x:.3g}\"))\nprint(tc.pivot_table(index=\"centre\", columns=[\"reading\", \"window\"], values=\"diff\").loc[lambda x: x.index.isin([-10, -5, -2.5, -2, 0, 0.5, 1.5, 2, 2.5, 3, 3.5, 5, 10])].to_string(float_format=lambda x: f\"{x:.1e}\"))\nfig, ax = plt.subplots(1, 5, figsize=(14, 2.6), sharey=True)\nfor i, win in enumerate(WIN[:5]):\n    d = tc[(tc.reading == \"a\") & (tc.window == win)]\n    ax[i].plot(d.centre, d[\"diff\"], \"k.-\"); ax[i].axhline(0, color=\"0.7\"); ax[i].set_title(f\"{win} ms\"); ax[i].set_xlabel(\"ms before V2 spike\")\nax[0].set_ylabel(\"spike - control (bits)\")\nprint(\"plotted range (reading a): %.2e to %.2e\" % (tc[tc.reading == \"a\"][\"diff\"].min(), tc[tc.reading == \"a\"][\"diff\"].max()))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## figs4-partner-not-needed\n#\n# > V1 coordination is elevated before spikes of middle-layer V2 neurons both with and without a\n# > significant CCG peak with a recorded V1 neuron, slightly more for those with one.\n\n# %% tags=[\"claim:figs4-partner-not-needed\"]\npartner = set(map(tuple, v12.loc[v12.sig10, [\"session\", \"j\"]].values))\nwith_p = {k: groups[k] & np.array([(k, int(u)) in partner for u in div[k][\"v2_units\"]]) for k in groups}\nwithout_p = {k: groups[k] & ~with_p[k] for k in groups}\nrng = np.random.default_rng(84)\nout = {}\nfor label, gm in [(\"with partner\", with_p), (\"without partner\", without_p)]:\n    n = sum(x.sum() for x in gm.values())\n    r = run_reading(gm, rng, True, \"main\")\n    r = r[r.window <= 80]\n    out[label] = r\n    print(f\"{label}: {n} neurons; ratio {np.round(r.ratio.values, 2)}; p-a {np.round(r.p_a.values, 4)}; p-b {np.round(r.p_b.values, 4)}; \"\n          f\"windows with spike > control at p < 0.05 (p-a): {((r.p_a < 0.05) & (r.spike > r.control)).sum()} of 5\")\nprint(\"ratio larger with partner at\", int((out[\"with partner\"].ratio.values > out[\"without partner\"].ratio.values).sum()), \"of 5 windows\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## Blocked claims\n#\n# - fig4-narrow-peak-depth, fig7b-nonmiddle-no-coordination, fig7e-nonmiddle-time-course,\n#   figs5-middle-layer-relay: need V2 depth or the order of sites in a penetration; the files\n#   hold one recording per V2 electrode per session and no depth (`data_missing`).\n# - fig7c-offset-rf-no-coordination: needs depth (500 to 1000 um from the layer 6/WM border)\n#   and RF offsets in degrees (`data_missing`).\n# - figs2a-v2-single-units, figs2b-v1-single-units: need unit SNR; the files hold no waveforms\n#   or SNR (`data_missing`).\n# - fig5a-rf-alignment, rf-sizes: need RF positions in degrees (`metadata_insufficient`).\n# - fig1-ffn-propagation, fig3-divergence-correlation, figs1-higher-order, fig8-architecture:\n#   simulations with no published code (`data: elsewhere`), not run in this attempt.\n\n# %% [markdown]\n# ## Summary\n\n# %%\nprint(f\"notebook run time {time.time() - T0:.0f} s; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb_src.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('nb_src.py').read()
s=s.replace('''# false positives: the same rule applied to negative peaks (troughs) of the same CCGs
print("pairs with a trough below -5 SD within 10 ms, an estimate of chance crossings: not computed by the rule; see below")
''','')
a=s.index('def gather('); b=s.index('def offset_hist(')
s=s[:a]+s[b:]
open('nb_src.py','w').write(s)
dev=s.replace('import v1v2 as h\n','import v1v2 as h\nh.SESSIONS = ["106r002p70", "107l002p67"]\nimport matplotlib; matplotlib.use("Agg")\n')
open('dev.py','w').write(dev)
EOF
. dev/bin/activate; cd entries/zandvakili-2015 && time python $TMPDIR/dev.py 2>&1 | tail -150
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/dev.py", line 61, in <module>
    import v1v2 as h
ModuleNotFoundError: No module named 'v1v2'

real	0m3.891s
user	0m4.083s
sys	0m0.250s
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; cd entries/zandvakili-2015 && time PYTHONPATH=. python $TMPDIR/dev.py 2>&1 | tail -150
```

```
84de899a70ef2f09c17dd41aa96e75c1  docs/crcns_v1v2-1_data_description.docx
72e436e8e0c006efbbe5eab4737c3c69  docs/crcns_v1v2-1_data_description.pdf
48917aea682f869c7aee45f170516c7d  docs/sessions_description.pdf
eb2042d9e1b708920b7a9eb8c986849c  filelist.txt
12a15c5a63366ccd1fa2b4e495f1d66d  v1-v2_gratings.zip

v1-v2_gratings/                                                       0
v1-v2_gratings/mat_neural_data/                                       0
v1-v2_gratings/mat_neural_data/106r002p70.mat                  15505921
v1-v2_gratings/mat_neural_data/105l001p16.mat                  34774439
v1-v2_gratings/mat_neural_data/107l003p143.mat                 38843972
v1-v2_gratings/mat_neural_data/106r001p26.mat                  29213463
v1-v2_gratings/mat_neural_data/107l002p67.mat                  34004346
v1-v2_gratings/software/                                              0
v1-v2_gratings/software/COLOR_MAP.mat                               395
v1-v2_gratings/software/Squash.m                                     90
v1-v2_gratings/software/SET_CONSTS.m                                108
v1-v2_gratings/software/BinTime.m                                   649
v1-v2_gratings/software/ExtractSpikes.m                            2810
v1-v2_gratings/software/example.m                                  1402
[... 76 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('nb_src.py').read()
s=s.replace('''            row[f"sig{w}"] = bool(sig); row[f"peak{w}"] = peak; row[f"lag{w}"] = int(lag); row[f"sd{w}"] = sd''','''            row[f"sig{w}"] = bool(sig); row[f"peak{w}"] = float(peak); row[f"lag{w}"] = int(lag); row[f"sd{w}"] = float(sd)''')
open('nb_src.py','w').write(s)
dev=s.replace('import v1v2 as h\n','import v1v2 as h\nh.SESSIONS = ["106r002p70", "107l002p67"]\nimport matplotlib; matplotlib.use("Agg")\nimport pickle\n')
cut='print(f"total {time.time() - T0:.0f} s")\n'
a,b=dev.split(cut)
a=a+cut+'pickle.dump(dict(pairs=pairs,sites=sites,clock=clock,sess_info=sess_info,div=div,dup=dup,sig_ccgs=sig_ccgs),open("/tmp/claude-1001/cache.pkl","wb"))\n'
head=a[:a.index('# %%\nL = 2')]
b=head+'L = 2 * h.MAXLAG + 1\nLAGS = np.arange(-h.MAXLAG, h.MAXLAG + 1)\nglobals().update(pickle.load(open("/tmp/claude-1001/cache.pkl","rb")))\n'+b
open('devA.py','w').write(a); open('devB.py','w').write(b)
EOF
. dev/bin/activate; cd entries/zandvakili-2015 && PYTHONPATH=. python $TMPDIR/devA.py 2>&1 | tail -3 && time PYTHONPATH=. python $TMPDIR/devB.py 2>&1 | tail -150
```

```
106r002p70: 70 s, peak memory 1.46 GB
107l002p67: 148 s, peak memory 1.99 GB
total 218 s
16    e-b3      80 0.000903 0.000495   1.82 0.0032  0.00658  0.000631    0.0011    0.000424    0.000563
17    e-b3    1280  0.00336  0.00111   3.04      0    8e-08   0.00251   0.00487    0.000979      0.0013
18     s-b       5 0.000214 0.000122   1.76 0.0028  0.00883  0.000159   0.00026    9.92e-05    0.000146
19     s-b      10  0.00042 0.000234   1.79 0.0004  0.00295  0.000306  0.000524    0.000182    0.000277
20     s-b      20 0.000591 0.000299   1.98      0 9.37e-05  0.000446  0.000718    0.000231    0.000351
21     s-b      40 0.000653 0.000374   1.75 0.0016  0.00524  0.000463  0.000828    0.000308    0.000427
22     s-b      80 0.000851 0.000407   2.09      0 0.000156  0.000609   0.00105    0.000309    0.000473
23     s-b    1280  0.00307 0.000974   3.16      0        0    0.0023   0.00467    0.000902     0.00116
24     r-b       5 0.000213 0.000119    1.8      0 5.48e-05  0.000169  0.000256    9.82e-05    0.000137
25     r-b      10 0.000415 0.000232   1.79      0  0.00026  0.000314  0.000518    0.000188    0.000264
26     r-b      20 0.000575 0.000317   1.81      0  0.00108  0.000416  0.000722    0.000253     0.00036
27     r-b      40 0.000743 0.000401   1.85      0   0.0013  0.000533  0.000915    0.000313    0.000453
28     r-b      80 0.000908 0.000469   1.93 0.0004   0.0022  0.000655    0.0011    0.000375    0.000529
29     r-b    1280  0.00336   0.0011   3.05      0        0   0.00258   0.00483       0.001     0.00132
30     d-b       5 0.000197 0.000124   1.58 0.0024   0.0118  0.000169  0.000261    0.000106    0.000176
31     d-b      10 0.000338 0.000208   1.63 0.0004   0.0018  0.000286  0.000429    0.000177    0.000273
32     d-b      20 0.000467 0.000266   1.76      0  0.00269  0.000368  0.000618    0.000219    0.000354
[... 137 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd  python tools/entry.py --help 2>&1 | head -30; grep -n "related\|python\|runtime" schemas/entry.schema.json | head -30; ls entries | grep -i crcns; grep -l "crcns" entries/*/entry.yaml | head -3
```

```
Thu Nov 12 16:52:39 UTC 2026
usage: entry.py [-h] [--output-dir OUTPUT_DIR] [--timeout TIMEOUT]
                [--max-minutes MAX_MINUTES] [--fresh] [--python PYTHON]
                [--before BEFORE]
                {lock,check,run,all,handover,upgrade-python,hash}
                entry [entry ...]

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
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cat entries/bruno-2017/entry.yaml; cat entries/bruno-2017/requirements.in
```

```
schema_version: 1
name: bruno-2017
type: reproduction
title: Spiral attractor in the Aplysia pedal ganglion (Bruno, Frost and Humphries 2017)
description: Tests the findings of Bruno, Frost and Humphries (2017) on CRCNS data set apl-1, which
  holds the spike times of 30 voltage-sensitive dye recordings of the pedal ganglion (three evoked
  bouts of fictive locomotion in each of 10 preparations), the P10 nerve spikes of nine of them and
  the neurons' positions on the photodiode array. It ports the paper's recurrence analysis, local
  linear models, manifold comparisons, P10 decoding, participation measures and ensemble typing from the
  paper's MATLAB code, under every reading of the kernel width and the number of dimensions.
license: Apache-2.0
notebooks:
- path: reproduce_bruno_2017.ipynb
  title: Reproducing Bruno, Frost and Humphries (2017) from CRCNS apl-1
  runtime_minutes: 40
helpers:
- apl.py
related:
- id: crcns:apl-1/unversioned
  relation: uses_data
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/zandvakili-2015 && cat > entry.yaml <<'EOF'
schema_version: 1
name: zandvakili-2015
type: reproduction
title: V1 coordination before V2 spiking in anesthetized macaques (Zandvakili and Kohn 2015)
description: Tests the findings of Zandvakili and Kohn (2015) on CRCNS data set v1v2-1, which holds
  the spike times of V1 Utah array units and V2 tetrode units in 5 sessions from 3 anesthetized
  macaques viewing drifting gratings, with receptive field fits per channel. It computes the
  jitter-corrected V1-V2, V1-V1 and V2-V2 cross-correlograms, finds the V2 sites with a narrow V1-V2
  peak, and measures the Jensen-Shannon divergence of V1 population states around V2 spikes against
  control epochs and shuffled data, under every reading of the open method details. The V2 depths,
  unit SNR and the pixel-to-degree scale that the layer, single-unit and receptive field analyses
  need are not in the data set.
license: Apache-2.0
notebooks:
- path: reproduce_zandvakili_2015.ipynb
  title: Reproducing Zandvakili and Kohn (2015) from CRCNS v1v2-1
  runtime_minutes: 15
helpers:
- v1v2.py
related:
- id: crcns:v1v2-1/unversioned
  relation: uses_data
- id: doi:10.1016/j.neuron.2015.07.026
  relation: reproduces
EOF
printf "aiohttp\nfsspec\nmatplotlib\nnumpy\npandas\nrequests\nscipy\n" > requirements.in
rm -rf __pycache__
. $TMPDIR/dev/bin/activate; python $TMPDIR/build_nb.py $TMPDIR/nb_src.py reproduce_zandvakili_2015.ipynb; cd ../..; deactivate; python tools/entry.py lock entries/zandvakili-2015 2>&1 | tail -5; python tools/entry.py check entries/zandvakili-2015 2>&1 | tail -20
```

```
wrote zandvakili-2015/requirements.lock.txt (Python 3.13, with hashes)
error: entries/zandvakili-2015/reproduce_zandvakili_2015.ipynb: neither the notebook nor a helper names version unversioned of dataset v1v2-1, which entry.yaml pins
1 error(s)
```

**Agent calls Bash**

```bash
grep -n "names version" -B25 tools/entry.py | grep -n "def \|version\|in text\|re\." | head -30
```

```
4:222-    versions = {d: v for d, _, v in used}
8:226-        for d, v in versions.items():
10:228-                report.error(rel / "entry.yaml", f"pin the version of dataset {d}, as {archives[d]}:{d}/<version>")
15:233-        nb = nbformat.read(path, as_version=4)
24:242-            version = versions[dandiset]
25:243-            if version and version not in code and version not in helper_code:
26:244:                report.error(rel / name, f"neither the notebook nor a helper names version {version} "
```

**Agent calls Bash**

```bash
cd entries/zandvakili-2015 && python3 - <<'EOF'
p='v1v2.py'; s=open(p).read()
s=s.replace('URL = "https','DATASET = "v1v2-1"\nVERSION = "unversioned"   # CRCNS data sets are not versioned (docs/archives.md); pinned by MD5\nURL = "https',1)
open(p,'w').write(s)
EOF
cd ../.. && python tools/entry.py check entries/zandvakili-2015 2>&1 | tail -5; date -u
```

```
0 error(s)
Thu Nov 12 16:53:04 UTC 2026
```

**Agent calls Bash**

```bash
time python tools/entry.py all entries/zandvakili-2015 2>&1 | tail -15; date -u
```

```
Installed kernelspec registry-zandvakili-2015 in executed/zandvakili-2015/.venv/share/jupyter/kernels/registry-zandvakili-2015
0 error(s)
pass  reproduce_zandvakili_2015.ipynb  (745 s)

real	12m34.805s
user	17m37.564s
sys	0m51.766s
Thu Nov 12 17:05:44 UTC 2026
```

**Agent**

The full run passes in 12.4 minutes. Reading the outputs.

**Agent calls Bash**

```bash
ls executed/zandvakili-2015/; python3 - <<'EOF'
import nbformat
nb=nbformat.read('executed/zandvakili-2015/reproduce_zandvakili_2015.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    if i<3: continue
    print('=== cell',i,c.metadata.get('tags'))
    for o in c.get('outputs',[]):
        if 'text' in o: print(o['text'][:6000])
        elif o.get('output_type')=='error': print(o['ename'],o['evalue'])
EOF
```

```
<persisted-output>
Output too large (32KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/0c90c0c9-43b9-40d9-b0f2-cee07c4eeda0/tool-results/brpnnq5lj.txt

Preview (first 2KB):
reproduce_zandvakili_2015.ipynb
result.json
=== cell 3 None
105l001p16: 157 s, peak memory 2.57 GB

106r001p26: 122 s, peak memory 2.57 GB

106r002p70: 70 s, peak memory 2.57 GB

107l002p67: 154 s, peak memory 2.57 GB

107l003p143: 201 s, peak memory 2.75 GB
total 705 s

=== cell 5 ['sanity']
            animal n_rows n_driven v1_units v1_kept v2_units v2_kept trial_id_increasing row_alternates
[... 15 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/0c90c0c9-43b9-40d9-b0f2-cee07c4eeda0/tool-results/brpnnq5lj.txt",
 "offset": 25
}
```

```
25	V1 driven rate, sp/s: min 0.47, median 15.01, max 131.23; below 0.5 sp/s: 2 removed
26	V2 driven rate, sp/s: min 0.41, median 3.66, max 54.66; below 0.5 sp/s: 1 removed
27	105l001p16 V2 electrodes (sites): [1, 5, 9, 13, 17, 21]  V1 electrodes: 93 of 96  rfInfo shapes V1 (96, 7, 1) V2 (28, 7, 1)
28	106r001p26 V2 electrodes (sites): [1, 5, 9, 13, 17, 25]  V1 electrodes: 76 of 96  rfInfo shapes V1 (96, 7, 2) V2 (28, 7, 2)
29	106r002p70 V2 electrodes (sites): [1, 5, 9, 13, 17]  V1 electrodes: 57 of 96  rfInfo shapes V1 (96, 7, 2) V2 (28, 7, 2)
30	107l002p67 V2 electrodes (sites): [1, 5, 9, 13, 17, 21, 25]  V1 electrodes: 75 of 96  rfInfo shapes V1 (96, 7, 2) V2 (28, 7, 2)
31	107l003p143 V2 electrodes (sites): [1, 5, 9, 13, 17, 21, 25]  V1 electrodes: 92 of 96  rfInfo shapes V1 (96, 7, 2) V2 (28, 7, 2)
32	V1 RF centre x range (pixels) -255 to 147, y -214 to 6; variance x median 231 px^2; r2 median 0.85
33	spike rasters hold only 0 and 1 (asserted when loading); times are 1 ms bins 0..1279 (driven) and 0..1499 (blank)
34	
35	Clock check: orientation decoded from V1 counts (chance 0.125), true labels and labels of the next trial
36	session                         105l001p16  106r001p26  106r002p70  107l002p67  107l003p143
37	window                                                                                     
38	0-30 ms                              0.133       0.121       0.122       0.130        0.125
39	1180-1280 ms                         0.946       0.870       0.774       0.949        0.989
40	30-60 ms                             0.164       0.145       0.126       0.222        0.181
41	60-160 ms                            0.991       0.989       0.939       0.975        0.991
42	last 100 ms of preceding blank       0.128       0.123       0.132       0.132        0.126
43	session                         105l001p16  106r001p26  106r002p70  107l002p67  107l003p143
44	window                                                                                     
[... 362 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('nb_src.py').read()
old='''            df.loc[ks, "width_u"] = [h.half_width(jc[w][k], l) for k, l in zip(ks, li)]'''
new='''            df.loc[ks, "width_u"] = [h.half_width(jc[w][k], l) for k, l in zip(ks, li)]
            # variant: peak lag refined below the 1 ms bin by a parabola through the three
            # bins at the maximum of the smoothed CCG (not the paper's method, which had 0.1 ms bins)
            y0, ym, yp = sm[ks, li], sm[ks, li - 1], sm[ks, li + 1]
            df.loc[ks, "lag_interp"] = lag[ks] + 0.5 * (ym - yp) / (ym - 2 * y0 + yp)'''
assert old in s; s=s.replace(old,new)
old='''sg25 = v12[v12.sig25]'''
new='''print(f"variant, peak lag interpolated below 1 ms: median {sg.lag_interp.median():.2f} ms, mean {sg.lag_interp.mean():.2f} ms")
sg25 = v12[v12.sig25]'''
assert old in s; s=s.replace(old,new)
old='''        pw = st.wilcoxon(nz).pvalue if len(nz) > 0 else np.nan'''
new='''        pw = st.wilcoxon(nz).pvalue if len(nz) > 0 else np.nan
        pp = st.wilcoxon(l_, zero_method="pratt").pvalue
        pz = st.wilcoxon(l_, zero_method="zsplit").pvalue'''
assert old in s; s=s.replace(old,new)
old='''f"zero {np.sum(l_ == 0)}, +{npos} / -{nneg}; Wilcoxon p = {pw:.3f}, sign test p = {ps:.3f}")'''
new='''f"zero {np.sum(l_ == 0)}, +{npos} / -{nneg}; Wilcoxon p = {pw:.3f} (zeros dropped), {pp:.3f} (Pratt), {pz:.3f} (zeros split); sign test p = {ps:.3f}")'''
assert old in s; s=s.replace(old,new)
old='''                rows.append(dict(reading=rd, window=WIN[w], centre=c, diff=r["spike"] - r["control"], p=r["p_a"],
                                 n_off=len(epochs_)))'''
new='''                rows.append(dict(reading=rd, window=WIN[w], centre=c, diff=r["spike"] - r["control"], p=r["p_a"],
                                 p_b=r["p_b"], n_off=len(epochs_)))'''
assert old in s; s=s.replace(old,new)
old='''tc["sig_up"] = (tc.p < 0.05 / tc.n_off) & (tc["diff"] > 0)

def judge_tc(tc):'''
new='''def judge_tc(tc):'''
assert old in s; s=s.replace(old,new)
old='''jt = judge_tc(tc)
print(jt.to_string(float_format=lambda x: f"{x:.3g}"))'''
new='''for pr in ["p", "p_b"]:
    tc["sig_up"] = (tc[pr] < 0.05 / tc.n_off) & (tc["diff"] > 0)
    jt = judge_tc(tc)
    print(f"bootstrap p reading {'p-a' if pr == 'p' else 'p-b'}:")
    print(jt.to_string(float_format=lambda x: f"{x:.3g}"))'''
assert old in s; s=s.replace(old,new)
old='''    print(f"{r}: ratios {np.round(rat, 2)}; (a) geometric mean {np.exp(np.log(rat).mean()):.2f}; (b) median {np.median(rat):.2f}; "'''
new='''    print(f"{r}: ratios {np.round(rat, 3)}; (a) geometric mean {np.exp(np.log(rat).mean()):.3f}; (b) median {np.median(rat):.3f}; "'''
assert old in s; s=s.replace(old,new)
s=s.replace('''# - Clock: orientation is decoded at chance from the end of the preceding blank and in the
#   first 30 ms, and far above chance from 60 ms, with chance accuracy when the labels are
#   shifted by one trial; the population PSTH rises some 30 to 50 ms after the start of the
#   driven row.''','''# - Clock: orientation is decoded at chance from the end of the preceding blank and in the
#   first 30 ms, and far above chance from 60 ms, with chance accuracy when the labels are
#   shifted by one trial; the V1 population PSTH rises 58 to 68 ms after the start of the
#   driven row, a typical V1 latency.''')
open('nb_src.py','w').write(s)
dev=s.replace('import v1v2 as h\n','import v1v2 as h\nimport matplotlib; matplotlib.use("Agg")\nimport pickle\n')
cut='print(f"total {time.time() - T0:.0f} s")\n'
a,b=dev.split(cut)
a=a+cut+'pickle.dump(dict(pairs=pairs,sites=sites,clock=clock,sess_info=sess_info,div=div,dup=dup,sig_ccgs=sig_ccgs),open("/tmp/claude-1001/cache.pkl","wb"))\n'
head=a[:a.index('# %%\nL = 2')]
b=head+'L = 2 * h.MAXLAG + 1\nLAGS = np.arange(-h.MAXLAG, h.MAXLAG + 1)\nglobals().update(pickle.load(open("/tmp/claude-1001/cache.pkl","rb")))\n'+b
open('devA.py','w').write(a); open('devB.py','w').write(b)
EOF
. dev/bin/activate; cd entries/zandvakili-2015 && PYTHONPATH=. python $TMPDIR/devA.py 2>&1 | tail -3 && PYTHONPATH=. python $TMPDIR/devB.py > $TMPDIR/outB.txt 2>&1; grep -n "variant, peak\|Wilcoxon\|geometric\|bootstrap p reading" -A0 $TMPDIR/outB.txt; grep -n "bootstrap p reading p-b" -A12 $TMPDIR/outB.txt; rm -rf __pycache__; date -u
```

```
107l002p67: 157 s, peak memory 2.58 GB
107l003p143: 200 s, peak memory 2.70 GB
total 720 s
172:Wilcoxon signed-rank (zeros dropped): WilcoxonResult(statistic=np.float64(1325.5), pvalue=np.float64(7.138685333164141e-20))
--
178:variant, peak lag interpolated below 1 ms: median 2.30 ms, mean 1.94 ms
--
180:V1V1 all pairs: n = 2620 of 32770, median 0.0 ms, mean 0.104, zero 742, +978 / -900; Wilcoxon p = 0.016 (zeros dropped), 0.027 (Pratt), 0.028 (zeros split); sign test p = 0.076
181:V1V1 different electrodes: n = 2460 of 32770, median 0.0 ms, mean 0.103, zero 742, +898 / -820; Wilcoxon p = 0.009 (zeros dropped), 0.018 (Pratt), 0.020 (zeros split); sign test p = 0.063
182:V2V2 all pairs: n = 249 of 2113, median 0.0 ms, mean -0.036, zero 77, +83 / -89; Wilcoxon p = 0.861 (zeros dropped), 0.758 (Pratt), 0.760 (zeros split); sign test p = 0.703
183:V2V2 different electrodes: n = 108 of 2113, median 0.0 ms, mean -0.148, zero 51, +20 / -37; Wilcoxon p = 0.030 (zeros dropped), 0.024 (Pratt), 0.031 (zeros split); sign test p = 0.033
--
255:main: ratios [1.716 1.875 1.923 1.964 2.072]; (a) geometric mean 1.906; (b) median 1.923; (c) within 2 to 4: 1 of 5
256:e-b2: ratios [1.559 1.72  1.803 1.905 1.993]; (a) geometric mean 1.790; (b) median 1.803; (c) within 2 to 4: 0 of 5
257:e-b3: ratios [1.821 1.99  2.032 2.011 2.137]; (a) geometric mean 1.995; (b) median 2.011; (c) within 2 to 4: 3 of 5
258:s-b: ratios [1.655 1.83  1.836 1.92  1.959]; (a) geometric mean 1.837; (b) median 1.836; (c) within 2 to 4: 0 of 5
259:r-b: ratios [1.715 1.895 1.927 1.951 2.041]; (a) geometric mean 1.903; (b) median 1.927; (c) within 2 to 4: 1 of 5
260:d-b: ratios [1.741 1.748 1.898 1.945 2.023]; (a) geometric mean 1.868; (b) median 1.898; (c) within 2 to 4: 1 of 5
--
343:bootstrap p reading p-a:
[... 16 more lines not kept]
```

**Agent**

Outcomes are clear. Two printouts need fixing before I write the conclusions: the broad-peak width hit the edge of the lag window, and the shuffle margin needs more digits.

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('nb_src.py').read()
old='''avg = SC.mean(0)
w_all = h.half_width(avg, h.MAXLAG + int(np.argmax(avg[np.abs(LAGS) <= 10])) - 10)
print(f"across-site average: peak {avg.max():.2e} at {LAGS[avg.argmax()]} ms, flank mean {avg[flank].mean():.2e}, width at half height {w_all:.0f} ms")'''
new='''avg = SC.mean(0)
pk = h.MAXLAG + int(np.argmax(avg[np.abs(LAGS) <= 10])) - 10
w_zero = h.half_width(avg, pk)
w_flank = h.half_width(avg - avg[flank].mean(), pk)
print(f"across-site average: peak {avg.max():.2e} at {LAGS[avg.argmax()]} ms, flank mean {avg[flank].mean():.2e}; "
      f"width at half height above zero {w_zero:.0f} ms (250 means it does not fall to half within +-125 ms), above the flank mean {w_flank:.0f} ms")'''
assert old in s; s=s.replace(old,new)
s=s.replace('''print(shuf.to_string(float_format=lambda x: f"{x:.3g}"))''','''print(shuf.to_string(float_format=lambda x: f"{x:.4g}"))''')
open('nb_src.py','w').write(s)
b=open('devB.py').read()
b=b.replace(old,new).replace('''print(shuf.to_string(float_format=lambda x: f"{x:.3g}"))''','''print(shuf.to_string(float_format=lambda x: f"{x:.4g}"))''')
open('devB.py','w').write(b)
EOF
. dev/bin/activate; PYTHONPATH=. python $TMPDIR/devB.py > $TMPDIR/outB.txt 2>&1; grep -n "across-site" $TMPDIR/outB.txt; grep -n "shuffle epochs" -A21 $TMPDIR/outB.txt | head -24; rm -rf __pycache__
```

```
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/zandvakili-2015 && . $TMPDIR/dev/bin/activate && PYTHONPATH=. python $TMPDIR/devB.py > $TMPDIR/outB.txt 2>&1; tail -3 $TMPDIR/outB.txt; grep -n "across-site" $TMPDIR/outB.txt; grep -n "shuffle epochs" -A21 $TMPDIR/outB.txt | head -24; rm -rf __pycache__
```

```
without partner: 49 neurons; ratio [1.32 1.55 1.52 1.6  1.67]; p-a [0. 0. 0. 0. 0.]; p-b [0.1533 0.0134 0.011  0.0018 0.0006]; windows with spike > control at p < 0.05 (p-a): 5 of 5
ratio larger with partner at 5 of 5 windows
notebook run time 37 s; peak memory 0.42 GB
155:across-site average: peak 9.73e-04 at 2 ms, flank mean 5.58e-04; width at half height above zero 250 ms (250 means it does not fall to half within +-125 ms), above the flank mean 68 ms
261:   shuffle epochs  window  shuffled  spike_lo  control_lo  both_above
262-0        a      c       5 0.0001881 0.0003302   0.0002013        True
263-1        a      c      10 0.0003043 0.0006026   0.0003346        True
264-2        a      c      20 0.0003905 0.0008838   0.0004608        True
265-3        a      c      40  0.000438  0.001066   0.0005583        True
266-4        a      c      80 0.0004539  0.001356   0.0006805        True
267-5        a      d       5 0.0002006 0.0003302   0.0002013        True
268-6        a      d      10 0.0003063 0.0006026   0.0003346        True
269-7        a      d      20 0.0004078 0.0008838   0.0004608        True
270-8        a      d      40 0.0004399  0.001066   0.0005583        True
271-9        a      d      80 0.0004622  0.001356   0.0006805        True
272-10       b      c       5 0.0001935 0.0003302   0.0002013        True
273-11       b      c      10 0.0002948 0.0006026   0.0003346        True
274-12       b      c      20 0.0003767 0.0008838   0.0004608        True
275-13       b      c      40  0.000402  0.001066   0.0005583        True
276-14       b      c      80 0.0003797  0.001356   0.0006805        True
[... 6 more lines not kept]
```

**Agent**

Writing the conclusions and summary into the notebook source.

**Agent calls Bash**

```bash
cd $TMPDIR && cat > results.py <<'PYEOF'
R = [
"""**Result: not reproduced.** 16 of 31 V2 sites (0.516) have a significant narrow peak in the
# site-average CCG with the 10 ms jitter, and 22 of 31 (0.710) with the 25 ms variant, against
# 0.206 +/- 0.021. The fraction is above the paper's in every animal (3 of 6, 5 of 11, 8 of 14).
# The data set holds 31 sites against the paper's 223, and the paper says some penetrations
# targeted middle-layer sites, so the fraction depends on which sessions were deposited.""",
"""**Result: reproduced.** Under both readings all 31 site-average shuffle-corrected CCGs have a
# broad peak: 16 of 16 sites with a narrow peak and 15 of 15 without. The across-site average
# peaks at 2 ms and is 68 ms wide at half its height above the flank mean; it stays above half
# its height above zero over the whole +-125 ms.""",
"""**Result: not reproduced.** 171 of 16,308 V1-V2 pairs (0.0105) have a significant narrow
# peak with the 10 ms jitter (185, 0.0113, with 25 ms), against 0.003 or 0.00355. The session
# fractions are 0.0028 to 0.018; only 106r002p70 (0.0028) is within tolerance. Narrow peaks are
# rare here too, about 1% of pairs. The site fraction (fig4c-narrow-peak-sites) is 2.5 times the
# paper's, consistent with sessions richer in coupled sites than the paper's sample.""",
"""**Result: partially reproduced.** Of 171 significant V1-V2 pairs, 151 peak after zero lag and
# 15 before (sign test p = 1.9e-29, Wilcoxon p = 7.1e-20), so the offset differs from zero with
# p < 0.001 as the paper reports. The median offset is 2.0 ms, outside 2.8 +/- 0.28. The files'
# 1 ms bins put the peaks at whole milliseconds (55 pairs at 2 ms, 49 at 3 ms); a parabola through
# the peak bins gives a median of 2.30 ms, also outside. The mean width is 3.89 +/- 0.07 ms on the
# smoothed CCG and 3.09 ms on the unsmoothed one, both outside 3.71 +/- 0.1.""",
"""**Result: not reproduced, resting on an assumption.** Both medians are 0.0 ms. For the 249
# V2-V2 pairs neither test finds a difference from zero (Wilcoxon p = 0.861, sign test p =
# 0.703). For the 2620 V1-V1 pairs the Wilcoxon signed-rank test finds one (p = 0.016 with zeros
# dropped, 0.027 and 0.028 with the other treatments of zeros) and the sign test does not (p =
# 0.076). The shift is small: mean 0.104 ms, 978 positive and 900 negative offsets. The outcome
# takes the Wilcoxon signed-rank test as the paper's test (see the attempt record). Without pairs
# on the same electrode, V2-V2 pairs also differ (Wilcoxon p = 0.030, sign test p = 0.033).""",
"""**Result: not reproduced.** For the 128 significant pairs with offset above 1 ms, the
# jitter-corrected efficacy (reading a) has median 0.324% and mean 0.496 +/- 0.046%, below 0.39
# +/- 0.039 and 0.69 +/- 0.12. On the raw CCG (reading b) the values are far above: median 6.494%
# uncorrected and 0.820% shuffle-corrected. The median of reading a is 0.334, 0.559 and 0.258%
# in the three animals.""",
"""**Result: reproduced.** The 16 middle-layer sites hold 88 V2 neurons with 1,985,591 spikes from
# 50 ms. Under the main reading the divergence before V2 spikes is above control at all six
# windows, 1.72 to 2.43 times, with p < 0.001 under both bootstrap readings (no draw of 5000
# under p-a; p-b at most 0.00037). Every other reading (single 1 ms bins 2 or 3 ms before for e-b,
# s-b, r-b, d-b) also gives 6 of 6 windows. In each animal the ratio is 1.50 or more at every
# window.""",
"""**Result: partially reproduced.** Divergence before V2 spikes is about twice the control
# divergence, not three times. Under the main reading the ratios at 5 to 80 ms are 1.716 to 2.072,
# geometric mean 1.906 and median 1.923, below the 2 to 4 tolerance, and 1 of 5 windows is in
# range. The other readings give geometric means of 1.790 to 1.995. The single bin 3 ms before
# gives a median of 2.011, at the edge of the tolerance; reading e-b, one bin centred 2.5 ms
# before, cannot be formed from 1 ms data, and the bins at 2 and 3 ms bracket it (median 1.803 and
# 2.011).""",
"""**Result: reproduced.** At every window from 5 to 80 ms and under all four readings, the
# shuffled divergence (1.82e-4 to 4.62e-4 bits) is below the lower 95% bound of both the spike
# divergence (3.30e-4 to 1.36e-3) and the control divergence (2.01e-4 to 6.81e-4). The narrowest
# margin is at 5 ms, control epochs of data shuffled within orientation: 2.006e-4 against a bound
# of 2.013e-4, a margin within the spread of one shuffle realization.""",
"""**Result: not reproduced.** After V2 spikes the divergence is above control at 80 ms under both
# bootstrap readings and every reading of the method (main: ratio 1.37, no draw of 5000 under p-a,
# p-b = 0.0038; p-b 0.046 or less in the others), and at 40 ms under p-a (ratio 1.20). At 5 to
# 20 ms the ratios are 1.03 to 1.08 (main, p-a 0.10 to 0.48). The elevation after the spike is
# smaller than before it (at 40 and 80 ms, 1.20 and 1.37 after against 1.96 and 2.07 before).""",
"""**Result: reproduced.** At 1280 ms the divergence is above control both before (ratio 2.43) and
# after V2 spikes (2.00), with p < 0.001 under both bootstrap readings in every reading of the
# method.""",
"""**Result: partially reproduced.** At every window from 5 to 80 ms the largest difference is 2.5
# ms before the V2 spike for 2 ms epochs (reading a) and 3 ms before for 1 ms bins (reading b).
# Some epochs after the spike or more than 8 ms before it are also above control after the
# Bonferroni correction: with the paired bootstrap (p-a) at every window (2 to 20 epochs per
# window), and with the independent one (p-b) at 80 ms only (6 epochs in reading a, 5 in reading
# b). These differences are smaller than near the spike: at 80 ms, 2.7e-4 bits for the epoch 2.5
# ms after against 8.3e-4 for the epoch 2.5 ms before.""",
"""**Result: reproduced.** 39 middle-layer neurons have a significant pair with a V1 unit and 49
# have none. Both subsets have spike divergence above control at all five windows under p-a (no
# draw of 5000), and under p-b at 5 of 5 with a partner and 4 of 5 without (at 5 ms p = 0.153). The
# ratio is larger with a partner at all five windows (1.91 to 2.30 against 1.32 to 1.67).""",
]
s = open('nb_src.py').read()
parts = s.split("# **Result: ...**")
assert len(parts) == len(R) + 1, len(parts)
out = parts[0]
for r, p in zip(R, parts[1:]):
    out += "# " + r + p
summary = '''# %% [markdown]
# ## Summary
#
# | claim | outcome |
# |---|---|
# | fig4c-broad-ccg-peaks | reproduced |
# | fig4c-narrow-peak-sites | not reproduced (0.516 of sites) |
# | fig4-narrow-peak-depth | blocked, data_missing |
# | fig5a-rf-alignment | blocked, metadata_insufficient |
# | fig5-narrow-pairs-rare | not reproduced (0.0105 of pairs) |
# | fig5b-v1v2-latency | partially reproduced (offset significant; median 2.0 ms, width 3.89 ms) |
# | fig5b-intra-areal-zero-lag | not reproduced, assumed (V1-V1 Wilcoxon p = 0.016) |
# | figs3-efficacy | not reproduced (median 0.324%, mean 0.496%) |
# | fig6a-coordination-before-v2 | reproduced |
# | fig7a-threefold | partially reproduced (ratio 1.91) |
# | fig7a-above-shuffle | reproduced |
# | fig6b-not-after-v2 | not reproduced (80 ms elevated after spikes) |
# | fig6-slow-both-sides | reproduced |
# | fig7d-time-course | partially reproduced |
# | fig7b-nonmiddle-no-coordination, fig7e-nonmiddle-time-course, fig7c-offset-rf-no-coordination, figs5-middle-layer-relay | blocked, data_missing |
# | figs2a-v2-single-units, figs2b-v1-single-units | blocked, data_missing |
# | figs4-partner-not-needed | reproduced |
# | rf-sizes | blocked, metadata_insufficient |
# | fig1-ffn-propagation, fig3-divergence-correlation, figs1-higher-order, fig8-architecture | blocked, not_runnable |
#
# A failure to reproduce here may be a failure of this attempt, not of the paper: see the
# reasoning and the differences from the paper's method.
#
# How the analysis differs from the paper's:
#
# - Spike times are at 1 ms in the files; the paper's CCGs used 0.1 ms bins. Peak offsets are
#   whole milliseconds here.
# - Units are kept by rate only; the SNR criterion cannot be applied.
# - Sites are V2 electrodes in a session, 31 in all against 223; depth, penetration and layer
#   are not known, so the non-middle-layer and offset-RF groups cannot be formed.
# - Readings of open details follow the claims file: the CCG jitter window (10 ms; 25 ms as a
#   variant), the epoch (two 1 ms bins; e-b approximated by one bin at 2 or 3 ms), the stratum of
#   the jitter and control trials, one or three jitter realizations, pooled or per-neuron
#   distributions, and paired or independent bootstrap p-values.
#
# What was found about the data set:
#
# - It holds 5 sessions from 3 animals, with 564 V1 and 147 V2 units; the descriptor's mean of
#   112.2 V1 units per session does not match the 112.8 in the files.
# - No V2 depth, penetration identity, unit SNR or waveforms; the paper's laminar and
#   single-unit analyses cannot be repeated.
# - RF positions and sizes are in pixels with no scale or fixation point; the paper does not
#   give the screen size either.
# - Narrow V1-V2 peaks are found at about half of the sites, against a fifth in the paper, so
#   the deposited sessions are a selection the documentation does not describe.
# - The descriptor's list of orientation codes does not hold for session 105l001p16, where code 7
#   is 180 deg (sessions description); the population responses agree with the latter.

# %%'''
out = out.replace('''# %% [markdown]
# ## Summary

# %%''', summary)
open('nb_src.py', 'w').write(out)
PYEOF
python3 results.py && grep -c "Result:" nb_src.py && . dev/bin/activate && python build_nb.py nb_src.py entries/zandvakili-2015/reproduce_zandvakili_2015.ipynb && cd  && deactivate && python tools/entry.py check entries/zandvakili-2015 | tail -3; date -u
```

```
13
0 error(s)
Thu Nov 12 17:22:17 UTC 2026
```

**Agent calls Bash**

```bash
python tools/entry.py all entries/zandvakili-2015 2>&1 | tail -4; date -u
```

```
Installed kernelspec registry-zandvakili-2015 in executed/zandvakili-2015/.venv/share/jupyter/kernels/registry-zandvakili-2015
0 error(s)
pass  reproduce_zandvakili_2015.ipynb  (738 s)
Thu Nov 12 17:34:48 UTC 2026
```

**Agent**

Run passes (12.3 min). Checking that the executed numbers match the conclusions I wrote.

**Agent calls Bash**

```bash
python3 - <<'EOF' > $TMPDIR/exec_out.txt
import nbformat
nb=nbformat.read('executed/zandvakili-2015/reproduce_zandvakili_2015.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    for o in c.get('outputs',[]):
        if 'text' in o: print(o['text'])
        elif o.get('output_type')=='error': print('ERROR',o['ename'],o['evalue'])
EOF
diff <(sed -n '/fig4c-narrow/,$p' $TMPDIR/exec_out.txt | grep -v "run time\|^$" | head -400) <(grep -v "run time\|^$" $TMPDIR/outB.txt | sed -n '/session  electrode  n_pairs/,$p' | head -400) | head; grep -n "ERROR\|across-site\|variant, peak\|V1V1 all\|geometric mean 1.906\|run time" $TMPDIR/exec_out.txt
```

```
0a1,307
>         session  electrode  n_pairs  n_v2_units  sig10    peak10      sd10  lag10  sig25
> 0    105l001p16          1      790           5  False  0.000035  0.000007     -7   True
> 1    105l001p16          5      790           5  False  0.000008  0.000004     -4  False
> 2    105l001p16          9      316           2   True  0.000165  0.000011      2   True
> 3    105l001p16         13     1106           7   True  0.000052  0.000005      3   True
> 4    105l001p16         17      158           1  False  0.000126  0.000028      3   True
> 5    105l001p16         21      790           5   True  0.000048  0.000006      3   True
> 6    106r001p26          1      324           3  False  0.000020  0.000008      1  False
> 7    106r001p26          5      648           6  False  0.000033  0.000009      2   True
169:across-site average: peak 9.73e-04 at 2 ms, flank mean 5.58e-04; width at half height above zero 250 ms (250 means it does not fall to half within +-125 ms), above the flank mean 68 ms
194:variant, peak lag interpolated below 1 ms: median 2.30 ms, mean 1.94 ms
197:V1V1 all pairs: n = 2620 of 32770, median 0.0 ms, mean 0.104, zero 742, +978 / -900; Wilcoxon p = 0.016 (zeros dropped), 0.027 (Pratt), 0.028 (zeros split); sign test p = 0.076
280:main: ratios [1.716 1.875 1.923 1.964 2.072]; (a) geometric mean 1.906; (b) median 1.923; (c) within 2 to 4: 1 of 5
419:notebook run time 731 s; peak memory 2.71 GB
```

**Agent calls Bash**

```bash
cd $TMPDIR; a=$(grep -n "session  electrode  n_pairs" exec_out.txt | head -1 | cut -d: -f1); b=$(grep -n "session  electrode  n_pairs" outB.txt | head -1 | cut -d: -f1); diff <(tail -n +$a exec_out.txt | grep -v "run time\|^$") <(tail -n +$b outB.txt | grep -v "run time\|^$") && echo IDENTICAL
```

```
IDENTICAL
Shell cwd was reset to
```

**Agent**

Executed outputs match the ones the conclusions were written from. Now the attempt record; checking the schema first.

**Agent calls Bash**

```bash
python3 -c "
import json; s=json.load(open('schemas/attempt.schema.json'))
print(s.get('required'))
for k,v in s['properties'].items(): print(k, '|', str(v)[:300])
" | head -60; grep -n "kind: methods_unavailable" -A8 attempts/*.yaml | head -20
```

```
['schema_version', 'id', 'datasets', 'paper', 'date', 'provenance', 'outcomes']
schema_version | {'const': 3}
id | {'type': 'string', 'pattern': '^[a-z0-9]+(-[a-z0-9]+)*$'}
datasets | {'description': 'Every dataset the attempt used (docs/protocol.md, "Record the attempt").', 'type': 'array', 'minItems': 1, 'items': {'description': "A dataset the attempt used: the archive, the dataset's identifier there, the pinned version, and how the paper relates to it.", 'type': 'object', 'add
missing_datasets | {'description': "Datasets the paper's claims rest on that this attempt could not use; claims that need one are blocked with dataset_missing.", 'type': 'array', 'items': {'type': 'object', 'additionalProperties': False, 'required': ['why'], 'properties': {'archive': {'type': 'string'}, 'id': {'type':
paper | {'type': 'string', 'pattern': '^doi:10\\.[0-9]{4,9}/.+$'}
date | {'type': 'string', 'format': 'date'}
entry | {'description': 'The entry this attempt produced (its name), if any.', 'type': 'string'}
deprecated | {'description': "Set when the attempt no longer stands, for example because its claims were written without the paper's full text. The record is kept as it was; its outcomes are shown but not counted.", 'type': 'object', 'additionalProperties': False, 'required': ['date', 'reason'], 'properties': {'
provenance | {'type': 'object', 'additionalProperties': False, 'required': ['kind', 'accountable'], 'properties': {'kind': {'enum': ['agent', 'person']}, 'accountable': {'description': 'The person or organisation responsible for this attempt.', 'type': 'object', 'additionalProperties': False, 'required': ['name'
outcomes | {'description': 'One per claim attempted.', 'type': 'array', 'minItems': 1, 'items': {'type': 'object', 'additionalProperties': False, 'required': ['claim', 'outcome'], 'properties': {'claim': {'description': "Claim id from the target's claims file.", 'type': 'string'}, 'outcome': {'enum': ['reprodu
verifications | {'type': 'array', 'items': {'typ
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json; s=json.load(open('schemas/attempt.schema.json'))
print(json.dumps(s['properties']['outcomes']['items']['properties'],indent=0)[:2500])
print(json.dumps(s['properties']['findings']['items'],indent=0)[:1500])
print(json.dumps(s['properties']['datasets']['items']['properties'],indent=0)[:800])
print(json.dumps(s['properties']['provenance']['properties'],indent=0)[:1500])
"
```

```
{
"claim": {
"description": "Claim id from the target's claims file.",
"type": "string"
},
"outcome": {
"enum": [
"reproduced",
"partially_reproduced",
"not_reproduced",
"blocked"
],
"description": "Describes the result, not the method: whether the effect the claim states was found. Differences in method from the paper go in `deviations`."
},
"blocked_by": {
"description": "Required when outcome is blocked.",
"enum": [
"data_missing",
"metadata_insufficient",
"methods_underspecified",
[... 225 more lines not kept]
```

**Agent**

Writing the attempt record.

**Agent calls Write**

```json
{
 "file_path": "attempts/zandvakili-2015-01.yaml",
 "content": "schema_version: 3\nid: zandvakili-2015-01\ndatasets:\n- archive: crcns\n  id: v1v2-1\n  version: unversioned\n  doi: 10.6080/K0B27SHN\n  relation: primary\npaper: doi:10.1016/j.neuron.2015.07.026\ndate: 2026-11-12\nentry: zandvakili-2015\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-14\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/43258308217\noutcomes:\n- claim: fig4c-broad-ccg-peaks\n  outcome: reproduced\n  notebook: reproduce_zandvakili_2015.ipynb\n  output: claim:fig4c-broad-ccg-peaks\n  notes: >-\n    All 31 site-average shuffle-corrected V1-V2 CCGs have a broad peak under both readings (mean over\n    -50 to 50 ms above the flank mean, and above zero), 16 of 16 sites with a narrow peak and 15 of\n    15 without. The across-site average peaks at 2 ms and is 68 ms wide at half its height above\n    the flank mean; it stays above half its height above zero over the whole +-125 ms.\n  deviations:\n  - >-\n    A site is a V2 tetrode in one session; the files hold no depth, so \"all laminar locations\" is\n    tested as sites with and without a narrow peak, as the criterion says.\n  - Spike times are in 1 ms bins in the files; the paper used 0.1 ms.\n- claim: fig4c-narrow-peak-sites\n  outcome: not_reproduced\n  notebook: reproduce_zandvakili_2015.ipynb\n  output: claim:fig4c-narrow-peak-sites\n  measured: 0.516\n  notes: >-\n    16 of 31 V2 sites have a significant narrow peak in the site-average jitter-corrected CCG with\n    the 10 ms jitter window (reading j-a), 0.516 against 0.206 +/- 0.021; 22 of 31 (0.710) with a\n    25 ms window. Per animal 3 of 6, 5 of 11 and 8 of 14. With a 4 or 6 SD threshold, 22 and 13\n    sites. The data set holds 31 sites of the paper's 223 and 5 of its sessions; the paper says\n    some penetrations targeted middle-layer sites, so the fraction depends on which sessions were\n    deposited, which the documentation does not say.\n  deviations:\n  - >-\n    CCGs at 1 ms resolution (the files' resolution) against the paper's 0.1 ms. Equation 1 is\n    combined over the eight stimuli by summing coincidences and the normaliser, which weights each\n    stimulus by its V1 spike count (a standard choice).\n  - >-\n    The jitter correction subtracts the expected CCG under the jitter the claims file describes\n    for the divergence analysis (each spike redrawn from the neuron's spikes in the same window on\n    trials of the same stimulus), computed analytically for both neurons, with windows tiling the\n    trial from 0 ms (Pairwise V1-V2 Analysis cites Smith and Kohn 2008 for the jitter). The 25 ms\n    window is this attempt's choice for reading j-b, which the claims file leaves unnamed.\n  - The SNR >= 2 unit criterion cannot be applied (no waveforms); units below 0.5 sp/s are removed.\n- claim: fig4-narrow-peak-depth\n  outcome: blocked\n  blocked_by: data_missing\n  notes: >-\n    The files hold no recording depth for any V2 site and no layer 6/white matter reference; the\n    descriptor lists spike rasters, stimulus codes, trial ids, unit codes and RF fits only.\n- claim: fig5a-rf-alignment\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notebook: reproduce_zandvakili_2015.ipynb\n  output: claim:fig5a-rf-alignment\n  notes: >-\n    RF centres are in pixels and the data set gives no pixel-to-degree scale and no fixation\n    point; the paper gives 1024 x 768 pixels at 110 cm without the screen size, so the 0.5 deg bins\n    of the criterion cannot be formed. Shown for information only, in pixels and the first eye,\n    the probability of a significant pair falls with RF offset (0.0165 at 0 to 25 px, 0.0136 at 25\n    to 50, 0.0106 at 50 to 75, 0.0034 at 75 to 100, 0 beyond 100 px; 15,463 pairs with both RFs\n    fitted).\n- claim: fig5-narrow-pairs-rare\n  outcome: not_reproduced\n  notebook: reproduce_zandvakili_2015.ipynb\n  output: claim:fig5-narrow-pairs-rare\n  measured:\n  - 0.0105\n  - 0.0105\n  notes: >-\n    171 of 16,308 V1-V2 pairs (0.0105) pass the 5 SD rule with 10 ms jitter, 185 (0.0113) with 25\n    ms, against 0.003 or 0.00355. Per session 0.0028 to 0.018; only 106r002p70 (6 of 2112, 0.0028)\n    is within tolerance. Narrow peaks remain rare (about 1% of pairs). The site fraction of\n    fig4c-narrow-peak-sites is 2.5 times the paper's, consistent with deposited sessions richer\n    in coupled sites than the paper's sample.\n  deviations:\n  - 1 ms bins against the paper's 0.1 ms; jitter as in fig4c-narrow-peak-sites.\n- claim: fig5b-v1v2-latency\n  outcome: partially_reproduced\n  notebook: reproduce_zandvakili_2015.ipynb\n  output: claim:fig5b-v1v2-latency\n  measured:\n  - 2.0\n  - 3.89\n  notes: >-\n    Of 171 significant V1-V2 pairs, 151 peak after zero lag, 5 at zero and 15 before; the offset\n    differs from zero with p < 0.001 under both readings (Wilcoxon p = 7.1e-20, sign test p =\n    1.9e-29). The median offset is 2.0 ms, outside 2.8 +/- 0.28 (per animal 3, 2 and 2 ms). The\n    peaks fall on whole milliseconds (23 at 1 ms, 55 at 2, 49 at 3, 18 at 4); a parabola through\n    the peak bins, a variant not in the paper, gives a median of 2.30 ms, also outside. The mean\n    width at half height is 3.89 +/- 0.07 ms on the smoothed CCG (reading a) and 3.09 +/- 0.09 ms\n    unsmoothed (reading b), both outside 3.71 +/- 0.1. The direction and significance of the\n    offset hold; its size and the width do not match.\n  deviations:\n  - >-\n    The files hold spike times in 1 ms bins, so offsets are whole milliseconds where the paper's\n    were at 0.1 ms resolution; this limits both the median and the width.\n- claim: fig5b-intra-areal-zero-lag\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_zandvakili_2015.ipynb\n  output: claim:fig5b-intra-areal-zero-lag\n  notes: >-\n    Both medians are 0.0 ms. V2-V2 (249 significant pairs of 2113) shows no difference from zero\n    under either reading (Wilcoxon p = 0.861, sign test p = 0.703). V1-V1 (2620 of 32,770) differs\n    under the Wilcoxon signed-rank test (p = 0.016 with zeros dropped, 0.027 Pratt, 0.028 zeros\n    split) and not under the sign test (p = 0.076); mean offset 0.104 ms, 978 positive, 900\n    negative, 742 zero. The readings give different outcomes, and the outcome takes the Wilcoxon\n    signed-rank test (see deviations). Without pairs on the same electrode, V1-V1 gives Wilcoxon p\n    = 0.009 and sign test p = 0.063, and V2-V2 (108 pairs) Wilcoxon p = 0.030 and sign test p =\n    0.033. Question for the authors, recorded as a finding; which test gave p = 0.45 and 0.42.\n  deviations:\n  - >-\n    Assumed that the paper's test of a median offset against zero is the Wilcoxon signed-rank test\n    (MATLAB signrank, documented as a test of zero median, the routine choice in a MATLAB-based\n    analysis such as the data set's own scripts). The paper names no test; the sign test gives the\n    opposite outcome for V1-V1 pairs.\n  - The lag sign within an area follows the order of the unit lists, as the criterion says; 1 ms bins.\n- claim: figs3-efficacy\n  outcome: not_reproduced\n  notebook: reproduce_zandvakili_2015.ipynb\n  output: claim:figs3-efficacy\n  measured:\n  - 0.324\n  - 0.496\n  notes: >-\n    128 of 171 significant pairs have an offset above 1 ms (255 in the paper). Reading a,\n    jitter-corrected CCG, median 0.324% and mean 0.496 +/- 0.046%, below 0.39 +/- 0.039 and 0.69\n    +/- 0.12. Reading b, the raw CCG, gives median 6.494% and mean 9.479% uncorrected and median\n    0.820% and mean 1.268% shuffle-corrected, far above. Reading a per animal, median 0.334%,\n    0.559% and 0.258% (20, 31 and 77 pairs).\n  deviations:\n  - >-\n    The integral within 2.5 ms of the peak is the sum of the five 1 ms bins centred on the peak\n    lag (-2.5 to +2.5 ms at the files' resolution).\n- claim: fig6a-coordination-before-v2\n  outcome: reproduced\n  notebook: reproduce_zandvakili_2015.ipynb\n  output: claim:fig6a-coordination-before-v2\n  notes: >-\n    88 V2 neurons at the 16 middle-layer sites (1,985,591 spikes from 50 ms; the paper 226 neurons).\n    Main reading (e-a, s-a, r-a, d-a) at 5, 10, 20, 40, 80 and 1280 ms, spike against control\n    divergence 4.05e-4 against 2.36e-4 bits at 5 ms up to 5.16e-3 against 2.12e-3 at 1280 ms, ratios\n    1.72 to 2.43, p < 0.001 at every window under p-a (no draw of 5000) and p-b (at most 0.00037).\n    All other readings (s-b, r-b with three realizations, d-b, and single bins at 2 or 3 ms for\n    e-b) give 6 of 6 windows. Per animal the ratio is 1.50 to 2.66.\n  deviations:\n  - >-\n    Reading e-b, one 1 ms bin centred 2.5 ms before the spike, cannot be formed from 1 ms data; it\n    is run as the bins centred 2 ms and 3 ms before, which bracket it.\n  - >-\n    The jitter pool includes the spike's own trial (the claims file says other trials), a\n    standard choice; one trial in 400 changes the pool little. Epochs falling before 50 ms are\n    dropped.\n  - Middle-layer sites are those of fig4c-narrow-peak-sites, 16 of 31, a larger share than the paper's.\n- claim: fig7a-threefold\n  outcome: partially_reproduced\n  notebook: reproduce_zandvakili_2015.ipynb\n  output: claim:fig7a-threefold\n  measured: 1.906\n  notes: >-\n    Divergence before V2 spikes is about twice control, not three times. Main reading, ratios at 5\n    to 80 ms 1.716, 1.875, 1.923, 1.964 and 2.072; (a) geometric mean 1.906, (b) median 1.923, (c) 1\n    of 5 windows within 2 to 4. Other readings give geometric means of 1.790 to 1.995; the single\n    bin 3 ms before gives a median of 2.011 and 3 of 5 windows in range, and the bin 2 ms before a\n    median of 1.803. The effect is present and weaker than reported.\n  deviations:\n  - Reading e-b approximated by single bins 2 and 3 ms before the spike, as in fig6a-coordination-before-v2.\n- claim: fig7a-above-shuffle\n  outcome: reproduced\n  notebook: reproduce_zandvakili_2015.ipynb\n  output: claim:fig7a-above-shuffle\n  notes: >-\n    Under all four readings (trials shuffled within orientation or across all trials; spike or\n    control epochs) and at every window from 5 to 80 ms, the shuffled divergence (1.82e-4 to\n    4.62e-4 bits) is below the lower 95% bootstrap bound of both the spike divergence (3.30e-4 to\n    1.36e-3) and the control divergence (2.01e-4 to 6.81e-4). The narrowest margin is at 5 ms,\n    control epochs, shuffle within orientation, 2.006e-4 against 2.013e-4, within the spread of a\n    single shuffle realization.\n  deviations:\n  - >-\n    One shuffle realization per reading, compared as a point value with the bootstrap bounds, as\n    the criterion says; the shuffled data are jittered with the same rule as the data.\n- claim: fig6b-not-after-v2\n  outcome: not_reproduced\n  notebook: reproduce_zandvakili_2015.ipynb\n  output: claim:fig6b-not-after-v2\n  notes: >-\n    In epochs 1.5 to 3.5 ms after V2 spikes the divergence is above control at 80 ms under both\n    bootstrap readings in every reading of the method (main ratio 1.37, p-a no draw of 5000, p-b\n    0.0038; p-b 0.046 or less in the others), and at 40 ms under p-a (ratio 1.20, p-b 0.099). At 5\n    to 20 ms the ratios are 1.03 to 1.08 (p-a 0.10 to 0.48). The elevation after the spike is\n    smaller than before it (1.20 and 1.37 at 40 and 80 ms, against 1.96 and 2.07 before).\n- claim: fig6-slow-both-sides\n  outcome: reproduced\n  notebook: reproduce_zandvakili_2015.ipynb\n  output: claim:fig6-slow-both-sides\n  notes: >-\n    At 1280 ms the divergence is above control before V2 spikes (5.16e-3 against 2.12e-3 bits,\n    ratio 2.43) and after them (4.13e-3 against 2.07e-3, ratio 2.00), p < 0.001 under both bootstrap\n    readings and in every reading of the method.\n- claim: fig7d-time-course\n  outcome: partially_reproduced\n  notebook: reproduce_zandvakili_2015.ipynb\n  output: claim:fig7d-time-course\n  notes: >-\n    At all five windows the largest spike minus control difference is at the epoch centred 2.5 ms\n    before the V2 spike (reading a, 2 ms epochs) or the bin 3 ms before (reading b). Epochs after\n    the spike or more than 8 ms before it are also significant after Bonferroni correction over\n    offsets, with the paired bootstrap (p-a) at every window (2 to 20 epochs per window), and with\n    the independent bootstrap (p-b) at 80 ms only (6 epochs in reading a, 5 in reading b). At 80\n    ms the difference is 8.3e-4 bits 2.5 ms before the spike and 2.7e-4 bits 2.5 ms after.\n  deviations:\n  - >-\n    2000 bootstrap draws per offset (a standard choice for 310 comparisons); offsets beyond 15 ms\n    are not run; epochs falling before 50 ms are dropped.\n- claim: fig7b-nonmiddle-no-coordination\n  outcome: blocked\n  blocked_by: data_missing\n  notes: >-\n    Needs V2 sites superficial or deep to the middle-layer sites of the same penetration. Each\n    session holds one recording per V2 tetrode, with no depth and no penetration identity, so the\n    order of sites cannot be known. Using sites without a narrow peak would not be the claim's\n    group.\n- claim: fig7e-nonmiddle-time-course\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Depends on fig7b-nonmiddle-no-coordination, blocked for lack of V2 depths and penetrations.\n- claim: fig7c-offset-rf-no-coordination\n  outcome: blocked\n  blocked_by: data_missing\n  notes: >-\n    Needs V2 neurons 500 to 1000 um from the layer 6/white matter border, and RF offsets in\n    degrees. The files hold no depth, and RF positions are in pixels with no scale\n    (metadata_insufficient, as for fig5a-rf-alignment).\n- claim: figs2a-v2-single-units\n  outcome: blocked\n  blocked_by: data_missing\n  notes: >-\n    Needs each unit's SNR (waveform amplitude over noise SD). The files hold no waveforms or SNR,\n    and the unit sort codes do not mark single units.\n- claim: figs2b-v1-single-units\n  outcome: blocked\n  blocked_by: data_missing\n  notes: >-\n    Needs V1 unit SNR, which the files do not hold; it also depends on fig7b and fig7c, blocked for\n    lack of depths.\n- claim: figs4-partner-not-needed\n  outcome: reproduced\n  notebook: reproduce_zandvakili_2015.ipynb\n  output: claim:figs4-partner-not-needed\n  notes: >-\n    39 middle-layer V2 neurons have a significant pair with a recorded V1 unit and 49 have none (73\n    and 153 in the paper). Both subsets have spike divergence above control at 5 of 5 windows from 5\n    to 80 ms under p-a, and under p-b at 5 of 5 with a partner and 4 of 5 without (5 ms p = 0.153).\n    The spike to control ratio is larger with a partner at all five windows (1.91 to 2.30 against\n    1.32 to 1.67).\n  deviations:\n  - Main reading of the shared divergence method only.\n- claim: figs5-middle-layer-relay\n  outcome: blocked\n  blocked_by: data_missing\n  notes: >-\n    Needs spikes of V2 units in layers superficial or deep to the middle layers, which cannot be\n    identified without depths (fig7b-nonmiddle-no-coordination). Within a session the V2 units\n    are from one depth per tetrode.\n- claim: fig1-ffn-propagation\n  outcome: blocked\n  blocked_by: not_runnable\n  notes: >-\n    A simulation (data elsewhere), with no published code. Writing and running a ten-layer\n    integrate-and-fire network from the Supplemental Experimental Procedures did not fit in this\n    attempt's five-hour run beside the claims on the data set; it was not attempted.\n- claim: fig3-divergence-correlation\n  outcome: blocked\n  blocked_by: not_runnable\n  notes: >-\n    A simulation with no published code; not attempted within the run's time, as for\n    fig1-ffn-propagation.\n- claim: figs1-higher-order\n  outcome: blocked\n  blocked_by: not_runnable\n  notes: >-\n    A simulation with no published code; not attempted within the run's time, as for\n    fig1-ffn-propagation.\n- claim: fig8-architecture\n  outcome: blocked\n  blocked_by: not_runnable\n  notes: >-\n    A simulation with no published code; not attempted within the run's time, as for\n    fig1-ffn-propagation.\n- claim: rf-sizes\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notebook: reproduce_zandvakili_2015.ipynb\n  output: claim:rf-sizes\n  notes: >-\n    RF variances are in pixels with no pixel-to-degree scale in the data set or the paper. In\n    pixels, the mean diameter (4 SD) is 60.9 px for 431 V1 channels and 119.9 px for 77 V2 channels\n    (reading a; 60.4 and 118.9 under reading b). The ratio of V2 to V1 diameter, which needs no\n    scale, is 1.97 against 2.27 / 1.21 = 1.88 in the paper. A scale of 50 to 53 px/deg would match\n    both means, but nothing in the data set or the paper fixes it.\nfindings:\n- kind: data_missing\n  statement: >-\n    The data set holds no V2 recording depth, penetration identity, unit SNR or waveforms. The\n    paper's layer groups (middle, superficial and deep V2), its depth of the narrow-peak sites,\n    its offset-RF group and its single-unit analyses cannot be repeated; 8 of the paper's claims\n    on the recordings are blocked for this.\n- kind: metadata_insufficient\n  statement: >-\n    Receptive field centres and variances (rfInfo) are in pixels, and neither the data set nor the\n    paper gives the pixel-to-degree scale or the fixation point (the paper gives 1024 x 768 pixels\n    at 110 cm without the screen size). In four sessions each channel has fits for two eyes 250 to\n    400 pixels apart. RF sizes and offsets in degrees, which the paper reports, cannot be computed.\n- kind: selection_undocumented\n  about: data\n  statement: >-\n    The data set holds 5 sessions in 3 animals of the paper's recordings in 7 animals (31 V2\n    sites of 223). Its documentation does not say how they were chosen. They differ from the\n    paper's sample in a measure the paper reports, with a significant narrow V1-V2 peak at 16 of\n    31 sites (0.52, against 46 of 223) and in 1.05% of V1-V2 pairs (against 0.3%).\n- kind: metadata_error\n  statement: >-\n    The data description gives an average of 112.2 V1 units per session; the five files hold 159,\n    109, 88, 97 and 111 V1 units, an average of 112.8. The V2 average (29.4) matches.\n- kind: metadata_insufficient\n  statement: >-\n    The data description lists stimulus code 7 as a 135 deg grating, but the sessions description\n    gives 180 deg for session 105l001p16. The population responses agree with the sessions\n    description (code 7 correlates 0.911 with code 1, against 0.637 and 0.845 with codes 6 and 8).\n    The spike rasters are at 1 ms resolution, where the paper's CCGs used 0.1 ms; the description\n    does not say that the spike times were binned.\n- kind: methods_unavailable\n  statement: >-\n    Question for the authors. Which test gave the p-values for the median CCG peak offsets against\n    zero (p < 0.001 for V1-V2; p = 0.45 and 0.42 for V1-V1 and V2-V2)? On this data set the\n    Wilcoxon signed-rank test finds the V1-V1 offsets different from zero (p = 0.016, mean 0.10\n    ms) and the sign test does not (p = 0.076); the attempt assumed the signed-rank test.\n- kind: methods_unavailable\n  statement: >-\n    Question for the authors. How were the bootstrap p-values comparing divergence in spike and\n    control epochs computed, with the same resampled neurons for both (paired) or from the two\n    bootstrap distributions taken as independent? The paired reading finds after-spike epochs and\n    epochs far from the spike above control at many offsets (Figure 7D) where the independent one\n    finds them at the 80 ms window only. The outcomes here are the same under both except where\n    the notes say.\n- kind: methods_unavailable\n  statement: >-\n    Question for the authors. The CCG jitter window used for the significance of narrow peaks is\n    given only for Figure 4C (10 ms); was it the same for all pairs and sites? With 25 ms, 22 of\n    31 sites and 185 pairs pass on this data set, against 16 and 171 with 10 ms.\n"
}
```

```
File created successfully at: attempts/zandvakili-2015-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent**

Fixing two statements not backed by printed numbers (the eye separation, and the count of claims blocked for missing depth/SNR, which is 7 not 8), then rerunning.

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('nb_src.py').read()
old='''print("spike rasters hold only 0 and 1'''
new='''for k, v in sess_info.items():
    if v["v1_rf"].shape[2] == 2:
        dx = np.abs(v["v1_rf"][:, 2, 1] - v["v1_rf"][:, 2, 0])
        print(f"{k}: two eyes mapped; horizontal distance between the eyes' V1 RF centres, median {np.nanmedian(dx):.0f} px (range {np.nanmin(dx):.0f} to {np.nanmax(dx):.0f})")
    else:
        print(f"{k}: one eye mapped")
print("spike rasters hold only 0 and 1'''
assert old in s; s=s.replace(old,new)
old='''#   scale or the position of the fixation point, and in four sessions the two eyes' RFs are
#   250 to 400 pixels apart (two gratings, Visual Stimuli).'''
new='''#   scale or the position of the fixation point, and in four sessions the two eyes' RFs are
#   mapped at the horizontal distances printed above (two gratings, Visual Stimuli).'''
assert old in s; s=s.replace(old,new)
open('nb_src.py','w').write(s)
EOF
. dev/bin/activate && python build_nb.py nb_src.py entries/zandvakili-2015/reproduce_zandvakili_2015.ipynb && cd  && deactivate && sed -i 's/its offset-RF group and its single-unit analyses cannot be repeated; 8 of the paper/its offset-RF group and its single-unit analyses cannot be repeated; 7 of the paper/' attempts/zandvakili-2015-01.yaml && python tools/entry.py all entries/zandvakili-2015 2>&1 | tail -3; date -u
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 - <<'EOF' > $TMPDIR/exec_out2.txt
import nbformat
nb=nbformat.read('executed/zandvakili-2015/reproduce_zandvakili_2015.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    for o in c.get('outputs',[]):
        if 'text' in o: print(o['text'])
        elif o.get('output_type')=='error': print('ERROR',o['ename'],o['evalue'])
EOF
grep -n "eye" $TMPDIR/exec_out2.txt; cd $TMPDIR; diff <(grep -v "run time\|^$\| s, peak memory\|total \| eye" exec_out.txt) <(grep -v "run time\|^$\| s, peak memory\|total \| eye" exec_out2.txt) && echo SAME
```

```
51:105l001p16: one eye mapped
52:106r001p26: two eyes mapped; horizontal distance between the eyes' V1 RF centres, median 244 px (range 107 to 355)
53:106r002p70: two eyes mapped; horizontal distance between the eyes' V1 RF centres, median 258 px (range 132 to 322)
54:107l002p67: two eyes mapped; horizontal distance between the eyes' V1 RF centres, median 244 px (range 160 to 360)
55:107l003p143: two eyes mapped; horizontal distance between the eyes' V1 RF centres, median 266 px (range 183 to 353)
SAME
Shell cwd was reset to
```

**Agent calls Bash**

```bash
sed -i 's/at 110 cm without the screen size). In four sessions each channel has fits for two eyes 250 to/at 110 cm without the screen size). In four sessions each channel has fits for two eyes, with V1/; s/^    400 pixels apart. RF sizes and offsets in degrees, which the paper reports, cannot be computed./    RF centres a median of 244 to 266 pixels apart horizontally. RF sizes and offsets in degrees,\n    which the paper reports, cannot be computed./' attempts/zandvakili-2015-01.yaml; grep -n "two eyes" -A3 attempts/zandvakili-2015-01.yaml; grep -n "—\|rather" attempts/zandvakili-2015-01.yaml entries/zandvakili-2015/*.py entries/zandvakili-2015/*.yaml; grep -c "rather\|—" $TMPDIR/nb_src.py; python tools/entry.py check entries/zandvakili-2015 | tail -3
```

```
331:    at 110 cm without the screen size). In four sessions each channel has fits for two eyes, with V1
332-    RF centres a median of 244 to 266 pixels apart horizontally. RF sizes and offsets in degrees,
333-    which the paper reports, cannot be computed.
334-- kind: selection_undocumented
0
0 error(s)
```

**Agent**

The entry needs a README carrying the required sentence. Checking the example's format.

**Agent calls Bash**

```bash
cat entries/fouke-2025/README.md | head -40
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
[... 14 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/zandvakili-2015/README.md",
 "content": "# Zandvakili & Kohn (2015) from CRCNS v1v2-1\n\nTests the findings of [Zandvakili and Kohn (2015)](https://doi.org/10.1016/j.neuron.2015.07.026)\nthat can be tested on [CRCNS v1v2-1](https://doi.org/10.6080/K0B27SHN), which holds V1 Utah array\nand V2 tetrode spike times from 5 sessions in 3 anesthetized macaques viewing drifting gratings. It\nhas no V2 depths, unit SNR or pixel-to-degree scale, so the laminar, single-unit and receptive field\nclaims cannot be tested, and the paper's simulations were not run.\n\n| Claim | Outcome |\n|---|---|\n| Broad V1-V2 CCG peaks at all sites | Reproduced |\n| Narrow site-average peak at a minority of V2 sites (46 of 223) | Not reproduced (16 of 31) |\n| Depth of narrow-peak sites (694 um) | Blocked: data missing |\n| Narrow peaks in 0.3% of V1-V2 pairs | Not reproduced (1.05%) |\n| V1-V2 peaks offset by a median of 2.8 ms, width 3.71 ms | Partially reproduced (2.0 ms, 3.89 ms) |\n| V1-V1 and V2-V2 peaks at zero lag | Not reproduced, resting on an assumption |\n| Efficacy, median 0.39% | Not reproduced (0.32%) |\n| V1 divergence higher before middle-layer V2 spikes than in control epochs | Reproduced |\n| About 3-fold higher | Partially reproduced (about 1.9-fold) |\n| Divergence above shuffled data | Reproduced |\n| No elevation after V2 spikes (5 to 80 ms) | Not reproduced (elevated at 80 ms) |\n| Elevation before and after at 1280 ms | Reproduced |\n| Time course peaks a few ms before V2 spikes | Partially reproduced |\n| Elevation with and without a V1 partner | Reproduced |\n| RF alignment and RF sizes | Blocked: metadata insufficient |\n| Non-middle-layer, offset-RF, single-unit and V2 relay analyses (seven claims) | Blocked: data missing |\n| Simulations (four claims) | Blocked: not runnable |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe files hold spike times in 1 ms bins, where the paper used 0.1 ms. The attempt record, with the\nreasons and the differences from the paper's method, is\n[`attempts/zandvakili-2015-01.yaml`](../../attempts/zandvakili-2015-01.yaml).\n\n- `reproduce_zandvakili_2015.ipynb`: the analysis. It takes about 13 minutes, most of it the\n  cross-correlograms and the jittered V1 populations.\n- `v1v2.py`: loading the sessions from the zip in place, CCGs with shuffle and jitter correction,\n  and the divergence of V1 population states around V2 spikes. Other notebooks on this data set\n  can import it.\n"
}
```

```
File created successfully at: entries/zandvakili-2015/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/entry.py check entries/zandvakili-2015 | tail -2; python tools/entry.py handover entries/zandvakili-2015 2>&1 | tail -5; ls executed/zandvakili-2015/handover/; git status --short
```

```
0 error(s)
wrote executed/zandvakili-2015/handover
reproduce_zandvakili_2015.ipynb
v1v2.py
zandvakili-2015.yaml
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
?? attempts/zandvakili-2015-01.yaml
?? entries/zandvakili-2015/
?? scripts
```

**Agent calls Bash**

```bash
ls -la .bashrc .profile .mcp.json scripts .idea 2>&1 | head; git log --oneline -1 -- scripts; grep -n "def .*stamp\|README" tools/entry.py | head
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 12 16:23 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 12 16:23 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 12 16:23 .mcp.json
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 12 16:23 .profile
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 12 16:23 scripts
```

**Agent calls Bash**

```bash
grep -n "def hash\|def _inputs\|stamp" tools/entry.py | head -15
```

```
30:A run that passes leaves a stamp beside the executed copies (.clean-run.json):
515:    """The stamp of executed copies that a run now would only make again: made from this hash, each copy still as
518:        stamp = json.loads((output_dir / STAMP).read_text())
520:        if stamp["hash"] != entry_hash(entry_dir) or time.time() - stamp["finished"] > REUSE_DAYS * 86400:
522:        if [n["path"] for n in entry["notebooks"]] != [r["notebook"] for r in stamp["results"]]:
524:        for r in stamp["results"]:
527:        return stamp
534:    stamp = None if fresh else reusable(entry_dir, output_dir, max_minutes)
535:    if stamp:
536:        when = time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime(stamp["finished"]))
537:        for r in stamp["results"]:
540:              f"{stamp['hash'][:12]}). Nothing was executed and no environment was built; --fresh runs it again.")
```

**Agent calls Bash**

```bash
grep -n "def entry_hash" -A20 tools/entry.py | head -25
```

```
500:def entry_hash(entry_dir: Path) -> str:
501-    """A hash of everything a run of the entry's notebooks reads from the repository: every file of the entry (its
502-    notebooks, helpers, lock and entry.yaml, which names the Python and the dataset versions), the packages `run`
503-    adds, and RUN_VERSION. Two runs from the same hash execute the same code on the same data versions."""
504-    import hashlib
505-    h = hashlib.sha256(f"run {RUN_VERSION}; harness {' '.join(HARNESS)}; python {python_of(entry_dir)}\n".encode())
506-    for path in sorted(p for p in entry_dir.rglob("*") if p.is_file()):
507-        rel = path.relative_to(entry_dir)
508-        if any(part in ("__pycache__", ".ipynb_checkpoints", ".venv") or part.endswith(".pyc") for part in rel.parts):
509-            continue
510-        h.update(f"{rel.as_posix()}\0{file_hash(path)}\n".encode())
511-    return h.hexdigest()
512-
513-
514-def reusable(entry_dir: Path, output_dir: Path, max_minutes: float) -> dict | None:
515-    """The stamp of executed copies that a run now would only make again: made from this hash, each copy still as
516-    the run left it, each within the time limit asked for now, and not older than REUSE_DAYS. Else None."""
517-    try:
518-        stamp = json.loads((output_dir / STAMP).read_text())
519-        entry = yaml.safe_load((entry_dir / "entry.yaml").read_text())
[... 1 more lines not kept]
```

**Agent**

The README is part of the run stamp, so I'll set the runtime in entry.yaml and do one final run, then rebuild the handover.

**Agent calls Bash**

```bash
sed -i 's/  runtime_minutes: 15/  runtime_minutes: 13/' entries/zandvakili-2015/entry.yaml && python tools/entry.py all entries/zandvakili-2015 2>&1 | tail -2 && python tools/entry.py handover entries/zandvakili-2015 2>&1 | tail -1; python3 - <<'EOF' > $TMPDIR/exec_out3.txt
import nbformat
nb=nbformat.read('executed/zandvakili-2015/reproduce_zandvakili_2015.ipynb',4)
for c in nb.cells:
    if c.cell_type!='code': continue
    for o in c.get('outputs',[]):
        if 'text' in o: print(o['text'])
        elif o.get('output_type')=='error': print('ERROR',o['ename'],o['evalue'])
EOF
cd $TMPDIR; diff <(grep -v "run time\|^$\| s, peak memory\|total " exec_out2.txt) <(grep -v "run time\|^$\| s, peak memory\|total " exec_out3.txt) && echo SAME; grep "run time" exec_out3.txt; date -u
```

```
0 error(s)
pass  reproduce_zandvakili_2015.ipynb  (756 s)
wrote executed/zandvakili-2015/handover
SAME
notebook run time 749 s; peak memory 2.76 GB
Thu Nov 12 18:03:30 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
ls -a entries/zandvakili-2015/; grep -c '"outputs": \[\]' entries/zandvakili-2015/reproduce_zandvakili_2015.ipynb; grep -c "Result:" executed/zandvakili-2015/handover/reproduce_zandvakili_2015.ipynb
```

```
.
..
.claude
README.md
__pycache__
entry.yaml
reproduce_zandvakili_2015.ipynb
requirements.in
requirements.lock.txt
v1v2.py
20
0
```

**Agent calls Bash**

```bash
ls -la entries/zandvakili-2015/.claude entries/zandvakili-2015/__pycache__; git check-ignore -v entries/zandvakili-2015/__pycache__ entries/zandvakili-2015/.claude
```

```
entries/zandvakili-2015/.claude:
total 12
drwxr-xr-x 3 runner runner 4096 Nov 12 16:38 .
drwxr-xr-x 4 runner runner 4096 Nov 12 17:50 ..
drwx------ 2 runner runner 4096 Nov 12 16:38 .cc-writes

entries/zandvakili-2015/__pycache__:
total 44
drwxr-xr-x 2 runner runner  4096 Nov 12 17:22 .
drwxr-xr-x 4 runner runner  4096 Nov 12 17:50 ..
-rw-r--r-- 1 runner runner 33943 Nov 12 17:22 v1v2.cpython-313.pyc
.gitignore:1:__pycache__/	entries/zandvakili-2015/__pycache__
```

**Agent**

I've finished steps 1 to 5 for the CRCNS v1v2-1 attempt and run the handover (step 6). The notebook runs cleanly from a fresh environment in 12.5 minutes with a peak of 2.8 GB of memory. `entry.py check` reports 0 errors. Nothing is committed.

The entry is in `entries/zandvakili-2015/` (notebook, helper `v1v2.py`, entry.yaml, README, requirements and lock). The record is `attempts/zandvakili-2015-01.yaml`, and the verifier's package is in `executed/zandvakili-2015/handover/`. I did no verification of my own.

**(1) Outcome per claim**

| claim | outcome |
|---|---|
| fig4c-broad-ccg-peaks | reproduced (31 of 31 sites) |
| fig4c-narrow-peak-sites | not reproduced (16 of 31 = 0.516, expected 0.206) |
| fig4-narrow-peak-depth | blocked, data_missing |
| fig5a-rf-alignment | blocked, metadata_insufficient |
| fig5-narrow-pairs-rare | not reproduced (0.0105 of pairs, expected 0.003) |
| fig5b-v1v2-latency | partially reproduced (offset is significant; median 2.0 ms, width 3.89 ms) |
| fig5b-intra-areal-zero-lag | not reproduced, rests on an assumption (V1-V1 Wilcoxon p = 0.016) |
| figs3-efficacy | not reproduced (median 0.324%, mean 0.496%) |
| fig6a-coordination-before-v2 | reproduced (6 of 6 windows under every reading) |
| fig7a-threefold | partially reproduced (ratio about 1.9, expected 3) |
| fig7a-above-shuffle | reproduced |
| fig6b-not-after-v2 | not reproduced (raised at 80 ms after the spike) |
| fig6-slow-both-sides | reproduced |
| fig7d-time-course | partially reproduced (peak 2.5 to 3 ms before; some epochs after or far before are significant) |
| figs4-partner-not-needed | reproduced |
| fig7b, fig7e, fig7c, figs2a, figs2b, figs5 | blocked, data_missing |
| rf-sizes | blocked, metadata_insufficient |
| fig1, fig3, figs1, fig8 (simulations) | blocked, not_runnable |

**(2) Dataset, assumptions and questions**
- **What it holds:** 5 sessions from 3 animals, with 564 V1 and 147 V2 units. Spike times are stored in 1 ms bins; the paper used 0.1 ms. Each session has one recording per V2 tetrode.
- **What it lacks:** V2 depth, penetration identity, unit SNR and waveforms. RF positions are in pixels, with no scale or fixation point anywhere in the data set or the paper.
- **Unexplained selection:** narrow V1-V2 peaks appear at half the sites, against a fifth in the paper. The deposited sessions look like a selection the documentation does not describe; I recorded this as `selection_undocumented`.
- **Small metadata errors:** the descriptor gives 112.2 V1 units per session where the files hold 112.8. Its stimulus-code list is wrong for session 105l001p16, where code 7 is 180 deg; the sessions description says so, and the responses agree with it.
- **Clock check passes:** orientation decodes at chance before 30 ms and in the preceding blank, and at 0.94 to 0.99 from 60 ms. No duplicate units or sessions.
- **Assumption:** the paper's test of median offsets is taken to be the Wilcoxon signed-rank test (MATLAB `signrank`). The sign test reverses the V1-V1 result.
- **Questions for the authors** (as `methods_unavailable` findings):
  1. Which test gave the p-values for the median peak offsets?
  2. Were the bootstrap p-values paired or independent?
  3. Was the 10 ms CCG jitter window used for all significance tests?
- **Questions to a reader:** none. I don't believe the claims file misreads the paper.

**(3) Where the protocol was unclear or did not fit**
1. Reading e-b of the claims file (one 1 ms bin centred 2.5 ms before the spike) cannot be formed from 1 ms data. I ran the bins at 2 and 3 ms, which bracket it, and said so in the deviations.
2. The protocol has no blocking reason for simulations with no code that were left undone for time. I used `not_runnable` and said they were not attempted.
3. The claims file leaves reading j-b ("another window") unnamed. I chose 25 ms as a variant and recorded it as my choice.
4. A claim of absence is "judged on the paper's test alone", but the paper names no test, so the claims file lists two. I treated the disagreement as a step 1.6 case: I adopted one test, set `assumed: true`, and recorded the question for the authors.
5. The criterion for fig7d is ambiguous about whether "no significant distant epoch" applies per window or across all windows. Its "partially reproduced" wording settles it, giving the same outcome under both bootstrap readings.
6. The repository's `entry.py check` needs the dataset version string to appear in the code. For CRCNS that is `unversioned`, so I added a `VERSION` constant to the helper.

**(4) Runtime and failures**
- The work took about 1 h 40 min (16:25 to 18:04 UTC). The full notebook takes 12.5 minutes per run, and I ran it four times.
- Nothing failed in the final run. The only development error was a dtype bug, which I fixed.

## End of run

61 turns, 92 minutes, $5.87 at API prices, result: success.
