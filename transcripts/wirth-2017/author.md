# wirth-2017 · author · run 43420118844

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls paper claims entries | head -50
```

```
<persisted-output>
Output too large (40.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/8022d746-1f1f-4364-b60a-55870fd7b0ca/tool-results/bqwr00zlk.txt

Preview (first 2KB):
Fri Nov 13 11:57:52 UTC 2026
# Protocol for an attempt

Version: `pilot-15`. Record this version in the attempt's provenance.

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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/8022d746-1f1f-4364-b60a-55870fd7b0ca/tool-results/bqwr00zlk.txt"
}
```

```
1	Fri Nov 13 11:57:52 UTC 2026
2	# Protocol for an attempt
3	
4	Version: `pilot-15`. Record this version in the attempt's provenance.
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
[... 739 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/wirth-2017.yaml; ls paper; cat papers/datasets/wirth-2017.yaml; ls questions | grep wirth; ls attempts | grep wirth; ls entries | grep wirth
```

```
<persisted-output>
Output too large (51.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/8022d746-1f1f-4364-b60a-55870fd7b0ca/tool-results/betxa9fxc.txt

Preview (first 2KB):
# Claims for Wirth, Baraduc, Plante, Pinede & Duhamel (2017), PLoS Biology 15(2), e2001045,
# tested on CRCNS hc-12 and hc-21.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
# protocol pilot-14 as stated in docs/protocol.md.
#
# Text read: the version of record (PMC5328243, open access), full text from Europe PMC JATS
# XML as stored under paper/: Results, Discussion, Materials and Methods, the figure legends of
# Figs 1 to 7 and the legends of S1 to S7 Figs. The supplementary text files S1 Appendix
# (sections A1 to A5: point-of-gaze density maps, gaze before joystick actions, recording
# methods and cell selection, population averages, the control for space dimensionality) and
# S2 Appendix (description of the CRCNS files and scripts) are DOCX files that are not under
# paper/ and were not read. The claims that rest on them say so (gaze-anticipates-action,
# gaze-anticipates-landmarks, dimensionality-control, fields-per-cell). No PDF was read; the
# reference list is absent from the stored text, so reference 60 (the learning curve method)
# is not named.
#
[... 12 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/8022d746-1f1f-4364-b60a-55870fd7b0ca/tool-results/betxa9fxc.txt"
}
```

```
1	# Claims for Wirth, Baraduc, Plante, Pinede & Duhamel (2017), PLoS Biology 15(2), e2001045,
2	# tested on CRCNS hc-12 and hc-21.
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
4	# protocol pilot-14 as stated in docs/protocol.md.
5	#
6	# Text read: the version of record (PMC5328243, open access), full text from Europe PMC JATS
7	# XML as stored under paper/: Results, Discussion, Materials and Methods, the figure legends of
8	# Figs 1 to 7 and the legends of S1 to S7 Figs. The supplementary text files S1 Appendix
9	# (sections A1 to A5: point-of-gaze density maps, gaze before joystick actions, recording
10	# methods and cell selection, population averages, the control for space dimensionality) and
11	# S2 Appendix (description of the CRCNS files and scripts) are DOCX files that are not under
12	# paper/ and were not read. The claims that rest on them say so (gaze-anticipates-action,
13	# gaze-anticipates-landmarks, dimensionality-control, fields-per-cell). No PDF was read; the
14	# reference list is absent from the stored text, so reference 60 (the learning curve method)
15	# is not named.
16	#
17	# Code: the paper links no repository. It says some Matlab scripts are hosted with the data on
18	# CRCNS (Supporting data; S2 Appendix); the hc-12 descriptor lists them (a scripts folder that
19	# plots position, direction and state-space maps, rasters and learning curves). These are files
20	# of the dataset and were not read. No criterion below takes a method from code; the author may
[... 843 more lines not kept]
```

**Agent calls Bash**

```bash
cat paper/hc-12.data-description.txt; echo ======; cat paper/hc-21.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/## CRCNS/,/^## [A-Z]/p' docs/archives.md; ls entries/fouke-2025; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in; head -c 6000 attempts/fouke-2025-01.yaml
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
[... 154 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md | head -80; wc -c docs/design.md
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
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
for d in hc-12 hc-21; do curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=$d/" | python -c "
import sys,re
t=sys.stdin.read()
for k,s in zip(re.findall('<Key>(.*?)</Key>',t),re.findall('<Size>(.*?)</Size>',t)): print(k,s)
print(re.findall('<IsTruncated>(.*?)<',t))"; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
B=https://crcnsarchive.s3-us-west-2.amazonaws.com; for f in hc-12/live/checksums.md5 hc-12/live/filelist.txt hc-21/live/checksums.md5 hc-21/live/filelist.txt; do echo "== $f"; curl -s $B/$f; done; cd $TMPDIR && curl -s $B/hc-12/live/scripts.tar.gz | tar tzv
```

```
== hc-12/live/checksums.md5
426c7d00c0358f2cc9873e0dbb331e2f  data.tar.gz
b2dca320bc61170f2add92f99cb8f7bf  docs/crcns_hc-12_data_description.docx
b405deaa58572a0f1e9aa5e0b1515d01  docs/crcns_hc-12_data_description.pdf
2e852d149424ccc7dbd311199286f64f  filelist.txt
82c02c4697bcb60bdea1a90ce48de5e0  scripts.tar.gz
== hc-12/live/filelist.txt
# CRCNS.org 'hc-12' dataset files
# To use this for fetching files, comment out files that are
# not needed by putting a '#' as the first character on the line (default mode)
# or put a '+' as the first character to specifiy files to be fetched (+ mode).
# mode='default' (change to '+' for + mode).
 data.tar.gz	3800737108 (3.5 GB)
 docs/crcns_hc-12_data_description.docx	32098 (31.3 KB)
 docs/crcns_hc-12_data_description.pdf	77613 (75.7 KB)
 scripts.tar.gz	8839 (8.6 KB)
 checksums.md5	287
== hc-21/live/checksums.md5
2129d5ce08854ccbbbb961365b88f861  analysis_scripts.zip
dee5e8aa4a7b3c44b61b8cecfe622a0a  data.tar.gz
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
B=https://crcnsarchive.s3-us-west-2.amazonaws.com; mkdir -p $TMPDIR/scr && cd $TMPDIR/scr && curl -s $B/hc-12/live/scripts.tar.gz | tar xz && for f in scripts/*.m; do echo "=== $f"; cat $f; done
```

```
<persisted-output>
Output too large (30.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/8022d746-1f1f-4364-b60a-55870fd7b0ca/tool-results/b9vrmbd7g.txt

Preview (first 2KB):
=== scripts/circ_ksdensity.m
function [pdf, sigma] = circ_ksdensity(T, ti, method, sigma)
%CIRC_KSDENSITY Probability density function of circular data.
%
% -------------
% INPUT
% -------------
% T - circular data values, n-by-1 vector
% ti - vector location in angles of even-spaced points where 
%     the pdf is to be computed (1:360 for example)
% method - {'msni'} | 'msn' | 'niqr' | 'mad' | 'std'
%     - type of method for infering the smoothing kernel width
%         from sample data statistics
%     - the methods differe in the statistics used for measuring 
%         the data spread and the choice of a multiplicative constant.
%     std - standard deviation of sample data
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/scr/scripts && for f in getencodetime.m getspikes.m interp1deg.m plot_multiple_ref_frames.m polar_map_sw_r.m runningaverage.m simple_place_cell_square_script_theta_r.m simple_raster_to_check_file.m star_remapped_cell_r.m; do echo "=== $f"; cat $f; done
```

```
=== getencodetime.m

function [encodetime1,encodetime2,encodetime3]= getencodetime(encode, trials,codematrix, timematrix, firstorsecond)

if firstorsecond==0
    encodetime1=[];
    
    [togetrow,togetcol]=find(codematrix(trials,2:end)==encode);
    toget=[togetrow,togetcol];
    toget=sortrows(toget,1);
    toget1=toget(:,2);
    toget_col=toget1+1; %because of the first column that we left out when screening above line 4
    toget_row=toget(:,1);
    for i=1:length(toget_row)
        trial=trials(toget_row(i));
        etime=timematrix(trial,toget_col(i));
        encodetime1=[encodetime1;etime];
        encodetime2=[];
        encodetime3=[];
    end
[... 778 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && . dev/bin/activate && uv pip install -q fsspec aiohttp requests scipy numpy pandas h5py statsmodels matplotlib nbformat nbclient ipykernel 2>&1 | tail -2; python -V; nproc; free -g
```

```
Python 3.13.18
4
               total        used        free      shared  buff/cache   available
Mem:              15           1          11           0           3          14
Swap:              2           0           2
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t1.py <<'EOF'
import fsspec, tarfile, time
t=time.time()
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-12/live/data.tar.gz"
f=fsspec.open(url,block_size=2**22).open()
tf=tarfile.open(fileobj=f,mode='r|gz')
n=0
for m in tf:
    print(m.name,m.size,round(time.time()-t,1))
    if m.isfile():
        b=tf.extractfile(m).read(); n+=1
        if n==1: open('first.mat','wb').write(b)
    if n>=6: break
EOF
python t1.py
```

```
data 0 0.9
data/ke20130221_HPC_e4_c4_seg.mat 22048269 0.9
data/ke20130221_HPC_e4_c5_seg.mat 22048179 1.9
data/ke20130301_HPC_e1_c1_seg.mat 9789866 3.2
data/ke20130306_HPC_e5_c1_seg.mat 30187159 3.8
data/ke20130306_HPC_e5_c2_seg.mat 30089858 5.7
data/ke20130306_HPC_e5_c3_seg.mat 30075866 7.3
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && rm -f first.mat && . dev/bin/activate && cat > t2.py <<'EOF'
import fsspec, tarfile, io, scipy.io as sio, numpy as np
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-12/live/data.tar.gz"
f=fsspec.open(url,block_size=2**22).open()
tf=tarfile.open(fileobj=f,mode='r|gz')
def show(o,ind=''):
    if isinstance(o,np.ndarray) and o.dtype.names:
        for nm in o.dtype.names:
            v=o[nm].flat[0] if o.size else None
            print(ind+nm, type(v).__name__, getattr(v,'shape',None), getattr(v,'dtype',None))
            show(v,ind+'  ')
    elif isinstance(o,np.ndarray) and o.dtype==object:
        print(ind,'objarr',o.shape)
for m in tf:
    if m.isfile():
        d=sio.loadmat(io.BytesIO(tf.extractfile(m).read()))
        print(m.name,[k for k in d if not k.startswith('__')])
        for k in d:
            if not k.startswith('__'): print(k,d[k].shape,d[k].dtype); show(d[k])
        fl=d['file'][0,0]
        np.set_printoptions(linewidth=200,suppress=True)
        cd=fl['camera_data'][0,0]
        print(cd.dtype)
        t60=cd['time_60'] if 'time_60' in cd.dtype.names else None
        print(t60[:5]); print(t60[::20000])
        na=fl['newallo'][0,0]
        print(na['codematrix'][:5]); print(na['timematrix'][:5]); print(na['learning_curves'][:5], na['learning_curves'].shape)
        print(fl['elec'][:5].ravel(), fl['elec'].shape, fl['eye_times'][:3].ravel(), fl['eye_times'][-1])
        re=fl['right_eye'][0,0]; print(re.dtype)
        for n in re.dtype.names: print(n, re[n].shape, re[n][:3].ravel())
        break
EOF
python t2.py
```

```
data/ke20130221_HPC_e4_c4_seg.mat ['file']
file (1, 1) [('elec', 'O'), ('right_eye', 'O'), ('left_eye', 'O'), ('eye_times', 'O'), ('newallo', 'O'), ('camera_data', 'O'), ('reclocation', 'O')]
elec ndarray (407, 1) float64
right_eye ndarray (1, 1) [('hor', 'O'), ('ver', 'O')]
  hor ndarray (831007, 1) float64
  ver ndarray (831007, 1) float64
left_eye ndarray (1, 1) [('hor', 'O'), ('ver', 'O')]
  hor ndarray (831007, 1) float64
  ver ndarray (831007, 1) float64
eye_times ndarray (831008, 1) float64
newallo ndarray (1, 1) [('codematrix', 'O'), ('timematrix', 'O'), ('elec', 'O'), ('ok', 'O'), ('learningtrial', 'O'), ('learning_curves', 'O')]
  codematrix ndarray (81, 15) uint8
  timematrix ndarray (81, 15) float64
  elec ndarray (2978, 1) float64
  ok ndarray (1, 1) uint8
  learningtrial ndarray (1, 1) uint8
  learning_curves ndarray (81, 3) float64
camera_data ndarray (1, 1) [('time_60', 'O'), ('raw', 'O')]
  time_60 ndarray (246431, 12) float64
  raw ndarray (1, 1) [('title', 'O'), ('comment', 'O'), ('resolution', 'O'), ('length', 'O'), ('items', 'O'), ('times', 'O'), ('codes', 'O'), ('text', 'O')]
[... 48 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > survey.py <<'EOF'
import fsspec, tarfile, io, scipy.io as sio, numpy as np, pickle, time, sys
ds=sys.argv[1]
url=f"https://crcnsarchive.s3-us-west-2.amazonaws.com/{ds}/live/data.tar.gz"
f=fsspec.open(url,block_size=2**22).open()
tf=tarfile.open(fileobj=f,mode='r|gz')
out={}
t=time.time()
def get(s,n):
    return s[n] if n in s.dtype.names else None
for m in tf:
    if not m.isfile(): print('nonfile',m.name); continue
    try:
        d=sio.loadmat(io.BytesIO(tf.extractfile(m).read()))
    except Exception as e:
        print('ERR',m.name,e); out[m.name]={'err':str(e)}; continue
    keys=[k for k in d if not k.startswith('__')]
    fl=d['file'][0,0]
    r={'keys':keys,'fields':fl.dtype.names}
    for k in fl.dtype.names:
        v=fl[k]
        r['shape_'+k]=v.shape
    elec=fl['elec'].ravel() if 'elec' in fl.dtype.names else None
    r['elec']=elec
    et=fl['eye_times'].ravel() if 'eye_times' in fl.dtype.names else None
    r['eye_range']=(et.min(),et.max(),len(et), np.median(np.diff(et))) if et is not None else None
    cd=fl['camera_data'][0,0]
    r['cd_fields']=cd.dtype.names
    t60=cd['time_60'] if 'time_60' in cd.dtype.names else None
    r['t60']=t60.astype(np.float32) if t60 is not None else None
    for maze in ['newallo','famallo']:
        if maze in fl.dtype.names:
            na=fl[maze][0,0]
            if na.dtype.names is None: r[maze]=('nostruct',na.shape); continue
            rr={'fields':na.dtype.names}
            for k in na.dtype.names:
                v=na[k]
                if k=='camera_data':
                    rr['t60']=v[0,0]['time_60'].astype(np.float32)
                elif k in('codematrix','timematrix','learning_curves','elec','ok','learningtrial'):
                    rr[k]=np.array(v)
                else: rr['shape_'+k]=v.shape
            r[maze]=rr
    r['reclocation']=fl['reclocation'] if 'reclocation' in fl.dtype.names else None
    out[m.name]=r
    print(m.name, round(time.time()-t), flush=True)
pickle.dump(out,open(f'survey_{ds}.pkl','wb'))
EOF
python survey.py hc-12 2>&1 | tail -5; du -sh survey_hc-12.pkl
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/survey.py", line 26, in <module>
    cd=fl['camera_data'][0,0]
       ~~^^^^^^^^^^^^^^^
ValueError: no field of name camera_data
du: cannot access 'survey_hc-12.pkl': No such file or directory
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
s=open('survey.py').read()
s=s.replace("""    cd=fl['camera_data'][0,0]
    r['cd_fields']=cd.dtype.names
    t60=cd['time_60'] if 'time_60' in cd.dtype.names else None
    r['t60']=t60.astype(np.float32) if t60 is not None else None""","""    if 'camera_data' in fl.dtype.names:
        cd=fl['camera_data'][0,0]
        r['cd_fields']=cd.dtype.names
        r['t60']=cd['time_60'].astype(np.float32)""")
s=s.replace("rr['t60']=v[0,0]['time_60'].astype(np.float32)","rr['cd_fields']=v[0,0].dtype.names; rr['t60']=v[0,0]['time_60'].astype(np.float32)")
s=s.replace("""        print('ERR',m.name,e); out[m.name]={'err':str(e)}; continue""","""        print('ERR',m.name,e); out[m.name]={'err':str(e)}; continue
    try:
        run(d,m,out)
    except Exception as e:
        import traceback; traceback.print_exc(); out[m.name]={'err2':str(e)}
pickle.dump(out,open(f'survey_{ds}.pkl','wb'))
""")
# restructure: move the body into a function
head,body=s.split("    keys=[k for k in d",1)
body="    keys=[k for k in d"+body
body=body.split("pickle.dump(out,open(f'survey_{ds}.pkl','wb'))\n")[0]
func="def run(d,m,out):\n"+body
s=head.replace("for m in tf:",func+"\nfor m in tf:")
# head contains loop start; reorder
open('survey2.py','w').write(s)
EOF
sed -n 1,200p survey2.py | head -80
```

```
import fsspec, tarfile, io, scipy.io as sio, numpy as np, pickle, time, sys
ds=sys.argv[1]
url=f"https://crcnsarchive.s3-us-west-2.amazonaws.com/{ds}/live/data.tar.gz"
f=fsspec.open(url,block_size=2**22).open()
tf=tarfile.open(fileobj=f,mode='r|gz')
out={}
t=time.time()
def get(s,n):
    return s[n] if n in s.dtype.names else None
def run(d,m,out):
    keys=[k for k in d if not k.startswith('__')]
    fl=d['file'][0,0]
    r={'keys':keys,'fields':fl.dtype.names}
    for k in fl.dtype.names:
        v=fl[k]
        r['shape_'+k]=v.shape
    elec=fl['elec'].ravel() if 'elec' in fl.dtype.names else None
    r['elec']=elec
    et=fl['eye_times'].ravel() if 'eye_times' in fl.dtype.names else None
    r['eye_range']=(et.min(),et.max(),len(et), np.median(np.diff(et))) if et is not None else None
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && sed -i "s/\['time_60'\].astype(np.float32)/['time_60'][::10].astype(np.float32)/g" survey2.py && (python survey2.py hc-12 > s12.log 2>&1; python survey2.py hc-21 > s21.log 2>&1); tail -3 s12.log s21.log; grep -c mat s12.log s21.log; grep -i err s12.log s21.log | head; ls -la survey_*
```

```
error: unexpected argument '-3' found

  tip: to pass '-3' as a value, use '-- -3'

Usage: tail [OPTION]... [FILE]...

For more information, try '--help'.
s12.log:189
s21.log:101
-rw-r--r-- 1 runner runner 233360510 Nov 13 12:07 survey_hc-12.pkl
-rw-r--r-- 1 runner runner 136110820 Nov 13 12:10 survey_hc-21.pkl
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import pickle, numpy as np, collections, re
for ds in ['hc-12','hc-21']:
    S=pickle.load(open(f'survey_{ds}.pkl','rb'))
    print('=====',ds,len(S))
    c=collections.Counter()
    for k,r in S.items():
        c[(tuple(r.get('fields',())), 'nf:'+str(r.get('newallo',{}).get('fields') if isinstance(r.get('newallo'),dict) else r.get('newallo')))]+=1
    for k,v in c.items(): print(v,k)
    names=[k.split('/')[-1] for k in S]
    print(names[:5])
    monk=collections.Counter(n[:2] for n in names); print(monk)
    sess=collections.Counter(n[:10] for n in names); print('sessions',len(sess), collections.Counter(n[:2] for n in sess))
EOF
```

```
===== hc-12 189
78 (('elec', 'right_eye', 'left_eye', 'eye_times', 'newallo', 'camera_data', 'reclocation'), "nf:('codematrix', 'timematrix', 'elec', 'ok', 'learningtrial', 'learning_curves')")
46 (('camera_data', 'right_eye', 'left_eye', 'eye_times', 'newallo', 'elec', 'reclocation'), "nf:('codematrix', 'timematrix', 'ok', 'learningtrial', 'learning_curves')")
34 (('elec', 'camera_data', 'right_eye', 'left_eye', 'eye_times', 'newallo', 'reclocation'), "nf:('codematrix', 'timematrix', 'ok', 'learningtrial', 'learning_curves')")
16 (('elec', 'right_eye', 'left_eye', 'eye_times', 'newallo', 'camera_data', 'reclocation'), "nf:('codematrix', 'timematrix', 'ok', 'learningtrial', 'learning_curves')")
1 (('camera_data', 'right_eye', 'left_eye', 'eye_times', 'newallo', 'codematrix', 'timematrix', 'elec', 'reclocation'), "nf:('codematrix', 'timematrix', 'ok', 'learningtrial', 'learning_curves')")
3 (('newallo', 'reclocation'), "nf:('timematrix', 'codematrix', 'elec1_14_00a', 'elec1_14_00b', 'elec1_14_00c', 'elec2_18_08a', 'elec2_18_08b', 'elec2_18_08c', 'elec2_18_08d', 'DigMark_32_00_11', 'DigMark_32_00_12', 'DigMark_32_00_127', 'DigMark_32_00_21', 'DigMark_32_00_22', 'DigMark_32_00_23', 'DigMark_32_00_40', 'DigMark_32_00_41', 'DigMark_32_00_42', 'DigMark_32_00_44', 'DigMark_32_00_50', 'DigMark_32_00_51', 'DigMark_32_00_52', 'DigMark_32_00_53', 'DigMark_32_00_54', 'Forward_04_03', 'Left_02_01', 'Reward_01_00', 'Right_03_02', 'AllFile', 'Left_Hor_07_30', 'Left_Hor_07_30_ts', 'Left_Hor_07_30_ind', 'Left_Ver_08_31', 'Left_Ver_08_31_ts', 'Left_Ver_08_31_ind', 'Right_Ho_05_28', 'Right_Ho_05_28_ts', 'Right_Ho_05_28_ind', 'Right_Ve_06_29', 'Right_Ve_06_29_ts', 'Right_Ve_06_29_ind', 'time_60', 'elec', 'allrescount', 'allrestiming', 'allresfiring', 'beforerescount', 'beforerestiming', 'beforeresfiring', 'afterrescount', 'afterrestiming', 'afterresfiring', 'y', 'correct_wrong_trials', 'camera_data', 'ok', 'learningtrial', 'learning_curves')")
1 (('newallo', 'reclocation'), "nf:('timem
[... 39 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import pickle, numpy as np
S=pickle.load(open('survey_hc-12.pkl','rb'))
np.set_printoptions(linewidth=220,suppress=True,precision=2)
for i,(k,r) in enumerate(S.items()):
    na=r.get('newallo')
    if not isinstance(na,dict): print(k,'NO NEWALLO', r.get('fields')); continue
    tm=na['timematrix']; cm=na['codematrix']
    t60=r.get('t60', na.get('t60'))
    tt=t60[:,0]; tt=tt[tt>0]
    el=r.get('elec'); el2=na.get('elec')
    el2=el2.ravel() if el2 is not None else None
    trow=tm[:,1:][cm[:,1:]>0]
    m12=np.unique(np.floor(t60[:,11][np.isfinite(t60[:,11])]))
    print(k.split('/')[-1][:24], cm.shape, 'tm',round(trow.min()),round(trow.max()), 't60',round(tt.min()),round(tt.max()), 'maze',m12,
      'elec', None if el is None else (len(el), round(el.min()), round(el.max())), 'nel', None if el2 is None else (len(el2),round(el2.min()),round(el2.max())),
      'eye', None if r['eye_range'] is None else [round(x,3) for x in r['eye_range']], 'ok',na['ok'].ravel(), 'lt',na['learningtrial'].ravel())
EOF
```

```
<persisted-output>
Output too large (35.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/8022d746-1f1f-4364-b60a-55870fd7b0ca/tool-results/bkgzn3c8l.txt

Preview (first 2KB):
ke20130221_HPC_e4_c4_seg (81, 15) tm 9 676 t60 9 4116 maze [1. 2.] elec (407, 23, 4061) nel (2978, 5, 4138) eye [np.float64(0.0), np.float64(4155.035), 831008, np.float64(0.005)] ok [1] lt [8]
ke20130221_HPC_e4_c5_seg (81, 15) tm 9 676 t60 9 4116 maze [1. 2.] elec (546, 9, 4151) nel (2978, 5, 4138) eye [np.float64(0.0), np.float64(4155.035), 831008, np.float64(0.005)] ok [1] lt [8]
ke20130301_HPC_e1_c1_seg (83, 14) tm 731 1419 t60 11 1419 maze [1. 2.] elec (12668, 0, 1578) nel (12668, 0, 1578) eye [np.float64(0.0), np.float64(1577.875), 315576, np.float64(0.005)] ok [1] lt [13]
ke20130306_HPC_e5_c1_seg (81, 18) tm 5 797 t60 5 5312 maze [1. 2. 3. 4.] elec (21435, 1, 5315) nel (78389, 0, 5315) eye [np.float64(0.0), np.float64(5315.055), 1063012, np.float64(0.005)] ok [1] lt [3]
ke20130306_HPC_e5_c2_seg (81, 18) tm 5 797 t60 5 5312 maze [1. 2. 3. 4.] elec (2843, 1, 5312) nel (78389, 0, 5315) eye [np.float64(0.0), np.float64(5315.055), 1063012, np.float64(0.005)] ok [1] lt [3]
ke20130306_HPC_e5_c3_seg (81, 18) tm 5 797 t60 5 5312 maze [1. 2. 3. 4.] elec (1446, 7, 5313) nel (78389, 0, 5315) eye [np.float64(0.0), np.float64(5315.055), 1063012, np.float64(0.005)] ok [1] lt [3]
ke20130314_HPC_e14_c2_se (81, 16) tm 5 687 t60 6 2416 maze [1. 2. 3.] elec (4424, 2, 2616) nel (4424, 2, 2616) eye [np.float64(0.0), np.float64(2616.775), 523356, np.float64(0.005)] ok [1] lt [3]
ke20130314_HPC_e15_c1_se (81, 16) tm 5 687 t60 6 2416 maze [1. 2. 3.] elec (2416, 0, 2609) nel (2416, 0, 2609) eye [np.float64(0.0), np.float64(2616.775), 523356, np.float64(0.005)] ok [1] lt [3]
ke20130314_hpc_e9_c1_seg (81, 16) tm 5 687 t60 6 2416 maze [1. 2. 3.] elec (25181, 0, 2617) nel (25181, 0, 2617) eye [np.float64(0.0), np.float64(2616.775), 523356, np.float64(0.005)] ok [1] lt [3]
ke201
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && cut -c1-25,26-200 /home/runner/.claude/projects/-home-runner-work-encore-encore/8022d746-1f1f-4364-b60a-55870fd7b0ca/tool-results/bkgzn3c8l.txt | sed 's/np.float64(\([^)]*\))/\1/g' | awk '{print}' | cut -c1-230 | sed -n '10,189p'
```

```
ke20130314_hpc_e9_c2_seg (81, 16) tm 5 687 t60 6 2416 maze [1. 2. 3.] elec (4302, 1, 2614) nel (4302, 1, 2614) eye [0.0, 2616.775, 523356, 0.005] ok [1] lt [3]
ke20130315_HPC_e10_c1_se (109, 18) tm 14 911 t60 14 2478 maze [1. 2.] elec (3297, 1, 3492) nel (3297, 1, 3492) eye [0.0, 3576.35, 715271, 0.005] ok [1] lt [9]
ke20130315_HPC_e11_c1_se (109, 18) tm 14 911 t60 14 1786 maze [1. 2.] elec (2791, 1, 3217) nel (2791, 1, 3217) eye [0.0, 3576.35, 715271, 0.005] ok [1] lt [9]
ke20130315_HPC_e2_c1_seg (109, 18) tm 14 911 t60 14 3545 maze [1. 2. 3.] elec (6109, 70, 3576) nel (15902, 0, 3576) eye [0.0, 3576.35, 715271, 0.005] ok [1] lt [9]
ke20130327_HPC_e11_c1_se (84, 15) tm 12 695 t60 13 4655 maze [1. 2. 3. 4. 5. 6.] elec (3522, 26, 4661) nel (12904, 26, 4665) eye [0.0, 4665.205, 933042, 0.005] ok [
ke20130402_HPC_e11_c2_se (80, 15) tm 9 624 t60 9 4707 maze [1. 2. 3. 4. 5. 6.] elec (3097, 1, 2867) nel None eye [0.0, 4739.93, 947987, 0.005] ok [1] lt [6]
ke20130402_HPC_e5_c1_seg (41, 15) tm 309 624 t60 9 4707 maze [1. 2. 3. 4. 5. 6.] elec (5290, 134, 4731) nel None eye [0.0, 4739.93, 947987, 0.005] ok [1] lt [3]
ke20130402_HPC_e5_c2_seg (80, 15) tm 9 624 t60 9 4707 maze [1. 2. 3. 4. 5. 6.] elec (818, 178, 4731) nel None eye [0.0, 4739.93, 947987, 0.005] ok [1] lt [6]
ke20130404_ec_e15_c1_seg (161, 20) tm 5 1240 t60 5 5312 maze [1. 2. 3. 4. 5.] elec (19150, 0, 5314) nel None eye [0.0, 5315.035, 1063008, 0.005] ok [1] lt [76]
ke20130404_ec_e15_c2_seg (161, 20) tm 5 1240 t60 5 5312 maze [1. 2. 3. 4. 5.] elec (20935, 1, 5314) nel None eye [0.0, 5315.035, 1063008, 0.005] ok [1] lt [76]
ke20130404_hpc_e10_c1_se (161, 20) tm 5 1240 t60 5 5312 maze [1. 2. 3. 4. 5.] elec (7320, 1, 5307) nel None eye [0.0, 5315.035, 1063008, 0.005] ok [1] lt [76]
ke20130404_hpc_e11_c1_se (161, 20) tm 5 1240 t60 5 5312 maze [1. 2. 3. 4. 5.] elec (2960, 0, 5314) nel None eye [0.0, 5315.035, 1063008, 0.005] ok [1] lt [76]
ke20130404_hpc_e7_c1_seg (161, 20) tm 5 1240 t60 5 5312 maze [1. 2. 3. 4. 5.] e
[... 168 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > eye.py <<'EOF'
import fsspec, tarfile, io, scipy.io as sio, numpy as np, sys
np.set_printoptions(linewidth=200,suppress=True,precision=2)
for ds,nmax in [('hc-12',3),('hc-21',2)]:
    f=fsspec.open(f"https://crcnsarchive.s3-us-west-2.amazonaws.com/{ds}/live/data.tar.gz",block_size=2**22).open()
    tf=tarfile.open(fileobj=f,mode='r|gz'); n=0
    for m in tf:
        if not m.isfile(): continue
        n+=1
        if n not in (1,3) and ds=='hc-12': continue
        fl=sio.loadmat(io.BytesIO(tf.extractfile(m).read()))['file'][0,0]
        print(m.name)
        for e in ['right_eye','left_eye']:
            s=fl[e][0,0]
            for c in ['hor','ver']:
                v=s[c].ravel(); print(e,c,np.nanpercentile(v,[0,1,5,25,50,75,95,99,100]))
        if n>=nmax: break
EOF
python eye.py
```

```
Exit code 1
data/ke20130221_HPC_e4_c4_seg.mat
right_eye hor [-4980.16 -3294.37 -1889.34   266.27  1568.76  2700.04  3728.03  4007.87  4781.49]
right_eye ver [-4999.85 -1455.07  -915.07  -139.47   939.79  2076.57  3252.72  4222.56  4999.85]
left_eye hor [-4999.85 -3198.23 -1771.55   377.66  1761.17  2915.65  3897.09  4197.08  4999.85]
left_eye ver [-4999.85 -1435.24  -858.46   -47.76  1106.87  2275.39  3379.47  4217.53  4999.85]
data/ke20130301_HPC_e1_c1_seg.mat
right_eye hor [-4999.85 -4999.85 -4999.85 -4330.14 -2745.06 -1345.98  1128.69  1794.32  2943.12]
right_eye ver [-4999.85 -4999.85 -1326.8    390.47  1081.54  2814.48  4418.64  4999.85  4999.85]
left_eye hor [-4999.85 -4999.85 -4999.85 -4644.09 -2928.47 -1430.82  1251.22  2050.17  4999.85]
left_eye ver [-4999.85 -4999.85 -1512.15  -193.48   519.56  1937.1   3630.68  4627.92  4999.85]
data/ke20140313_c1.mat
Traceback (most recent call last):
  File "/tmp/claude-1001/eye.py", line 15, in <module>
    v=s[c].ravel(); print(e,c,np.nanpercentile(v,[0,1,5,25,50,75,95,99,100]))
                              ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/numpy/lib/_nanfunctions_impl.py", line 1396, in nanpercentile
    return _nanquantile_unchecked(
        a, q, axis, out, overwrite_input, method, keepdims, weights, weak_q)
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/numpy/lib/_nanfunctions_impl.py", line 1593, in _nanquantile_unchecked
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import pickle, numpy as np, collections
S=pickle.load(open('survey_hc-12.pkl','rb'))
np.set_printoptions(linewidth=220,suppress=True,precision=3)
k=list(S)[0]; r=S[k]; na=r['newallo']; t=r['t60']; cm=na['codematrix']; tm=na['timematrix']
w=(t[:,0]>=tm[0,2]-1)&(t[:,0]<=tm[-1,:].max())
t=t[w]
print(collections.Counter(t[:,10].astype(int)).most_common(60))
print('col4',np.nanpercentile(t[:,4],[0,50,100]),'col5',np.nanpercentile(t[:,5],[0,50,100]),'col6',np.nanpercentile(t[:,6],[0,50,100]),'col7',np.nanpercentile(t[:,7],[0,50,100]))
# trial 2: print tag sequence over time
for i in range(3):
    a,b=tm[i,2],tm[i+1,2]
    seg=t[(t[:,0]>=a)&(t[:,0]<b)]
    print(cm[i], tm[i].round(2))
    ch=np.r_[0,np.nonzero(np.diff(seg[:,10]))[0]+1]
    for j in ch: print('   t=%.2f tag=%d x=%.1f y=%.1f th=%.0f c4=%.2f c5=%.2f'%(seg[j,0],seg[j,10],seg[j,1],seg[j,2],seg[j,3],seg[j,4],seg[j,5]))
EOF
```

```
Exit code 1
Fri Nov 13 12:13:00 UTC 2026
<stdin>:7: RuntimeWarning: invalid value encountered in cast
/tmp/claude-1001/dev/lib/python3.13/site-packages/numpy/lib/_function_base_impl.py:4609: RuntimeWarning: invalid value encountered in subtract
  diff_b_a = b - a
[(np.int64(404), 461), (np.int64(545), 453), (np.int64(543), 358), (np.int64(542), 316), (np.int64(541), 314), (np.int64(105), 198), (np.int64(334), 198), (np.int64(354), 181), (np.int64(103), 155), (np.int64(101), 141), (np.int64(102), 139), (np.int64(214), 136), (np.int64(253), 130), (np.int64(235), 130), (np.int64(224), 97), (np.int64(405), 70), (np.int64(551), 68), (np.int64(552), 67), (np.int64(555), 67), (np.int64(531), 45), (np.int64(533), 44), (np.int64(403), 39), (np.int64(321), 34), (np.int64(225), 31), (np.int64(315), 24), (np.int64(512), 23), (np.int64(532), 22), (np.int64(553), 22), (np.int64(252), 16), (np.int64(345), 12), (np.int64(401), 7), (np.int64(-9223372036854775808), 4)]
col4 [  nan 0.307 1.   ] col5 [-1.013  0.074  1.005] col6 [-3.142 -0.626  5.027] col7 [0.809 1.66  2.4  ]
[ 1 44 21 61  3 22  2  3 52 12 23  0  0  0  0] [ 1.    8.77  9.28  9.29 10.25 11.45 11.6  12.68 12.73 13.93 13.94  0.    0.    0.    0.  ]
Traceback (most recent call last):
  File "<stdin>", line 15, in <module>
ValueError: cannot convert float NaN to integer
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF' 2>&1 | grep -v Warn
import pickle, numpy as np, collections
S=pickle.load(open('survey_hc-12.pkl','rb'))
np.set_printoptions(linewidth=220,suppress=True,precision=3)
k=list(S)[0]; r=S[k]; na=r['newallo']; t=r['t60']; cm=na['codematrix']; tm=na['timematrix']
t=t[np.isfinite(t[:,10])]
for i in range(4):
    a,b=tm[i,2],tm[i+1,2]
    seg=t[(t[:,0]>=a)&(t[:,0]<b)]
    print(cm[i], tm[i].round(2))
    ch=np.r_[0,np.nonzero(np.diff(seg[:,10]))[0]+1]
    for j in ch: print('   t=%.2f tag=%d x=%.1f y=%.1f th=%.0f c4=%.2f c5=%.2f c6=%.2f c7=%.2f c11=%.4f'%(seg[j,0],seg[j,10],seg[j,1],seg[j,2],seg[j,3],seg[j,4],seg[j,5],seg[j,6],seg[j,7],seg[j,11]))
EOF
```

```
[ 1 44 21 61  3 22  2  3 52 12 23  0  0  0  0] [ 1.    8.77  9.28  9.29 10.25 11.45 11.6  12.68 12.73 13.93 13.94  0.    0.    0.    0.  ]
   t=9.58 tag=105 x=-4.9 y=15.2 th=18 c4=1.00 c5=1.00 c6=1.26 c7=2.00 c11=2.0001
   t=11.41 tag=253 x=0.0 y=0.0 th=18 c4=0.00 c5=-0.00 c6=1.25 c7=1.00 c11=2.0001
   t=12.75 tag=403 x=0.3 y=-0.2 th=54 c4=0.02 c5=0.02 c6=0.63 c7=1.02 c11=2.0001
   t=14.08 tag=532 x=12.9 y=-9.4 th=55 c4=1.00 c5=-0.00 c6=0.62 c7=2.01 c11=2.0001
[ 2 41 21 61  3 22  1  3 53 11 23  0  0  0  0] [ 2.   15.13 17.66 17.67 17.67 18.73 18.76 19.71 19.78 20.98 20.98  0.    0.    0.    0.  ]
   t=17.75 tag=102 x=-4.5 y=-13.8 th=162 c4=0.91 c5=0.91 c6=5.03 c7=1.91 c11=2.1002
   t=18.75 tag=224 x=0.0 y=0.0 th=162 c4=0.00 c5=0.00 c6=-1.25 c7=1.00 c11=2.1002
   t=19.91 tag=404 x=1.7 y=1.2 th=126 c4=0.13 c5=0.13 c6=-0.63 c7=1.13 c11=2.1002
   t=21.08 tag=541 x=12.9 y=9.4 th=126 c4=1.00 c5=0.00 c6=-0.63 c7=2.00 c11=2.1002
[ 3 40 21 61  3 22  2  3 53 11 23  0  0  0  0] [ 3.   22.18 24.71 24.71 24.72 25.83 25.85 26.63 26.63 27.83 27.83  0.    0.    0.    0.  ]
   t=24.75 tag=101 x=-15.5 y=0.0 th=90 c4=0.97 c5=0.97 c6=0.00 c7=1.97 c11=2.1003
   t=25.91 tag=214 x=0.0 y=0.0 th=93 c4=0.00 c5=-0.08 c6=-0.05 c7=1.00 c11=2.1003
   t=26.75 tag=404 x=1.3 y=1.0 th=126 c4=0.10 c5=0.10 c6=-0.63 c7=1.10 c11=2.1003
   t=27.91 tag=543 x=12.9 y=9.4 th=126 c4=1.00 c5=-0.00 c6=-0.63 c7=2.00 c11=2.1003
[ 4 42 21 61  3 22  1  3 54 12 23  0  0  0  0] [ 4.   29.03 31.56 31.56 31.57 32.61 32.68 33.46 33.46 34.66 34.66  0.    0.    0.    0.  ]
   t=31.58 tag=103 x=12.7 y=-9.3 th=234 c4=0.98 c5=0.98 c6=3.77 c7=1.98 c11=2.0004
   t=32.75 tag=235 x=0.0 y=0.0 th=231 c4=0.00 c5=0.09 c6=-2.46 c7=1.00 c11=2.0004
   t=33.58 tag=405 x=-0.6 y=1.8 th=198 c4=0.12 c5=0.12 c6=-1.88 c7=1.12 c11=2.0004
   t=34.75 tag=552 x=-4.9 y=15.2 th=198 c4=1.00 c5=0.00 c6=-1.88 c7=2.00 c11=2.0004
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper && wc -w *.txt; grep -n -i -E "learning curve|\[60\]|state.space model|Smith|chance level|confidence bound" 10.1371-journal.pbio.2001045.txt | head -30
```

```
14947 10.1371-journal.pbio.2001045.txt
  1037 hc-12.data-description.txt
  1246 hc-21.data-description.txt
 17230 total
31:Animals quickly solved the task. On average, both animals learned to reach the rewarded arm in a dozen trials ( S3A and S3B Fig ); monkey S performed above chance after 12.3 ± 2 trials (SEM), and monkey K did so after 14.8 ± 2.4 trials. From then to when the upper confidence bound of success reached 90%, less than 10 trials were usually necessary (89% of sessions).
249:Learning curves: performance as a function of trials. A. Average probability of a correct response over the course of a testing block of 80 trials. B. Learning curves in three representative individual sessions in monkey K (top) and monkey S (bottom). Dots illustrate trial outcome (blue: rewarded, red: non-rewarded). The solid blue line represents the probability of a correct response, and the dotted lines are the upper and lower confidence bounds (methods based on [ 60 ]). As the reward was never positioned at the end of the entry arm, we considered that learning of the reward position was manifest when the lower confidence bound exceeded 1/4 (black vertical line). C. Examples of performance during two individual sessions (monkey K, top; Monkey S, bottom). Each dot represents a correct (blue) or incorrect (red) response (i.e., the monkey did or did not reach the rewarded arm) as a function of trial number (x axis) for the different entries (y axis: starting positions). On the top row, animal K started from entry 1 for the first 36 trials and usually performed incorrectly until the 30 th trial, after which the animal performed correctly. On the 37 th trial, the animal was asked to reach the reward by starting trials from the other 3 entries. Despite the fact that the animal had never tried to reach the reward from these entries before, the animal performed correctly proving that it used the information acquired on the previous 36 trials to deduce the reward position with respect t
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^#" 10.1371-journal.pbio.2001045.txt | head -80
```

```
11:## Introduction
17:## Results
19:## Animals use direction and compute trajectory in the virtual world
25:## Experimental setup and behavioral task.
37:## What is encoded in hippocampal cell activity?
47:## Individual examples of cell activity in the four coding spaces studied.
51:## Sensitivity of the cells to a combination of variables
59:## Population statistics.
65:## Direction selectivity
69:## Hippocampal cells encode a fine-grained state-space representation of the maze
73:## Cells discriminate different contexts for the same position and direction
79:## State-space selectivity.
83:## Cells encode landmark identity and distance with respect to landmark
89:## Sensitivity to landmark identity and relative distance.
93:## Landmark-triggered activity and viewpoint dependence
101:## Landmark viewpoint-invariant versus viewpoint-dependent cells.
105:## Visual exploration and hippocampal activity dynamics
111:## Modulation of cell selectivity by the point of gaze.
117:## Discussion
123:## Wayfinding in virtual reality
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '159,215p;239,245p;371,380p' 10.1371-journal.pbio.2001045.txt; sed -n '65,92p' 10.1371-journal.pbio.2001045.txt
```

```
## Behavioral methods and setup

Animals were head restrained and placed in front of a large screen (152 x 114 cm) at a distance of 101 cm. They were further equipped with active shutter glasses (Nuvision) coupled to the computer for 3-D projection (DepthQ projector, Infocus) of a virtual world (Monkey3D, Holodia, S1 – S3 Movies). The projection parameters were calibrated to render objects’ size real by calibrating disparity using the actual interpupillary distance of the monkeys (3.1 cm for monkey K and 3.0 cm for monkey S). We confirmed the animals perceived images with the depth of stereoscopic projection by measuring vergence as a small object moved from an apparent 50 cm in front of the screen to 150 cm behind the screen. To this end, two small infrared cameras were mounted above each eye and the movement of the pupils of each eye was monitored (ASL). The cameras further allowed monitoring the animal’s gaze through the task. Animals learned to navigate via the joystick towards a reward hidden at the end of one of the star maze’s arms ( Fig 1B , S1 – S3 Movies). The star maze had a radius of 16 m and speed of displacement was 5 m per second. This velocity was chosen to optimize the number of rewarded trials in a session and prevent the animals from getting too impatient. During a shaping period that lasted 6 mo, animals learned to find the reward targets whilst operating a joystick that controlled a sphere on the screen. Once they had mastered this task, they were introduced to a 3-D version of this task. Then, they were introduced to a simple Y maze in which they had to move the joystick to approach the sphere. Next, landmarks were introduced along the Y maze, and animals were trained with the sphere in presence of the landmarks. Then, the sphere was removed and animals were rewarded when they went toward the end of the arm where the sphere was last. To this end, they had to use the landmarks. At this point, they were introduced to the full star maze. For one a
[... 88 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd  && sed -n 1,60p entries/fouke-2025/omr.py; python -c "import json,nbformat; nb=nbformat.read('entries/fouke-2025/reproduce_fouke_2025.ipynb',4); [print(c.cell_type, c.metadata.get('tags'), c.source[:300].replace('\n',' | ')) for c in nb.cells[:8]]"; cat entries/fouke-2025/README.md | head -30
```

```
Fri Nov 13 12:14:09 UTC 2026
"""Loading and measures for the freely swimming optomotor data of dandiset 001453.

Fouke, He, Loring & Naumann (2025), Current Biology, doi:10.1016/j.cub.2025.04.027.

Each NWB file holds one fish: x and y position (pixels), heading (`f0_theta`, radians), its
change per frame (`f0_vtheta`; the file says radians/s, the data show radians per frame),
velocity estimates, and per frame the stimulus code and trial number (`stim_index`). Files are
streamed from the archive at the pinned version; nothing is written to disk.

Where the parameters come from:

- Trial processing follows the paper's analysis notebook, Fig1-S1.ipynb, in
  https://gitlab.oit.duke.edu/ean26/danionella_omr_neuralcircuits2025 at commit
  33a5c297ff4ab6ff49f6bdd96139e9fdd867025c (the Methods give none of these): Savitzky-Golay
  smoothing of positions (21 frames, order 2); rejection of trials whose absolute cumulative
  heading change exceeds 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or
  whose mean speed exceeds 100 mm/s; measures from 3 s to 35 s after the first tracked frame;
  10 pixels per mm (the code divides pixels per second by 10 to give mm/s); per fish the median
  over trials. The 3 s stationary phase and the 32 s of motion are in the Methods.
[... 78 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/wirth-2017/wirth.py",
 "content": "\"\"\"Loading and measures for CRCNS hc-12 (and hc-21), the data of Wirth, Baraduc, Plante,\nPinede & Duhamel (2017), PLoS Biology 15(2), e2001045, doi:10.1371/journal.pbio.2001045.\n\nThe data sets are single tar.gz archives of MATLAB files, one file per cell, in the public S3\nbucket crcnsarchive. They are streamed: the archive is decompressed as it is read and each\nmember is loaded in memory and reduced to what the analysis needs, one at a time. Nothing is\nwritten to disk.\n\nFile layout (descriptor of hc-12, version 0.7, and the files themselves): spike times\n(`file.elec`, or `file.newallo.elec` when the top level has none), the trial tables of the new\nmaze (`newallo.codematrix`, `newallo.timematrix`), learning curves, eye positions at 250 Hz\nwith `eye_times`, and `camera_data.time_60`, 60 Hz rows of [time, x, y, camera orientation\n(deg), curvilinear abscissa on the maze branch (0 centre, 1 arm end), state-space curvilinear\nabscissa, state-space polar angle, state-space radius, next, previous and current transition\ntag, composite maze tag]. `time_60` sits under `newallo.camera_data` in some files.\n\nWhere the parameters come from:\n\n- Successful trials only; maps unsmoothed; a bin is valid with at least four successful\n  trials (Methods, Activity maps) and more than 400 ms of time in successful trials (Methods,\n  Information Content). The resolution of each map is stepped until the number of valid bins\n  is as close to 200 as possible (Methods, Information Content). The steps (square bins for\n  position and state space, equal angular bins for direction) are a standard choice; the\n  square grids follow the dataset's own scripts (simple_place_cell_square_script_theta_r.m,\n  1 m squares of x, y; star_remapped_cell_r.m, squares of the planar state-space projection\n  pol2cart(time_60 columns 7 and 8)), which also show that the state-space map is a map of\n  that planar projection.\n- Skaggs information in bits per spike and the sparsity index as written in the Methods\n  (Information Content; Sparsity index). Normalized values subtract the mean of 999 surrogates.\n- Surrogates (Methods, Permutation statistics): the recording time of the new-maze session is\n  cut into 5 s chunks that are \"randomly shifted\". Reading \"permute\" (claims file, Method W\n  (a)): the order of the chunks of the spike train is permuted. Reading \"shift\" (Method W\n  (b)): each chunk is moved by an independent random offset, circularly. The p-value is\n  bilateral, twice the smaller tail fraction of the rank among 1,000 (claims file, a standard\n  choice); one-tailed fractions are kept for the claims that count each tail.\n- Trial windows (claims file, Method W): reading \"full\", trial start (code 21) to the next\n  trial start, so the passive return after the trial belongs to it; reading \"toreward\",\n  trial start to reward (code 11).\n- Maze centre: transition tags 2xy and 3xy (rotations at the centre); return paths: tags 5xy\n  (descriptor, transition tags). Entry paths: tags 10x, x = start arm code - 39 (shown in the\n  notebook from the files).\n- State-space selectivity (Methods, State-space selectivity): 3.6 degree bins, three move\n  types, at least 400 ms in each of at least two types. The three types are read as the 36\n  degree alignment (tags 2xy), a 72 degree rotation to the right and one to the left (tags\n  3xy, split by the sign of the change of camera orientation); an assumption, as the paper\n  does not name them.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport io\nimport tarfile\n\nimport fsspec\nimport numpy as np\nimport scipy.io as sio\nfrom scipy import sparse\n\nBUCKET = \"https://crcnsarchive.s3-us-west-2.amazonaws.com\"\nARCHIVES = {\"hc-12\": f\"{BUCKET}/hc-12/live/data.tar.gz\",\n            \"hc-21\": f\"{BUCKET}/hc-21/live/data.tar.gz\"}\nMD5 = {\"hc-12\": \"426c7d00c0358f2cc9873e0dbb331e2f\",   # checksums.md5 of each data set\n       \"hc-21\": \"dee5e8aa4a7b3c44b61b8cecfe622a0a\"}\n\nDT = 1 / 60                   # camera rows are 60 Hz\nMIN_BIN_S = 0.4               # Methods, Information Content\nMIN_TRIALS = 4                # Methods, Activity maps\nTARGET_BINS = 200             # Methods, Information Content\nCHUNK_S = 5.0                 # Methods, Permutation statistics\nN_SURR = 999\nSSI_BIN_DEG = 3.6             # Methods, State-space selectivity\n\nPOS_STEPS = np.round(np.arange(0.4, 8.01, 0.1), 2)          # m, square bins\nSTATE_STEPS = np.round(np.arange(0.02, 0.60, 0.005), 3)     # planar state-space units\nDIR_STEPS = np.arange(8, 721)                                # number of angular bins\n\n\n# ---------------------------------------------------------------- loading\n\ndef stream_members(dataset):\n    \"\"\"Yield (member name, loaded MATLAB dict) for every .mat file of a data set's archive.\"\"\"\n    f = fsspec.open(ARCHIVES[dataset], block_size=2**22).open()\n    with tarfile.open(fileobj=f, mode=\"r|gz\") as tf:\n        for m in tf:\n            if m.isfile() and m.name.endswith(\".mat\"):\n                yield m.name.split(\"/\")[-1], sio.loadmat(io.BytesIO(tf.extractfile(m).read()))\n\n\ndef _field(s, name):\n    return s[name] if (s.dtype.names and name in s.dtype.names) else None\n\n\ndef reduce_file(name, d, maze=\"newallo\"):\n    \"\"\"Reduce one cell file to the arrays used here; None when it has no `maze` trials.\"\"\"\n    fl = d[\"file\"][0, 0]\n    mz = _field(fl, maze)\n    if mz is None or mz.dtype.names is None:\n        return None\n    mz = mz[0, 0]\n    el = _field(fl, \"elec\")\n    spike_src = \"file.elec\"\n    if el is None or el.size == 0:\n        el = _field(mz, \"elec\")\n        spike_src = f\"{maze}.elec\"\n    cd = _field(fl, \"camera_data\")\n    if cd is None:\n        cd = _field(mz, \"camera_data\")\n    t60 = np.asarray(cd[0, 0][\"time_60\"], float)\n    cm = np.asarray(mz[\"codematrix\"], float)\n    tm = np.asarray(mz[\"timematrix\"], float)\n    lc = _field(mz, \"learning_curves\")\n    lt = _field(mz, \"learningtrial\")\n    out = {\"name\": name, \"monkey\": name[:2], \"session\": name.split(\"_\")[0],\n           \"spikes\": np.sort(np.asarray(el, float).ravel()), \"spike_src\": spike_src,\n           \"cm\": cm, \"tm\": tm,\n           \"lc\": None if lc is None else np.asarray(lc, float),\n           \"learningtrial\": None if lt is None or lt.size == 0 else float(lt.ravel()[0]),\n           \"reclocation\": None if _field(fl, \"reclocation\") is None\n           else np.asarray(fl[\"reclocation\"], float).ravel()}\n    # session window: first trial start to last trial end (as the dataset's scripts do)\n    t0 = _code_times(cm, tm, 21)\n    t0 = np.nanmin(t0)\n    t1 = np.nanmax(np.where(cm[:, 1:] > 0, tm[:, 1:], np.nan))\n    keep = (t60[:, 0] >= t0) & (t60[:, 0] <= t1 + 1.0) & np.isfinite(t60[:, 10])\n    t60 = t60[keep]\n    t60 = t60[np.argsort(t60[:, 0], kind=\"stable\")]\n    out[\"t60\"] = t60.astype(np.float64)\n    out[\"window\"] = (t0, t1)\n    et = _field(fl, \"eye_times\")\n    if et is not None and et.size:\n        et = np.asarray(et, float).ravel()\n        w = (et >= t0 - 1) & (et <= t1 + 1)\n        eyes = {}\n        for e in (\"left_eye\", \"right_eye\"):\n            s = _field(fl, e)\n            if s is None:\n                continue\n            s = s[0, 0]\n            for c in (\"hor\", \"ver\"):\n                v = np.asarray(s[c], float).ravel()\n                n = min(len(v), len(et))\n                eyes[f\"{e[0]}_{c}\"] = v[:n][w[:n]].astype(np.float32)\n        n = min(len(v) for v in eyes.values()) if eyes else 0\n        out[\"eye_t\"] = et[w][:n]\n        out[\"eye\"] = {k: v[:n] for k, v in eyes.items()}\n    else:\n        out[\"eye_t\"] = None\n        out[\"eye\"] = None\n    return out\n\n\ndef _code_times(cm, tm, code):\n    \"\"\"Per trial, the time of the first occurrence of an event code (NaN if absent).\"\"\"\n    hit = cm[:, 1:] == code\n    first = np.where(hit.any(1), hit.argmax(1) + 1, -1)\n    return np.where(first > 0, tm[np.arange(len(cm)), np.maximum(first, 0)], np.nan)\n\n\ndef trials(c):\n    \"\"\"Per-trial table: start arm (1-5), chosen arm (1-5), outcome, event times.\"\"\"\n    cm, tm = c[\"cm\"], c[\"tm\"]\n    start_code = np.array([next((v for v in row[1:] if 40 <= v <= 44), np.nan) for row in cm])\n    chosen = np.array([next((v for v in row[1:] if 50 <= v <= 54), np.nan) for row in cm])\n    turns = [[int(v) for v in row[1:] if v in (1, 2)] for row in cm]\n    turn_t = [[t for v, t in zip(row[1:], trow[1:]) if v in (1, 2)] for row, trow in zip(cm, tm)]\n    return {\"start_arm\": start_code - 39, \"chosen_arm\": chosen - 49,\n            \"correct\": (cm[:, 1:] == 11).any(1), \"error\": (cm[:, 1:] == 12).any(1),\n            \"t_start\": _code_times(cm, tm, 21), \"t_center\": _code_times(cm, tm, 22),\n            \"t_reward\": _code_times(cm, tm, 11), \"t_end\": _code_times(cm, tm, 23),\n            \"turns\": turns, \"turn_t\": turn_t}\n\n\n# ---------------------------------------------------------------- frames and bins\n\ndef frame_table(c, reading=\"full\"):\n    \"\"\"Per camera frame: trial index (or -1), whether it is analysed (successful trial).\"\"\"\n    t = c[\"t60\"][:, 0]\n    tr = trials(c)\n    ts = tr[\"t_start\"]\n    n = len(ts)\n    trial = np.full(len(t), -1)\n    for i in range(n):\n        if not np.isfinite(ts[i]):\n            continue\n        if reading == \"full\":\n            nxt = ts[i + 1] if i + 1 < n and np.isfinite(ts[i + 1]) else tr[\"t_end\"][i] + 1.0\n            end = nxt\n        else:  # \"toreward\"\n            end = tr[\"t_reward\"][i]\n            if not np.isfinite(end):\n                continue\n        trial[(t >= ts[i]) & (t < end)] = i\n    ok = (trial >= 0) & tr[\"correct\"][np.maximum(trial, 0)]\n    return trial, ok\n\n\ndef spike_counts(c):\n    \"\"\"Spikes per camera frame, frame k covering [t_k, t_k + 1/60).\"\"\"\n    t = c[\"t60\"][:, 0]\n    sp = c[\"spikes\"]\n    lo = np.searchsorted(sp, t)\n    hi = np.searchsorted(sp, t + DT)\n    return (hi - lo).astype(np.float64)\n\n\ndef space_coords(c):\n    t60 = c[\"t60\"]\n    th, rho = t60[:, 6], t60[:, 7]\n    return {\"position\": (t60[:, 1], t60[:, 2]),\n            \"direction\": (np.mod(t60[:, 3], 360.0),),\n            \"state\": (rho * np.cos(th), rho * np.sin(th))}\n\n\ndef _bin_index(coords, step, kind):\n    if kind == \"direction\":\n        nb = int(step)\n        b = np.floor(coords[0] / (360.0 / nb)).astype(int)\n        return np.clip(b, 0, nb - 1), nb\n    x, y = coords\n    lo = -25.0 if kind == \"position\" else -3.0\n    nx = int(np.ceil(2 * -lo / step))\n    bx = np.floor((x - lo) / step).astype(int)\n    by = np.floor((y - lo) / step).astype(int)\n    good = np.isfinite(x) & np.isfinite(y)\n    b = np.where(good, by * nx + bx, -1)\n    return b, nx * nx\n\n\ndef valid_bins(b, nb, ok, trial):\n    \"\"\"Occupancy (s) per bin over analysed frames and the valid mask (>400 ms, >=4 trials).\"\"\"\n    sel = ok & (b >= 0)\n    occ = np.bincount(b[sel], minlength=nb) * DT\n    pairs = np.unique(b[sel].astype(np.int64) * 100000 + trial[sel])\n    ntr = np.bincount((pairs // 100000).astype(int), minlength=nb)\n    return occ, (occ > MIN_BIN_S) & (ntr >= MIN_TRIALS)\n\n\ndef choose_resolution(coords, kind, ok, trial):\n    \"\"\"Step the resolution until the number of valid bins is closest to 200.\"\"\"\n    steps = {\"position\": POS_STEPS, \"state\": STATE_STEPS, \"direction\": DIR_STEPS}[kind]\n    best = None\n    for s in steps:\n        b, nb = _bin_index(coords, s, kind)\n        occ, val = valid_bins(b, nb, ok, trial)\n        d = abs(int(val.sum()) - TARGET_BINS)\n        if best is None or d < best[0]:\n            best = (d, s, b, nb, occ, val)\n    _, s, b, nb, occ, val = best\n    return {\"step\": s, \"bins\": b, \"nb\": nb, \"occ\": occ, \"valid\": val}\n\n\ndef design(mask_frames, b, valid):\n    \"\"\"Sparse frames x valid-bins indicator for the frames in mask_frames.\"\"\"\n    vidx = -np.ones(len(valid), int)\n    vidx[valid] = np.arange(valid.sum())\n    rows = np.nonzero(mask_frames & (b >= 0))[0]\n    cols = vidx[b[rows]]\n    keep = cols >= 0\n    return sparse.csr_matrix((np.ones(keep.sum()), (rows[keep], cols[keep])),\n                             shape=(len(b), int(valid.sum())))\n\n\n# ---------------------------------------------------------------- measures\n\ndef skaggs_ic(counts, occ):\n    \"\"\"Skaggs information (bits/spike); counts (..., M) spikes per bin, occ (M,) seconds.\"\"\"\n    p = occ / occ.sum()\n    lam = counts / occ\n    mean = (lam * p).sum(-1, keepdims=True)\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        r = lam / mean\n        term = np.where(r > 0, p * r * np.log2(r), 0.0)\n    out = term.sum(-1)\n    return np.where(mean[..., 0] > 0, out, np.nan)\n\n\ndef sparsity(counts, occ):\n    \"\"\"(M - (sum rate)^2 / sum rate^2) / (M - 1), Methods, Sparsity index.\"\"\"\n    lam = counts / occ\n    m = lam.shape[-1]\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        s = (m - lam.sum(-1) ** 2 / (lam ** 2).sum(-1)) / (m - 1)\n    return s\n\n\ndef uncentered_corr(a, b):\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        return (a * b).sum(-1) / np.sqrt((a ** 2).sum(-1) * (b ** 2).sum(-1))\n\n\ndef surrogate_counts(s, rng, reading, n=N_SURR, batch=111):\n    \"\"\"Yield batches of surrogate spike-count series (batch x T).\"\"\"\n    T = len(s)\n    L = int(round(CHUNK_S / DT))\n    nch = T // L\n    done = 0\n    while done < n:\n        k = min(batch, n - done)\n        out = np.empty((k, T))\n        for i in range(k):\n            if reading == \"permute\":\n                perm = rng.permutation(nch)\n                body = s[: nch * L].reshape(nch, L)[perm].ravel()\n                out[i] = np.concatenate([body, s[nch * L:]])\n            else:  # \"shift\": each chunk moved by an independent random offset, circularly\n                src = np.arange(T)\n                ch = np.minimum(src // L, nch)  # the remainder is one more chunk\n                offs = rng.integers(0, T, size=nch + 1)\n                tgt = (src - (ch * L) + ch * L + offs[ch]) % T\n                out[i] = np.bincount(tgt, weights=s, minlength=T)\n        done += k\n        yield out\n\n\ndef tail_p(actual, surr):\n    \"\"\"Rank p-values among actual + surrogates: (bilateral, upper, lower).\"\"\"\n    surr = np.asarray(surr)\n    n = surr.shape[0] + 1\n    up = (1 + np.sum(surr >= actual, 0)) / n\n    lo = (1 + np.sum(surr <= actual, 0)) / n\n    return np.minimum(1.0, 2 * np.minimum(up, lo)), up, lo\n\n\ndef lower_bound_criterion(lc_lower, chance=0.25):\n    \"\"\"First trial (1-based) at which the lower bound exceeds chance, or NaN (S3B legend).\"\"\"\n    i = np.nonzero(lc_lower > chance)[0]\n    return float(i[0] + 1) if len(i) else np.nan\n\n\ndef binom_upper(k, n, p):\n    from scipy.stats import binom\n    return float(binom.sf(k - 1, n, p))\n"
}
```

```
File created successfully at: entries/wirth-2017/wirth.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/wirth-2017 && python - <<'EOF'
s=open('wirth.py').read()
s=s.replace("""                src = np.arange(T)
                ch = np.minimum(src // L, nch)  # the remainder is one more chunk
                offs = rng.integers(0, T, size=nch + 1)
                tgt = (src - (ch * L) + ch * L + offs[ch]) % T""","""                src = np.arange(T)
                ch = np.minimum(src // L, nch)  # the remainder is one more chunk
                offs = rng.integers(0, T, size=nch + 1)
                tgt = (src + offs[ch]) % T""")
open('wirth.py','w').write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cat >> wirth.py <<'EOF'


# ---------------------------------------------------------------- per-cell analysis

SHIFTS_S = (-5.0, -2.0, -1.0, -0.5, -0.25, 0.0, 0.25, 0.5, 1.0, 2.0, 5.0)


def turn_types(c):
    """Per frame: 0 for a 36 degree alignment (tag 2xy), 1 for a 72 degree rotation to the
    right, 2 to the left (tags 3xy, by the sign of the orientation change over the run of
    frames carrying the tag), -1 elsewhere. A right turn (code 1) lowers the camera
    orientation, as the notebook shows from the files."""
    tag = c["t60"][:, 10]
    th = c["t60"][:, 3]
    out = np.full(len(tag), -1)
    out[(tag >= 200) & (tag < 300)] = 0
    is3 = (tag >= 300) & (tag < 400)
    if is3.any():
        brk = np.nonzero(np.diff(np.r_[0, is3.astype(int), 0]))[0]
        dth = np.r_[0, (np.diff(th) + 180) % 360 - 180]
        for a, b in zip(brk[::2], brk[1::2]):
            tot = dth[a + 1:b].sum() if b - a > 1 else 0.0
            same = np.ones(b - a, bool)
            # split runs where the tag value changes
            vals = tag[a:b]
            for v in np.unique(vals):
                idx = np.arange(a, b)[vals == v]
                tv = dth[idx[1:]].sum() if len(idx) > 1 else tot
                out[idx] = 1 if tv < 0 else 2
    return out


class Session:
    """Behaviour-only quantities shared by the cells of one session (same trial table)."""

    def __init__(self, c):
        self.t60 = c["t60"]
        self.tag = c["t60"][:, 10]
        self.coords = space_coords(c)
        self.tables = {r: frame_table(c, r) for r in ("full", "toreward")}
        self.res = {}
        for r, (trial, ok) in self.tables.items():
            for kind, xy in self.coords.items():
                self.res[(r, kind)] = choose_resolution(xy, kind, ok, trial)
        trial, ok = self.tables["full"]
        self.center = ok & (self.tag >= 200) & (self.tag < 400)
        self.ret = ok & (self.tag >= 500) & (self.tag < 600)
        self.entry = ok & (self.tag >= 100) & (self.tag < 200)
        # common direction resolution for centre and return maps
        best = None
        d = self.coords["direction"]
        for nb in DIR_STEPS:
            b, _ = _bin_index(d, nb, "direction")
            oc, vc = valid_bins(b, nb, self.center, trial)
            orr, vr = valid_bins(b, nb, self.ret, trial)
            k = abs(int((vc & vr).sum()) - TARGET_BINS)
            if best is None or k < best[0]:
                best = (k, nb, b, oc, vc, orr, vr)
        _, nb, b, oc, vc, orr, vr = best
        self.cr = {"nb": nb, "bins": b, "occ_c": oc, "val_c": vc, "occ_r": orr, "val_r": vr}
        # state-space selectivity layout: 3.6 degree bins x 3 move types, centre frames
        types = turn_types(c)
        nbin = int(round(360 / SSI_BIN_DEG))
        db = np.clip(np.floor(np.mod(self.t60[:, 3], 360) / SSI_BIN_DEG).astype(int), 0, nbin - 1)
        col = np.where(self.center & (types >= 0), db * 3 + np.maximum(types, 0), -1)
        occ = np.bincount(col[col >= 0], minlength=nbin * 3).reshape(nbin, 3) * DT
        self.ssi = {"col": col, "occ": occ, "nbin": nbin}
        self.types = types
        # designs
        self.designs = {}
        for (r, kind), rr in self.res.items():
            okr = self.tables[r][1]
            self.designs[(r, kind)] = design(okr, rr["bins"], rr["valid"])
        self.designs["center"] = design(self.center, b, vc)
        self.designs["return"] = design(self.ret, b, vr)
        both = vc & vr
        self.designs["center_common"] = design(self.center, b, both)
        self.designs["return_common"] = design(self.ret, b, both)
        self.occ_common = (oc[both], orr[both])
        good = col >= 0
        self.designs["ssi"] = sparse.csr_matrix(
            (np.ones(good.sum()), (np.nonzero(good)[0], col[good])), shape=(len(col), nbin * 3))


def _occ(sess, key):
    if key in sess.res:
        rr = sess.res[key]
        return rr["occ"][rr["valid"]]
    if key == "center":
        return sess.cr["occ_c"][sess.cr["val_c"]]
    if key == "return":
        return sess.cr["occ_r"][sess.cr["val_r"]]
    raise KeyError(key)


def ssi_index(counts, occ):
    """SSI over bins with >= 400 ms in each of >= 2 move types (Methods, State-space
    selectivity); counts (..., nbin*3)."""
    nbin = occ.shape[0]
    cnt = counts.reshape(counts.shape[:-1] + (nbin, 3))
    good_t = occ >= MIN_BIN_S
    good_b = good_t.sum(1) >= 2
    with np.errstate(divide="ignore", invalid="ignore"):
        lam = np.where(good_t, cnt / occ, np.nan)
    lam = lam[..., good_b, :]
    mx = np.nanmax(lam, -1)
    mn = np.nanmin(lam, -1)
    with np.errstate(divide="ignore", invalid="ignore"):
        return (mx - mn).sum(-1) / (mx + mn).sum(-1), int(good_b.sum())


def analyse_cell(c, sess, seed):
    """All map measures of one cell with their surrogates, both surrogate readings."""
    s = spike_counts(c)
    out = {"name": c["name"], "monkey": c["monkey"], "session": c["session"],
           "n_spikes_window": int(s.sum()), "n_spikes_file": int(len(c["spikes"])),
           "spike_src": c["spike_src"]}
    keys = [k for k in sess.designs if isinstance(k, tuple)] + ["center", "return"]
    actual = {k: s @ sess.designs[k] for k in keys}
    act_cc = (s @ sess.designs["center_common"], s @ sess.designs["return_common"])
    act_ssi = s @ sess.designs["ssi"]
    for k in keys:
        occ = _occ(sess, k)
        out[f"ic|{k}"] = float(skaggs_ic(actual[k], occ)) if len(occ) else np.nan
        out[f"sp|{k}"] = float(sparsity(actual[k], occ)) if len(occ) > 1 else np.nan
        out[f"nbins|{k}"] = int(len(occ))
    oc_c, oc_r = sess.occ_common
    out["corr"] = float(uncentered_corr(act_cc[0] / oc_c, act_cc[1] / oc_r)) if len(oc_c) else np.nan
    out["n_common"] = int(len(oc_c))
    ssi_a, nb_ssi = ssi_index(act_ssi, sess.ssi["occ"])
    out["ssi"] = float(ssi_a)
    out["ssi_bins"] = nb_ssi
    for sr, sub in (("permute", 1), ("shift", 2)):
        rng = np.random.default_rng([seed, sub])
        surr = {k: [] for k in keys}
        surr_cc, surr_ssi = [], []
        for S in surrogate_counts(s, rng, sr):
            St = S.T
            for k in keys:
                surr[k].append((sess.designs[k].T @ St).T)
            surr_cc.append(((sess.designs["center_common"].T @ St).T,
                            (sess.designs["return_common"].T @ St).T))
            surr_ssi.append((sess.designs["ssi"].T @ St).T)
        stats = {}
        for k in keys:
            occ = _occ(sess, k)
            cnts = np.vstack(surr[k])
            if len(occ) < 2:
                continue
            ic_s = skaggs_ic(cnts, occ)
            sp_s = sparsity(cnts, occ)
            stats[k] = (ic_s, sp_s)
            for meas, a, sv in (("ic", out[f"ic|{k}"], ic_s), ("sp", out[f"sp|{k}"], sp_s)):
                sv = sv[np.isfinite(sv)]
                p2, pu, pl = tail_p(a, sv)
                out[f"{meas}n|{k}|{sr}"] = float(a - sv.mean()) if len(sv) else np.nan
                out[f"{meas}p|{k}|{sr}"] = float(p2)
        # sparsity and IC differences, state space minus another space (per trial reading)
        for r in ("full", "toreward"):
            st = (r, "state")
            for other in ("position", "direction"):
                ok_ = (r, other)
                if st in stats and ok_ in stats:
                    for j, meas in ((1, "sp"), (0, "ic")):
                        a = out[f"{meas}|{st}"] - out[f"{meas}|{ok_}"]
                        d = stats[st][j] - stats[ok_][j]
                        d = d[np.isfinite(d)]
                        p2, pu, pl = tail_p(a, d)
                        out[f"{meas}diffp|{r}|{other}|{sr}"] = float(p2)
        if len(oc_c):
            cc = np.vstack([x[0] for x in surr_cc]) / oc_c
            rr = np.vstack([x[1] for x in surr_cc]) / oc_r
            cs = uncentered_corr(cc, rr)
            cs = cs[np.isfinite(cs)]
            p2, pu, pl = tail_p(out["corr"], cs)
            out[f"corr_up|{sr}"], out[f"corr_lo|{sr}"] = float(pu), float(pl)
            out[f"corrn|{sr}"] = float(out["corr"] - cs.mean()) if len(cs) else np.nan
        ss, _ = ssi_index(np.vstack(surr_ssi), sess.ssi["occ"])
        ss = ss[np.isfinite(ss)]
        if np.isfinite(ssi_a) and len(ss):
            p2, pu, pl = tail_p(ssi_a, ss)
            out[f"ssin|{sr}"] = float(ssi_a - ss.mean())
            out[f"ssi_up|{sr}"], out[f"ssi_lo|{sr}"] = float(pu), float(pl)
    # clock check: state-space IC with the spikes shifted in time
    key = ("full", "state")
    occ = _occ(sess, key)
    t = c["t60"][:, 0]
    for sh in SHIFTS_S:
        sp = c["spikes"] + sh
        cnt = (np.searchsorted(sp, t + DT) - np.searchsorted(sp, t)).astype(float)
        out[f"shift_ic|{sh}"] = float(skaggs_ic(cnt @ sess.designs[key], occ))
    return out, s
EOF
date -u
```

```
Fri Nov 13 12:16:08 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > dev1.py <<'EOF'
import sys, time, pickle, resource
sys.path.insert(0,'entries/wirth-2017')
import wirth, numpy as np
cells=[]
t=time.time()
for i,(name,d) in enumerate(wirth.stream_members('hc-12')):
    c=wirth.reduce_file(name,d)
    if c: cells.append(c)
    if len(cells)>=6: break
print('load',time.time()-t)
pickle.dump(cells,open('dev_cells.pkl','wb'))
t=time.time(); sess=wirth.Session(cells[0]); print('session',time.time()-t)
for k,v in sess.res.items(): print(k, v['step'], v['valid'].sum())
print('cr',sess.cr['nb'],sess.cr['val_c'].sum(),sess.cr['val_r'].sum(),(sess.cr['val_c']&sess.cr['val_r']).sum())
t=time.time(); out,s=wirth.analyse_cell(cells[0],sess,0); print('cell',time.time()-t)
for k,v in out.items(): print(k,v)
print('maxrss MB',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e3)
EOF
python dev1.py 2>&1 | tail -120
```

```
ic|('toreward', 'direction') 0.8793500067324166
sp|('toreward', 'direction') 0.7904954411593872
nbins|('toreward', 'direction') 151
ic|('toreward', 'state') 1.4412636132122727
sp|('toreward', 'state') 0.8054402193266738
nbins|('toreward', 'state') 199
ic|center 1.7793491776483492
sp|center 0.7926702073719771
nbins|center 151
ic|return 0.9444380308135629
sp|return 0.7206292824796474
nbins|return 153
corr 0.2780963011283511
n_common 150
ssi 0.7200607608904579
ssi_bins 20
icn|('full', 'position')|permute 0.0030485758213943948
icp|('full', 'position')|permute 0.904
spn|('full', 'position')|permute 0.013176441205797418
spp|('full', 'position')|permute 0.636
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python dev1.py 2>&1 | head -30
```

```
load 10.27935791015625
session 2.7726869583129883
('full', 'position') 0.9 199
('full', 'direction') 331 200
('full', 'state') 0.12 201
('toreward', 'position') 0.5 134
('toreward', 'direction') 254 151
('toreward', 'state') 0.05 199
cr 254 151 153 150
cell 2.075460910797119
name ke20130221_HPC_e4_c4_seg.mat
monkey ke
session ke20130221
n_spikes_window 294
n_spikes_file 407
spike_src file.elec
ic|('full', 'position') 0.8609690312492603
sp|('full', 'position') 0.790075371539391
nbins|('full', 'position') 199
ic|('full', 'direction') 0.6795033687680216
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> entries/wirth-2017/wirth.py <<'EOF'


# ---------------------------------------------------------------- landmark analyses

def landmark_tables(c, s, sess):
    """Per lap rates for the landmark ANOVAs.

    Two-way (Methods, ANOVA for landmark identity and relative distance): entry-path frames
    (tags 10x) of successful trials, cut by the curvilinear abscissa (0 centre, 1 arm end)
    into RD1 (1 to 0.75, 16 to 12 m) ... RD4 (0.25 to 0); identity is the entry path x, whose
    view faces one landmark. One-way at the centre (claims file, readings): (a) centre frames
    whose camera orientation lies within the 3.6 degree bin of the heading of entry path x
    (the landmark straight ahead on arrival), one rate per trial; (b) the 36 degree alignment
    after arriving from path x (tags 2xy), one rate per visit."""
    import pandas as pd
    t60 = c["t60"]
    trial, ok = sess.tables["full"]
    tag = sess.tag
    ab = t60[:, 4]
    rows = []
    ent = sess.entry & np.isfinite(ab)
    seg = np.clip(np.floor((1 - ab) * 4).astype(int), 0, 3)
    key = pd.DataFrame({"trial": trial[ent], "lm": (tag[ent] % 100).astype(int),
                        "rd": seg[ent], "n": s[ent]})
    two = key.groupby(["trial", "lm", "rd"]).agg(spk=("n", "sum"), fr=("n", "size")).reset_index()
    two["rate"] = two.spk / (two.fr * DT)
    # one-way (b): 2xy visits
    m2 = ok & (tag >= 200) & (tag < 300)
    df2 = pd.DataFrame({"trial": trial[m2], "lm": ((tag[m2] // 10) % 10).astype(int), "n": s[m2]})
    oneb = df2.groupby(["trial", "lm"]).agg(spk=("n", "sum"), fr=("n", "size")).reset_index()
    oneb["rate"] = oneb.spk / (oneb.fr * DT)
    # one-way (a): heading of each entry path, then centre frames facing it
    th = np.mod(t60[:, 3], 360)
    heads = {}
    for x in np.unique(tag[sess.entry] % 100).astype(int):
        mm = sess.entry & (tag % 100 == x)
        a = np.deg2rad(th[mm])
        heads[x] = np.rad2deg(np.arctan2(np.sin(a).mean(), np.cos(a).mean())) % 360
    reca = []
    for x, h in heads.items():
        d = np.abs((th - h + 180) % 360 - 180)
        mm = sess.center & (d <= SSI_BIN_DEG / 2)
        reca.append(pd.DataFrame({"trial": trial[mm], "lm": x, "n": s[mm]}))
    onea = pd.concat(reca).groupby(["trial", "lm"]).agg(spk=("n", "sum"), fr=("n", "size")).reset_index()
    onea["rate"] = onea.spk / (onea.fr * DT)
    return two, onea, oneb, heads


def anova_two(two):
    import warnings
    import statsmodels.api as sm
    from statsmodels.formula.api import ols
    if two.lm.nunique() < 2 or two.rd.nunique() < 2 or two.rate.var() == 0:
        return None
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        fit = ols("rate ~ C(lm) * C(rd)", data=two).fit()
        tab = sm.stats.anova_lm(fit, typ=2)
    return {"p_lm": tab.loc["C(lm)", "PR(>F)"], "p_rd": tab.loc["C(rd)", "PR(>F)"],
            "p_int": tab.loc["C(lm):C(rd)", "PR(>F)"], "F_int": tab.loc["C(lm):C(rd)", "F"],
            "df_int": tab.loc["C(lm):C(rd)", "df"], "df_res": tab.loc["Residual", "df"],
            "n_lm": int(two.lm.nunique())}


def anova_one(df):
    from scipy.stats import f_oneway
    groups = [g.rate.values for _, g in df.groupby("lm") if len(g) >= 2]
    if len(groups) < 2 or np.var(np.concatenate(groups)) == 0:
        return np.nan, len(groups)
    return float(f_oneway(*groups).pvalue), len(groups)


# ---------------------------------------------------------------- eye

EYE_SAT = 4990.0   # samples at the +-4999.85 rail are saturated (shown in the notebook)


def eye_mean(c, t0, t1, which="mean"):
    """Mean horizontal eye signal in [t0, t1), raw file units; saturated samples dropped."""
    if c["eye"] is None:
        return np.nan
    et = c["eye_t"]
    i0, i1 = np.searchsorted(et, t0), np.searchsorted(et, t1)
    if i1 <= i0:
        return np.nan
    if which == "mean":
        v = np.vstack([c["eye"]["l_hor"][i0:i1], c["eye"]["r_hor"][i0:i1]])
        v = np.where(np.abs(v) < EYE_SAT, v, np.nan)
        with np.errstate(all="ignore"):
            v = np.nanmean(v, 0)
    else:
        v = c["eye"][f"{which}_hor"][i0:i1]
        v = np.where(np.abs(v) < EYE_SAT, v, np.nan)
    v = v[np.isfinite(v)]
    return float(v.mean()) if len(v) else np.nan


def return_turns(c):
    """Per trial, the passive return after it (tags 5xy before the next trial start): the sign
    of the total change of camera orientation (negative = to the right, as for code 1) and
    its start and end times."""
    t60 = c["t60"]
    tr = trials(c)
    ts = tr["t_start"]
    out = []
    dth = np.r_[0, (np.diff(t60[:, 3]) + 180) % 360 - 180]
    for i in range(len(ts) - 1):
        a, b = tr["t_end"][i], ts[i + 1]
        if not (np.isfinite(a) and np.isfinite(b)):
            continue
        m = (t60[:, 0] >= a) & (t60[:, 0] < b) & (t60[:, 10] >= 500) & (t60[:, 10] < 600)
        if m.sum() < 5:
            continue
        idx = np.nonzero(m)[0]
        tot = dth[idx[1:]].sum()
        out.append({"trial": i, "correct": bool(tr["correct"][i]), "t0": t60[idx[0], 0],
                    "t1": t60[idx[-1], 0], "dtheta": tot})
    return out
EOF
date -u
```

```
Fri Nov 13 12:17:12 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF' 2>&1 | grep -v Warn
import pickle, numpy as np, sys
sys.path.insert(0,'entries/wirth-2017')
import wirth
S=pickle.load(open('survey_hc-12.pkl','rb'))
o12=o23=0; n=0; rows=[]
for k,r in S.items():
    na=r.get('newallo')
    if not isinstance(na,dict): continue
    lc=na['learning_curves'].astype(float)
    if lc.ndim!=2 or lc.shape[1]!=3: print(k,lc.shape); continue
    n+=1
    o12+=np.all(lc[:,1]<=lc[:,0]+1e-9); o23+=np.all(lc[:,0]<=lc[:,2]+1e-9)
    crit=wirth.lower_bound_criterion(lc[:,1])
    cm=na['codematrix'].astype(float)
    corr=(cm[:,1:]==11).any(1)
    rows.append((k.split('/')[-1][:22], lc.shape[0], cm.shape[0], crit, float(na['learningtrial'].ravel()[0]), round(corr.mean(),2)))
print(n,o12,o23)
for r in rows[::4]: print(r)
EOF
```

```
187 187 187
('ke20130221_HPC_e4_c4_s', 81, 81, 8.0, 8.0, np.float64(0.8))
('ke20130306_HPC_e5_c2_s', 81, 81, 3.0, 3.0, np.float64(0.84))
('ke20130314_hpc_e9_c1_s', 81, 81, 3.0, 3.0, np.float64(0.9))
('ke20130315_HPC_e2_c1_s', 109, 109, 9.0, 9.0, np.float64(0.76))
('ke20130402_HPC_e5_c2_s', 80, 80, 6.0, 6.0, np.float64(0.88))
('ke20130404_hpc_e11_c1_', 161, 161, 76.0, 76.0, np.float64(0.48))
('ke20130411_hpc_e8_c1_s', 115, 115, 61.0, 61.0, np.float64(0.56))
('ke20130716_HPC_e4_c1_s', 76, 76, 24.0, 24.0, np.float64(0.36))
('ke20130718_hpc_e11_c1_', 101, 101, 40.0, 40.0, np.float64(0.57))
('ke20130722_hpc_e10_c2_', 95, 95, 15.0, 15.0, np.float64(0.87))
('ke20130722_hpc_e6_c1_s', 95, 95, 15.0, 15.0, np.float64(0.87))
('ke20130726_HPC_e10_c2_', 113, 113, 7.0, 7.0, np.float64(0.69))
('ke20131023_e1_HPC_c2_s', 82, 82, 3.0, 3.0, np.float64(0.8))
('ke20131122_HPC_e1_c2_s', 81, 81, 7.0, 7.0, np.float64(0.93))
('ke20131128_HPC_e1_c1_s', 82, 82, 10.0, 10.0, np.float64(0.89))
('ke20140226_HPC_c3_seg.', 80, 80, 12.0, 12.0, np.float64(0.85))
('ke20140304_HPC_c1_seg.', 56, 56, nan, -2.0, np.float64(0.32))
('ke20140305_hpc_c1_seg.', 39, 39, 22.0, 22.0, np.float64(0.49))
('ke20140306_HPC_c3_seg.', 80, 80, 5.0, 5.0, np.float64(0.86))
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF' 2>&1 | grep -v Warn
import pickle, numpy as np, sys, time
sys.path.insert(0,'entries/wirth-2017')
import wirth
cells=pickle.load(open('dev_cells.pkl','rb'))
c=cells[3]; sess=wirth.Session(c); s=wirth.spike_counts(c)
t=time.time()
two,onea,oneb,heads=wirth.landmark_tables(c,s,sess)
print(heads); print(two.groupby(['lm','rd']).size().unstack())
print(wirth.anova_two(two), wirth.anova_one(onea), wirth.anova_one(oneb), time.time()-t)
print(onea.groupby('lm').size(), oneb.groupby('lm').size())
tr=wirth.trials(c); print(np.unique(tr['start_arm'][tr['correct']],return_counts=True), np.unique(tr['chosen_arm'],return_counts=True))
# turn direction check
t60=c['t60']
for code in (1,2):
    d=[]
    for tt,ty in zip(tr['turn_t'],tr['turns']):
        for a,b in zip(tt,ty):
            if b==code:
                i0=np.searchsorted(t60[:,0],a); i1=np.searchsorted(t60[:,0],a+0.6)
                d.append(((t60[i1,3]-t60[i0,3]+180)%360)-180)
    print('code',code,np.median(d),len(d))
print(np.unique(sess.types,return_counts=True))
rt=wirth.return_turns(c); print(len(rt), np.median([abs(r['dtheta']) for r in rt]))
print(np.unique(np.sign([r['dtheta'] for r in rt]),return_counts=True))
print(wirth.eye_mean(c, tr['t_center'][0]-0.5, tr['t_center'][0]))
print([len(x) for x in tr['turns']][:20])
EOF
```

```
seg = np.clip(np.floor((1 - ab) * 4).astype(int), 0, 3)
{np.int64(1): np.float64(90.0), np.int64(2): np.float64(162.0), np.int64(3): np.float64(233.99999999999997), np.int64(5): np.float64(18.0)}
rd   0   1   2   3
lm                
1   17  17  17  17
2   18  18  18  18
3   16  16  16  16
5   17  17  17  17
{'p_lm': np.float64(0.41648717082758846), 'p_rd': np.float64(0.766563858804802), 'p_int': np.float64(0.400048260166895), 'F_int': np.float64(1.0508289777052449), 'df_int': np.float64(9.0), 'df_res': np.float64(256.0), 'n_lm': 4} (0.4605679075419715, 4) (0.3113128623252961, 4) 3.6359245777130127
lm
1    34
2    34
3    16
5    17
dtype: int64 lm
1    17
2    18
3    16
5    17
dtype: int64
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> entries/wirth-2017/wirth.py <<'EOF'


# ---------------------------------------------------------------- one pass over a data set

EYE_LAGS = np.round(np.arange(-1.0, 1.51, 0.1), 2)   # clock check, s from the turn code


def behaviour(c):
    """Session behaviour: trial table, learning curves, eye before turns and on returns."""
    tr = trials(c)
    turns = []
    for i, (ty, tt) in enumerate(zip(tr["turns"], tr["turn_t"])):
        for j, (code, t) in enumerate(zip(ty, tt)):
            row = {"trial": i, "k": j, "code": code, "correct": bool(tr["correct"][i])}
            for w in (0.5, 0.3):
                for which in ("mean", "l", "r"):
                    row[f"eye{int(w * 1000)}_{which}"] = eye_mean(c, t - w, t, which)
            for lag in EYE_LAGS:
                row[f"lag{lag}"] = eye_mean(c, t + lag, t + lag + 0.1)
            i0 = np.searchsorted(c["t60"][:, 0], t)
            i1 = np.searchsorted(c["t60"][:, 0], t + 0.6)
            if i1 < len(c["t60"]):
                row["dtheta_0_600ms"] = ((c["t60"][i1, 3] - c["t60"][i0, 3] + 180) % 360) - 180
            turns.append(row)
    rets = return_turns(c)
    for r in rets:
        for which in ("mean", "l", "r"):
            r[f"eye_{which}"] = eye_mean(c, r["t0"], r["t1"], which)
    eye_sat = None
    if c["eye"] is not None:
        v = np.concatenate([c["eye"]["l_hor"], c["eye"]["r_hor"]])
        eye_sat = float(np.mean(np.abs(v) >= EYE_SAT))
        eye_rng = (float(np.percentile(v, 1)), float(np.percentile(v, 99)))
    else:
        eye_rng = None
    return {"monkey": c["monkey"], "session": c["session"], "n_trials": len(c["cm"]),
            "start_arm": tr["start_arm"], "chosen_arm": tr["chosen_arm"],
            "correct": tr["correct"], "lc": c["lc"], "learningtrial": c["learningtrial"],
            "turns": turns, "returns": rets, "eye_saturated": eye_sat, "eye_range": eye_rng,
            "has_eye": c["eye"] is not None}


def file_meta(name, d, c):
    fl = d["file"][0, 0]
    row = {"file": name, "monkey": name[:2], "session": name.split("_")[0],
           "fields": ",".join(fl.dtype.names), "has_newallo": c is not None}
    if c is not None:
        t60 = c["t60"]
        row.update({"spike_src": c["spike_src"], "n_spikes_file": len(c["spikes"]),
                    "n_trials": len(c["cm"]), "n_correct": int(trials(c)["correct"].sum()),
                    "t_start": c["window"][0], "t_end": c["window"][1],
                    "frames": len(t60), "frame_dt_ms": float(np.median(np.diff(t60[:, 0])) * 1000),
                    "x_min": float(np.nanmin(t60[:, 1])), "x_max": float(np.nanmax(t60[:, 1])),
                    "y_min": float(np.nanmin(t60[:, 2])), "y_max": float(np.nanmax(t60[:, 2])),
                    "theta_min": float(np.nanmin(t60[:, 3])), "theta_max": float(np.nanmax(t60[:, 3])),
                    "abscissa_min": float(np.nanmin(t60[:, 4])), "abscissa_max": float(np.nanmax(t60[:, 4])),
                    "has_eye": c["eye"] is not None,
                    "eye_dt_ms": float(np.median(np.diff(c["eye_t"])) * 1000) if c["eye"] is not None else np.nan,
                    "spikes_in_window": int(np.sum((c["spikes"] >= c["window"][0]) & (c["spikes"] <= c["window"][1]))),
                    "spikes_sorted": bool(np.all(np.diff(np.asarray(fl["elec"] if "elec" in fl.dtype.names else c["spikes"], float).ravel()) >= 0)),
                    "reclocation": None if c["reclocation"] is None else tuple(np.round(c["reclocation"], 2)),
                    "learningtrial": c["learningtrial"],
                    "lc_order_ok": None if c["lc"] is None else bool(np.all(c["lc"][:, 1] <= c["lc"][:, 0] + 1e-9) and np.all(c["lc"][:, 0] <= c["lc"][:, 2] + 1e-9)),
                    "first_spikes": tuple(np.round(c["spikes"][:5], 4))})
    return row


def collect(dataset="hc-12", limit=None, log=print):
    """Stream a data set once and compute every per-cell and per-session quantity."""
    import time
    import zlib
    metas, cells, beh, lmk = [], [], {}, []
    sess_key, sess = None, None
    t0 = time.time()
    for i, (name, d) in enumerate(stream_members(dataset)):
        c = reduce_file(name, d)
        metas.append(file_meta(name, d, c))
        del d
        if c is None:
            continue
        key = (c["session"], len(c["cm"]), round(c["window"][0], 3))
        if key != sess_key:
            sess_key, sess = key, Session(c)
        out, s = analyse_cell(c, sess, zlib.crc32(name.encode()))
        two, onea, oneb, heads = landmark_tables(c, s, sess)
        a2 = anova_two(two) or {}
        out.update({f"lm2_{k}": v for k, v in a2.items()})
        out["lm1a_p"], out["lm1a_groups"] = anova_one(onea)
        out["lm1b_p"], out["lm1b_groups"] = anova_one(oneb)
        out["n_laps"] = int(two.trial.nunique())
        out["n_trials"] = len(c["cm"])
        cells.append(out)
        b = beh.get(c["session"])
        if b is None or b["n_trials"] < len(c["cm"]):
            beh[c["session"]] = behaviour(c)
        if log and (i % 20 == 0):
            log(f"{i + 1} files, {time.time() - t0:.0f} s")
        if limit and i + 1 >= limit:
            break
    return metas, cells, beh


def fingerprint(dataset, maze="newallo", log=print):
    """Per file of a data set: spike count and first spike times, trial count and first trial
    start in `maze`, for finding recordings deposited twice."""
    rows = []
    for name, d in stream_members(dataset):
        c = reduce_file(name, d, maze)
        fl = d["file"][0, 0]
        row = {"file": name, "session": name.split("_")[0], "fields": ",".join(fl.dtype.names),
               "has_maze": c is not None}
        if c is not None:
            row.update({"n_spikes": len(c["spikes"]), "spikes_head": tuple(np.round(c["spikes"][:20], 3)),
                        "n_trials": len(c["cm"]), "t_first": round(float(c["window"][0]), 3),
                        "codes_head": tuple(c["cm"][:10, 1].astype(int))})
        rows.append(row)
    return rows
EOF
cd $TMPDIR && . dev/bin/activate && cat > dev2.py <<'EOF'
import sys, time, pickle, resource
sys.path.insert(0,'entries/wirth-2017')
import wirth
t=time.time()
res=wirth.collect('hc-12', limit=int(sys.argv[1]) if len(sys.argv)>1 else None)
print('time',time.time()-t, 'rss MB',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e3)
pickle.dump(res,open('dev_res%s.pkl'%(sys.argv[1] if len(sys.argv)>1 else 'all'),'wb'))
EOF
python dev2.py 8 2>&1 | grep -v Warn | tail
```

```
seg = np.clip(np.floor((1 - ab) * 4).astype(int), 0, 3)
  seg = np.clip(np.floor((1 - ab) * 4).astype(int), 0, 3)
  v = np.nanmean(v, 0)
  seg = np.clip(np.floor((1 - ab) * 4).astype(int), 0, 3)
  seg = np.clip(np.floor((1 - ab) * 4).astype(int), 0, 3)
  seg = np.clip(np.floor((1 - ab) * 4).astype(int), 0, 3)
  seg = np.clip(np.floor((1 - ab) * 4).astype(int), 0, 3)
  seg = np.clip(np.floor((1 - ab) * 4).astype(int), 0, 3)
1 files, 8 s
time 41.42164754867554 rss MB 685.96
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/wirth-2017 && python - <<'EOF'
s=open('wirth.py').read()
s=s.replace("    seg = np.clip(np.floor((1 - ab) * 4).astype(int), 0, 3)","    seg = np.clip(np.floor((1 - np.nan_to_num(ab)) * 4).astype(int), 0, 3)")
s=s.replace("""        with np.errstate(all="ignore"):
            v = np.nanmean(v, 0)""","""        n = np.isfinite(v).sum(0)
        v = np.where(n > 0, np.nansum(v, 0) / np.maximum(n, 1), np.nan)""")
open('wirth.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && python dev2.py 2>&1 | grep -v Warn | tail -5; date -u
```

```
c = reduce_file(name, d)
  File "entries/wirth-2017/wirth.py", line 140, in reduce_file
    v = np.asarray(s[c], float).ravel()
        ~~~~~~~~~~^^^^^^^^^^^^^
TypeError: Cannot cast array data from dtype([('title', 'O'), ('comment', 'O'), ('interval', 'O'), ('scale', 'O'), ('offset', 'O'), ('units', 'O'), ('start', 'O'), ('length', 'O'), ('values', 'O')]) to dtype('float64') according to the rule 'unsafe'
Fri Nov 13 12:20:22 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/wirth-2017 && python - <<'EOF'
s=open('wirth.py').read()
old="""            for c in ("hor", "ver"):
                v = np.asarray(s[c], float).ravel()"""
new="""            for c in ("hor", "ver"):
                v = s[c]
                if v.dtype.names:  # a Spike2 channel struct: take its values, keep its units
                    v = v[0, 0]
                    eye_units.add(str(np.asarray(v["units"]).ravel()[0]) if v["units"].size else "")
                    v = v["values"]
                v = np.asarray(v, float).ravel()"""
assert old in s
s=s.replace(old,new)
s=s.replace("""        eyes = {}
        for e in""","""        eyes = {}
        eye_units = set()
        for e in""")
s=s.replace("""        out["eye"] = {k: v[:n] for k, v in eyes.items()}""","""        out["eye"] = {k: v[:n] for k, v in eyes.items()}
        out["eye_units"] = ",".join(sorted(eye_units)) or None""")
s=s.replace("""        out["eye_t"] = None
        out["eye"] = None""","""        out["eye_t"] = None
        out["eye"] = None
        out["eye_units"] = None""")
s=s.replace("""                    "has_eye": c["eye"] is not None,""","""                    "has_eye": c["eye"] is not None, "eye_units": c["eye_units"],""")
open('wirth.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && python dev2.py 2>&1 | grep -v Warn | tail -5; date -u
```

```
101 files, 626 s
141 files, 932 s
161 files, 1010 s
181 files, 1080 s
time 1114.7045602798462 rss MB 918.208
Fri Nov 13 12:39:05 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF' 2>&1 | grep -v Warn
import pickle, numpy as np, pandas as pd
pd.set_option('display.width',250); pd.set_option('display.max_columns',40)
metas,cells,beh=pickle.load(open('dev_resall.pkl','rb'))
M=pd.DataFrame(metas); C=pd.DataFrame(cells)
print(M.groupby('monkey').agg(files=('file','size'),newallo=('has_newallo','sum'),sessions=('session','nunique')))
print(M.spike_src.value_counts(), M.eye_units.value_counts(dropna=False), M.has_eye.value_counts())
print(M.lc_order_ok.value_counts(), M.spikes_sorted.value_counts())
print('frame dt', M.frame_dt_ms.describe().round(2).to_dict()); print('eye dt',M.eye_dt_ms.describe().round(2).to_dict())
print(M[['x_min','x_max','y_min','y_max','theta_min','theta_max','abscissa_min','abscissa_max']].describe().round(2))
print('spikes window >100', (C.n_spikes_window>100).sum(), 'of', len(C), C.groupby('monkey').apply(lambda d:(d.n_spikes_window>100).sum()))
print(C.n_spikes_window.describe())
# duplicates within hc-12
dup=M[M.has_newallo].groupby(['first_spikes','n_spikes_file']).file.apply(list)
print('dup groups', [v for v in dup if len(v)>1])
EOF
```

```
diff_b_a = b - a
  sqr = (avg - values) ** 2
        files  newallo  sessions
monkey                          
ke         99       99        41
sn         90       88        26
spike_src
file.elec       175
newallo.elec     12
Name: count, dtype: int64 eye_units
NaN    189
Name: count, dtype: int64 has_eye
True     179
False      8
Name: count, dtype: int64
lc_order_ok
True    187
Name: count, dtype: int64 spikes_sorted
True    187
Name: count, dtype: int64
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF' 2>&1 | grep -v Warn
import pickle, numpy as np, pandas as pd
from scipy import stats
pd.set_option('display.width',250)
metas,cells,beh=pickle.load(open('dev_resall.pkl','rb'))
C=pd.DataFrame(cells); C=C[C.n_spikes_window>100]
for r in ['full','toreward']:
  for sr in ['permute','shift']:
    sig={k:(C[f"icp|('{r}', '{k}')|{sr}"]<0.01) for k in ['position','direction','state']}
    anyr=sig['position']|sig['direction']|sig['state']
    print(r,sr,{k:int(v.sum()) for k,v in sig.items()}, 'any',int(anyr.sum()), 'multi', int((sum(v.astype(int) for v in sig.values())>=2).sum()),
     'pos001', int((C[f"icp|('{r}', 'position')|{sr}"]<0.05).sum()))
# clock shift
sh=[c for c in C.columns if c.startswith('shift_ic')]
print(C[sh].median().round(3))
print('n bins', C[[c for c in C.columns if c.startswith('nbins')]].median())
EOF
```

```
full permute {'position': 46, 'direction': 40, 'state': 57} any 59 multi 46 pos001 65
full shift {'position': 27, 'direction': 24, 'state': 33} any 39 multi 28 pos001 38
toreward permute {'position': 33, 'direction': 40, 'state': 42} any 55 multi 39 pos001 55
toreward shift {'position': 20, 'direction': 21, 'state': 24} any 32 multi 23 pos001 34
shift_ic|-5.0     0.319
shift_ic|-2.0     0.324
shift_ic|-1.0     0.339
shift_ic|-0.5     0.340
shift_ic|-0.25    0.357
shift_ic|0.0      0.343
shift_ic|0.25     0.348
shift_ic|0.5      0.335
shift_ic|1.0      0.344
shift_ic|2.0      0.343
shift_ic|5.0      0.318
dtype: float64
n bins nbins|('full', 'position')         198.0
nbins|('full', 'direction')        200.0
nbins|('full', 'state')            200.0
nbins|('toreward', 'position')     138.0
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF' 2>&1 | grep -v Warn
import pickle, numpy as np, pandas as pd
metas,cells,beh=pickle.load(open('dev_resall.pkl','rb'))
C=pd.DataFrame(cells); C=C[C.n_spikes_window>100]
sh=[c for c in C.columns if c.startswith('shift_ic')]
r=C["icp|('full', 'state')|permute"]<0.01
X=C.loc[r,sh].values; X=X/X[:,[5]]
print(np.median(X,0).round(3))
print(C.groupby('monkey').apply(lambda d: (d["icp|('full', 'state')|permute"]<0.01).mean()))
# icn one-sided variant
for k in ['position','direction','state']:
    print(k, (C[f"icp|('full', '{k}')|permute"]<0.02).sum())
EOF
```

```
[0.802 0.949 0.959 1.021 1.    1.    0.984 0.982 0.956 0.899 0.768]
monkey
ke    0.224490
sn    0.397727
dtype: float64
position 58
direction 46
state 62
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF' 2>&1 | grep -v Warn
import pickle, numpy as np, pandas as pd, sys
sys.path.insert(0,'entries/wirth-2017')
import wirth
from scipy import stats
metas,cells,beh=pickle.load(open('dev_resall.pkl','rb'))
rows=[]
for s,b in beh.items():
    sa=b['start_arm']; n=len(sa)
    first=set(sa[:10][np.isfinite(sa[:10])].astype(int)); allarms=set(sa[np.isfinite(sa)].astype(int))
    lc=b['lc']; crit=wirth.lower_bound_criterion(lc[:,1])
    up=np.nonzero(lc[:,2]>=0.9)[0]; up=[u for u in up if np.isfinite(crit) and u+1>=crit]
    t90=(up[0]+1-crit) if up else np.nan
    intro=next((i for i in range(n) if np.isfinite(sa[i]) and int(sa[i]) not in first),None)
    rows.append(dict(session=s,monkey=b['monkey'],n=n,first=sorted(first),arms=sorted(allarms),crit=crit,t90=t90,intro=intro,
                     pc=b['correct'].mean(), rew=np.unique(b['chosen_arm'][b['correct']])))
D=pd.DataFrame(rows); pd.set_option('display.width',250); pd.set_option('display.max_rows',100)
print(D.to_string())
EOF
```

```
session monkey    n            first             arms  crit   t90  intro        pc         rew
0    ke20130221     ke   81     [1, 2, 3, 5]     [1, 2, 3, 5]   8.0   3.0    NaN  0.802469       [4.0]
1    ke20130301     ke   83     [1, 2, 3, 5]     [1, 2, 3, 5]  13.0  19.0    NaN  0.674699       [4.0]
2    ke20130306     ke   81        [1, 2, 3]     [1, 2, 3, 5]   3.0   3.0   13.0  0.839506       [4.0]
3    ke20130314     ke   81     [1, 2, 3, 5]     [1, 2, 3, 5]   3.0   7.0    NaN  0.901235       [4.0]
4    ke20130315     ke  109     [1, 2, 3, 4]     [1, 2, 3, 4]   9.0  16.0    NaN  0.761468       [5.0]
5    ke20130327     ke   84        [2, 3, 5]     [1, 2, 3, 5]   3.0   1.0   11.0  0.964286       [4.0]
6    ke20130402     ke   80        [2, 3, 5]     [1, 2, 3, 5]   6.0   2.0   10.0  0.875000       [4.0]
7    ke20130404     ke  161     [1, 2, 3, 4]     [1, 2, 3, 4]  76.0  27.0    NaN  0.478261       [5.0]
8    ke20130405     ke   80     [1, 3, 4, 5]     [1, 3, 4, 5]  15.0   2.0    NaN  0.812500       [2.0]
9    ke20130410     ke   86     [1, 2, 3, 5]     [1, 2, 3, 5]  32.0   3.0    NaN  0.697674       [4.0]
10   ke20130411     ke  115        [1, 2, 4]     [1, 2, 4, 5]  61.0   2.0   10.0  0.556522       [3.0]
11  ke20130412a     ke   80     [1, 2, 3, 5]     [1, 2, 3, 5]  14.0   2.0    NaN  0.787500       [4.0]
12   ke20130716     ke   76     [1, 2, 3, 5]     [1, 2, 3, 5]  24.0   8.0    NaN  0.355263       [4.0]
13   ke20130717     ke  112     [1, 3, 4, 5]     [1, 3, 4, 5]  31.0  34.0    NaN  0.571429       [2.0]
14   ke20130718     ke  101     [2, 3, 4, 5]     [2, 3, 4, 5]  40.0   2.0    NaN  0.574257       [1.0]
15   ke20130722     ke   95     [1, 2, 3, 5]     [1, 2, 3, 5]  15.0   0.0    NaN  0.873684       [4.0]
16   ke20130726     ke  113     [1, 2, 3, 5]     [1, 2, 3, 5]   7.0   2.0    NaN  0.690265       [4.0]
17   ke20131023     ke   82     [1, 2, 3, 5]     [1, 2, 3, 5]   3.0   3.0    NaN  0.804878       [4.0]
18   ke20131024     ke   83     [1, 2, 3, 4]     [1
[... 48 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF' 2>&1 | grep -v Warn
import pickle, numpy as np
metas,cells,beh=pickle.load(open('dev_resall.pkl','rb'))
for s,b in beh.items():
    sa=b['start_arm']; 
    seq=''.join(str(int(x)) if np.isfinite(x) else '.' for x in sa)
    L=0; st=set()
    for x in sa:
        st=st|{x}
        if len(st)>2: break
        L+=1
    print(s, len(sa), 'L2=',L, seq[:70])
EOF
```

```
ke20130221 81 L2= 2 5213252121213322322521533355355555121225315311531135532521511253115331
ke20130301 83 L2= 2 2535155133323222315523532233113313322122133511155552221133132311522535
ke20130306 81 L2= 4 3133232213321553112112355233351223115133555132532525551252525333552332
ke20130314 81 L2= 2 5213535125511332511122521331112522552353252352121331115123122123322531
ke20130315 109 L2= 2 4321313423311113331243444223311244114342214211221223234223243412134321
ke20130327 84 L2= 5 2555533352215531213331231212332522255335311515251312325551113235235253
ke20130402 80 L2= 3 5223352223112331325533552152235123111521231511513251521523511351153253
ke20130404 161 L2= 3 2421314144433421211434242321124242214331332412424421131124243331443111
ke20130405 80 L2= 4 1444553451133433345533331434444115311511533334154511454311431153151334
ke20130410 86 L2= 3 1135332533325521533332115215322313122322212122535351221525335533232552
ke20130411 115 L2= 3 4421214141544425225524555221151512111252425214214554212444552541412515
ke20130412a 80 L2= 6 1133315225255251353222523125253231533531322525215152555333133211111332
ke20130716 76 L2= 4 3535235231225325153333112135232231215253133251513333315131212253213551
ke20130717 112 L2= 3 3531433511133335551515153115345544453334313434555413134544455354443111
ke20130718 101 L2= 7 5544445332322445533425252422355524243255333434352353544245254432423235
ke20130722 95 L2= 5 5525213221353522225111351332215511233123131135231113552111315355512231
ke20130726 113 L2= 2 1353551222222153225332122115232351231131533333131315351213311531551215
ke20131023 82 L2= 4 1115353312211225552555515135555353153211222332331331533123153233123251
ke20131024 83 L2= 2 3243234221442231211311123431221324431213344441314444241322232131222443
ke20131121 86 L2= 2 2434324142233214341141121232432121114313144242443221121433423321134133
[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > devb.py <<'EOF'
import pickle, numpy as np, pandas as pd, sys
sys.path.insert(0,'entries/wirth-2017')
import wirth
from scipy import stats
metas,cells,beh=pickle.load(open('dev_resall.pkl','rb'))
rows=[]
for s,b in beh.items():
    sa=b['start_arm']; n=len(sa)
    first=set(sa[:10][np.isfinite(sa[:10])].astype(int))
    probe=len(first)<=2
    intro=next((i for i in range(n) if np.isfinite(sa[i]) and int(sa[i]) not in first),None) if probe else None
    lc=b['lc']; crit=wirth.lower_bound_criterion(lc[:,1])
    up=np.nonzero(lc[:,2]>=0.9)[0]; up=[u for u in up if np.isfinite(crit) and u+1>=crit]
    t90=(up[0]+1-crit) if up else np.nan
    cor=b['correct']
    rows.append(dict(session=s,monkey=b['monkey'],n=n,probe=probe and intro is not None,intro=intro,crit=crit,t90=t90,
       pc_first5=cor[:5].mean(), pc_after5=cor[intro:intro+5].mean() if intro is not None else np.nan))
D=pd.DataFrame(rows)
for rd,sub in [('all',D),('nonprobe',D[~D.probe])]:
    g=sub.groupby('monkey').crit.agg(['mean','sem','count',lambda x:x.isna().sum()])
    print(rd); print(g)
    x=sub.t90; print('t90<10 frac (sessions reaching)', (x<10).sum(), x.notna().sum(), (x<10).sum()/x.notna().sum(), 'over all', (x<10).sum()/len(x))
P=D[D.probe]; print(P[['session','intro','pc_first5','pc_after5']])
print(P.groupby('monkey')[['pc_first5','pc_after5']].mean())
print(stats.wilcoxon(P.pc_after5,P.pc_first5))
EOF
python devb.py 2>&1 | grep -v Warn
```

```
all
             mean       sem  count  <lambda_0>
monkey                                        
ke      16.526316  2.689936     38           3
sn      12.260870  3.275986     23           2
t90<10 frac (sessions reaching) 53 59 0.8983050847457628 over all 0.803030303030303
nonprobe
             mean       sem  count  <lambda_0>
monkey                                        
ke      15.821429  3.437674     28           1
sn      12.260870  3.275986     23           2
t90<10 frac (sessions reaching) 44 49 0.8979591836734694 over all 0.8148148148148148
       session  intro  pc_first5  pc_after5
24  ke20140207   24.0        0.2        0.2
25  ke20140211   12.0        0.0        0.8
26  ke20140226   11.0        0.2        0.6
28  ke20140228   30.0        0.0        1.0
29  ke20140304   16.0        0.4        0.0
30  ke20140305   28.0        0.4        1.0
31  ke20140306   10.0        0.6        0.8
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > devg.py <<'EOF'
import pickle, numpy as np, pandas as pd, sys
from scipy import stats
metas,cells,beh=pickle.load(open('dev_resall.pkl','rb'))
T=[];R=[]
for s,b in beh.items():
    for t in b['turns']: T.append(dict(session=s,monkey=b['monkey'],**t))
    for r in b['returns']: R.append(dict(session=s,monkey=b['monkey'],**r))
T=pd.DataFrame(T); R=pd.DataFrame(R)
print('dtheta by code', T.groupby('code').dtheta_0_600ms.median())
print('return dtheta sign', np.sign(R.dtheta).value_counts())
lags=[c for c in T.columns if c.startswith('lag')]
for m in ['ke','sn']:
    x=T[(T.monkey==m)&T.correct]
    print(m, 'right-left by lag', (x[x.code==1][lags].median()-x[x.code==2][lags].median()).round(0).values)
for w in ['eye500','eye300']:
  for which in ['mean','l','r']:
    col=f'{w}_{which}'
    for m in ['ke','sn',None]:
        x=T[T.correct] if m is None else T[(T.monkey==m)&T.correct]
        x=x[x[col].notna()]
        # session-centred
        xc=x[col]-x.groupby('session')[col].transform('median')
        a=x[x.code==1][col]; b=x[x.code==2][col]
        p=stats.mannwhitneyu(a,b).pvalue; pc=stats.mannwhitneyu(xc[x.code==1],xc[x.code==2]).pvalue
        print(col,m,len(a),len(b),'med R-L raw',round(a.median()-b.median()),'p',p,'centred',round(xc[x.code==1].median()-xc[x.code==2].median()),pc)
# returns
for which in ['mean']:
    for m in ['ke','sn',None]:
        x=R if m is None else R[R.monkey==m]
        x=x[x[f'eye_{which}'].notna()]
        xc=x[f'eye_{which}']-x.groupby('session')[f'eye_{which}'].transform('median')
        rgt=x.dtheta<0
        print('return',m,rgt.sum(),(~rgt).sum(), round(x[rgt][f'eye_{which}'].median()-x[~rgt][f'eye_{which}'].median()), stats.mannwhitneyu(x[rgt][f'eye_{which}'],x[~rgt][f'eye_{which}']).pvalue,
              round(xc[rgt].median()-xc[~rgt].median()), stats.mannwhitneyu(xc[rgt],xc[~rgt]).pvalue)
EOF
python devg.py 2>&1 | grep -v Warn
```

```
dtheta by code code
1   -28.052911
2    28.050487
Name: dtheta_0_600ms, dtype: float64
return dtheta sign dtheta
 1.0    2944
-1.0    2678
Name: count, dtype: int64
ke right-left by lag [-1. -1. -1. -2. -2. -3. -3. -3. -2. -2. -2. -1. -1. -2. -2. -2. -3. -4.
 -4. -4. -3. -3. -3. -3. -3. -3.]
sn right-left by lag [-1.000e+00 -4.000e+00 -2.120e+02 -4.610e+02 -7.000e+02 -8.230e+02
 -9.710e+02 -1.131e+03 -1.154e+03 -1.187e+03 -1.300e+03 -1.321e+03
 -1.319e+03 -2.333e+03 -3.104e+03 -3.072e+03 -2.672e+03 -2.367e+03
 -2.549e+03 -2.639e+03 -2.466e+03 -2.261e+03 -2.096e+03 -1.683e+03
 -1.279e+03 -8.920e+02]
eye500_mean ke 1842 1912 med R-L raw -2 p 6.4152395981294745e-102 centred -2 1.5172218826240077e-143
eye500_mean sn 970 1028 med R-L raw -1133 p 2.433490838253445e-155 centred -1052 1.5755329743647844e-153
eye500_mean None 2812 2940 med R-L raw -4 p 2.8158517767019454e-236 centred -4 2.0362499522390745e-287
eye500_l ke 1839 1912 med R-L raw -2 p 1.5979902149297653e-98 centred -2 1.3340895056459066e-142
eye500_l sn 964 1025 med R-L raw -1135 p 4.462873786024701e-146 centred -1003 9.73990200200311e-149
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && python - <<'EOF' 2>&1 | grep -v Warn
import pickle, numpy as np, pandas as pd
metas,cells,beh=pickle.load(open('dev_resall.pkl','rb'))
for s,b in beh.items(): print(s, b['has_eye'], b['eye_range'] and [round(v) for v in b['eye_range']], b['eye_saturated'] and round(b['eye_saturated'],3))
EOF
```

```
Fri Nov 13 12:41:01 UTC 2026
ke20130221 True [-3536, 4037] 0.0
ke20130301 True [-5000, 1311] 0.219
ke20130306 True [-4997, 4259] 0.038
ke20130314 True [-3687, 4158] 0.0
ke20130315 True [-3576, 4271] 0.0
ke20130327 True [-3686, 4099] 0.0
ke20130402 True [-3, 4] 0.0
ke20130404 True [-3985, 4024] 0.0
ke20130405 True [-3904, 4102] 0.0
ke20130410 True [-3591, 3989] 0.0
ke20130411 True [-4998, 3908] 0.039
ke20130412a True [-3737, 4203] 0.0
ke20130716 True [-5000, 2428] 0.052
ke20130717 True [-3822, 4205] 0.003
ke20130718 True [-3294, 4231] 0.004
ke20130722 True [-4977, 3897] 0.008
ke20130726 True [-3687, 5000] 0.018
ke20131023 True [-4, 4] 0.0
ke20131024 True [-4, 4] 0.0
[... 48 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/wirth-2017 && python - <<'EOF'
s=open('wirth.py').read()
old='''EYE_SAT = 4990.0   # samples at the +-4999.85 rail are saturated (shown in the notebook)
'''
new='''EYE_RAIL = 0.9999  # samples at the rail (+-4999.85 or +-4.99985) are saturated (notebook)
'''
s=s.replace(old,new)
s=s.replace('''        v = np.vstack([c["eye"]["l_hor"][i0:i1], c["eye"]["r_hor"][i0:i1]])
        v = np.where(np.abs(v) < EYE_SAT, v, np.nan)''','''        v = np.vstack([c["eye"]["l_hor"][i0:i1], c["eye"]["r_hor"][i0:i1]])
        v = np.where(np.abs(v) < EYE_RAIL * c["eye_rail"], v, np.nan)''')
s=s.replace('''        v = c["eye"][f"{which}_hor"][i0:i1]
        v = np.where(np.abs(v) < EYE_SAT, v, np.nan)''','''        v = c["eye"][f"{which}_hor"][i0:i1]
        v = np.where(np.abs(v) < EYE_RAIL * c["eye_rail"], v, np.nan)''')
s=s.replace('''        out["eye_units"] = ",".join(sorted(eye_units)) or None''','''        out["eye_units"] = ",".join(sorted(eye_units)) or None
        # the files hold the eye signal on a +-5000 or a +-5 scale; the rail is that bound
        big = max(float(np.nanmax(np.abs(v))) for v in out["eye"].values()) if n else 0.0
        out["eye_rail"] = 5000.0 * 0.99997 if big > 10 else 5.0 * 0.99997''')
s=s.replace('''        eye_sat = float(np.mean(np.abs(v) >= EYE_SAT))''','''        eye_sat = float(np.mean(np.abs(v) >= EYE_RAIL * c["eye_rail"]))''')
s=s.replace('''            "has_eye": c["eye"] is not None}''','''            "has_eye": c["eye"] is not None,
            "eye_scale": None if c["eye"] is None else ("+-5000" if c["eye_rail"] > 10 else "+-5")}''')
open('wirth.py','w').write(s)
EOF
grep -n "EYE_SAT\|eye_rail" wirth.py
```

```
155:        out["eye_rail"] = 5000.0 * 0.99997 if big > 10 else 5.0 * 0.99997
623:        v = np.where(np.abs(v) < EYE_RAIL * c["eye_rail"], v, np.nan)
628:        v = np.where(np.abs(v) < EYE_RAIL * c["eye_rail"], v, np.nan)
685:        eye_sat = float(np.mean(np.abs(v) >= EYE_RAIL * c["eye_rail"]))
694:            "eye_scale": None if c["eye"] is None else ("+-5000" if c["eye_rail"] > 10 else "+-5")}
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('wirth.py').read()
old='''    rets = return_turns(c)
    for r in rets:'''
new='''    t60 = c["t60"]
    clock = {}
    for nm, tt in (("start", tr["t_start"]), ("center", tr["t_center"]), ("reward", tr["t_reward"])):
        for sh in (0.0, -1.0, 1.0):
            i = np.searchsorted(t60[:, 0], tt[np.isfinite(tt)] + sh)
            i = i[i < len(t60)]
            clock[(nm, sh)] = float(np.nanmedian(t60[i, 4])) if len(i) else np.nan
    rets = return_turns(c)
    for r in rets:'''
assert old in s
s=s.replace(old,new)
s=s.replace('''            "turns": turns, "returns": rets,''','''            "turns": turns, "returns": rets, "abscissa_at_events": clock,''')
open('wirth.py','w').write(s)
EOF
date -u
```

```
Fri Nov 13 12:41:57 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "entries/wirth-2017/build_nb.py",
 "content": "\"\"\"Builds reproduce_wirth_2017.ipynb from the cells below (cells split on '# %%').\"\"\"\nimport re\nimport sys\n\nimport nbformat\n\nSRC = open(sys.argv[1]).read()\nnb = nbformat.v4.new_notebook()\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nfor block in re.split(r\"^# %%\", SRC, flags=re.M)[1:]:\n    head, _, body = block.partition(\"\\n\")\n    tags = re.findall(r\"tags=\\[([^\\]]*)\\]\", head)\n    tags = [t.strip().strip(\"'\\\"\") for t in tags[0].split(\",\")] if tags else []\n    body = body.strip(\"\\n\")\n    if \"[markdown]\" in head:\n        body = \"\\n\".join(line[2:] if line.startswith(\"# \") else line.lstrip(\"#\") for line in body.splitlines())\n        cell = nbformat.v4.new_markdown_cell(body)\n    else:\n        cell = nbformat.v4.new_code_cell(body)\n    if tags:\n        cell.metadata[\"tags\"] = tags\n    nb.cells.append(cell)\nnbformat.write(nb, sys.argv[2])\n"
}
```

```
File created successfully at: entries/wirth-2017/build_nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
mv entries/wirth-2017/build_nb.py $TMPDIR/; date -u
```

```
Fri Nov 13 12:42:25 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb_src.py",
 "content": "# %% [markdown]\n# # Reproducing Wirth et al. (2017) from CRCNS hc-12\n#\n# Paper. Wirth S, Baraduc P, Plante A, Pinede S, Duhamel JR (2017). Gaze-informed, task-situated\n# representation of space in primate hippocampus during virtual navigation. PLoS Biology 15(2):\n# e2001045. [doi:10.1371/journal.pbio.2001045](https://doi.org/10.1371/journal.pbio.2001045).\n# The claims file (`claims/wirth-2017.yaml`) was written from the version of record (PMC5328243),\n# Results, Methods and the legends of Figs 1 to 7 and S1 to S7; S1 Appendix was not available.\n#\n# Datasets. CRCNS [hc-12](https://doi.org/10.6080/K0R49NQV) (189 cells, the new-maze sessions;\n# every claim rests on it) and CRCNS [hc-21](https://doi.org/10.6080/K0GX48R9) (101 cells, a\n# familiar and a new maze per file), streamed from the public bucket `crcnsarchive`\n# (`hc-12/live/data.tar.gz`, `hc-21/live/data.tar.gz`). CRCNS data sets are not versioned; the\n# version is recorded as `unversioned`, and the MD5 sums from each data set's `checksums.md5`\n# for the files read are: hc-12 `data.tar.gz` 426c7d00c0358f2cc9873e0dbb331e2f (descriptor\n# version 0.7, 17 Jan 2017); hc-21 `data.tar.gz` dee5e8aa4a7b3c44b61b8cecfe622a0a (descriptor\n# version 0.52, 21 Dec 2018). Each data set has one published state (`live/`, with only\n# documentation under `orig/`), so the version pinned is the only one there is, and hc-12 is the\n# deposit the paper cites. hc-21 is read only to check whether it holds recordings that are also\n# in hc-12 and whether it holds the probe sessions hc-12 lacks; no claim rests on it.\n#\n# | Claim | Tested here |\n# |---|---|\n# | gaze-anticipates-action, gaze-anticipates-landmarks | tested (eye-signal sign assumed) |\n# | learning-trials, learning-to-90 | tested |\n# | probe-transfer | tested on monkey K; monkey S has no probe session in hc-12 |\n# | probe-faster-criterion | blocked: methods underspecified (learning-curve method of reference 60) |\n# | cells-recorded | tested |\n# | responsive-cells, multi-space-coding, state-space-ic-higher, sparsity-gaze-vs-state, spatial-selectivity-fraction | blocked: the point-of-gaze space cannot be built (no eye calibration); three-space results shown |\n# | state-space-most-responsive | tested on the state-space count, which needs no gaze |\n# | direction-center-vs-periphery, direction-tuning-not-maintained | tested |\n# | sparsity-state-vs-direction, sparsity-state-vs-position | tested |\n# | state-space-selectivity, landmark-identity-distance, landmark-identity-center | tested by bounds on the responsive set |\n# | path-selectivity, gaze-aligned-dynamics, latency-skew, eccentricity-modulation, foveation-selectivity, gaze-map-landmarks | blocked: need calibrated gaze |\n# | fields-per-cell, dimensionality-control | blocked: methods underspecified (S1 Appendix) |\n\n# %%\nimport resource\nimport time\nimport warnings\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\n\nimport wirth\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\npd.set_option(\"display.width\", 220)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 200)\n\n# %% [markdown]\n# ## One pass over hc-12\n#\n# The archive is streamed once. For each cell file the helper keeps the new-maze trials, the\n# camera rows inside the new-maze session, the spikes and the eye signal, computes every map\n# measure with 999 surrogates under both surrogate readings, the landmark ANOVAs, and, once per\n# session, the behaviour. Seeds are fixed per cell (CRC32 of the file name).\n\n# %%\nt0 = time.time()\nmetas, cells, beh = wirth.collect(\"hc-12\", log=None)\nM = pd.DataFrame(metas)\nC_all = pd.DataFrame(cells)\nprint(f\"hc-12 pass: {time.time() - t0:.0f} s, peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n\n# %%\nt0 = time.time()\nfp21 = pd.DataFrame(wirth.fingerprint(\"hc-21\", log=None))\nprint(f\"hc-21 pass: {time.time() - t0:.0f} s, {len(fp21)} files\")\n\n# %% [markdown]\n# ## Data check\n\n# %% tags=[\"sanity\"]\nprint(\"Files by monkey (ke = monkey K, sn = monkey S):\")\nprint(M.groupby(\"monkey\").agg(files=(\"file\", \"size\"), with_new_maze=(\"has_newallo\", \"sum\"),\n                              sessions=(\"session\", \"nunique\")).to_string())\nprint(\"\\nFiles without a new-maze (newallo) field:\", M.loc[~M.has_newallo, \"file\"].tolist())\nprint(\"\\nSpike times taken from:\", M.spike_src.value_counts().to_dict())\nprint(\"Top-level field sets:\", M.fields.nunique(), \"different layouts\")\nprint(\"Camera frame interval (ms):\", M.frame_dt_ms.describe()[[\"min\", \"max\"]].round(3).to_dict())\nprint(\"Eye sample interval (ms):\", M.eye_dt_ms.describe()[[\"min\", \"max\"]].round(3).to_dict(),\n      \"; files without eye data:\", int((~M.has_eye.fillna(False).astype(bool)).sum() - (~M.has_newallo).sum()))\nprint(\"Spike times sorted in every file:\", bool(M.spikes_sorted.dropna().all()))\nrng_cols = [\"x_min\", \"x_max\", \"y_min\", \"y_max\", \"theta_min\", \"theta_max\", \"abscissa_max\"]\nprint(\"\\nRanges of the camera variables over files (min / max of each):\")\nprint(M[rng_cols].agg([\"min\", \"max\"]).round(2).to_string())\nprint(\"\\nTrials per new-maze session (per file):\", M.n_trials.describe()[[\"min\", \"50%\", \"max\"]].to_dict())\nprint(\"Session length, first trial start to last trial end (min):\",\n      ((M.t_end - M.t_start) / 60).describe()[[\"min\", \"50%\", \"max\"]].round(1).to_dict())\n\n# %% [markdown]\n# The descriptor (hc-12, version 0.7) gives the positions as virtual X, Y. The values span x from\n# -16 to 12.9 and y from -15.2 to 15.2, five arm ends at radius 16 m (Methods: radius 16 m), so\n# positions are in metres. The camera orientation is in degrees, on 0 to 360 in some files and\n# -180 to 180 in others; the analysis takes it modulo 360. Column 5 (curvilinear abscissa along\n# the branch) runs from 0 at the centre to 1 at the arm end, a fraction of the arm, not metres.\n# Camera rows are at 60 Hz and eye samples at 200 Hz (5 ms), where the descriptor says 250 Hz.\n\n# %% tags=[\"sanity\"]\nB = pd.DataFrame([{k: v for k, v in b.items() if k in (\"monkey\", \"session\", \"n_trials\", \"learningtrial\", \"has_eye\", \"eye_scale\", \"eye_saturated\")}\n                  for b in beh.values()])\nlc_ok = M.lc_order_ok.dropna()\nprint(\"Learning curves: column 2 <= column 1 <= column 3 in\", int(lc_ok.sum()), \"of\", len(lc_ok), \"files\")\ncrit_files = []\nfor b in beh.values():\n    crit = wirth.lower_bound_criterion(b[\"lc\"][:, 1])\n    crit_files.append((b[\"learningtrial\"], crit))\nsame = sum((np.isnan(c) and lt == -2) or lt == c for lt, c in crit_files)\nprint(\"Field learningtrial equals the first trial with column 2 > 1/4 (or -2 when never):\", same, \"of\", len(crit_files), \"sessions\")\nprint(\"\\nEye signal scale by session:\", B.eye_scale.value_counts(dropna=False).to_dict())\nprint(\"Fraction of eye samples at the +-5000 / +-5 rail, by session: median\",\n      round(B.eye_saturated.median(), 4), \"max\", round(B.eye_saturated.max(), 3))\nrew = pd.Series({s: tuple(np.unique(b[\"chosen_arm\"][b[\"correct\"]]).astype(int)) for s, b in beh.items()})\nprint(\"\\nArm chosen on rewarded trials (1-5 = codes 50-54), sessions per value:\", rew.value_counts().to_dict())\ntag_arm = []\nfor b in beh.values():\n    pass\nprint(\"\\nCamera abscissa (0 centre, 1 arm end) at event times, median over sessions:\")\nab = pd.DataFrame([{f\"{k[0]} {k[1]:+.0f}s\": v for k, v in b[\"abscissa_at_events\"].items()} for b in beh.values()])\nprint(ab.median().round(2).to_string())\n\n# %% [markdown]\n# Checks against the description:\n# - The descriptor says the learning curve's middle column is the probability of a correct\n#   response, with the bounds in columns 1 and 3. In every file column 2 is the lowest and column\n#   3 the highest, so column 1 is the probability, column 2 the lower bound and column 3 the upper\n#   bound. The field `learningtrial`, which the descriptor does not describe, equals the first\n#   trial whose column 2 exceeds 1/4 (S3B legend's criterion), which confirms that reading.\n# - The descriptor says code 43 is the rewarded start arm and code 53 the rewarded chosen arm. The\n#   arm chosen on rewarded trials differs between sessions (printed above), as each day had a new\n#   reward location (Results); 53 is the rewarded arm only in some sessions.\n# - The eye signal is in undocumented units, on a +-5000 scale in some sessions and a +-5 scale in\n#   others, with a rail at the bound; no calibration to degrees is given. Eye samples are 5 ms\n#   apart (200 Hz), where the descriptor says 250 Hz.\n# - The camera rows share the trial clock: at the trial start (code 21) the abscissa is at the arm\n#   end, at the arrival at the choice point (code 22) it is 0, and one second later or earlier it is\n#   not (printed above).\n\n# %% tags=[\"sanity\"]\nC = C_all[C_all.n_spikes_window > 100].copy()\nprint(\"Cells with a new maze:\", len(C_all), \"; with more than 100 spikes in the new-maze session:\", len(C),\n      C.groupby(\"monkey\").size().to_dict())\nsh_cols = [c for c in C.columns if c.startswith(\"shift_ic|\")]\nresp_state = C[\"icp|('full', 'state')|permute\"] < 0.01\nrel = C.loc[resp_state, sh_cols].div(C.loc[resp_state, \"shift_ic|0.0\"], axis=0)\nprint(\"\\nClock check for the spikes: state-space IC with the spikes shifted in time, relative to no shift,\")\nprint(\"median over the\", int(resp_state.sum()), \"cells with significant state-space IC (and over all cells, unnormalized):\")\nprint(pd.DataFrame({\"relative (sig. cells)\": rel.median().round(3).values,\n                    \"IC bits/spike (all cells)\": C[sh_cols].median().round(3).values},\n                   index=[c.split(\"|\")[1] + \" s\" for c in sh_cols]).T.to_string())\n\n# %% [markdown]\n# The spike clock check selects cells at zero shift, so the peak there is partly a selection\n# effect; the fall of the information with shifts of 2 to 5 s is consistent with spikes and camera\n# sharing one clock, without proving it. The eye clock is checked with the turn codes in the\n# section on gaze anticipation.\n\n# %% tags=[\"sanity\"]\n# Recordings deposited twice: hc-12 against hc-21, by spike count and first spike times.\nfp12 = M[M.has_newallo][[\"file\", \"session\", \"n_spikes_file\", \"first_spikes\"]].copy()\nfp12[\"head\"] = fp12.first_spikes.apply(lambda t: tuple(np.round(t[:5], 3)))\nfp21m = fp21[fp21.has_maze].copy()\nfp21m[\"head\"] = fp21m.spikes_head.apply(lambda t: tuple(np.round(t[:5], 3)))\npairs = fp12.merge(fp21m, on=\"head\", suffixes=(\"_hc12\", \"_hc21\"))\nprint(\"hc-21 files:\", len(fp21), \"; with a new maze:\", int(fp21.has_maze.sum()),\n      \"; sessions:\", fp21.session.nunique(), fp21.drop_duplicates(\"session\").session.str[:2].value_counts().to_dict())\nprint(\"hc-12 / hc-21 file pairs with the same first five spike times:\", len(pairs))\nif len(pairs):\n    print(pairs[[\"file_hc12\", \"file_hc21\", \"n_spikes_file\", \"n_spikes\", \"n_trials\"]].to_string())\nprint(\"Sessions (dates) in both data sets:\", sorted(set(M.session) & set(fp21.session)))\ndup12 = fp12.groupby([\"head\", \"n_spikes_file\"]).file.apply(list)\nprint(\"hc-12 files sharing spike trains with another hc-12 file:\", [v for v in dup12 if len(v) > 1])\n\n# %% [markdown]\n# ## cells-recorded\n#\n# > Of 270 cells recorded in the right hippocampus (128 in monkey S, 142 in monkey K), 189 fired\n# > more than 100 spikes per session and were analysed.\n\n# %% tags=[\"claim:cells-recorded\"]\ncr = pd.DataFrame({\"files\": M.groupby(\"monkey\").size(),\n                   \"with_new_maze\": M.groupby(\"monkey\").has_newallo.sum(),\n                   \"over_100_spikes\": C.groupby(\"monkey\").size()})\ncr.loc[\"total\"] = cr.sum()\nprint(cr.to_string())\nprint(\"\\nRecording locations (AP, ML, DV relative to the interaural line) present in\", int(M.reclocation.notna().sum()), \"files;\",\n      \"the files give no subfield (CA3, CA1, dentate gyrus).\")\n\n# %% [markdown]\n# ## Learning: learning-trials and learning-to-90\n#\n# > Both monkeys learned the rewarded arm in about a dozen trials; monkey S performed above chance\n# > after 12.3 plus or minus 2 trials (SEM) and monkey K after 14.8 plus or minus 2.4.\n#\n# The curves are the files' own (columns as established in the data check). Probe sessions are\n# defined in the probe-transfer section; reading (b) leaves them out. Sessions whose lower bound\n# never exceeds 1/4 have no trial to criterion and are counted apart.\n\n# %%\ndef probe_info(b):\n    sa = b[\"start_arm\"]\n    first = set(sa[:10][np.isfinite(sa[:10])].astype(int))\n    if len(first) > 2:\n        return False, None, first\n    intro = next((i for i in range(len(sa)) if np.isfinite(sa[i]) and int(sa[i]) not in first), None)\n    return intro is not None, intro, first\n\n\nrows = []\nfor s, b in beh.items():\n    lc = b[\"lc\"]\n    crit = wirth.lower_bound_criterion(lc[:, 1])\n    up = [u for u in np.nonzero(lc[:, 2] >= 0.9)[0] if np.isfinite(crit) and u + 1 >= crit]\n    is_probe, intro, first = probe_info(b)\n    rows.append({\"session\": s, \"monkey\": b[\"monkey\"], \"n_trials\": b[\"n_trials\"], \"probe\": is_probe,\n                 \"intro\": intro, \"first_arms\": sorted(first), \"crit\": crit,\n                 \"t90\": (up[0] + 1 - crit) if up else np.nan, \"pc\": b[\"correct\"].mean()})\nS = pd.DataFrame(rows)\n\n# %% tags=[\"claim:learning-trials\"]\nfor name, sub in ((\"(a) all sessions\", S), (\"(b) sessions that are not probe sessions\", S[~S.probe])):\n    g = sub.groupby(\"monkey\").crit.agg(mean=\"mean\", sem=\"sem\", sessions_reaching=\"count\",\n                                       sessions_never=lambda x: int(x.isna().sum()), median=\"median\")\n    print(name); print(g.round(2).to_string()); print()\nprint(\"Expected: monkey S (sn) 12.3 +- 2, monkey K (ke) 14.8 +- 2.4\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% tags=[\"claim:learning-to-90\"]\nfor name, sub in ((\"(a) all sessions\", S), (\"(b) not probe sessions\", S[~S.probe])):\n    reach = sub.t90.notna()\n    print(f\"{name}: sessions reaching both criteria {int(reach.sum())} of {len(sub)}; \"\n          f\"fewer than 10 trials from lower bound > 1/4 to upper bound >= 0.9: {int((sub.t90 < 10).sum())}, \"\n          f\"fraction of sessions reaching {(sub.t90 < 10).sum() / reach.sum():.3f}, of all sessions {(sub.t90 < 10).mean():.3f}\")\nprint(\"Trials from criterion to upper bound 0.9 (sessions reaching):\", S.t90.describe()[[\"min\", \"50%\", \"max\"]].to_dict())\nprint(\"Expected 0.89 +- 0.089\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## probe-transfer\n#\n# > In probe sessions, performance after the new western entries were introduced was higher than\n# > at the start of the session (monkey K 73% against 44%, monkey S 80% against 55%).\n#\n# A probe session is read from the start arms: the first 10 trials use one or two entries and\n# later trials use others (Results; S3C legend: one entry for 36 trials, or two entries until trial\n# 60). The introduction is the first trial from an entry not used in the first 10.\n\n# %% tags=[\"claim:probe-transfer\"]\nP = S[S.probe].copy()\nP[\"pc_first5\"] = [beh[s][\"correct\"][:5].mean() for s in P.session]\nP[\"pc_after5\"] = [beh[s][\"correct\"][int(i):int(i) + 5].mean() for s, i in zip(P.session, P.intro)]\nprint(P[[\"session\", \"monkey\", \"n_trials\", \"first_arms\", \"intro\", \"pc_first5\", \"pc_after5\"]].to_string())\nprint(\"\\nProbe sessions per monkey:\", P.groupby(\"monkey\").size().to_dict(), \"(paper: 9 for S, 15 for K)\")\nprint(\"Sessions of monkey S whose first 10 trials use at most two entries:\",\n      int(((S.monkey == \"sn\") & S.first_arms.apply(len).le(2)).sum()))\nprint((P.groupby(\"monkey\")[[\"pc_first5\", \"pc_after5\"]].mean() * 100).round(1).to_string())\nif len(P) > 1:\n    w = stats.wilcoxon(P.pc_after5, P.pc_first5)\n    print(f\"Wilcoxon signed-rank, after against first 5 trials, {len(P)} sessions: W = {w.statistic}, p = {w.pvalue:.4f}\")\n    print(\"Median difference (after - first):\", (P.pc_after5 - P.pc_first5).median())\nprint(\"\\nExpected: K 73 +- 7.3 after, 44 +- 4.4 at the start; S 80 +- 8, 55 +- 5.5\")\n# hc-21: sessions whose first 10 start codes use at most two entries\nfp21m[\"first_arms\"] = fp21m.codes_head.apply(lambda c: sorted(set(c)))\np21 = fp21m[fp21m.first_arms.apply(len) <= 2].drop_duplicates(\"session\")\nprint(\"hc-21 new-maze sessions whose first 10 trials use at most two entries:\", p21.session.tolist())\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## gaze-anticipates-action\n#\n# > During the 500 ms before each joystick action, gaze anticipated the direction of the\n# > subsequent movement.\n#\n# Each left (code 2) or right (code 1) joystick move; mean horizontal eye signal in the 500 ms\n# (reading a) or 300 ms (reading b) before it, for successful trials (Method W) and, as a variant,\n# all trials. The eye signal is in uncalibrated units on two scales (data check), so values are\n# standardized within each session (minus the session median, over the session's SD) before\n# pooling sessions; per-session differences are also counted. Wilcoxon rank-sum, right against\n# left, per monkey (reading i) and pooled (reading ii).\n\n# %%\nT = pd.DataFrame([dict(session=s, monkey=b[\"monkey\"], **t) for s, b in beh.items() for t in b[\"turns\"]])\nprint(\"Orientation change in the 600 ms after the code, median (deg):\", T.groupby(\"code\").dtheta_0_600ms.median().round(1).to_dict(),\n      \"(code 1 = right lowers the camera orientation)\")\n\n\ndef zsess(df, col):\n    g = df.groupby(\"session\")[col]\n    return (df[col] - g.transform(\"median\")) / g.transform(\"std\")\n\n\ndef rank_test(df, col, right):\n    x = df[col].dropna()\n    a, b = x[right.loc[x.index]], x[~right.loc[x.index]]\n    if len(a) < 2 or len(b) < 2:\n        return np.nan, np.nan, len(a), len(b)\n    return float(a.median() - b.median()), float(stats.mannwhitneyu(a, b).pvalue), len(a), len(b)\n\n# %% tags=[\"claim:gaze-anticipates-action\"]\nres = []\nfor trials_used, Tsub in ((\"successful\", T[T.correct]), (\"all\", T)):\n    Tsub = Tsub.copy()\n    for w in (\"eye500\", \"eye300\"):\n        for eye in (\"mean\", \"l\", \"r\"):\n            col = f\"{w}_{eye}\"\n            Tsub[\"z\"] = zsess(Tsub, col)\n            for mk in (\"ke\", \"sn\", \"both\"):\n                d = Tsub if mk == \"both\" else Tsub[Tsub.monkey == mk]\n                diff, p, na, nb = rank_test(d, \"z\", d.code == 1)\n                sess_diff = d.groupby(\"session\").apply(lambda g: g[g.code == 1][col].median() - g[g.code == 2][col].median()).dropna()\n                res.append({\"trials\": trials_used, \"window\": w[3:] + \" ms\", \"eye\": eye, \"monkey\": mk,\n                            \"n_right\": na, \"n_left\": nb, \"median z right-left\": round(diff, 3), \"p\": p,\n                            \"sessions right<left\": f\"{int((sess_diff < 0).sum())}/{len(sess_diff)}\"})\nR1 = pd.DataFrame(res)\nprint(R1.to_string())\nlags = [c for c in T.columns if c.startswith(\"lag\")]\nTc = T[T.correct].copy()\nprof = {}\nfor mk in (\"ke\", \"sn\"):\n    d = Tc[Tc.monkey == mk].copy()\n    for c in lags:\n        d[c] = zsess(d, c)\n    prof[mk] = (d[d.code == 1][lags].median() - d[d.code == 2][lags].median()).values\nprint(\"\\nEye clock check: median standardized eye signal, right minus left turns, in 100 ms windows from the code:\")\nprint(pd.DataFrame(prof, index=[f\"{float(c[3:]):+.1f}\" for c in lags]).T.round(2).to_string())\n\n# %% [markdown]\n# Sign of the eye signal. The files do not say which sign of the horizontal signal is rightward.\n# During a turn the view rotates, and the mean eye position in optokinetic stimulation shifts\n# toward the side of the quick phases, which is the side the observer turns to. The difference\n# right minus left grows in the same (negative) direction from the turn on, in both monkeys\n# (profile above). The analysis therefore takes a negative value as rightward, an assumption.\n#\n# **Result: ...**\n\n# %% [markdown]\n# ## gaze-anticipates-landmarks\n#\n# > When relocated to a new entry, the monkeys gazed proactively at the location where the\n# > landmarks would appear.\n#\n# Passive returns (tags 5xy between the end of a trial and the next start); a return turns right\n# when the camera orientation falls over it (as for code 1). Mean horizontal eye signal over the\n# return, standardized within session; rank-sum right against left. Returns after all trials,\n# and after successful trials as a variant (Method W).\n\n# %% tags=[\"claim:gaze-anticipates-landmarks\"]\nRt = pd.DataFrame([dict(session=s, monkey=b[\"monkey\"], **r) for s, b in beh.items() for r in b[\"returns\"]])\nres = []\nfor trials_used, Rsub in ((\"all\", Rt), (\"after successful\", Rt[Rt.correct])):\n    Rsub = Rsub.copy()\n    for eye in (\"mean\", \"l\", \"r\"):\n        Rsub[\"z\"] = zsess(Rsub, f\"eye_{eye}\")\n        for mk in (\"ke\", \"sn\", \"both\"):\n            d = Rsub if mk == \"both\" else Rsub[Rsub.monkey == mk]\n            diff, p, na, nb = rank_test(d, \"z\", d.dtheta < 0)\n            sd = d.groupby(\"session\").apply(lambda g: g[g.dtheta < 0][f\"eye_{eye}\"].median() - g[g.dtheta >= 0][f\"eye_{eye}\"].median()).dropna()\n            res.append({\"returns\": trials_used, \"eye\": eye, \"monkey\": mk, \"n_right\": na, \"n_left\": nb,\n                        \"median z right-left\": round(diff, 3), \"p\": p, \"sessions right<left\": f\"{int((sd < 0).sum())}/{len(sd)}\"})\nprint(\"Median absolute orientation change over a return (deg):\", round(Rt.dtheta.abs().median(), 1))\nprint(pd.DataFrame(res).to_string())\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## Information content in the coding spaces\n#\n# The point-of-gaze space needs the gaze direction in degrees, which the files cannot give (the\n# eye signal is uncalibrated, data check). Position, direction and state space are computed for\n# the cells with more than 100 spikes in the new-maze session. Readings: trial window \"full\"\n# (start to next start) or \"toreward\" (start to reward); surrogates \"permute\" or \"shift\"\n# (Method W). Significance is the bilateral surrogate p < 0.01. The responsive set of the paper\n# needs all four spaces; the set responsive in the three spaces here is contained in it, and all\n# cells contain it, so counts over these two sets bound the count over the paper's set.\n\n# %%\nREADINGS = [(\"full\", \"permute\"), (\"full\", \"shift\"), (\"toreward\", \"permute\"), (\"toreward\", \"shift\")]\nSPACES = (\"position\", \"direction\", \"state\")\n\n\ndef sig(space, r, sr, alpha=0.01):\n    return C[f\"icp|('{r}', '{space}')|{sr}\"] < alpha\n\n\nrows = []\nfor r, sr in READINGS:\n    sg = {k: sig(k, r, sr) for k in SPACES}\n    n_sig = sum(v.astype(int) for v in sg.values())\n    rows.append({\"trials\": r, \"surrogates\": sr, **{k: int(v.sum()) for k, v in sg.items()},\n                 \"any of three\": int((n_sig > 0).sum()), \"two or more\": int((n_sig >= 2).sum()),\n                 \"cells\": len(C)})\nIC3 = pd.DataFrame(rows)\nprint(IC3.to_string())\nprint(\"\\nMedian number of valid bins per map:\", C[[c for c in C.columns if c.startswith(\"nbins|\")]].median().to_dict())\n\n# %% [markdown]\n# ## responsive-cells (blocked) and state-space-most-responsive\n#\n# > 111 of the 189 cells (59%) had significant information content in at least one of the four\n# > coding spaces.\n#\n# > The proportions of cells responsive to each space were unequal; the state space accounted for\n# > the most cells (84), and more cells were responsive to state space than to point of gaze.\n\n# %% tags=[\"claim:state-space-most-responsive\"]\nprint(\"Cells with significant state-space IC (p < 0.01), per reading, and per monkey:\")\nfor r, sr in READINGS:\n    s_ = sig(\"state\", r, sr)\n    print(f\"  {r}/{sr}: {int(s_.sum())} of {len(C)}\", s_.groupby(C.monkey).sum().to_dict())\nprint(\"Expected 84 +- 8.4 (75.6 to 92.4)\")\nprint(\"\\nThree-space responsive cells per reading (a lower bound of the paper's 111 +- 11.1):\", IC3[\"any of three\"].tolist())\nprint(\"One-sided variant (upper tail p < 0.01, i.e. bilateral p < 0.02), state space:\",\n      [int(sig(\"state\", r, sr, 0.02).sum()) for r, sr in READINGS])\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## direction-center-vs-periphery\n#\n# > For direction-selective cells, both information per spike and sparsity of directional firing\n# > were higher in the maze center than on the peripheral return paths.\n#\n# Directional maps from centre time (tags 2xy, 3xy) and return paths (tags 5xy) of successful\n# trials with their returns (reading \"full\"), at one common angular resolution per session.\n# Normalized IC and sparsity (minus the surrogate mean); Wilcoxon signed-rank across cells.\n\n# %% tags=[\"claim:direction-center-vs-periphery\"]\ndir_rows = []\nfor sr in (\"permute\", \"shift\"):\n    for cellset, mask in ((\"(a) direction IC p < 0.01\", sig(\"direction\", \"full\", sr)),\n                          (\"(b) three-space responsive\", sum(sig(k, \"full\", sr).astype(int) for k in SPACES) > 0)):\n        d = C[mask]\n        for meas in (\"ic\", \"sp\"):\n            a, b_ = d[f\"{meas}n|center|{sr}\"], d[f\"{meas}n|return|{sr}\"]\n            ok = a.notna() & b_.notna()\n            w = stats.wilcoxon(a[ok], b_[ok])\n            dir_rows.append({\"surrogates\": sr, \"cells\": cellset, \"measure\": {\"ic\": \"IC\", \"sp\": \"sparsity\"}[meas],\n                             \"n\": int(ok.sum()), \"median centre\": round(a[ok].median(), 3),\n                             \"median return\": round(b_[ok].median(), 3),\n                             \"median diff\": round((a[ok] - b_[ok]).median(), 3),\n                             \"centre higher\": int((a[ok] > b_[ok]).sum()), \"p\": w.pvalue})\nprint(pd.DataFrame(dir_rows).to_string())\nprint(\"\\nValid direction bins: centre median\", C[\"nbins|center\"].median(), \", return median\", C[\"nbins|return\"].median())\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## direction-tuning-not-maintained\n#\n# > Direction tuning was not maintained across positions; the correlation between directional\n# > tuning in the center and on return paths was significantly low in 20 of 56 cells (36%), more\n# > than chance, and significantly high in only 3, consistent with chance.\n#\n# Uncentered correlation over the bins valid in both maps (Methods, Directional correlations);\n# low or high when the actual value is in the lower or upper 2.5% of the surrogates; binomial\n# chance rate 0.025 (claims file). Cells with at least 10 common valid bins (a standard choice;\n# 2 shown as a variant).\n\n# %% tags=[\"claim:direction-tuning-not-maintained\"]\nrows = []\nfor sr in (\"permute\", \"shift\"):\n    for cellset, mask in ((\"(a) direction IC p < 0.01\", sig(\"direction\", \"full\", sr)),\n                          (\"(b) three-space responsive\", sum(sig(k, \"full\", sr).astype(int) for k in SPACES) > 0)):\n        for min_common in (10, 2):\n            d = C[mask & (C.n_common >= min_common) & C[f\"corr_lo|{sr}\"].notna()]\n            lo = int((d[f\"corr_lo|{sr}\"] <= 0.025).sum())\n            hi = int((d[f\"corr_up|{sr}\"] <= 0.025).sum())\n            rows.append({\"surrogates\": sr, \"cells\": cellset, \"min common bins\": min_common, \"n\": len(d),\n                         \"low\": lo, \"high\": hi, \"p binom low\": wirth.binom_upper(lo, len(d), 0.025),\n                         \"p binom high\": wirth.binom_upper(hi, len(d), 0.025),\n                         \"median corr\": round(d.corr.median(), 3) if len(d) else np.nan})\nprint(pd.DataFrame(rows).to_string())\nprint(\"Expected: tested 56 +- 5.6, low 20 +- 2 with binomial p < 0.001, high 2 to 4\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## sparsity-state-vs-direction and sparsity-state-vs-position\n#\n# > Sparsity was significantly higher in state space than in direction space.\n#\n# > Sparsity was not significantly higher in state space than in position space overall, but the\n# > 15 cells whose difference was individually significant were sparser in state space.\n#\n# Cells with significant IC in both spaces compared; per cell normalized state-space sparsity\n# minus the other space's; Wilcoxon signed-rank. The per-cell difference is significant when its\n# surrogate p (the difference recomputed on each surrogate) is below 0.05 (reading a) or 0.01 (b).\n\n# %%\ndef sparsity_compare(other):\n    rows = []\n    for r, sr in READINGS:\n        both = sig(\"state\", r, sr) & sig(other, r, sr)\n        d = C[both]\n        diff = d[f\"spn|('{r}', 'state')|{sr}\"] - d[f\"spn|('{r}', '{other}')|{sr}\"]\n        w = stats.wilcoxon(diff) if len(diff) > 1 else None\n        row = {\"trials\": r, \"surrogates\": sr, \"cells in both\": len(d), \"median diff\": round(diff.median(), 4),\n               \"state sparser\": int((diff > 0).sum()), \"p\": w.pvalue if w else np.nan}\n        for lvl, nm in ((0.05, \"a\"), (0.01, \"b\")):\n            ind = d[f\"spdiffp|{r}|{other}|{sr}\"] < lvl\n            sub = diff[ind]\n            ws = stats.wilcoxon(sub) if len(sub) > 1 else None\n            row.update({f\"indiv sig ({nm})\": int(ind.sum()), f\"their median ({nm})\": round(sub.median(), 4) if len(sub) else np.nan,\n                        f\"their p ({nm})\": ws.pvalue if ws else np.nan})\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n# %% tags=[\"claim:sparsity-state-vs-direction\"]\nprint(sparsity_compare(\"direction\").to_string())\n\n# %% [markdown]\n# **Result: ...**\n\n# %% tags=[\"claim:sparsity-state-vs-position\"]\nprint(sparsity_compare(\"position\").to_string())\nprint(\"Expected: overall not significant (p >= 0.05); individually significant 15 +- 1.5, sparser in state space with p < 0.05\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## state-space-selectivity\n#\n# > In the maze center, at the same position and direction, 12 of 111 responsive cells (11%)\n# > showed significantly high state-space selectivity, discriminating the current rotational move,\n# > more than chance; only 4 showed significantly low selectivity, as expected by chance.\n#\n# SSI per Methods, State-space selectivity; high or low when in the upper or lower 5% of the\n# surrogates (binomial chance 0.05, claims file). Counts over the three-space responsive cells\n# (lower bound) and over all cells (upper bound).\n\n# %% tags=[\"claim:state-space-selectivity\"]\nrows = []\nfor r, sr in READINGS:\n    resp3 = sum(sig(k, r, sr).astype(int) for k in SPACES) > 0\n    for cellset, mask in ((\"three-space responsive\", resp3), (\"all cells\", pd.Series(True, index=C.index))):\n        d = C[mask & C[f\"ssi_up|{sr}\"].notna()]\n        hi = int((d[f\"ssi_up|{sr}\"] <= 0.05).sum())\n        lo = int((d[f\"ssi_lo|{sr}\"] <= 0.05).sum())\n        rows.append({\"trials (responsive set)\": r, \"surrogates\": sr, \"cells\": cellset, \"n\": len(d), \"high\": hi, \"low\": lo,\n                     \"p binom high\": wirth.binom_upper(hi, len(d), 0.05), \"p binom low\": wirth.binom_upper(lo, len(d), 0.05)})\nprint(pd.DataFrame(rows).to_string())\nprint(\"Cells without an SSI (fewer than one bin with 400 ms in two move types):\", int(C.ssi.isna().sum()))\nprint(\"Bins entering the SSI, median:\", C.ssi_bins.median())\nprint(\"Expected: high 12 +- 1.2 (11 to 13) with binomial p < 0.05; low 3 to 5, not significant\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## landmark-identity-distance and landmark-identity-center\n#\n# > A two-way ANOVA of firing on the entry paths by landmark viewed and relative distance gave a\n# > main effect of landmark identity in 30 of 111 responsive cells and of relative distance in 64;\n# > 29 cells coded a combination (14 with a significant interaction, 15 with both main effects),\n# > more than chance.\n#\n# > The main effect of landmark identity was confirmed by a one-way ANOVA on firing to the four\n# > landmark views at the center, significant in 12 of 111 responsive cells, more than chance.\n\n# %%\ndef lm_counts(d):\n    a = 0.05\n    lmk, rd, it = d.lm2_p_lm < a, d.lm2_p_rd < a, d.lm2_p_int < a\n    return {\"n\": len(d), \"identity\": int(lmk.sum()), \"distance\": int(rd.sum()), \"interaction\": int(it.sum()),\n            \"both, no interaction (a)\": int((lmk & rd & ~it).sum()), \"both (b)\": int((lmk & rd).sum()),\n            \"centre one-way (a)\": int((d.lm1a_p < a).sum()), \"centre one-way (b)\": int((d.lm1b_p < a).sum())}\n\n\nrows = []\nfor r, sr in READINGS:\n    resp3 = sum(sig(k, r, sr).astype(int) for k in SPACES) > 0\n    rows.append({\"responsive set\": f\"three-space {r}/{sr}\", **lm_counts(C[resp3])})\nrows.append({\"responsive set\": \"all cells\", **lm_counts(C)})\nLM = pd.DataFrame(rows)\nprint(\"Entry paths per cell:\", C.lm2_n_lm.value_counts().to_dict(), \"; laps per cell, median:\", C.n_laps.median())\nprint(\"Residual df of the two-way ANOVA, median:\", C.lm2_df_res.median(), \"(paper's example cells: 756)\")\n\n# %% tags=[\"claim:landmark-identity-distance\"]\nprint(LM.drop(columns=[\"centre one-way (a)\", \"centre one-way (b)\"]).to_string())\nprint(\"Expected: identity 30 +- 3, distance 64 +- 6.4, interaction 14 +- 1.4, both 15 +- 1.5\")\nfx = C[[\"name\", \"session\", \"lm2_F_int\", \"lm2_p_int\", \"lm2_df_int\", \"lm2_df_res\"]].copy()\nfx[\"dist\"] = np.minimum(abs(fx.lm2_F_int - 4.4076), abs(fx.lm2_F_int - 2.1243))\nprint(\"\\nCells whose interaction F comes nearest the Fig 5 values (4.41 and 2.12):\")\nprint(fx.nsmallest(4, \"dist\").round(4).to_string())\n\n# %% [markdown]\n# **Result: ...**\n\n# %% tags=[\"claim:landmark-identity-center\"]\nprint(LM[[\"responsive set\", \"n\", \"centre one-way (a)\", \"centre one-way (b)\"]].to_string())\nprint(\"Expected 12 +- 1.2 (11 to 13), binomial p < 0.05 at chance 0.05\")\nprint(\"Groups in the one-way ANOVAs:\", C.lm1a_groups.value_counts().to_dict(), C.lm1b_groups.value_counts().to_dict())\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## Claims blocked by the missing gaze calibration: three-space results\n#\n# These numbers do not decide an outcome; they show how far the claims can be followed without\n# the point-of-gaze space.\n\n# %%\nr, sr = \"full\", \"permute\"\nresp3 = sum(sig(k, r, sr).astype(int) for k in SPACES) > 0\nprint(f\"Reading {r}/{sr}: responsive in three spaces {int(resp3.sum())} of {len(C)} ({resp3.mean():.2f});\",\n      f\"two or more spaces {IC3.loc[0, 'two or more']}; position IC p < 0.01 {int(sig('position', r, sr).sum())} \"\n      f\"({sig('position', r, sr).mean():.3f} of the cells)\")\nfor other in (\"position\", \"direction\"):\n    both = sig(\"state\", r, sr) & sig(other, r, sr)\n    d = C[both]\n    diff = d[f\"icn|('{r}', 'state')|{sr}\"] - d[f\"icn|('{r}', '{other}')|{sr}\"]\n    print(f\"State-space minus {other} normalized IC, {len(d)} cells: median {diff.median():.3f}, Wilcoxon p = {stats.wilcoxon(diff).pvalue:.3g}\")\n\n# %% [markdown]\n# ## Summary\n#\n# Filled in after the run.\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb_src.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > dev3.py <<'EOF'
import sys, pickle, time
sys.path.insert(0,'entries/wirth-2017')
import wirth
t=time.time()
metas=[]; beh={}
for name,d in wirth.stream_members('hc-12'):
    c=wirth.reduce_file(name,d); metas.append(wirth.file_meta(name,d,c))
    if c is None: continue
    b=beh.get(c['session'])
    if b is None or b['n_trials']<len(c['cm']): beh[c['session']]=wirth.behaviour(c)
print('hc12',time.time()-t)
fp=wirth.fingerprint('hc-21')
print('hc21',time.time()-t)
_,cells,_=pickle.load(open('dev_resall.pkl','rb'))
pickle.dump((metas,cells,beh,fp),open('dev_all2.pkl','wb'))
EOF
python dev3.py 2>&1 | grep -v Warn | tail -3
```

```
hc12 319.31054186820984
hc21 495.14993500709534
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
s=open('nb_src.py').read()
s=s.replace('metas, cells, beh = wirth.collect("hc-12", log=None)','import pickle; metas, cells, beh, _fp = pickle.load(open("/tmp/claude-1001/dev_all2.pkl","rb"))')
s=s.replace('fp21 = pd.DataFrame(wirth.fingerprint("hc-21", log=None))','fp21 = pd.DataFrame(_fp)')
open('nb_dev.py','w').write(s)
EOF
python build_nb.py nb_dev.py entries/wirth-2017/dev.ipynb && cd entries/wirth-2017 && python - <<'EOF'
import nbformat
from nbclient import NotebookClient
nb=nbformat.read('dev.ipynb',4)
try:
    NotebookClient(nb,timeout=1200,kernel_name='python3',allow_errors=True,resources={'metadata':{'path':'.'}}).execute()
finally:
    nbformat.write(nb,'/tmp/claude-1001/dev_out.ipynb')
for c in nb.cells:
    if c.cell_type=='code':
        for o in c.get('outputs',[]):
            if o.output_type=='stream': print(o.text[:6000])
            elif o.output_type=='error': print('ERROR',o.ename,o.evalue)
            elif 'text/plain' in o.get('data',{}): print(o['data']['text/plain'][:3000])
        print('-----')
EOF
rm -f dev.ipynb
```

```
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
-----
hc-12 pass: 0 s, peak memory 0.21 GB

-----
hc-21 pass: 0 s, 101 files

-----
Files by monkey (ke = monkey K, sn = monkey S):
        files  with_new_maze  sessions
monkey                                
ke         99             99        41
sn         90             88        26

Files without a new-maze (newallo) field: ['sn20121015_HPC_e2_c1a_seg.mat', 'sn20121015_HPC_e2_c1c_seg.mat']

Spike times taken from: {'file.elec': 175, 'newallo.elec': 12}
Top-level field sets: 7 different layouts
Camera frame interval (ms): {'min': 16.667, 'max': 16.667}
Eye sample interval (ms): {'min': 5.0, 'max': 5.0} ; files without eye data: 8
[... 334 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd entries/wirth-2017 && python - <<'EOF'
s=open('wirth.py').read()
old='''def landmark_tables(c, s, sess):'''
new='''def landmark_tables(c, s, sess, laps="successful"):'''
s=s.replace(old,new)
old='''    t60 = c["t60"]
    trial, ok = sess.tables["full"]
    tag = sess.tag
    ab = t60[:, 4]
    rows = []
    ent = sess.entry & np.isfinite(ab)'''
new='''    t60 = c["t60"]
    trial, ok = sess.tables["full"]
    if laps == "all":  # every trial, rewarded or not
        ok = trial >= 0
    tag = sess.tag
    ab = t60[:, 4]
    entry = ok & (tag >= 100) & (tag < 200)
    center = ok & (tag >= 200) & (tag < 400)
    ent = entry & np.isfinite(ab)'''
assert old in s; s=s.replace(old,new)
s=s.replace('''    for x in np.unique(tag[sess.entry] % 100).astype(int):
        mm = sess.entry & (tag % 100 == x)''','''    for x in np.unique(tag[entry] % 100).astype(int):
        mm = entry & (tag % 100 == x)''')
s=s.replace('''        mm = sess.center & (d <= SSI_BIN_DEG / 2)''','''        mm = center & (d <= SSI_BIN_DEG / 2)''')
old='''        out["n_laps"] = int(two.trial.nunique())'''
new='''        out["n_laps"] = int(two.trial.nunique())
        two, onea, oneb, _ = landmark_tables(c, s, sess, laps="all")
        a2 = anova_two(two) or {}
        out.update({f"lm2all_{k}": v for k, v in a2.items()})
        out["lm1aall_p"], _ = anova_one(onea)
        out["lm1ball_p"], _ = anova_one(oneb)
        out["n_laps_all"] = int(two.trial.nunique())'''
assert old in s; s=s.replace(old,new)
open('wirth.py','w').write(s)
EOF
grep -n "sess.entry\|sess.center" wirth.py
```

```
Fri Nov 13 12:53:34 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF' 2>&1 | grep -v Warn
import sys; sys.path.insert(0,'entries/wirth-2017')
import wirth, numpy as np
n=0
for name,d in wirth.stream_members('hc-12'):
    if not name.startswith('sn20110624'): continue
    c=wirth.reduce_file(name,d); sess=wirth.Session(c); s=wirth.spike_counts(c)
    for laps in ('successful','all'):
        two,onea,oneb,h=wirth.landmark_tables(c,s,sess,laps)
        print(name, laps, wirth.anova_two(two), two.trial.nunique())
    n+=1
    if n==3: break
EOF
date -u
```

```
seg = np.clip(np.floor((1 - np.nan_to_num(ab)) * 4).astype(int), 0, 3)
  seg = np.clip(np.floor((1 - np.nan_to_num(ab)) * 4).astype(int), 0, 3)
  seg = np.clip(np.floor((1 - np.nan_to_num(ab)) * 4).astype(int), 0, 3)
  seg = np.clip(np.floor((1 - np.nan_to_num(ab)) * 4).astype(int), 0, 3)
  seg = np.clip(np.floor((1 - np.nan_to_num(ab)) * 4).astype(int), 0, 3)
  seg = np.clip(np.floor((1 - np.nan_to_num(ab)) * 4).astype(int), 0, 3)
  seg = np.clip(np.floor((1 - np.nan_to_num(ab)) * 4).astype(int), 0, 3)
  seg = np.clip(np.floor((1 - np.nan_to_num(ab)) * 4).astype(int), 0, 3)
  seg = np.clip(np.floor((1 - np.nan_to_num(ab)) * 4).astype(int), 0, 3)
  seg = np.clip(np.floor((1 - np.nan_to_num(ab)) * 4).astype(int), 0, 3)
  seg = np.clip(np.floor((1 - np.nan_to_num(ab)) * 4).astype(int), 0, 3)
  seg = np.clip(np.floor((1 - np.nan_to_num(ab)) * 4).astype(int), 0, 3)
sn20110624_e1_HPC_c1_seg.mat successful {'p_lm': np.float64(0.12089765648281192), 'p_rd': np.float64(0.5875469289594154), 'p_int': np.float64(0.41252276880721855), 'F_int': np.float64(1.0322259524601833), 'df_int': np.float64(9.0), 'df_res': np.float64(596.0), 'n_lm': 4} 153
sn20110624_e1_HPC_c1_seg.mat all {'p_lm': np.float64(0.06737634482839427), 'p_rd': np.float64(0.7948276479953686), 'p_int': np.float64(0.0603254602558946), 'F_int': np.float64(1.8255254606955147), 'df_int': np.float64(9.0), 'df_res': np.float64(756.0), 'n_lm': 4} 193
sn20110624_e1_HPC_c2_seg.mat successful {'p_lm': np.float64(0.0025234562788594146), 'p_rd': np.float64(0.7838662691325158), 'p_int': np.float64(0.07816982859574813), 'F_int': np.float64(1.7341353775229407), 'df_int': np.float64(9.0), 'df_res': np.float64(596.0), 'n_lm': 4} 153
sn20110624_e1_HPC_c2_seg.mat all {'p_lm': np.float64(4.54990336337943e-05), 'p_rd': np.float64(0.22579400466678398), 'p_int': np.float64(0.0008481515151970631), 'F_int': np.float64(3.1896211026134007), 'df_int': np.float64(9.0), 'df_res': np.float64(756.0), 'n_lm': 4} 193
sn20110624_e1_HPC_c3_seg.mat su
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('nb_src.py').read()
s=s.replace('"median corr": round(d.corr.median(), 3)','"median corr": round(d["corr"].median(), 3)')
old='''def lm_counts(d):
    a = 0.05
    lmk, rd, it = d.lm2_p_lm < a, d.lm2_p_rd < a, d.lm2_p_int < a
    return {"n": len(d), "identity": int(lmk.sum()), "distance": int(rd.sum()), "interaction": int(it.sum()),
            "both, no interaction (a)": int((lmk & rd & ~it).sum()), "both (b)": int((lmk & rd).sum()),
            "centre one-way (a)": int((d.lm1a_p < a).sum()), "centre one-way (b)": int((d.lm1b_p < a).sum())}


rows = []
for r, sr in READINGS:
    resp3 = sum(sig(k, r, sr).astype(int) for k in SPACES) > 0
    rows.append({"responsive set": f"three-space {r}/{sr}", **lm_counts(C[resp3])})
rows.append({"responsive set": "all cells", **lm_counts(C)})
LM = pd.DataFrame(rows)
print("Entry paths per cell:", C.lm2_n_lm.value_counts().to_dict(), "; laps per cell, median:", C.n_laps.median())
print("Residual df of the two-way ANOVA, median:", C.lm2_df_res.median(), "(paper's example cells: 756)")'''
new='''def lm_counts(d, laps):
    a = 0.05
    k2, k1 = ("lm2", "lm1") if laps == "successful" else ("lm2all", "lm1")
    lmk, rd, it = d[f"{k2}_p_lm"] < a, d[f"{k2}_p_rd"] < a, d[f"{k2}_p_int"] < a
    ca, cb = ("lm1a_p", "lm1b_p") if laps == "successful" else ("lm1aall_p", "lm1ball_p")
    return {"laps": laps, "n": len(d), "identity": int(lmk.sum()), "distance": int(rd.sum()), "interaction": int(it.sum()),
            "both, no interaction (a)": int((lmk & rd & ~it).sum()), "both (b)": int((lmk & rd).sum()),
            "centre one-way (a)": int((d[ca] < a).sum()), "centre one-way (b)": int((d[cb] < a).sum())}


rows = []
for laps in ("successful", "all"):
    for r, sr in READINGS:
        resp3 = sum(sig(k, r, sr).astype(int) for k in SPACES) > 0
        rows.append({"responsive set": f"three-space {r}/{sr}", **lm_counts(C[resp3], laps)})
    rows.append({"responsive set": "all cells", **lm_counts(C, laps)})
LM = pd.DataFrame(rows)
print("Entry paths per cell:", C.lm2_n_lm.value_counts().to_dict(), "; laps per cell, median: successful", C.n_laps.median(),
      ", all", C.n_laps_all.median())
print("Residual df of the two-way ANOVA, median: successful laps", C.lm2_df_res.median(), ", all laps", C.lm2all_df_res.median())
ex = C[C.session == "sn20110624"][["name", "n_trials", "lm2_df_res", "lm2all_df_res", "lm2all_F_int", "lm2all_p_int"]]
print("\\nThe session with 193 trials, whose residual df with all laps is 193 x 4 - 16 = 756, as in Fig 5:")
print(ex.round(4).to_string())'''
assert old in s; s=s.replace(old,new)
old='''# %% [markdown]
# ## landmark-identity-distance and landmark-identity-center'''
assert old in s
s=s.replace('''fx = C[["name", "session", "lm2_F_int", "lm2_p_int", "lm2_df_int", "lm2_df_res"]].copy()
fx["dist"] = np.minimum(abs(fx.lm2_F_int - 4.4076), abs(fx.lm2_F_int - 2.1243))''','''fx = C[["name", "session", "lm2all_F_int", "lm2all_p_int", "lm2all_df_int", "lm2all_df_res"]].copy()
fx["dist"] = np.minimum(abs(fx.lm2all_F_int - 4.4076), abs(fx.lm2all_F_int - 2.1243))''')
s=s.replace('''print("\\nCells whose interaction F comes nearest the Fig 5 values (4.41 and 2.12):")''','''print("\\nCells whose interaction F (all laps) comes nearest the Fig 5 values (4.41 and 2.12):")''')
open('nb_src.py','w').write(s)
EOF
grep -n "Fig 5 values" $TMPDIR/nb_src.py
```

```
604:print("\nCells whose interaction F (all laps) comes nearest the Fig 5 values (4.41 and 2.12):")
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('nb_src.py').read()
old='''# %%
def lm_counts(d, laps):'''
new='''# %% [markdown]
# Which laps enter is read two ways. Method W takes successful trials only; the Methods' ANOVA
# section says "firing rates were collected for each of the animal's laps on each of the four
# entry paths", and Fig 5 reports F(9,756) for two cells recorded together. In hc-12 only one
# session gives 756 residual degrees of freedom: sn20110624, with 193 trials, when every lap is
# used (193 x 4 - 16 = 756; printed below). Both readings are run. Counts over the
# three-space responsive cells and over all cells bound the count over the paper's responsive
# set, as above.

# %%
def lm_counts(d, laps):'''
assert old in s; s=s.replace(old,new); open('nb_src.py','w').write(s)
EOF
cd  && sed -n 1,200p tools/entry.py | grep -n "def \|python\|requirements" | head -40; ls schemas
```

```
3:    python tools/entry.py lock  entries/<name>   # pin the environment
4:    python tools/entry.py check entries/<name>   # validate metadata and conventions
5:    python tools/entry.py check entries/*/       # the same for every entry, in one process
6:    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
7:    python tools/entry.py all   entries/<name>   # check, then run
8:    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies
10:`lock` compiles the entry's requirements.in (direct dependencies only) into
11:requirements.lock.txt with every version pinned.
19:- the lock file is present and newer requirements are not left unlocked;
77:    def __init__(self):
80:    def error(self, where, message: str) -> None:
85:def dataset_id(record: dict) -> str | None:
94:def dataset_ids(record: dict) -> list[str]:
99:def claims_paths() -> list[Path]:
105:def claims_target(data: dict) -> tuple:
110:def lookup(index: dict, attempt: dict):
119:def schema(name: str) -> Draft202012Validator:
130:def _parsed(text: str):
138:def _schema_errors(text: str, schema_name: str) -> tuple[str, ...]:
144:def load(report: Report, path: Path):
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 179,330p tools/entry.py
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

[... 133 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "_derivation_checks" -A40 tools/entry.py | sed -n 1,60p | grep -v "^--$" | head -60
```

```
246:        _derivation_checks(report, rel / name, code)
247-    for name in helpers:
248-        if (entry_dir / name).is_file():
249:            _derivation_checks(report, rel / name, (entry_dir / name).read_text())
250-
251-    # Claims and attempts that go with this entry.
252-    claims_by_target, labels_used, kinds_by_target, claims_checked = {}, {}, {}, {}
253-    for path in claims_paths():
254-        data = validate(report, path, "claims") or {}
255-        ids = {c["id"] for c in data.get("claims", [])}
256-        claims_by_target[claims_target(data)] = ids
257-        claims_checked[claims_target(data)] = max((str(c.get("date") or "") for c in data.get("checks") or []),
258-                                                  default="")
259-        kinds_by_target[claims_target(data)] = {
260-            c["id"]: c.get("data", "dataset") for c in data.get("claims", [])}
261-        labels_used[claims_target(data)] = any(
262-            c.get("data") == "with_labels" for c in data.get("claims", []))
263-        for c in data.get("claims", []):
264-            for other in c.get("depends_on", []):
265-                if other not in ids:
[... 39 more lines not kept]
```

**Agent**

Now the entry files.

**Agent calls Bash**

```bash
cd entries/wirth-2017 && python - <<'EOF'
s=open('wirth.py').read()
s=s.replace('''MD5 = {"hc-12"''','''VERSION = "unversioned"       # CRCNS data sets are not versioned (docs/archives.md)
MD5 = {"hc-12"''')
open('wirth.py','w').write(s)
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: wirth-2017
type: reproduction
title: Space in the macaque hippocampus during virtual navigation (Wirth et al. 2017)
description: Tests the findings of Wirth, Baraduc, Plante, Pinede and Duhamel (2017) on CRCNS hc-12,
  which holds 189 hippocampal cells of two macaques navigating a virtual star maze with eye tracking,
  and uses CRCNS hc-21 to check which of its recordings are also in hc-12. It covers learning, gaze
  before turns and on passive returns, information content in position, direction and state space,
  centre and return direction maps, state-space selectivity and the landmark ANOVAs. The point-of-gaze
  analyses need a calibration of the eye signal that the files do not give.
license: Apache-2.0
notebooks:
- path: reproduce_wirth_2017.ipynb
  title: Reproducing Wirth et al. (2017) from CRCNS hc-12
  runtime_minutes: 30
helpers:
- wirth.py
related:
- id: crcns:hc-12/unversioned
  relation: uses_data
- id: crcns:hc-21/unversioned
  relation: uses_data
- id: doi:10.1371/journal.pbio.2001045
  relation: reproduces
EOF
printf "aiohttp\nfsspec\nipykernel\nnumpy\npandas\nrequests\nscipy\nstatsmodels\n" > requirements.in
cd  && python $TMPDIR/build_nb.py $TMPDIR/nb_src.py entries/wirth-2017/reproduce_wirth_2017.ipynb && python tools/entry.py lock entries/wirth-2017 2>&1 | tail -3 && python tools/entry.py check entries/wirth-2017 2>&1 | tail -15
```

```
wrote wirth-2017/requirements.lock.txt (Python 3.13, with hashes)
0 error(s)
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='/tmp/claude-1001/nb_src.py'; s=open(p).read()
s=s.replace('''tag_arm = []
for b in beh.values():
    pass
''','')
open(p,'w').write(s)
p='entries/wirth-2017/wirth.py'; s=open(p).read()
s=s.replace('''  (descriptor, transition tags). Entry paths: tags 10x, x = start arm code - 39 (shown in the
  notebook from the files).''','''  (descriptor, transition tags). Entry paths: tags 10x, the path x being the landmark identity.''')
open(p,'w').write(s)
EOF
python $TMPDIR/build_nb.py $TMPDIR/nb_src.py entries/wirth-2017/reproduce_wirth_2017.ipynb && date -u && time python tools/entry.py all entries/wirth-2017 2>&1 | tail -15; date -u
```

```
Fri Nov 13 12:57:31 UTC 2026
Installed kernelspec registry-wirth-2017 in executed/wirth-2017/.venv/share/jupyter/kernels/registry-wirth-2017
0 error(s)
pass  reproduce_wirth_2017.ipynb  (1231 s)

real	20m40.188s
user	12m46.418s
sys	1m37.575s
Fri Nov 13 13:18:11 UTC 2026
```

**Agent calls Bash**

```bash
ls executed/wirth-2017/ && python - <<'EOF'
import nbformat
nb=nbformat.read('executed/wirth-2017/reproduce_wirth_2017.ipynb',4)
skip=0
for i,c in enumerate(nb.cells):
    if c.cell_type=='code':
        for o in c.get('outputs',[]):
            t=o.get('text') or o.get('data',{}).get('text/plain','')
            if o.output_type=='error': t='ERROR '+o.ename+' '+o.evalue
            print(i, t[:2500])
EOF
```

```
reproduce_wirth_2017.ipynb
result.json
3 hc-12 pass: 1045 s, peak memory 0.96 GB

4 hc-21 pass: 178 s, 101 files

6 Files by monkey (ke = monkey K, sn = monkey S):
        files  with_new_maze  sessions
monkey                                
ke         99             99        41
sn         90             88        26

Files without a new-maze (newallo) field: ['sn20121015_HPC_e2_c1a_seg.mat', 'sn20121015_HPC_e2_c1c_seg.mat']

Spike times taken from: {'file.elec': 175, 'newallo.elec': 12}
Top-level field sets: 7 different layouts
Camera frame interval (ms): {'min': 16.667, 'max': 16.667}
Eye sample interval (ms): {'min': 5.0, 'max': 5.0} ; files without eye data: 8
Spike times sorted in every file: True

[... 275 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; grep -n "Result: \.\.\.\|## Summary\|Filled in after" $TMPDIR/nb_src.py
```

```
Fri Nov 13 13:18:59 UTC 2026
228:# **Result: ...**
240:# **Result: ...**
272:# **Result: ...**
340:# **Result: ...**
370:# **Result: ...**
423:# **Result: ...**
454:# **Result: ...**
485:# **Result: ...**
522:# **Result: ...**
529:# **Result: ...**
558:# **Result: ...**
614:# **Result: ...**
622:# **Result: ...**
643:# ## Summary
645:# Filled in after the run.
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('nb_src.py').read()
R=[
# learning-trials
"""**Result: reproduced.** Under reading (a) monkey S reaches criterion after 12.26 +- 3.28 trials
# (mean +- SEM, 23 sessions) and monkey K after 16.53 +- 2.69 (38 sessions), both within the
# paper's 12.3 +- 2 and 14.8 +- 2.4. Without the probe sessions (b) monkey K gives 15.82 +- 3.44,
# also within. Two sessions of S and three of K never reach the criterion and are left out. The
# SEMs here are larger than the paper's.""",
# learning-to-90
"""**Result: reproduced.** Of the 59 sessions that reach both criteria, 53 need fewer than 10
# trials (0.898, expected 0.89 +- 0.089); counted over all 66 sessions the fraction is 0.803, also
# inside the tolerance (0.801 to 0.979). Without the probe sessions the fractions are 0.898 and
# 0.815.""",
# probe-transfer
"""**Result: not reproduced.** hc-12 holds 12 probe sessions of monkey K (the paper has 15) and
# none of monkey S (the paper has 9); hc-21 adds no other. For K, performance is 28.3% over the
# first 5 trials and 58.3% over the 5 trials after the new entries, both below the paper's 44% and
# 73% by more than the tolerance, and the Wilcoxon signed-rank test gives p = 0.072. The direction
# of the effect is the paper's (median gain 0.30).""",
# gaze-anticipates-action
"""**Result: reproduced, resting on the assumed sign of the eye signal.** Before right turns the
# horizontal eye signal lies on the negative side of that before left turns in each monkey, in
# both windows, for each eye and both eyes, with rank-sum p below 1e-100 (500 ms, both eyes,
# successful trials: K median difference -0.77 session SD, p = 4.0e-148; S -1.00, p = 4.3e-146),
# and in 39 of 40 sessions of K and 20 of 20 of S. Taking negative as rightward (the profile
# after the turn grows in the same direction), gaze is on the side of the coming turn.""",
# gaze-anticipates-landmarks
"""**Result: reproduced, resting on the assumed sign of the eye signal.** During passive returns
# that turn right the eye signal lies on the negative (rightward, as assumed above) side of that
# during returns that turn left, in each monkey (all returns, both eyes: K -0.56 session SD,
# p = 6.2e-58, 39 of 41 sessions; S -0.56, p = 6.4e-30, 20 of 21 sessions), and after successful
# trials only (p = 4.7e-34 and 1.5e-10).""",
# state-space-most-responsive
"""**Result: not reproduced.** The state-space count is 57 of 186 cells under the main reading
# (full trials, permuted chunks) and 33, 42 and 24 under the others, all below the expected
# 75.6 to 92.4. The count needs no gaze, so the missing gaze space does not change this; the
# chi-squared tests across the four spaces could not be run. State space is still the space with
# the most significant cells of the three computed here (57 against 46 and 40).""",
# direction-center-vs-periphery
"""**Result: not reproduced.** For the 40 direction-selective cells (reading a, permuted chunks)
# normalized sparsity is higher in the centre (median difference 0.020, p = 0.031) but IC is not
# (0.012, p = 0.43), so neither p < 0.001 nor both p < 0.05 holds. Over the 59 cells responsive in
# the three spaces computed here, a stand-in for reading (b), both are higher with p = 0.045 and
# 0.0074, the criterion's partial level; with shifted chunks no comparison is significant.""",
# direction-tuning-not-maintained
"""**Result: partially reproduced.** Among the 40 direction-selective cells, 15 have a
# significantly low centre-return correlation (38%, binomial p = 2.1e-14 at chance 0.025) and 4 a
# significantly high one (p = 0.017). The proportion of low cells is the paper's (36%), and the
# high count is inside 2 to 4, but 40 cells are tested (expected 56 +- 5.6) and the low count of
# 15 is outside 20 +- 2. Over the 59 three-space responsive cells, 16 are low and 4 high. The
# minimum of common bins (10 or 2) changes nothing; with shifted chunks 5 of 24 are low.""",
# sparsity-state-vs-direction
"""**Result: reproduced under the main reading only.** For the 40 cells significant in both
# state and direction space (full trials, permuted chunks), normalized sparsity is higher in state
# space (median difference 0.016, 28 of 40 cells, Wilcoxon p = 0.0022). Under the other three
# readings it is not significant (p = 0.32, 0.92, 0.36).""",
# sparsity-state-vs-position
"""**Result: not reproduced.** Under the main reading state space is significantly sparser than
# position space overall (median difference 0.016, p = 0.00043), where the paper finds no
# significant difference; 9 (level 0.05) or 5 (level 0.01) cells differ individually, against
# 15 +- 1.5. Under the readings where the overall test is not significant (shifted chunks), only
# 2 or 6 cells differ individually. No reading meets all three parts.""",
# state-space-selectivity
"""**Result: not reproduced.** The paper's responsive set contains the three-space responsive
# cells and is contained in all cells, so its counts lie between the two printed rows. Under the
# main reading the high count lies between 15 and 23, above 11 to 13; with shifted chunks it lies
# between 3 and 8, below. Under trials to reward with permuted chunks the high count (13 to 23)
# could reach 13, but the low count lies between 7 and 12, above the 3 to 5 the criterion
# allows. No reading can meet the criterion.""",
# landmark-identity-distance
"""**Result: not reproduced.** With successful laps, at most 24 cells (all 186 cells) show a main
# effect of relative distance, and at most 31 with all laps, against 64 +- 6.4; this bound holds
# for any responsive set. The identity count lies between 16 and 32 (successful laps) or 24 and 47
# (all laps), which allows 30, and the interaction count between 6 and 14 or 8 and 17, but the
# distance count fails under every reading, and with it the partial level. All laps give the
# paper's residual df of 756 in the one session of 193 trials; none of its three cells has the
# Fig 5 F values (1.83, 3.19, 1.56 against 4.41 and 2.12).""",
# landmark-identity-center
"""**Result: blocked (metadata insufficient).** Over the three-space responsive cells and over all
# cells the one-way count lies between 9 and 16 (reading a) or 11 and 23 (reading b) with
# successful laps, and between 8 and 18 or 12 and 26 with all laps, so it may or may not fall in
# 11 to 13, and the binomial test depends on the size of the responsive set. Without the
# point-of-gaze space the paper's responsive set cannot be formed, and the claim cannot be
# decided.""",
]
parts=s.split("# **Result: ...**")
assert len(parts)==len(R)+1, len(parts)
out=parts[0]
for r,p in zip(R,parts[1:]): out+="# "+r+p
s=out
s=s.replace('print(LM[["responsive set", "n", "centre one-way (a)", "centre one-way (b)"]].to_string())','print(LM[["responsive set", "laps", "n", "centre one-way (a)", "centre one-way (b)"]].to_string())')
summary='''# ## Summary
#
# | Claim | Outcome |
# |---|---|
# | gaze-anticipates-action | reproduced (assumed sign of the eye signal) |
# | gaze-anticipates-landmarks | reproduced (assumed sign of the eye signal) |
# | learning-trials | reproduced |
# | learning-to-90 | reproduced |
# | probe-transfer | not reproduced (monkey K only; no probe session of S in hc-12) |
# | probe-faster-criterion | blocked: methods underspecified |
# | cells-recorded | partially reproduced (only the 189 analysed cells are deposited) |
# | responsive-cells | blocked: metadata insufficient (no gaze calibration) |
# | state-space-most-responsive | not reproduced |
# | multi-space-coding | blocked: metadata insufficient |
# | direction-center-vs-periphery | not reproduced |
# | direction-tuning-not-maintained | partially reproduced |
# | state-space-ic-higher | blocked: metadata insufficient |
# | sparsity-state-vs-direction | reproduced (main reading only) |
# | sparsity-state-vs-position | not reproduced |
# | sparsity-gaze-vs-state | blocked: metadata insufficient |
# | state-space-selectivity | not reproduced |
# | landmark-identity-distance | not reproduced |
# | landmark-identity-center | blocked: metadata insufficient |
# | path-selectivity, gaze-aligned-dynamics, latency-skew, eccentricity-modulation, foveation-selectivity, gaze-map-landmarks | blocked: metadata insufficient |
# | fields-per-cell, dimensionality-control | blocked: methods underspecified |
# | spatial-selectivity-fraction | blocked: metadata insufficient |
#
# A failure to reproduce here may be a failure of this attempt, not of the paper: see the
# reasoning and the differences from the paper's method.
#
# How the analysis differs from the paper's. The point-of-gaze space is missing, as the eye
# signal has no calibration, so the responsive set of the paper cannot be formed; counts over it
# are bounded by counts over the three-space responsive cells and over all cells. The map
# resolution steps, the surrogate shifting (two readings), the trial windows (two readings), the
# move types of the state-space selectivity, the per-session standardization of the eye signal and
# its sign are choices the paper does not fix. The learning-curve method of the paper's reference
# 60 is not known, so curves were not recomputed.
#
# What was found about the data. The learning curves' columns are probability, lower and upper
# bound, not the order the descriptor gives; eye samples are 200 Hz, not 250 Hz; the eye signal
# is on two different scales with no units or calibration; the rewarded arm is not always code 53;
# two hc-12 files have no new-maze data; 87 of the 101 hc-21 files hold the same spike trains as
# hc-12 files; hc-12 holds 12 of monkey K's 15 probe sessions and none of monkey S's 9.'''
s=s.replace('''# ## Summary
#
# Filled in after the run.''',summary)
open('nb_src.py','w').write(s)
EOF
grep -c "Result:" $TMPDIR/nb_src.py
```

```
13
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('nb_src.py').read()
old='''      "the files give no subfield (CA3, CA1, dentate gyrus).")
'''
new='''      "the files give no subfield (CA3, CA1, dentate gyrus).")

# %% [markdown]
# **Result: partially reproduced.** hc-12 holds 189 cell files (99 of monkey K, 90 of monkey S),
# the paper's analysed count; 187 have new-maze data and 186 of them fire more than 100 spikes in
# the new-maze session (expected 189 +- 18.9). The 270 cells recorded (128 S, 142 K) are not all
# deposited: only the 189 are, so that count cannot be checked here.
'''
assert old in s; s=s.replace(old,new,1); open('nb_src.py','w').write(s)
EOF
cd  && python $TMPDIR/build_nb.py $TMPDIR/nb_src.py entries/wirth-2017/reproduce_wirth_2017.ipynb && date -u
```

```
Fri Nov 13 13:19:41 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/wirth-2017 && python - <<'EOF'
s=open('wirth.py').read()
old='''        for a, b in zip(brk[::2], brk[1::2]):
            tot = dth[a + 1:b].sum() if b - a > 1 else 0.0
            same = np.ones(b - a, bool)
            # split runs where the tag value changes
            vals = tag[a:b]
            for v in np.unique(vals):
                idx = np.arange(a, b)[vals == v]
                tv = dth[idx[1:]].sum() if len(idx) > 1 else tot
                out[idx] = 1 if tv < 0 else 2'''
new='''        for a, b in zip(brk[::2], brk[1::2]):
            vals = tag[a:b]
            for v in np.unique(vals):  # one run per tag value
                idx = np.arange(a, b)[vals == v]
                out[idx] = 1 if dth[idx[1:]].sum() < 0 else 2'''
assert old in s; s=s.replace(old,new); open('wirth.py','w').write(s)
EOF
cat > README.md <<'EOF'
# Wirth, Baraduc, Plante, Pinede & Duhamel (2017) from CRCNS hc-12

Tests the findings of [Wirth et al. (2017)](https://doi.org/10.1371/journal.pbio.2001045) that can be
tested on [CRCNS hc-12](https://doi.org/10.6080/K0R49NQV), which holds the 189 analysed hippocampal
cells of two macaques navigating a virtual star maze, with eye tracking. [CRCNS
hc-21](https://doi.org/10.6080/K0GX48R9) is read to check which of its recordings are also in hc-12.

| Claim | Outcome |
|---|---|
| Gaze anticipates the turn, and the side where landmarks will appear | Reproduced (sign of the eye signal assumed) |
| Learning in about a dozen trials; fewer than 10 more trials to 90% | Reproduced |
| Performance after new entries in probe sessions | Not reproduced (monkey K only) |
| Faster learning after new entries | Blocked: methods underspecified |
| 189 cells analysed of 270 recorded | Partially reproduced |
| State space has the most responsive cells (84) | Not reproduced |
| Direction maps: centre against return paths | IC and sparsity not reproduced; low correlations partially reproduced |
| Sparser in state space than in direction space | Reproduced (main reading) |
| Sparsity, state against position space | Not reproduced |
| State-space selectivity in the centre | Not reproduced |
| Landmark identity and distance (two-way ANOVA) | Not reproduced |
| Claims that need the point-of-gaze space or the paper's responsive set (12 claims) | Blocked: metadata insufficient |
| Number of fields, control for dimensionality | Blocked: methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The eye signal has no calibration, units or sign in the files, so the paper's point-of-gaze maps
cannot be built. The attempt record, with the reasons and the differences from the paper's
method, is [`attempts/wirth-2017-01.yaml`](../../attempts/wirth-2017-01.yaml).
EOF
cd  && date -u && python tools/entry.py all entries/wirth-2017 2>&1 | tail -4; date -u
```

```
Fri Nov 13 13:19:54 UTC 2026
Installed kernelspec registry-wirth-2017 in executed/wirth-2017/.venv/share/jupyter/kernels/registry-wirth-2017
0 error(s)
pass  reproduce_wirth_2017.ipynb  (1178 s)
Fri Nov 13 13:39:41 UTC 2026
```

**Agent calls Bash**

```bash
python - <<'EOF'
import nbformat
nb=nbformat.read('executed/wirth-2017/reproduce_wirth_2017.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type=='code' and any(t.startswith('claim:') for t in c.metadata.get('tags',[])):
        t=''.join((o.get('text') or o.get('data',{}).get('text/plain','')) for o in c.get('outputs',[]))
        print(c.metadata['tags'], t[:900].replace('\n\n','\n'))
EOF
```

```
['claim:cells-recorded']         files  with_new_maze  over_100_spikes
monkey                                       
ke         99             99               98
sn         90             88               88
total     189            187              186
Recording locations (AP, ML, DV relative to the interaural line) present in 187 files; the files give no subfield (CA3, CA1, dentate gyrus).

['claim:learning-trials'] (a) all sessions
         mean   sem  sessions_reaching  sessions_never  median
monkey                                                        
ke      16.53  2.69                 38               3    11.0
sn      12.26  3.28                 23               2     6.0
(b) sessions that are not probe sessions
         mean   sem  sessions_reaching  sessions_never  median
monkey                                                        
ke      15.82  3.44                 28               1     8.5
sn      12.26  3.28                 23               2     6.0
Expected: monkey S (sn) 12.3 +- 2, monkey K (ke) 14.8 +- 2.4

['claim:learning-to-90'] (a) all sessions: sessions reaching both criteria 59 of 66; fewer than 10 trials from lower bound > 1/4 to upper bound >= 0.9: 53, fraction of sessions reaching 0.898, of all sessions 0.803
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; python -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s['required']));print(list(s['properties']));
o=s['properties']['outcomes']['items'];print(json.dumps(o.get('required')),list(o['properties']));
f=s['properties']['findings']['items'];print(json.dumps(f,indent=0)[:1500]);print(json.dumps(s['properties']['provenance'])[:1500]); print(json.dumps(s['properties']['datasets'])[:800]); print(json.dumps(s['properties'].get('missing_datasets'))[:400])"; sed -n '/^findings:/,$p' attempts/fouke-2025-01.yaml | head -40
```

```
Fri Nov 13 13:39:53 UTC 2026
["schema_version", "id", "datasets", "paper", "date", "provenance", "outcomes"]
['schema_version', 'id', 'datasets', 'missing_datasets', 'paper', 'date', 'entry', 'deprecated', 'provenance', 'outcomes', 'verifications', 'findings', 'reconciliation', 'inputs']
["claim", "outcome"] ['claim', 'outcome', 'blocked_by', 'notes', 'notebook', 'output', 'measured', 'deviations', 'assumed', 'proposed']
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
[... 76 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "attempts/wirth-2017-01.yaml",
 "content": "schema_version: 3\nid: wirth-2017-01\ndatasets:\n- archive: crcns\n  id: hc-21\n  version: unversioned\n  doi: 10.6080/K0GX48R9\n  relation: primary\n- archive: crcns\n  id: hc-12\n  version: unversioned\n  doi: 10.6080/K0R49NQV\n  relation: primary\npaper: doi:10.1371/journal.pbio.2001045\ndate: 2026-11-13\nentry: wirth-2017\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-15\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/43420118844\noutcomes:\n- claim: gaze-anticipates-action\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_wirth_2017.ipynb\n  output: claim:gaze-anticipates-action\n  notes: Before right turns (code 1) the horizontal eye signal, standardized within session, lies\n    on the negative side of that before left turns (code 2) in each monkey, in the 500 and the 300\n    ms windows, for each eye and both eyes, successful or all trials, with rank-sum p below 1e-100.\n    500 ms, both eyes, successful trials, K median difference -0.77 session SD (p = 4.0e-148, 39 of\n    40 sessions), S -1.00 (p = 4.3e-146, 20 of 20 sessions). Taking negative as rightward, gaze lies\n    on the side of the coming turn. Both monkeys, each window and the pooled test agree, so the\n    readings of the criterion give one outcome.\n  deviations:\n  - The eye signal has no calibration, units or sign in the files, and is on a +-5000 scale in 36\n    sessions and a +-5 scale in 26. Values are standardized within each session (minus the session\n    median, over its SD) before sessions are pooled; per-session differences are also counted.\n  - Assumed that a negative horizontal value is rightward. During a turn the mean eye position in\n    optokinetic stimulation shifts toward the side of the quick phases, the side the observer turns\n    to, and the right-minus-left difference grows in the negative direction from the turn code on\n    (to -1.4 session SD in S and -0.9 in K at 0.4 to 0.6 s). If the sign were the other way, gaze\n    before a turn would lie opposite the turn.\n  - S1 Appendix A2, which holds the paper's analysis, was not available; the test is the rank-sum\n    of the claims file.\n- claim: gaze-anticipates-landmarks\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_wirth_2017.ipynb\n  output: claim:gaze-anticipates-landmarks\n  notes: Passive returns (tags 5xy) turn right when the camera orientation falls over them, as it\n    does after code 1. During right-turning returns the standardized eye signal lies on the negative\n    side, rightward as assumed for gaze-anticipates-action, in each monkey (all returns, both eyes,\n    K -0.56 session SD, p = 6.2e-58, 39 of 41 sessions; S -0.56, p = 6.4e-30, 20 of 21 sessions)\n    and after successful trials only (p = 4.7e-34 and 1.5e-10).\n  deviations:\n  - The same standardization and assumed sign as gaze-anticipates-action.\n  - The side of a return is taken from the change of camera orientation over it (median absolute\n    change 102.5 degrees); the files do not say where the landmarks appear.\n- claim: learning-trials\n  outcome: reproduced\n  notebook: reproduce_wirth_2017.ipynb\n  output: claim:learning-trials\n  measured:\n  - 12.26\n  - 16.53\n  notes: Using the files' own learning curves, the first trial whose lower bound exceeds 1/4 is on\n    average 12.26 +- 3.28 (SEM, 23 sessions) for monkey S and 16.53 +- 2.69 (38 sessions) for monkey\n    K over all sessions (reading a), and 15.82 +- 3.44 for K without the probe sessions (reading b).\n    Both monkeys fall within the paper's SEMs under both readings. Two sessions of S and three of K\n    never reach the criterion and are left out. The field learningtrial of every session equals\n    this trial.\n  deviations:\n  - The curves are the files' own; the method of the paper's reference 60 is not named in the text\n    read. The columns are read as probability, lower and upper bound, as the values show, where the\n    descriptor puts the probability in the middle column.\n- claim: learning-to-90\n  outcome: reproduced\n  notebook: reproduce_wirth_2017.ipynb\n  output: claim:learning-to-90\n  measured: 0.898\n  notes: Of the 59 sessions that reach both the lower bound above 1/4 and the upper bound at 0.9, 53\n    need fewer than 10 trials between them (0.898). Over all 66 sessions the fraction is 0.803, also\n    within 0.89 +- 0.089, and without the probe sessions 0.898 and 0.815.\n  deviations:\n  - The denominator is not stated; the fraction is given over the sessions reaching both criteria\n    and over all sessions, and both match.\n- claim: probe-transfer\n  outcome: not_reproduced\n  notebook: reproduce_wirth_2017.ipynb\n  output: claim:probe-transfer\n  measured:\n  - 58.3\n  - 28.3\n  notes: hc-12 holds 12 probe sessions of monkey K (the paper reports 15) and none of monkey S (the\n    paper reports 9); the 8 probe-like sessions of hc-21 are among the 12. For K, 28.3% correct over\n    the first 5 trials and 58.3% over the 5 trials after the new entries, both below the paper's 44%\n    and 73% by more than the tolerance; Wilcoxon signed-rank over the 12 sessions p = 0.072 (median\n    gain 0.30). The two values of monkey S could not be computed; the criterion fails on K's values\n    alone.\n  deviations:\n  - Probe sessions are found from the start arms (the first 10 trials use one or two entries and\n    later ones others), as the files do not mark them. The introduction is the first trial from an\n    entry not used in the first 10 (S3C legend).\n  - The measured values are monkey K's, after and at the start; monkey S has no probe session in\n    the data.\n- claim: probe-faster-criterion\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notes: Counting trials to criterion from the introduction of the new entries needs learning\n    curves recomputed on part of the session, with the confidence bounds of the paper's reference\n    60, which the text read does not name (S3B legend, \"methods based on [60]\"). The files hold only\n    whole-session curves. Any other curve method would set the criterion differently. hc-12 also\n    holds no probe session of monkey S. The question is for the paper's authors (findings).\n- claim: cells-recorded\n  outcome: partially_reproduced\n  notebook: reproduce_wirth_2017.ipynb\n  output: claim:cells-recorded\n  measured:\n  - 189\n  - 186\n  notes: hc-12 holds 189 cell files (99 of monkey K, 90 of monkey S), the paper's analysed count; 187\n    have new-maze data and 186 fire more than 100 spikes in the new-maze session (within 189 +-\n    18.9). The 270 cells recorded (128 S, 142 K) are not deposited beyond these 189, so that count\n    cannot be checked. The files give recording coordinates but no subfield.\n- claim: responsive-cells\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: Responsiveness is defined over four spaces, one of them the point of gaze, which needs the\n    gaze direction in degrees; the eye signal has no calibration, units or sign in the files.\n    Responsive in the three spaces computed here are 59 of 186 cells (full trials, permuted chunks;\n    39, 55 and 32 under the other readings), a lower bound of the four-space count, which could lie\n    anywhere from 59 to 186.\n- claim: state-space-most-responsive\n  outcome: not_reproduced\n  notebook: reproduce_wirth_2017.ipynb\n  output: claim:state-space-most-responsive\n  measured: 57\n  notes: 57 of 186 cells have significant state-space IC under the main reading (full trials,\n    permuted chunks) and 33, 42 and 24 under the others, all below 75.6 to 92.4. With a one-sided\n    test at 0.01 the counts are 62, 34, 52 and 29. The count needs no gaze, so the missing gaze space\n    does not change the outcome; the chi-squared tests across the four spaces could not be run.\n    State space has the most cells of the three spaces computed (57 against 46 for position and 40\n    for direction).\n  deviations:\n  - Map resolution steps (square bins for position and state space, as in the dataset's scripts,\n    equal angular bins for direction) and the two readings each of the trial window and of the\n    surrogate shifting, as in the claims file (Method W).\n- claim: multi-space-coding\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: Depends on responsive-cells (the gaze space). Of the 59 cells responsive in the three\n    spaces computed, 46 are significant in two or more; cells responsive only in gaze space would\n    add to the denominator, so the fraction over the paper's set cannot be bounded above one half.\n- claim: direction-center-vs-periphery\n  outcome: not_reproduced\n  notebook: reproduce_wirth_2017.ipynb\n  output: claim:direction-center-vs-periphery\n  notes: For the 40 cells with significant direction IC (reading a, permuted chunks) normalized\n    sparsity is higher in the centre than on return paths (median difference 0.020, 25 of 40,\n    Wilcoxon p = 0.031) and IC is not (0.012, p = 0.43). Neither the reproduced level (both p <\n    0.001) nor the partial level (both p < 0.05, or one p < 0.001) is met. Over the 59 three-space\n    responsive cells, which stand in for reading (b), IC and sparsity are higher with p = 0.045 and\n    0.0074, the partial level; with shifted chunks no comparison is significant. The statement\n    speaks of direction-selective cells, which is reading (a).\n  deviations:\n  - Centre and return maps at one common angular resolution per session, chosen so the number of\n    bins valid in both is closest to 200 (median 151 centre and 157.5 return bins valid); the\n    paper does not say how the two maps were binned.\n  - Reading (b), all responsive cells, cannot be formed without the gaze space; the three-space\n    responsive cells are shown.\n- claim: direction-tuning-not-maintained\n  outcome: partially_reproduced\n  notebook: reproduce_wirth_2017.ipynb\n  output: claim:direction-tuning-not-maintained\n  measured:\n  - 15\n  - 40\n  - 4\n  notes: Of 40 direction-selective cells, 15 (38%) have a significantly low centre-return\n    correlation (binomial p = 2.1e-14 at chance 0.025) and 4 a significantly high one (p = 0.017).\n    The proportion of low cells matches the paper's 36% and the high count is inside 2 to 4, but the\n    number of cells tested (40, expected 56 +- 5.6) and the low count (15, expected 20 +- 2) are\n    outside the tolerance. Over the 59 three-space responsive cells 16 are low and 4 high. With\n    shifted chunks 5 of 24 are low and 3 high.\n  deviations:\n  - Cells with at least 10 common valid bins, a standard choice for \"enough\"; with 2 the counts do\n    not change.\n- claim: state-space-ic-higher\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: One of the three comparisons is with the point-of-gaze space, which cannot be built. The\n    other two hold under the main reading; normalized IC is higher in state space than in position\n    space (44 cells, median 0.014, Wilcoxon p = 1.1e-4) and than in direction space (40 cells,\n    median 0.021, p = 2.5e-7).\n- claim: sparsity-state-vs-direction\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_wirth_2017.ipynb\n  output: claim:sparsity-state-vs-direction\n  measured: 0.0022\n  notes: For the 40 cells with significant IC in both state and direction space (full trials,\n    permuted chunks), normalized sparsity is higher in state space (median difference 0.016, 28 of\n    40 cells, Wilcoxon p = 0.0022). Under the other three readings it is not significant (p = 0.32,\n    0.92 and 0.36), so the outcome rests on the main reading.\n  deviations:\n  - The main reading takes the trial window from start to next start (the state space includes the\n    returns, Fig 1F legend) and permutes the order of the 5 s chunks (Results, \"randomly shuffling\n    periods of spiking activity in time\"); the paper does not settle either, and the outcome\n    depends on them (findings).\n- claim: sparsity-state-vs-position\n  outcome: not_reproduced\n  notebook: reproduce_wirth_2017.ipynb\n  output: claim:sparsity-state-vs-position\n  measured: 9\n  notes: Under the main reading state space is significantly sparser than position space over the\n    44 cells responsive in both (median difference 0.016, Wilcoxon p = 0.00043), where the paper's\n    test finds no significant difference; 9 (per-cell level 0.05) or 5 (0.01) cells differ\n    individually, against 15 +- 1.5, and those 9 are sparser in state space (p = 0.0039). Under\n    shifted chunks the overall test is not significant (p = 0.31 and 0.17) but only 2 or 6 cells\n    differ individually. No reading meets all parts.\n- claim: sparsity-gaze-vs-state\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: Needs the point-of-gaze space; the eye signal has no calibration.\n- claim: state-space-selectivity\n  outcome: not_reproduced\n  notebook: reproduce_wirth_2017.ipynb\n  output: claim:state-space-selectivity\n  notes: The paper's responsive set contains the three-space responsive cells and lies within all\n    cells, so its counts are bounded by the counts over these two sets. Under the main reading the\n    high count lies between 15 and 23, above 11 to 13; with shifted chunks between 3 and 8, below.\n    With trials to reward and permuted chunks the high count lies between 13 and 23 and the low count\n    between 7 and 12, above the 3 to 5 the criterion allows. No reading can meet the criterion.\n  deviations:\n  - The three rotational moves are read as the 36 degree alignment (tags 2xy) and the 72 degree\n    rotations to the right and to the left (tags 3xy, split by the sign of the orientation change);\n    the paper does not name them. High and low are the upper and lower 5% of the surrogates, the\n    level implied by the binomial chance rate of the claims file.\n  - The paper's responsive set cannot be formed (gaze space); the outcome rests on the bounds.\n- claim: landmark-identity-distance\n  outcome: not_reproduced\n  notebook: reproduce_wirth_2017.ipynb\n  output: claim:landmark-identity-distance\n  notes: At most 24 cells (over all 186) show a main effect of relative distance with successful\n    laps, and at most 31 with all laps, against 64 +- 6.4; this bound holds for any responsive set.\n    The identity count lies between 16 and 32 (successful laps) or 24 and 47 (all laps) and the\n    interaction count between 6 and 14 or 8 and 17, but the distance count fails under every\n    reading, and with it the partial level. With all laps the one session of 193 trials\n    (sn20110624) gives the residual df of Fig 5, 756, and its three cells have interaction F of\n    1.83, 3.19 and 1.56, not the 4.41 and 2.12 of Fig 5.\n  deviations:\n  - Laps read two ways, successful trials (Method W) and all trials (Methods, \"each of the animal's\n    laps\"); the residual df of 756 in Fig 5 is reached only with all laps of sn20110624 (193 x 4 -\n    16), which supports the second.\n  - Relative distance from the files' curvilinear abscissa (0 centre, 1 arm end) in quarters; the\n    landmark identity is the entry path. Rates per lap and segment, ANOVA with interaction, type II\n    sums of squares, alpha 0.05.\n- claim: landmark-identity-center\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: Over the three-space responsive cells and over all cells the one-way count lies between 9\n    and 16 (reading a) or 11 and 23 (reading b) with successful laps, and between 8 and 18 or 12 and\n    26 with all laps (main reading of the responsive set), so it may or may not fall in 11 to 13, and\n    the binomial test depends on the size of the responsive set, which needs the gaze space.\n- claim: path-selectivity\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: Cells enter on significant point-of-gaze IC, and landmark entry into the field of view\n    needs the landmark positions, which the files do not give (only the arms' geometry is in the\n    camera data). The eye signal has no calibration.\n- claim: gaze-aligned-dynamics\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: Foveation is gaze within 10 degrees of a landmark, which needs the gaze in degrees and the\n    landmark positions; the files give neither.\n- claim: latency-skew\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: Depends on gaze-aligned-dynamics; the gaze-aligned latencies need foveation and the onset\n    latencies need the landmark positions.\n- claim: eccentricity-modulation\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: Depends on gaze-aligned-dynamics; landmark eccentricity needs calibrated gaze and the\n    landmark positions.\n- claim: foveation-selectivity\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: Depends on gaze-aligned-dynamics; needs foveation epochs and landmark onsets.\n- claim: fields-per-cell\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notes: The paper's text and legends do not define a positional field (S5B counts peaks); the\n    definition is presumably in S1 Appendix, which was not available. The question is for the\n    paper's authors (findings).\n- claim: spatial-selectivity-fraction\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: Under reading (a) 46 of 186 cells (0.247) have significant position IC, outside 0.5 +-\n    0.05. Readings (b) and (c) need the responsive set; responsive cells among all lie between 0.32\n    and 1, and position cells among responsive between 0.247 and 0.78, both of which include 0.5.\n- claim: gaze-map-landmarks\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: Needs point-of-gaze maps and the landmark positions; the eye signal has no calibration and\n    the files give no landmark positions.\n- claim: dimensionality-control\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notes: The control is described in S1 Appendix A5, which was not available; the S7 legend shows\n    only that spikes were simulated on the trajectory with a box-shaped field.\nfindings:\n- kind: metadata_insufficient\n  datasets:\n  - crcns-hc-12\n  - crcns-hc-21\n  statement: The horizontal and vertical eye signals have no units, calibration or sign convention.\n    They are on a +-5000 scale in 36 hc-12 sessions and a +-5 scale in 26, with saturated samples at\n    the bound (up to 22% of a session). The paper's point-of-gaze maps, foveation and landmark\n    eccentricity cannot be computed, which blocks 12 of the 28 claims; the files also give no\n    positions of the landmarks.\n- kind: metadata_error\n  datasets:\n  - crcns-hc-12\n  statement: The descriptor puts the probability of a correct response in the middle column of\n    learning_curves and the bounds in columns 1 and 3. In all 187 files column 2 is the lowest and\n    column 3 the highest, so the columns are probability, lower bound and upper bound. The field\n    learningtrial, not described, is the first trial whose lower bound exceeds 1/4 (-2 when none).\n- kind: metadata_error\n  datasets:\n  - crcns-hc-12\n  statement: The descriptor gives the eye positions at 250 Hz; eye_times are 5 ms apart (200 Hz) in\n    every file.\n- kind: metadata_error\n  datasets:\n  - crcns-hc-12\n  statement: The descriptor says code 43 is the rewarded start arm and code 53 the rewarded chosen\n    arm. The arm chosen on rewarded trials is 53 in 32 of 66 sessions and another arm in the rest,\n    as the reward moved each day.\n- kind: data_missing\n  datasets:\n  - crcns-hc-12\n  statement: Two hc-12 files (sn20121015_HPC_e2_c1a and c1c) have no new-maze (newallo) data, the\n    only maze the paper analyses, so 187 of the 189 cells can be analysed.\n- kind: data_missing\n  datasets:\n  - crcns-hc-12\n  - crcns-hc-21\n  statement: hc-12 holds 12 probe sessions of monkey K and none of monkey S, where the paper reports\n    15 and 9; hc-21 holds 8 probe-like sessions, all among K's 12.\n- kind: other\n  about: data\n  datasets:\n  - crcns-hc-12\n  - crcns-hc-21\n  statement: 87 of the 101 hc-21 files hold the same spike trains (same spike count and first spike\n    times) and trial tables as hc-12 files, under other file names. Neither descriptor says that the\n    two data sets overlap.\n- kind: other\n  about: data\n  datasets:\n  - crcns-hc-12\n  statement: The files come in seven layouts. The spike times are under file.elec in 175 files and\n    only under newallo.elec in 12; camera data are at the top level or under newallo; the camera\n    orientation runs from 0 to 360 in some files and -180 to 180 in others; the eye signal is a plain\n    array or a Spike2 channel structure. The descriptor gives one layout.\n- kind: methods_unavailable\n  statement: How were the 5 s chunks of recording \"randomly shifted\" for the surrogates (their order\n    permuted, or each moved by its own offset), and did the maps include the passive returns after\n    successful trials? Significant counts change two-fold between these readings (state space 57 or\n    33 of 186 cells with returns, 42 or 24 without), and sparsity-state-vs-direction holds only with\n    permuted chunks and returns.\n- kind: methods_unavailable\n  statement: Which learning-curve method is reference 60, and how were trials to criterion counted\n    after the new entries of probe sessions? The files hold only whole-session curves.\n- kind: methods_unavailable\n  statement: How is a positional field defined for the count of 2.7 fields per cell, and how was the\n    control for the dimensionality of the state space done (S1 Appendix A5)? S1 Appendix was not\n    available to this attempt.\n- kind: methods_unavailable\n  statement: Which three rotational moves enter the state-space selectivity index, and were the\n    two-way ANOVA's laps all trials or only successful ones? The residual df of 756 in Fig 5 fits all\n    193 laps of session sn20110624.\n"
}
```

```
File created successfully at: attempts/wirth-2017-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='attempts/wirth-2017-01.yaml'; s=open(p).read()
s=s.replace("""    (to -1.4 session SD in S and -0.9 in K at 0.4 to 0.6 s).""","""    (to -1.4 session SD in S at 0.3 to 0.6 s and -0.9 in K at 0.6 to 0.7 s).""")
s=s.replace("""  statement: 87 of the 101 hc-21 files hold the same spike trains (same spike count and first spike
    times) and trial tables as hc-12 files, under other file names.""","""  statement: 87 of the 101 hc-21 files hold the same spike trains (same spike count and first five
    spike times) as hc-12 files, under other file names.""")
s=s.replace("""    orientation runs from 0 to 360 in some files and -180 to 180 in others; the eye signal is a plain
    array or a Spike2 channel structure. The descriptor gives one layout.""","""    orientation runs from 0 to 360 in some files and -180 to 180 in others. The descriptor gives one
    layout.""")
open(p,'w').write(s)
EOF
grep -n ": " attempts/wirth-2017-01.yaml | grep -v "^[0-9]*:\s*-\? *[a-z_]*: " | head; python tools/entry.py check entries/wirth-2017 2>&1 | tail -10
```

```
0 error(s)
```

**Agent calls Bash**

```bash
python tools/entry.py handover entries/wirth-2017 2>&1 | tail -5; ls executed/wirth-2017/handover/; git status --short; date -u
```

```
wrote executed/wirth-2017/handover
reproduce_wirth_2017.ipynb
wirth-2017.yaml
wirth.py
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
?? attempts/wirth-2017-01.yaml
?? entries/wirth-2017/
?? scripts
Fri Nov 13 13:41:36 UTC 2026
```

**Agent calls Bash**

```bash
ls -la entries/wirth-2017; git check-ignore -v executed/wirth-2017 | head -2
```

```
total 260
drwxr-xr-x   4 runner runner   4096 Nov 13 13:19 .
drwxr-xr-x 285 runner runner  12288 Nov 13 12:15 ..
drwxr-xr-x   3 runner runner   4096 Nov 13 12:16 .claude
-rw-r--r--   1 runner runner   1972 Nov 13 13:19 README.md
drwxr-xr-x   2 runner runner   4096 Nov 13 13:20 __pycache__
-rw-r--r--   1 runner runner   1077 Nov 13 12:57 entry.yaml
-rw-r--r--   1 runner runner  56607 Nov 13 13:19 reproduce_wirth_2017.ipynb
-rw-r--r--   1 runner runner     65 Nov 13 12:57 requirements.in
-rw-r--r--   1 runner runner 131821 Nov 13 12:57 requirements.lock.txt
-rw-r--r--   1 runner runner  35787 Nov 13 13:19 wirth.py
.gitignore:6:executed/	executed/wirth-2017
```

**Agent calls Bash**

```bash
ls -la entries/wirth-2017/.claude entries/wirth-2017/.claude/*; git check-ignore -v entries/wirth-2017/__pycache__ entries/wirth-2017/.claude
```

```
ls: cannot access 'entries/wirth-2017/.claude/*': No such file or directory
entries/wirth-2017/.claude:
total 12
drwxr-xr-x 3 runner runner 4096 Nov 13 12:16 .
drwxr-xr-x 4 runner runner 4096 Nov 13 13:19 ..
drwx------ 2 runner runner 4096 Nov 13 12:16 .cc-writes
.gitignore:1:__pycache__/	entries/wirth-2017/__pycache__
```

**Agent**

The author run is complete: 28 claims recorded, the entry's checks pass with 0 errors, and the handover is built. The notebook ran from a clean environment in 1,178 s (about 20 minutes), with peak memory around 1 GB.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| gaze-anticipates-action | reproduced (rests on an assumption about the eye signal's sign) |
| gaze-anticipates-landmarks | reproduced (same assumption) |
| learning-trials | reproduced (monkey S 12.26, monkey K 16.53 / 15.82) |
| learning-to-90 | reproduced (0.898) |
| probe-transfer | not_reproduced (monkey K 28% → 58%, p = 0.07; monkey S has no probe sessions in the data) |
| probe-faster-criterion | blocked, methods_underspecified |
| cells-recorded | partially_reproduced (only the 189 analysed cells are deposited, not all 270 recorded) |
| state-space-most-responsive | not_reproduced (57 cells against 84) |
| direction-center-vs-periphery | not_reproduced |
| direction-tuning-not-maintained | partially_reproduced (15 of 40 low, the paper's 36%, but counts outside tolerance) |
| sparsity-state-vs-direction | reproduced (main reading only, assumed) |
| sparsity-state-vs-position | not_reproduced |
| state-space-selectivity | not_reproduced |
| landmark-identity-distance | not_reproduced (distance count at most 24 or 31 against 64) |
| responsive-cells, multi-space-coding, state-space-ic-higher, sparsity-gaze-vs-state, spatial-selectivity-fraction, landmark-identity-center, path-selectivity, gaze-aligned-dynamics, latency-skew, eccentricity-modulation, foveation-selectivity, gaze-map-landmarks | blocked, metadata_insufficient |
| fields-per-cell, dimensionality-control | blocked, methods_underspecified |

## 2. Dataset, assumptions, questions

**What the data show:**
- The eye signal has no units, calibration or sign. It is on a ±5000 scale in some sessions and ±5 in others. Without it the point-of-gaze space cannot be built, and that is behind 12 of the blocked claims.
- The learning-curve columns are probability, lower bound, upper bound, not the order the descriptor gives. The undocumented field `learningtrial` equals the paper's learning criterion.
- Eye samples are 200 Hz, not the 250 Hz the descriptor states.
- The rewarded arm is code 53 in only 32 of 66 sessions.
- Two hc-12 files have no new-maze data.
- hc-12 holds 12 of monkey K's 15 probe sessions and none of monkey S's 9.
- 87 of the 101 hc-21 files hold the same spike trains as hc-12 files, under other names. No claim rests on hc-21; I used it only for this overlap check and to look for the missing probe sessions.

**Assumptions:**
- A negative horizontal eye value is rightward. This rests on the optokinetic shift during turns.
- Eye values are standardized within each session before sessions are pooled.
- The main reading includes returns in the trial window and permutes the order of the 5 s chunks for the surrogates.
- The three rotational moves are the 36° alignment and 72° turns right and left.
- Counts over the paper's responsive set are bounded between the cells responsive in three spaces and all cells. I used those bounds for three claims (state-space-most-responsive, state-space-selectivity, landmark-identity-distance).

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- How the surrogate chunks were shifted, and whether maps include the returns. These readings change the significant counts about two-fold.
- Which method reference 60 is, for the learning curves.
- How a positional field is defined, and how the dimensionality control was done.
- Which moves enter the state-space selectivity index, and which laps the two-way ANOVA used. The ANOVA's residual df of 756 matches only all 193 laps of session sn20110624.

**Questions to a reader:** none.

## 3. Protocol points

1. The datasets are tar.gz files, not zips, so they cannot be opened in place. I streamed each archive with `tarfile` in `r|gz` mode, reducing each member in memory as it was read.
2. The protocol doesn't say how to judge a count over a selection that cannot be formed. I used lower and upper bounds and blocked a claim only when the bounds include the expected value; it is stated in the notebook.
3. The protocol doesn't say what to do when part of a criterion can't be tested (monkey S's probe sessions). I judged probe-transfer on monkey K's values, which already fail the criterion.
4. During development I cached reduced arrays, not raw files, in `$TMPDIR` to avoid re-streaming. The protocol doesn't address dev caches; the entry itself streams the data.
5. The protocol says what a `partially_reproduced` covers only loosely. I used it for a correct proportion with counts outside tolerance (direction-tuning-not-maintained) and for cells-recorded.

## 4. Runtime and failures

The run took about 1 h 50 min, 11:51 to 13:42 UTC. Two full runs of the entry passed: 1,231 s, then 1,178 s. During development the loader failed twice, on files whose camera data or eye channels sit in other layouts; I fixed both and nothing failed after. `entry.yaml` still says 30 minutes of runtime where the actual run takes about 20; I left it so as not to invalidate the executed copy. As instructed, nothing was committed or pushed.

## End of run

74 turns, 104 minutes, $7.42 at API prices, result: success.
