# asari-2009 · author · run 43709631660

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; ls; ls docs entries attempts claims paper tools; wc -l docs/*.md README.md
```

```
Sun Nov 15 11:42:12 UTC 2026
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
[... 1011 more lines not kept]
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
 "file_path": "claims/asari-2009.yaml"
}
```

```
1	# Claims for Asari & Zador (2009), J Neurophysiol 102:2638-2656, on CRCNS ac-1.
2	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
3	# protocol pilot-14 as stated in docs/protocol.md. The writer did not look at the dataset's data or
4	# files; only its description on crcns.org (paper/ac-1.data-description.txt) was read.
5	#
6	# Text read: the version of record, as a text extraction of the publisher's PDF (PyMuPDF), with
7	# the PDF. The extraction garbles some symbols (Greek letters, "<", ">", "~", "=" and "+/-" print
8	# as a replacement glyph); they were read from context, and quotes are cut around them. The PDF
9	# pages could not be rendered in this run, so figure axes were not read; every value used here is
10	# printed in the text or a legend. The online supplement (Supplemental Figures S1 to S10) was not
11	# supplied and was not read. The main findings rest on the main-text Figures 2 to 9 and their
12	# legends; the supplement holds example traces (S2 to S10) and the "silence probe" analysis (S1),
13	# whose one claim (figs1-silence-probe) is quoted from the Methods only.
14	#
15	# Code read: none. The paper links no code; it says all analysis was done in MATLAB.
16	#
17	# Data the paper used. Long-Evans rats, 20 to 28 days old, anesthetized with ketamine and
18	# medetomidine; in vivo blind patch recordings sampled at 10 kHz.
19	# - A1 current clamp (whole cell): 194 cells in 139 animals, of which 123 met the analysis
20	#   criterion (at least 4 repeats of a probe tested with at least 2 conditioning stimuli). By
[... 697 more lines not kept]
```

**Agent calls Bash**

```bash
cat paper/ac-1.data-description.txt; ls entries/fouke-2025 entries/asari-2009; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in; ls questions | head; cat papers/datasets/asari-2009.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/CRCNS/,/^## [A-Z]/p' docs/archives.md | head -120; cat attempts/fouke-2025-01.yaml | head -150
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
[... 158 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/^findings/,$p' attempts/fouke-2025-01.yaml | head -60; ls schemas; grep -n "blocked_by\|assumed\|measured" schemas/attempt*.json | head -30
```

```
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
    only Danio rerio; the files hold 37 fish of two species.
[... 52 more lines not kept]
```

**Agent**

Now let me list the dataset in the bucket.

**Agent calls Bash**

```bash
curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=ac-1/" | python3 -c "
import sys,re
t=sys.stdin.read()
for k,s in re.findall(r'<Key>(.*?)</Key>.*?<Size>(\d+)</Size>',t): print(s,k)
print(re.findall(r'<IsTruncated>(.*?)<',t))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
B=https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-1; curl -s $B/checksums.md5; curl -s $B/filelist.txt; python3 -c "import fsspec,scipy,h5py;print('ok')"; which uv python3
```

```
18537da81d98e311c0274f62aea04daa  crcns-ac1-asari-results-1.zip
2f7ab955cc778fc6839ce59ed51bce89  crcns-ac1-asari-results-2.zip
2300ee76d93383ab8c808ddf16761a23  crcns-ac1.zip
bd87f2663a3b383dc33de4841d601d54  filelist.txt
# CRCNS.org 'ac-1' dataset files
# To use this for fetching files, comment out files that are
# not needed by putting a '#' as the first character on the line (default mode)
# or put a '+' as the first character to specifiy files to be fetched (+ mode).
# mode='default' (change to '+' for + mode).
 crcns-ac1-asari-results-1.zip	1470654524 (1.3 GB)
 crcns-ac1-asari-results-2.zip	1368844108 (1.2 GB)
 crcns-ac1.zip	1348780283 (1.2 GB)
 checksums.md5	223
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import fsspec,scipy,h5py;print('ok')
    ^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'fsspec'
/opt/hostedtoolcache/Python/3.13.18/x64/bin/uv
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python3
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && . dev/bin/activate && uv pip install -q fsspec aiohttp requests scipy h5py numpy matplotlib pandas nbformat nbclient ipykernel 2>&1 | tail -2; python -c "
import fsspec,zipfile
B='https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-1/'
for f in ['crcns-ac1.zip','crcns-ac1-asari-results-1.zip','crcns-ac1-asari-results-2.zip']:
    z=zipfile.ZipFile(fsspec.open(B+f,block_size=2**20).open())
    il=z.infolist(); print(f,len(il))
    for i in il: print(' ',i.file_size,i.filename)
" > $TMPDIR/list.txt; wc -l $TMPDIR/list.txt; head -80 $TMPDIR/list.txt
```

```
2335 /tmp/claude-1001/list.txt
crcns-ac1.zip 1823
  0 asari/
  6221 asari/Summary.mat
  3478 asari/Contents.m
  0 asari/Stimuli/
  1140806 asari/Stimuli/NaturalSoundFragments.pdf
  0 asari/Stimuli/class6/
  3017588 asari/Stimuli/class6/8.mat
  3244692 asari/Stimuli/class6/7.mat
  1594084 asari/Stimuli/class6/6s.mat
  3082738 asari/Stimuli/class6/6pl.mat
  3084367 asari/Stimuli/class6/6p.mat
  3077803 asari/Stimuli/class6/6m.mat
  4103837 asari/Stimuli/class6/6l.mat
  3487505 asari/Stimuli/class6/6.mat
  2638018 asari/Stimuli/class6/5.mat
  1606957 asari/Stimuli/class6/4s.mat
  2563659 asari/Stimuli/class6/4.mat
  1604211 asari/Stimuli/class6/3s.mat
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; grep -v "Stimuli/class" list.txt | awk '{print $2}' | sed 's#/[^/]*$##' | sort | uniq -c | head -80; grep -v Stimuli/class list.txt | grep -v "/$" | head -60
```

```
1 1823
      1 245
      1 264
      1 Methods.txt
      1 ReadMe.txt
      3 asari
      2 asari-results-1
      3 asari-results-1/20051101-ha1-005
      4 asari-results-1/20051107-ha1-001
      3 asari-results-1/20051107-ha1-002
      4 asari-results-1/20051108-ha1-001
      3 asari-results-1/20051114-ha2-001
      3 asari-results-1/20051125-ha1-001
      3 asari-results-1/20051126-ha2-001
      4 asari-results-1/20051126-ha2-002
      5 asari-results-1/20051126-ha2-003
      3 asari-results-1/20051127-ha1-001
      3 asari-results-1/20051127-ha1-002
      3 asari-results-1/20051203-ha1-001
      3 asari-results-1/20051207-ha1-002
[... 121 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . dev/bin/activate; python -c "
import fsspec,zipfile
B='https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-1/'
z=zipfile.ZipFile(fsspec.open(B+'crcns-ac1.zip',block_size=2**20).open())
import os
os.makedirs('code',exist_ok=True)
for n in z.namelist():
    if n.endswith(('.m','.txt')):
        p='code/'+n.replace('/','__'); open(p,'wb').write(z.read(n))
"; ls code; cat code/ReadMe.txt code/Methods.txt code/asari__Contents.m code/asari__Results__README-Results.txt
```

```
Methods.txt
ReadMe.txt
asari__Contents.m
asari__Results__README-Results.txt
asari__Tools__CxtDep.m
asari__Tools__DMRipple2.m
asari__Tools__GetData.m
asari__Tools__GetEvoked.m
asari__Tools__GetSpikes.m
asari__Tools__MHTones.m
asari__Tools__MakeRamp.m
asari__Tools__MakeRandomChords.m
asari__Tools__MakeTone.m
asari__Tools__MakeWhiteNoise.m
asari__Tools__MovingRipple4.m
asari__Tools__PinkNoise.m
asari__Tools__SoundTrans.m
asari__Tools__TuningCurve.m
asari__Tools__ViewCxtDep.m
asari__Tools__ViewResp.m
[... 327 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code; cat asari__Tools__CxtDep.m asari__Tools__GetEvoked.m
```

```
function [PARAM,stim] = CxtDep(response,triggers,param)

% Basic analysis script for Asari and Zador (2008)
%
% --- Input ---
%   response - structure containing 
%       .trace : data vector
%       .datatype : specify data class of .trace
%       .scale : scaling factors if the input is in int16
%       .sf : sampling frequency
%
%   triggers - structure containing
%       .type : stimulus type
%       .time : trigger onset position
%       .param : parameters of stimuli
%
%   param - structure containing various parameters
%       .smooth : window length of median filter smoothing (default: 10 msec)
%       .homedir : home directory (optional)
%       .fig : vector of stimulus index to be shown
[... 546 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code; cat asari__Tools__ViewResp.m asari__Tools__GetData.m; sed -n 1,400p asari__Tools__GetSpikes.m | head -150
```

```
function [resp,stim,spont] = ViewResp(response,triggers,param)

% displays responses aligned with stimuli
%
% --- caution ---
%   Further computions need to be dome for some stimuli.
%   Edit soubroutine GETSTIMULI to obtain appropriate stimulus information.
%
% --- Input ---
%   response - structure containing 
%       .trace : data vector
%       .datatype : specify data class of .trace
%       .scale : scaling factors if the input is in int16
%       .sf : sampling frequency
%
%   triggers - structure containing
%       .type : stimulus type
%       .time : trigger onset position
%       .param : parameters of stimuli
%
[... 444 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code; sed -n 150,400p asari__Tools__GetSpikes.m
```

```
end
                reextract=0;
            end
            hold off; plot(filtered); hold on; set(gca,'XLim',[plotfrom plotto]);

            tmp_spikes = threshold*ones(size(filtered))*(auto~=0);
%            tmp_spikes = sweep_spikes; 
            tmp_spikes(sweep_spikes==1) = filtered(sweep_spikes==1); 
            plot(tmp_spikes,'r'); % spikes in red
%            spplot=plot(sweep_spikes,'r'); 
            plot([1 length(sweep_spikes)],[threshold threshold],'g'); % threshold in green
        end

        spike_pos=find(sweep_spikes==1); % stores the spike positions so far before moving on
    	if ~isempty(spike_pos), spikes=[spikes; spike_pos+fromdatasample-1];end
        
    end 
    
    spikes=unique(spikes);  % IMPORTANT, because we are using overlapping windows
    close(fig);
[... 151 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; grep -c . list.txt; grep "results-2" -A3 list.txt | head; awk '{print $2}' list.txt | grep -o '\.[a-z]*$' | sort | uniq -c; grep asari-results list.txt | head -20; wc -c ~/work/encore/encore/paper/*.txt; date -u
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; . dev/bin/activate; python -c "
import fsspec,zipfile,scipy.io as sio,io
B='https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-1/'
z=zipfile.ZipFile(fsspec.open(B+'crcns-ac1.zip',block_size=2**20).open())
open('asari_Summary.mat','wb').write(z.read('asari/Summary.mat'))
open('wehr_Summary.mat','wb').write(z.read('wehr/Summary.mat'))
m=sio.loadmat('asari_Summary.mat',squeeze_me=True,struct_as_record=False)
e=m['experiment']
print(type(e), getattr(e,'shape',None))
for x in (e if hasattr(e,'__len__') else [e]):
    print('==',x.description, '|', x.reference if hasattr(x,'reference') else '')
    c=x.cell
    c = c if hasattr(c,'__len__') else [c]
    print(' ncell',len(c))
    for cc in c[:3]: print('  ',cc.file, '|', cc.description)
"
```

```
<class 'numpy.ndarray'> (4,)
== Auditory cortical cell responses to natural sound combinations. | Asari and Zador (submitted) Long-lasting context dependence constrains neural encoding models in rodent auditory cortex.
 ncell 39
   ['Results/20051101-ha1-005/20051101-ha1-005-001.mat'
 'Results/20051101-ha1-005/20051101-ha1-005-003.mat'] | ['tuning curve' 'Natural Sounds: combinations of 4 stimuli (class5)']
   ['Results/20051107-ha1-001/20051107-ha1-001-001.mat'
 'Results/20051107-ha1-001/20051107-ha1-001-003.mat'
 'Results/20051107-ha1-001/20051107-ha1-001-004.mat'] | ['tuning curve' 'Natural Sounds: combinations of 4 stimuli (class6)'
 'Natural Sounds: combinations of 4 stimuli (class5)']
   ['Results/20051107-ha1-002/20051107-ha1-002-001.mat'
 'Results/20051107-ha1-002/20051107-ha1-002-003.mat'] | ['tuning curve' 'Natural Sounds: combinations of 4 stimuli (class6)']
== Thalamic cell responses to natural sound combinations. | Asari and Zador (submitted) Long-lasting context dependence constrains neural encoding models in rodent auditory cortex.
 ncell 14
   ['Results/20071009-ha1-002/20071009-ha1-002-001.mat'
 'Results/20071009-ha1-002/20071009-ha1-002-002.mat'
 'Results/20071009-ha1-002/20071009-ha1-002-003.mat'] | ['tuning curve' 'Natural Sounds: combinations of 4 stimuli (class6)'
 'Natural Sounds: combinations of 4 stimuli (class5)']
   ['Results/20071009-ha1-003/20071009-ha1-003-001.mat'
 'Results/20071009-ha1-003/20071009-ha1-003-002.mat'
 'Results/20071009-ha1-003/20071009-ha1-003-003.mat'
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . dev/bin/activate; python -c "
import scipy.io as sio, collections
m=sio.loadmat('asari_Summary.mat',squeeze_me=True,struct_as_record=False)
for x in m['experiment']:
    c=x.cell; c=c if hasattr(c,'__len__') else [c]
    cnt=collections.Counter(); nf=0
    for cc in c:
        f=cc.file; f=[f] if isinstance(f,str) else list(f)
        d=cc.description; d=[d] if isinstance(d,str) else list(d)
        for dd in d:
            if not isinstance(dd,str): dd=' '.join(s.strip() for s in dd)
            cnt[dd]+=1
        nf+=len(f)
    print('==',x.description,len(c),'cells',nf,'files')
    for k,v in cnt.items(): print('   ',v,k)
"
python - <<'EOF'
import scipy.io as sio
m=sio.loadmat('wehr_Summary.mat',squeeze_me=True,struct_as_record=False)
e=m['experiment']; e=e if hasattr(e,'__len__') else [e]
for x in e:
    print(x.description, getattr(x,'reference',''))
    c=x.cell; c=c if hasattr(c,'__len__') else [c]; print(len(c)); print(c[0].file, c[0].description)
EOF
```

```
== Auditory cortical cell responses to natural sound combinations. 39 cells 85 files
    39 tuning curve
    3 Natural Sounds: combinations of 4 stimuli (class5)
    3 Natural Sounds: combinations of 4 stimuli (class6)
    5 Natural Sounds: combinations of 6 stimuli (one of each class)
    4 Natural Sounds: combinations of 5 short stimuli (each with 2 intensities)
    1 Natural Sounds: combinations of 4 stimuli (class4)
    1 Natural Sounds: combinations of 10 short stimuli
    24 Natural Sounds: combinations of 7 long stimuli
    2 Natural Sounds: combinations of 3 stimuli (each with 3 intensities; class 6)
    1 Natural Sounds: combinations of 3 stimuli (each with 3 intensities; class 4)
    2 Natural Sounds: combinations of one probe (class2-2) and many contexts
== Thalamic cell responses to natural sound combinations. 14 cells 35 files
    14 tuning curve
    12 Natural Sounds: combinations of 4 stimuli (class6)
    5 Natural Sounds: combinations of 4 stimuli (class5)
    3 Natural Sounds: combinations of 7 long stimuli
    1 Natural Sounds: combinations of 4 stimuli (class4)
== Auditory cortical cell responses to synthetic sound combinations. 96 cells 201 files
    96 tuning curve
[... 335 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n "METHODS\|RESULTS\|DISCUSSION\|REFERENCES\|Analysis\|Stimulus design\|Electrophysiology\|Neural encoding\|Model performance\|TABLE" 10.1152-jn.00577.2009.txt | head -40; wc -l 10.1152-jn.00577.2009.txt
```

```
119:Electrophysiology
171:Stimulus design
174:TABLE 1.
213:than one probe stimulus, each of which could in turn be tested with more than one type of conditioning stimulus ensemble (see also Stimulus design in METHODS
282:goal of the analysis (for details, see Stimulus design in METHODS). Here we assumed that the response power (broken line; �[rij(t)] from Eq. 11) to a probe stimulus
284:decomposed into a context-independent fraction (�[�(t)] in Eq. 18) and a context-dependent fraction (gray; �[�i(t)] in Eq. 19). For details, see Analysis in
285:METHODS. B: natural sounds and synthetic sounds. Natural sound fragments (SNS1 and SNS2; 4.11 s long; sound pressure waveforms, spectrograms, and temporal
291:has slower AM rates by 4 Hz on average, and S�FM has half the SD for the frequency-modulated (FM) depth. For details, see SYNTHETIC SOUNDS in METHODS.
299:stimulus combinations as possible (see Stimulus design and Fig. 1A).
462:Analysis
529:responses to the probe stimulus (see Stimulus design), the mode of
703:resistance compensation was used (see Electrophysiology). The total
747:(see Electrophysiology in preceding text).
1006:with enough varieties of stimuli (see Stimulus design), which could
1128:(see Stimulus design in METHODS and Fig. 1). The use of such
1219:dependence. (Note that the estimated power can be negative; see CONTEXT DEPENDENCE AT SUBTHRESHOLD VOLTAGE LEVEL in METHODS for details.) The
1247:DEPENDENCE AT SUBTHRESHOLD VOLTAGE LEVEL in METHODS for
1317:exceeds threshold (P �0.01 for �5 ms; see CONTEXT DEPENDENCE AT SUBTHRESHOLD VOLTAGE LEVEL in METHODS) for a particular probe–stimulus combination
1355:VOLTAGE LEVEL and RESPONSE PREDICTABILITY in METHODS for
1405:could build a plausible predictive model (see also DISCUSSION,
[... 12 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1152-jn.00577.2009.txt",
 "offset": 100,
 "limit": 340
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1152-jn.00577.2009.txt",
 "offset": 460,
 "limit": 560
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1152-jn.00577.2009.txt",
 "offset": 1019,
 "limit": 420
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1152-jn.00577.2009.txt",
 "offset": 1438,
 "limit": 520
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Paper and analysis code read. Now inspecting a data file.

**Agent calls Bash**

```bash
cd $TMPDIR; . dev/bin/activate; date -u; time python - <<'EOF'
import fsspec,zipfile,scipy.io as sio,io,numpy as np
B='https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-1/'
z=zipfile.ZipFile(fsspec.open(B+'crcns-ac1-asari-results-1.zip',block_size=2**22).open())
names=[n for n in z.namelist() if n.endswith('.mat')]
n='asari-results-1/20051107-ha1-001/20051107-ha1-001-003.mat'
b=z.read(n); print(len(b))
m=sio.loadmat(io.BytesIO(b),squeeze_me=True,struct_as_record=False)
print(m.keys())
r=m['response']; print(r._fieldnames, r.trace.dtype, r.trace.shape, r.scale, r.unit, r.sf, r.datatype)
t=m['triggers']; print(type(t), t.shape, t[0]._fieldnames)
for x in t[:4]: print(x.type, x.time, x.param._fieldnames if hasattr(x.param,'_fieldnames') else x.param)
print(t[0].param.__dict__)
p=m['param']; print(p._fieldnames)
print(p.ID.__dict__); print(p.recording.__dict__)
print(p.notes)
s=p.stimulus; print(type(s), getattr(s,'shape',None)); 
s0 = s[0] if hasattr(s,'__len__') else s
print(s0._fieldnames, s0.__dict__ if len(str(s0.__dict__))<2000 else str(s0.__dict__)[:2000])
EOF
```

```
Sun Nov 15 11:43:52 UTC 2026
13230521
dict_keys(['__header__', '__version__', '__globals__', 'response', 'triggers', 'param'])
['trace', 'datatype', 'scale', 'unit', 'sf'] int16 (12214208,) 0.015259021896696421 mV 10000 int16
<class 'numpy.ndarray'> (97,) ['type', 'time', 'param']
pulse 9839 ['start', 'width', 'height', 'npulses', 'isi', 'duration']
naturalsound 54400 ['duration', 'description']
pulse 259687 ['start', 'width', 'height', 'npulses', 'isi', 'duration']
naturalsound 304683 ['duration', 'description']
{'_fieldnames': ['start', 'width', 'height', 'npulses', 'isi', 'duration'], 'start': 0, 'width': 100, 'height': -100, 'npulses': 1, 'isi': 0, 'duration': 100}
['ID', 'animal', 'prep', 'recording', 'stimulus', 'notes', 'reference']
{'_fieldnames': ['date', 'animal', 'PenetNo', 'RecNo', 'info', 'description'], 'date': '20051107', 'animal': 'ha1', 'PenetNo': 1, 'RecNo': 3, 'info': 'Hiroki Asari, Zador Lab, CSHL', 'description': 'Natural Sounds: combinations of 4 stimuli (class6)'}
{'_fieldnames': ['type', 'electrode', 'depth', 'pressure', 'Rt', 'Rs', 'offset', 'site'], 'type': 'Whole-cell', 'electrode': '4.30', 'depth': '426', 'pressure': '-1', 'Rt': '1200.00', 'Rs': '400.00', 'offset': '-8.80', 'site': 'Contralateral (left) primary auditory cortex'}
['Stimulus sequences are given as follows.                          '
 'Seq.1:  2  1  3  1  4                                             '
 'Seq.2:  3  2  4  4  1                                             '
 'Seq.3:  4  3  3  4  2                                             '
 'Seq.4:  1  1  2  2  3                                             '
 '                                                                  '
 'Effective repeats:  12                                            '
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . dev/bin/activate; python - <<'EOF'
import fsspec,zipfile,scipy.io as sio,io,numpy as np
B='https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-1/'
z=zipfile.ZipFile(fsspec.open(B+'crcns-ac1-asari-results-1.zip',block_size=2**22).open())
n='asari-results-1/20051107-ha1-001/20051107-ha1-001-003.mat'
m=sio.loadmat(io.BytesIO(z.read(n)),squeeze_me=True,struct_as_record=False)
t=m['triggers']
for x in t[:8]: print(x.type, x.time, x.param.__dict__)
print(np.diff([x.time for x in t if x.type!='pulse'])[:10]/1e4)
s=m['param'].stimulus
for x in s: print(x.name, x.file, x.param.__dict__)
print(m['param'].animal.__dict__, m['param'].prep.__dict__)
print(m['param'].reference)
print([zi for zi in z.infolist() if zi.filename==n][0].compress_type)
EOF
```

```
pulse 9839 {'_fieldnames': ['start', 'width', 'height', 'npulses', 'isi', 'duration'], 'start': 0, 'width': 100, 'height': -100, 'npulses': 1, 'isi': 0, 'duration': 100}
naturalsound 54400 {'_fieldnames': ['duration', 'description'], 'duration': 19940, 'description': 'Sequence 2: 2  1  3  1  4'}
pulse 259687 {'_fieldnames': ['start', 'width', 'height', 'npulses', 'isi', 'duration'], 'start': 0, 'width': 100, 'height': -100, 'npulses': 1, 'isi': 0, 'duration': 100}
naturalsound 304683 {'_fieldnames': ['duration', 'description'], 'duration': 20440, 'description': 'Sequence 4: 3  2  4  4  1'}
pulse 515001 {'_fieldnames': ['start', 'width', 'height', 'npulses', 'isi', 'duration'], 'start': 0, 'width': 100, 'height': -100, 'npulses': 1, 'isi': 0, 'duration': 100}
naturalsound 561719 {'_fieldnames': ['duration', 'description'], 'duration': 21240, 'description': 'Sequence 6: 4  3  3  4  2'}
pulse 780005 {'_fieldnames': ['start', 'width', 'height', 'npulses', 'isi', 'duration'], 'start': 0, 'width': 100, 'height': -100, 'npulses': 1, 'isi': 0, 'duration': 100}
naturalsound 825347 {'_fieldnames': ['duration', 'description'], 'duration': 20580, 'description': 'Sequence 8: 1  1  2  2  3'}
[25.0283 25.7036 26.3628 25.2686 24.7158 25.3526 26.04   25.2627 24.6816
 25.3467]
natural sound fragment 1 class6/5.mat {'_fieldnames': ['ramp', 'duration', 'sf'], 'ramp': 5, 'duration': 3500.0307200786438, 'sf': 97656}
natural sound fragment 2 class6/6.mat {'_fieldnames': ['ramp', 'duration', 'sf'], 'ramp': 5, 'duration': 4640.0323584828375, 'sf': 97656}
natural sound fragment 3 class6/7.mat {'_fieldnames': ['ramp', 'duration', 'sf'], 'ramp': 5, 'duration': 4300.032768083886, 'sf': 97656}
natural sound fragment 4 class6/8.mat {'_fieldnames': ['ramp', 'duration', 'sf'], 'ramp': 5, 'duration': 4000.0307200786438, 'sf': 97656}
{'_fieldnames': ['species', 'sex', 'age', 'weight'], 'species': 'Long-Evans Rat', 'sex': 'male', 'age': '24', 'weight': '47'} {'_fieldnames': ['anesthesia', 'surgery'], 
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . dev/bin/activate; cat > survey.py <<'EOF'
import fsspec,zipfile,scipy.io as sio,io,numpy as np,pickle,collections,time
from concurrent.futures import ThreadPoolExecutor
B='https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-1/'
def job(args):
    zipname, names = args
    z=zipfile.ZipFile(fsspec.open(B+zipname,block_size=2**22).open())
    out={}
    for n in names:
        try:
            m=sio.loadmat(io.BytesIO(z.read(n)),squeeze_me=True,struct_as_record=False)
        except Exception as e:
            out[n]={'error':repr(e)}; continue
        r=m['response']; p=m['param']; t=m['triggers']; t=np.atleast_1d(t)
        st=np.atleast_1d(p.stimulus) if hasattr(p,'stimulus') else []
        d=dict(type=p.recording.type, desc=p.ID.description, sf=r.sf, n=len(r.trace), unit=r.unit, scale=r.scale,
               offset=p.recording.offset, notes=list(np.atleast_1d(p.notes)) if hasattr(p,'notes') else [],
               trig=collections.Counter(x.type for x in t),
               tdesc=collections.Counter(str(getattr(x.param,'description','')) for x in t if x.type!='pulse'),
               stim=[(getattr(s,'name',''),getattr(s,'description',''),getattr(s,'file',''),getattr(getattr(s,'param',None),'duration',None)) for s in st],
               age=p.animal.age if hasattr(p,'animal') else None, recfields=p.recording._fieldnames)
        out[n]=d
    return out
jobs=[]
for zn in ['crcns-ac1-asari-results-1.zip','crcns-ac1-asari-results-2.zip']:
    z=zipfile.ZipFile(fsspec.open(B+zn).open())
    ns=[n for n in z.namelist() if n.endswith('.mat')]
    for k in range(0,len(ns),40): jobs.append((zn,ns[k:k+40]))
t0=time.time()
res={}
with ThreadPoolExecutor(4) as ex:
    for o in ex.map(job,jobs): res.update(o)
print(len(res), time.time()-t0)
pickle.dump(res,open('survey.pkl','wb'))
EOF
python survey.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/survey.py", line 31, in <module>
    for o in ex.map(job,jobs): res.update(o)
             ~~~~~~^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/concurrent/futures/_base.py", line 625, in result_iterator
    yield _result_or_cancel(fs.pop())
          ~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/concurrent/futures/_base.py", line 318, in _result_or_cancel
    return fut.result(timeout)
           ~~~~~~~~~~^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/concurrent/futures/_base.py", line 453, in result
    return self.__get_result()
           ~~~~~~~~~~~~~~~~~^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/concurrent/futures/_base.py", line 402, in __get_result
    raise self._exception
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/concurrent/futures/thread.py", line 59, in run
    result = self.fn(*self.args, **self.kwargs)
  File "/tmp/claude-1001/survey.py", line 16, in job
    offset=p.recording.offset, notes=list(np.atleast_1d(p.notes)) if hasattr(p,'notes') else [],
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . dev/bin/activate; sed -i "s/offset=p.recording.offset,/offset=getattr(p.recording,'offset',None),/; s/type=p.recording.type,/type=getattr(p.recording,'type',None),/" survey.py; python survey.py
```

```
346 32.63009762763977
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; . dev/bin/activate; python - <<'EOF'
import pickle,collections
r=pickle.load(open('survey.pkl','rb'))
print(collections.Counter(d.get('type') for d in r.values()))
print(collections.Counter(d.get('error') for d in r.values()))
c=collections.Counter((d.get('type'),d.get('desc') if isinstance(d.get('desc'),str) else ' '.join(x.strip() for x in d.get('desc'))) for d in r.values())
for k,v in sorted(c.items(),key=str): print(v,k)
print(collections.Counter(d.get('sf') for d in r.values()), collections.Counter(d.get('unit') for d in r.values()))
tt=collections.Counter()
for d in r.values(): tt.update(d.get('trig',{}).keys())
print(tt)
EOF
```

```
Counter({'Whole-cell': 311, 'Cell-attached': 35})
Counter({None: 346})
1 ('Cell-attached', 'Natural Sounds: combinations of 4 stimuli (class4)')
5 ('Cell-attached', 'Natural Sounds: combinations of 4 stimuli (class5)')
12 ('Cell-attached', 'Natural Sounds: combinations of 4 stimuli (class6)')
3 ('Cell-attached', 'Natural Sounds: combinations of 7 long stimuli')
14 ('Cell-attached', 'tuning curve')
6 ('Whole-cell', 'Combinations of 4 sounds (2 natural sounds, each with corresponding pink noise)')
58 ('Whole-cell', 'Combinations of 4 synthetic sounds')
5 ('Whole-cell', 'Combinations of 6 naturalistic sounds')
8 ('Whole-cell', 'Combinations of 6 sounds (2 natural sounds, each with 2 corresponding pink noise)')
10 ('Whole-cell', 'Combinations of 6 sounds (3 natural sounds, each with corresponding pink noise)')
7 ('Whole-cell', 'Combinations of 6 synthetic sounds')
1 ('Whole-cell', 'Natural Sounds: combinations of 10 short stimuli')
1 ('Whole-cell', 'Natural Sounds: combinations of 3 stimuli (each with 3 intensities; class 4)')
2 ('Whole-cell', 'Natural Sounds: combinations of 3 stimuli (each with 3 intensities; class 6)')
1 ('Whole-cell', 'Natural Sounds: combinations of 4 stimuli (class4)')
3 ('Whole-cell', 'Natural Sounds: combinations of 4 stimuli (class5)')
3 ('Whole-cell', 'Natural Sounds: combinations of 4 stimuli (class6)')
4 ('Whole-cell', 'Natural Sounds: combinations of 5 short stimuli (each with 2 intensities)')
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; grep "wehr/" list.txt | awk '{print $2}' | sed 's#/[^/]*$##' | sort | uniq -c; grep "wehr/Results" list.txt | awk '{s+=$1} END {print s}'; cat code/wehr__Contents.m | head -80
```

```
3 wehr
      1 wehr/Results
    154 wehr/Results/20020508-mw-003
    121 wehr/Results/20020530-mw-001
     66 wehr/Results/20020602-mw-001
    113 wehr/Results/20020604-mw-001
     61 wehr/Results/20020604-mw-002
    169 wehr/Results/20020604-mw-003
     96 wehr/Results/20020605-mw-002
     81 wehr/Results/20020605-mw-003
     74 wehr/Results/20020608-mw-001
    219 wehr/Results/20020608-mw-002
     17 wehr/Results/20030328-mw-001
     47 wehr/Results/20030401-mw-001
     29 wehr/Results/20030401-mw-003
     62 wehr/Results/20030403-mw-001
     15 wehr/Results/20030404-mw-001
     32 wehr/Results/20030404-mw-002
     51 wehr/Results/20030407-mw-001
     30 wehr/Results/20030407-mw-002
[... 91 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . dev/bin/activate; python - <<'EOF'
import pickle,collections
r=pickle.load(open('survey.pkl','rb'))
seen=set()
for n,d in sorted(r.items()):
    desc=d['desc'] if isinstance(d['desc'],str) else ' '.join(x.strip() for x in d['desc'])
    if desc=='tuning curve' or desc in seen: continue
    seen.add(desc)
    print('=====',n,d['type'],desc, dict(d['trig']))
    print('\n'.join(x.rstrip() for x in d['notes'] if x.strip())[:1500])
    print(list(d['tdesc'].items())[:3])
    for s in d['stim'][:8]: print('   ',s)
EOF
```

```
===== asari-results-1/20051101-ha1-005/20051101-ha1-005-003.mat Whole-cell Natural Sounds: combinations of 4 stimuli (class5) {'naturalsound': 28}
Stimulus sequences are given as follows.
Seq.1:  2  1  3  1  4
Seq.2:  3  2  4  4  1
Seq.3:  4  3  3  4  2
Seq.4:  1  1  2  2  3
Effective repeats:  6
Natural Sound CDs (Cornell Laboratory of Ornithology, Ithaca, NY):
The Diversity of Animal Sounds
Sounds of Neotropical Rainforest Mammals, Disc 1 and 2
[('Sequence 1: 2  1  3  1  4', 7), ('Sequence 2: 3  2  4  4  1', 7), ('Sequence 3: 4  3  3  4  2', 7)]
    ('natural sound fragment 1', 'neotropical-mammals-2 Track 07 (Saddleback tamarin) From 81.343 to 85.45 sec', 'class5/5.mat', 4107.038994019825)
    ('natural sound fragment 2', 'neotropical-mammals-2 Track 18 (Golden lion tamarin) From 68.76 to 72.96 sec', 'class5/6.mat', 4200.0286720734)
    ('natural sound fragment 3', 'neotropical-mammals-2 Track 20 (Golden-rumped lion tamarin) From 52.33 to 56.3 sec', 'class5/7.mat', 3970.0274432702545)
    ('natural sound fragment 4', 'diversity Track 34 (Winter Wren) From 42.97 to 47.95 sec', 'class5/1.mat', 4980.0319488817895)
===== asari-results-1/20051107-ha1-001/20051107-ha1-001-003.mat Whole-cell Natural Sounds: combinations of 4 stimuli (class6) {'pulse': 49, 'naturalsound': 48}
Stimulus sequences are given as follows.
Seq.1:  2  1  3  1  4
Seq.2:  3  2  4  4  1
Seq.3:  4  3  3  4  2
[... 366 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . dev/bin/activate; python - <<'EOF'
import pickle,collections
r=pickle.load(open('survey.pkl','rb'))
c=collections.Counter(); ex={}
for n,d in sorted(r.items()):
    desc=d['desc'] if isinstance(d['desc'],str) else ' '.join(x.strip() for x in d['desc'])
    if 'synthetic' not in desc and 'pink' not in desc and 'naturalistic' not in desc: continue
    key=(desc, tuple(s[1] for s in d['stim']), tuple(x.strip() for x in d['notes'] if 'variant' in x or 'silence' in x.lower() or 'default' in x))
    c[key]+=1; ex[key]=n
for k,v in c.items(): print(v, ex[k]); print('   ',k)
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 8, in <module>
TypeError: unhashable type: 'numpy.ndarray'
```

**Agent calls Bash**

```bash
cd $TMPDIR; . dev/bin/activate; python - <<'EOF'
import pickle,collections
r=pickle.load(open('survey.pkl','rb'))
c=collections.Counter(); ex={}
for n,d in sorted(r.items()):
    desc=d['desc'] if isinstance(d['desc'],str) else ' '.join(x.strip() for x in d['desc'])
    if 'ynthetic' not in desc and 'pink' not in desc and 'naturalistic' not in desc: continue
    key=(desc, tuple(str(s[1]) for s in d['stim']), tuple(x.strip() for x in d['notes'] if 'variant' in x or 'silence' in x.lower() or 'default' in x))
    c[key]+=1; ex[key]=n
for k,v in c.items(): print(v, ex[k]); print('   ',k)
EOF
```

```
4 asari-results-1/20060216-ha2-002/20060216-ha2-002-002.mat
    ('Combinations of 6 synthetic sounds', ('TORCs: bandwidth variants', 'TORCs: bandwidth variants', 'TORCs: bandwidth variants', 'TORCs: bandwidth variants', 'TORCs: bandwidth variants', 'TORCs: bandwidth variants'), ())
3 asari-results-2/20060202-ha2-002/20060202-ha2-002-002.mat
    ('Combinations of 6 synthetic sounds', ('TORCs: amplitude variants', 'TORCs: amplitude variants', 'TORCs: amplitude variants', 'TORCs: amplitude variants', 'TORCs: amplitude variants', 'TORCs: amplitude variants'), ())
5 asari-results-2/20060315-ha1-002/20060315-ha1-002-003.mat
    ('Combinations of 4 synthetic sounds', ('TORC sequence; bandwidth variants', 'TORC sequence; bandwidth variants', 'TORC sequence; bandwidth variants', 'TORC sequence; bandwidth variants'), ())
6 asari-results-2/20060316-ha1-001/20060316-ha1-001-002.mat
    ('Combinations of 4 synthetic sounds', ('TORC sequence; amplitude variants', 'TORC sequence; amplitude variants', 'TORC sequence; amplitude variants', 'TORC sequence; amplitude variants'), ())
4 asari-results-2/20060910-ha1-001/20060910-ha1-001-002.mat
    ('Combinations of 4 synthetic sounds', ('neotropical-mammals-2 Track 06 (Buffy-headed marmoset) From 41.275 to 46.75 sec', 'neotropical-mammals-2 Track 06 (Buffy-headed marmoset) From 41.275 to 46.75 sec', 'neotropical-mammals-2 Track 06 (Buffy-headed marmoset) From 41.275 to 46.75 sec', 'neotropical-mammals-2 Track 06 (Buffy-headed marmoset) From 41.275 to 46.75 sec', 'neotropical-mammals-2 Track 06 (Buffy-headed marmoset) From 41.275 to 46.75 sec', 'neotropical-mammals-2 Track 06 (Buffy-headed marmoset) From 41.275 to 46.75 sec', 'neotropical-mammals-2 Track 06 (Buffy-headed marmoset) From 41.275 to 46.75 sec', 'neotropical-mammals-2 Track 06 (Buffy-headed marmoset) From 41.275 to 46.75 sec', 'neotropical-mammals-2 Track 06 (Buffy-headed marmoset) From 41.275 to 46.75 sec', 'neotropical-mammals-2 Track 06 (Buffy-headed marmoset) From 41.275 t
[... 71 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . dev/bin/activate; python - <<'EOF'
import fsspec,zipfile,scipy.io as sio,io,numpy as np
B='https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-1/'
z=zipfile.ZipFile(fsspec.open(B+'crcns-ac1-asari-results-2.zip',block_size=2**22).open())
for n in ['asari-results-2/20061008-ha4-001/20061008-ha4-001-002.mat','asari-results-2/20060909-ha4-002/20060909-ha4-002-002.mat','asari-results-2/20060916-ha1-001/20060916-ha1-001-002.mat']:
    m=sio.loadmat(io.BytesIO(z.read(n)),squeeze_me=True,struct_as_record=False)
    p=m['param']
    print('=====',n); print('\n'.join(x.rstrip() for x in p.notes if x.strip()))
    for s in p.stimulus[:17]:
        d={k:(v if np.size(v)<6 else f'arr{np.shape(v)}') for k,v in s.param.__dict__.items() if k!='_fieldnames'}
        print(s.name,'|',s.description,'|',d)
EOF
```

```
===== asari-results-2/20061008-ha4-001/20061008-ha4-001-002.mat
Stimulus sequences are given as follows.
Seq.1:  16   1   9   1
Seq.2:  1   4   1  15   1
Seq.3:  5   1  11   1
Seq.4:  6  1  3  1
Seq.5:  10   1  17   1
Seq.6:  2   1  12   1
Seq.7:  14   1   8   1
Seq.8:  7   1  13   1
Effective repeats:  4
See also SoundTrans.m, DMRipple2.m, and MHTones.m.
Forgot to save the state of RANDN function.
natural sound (probe) | neotropical-mammals-1 Track 07 (Greater Spear-nosed Bat) From 10.6576 to 15.737 sec | {'ramp': 5, 'duration': 5079.370443188335, 'sf': 97656}
synthetic conditioning stimulus 1 | Modulated Harmonic Tone 1 | {'sf': 97656, 'm': 7, 'f0': 3000, 'duration': 5000, 'iniphase': 'arr(7,)', 'AMrange': array([], dtype=uint8), 'AMmean': 40, 'AMstd': 15, 'FMrange': array([], dtype=uint8), 'FMstd': 1000, 'ramp': 5}
synthetic conditioning stimulus 2 | Modulated Harmonic Tone 2 | {'sf': 97656, 'm': 7, 'f0': 3000, 'duration': 5000, 'iniphase': 'arr(7,)', 'AMrange': array([0, 4], dtype=uint8), 'AMmean': 40, 'AMstd': 15, 'FMrange': array([], dtype=uint8), 'FMstd': 1000, 'ramp': 5}
synthetic conditioning stimulus 3 | Modulated Harmonic Tone 3 | {'sf': 97656, 'm': 7, 'f0': 3000, 'duration': 5000, 'iniphase': 'arr(7,)', 'AMrange': array([ 4, 12], dtype=uint8), 'AMmean': 40, 'AMstd': 15, 'FMrange': array([], dtype=uint8), 'FMstd': 1000, 'ramp': 5}
synthetic conditioning stimulus 4 | Modulated Harmonic Tone 4 | {'sf': 97656, 'm': 7, 'f0': 3000, 'duration': 5000, 'iniphase': 'arr(7,)', 'AMrange': array([12, 24], dtype=uint8), 'AMmean': 40, 'AMstd': 15, 'FMrange': array([], dtype=uint8), 'FMstd': 1000, 'ramp': 5}
synthetic conditioning stimulus 5 | Modulated Harmonic Tone 5 | {'sf': 97656, 'm': 7, 'f0': 3000, 'duration': 5000, 'iniphase': 'arr(7,)', 'AMrange': array([], dtype=uint8), 'AMmean': 40, 'AMstd': 15, 'FMrange': array([0, 4], dtype=uint8), 'FMstd': 1000, 'ramp': 5}
synthetic conditioning stimulus 6 | Modulated Harmonic Tone 6 | {'sf': 97656, 'm': 7, 'f0': 3000, 'dur
[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; mkdir -p entries/asari-2009
```

```
Sun Nov 15 11:47:32 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "entries/asari-2009/ctxdep.py",
 "content": "\"\"\"Loading and context-dependence measures for CRCNS ac-1 (Asari and Zador 2009).\n\nThe data set is read from the public S3 bucket of CRCNS by range requests into\nits zip files (docs/archives.md, \"CRCNS\"); nothing is written to disk.\n\nWhere each parameter comes from:\n\n- Probe and context construction, the \"silence\" context (last 4 s of the\n  intersequence interval) and the \"silence probe\" (first 2.5 s after a\n  sequence), the rule that a probe needs at least two distinct contexts, the\n  truncation of every context to the smallest number of trials, the\n  Kruskal-Wallis significance with P < 0.01 for at least 5 ms, the noise\n  floor from 1000 trial shuffles, the fractional power estimates (Eqs. 17 to\n  19, each trial centred over the probe period) and the PSTH of the MGB units\n  (100-ms bins from probe onset, SD over contexts with n - 1) are ported from\n  the authors' analysis code deposited in the data set\n  (asari/Tools/CxtDep.m, GetEvoked.m, ViewResp.m in crcns-ac1.zip), and agree\n  with the paper's Methods (Analysis; Eqs. 10, 17 to 19, 42).\n- The 10-ms median filter that clips spikes: Methods, Analysis, paragraph 2,\n  and CxtDep.m (param.smooth = 10).\n- MGB spike extraction: the high-pass FIR filter, the automatic threshold\n  (two thirds of the largest filtered deflection) and the removal of\n  downward artefacts are ported from GetSpikes.m (automatic mode, which\n  ViewResp.m uses for cell-attached recordings); the Methods (Analysis,\n  paragraph 3) say only \"high-pass filter and thresholding\".\n- Time resolution: the paper works at 0.1 ms. Here the median-filtered\n  membrane potential is evaluated every 1 ms (the median over the 10-ms\n  window centred on each 1-ms point) and a significant period needs at least\n  5 consecutive 1-ms points (5 ms). This is a standard choice to keep the\n  1000-shuffle noise floor within the time limit; after a 10-ms median filter\n  the trace changes little within 1 ms. The notebook compares the two\n  resolutions on a subset of probes.\n- Ranks for the Kruskal-Wallis test use average ranks for ties (the code uses\n  ordinal ranks); a standard choice that cannot change a result beyond ties.\n\"\"\"\nfrom __future__ import annotations\n\nimport functools\nimport io\nimport re\nimport zipfile\nfrom dataclasses import dataclass, field\n\nimport fsspec\nimport numpy as np\nimport scipy.io as sio\nfrom scipy import ndimage, optimize, signal, stats\n\nBASE = \"https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-1/\"\nZIPS = [\"crcns-ac1.zip\", \"crcns-ac1-asari-results-1.zip\", \"crcns-ac1-asari-results-2.zip\"]\nSF = 10000          # recording sampling rate (Hz), checked against every file\nDEC = 10            # 10 kHz -> 1 kHz for the subthreshold analysis (see docstring)\nFS = SF // DEC      # analysis rate (Hz)\nMEDWIN = 100        # 10-ms median filter at 10 kHz (Methods; CxtDep.m)\nBLANK_PROBE = 2.5   # s, silence probe (CxtDep.m)\nBLANK_CONTEXT = 4.0 # s, silence context (CxtDep.m)\nALPHA = 0.01        # Methods, Significance measure\nMIN_RUN = 5         # 1-ms points = 5 ms (Methods: P < 0.01 for >= 5 ms)\nNSHUFFLE = 1000     # Methods: 1000 resamplings per probe\n\n# High-pass FIR filter of GetSpikes.m (ExtractSpikes)\nHP_NUM = np.array([-2.9419, -7.7633, -16.2976, -28.7498, -44.7001, -62.8034, -80.9099, -96.4457,\n                   -106.9520, 889.3317, -106.9520, -96.4457, -80.9099, -62.8034, -44.7001, -28.7498,\n                   -16.2976, -7.7633, -2.9419]) / 1000\n\n\n# ----------------------------------------------------------------------------- archive access\n@functools.lru_cache(maxsize=None)\ndef open_zip(name: str) -> zipfile.ZipFile:\n    return zipfile.ZipFile(fsspec.open(BASE + name, block_size=2**22).open())\n\n\ndef checksums() -> dict:\n    with fsspec.open(BASE + \"checksums.md5\", \"rt\") as f:\n        return {ln.split()[1]: ln.split()[0] for ln in f if ln.strip()}\n\n\ndef bucket_listing() -> list:\n    import urllib.request\n    xml = urllib.request.urlopen(BASE.replace(\"ac-1/\", \"\") + \"?list-type=2&prefix=ac-1/\").read().decode()\n    return re.findall(r\"<Key>(.*?)</Key>.*?<Size>(\\d+)</Size>\", xml)\n\n\n@functools.lru_cache(maxsize=None)\ndef member_index() -> dict:\n    \"\"\"Map 'Results/<cell>/<file>.mat' (as Summary.mat names files) to (zip, member).\"\"\"\n    idx = {}\n    for zn in ZIPS[1:]:\n        for n in open_zip(zn).namelist():\n            if n.endswith(\".mat\"):\n                idx[\"Results/\" + n.split(\"/\", 1)[1]] = (zn, n)\n    return idx\n\n\ndef loadmat_member(zn: str, member: str) -> dict:\n    return sio.loadmat(io.BytesIO(open_zip(zn).read(member)), squeeze_me=True, struct_as_record=False)\n\n\ndef _txt(x) -> str:\n    if isinstance(x, str):\n        return x.strip()\n    return \" \".join(str(s).strip() for s in np.atleast_1d(x))\n\n\ndef summary(who: str = \"asari\") -> list:\n    \"\"\"Experiment groups of <who>/Summary.mat: description and cells with their files.\"\"\"\n    m = loadmat_member(\"crcns-ac1.zip\", f\"{who}/Summary.mat\")\n    out = []\n    for e in np.atleast_1d(m[\"experiment\"]):\n        cells = []\n        for c in np.atleast_1d(e.cell):\n            files = [str(f) for f in np.atleast_1d(c.file)]\n            descs = [_txt(d) for d in np.atleast_1d(c.description)] if not isinstance(c.description, str) else [c.description]\n            cells.append(dict(cell=files[0].split(\"/\")[1], files=files, descriptions=descs))\n        out.append(dict(description=_txt(e.description), reference=_txt(getattr(e, \"reference\", \"\")), cells=cells))\n    return out\n\n\n# ----------------------------------------------------------------------------- one recording\n@dataclass\nclass Recording:\n    path: str\n    cell: str\n    rec_type: str\n    description: str\n    sf: int\n    unit: str\n    n_samples: int\n    triggers: list                      # (type, onset sample, duration samples, description)\n    notes: list\n    stimuli: list                       # stimulus structs (name, description, file, param)\n    durations: np.ndarray               # fragment durations in samples (CxtDep: round(ms/1000*sf))\n    rep: int | None                     # 'Effective repeats' in the notes\n    vm: np.ndarray | None = None        # median filtered, 1 kHz (mV)\n    raw: np.ndarray | None = None       # raw 10 kHz (mV), kept only when asked\n    meta: dict = field(default_factory=dict)\n\n\ndef _medfilt_decimated(x: np.ndarray) -> np.ndarray:\n    \"\"\"Median over the 10-ms window centred on every 10th sample (1 kHz output).\"\"\"\n    h = MEDWIN // 2\n    xp = np.concatenate([np.full(h, x[0]), x, np.full(h, x[-1])])\n    win = np.lib.stride_tricks.sliding_window_view(xp, MEDWIN)[::DEC]\n    out = np.empty(win.shape[0], dtype=np.float32)\n    for k in range(0, win.shape[0], 200_000):\n        out[k:k + 200_000] = np.median(win[k:k + 200_000], axis=1)\n    return out[: (len(x) + DEC - 1) // DEC]\n\n\ndef load_recording(path: str, keep_raw: bool = False, filtered: bool = True) -> Recording:\n    zn, member = member_index()[path]\n    m = loadmat_member(zn, member)\n    r, p = m[\"response\"], m[\"param\"]\n    x = r.trace.astype(np.float64) * float(r.scale)\n    trig = []\n    for t in np.atleast_1d(m[\"triggers\"]):\n        dur = getattr(t.param, \"duration\", 0)\n        trig.append((str(t.type), int(t.time), int(round(float(dur) / 1000 * r.sf)) if np.size(dur) == 1 else 0,\n                     _txt(getattr(t.param, \"description\", \"\"))))\n    notes = [str(s).rstrip() for s in np.atleast_1d(getattr(p, \"notes\", []))]\n    rep = None\n    for ln in notes:\n        if \"Effective repeats:\" in ln:\n            rep = int(ln.split(\":\")[1])\n    stim = list(np.atleast_1d(getattr(p, \"stimulus\", [])))\n    durs = np.array([int(round(float(s.param.duration) / 1000 * r.sf)) for s in stim]) if stim else np.array([], int)\n    rec = Recording(path=path, cell=path.split(\"/\")[1], rec_type=str(p.recording.type), description=_txt(p.ID.description),\n                    sf=int(r.sf), unit=str(r.unit), n_samples=len(x), triggers=trig, notes=notes, stimuli=stim,\n                    durations=durs, rep=rep)\n    rec.meta = dict(age=str(getattr(p.animal, \"age\", \"\")), animal=str(p.ID.animal), date=str(p.ID.date),\n                    Rs=str(getattr(p.recording, \"Rs\", \"\")), depth=str(getattr(p.recording, \"depth\", \"\")),\n                    vmin=float(x.min()), vmax=float(x.max()), vmedian=float(np.median(x[::100])))\n    if filtered:\n        rec.vm = _medfilt_decimated(x)\n    if keep_raw:\n        rec.raw = x\n    return rec\n\n\ndef sequence_segments(rec: Recording):\n    \"\"\"Port of GetEvoked.m: evoked (non-pulse triggers) and the silences between them.\n\n    Returns a list of presentations in time order: dict(seq=tuple of fragments, on, off,\n    pre=(start, end) of the silence before, post=(start, end) of the silence after),\n    all in 10-kHz samples.\n    \"\"\"\n    ev = [t for t in rec.triggers if \"pulse\" not in t[0]]\n    out = []\n    prev_end = 0\n    for k, (typ, on, dur, desc) in enumerate(ev):\n        nxt = ev[k + 1][1] if k + 1 < len(ev) else rec.n_samples\n        off = min(on + dur, rec.n_samples)\n        seq = None\n        if \":\" in desc and desc.lower().startswith(\"sequence\"):\n            seq = tuple(int(v) for v in desc.split(\":\", 1)[1].split())\n        out.append(dict(type=typ, desc=desc, seq=seq, on=on, off=off, pre=(prev_end, on), post=(off, nxt)))\n        prev_end = off\n    return out\n\n\n@dataclass\nclass Probe:\n    cell: str\n    path: str\n    probe: int            # fragment index (1-based), or 0 for the silence probe\n    contexts: list        # context fragment per group (0 = silence)\n    traces: list          # per context: (n_trials, T) arrays at 1 kHz (median filtered)\n    n_trials: list        # trials available per context before truncation\n    duration: float       # s\n    spikes: list | None = None   # per context: list of spike-time arrays (s, from probe onset)\n    kind: str = \"\"\n\n    @property\n    def rep(self) -> int:\n        return min(self.n_trials)\n\n\ndef build_probes(rec: Recording, include_silence_context: bool = True, include_silence_probe: bool = False,\n                 spikes: np.ndarray | None = None) -> list:\n    \"\"\"Port of CxtDep.m: all probes with at least two distinct contexts.\n\n    Trials of a context are pooled over the sequences where the pair occurs, the first\n    `Effective repeats` presentations of every sequence are used, and every context is\n    cut to the smallest number of trials (GetResp in CxtDep.m).\n    \"\"\"\n    segs = [s for s in sequence_segments(rec) if s[\"seq\"] is not None]\n    if not segs:\n        return []\n    by_seq = {}\n    for s in segs:\n        by_seq.setdefault(s[\"seq\"], []).append(s)\n    if rec.rep:\n        by_seq = {k: v[: rec.rep] for k, v in by_seq.items()}\n    durs = rec.durations\n    nfrag = len(durs)\n    # length of the silence windows: the shortest available (CxtDep.m)\n    bctx = min([BLANK_CONTEXT] + [(s[\"pre\"][1] - s[\"pre\"][0]) / SF for v in by_seq.values() for s in v])\n    bprb = min([BLANK_PROBE] + [(s[\"post\"][1] - s[\"post\"][0]) / SF for v in by_seq.values() for s in v])\n    occ = {}   # probe -> context -> list of (presentation, start sample of probe, length)\n    for seq, pres in by_seq.items():\n        if any(f < 1 or f > nfrag for f in seq):\n            continue\n        starts = np.concatenate([[0], np.cumsum([durs[f - 1] for f in seq])])\n        ext = [0] + list(seq)\n        for k, f in enumerate(seq):\n            ctx = ext[k]\n            if ctx == 0 and not include_silence_context:\n                continue\n            for s in pres:\n                occ.setdefault(f, {}).setdefault(ctx, []).append((s[\"on\"] + starts[k], durs[f - 1]))\n        if include_silence_probe:\n            for s in pres:\n                occ.setdefault(0, {}).setdefault(seq[-1], []).append((s[\"off\"], int(round(bprb * SF))))\n    probes = []\n    for f, ctxs in sorted(occ.items()):\n        if len(ctxs) < 2:\n            continue\n        cl = sorted(ctxs)\n        length = min(L for c in cl for _, L in ctxs[c])\n        T = length // DEC\n        traces, ntr, spk = [], [], []\n        for c in cl:\n            arr = []\n            sp = []\n            for st, _ in ctxs[c]:\n                i0 = st // DEC\n                seg = rec.vm[i0:i0 + T] if rec.vm is not None else None\n                if seg is not None and len(seg) == T:\n                    arr.append(seg)\n                if spikes is not None:\n                    sp.append((spikes[(spikes >= st) & (spikes < st + length)] - st) / SF)\n            traces.append(np.array(arr) if arr else np.zeros((len(ctxs[c]), 0)))\n            ntr.append(len(ctxs[c]))\n            spk.append(sp)\n        probes.append(Probe(cell=rec.cell, path=rec.path, probe=f, contexts=cl, traces=traces, n_trials=ntr,\n                            duration=length / SF, spikes=spk if spikes is not None else None,\n                            kind=\"silence\" if f == 0 else \"fragment\"))\n    return probes\n\n\n# ----------------------------------------------------------------------------- significance\ndef _runs_mask(b: np.ndarray, min_run: int = MIN_RUN) -> np.ndarray:\n    \"\"\"Keep only runs of True at least min_run long (along the last axis).\"\"\"\n    st = np.ones((1,) * (b.ndim - 1) + (min_run,), bool)\n    return ndimage.binary_opening(b, structure=st)\n\n\ndef kw_significance(p: Probe, contexts_subset=None, nshuffle: int = NSHUFFLE, rng=None, t_max: float | None = None):\n    \"\"\"Kruskal-Wallis across contexts at each 1-ms point; significant runs; noise floor.\n\n    Returns dict(p=p-values, sig=bool mask, noise=fraction of shuffles significant per point).\n    \"\"\"\n    idx = range(len(p.contexts)) if contexts_subset is None else [p.contexts.index(c) for c in contexts_subset]\n    rep = min(p.traces[i].shape[0] for i in idx)\n    X = np.concatenate([p.traces[i][:rep] for i in idx], axis=0).astype(np.float64)\n    if t_max is not None:\n        X = X[:, : int(round(t_max * FS))]\n    M = len(idx)\n    N = X.shape[0]\n    R = stats.rankdata(X, axis=0).astype(np.float32)\n    grp = np.repeat(np.arange(M), rep)\n\n    def kw_from(Rm):\n        rbar = Rm.reshape(M, rep, -1).mean(axis=1)\n        return 12 * ((rbar - (N + 1) / 2) ** 2).sum(axis=0) / (M * (N + 1))\n\n    kw = kw_from(R)\n    pval = stats.chi2.sf(kw, M - 1)\n    sig = _runs_mask(pval < ALPHA)\n    noise = None\n    if nshuffle:\n        rng = rng or np.random.default_rng(0)\n        crit = stats.chi2.isf(ALPHA, M - 1)\n        noise = np.zeros(X.shape[1])\n        B = 50\n        for b0 in range(0, nshuffle, B):\n            nb = min(B, nshuffle - b0)\n            G = np.zeros((nb * M, N), np.float32)\n            for j in range(nb):\n                perm = rng.permutation(N)\n                G[j * M + grp[perm], np.arange(N)] = 1.0 / rep\n            rbar = (G @ R).reshape(nb, M, -1)\n            kws = 12 * ((rbar - (N + 1) / 2) ** 2).sum(axis=1) / (M * (N + 1))\n            noise += _runs_mask(kws > crit).sum(axis=0)\n        noise /= nshuffle\n    return dict(p=pval, sig=sig, noise=noise, rep=rep, n_ctx=M)\n\n\n# ----------------------------------------------------------------------------- fractional power\ndef frac_power(p: Probe, contexts_subset=None, t_max: float | None = None):\n    \"\"\"Port of FracPow (CxtDep.m): Eqs. 17 (predictable), 18 (invariant) per time point.\"\"\"\n    idx = range(len(p.contexts)) if contexts_subset is None else [p.contexts.index(c) for c in contexts_subset]\n    rep = min(p.traces[i].shape[0] for i in idx)\n    X = np.stack([p.traces[i][:rep] for i in idx]).astype(np.float64)   # (n, rep, T)\n    if t_max is not None:\n        X = X[:, :, : int(round(t_max * FS))]\n    X = X - X.mean(axis=2, keepdims=True)          # each trial centred over the probe period\n    n = X.shape[0]\n    mk = X.mean(axis=1)                              # (n, T)\n    pred = ((rep * mk ** 2 - (X ** 2).mean(axis=1)) / (rep - 1)).mean(axis=0)\n    inv = (n * mk.mean(axis=0) ** 2 - (mk ** 2).mean(axis=0)) / (n - 1)\n    return dict(pred=pred, inv=inv, dep=pred - inv, total=(X ** 2).mean(axis=(0, 1)))\n\n\ndef stack_curves(curves: list, T: int, fill=np.nan) -> np.ndarray:\n    out = np.full((len(curves), T), fill, dtype=float)\n    for i, c in enumerate(curves):\n        L = min(len(c), T)\n        out[i, :L] = c[:L]\n    return out\n\n\ndef running_mean_0_2t(x: np.ndarray) -> np.ndarray:\n    \"\"\"Mean of x over [0, 2t] at each t (Methods, Eq. 20), truncated at the end of x.\"\"\"\n    c = np.concatenate([[0], np.nancumsum(x)])\n    cnt = np.concatenate([[0], np.cumsum(~np.isnan(x))])\n    t = np.arange(len(x))\n    hi = np.minimum(2 * t + 1, len(x))\n    return (c[hi] - c[0]) / np.maximum(cnt[hi], 1)\n\n\n# ----------------------------------------------------------------------------- curve fits\ndef fit_exp(t, y, n_exp: int, kappa=None, starts=None):\n    \"\"\"Least-squares fit of Eq. 44, sum_k a_k exp(-t/tau_k) + kappa, over a grid of starts.\n\n    kappa fixed when a number is given, free when None. Taus bounded to [1 ms, 100 s].\n    \"\"\"\n    t = np.asarray(t, float)\n    y = np.asarray(y, float)\n    ok = np.isfinite(y)\n    t, y = t[ok], y[ok]\n    free_k = kappa is None\n\n    def model(th):\n        a = th[0:2 * n_exp:2]\n        tau = th[1:2 * n_exp:2]\n        k = th[-1] if free_k else kappa\n        return (a[:, None] * np.exp(-t[None, :] / tau[:, None])).sum(axis=0) + k\n\n    taus = [0.03, 0.1, 0.3, 1.0, 3.0]\n    best = None\n    grid = starts or ([(a, b) for a in taus for b in taus if b > a] if n_exp == 2 else [(a,) for a in taus])\n    for g in grid:\n        th0 = []\n        for tau in g:\n            th0 += [float(y[0] - (np.nanmean(y[-10:]) if free_k else kappa)) / n_exp, tau]\n        lo = [-np.inf, 1e-3] * n_exp\n        hi = [np.inf, 100.0] * n_exp\n        if free_k:\n            th0.append(float(np.nanmean(y[-10:])))\n            lo.append(-np.inf)\n            hi.append(np.inf)\n        try:\n            res = optimize.least_squares(lambda th: model(th) - y, th0, bounds=(lo, hi))\n        except Exception:\n            continue\n        if best is None or res.cost < best.cost:\n            best = res\n    th = best.x\n    comps = sorted([(th[2 * k], th[2 * k + 1]) for k in range(n_exp)], key=lambda z: z[1])\n    return dict(alpha=[c[0] for c in comps], tau=[c[1] for c in comps], kappa=th[-1] if free_k else kappa,\n                sse=2 * best.cost, n=len(t))\n\n\ndef fit_with_rule(t, y, kappa=None):\n    \"\"\"Two exponentials if each size is at least a tenth of the total (Methods, Eq. 44), else one.\"\"\"\n    f2 = fit_exp(t, y, 2, kappa)\n    tot = sum(abs(a) for a in f2[\"alpha\"])\n    if all(abs(a) >= tot / 10 for a in f2[\"alpha\"]):\n        f2[\"n_exp\"] = 2\n        return f2, fit_exp(t, y, 1, kappa)\n    f1 = fit_exp(t, y, 1, kappa)\n    f1[\"n_exp\"] = 1\n    return f1, f2\n\n\n# ----------------------------------------------------------------------------- spikes\ndef extract_spikes(raw: np.ndarray, threshold: float | None = None, remove_downward: bool = True) -> np.ndarray:\n    \"\"\"Port of ExtractSpikes in GetSpikes.m (automatic mode). Returns spike sample indices.\"\"\"\n    f = signal.filtfilt(HP_NUM, [1.0], raw)\n    if threshold is None:\n        i = int(np.argmax(np.abs(f)))\n        threshold = 2 / 3 * abs(f[i])\n        if threshold > 100:\n            mask = np.ones(len(f), bool)\n            mask[max(0, i - 30): i + 31] = False\n            threshold = np.abs(f[mask]).max() * 2 / 3\n    above = f > threshold\n    if not above.any():\n        return np.array([], int)\n    lab, n = ndimage.label(above)\n    peaks = np.array(ndimage.maximum_position(f, lab, np.arange(1, n + 1))).ravel().astype(int)\n    if remove_downward and len(peaks):\n        h = f[peaks]\n        mins = np.array([f[max(0, k - 10): k + 11].min() for k in peaks])\n        peaks = peaks[~(mins < -h)]\n    return peaks\n\n\ndef psth_sd(p: Probe, dt: float = 0.1, nbins: int = 61):\n    \"\"\"Port of psth() in CxtDep.m: PSTH per context (bins from probe onset), SD over contexts.\"\"\"\n    rep = min(len(s) for s in p.spikes)\n    edges = np.arange(nbins + 1) * dt\n    T = int(np.floor(p.duration / dt + 1e-9)) + 1    # histc bins t = 0:dt:Tend\n    H = []\n    for sp in p.spikes:\n        allsp = np.concatenate(sp[:rep]) if rep else np.array([])\n        allsp = allsp[(allsp > 0) & (allsp <= p.duration)]\n        h, _ = np.histogram(allsp, bins=edges)\n        H.append(h / rep / dt)\n    H = np.array(H)[:, :min(T, nbins)]\n    return dict(psth=H, sd=H.std(axis=0, ddof=1), rep=rep)\n"
}
```

```
File created successfully at: entries/asari-2009/ctxdep.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/asari-2009; . $TMPDIR/dev/bin/activate; python - <<'EOF'
import time, resource, ctxdep as cd, numpy as np
S=cd.summary()
g=S[0]; print(g['description'], len(g['cells']))
c=g['cells'][0]; print(c)
t0=time.time()
rec=cd.load_recording(c['files'][1]); print('load',time.time()-t0, rec.rep, rec.durations, len(rec.vm))
segs=cd.sequence_segments(rec); print(len(segs), segs[0])
for inc in [True, False]:
    P=cd.build_probes(rec, include_silence_context=inc)
    print(inc, [(p.probe,p.contexts,p.n_trials,p.duration) for p in P])
P=cd.build_probes(rec)
t0=time.time(); r=cd.kw_significance(P[0]); print('kw',time.time()-t0, r['sig'].mean(), r['noise'].mean(), r['rep'])
fp=cd.frac_power(P[0]); print({k:np.nanmean(v) for k,v in fp.items()})
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,'GB')
EOF
```

```
Auditory cortical cell responses to natural sound combinations. 39
{'cell': '20051101-ha1-005', 'files': ['Results/20051101-ha1-005/20051101-ha1-005-001.mat', 'Results/20051101-ha1-005/20051101-ha1-005-003.mat'], 'descriptions': ['tuning curve', 'Natural Sounds: combinations of 4 stimuli (class5)']}
load 1.5621111392974854 6 [41070 42000 39700 49800] 749972
28 {'type': 'naturalsound', 'desc': 'Sequence 1: 2  1  3  1  4', 'seq': (2, 1, 3, 1, 4), 'on': 55126, 'off': 268766, 'pre': (0, 55126), 'post': (268766, 322329)}
True [(1, [0, 1, 2, 3, 4], [6, 6, 6, 6, 6], np.float64(4.107)), (2, [0, 1, 2, 3, 4], [6, 6, 6, 6, 6], np.float64(4.2)), (3, [0, 1, 2, 3, 4], [6, 6, 6, 6, 6], np.float64(3.97)), (4, [0, 1, 2, 3, 4], [6, 6, 6, 6, 6], np.float64(4.98))]
False [(1, [1, 2, 3, 4], [6, 6, 6, 6], np.float64(4.107)), (2, [1, 2, 3, 4], [6, 6, 6, 6], np.float64(4.2)), (3, [1, 2, 3, 4], [6, 6, 6, 6], np.float64(3.97)), (4, [1, 2, 3, 4], [6, 6, 6, 6], np.float64(4.98))]
kw 0.11295843124389648 0.01704407109812515 0.0031383004626247876 6
{'pred': np.float64(5.383665930339733), 'inv': np.float64(5.186817520879776), 'dep': np.float64(0.1968484094599575), 'total': np.float64(11.331174923936226)}
0.46122 GB
```

**Agent calls Bash**

```bash
cd entries/asari-2009; . $TMPDIR/dev/bin/activate; cat > $TMPDIR/nat.py <<'EOF'
import time, resource, ctxdep as cd, numpy as np, pickle, collections
S=cd.summary()
g=S[0]
t0=time.time(); out=[]
for c in g['cells']:
    for f,d in zip(c['files'],c['descriptions']):
        if d=='tuning curve': continue
        rec=cd.load_recording(f)
        for inc in [True, False]:
            P=cd.build_probes(rec, include_silence_context=inc, include_silence_probe=inc)
            for p in P:
                r=cd.kw_significance(p, rng=np.random.default_rng(len(out)))
                fp=cd.frac_power(p)
                out.append(dict(cell=p.cell,path=p.path,desc=d,probe=p.probe,ctx=p.contexts,ntr=p.n_trials,dur=p.duration,
                                silence=inc,sig=r['sig'],noise=r['noise'],p=r['p'],rep=r['rep'],**fp))
    print(c['cell'], len(out), round(time.time()-t0), flush=True)
pickle.dump(out,open('/tmp/claude-1001/nat.pkl','wb'))
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,'GB')
EOF
python $TMPDIR/nat.py 2>&1 | tail -8
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/nat.py", line 1, in <module>
    import time, resource, ctxdep as cd, numpy as np, pickle, collections
ModuleNotFoundError: No module named 'ctxdep'
```

**Agent calls Bash**

```bash
cd entries/asari-2009; . $TMPDIR/dev/bin/activate; PYTHONPATH=. python $TMPDIR/nat.py 2>&1 | tail -8
```

```
20060320-ha3-003 577 131
20060329-ha1-001 592 135
20060402-ha1-001 607 139
20060430-ha1-001 609 141
20061006-ha1-001 624 145
20061007-ha2-001 639 149
20061007-ha4-001 654 152
0.863312 GB
```

**Agent calls Bash**

```bash
cd $TMPDIR; . dev/bin/activate; python - <<'EOF'
import pickle, numpy as np, collections
out=pickle.load(open('nat.pkl','rb'))
for inc in [True,False]:
    P=[o for o in out if o['silence']==inc and o['probe']!=0]
    ok=[o for o in P if o['rep']>=4]
    cells=set(o['cell'] for o in ok)
    print('silence',inc,'probes',len(P),'rep>=4',len(ok),'cells',len(cells), 'rep<4 cells', len(set(o['cell'] for o in P))-len(cells))
    nsig=sum(o['sig'].any() for o in ok); print('  significant',nsig, nsig/len(ok))
    print('  reps',collections.Counter(o['rep'] for o in P))
    print('  nctx',collections.Counter(len(o['ctx']) for o in ok))
    print('  by desc', collections.Counter(o['desc'] for o in ok))
EOF
```

```
silence True probes 305 rep>=4 305 cells 39 rep<4 cells 0
  significant 187 0.6131147540983607
  reps Counter({4: 113, 6: 59, 7: 58, 5: 44, 8: 16, 9: 7, 12: 4, 10: 4})
  nctx Counter({3: 114, 7: 54, 5: 53, 8: 48, 11: 25, 10: 9, 19: 2})
  by desc Counter({'Natural Sounds: combinations of 7 long stimuli': 168, 'Natural Sounds: combinations of 5 short stimuli (each with 2 intensities)': 40, 'Natural Sounds: combinations of 6 stimuli (one of each class)': 30, 'Natural Sounds: combinations of 3 stimuli (each with 3 intensities; class 6)': 18, 'Natural Sounds: combinations of 4 stimuli (class5)': 12, 'Natural Sounds: combinations of 4 stimuli (class6)': 12, 'Natural Sounds: combinations of 10 short stimuli': 10, 'Natural Sounds: combinations of 3 stimuli (each with 3 intensities; class 4)': 9, 'Natural Sounds: combinations of 4 stimuli (class4)': 4, 'Natural Sounds: combinations of one probe (class2-2) and many contexts': 2})
silence False probes 305 rep>=4 305 cells 39 rep<4 cells 0
  significant 169 0.5540983606557377
  reps Counter({4: 113, 6: 59, 7: 58, 5: 44, 8: 16, 9: 7, 12: 4, 10: 4})
  nctx Counter({2: 111, 6: 54, 4: 53, 7: 48, 10: 25, 9: 9, 3: 3, 18: 2})
  by desc Counter({'Natural Sounds: combinations of 7 long stimuli': 168, 'Natural Sounds: combinations of 5 short stimuli (each with 2 intensities)': 40, 'Natural Sounds: combinations of 6 stimuli (one of each class)': 30, 'Natural Sounds: combinations of 3 stimuli (each with 3 intensities; class 6)': 18, 'Natural Sounds: combinations of 4 stimuli (class5)': 12, 'Natural Sounds: combinations of 4 stimuli (class6)': 12, 'Natural Sounds: combinations of 10 short stimuli': 10, 'Natural Sounds: combinations of 3 stimuli (each with 3 intensities; class 4)': 9, 'Natural Sounds: combinations of 4 stimuli (class4)': 4, 'Natural Sounds: combinations of one probe (class2-2) and many contexts': 2})
Shell cwd was reset to
```

**Agent**

305 probes in 39 cells, matching the paper exactly; 187 significant (paper 204, within tolerance). Now the population curves and fits.

**Agent calls Bash**

```bash
cd entries/asari-2009; . $TMPDIR/dev/bin/activate; PYTHONPATH=. python - <<'EOF'
import pickle, numpy as np, ctxdep as cd
out=pickle.load(open('/tmp/claude-1001/nat.pkl','rb'))
FS=cd.FS
for inc in [True,False]:
    P=[o for o in out if o['silence']==inc and o['probe']!=0]
    T=int(6.1*FS)
    S=cd.stack_curves([o['sig'].astype(float) for o in P],T)
    N=cd.stack_curves([o['noise'] for o in P],T)
    t=np.arange(T)/FS
    for den in ['all','running']:
        if den=='all': prop=np.nan_to_num(S).sum(0)/len(P); nf=np.nan_to_num(N).sum(0)/len(P)
        else: prop=np.nanmean(S,0); nf=np.nanmean(N,0)
        corr=prop-nf; cum=np.cumsum(corr); 
        ipk=np.argmax(cum); cumn=cum/cum[ipk]
        late=1-cumn[int(1*FS)]
        kappa=np.nanmean(nf[:int(4.72*FS)])
        for tmax in [4.72,6.0]:
            m=t<=tmax
            f,alt=cd.fit_with_rule(t[m],prop[m],kappa=kappa)
            print(inc,den,'late',round(late,3),'peak',t[ipk],'kappa',round(kappa,5),'tmax',tmax,f['n_exp'],np.round(f['alpha'],3),np.round(f['tau'],3), 'alt',np.round(alt['alpha'],3),np.round(alt['tau'],3))
    # frac power
    for den in ['running']:
        pred=np.nanmean(cd.stack_curves([o['pred'] for o in P],T),0)
        dep=np.nanmean(cd.stack_curves([o['dep'] for o in P],T),0)
        inv=np.nanmean(cd.stack_curves([o['inv'] for o in P],T),0)
        ps=cd.running_mean_0_2t(pred)
        Q=dep/ps; U=inv/ps; U2=inv/pred
        for tmax in [4.0,6.0]:
            m=t<=tmax
            f=cd.fit_exp(t[m],Q[m],1,kappa=0.0); g=cd.fit_exp(t[m],U[m],1,kappa=1.0); g2=cd.fit_exp(t[m],U2[m],1,kappa=1.0)
            print(' Q',inc,tmax,np.round(f['alpha'],3),np.round(f['tau'],3),' U',np.round(1+g['alpha'][0],3),np.round(g['tau'],3),' Unsm',np.round(1+g2['alpha'][0],3),np.round(g2['tau'],3))
EOF
```

```
<stdin>:12: RuntimeWarning: Mean of empty slice
<stdin>:23: RuntimeWarning: Mean of empty slice
<stdin>:24: RuntimeWarning: Mean of empty slice
<stdin>:25: RuntimeWarning: Mean of empty slice
True all late 0.251 peak 4.781 kappa 0.00258 tmax 4.72 2 [0.151 0.079] [0.253 0.975] alt [0.205] [0.502]
True all late 0.251 peak 4.781 kappa 0.00258 tmax 6.0 2 [0.148 0.082] [0.25 0.95] alt [0.205] [0.502]
True running late nan peak 6.06 kappa 0.00293 tmax 4.72 2 [0.162 0.068] [0.266 1.087] alt [0.205] [0.5]
True running late nan peak 6.06 kappa 0.00293 tmax 6.0 2 [0.158 0.072] [0.261 1.04 ] alt [0.205] [0.5]
 Q True 4.0 [0.47] [1.732]  U 0.43 [2.317]  Unsm 0.498 [1.908]
 Q True 6.0 [0.466] [1.775]  U 0.466 [2.808]  Unsm 0.498 [1.91]
False all late 0.177 peak 3.419 kappa 0.00286 tmax 4.72 1 [0.166] [0.316] alt [0.158 0.015] [0.261 1.34 ]
False all late 0.177 peak 3.419 kappa 0.00286 tmax 6.0 1 [0.166] [0.316] alt [0.156 0.017] [0.258 1.189]
False running late nan peak 6.06 kappa 0.00327 tmax 4.72 1 [0.166] [0.313] alt [0.159 0.013] [0.262 1.491]
False running late nan peak 6.06 kappa 0.00327 tmax 6.0 1 [0.166] [0.313] alt [0.157 0.015] [0.259 1.278]
 Q False 4.0 [0.454] [1.272]  U 0.466 [1.861]  Unsm 0.534 [1.475]
 Q False 6.0 [0.452] [1.284]  U 0.49 [2.109]  Unsm 0.53 [1.447]
```

**Agent calls Bash**

```bash
cd entries/asari-2009; . $TMPDIR/dev/bin/activate; cat > $TMPDIR/mgb.py <<'EOF'
import pickle, numpy as np, ctxdep as cd, time, collections
S=cd.summary(); g=S[1]
out=[]; rates=[]
t0=time.time()
for c in g['cells']:
    for f,d in zip(c['files'],c['descriptions']):
        rec=cd.load_recording(f, keep_raw=True, filtered=False)
        sp=cd.extract_spikes(rec.raw)
        segs=cd.sequence_segments(rec)
        ev=sum(s['off']-s['on'] for s in segs); nev=sum(((sp>=s['on'])&(sp<s['off'])).sum() for s in segs)
        spont=sum(s['pre'][1]-s['pre'][0] for s in segs)+ (segs[-1]['post'][1]-segs[-1]['post'][0] if segs else 0)
        nsp=sum(((sp>=s['pre'][0])&(sp<s['pre'][1])).sum() for s in segs)+(((sp>=segs[-1]['post'][0])&(sp<segs[-1]['post'][1])).sum() if segs else 0)
        rates.append(dict(cell=c['cell'],desc=d,ev_rate=nev/ev*cd.SF if ev else np.nan,sp_rate=nsp/spont*cd.SF if spont else np.nan,nspk=len(sp),ev=ev/cd.SF,spont=spont/cd.SF))
        if d=='tuning curve': continue
        for inc in [True,False]:
            for p in cd.build_probes(rec, include_silence_context=inc, spikes=sp):
                r=cd.psth_sd(p)
                out.append(dict(cell=p.cell,path=p.path,probe=p.probe,ctx=p.contexts,ntr=p.n_trials,dur=p.duration,silence=inc,rep=r['rep'],sd=r['sd'],psth=r['psth']))
    print(c['cell'],round(time.time()-t0),flush=True)
pickle.dump((out,rates),open('/tmp/claude-1001/mgb.pkl','wb'))
EOF
PYTHONPATH=. python $TMPDIR/mgb.py | tail -3; python - <<'EOF'
import pickle, numpy as np, collections
out,rates=pickle.load(open('/tmp/claude-1001/mgb.pkl','rb'))
import pandas as pd
R=pd.DataFrame(rates); print(R.groupby('desc')[['ev_rate','sp_rate']].mean())
seqR=R[R.desc!='tuning curve'].groupby('cell')[['ev_rate','sp_rate']].mean(); print('seq files', seqR.mean().round(3).to_dict(), seqR.std().round(3).to_dict())
allR=R.groupby('cell').apply(lambda d: pd.Series(dict(ev=(d.ev_rate*d.ev).sum()/d.ev.sum(), sp=(d.sp_rate*d.spont).sum()/d.spont.sum()))); print('all files',allR.mean().round(3).to_dict(),allR.std().round(3).to_dict())
for inc in [True,False]:
    P=[o for o in out if o['silence']==inc]
    ok=[o for o in P if o['rep']>=10]
    print(inc,len(P),len(ok),len(set(o['cell'] for o in ok)), collections.Counter(o['rep'] for o in P))
EOF
```

```
20071012-ha1-002 107
20071012-ha1-003 113
20071012-ha1-004 119
                                                      ev_rate   sp_rate
desc                                                                   
Natural Sounds: combinations of 4 stimuli (class4)  54.112492  1.524291
Natural Sounds: combinations of 4 stimuli (class5)   3.110062  1.198835
Natural Sounds: combinations of 4 stimuli (class6)   1.229984  0.089716
Natural Sounds: combinations of 7 long stimuli      12.469158  1.695527
tuning curve                                        11.664332  0.868312
seq files {'ev_rate': 5.082, 'sp_rate': 0.554} {'ev_rate': 11.738, 'sp_rate': 1.238}
all files {'ev': 5.072, 'sp': 0.618} {'ev': 11.456, 'sp': 1.134}
True 93 93 14 Counter({20: 16, 21: 16, 10: 14, 19: 8, 23: 8, 24: 8, 17: 7, 22: 4, 25: 4, 15: 4, 13: 4})
False 93 93 14 Counter({20: 16, 21: 16, 10: 14, 19: 8, 23: 8, 24: 8, 17: 7, 22: 4, 25: 4, 15: 4, 13: 4})
```

**Agent**

MGB: 93 probes in 14 cells, matching exactly. Now checking A1 spike detection on whole-cell traces.

**Agent calls Bash**

```bash
date -u; cd entries/asari-2009; . $TMPDIR/dev/bin/activate; PYTHONPATH=. python - <<'EOF'
import numpy as np, ctxdep as cd
from scipy import signal
S=cd.summary()
for f in [S[0]['cells'][0]['files'][1], S[0]['cells'][10]['files'][1], S[2]['cells'][5]['files'][1]]:
    rec=cd.load_recording(f, keep_raw=True)
    base=np.repeat(rec.vm, cd.DEC)[:rec.n_samples]
    res=rec.raw-base
    pk,_=signal.find_peaks(res, height=5, distance=20)
    h=res[pk]
    print(f, rec.meta['vmedian'], rec.meta['vmax'], 'peaks>5',len(pk), [int((h>x).sum()) for x in (10,15,20,30)], np.percentile(h,[50,90,99]).round(1) if len(h) else None, rec.n_samples/1e4)
EOF
```

```
Sun Nov 15 11:54:36 UTC 2026
Results/20051101-ha1-005/20051101-ha1-005-003.mat -50.458533607995726 -4.254215304798962 peaks>5 1063 [840, 828, 807, 121] [26.  30.2 32. ] 749.972
Results/20051127-ha1-002/20051127-ha1-002-002.mat -59.80010681315328 -0.6256198977645533 peaks>5 722 [614, 323, 213, 68] [13.8 29.7 38. ] 942.689
Results/20061125-ha1-001/20061125-ha1-001-002.mat -78.12619211108567 -9.308003356984816 peaks>5 340 [340, 339, 209, 46] [20.5 32.3 40.9] 1109.8057
```

**Agent**

Core natural-sound and MGB pipelines work and run fast. Next I'll try to reconstruct the property groups of the synthetic ensembles (Figure 8) from the stimulus parameters.

**Agent calls Bash**

```bash
cd entries/asari-2009; . $TMPDIR/dev/bin/activate; PYTHONPATH=. python - <<'EOF' > $TMPDIR/synth_designs.txt
import numpy as np, ctxdep as cd, collections
S=cd.summary(); g=S[2]
seen={}
for c in g['cells']:
    for f,d in zip(c['files'],c['descriptions']):
        if d=='tuning curve': continue
        zn,mem=cd.member_index()[f]
        m=cd.loadmat_member(zn,mem); p=m['param']
        st=list(np.atleast_1d(p.stimulus))
        def key(s):
            d={k:v for k,v in s.param.__dict__.items() if k not in ('_fieldnames','iniphase','sinphase','tempmod','specmod','envphase','sf','ramp')}
            return ' '.join(f"{k}={np.round(v,3).tolist() if np.size(v)>0 and np.asarray(v).dtype.kind in 'fiu' else v}" for k,v in d.items())
        sig=(d, tuple(s.description if isinstance(s.description,str) else '' for s in st), tuple(key(s) for s in st))
        seqs=[ln.strip() for ln in p.notes if ln.strip().startswith('Seq')]
        seen.setdefault(sig,[]).append((c['cell'],f.split('/')[-1],seqs))
for sig,v in seen.items():
    print('#####',len(v),'files',sig[0]); print('   cells', [x[0]+'/'+x[1] for x in v])
    print('   seqs', ' | '.join(v[0][2]))
    for i,(a,b) in enumerate(zip(sig[1],sig[2])): print('   ',i+1,a[:40],'|',b)
EOF
wc -l $TMPDIR/synth_designs.txt; head -150 $TMPDIR/synth_designs.txt
```

```
981 /tmp/claude-1001/synth_designs.txt
##### 1 files Natural sound probe following synthetic sound variants (amplitude, frequency, amplitude-, and frequency-modulation)
   cells ['20061022-ha4-001/20061022-ha4-001-002.mat']
   seqs Seq.1:  9  1 | Seq.2:  15   1 | Seq.3:  18   1 | Seq.4:  16   1 | Seq.5:  2  1 | Seq.6:  11   1 | Seq.7:  6  1 | Seq.8:  5  1 | Seq.9:  4  1 | Seq.10:  12   1 | Seq.11:  8  1 | Seq.12:  13   1 | Seq.13:  10   1 | Seq.14:  7  1 | Seq.15:  17   1 | Seq.16:  14   1 | Seq.17:  19   1 | Seq.18:  3  1
    1 neotropical-mammals-2 Track 06 (Buffy-he | duration=5475.014
    2 Modulated Harmonic Tone 1 | m=5 df=0.5 f0=2121.32 duration=5000 AMrange=[4, 12] AMmean=64 AMstd=10 FMrange=[4, 12] FMstd=0.333
    3 Modulated Harmonic Tone 2 | m=5 df=0.5 f0=2121.32 duration=5000 AMrange=[4, 12] AMmean=44 AMstd=10 FMrange=[4, 12] FMstd=0.333
    4 Modulated Harmonic Tone 3 | m=5 df=0.5 f0=2121.32 duration=5000 AMrange=[4, 12] AMmean=24 AMstd=10 FMrange=[4, 12] FMstd=0.333
    5 Modulated Harmonic Tone 4 | m=5 df=0.5 f0=2121.32 duration=5000 AMrange=[4, 12] AMmean=4 AMstd=10 FMrange=[4, 12] FMstd=0.333
    6 Modulated Harmonic Tone 5 | m=5 df=0.5 f0=750 duration=5000 AMrange=[4, 12] AMmean=54 AMstd=10 FMrange=[4, 12] FMstd=0.333
    7 Modulated Harmonic Tone 6 | m=5 df=0.5 f0=1261.345 duration=5000 AMrange=[4, 12] AMmean=54 AMstd=10 FMrange=[4, 12] FMstd=0.333
    8 Modulated Harmonic Tone 7 | m=5 df=0.5 f0=2121.32 duration=5000 AMrange=[4, 12] AMmean=54 AMstd=10 FMrange=[4, 12] FMstd=0.333
    9 Modulated Harmonic Tone 8 | m=5 df=0.5 f0=3567.621 duration=5000 AMrange=[4, 12] AMmean=54 AMstd=10 FMrange=[4, 12] FMstd=0.333
    10 Modulated Harmonic Tone 9 | m=5 df=0.5 f0=6000 duration=5000 AMrange=[4, 12] AMmean=54 AMstd=10 FMrange=[4, 12] FMstd=0.333
    11 Modulated Harmonic Tone 10 | m=5 df=0.5 f0=2121.32 duration=5000 AMrange=[0, 4] AMmean=54 AMstd=10 FMrange=[4, 12] FMstd=0.333
    12 Modulated Harmonic Tone 11 | m=5 df=0.5 f0=2121.32 duration=5000 AMrang
[... 135 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "#####\|cells\|seqs" $TMPDIR/synth_designs.txt | sed -n 20,200p | cut -c1-400
```

```
121:   cells ['20061125-ha2-003/20061125-ha2-003-002.mat']
122:   seqs Seq.1:  2  1  6  6  1  4  4 | Seq.2:  1  5  1  2  2  3  1 | Seq.3:  4  1  1  3  2  6  2 | Seq.4:  5  4  2  5  2  4  6 | Seq.5:  3  4  3  5  6  4  5 | Seq.6:  6  3  6  5  5  3  3
129:##### 1 files Combinations of 6 naturalistic sounds
130:   cells ['20061201-ha2-001/20061201-ha2-001-002.mat']
131:   seqs Seq.1:  2  1  6  6  1  4  4 | Seq.2:  1  5  1  2  2  3  1 | Seq.3:  4  1  1  3  2  6  2 | Seq.4:  5  4  2  5  2  4  6 | Seq.5:  3  4  3  5  6  4  5 | Seq.6:  6  3  6  5  5  3  3
138:##### 3 files Combinations of 6 synthetic sounds
139:   cells ['20060202-ha2-001/20060202-ha2-001-002.mat', '20060202-ha2-002/20060202-ha2-002-002.mat', '20060212-ha1-001/20060212-ha1-001-003.mat']
140:   seqs Seq.1:  2  1  6  6  1  4  4 | Seq.2:  1  5  1  2  2  3  1 | Seq.3:  4  1  1  3  2  6  2 | Seq.4:  5  4  2  5  2  4  6 | Seq.5:  3  4  3  5  6  4  5 | Seq.6:  6  3  6  5  5  3  3
147:##### 4 files Combinations of 6 synthetic sounds
148:   cells ['20060202-ha3-004/20060202-ha3-004-002.mat', '20060212-ha1-001/20060212-ha1-001-002.mat', '20060212-ha2-001/20060212-ha2-001-002.mat', '20060216-ha2-002/20060216-ha2-002-002.mat']
149:   seqs Seq.1:  2  1  6  6  1  4  4 | Seq.2:  1  5  1  2  2  3  1 | Seq.3:  4  1  1  3  2  6  2 | Seq.4:  5  4  2  5  2  4  6 | Seq.5:  3  4  3  5  6  4  5 | Seq.6:  6  3  6  5  5  3  3
156:##### 1 files Combinations of 4 synthetic sounds
157:   cells ['20060313-ha1-001/20060313-ha1-001-003.mat']
158:   seqs Seq.1:  1  1  2  3  3 | Seq.2:  2  4  4  2  1 | Seq.3:  3  4  3  2  2 | Seq.4:  4  1  3  1  4
187:##### 1 files Combinations of 4 synthetic sounds
188:   cells ['20060313-ha1-002/20060313-ha1-002-002.mat']
189:   seqs Seq.1:  1  1  2  3  3 | Seq.2:  2  4  4  2  1 | Seq.3:  3  4  3  2  2 | Seq.4:  4  1  3  1  4
218:##### 1 files Combinations of 4 synthetic sounds
219:   cells ['20060313-ha1-003/20060313-ha1-003-002.mat']
220:   seqs Seq.1:  1  1  2  3  3 | Seq.2:  2  4  4  2  1 | Seq.3:  3
[... 120 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 699,760p $TMPDIR/synth_designs.txt | cut -c1-250; grep -n "DMR1" -A6 $TMPDIR/synth_designs.txt | cut -c1-200 | head
```

```
seqs Seq.1:  13   1   7   1 | Seq.2:  1  8  1  2  1 | Seq.3:  9  1  6  1 | Seq.4:  12   1  10   1 | Seq.5:  4  1  3  1 | Seq.6:  5   1  11   1
    1 neotropical-mammals-1 Track 07 (Greater  | duration=5079.37
    2 DMR; frequency variants | SFtemp=3 SFspec=6 dx=0.016 ff=[250, 1000] duration=5000
    3 DMR; frequency variants | SFtemp=3 SFspec=6 dx=0.016 ff=[500, 2000] duration=5000
    4 DMR; frequency variants | SFtemp=3 SFspec=6 dx=0.016 ff=[1000, 4000] duration=5000
    5 DMR; frequency variants | SFtemp=3 SFspec=6 dx=0.016 ff=[2000, 8000] duration=5000
    6 DMR; frequency variants | SFtemp=3 SFspec=6 dx=0.016 ff=[4000, 16000] duration=5000
    7 DMR; frequency variants | SFtemp=3 SFspec=6 dx=0.016 ff=[8000, 32000] duration=5000
    8 DMR; frequency variants | SFtemp=3 SFspec=6 dx=0.016 ff=[250, 1000] duration=5000 syllables=[0, 1, 1]
    9 DMR; frequency variants | SFtemp=3 SFspec=6 dx=0.016 ff=[500, 2000] duration=5000 syllables=[0, 1, 1]
    10 DMR; frequency variants | SFtemp=3 SFspec=6 dx=0.016 ff=[1000, 4000] duration=5000 syllables=[0, 1, 1]
    11 DMR; frequency variants | SFtemp=3 SFspec=6 dx=0.016 ff=[2000, 8000] duration=5000 syllables=[0, 1, 1]
    12 DMR; frequency variants | SFtemp=3 SFspec=6 dx=0.016 ff=[4000, 16000] duration=5000 syllables=[0, 1, 1]
    13 DMR; frequency variants | SFtemp=3 SFspec=6 dx=0.016 ff=[8000, 32000] duration=5000 syllables=[0, 1, 1]
##### 1 files Combinations of 4 synthetic sounds
   cells ['20060916-ha5-002/20060916-ha5-002-002.mat']
   seqs Seq.1:  5  1  9  1 | Seq.2:  2   1  10   1 | Seq.3:  1  13   1  12   1 | Seq.4:  11   1   8   1 | Seq.5:  4  1  7  1 | Seq.6:  3  1  6  1
    1 neotropical-mammals-1 Track 40 (Amazon D | duration=5804.016
    2 DMR; frequency variants | SFtemp=3 SFspec=6 dx=0.016 ff=[250, 1000] duration=5000
    3 DMR; frequency variants | SFtemp=3 SFspec=6 dx=0.016 ff=[500, 2000] duration=5000
[... 49 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "ff=\[625, 2500\]\|ff=\[2500, 10000\]\|ff=\[10000, 40000\]" $TMPDIR/synth_designs.txt | cut -c1-160 | head -30; sed -n 156,190p $TMPDIR/synth_designs.txt | cut -c1-200
```

```
733:    2 DMR; amplitude variants | SFtemp=3 SFspec=6 dx=0.016 ff=[2500, 10000] duration=5000 attenuation=3.162
734:    3 DMR; amplitude variants | SFtemp=3 SFspec=6 dx=0.016 ff=[2500, 10000] duration=5000 attenuation=1
735:    4 DMR; amplitude variants | SFtemp=3 SFspec=6 dx=0.016 ff=[2500, 10000] duration=5000 attenuation=0.316
736:    5 DMR; amplitude variants | SFtemp=3 SFspec=6 dx=0.016 ff=[2500, 10000] duration=5000 attenuation=0.1
737:    6 DMR; amplitude variants | SFtemp=3 SFspec=6 dx=0.016 ff=[2500, 10000] duration=5000 attenuation=0.032
738:    7 DMR; amplitude variants | SFtemp=3 SFspec=6 dx=0.016 ff=[2500, 10000] duration=5000 attenuation=0.01
739:    8 DMR; amplitude variants | SFtemp=3 SFspec=6 dx=0.016 ff=[2500, 10000] duration=5000 attenuation=0.003
740:    9 DMR; amplitude variants | SFtemp=3 SFspec=6 dx=0.016 ff=[2500, 10000] duration=5000 attenuation=0.001
741:    10 DMR; amplitude variants | SFtemp=3 SFspec=6 dx=0.016 ff=[2500, 10000] duration=5000 attenuation=3.162 syllables=[0, 1, 1]
742:    11 DMR; amplitude variants | SFtemp=3 SFspec=6 dx=0.016 ff=[2500, 10000] duration=5000 attenuation=1 syllables=[0, 1, 1]
743:    12 DMR; amplitude variants | SFtemp=3 SFspec=6 dx=0.016 ff=[2500, 10000] duration=5000 attenuation=0.316 syllables=[0, 1, 1]
744:    13 DMR; amplitude variants | SFtemp=3 SFspec=6 dx=0.016 ff=[2500, 10000] duration=5000 attenuation=0.1 syllables=[0, 1, 1]
745:    14 DMR; amplitude variants | SFtemp=3 SFspec=6 dx=0.016 ff=[2500, 10000] duration=5000 attenuation=0.032 syllables=[0, 1, 1]
746:    15 DMR; amplitude variants | SFtemp=3 SFspec=6 dx=0.016 ff=[2500, 10000] duration=5000 attenuation=0.01 syllables=[0, 1, 1]
747:    16 DMR; amplitude variants | SFtemp=3 SFspec=6 dx=0.016 ff=[2500, 10000] duration=5000 attenuation=0.003 syllables=[0, 1, 1]
748:    17 DMR; amplitude variants | SFtemp=3 SFspec=6 dx=0.016 ff=[2500, 10000] duration=5000 attenuation=0.001 syllables=[0, 1, 1]
##### 1 files Combinations of 4 synthetic sounds
   ce
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> entries/asari-2009/ctxdep.py <<'EOF'


# ----------------------------------------------------------------------------- A1 spikes, rates, checks
def a1_spikes(rec: Recording, height: float) -> np.ndarray:
    """Spikes of a whole-cell trace: peaks of the raw trace minus its 10-ms median filter.

    The paper detected A1 spikes by hand (GetSpikes.m, manual mode, which the code says
    is needed for intracellular data). Here a spike is a peak at least `height` mV above
    the median-filtered membrane potential, at least 2 ms after the previous one; the
    heights used (10, 15, 20 mV) are readings, an assumption stated in the notebook.
    """
    base = np.repeat(rec.vm, DEC)[: rec.n_samples]
    pk, _ = signal.find_peaks(rec.raw - base, height=height, distance=20)
    return pk


def window_rates(rec: Recording, spikes: np.ndarray, pre_baseline: float = 1.0, pulse_skip: float = 0.5) -> dict:
    """Spike counts and durations in the stimulus periods and in the silences.

    Stimulus periods are the non-pulse triggers (GetEvoked.m). Silences are the gaps
    between them, less `pulse_skip` s after each test pulse; the pre-stimulus baseline
    is the last `pre_baseline` s before each stimulus.
    """
    ev = [t for t in rec.triggers if "pulse" not in t[0]]
    pulses = [t[1] for t in rec.triggers if "pulse" in t[0]]
    mask_sp = np.zeros(rec.n_samples, bool)
    mask_ev = np.zeros(rec.n_samples, bool)
    mask_pre = np.zeros(rec.n_samples, bool)
    prev = 0
    for typ, on, dur, _ in ev:
        mask_sp[prev:on] = True
        mask_pre[max(prev, on - int(pre_baseline * SF)):on] = True
        mask_ev[on:on + dur] = True
        prev = on + dur
    mask_sp[prev:] = True
    for p in pulses:
        a, b = p, p + int(pulse_skip * SF)
        mask_sp[a:b] = False
        mask_pre[a:b] = False
    mask_sp &= ~mask_ev
    mask_pre &= ~mask_ev
    sp = np.zeros(rec.n_samples, bool)
    sp[spikes[spikes < rec.n_samples]] = True
    return dict(n_ev=int(sp[mask_ev].sum()), t_ev=mask_ev.sum() / SF, n_sp=int(sp[mask_sp].sum()), t_sp=mask_sp.sum() / SF,
                n_pre=int(sp[mask_pre].sum()), t_pre=mask_pre.sum() / SF)


def onset_contrast(rec: Recording, win: float = 1.0) -> dict:
    """Clock check: across-trial predictable power (Eq. 52) of the membrane potential in
    the `win` s after each sequence onset and in the `win` s before it, per sequence."""
    segs = [s for s in sequence_segments(rec) if s["seq"] is not None]
    by = {}
    for s in segs:
        by.setdefault(s["seq"], []).append(s["on"] // DEC)
    W = int(win * FS)
    post, pre = [], []
    for ons in by.values():
        ons = [o for o in ons if o - W >= 0 and o + W <= len(rec.vm)]
        if len(ons) < 2:
            continue
        for sign, out in ((1, post), (-1, pre)):
            X = np.array([rec.vm[o:o + W] if sign > 0 else rec.vm[o - W:o] for o in ons], float)
            X -= X.mean(axis=1, keepdims=True)
            m = len(ons)
            out.append(((m * X.mean(0) ** 2 - (X ** 2).mean(0)) / (m - 1)).mean())
    return dict(post=float(np.mean(post)) if post else np.nan, pre=float(np.mean(pre)) if pre else np.nan)


def spont_autocorr(rec: Recording, max_lag: float = 0.5, skip: float = 0.0) -> np.ndarray | None:
    """Mean normalized autocorrelation (Eq. 45) of the silences between sequences (1 kHz,
    median filtered, each segment centred), skipping `skip` s after each sequence end and
    0.5 s after each test pulse."""
    segs = [s for s in sequence_segments(rec) if s["seq"] is not None]
    pulses = np.array([t[1] for t in rec.triggers if "pulse" in t[0]])
    L = int(max_lag * FS)
    acs = []
    for s in segs:
        a, b = s["post"][0] + int(skip * SF), s["post"][1]
        if len(pulses):
            inside = pulses[(pulses >= a) & (pulses < b)]
            if len(inside):
                b = int(inside.min())          # stop at the first test pulse
        x = rec.vm[a // DEC: b // DEC].astype(float)
        if len(x) < 2 * L:
            continue
        x = x - x.mean()
        ac = signal.correlate(x, x, mode="full", method="fft")[len(x) - 1: len(x) - 1 + L + 1]
        ac = ac / np.arange(len(x), len(x) - L - 1, -1)
        acs.append(ac / ac[0])
    return np.mean(acs, axis=0) if acs else None


def noise_autocorr(p: Probe, max_lag: float = 0.5) -> np.ndarray:
    """Mean normalized autocorrelation of the trial residuals (Eqs. 14 and 45) of a probe."""
    L = int(max_lag * FS)
    acs = []
    for X in p.traces:
        if X.shape[0] < 2:
            continue
        E = X - X.mean(axis=0, keepdims=True)
        for e in E:
            e = e - e.mean()
            if len(e) < 2 * L or not np.any(e):
                continue
            ac = signal.correlate(e, e, mode="full", method="fft")[len(e) - 1: len(e) - 1 + L + 1]
            ac = ac / np.arange(len(e), len(e) - L - 1, -1)
            acs.append(ac / ac[0])
    return np.mean(acs, axis=0)


def trial_correlations(X: np.ndarray) -> tuple:
    """Trial-to-trial reliability of one context: (mean pairwise r, mean r of each trial with
    the mean of the others)."""
    C = np.corrcoef(X)
    iu = np.triu_indices(len(X), 1)
    loo = [np.corrcoef(X[i], np.delete(X, i, 0).mean(0))[0, 1] for i in range(len(X))]
    return float(np.nanmean(C[iu])), float(np.nanmean(loo))


def first_cross(t: np.ndarray, y: np.ndarray, level: float) -> float:
    i = np.where(y < level)[0]
    return float(t[i[0]]) if len(i) else np.nan
EOF
date -u
```

```
Sun Nov 15 11:57:29 UTC 2026
```

**Agent**

Now writing the notebook builder.

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build_nb.py",
 "content": "import nbformat as nbf\n\nnb = nbf.v4.new_notebook()\ncells = []\n\n\ndef md(s, tags=None):\n    c = nbf.v4.new_markdown_cell(s.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\ndef code(s, tags=None):\n    c = nbf.v4.new_code_cell(s.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\nmd(r\"\"\"\n# Reproducing Asari and Zador (2009) on CRCNS ac-1\n\nPaper: H. Asari and A. M. Zador (2009), \"Long-Lasting Context Dependence Constrains Neural Encoding\nModels in Rodent Auditory Cortex\", J Neurophysiol 102:2638-2656, doi:10.1152/jn.00577.2009.\n\nDataset: CRCNS ac-1 (doi:10.6080/K0KW5CXR), \"Auditory cortex and thalamic neuronal responses to\nvarious natural and synthetic sounds\", read anonymously from the public S3 bucket `crcnsarchive`\n(`ac-1/`), streaming the zip files by range requests.\n\nVersion. CRCNS data sets are not versioned, so the version is recorded as `unversioned`; the\ncell below prints the bucket listing and the MD5 sums of `checksums.md5` for the three zip files\nread, so that a later change can be detected. There is only one published version to choose; the\npaper cites the data set without a version.\n\nClaims file: `claims/asari-2009.yaml`, written from the version of record (text extraction and\nPDF), without the online supplement. This notebook is a repeat attempt, made blind to the earlier\nones.\n\nThe data set holds, besides the recordings, the authors' MATLAB analysis code\n(`asari/Tools/CxtDep.m` and others in `crcns-ac1.zip`). Method details the claims file leaves open\nare taken from the paper first and, where the paper is silent, from that code; each is cited in\nthe helper module `ctxdep.py` and below.\n\n| Claim | Tested here |\n|---|---|\n| methods-recording-counts | tested (voltage-clamp counts: no data) |\n| a1-mgb-firing-rates | tested |\n| fig2-example-reliability | tested |\n| fig2-example-long-context | tested (example searched) |\n| fig3a-proportion-significant | tested |\n| fig3a-significance-decay | tested |\n| fig3b-fractional-power-decay | tested |\n| timescale-longer-than-membrane | tested |\n| fig4-predictability-upper-bound | tested |\n| fig4-strf-performance-low | blocked |\n| fig5-example-conductances | blocked, no voltage-clamp recordings |\n| fig6-conductance-decay | blocked, no voltage-clamp recordings |\n| fig8a-proportion-by-property | blocked, property groups not documented |\n| fig8b-decay-by-property | blocked (depends on fig8a) |\n| fig8a-significance-fits | blocked (depends on fig8a) |\n| fig8c-relative-effects | blocked (depends on fig8b) |\n| fig8-natural-synthetic-probes-alike | blocked (depends on fig8a) |\n| fig9-mgb-fast-decay | tested |\n| fig9-example-first-bin | tested |\n| fig7-example-frequency-context | searched; no matching recording |\n| figs1-silence-probe | tested |\n\"\"\")\n\ncode(r\"\"\"\nimport os, time, zlib, resource, collections\nos.environ.setdefault(\"OMP_NUM_THREADS\", \"1\")\nos.environ.setdefault(\"OPENBLAS_NUM_THREADS\", \"1\")\nfrom concurrent.futures import ThreadPoolExecutor\nimport numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nfrom scipy import ndimage, stats\nimport ctxdep as cd\n\nT0 = time.time()\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 30)\n\n\ndef seed(*parts):\n    # one generator per probe and reading, independent of processing order\n    return np.random.default_rng([zlib.crc32(\"/\".join(map(str, parts)).encode())])\n\"\"\")\n\nmd(\"## Data: listing, checksums, and one pass over the recordings\")\n\ncode(r\"\"\"\nlisting = cd.bucket_listing()\nmd5 = cd.checksums()\nprint(\"bucket listing of ac-1/:\")\nfor k, s in listing:\n    print(f\"  {k:45s} {int(s):>12d} bytes\")\nprint(\"MD5 (checksums.md5) of the files read:\")\nfor z in cd.ZIPS:\n    print(f\"  {z:35s} {md5[z]}\")\nS = cd.summary(\"asari\")\nfor g in S:\n    print(f\"{len(g['cells']):3d} cells | {g['description']} | {g['reference'][:60]}\")\nW = cd.summary(\"wehr\")\nfor g in W:\n    print(f\"{len(g['cells']):3d} cells | Wehr | {g['description']}\")\n\"\"\")\n\ncode(r\"\"\"\nNAT, MGB, SYN, MISC = S[0], S[1], S[2], S[3]\nassert \"natural sound\" in NAT[\"description\"] and \"Thalamic\" in MGB[\"description\"]\nassert \"synthetic\" in SYN[\"description\"]\n\n\ndef proc_a1(job):\n    group, cell, path, desc = job\n    rec = cd.load_recording(path, keep_raw=True)\n    out = dict(group=group, cell=cell, path=path, desc=desc, type=rec.rec_type, sf=rec.sf, unit=rec.unit,\n               dur=rec.n_samples / rec.sf, rep=rec.rep, nfrag=len(rec.durations), trig=collections.Counter(t[0] for t in rec.triggers),\n               **rec.meta)\n    out[\"rates\"] = {h: cd.window_rates(rec, cd.a1_spikes(rec, h)) for h in (10, 15, 20)}\n    rec.raw = None\n    if desc != \"tuning curve\":\n        out[\"clock\"] = cd.onset_contrast(rec)\n        out[\"counts\"] = {inc: [(p.probe, tuple(p.contexts), tuple(p.n_trials), p.duration) for p in cd.build_probes(rec, include_silence_context=inc)]\n                         for inc in (True, False)}\n        out[\"stim\"] = [(str(getattr(s, \"name\", \"\")), str(getattr(s, \"description\", \"\")),\n                        np.atleast_1d(getattr(s.param, \"ff\", [])).tolist()) for s in rec.stimuli]\n    if group == \"natural\" and desc != \"tuning curve\":\n        res = []\n        for inc in (True, False):\n            for p in cd.build_probes(rec, include_silence_context=inc, include_silence_probe=inc):\n                r = cd.kw_significance(p, rng=seed(path, p.probe, inc))\n                fp = cd.frac_power(p)\n                d = dict(cell=cell, path=path, desc=desc, probe=p.probe, ctx=tuple(p.contexts), ntr=tuple(p.n_trials),\n                         dur=p.duration, silence=inc, rep=r[\"rep\"], sig=r[\"sig\"], noise=r[\"noise\"], pval=r[\"p\"], **fp)\n                if inc:\n                    d[\"traces\"] = p.traces\n                res.append(d)\n        out[\"probes\"] = res\n        out[\"spont_ac\"] = {0.0: cd.spont_autocorr(rec, skip=0.0), 1.0: cd.spont_autocorr(rec, skip=1.0)}\n    return out\n\n\ndef proc_mgb(job):\n    group, cell, path, desc = job\n    rec = cd.load_recording(path, keep_raw=True, filtered=False)\n    sp = cd.extract_spikes(rec.raw)\n    out = dict(group=group, cell=cell, path=path, desc=desc, type=rec.rec_type, sf=rec.sf, unit=rec.unit,\n               dur=rec.n_samples / rec.sf, rep=rec.rep, nspk=len(sp), **rec.meta)\n    out[\"rates\"] = cd.window_rates(rec, sp)\n    rec.raw = None\n    if desc != \"tuning curve\":\n        segs = [s for s in cd.sequence_segments(rec) if s[\"seq\"] is not None]\n        post = sum(((sp >= s[\"on\"]) & (sp < s[\"on\"] + cd.SF // 2)).sum() for s in segs) / (0.5 * len(segs))\n        pre = sum(((sp >= s[\"on\"] - cd.SF // 2) & (sp < s[\"on\"])).sum() for s in segs) / (0.5 * len(segs))\n        out[\"clock\"] = dict(post=post, pre=pre)\n        res = []\n        for inc in (True, False):\n            for p in cd.build_probes(rec, include_silence_context=inc, spikes=sp):\n                r = cd.psth_sd(p)\n                res.append(dict(cell=cell, path=path, desc=desc, probe=p.probe, ctx=tuple(p.contexts), ntr=tuple(p.n_trials),\n                                dur=p.duration, silence=inc, rep=r[\"rep\"], sd=r[\"sd\"], psth=r[\"psth\"]))\n        out[\"probes\"] = res\n    return out\n\n\njobs_a1 = [(gname, c[\"cell\"], f, d) for gname, g in ((\"natural\", NAT), (\"synthetic\", SYN), (\"various\", MISC))\n           for c in g[\"cells\"] for f, d in zip(c[\"files\"], c[\"descriptions\"])]\njobs_mgb = [(\"mgb\", c[\"cell\"], f, d) for c in MGB[\"cells\"] for f, d in zip(c[\"files\"], c[\"descriptions\"])]\nprint(len(jobs_a1), \"A1 files;\", len(jobs_mgb), \"MGB files\")\nwith ThreadPoolExecutor(4) as ex:\n    A1 = list(ex.map(proc_a1, jobs_a1))\n    MG = list(ex.map(proc_mgb, jobs_mgb))\nprint(f\"loaded in {time.time() - T0:.0f} s; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n\"\"\")\n\nmd(\"## Data check\")\n\ncode(r\"\"\"\nF = pd.DataFrame([{k: v for k, v in o.items() if k in (\"group\", \"cell\", \"path\", \"desc\", \"type\", \"sf\", \"unit\", \"dur\", \"rep\",\n                                                    \"age\", \"vmin\", \"vmax\", \"vmedian\")} for o in A1 + MG])\nprint(\"files by group and recording type:\")\nprint(F.groupby([\"group\", \"type\"]).agg(files=(\"path\", \"size\"), cells=(\"cell\", \"nunique\"), animals=(\"cell\", lambda c: c.str[:12].nunique())))\nprint(\"\\nsampling rates:\", sorted(F.sf.unique()), \"| units:\", sorted(F.unit.unique()))\nprint(\"recording types in the whole data set:\", sorted(F.type.unique()), \"(no voltage-clamp recording: every trace is in mV)\")\nprint(\"\\nmedian membrane potential of whole-cell files (mV): range %.1f to %.1f; trace extremes %.1f to %.1f mV\"\n      % (F[F.type == \"Whole-cell\"].vmedian.min(), F[F.type == \"Whole-cell\"].vmedian.max(),\n         F[F.type == \"Whole-cell\"].vmin.min(), F[F.type == \"Whole-cell\"].vmax.max()))\nprint(\"recording length per file (s): %.0f to %.0f\" % (F.dur.min(), F.dur.max()))\nprint(\"animal age (days) as stored:\", collections.Counter(F.age).most_common(12))\nprint(\"\\nnatural sound A1 recordings by design:\")\nprint(F[(F.group == \"natural\") & (F.desc != \"tuning curve\")].groupby(\"desc\").agg(files=(\"path\", \"size\"), cells=(\"cell\", \"nunique\"), rep_min=(\"rep\", \"min\"), rep_max=(\"rep\", \"max\")))\nprint(\"\\nMGB recordings by design:\")\nprint(F[(F.group == \"mgb\") & (F.desc != \"tuning curve\")].groupby(\"desc\").agg(files=(\"path\", \"size\"), cells=(\"cell\", \"nunique\"), rep_min=(\"rep\", \"min\"), rep_max=(\"rep\", \"max\")))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nClock check. The trigger times must share the clock of the traces. For each sequence, the\nacross-trial predictable power (Eq. 52) of the membrane potential in the 1 s after the sequence\nonset is compared with the 1 s before it (silence). If the triggers were offset from the traces,\nthe two would be alike. For MGB units the firing rate in the 0.5 s after onset is compared with\nthe 0.5 s before.\n\"\"\")\n\ncode(r\"\"\"\nck = pd.DataFrame([dict(group=o[\"group\"], path=o[\"path\"], post=o[\"clock\"][\"post\"], pre=o[\"clock\"][\"pre\"])\n                   for o in A1 + MG if \"clock\" in o and np.isfinite(o[\"clock\"][\"post\"])])\nfor g, d in ck.groupby(\"group\"):\n    print(f\"{g:10s} files {len(d):3d}: post-onset median {d.post.median():.3f}, pre-onset median {d.pre.median():.3f}; \"\n          f\"post > pre in {(d.post > d.pre).sum()} of {len(d)}\")\nprint(\"(A1 in mV^2 of predictable power; MGB in spikes/s)\")\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nDuplicates. Recordings deposited twice would have identical traces. Each file's trace extremes and\nmedian, and its length, are compared across files.\n\"\"\")\n\ncode(r\"\"\"\nkey = F.assign(k=F.dur.round(4).astype(str) + \"|\" + F.vmin.round(4).astype(str) + \"|\" + F.vmax.round(4).astype(str) + \"|\" + F.vmedian.round(4).astype(str))\ndups = key[key.duplicated(\"k\", keep=False)].sort_values(\"k\")\nprint(\"files sharing length, extremes and median:\", len(dups))\nprint(dups[[\"path\", \"dur\", \"vmin\", \"vmax\"]].to_string() if len(dups) else \"none\")\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nTime resolution. The analysis runs at 1 kHz (helper docstring). On the probes of one recording the\nKruskal-Wallis significance is recomputed at the paper's 0.1 ms on the 10-kHz median-filtered\ntrace (no shuffles), and the significant periods are compared.\n\"\"\")\n\ncode(r\"\"\"\ndef kw_fullres(trace10, starts, length, rep):\n    X = np.array([trace10[s:s + length] for s in starts], float)\n    M = len(starts) // rep\n    N = X.shape[0]\n    R = stats.rankdata(X, axis=0)\n    rbar = R.reshape(M, rep, -1).mean(axis=1)\n    kw = 12 * ((rbar - (N + 1) / 2) ** 2).sum(axis=0) / (M * (N + 1))\n    pv = stats.chi2.sf(kw, M - 1)\n    return ndimage.binary_opening(pv < cd.ALPHA, structure=np.ones(51, bool))   # >= 5.1 ms, as CxtDep.m\n\n\npath0 = [o for o in A1 if o[\"group\"] == \"natural\" and o[\"desc\"] != \"tuning curve\"][0][\"path\"]\nrec0 = cd.load_recording(path0, keep_raw=True)\nx10 = ndimage.median_filter(rec0.raw, size=cd.MEDWIN)\nsegs = [s for s in cd.sequence_segments(rec0) if s[\"seq\"] is not None]\nby = {}\nfor s in segs:\n    by.setdefault(s[\"seq\"], []).append(s)\nby = {k: v[: rec0.rep] for k, v in by.items()}\nagree = []\nfor pr in cd.build_probes(rec0):\n    rep = pr.rep\n    starts = []\n    for c in pr.contexts:\n        st = []\n        for seq, pres in by.items():\n            ext = [0] + list(seq)\n            for k, f in enumerate(seq):\n                if f == pr.probe and ext[k] == c:\n                    off = int(sum(rec0.durations[g - 1] for g in seq[:k]))\n                    st += [s_[\"on\"] + off for s_ in pres]\n        starts += st[:rep]\n    L = int(pr.duration * cd.SF)\n    full = kw_fullres(x10, starts, L, rep)\n    low = cd.kw_significance(pr, nshuffle=0)[\"sig\"]\n    full_ds = full[::cd.DEC][: len(low)]\n    agree.append(dict(probe=pr.probe, frac_sig_10kHz=full.mean(), frac_sig_1kHz=low.mean(), agreement=(full_ds == low[: len(full_ds)]).mean(),\n                      any_10kHz=full.any(), any_1kHz=low.any(), last_10kHz=(np.where(full)[0].max() / cd.SF if full.any() else np.nan),\n                      last_1kHz=(np.where(low)[0].max() / cd.FS if low.any() else np.nan)))\ndel rec0, x10\nprint(path0)\nprint(pd.DataFrame(agree).round(4).to_string())\n\"\"\", tags=[\"sanity\"])\n\n# ------------------------------------------------------------------ counts\nmd(r\"\"\"\n## methods-recording-counts\n\n> Of 194 A1 cells recorded in current clamp, 123 met the analysis criterion (39 tested with natural\n> sounds, 14 with TORCs, 6 with DMRs, 39 with modulated harmonic tones, 27 with modulated colored\n> noise); 14 of 42 voltage-clamped cells and 14 of 16 MGB cells were analysed.\n\nRule (criterion; CxtDep.m): a probe counts when it follows at least two distinct conditioning\nstimuli, each with at least 4 trials in A1 current clamp and at least 10 in MGB, after cutting all\ncontexts to the smallest number of trials. Both readings of \"silence\" are run.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor o in A1 + MG:\n    if \"counts\" in o:\n        for inc, lst in o[\"counts\"].items():\n            for pr, ctx, ntr, dur in lst:\n                rows.append(dict(group=o[\"group\"], cell=o[\"cell\"], path=o[\"path\"], desc=o[\"desc\"], silence=inc, probe=pr,\n                                 nctx=len(ctx), rep=min(ntr), dur=dur))\nfor o in MG:\n    for p in o.get(\"probes\", []):\n        pass\nC = pd.DataFrame(rows)\nC[\"ok\"] = np.where(C.group == \"mgb\", C.rep >= 10, C.rep >= 4)\ncnt = C[C.ok].groupby([\"group\", \"silence\"]).agg(probes=(\"probe\", \"size\"), cells=(\"cell\", \"nunique\"))\nprint(cnt)\nallc = {o[\"cell\"] for o in A1 if o[\"group\"] in (\"natural\", \"synthetic\", \"various\")}\nfor inc in (True, False):\n    okc = set(C[(C.ok) & (C.group != \"mgb\") & (C.silence == inc)].cell)\n    print(f\"silence counted={inc}: A1 cells meeting the criterion (natural and synthetic ensembles) {len(okc)} of {len(allc)} whole-cell cells in the data set\")\nprint(\"probes in the data set failing the rule:\", int((~C.ok).sum()))\nprint(\"A1 cells in the data set:\", {g: len({o['cell'] for o in A1 if o['group'] == g}) for g in ('natural', 'synthetic', 'various')},\n      \"| MGB cells:\", len({o['cell'] for o in MG}))\nprint(\"voltage-clamp recordings in the data set: 0 (see the data check)\")\n\"\"\", tags=[\"claim:methods-recording-counts\"])\n\nmd(r\"\"\"\n**Result: ...** (filled after the run)\n\"\"\")\n\n# ------------------------------------------------------------------ firing rates\nmd(r\"\"\"\n## a1-mgb-firing-rates\n\n> Firing rates were low in A1 (spontaneous 0.47 +/- 0.61 Hz, evoked 0.57 +/- 0.77 Hz, mean +/- SD, 194\n> cells) and high in MGB (spontaneous 0.78 +/- 1.25 Hz, evoked 11.4 +/- 16.9 Hz, 16 cells).\n\nSpontaneous: (a) all silences between stimuli, less 0.5 s after each test pulse, or (b) the last\n1 s before each stimulus. Evoked: all stimulus periods (which are the probe periods of the\nanalysis, every fragment being a probe). A1 spikes, which the paper detected by hand, are peaks at\nleast 10, 15 or 20 mV above the 10-ms median-filtered trace (an assumption; readings shown). MGB\nspikes use the automatic detector of GetSpikes.m. Rates are per cell over all its files, in the\nsequence files only, or (MGB) in the tuning-curve files only.\n\"\"\")\n\ncode(r\"\"\"\ndef cell_rates(objs, key=None, files=\"all\"):\n    rows = []\n    for o in objs:\n        if files == \"seq\" and o[\"desc\"] == \"tuning curve\":\n            continue\n        if files == \"tuning\" and o[\"desc\"] != \"tuning curve\":\n            continue\n        r = o[\"rates\"][key] if key is not None else o[\"rates\"]\n        rows.append(dict(cell=o[\"cell\"], **r))\n    d = pd.DataFrame(rows).groupby(\"cell\").sum()\n    return pd.DataFrame(dict(spont=d.n_sp / d.t_sp, pre=d.n_pre / d.t_pre, evoked=d.n_ev / d.t_ev))\n\n\nout = []\nfor h in (10, 15, 20):\n    for files in (\"all\", \"seq\"):\n        r = cell_rates(A1, h, files)\n        out.append(dict(region=\"A1\", detector=f\"{h} mV\", files=files, cells=len(r), spont_mean=r.spont.mean(), spont_sd=r.spont.std(),\n                        pre_mean=r.pre.mean(), pre_sd=r.pre.std(), evoked_mean=r.evoked.mean(), evoked_sd=r.evoked.std()))\nfor files in (\"all\", \"seq\", \"tuning\"):\n    r = cell_rates(MG, None, files)\n    out.append(dict(region=\"MGB\", detector=\"GetSpikes auto\", files=files, cells=len(r), spont_mean=r.spont.mean(), spont_sd=r.spont.std(),\n                    pre_mean=r.pre.mean(), pre_sd=r.pre.std(), evoked_mean=r.evoked.mean(), evoked_sd=r.evoked.std()))\nRATES = pd.DataFrame(out)\nprint(RATES.round(3).to_string())\nprint(\"\\npaper: A1 spont 0.47 +/- 0.61, evoked 0.57 +/- 0.77 (194 cells); MGB spont 0.78 +/- 1.25, evoked 11.4 +/- 16.9 Hz (16 cells)\")\nprint(\"tolerances: A1 0.423-0.517 and 0.513-0.627; MGB 0.702-0.858 and 10.26-12.54 Hz\")\nmg_seq = cell_rates(MG, None, \"seq\")\nprint(\"\\nMGB per cell (sequence files), Hz:\\n\", mg_seq.round(2).to_string())\n\"\"\", tags=[\"claim:a1-mgb-firing-rates\"])\n\nmd(\"**Result: ...**\")\n\n# ------------------------------------------------------------------ natural probes table\nmd(r\"\"\"\n## Natural sound probes in A1\n\nAll natural-sound A1 probes, with \"silence\" counted among the contexts (main reading) and not\ncounted. The silence probes (probe 0, the first 2.5 s after a sequence) are kept apart for\nfigs1-silence-probe.\n\"\"\")\n\ncode(r\"\"\"\nNP = [p for o in A1 if o[\"group\"] == \"natural\" for p in o.get(\"probes\", [])]\nNPf = {inc: [p for p in NP if p[\"silence\"] == inc and p[\"probe\"] != 0 and p[\"rep\"] >= 4] for inc in (True, False)}\nSILP = [p for p in NP if p[\"silence\"] and p[\"probe\"] == 0]\nfor inc in (True, False):\n    d = pd.DataFrame([dict(cell=p[\"cell\"], dur=p[\"dur\"], nctx=len(p[\"ctx\"]), rep=p[\"rep\"]) for p in NPf[inc]])\n    print(f\"silence counted={inc}: {len(d)} probes in {d.cell.nunique()} cells; contexts per probe {d.nctx.min()}-{d.nctx.max()} \"\n          f\"(median {d.nctx.median():.0f}); trials per context {d.rep.min()}-{d.rep.max()}; probe length {d.dur.min():.2f}-{d.dur.max():.2f} s\")\nprint(\"silence probes:\", len(SILP), \"in\", len({p['cell'] for p in SILP}), \"cells\")\nTMAX = 6.1\nTT = int(TMAX * cd.FS)\nt_ax = np.arange(TT) / cd.FS\n\"\"\")\n\n# ------------------------------------------------------------------ reliability\nmd(r\"\"\"\n## fig2-example-reliability\n\n> The example A1 neuron of Figure 2 had high trial-to-trial reliability (correlation across trials\n> 0.74 +/- 0.08 for the shown probe and 0.61 +/- 0.07 over the seven natural sound fragments tested),\n> and the mean correlation over the population was 0.31 +/- 0.09.\n\nCorrelation between the median-filtered traces of the trials of one context over the probe period.\nReadings: (a) mean over all pairs of trials, (b) mean correlation of each trial with the mean of\nthe others; population mean over cells (each cell the mean over its probes and contexts) or over\nprobes. Silence counted as a context (it is a context of Figure 2B).\n\"\"\")\n\ncode(r\"\"\"\nrel = []\nfor p in NPf[True]:\n    for c, X in zip(p[\"ctx\"], p[\"traces\"]):\n        if X.shape[0] >= 2:\n            a, b = cd.trial_correlations(X.astype(float))\n            rel.append(dict(cell=p[\"cell\"], path=p[\"path\"], desc=p[\"desc\"], probe=p[\"probe\"], ctx=c, ntr=X.shape[0], pair=a, loo=b))\nREL = pd.DataFrame(rel)\nper_probe = REL.groupby([\"path\", \"probe\"])[[\"pair\", \"loo\"]].mean()\nper_cell = REL.groupby(\"cell\")[[\"pair\", \"loo\"]].mean()\nfor r in (\"pair\", \"loo\"):\n    print(f\"reading {r}: over cells mean {per_cell[r].mean():.3f} +/- {per_cell[r].std():.3f} (n={len(per_cell)}); \"\n          f\"over probes {per_probe[r].mean():.3f} +/- {per_probe[r].std():.3f} (n={len(per_probe)}); \"\n          f\"range over cells {per_cell[r].min():.2f} to {per_cell[r].max():.2f}\")\nprint(\"paper: 0.31 +/- 0.09 (tolerance 0.22 to 0.40)\")\n# example cell: seven natural fragments, six repeats\ncand = REL[REL.desc.str.contains(\"7 long\")]\ncc = cand.groupby(\"path\").agg(cell_mean=(\"pair\", \"mean\"), cell_mean_loo=(\"loo\", \"mean\"), max_ctx=(\"pair\", \"max\"), ntr_max=(\"ntr\", \"max\"))\ncc = cc[cc.ntr_max >= 6]\nprint(\"\\ncandidate example cells (7 natural fragments, >= 6 trials in a context):\", len(cc))\nprint(cc.round(3).to_string())\nm = cc[(cc.cell_mean.between(0.54, 0.68)) | (cc.cell_mean_loo.between(0.54, 0.68))]\nprint(\"cells whose mean is within 0.61 +/- 0.07:\", len(m))\nfor path in m.index:\n    d = cand[cand.path == path]\n    print(path, \"probe-context values within 0.74 +/- 0.08:\", int(d.pair.between(0.66, 0.82).sum()), \"(pairs),\", int(d.loo.between(0.66, 0.82).sum()), \"(loo)\")\n\"\"\", tags=[\"claim:fig2-example-reliability\"])\n\nmd(\"**Result: ...**\")\n\n# ------------------------------------------------------------------ long context example\nmd(r\"\"\"\n## fig2-example-long-context\n\n> In an example A1 neuron, changing the conditioning stimulus changed the response to the probe for\n> about 4 s; responses did not differ between 2 and 4 s after probe onset and diverged again after\n> about 4 s.\n\nSearch (criterion): current-clamp cells tested with seven natural sound fragments, probes with\nthree contexts of which one is silence, and at least six trials in one context. Reproduced when a\nmatched probe has significant periods before 2 s and after 4 s and none between 2 and 4 s.\n\"\"\")\n\ncode(r\"\"\"\nex = []\nfor p in NPf[True]:\n    s = p[\"sig\"]\n    t = np.arange(len(s)) / cd.FS\n    ex.append(dict(path=p[\"path\"], probe=p[\"probe\"], desc=p[\"desc\"], ctx=p[\"ctx\"], ntr=p[\"ntr\"], dur=p[\"dur\"],\n                   before2=bool(s[t < 2].any()), mid=bool(s[(t >= 2) & (t <= 4)].any()), after4=bool(s[t > 4].any()),\n                   last=(t[s].max() if s.any() else np.nan)))\nEX = pd.DataFrame(ex)\nmatch = EX[EX.desc.str.contains(\"7 long\") & EX.ctx.apply(lambda c: len(c) == 3 and 0 in c) & EX.ntr.apply(lambda n: max(n) >= 6)]\nprint(\"probes matching the example's design:\", len(match), \"in\", match.path.nunique(), \"recordings\")\npat = match[match.before2 & ~match.mid & match.after4]\nprint(\"of these, with significance before 2 s, none in 2-4 s and again after 4 s:\", len(pat))\nprint(pat[[\"path\", \"probe\", \"ctx\", \"ntr\", \"dur\", \"last\"]].to_string())\nprint(\"\\nall 305 probes: significant period later than 4 s in\", int((EX.last > 4).sum()), \"; the 2-4 s gap pattern in\",\n      int((EX.before2 & ~EX.mid & EX.after4).sum()))\n\"\"\", tags=[\"claim:fig2-example-long-context\"])\n\ncode(r\"\"\"\nif len(pat):\n    p = [q for q in NPf[True] if q[\"path\"] == pat.iloc[0].path and q[\"probe\"] == pat.iloc[0].probe][0]\n    fig, ax = plt.subplots(2, 1, figsize=(8, 5), sharex=True)\n    for c, X in zip(p[\"ctx\"], p[\"traces\"]):\n        ax[0].plot(np.arange(X.shape[1]) / cd.FS, X.mean(0), lw=1, label=f\"context {c}\")\n    ax[0].legend(fontsize=7); ax[0].set_ylabel(\"mean Vm (mV)\")\n    ax[1].semilogy(np.arange(len(p[\"pval\"])) / cd.FS, p[\"pval\"], lw=0.5)\n    ax[1].fill_between(np.arange(len(p[\"sig\"])) / cd.FS, 1e-6, 1, where=p[\"sig\"], color=\"0.8\")\n    ax[1].set_ylabel(\"P (Kruskal-Wallis)\"); ax[1].set_xlabel(\"time from probe onset (s)\")\n    print(\"plotted:\", pat.iloc[0].path, \"probe\", pat.iloc[0].probe, \"; Vm range\", float(min(X.min() for X in p[\"traces\"])), \"to\", float(max(X.max() for X in p[\"traces\"])), \"mV; P from\", p[\"pval\"].min(), \"to 1\")\n    plt.show()\n\"\"\", tags=[\"claim:fig2-example-long-context\"])\n\nmd(\"**Result: ...**\")\n\n# ------------------------------------------------------------------ fig3a\nmd(r\"\"\"\n## fig3a-proportion-significant\n\n> Of 305 natural sound probes tested in 39 A1 cells with typically five to eight natural sound\n> contexts, 204 (66.9%) showed significant context dependence, and about a quarter (23.7%) of the\n> significant events occurred more than 1 s after probe onset.\n\nA probe is significant when it has at least one period with P < 0.01 for at least 5 ms. Late\nfraction: one minus the cumulative probability at 1 s, the cumulative probability being the\nrunning integral of the proportion curve less the noise floor, normalized at its peak (Figure 3A\nlegend). Readings: silence counted or not; proportion over all probes (a probe that has ended\ncounts as not significant) or over the probes still running.\n\"\"\")\n\ncode(r\"\"\"\ndef pop_curves(P, denom):\n    Sg = cd.stack_curves([p[\"sig\"].astype(float) for p in P], TT)\n    Nf = cd.stack_curves([p[\"noise\"] for p in P], TT)\n    if denom == \"all\":\n        return np.nan_to_num(Sg).sum(0) / len(P), np.nan_to_num(Nf).sum(0) / len(P), np.ones(TT) * len(P)\n    n = (~np.isnan(Sg)).sum(0)\n    with np.errstate(invalid=\"ignore\"):\n        return np.nansum(Sg, 0) / n, np.nansum(Nf, 0) / n, n\n\n\nfig3a = []\nCURVES = {}\nfor inc in (True, False):\n    P = NPf[inc]\n    nsig = sum(bool(p[\"sig\"].any()) for p in P)\n    for denom in (\"all\", \"running\"):\n        prop, nf, n = pop_curves(P, denom)\n        ok = n >= 10\n        corr = np.where(ok, prop - nf, 0.0)\n        cum = np.cumsum(corr) / cd.FS\n        ipk = int(np.argmax(cum))\n        cumn = cum / cum[ipk]\n        CURVES[(inc, denom)] = (prop, nf, cumn, ok)\n        fig3a.append(dict(silence=inc, denom=denom, probes=len(P), significant=nsig, fraction=nsig / len(P),\n                          late_fraction=1 - cumn[int(1.0 * cd.FS)], cum_peak_s=ipk / cd.FS, last_t_with_10_probes=t_ax[ok].max()))\nFIG3A = pd.DataFrame(fig3a)\nprint(FIG3A.round(4).to_string())\nprint(\"paper: 204 of 305 (66.9%), late fraction 0.237, peak of the cumulative curve 4.72 s\")\nprint(\"tolerances: 183.6-224.4 probes, 0.602-0.736, 0.213-0.261\")\n# significance by cell\nbycell = pd.DataFrame([dict(cell=p[\"cell\"], sig=bool(p[\"sig\"].any())) for p in NPf[True]]).groupby(\"cell\").sig.agg([\"sum\", \"size\"])\nprint(f\"\\ncells with at least one significant probe: {(bycell['sum'] > 0).sum()} of {len(bycell)}; per-cell fraction median {(bycell['sum'] / bycell['size']).median():.2f}\")\n\"\"\", tags=[\"claim:fig3a-proportion-significant\"])\n\ncode(r\"\"\"\nprop, nf, cumn, ok = CURVES[(True, \"all\")]\nfig, ax = plt.subplots(2, 1, figsize=(7, 5), sharex=True)\nax[0].plot(t_ax, prop, \"k\", lw=1, label=\"proportion significant\"); ax[0].plot(t_ax, nf, \"0.6\", lw=1, label=\"noise floor\")\nax[0].legend(fontsize=8); ax[0].set_ylabel(\"probability\")\nax[1].plot(t_ax, cumn, \"k\"); ax[1].set_ylabel(\"cumulative (normalized)\"); ax[1].set_xlabel(\"time from probe onset (s)\")\nprint(f\"plotted ranges: proportion {prop.min():.3f}-{prop.max():.3f}, noise {nf.min():.4f}-{nf.max():.4f}, cumulative {cumn.min():.3f}-{cumn.max():.3f}\")\nplt.show()\n\"\"\", tags=[\"claim:fig3a-proportion-significant\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n## fig3a-significance-decay\n\n> The proportion of probes with significant context dependence decays after probe onset as the sum\n> of two exponentials (sizes 0.17 and 0.09, decay constants 0.20 and 0.90 s), above a noise floor\n> of about 2.8 x 10^-3.\n\nEq. 44 with the constant fixed at the mean noise floor over the fit range, least squares from a\ngrid of start values (standard choice), two exponentials kept when each size is at least a tenth\nof the total. Readings: fit range 0 to 4.72 s or 0 to 6 s; silence counted or not; proportion over\nall probes or over running ones.\n\"\"\")\n\ncode(r\"\"\"\nfits = []\nfor (inc, denom), (prop, nf, cumn, ok) in CURVES.items():\n    for tmax in (4.72, 6.0):\n        m = (t_ax <= tmax) & ok\n        kappa = float(np.mean(nf[m]))\n        f, alt = cd.fit_with_rule(t_ax[m], prop[m], kappa=kappa)\n        two = f if f[\"n_exp\"] == 2 else alt\n        fits.append(dict(silence=inc, denom=denom, t_max=tmax, n_exp=f[\"n_exp\"], kappa=kappa,\n                         a1=two[\"alpha\"][0], tau1=two[\"tau\"][0], a2=two[\"alpha\"][1], tau2=two[\"tau\"][1],\n                         one_a=(f if f[\"n_exp\"] == 1 else alt)[\"alpha\"][0] if f[\"n_exp\"] == 1 else np.nan,\n                         one_tau=(f if f[\"n_exp\"] == 1 else alt)[\"tau\"][0] if f[\"n_exp\"] == 1 else np.nan))\nFIT3A = pd.DataFrame(fits)\nprint(FIT3A.round(4).to_string())\nprint(\"paper: a1 0.17, tau1 0.20 s, a2 0.09, tau2 0.90 s, kappa 2.8e-3\")\nprint(\"tolerances: a1 0.153-0.187, tau1 0.18-0.22, a2 0.081-0.099, tau2 0.81-0.99, kappa 0.00252-0.00308\")\n\"\"\", tags=[\"claim:fig3a-significance-decay\"])\n\nmd(\"**Result: ...**\")\n\n# ------------------------------------------------------------------ fig3b and fig4\nmd(r\"\"\"\n## fig3b-fractional-power-decay\n\n> The context-dependent fraction of the stimulus-related response power, normalized by the\n> smoothed stimulus-related power, decays from about 0.49 with a time constant of about 1.04 s.\n\nQ(t) of Eq. 20: Eq. 19 over Eq. 17, both averaged over probes at each time, the denominator\nsmoothed by a running mean over [0, 2t]; one exponential with constant 0. The average at time t is\nover the probes still running at t (a power cannot be averaged over probes that have ended; with\nzeros for ended probes the ratio is unchanged except through the smoothing). Readings: silence\ncounted or not, fit range 0 to 4 s or 0 to 6 s, and 0 to the shortest probe.\n\"\"\")\n\ncode(r\"\"\"\nPOW = {}\nfor inc in (True, False):\n    P = NPf[inc]\n    pred = np.nanmean(cd.stack_curves([p[\"pred\"] for p in P], TT), 0)\n    inv = np.nanmean(cd.stack_curves([p[\"inv\"] for p in P], TT), 0)\n    dep = np.nanmean(cd.stack_curves([p[\"dep\"] for p in P], TT), 0)\n    POW[inc] = dict(pred=pred, inv=inv, dep=dep, ps=cd.running_mean_0_2t(pred), shortest=min(p[\"dur\"] for p in P))\nrows = []\nfor inc, d in POW.items():\n    Q = d[\"dep\"] / d[\"ps\"]\n    for tmax in (4.0, 6.0, d[\"shortest\"]):\n        m = (t_ax <= tmax) & np.isfinite(Q)\n        f = cd.fit_exp(t_ax[m], Q[m], 1, kappa=0.0)\n        rows.append(dict(silence=inc, t_max=round(tmax, 2), alpha1=f[\"alpha\"][0], tau1=f[\"tau\"][0],\n                         Q_first_50ms=float(np.mean(Q[:50])), Q_at_1s=float(Q[1000]), Q_at_3s=float(Q[3000])))\nFIT3B = pd.DataFrame(rows)\nprint(FIT3B.round(3).to_string())\nprint(\"paper: alpha1 0.49 (0.441-0.539), tau1 1.04 s (0.936-1.144)\")\n\"\"\", tags=[\"claim:fig3b-fractional-power-decay\"])\n\ncode(r\"\"\"\nd = POW[True]\nQ = d[\"dep\"] / d[\"ps\"]\nfig, ax = plt.subplots(2, 1, figsize=(7, 5), sharex=True)\nax[0].plot(t_ax, d[\"pred\"], \"k\", lw=0.5, label=\"stimulus-related (Eq. 17)\"); ax[0].plot(t_ax, d[\"ps\"], \"0.5\", label=\"running mean [0, 2t]\")\nax[0].plot(t_ax, d[\"dep\"], \"k\", lw=2, label=\"context-dependent (Eq. 19)\"); ax[0].legend(fontsize=7); ax[0].set_ylabel(\"mV^2\")\nax[1].plot(t_ax, Q, \"k\"); ax[1].set_ylim(-0.2, 1.0); ax[1].set_ylabel(\"Q(t)\"); ax[1].set_xlabel(\"time from probe onset (s)\")\nprint(f\"ranges: Eq.17 {np.nanmin(d['pred']):.2f}-{np.nanmax(d['pred']):.2f} mV^2, Eq.19 {np.nanmin(d['dep']):.2f}-{np.nanmax(d['dep']):.2f}; \"\n      f\"Q {np.nanmin(Q):.3f}-{np.nanmax(Q):.3f}, points outside -0.2..1: {int(((Q < -0.2) | (Q > 1)).sum())}\")\nplt.show()\n\"\"\", tags=[\"claim:fig3b-fractional-power-decay\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n## fig4-predictability-upper-bound\n\n> Without knowledge of the context, no model can capture more than about half (0.51) of the\n> predictable response power with a window of about 100 ms; the upper bound approaches one only\n> with a window of seconds (time constant 1.04 s).\n\nEq. 43, Eq. 18 over Eq. 17 averaged over probes, with the denominator smoothed over [0, 2t] (main\nreading) or not; one exponential with constant 1 (1 + alpha1 exp(-t/tau1)).\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor inc, d in POW.items():\n    for smooth in (True, False):\n        U = d[\"inv\"] / (d[\"ps\"] if smooth else d[\"pred\"])\n        for tmax in (4.0, 6.0, d[\"shortest\"]):\n            m = (t_ax <= tmax) & np.isfinite(U)\n            f = cd.fit_exp(t_ax[m], U[m], 1, kappa=1.0)\n            rows.append(dict(silence=inc, smoothed=smooth, t_max=round(tmax, 2), bound_at_0=1 + f[\"alpha\"][0], tau1=f[\"tau\"][0],\n                             U_mean_0_100ms=float(np.mean(U[:100])), U_at_1s=float(U[1000]), U_at_3s=float(U[3000])))\nFIT4 = pd.DataFrame(rows)\nprint(FIT4.round(3).to_string())\nprint(\"paper: 1 + alpha1 = 0.51 (0.459-0.561), tau1 1.04 s (0.936-1.144)\")\n\"\"\", tags=[\"claim:fig4-predictability-upper-bound\"])\n\nmd(\"**Result: ...**\")\n\n# ------------------------------------------------------------------ timescale\nmd(r\"\"\"\n## timescale-longer-than-membrane\n\n> The trial-to-trial noise autocorrelation and the autocorrelation of spontaneous activity decay\n> within about 100 ms, much faster than the second-long timescale of context dependence in A1.\n\nNoise: residual of each trial from its context mean (Eq. 14) over the probe period, autocorrelation\nnormalized by its variance (Eq. 45), averaged over trials and probes. Spontaneous: the silences\nbetween sequences (whole, or without their first 1 s), up to the first test pulse in each. Decay:\nlag at which the mean autocorrelation first falls below 1/e (main) or 0.1 (variant).\n\"\"\")\n\ncode(r\"\"\"\nlags = np.arange(int(0.5 * cd.FS) + 1) / cd.FS\nac_noise = np.mean([cd.noise_autocorr(dict2) for dict2 in [cd.Probe(cell=p[\"cell\"], path=p[\"path\"], probe=p[\"probe\"], contexts=list(p[\"ctx\"]), traces=p[\"traces\"], n_trials=list(p[\"ntr\"]), duration=p[\"dur\"]) for p in NPf[True]]], axis=0)\nac_sp = {k: np.mean([o[\"spont_ac\"][k] for o in A1 if o.get(\"spont_ac\") and o[\"spont_ac\"][k] is not None], axis=0) for k in (0.0, 1.0)}\nnsp = {k: sum(1 for o in A1 if o.get(\"spont_ac\") and o[\"spont_ac\"][k] is not None) for k in (0.0, 1.0)}\nrows = [dict(series=\"trial noise (305 probes)\", lag_1e=cd.first_cross(lags, ac_noise, 1 / np.e), lag_01=cd.first_cross(lags, ac_noise, 0.1))]\nfor k in (0.0, 1.0):\n    rows.append(dict(series=f\"spontaneous, skip {k:.0f} s ({nsp[k]} files)\", lag_1e=cd.first_cross(lags, ac_sp[k], 1 / np.e), lag_01=cd.first_cross(lags, ac_sp[k], 0.1)))\nTS = pd.DataFrame(rows)\nprint(TS.to_string())\nprint(\"criterion: both 1/e lags < 0.150 s, and below a third of 1.04 s (0.347 s)\")\nprint(\"autocorrelation at 100 ms: noise %.3f, spontaneous %.3f\" % (ac_noise[100], ac_sp[0.0][100]))\n\"\"\", tags=[\"claim:timescale-longer-than-membrane\"])\n\nmd(\"**Result: ...**\")\n\n# ------------------------------------------------------------------ MGB\nmd(r\"\"\"\n## fig9-mgb-fast-decay\n\n> In the auditory thalamus (MGB), context dependence of spike responses decayed within a short time\n> (time constant about 80 ms; 93 probes in 14 cells), so the long-lasting component in A1 arises\n> mainly in cortex.\n\nPSTH in 100-ms bins from probe onset for each context, SD over contexts (n - 1), averaged over\nprobes (CxtDep.m, psth); one exponential with a free constant. Readings: bin time at its start or\ncentre; average over the probes still running or over all (ended probes as zero); silence counted\nor not.\n\"\"\")\n\ncode(r\"\"\"\nMP = {inc: [p for o in MG for p in o.get(\"probes\", []) if p[\"silence\"] == inc and p[\"rep\"] >= 10] for inc in (True, False)}\nfor inc in (True, False):\n    print(f\"silence counted={inc}: {len(MP[inc])} probes in {len({p['cell'] for p in MP[inc]})} cells\")\nrows = []\nSDC = {}\nfor inc in (True, False):\n    Sd = cd.stack_curves([p[\"sd\"] for p in MP[inc]], 61)\n    for denom in (\"running\", \"all\"):\n        y = np.nanmean(Sd, 0) if denom == \"running\" else np.nan_to_num(Sd).sum(0) / len(MP[inc])\n        SDC[(inc, denom)] = y\n        for pos in (\"start\", \"centre\"):\n            tb = np.arange(61) * 0.1 + (0.05 if pos == \"centre\" else 0.0)\n            f = cd.fit_exp(tb, y, 1, kappa=None)\n            late = float(np.nanmean(y[tb > 0.5]))\n            rows.append(dict(silence=inc, denom=denom, bin_time=pos, alpha1=f[\"alpha\"][0], tau1=f[\"tau\"][0], kappa=f[\"kappa\"],\n                             first_bin=y[0], second_bin=y[1], mean_after_0_5s=late, plateau_ratio=late / f[\"kappa\"]))\nFIT9 = pd.DataFrame(rows)\nprint(FIT9.round(3).to_string())\nprint(\"paper: alpha1 15.0 spike/s (13.5-16.5), tau1 0.080 s (0.072-0.088, or below 0.1 s), kappa 2.0 (1.8-2.2)\")\ny = SDC[(True, \"running\")]\nprint(\"mean SD by bin (silence counted, running probes):\", np.round(y[:12], 2))\n\"\"\", tags=[\"claim:fig9-mgb-fast-decay\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n## fig9-example-first-bin\n\n> In an example MGB unit, the response to a probe differed between contexts only in the first\n> 100-ms bin of the PSTH.\n\nAmong MGB probes with the design of Figure 9A (the Figure 2 sequence design, seven long natural\nfragments, three contexts of which one is silence, at least 10 trials), reproduced when at least one\nhas its SD over contexts in the first bin at least twice that of every later bin. The fraction of\nall probes with that pattern is reported.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor p in MP[True]:\n    sd = p[\"sd\"]\n    rows.append(dict(path=p[\"path\"], probe=p[\"probe\"], desc=p[\"desc\"], ctx=p[\"ctx\"], rep=p[\"rep\"], first=sd[0],\n                     max_later=sd[1:].max(), ratio=sd[0] / sd[1:].max() if sd[1:].max() > 0 else np.inf))\nE9 = pd.DataFrame(rows)\nE9[\"pattern\"] = E9.ratio >= 2\ndes = E9[E9.desc.str.contains(\"7 long\") & E9.ctx.apply(lambda c: len(c) == 3 and 0 in c)]\nprint(\"probes with the Figure 9A design:\", len(des), \"; with the first-bin pattern:\", int(des.pattern.sum()))\nprint(des[[\"path\", \"probe\", \"ctx\", \"rep\", \"first\", \"max_later\", \"ratio\"]].round(2).to_string())\nprint(f\"\\nall {len(E9)} probes: pattern in {int(E9.pattern.sum())} ({E9.pattern.mean():.3f}); with factor 1.5: {(E9.ratio >= 1.5).sum()}, factor 3: {(E9.ratio >= 3).sum()}\")\n\"\"\", tags=[\"claim:fig9-example-first-bin\"])\n\nmd(\"**Result: ...**\")\n\n# ------------------------------------------------------------------ fig7 search\nmd(r\"\"\"\n## fig7-example-frequency-context\n\n> In an example A1 neuron, a natural sound probe preceded by three DMR contexts that differed only\n> in frequency band gave significant context dependence for about 4 s.\n\nSearch (criterion): a recording with DMR contexts in 0.625-2.5, 2.5-10 and 10-40 kHz and a natural\nsound probe. The frequency bands of every DMR or TORC stimulus in the synthetic recordings are\nlisted from the stimulus parameters (`ff`, in Hz).\n\"\"\")\n\ncode(r\"\"\"\ntarget = [(625, 2500), (2500, 10000), (10000, 40000)]\nrows = []\nfor o in A1:\n    if o[\"group\"] != \"synthetic\" or o[\"desc\"] == \"tuning curve\":\n        continue\n    bands = [tuple(int(v) for v in s[2]) for s in o[\"stim\"] if s[2]]\n    kinds = sorted({s[1].split(\";\")[0].split(\":\")[0][:30] for s in o[\"stim\"]})\n    has_nat = any((\"Track\" in s[1]) for s in o[\"stim\"])\n    rows.append(dict(path=o[\"path\"], kinds=\", \".join(kinds), natural_probe=has_nat, bands=sorted(set(bands)),\n                     match=all(b in bands for b in target)))\nB = pd.DataFrame(rows)\nprint(\"synthetic recordings:\", len(B), \"; with all three Figure 7 bands:\", int(B.match.sum()), \"; with any of them:\",\n      int(B.bands.apply(lambda b: any(x in b for x in target)).sum()))\nseen = collections.Counter(str(b) for b in B.bands)\nfor k, v in seen.most_common():\n    print(f\"  {v:3d} recordings with bands {k}\")\n\"\"\", tags=[\"claim:fig7-example-frequency-context\"])\n\nmd(\"**Result: ...**\")\n\n# ------------------------------------------------------------------ silence probe\nmd(r\"\"\"\n## figs1-silence-probe\n\n> A subset of cells showed significant context dependence soon after the onset of the intersequence\n> silences, but the response power attributable to the preceding stimulus alone faded within about\n> 1 s after the stimulus ended.\n\nThe silence probe is the first 2.5 s after each sequence (CxtDep.m), its contexts the last fragment\nof each sequence. Reproduced when at least one cell has a significant period starting within 0.5 s\nof the silence onset, and the stimulus-related power (Eq. 17, averaged over silence probes) falls\nbelow 10% of its onset value (mean of the first 10 ms) by 1.1 s. Eq. 19 is a variant.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor p in SILP:\n    s = p[\"sig\"]\n    on = np.where(s)[0]\n    rows.append(dict(cell=p[\"cell\"], path=p[\"path\"], nctx=len(p[\"ctx\"]), rep=p[\"rep\"], any_sig=bool(s.any()),\n                     first_sig=on[0] / cd.FS if len(on) else np.nan))\nSP = pd.DataFrame(rows)\nSP = SP[SP.rep >= 4]\nearly = SP[SP.first_sig <= 0.5]\nprint(f\"silence probes {len(SP)} in {SP.cell.nunique()} cells; with any significant period {int(SP.any_sig.sum())}; \"\n      f\"starting within 0.5 s: {len(early)} probes in {early.cell.nunique()} cells\")\nTS2 = int(2.5 * cd.FS)\npredS = np.nanmean(cd.stack_curves([p[\"pred\"] for p in SILP if p[\"rep\"] >= 4], TS2), 0)\ndepS = np.nanmean(cd.stack_curves([p[\"dep\"] for p in SILP if p[\"rep\"] >= 4], TS2), 0)\ntS = np.arange(TS2) / cd.FS\nfor name, y in ((\"Eq. 17 (stimulus-related)\", predS), (\"Eq. 19 (context-dependent)\", depS)):\n    y0 = float(np.mean(y[:10]))\n    print(f\"{name}: onset {y0:.3f} mV^2, at 0.5 s {y[500]:.3f}, at 1.0 s {y[1000]:.3f}, at 2.0 s {y[2000]:.3f}; \"\n          f\"first below 10% of onset at {cd.first_cross(tS, y, 0.1 * y0):.3f} s\")\nnoise_sil = np.nanmean(cd.stack_curves([p[\"noise\"] for p in SILP if p[\"rep\"] >= 4], TS2), 0)\nprint(f\"noise floor of the silence probes: mean {noise_sil.mean():.4f}\")\n\"\"\", tags=[\"claim:figs1-silence-probe\"])\n\nmd(\"**Result: ...**\")\n\nmd(r\"\"\"\n## Claims not tested\n\n- fig5-example-conductances, fig6-conductance-decay: every file of the data set is a current-clamp\n  or cell-attached recording in mV (data check); the 42 voltage-clamp cells are not deposited.\n- fig8a-proportion-by-property and the claims that depend on it (fig8b-decay-by-property,\n  fig8a-significance-fits, fig8c-relative-effects, fig8-natural-synthetic-probes-alike): the\n  synthetic recordings are there, but which conditioning stimuli form the paper's amplitude,\n  frequency, AM, FM and higher-order sets (Table 1) is written in the notes of only 6 recordings.\n  The cell below lists the designs.\n- fig4-strf-performance-low: not run in this attempt (see the record).\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor o in A1:\n    if o[\"group\"] != \"synthetic\" or o[\"desc\"] == \"tuning curve\":\n        continue\n    descs = collections.Counter(s[1].split(\" From \")[0][:40] for s in o[\"stim\"])\n    rows.append(dict(design=o[\"desc\"][:60], stimuli=len(o[\"stim\"]), kinds=\"; \".join(sorted(k for k in descs))[:110]))\nD = pd.DataFrame(rows).groupby([\"design\", \"stimuli\", \"kinds\"]).size().rename(\"recordings\").reset_index()\nprint(D.to_string())\nn_notes = sum(1 for o in A1 if o[\"group\"] == \"synthetic\" and \"probe following synthetic sound variants\" in o[\"desc\"])\nprint(\"\\nrecordings whose notes name the property groups:\", n_notes)\n\"\"\")\n\nmd(r\"\"\"\n## Summary\n\n(filled after the run)\n\"\"\")\n\ncode(r\"\"\"\nprint(f\"notebook runtime {(time.time() - T0) / 60:.1f} min; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n\"\"\")\n\nnb[\"cells\"] = cells\nnb[\"metadata\"][\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbf.write(nb, \"entries/asari-2009/reproduce_asari_2009.ipynb\")\nprint(\"written\", len(cells), \"cells\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/build_nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/asari-2009; . $TMPDIR/dev/bin/activate; python $TMPDIR/build_nb.py && cat > $TMPDIR/run_nb.py <<'EOF'
import nbformat, sys, time
from nbclient import NotebookClient
nb=nbformat.read(sys.argv[1],as_version=4)
t=time.time()
c=NotebookClient(nb, timeout=7200, kernel_name='python3', resources={'metadata':{'path':'.'}}, allow_errors=True)
c.execute()
nbformat.write(nb, sys.argv[2])
print('done', time.time()-t)
for i,cell in enumerate(nb.cells):
    if cell.cell_type=='code':
        for o in cell.get('outputs',[]):
            if o.get('output_type')=='error': print('ERROR in cell',i,o['ename'],o['evalue'])
EOF
python -m ipykernel install --user --name python3 >/dev/null 2>&1; date -u; python $TMPDIR/run_nb.py reproduce_asari_2009.ipynb $TMPDIR/exec.ipynb; date -u
```

```
written 61 cells
Sun Nov 15 12:00:32 UTC 2026
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
done 328.9307532310486
Sun Nov 15 12:06:01 UTC 2026
```

**Agent**

Notebook ran in 5.5 minutes without errors. Reading the outputs.

**Agent calls Bash**

```bash
cd $TMPDIR; . dev/bin/activate; python - <<'EOF'
import nbformat
nb=nbformat.read('exec.ipynb',as_version=4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    for o in c.outputs:
        if o.output_type=='stream': print(f'--- cell {i}'); print(o.text[:6000])
        elif o.output_type=='error': print('ERR',o.ename,o.evalue)
EOF
```

```
--- cell 3
bucket listing of ac-1/:
  ac-1/                                                    0 bytes
  ac-1/checksums.md5                                     223 bytes
  ac-1/crcns-ac1-asari-results-1.zip              1470654524 bytes
  ac-1/crcns-ac1-asari-results-2.zip              1368844108 bytes
  ac-1/crcns-ac1.zip                              1348780283 bytes
  ac-1/filelist.txt                                      455 bytes
MD5 (checksums.md5) of the files read:
  crcns-ac1.zip                       2300ee76d93383ab8c808ddf16761a23
  crcns-ac1-asari-results-1.zip       18537da81d98e311c0274f62aea04daa
  crcns-ac1-asari-results-2.zip       2f7ab955cc778fc6839ce59ed51bce89

--- cell 3
 39 cells | Auditory cortical cell responses to natural sound combinations. | Asari and Zador (submitted) Long-lasting context dependence 
 14 cells | Thalamic cell responses to natural sound combinations. | Asari and Zador (submitted) Long-lasting context dependence 
 96 cells | Auditory cortical cell responses to synthetic sound combinations. | Asari and Zador (submitted) Long-lasting context dependence 
 12 cells | Auditory cortical cell responses to various acoustic stimuli. | Unpublished
 10 cells | Wehr | Repeated presentation of a fixed subset of sounds to auditory cortical cell.
 15 cells | Wehr | Auditory cortical responses to as many natural sounds as possible.
[... 309 more lines not kept]
```

**Agent**

Most claims came out cleanly. Two things to check: duplicate file paths in Summary.mat, and cell counts per synthetic ensemble type.

**Agent calls Bash**

```bash
cd entries/asari-2009; . $TMPDIR/dev/bin/activate; PYTHONPATH=. python - <<'EOF'
import ctxdep as cd, collections
S=cd.summary()
paths=collections.Counter(); where=collections.defaultdict(list)
for gi,g in enumerate(S):
    for c in g['cells']:
        for f in c['files']:
            paths[f]+=1; where[f].append((gi,c['cell'],tuple(c['files'])))
for f,n in paths.items():
    if n>1: print(f,n, where[f])
cellids=collections.Counter(c['cell'] for g in S for c in g['cells'])
print([k for k,v in cellids.items() if v>1])
print(sum(len(g['cells']) for g in S))
EOF
```

```
Results/20060314-ha1-001/20060314-ha1-001-001.mat 2 [(0, '20060314-ha1-001', ('Results/20060314-ha1-001/20060314-ha1-001-001.mat', 'Results/20060314-ha1-001/20060314-ha1-001-004.mat')), (2, '20060314-ha1-001', ('Results/20060314-ha1-001/20060314-ha1-001-001.mat', 'Results/20060314-ha1-001/20060314-ha1-001-002.mat', 'Results/20060314-ha1-001/20060314-ha1-001-003.mat'))]
Results/20060320-ha3-003/20060320-ha3-003-001.mat 2 [(0, '20060320-ha3-003', ('Results/20060320-ha3-003/20060320-ha3-003-001.mat', 'Results/20060320-ha3-003/20060320-ha3-003-003.mat')), (2, '20060320-ha3-003', ('Results/20060320-ha3-003/20060320-ha3-003-001.mat', 'Results/20060320-ha3-003/20060320-ha3-003-002.mat'))]
['20060314-ha1-001', '20060320-ha3-003']
161
```

**Agent calls Bash**

```bash
cd $TMPDIR/code; sed -n 1,200p wehr__Tools__STRFanalysis.m | grep -v "^\s*$" | head -150
```

```
function strf = STRFanalysis(data,PARAM)
% computes linear STRF filter and its performance.
% 
% 
% --- Input ---
%   data - structure containing 
%       .response : structure containing 
%           .evoked : cell for neural response traces
%           .sf : sampling frequency in Hz
%       .stimulus : structure containing
%           .samples : signal
%           .sf : sampling frequency
%
%   PARAM - structure containing parameters
%       .dt : temporal bin size (default: 0.01 sec)
%       .df : spectral bin size (default: 3 bins/octave)
%       .fmin : minimum frequency (default: 400 Hz)
%       .fmax : maximum frequency (default: 22100 Hz)
%       .xval : cross-validation (default: 10-fold)
%       .nbin : window length (default: 30 bins)
[... 131 more lines not kept]
```

**Agent**

I'll finish the main notebook and record first, then attempt the STRF claim on the Wehr data with whatever time is left. Updating the count cell (ensemble types) and the duplicate check.

**Agent calls Bash**

```bash
cd $TMPDIR; python - <<'EOF'
s=open('build_nb.py').read()
old='''for o in MG:
    for p in o.get("probes", []):
        pass
C = pd.DataFrame(rows)'''
new='''C = pd.DataFrame(rows)


def ens_kind(o):
    if o["group"] == "natural":
        return "natural"
    d = " ".join(st[1] for st in o.get("stim", []))
    for key, name in (("TORC", "TORC"), ("DMR", "DMR"), ("Modulated Harmonic Tone", "MHT"), ("pink noise", "MCN")):
        if key in d:
            return name
    return "naturalistic" if "naturalistic" in o["desc"] else "natural sound variants"


KIND = {o["path"]: ens_kind(o) for o in A1 if "counts" in o}
C["kind"] = C.path.map(KIND).fillna("mgb")'''
assert old in s; s=s.replace(old,new)
old2='''print("voltage-clamp recordings in the data set: 0 (see the data check)")'''
new2='''print("voltage-clamp recordings in the data set: 0 (see the data check)")
okk = C[C.ok & C.silence & (C.group != "mgb")]
byk = okk.groupby("kind").agg(probes=("probe", "size"), cells=("cell", "nunique"))
byk["paper_cells"] = byk.index.map({"natural": 39, "TORC": 14, "DMR": 6, "MHT": 39, "MCN": 27}).astype("float")
print("\\nA1 cells meeting the rule by ensemble (stimulus descriptions):")
print(byk.to_string())
print("sum of cells over ensembles:", int(byk.cells.sum()), "| over the paper's five ensembles:",
      int(byk.loc[[k for k in ("natural", "TORC", "DMR", "MHT", "MCN") if k in byk.index]].cells.sum()),
      "| distinct cells in those five:", okk[okk.kind.isin(["natural", "TORC", "DMR", "MHT", "MCN"])].cell.nunique())'''
assert old2 in s; s=s.replace(old2,new2)
old3='''md(r"""
Duplicates. Recordings deposited twice would have identical traces. Each file's trace extremes and
median, and its length, are compared across files.
""")'''
new3='''md(r"""
Duplicates. Recordings deposited twice would have identical traces. Each file's trace extremes and
median, and its length, are compared across distinct files; files that Summary.mat lists under more
than one experiment group are shown apart.
""")'''
assert old3 in s; s=s.replace(old3,new3)
old4='''key = F.assign(k=F.dur.round(4).astype(str) + "|" + F.vmin.round(4).astype(str) + "|" + F.vmax.round(4).astype(str) + "|" + F.vmedian.round(4).astype(str))
dups = key[key.duplicated("k", keep=False)].sort_values("k")
print("files sharing length, extremes and median:", len(dups))
print(dups[["path", "dur", "vmin", "vmax"]].to_string() if len(dups) else "none")'''
new4='''multi = F.groupby("path").group.agg(list)
multi = multi[multi.apply(len) > 1]
print("files listed in more than one experiment group of Summary.mat:")
print(multi.to_string() if len(multi) else "none")
cells_multi = F.groupby("cell").group.agg(lambda g: sorted(set(g)))
print("cells listed in more than one group:", cells_multi[cells_multi.apply(len) > 1].to_dict())
U = F.drop_duplicates("path")
key = U.assign(k=U.dur.round(4).astype(str) + "|" + U.vmin.round(4).astype(str) + "|" + U.vmax.round(4).astype(str) + "|" + U.vmedian.round(4).astype(str))
dups = key[key.duplicated("k", keep=False)].sort_values("k")
print("distinct files sharing length, extremes and median:", len(dups))
print(dups[["path", "dur", "vmin", "vmax"]].to_string() if len(dups) else "none")
print("distinct A1 whole-cell cells:", F[F.type == "Whole-cell"].cell.nunique(), "| MGB cells:", F[F.type == "Cell-attached"].cell.nunique())'''
assert old4 in s; s=s.replace(old4,new4)
open('build_nb.py','w').write(s)
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  python tools/entry.py --help 2>&1 | head -30; cat entries/fouke-2025/README.md | head -40; grep -n "python" entries/*/entry.yaml | head -3; ls entries/ito-2009
```

```
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
the entry, against the schemas, and applies the conventions that keep a result
[... 53 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat entries/ito-2009/entry.yaml; grep -rn "crcns" entries/*/entry.yaml | head -5
```

```
schema_version: 1
name: ito-2009
type: reproduction
title: Decision-making models and decision variables in the rat ventral basal ganglia (Ito and Doya 2009)
description: Tests the findings of Ito and Doya (2009) on dandiset 001641, which holds the behaviour of six
  rats in 70 sessions of a probabilistic free-choice task and 214 single units from the nucleus accumbens
  and ventral pallidum. It covers the trial counts and choice history (Fig. 2), the least-squares and
  maximum-likelihood fits of Markov and Q-learning models with constant and time-varying parameters
  (Fig. 3 to 5, Tables 1 to 3), and the coding of state, action, reward and action values by the neurons
  (Fig. 8 and 9).
license: Apache-2.0
notebooks:
- path: reproduce_ito_2009.ipynb
  title: Reproducing Ito and Doya (2009) from dandiset 001641
  runtime_minutes: 39
helpers:
- ito2009.py
related:
- id: dandi:001641/0.260922.0719
  relation: uses_data
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/asari-2009; cat > entry.yaml <<'EOF'
schema_version: 1
name: asari-2009
type: reproduction
title: Long-lasting context dependence in rat auditory cortex (Asari and Zador 2009)
description: Tests the findings of Asari and Zador (2009) on CRCNS ac-1, which holds the whole-cell
  current-clamp recordings of A1 neurons to sequences of natural and synthetic sounds, the
  cell-attached recordings of MGB units, and the earlier recordings of Wehr. It covers the cell and
  probe counts, firing rates, trial reliability, the significance and fractional power measures of
  context dependence and their time constants (Fig. 2 to 4), the timescale of membrane noise, the
  silence probes, and the fast decay in the thalamus (Fig. 9).
license: Apache-2.0
notebooks:
- path: reproduce_asari_2009.ipynb
  title: Reproducing Asari and Zador (2009) from CRCNS ac-1
  runtime_minutes: 6
helpers:
- ctxdep.py
related:
- id: crcns:ac-1/unversioned
  relation: uses_data
- id: doi:10.1152/jn.00577.2009
  relation: reproduces
EOF
printf "fsspec\naiohttp\nrequests\nnumpy\nscipy\npandas\nmatplotlib\n" > requirements.in
. $TMPDIR/dev/bin/activate; python $TMPDIR/build_nb.py; cd  python tools/entry.py lock entries/asari-2009 2>&1 | tail -3; python tools/entry.py check entries/asari-2009 2>&1 | tail -15
```

```
written 61 cells
  File "tools/entry.py", line 59, in <module>
    import yaml
ModuleNotFoundError: No module named 'yaml'
Traceback (most recent call last):
  File "tools/entry.py", line 59, in <module>
    import yaml
ModuleNotFoundError: No module named 'yaml'
```

**Agent calls Bash**

```bash
cd  uv run python tools/entry.py lock entries/asari-2009 2>&1 | tail -3; uv run python tools/entry.py check entries/asari-2009 2>&1 | tail -15
```

```
If this is intentional, set `export UV_LINK_MODE=copy` or use `--link-mode=copy` to suppress this warning.
Installed 24 packages in 1.59s
wrote asari-2009/requirements.lock.txt (Python 3.13, with hashes)
error: entries/asari-2009/reproduce_asari_2009.ipynb: neither the notebook nor a helper names version unversioned of dataset ac-1, which entry.yaml pins
1 error(s)
```

**Agent calls Bash**

```bash
cd  grep -n "names version" -B30 tools/entry.py | grep -n "def \|re\.\|in text\|crcns\|unversioned" | head -20
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  grep -rn "neither the notebook nor a helper" tools/ | head; grep -rn "def .*names.*version\|_names_dataset\|def dataset_named" tools/*.py tools/*/*.py | head
```

```
tools/entry.py:241:                report.error(rel / name, f"neither the notebook nor a helper names dataset {dandiset}")
tools/entry.py:244:                report.error(rel / name, f"neither the notebook nor a helper names version {version} "
```

**Agent calls Read**

```json
{
 "file_path": "tools/entry.py",
 "offset": 215,
 "limit": 32
}
```

```
215	
216	    # Datasets are related as <archive>:<id>/<version> (docs/archives.md); papers as doi:, entries as entry:.
217	    used = [r["id"].split(":", 1)[1].partition("/")
218	            for r in entry.get("related", []) if not r["id"].startswith(("doi:", "entry:"))]
219	    archives = {r["id"].split(":", 1)[1].partition("/")[0]: r["id"].split(":", 1)[0]
220	                for r in entry.get("related", []) if not r["id"].startswith(("doi:", "entry:"))}
221	    dandisets = [d for d, _, _ in used]
222	    versions = {d: v for d, _, v in used}
223	    if entry.get("type") in ("orientation", "reproduction"):
224	        if not dandisets:
225	            report.error(rel / "entry.yaml", "an orientation or reproduction entry must relate to a dataset")
226	        for d, v in versions.items():
227	            if not v:
228	                report.error(rel / "entry.yaml", f"pin the version of dataset {d}, as {archives[d]}:{d}/<version>")
229	    helper_code = "\n".join((entry_dir / h).read_text() for h in helpers if (entry_dir / h).is_file())
230	
231	    for name in [n for n in listed if n in present]:
232	        path = entry_dir / name
233	        nb = nbformat.read(path, as_version=4)
234	        if any(c.cell_type == "code" and (c.get("outputs") or c.get("execution_count")) for c in nb.cells):
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -i 's|^BASE = "https://crcnsarchive|DATASET = "crcns:ac-1/unversioned"   # CRCNS data sets are not versioned (docs/archives.md)\nBASE = "https://crcnsarchive|' entries/asari-2009/ctxdep.py; grep -n "DATASET\|^BASE" entries/asari-2009/ctxdep.py; date -u; uv run python tools/entry.py all entries/asari-2009 2>&1 | tail -15; date -u
```

```
49:DATASET = "crcns:ac-1/unversioned"   # CRCNS data sets are not versioned (docs/archives.md)
50:BASE = "https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-1/"
Sun Nov 15 12:08:00 UTC 2026
Installed kernelspec registry-asari-2009 in executed/asari-2009/.venv/share/jupyter/kernels/registry-asari-2009
0 error(s)
pass  reproduce_asari_2009.ipynb  (184 s)
Sun Nov 15 12:11:13 UTC 2026
```

**Agent**

Entry checks pass and the notebook runs in about 3 minutes under the locked environment. Reading the new count and duplicate outputs.

**Agent calls Bash**

```bash
cd  ls executed/asari-2009/; . $TMPDIR/dev/bin/activate; python - <<'EOF'
import nbformat
nb=nbformat.read('executed/asari-2009/reproduce_asari_2009.ipynb',as_version=4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    if i not in (10,14): continue
    for o in c.outputs:
        if o.output_type=='stream': print(f'--- cell {i}'); print(o.text[:5000])
        elif o.output_type=='error': print('ERR',o.ename,o.evalue)
EOF
```

```
reproduce_asari_2009.ipynb
result.json
--- cell 10
files listed in more than one experiment group of Summary.mat:
path
Results/20060314-ha1-001/20060314-ha1-001-001.mat    [natural, synthetic]
Results/20060320-ha3-003/20060320-ha3-003-001.mat    [natural, synthetic]
cells listed in more than one group: {'20060314-ha1-001': ['natural', 'synthetic'], '20060320-ha3-003': ['natural', 'synthetic']}
distinct files sharing length, extremes and median: 0
none
distinct A1 whole-cell cells: 145 | MGB cells: 14

--- cell 14
                   probes  cells
group     silence               
natural   False       305     39
          True        305     39
synthetic False       333     95
          True        333     95
silence counted=True: A1 cells meeting the criterion (natural and synthetic ensembles) 132 of 145 whole-cell cells in the data set
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd  uv run python - <<'EOF'
import json
s=json.load(open('schemas/attempt.schema.json'))
def find(d,path=''):
    if isinstance(d,dict):
        for k,v in d.items():
            if k in ('measured','outcome','blocked_by','findings','verifications','provenance','datasets','inputs','proposed'):
                print(path+'/'+k, json.dumps(v)[:900]); print()
            find(v,path+'/'+k)
    elif isinstance(d,list):
        for x in d: find(x,path)
find(s)
EOF
```

```
/properties/datasets {"description": "Every dataset the attempt used (docs/protocol.md, \"Record the attempt\").", "type": "array", "minItems": 1, "items": {"description": "A dataset the attempt used: the archive, the dataset's identifier there, the pinned version, and how the paper relates to it.", "type": "object", "additionalProperties": false, "required": ["archive", "id", "version", "relation"], "properties": {"archive": {"description": "The archive that holds the dataset, in lower case: dandi, ebrains, openneuro, dryad, zenodo, figshare and so on.", "type": "string", "pattern": "^[a-z][a-z0-9-]*$"}, "id": {"description": "The dataset's identifier in that archive, e.g. 000003 on DANDI.", "type": "string", "minLength": 1}, "version": {"description": "The version the attempt read, e.g. 0.220127.0436, or draft.", "type": "string", "minLength": 1}, "modified": {"description": "For a version that can still c

/properties/provenance {"type": "object", "additionalProperties": false, "required": ["kind", "accountable"], "properties": {"kind": {"enum": ["agent", "person"]}, "accountable": {"description": "The person or organisation responsible for this attempt.", "type": "object", "additionalProperties": false, "required": ["name"], "properties": {"name": {"type": "string"}, "orcid": {"type": "string", "pattern": "^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]$"}, "ror": {"type": "string"}}}, "agent": {"description": "Required when kind is agent.", "type": "object", "additionalProperties": false, "required": ["harness", "model", "protocol"], "properties": {"harness": {"type": "string"}, "model": {"type": "string"}, "protocol": {"description": "Version of the reproduction protocol the agent followed.", "type": "string"}}}, "runner": {"description": "Where the attempt was run: the platform, and the run that wrote this record

/properties/outcomes/items/properties/outcome {"enum": ["reproduced", "partially_reproduced", "not_reproduced", "blocked"], "description": "Describes th
[... 30 more lines not kept]
```

**Agent**

Writing conclusions next. First a quick check on recorded ages: the paper says 20 to 28 days, and some files say 29.

**Agent calls Bash**

```bash
cd $TMPDIR; . dev/bin/activate; python - <<'EOF'
import pickle,collections
r=pickle.load(open('survey.pkl','rb'))
c=collections.defaultdict(set)
for n,d in r.items():
    c[str(d['age'])].add(n.split('/')[1])
for k,v in sorted(c.items()): print(k, len(v), sorted(v)[:6])
EOF
```

```
20 5 ['20051215-ha1-001', '20051222-ha1-001', '20051225-ha3-001', '20060320-ha1-001', '20060329-ha1-001']
21 24 ['20051125-ha1-001', '20051226-ha1-001', '20051226-ha1-002', '20051226-ha2-001', '20051227-ha1-001', '20060202-ha2-001']
22 19 ['20051126-ha2-001', '20051126-ha2-002', '20051126-ha2-003', '20051203-ha1-001', '20051224-ha2-001', '20051228-ha1-001']
23 25 ['20051127-ha1-001', '20051127-ha1-002', '20060105-ha1-001', '20060216-ha2-002', '20060225-ha1-001', '20060225-ha2-001']
24 33 ['20051107-ha1-001', '20051107-ha1-002', '20060212-ha1-001', '20060212-ha2-001', '20060226-ha2-002', '20060402-ha1-001']
25 24 ['20051101-ha1-005', '20051108-ha1-001', '20051114-ha2-001', '20060220-ha1-005', '20060313-ha1-001', '20060313-ha1-002']
26 15 ['20051207-ha1-002', '20051207-ha2-001', '20051213-ha1-001', '20060314-ha1-001', '20060904-ha1-001', '20060909-ha1-001']
27 7 ['20060320-ha3-001', '20060320-ha3-003', '20071010-ha2-001', '20071010-ha2-002', '20071010-ha2-003', '20071010-ha2-004']
28 2 ['20071011-ha1-001', '20071011-ha1-002']
29 4 ['20071012-ha1-001', '20071012-ha1-002', '20071012-ha1-003', '20071012-ha1-004']
[] 1 ['20061229-ha2-004']
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; cat > patch2.py <<'EOF'
s=open('build_nb.py').read()
old='''print("animal age (days) as stored:", collections.Counter(F.age).most_common(12))'''
new='''ages = F.drop_duplicates("cell")
print("animal age (days) as stored, cells per age:", dict(sorted(collections.Counter(ages.age).items())))
print("cells outside the paper's 20 to 28 days or without an age:",
      ages[~ages.age.isin([str(a) for a in range(20, 29)])][["group", "cell", "age"]].values.tolist())'''
assert old in s; s=s.replace(old,new)
old='''      "| distinct cells in those five:", okk[okk.kind.isin(["natural", "TORC", "DMR", "MHT", "MCN"])].cell.nunique())'''
new=old+'''
print("the paper's per-ensemble cell counts (39 + 14 + 6 + 39 + 27) sum to", 39 + 14 + 6 + 39 + 27, "for 123 cells")'''
assert old in s; s=s.replace(old,new)
R = {}
R['methods-recording-counts'] = """**Result: partially reproduced.** The natural sound sample is exact: 305 probes in 39 cells under
both readings of silence. The MGB sample is exact: 93 probes in 14 cells. In A1, 132 of the 145
whole-cell cells in the data set meet the rule, against 123; restricted to the five ensembles the
paper names, 118 distinct cells. By ensemble, natural sounds (39) and TORCs (14) match, MCN gives 26
against 27, and DMR (15 against 6) and MHT (26 against 39) depend on how the mixed designs, a
natural probe after DMR or MHT variants, are assigned, which the files do not say. The two cells
listed in both the natural and the synthetic group of Summary.mat agree with the paper's ensemble
counts summing to 125 for 123 cells. The voltage-clamp counts (29 probes in 14 cells) cannot be
tested: the data set holds no voltage-clamp recording."""
R['a1-mgb-firing-rates'] = """**Result: partially reproduced, resting on an assumption (the A1 spike detector).** No single
reading puts all four means within tolerance. In A1, with the 15-mV detector on the sequence
recordings, the spontaneous and evoked means are 0.488 and 0.541 Hz (SD 0.608 and 0.677), both
within tolerance; over all recordings the spontaneous mean is 0.363 Hz. In MGB, over all recordings,
the spontaneous rate is 0.618 Hz over all silences or 0.817 Hz in the second before each stimulus,
and the evoked rate is 5.07 Hz (SD 11.46), against 0.78 and 11.4 Hz; the tuning-curve recordings
alone give 11.66 Hz evoked. Under the all-recordings reading the A1 means are below 1 Hz and the MGB
evoked mean is above 5 Hz, the claim's rule for partial; on the sequence recordings alone the MGB
evoked mean is 4.99 Hz."""
R['fig2-example-reliability'] = """**Result: reproduced.** The mean pairwise trial correlation is 0.310 +/- 0.098 over 39 cells (0.319 +/-
0.129 over 305 probes), against 0.31 +/- 0.09; the leave-one-out reading gives 0.436. One recording
with seven fragments and six trials (20051222-ha1-001) has a cell mean of 0.603 and 15 probe-context
values between 0.66 and 0.82, consistent with the example cell (0.61 and 0.74)."""
R['fig2-example-long-context'] = """**Result: reproduced.** Of 40 probes with the example's design in 10 recordings, 2 are significant
before 2 s, not between 2 and 4 s, and again after 4 s (last significant time 4.06 and 5.04 s). Over
all 305 probes, 18 have a significant period later than 4 s."""
R['fig3a-proportion-significant'] = """**Result: reproduced.** With silence counted as a context, 187 of 305 probes (61.3%) have a
significant period, within the tolerance of 204 (66.9%), and the late fraction is 0.251 with the
proportion taken over all probes (peak of the cumulative curve at 4.78 s, paper 4.72 s); over the
running probes it is 0.267, outside. Without silence 169 probes (55.4%) are significant and the late
fraction is 0.177, both outside. 36 of 39 cells have at least one significant probe."""
R['fig3a-significance-decay'] = """**Result: partially reproduced.** Two exponentials are selected under every reading with silence
counted. Over all probes from 0 to 4.72 s the sizes are 0.151 and 0.079 and the constants 0.253 and
0.974 s, with a constant of 0.0026: the slow constant and the noise floor are within tolerance, the
fast size, the fast constant and the slow size are not. Over the running probes the fast size is
within tolerance (0.162) and the slow constant is 1.09 s. Without silence one exponential is
selected (size 0.166, constant 0.316 s)."""
R['fig3b-fractional-power-decay'] = """**Result: partially reproduced.** Q(t) falls from 0.76 in the first 50 ms to 0.19 at 1 s. The fitted
size is 0.470 (0 to 4 s) or 0.466 (0 to 6 s), within tolerance, but the time constant is 1.73 or
1.78 s, outside 0.936 to 1.144 s. Without silence the constant is 1.27 s. A fit up to the shortest
probe (1.98 s) gives 1.12 s with a size of 0.554, just outside its tolerance. No reading puts both
values within tolerance; every reading gives a decay with a constant above one second."""
R['fig4-predictability-upper-bound'] = """**Result: partially reproduced.** The bound near probe onset matches: 1 + alpha1 is 0.498 with the
unsmoothed denominator and silence counted, 0.490 with the smoothed one without silence (0 to 6 s),
and the mean of Eq. 43 over the first 100 ms is 0.492 (smoothed, silence counted). The approach to
one is slower than the paper's: the time constant is 1.45 to 2.81 s in every fit to 4 or 6 s,
against 1.04 s, and the main reading (smoothed, silence counted, 0 to 4 s) gives 0.430 and 2.32 s,
both outside. The closest constant, 0.928 s, comes from a fit to 1.98 s, where the bound is 0.439."""
R['timescale-longer-than-membrane'] = """**Result: reproduced.** The noise autocorrelation falls below 1/e at 72 ms (below 0.1 at 115 ms)
and that of the spontaneous activity at 78 ms (76 ms without the first 1 s of each silence), all
under 150 ms and under a third of 1.04 s."""
R['fig9-mgb-fast-decay'] = """**Result: reproduced.** The mean SD of the PSTHs over 93 probes in 14 cells falls from 6.45 spikes/s
in the first bin to 2.04 in the second. With silence counted and the running probes, tau1 is 0.058
s and the mean after 0.5 s is 0.99 times the fitted constant; over all probes with bin starts tau1 is
0.080 s. The sizes are smaller than the paper's: alpha1 5.2 to 12.4 spikes/s against 15.0, and
kappa 0.81 to 1.21 against 2.0. Without silence the first bin is 2.50, and the fit over all probes
does not converge to a decay (tau1 at its bound of 100 s)."""
R['fig9-example-first-bin'] = """**Result: reproduced.** Of 12 probes with the Figure 9A design, 4 (all in 20071010-ha2-003) have a
first-bin SD at least twice that of every later bin (ratios 2.05 to 2.81). Over all 93 probes the
pattern holds in 35 (0.376)."""
R['fig7-example-frequency-context'] = """**Result: not testable.** None of the 105 synthetic recordings has contexts in all three bands of
Figure 7 (0.625-2.5, 2.5-10 and 10-40 kHz). The DMR frequency variants that precede a natural sound
probe span 0.25-1 to 8-32 kHz in two-octave bands."""
R['figs1-silence-probe'] = """**Result: reproduced.** Of 44 silence probes in 38 cells, 26 have a significant period, and 22 (in 19
cells) have one starting within 0.5 s of the silence onset. The stimulus-related power over the
silence probes falls from 5.61 mV^2 at onset to 1.34 at 0.5 s and below 10% of its onset value at
0.54 s (Eq. 19: 0.46 s). The noise floor of the silence probes is 0.0057."""
order = ['methods-recording-counts','a1-mgb-firing-rates','fig2-example-reliability','fig2-example-long-context',
 'fig3a-proportion-significant','fig3a-significance-decay','fig3b-fractional-power-decay','fig4-predictability-upper-bound',
 'timescale-longer-than-membrane','fig9-mgb-fast-decay','fig9-example-first-bin','fig7-example-frequency-context','figs1-silence-probe']
# replace placeholders in order
parts = s.split('md("**Result: ...**")')
first_placeholder = 'md(r"""\n**Result: ...** (filled after the run)\n""")'
s = s.replace(first_placeholder, 'md(r"""\n' + R[order[0]] + '\n""")', 1)
for k in order[1:]:
    s = s.replace('md("**Result: ...**")', 'md(r"""\n' + R[k] + '\n""")', 1)
assert '**Result: ...**' not in s
open('build_nb.py','w').write(s)
print('ok')
EOF
python patch2.py
```

```
ok
Shell cwd was reset to
```

**Agent**

Conclusions are in. Now the STRF claim: inspecting the Wehr recordings.

**Agent calls Bash**

```bash
cd entries/asari-2009; . $TMPDIR/dev/bin/activate; PYTHONPATH=. python - <<'EOF'
import ctxdep as cd, numpy as np, collections
W=cd.summary('wehr')
z=cd.open_zip('crcns-ac1.zip')
for g in W:
    print('==',g['description'])
    for c in g['cells']:
        d=collections.Counter(x.split(':')[0] for x in c['descriptions'])
        print('  ',c['cell'],len(c['files']),dict(d))
c=W[0]['cells'][0]
for f,dsc in list(zip(c['files'],c['descriptions']))[10:12]:
    m=cd.loadmat_member('crcns-ac1.zip','wehr/'+f)
    r=m['response']; p=m['param']; t=np.atleast_1d(m['triggers'])
    print(f, dsc, r.trace.shape, r.sf, r.unit, [ (x.type,x.time, x.param.__dict__ if hasattr(x.param,'__dict__') else x.param) for x in t][:3])
    print(p._fieldnames, p.recording.__dict__ if hasattr(p,'recording') else '')
    print(getattr(p,'stimulus',None).__dict__ if hasattr(p,'stimulus') else '')
EOF
```

```
== Repeated presentation of a fixed subset of sounds to auditory cortical cell.
   20020508-mw-003 152 {'tuning curve': 10, 'natural sound fragment (three-humped treehopper)': 20, 'natural sound fragment (bowhead whale)': 10, 'natural sound fragment (superb lyrebird)': 10, 'natural sound fragment (jaguar mating call)': 10, 'natural sound fragment (humpback whale)': 10, 'natural sound fragment (knudsens frog)': 10, 'natural sound fragment (tungara frog)': 10, 'silence': 11, 'music fragment (Jimi Hendrix': 10, 'natural sound fragment (smoky jungle frog)': 10, 'natural sound fragment (club-winged manakin)': 11, 'natural sound fragment (black-and-gold cotinga)': 10, 'white noise': 10}
   20020530-mw-001 119 {'natural sound fragment (humpback whale)': 10, 'natural sound fragment (smoky jungle frog + screaming piha)': 10, 'white noise': 5, 'natural sound fragment (knudsens frog)': 12, 'natural sound fragment (screaming piha + bearded manakin)': 10, 'natural sound fragment (tungara frog)': 10, 'silence': 11, 'natural sound fragment (olive oropendola)': 11, 'tuning curve': 26, 'natural sound fragment (jaguar mating call)': 14}
   20020602-mw-001 65 {'tuning curve': 15, 'natural sound fragment (humpback whale)': 10, 'natural sound fragment (knudsens frog)': 10, 'natural sound fragment (tungara frog)': 10, 'natural sound fragment (smoky jungle frog)': 10, 'natural sound fragment (club-winged manakin)': 10}
   20020604-mw-001 112 {'tuning curve': 6, 'natural sound fragment (humpback whale)': 6, 'natural sound fragment (knudsens frog)': 9, 'natural sound fragment (tungara frog)': 12, 'natural sound fragment (smoky jungle frog)': 10, 'natural sound fragment (club-winged manakin)': 10, 'natural sound fragment (black-and-gold cotinga)': 10, 'silence': 10, 'natural sound fragment (bowhead whale)': 10, 'natural sound fragment (superb lyrebird)': 10, 'natural sound fragment (jaguar mating call)': 19}
   20020604-mw-002 60 {'tuning curve': 6, 'natural sound fragment (humpback whale)':
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/asari-2009; . $TMPDIR/dev/bin/activate; PYTHONPATH=. python - <<'EOF'
import ctxdep as cd, numpy as np, time
z=cd.open_zip('crcns-ac1.zip')
t=time.time()
for f in ['wehr/Stimuli/fragments/1.mat','wehr/Stimuli/category2/1.mat']:
    m=cd.loadmat_member('crcns-ac1.zip',f)
    s=m['stimulus']; print(f, s._fieldnames, np.shape(s.sample), s.param.__dict__ if hasattr(s.param,'__dict__') else s.param, time.time()-t)
W=cd.summary('wehr')
c=W[1]['cells'][1]
for f,d in list(zip(c['files'],c['descriptions']))[:3]+list(zip(c['files'],c['descriptions']))[-3:]:
    m=cd.loadmat_member('crcns-ac1.zip','wehr/'+f); tr=np.atleast_1d(m['triggers'])
    print(d, m['response'].trace.shape, m['response'].sf, [(x.type,x.time,{k:v for k,v in x.param.__dict__.items() if k!='_fieldnames'}) for x in tr])
# fragment descriptions
for i in range(1,20):
    m=cd.loadmat_member('crcns-ac1.zip',f'wehr/Stimuli/fragments/{i}.mat'); s=m['stimulus']
    print(i, s.param.description if hasattr(s.param,'description') else '', np.shape(s.sample), s.param.sf)
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
AttributeError: 'mat_struct' object has no attribute 'sample'. Did you mean: 'samples'?
```

**Agent calls Bash**

```bash
cd entries/asari-2009; . $TMPDIR/dev/bin/activate; PYTHONPATH=. python - <<'EOF' 2>&1 | cut -c1-300
import ctxdep as cd, numpy as np, time
t=time.time()
for f in ['wehr/Stimuli/fragments/1.mat','wehr/Stimuli/category2/1.mat']:
    m=cd.loadmat_member('crcns-ac1.zip',f)
    s=m['stimulus']; print(f, s._fieldnames, np.shape(s.samples), {k:v for k,v in s.param.__dict__.items() if k!='_fieldnames'} if hasattr(s,'param') else '', time.time()-t)
W=cd.summary('wehr')
c=W[1]['cells'][1]
for f,d in list(zip(c['files'],c['descriptions']))[:2]+list(zip(c['files'],c['descriptions']))[-2:]:
    m=cd.loadmat_member('crcns-ac1.zip','wehr/'+f); tr=np.atleast_1d(m['triggers'])
    print(d, m['response'].trace.shape, m['response'].sf, [(x.type,x.time,{k:v for k,v in x.param.__dict__.items() if k!='_fieldnames'}) for x in tr])
for i in range(1,20):
    m=cd.loadmat_member('crcns-ac1.zip',f'wehr/Stimuli/fragments/{i}.mat'); s=m['stimulus']
    print(i, {k:v for k,v in s.param.__dict__.items() if k!='_fieldnames'} if hasattr(s,'param') else s._fieldnames, np.shape(s.samples))
EOF
```

```
wehr/Stimuli/fragments/1.mat ['samples', 'param'] (1464848,) {'description': 'jaguar mating call', 'sf': 97656} 1.1283092498779297
wehr/Stimuli/category2/1.mat ['samples', 'param'] (2197276,) {'description': 'natural sound stream (0-6.4 kHz), No.1', 'sf': 97656} 1.799297571182251
natural sound stream (0-6.4 kHz), No.1: Trial No.1 (132000,) 4000 [('nauralsound', 1, {'ramp': 20, 'duration': 22500.16384041943, 'description': 'natural sound stream (0-6.4 kHz), No.1', 'sf': 97656})]
natural sound stream (0-6.4 kHz), No.2: Trial No.2 (132000,) 4000 [('nauralsound', 1, {'ramp': 20, 'duration': 26000.15360039322, 'description': 'natural sound stream (0-6.4 kHz), No.2', 'sf': 97656})]
white noise: Trial No.9 (108000,) 4000 [('whitenoise', 4000, {'amplitude': 80, 'duration': 25, 'ramp': 5}), ('whitenoise', 8000, {'amplitude': 80, 'duration': 25, 'ramp': 5}), ('whitenoise', 12000, {'amplitude': 80, 'duration': 25, 'ramp': 5}), ('whitenoise', 16000, {'amplitude': 80, 'duration': 25,
white noise: Trial No.10 (108000,) 4000 [('whitenoise', 2004.7488000000003, {'amplitude': 80, 'duration': 25, 'ramp': 5}), ('whitenoise', 4009.4960000000005, {'amplitude': 80, 'duration': 25, 'ramp': 5}), ('whitenoise', 6014.248, {'amplitude': 80, 'duration': 25, 'ramp': 5}), ('whitenoise', 8018.995
1 {'description': 'jaguar mating call', 'sf': 97656} (1464848,)
2 {'description': 'superb lyrebird', 'sf': 97656} (1464848,)
3 {'description': 'three-humped treehopper', 'sf': 97656} (1464848,)
4 {'description': 'bowhead whale', 'sf': 97656} (1464848,)
5 {'description': 'humpback whale', 'sf': 97656} (1464848,)
6 {'description': 'knudsens frog', 'sf': 97656} (1464848,)
7 {'description': 'tungara frog', 'sf': 97656} (1464848,)
8 {'description': 'smoky jungle frog', 'sf': 97656} (1464848,)
9 {'description': 'club-winged manakin', 'sf': 97656} (1464848,)
10 {'description': 'black-and-gold cotinga', 'sf': 97656} (1464848,)
11 {'description': 'Jimi Hendrix: purple haze', 'sf': 97656} (3100599,)
12 {'descripti
[... 20 more lines not kept]
```

**Agent**

The stimuli are 15-s fragments (natural) and 22.5-s streams at 97.656 kHz, with one file per trial. Writing the STRF helper.

**Agent calls Write**

```json
{
 "file_path": "entries/asari-2009/strf.py",
 "content": "\"\"\"Linear (STRF) and linear-nonlinear encoding models on Wehr's recordings in CRCNS ac-1.\n\nPaper: Asari and Zador (2009), Methods, \"Neural encoding models\" and \"Model performance\"\n(Eqs. 46 to 53), and the claim fig4-strf-performance-low in claims/asari-2009.yaml.\n\nWhere each parameter comes from:\n\n- Spectrogram (Eq. 47): log-frequency bins at 3 per octave from 0.40 kHz (17 bins, to 20.3\n  kHz; the paper says 0.40 to 22 kHz, 17 bins), dB of the power; each frequency centred over\n  time, as in the authors' STRFanalysis.m (wehr/Tools in crcns-ac1.zip). The window h(t) is open:\n  Hann windows of 10 and 20 ms are the readings the claim names.\n- Time bins of 2^k ms for k = 2 to 10, 45 bins per model split as [45], [9, 36], [9, 8, 28], ...,\n  [9, 8, ..., 1], giving windows of 180 to 4052 ms and 765 parameters (Methods).\n- Response: the membrane potential, median filtered over 10 ms to clip spikes (Methods,\n  Analysis, as for the A1 data), averaged in 4-ms bins (the finest time bin; a reading the claim\n  names), each trial centred over time.\n- Ridge regression (Eq. 50) with 10-fold cross-validation, the ridge parameter chosen as the one\n  with the best mean validation performance over folds (Methods; STRFanalysis.m). The grid of\n  ridge values (13 values, 1e-4 to 1e2 times the mean eigenvalue of S'S) is a standard choice\n  wide enough that the chosen value is reported with its position in the grid. Folds are\n  contiguous blocks of the concatenated data (reading A) or whole stimuli (reading B).\n- Static nonlinearity (Eq. 51): robust lowess with a 5% span and 5 iterations on the training set,\n  applied to the validation set by linear interpolation (Methods).\n- Performance (Eq. 53): (total power - error power) / predictable power (Eq. 52), with the\n  predictable power estimated from the trials of each stimulus, on the training set (upper) and\n  the validation set (lower).\n\"\"\"\nfrom __future__ import annotations\n\nimport numpy as np\nfrom scipy import ndimage\nfrom statsmodels.nonparametric.smoothers_lowess import lowess\n\nimport ctxdep as cd\n\nDT = 0.004                     # s, finest time bin (2^2 ms)\nF_LO, NB_OCT, NF = 400.0, 3, 17\nCOUNTS = [[45], [9, 36], [9, 8, 28], [9, 8, 7, 21], [9, 8, 7, 6, 15], [9, 8, 7, 6, 5, 10],\n          [9, 8, 7, 6, 5, 4, 6], [9, 8, 7, 6, 5, 4, 3, 3], [9, 8, 7, 6, 5, 4, 3, 2, 1]]\nWIDTHS = [2 ** k for k in range(0, 9)]       # in 4-ms units: 4, 8, ..., 1024 ms\nRIDGE_SCALE = np.logspace(-4, 2, 13)\n\n\ndef window_ms(counts) -> int:\n    return int(sum(c * w * 4 for c, w in zip(counts, WIDTHS)))\n\n\ndef lag_bins(counts):\n    \"\"\"(start lag, width) in 4-ms units for each of the 45 bins, from near to distant past.\"\"\"\n    out, a = [], 0\n    for c, w in zip(counts, WIDTHS):\n        for _ in range(c):\n            out.append((a, w))\n            a += w\n    return out\n\n\ndef spectrogram(x: np.ndarray, sf: float, win_ms: float) -> np.ndarray:\n    \"\"\"dB power in 17 log-frequency bins, one frame every 4 ms (frame centred on the bin).\"\"\"\n    L = int(round(win_ms / 1000 * sf))\n    nfft = int(2 ** np.ceil(np.log2(L)))\n    w = np.hanning(L)\n    n = int(len(x) / sf / DT)\n    xp = np.concatenate([np.zeros(L), x, np.zeros(L)])\n    centres = (np.arange(n) * DT + DT / 2) * sf + L\n    idx = (centres[:, None] - L // 2 + np.arange(L)[None, :]).astype(int)\n    P = np.abs(np.fft.rfft(xp[idx] * w, nfft, axis=1)) ** 2\n    f = np.fft.rfftfreq(nfft, 1 / sf)\n    edges = F_LO * 2 ** (np.arange(NF + 1) / NB_OCT)\n    S = np.stack([P[:, (f >= edges[i]) & (f < edges[i + 1])].sum(axis=1) for i in range(NF)], axis=1)\n    S = 10 * np.log10(S + S.max() * 1e-8)\n    return S - S.mean(axis=0, keepdims=True)\n\n\ndef response_bins(trace: np.ndarray, sf: float, n: int) -> np.ndarray:\n    \"\"\"10-ms median filter, mean in 4-ms bins, centred.\"\"\"\n    v = ndimage.median_filter(trace.astype(float), size=int(round(0.010 * sf)))\n    k = int(round(DT * sf))\n    v = v[: n * k].reshape(-1, k).mean(axis=1)\n    return v - v.mean()\n\n\ndef design(S: np.ndarray, counts) -> np.ndarray:\n    \"\"\"Lagged features: mean of the spectrogram over each lag bin before (and including) t.\"\"\"\n    n = S.shape[0]\n    bins = lag_bins(counts)\n    maxlag = max(a + w for a, w in bins)\n    Sp = np.concatenate([np.zeros((maxlag, S.shape[1])), S])\n    C = np.concatenate([np.zeros((1, S.shape[1])), np.cumsum(Sp, axis=0)])\n    t = np.arange(n) + maxlag + 1             # index after time t in C\n    X = np.empty((n, len(bins) * S.shape[1]), np.float32)\n    for j, (a, w) in enumerate(bins):\n        X[:, j * S.shape[1]:(j + 1) * S.shape[1]] = (C[t - a] - C[t - a - w]) / w\n    return X\n\n\ndef performance(R_list, rhat, idx_list):\n    \"\"\"Eq. 53 over the time points idx of each stimulus; R_list holds (trials, T) arrays.\"\"\"\n    tot = err = pred = 0.0\n    n = 0\n    for R, rh, idx in zip(R_list, rhat, idx_list):\n        if len(idx) == 0:\n            continue\n        Rs = R[:, idx]\n        m = Rs.shape[0]\n        tot += (Rs ** 2).mean(axis=0).sum()\n        err += ((Rs - rh[idx]) ** 2).mean(axis=0).sum()\n        pred += ((m * Rs.mean(axis=0) ** 2 - (Rs ** 2).mean(axis=0)) / (m - 1)).sum()\n        n += len(idx)\n    return (tot - err) / pred, pred / n\n\n\ndef fit_cell(stims, counts, folds: str = \"blocks\", nfold: int = 10, ln: bool = True):\n    \"\"\"stims: list of (S spectrogram (T, 17), R trials (m, T)). Returns performances.\"\"\"\n    Xs = [design(S, counts) for S, _ in stims]\n    ys = [R.mean(axis=0) for _, R in stims]\n    lens = [len(y) for y in ys]\n    off = np.concatenate([[0], np.cumsum(lens)])\n    X = np.concatenate(Xs).astype(np.float64)\n    y = np.concatenate(ys)\n    N = len(y)\n    if folds == \"blocks\":\n        edges = np.linspace(0, N, nfold + 1).astype(int)\n        fold_of = np.searchsorted(edges, np.arange(N), side=\"right\") - 1\n    else:\n        order = np.arange(len(stims)) % nfold\n        fold_of = np.concatenate([np.full(L, order[i]) for i, L in enumerate(lens)])\n    XtX = X.T @ X\n    Xty = X.T @ y\n    lam0 = np.trace(XtX) / X.shape[1]\n    res = {s: dict(tr=[], va=[]) for s in RIDGE_SCALE}\n    W_all = {}\n    for k in range(nfold):\n        v = fold_of == k\n        if not v.any():\n            continue\n        A = XtX - X[v].T @ X[v]\n        b = Xty - X[v].T @ y[v]\n        ev, U = np.linalg.eigh(A)\n        Ub = U.T @ b\n        for s in RIDGE_SCALE:\n            w = U @ (Ub / (ev + s * lam0))\n            W_all[(k, s)] = w\n            rh = X @ w\n            rh_list = [rh[off[i]:off[i + 1]] for i in range(len(stims))]\n            va_idx = [np.where(v[off[i]:off[i + 1]])[0] for i in range(len(stims))]\n            tr_idx = [np.where(~v[off[i]:off[i + 1]])[0] for i in range(len(stims))]\n            res[s][\"va\"].append(performance([R for _, R in stims], rh_list, va_idx)[0])\n            res[s][\"tr\"].append(performance([R for _, R in stims], rh_list, tr_idx)[0])\n    best = max(RIDGE_SCALE, key=lambda s: np.mean(res[s][\"va\"]))\n    out = dict(window_ms=window_ms(counts), ridge_scale=best, ridge_pos=int(np.where(RIDGE_SCALE == best)[0][0]),\n               lin_va=float(np.mean(res[best][\"va\"])), lin_tr=float(np.mean(res[best][\"tr\"])))\n    if ln:\n        va_l, tr_l = [], []\n        for k in range(nfold):\n            v = fold_of == k\n            if not v.any():\n                continue\n            rh = X @ W_all[(k, best)]\n            fit = lowess(y[~v], rh[~v], frac=0.05, it=5, delta=0.005 * np.ptp(rh[~v]), return_sorted=True)\n            xs, ix = np.unique(fit[:, 0], return_index=True)\n            g = np.interp(rh, xs, fit[ix, 1])\n            g_list = [g[off[i]:off[i + 1]] for i in range(len(stims))]\n            va_idx = [np.where(v[off[i]:off[i + 1]])[0] for i in range(len(stims))]\n            tr_idx = [np.where(~v[off[i]:off[i + 1]])[0] for i in range(len(stims))]\n            va_l.append(performance([R for _, R in stims], g_list, va_idx)[0])\n            tr_l.append(performance([R for _, R in stims], g_list, tr_idx)[0])\n        out.update(ln_va=float(np.mean(va_l)), ln_tr=float(np.mean(tr_l)))\n    return out\n\n\ndef load_cell(cell: dict, stim_cache: dict, win_ms: float, min_trials: int = 2):\n    \"\"\"Natural sound trials of one Wehr cell, grouped by stimulus; stimuli with >= min_trials.\"\"\"\n    groups = {}\n    for f, d in zip(cell[\"files\"], cell[\"descriptions\"]):\n        if not d.startswith(\"natural sound\"):\n            continue\n        groups.setdefault(d.split(\": Trial\")[0], []).append(f)\n    stims = []\n    for desc, files in groups.items():\n        if len(files) < min_trials:\n            continue\n        key = (desc, win_ms)\n        if key not in stim_cache:\n            stim_cache[key] = None\n        trials, sf, sdesc = [], None, None\n        for f in files:\n            m = cd.loadmat_member(\"crcns-ac1.zip\", \"wehr/\" + f)\n            tr = np.atleast_1d(m[\"triggers\"])[0]\n            sf = float(m[\"response\"].sf)\n            x = m[\"response\"].trace.astype(float) * float(getattr(m[\"response\"], \"scale\", 1.0))\n            on = int(tr.time) - 1\n            dur = float(tr.param.duration) / 1000\n            sdesc = str(tr.param.description)\n            trials.append((x[on:], dur))\n        if stim_cache[key] is None:\n            stim_cache[key] = spectrogram(STIMULI[sdesc], 97656.0, win_ms)\n        S = stim_cache[key]\n        n = min([S.shape[0]] + [int(len(x) / sf / DT) for x, _ in trials])\n        R = np.array([response_bins(x, sf, n) for x, _ in trials])\n        stims.append((S[:n], R))\n    return stims\n\n\nSTIMULI: dict = {}\n\n\ndef load_stimuli():\n    \"\"\"All Wehr stimulus waveforms, by description.\"\"\"\n    z = cd.open_zip(\"crcns-ac1.zip\")\n    for n in z.namelist():\n        if n.startswith(\"wehr/Stimuli/\") and n.endswith(\".mat\"):\n            s = cd.loadmat_member(\"crcns-ac1.zip\", n)[\"stimulus\"]\n            STIMULI[str(s.param.description)] = np.asarray(s.samples, float)\n    return STIMULI\n"
}
```

```
File created successfully at: entries/asari-2009/strf.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/asari-2009; . $TMPDIR/dev/bin/activate; uv pip install -q statsmodels 2>&1|tail -1; PYTHONPATH=. python - <<'EOF'
import time, resource, numpy as np, ctxdep as cd, strf
t=time.time(); strf.load_stimuli(); print('stimuli', len(strf.STIMULI), time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
W=cd.summary('wehr')
cache={}
c=W[0]['cells'][0]
t=time.time(); st=strf.load_cell(c, cache, 10); print('cell load', time.time()-t, [(S.shape,R.shape) for S,R in st][:3], len(st))
for counts in (strf.COUNTS[0], strf.COUNTS[-1]):
    t=time.time(); r=strf.fit_cell(st, counts); print(r, time.time()-t)
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
EOF
```

```
stimuli 51 26.647164344787598 1.17766
cell load 11.308079481124878 [((3750, 17), (20, 3750)), ((3750, 17), (10, 3750)), ((3750, 17), (10, 3750))] 10
{'window_ms': 180, 'ridge_scale': np.float64(10.0), 'ridge_pos': 10, 'lin_va': 0.17781921661096328, 'lin_tr': 0.2925549007507048, 'ln_va': 0.10012378796504147, 'ln_tr': 0.2987542852889894} 3.5100831985473633
{'window_ms': 4052, 'ridge_scale': np.float64(10.0), 'ridge_pos': 10, 'lin_va': 0.18961256161506884, 'lin_tr': 0.320646824931371, 'ln_va': 0.10608836325453208, 'ln_tr': 0.31861887215773677} 3.527116298675537
1.616916
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build_strf.py",
 "content": "import nbformat as nbf\n\ncells = []\n\n\ndef md(s):\n    cells.append(nbf.v4.new_markdown_cell(s.strip(\"\\n\")))\n\n\ndef code(s, tags=None):\n    c = nbf.v4.new_code_cell(s.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\nmd(r\"\"\"\n# Asari and Zador (2009): STRF and LN model performance on Wehr's recordings (CRCNS ac-1)\n\nPaper: doi:10.1152/jn.00577.2009, Figure 4 and Methods, \"Neural encoding models\" and \"Model\nperformance\". Dataset: CRCNS ac-1, `unversioned` (MD5 sums printed below), the folder `wehr/` of\n`crcns-ac1.zip`, which holds the recordings of Machens et al. (2004) that the paper reanalysed.\n\nThis notebook tests one claim, fig4-strf-performance-low; the other claims are in\n`reproduce_asari_2009.ipynb`. Every method detail and its source is in the docstring of\n`strf.py`.\n\n| Claim | Tested here |\n|---|---|\n| fig4-strf-performance-low | tested |\n\"\"\")\n\ncode(r\"\"\"\nimport time, resource, collections\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nimport matplotlib.pyplot as plt\nimport ctxdep as cd\nimport strf\n\nT0 = time.time()\npd.set_option(\"display.width\", 200)\nmd5 = cd.checksums()\nprint(\"crcns-ac1.zip MD5:\", md5[\"crcns-ac1.zip\"])\nW = cd.summary(\"wehr\")\nstrf.load_stimuli()\nprint(\"stimulus waveforms:\", len(strf.STIMULI), \"| loaded in %.0f s\" % (time.time() - T0))\n\"\"\")\n\nmd(\"## Data check\")\n\ncode(r\"\"\"\nrows = []\nfor g in W:\n    for c in g[\"cells\"]:\n        nat = collections.Counter(d.split(\": Trial\")[0] for d in c[\"descriptions\"] if d.startswith(\"natural sound\"))\n        rep = [v for v in nat.values() if v >= 2]\n        rows.append(dict(group=g[\"description\"][:40], cell=c[\"cell\"], files=len(c[\"files\"]), natural_stimuli=len(nat),\n                         stimuli_2plus_trials=len(rep), trials_median=float(np.median(list(nat.values()))) if nat else 0))\nCELLS = pd.DataFrame(rows)\nprint(CELLS.to_string())\nUSE = CELLS[CELLS.stimuli_2plus_trials >= 2].cell.tolist()\nprint(f\"\\n{len(CELLS)} cells in wehr/; {len(USE)} have at least two natural sound stimuli with at least two trials, \"\n      \"which Eq. 52 needs; the paper used 20 cells and does not list them\")\nmissing = sorted({d.split(\": Trial\")[0] for g in W for c in g[\"cells\"] for d in c[\"descriptions\"] if d.startswith(\"natural sound\")}\n                 - {k for k in strf.STIMULI} - {\"natural sound fragment (\" + k + \")\" for k in strf.STIMULI})\nprint(\"trial descriptions without a stimulus file of that name:\", missing[:5], len(missing))\n\"\"\", tags=[\"sanity\"])\n\ncode(r\"\"\"\ncache = {}\nDATA = {}\nt = time.time()\ncellmap = {c[\"cell\"]: c for g in W for c in g[\"cells\"]}\nfor name in USE:\n    for win in (10, 20):\n        DATA[(name, win)] = strf.load_cell(cellmap[name], cache, win)\nd0 = DATA[(USE[0], 10)]\nprint(\"loaded %d cells in %.0f s\" % (len(USE), time.time() - t))\nsumm = pd.DataFrame([dict(cell=n, stimuli=len(DATA[(n, 10)]), trials=sum(R.shape[0] for _, R in DATA[(n, 10)]),\n                          seconds=sum(R.shape[1] for _, R in DATA[(n, 10)]) * strf.DT,\n                          vm_sd=np.mean([R.std() for _, R in DATA[(n, 10)]])) for n in USE])\nprint(summ.round(2).to_string())\nS0 = d0[0][0]\nprint(\"spectrogram: %d frames x %d bands, dB range after centring %.1f to %.1f\" % (S0.shape[0], S0.shape[1], S0.min(), S0.max()))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nClock check: the trial-averaged response must follow the stimulus. A model with the 180-ms window\nfitted on the true alignment is compared with one fitted after shifting the response by half the\nstimulus length (circularly), on the first cell.\n\"\"\")\n\ncode(r\"\"\"\nst = DATA[(USE[0], 10)]\ntrue = strf.fit_cell(st, strf.COUNTS[0], ln=False)\nshifted = [(S, np.roll(R, R.shape[1] // 2, axis=1)) for S, R in st]\nsh = strf.fit_cell(shifted, strf.COUNTS[0], ln=False)\nprint(f\"{USE[0]}: validation performance true alignment {true['lin_va']:.3f}, shifted {sh['lin_va']:.3f}\")\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\n## fig4-strf-performance-low\n\n> Linear STRF models of 20 A1 cells from Machens et al. (2004) predicted less than about 20% of the\n> predictable response power, and extending the window from 180 ms to about 4 s did not improve them\n> significantly, with or without a static nonlinearity; the LN model did only slightly better.\n\nMain reading: 10-ms Hann window, contiguous folds, all nine windows. Readings at 180 and 4052 ms:\n20-ms Hann window, and folds by stimulus.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nt = time.time()\nfor name in USE:\n    for k, counts in enumerate(strf.COUNTS):\n        r = strf.fit_cell(DATA[(name, 10)], counts, folds=\"blocks\")\n        rows.append(dict(cell=name, reading=\"hann10/blocks\", **r))\n    for win, folds in ((20, \"blocks\"), (10, \"stimulus\")):\n        for counts in (strf.COUNTS[0], strf.COUNTS[-1]):\n            r = strf.fit_cell(DATA[(name, win)], counts, folds=folds)\n            rows.append(dict(cell=name, reading=f\"hann{win}/{folds}\", **r))\nPERF = pd.DataFrame(rows)\nprint(\"fits: %d in %.0f s\" % (len(PERF), time.time() - t))\nprint(\"ridge value chosen at grid position (0 to 12):\", dict(collections.Counter(PERF.ridge_pos)))\n\"\"\", tags=[\"claim:fig4-strf-performance-low\"])\n\ncode(r\"\"\"\nmain = PERF[PERF.reading == \"hann10/blocks\"]\ntab = main.groupby(\"window_ms\")[[\"lin_va\", \"lin_tr\", \"ln_va\", \"ln_tr\"]].agg([\"mean\", \"sem\"])\nprint(tab.round(3).to_string())\nprint(\"\\nmaximum over windows of the mean: STRF validation %.3f, training %.3f; LN validation %.3f, training %.3f\"\n      % tuple(main.groupby(\"window_ms\")[c].mean().max() for c in (\"lin_va\", \"lin_tr\", \"ln_va\", \"ln_tr\")))\nprint(\"criterion: at most 0.22 at every window for STRF and LN, under one reading\")\nfor rd in PERF.reading.unique():\n    d = PERF[PERF.reading == rd]\n    print(rd, d.groupby(\"window_ms\")[[\"lin_va\", \"lin_tr\", \"ln_va\", \"ln_tr\"]].mean().round(3).to_dict(\"index\"))\n\"\"\", tags=[\"claim:fig4-strf-performance-low\"])\n\ncode(r\"\"\"\ndef wil(d, col):\n    a = d[d.window_ms == 180].set_index(\"cell\")[col]\n    b = d[d.window_ms == 4052].set_index(\"cell\")[col]\n    diff = (b - a).dropna()\n    p = stats.wilcoxon(diff, alternative=\"greater\").pvalue\n    return diff.median(), p, int((diff > 0).sum()), len(diff)\n\n\nfor rd in PERF.reading.unique():\n    d = PERF[PERF.reading == rd]\n    for col in (\"lin_va\", \"ln_va\"):\n        m, p, npos, n = wil(d, col)\n        print(f\"{rd:16s} {col}: 4052 minus 180 ms median {m:+.4f}, improved in {npos} of {n} cells, one-sided Wilcoxon p = {p:.4f}\")\nfor col in (\"lin_va\", \"ln_va\"):\n    piv = main.pivot(index=\"cell\", columns=\"window_ms\", values=col)\n    print(f\"Friedman over nine windows ({col}): chi2 = {stats.friedmanchisquare(*[piv[c] for c in piv.columns]).statistic:.2f}, \"\n          f\"p = {stats.friedmanchisquare(*[piv[c] for c in piv.columns]).pvalue:.4f}\")\ngain = (main.ln_va - main.lin_va)\nprint(f\"LN minus STRF, validation: mean {gain.mean():+.3f}; training: mean {(main.ln_tr - main.lin_tr).mean():+.3f}\")\n\"\"\", tags=[\"claim:fig4-strf-performance-low\"])\n\ncode(r\"\"\"\nm = main.groupby(\"window_ms\")[[\"lin_va\", \"lin_tr\", \"ln_va\", \"ln_tr\"]].mean()\nfig, ax = plt.subplots(figsize=(6, 4))\nfor c, st_ in ((\"lin_va\", \"x-\"), (\"lin_tr\", \"o-\"), (\"ln_va\", \"x--\"), (\"ln_tr\", \"o--\")):\n    ax.plot(m.index / 1000, m[c], st_, label=c)\nax.set_xlabel(\"window length (s)\"); ax.set_ylabel(\"model performance (Eq. 53)\"); ax.set_ylim(0, 1); ax.legend(fontsize=8)\nprint(\"plotted range: %.3f to %.3f\" % (m.values.min(), m.values.max()))\nplt.show()\n\"\"\", tags=[\"claim:fig4-strf-performance-low\"])\n\nmd(r\"\"\"\n**Result: ...**\n\"\"\")\n\ncode(r\"\"\"\nprint(f\"runtime {(time.time() - T0) / 60:.1f} min; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n\"\"\")\n\nnb = nbf.v4.new_notebook()\nnb[\"cells\"] = cells\nnb[\"metadata\"][\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbf.write(nb, \"entries/asari-2009/strf_asari_2009.ipynb\")\nprint(\"written\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/build_strf.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/asari-2009; . $TMPDIR/dev/bin/activate; python $TMPDIR/build_strf.py; date -u; python $TMPDIR/run_nb.py strf_asari_2009.ipynb $TMPDIR/strf_exec.ipynb 2>&1 | grep -v WARNING; date -u; python - <<'EOF'
import nbformat
nb=nbformat.read('/tmp/claude-1001/strf_exec.ipynb',as_version=4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    for o in c.outputs:
        if o.output_type=='stream': print(f'--- cell {i}'); print(o.text[:5000])
        elif o.output_type=='error': print('ERR',o.ename,o.evalue)
EOF
```

```
written
Sun Nov 15 12:16:29 UTC 2026
done 1297.9122183322906
Sun Nov 15 12:38:07 UTC 2026
--- cell 1
crcns-ac1.zip MD5: 2300ee76d93383ab8c808ddf16761a23

--- cell 1
stimulus waveforms: 51 | loaded in 28 s

--- cell 3
                                       group             cell  files  natural_stimuli  stimuli_2plus_trials  trials_median
0   Repeated presentation of a fixed subset   20020508-mw-003    152               10                    10           10.0
1   Repeated presentation of a fixed subset   20020530-mw-001    119                7                     7           10.0
2   Repeated presentation of a fixed subset   20020602-mw-001     65                5                     5           10.0
3   Repeated presentation of a fixed subset   20020604-mw-001    112                9                     9           10.0
4   Repeated presentation of a fixed subset   20020604-mw-002     60                3                     3           20.0
5   Repeated presentation of a fixed subset   20020604-mw-003    168                8                     8           20.0
6   Repeated presentation of a fixed subset   20020605-mw-002     95                5                     5           10.0
7   Repeated presentation of a fixed subset   20020605-mw-003     80                3                     3           20.0
[... 85 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; python - <<'EOF'
s=open('build_strf.py').read()
R='''**Result: partially reproduced, resting on the claims file's test and on the cell selection.** Over
16 cells, the mean validation (lower) performance is 0.130 to 0.152 for the STRF and 0.084 to 0.121
for the LN model at every window, below 0.22; the training (upper) estimates are 0.205 to 0.249 and
0.234 to 0.289. Extending the window improves the models a little, and the one-sided Wilcoxon test
of 4052 against 180 ms finds the improvement: median +0.016 for the STRF (11 of 16 cells, p =
0.0038) and +0.023 for the LN model (14 of 16, p = 0.017), with p from 0.0038 to 0.033 under the
other readings. The LN model is worse than the STRF on validation data (mean difference -0.038)
and better on training data (+0.040). So performance is low, as the paper says, but the absence
of an improvement and the small LN gain are not reproduced.'''
s=s.replace('md(r"""\n**Result: ...**\n""")','md(r"""\n'+R+'\n""")')
open('build_strf.py','w').write(s)
b=open('build_nb.py').read()
b=b.replace("| fig4-strf-performance-low | blocked |","| fig4-strf-performance-low | tested in `strf_asari_2009.ipynb` |")
b=b.replace('''- fig4-strf-performance-low: not run in this attempt (see the record).
''','')
summary='''md(r"""
## Summary

| Claim | Outcome |
|---|---|
| methods-recording-counts | partially reproduced: natural sound (305 probes, 39 cells) and MGB (93, 14) samples exact; 132 A1 cells meet the rule against 123; no voltage-clamp data |
| a1-mgb-firing-rates | partially reproduced (assumption: A1 spike detector) |
| fig2-example-reliability | reproduced |
| fig2-example-long-context | reproduced |
| fig3a-proportion-significant | reproduced |
| fig3a-significance-decay | partially reproduced |
| fig3b-fractional-power-decay | partially reproduced: time constant 1.3 to 1.8 s against 1.04 s |
| timescale-longer-than-membrane | reproduced |
| fig4-predictability-upper-bound | partially reproduced: bound 0.49 to 0.50 matches, time constant longer |
| fig4-strf-performance-low | partially reproduced (`strf_asari_2009.ipynb`) |
| fig5-example-conductances, fig6-conductance-decay | blocked: no voltage-clamp recordings |
| fig8a, fig8b, fig8a-significance-fits, fig8c, fig8-natural-synthetic-probes-alike | blocked: property groups of the synthetic stimuli not documented |
| fig9-mgb-fast-decay | reproduced |
| fig9-example-first-bin | reproduced |
| fig7-example-frequency-context | blocked: no recording with the example's design |
| figs1-silence-probe | reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and
the differences from the paper's method.

How the analysis differs from the paper's. It runs at 1 kHz on the 10-ms median-filtered membrane
potential where the paper used 0.1 ms; on the probes of one recording both give the same
significant periods (agreement 0.997 to 1.000). Probe construction, the silence context and
probe, and the trial truncation follow the authors' code deposited with the data (CxtDep.m). A1
spikes are detected automatically, where the paper did it by hand. Fit ranges, the probes averaged at
each time, and the bin times of the MGB PSTH are run as readings.

What was found about the dataset. It holds no voltage-clamp recording, so Figures 5 and 6 cannot
be tested. It holds 145 of the 194 A1 current-clamp cells and 14 of the 16 MGB cells, including all
the cells of the natural sound and MGB analyses. Which synthetic stimuli form the paper's property
groups is written in the notes of 6 of 105 synthetic recordings only. Two cells are listed in both
the natural and the synthetic group of Summary.mat. Four MGB cells come from an animal recorded as
29 days old, outside the paper's 20 to 28 days, and one cell has no age. The trigger times share the
clock of the traces (data check). The data set includes the authors' analysis code, which settles
several details the paper leaves open.
""")'''
b=b.replace('''md(r"""
## Summary

(filled after the run)
""")''', summary)
open('build_nb.py','w').write(b)
print('ok')
EOF
cd entries/asari-2009; . $TMPDIR/dev/bin/activate; python $TMPDIR/build_nb.py; python $TMPDIR/build_strf.py; grep -c "Result: \.\.\." reproduce_asari_2009.ipynb strf_asari_2009.ipynb
```

```
ok
written 61 cells
written
reproduce_asari_2009.ipynb:0
strf_asari_2009.ipynb:0
```

**Agent calls Bash**

```bash
cd entries/asari-2009; python3 - <<'EOF'
s=open('entry.yaml').read()
s=s.replace("""  runtime_minutes: 6
helpers:
- ctxdep.py""","""  runtime_minutes: 4
- path: strf_asari_2009.ipynb
  title: STRF and LN model performance on Wehr's recordings in CRCNS ac-1
  runtime_minutes: 22
helpers:
- ctxdep.py
- strf.py""")
s=s.replace("silence probes, and the fast decay in the thalamus (Fig. 9).","silence probes, the fast decay in the thalamus (Fig. 9), and the STRF and LN model performance\n  on the Wehr cells (Fig. 4).")
open('entry.yaml','w').write(s)
EOF
echo statsmodels >> requirements.in; cat entry.yaml requirements.in; cd  uv run python tools/entry.py lock entries/asari-2009 2>&1 | tail -1; date -u
```

```
schema_version: 1
name: asari-2009
type: reproduction
title: Long-lasting context dependence in rat auditory cortex (Asari and Zador 2009)
description: Tests the findings of Asari and Zador (2009) on CRCNS ac-1, which holds the whole-cell
  current-clamp recordings of A1 neurons to sequences of natural and synthetic sounds, the
  cell-attached recordings of MGB units, and the earlier recordings of Wehr. It covers the cell and
  probe counts, firing rates, trial reliability, the significance and fractional power measures of
  context dependence and their time constants (Fig. 2 to 4), the timescale of membrane noise, the
  silence probes, the fast decay in the thalamus (Fig. 9), and the STRF and LN model performance
  on the Wehr cells (Fig. 4).
license: Apache-2.0
python: "3.13"
notebooks:
- path: reproduce_asari_2009.ipynb
  title: Reproducing Asari and Zador (2009) from CRCNS ac-1
  runtime_minutes: 4
- path: strf_asari_2009.ipynb
  title: STRF and LN model performance on Wehr's recordings in CRCNS ac-1
  runtime_minutes: 22
[... 18 more lines not kept]
```

**Agent**

Writing the entry README before the full run, so the run's stamp covers the final entry files.

**Agent calls Write**

```json
{
 "file_path": "entries/asari-2009/README.md",
 "content": "# Asari and Zador (2009) from CRCNS ac-1\n\nTests the findings of [Asari and Zador (2009)](https://doi.org/10.1152/jn.00577.2009) that can be\ntested on [CRCNS ac-1](https://doi.org/10.6080/K0KW5CXR), which holds the whole-cell current-clamp\nrecordings of rat A1 neurons to sequences of natural and synthetic sounds, the cell-attached\nrecordings of MGB units, and the recordings of Wehr reanalysed for the encoding models. The\nvoltage-clamp recordings of Figures 5 and 6 are not in it.\n\n| Claim | Outcome |\n|---|---|\n| Cell and probe counts (305 natural sound probes in 39 cells, 93 MGB probes in 14 cells) | Partially reproduced |\n| Low firing rates in A1, high evoked rates in MGB | Partially reproduced |\n| Trial-to-trial reliability, 0.31 over the population | Reproduced |\n| Example neuron with context effects for about 4 s, absent from 2 to 4 s | Reproduced |\n| 204 of 305 probes (66.9%) significant, a quarter of events after 1 s | Reproduced |\n| Proportion significant decays as two exponentials (0.20 and 0.90 s) | Partially reproduced |\n| Normalized context-dependent power decays with a constant of 1.04 s | Partially reproduced |\n| Noise and spontaneous autocorrelations decay within about 100 ms | Reproduced |\n| No model without context captures more than half the predictable power at 100 ms | Partially reproduced |\n| STRF and LN models stay below about 20% and do not improve with longer windows | Partially reproduced |\n| Context dependence of excitatory and inhibitory conductances (Figures 5 and 6) | Blocked: data missing |\n| Effects of amplitude, frequency, AM, FM and higher-order properties (Figure 8, five claims) | Blocked: metadata insufficient |\n| Example of frequency context (Figure 7) | Blocked: data missing |\n| Fast decay of context dependence in MGB (about 80 ms) | Reproduced |\n| Example MGB unit with an effect in the first 100-ms bin only | Reproduced |\n| Significant effects soon after the onset of the silences | Reproduced |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe data set includes the authors' MATLAB analysis code (`asari/Tools/CxtDep.m`), which settles how\nprobes, contexts and the silence periods are formed; the helper ports it. The attempt record, with\nthe reasons and the differences from the paper's method, is\n[`attempts/asari-2009-02.yaml`](../../attempts/asari-2009-02.yaml).\n\n- `reproduce_asari_2009.ipynb`: all claims except the encoding models. It takes about four\n  minutes, most of it streaming the files.\n- `strf_asari_2009.ipynb`: the STRF and LN models on the Wehr cells. It takes about 22 minutes.\n- `ctxdep.py`: loading the files, probe construction, the significance and fractional power\n  measures, spike extraction and curve fits. Other notebooks on this data set can import it.\n- `strf.py`: spectrograms, lagged designs, ridge regression with cross-validation, the static\n  nonlinearity and the performance measure of the paper.\n"
}
```

```
File created successfully at: entries/asari-2009/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  date -u; uv run python tools/entry.py all entries/asari-2009 2>&1 | tail -8; date -u
```

```
Sun Nov 15 12:39:15 UTC 2026
Installed kernelspec registry-asari-2009 in executed/asari-2009/.venv/share/jupyter/kernels/registry-asari-2009
0 error(s)
pass  reproduce_asari_2009.ipynb  (185 s)
pass  strf_asari_2009.ipynb  (1277 s)
Sun Nov 15 13:03:46 UTC 2026
```

**Agent**

Both notebooks pass (3 and 21 minutes). Checking that the executed outputs match the written conclusions.

**Agent calls Bash**

```bash
cd  . $TMPDIR/dev/bin/activate; python - <<'EOF'
import nbformat, difflib
def outs(p):
    nb=nbformat.read(p,as_version=4); r=[]
    for c in nb.cells:
        if c.cell_type=='code':
            r.append(''.join(o.get('text','') for o in c.outputs if o.output_type=='stream'))
    return r
a=outs('executed/asari-2009/reproduce_asari_2009.ipynb'); b=outs('/tmp/claude-1001/exec.ipynb')
print(len(a),len(b))
for i,(x,y) in enumerate(zip(a,b)):
    if x!=y:
        d=[l for l in difflib.unified_diff(y.splitlines(),x.splitlines(),lineterm='',n=0) if not l.startswith(('---','+++','@@'))]
        print('== cell',i); print('\n'.join(d[:40]))
a=outs('executed/asari-2009/strf_asari_2009.ipynb'); b=outs('/tmp/claude-1001/strf_exec.ipynb')
for i,(x,y) in enumerate(zip(a,b)):
    if x!=y:
        d=[l for l in difflib.unified_diff(y.splitlines(),x.splitlines(),lineterm='',n=0) if not l.startswith(('---','+++','@@'))]
        print('== strf cell',i); print('\n'.join(d[:20]))
EOF
```

```
26 26
== cell 2
-loaded in 318 s; peak memory 6.04 GB
+loaded in 172 s; peak memory 6.05 GB
== cell 3
-animal age (days) as stored: [('24', 69), ('21', 54), ('25', 52), ('23', 51), ('22', 41), ('26', 38), ('27', 18), ('20', 10), ('29', 9), ('28', 4), ('[]', 2)]
+animal age (days) as stored, cells per age: {'20': 5, '21': 24, '22': 19, '23': 25, '24': 33, '25': 24, '26': 15, '27': 7, '28': 2, '29': 4, '[]': 1}
+cells outside the paper's 20 to 28 days or without an age: [['synthetic', '20061229-ha2-004', '[]'], ['mgb', '20071012-ha1-001', '29'], ['mgb', '20071012-ha1-002', '29'], ['mgb', '20071012-ha1-003', '29'], ['mgb', '20071012-ha1-004', '29']]
== cell 5
-files sharing length, extremes and median: 4
-                                                  path       dur       vmin       vmax
-69   Results/20060314-ha1-001/20060314-ha1-001-001.mat  106.9002 -68.482490 -43.091478
-125  Results/20060314-ha1-001/20060314-ha1-001-001.mat  106.9002 -68.482490 -43.091478
-71   Results/20060320-ha3-003/20060320-ha3-003-001.mat  107.8730 -72.098878  18.432898
-142  Results/20060320-ha3-003/20060320-ha3-003-001.mat  107.8730 -72.098878  18.432898
+files listed in more than one experiment group of Summary.mat:
+path
+Results/20060314-ha1-001/20060314-ha1-001-001.mat    [natural, synthetic]
+Results/20060320-ha3-003/20060320-ha3-003-001.mat    [natural, synthetic]
+cells listed in more than one group: {'20060314-ha1-001': ['natural', 'synthetic'], '20060320-ha3-003': ['natural', 'synthetic']}
[... 39 more lines not kept]
```

**Agent**

All numbers in the clean run are identical to the development run. Now the attempt record; checking the schema's required fields first.

**Agent calls Bash**

```bash
cd  uv run python - <<'EOF'
import json
s=json.load(open('schemas/attempt.schema.json'))
print('required', s.get('required')); print('props', list(s['properties']))
o=s['properties']['outcomes']['items']; print('outcome req', o.get('required'), list(o['properties']))
print(json.dumps(s['properties']['datasets']['items']['properties'],indent=0)[:1500])
print(json.dumps(s['properties']['provenance']['properties']['runner'])[:600])
f=s['properties']['findings']['items']; print(list(f['properties']), f.get('allOf'))
EOF
```

```
required ['schema_version', 'id', 'datasets', 'paper', 'date', 'provenance', 'outcomes']
props ['schema_version', 'id', 'datasets', 'missing_datasets', 'paper', 'date', 'entry', 'deprecated', 'provenance', 'outcomes', 'verifications', 'findings', 'reconciliation', 'inputs']
outcome req ['claim', 'outcome'] ['claim', 'outcome', 'blocked_by', 'notes', 'notebook', 'output', 'measured', 'deviations', 'assumed', 'proposed']
{
"archive": {
"description": "The archive that holds the dataset, in lower case: dandi, ebrains, openneuro, dryad, zenodo, figshare and so on.",
"type": "string",
"pattern": "^[a-z][a-z0-9-]*$"
},
"id": {
"description": "The dataset's identifier in that archive, e.g. 000003 on DANDI.",
"type": "string",
"minLength": 1
},
"version": {
"description": "The version the attempt read, e.g. 0.220127.0436, or draft.",
"type": "string",
"minLength": 1
},
"modified": {
[... 19 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "attempts/asari-2009-02.yaml",
 "content": "schema_version: 3\nid: asari-2009-02\ndatasets:\n- archive: crcns\n  id: ac-1\n  version: unversioned\n  doi: 10.6080/K0KW5CXR\n  relation: primary\npaper: doi:10.1152/jn.00577.2009\ndate: 2026-11-15\nentry: asari-2009\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-15\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/43709631660\ninputs: []\noutcomes:\n- claim: methods-recording-counts\n  outcome: partially_reproduced\n  notebook: reproduce_asari_2009.ipynb\n  output: claim:methods-recording-counts\n  notes: The natural sound sample is exact, 305 probes in 39 cells, under both readings of silence,\n    and so is the MGB sample, 93 probes in 14 cells with at least 10 trials. Of the 145 distinct A1\n    whole-cell cells in the data set, 132 have at least one probe that meets the rule, against 123;\n    restricted to the five ensembles the paper names, 118 distinct cells. By ensemble, natural\n    sounds 39 (paper 39), TORC 14 (14), MCN 26 (27), DMR 15 (6) and MHT 26 (39); the DMR and MHT\n    counts depend on how designs with a natural sound probe after DMR or MHT variants are assigned,\n    which the files do not say. Two cells are listed in both the natural and the synthetic group of\n    Summary.mat, which agrees with the paper's ensemble counts summing to 125 for 123 cells. The\n    voltage-clamp counts (29 probes in 14 cells) cannot be tested, as no voltage-clamp recording is\n    in the data set. The natural sound probe count (305) and the MGB counts (93, 14) are within their\n    zero tolerance; the A1 total (132) is not.\n  deviations:\n  - The voltage-clamp part of the claim is not tested (no data).\n  - Ensembles are assigned from the stimulus descriptions in each file (TORC, DMR, Modulated\n    Harmonic Tone, pink noise); the paper gives no file-level assignment.\n- claim: a1-mgb-firing-rates\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_asari_2009.ipynb\n  output: claim:a1-mgb-firing-rates\n  measured:\n  - 0.363\n  - 0.533\n  - 0.618\n  - 5.072\n  notes: No reading puts all four means within tolerance. Measured values are the first reading\n    (all silences, all stimulus periods, all recordings, 15-mV A1 detector). A1 over 145 cells, 15-mV\n    detector, sequence recordings only, gives 0.488 Hz spontaneous and 0.541 Hz evoked (SD 0.608\n    and 0.677), both within tolerance; over all recordings the spontaneous mean falls to 0.363 Hz\n    (evoked 0.533). The 10-mV and 20-mV detectors give evoked means of 0.586 and 0.447 Hz over all\n    recordings. MGB over 14 cells and all recordings gives 0.618 Hz spontaneous over all silences,\n    0.817 Hz in the second before each stimulus, and 5.07 Hz evoked (SD 11.46); the tuning-curve\n    recordings alone give 0.868 and 11.66 Hz, and the sequence recordings alone 0.551 and 4.99 Hz.\n    The A1 means are below 1 Hz and the MGB evoked mean is above 5 Hz under the all-recordings\n    reading, the claim's rule for partial. The MGB evoked rate is dominated by a few cells (one at\n    43.1 Hz, most below 2 Hz on the sequence recordings). The question for the paper's authors is\n    under findings.\n  deviations:\n  - A1 spikes were detected by hand in the paper (GetSpikes.m, manual mode). Here a spike is a peak\n    at least 10, 15 or 20 mV above the 10-ms median-filtered trace, an assumption; 15 mV is the main\n    reading. MGB spikes use the automatic detector of GetSpikes.m (high-pass FIR, two thirds of the\n    largest deflection), as ViewResp.m does for cell-attached data.\n  - 145 A1 cells and 14 MGB cells are in the data set, against 194 and 16 in the paper.\n  - The 0.5 s after each test current pulse is left out of the silences.\n- claim: fig2-example-reliability\n  outcome: reproduced\n  notebook: reproduce_asari_2009.ipynb\n  output: claim:fig2-example-reliability\n  measured: 0.310\n  notes: Mean pairwise correlation between the trials of one context over the probe period, 0.310\n    +/- 0.098 over 39 cells (range 0.18 to 0.60) and 0.319 +/- 0.129 over 305 probes; the\n    leave-one-out reading gives 0.436 +/- 0.104 over cells. Of 10 recordings with seven natural\n    fragments and at least six trials, one (20051222-ha1-001) has a cell mean of 0.603, within 0.61\n    +/- 0.07, and 15 probe-context values between 0.66 and 0.82 (0.74 +/- 0.08), so the example\n    values are consistent with that cell; the shown probe cannot be identified, and measured gives\n    the population value only.\n- claim: fig2-example-long-context\n  outcome: reproduced\n  notebook: reproduce_asari_2009.ipynb\n  output: claim:fig2-example-long-context\n  notes: 40 probes in 10 recordings have the example's design (seven long natural fragments, three\n    contexts including silence, at least six trials in one context). Two of them are significant\n    before 2 s, not from 2 to 4 s, and again after 4 s (20060105-ha1-001 probe 4, last significant\n    time 4.06 s; 20060225-ha1-001 probe 5, 5.04 s). Over all 305 probes, 18 have a significant\n    period later than 4 s and 8 show the 2 to 4 s gap.\n  deviations:\n  - The significance measure runs at 1 kHz with runs of at least 5 ms, where the paper used 0.1 ms\n    and 50 points; on the probes of one recording the two agree at 0.997 to 1.000 of time points.\n- claim: fig3a-proportion-significant\n  outcome: reproduced\n  notebook: reproduce_asari_2009.ipynb\n  output: claim:fig3a-proportion-significant\n  measured:\n  - 187\n  - 0.613\n  - 0.251\n  notes: With silence counted as a context and the proportion over all 305 probes, 187 probes\n    (61.3%) are significant and the late fraction is 0.251 (peak of the cumulative curve at 4.78 s,\n    paper 4.72 s), all within tolerance. Over the running probes the late fraction is 0.267, outside.\n    Without silence, 169 probes (55.4%) and a late fraction of 0.177, outside. 36 of 39 cells have a\n    significant probe. The mean noise floor is 0.0026.\n  deviations:\n  - Silence is counted as a context in the main reading, as CxtDep.m does (the last 4 s of the\n    interval before each sequence) and as Figure 2B shows; the reading without it is shown.\n  - 1-kHz resolution, as for fig2-example-long-context.\n- claim: fig3a-significance-decay\n  outcome: partially_reproduced\n  notebook: reproduce_asari_2009.ipynb\n  output: claim:fig3a-significance-decay\n  measured:\n  - 0.151\n  - 0.253\n  - 0.079\n  - 0.974\n  - 0.0026\n  notes: Two exponentials are selected under every reading with silence counted. Over all probes and\n    0 to 4.72 s the sizes are 0.151 and 0.079, the constants 0.253 and 0.974 s, and the fixed\n    constant 0.0026; the slow constant and the noise floor are within tolerance, the fast size, fast\n    constant and slow size are not. Over 0 to 6 s the values are 0.150, 0.251 s, 0.080 and 0.975 s.\n    Over the running probes the fast size is 0.162 (within tolerance) and the slow constant 1.04 to\n    1.09 s. Without silence one exponential is selected (0.166, 0.316 s). The slow constant lies\n    between 0.5 and 2 s in every two-exponential fit.\n  deviations:\n  - Fits use least squares from a grid of start values (standard choice), with taus bounded to 1\n    ms to 100 s; the paper used lsqcurvefit without stating starts or bounds.\n- claim: fig3b-fractional-power-decay\n  outcome: partially_reproduced\n  notebook: reproduce_asari_2009.ipynb\n  output: claim:fig3b-fractional-power-decay\n  measured:\n  - 0.470\n  - 1.732\n  notes: Q(t) falls from 0.76 over the first 50 ms to 0.19 at 1 s and 0.13 at 3 s. With silence\n    counted the fitted size is 0.470 (0 to 4 s) or 0.466 (0 to 6 s), within tolerance, and the\n    constant 1.73 or 1.78 s, outside 0.936 to 1.144 s. Without silence the constant is 1.27 to\n    1.28 s with sizes 0.452 to 0.454. A fit up to the shortest probe (1.98 s) gives 1.12 s with a\n    size of 0.554 (silence counted), or 0.73 s with 0.580 (without). No reading puts both values\n    within tolerance; every fit to 4 or 6 s gives a decay constant above one second, so the\n    long-lasting decay is reproduced and its value is longer than the paper's.\n  deviations:\n  - The population average at time t is over the probes still running at t; the paper does not\n    say how probes of different lengths are combined. With zeros for ended probes the ratio is the\n    same except through the smoothing.\n  - Each trial is centred over the probe period before the power estimates, as FracPow in CxtDep.m\n    does.\n- claim: timescale-longer-than-membrane\n  outcome: reproduced\n  notebook: reproduce_asari_2009.ipynb\n  output: claim:timescale-longer-than-membrane\n  notes: The trial-noise autocorrelation over 305 probes falls below 1/e at 72 ms and below 0.1 at\n    115 ms. The autocorrelation of the silences between sequences falls below 1/e at 78 ms (44\n    recordings), or 76 ms without the first 1 s of each silence (46 recordings), and below 0.1 at\n    123 and 119 ms. All 1/e lags are under 150 ms and under a third of 1.04 s.\n  deviations:\n  - Each silence is cut at the first test current pulse inside it.\n- claim: fig4-predictability-upper-bound\n  outcome: partially_reproduced\n  notebook: reproduce_asari_2009.ipynb\n  output: claim:fig4-predictability-upper-bound\n  measured:\n  - 0.430\n  - 2.317\n  notes: Measured values are the main reading (smoothed denominator, silence counted, 0 to 4 s). The\n    bound near onset matches under other readings, 1 + alpha1 is 0.498 with the unsmoothed\n    denominator and 0.490 with the smoothed one without silence (0 to 6 s), and the mean of Eq. 43\n    over the first 100 ms is 0.492 (smoothed, silence counted). The approach to one is slower than\n    the paper's, the time constant being 1.45 to 2.81 s in every fit to 4 or 6 s against 1.04 s.\n    The closest constant, 0.928 s, comes from a fit to the shortest probe (1.98 s, unsmoothed,\n    without silence), where the bound is 0.439. Eq. 43 is 0.54 at 1 s and 0.76 at 3 s (main\n    reading). No reading puts both values within tolerance.\n  deviations:\n  - As for fig3b-fractional-power-decay, the average at time t is over the running probes.\n- claim: fig4-strf-performance-low\n  outcome: partially_reproduced\n  assumed: true\n  notebook: strf_asari_2009.ipynb\n  output: claim:fig4-strf-performance-low\n  measured: 0.152\n  notes: Over 16 Wehr cells (10-ms Hann window, contiguous folds), the mean validation performance\n    is 0.130 to 0.152 for the STRF and 0.084 to 0.121 for the LN model across the nine windows,\n    below 0.22 at every window; the training estimates are 0.205 to 0.249 and 0.234 to 0.289. The\n    one-sided Wilcoxon test of 4052 against 180 ms finds an improvement for both models, median\n    +0.016 for the STRF (11 of 16 cells improve, p = 0.0038) and +0.023 for the LN model (14 of 16,\n    p = 0.017); with a 20-ms window p = 0.0038 and 0.022, with folds by stimulus p = 0.033 and\n    0.022. The Friedman test over the nine windows gives p = 0.057 (STRF) and 0.0001 (LN). The LN\n    model is worse than the STRF on validation data (mean -0.038) and better on training data\n    (+0.040). Low performance holds; the absence of an improvement and the small LN gain do not. A\n    model fitted after shifting the response by half the stimulus gives -0.002, against 0.178 with\n    the true alignment. The ridge value was chosen at the top of the grid in 36 of 208 fits.\n  deviations:\n  - The paper's 20 cells are not listed. The data set holds 25 Wehr cells; the 16 with at least two\n    natural sound stimuli of at least two trials, which Eq. 52 needs, are used.\n  - The test of no improvement is the claims file's assumption (paired one-sided Wilcoxon,\n    validation, 4052 against 180 ms).\n  - Response sampled in 4-ms bins of the 10-ms median-filtered membrane potential; spectrogram\n    bands from 0.40 to 20.3 kHz at 3 per octave (17 bands); the paper gives 0.40 to 22 kHz.\n  - The static nonlinearity is a lowess fit on the training set (5% span, 5 robust iterations)\n    applied to the validation set by interpolation; how the paper applied it to new data is not\n    stated.\n- claim: fig5-example-conductances\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Every file of the data set is a current-clamp or cell-attached recording in mV; no\n    voltage-clamp recording (the paper's 42 cells) is deposited, and no other public source is\n    named by the paper.\n- claim: fig6-conductance-decay\n  outcome: blocked\n  blocked_by: data_missing\n  notes: As for fig5-example-conductances, the 29 voltage-clamp probes in 14 cells are not in the\n    data set.\n- claim: fig8a-proportion-by-property\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: The 105 synthetic recordings are in the data set, but the files do not say which\n    conditioning stimuli form the paper's amplitude, frequency, AM, FM and higher-order sets of\n    Table 1. Only the 6 recordings of a natural probe after MHT variants name the groups in their\n    notes. Most MHT recordings are 4 by 4 designs of AM and FM ranges with a natural probe, whose\n    grouping into sets is not stated, and the MHT probes of Table 1 (71 AM and 57 FM probes) cannot\n    be found among the designs, where MHT fragments follow only a natural sound or silence. Any\n    assignment would be the author's, so the counts are not tested.\n- claim: fig8b-decay-by-property\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: Depends on the property sets of fig8a-proportion-by-property.\n- claim: fig8a-significance-fits\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: Depends on the property sets of fig8a-proportion-by-property.\n- claim: fig8c-relative-effects\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: Depends on fig8b-decay-by-property.\n- claim: fig8-natural-synthetic-probes-alike\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: Depends on the property sets of fig8a-proportion-by-property.\n- claim: fig9-mgb-fast-decay\n  outcome: reproduced\n  notebook: reproduce_asari_2009.ipynb\n  output: claim:fig9-mgb-fast-decay\n  measured:\n  - 5.239\n  - 0.058\n  - 1.206\n  notes: The mean SD of the PSTHs over 93 probes in 14 cells is 6.45 spikes/s in the first bin and\n    2.04 in the second. With silence counted and the running probes, tau1 is 0.058 s with bins at\n    their start or centre, and the mean after 0.5 s is 0.99 times the fitted constant; over all\n    probes with bins at their start, tau1 is 0.080 s. The sizes are smaller than the paper's,\n    alpha1 5.2 to 12.4 spikes/s against 15.0 and kappa 0.81 to 1.21 against 2.0. Without silence\n    the first bin is 2.50 spikes/s, tau1 is 0.075 s over the running probes, and the fit over all\n    probes does not converge to a decay (tau1 at its 100 s bound). tau1 is never above 0.3 s.\n  deviations:\n  - Spikes from the automatic detector of GetSpikes.m, as for a1-mgb-firing-rates.\n- claim: fig9-example-first-bin\n  outcome: reproduced\n  notebook: reproduce_asari_2009.ipynb\n  output: claim:fig9-example-first-bin\n  notes: Of 12 probes with the Figure 9A design (seven long natural fragments, three contexts with\n    silence, 10 to 17 trials), 4, all in 20071010-ha2-003, have a first-bin SD at least twice that of\n    every later bin (ratios 2.05 to 2.81). Over all 93 probes the pattern holds in 35 (0.376); with\n    a factor of 1.5 in 51 and of 3 in 18.\n- claim: fig7-example-frequency-context\n  outcome: blocked\n  blocked_by: data_missing\n  notes: None of the 105 synthetic recordings has contexts in the three bands of Figure 7 (0.625-2.5,\n    2.5-10 and 10-40 kHz), and only one has any of them. The DMR frequency variants that precede a\n    natural sound probe (5 recordings) span 0.25-1 to 8-32 kHz in two-octave bands, and the 4-band\n    DMR recordings have no natural probe. The recording of Figure 7 is not in the data set, or not\n    with the bands the legend gives.\n- claim: figs1-silence-probe\n  outcome: reproduced\n  notebook: reproduce_asari_2009.ipynb\n  output: claim:figs1-silence-probe\n  notes: Of 44 silence probes in 38 cells, 26 have a significant period, and 22 in 19 cells have one\n    starting within 0.5 s of the silence onset. The stimulus-related power (Eq. 17) averaged over\n    the silence probes falls from 5.61 mV^2 at onset to 1.34 at 0.5 s and first below 10% of its\n    onset value at 0.54 s; the context-dependent power (Eq. 19) at 0.46 s. The noise floor of the\n    silence probes is 0.0057, about twice that of the fragment probes (0.0026).\n  deviations:\n  - The silence probe is the first 2.5 s after each sequence and its contexts the last fragment of\n    each sequence, as in CxtDep.m; the supplement was not read.\nfindings:\n- kind: data_missing\n  about: data\n  statement: The data set holds no voltage-clamp recording. The paper recorded 42 cells in voltage\n    clamp and analysed 14 (29 probes, Figures 5 and 6); every file in ac-1 is a current-clamp or\n    cell-attached recording in mV.\n- kind: data_missing\n  about: data\n  statement: The data set holds 145 of the 194 A1 current-clamp cells and 14 of the 16 MGB cells the\n    paper recorded. The cells of the natural sound analysis (305 probes in 39 cells) and of the MGB\n    analysis (93 probes in 14 cells) are all there.\n- kind: metadata_insufficient\n  about: data\n  statement: For the synthetic recordings, the files do not say which conditioning stimuli form the\n    amplitude, frequency, AM, FM and higher-order sets of the paper's Table 1 and Figure 8. Only 6\n    of 105 recordings name the sets in their notes; the others give stimulus parameters (for\n    example AM and FM ranges of modulated harmonic tones in 4 by 4 designs) without the grouping,\n    and the MHT probes of Table 1 cannot be found among the designs.\n- kind: data_missing\n  about: data\n  statement: No recording has the design of Figure 7 (a natural sound probe after DMR contexts in\n    0.625-2.5, 2.5-10 and 10-40 kHz). The DMR frequency variants in the data set use the bands 0.25-1\n    to 8-32 kHz.\n- kind: other\n  about: data\n  statement: Summary.mat lists two cells (20060314-ha1-001 and 20060320-ha3-003), with the same\n    tuning-curve file, in both the natural sound and the synthetic group, so counting cells per\n    group gives 147 A1 cells where the data set holds 145. This agrees with the paper, whose\n    ensemble counts sum to 125 for 123 cells, but it is not documented.\n- kind: other\n  about: data\n  statement: Four MGB cells (20071012-ha1-001 to -004) come from an animal whose age is stored as 29\n    days, outside the 20 to 28 days of the paper's Methods, and one cell (20061229-ha2-004) has no\n    age.\n- kind: other\n  about: data\n  statement: In some recordings the sequence numbers in the trigger descriptions differ from those\n    in the notes (for example \"Sequence 2, 4, 6, 8\" in the triggers of 20051107-ha1-001-003 against\n    \"Seq.1 to 4\" in its notes); the fragment lists agree, so the analysis uses the lists.\n- kind: other\n  about: data\n  statement: The data set includes the authors' MATLAB analysis code (asari/Tools/CxtDep.m and\n    others), which the paper does not mention. It fixes how probes, contexts, the silence context\n    (last 4 s of the interval) and the silence probe (first 2.5 s) are formed, and it reproduces the\n    paper's sample sizes exactly (305 natural sound probes, 93 MGB probes).\n- kind: methods_unavailable\n  about: paper\n  statement: Question for the authors. How were A1 spikes detected for the firing rates (the code\n    says by hand), and which periods count as spontaneous and evoked, and which recordings? With an\n    automatic detector the A1 means match (0.49 and 0.54 Hz) but the MGB evoked rate is 5.0 Hz over\n    the sequence recordings against 11.4 Hz, and 11.7 Hz over the tuning-curve recordings.\n- kind: methods_unavailable\n  about: paper\n  statement: Question for the authors. Over what time range were Eq. 44 fitted to the population\n    curves, and how were probes of different lengths (2 to 6 s) combined at times after the shorter\n    ones end? The time constants of Q(t) (Fig. 3B) and of Eq. 43 (Fig. 4) depend on it, 0.73 to\n    1.78 s and 0.93 to 2.98 s here against 1.04 s, and only fits restricted to the first 2 s come\n    near 1.04 s.\n- kind: methods_unavailable\n  about: paper\n  statement: Question for the authors. Which 20 of the 25 Wehr cells in the data set were used for\n    the encoding models, and how was the static nonlinearity applied to validation data? Only 16\n    cells have the repeated trials that Eq. 52 needs.\n- kind: paper_inconsistency\n  about: paper\n  statement: The Results give 73 of 110 probes for frequency changes as 64.6%; 73/110 is 66.4%. 64.6%\n    is the value given for AM (62/96).\n"
}
```

```
File created successfully at: attempts/asari-2009-02.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
p='attempts/asari-2009-02.yaml'; s=open(p).read()
old="probes does not converge to a decay (tau1 at its 100 s bound). tau1 is never above 0.3 s."
new="probes does not converge to a decay (tau1 at its 100 s bound); apart from that fit, tau1 is at\n    most 0.080 s."
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
EOF
grep -n ": " attempts/asari-2009-02.yaml | grep -v "^[0-9]*: *[-a-z_]*: \|^[0-9]*: *- [a-z_]*: " | head; uv run python tools/entry.py check entries/asari-2009 2>&1 | tail -5; date -u
```

```
0 error(s)
Sun Nov 15 13:05:42 UTC 2026
```

**Agent**

Checks pass with 0 errors. Running the handover (step 6).

**Agent calls Bash**

```bash
cd  uv run python tools/entry.py handover entries/asari-2009 2>&1 | tail -8; ls -R executed/asari-2009/handover | head; git status --short 2>/dev/null | head
```

```
wrote executed/asari-2009/handover
executed/asari-2009/handover:
asari-2009.yaml
ctxdep.py
reproduce_asari_2009.ipynb
strf.py
strf_asari_2009.ipynb
```

**Agent calls Bash**

```bash
cd  grep -c "Result:" executed/asari-2009/handover/*.ipynb; ls -a entries/asari-2009; rm -rf entries/asari-2009/__pycache__; ls entries/asari-2009; date -u
```

```
executed/asari-2009/handover/reproduce_asari_2009.ipynb:0
executed/asari-2009/handover/strf_asari_2009.ipynb:0
.
..
.claude
README.md
__pycache__
ctxdep.py
entry.yaml
reproduce_asari_2009.ipynb
requirements.in
requirements.lock.txt
strf.py
strf_asari_2009.ipynb
README.md
ctxdep.py
entry.yaml
reproduce_asari_2009.ipynb
requirements.in
requirements.lock.txt
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/asari-2009; find .claude -type f | head; ls -la .claude
```

```
total 12
drwxr-xr-x 3 runner runner 4096 Nov 15 11:49 .
drwxr-xr-x 3 runner runner 4096 Nov 15 13:06 ..
drwx------ 2 runner runner 4096 Nov 15 11:49 .cc-writes
```

**Agent**

The entry is written, locked, checked (0 errors) and run from a clean environment. Both notebooks pass: `reproduce_asari_2009.ipynb` in 3 min and `strf_asari_2009.ipynb` in 21 min. The record is `attempts/asari-2009-02.yaml` and the handover is built. I did not come across any earlier attempt's results.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| methods-recording-counts | partially reproduced: 305 natural probes in 39 cells and 93 MGB probes in 14 cells match exactly; 132 A1 cells meet the rule against 123; voltage-clamp counts can't be tested |
| a1-mgb-firing-rates | partially reproduced, rests on an assumption (A1 spike detector) |
| fig2-example-reliability | reproduced (0.310 ± 0.098) |
| fig2-example-long-context | reproduced (2 matching probes) |
| fig3a-proportion-significant | reproduced (187 of 305, late fraction 0.251) |
| fig3a-significance-decay | partially reproduced |
| fig3b-fractional-power-decay | partially reproduced (size 0.47 matches; time constant 1.3–1.8 s against 1.04 s) |
| timescale-longer-than-membrane | reproduced (72 and 78 ms) |
| fig4-predictability-upper-bound | partially reproduced (bound 0.49–0.50 matches; time constant longer) |
| fig4-strf-performance-low | partially reproduced, rests on an assumption: performance is low, but the Wilcoxon test finds a small improvement with longer windows |
| fig5, fig6 | blocked: data_missing |
| fig8a, fig8b, fig8a-significance-fits, fig8c, fig8-natural-synthetic | blocked: metadata_insufficient |
| fig7-example-frequency-context | blocked: data_missing |
| fig9-mgb-fast-decay | reproduced (tau 0.058–0.080 s) |
| fig9-example-first-bin | reproduced |
| figs1-silence-probe | reproduced |

## 2. Dataset, assumptions, questions

**What was found about the dataset:**
- There are no voltage-clamp recordings at all.
- It holds 145 of the 194 A1 current-clamp cells and 14 of the 16 MGB cells. Every cell used in the natural-sound and MGB analyses is there.
- For the synthetic recordings, only 6 of 105 say which conditioning stimuli form the paper's five property groups (amplitude, frequency, AM, FM, higher-order). That is why the Figure 8 claims are blocked.
- No recording has the Figure 7 design.
- Summary.mat lists two cells in both the natural and the synthetic group.
- Four MGB cells come from an animal stored as 29 days old, outside the paper's 20–28 days; one cell has no age.
- Sequence numbers in some trigger descriptions don't match the numbering in the file notes; the fragment lists agree.
- The data set contains the authors' own analysis code (`CxtDep.m`). The paper doesn't mention it. I ported it, and it reproduces the paper's sample sizes exactly.

**Assumptions:**
- A1 spike detector: a peak at least 15 mV above the median-filtered trace, with 10 and 20 mV also shown. The paper detected A1 spikes by hand.
- STRF: the 16 of 25 Wehr cells that have the repeated trials Eq. 52 needs, plus the claims file's Wilcoxon test.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- How A1 spikes were detected, and which periods and recordings count as spontaneous and evoked.
- Over what time range the Eq. 44 fits were made, and how probes of different lengths were combined.
- Which 20 Wehr cells were used.

I also recorded a `paper_inconsistency`: the paper gives 73/110 as 64.6%; it is 66.4%.

I asked no questions of a reader.

## 3. Protocol gaps
1. The analysis code ships inside the dataset, and the paper doesn't link it. The protocol only covers "code the paper links". I treated it as the paper's code and cited it.
2. `measured` cannot hold a missing value. The counts claim has two untestable expected values (the voltage-clamp counts), so I left `measured` out for that claim.
3. Several criteria define only "reproduced" (fig3b, fig4, STRF). I used the protocol's general definition of "partially reproduced" for the cases in between.
4. A "not testable when no cell matches" criterion has no matching `blocked_by` value. I used `data_missing` for fig7.
5. The duplicate check compares recordings by length and trace statistics. Comparing full traces would have meant streaming everything twice.

## 4. Runtime and failures
The run took about 1.5 h of the 5 h. The clean-environment runs take 3 min and 21 min, with peak memory of 6.0 GB and 3.8 GB. Nothing failed.

## End of run

83 turns, 84 minutes, $9.67 at API prices, result: success.
