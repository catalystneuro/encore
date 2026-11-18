# mcguire-2016 · author · run 43061505476

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; ls; ls docs entries claims attempts paper | head -50
```

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md"
}
```

```
Wed Nov 11 17:01:37 UTC 2026
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
[... 62 more lines not kept]
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
[... 646 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md | head -80; echo ----; cat docs/archives.md; echo ----; ls paper; cat claims/mcguire-2016.yaml; ls papers/datasets | grep -i mcg; cat papers/datasets/mcguire-2016.yaml; ls questions | head
```

```
<persisted-output>
Output too large (80.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/48cbaa43-b35d-452c-8bc0-0dfa6fe1c735/tool-results/bqft8v2zf.txt

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
cat docs/archives.md | sed -n '/CRCNS/,/^## [A-Z]/p' | head -120; ls paper; wc -c paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/mcguire-2016.yaml; cat papers/datasets/mcguire-2016.yaml; ls questions | grep mcg; cat paper/ssc-4.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/mcguire-2016.yaml"
}
```

```
1	# Claims for McGuire, Telian, Laboy-Juarez, Miyashita, Lee, Smith & Feldman (2016), PLoS Biology
2	# 14(8) e1002549, on CRCNS ssc-4.
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
4	# protocol pilot-14 as stated in docs/protocol.md. The writer did not look at the dataset's data or
5	# files; only its title and the summary of its data descriptor were read, to know which experiments
6	# it holds.
7	#
8	# Text read: the version of record (open access), full text as served by Europe PMC (PMC5004814,
9	# JATS XML flattened), with the Methods and the legends of the supporting information (S1 to S7
10	# Figs, S1 Table, S1 and S2 Data). The contents of S1 Table (baseline firing rates by layer and unit
11	# type, DOCX) and of S1 and S2 Data (XLSX) are not in the text; no claim rests on numbers found only
12	# there. No PDF was supplied, so no figure could be read. Table 1 is garbled in the text: its
13	# sequence rows read "FFF 34 120 65.7 Right", "FMS 34 132 54.4 Right", "SMF 34 132 54.7 Left", "SSS
14	# 34 148 44.6 Left" under headers that do not fit. They are read here as interpulse interval (ms),
15	# duration (ms, matching the 120 to 148 ms of the Results), mean speed (mm/s, ordered as the
16	# Results say) and rewarded port.
17	#
18	# Code read: none. The paper links no code. The Methods say the regression was run in Matlab and
19	# the decoders in Python with scikit-learn; neither script is published.
20	#
[... 944 more lines not kept]
```

**Agent**

Claims file has about 35 claims. Next I'm reading the data descriptor, the paper, and the reference entry format.

**Agent calls Bash**

```bash
cat paper/ssc-4.data-description.txt; ls entries/fouke-2025; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in; ls entries/fouke-2025/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=ssc-4/" | python -c "import sys,re; t=sys.stdin.read(); [print(m) for m in re.findall(r'<Key>(.*?)</Key><LastModified>(.*?)</LastModified><ETag>(.*?)</ETag><Size>(.*?)</Size>',t)]"; curl -s https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-4/live/checksums.md5 | head
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=ssc-4/" | head -c 3000; echo; curl -s https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-4/live/filelist.txt
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
ls entries | head -100 | tr '\n' ' '; echo; grep -l crcns entries/*/entry.yaml; python --version; uv --version; which python; python -c "import scipy, fsspec, numpy; print(scipy.__version__)"
```

```
Exit code 1
amjad-2025 armstrong-2026 ashworth-2025 athalye-2023 azcorra-2023 bech-2026 bellvila-2026 bennett-2024 berg-2020 boran-2022 bouabid-2026 bouchard-2013 brezovec-2022 bruno-2017 buccino-2020 buccino-2024 burman-2023 carcea-2021 chandravadia-2020 chang-2023 chantranupong-2023 chartrand-2023 chaunsali-2025 chen-2017 chen-2026 choi-2025 chowdhury-2020 churchland-2010-000128 churchland-2010-000138 churchland-2010-000139 churchland-2010-000140 churchland-2012 claar-2023 clark-2024 cody-2024 daume-2024 daume-2024-phase davatolhagh-2025 dehaqani-2024 dembrow-2024 deweese-2004 dias-2025 didion-gency-2024 dimakopoulos-2022 doherty-2025 duszkiewicz-2024 economo-2018 even-chen-2019 eyherabide-2008 fan-2024 farrell-2020 fedele-2020 fouke-2025 fujimoto-2026-001773 fujimoto-2026-001785 fujisawa-2008-000067 fujisawa-2008-crcns-pfc-2 funamizu-2016 gao-2018 gao-2025-000637 gao-2025-000946 gao-2025-001199 gao-2026 geiller-2020 gerken-2025 ghaderi-2026 gillespie-2021 gillon-2023-000037 gillon-2023-000336 girardeau-2017-000061 girardeau-2017-crcns-hc-14 goncalves-2013 gonzalez-cabrera-2026 grosmark-2016-000044 gu-2011 gu-2026 guan-2022 guan-2022-finger guo-2017 hadjas-2025 hart-2023 hart-2024 heeringa-2024 henry-2022 hickman-2026 hires-2015 hristova-2025 hulsey-2024 huszar-2022 ibl-2021 ibl-2025 iram-2024 ishii-2025 ito-2009 ito-2015 jackson-2019 jadhav-2016 jeong-2022 johnson-2018 johnson-2019 
entries/bruno-2017/entry.yaml
entries/deweese-2004/entry.yaml
entries/eyherabide-2008/entry.yaml
entries/farrell-2020/entry.yaml
entries/fujisawa-2008-crcns-pfc-2/entry.yaml
entries/girardeau-2017-crcns-hc-14/entry.yaml
entries/goncalves-2013/entry.yaml
entries/gu-2011/entry.yaml
entries/henry-2022/entry.yaml
entries/jadhav-2016/entry.yaml
entries/johnson-2018/entry.yaml
entries/johnson-2019/entry.yaml
entries/kohus-2016/entry.yaml
entries/lee-2014/entry.yaml
entries/lefebvre-2008/entry.yaml
entries/lemessurier-2019/entry.yaml
entries/li-2015-crcns-alm-1/entry.yaml
entries/li-2016-crc
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
cat entries/bruno-2017/entry.yaml | sed -n '/related/,$p'; sed -n 1,80p tools/entry.py | head -80; cat pyproject.toml | head -40
```

```
related:
- id: crcns:apl-1/unversioned
  relation: uses_data
- id: doi:10.7554/elife.27342
  relation: reproduces
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
[... 100 more lines not kept]
```

**Agent**

