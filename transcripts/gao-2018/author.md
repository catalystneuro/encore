# gao-2018 · author · run 43586299319

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cd  ls; ls docs entries attempts claims paper tools; wc -l docs/*.md README.md
```

```
Sat Nov 14 10:45:49 UTC 2026
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
[... 987 more lines not kept]
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
 "file_path": "claims/gao-2018.yaml"
}
```

```
1	# Claims for Gao, Davis, Thomas, Economo, Abrego, Svoboda, De Zeeuw and Li (2018), "A
2	# cortico-cerebellar loop for motor planning", Nature 563, 113-116, doi:10.1038/s41586-018-0633-x,
3	# tested on DANDI:000007 and CRCNS:alm-4.
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-14,
5	# protocol pilot-15 as stated in docs/protocol.md. It updates the file written 2026-11-10 under
6	# pilot-14 (and checked that day) for DANDI:000007 alone; ids are kept where the finding is the
7	# same, and the changes of that check are carried over.
8	#
9	# Text read: the version of record (PMC6212318, open access), Europe PMC JATS XML flattened, in
10	# paper/10.1038-s41586-018-0633-x.txt: main text, Methods, the legends of Extended Data Figs. 1 to
11	# 10, and the Supplementary Information (41586_2018_633_MOESM1_ESM.pdf, from the publisher; also
12	# paper/...supp1.pdf), whose text is appended: the Extended Data Fig. 10 discussion, the cerebellar
13	# circuitry discussion and Supplemental Table 1 (mice and hemispheres per experiment). supp2.pdf is
14	# the Nature reporting summary. The legends of the main Figs. 1 to 4 are not in the stored text,
15	# and there is no PDF of the main paper; values, significance marks and neuron counts given only in
16	# those legends or inside the figures are not used here (see the report of this run). Sources cite
17	# main-text paragraphs counting the opening summary paragraph as paragraph 1.
18	# Code: the paper links none. Its Code availability says "Software used for data analysis is
19	# available from the corresponding author upon reasonable request"; the reporting summary says
20	# "Custom analysis scripts and data will be deposited on CRCNS.org" and gives no identifier. The
[... 851 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/gao-2018.yaml",
 "offset": 871
}
```

```
871	  statement: Transient fastigial photo-activation alters ALM preparatory activity long (more than
872	    1 s) after the photostimulus ends.
873	  source: Main text, paragraph 16; Figure 4f; Extended Data Figure 9b
874	  quote: Transient photo-activation of the fastigial nucleus altered ALM preparatory activity long
875	    (>1 s) after cessation of the photostimulus
876	  datasets:
877	  - "000007"
878	  - crcns-alm-4
879	  criterion: For each ALM pyramidal neuron of the fastigial photo-activation sessions, E4 in 400
880	    ms bins in 50 ms steps (Methods, for Fig. 4f) gives the fraction with a significant change (p
881	    < 0.01). What the fraction is compared with is not given (open; readings (a) the 1% expected
882	    by chance at p < 0.01, (b) the fraction in the bins before photostimulus onset). Reproduced
883	    when under one reading the fraction in bins starting 1 s or more after photostimulus offset
884	    (and ending before the go cue or within the response epoch) exceeds the comparison, by a
885	    one-sided binomial test at p < 0.05 for reading (a) or a one-sided test of two proportions
886	    for reading (b).
887	- id: fig4g-dentate-effect-recovers
888	  statement: Dentate photo-activation also changes ALM responses (latency 8.3 plus or minus 5.0
889	    ms), but ALM activity recovers quickly after it.
890	  source: Main text, paragraph 16; Figure 4g; Extended Data Figure 9a
[... 211 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat docs/archives.md; ls entries/fouke-2025; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in; ls papers/datasets | grep gao; cat papers/datasets/gao-2018.yaml; ls questions | grep gao
```

```
# Archives

The registry tests papers against data in public archives. It began with one,
the DANDI Archive. The protocol is written for any archive. What is particular
to an archive (how its datasets are named, versioned and read) is here, and an
agent is pointed to its archive's section.

A dataset is keyed as `<archive>:<id>` and shown as `<LABEL>:<id>`, for example
`DANDI:000003`. Its files in this repository (`claims/`, `questions/`,
`transcripts/`, the `attempt/` branch, the paper store) are under its folder
name: the identifier alone for DANDI, which the registry began with, and
`<archive>-<id>` for any other archive. Each archive is an adapter, a module in `tools/archives/` ("Adding an archive",
below), and `tools/datasets.py` turns one form of a dataset's name into another.
The workflows take a dataset in any of these forms.

## DANDI

- **Datasets.** A dandiset, identified by six digits (`000003`). Targets are the
  public dandisets whose metadata names a paper (`targets/dandisets.json`, built
  by `tools/build_targets.py` and refreshed daily by the Track DANDI workflow).
[... 320 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/fouke-2025-01.yaml | head -150; cat paper/alm-4.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Read the protocol, claims file (about 45 claims) and the CRCNS descriptor. Next I'll survey both datasets.

**Agent calls Bash**

```bash
cd  sed -n 150,400p attempts/fouke-2025-01.yaml | grep -n -A3 -E "^(findings|missing|verifications|- kind|  - kind)" | head -60; ls schemas; python tools/entry.py --help 2>&1 | head -30
```

```
95:findings:
96:- kind: data_missing
97-  statement: The dandiset holds only the freely swimming tracking of Figure 1 and Figure S1. The
98-    two-photon imaging and the head-fixed tail tracking behind Figures 2 to 4 are not in it, and
99-    the GitLab repository the paper names for all behavioural and imaging data holds analysis
--
101:- kind: metadata_insufficient
102-  statement: The stimulus codes 0 to 20 have no names or description in the files or the
103-    dandiset metadata. They can be named only from the paper's analysis notebook and the protocol
104-    file of its stimulus software.
105:- kind: code_mismatch
106-  statement: The paper's analysis notebook labels code 9 as lateral right and 11 as lateral left,
107-    while its conversion of the stimulus software's names gives the reverse (it carries a remap
108-    that swaps them). The data do not settle which is right; zebrafish barely turn to either, and
--
111:- kind: metadata_error
112-  statement: Subject ids 0 to 11 are each used for one zebrafish and one Danionella cerebrum, so
113-    subject_id does not identify an animal. The archive's summary counts 25 subjects and lists
114-    only Danio rerio; the files hold 37 fish of two species.
115:- kind: metadata_error
[... 73 more lines not kept]
```

**Agent**

Now the data: DANDI 000007 versions and assets, and the CRCNS bucket listing.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/000007/versions/" | python -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/000007/" | python -c "import json,sys;d=json.load(sys.stdin);print(d['most_recent_published_version'], d['draft_version'])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/000007/versions/0.220126.1903/assets/?page_size=100" | python -c "
import json,sys;d=json.load(sys.stdin)
for a in d['results']: print(a['path'], a['size'], a['asset_id'])"; curl -s "https://api.dandiarchive.org/api/dandisets/000007/versions/0.220126.1903/" | python -c "
import json,sys;d=json.load(sys.stdin);print(d.get('description'));print(d.get('relatedResource'));print(d.get('assetsSummary'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=alm-4/" | python -c "
import sys,re
t=sys.stdin.read()
for k,s in re.findall(r'<Key>(.*?)</Key>.*?<Size>(\d+)</Size>',t): print(k,s)
print('trunc', re.findall('<IsTruncated>(.*?)</IsTruncated>',t))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://crcnsarchive.s3-us-west-2.amazonaws.com/alm-4/live/checksums.md5; curl -s https://crcnsarchive.s3-us-west-2.amazonaws.com/alm-4/live/filelist.txt; python -c "
import fsspec,zipfile
for d in ['ALM_recording_DCN_photoactivation','ALM_recording_DCN_photoinhibition']:
    f=fsspec.open(f'https://crcnsarchive.s3-us-west-2.amazonaws.com/alm-4/live/{d}/analyses_scripts.zip',block_size=2**20).open()
    z=zipfile.ZipFile(f)
    print(d,len(z.infolist()))
    for i in z.infolist(): print(' ',i.filename,i.file_size)
" 2>&1 | head -150
```

Result: the fetched text is not kept.

**Agent**

Need a working environment; I'll make a venv in $TMPDIR.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q -p 3.12 venv && . venv/bin/activate && uv pip install -q fsspec aiohttp requests h5py remfile pynwb numpy scipy pandas matplotlib statsmodels ipykernel nbformat nbconvert 2>&1 | tail -3; python -c "import pynwb,fsspec;print(pynwb.__version__)"
```

```
4.2.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; python -c "
import fsspec,zipfile
for d in ['ALM_recording_DCN_photoactivation','ALM_recording_DCN_photoinhibition']:
    f=fsspec.open(f'https://crcnsarchive.s3-us-west-2.amazonaws.com/alm-4/live/{d}/analyses_scripts.zip',block_size=2**20).open()
    z=zipfile.ZipFile(f)
    print(d,len(z.infolist()))
    for i in z.infolist(): print(' ',i.filename,i.file_size)
" 2>&1 | head -200
```

```
ALM_recording_DCN_photoactivation 24
  analyses_scripts/ 0
  analyses_scripts/analysis_ALM_DCN_photoactivation_selectivity.m 5456
  analyses_scripts/analysis_compiled_all_ALM_DCNstim_FR.mat 3078005
  analyses_scripts/analysis_ALM_CodingDirection_DCN_photoactivation.m 10189
  analyses_scripts/analysis_ALM_population_selectivity.m 1063
  analyses_scripts/analysis_compiled_all_ALM_DCNstim_selectivity.mat 130371326
  analyses_scripts/helper_functions/ 0
  analyses_scripts/helper_functions/basis_col.m 1488
  analyses_scripts/helper_functions/ref.m 1774
  analyses_scripts/helper_functions/is_orthonormal_set.m 1363
  analyses_scripts/helper_functions/func_discriminant.m 745
  analyses_scripts/helper_functions/func_getPSTHsmallBin.m 538
  analyses_scripts/helper_functions/is_orthogonal_set.m 1110
  analyses_scripts/helper_functions/func_getPSTH_smallBin.m 527
  analyses_scripts/helper_functions/func_plot_mean_and_sem.m 961
  analyses_scripts/helper_functions/func_getPSTH.m 866
  analyses_scripts/helper_functions/Gram_Schmidt_process.m 1704
  analyses_scripts/analysis_compiled_all_ALM_DCNstim_FR.m 20958
  analyses_scripts/analysis_compiled_all_ALM_DCNstim_selectivity.m 21137
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; cat > survey.py <<'EOF'
import remfile,h5py,pynwb,requests,sys
aid=sys.argv[1]
url=requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=True).url
f=h5py.File(remfile.File(url),'r')
io=pynwb.NWBHDF5IO(file=f,mode='r',load_namespaces=True)
nwb=io.read()
print(nwb)
print(nwb.session_description, nwb.experiment_description, nwb.subject)
def walk(g,p=''):
    for k,v in g.items():
        if isinstance(v,h5py.Dataset): print(p+'/'+k, v.shape, v.dtype)
        else: walk(v,p+'/'+k)
walk(f)
for k,v in f.attrs.items(): print(k,v)
EOF
python survey.py 2b588d93-15de-4190-8efc-7562e725068d 2>&1 | head -250
```

```
root pynwb.file.NWBFile at 0x139067886956720
Fields:
  devices: {
    Cambridge NeuroTech 64ch H2 probe <class 'pynwb.device.Device'>,
    fiber <class 'pynwb.device.Device'>
  }
  electrode_groups: {
    Cambridge NeuroTech 64ch H2 probe_g1 <class 'pynwb.ecephys.ElectrodeGroup'>
  }
  electrodes: electrodes <class 'pynwb.ecephys.ElectrodesTable'>
  experiment_description: Extracelluar recording in ALM
  experimenter: ['Nuo Li']
  file_create_date: [datetime.datetime(2020, 3, 24, 23, 6, 36, 213939, tzinfo=tzlocal())]
  identifier: BAYLORCD8_2017-10-18 12:35:50
  institution: Janelia Research Campus
  intervals: {
    trials <class 'pynwb.epoch.TimeIntervals'>
  }
  keywords: <StrDataset for HDF5 dataset "keywords": shape (5,), type "|O">
  ogen_sites: {
[... 98 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; cat > survey2.py <<'EOF'
import remfile,h5py,pynwb,requests,sys,collections, numpy as np
aid=sys.argv[1]
url=requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=True).url
f=h5py.File(remfile.File(url),'r')
io=pynwb.NWBHDF5IO(file=f,mode='r',load_namespaces=True)
nwb=io.read()
t=nwb.trials.to_dataframe()
print(t.head(10).to_string())
for c in ['photo_stim_id','response','lick_early','session_directory']: print(c, collections.Counter(t[c]).most_common(20))
print(pd_desc:=None)
for c in nwb.trials.columns: print(c.name, '|', c.description)
u=nwb.units
for c in u.columns: print(c.name,'|',c.description)
print(collections.Counter(u['cell_type'][:]))
print(nwb.ogen_sites['Fastigial'] if 'Fastigial' in nwb.ogen_sites else list(nwb.ogen_sites.values())[0])
e=nwb.electrodes.to_dataframe(); print(e.head(3).to_string()); print(collections.Counter(e.location))
print(u['obs_intervals'][:3], u['sampling_rate'][:3])
st=u['spike_times'][0]; print(len(st), st[:5], st[-1], t.start_time.min(), t.stop_time.max())
print(nwb.keywords[:])
EOF
python survey2.py 2b588d93-15de-4190-8efc-7562e725068d 2>&1 | head -120
```

```
start_time  stop_time                                        session_directory  pole_in_time  pole_out_time  cue_time response  lick_early photo_stim_id
id                                                                                                                                                          
0      3725.97    3730.97  /data/datafiles 2/data_structure_BAYLORCD8_20171018.mat       3726.54        3727.84  3729.140  NoLickR           0             5
1      3739.91    3744.91  /data/datafiles 2/data_structure_BAYLORCD8_20171018.mat       3740.48        3741.78  3743.080  NoLickL           0             6
2      3752.80    3757.80  /data/datafiles 2/data_structure_BAYLORCD8_20171018.mat       3753.37        3754.67  3757.329     HitL           1             0
3      3762.61    3767.61  /data/datafiles 2/data_structure_BAYLORCD8_20171018.mat       3763.18        3764.48  3765.780     ErrR           0             0
4      3775.57    3780.57  /data/datafiles 2/data_structure_BAYLORCD8_20171018.mat       3776.14        3777.44  3778.740     HitL           0             0
5      3784.02    3789.02  /data/datafiles 2/data_structure_BAYLORCD8_20171018.mat       3784.59        3785.89  3787.190     HitL           0             0
6      3792.47    3797.47  /data/datafiles 2/data_structure_BAYLORCD8_20171018.mat       3793.04        3794.34  3795.640  NoLickL           0             6
7      3805.38    3810.38  /data/datafiles 2/data_structure_BAYLORCD8_20171018.mat       3805.95        3807.25  3808.550     ErrR           0             0
8      3818.33    3823.33  /data/datafiles 2/data_structure_BAYLORCD8_20171018.mat       3818.90        3820.20  3821.500  NoLickR           0             6
9      3831.27    3836.27  /data/datafiles 2/data_structure_BAYLORCD8_20171018.mat       3831.84        3833.14  3834.440     HitR           0             0
photo_stim_id [('0', 284), ('6', 70), ('5', 68)]
response [('HitR', 143), ('HitL', 132), ('ErrR', 72), ('NoLickR', 37), 
[... 42 more lines not kept]
```

**Agent**

DANDI trial tables have no lick times; `cue_time` is in session time though described as relative to trial start. Now the CRCNS tar.gz layout (streaming the head).

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; timeout 600 python -c "
import fsspec,tarfile,time
t0=time.time()
for d in ['ALM_recording_DCN_photoactivation','ALM_recording_DCN_photoinhibition']:
  f=fsspec.open(f'https://crcnsarchive.s3-us-west-2.amazonaws.com/alm-4/live/{d}/datafiles.tar.gz',block_size=2**24).open()
  tf=tarfile.open(fileobj=f,mode='r|gz')
  n=0
  for m in tf:
    print(m.name,m.size, round(time.time()-t0,1), f.tell()//2**20)
    n+=1
    if n>25: break
"
```

```
datafiles 0 0.9 0
datafiles/data_structure_BAYLORNL15_20170602.mat 253091041 0.9 0
datafiles/data_structure_BAYLORNL14_20170607.mat 243212082 11.4 228
datafiles/meta_data_BAYLORNL12_20170610.mat 1629 20.7 438
datafiles/data_structure_BAYLORNL15_20170605.mat 216802289 20.7 438
datafiles/meta_data_ANM314758_20151022.mat 1622 29.3 634
datafiles/data_structure_BAYLORCD6_20170612.mat 205340464 29.3 634
datafiles/data_structure_BAYLORNL12_20170614.mat 309520942 37.8 819
datafiles/data_structure_ANM314760_20151020.mat 135418964 49.6 1101
datafiles/data_structure_ANM314756_20151023.mat 93944426 53.9 1214
datafiles/meta_data_BAYLORNL14_20170603.mat 1624 57.5 1290
datafiles/data_structure_ANM314756_20151020.mat 120021104 57.5 1290
datafiles/meta_data_ANM314758_20151021.mat 1620 62.4 1393
datafiles/data_structure_BAYLORNL12_20170613.mat 403415645 62.4 1393
datafiles/meta_data_ANM314758_20151020.mat 1626 79.2 1765
datafiles/meta_data_ANM314757_20151021.mat 1624 79.2 1765
datafiles/data_structure_ANM314746_20151022.mat 115928691 79.2 1765
datafiles/meta_data_BAYLORNL15_20170602.mat 1627 83.2 1862
datafiles/meta_data_ANM314746_20151022.mat 1621 83.2 1862
datafiles/meta_data_BAYLORCD6_20170610.mat 1622 83.3 1862
[... 33 more lines not kept]
```

**Agent**

Streaming both tar.gz archives takes about 10 min (~22 MB/s); members are per-session `data_structure_*.mat` (100 to 500 MB) and `meta_data_*.mat`. Let me read the deposited analysis scripts.

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; python -c "
import fsspec,zipfile
for d in ['ALM_recording_DCN_photoactivation','ALM_recording_DCN_photoinhibition']:
    f=fsspec.open(f'https://crcnsarchive.s3-us-west-2.amazonaws.com/alm-4/live/{d}/analyses_scripts.zip',block_size=2**20).open()
    z=zipfile.ZipFile(f)
    for i in z.infolist():
        if i.filename.endswith('.m'):
            open('scr_'+d[14:18]+'_'+i.filename.split('/')[-1],'wb').write(z.read(i))
"; ls scr_*; cat scr_DCN__analysis_compile_all_ALM_data.m
```

```
scr_DCN__Gram_Schmidt_process.m
scr_DCN__analysis_ALM_CodingDirection_DCN_photoactivation.m
scr_DCN__analysis_ALM_DCN_photoactivation_FR.m
scr_DCN__analysis_ALM_DCN_photoactivation_selectivity.m
scr_DCN__analysis_ALM_DCN_photoinhibition_selectivity.m
scr_DCN__analysis_ALM_population_selectivity.m
scr_DCN__analysis_compile_all_ALM_data.m
scr_DCN__analysis_compiled_all_ALM_DCNsilencing_selectivity.m
scr_DCN__analysis_compiled_all_ALM_DCNstim_CD.m
scr_DCN__analysis_compiled_all_ALM_DCNstim_FR.m
scr_DCN__analysis_compiled_all_ALM_DCNstim_selectivity.m
scr_DCN__basis_col.m
scr_DCN__func_discriminant.m
scr_DCN__func_getPSTH.m
scr_DCN__func_getPSTH_smallBin.m
scr_DCN__func_getPSTHsmallBin.m
scr_DCN__func_plot_mean_and_sem.m
scr_DCN__is_orthogonal_set.m
scr_DCN__is_orthonormal_set.m
scr_DCN__ref.m
[... 492 more lines not kept]
```

**Agent**

The deposited code fixes several open details (selectivity on correct non-stim trials, response window 1.3 s from cue, preference from 10 screen trials per type). Reading the remaining scripts.

**Agent calls Bash**

```bash
cd $TMPDIR; grep -v '^\s*$' scr_DCN__analysis_compiled_all_ALM_DCNstim_FR.m | head -400
```

```
clear all
close all
addpath('.\helper_functions\')
file_list = dir('..\datafiles\data_structure_*.mat');
%% establish variables to compute and save
N_trials_all = [];
FR_mean_all = [];
p_stim1_FN = [];
p_stim2_FN = [];
p_stim1_DN = [];
p_stim2_DN = [];
sig_selective = [];         %[sample delay resposne]
spk_count_yes_screen  = [];    %[whole_trial sample delay resposne]
spk_count_no_screen  = [];
PSTH_prefer_cue_aligned  = [];
PSTH_nonprefer_cue_aligned  = [];
Probe_type_all = {};
Channel_all = [];
cellType_all = [];
waveform_all = [];
[... 349 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; grep -v '^\s*$' scr_DCN__analysis_compiled_all_ALM_DCNstim_selectivity.m | sed -n 1,400p
```

```
clear all
close all
addpath('.\helper_functions\')
file_list = dir('..\datafiles\data_structure_*.mat');
%% establish variables to compute and save
N_trials_all = [];
FR_mean_all = [];
PSTH_yes_cue_aligned  = [];      
PSTH_no_cue_aligned  = [];
PSTH_stim1_yes_aligned_FN  = [];    % for neurons tested with fastigial photoactivation
PSTH_stim1_no_aligned_FN  = [];
PSTH_stim2_yes_aligned_FN  = [];
PSTH_stim2_no_aligned_FN  = [];
PSTH_stim1_yes_aligned_DN  = [];    % for neurons tested with fastigial photoactivation
PSTH_stim1_no_aligned_DN  = [];
PSTH_stim2_yes_aligned_DN  = [];
PSTH_stim2_no_aligned_DN  = [];
sig_selective = [];         %[sample delay resposne]
spk_count_yes_screen  = [];    %[whole_trial sample delay resposne]
spk_count_no_screen  = [];
[... 354 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; for f in scr_DCN__analysis_ALM_population_selectivity.m scr_DCN__analysis_ALM_DCN_photoactivation_selectivity.m scr_DCN__analysis_ALM_DCN_photoactivation_FR.m scr_DCN__analysis_ALM_DCN_photoinhibition_selectivity.m scr_DCN__func_getPSTH.m; do echo "=== $f"; grep -v '^\s*$' $f; done
```

```
=== scr_DCN__analysis_ALM_population_selectivity.m
%% figure 2
clear all
close all
addpath('.\helper_functions\')
% check to see if the data has been compiled
if ~exist('analysis_compile_all_ALM_data.mat')
    % if not, compile all data first
    analysis_compile_all_ALM_data
end
load analysis_compile_all_ALM_data
sig_selective(isnan(sig_selective))=0;
%% population average selectivity time course 
i_sel = (cellType_all(:,1)==1 & sum(sig_selective,2)>0 & N_trials_all(:,1)>15 & N_trials_all(:,2)>15);
FR_diff_all = PSTH_prefer_cue_aligned-PSTH_nonprefer_cue_aligned;
FR_diff_all = FR_diff_all(i_sel,:);
figure;
func_plot_mean_and_sem(t, FR_diff_all, 'k', [.8 .8 .8], 'n',3)
y_max = max([mean(FR_diff_all)]);
y_min = min([mean(FR_diff_all)]);
[... 323 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; grep -v '^\s*$' scr_DCN__analysis_ALM_CodingDirection_DCN_photoactivation.m | head -230; echo =====; grep -n -E "i_yes_trial|Photostim_type==|ttest|t_stim|>2|>3|screen\(|1:5|1:10" scr_DCN__analysis_compiled_all_ALM_DCNsilencing_selectivity.m | head -50
```

```
clear all
close all
addpath('.\helper_functions\')
% check to see if the data has been compiled
if ~exist('analysis_compiled_all_ALM_DCNstim_CD.mat')
    % if not, compile all data first
    analysis_compiled_all_ALM_DCNstim_CD
end
load analysis_compiled_all_ALM_DCNstim_CD
%% Fastigial perturbation 
proj_R_training_CD = [];
proj_L_training_CD = [];
proj_R_nonStim_CD = [];
proj_L_nonStim_CD = [];
proj_R_sampleStim_CD = [];
proj_L_sampleStim_CD = [];
proj_R_delayStim_CD = [];
proj_L_delayStim_CD = [];
n_session = 0;
for i_session = find(session_type==1)'
[... 208 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; grep -v '^\s*$' scr_DCN__analysis_compiled_all_ALM_DCNstim_CD.m | sed -n 60,260p
```

```
i_NoLickL = find(strcmp(obj.trialTypeStr,'NoLickL'));
    i_LickEarly = find(strcmp(obj.trialTypeStr,'LickEarly'));
    i_StimTrials = find(strcmp(obj.trialTypeStr,'StimTrials'));
    HitR = obj.trialTypeMat(i_HitR,:)';
    HitL = obj.trialTypeMat(i_HitL,:)';
    ErrR = obj.trialTypeMat(i_ErrR,:)';
    ErrL = obj.trialTypeMat(i_ErrL,:)';
    NoLickR = obj.trialTypeMat(i_NoLickR,:)';
    NoLickL = obj.trialTypeMat(i_NoLickL,:)';
    LickEarly = obj.trialTypeMat(i_LickEarly,:)';
    StimTrials = obj.trialTypeMat(i_StimTrials,:)';
    % get the good trials (periods when mice is performing)
    i_GoodTrials = find(strcmp(obj.trialPropertiesHash.keyNames,'GoodTrials'));
    GoodTrials = obj.trialPropertiesHash.value{i_GoodTrials};
    % get trial temporal structure
    t_TrialStart = obj.trialStartTimes;
    Pole_in_Time = obj.trialPropertiesHash.value{1};
    Pole_out_Time = obj.trialPropertiesHash.value{2};
    Cue_Time = obj.trialPropertiesHash.value{3};
    % get photostimulation information
[... 148 more lines not kept]
```

**Agent**

Time check and then inspect one CRCNS session struct to compare with its DANDI counterpart.

**Agent calls Bash**

```bash
date -u; cd $TMPDIR; . venv/bin/activate; cat > crcns1.py <<'EOF'
import fsspec,tarfile,time,io,scipy.io as sio, numpy as np, resource
t0=time.time()
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/alm-4/live/ALM_recording_DCN_photoinhibition/datafiles.tar.gz',block_size=2**24).open()
tf=tarfile.open(fileobj=f,mode='r|gz')
for m in tf:
    if m.name.endswith('CD14_20171028.mat') and 'data_structure' in m.name:
        b=tf.extractfile(m).read(); print('read',len(b),time.time()-t0, b[:120])
        d=sio.loadmat(io.BytesIO(b),squeeze_me=True,struct_as_record=False)
        print(d.keys()); obj=d['obj']; print(obj._fieldnames)
        for k in obj._fieldnames:
            v=getattr(obj,k); print(k, type(v), getattr(v,'shape',None), v if np.size(v)<20 else '')
        tp=obj.trialPropertiesHash; print(tp._fieldnames, tp.keyNames, tp.descr)
        for v in tp.value: print(np.shape(v), np.unique(v[~np.isnan(v)] if v.dtype.kind=='f' else v)[:20])
        ts=obj.timeSeriesArrayHash; print(ts._fieldnames, ts.keyNames, ts.descr)
        v=ts.value; print(type(v), v._fieldnames if hasattr(v,'_fieldnames') else len(v))
        vv=v if hasattr(v,'_fieldnames') else v[0]
        for k in vv._fieldnames: x=getattr(vv,k); print(' ',k,getattr(x,'shape',None), x if np.size(x)<10 else '')
        es=obj.eventSeriesHash; print(es._fieldnames, es.keyNames[:5], es.descr[:3] if np.size(es.descr)>1 else es.descr)
        u=es.value[0]; print(u._fieldnames)
        for k in u._fieldnames: x=getattr(u,k); print(' ',k,getattr(x,'shape',None), x if np.size(x)<5 else x[:5] if np.ndim(x)==1 else '')
        print('trialTypeStr',obj.trialTypeStr, obj.trialTypeMat.shape, obj.trialStartTimes[:5], obj.trialIds[:5])
        print('mem MB',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024)
        break
EOF
python crcns1.py 2>&1 | tail -60
```

```
Sat Nov 14 10:52:19 UTC 2026
read 324003182 12.557929039001465 b'MATLAB 5.0 MAT-file, Platform: PCWIN64, Created on: Thu Aug 16 12:36:12 2018                                        \x00\x00\x00\x00'
dict_keys(['__header__', '__version__', '__globals__', 'obj'])
['timeUnitIds', 'timeUnitNames', 'descrHash', 'trialTimeUnit', 'trialTypeStr', 'trialIds', 'trialStartTimes', 'trialTypeMat', 'trialPropertiesHash', 'timeSeriesHash', 'timeSeriesArrayHash', 'eventSeriesHash']
timeUnitIds <class 'numpy.ndarray'> (5,) [1 2 3 4 5]
timeUnitNames <class 'numpy.ndarray'> (5,) ['millisecond' 'second' 'minute' 'hour' 'day']
descrHash <class 'scipy.io.matlab._mio5_params.mat_struct'> None <scipy.io.matlab._mio5_params.mat_struct object at 0x7fb4be4885f0>
trialTimeUnit <class 'int'> None 2
trialTypeStr <class 'numpy.ndarray'> (8,) ['HitR' 'HitL' 'ErrR' 'ErrL' 'NoLickR' 'NoLickL' 'LickEarly' 'StimTrials']
trialIds <class 'numpy.ndarray'> (400,) 
trialStartTimes <class 'numpy.ndarray'> (400,) 
trialTypeMat <class 'numpy.ndarray'> (8, 400) 
trialPropertiesHash <class 'scipy.io.matlab._mio5_params.mat_struct'> None <scipy.io.matlab._mio5_params.mat_struct object at 0x7fb4be488590>
timeSeriesHash <class 'numpy.ndarray'> (0,) []
timeSeriesArrayHash <class 'scipy.io.matlab._mio5_params.mat_struct'> None <scipy.io.matlab._mio5_params.mat_struct object at 0x7fb4be4883b0>
eventSeriesHash <class 'scipy.io.matlab._mio5_params.mat_struct'> None <scipy.io.matlab._mio5_params.mat_struct object at 0x7fb4be48a390>
['keyNames', 'descr', 'value'] ['PoleInTime' 'PoleOutTime' 'CueTime' 'GoodTrials' 'PhotostimulationType'] ['Start of Sample period (in seconds, relative to trial start time)'
 'Start of Delay period (in seconds, relative to trial start time)'
 'Start of Response period (in seconds, relative to trial start time)'
 '0 for trials in which mice are not performing, discard for analyses'
[... 33 more lines not kept]
```

**Agent**

CRCNS session structs hold GoodTrials, a 2-column CueTime, and per-trial laser power traces (no lick channel). Now a DANDI loader for all 54 sessions, timed.

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; cat > dl.py <<'EOF'
import remfile,h5py,requests,time,json,numpy as np,resource
from concurrent.futures import ThreadPoolExecutor
V='0.220126.1903'
r=requests.get(f"https://api.dandiarchive.org/api/dandisets/000007/versions/{V}/assets/?page_size=100").json()['results']
def load(a):
    url=f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/"
    url=requests.head(url,allow_redirects=True).url
    f=h5py.File(remfile.File(url),'r')
    T={k:f['intervals/trials/'+k][:] for k in ['start_time','stop_time','pole_in_time','pole_out_time','cue_time','response','lick_early','photo_stim_id','id']}
    u=f['units']; st=u['spike_times'][:]; idx=u['spike_times_index'][:]
    ct=u['cell_type'][:]; wf=u['waveform_mean'][:]
    og={k:json.loads(f['general/optogenetics/'+k+'/location'][()]) for k in f['general/optogenetics']}
    eg={k:f['general/extracellular_ephys/'+k+'/location'][()] for k in f['general/extracellular_ephys'] if k!='electrodes'}
    return a['path'],T,np.split(st,idx[:-1]),ct,wf,og,eg,f['general/subject/genotype'][()]
t0=time.time()
with ThreadPoolExecutor(8) as ex: out=list(ex.map(load,r))
print(time.time()-t0, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024)
import pickle; pickle.dump(out,open('dandi.pkl','wb'))
for p,T,sp,ct,wf,og,eg,g in out:
    print(p.split('/')[1][:-4], len(T['id']), len(sp), dict(zip(*np.unique(T['photo_stim_id'].astype(str),return_counts=True))), dict(zip(*np.unique(ct.astype(str),return_counts=True))), {k:(v['hemisphere'],v.get('brain_location')) for k,v in og.items()}, [json.loads(v).get('rec_coordinate_ml') for v in eg.values()], g)
EOF
python dl.py 2>&1 | tail -60
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/dl.py", line 16, in <module>
    with ThreadPoolExecutor(8) as ex: out=list(ex.map(load,r))
                                          ^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/.local/share/uv/python/cpython-3.12.16-linux-x86_64-gnu/lib/python3.12/concurrent/futures/_base.py", line 619, in result_iterator
    yield _result_or_cancel(fs.pop())
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/.local/share/uv/python/cpython-3.12.16-linux-x86_64-gnu/lib/python3.12/concurrent/futures/_base.py", line 317, in _result_or_cancel
    return fut.result(timeout)
           ^^^^^^^^^^^^^^^^^^^
  File "/home/runner/.local/share/uv/python/cpython-3.12.16-linux-x86_64-gnu/lib/python3.12/concurrent/futures/_base.py", line 456, in result
    return self.__get_result()
           ^^^^^^^^^^^^^^^^^^^
  File "/home/runner/.local/share/uv/python/cpython-3.12.16-linux-x86_64-gnu/lib/python3.12/concurrent/futures/_base.py", line 401, in __get_result
    raise self._exception
  File "/home/runner/.local/share/uv/python/cpython-3.12.16-linux-x86_64-gnu/lib/python3.12/concurrent/futures/thread.py", line 59, in run
    result = self.fn(*self.args, **self.kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/dl.py", line 13, in load
    eg={k:f['general/extracellular_ephys/'+k+'/location'][()] for k in f['general/extracellular_ephys'] if k!='electrodes'}
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; sed -i "s#eg={k:f\['general/extracellular_ephys/'+k+'/location'\]\[()\]#eg={k:f['general/extracellular_ephys/'+k].attrs.get('location','{}')#" dl.py; sed -i "s#og={k:json.loads(f\['general/optogenetics/'+k+'/location'\]\[()\])#og={k:json.loads(f['general/optogenetics/'+k+'/location'][()] or '{}')#" dl.py; python dl.py 2>&1 | tail -60
```

```
35.26839232444763 344.91796875
sub-anm00314756_ses-20151020T194211 211 20 {np.str_('0'): np.int64(164), np.str_('3'): np.int64(20), np.str_('4'): np.int64(27)} {np.str_('pyramidal'): np.int64(20)} {'Dentate': ('right', 'Dentate')} ['-1.5'] b'unknown'
sub-anm00314756_ses-20151023T141029 246 6 {np.str_('0'): np.int64(189), np.str_('3'): np.int64(31), np.str_('4'): np.int64(26)} {np.str_('pyramidal'): np.int64(6)} {'Dentate': ('right', 'Dentate')} ['-1.5'] b'unknown'
sub-anm00314746_ses-20151020T093604 276 23 {np.str_('0'): np.int64(213), np.str_('1'): np.int64(37), np.str_('2'): np.int64(26)} {np.str_('pyramidal'): np.int64(23)} {'Fastigial': ('right', 'Fastigial')} ['-1.5'] b'unknown'
sub-anm00314746_ses-20151022T151738 258 21 {np.str_('0'): np.int64(202), np.str_('1'): np.int64(30), np.str_('2'): np.int64(26)} {np.str_('pyramidal'): np.int64(21)} {'Fastigial': ('right', 'Fastigial')} ['-1.5'] b'unknown'
sub-anm00314746_ses-20151021T112541 246 19 {np.str_('0'): np.int64(191), np.str_('1'): np.int64(22), np.str_('2'): np.int64(33)} {np.str_('FS'): np.int64(3), np.str_('pyramidal'): np.int64(16)} {'Fastigial': ('right', 'Fastigial')} ['-1.5'] b'unknown'
sub-anm00314757_ses-20151021T180248 34 25 {np.str_('0'): np.int64(27), np.str_('1'): np.int64(2), np.str_('2'): np.int64(5)} {np.str_('FS'): np.int64(2), np.str_('pyramidal'): np.int64(23)} {'Fastigial': ('left', 'Fastigial')} ['1.5'] b'unknown'
sub-anm00314757_ses-20151020T173731 246 13 {np.str_('0'): np.int64(192), np.str_('1'): np.int64(31), np.str_('2'): np.int64(23)} {np.str_('FS'): np.int64(1), np.str_('pyramidal'): np.int64(12)} {'Fastigial': ('left', 'Fastigial')} ['1.5'] b'unknown'
sub-anm00314758_ses-20151021T101014 296 14 {np.str_('0'): np.int64(228), np.str_('1'): np.int64(42), np.str_('2'): np.int64(26)} {np.str_('pyramidal'): np.int64(14)} {'Fastigial': ('right', 'Fastigial')} ['-1.5'] b'unknown'
sub-anm00314758_ses-20151022T112047 257 10 {np.str_('0'): np.int64(202), np.str_('1'): np.int64(24), np.str_('2
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; cat > crcns_all.py <<'EOF'
import fsspec,tarfile,time,io,scipy.io as sio, numpy as np, resource, pickle
def s2d(o):
    if isinstance(o,sio.matlab.mat_struct): return {k:s2d(getattr(o,k)) for k in o._fieldnames}
    return o
t0=time.time(); out={}; meta={}
for d in ['ALM_recording_DCN_photoactivation','ALM_recording_DCN_photoinhibition']:
  f=fsspec.open(f'https://crcnsarchive.s3-us-west-2.amazonaws.com/alm-4/live/{d}/datafiles.tar.gz',block_size=2**24).open()
  tf=tarfile.open(fileobj=f,mode='r|gz')
  for m in tf:
    if not m.isfile(): continue
    name=m.name.split('/')[-1][:-4]
    b=tf.extractfile(m).read()
    dd=sio.loadmat(io.BytesIO(b),squeeze_me=True,struct_as_record=False); del b
    if name.startswith('meta_data'):
        meta[name[10:]]=s2d(dd['meta_data']); continue
    o=dd['obj']; tp=o.trialPropertiesHash
    S=dict(trialIds=o.trialIds, start=o.trialStartTimes, tts=o.trialTypeStr, ttm=o.trialTypeMat, keys=tp.keyNames, props=list(tp.value), pdescr=tp.descr)
    ts=o.timeSeriesArrayHash.value
    tt=ts.time; vm=ts.valueMatrix; n=tt.shape[1]
    pw=vm[:,n:2*n]; aom=vm[:,:n]
    rows=[]
    for i in range(tt.shape[0]):
        p=pw[i]; on=np.flatnonzero(p>0.05*max(p.max(),1e-9)) if p.max()>0.05 else []
        if len(on): rows.append((tt[i,on[0]],tt[i,on[-1]],p[on[0]:on[-1]+1].mean(),p.max()))
        else: rows.append((np.nan,np.nan,0.0,p.max()))
    S['laser']=np.array(rows); S['laser_t0']=tt[:,0]; S['laser_dt']=np.median(np.diff(tt[0]))
    S['idStr']=ts.idStr
    U=[]
    for k,u in zip(o.eventSeriesHash.keyNames,o.eventSeriesHash.value):
        U.append(dict(key=k,t=np.atleast_1d(u.eventTimes),tr=np.atleast_1d(u.eventTrials),ct=u.cellType,wf=np.atleast_2d(u.waveforms).mean(0),ch=np.median(u.channel)))
    S['units']=U
    out[name[15:]]=S
    del dd,o,ts,tt,vm,pw,aom
    print(name, round(time.time()-t0), int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024),flush=True)
pickle.dump((out,meta),open('crcns.pkl','wb'))
print('done',time.time()-t0)
EOF
python crcns_all.py 2>&1 | tail -25
```

```
data_structure_BAYLORNL15_20170602 13 1364
data_structure_BAYLORNL14_20170607 24 2112
data_structure_BAYLORNL15_20170605 34 2165
data_structure_BAYLORCD6_20170612 45 2204
data_structure_BAYLORNL12_20170614 60 2849
Traceback (most recent call last):
  File "/tmp/claude-1001/crcns_all.py", line 19, in <module>
    tt=ts.time; vm=ts.valueMatrix; n=tt.shape[1]
                                     ~~~~~~~~^^^
IndexError: tuple index out of range
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; python - <<'EOF'
import re
s=open('crcns_all.py').read()
old=s[s.index("    tt=ts.time"):s.index("    S['idStr']")]
new='''    tt=ts.time; vm=ts.valueMatrix; ids=list(ts.idStr); ip=ids.index('laser_power')
    if tt.ndim==2:
        n=tt.shape[1]; pw=vm[:,ip*n:(ip+1)*n]; S['form']='2d'
        S['halfmax']=[vm[:,:n].max(),vm[:,n:2*n].max()]
        trials=[(tt[i],pw[i]) for i in range(tt.shape[0])]
    else:
        S['form']='1d'; tr=ts.trial; pwv=vm[:,ip]
        brk=np.flatnonzero(np.diff(tr))+1; seg=np.split(np.arange(len(tr)),brk)
        trials=[(tt[g],pwv[g]) for g in seg]; S['laser_trial']=np.array([tr[g[0]] for g in seg])
        S['halfmax']=list(vm.max(0))
    rows=[]
    for t_,p in trials:
        on=np.flatnonzero(p>0.05*p.max()) if p.max()>0.05 else []
        if len(on): rows.append((t_[0],t_[on[0]],t_[on[-1]],p[on[0]:on[-1]+1].mean(),p.max()))
        else: rows.append((t_[0],np.nan,np.nan,0.0,p.max()))
    S['laser']=np.array(rows); S['laser_dt']=np.median(np.diff(trials[0][0]))
'''
s=s.replace(old,new).replace("del dd,o,ts,tt,vm,pw,aom","del dd,o,ts,tt,vm,trials")
open('crcns_all.py','w').write(s)
EOF
python crcns_all.py 2>&1 | tail -8
```

```
data_structure_BAYLORCD14_20171025 582 3897
data_structure_BAYLORCD8_20171018 605 3897
data_structure_BAYLORCD12_20180129 618 3897
data_structure_BAYLORCD13_20171214 630 3897
data_structure_BAYLORCD14_20171024 641 3897
data_structure_BAYLORCD14_20171026 672 3897
data_structure_BAYLORCD12_20180125 750 3897
done 749.6856174468994
Shell cwd was reset to
```

**Agent**

CRCNS pass: 12.5 min, 3.9 GB peak. Now comparing it with DANDI and checking the laser traces and metadata.

**Agent calls Bash**

```bash
date -u; cd $TMPDIR; . venv/bin/activate; python - <<'EOF'
import pickle,numpy as np,collections
out,meta=pickle.load(open('crcns.pkl','rb'))
D=pickle.load(open('dandi.pkl','rb'))
print(len(out),len(meta))
k0=sorted(meta)[0]; print(k0, meta[k0])
for k in sorted(meta): 
    e=meta[k].get('extracellular',{}); print(k, {kk:e[kk] for kk in e if kk in ('recordingCoordinates','penetrationN','probeType','recordingMarker','groundCoordinates')}, meta[k].get('photostim',''))
EOF
```

```
Sat Nov 14 11:08:00 UTC 2026
54 54
ANM314746_20151020 {'species': 'Mus musculus', 'animalStrain': '000664', 'animalGeneModification': array([], dtype=object), 'animalSource': 'JAX', 'animalGeneCopy': array([], dtype=object), 'animalGeneticBackground': 'unidentified', 'animalID': 'anm00314746', 'sex': 'm', 'dateOfBirth': '20150630', 'dateOfExperiment': '20151020', 'timeOfExperiment': '093604', 'experimenters': 'Nuo Li', 'citation': '**PMID currently not avaliable', 'whiskerConfig': 'full', 'weightBefore': array([], dtype=object), 'weightAfter': array([], dtype=object), 'experimentType': array(['behavior', 'extracellular', 'photostim'], dtype=object), 'referenceAtlas': 'Allen Reference Atlas', 'surgicalManipulation': 'virus injection', 'virus': {'virusSource': 'UNC', 'virusID': 'AAV2-hSyn-hChR2(H134R)-EYFP', 'virusLotNumber': array([], dtype=object), 'infectionCoordinates': array([-2.5,  0.8,  2.4]), 'infectionLocation': 'right Fastigial (coordinates are from lambda)', 'virusTiter': 'untitered', 'injectionVolume': 150, 'injectionDate': '20150825'}, 'extracellular': {'recordingCoordinates': array([ 2.5, -1.5,  nan]), 'recordingLocation': 'ALM', 'recordingMarker': 'stereotaxic', 'recordingType': 'acute', 'penetrationN': 1, 'probeSource': array(['neuronexus', 'Janelia Research Campus', 'Cambridge NeuroTech'],
      dtype=object), 'probeType': array(['NN 32ch A4x8-5mm-100-200-177', 'Janelia APIG 64ch',
       'Cambridge NeuroTech 64ch H2 probe'], dtype=object), 'groundCoordinates': array([-3, -1,  1], dtype=int16), 'referenceCoordinates': array([], dtype=uint8), 'siteLocations': array([], dtype=uint8), 'extracellularDataType': array(['sorted spike times', 'spike waveform snipets',
       'spike band voltage traces'], dtype=object), 'cellType': array(['pyramidal', 'interneuron'], dtype=object), 'identificationMethod': array(['waveform shape', 'waveform shape'], dtype=object), 'amplifierRolloff': array([], dtype=object), 'spikeSorting': 'manual', 'ADunit': '14 bits'}, 'phot
[... 90 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; python - <<'EOF'
import pickle,numpy as np,collections
out,meta=pickle.load(open('crcns.pkl','rb'))
D=pickle.load(open('dandi.pkl','rb'))
for p,T,sp,ct,wf,og,eg,g in sorted(D,key=lambda x:x[0]):
    sub=p.split('/')[0][4:]; ses=p.split('_ses-')[1][:8]
    key=(sub.replace('anm00','ANM') if sub.startswith('anm') else sub)+'_'+ses
    S=out[key]; P=dict(zip(S['keys'],S['props']))
    good=P['GoodTrials']; pt=P['PhotostimulationType']; st=S['start']
    # match trials by start time
    m=np.searchsorted(st,T['start_time']-1e-3)
    ok=np.abs(st[np.minimum(m,len(st)-1)]-T['start_time'])<0.01
    tts=list(S['tts']); 
    le=S['ttm'][tts.index('LickEarly')]
    cue=P['CueTime']; cue1=cue[:,0] if cue.ndim==2 else cue
    mm=m[ok]
    dcue=np.nanmax(np.abs(T['cue_time'][ok]-(st[mm]+cue1[mm])))
    dle=np.sum(T['lick_early'][ok]!=le[mm])
    nu=len(S['units']); same=sum(len(a)==len(b['t']) and np.allclose(a,b['t']) for a,b in zip(sp,S['units']))
    ctc=sum(str(a)==str(b['ct'] if np.size(b['ct']) else 'unknown') for a,b in zip(ct.astype(str),S['units']))
    print(key, 'D',len(T['start_time']),'C',len(st),'good',int(np.nansum(good)),'matched',ok.sum(),'goodOfMatched',int(good[mm].sum()), 'ptNaN',int(np.isnan(pt).sum()),'dcue',round(dcue,4),'dLE',dle,'units',len(sp),nu,'sameSpikes',same,'ct',ctc, 'cue2col', cue.ndim==2)
EOF
```

```
BAYLORCD12_20180125 D 273 C 344 good 315 matched 172 goodOfMatched 172 ptNaN 43 dcue 0.005 dLE 0 units 20 20 sameSpikes 20 ct 20 cue2col True
BAYLORCD12_20180126 D 256 C 336 good 309 matched 163 goodOfMatched 163 ptNaN 54 dcue 0.005 dLE 0 units 22 22 sameSpikes 22 ct 21 cue2col True
BAYLORCD12_20180128 D 318 C 400 good 384 matched 186 goodOfMatched 186 ptNaN 66 dcue 0.005 dLE 0 units 22 22 sameSpikes 22 ct 22 cue2col True
BAYLORCD12_20180129 D 196 C 280 good 214 matched 115 goodOfMatched 115 ptNaN 18 dcue 0.005 dLE 0 units 44 44 sameSpikes 44 ct 41 cue2col True
BAYLORCD12_20180130 D 162 C 216 good 186 matched 104 goodOfMatched 104 ptNaN 26 dcue 0.005 dLE 0 units 52 52 sameSpikes 52 ct 50 cue2col True
BAYLORCD13_20171211 D 15 C 106 good 15 matched 15 goodOfMatched 15 ptNaN 0 dcue 0.0 dLE 0 units 38 38 sameSpikes 38 ct 37 cue2col True
BAYLORCD13_20171212 D 119 C 177 good 119 matched 71 goodOfMatched 71 ptNaN 0 dcue 0.005 dLE 0 units 22 22 sameSpikes 22 ct 22 cue2col True
BAYLORCD13_20171213 D 298 C 311 good 298 matched 194 goodOfMatched 194 ptNaN 0 dcue 0.005 dLE 0 units 14 14 sameSpikes 14 ct 14 cue2col True
BAYLORCD13_20171214 D 294 C 317 good 295 matched 196 goodOfMatched 196 ptNaN 1 dcue 0.005 dLE 0 units 19 19 sameSpikes 19 ct 19 cue2col True
BAYLORCD13_20171215 D 241 C 269 good 241 matched 164 goodOfMatched 164 ptNaN 0 dcue 0.005 dLE 0 units 7 7 sameSpikes 7 ct 7 cue2col True
BAYLORCD14_20171024 D 239 C 310 good 239 matched 25 goodOfMatched 25 ptNaN 0 dcue 0.01 dLE 0 units 43 43 sameSpikes 43 ct 41 cue2col True
BAYLORCD14_20171025 D 281 C 337 good 281 matched 190 goodOfMatched 190 ptNaN 0 dcue 0.005 dLE 0 units 42 42 sameSpikes 42 ct 42 cue2col True
BAYLORCD14_20171026 D 497 C 511 good 499 matched 323 goodOfMatched 323 ptNaN 2 dcue 0.005 dLE 0 units 27 27 sameSpikes 27 ct 26 cue2col True
BAYLORCD14_20171027 D 359 C 378 good 359 matched 214 goodOfMatched 214 ptNaN 0 dcue 0.005 dLE 0 units 43 43 sameSpikes 43 ct 41 cue2col True
BAYLORCD14_20171028 D 343 C 400 good
[... 40 more lines not kept]
```

**Agent**

Spike times are identical in all 54 sessions. DANDI holds fewer trials than CRCNS; I'll match trials by nearest start time to see which trials DANDI drops.

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; python - <<'EOF'
import pickle,numpy as np,collections
out,meta=pickle.load(open('crcns.pkl','rb'))
D=pickle.load(open('dandi.pkl','rb'))
tot=collections.Counter()
for p,T,sp,ct,wf,og,eg,g in sorted(D,key=lambda x:x[0]):
    sub=p.split('/')[0][4:]; ses=p.split('_ses-')[1][:8]
    key=(sub.replace('anm00','ANM') if sub.startswith('anm') else sub)+'_'+ses
    S=out[key]; P=dict(zip(S['keys'],S['props'])); st=S['start']
    good=P['GoodTrials']==1; pt=P['PhotostimulationType']
    d=np.abs(st[:,None]-T['start_time'][None,:]); j=d.argmin(0); dm=d.min(0)
    ok=dm<0.006
    inD=np.zeros(len(st),bool); inD[j[ok]]=True
    # what CRCNS trials are not in DANDI
    tts=list(S['tts']); ttm=S['ttm']
    hasresp=ttm[[tts.index(x) for x in ['HitR','HitL','ErrR','ErrL','NoLickR','NoLickL']]].sum(0)>0
    miss=~inD
    c=collections.Counter(zip(good[miss],np.isnan(pt[miss]),hasresp[miss]))
    extra=inD & ~good
    print(key,'D',len(T['start_time']),'matched',ok.sum(),'maxdt',round(dm.max(),4),'missing(good,ptnan,hasresp):',dict(c),'DnotGood',extra.sum(), 'trialIds_contig', np.all(np.diff(S['trialIds'])==1))
    tot['good_missing']+=int((miss&good&~np.isnan(pt)).sum())
print(tot)
EOF
```

```
BAYLORCD12_20180125 D 273 matched 273 maxdt 0.005 missing(good,ptnan,hasresp): {(np.False_, np.False_, np.False_): 28, (np.True_, np.True_, np.True_): 42, (np.False_, np.True_, np.False_): 1} DnotGood 0 trialIds_contig True
BAYLORCD12_20180126 D 256 matched 256 maxdt 0.005 missing(good,ptnan,hasresp): {(np.False_, np.False_, np.False_): 26, (np.True_, np.True_, np.True_): 53, (np.False_, np.True_, np.False_): 1} DnotGood 0 trialIds_contig True
BAYLORCD12_20180128 D 318 matched 318 maxdt 0.005 missing(good,ptnan,hasresp): {(np.False_, np.False_, np.False_): 16, (np.True_, np.True_, np.True_): 66} DnotGood 0 trialIds_contig True
BAYLORCD12_20180129 D 196 matched 196 maxdt 0.005 missing(good,ptnan,hasresp): {(np.False_, np.False_, np.False_): 66, (np.True_, np.True_, np.True_): 18} DnotGood 0 trialIds_contig True
BAYLORCD12_20180130 D 162 matched 162 maxdt 0.005 missing(good,ptnan,hasresp): {(np.False_, np.False_, np.False_): 28, (np.True_, np.True_, np.True_): 24, (np.False_, np.True_, np.False_): 2} DnotGood 0 trialIds_contig True
BAYLORCD13_20171211 D 15 matched 15 maxdt 0.0 missing(good,ptnan,hasresp): {(np.False_, np.False_, np.False_): 91} DnotGood 0 trialIds_contig True
BAYLORCD13_20171212 D 119 matched 119 maxdt 0.005 missing(good,ptnan,hasresp): {(np.False_, np.False_, np.False_): 58} DnotGood 0 trialIds_contig True
BAYLORCD13_20171213 D 298 matched 298 maxdt 0.005 missing(good,ptnan,hasresp): {(np.False_, np.False_, np.False_): 13} DnotGood 0 trialIds_contig True
BAYLORCD13_20171214 D 294 matched 294 maxdt 0.005 missing(good,ptnan,hasresp): {(np.False_, np.False_, np.False_): 22, (np.True_, np.True_, np.True_): 1} DnotGood 0 trialIds_contig True
BAYLORCD13_20171215 D 241 matched 241 maxdt 0.005 missing(good,ptnan,hasresp): {(np.False_, np.False_, np.False_): 28} DnotGood 0 trialIds_contig True
BAYLORCD14_20171024 D 239 matched 25 maxdt 0.053 missing(good,ptnan,hasresp): {(np.False_, np.False_, np.False_): 71, (np.True_, np.False_, np.True_): 214} DnotGood 0 t
[... 45 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; python - <<'EOF'
import pickle,numpy as np,collections
out,meta=pickle.load(open('crcns.pkl','rb'))
D=pickle.load(open('dandi.pkl','rb'))
for p,T,sp,ct,wf,og,eg,g in sorted(D,key=lambda x:x[0]):
    sub=p.split('/')[0][4:]; ses=p.split('_ses-')[1][:8]
    key=(sub.replace('anm00','ANM') if sub.startswith('anm') else sub)+'_'+ses
    S=out[key]; P=dict(zip(S['keys'],S['props'])); st=S['start']
    good=P['GoodTrials']==1; pt=P['PhotostimulationType']
    d=np.abs(st[:,None]-T['start_time'][None,:]); j=d.argmin(0); dm=d.min(0)
    ok=dm<0.06; inD=np.zeros(len(st),bool); inD[j[ok]]=True
    gm=(good&~np.isnan(pt)&~inD).sum()
    if ok.sum()<len(T['start_time']) or gm>0: print(key,'D',len(T['start_time']),'matched',ok.sum(),'good&pt not in D',gm, 'ids of those', S['trialIds'][good&~np.isnan(pt)&~inD][:3], S['trialIds'][good&~np.isnan(pt)&~inD][-3:], 'D start range', T['start_time'][[0,-1]], 'C', st[[0,-1]], 'pstim of missing', collections.Counter(pt[good&~np.isnan(pt)&~inD]))
EOF
```

```
ANM314746_20151022 D 258 matched 258 good&pt not in D 26 ids of those [279 280 281] [302 303 304] D start range [1283.34 3657.02] C [2.29286800e+00 3.98326561e+03] pstim of missing Counter({np.uint8(0): 18, np.uint8(1): 6, np.uint8(2): 2})
ANM314757_20151021 D 34 matched 34 good&pt not in D 268 ids of those [48 49 50] [313 314 315] D start range [ 970.405 1302.87 ] C [2.72221000e+00 4.06564996e+03] pstim of missing Counter({np.uint8(0): 207, np.uint8(2): 33, np.uint8(1): 28})
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; python - <<'EOF'
import pickle,numpy as np,collections
out,meta=pickle.load(open('crcns.pkl','rb'))
for key in sorted(out):
    S=out[key]; P=dict(zip(S['keys'],S['props'])); st=S['start']
    L=S['laser']; good=P['GoodTrials']==1; pt=P['PhotostimulationType']
    if S['form']=='1d':
        # map laser rows to trial ids
        idx=np.searchsorted(S['trialIds'],S['laser_trial'])
        LL=np.full((len(st),5),np.nan); LL[idx]=L; L=LL
    rel_on=L[:,1]-st; rel_off=L[:,2]-st
    po=P['PoleOutTime']; pi=P['PoleInTime']; cue=P['CueTime']; cue1=cue[:,0] if cue.ndim==2 else cue
    res=[]
    for c in [0,1,2,3,4,5,6]:
        m=good&(pt==c)
        if m.sum()==0: continue
        ref=pi if c in (1,3) else po
        on=rel_on[m]-ref[m]; dur=rel_off[m]-rel_on[m]; pw=L[m,3]
        res.append(f"c{c} n{m.sum()} lit{np.mean(np.isfinite(on)):.2f} on{np.nanmedian(on):.3f}[{np.nanmin(on) if np.isfinite(on).any() else np.nan:.3f},{np.nanmax(on) if np.isfinite(on).any() else np.nan:.3f}] dur{np.nanmedian(dur):.3f} pw{np.unique(np.round(pw[np.isfinite(on)],1))[:5]}")
    print(key, S['form'], S['laser_dt'], S['halfmax'] if len(S['halfmax'])<4 else '', ' | '.join(res))
    if key.startswith('BAYLORCD8_20171018'): print('cue2', np.nanmedian(cue[:,1]-cue[:,0]), cue[:5])
EOF
```

```
<stdin>:18: RuntimeWarning: All-NaN slice encountered
ANM314746_20151020 1d 9.999999997489795e-05 [np.float64(1.2694512551887545), np.float64(nan)] c0 n213 lit0.00 onnan[nan,nan] durnan pw[] | c1 n37 lit1.00 on0.000[0.000,0.000] dur1.300 pw[1.1] | c2 n26 lit1.00 on0.000[0.000,0.000] dur1.300 pw[1.1]
ANM314746_20151021 1d 9.999999997489795e-05 [np.float64(1.2633230669707889), np.float64(nan)] c0 n191 lit0.00 onnan[nan,nan] durnan pw[] | c1 n22 lit1.00 on0.000[0.000,0.000] dur0.500 pw[1.1] | c2 n33 lit1.00 on0.000[0.000,0.000] dur0.500 pw[1.1]
ANM314746_20151022 1d 9.999999997489795e-05 [np.float64(1.2665484291822962), np.float64(10.214100235341096)] c0 n220 lit0.00 onnan[nan,nan] durnan pw[] | c1 n36 lit0.83 on0.000[0.000,0.000] dur0.500 pw[1.1] | c2 n28 lit0.93 on0.000[0.000,0.000] dur0.500 pw[1.1]
ANM314756_20151020 1d 9.999999997489795e-05 [np.float64(1.304285168464974), np.float64(nan)] c0 n164 lit0.00 onnan[nan,nan] durnan pw[] | c3 n20 lit1.00 on0.000[-0.495,0.000] dur0.828 pw[0.1 0.2 0.3 0.5 1. ] | c4 n27 lit1.00 on0.000[-1.823,0.000] dur0.778 pw[0.1 0.2 0.3 0.4 0.5]
ANM314756_20151023 1d 9.999999997489795e-05 [np.float64(1.2639681394115851), np.float64(nan)] c0 n189 lit0.00 onnan[nan,nan] durnan pw[] | c3 n31 lit1.00 on0.000[0.000,0.000] dur0.500 pw[1.  1.1] | c4 n26 lit1.00 on0.000[-7.184,0.000] dur0.500 pw[0.1 1.  1.1]
ANM314757_20151020 1d 0.00010000000020227162 [np.float64(1.260742777215121), np.float64(nan)] c0 n192 lit0.00 onnan[nan,nan] durnan pw[] | c1 n31 lit1.00 on0.000[0.000,0.000] dur0.500 pw[0.5 1.1] | c2 n23 lit1.00 on0.000[0.000,0.000] dur0.500 pw[0.5 1.1]
ANM314757_20151021 1d 9.999999997489795e-05 [np.float64(1.260742777215121), np.float64(10.15687606727253)] c0 n234 lit0.00 onnan[nan,nan] durnan pw[] | c1 n30 lit0.83 on-0.572[-0.573,1.301] dur5.000 pw[0.1 0.9 1.1] | c2 n38 lit0.89 on-1.873[-2.446,0.000] dur5.000 pw[0.1 0.9 1.1]
ANM314758_20151020 1d 9.999999997489795e-05 [np.float64(1.2626779945307447), np.float64(nan)] c0 n200 lit0.00 onnan
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd  sed -n 1,80p entries/fouke-2025/omr.py; python -c "
import json;d=json.load(open('entries/fouke-2025/reproduce_fouke_2025.ipynb'));
for c in d['cells'][:6]: print(c['cell_type'],c.get('metadata'),''.join(c['source'])[:600]);print('---')"
```

```
Sat Nov 14 11:09:39 UTC 2026
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
[... 124 more lines not kept]
```

**Agent**

Helper design is settled. Checking the paper's Methods passages on the coding direction and latency before coding.

**Agent calls Bash**

```bash
cd paper; grep -n -i -E "coding direction|latency|10 ms bins|400 ms|screen|preferred|hierarchical|bootstrap" 10.1038-s41586-018-0633-x.txt | cut -c1-600 | head -40
```

```
17:We tested fastigial involvement during specific behavioral epochs by disrupting activity using channelrhodopsin-2 (ChR2) activation (photo-activation, Fig 1f , Methods). Fastigial photo-activation during the early sample epoch had no effect on behavioral choice (p>0.05 for either trial type, bootstrap, Methods). Photo-activation during the delay and response epochs both resulted in incorrect choices ( Fig 1g–h ). Incorrect choices were induced even when the photostimuli ceased 800 ms before the movement. Photo-activation during the delay epoch biased future movements to either the contralat
19:Fastigial photo-activation did not block or perturb the frequency and duration of licking movements after initiation of licking bouts ( Fig 1i ). Fastigial photo-activation during the delay epoch did not evoke early licks ( Extended Data Fig 1f ). These data show that rhythmic licking is independent of fastigial activity, but they do not rule out fastigial involvement in controlling the direction and timing of licking bouts via its descending input to oscillators in the medulla that drive licking 25 . Dentate photo-activation produced little effect on behavioral choice ( Fig 1g , p=0.06, bo
21:We tested for necessity by silencing fastigial activity. We photostimulated ChR2 expressing Purkinje cells, which inhibited CN activity (photo-inhibition, Fig 1j ; Extended Data Fig 2 , Methods). Photo-inhibition during the early sample epoch did not affect behavioral choice ( Fig 1k , p>0.05 for either trial type, bootstrap, Methods). Photo-inhibition during the late sample and delay epochs resulted in incorrect behavioral choices, with a larger effect induced in the delay epoch ( Fig 1k , Extended Data Fig 2g–h ). Photo-inhibition during the delay epoch biased future movements to either t
29:Preparatory activity was present in all three cerebellar nuclei ( Extended Data Fig 3 – 4 ). In the fastigial nucleus, distinct patterns of selectivity were observed during the early versus late
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 109,111p 10.1038-s41586-018-0633-x.txt | cut -c1-2500; sed -n 129,129p 10.1038-s41586-018-0633-x.txt | cut -c500-2000; sed -n 139,145p 10.1038-s41586-018-0633-x.txt | cut -c1-1800
```

```
Performance was computed as the fraction of correct choices, excluding lick early trials and no lick trials ( Fig 1g , Extended Data Figs 1e , 2g , 10b ). Chance performance was 50%. We also separately computed the performance for “lick right” and “lick left” trials ( Fig 1 ; Extended Data Figs 1 , 2 , 6 , 10 ). Significance of the performance change in each photostimulation condition was determined using bootstrap to account for variability across mice, sessions, and trials. We tested against the null hypothesis that the performance change caused by photostimulation was due to normal behavioral variability. In each round of bootstrap, we replaced the original behavioral dataset with a re-sampled dataset in which we re-sampled with replacement from: 1) mice, 2) sessions performed by each mice, 3) the trials within each session. We then computed the performance change on the re-sampled dataset. Repeating this procedure 10,000 times produced a distribution of performance changes that reflected the behavioral variability. The p-value of the observed performance change was computed as the fraction of times the bootstrap produced an inconsistent performance change (e.g. if a performance decrease was observed during photostimulation, the p-value was the fraction of times a performance increase was observed during bootstrap, one-tailed test).

## Electrophysiology
or ALM, 20 for CN), selectivity was calculated as the spike rate difference between “lick left” and “lick right” trials on the remaining data. Selecting preferred trial type using either sample, delay, or response epoch data yielded qualitatively similar preparatory activity.
Average spike counts were computed in 400 ms windows in 10 ms steps. For each movement direction ( “lick right” and “lick left”) we computed the average spike counts x ¯ l i c k r i g h t and x ¯ l i c k l e f t , n × 1 response vectors that described the population response at each time point, t . We computed the difference in the mean resp
[... 6 more lines not kept]
```

**Agent**

Writing the helper module now.

**Agent calls Write**

```json
{
 "file_path": "entries/gao-2018/gao2018.py",
 "content": "\"\"\"Loading and measures for Gao et al. (2018), \"A cortico-cerebellar loop for motor planning\",\nNature 563, 113-116, doi:10.1038/s41586-018-0633-x, on its two datasets.\n\n- DANDI:000007, version 0.220126.1903: 54 NWB files (13 mice) of ALM single units, a trial\n  table and the photostimulation code of each trial. Streamed with remfile and h5py.\n- CRCNS:alm-4 (doi:10.6080/K0NS0S26, unversioned): the same 54 sessions as MATLAB structures\n  in two tar.gz archives (``datafiles.tar.gz``), with the GoodTrials flag, the trial type\n  matrix, the laser power trace of every trial and the unit waveforms, plus the lab's analysis\n  scripts (``analyses_scripts.zip``). The archives are gzip streams, which cannot be opened in\n  place, so each is read once from start to end over HTTP and every member is reduced in\n  memory as it passes; nothing is written to disk. One archive (7.4 GB) takes about 6 minutes.\n\nWhere the parameters come from (claims file ``claims/gao-2018.yaml``, shared methods B1 and\nE1 to E6, cited there from the paper's Methods and legends):\n\n- Trials. Neural analyses use trials with GoodTrials = 1, a photostimulation code that is not\n  NaN, no early lick, and inside the unit's stable range (its first to last trial with a\n  spike). The paper's Methods give none of these; they are taken from the analysis scripts\n  deposited with CRCNS:alm-4 (``analysis_compile_all_ALM_data.m`` and the other compile\n  scripts), which the paper's reporting summary announces (\"Custom analysis scripts and data\n  will be deposited on CRCNS.org\").\n- Epochs. Sample: pole in to pole out; delay: pole out to the go cue; response: go cue to\n  1.3 s after it (scripts, ``Cue_Time + 1.3``; the claims file's reading (a) of E2). Rates are\n  spike counts divided by the window length, as in the scripts.\n- Units. Putative pyramidal neurons are those whose ``cellType`` is \"pyramidal\" (E1; the\n  descriptor says this is the spike-width rule of the Methods).\n- Selectivity test (E2): two-tailed t-test, \"lick right\" against \"lick left\" trials, p < 0.05,\n  in any epoch.\n- Population selectivity (E3): preferred trial type from 10 screening trials of each type\n  (Methods, \"10 trials for ALM\"; the Fig. 2 script draws 10 of each type), spike counts from\n  pole in to 1.3 s after the cue (scripts); PSTHs from the remaining trials, smoothed with a\n  200 ms boxcar (``func_getPSTH.m``), here evaluated on a 10 ms grid (a standard choice for\n  a detail that cannot change a result).\n- Photostimulation effect (E4): t-test, control against photostimulation trials, both trial\n  types pooled, p < 0.01. A neuron is tested when it has at least 8 control trials of each\n  type and more than 3 photostimulation trials of each type (``analysis_compiled_all_ALM_\n  DCNstim_FR.m``).\n- Latency (E5): 10 ms bins in 1 ms steps, sign flipped for suppressed neurons, onset the first\n  bin whose population change differs from 0 (two-tailed t-test, p < 0.01), 10,000 bootstrap\n  resamples of neurons (Extended Data Fig. 9a legend).\n- Behavior (B1): fraction correct excluding early-lick and no-lick trials; hierarchical\n  bootstrap over mice, sessions and trials, 10,000 times (Methods, Behavioral data analysis).\n  Trials resampled within a session are drawn as a binomial count of correct trials, which is\n  the same distribution as resampling the trials with replacement.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport io\nimport json\nimport tarfile\nimport time\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport fsspec\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nimport requests\nimport scipy.io as sio\nfrom scipy import stats\n\nDANDISET_ID = \"000007\"\nDANDISET_VERSION = \"0.220126.1903\"\nCRCNS_ID = \"alm-4\"\nCRCNS_DOI = \"10.6080/K0NS0S26\"\nCRCNS_BASE = \"https://crcnsarchive.s3-us-west-2.amazonaws.com/alm-4/live/\"\n# MD5 sums from alm-4/live/checksums.md5, for the files read\nCRCNS_FILES = {\n    \"photoactivation\": (\"ALM_recording_DCN_photoactivation/datafiles.tar.gz\",\n                        \"12e9d7af630523ed2511826eeacf6b48\"),\n    \"photoinhibition\": (\"ALM_recording_DCN_photoinhibition/datafiles.tar.gz\",\n                        \"5123dc96df58457f853e2deb5ce479c7\"),\n}\nCRCNS_SCRIPTS = {\n    \"photoactivation\": (\"ALM_recording_DCN_photoactivation/analyses_scripts.zip\",\n                        \"601f4b52198614dbd4761a64d2658698\"),\n    \"photoinhibition\": (\"ALM_recording_DCN_photoinhibition/analyses_scripts.zip\",\n                        \"4639a8478bc307fb3a5a4b8f2a53fb58\"),\n}\nCODES = {0: \"control\", 1: \"fastigial sample\", 2: \"fastigial delay\", 3: \"dentate sample\",\n         4: \"dentate delay\", 5: \"CN inhibition delay 0.5 s\", 6: \"CN inhibition delay 1.3 s\"}\nOUTCOMES = [\"HitR\", \"HitL\", \"ErrR\", \"ErrL\", \"NoLickR\", \"NoLickL\"]\nRESPONSE_S = 1.3\n\n\n# ----------------------------------------------------------------------------- loading\n\n\ndef session_key(subject: str, date: str) -> str:\n    \"\"\"'ANM314746_20151020' style key from a DANDI subject id or a CRCNS file name.\"\"\"\n    s = subject.replace(\"sub-\", \"\")\n    if s.lower().startswith(\"anm00\"):\n        s = \"ANM\" + s[5:]\n    return f\"{s}_{date}\"\n\n\ndef _dandi_one(asset):\n    url = requests.head(f\"https://api.dandiarchive.org/api/assets/{asset['asset_id']}/download/\",\n                        allow_redirects=True, timeout=60).url\n    with h5py.File(remfile.File(url), \"r\") as f:\n        tr = {k: f[\"intervals/trials/\" + k][:] for k in\n              [\"start_time\", \"stop_time\", \"pole_in_time\", \"pole_out_time\", \"cue_time\",\n               \"response\", \"lick_early\", \"photo_stim_id\"]}\n        u = f[\"units\"]\n        st, idx = u[\"spike_times\"][:], u[\"spike_times_index\"][:]\n        og = {k: json.loads(f[f\"general/optogenetics/{k}/location\"][()] or \"{}\")\n              for k in f[\"general/optogenetics\"]}\n        eg = {k: json.loads(f[f\"general/extracellular_ephys/{k}\"].attrs.get(\"location\", \"{}\"))\n              for k in f[\"general/extracellular_ephys\"] if k != \"electrodes\"}\n        out = dict(path=asset[\"path\"], trials=pd.DataFrame({k: (v.astype(str) if v.dtype == object else v)\n                                                             for k, v in tr.items()}),\n                   spikes=np.split(st, idx[:-1]), cell_type=u[\"cell_type\"][:].astype(str),\n                   ogen=og, egroups=eg, genotype=f[\"general/subject/genotype\"][()].decode(),\n                   trial_columns={k: f[\"intervals/trials/\" + k].attrs.get(\"description\", \"\")\n                                  for k in f[\"intervals/trials\"]})\n    sub = asset[\"path\"].split(\"/\")[0]\n    out[\"key\"] = session_key(sub, asset[\"path\"].split(\"_ses-\")[1][:8])\n    return out\n\n\ndef load_dandi() -> dict:\n    \"\"\"Every NWB file of the pinned version, reduced to trials, spike times and metadata.\"\"\"\n    r = requests.get(f\"https://api.dandiarchive.org/api/dandisets/{DANDISET_ID}/versions/\"\n                     f\"{DANDISET_VERSION}/assets/?page_size=200\", timeout=60).json()\n    assets = [a for a in r[\"results\"] if a[\"path\"].endswith(\".nwb\")]\n    with ThreadPoolExecutor(8) as ex:\n        sessions = list(ex.map(_dandi_one, assets))\n    return {s[\"key\"]: s for s in sessions}\n\n\ndef _s2d(o):\n    if isinstance(o, sio.matlab.mat_struct):\n        return {k: _s2d(getattr(o, k)) for k in o._fieldnames}\n    return o\n\n\ndef _laser_rows(ts):\n    \"\"\"Per trial: (first sample time, laser on, laser off, mean power while on, peak power),\n    from the 'laser_power' channel of the Ephus time series.\"\"\"\n    ids = list(np.atleast_1d(ts.idStr))\n    ip = ids.index(\"laser_power\")\n    tt, vm = ts.time, ts.valueMatrix\n    if tt.ndim == 2:            # one row per trial, channels side by side\n        n = tt.shape[1]\n        trials = [(tt[i], vm[i, ip * n:(ip + 1) * n]) for i in range(tt.shape[0])]\n        trial_ids = None\n    else:                        # one long series with a trial number per sample\n        tr = ts.trial\n        seg = np.split(np.arange(len(tr)), np.flatnonzero(np.diff(tr)) + 1)\n        trials = [(tt[g], vm[g, ip]) for g in seg]\n        trial_ids = np.array([tr[g[0]] for g in seg])\n    rows = []\n    for t_, p in trials:\n        p = np.nan_to_num(p)\n        pk = p.max() if len(p) else 0.0\n        on = np.flatnonzero(p > 0.05 * pk) if pk > 0.05 else []\n        if len(on):\n            rows.append((t_[0], t_[on[0]], t_[on[-1]], p[on[0]:on[-1] + 1].mean(), pk))\n        else:\n            rows.append((t_[0], np.nan, np.nan, 0.0, pk))\n    return np.array(rows), trial_ids, tt.ndim\n\n\ndef _reduce_session(obj) -> dict:\n    tp = obj.trialPropertiesHash\n    props = dict(zip(tp.keyNames, tp.value))\n    tts = list(obj.trialTypeStr)\n    ttm = obj.trialTypeMat\n    cue = np.asarray(props[\"CueTime\"], float)\n    trial_ids = np.asarray(obj.trialIds)\n    n = len(trial_ids)\n    outcome = np.full(n, \"\", object)\n    for o in OUTCOMES:\n        outcome[ttm[tts.index(o)] == 1] = o\n    t = pd.DataFrame(dict(\n        trial_id=trial_ids, start=np.asarray(obj.trialStartTimes, float),\n        pole_in=np.asarray(props[\"PoleInTime\"], float), pole_out=np.asarray(props[\"PoleOutTime\"], float),\n        cue=cue[:, 0] if cue.ndim == 2 else cue,\n        cue_col2=cue[:, 1] if cue.ndim == 2 else np.nan,\n        good=np.asarray(props[\"GoodTrials\"]) == 1,\n        ptype=np.asarray(props[\"PhotostimulationType\"], float),\n        outcome=outcome, lick_early=ttm[tts.index(\"LickEarly\")] == 1,\n        stim_flag=ttm[tts.index(\"StimTrials\")] == 1))\n    rows, lt_ids, form = _laser_rows(obj.timeSeriesArrayHash.value)\n    lz = np.full((n, 5), np.nan)\n    if lt_ids is None:\n        lz[:len(rows)] = rows\n    else:\n        pos = np.searchsorted(trial_ids, lt_ids)\n        ok = (pos < n) & (trial_ids[np.minimum(pos, n - 1)] == lt_ids)\n        lz[pos[ok]] = rows[ok]\n    for j, c in enumerate([\"laser_t0\", \"laser_on\", \"laser_off\", \"laser_mean\", \"laser_peak\"]):\n        t[c] = lz[:, j]\n    t[\"laser_on\"] -= t.start\n    t[\"laser_off\"] -= t.start\n    t[\"laser_t0\"] -= t.start\n    units = []\n    for key, u in zip(np.atleast_1d(obj.eventSeriesHash.keyNames), np.atleast_1d(obj.eventSeriesHash.value)):\n        ev = np.atleast_1d(np.asarray(u.eventTimes, float))\n        etr = np.atleast_1d(np.asarray(u.eventTrials)).astype(int)\n        ct = u.cellType if isinstance(u.cellType, str) else (\n            \"\" if np.size(u.cellType) == 0 else str(np.atleast_1d(u.cellType)[0]))\n        units.append(dict(key=str(key), t=ev, trial=etr, cell_type=ct,\n                          waveform=np.atleast_2d(u.waveforms).mean(0), channel=float(np.median(u.channel))))\n    return dict(trials=t, units=units, laser_form=int(form),\n                trial_descr=[str(x) for x in np.atleast_1d(tp.descr).ravel()])\n\n\ndef stream_crcns(which: str, verbose: bool = True) -> tuple[dict, dict]:\n    \"\"\"Read one CRCNS archive from start to end, reducing each member in memory.\"\"\"\n    path, _ = CRCNS_FILES[which]\n    sessions, meta = {}, {}\n    t0 = time.time()\n    with fsspec.open(CRCNS_BASE + path, block_size=2 ** 24).open() as f:\n        with tarfile.open(fileobj=f, mode=\"r|gz\") as tf:\n            for m in tf:\n                if not m.isfile():\n                    continue\n                name = m.name.split(\"/\")[-1][:-4]\n                d = sio.loadmat(io.BytesIO(tf.extractfile(m).read()), squeeze_me=True,\n                                struct_as_record=False)\n                if name.startswith(\"meta_data_\"):\n                    meta[name[len(\"meta_data_\"):]] = _s2d(d[\"meta_data\"])\n                elif name.startswith(\"data_structure_\"):\n                    sessions[name[len(\"data_structure_\"):]] = _reduce_session(d[\"obj\"])\n                del d\n    if verbose:\n        print(f\"{path}: {len(sessions)} sessions, {len(meta)} meta files, {time.time() - t0:.0f} s\")\n    return sessions, meta\n\n\ndef read_script(which: str, name: str) -> str:\n    \"\"\"Text of one analysis script in the CRCNS zip, read in place.\"\"\"\n    import zipfile\n    path, _ = CRCNS_SCRIPTS[which]\n    with fsspec.open(CRCNS_BASE + path, block_size=2 ** 20).open() as f:\n        with zipfile.ZipFile(f) as z:\n            return z.read(f\"analyses_scripts/{name}\").decode(\"latin-1\")\n\n\n# ----------------------------------------------------------------------------- sessions\n\n\nclass Session:\n    \"\"\"One recording session in analysis form (from CRCNS:alm-4, checked against DANDI).\"\"\"\n\n    def __init__(self, key, s, meta):\n        self.key = key\n        self.mouse, self.date = key.split(\"_\")\n        t = s[\"trials\"].copy()\n        assert np.all(np.diff(t.trial_id) == 1) and t.trial_id.iloc[0] == 1\n        t[\"instructed\"] = np.where(t.outcome.str.endswith(\"R\"), \"R\",\n                                   np.where(t.outcome.str.endswith(\"L\"), \"L\", \"\"))\n        t[\"correct\"] = t.outcome.str.startswith(\"Hit\")\n        t[\"error\"] = t.outcome.str.startswith(\"Err\")\n        t[\"nolick\"] = t.outcome.str.startswith(\"NoLick\")\n        # licked direction: a hit licks the instructed side, an error the other one\n        t[\"licked\"] = np.where(t.correct, t.instructed,\n                               np.where(t.error, np.where(t.instructed == \"R\", \"L\", \"R\"), \"\"))\n        self.trials = t\n        ps = meta[\"photostim\"][\"photostimLocation\"]\n        self.cn_side, self.cn = ps.split()[0], ps.split()[1]\n        self.alm_ml = float(meta[\"extracellular\"][\"recordingCoordinates\"][1])\n        self.alm_side = \"left\" if self.alm_ml < 0 else \"right\"\n        codes = set(t.ptype[t.good & t.ptype.notna()].astype(int))\n        self.group = (\"fastigial\" if codes & {1, 2} else \"dentate\" if codes & {3, 4}\n                      else \"inhibition\")\n        self.units = []\n        st = t.start.to_numpy()\n        for u in s[\"units\"]:\n            ti = u[\"trial\"] - 1\n            ok = (ti >= 0) & (ti < len(t))\n            ti, ts = ti[ok], u[\"t\"][ok]\n            self.units.append(dict(key=u[\"key\"], cell_type=u[\"cell_type\"], ti=ti, rel=ts - st[ti],\n                                   first=ti.min() if len(ti) else 0, last=ti.max() if len(ti) else -1,\n                                   n_spikes=len(ts), waveform=u[\"waveform\"]))\n\n    def pyramidal(self):\n        return [u for u in self.units if u[\"cell_type\"] == \"pyramidal\"]\n\n    def base_mask(self):\n        \"\"\"Trials the scripts analyse: performing, a valid photostimulation code, no early lick.\"\"\"\n        t = self.trials\n        return (t.good & t.ptype.notna() & ~t.lick_early).to_numpy()\n\n    @staticmethod\n    def stable(u, n):\n        m = np.zeros(n, bool)\n        m[u[\"first\"]:u[\"last\"] + 1] = True\n        return m\n\n    def counts(self, u, a, b):\n        \"\"\"Spike count of unit u per trial in (a, b), times relative to trial start\n        (a and b are arrays over trials or scalars).\"\"\"\n        n = len(self.trials)\n        a = np.broadcast_to(np.asarray(a, float), (n,))\n        b = np.broadcast_to(np.asarray(b, float), (n,))\n        m = (u[\"rel\"] > a[u[\"ti\"]]) & (u[\"rel\"] < b[u[\"ti\"]])\n        return np.bincount(u[\"ti\"][m], minlength=n).astype(float)\n\n\ndef build_sessions(crcns: dict, meta: dict) -> list[Session]:\n    return [Session(k, crcns[k], meta[k]) for k in sorted(crcns)]\n\n\n# ----------------------------------------------------------------------------- behavior\n\n\ndef perf_table(sessions, codes, contra_from=\"paper\"):\n    \"\"\"One row per session, photostimulation code and instructed type: correct and total\n    trials (early-lick and no-lick trials excluded, Methods). 'side' is the instructed\n    direction relative to the manipulated CN: contra or ipsi. contra_from='paper' takes the\n    manipulated CN as contralateral to the recorded ALM (Methods; the photostimulation code\n    descriptions); 'metadata' takes the CN side the files give.\"\"\"\n    rows = []\n    for s in sessions:\n        t = s.trials\n        m = t.good & t.ptype.notna() & ~t.lick_early & ~t.nolick & (t.instructed != \"\")\n        if contra_from == \"paper\":\n            cn_side = \"right\" if s.alm_side == \"left\" else \"left\"\n        else:\n            cn_side = s.cn_side\n        contra_dir = \"L\" if cn_side == \"right\" else \"R\"\n        for c in codes:\n            for d in (\"L\", \"R\"):\n                mm = m & (t.ptype == c) & (t.instructed == d)\n                rows.append(dict(mouse=s.mouse, session=s.key, group=s.group, code=c, instructed=d,\n                                 side=\"contra\" if d == contra_dir else \"ipsi\",\n                                 n=int(mm.sum()), k=int((mm & t.correct).sum())))\n    return pd.DataFrame(rows)\n\n\ndef hier_boot(tab, stim_code, side=None, n_boot=10000, rng=None, ctrl_code=0):\n    \"\"\"Performance in control and stim trials and the one-tailed hierarchical bootstrap\n    p-value of the change (Methods): resample mice, then sessions of each mouse, then trials\n    of each session (as binomial counts), 10,000 times; p is the fraction of resamples whose\n    change has the sign opposite to the observed change. Also returns p_drop, the fraction of\n    resamples with no drop (change >= 0), which is the p of a test for a drop.\"\"\"\n    rng = rng or np.random.default_rng(0)\n    t = tab if side is None else tab[tab.side == side]\n    g = t.groupby([\"mouse\", \"session\", \"code\"])[[\"n\", \"k\"]].sum().reset_index()\n    ctrl = g[g.code == ctrl_code].set_index([\"mouse\", \"session\"])\n    stim = g[g.code == stim_code].set_index([\"mouse\", \"session\"])\n    idx = ctrl.index.intersection(stim.index)\n    idx = [i for i in idx if stim.loc[i, \"n\"] > 0 and ctrl.loc[i, \"n\"] > 0]\n    if not idx:\n        return dict(ctrl=np.nan, stim=np.nan, change=np.nan, p=np.nan, p_drop=np.nan, n_mice=0, n_sessions=0)\n    cn = np.array([ctrl.loc[i, \"n\"] for i in idx]); ck = np.array([ctrl.loc[i, \"k\"] for i in idx])\n    sn = np.array([stim.loc[i, \"n\"] for i in idx]); sk = np.array([stim.loc[i, \"k\"] for i in idx])\n    mice = np.array([i[0] for i in idx])\n    obs_c, obs_s = ck.sum() / cn.sum(), sk.sum() / sn.sum()\n    change = obs_s - obs_c\n    umice = np.unique(mice)\n    ses_of = [np.flatnonzero(mice == m) for m in umice]\n    chg = np.empty(n_boot)\n    for b in range(n_boot):\n        pick_m = rng.integers(0, len(umice), len(umice))\n        ses = np.concatenate([ses_of[m][rng.integers(0, len(ses_of[m]), len(ses_of[m]))] for m in pick_m])\n        kc = rng.binomial(cn[ses], ck[ses] / cn[ses]).sum()\n        ks = rng.binomial(sn[ses], sk[ses] / sn[ses]).sum()\n        chg[b] = ks / sn[ses].sum() - kc / cn[ses].sum()\n    p = np.mean(chg >= 0) if change < 0 else np.mean(chg <= 0)\n    return dict(ctrl=obs_c, stim=obs_s, change=change, p=p, p_drop=np.mean(chg >= 0),\n                n_ctrl=int(cn.sum()), n_stim=int(sn.sum()), n_mice=len(umice), n_sessions=len(idx))\n\n\n# ----------------------------------------------------------------------------- neurons\n\n\ndef selectivity_tests(s: Session, u, trials=\"correct\", response_s=RESPONSE_S):\n    \"\"\"E2: p-values of the t-test 'lick right' against 'lick left' in the sample, delay and\n    response epochs, control trials. trials='correct' (reading a; the Fig. 2 script) or\n    'all' (reading b: correct and error trials grouped by instructed type).\"\"\"\n    t = s.trials\n    n = len(t)\n    m = s.base_mask() & (t.ptype == 0).to_numpy() & s.stable(u, n)\n    m &= t.correct.to_numpy() if trials == \"correct\" else (t.correct | t.error).to_numpy()\n    R, L = m & (t.instructed == \"R\").to_numpy(), m & (t.instructed == \"L\").to_numpy()\n    pi, po, cue = t.pole_in.to_numpy(), t.pole_out.to_numpy(), t.cue.to_numpy()\n    out = {\"nR\": int(R.sum()), \"nL\": int(L.sum())}\n    for ep, (a, b) in dict(sample=(pi, po), delay=(po, cue), response=(cue, cue + response_s)).items():\n        r = s.counts(u, a, b) / (b - a)\n        if R.sum() >= 2 and L.sum() >= 2 and (np.var(r[R]) > 0 or np.var(r[L]) > 0):\n            out[ep] = stats.ttest_ind(r[R], r[L]).pvalue\n        else:\n            out[ep] = np.nan\n    return out\n\n\nGRID = np.round(np.arange(-3.5, 2.0001, 0.01), 3)  # time relative to the go cue, s\n\n\ndef psth(s: Session, u, mask, half=0.1):\n    \"\"\"Mean rate (spikes/s) over the trials in mask, in a 200 ms boxcar centred on each point\n    of GRID (relative to the go cue; func_getPSTH.m uses a 200 ms boxcar).\"\"\"\n    idx = np.flatnonzero(mask)\n    if len(idx) == 0:\n        return np.full(len(GRID), np.nan)\n    cue = s.trials.cue.to_numpy()\n    sel = np.isin(u[\"ti\"], idx)\n    rel = u[\"rel\"][sel] - cue[u[\"ti\"][sel]]\n    rel = np.sort(rel)\n    hi = np.searchsorted(rel, GRID + half, side=\"left\")\n    lo = np.searchsorted(rel, GRID - half, side=\"right\")\n    return (hi - lo) / (2 * half) / len(idx)\n\n\ndef pref_selectivity(s: Session, u, ctrl_mask, stim_masks, n_screen, rng):\n    \"\"\"E3: preferred type from n_screen control trials of each type (counts from pole in to\n    1.3 s after the cue), then preferred minus non-preferred PSTH on the remaining control\n    trials and on each stimulation condition. Returns (control, {name: stim}) or None.\"\"\"\n    t = s.trials\n    R = np.flatnonzero(ctrl_mask & (t.instructed == \"R\").to_numpy())\n    L = np.flatnonzero(ctrl_mask & (t.instructed == \"L\").to_numpy())\n    if len(R) <= n_screen or len(L) <= n_screen:\n        return None\n    R, L = rng.permutation(R), rng.permutation(L)\n    c = s.counts(u, t.pole_in.to_numpy(), t.cue.to_numpy() + RESPONSE_S)\n    pref_R = c[R[:n_screen]].mean() > c[L[:n_screen]].mean()\n    n = len(t)\n    mR = np.zeros(n, bool); mR[R[n_screen:]] = True\n    mL = np.zeros(n, bool); mL[L[n_screen:]] = True\n    sign = 1 if pref_R else -1\n    ctrl = sign * (psth(s, u, mR) - psth(s, u, mL))\n    out = {}\n    for name, sm in stim_masks.items():\n        out[name] = sign * (psth(s, u, sm & (t.instructed == \"R\").to_numpy())\n                            - psth(s, u, sm & (t.instructed == \"L\").to_numpy()))\n    return ctrl, out\n\n\ndef boot_mean_ci(x, rng, n_boot=10000, axis0=True):\n    \"\"\"Mean over rows and 95% bootstrap interval over rows (neurons or sessions).\"\"\"\n    x = np.asarray(x, float)\n    n = len(x)\n    means = np.empty((n_boot,) + x.shape[1:])\n    for b in range(n_boot):\n        means[b] = np.nanmean(x[rng.integers(0, n, n)], axis=0)\n    return np.nanmean(x, axis=0), np.percentile(means, 2.5, axis=0), np.percentile(means, 97.5, axis=0)\n\n\ndef stim_trials(s: Session, u, code, which=\"all\"):\n    \"\"\"E4 trial sets: control and code trials, both types pooled, within the unit's stable\n    range. which='all' (correct, error and no-lick, as the FR script) or 'correct'.\"\"\"\n    t = s.trials\n    n = len(t)\n    m = s.base_mask() & s.stable(u, n) & (t.instructed != \"\").to_numpy()\n    if which == \"correct\":\n        m &= t.correct.to_numpy()\n    ctrl = m & (t.ptype == 0).to_numpy()\n    stim = m & (t.ptype == code).to_numpy()\n    R, L = (t.instructed == \"R\").to_numpy(), (t.instructed == \"L\").to_numpy()\n    enough = (ctrl & R).sum() >= 8 and (ctrl & L).sum() >= 8 and (stim & R).sum() > 3 and (stim & L).sum() > 3\n    return ctrl, stim, enough\n\n\ndef modulation(s: Session, u, code, a_rel, b_rel, which=\"all\", ref=\"pole_out\"):\n    \"\"\"t-test of spike counts in (ref + a_rel, ref + b_rel), control against code trials.\n    b_rel may be 'cue' for the end of the delay. Returns p, rate change, rates.\"\"\"\n    ctrl, stim, enough = stim_trials(s, u, code, which)\n    if not enough:\n        return None\n    t = s.trials\n    r0 = t[ref].to_numpy()\n    a = r0 + a_rel\n    b = t.cue.to_numpy() if isinstance(b_rel, str) else r0 + b_rel\n    c = s.counts(u, a, b)\n    dur = b - a\n    rate = c / dur\n    p = stats.ttest_ind(c[ctrl], c[stim]).pvalue if (np.var(c[ctrl]) + np.var(c[stim])) > 0 else 1.0\n    return dict(p=p, rate_ctrl=rate[ctrl].mean(), rate_stim=rate[stim].mean(),\n                change=rate[stim].mean() - rate[ctrl].mean(), n_ctrl=int(ctrl.sum()), n_stim=int(stim.sum()))\n\n\ndef fine_change(s: Session, u, code, which=\"all\", t_from=-0.1, t_to=0.3, width=0.010, step=0.001):\n    \"\"\"Rate change (stim minus control, spikes/s) in `width` bins stepped by `step`, aligned to\n    delay onset (the photostimulation onset of codes 2, 4, 5, 6). Bins are labelled by start.\"\"\"\n    ctrl, stim, enough = stim_trials(s, u, code, which)\n    if not enough:\n        return None\n    t = s.trials\n    po = t.pole_out.to_numpy()\n    starts = np.round(np.arange(t_from, t_to + 1e-9, step), 4)\n    sel = np.isin(u[\"ti\"], np.flatnonzero(ctrl | stim))\n    rel = u[\"rel\"][sel] - po[u[\"ti\"][sel]]\n    ti = u[\"ti\"][sel]\n    out = []\n    for m in (ctrl, stim):\n        r = np.sort(rel[m[ti]])\n        hi = np.searchsorted(r, starts + width, side=\"left\")\n        lo = np.searchsorted(r, starts, side=\"right\")\n        out.append((hi - lo) / width / m.sum())\n    return starts, out[1] - out[0]\n\n\ndef latency(changes, signs, rng, n_boot=10000, alpha=0.01, starts=None, label_shift=0.0):\n    \"\"\"E5 onset: first bin (start >= 0) where the mean sign-flipped change differs from 0 by a\n    two-tailed one-sample t-test at p < alpha; bootstrap over neurons. label_shift is added to\n    the bin start to label a bin (0: start, 0.005: centre, 0.010: end). Returns onset on all\n    neurons, bootstrap mean and s.d. of the onset (ms), and the fraction of resamples with no\n    onset.\"\"\"\n    X = np.asarray(changes) * np.asarray(signs)[:, None]\n    valid = starts >= 0\n\n    def onset(Y):\n        mu, sd = Y.mean(0), Y.std(0, ddof=1)\n        tt = mu / (sd / np.sqrt(len(Y)))\n        p = 2 * stats.t.sf(np.abs(tt), len(Y) - 1)\n        hit = np.flatnonzero(valid & (p < alpha) & (mu > 0))\n        return (starts[hit[0]] + label_shift) * 1000 if len(hit) else np.nan\n\n    full = onset(X)\n    n = len(X)\n    ons = np.array([onset(X[rng.integers(0, n, n)]) for _ in range(n_boot)])\n    return dict(onset_all=full, boot_mean=np.nanmean(ons), boot_sd=np.nanstd(ons), no_onset=np.mean(np.isnan(ons)), n=n)\n\n\n# ----------------------------------------------------------------------------- coding direction\n\nCD_STARTS = np.round(np.arange(-3.5, 1.0001, 0.01), 3)  # window starts rel. go cue; windows 400 ms\nCD_WIN = 0.4\n\n\ndef cd_session(s: Session, rng, stim_code=None, min_neurons=5, min_trials=5):\n    \"\"\"E6 for one session. Neurons: pyramidal units stable from the 50th trial to the 50th\n    before the end (``analysis_compiled_all_ALM_DCNstim_CD.m``); trials inside every\n    neuron's stable range. Rates in 400 ms windows in 10 ms steps (labelled by window centre).\n    Control trials (correct and error) are split at random in halves; the cd is the mean\n    over windows centred in the delay epoch of mean 'lick right' minus mean 'lick left'\n    (correct trials of the first half), normalised to unit length. Returns None when the\n    session has <= min_neurons neurons or <= min_trials trials in a condition.\"\"\"\n    t = s.trials\n    n = len(t)\n    neurons = [u for u in s.pyramidal() if u[\"first\"] <= 49 and u[\"last\"] >= n - 51]\n    if len(neurons) <= min_neurons:\n        return None\n    stab = np.ones(n, bool)\n    for u in neurons:\n        stab &= s.stable(u, n)\n    base = s.base_mask() & stab & (t.correct | t.error).to_numpy()\n    R, L = (t.instructed == \"R\").to_numpy(), (t.instructed == \"L\").to_numpy()\n    ctrl = base & (t.ptype == 0).to_numpy()\n    cR, cL = rng.permutation(np.flatnonzero(ctrl & R)), rng.permutation(np.flatnonzero(ctrl & L))\n    trR, teR = cR[: len(cR) // 2], cR[len(cR) // 2:]\n    trL, teL = cL[: len(cL) // 2], cL[len(cL) // 2:]\n    trRc = trR[t.correct.to_numpy()[trR]]\n    trLc = trL[t.correct.to_numpy()[trL]]\n    stim_codes = [stim_code] if stim_code is not None else []\n    sets = {\"train_R\": trRc, \"train_L\": trLc, \"test_R\": teR, \"test_L\": teL,\n            \"train_all\": np.concatenate([trR, trL])}\n    for c in stim_codes:\n        sets[f\"stim_R\"] = np.flatnonzero(base & (t.ptype == c).to_numpy() & R)\n        sets[f\"stim_L\"] = np.flatnonzero(base & (t.ptype == c).to_numpy() & L)\n    if min(len(v) for v in sets.values()) <= min_trials:\n        return None\n    used = np.unique(np.concatenate(list(sets.values())))\n    cue = t.cue.to_numpy()\n    X = np.zeros((len(neurons), n, len(CD_STARTS)))\n    for j, u in enumerate(neurons):\n        sel = np.isin(u[\"ti\"], used)\n        ti = u[\"ti\"][sel]\n        rel = u[\"rel\"][sel] - cue[ti]\n        for i in used:\n            r = np.sort(rel[ti == i])\n            X[j, i] = (np.searchsorted(r, CD_STARTS + CD_WIN) - np.searchsorted(r, CD_STARTS, side=\"right\")) / CD_WIN\n    centres = CD_STARTS + CD_WIN / 2\n    po = np.median(t.pole_out.to_numpy()[used] - cue[used])\n    pi = np.median(t.pole_in.to_numpy()[used] - cue[used])\n    delay_w = (centres >= po) & (centres <= 0)   # windows centred in the delay epoch\n    cd_t = X[:, sets[\"train_R\"]].mean(1) - X[:, sets[\"train_L\"]].mean(1)\n    cd = cd_t[:, delay_w].mean(1)\n    cd = cd / np.linalg.norm(cd)\n    proj = np.einsum(\"j,jit->it\", cd, X)          # trials x windows\n    offset = proj[sets[\"train_all\"]].mean()\n    return dict(session=s.key, mouse=s.mouse, group=s.group, n_neurons=len(neurons), cd=cd, X=X,\n                proj=proj - offset, sets=sets, centres=centres, pole_out=po, pole_in=pi,\n                licked=t.licked.to_numpy(), cd_t=cd_t, stab=stab)\n"
}
```

```
File created successfully at: entries/gao-2018/gao2018.py (file state is current in your context — no need to Read it back)
```

**Agent**

Building a dev adapter from the cached pickle so I can develop without re-streaming 12 GB.

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; cat > adapt.py <<'EOF'
import pickle,numpy as np,pandas as pd,sys
sys.path.insert(0,'entries/gao-2018')
import gao2018 as G
out,meta=pickle.load(open('crcns.pkl','rb'))
new={}
for k,S in out.items():
    props=dict(zip(S['keys'],S['props'])); tts=list(S['tts']); ttm=S['ttm']
    cue=np.asarray(props['CueTime'],float); ids=S['trialIds']; n=len(ids)
    outcome=np.full(n,'',object)
    for o in G.OUTCOMES: outcome[ttm[tts.index(o)]==1]=o
    t=pd.DataFrame(dict(trial_id=ids,start=S['start'],pole_in=props['PoleInTime'],pole_out=props['PoleOutTime'],cue=cue[:,0] if cue.ndim==2 else cue,cue_col2=cue[:,1] if cue.ndim==2 else np.nan,good=props['GoodTrials']==1,ptype=np.asarray(props['PhotostimulationType'],float),outcome=outcome,lick_early=ttm[tts.index('LickEarly')]==1,stim_flag=ttm[tts.index('StimTrials')]==1))
    rows=S['laser']; lz=np.full((n,5),np.nan)
    if S['form']=='2d': lz[:len(rows)]=rows
    else:
        pos=np.searchsorted(ids,S['laser_trial']); ok=(pos<n); lz[pos[ok]]=rows[ok]
    for j,c in enumerate(['laser_t0','laser_on','laser_off','laser_mean','laser_peak']): t[c]=lz[:,j]
    for c in ['laser_on','laser_off','laser_t0']: t[c]-=t.start
    U=[dict(key=u['key'],t=u['t'],trial=u['tr'].astype(int),cell_type=(u['ct'] if isinstance(u['ct'],str) else ''),waveform=u['wf'],channel=u['ch']) for u in S['units']]
    new[k]=dict(trials=t,units=U,laser_form=2 if S['form']=='2d' else 1)
pickle.dump((new,meta),open('crcns_new.pkl','wb'))
EOF
python adapt.py && ls -la crcns_new.pkl
```

```
-rw-r--r-- 1 runner runner 369170359 Nov 14 11:12 crcns_new.pkl
Shell cwd was reset to
```

**Agent**

Now the first analyses: unit counts and the Fig. 2 selectivity fractions.

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; cat > dev1.py <<'EOF'
import pickle,numpy as np,pandas as pd,sys,time
sys.path.insert(0,'entries/gao-2018')
import gao2018 as G
crc,meta=pickle.load(open('crcns_new.pkl','rb'))
S=G.build_sessions(crc,meta)
pickle.dump(S,open('sessions.pkl','wb'))
df=pd.DataFrame([dict(key=s.key,mouse=s.mouse,group=s.group,cn=s.cn,cn_side=s.cn_side,alm=s.alm_side,units=len(s.units),pyr=len(s.pyramidal()),fs=sum(u['cell_type']=='FS' for u in s.units)) for s in S])
print(df.groupby('group')[['units','pyr','fs']].sum(), df.groupby(['group','mouse']).size())
t0=time.time()
rows=[]
for s in S:
    if s.group=='inhibition': continue
    for u in s.pyramidal():
        for tr in ['correct','all']:
            for rw in [1.3,1.5]:
                r=G.selectivity_tests(s,u,tr,rw); r.update(key=s.key,mouse=s.mouse,unit=u['key'],trials=tr,resp=rw); rows.append(r)
print(time.time()-t0)
sel=pd.DataFrame(rows)
for (tr,rw),g in sel.groupby(['trials','resp']):
    p=g[['sample','delay','response']].fillna(1)<0.05
    anys=p.any(axis=1); prep=p[['sample','delay']].any(axis=1); resp=p.response
    print(tr,rw,'N',len(g),'sel',anys.sum(),round(anys.mean(),3),'prep/all',round(prep.mean(),3),'prep/sel',round(prep.sum()/anys.sum(),3),'resp/all',round(resp.mean(),3),'resp/sel',round(resp.sum()/anys.sum(),3), 'untestable',g[['sample']].isna().sum().item())
EOF
python dev1.py
```

```
units  pyr  fs
group                     
dentate       578  530  33
fastigial     608  554  40
inhibition    737  682  29 group       mouse     
dentate     ANM314756     2
            BAYLORNL12    5
            BAYLORNL14    6
fastigial   ANM314746     3
            ANM314757     2
            ANM314758     4
            ANM314760     3
            BAYLORCD6     4
            BAYLORNL15    5
inhibition  BAYLORCD12    5
            BAYLORCD13    5
            BAYLORCD14    5
            BAYLORCD8     5
dtype: int64
13.652242660522461
[... 5 more lines not kept]
```

**Agent**

Fig. 2 fractions in ALM match under the main reading (0.79 selective; 0.56 preparatory; 0.64 response). Next, behavior with the hierarchical bootstrap.

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; cat > dev2.py <<'EOF'
import pickle,numpy as np,pandas as pd,sys,time
sys.path.insert(0,'entries/gao-2018')
import gao2018 as G
S=pickle.load(open('sessions.pkl','rb'))
t0=time.time()
fa=[s for s in S if s.group=='fastigial']; de=[s for s in S if s.group=='dentate']; inh=[s for s in S if s.group=='inhibition']
tf=G.perf_table(fa,[0,1,2]); td=G.perf_table(de,[0,3,4]); ti=G.perf_table(inh,[0,5,6]); tim=G.perf_table(inh,[0,5,6],contra_from='metadata')
rng=np.random.default_rng(1)
for name,tab,c in [('FN sample',tf,1),('FN delay',tf,2),('DN delay',td,4),('DN sample',td,3),('inh 0.5',ti,5),('inh 1.3',ti,6)]:
    for side in [None,'contra','ipsi']:
        r=G.hier_boot(tab,c,side,rng=rng); print(name,side,{k:(round(v,4) if isinstance(v,float) else v) for k,v in r.items()})
print(time.time()-t0)
# per mouse
for name,tab,c in [('FN delay',tf,2),('inh 0.5',ti,5),('inh 1.3',ti,6),('inh 0.5 meta',tim,5),('inh 1.3 meta',tim,6)]:
    for m,g in tab.groupby('mouse'):
        rc=G.hier_boot(g,c,'contra',rng=rng,n_boot=2000); ri=G.hier_boot(g,c,'ipsi',rng=rng,n_boot=2000)
        print(name,m,'contra',round(rc['change'],3),rc['p_drop'],'ipsi',round(ri['change'],3),ri['p_drop'])
EOF
python dev2.py
```

```
FN sample None {'ctrl': np.float64(0.8696), 'stim': np.float64(0.8606), 'change': np.float64(-0.009), 'p': np.float64(0.4186), 'p_drop': np.float64(0.4186), 'n_ctrl': 3897, 'n_stim': 538, 'n_mice': 6, 'n_sessions': 21}
FN sample contra {'ctrl': np.float64(0.8565), 'stim': np.float64(0.8256), 'change': np.float64(-0.0309), 'p': np.float64(0.3653), 'p_drop': np.float64(0.3653), 'n_ctrl': 2070, 'n_stim': 281, 'n_mice': 6, 'n_sessions': 20}
FN sample ipsi {'ctrl': np.float64(0.8866), 'stim': np.float64(0.8988), 'change': np.float64(0.0122), 'p': np.float64(0.3699), 'p_drop': np.float64(0.6301), 'n_ctrl': 1808, 'n_stim': 257, 'n_mice': 6, 'n_sessions': 21}
FN delay None {'ctrl': np.float64(0.8696), 'stim': np.float64(0.6295), 'change': np.float64(-0.2402), 'p': np.float64(0.0), 'p_drop': np.float64(0.0), 'n_ctrl': 3897, 'n_stim': 475, 'n_mice': 6, 'n_sessions': 21}
FN delay contra {'ctrl': np.float64(0.855), 'stim': np.float64(0.5361), 'change': np.float64(-0.3188), 'p': np.float64(0.0191), 'p_drop': np.float64(0.0191), 'n_ctrl': 2089, 'n_stim': 263, 'n_mice': 6, 'n_sessions': 21}
FN delay ipsi {'ctrl': np.float64(0.8866), 'stim': np.float64(0.7453), 'change': np.float64(-0.1413), 'p': np.float64(0.0157), 'p_drop': np.float64(0.0157), 'n_ctrl': 1808, 'n_stim': 212, 'n_mice': 6, 'n_sessions': 21}
DN delay None {'ctrl': np.float64(0.8733), 'stim': np.float64(0.8349), 'change': np.float64(-0.0385), 'p': np.float64(0.1059), 'p_drop': np.float64(0.1059), 'n_ctrl': 3410, 'n_stim': 545, 'n_mice': 3, 'n_sessions': 13}
DN delay contra {'ctrl': np.float64(0.8647), 'stim': np.float64(0.8097), 'change': np.float64(-0.0551), 'p': np.float64(0.0912), 'p_drop': np.float64(0.0912), 'n_ctrl': 1730, 'n_stim': 289, 'n_mice': 3, 'n_sessions': 13}
DN delay ipsi {'ctrl': np.float64(0.8821), 'stim': np.float64(0.8633), 'change': np.float64(-0.0189), 'p': np.float64(0.4233), 'p_drop': np.float64(0.4233), 'n_ctrl': 1680, 'n_stim': 256, 'n_mice': 3, 'n_sessions': 13}
DN sample None {'ctrl': np.fl
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; cat > dev3.py <<'EOF'
import pickle,numpy as np,pandas as pd,sys,time
sys.path.insert(0,'entries/gao-2018')
import gao2018 as G
from scipy import stats
S=pickle.load(open('sessions.pkl','rb'))
t0=time.time()
res={}
for grp,code,dur in [('fastigial',2,0.455),('dentate',4,0.455),('inhibition',6,1.3)]:
    for which in ['all','correct']:
        rows=[];F=[]
        for s in S:
            if s.group!=grp: continue
            for u in s.pyramidal():
                rd=G.modulation(s,u,code,0,'cue',which)
                if rd is None: continue
                rp=G.modulation(s,u,code,0,dur,which)
                fc=G.fine_change(s,u,code,which)
                rows.append(dict(key=s.key,mouse=s.mouse,unit=u['key'],p_delay=rd['p'],ch_delay=rd['change'],r0=rd['rate_ctrl'],r1=rd['rate_stim'],p_stim=rp['p'],ch_stim=rp['change']))
                F.append(fc[1]); starts=fc[0]
        d=pd.DataFrame(rows); F=np.array(F)
        for win in ['delay','stim']:
            sig=d[f'p_{win}']<0.01
            sg=np.sign(d[f'ch_{win}'])
            for lab,sh in [('start',0),('centre',0.005),('end',0.01)]:
                L=G.latency(F[sig.values],sg[sig].values,np.random.default_rng(2),n_boot=1000,starts=starts,label_shift=sh)
                print(grp,which,win,'N',len(d),'sig',sig.sum(),round(sig.mean(),3),'inc',(sg[sig]>0).sum(),'dec',(sg[sig]<0).sum(),lab,{k:round(v,2) for k,v in L.items()})
        if grp=='inhibition':
            print('mean rate ctrl',d.r0.mean(),'stim',d.r1.mean(),'paired',stats.ttest_rel(d.r0,d.r1).pvalue,'unpaired',stats.ttest_ind(d.r0,d.r1).pvalue)
            ss=d[d.p_delay<0.01]; print('mod: ',ss.r0.mean(),ss.r1.mean(),stats.ttest_rel(ss.r0,ss.r1).pvalue,stats.ttest_ind(ss.r0,ss.r1).pvalue)
print(time.time()-t0)
EOF
python dev3.py
```

```
fastigial all delay N 445 sig 187 0.42 inc 111 dec 76 start {'onset_all': np.float64(9.0), 'boot_mean': np.float64(7.82), 'boot_sd': np.float64(4.04), 'no_onset': np.float64(0.0), 'n': 187}
fastigial all delay N 445 sig 187 0.42 inc 111 dec 76 centre {'onset_all': np.float64(14.0), 'boot_mean': np.float64(12.82), 'boot_sd': np.float64(4.04), 'no_onset': np.float64(0.0), 'n': 187}
fastigial all delay N 445 sig 187 0.42 inc 111 dec 76 end {'onset_all': np.float64(19.0), 'boot_mean': np.float64(17.82), 'boot_sd': np.float64(4.04), 'no_onset': np.float64(0.0), 'n': 187}
fastigial all stim N 445 sig 177 0.398 inc 104 dec 73 start {'onset_all': np.float64(3.0), 'boot_mean': np.float64(3.6), 'boot_sd': np.float64(2.83), 'no_onset': np.float64(0.0), 'n': 177}
fastigial all stim N 445 sig 177 0.398 inc 104 dec 73 centre {'onset_all': np.float64(8.0), 'boot_mean': np.float64(8.6), 'boot_sd': np.float64(2.83), 'no_onset': np.float64(0.0), 'n': 177}
fastigial all stim N 445 sig 177 0.398 inc 104 dec 73 end {'onset_all': np.float64(13.0), 'boot_mean': np.float64(13.6), 'boot_sd': np.float64(2.83), 'no_onset': np.float64(0.0), 'n': 177}
fastigial correct delay N 199 sig 68 0.342 inc 48 dec 20 start {'onset_all': np.float64(0.0), 'boot_mean': np.float64(6.08), 'boot_sd': np.float64(7.52), 'no_onset': np.float64(0.0), 'n': 68}
fastigial correct delay N 199 sig 68 0.342 inc 48 dec 20 centre {'onset_all': np.float64(5.0), 'boot_mean': np.float64(11.08), 'boot_sd': np.float64(7.52), 'no_onset': np.float64(0.0), 'n': 68}
fastigial correct delay N 199 sig 68 0.342 inc 48 dec 20 end {'onset_all': np.float64(10.0), 'boot_mean': np.float64(16.08), 'boot_sd': np.float64(7.52), 'no_onset': np.float64(0.0), 'n': 68}
fastigial correct stim N 199 sig 67 0.337 inc 41 dec 26 start {'onset_all': np.float64(14.0), 'boot_mean': np.float64(8.01), 'boot_sd': np.float64(6.37), 'no_onset': np.float64(0.0), 'n': 67}
fastigial correct stim N 199 sig 67 0.337 inc 41 dec 26 centre {'onset_all': np.float64(1
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR; . venv/bin/activate; cat > dev4.py <<'EOF'
import pickle,numpy as np,pandas as pd,sys,time
sys.path.insert(0,'entries/gao-2018')
import gao2018 as G
from scipy import stats
S=pickle.load(open('sessions.pkl','rb'))
t0=time.time()
# fig4f: 400 ms bins in 50 ms steps relative to cue
tb=np.round(np.arange(-3,2.0001,0.05),3)
for grp,code in [('fastigial',2),('dentate',4)]:
    P=[]
    for s in S:
        if s.group!=grp: continue
        for u in s.pyramidal():
            ctrl,stim,en=G.stim_trials(s,u,code,'all')
            if not en: continue
            cue=s.trials.cue.to_numpy()
            ps=[]
            for b in tb:
                c=s.counts(u,cue+b-0.2,cue+b+0.2)
                ps.append(stats.ttest_ind(c[ctrl],c[stim]).pvalue if np.var(c[ctrl])+np.var(c[stim])>0 else 1.0)
            P.append(ps)
    P=np.array(P); frac=(P<0.01).mean(0)
    pre=(tb+0.2<=-1.3)&(tb-0.2>=-3.0); post=(tb-0.2>=-0.845+1.0)&(tb-0.2<1.3)
    print(grp,len(P),'pre',frac[pre].mean().round(4),'post',frac[post].mean().round(4),'during',frac[(tb>-1.3)&(tb<-0.845)].max().round(3))
    print(' '.join(f'{b:.2f}:{f:.3f}' for b,f in zip(tb[::4],frac[::4])))
print(time.time()-t0)
EOF
python dev4.py
```

```
Sat Nov 14 11:14:43 UTC 2026
fastigial 445 pre 0.0092 post 0.1345 during 0.418
-3.00:0.013 -2.80:0.016 -2.60:0.009 -2.40:0.009 -2.20:0.016 -2.00:0.009 -1.80:0.002 -1.60:0.007 -1.40:0.092 -1.20:0.297 -1.00:0.416 -0.80:0.380 -0.60:0.333 -0.40:0.333 -0.20:0.321 -0.00:0.303 0.20:0.218 0.40:0.175 0.60:0.142 0.80:0.130 1.00:0.139 1.20:0.126 1.40:0.121 1.60:0.128 1.80:0.128 2.00:0.142
dentate 517 pre 0.0147 post 0.0476 during 0.329
-3.00:0.014 -2.80:0.008 -2.60:0.004 -2.40:0.012 -2.20:0.021 -2.00:0.015 -1.80:0.014 -1.60:0.027 -1.40:0.081 -1.20:0.265 -1.00:0.325 -0.80:0.286 -0.60:0.240 -0.40:0.172 -0.20:0.128 -0.00:0.103 0.20:0.064 0.40:0.050 0.60:0.039 0.80:0.052 1.00:0.062 1.20:0.043 1.40:0.050 1.60:0.050 1.80:0.041 2.00:0.037
77.3223705291748
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; cat > dev5.py <<'EOF'
import pickle,numpy as np,pandas as pd,sys,time
sys.path.insert(0,'entries/gao-2018')
import gao2018 as G
from scipy import stats
S=pickle.load(open('sessions.pkl','rb'))
t0=time.time()
rng=np.random.default_rng(3)
for grp,code,dur in [('inhibition',6,1.3),('fastigial',2,0.455),('dentate',4,0.455)]:
  for nscr in [10,5]:
    C=[];Z=[];info=[]
    for s in S:
        if s.group!=grp: continue
        t=s.trials; n=len(t)
        for u in s.pyramidal():
            sel=G.selectivity_tests(s,u,'correct')
            if not any((sel.get(e,1) or 1)<0.05 for e in ['sample','delay','response'] if not np.isnan(sel.get(e,np.nan))): continue
            base=s.base_mask()&s.stable(u,n)&(t.correct|t.error).to_numpy()
            ctrl=base&(t.ptype==0).to_numpy(); stim=base&(t.ptype==code).to_numpy()
            R=(t.instructed=='R').to_numpy(); L=~R
            if min((ctrl&R).sum(),(ctrl&L).sum())-nscr<=3 or min((stim&R).sum(),(stim&L).sum())<=3: continue
            r=G.pref_selectivity(s,u,ctrl,{'stim':stim},nscr,rng)
            if r is None: continue
            C.append(r[0]); Z.append(r[1]['stim']); info.append((s.key,u['key']))
    C=np.array(C);Z=np.array(Z)
    g=G.GRID; delay=(g>-1.3)&(g<0); late=(g>-0.5)&(g<0); post=(g>-1.3+dur)&(g<0)
    for wn,w in [('delay',delay),('last500',late),('post',post)]:
        c=np.nanmean(C[:,w],1); z=np.nanmean(Z[:,w],1)
        mc,lc,hc=G.boot_mean_ci(c,rng,2000); mz,lz,hz=G.boot_mean_ci(z,rng,2000); md,ld,hd=G.boot_mean_ci(c-z,rng,2000)
        print(grp,nscr,'N',len(C),wn,'ctrl',round(mc,2),(round(lc,2),round(hc,2)),'stim',round(mz,2),(round(lz,2),round(hz,2)),'diff',round(md,2),(round(ld,2),round(hd,2)))
print(time.time()-t0)
EOF
python dev5.py
```

```
/tmp/claude-1001/dev5.py:27: RuntimeWarning: Mean of empty slice
  c=np.nanmean(C[:,w],1); z=np.nanmean(Z[:,w],1)
entries/gao-2018/gao2018.py:440: RuntimeWarning: Mean of empty slice
  means[b] = np.nanmean(x[rng.integers(0, n, n)], axis=0)
entries/gao-2018/gao2018.py:441: RuntimeWarning: Mean of empty slice
  return np.nanmean(x, axis=0), np.percentile(means, 2.5, axis=0), np.percentile(means, 97.5, axis=0)
/tmp/claude-1001/dev5.py:27: RuntimeWarning: Mean of empty slice
  c=np.nanmean(C[:,w],1); z=np.nanmean(Z[:,w],1)
entries/gao-2018/gao2018.py:440: RuntimeWarning: Mean of empty slice
  means[b] = np.nanmean(x[rng.integers(0, n, n)], axis=0)
entries/gao-2018/gao2018.py:441: RuntimeWarning: Mean of empty slice
  return np.nanmean(x, axis=0), np.percentile(means, 2.5, axis=0), np.percentile(means, 97.5, axis=0)
inhibition 10 N 336 delay ctrl 1.39 (np.float64(1.06), np.float64(1.72)) stim 0.41 (np.float64(0.21), np.float64(0.61)) diff 0.98 (np.float64(0.68), np.float64(1.31))
inhibition 10 N 336 last500 ctrl 1.4 (np.float64(1.01), np.float64(1.84)) stim 0.35 (np.float64(0.11), np.float64(0.59)) diff 1.05 (np.float64(0.65), np.float64(1.48))
inhibition 10 N 336 post ctrl nan (np.float64(nan), np.float64(nan)) stim nan (np.float64(nan), np.float64(nan)) diff nan (np.float64(nan), np.float64(nan))
inhibition 5 N 336 delay ctrl 1.35 (np.float64(1.04), np.float64(1.68)) stim 0.38 (np.float64(0.17), np.float64(0.59)) diff 0.97 (np.float64(0.66), np.float64(1.31))
inhibition 5 N 336 last500 ctrl 1.42 (np.float64(1.02), np.float64(1.82)) stim 0.36 (np.float64(0.11), np.float64(0.62)) diff 1.06 (np.float64(0.68), np.float64(1.48))
inhibition 5 N 336 post ctrl nan (np.float64(nan), np.float64(nan)) stim nan (np.float64(nan), np.float64(nan)) diff nan (np.float64(nan), np.float64(nan))
fastigial 10 N 328 delay ctrl 1.94 (np.float64(1.46), np.float64(2.49)) stim 0.67 (np.float64(0.37), np.float64(1.0)) diff 1.28 (np.float64(0.81), np.float64(1.78))
fastigial 10 N 328 last500 ct
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; cat > dev6.py <<'EOF'
import pickle,numpy as np,pandas as pd,sys,time
sys.path.insert(0,'entries/gao-2018')
import gao2018 as G
from scipy import stats
import statsmodels.api as sm
S=pickle.load(open('sessions.pkl','rb'))
t0=time.time(); rng=np.random.default_rng(4)
CDs=[]
for s in S:
    if s.group=='inhibition': continue
    r=G.cd_session(s,rng,stim_code=2 if s.group=='fastigial' else 4)
    print(s.key, None if r is None else r['n_neurons'], None if r is None else {k:len(v) for k,v in r['sets'].items()})
    if r: CDs.append(r)
print(len(CDs), time.time()-t0)
pickle.dump(CDs,open('cds.pkl','wb'))
EOF
python dev6.py
```

```
ANM314746_20151020 16 {'train_R': 43, 'train_L': 31, 'test_R': 46, 'test_L': 37, 'train_all': 82, 'stim_R': 7, 'stim_L': 11}
ANM314746_20151021 10 {'train_R': 46, 'train_L': 29, 'test_R': 48, 'test_L': 31, 'train_all': 77, 'stim_R': 15, 'stim_L': 11}
ANM314746_20151022 None None
ANM314756_20151020 9 {'train_R': 31, 'train_L': 22, 'test_R': 40, 'test_L': 29, 'train_all': 68, 'stim_R': 13, 'stim_L': 10}
ANM314756_20151023 None None
ANM314757_20151020 8 {'train_R': 28, 'train_L': 31, 'test_R': 34, 'test_L': 34, 'train_all': 66, 'stim_R': 7, 'stim_L': 9}
ANM314757_20151021 None None
ANM314758_20151020 17 {'train_R': 37, 'train_L': 32, 'test_R': 43, 'test_L': 34, 'train_all': 77, 'stim_R': 8, 'stim_L': 12}
ANM314758_20151021 None None
ANM314758_20151022 None None
ANM314758_20151023 None None
ANM314760_20151020 None None
ANM314760_20151021 12 {'train_R': 33, 'train_L': 44, 'test_R': 41, 'test_L': 48, 'train_all': 89, 'stim_R': 13, 'stim_L': 11}
ANM314760_20151022 None None
BAYLORCD6_20170610 30 {'train_R': 28, 'train_L': 40, 'test_R': 40, 'test_L': 57, 'train_all': 95, 'stim_R': 11, 'stim_L': 16}
BAYLORCD6_20170611 None None
BAYLORCD6_20170612 None None
BAYLORCD6_20170614 None None
BAYLORNL12_20170610 36 {'train_R': 40, 'train_L': 48, 'test_R': 55, 'test_L': 62, 'train_all': 117, 'stim_R': 12, 'stim_L': 20}
BAYLORNL12_20170611 12 {'train_R': 55, 'train_L': 52, 'test_R': 68, 'test_L': 62, 'train_all': 128, 'stim_R': 24, 'stim_L': 13}
[... 16 more lines not kept]
```

**Agent**

20 of 34 sessions pass the deposited script's stability rule (paper: 28 of 39). Computing the coding-direction claims.

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; cat > dev7.py <<'EOF'
import pickle,numpy as np,pandas as pd,sys,time
sys.path.insert(0,'entries/gao-2018')
import gao2018 as G
import statsmodels.api as sm
CDs=pickle.load(open('cds.pkl','rb')); rng=np.random.default_rng(5)
c=CDs[0]['centres']
def sep(r,a,b): return r['proj'][r['sets'][a]].mean(0)-r['proj'][r['sets'][b]].mean(0)
ctrl=np.array([sep(r,'test_R','test_L') for r in CDs])
m,lo,hi=G.boot_mean_ci(ctrl,rng,10000)
samp=(c>-2.6)&(c<-1.3); dl=(c>=-1.3)&(c<=0)
print('control: sample any excl0', np.any(lo[samp]>0), 'delay all', np.all(lo[dl]>0), 'min lo delay', lo[dl].min())
for grp in ['fastigial','dentate']:
    R=[r for r in CDs if r['group']==grp]
    cs=np.array([sep(r,'test_R','test_L') for r in R]); st=np.array([sep(r,'stim_R','stim_L') for r in R])
    for wn,w in [('last400',np.isclose(c,-0.2)),('post',(c>=-1.3+0.455)&(c<=0))]:
        a=cs[:,w].mean(1); b=st[:,w].mean(1)
        ma,la,ha=G.boot_mean_ci(a,rng); mb,lb,hb=G.boot_mean_ci(b,rng); md,ld,hd=G.boot_mean_ci(a-b,rng)
        print(grp,len(R),wn,'ctrl',round(ma,2),round(la,2),round(ha,2),'stim',round(mb,2),round(lb,2),round(hb,2),'diff',round(md,2),round(ld,2),round(hd,2))
# captured
res=[]
for r in CDs:
    X=r['X']; sets=r['sets']; cd=r['cd']
    tr=np.concatenate([sets['train_R'],sets['train_L'],sets['test_R'],sets['test_L']])
    w=(c>r['pole_in'])&(c<=0)
    t=X; R=np.concatenate([sets['train_R']]); L=sets['train_L']
    # control correct trials all (both halves, correct only)
    D=X[:,R].mean(1)-X[:,L].mean(1)
    D=D[:,w]
    tot=np.sqrt((D**2).sum(0).mean()); al=np.sqrt(((cd@D)**2).mean())
    base=(c<r['pole_in']) & (c> r['pole_in']-0.5)
    xr=X[:,R].mean(1); xl=X[:,L].mean(1); b0=(xr[:,base].mean(1)+xl[:,base].mean(1))/2
    A=np.concatenate([xr[:,w],xl[:,w]],1)-b0[:,None]
    vt=np.sqrt((A**2).sum(0).mean()); va=np.sqrt(((cd@A)**2).mean())
    res.append((al/tot, (al/tot)**2, va/vt, (va/vt)**2))
res=np.array(res)*100; print('captured mean',res.mean(0).round(1),'sem',(res.std(0,ddof=1)/np.sqrt(len(res))).round(1),'sd',res.std(0,ddof=1).round(1))
# ed10d logistic
for grp in ['fastigial']:
    xs=[];ys=[];xc=[];yc=[]
    for r in CDs:
        if r['group']!=grp: continue
        k=np.isclose(c,-0.2)
        for sset,X_,Y_ in [(np.concatenate([r['sets']['stim_R'],r['sets']['stim_L']]),xs,ys),(np.concatenate([r['sets']['test_R'],r['sets']['test_L']]),xc,yc)]:
            lk=r['licked'][sset]; ok=lk!=''
            X_.extend(r['proj'][sset[ok]][:,k].ravel()); Y_.extend((lk[ok]=='R').astype(int))
    for nm,x,y in [('stim',xs,ys),('ctrl',xc,yc)]:
        x=np.array(x);y=np.array(y); fit=sm.Logit(y,sm.add_constant(x/np.std(x))).fit(disp=0)
        print(nm,len(x),fit.params[1],fit.pvalues[1],fit.conf_int()[1])
EOF
python dev7.py
```

```
control: sample any excl0 True delay all True min lo delay 6.2158586219472785
fastigial 8 last400 ctrl 18.22 10.48 26.34 stim 6.81 1.3 14.71 diff 11.41 4.05 20.15
fastigial 8 post ctrl 16.81 9.22 24.19 stim 5.82 1.23 13.04 diff 10.99 3.91 19.18
dentate 12 last400 ctrl 15.3 9.39 21.49 stim 13.01 7.35 18.98 diff 2.29 0.54 4.29
dentate 12 post ctrl 15.02 9.46 20.79 stim 11.9 6.67 17.62 diff 3.12 1.38 4.98
captured mean [85.4 73.9 57.9 38. ] sem [2.3 3.8 4.8 5.9] sd [10.5 16.8 21.6 26.6]
stim 181 0.5780478037550298 0.0021657736640305404 [0.20858714 0.94750847]
ctrl 729 1.6519507193422374 1.4676062523878205e-32 [1.37945822 1.92444322]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  grep -n "datasets\|missing_datasets\|verifications\|assumed\|measured\|questions" schemas/attempt.schema.json | head -40; python - <<'EOF'
import json
s=json.load(open('schemas/attempt.schema.json'))
print(json.dumps(s['properties'].get('datasets'),indent=0)[:1500])
print(list(s['properties'].keys()))
o=s.get('$defs',s.get('definitions',{}))
print(list(o.keys()))
for k in o:
    if 'outcome' in k.lower() or 'finding' in k.lower(): print(k, json.dumps(o[k])[:1500])
EOF
```

```
10:    "datasets",
24:    "datasets": {
88:    "missing_datasets": {
276:          "measured": {
299:          "assumed": {
300:            "description": "True when the outcome rests on an assumption about a method the paper leaves open: a choice the paper best supports, stated in a deviation that says what was assumed and why (docs/protocol.md, Author, step 1.6).",
359:                "assumed": {
364:                "assumed"
386:    "verifications": {
497:          "datasets": {
498:            "description": "For a finding about the data, in an attempt that used several datasets: the folders of the datasets it is about (000147, crcns-hc-18). Unset: the attempt's one dataset, or all of them.",
{
"description": "Every dataset the attempt used (docs/protocol.md, \"Record the attempt\").",
"type": "array",
"minItems": 1,
"items": {
"description": "A dataset the attempt used: the archive, the dataset's identifier there, the pinned version, and how the paper relates to it.",
"type": "object",
"additionalProperties": false,
"required": [
[... 49 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 230,380p schemas/attempt.schema.json; sed -n 440,520p schemas/attempt.schema.json
```

```
"items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "claim",
          "outcome"
        ],
        "properties": {
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
[... 212 more lines not kept]
```

**Agent**

Adding the DANDI comparison function to the helper, then writing the notebook generator.

**Agent calls Bash**

```bash
cd entries/gao-2018; cat >> gao2018.py <<'EOF'


# ----------------------------------------------------------------------------- the two deposits


def compare_deposits(sessions: list[Session], dandi: dict, crcns: dict) -> pd.DataFrame:
    """Match each CRCNS session to its DANDI file (subject and date), its trials by start time
    (nearest, within 0.06 s, as DANDI rounds start times) and its units by order, and compare
    them. Adds the column `in_dandi` to each session's trial table."""
    rows = []
    for s in sessions:
        d = dandi[s.key]
        t = s.trials
        dt = d["trials"]
        dist = np.abs(t.start.to_numpy()[:, None] - dt.start_time.to_numpy()[None, :])
        j, dm = dist.argmin(0), dist.min(0)
        ok = dm < 0.06
        in_d = np.zeros(len(t), bool)
        in_d[j[ok]] = True
        t["in_dandi"] = in_d
        eligible = (t.good & t.ptype.notna()).to_numpy()
        jj = j[ok]
        ptype_same = np.all(dt.photo_stim_id.to_numpy()[ok].astype(float) == t.ptype.to_numpy()[jj])
        resp_same = np.all(dt.response.to_numpy()[ok] == t.outcome.to_numpy()[jj])
        cue_diff = np.nanmax(np.abs(dt.cue_time.to_numpy()[ok] - (t.start + t.cue).to_numpy()[jj]))
        cu = crcns[s.key]["units"]
        same = sum(len(a) == len(b["t"]) and np.allclose(a, b["t"]) for a, b in zip(d["spikes"], cu))
        ct_same = sum(a == (b["cell_type"] or "unknown") for a, b in zip(d["cell_type"], cu))
        rows.append(dict(session=s.key, group=s.group, crcns_trials=len(t), good_with_code=int(eligible.sum()),
                         dandi_trials=len(dt), matched=int(ok.sum()), max_start_diff_s=round(float(dm.max()), 3),
                         eligible_not_in_dandi=int((eligible & ~in_d).sum()), dandi_not_eligible=int((in_d & ~eligible).sum()),
                         codes_same=bool(ptype_same), outcomes_same=bool(resp_same), max_cue_diff_s=round(float(cue_diff), 4),
                         units_crcns=len(cu), units_dandi=len(d["spikes"]), units_same_spikes=same, cell_type_same=ct_same))
    return pd.DataFrame(rows)
EOF
date -u
```

```
Sat Nov 14 11:17:45 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; python -c "
import pickle,numpy as np
out,meta=pickle.load(open('crcns.pkl','rb'))
for k in ['ANM314746_20151020','ANM314746_20151021','ANM314757_20151021','BAYLORCD6_20170610']:
    S=out[k]; print(k,S['form'],S['idStr'],S['halfmax'])
"
```

```
ANM314746_20151020 1d ['aom_input_trace' 'laser_power'] [np.float64(1.2694512551887545), np.float64(nan)]
ANM314746_20151021 1d ['aom_input_trace' 'laser_power'] [np.float64(1.2633230669707889), np.float64(nan)]
ANM314757_20151021 1d ['aom_input_trace' 'laser_power'] [np.float64(1.260742777215121), np.float64(10.15687606727253)]
BAYLORCD6_20170610 2d ['aom_input_trace' 'laser_power'] [np.float64(1.68548583984375), np.float64(14.871933880974264)]
Shell cwd was reset to
```

**Agent**

Now the notebook generator (long script).

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/make_nb.py",
 "content": "import nbformat as nbf\n\nnb = nbf.v4.new_notebook()\ncells = []\n\n\ndef md(s):\n    cells.append(nbf.v4.new_markdown_cell(s.strip(\"\\n\")))\n\n\ndef code(s, tags=None):\n    c = nbf.v4.new_code_cell(s.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\nmd(r\"\"\"\n# Reproducing Gao et al. (2018) from DANDI:000007 and CRCNS:alm-4\n\n**Paper.** Gao Z, Davis C, Thomas AM, Economo MN, Abrego AM, Svoboda K, De Zeeuw CI, Li N (2018).\nA cortico-cerebellar loop for motor planning. *Nature* 563, 113-116.\n[doi:10.1038/s41586-018-0633-x](https://doi.org/10.1038/s41586-018-0633-x). The claims file\n(`claims/gao-2018.yaml`) was written from the version of record (PMC6212318) with its Methods,\nExtended Data legends and Supplementary Information; the legends of the main Figures 1 to 4 were\nnot in the text read.\n\n**Datasets.**\n- [DANDI:000007](https://dandiarchive.org/dandiset/000007/0.220126.1903), version\n  `0.220126.1903` (doi:10.48324/dandi.000007/0.220126.1903). The paper cites no DANDI version\n  (the dandiset was created in 2020, after the paper). This is the only published version; the\n  draft has the same 54 assets and size, so the published one is pinned.\n- [CRCNS:alm-4](https://crcns.org/data-sets/motor-cortex/alm-4) (doi:10.6080/K0NS0S26),\n  unversioned (descriptor version 0.6, 23 October 2018). Files read, with their MD5 sums from\n  `checksums.md5`: `ALM_recording_DCN_photoactivation/datafiles.tar.gz`\n  (12e9d7af630523ed2511826eeacf6b48), `ALM_recording_DCN_photoinhibition/datafiles.tar.gz`\n  (5123dc96df58457f853e2deb5ce479c7), and, for method details, the two `analyses_scripts.zip`\n  (601f4b52198614dbd4761a64d2658698 and 4639a8478bc307fb3a5a4b8f2a53fb58).\n\nBoth datasets hold the same 54 ALM recording sessions of 13 mice (shown below). The analysis\nruns on the CRCNS copy, which holds every trial, the GoodTrials flag and the laser traces; the\nDANDI copy is checked against it unit by unit and trial by trial, and the counts of the Fig. 2\nclaim are also given on the DANDI trial set.\n\nNeither dataset holds the lesion experiments, the behavior-only sessions, the CN recordings,\nlick times, video, the VGAT-ChR2-EYFP experiments or the anatomy; the claims on those are\nblocked as `data_missing` (table below).\n\n| claim | tested |\n|---|---|\n| fig1d-fastigial-lesion-contra-choice | blocked, data_missing |\n| fig1e-fastigial-lesion-slow-initiation | blocked, data_missing |\n| fig1d-dentate-lesion-no-effect | blocked, data_missing |\n| fig1g-fastigial-activation-early-sample-no-effect | tested (recording sessions) |\n| fig1g-fastigial-activation-delay-errors | tested (recording sessions) |\n| fig1h-fastigial-activation-delay-bias | tested, reading (a) only |\n| fig1h-fastigial-activation-response-contra-bias | blocked, data_missing |\n| fig1i-fastigial-activation-licking-unaffected | blocked, data_missing |\n| fig1g-dentate-activation-little-effect | tested, reading (a), 3 of 8 mice |\n| fig1j-photoinhibition-silences-fastigial | blocked, data_missing |\n| fig1k-inhibition-early-sample-no-effect | blocked, data_missing |\n| fig1k-inhibition-late-sample-delay-errors | blocked, data_missing |\n| fig1k-inhibition-delay-bias | tested (recording mice) |\n| fig1k-inhibition-response-ipsi-bias | blocked, data_missing |\n| fig1l-inhibition-execution-unaffected | blocked, data_missing |\n| ed10-vgat-fastigial-perturbation-performance | blocked, data_missing |\n| fig2-alm-selective-fraction | tested |\n| fig2-cn-selective-fraction | blocked, data_missing |\n| fig2-preparatory-more-in-alm | tested, ALM only |\n| fig2-peri-movement-equal | tested, ALM only |\n| ed4-lick-modulated-few | blocked, data_missing |\n| fig2cd-selectivity-emerges-gradually | tested, ALM only |\n| ed4e-cn-predicts-movement | blocked, data_missing |\n| ed4f-preparatory-all-nuclei | blocked, data_missing |\n| ed4g-fastigial-contra-late-delay | blocked, data_missing |\n| fig3-cn-altered-by-alm-inhibition | blocked, data_missing |\n| fig3b-cn-net-disinhibition | blocked, data_missing |\n| fig3c-cn-selectivity-abolished | blocked, data_missing |\n| ed6-cn-selectivity-both-alm-hemispheres | blocked, data_missing |\n| fig3d-alm-altered-by-cn-inhibition | tested |\n| fig3e-alm-mean-rate-unchanged | tested |\n| fig3e-alm-increase-decrease | tested |\n| fig3f-alm-selectivity-abolished-by-cn-inhibition | tested |\n| fig4bc-fastigial-targets-alm-thalamus | blocked, data_missing |\n| ed8-snr-sc-converge | blocked, data_missing |\n| fig4-fastigial-activation-alm-latency | tested |\n| fig4e-fastigial-activation-abolishes-alm-selectivity | tested |\n| fig4f-fastigial-effect-persists | tested |\n| fig4g-dentate-effect-recovers | tested |\n| fig4i-cd-control-separation | tested |\n| fig4i-fastigial-collapses-cd | tested |\n| cd-captures-selectivity | tested |\n| ed10b-fastigial-activation-errors-during-recording | tested |\n| ed10c-alm-inhibition-endpoints-predict | blocked, data_missing |\n| ed10d-fastigial-endpoints-no-prediction | tested |\n| ed10ef-alm-drives-licking-after-fastigial | blocked, data_missing |\n\nMethod details the claims file leaves open are taken from the paper's Methods and, where those\nare silent, from the analysis scripts deposited in CRCNS:alm-4 (the paper's reporting summary\nsays its analysis scripts would be deposited on CRCNS.org). Each is cited in `gao2018.py` or in\nthe claim's section.\n\"\"\")\n\ncode(r\"\"\"\nimport time\nimport resource\nimport warnings\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nimport statsmodels.api as sm\nfrom scipy import stats\n\nimport gao2018 as G\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\npd.set_option(\"display.width\", 220)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 300)\n\nstarted = time.time()\ndandi = G.load_dandi()\nprint(f\"DANDI:{G.DANDISET_ID} version {G.DANDISET_VERSION}: {len(dandi)} NWB files streamed \"\n      f\"in {time.time() - started:.0f} s\")\ncrcns, meta = {}, {}\nfor which in G.CRCNS_FILES:\n    s_, m_ = G.stream_crcns(which)\n    crcns.update(s_)\n    meta.update(m_)\nprint(f\"CRCNS:{G.CRCNS_ID} (doi:{G.CRCNS_DOI}, unversioned): {len(crcns)} sessions, \"\n      f\"{time.time() - started:.0f} s so far, peak memory \"\n      f\"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.1f} GB\")\nsessions = G.build_sessions(crcns, meta)\n\"\"\")\n\nmd(\"## Data check\")\n\ncode(r\"\"\"\ninfo = pd.DataFrame([dict(session=s.key, mouse=s.mouse, group=s.group, cn=s.cn, cn_side=s.cn_side,\n                          alm_ml=s.alm_ml, trials=len(s.trials),\n                          good=int(s.trials.good.sum()),\n                          units=len(s.units), pyramidal=len(s.pyramidal()),\n                          FS=sum(u['cell_type'] == 'FS' for u in s.units),\n                          unclassified=sum(u['cell_type'] not in ('pyramidal', 'FS') for u in s.units))\n                     for s in sessions])\nprint(\"Sessions and units by group and mouse:\")\nprint(info.groupby([\"group\", \"mouse\"]).agg(sessions=(\"session\", \"size\"), units=(\"units\", \"sum\"),\n                                         pyramidal=(\"pyramidal\", \"sum\"), FS=(\"FS\", \"sum\"),\n                                         unclassified=(\"unclassified\", \"sum\"),\n                                         cn=(\"cn\", \"first\"), cn_side=(\"cn_side\", \"first\"),\n                                         alm_ml=(\"alm_ml\", \"first\")).to_string())\nprint(\"\\nTotals by group:\")\nprint(info.groupby(\"group\")[[\"units\", \"pyramidal\", \"FS\", \"unclassified\"]].sum().to_string())\nprint(\"\\nPhotostimulation codes on good trials, by group:\")\nct = pd.concat([s.trials.assign(group=s.group) for s in sessions])\nprint(pd.crosstab(ct[ct.good].group, ct[ct.good].ptype.fillna(-1).astype(int)).to_string())\nprint(\"\\nTrial outcomes on good trials:\", ct[ct.good].outcome.value_counts().to_dict())\nprint(\"Photostimulation code descriptions in the files:\")\nfor line in sessions[0].trials.columns[:0]:\n    pass\nfor key in [\"ANM314746_20151020\", \"BAYLORCD8_20171018\"]:\n    print(\" \", key, crcns[key][\"trial_descr\"][4:])\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nThe CRCNS descriptor lists 34 sessions (9 mice) of ALM recording during fastigial or dentate\nphoto-activation and 20 sessions (4 mice) during CN photo-inhibition; the files hold exactly\nthese. The fastigial mice are 6 (ANM314746, ANM314757, ANM314758, ANM314760, BAYLORCD6,\nBAYLORNL15) and the dentate mice 3 (ANM314756, BAYLORNL12, BAYLORNL14), as Supplemental Table 1\ngives (6 and 3). The paper reports 1309 ALM units (1194 putative pyramidal) in 10 mice over 39\nsessions for Fig. 2, of which 912 pyramidal neurons in the 9 photo-activation mice, and 490\nunits (454 pyramidal) in 4 mice over 19 sessions for CN photo-inhibition. The counts above\ndiffer from both (printed): the files hold more units than the paper reports for the same\nmice.\n\"\"\")\n\ncode(r\"\"\"\ncmp_ = G.compare_deposits(sessions, dandi, crcns)\nprint(cmp_.to_string(index=False))\nprint(\"\\nAll units have identical spike times in both deposits:\",\n      bool((cmp_.units_same_spikes == cmp_.units_crcns).all() and (cmp_.units_dandi == cmp_.units_crcns).all()))\nprint(\"Units whose cell type differs (DANDI 'unknown' where CRCNS has none counts as same):\",\n      int((cmp_.units_crcns - cmp_.cell_type_same).sum()))\nprint(\"DANDI trials = CRCNS good trials with a photostimulation code, except in sessions:\")\nprint(cmp_[cmp_.eligible_not_in_dandi > 0][[\"session\", \"good_with_code\", \"dandi_trials\", \"eligible_not_in_dandi\"]].to_string(index=False))\nprint(\"DANDI trial codes and outcomes equal CRCNS for every matched trial:\",\n      bool(cmp_.codes_same.all() and cmp_.outcomes_same.all()))\nex = dandi[\"BAYLORCD8_20171018\"]\nprint(\"\\nDANDI trial column descriptions:\", {k: v for k, v in ex[\"trial_columns\"].items() if k in (\"cue_time\", \"pole_in_time\")})\nprint(\"DANDI cue_time minus start_time, first trials (s):\", (ex[\"trials\"].cue_time - ex[\"trials\"].start_time).head(3).round(3).tolist())\nprint(\"CRCNS second CueTime column, median minus first column (s):\",\n      round(float(np.nanmedian(np.concatenate([(s.trials.cue_col2 - s.trials.cue).to_numpy() for s in sessions]))), 3),\n      \"; non-NaN first column in sessions with two columns:\",\n      {s.key: int(s.trials.cue.notna().sum()) for s in sessions if s.trials.cue_col2.notna().any()} if False else \"\")\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nThe two deposits hold the same recordings: every unit's spike times are identical, and every\nDANDI trial matches a CRCNS trial with the same photostimulation code and outcome. Each\nrecording is counted once here. DANDI keeps only the trials with GoodTrials = 1 and a valid\ncode, which the scripts also use, but in two sessions it lacks trials CRCNS holds (printed\nabove). DANDI rounds trial start times (differences up to 0.05 s) and describes `cue_time`\nand `pole_in_time` as relative to the trial start, while the values are in session time.\n\"\"\")\n\ncode(r\"\"\"\nlat = []\nfor s in sessions:\n    t = s.trials[s.trials.good & s.trials.ptype.notna()]\n    for c in sorted(t.ptype.unique()):\n        tc = t[t.ptype == c]\n        ref = np.where(np.isin(c, [1, 3]), tc.pole_in, tc.pole_out) if c > 0 else tc.pole_out\n        on = tc.laser_on - ref\n        lat.append(dict(session=s.key, form=crcns[s.key][\"laser_form\"], code=int(c), n=len(tc),\n                        lit=round(float(tc.laser_on.notna().mean()), 2),\n                        onset_median_ms=round(float(np.nanmedian(on)) * 1000, 1) if on.notna().any() else np.nan,\n                        onset_iqr_ms=round(float(np.nanpercentile(on, 75) - np.nanpercentile(on, 25)) * 1000, 1) if on.notna().any() else np.nan,\n                        dur_median_s=round(float(np.nanmedian(tc.laser_off - tc.laser_on)), 3) if on.notna().any() else np.nan,\n                        mean_power=round(float(np.nanmedian(tc.laser_mean[tc.laser_on.notna()])), 2) if on.notna().any() else np.nan,\n                        peak=round(float(np.nanmedian(tc.laser_peak)), 2)))\nlat = pd.DataFrame(lat)\nprint(\"Laser power trace ('laser_power' channel) per session and code: fraction of trials with light,\")\nprint(\"onset relative to the epoch the code names (sample: pole in; delay: pole out), duration, mean power while on, peak:\")\nprint(lat[lat.code > 0].to_string(index=False))\nprint(\"\\nControl trials with light:\", int((lat[lat.code == 0].lit > 0).sum()), \"sessions of\", int((lat.code == 0).sum()))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nLaser traces: in the 2017 and 2018 sessions (stored one row per trial) the light starts within\n2 ms of the epoch the code names, lasts 0.455 s for photo-activation (10 pulses at 20 Hz) and\n0.494 s or 1.295 s for codes 5 and 6, as the descriptor and Methods say. The traces confirm the\ntiming of the stimulation relative to the trial events in those sessions. The 2015 sessions\nstore the series differently (one long series with a trial number per sample); their summary is\nprinted as it comes out and is discussed in the summary. The power values are those of the\n`laser_power` channel, which the files say is in mW.\n\"\"\")\n\ncode(r\"\"\"\n# Clock check: trial-type selectivity should be absent before the sample epoch and appear after it,\n# and photostimulation should change ALM rates within milliseconds of the light onset.\nrng = np.random.default_rng(100)\nwin = np.arange(-1.0, 1.21, 0.2)    # window starts relative to pole in (sample onset), 200 ms windows\nfrac = []\nfor shift_name, shift in [(\"true\", 0.0), (\"shifted by -2 s\", -2.0)]:\n    nsig = np.zeros(len(win)); ntot = 0\n    for s in sessions:\n        if s.group == \"inhibition\":\n            continue\n        t = s.trials\n        for u in s.pyramidal():\n            m = s.base_mask() & (t.ptype == 0).to_numpy() & t.correct.to_numpy() & s.stable(u, len(t))\n            R, L = m & (t.instructed == \"R\").to_numpy(), m & (t.instructed == \"L\").to_numpy()\n            if R.sum() < 5 or L.sum() < 5:\n                continue\n            ntot += 1\n            pi = t.pole_in.to_numpy() + shift\n            for k, w0 in enumerate(win):\n                c = s.counts(u, pi + w0, pi + w0 + 0.2)\n                if np.var(c[R]) + np.var(c[L]) > 0 and stats.ttest_ind(c[R], c[L]).pvalue < 0.05:\n                    nsig[k] += 1\n    frac.append(pd.Series(nsig / ntot, index=np.round(win, 1), name=f\"{shift_name} (n={ntot})\"))\nprint(\"Fraction of photo-activation-session pyramidal neurons selective (t-test p<0.05) in 200 ms windows\")\nprint(\"starting at the given time from pole in (sample onset), with true and shifted alignment:\")\nprint(pd.concat(frac, axis=1).round(3).to_string())\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nWith the true alignment the fraction of selective neurons is near the 5% false-positive rate\nbefore sample onset and rises after it; with the trial events shifted by 2 s the rise moves\naccordingly (printed). Spikes and trial events share a clock in the photo-activation sessions;\nthe rapid photostimulation responses in the claim sections below (latencies of a few ms from\nthe light onset) show it for the stimulation trials of all three groups.\n\"\"\")\n\n# ---------------------------------------------------------------- behavior\nmd(r\"\"\"\n## Behavior in the recording sessions\n\nThe claims on Fig. 1g, 1h and 1k concern behavior sessions; the datasets hold only the\nrecording sessions, in which photostimulation was on 33% of trials (Methods). Supplemental\nTable 1 shows that the 6 fastigial photo-activation mice of Fig. 1g are the 6 recorded ones,\nso the recording sessions hold part of their behavior. Performance is the fraction correct\nexcluding early-lick and no-lick trials, on good trials (B1). Contra and ipsi are relative to\nthe manipulated CN, which the Methods and the photostimulation codes put contralateral to the\nrecorded ALM; the files' CN side disagrees for three photo-inhibition mice (see the summary),\nso both are run where it matters.\n\"\"\")\n\ncode(r\"\"\"\nfa = [s for s in sessions if s.group == \"fastigial\"]\nde = [s for s in sessions if s.group == \"dentate\"]\ninh = [s for s in sessions if s.group == \"inhibition\"]\ntab_fa = G.perf_table(fa, [0, 1, 2])\ntab_de = G.perf_table(de, [0, 3, 4])\ntab_in = G.perf_table(inh, [0, 5, 6])\ntab_in_meta = G.perf_table(inh, [0, 5, 6], contra_from=\"metadata\")\n\n\ndef show(r):\n    return {k: (round(float(v), 4) if isinstance(v, (float, np.floating)) else v) for k, v in r.items()}\n\"\"\")\n\nmd(r\"\"\"\n### fig1g-fastigial-activation-early-sample-no-effect\n\n> Fastigial photo-activation during the early sample epoch does not affect behavioral choice\n> for either trial type.\n\nCriterion: per trial type, control against early sample photo-activation (code 1, 0.455 s),\none-sided bootstrap of B1; reproduced when p > 0.05 for both trial types.\n\"\"\")\n\ncode(r\"\"\"\nrng = np.random.default_rng(11)\nfor side in [\"contra\", \"ipsi\"]:\n    print(side, show(G.hier_boot(tab_fa, 1, side, rng=rng)))\nprint(\"pooled\", show(G.hier_boot(tab_fa, 1, None, rng=rng)))\nprint(\"\\nPer mouse (pooled types), control and sample photo-activation:\")\nfor m, g in tab_fa.groupby(\"mouse\"):\n    r = G.hier_boot(g, 1, None, rng=rng, n_boot=2000)\n    print(f\"  {m}: control {r['ctrl']:.3f} (n={r['n_ctrl']}), stim {r['stim']:.3f} (n={r['n_stim']})\")\n\"\"\", tags=[\"claim:fig1g-fastigial-activation-early-sample-no-effect\"])\n\nmd(r\"\"\"\n### fig1g-fastigial-activation-delay-errors\n\n> Fastigial photo-activation during the early delay epoch lowers behavioral performance, even\n> though the photostimulus ends 800 ms before the movement.\n\nCriterion: pooled performance, control against early delay photo-activation (code 2), one-sided\nbootstrap p < 0.05. The light ends 0.455 s after delay onset, 0.845 s before the go cue (laser\ntraces above).\n\"\"\")\n\ncode(r\"\"\"\nrng = np.random.default_rng(12)\nr = G.hier_boot(tab_fa, 2, None, rng=rng)\nprint(show(r))\nprint(\"p reported as the fraction of 10,000 resamples without a drop; 0 means < 0.0001\")\nfor m, g in tab_fa.groupby(\"mouse\"):\n    rr = G.hier_boot(g, 2, None, rng=rng, n_boot=2000)\n    print(f\"  {m}: control {rr['ctrl']:.3f}, stim {rr['stim']:.3f}, change {rr['change']:+.3f}\")\n\"\"\", tags=[\"claim:fig1g-fastigial-activation-delay-errors\"])\n\nmd(r\"\"\"\n### ed10b-fastigial-activation-errors-during-recording\n\n> In the ALM recording sessions, contralateral fastigial photo-activation lowers behavioral\n> performance, with \"lick left\" and \"lick right\" trials pooled, in the 6 mice.\n\nCriterion: same comparison as above, reproduced when the one-sided hierarchical bootstrap gives\np < 0.001. The numbers are those printed for fig1g-fastigial-activation-delay-errors; they are\nrepeated here with their own generator.\n\"\"\")\n\ncode(r\"\"\"\nrng = np.random.default_rng(13)\nr = G.hier_boot(tab_fa, 2, None, rng=rng)\nprint(show(r))\nprint(\"mice:\", r[\"n_mice\"], \"sessions:\", r[\"n_sessions\"])\n\"\"\", tags=[\"claim:ed10b-fastigial-activation-errors-during-recording\"])\n\nmd(r\"\"\"\n### fig1h-fastigial-activation-delay-bias\n\n> Fastigial photo-activation during the delay epoch biases future movements toward either the\n> contralateral or the ipsilateral direction, depending on the mouse.\n\nCriterion: per mouse, change in performance on contralateral and ipsilateral trials, per-mouse\none-sided bootstrap (sessions and trials of that mouse) at p < 0.05; reproduced when under one\nreading at least one mouse has a significant contralateral drop larger than its ipsilateral drop\nand at least one a significant ipsilateral drop larger than its contralateral drop. Reading (a),\nearly delay 0.455 s (code 2), is in the data; reading (b), the 1.255 s whole-delay experiment,\nis not.\n\"\"\")\n\ncode(r\"\"\"\nrng = np.random.default_rng(14)\nrows = []\nfor m, g in tab_fa.groupby(\"mouse\"):\n    rc = G.hier_boot(g, 2, \"contra\", rng=rng); ri = G.hier_boot(g, 2, \"ipsi\", rng=rng)\n    rows.append(dict(mouse=m, contra_ctrl=rc[\"ctrl\"], contra_stim=rc[\"stim\"], contra_change=rc[\"change\"], contra_p=rc[\"p_drop\"],\n                     ipsi_ctrl=ri[\"ctrl\"], ipsi_stim=ri[\"stim\"], ipsi_change=ri[\"change\"], ipsi_p=ri[\"p_drop\"]))\nb = pd.DataFrame(rows)\nb[\"contra_biased\"] = (b.contra_p < 0.05) & (b.contra_change < b.ipsi_change)\nb[\"ipsi_biased\"] = (b.ipsi_p < 0.05) & (b.ipsi_change < b.contra_change)\nprint(b.round(4).to_string(index=False))\nprint(\"mice with a significant larger contralateral drop:\", int(b.contra_biased.sum()),\n      \"; with a significant larger ipsilateral drop:\", int(b.ipsi_biased.sum()))\n\"\"\", tags=[\"claim:fig1h-fastigial-activation-delay-bias\"])\n\nmd(r\"\"\"\n### fig1g-dentate-activation-little-effect\n\n> Dentate photo-activation produces little effect on behavioral choice.\n\nCriterion: pooled performance, control against delay dentate photo-activation, one-sided\nbootstrap; a claim of absence, reproduced when it does not find a drop at p < 0.05 (paper\np = 0.06). Reading (a), early delay 0.455 s (code 4), in the 3 recorded dentate mice; the paper's\n8 dentate mice and reading (b) are not in the data.\n\"\"\")\n\ncode(r\"\"\"\nrng = np.random.default_rng(15)\nprint(\"pooled\", show(G.hier_boot(tab_de, 4, None, rng=rng)))\nfor side in [\"contra\", \"ipsi\"]:\n    print(side, show(G.hier_boot(tab_de, 4, side, rng=rng)))\nprint(\"sample epoch (code 3), pooled, for reference:\", show(G.hier_boot(tab_de, 3, None, rng=rng)))\n\"\"\", tags=[\"claim:fig1g-dentate-activation-little-effect\"])\n\nmd(r\"\"\"\n### fig1k-inhibition-delay-bias\n\n> Fastigial photo-inhibition during the delay epoch biases future movements to the\n> contralateral or the ipsilateral direction, depending on the mouse.\n\nCriterion: as fig1h-fastigial-activation-delay-bias, on delay photo-inhibition trials; readings\n(a) 0.5 s early delay (code 5; the late delay is not in the data) and (b) 1.3 s whole delay\n(code 6). The data hold the 4 recorded L7-cre x Ai32 mice (CD8, CD12, CD13, CD14), not the 7\nand 3 behavior mice of Extended Data Fig. 2h and 2g (of which CD12 and CD13 are in both). Contra\nand ipsi from the paper's rule (CN contralateral to the recorded ALM) and, as a variant, from\nthe files' CN side.\n\"\"\")\n\ncode(r\"\"\"\nrng = np.random.default_rng(16)\nfor lab, tab in [(\"paper rule\", tab_in), (\"files' CN side\", tab_in_meta)]:\n    for code_ in (5, 6):\n        rows = []\n        for m, g in tab.groupby(\"mouse\"):\n            rc = G.hier_boot(g, code_, \"contra\", rng=rng); ri = G.hier_boot(g, code_, \"ipsi\", rng=rng)\n            rows.append(dict(mouse=m, contra_change=rc[\"change\"], contra_p=rc[\"p_drop\"], ipsi_change=ri[\"change\"], ipsi_p=ri[\"p_drop\"],\n                             n_stim=rc[\"n_stim\"] + ri[\"n_stim\"]))\n        b = pd.DataFrame(rows)\n        b[\"contra_biased\"] = (b.contra_p < 0.05) & (b.contra_change < b.ipsi_change)\n        b[\"ipsi_biased\"] = (b.ipsi_p < 0.05) & (b.ipsi_change < b.contra_change)\n        print(f\"{lab}, code {code_} ({G.CODES[code_]}):\")\n        print(b.round(4).to_string(index=False))\n        print(f\"  contra-biased mice {int(b.contra_biased.sum())}, ipsi-biased mice {int(b.ipsi_biased.sum())}\\n\")\nprint(\"Pooled over mice:\", {c: show(G.hier_boot(tab_in, c, None, rng=rng)) for c in (5, 6)})\n\"\"\", tags=[\"claim:fig1k-inhibition-delay-bias\"])\n\n# ---------------------------------------------------------------- Fig 2\nmd(r\"\"\"\n## ALM selectivity (Fig. 2)\n\nUnits as E1 (pyramidal), in the 34 photo-activation sessions (the Fig. 2 population; the paper's\n39 sessions include a tenth mouse that is not deposited). Selectivity test E2 on control trials.\nReadings: trials (a) correct, (b) correct and error grouped by instructed type; response window\n(a) 1.3 s, (b) 1.5 s after the go cue. The deposited Fig. 2 script uses (a) and (a).\n\"\"\")\n\ncode(r\"\"\"\nt0 = time.time()\nsel_rows = []\nfor s in sessions:\n    if s.group == \"inhibition\":\n        continue\n    for u in s.pyramidal():\n        for tr in (\"correct\", \"all\"):\n            for rw in (1.3, 1.5):\n                r = G.selectivity_tests(s, u, tr, rw)\n                r.update(session=s.key, mouse=s.mouse, unit=u[\"key\"], trials=tr, response_s=rw)\n                sel_rows.append(r)\nsel = pd.DataFrame(sel_rows)\np = sel[[\"sample\", \"delay\", \"response\"]].fillna(1) < 0.05\nsel[\"selective\"] = p.any(axis=1)\nsel[\"preparatory\"] = p[[\"sample\", \"delay\"]].any(axis=1)\nsel[\"peri\"] = p[\"response\"]\nsel[\"testable\"] = sel[[\"sample\", \"delay\", \"response\"]].notna().any(axis=1)\nsumm = sel.groupby([\"trials\", \"response_s\"]).agg(neurons=(\"unit\", \"size\"), testable=(\"testable\", \"sum\"),\n                                                  selective=(\"selective\", \"sum\"), preparatory=(\"preparatory\", \"sum\"),\n                                                  peri=(\"peri\", \"sum\"))\nsumm[\"frac_selective\"] = summ.selective / summ.neurons\nsumm[\"prep_of_all\"] = summ.preparatory / summ.neurons\nsumm[\"prep_of_selective\"] = summ.preparatory / summ.selective\nsumm[\"peri_of_all\"] = summ.peri / summ.neurons\nsumm[\"peri_of_selective\"] = summ.peri / summ.selective\nprint(summ.round(3).to_string())\nprint(f\"({time.time() - t0:.0f} s)\")\n\"\"\")\n\nmd(r\"\"\"\n### fig2-alm-selective-fraction\n\n> Most ALM putative pyramidal neurons (980 of 1194) distinguish \"lick left\" from \"lick right\"\n> trials in their spike counts.\n\nCriterion: fraction within 0.82 ± 0.082 under one reading; the counts are judged only where the\ndataset holds all units (it holds 34 of the 39 sessions).\n\"\"\")\n\ncode(r\"\"\"\nprint(summ[[\"neurons\", \"selective\", \"frac_selective\"]].round(3).to_string())\na = sel[(sel.trials == \"correct\") & (sel.response_s == 1.3)]\nprint(\"\\nReading (a, a) by mouse:\")\nprint(a.groupby(\"mouse\").selective.agg([\"size\", \"sum\", \"mean\"]).round(3).to_string())\n# the same on the DANDI trial set\nrows = []\nfor s in sessions:\n    if s.group == \"inhibition\":\n        continue\n    keep = s.trials.in_dandi.to_numpy()\n    for u in s.pyramidal():\n        t = s.trials\n        m = s.base_mask() & (t.ptype == 0).to_numpy() & s.stable(u, len(t)) & t.correct.to_numpy() & keep\n        R, L = m & (t.instructed == \"R\").to_numpy(), m & (t.instructed == \"L\").to_numpy()\n        pi, po, cue = t.pole_in.to_numpy(), t.pole_out.to_numpy(), t.cue.to_numpy()\n        ps = []\n        for a_, b_ in [(pi, po), (po, cue), (cue, cue + 1.3)]:\n            r_ = s.counts(u, a_, b_) / (b_ - a_)\n            ps.append(stats.ttest_ind(r_[R], r_[L]).pvalue if R.sum() >= 2 and L.sum() >= 2 and np.var(r_[R]) + np.var(r_[L]) > 0 else 1.0)\n        rows.append(min(ps) < 0.05)\nprint(f\"\\nOn the DANDI trial set (reading a, a): {sum(rows)} of {len(rows)} selective ({np.mean(rows):.3f})\")\n\"\"\", tags=[\"claim:fig2-alm-selective-fraction\"])\n\nmd(r\"\"\"\n### fig2-preparatory-more-in-alm\n\n> Preparatory activity (selectivity before the response epoch) is more prevalent in ALM (59% of\n> neurons) than in the CN (35%).\n\nCriterion: sample or delay selectivity; denominators (a) all neurons, (b) selective neurons.\nThe CN neurons are not in either dataset; the criterion says the ALM fraction alone is tested\nwhere the CN neurons are missing (0.59 ± 0.059).\n\"\"\")\n\ncode(r\"\"\"\nprint(summ[[\"neurons\", \"selective\", \"preparatory\", \"prep_of_all\", \"prep_of_selective\"]].round(3).to_string())\n\"\"\", tags=[\"claim:fig2-preparatory-more-in-alm\"])\n\nmd(r\"\"\"\n### fig2-peri-movement-equal\n\n> Peri-movement activity (selectivity in the response epoch) is equally prevalent in ALM (67%)\n> and the CN (66%).\n\nCriterion: response-epoch selectivity; both fractions within tolerance under one reading. Only\nthe ALM half (0.67 ± 0.067) can be computed.\n\"\"\")\n\ncode(r\"\"\"\nprint(summ[[\"neurons\", \"selective\", \"peri\", \"peri_of_all\", \"peri_of_selective\"]].round(3).to_string())\n\"\"\", tags=[\"claim:fig2-peri-movement-equal\"])\n\nmd(r\"\"\"\n### fig2cd-selectivity-emerges-gradually\n\n> Selectivity for \"lick left\" and \"lick right\" trials emerges gradually in both the ALM and the\n> CN population averages, starting during the sample epoch and peaking in the response epoch.\n\nCriterion: population selectivity E3 (preferred type from 10 screening trials of each type,\ncorrect control trials, neurons with more than 15 trials of each type, as the Fig. 2 script)\nover (a) all selective neurons, (b) neurons with sample or delay selectivity. In a region,\nreproduced when the bootstrap 95% interval over neurons excludes zero in at least one window of\nthe sample epoch, the delay mean exceeds the sample mean, and the maximum lies in the response\nepoch. Only ALM can be tested.\n\"\"\")\n\ncode(r\"\"\"\nrng = np.random.default_rng(21)\nA = sel[(sel.trials == \"correct\") & (sel.response_s == 1.3)].set_index([\"session\", \"unit\"])\ncurves, prep_flag = [], []\nfor s in sessions:\n    if s.group == \"inhibition\":\n        continue\n    t = s.trials\n    for u in s.pyramidal():\n        row = A.loc[(s.key, u[\"key\"])]\n        if not row.selective or row.nR <= 15 or row.nL <= 15:\n            continue\n        m = s.base_mask() & (t.ptype == 0).to_numpy() & s.stable(u, len(t)) & t.correct.to_numpy()\n        r = G.pref_selectivity(s, u, m, {}, 10, rng)\n        if r is None:\n            continue\n        curves.append(r[0]); prep_flag.append(bool(row.preparatory))\ncurves, prep_flag = np.array(curves), np.array(prep_flag)\ng = G.GRID\nsamp, dl, resp = (g > -2.6) & (g < -1.3), (g > -1.3) & (g < 0), (g > 0) & (g < 1.3)\nfor name, X in [(\"(a) all selective\", curves), (\"(b) sample or delay selective\", curves[prep_flag])]:\n    m_, lo, hi = G.boot_mean_ci(X, rng, 10000)\n    print(f\"{name}: n={len(X)}; sample windows with interval above 0: {int((lo[samp] > 0).sum())} of {int(samp.sum())}, \"\n          f\"first at {g[samp][lo[samp] > 0][0] if (lo[samp] > 0).any() else np.nan:.2f} s; \"\n          f\"mean sample {m_[samp].mean():.2f}, delay {m_[dl].mean():.2f}, response {m_[resp].mean():.2f} spikes/s; \"\n          f\"maximum {m_[(g > -3) & (g < 1.8)].max():.2f} at {g[(g > -3) & (g < 1.8)][np.argmax(m_[(g > -3) & (g < 1.8)])]:.2f} s from the go cue\")\n    print(f\"   mean before sample onset (-3.0 to -2.6 s): {m_[(g > -3) & (g < -2.6)].mean():.2f}\")\nfig, ax = plt.subplots(figsize=(6, 3))\nm_, lo, hi = G.boot_mean_ci(curves, rng, 2000)\nax.fill_between(g, lo, hi, color=\"0.8\"); ax.plot(g, m_, \"k\")\nfor x in (-2.6, -1.3, 0):\n    ax.axvline(x, ls=\":\", c=\"0.5\")\nax.set_xlim(-3, 1.8); ax.set_xlabel(\"time from go cue (s)\"); ax.set_ylabel(\"selectivity (spikes/s)\")\nprint(f\"plotted range: {np.nanmin(lo[(g > -3) & (g < 1.8)]):.2f} to {np.nanmax(hi[(g > -3) & (g < 1.8)]):.2f}\")\nplt.show()\n\"\"\", tags=[\"claim:fig2cd-selectivity-emerges-gradually\"])\n\n# ---------------------------------------------------------------- photostim on ALM neurons\nmd(r\"\"\"\n## ALM responses to CN photostimulation (Figs. 3 and 4)\n\nModulation E4: two-tailed t-test of spike counts, control against photostimulation trials, both\ntrial types pooled, p < 0.01; neurons with at least 8 control trials of each type and more than 3\nphotostimulation trials of each type (deposited FR script). Windows: (a) the photostimulation\nperiod (0.455 s for photo-activation, 1.3 s for code 6), (b) the whole delay epoch. Trials:\nall (correct, error and no-lick, as the FR script) and correct only. Latency E5: 10 ms bins in\n1 ms steps from delay onset, sign-flipped for suppressed neurons, first bin with p < 0.01,\n10,000 bootstrap resamples of neurons; the bin can be labelled by its start, centre or end\n(not stated in the paper), and all three are shown.\n\"\"\")\n\ncode(r\"\"\"\nt0 = time.time()\nmod = {}\nfine = {}\nfor grp, code_, dur in [(\"fastigial\", 2, 0.455), (\"dentate\", 4, 0.455), (\"inhibition\", 6, 1.3)]:\n    for which in (\"all\", \"correct\"):\n        rows, F = [], []\n        for s in sessions:\n            if s.group != grp:\n                continue\n            for u in s.pyramidal():\n                rd = G.modulation(s, u, code_, 0, \"cue\", which)\n                if rd is None:\n                    continue\n                rp = G.modulation(s, u, code_, 0, dur, which)\n                st_, fc = G.fine_change(s, u, code_, which)\n                rows.append(dict(session=s.key, mouse=s.mouse, unit=u[\"key\"], p_delay=rd[\"p\"], change_delay=rd[\"change\"],\n                                 rate_ctrl=rd[\"rate_ctrl\"], rate_stim=rd[\"rate_stim\"], p_stim=rp[\"p\"], change_stim=rp[\"change\"]))\n                F.append(fc)\n        mod[(grp, which)] = pd.DataFrame(rows)\n        fine[(grp, which)] = (st_, np.array(F))\nn_pyr = {g_: sum(len(s.pyramidal()) for s in sessions if s.group == g_) for g_ in (\"fastigial\", \"dentate\", \"inhibition\")}\nprint(\"pyramidal neurons per group:\", n_pyr)\ntabm = []\nfor (grp, which), d in mod.items():\n    for w in (\"stim\", \"delay\"):\n        sig = d[f\"p_{w}\"] < 0.01\n        tabm.append(dict(group=grp, trials=which, window=w, tested=len(d), modulated=int(sig.sum()),\n                         frac_of_tested=sig.mean(), frac_of_pyramidal=sig.sum() / n_pyr[grp],\n                         increase=int((sig & (d[f\"change_{w}\"] > 0)).sum()), decrease=int((sig & (d[f\"change_{w}\"] < 0)).sum())))\ntabm = pd.DataFrame(tabm)\nprint(tabm.round(3).to_string(index=False))\nprint(f\"({time.time() - t0:.0f} s)\")\n\"\"\")\n\ncode(r\"\"\"\nt0 = time.time()\nlat_rows = []\nfor (grp, which), d in mod.items():\n    starts, F = fine[(grp, which)]\n    for w in (\"stim\", \"delay\"):\n        sig = (d[f\"p_{w}\"] < 0.01).to_numpy()\n        signs = np.sign(d[f\"change_{w}\"].to_numpy())[sig]\n        L = G.latency(F[sig], signs, np.random.default_rng(31), n_boot=10000, starts=starts)\n        for lab, sh in ((\"start\", 0.0), (\"centre\", 5.0), (\"end\", 10.0)):\n            lat_rows.append(dict(group=grp, trials=which, window=w, label=lab, n=L[\"n\"],\n                                 onset_all_ms=L[\"onset_all\"] + sh, boot_mean_ms=L[\"boot_mean\"] + sh,\n                                 boot_sd_ms=L[\"boot_sd\"], no_onset=L[\"no_onset\"]))\nlatd = pd.DataFrame(lat_rows)\nprint(latd.round(2).to_string(index=False))\nprint(f\"({time.time() - t0:.0f} s)\")\n\"\"\")\n\nmd(r\"\"\"\n### fig4-fastigial-activation-alm-latency\n\n> Fastigial photo-activation changes ALM activity rapidly (latency 4.5 plus or minus 2.6 ms),\n> consistent with a disynaptic pathway through the thalamus.\n\nCriterion: latency within 4.5 ± 2.6 ms under one reading, and the count of modulated neurons\nwithin 227 ± 22.7, as the dataset holds all 6 mice.\n\"\"\")\n\ncode(r\"\"\"\nprint(tabm[tabm.group == \"fastigial\"].round(3).to_string(index=False))\nprint(latd[latd.group == \"fastigial\"].round(2).to_string(index=False))\nd = mod[(\"fastigial\", \"all\")]\nprint(\"\\nModulated (stimulation window, all trials) by mouse:\")\nprint(d.assign(sig=d.p_stim < 0.01).groupby(\"mouse\").sig.agg([\"size\", \"sum\"]).to_string())\n# variant: no minimum trial count beyond two trials of each condition\ncnt = 0; tested = 0\nfor s in fa:\n    for u in s.pyramidal():\n        ctrl, stim, _ = G.stim_trials(s, u, 2, \"all\")\n        if ctrl.sum() < 2 or stim.sum() < 2:\n            continue\n        tested += 1\n        po = s.trials.pole_out.to_numpy()\n        c = s.counts(u, po, po + 0.455)\n        if np.var(c[ctrl]) + np.var(c[stim]) > 0 and stats.ttest_ind(c[ctrl], c[stim]).pvalue < 0.01:\n            cnt += 1\nprint(f\"\\nVariant without the script's minimum trial counts (stimulation window, all trials): {cnt} of {tested}\")\n\"\"\", tags=[\"claim:fig4-fastigial-activation-alm-latency\"])\n\nmd(r\"\"\"\n### fig4g-dentate-effect-recovers\n\n> Dentate photo-activation also changes ALM responses (latency 8.3 plus or minus 5.0 ms), but ALM\n> activity recovers quickly after it.\n\nCriterion: latency within 8.3 ± 5.0 ms and count within 163 ± 16.3 under one reading, and the\nfraction of significant neurons in bins starting 1 s or more after photostimulus offset not\nabove the comparison of fig4f (p >= 0.05) and lower than the fastigial fraction (one-sided test\nof two proportions, p < 0.05). The persistence numbers are printed in the fig4f section.\n\"\"\")\n\ncode(r\"\"\"\nprint(tabm[tabm.group == \"dentate\"].round(3).to_string(index=False))\nprint(latd[latd.group == \"dentate\"].round(2).to_string(index=False))\n\"\"\", tags=[\"claim:fig4g-dentate-effect-recovers\"])\n\nmd(r\"\"\"\n### fig4f-fastigial-effect-persists\n\n> Transient fastigial photo-activation alters ALM preparatory activity long (more than 1 s)\n> after the photostimulus ends.\n\nCriterion: E4 in 400 ms bins in 50 ms steps (Methods), fraction of neurons with p < 0.01 in\nbins starting 1 s or more after photostimulus offset (offset at 0.845 s before the go cue, so\nthese bins lie in the response epoch); compared with (a) 1% by a one-sided binomial test, (b)\nthe fraction in bins ending before photostimulus onset by a one-sided test of two proportions.\nThe mean fraction over those bins is tested, with the number of neurons as n. Neurons and trials\nas the FR script (all trials).\n\"\"\")\n\ncode(r\"\"\"\nt0 = time.time()\ntb = np.round(np.arange(-3, 2.0001, 0.05), 3)      # bin centres relative to the go cue (FR script)\npersist = {}\nfor grp, code_, ss in [(\"fastigial\", 2, fa), (\"dentate\", 4, de)]:\n    P = []\n    for s in ss:\n        cue = s.trials.cue.to_numpy()\n        for u in s.pyramidal():\n            ctrl, stim, en = G.stim_trials(s, u, code_, \"all\")\n            if not en:\n                continue\n            ps = []\n            for b_ in tb:\n                c = s.counts(u, cue + b_ - 0.2, cue + b_ + 0.2)\n                ps.append(stats.ttest_ind(c[ctrl], c[stim]).pvalue if np.var(c[ctrl]) + np.var(c[stim]) > 0 else 1.0)\n            P.append(ps)\n    P = np.array(P)\n    persist[grp] = P\npre = (tb + 0.2 <= -1.3) & (tb - 0.2 >= -3.0)\npost = (tb - 0.2 >= -1.3 + 0.455 + 1.0) & (tb - 0.2 < 1.3)\nres_p = {}\nfor grp, P in persist.items():\n    f = (P < 0.01).mean(0)\n    n = len(P)\n    fpost, fpre = f[post].mean(), f[pre].mean()\n    k = int(round(fpost * n))\n    pa = stats.binomtest(k, n, 0.01, alternative=\"greater\").pvalue\n    kp = int(round(fpre * n))\n    z = sm.stats.proportions_ztest([k, kp], [n, n], alternative=\"larger\")\n    res_p[grp] = (fpost, n, k)\n    print(f\"{grp}: neurons {n}; fraction significant: before onset {fpre:.4f}, during light max {f[(tb > -1.3) & (tb < -0.845)].max():.3f}, \"\n          f\">=1 s after offset {fpost:.4f} ({post.sum()} bins); (a) vs 1%: binomial p = {pa:.2g}; (b) vs before onset: z = {z[0]:.2f}, p = {z[1]:.2g}\")\n    print(\"   fraction per bin (every 4th bin, centre in s from go cue):\",\n          \" \".join(f\"{b_:.2f}:{x:.3f}\" for b_, x in zip(tb[::4], f[::4])))\n(ff, nf, kf), (fd, nd, kd) = res_p[\"fastigial\"], res_p[\"dentate\"]\nz = sm.stats.proportions_ztest([kd, kf], [nd, nf], alternative=\"smaller\")\nprint(f\"dentate lower than fastigial after offset: {fd:.4f} vs {ff:.4f}, z = {z[0]:.2f}, one-sided p = {z[1]:.2g}\")\nprint(f\"({time.time() - t0:.0f} s)\")\n\"\"\", tags=[\"claim:fig4f-fastigial-effect-persists\", \"claim:fig4g-dentate-effect-recovers\"])\n\nmd(r\"\"\"\n### fig3d-alm-altered-by-cn-inhibition\n\n> CN photo-inhibition during the delay rapidly alters the activity of many ALM neurons (197 of\n> 454), with a latency of 7.1 plus or minus 3.8 ms.\n\nCriterion: 1.3 s delay photo-inhibition (code 6), E4 on the whole delay epoch, latency E5 (both\nwindow readings); reproduced when the count (or the fraction 0.43 where the dataset holds fewer\nneurons) and the latency are within tolerance under one reading.\n\"\"\")\n\ncode(r\"\"\"\nprint(tabm[tabm.group == \"inhibition\"].round(3).to_string(index=False))\nprint(latd[latd.group == \"inhibition\"].round(2).to_string(index=False))\nd = mod[(\"inhibition\", \"all\")]\nprint(\"\\nBy mouse (delay window, all trials):\")\nprint(d.assign(sig=d.p_delay < 0.01).groupby(\"mouse\").sig.agg([\"size\", \"sum\", \"mean\"]).round(3).to_string())\n\"\"\", tags=[\"claim:fig3d-alm-altered-by-cn-inhibition\"])\n\nmd(r\"\"\"\n### fig3e-alm-mean-rate-unchanged\n\n> Despite the changes in individual neurons, the average ALM spike rate is nearly unchanged by\n> CN photo-inhibition (4.15 against 4.39 spikes/s).\n\nCriterion: a claim of absence on the paper's two-tailed t-test; mean delay rate per neuron in\ncontrol and photo-inhibition trials (E4 trials), neurons (a) all tested pyramidal, (b)\nmodulated; t-test paired and unpaired. Reproduced when the rates are within tolerance under one\nreading of the neurons and the t-test finds no difference.\n\"\"\")\n\ncode(r\"\"\"\nfor which in (\"all\", \"correct\"):\n    d = mod[(\"inhibition\", which)]\n    for nm, dd in [(\"(a) all tested\", d), (\"(b) modulated\", d[d.p_delay < 0.01])]:\n        print(f\"trials {which}, {nm}: n={len(dd)}, control {dd.rate_ctrl.mean():.2f}, inhibition {dd.rate_stim.mean():.2f} spikes/s, \"\n              f\"change {dd.rate_stim.mean() - dd.rate_ctrl.mean():+.2f}; paired p = {stats.ttest_rel(dd.rate_ctrl, dd.rate_stim).pvalue:.3f}, \"\n              f\"unpaired p = {stats.ttest_ind(dd.rate_ctrl, dd.rate_stim).pvalue:.3f}\")\n\"\"\", tags=[\"claim:fig3e-alm-mean-rate-unchanged\"])\n\nmd(r\"\"\"\n### fig3e-alm-increase-decrease\n\n> Among ALM neurons modulated by CN photo-inhibition, 108 increase and 89 decrease their\n> responses.\n\nCriterion: sign of the delay rate change among the neurons of fig3d; both counts within\ntolerance, or, where the dataset holds fewer neurons, the increase fraction 0.55 within 10%.\n\"\"\")\n\ncode(r\"\"\"\nx = tabm[(tabm.group == \"inhibition\")]\nx = x.assign(increase_fraction=x.increase / x.modulated)\nprint(x[[\"trials\", \"window\", \"tested\", \"modulated\", \"increase\", \"decrease\", \"increase_fraction\"]].round(3).to_string(index=False))\n\"\"\", tags=[\"claim:fig3e-alm-increase-decrease\"])\n\n# ---------------------------------------------------------------- selectivity under stimulation\nmd(r\"\"\"\n## ALM selectivity under CN photostimulation\n\nPopulation selectivity E3 over selective neurons (E2, correct trials, 1.3 s response window)\ntested on more than 3 trials in every condition (control trials beyond the screening trials,\nand photostimulation trials, of each type), all trials grouped by instructed type (Extended\nData Figs. 5b and 9c legends). Preferred type from 10 screening control trials of each type\n(Methods); the deposited photostimulation scripts use 5, shown as a variant.\n\"\"\")\n\ncode(r\"\"\"\nt0 = time.time()\nselstim = {}\nfor grp, code_ in [(\"inhibition\", 6), (\"fastigial\", 2), (\"dentate\", 4)]:\n    for nscr in (10, 5):\n        rng = np.random.default_rng(41 + nscr)\n        C, Z, keys = [], [], []\n        for s in sessions:\n            if s.group != grp:\n                continue\n            t = s.trials\n            n = len(t)\n            R = (t.instructed == \"R\").to_numpy(); L = (t.instructed == \"L\").to_numpy()\n            for u in s.pyramidal():\n                e2 = G.selectivity_tests(s, u, \"correct\")\n                if not any(e2[e] < 0.05 for e in (\"sample\", \"delay\", \"response\") if not np.isnan(e2[e])):\n                    continue\n                base = s.base_mask() & s.stable(u, n) & (t.correct | t.error).to_numpy()\n                ctrl = base & (t.ptype == 0).to_numpy(); stim = base & (t.ptype == code_).to_numpy()\n                if min((ctrl & R).sum(), (ctrl & L).sum()) - nscr <= 3 or min((stim & R).sum(), (stim & L).sum()) <= 3:\n                    continue\n                r = G.pref_selectivity(s, u, ctrl, {\"stim\": stim}, nscr, rng)\n                C.append(r[0]); Z.append(r[1][\"stim\"]); keys.append((s.key, u[\"key\"]))\n        selstim[(grp, nscr)] = (np.array(C), np.array(Z), keys)\ng = G.GRID\nW = {\"whole delay\": (g > -1.3) & (g < 0), \"last 500 ms of delay\": (g > -0.5) & (g < 0),\n     \"light offset to go cue\": (g > -1.3 + 0.455) & (g < 0)}\nrows = []\nfor (grp, nscr), (C, Z, keys) in selstim.items():\n    rng = np.random.default_rng(50)\n    for wn, w in W.items():\n        if grp == \"inhibition\" and wn == \"light offset to go cue\":\n            continue\n        c, z = np.nanmean(C[:, w], 1), np.nanmean(Z[:, w], 1)\n        mc, lc, hc = G.boot_mean_ci(c, rng); mz, lz, hz = G.boot_mean_ci(z, rng); md_, ld, hd = G.boot_mean_ci(c - z, rng)\n        rows.append(dict(group=grp, screen=nscr, window=wn, neurons=len(C), control=mc, control_lo=lc, control_hi=hc,\n                         stim=mz, stim_lo=lz, stim_hi=hz, diff=md_, diff_lo=ld, diff_hi=hd))\nselres = pd.DataFrame(rows)\nprint(selres.round(2).to_string(index=False))\nprint(f\"({time.time() - t0:.0f} s)\")\n\"\"\")\n\nmd(r\"\"\"\n### fig3f-alm-selectivity-abolished-by-cn-inhibition\n\n> CN photo-inhibition abolishes ALM trial-type selectivity.\n\nCriterion: control selectivity above zero and photo-inhibition selectivity not distinguishable\nfrom zero (its 95% interval includes zero), windows (a) whole delay, (b) last 500 ms.\n\"\"\")\n\ncode(r\"\"\"\nprint(selres[selres.group == \"inhibition\"].round(2).to_string(index=False))\nC, Z, keys = selstim[(\"inhibition\", 10)]\nprint(\"neurons by mouse:\", pd.Series([k[0].split(\"_\")[0] for k in keys]).value_counts().to_dict())\nfig, ax = plt.subplots(figsize=(6, 3))\nax.plot(G.GRID, np.nanmean(C, 0), \"k\", label=\"control\"); ax.plot(G.GRID, np.nanmean(Z, 0), \"c\", label=\"CN photo-inhibition\")\nfor x_ in (-2.6, -1.3, 0):\n    ax.axvline(x_, ls=\":\", c=\"0.5\")\nax.set_xlim(-3, 1.6); ax.legend(); ax.set_xlabel(\"time from go cue (s)\"); ax.set_ylabel(\"selectivity (spikes/s)\")\nsl = (G.GRID > -3) & (G.GRID < 1.6)\nprint(f\"plotted range: {min(np.nanmean(C, 0)[sl].min(), np.nanmean(Z, 0)[sl].min()):.2f} to {max(np.nanmean(C, 0)[sl].max(), np.nanmean(Z, 0)[sl].max()):.2f}\")\nplt.show()\n\"\"\", tags=[\"claim:fig3f-alm-selectivity-abolished-by-cn-inhibition\"])\n\nmd(r\"\"\"\n### fig4e-fastigial-activation-abolishes-alm-selectivity\n\n> Fastigial photo-activation abolishes selective persistent and ramping activity in most ALM\n> neurons, while in a minority it creates new preparatory activity.\n\nCriterion: n = 328 neurons expected; population selectivity lower in photo-activation trials\n(interval of the difference excludes zero) in the delay after the photostimulus ((a) light\noffset to go cue, (b) last 500 ms); per neuron, the t-test of E2 on that window (all trials by\ninstructed type), control against photo-activation trials: more than half of the\ncontrol-selective neurons lose significance, and fewer gain it than lose it.\n\"\"\")\n\ncode(r\"\"\"\nprint(selres[selres.group == \"fastigial\"].round(2).to_string(index=False))\nC, Z, keys = selstim[(\"fastigial\", 10)]\nkset = set(keys)\nfor wn, (a_rel, b_rel) in {\"(a) light offset to go cue\": (0.455, None), \"(b) last 500 ms\": (None, 0.5)}.items():\n    lose = gain = ctrl_sel = 0\n    for s in fa:\n        t = s.trials\n        n = len(t)\n        R = (t.instructed == \"R\").to_numpy(); L = (t.instructed == \"L\").to_numpy()\n        po, cue = t.pole_out.to_numpy(), t.cue.to_numpy()\n        a = po + a_rel if a_rel is not None else cue - b_rel\n        for u in s.pyramidal():\n            if (s.key, u[\"key\"]) not in kset:\n                continue\n            base = s.base_mask() & s.stable(u, n) & (t.correct | t.error).to_numpy()\n            ctrl = base & (t.ptype == 0).to_numpy(); stim = base & (t.ptype == 2).to_numpy()\n            c = s.counts(u, a, cue)\n            pc = stats.ttest_ind(c[ctrl & R], c[ctrl & L]).pvalue if np.var(c[ctrl & R]) + np.var(c[ctrl & L]) > 0 else 1\n            ps = stats.ttest_ind(c[stim & R], c[stim & L]).pvalue if np.var(c[stim & R]) + np.var(c[stim & L]) > 0 else 1\n            ctrl_sel += pc < 0.05\n            lose += (pc < 0.05) and not (ps < 0.05)\n            gain += (ps < 0.05) and not (pc < 0.05)\n    print(f\"{wn}: neurons {len(keys)}, selective in control {ctrl_sel}, lose significance {lose} ({lose / max(ctrl_sel, 1):.2f}), gain {gain}\")\n\"\"\", tags=[\"claim:fig4e-fastigial-activation-abolishes-alm-selectivity\"])\n\n# ---------------------------------------------------------------- coding direction\nmd(r\"\"\"\n## Coding direction (Fig. 4h, 4i; Extended Data Fig. 10)\n\nE6: sessions with more than 5 neurons and more than 5 trials per condition. Neurons are the\npyramidal units stable from the 50th trial to the 50th before the end, and trials those inside\nevery neuron's stable range, as the deposited CD script; rates in 400 ms windows in 10 ms\nsteps, labelled by window centre. Control trials are split at random into halves: correct trials\nof the first half estimate the cd (mean \"lick right\" minus mean \"lick left\" over windows centred\nin the delay, unit length) and the session offset; the second half and the photostimulation\ntrials (correct and error, by instructed type) are projected. Bootstrap over sessions.\n\"\"\")\n\ncode(r\"\"\"\nrng = np.random.default_rng(60)\ncds = []\nskipped = []\nfor s in sessions:\n    if s.group == \"inhibition\":\n        continue\n    r = G.cd_session(s, rng, stim_code=2 if s.group == \"fastigial\" else 4)\n    (cds.append(r) if r is not None else skipped.append(s.key))\nprint(f\"sessions used: {len(cds)} of {len(cds) + len(skipped)} \"\n      f\"(fastigial {sum(r['group'] == 'fastigial' for r in cds)}, dentate {sum(r['group'] == 'dentate' for r in cds)}); \"\n      f\"neurons per session {min(r['n_neurons'] for r in cds)} to {max(r['n_neurons'] for r in cds)}\")\nprint(\"not used:\", skipped)\ncent = cds[0][\"centres\"]\n\n\ndef separation(r, a, b):\n    return r[\"proj\"][r[\"sets\"][a]].mean(0) - r[\"proj\"][r[\"sets\"][b]].mean(0)\n\"\"\")\n\nmd(r\"\"\"\n### fig4i-cd-control-separation\n\n> In control trials, ALM activity trajectories for \"lick left\" and \"lick right\" diverge along\n> the coding direction during the sample epoch and stay separated through the delay epoch.\n\nCriterion: \"lick right\" minus \"lick left\" projection of independent control trials, mean over\nsessions with a bootstrap over sessions; reproduced when the 95% interval excludes zero at some\ntime in the sample epoch and at every window centred within the delay epoch.\n\"\"\")\n\ncode(r\"\"\"\nrng = np.random.default_rng(61)\nX = np.array([separation(r, \"test_R\", \"test_L\") for r in cds])\nm_, lo, hi = G.boot_mean_ci(X, rng)\nsamp = (cent > -2.6) & (cent < -1.3); dl = (cent >= -1.3) & (cent <= 0)\nprint(f\"sessions {len(X)}; sample-epoch windows with interval above 0: {int((lo[samp] > 0).sum())} of {int(samp.sum())} \"\n      f\"(first at {cent[samp][lo[samp] > 0][0]:.2f} s from the go cue)\")\nprint(f\"delay windows with interval above 0: {int((lo[dl] > 0).sum())} of {int(dl.sum())}; smallest lower bound {lo[dl].min():.2f}\")\nprint(f\"separation before sample onset (centres -3.0 to -2.8 s): {m_[(cent >= -3.0) & (cent <= -2.8)].mean():.2f}\")\nfig, ax = plt.subplots(figsize=(6, 3))\nax.fill_between(cent, lo, hi, color=\"0.8\"); ax.plot(cent, m_, \"k\")\nfor x_ in (-2.6, -1.3, 0):\n    ax.axvline(x_, ls=\":\", c=\"0.5\")\nax.set_xlabel(\"time from go cue (s)\"); ax.set_ylabel(\"R minus L projection\")\nprint(f\"plotted range: {lo.min():.2f} to {hi.max():.2f}\")\nplt.show()\n\"\"\", tags=[\"claim:fig4i-cd-control-separation\"])\n\nmd(r\"\"\"\n### fig4i-fastigial-collapses-cd\n\n> Fastigial photo-activation collapses ALM activity trajectories along the coding direction,\n> while dentate photo-activation minimally affects them.\n\nCriterion: separation in control, fastigial and dentate photo-activation trials in the last 400\nms of the delay and averaged from light offset to the go cue; \"collapse\" read as (a) fastigial\nseparation not distinguishable from zero, (b) lower than control (interval of the difference\nexcludes zero); reproduced when, in the same window, the fastigial separation collapses and the\ndentate separation does not differ from its control (interval of the difference includes zero).\n\"\"\")\n\ncode(r\"\"\"\nrng = np.random.default_rng(62)\nfor grp in (\"fastigial\", \"dentate\"):\n    R_ = [r for r in cds if r[\"group\"] == grp]\n    cs = np.array([separation(r, \"test_R\", \"test_L\") for r in R_]); st_ = np.array([separation(r, \"stim_R\", \"stim_L\") for r in R_])\n    for wn, w in [(\"last 400 ms\", np.isclose(cent, -0.2)), (\"light offset to go cue\", (cent >= -1.3 + 0.455) & (cent <= 0))]:\n        a, b = cs[:, w].mean(1), st_[:, w].mean(1)\n        ma, la, ha = G.boot_mean_ci(a, rng); mb, lb, hb = G.boot_mean_ci(b, rng); md_, ld, hd = G.boot_mean_ci(a - b, rng)\n        print(f\"{grp} ({len(R_)} sessions), {wn}: control {ma:.2f} [{la:.2f}, {ha:.2f}], photo-activation {mb:.2f} [{lb:.2f}, {hb:.2f}], \"\n              f\"control minus stim {md_:.2f} [{ld:.2f}, {hd:.2f}] ({md_ / ma:.0%} of control)\")\n\"\"\", tags=[\"claim:fig4i-fastigial-collapses-cd\"])\n\nmd(r\"\"\"\n### cd-captures-selectivity\n\n> The projection along the coding direction captures 64.1% of ALM population selectivity over\n> the sample and delay epochs and 27.0% of the total variance in task-related activity.\n\nCriterion: per session, control trials, sample and delay epochs; selectivity is the RMS of the\n\"lick right\" minus \"lick left\" rate difference, variance the RMS of the baseline-subtracted\nactivity (baseline: the 500 ms before sample onset); captured fraction (a) ratio of RMS along\nthe unit cd to RMS over all neurons, (b) its square. Reproduced when under one reading both\nmeans are within tolerance. Variants: measures on the cd-estimating trials (in sample) or on the\nindependent correct control trials; activity variance from condition means or from single\ntrials.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor r in cds:\n    X_, sets, cd = r[\"X\"], r[\"sets\"], r[\"cd\"]\n    w = (cent > r[\"pole_in\"]) & (cent <= 0)\n    base = (cent < r[\"pole_in\"]) & (cent >= r[\"pole_in\"] - 0.5)\n    corr = np.flatnonzero(np.isin(np.arange(X_.shape[1]), np.concatenate([sets[\"test_R\"], sets[\"test_L\"]])))\n    tc = sessions[[s.key for s in sessions].index(r[\"session\"])].trials.correct.to_numpy()\n    for nm, Rr, Ll in [(\"in sample\", sets[\"train_R\"], sets[\"train_L\"]),\n                       (\"held out\", sets[\"test_R\"][tc[sets[\"test_R\"]]], sets[\"test_L\"][tc[sets[\"test_L\"]]])]:\n        xr, xl = X_[:, Rr].mean(1), X_[:, Ll].mean(1)\n        D = (xr - xl)[:, w]\n        sel_ratio = np.sqrt(((cd @ D) ** 2).mean()) / np.sqrt((D ** 2).sum(0).mean())\n        b0 = (xr[:, base].mean(1) + xl[:, base].mean(1)) / 2\n        A = np.concatenate([xr[:, w], xl[:, w]], 1) - b0[:, None]\n        var_ratio = np.sqrt(((cd @ A) ** 2).mean()) / np.sqrt((A ** 2).sum(0).mean())\n        T = np.concatenate([X_[:, Rr][:, :, w], X_[:, Ll][:, :, w]], 1) - b0[:, None, None]\n        var_trial = np.sqrt((np.einsum(\"j,jit->it\", cd, T) ** 2).mean()) / np.sqrt((T ** 2).sum(0).mean())\n        rows.append(dict(session=r[\"session\"], trials=nm, sel_a=sel_ratio * 100, sel_b=sel_ratio ** 2 * 100,\n                         var_a=var_ratio * 100, var_b=var_ratio ** 2 * 100, var_trial_a=var_trial * 100, var_trial_b=var_trial ** 2 * 100))\ncap = pd.DataFrame(rows)\nagg = cap.groupby(\"trials\").agg([\"mean\", \"sem\", \"std\"]).drop(columns=\"session\", errors=\"ignore\")\nprint(agg.round(1).T.to_string())\n\"\"\", tags=[\"claim:cd-captures-selectivity\"])\n\nmd(r\"\"\"\n### ed10d-fastigial-endpoints-no-prediction\n\n> After fastigial photo-activation, the distance of ALM trajectories to the endpoints along the\n> coding direction no longer predicts future movements.\n\nCriterion: projection in the last 400 ms of the delay (window centred 0.2 s before the go cue)\nof fastigial photo-activation trials, pooled over sessions; logistic regression of lick direction\non the projection; a claim of absence, reproduced when the slope is not significant (p < 0.05).\nControl trials (independent half) for comparison. The projection is offset per session (E6);\nit is scaled by its standard deviation over the pooled trials for the fit, which does not change\nthe p-value.\n\"\"\")\n\ncode(r\"\"\"\nk = np.isclose(cent, -0.2)\nfor nm, a, b in [(\"fastigial photo-activation\", \"stim_R\", \"stim_L\"), (\"control (independent half)\", \"test_R\", \"test_L\")]:\n    xs, ys = [], []\n    for r in cds:\n        if r[\"group\"] != \"fastigial\":\n            continue\n        idx = np.concatenate([r[\"sets\"][a], r[\"sets\"][b]])\n        lk = r[\"licked\"][idx]\n        ok = lk != \"\"\n        xs.extend(r[\"proj\"][idx[ok]][:, k].ravel()); ys.extend((lk[ok] == \"R\").astype(int))\n    x_, y_ = np.array(xs), np.array(ys)\n    fit = sm.Logit(y_, sm.add_constant(x_ / x_.std())).fit(disp=0)\n    ci = fit.conf_int()[1]\n    q = pd.qcut(x_, 4, labels=False)\n    print(f\"{nm}: trials {len(x_)}, slope {fit.params[1]:.2f} [{ci[0]:.2f}, {ci[1]:.2f}] per s.d., p = {fit.pvalues[1]:.2g}; \"\n          f\"P(lick right) by projection quartile {[round(float(y_[q == i].mean()), 2) for i in range(4)]}\")\nprint(\"sessions:\", sum(r[\"group\"] == \"fastigial\" for r in cds))\n\"\"\", tags=[\"claim:ed10d-fastigial-endpoints-no-prediction\"])\n\nmd(r\"\"\"\n## Summary\n\nThe outcomes, with the numbers they rest on, are in the attempt record\n(`attempts/gao-2018-02.yaml`); the table here gives them in brief.\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nSUMMARY_TABLE\n\"\"\")\n\ncode(r\"\"\"\nprint(f\"total runtime {(time.time() - started) / 60:.1f} min, peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.1f} GB\")\n\"\"\")\n\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbf.write(nb, \"entries/gao-2018/reproduce_gao_2018.ipynb\")\nprint(\"written\", len(cells))\n"
}
```

```
File created successfully at: /tmp/claude-1001/make_nb.py (file state is current in your context — no need to Read it back)
```

**Agent**

Cleaning two leftover lines in the generator, then testing the cells with the cached data (real DANDI load, CRCNS from pickle).

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; python - <<'EOF'
s=open('make_nb.py').read()
s=s.replace('''print("Photostimulation code descriptions in the files:")
for line in sessions[0].trials.columns[:0]:
    pass
for key in''','''print("Photostimulation code descriptions in the files:")
for key in''')
s=s.replace('''print("CRCNS second CueTime column, median minus first column (s):",
      round(float(np.nanmedian(np.concatenate([(s.trials.cue_col2 - s.trials.cue).to_numpy() for s in sessions]))), 3),
      "; non-NaN first column in sessions with two columns:",
      {s.key: int(s.trials.cue.notna().sum()) for s in sessions if s.trials.cue_col2.notna().any()} if False else "")''','''two = [s for s in sessions if s.trials.cue_col2.notna().any()]
d2 = np.concatenate([(s.trials.cue_col2 - s.trials.cue)[s.trials.good].to_numpy() for s in two])
print(f"CRCNS CueTime has two columns in {len(two)} sessions; on good trials the second minus the first: "
      f"median {np.nanmedian(d2):.3f} s, nonzero in {int(np.nansum(np.abs(d2) > 1e-6))} of {int(np.isfinite(d2).sum())} trials "
      "(the scripts use the first column)")''')
open('make_nb.py','w').write(s)
EOF
python make_nb.py && cat > runtest.py <<'EOF'
import json,pickle,sys,time,os
os.chdir('entries/gao-2018'); sys.path.insert(0,'.')
import matplotlib; matplotlib.use('Agg')
nb=json.load(open('reproduce_gao_2018.ipynb'))
codes=[''.join(c['source']) for c in nb['cells'] if c['cell_type']=='code']
start=int(sys.argv[1]) if len(sys.argv)>1 else 0
stop=int(sys.argv[2]) if len(sys.argv)>2 else len(codes)
ns={}
if start==0:
    src=codes[0]
    a=src.index('crcns, meta = {}, {}'); b=src.index('sessions = G.build_sessions')
    src=src[:a]+"import pickle\ncrcns, meta = pickle.load(open('/tmp/claude-1001/crcns_new.pkl','rb'))\nfor v in crcns.values(): v.setdefault('trial_descr',['','','','',''])\n"+src[b:]
    exec(src,ns); start=1
    pickle.dump({k:ns[k] for k in ['dandi','crcns','meta']},open('/tmp/claude-1001/ns0.pkl','wb'))
else:
    exec(codes[0].split('started = time.time()')[0],ns); ns['started']=time.time()
    d=pickle.load(open('/tmp/claude-1001/ns0.pkl','rb')); ns.update(d); ns['sessions']=ns['G'].build_sessions(ns['crcns'],ns['meta'])
for i in range(start,stop):
    t0=time.time(); print(f'===== cell {i}'); exec(codes[i],ns); print(f'----- {time.time()-t0:.0f}s')
EOF
timeout 3000 python runtest.py 0 4 2>&1 | tail -120
```

```
written 68
DANDI:000007 version 0.220126.1903: 54 NWB files streamed in 36 s
===== cell 1
Sessions and units by group and mouse:
                       sessions  units  pyramidal  FS  unclassified         cn cn_side  alm_ml
group      mouse                                                                              
dentate    ANM314756          2     26         25   0             1    Dentate   right    -1.5
           BAYLORNL12         5    244        224  13             7    Dentate   right    -1.5
           BAYLORNL14         6    308        281  20             7    Dentate   right    -1.5
fastigial  ANM314746          3     63         59   3             1  Fastigial   right    -1.5
           ANM314757          2     38         34   3             1  Fastigial    left     1.5
           ANM314758          4     62         58   1             3  Fastigial   right    -1.5
           ANM314760          3     72         64   8             0  Fastigial   right    -1.5
           BAYLORCD6          4    196        183   8             5  Fastigial   right    -1.5
           BAYLORNL15         5    177        156  17             4  Fastigial   right    -1.5
inhibition BAYLORCD12         5    160        147   6             7  Fastigial    left    -1.5
           BAYLORCD13         5    100         95   4             1  Fastigial    left    -1.5
           BAYLORCD14         5    195        177   9             9  Fastigial    left    -1.5
           BAYLORCD8          5    282        263  10             9  Fastigial   right    -1.5

[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; sed -i 's/ct = pd.concat(\[s.trials.assign(group=s.group) for s in sessions\])/ct = pd.concat([s.trials.assign(group=s.group) for s in sessions], ignore_index=True)/' make_nb.py && python make_nb.py && timeout 3000 python runtest.py 1 6 2>&1 | tail -150
```

```
written 68
BAYLORNL15_20170603  fastigial           454             432           432      432             0.005                      0                   0        True           True          0.0050           51           51                 51              49
BAYLORNL15_20170604  fastigial           319             295           295      295             0.005                      0                   0        True           True          0.0050           27           27                 27              27
BAYLORNL15_20170605  fastigial           264             232           232      232             0.005                      0                   0        True           True          0.0050           32           32                 32              31
BAYLORNL15_20170607  fastigial           303             280           280      280             0.005                      0                   0        True           True          0.0050           33           33                 33              32

All units have identical spike times in both deposits: True
Units whose cell type differs (DANDI 'unknown' where CRCNS has none counts as same): 52
DANDI trials = CRCNS good trials with a photostimulation code, except in sessions:
           session  good_with_code  dandi_trials  eligible_not_in_dandi
ANM314746_20151022             284           258                     26
ANM314757_20151021             302            34                    268
DANDI trial codes and outcomes equal CRCNS for every matched trial: True

DANDI trial column descriptions: {'cue_time': 'float # in secs, the end of the delay period, relative to the start of the trials', 'pole_in_time': 'float # in secs, the start of the sample period for each trial, relative to the trial start'}
DANDI cue_time minus start_time, first trials (s): [3.17, 3.17, 4.529]
CRCNS CueTime has two columns in 40 sessions; on good trials the second minus the first: median 0.000 s, nonzero in 0 of 12584 trials (the scripts use the fir
[... 135 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; python - <<'EOF'
s=open('make_nb.py').read()
s=s.replace('''                        lit=round(float(tc.laser_on.notna().mean()), 2),''','''                        lit=round(float(tc.laser_on.notna().mean()), 2),
                        at_named_epoch=round(float((np.abs(on) < 0.02).mean()), 2),''')
s=s.replace('for shift_name, shift in [("true", 0.0), ("shifted by -2 s", -2.0)]:','for shift_name, shift in [("true", 0.0), ("events taken 0.6 s later", 0.6)]:')
s=s.replace('''With the true alignment the fraction of selective neurons is near the 5% false-positive rate
before sample onset and rises after it; with the trial events shifted by 2 s the rise moves
accordingly (printed).''','''With the true alignment the fraction of selective neurons is near the 5% false-positive rate
before sample onset and rises in the first window after it; with the trial events taken 0.6 s
later the rise moves 0.6 s earlier relative to the shifted events (printed).''')
open('make_nb.py','w').write(s)
EOF
python make_nb.py && timeout 3000 python runtest.py 1 20 2>&1 | grep -v "^ *BAYLOR\|^ *ANM" | tail -150
```

```
written 68
sample epoch (code 3), pooled, for reference: {'ctrl': 0.8733, 'stim': 0.879, 'change': 0.0057, 'p': 0.4122, 'p_drop': 0.588, 'n_ctrl': 3410, 'n_stim': 529, 'n_mice': 3, 'n_sessions': 13}
----- 2s
===== cell 11
paper rule, code 5 (CN inhibition delay 0.5 s):
     mouse  contra_change  contra_p  ipsi_change  ipsi_p  n_stim  contra_biased  ipsi_biased
  contra-biased mice 0, ipsi-biased mice 2

paper rule, code 6 (CN inhibition delay 1.3 s):
     mouse  contra_change  contra_p  ipsi_change  ipsi_p  n_stim  contra_biased  ipsi_biased
  contra-biased mice 2, ipsi-biased mice 1

files' CN side, code 5 (CN inhibition delay 0.5 s):
     mouse  contra_change  contra_p  ipsi_change  ipsi_p  n_stim  contra_biased  ipsi_biased
  contra-biased mice 1, ipsi-biased mice 1

files' CN side, code 6 (CN inhibition delay 1.3 s):
     mouse  contra_change  contra_p  ipsi_change  ipsi_p  n_stim  contra_biased  ipsi_biased
  contra-biased mice 1, ipsi-biased mice 2

[... 133 more lines not kept]
```

**Agent**

Cells through the latency analysis run. Continuing with the remaining cells.

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; timeout 3000 python runtest.py 1 40 2>&1 | sed -n '/===== cell 20/,$p' | tail -150
```

```
(76 s)
----- 76s
===== cell 22
     group  trials window  tested  modulated  frac_of_tested  frac_of_pyramidal  increase  decrease
inhibition     all   stim     486        228           0.469              0.334       122       106
inhibition     all  delay     486        228           0.469              0.334       122       106
inhibition correct   stim     263        106           0.403              0.155        65        41
inhibition correct  delay     263        106           0.403              0.155        65        41
     group  trials window  label   n  onset_all_ms  boot_mean_ms  boot_sd_ms  no_onset
inhibition     all   stim  start 228          28.0         15.27       12.88       0.0
inhibition     all   stim centre 228          33.0         20.27       12.88       0.0
inhibition     all   stim    end 228          38.0         25.27       12.88       0.0
inhibition     all  delay  start 228          28.0         15.27       12.88       0.0
inhibition     all  delay centre 228          33.0         20.27       12.88       0.0
inhibition     all  delay    end 228          38.0         25.27       12.88       0.0
inhibition correct   stim  start 106          32.0         31.71        8.53       0.0
inhibition correct   stim centre 106          37.0         36.71        8.53       0.0
inhibition correct   stim    end 106          42.0         41.71        8.53       0.0
inhibition correct  delay  start 106          32.0         31.71        8.53       0.0
inhibition correct  delay centre 106          37.0         36.71        8.53       0.0
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; python - <<'EOF'
s=open('make_nb.py').read()
s=s.replace('''agg = cap.groupby("trials").agg(["mean", "sem", "std"]).drop(columns="session", errors="ignore")''','''agg = cap.drop(columns="session").groupby("trials").agg(["mean", "sem", "std"])''')
s=s.replace('''    corr = np.flatnonzero(np.isin(np.arange(X_.shape[1]), np.concatenate([sets["test_R"], sets["test_L"]])))\n''','')
open('make_nb.py','w').write(s)
EOF
python make_nb.py; sed -i 's/^for i in range(start,stop):/if start>1: [exec(codes[j],ns) for j in (5,27)]\nfor i in range(start,stop):/' runtest.py; timeout 3000 python runtest.py 27 40 2>&1 | sed -n '/===== cell 31/,$p'
```

```
written 68
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; timeout 3000 python runtest.py 27 40 2>&1 | tail -40
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/runtest.py", line 18, in <module>
    if start>1: [exec(codes[j],ns) for j in (5,27)]
                 ^^^^^^^^^^^^^^^^^
  File "<string>", line 1, in <module>
NameError: name 'selres' is not defined
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; sed -i 's/for j in (5,27)\]/for j in (5,)]/' runtest.py; timeout 3000 python runtest.py 28 40 2>&1 | tail -40
```

```
fastigial (8 sessions), last 400 ms: control 18.39 [10.05, 27.12], photo-activation 6.09 [0.26, 14.46], control minus stim 12.30 [5.84, 20.91] (67% of control)
fastigial (8 sessions), light offset to go cue: control 17.06 [8.95, 25.15], photo-activation 5.30 [0.27, 12.96], control minus stim 11.76 [5.66, 19.26] (69% of control)
dentate (12 sessions), last 400 ms: control 14.68 [8.25, 21.60], photo-activation 12.62 [6.88, 18.69], control minus stim 2.07 [0.15, 4.18] (14% of control)
dentate (12 sessions), light offset to go cue: control 14.29 [8.49, 20.33], photo-activation 11.65 [6.34, 17.42], control minus stim 2.64 [0.75, 4.65] (18% of control)
----- 2s
===== cell 31
trials            held out  in sample
sel_a       mean      79.9       85.0
            sem        3.6        2.4
            std       16.0       10.8
sel_b       mean      66.3       73.4
            sem        5.0        3.9
            std       22.5       17.5
var_a       mean      56.0       58.9
            sem        4.9        4.6
            std       21.8       20.7
var_b       mean      35.9       38.7
            sem        5.9        5.6
            std       26.4       25.2
var_trial_a mean      50.6       51.7
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd  cat entries/fouke-2025/README.md | head -40; ls executed 2>/dev/null | head -3; grep -n "python\|runtime_minutes" entries/fouke-2025/entry.yaml
```

```
Sat Nov 14 11:30:41 UTC 2026
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
[... 16 more lines not kept]
```

**Agent**

Decided outcomes: 21 tested claims, 24 blocked as data_missing. Writing the summary into the notebook generator, then the entry files.

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; cat > summary.md <<'EOF'
| claim | outcome | main numbers (printed above) |
|---|---|---|
| fig1g-fastigial-activation-early-sample-no-effect | reproduced | contra and ipsi changes -0.031 and +0.012, p 0.37 and 0.37 |
| fig1g-fastigial-activation-delay-errors | reproduced | 0.870 to 0.630, p < 0.0001 (6 mice, 21 sessions) |
| ed10b-fastigial-activation-errors-during-recording | reproduced | same comparison, p < 0.0001 |
| fig1h-fastigial-activation-delay-bias | reproduced | 2 mice contra-biased, 2 ipsi-biased (early delay) |
| fig1g-dentate-activation-little-effect | reproduced | 0.873 to 0.835, p = 0.11 (3 of the 8 mice) |
| fig1k-inhibition-delay-bias | reproduced | 1.3 s photo-inhibition: mice biased both ways under either laterality |
| fig2-alm-selective-fraction | reproduced | 856 of 1084 (0.79) |
| fig2-preparatory-more-in-alm | reproduced (ALM only) | 0.563 of all neurons; CN not deposited |
| fig2-peri-movement-equal | partially reproduced | ALM 0.642; CN not deposited |
| fig2cd-selectivity-emerges-gradually | partially reproduced | ALM holds under reading (a); CN not deposited |
| fig3d-alm-altered-by-cn-inhibition | partially reproduced | 228 of 486 (0.469); latency 15 to 32 ms, not 7.1 |
| fig3e-alm-mean-rate-unchanged | reproduced | 4.03 and 4.21 spikes/s, p = 0.51 |
| fig3e-alm-increase-decrease | reproduced (assumption) | 122 and 106; increase fraction 0.535 |
| fig3f-alm-selectivity-abolished-by-cn-inhibition | partially reproduced | 1.46 to 0.39 spikes/s, interval excludes zero |
| fig4-fastigial-activation-alm-latency | partially reproduced | latency 3.6 ms (one reading); 177 to 190 modulated, not 227 |
| fig4e-fastigial-activation-abolishes-alm-selectivity | reproduced | 328 neurons; 163 of 183 lose selectivity, 6 gain |
| fig4f-fastigial-effect-persists | reproduced | 0.13 of neurons >= 1 s after offset, 0.009 before onset |
| fig4g-dentate-effect-recovers | partially reproduced | latency and count match one reading; late fraction still above baseline |
| fig4i-cd-control-separation | reproduced | 20 sessions; separated from -2.06 s and through the delay |
| fig4i-fastigial-collapses-cd | partially reproduced | fastigial -67%; dentate -14%, interval excludes zero |
| cd-captures-selectivity | reproduced (assumption) | 66.3% and 28.4% under one set of choices |
| ed10d-fastigial-endpoints-no-prediction | not reproduced | slope 0.54 per s.d., p = 0.003 |
| 24 other claims | blocked, data_missing | lesions, behavior-only sessions, CN recordings, licks, VGAT, anatomy |

How the analysis differs from the paper's. Behavior is from the recording sessions, not the
behavior sessions. The data hold 34 of the 39 Fig. 2 sessions and more units than the paper
reports for these mice (1084 pyramidal neurons in the photo-activation sessions against 912;
682 against 454 in the photo-inhibition sessions), so counts are compared with care. Details the
Methods leave open come from the deposited scripts: trial selection, the 1.3 s response window,
the minimum trial counts for photostimulation tests and the coding-direction neuron selection,
which keeps 20 of 34 sessions (the paper: 28 of 39).

What was found about the datasets. The two deposits hold the same 54 sessions with identical
spike times; DANDI lacks 26 and 268 trials in two sessions, rounds trial start times, and
describes event times as relative to the trial start when they are in session time. For the
three photo-inhibition mice CD12, CD13 and CD14 both deposits place the fastigial fiber on the
same side as the recorded ALM, against the paper's and the codes' contralateral design. The laser
traces confirm the stimulation timing in the 2017 and 2018 sessions; in some 2015 sessions they
show a 1.3 s light, varying durations, or no light, and in one 2017 session delay-coded trials lit
at sample onset (laser table). The power channel of the photo-inhibition sessions reads lower
than the powers the Methods state.
EOF
python - <<'EOF'
s=open('/tmp/claude-1001/make_nb.py').read()
s=s.replace('SUMMARY_TABLE', open('/tmp/claude-1001/summary.md').read().replace('\\','\\\\'))
open('/tmp/claude-1001/make_nb.py','w').write(s)
EOF
python make_nb.py
```

```
written 68
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/gao-2018; cat > requirements.in <<'EOF'
fsspec
aiohttp
requests
h5py
remfile
numpy
pandas
scipy
statsmodels
matplotlib
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: gao-2018
type: reproduction
title: A cortico-cerebellar loop for motor planning (Gao et al. 2018)
description: Tests the findings of Gao, Davis, Thomas, Economo, Abrego, Svoboda, De Zeeuw and Li
  (2018) on its two deposits, DANDI:000007 and CRCNS:alm-4, which hold the same 54 ALM recording
  sessions of 13 mice during fastigial or dentate photo-activation and CN photo-inhibition. It
  tests the behavior in those sessions, ALM trial-type selectivity, ALM responses to CN
  photostimulation and the coding direction analysis. The lesion experiments, CN recordings, lick
  times, VGAT-ChR2 experiments and anatomy are not deposited.
license: Apache-2.0
notebooks:
- path: reproduce_gao_2018.ipynb
  title: Reproducing Gao et al. (2018) from DANDI:000007 and CRCNS:alm-4
  runtime_minutes: 25
helpers:
- gao2018.py
related:
- id: dandi:000007/0.220126.1903
  relation: uses_data
- id: crcns:alm-4/unversioned
  relation: uses_data
- id: doi:10.1038/s41586-018-0633-x
  relation: reproduces
EOF
cd  date -u; timeout 600 python tools/entry.py lock entries/gao-2018 2>&1 | tail -5
```

```
Sat Nov 14 11:31:55 UTC 2026
wrote gao-2018/requirements.lock.txt (Python 3.13, with hashes)
```

**Agent calls Bash**

```bash
cd entries/gao-2018; cat > README.md <<'EOF'
# Gao et al. (2018) from DANDI:000007 and CRCNS:alm-4

Tests the findings of [Gao et al. (2018)](https://doi.org/10.1038/s41586-018-0633-x) that can be
tested on its two deposits, [DANDI:000007](https://dandiarchive.org/dandiset/000007/0.220126.1903)
and [CRCNS:alm-4](https://doi.org/10.6080/K0NS0S26). Both hold the same 54 sessions of ALM
recording in 13 mice: 34 during fastigial or dentate photo-activation and 20 during CN
photo-inhibition. The lesion experiments, behavior-only sessions, CN recordings, lick times,
VGAT-ChR2 experiments and anatomy are in neither, so 24 of the 45 claims are blocked.

| Claim | Outcome |
|---|---|
| Behavior in the recording sessions (Fig. 1g, 1h, 1k; Extended Data Fig. 10b), six claims | Reproduced |
| Most ALM pyramidal neurons are selective (Fig. 2) | Reproduced |
| Preparatory activity in 59% of ALM neurons | Reproduced (ALM only) |
| Peri-movement activity, ALM and CN | Partially reproduced (ALM only) |
| Selectivity emerges gradually (Fig. 2c, d) | Partially reproduced (ALM only) |
| CN photo-inhibition alters many ALM neurons, 7.1 ms latency | Partially reproduced |
| Mean ALM rate unchanged by CN photo-inhibition | Reproduced |
| Increase against decrease among modulated ALM neurons | Reproduced, on an assumption |
| CN photo-inhibition abolishes ALM selectivity | Partially reproduced |
| Fastigial photo-activation changes ALM within 4.5 ms | Partially reproduced |
| Fastigial photo-activation abolishes ALM selectivity | Reproduced |
| The fastigial effect persists for more than 1 s | Reproduced |
| Dentate effect recovers quickly | Partially reproduced |
| Control trajectories separate along the coding direction | Reproduced |
| Fastigial, not dentate, photo-activation collapses the trajectories | Partially reproduced |
| The coding direction captures 64.1% of selectivity and 27.0% of variance | Reproduced, on an assumption |
| After fastigial photo-activation the projection no longer predicts licking | Not reproduced |
| Lesions, CN recordings, licking, VGAT-ChR2 and anatomy (24 claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The two deposits have identical spike times; the analysis reads the CRCNS copy, which keeps every
trial and the laser traces, and checks DANDI against it. Method details the paper leaves open are
taken from the analysis scripts deposited with CRCNS:alm-4. The attempt record, with the reasons
and the differences from the paper's method, is
[`attempts/gao-2018-02.yaml`](../../attempts/gao-2018-02.yaml).

- `reproduce_gao_2018.ipynb`: the analysis. It takes about 25 minutes, most of it reading the two
  CRCNS archives (12.8 GB of gzip, read once each as a stream).
- `gao2018.py`: loading both deposits, the trial selection of the deposited scripts, and the
  measures (selectivity, photostimulation tests, latency, hierarchical bootstrap, coding
  direction).
EOF
cd  timeout 600 python tools/entry.py check entries/gao-2018 2>&1 | tail -20
```

```
0 error(s)
```

**Agent**

Check passes. Running the full entry now (expected ~20 to 25 min).

**Agent calls Bash**

```bash
cd  date -u; timeout 5400 python tools/entry.py all entries/gao-2018 2>&1 | tail -30; date -u
```

```
Sat Nov 14 11:32:17 UTC 2026
Installed kernelspec registry-gao-2018 in executed/gao-2018/.venv/share/jupyter/kernels/registry-gao-2018
0 error(s)
pass  reproduce_gao_2018.ipynb  (1010 s)
Sat Nov 14 11:49:18 UTC 2026
```

**Agent**

Ran in 17 min. Reading the executed outputs to confirm the numbers.

**Agent calls Bash**

```bash
cd  ls executed/gao-2018/; python - <<'EOF'
import json
nb=json.load(open('executed/gao-2018/reproduce_gao_2018.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    out=''.join(''.join(o.get('text','')) if o.get('output_type')=='stream' else ''.join(o.get('data',{}).get('text/plain','')) for o in c.get('outputs',[]))
    tags=c['metadata'].get('tags',[])
    if i in (1,): print(i,tags,out[:2000]); continue
    if 'laser' in ''.join(c['source'])[:300] or 'compare_deposits' in ''.join(c['source']): 
        print(i,tags,'\n'.join(l for l in out.splitlines() if not l.strip().startswith(('BAYLOR','ANM')) or 'ANM314746_20151020' in l or 'ANM314756_20151020' in l or 'ANM314757_20151021' in l or 'NL14_20170603' in l or 'CD14_20171028' in l)[:4000]); continue
    print(i,tags,out[-2500:])
EOF
```

```
<persisted-output>
Output too large (35KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/a42792bc-0747-45ec-8290-0b4969ce496e/tool-results/bfx7lfgpa.txt

Preview (first 2KB):
reproduce_gao_2018.ipynb
result.json
1 [] DANDI:000007 version 0.220126.1903: 54 NWB files streamed in 37 s
ALM_recording_DCN_photoactivation/datafiles.tar.gz: 34 sessions, 34 meta files, 389 s
ALM_recording_DCN_photoinhibition/datafiles.tar.gz: 20 sessions, 20 meta files, 286 s
CRCNS:alm-4 (doi:10.6080/K0NS0S26, unversioned): 54 sessions, 712 s so far, peak memory 3.2 GB

3 ['sanity']              1  Fastigial   right    -1.5
           ANM314757          2     38         34   3             1  Fastigial    left     1.5
           ANM314758          4     62         58   1             3  Fastigial   right    -1.5
           ANM314760          3     72         64   8             0  Fastigial   right    -1.5
           BAYLORCD6          4    196        183   8             5  Fastigial   right    -1.5
           BAYLORNL15         5    177        156  17             4  Fastigial   right    -1.5
inhibition BAYLORCD12         5    160        147   6             7  Fastigial    left    -1.5
           BAYLORCD13         5    100         95   4             1  Fastigial    left    -1.5
           BAYLORCD14         5    195        177   9             9  Fastigial    left    -1.5
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/gao-2018/reproduce_gao_2018.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    out=''.join(''.join(o.get('text','')) if o.get('output_type')=='stream' else '' for o in c.get('outputs',[]))
    tags=c['metadata'].get('tags',[])
    src=''.join(c['source'])
    if 'laser' in src[:400]:
        print(i,'\n'.join(l for l in out.splitlines() if ('ANM314746_20151020' in l or 'ANM314756_20151020' in l or 'ANM314757_20151021' in l or 'NL14_20170603' in l or 'at_named' in l or 'Control' in l))); continue
    if i in (3,5): print(i, out[-1500:]); continue
    if 'claim:' in str(tags) and any(k in str(tags) for k in ['fig1','ed10b','fig4f']):
        print(i,tags,out[-1800:])
EOF
```

```
3         
dentate       578        530  33            15
fastigial     608        554  40            14
inhibition    737        682  29            26

Photostimulation codes on good trials, by group:
ptype        -1     0    1    2    3    4    5    6
group                                              
dentate       0  3541    0    0  546  563    0    0
fastigial     0  4331  652  609    0    0    0    0
inhibition  217  4161    0    0    0    0  779  746

Trial outcomes on good trials: {'HitL': 6495, 'HitR': 6487, 'ErrL': 1367, 'ErrR': 1186, 'NoLickR': 316, 'NoLickL': 294}
Photostimulation code descriptions in the files:
  ANM314746_20151020 ['[\'"0"--non-stimulation trials;\'\n \'"1"--  Fastigial (contralateral to recoding); Sample; 500ms (5ms pulses at 20 Hz);\'\n \'"2"--  Fastigial (contralateral to recoding); Delay; 500ms (5ms pulses at 20 Hz);\'\n \'"3"--  Right Dentate (contralateral to recoding); Sample; 500ms (5ms pulses at 20 Hz);\'\n \'"4"--  Right Dentate (contralateral to recoding); Delay; 500ms (5ms pulses at 20 Hz);\'\n \'"NaN and others"--discard (stimulation configuration for other purposes, should not analyze)\']']
  BAYLORCD8_20171018 ['[\'"0"--non-stimulation trials;\'\n \'"5"--  DCN photoinhibition (contralateral to ALM recoding); Delay; 500ms (40 Hz cosine);\'\n \'"6"--  DCN photoinhibition (contralateral to ALM recoding); Delay; 1.3ms (40 Hz cosine);\'\n \'"NaN and others"--discard (stimulation configuration for other purposes, should not analyze)\']']

5 YLORNL15_20170605  fastigial           264             232           232      232             0.005                      0                   0        True           True          0.0050           32           32                 32              31
BAYLORNL15_20170607  fastigial           303             280           280      280             0.005                      0                   0        True           True          0.0050           33           33                 33              32
[... 91 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/gao-2018/reproduce_gao_2018.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    out=''.join(''.join(o.get('text','')) if o.get('output_type')=='stream' else '' for o in c.get('outputs',[]))
    tags=c['metadata'].get('tags',[])
    src=''.join(c['source'])
    if 'Clock check' in src or any(k in str(tags) for k in ['fig2-alm','fig2cd','fig3d','fig3e','fig3f','fig4-fast','fig4e','fig4g-dentate-effect-recovers\']','fig4i','cd-capt','ed10d']) or 'total runtime' in src:
        print(i,tags,out[-1600:])
EOF
```

```
9 ['sanity'] Fraction of photo-activation-session pyramidal neurons selective (t-test p<0.05) in 200 ms windows
starting at the given time from pole in (sample onset), with true and shifted alignment:
      true (n=1068)  events taken 0.6 s later (n=1068)
-1.0          0.050                              0.046
-0.8          0.052                              0.032
-0.6          0.047                              0.051
-0.4          0.046                              0.138
-0.2          0.032                              0.236
-0.0          0.051                              0.245
 0.2          0.138                              0.256
 0.4          0.236                              0.263
 0.6          0.245                              0.279
 0.8          0.256                              0.338
 1.0          0.263                              0.369
 1.2          0.279                              0.356

28 ['claim:fig2-alm-selective-fraction']                     neurons  selective  frac_selective
trials  response_s                                    
all     1.3            1084        802           0.740
        1.5            1084        807           0.744
[... 167 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; python - <<'EOF'
s=open('make_nb.py').read()
old='''The power channel of the photo-inhibition sessions reads lower
than the powers the Methods state.'''
assert old in s
s=s.replace(old,'''The power channel of the photo-inhibition sessions reads 0.6 to 0.7
or 1.7 to 1.9 mW on average while the light is on, which matches neither of the 1.5 and 4.5 mW
the Methods state.''')
old2='''        print(f"{grp} ({len(R_)} sessions), {wn}: control {ma:.2f} [{la:.2f}, {ha:.2f}], photo-activation {mb:.2f} [{lb:.2f}, {hb:.2f}], "
              f"control minus stim {md_:.2f} [{ld:.2f}, {hd:.2f}] ({md_ / ma:.0%} of control)")'''
assert old2 in s
s=s.replace(old2, old2+'''
        if wn == "last 400 ms":
            print("   per session (control, photo-activation):",
                  "; ".join(f"{r['session']} {x:.1f}, {y:.1f}" for r, x, y in zip(R_, a, b)))''')
old3='''              f"unpaired p = {stats.ttest_ind(dd.rate_ctrl, dd.rate_stim).pvalue:.3f}")'''
assert old3 in s
s=s.replace(old3, old3+'''
d = mod[("inhibition", "all")]
print("\\nBy mouse, all tested neurons, all trials (control, inhibition, spikes/s):")
print(d.groupby("mouse")[["rate_ctrl", "rate_stim"]].mean().round(2).to_string())''')
open('make_nb.py','w').write(s)
EOF
python make_nb.py; cd  date -u; timeout 5400 python tools/entry.py all entries/gao-2018 2>&1 | tail -5; date -u
```

```
written 68
Sat Nov 14 11:49:52 UTC 2026
Traceback (most recent call last):
  File "tools/entry.py", line 59, in <module>
    import yaml
ModuleNotFoundError: No module named 'yaml'
Sat Nov 14 11:49:52 UTC 2026
```

**Agent calls Bash**

```bash
cd  date -u; timeout 5400 python tools/entry.py all entries/gao-2018 2>&1 | tail -5; date -u
```

```
Sat Nov 14 11:49:55 UTC 2026
Installed kernelspec registry-gao-2018 in executed/gao-2018/.venv/share/jupyter/kernels/registry-gao-2018
0 error(s)
pass  reproduce_gao_2018.ipynb  (1102 s)
Sat Nov 14 12:08:28 UTC 2026
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/gao-2018/reproduce_gao_2018.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    out=''.join(''.join(o.get('text','')) if o.get('output_type')=='stream' else '' for o in c.get('outputs',[]))
    tags=c['metadata'].get('tags',[])
    if any(k in str(tags) for k in ['fig3e-alm-mean','fig4i-fastigial','fig2-alm','fig4e']) or i==67: print(i,out[-1500:])
    for o in c.get('outputs',[]):
        if o.get('output_type')=='error': print('ERROR',i)
EOF
```

```
28                     neurons  selective  frac_selective
trials  response_s                                    
all     1.3            1084        802           0.740
        1.5            1084        807           0.744
correct 1.3            1084        856           0.790
        1.5            1084        864           0.797

Reading (a, a) by mouse:
            size  sum   mean
mouse                       
ANM314746     59   50  0.847
ANM314756     25   20  0.800
ANM314757     34   24  0.706
ANM314758     58   49  0.845
ANM314760     64   55  0.859
BAYLORCD6    183  116  0.634
BAYLORNL12   224  186  0.830
BAYLORNL14   281  241  0.858
BAYLORNL15   156  115  0.737

[... 34 more lines not kept]
```

**Agent**

Final run passed (18 min, 3.2 GB peak). Writing the attempt record now.

**Agent calls Bash**

```bash
cd  grep -l "crcns" attempts/*.yaml | head -3; f=$(grep -l "archive: crcns" attempts/*.yaml | tail -1); sed -n 1,40p $f; grep -n "protocol:" attempts/*.yaml | tail -3; grep -rn "harness" attempts/fujimoto-2026-02.yaml | head
```

```
attempts/asari-2009-01.yaml
attempts/brinke-2017-01.yaml
attempts/bruno-2017-01.yaml
schema_version: 3
id: zandvakili-2015-01
datasets:
- archive: crcns
  id: v1v2-1
  version: unversioned
  doi: 10.6080/K0B27SHN
  relation: primary
paper: doi:10.1016/j.neuron.2015.07.026
date: 2026-11-12
entry: zandvakili-2015
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
[... 29 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "attempts/gao-2018-02.yaml",
 "content": "schema_version: 3\nid: gao-2018-02\ndatasets:\n- archive: dandi\n  id: \"000007\"\n  version: 0.220126.1903\n  doi: 10.48324/dandi.000007/0.220126.1903\n  relation: primary\n- archive: crcns\n  id: alm-4\n  version: unversioned\n  doi: 10.6080/K0NS0S26\n  relation: primary\npaper: doi:10.1038/s41586-018-0633-x\ndate: 2026-11-14\nentry: gao-2018\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-15\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/43586299319\noutcomes:\n- claim: fig1d-fastigial-lesion-contra-choice\n  outcome: blocked\n  blocked_by: data_missing\n  notes: >-\n    Neither dataset holds the lesion experiments. DANDI:000007 holds 54 ALM recording sessions and\n    CRCNS:alm-4 the same 54 sessions (34 during CN photo-activation, 20 during CN photo-inhibition);\n    the CRCNS descriptor lists no lesion data, and no other deposit is named by the paper.\n- claim: fig1e-fastigial-lesion-slow-initiation\n  outcome: blocked\n  blocked_by: data_missing\n  notes: >-\n    No lesion sessions and no lick times in either dataset (the trial tables give the outcome and an\n    early-lick flag only; the CRCNS time series hold the laser command and power, not the lick\n    contacts).\n- claim: fig1d-dentate-lesion-no-effect\n  outcome: blocked\n  blocked_by: data_missing\n  notes: No lesion sessions in either dataset; see fig1d-fastigial-lesion-contra-choice.\n- claim: fig1g-fastigial-activation-early-sample-no-effect\n  outcome: reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:fig1g-fastigial-activation-early-sample-no-effect\n  notes: >-\n    Early sample photo-activation (code 1) against control in the 6 fastigial mice: contralateral\n    trials 0.857 to 0.826 (change -0.031, one-sided bootstrap p = 0.36), ipsilateral 0.887 to 0.899\n    (+0.012, p = 0.37); pooled 0.870 to 0.861 (p = 0.42). Both p > 0.05.\n  deviations:\n  - >-\n    Tested on the behavior of the ALM recording sessions (21 sessions, 6 mice), where\n    photostimulation was on about a third of trials; the paper's Fig. 1g uses behavior sessions,\n    which are not deposited. Supplemental Table 1 gives the same 6 mice for both.\n  - >-\n    Trials with GoodTrials = 0 or a NaN photostimulation code are left out, as in the deposited\n    analysis scripts; the Methods do not mention them.\n- claim: fig1g-fastigial-activation-delay-errors\n  outcome: reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:fig1g-fastigial-activation-delay-errors\n  notes: >-\n    Early delay photo-activation (code 2, light for 0.455 s from delay onset, ending 0.845 s before\n    the go cue by the laser traces) lowers pooled performance from 0.870 to 0.630 (change -0.240; no\n    resample of 10,000 without a drop, p < 0.0001). Every mouse drops, by 0.083 to 0.450.\n  deviations:\n  - Behavior from the ALM recording sessions, not the behavior sessions of Fig. 1g.\n- claim: fig1h-fastigial-activation-delay-bias\n  outcome: reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:fig1h-fastigial-activation-delay-bias\n  notes: >-\n    Reading (a), early delay photo-activation. ANM314760 and BAYLORNL15 drop on contralateral trials\n    (by 0.726 and 0.719, p < 0.0005) with no ipsilateral drop; ANM314746 and ANM314757 drop on\n    ipsilateral trials (by 0.391, p = 0.003, and 0.221, p = 0.03), more than on contralateral\n    trials. ANM314758 and BAYLORCD6 show neither significantly. Reading (b), the 1.255 s whole-delay\n    experiment, is not in the datasets.\n  deviations:\n  - Recording-session behavior; reading (b) not testable.\n  - >-\n    Contra and ipsi are relative to the manipulated fastigial nucleus; for these mice the files'\n    fiber side and the recorded ALM are on opposite sides, as the paper states.\n- claim: fig1h-fastigial-activation-response-contra-bias\n  outcome: blocked\n  blocked_by: data_missing\n  notes: >-\n    The recording sessions have photo-activation only in the sample and delay epochs (codes 1 to\n    4); response-epoch photo-activation was in behavior sessions, which are not deposited.\n- claim: fig1i-fastigial-activation-licking-unaffected\n  outcome: blocked\n  blocked_by: data_missing\n  notes: >-\n    Lick times are in neither dataset, so lick rate within bouts and bout duration cannot be\n    measured, and there is no response-epoch photo-activation. Only an early-lick flag per trial is\n    deposited.\n- claim: fig1g-dentate-activation-little-effect\n  outcome: reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:fig1g-dentate-activation-little-effect\n  notes: >-\n    Reading (a), early delay dentate photo-activation (code 4) in the 3 recorded dentate mice:\n    pooled performance 0.873 to 0.835 (change -0.039, one-sided bootstrap p = 0.107, paper p = 0.06).\n    No drop at p < 0.05; contralateral -0.055 (p = 0.09), ipsilateral -0.019 (p = 0.42).\n  deviations:\n  - >-\n    3 of the paper's 8 dentate mice (the recorded ones), from recording sessions; reading (b), the\n    1.255 s photostimulus, is not in the datasets.\n- claim: fig1j-photoinhibition-silences-fastigial\n  outcome: blocked\n  blocked_by: data_missing\n  notes: CN recordings are in neither dataset; both hold ALM units only.\n- claim: fig1k-inhibition-early-sample-no-effect\n  outcome: blocked\n  blocked_by: data_missing\n  notes: >-\n    The photo-inhibition recording sessions have delay photo-inhibition only (codes 5 and 6); the\n    behavior sessions with sample-epoch photo-inhibition are not deposited.\n- claim: fig1k-inhibition-late-sample-delay-errors\n  outcome: blocked\n  blocked_by: data_missing\n  notes: >-\n    Late-sample and late-delay photo-inhibition are not in the datasets. The early-delay 0.5 s\n    photo-inhibition of the recording sessions (code 5) lowers pooled performance from 0.848 to\n    0.706 (one-sided bootstrap p = 0.014, 4 mice), shown in the fig1k-inhibition-delay-bias section.\n- claim: fig1k-inhibition-delay-bias\n  outcome: reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:fig1k-inhibition-delay-bias\n  notes: >-\n    Reading (b), 1.3 s delay photo-inhibition (code 6): with contra and ipsi from the paper's rule\n    (CN contralateral to the recorded ALM), BAYLORCD12 and BAYLORCD13 drop on contralateral trials\n    (by 0.464, p = 0.001, and 0.385, p = 0.009) and BAYLORCD14 on ipsilateral trials (0.234,\n    p = 0.008); with the files' CN side the labels of CD12, CD13 and CD14 swap, giving 1 contra-\n    and 2 ipsi-biased mice. Both give mice biased each way. Reading (a), 0.5 s early delay (code 5),\n    gives 0 contra- and 2 ipsi-biased mice under the paper's rule, 1 and 1 under the files' side.\n  deviations:\n  - >-\n    The 4 recorded L7-cre x Ai32 mice (CD8, CD12, CD13, CD14) from recording sessions, in place of\n    the 3 (CD12, CD13, CD16) and 7 behavior mice of Extended Data Fig. 2g and 2h; late-delay\n    photo-inhibition is not deposited.\n  - >-\n    The files put the fastigial fiber on the same side as the recorded ALM for CD12, CD13 and CD14,\n    against the paper's contralateral design; both side assignments were run and both reproduce.\n- claim: fig1k-inhibition-response-ipsi-bias\n  outcome: blocked\n  blocked_by: data_missing\n  notes: No response-epoch photo-inhibition in the recording sessions; behavior sessions are not deposited.\n- claim: fig1l-inhibition-execution-unaffected\n  outcome: blocked\n  blocked_by: data_missing\n  notes: >-\n    No lick times, no video or jaw tracking, and no response-epoch photo-inhibition in either\n    dataset.\n- claim: ed10-vgat-fastigial-perturbation-performance\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The VGAT-ChR2-EYFP behavior is in neither dataset (the 13 mice are wild type or L7-cre x Ai32).\n- claim: fig2-alm-selective-fraction\n  outcome: reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:fig2-alm-selective-fraction\n  measured:\n  - 1084\n  - 856\n  - 0.79\n  notes: >-\n    In the 34 photo-activation sessions, 856 of 1084 pyramidal neurons are selective (0.790) with\n    correct trials and a 1.3 s response window, the reading of the deposited Fig. 2 script; 0.797\n    with 1.5 s, 0.740 and 0.744 with correct and error trials. All four readings are within\n    0.82 +- 0.082. By mouse 0.63 to 0.86. On the DANDI trial set (which lacks trials in two sessions)\n    842 of 1084 (0.777). The counts are not judged, as the datasets hold 34 of the 39 sessions.\n  deviations:\n  - >-\n    34 of the 39 sessions (9 of 10 mice); the tenth mouse, excluded from the photo-activation\n    analyses, is not deposited.\n  - >-\n    The response window (1.3 s from the go cue) and the trial set (correct trials) are from the\n    deposited script analysis_compile_all_ALM_data.m; the Methods do not give them. Both readings of\n    each were run.\n- claim: fig2-cn-selective-fraction\n  outcome: blocked\n  blocked_by: data_missing\n  notes: CN recordings are in neither dataset.\n- claim: fig2-preparatory-more-in-alm\n  outcome: reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:fig2-preparatory-more-in-alm\n  measured: 0.563\n  notes: >-\n    ALM only, as the criterion allows when the CN neurons are missing. 610 of 1084 pyramidal\n    neurons (0.563) are selective in the sample or delay epoch with correct trials, 0.538 with\n    correct and error trials; both within 0.59 +- 0.059. As a fraction of selective neurons, 0.71\n    to 0.73. The CN fraction and the chi-square comparison cannot be computed, so the claim's\n    comparison with the CN is untested; measured is the ALM fraction.\n  deviations:\n  - CN half not deposited.\n- claim: fig2-peri-movement-equal\n  outcome: partially_reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:fig2-peri-movement-equal\n  measured: 0.642\n  notes: >-\n    The ALM half holds; 696 of 1084 pyramidal neurons (0.642) are selective in the response epoch\n    with correct trials and a 1.3 s window (0.636 with 1.5 s), within 0.67 +- 0.067; with correct\n    and error trials 0.562 to 0.571, outside. The CN half, and so the equality the claim states,\n    cannot be tested; the outcome records that only part of the claim could be shown.\n  deviations:\n  - CN half not deposited.\n- claim: ed4-lick-modulated-few\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Lick times are in neither dataset, and CN recordings are not deposited.\n- claim: fig2cd-selectivity-emerges-gradually\n  outcome: partially_reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:fig2cd-selectivity-emerges-gradually\n  notes: >-\n    ALM, reading (a), 827 selective neurons: the bootstrap interval excludes zero from 0.13 s\n    after sample onset (117 of 129 sample-epoch points), the mean is 0.65 spikes/s in the sample,\n    1.80 in the delay and 1.91 in the response epoch, and the maximum (2.37) is 0.23 s after the go\n    cue; all three conditions hold. Reading (b), 591 neurons, peaks 0.06 s before the go cue.\n    The CN half of the claim cannot be tested.\n  deviations:\n  - CN half not deposited.\n  - >-\n    Preferred type from 10 correct control trials of each type and neurons with more than 15 trials\n    of each type, from the deposited Fig. 2 script; PSTHs with its 200 ms boxcar, on a 10 ms grid.\n- claim: ed4e-cn-predicts-movement\n  outcome: blocked\n  blocked_by: data_missing\n  notes: CN recordings are in neither dataset.\n- claim: ed4f-preparatory-all-nuclei\n  outcome: blocked\n  blocked_by: data_missing\n  notes: CN recordings are in neither dataset.\n- claim: ed4g-fastigial-contra-late-delay\n  outcome: blocked\n  blocked_by: data_missing\n  notes: CN recordings are in neither dataset.\n- claim: fig3-cn-altered-by-alm-inhibition\n  outcome: blocked\n  blocked_by: data_missing\n  notes: CN recordings during ALM photo-inhibition are in neither dataset.\n- claim: fig3b-cn-net-disinhibition\n  outcome: blocked\n  blocked_by: data_missing\n  notes: CN recordings are in neither dataset; depends on fig3-cn-altered-by-alm-inhibition.\n- claim: fig3c-cn-selectivity-abolished\n  outcome: blocked\n  blocked_by: data_missing\n  notes: CN recordings are in neither dataset.\n- claim: ed6-cn-selectivity-both-alm-hemispheres\n  outcome: blocked\n  blocked_by: data_missing\n  notes: CN recordings are in neither dataset.\n- claim: fig3d-alm-altered-by-cn-inhibition\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:fig3d-alm-altered-by-cn-inhibition\n  measured:\n  - 486\n  - 228\n  - 15.27\n  notes: >-\n    With 1.3 s delay photo-inhibition (19 sessions, 4 mice), 228 of 486 tested pyramidal neurons\n    change their delay rate (0.469; correct trials only, 106 of 263, 0.403). The fraction is within\n    10% of 0.43 and the count of 228 is outside 197 +- 19.7. The latency is 15.3 +- 12.9 ms (bootstrap\n    mean and s.d., bin start, all trials) and 31.7 ms with correct trials; 20 to 42 ms when bins are\n    labelled by centre or end. No reading reaches 7.1 +- 3.8 ms. Many neurons are altered, but\n    the latency does not reproduce. By mouse the modulated fraction is 0.16 (CD12) to 0.55 (CD8).\n  deviations:\n  - >-\n    The files hold 682 pyramidal neurons in the photo-inhibition sessions where the paper reports\n    454, so the count is judged by its fraction (assumed; the criterion uses the fraction when the\n    dataset holds fewer neurons, and here it holds a different, larger set).\n  - >-\n    Neurons tested need at least 8 control trials of each type and more than 3 photo-inhibition\n    trials of each type, and early-lick trials are left out, as the deposited FR script; the\n    Methods give neither.\n  - >-\n    Latency bins are labelled by their start, centre or end, which the paper does not state; all\n    three are shown.\n- claim: fig3e-alm-mean-rate-unchanged\n  outcome: reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:fig3e-alm-mean-rate-unchanged\n  measured:\n  - 4.03\n  - 4.21\n  notes: >-\n    Reading (a), all 486 tested pyramidal neurons, all trials: delay rate 4.03 spikes/s in control\n    and 4.21 with CN photo-inhibition (change +0.18), paired t-test p = 0.51, unpaired p = 0.66; both\n    rates within tolerance and no difference. Reading (b), the 228 modulated neurons: 5.52 and 6.20\n    (p = 0.25 and 0.35). With correct trials only, 3.27 and 3.85 (p = 0.08 and 0.24).\n- claim: fig3e-alm-increase-decrease\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:fig3e-alm-increase-decrease\n  measured:\n  - 122\n  - 106\n  notes: >-\n    Of the 228 modulated neurons, 122 increase and 106 decrease (increase fraction 0.535, within 10%\n    of 0.55); the counts are above 108 +- 10.8 and 89 +- 8.9. With correct trials, 65 and 41\n    (0.613, outside 10%).\n  deviations:\n  - >-\n    Judged by the increase fraction because the files hold more neurons than the paper (682\n    pyramidal against 454), so counts are not comparable; the criterion gives the fraction for a\n    dataset holding fewer neurons, and its use here is an assumption.\n- claim: fig3f-alm-selectivity-abolished-by-cn-inhibition\n  outcome: partially_reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:fig3f-alm-selectivity-abolished-by-cn-inhibition\n  notes: >-\n    336 selective neurons tested on more than 3 trials in all conditions. Whole delay: control 1.46\n    spikes/s [1.14, 1.82], photo-inhibition 0.39 [0.19, 0.60]; last 500 ms: 1.52 [1.12, 1.96] and\n    0.27 [0.02, 0.53]. Selectivity falls by 73% to 82% but its interval excludes zero in both windows,\n    so it is not abolished by the criterion. With 5 screening trials (the deposited script) 0.37\n    [0.17, 0.57] and 0.32 [0.06, 0.56].\n  deviations:\n  - >-\n    The criterion's 10 screening trials per type are from the Methods; the deposited script uses 5,\n    shown as a variant.\n- claim: fig4bc-fastigial-targets-alm-thalamus\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The anatomy (injections and sections) is in neither dataset.\n- claim: ed8-snr-sc-converge\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The anatomy is in neither dataset.\n- claim: fig4-fastigial-activation-alm-latency\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:fig4-fastigial-activation-alm-latency\n  measured:\n  - 3.64\n  - 177\n  notes: >-\n    Neurons modulated in the 0.455 s photostimulation window, all trials, bins labelled by start:\n    latency 3.6 +- 2.9 ms, within 4.5 +- 2.6. Labelled by centre it is 8.6 ms, outside; with the whole\n    delay as window 7.8 ms. The count is 177 of 445 tested (whole-delay window 187, correct trials\n    67 to 68, without the script's minimum trial counts 190 of 538), against 227 +- 22.7 from the\n    same 6 mice; the count does not reproduce. The fraction of tested neurons (0.40 to 0.42) is\n    close to 227 of the paper's unknown denominator. By mouse 11 to 66 modulated neurons.\n  deviations:\n  - >-\n    The latency match rests on labelling each 10 ms bin by its start (assumed); the paper does not\n    say how a bin is placed in time, and the centre and end labels give 8.6 and 13.6 ms.\n  - Minimum trial counts and early-lick exclusion from the deposited FR script.\n- claim: fig4e-fastigial-activation-abolishes-alm-selectivity\n  outcome: reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:fig4e-fastigial-activation-abolishes-alm-selectivity\n  measured: 328\n  notes: >-\n    328 selective neurons tested on more than 3 trials in all conditions, as Extended Data Fig. 9c.\n    From light offset to the go cue the population selectivity is 2.20 spikes/s [1.67, 2.79] in\n    control and 0.66 [0.31, 1.03] with photo-activation (difference 1.55 [1.01, 2.09]); 163 of the\n    183 neurons selective in control lose significance (0.89) and 6 gain it. In the last 500 ms,\n    157 of 174 lose it and 9 gain it. With 5 screening trials the difference is 1.20 [0.66, 1.78].\n  deviations:\n  - The per-neuron test (E2 t-test on the window) is the claims file's choice; the paper gives none.\n- claim: fig4f-fastigial-effect-persists\n  outcome: reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:fig4f-fastigial-effect-persists\n  notes: >-\n    In 400 ms bins starting 1 s or more after light offset (all in the response epoch), a mean 0.1345\n    of 445 neurons change their rate at p < 0.01, against 1% (binomial p = 3e-47) and against 0.0092\n    in the bins before light onset (z = 7.27, p = 2e-13). The fraction peaks at 0.42 during the\n    light and stays at 0.12 to 0.14 up to 2 s after the go cue.\n- claim: fig4g-dentate-effect-recovers\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:fig4g-dentate-effect-recovers\n  measured:\n  - 8.3\n  - 172\n  notes: >-\n    Stimulation window, all trials, bins labelled by centre: latency 8.3 +- 3.1 ms and 172 modulated\n    neurons of 517, both within tolerance (by start 3.3 ms, just below 3.3 to 13.3; whole-delay window\n    146 neurons). After the light the fraction of significant neurons falls from 0.33 to 0.0476 in the\n    bins 1 s or more after offset, lower than fastigial (0.1345, one-sided p = 1e-6), but still above\n    1% (binomial p = 2e-10) and above the 0.0147 before light onset (p = 0.0013). The recovery test\n    fails under both comparisons, so the claim holds in part.\n  deviations:\n  - >-\n    The latency match rests on labelling bins by their centre (assumed); no single labelling\n    matches both the fastigial and the dentate latency.\n- claim: fig4i-cd-control-separation\n  outcome: reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:fig4i-cd-control-separation\n  notes: >-\n    20 sessions (8 to 46 neurons). The separation of independent control trials along the cd\n    excludes zero from 2.06 s before the go cue, in 75 of 130 sample-epoch windows, and in all 131\n    windows centred in the delay (smallest lower bound 5.98). Before sample onset it is -0.13.\n  deviations:\n  - >-\n    20 of 34 sessions pass the neuron rule of the deposited CD script (stable from the 50th trial\n    to the 50th before the end); the paper used 28 of 39. The rule is the script's; the Methods give\n    only \"> 5 neurons for > 5 trials per condition\".\n  - >-\n    The cd uses correct trials of a random half of control trials; the paper does not say how the\n    trials are split (the claims file names this split as a standard choice).\n- claim: fig4i-fastigial-collapses-cd\n  outcome: partially_reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:fig4i-fastigial-collapses-cd\n  notes: >-\n    Fastigial (8 sessions), last 400 ms: control 18.39 [10.05, 27.12], photo-activation 6.09 [0.26,\n    14.46], difference 12.30 [5.84, 20.91], 67% of control; reading (b) holds and reading (a) does\n    not (interval above zero). Dentate (12 sessions): 14.68 against 12.62, difference 2.07 [0.15,\n    4.18], 14% of control; the interval of the difference excludes zero, so the dentate condition of\n    the criterion fails. From light offset to the go cue the same: fastigial -69%, dentate -18%\n    [0.75, 4.65]. The contrast the claim states is present, but the dentate effect is not nil.\n  deviations:\n  - 8 fastigial and 12 dentate sessions pass the session rule (see fig4i-cd-control-separation).\n- claim: cd-captures-selectivity\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:cd-captures-selectivity\n  measured:\n  - 66.3\n  - 28.4\n  notes: >-\n    Reading (b), squared ratios, with the selectivity measured on held-out correct control trials\n    and the variance on single trials: 66.3% (s.e.m. 5.0) and 28.4% (4.3), within 64.1 +- 3.4 and\n    27.0 +- 4.2. On the cd-estimating trials, 73.4% and 29.4%; with the variance of condition means,\n    35.9% to 38.7%; reading (a), plain ratios, 79.9% to 85.0% and 50.6% to 58.9%. Only the stated\n    combination matches both values.\n  deviations:\n  - >-\n    Assumed that the captured fractions are ratios of squared RMS (variance fractions), that\n    selectivity is measured on trials independent of those that estimated the cd, and that activity\n    variance is over single trials; the Methods state none of these, and the outcome depends on\n    each.\n- claim: ed10b-fastigial-activation-errors-during-recording\n  outcome: reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:ed10b-fastigial-activation-errors-during-recording\n  notes: >-\n    6 mice, 21 sessions: pooled performance 0.870 in control and 0.630 with early delay\n    photo-activation; no resample of 10,000 without a drop (p < 0.0001 < 0.001).\n- claim: ed10c-alm-inhibition-endpoints-predict\n  outcome: blocked\n  blocked_by: data_missing\n  notes: >-\n    Neither dataset has ALM photo-inhibition trials (the codes are 0 to 6, CN photostimulation\n    only), and no VGAT-ChR2 mouse is deposited.\n- claim: ed10d-fastigial-endpoints-no-prediction\n  outcome: not_reproduced\n  notebook: reproduce_gao_2018.ipynb\n  output: claim:ed10d-fastigial-endpoints-no-prediction\n  notes: >-\n    181 fastigial photo-activation trials with a lick in 8 sessions. The projection on the cd in the\n    last 400 ms of the delay still predicts the lick direction (logistic slope 0.54 per s.d. [0.19,\n    0.90], p = 0.003); the probability of licking right is 0.43, 0.49, 0.47 and 0.73 by projection\n    quartile. On control trials the slope is 1.85 [1.55, 2.15] (0.16 to 0.92 by quartile). The\n    prediction is weaker after photo-activation but not absent.\n  deviations:\n  - The projection is not converted to a distance to endpoints; the criterion fits lick direction on the projection itself.\n  - 8 fastigial sessions pass the session rule (see fig4i-cd-control-separation).\n- claim: ed10ef-alm-drives-licking-after-fastigial\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The VGAT-ChR2-EYFP experiments are in neither dataset.\ninputs: []\nfindings:\n- kind: data_missing\n  statement: >-\n    Both datasets hold only the ALM recordings during CN photo-activation (34 sessions, 9 mice)\n    and CN photo-inhibition (20 sessions, 4 mice). The lesion experiments, the behavior-only\n    sessions (including response-epoch and 1.3 s photostimulation), the 878 CN units, lick times,\n    video, the VGAT-ChR2-EYFP experiments, the anatomy, and the tenth mouse of the Fig. 2 ALM\n    recordings are not deposited; 24 of the paper's 45 claims in the claims file cannot be tested.\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n- kind: data_missing\n  statement: >-\n    DANDI:000007 lacks trials that CRCNS:alm-4 holds with GoodTrials = 1 and a valid\n    photostimulation code; ANM314746 2015-10-22 has 258 of 284 (the last 26 missing) and ANM314757\n    2015-10-21 has 34 of 302 (trials 48 to 315 missing). In the other 52 sessions DANDI holds exactly\n    those trials, with the same codes and outcomes, and every unit's spike times are identical.\n  datasets:\n  - \"000007\"\n- kind: metadata_error\n  statement: >-\n    In DANDI:000007 the trial columns cue_time and pole_in_time (and pole_out_time) are described\n    as relative to the trial start, but hold session times; trial start times are rounded (they\n    differ from CRCNS:alm-4 by up to 0.05 s).\n  datasets:\n  - \"000007\"\n- kind: metadata_error\n  statement: >-\n    For the photo-inhibition mice BAYLORCD12, BAYLORCD13 and BAYLORCD14 both datasets give the\n    photostimulation site as the left fastigial nucleus and the ALM recording at ML -1.5 mm (left),\n    on the same side, while the paper, the CRCNS descriptor and the trial code descriptions say the\n    CN was manipulated contralateral to the recorded ALM; Supplemental Table 1 lists BAYLORCD14 as\n    recorded in right ALM. Which side was manipulated cannot be told from the files.\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n- kind: other\n  about: data\n  statement: >-\n    The laser power traces of CRCNS:alm-4 disagree with the trial codes in some sessions. In\n    ANM314746 2015-10-20 codes 1 and 2 (described as 500 ms) have 1.3 s of light; in ANM314756\n    2015-10-20 the light lasts a median 0.83 and 0.78 s and starts at the named epoch in 90% and 78%\n    of trials; ANM314757 2015-10-21 shows almost no light on its stimulation trials (peak 0.17 mW,\n    3% to 5% at the named epoch); in BAYLORNL14 2017-06-03 only 54% of code 3 and 39% of code 4\n    trials are lit at the named epoch, the others at the other epoch. Elsewhere the light starts\n    within 2 ms of the named epoch and lasts 0.455 s (photo-activation) or 0.494 and 1.295 s\n    (codes 5 and 6), and no control trial is lit.\n  datasets:\n  - crcns-alm-4\n- kind: other\n  about: data\n  statement: >-\n    The laser_power channel of the photo-inhibition sessions reads 0.6 to 0.7 or 1.7 to 1.9 mW on\n    average while the light is on (peaks 1.45 and 3.8 to 4.1), which matches neither of the 1.5 and\n    4.5 mW of the Methods and the descriptor; its calibration is not documented.\n  datasets:\n  - crcns-alm-4\n- kind: selection_undocumented\n  about: paper\n  statement: >-\n    The datasets hold more ALM units than the paper reports for the same mice; 1186 units (1084\n    pyramidal) in the 9 photo-activation mice, where the paper reports 912 pyramidal neurons, and\n    737 units (682 pyramidal) in the 4 photo-inhibition mice, where it reports 490 units (454\n    pyramidal) over 19 sessions. Which units, and for the photo-inhibition mice which of the 20\n    sessions, entered the paper's analyses is not stated.\n- kind: metadata_insufficient\n  statement: >-\n    In 40 sessions of CRCNS:alm-4 the trial property CueTime has two columns; the second equals the\n    first on every good trial, and neither the descriptor nor the property's description says what\n    it is.\n  datasets:\n  - crcns-alm-4\n- kind: code_mismatch\n  statement: >-\n    The analysis scripts deposited with CRCNS:alm-4 differ from the Methods in places. The\n    photostimulation selectivity scripts fix each neuron's preferred trial type from 5 trials of\n    each type, where the Methods say 10 for ALM; the coding direction script averages cd_t over\n    windows starting from 3.0 s to 0.4 s before the go cue (pre-sample, sample and delay), where the\n    Methods say the delay epoch; the selectivity test uses correct trials in the Fig. 2 script and\n    correct and error trials in the photostimulation scripts.\n- kind: methods_unavailable\n  statement: >-\n    For the response latencies (4.5, 8.3 and 7.1 ms), how is a 10 ms bin placed in time (start,\n    centre or end) and which window decides that a neuron is significantly modulated? Labelling by\n    start gives 3.6 ms for fastigial and 3.3 ms for dentate photo-activation, by centre 8.6 and 8.3\n    ms, so no single choice here matches both reported values; for CN photo-inhibition every choice\n    gives 15 ms or more.\n- kind: methods_unavailable\n  statement: >-\n    For the fractions captured by the coding direction (64.1% of selectivity, 27.0% of variance),\n    are they ratios of RMS or of squared RMS, is selectivity measured on the trials that estimated\n    the cd or on independent ones, and is activity variance over single trials or condition means?\n    Only squared ratios on independent trials with single-trial variance give both values here (66.3%\n    and 28.4%); other combinations give 73% to 85% and 36% to 59%.\n- kind: methods_unavailable\n  statement: >-\n    Which neurons were tested for photostimulation effects (the minimum numbers of control and\n    photostimulation trials) and which sessions entered the coding direction analysis? With the\n    deposited scripts' rules 177 to 190 ALM neurons are modulated by fastigial photo-activation\n    (paper 227) and 20 of 34 sessions enter the coding direction analysis (paper 28 of 39).\n"
}
```

```
File created successfully at: attempts/gao-2018-02.yaml (file state is current in your context — no need to Read it back)
```

**Agent**

Checking two numbers in the executed notebook before validating the record.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/gao-2018/reproduce_gao_2018.ipynb'))
for c in nb['cells']:
    if 'claim:fig1k-inhibition-delay-bias' in str(c['metadata'].get('tags')):
        out=''.join(''.join(o.get('text','')) for o in c['outputs'] if o.get('output_type')=='stream'); print(out[:1500])
EOF
```

```
paper rule, code 5 (CN inhibition delay 0.5 s):
     mouse  contra_change  contra_p  ipsi_change  ipsi_p  n_stim  contra_biased  ipsi_biased
BAYLORCD12        -0.1630    0.0841       0.0889  0.8784      61          False        False
BAYLORCD13        -0.1129    0.1108       0.0415  0.6742      71          False        False
BAYLORCD14         0.0173    0.6226      -0.2761  0.0004     227          False         True
 BAYLORCD8        -0.0565    0.2580      -0.3590  0.0000     249          False         True
  contra-biased mice 0, ipsi-biased mice 2

paper rule, code 6 (CN inhibition delay 1.3 s):
     mouse  contra_change  contra_p  ipsi_change  ipsi_p  n_stim  contra_biased  ipsi_biased
BAYLORCD12        -0.4641    0.0015       0.0746  0.8204      65           True        False
BAYLORCD13        -0.3846    0.0091       0.0595  0.6990      84           True        False
BAYLORCD14         0.0103    0.5994      -0.2343  0.0083     221          False         True
 BAYLORCD8        -0.1385    0.0651      -0.3242  0.0980     154          False        False
  contra-biased mice 2, ipsi-biased mice 1

files' CN side, code 5 (CN inhibition delay 0.5 s):
     mouse  contra_change  contra_p  ipsi_change  ipsi_p  n_stim  contra_biased  ipsi_biased
BAYLORCD12         0.0889    0.8775      -0.1630  0.0843      61          False        False
BAYLORCD13         0.0415    0.6754      -0.1129  0.1079      71          False        False
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='attempts/gao-2018-02.yaml'
s=open(p).read()
reps=[("(by 0.464, p = 0.001, and 0.385, p = 0.009)","(by 0.464, p = 0.002, and 0.385, p = 0.009)"),
("(by 0.726 and 0.719, p < 0.0005)","(by 0.726 and 0.719, p < 0.0001)"),
("cue_time and pole_in_time (and pole_out_time) are described","cue_time and pole_in_time are described")]
for a,b in reps:
    assert a in s,a; s=s.replace(a,b)
open(p,'w').write(s)
import yaml
c=yaml.safe_load(open('claims/gao-2018.yaml')); a=yaml.safe_load(open(p))
ids=[x['id'] for x in c['claims']]; got=[o['claim'] for o in a['outcomes']]
print(len(ids),len(got),set(ids)-set(got),set(got)-set(ids))
import collections; print(collections.Counter(o['outcome'] for o in a['outcomes']))
EOF
python tools/entry.py check entries/gao-2018 2>&1 | tail -15
```

```
46 46 set() set()
Counter({'blocked': 24, 'reproduced': 14, 'partially_reproduced': 7, 'not_reproduced': 1})
0 error(s)
```

**Agent**

The claims file has 46 claims, not 45. Fixing that count in the README and the record.

**Agent calls Bash**

```bash
cd  sed -i 's/so 24 of the 45 claims are blocked/so 24 of the 46 claims are blocked/' entries/gao-2018/README.md; sed -i "s/24 of the paper's 45 claims in the claims file cannot be tested/24 of the 46 claims in the claims file cannot be tested/" attempts/gao-2018-02.yaml; grep -n "45 claims\|46 claims" entries/gao-2018/README.md attempts/gao-2018-02.yaml; date -u; timeout 5400 python tools/entry.py all entries/gao-2018 2>&1 | tail -4; date -u
```

```
entries/gao-2018/README.md:8:VGAT-ChR2 experiments and anatomy are in neither, so 24 of the 46 claims are blocked.
attempts/gao-2018-02.yaml:488:    recordings are not deposited; 24 of the 46 claims in the claims file cannot be tested.
Sat Nov 14 12:10:51 UTC 2026
Installed kernelspec registry-gao-2018 in executed/gao-2018/.venv/share/jupyter/kernels/registry-gao-2018
0 error(s)
pass  reproduce_gao_2018.ipynb  (1211 s)
Sat Nov 14 12:31:12 UTC 2026
```

**Agent**

Re-ran in 20 min. Spot-checking that seeded outputs are unchanged, then building the handover.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/gao-2018/reproduce_gao_2018.ipynb'))
for c in nb['cells']:
    t=str(c['metadata'].get('tags'))
    out=''.join(''.join(o.get('text','')) for o in c.get('outputs',[]) if o.get('output_type')=='stream')
    if any(o.get('output_type')=='error' for o in c.get('outputs',[])): print('ERROR')
    for k in ['fig3e-alm-mean','cd-captures','ed10d','fig4e','fig1h-fastigial-activation-delay-bias']:
        if k in t: print(k, out.splitlines()[0][:200] if k!='cd-captures' else out[:400])
EOF
python tools/entry.py handover entries/gao-2018 2>&1 | tail -5; ls executed/gao-2018/handover
```

```
fig1h-fastigial-activation-delay-bias      mouse  contra_ctrl  contra_stim  contra_change  contra_p  ipsi_ctrl  ipsi_stim  ipsi_change  ipsi_p  contra_biased  ipsi_biased
fig3e-alm-mean trials all, (a) all tested: n=486, control 4.03, inhibition 4.21 spikes/s, change +0.18; paired p = 0.513, unpaired p = 0.658
fig4e     group  screen                 window  neurons  control  control_lo  control_hi  stim  stim_lo  stim_hi  diff  diff_lo  diff_hi
cd-captures trials            held out  in sample
sel_a       mean      79.9       85.0
            sem        3.6        2.4
            std       16.0       10.8
sel_b       mean      66.3       73.4
            sem        5.0        3.9
            std       22.5       17.5
var_a       mean      56.0       58.9
            sem        4.9        4.6
            std       21.8       20.7
var_b       mean    
ed10d fastigial photo-activation: trials 181, slope 0.54 [0.19, 0.90] per s.d., p = 0.0028; P(lick right) by projection quartile [0.43, 0.49, 0.47, 0.73]
wrote executed/gao-2018/handover
gao-2018.yaml
gao2018.py
reproduce_gao_2018.ipynb
```

**Agent calls Bash**

```bash
cd  ls -la entries/gao-2018; python tools/entry.py check entries/gao-2018 2>&1 | tail -2; date -u
```

```
total 292
drwxr-xr-x   4 runner runner   4096 Nov 14 12:10 .
drwxr-xr-x 293 runner runner  12288 Nov 14 11:12 ..
drwxr-xr-x   3 runner runner   4096 Nov 14 11:17 .claude
-rw-r--r--   1 runner runner   3001 Nov 14 12:10 README.md
drwxr-xr-x   2 runner runner   4096 Nov 14 11:32 __pycache__
-rw-r--r--   1 runner runner   1030 Nov 14 11:31 entry.yaml
-rw-r--r--   1 runner runner  30767 Nov 14 11:17 gao2018.py
-rw-r--r--   1 runner runner  76424 Nov 14 11:49 reproduce_gao_2018.ipynb
-rw-r--r--   1 runner runner     79 Nov 14 11:31 requirements.in
-rw-r--r--   1 runner runner 149001 Nov 14 11:31 requirements.lock.txt
0 error(s)
Sat Nov 14 12:31:47 UTC 2026
```

**Agent**

Stray `__pycache__` and `.claude` directories are in the entry; checking them before removing.

**Agent calls Bash**

```bash
cd entries/gao-2018; find .claude __pycache__ -type f | head;
```

```
__pycache__/gao2018.cpython-313.pyc
__pycache__/gao2018.cpython-312.pyc
```

**Agent calls Bash**

```bash
cd entries/gao-2018; find .claude; rm -rf __pycache__; rmdir -p .claude/* 2>/dev/null; rmdir .claude 2>/dev/null; ls -la
```

```
Permission for this tool use was denied. It requires approval, and this session has no approval surface — nobody can answer a permission prompt here — so it was denied automatically. The action was NOT performed; do not claim it succeeded, and do not retry it: this action, and anything else that requires approval, will be denied the same way for the rest of this session. Tell the user what was blocked and why you needed it, then continue with the parts of the task that do not require approval. What required approval: Dangerous rmdir operation detected: 'entries/gao-2018/.claude/*'

This command's removal target cannot be statically resolved to a directory. This requires explicit approval and cannot be auto-allowed by permission rules. Dangerous rmdir operation on statically-unresolvable target: entries/gao-2018/.claude/*
```

**Agent**

I've written the new entry at `entries/gao-2018`, the record at `attempts/gao-2018-02.yaml`, and built the handover in `executed/gao-2018/handover/`. The entry check gives 0 errors and the notebook runs from a clean environment in about 20 minutes. I did not verify my own work, commit or push. I did not come across any earlier attempt's results.

**1. Outcomes (46 claims: 14 reproduced, 7 partially reproduced, 1 not reproduced, 24 blocked)**

| Claim | Outcome |
|---|---|
| fig1g early-sample no effect; fig1g delay errors; ed10b; fig1h delay bias; fig1g dentate little effect; fig1k delay bias | reproduced (all from the behavior in the recording sessions) |
| fig2-alm-selective-fraction (856/1084 = 0.79) | reproduced |
| fig2-preparatory-more-in-alm (ALM only, 0.563) | reproduced (the CN comparison is untested) |
| fig2-peri-movement-equal; fig2cd-selectivity-emerges-gradually | partially reproduced (ALM half holds; CN not deposited) |
| fig3d ALM altered by CN inhibition (fraction 0.469 matches; latency 15 to 32 ms, not 7.1) | partially reproduced, assumed |
| fig3e mean rate unchanged (4.03 vs 4.21 spikes/s, p = 0.51) | reproduced |
| fig3e increase/decrease (fraction 0.535) | reproduced, assumed |
| fig3f selectivity abolished by CN inhibition (falls 73%, but its interval stays above zero) | partially reproduced |
| fig4 fastigial latency (3.6 ms matches; 177 modulated neurons against 227) | partially reproduced, assumed |
| fig4e (n = 328 exactly, as the paper); fig4f persistence | reproduced |
| fig4g dentate recovers (late fraction still above baseline) | partially reproduced, assumed |
| fig4i control separation | reproduced |
| fig4i fastigial collapse (dentate also drops 14%, interval excludes zero) | partially reproduced |
| cd-captures-selectivity (66.3% and 28.4%) | reproduced, assumed |
| ed10d: projection no longer predicts licking (slope still significant, p = 0.003) | not reproduced |
| 24 claims on lesions, CN recordings, licks, behavior-only sessions, VGAT mice, anatomy | blocked, data_missing |

**2. What I found about the datasets**
- **Same recordings in both:** the two datasets hold the same 54 sessions of 13 mice, and every unit's spike times are identical. I analysed the CRCNS copy and checked DANDI against it.
- **DANDI gaps:** DANDI lacks 26 trials in one session and 268 of 302 in another. Its trial start times are rounded, and its event times are described as relative to the trial start when they are in session time.
- **Laterality:** for mice CD12, CD13 and CD14, both datasets put the fastigial fiber on the same side as the recorded ALM. This contradicts the paper's contralateral design. Both side assignments were run; fig1k reproduces either way.
- **Laser traces:**
  - Several 2015 sessions disagree with their trial codes: one has 1.3 s of light instead of 500 ms, one has varying durations, one has almost no light.
  - In one 2017 session, many delay-coded trials are lit at sample onset.
  - The photo-inhibition power values match neither of the 1.5 and 4.5 mW the Methods state.
- **More units than the paper reports:** 1084 pyramidal neurons in the photo-activation mice against the paper's 912, and 682 in the photo-inhibition mice against 454.
- **Analysis code:** CRCNS:alm-4 holds the lab's analysis scripts, which the paper's reporting summary says would be deposited there. The claims file says the paper links no code. I took the method details the Methods leave open from these scripts and cited each one.
- **Assumptions:** latency bins labelled by start (fastigial) or centre (dentate); counts compared by fraction where the files hold more neurons; for the cd fractions, squared ratios on held-out trials with single-trial variance.
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings): how latency bins are placed in time; how the cd fractions are computed; the neuron and session selection.
- **Questions to a reader:** none.

**3. Where the protocol was unclear**
1. When a claim compares ALM with CN and only ALM can be tested, it is unclear whether the outcome is partial or blocked. I followed the criterion where it allows ALM alone, and used partially reproduced elsewhere, explaining why in the notes.
2. Several count criteria fall back to a fraction "where the dataset holds fewer neurons", but here the files hold more. I used the fraction as an assumption.
3. `measured` has no slot for an expected value that cannot be computed (the CN fractions). I recorded the ALM value alone.
4. The CRCNS data are gzip tar archives, which cannot be opened in place as `archives.md` assumes for zips. I read each archive once as a stream and reduced it in memory (12.8 GB, about 12 minutes).
5. Any edit to the entry, even the README, forces a full re-run. I re-ran (20 minutes) after fixing the claim count in the README from 45 to 46.

**4. Runtime and failures**
- The notebook takes 17 to 20 minutes with a peak of 3.2 GB; the whole session ran from 10:40 to 12:32 UTC.
- I could not remove two stray directories from `entries/gao-2018`. The cleanup command needed approval, which this session cannot give, so it was denied and nothing was removed. They are `__pycache__` (compiled helper files) and an empty `.claude` directory the harness created. The entry check passes with them present; they should be deleted before the workflow commits.

## End of run

77 turns, 106 minutes, $9.43 at API prices, result: success.