Setting up a dev environment and opening the .mat file.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && . dev/bin/activate && uv pip install -q numpy scipy fsspec aiohttp requests h5py pandas statsmodels scikit-learn matplotlib ipykernel nbformat nbconvert pyyaml jsonschema && python -c "
import fsspec
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-4/live/AllRats.mat',block_size=2**20).open()
print(f.read(128))"
```

```
b'MATLAB 5.0 MAT-file, Platform: MACI64, Created on: Thu Jul 14 11:54:44 2016                                         \x00\x00\x00\x00\x00\x00\x00\x00\x00\x01IM'
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > load.py <<'EOF'
import fsspec, scipy.io, time, resource, pickle
t=time.time()
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-4/live/AllRats.mat',block_size=2**22).open()
d=scipy.io.loadmat(f, squeeze_me=True, struct_as_record=False)
print(time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
A=d['AllRats']; print(type(A), A.shape)
e=A[0]; print(e._fieldnames)
for k in e._fieldnames:
    v=getattr(e,k); print(k, type(v).__name__, getattr(v,'shape',None), repr(v)[:200])
EOF
python load.py
```

```
6.015965223312378 0.4458
<class 'numpy.ndarray'> (80,)
['Trialn', 'StartTime', 'NPDuration', 'NPTimeReq', 'StimOnsetDelay', 'StimNumber', 'StimName', 'TargetDP', 'ChosenDP', 'Complete', 'Withdrew', 'Timeout', 'Correct', 'DPopentime', 'HistDepth', 'RecName', 'RecTime', 'TrialCells', 'TempSig', 'StimReg', 'BestBin', 'RatName', 'StimTimes', 'TrialCellInfo', 'LongShortInfo']
Trialn ndarray (150,) array([  1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,
        14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25,  26,
        27,  28,  29,  30,  31,  32,  33,  34,  35,  36,
StartTime ndarray (150,) array([ 118.82,  145.87,  150.45,  179.43,  199.77,  202.63,  283.82,
        288.2 ,  292.25,  295.35,  298.07,  300.37,  302.4 ,  304.83,
        307.35,  309.83,  312.13,  314.42,  316.92,  319.27,
NPDuration ndarray (150,) array([282, 202, 278,  64, 332, 212, 224, 274, 298, 262, 282, 268, 286,
       296, 268, 310, 254, 254, 254, 308, 274, 264, 270, 178, 176, 292,
       260, 260, 226, 284, 260, 280, 254, 276, 284, 332,
NPTimeReq ndarray (150,) array([250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250,
       250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250,
       250, 250, 250, 250, 250, 250, 250, 250, 250, 250,
StimOnsetDelay ndarray (150,) array([83, 92, 80, 97, 94, 83, 85, 94, 92, 88, 82, 88, 94, 83, 78, 95, 86,
       97, 75, 78, 78, 93, 83, 98, 80, 90, 86, 89, 98, 86, 92, 85, 80, 92,
       87, 78, 76, 77, 97, 94, 88, 99, 76, 91, 85,
StimNumber ndarray (150,) array([3, 1, 2, 3, 3, 4, 3, 4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 2, 1, 1, 2, 1,
       3, 2, 3, 1, 3, 4, 4, 2, 3, 3, 4, 4, 2, 2, 1, 1, 4, 4, 3, 1, 3, 3,
[... 48 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > explore.py <<'EOF'
import fsspec, scipy.io, numpy as np
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-4/live/AllRats.mat',block_size=2**22).open()
d=scipy.io.loadmat(f, squeeze_me=True, struct_as_record=False)
A=d['AllRats']
e=A[0]
def show(s,name):
    print('==',name, s._fieldnames)
    for k in s._fieldnames:
        v=getattr(s,k); print('  ',k, type(v).__name__, getattr(v,'shape',None), repr(v)[:300])
show(e.TempSig,'TempSig'); show(e.TrialCellInfo,'TrialCellInfo'); show(e.LongShortInfo,'LongShortInfo')
show(e.BestBin[0],'BestBin0'); show(e.StimReg[0,0],'StimReg00')
r=e.StimReg[0,0]
for k in r._fieldnames:
    v=getattr(r,k)
    if hasattr(v,'_fieldnames'): show(v,k)
print(e.StimTimes)
print(np.asarray(e.StimReg[0,3].RtStBins).shape)
EOF
python explore.py
```

```
== TempSig ['Params', 'TemporalPval']
   Params mat_struct None <scipy.io.matlab._mio5_params.mat_struct object at 0x750f88a444d0>
   TemporalPval ndarray (9,) array([0.    , 0.    , 0.    , 0.1915, 0.    , 0.    , 0.    , 0.    ,
       0.    ])
== TrialCellInfo ['Id', 'Elect', 'IsiDistrib', 'Waveform', 'SigToNoise', 'RefractViolKJL', 'CellTypeKJL']
   Id ndarray (9,) array(['Electrode 1, Cell 1', 'Electrode 1, Cell 2',
       'Electrode 1, Cell 3', 'Electrode 2, Cell 1',
       'Electrode 3, Cell 1', 'Electrode 4, Cell 1',
       'Electrode 4, Cell 2', 'Electrode 5, Cell 1',
       'Electrode 5, Cell 2'], dtype=object)
   Elect ndarray (9,) array([1, 1, 1, 2, 3, 4, 4, 5, 5], dtype=uint8)
   IsiDistrib ndarray (9,) array([array([[0.000e+00, 1.300e+01],
              [1.000e+00, 8.570e+02],
              [2.000e+00, 1.405e+03],
              [3.000e+00, 1.313e+03],
              [4.000e+00, 1.223e+03],
              [5.000e+00, 9.140e+02],
              [6.000e+00, 8.120e+02],
              [7.000e+00, 7.310e+0
   Waveform ndarray (9,) array([array([  -3.79472371,   -4.41544238,   -5.15174742,   -5.96543386,
[... 84 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "" paper/10.1371-journal.pbio.1002549.txt | awk -F: 'length($0)>0{print $1": "substr($0, length($1)+2, 100)}' | head -300
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 129,140p paper/10.1371-journal.pbio.1002549.txt; sed -n 155,241p paper/10.1371-journal.pbio.1002549.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/48cbaa43-b35d-452c-8bc0-0dfa6fe1c735/tool-results/btkxks5s9.txt"
}
```

```
1	After 14.2 ± 4.4 (standard deviation [s.d.]) (range: 8–22) d of training on FFF-FMS-SMF-SSS discrimination, all eight rats successfully discriminated FFF from SSS stimuli, but failed to respond appropriately to FMS and SMF stimuli, instead treating them as equivalent and intermediate between FFF and SSS ( Fig 2A and 2B ). Seven out of eight rats failed to differentiate at all between FMS from SMF stimuli (proportion test, Bonferroni-adjusted p -value >0.00625). One rat (62SC) showed modest but significant discrimination, with more right-side choices to FMS than SMF stimuli ( p = 0.0039). Behavior was stable, on average, across the training period ( S2 Fig ). Thus, seven out of eight rats showed behavior consistent with guiding decisions by time-integrated whisker information. To examine this further, we plotted the mean behavioral performance of each rat versus the mean speed of panel movement across the entire sequence (150 ms). Behavioral performance was computed as (fraction of right drink port choices for each stimulus)–(mean fraction of right drink port choices for all stimuli), to account for right-left choice bias by some rats ( Fig 2B ). Right drink port choice was strongly related to mean sequence speed for all rats ( Fig 2C ).
2	
3	Behavioral performance on FFF-FMS-SMF-SSS discrimination task. (A) Discrimination performance for one example rat, across 13 d of training (44–50 trials for each stimulus per day). FMS and SMF stimuli were first introduced on Day 0. The rat reliably discriminated FFF from SSS stimuli but treated FMS and SMF stimuli identically and at chance. The rat responded similarly to all stimuli when the panel was fixed, and thus was not discriminating based on piezo auditory cues. (B) Mean performance (± SEM) for all rats across all behavior sessions. (C) Relative right drink port choice as a function of mean panel speed over the entire 150-ms sequence. Each symbol is a different rat ( n = 8). (D) D-prime analysis of FFF versus SSS discr
[... 97 more lines not kept]
```

**Agent**

Now the Methods.

**Agent calls Bash**

```bash
sed -n 271,400p paper/10.1371-journal.pbio.1002549.txt | grep -v "^$" | grep -v "^\[" | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && cat > survey.py <<'EOF'
import fsspec, scipy.io, numpy as np, collections
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-4/live/AllRats.mat',block_size=2**22).open()
A=scipy.io.loadmat(f, squeeze_me=True, struct_as_record=False)['AllRats']
rats=collections.Counter(e.RatName for e in A); print(rats)
nu=collections.Counter(); lab=collections.Counter(); ntr=[]; names=collections.Counter()
print(A[0].TempSig.Params._fieldnames, [getattr(A[0].TempSig.Params,k) for k in A[0].TempSig.Params._fieldnames])
for i,e in enumerate(A):
    ct=np.atleast_1d(e.TrialCellInfo.CellTypeKJL); nu.update(ct)
    lab.update(np.atleast_1d(e.LongShortInfo.DFLabel)); names.update(np.atleast_1d(e.StimName))
    ntr.append(len(np.atleast_1d(e.StimNumber)))
    if i<80: print(i,e.RatName,e.RecName,e.RecTime,'trials',ntr[-1],'units',len(ct),'TC',np.shape(e.TrialCells),'depth',np.atleast_1d(e.HistDepth).round(0),'elect',np.unique(np.atleast_1d(e.TrialCellInfo.Elect)), 'NPreq',np.unique(e.NPTimeReq), 'stimnums',np.unique(e.StimNumber))
print(nu, sum(nu.values())); print(lab); print(names); print(sum(ntr))
EOF
python survey.py
```

```
Wed Nov 11 17:03:43 UTC 2026
Counter({'62B': 22, '18R': 19, '18RI': 15, '18FB': 12, '107ST': 12})
['window', 'starttime', 'endtime', 'nperm'] [10, -50, 300, 10000]
0 18FB 18FB101411.ddt 14-Oct-2011 14:08 trials 150 units 9 TC (150, 9) depth [745. 745. 745. 745. 745.] elect [1 2 3 4 5] NPreq [250] stimnums [1 2 3 4]
1 18FB 18FB101511.ddt 15-Oct-2011 12:13 trials 134 units 16 TC (134, 16) depth [859. 859. 859. 859. 859.] elect [1 2 3 4 5] NPreq [250] stimnums [1 2 3 4]
2 18FB 18FB101611.ddt 16-Oct-2011 11:49 trials 268 units 12 TC (268, 12) depth [974. 974. 974. 974. 974.] elect [1 2 3 4 5] NPreq [250] stimnums [1 2 3 4]
3 18FB 18FB101711.ddt 17-Oct-2011 15:19 trials 213 units 7 TC (213, 7) depth [1088. 1088. 1088. 1088. 1088.] elect [1 2 3 4 5] NPreq [250] stimnums [1 2 3 4]
4 18FB 18FB101811.ddt 18-Oct-2011 14:37 trials 219 units 8 TC (219, 8) depth [1203. 1203. 1203. 1203. 1203.] elect [1 2 3 4 5] NPreq [250] stimnums [1 2 3 4]
5 18FB 18FB101911.ddt 19-Oct-2011 15:25 trials 172 units 8 TC (172, 8) depth [1317. 1317. 1317. 1317. 1317.] elect [1 2 3 4 5] NPreq [250] stimnums [1 2 3 4]
6 18FB 18FB102011.ddt 20-Oct-2011 16:09 trials 212 units 9 TC (212, 9) depth [1432. 1432. 1432. 1432. 1432.] elect [1 2 3 4 5] NPreq [250] stimnums [1 2 3 4]
7 18FB 18FB102111.ddt 21-Oct-2011 15:21 trials 177 units 13 TC (177, 13) depth [1546. 1546. 1546. 1546. 1546.] elect [1 2 3 4 5] NPreq [250] stimnums [1 2 3 4]
8 18FB 18FB102211.ddt 22-Oct-2011 11:19 trials 150 units 8 TC (150, 8) depth [1661. 1661. 1661. 1661. 1661.] elect [1 2 3 4 5] NPreq [250] stimnums [1 2 3 4]
9 18FB 18FB2102211.ddt 22-Oct-2011 16:36 trials 89 units 9 TC (89, 9) depth [1775. 1775. 1775. 1775. 1775.] elect [1 2 3 4 5] NPreq [250] stimnums [1 2 3 4]
10 18FB 18FB102311.ddt 23-Oct-2011 14:51 trials 119 units 7 TC (119, 7) depth [1775. 1775. 1775. 1775. 1775.] elect [1 2 3 4 5] NPreq [250] stimnums [1 2 3 4]
11 18FB 18FB102411.ddt 24-Oct-2011 13:49 trials 206 units 9 TC (206, 9) depth [1890 1890 1890 1890 1890] el
[... 73 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > survey2.py <<'EOF'
import fsspec, scipy.io, numpy as np, collections
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-4/live/AllRats.mat',block_size=2**22).open()
A=scipy.io.loadmat(f, squeeze_me=True, struct_as_record=False)['AllRats']
c5=collections.Counter(); cn=collections.Counter(); ps=[]; perses=[]
for e in A:
    el=np.atleast_1d(e.TrialCellInfo.Elect); ct=np.atleast_1d(e.TrialCellInfo.CellTypeKJL)
    p=np.atleast_1d(e.TempSig.TemporalPval); lab=np.atleast_1d(e.LongShortInfo.DFLabel)
    for u in range(len(el)):
        (c5 if el[u]==5 else cn)[ct[u]]+=1
        if el[u]!=5: ps.append((p[u]<0.05, lab[u], e.RatName))
    perses.append(sum((el!=5)&(ct!='MU')))
print('e5',c5,sum(c5.values()),'other',cn,sum(cn.values()))
print('tempmod excl e5', sum(x[0] for x in ps), collections.Counter(x[1] for x in ps))
print('SU per session excl e5 mean', np.mean(perses), max(perses), min(perses))
print(collections.Counter((x[0], x[1]=='NoTempMod') for x in ps))
# irregular stim names
for e in A:
    n=np.atleast_1d(e.StimName)
    if any(s.startswith('Stim') for s in n):
        print(e.RecName, collections.Counter(zip(n, e.StimNumber)).most_common(8)); break
# Xval consistency
X0=None
for e in A[:3]:
    sr=e.StimReg
    for u in range(min(2,sr.shape[0])):
        x=np.array([sr[u,w].Xval[:,1] for w in range(36)])
        if X0 is None: X0=x
        print(e.RecName,u, np.abs(x-X0).max(), [sr[u,w].RtStBins.tolist() for w in (0,1,35)], sr[u,0].Delay)
x5=X0[0].reshape(4,36)
print(x5.round(1))
# check window w = sum of preceding w/5 5ms bins
cs=np.concatenate([np.zeros((4,36)),x5],1)
for w in [1,2,3,10,35]:
    pred=np.array([[cs[s,36+b-w+1:36+b+1].sum() for b in range(36)] for s in range(4)])
    print(w+1, np.abs(pred-X0[w].reshape(4,36)).max(), X0[w].reshape(4,36)[:, :5].round(1))
EOF
python survey2.py
```

```
e5 Counter({'SU_RS': 21, 'MU': 16, 'SU_FS': 10}) 47 other Counter({'SU_RS': 236, 'MU': 160, 'SU_FS': 63}) 459
tempmod excl e5 285 Counter({'NoTempMod': 173, 'FastPos': 148, 'SlowPos': 49, 'FastNeg': 45, 'SlowNeg': 43, 'ImproperPeakBin': 1})
SU per session excl e5 mean 3.7375 12 0
Counter({(np.True_, False): 285, (np.False_, True): 173, (np.False_, False): 1})
62B080111.ddt [(('Stim0_isi30_5/17.25/4.5_9/21.25/5_15/27.25/6.1', np.uint8(1)), 15), (('Stim2_isi30_15/27.25/6.1', np.uint8(4)), 14), (('Stim2_isi30_5/17.25/4.5', np.uint8(3)), 13), (('Stim1_isi30_15/27.25/6.1_9/21.25/5_5/17.25/4.5', np.uint8(2)), 11)]
18FB101411.ddt 0 0.0 [[5, 5], [5, 10], [5, 180]] 0
18FB101411.ddt 1 0.0 [[5, 5], [5, 10], [5, 180]] 0
18FB101511.ddt 0 0.0 [[5, 5], [5, 10], [5, 180]] 0
18FB101511.ddt 1 0.0 [[5, 5], [5, 10], [5, 180]] 0
18FB101611.ddt 0 0.0 [[5, 5], [5, 10], [5, 180]] 0
18FB101611.ddt 1 0.0 [[5, 5], [5, 10], [5, 180]] 0
[[2.9400e+01 1.0432e+03 3.3981e+03 2.1258e+03 2.3152e+03 8.5280e+02
  9.9860e+02 5.2540e+02 6.9110e+02 8.1830e+02 2.6810e+02 6.6330e+02
  3.0428e+03 1.8532e+03 3.0368e+03 8.0740e+02 3.0510e+02 1.8240e+02
  1.1090e+02 3.5400e+01 2.6360e+02 1.8600e+02 3.3340e+02 1.6415e+03
  1.6370e+03 8.3770e+02 2.3780e+03 1.0695e+03 1.0280e+02 1.9620e+02
  4.8800e+01 3.9800e+01 7.9000e+00 1.2850e+02 9.5100e+01 9.1000e+00]
 [4.4000e+01 3.9090e+02 1.9061e+03 1.3942e+03 7.7840e+02 2.3844e+03
  1.0219e+03 3.7800e+01 1.1200e+02 1.1180e+02 1.1220e+02 6.3000e+00
  1.5880e+02 7.2310e+02 2.8760e+03 1.3576e+03 2.2819e+03 1.4353e+03
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && cat > survey3.py <<'EOF'
import fsspec, scipy.io, numpy as np, collections
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-4/live/AllRats.mat',block_size=2**22).open()
A=scipy.io.loadmat(f, squeeze_me=True, struct_as_record=False)['AllRats']
for ei in [0,15,60]:
    e=A[ei]; sn=e.StimNumber; npd=e.NPDuration
    for u in [0,1]:
        Y=e.StimReg[u,0].Yval.reshape(4,36)
        for name,sel in [('all',np.ones_like(sn,bool)),('np>250',npd>250),('complete',e.Complete==1),('np>250&compl',(npd>250)&(e.Complete==1)), ('np>=250',npd>=250)]:
            C=np.zeros((4,36))
            for t in np.where(sel)[0]:
                s=np.atleast_1d(e.TrialCells[t,u])
                h,_=np.histogram(s,np.arange(0,181,5)); C[sn[t]-1]+=h
            print(ei,u,name,np.abs(C-Y).max(), C.sum(), Y.sum())
        # Is Yval a rate?
print(A[0].StimReg[0,0].Yval[:10])
e=A[0]; print('withdrew vs np', collections.Counter(zip(e.Withdrew, e.NPDuration>250, e.Complete)))
EOF
python survey3.py
```

```
Wed Nov 11 17:04:35 UTC 2026
0 0 all 4.0 700.0 589
0 0 np>250 2.0 623.0 589
0 0 complete 0.0 589.0 589
0 0 np>250&compl 0.0 589.0 589
0 0 np>=250 3.0 636.0 589
0 1 all 2.0 238.0 207
0 1 np>250 2.0 221.0 207
0 1 complete 0.0 207.0 207
0 1 np>250&compl 0.0 207.0 207
0 1 np>=250 2.0 222.0 207
15 0 all 8.0 950.0 538
15 0 np>250 1.0 540.0 538
15 0 complete 0.0 538.0 538
15 0 np>250&compl 0.0 538.0 538
15 0 np>=250 1.0 540.0 538
15 1 all 8.0 838.0 483
15 1 np>250 1.0 485.0 483
15 1 complete 0.0 483.0 483
15 1 np>250&compl 0.0 483.0 483
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; for s in 001 002; do curl -sL -o s$s.bin -w "%{http_code} %{content_type} %{size_download}\n" "https://journals.plos.org/plosbiology/article/file?type=supplementary&id=10.1371/journal.pbio.1002549.s$s"; done; file s00*.bin
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && uv pip install -q openpyxl && md5sum s00*.bin && python -c "
import pandas as pd
for f in ['s001.bin','s002.bin']:
    x=pd.read_excel(f,sheet_name=None,header=None)
    for k,v in x.items():
        print('=====',f,k,v.shape); print(v.head(40).to_string(max_cols=30,max_colwidth=14))
" > sx.txt; wc -l sx.txt; grep ===== sx.txt
```

```
78f680d6b80ca361f25e2b5c6b8e8f78  s001.bin
2cc739cf12afcaeaa5cad2831b470a12  s002.bin
/tmp/claude-1001/dev/lib/python3.13/site-packages/openpyxl/worksheet/_reader.py:329: UserWarning: Unknown extension is not supported and will be removed
  warn(msg)
/tmp/claude-1001/dev/lib/python3.13/site-packages/openpyxl/worksheet/_reader.py:329: UserWarning: Unknown extension is not supported and will be removed
  warn(msg)
/tmp/claude-1001/dev/lib/python3.13/site-packages/openpyxl/worksheet/_reader.py:329: UserWarning: Unknown extension is not supported and will be removed
  warn(msg)
/tmp/claude-1001/dev/lib/python3.13/site-packages/openpyxl/worksheet/_reader.py:329: UserWarning: Unknown extension is not supported and will be removed
  warn(msg)
/tmp/claude-1001/dev/lib/python3.13/site-packages/openpyxl/worksheet/_reader.py:329: UserWarning: Unknown extension is not supported and will be removed
  warn(msg)
/tmp/claude-1001/dev/lib/python3.13/site-packages/openpyxl/worksheet/_reader.py:329: UserWarning: Unknown extension is not supported and will be removed
  warn(msg)
/tmp/claude-1001/dev/lib/python3.13/site-packages/openpyxl/worksheet/_reader.py:329: UserWarning: Unknown extension is not supported and will be removed
  warn(msg)
/tmp/claude-1001/dev/lib/python3.13/site-packages/openpyxl/worksheet/_reader.py:329: UserWarning: Unknown extension is not supported and will be removed
  warn(msg)
/tmp/claude-1001/dev/lib/python3.13/site-packages/openpyxl/worksheet/_reader.py:329: UserWarning: Unknown extension is not supported and will be removed
  warn(msg)
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && awk '/===== s001.bin Fig 2/,/===== s001.bin Fig 6 A/' sx.txt; awk '/Fig S2 /,0' sx.txt
```

```
===== s001.bin Fig 2 (47, 11)
              0              1              2         3         4              5              6         7         8         9       10
0            NaN            NaN            NaN       NaN       NaN            NaN            NaN       NaN       NaN       NaN     NaN
1      Figure 2A            NaN            NaN       NaN       NaN            NaN            NaN       NaN       NaN       NaN     NaN
2            NaN  Rat 107ST:...            NaN       NaN       NaN            NaN  Fixed Pane...       NaN       NaN       NaN     NaN
3   Training Day            FFF            FMS       SMF       SSS            NaN  Fraction R...  Stimulus       NaN       NaN     NaN
4              1       0.774194            0.5   0.55814  0.342857            NaN          0.375       FFF       NaN       NaN     NaN
5              2       0.813953       0.638889  0.692308  0.395833            NaN       0.333333       FMS       NaN       NaN     NaN
6              3       0.741935       0.553191  0.342105     0.325            NaN       0.333333       SMF       NaN       NaN     NaN
7              4       0.666667       0.485714  0.509091  0.421053            NaN       0.275862       SSS       NaN       NaN     NaN
8              5        0.71875       0.433333  0.355556      0.25            NaN            NaN       NaN       NaN       NaN     NaN
9              6       0.774194       0.607143   0.44186  0.384615            NaN            NaN       NaN       NaN       NaN     NaN
10             7       0.666667       0.391304  0.338983  0.263158            NaN            NaN       NaN       NaN       NaN     NaN
11             8       0.666667       0.588235  0.483871  0.129032            NaN            NaN       NaN       NaN       NaN     NaN
12             9       0.682927       0.571429  0.490196  0.255319            NaN            NaN       NaN       NaN       NaN     NaN
13            10       0.821429       0.540541  0.574468  0.236842            Na
[... 154 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import pandas as pd, warnings; warnings.filterwarnings('ignore')
x=pd.read_excel('s001.bin',sheet_name='Fig 3',header=None); print(x.iloc[36:].to_string(max_colwidth=40))
x=pd.read_excel('s002.bin',sheet_name='Fig S2',header=None); print(x.iloc[34:].to_string(max_colwidth=40))
x=pd.read_excel('s002.bin',sheet_name='Fig S6',header=None); print(x.iloc[:4].to_string(max_colwidth=60)); print(x.iloc[38:].to_string(max_colwidth=60))
"
```

```
0             1            2             3            4         5    6
36              NaN            33          NaN           NaN          NaN  0.737201  NaN
37              NaN            34     0.498127           NaN          NaN       NaN  NaN
38              NaN            35     0.578947           NaN          NaN       NaN  NaN
39              NaN            36     0.527331           NaN        0.487       NaN  NaN
40              NaN            37      0.48062           NaN     0.519608       NaN  NaN
41              NaN            38     0.489712           NaN     0.518732       NaN  NaN
42              NaN            40          NaN           NaN     0.524355       NaN  NaN
43              NaN            41        0.441           NaN          NaN       NaN  NaN
44              NaN            42     0.513793           NaN          NaN       NaN  NaN
45              NaN            43     0.477912           NaN     0.513043       NaN  NaN
46              NaN            44     0.538462           NaN          NaN       NaN  NaN
47              NaN            45      0.53668           NaN     0.460317       NaN  NaN
48              NaN            46          NaN           NaN     0.536896       NaN  NaN
49              NaN            47          NaN           NaN     0.520408       NaN  NaN
50              NaN            50          NaN           NaN     0.514056       NaN  NaN
51              NaN            51          NaN           NaN          0.5       NaN  NaN
52              NaN            52          NaN           NaN     0.582734       NaN  NaN
53              NaN            55     0.493827           NaN          NaN       NaN  NaN
54              NaN            56     0.561111           NaN          NaN       NaN  NaN
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import fsspec, scipy.io, numpy as np, collections, hashlib
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-4/live/AllRats.mat',block_size=2**22).open()
A=scipy.io.loadmat(f, squeeze_me=True, struct_as_record=False)['AllRats']
e=A[0]
print(collections.Counter(zip(e.ChosenDP,e.Complete,e.Withdrew,e.Timeout)))
tot=collections.Counter()
for e in A: tot.update(zip(e.ChosenDP,e.Complete,e.Withdrew, e.NPDuration>250))
print(tot)
print([np.atleast_1d(e.StimTimes[s]).tolist() for s in range(4)] )
print(set(str([np.round(np.atleast_1d(x.StimTimes[s]),2).tolist() for s in range(4)]) for x in A))
print(A[0].BestBin[0].PeakBin, A[0].StimReg[0,0].Regress.Stats)
"
```

```
Counter({(np.int16(0), np.uint8(1), np.uint8(0), np.uint8(0)): 86, (np.int16(1), np.uint8(1), np.uint8(0), np.uint8(0)): 38, (np.int16(-1), np.uint8(0), np.uint8(1), np.uint8(0)): 18, (np.int16(-1), np.uint8(0), np.uint8(0), np.uint8(1)): 8})
Counter({(np.int16(0), np.uint8(1), np.uint8(0), np.True_): 7596, (np.int16(1), np.uint8(1), np.uint8(0), np.True_): 6590, (np.int16(-1), np.uint8(0), np.uint8(1), np.False_): 3757, (np.int16(-1), np.uint8(0), np.uint8(0), np.True_): 126, (np.int16(-1), np.uint8(0), np.uint8(1), np.True_): 3})
[[[0.0, 47.25], [47.25, 99.5], [99.5, 156.75]], [[0.0, 57.25], [57.25, 109.5], [109.5, 156.75]], [[0.0, 47.25], [47.25, 94.5], [94.5, 141.75]], [[0.0, 57.25], [57.25, 114.5], [114.5, 171.75]]]
{'[[[0.0, 47.25], [47.25, 98.5], [98.5, 146.75]], [[0.0, 57.25], [57.25, 108.5], [108.5, 156.75]], [[0.0, 47.25], [47.25, 94.5], [94.5, 141.75]], [[0.0, 57.25], [57.25, 114.5], [114.5, 171.75]]]', '[[[0.0, 47.25], [47.25, 99.5], [99.5, 156.75]], [[0.0, 57.25], [57.25, 109.5], [109.5, 156.75]], [[0.0, 47.25], [47.25, 94.5], [94.5, 141.75]], [[0.0, 57.25], [57.25, 114.5], [114.5, 171.75]]]', '[[[0.0, 50.25], [50.25, 105.5], [105.5, 165.75]], [[0.0, 60.25], [60.25, 115.5], [115.5, 165.75]], [[0.0, 50.25], [50.25, 100.5], [100.5, 150.75]], [[0.0, 60.25], [60.25, 120.5], [120.5, 180.75]]]'}
5 [3.38442621e-01 7.26450246e+01 2.06477310e-14 5.12393143e+00]
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "entries/mcguire-2016/ssc4.py",
 "content": "\"\"\"Loading and measures for CRCNS ssc-4 (McGuire, Telian, Laboy-Juarez et al. 2016, PLoS Biol 14 e1002549).\n\nThe data set is one MATLAB file, AllRats.mat, streamed from the public CRCNS bucket\n(crcns:ssc-4/unversioned, doi:10.6080/K06D5QXN). Nothing is written to disk.\n\nWhere each parameter comes from:\n- Trials. Neural analyses use completed trials (Complete == 1). The data set's own regression inputs\n  (StimReg(...).Yval) equal the spike counts summed over exactly these trials (checked in the\n  notebook), and the data descriptor says the paper used trials with nose poke > 250 ms, which all\n  completed trials meet. This is a detail taken from the data and its descriptor (author, step 1.6).\n- Layers from depth: L2/3 200-650, L4 650-975, L5a 975-1285, L5b 1285-1575, L6 1575-2200 um (Methods,\n  Neural Recordings).\n- Baseline 25 ms before stimulus onset (Results, S1 Recordings, paragraph 2; claim baseline-rates).\n- Impulse windows: evoked 5-35 ms after impulse onset, impulse baseline 0-10 ms before it, peak in a\n  40-ms window after onset of the 10-ms boxcar smoothed 1-ms PSTH (Methods, Stimulus-evoked responses).\n  The boxcar is centred, a standard choice.\n- Temporal modulation: 10-ms bins, 10,000 permutations, p < 0.05 (Methods, Temporal response\n  modulation). Spikes permuted uniformly within the window on each trial (claim's standard choice);\n  pooled over trials this makes the null PSTH multinomial with equal bin probabilities, which is\n  how it is drawn here. The variance of the PSTH across bins and the sum of squared deviations from\n  the mean permuted PSTH differ only by a constant under this null, so the two statistics the\n  claim names give the same p-value.\n- Regression: 5-ms bins 0-180 ms, regressor the integrated panel speed over 5-180 ms windows ending at\n  the bin start (Methods, Stimulus regression). The regressor values are the data set's own (Xval in\n  StimReg), the stimulus record the claim allows.\n- Decoders: logistic regression per unit, 10-ms bins or one bin 0-150 ms, 70% of trials to fit,\n  outputs normalised per unit, summed, 300 repeats (Methods, Neural Decoders). L2 penalty with C = 1\n  (scikit-learn's default, claim reading a) is fit here by Newton's method batched over units, which\n  gives the same optimum as scikit-learn's lbfgs (checked in the notebook). The 70% split is\n  stratified by class, and 100 pseudo-trials per class per repeat are drawn: standard choices.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport collections\nimport io\n\nimport fsspec\nimport numpy as np\nimport pandas as pd\nimport scipy.io\nfrom scipy import stats\n\nURL = \"https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-4/live/AllRats.mat\"\nDATASET = \"crcns:ssc-4/unversioned\"\nDOI = \"10.6080/K06D5QXN\"\nMD5 = \"a929b803ca0feab5270e807f571d13eb\"  # AllRats.mat, from ssc-4/live/checksums.md5\nS1_DATA = \"https://journals.plos.org/plosbiology/article/file?type=supplementary&id=10.1371/journal.pbio.1002549.s001\"\nS2_DATA = \"https://journals.plos.org/plosbiology/article/file?type=supplementary&id=10.1371/journal.pbio.1002549.s002\"\n\nRAT_NAMES = {\"18FB\": \"18FB\", \"18RI\": \"18Ri\", \"18R\": \"18Ro\", \"62B\": \"62BS\", \"107ST\": \"107St\"}\nSTIMS = [\"FMS\", \"SMF\", \"FFF\", \"SSS\"]          # StimNumber 1..4 (data descriptor)\nMEAN_SPEED = {\"FFF\": 65.7, \"FMS\": 54.4, \"SMF\": 54.7, \"SSS\": 44.6}   # Table 1, mm/s\nLAYERS = [(\"L2/3\", 200, 650), (\"L4\", 650, 975), (\"L5a\", 975, 1285), (\"L5b\", 1285, 1575), (\"L6\", 1575, 2200)]\nT0, T1 = -100, 400                            # 1-ms spike matrix span, ms from first impulse onset\n\n\ndef layer_of(depth):\n    for name, lo, hi in LAYERS:\n        if lo <= depth < hi:\n            return name\n    return \"none\"\n\n\ndef load_mat():\n    f = fsspec.open(URL, block_size=2**22).open()\n    return scipy.io.loadmat(f, squeeze_me=True, struct_as_record=False)[\"AllRats\"]\n\n\ndef fetch_xlsx(url):\n    with fsspec.open(url, block_size=2**20).open() as f:\n        return pd.read_excel(io.BytesIO(f.read()), sheet_name=None, header=None)\n\n\nclass Data:\n    \"\"\"Sessions, trials, units and a 1-ms spike matrix per session (trials x units x ms).\"\"\"\n\n    def __init__(self, A):\n        self.A = A\n        trials, units, self.spk, self.tw = [], [], [], []\n        for si, e in enumerate(A):\n            n = len(np.atleast_1d(e.StimNumber))\n            t = pd.DataFrame(dict(\n                session=si, rat=RAT_NAMES[e.RatName], date=pd.to_datetime(e.RecTime).date(),\n                stim=[STIMS[k - 1] for k in np.atleast_1d(e.StimNumber)],\n                stim_name=np.atleast_1d(e.StimName), chosen=np.atleast_1d(e.ChosenDP).astype(int),\n                target=np.atleast_1d(e.TargetDP).astype(int), complete=np.atleast_1d(e.Complete).astype(bool),\n                withdrew=np.atleast_1d(e.Withdrew).astype(bool), timeout=np.atleast_1d(e.Timeout).astype(bool),\n                correct=np.atleast_1d(e.Correct).astype(bool), np_dur=np.atleast_1d(e.NPDuration).astype(float),\n                np_req=np.atleast_1d(e.NPTimeReq), delay=np.atleast_1d(e.StimOnsetDelay).astype(float),\n                start_min=np.atleast_1d(e.StartTime)))\n            t[\"trial\"] = np.arange(n)\n            t[\"withdraw_t\"] = t.np_dur - t.delay   # nose poke withdrawal, ms after stimulus onset\n            trials.append(t)\n            info = e.TrialCellInfo\n            el = np.atleast_1d(info.Elect).astype(int)\n            depth = np.atleast_1d(e.HistDepth).astype(float)\n            ct = np.atleast_1d(info.CellTypeKJL)\n            pv = np.atleast_1d(e.TempSig.TemporalPval)\n            lab = np.atleast_1d(e.LongShortInfo.DFLabel)\n            bb = np.atleast_1d(e.BestBin)\n            nu = len(el)\n            for u in range(nu):\n                units.append(dict(session=si, rat=RAT_NAMES[e.RatName], unit=u, elect=el[u],\n                                  depth=depth[el[u] - 1], layer=layer_of(depth[el[u] - 1]), type=ct[u],\n                                  dep_temp_p=float(pv[u]), dep_label=lab[u], dep_peakbin=bb[u].PeakBin))\n            tc = np.asarray(e.TrialCells).reshape(n, nu)\n            M = np.zeros((n, nu, T1 - T0), np.uint8)\n            for i in range(n):\n                for u in range(nu):\n                    s = np.atleast_1d(tc[i, u]).astype(float)\n                    s = s[(s >= T0) & (s < T1)]\n                    np.add.at(M[i, u], np.floor(s - T0).astype(int), 1)\n            self.spk.append(M)\n            # counts in the 100 ms before nose poke withdrawal (Results, Neural Decoding, paragraph 4)\n            w = t.withdraw_t.values\n            C = np.zeros((n, nu))\n            for i in range(n):\n                for u in range(nu):\n                    s = np.atleast_1d(tc[i, u]).astype(float)\n                    C[i, u] = np.sum((s >= w[i] - 100) & (s < w[i]))\n            self.tw.append(C)\n        self.trials = pd.concat(trials, ignore_index=True)\n        self.units = pd.DataFrame(units)\n        self.units[\"uid\"] = np.arange(len(self.units))\n        self.stimtimes = [[np.atleast_2d(e.StimTimes[k]).astype(float) for k in range(4)] for e in A]\n\n    def onsets(self, si, stim):\n        \"\"\"Impulse onsets (ms, floored as in the descriptor's example code) for a session and sequence.\"\"\"\n        return np.floor(self.stimtimes[si][STIMS.index(stim)][:, 0]).astype(int)\n\n    def unit_trials(self, uid, sel=None):\n        \"\"\"Spike matrix (trials x ms) and trial table of one unit, completed trials only by default.\"\"\"\n        r = self.units.iloc[uid]\n        t = self.trials[self.trials.session == r.session]\n        m = t.complete.values if sel is None else sel(t)\n        return self.spk[r.session][m, r.unit, :].astype(float), t[m].reset_index(drop=True), \\\n            self.tw[r.session][m, r.unit]\n\n\ndef rate(M, a, b):\n    \"\"\"Mean rate (Hz) per trial in [a, b) ms from stimulus onset; M is trials x ms from T0.\"\"\"\n    return M[:, a - T0:b - T0].sum(1) * 1000.0 / (b - a)\n\n\n# ---------- temporal modulation ----------\n\ndef perm_pval(counts, rng, nperm=10000):\n    \"\"\"Permutation p-value of the variance of a pooled PSTH against uniformly redistributed spikes.\"\"\"\n    counts = np.asarray(counts, float)\n    N, k = int(counts.sum()), len(counts)\n    if N == 0:\n        return 1.0\n    obs = counts.var()\n    null = rng.multinomial(N, np.full(k, 1.0 / k), size=nperm).var(1)\n    return (np.sum(null >= obs - 1e-12) + 1) / (nperm + 1)\n\n\ndef temporal_counts(D, uid, reading):\n    \"\"\"Pooled 10-ms counts. reading 'np': 0-180 ms after nose poke entry; 'stim': 0-180 ms after\n    stimulus onset; 'deposit': -50 to 300 ms after onset (TempSig.Params of the data set).\"\"\"\n    M, t, _ = D.unit_trials(uid)\n    if reading == \"stim\":\n        return M[:, -T0:180 - T0].reshape(len(M), 18, 10).sum((0, 2))\n    if reading == \"deposit\":\n        return M[:, -50 - T0:300 - T0].reshape(len(M), 35, 10).sum((0, 2))\n    out = np.zeros(18)\n    for i, d in enumerate(t.delay.values.astype(int)):   # NP entry is `delay` ms before onset\n        out += M[i, -d - T0:-d + 180 - T0].reshape(18, 10).sum(1)\n    return out\n\n\n# ---------- impulse-locked measures ----------\n\ndef box10(x):\n    return np.convolve(x, np.ones(10) / 10, mode=\"same\")\n\n\ndef impulse_segments(D, uid, stims=None, pulses=(0, 1, 2), kinds=None, trials_sel=None):\n    \"\"\"Per impulse instance (sequence, pulse) the trial x ms spike matrix aligned to impulse onset,\n    from -10 to +40 ms. Returns a list of dicts.\"\"\"\n    M, t, _ = D.unit_trials(uid, trials_sel)\n    si = int(D.units.iloc[uid].session)\n    segs = []\n    for s in (stims or STIMS):\n        m = (t.stim == s).values\n        if m.sum() == 0:\n            continue\n        on = D.onsets(si, s)\n        for p in pulses:\n            k = s[p]\n            if kinds and k not in kinds:\n                continue\n            a = on[p] - 10 - T0\n            segs.append(dict(stim=s, pulse=p, kind=k, X=M[m, a:a + 50], trials=t[m]))\n    return segs\n\n\ndef evoked_peak(segs, pooled=True):\n    \"\"\"Peak modulation (signed extreme of larger |deviation| from the 0-10 ms pre-impulse baseline,\n    in the 10-ms smoothed PSTH over 0-40 ms after onset), the 5-35 ms mean minus baseline, and the\n    latency of the maximum. pooled: one PSTH over all impulses (reading i); else per impulse, averaged\n    (reading ii).\"\"\"\n    def one(X):\n        psth = X.mean(0) * 1000.0\n        base = psth[0:10].mean()\n        sm = box10(psth)[10:50] - base\n        imax, imin = sm.argmax(), sm.argmin()\n        peak = sm[imax] if abs(sm[imax]) >= abs(sm[imin]) else sm[imin]\n        return peak, psth[15:45].mean() - base, float(imax)\n    if pooled:\n        X = np.concatenate([g[\"X\"] for g in segs])\n        return one(X)\n    v = np.array([one(g[\"X\"]) for g in segs])\n    return tuple(v.mean(0))\n\n\ndef impulse_ttest(segs):\n    \"\"\"Per trial, mean rate 5-35 ms after impulse onset against 0-10 ms before, averaged over the\n    trial's impulses; paired t test across trials. Returns (t, p two-sided, p one-sided greater).\"\"\"\n    post, pre = [], []\n    for g in segs:\n        post.append(g[\"X\"][:, 15:45].mean(1) * 1000)\n        pre.append(g[\"X\"][:, 0:10].mean(1) * 1000)\n    # group by trial within each sequence: impulses of the same trial are averaged\n    d = collections.defaultdict(list)\n    for g, a, b in zip(segs, post, pre):\n        for i, (x, y) in enumerate(zip(a, b)):\n            d[(g[\"stim\"], i)].append(x - y)\n    diff = np.array([np.mean(v) for v in d.values()])\n    if diff.std() == 0:\n        return 0.0, 1.0, 1.0\n    r = stats.ttest_1samp(diff, 0)\n    return r.statistic, r.pvalue, (r.pvalue / 2 if r.statistic > 0 else 1 - r.pvalue / 2)\n\n\n# ---------- regression ----------\n\ndef regression(D, uid, use_rate=False):\n    \"\"\"36 OLS regressions of 5-ms counts (0-180 ms, 4 sequences) on the data set's integrated speed.\n    Returns arrays R2, p, slope over windows 5..180 ms.\"\"\"\n    r = D.units.iloc[uid]\n    e = D.A[r.session]\n    M, t, _ = D.unit_trials(uid)\n    Y = np.zeros((4, 36))\n    for k, s in enumerate(STIMS):\n        m = (t.stim == s).values\n        Y[k] = M[m, -T0:180 - T0].reshape(m.sum(), 36, 5).sum((0, 2))\n        if use_rate:\n            Y[k] = Y[k] / max(m.sum(), 1) / 0.005\n    y = Y.ravel()\n    sr = np.atleast_2d(e.StimReg)[r.unit]\n    R2, P, B = np.zeros(36), np.ones(36), np.zeros(36)\n    for w in range(36):\n        x = np.asarray(sr[w].Xval)[:, 1]\n        res = stats.linregress(x, y)\n        R2[w], P[w], B[w] = res.rvalue**2, res.pvalue, res.slope\n    return R2, P, B\n\n\ndef classify(best_ms, slope, sig, which=\"all\", medium55=False):\n    \"\"\"Fast 5-20 ms, Medium 25-50 (or 25-55), Slow above; Slow split by slope sign (Results).\"\"\"\n    if which == \"sig\" and not sig:\n        return \"none\"\n    if best_ms <= 20:\n        return \"Fast\"\n    if best_ms <= (55 if medium55 else 50):\n        return \"Medium\"\n    return \"SlowPos\" if slope > 0 else \"SlowNeg\"\n\n\n# ---------- logistic decoders ----------\n\ndef fit_logistic(X, y, w, C=1.0, iters=25):\n    \"\"\"L2-penalised logistic regression (scikit-learn's objective: 0.5|b|^2 + C sum w*logloss, intercept\n    unpenalised), batched: X (P, n, d), y and w (P, n). Newton's method. Returns (P, d+1).\"\"\"\n    P, n, d = X.shape\n    Xa = np.concatenate([X, np.ones((P, n, 1))], 2)\n    beta = np.zeros((P, d + 1))\n    reg = np.ones(d + 1) / C\n    reg[-1] = 1e-8\n    for _ in range(iters):\n        z = np.einsum(\"pnd,pd->pn\", Xa, beta)\n        mu = 1 / (1 + np.exp(-z))\n        g = np.einsum(\"pnd,pn->pd\", Xa, w * (mu - y)) + reg * beta\n        Wt = w * mu * (1 - mu)\n        H = np.einsum(\"pnd,pn,pne->pde\", Xa, Wt, Xa) + np.eye(d + 1) * reg\n        step = np.linalg.solve(H, g[..., None])[..., 0]\n        beta -= step\n        if np.abs(step).max() < 1e-8:\n            break\n    return beta\n\n\ndef predict_logistic(beta, X):\n    Xa = np.concatenate([X, np.ones(X.shape[:-1] + (1,))], -1)\n    return 1 / (1 + np.exp(-(Xa @ beta)))\n"
}
```

```
File created successfully at: entries/mcguire-2016/ssc4.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cat >> entries/mcguire-2016/ssc4.py <<'EOF'


def unit_features(D, uid, kind):
    """Completed-trial features of one unit: '10ms' (15 counts, 0-150 ms), '1bin' (count 0-150 ms),
    'pre100' (count in the 100 ms before withdrawal). Returns X, trial table."""
    M, t, tw = D.unit_trials(uid)
    if kind == "10ms":
        X = M[:, -T0:150 - T0].reshape(len(M), 15, 10).sum(2)
    elif kind == "1bin":
        X = M[:, -T0:150 - T0].sum(1, keepdims=True)
    else:
        X = tw[:, None]
    return X.astype(float), t


def transform(X, how, rng):
    if how == "norm":   # each trial's count vector divided by its Euclidean norm (Methods)
        n = np.linalg.norm(X, axis=1, keepdims=True)
        return np.divide(X, n, out=np.zeros_like(X), where=n > 0)
    if how == "scramble":   # spikes redistributed uniformly over the 0-150 ms window of each trial
        return np.array([rng.multinomial(int(c), np.full(X.shape[1], 1 / X.shape[1])) for c in X.sum(1)], float)
    return X


def _split(y, rng, frac=0.7):
    tr = np.zeros(len(y), bool)
    for c in np.unique(y):
        idx = np.where(y == c)[0]
        rng.shuffle(idx)
        tr[idx[:int(round(frac * len(idx)))]] = True
    return tr


def _cv_C(Xs, ys, rng, Cs, folds=5):
    """Per problem, the C of the grid with the best mean held-out accuracy over stratified folds."""
    P = len(Xs)
    acc = np.zeros((P, len(Cs)))
    fold_of = []
    for y in ys:
        f = np.zeros(len(y), int)
        for c in np.unique(y):
            idx = np.where(y == c)[0]
            rng.shuffle(idx)
            f[idx] = np.arange(len(idx)) % folds
        fold_of.append(f)
    for k in range(folds):
        Xtr = [x[f != k] for x, f in zip(Xs, fold_of)]
        ytr = [y[f != k] for y, f in zip(ys, fold_of)]
        Xb, yb, wb = _pad(Xtr, ytr)
        for j, C in enumerate(Cs):
            beta = fit_logistic(Xb, yb, wb, C=C)
            for p in range(P):
                te = fold_of[p] == k
                if te.sum():
                    acc[p, j] += np.mean((predict_logistic(beta[p], Xs[p][te]) > 0.5) == (ys[p][te] > 0.5)) / folds
    return np.array(Cs)[acc.argmax(1)]


def _pad(Xs, ys):
    n = max(len(x) for x in Xs)
    d = Xs[0].shape[1]
    X = np.zeros((len(Xs), n, d))
    y = np.zeros((len(Xs), n))
    w = np.zeros((len(Xs), n))
    for i, (a, b) in enumerate(zip(Xs, ys)):
        X[i, :len(a)] = a
        y[i, :len(b)] = b
        w[i, :len(b)] = 1
    return X, y, w


def _fit(Xs, ys, rng, cv):
    Xb, yb, wb = _pad(Xs, ys)
    if not cv:
        return fit_logistic(Xb, yb, wb)
    Cs = _cv_C(Xs, ys, rng, [1e-3, 1e-2, 1e-1, 1, 10, 100])
    return np.stack([fit_logistic(Xb[i:i + 1], yb[i:i + 1], wb[i:i + 1], C=C)[0] for i, C in enumerate(Cs)])


def stim_decoder(D, uids, kind="10ms", how=None, repeats=300, seed=0, cv=False, npseudo=100):
    """Population one-vs-all stimulus decoder (Methods, Neural Decoders). Returns the mean confusion
    matrix (rows true FFF, FMS, SMF, SSS; rows sum to 1), per-repeat accuracy and per-unit accuracy."""
    rng = np.random.default_rng(seed)
    order = ["FFF", "FMS", "SMF", "SSS"]
    feats = []
    for u in uids:
        X, t = unit_features(D, u, kind)
        X = transform(X, how, rng)
        feats.append((X, np.array([order.index(s) for s in t.stim])))
    U = len(feats)
    conf = np.zeros((4, 4))
    accs, unit_acc = [], np.zeros(U)
    for r in range(repeats):
        Xs, ys, tests = [], [], []
        for X, y in feats:
            tr = _split(y, rng)
            tests.append((X[~tr], y[~tr]))
            for c in range(4):
                Xs.append(X[tr])
                ys.append((y[tr] == c).astype(float))
        beta = _fit(Xs, ys, rng, cv).reshape(U, 4, -1)
        probs = []
        for i, (Xt, yt) in enumerate(tests):
            p = np.stack([predict_logistic(beta[i, c], Xt) for c in range(4)], 1)
            p = p / p.sum(1, keepdims=True)
            probs.append((p, yt))
            unit_acc[i] += np.mean(p.argmax(1) == yt) / repeats
        cm = np.zeros((4, 4))
        for c in range(4):
            tot = np.zeros((npseudo, 4))
            for p, yt in probs:
                idx = np.where(yt == c)[0]
                if len(idx):
                    tot += p[rng.choice(idx, npseudo)]
            pred = tot.argmax(1)
            cm[c] = np.bincount(pred, minlength=4) / npseudo
        conf += cm / repeats
        accs.append(np.trace(cm) / 4)
    return conf, np.array(accs), unit_acc


def choice_decoder(D, uids, kind="1bin", repeats=300, seed=0, cv=False, npseudo=100):
    """Population choice decoder (Methods): one logistic function per unit fit on trials of all four
    sequences, tested within each sequence. Returns, per sequence, accuracy with equal numbers of
    right and left pseudo-trials (reading i) and with the data's proportions (reading ii), averaged
    over repeats, and each unit's balanced accuracy on its own test trials."""
    rng = np.random.default_rng(seed)
    feats = []
    for u in uids:
        X, t = unit_features(D, u, kind)
        feats.append((X, (t.chosen.values == 1).astype(float), t.stim.values))
    allt = pd.concat([unit_features(D, u, kind)[1] for u in uids])
    pright = allt.groupby("stim").chosen.mean().to_dict()
    U = len(feats)
    res = {s: np.zeros(2) for s in STIMS}
    unit_acc = np.zeros(U)
    for r in range(repeats):
        Xs, ys, tests = [], [], []
        for X, y, st in feats:
            tr = _split(y + 2 * np.array([STIMS.index(s) for s in st]), rng)   # stratify by stim and choice
            Xs.append(X[tr])
            ys.append(y[tr])
            tests.append((X[~tr], y[~tr], st[~tr]))
        beta = _fit(Xs, ys, rng, cv)
        P = [(predict_logistic(beta[i], Xt), yt, st) for i, (Xt, yt, st) in enumerate(tests)]
        for i, (p, yt, st) in enumerate(P):
            unit_acc[i] += np.mean([np.mean((p[yt == c] > 0.5) == c) for c in (0, 1) if np.any(yt == c)]) / repeats
        for s in STIMS:
            acc_c = {}
            for c in (0, 1):
                tot = np.zeros(npseudo)
                cnt = np.zeros(npseudo)
                for p, yt, st in P:
                    idx = np.where((st == s) & (yt == c))[0]
                    if len(idx):
                        tot += p[rng.choice(idx, npseudo)]
                        cnt += 1
                acc_c[c] = np.mean((tot > cnt / 2) == c)
            res[s] += np.array([(acc_c[0] + acc_c[1]) / 2,
                                pright[s] * acc_c[1] + (1 - pright[s]) * acc_c[0]]) / repeats
    return res, unit_acc
EOF
cd $TMPDIR && . dev/bin/activate && cd entries/mcguire-2016 && cat > $TMPDIR/t1.py <<'EOF'
import time, resource, numpy as np, sys
sys.path.insert(0,'.')
import ssc4
t=time.time(); D=ssc4.Data(ssc4.load_mat()); print('load',time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
print(len(D.units), D.trials.shape)
rng=np.random.default_rng(0)
t=time.time()
ps={r:np.array([ssc4.perm_pval(ssc4.temporal_counts(D,u,r),rng) for u in D.units.uid]) for r in ['np','stim','deposit']}
print('perm',time.time()-t)
dep=D.units.dep_temp_p.values
for r,p in ps.items(): print(r,(p<0.05).sum(), 'agree with deposit', np.mean((p<0.05)==(dep<0.05)), np.corrcoef(p,dep)[0,1])
t=time.time()
R=[ssc4.regression(D,u) for u in D.units.uid[:50]]
print('reg 50',time.time()-t)
# compare with deposited
e=D.A[0]; R2,P,B=ssc4.regression(D,0); print(R2[:3], [np.atleast_2d(e.StimReg)[0][w].Regress.Stats[[0,2]] for w in range(3)])
EOF
python $TMPDIR/t1.py
```

```
load 7.958294153213501 0.589532
506 (18072, 17)
perm 43.67689800262451
np 312 agree with deposit 0.7351778656126482 nan
stim 261 agree with deposit 0.7490118577075099 nan
deposit 363 agree with deposit 0.8162055335968379 nan
reg 50 1.0157005786895752
[0.33844262 0.2581435  0.14377827] [array([3.38442621e-01, 2.06477310e-14]), array([2.58143497e-01, 8.00822737e-11]), array([1.43778266e-01, 2.77580556e-06])]
```

**Agent calls Bash**

```bash
date -u; cd entries/mcguire-2016 && . $TMPDIR/dev/bin/activate && cat > $TMPDIR/t2.py <<'EOF'
import time, numpy as np, sys
sys.path.insert(0,'.')
import ssc4
from sklearn.linear_model import LogisticRegression
D=ssc4.Data(ssc4.load_mat())
fm=D.units.uid[D.units.dep_label.isin(['FastPos','FastNeg'])].values
print(len(fm))
# check batched fit vs sklearn
X,t=ssc4.unit_features(D,fm[0],'10ms'); y=(t.stim=='FFF').values.astype(float)
b=ssc4.fit_logistic(X[None],y[None],np.ones((1,len(y))))
sk=LogisticRegression(C=1.0,max_iter=5000,tol=1e-10).fit(X,y); print(np.abs(b[0,:-1]-sk.coef_[0]).max(), b[0,-1], sk.intercept_)
t0=time.time(); conf,acc,ua=ssc4.stim_decoder(D,fm,'10ms',repeats=5); print('5 reps',time.time()-t0, acc.mean()); print(conf.round(2))
t0=time.time(); res,ua=ssc4.choice_decoder(D,fm,'1bin',repeats=5); print('choice 5 reps',time.time()-t0, res)
EOF
python $TMPDIR/t2.py
```

```
Wed Nov 11 17:09:36 UTC 2026
213
6.42918286386518e-08 -1.04418857655431 [-1.04418854]
5 reps 4.033289670944214 0.889
[[0.91 0.09 0.   0.  ]
 [0.09 0.84 0.02 0.05]
 [0.   0.   0.86 0.14]
 [0.   0.   0.05 0.95]]
choice 5 reps 1.2333550453186035 {'FMS': array([0.5       , 0.55119491]), 'SMF': array([0.5       , 0.56828902]), 'FFF': array([0.5       , 0.36735369]), 'SSS': array([0.5       , 0.67637403])}
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='ssc4.py'; s=open(p).read()
s=s.replace('''def _pad(Xs, ys):
    n = max(len(x) for x in Xs)''','''def _pad(Xs, ys, balanced=False):
    n = max(len(x) for x in Xs)''')
s=s.replace('''        y[i, :len(b)] = b
        w[i, :len(b)] = 1
    return X, y, w''','''        y[i, :len(b)] = b
        w[i, :len(b)] = 1
        if balanced:   # each class weighted to half the total, as scikit-learn's class_weight="balanced"
            for c in (0, 1):
                m = b == c
                if m.any():
                    w[i, :len(b)][m] = len(b) / (2 * m.sum())
    return X, y, w''')
s=s.replace('''def _fit(Xs, ys, rng, cv):
    Xb, yb, wb = _pad(Xs, ys)''','''def _fit(Xs, ys, rng, cv, balanced=False):
    Xb, yb, wb = _pad(Xs, ys, balanced)''')
s=s.replace('''def choice_decoder(D, uids, kind="1bin", repeats=300, seed=0, cv=False, npseudo=100):''','''def choice_decoder(D, uids, kind="1bin", repeats=300, seed=0, cv=False, npseudo=100, balanced=True):''')
s=s.replace('''    over repeats, and each unit's balanced accuracy on its own test trials."""''','''    over repeats, and each unit's balanced accuracy on its own test trials. balanced: training trials
    weighted so that right and left count equally (an assumption: the paper gives chance as 50%)."""''')
s=s.replace('''        beta = _fit(Xs, ys, rng, cv)
        P = [''','''        beta = _fit(Xs, ys, rng, cv, balanced)
        P = [''')
open(p,'w').write(s)
EOF
grep -n "balanced" ssc4.py | head
```

```
356:def _pad(Xs, ys, balanced=False):
366:        if balanced:   # each class weighted to half the total, as scikit-learn's class_weight="balanced"
374:def _fit(Xs, ys, rng, cv, balanced=False):
375:    Xb, yb, wb = _pad(Xs, ys, balanced)
424:def choice_decoder(D, uids, kind="1bin", repeats=300, seed=0, cv=False, npseudo=100, balanced=True):
428:    over repeats, and each unit's balanced accuracy on its own test trials. balanced: training trials
447:        beta = _fit(Xs, ys, rng, cv, balanced)
```

**Agent**

Now adding unit-level pipeline functions (temporal p-values, regression for all units, class assignment) to the helper so both notebooks share them.

**Agent calls Bash**

```bash
cat >> ssc4.py <<'EOF'


# ---------- unit selection pipeline shared by the notebooks ----------

def temporal_pvals(D, reading, seed):
    rng = np.random.default_rng(seed)
    return np.array([perm_pval(temporal_counts(D, u, reading), rng) for u in D.units.uid])


def regress_all(D, use_rate=False):
    """R2, p and slope (units x 36 windows) for every unit."""
    out = [regression(D, u, use_rate) for u in D.units.uid]
    return tuple(np.array([o[k] for o in out]) for k in range(3))


def unit_classes(R2, P, B, mod, which="all", medium55=False):
    """Class of each unit from its regression: temporally modulated units only ('none' otherwise).
    which='all': every modulated unit by its highest-R2 window (reading a); 'sig': only units with
    a window at p < 0.05/36 (reading b). Best window in ms, slope of that window."""
    best = (R2.argmax(1) + 1) * 5
    slope = B[np.arange(len(B)), R2.argmax(1)]
    sig = (P < 0.05 / 36).any(1)
    lab = np.array([classify(b, s, g, which, medium55) if m else "none"
                    for b, s, g, m in zip(best, slope, sig, mod)])
    return lab, best, slope, sig


def deposited_classes(D):
    """The data set's own labels mapped to the paper's classes: FastPos/FastNeg split at the 20-ms
    boundary into Fast and Medium by PeakBin (ms), SlowPos, SlowNeg; NoTempMod and others 'none'."""
    out = []
    for lab, pb in zip(D.units.dep_label, D.units.dep_peakbin):
        if lab in ("FastPos", "FastNeg"):
            out.append("Fast" if pb <= 20 else "Medium")
        elif lab in ("SlowPos", "SlowNeg"):
            out.append(lab)
        else:
            out.append("none")
    return np.array(out)
EOF
. $TMPDIR/dev/bin/activate && python -c "
import sys; sys.path.insert(0,'.'); import ssc4, numpy as np, collections
D=ssc4.Data(ssc4.load_mat())
print(collections.Counter(zip(D.units.dep_label, np.array(D.units.dep_peakbin)//5*5)).most_common(60))
"
```

```
[(('FastPos', np.float64(10.0)), 69), (('FastPos', np.float64(5.0)), 62), (('NoTempMod', np.float64(5.0)), 39), (('NoTempMod', np.float64(10.0)), 22), (('SlowPos', np.float64(180.0)), 21), (('SlowNeg', np.float64(180.0)), 21), (('NoTempMod', np.float64(15.0)), 16), (('FastPos', np.float64(15.0)), 12), (('NoTempMod', np.float64(180.0)), 12), (('FastNeg', np.float64(40.0)), 11), (('NoTempMod', np.float64(40.0)), 9), (('FastNeg', np.float64(25.0)), 9), (('NoTempMod', np.float64(55.0)), 7), (('FastPos', np.float64(20.0)), 7), (('NoTempMod', np.float64(30.0)), 6), (('FastPos', np.float64(25.0)), 6), (('NoTempMod', np.float64(45.0)), 6), (('NoTempMod', np.float64(160.0)), 6), (('NoTempMod', np.float64(105.0)), 5), (('NoTempMod', np.float64(130.0)), 5), (('NoTempMod', np.float64(65.0)), 5), (('FastNeg', np.float64(50.0)), 5), (('SlowPos', np.float64(150.0)), 5), (('FastNeg', np.float64(30.0)), 5), (('NoTempMod', np.float64(60.0)), 5), (('NoTempMod', np.float64(110.0)), 5), (('NoTempMod', np.float64(20.0)), 4), (('NoTempMod', np.float64(35.0)), 4), (('NoTempMod', np.float64(25.0)), 4), (('FastPos', np.float64(30.0)), 4), (('SlowNeg', np.float64(95.0)), 4), (('NoTempMod', np.float64(50.0)), 4), (('NoTempMod', np.float64(85.0)), 4), (('NoTempMod', np.float64(170.0)), 3), (('FastNeg', np.float64(15.0)), 3), (('FastNeg', np.float64(20.0)), 3), (('SlowNeg', np.float64(80.0)), 3), (('NoTempMod', np.float64(145.0)), 3), (('SlowPos', np.float64(175.0)), 3), (('FastNeg', np.float64(5.0)), 3), (('FastNeg', np.float64(35.0)), 3), (('NoTempMod', np.float64(165.0)), 3), (('FastNeg', np.float64(45.0)), 3), (('NoTempMod', np.float64(150.0)), 2), (('NoTempMod', np.float64(95.0)), 2), (('SlowNeg', np.float64(85.0)), 2), (('NoTempMod', np.float64(75.0)), 2), (('SlowNeg', np.float64(165.0)), 2), (('FastPos', np.float64(45.0)), 2), (('SlowPos', np.float64(65.0)), 2), (('SlowPos', np.float64(165.0)), 2), (('SlowPos', np.float64(90.0)), 2), (('SlowNeg', np.float64(175.0)), 2), (('SlowPos', np.fl
[... 1 more lines not kept]
```

**Agent**

Now the builder and the first notebook (data checks, behaviour, unit-level claims).

**Agent calls Bash**

```bash
cat > $TMPDIR/build.py <<'EOF'
"""Build an ipynb from a percent-format script: '# %% [markdown]' and '# %% tags=a,b' headers."""
import sys, nbformat, re
src, out = sys.argv[1], sys.argv[2]
cells, cur, kind, tags = [], [], None, []
def flush():
    if kind is None: return
    text = "\n".join(cur).strip("\n")
    if kind == "md":
        text = "\n".join(l[2:] if l.startswith("# ") else (l[1:] if l.startswith("#") else l) for l in text.split("\n"))
        c = nbformat.v4.new_markdown_cell(text)
    else:
        c = nbformat.v4.new_code_cell(text)
    if tags: c.metadata["tags"] = tags
    cells.append(c)
for line in open(src).read().split("\n"):
    m = re.match(r"# %%(.*)$", line)
    if m:
        flush(); cur = []
        h = m.group(1).strip()
        kind = "md" if "[markdown]" in h else "code"
        t = re.search(r"tags=(\S+)", h); tags = t.group(1).split(",") if t else []
    else:
        cur.append(line)
flush()
nb = nbformat.v4.new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nbformat.write(nb, out)
print(len(cells), "cells")
EOF
echo ok
```

```
ok
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb1.py",
 "content": "# %% [markdown]\n# # Reproducing McGuire, Telian, Laboy-Juarez et al. (2016) from CRCNS ssc-4: behaviour and single units\n#\n# Paper: McGuire LM, Telian G, Laboy-Juarez KJ, Miyashita T, Lee DJ, Smith KA, Feldman DE (2016),\n# \"Short Time-Scale Sensory Coding in S1 during Discrimination of Whisker Vibrotactile Sequences\",\n# PLoS Biology 14(8) e1002549, doi:10.1371/journal.pbio.1002549.\n#\n# Dataset: CRCNS ssc-4 (doi:10.6080/K06D5QXN), the single file `ssc-4/live/AllRats.mat`, streamed\n# from the public bucket `crcnsarchive`. Version: CRCNS data sets are not versioned, so the version\n# is recorded as `unversioned` and the file is pinned by the MD5 sum in the data set's\n# `checksums.md5`, a929b803ca0feab5270e807f571d13eb (printed below from the bucket). There is only\n# this one version of the data set in the bucket (`live/`, no `old/`), so it is the one pinned; the\n# paper cites the data set by accession only. Outside inputs: the paper's supporting information\n# S1 Data (doi:10.1371/journal.pbio.1002549.s001) and S2 Data (doi:10.1371/journal.pbio.1002549.s002),\n# read for the two claims whose data are there (`data: elsewhere`) and as variants.\n#\n# The claims file (`claims/mcguire-2016.yaml`) was written from the version of record (Europe PMC,\n# PMC5004814) with the Methods and the supporting legends.\n#\n# This notebook covers the behavioural and single-unit claims. The decoders (Figure 9) are in\n# `decoders.ipynb`, which uses the same helper (`ssc4.py`).\n#\n# | claim | here |\n# |---|---|\n# | fig2ab-fms-smf-not-discriminated | tested (5 of 8 rats in the data) |\n# | training-days | tested (5 of 8 rats) |\n# | fig2c-choice-follows-mean-speed | tested (5 of 8 rats) |\n# | fig2d-fixed-panel-impairs | blocked, data_missing (no fixed-panel trials); S2 Data shown as a variant |\n# | dprime-fff-sss-range | tested (5 of 8 rats) |\n# | fig3-fsfs-sffs-intensity-only | tested on S1 Data (elsewhere) |\n# | units-recorded | tested |\n# | baseline-rates | tested |\n# | temporal-modulation-count | tested |\n# | modulated-higher-baseline | tested |\n# | fig4d-evoked-modulation-by-layer | tested |\n# | latency-by-layer | tested |\n# | fig4d-gradual-decrease | tested |\n# | fig6-regression-significant | tested |\n# | fig6e-unit-classes | tested |\n# | fig6fg-laminar-classes | tested |\n# | fig7c-fast-impulse-velocity | tested |\n# | fig7c-fast-sequence-rate | tested |\n# | fig7-fff-adaptation | tested |\n# | fig7-sss-no-adaptation | tested |\n# | s4-fms-middle-pulse | tested |\n# | fig7de-medium-suppressed | tested |\n# | fig8a-slow-positive-no-sequence-difference | tested |\n# | fig8b-slow-negative-no-impulse-response | tested |\n# | fig8d-slow-positive-right-choice-l5 | tested |\n# | fig8d-fast-medium-no-choice-bias | tested |\n# | fig8e-choice-divergence-125ms | tested |\n# | s5-slow-positive-no-integration | tested |\n# | s6-head-position-choice | tested on S2 Data (elsewhere) |\n# | s7-no-fs-l5-slow-positive | tested |\n# | fig9b, fig9c, fig9d, fig9e, fig9f, fig9g (seven claims) | in `decoders.ipynb` |\n\n# %%\nimport collections, warnings\nimport numpy as np, pandas as pd, fsspec\nfrom scipy import stats\nimport matplotlib.pyplot as plt\nfrom statsmodels.stats.proportion import proportions_ztest\nfrom scipy.stats import chi2_contingency\nimport ssc4\nwarnings.filterwarnings(\"ignore\", category=UserWarning)\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 40)\n\nprint(fsspec.open(\"https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-4/live/checksums.md5\").open().read().decode())\nD = ssc4.Data(ssc4.load_mat())\nT, U = D.trials, D.units\nS1 = ssc4.fetch_xlsx(ssc4.S1_DATA)\nS2 = ssc4.fetch_xlsx(ssc4.S2_DATA)\nprint(\"S1 Data sheets\", list(S1), \"S2 Data sheets\", list(S2))\n\n# %% [markdown]\n# ## Data check\n\n# %% tags=sanity\nprint(\"sessions\", len(D.A), \"rats\", T.rat.nunique())\nprint(T.groupby(\"rat\").agg(sessions=(\"session\", \"nunique\"), days=(\"date\", \"nunique\"), trials=(\"trial\", \"size\")))\nprint(\"\\ntrials by sequence (StimNumber) and outcome\")\nT[\"outcome\"] = np.select([T.complete, T.withdrew, T.timeout], [\"choice\", \"early withdrawal\", \"no choice\"], \"other\")\nprint(pd.crosstab(T.stim, T.outcome, margins=True))\nprint(\"\\nStimName irregular names, by the StimNumber they carry (the descriptor says to use StimNumber)\")\nirr = T[~T.stim_name.isin(ssc4.STIMS)]\nprint(pd.crosstab(irr.stim_name, irr.stim))\nprint(\"\\nchosen port codes\", T.chosen.value_counts().to_dict(), \" target codes\", T.target.value_counts().to_dict())\nprint(\"completed trials with nose poke <= 250 ms:\", int((T.complete & (T.np_dur <= 250)).sum()))\nprint(\"nose poke duration (ms), completed trials: min %.0f, median %.0f, max %.0f\" % tuple(T[T.complete].np_dur.quantile([0, .5, 1])))\nprint(\"stimulus onset delay (ms): min %.0f max %.0f (Methods: 75-100)\" % (T.delay.min(), T.delay.max()))\nprint(\"required nose poke (ms)\", T.np_req.value_counts().to_dict())\nprint(\"\\nunits\", len(U))\nprint(pd.crosstab(U.layer, U.type, margins=True))\nprint(\"depth range (um) %.0f to %.0f\" % (U.depth.min(), U.depth.max()))\nprint(\"electrodes per session\", collections.Counter(len(np.atleast_1d(e.HistDepth)) for e in D.A))\nprint(\"distinct depths across electrodes within a session:\", max(len(set(np.atleast_1d(e.HistDepth).round(3))) for e in D.A))\nprint(\"\\nimpulse onset sets (ms) across sessions, StimTimes[:,0] by sequence FMS SMF FFF SSS:\")\nsets = collections.Counter(str([D.stimtimes[s][k][:, 0].tolist() for k in range(4)]) for s in range(len(D.A)))\nfor k, v in sets.items():\n    ss = [s for s in range(len(D.A)) if str([D.stimtimes[s][j][:, 0].tolist() for j in range(4)]) == k]\n    print(v, \"sessions\", k, \"rats\", sorted(set(T[T.session.isin(ss)].rat)))\nprint(\"\\nfields of a session:\", D.A[0]._fieldnames)\nprint(\"MapPosition (column of each electrode, named in the descriptor) present:\", \"MapPosition\" in D.A[0]._fieldnames)\nprint(\"deposited labels\", U.dep_label.value_counts().to_dict())\nprint(\"deposited TemporalPval < 0.05:\", int((U.dep_temp_p < 0.05).sum()))\nprint(\"TempSig.Params:\", {k: getattr(D.A[0].TempSig.Params, k) for k in D.A[0].TempSig.Params._fieldnames})\nspk_all = np.concatenate([M.sum(axis=(0, 2)) for M in D.spk])\nprint(\"spikes per unit in the -100..400 ms span: min %d, median %d\" % (spk_all.min(), np.median(spk_all)))\n\n# %% [markdown]\n# ### Checks of the description against the values\n#\n# 1. The regression inputs deposited with each unit (`StimReg(...).Yval`) against spike counts from\n#    `TrialCells`, to find which trials the authors analysed.\n# 2. The regressor (`Xval`) is the same for every unit and session.\n# 3. The deposited regression R2 and p against a fresh OLS fit.\n# 4. Recordings deposited twice: identical trial tables or spike trains across sessions.\n# 5. Columns: the descriptor says to drop units in columns A1 and B2 using `MapPosition`.\n\n# %%\nsel_names = {\"all trials\": lambda t: np.ones(len(t), bool), \"nose poke > 250 ms\": lambda t: (t.np_dur > 250).values,\n             \"completed\": lambda t: t.complete.values}\nmatch = collections.Counter()\nfor uid in U.uid:\n    r = U.iloc[uid]\n    Y = np.asarray(np.atleast_2d(D.A[r.session].StimReg)[r.unit][0].Yval).reshape(4, 36)\n    for name, f in sel_names.items():\n        M, t, _ = D.unit_trials(uid, f)\n        C = np.stack([M[(t.stim == s).values, -ssc4.T0:180 - ssc4.T0].reshape(-1, 36, 5).sum((0, 2)) for s in ssc4.STIMS])\n        match[name] += int(np.array_equal(C, Y))\nprint(\"units whose deposited Yval equals the summed counts, by trial selection:\", dict(match), \"of\", len(U))\n\nX0 = np.array([np.asarray(np.atleast_2d(D.A[0].StimReg)[0][w].Xval)[:, 1] for w in range(36)])\ndx = max(np.abs(np.array([np.asarray(np.atleast_2d(D.A[r.session].StimReg)[r.unit][w].Xval)[:, 1] for w in range(36)]) - X0).max()\n         for r in U.itertuples())\nprint(\"largest difference of Xval from the first unit's, over all units:\", dx)\n\nR2, P, B = ssc4.regress_all(D)\ndep = np.array([[np.atleast_2d(D.A[r.session].StimReg)[r.unit][w].Regress.Stats[[0, 2]] for w in range(36)] for r in U.itertuples()])\nprint(\"max |R2 - deposited R2| = %.2e, max |log10 p - deposited| = %.2e\" % (np.abs(R2 - dep[..., 0]).max(),\n      np.abs(np.log10(P + 1e-300) - np.log10(dep[..., 1] + 1e-300)).max()))\ndep_best = U.dep_peakbin.values\nprint(\"best window (highest R2) equals deposited PeakBin for\", int(((R2.argmax(1) + 1) * 5 == dep_best).sum()), \"of\", len(U), \"units\")\n\nfp = T.groupby(\"session\").apply(lambda t: hash((tuple(t.np_dur), tuple(t.stim), tuple(t.delay))))\nprint(\"sessions sharing a trial table with another:\", int(fp.duplicated(keep=False).sum()))\nsp = {}\nfor r in U.itertuples():\n    M = D.spk[r.session][:, r.unit, :]\n    sp.setdefault(hash(M[:20].tobytes()), []).append((r.session, r.unit))\nprint(\"unit pairs with identical spike matrices over the first 20 trials:\", [v for v in sp.values() if len(v) > 1])\n\n# %% [markdown]\n# ### Clock of the spikes against the trial table\n#\n# Spike times are said to be in ms from the first impulse onset. The second impulse starts about\n# 50 ms after the first in FFF and FMS (the F-first sequences) and about 60 ms after it in SMF and\n# SSS. If the spikes share the trial clock, the population rate 55 to 60 ms after onset (an early\n# response to impulse 2 at 50 ms) is higher in FFF and FMS trials than in SMF and SSS trials, and a\n# window before stimulus onset shows no such difference.\n\n# %%\ndef group_contrast(a, b):\n    out = []\n    for si, M in enumerate(D.spk):\n        t = T[T.session == si]\n        m = t.complete.values\n        st = t.stim.values[m]\n        r = M[m][:, :, a - ssc4.T0:b - ssc4.T0].sum((1, 2)) * 1000 / (b - a)\n        out.append(r[np.isin(st, [\"FFF\", \"FMS\"])].mean() - r[np.isin(st, [\"SMF\", \"SSS\"])].mean())\n    return np.array(out)\nfor a, b in [(55, 60), (-60, -55)]:\n    d = group_contrast(a, b)\n    print(\"window %d to %d ms: sessions with F-first > S-first rate %d of %d; mean difference %.1f Hz (summed over units); sign test p = %.2g\"\n          % (a, b, (d > 0).sum(), len(d), d.mean(), stats.binomtest(int((d > 0).sum()), len(d)).pvalue))\nfor rat in sorted(T.rat.unique()):\n    ss = sorted(T[T.rat == rat].session.unique())\n    d = group_contrast(55, 60)[ss]\n    print(\"  %s: %d of %d sessions F-first higher\" % (rat, (d > 0).sum(), len(d)))\n\n# %% [markdown]\n# ## Behaviour (Figure 2)\n#\n# Only the five recorded rats are in the data set (18FB, 18Ri, 18Ro, 62BS, 107St); the paper's\n# behaviour is from eight rats, and 62SC, 107Si and 62SS are not here. A trial enters when the rat\n# chose a port. The two trial readings of fig2ab-fms-smf-not-discriminated are (i) every trial with\n# a choice and (ii) completed trials with no premature withdrawal and nose poke over 250 ms.\n\n# %%\ndef behav_trials(reading):\n    t = T[T.chosen >= 0]\n    if reading == \"ii\":\n        t = t[t.complete & ~t.withdrew & (t.np_dur > 250)]\n    return t\nfor rd in [\"i\", \"ii\"]:\n    print(\"reading\", rd, \"trials\", len(behav_trials(rd)))\nbt = behav_trials(\"i\")\nfrac = bt.groupby([\"rat\", \"stim\"]).chosen.mean().unstack()[[\"FFF\", \"FMS\", \"SMF\", \"SSS\"]]\nntr = bt.groupby([\"rat\", \"stim\"]).chosen.size().unstack()[[\"FFF\", \"FMS\", \"SMF\", \"SSS\"]]\nprint(\"\\nfraction of right choices, all sessions pooled (reading i)\\n\", frac.round(3))\nprint(\"\\ntrials\\n\", ntr)\n\n# %% [markdown]\n# ### fig2ab-fms-smf-not-discriminated\n#\n# > All eight rats discriminated FFF from SSS but treated FMS and SMF as equivalent and\n# > intermediate; seven of eight showed no difference between FMS and SMF, and one rat (62SC) made\n# > more right choices to FMS than to SMF.\n\n# %% tags=claim:fig2ab-fms-smf-not-discriminated\nrows = []\nfor rd in [\"i\", \"ii\"]:\n    bt = behav_trials(rd)\n    for rat, t in bt.groupby(\"rat\"):\n        f = t.groupby(\"stim\").chosen.agg([\"sum\", \"size\"])\n        p = f[\"sum\"] / f[\"size\"]\n        cnt, nob = f.loc[[\"FMS\", \"SMF\"], \"sum\"].values, f.loc[[\"FMS\", \"SMF\"], \"size\"].values\n        z, pz = proportions_ztest(cnt, nob)\n        tab = np.array([cnt, nob - cnt])\n        chi_c = chi2_contingency(tab, correction=True)[1]\n        rows.append(dict(reading=rd, rat=rat, FFF=p.FFF, FMS=p.FMS, SMF=p.SMF, SSS=p.SSS,\n                         FFF_gt_SSS=p.FFF > p.SSS,\n                         between=(min(p.FMS, p.SMF) > p.SSS) and (max(p.FMS, p.SMF) < p.FFF),\n                         FMS_minus_SMF=p.FMS - p.SMF, p_z=pz, p_chi2_corrected=chi_c,\n                         sig_z=pz < 0.00625, sig_chi=chi_c < 0.00625))\nfig2ab = pd.DataFrame(rows)\nprint(fig2ab.round(4).to_string())\nprint(\"\\n62SC is not in the data set:\", \"62SC\" not in set(T.rat))\nprint(\"\\nVariant: the paper's own per-rat means (S1 Data, Figure 2B, mean over sessions), against the same from the data set\")\nf2 = S1[\"Fig 2\"]\npaper2b = pd.DataFrame(f2.iloc[23:31, 1:5].values.astype(float), index=f2.iloc[23:31, 0], columns=[\"FFF\", \"FMS\", \"SMF\", \"SSS\"])\nbt = behav_trials(\"i\")\nsess = bt.groupby([\"rat\", \"session\", \"stim\"]).chosen.mean().unstack().groupby(\"rat\").mean()[[\"FFF\", \"FMS\", \"SMF\", \"SSS\"]]\nname = {\"18FB\": \"18FB\", \"18Ri\": \"18Ri\", \"18Ro\": \"18Ro\", \"62BS\": \"62BS\", \"107St\": \"107ST\"}\ncmp = pd.concat({\"data set (mean of sessions)\": sess.rename(index=name), \"S1 Data\": paper2b.loc[[name[r] for r in sess.index]]}, axis=1)\nprint(cmp.round(3))\nprint(\"largest absolute difference: %.3f\" % np.abs(cmp[\"data set (mean of sessions)\"].values - cmp[\"S1 Data\"].values).max())\nprint(\"\\nS1 Data, all eight rats: FFF > SSS for\", int((paper2b.FFF > paper2b.SSS).sum()), \"of 8; FMS and SMF between for\",\n      int(((paper2b[[\"FMS\", \"SMF\"]].min(1) > paper2b.SSS) & (paper2b[[\"FMS\", \"SMF\"]].max(1) < paper2b.FFF)).sum()), \"of 8\")\n\n# %% [markdown]\n# ### training-days\n#\n# > Rats trained on FFF-FMS-SMF-SSS discrimination for 14.2 days on average (s.d. 4.4, range 8 to 22).\n\n# %% tags=claim:training-days\ndays = T.groupby(\"rat\").date.nunique()\nprint(days.to_string())\nprint(\"mean %.1f, s.d. %.1f, min %d, max %d (n = %d rats)\" % (days.mean(), days.std(), days.min(), days.max(), len(days)))\nprint(\"first and last recording date per rat:\")\nprint(T.groupby(\"rat\").date.agg([\"min\", \"max\"]))\n\n# %% [markdown]\n# ### fig2c-choice-follows-mean-speed\n#\n# > Relative right-port choice (fraction of right choices for a stimulus minus the mean over all\n# > stimuli) was strongly related to the mean speed of the sequence for all rats.\n\n# %% tags=claim:fig2c-choice-follows-mean-speed\nspeed = pd.Series(ssc4.MEAN_SPEED)[[\"FFF\", \"FMS\", \"SMF\", \"SSS\"]]\ndef fig2c_table(fr):\n    rel = fr.sub(fr.mean(1), axis=0)\n    out = pd.DataFrame(dict(\n        order_a=(rel.FFF > rel[[\"FMS\", \"SMF\"]].max(1)) & (rel[[\"FMS\", \"SMF\"]].min(1) > rel.SSS),\n        r=[stats.pearsonr(speed.values, rel.loc[i].values)[0] for i in rel.index]))\n    out[\"r_gt_0.8\"] = out.r > 0.8\n    return pd.concat([rel.round(3), out], axis=1)\nfor rd in [\"i\", \"ii\"]:\n    fr = behav_trials(rd).groupby([\"rat\", \"stim\"]).chosen.mean().unstack()[[\"FFF\", \"FMS\", \"SMF\", \"SSS\"]]\n    print(\"reading\", rd); print(fig2c_table(fr).round(3))\nprint(\"\\nVariant, all eight rats from S1 Data Figure 2B means:\")\nprint(fig2c_table(paper2b).round(3))\n\n# %% [markdown]\n# ### fig2d-fixed-panel-impairs (blocked: no fixed-panel trials in the data set)\n#\n# The data set holds only the four normal sequences (StimNumber 1 to 4, table above); the\n# fixed-panel sessions are not deposited. S2 Data holds the per-rat summary of S2B Fig, shown here\n# as a variant that does not decide the outcome.\n\n# %%\ns2b = S2[\"Fig S2\"].iloc[38:41, 0:9]\ns2b = pd.DataFrame(s2b.iloc[1:, 1:].values.astype(float), index=s2b.iloc[1:, 0].values, columns=s2b.iloc[0, 1:].values).T\nprint(s2b)\nboth = s2b.dropna()\nfor nm, d in [(\"rat with 0 kept\", both), (\"rat with 0 left out\", both[both.FixedPanel > 0])]:\n    r = stats.ttest_rel(d.MovingPanel, d.FixedPanel)\n    print(\"%s: n = %d, fixed lower in %d, paired t = %.2f, p = %.4f\" % (nm, len(d), (d.FixedPanel < d.MovingPanel).sum(), r.statistic, r.pvalue))\n\n# %% [markdown]\n# ### dprime-fff-sss-range\n#\n# > Discrimination of FFF against SSS in normal sessions was modest, with d-prime from 0.5 to 1.5 across rats.\n\n# %% tags=claim:dprime-fff-sss-range\ndef dprime(hr, fa, n1, n2):\n    hr = np.clip(hr, 0.5 / n1, 1 - 0.5 / n1)\n    fa = np.clip(fa, 0.5 / n2, 1 - 0.5 / n2)\n    return stats.norm.ppf(hr) - stats.norm.ppf(fa)\nfor rd in [\"i\", \"ii\"]:\n    bt = behav_trials(rd)\n    pooled, persess = {}, {}\n    for rat, t in bt.groupby(\"rat\"):\n        f = t.groupby(\"stim\").chosen.agg([\"mean\", \"size\"])\n        pooled[rat] = dprime(f.loc[\"FFF\", \"mean\"], f.loc[\"SSS\", \"mean\"], f.loc[\"FFF\", \"size\"], f.loc[\"SSS\", \"size\"])\n        v = []\n        for s, ts in t.groupby(\"session\"):\n            g = ts.groupby(\"stim\").chosen.agg([\"mean\", \"size\"])\n            if {\"FFF\", \"SSS\"} <= set(g.index):\n                v.append(dprime(g.loc[\"FFF\", \"mean\"], g.loc[\"SSS\", \"mean\"], g.loc[\"FFF\", \"size\"], g.loc[\"SSS\", \"size\"]))\n        persess[rat] = np.mean(v)\n    dp = pd.DataFrame(dict(pooled=pooled, session_mean=persess))\n    print(\"reading\", rd); print(dp.round(3))\n    print(\"  pooled: range %.2f to %.2f; session mean: range %.2f to %.2f\" % (dp.pooled.min(), dp.pooled.max(), dp.session_mean.min(), dp.session_mean.max()))\ndp8 = dprime(paper2b.FFF, paper2b.SSS, 1e9, 1e9)\nprint(\"Variant: d-prime from the S1 Data means of all eight rats (mean of sessions, not pooled):\", dp8.round(2).to_dict())\n\n# %% [markdown]\n# ### fig3-fsfs-sffs-intensity-only (S1 Data, Figure 3)\n#\n# > Two rats discriminated FSFS from SFFS when the sequences differed in mean speed (70 and 69.2%\n# > correct) but not when mean speed was the same (52 and 53%), even after more than 20 days;\n# > d-prime was 1.02 against 0.12.\n\n# %% tags=claim:fig3-fsfs-sffs-intensity-only\nf3 = S1[\"Fig 3\"]\nprint(\"columns:\", f3.iloc[2, 2:6].tolist(), f3.iloc[3, 2:6].tolist())\nvals = f3.iloc[4:55, 1:6].apply(pd.to_numeric, errors=\"coerce\")\nvals.columns = [\"day\", \"58B same\", \"58B diff\", \"60W same\", \"60W diff\"]\nsumm = pd.DataFrame({c: dict(sessions=vals[c].notna().sum(), mean_pct=100 * vals[c].mean(),\n                             sem_pct=100 * vals[c].std() / np.sqrt(vals[c].notna().sum()), last_day=vals.day[vals[c].notna()].max())\n                     for c in vals.columns[1:]}).T\nprint(summ.round(2))\ndpr = f3.iloc[59:62, 0:5]\nprint(dpr.to_string())\ndd = pd.to_numeric(dpr.iloc[1, [1, 3]]).values\nds = pd.to_numeric(dpr.iloc[2, [1, 3]]).values\nprint(\"d-prime different intensity: mean of rats %.3f (60W %.3f, 58B %.3f)\" % (dd.mean(), dd[0], dd[1]))\nprint(\"d-prime same intensity: mean of rats %.3f (60W %.3f, 58B %.3f)\" % (ds.mean(), ds[0], ds[1]))\n\n# %% [markdown]\n# ## Units\n#\n# ### units-recorded\n#\n# > The recordings yielded 306 single units and 167 multi-unit clusters (473 units) over 80\n# > sessions in five rats, 3.8 single units per session on average (range 0 to 11).\n\n# %% tags=claim:units-recorded\nsu = U.type.str.startswith(\"SU\")\nper = U[su].groupby(\"session\").size().reindex(range(len(D.A)), fill_value=0)\nprint(\"single units %d (RS %d, FS %d), multi-unit clusters %d, total %d\" % (su.sum(), (U.type == \"SU_RS\").sum(), (U.type == \"SU_FS\").sum(), (~su).sum(), len(U)))\nprint(\"sessions %d, rats %d\" % (len(D.A), U.rat.nunique()))\nprint(\"single units per session: mean %.2f, min %d, max %d\" % (per.mean(), per.min(), per.max()))\nprint(U.groupby([\"rat\", \"type\"]).size().unstack())\nprint(\"\\nby electrode (18FB and 18Ri have a fifth electrode; leaving it out does not give 473):\")\nprint(pd.crosstab(U.elect, U.type, margins=True))\n\n# %% [markdown]\n# ### baseline-rates\n#\n# > Mean firing rate in the 25-ms prestimulus baseline in the nose poke was 6 to 10 Hz across\n# > layers for RS units, 8 to 32 Hz for FS units, and higher for multi-unit clusters.\n\n# %% tags=claim:baseline-rates\nU[\"base25\"] = [ssc4.rate(D.unit_trials(u)[0], -25, 0).mean() for u in U.uid]\nU[\"base25_all\"] = [ssc4.rate(D.unit_trials(u, lambda t: np.ones(len(t), bool))[0], -25, 0).mean() for u in U.uid]\norder = [\"L2/3\", \"L4\", \"L5a\", \"L5b\", \"L6\"]\nbl = U.groupby([\"layer\", \"type\"]).base25.agg([\"mean\", \"size\"]).unstack().loc[order]\nprint(bl.round(2))\nfor ty in [\"SU_RS\", \"SU_FS\"]:\n    m = bl[(\"mean\", ty)]\n    print(\"%s: lowest layer mean %.2f Hz (%s), highest %.2f Hz (%s)\" % (ty, m.min(), m.idxmin(), m.max(), m.idxmax()))\nmu = bl[(\"mean\", \"MU\")]\nprint(\"MU higher than RS in %d of 5 layers; higher than RS and FS in %d of 5\" % ((mu > bl[(\"mean\", \"SU_RS\")]).sum(),\n      ((mu > bl[(\"mean\", \"SU_RS\")]) & (mu > bl[(\"mean\", \"SU_FS\")])).sum()))\nprint(\"\\nVariant, all trials (not only completed):\")\nprint(U.groupby([\"layer\", \"type\"]).base25_all.mean().unstack().loc[order].round(2))\n\n# %% [markdown]\n# ### temporal-modulation-count\n#\n# > 305 of 473 units (63.5%) had firing rates significantly modulated in time during the nose poke period.\n#\n# Readings of the window: (a) 0 to 180 ms after nose poke entry, (b) 0 to 180 ms after stimulus\n# onset. The two statistics the claim names give the same p-value under the uniform permutation\n# (helper docstring), so one is run. A third window, -50 to 300 ms after onset, is the one stored\n# with the data set's own p-values (`TempSig.Params`), shown as a variant.\n\n# %% tags=claim:temporal-modulation-count\npv = {\"a: 0-180 after NP entry\": ssc4.temporal_pvals(D, \"np\", seed=1),\n      \"b: 0-180 after onset\": ssc4.temporal_pvals(D, \"stim\", seed=2),\n      \"variant: -50-300 after onset\": ssc4.temporal_pvals(D, \"deposit\", seed=3)}\ndepmod = U.dep_temp_p.values < 0.05\nfor k, p in pv.items():\n    m = p < 0.05\n    print(\"%-30s modulated %d of %d (%.1f%%); agrees with the deposited p < 0.05 on %d units (%.1f%%)\" %\n          (k, m.sum(), len(m), 100 * m.mean(), (m == depmod).sum(), 100 * np.mean(m == depmod)))\nprint(\"deposited TemporalPval < 0.05: %d of %d (%.1f%%)\" % (depmod.sum(), len(U), 100 * depmod.mean()))\nU[\"mod\"] = pv[\"a: 0-180 after NP entry\"] < 0.05\nfor thr in [0.01, 0.05, 0.1]:\n    print(\"threshold %.2f: reading a %d, reading b %d\" % (thr, (pv[\"a: 0-180 after NP entry\"] < thr).sum(), (pv[\"b: 0-180 after onset\"] < thr).sum()))\nprint(\"\\nby rat, reading a\"); print(U.groupby(\"rat\")[\"mod\"].agg([\"sum\", \"size\"]))\n\n# %% [markdown]\n# The units used from here on are the reading (a) set: the Methods' window (\"0-180 ms after NP\n# entry\"), the reading that fits the count. This is a choice between the claim's readings for the\n# claims that depend on this one; the deposited labels are shown as a variant where they bear.\n\n# %% [markdown]\n# ### modulated-higher-baseline\n#\n# > Temporally modulated units were distributed uniformly across columns and layers and had higher\n# > baseline firing rates than non-modulated units.\n\n# %% tags=claim:modulated-higher-baseline\nrs = U[U.type == \"SU_RS\"]\ntab = rs.groupby([\"layer\", \"mod\"]).base25.agg([\"mean\", \"sem\", \"size\"]).unstack().loc[order]\nprint(tab.round(2))\nhi = (tab[(\"mean\", True)] > tab[(\"mean\", False)])\nprint(\"modulated RS mean higher in %d of 5 layers\" % hi.sum())\nct = pd.crosstab(U.layer, U[\"mod\"]).loc[order]\nprint(ct.assign(frac=ct[True] / ct.sum(1)).round(3))\nprint(\"chi-square layer x modulation (all units): p = %.3f\" % chi2_contingency(ct.values)[1])\nprint(\"columns cannot be tested: the column of each electrode (MapPosition) is not in the data set\")\n\n# %% [markdown]\n# ### fig4d-evoked-modulation-by-layer\n#\n# > The mean impulse-evoked firing rate modulation, above the pre-impulse baseline, was 14.2 Hz in\n# > L2/3, 15.2 in L4, 6.3 in L5a, 14.4 in L5b and 7.0 in L6, greatest in L2/3, L4 and L5b.\n\n# %% tags=claim:fig4d-evoked-modulation-by-layer\nmodu = U[U[\"mod\"]].uid.values\nev = {}\nfor u in modu:\n    segs = ssc4.impulse_segments(D, u)\n    ev[u] = dict(pooled=ssc4.evoked_peak(segs, True), each=ssc4.evoked_peak(segs, False))\nrows = []\nfor u in modu:\n    for pool in [\"pooled\", \"each\"]:\n        pk, mn, lat = ev[u][pool]\n        rows.append(dict(uid=u, layer=U.layer[u], pool=pool, A_signed=pk, A_abs=abs(pk), B_mean=mn))\nEV = pd.DataFrame(rows)\nexpect = pd.Series({\"L2/3\": 14.2, \"L4\": 15.2, \"L5a\": 6.3, \"L5b\": 14.4, \"L6\": 7.0})\ntol = pd.Series({\"L2/3\": 2.3, \"L4\": 1.9, \"L5a\": 1.2, \"L5b\": 2.3, \"L6\": 1.5})\nres = {}\nfor pool in [\"pooled\", \"each\"]:\n    for meas in [\"A_signed\", \"A_abs\", \"B_mean\"]:\n        g = EV[EV.pool == pool].groupby(\"layer\")[meas]\n        res[(meas, pool)] = g.mean().loc[order]\nR = pd.DataFrame(res).T\nR[\"within_all\"] = [(np.abs(R.loc[i, order] - expect) <= tol).all() for i in R.index]\nR[\"n_within\"] = [(np.abs(R.loc[i, order] - expect) <= tol).sum() for i in R.index]\nR[\"L5a_L6_lowest\"] = [set(R.loc[i, order].astype(float).nsmallest(2).index) == {\"L5a\", \"L6\"} for i in R.index]\nprint(\"expected\", expect.to_dict())\nprint(R.round(2).to_string())\nprint(\"units per layer\", EV[EV.pool == \"pooled\"].groupby(\"layer\").size().loc[order].to_dict())\nprint(\"SEM across units, A_signed pooled:\", EV[EV.pool == \"pooled\"].groupby(\"layer\").A_signed.sem().loc[order].round(2).to_dict())\nprint(\"\\nVariant, units modulated by the deposited p-values:\")\ndm = EV[EV.uid.isin(U.uid[depmod])]\nprint(dm[dm.pool == \"pooled\"].groupby(\"layer\")[[\"A_signed\", \"A_abs\", \"B_mean\"]].mean().loc[order].round(2).T)\nprint(\"units per layer\", U[depmod].groupby(\"layer\").size().loc[order].to_dict())\n\n# %% [markdown]\n# ### latency-by-layer\n#\n# > Among impulse-responsive units, peak response latency was shortest in L4, L5a and L5b (9.8,\n# > 10.3 and 12.0 ms) and longest in L2/3 and L6 (13.8 and 16.1 ms).\n\n# %% tags=claim:latency-by-layer\nlt = []\nfor u in modu:\n    segs = ssc4.impulse_segments(D, u)\n    tt, p2, p1 = ssc4.impulse_ttest(segs)\n    lt.append(dict(uid=u, layer=U.layer[u], lat=ev[u][\"pooled\"][2], p_one=p1, p_two=p2))\nLT = pd.DataFrame(lt)\nlexp = pd.Series({\"L4\": 9.8, \"L5a\": 10.3, \"L5b\": 12.0, \"L2/3\": 13.8, \"L6\": 16.1})\nrows = {}\nfor test in [\"p_one\", \"p_two\"]:\n    r = LT[LT[test] < 0.05]\n    for summ in [\"mean\", \"median\"]:\n        rows[(test, summ)] = r.groupby(\"layer\").lat.agg(summ).loc[order]\n    rows[(test, \"n\")] = r.groupby(\"layer\").size().loc[order]\nL = pd.DataFrame(rows).T\nprint(\"expected\", lexp.loc[order].to_dict(), \"tolerance 10%\")\nprint(L.round(2).to_string())\nfor k in [(\"p_one\", \"mean\"), (\"p_one\", \"median\"), (\"p_two\", \"mean\"), (\"p_two\", \"median\")]:\n    v = L.loc[k, order].astype(float)\n    within = (np.abs(v - lexp.loc[order]) <= 0.1 * lexp.loc[order])\n    ordered = max(v[[\"L4\", \"L5a\", \"L5b\"]]) < min(v[[\"L2/3\", \"L6\"]])\n    print(k, \"within tolerance:\", within.sum(), \"of 5;\", \"ordering L4, L5a, L5b below L2/3, L6:\", ordered)\n\n# %% [markdown]\n# ### fig4d-gradual-decrease\n#\n# > Superimposed on the phasic impulse responses, average firing rate decreased gradually during\n# > the nose poke period in all layers except L5a.\n\n# %% tags=claim:fig4d-gradual-decrease\ndef unit_psth(u, a=-25, b=180, sel=None):\n    M, t, _ = D.unit_trials(u, sel)\n    return M[:, a - ssc4.T0:b - ssc4.T0].mean(0) * 1000\ntax = np.arange(-25, 180)\nrows = []\nfor lay in order:\n    us = U[U[\"mod\"] & (U.layer == lay)].uid\n    pop = np.mean([unit_psth(u) for u in us], 0)\n    slope = stats.linregress(tax, pop)\n    rows.append(dict(layer=lay, n=len(us), slope_hz_per_100ms=100 * slope.slope, slope_p=slope.pvalue,\n                     baseline=pop[:25].mean(), last30=pop[-30:].mean(), last30_minus_base=pop[-30:].mean() - pop[:25].mean()))\nGD = pd.DataFrame(rows).set_index(\"layer\")\nGD[\"decrease_a\"] = GD.slope_hz_per_100ms < 0\nGD[\"decrease_b\"] = GD.last30_minus_base < 0\nprint(GD.round(3))\n\n# %% [markdown]\n# ## Regression and unit classes (Figure 6)\n#\n# ### fig6-regression-significant\n#\n# > Of the 305 temporally modulated units, 204 had a significant regression of firing rate on\n# > integrated panel speed for at least one of the 36 integration windows.\n\n# %% tags=claim:fig6-regression-significant\nsig = (P < 0.05 / 36).any(1)\nmod = U[\"mod\"].values\nprint(\"significant regression among modulated units (reading a set): %d of %d\" % ((sig & mod).sum(), mod.sum()))\nprint(\"among units modulated by the deposited p-values: %d of %d\" % ((sig & depmod).sum(), depmod.sum()))\nprint(\"among all units: %d of %d\" % (sig.sum(), len(sig)))\nR2r, Pr, Br = ssc4.regress_all(D, use_rate=True)\nsigr = (Pr < 0.05 / 36).any(1)\nprint(\"variant, rate per trial instead of summed counts: %d of %d modulated\" % ((sigr & mod).sum(), mod.sum()))\nprint(\"by rat:\"); print(pd.Series(sig & mod).groupby(U.rat).sum())\n\n# %% [markdown]\n# ### fig6e-unit-classes\n#\n# > Units were classed by best-fit integration window as Fast (5 to 20 ms, 158 units, 52%, positive\n# > slopes), Medium (25 to 55 ms, 52 units, largely negative slopes), Slow Positive (51) and Slow\n# > Negative (44); 44% of units had very fast (5 to 10 ms) windows.\n\n# %% tags=claim:fig6e-unit-classes\ncls = {}\nrows = []\nexp6 = dict(Fast=158, Medium=52, SlowPos=51, SlowNeg=44)\nfor which in [\"all\", \"sig\"]:\n    for m55 in [False, True]:\n        lab, best, slope, sg = ssc4.unit_classes(R2, P, B, mod, which, m55)\n        key = \"%s, 55 ms %s\" % (\"a all modulated\" if which == \"all\" else \"b significant only\", \"Medium\" if m55 else \"Slow\")\n        cls[key] = lab\n        c = collections.Counter(lab)\n        fast = lab == \"Fast\"\n        med = lab == \"Medium\"\n        row = dict(reading=key, **{k: c[k] for k in exp6})\n        row[\"pct_fast_of_mod\"] = 100 * fast.sum() / mod.sum()\n        row[\"pct_5_10_of_mod\"] = 100 * ((best <= 10) & (lab != \"none\")).sum() / mod.sum()\n        row[\"fast_pos_frac\"] = np.mean(slope[fast] > 0)\n        row[\"medium_neg_frac\"] = np.mean(slope[med] < 0)\n        row[\"counts_within\"] = all(abs(c[k] - v) <= 0.1 * v for k, v in exp6.items())\n        row[\"pcts_within\"] = abs(row[\"pct_fast_of_mod\"] - 52) <= 5.2 and abs(row[\"pct_5_10_of_mod\"] - 44) <= 4.4\n        rows.append(row)\nC6 = pd.DataFrame(rows).set_index(\"reading\")\nprint(C6.round(3).to_string())\ndepc = ssc4.deposited_classes(D)\nprint(\"\\ndeposited labels (Fast/Medium split at 20 ms by PeakBin):\", collections.Counter(depc))\nlab_main = cls[\"a all modulated, 55 ms Slow\"]\nprint(\"agreement of reading (a, 55 Slow) with the deposited classes, over units modulated in both:\",\n      \"%.3f\" % np.mean(lab_main[mod & depmod] == depc[mod & depmod]))\nprint(pd.crosstab(pd.Series(lab_main, name=\"this attempt\"), pd.Series(depc, name=\"deposited\")))\n\n# %% [markdown]\n# Downstream claims use the classes of reading (a) with 55 ms Slow: the four counts the paper\n# reports sum to 305, all temporally modulated units, and the Figure 6D legend puts Fast and Medium\n# below 55 ms. The deposited labels are shown as a variant.\n\n# %% [markdown]\n# ### fig6fg-laminar-classes\n#\n# > Fast units were 73% of temporally modulated units in L2/3 and L4, 50% in L5 and 23% in L6;\n# > slow units were 13% in L2/3 and L4, 31% in L5 and 56% in L6.\n\n# %% tags=claim:fig6fg-laminar-classes\ngrp = {\"L2/3\": \"L2/3+L4\", \"L4\": \"L2/3+L4\", \"L5a\": \"L5\", \"L5b\": \"L5\", \"L6\": \"L6\"}\nexpF = {\"L2/3+L4\": 73, \"L5\": 50, \"L6\": 23}\nexpS = {\"L2/3+L4\": 13, \"L5\": 31, \"L6\": 56}\ndef laminar(lab, modmask):\n    d = pd.DataFrame(dict(layer=U.layer, lab=lab))[modmask]\n    out = {}\n    for gname, keyf in [(\"grouped\", lambda l: grp.get(l, \"none\")), (\"separate\", lambda l: l)]:\n        g = d.assign(g=d.layer.map(keyf))\n        f = g.groupby(\"g\").lab.apply(lambda x: 100 * np.mean(x == \"Fast\"))\n        s = g.groupby(\"g\").lab.apply(lambda x: 100 * np.mean(np.isin(x, [\"SlowPos\", \"SlowNeg\"])))\n        out[gname] = pd.DataFrame(dict(fast_pct=f, slow_pct=s, n=g.groupby(\"g\").size()))\n    return out\nfor key, lab in list(cls.items()) + [(\"deposited labels\", depc)]:\n    mm = mod if key != \"deposited labels\" else depmod\n    o = laminar(lab, mm)\n    gr = o[\"grouped\"].loc[[\"L2/3+L4\", \"L5\", \"L6\"]]\n    win = sum(abs(gr.fast_pct[k] - expF[k]) <= 0.1 * expF[k] for k in expF) + sum(abs(gr.slow_pct[k] - expS[k]) <= 0.1 * expS[k] for k in expS)\n    grad = gr.fast_pct.is_monotonic_decreasing and gr.slow_pct.is_monotonic_increasing\n    print(\"\\n\", key, \"| values within tolerance: %d of 6 | gradient holds: %s\" % (win, grad))\n    print(gr.round(1).T.to_string())\n    print(o[\"separate\"].loc[[\"L2/3\", \"L4\"]].round(1).T.to_string())\n\n# %% [markdown]\n# ## Response classes (Figures 7 and 8)\n\n# %%\nU[\"cls\"] = lab_main\nU[\"cls_dep\"] = depc\nU[\"best\"] = (R2.argmax(1) + 1) * 5\nKINDS = [\"F\", \"M\", \"S\"]\n\ndef net_evoked(u, kinds=KINDS):\n    \"\"\"Mean over impulses of each kind (all sequences) of the rate 5-35 ms after onset minus 0-10 ms before.\"\"\"\n    segs = ssc4.impulse_segments(D, u)\n    out = {}\n    for k in kinds:\n        X = np.concatenate([g[\"X\"] for g in segs if g[\"kind\"] == k])\n        out[k] = X[:, 15:45].mean() * 1000 - X[:, 0:10].mean() * 1000\n    return out\n\ndef seq_rates(u, base, sel=None):\n    \"\"\"Per sequence, mean rate 0-150 ms after onset minus the pre-stimulus baseline (base: '25' or '10').\"\"\"\n    M, t, _ = D.unit_trials(u, sel)\n    a = -25 if base == \"25\" else -10\n    out = {}\n    for s in [\"FFF\", \"FMS\", \"SMF\", \"SSS\"]:\n        m = (t.stim == s).values\n        out[s] = ssc4.rate(M[m], 0, 150).mean() - ssc4.rate(M[m], a, 0).mean()\n    return out\n\ndef pulse_evoked(u, base, sel=None):\n    \"\"\"Per sequence and pulse, rate 5-35 ms after the pulse onset minus the pre-sequence baseline (S4 Fig).\"\"\"\n    M, t, _ = D.unit_trials(u, sel)\n    si = int(U.session[u])\n    a = -25 if base == \"25\" else -10\n    out = {}\n    for s in [\"FFF\", \"FMS\", \"SMF\", \"SSS\"]:\n        m = (t.stim == s).values\n        if m.sum() == 0:\n            continue\n        b0 = ssc4.rate(M[m], a, 0).mean()\n        for p, on in enumerate(D.onsets(si, s)):\n            out[(s, p + 1)] = ssc4.rate(M[m], on + 5, on + 35).mean() - b0\n    return out\n\nNE = pd.DataFrame({u: net_evoked(u) for u in U.uid[U.cls != \"none\"]}).T\nSR = {b: pd.DataFrame({u: seq_rates(u, b) for u in U.uid[U.cls != \"none\"]}).T for b in [\"25\", \"10\"]}\nNE_dep = pd.DataFrame({u: net_evoked(u) for u in U.uid[(U.cls_dep != \"none\")]}).T\nSR_dep = {b: pd.DataFrame({u: seq_rates(u, b) for u in U.uid[U.cls_dep != \"none\"]}).T for b in [\"25\", \"10\"]}\nprint(\"class sizes (this attempt):\", U.cls.value_counts().to_dict())\n\n# %% [markdown]\n# ### fig7c-fast-impulse-velocity\n#\n# > In Fast units the evoked rate after an impulse was greater for F than S impulses and\n# > intermediate for M impulses.\n\n# %% tags=claim:fig7c-fast-impulse-velocity\nfor nm, ne, c in [(\"this attempt\", NE, \"cls\"), (\"variant: deposited labels\", NE_dep, \"cls_dep\")]:\n    f = ne.loc[U.uid[U[c] == \"Fast\"]]\n    m = f.mean()\n    t = stats.ttest_rel(f.F, f.S)\n    print(\"%s: n = %d Fast units, net evoked F %.2f, M %.2f, S %.2f Hz (SEM %s); F > M > S: %s; paired t F vs S t = %.2f p = %.2g\"\n          % (nm, len(f), m.F, m.M, m.S, f.sem().round(2).to_dict(), m.F > m.M > m.S, t.statistic, t.pvalue))\nf = NE.loc[U.uid[U.cls == \"Fast\"]]\nprint(\"by rat:\"); print(f.groupby(U.rat).mean().round(2))\n\n# %% [markdown]\n# ### fig7c-fast-sequence-rate\n#\n# > Mean firing rate of Fast units over the whole sequence (0 to 150 ms) followed the mean speed of\n# > the sequence, highest for FFF, lowest for SSS, and intermediate and equal for FMS and SMF.\n\n# %% tags=claim:fig7c-fast-sequence-rate\nfor nm, sr, c in [(\"this attempt\", SR, \"cls\"), (\"variant: deposited labels\", SR_dep, \"cls_dep\")]:\n    for b in [\"25\", \"10\"]:\n        f = sr[b].loc[U.uid[U[c] == \"Fast\"]]\n        m = f.mean()\n        t = stats.ttest_rel(f.FMS, f.SMF)\n        print(\"%s, baseline %s ms: n = %d, FFF %.2f, FMS %.2f, SMF %.2f, SSS %.2f Hz; FFF > FMS,SMF > SSS: %s; FMS vs SMF diff %.2f Hz, t = %.2f, p = %.3f\"\n              % (nm, b, len(f), m.FFF, m.FMS, m.SMF, m.SSS, m.FFF > max(m.FMS, m.SMF) and min(m.FMS, m.SMF) > m.SSS, m.FMS - m.SMF, t.statistic, t.pvalue))\nf = SR[\"25\"].loc[U.uid[U.cls == \"Fast\"]]\nprint(\"by rat (baseline 25 ms):\"); print(f.groupby(U.rat).mean().round(2))\n\n# %% [markdown]\n# ### fig7-fff-adaptation\n#\n# > Fast RS single units adapted modestly in FFF trains, with pulse 2 to pulse 1 ratio 0.80 and\n# > pulse 3 to pulse 1 ratio 0.70, significant by t test.\n#\n# Units: Fast RS single units whose response to F impulses is significant by the impulse t test\n# (one-sided, two-sided). A per-unit ratio is defined only when the unit's pulse 1 response is above\n# 0; units without are counted.\n\n# %% tags=claim:fig7-fff-adaptation\ndef f_responsive(u, side):\n    segs = ssc4.impulse_segments(D, u, kinds=[\"F\"])\n    tt, p2, p1 = ssc4.impulse_ttest(segs)\n    return (p1 if side == \"one\" else p2) < 0.05\ndef adaptation(units, seq, base):\n    pe = pd.DataFrame({u: pulse_evoked(u, base) for u in units}).T\n    p1, p2, p3 = pe[(seq, 1)], pe[(seq, 2)], pe[(seq, 3)]\n    ok = p1 > 0\n    out = {}\n    for n, pn in [(\"2/1\", p2), (\"3/1\", p3)]:\n        ratio = (pn / p1)[ok]\n        out[n] = dict(mean_ratio=ratio.mean(), sem=ratio.sem(), ratio_of_means=pn.mean() / p1.mean(),\n                      p_ratio_vs_1=stats.ttest_1samp(ratio, 1).pvalue, p_paired=stats.ttest_rel(pn, p1).pvalue,\n                      n=len(units), n_ratio=int(ok.sum()))\n    return pd.DataFrame(out).T, pe\nfastrs = {c: U.uid[(U[c] == \"Fast\") & (U.type == \"SU_RS\")].values for c in [\"cls\", \"cls_dep\"]}\nresp = {(c, side): [u for u in fastrs[c] if f_responsive(u, side)] for c in fastrs for side in [\"one\", \"two\"]}\nfor k, v in resp.items():\n    print(k, \"Fast RS single units\", len(fastrs[k[0]]), \"F-responsive\", len(v))\nADAPT = {}\nfor (c, side), units in resp.items():\n    for base in [\"25\", \"10\"]:\n        tab, pe = adaptation(units, \"FFF\", base)\n        ADAPT[(c, side, base)] = pe\n        print(\"\\nFFF, classes %s, %s-sided, baseline %s ms\" % (c, side, base))\n        print(tab.round(3).to_string())\n\n# %% [markdown]\n# ### fig7-sss-no-adaptation\n#\n# > Adaptation was statistically absent in SSS trains (pulse 2/pulse 1 ratio 1.09, pulse 3/pulse 1 ratio 0.86).\n\n# %% tags=claim:fig7-sss-no-adaptation\nfor (c, side), units in resp.items():\n    for base in [\"25\", \"10\"]:\n        tab, _ = adaptation(units, \"SSS\", base)\n        print(\"\\nSSS, classes %s, %s-sided, baseline %s ms\" % (c, side, base))\n        print(tab.round(3).to_string())\n\n# %% [markdown]\n# ### s4-fms-middle-pulse\n#\n# > The middle M pulse appeared weaker in FMS than in SMF sequences in Fast RS single units, but the\n# > difference was not significant.\n\n# %% tags=claim:s4-fms-middle-pulse\nfor (c, side, base), pe in ADAPT.items():\n    a, b = pe[(\"FMS\", 2)], pe[(\"SMF\", 2)]\n    t = stats.ttest_rel(a, b)\n    print(\"classes %s, %s-sided, baseline %s: n = %d, pulse 2 FMS %.2f, SMF %.2f Hz, diff %.2f Hz, paired t = %.2f, p = %.3f\"\n          % (c, side, base, len(a), a.mean(), b.mean(), a.mean() - b.mean(), t.statistic, t.pvalue))\n\n# %% [markdown]\n# ### fig7de-medium-suppressed\n#\n# > Medium units were suppressed by F, M and S impulses and did not distinguish impulse identity or\n# > sequence identity.\n\n# %% tags=claim:fig7de-medium-suppressed\nfor nm, ne, sr, c in [(\"this attempt\", NE, SR, \"cls\"), (\"variant: deposited labels\", NE_dep, SR_dep, \"cls_dep\")]:\n    us = U.uid[U[c] == \"Medium\"]\n    f = ne.loc[us]\n    t1 = stats.ttest_rel(f.F, f.S)\n    print(\"%s: n = %d Medium units; net evoked F %.2f, M %.2f, S %.2f Hz; all negative: %s; F vs S t = %.2f p = %.3f\"\n          % (nm, len(f), f.F.mean(), f.M.mean(), f.S.mean(), (f.mean() < 0).all(), t1.statistic, t1.pvalue))\n    print(\"   one-sample t against 0:\", {k: round(stats.ttest_1samp(f[k], 0).pvalue, 4) for k in KINDS})\n    for b in [\"25\", \"10\"]:\n        s = sr[b].loc[us]\n        t2 = stats.ttest_rel(s.FFF, s.SSS)\n        print(\"   baseline %s: sequence rates %s; FFF vs SSS diff %.2f t = %.2f p = %.3f\" % (b, s.mean().round(2).to_dict(), (s.FFF - s.SSS).mean(), t2.statistic, t2.pvalue))\n\n# %% [markdown]\n# ### fig8a-slow-positive-no-sequence-difference\n#\n# > Slow Positive units showed small, sustained responses mostly to the second and third impulses,\n# > evident for F and M but not S impulses, and their mean firing did not differ between FFF, FMS,\n# > SMF and SSS.\n\n# %% tags=claim:fig8a-slow-positive-no-sequence-difference\ndef rm_anova(Y):\n    \"\"\"One-way repeated-measures ANOVA, Y units x conditions.\"\"\"\n    Y = np.asarray(Y, float)\n    n, k = Y.shape\n    gm = Y.mean()\n    ss_c = n * ((Y.mean(0) - gm) ** 2).sum()\n    ss_s = k * ((Y.mean(1) - gm) ** 2).sum()\n    ss_e = ((Y - gm) ** 2).sum() - ss_c - ss_s\n    F = (ss_c / (k - 1)) / (ss_e / ((n - 1) * (k - 1)))\n    return F, stats.f.sf(F, k - 1, (n - 1) * (k - 1))\nfor nm, ne, sr, c in [(\"this attempt\", NE, SR, \"cls\"), (\"variant: deposited labels\", NE_dep, SR_dep, \"cls_dep\")]:\n    us = U.uid[U[c] == \"SlowPos\"]\n    f = ne.loc[us]\n    tt = {k: stats.ttest_1samp(f[k], 0) for k in KINDS}\n    print(\"%s: n = %d Slow Positive; net evoked %s Hz; one-sample t p: %s\" % (nm, len(f), f.mean().round(2).to_dict(),\n          {k: \"%.3g (t %.2f)\" % (v.pvalue, v.statistic) for k, v in tt.items()}))\n    for b in [\"25\", \"10\"]:\n        s = sr[b].loc[us]\n        F, p = rm_anova(s.values)\n        print(\"   baseline %s: sequence rates %s; RM-ANOVA F = %.2f p = %.3f\" % (b, s.mean().round(2).to_dict(), F, p))\npp = pd.DataFrame({u: pulse_evoked(u, \"25\") for u in U.uid[U.cls == \"SlowPos\"]}).T\nprint(\"pulse-evoked rate above the 25-ms baseline by pulse (mean over Slow Positive units and sequences):\",\n      {p: round(pp[[c for c in pp.columns if c[1] == p]].mean(1).mean(), 2) for p in (1, 2, 3)})\n\n# %% [markdown]\n# ### fig8b-slow-negative-no-impulse-response\n#\n# > Slow Negative units did not respond to impulses, and their firing declined steadily over time.\n\n# %% tags=claim:fig8b-slow-negative-no-impulse-response\nfor nm, ne, c in [(\"this attempt\", NE, \"cls\"), (\"variant: deposited labels\", NE_dep, \"cls_dep\")]:\n    us = U.uid[U[c] == \"SlowNeg\"]\n    f = ne.loc[us]\n    tt = {k: stats.ttest_1samp(f[k], 0) for k in KINDS}\n    pos = [k for k, v in tt.items() if v.statistic > 0 and v.pvalue < 0.05]\n    pop = np.mean([unit_psth(u, 0, 180) for u in us], 0)\n    sl = stats.linregress(np.arange(180), pop)\n    print(\"%s: n = %d Slow Negative; net evoked %s Hz; t (p): %s; significantly positive kinds: %s; PSTH slope 0-180 ms %.2f Hz/100 ms (p = %.2g)\"\n          % (nm, len(f), f.mean().round(2).to_dict(), {k: \"%.2f (%.3g)\" % (v.statistic, v.pvalue) for k, v in tt.items()}, pos, 100 * sl.slope, sl.pvalue))\n\n# %% [markdown]\n# ### fig8d-slow-positive-right-choice-l5\n#\n# > Slow Positive units fired more on right-choice trials (contralateral to the recording) for all\n# > stimuli; right-choice bias, measured 5 to 50 ms after the start of the final impulse, was\n# > significant in L5a and L5b but not in other layers.\n\n# %% tags=claim:fig8d-slow-positive-right-choice-l5\ndef choice_bias(u):\n    \"\"\"Rate 5-50 ms after the third impulse onset, right minus left: (a) all trials pooled, (b) per sequence, averaged.\"\"\"\n    M, t, _ = D.unit_trials(u)\n    si = int(U.session[u])\n    r = np.zeros(len(t))\n    for s in ssc4.STIMS:\n        m = (t.stim == s).values\n        on = D.onsets(si, s)[2]\n        r[m] = ssc4.rate(M[m], on + 5, on + 50)\n    right = t.chosen.values == 1\n    a = (r[right].mean(), r[~right].mean())\n    d = []\n    for s in ssc4.STIMS:\n        m = (t.stim == s).values\n        if (m & right).any() and (m & ~right).any():\n            d.append((r[m & right].mean(), r[m & ~right].mean()))\n    b = tuple(np.mean(d, 0))\n    return a + b\ndef bias_table(cl, c=\"cls\"):\n    us = U.uid[U[c].isin(cl)]\n    cb = pd.DataFrame({u: choice_bias(u) for u in us}, index=[\"aR\", \"aL\", \"bR\", \"bL\"]).T\n    cb[\"layer\"] = U.layer[us].values\n    rows = []\n    for lay in order:\n        g = cb[cb.layer == lay]\n        row = dict(layer=lay, n=len(g))\n        for rd in \"ab\":\n            if len(g) > 1:\n                t = stats.ttest_rel(g[rd + \"R\"], g[rd + \"L\"])\n                row.update({rd + \"_diff\": (g[rd + \"R\"] - g[rd + \"L\"]).mean(), rd + \"_t\": t.statistic, rd + \"_p\": t.pvalue})\n        rows.append(row)\n    return pd.DataFrame(rows).set_index(\"layer\")\nfor nm, c in [(\"this attempt\", \"cls\"), (\"variant: deposited labels\", \"cls_dep\")]:\n    bt8 = bias_table([\"SlowPos\"], c)\n    print(nm, \"Slow Positive\"); print(bt8.round(4).to_string())\n    for rd in \"ab\":\n        ok = (bt8.loc[[\"L5a\", \"L5b\"], rd + \"_p\"] < 0.05).all() and (bt8.loc[[\"L5a\", \"L5b\"], rd + \"_diff\"] > 0).all() and \\\n             not (bt8.loc[[\"L2/3\", \"L4\", \"L6\"], rd + \"_p\"] < 0.05).any()\n        print(\"  reading %s: L5a and L5b significant with right higher, other layers not: %s\" % (rd, ok))\nprint(\"\\nVariant (not judged): Fast and Medium units by layer\")\nprint(bias_table([\"Fast\", \"Medium\"]).round(4).to_string())\nprint(\"paper's starred p-values: 0.022, 9.5e-4, 7.5e-5\")\n\n# %% [markdown]\n# ### fig8e-choice-divergence-125ms\n#\n# > In L5 Slow Positive units, firing on right- and left-choice trials diverged after the second\n# > impulse and was consistently significant by 125 ms, before the earliest withdrawals (150 ms) and\n# > the mean withdrawal time (190 ms).\n#\n# Per unit the PSTH for each choice is the mean of its per-sequence PSTHs (sequences with trials of\n# that choice). \"Lasts to the end of the third impulse\" is taken as lasting to 150 ms, the end of\n# the 0-150 ms sequence window of the paper, a standard choice; 140 and 160 ms are shown too.\n\n# %% tags=claim:fig8e-choice-divergence-125ms\ndef choice_psth(u, a=-50, b=250):\n    M, t, _ = D.unit_trials(u)\n    out = {}\n    for c in (1, 0):\n        ps = [M[((t.stim == s) & (t.chosen == c)).values, a - ssc4.T0:b - ssc4.T0].mean(0) * 1000\n              for s in ssc4.STIMS if ((t.stim == s) & (t.chosen == c)).any()]\n        out[c] = np.mean(ps, 0)\n    return out\nTAX = np.arange(-50, 250)\ndef sliding(us, reading):\n    R = np.array([choice_psth(u)[1] for u in us])\n    L = np.array([choice_psth(u)[0] for u in us])\n    if reading == \"a\":    # 10-ms windows stepped by 1 ms, centred\n        k = np.ones(10) / 10\n        R = np.array([np.convolve(r, k, \"same\") for r in R]); L = np.array([np.convolve(r, k, \"same\") for r in L])\n        t = TAX\n    else:                 # 5-ms bins\n        R = R.reshape(len(us), -1, 5).mean(2); L = L.reshape(len(us), -1, 5).mean(2)\n        t = TAX[::5]\n    tt = stats.ttest_rel(R, L, axis=0)\n    return t, tt.pvalue, (R - L).mean(0)\ndef onset_of_run(t, p, end):\n    s = p < 0.05\n    m = t <= end\n    for i in np.where(m & s)[0]:\n        if s[i:np.searchsorted(t, end, \"right\")].all():\n            return t[i]\n    return np.nan\nfor nm, c in [(\"this attempt\", \"cls\"), (\"variant: deposited labels\", \"cls_dep\")]:\n    us = U.uid[(U[c] == \"SlowPos\") & U.layer.isin([\"L5a\", \"L5b\"])].values\n    for rd in \"ab\":\n        t, p, d = sliding(us, rd)\n        ons = {end: onset_of_run(t, p, end) for end in (140, 150, 160)}\n        first = t[(p < 0.05) & (t >= 0)]\n        print(\"%s, reading %s: n = %d L5 Slow Positive; onset of the run lasting to 140/150/160 ms: %s; first significant time after 0: %s\"\n              % (nm, rd, len(us), ons, first[0] if len(first) else None))\nus = U.uid[(U.cls == \"SlowPos\") & U.layer.isin([\"L5a\", \"L5b\"])].values\ntr = pd.concat([D.unit_trials(u)[1].assign(session=int(U.session[u])) for u in us]).drop_duplicates([\"session\", \"trial\"])\nprint(\"withdrawal after onset over the %d trials of these units' sessions: min %.0f, 1st percentile %.1f, mean %.1f ms\"\n      % (len(tr), tr.withdraw_t.min(), np.percentile(tr.withdraw_t, 1), tr.withdraw_t.mean()))\nt, p, d = sliding(us, \"a\")\nprint(\"right minus left (Hz), 10-ms windows, at 50/75/100/125/150 ms:\", {x: round(float(d[TAX == x][0]), 2) for x in (50, 75, 100, 125, 150)})\n\n# %% [markdown]\n# ### fig8d-fast-medium-no-choice-bias\n#\n# > Choice-related activity was absent in L4 Fast units.\n\n# %% tags=claim:fig8d-fast-medium-no-choice-bias\nfor nm, c in [(\"this attempt\", \"cls\"), (\"variant: deposited labels\", \"cls_dep\")]:\n    us = U.uid[(U[c] == \"Fast\") & (U.layer == \"L4\")].values\n    for rd in \"ab\":\n        t, p, d = sliding(us, rd)\n        m = (t >= 0) & (t <= 150)\n        sigt = t[m & (p < 0.05)]\n        print(\"%s, reading %s: n = %d L4 Fast; significant times 0-150 ms: %d (%s); run lasting to 150 ms from: %s; largest |R-L| 0-150 ms %.2f Hz\"\n              % (nm, rd, len(us), len(sigt), sigt[:20].tolist(), onset_of_run(t, p, 150), np.abs(d[m]).max()))\nprint(\"\\nVariant: Fast and Medium right-choice bias by layer is printed under fig8d-slow-positive-right-choice-l5.\")\n\n# %% [markdown]\n# ### s5-slow-positive-no-integration\n#\n# > Within right- or left-choice trials, L5 Slow Positive units fired little to pulses 1 and 2, and\n# > their pulse 3 firing was the same for FFF, FMS, SMF and SSS and did not correlate with mean\n# > speed of the sequence or of the last two impulses.\n#\n# Impulse mean speed is taken from Table 1 as twice the peak amplitude over the duration (a ramp\n# out and back): F 2 x 1.03/16, M 2 x 1.15/22, S 2 x 1.14/28 mm/ms.\n\n# %% tags=claim:s5-slow-positive-no-integration\nimp_speed = {\"F\": 2 * 1.03 / 16 * 1000, \"M\": 2 * 1.15 / 22 * 1000, \"S\": 2 * 1.14 / 28 * 1000}\nfor nm, c in [(\"this attempt\", \"cls\"), (\"variant: deposited labels\", \"cls_dep\")]:\n    us = U.uid[(U[c] == \"SlowPos\") & U.layer.isin([\"L5a\", \"L5b\"])].values\n    for ch, chn in [(1, \"right\"), (0, \"left\")]:\n        for base in [\"25\", \"10\"]:\n            pe = pd.DataFrame({u: pulse_evoked(u, base, lambda t, ch=ch: (t.complete & (t.chosen == ch)).values) for u in us}).T\n            p3 = pe[[(s, 3) for s in [\"FFF\", \"FMS\", \"SMF\", \"SSS\"]]].dropna()\n            F, p = rm_anova(p3.values)\n            pop = p3.mean()\n            seqs = [\"FFF\", \"FMS\", \"SMF\", \"SSS\"]\n            r1 = stats.pearsonr([ssc4.MEAN_SPEED[s] for s in seqs], pop.values)\n            r2 = stats.pearsonr([(imp_speed[s[1]] + imp_speed[s[2]]) / 2 for s in seqs], pop.values)\n            r3 = stats.pearsonr([(imp_speed[s[0]] + imp_speed[s[1]]) / 2 for s in seqs], pop.values)\n            p12 = pe[[c2 for c2 in pe.columns if c2[1] in (1, 2)]].mean().mean()\n            print(\"%s, %s choice, baseline %s: n = %d; pulse 1-2 mean %.2f Hz; pulse 3 %s; RM-ANOVA F = %.2f p = %.3f; r(seq speed) = %.2f p = %.2f; r(pulses 2,3) = %.2f p = %.2f; r(pulses 1,2) = %.2f p = %.2f\"\n                  % (nm, chn, base, len(p3), p12, pop.round(2).to_dict(), F, p, r1[0], r1[1], r2[0], r2[1], r3[0], r3[1]))\n\n# %% [markdown]\n# ### s6-head-position-choice (S2 Data, S6 Fig)\n#\n# > In high-speed video of 43 trials, head angle and whisker tip trajectories did not differ between\n# > right- and left-choice trials, while head position differed modestly from 100 ms, by 0.6 mm at\n# > 125 ms.\n#\n# S2 Data gives the mean and SEM per frame for 22 left- and 21 right-choice trials, so the t tests\n# are computed from those summaries.\n\n# %% tags=claim:s6-head-position-choice\ns6 = S2[\"Fig S6\"]\ncols = s6.iloc[3, :].tolist()\nleft = pd.DataFrame(s6.iloc[4:23].values.astype(float), columns=cols)\nright = pd.DataFrame(s6.iloc[26:45].values.astype(float), columns=cols)\nnL, nR = 22, 21\nout = {\"time\": left[\"Time (ms)\"].values}\nfor v in [\"Head Angle\", \"W Lat\", \"W RC\", \"Head dx\", \"Head dy\"]:\n    mL, sL = left[[c for c in cols if c.startswith(v) and \"mean\" in c][0]], left[[c for c in cols if c.startswith(v) and \"sem\" in c.replace(\"  \", \" \")][0]]\n    mR, sR = right[[c for c in cols if c.startswith(v) and \"mean\" in c][0]], right[[c for c in cols if c.startswith(v) and \"sem\" in c.replace(\"  \", \" \")][0]]\n    sdL, sdR = sL * np.sqrt(nL), sR * np.sqrt(nR)\n    w = stats.ttest_ind_from_stats(mR, sdR, nR, mL, sdL, nL, equal_var=False)\n    s = stats.ttest_ind_from_stats(mR, sdR, nR, mL, sdL, nL, equal_var=True)\n    out[v + \" R-L\"] = (mR - mL).values\n    out[v + \" p_welch\"] = w.pvalue\n    out[v + \" p_student\"] = s.pvalue\nS6 = pd.DataFrame(out)\nprint(S6.round(3).to_string())\nfor v in [\"Head Angle\", \"W Lat\", \"W RC\", \"Head dx\", \"Head dy\"]:\n    for k in [\"p_welch\", \"p_student\"]:\n        sigt = S6.time[S6[v + \" \" + k] < 0.05].tolist()\n        print(\"%s %s: frames with p < 0.05: %s\" % (v, k, sigt))\ni = int(np.argmin(np.abs(S6.time - 125)))\nprint(\"at %.1f ms: head dx right minus left %.3f mm, head dy %.3f mm\" % (S6.time[i], S6[\"Head dx R-L\"][i], S6[\"Head dy R-L\"][i]))\n\n# %% [markdown]\n# ### s7-no-fs-l5-slow-positive\n#\n# > All four response classes (Fast, Medium, Slow Positive, Slow Negative) included RS single units,\n# > FS single units and multi-unit clusters; few FS units were in the Slow classes and none among L5\n# > Slow Positive units.\n\n# %% tags=claim:s7-no-fs-l5-slow-positive\nfor nm, c in [(\"this attempt\", \"cls\"), (\"variant: deposited labels\", \"cls_dep\")]:\n    ct = pd.crosstab(U[c], U.type).drop(\"none\")\n    ct[\"FS_frac\"] = ct.SU_FS / ct[[\"MU\", \"SU_FS\", \"SU_RS\"]].sum(1)\n    print(nm); print(ct.round(3))\n    l5sp = U[(U[c] == \"SlowPos\") & U.layer.isin([\"L5a\", \"L5b\"])].type.value_counts().to_dict()\n    print(\"  L5 Slow Positive by type:\", l5sp)\n    print(\"  every class holds all three types:\", bool((ct[[\"MU\", \"SU_FS\", \"SU_RS\"]] > 0).all().all()),\n          \"| FS fraction of each Slow class below Fast:\", bool((ct.loc[[\"SlowPos\", \"SlowNeg\"], \"FS_frac\"] < ct.loc[\"Fast\", \"FS_frac\"]).all()))\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb1.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
date -u; cd entries/mcguire-2016 && . $TMPDIR/dev/bin/activate && time python $TMPDIR/nb1.py > $TMPDIR/nb1.out 2>&1; tail -5 $TMPDIR/nb1.out; wc -l $TMPDIR/nb1.out
```

```
Wed Nov 11 17:14:41 UTC 2026

real	0m2.705s
user	0m3.018s
sys	0m0.211s
Traceback (most recent call last):
  File "/tmp/claude-1001/nb1.py", line 64, in <module>
    import ssc4
ModuleNotFoundError: No module named 'ssc4'
4 /tmp/claude-1001/nb1.out
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && time PYTHONPATH=. python $TMPDIR/nb1.py > $TMPDIR/nb1.out 2>&1; tail -5 $TMPDIR/nb1.out; wc -l $TMPDIR/nb1.out
```

```
real	0m25.793s
user	0m22.229s
sys	0m0.596s
Traceback (most recent call last):
  File "/tmp/claude-1001/nb1.py", line 317, in <module>
    print("Variant: d-prime from the S1 Data means of all eight rats (mean of sessions, not pooled):", dp8.round(2).to_dict())
                                                                                                       ^^^^^^^^^^^^^^^^^^^^
AttributeError: 'numpy.ndarray' object has no attribute 'to_dict'. Did you mean: 'to_device'?
217 /tmp/claude-1001/nb1.out
```

**Agent calls Bash**

```bash
sed -i 's/^dp8 = dprime(paper2b.FFF, paper2b.SSS, 1e9, 1e9)/dp8 = pd.Series(dprime(paper2b.FFF.values, paper2b.SSS.values, 1e9, 1e9), index=paper2b.index)/' $TMPDIR/nb1.py && . $TMPDIR/dev/bin/activate && time PYTHONPATH=. python $TMPDIR/nb1.py > $TMPDIR/nb1.out 2>&1; tail -5 $TMPDIR/nb1.out; wc -l $TMPDIR/nb1.out
```

```
real	1m37.800s
user	1m34.596s
sys	0m0.616s
Medium   20      7     26    0.132
SlowNeg  21      2     23    0.043
SlowPos  12      7     32    0.137
  L5 Slow Positive by type: {'SU_RS': 14, 'MU': 7}
  every class holds all three types: True | FS fraction of each Slow class below Fast: True
652 /tmp/claude-1001/nb1.out
```

**Agent**

Notebook 1 code runs end to end in about 1.6 min. Reading the outputs.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb1.out"
}
```

```
1	/tmp/claude-1001/nb1.py:240: Pandas4Warning: Starting with pandas version 4.0 all arguments of min will be keyword-only.
2	  int(((paper2b[["FMS", "SMF"]].min(1) > paper2b.SSS) & (paper2b[["FMS", "SMF"]].max(1) < paper2b.FFF)).sum()), "of 8")
3	/tmp/claude-1001/nb1.py:240: Pandas4Warning: Starting with pandas version 4.0 all arguments of max will be keyword-only.
4	  int(((paper2b[["FMS", "SMF"]].min(1) > paper2b.SSS) & (paper2b[["FMS", "SMF"]].max(1) < paper2b.FFF)).sum()), "of 8")
5	/tmp/claude-1001/nb1.py:263: Pandas4Warning: Starting with pandas version 4.0 all arguments of mean will be keyword-only.
6	  rel = fr.sub(fr.mean(1), axis=0)
7	/tmp/claude-1001/nb1.py:265: Pandas4Warning: Starting with pandas version 4.0 all arguments of max will be keyword-only.
8	  order_a=(rel.FFF > rel[["FMS", "SMF"]].max(1)) & (rel[["FMS", "SMF"]].min(1) > rel.SSS),
9	/tmp/claude-1001/nb1.py:265: Pandas4Warning: Starting with pandas version 4.0 all arguments of min will be keyword-only.
10	  order_a=(rel.FFF > rel[["FMS", "SMF"]].max(1)) & (rel[["FMS", "SMF"]].min(1) > rel.SSS),
11	/tmp/claude-1001/nb1.py:263: Pandas4Warning: Starting with pandas version 4.0 all arguments of mean will be keyword-only.
12	  rel = fr.sub(fr.mean(1), axis=0)
13	/tmp/claude-1001/nb1.py:265: Pandas4Warning: Starting with pandas version 4.0 all arguments of max will be keyword-only.
14	  order_a=(rel.FFF > rel[["FMS", "SMF"]].max(1)) & (rel[["FMS", "SMF"]].min(1) > rel.SSS),
15	/tmp/claude-1001/nb1.py:265: Pandas4Warning: Starting with pandas version 4.0 all arguments of min will be keyword-only.
16	  order_a=(rel.FFF > rel[["FMS", "SMF"]].max(1)) & (rel[["FMS", "SMF"]].min(1) > rel.SSS),
17	a929b803ca0feab5270e807f571d13eb  AllRats.mat
18	5302f4f1dd7055fc72484b6ea7dab402  docs/crcns_ssc-4_data_description.docx
19	71ab6b260e031c252a2af1db85c5b620  docs/crcns_ssc-4_data_description.pdf
20	b8c483faa24ce741b46372230f86bc43  filelist.txt
[... 633 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='nb1.py'; s=open(p).read()
s=s.replace('''X0 = np.array([np.asarray(np.atleast_2d(D.A[0].StimReg)[0][w].Xval)[:, 1] for w in range(36)])
dx = max(np.abs(np.array([np.asarray(np.atleast_2d(D.A[r.session].StimReg)[r.unit][w].Xval)[:, 1] for w in range(36)]) - X0).max()
         for r in U.itertuples())
print("largest difference of Xval from the first unit's, over all units:", dx)''','''tset = {si: str([D.stimtimes[si][k][:, 0].tolist() for k in range(4)]) for si in range(len(D.A))}
X0 = {}
dx = collections.defaultdict(float)
for r in U.itertuples():
    x = np.array([np.asarray(np.atleast_2d(D.A[r.session].StimReg)[r.unit][w].Xval)[:, 1] for w in range(36)])
    k = tset[r.session]
    X0.setdefault(k, x)
    dx[k] = max(dx[k], np.abs(x - X0[k]).max())
print("largest difference of Xval between units, within each impulse-timing set:", [round(v, 6) for v in dx.values()])
print("between timing sets, largest difference:", round(float(np.abs(np.subtract(*list(X0.values())[:2])).max()), 1))''')
s=s.replace('''print("max |R2 - deposited R2| = %.2e, max |log10 p - deposited| = %.2e" % (np.abs(R2 - dep[..., 0]).max(),
      np.abs(np.log10(P + 1e-300) - np.log10(dep[..., 1] + 1e-300)).max()))''','''print("units with no spikes in 0-180 ms (regression undefined):", int(np.isnan(R2).all(1).sum()))
print("max |R2 - deposited R2| = %.2e, max |log10 p - deposited| = %.2e" % (np.nanmax(np.abs(R2 - dep[..., 0])),
      np.nanmax(np.abs(np.log10(P + 1e-300) - np.log10(dep[..., 1] + 1e-300)))))
R2 = np.nan_to_num(R2, nan=0.0); P = np.nan_to_num(P, nan=1.0); B = np.nan_to_num(B)''')
s=s.replace('''print("best window (highest R2) equals deposited PeakBin for", int(((R2.argmax(1) + 1) * 5 == dep_best).sum()), "of", len(U), "units")''','''same = (R2.argmax(1) + 1) * 5 == dep_best
print("best window (highest R2) equals deposited PeakBin for", int(same.sum()), "of", len(U), "units; the others:",
      U.loc[~same, ["session", "unit", "dep_label", "dep_peakbin"]].to_dict("records"))''')
s=s.replace('''        m = (t >= 0) & (t <= 150)
        sigt''','''        m = (t >= 0) & (t <= 150) if rd == "a" else (t >= 0) & (t + 5 <= 150)
        sigt''')
s=s.replace('''for (c, side), units in resp.items():
    for base in ["25", "10"]:
        tab, pe = adaptation(units, "FFF", base)''','''resp[("cls", "all Fast RS")] = list(fastrs["cls"])
for (c, side), units in resp.items():
    for base in ["25", "10"]:
        tab, pe = adaptation(units, "FFF", base)''')
s=s.replace(".min(1)",".min(axis=1)").replace(".max(1)",".max(axis=1)").replace("fr.mean(1)","fr.mean(axis=1)").replace("ct.sum(1)","ct.sum(axis=1)").replace('].sum(1)','].sum(axis=1)').replace("].mean(1).mean()","].mean(axis=1).mean()")
open(p,'w').write(s)
EOF
grep -n "all Fast RS" nb1.py | head -3
```

```
730:resp[("cls", "all Fast RS")] = list(fastrs["cls"])
Shell cwd was reset to
```

**Agent**

Now the decoder notebook.

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb2.py",
 "content": "# %% [markdown]\n# # Reproducing McGuire, Telian, Laboy-Juarez et al. (2016) from CRCNS ssc-4: decoders (Figure 9)\n#\n# Paper: doi:10.1371/journal.pbio.1002549. Dataset: CRCNS ssc-4 (doi:10.6080/K06D5QXN),\n# `ssc-4/live/AllRats.mat`, version `unversioned`, pinned by its MD5 sum\n# a929b803ca0feab5270e807f571d13eb from the data set's `checksums.md5` (the only version in the\n# bucket; see the header of `reproduce_mcguire_2016.ipynb` for the reasons and the data checks).\n# The claims file was written from the version of record with the Methods and supporting legends.\n#\n# The unit classes are recomputed here exactly as in `reproduce_mcguire_2016.ipynb` (temporal\n# modulation reading a, regression classes reading a with 55 ms Slow), with the same seed.\n#\n# | claim | here |\n# |---|---|\n# | fig9b-stimulus-decoder-fast-medium | tested |\n# | fig9c-best-units-short-windows | tested |\n# | fig9b-stimulus-decoder-slow-chance | tested |\n# | fig9d-single-bin-decoder | tested |\n# | fig9e-temporal-pattern-decoding | tested |\n# | fig9f-choice-decoder | tested |\n# | fig9g-l5b-slow-positive-best-choice | tested |\n#\n# Decoder details (helper docstring): logistic regression per unit, L2 with C = 1 (claim reading a)\n# fit by a batched Newton solver checked against scikit-learn below; reading b (C chosen by 5-fold\n# cross-validation on the 70%) is run with fewer repeats, as it costs about 30 times more. The\n# number of repeats of each run is printed with it.\n\n# %%\nimport collections, time, os\nos.environ.setdefault(\"OMP_NUM_THREADS\", \"1\")\nimport numpy as np, pandas as pd\nfrom scipy import stats\nfrom sklearn.linear_model import LogisticRegression\nimport ssc4\npd.set_option(\"display.width\", 200)\nt_start = time.time()\nD = ssc4.Data(ssc4.load_mat())\nU = D.units\npmod = ssc4.temporal_pvals(D, \"np\", seed=1)\nR2, P, B = ssc4.regress_all(D)\nR2 = np.nan_to_num(R2, nan=0.0); P = np.nan_to_num(P, nan=1.0); B = np.nan_to_num(B)\nU[\"mod\"] = pmod < 0.05\nU[\"cls\"], U[\"best\"], _, _ = ssc4.unit_classes(R2, P, B, U[\"mod\"].values, \"all\", False)\nU[\"cls_dep\"] = ssc4.deposited_classes(D)\n\n# %% tags=sanity\nprint(\"sessions\", len(D.A), \"units\", len(U), \"completed trials\", int(D.trials.complete.sum()))\nprint(\"completed trials by sequence\", D.trials[D.trials.complete].stim.value_counts().to_dict())\nprint(\"classes (this attempt)\", U.cls.value_counts().to_dict())\nprint(\"classes (deposited labels)\", U.cls_dep.value_counts().to_dict())\nFM = U.uid[U.cls.isin([\"Fast\", \"Medium\"])].values\nSL = U.uid[U.cls.isin([\"SlowPos\", \"SlowNeg\"])].values\nFMd = U.uid[U.cls_dep.isin([\"Fast\", \"Medium\"])].values\nSLd = U.uid[U.cls_dep.isin([\"SlowPos\", \"SlowNeg\"])].values\nprint(\"Fast/Medium units %d, Slow units %d (deposited: %d, %d)\" % (len(FM), len(SL), len(FMd), len(SLd)))\nntr = pd.Series({u: len(D.unit_trials(u)[1]) for u in U.uid})\nprint(\"completed trials per unit: min %d, median %d, max %d\" % (ntr.min(), ntr.median(), ntr.max()))\nX, t = ssc4.unit_features(D, FM[0], \"10ms\")\nprint(\"10-ms features of one unit: shape\", X.shape, \"count range\", X.min(), X.max())\nwithdraw = D.trials[D.trials.complete].withdraw_t\nprint(\"withdrawal after onset (ms), completed trials: min %.0f, mean %.0f, max %.0f\" % (withdraw.min(), withdraw.mean(), withdraw.max()))\n# the batched solver against scikit-learn on one unit\ny = (t.stim == \"FFF\").values.astype(float)\nb = ssc4.fit_logistic(X[None], y[None], np.ones((1, len(y))))\nsk = LogisticRegression(C=1.0, tol=1e-10, max_iter=10000).fit(X, y)\nprint(\"batched Newton vs scikit-learn lbfgs: max coefficient difference %.2e, intercepts %.5f %.5f\"\n      % (np.abs(b[0, :-1] - sk.coef_[0]).max(), b[0, -1], sk.intercept_[0]))\n\n# %%\nORDER = [\"FFF\", \"FMS\", \"SMF\", \"SSS\"]\ndef show(conf, accs, label):\n    cm = pd.DataFrame(conf, index=ORDER, columns=ORDER)\n    diag = np.diag(conf)\n    fs = [ORDER.index(\"FMS\"), ORDER.index(\"SMF\")]\n    A = diag[fs].mean()\n    sub = conf[np.ix_(fs, fs)]\n    Bv = np.mean(np.diag(sub) / sub.sum(1))\n    print(\"%s: %d repeats, overall %.1f%% (SD over repeats %.1f); per sequence %s; FMS/SMF reading A %.1f%%, reading B %.1f%%\"\n          % (label, len(accs), 100 * accs.mean(), 100 * accs.std(), dict(zip(ORDER, (100 * diag).round(1))), 100 * A, 100 * Bv))\n    print(cm.round(3))\n    return dict(overall=100 * accs.mean(), **{s: 100 * d for s, d in zip(ORDER, diag)}, A=100 * A, B=100 * Bv)\nRES = {}\ndef run(name, units, kind, how=None, reps=300, cv=False, seed=0):\n    t0 = time.time()\n    conf, accs, ua = ssc4.stim_decoder(D, units, kind, how, repeats=reps, seed=seed, cv=cv)\n    RES[name] = dict(conf=conf, accs=accs, ua=ua, units=units, summary=show(conf, accs, name))\n    print(\"   (%.0f s)\" % (time.time() - t0))\n\n# %% [markdown]\n# ### fig9b-stimulus-decoder-fast-medium\n#\n# > A decoder built from all Fast and Medium units with 10-ms bins identified the sequence with 83%\n# > accuracy (74% for FMS to 88% for FFF; chance 25%), and identified FMS and SMF with 78% accuracy.\n\n# %% tags=claim:fig9b-stimulus-decoder-fast-medium\nrun(\"FM 10ms\", FM, \"10ms\", seed=11)\nrun(\"FM 10ms, C by CV (reading b)\", FM, \"10ms\", reps=10, cv=True, seed=12)\nrun(\"variant: FM 10ms, deposited labels\", FMd, \"10ms\", reps=100, seed=13)\n\n# %% [markdown]\n# ### fig9c-best-units-short-windows\n#\n# > The individual units with the best stimulus prediction in the Fast/Medium decoder were those\n# > with 5 to 10 ms best integration windows.\n\n# %% tags=claim:fig9c-best-units-short-windows\nr = RES[\"FM 10ms\"]\nua = pd.DataFrame(dict(acc=100 * r[\"ua\"], best=U.best[r[\"units\"]].values, cls=U.cls[r[\"units\"]].values))\ng = ua.groupby(\"best\").acc.agg([\"mean\", \"size\"]).round(1)\nprint(g.T.to_string())\ntop = ua.nlargest(int(np.ceil(0.1 * len(ua))), \"acc\")\nprint(\"top 10%% (%d units): best windows %s; from 5 or 10 ms: %d\" % (len(top), top.best.value_counts().to_dict(), top.best.isin([5, 10]).sum()))\nprint(\"group with the highest mean:\", g[\"mean\"].idxmax(), \"ms; groups with at least 3 units:\", g[g[\"size\"] >= 3][\"mean\"].idxmax(), \"ms\")\nprint(\"chance 25%; units above 25%:\", int((ua.acc > 25).sum()), \"of\", len(ua))\n\n# %% [markdown]\n# ### fig9b-stimulus-decoder-slow-chance\n#\n# > A decoder built from all Slow units with 10-ms bins predicted sequence identity near chance (32%,\n# > not different from chance).\n\n# %% tags=claim:fig9b-stimulus-decoder-slow-chance\nrun(\"Slow 10ms\", SL, \"10ms\", seed=21)\nrun(\"Slow 10ms, C by CV (reading b)\", SL, \"10ms\", reps=10, cv=True, seed=22)\nrun(\"variant: Slow 10ms, deposited labels\", SLd, \"10ms\", reps=100, seed=23)\ndef chance_tests(name, npseudo=100):\n    a = RES[name][\"accs\"]\n    pa = min(1.0, 2 * min(np.mean(a <= 0.25), np.mean(a >= 0.25)))\n    n = len(a) * 4 * npseudo\n    k = int(round(a.mean() * n))\n    pb = stats.binomtest(k, n, 0.25).pvalue\n    print(\"%s: accuracy %.1f%%; (a) two-sided fraction of repeats on the other side of 25%%: p = %.3f; (b) binomial test of %d pooled pseudo-trials: p = %.2g\"\n          % (name, 100 * a.mean(), pa, n, pb))\nfor nm in [\"Slow 10ms\", \"Slow 10ms, C by CV (reading b)\", \"variant: Slow 10ms, deposited labels\"]:\n    chance_tests(nm)\n\n# %% [markdown]\n# ### fig9d-single-bin-decoder\n#\n# > Decoding from mean firing rate in a single 150-ms bin reduced Fast/Medium decoder accuracy to 43%\n# > and did not improve Slow decoder accuracy.\n\n# %% tags=claim:fig9d-single-bin-decoder\nrun(\"FM 1bin\", FM, \"1bin\", seed=31)\nrun(\"Slow 1bin\", SL, \"1bin\", seed=32)\nrun(\"FM 1bin, C by CV (reading b)\", FM, \"1bin\", reps=10, cv=True, seed=33)\nrun(\"Slow 1bin, C by CV (reading b)\", SL, \"1bin\", reps=10, cv=True, seed=34)\nfor a, b in [(\"Slow 1bin\", \"Slow 10ms\"), (\"Slow 1bin, C by CV (reading b)\", \"Slow 10ms, C by CV (reading b)\")]:\n    d = RES[a][\"summary\"][\"overall\"] - RES[b][\"summary\"][\"overall\"]\n    print(\"%s minus %s: %.1f points (limit 3.2)\" % (a, b, d))\n\n# %% [markdown]\n# ### fig9e-temporal-pattern-decoding\n#\n# > Fast/Medium decoders trained on rate-normalized spike trains performed well (80%), while\n# > time-scrambling spikes within trials abolished performance.\n\n# %% tags=claim:fig9e-temporal-pattern-decoding\nrun(\"FM 10ms rate-normalized\", FM, \"10ms\", \"norm\", seed=41)\nrun(\"FM 10ms time-scrambled\", FM, \"10ms\", \"scramble\", seed=42)\nrun(\"FM 10ms rate-normalized, C by CV (reading b)\", FM, \"10ms\", \"norm\", reps=10, cv=True, seed=43)\nrun(\"FM 10ms time-scrambled, C by CV (reading b)\", FM, \"10ms\", \"scramble\", reps=10, cv=True, seed=44)\nfor nm in [\"FM 10ms time-scrambled\", \"FM 10ms time-scrambled, C by CV (reading b)\"]:\n    chance_tests(nm)\n    print(\"   below 32%%: %s\" % (RES[nm][\"summary\"][\"overall\"] < 32))\n\n# %% [markdown]\n# ### fig9f-choice-decoder\n#\n# > A choice decoder from Slow units predicted drink port choice at 65% (chance 50%) from a single\n# > 150-ms bin or from the last 100 ms before nose poke withdrawal, while one from Fast and Medium\n# > units could not predict choice.\n#\n# Training weights each choice equally (an assumption: the Methods sum the probabilities and give\n# chance as 50%, which an unweighted fit on a side-biased rat does not give); the unweighted fit is\n# shown as a variant.\n\n# %% tags=claim:fig9f-choice-decoder\nCH = {}\ndef runc(name, units, kind, reps=300, seed=0, balanced=True, cv=False):\n    t0 = time.time()\n    res, ua = ssc4.choice_decoder(D, units, kind, repeats=reps, seed=seed, balanced=balanced, cv=cv)\n    tab = pd.DataFrame(res, index=[\"i equal draws\", \"ii data proportions\"]).T.loc[ORDER] * 100\n    a_i, a_ii = tab.iloc[:, 0].mean(), tab.iloc[:, 1].mean()\n    allt = D.trials[D.trials.complete & D.trials.session.isin(U.session[units].unique())]\n    w = allt.groupby(\"stim\").size()\n    p_i = (tab.iloc[:, 0] * w.loc[ORDER]).sum() / w.sum()\n    p_ii = (tab.iloc[:, 1] * w.loc[ORDER]).sum() / w.sum()\n    CH[name] = dict(tab=tab, ua=ua, units=units, a_i=a_i, a_ii=a_ii, pooled_i=p_i, pooled_ii=p_ii)\n    print(\"%s: %d repeats; mean over sequences (a): draws i %.1f%%, ii %.1f%%; pooled over trials (b): i %.1f%%, ii %.1f%%  (%.0f s)\"\n          % (name, reps, a_i, a_ii, p_i, p_ii, time.time() - t0))\n    print(tab.round(1).T.to_string())\nrunc(\"Slow 1bin\", SL, \"1bin\", seed=51)\nrunc(\"Slow pre100\", SL, \"pre100\", seed=52)\nrunc(\"FM 1bin\", FM, \"1bin\", seed=53)\nrunc(\"FM pre100\", FM, \"pre100\", seed=54)\nrunc(\"Slow 1bin, C by CV (reading b)\", SL, \"1bin\", reps=10, seed=55, cv=True)\nrunc(\"Slow pre100, C by CV (reading b)\", SL, \"pre100\", reps=10, seed=56, cv=True)\nrunc(\"FM 1bin, C by CV (reading b)\", FM, \"1bin\", reps=10, seed=57, cv=True)\nrunc(\"FM pre100, C by CV (reading b)\", FM, \"pre100\", reps=10, seed=58, cv=True)\nrunc(\"variant: Slow pre100, unweighted training\", SL, \"pre100\", reps=50, seed=59, balanced=False)\nrunc(\"variant: FM pre100, unweighted training\", FM, \"pre100\", reps=50, seed=60, balanced=False)\nrunc(\"variant: Slow pre100, deposited labels\", SLd, \"pre100\", reps=100, seed=61)\nrunc(\"variant: FM pre100, deposited labels\", FMd, \"pre100\", reps=100, seed=62)\nprint(\"\\nchance: 50% under draws i; under draws ii, the majority choice of each sequence gives\",\n      {s: round(100 * max(p, 1 - p), 1) for s, p in D.trials[D.trials.complete].groupby(\"stim\").chosen.mean().items()})\n\n# %% [markdown]\n# ### fig9g-l5b-slow-positive-best-choice\n#\n# > The units with the best choice prediction were Slow Positive units located primarily in L5b.\n#\n# Each Slow unit's own classifier on its test trials, one 100-ms bin before withdrawal, scored as\n# balanced accuracy (mean of right and left hit rates) so that chance is 50%, a standard choice.\n\n# %% tags=claim:fig9g-l5b-slow-positive-best-choice\nr = CH[\"Slow pre100\"]\nua = pd.DataFrame(dict(acc=100 * r[\"ua\"], layer=U.layer[r[\"units\"]].values, cls=U.cls[r[\"units\"]].values))\ng = ua.groupby([\"layer\", \"cls\"]).acc.agg([\"mean\", \"size\"]).round(1)\nprint(g.to_string())\nprint(\"group with the highest mean:\", g[\"mean\"].idxmax(), \"| among groups with at least 3 units:\", g[g[\"size\"] >= 3][\"mean\"].idxmax())\ntop = ua.nlargest(int(np.ceil(0.1 * len(ua))), \"acc\")\nprint(\"top 10%% (%d units): %s; L5b Slow Positive: %d\" % (len(top), collections.Counter(zip(top.layer, top.cls)).most_common(),\n      int(((top.layer == \"L5b\") & (top.cls == \"SlowPos\")).sum())))\nprint(\"total run time of this notebook so far: %.1f min\" % ((time.time() - t_start) / 60))\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb2.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
date -u; cd entries/mcguire-2016 && . $TMPDIR/dev/bin/activate && cat > $TMPDIR/t3.py <<'EOF'
import time, resource, numpy as np, sys
import ssc4
D=ssc4.Data(ssc4.load_mat())
fm=D.units.uid[D.units.dep_label.isin(['FastPos','FastNeg'])].values
sl=D.units.uid[D.units.dep_label.isin(['SlowPos','SlowNeg'])].values
for nm,f in [('stim10',lambda: ssc4.stim_decoder(D,fm,'10ms',repeats=3)),('stimcv',lambda: ssc4.stim_decoder(D,fm,'10ms',repeats=1,cv=True)),
             ('choice',lambda: ssc4.choice_decoder(D,sl,'pre100',repeats=3)),('choicecv',lambda: ssc4.choice_decoder(D,sl,'pre100',repeats=1,cv=True))]:
    t=time.time(); r=f(); print(nm, time.time()-t)
    if nm.startswith('choice'): print(r[0])
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
EOF
OMP_NUM_THREADS=1 python $TMPDIR/t3.py
```

```
Exit code 1
Wed Nov 11 17:19:02 UTC 2026
Traceback (most recent call last):
  File "/tmp/claude-1001/t3.py", line 2, in <module>
    import ssc4
ModuleNotFoundError: No module named 'ssc4'
```

**Agent calls Bash**

```bash
cd entries/mcguire-2016 && . $TMPDIR/dev/bin/activate && OMP_NUM_THREADS=1 PYTHONPATH=. python $TMPDIR/t3.py
```

```
stim10 2.508991003036499
stimcv 18.51395344734192
choice 0.43435072898864746
{'FMS': array([0.93833333, 0.94001003]), 'SMF': array([0.91666667, 0.91952158]), 'FFF': array([0.93      , 0.93931979]), 'SSS': array([0.93      , 0.93693934])}
choicecv 0.6182916164398193
{'FMS': array([0.925     , 0.92763481]), 'SMF': array([0.97      , 0.97095164]), 'FFF': array([0.945    , 0.9465533]), 'SSS': array([0.965     , 0.97020451])}
0.730692
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='ssc4.py'; s=open(p).read()
old='''def _fit(Xs, ys, rng, cv, balanced=False):
    Xb, yb, wb = _pad(Xs, ys, balanced)
    if not cv:
        return fit_logistic(Xb, yb, wb)'''
new='''def _fit(Xs, ys, rng, cv, balanced=False):
    if not cv:   # problems grouped by trial count, so that little padding is fitted
        order = np.argsort([len(y) for y in ys])
        beta = np.zeros((len(ys), Xs[0].shape[1] + 1))
        for chunk in np.array_split(order, max(1, len(ys) // 64)):
            Xb, yb, wb = _pad([Xs[i] for i in chunk], [ys[i] for i in chunk], balanced)
            beta[chunk] = fit_logistic(Xb, yb, wb)
        return beta
    Xb, yb, wb = _pad(Xs, ys, balanced)'''
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
EOF
. $TMPDIR/dev/bin/activate && OMP_NUM_THREADS=1 PYTHONPATH=. python $TMPDIR/t3.py
```

```
stim10 1.4743995666503906
stimcv 18.307055711746216
choice 0.43927979469299316
{'FMS': array([0.93833333, 0.94001003]), 'SMF': array([0.91666667, 0.91952158]), 'FFF': array([0.93      , 0.93931979]), 'SSS': array([0.93      , 0.93693934])}
choicecv 0.6139922142028809
{'FMS': array([0.925     , 0.92763481]), 'SMF': array([0.97      , 0.97095164]), 'FFF': array([0.945    , 0.9465533]), 'SSS': array([0.965     , 0.97020451])}
0.734788
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='ssc4.py'; s=open(p).read()
old=s[s.index('def _fit(Xs, ys, rng, cv, balanced=False):'):s.index('def stim_decoder')]
new='''def _fit_bucketed(Xs, ys, C=1.0, balanced=False):
    """Fit many problems, grouped by trial count so that little padding is fitted."""
    order = np.argsort([len(y) for y in ys])
    beta = np.zeros((len(ys), Xs[0].shape[1] + 1))
    for chunk in np.array_split(order, max(1, len(ys) // 64)):
        Xb, yb, wb = _pad([Xs[i] for i in chunk], [ys[i] for i in chunk], balanced)
        beta[chunk] = fit_logistic(Xb, yb, wb, C=C)
    return beta


def _fit(Xs, ys, rng, cv, balanced=False):
    if not cv:
        return _fit_bucketed(Xs, ys, 1.0, balanced)
    Cs = _cv_C(Xs, ys, rng, [1e-3, 1e-2, 1e-1, 1, 10, 100], balanced=balanced)
    beta = np.zeros((len(ys), Xs[0].shape[1] + 1))
    for C in np.unique(Cs):
        idx = np.where(Cs == C)[0]
        beta[idx] = _fit_bucketed([Xs[i] for i in idx], [ys[i] for i in idx], C, balanced)
    return beta


'''
s=s.replace(old,new)
old2=s[s.index('def _cv_C('):s.index('def _pad(')]
new2='''def _cv_C(Xs, ys, rng, Cs, folds=5, balanced=False):
    """Per problem, the C of the grid with the best mean held-out accuracy over stratified folds
    (balanced accuracy when the fit is class-balanced)."""
    P = len(Xs)
    acc = np.zeros((P, len(Cs)))
    fold_of = []
    for y in ys:
        f = np.zeros(len(y), int)
        for c in np.unique(y):
            idx = np.where(y == c)[0]
            rng.shuffle(idx)
            f[idx] = np.arange(len(idx)) % folds
        fold_of.append(f)
    for k in range(folds):
        Xtr = [x[f != k] for x, f in zip(Xs, fold_of)]
        ytr = [y[f != k] for y, f in zip(ys, fold_of)]
        for j, C in enumerate(Cs):
            beta = _fit_bucketed(Xtr, ytr, C, balanced)
            for p in range(P):
                te = fold_of[p] == k
                if te.sum():
                    hit = (predict_logistic(beta[p], Xs[p][te]) > 0.5) == (ys[p][te] > 0.5)
                    if balanced:
                        acc[p, j] += np.mean([hit[ys[p][te] == c].mean() for c in (0, 1) if np.any(ys[p][te] == c)]) / folds
                    else:
                        acc[p, j] += hit.mean() / folds
    return np.array(Cs)[acc.argmax(1)]


'''
s=s.replace(old2,new2)
open(p,'w').write(s)
EOF
. $TMPDIR/dev/bin/activate && OMP_NUM_THREADS=1 PYTHONPATH=. python $TMPDIR/t3.py
```

```
stim10 1.4878408908843994
stimcv 10.543389320373535
choice 0.4424571990966797
{'FMS': array([0.93833333, 0.94001003]), 'SMF': array([0.91666667, 0.91952158]), 'FFF': array([0.93      , 0.93931979]), 'SSS': array([0.93      , 0.93693934])}
choicecv 0.7249977588653564
{'FMS': array([0.73      , 0.72089794]), 'SMF': array([0.675     , 0.67357254]), 'FFF': array([0.84      , 0.82136042]), 'SSS': array([0.975     , 0.96979549])}
0.630948
```

**Agent**

Decoders now take about 0.5 s per repeat (10 s with cross-validated C). The decoder notebook should take about 20 minutes. Running notebook 1 again first, then notebook 2.

**Agent calls Bash**

```bash
sed -i 's/reps=10, cv=True, seed=\(1[0-9]\|2[0-9]\|3[0-9]\|4[0-9]\))/reps=5, cv=True, seed=\1)/' $TMPDIR/nb2.py; grep -n "cv=True" $TMPDIR/nb2.py | head -20; . $TMPDIR/dev/bin/activate && time PYTHONPATH=. python $TMPDIR/nb1.py > $TMPDIR/nb1.out 2>&1; grep -n -i "error\|Traceback" $TMPDIR/nb1.out | head
```

```
97:run("FM 10ms, C by CV (reading b)", FM, "10ms", reps=5, cv=True, seed=12)
124:run("Slow 10ms, C by CV (reading b)", SL, "10ms", reps=5, cv=True, seed=22)
146:run("FM 1bin, C by CV (reading b)", FM, "1bin", reps=5, cv=True, seed=33)
147:run("Slow 1bin, C by CV (reading b)", SL, "1bin", reps=5, cv=True, seed=34)
161:run("FM 10ms rate-normalized, C by CV (reading b)", FM, "10ms", "norm", reps=5, cv=True, seed=43)
162:run("FM 10ms time-scrambled, C by CV (reading b)", FM, "10ms", "scramble", reps=5, cv=True, seed=44)
197:runc("Slow 1bin, C by CV (reading b)", SL, "1bin", reps=10, seed=55, cv=True)
198:runc("Slow pre100, C by CV (reading b)", SL, "pre100", reps=10, seed=56, cv=True)
199:runc("FM 1bin, C by CV (reading b)", FM, "1bin", reps=10, seed=57, cv=True)
200:runc("FM pre100, C by CV (reading b)", FM, "pre100", reps=10, seed=58, cv=True)

real	1m38.327s
user	1m34.886s
sys	0m0.662s
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR; sed -n '/units whose deposited Yval/,/sign test/p' nb1.out; grep -n "all Fast RS" -A3 nb1.out | head -30; grep -n "L4 Fast" nb1.out; grep -n "temporal\|modulated .* of 506" nb1.out | head
```

```
Wed Nov 11 17:22:48 UTC 2026
units whose deposited Yval equals the summed counts, by trial selection: {'all trials': 1, 'nose poke > 250 ms': 204, 'completed': 506} of 506
largest difference of Xval between units, within each impulse-timing set: [0.0, np.float64(11291.47), 0.0]
between timing sets, largest difference: 11291.5
units with no spikes in 0-180 ms (regression undefined): 1
max |R2 - deposited R2| = 1.63e-15, max |log10 p - deposited| = 1.82e-13
best window (highest R2) equals deposited PeakBin for 505 of 506 units; the others: [{'session': 6, 'unit': 3, 'dep_label': 'ImproperPeakBin', 'dep_peakbin': nan}]
sessions sharing a trial table with another: 0
unit pairs with identical spike matrices over the first 20 trials: []
window 55 to 60 ms: sessions with F-first > S-first rate 61 of 80; mean difference 18.4 Hz (summed over units); sign test p = 2.7e-06
462:FFF, classes cls, all Fast RS-sided, baseline 25 ms
463-     mean_ratio    sem  ratio_of_means  p_ratio_vs_1  p_paired     n  n_ratio
464-2/1       -0.16  0.505           0.701         0.027     0.039  63.0     41.0
465-3/1        0.54  0.348           0.773         0.194     0.141  63.0     41.0
--
467:FFF, classes cls, all Fast RS-sided, baseline 10 ms
468-       mean_ratio           sem  ratio_of_means  p_ratio_vs_1  p_paired     n  n_ratio
469-2/1 -2.101344e+12  1.359710e+13           0.754         0.878     0.039  63.0     47.0
470-3/1 -5.463493e+13  3.832840e+13           0.813         0.161     0.141  63.0     47.0
--
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
sed -i 's/print("\\nFFF, classes %s, %s-sided, baseline %s ms" % (c, side, base))/print("\\nFFF, classes %s, F-responsive selection %s, baseline %s ms" % (c, side, base))/; s/print("\\nSSS, classes %s, %s-sided, baseline %s ms" % (c, side, base))/print("\\nSSS, classes %s, F-responsive selection %s, baseline %s ms" % (c, side, base))/; s/print("classes %s, %s-sided, baseline %s: n = %d, pulse 2/print("classes %s, selection %s, baseline %s: n = %d, pulse 2/' $TMPDIR/nb1.py; grep -c "selection %s" $TMPDIR/nb1.py; cd entries/mcguire-2016 && . $TMPDIR/dev/bin/activate && time OMP_NUM_THREADS=1 PYTHONPATH=. python $TMPDIR/nb2.py > $TMPDIR/nb2.out 2>&1; tail -3 $TMPDIR/nb2.out
```

```
3

real	15m28.663s
user	15m25.743s
sys	0m0.650s
group with the highest mean: ('L5b', 'SlowPos') | among groups with at least 3 units: ('L5b', 'SlowPos')
top 10% (11 units): [(('L5b', 'SlowPos'), 5), (('L6', 'SlowPos'), 2), (('L5a', 'SlowPos'), 2), (('L5b', 'SlowNeg'), 1), (('L2/3', 'SlowNeg'), 1)]; L5b Slow Positive: 5
total run time of this notebook so far: 15.4 min
```

**Agent calls Bash**

```bash
date -u; grep -v "^\s*$" $TMPDIR/nb2.out | grep -v Warning | head -250
```

```
Wed Nov 11 17:38:28 UTC 2026
sessions 80 units 506 completed trials 14186
completed trials by sequence {'SMF': 3599, 'SSS': 3558, 'FMS': 3547, 'FFF': 3482}
classes (this attempt) {'none': 196, 'Fast': 160, 'SlowNeg': 51, 'SlowPos': 51, 'Medium': 48}
classes (deposited labels) {'none': 196, 'Fast': 160, 'Medium': 53, 'SlowPos': 51, 'SlowNeg': 46}
Fast/Medium units 208, Slow units 102 (deposited: 213, 97)
completed trials per unit: min 43, median 168, max 332
10-ms features of one unit: shape (124, 15) count range 0.0 4.0
withdrawal after onset (ms), completed trials: min 153, mean 194, max 362
batched Newton vs scikit-learn lbfgs: max coefficient difference 6.43e-08, intercepts -1.04419 -1.04419
FM 10ms: 300 repeats, overall 84.1% (SD over repeats 3.6); per sequence {'FFF': np.float64(84.4), 'FMS': np.float64(74.9), 'SMF': np.float64(89.2), 'SSS': np.float64(87.9)}; FMS/SMF reading A 82.1%, reading B 97.6%
       FFF    FMS    SMF    SSS
FFF  0.844  0.147  0.008  0.001
FMS  0.190  0.749  0.037  0.024
SMF  0.000  0.001  0.892  0.107
SSS  0.000  0.001  0.120  0.879
   (122 s)
FM 10ms, C by CV (reading b): 5 repeats, overall 76.0% (SD over repeats 5.6); per sequence {'FFF': np.float64(75.2), 'FMS': np.float64(62.2), 'SMF': np.float64(89.2), 'SSS': np.float64(77.6)}; FMS/SMF reading A 75.7%, reading B 90.4%
       FFF    FMS    SMF    SSS
FFF  0.752  0.176  0.048  0.024
[... 167 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls schemas; cat attempts/fouke-2025-01.yaml | head -150
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
schema_version: 3
id: fouke-2025-01
datasets:
- archive: dandi
  id: "001453"
  version: 0.250518.1950
  doi: 10.48324/dandi.001453/0.250518.1950
  relation: primary
paper: doi:10.1016/j.cub.2025.04.027
date: 2026-10-14
entry: fouke-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
[... 134 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n '150,400p' attempts/fouke-2025-01.yaml | grep -n "^[a-z]\|^- kind\|^  [a-z_]*:" | head -40; python -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
print(json.dumps(s['properties'],indent=0)[:3500])"
```

```
1:  outcome: not_reproduced
2:  notebook: reproduce_fouke_2025.ipynb
3:  output: claim:fig1h-zf-higher-angular-acceleration
4:  notes: With angular acceleration as the Methods define it, DC are higher than ZF for all nine
20:  deviations:
26:  outcome: reproduced
27:  notebook: reproduce_fouke_2025.ipynb
28:  output: claim:figs1e-dc-respond-less-monocular
29:  notes: Species effect F = 23.3, p = 2.5e-06. DC turn less toward the stimulus than ZF for
36:  deviations:
40:  outcome: reproduced
41:  notebook: reproduce_fouke_2025.ipynb
42:  output: claim:fig1c-continuous-vs-bouts
43:  notes: The median-to-mean ratio of instantaneous speed is 0.306 in ZF (25 fish, 0.244 to 0.580)
46:  deviations:
50:  outcome: blocked
51:  blocked_by: metadata_insufficient
52:  notes: The numbers come from single representative fish and trials. Fig1-S1.ipynb selects them
56:  outcome: blocked
57:  blocked_by: data_missing
[... 196 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
p=s['properties']
for k in ['inputs','outcomes','findings']: print(k, json.dumps(p[k])[:2500]); print()
print(json.dumps(s.get('\$defs',{}))[:3000])"; tail -60 attempts/fouke-2025-01.yaml; ls questions | head -3; head -30 questions/$(ls questions | head -1)
```

```
inputs {"description": "Everything the attempt used that is not in the dataset.", "type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["what", "source"], "properties": {"what": {"type": "string", "minLength": 1}, "source": {"description": "A DOI, or a repository URL with the commit read.", "type": "string", "minLength": 1}}}}

outcomes {"description": "One per claim attempted.", "type": "array", "minItems": 1, "items": {"type": "object", "additionalProperties": false, "required": ["claim", "outcome"], "properties": {"claim": {"description": "Claim id from the target's claims file.", "type": "string"}, "outcome": {"enum": ["reproduced", "partially_reproduced", "not_reproduced", "blocked"], "description": "Describes the result, not the method: whether the effect the claim states was found. Differences in method from the paper go in `deviations`."}, "blocked_by": {"description": "Required when outcome is blocked.", "enum": ["data_missing", "metadata_insufficient", "methods_underspecified", "data_unreadable", "dataset_missing", "too_large", "not_runnable", "other"]}, "notes": {"description": "What differs, or what was missing, stated factually.", "type": "string"}, "notebook": {"description": "Path of the notebook within the entry.", "type": "string"}, "output": {"description": "Which output shows the result, e.g. a cell tag.", "type": "string"}, "measured": {"description": "The values obtained, for claims with expected values: one number, or one per expected value, in the same order.", "oneOf": [{"type": "number"}, {"type": "array", "minItems": 1, "items": {"type": "number"}}]}, "deviations": {"description": "How the test differed from the paper's method or data, e.g. one session of four, or a substituted model.", "type": "array", "items": {"type": "string", "minLength": 1}}, "assumed": {"description": "True when the outcome rests on an assumption about a method the paper leaves open: a choice the paper best supports, stated in a dev
[... 78 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,25p questions/athalye-2023.yaml; grep -n "verifications\|^findings\|^- kind" attempts/fouke-2025-01.yaml | head; python -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(s['required']); print(json.dumps(s['properties']['provenance'])[1500:3200])"
```

```
dandiset: "000404"
paper: doi:10.1016/j.cub.2023.06.027
questions:
- claim: fig5f-condition-specific-next-command
  asked: 2026-10-30
  question: The criterion takes the error of the predicted condition-specific next command in the
    command's own units, as the paper does not state them. Are the expected values (3.956 for Monkey
    G, 7.324 for Monkey J, and the shuffle 5th percentiles 5.38 and 9.240 of Table S1) in those units,
    or in units ten times larger (commands computed from activity in Hz, counts per 100 ms bin times
    10, as the code converts spike counts to rates)?
  passage: Table S1, row labelled 5E, gives the error and shuffle values without a unit; Methods,
    "Predicting condition-specific next command", defines the error as the L2-norm of the difference
    between the true and predicted average next command; Methods, "Command definition", gives the
    command as the decoder's update to cursor velocity (cm/sec for Monkey G).
  why: In the command's units the errors here are 0.397 (G) and 0.705 (J), a tenth of the expected
    values, while every test and the fraction of significant tuples hold; multiplied by 10 they are
    3.973 and 7.052, within tolerance. Under the claims file as written the claim is partially
    reproduced; under the reading in units ten times larger it would be reproduced.
  answer: >-
    Ten times larger. The paper gives no unit (Table S1 row 5E; the Methods say only "The L2-norm
[... 16 more lines not kept]
```

**Agent**

Writing the conclusion cells now.

**Agent calls Bash**

```bash
cat > $TMPDIR/results1.py <<'EOF'
R = {
"fig2ab-fms-smf-not-discriminated": "**Result: partially reproduced.** In all five rats the data hold, FFF draws more right choices than SSS and FMS and SMF lie between them, and FMS against SMF is not significant at 0.00625 in any of them (smallest p 0.10 without and 0.11 with continuity correction, 62BS), under both trial readings, which select the same 14186 trials. Rat 62SC, the one the paper finds discriminating FMS from SMF, is not in the data set, nor are two other behaviour-only rats, so the claim is tested on 5 of 8 rats. The data set's per-rat means of sessions equal the S1 Data values for four rats and differ by up to 0.026 for 18FB.",
"training-days": "**Result: partially reproduced.** Counting distinct recording dates, the five rats in the data set have 11 to 20 days, mean 14.8 (s.d. 4.3): the mean and the maximum are within tolerance of 14.2 and 22, the minimum (11) is not within 0.8 of 8. The data hold only the recording days of five of the eight rats.",
"fig2c-choice-follows-mean-speed": "**Result: reproduced.** For each of the five rats relative right choice orders FFF > FMS and SMF > SSS, and its Pearson correlation with mean speed is 0.967 to 0.998, under both trial readings. The S1 Data means of all eight rats give the same (r 0.967 to 0.995).",
"fig2d-fixed-panel-impairs": "**Result: blocked (data_missing).** The data set has no fixed-panel trials. As a variant only, the per-rat values of S2B Fig in S2 Data give fixed-panel discrimination lower in all six rats, paired t p = 0.0120 with the rat at 0 kept and p = 0.0308 without it.",
"dprime-fff-sss-range": "**Result: partially reproduced.** Per-rat d-prime over pooled sessions is 0.45 to 1.09 (mean of sessions 0.46 to 1.23): the lowest value is within tolerance of 0.5, the highest is below 1.35 under both readings. The three rats missing from the data set include the two with the highest d-prime by S1 Data (62SS 1.32, 107Si 1.17).",
"fig3-fsfs-sffs-intensity-only": "**Result: reproduced.** From S1 Data, 58B is 69.98 +- 1.47% correct and 60W 69.17 +- 1.57% with different intensities, and 51.74 +- 0.81% and 53.02 +- 0.82% with the same intensity, over sessions up to day 56 and 52. The d-prime is 1.004 and 0.130 as the mean of the two rats (reading a), all within tolerance.",
"units-recorded": "**Result: reproduced.** The data set holds 330 single units and 176 multi-unit clusters over 80 sessions in five rats, 4.12 single units per session (0 to 12), each within tolerance. The total is 506 against the paper's 473; the 33 extra units cannot be identified, as the column map is missing.",
"baseline-rates": "**Result: partially reproduced.** RS single-unit layer means span 5.93 (L2/3) to 11.40 Hz (L5a), FS 7.59 to 30.18 Hz, and multi-units are higher than RS in 5 of 5 layers. The RS maximum is above the 11 Hz limit; the other three bounds are within tolerance. With all trials the RS maximum is 11.49 Hz.",
"temporal-modulation-count": "**Result: reproduced.** With the Methods' window, 0 to 180 ms after nose poke entry (reading a), 310 of 506 units (61.3%) are modulated, within tolerance of 305 and 63.5%; with 0 to 180 ms after onset (reading b) 261 (51.6%). The data set's own p-values also give 310, but they agree with reading (a) unit by unit for only 73.1% of units.",
"modulated-higher-baseline": "**Result: reproduced.** Modulated RS single units have higher baseline rates than non-modulated ones in 5 of 5 layers. The fraction modulated is 0.51 to 0.68 across layers (chi-square p = 0.105). Columns cannot be tested without the column map.",
"fig4d-evoked-modulation-by-layer": "**Result: partially reproduced.** No combination puts all five layers within tolerance; the closest, the absolute peak averaged over impulses (A, b, ii), has 4 of 5 (16.06, 15.29, 7.65, 16.56, 8.20 Hz, L5a outside). L5a and L6 are the two lowest layers under every combination.",
"latency-by-layer": "**Result: partially reproduced.** Latencies are 14 to 20 ms in every layer, longer than the paper's 9.8 to 16.1 ms; at most one layer is within tolerance under any reading. The ordering (L4, L5a, L5b below L2/3 and L6) holds under three of the four readings (medians with both tests, mean with the two-sided test).",
"fig4d-gradual-decrease": "**Result: not reproduced.** The population rate decreases in every layer, L5a included: the slope from -25 to 180 ms is -0.88 Hz per 100 ms in L5a (p < 0.001) and -1.09 to -2.43 in the others, and the last 30 ms are below baseline in all five layers. The claim requires no decrease in L5a.",
"fig6-regression-significant": "**Result: reproduced.** 194 of the 310 modulated units have a significant regression at p < 0.05/36, within tolerance of 204 (207 among the units the deposited p-values mark as modulated). The regression reproduces the data set's stored R2 and p to numerical precision.",
"fig6e-unit-classes": "**Result: partially reproduced.** Classing all modulated units by their best window (reading a) gives 160 Fast, 48 Medium, 51 Slow Positive and 51 Slow Negative (55 ms as Medium: 160, 50, 50, 50); Slow Negative is above the 48.4 limit, the other counts are within tolerance. Fast units are 51.6% of modulated units and 42.9% have 5 to 10 ms windows, both within tolerance; 93% of Fast units have positive slopes and 69% of Medium units negative. Classing only units with a significant regression (reading b) gives 119, 26, 23, 26. The data set's own labels give 160, 53, 51, 46, all within tolerance.",
"fig6fg-laminar-classes": "**Result: partially reproduced.** Under reading (a), Fast units are 69.2% of modulated units in L2/3 and L4, 50.7% in L5 and 26.5% in L6, and Slow units 18.3%, 33.3% and 54.4%: 4 of 6 values within tolerance (L6 Fast and L2/3-L4 Slow outside) and the gradient holds. The data set's labels give all 6 within tolerance (74.0, 49.6, 23.2; 13.0, 31.9, 56.5).",
"fig7c-fast-impulse-velocity": "**Result: reproduced.** Over 160 Fast units the net evoked rate is 9.59 Hz for F, 8.73 for M and 7.42 for S impulses (paired t F against S p = 1.4e-05); the deposited labels give the same order.",
"fig7c-fast-sequence-rate": "**Result: reproduced.** The sequence rate of Fast units orders FFF > FMS and SMF > SSS with both baselines. FMS and SMF do not differ with the 0 to 10 ms baseline (reading b; -0.76 Hz, p = 0.31) and differ just at 0.05 with the 25-ms baseline (reading a; -0.95 Hz, p = 0.046). The claim holds under reading (b).",
"fig7-fff-adaptation": "**Result: partially reproduced.** The t test selects 34 of 63 Fast RS single units, not 61. Over them the ratio of population means is 0.79 to 0.82 for pulse 2/1 and 0.80 to 0.83 for 3/1, within tolerance. Only 2/1 is significant: per-unit ratio against 1, p = 0.026 with the 25-ms baseline. 3/1 is not (p = 0.644), nor is either paired test (p 0.119 and 0.162). With all 63 Fast RS units (variant), the ratios of means are 0.70 and 0.77 and the paired test gives p = 0.039 for 2/1 and 0.141 for 3/1.",
"fig7-sss-no-adaptation": "**Result: reproduced.** For SSS the ratios of population means are 0.86 to 0.88 for 2/1 and 3/1, within tolerance, and no test finds a difference from pulse 1 (all p > 0.2) in any reading. Per-unit mean ratios with the 25-ms baseline are larger (1.34 and 1.66), outside tolerance for 3/1.",
"s4-fms-middle-pulse": "**Result: reproduced.** In the 34 selected units the pulse 2 response is 1.60 Hz lower in FMS than SMF with the 25-ms baseline (p = 0.259) and 0.20 Hz lower with the 10-ms one (p = 0.913). With all 63 Fast RS units (variant) it is 1.60 Hz lower, p = 0.087, close to the paper's p = 0.08.",
"fig7de-medium-suppressed": "**Result: partially reproduced.** Medium units do not distinguish impulses or sequences (F against S p = 0.637, FFF against SSS p = 0.428 and 0.468), but they are not suppressed by impulses: net evoked rates are +0.05 (F), -0.30 (M) and -0.36 Hz (S), none different from 0 (p > 0.6). With the data set's labels all three are negative (-0.27 to -0.52 Hz) and none significant.",
"fig8a-slow-positive-no-sequence-difference": "**Result: partially reproduced.** Slow Positive units respond to F (1.46 Hz, p = 0.0016) and M impulses (2.82 Hz, p = 0.00018), but also to S (1.23 Hz, p = 0.027), which the claim says they do not. Their sequence rates do not differ (repeated-measures ANOVA p = 0.087 and 0.430). Responses grow over the pulses (-0.76, 1.87, 5.57 Hz for pulses 1 to 3).",
"fig8b-slow-negative-no-impulse-response": "**Result: reproduced.** No impulse kind evokes a significant increase in the 51 Slow Negative units (t 1.88, -0.96 and 0.89), and their population rate falls from 0 to 180 ms (-5.49 Hz per 100 ms).",
"fig8d-slow-positive-right-choice-l5": "**Result: partially reproduced.** Slow Positive units in L5b fire more on right-choice trials (6.32 Hz, p = 0.0045 pooled; 7.24 Hz, p = 0.0008 per sequence), and L2/3, L4 and L6 show no bias. In L5a the bias is 4.27 Hz but not significant (p = 0.117 and 0.121, 6 units). With the data set's labels (7 L5a units) L5a reaches p = 0.049 under reading (a), so that the claim holds there.",
"fig8d-fast-medium-no-choice-bias": "**Result: reproduced.** With 5-ms bins (reading b) no bin from 0 to 150 ms differs between right- and left-choice trials in the 56 L4 Fast units. With 1-ms steps of 10-ms windows (reading a), 5 steps at 5 to 9 ms reach p < 0.05, with no run lasting to the end of the sequence. The largest difference is 2.6 to 2.7 Hz.",
"fig8e-choice-divergence-125ms": "**Result: reproduced.** In 21 L5 Slow Positive units the right-left difference is significant without a break from 122 ms to 150 ms with 10-ms windows (reading a); with 5-ms bins the run from 125 ms lasts to 140 ms but not to 150. Withdrawals over the same sessions are at 153 ms at the earliest and 193 ms on average, all three values within tolerance under reading (a).",
"s5-slow-positive-no-integration": "**Result: reproduced.** With the 25-ms baseline (reading a), pulse 3 firing does not differ across sequences in right-choice (ANOVA p = 0.052) or left-choice trials (p = 0.324). It does not correlate with sequence mean speed or with the mean speed of pulses 2 and 3 or 1 and 2 (all p >= 0.08). Pulses 1 and 2 evoke 1.04 and -0.36 Hz. With the 10-ms baseline, the left-choice correlation with pulses 2 and 3 reaches p = 0.03.",
"s6-head-position-choice": "**Result: reproduced.** From S2 Data, head position along x differs between right- and left-choice trials at every frame from 100.8 ms (p = 0.037) on, by 0.595 mm at 126 ms. Head angle, both whisker tip coordinates and head y differ at no frame.",
"s7-no-fs-l5-slow-positive": "**Result: reproduced.** Every class holds RS, FS and multi-units; the FS fraction is 0.157 in Slow Positive and 0.039 in Slow Negative against 0.162 in Fast; the 21 L5 Slow Positive units are 15 RS and 6 multi-units, with no FS unit.",
}
EOF
python - <<'EOF'
import re,sys
sys.path.insert(0,'/tmp/claude-1001'); from results1 import R
p='/tmp/claude-1001/nb1.py'; s=open(p).read()
lines=s.split('\n'); out=[]; pending=None
for i,l in enumerate(lines):
    if l.startswith('# %%') and pending:
        out += ['# %% [markdown]', '# '+R[pending], '']
        pending=None
    m=re.match(r'# %% tags=claim:(\S+)',l)
    if m: pending=m.group(1)
    if l.startswith('# ### fig2d-fixed-panel-impairs'):
        pass
    out.append(l)
if pending: out += ['# %% [markdown]', '# '+R[pending], '']
s='\n'.join(out)
# fig2d: result after its variant cell
s=s.replace('''    print("%s: n = %d, fixed lower in %d, paired t = %.2f, p = %.4f" % (nm, len(d), (d.FixedPanel < d.MovingPanel).sum(), r.statistic, r.pvalue))
''','''    print("%s: n = %d, fixed lower in %d, paired t = %.2f, p = %.4f" % (nm, len(d), (d.FixedPanel < d.MovingPanel).sum(), r.statistic, r.pvalue))

# %% [markdown]
# '''+R["fig2d-fixed-panel-impairs"]+'''
''')
open(p,'w').write(s)
print(s.count('**Result:'))
EOF
```

```
30
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='nb1.py'; s=open(p).read()
reps=[("the ratio of population means is 0.79 to 0.82 for pulse 2/1 and 0.80 to 0.83 for 3/1","the ratio of population means is 0.79 to 0.83 for pulse 2/1 and 0.80 to 0.83 for 3/1"),
("nor is either paired test (p 0.119 and 0.162)","nor is either paired test (p 0.119 to 0.185)"),
("the ratios of population means are 0.86 to 0.88 for 2/1 and 3/1","the ratios of population means are 0.85 to 0.88 for 2/1 and 3/1"),
("Pulses 1 and 2 evoke 1.04 and -0.36 Hz.","Pulses 1 and 2 evoke 1.04 Hz on right-choice and -0.36 Hz on left-choice trials, against 5.40 to 12.13 Hz for pulse 3 on right-choice trials.")]
for a,b in reps:
    assert a in s, a; s=s.replace(a,b)
open(p,'w').write(s)
EOF
echo done
```

```
done
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='nb1.py'; s=open(p).read()
anchor='''# %% [markdown]
# ### Clock of the spikes against the trial table'''
add='''# %% [markdown]
# What the checks show (numbers above):
#
# - The stored regression inputs equal the spike counts summed over completed trials for all 506
#   units (204 units for nose poke > 250 ms, 1 for all trials). The authors' unit analyses used
#   completed trials, and so does this notebook.
# - The stored regressor is identical across units within two of the three impulse-timing sets and
#   differs within the third; each unit's own stored regressor is used. A fresh fit reproduces the
#   stored R2 and p to numerical precision; one unit has no spikes from 0 to 180 ms (stored label
#   ImproperPeakBin).
# - No two sessions share a trial table and no two units share spikes: no recording is deposited
#   twice. The paper says a new set of units was sampled in every session (Methods, Neural
#   Recordings), so units are counted once per session, an assumption the data cannot check.
# - The data set holds 506 units (330 single, 176 multi) where the paper reports 473 (306, 167).
#   The descriptor says units in columns A1 and B2 must be dropped using `MapPosition`, which the
#   file does not contain; leaving out the fifth electrode of 18FB and 18Ri gives 459, not 473.
#   The extra units cannot be identified.
# - The stored temporal-modulation p-values were computed with a -50 to 300 ms window
#   (`TempSig.Params`), where the Methods say 0 to 180 ms after nose poke entry.
# - The impulse onsets differ between rats (50.25 and 60.25 ms for the second impulse in 18FB,
#   18Ri and 18Ro sessions; 47.25 and 57.25 ms in others); each session's own onsets are used.
# - Withdrawal times (nose poke duration minus onset delay) and the descriptor's trial fields are
#   consistent with the Methods: delays 75 to 99 ms, completed trials all held over 250 ms.

'''
assert anchor in s; s=s.replace(anchor, add+anchor)
anchor2='''# %% [markdown]
# ## Behaviour (Figure 2)'''
add2='''# %% [markdown]
# The response to impulse 2 is earlier in F-first sequences in 61 of 80 sessions (sign test
# p = 2.7e-06), and a window before onset shows no difference (35 of 80, p = 0.31): consistent with
# spikes and trial table sharing one clock. By rat this holds in 10 to 17 sessions of 12 to 22, and
# in 18Ro in 11 of 19, where the check is weak.

'''
assert anchor2 in s; s=s.replace(anchor2, add2+anchor2)
s += '''
# %% [markdown]
# ## Summary
#
# A failure to reproduce here may be a failure of this attempt, not of the paper: see the
# reasoning and the differences from the paper's method.
#
# | claim | outcome |
# |---|---|
# | fig2ab-fms-smf-not-discriminated | partially reproduced (5 of 8 rats; 62SC not in the data) |
# | training-days | partially reproduced (minimum 11 days, not 8) |
# | fig2c-choice-follows-mean-speed | reproduced |
# | fig2d-fixed-panel-impairs | blocked, data_missing |
# | dprime-fff-sss-range | partially reproduced (highest 1.09, not 1.5) |
# | fig3-fsfs-sffs-intensity-only | reproduced (S1 Data) |
# | units-recorded | reproduced (but 506 units against 473) |
# | baseline-rates | partially reproduced (RS maximum 11.4 Hz) |
# | temporal-modulation-count | reproduced |
# | modulated-higher-baseline | reproduced |
# | fig4d-evoked-modulation-by-layer | partially reproduced |
# | latency-by-layer | partially reproduced (ordering only) |
# | fig4d-gradual-decrease | not reproduced (L5a also decreases) |
# | fig6-regression-significant | reproduced |
# | fig6e-unit-classes | partially reproduced (Slow Negative 51) |
# | fig6fg-laminar-classes | partially reproduced (4 of 6) |
# | fig7c-fast-impulse-velocity | reproduced |
# | fig7c-fast-sequence-rate | reproduced (10-ms baseline reading) |
# | fig7-fff-adaptation | partially reproduced |
# | fig7-sss-no-adaptation | reproduced |
# | s4-fms-middle-pulse | reproduced |
# | fig7de-medium-suppressed | partially reproduced (no suppression) |
# | fig8a-slow-positive-no-sequence-difference | partially reproduced (S response too) |
# | fig8b-slow-negative-no-impulse-response | reproduced |
# | fig8d-slow-positive-right-choice-l5 | partially reproduced (L5b only) |
# | fig8d-fast-medium-no-choice-bias | reproduced |
# | fig8e-choice-divergence-125ms | reproduced |
# | s5-slow-positive-no-integration | reproduced |
# | s6-head-position-choice | reproduced (S2 Data) |
# | s7-no-fs-l5-slow-positive | reproduced |
#
# The decoder claims of Figure 9 are in `decoders.ipynb`.
#
# How the analysis differs from the paper's: behaviour rests on the five recorded rats, not
# eight; units are all 506 deposited, not the paper's 473, since the columns to drop cannot be
# identified; the temporally modulated units are recomputed (reading a) and agree with the stored
# p-values for 73% of units, so downstream classes differ from the data set's labels for some
# units (shown as variants); impulse-responsive units are selected by a paired t test across
# trials, which selects 34 Fast RS units where the paper has 61.
#
# What was found about the data set: the column map (`MapPosition`) the descriptor documents is
# missing, so 33 units beyond the paper's 473 cannot be removed; the stored temporal-modulation
# p-values use a -50 to 300 ms window, not the Methods' window; the fixed-panel sessions and three
# behaviour-only rats are not deposited; the stored regression inputs show that completed trials
# were analysed; no recording is deposited twice; spikes and trials share one clock.
'''
open(p,'w').write(s)
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='nb1.py'; s=open(p).read()
a='''# - The impulse onsets differ between rats (50.25 and 60.25 ms for the second impulse in 18FB,
#   18Ri and 18Ro sessions; 47.25 and 57.25 ms in others); each session's own onsets are used.'''
b='''# - The impulse onsets differ between sessions: in 32 sessions (18FB, 18Ri, 18Ro) the second
#   impulse starts at 50.25 or 60.25 ms, in 48 (all rats but 18FB) at 47.25 or 57.25 ms; each
#   session's own onsets are used.'''
assert a in s; s=s.replace(a,b); open(p,'w').write(s)
R = {
"fig9b-stimulus-decoder-fast-medium": "**Result: reproduced.** With C = 1 (reading a, 300 repeats) the Fast/Medium decoder is 84.1% correct overall, 74.9% for FMS and 84.4% for FFF, and 82.1% on FMS and SMF (reading A; 97.6% under reading B), all within tolerance. With C chosen by cross-validation (5 repeats) it is 76.0% overall and 62.2% for FMS. The data set's labels give 87.1% (100 repeats).",
"fig9c-best-units-short-windows": "**Result: reproduced.** Units with a 5-ms best window have the highest mean single-unit accuracy (32.7%, 10 ms 31.5%, longer windows 27.2 to 30.9%), and 17 of the 21 top-ranked units have 5 or 10 ms windows.",
"fig9b-stimulus-decoder-slow-chance": "**Result: reproduced.** The Slow decoder is 30.1% correct (C = 1, 300 repeats), within tolerance of 32%, and not different from chance by the fraction of repeats (p = 0.213, reading a). The binomial test on 120,000 pooled pseudo-trials (reading b) is significant (p near 0), as any small excess over 25% is with that many draws. With C by cross-validation it is 28.9%, significant by both tests.",
"fig9d-single-bin-decoder": "**Result: reproduced.** With one 150-ms bin the Fast/Medium decoder falls to 39.4% (within tolerance of 43%) and the Slow decoder to 26.5%, 3.6 points below its 10-ms value, not above it. With C by cross-validation the values are 28.9% and 24.9%.",
"fig9e-temporal-pattern-decoding": "**Result: reproduced.** Rate-normalized trains give 79.4% (within tolerance of 80%), time-scrambled trains 28.9%, not above chance by the fraction of repeats (p = 0.367) and below 32%. With C by cross-validation, 72.1% and 28.3%.",
"fig9f-choice-decoder": "**Result: not reproduced.** The Slow choice decoder predicts choice far better than 65%: 80.1% from the 150-ms bin and 91.7% from the 100 ms before withdrawal (equal draws, mean over sequences; 74.6% and 79.2% with C by cross-validation), and the Fast/Medium decoder is not unable (67.1% and 79.0%). Trained without balancing the two choices, both decoders fall to 50 to 54%. None of the readings gives Slow at 65% with Fast/Medium near 50%.",
"fig9g-l5b-slow-positive-best-choice": "**Result: reproduced.** L5b Slow Positive units have the highest mean single-unit choice accuracy (59.8%, 15 units; next L5a Slow Positive 56.4%, L5b Slow Negative 55.4%), and 5 of the 11 top-ranked units are L5b Slow Positive, the largest group but not more than half.",
}
p='nb2.py'; s=open(p).read()
import re
lines=s.split('\n'); out=[]; pending=None
for l in lines:
    if l.startswith('# %%') and pending:
        out += ['# %% [markdown]', '# '+R[pending], '']; pending=None
    m=re.match(r'# %% tags=claim:(\S+)',l)
    if m: pending=m.group(1)
    out.append(l)
if pending: out += ['# %% [markdown]', '# '+R[pending], '']
s='\n'.join(out)
s+='''
# %% [markdown]
# ## Summary
#
# A failure to reproduce here may be a failure of this attempt, not of the paper: see the
# reasoning and the differences from the paper's method.
#
# | claim | outcome |
# |---|---|
# | fig9b-stimulus-decoder-fast-medium | reproduced |
# | fig9c-best-units-short-windows | reproduced |
# | fig9b-stimulus-decoder-slow-chance | reproduced |
# | fig9d-single-bin-decoder | reproduced |
# | fig9e-temporal-pattern-decoding | reproduced |
# | fig9f-choice-decoder | not reproduced |
# | fig9g-l5b-slow-positive-best-choice | reproduced |
#
# How the analysis differs from the paper's: the units are this attempt's classes (208
# Fast/Medium, 102 Slow) from all 506 deposited units; the population decoder draws 100
# pseudo-trials per class per repeat; the cross-validated penalty (reading b) is run with 5 to 10
# repeats; the choice decoder weights the two choices equally in training (an assumption), as the
# unweighted fit predicts one side for every trial.
'''
open(p,'w').write(s)
print(s.count('**Result:'))
EOF
```

```
7
Shell cwd was reset to
```

**Agent**

Building the entry: notebooks, `entry.yaml`, requirements, README.

**Agent calls Bash**

```bash
cd entries/mcguire-2016 && sed -i '/^import matplotlib.pyplot as plt$/d' $TMPDIR/nb1.py && . $TMPDIR/dev/bin/activate && python $TMPDIR/build.py $TMPDIR/nb1.py reproduce_mcguire_2016.ipynb && python $TMPDIR/build.py $TMPDIR/nb2.py decoders.ipynb && cat > requirements.in <<'EOF'
aiohttp
fsspec
numpy
openpyxl
pandas
requests
scikit-learn
scipy
statsmodels
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: mcguire-2016
type: reproduction
title: Short time-scale coding in rat S1 during whisker sequence discrimination (McGuire et al. 2016)
description: Tests the findings of McGuire, Telian, Laboy-Juarez et al. (2016) on CRCNS ssc-4, which
  holds the spike times and trial data of 80 recording sessions in the five recorded rats. It
  checks the behaviour of those rats, the unit counts, baseline rates, temporal modulation, impulse
  responses by layer, the regression on integrated panel speed that classes units as Fast, Medium,
  Slow Positive and Slow Negative, the responses and choice coding of each class, and the
  population decoders of stimulus and choice. Two claims are tested on the paper's supporting data.
license: Apache-2.0
notebooks:
- path: reproduce_mcguire_2016.ipynb
  title: Behaviour, units, regression classes and responses (Figures 2 to 8)
  runtime_minutes: 2
- path: decoders.ipynb
  title: Stimulus and choice decoders (Figure 9)
  runtime_minutes: 16
helpers:
- ssc4.py
related:
- id: crcns:ssc-4/unversioned
  relation: uses_data
- id: doi:10.1371/journal.pbio.1002549
  relation: reproduces
EOF
cat > README.md <<'EOF'
# McGuire et al. (2016) on CRCNS ssc-4

Tests the claims in `claims/mcguire-2016.yaml` on the CRCNS data set ssc-4 (doi:10.6080/K06D5QXN),
the file `AllRats.mat`, streamed from the public CRCNS bucket and pinned by its MD5 sum. Two claims
use the paper's supporting data (S1 and S2 Data).

- `reproduce_mcguire_2016.ipynb`: data checks, behaviour, units, regression classes and the
  responses of each class (Figures 2 to 8, S2 to S7).
- `decoders.ipynb`: the population decoders of Figure 9.
- `ssc4.py`: loading and the shared measures.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.
EOF
cat ../../targets/crcns.json 2>/dev/null | head -20; ls ../../papers/datasets/ | grep -i mcg; cat ../../papers/datasets/mcguire-2016.yaml 2>/dev/null
```

```
107 cells
26 cells
{
 "schema_version": 1,
 "archive": "crcns",
 "generated": "2026-11-06T21:36:03+00:00",
 "source": "https://crcns.org/data-sets (each data set's About page) and DataCite, chosen by hand; files in s3://crcnsarchive (us-west-2)",
 "note": "Chosen by hand from a scan of CRCNS of 2026-11-04: data sets whose About page names the paper of a finding, small ones first, and those whose paper is also a DANDI target, to compare the two copies. ret-1 was the first, to test the pipeline beyond DANDI.",
 "counts": {
  "with_a_paper": 88
 },
 "targets": [
  {
   "id": "ret-1",
   "name": "Multi-electrode recordings from retinal ganglion cells",
   "url": "https://crcns.org/data-sets/retina/ret-1",
   "doi": "10.6080/K0RF5RZT",
   "published_version": null,
   "asset_count": 4,
   "size_gb": 0.07,
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd  && . $TMPDIR/dev/bin/activate && python tools/entry.py lock entries/mcguire-2016 2>&1 | tail -5 && python tools/entry.py check entries/mcguire-2016 2>&1 | tail -20
```

```
Wed Nov 11 17:41:29 UTC 2026
wrote mcguire-2016/requirements.lock.txt (Python 3.13, with hashes)
0 error(s)
```

**Agent**

Lock and check pass. Running the entry from a clean environment (about 18 min).

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && time python tools/entry.py all entries/mcguire-2016 2>&1 | tail -15
```

```
Installed kernelspec registry-mcguire-2016 in executed/mcguire-2016/.venv/share/jupyter/kernels/registry-mcguire-2016
0 error(s)
pass  reproduce_mcguire_2016.ipynb  (106 s)
pass  decoders.ipynb  (925 s)

real	17m19.232s
user	17m9.187s
sys	0m5.835s
```

**Agent**

Both notebooks pass (106 s and 925 s). Checking that the executed outputs match the numbers in the conclusions.

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF'
import nbformat, re
for nb, ref in [('executed/mcguire-2016/reproduce_mcguire_2016.ipynb','/tmp/claude-1001/nb1.out'),('executed/mcguire-2016/decoders.ipynb','/tmp/claude-1001/nb2.out')]:
    n=nbformat.read(nb,4)
    txt=''.join(o.get('text','') for c in n.cells if c.cell_type=='code' for o in c.get('outputs',[]) if o.get('output_type')=='stream' and o.get('name')=='stdout')
    txt+= ''.join(str(o.get('data',{}).get('text/plain','')) for c in n.cells if c.cell_type=='code' for o in c.get('outputs',[]))
    errs=[o for c in n.cells if c.cell_type=='code' for o in c.get('outputs',[]) if o.get('output_type')=='error']
    ref_lines=[l.strip() for l in open(ref) if l.strip() and 'Warning' not in l and 'warn' not in l and '(' not in l[:3]]
    missing=[l for l in ref_lines if l not in txt and not l.startswith('/tmp') and not re.search(r'\(\d+ s\)', l) and 'run time' not in l]
    print(nb, 'errors', len(errs), 'ref lines missing', len(missing)); print('\n'.join(missing[:15]))
EOF
```

```
executed/mcguire-2016/reproduce_mcguire_2016.ipynb errors 0 ref lines missing 30
FFF, classes cls, one-sided, baseline 25 ms
FFF, classes cls, one-sided, baseline 10 ms
FFF, classes cls, two-sided, baseline 25 ms
FFF, classes cls, two-sided, baseline 10 ms
FFF, classes cls_dep, one-sided, baseline 25 ms
FFF, classes cls_dep, one-sided, baseline 10 ms
FFF, classes cls_dep, two-sided, baseline 25 ms
FFF, classes cls_dep, two-sided, baseline 10 ms
FFF, classes cls, all Fast RS-sided, baseline 25 ms
FFF, classes cls, all Fast RS-sided, baseline 10 ms
SSS, classes cls, one-sided, baseline 25 ms
SSS, classes cls, one-sided, baseline 10 ms
SSS, classes cls, two-sided, baseline 25 ms
SSS, classes cls, two-sided, baseline 10 ms
SSS, classes cls_dep, one-sided, baseline 25 ms
executed/mcguire-2016/decoders.ipynb errors 0 ref lines missing 0
```

**Agent**

Executed outputs match the development run; the only differences are three print labels I renamed. Now the questions file and the attempt record.

**Agent calls Bash**

```bash
cd  for f in bruno-2017 deweese-2004 gu-2011 rodgers-2014; do [ -f questions/$f.yaml ] && head -5 questions/$f.yaml && echo; done; ls attempts | grep mcguire; grep -n "questions" tools/entry.py | head
```

```
questions:
- claim: culling-controls
  question: Does the paper's random culling control apply the 10-trial tone criterion again after
    the random removal? The criterion says "the tone criteria are then applied". Read that way, a
    control that removes as many trials per tone as LFP-based culling drops exactly the tones that

# Questions from attempt gu-2011-01 (author, 2026-11-06) about the claims file
# claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml. Each was raised by the round-2 verifier
# and is asked under docs/protocol.md, "Hand over for verification"; the claims are tested as
# written.
questions:

questions:
- claim: fig4ab-a1-example-units
  asked: 2026-11-06
  question: The criterion names the units as metadata/figures_generated_by_each_script.csv gives
    them, 4A CR20B_120602_001_behaving-612 and 4B CR20B_120602_001_behaving-712, and compares unit A
```

**Agent calls Write**

```json
{
 "file_path": "questions/mcguire-2016.yaml",
 "content": "# Questions from attempt mcguire-2016-01 (author, 2026-11-11) about the claims file\n# claims/mcguire-2016.yaml. The claims are tested as written.\nquestions:\n- claim: fig2d-fixed-panel-impairs\n  asked: 2026-11-11\n  question: The claim has the default `data` (the data set), but CRCNS ssc-4 holds no fixed-panel\n    trials, while the paper's S2 Data (doi:10.1371/journal.pbio.1002549.s002, sheet \"Fig S2\",\n    section S2B) gives each rat's FFF minus SSS right-choice fraction for moving-panel and\n    fixed-panel trials, the values the S2B Fig paired t test uses. Should the claim be `data:\n    elsewhere` with `where` naming S2 Data, as fig3-fsfs-sffs-intensity-only and\n    s6-head-position-choice are?\n  passage: S2 Fig legend, \"B, Behavioral effect of fixed panel trials ... Discrimination was\n    reduced on fixed panel trials (p = 0.012, two-sided paired t test) ... Data are in S2 Data\";\n    Figure 2 legend, \"Data for this figure are in S1 Data\".\n  why: As written the claim is blocked (data_missing), since the data set lacks the fixed-panel\n    sessions. Tested on S2 Data, which the attempt shows as a variant, fixed-panel discrimination\n    is lower in all six rats and the paired t test gives p = 0.0120 with the rat at 0 kept (0.0308\n    without it), so the claim would be testable and would match the paper under reading (ii), and\n    the criterion's readings (a) to (c) of the comparison could not all be told apart from these\n    summaries.\n"
}
```

```
File created successfully at: questions/mcguire-2016.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "attempts/mcguire-2016-01.yaml",
 "content": "schema_version: 3\nid: mcguire-2016-01\ndatasets:\n- archive: crcns\n  id: ssc-4\n  version: unversioned\n  doi: 10.6080/K06D5QXN\n  relation: primary\npaper: doi:10.1371/journal.pbio.1002549\ndate: 2026-11-11\nentry: mcguire-2016\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-14\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/43061505476\ninputs:\n- what: S1 Data of the paper (XLSX), sheets \"Fig 2\" (per-rat right-choice fractions of all eight\n    rats, used as variants) and \"Fig 3\" (per-session percent correct and per-rat d-prime of the\n    FSFS-SFFS rats, used for fig3-fsfs-sffs-intensity-only). Streamed from PLOS, MD5\n    78f680d6b80ca361f25e2b5c6b8e8f78 when read.\n  source: doi:10.1371/journal.pbio.1002549.s001\n- what: S2 Data of the paper (XLSX), sheets \"Fig S2\" (per-rat moving and fixed-panel\n    discrimination, shown as a variant for the blocked fig2d-fixed-panel-impairs) and \"Fig S6\"\n    (per-frame mean and SEM of head and whisker tracking by choice, used for\n    s6-head-position-choice). Streamed from PLOS, MD5 2cc739cf12afcaeaa5cad2831b470a12 when read.\n  source: doi:10.1371/journal.pbio.1002549.s002\noutcomes:\n- claim: fig2ab-fms-smf-not-discriminated\n  outcome: partially_reproduced\n  notebook: reproduce_mcguire_2016.ipynb\n  output: claim:fig2ab-fms-smf-not-discriminated\n  notes: The data set holds five of the eight rats (18FB, 18Ri, 18Ro, 62BS, 107St). In all five,\n    FFF draws more right choices than SSS (0.537 to 0.698 against 0.234 to 0.390) and FMS and SMF\n    lie between, and FMS against SMF is not significant at 0.00625 (smallest p 0.10 by the z test\n    and 0.11 by the continuity-corrected chi-square, 62BS). Both trial readings select the same\n    14186 trials. Rat 62SC, the one the paper finds discriminating, is not in the data set, so\n    that part cannot be tested; the criterion caps the outcome at partial for fewer than eight\n    rats. The data set's per-rat means over sessions equal the S1 Data values for four rats and\n    differ by up to 0.026 for 18FB.\n  deviations:\n  - Five of eight rats; the three behaviour-only rats are not deposited.\n- claim: training-days\n  outcome: partially_reproduced\n  notebook: reproduce_mcguire_2016.ipynb\n  output: claim:training-days\n  measured:\n  - 14.8\n  - 11\n  - 20\n  notes: Distinct recording dates per rat are 11 (18FB), 12 (18Ri, 107St), 19 (18Ro) and 20 (62BS);\n    mean 14.8, s.d. 4.3. The mean and the maximum are within tolerance, the minimum (11) is not\n    within 0.8 of 8. The data set holds only the recording days of the five recorded rats, and the\n    shortest-trained rats may be among the three not deposited.\n  deviations:\n  - Five of eight rats, and only days with a deposited recording session.\n- claim: fig2c-choice-follows-mean-speed\n  outcome: reproduced\n  notebook: reproduce_mcguire_2016.ipynb\n  output: claim:fig2c-choice-follows-mean-speed\n  notes: For each of the five rats relative right choice orders FFF above FMS and SMF above SSS\n    (reading a), and the Pearson correlation with Table 1 mean speed is 0.967 to 0.998 (reading\n    b), under both trial readings. The S1 Data means of all eight rats give the same (r 0.967 to\n    0.995).\n  deviations:\n  - Five of eight rats in the data set; all eight shown from S1 Data as a variant.\n- claim: fig2d-fixed-panel-impairs\n  outcome: blocked\n  blocked_by: data_missing\n  notebook: reproduce_mcguire_2016.ipynb\n  notes: The data set holds only the four normal sequences (StimNumber 1 to 4, including the trials\n    with irregular StimName strings, which map one to one to them); no fixed-panel session is\n    deposited. The paper's S2 Data holds the per-rat summary of S2B Fig; as a variant, fixed-panel\n    discrimination is lower in all six rats there, paired t p = 0.0120 with the rat at 0 kept and\n    0.0308 without it. Whether the claim should be tested on S2 Data is asked of a reader\n    (questions/mcguire-2016.yaml).\n- claim: dprime-fff-sss-range\n  outcome: partially_reproduced\n  notebook: reproduce_mcguire_2016.ipynb\n  output: claim:dprime-fff-sss-range\n  measured:\n  - 0.45\n  - 1.09\n  notes: Per-rat d-prime over pooled sessions (reading a) is 0.45 (18FB) to 1.09 (18Ro), and the\n    mean of per-session values (reading b) 0.46 to 1.23. The lowest value is within tolerance of\n    0.5; the highest is below 1.35 under both readings. Of the three rats not deposited, two have\n    the highest d-prime by the S1 Data means (62SS 1.32, 107Si 1.17).\n  deviations:\n  - Five of eight rats.\n  - Rates of 0 or 1 in a session are moved by half a trial before the z transform, a standard\n    choice.\n- claim: fig3-fsfs-sffs-intensity-only\n  outcome: reproduced\n  notebook: reproduce_mcguire_2016.ipynb\n  output: claim:fig3-fsfs-sffs-intensity-only\n  measured:\n  - 69.98\n  - 69.17\n  - 51.74\n  - 53.02\n  - 1.004\n  - 0.130\n  notes: From the per-session values of S1 Data, 58B is 69.98 +- 1.47% correct (13 sessions) and\n    60W 69.17 +- 1.57% (15) with different intensities, and 51.74 +- 0.81% (22) and 53.02 +- 0.82%\n    (21) with the same intensity, with same-intensity sessions up to day 56 and 52. D-prime as the\n    mean of the two rats (reading a) is 1.004 and 0.130; per rat 1.061 and 0.947, 0.168 and 0.093\n    (reading b, outside tolerance for single rats). All six values are within tolerance under\n    reading a.\n- claim: units-recorded\n  outcome: reproduced\n  notebook: reproduce_mcguire_2016.ipynb\n  output: claim:units-recorded\n  measured:\n  - 330\n  - 176\n  - 80\n  - 5\n  - 4.12\n  - 12\n  notes: 330 single units (257 RS, 73 FS) and 176 multi-unit clusters, 506 in all, over 80 sessions\n    in five rats; 4.12 single units per session, 0 to 12. Each value is within its tolerance, but\n    the total is 33 above the paper's 473. The descriptor says units in columns A1 and B2 are to\n    be dropped using MapPosition, which the file lacks; leaving out the fifth electrode of 18FB and\n    18Ri gives 459, not 473.\n- claim: baseline-rates\n  outcome: partially_reproduced\n  notebook: reproduce_mcguire_2016.ipynb\n  output: claim:baseline-rates\n  measured:\n  - 5.93\n  - 11.40\n  - 7.59\n  - 30.18\n  notes: Layer means of the 25-ms baseline over completed trials are 5.93 (L2/3) to 11.40 Hz (L5a)\n    for RS single units and 7.59 (L2/3) to 30.18 Hz (L5b) for FS. The RS maximum is above 11 Hz;\n    the other bounds are within tolerance. Multi-units are higher than RS in 5 of 5 layers and\n    higher than both RS and FS in 4 of 5. With all trials the RS maximum is 11.49 Hz.\n  deviations:\n  - All 506 deposited units, not the paper's 473.\n- claim: temporal-modulation-count\n  outcome: reproduced\n  notebook: reproduce_mcguire_2016.ipynb\n  output: claim:temporal-modulation-count\n  measured:\n  - 310\n  - 61.3\n  notes: With 0 to 180 ms after nose poke entry (reading a) 310 of 506 units (61.3%) are modulated;\n    with 0 to 180 ms after onset (reading b) 261 (51.6%). The two statistics the criterion names\n    give the same p-value under uniform permutation, so they are one reading. The data set's\n    stored p-values also mark 310 units, but they agree with reading a unit by unit for 73.1%,\n    and they were computed over -50 to 300 ms (TempSig.Params); that window gives 363 units here,\n    agreeing on 81.6%. Units modulated by reading a are used by every claim that depends on this\n    one.\n  deviations:\n  - 506 units in the denominator, not 473.\n  - Spikes are permuted uniformly within the window on each trial (the criterion's standard\n    choice), drawn as a multinomial over the pooled bins, which is the same null.\n- claim: modulated-higher-baseline\n  outcome: reproduced\n  notebook: reproduce_mcguire_2016.ipynb\n  output: claim:modulated-higher-baseline\n  notes: Modulated RS single units have the higher baseline in 5 of 5 layers (for example L4 10.13\n    against 6.08 Hz, L6 11.10 against 3.00 Hz). The fraction modulated is 0.51 to 0.68 across\n    layers, chi-square p = 0.105. Columns cannot be tested, as the column map is missing.\n- claim: fig4d-evoked-modulation-by-layer\n  outcome: partially_reproduced\n  notebook: reproduce_mcguire_2016.ipynb\n  output: claim:fig4d-evoked-modulation-by-layer\n  measured:\n  - 16.06\n  - 15.29\n  - 7.65\n  - 16.56\n  - 8.20\n  notes: No combination of the criterion's readings puts all five layers within tolerance. The\n    closest, the absolute peak averaged over impulses (A, b, ii), gives 16.06, 15.29, 7.65, 16.56\n    and 8.20 Hz, 4 of 5 within tolerance (L5a outside); measured gives it. The signed peak over\n    pooled impulses (A, a, i) gives 9.17, 11.71, -1.85, 10.42 and -0.33 Hz, and the 5 to 35 ms mean\n    (B) 1.4 to 7.8 Hz. L5a and L6 are the two lowest layers under every combination. Units per\n    layer 27 to 77. With the stored temporal-modulation p-values the values are similar.\n  deviations:\n  - The 10-ms boxcar is centred, a standard choice.\n- claim: latency-by-layer\n  outcome: partially_reproduced\n  notebook: reproduce_mcguire_2016.ipynb\n  output: claim:latency-by-layer\n  measured:\n  - 15.0\n  - 16.5\n  - 15.0\n  - 17.0\n  - 17.0\n  notes: Peak latencies are 14 to 20 ms in every layer, longer than the paper's 9.8 to 16.1 ms; at\n    most one layer is within tolerance under any reading. The ordering (L4, L5a and L5b below L2/3\n    and L6) holds for the medians under both tests and for the mean under the two-sided test, not\n    for the mean under the one-sided test. Measured gives the one-sided medians in the claim's\n    order (L4, L5a, L5b, L2/3, L6). 18 to 50 impulse-responsive units per layer. The paper's\n    latency definition (time of the maximum after onset, 10-ms smoothing) may differ from the one\n    used here in a way the text does not show; this is asked of the authors (findings).\n  deviations:\n  - The impulse t test compares, per trial, the 5 to 35 ms rate with the 0 to 10 ms rate, averaged\n    over the trial's three impulses, across trials (Methods, Stimulus-evoked responses, \"by t\n    test\").\n- claim: fig4d-gradual-decrease\n  outcome: not_reproduced\n  notebook: reproduce_mcguire_2016.ipynb\n  output: claim:fig4d-gradual-decrease\n  notes: The population rate of modulated units falls in every layer, L5a included. The slope from\n    -25 to 180 ms is -0.88 Hz per 100 ms in L5a (p below 0.001) and -1.09 to -2.43 in the other\n    layers (reading a), and the last 30 ms are below the baseline in all five layers, by 1.65 Hz in\n    L5a (reading b). The claim requires no decrease in L5a.\n- claim: fig6-regression-significant\n  outcome: reproduced\n  notebook: reproduce_mcguire_2016.ipynb\n  output: claim:fig6-regression-significant\n  measured: 194\n  notes: 194 of the 310 modulated units have a regression at p < 0.05/36 in at least one window\n    (207 among the units the stored p-values mark). With rates per trial in place of summed counts,\n    189. The fit reproduces the data set's stored R2 and p for every unit to numerical precision.\n  deviations:\n  - The regressor is the data set's stored integrated speed (Xval), the stimulus record the\n    criterion allows; the dependent variable is the spike count summed over completed trials, as\n    the stored inputs show.\n- claim: fig6e-unit-classes\n  outcome: partially_reproduced\n  notebook: reproduce_mcguire_2016.ipynb\n  output: claim:fig6e-unit-classes\n  measured:\n  - 160\n  - 48\n  - 51\n  - 51\n  - 51.6\n  - 42.9\n  notes: Classing all modulated units by their highest-R2 window (reading a, 55 ms Slow) gives 160\n    Fast, 48 Medium, 51 Slow Positive and 51 Slow Negative; with 55 ms Medium 160, 50, 50, 50.\n    Slow Negative is above its limit of 48.4 in both; the other counts, the Fast share (51.6%) and\n    the share with 5 to 10 ms windows (42.9%) are within tolerance. 93% of Fast units have\n    positive slopes and 69% of Medium units negative. Reading b (significant units only) gives\n    119, 26, 23 and 26. The data set's own labels give 160, 53, 51 and 46, all within tolerance;\n    over units modulated in both, this attempt's classes agree with them for 99.6%.\n- claim: fig6fg-laminar-classes\n  outcome: partially_reproduced\n  notebook: reproduce_mcguire_2016.ipynb\n  output: claim:fig6fg-laminar-classes\n  measured:\n  - 69.2\n  - 50.7\n  - 26.5\n  - 18.3\n  - 33.3\n  - 54.4\n  notes: Under reading a, 4 of 6 values are within tolerance (L6 Fast 26.5% and L2/3 with L4 Slow\n    18.3% outside) and Fast falls and Slow rises from superficial to deep. Separately, L2/3 is 59.3%\n    Fast and L4 72.7%. The data set's labels give 74.0, 49.6, 23.2, 13.0, 31.9 and 56.5%, all\n    within tolerance.\n- claim: fig7c-fast-impulse-velocity\n  outcome: reproduced\n  notebook: reproduce_mcguire_2016.ipynb\n  output: claim:fig7c-fast-impulse-velocity\n  notes: Over 160 Fast units the net evoked rate is 9.59 Hz for F, 8.73 for M and 7.42 for S\n    impulses (SEM 0.77 to 0.88); paired t F against S, t = 4.48, p = 1.4e-05. The data set's\n    labels give 9.99, 8.54 and 7.77 Hz. In 18Ri M is above F and in 107St S above M.\n- claim: fig7c-fast-sequence-rate\n  outcome: reproduced\n  notebook: reproduce_mcguire_2016.ipynb\n  output: claim:fig7c-fast-sequence-rate\n  notes: With the 0 to 10 ms baseline (reading b) Fast units give FFF 4.62, FMS 2.09, SMF 2.85 and\n    SSS 1.59 Hz above baseline, FMS against SMF p = 0.31. With the 25-ms baseline (reading a) the\n    order is the same but FMS and SMF differ at p = 0.046 (difference 0.95 Hz). The claim holds\n    under reading b.\n- claim: fig7-fff-adaptation\n  outcome: partially_reproduced\n  notebook: reproduce_mcguire_2016.ipynb\n  output: claim:fig7-fff-adaptation\n  measured:\n  - 0.794\n  - 0.800\n  notes: The impulse t test selects 34 of 63 Fast RS single units as F-responsive, not 61. Over\n    them the ratio of population means (reading b) is 0.794 (2/1) and 0.800 (3/1) with the 25-ms\n    baseline, and 0.79 to 0.83 under the other selections and baselines, within tolerance. The\n    per-unit ratio against 1 is significant for 2/1 (p = 0.026) but not for 3/1 (p = 0.644), and\n    the paired tests are not significant (p 0.119 to 0.185). The mean of per-unit ratios is\n    unstable where pulse 1 is near 0 (with the 10-ms baseline it is of order 1e13). With all 63\n    Fast RS units, a count close to the paper's 61, the ratios of means are 0.70 and 0.77 and the\n    paired test gives p = 0.039 for 2/1 and 0.141 for 3/1.\n  deviations:\n  - Per-unit ratios are taken only where the pulse 1 response is above 0 (28 of 34 units).\n- claim: fig7-sss-no-adaptation\n  outcome: reproduced\n  notebook: reproduce_mcguire_2016.ipynb\n  output: claim:fig7-sss-no-adaptation\n  measured:\n  - 0.883\n  - 0.881\n  notes: In SSS the ratios of population means are 0.883 and 0.881 (one-sided selection, 25-ms\n    baseline) and 0.85 to 0.88 under the other selections, within tolerance; no test differs from\n    1 or pulse 1 (all p above 0.2). The mean of per-unit ratios is 1.34 and 1.66 with the 25-ms\n    baseline (3/1 outside tolerance) and 0.84 and 0.76 with the 10-ms baseline.\n- claim: s4-fms-middle-pulse\n  outcome: reproduced\n  notebook: reproduce_mcguire_2016.ipynb\n  output: claim:s4-fms-middle-pulse\n  notes: In the 34 selected units the pulse 2 response is 1.60 Hz lower in FMS than in SMF with the\n    25-ms baseline (paired t p = 0.259) and 0.20 Hz lower with the 10-ms one (p = 0.913). With all\n    63 Fast RS units it is 1.60 Hz lower, p = 0.087.\n- claim: fig7de-medium-suppressed\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_mcguire_2016.ipynb\n  output: claim:fig7de-medium-suppressed\n  notes: The 48 Medium units do not distinguish F from S impulses (p = 0.637) or FFF from SSS\n    (p = 0.428 and 0.468), but impulses do not suppress them; net evoked rates are +0.05 (F), -0.30\n    (M) and -0.36 Hz (S), none different from 0 (p above 0.6). Their sequence rates are 1.5 to 4.1\n    Hz below the pre-stimulus baseline, which the gradual decline of all layers can explain. With\n    the data set's labels (53 units) all three impulse values are negative (-0.27 to -0.52 Hz,\n    none significant), which would meet the criterion.\n  deviations:\n  - Classes are this attempt's (reading a of fig6e-unit-classes, 55 ms Slow), adopted because the\n    paper's four counts sum to all 305 modulated units and the Figure 6D legend puts Fast and\n    Medium below 55 ms. The outcome rests on this choice; the data set's labels are shown as a\n    variant.\n- claim: fig8a-slow-positive-no-sequence-difference\n  outcome: partially_reproduced\n  notebook: reproduce_mcguire_2016.ipynb\n  output: claim:fig8a-slow-positive-no-sequence-difference\n  notes: The 51 Slow Positive units respond to F (1.46 Hz, p = 0.0016) and M impulses (2.82 Hz,\n    p = 0.00018) but also to S impulses (1.23 Hz, p = 0.027), which the claim says they do not.\n    Their sequence rates do not differ (repeated-measures ANOVA p = 0.087 and 0.430 for the two\n    baselines). Responses grow over the pulses (-0.76, 1.87 and 5.57 Hz above the 25-ms baseline\n    for pulses 1 to 3). The data set's labels give the same pattern (S p = 0.021).\n- claim: fig8b-slow-negative-no-impulse-response\n  outcome: reproduced\n  notebook: reproduce_mcguire_2016.ipynb\n  output: claim:fig8b-slow-negative-no-impulse-response\n  notes: In 51 Slow Negative units no impulse kind gives a significant increase (t = 1.88, -0.96\n    and 0.89 for F, M and S), and the population rate falls by 5.49 Hz per 100 ms over 0 to 180\n    ms. The data set's labels give the same.\n- claim: fig8d-slow-positive-right-choice-l5\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_mcguire_2016.ipynb\n  output: claim:fig8d-slow-positive-right-choice-l5\n  notes: L5b Slow Positive units (15) fire more on right-choice trials, by 6.32 Hz (p = 0.0045,\n    reading a) and 7.24 Hz (p = 0.0008, reading b); L2/3, L4 and L6 show no significant bias. In\n    L5a (6 units) the bias is 4.27 Hz, p = 0.117 and 0.121, not significant. With the data set's\n    labels (7 L5a units) L5a reaches p = 0.049 under reading a, where the criterion would be met.\n    The printed p-values here (0.0045, 0.0008) are not the paper's (0.022, 9.5e-4, 7.5e-5). Fast\n    and Medium units, a variant, show right-choice bias in L4 (p = 0.018) and L5b (p = 0.024)\n    under reading a.\n  deviations:\n  - Classes are this attempt's, as for fig7de-medium-suppressed; the outcome rests on that\n    choice, as the data set's labels give the claim under reading a.\n- claim: fig8d-fast-medium-no-choice-bias\n  outcome: reproduced\n  notebook: reproduce_mcguire_2016.ipynb\n  output: claim:fig8d-fast-medium-no-choice-bias\n  notes: In 56 L4 Fast units, with 5-ms bins (reading b) no bin from 0 to 150 ms differs between\n    right- and left-choice trials. With 10-ms windows stepped by 1 ms (reading a), steps at 5 to 9\n    ms reach p < 0.05, a brief run that does not last to the end of the sequence. The largest\n    right-left difference is 2.6 to 2.7 Hz.\n- claim: fig8e-choice-divergence-125ms\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_mcguire_2016.ipynb\n  output: claim:fig8e-choice-divergence-125ms\n  measured:\n  - 122\n  - 153\n  - 193.0\n  notes: In 21 L5 Slow Positive units, with 10-ms windows (reading a), right and left differ without\n    a break from 122 ms to 150 ms; with 5-ms bins (reading b) the run from 125 ms lasts to 140 ms\n    and breaks before 150. Over the 2355 trials of these units' sessions, withdrawal is at 153 ms\n    at the earliest (1st percentile 157.5) and 193.0 ms on average. All three values are within\n    tolerance under reading a and the minimum. Asking the run to last to 160 ms finds none under\n    reading a.\n  deviations:\n  - The end of the third impulse is taken as 150 ms, the end of the paper's 0 to 150 ms sequence\n    window; the third impulse ends at about 117 to 149 ms across sequences (onset plus the Table 1\n    duration). The outcome rests on this choice (140 and 150 ms give 122, 160 ms gives no run).\n  - Each unit's PSTH per choice is the mean of its per-sequence PSTHs; the 10-ms window is centred,\n    a standard choice.\n- claim: s5-slow-positive-no-integration\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_mcguire_2016.ipynb\n  output: claim:s5-slow-positive-no-integration\n  notes: With the 25-ms baseline (reading a), the pulse 3 response of the 21 L5 Slow Positive units\n    does not differ across sequences on right-choice (ANOVA p = 0.052) or left-choice trials\n    (p = 0.324), and it does not correlate with sequence mean speed or with the mean speed of\n    pulses 2 and 3 or of pulses 1 and 2 (all p of 0.08 or more). Pulses 1 and 2 evoke 1.04 Hz on\n    right-choice and -0.36 Hz on left-choice trials. With the 10-ms baseline the left-choice\n    correlation with pulses 2 and 3 reaches p = 0.03. With the data set's labels the right-choice\n    ANOVA is significant with the 25-ms baseline (p = 0.016).\n  deviations:\n  - Impulse mean speed is twice the Table 1 peak amplitude over the Table 1 duration (a ramp out\n    and back), in place of the S1 Fig profiles; with four sequences only the ordering matters.\n  - Classes are this attempt's, as for fig7de-medium-suppressed; the data set's labels give a\n    significant ANOVA under the 25-ms baseline, so the outcome rests on the choice.\n- claim: s6-head-position-choice\n  outcome: reproduced\n  notebook: reproduce_mcguire_2016.ipynb\n  output: claim:s6-head-position-choice\n  measured: 0.595\n  notes: From S2 Data, head x position differs between right- and left-choice trials at every frame\n    from 100.8 ms (p = 0.037) to 151.2 ms, by 0.595 mm at 126 ms (right minus left -0.595), with\n    both t tests. Head angle, both whisker tip coordinates and head y differ at no frame.\n  deviations:\n  - The tests are computed from the per-frame means and SEMs, with 22 left- and 21 right-choice\n    trials, as S2 Data holds no single trials.\n- claim: s7-no-fs-l5-slow-positive\n  outcome: reproduced\n  notebook: reproduce_mcguire_2016.ipynb\n  output: claim:s7-no-fs-l5-slow-positive\n  notes: Every class holds RS, FS and multi-units (Fast 63, 26, 71; Medium 23, 7, 18; Slow Positive\n    30, 8, 13; Slow Negative 25, 2, 24). The FS fraction is 0.157 in Slow Positive and 0.039 in\n    Slow Negative against 0.162 in Fast. The 21 L5 Slow Positive units are 15 RS and 6 multi-units.\n- claim: fig9b-stimulus-decoder-fast-medium\n  outcome: reproduced\n  notebook: decoders.ipynb\n  output: claim:fig9b-stimulus-decoder-fast-medium\n  measured:\n  - 84.1\n  - 74.9\n  - 84.4\n  - 82.1\n  notes: With C = 1 (reading a, 300 repeats) 208 Fast and Medium units decode the sequence at 84.1%,\n    74.9% for FMS and 84.4% for FFF; FMS and SMF at 82.1% under reading A (97.6% under reading B).\n    The largest confusion is FMS with FFF (19%), not FMS with SMF. With C by cross-validation\n    (reading b, 5 repeats), 76.0% overall and 62.2% for FMS. The data set's labels give 87.1%.\n  deviations:\n  - 100 pseudo-trials per sequence per repeat, and a split stratified by sequence, standard\n    choices.\n- claim: fig9c-best-units-short-windows\n  outcome: reproduced\n  notebook: decoders.ipynb\n  output: claim:fig9c-best-units-short-windows\n  notes: Mean single-unit accuracy is 32.7% for 5-ms units (69), 31.5% for 10-ms units (64) and 27.2\n    to 30.9% for longer windows; 17 of the 21 top-ranked units have 5 or 10 ms windows.\n- claim: fig9b-stimulus-decoder-slow-chance\n  outcome: reproduced\n  notebook: decoders.ipynb\n  output: claim:fig9b-stimulus-decoder-slow-chance\n  measured: 30.1\n  notes: 102 Slow units decode the sequence at 30.1% (C = 1, 300 repeats), within tolerance of 32%,\n    and not above chance by the fraction of repeats (p = 0.213, reading a). The binomial test of\n    120,000 pooled pseudo-trials (reading b) is significant, as any excess is with that many draws.\n    With C by cross-validation, 28.9%, significant by both tests over 5 repeats. The data set's\n    labels give 33.1% (p = 0.020 by reading a).\n- claim: fig9d-single-bin-decoder\n  outcome: reproduced\n  notebook: decoders.ipynb\n  output: claim:fig9d-single-bin-decoder\n  measured: 39.4\n  notes: With one 0 to 150 ms bin the Fast/Medium decoder is 39.4% (within tolerance of 43%) and the\n    Slow decoder 26.5%, 3.6 points below its 10-ms accuracy. With C by cross-validation, 28.9% and\n    24.9%.\n- claim: fig9e-temporal-pattern-decoding\n  outcome: reproduced\n  notebook: decoders.ipynb\n  output: claim:fig9e-temporal-pattern-decoding\n  measured: 79.4\n  notes: Rate-normalized trains give 79.4%; time-scrambled trains 28.9%, not above chance by the\n    fraction of repeats (p = 0.367) and below 32%. With C by cross-validation, 72.1% and 28.3%.\n  deviations:\n  - Scrambling redistributes each trial's spikes uniformly over 0 to 150 ms, once per run, a\n    standard choice.\n- claim: fig9f-choice-decoder\n  outcome: not_reproduced\n  notebook: decoders.ipynb\n  output: claim:fig9f-choice-decoder\n  measured:\n  - 80.1\n  - 91.7\n  notes: The Slow choice decoder predicts choice at 80.1% from the 150-ms bin and 91.7% from the\n    100 ms before withdrawal (equal draws, mean over sequences; 80.1 to 92.0% under the other\n    readings), and at 74.6% and 79.2% with C by cross-validation, all above 71.5%. The Fast/Medium\n    decoder predicts choice at 67.1% and 79.0% (63.8% and 66.9% with cross-validation), not within\n    45 to 55%. Trained without balancing the two choices, both decoders fall to 50 to 54%, Slow\n    included. No reading gives Slow at 65% with Fast/Medium near chance. The pseudo-population sums\n    about 100 independent units, which can raise accuracy well above that of single units\n    (L5b Slow Positive units average 59.8% alone).\n  deviations:\n  - Training weights the two choices equally (an assumption, as the Methods give chance as 50%\n    and an unweighted fit predicts one side for every trial); the unweighted fit is shown and does\n    not give the claim either.\n  - Cross-validated C (reading b) run with 10 repeats.\n- claim: fig9g-l5b-slow-positive-best-choice\n  outcome: reproduced\n  notebook: decoders.ipynb\n  output: claim:fig9g-l5b-slow-positive-best-choice\n  notes: L5b Slow Positive units have the highest mean single-unit choice accuracy, 59.8% balanced\n    accuracy over 15 units (next L5a Slow Positive 56.4%, L5b Slow Negative 55.4%), and 5 of the 11\n    top-ranked Slow units are L5b Slow Positive, the largest group but not more than half.\n  deviations:\n  - Single-unit accuracy is balanced accuracy on the unit's own test trials, a standard choice so\n    that chance is 50%.\nfindings:\n- kind: metadata_error\n  statement: The data descriptor gives the column of each electrode as AllRats(expt).MapPosition\n    and says units in columns A1 and B2 must not be used in stimulus analyses, but AllRats.mat has\n    no MapPosition field. No field gives the recorded column.\n- kind: selection_undocumented\n  statement: AllRats.mat holds 506 units (330 single, 176 multi-unit) where the paper reports 473\n    (306 single, 167 multi-unit). The extra units are probably those in columns A1 and B2, but\n    without the column map they cannot be identified, so every unit analysis here uses all 506.\n- kind: data_missing\n  statement: The data set holds only the five recorded rats. The fixed-panel control sessions and\n    the behaviour of rats 62SC, 107Si and 62SS (Figure 2) are not deposited; the paper's S1 and S2\n    Data give only per-rat and per-session summaries.\n- kind: methods_unavailable\n  statement: Question for the authors. The stored temporal-modulation p-values (TempSig) were\n    computed over -50 to 300 ms in 10-ms bins (TempSig.Params), while the Methods give 0 to 180 ms\n    after nose poke entry, and the Methods do not name the statistic compared with permuted\n    spikes. Permuting spikes uniformly and comparing the PSTH variance gives 310 modulated units\n    over the Methods' window, the same count as the stored values, but the two agree for only 73%\n    of units (82% with the stored window). Which window and statistic were used for the paper's 305?\n- kind: methods_unavailable\n  statement: Question for the authors. Which test selected the 61 Fast RS single units \"with\n    significant response to F impulses\"? A paired t test across trials of the 5 to 35 ms rate\n    against the 0 to 10 ms rate selects 34 of 63 Fast RS units; the paper's 61 is close to all of\n    them.\n- kind: methods_unavailable\n  statement: Question for the authors. How was the choice decoder's 65% obtained? With per-unit\n    logistic functions summed over a pseudo-population, as the Methods describe, Slow units give 80\n    to 92% when the two choices are weighted equally in training and about 51% when they are not,\n    and Fast/Medium units 67 to 79%. Were the choices balanced, how many units entered each\n    prediction, and were test trials drawn within each rat?\n- kind: methods_unavailable\n  statement: Question for the authors. How were the peak latency and the evoked modulation of\n    Figure 4D computed (smoothing window placement, pooling of impulses and sequences)? From the\n    10-ms smoothed 1-ms PSTH the latencies are 14 to 20 ms in every layer, against 9.8 to 16.1 ms\n    in the paper.\n- kind: other\n  statement: The stored regression inputs (StimReg Yval) equal the spike counts summed over\n    completed trials (Complete equal to 1) for all 506 units, while the descriptor says the paper\n    used trials with nose poke duration over 250 ms, a set that also holds 126 trials without a\n    choice. The stored regression results are reproduced exactly from the spikes and the stored\n    regressor.\n- kind: other\n  statement: For rat 18FB the per-rat right-choice fractions computed from the data set's sessions\n    differ by up to 0.026 from the S1 Data values of Figure 2B, while for the other four rats they\n    are equal, so S1 Data and the data set hold different sessions for 18FB.\n"
}
```

```
File created successfully at: attempts/mcguire-2016-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
sed -i 's/a set that also holds 126 trials without a/a set that also holds 129 trials without a/' attempts/mcguire-2016-01.yaml && . $TMPDIR/dev/bin/activate && python - <<'EOF'
import yaml,re
for f in ['attempts/mcguire-2016-01.yaml','questions/mcguire-2016.yaml']:
    d=yaml.safe_load(open(f))
    txt=open(f).read()
    # find ': ' inside continuation/plain values (after the key)
    for i,l in enumerate(txt.split('\n')):
        m=re.match(r'^\s*(- )?[a-z_]+: (.*)$',l)
        rest = m.group(2) if m else l.strip()
        if ': ' in rest: print(f,i+1,l)
        for w in ['—','rather']:
            if w in l: print('WORD',f,i+1,l)
    print(f,'ok')
d=yaml.safe_load(open('attempts/mcguire-2016-01.yaml'))
c=yaml.safe_load(open('claims/mcguire-2016.yaml'))
ids=[x['id'] for x in c['claims']]; got=[o['claim'] for o in d['outcomes']]
print(len(ids),len(got), set(ids)^set(got))
import collections; print(collections.Counter(o['outcome'] for o in d['outcomes']))
EOF
python tools/entry.py check entries/mcguire-2016 2>&1 | tail
```

```
attempts/mcguire-2016-01.yaml ok
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/yaml/__init__.py", line 125, in safe_load
    return load(stream, SafeLoader)
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/yaml/__init__.py", line 81, in load
    return loader.get_single_data()
           ~~~~~~~~~~~~~~~~~~~~~~^^
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/yaml/constructor.py", line 49, in get_single_data
    node = self.get_single_node()
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/yaml/composer.py", line 36, in get_single_node
    document = self.compose_document()
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/yaml/composer.py", line 55, in compose_document
    node = self.compose_node(None, None)
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/yaml/composer.py", line 84, in compose_node
    node = self.compose_mapping_node(anchor)
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/yaml/composer.py", line 133, in compose_mapping_node
    item_value = self.compose_node(node, item_key)
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/yaml/composer.py", line 82, in compose_node
    node = self.compose_sequence_node(anchor)
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 9,10p questions/mcguire-2016.yaml; python - <<'EOF'
p='questions/mcguire-2016.yaml'; s=open(p).read()
s=s.replace('''Should the claim be `data:
    elsewhere` with `where` naming S2 Data, as fig3-fsfs-sffs-intensity-only and
    s6-head-position-choice are?''','''Should the claim's data field be `elsewhere`, with `where` naming S2 Data, as for
    fig3-fsfs-sffs-intensity-only and s6-head-position-choice?''')
open(p,'w').write(s)
EOF
. $TMPDIR/dev/bin/activate && python - <<'EOF'
import yaml,collections
q=yaml.safe_load(open('questions/mcguire-2016.yaml')); print(len(q['questions']))
d=yaml.safe_load(open('attempts/mcguire-2016-01.yaml'))
c=yaml.safe_load(open('claims/mcguire-2016.yaml'))
ids=[x['id'] for x in c['claims']]; got=[o['claim'] for o in d['outcomes']]
print(len(ids),len(got), set(ids)^set(got), ids==got)
print(collections.Counter(o['outcome'] for o in d['outcomes']))
EOF
python tools/entry.py check entries/mcguire-2016 2>&1 | tail -3; git status --short
```

```
fixed-panel trials, the values the S2B Fig paired t test uses. Should the claim be `data:
    elsewhere` with `where` naming S2 Data, as fig3-fsfs-sffs-intensity-only and
1
37 37 set() True
Counter({'reproduced': 22, 'partially_reproduced': 12, 'not_reproduced': 2, 'blocked': 1})
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
?? attempts/mcguire-2016-01.yaml
?? entries/mcguire-2016/
?? questions/mcguire-2016.yaml
?? scripts
```

**Agent**

Checks pass, with 37 outcomes against 37 claims. Building the verifier's handover package.

**Agent calls Bash**

```bash
date -u; . $TMPDIR/dev/bin/activate && python tools/entry.py handover entries/mcguire-2016 2>&1 | tail -5; ls -R executed/mcguire-2016/handover | head; python - <<'EOF'
import nbformat,glob
for f in glob.glob('executed/mcguire-2016/handover/**/*.ipynb',recursive=True):
    n=nbformat.read(f,4); print(f, sum('**Result' in c.source for c in n.cells), any('## Summary' in c.source for c in n.cells))
EOF
```

```
Wed Nov 11 18:02:10 UTC 2026
wrote executed/mcguire-2016/handover
executed/mcguire-2016/handover:
decoders.ipynb
mcguire-2016.yaml
reproduce_mcguire_2016.ipynb
ssc4.py
executed/mcguire-2016/handover/reproduce_mcguire_2016.ipynb 0 False
executed/mcguire-2016/handover/decoders.ipynb 0 False
```

**Agent**

I've built and run the entry, written the attempt record, and produced the handover package. Of the 37 claims, 22 reproduced, 12 partially reproduced, 2 did not reproduce and 1 is blocked. Nothing was committed.

## 1. Outcomes

| claim | outcome |
|---|---|
| fig2ab-fms-smf-not-discriminated | partial (only 5 of 8 rats in the data; 62SC is missing) |
| training-days | partial (fewest days is 11, not 8) |
| fig2c-choice-follows-mean-speed | reproduced |
| fig2d-fixed-panel-impairs | blocked, data_missing |
| dprime-fff-sss-range | partial (highest is 1.09, not 1.5) |
| fig3-fsfs-sffs-intensity-only | reproduced (from the paper's S1 Data) |
| units-recorded | reproduced (but 506 units, not 473) |
| baseline-rates | partial (highest RS layer mean is 11.4 Hz, limit 11) |
| temporal-modulation-count | reproduced (310 units) |
| modulated-higher-baseline | reproduced |
| fig4d-evoked-modulation-by-layer | partial (best reading gets 4 of 5 layers) |
| latency-by-layer | partial (layer order holds, values are 14 to 20 ms) |
| fig4d-gradual-decrease | not reproduced (L5a also decreases) |
| fig6-regression-significant | reproduced (194) |
| fig6e-unit-classes | partial (51 Slow Negative units, limit 48.4) |
| fig6fg-laminar-classes | partial (4 of 6 values) |
| fig7c-fast-impulse-velocity, fig7c-fast-sequence-rate | reproduced |
| fig7-fff-adaptation | partial (test selects 34 units, not 61; only pulse 2/1 significant) |
| fig7-sss-no-adaptation, s4-fms-middle-pulse | reproduced |
| fig7de-medium-suppressed | partial (no suppression), rests on an assumption |
| fig8a-slow-positive-no-sequence-difference | partial (S impulses also evoke a response) |
| fig8b-slow-negative-no-impulse-response | reproduced |
| fig8d-slow-positive-right-choice-l5 | partial (L5b only), rests on an assumption |
| fig8d-fast-medium-no-choice-bias | reproduced |
| fig8e-choice-divergence-125ms | reproduced (122 ms), rests on an assumption |
| s5-slow-positive-no-integration | reproduced, rests on an assumption |
| s6-head-position-choice | reproduced (from S2 Data) |
| s7-no-fs-l5-slow-positive | reproduced |
| fig9b fast/medium, fig9c, fig9b slow-chance, fig9d, fig9e, fig9g | reproduced |
| fig9f-choice-decoder | not reproduced (Slow units 80 to 92%, not 65%; Fast/Medium 67 to 79%, not near chance) |

## 2. What was found about the dataset

- **Version:** the data set is one file, `AllRats.mat`, under `ssc-4/live/`. It is pinned as `unversioned` with the MD5 sum from the data set's `checksums.md5`; it is the only copy in the bucket.
- **Column map missing:** the descriptor says to drop units in columns A1 and B2 using a `MapPosition` field, but the file has no such field. So 33 units beyond the paper's 473 cannot be removed, and every unit analysis uses all 506.
- **Stored p-values:** the deposited temporal-modulation p-values were computed over -50 to 300 ms, not the Methods' 0 to 180 ms after nose-poke entry. My recomputation gives the same count (310) but agrees unit by unit for only 73%.
- **Trials used by the authors:** the deposited regression inputs equal spike counts summed over completed trials, and the deposited R² and p reproduce exactly. That settles which trials the paper analysed.
- **Not deposited:** the fixed-panel sessions and three behaviour-only rats (62SC, 107Si, 62SS). Rat 18FB's per-rat values differ from S1 Data by up to 0.026; the other four rats match exactly.
- **Checks passed:** no recording is deposited twice, and spikes and trials share one clock (impulse-2 timing contrast, 61 of 80 sessions; weak in rat 18Ro).

**Assumptions:**
- Downstream claims use my own recomputed unit classes. They agree 99.6% with the deposited labels where both mark a unit as modulated. The deposited labels are shown as a variant. Four claims are marked `assumed` because that variant would change their outcome or the reading matters (fig7de, fig8d-L5, s5, and fig8e, where the third impulse is taken to end at 150 ms).
- The choice decoder weights right and left equally in training, since the paper gives chance as 50%. The unweighted fit is shown; it does not give the claim either.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- Which window and statistic the temporal-modulation test used.
- Which test selected the 61 F-responsive Fast RS units. A paired t test gives 34; all Fast RS units number 63, and with those the FMS/SMF test gives p = 0.087 against the paper's 0.08.
- How the 65% choice-decoder accuracy was obtained.
- How peak latency and evoked modulation were computed.

**Question for a reader** (`questions/mcguire-2016.yaml`): should fig2d be marked `data: elsewhere`? The paper's S2 Data holds the per-rat values; tested as a variant there, they give p = 0.012, matching the paper.

## 3. Where the protocol was unclear

1. `archives.md` describes CRCNS data sets as zip files; this one is a single MATLAB file. I streamed it with fsspec into `scipy.io.loadmat` in memory.
2. The protocol does not say whether the author may treat a claim's `data` field as part of the claim. Here fig2d's data are public in S2 Data. I left the field as written, blocked the claim, showed the S2 Data test as a variant and asked a reader.
3. It is silent on whether the data set's own stored analysis results (labels, p-values) or a recomputation should select units for dependent claims. I recomputed, showed the stored labels as a variant, and marked `assumed` where the outcome depends on it.
4. It does not say which reading of an upstream claim feeds the claims that depend on it. I adopted one, recorded it as a deviation, and flagged the outcomes it changes.
5. `measured` is defined for when a reading matches, not for when none does. I recorded the closest reading and said so in the notes.
6. It does not say whether an expensive reading may run with fewer repeats. The cross-validated decoder reading ran with 5 to 10 repeats instead of 300 to stay within the runtime limits; I recorded this in the notebook and the deviations.
7. The suggested clock check (decoding a task variable around trial start) did not fit well. I used a contrast of impulse-2 onset times between sequences, plus a pre-onset control window.

## 4. Runtime and failures

The run took about 1 h 10 min (16:54 to about 18:03 UTC). In the clean run the main notebook took 106 s and the decoder notebook 925 s, both passing; `entry.py check` reports 0 errors and the handover is in `executed/mcguire-2016/handover/`. During development there were only small script errors, all fixed before the final run; nothing failed in it.

## End of run

66 turns, 61 minutes, $7.39 at API prices, result: success.
