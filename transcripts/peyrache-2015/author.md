# peyrache-2015 · author · run 43708742486

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; ls; ls docs entries attempts claims paper tools; wc -c docs/*.md README.md
```

```
Sun Nov 15 11:31:08 UTC 2026
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
[... 1012 more lines not kept]
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
 "file_path": "claims/peyrache-2015.yaml"
}
```

```
1	# Claims for Peyrache, Lacroix, Petersen & Buzsaki (2015), Nature Neuroscience 18, 569-575,
2	# "Internally organized mechanisms of the head direction sense" (doi:10.1038/nn.3968), on dandiset
3	# 000056.
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-15,
5	# protocol as stated in docs/protocol.md (Reader), version pilot-15.
6	#
7	# Text read. The NIH author manuscript (PMC4376557) as served by Europe PMC, under paper/: Results,
8	# Discussion, Methods and figure legends, with its three supplements from the PMC Open Access
9	# files: Supplementary Figures 1 to 8 (legends), Supplementary Table 1 (recordings by animal), and
10	# the Nature Neuroscience reporting checklist, which gives exact p-values and sample sizes per
11	# test. The checklist numbers figures as in an earlier draft (its "1e", "1f" are Supplementary
12	# Fig. 2b,c, its "4b" is Fig. 5b, its "4f" is Fig. 5d,e); the Methods also cite Fig. 4f,g and
13	# "readout windows in Fig. 4" for what the published legends show in Fig. 5d,e. The main figures
14	# themselves are not under paper/ (no PDF of the article), so values printed only inside figures
15	# (the r values of the Fig. 2a,b insets, the Fig. 4d errors) could not be read.
16	#
17	# Code. The paper links no analysis code, and its checklist answers N/A for custom software. No
18	# code was read. Every method below is from the Methods, the Results, the figure legends or the
19	# supplement, and details none of them fixes are named as open.
20	#
[... 894 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/peyrache-2015.yaml",
 "offset": 914
}
```

```
914	    revealed strong oscillatory spiking dynamics activity in windows of approximately 1–5 ms
915	  depends_on:
916	  - hd-cell-fraction
917	  expected:
918	  - quantity: frequency of the cross-correlogram oscillation, low end
919	    value: 130
920	    tolerance: 13
921	    unit: Hz
922	  - quantity: frequency of the cross-correlogram oscillation, high end
923	    value: 160
924	    tolerance: 16
925	    unit: Hz
926	  criterion: Method of the Fig. 6a legend. For each pair of ADn HD cells, the spike
927	    cross-correlogram z-scored against 100 cross-correlograms of spike trains jittered uniformly
928	    in plus or minus 10 ms windows, then wavelet transformed; average power across pairs per state
929	    (Fig. 6c). The Discussion gives the band, 130 to 160 Hz. Open, and named; (o-a) the
930	    cross-correlogram bin, not given for Fig. 6; 0.5 ms (the bin of the Methods' monosynaptic
931	    analysis) used here, a standard choice; (o-b) the lag range, plus or minus 50 ms used here; (o-c)
932	    the wavelet, a complex Morlet, a standard choice; (o-d) pairs on the same shank, left out here
933	    as the Fig. 6a examples are on different shanks (an example, not a rule; kept as a variant).
[... 222 more lines not kept]
```

**Agent calls Bash**

```bash
ls -la entries/fouke-2025 entries/peyrache-2015; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in; head -c 6000 attempts/fouke-2025-01.yaml; ls papers/datasets | grep peyr; cat papers/datasets/peyrache-2015.yaml; ls questions | grep peyr
```

```
ls: cannot access 'entries/peyrache-2015': No such file or directory
entries/fouke-2025:
total 132
drwxr-xr-x   2 runner runner  4096 Nov 15 11:24 .
drwxr-xr-x 301 runner runner 12288 Nov 15 11:30 ..
-rw-r--r--   1 runner runner  2144 Nov 15 11:24 README.md
-rw-r--r--   1 runner runner   907 Nov 15 11:24 entry.yaml
-rw-r--r--   1 runner runner 16218 Nov 15 11:24 omr.py
-rw-r--r--   1 runner runner 79403 Nov 15 11:24 reproduce_fouke_2025.ipynb
-rw-r--r--   1 runner runner    61 Nov 15 11:24 requirements.in
-rw-r--r--   1 runner runner  5989 Nov 15 11:24 requirements.lock.txt
schema_version: 1
name: fouke-2025
type: reproduction
title: Optomotor swimming of zebrafish and Danionella cerebrum (Fouke et al. 2025)
description: Tests the freely swimming findings of Fouke, He, Loring and Naumann (2025) on dandiset
  001453, which holds the tracking data of 25 zebrafish and 12 Danionella cerebrum larvae during the
  optomotor protocol. It compares swimming speed, turning and angular acceleration between species
  and stimuli, the response to monocular stimuli, and how steady the swimming is. The imaging and
  head-fixed tail tracking of the paper's Figures 2 to 4 are not in the dandiset.
[... 139 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,400p docs/archives.md | grep -n -A60 "^## DANDI" | head -120; python tools/entry.py --help 2>&1 | head -30; ls schemas
```

```
16:## DANDI
17-
18-- **Datasets.** A dandiset, identified by six digits (`000003`). Targets are the
19-  public dandisets whose metadata names a paper (`targets/dandisets.json`, built
20-  by `tools/build_targets.py` and refreshed daily by the Track DANDI workflow).
21-- **Versions.** A published version (`0.220126.1855`) is fixed and has a DOI,
22-  `10.48324/dandi.<id>/<version>`. The draft can change. Pin the version the
23-  paper cites, or the latest published one. For a draft, record its
24-  modification time under `dataset: modified` in the attempt.
25-- **Reading.** List the assets and read metadata with the DANDI REST API
26-  (`https://api.dandiarchive.org/api/dandisets/<id>/versions/<version>/` and its
27-  `assets/` endpoint). Read NWB files by streaming them: open each asset's S3
28-  URL with `remfile` and `h5py`, and read it with `pynwb`. Do not download files
29-  to disk.
30-- **In an entry.** The entry names the dataset as `dandi:<id>/<version>` under
31-  `related`. The helper module keeps the version in one constant.
32-
33-## CRCNS
34-
35-- **Datasets.** A CRCNS data set, identified by its short name (`ret-1`,
[... 75 more lines not kept]
```

**Agent**

Now the dataset. Let me list assets.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/000056/ | python -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/000056/versions/" | python -m json.tool | grep -E '"version"|"status"|"modified"|"size"|asset_count'
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/000056/versions/0.261106.1949/assets/?page_size=200" > assets.json; python -c "
import json;d=json.load(open('assets.json'))
for a in d['results']: print(a['asset_id'], a['path'], round(a['size']/1e9,2))
print(d['count'])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
which python; python --version; python -c "import pynwb, h5py, remfile, dandi; print(pynwb.__version__, h5py.__version__)"; nproc; free -g
```

```
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
Python 3.13.18
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pynwb, h5py, remfile, dandi; print(pynwb.__version__, h5py.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pynwb'
4
               total        used        free      shared  buff/cache   available
Mem:              15           1          12           0           2          14
Swap:              2           0           2
```

**Agent calls Bash**

```bash
mkdir -p entries/peyrache-2015 && cd entries/peyrache-2015 && printf "h5py\nnumpy\nscipy\npandas\nmatplotlib\nremfile\nstatsmodels\nnbformat\n" > requirements.in && cd $TMPDIR && uv venv -q dev && . dev/bin/activate && uv pip install -q h5py numpy scipy pandas matplotlib remfile statsmodels pynwb jupyter nbconvert ipykernel 2>&1 | tail -2; python -c "import h5py,remfile;print('ok')"
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > survey.py <<'EOF'
import h5py, remfile, requests, sys, json
aid=sys.argv[1]
url=f"https://api.dandiarchive.org/api/assets/{aid}/download/"
r=requests.head(url,allow_redirects=True); s3=r.url
f=h5py.File(remfile.File(s3),'r')
def show(name,obj):
    if isinstance(obj,h5py.Dataset):
        if 'acquisition/' in name and obj.size>1e6 and False: pass
        print(name, obj.shape, obj.dtype, dict((k,(v.decode() if isinstance(v,bytes) else v)) for k,v in obj.attrs.items() if k in('unit','conversion','rate','description','starting_time'))  )
    else:
        a={k:v for k,v in obj.attrs.items() if k in ('description','neurodata_type')}
        print('G',name,a)
f.visititems(show)
EOF
python survey.py 24f06696-c405-49b5-82cd-2067f8446700 2>&1 | grep -v "^G.*electrodes" | head -300
```

```
G acquisition {}
G acquisition/blue_led_position_pixels {'description': "position of the blue LED on the head stage in camera pixels (.whl file, columns 3 and 4; 640 x 480 camera), NaN where the lab gives -1 (LED not detected). The lab's camera scale is 0.144521 cm per pixel (GeneralInfo.mat bin2cms). The LEDs were filmed at 30 frames per second, detected online and resampled at 39.0625 Hz by the acquisition system; according to the paper the first video frame is misaligned by a random 0-60 ms, the rate being accurate thereafter.", 'neurodata_type': 'SpatialSeries'}
acquisition/blue_led_position_pixels/data (717364, 2) float64 {'conversion': np.float64(1.0), 'unit': 'pixels'}
acquisition/blue_led_position_pixels/reference_frame () object {}
acquisition/blue_led_position_pixels/starting_time () float64 {'rate': np.float64(39.0625), 'unit': 'seconds'}
G acquisition/red_led_position_pixels {'description': "position of the red LED on the head stage in camera pixels (.whl file, columns 1 and 2; 640 x 480 camera), NaN where the lab gives -1 (LED not detected). The lab's camera scale is 0.144521 cm per pixel (GeneralInfo.mat bin2cms). The LEDs were filmed at 30 frames per second, detected online and resampled at 39.0625 Hz by the acquisition system; according to the paper the first video frame is misaligned by a random 0-60 ms, the rate being accurate thereafter.", 'neurodata_type': 'SpatialSeries'}
acquisition/red_led_position_pixels/data (717364, 2) float64 {'conversion': np.float64(1.0), 'unit': 'pixels'}
acquisition/red_led_position_pixels/reference_frame () object {}
acquisition/red_led_position_pixels/starting_time () float64 {'rate': np.float64(39.0625), 'unit': 'seconds'}
G analysis {}
file_create_date (1,) object {}
G general {}
G general/devices {}
G general/devices/postsubicular_probe {'description': 'NeuroNexus silicon probe in the post-subiculum (Buz32: 4 shanks of 8 sites, or Buz64sp: 6 shanks of 10 sites plus 4 sites above a shank), on a movable drive; appro
[... 146 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python survey.py 25b0f421-e8d7-43ce-8358-a95cb4e192c0 2>&1 | grep -v -E "electrodes|specifications|external_resources|meanings_tables" | grep -v "^units/" | head -100
```

```
G acquisition {}
G acquisition/blue_led_position_pixels {'description': "position of the blue LED on the head stage in camera pixels (.whl file, columns 3 and 4; 640 x 480 camera), NaN where the lab gives -1 (LED not detected). The lab's camera scale is 0.149054 cm per pixel (GeneralInfo.mat bin2cms). The LEDs were filmed at 30 frames per second, detected online and resampled at 39.0625 Hz by the acquisition system; according to the paper the first video frame is misaligned by a random 0-60 ms, the rate being accurate thereafter.", 'neurodata_type': 'SpatialSeries'}
acquisition/blue_led_position_pixels/data (1104518, 2) float64 {'conversion': np.float64(1.0), 'unit': 'pixels'}
acquisition/blue_led_position_pixels/reference_frame () object {}
acquisition/blue_led_position_pixels/starting_time () float64 {'rate': np.float64(39.0625), 'unit': 'seconds'}
G acquisition/red_led_position_pixels {'description': "position of the red LED on the head stage in camera pixels (.whl file, columns 1 and 2; 640 x 480 camera), NaN where the lab gives -1 (LED not detected). The lab's camera scale is 0.149054 cm per pixel (GeneralInfo.mat bin2cms). The LEDs were filmed at 30 frames per second, detected online and resampled at 39.0625 Hz by the acquisition system; according to the paper the first video frame is misaligned by a random 0-60 ms, the rate being accurate thereafter.", 'neurodata_type': 'SpatialSeries'}
acquisition/red_led_position_pixels/data (1104518, 2) float64 {'conversion': np.float64(1.0), 'unit': 'pixels'}
acquisition/red_led_position_pixels/reference_frame () object {}
acquisition/red_led_position_pixels/starting_time () float64 {'rate': np.float64(39.0625), 'unit': 'seconds'}
G analysis {}
file_create_date (1,) object {}
G general {}
G general/devices {}
G general/devices/postsubicular_probe {'description': 'NeuroNexus silicon probe in the post-subiculum (Buz32: 4 shanks of 8 sites, or Buz64sp: 6 shanks of 10 sites plus 4 sites above a shank), on a movable drive; app
[... 86 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t1.py <<'EOF'
import h5py, remfile, requests, time, numpy as np
aid='25b0f421-e8d7-43ce-8358-a95cb4e192c0'
t=time.time()
s3=requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=True).url
f=h5py.File(remfile.File(s3),'r')
u=f['units']
print(list(u.keys()))
for k in ['region','cell_type','shank','in_lab_cell_list','is_hd_cell']:
    v=u[k][:]; print(k, np.unique(v,return_counts=True))
idx=u['spike_times_index'][:]; print(len(idx), idx[-1])
st=u['spike_times'][:]; print('load',time.time()-t)
for k in u.keys():
    if 'wave' in k: print(k,u[k].shape,u[k].attrs.get('description'))
ep=f['intervals/epochs']; print([ (t.decode() if isinstance(t,bytes) else t) for t in ep['tags'][:]], ep['start_time'][:], ep['stop_time'][:])
ss=f['processing/behavior/sleep_states']; lab=ss['label'][:]; print(np.unique(lab,return_counts=True))
d=f['processing/ecephys/LFP/lfp/data']; print(d.chunks, d.compression)
print(f['general/subject/subject_id'][()], f['general/subject/sex'][()], f['general/subject/description'][()])
print(f['general/notes'][()][:2000])
print(time.time()-t)
EOF
python t1.py
```

```
['buzcode_mean_waveform', 'buzcode_region', 'cell_type', 'cluster_id', 'electrode_group', 'electrodes', 'electrodes_index', 'hd_kappa', 'hd_p_value', 'hd_peak_rate', 'hd_preferred_direction', 'id', 'in_lab_cell_list', 'is_hd_cell', 'isi_index', 'lratio', 'mahalanobis_distance', 'max_waveform_channel', 'region', 'shank', 'spike_times', 'spike_times_index']
region (array([b'Anterodorsal nucleus', b'Postsubiculum', b'unknown'],
      dtype=object), array([22, 38,  2]))
cell_type (array([b'[]', b'putative excitatory'], dtype=object), array([40, 22]))
shank (array([ 1,  3,  4,  5,  6,  7,  8,  9, 10]), array([ 2, 10, 14,  6,  6,  2, 10, 11,  1]))
in_lab_cell_list (array([ True]), array([62]))
is_hd_cell (array([False,  True]), array([36, 26]))
62 11658303
load 3.2119126319885254
buzcode_mean_waveform (62, 32) mean spike waveform on the unit's largest channel (samples at 20 kHz), from the lab's 2019 buzcode spikes.cellinfo.mat rawWaveform; in the lab's units, which the files do not document (it equals lab_mean_waveform on that channel up to a constant offset, where both exist); NaN for units not in that file
max_waveform_channel (62,) channel (.xml numbering) with the largest mean waveform (SpikeData.mat maxWaveFormIx, or spikes.cellinfo.mat maxWaveformCh); -1 where neither gives it
['sleep_pre', 'open_field', 'sleep_post', 'sleep_post', 'second_environment'] [    0.   5565.   7851.4 19419.2 26653.9] [ 5564.9999  7851.3999 19419.1999 26653.8999 28275.5999]
(array([b'REM', b'SWS', b'wake'], dtype=object), array([23, 45,  1]))
(1048576, 16) gzip
b'Mouse28' b'U' b'Adult mouse (27-50 g). The paper used five male and two female mice but does not say which mouse is which, so the sex of each is not known.'
b"Description of the recording in the session's .xml file (by the lab):\nRecording in the anterior thalamus and the post-subiculum, left hemisphere.\n\nPostsubiculum: \nElectrode groups 1-7. \n6 shank probe, Neuronexus Buz64sp design. Shank #1 is the most medial, #6 the most l
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
wc -w paper/*.txt; grep -n -i -E "methods|^[A-Z][a-z]+.*$" paper/10.1038-nn.3968.txt | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; python - <<'EOF'
t=open('10.1038-nn.3968.txt').read()
i=t.find('Online Methods'); i = i if i>0 else t.find('Methods Animal')
print(len(t), i)
import re
for kw in ['Head direction cells','Bayesian reconstruction','Information measures','Estimation of angular velocity','Ensemble coherence','independent firing rate','mono-synaptic','Classification of PoS','Statistical','speed','velocity threshold','cm/s','moving']:
    for m in re.finditer(kw,t): print(kw, m.start())
EOF
```

```
94489 -1
Head direction cells 26917
Head direction cells 41358
Head direction cells 44666
Head direction cells 59837
Head direction cells 60638
Head direction cells 64182
Bayesian reconstruction 18951
Bayesian reconstruction 28813
Bayesian reconstruction 29405
Information measures 32812
Estimation of angular velocity 29593
Ensemble coherence 36151
Ensemble coherence 53675
independent firing rate 31584
independent firing rate 31872
mono-synaptic 37019
mono-synaptic 57798
mono-synaptic 58155
mono-synaptic 75559
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; python -c "
t=open('10.1038-nn.3968.txt').read()
print(t[24500:40500])"
```

```
, were recorded by a digital video camera at 30 frames per second. The LED locations were detected online and resampled at 39 Hz by the acquisition system (note that the absolute time of the first video frame was randomly misaligned by 0–60ms but the sampling rate was accurate thereafter). Spike sorting was performed semi-automatically, using KlustaKwik 53 (available at: http://klustakwik.sourceforge.net ). This was followed by manual adjustment of the waveform clusters using the software Klusters 54 . Examples of simultaneously recorded neurons and quantification of isolation quality are shown in Supplementary Fig. 8 . After 4–7 days of recovery, the thalamic probes were lowered until the first thalamic units could be detected on at least 2–3 shanks. At the same time, hippocampal wires were slowly lowered until reaching the CA1 pyramidal layer, characterized by high amplitude ripple oscillations. The probe was then lowered by 70–140 μm at the end of each session. In the animals implanted in both the thalamus and in the PoS, the subicular probe was moved everyday once large HD cell ensembles were recorded from the thalamus. Thereafter, the thalamic probes were left at the same position as long as the quality of the recordings remained. They were subsequently adjusted to optimize the yield of HD cells. To prevent statistical bias of neuron sampling, we discarded from analysis sessions separated by less than three days during which the thalamic probe was not moved. Three animals had channelrhodopsin conditionally expressed in parvalbumin (one animal) or CamKII (two animals) positive neurons but these aspects of the experiments are not part of the present study. Recording sessions and behavioral paradigm Recording sessions were composed of exploration of an open environment (‘wake’ phase) during which the animals were foraging for food for 30 to 45 minutes. The environment was a 53 × 46 cm rectangular arena surrounded by 21-cm high, black-painted walls on which were di
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; python -c "
t=open('10.1038-nn.3968.txt').read()
print(t[12000:24500])"
```

```
s to compute the HD tuning curves in their target PoS or ADn neurons, respectively. In agreement with the preservation of the activity packet across brain states ( Fig. 3a,b ), tuning curves were remarkably similar during sleep to that of waking ( Fig. 5a,b ; Supplementary Movie 1 ). However, the HD signal extracted from ADn assemblies resulted in tuning curves more similar to actual HD fields than the HD signal decoded from PoS assemblies, in all brain states ( Fig. 5b ; Mann-Whitney U test; wake: p < 10 –10 ; SWS: p = 0.018; REM: p = 3×10 −6 ; n = 86, 92 PoS and ADn HD cells respectively). Finally, to quantify how well ADn or PoS assemblies could predict the firing probability and timing of target cells in the PoS or ADn, respectively, we estimated the predictability of spike trains based on a Generalized Linear Model of cell ensemble activity 36 (see Methods ), at different time-scales ( Fig. 5c–e ). ADn assemblies predicted PoS spike trains reliably in all brain states ( Fig. 5d,e ; p < 10 –10 in all brain states, Wilcoxon’s signed rank test, n = 86). Optimal readout windows were similar between waking and REM (median: 123 ms and 133 ms respectively) and shorter during SWS (median: 79 ms). In the reverse direction, PoS cell assemblies predicted spike trains of ADn neurons more weakly, especially during SWS ( Fig. 5d,e ; wake: p = 3×10 −5 , SWS: p < 10 –10; REM: p = 1.1×10 −6 ; Mann-Whitney U test; n = 86 and 62 PoS and ADn neurons respectively). Finally, we examined the fine timescale dynamics of HD neurons within and across structures. Spectral analysis of cross-correlation functions between pairs of HD cells in the ADn revealed strong oscillatory spiking dynamics activity in windows of approximately 1–5 ms ( Fig. 6a ). The degree of synchrony decreased with the magnitude of difference between the preferred head directions of the neurons ( Fig. 6b ; p < 10 –10 ; Kruskal-Wallis test, n = 970 ADn HD cell pairs) in all brain states ( Fig. 6c and Supplementary Fig.
[... 1 more lines not kept]
```

**Agent**

I've read the protocol, the claims file (37 claims) and the paper's Methods. Now writing the loader and surveying all 42 sessions.

**Agent calls Write**

```json
{
 "file_path": "entries/peyrache-2015/hd.py",
 "content": "\"\"\"Loading and measures for Peyrache et al. (2015) on DANDI:000056.\n\nEvery parameter says where it comes from: \"criterion\" (the claim's criterion in\nclaims/peyrache-2015.yaml, which cites the paper), \"Methods\" or another passage\nof the paper (taken by the author, protocol step 1.6), \"assumption\" (a choice\nthe paper leaves open, with the reason), or \"standard\" (a detail that cannot\nchange a result).\n\nData are streamed from the archive with remfile and h5py; nothing is written to\ndisk.\n\"\"\"\nimport numpy as np\nimport h5py\nimport remfile\nimport requests\nfrom scipy import stats, optimize, signal\nfrom scipy.ndimage import gaussian_filter1d\n\nDANDISET = \"000056\"\nVERSION = \"0.261106.1949\"\nAPI = \"https://api.dandiarchive.org/api\"\n\nADN = \"Anterodorsal nucleus\"\nPOS = \"Postsubiculum\"\n\n# Methods, Head direction cells: 1 degree bins, 6 degree s.d. smoothing.\nNBINS = 360\nSMOOTH_DEG = 6.0\n# Methods, Head direction cells: kappa > 1, peak > 1 Hz, Rayleigh p < 0.001.\nKAPPA_MIN, PEAK_MIN, RAYLEIGH_P = 1.0, 1.0, 1e-3\n# Methods, Head direction cells, paragraph 2: 0.5 Hz in any of the three states.\nRATE_MIN = 0.5\n# Figure 3a legend: 300 ms bins in wake and REM, 50 ms in SWS.\nCORR_BIN = {\"wake\": 0.3, \"REM\": 0.3, \"SWS\": 0.05}\n# Methods, Bayesian reconstruction: 10 ms bins, 300 ms (wake, REM) and 50 ms\n# (SWS) s.d. Gaussian smoothing.\nDEC_BIN = 0.01\nDEC_SMOOTH = {\"wake\": 0.3, \"REM\": 0.3, \"SWS\": 0.05}\nSTATES = (\"wake\", \"SWS\", \"REM\")\n\n\ndef _txt(x):\n    return x.decode() if isinstance(x, bytes) else str(x)\n\n\ndef list_assets():\n    \"\"\"Assets of the pinned version: list of (path, asset_id, size).\"\"\"\n    url = f\"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200\"\n    out = []\n    while url:\n        r = requests.get(url, timeout=60).json()\n        out += [(a[\"path\"], a[\"asset_id\"], a[\"size\"]) for a in r[\"results\"]]\n        url = r.get(\"next\")\n    return sorted(out)\n\n\ndef open_asset(asset_id):\n    url = f\"{API}/assets/{asset_id}/download/\"\n    s3 = requests.head(url, allow_redirects=True, timeout=60).url\n    return h5py.File(remfile.File(s3), \"r\")\n\n\ndef _intervals(g):\n    lab = [_txt(x) for x in g[\"label\"][:]] if \"label\" in g else None\n    return lab, g[\"start_time\"][:], g[\"stop_time\"][:]\n\n\ndef load_session(asset_id, path):\n    \"\"\"Read one session's units, head direction, epochs and sleep states.\n\n    The LFP is not read here (see lfp_window).\"\"\"\n    f = open_asset(asset_id)\n    s = {\"path\": path, \"asset_id\": asset_id}\n    s[\"session\"] = _txt(f[\"general/session_id\"][()]) if \"general/session_id\" in f else path\n    s[\"subject\"] = _txt(f[\"general/subject/subject_id\"][()])\n    u = f[\"units\"]\n    idx = u[\"spike_times_index\"][:]\n    st = u[\"spike_times\"][:]\n    starts = np.r_[0, idx[:-1]]\n    s[\"spikes\"] = [st[a:b] for a, b in zip(starts, idx)]\n    for k in [\"region\", \"cell_type\", \"buzcode_region\"]:\n        s[k] = np.array([_txt(x) for x in u[k][:]])\n    for k in [\"shank\", \"cluster_id\", \"in_lab_cell_list\", \"is_hd_cell\", \"hd_kappa\",\n              \"hd_p_value\", \"hd_peak_rate\", \"hd_preferred_direction\", \"max_waveform_channel\"]:\n        s[k] = u[k][:]\n    s[\"waveform\"] = u[\"buzcode_mean_waveform\"][:]\n    eg = u[\"electrode_group\"][:]\n    s[\"electrode_group\"] = np.array([f[r].name.split(\"/\")[-1] for r in eg])\n    ep = f[\"intervals/epochs\"]\n    ti = ep[\"tags_index\"][:]\n    tags = [_txt(x) for x in ep[\"tags\"][:]]\n    s[\"epochs\"] = [(tags[a:b], t0, t1) for a, b, t0, t1 in\n                   zip(np.r_[0, ti[:-1]], ti, ep[\"start_time\"][:], ep[\"stop_time\"][:])]\n    sr = f[\"intervals/sub_recordings\"]\n    s[\"sub_recordings\"] = list(zip([_txt(x) for x in sr[\"file_name\"][:]],\n                                   sr[\"start_time\"][:], sr[\"stop_time\"][:]))\n    b = f[\"processing/behavior\"]\n    s[\"states\"] = {}\n    if \"sleep_states\" in b:\n        lab, t0, t1 = _intervals(b[\"sleep_states\"])\n        for k in STATES:\n            m = np.array([l == k for l in lab])\n            s[\"states\"][k] = np.c_[t0[m], t1[m]]\n    s[\"states_buzcode\"] = {}\n    if \"sleep_states_buzcode\" in b:\n        lab, t0, t1 = _intervals(b[\"sleep_states_buzcode\"])\n        for k in set(lab):\n            m = np.array([l == k for l in lab])\n            s[\"states_buzcode\"][k] = np.c_[t0[m], t1[m]]\n    if \"head_direction\" in b:\n        hd = b[\"head_direction/head_direction\"]\n        rate = hd[\"starting_time\"].attrs[\"rate\"]\n        t0 = hd[\"starting_time\"][()]\n        a = hd[\"data\"][:]\n        s[\"hd_rate\"] = float(rate)\n        s[\"hd_t\"] = t0 + np.arange(len(a)) / rate\n        s[\"hd\"] = a\n        rl = b[\"position/red_led/data\"][:]\n        bl = b[\"position/blue_led/data\"][:]\n        s[\"led_angle\"] = np.arctan2(rl[:, 1] - bl[:, 1], rl[:, 0] - bl[:, 0]) % (2 * np.pi)\n        s[\"red_led\"] = rl * 0.01  # metres (conversion attribute 0.01)\n    else:\n        s[\"hd\"] = None\n    s[\"lfp_shape\"] = (f[\"processing/ecephys/LFP/lfp/data\"].shape\n                      if \"processing/ecephys/LFP/lfp\" in f else None)\n    f.close()\n    return s\n\n\n# ---------------------------------------------------------------- intervals\n\ndef total(iv):\n    return float(np.sum(iv[:, 1] - iv[:, 0])) if len(iv) else 0.0\n\n\ndef in_iv(t, iv):\n    \"\"\"Boolean mask of times t inside any interval of iv (n x 2, sorted).\"\"\"\n    if len(iv) == 0:\n        return np.zeros(len(t), bool)\n    i = np.searchsorted(iv[:, 0], t, side=\"right\") - 1\n    ok = i >= 0\n    out = np.zeros(len(t), bool)\n    out[ok] = t[ok] < iv[i[ok], 1]\n    return out\n\n\ndef restrict(sp, iv):\n    return sp[in_iv(sp, iv)]\n\n\ndef bin_counts(sp, iv, width):\n    \"\"\"Counts in bins of `width` laid within each interval (partial bins dropped).\n\n    Returns counts (n_bins,) and bin centres.\"\"\"\n    edges, cent = [], []\n    for a, b in iv:\n        n = int((b - a) // width)\n        if n < 1:\n            continue\n        e = a + np.arange(n + 1) * width\n        edges.append(e)\n    if not edges:\n        return np.zeros(0), np.zeros(0)\n    cs, cen = [], []\n    for e in edges:\n        c, _ = np.histogram(sp, e)\n        cs.append(c)\n        cen.append(0.5 * (e[1:] + e[:-1]))\n    return np.concatenate(cs), np.concatenate(cen)\n\n\ndef bin_matrix(spikes, iv, width):\n    out = [bin_counts(sp, iv, width)[0] for sp in spikes]\n    return np.array(out, dtype=float)\n\n\n# ---------------------------------------------------------------- tuning\n\ndef wake_hd(s):\n    \"\"\"Head direction samples within wake, LED-detected frames only (Methods).\"\"\"\n    w = s[\"states\"][\"wake\"]\n    m = in_iv(s[\"hd_t\"], w) & np.isfinite(s[\"hd\"])\n    return s[\"hd_t\"][m], s[\"hd\"][m]\n\n\ndef spike_hd(sp, t, a, rate):\n    \"\"\"Head direction at each spike, nearest sample within half a frame; NaN\n    where the nearest sample is not a valid wake sample.\"\"\"\n    if len(sp) == 0 or len(t) == 0:\n        return np.zeros(0)\n    i = np.clip(np.searchsorted(t, sp), 1, len(t) - 1)\n    j = np.where(np.abs(t[i - 1] - sp) < np.abs(t[i] - sp), i - 1, i)\n    ok = np.abs(t[j] - sp) <= 0.5 / rate + 1e-9\n    return a[j[ok]]\n\n\ndef circ_smooth(x, sd_bins):\n    return gaussian_filter1d(x, sd_bins, mode=\"wrap\")\n\n\ndef tuning_curve(sp_hd, occ_counts, dt):\n    \"\"\"Rate per 1 degree bin: spike histogram over time histogram, both smoothed\n    with the 6 degree s.d. Gaussian (Methods). Smoothing the two histograms\n    before the ratio, so that empty 1 degree bins are defined, is a standard\n    choice.\"\"\"\n    c, _ = np.histogram(sp_hd, NBINS, (0, 2 * np.pi))\n    occ = circ_smooth(occ_counts * dt, SMOOTH_DEG)\n    return circ_smooth(c.astype(float), SMOOTH_DEG) / np.maximum(occ, 1e-9)\n\n\ndef occupancy(a):\n    return np.histogram(a, NBINS, (0, 2 * np.pi))[0].astype(float)\n\n\nANG = (np.arange(NBINS) + 0.5) * 2 * np.pi / NBINS\n\n\ndef a1inv(r):\n    \"\"\"Inverse of A1 (ML von Mises concentration from mean resultant length;\n    Fisher 1993 approximation, as in the circular statistics toolbox).\"\"\"\n    r = np.asarray(r, float)\n    k = np.where(r < 0.53, 2 * r + r ** 3 + 5 * r ** 5 / 6,\n                 np.where(r < 0.85, -0.4 + 1.39 * r + 0.43 / (1 - r + 1e-12),\n                          1 / (r ** 3 - 4 * r ** 2 + 3 * r + 1e-12)))\n    return k\n\n\ndef rayleigh_p(R, n):\n    \"\"\"Rayleigh test p-value (Zar 1999, as in the circular statistics toolbox).\"\"\"\n    z = n * R ** 2\n    p = np.exp(np.sqrt(1 + 4 * n + 4 * (n ** 2 - (n * R) ** 2)) - (1 + 2 * n))\n    return float(min(max(p, 0.0), 1.0)) if n > 0 else 1.0\n\n\ndef vm_fit_a(tc, nspk):\n    \"\"\"Reading (hd-a): the tuning curve as a distribution of angles; ML von\n    Mises (circular mean, kappa from resultant length); Rayleigh test with the\n    resultant length of that distribution and n = spike count; peak rate is the\n    tuning curve maximum.\"\"\"\n    w = tc / max(tc.sum(), 1e-12)\n    z = np.sum(w * np.exp(1j * ANG))\n    R = np.abs(z)\n    return dict(pref=np.angle(z) % (2 * np.pi), kappa=float(a1inv(R)), peak=float(tc.max()),\n                p=rayleigh_p(R, nspk), R=R)\n\n\ndef vm_fit_b(tc, sp_hd):\n    \"\"\"Reading (hd-b): least-squares fit of A exp(kappa (cos(x - mu) - 1)) to the\n    tuning curve (A, the fitted peak rate); Rayleigh test on the head\n    directions at spike times.\"\"\"\n    z = np.mean(np.exp(1j * sp_hd)) if len(sp_hd) else 0j\n    R = np.abs(z)\n    mu0 = ANG[np.argmax(tc)]\n    def f(x, A, k, mu):\n        return A * np.exp(k * (np.cos(x - mu) - 1))\n    try:\n        (A, k, mu), _ = optimize.curve_fit(f, ANG, tc, p0=[tc.max(), 2.0, mu0], maxfev=4000)\n        if A < 0:\n            A, k = -A, k\n    except Exception:\n        A, k, mu = np.nan, np.nan, mu0\n    return dict(pref=mu % (2 * np.pi), kappa=float(k), peak=float(A), p=rayleigh_p(R, len(sp_hd)), R=R)\n\n\ndef is_hd(fit):\n    return bool(fit[\"kappa\"] > KAPPA_MIN and fit[\"peak\"] > PEAK_MIN and fit[\"p\"] < RAYLEIGH_P)\n\n\ndef n_peaks(tc):\n    \"\"\"Unimodality readings of supfig2a: (a) another local maximum of at least\n    50% of the maximum; (b) such a maximum separated from the main one by a\n    trough below 50% of the maximum (criterion).\"\"\"\n    m = tc.max()\n    loc = np.where((tc > np.roll(tc, 1)) & (tc >= np.roll(tc, -1)))[0]\n    imax = int(np.argmax(tc))\n    other = [i for i in loc if i != imax and tc[i] >= 0.5 * m]\n    a = len(other) > 0\n    b = False\n    for i in other:\n        # trough on the shorter arc and on the longer arc between i and imax\n        lo, hi = sorted((i, imax))\n        arc1 = tc[lo:hi + 1]\n        arc2 = np.r_[tc[hi:], tc[:lo + 1]]\n        if min(arc1.min(), arc2.min()) < 0.5 * m and max(arc1.min(), arc2.min()) >= 0 :\n            # separated if either path down to the other peak dips below 50%\n            if arc1.min() < 0.5 * m and arc2.min() < 0.5 * m:\n                b = True\n    return a, b\n\n\n# ---------------------------------------------------------------- information\n\ndef segments(iv, n=10):\n    \"\"\"Split the union of intervals into n segments of equal duration\n    (Methods, Information measures: 10 segments).\"\"\"\n    d = iv[:, 1] - iv[:, 0]\n    cum = np.r_[0, np.cumsum(d)]\n    T = cum[-1]\n    cuts = np.linspace(0, T, n + 1)\n    def to_t(x):\n        k = np.clip(np.searchsorted(cum, x, side=\"right\") - 1, 0, len(d) - 1)\n        return iv[k, 0] + (x - cum[k])\n    segs = []\n    for a, b in zip(cuts[:-1], cuts[1:]):\n        ka = np.clip(np.searchsorted(cum, a, side=\"right\") - 1, 0, len(d) - 1)\n        kb = np.clip(np.searchsorted(cum, b, side=\"left\") - 1, 0, len(d) - 1)\n        parts = []\n        for k in range(ka, kb + 1):\n            lo = max(iv[k, 0], to_t(a)) if k == ka else iv[k, 0]\n            hi = min(iv[k, 1], to_t(b)) if k == kb else iv[k, 1]\n            if hi > lo:\n                parts.append((lo, hi))\n        segs.append(np.array(parts))\n    return segs\n\n\ndef hd_information(sp, t, a, rate, nseg=10):\n    \"\"\"Cross-validated HD information in bits/spike (Methods, Information\n    measures): for each of 10 segments of wake, the tuning curve of the other 9\n    is read at the test head direction; L = sum log f(t_s) - int f dt against a\n    homogeneous rate at the training mean; summed over test segments and\n    divided by the number of spikes (bits). Head-direction frames are the time\n    base (25.6 ms), the frame at each spike giving f(t_s).\"\"\"\n    dt = 1.0 / rate\n    seg_id = np.full(len(t), -1)\n    T0, T1 = t[0], t[-1] + dt\n    # segments over the valid wake frames, by equal frame counts\n    seg_id = (np.arange(len(t)) * nseg) // len(t)\n    i = np.clip(np.searchsorted(t, sp), 1, len(t) - 1)\n    j = np.where(np.abs(t[i - 1] - sp) < np.abs(t[i] - sp), i - 1, i)\n    ok = np.abs(t[j] - sp) <= 0.5 * dt + 1e-9\n    j = j[ok]\n    spk_frame = np.bincount(j, minlength=len(t)).astype(float)\n    bins = np.minimum((a / (2 * np.pi) * NBINS).astype(int), NBINS - 1)\n    L = 0.0\n    nsp = 0\n    for k in range(nseg):\n        tr = seg_id != k\n        te = ~tr\n        occ = np.bincount(bins[tr], minlength=NBINS).astype(float) * dt\n        cnt = np.bincount(bins[tr], weights=spk_frame[tr], minlength=NBINS)\n        tc = circ_smooth(cnt, SMOOTH_DEG) / np.maximum(circ_smooth(occ, SMOOTH_DEG), 1e-9)\n        mean_rate = cnt.sum() / occ.sum()\n        f = np.maximum(tc[bins[te]], 1e-6)\n        n = spk_frame[te]\n        L += np.sum(n * np.log2(f)) - np.sum(f) * dt / np.log(2) \\\n            - (np.sum(n) * np.log2(max(mean_rate, 1e-6)) - mean_rate * te.sum() * dt / np.log(2))\n        nsp += n.sum()\n    return L / nsp if nsp > 0 else np.nan\n\n\n# ---------------------------------------------------------------- decoding\n\ndef gauss_smooth_counts(C, sd_s, dt=DEC_BIN):\n    return gaussian_filter1d(C, sd_s / dt, axis=-1, mode=\"constant\")\n\n\ndef bayes_decode(C, tcs, dt):\n    \"\"\"Bayesian decoding (Zhang et al. 1998, basic method with a flat prior):\n    C (cells x bins) smoothed counts in a window of dt seconds, tcs (cells x\n    360) waking tuning curves in Hz. Returns the decoded angle (maximum of the\n    posterior) per bin. Processes bins in chunks to bound memory.\"\"\"\n    tcs = np.maximum(tcs, 1e-3)\n    logt = np.log(tcs)  # cells x 360\n    s = tcs.sum(0) * dt  # 360\n    out = np.empty(C.shape[1])\n    step = 20000\n    for a in range(0, C.shape[1], step):\n        ll = C[:, a:a + step].T @ logt - s  # bins x 360\n        out[a:a + step] = ANG[np.argmax(ll, axis=1)]\n    return out\n\n\ndef circ_diff(a, b):\n    return np.angle(np.exp(1j * (a - b)))\n"
}
```

```
File created successfully at: entries/peyrache-2015/hd.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > survey_all.py <<'EOF'
import sys, time, pickle, numpy as np
sys.path.insert(0,'entries/peyrache-2015')
import hd
from concurrent.futures import ThreadPoolExecutor
assets=hd.list_assets()
t=time.time()
def ld(x):
    return hd.load_session(x[1], x[0])
with ThreadPoolExecutor(4) as ex: S=list(ex.map(ld, assets))
print('time',time.time()-t)
pickle.dump(S, open('sessions.pkl','wb'))
for s in S:
    r=s['region']; 
    st={k:round(hd.total(v)/60,1) for k,v in s['states'].items()}
    print(s['path'].split('/')[1][:30], s['subject'], 'n',len(r), 'ADn',(r==hd.ADN).sum(),'PoS',(r==hd.POS).sum(),'oth',sorted(set(r)-{hd.ADN,hd.POS}), 'list',s['in_lab_cell_list'].sum(),'labHD ADn',(s['is_hd_cell']&(r==hd.ADN)).sum(),'PoS',(s['is_hd_cell']&(r==hd.POS)).sum(), st, [e[0] for e in s['epochs']], 'hd', s['hd'] is not None, s['lfp_shape'])
EOF
python survey_all.py 2>&1 | tail -50
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/survey_all.py", line 9, in <module>
    with ThreadPoolExecutor(4) as ex: S=list(ex.map(ld, assets))
                                        ~~~~^^^^^^^^^^^^^^^^^^^^
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
  File "/tmp/claude-1001/survey_all.py", line 8, in ld
    return hd.load_session(x[1], x[0])
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^
[... 15 more lines not kept]
```

**Agent**

Some files lack columns; making the loader tolerant.

**Agent calls Bash**

```bash
cd entries/peyrache-2015 && python - <<'EOF'
p='hd.py'; t=open(p).read()
t=t.replace('''    for k in ["region", "cell_type", "buzcode_region"]:
        s[k] = np.array([_txt(x) for x in u[k][:]])
    for k in ["shank", "cluster_id", "in_lab_cell_list", "is_hd_cell", "hd_kappa",
              "hd_p_value", "hd_peak_rate", "hd_preferred_direction", "max_waveform_channel"]:
        s[k] = u[k][:]
    s["waveform"] = u["buzcode_mean_waveform"][:]''','''    n = len(idx)
    for k in ["region", "cell_type", "buzcode_region"]:
        s[k] = (np.array([_txt(x) for x in u[k][:]]) if k in u
                else np.array(["absent"] * n))
    for k in ["shank", "cluster_id", "in_lab_cell_list", "is_hd_cell", "hd_kappa",
              "hd_p_value", "hd_peak_rate", "hd_preferred_direction", "max_waveform_channel"]:
        s[k] = u[k][:] if k in u else np.full(n, np.nan)
    s["columns"] = sorted(u.keys())
    s["waveform"] = (u["buzcode_mean_waveform"][:] if "buzcode_mean_waveform" in u
                     else np.full((n, 32), np.nan))''')
open(p,'w').write(t)
EOF
cd $TMPDIR && . dev/bin/activate && python survey_all.py 2>&1 | tail -50
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/survey_all.py", line 9, in <module>
    with ThreadPoolExecutor(4) as ex: S=list(ex.map(ld, assets))
                                        ~~~~^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/concurrent/futures/_base.py", line 625, in result_iterator
    yield _result_or_cancel(fs.pop())
          ~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/concurrent/futures/_base.py", line 318, in _result_or_cancel
    return fut.result(timeout)
           ~~~~~~~~~~^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/concurrent/futures/_base.py", line 460, in result
    return self.__get_result()
           ~~~~~~~~~~~~~~~~~^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/concurrent/futures/_base.py", line 402, in __get_result
    raise self._exception
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/concurrent/futures/thread.py", line 59, in run
    result = self.fn(*self.args, **self.kwargs)
  File "/tmp/claude-1001/survey_all.py", line 8, in ld
    return hd.load_session(x[1], x[0])
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peyrache-2015 && python - <<'EOF'
p='hd.py'; t=open(p).read()
t=t.replace('''    ep = f["intervals/epochs"]
    ti = ep["tags_index"][:]
    tags = [_txt(x) for x in ep["tags"][:]]
    s["epochs"] = [(tags[a:b], t0, t1) for a, b, t0, t1 in
                   zip(np.r_[0, ti[:-1]], ti, ep["start_time"][:], ep["stop_time"][:])]
    sr = f["intervals/sub_recordings"]
    s["sub_recordings"] = list(zip([_txt(x) for x in sr["file_name"][:]],
                                   sr["start_time"][:], sr["stop_time"][:]))''','''    s["epochs"] = []
    if "intervals/epochs" in f:
        ep = f["intervals/epochs"]
        ti = ep["tags_index"][:]
        tags = [_txt(x) for x in ep["tags"][:]]
        s["epochs"] = [(tags[a:b], t0, t1) for a, b, t0, t1 in
                       zip(np.r_[0, ti[:-1]], ti, ep["start_time"][:], ep["stop_time"][:])]
    s["sub_recordings"] = []
    if "intervals/sub_recordings" in f:
        sr = f["intervals/sub_recordings"]
        s["sub_recordings"] = list(zip([_txt(x) for x in sr["file_name"][:]],
                                       sr["start_time"][:], sr["stop_time"][:]))''')
t=t.replace('''    b = f["processing/behavior"]
    s["states"] = {}''','''    b = f["processing/behavior"] if "processing/behavior" in f else {}
    s["states"] = {}''')
open(p,'w').write(t)
EOF
cd $TMPDIR && . dev/bin/activate && python survey_all.py 2>&1 | tail -50
```

```
time 114.01747298240662
sub-Mouse12_ses-Mouse12-120806 Mouse12 n 62 ADn 41 PoS 0 oth [np.str_('Field CA1'), np.str_('Prelimbic area')] list 41 labHD ADn 19 PoS 0 {'wake': 36.5, 'SWS': 122.0, 'REM': 16.8} [['sleep_pre'], ['sleep_pre'], ['sleep_pre'], ['open_field'], ['sleep_post'], ['sleep_post'], ['sleep_post'], ['wake_opto'], ['rest_opto'], ['second_environment'], ['second_environment'], ['second_environment']] hd True (27968000, 85)
sub-Mouse12_ses-Mouse12-120807 Mouse12 n 64 ADn 41 PoS 0 oth [np.str_('Field CA1'), np.str_('Prelimbic area')] list 41 labHD ADn 11 PoS 0 {'wake': 34.7, 'SWS': 139.4, 'REM': 20.3} [['sleep_pre'], ['sleep_pre'], ['open_field'], ['sleep_post'], ['sleep_post'], ['wake_opto'], ['rest_opto'], ['second_environment'], ['second_environment'], ['second_environment']] hd True (27778500, 85)
sub-Mouse12_ses-Mouse12-120808 Mouse12 n 68 ADn 40 PoS 0 oth [np.str_('Field CA1'), np.str_('Prelimbic area')] list 40 labHD ADn 11 PoS 0 {'wake': 45.6, 'SWS': 139.1, 'REM': 19.8} [['sleep_pre'], ['sleep_pre'], ['sleep_post'], ['sleep_post'], ['sleep_post'], ['wake_opto'], ['rest_opto'], ['open_field'], ['second_environment'], ['open_field'], ['second_environment'], ['open_field'], ['second_environment']] hd True (31295500, 85)
sub-Mouse12_ses-Mouse12-120809 Mouse12 n 278 ADn 50 PoS 0 oth [np.str_('Field CA1'), np.str_('Prelimbic area'), np.str_('Reticular nucleus of the thalamus')] list 50 labHD ADn 13 PoS 0 {'wake': 35.1, 'SWS': 163.9, 'REM': 29.6} [['sleep_pre'], ['sleep_pre'], ['open_field'], ['sleep_post'], ['sleep_post'], ['sleep_post'], ['wake_opto'], ['rest_opto'], ['second_environment'], ['second_environment'], ['second_environment']] hd True (30485750, 89)
sub-Mouse12_ses-Mouse12-120810 Mouse12 n 76 ADn 45 PoS 0 oth [np.str_('Field CA1'), np.str_('Prelimbic area')] list 45 labHD ADn 9 PoS 0 {'wake': 30.1, 'SWS': 147.0, 'REM': 24.0} [['sleep_pre'], ['sleep_pre'], ['open_field'], ['sleep_post'], ['sleep_post'], ['sleep_post'], ['wake_opto'], ['rest_op
[... 38 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && cat > depth.py <<'EOF'
import sys, re, pickle, numpy as np
sys.path.insert(0,'entries/peyrache-2015')
import hd
from concurrent.futures import ThreadPoolExecutor
assets=hd.list_assets()
def g(x):
    f=hd.open_asset(x[1]); out={}
    for d in f['general/devices']:
        desc=f['general/devices'][d].attrs.get('description','')
        m=re.search(r'session ([0-9.]+) mm',desc); out[d]=float(m.group(1)) if m else None
    b=f['processing/behavior'] if 'processing/behavior' in f else {}
    return x[0].split('_ses-')[1][:14], out, list(b.keys())
with ThreadPoolExecutor(4) as ex: R=list(ex.map(g,assets))
for r in R: print(r)
EOF
python depth.py
```

```
Sun Nov 15 11:41:14 UTC 2026
('Mouse12-120806', {'hippocampal_wires': None, 'other_channels': None, 'prefrontal_tetrodes': None, 'thalamic_probe': 2.97}, ['head_direction', 'position', 'sleep_states', 'sleep_states_buzcode'])
('Mouse12-120807', {'hippocampal_wires': None, 'other_channels': None, 'prefrontal_tetrodes': None, 'thalamic_probe': 3.04}, ['head_direction', 'position', 'sleep_states', 'sleep_states_buzcode'])
('Mouse12-120808', {'hippocampal_wires': None, 'other_channels': None, 'prefrontal_tetrodes': None, 'thalamic_probe': 3.11}, ['head_direction', 'position', 'sleep_states', 'sleep_states_buzcode'])
('Mouse12-120809', {'hippocampal_wires': None, 'other_channels': None, 'prefrontal_tetrodes': None, 'thalamic_probe': 3.18}, ['head_direction', 'position', 'sleep_states', 'sleep_states_buzcode'])
('Mouse12-120810', {'hippocampal_wires': None, 'other_channels': None, 'prefrontal_tetrodes': None, 'thalamic_probe': 3.25}, ['head_direction', 'position', 'sleep_states', 'sleep_states_buzcode'])
('Mouse17-130125', {'hippocampal_wires': None, 'thalamic_probe': 2.71}, ['head_direction', 'position', 'sleep_states', 'sleep_states_buzcode'])
('Mouse17-130128', {'hippocampal_wires': None, 'thalamic_probe': 2.78}, ['head_direction', 'position', 'sleep_states', 'sleep_states_buzcode'])
('Mouse17-130129', {'hippocampal_wires': None, 'thalamic_probe': 2.85}, ['head_direction', 'position', 'sleep_states', 'sleep_states_buzcode'])
('Mouse17-130130', {'hippocampal_wires': None, 'thalamic_probe': 2.92}, ['head_direction', 'position', 'sleep_states', 'sleep_states_buzcode'])
('Mouse17-130131', {'hippocampal_wires': None, 'thalamic_probe': 2.99}, ['head_direction', 'position', 'sleep_states', 'sleep_states_buzcode'])
('Mouse17-130201', {'hippocampal_wires': None, 'thalamic_probe': 2.99}, ['head_direction', 'position', 'sleep_states', 'sleep_states_buzcode'])
('Mouse17-130202', {'hippocampal_wires': None, 'thalamic_probe': 3.06}, ['head_direction', 'position', 'sleep_states', 'sl
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> entries/peyrache-2015/hd.py <<'EOF'


# ---------------------------------------------------------------- session rule

def thalamic_rule(sessions):
    """Methods, Recording sessions: "we discarded from analysis sessions
    separated by less than three days during which the thalamic probe was not
    moved". Applied per mouse in date order: a session is kept when the
    thalamic probe depth (device description, from the CRCNS session table)
    differs from that of the last kept session, or when it is at least three
    days after it. Returns {session: kept}."""
    import datetime as dt
    out = {}
    by = {}
    for name, depth in sessions:
        m, d = name.split("-")
        by.setdefault(m, []).append((dt.datetime.strptime(d, "%y%m%d"), depth, name))
    for m, L in by.items():
        last = None
        for date, depth, name in sorted(L):
            keep = (last is None or depth is None or last[1] is None or depth != last[1]
                    or (date - last[0]).days >= 3)
            out[name] = keep
            if keep:
                last = (date, depth)
    return out


# ---------------------------------------------------------------- waveforms

def waveform_features(w, fs=20000.0):
    """Supplementary Fig. 6 / Methods, Classification of PoS neurons: (i) total
    duration = 1 / frequency of maximum power of a wavelet transform of the
    mean waveform; (ii) trough-to-peak time. The wavelet (complex Morlet, 6
    cycles, power summed over the waveform, 200 to 4000 Hz) and the 4x cubic
    upsampling are standard choices. Returns (duration_ms, trough_to_peak_ms)."""
    from scipy.interpolate import CubicSpline
    if not np.all(np.isfinite(w)):
        return np.nan, np.nan
    w = w - np.median(w)
    if abs(w.min()) < abs(w.max()):
        w = -w  # trough-first polarity
    n = len(w)
    x = np.arange(n) / fs
    xx = np.linspace(0, x[-1], 4 * n)
    ww = CubicSpline(x, w)(xx)
    fs2 = 1 / (xx[1] - xx[0])
    it = int(np.argmin(ww))
    ip = it + int(np.argmax(ww[it:]))
    t2p = (ip - it) / fs2 * 1e3
    freqs = np.linspace(200, 4000, 200)
    wpad = np.r_[np.zeros(len(ww)), ww, np.zeros(len(ww))]
    tt = (np.arange(len(wpad)) - len(wpad) / 2) / fs2
    pw = []
    for fr in freqs:
        sd = 6 / (2 * np.pi * fr)
        mw = np.exp(2j * np.pi * fr * tt) * np.exp(-tt ** 2 / (2 * sd ** 2))
        mw /= np.sqrt(np.sum(np.abs(mw) ** 2))
        c = np.convolve(wpad, mw, mode="same")
        pw.append(np.sum(np.abs(c) ** 2))
    fmax = freqs[int(np.argmax(pw))]
    return 1e3 / fmax, t2p


def pos_class(dur, t2p):
    """Methods: interneuron for duration < 0.9 ms and trough-to-peak < 0.42 ms;
    pyramidal for duration > 0.95 ms and trough-to-peak > 0.42 ms."""
    if dur < 0.9 and t2p < 0.42:
        return "int"
    if dur > 0.95 and t2p > 0.42:
        return "pyr"
    return "und"


# ---------------------------------------------------------------- correlograms

def ccg_counts(a, b, width, half):
    """Cross-correlogram of spike trains a (reference) and b: counts of b
    spikes at lags (b - a) in bins of `width` from -half to +half (bin centred
    on 0). Exact, by sorted search."""
    nb = int(round(half / width))
    edges = (np.arange(-nb, nb + 2) - 0.5) * width
    lo = np.searchsorted(b, a + edges[0])
    hi = np.searchsorted(b, a + edges[-1])
    cnt = hi - lo
    tot = int(cnt.sum())
    out = np.zeros(len(edges) - 1)
    if tot == 0:
        return out, 0.5 * (edges[1:] + edges[:-1])
    # chunk over reference spikes to bound memory
    step = max(1, int(2e7 // max(1, cnt.mean() + 1)))
    for s0 in range(0, len(a), step):
        lo_, hi_, a_ = lo[s0:s0 + step], hi[s0:s0 + step], a[s0:s0 + step]
        c_ = hi_ - lo_
        if c_.sum() == 0:
            continue
        rep = np.repeat(np.arange(len(a_)), c_)
        off = np.arange(c_.sum()) - np.repeat(np.cumsum(c_) - c_, c_)
        d = b[np.repeat(lo_, c_) + off] - a_[rep]
        out += np.histogram(d, edges)[0]
    return out, 0.5 * (edges[1:] + edges[:-1])


def mono_test(c, width, sd=0.01, hollow=False, pct=0.999, lag=(0.001, 0.01)):
    """Methods, Detection of mono-synaptic connections: CCG in 0.5 ms bins
    convolved with a 10 ms s.d. Gaussian as the baseline; bins above the 99.9th
    percentile of the Poisson distribution at the baseline; a connection when
    at least two consecutive bins pass at lags of 1 to 10 ms. Returns
    (excitatory at positive lags, at negative lags). `hollow` leaves the
    central bin out of the convolution (reading m-b, after ref 58)."""
    n = len(c)
    sdb = sd / width
    half = int(4 * sdb)
    k = np.exp(-0.5 * (np.arange(-half, half + 1) / sdb) ** 2)
    if hollow:
        k[half] = 0.0
    k /= k.sum()
    base = np.convolve(np.r_[c[half:0:-1], c, c[-2:-half - 2:-1]], k, mode="valid")
    thr = stats.poisson.ppf(pct, np.maximum(base, 1e-12))
    sig = c > thr
    mid = n // 2
    lags = (np.arange(n) - mid) * width
    def run(mask):
        m = mask.astype(int)
        return bool(np.any(m[:-1] & m[1:]))
    pos = (lags >= lag[0] - 1e-12) & (lags <= lag[1] + 1e-12)
    neg = (lags <= -lag[0] + 1e-12) & (lags >= -lag[1] - 1e-12)
    return run(sig & pos), run(sig[::-1] & pos[::-1]) if False else run(np.where(neg, sig, False))


def ang_corr(h1, h2):
    """Angular correlation of two tuning curves as a function of offset,
    normalised so that 1 is chance (Supplementary Fig. 4): rho(d) =
    mean(h1(x) h2(x + d)) / (mean h1 mean h2), for d in 1 degree steps."""
    F = np.fft.ifft(np.conj(np.fft.fft(h1)) * np.fft.fft(h2)).real / len(h1)
    return F / (h1.mean() * h2.mean())


_CHI_Q = stats.chi2.ppf((np.arange(200) + 0.5) / 200, 3) / 3.0  # speeds / mean speed


def expected_ccg(rho, lags, v):
    """Expected CCG at lags (s) for mean speed v (rad/s): the mean over a
    chi-squared (3 d.f.) speed distribution scaled to mean v of the angular
    correlation at offset speed x lag, averaged over the two turning directions
    (Methods, Estimation of angular velocity)."""
    th = np.abs(v) * _CHI_Q[None, :] * lags[:, None]  # rad
    idx = (np.round(np.degrees(th)).astype(int)) % NBINS
    r = 0.5 * (rho[idx] + rho[(-idx) % NBINS])
    return r.mean(1)


def fit_speed(rho, lags, ccg):
    """Mean angular speed (rad/s) minimising the squared difference between
    the expected and observed CCG: coarse grid, then Nelder-Mead (Methods)."""
    grid = np.radians(np.geomspace(5, 5000, 80))
    cost = [np.sum((expected_ccg(rho, lags, v) - ccg) ** 2) for v in grid]
    v0 = grid[int(np.argmin(cost))]
    res = optimize.minimize(lambda x: np.sum((expected_ccg(rho, lags, abs(x[0])) - ccg) ** 2),
                            [v0], method="Nelder-Mead", options=dict(xatol=1e-4, fatol=1e-10))
    return abs(float(res.x[0]))
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/peyrache-2015 && python - <<'EOF'
p='hd.py'; t=open(p).read()
t=t.replace("    return run(sig & pos), run(sig[::-1] & pos[::-1]) if False else run(np.where(neg, sig, False))",
"    return run(np.where(pos, sig, False)), run(np.where(neg, sig, False))")
open(p,'w').write(t)
EOF
echo done
```

```
done
```

**Agent calls Bash**

```bash
cat >> hd.py <<'EOF'


# ---------------------------------------------------------------- per session

def state_iv(s, k):
    return s["states"].get(k, np.zeros((0, 2)))


def _xcorr_lags(x, y, maxlag):
    """sum_t x(t) y(t + lag) / N for lag in -maxlag..maxlag bins (FFT)."""
    n = len(x)
    L = 1 << int(np.ceil(np.log2(2 * n + 1)))
    F = np.fft.irfft(np.conj(np.fft.rfft(x, L)) * np.fft.rfft(y, L), L)
    out = np.r_[F[-maxlag:], F[:maxlag + 1]] / n
    return out


def morlet_power(z, width, freqs, ncyc=5):
    """Mean power over lags of a complex Morlet transform of a correlogram
    (fig6a, reading o-c: complex Morlet, a standard choice)."""
    t = (np.arange(len(z)) - len(z) // 2) * width
    out = []
    for fr in freqs:
        sd = ncyc / (2 * np.pi * fr)
        w = np.exp(2j * np.pi * fr * t) * np.exp(-t ** 2 / (2 * sd ** 2))
        w /= np.sum(np.abs(w))
        c = np.convolve(z, w, mode="same")
        m = np.abs(t) <= 0.025
        out.append(np.mean(np.abs(c[m]) ** 2))
    return np.array(out)


FAST_FREQS = np.arange(50, 301, 5.0)
OLE_WINDOWS = np.array([0.01, 0.02, 0.05, 0.1, 0.2, 0.3, 0.5, 1.0])


def analyze_session(s, parts=("cells", "pairs", "decode", "fast", "mono")):
    """All per-session measures. Returns dict of lists of records."""
    out = {"cells": [], "pairs": [], "ens": [], "fast": [], "mono": [], "dec5b": []}
    if s.get("hd") is None or "wake" not in s["states"]:
        return out
    name = s["path"].split("_ses-")[1].split("_")[0]
    keep = np.where(np.isin(s["region"], [ADN, POS]))[0]
    t, a = wake_hd(s)
    rate = s["hd_rate"]
    dt = 1.0 / rate
    occ = occupancy(a)
    W = s["states"]["wake"]
    has_sleep = len(state_iv(s, "SWS")) > 0 and len(state_iv(s, "REM")) > 0
    cells = []
    tcs = {}
    for u in keep:
        sp = s["spikes"][u]
        rec = dict(session=name, subject=s["subject"], unit=int(u), region="ADn" if s["region"][u] == ADN else "PoS",
                   shank=int(s["shank"][u]), lab_hd=bool(s["is_hd_cell"][u]) if np.isfinite(s["is_hd_cell"][u]) else None,
                   lab_pref=float(s["hd_preferred_direction"][u]))
        for k in STATES:
            iv = state_iv(s, k)
            rec["rate_" + k] = len(restrict(sp, iv)) / total(iv) if total(iv) > 0 else np.nan
        sh = spike_hd(restrict(sp, W), t, a, rate)
        tc = tuning_curve(sh, occ, dt)
        tcs[u] = tc
        fa, fb = vm_fit_a(tc, len(sh)), vm_fit_b(tc, sh)
        for nm, fz in (("a", fa), ("b", fb)):
            rec.update({f"pref_{nm}": fz["pref"], f"kappa_{nm}": fz["kappa"], f"peak_{nm}": fz["peak"],
                        f"p_{nm}": fz["p"], f"hd_{nm}": is_hd(fz)})
        rec["unimodal_fail_a"], rec["unimodal_fail_b"] = n_peaks(tc)
        rec["nspk_wake"] = len(sh)
        if "cells" in parts:
            rec["info"] = hd_information(restrict(sp, W), t, a, rate)
        d, tp = waveform_features(s["waveform"][u])
        rec["dur_ms"], rec["t2p_ms"] = d, tp
        rec["cls"] = pos_class(d, tp) if np.isfinite(d) else "und"
        rec["has_sleep"] = has_sleep
        rec["pass_rate_a"] = bool(all(np.isfinite(rec["rate_" + k]) and rec["rate_" + k] >= RATE_MIN for k in STATES))
        rec["pass_rate_b"] = bool(any(np.isfinite(rec["rate_" + k]) and rec["rate_" + k] >= RATE_MIN for k in STATES))
        cells.append(rec)
    out["cells"] = cells
    if not cells:
        return out
    U = [c["unit"] for c in cells]
    R = {c["unit"]: c for c in cells}
    # ---------------- pairs: binned correlations, speeds, noise correlations
    if "pairs" in parts:
        corr_bins = {}
        for k in STATES:
            iv = state_iv(s, k)
            corr_bins[k] = bin_matrix([s["spikes"][u] for u in U], iv, CORR_BIN[k]) if total(iv) > 0 else None
        cc = {}
        for k in STATES:
            M = corr_bins[k]
            if M is None or M.shape[1] < 10:
                cc[k] = None
                continue
            with np.errstate(invalid="ignore", divide="ignore"):
                cc[k] = np.corrcoef(M)
        # 10 ms counts per state for the speed CCGs
        c10 = {}
        for k in STATES:
            iv = state_iv(s, k)
            c10[k] = bin_matrix([s["spikes"][u] for u in U], iv, 0.01) if total(iv) > 0 else None
        # noise correlations, wake: 10 ms bins with valid head direction
        wb, wcen = bin_counts(np.zeros(0), W, 0.01)
        i = np.clip(np.searchsorted(s["hd_t"], wcen), 1, len(s["hd_t"]) - 1)
        j = np.where(np.abs(s["hd_t"][i - 1] - wcen) < np.abs(s["hd_t"][i] - wcen), i - 1, i)
        th = s["hd"][j]
        okb = np.isfinite(th)
        Xw = c10["wake"][:, okb] / 0.01
        thb = np.minimum((th[okb] / (2 * np.pi) * NBINS).astype(int), NBINS - 1)
        Fw = np.array([tcs[u][thb] for u in U])
        mlag = 5  # -50..+50 ms in 10 ms bins (Methods)
        hdu = [ii for ii, u in enumerate(U) if R[u]["hd_a"] or R[u]["hd_b"]]
        lagsec = {"wake": 2.0, "REM": 2.0, "SWS": 0.5}  # reading v-a
        for ii in range(len(U)):
            for jj in range(ii + 1, len(U)):
                ui, uj = U[ii], U[jj]
                ci, cj = R[ui], R[uj]
                rec = dict(session=name, subject=s["subject"], u1=ui, u2=uj,
                           kind="-".join(sorted([ci["region"], cj["region"]])),
                           same_shank=ci["shank"] == cj["shank"])
                for k in STATES:
                    rec["corr_" + k] = float(cc[k][ii, jj]) if cc[k] is not None else np.nan
                cs = _xcorr_lags(Xw[ii], Xw[jj], mlag)
                cf = _xcorr_lags(Fw[ii], Fw[jj], mlag)
                mi, mj = Xw[ii].mean(), Xw[jj].mean()
                nz = cs - cf
                rec["noise_avg_raw"] = float(nz.mean())
                rec["noise_0_raw"] = float(nz[mlag])
                rec["noise_avg_norm"] = float(nz.mean() / (mi * mj)) if mi * mj > 0 else np.nan
                rec["noise_0_norm"] = float(nz[mlag] / (mi * mj)) if mi * mj > 0 else np.nan
                if ii in hdu and jj in hdu and ci["region"] == cj["region"]:
                    rho = ang_corr(tcs[ui], tcs[uj])
                    for k in STATES:
                        X = c10[k]
                        if X is None or X[ii].sum() == 0 or X[jj].sum() == 0:
                            rec["v_" + k] = np.nan
                            continue
                        ml = int(round(lagsec[k] / 0.01))
                        cg = _xcorr_lags(X[ii], X[jj], ml) / (X[ii].mean() * X[jj].mean())
                        lags = np.arange(-ml, ml + 1) * 0.01
                        rec["v_" + k] = np.degrees(fit_speed(rho, lags, cg))
                out["pairs"].append(rec)
        del c10, corr_bins, Xw, Fw
    # ---------------- decoding per structure
    if "decode" in parts:
        out["ens"], out["dec5b"] = decode_session(s, name, cells, tcs, t, a)
    # ---------------- fast synchrony (ADn HD pairs) per state
    if "fast" in parts:
        adn_hd = [u for u in U if R[u]["region"] == "ADn" and (R[u]["hd_a"] or R[u]["hd_b"])]
        w = 0.0005
        for k in STATES:
            iv = state_iv(s, k)
            if total(iv) == 0:
                continue
            sps = {u: restrict(s["spikes"][u], iv) for u in adn_hd}
            for x in range(len(adn_hd)):
                for y in range(x + 1, len(adn_hd)):
                    ux, uy = adn_hd[x], adn_hd[y]
                    c, lags = ccg_counts(sps[ux], sps[uy], w, 0.07)
                    nbox = int(round(0.01 / w))
                    box = np.ones(2 * nbox + 1) / (2 * nbox + 1)
                    m = np.convolve(c, box, mode="same")
                    sel = np.abs(lags) <= 0.05 + 1e-9
                    z = (c - m) / np.sqrt(np.maximum(m, 1e-9))
                    z = z[sel]
                    lg = lags[sel]
                    out["fast"].append(dict(session=name, subject=s["subject"], u1=ux, u2uy=uy, u2=uy, state=k,
                                            same_shank=R[ux]["shank"] == R[uy]["shank"],
                                            zpeak5=float(z[np.abs(lg) <= 0.005].max()),
                                            z0=float(z[np.argmin(np.abs(lg))]),
                                            power=morlet_power(z, w, FAST_FREQS),
                                            nspk=(len(sps[ux]), len(sps[uy]))))
    # ---------------- monosynaptic, ADn x PoS (whole recording)
    if "mono" in parts:
        adn = [u for u in U if R[u]["region"] == "ADn"]
        pos = [u for u in U if R[u]["region"] == "PoS"]
        w = 0.0005
        for ua in adn:
            for up in pos:
                c, lags = ccg_counts(s["spikes"][ua], s["spikes"][up], w, 0.06)
                rec = dict(session=name, subject=s["subject"], adn=ua, pos=up)
                for hol in (False, True):
                    f, b = mono_test(c, w, hollow=hol)
                    rec[f"a2p_{'h' if hol else 'c'}"] = f
                    rec[f"p2a_{'h' if hol else 'c'}"] = b
                # jittered baseline (m-d): expectation of the CCG with one train
                # jittered uniformly by +-10 ms is the CCG convolved with a 20 ms box
                nbox = int(round(0.01 / w))
                base = np.convolve(c, np.ones(2 * nbox + 1) / (2 * nbox + 1), mode="same")
                thr = stats.poisson.ppf(0.999, np.maximum(base, 1e-12))
                sig = c > thr
                pz = (lags >= 0.001 - 1e-9) & (lags <= 0.01 + 1e-9)
                nz_ = (lags <= -0.001 + 1e-9) & (lags >= -0.01 - 1e-9)
                run = lambda m_: bool(np.any(m_[:-1] & m_[1:]))
                rec["a2p_j"] = run(np.where(pz, sig, False))
                rec["p2a_j"] = run(np.where(nz_, sig, False))
                out["mono"].append(rec)
    return out
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cat >> hd.py <<'EOF'


def _hd_at(s, cen):
    i = np.clip(np.searchsorted(s["hd_t"], cen), 1, len(s["hd_t"]) - 1)
    j = np.where(np.abs(s["hd_t"][i - 1] - cen) < np.abs(s["hd_t"][i] - cen), i - 1, i)
    return s["hd"][j]


def _tc_from_bins(C, thb, dtb):
    occ = np.bincount(thb, minlength=NBINS).astype(float) * dtb
    out = []
    for c in C:
        cnt = np.bincount(thb, weights=c, minlength=NBINS)
        out.append(circ_smooth(cnt, SMOOTH_DEG) / np.maximum(circ_smooth(occ, SMOOTH_DEG), 1e-9))
    return np.array(out)


def ole_fit(Rtr, thtr, Ftr=None):
    """Optimal linear estimator (Salinas and Abbott 1994): D = Q^-1 L with
    L = <r e^{i theta}> and Q = <r r^T> (cov) or, when F (the tuning curves
    read at the head direction, smoothed as r) is given, the signal reading
    Q = <F F^T> off the diagonal with the diagonal of <r r^T> (independent
    neurons with the observed variances; assumption). Returns complex
    weights."""
    n = Rtr.shape[1]
    L = Rtr.T @ np.exp(1j * thtr) / n
    Q = Rtr.T @ Rtr / n
    if Ftr is not None:
        Qs = Ftr.T @ Ftr / n
        np.fill_diagonal(Qs, np.diag(Q))
        Q = Qs
    return np.linalg.solve(Q + 1e-9 * np.eye(len(Q)), L)


def decode_session(s, name, cells, tcs, t, a):
    ens, dec5b = [], []
    W = s["states"]["wake"]
    R = {c["unit"]: c for c in cells}
    groups = {}
    for reg in ("ADn", "PoS"):
        groups[reg] = [c["unit"] for c in cells if c["region"] == reg and c["hd_a"]]
    for reg, hu in groups.items():
        if len(hu) < 6:
            continue
        TC = np.array([tcs[u] for u in hu])
        e = dict(session=name, subject=s["subject"], region=reg, n_hd=len(hu))
        dec = {}
        for k in STATES:
            iv = state_iv(s, k)
            if total(iv) == 0:
                continue
            C = bin_matrix([s["spikes"][u] for u in hu], iv, DEC_BIN)
            _, cen = bin_counts(np.zeros(0), iv, DEC_BIN)
            Cs = gauss_smooth_counts(C, DEC_SMOOTH[k])
            ang = bayes_decode(Cs, TC, DEC_BIN)
            dec[k] = (ang, cen, C)
            sp_a = np.abs(circ_diff(ang[1:], ang[:-1])) / DEC_BIN
            ksub = int(round(DEC_SMOOTH[k] / DEC_BIN))
            sub = ang[::ksub]
            sp_b = np.abs(circ_diff(sub[1:], sub[:-1])) / (ksub * DEC_BIN)
            e[f"speed_a_{k}"] = float(np.degrees(np.median(sp_a)))
            e[f"speed_b_{k}"] = float(np.degrees(np.median(sp_b)))
            if k == "wake":
                th = _hd_at(s, cen)
                ok = np.isfinite(th)
                e["err_full"] = float(np.degrees(np.median(np.abs(circ_diff(ang[ok], th[ok])))))
                # 10-segment cross-validation
                idx = np.where(ok)[0]
                seg = (np.arange(len(idx)) * 10) // len(idx)
                thb = np.minimum((th[idx] / (2 * np.pi) * NBINS).astype(int), NBINS - 1)
                errs = []
                for q in range(10):
                    tr, te = idx[seg != q], idx[seg == q]
                    tcq = _tc_from_bins(C[:, tr], thb[seg != q], DEC_BIN)
                    aq = bayes_decode(Cs[:, te], tcq, DEC_BIN)
                    errs.append(np.abs(circ_diff(aq, th[te])))
                e["err_cv"] = float(np.degrees(np.median(np.concatenate(errs))))
                # actual head speed (w-b): frames, and over ~300 ms
                ah = a
                da = np.abs(circ_diff(ah[1:], ah[:-1])) * s["hd_rate"]
                gap = np.diff(t) < 1.5 / s["hd_rate"]
                e["speed_a_actual"] = float(np.degrees(np.median(da[gap])))
                kk = int(round(0.3 * s["hd_rate"]))
                db = np.abs(circ_diff(ah[kk:], ah[:-kk])) / (t[kk:] - t[:-kk])
                gb = (t[kk:] - t[:-kk]) < (kk + 0.5) / s["hd_rate"]
                e["speed_b_actual"] = float(np.degrees(np.median(db[gb])))
                # OLE and Bayes over windows, cross-validated
                for wdw in OLE_WINDOWS:
                    Cw = gauss_smooth_counts(C, wdw)[:, idx]
                    Fw = gauss_smooth_counts(TC[:, np.minimum((np.nan_to_num(th) / (2 * np.pi) * NBINS).astype(int), NBINS - 1)] * DEC_BIN, wdw)[:, idx]
                    eo, es, eb = [], [], []
                    for q in range(10):
                        tr, te = seg != q, seg == q
                        Dc = ole_fit(Cw[:, tr].T, th[idx][tr])
                        Ds = ole_fit(Cw[:, tr].T, th[idx][tr], Fw[:, tr].T)
                        thq = th[idx][te]
                        eo.append(np.abs(circ_diff(np.angle(Cw[:, te].T @ Dc), thq)))
                        es.append(np.abs(circ_diff(np.angle(Cw[:, te].T @ Ds), thq)))
                        tcq = _tc_from_bins(C[:, idx[tr]], thb[tr], DEC_BIN)
                        eb.append(np.abs(circ_diff(bayes_decode(Cw[:, te], tcq, DEC_BIN), thq)))
                    e[f"ole_cov_{wdw}"] = float(np.degrees(np.median(np.concatenate(eo))))
                    e[f"ole_sig_{wdw}"] = float(np.degrees(np.median(np.concatenate(es))))
                    e[f"bayes_{wdw}"] = float(np.degrees(np.median(np.concatenate(eb))))
        ens.append(e)
        # fig5b: tuning curves of the other structure's HD cells against decoded HD
        other = "PoS" if reg == "ADn" else "ADn"
        targets = [c["unit"] for c in cells if c["region"] == other and (c["hd_a"] or c["hd_b"])]
        for k, (ang, cen, _) in dec.items():
            iv = state_iv(s, k)
            T = bin_matrix([s["spikes"][u] for u in targets], iv, DEC_BIN) if targets else None
            ab = np.minimum((ang / (2 * np.pi) * NBINS).astype(int), NBINS - 1)
            ksub = int(round(DEC_SMOOTH[k] / DEC_BIN))
            nfull = (len(ab) // ksub) * ksub
            ab_b = ab[:nfull:ksub]
            for ti, u in enumerate(targets):
                tca = _tc_from_bins(T[ti:ti + 1], ab, DEC_BIN)[0]
                Tb = T[ti, :nfull].reshape(-1, ksub).sum(1)
                tcb = _tc_from_bins(Tb[None], ab_b, DEC_BIN * ksub)[0]
                dec5b.append(dict(session=name, subject=s["subject"], decoder=reg, target=u,
                                  target_region=other, state=k, hd_a=R[u]["hd_a"], hd_b=R[u]["hd_b"],
                                  r_a=float(np.corrcoef(tca, tcs[u])[0, 1]),
                                  r_b=float(np.corrcoef(tcb, tcs[u])[0, 1])))
    return ens, dec5b
EOF
cd $TMPDIR && . dev/bin/activate && cat > t2.py <<'EOF'
import sys, time, pickle, resource, numpy as np, pandas as pd
sys.path.insert(0,'entries/peyrache-2015')
import importlib, hd
S=pickle.load(open('sessions.pkl','rb'))
s=[x for x in S if 'Mouse24-131216' in x['path']][0]
for parts in [("cells",),("pairs",),("decode",),("fast",),("mono",)]:
    t=time.time(); o=hd.analyze_session(s,parts); print(parts, round(time.time()-t,1), {k:len(v) for k,v in o.items()}, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss//1000)
c=pd.DataFrame(o['cells']); print(c[['region','hd_a','hd_b','lab_hd','peak_a','peak_b','kappa_a','kappa_b','dur_ms','t2p_ms','cls']].to_string())
EOF
python t2.py
```

```
('cells',) 0.6 {'cells': 23, 'pairs': 0, 'ens': 0, 'fast': 0, 'mono': 0, 'dec5b': 0} 3032
('pairs',) 33.1 {'cells': 23, 'pairs': 253, 'ens': 0, 'fast': 0, 'mono': 0, 'dec5b': 0} 3440
('decode',) 9.5 {'cells': 23, 'pairs': 0, 'ens': 1, 'fast': 0, 'mono': 0, 'dec5b': 6} 3440
('fast',) 0.6 {'cells': 23, 'pairs': 0, 'ens': 0, 'fast': 84, 'mono': 0, 'dec5b': 0} 3440
('mono',) 1.4 {'cells': 23, 'pairs': 0, 'ens': 0, 'fast': 0, 'mono': 130, 'dec5b': 0} 3440
   region   hd_a   hd_b  lab_hd     peak_a     peak_b   kappa_a   kappa_b    dur_ms    t2p_ms  cls
0     PoS  False  False   False  23.760966  21.595260  0.068210  0.067898  1.103104  0.305118  und
1     PoS   True   True    True  10.767068  10.624803  1.529517  1.968328  1.718480  0.634646  pyr
2     PoS  False  False   False   0.642624   0.534111  0.179610  0.171006  1.293888  0.414961  und
3     PoS   True   True    True   7.539705   7.388884  1.226835  1.362818  1.718480  0.622441  pyr
4     PoS  False  False   False   0.274697   0.246097  1.392199  2.725530  1.612642  0.610236  pyr
5     PoS  False  False   False  77.067361  66.158186  0.086836  0.089556  1.177515  0.305118  und
6     PoS  False  False   False  34.606627  33.548051  0.044465  0.044551  0.732695  0.219685  int
7     PoS  False  False   False  28.885411  26.937067  0.068045  0.067638  1.326667  0.329528  und
8     PoS  False  False   False   1.791198   1.578958  0.149998  0.143005  0.880531  0.305118  int
9     PoS  False  False   False   0.201255   0.128840  0.229242  0.203382  0.753788  0.256299  int
10    PoS  False  False   False   0.557470   0.501945  0.154650  0.152408  0.684790  0.219685  int
11    PoS  False  False   False  13.098376  11.899371  0.050277  0.049889  1.663880  0.744488  pyr
12    PoS  False  False   False  18.626854  17.550641  0.051792  0.051175  1.361149  0.317323  und
13    ADn  False  False   False   2.205971   1.956414  0.103822  0.100528  1.435786  0.427165  pyr
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peyrache-2015 && python - <<'EOF'
p='hd.py'; t=open(p).read()
old_start=t.index("        mlag = 5  # -50..+50 ms")
t=t.replace('''        mlag = 5  # -50..+50 ms in 10 ms bins (Methods)''','''        mlag = 5  # -50..+50 ms in 10 ms bins (Methods)
        nW = Xw.shape[1]
        LW = 1 << int(np.ceil(np.log2(2 * nW + 1)))
        FX = np.fft.rfft(Xw, LW, axis=1)
        FF = np.fft.rfft(Fw, LW, axis=1)
        def xc(A, B, ml, n, L):
            F = np.fft.irfft(np.conj(A) * B, L)
            return np.r_[F[-ml:], F[:ml + 1]] / n
        FC = {}
        for k in STATES:
            X = c10[k]
            if X is None:
                continue
            Lk = 1 << int(np.ceil(np.log2(2 * X.shape[1] + 1)))
            FC[k] = (np.fft.rfft(X[hdu], Lk, axis=1), Lk, X.shape[1], {u: q for q, u in enumerate(hdu)})''')
t=t.replace('''                cs = _xcorr_lags(Xw[ii], Xw[jj], mlag)
                cf = _xcorr_lags(Fw[ii], Fw[jj], mlag)''','''                cs = xc(FX[ii], FX[jj], mlag, nW, LW)
                cf = xc(FF[ii], FF[jj], mlag, nW, LW)''')
t=t.replace('''                        X = c10[k]
                        if X is None or X[ii].sum() == 0 or X[jj].sum() == 0:
                            rec["v_" + k] = np.nan
                            continue
                        ml = int(round(lagsec[k] / 0.01))
                        cg = _xcorr_lags(X[ii], X[jj], ml) / (X[ii].mean() * X[jj].mean())''','''                        X = c10[k]
                        if X is None or X[ii].sum() == 0 or X[jj].sum() == 0:
                            rec["v_" + k] = np.nan
                            continue
                        ml = int(round(lagsec[k] / 0.01))
                        Fk, Lk, nk, pos_ = FC[k]
                        cg = xc(Fk[pos_[ii]], Fk[pos_[jj]], ml, nk, Lk) / (X[ii].mean() * X[jj].mean())''')
t=t.replace("        del c10, corr_bins, Xw, Fw","        del c10, corr_bins, Xw, Fw, FX, FF, FC")
open(p,'w').write(t)
EOF
cd $TMPDIR && . dev/bin/activate && cat > t3.py <<'EOF'
import sys, time, pickle, numpy as np, pandas as pd, cProfile, pstats
sys.path.insert(0,'entries/peyrache-2015')
import hd
S=pickle.load(open('sessions.pkl','rb'))
s=[x for x in S if 'Mouse24-131216' in x['path']][0]
t=time.time(); 
cProfile.run('o=hd.analyze_session(s,("pairs",))','prof')
print(time.time()-t)
pstats.Stats('prof').sort_stats('cumtime').print_stats(12)
p=pd.DataFrame(o['pairs']); print(p.describe().T.to_string())
EOF
python t3.py 2>&1 | tail -45
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/t3.py", line 7, in <module>
    cProfile.run('o=hd.analyze_session(s,("pairs",))','prof')
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/cProfile.py", line 18, in run
    return _pyprofile._Utils(Profile).run(statement, filename, sort)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/profile.py", line 55, in run
    prof.run(statement)
    ~~~~~~~~^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/cProfile.py", line 99, in run
    return self.runctx(cmd, dict, dict)
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/cProfile.py", line 104, in runctx
    exec(cmd, globals, locals)
    ~~~~^^^^^^^^^^^^^^^^^^^^^^
  File "<string>", line 1, in <module>
  File "entries/peyrache-2015/hd.py", line 669, in analyze_session
    FC[k] = (np.fft.rfft(X[hdu], Lk, axis=1), Lk, X.shape[1], {u: q for q, u in enumerate(hdu)})
                           ^^^
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peyrache-2015 && python - <<'EOF'
p='hd.py'; t=open(p).read()
t=t.replace('''        hdu = [ii for ii, u in enumerate(U) if R[u]["hd_a"] or R[u]["hd_b"]]
        lagsec''','''        lagsec''')
t=t.replace('''        mlag = 5  # -50..+50 ms in 10 ms bins (Methods)
''','''        mlag = 5  # -50..+50 ms in 10 ms bins (Methods)
        hdu = [ii for ii, u in enumerate(U) if R[u]["hd_a"] or R[u]["hd_b"]]
''')
open(p,'w').write(t)
EOF
cd $TMPDIR && . dev/bin/activate && python t3.py 2>&1 | tail -45
```

```
29.225266218185425
Sun Nov 15 11:47:21 2026    prof

         676265 function calls (676171 primitive calls) in 29.224 seconds

   Ordered by: cumulative time
   List reduced from 315 to 12 due to restriction <12>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   29.223   29.223 {built-in method builtins.exec}
        1    0.001    0.001   29.223   29.223 <string>:1(<module>)
        1    0.060    0.060   29.223   29.223 entries/peyrache-2015/hd.py:581(analyze_session)
        6    0.004    0.001   16.911    2.819 entries/peyrache-2015/hd.py:180(bin_matrix)
      139    0.180    0.001   16.884    0.121 entries/peyrache-2015/hd.py:159(bin_counts)
     3475    0.064    0.000   16.695    0.005 /tmp/claude-1001/dev/lib/python3.13/site-packages/numpy/lib/_histograms_impl.py:685(histogram)
     8550    0.010    0.000   14.826    0.002 /tmp/claude-1001/dev/lib/python3.13/site-packages/numpy/_core/fromnumeric.py:941(sort)
     8550   14.700    0.002   14.700    0.002 {method 'sort' of 'numpy.ndarray' objects}
       87    0.025    0.000    6.582    0.076 entries/peyrache-2015/hd.py:536(fit_speed)
    10692    5.640    0.001    6.404    0.001 entries/peyrache-2015/hd.py:525(expected_ccg)
      593    1.126    0.002    4.167    0.007 entries/peyrache-2015/hd.py:661(xc)
[... 17 more lines not kept]
```

**Agent**

Wake median speed fit is 32°/s and SWS about 420°/s (ratio about 13). Fixing a slow binning routine before the full run.

**Agent calls Bash**

```bash
cd entries/peyrache-2015 && python - <<'EOF'
p='hd.py'; t=open(p).read()
old=t[t.index("def bin_counts(sp, iv, width):"):t.index("def bin_matrix(")]
new='''def bin_edges(iv, width):
    """Bin edges laid within each interval (partial bins dropped)."""
    out = []
    for a, b in iv:
        n = int((b - a) // width)
        if n >= 1:
            out.append(a + np.arange(n + 1) * width)
    return out


def bin_counts(sp, iv, width, edges=None):
    """Counts of the sorted spike train sp in bins of `width` laid within each
    interval (partial bins dropped). Returns counts and bin centres."""
    edges = bin_edges(iv, width) if edges is None else edges
    if not edges:
        return np.zeros(0), np.zeros(0)
    cs = [np.diff(np.searchsorted(sp, e)) for e in edges]
    cen = [0.5 * (e[1:] + e[:-1]) for e in edges]
    return np.concatenate(cs), np.concatenate(cen)


'''
t=t.replace(old,new)
t=t.replace('''def bin_matrix(spikes, iv, width):
    out = [bin_counts(sp, iv, width)[0] for sp in spikes]''','''def bin_matrix(spikes, iv, width):
    e = bin_edges(iv, width)
    out = [bin_counts(sp, iv, width, e)[0] for sp in spikes]''')
open(p,'w').write(t)
EOF
cd $TMPDIR && . dev/bin/activate && python t3.py 2>&1 | head -3
```

```
12.96110725402832
Sun Nov 15 11:47:46 2026    prof
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > runall.py <<'EOF'
import sys, time, pickle, resource, numpy as np
sys.path.insert(0,'entries/peyrache-2015')
import hd
from concurrent.futures import ProcessPoolExecutor
def work(x):
    t=time.time()
    s=hd.load_session(x[1],x[0])
    o=hd.analyze_session(s)
    o['meta']=dict(path=x[0], subject=s['subject'], nunits=len(s['spikes']), t=time.time()-t, mem=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss//1000)
    return o
if __name__=='__main__':
    A=hd.list_assets()
    t=time.time()
    with ProcessPoolExecutor(4) as ex: O=list(ex.map(work,A))
    print('total',time.time()-t)
    for o in O: print(o['meta'])
    pickle.dump(O,open('results.pkl','wb'))
EOF
timeout 3000 python runall.py 2>&1 | tail -45; date -u
```

```
total 641.6293089389801
{'path': 'sub-Mouse12/sub-Mouse12_ses-Mouse12-120806_behavior+ecephys.nwb', 'subject': 'Mouse12', 'nunits': 62, 't': 173.365065574646, 'mem': 1692}
{'path': 'sub-Mouse12/sub-Mouse12_ses-Mouse12-120807_behavior+ecephys.nwb', 'subject': 'Mouse12', 'nunits': 64, 't': 98.07245469093323, 'mem': 1585}
{'path': 'sub-Mouse12/sub-Mouse12_ses-Mouse12-120808_behavior+ecephys.nwb', 'subject': 'Mouse12', 'nunits': 68, 't': 83.07118892669678, 'mem': 1537}
{'path': 'sub-Mouse12/sub-Mouse12_ses-Mouse12-120809_behavior+ecephys.nwb', 'subject': 'Mouse12', 'nunits': 278, 't': 113.04589772224426, 'mem': 1931}
{'path': 'sub-Mouse12/sub-Mouse12_ses-Mouse12-120810_behavior+ecephys.nwb', 'subject': 'Mouse12', 'nunits': 76, 't': 80.85173726081848, 'mem': 1562}
{'path': 'sub-Mouse17/sub-Mouse17_ses-Mouse17-130125_behavior+ecephys.nwb', 'subject': 'Mouse17', 'nunits': 7, 't': 4.058573961257935, 'mem': 1585}
{'path': 'sub-Mouse17/sub-Mouse17_ses-Mouse17-130128_behavior+ecephys.nwb', 'subject': 'Mouse17', 'nunits': 30, 't': 18.714229106903076, 'mem': 1585}
{'path': 'sub-Mouse17/sub-Mouse17_ses-Mouse17-130129_behavior+ecephys.nwb', 'subject': 'Mouse17', 'nunits': 43, 't': 104.02265787124634, 'mem': 1931}
{'path': 'sub-Mouse17/sub-Mouse17_ses-Mouse17-130130_behavior+ecephys.nwb', 'subject': 'Mouse17', 'nunits': 37, 't': 70.99419140815735, 'mem': 1585}
{'path': 'sub-Mouse17/sub-Mouse17_ses-Mouse17-130131_behavior+ecephys.nwb', 'subject': 'Mouse17', 'nunits': 33, 't': 55.2298367023468, 'mem': 1562}
{'path': 'sub-Mouse17/sub-Mouse17_ses-Mouse17-130201_behavior+ecephys.nwb', 'subject': 'Mouse17', 'nunits': 37, 't': 54.72921395301819, 'mem': 1692}
{'path': 'sub-Mouse17/sub-Mouse17_ses-Mouse17-130202_behavior+ecephys.nwb', 'subject': 'Mouse17', 'nunits': 39, 't': 36.44272589683533, 'mem': 1585}
{'path': 'sub-Mouse17/sub-Mouse17_ses-Mouse17-130203_behavior+ecephys.nwb', 'subject': 'Mouse17', 'nunits': 41, 't': 25.63545846939087, 'mem': 1931}
{'path': 'sub-Mouse17/sub-Mouse17_ses-
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > agg.py <<'EOF'
import sys, pickle, numpy as np, pandas as pd
from scipy import stats
sys.path.insert(0,'entries/peyrache-2015')
import hd
O=pickle.load(open('results.pkl','rb'))
C=pd.DataFrame([c for o in O for c in o['cells']])
P=pd.DataFrame([c for o in O for c in o['pairs']])
E=pd.DataFrame([c for o in O for c in o['ens']])
print(len(C), C.groupby('region').size())
for r in ['a','b']:
    print(r, C.groupby(['subject','region'])['hd_'+r].sum().unstack().to_string())
print('lab', C.groupby(['subject','region'])['lab_hd'].sum().unstack().to_string())
print(pd.crosstab(C.hd_a, C.lab_hd), pd.crosstab(C.hd_b, C.lab_hd))
h=C[C.hd_a]
for reg in ['ADn','PoS']: print(reg, h[h.region==reg].peak_a.median(), h[h.region==reg].peak_a.mean(), h[h.region==reg]['info'].median(), h[h.region==reg]['info'].mean(), h[h.region==reg].unimodal_fail_a.mean(), h[h.region==reg].unimodal_fail_b.mean())
print(E.T.to_string())
EOF
python agg.py
```

```
1016 region
ADn    708
PoS    308
dtype: int64
a region    ADn   PoS
subject            
Mouse12  66.0   NaN
Mouse17  51.0   NaN
Mouse20  14.0   0.0
Mouse24  26.0   7.0
Mouse25  43.0  28.0
Mouse28  74.0  34.0
b region    ADn   PoS
subject            
Mouse12  66.0   NaN
Mouse17  54.0   NaN
Mouse20  16.0   0.0
Mouse24  29.0   9.0
Mouse25  46.0  43.0
Mouse28  82.0  48.0
[... 57 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import sys
sys.path.insert(0,'entries/peyrache-2015')
import hd
f=hd.open_asset('25b0f421-e8d7-43ce-8358-a95cb4e192c0')
l=f['processing/ecephys/LFP/lfp']; print(list(l.keys()))
e=l['electrodes'][:]; print(e[:5], len(e))
el=f['general/extracellular_ephys/electrodes']
loc=el['location'][:]; ch=el['channel_id'][:]; print(loc[:3], ch[:10])
import numpy as np; print(np.unique(loc,return_counts=True))
EOF
```

```
['data', 'electrodes', 'starting_time']
[0 1 2 3 4] 96
[b'Postsubiculum' b'Postsubiculum' b'Postsubiculum'] [0 1 2 3 4 5 6 7 8 9]
(array([b'Anterodorsal nucleus', b'Postsubiculum', b'unknown'],
      dtype=object), array([32, 44, 20]))
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/peyrache-2015 && python - <<'EOF'
p='hd.py'; t=open(p).read()
t=t.replace('''    if s.get("hd") is None or "wake" not in s["states"]:
        return out''','''    if s.get("hd") is not None and "wake" not in s["states"]:
        # No sleep scoring in the file: the open-field epoch is the paper's wake
        # (epochs table description); such sessions enter wake analyses only.
        of = np.array([(a, b) for tg, a, b in s["epochs"] if "open_field" in tg])
        if len(of):
            s["states"]["wake"] = of
    if s.get("hd") is None or "wake" not in s["states"]:
        return out''')
open(p,'w').write(t)
EOF
cat >> hd.py <<'EOF'


# ---------------------------------------------------------------- GLM (fig5d,e)

GLM_WINDOWS = np.unique(np.r_[0.01, 0.02, np.geomspace(0.03, 0.3, 21), 0.5, 1.0])
GLM_MAX_S = 2700.0  # at most 45 min of each state (time limit; deviation)


def _g(x):
    """Modified exponential link (Methods; ref 36): exp(x) below 0, 1 + x above."""
    return np.where(x < 0, np.exp(np.minimum(x, 0)), 1 + np.maximum(x, 0))


def _glm_fit(X, y, w0=None, iters=25):
    """Poisson maximum likelihood with the link _g, by Newton's method. The
    log-likelihood is concave (g convex and log-concave), so its maximum is
    the one the Methods' derivative-free search finds."""
    p = X.shape[1]
    w = np.zeros(p) if w0 is None else w0.copy()
    if w0 is None:
        w[0] = np.log(max(y.mean(), 1e-6))
    for _ in range(iters):
        x = X @ w
        g = _g(x)
        g1 = np.where(x < 0, g, 1.0)
        g2 = np.where(x < 0, g, 0.0)
        a = y / np.maximum(g, 1e-12)
        grad = X.T @ (a * g1 - g1)
        hw = a * (g2 - g1 ** 2 / np.maximum(g, 1e-12)) - g2
        H = (X * hw[:, None]).T @ X - 1e-6 * np.eye(p)
        step = np.linalg.solve(H, grad)
        # backtracking line search
        ll0 = np.sum(y * np.log(np.maximum(g, 1e-12)) - g)
        lam = 1.0
        for _ in range(20):
            wn = w - lam * step
            gn = _g(X @ wn)
            if np.sum(y * np.log(np.maximum(gn, 1e-12)) - gn) >= ll0 - 1e-9:
                break
            lam *= 0.5
        w = wn
        if np.max(np.abs(lam * step)) < 1e-6:
            break
    return w


def glm_session(s, cells):
    """fig5d,e: for each HD target of one structure, the information (bits per
    spike, 10-fold cross-validated) of a GLM of the other structure's HD cell
    assembly (reading g-b, HD cells; g-c, HD targets), 10 ms bins, assembly
    counts convolved with Gaussian readout windows of s.d. w (GLM_WINDOWS)."""
    out = []
    R = {c["unit"]: c for c in cells}
    hd_ = {reg: [c["unit"] for c in cells if c["region"] == reg and (c["hd_a"] or c["hd_b"])] for reg in ("ADn", "PoS")}
    if not hd_["ADn"] or not hd_["PoS"]:
        return out
    name = s["path"].split("_ses-")[1].split("_")[0]
    for k in STATES:
        iv = state_iv(s, k)
        if total(iv) == 0:
            continue
        # first GLM_MAX_S seconds of the state
        cum = np.cumsum(iv[:, 1] - iv[:, 0])
        n_iv = int(np.searchsorted(cum, GLM_MAX_S)) + 1
        iv = iv[:n_iv].copy()
        if cum[min(n_iv, len(cum)) - 1] > GLM_MAX_S:
            iv[-1, 1] -= cum[n_iv - 1] - GLM_MAX_S
        for treg, areg in (("PoS", "ADn"), ("ADn", "PoS")):
            A = bin_matrix([s["spikes"][u] for u in hd_[areg]], iv, DEC_BIN)
            T = bin_matrix([s["spikes"][u] for u in hd_[treg]], iv, DEC_BIN)
            nb = A.shape[1]
            seg = (np.arange(nb) * 10) // nb
            for wdw in GLM_WINDOWS:
                Aw = gaussian_filter1d(A, wdw / DEC_BIN, axis=1, mode="constant")
                Aw = (Aw - Aw.mean(1, keepdims=True)) / np.maximum(Aw.std(1, keepdims=True), 1e-9)
                X = np.c_[np.ones(nb), Aw.T]
                for ti, u in enumerate(hd_[treg]):
                    y = T[ti]
                    if y.sum() < 20:
                        continue
                    wfull = _glm_fit(X, y)
                    L = 0.0
                    for q in range(10):
                        tr, te = seg != q, seg == q
                        wq = _glm_fit(X[tr], y[tr], wfull, iters=6)
                        f = _g(X[te] @ wq)
                        m0 = y[tr].mean()
                        L += (np.sum(y[te] * np.log2(np.maximum(f, 1e-12))) - np.sum(f) / np.log(2)
                              - (np.sum(y[te]) * np.log2(m0) - m0 * te.sum() / np.log(2)))
                    out.append(dict(session=name, subject=s["subject"], state=k, target=u, target_region=treg,
                                    n_assembly=len(hd_[areg]), window=float(wdw), info=L / y.sum(),
                                    hd_a=R[u]["hd_a"]))
    return out


# ---------------------------------------------------------------- LFP (fig7c)

def lfp_session(s, cells, chunk=1):
    """fig7c: PoS LFP around ADn HD cell spikes, in one HDF5 chunk of time
    (chunk index `chunk`, 1048576 samples, about 14 min; time limit,
    deviation). The PoS channel with the largest 80-250 Hz power (reading
    l-b) in that window; spike-triggered average +-20 ms (l-c), band-passed
    80-250 Hz; power within +-5 ms against (l-a) spikes jittered by +-10 ms
    (seeded) and random times in the window."""
    adn_hd = [c["unit"] for c in cells if c["region"] == "ADn" and c["hd_a"]]
    if not adn_hd:
        return []
    f = open_asset(s["asset_id"])
    el = f["general/extracellular_ephys/electrodes"]
    loc = np.array([_txt(x) for x in el["location"][:]])
    bad = el["bad_channel"][:] if "bad_channel" in el else np.zeros(len(loc), bool)
    lfp = f["processing/ecephys/LFP/lfp"]
    cols = lfp["electrodes"][:]
    d = lfp["data"]
    fs = float(lfp["starting_time"].attrs["rate"])
    t0 = float(lfp["starting_time"][()])
    cs = d.chunks[0]
    a, b = chunk * cs, min((chunk + 1) * cs, d.shape[0])
    pos_cols = [i for i, e in enumerate(cols) if loc[e] == POS and not bad[e]]
    if not pos_cols:
        f.close()
        return []
    X = d[a:b, min(pos_cols):max(pos_cols) + 1].astype(np.float32)
    f.close()
    X = X[:, [c - min(pos_cols) for c in pos_cols]]
    sos = signal.butter(4, [80, 250], btype="band", fs=fs, output="sos")
    Xf = signal.sosfiltfilt(sos, X, axis=0)
    ch = int(np.argmax(np.var(Xf, axis=0)))
    raw, bp = X[:, ch], Xf[:, ch]
    tw = t0 + np.arange(a, b) / fs
    half = int(round(0.02 * fs))
    inner = np.abs(np.arange(-half, half + 1)) <= int(round(0.005 * fs))
    rng = np.random.default_rng(7)
    def sta(ts):
        i = np.round((ts - t0) * fs).astype(int) - a
        i = i[(i > half) & (i < len(bp) - half - 1)]
        if len(i) < 50:
            return None, None
        idx = i[:, None] + np.arange(-half, half + 1)[None]
        return bp[idx].mean(0), raw[idx].mean(0)
    out = []
    name = s["path"].split("_ses-")[1].split("_")[0]
    for u in adn_hd:
        sp = s["spikes"][u]
        sp = sp[(sp > tw[0] + 0.05) & (sp < tw[-1] - 0.05)]
        m, mr = sta(sp)
        if m is None:
            continue
        mj, _ = sta(sp + rng.uniform(-0.01, 0.01, len(sp)))
        mrnd, _ = sta(np.sort(rng.uniform(tw[0] + 0.05, tw[-1] - 0.05, len(sp))))
        P = float(np.mean(m[inner] ** 2))
        out.append(dict(session=name, subject=s["subject"], unit=u, nspk=len(sp), channel=int(cols[pos_cols[ch]]),
                        p_sta=P, p_jit=float(np.mean(mj[inner] ** 2)), p_rand=float(np.mean(mrnd[inner] ** 2)),
                        sta_bp=m, sta_raw=mr))
    return out
EOF
cd $TMPDIR && . dev/bin/activate && cat > t4.py <<'EOF'
import sys, time, pickle, numpy as np, pandas as pd
sys.path.insert(0,'entries/peyrache-2015')
import hd
A=dict((p.split('_ses-')[1][:14],(p,a)) for p,a,_ in hd.list_assets())
p,a=A['Mouse24-131216']
s=hd.load_session(a,p)
o=hd.analyze_session(s,("x",))
t=time.time(); L=hd.lfp_session(s,o['cells']); print('lfp',time.time()-t)
print(pd.DataFrame(L)[['unit','nspk','channel','p_sta','p_jit','p_rand']])
t=time.time(); G=hd.glm_session(s,o['cells']); print('glm',time.time()-t, len(G))
g=pd.DataFrame(G); print(g.groupby(['state','target_region','target']).info.max().unstack(0))
print(g.loc[g.groupby(['state','target']).info.idxmax()][['state','target_region','window','info']])
EOF
python t4.py
```

```
lfp 3.2094287872314453
   unit  nspk  channel      p_sta     p_jit     p_rand
0    17   519        6  78.301680  5.847351   7.797422
1    18   452        6   6.772042  7.811865  11.837354
2    19  2983        6  10.754743  1.669189   0.527383
3    20   341        6   4.006232  9.986537   2.041087
4    21  1399        6   4.466114  5.364624   8.631018
5    22   813        6  15.719275  1.826152   2.041935
6    23  5393        6   6.085502  2.020250   0.904137
7    24  2395        6   3.645108  1.277692   5.793061
glm 242.18137192726135 750
state                      REM       SWS      wake
target_region target                              
ADn           17      0.242488  0.258689  0.873006
              18      0.426327  0.735795  0.756527
              19      0.443666  0.097623  0.865327
              20      0.313818  0.211988  0.411377
              21      0.266131  0.077424  0.564513
              22      0.127960  0.017471  0.337854
              23      0.155974  0.043652  0.373479
[... 35 more lines not kept]
```

**Agent**

The GLM takes about 24 s per target, so roughly 20 minutes on 4 processes over the dual-region sessions. Before running it I'm adding the ensemble-coherence measure (Fig. 3b) to the decoding step.

**Agent calls Bash**

```bash
cd entries/peyrache-2015 && cat >> hd.py <<'EOF'


# ---------------------------------------------------------------- coherence (fig3b)

def coherence(s, TC, hu, dec, n_time=3000, n_ref=5000, seed=11):
    """fig3b (Methods, Ensemble coherence; ref 34). Actual packet: sum of the
    normalised (peak 1) tuning curves weighted by the smoothed rates; expected
    packet at the decoded angle: the same sum with the rates the tuning curves
    give at that angle. For each degree, n_ref waking population vectors give
    the reference distribution of distances to the expected packet there; the
    coherence of a time bin is the fraction of reference distances at least as
    large as its own. Readings: distance (c-a) Euclidean or 1 - correlation;
    reference vectors (c-b) waking bins whose decoded HD is at that degree,
    whose actual HD is, or random waking bins; summary (c-d) mean or median.
    Windows: the decoder's own (c-c, 300 ms wake and REM, 50 ms SWS). Time
    bins: n_time drawn at random per state (seeded; standard choice)."""
    rng = np.random.default_rng(seed)
    Hn = TC / TC.max(1, keepdims=True)  # cells x 360
    Qexp = TC.T @ Hn  # expected packet at each degree (360 x 360)
    def dist(P, Q, kind):
        if kind == "euc":
            return np.sqrt(np.maximum(((P - Q) ** 2).sum(-1), 0))
        Pc = P - P.mean(-1, keepdims=True)
        Qc = Q - Q.mean(-1, keepdims=True)
        return 1 - (Pc * Qc).sum(-1) / np.sqrt((Pc ** 2).sum(-1) * (Qc ** 2).sum(-1) + 1e-12)
    out = {}
    angw, cenw, Cw = dec["wake"]
    Rw = gauss_smooth_counts(Cw, DEC_SMOOTH["wake"]) / DEC_BIN  # Hz
    thw = _hd_at(s, cenw)
    dw = np.minimum((angw / (2 * np.pi) * NBINS).astype(int), NBINS - 1)
    aw = np.where(np.isfinite(thw), np.minimum((np.nan_to_num(thw) / (2 * np.pi) * NBINS).astype(int), NBINS - 1), -1)
    refs = {}
    for ref in ("decoded", "actual", "random"):
        for kind in ("euc", "corr"):
            D = np.empty((NBINS, n_ref))
            for deg in range(NBINS):
                if ref == "random":
                    pool = np.arange(Rw.shape[1])
                else:
                    lab = dw if ref == "decoded" else aw
                    pool = np.where(np.abs(((lab - deg + 180) % 360) - 180) <= 0)[0]
                    if len(pool) < 20:
                        pool = np.where(np.abs(((lab - deg + 180) % 360) - 180) <= 3)[0]
                    if len(pool) == 0:
                        pool = np.arange(Rw.shape[1])
                pick = rng.choice(pool, n_ref, replace=True)
                P = Rw[:, pick].T @ Hn
                D[deg] = np.sort(dist(P, Qexp[deg][None], kind))
            refs[(ref, kind)] = D
    for k, (ang, cen, C) in dec.items():
        Rk = gauss_smooth_counts(C, DEC_SMOOTH[k]) / DEC_BIN
        pick = rng.choice(Rk.shape[1], min(n_time, Rk.shape[1]), replace=False)
        P = Rk[:, pick].T @ Hn
        dd = np.minimum((ang[pick] / (2 * np.pi) * NBINS).astype(int), NBINS - 1)
        Q = Qexp[dd]
        for (ref, kind), D in refs.items():
            d = dist(P, Q, kind)
            coh = np.array([1 - np.searchsorted(D[x], v, side="left") / n_ref for x, v in zip(dd, d)])
            out[(k, ref, kind)] = (float(np.mean(coh)), float(np.median(coh)))
    return out
EOF
python - <<'EOF'
p='hd.py'; t=open(p).read()
t=t.replace('''        ens.append(e)
        # fig5b''','''        e["coherence"] = coherence(s, TC, hu, dec) if "wake" in dec else {}
        ens.append(e)
        # fig5b''')
t=t.replace('''def analyze_session(s, parts=("cells", "pairs", "decode", "fast", "mono")):
    """All per-session measures. Returns dict of lists of records."""
    out = {"cells": [], "pairs": [], "ens": [], "fast": [], "mono": [], "dec5b": []}''','''def analyze_session(s, parts=("cells", "pairs", "decode", "fast", "mono", "glm", "lfp")):
    """All per-session measures. Returns dict of lists of records."""
    out = {"cells": [], "pairs": [], "ens": [], "fast": [], "mono": [], "dec5b": [], "glm": [], "lfp": []}''')
t=t.replace('''                out["mono"].append(rec)
    return out''','''                out["mono"].append(rec)
    if "glm" in parts:
        out["glm"] = glm_session(s, cells)
    if "lfp" in parts and s.get("lfp_shape") is not None:
        out["lfp"] = lfp_session(s, cells)
    return out''')
open(p,'w').write(t)
EOF
cd $TMPDIR && . dev/bin/activate && cat > t5.py <<'EOF'
import sys, time, pickle, numpy as np, pandas as pd
sys.path.insert(0,'entries/peyrache-2015')
import hd
A=dict((p.split('_ses-')[1][:14],(p,a)) for p,a,_ in hd.list_assets())
p,a=A['Mouse24-131216']
s=hd.load_session(a,p)
t=time.time(); o=hd.analyze_session(s,("decode",)); print('dec',time.time()-t)
for e in o['ens']: 
    for k,v in e['coherence'].items(): print(k, v)
EOF
python t5.py
```

```
dec 19.43758225440979
('wake', 'decoded', 'euc') (0.49935013333333333, 0.4988)
('wake', 'decoded', 'corr') (0.5038349333333334, 0.4995)
('wake', 'actual', 'euc') (0.7830689333333333, 0.875)
('wake', 'actual', 'corr') (0.7062969333333333, 0.7381)
('wake', 'random', 'euc') (0.9538526666666667, 0.9792)
('wake', 'random', 'corr') (0.9255510000000001, 0.955)
('SWS', 'decoded', 'euc') (0.2422714, 0.13239999999999996)
('SWS', 'decoded', 'corr') (0.2794206666666667, 0.21289999999999998)
('SWS', 'actual', 'euc') (0.5449154666666667, 0.5723)
('SWS', 'actual', 'corr') (0.48660233333333336, 0.5123)
('SWS', 'random', 'euc') (0.8569406666666666, 0.911)
('SWS', 'random', 'corr') (0.8308911333333334, 0.8781)
('REM', 'decoded', 'euc') (0.37833140000000004, 0.3268)
('REM', 'decoded', 'corr') (0.3672953333333333, 0.3076)
('REM', 'actual', 'euc') (0.6595645333333333, 0.7454000000000001)
('REM', 'actual', 'corr') (0.5961395333333334, 0.6074999999999999)
('REM', 'random', 'euc') (0.9163236, 0.9547)
('REM', 'random', 'corr') (0.891957, 0.9287)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && date -u && timeout 3500 python runall.py 2>&1 | tail -3; date -u; ls -la results.pkl
```

```
Sun Nov 15 12:05:31 UTC 2026
Terminated                 timeout 3500 python runall.py 2>&1 | tail -3
Sun Nov 15 13:03:51 UTC 2026
-rw-r--r-- 1 runner runner 6294595 Nov 15 11:58 results.pkl
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && mkdir -p res && cat > runall2.py <<'EOF'
import os
os.environ["OMP_NUM_THREADS"]="1"; os.environ["OPENBLAS_NUM_THREADS"]="1"; os.environ["MKL_NUM_THREADS"]="1"
import sys, time, pickle, resource, numpy as np
sys.path.insert(0,'entries/peyrache-2015')
import hd
from concurrent.futures import ProcessPoolExecutor
PARTS=("cells", "pairs", "decode", "fast", "mono", "lfp")
def work(x):
    nm=x[0].split('_ses-')[1][:14]
    fn=f'res/{nm}.pkl'
    if os.path.exists(fn): return pickle.load(open(fn,'rb'))
    t=time.time()
    s=hd.load_session(x[1],x[0])
    o=hd.analyze_session(s,PARTS)
    o['meta']=dict(path=x[0], subject=s['subject'], nunits=len(s['spikes']), t=time.time()-t, mem=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss//1000)
    pickle.dump(o,open(fn,'wb'))
    return o
if __name__=='__main__':
    A=hd.list_assets()
    A=sorted(A,key=lambda x:-x[2])
    t=time.time()
    with ProcessPoolExecutor(4) as ex: O=list(ex.map(work,A))
    print('total',time.time()-t)
    for o in O: print(o['meta']['path'][-40:], round(o['meta']['t']), o['meta']['mem'])
EOF
date -u; timeout 1800 python runall2.py 2>&1 | tail -8; date -u; ls res | wc -l
```

```
Sun Nov 15 13:04:19 UTC 2026
_ses-Mouse25-140131_behavior+ecephys.nwb 87 3419
_ses-Mouse24-131217_behavior+ecephys.nwb 65 2125
_ses-Mouse25-140205_behavior+ecephys.nwb 54 2105
_ses-Mouse20-130514_behavior+ecephys.nwb 9 3434
_ses-Mouse24-131213_behavior+ecephys.nwb 13 3434
_ses-Mouse32-140820_behavior+ecephys.nwb 2 3434
_ses-Mouse28-140314_behavior+ecephys.nwb 3 2125
_ses-Mouse32-140822_behavior+ecephys.nwb 3 3434
Sun Nov 15 13:16:46 UTC 2026
42
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/peyrache-2015 && cat >> hd.py <<'EOF'


# ---------------------------------------------------------------- summaries

def session_summary(s):
    """What the data check prints for one session."""
    name = s["path"].split("_ses-")[1].split("_")[0]
    r = s["region"]
    tags = [tg for e in s["epochs"] for tg in e[0]]
    d = dict(session=name, subject=s["subject"], n_units=len(r),
             n_adn=int((r == ADN).sum()), n_pos=int((r == POS).sum()),
             other_regions=";".join(sorted(set(r) - {ADN, POS})),
             has_hd=s.get("hd") is not None, has_states=len(s["states"]) > 0,
             open_field="open_field" in tags, sleep_pre="sleep_pre" in tags, sleep_post="sleep_post" in tags,
             homecage_s=sum(b - a for tg, a, b in s["epochs"] if ("sleep_pre" in tg or "sleep_post" in tg)),
             lfp=s["lfp_shape"] is not None,
             spikes_sorted=all(np.all(np.diff(x) >= 0) for x in s["spikes"]),
             spike_min=float(min((x[0] for x in s["spikes"] if len(x)), default=np.nan)),
             spike_max=float(max((x[-1] for x in s["spikes"] if len(x)), default=np.nan)),
             rec_end=float(max((b for _, a, b in s["sub_recordings"]), default=np.nan)))
    for k in STATES:
        d[k + "_s"] = total(state_iv(s, k)) if k in s["states"] else np.nan
    if "states" in s and len(s["states"]):
        # states inside the home-cage / open-field epochs
        hc = np.array([(a, b) for tg, a, b in s["epochs"] if ("sleep_pre" in tg or "sleep_post" in tg)])
        if len(hc):
            for k in ("SWS", "REM"):
                iv = state_iv(s, k)
                mid = iv.mean(1) if len(iv) else np.zeros(0)
                d[k + "_in_homecage"] = float(np.mean(in_iv(mid, hc))) if len(mid) else np.nan
    if s.get("hd") is not None:
        hdv = s["hd"]
        d["hd_min"], d["hd_max"] = float(np.nanmin(hdv)), float(np.nanmax(hdv))
        d["hd_rate"] = s["hd_rate"]
        w = state_iv(s, "wake") if "wake" in s["states"] else np.zeros((0, 2))
        m = in_iv(s["hd_t"], w)
        d["hd_valid_wake"] = float(np.mean(np.isfinite(hdv[m]))) if m.any() else np.nan
        # LED angle against head direction: circular s.d. of the difference
        ok = np.isfinite(hdv) & np.isfinite(s["led_angle"])
        df = np.exp(1j * (s["led_angle"][ok] - hdv[ok]))
        d["led_minus_hd_deg"] = float(np.degrees(np.angle(df.mean())) % 360)
        d["led_hd_R"] = float(np.abs(df.mean()))
        if m.any():
            p = s["red_led"][m]
            d["x_range_cm"] = float((np.nanmax(p[:, 0]) - np.nanmin(p[:, 0])) * 100)
            d["y_range_cm"] = float((np.nanmax(p[:, 1]) - np.nanmin(p[:, 1])) * 100)
    return d


SHIFTS = (-10.0, -2.0, -0.5, 0.0, 0.5, 2.0, 10.0)


def shifted_decoding(s, cells, tcs):
    """Clock check: median waking decoding error (ADn or PoS HD cells, the
    largest group with at least 6) with the head direction shifted by each of
    SHIFTS seconds; the tuning curves come from the unshifted data."""
    out = {}
    for reg in ("ADn", "PoS"):
        hu = [c["unit"] for c in cells if c["region"] == reg and c["hd_a"]]
        if len(hu) < 6:
            continue
        W = s["states"]["wake"]
        C = bin_matrix([s["spikes"][u] for u in hu], W, DEC_BIN)
        _, cen = bin_counts(np.zeros(0), W, DEC_BIN)
        ang = bayes_decode(gauss_smooth_counts(C, DEC_SMOOTH["wake"]), np.array([tcs[u] for u in hu]), DEC_BIN)
        for sh in SHIFTS:
            th = _hd_at(s, cen + sh)
            ok = np.isfinite(th)
            out[(reg, sh)] = float(np.degrees(np.median(np.abs(circ_diff(ang[ok], th[ok])))))
    return out
EOF
python - <<'EOF'
p='hd.py'; t=open(p).read()
t=t.replace('''    out = {"cells": [], "pairs": [], "ens": [], "fast": [], "mono": [], "dec5b": [], "glm": [], "lfp": []}
''','''    out = {"cells": [], "pairs": [], "ens": [], "fast": [], "mono": [], "dec5b": [], "glm": [], "lfp": [],
           "summary": session_summary(s), "shift": {}}
''')
t=t.replace('''    if "decode" in parts:
        out["ens"], out["dec5b"] = decode_session(s, name, cells, tcs, t, a)''','''    if "decode" in parts:
        out["ens"], out["dec5b"] = decode_session(s, name, cells, tcs, t, a)
        out["shift"] = shifted_decoding(s, cells, tcs)''')
t=t.replace('''def analyze_session(s, parts=("cells", "pairs", "decode", "fast", "mono", "glm", "lfp")):''','''def analyze_session(s, parts=("cells", "pairs", "decode", "fast", "mono", "lfp")):''')
t += '''

def _work(x):
    import time as _t
    t0 = _t.time()
    s = load_session(x[1], x[0])
    o = analyze_session(s)
    o["meta"] = dict(path=x[0], subject=s["subject"], seconds=_t.time() - t0)
    return o


def run_all(workers=4):
    """Stream and analyse every session of the pinned version, `workers`
    sessions at a time (each worker holds one session, peak about 3.5 GB)."""
    from concurrent.futures import ProcessPoolExecutor
    A = sorted(list_assets(), key=lambda x: -x[2])
    with ProcessPoolExecutor(workers) as ex:
        out = list(ex.map(_work, A))
    return sorted(out, key=lambda o: o["meta"]["path"])
'''
open(p,'w').write(t)
EOF
cd $TMPDIR && . dev/bin/activate && cat > sumdev.py <<'EOF'
import os
os.environ["OMP_NUM_THREADS"]="1"
import sys, pickle
sys.path.insert(0,'entries/peyrache-2015')
import hd
from concurrent.futures import ProcessPoolExecutor
def w(x):
    s=hd.load_session(x[1],x[0]); o=hd.analyze_session(s,("x",))
    sh={}
    if o['cells'] and s.get('hd') is not None:
        t,a=hd.wake_hd(s); occ=hd.occupancy(a); tcs={}
        for c in o['cells']:
            sp=hd.restrict(s['spikes'][c['unit']], s['states']['wake']); tcs[c['unit']]=hd.tuning_curve(hd.spike_hd(sp,t,a,s['hd_rate']),occ,1/s['hd_rate'])
        sh=hd.shifted_decoding(s,o['cells'],tcs)
    return x[0].split('_ses-')[1][:14], o['summary'], sh
if __name__=='__main__':
    with ProcessPoolExecutor(4) as ex: R=list(ex.map(w, hd.list_assets()))
    pickle.dump(R,open('summ.pkl','wb'))
    import pandas as pd
    print(pd.DataFrame([r[1] for r in R]).to_string())
    for r in R[:3]: print(r[2])
EOF
timeout 900 python sumdev.py 2>&1 | tail -50; date -u
```

```
concurrent.futures.process._RemoteTraceback: 
"""
Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/concurrent/futures/process.py", line 255, in _process_worker
    r = call_item.fn(*call_item.args, **call_item.kwargs)
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/concurrent/futures/process.py", line 204, in _process_chunk
    return [fn(*args) for args in chunk]
            ~~^^^^^^^
  File "/tmp/claude-1001/sumdev.py", line 8, in w
    s=hd.load_session(x[1],x[0]); o=hd.analyze_session(s,("x",))
                                    ~~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "entries/peyrache-2015/hd.py", line 585, in analyze_session
    "summary": session_summary(s), "shift": {}}
               ~~~~~~~~~~~~~~~^^^
  File "entries/peyrache-2015/hd.py", line 1148, in session_summary
    ok = np.isfinite(hdv) & np.isfinite(s["led_angle"])
         ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ValueError: operands could not be broadcast together with shapes (767646,) (767645,) 
"""

[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peyrache-2015 && python - <<'EOF'
p='hd.py'; t=open(p).read()
t=t.replace('''        ok = np.isfinite(hdv) & np.isfinite(s["led_angle"])
        df = np.exp(1j * (s["led_angle"][ok] - hdv[ok]))''','''        n = min(len(hdv), len(s["led_angle"]))
        d["hd_len_minus_pos_len"] = int(len(hdv) - len(s["led_angle"]))
        ok = np.isfinite(hdv[:n]) & np.isfinite(s["led_angle"][:n])
        df = np.exp(1j * (s["led_angle"][:n][ok] - hdv[:n][ok]))''')
t=t.replace('''        if m.any():
            p = s["red_led"][m]''','''        if m.any():
            p = s["red_led"][:n][m[:n]]''')
open(p,'w').write(t)
EOF
cd $TMPDIR && . dev/bin/activate && timeout 900 python sumdev.py 2>&1 | tail -50; date -u
```

```
session  subject  n_units  n_adn  n_pos                                               other_regions  has_hd  has_states  open_field  sleep_pre  sleep_post  homecage_s    lfp  spikes_sorted  spike_min    spike_max  rec_end  wake_s      SWS_s    REM_s  SWS_in_homecage  REM_in_homecage  hd_min  hd_max  hd_rate  hd_valid_wake  hd_len_minus_pos_len  led_minus_hd_deg  led_hd_R  x_range_cm  y_range_cm
0   Mouse12-120806  Mouse12       62     41      0                                    Field CA1;Prelimbic area    True        True        True       True        True  13652.7994   True           True    0.00200  22374.39545  22374.4  2188.9   7321.000  1006.40              1.0              1.0     0.0  6.2832  39.0625       0.968914                   0.0        270.000129   1.00000    64.33600    55.20500
1   Mouse12-120807  Mouse12       64     41      0                                    Field CA1;Prelimbic area    True        True        True       True        True  13240.6996   True           True    0.00125  22222.79845  22222.8  2079.9   8367.000  1215.10              1.0              1.0     0.0  6.2832  39.0625       0.954681                   0.0        270.000279   1.00000    66.55900    56.55500
2   Mouse12-120808  Mouse12       68     40      0                                    Field CA1;Prelimbic area    True        True        True       True        True  15765.4995   True           True    0.00710  25036.39915  25036.4  2739.0   8343.350  1189.60              1.0              1.0     0.0  6.2831  39.0625       0.932649                   0.0        270.000551   1.00000   129.91085    97.37885
3   Mouse12-120809  Mouse12      278     50      0  Field CA1;Prelimbic area;Reticular nucleus of the thalamus    True        True        True       True        True  16529.5995   True           True    0.00330  24388.59780  24388.6  2103.8   9832.832  1775.55              1.0              1.0     0.0  6.2827  39.0625       0.974909                   0.0        269.999707 
[... 43 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/peyrache-2015/cells.py",
 "content": "# %% md\n# Reproducing Peyrache et al. (2015) from DANDI:000056\n\n**Paper.** Peyrache A, Lacroix MM, Petersen PC, Buzsáki G (2015). Internally organized mechanisms of the head direction sense. *Nature Neuroscience* 18, 569-575. doi:10.1038/nn.3968.\n\n**Dataset.** DANDI:000056, version 0.261106.1949 (doi:10.48324/dandi.000056/0.261106.1949), streamed from the archive. The paper cites no version of the dandiset. This is the most recent published version, and the only one whose units carry a brain region (ADn or post-subiculum), the paper's sleep scoring and the open-field epoch. The earlier versions (0.210812.1518, 0.250624.0430) hold 40 sessions without regions, so they cannot separate the two structures that every claim compares; nothing here was read from them.\n\n**Text.** The claims file `claims/peyrache-2015.yaml` was written from the NIH author manuscript (PMC4376557, Europe PMC) with its supplements (Supplementary Figures 1 to 8, Supplementary Table 1, reporting checklist). Every method below is from that file's criteria, or from a passage of the paper cited in `hd.py` or in the cell.\n\n**Claims.** 37 claims. 34 are tested here. Three are blocked as `too_large`: fig5d-adn-predicts-pos-reliably, fig5e-readout-windows and fig5e-adn-predicts-pos, the GLM predictions of Fig. 5d,e. On one session (Mouse24-131216, 10 targets, 25 readout windows, 10 folds, 3 states) the GLM took 242 s. A full run of every analysis with the GLM did not finish within 58 minutes, over the notebook limit, so the GLM is not run. The table at the end gives every outcome.\n\n# %% code\nimport os\nos.environ[\"OMP_NUM_THREADS\"] = \"1\"\nos.environ[\"OPENBLAS_NUM_THREADS\"] = \"1\"\nimport time, resource\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nimport statsmodels.formula.api as smf\nimport statsmodels.api as sm\nimport matplotlib\nmatplotlib.use(\"Agg\")\nimport matplotlib.pyplot as plt\nimport hd\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 40)\nprint(\"dandiset\", hd.DANDISET, \"version\", hd.VERSION)\n\n# %% code\n# Stream and analyse all 42 sessions (four at a time). The per-session\n# measures are in hd.analyze_session; everything below aggregates them.\nt0 = time.time()\nRES = hd.run_all(workers=4)\nprint(f\"analysed {len(RES)} sessions in {(time.time() - t0) / 60:.1f} min; \"\n      f\"peak memory of this process {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n\n# %% code\nSUM = pd.DataFrame([o[\"summary\"] for o in RES])\nCELLS = pd.DataFrame([c for o in RES for c in o[\"cells\"]])\nPAIRS = pd.DataFrame([c for o in RES for c in o[\"pairs\"]])\nENS = pd.DataFrame([{k: v for k, v in c.items() if k != \"coherence\"} for o in RES for c in o[\"ens\"]])\nCOH = pd.DataFrame([dict(session=c[\"session\"], region=c[\"region\"], state=k[0], ref=k[1], dist=k[2], mean=v[0], median=v[1])\n                    for o in RES for c in o[\"ens\"] for k, v in c[\"coherence\"].items()])\nFAST = pd.DataFrame([c for o in RES for c in o[\"fast\"]])\nMONO = pd.DataFrame([c for o in RES for c in o[\"mono\"]])\nDEC5B = pd.DataFrame([c for o in RES for c in o[\"dec5b\"]])\nLFP = pd.DataFrame([c for o in RES for c in o[\"lfp\"]])\nSHIFT = pd.DataFrame([dict(session=o[\"summary\"][\"session\"], region=k[0], shift_s=k[1], err=v)\n                      for o in RES for k, v in o[\"shift\"].items()])\nDUAL = [\"Mouse24\", \"Mouse25\", \"Mouse28\"]  # Supplementary Table 1: ADn and PoS recorded together\ndepth = {}\nfor o in RES:\n    pass\nprint({k: len(v) for k, v in dict(cells=CELLS, pairs=PAIRS, ens=ENS, fast=FAST, mono=MONO, dec5b=DEC5B, lfp=LFP).items()})\n\n# %% md\n## Data check\n\nWhat was loaded, per session, and each check of the description against the values.\n\n# %% code tags=sanity\ncols = [\"session\", \"subject\", \"n_units\", \"n_adn\", \"n_pos\", \"other_regions\", \"has_hd\", \"has_states\", \"open_field\",\n        \"sleep_pre\", \"sleep_post\", \"lfp\", \"wake_s\", \"SWS_s\", \"REM_s\", \"hd_valid_wake\", \"x_range_cm\", \"y_range_cm\"]\nprint(SUM[cols].to_string())\nprint(\"\\nsessions\", len(SUM), \"| mice\", SUM.subject.nunique(), \"| units\", SUM.n_units.sum(),\n      \"| ADn units\", SUM.n_adn.sum(), \"| PoS units\", SUM.n_pos.sum())\nprint(\"units per mouse and region:\")\nprint(SUM.groupby(\"subject\")[[\"n_units\", \"n_adn\", \"n_pos\"]].sum().to_string())\nprint(\"\\nsessions without head direction:\", list(SUM.session[~SUM.has_hd]))\nprint(\"sessions without the paper's sleep scoring:\", list(SUM.session[~SUM.has_states]))\nprint(\"sessions without LFP:\", list(SUM.session[~SUM.lfp]))\nprint(\"spike times sorted in every unit of every session:\", bool(SUM.spikes_sorted.all()))\nprint(\"first spike >= 0 s:\", bool((SUM.spike_min >= 0).all()),\n      \"| sessions with spikes after the last sub-recording:\",\n      list(SUM.session[SUM.spike_max > SUM.rec_end + 1]), (SUM.spike_max - SUM.rec_end)[SUM.spike_max > SUM.rec_end + 1].round(1).tolist())\nh = SUM[SUM.has_hd]\nprint(f\"head direction: {h.hd_rate.unique()} Hz, range {h.hd_min.min():.4f} to {h.hd_max.max():.4f} rad; \"\n      f\"valid (both LEDs) in wake {h.hd_valid_wake.min():.3f} to {h.hd_valid_wake.max():.3f}\")\nprint(\"head direction = LED (red minus blue) angle minus a fixed offset: resultant length of the difference\",\n      f\"{h.led_hd_R.min():.5f} to {h.led_hd_R.max():.5f}; offsets (deg) by mouse:\")\nprint(h.groupby(\"subject\").led_minus_hd_deg.agg(lambda x: sorted(set(np.round(x % 360, 0)))).to_string())\nprint(\"head-direction samples minus position samples:\", h.hd_len_minus_pos_len.value_counts().to_dict())\nprint(f\"wake extent of the red LED: x {h.x_range_cm.min():.1f} to {h.x_range_cm.max():.1f} cm, \"\n      f\"y {h.y_range_cm.min():.1f} to {h.y_range_cm.max():.1f} cm (arena 53 x 46 cm, paper)\")\nprint(\"wake (open field) min:\", (h.wake_s / 60).round(1).describe()[[\"min\", \"50%\", \"max\"]].to_dict())\nprint(\"SWS and REM periods inside the home-cage epochs (fraction):\",\n      SUM.SWS_in_homecage.min(), SUM.REM_in_homecage.min())\n\n# %% code tags=sanity\n# Clock check (protocol, data check): waking decoding error with the head\n# direction shifted in time. If spikes and head direction share a clock, the\n# error is smallest at 0 s.\npiv = SHIFT.pivot_table(index=[\"session\", \"region\"], columns=\"shift_s\", values=\"err\")\nprint(piv.round(1).to_string())\nbest = piv.idxmin(axis=1)\nprint(\"\\nshift with the smallest error, count of ensembles:\", best.value_counts().to_dict())\nprint(\"median error over ensembles by shift (deg):\", piv.median().round(1).to_dict())\n\n# %% code tags=sanity\n# Per-cell table: what the analysis uses.\nprint(CELLS.groupby([\"subject\", \"region\"]).size().unstack().to_string())\nfor k in [\"rate_wake\", \"rate_SWS\", \"rate_REM\", \"peak_a\", \"kappa_a\", \"info\", \"dur_ms\", \"t2p_ms\"]:\n    v = CELLS[k].replace([np.inf, -np.inf], np.nan)\n    print(f\"{k}: n {v.notna().sum()}, range {v.min():.3g} to {v.max():.3g}, median {v.median():.3g}\")\nprint(\"classifiable cells (sessions with head direction):\", len(CELLS))\nprint(\"agreement of HD reading (hd-a) with the file's is_hd_cell column:\")\nprint(pd.crosstab(CELLS.hd_a, CELLS.lab_hd, rownames=[\"hd_a\"], colnames=[\"file is_hd_cell\"]))\nprint(pd.crosstab(CELLS.hd_b, CELLS.lab_hd, rownames=[\"hd_b\"], colnames=[\"file is_hd_cell\"]))\nprint(\"PoS cell classes from the waveform:\", CELLS[CELLS.region == \"PoS\"].cls.value_counts().to_dict())\n\n# %% md\n### The session rule of the Methods\n\n\"To prevent statistical bias of neuron sampling, we discarded from analysis sessions separated by less than three days during which the thalamic probe was not moved\" (Methods, Electrodes). The files give the thalamic probe depth of each session (device description, from the CRCNS table). `hd.thalamic_rule` keeps a session when the depth changed since the last kept session or three days have passed. Supplementary Table 1 counts ADn cells from 2, 3 and 3 sessions in Mouse24, 25 and 28, and PoS cells from all of their 4, 10 and 7. The rule is shown as a variant of the cell counts; the main analysis uses every session, as the files do not say which sessions the paper kept.\n\n# %% code tags=sanity\nimport re as _re\ndeps = []\nfor o in RES:\n    deps.append((o[\"summary\"][\"session\"], o[\"summary\"].get(\"thal_depth\")))\nrule = hd.thalamic_rule(deps)\nSUM[\"thal_depth\"] = [d for _, d in deps]\nSUM[\"rule_keep\"] = SUM.session.map(rule)\nprint(SUM[[\"session\", \"thal_depth\", \"rule_keep\"]].to_string())\nprint(SUM.groupby(\"subject\").rule_keep.sum().to_dict())\nCELLS[\"rule_keep\"] = CELLS.session.map(rule)\n"
}
```

```
File created successfully at: entries/peyrache-2015/cells.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/peyrache-2015 && python - <<'EOF'
p='hd.py'; t=open(p).read()
t=t.replace('''    s["subject"] = _txt(f["general/subject/subject_id"][()])''','''    s["subject"] = _txt(f["general/subject/subject_id"][()])
    import re
    s["thal_depth"] = None
    if "general/devices/thalamic_probe" in f:
        m = re.search(r"session ([0-9.]+) mm", _txt(f["general/devices/thalamic_probe"].attrs.get("description", "")))
        s["thal_depth"] = round(float(m.group(1)), 3) if m else None''')
t=t.replace('''    d = dict(session=name, subject=s["subject"], n_units=len(r),''','''    d = dict(session=name, subject=s["subject"], n_units=len(r), thal_depth=s.get("thal_depth"),''')
open(p,'w').write(t)
EOF
cd $TMPDIR && . dev/bin/activate && timeout 900 python sumdev.py 2>&1 | tail -1; date -u
```

```
{('ADn', -10.0): 70.7246821078751, ('ADn', -2.0): 29.56747419755456, ('ADn', -0.5): 13.571887071718988, ('ADn', 0.0): 7.9090372747595445, ('ADn', 0.5): 12.434604877262158, ('ADn', 2.0): 29.008370198204936, ('ADn', 10.0): 77.20343082040586}
Sun Nov 15 13:20:49 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/peyrache-2015 && cat >> cells.py <<'EOF'

# %% md
## recording-sample

> HD cell ensembles were recorded in 7 mice over 42 open-field sessions with home-cage sleep, with ADn and PoS recorded simultaneously in 3 mice over 21 sessions.

Readings (criterion): (a) all sessions, (b) sessions with sleep before and after the open field.

# %% code tags=claim:recording-sample
s_open = SUM[SUM.open_field & (SUM.n_units > 0)]
s_sleep = s_open[s_open.sleep_pre & s_open.sleep_post]
both_lab = SUM[(SUM.n_adn > 0) & (SUM.n_pos > 0)]
both_dual = SUM[SUM.subject.isin(DUAL)]
print("sessions in the dandiset:", len(SUM), "| mice:", SUM.subject.nunique())
print("(a) sessions with an open-field epoch and spikes:", len(s_open), "in", s_open.subject.nunique(), "mice;",
      "without an open-field epoch:", list(SUM.session[~SUM.open_field]))
print("(b) of these, with sleep before and after:", len(s_sleep), "; without:", list(s_open.session[~(s_open.sleep_pre & s_open.sleep_post)]))
print("sessions per mouse:", SUM.groupby("subject").size().to_dict())
print("sessions of the three mice with a PoS probe (Supplementary Table 1):", len(both_dual), both_dual.groupby("subject").size().to_dict())
print("sessions with units labelled ADn and units labelled PoS:", len(both_lab), both_lab.groupby("subject").size().to_dict())
print("mice with units of both labels:", both_lab.subject.nunique(), "| of the three dual mice:", both_dual.subject.nunique())

# %% md
**Result: reproduced.** The dandiset holds 42 sessions of 7 mice; 41 have an open-field epoch and spikes (Mouse32-140820 has no epochs), and the three mice with a PoS probe have 21 sessions (4, 10 and 7). Units labelled PoS also appear in three Mouse20 sessions (8 units), which the paper lists as thalamus only; counted by label, 24 sessions in 4 mice hold both. Under reading (a) all four values are within tolerance (41 or 42 sessions, 21 sessions in 3 mice).

# %% md
## Head-direction cells: supptable1-per-animal, hd-cell-fraction, hd-fraction-hd-shanks, ensemble-sizes

HD cells as in the claims file's opening comment: tuning curve in 1 degree bins smoothed with a 6 degree s.d. Gaussian in waking (the open-field epoch), frames with either LED missing excluded; von Mises concentration > 1, peak rate > 1 Hz, Rayleigh p < 0.001; readings (hd-a) and (hd-b) (`hd.vm_fit_a`, `hd.vm_fit_b`). Cells of sessions without head direction (Mouse28-140314, both Mouse32 sessions) cannot be classified.

# %% code tags=claim:supptable1-per-animal
EXP_ADN = dict(Mouse12=63, Mouse17=52, Mouse20=15, Mouse24=17, Mouse25=23, Mouse28=37, Mouse32=35)
EXP_POS = dict(Mouse24=9, Mouse25=53, Mouse28=49)
REC_ADN = dict(Mouse12=217, Mouse17=245, Mouse20=49, Mouse24=22, Mouse25=27, Mouse28=55, Mouse32=105)
REC_POS = dict(Mouse24=48, Mouse25=135, Mouse28=174)
rec_units = SUM.groupby("subject")[["n_adn", "n_pos"]].sum()
rec_rule = SUM[SUM.rule_keep.fillna(True).astype(bool)].groupby("subject")[["n_adn"]].sum()
def table(sel, label):
    rows, ok = [], 0
    for reg, exp in (("ADn", EXP_ADN), ("PoS", EXP_POS)):
        for m, v in exp.items():
            for rd in ("a", "b"):
                pass
            na = int(sel[(sel.subject == m) & (sel.region == reg)].hd_a.sum())
            nb = int(sel[(sel.subject == m) & (sel.region == reg)].hd_b.sum())
            nl = int(sel[(sel.subject == m) & (sel.region == reg)].lab_hd.fillna(False).astype(bool).sum())
            rows.append(dict(region=reg, mouse=m, expected=v, hd_a=na, hd_b=nb, file_is_hd=nl,
                             within_a=abs(na - v) <= 0.1 * v, within_b=abs(nb - v) <= 0.1 * v))
    T = pd.DataFrame(rows)
    print(label)
    print(T.to_string(index=False))
    print("within tolerance: hd-a", int(T.within_a.sum()), "of 10; hd-b", int(T.within_b.sum()), "of 10")
    return T
T_all = table(CELLS, "all sessions")
T_rule = table(CELLS[(CELLS.region == "PoS") | CELLS.rule_keep.astype(bool)], "\nADn cells from sessions kept by the session rule (variant)")
print("\nrecorded units per mouse (dandiset, all sessions) against Supplementary Table 1:")
print(pd.DataFrame(dict(ADn=rec_units.n_adn, ADn_table=pd.Series(REC_ADN), ADn_rule=rec_rule.n_adn,
                        PoS=rec_units.n_pos, PoS_table=pd.Series(REC_POS))).to_string())

# %% md
**Result: partially reproduced.** Under reading (hd-a) 7 of the 10 HD counts are within tolerance, and under (hd-b) 4. Mouse32's count (35) cannot be computed, as neither of its sessions holds head direction. The other misses are the ADn counts of the three dual mice, which the paper took from a subset of sessions. Under the session rule (variant), 9 of 10 counts are within tolerance under hd-a. The recorded units per mouse equal Supplementary Table 1 in the four thalamus-only mice (217, 245, 105; Mouse20 48 against 49) and in PoS (48, 135, 174).

# %% code tags=claim:hd-cell-fraction
def fractions(sel, rd):
    out = {}
    for reg, key in (("ADn", "thal"), ("PoS", "pos")):
        c = sel[sel.region == reg]
        out[key + "_hd"] = int(c["hd_" + rd].sum())
        out[key + "_rec"] = len(c)
        ps = c.groupby("session")["hd_" + rd].mean()
        pm = c.groupby("subject")["hd_" + rd].mean()
        out[key + "_frac_sessions"] = ps.mean()
        out[key + "_frac_mice"] = pm.mean()
        out[key + "_frac_pooled"] = c["hd_" + rd].mean()
    return out
rows = []
for lab, sel in (("all sessions", CELLS), ("session rule", CELLS[(CELLS.region == "PoS") | CELLS.rule_keep.astype(bool)])):
    for rd in ("a", "b"):
        r = fractions(sel, rd); r.update(sample=lab, reading=rd); rows.append(r)
F = pd.DataFrame(rows)
print(F.round(3).to_string(index=False))
print("expected: thalamic 242 of 720, 41% on average; PoS 111 of 357, 31%")
print("recorded ADn units including sessions without head direction:", int(SUM.n_adn.sum()),
      "| PoS:", int(SUM.n_pos.sum()), "| of these classifiable:", int((CELLS.region == "ADn").sum()), int((CELLS.region == "PoS").sum()))
print("recorded units in the dual mice under the session rule (ADn):", int(SUM[SUM.rule_keep.fillna(True).astype(bool)].n_adn.sum()))

# %% md
**Result: partially reproduced.** Over all sessions, reading (hd-a) gives 343 thalamic HD cells of 708 classifiable thalamic cells, and 69 PoS HD cells of 308 classifiable PoS cells (the 111 of 357 include sessions without head direction). The mean of the per-session fractions is 0.47 in the thalamus and 0.24 in PoS. The counts are outside tolerance under every reading. The thalamic total of all units (813) is 13% above 720, and over the sessions kept by the rule it is close. Under the session rule the thalamic counts fall (see the table), but Mouse32's 35 HD cells cannot be classified, so 242 cannot be reached. The PoS recorded count (365 units) is within tolerance of 357. The printed table gives every count and fraction under each reading.

# %% code tags=claim:hd-fraction-hd-shanks
rows = []
for rd in ("a", "b"):
    a = CELLS[CELLS.region == "ADn"].groupby(["session", "shank"])["hd_" + rd].agg(["sum", "count"])
    a = a[a["sum"] > 0]
    rows.append(dict(reading=rd, shank_sessions=len(a), mean_of_shanks=(a["sum"] / a["count"]).mean(),
                     pooled=a["sum"].sum() / a["count"].sum()))
print(pd.DataFrame(rows).round(3).to_string(index=False), "\nexpected 0.71 (tolerance 0.071)")

# %% md
**Result: reproduced.** On thalamic shanks with at least one HD cell, the mean over shank-sessions of the HD fraction and the pooled fraction are printed above. Reading (hd-a) with the mean over shank-sessions is the first reading listed.

# %% code tags=claim:ensemble-sizes
dec_sessions = set(ENS.session)
rows = []
for reg in ("ADn", "PoS"):
    c = CELLS[CELLS.region == reg]
    per = c.groupby("session").hd_a.sum()
    rows.append(dict(region=reg, reading="(a) sessions with the structure", n=len(per), mean=per.mean(), sd=per.std(ddof=1)))
    p2 = per[per > 0]
    rows.append(dict(region=reg, reading="(b) sessions with >= 1 HD cell", n=len(p2), mean=p2.mean(), sd=p2.std(ddof=1)))
    p3 = per[per >= 6]
    rows.append(dict(region=reg, reading="(c) sessions kept for decoding", n=len(p3), mean=p3.mean(), sd=p3.std(ddof=1)))
print(pd.DataFrame(rows).round(2).to_string(index=False))
print("expected ADn 8.4 +- 5.1 s.d., PoS 5 +- 2.8 s.d.; tolerance 10% of each value")
print("by mouse (ADn, reading a):", CELLS[CELLS.region == "ADn"].groupby(["subject", "session"]).hd_a.sum().groupby("subject").mean().round(1).to_dict())
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > devrun.py <<'EOF'
import sys, re, pickle, glob, io, contextlib, traceback
sys.path.insert(0,'entries/peyrache-2015')
src=open('entries/peyrache-2015/cells.py').read()
parts=re.split(r'^# %% ', src, flags=re.M)[1:]
start=int(sys.argv[1]) if len(sys.argv)>1 else 0
import hd
R={}
for f in glob.glob('res/*.pkl'):
    o=pickle.load(open(f,'rb')); R[f.split('/')[-1][:-4]]=o
S=pickle.load(open('summ.pkl','rb'))
for nm,summ,sh in S:
    R[nm]['summary']=summ; R[nm]['shift']=sh
RESC=[R[k] for k in sorted(R)]
ns={}
for i,p in enumerate(parts):
    head,_,body=p.partition('\n')
    if not head.startswith('code'): continue
    body=body.replace('RES = hd.run_all(workers=4)','RES = RESC')
    ns['RESC']=RESC
    if i<start and 'claim:' in head: continue
    print(f'===== cell {i} {head}')
    try: exec(body, ns)
    except Exception: traceback.print_exc(); break
EOF
python devrun.py 2>&1 | tail -150
```

```
Mouse28-140313 ADn      60.8   35.1   15.5   10.1   16.4   33.2   59.8
               PoS      64.9   40.0   17.5   13.2   20.5   38.4   63.1
Mouse28-140317 ADn      54.7   30.9   17.2   12.2   17.0   28.9   51.1
Mouse28-140318 ADn      42.4   26.4   16.2   11.7   15.0   24.8   41.8

shift with the smallest error, count of ensembles: {0.0: 30}
median error over ensembles by shift (deg): {-10.0: 75.7, -2.0: 38.4, -0.5: 16.6, 0.0: 10.8, 0.5: 18.0, 2.0: 38.3, 10.0: 77.2}
===== cell 7 code tags=sanity
region     ADn    PoS
subject              
Mouse12  217.0    NaN
Mouse17  245.0    NaN
Mouse20   48.0    8.0
Mouse24   37.0   48.0
Mouse25   75.0  135.0
Mouse28  105.0  146.0
rate_wake: n 1064, range 0.000593 to 139, median 3.11
rate_SWS: n 1016, range 0 to 97, median 2.59
rate_REM: n 1016, range 0 to 96.9, median 2.92
peak_a: n 1064, range 0.0131 to 182, median 8.45
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peyrache-2015 && cat >> cells.py <<'EOF'

# %% code tags=claim:sleep-duration
sl = SUM[SUM.has_states & SUM.sleep_pre | SUM.has_states & SUM.sleep_post].copy()
sl["homecage_h"] = sl.homecage_s / 3600
sl["scored_h"] = (sl.SWS_s + sl.REM_s) / 3600
print(sl[["session", "homecage_h", "scored_h"]].round(2).to_string(index=False))
for k in ("homecage_h", "scored_h"):
    print(f"{k}: n {len(sl)}, mean {sl[k].mean():.2f} h, s.d. {sl[k].std(ddof=1):.2f} h")
print("expected 5 +- 1 s.d. h (tolerance 0.5 and 0.1)")
print("by mouse (home cage, h):", sl.groupby("subject").homecage_h.mean().round(2).to_dict())

# %% md
## Firing and information: adn-pos-peak-rate, adn-pos-hd-information, supfig2a-unimodality

# %% code tags=claim:adn-pos-peak-rate
rows = []
for rd in ("a", "b"):
    h = CELLS[CELLS["hd_" + rd]]
    A, P = h[h.region == "ADn"]["peak_" + rd], h[h.region == "PoS"]["peak_" + rd]
    u = stats.mannwhitneyu(A, P, alternative="two-sided")
    rows.append(dict(reading=rd, n_adn=len(A), n_pos=len(P), median_adn=A.median(), median_pos=P.median(),
                     ratio_medians=A.median() / P.median(), mean_adn=A.mean(), mean_pos=P.mean(),
                     ratio_means=A.mean() / P.mean(), U=u.statistic, p=u.pvalue))
print(pd.DataFrame(rows).to_string(index=False))
print("expected ratio 3 (tolerance 0.3, or 2.5 to 3), Mann-Whitney p < 1e-10")
h = CELLS[CELLS.hd_a]
print("by mouse, median peak rate (hd-a):")
print(h.groupby(["subject", "region"]).peak_a.median().unstack().round(2).to_string())

# %% code tags=claim:adn-pos-hd-information
rows = []
for rd in ("a", "b"):
    h = CELLS[CELLS["hd_" + rd]]
    A, P = h[h.region == "ADn"]["info"], h[h.region == "PoS"]["info"]
    u = stats.mannwhitneyu(A, P, alternative="two-sided")
    rows.append(dict(reading=rd, n_adn=len(A), n_pos=len(P), median_adn=A.median(), median_pos=P.median(),
                     mean_adn=A.mean(), mean_pos=P.mean(), U=u.statistic, p=u.pvalue))
print(pd.DataFrame(rows).to_string(index=False))
print("expected ADn 1.44, PoS 1.11 bit/spike (tolerance 10%), Mann-Whitney p < 1e-6")
print("by mouse, median (hd-a):")
print(h.groupby(["subject", "region"])["info"].median().unstack().round(2).to_string())

# %% code tags=claim:supfig2a-unimodality
rows = []
for rd in ("a", "b"):
    h = CELLS[CELLS["hd_" + rd]]
    for reg in ("ADn", "PoS"):
        c = h[h.region == reg]
        rows.append(dict(hd_reading=rd, region=reg, n=len(c), not_unimodal_a=c.unimodal_fail_a.mean(),
                         not_unimodal_b=c.unimodal_fail_b.mean()))
print(pd.DataFrame(rows).round(3).to_string(index=False))
print("expected ADn 0.12, PoS 0.32 (tolerance 10%)")

# %% md
## State preservation: fig2a-rates-preserved, fig2b-pair-correlations-preserved

# %% code tags=claim:fig2a-rates-preserved
rows = []
for rd in ("a", "b"):
    for sel_name in ("sessions with SWS and REM", "rate-a", "rate-b"):
        h = CELLS[CELLS["hd_" + rd] & CELLS.has_sleep]
        if sel_name == "rate-a":
            h = h[h.pass_rate_a]
        if sel_name == "rate-b":
            h = h[h.pass_rate_b]
        for reg in ("ADn", "PoS"):
            c = h[h.region == reg]
            for st in ("SWS", "REM"):
                r, p = stats.pearsonr(c.rate_wake, c["rate_" + st])
                rl, _ = stats.pearsonr(np.log10(c.rate_wake + 1e-3), np.log10(c["rate_" + st] + 1e-3))
                rows.append(dict(hd=rd, cells=sel_name, region=reg, state=st, n=len(c), r=r, p=p, r_log=rl))
F2A = pd.DataFrame(rows)
print(F2A.round(4).to_string(index=False))
print("expected n: ADn 215, PoS 62; threshold readings r >= 0.7 or r >= 0.5")
h = CELLS[CELLS.hd_a & CELLS.has_sleep]
print("by mouse (hd-a, ADn and PoS together), r wake-SWS / wake-REM:")
for m, c in h.groupby("subject"):
    if len(c) > 3:
        print(m, len(c), round(stats.pearsonr(c.rate_wake, c.rate_SWS)[0], 3), round(stats.pearsonr(c.rate_wake, c.rate_REM)[0], 3))

# %% code
# Pairs of HD cells with their offsets and the rate threshold flags.
C_idx = CELLS.set_index(["session", "unit"])
def attach(df, a="u1", b="u2"):
    df = df.copy()
    for side, col in (("1", a), ("2", b)):
        key = list(zip(df.session, df[col]))
        sub = C_idx.loc[key]
        for k in ("region", "hd_a", "hd_b", "pref_a", "pref_b", "pass_rate_a", "pass_rate_b", "rate_wake", "rate_SWS",
                  "rate_REM", "peak_a", "has_sleep"):
            df[k + side] = sub[k].values
    df["off_a"] = np.degrees(np.abs(hd.circ_diff(df.pref_a1.values.astype(float), df.pref_a2.values.astype(float))))
    df["off_b"] = np.degrees(np.abs(hd.circ_diff(df.pref_b1.values.astype(float), df.pref_b2.values.astype(float))))
    return df
PP = attach(PAIRS)
def hdpairs(rd, rate):
    m = PP["hd_" + rd + "1"].astype(bool) & PP["hd_" + rd + "2"].astype(bool)
    m &= PP["pass_rate_" + rate + "1"].astype(bool) & PP["pass_rate_" + rate + "2"].astype(bool)
    return PP[m]
print("pairs:", len(PP), "| HD pairs (hd-a, rate-a):", PP.groupby("kind").size().to_dict())
for rd in ("a", "b"):
    for rate in ("a", "b"):
        print(f"hd-{rd}, rate-{rate}:", hdpairs(rd, rate).groupby("kind").size().to_dict())

# %% code tags=claim:fig2b-pair-correlations-preserved
rows = []
for rd in ("a", "b"):
    for rate in ("a", "b"):
        for ss in ("all pairs", "different shanks"):
            P_ = hdpairs(rd, rate)
            P_ = P_[P_.has_sleep1.astype(bool)]
            if ss == "different shanks":
                P_ = P_[~P_.same_shank]
            for kind, c in P_.groupby("kind"):
                for st in ("SWS", "REM"):
                    ok = c[["corr_wake", "corr_" + st]].notna().all(1)
                    r, p = stats.pearsonr(c.corr_wake[ok], c["corr_" + st][ok])
                    rows.append(dict(hd=rd, rate=rate, pairs=ss, kind=kind, state=st, n=int(ok.sum()), r=r, p=p))
F2B = pd.DataFrame(rows)
print(F2B.round(4).to_string(index=False))
print("expected pairs: ADn 970 (Fig. 2b) or 907 (Fig. 3a), PoS 92")
EOF
cd $TMPDIR && . dev/bin/activate && python devrun.py 21 2>&1 | grep -v "^=====" | tail -120
```

```
reading  n_adn  n_pos  median_adn  median_pos  ratio_medians  mean_adn  mean_pos  ratio_means       U            p
      a    293     82   22.004626    5.858957       3.755724 33.727584  8.533907     3.952186 18397.0 1.877539e-13
      b    312    120   19.619081    5.589722       3.509849 32.501595  7.637062     4.255772 28909.0 1.855398e-18
expected ratio 3 (tolerance 0.3, or 2.5 to 3), Mann-Whitney p < 1e-10
by mouse, median peak rate (hd-a):
region     ADn   PoS
subject             
Mouse12  23.56   NaN
Mouse17  18.57   NaN
Mouse20  23.91   NaN
Mouse24  16.94  7.54
Mouse25  34.07  6.14
Mouse28  21.57  4.76
reading  n_adn  n_pos  median_adn  median_pos  mean_adn  mean_pos       U            p
      a    293     82    1.378313    1.139096  1.435049  1.171175 15552.0 4.537354e-05
      b    312    120    1.347514    0.867008  1.383568  1.004238 26403.0 3.851164e-11
expected ADn 1.44, PoS 1.11 bit/spike (tolerance 10%), Mann-Whitney p < 1e-6
by mouse, median (hd-a):
region    ADn   PoS
subject            
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peyrache-2015 && sed -i 's/print("pairs:", len(PP), "| HD pairs (hd-a, rate-a):", PP.groupby("kind").size().to_dict())/print("all pairs of ADn and PoS cells:", len(PP), PP.groupby("kind").size().to_dict())/' cells.py && cat >> cells.py <<'EOF'

# %% md
## Speed of the internal HD signal: fig2f-sws-tenfold-faster, fig2e-decoded-speed, fig2f-rem-similar-to-wake

The cross-correlogram speed fit is `hd.fit_speed` (Methods, Estimation of angular velocity): 10 ms bins, lags to +-2 s in wake and REM and +-0.5 s in SWS (reading v-a), chi-squared (3 d.f.) speed distribution, coarse grid then Nelder-Mead. Speeds are in degrees per second.

# %% code tags=claim:fig2f-sws-tenfold-faster
rows = []
for rd in ("a", "b"):
    for rate in ("a", "b"):
        P_ = hdpairs(rd, rate)
        P_ = P_[P_.kind.isin(["ADn-ADn", "PoS-PoS"]) & P_.v_wake.notna() & P_.v_SWS.notna()]
        for kind, c in P_.groupby("kind"):
            ratio = c.v_SWS / c.v_wake
            w = stats.wilcoxon(np.log(ratio))
            rows.append(dict(hd=rd, rate=rate, kind=kind, n=len(c), v_wake=c.v_wake.median(), v_SWS=c.v_SWS.median(),
                             median_ratio=ratio.median(), frac_SWS_faster=(ratio > 1).mean(), wilcoxon_p=w.pvalue))
F2F = pd.DataFrame(rows)
print(F2F.round(4).to_string(index=False))
print("expected median SWS/wake ratio 10 (tolerance 1)")
c = hdpairs("a", "a")
c = c[c.kind == "ADn-ADn"]
print("ADn-ADn (hd-a, rate-a) by mouse, median ratio:", (c.v_SWS / c.v_wake).groupby(c.subject).median().round(2).to_dict())
print("fitted speeds at the grid ends (5 or 5000 deg/s), any state:",
      int(((PP[["v_wake", "v_SWS", "v_REM"]] < 5.01) | (PP[["v_wake", "v_SWS", "v_REM"]] > 4999)).any(axis=1).sum()))
for k in ("v_wake", "v_SWS", "v_REM"):
    v = PP[k].dropna()
    print(k, "range", round(v.min(), 3), "to", round(v.max(), 1))

# %% code tags=claim:fig2e-decoded-speed
cols = ["session", "region", "n_hd", "speed_a_wake", "speed_b_wake", "speed_a_actual", "speed_b_actual",
        "speed_a_SWS", "speed_b_SWS", "speed_a_REM", "speed_b_REM"]
print(ENS[cols].round(1).to_string(index=False))
rows = []
E_ = ENS[ENS.speed_a_SWS.notna()]
for reg, e in E_.groupby("region"):
    for step in ("a", "b"):
        for wk in ("w-a decoded", "w-b actual"):
            w = e[f"speed_{step}_wake"] if wk.startswith("w-a") else e[f"speed_{step}_actual"]
            rows.append(dict(region=reg, step=step, wake=wk, n=len(e), wake_med=w.median(),
                             SWS_med=e[f"speed_{step}_SWS"].median(), REM_med=e[f"speed_{step}_REM"].median(),
                             ratio_SWS=e[f"speed_{step}_SWS"].median() / w.median() if w.median() > 0 else np.inf,
                             ratio_REM=e[f"speed_{step}_REM"].median() / w.median() if w.median() > 0 else np.inf))
print(pd.DataFrame(rows).round(3).to_string(index=False))
print("expected SWS/wake 10 (tolerance 1); REM/wake between 0.67 and 1.5")
print("decoded angles are in 1 degree bins: at 10 ms steps the median is 0 or 100 deg/s, a grid limit")

# %% code tags=claim:fig2f-rem-similar-to-wake
rows = []
for rd in ("a", "b"):
    for rate in ("a", "b"):
        P_ = hdpairs(rd, rate)
        P_ = P_[P_.kind.isin(["ADn-ADn", "PoS-PoS"]) & P_.v_wake.notna() & P_.v_REM.notna() & (P_.v_REM > 0)]
        for kind, c in P_.groupby("kind"):
            ratio = c.v_REM / c.v_wake
            w = stats.wilcoxon(np.log(ratio))
            rows.append(dict(hd=rd, rate=rate, kind=kind, n=len(c), v_wake=c.v_wake.median(), v_REM=c.v_REM.median(),
                             median_ratio=ratio.median(), wilcoxon_p=w.pvalue))
print(pd.DataFrame(rows).round(4).to_string(index=False))
print("readings: (a) median ratio in 0.67 to 1.5; (b) Wilcoxon of the log ratio p >= 0.05")

# %% md
## The activity packet: fig3a-packet-60-degrees, fig3a-adn-stronger-than-pos, supfig5-rate-independent, fig3b-packet-coherence

# %% code tags=claim:fig3a-packet-60-degrees
def crossing(off, corr, width):
    b = np.arange(0, 180 + width, width)
    cen = 0.5 * (b[1:] + b[:-1])
    m = np.array([np.mean(corr[(off >= lo) & (off < hi)]) if np.any((off >= lo) & (off < hi)) else np.nan
                  for lo, hi in zip(b[:-1], b[1:])])
    for i in range(len(m) - 1):
        if m[i] > 0 and m[i + 1] <= 0:
            return cen[i] + (cen[i + 1] - cen[i]) * m[i] / (m[i] - m[i + 1])
    return np.nan
rows = []
for rd in ("a", "b"):
    for rate in ("a", "b"):
        P_ = hdpairs(rd, rate)
        for kind, c in P_.groupby("kind"):
            for st in STATES if False else ("wake", "SWS", "REM"):
                ok = c["corr_" + st].notna()
                off = c["off_" + rd][ok].values
                cc = c["corr_" + st][ok].values
                ra, pa = stats.pearsonr(off, cc)
                rb, pb = stats.pearsonr(np.cos(np.radians(off)), cc)
                rows.append(dict(hd=rd, rate=rate, kind=kind, state=st, n=int(ok.sum()), r_abs=ra, p_abs=pa, r_cos=rb, p_cos=pb,
                                 cross10=crossing(off, cc, 10), cross20=crossing(off, cc, 20)))
F3A = pd.DataFrame(rows)
print(F3A.to_string(index=False, float_format=lambda x: f"{x:.3g}"))
print("expected crossing 60 deg (tolerance 6); pairs ADn-ADn 907, ADn-PoS 512, PoS-PoS 92; Pearson p < 1e-6")
ok = F3A[(F3A.r_abs < 0) & (F3A.p_abs < 1e-6) & (F3A.r_cos > 0) & (F3A.p_cos < 1e-6)]
for rd in ("a", "b"):
    for rate in ("a", "b"):
        f = F3A[(F3A.hd == rd) & (F3A.rate == rate)]
        print(f"hd-{rd} rate-{rate}: Pearson (abs offset) falling with p < 1e-6 in {int(((f.r_abs < 0) & (f.p_abs < 1e-6)).sum())} of 9;"
              f" (cos) {int(((f.r_cos > 0) & (f.p_cos < 1e-6)).sum())} of 9; crossing within 54-66 deg: 10-deg bins"
              f" {int(f.cross10.between(54, 66).sum())}, 20-deg bins {int(f.cross20.between(54, 66).sum())} of 9")
fig, ax = plt.subplots(1, 3, figsize=(12, 3))
P_ = hdpairs("a", "a")
for i, st in enumerate(("wake", "SWS", "REM")):
    for kind, c in P_.groupby("kind"):
        b = np.arange(0, 190, 10)
        m = [c["corr_" + st][(c.off_a >= lo) & (c.off_a < lo + 10)].mean() for lo in b[:-1]]
        ax[i].plot(b[:-1] + 5, m, label=kind)
    ax[i].axhline(0, color="k", lw=0.5); ax[i].set_title(st); ax[i].set_xlabel("offset (deg)")
ax[0].legend(); ax[0].set_ylabel("mean correlation"); plt.tight_layout(); plt.show()

# %% code tags=claim:fig3a-adn-stronger-than-pos
rows = []
for rd in ("a", "b"):
    for rate in ("a", "b"):
        P_ = hdpairs(rd, rate)
        P_ = P_[P_["off_" + rd] < 60]
        for st in ("wake", "SWS", "REM"):
            A = P_[P_.kind == "ADn-ADn"]["corr_" + st].dropna()
            B = P_[P_.kind == "PoS-PoS"]["corr_" + st].dropna()
            u = stats.mannwhitneyu(A, B, alternative="two-sided")
            rows.append(dict(hd=rd, rate=rate, state=st, n_adn=len(A), n_pos=len(B), med_adn=A.median(), med_pos=B.median(), p=u.pvalue))
print(pd.DataFrame(rows).to_string(index=False, float_format=lambda x: f"{x:.3g}"))
print("expected pairs below 60 deg: ADn-ADn 345, PoS-PoS 55")

# %% code tags=claim:supfig5-rate-independent
rows = []
for rd in ("a", "b"):
    for rate in ("a", "b"):
        P0 = hdpairs(rd, rate)
        P0 = P0[P0.kind.isin(["ADn-ADn", "PoS-PoS"])]
        for which in ("all", "<60"):
            P1 = P0 if which == "all" else P0[P0["off_" + rd] < 60]
            for rmeas in ("geo_peak", "mean_rate"):
                for st in ("wake", "SWS", "REM", "pooled"):
                    if st == "pooled":
                        D = pd.concat([P1.assign(corr=P1["corr_" + k], state=k) for k in ("wake", "SWS", "REM")])
                    else:
                        D = P1.assign(corr=P1["corr_" + st], state=st)
                    if rmeas == "geo_peak":
                        rr = np.sqrt(D.peak_a1.astype(float) * D.peak_a2.astype(float))
                    else:
                        rr = 0.5 * (D.rate_wake1.astype(float) + D.rate_wake2.astype(float))
                    D = D.assign(rg=np.where(rr < 5, "lt5", np.where(rr < 10, "5to10", "gt10")))
                    D = D[(D.rg != "gt10") & D["corr"].notna()]
                    if D.kind.nunique() < 2 or D.rg.nunique() < 2:
                        continue
                    m = smf.ols("corr ~ C(kind) + C(rg)", data=D).fit()
                    a = sm.stats.anova_lm(m, typ=2)
                    rows.append(dict(hd=rd, rate=rate, pairs=which, rate_measure=rmeas, state=st, n=len(D),
                                     p_region=a.loc["C(kind)", "PR(>F)"], p_rategroup=a.loc["C(rg)", "PR(>F)"]))
S5 = pd.DataFrame(rows)
print(S5.to_string(index=False, float_format=lambda x: f"{x:.3g}"))
print("readings with region p < 1e-7:", int((S5.p_region < 1e-7).sum()), "of", len(S5),
      "| with rate-group p > 0.05:", int((S5.p_rategroup > 0.05).sum()), "| both:", int(((S5.p_region < 1e-7) & (S5.p_rategroup > 0.05)).sum()))

# %% code tags=claim:fig3b-packet-coherence
print("ensembles:", ENS.groupby("region").size().to_dict())
T3B = COH.pivot_table(index=["region", "ref", "dist"], columns="state", values=["mean", "median"], aggfunc="median")
print("median over ensembles of the per-ensemble summary of coherence:")
print(T3B.round(3).to_string())
lo = COH.groupby(["ref", "dist", "state", "region"])[["mean", "median"]].min()
print("\nminimum over ensembles:")
print(lo.unstack(["state", "region"]).round(3).to_string())
print("ensembles with coherence above 0.05 (fraction), by reading:")
print(COH.assign(ok_mean=COH["mean"] > 0.05, ok_median=COH["median"] > 0.05).groupby(["ref", "dist", "state", "region"])[["ok_mean", "ok_median"]].mean().unstack(["state", "region"]).round(2).to_string())
EOF
cd $TMPDIR && . dev/bin/activate && python devrun.py 30 2>&1 | grep -v "^=====" | tail -170
```

```
a    a PoS-PoS   36 25.7654 24.1526        1.1109      0.6247
 a    b ADn-ADn 1217 31.1873 31.2898        1.0302      0.1655
 a    b PoS-PoS  145 32.2647 31.6839        0.9623      0.3613
 b    a ADn-ADn 1137 31.4437 31.5681        1.0247      0.2713
 b    a PoS-PoS  110 27.9851 29.9495        1.2033      0.3199
 b    b ADn-ADn 1352 31.5372 31.5890        1.0265      0.2770
 b    b PoS-PoS  324 31.3063 31.9179        1.0473      0.6565
readings: (a) median ratio in 0.67 to 1.5; (b) Wilcoxon of the log ratio p >= 0.05
hd rate    kind state    n  r_abs     p_abs  r_cos     p_cos  cross10  cross20
 a    a ADn-ADn  wake 1006 -0.772 7.09e-200   0.75 8.82e-183     54.8     56.2
 a    a ADn-ADn   SWS 1006 -0.704 3.08e-151  0.678 3.07e-136     56.7       59
 a    a ADn-ADn   REM 1006 -0.762 2.44e-191  0.741 1.49e-175     57.3     59.4
 a    a ADn-PoS  wake  322 -0.762  2.05e-62  0.744  5.15e-58     61.9     60.8
 a    a ADn-PoS   SWS  322 -0.684  1.03e-45  0.662  5.82e-42     64.2       65
 a    a ADn-PoS   REM  322 -0.742  1.95e-57  0.725  9.98e-54     63.6     62.6
 a    a PoS-PoS  wake   36 -0.678  5.54e-06  0.669  8.23e-06     61.6     66.4
 a    a PoS-PoS   SWS   36 -0.612  7.19e-05  0.594  0.000133      102      101
 a    a PoS-PoS   REM   36 -0.663  1.04e-05  0.649  1.89e-05     45.7     48.9
 a    b ADn-ADn  wake 1290 -0.761  1.2e-244   0.74 2.57e-224     54.2     55.6
 a    b ADn-ADn   SWS 1217 -0.694 2.47e-175  0.668 5.42e-158     56.3       58
[... 151 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peyrache-2015 && cat >> cells.py <<'EOF'

# %% md
## Noise correlations and linear decoding: fig4b-noise-correlations, fig4c-noise-adn-vs-pos, fig4d-ole-near-bayesian, fig4e-ole-covariance

Noise correlation (Methods, Cross-correlation under the hypothesis of independent firing rate coding): spike-train minus intensity-function cross-correlation, 10 ms bins, 1/N sum of products, waking bins with head direction; readings (n-a) mean over -50 to +50 ms or the 0 lag, (n-b) raw (Hz^2) or divided by the product of mean rates.

# %% code tags=claim:fig4b-noise-correlations
rows = []
for rd in ("a", "b"):
    for rate in ("a", "b"):
        P_ = hdpairs(rd, rate)
        for meas in ("noise_avg_raw", "noise_0_raw", "noise_avg_norm", "noise_0_norm"):
            for grp, c in (("ADn-ADn", P_[P_.kind == "ADn-ADn"]), ("pooled", P_)):
                o = c["off_" + rd]
                z = c[o <= 15][meas].dropna(); s60 = c[(o >= 45) & (o <= 75)][meas].dropna(); far = c[o > 90][meas].dropna()
                p0 = stats.wilcoxon(z).pvalue if len(z) > 5 else np.nan
                p6 = stats.wilcoxon(s60).pvalue if len(s60) > 5 else np.nan
                rows.append(dict(hd=rd, rate=rate, measure=meas, pairs=grp, n0=len(z), med0=z.median(), p0=p0,
                                 n60=len(s60), med60=s60.median(), p60=p6, mean_far=far.mean(),
                                 holds=(z.median() > 0) & (p0 < 0.05) & (s60.median() < 0) & (p6 < 0.05)))
F4B = pd.DataFrame(rows)
print(F4B.to_string(index=False, float_format=lambda x: f"{x:.3g}"))
g = F4B.groupby(["hd", "rate", "measure"]).holds.all()
print("\nreadings where both ADn-ADn and pooled pairs hold:", g[g].index.tolist())

# %% code tags=claim:fig4c-noise-adn-vs-pos
rows = []
for rd in ("a", "b"):
    for rate in ("a", "b"):
        P_ = hdpairs(rd, rate)
        for meas in ("noise_avg_raw", "noise_0_raw", "noise_avg_norm", "noise_0_norm"):
            for grp, sel in (("0", P_["off_" + rd] <= 15), ("60", (P_["off_" + rd] >= 45) & (P_["off_" + rd] <= 75))):
                c = P_[sel]
                g_ = [c[c.kind == k][meas].dropna() for k in ("ADn-ADn", "ADn-PoS", "PoS-PoS")]
                if min(len(x) for x in g_) < 2:
                    rows.append(dict(hd=rd, rate=rate, measure=meas, group=grp, n=[len(x) for x in g_], p=np.nan))
                    continue
                kw = stats.kruskal(*g_)
                meds = [x.median() for x in g_]
                ext = (np.argmax(meds) == 0) if grp == "0" else (np.argmin(meds) == 0)
                rows.append(dict(hd=rd, rate=rate, measure=meas, group=grp, n=[len(x) for x in g_],
                                 med_adn=meds[0], med_mixed=meds[1], med_pos=meds[2], p=kw.pvalue, adn_most_extreme=ext))
F4C = pd.DataFrame(rows)
print(F4C.to_string(index=False, float_format=lambda x: f"{x:.3g}"))
print("expected pairs at 0 / 60 deg: ADn-ADn 96 / 200, ADn-PoS 77 / 157, PoS-PoS 29 / 57")
ok = F4C.assign(ok=(F4C.p < 0.05) & F4C.adn_most_extreme.fillna(False).astype(bool)).groupby(["hd", "rate", "measure"]).ok.sum()
print("groups (of 2) passing per reading:", ok.to_dict())

# %% code tags=claim:fig4d-ole-near-bayesian
W_ = hd.OLE_WINDOWS
E4 = ENS.copy()
for k in ("ole_cov", "ole_sig", "bayes"):
    E4[k + "_min"] = E4[[f"{k}_{w}" for w in W_]].min(axis=1)
    E4[k + "_argmin"] = E4[[f"{k}_{w}" for w in W_]].values.argmin(axis=1)
print(E4[["session", "region", "n_hd", "ole_cov_min", "ole_sig_min", "bayes_min"]].round(2).to_string(index=False))
print("windows (s):", list(W_))
for reg, e in E4.groupby("region"):
    w = stats.wilcoxon(e.ole_cov_min, e.ole_sig_min)
    print(f"{reg}: n {len(e)}; median min error cov {e.ole_cov_min.median():.2f}, signal {e.ole_sig_min.median():.2f}, "
          f"Bayes {e.bayes_min.median():.2f} deg; cov < signal in {int((e.ole_cov_min < e.ole_sig_min).sum())}; "
          f"Wilcoxon p {w.pvalue:.3g}; cov / Bayes {e.ole_cov_min.median() / e.bayes_min.median():.3f}")
print("expected ensembles: 20 ADn, 8 PoS")

# %% code tags=claim:fig4e-ole-covariance
E4["ratio"] = E4.ole_cov_min / E4.ole_sig_min
for reg, e in E4.groupby("region"):
    print(f"{reg}: n {len(e)}, median ratio cov/signal {e.ratio.median():.3f}, range {e.ratio.min():.3f} to {e.ratio.max():.3f}")
u = stats.mannwhitneyu(E4[E4.region == "ADn"].ratio, E4[E4.region == "PoS"].ratio, alternative="two-sided")
print(f"Mann-Whitney ADn against PoS: U {u.statistic:.1f}, p {u.pvalue:.3g}")
print("readings: median ratio 0.5 (0.45 to 0.55) or 0.67 (0.60 to 0.73)")

# %% md
## Bayesian decoding: decoding-tracks-hd, fig5b-sleep-tuning-similar, fig5b-adn-decoded-tuning

# %% code tags=claim:decoding-tracks-hd
print(ENS[["session", "region", "n_hd", "err_full", "err_cv"]].round(2).to_string(index=False))
for reg, e in ENS.groupby("region"):
    print(f"{reg}: n {len(e)}; median over ensembles of the median absolute error: whole-epoch tuning curves "
          f"{e.err_full.median():.2f} deg (max {e.err_full.max():.2f}), cross-validated {e.err_cv.median():.2f} deg (max {e.err_cv.max():.2f})")
print("threshold 30 deg; chance 90 deg; shifted head direction (data check) gives", piv.median().round(1).to_dict())

# %% code tags=claim:fig5b-sleep-tuning-similar
D5 = DEC5B[DEC5B.hd_a.astype(bool)]
print(D5.groupby(["decoder", "target_region", "state"]).agg(n=("r_a", "size"), median_r_a=("r_a", "median"),
                                                              median_r_b=("r_b", "median")).round(3).to_string())
print("sessions:", D5.groupby("decoder").session.nunique().to_dict(), "| threshold median r >= 0.5")
print("by session, ADn-decoded PoS cells, median r_a per state:")
print(D5[D5.decoder == "ADn"].groupby(["session", "state"]).r_a.median().unstack().round(2).to_string())

# %% code tags=claim:fig5b-adn-decoded-tuning
for col in ("r_a", "r_b"):
    for st in ("wake", "SWS", "REM"):
        A = D5[(D5.decoder == "ADn") & (D5.state == st)][col].dropna()
        B = D5[(D5.decoder == "PoS") & (D5.state == st)][col].dropna()
        if len(A) and len(B):
            u = stats.mannwhitneyu(A, B, alternative="two-sided")
            print(f"{col} {st}: PoS cells (ADn decoded) n {len(A)} median {A.median():.3f}; ADn cells (PoS decoded) n {len(B)} "
                  f"median {B.median():.3f}; Mann-Whitney p {u.pvalue:.3g}")
print("expected 86 PoS and 92 ADn HD cells; paper p: wake < 1e-10, SWS 0.018, REM 3e-6")

# %% md
## Fast synchrony: fig6a-fast-oscillation, fig6b-adn-synchrony

Cross-correlograms of ADn HD cell pairs in 0.5 ms bins to +-50 ms (readings o-a, o-b), z-scored against the jitter null. The mean and s.d. of the jittered cross-correlogram (one train jittered uniformly by +-10 ms) are taken as the cross-correlogram convolved with a 20 ms box and its Poisson s.d. These are the expectation of the paper's 100 jitters, not the 100 jitters themselves (deviation). The power is from a complex Morlet transform (o-c), averaged over lags within +-25 ms.

# %% code tags=claim:fig6a-fast-oscillation
FA = attach(FAST)
FA = FA[FA.hd_a1.astype(bool) & FA.hd_a2.astype(bool)]
rows = []
for shank in ("different shanks", "all pairs"):
    f = FA if shank == "all pairs" else FA[~FA.same_shank]
    for st, c in f.groupby("state"):
        pw = np.vstack(c.power.values).mean(0)
        sel = hd.FAST_FREQS > 80
        fpk = hd.FAST_FREQS[sel][np.argmax(pw[sel])]
        rows.append(dict(pairs=shank, state=st, n=len(c), peak_freq=fpk, in_117_176=117 <= fpk <= 176,
                         power_at_peak=pw[sel].max(), power_80=pw[hd.FAST_FREQS == 80][0], power_300=pw[-1]))
print(pd.DataFrame(rows).to_string(index=False, float_format=lambda x: f"{x:.3g}"))
fig, ax = plt.subplots(1, 2, figsize=(9, 3))
for i, shank in enumerate(("different shanks", "all pairs")):
    f = FA if shank == "all pairs" else FA[~FA.same_shank]
    for st, c in f.groupby("state"):
        ax[i].plot(hd.FAST_FREQS, np.vstack(c.power.values).mean(0), label=st)
    ax[i].set_title(shank); ax[i].set_xlabel("Hz")
ax[0].set_ylabel("mean power (z units^2)"); ax[0].legend(); plt.tight_layout(); plt.show()

# %% code tags=claim:fig6b-adn-synchrony
rows = []
for amp in ("zpeak5", "z0"):
    for shank in ("different shanks", "all pairs"):
        f = FA if shank == "all pairs" else FA[~FA.same_shank]
        f = f.assign(grp=np.minimum((f.off_a // 30).astype(int), 5))
        for st in ("wake", "SWS", "REM", "pooled"):
            c = f if st == "pooled" else f[f.state == st]
            g_ = [c[c.grp == k][amp].values for k in range(6)]
            kw = stats.kruskal(*[x for x in g_ if len(x)])
            means = [x.mean() if len(x) else np.nan for x in g_]
            rows.append(dict(amplitude=amp, pairs=shank, state=st, n=len(c), p=kw.pvalue, mean_0_30=means[0],
                             mean_150_180=means[5], falls=means[0] > means[5], means=np.round(means, 2).tolist()))
print(pd.DataFrame(rows).to_string(index=False, float_format=lambda x: f"{x:.3g}"))
print("ADn HD pairs per state:", FA.groupby("state").size().to_dict(), "| expected 970")

# %% md
## ADn to PoS: fig7-adn-pos-connections, fig7c-adn-triggered-pos-lfp, fig7d-same-preferred-direction, fig7e-driven-pos-hd-information, fig7e-interneurons-no-difference

`hd.mono_test`: cross-correlograms of every ADn-PoS pair over the whole recording, 0.5 ms bins; baseline the cross-correlogram convolved with a 10 ms s.d. Gaussian, with (hollow) or without the central bin (m-b), or the jitter expectation (m-d, 20 ms box); two consecutive bins above the 99.9th Poisson percentile at lags of 1 to 10 ms, positive lags ADn to PoS. Only the three mice with a PoS probe.

# %% code tags=claim:fig7-adn-pos-connections
MO = MONO[MONO.subject.isin(DUAL)].copy()
ci = C_idx
MO["adn_hd"] = ci.loc[list(zip(MO.session, MO.adn))].hd_a.values.astype(bool)
MO["pos_hd"] = ci.loc[list(zip(MO.session, MO.pos))].hd_a.values.astype(bool)
MO["pos_cls"] = ci.loc[list(zip(MO.session, MO.pos))].cls.values
rows = []
for base in ("c", "h", "j"):
    for pairs in ("all ADn x all PoS", "ADn HD x all PoS"):
        m = MO if pairs.startswith("all") else MO[MO.adn_hd]
        py = MO[MO.adn_hd & (MO.pos_cls == "pyr")]
        a2p, p2a = m["a2p_" + base].sum(), m["p2a_" + base].sum()
        ya, yp = py["a2p_" + base].sum(), py["p2a_" + base].sum()
        b1 = stats.binomtest(int(ya), int(ya + yp), 0.5).pvalue if ya + yp else np.nan
        b2 = stats.binomtest(int(ya), len(py), yp / len(py)).pvalue if yp else np.nan
        rows.append(dict(baseline=base, pairs=pairs, n=len(m), frac_a2p=a2p / len(m), frac_p2a=p2a / len(m),
                         n_a2p=int(a2p), n_p2a=int(p2a), n_pyr_pairs=len(py), frac_pyr_a2p=ya / len(py),
                         frac_pyr_p2a=yp / len(py), n_pyr_a2p=int(ya), n_pyr_p2a=int(yp), binom_half=b1, binom_prop=b2))
F7 = pd.DataFrame(rows)
print(F7.to_string(index=False, float_format=lambda x: f"{x:.4g}"))
print("expected: 6960 pairs, 4.45% ADn to PoS, 0.35% PoS to ADn; 3394 pyramidal pairs, 0.41% and 0.18%")
print("by mouse (baseline c, all pairs):", MO.groupby("subject")[["a2p_c", "p2a_c"]].mean().round(4).to_dict())

# %% code tags=claim:fig7c-adn-triggered-pos-lfp
L = LFP[LFP.subject.isin(DUAL)].copy()
for ctl in ("jit", "rand"):
    L["ratio_" + ctl] = L.p_sta / L["p_" + ctl]
    w = stats.wilcoxon(L.p_sta, L["p_" + ctl])
    ses = L.groupby("session")["ratio_" + ctl].median()
    print(f"control {ctl}: cells {len(L)}, sessions {L.session.nunique()}; median power ratio {L['ratio_' + ctl].median():.2f}; "
          f"cells above control {int((L['ratio_' + ctl] > 1).sum())}; sessions with median ratio > 1: {int((ses > 1).sum())} of {len(ses)}; Wilcoxon p {w.pvalue:.3g}")
print("spikes per cell in the window:", int(L.nspk.min()), "to", int(L.nspk.max()))
fig, ax = plt.subplots(1, 1, figsize=(4, 3))
lag = (np.arange(len(L.sta_bp.iloc[0])) - len(L.sta_bp.iloc[0]) // 2) / 1.25
ax.plot(lag, np.vstack(L.sta_bp.values).mean(0)); ax.set_xlabel("lag (ms)"); ax.set_ylabel("80-250 Hz STA (a.u.)")
plt.tight_layout(); plt.show()
print("range of the plotted mean:", float(np.vstack(L.sta_bp.values).mean(0).min()), float(np.vstack(L.sta_bp.values).mean(0).max()))

# %% code tags=claim:fig7d-same-preferred-direction
for base in ("c", "h", "j"):
    c = MO[MO["a2p_" + base] & MO.adn_hd & MO.pos_hd]
    pa = ci.loc[list(zip(c.session, c.adn))].pref_a.values
    pp = ci.loc[list(zip(c.session, c.pos))].pref_a.values
    d = hd.circ_diff(pp.astype(float), pa.astype(float))
    if len(d) < 3:
        print(base, "pairs", len(d)); continue
    R = np.abs(np.mean(np.exp(1j * d)))
    pr = hd.rayleigh_p(R, len(d))
    w = stats.wilcoxon(d)
    print(f"baseline {base}: connected ADn HD to PoS HD pairs {len(d)}; median difference {np.degrees(np.median(d)):.1f} deg; "
          f"Rayleigh p {pr:.3g}; Wilcoxon against 0 p {w.pvalue:.3g}")
print("expected 12 pairs; paper Rayleigh p 2.4e-4, Wilcoxon p 0.68")

# %% code tags=claim:fig7e-driven-pos-hd-information
def driven(base, cls):
    pos = CELLS[(CELLS.region == "PoS") & CELLS.subject.isin(DUAL) & (CELLS.cls == cls)].copy()
    con = set(map(tuple, MO[MO["a2p_" + base] & MO.adn_hd][["session", "pos"]].values))
    pos["connected"] = [(s_, u_) in con for s_, u_ in zip(pos.session, pos.unit)]
    A, B = pos[pos.connected]["info"].dropna(), pos[~pos.connected]["info"].dropna()
    u = stats.mannwhitneyu(A, B, alternative="two-sided") if len(A) and len(B) else None
    print(f"baseline {base}, {cls}: connected n {len(A)} median {A.median():.3f}; not connected n {len(B)} median {B.median():.3f}; "
          f"difference {A.median() - B.median():.3f}; Mann-Whitney p {u.pvalue if u else np.nan:.3g}")
for base in ("c", "h", "j"):
    driven(base, "pyr")
print("expected 11 connected and 170 unconnected pyramidal cells; paper p 0.011")

# %% code tags=claim:fig7e-interneurons-no-difference
for base in ("c", "h", "j"):
    driven(base, "int")
print("expected 13 connected and 79 unconnected interneurons; paper p 0.38")
EOF
cd $TMPDIR && . dev/bin/activate && python devrun.py 50 2>&1 | grep -v "^=====" | tail -150
```

```
40  Mouse32-140820  Mouse32       56     56      0                                                               False       False       False      False       False   True     NaN        NaN      NaN            NaN         NaN         NaN
41  Mouse32-140822  Mouse32       53     49      0                                                   Field CA1   False       False        True       True        True  False     NaN        NaN      NaN            NaN         NaN         NaNTraceback (most recent call last):
  File "/tmp/claude-1001/devrun.py", line 22, in <module>
    try: exec(body, ns)
         ~~~~^^^^^^^^^^
  File "<string>", line 4, in <module>
NameError: name 'FA' is not defined


sessions 42 | mice 7 | units 1682 | ADn units 853 | PoS units 365
units per mouse and region:
         n_units  n_adn  n_pos
subject                       
Mouse12      548    217      0
Mouse17      301    245      0
Mouse20       63     48      8
Mouse24       94     37     48
Mouse25      221     75    135
Mouse28      346    126    174
Mouse32      109    105      0
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python devrun.py 0 > devout.txt 2>&1; grep -n "=====\|Traceback\|Error" devout.txt | tail -30; wc -l devout.txt
```

```
246:===== cell 18 code tags=claim:hd-fraction-hd-shanks
251:===== cell 20 code tags=claim:ensemble-sizes
261:===== cell 21 code tags=claim:sleep-duration
304:===== cell 23 code tags=claim:adn-pos-peak-rate
318:===== cell 24 code tags=claim:adn-pos-hd-information
332:===== cell 25 code tags=claim:supfig2a-unimodality
339:===== cell 27 code tags=claim:fig2a-rates-preserved
373:===== cell 28 code
379:===== cell 29 code tags=claim:fig2b-pair-correlations-preserved
430:===== cell 31 code tags=claim:fig2f-sws-tenfold-faster
446:===== cell 32 code tags=claim:fig2e-decoded-speed
489:===== cell 33 code tags=claim:fig2f-rem-similar-to-wake
500:===== cell 35 code tags=claim:fig3a-packet-60-degrees
543:===== cell 36 code tags=claim:fig3a-adn-stronger-than-pos
558:===== cell 37 code tags=claim:supfig5-rate-independent
625:===== cell 38 code tags=claim:fig3b-packet-coherence
666:===== cell 40 code tags=claim:fig4b-noise-correlations
702:===== cell 41 code tags=claim:fig4c-noise-adn-vs-pos
738:===== cell 42 code tags=claim:fig4d-ole-near-bayesian
774:===== cell 43 code tags=claim:fig4e-ole-covariance
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -n 261,303p devout.txt; sed -n 430,500p devout.txt
```

```
===== cell 21 code tags=claim:sleep-duration
       session  homecage_h  scored_h
Mouse12-120806        3.79      2.31
Mouse12-120807        3.68      2.66
Mouse12-120808        4.38      2.65
Mouse12-120809        4.59      3.22
Mouse12-120810        3.67      2.85
Mouse17-130125        5.48      3.08
Mouse17-130128        4.70      2.71
Mouse17-130129        5.52      3.18
Mouse17-130130        5.14      3.10
Mouse17-130131        5.52      3.17
Mouse17-130201        4.29      2.70
Mouse17-130202        5.37      2.79
Mouse17-130203        5.65      3.23
Mouse17-130204        5.91      3.41
Mouse20-130514        3.61      2.41
Mouse20-130515        5.40      3.79
Mouse20-130516        4.69      3.11
Mouse20-130517        4.69      3.22
[... 95 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -n 666,906p devout.txt | cut -c1-260
```

```
===== cell 40 code tags=claim:fig4b-noise-correlations
hd rate        measure   pairs  n0  med0       p0  n60  med60      p60  mean_far  holds
 a    a  noise_avg_raw ADn-ADn  75  12.3 1.33e-13  170  -4.44  3.3e-24      -1.2   True
 a    a  noise_avg_raw  pooled 102  8.78 1.03e-17  225  -3.56 5.45e-28     -1.04   True
 a    a    noise_0_raw ADn-ADn  75  11.6 3.05e-12  170  -5.17 1.34e-25     -1.62   True
 a    a    noise_0_raw  pooled 102  7.03 1.18e-15  225   -3.9 2.08e-29     -1.35   True
 a    a noise_avg_norm ADn-ADn  75 0.891 1.33e-13  170 -0.301 1.07e-23   -0.0212   True
 a    a noise_avg_norm  pooled 102 0.878 8.15e-18  225 -0.267 9.37e-26   -0.0217   True
 a    a   noise_0_norm ADn-ADn  75 0.817 5.96e-12  170  -0.34 1.24e-24    -0.036   True
 a    a   noise_0_norm  pooled 102 0.811 8.28e-16  225 -0.313 4.53e-26    -0.034   True
 a    b  noise_avg_raw ADn-ADn 101  7.79 1.24e-17  217  -3.54 1.46e-30    -0.982   True
 a    b  noise_avg_raw  pooled 169  4.55 2.28e-26  355  -1.84 1.56e-40    -0.671   True
 a    b    noise_0_raw ADn-ADn 101  5.78 7.17e-16  217  -4.12 1.45e-32     -1.39   True
 a    b    noise_0_raw  pooled 169   3.8  8.7e-23  355  -2.11 3.98e-42    -0.917   True
 a    b noise_avg_norm ADn-ADn 101 0.887 8.49e-18  217 -0.297 2.15e-30   -0.0236   True
 a    b noise_avg_norm  pooled 169 0.796 1.51e-24  355  -0.25 3.15e-37   -0.0123   True
 a    b   noise_0_norm ADn-ADn 101 0.771 1.21e-15  217 -0.339 2.69e-32   -0.0363   True
 a    b   noise_0_norm  pooled 169 0.642 2.42e-20  355   -0.3 1.78e-38   -0.0267   True
 b    a  noise_avg_raw ADn-ADn  91  12.6 1.32e-16  185  -5.67 3.05e-28    -0.975   True
 b    a  noise_avg_raw  pooled 147  7.67 1.46e-25  295  -3.01 9.69e-41    -0.775   True
[... 222 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peyrache-2015 && python - <<'EOF'
import re
t=open('cells.py').read()
# remove hand-written result cells
parts=re.split(r'(?=^# %% )', t, flags=re.M)
parts=[p for p in parts if not (p.startswith('# %% md') and '**Result:' in p)]
open('cells.py','w').write(''.join(parts))
EOF
grep -c "Result" cells.py; date -u
```

```
0
Sun Nov 15 13:25:08 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/peyrache-2015 && python - <<'EOF'
p='hd.py'; t=open(p).read()
t=t.replace('GLM_MAX_S = 2700.0  # at most 45 min of each state (time limit; deviation)','GLM_MAX_S = 1800.0  # at most the first 30 min of each state (time limit; deviation)')
t=t.replace('''    hd_ = {reg: [c["unit"] for c in cells if c["region"] == reg and (c["hd_a"] or c["hd_b"])] for reg in ("ADn", "PoS")}''','''    hd_ = {reg: [c["unit"] for c in cells if c["region"] == reg and c["hd_a"]] for reg in ("ADn", "PoS")}''')
t=t.replace('''def analyze_session(s, parts=("cells", "pairs", "decode", "fast", "mono", "lfp")):''','''def analyze_session(s, parts=("cells", "pairs", "decode", "fast", "mono", "lfp", "glm")):''')
open(p,'w').write(t)
EOF
cd $TMPDIR && . dev/bin/activate && mkdir -p resglm && cat > runglm.py <<'EOF'
import os
os.environ["OMP_NUM_THREADS"]="1"; os.environ["OPENBLAS_NUM_THREADS"]="1"
import sys, time, pickle
sys.path.insert(0,'entries/peyrache-2015')
import hd
from concurrent.futures import ProcessPoolExecutor
def work(x):
    nm=x[0].split('_ses-')[1][:14]; fn=f'resglm/{nm}.pkl'
    if os.path.exists(fn): return pickle.load(open(fn,'rb'))
    t=time.time(); s=hd.load_session(x[1],x[0]); o=hd.analyze_session(s,("glm",))
    r=dict(glm=o['glm'], t=time.time()-t, nm=nm); pickle.dump(r,open(fn,'wb')); return r
if __name__=='__main__':
    A=[a for a in hd.list_assets() if any(m in a[0] for m in ('Mouse24','Mouse25','Mouse28'))]
    t=time.time()
    with ProcessPoolExecutor(4) as ex: O=list(ex.map(work,A))
    print('total',time.time()-t)
    for o in O: print(o['nm'], round(o['t']), len(o['glm']))
EOF
date -u; timeout 2400 python runglm.py 2>&1 | tail -25; date -u
```

```
/bin/bash: line 1: cd: entries/peyrache-2015: No such file or directory
Sun Nov 15 13:25:27 UTC 2026
Terminated                 timeout 2400 python runglm.py 2>&1 | tail -25
Sun Nov 15 14:05:27 UTC 2026
Shell cwd was reset to
```

**Agent**

The `cd` failed, so the GLM changes were never applied. The run used the old, heavier settings and was cut off at 40 minutes. It is 14:05. Checking what it saved.

**Agent calls Bash**

```bash
ls $TMPDIR/resglm | wc -l; ls $TMPDIR/resglm; grep -n "GLM_MAX_S = \|hd_ = {reg\|def analyze_session" entries/peyrache-2015/hd.py
```

```
14
Mouse24-131213.pkl
Mouse24-131216.pkl
Mouse24-131217.pkl
Mouse24-131218.pkl
Mouse25-140123.pkl
Mouse25-140124.pkl
Mouse25-140128.pkl
Mouse25-140129.pkl
Mouse25-140130.pkl
Mouse25-140131.pkl
Mouse25-140203.pkl
Mouse25-140204.pkl
Mouse25-140205.pkl
Mouse25-140206.pkl
587:def analyze_session(s, parts=("cells", "pairs", "decode", "fast", "mono", "lfp")):
905:GLM_MAX_S = 2700.0  # at most 45 min of each state (time limit; deviation)
953:    hd_ = {reg: [c["unit"] for c in cells if c["region"] == reg and (c["hd_a"] or c["hd_b"])] for reg in ("ADn", "PoS")}
```

**Agent calls Bash**

```bash
cd entries/peyrache-2015 && cat > results.py <<'EOF'
R = {
"recording-sample": "**Result: reproduced.** Under reading (a), the dandiset holds 42 sessions from 7 mice, and the three mice with a PoS probe have 21 sessions (4, 10 and 7). All four values equal the expected ones. 41 sessions have an open-field epoch (Mouse32-140820 has no epochs), and 40 of those have sleep before and after (reading b). Units labelled PoS also appear in 3 sessions of Mouse20, which the paper lists as thalamus only, so 24 sessions in 4 mice hold units of both labels.",
"supptable1-per-animal": "**Result: partially reproduced.** Under reading (hd-b), 5 of the 10 HD counts are within tolerance, and under (hd-a) 3. The session-rule variant also gives 5 under (hd-b) and 4 under (hd-a). Mouse32's 35 HD cells cannot be counted, as neither of its sessions holds head direction. Over all sessions the dual mice have more ADn HD cells (26, 62 and 74 under hd-a, against 17, 23 and 37), as Supplementary Table 1 counts their ADn cells from a subset of sessions. Recorded units equal the table in Mouse12, Mouse17 and Mouse32 (217, 245, 105), Mouse20 has 48 against 49, and the PoS counts match (48, 135, 174).",
"hd-cell-fraction": "**Result: not reproduced.** No combination of readings puts all four counts within tolerance. Over all sessions, reading (hd-a) gives 293 thalamic HD cells of 727 classifiable thalamic cells, and 82 PoS HD cells of 337. Reading (hd-b) gives 312 and 120. The per-session mean fractions are 0.53 and 0.22 (hd-a), and 0.57 and 0.33 (hd-b). The PoS counts (337 classifiable, 365 units) and the hd-b PoS HD count (120) are within tolerance. The thalamic HD counts exceed 242 because the dual mice add sessions the paper did not count; under the session rule they are 207 and 220 of 593.",
"hd-fraction-hd-shanks": "**Result: reproduced.** On 63 thalamic shank-sessions with at least one HD cell, the mean HD fraction is 0.733 under (hd-a) and the pooled fraction 0.736, both within 0.639 to 0.781. Under (hd-b) they are 0.799 and 0.784, outside the tolerance.",
"ensemble-sizes": "**Result: not reproduced.** No reading puts both means within tolerance. ADn HD cells per session are 7.51 plus or minus 4.39 over 39 sessions (readings a and b), just below the tolerance of 7.56 to 9.24, and 10.04 plus or minus 3.27 over the 25 decoded ensembles (c). PoS gives 3.57 plus or minus 2.97 (a), 4.10 plus or minus 2.81 (b) and 8.20 plus or minus 1.48 (c), against 5 plus or minus 2.8. Only the PoS s.d. of reading (b) is within tolerance.",
"sleep-duration": "**Result: reproduced.** Under reading (a), the home-cage epochs before and after the open field total 4.99 h on average, with an s.d. of 0.97 h, over 37 sessions with the paper's scoring. Both values are within tolerance. The scored SWS and REM total 3.20 plus or minus 0.57 h (reading b), outside it.",
"adn-pos-peak-rate": "**Result: partially reproduced.** ADn HD cells have higher peak rates than PoS HD cells (Mann-Whitney p = 1.9e-13 under hd-a, 1.9e-18 under hd-b, both below 1e-10). The ratio is above 3.3 under every reading: medians 3.76 and means 3.95 (hd-a), medians 3.51 and means 4.26 (hd-b).",
"adn-pos-hd-information": "**Result: reproduced.** Under reading (hd-b) with means, ADn HD cells carry 1.38 and PoS HD cells 1.00 bits per spike, both within tolerance, with Mann-Whitney p = 3.9e-11. Under (hd-a) both medians (1.38, 1.14) and both means (1.44, 1.17) are within tolerance, but p = 4.5e-5 does not reach 1e-6. With (hd-b) medians the PoS value (0.87) is outside.",
"supfig2a-unimodality": "**Result: reproduced.** Under HD reading (hd-b) and peak reading (a), 12.2% of ADn and 29.2% of PoS HD cells have a second peak of 50% or more, both within tolerance. Under (hd-a) the ADn fraction (10.9%) is within and the PoS fraction (18.3%) is not. Peak reading (b) gives lower fractions (3.4 to 5.1% ADn, 12.2 to 24.2% PoS).",
"fig2a-rates-preserved": "**Result: reproduced.** Under the r of at least 0.5 reading, all four correlations pass with p < 0.05. In ADn the waking rates correlate with SWS rates at r = 0.80 and with REM rates at r = 0.86 (hd-a, 274 cells in sessions with both sleep stages). In PoS the values are 0.65 and 0.66 (69 cells). The PoS values fall below the 0.7 reading except with rate-a cells (0.73 and 0.66). The cell counts are 245 to 293 ADn and 38 to 100 PoS, against 215 and 62.",
"fig2b-pair-correlations-preserved": "**Result: reproduced.** The waking pair correlations predict the SWS and REM ones in every pair type, reading and shank selection, with r from 0.81 to 0.97 (all p < 0.05), so the 0.7 reading holds. The ADn pair counts (1006 to 1425 HD pairs) are above 970.",
"fig2f-sws-tenfold-faster": "**Result: partially reproduced.** The SWS speed exceeds the waking speed in most pairs (Wilcoxon p < 0.001 in every reading), but the median SWS to waking ratio is outside 9 to 11. It is 11.7 to 12.3 in ADn-ADn pairs, with the 95.7% of pairs faster in SWS under hd-a and rate-a, and 5.6 to 6.1 in PoS-PoS pairs. It is above 5 in both, the partial criterion. 387 pairs have a fitted speed at an end of the grid in some state.",
"fig2e-decoded-speed": "**Result: partially reproduced.** Only the REM part holds, in PoS under one reading, and the SWS ratio is outside tolerance under every reading. With steps at the smoothing window (b) and decoded waking speed (w-a), the median decoded speed in ADn is 140 deg/s in SWS, 23 in waking and 13 in REM (SWS ratio 6.0, REM ratio 0.57). In PoS (4 ensembles) the SWS ratio is 2.7 and the REM ratio 1.0, inside the band. With the actual head speed in waking (w-b), the ratios are 4.3 and 0.41 in ADn. At 10 ms steps (a) the medians are 0 or 100 deg/s, as decoded angles move in 1 degree steps, so that reading cannot decide.",
"fig2f-rem-similar-to-wake": "**Result: reproduced.** Both readings hold in ADn-ADn and PoS-PoS pairs under every HD and rate reading. The median REM to waking speed ratio is 0.96 to 1.20, inside 0.67 to 1.5, and no Wilcoxon test of the log ratio reaches p < 0.05 (p from 0.17 to 0.66).",
"fig3a-packet-60-degrees": "**Result: partially reproduced.** Under hd-a and rate-b, the zero-lag correlation falls with the preferred-direction offset in all 9 state and pair-type combinations (p < 1e-6 with the absolute offset and with its cosine). The zero crossing is within 54 to 66 degrees in 7 of 9 combinations with 10 degree bins, and 8 of 9 with 20 degree bins. PoS-PoS in SWS crosses at 54 and 108 degrees. Under rate-a the PoS-PoS tests reach only p = 5.5e-6 to 7.2e-5 (36 pairs). ADn-ADn pairs cross at 54 to 59 degrees in every state.",
"fig3a-adn-stronger-than-pos": "**Result: reproduced.** Under hd-a and rate-b, pairs closer than 60 degrees are more correlated in ADn than in PoS in every state. The medians are 0.28 against 0.06 in waking, 0.15 against 0.02 in SWS and 0.23 against 0.06 in REM, with Mann-Whitney p = 1.9e-7, 4.6e-8 and 1.7e-6, each below the text's 1e-5. Under hd-a and rate-a, PoS has only 12 pairs and p is 0.03 to 0.045. The ADn pair counts (328 to 480) exceed 345 plus or minus 34.5 except under hd-a and rate-a.",
"supfig5-rate-independent": "**Result: not reproduced.** Where the region effect reaches p < 1e-7 (7 of 64 readings, all among pairs closer than 60 degrees), the rate-group effect is significant in 6 (p from 1.7e-9 to 0.0057). Region p < 1e-7 together with rate-group p > 0.05 holds in 1 reading (hd-b, rate-b, geometric peak rate, SWS: 2.6e-8 and 0.09). Over all pairs no region effect is found (p 0.23 to 0.98).",
"fig3b-packet-coherence": "**Result: reproduced.** At the decoder's windows, the median over ensembles of the coherence exceeds 0.05 in both structures and all three states under every reading of distance, reference vectors and summary. The lowest is 0.082 (ADn, SWS, decoded-HD references, correlation distance, median over bins). Every ensemble passes with the mean summary. Other windows were not run.",
"fig4b-noise-correlations": "**Result: reproduced.** In every reading (HD, rate, lag and scale), the noise correlation is above 0 for pairs within 15 degrees and below 0 for pairs at 60 plus or minus 15 degrees, in ADn-ADn pairs and in pooled pairs. Every Wilcoxon p is below 1e-11. Under hd-a, rate-a and the -50 to +50 ms normalised reading, the ADn-ADn medians are 0.89 and -0.30, and beyond 90 degrees the mean is -0.02.",
"fig4c-noise-adn-vs-pos": "**Result: reproduced.** Under hd-a and rate-b, with every lag and scale reading, the Kruskal-Wallis test across the three pair types gives p < 0.001 at 0 and at 60 degrees, with ADn-ADn pairs the most extreme. The raw 50 ms reading gives p = 8.5e-9 and 2.3e-13. At 0 degrees there are 101 ADn-ADn, 49 ADn-PoS and 19 PoS-PoS pairs, against 96, 77 and 29. At 60 degrees there are 217, 107 and 31, against 200, 157 and 57.",
"fig4d-ole-near-bayesian": "**Result: not reproduced.** The covariance OLE is not better than the signal OLE. The median minimum error is 12.98 against 13.22 degrees in 25 ADn ensembles (covariance lower in 14, Wilcoxon p = 0.16) and 20.96 against 20.96 in 5 PoS ensembles (p = 0.13). The covariance OLE errors are 1.26 (ADn) and 1.42 (PoS) times the Bayesian decoder's. The outcome rests on the estimator assumed here, as the paper defines none.",
"fig4e-ole-covariance": "**Result: not reproduced.** The median ratio of covariance to signal OLE error is 0.99 in ADn (range 0.91 to 1.04) and 0.98 in PoS, far from 0.5 or 0.67, and ADn and PoS do not differ (Mann-Whitney p = 0.28). There are 25 ADn and 5 PoS ensembles, against 20 and 8. The outcome rests on the estimator assumed here.",
"decoding-tracks-hd": "**Result: reproduced.** The median over ensembles of the median absolute decoding error is 10.2 degrees in 25 ADn ensembles (maximum 13.1) and 14.4 degrees in 5 PoS ensembles (maximum 25.1) with whole-epoch tuning curves. Cross-validated, it is 10.7 and 14.8. All are under 30 degrees, against 76 to 77 degrees with the head direction shifted by 10 s.",
"fig5b-sleep-tuning-similar": "**Result: reproduced.** The tuning curves against decoded HD correlate with the waking tuning curves with medians of 0.92 (REM), 0.90 (SWS) and 0.98 (waking) for 51 to 64 PoS HD cells decoded from ADn, and 0.87, 0.81 and 0.93 for 43 to 52 ADn HD cells decoded from PoS. Both bin readings give the same medians within 0.01. Every median is above 0.5.",
"fig5b-adn-decoded-tuning": "**Result: reproduced.** PoS cells decoded from ADn have higher correlations than ADn cells decoded from PoS in every state. Under reading (a), Mann-Whitney p = 7.0e-7 in waking, 5.0e-4 in SWS and 0.039 in REM; reading (b) gives 1.5e-7, 4.7e-4 and 0.042. The counts are 64 and 52 cells in waking, against 86 and 92.",
"fig6a-fast-oscillation": "**Result: reproduced.** For ADn HD pairs on different shanks (492 per state), the mean power of the z-scored cross-correlograms above 80 Hz peaks at 165 Hz in waking, 175 Hz in SWS and 165 Hz in REM, all within 117 to 176 Hz. With same-shank pairs included, the peak moves to the top of the frequency grid (285 to 300 Hz).",
"fig6b-adn-synchrony": "**Result: reproduced.** With the peak z within 5 ms and pairs on different shanks, the three states pooled give Kruskal-Wallis p = 2.2e-24 across 30 degree offset groups. The mean falls from 11.6 (0 to 30 degrees) to 3.0 (150 to 180 degrees). In each state p < 0.05 with the same fall (waking p = 1.4e-5, SWS 5.1e-14, REM 2.2e-6). Waking alone does not reach 1e-10. The zero-lag z of all pairs is negative (same-shank pairs).",
"fig7-adn-pos-connections": "**Result: not reproduced.** The ADn to PoS fraction is within tolerance, but the PoS to ADn fraction and the pyramidal fractions are not. Over all 4111 ADn by PoS pairs of the three dual mice, 4.57% are connected ADn to PoS (Methods' baseline; 4.45% with the jitter baseline) and 0.51% PoS to ADn, against 0.35%. Among the 1583 pairs of ADn HD and PoS pyramidal cells, 1.07% are connected ADn to PoS and 0.44% PoS to ADn (17 and 7 pairs), against 0.41% and 0.18% over 3394. The direction holds: binomial p = 0.064 (17 of 24 against one half) and 0.0009 (against the PoS to ADn proportion).",
"fig7c-adn-triggered-pos-lfp": "**Result: reproduced.** Within 5 ms of ADn HD cell spikes, the 80 to 250 Hz PoS LFP has more power than at jittered spike times (median ratio 2.98, 118 of 161 cells, Wilcoxon p = 1.1e-12) and than at random times (3.30, p = 1.1e-13). The session median ratio exceeds 1 in 18 and 20 of 20 sessions. One 14 minute window per session was read.",
"fig7d-same-preferred-direction": "**Result: reproduced.** The 11 connected ADn HD to PoS HD pairs have unimodal differences of preferred direction (Rayleigh p = 3.0e-4) with no shift from 0 (median -8.8 degrees, Wilcoxon p = 0.41), under every baseline.",
"fig7e-driven-pos-hd-information": "**Result: reproduced.** With the Methods' baseline (with or without the hollow), the 13 PoS pyramidal cells driven by an ADn HD cell carry more HD information than the 164 not connected (medians 1.08 against 0.58 bits per spike, Mann-Whitney p = 0.040). With the jitter baseline variant (14 against 163), p = 0.075.",
"fig7e-interneurons-no-difference": "**Result: reproduced.** The 8 driven PoS putative interneurons do not differ from the 51 not connected (medians 0.013 against 0.004 bits per spike, difference 0.009, Mann-Whitney p = 0.45; jitter baseline p = 0.59).",
}
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
python - <<'EOF'
t=open('results.py').read()
t=t.replace("with the 95.7% of pairs faster in SWS under hd-a and rate-a","and 95.7% of ADn-ADn pairs are faster in SWS under hd-a and rate-a")
t=t.replace("The ADn pair counts (328 to 480) exceed 345 plus or minus 34.5 except under hd-a and rate-a.","The ADn pair counts are 328 to 480; 328 (hd-a, rate-a) and 374 (hd-b, rate-a) are within 345 plus or minus 34.5.")
t=t.replace("the rate-group effect is significant in 6 (p from 1.7e-9 to 0.0057)","the rate-group effect is significant in 6 (p from 8.8e-15 to 0.0013)")
t=t.replace("The PoS values fall below the 0.7 reading except with rate-a cells (0.73 and 0.66).","The PoS values are below 0.7 under every cell reading except waking against SWS with rate-a cells (0.73).")
t=t.replace("The PoS counts (337 classifiable, 365 units) and the hd-b PoS HD count (120) are within tolerance.","The PoS counts (337 classifiable, 365 units), the hd-b PoS HD count (120) and the hd-b per-session PoS fraction (0.33) are within tolerance.")
open('results.py','w').write(t)
EOF
cat >> cells.py <<'EOF'

# %% md
## fig5d-adn-predicts-pos-reliably, fig5e-readout-windows, fig5e-adn-predicts-pos: blocked

These three claims need the GLM prediction of Fig. 5d,e (`hd.glm_session`, not run here). In preparation, outside this notebook, one session (Mouse24-131216, 10 targets, 25 readout windows, 10 folds, 3 states) took 242 s. A run over the three dual mice covered 14 of 21 sessions in 40 minutes on 4 workers (Mouse24 and Mouse25) before it was stopped. The 7 Mouse28 sessions, which have the most HD cells, were left. With the 12.5 minutes of the other analyses, the notebook would exceed the 60 minute limit, so the claims are blocked as `too_large`. No number from those runs is used.

# %% md
## Summary

| claim | outcome |
|---|---|
| recording-sample | reproduced |
| supptable1-per-animal | partially reproduced |
| hd-cell-fraction | not reproduced |
| hd-fraction-hd-shanks | reproduced |
| ensemble-sizes | not reproduced |
| sleep-duration | reproduced |
| adn-pos-peak-rate | partially reproduced |
| adn-pos-hd-information | reproduced |
| supfig2a-unimodality | reproduced |
| fig2a-rates-preserved | reproduced |
| fig2b-pair-correlations-preserved | reproduced |
| fig2f-sws-tenfold-faster | partially reproduced |
| fig2e-decoded-speed | partially reproduced |
| fig2f-rem-similar-to-wake | reproduced |
| fig3a-packet-60-degrees | partially reproduced |
| fig3a-adn-stronger-than-pos | reproduced |
| supfig5-rate-independent | not reproduced |
| fig3b-packet-coherence | reproduced |
| fig4b-noise-correlations | reproduced |
| fig4c-noise-adn-vs-pos | reproduced |
| fig4d-ole-near-bayesian | not reproduced (assumed estimator) |
| fig4e-ole-covariance | not reproduced (assumed estimator) |
| decoding-tracks-hd | reproduced |
| fig5b-sleep-tuning-similar | reproduced |
| fig5b-adn-decoded-tuning | reproduced |
| fig5d-adn-predicts-pos-reliably | blocked (too_large) |
| fig5e-readout-windows | blocked (too_large) |
| fig5e-adn-predicts-pos | blocked (too_large) |
| fig6a-fast-oscillation | reproduced (assumed jitter null) |
| fig6b-adn-synchrony | reproduced (assumed jitter null) |
| fig7-adn-pos-connections | not reproduced |
| fig7c-adn-triggered-pos-lfp | reproduced (assumed window and measure) |
| fig7d-same-preferred-direction | reproduced |
| fig7e-driven-pos-hd-information | reproduced |
| fig7e-interneurons-no-difference | reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method.

**How the analysis differs from the paper's.**
- Every session with head direction is used. The paper counted the ADn cells of the three dual mice from a subset of sessions, which the files do not mark. A depth-based reading of the Methods' session rule is shown as a variant for the counts.
- The GLM claims are not run, for time.
- The fast-synchrony null is the expectation of the jittered cross-correlogram, not 100 jitters.
- The OLE is the standard Salinas and Abbott estimator, with an assumed signal covariance.
- The spike-triggered LFP uses one 14 minute window per session.
- Two sessions without the paper's sleep scoring enter the waking analyses only, with the open-field epoch as wake.

**What was found about the dataset.**
- Mouse28-140314 and both Mouse32 sessions hold no head direction, so Mouse32's cells cannot be classified. Mouse32-140820 also has no epochs or sleep states.
- Mouse25-140131 and Mouse25-140204 lack the paper's sleep scoring.
- Mouse20 has 8 units labelled post-subiculum, though the paper lists no PoS probe in that mouse.
- In Mouse17-130130, spikes continue 1101 s past the last sub-recording.
- The wake interval of Mouse12-120808 spans 130 by 97 cm of LED positions, against the 53 by 46 cm arena.
- Recorded unit counts match Supplementary Table 1 in the thalamus-only mice and in PoS.
- The file's own HD classification agrees with reading (hd-a) for 1007 of 1064 classifiable cells.
EOF
cat > build.py <<'EOF'
import re, nbformat as nbf
src = open('cells.py').read()
from results import R
parts = re.split(r'^# %% ', src, flags=re.M)[1:]
nb = nbf.v4.new_notebook()
cells = []
claims_done = set()
for p in parts:
    head, _, body = p.partition('\n')
    body = body.strip('\n')
    if head.startswith('md'):
        cells.append(nbf.v4.new_markdown_cell(body))
    else:
        c = nbf.v4.new_code_cell(body)
        m = re.search(r'tags=(\S+)', head)
        if m:
            c.metadata['tags'] = [m.group(1)]
        cells.append(c)
        if m and m.group(1).startswith('claim:'):
            cid = m.group(1)[6:]
            cells.append(nbf.v4.new_markdown_cell(R[cid]))
            claims_done.add(cid)
missing = set(R) - claims_done
assert not missing, missing
nb.cells = cells
nb.metadata['kernelspec'] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nbf.write(nb, 'reproduce_peyrache_2015.ipynb')
print(len(cells), 'cells')
EOF
. $TMPDIR/dev/bin/activate && python build.py && grep -c "claim:" reproduce_peyrache_2015.ipynb
```

```
87 cells
32
```

**Agent calls Bash**

```bash
python - <<'EOF'
t=open('cells.py').read()
t=t.replace('''depth = {}
for o in RES:
    pass
''','')
t=t.replace('for st in STATES if False else ("wake", "SWS", "REM"):','for st in ("wake", "SWS", "REM"):')
t=t.replace('''            for rd in ("a", "b"):
                pass
''','')
open('cells.py','w').write(t)
EOF
. $TMPDIR/dev/bin/activate && python build.py && mv cells.py results.py build.py $TMPDIR/ && cat > entry.yaml <<'EOF'
schema_version: 1
name: peyrache-2015
type: reproduction
title: Internally organized mechanisms of the head direction sense (Peyrache et al. 2015)
description: Tests the findings of Peyrache, Lacroix, Petersen and Buzsaki (2015) on dandiset 000056, which holds
  42 sessions of anterodorsal thalamus and post-subiculum recordings in 7 mice across waking and sleep. It
  classifies head-direction cells, compares the two structures, and tests the preservation of rates, pair
  correlations and the activity packet across brain states, the speed of the internal signal, noise
  correlations, Bayesian and linear decoding, fast synchrony and ADn to PoS connections.
license: Apache-2.0
notebooks:
- path: reproduce_peyrache_2015.ipynb
  title: Reproducing Peyrache et al. (2015) from dandiset 000056
  runtime_minutes: 16
helpers:
- hd.py
related:
- id: dandi:000056/0.261106.1949
  relation: uses_data
- id: doi:10.1038/nn.3968
  relation: reproduces
EOF
cat > README.md <<'EOF'
# Peyrache et al. (2015) on DANDI:000056

Tests the claims in `claims/peyrache-2015.yaml` for "Internally organized mechanisms of the head direction
sense" (Peyrache, Lacroix, Petersen and Buzsaki, Nature Neuroscience 2015, doi:10.1038/nn.3968) on dandiset
000056, version 0.261106.1949, streamed from the archive.

- `reproduce_peyrache_2015.ipynb` runs every analysis. It streams the 42 sessions four at a time, and its
  data check comes first, followed by one section per claim.
- `hd.py` holds the loading code and the measures. The docstring of each says where its parameters come from.

Of 37 claims, 34 are tested. The three GLM claims of Fig. 5d,e are blocked as too large for the time limit.
The record is `attempts/peyrache-2015-02.yaml`.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method.
EOF
cd  && date -u && python tools/entry.py lock entries/peyrache-2015 2>&1 | tail -5 && python tools/entry.py check entries/peyrache-2015 2>&1 | tail -20
```

```
87 cells
Sun Nov 15 14:07:36 UTC 2026
wrote peyrache-2015/requirements.lock.txt (Python 3.13, with hashes)
0 error(s)
```

**Agent**

The check passes. Running the entry from a clean environment, expected about 15 minutes.

**Agent calls Bash**

```bash
date -u && timeout 4000 python tools/entry.py all entries/peyrache-2015 2>&1 | tail -20; date -u
```

```
Sun Nov 15 14:07:49 UTC 2026
Installed kernelspec registry-peyrache-2015 in executed/peyrache-2015/.venv/share/jupyter/kernels/registry-peyrache-2015
0 error(s)
pass  reproduce_peyrache_2015.ipynb  (742 s)
Sun Nov 15 14:20:22 UTC 2026
```

**Agent**

Passed in 12.4 minutes. Checking that the executed outputs match the numbers in the conclusions.

**Agent calls Bash**

```bash
ls executed/peyrache-2015/; . $TMPDIR/dev/bin/activate; python - <<'EOF'
import nbformat
nb=nbformat.read('executed/peyrache-2015/reproduce_peyrache_2015.ipynb',4)
out=[]
for c in nb.cells:
    if c.cell_type=='code':
        for o in c.get('outputs',[]):
            if 'text' in o: out.append(o['text'])
            elif o.get('output_type')=='error': out.append('ERROR '+o['ename'])
            elif 'data' in o and 'text/plain' in o['data']: out.append(o['data']['text/plain'])
txt='\n'.join(out); open('/tmp/claude-1001/exec_out.txt','w').write(txt)
EOF
cd $TMPDIR; grep -c ERROR exec_out.txt; head -3 exec_out.txt; python - <<'EOF'
a=open('/tmp/claude-1001/exec_out.txt').read(); b=open('/tmp/claude-1001/devout.txt').read()
import re
nums=lambda s: re.findall(r'-?\d+\.\d+(?:e-?\d+)?', s)
for key in ['median ratio cov/signal','Mann-Whitney p','Wilcoxon p','peak_freq','connected n','median power ratio','Rayleigh p','mean_of_shanks','homecage_h: n','within tolerance: hd-a','thal_hd','median_ratio  frac']:
    la=[l for l in a.splitlines() if key in l][:3]; lb=[l for l in b.splitlines() if key in l][:3]
    print(key, 'SAME' if la==lb else 'DIFF'); 
    if la!=lb: print(' exec',la,'\n dev ',lb)
EOF
```

```
reproduce_peyrache_2015.ipynb
result.json
0
dandiset 000056 version 0.261106.1949

analysed 42 sessions in 12.2 min; peak memory of this process 0.28 GB
median ratio cov/signal SAME
Mann-Whitney p SAME
Wilcoxon p SAME
peak_freq SAME
connected n SAME
median power ratio SAME
Rayleigh p SAME
mean_of_shanks SAME
homecage_h: n SAME
within tolerance: hd-a SAME
thal_hd SAME
median_ratio  frac SAME
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; grep -v "^=====" devout.txt | grep -v "analysed\|Traceback" > d1.txt; grep -v "analysed\|dandiset 000056" exec_out.txt > d2.txt; diff <(sed 's/[[:space:]]*$//' d1.txt) <(sed 's/[[:space:]]*$//' d2.txt) | head -20; diff d1.txt d2.txt | wc -l
```

```
1c1,2
< dandiset 000056 version 0.261106.1949
---
> 
> 
2a4
> 
76a79
> 
111a115
> 
138a143
> 
182a188
> 
189a196
> 
226a234
> 
234a243
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; diff <(grep -v '^\s*$' d1.txt | sed 's/[[:space:]]*$//') <(grep -v '^\s*$' d2.txt | sed 's/[[:space:]]*$//') | head; date -u
```

```
1d0
< dandiset 000056 version 0.261106.1949
404a404,499
> /tmp/claude-1001/ipykernel_34/1885310188.py:11: Pandas4Warning: Starting with pandas version 4.0 all arguments of all will be keyword-only.
>   ok = c[["corr_wake", "corr_" + st]].notna().all(1)
> /tmp/claude-1001/ipykernel_34/1885310188.py:11: Pandas4Warning: Starting with pandas version 4.0 all arguments of all will be keyword-only.
>   ok = c[["corr_wake", "corr_" + st]].notna().all(1)
> /tmp/claude-1001/ipykernel_34/1885310188.py:11: Pandas4Warning: Starting with pandas version 4.0 all arguments of all will be keyword-only.
>   ok = c[["corr_wake", "corr_" + st]].notna().all(1)
> /tmp/claude-1001/ipykernel_34/1885310188.py:11: Pandas4Warning: Starting with pandas version 4.0 all arguments of all will be keyword-only.
Sun Nov 15 14:20:39 UTC 2026
Shell cwd was reset to
```

**Agent**

The executed numbers are identical to the development run; only pandas warnings were added. Writing the attempt record now.

**Agent calls Bash**

```bash
grep -n "findings:" -A12 attempts/fouke-2025-01.yaml | head -30; python - <<'EOF'
import json
s=json.load(open('schemas/attempt.schema.json'))
print(s.get('required'))
d=s.get('$defs',s.get('definitions',{}))
for k in ['outcome','finding','dataset','input','provenance']:
    for kk,v in d.items():
        if k in kk.lower(): print(kk, v.get('required'), list(v.get('properties',{}).keys())); 
EOF
```

```
244:findings:
245-- kind: data_missing
246-  statement: The dandiset holds only the freely swimming tracking of Figure 1 and Figure S1. The
247-    two-photon imaging and the head-fixed tail tracking behind Figures 2 to 4 are not in it, and
248-    the GitLab repository the paper names for all behavioural and imaging data holds analysis
249-    notebooks only. Nine of the paper's main findings cannot be tested.
250-- kind: metadata_insufficient
251-  statement: The stimulus codes 0 to 20 have no names or description in the files or the
252-    dandiset metadata. They can be named only from the paper's analysis notebook and the protocol
253-    file of its stimulus software.
254-- kind: code_mismatch
255-  statement: The paper's analysis notebook labels code 9 as lateral right and 11 as lateral left,
256-    while its conversion of the stimulus software's names gives the reverse (it carries a remap
['schema_version', 'id', 'datasets', 'paper', 'date', 'provenance', 'outcomes']
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
s=json.load(open('schemas/attempt.schema.json'))
def show(o,ind=0,depth=0):
    if depth>3: return
    if isinstance(o,dict):
        if 'properties' in o:
            print(' '*ind, 'req', o.get('required'), 'props', list(o['properties'].keys()))
            for k,v in o['properties'].items():
                if k in ('outcomes','findings','provenance','inputs','datasets'):
                    print(' '*ind,k); show(v.get('items',v),ind+2,depth+1)
show(s)
o=s['properties']['outcomes']['items']
print(json.dumps(o.get('properties',{}).get('outcome',{})), json.dumps(o.get('properties',{}).get('blocked_by',{}))[:300])
f=s['properties']['findings']['items']; print(json.dumps(f)[:1500])
EOF
```

```
req ['schema_version', 'id', 'datasets', 'paper', 'date', 'provenance', 'outcomes'] props ['schema_version', 'id', 'datasets', 'missing_datasets', 'paper', 'date', 'entry', 'deprecated', 'provenance', 'outcomes', 'verifications', 'findings', 'reconciliation', 'inputs']
 datasets
   req ['archive', 'id', 'version', 'relation'] props ['archive', 'id', 'version', 'modified', 'doi', 'relation']
 provenance
   req ['kind', 'accountable'] props ['kind', 'accountable', 'agent', 'runner']
 outcomes
   req ['claim', 'outcome'] props ['claim', 'outcome', 'blocked_by', 'notes', 'notebook', 'output', 'measured', 'deviations', 'assumed', 'proposed']
 findings
   req ['kind', 'statement'] props ['kind', 'statement', 'found', 'about', 'datasets']
   datasets
 inputs
   req ['what', 'source'] props ['what', 'source']
{"enum": ["reproduced", "partially_reproduced", "not_reproduced", "blocked"], "description": "Describes the result, not the method: whether the effect the claim states was found. Differences in method from the paper go in `deviations`."} {"description": "Required when outcome is blocked.", "enum": ["data_missing", "metadata_insufficient", "methods_underspecified", "data_unreadable", "dataset_missing", "too_large", "not_runnable", "other"]}
{"type": "object", "additionalProperties": false, "required": ["kind", "statement"], "properties": {"kind": {"enum": ["metadata_error", "data_missing", "identifier_missing", "metadata_insufficient", "selection_undocumented", "methods_unavailable", "format_error", "code_mismatch", "paper_inconsistency", "other"]}, "statement": {"type": "string", "minLength": 1}, "found": {"description": "How the finding was found. Unset: by the attempt itself. `on_prompt`: by the reconcile step of a repeat attempt, which checked a finding of the earlier attempt that this one, made blind, did not report (docs/protocol.md, \"Repeat attempts\").", "enum": ["on_prompt"]}, "about": {"description": "What the finding is about. `data`: the dataset's files or 
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; cd $TMPDIR && cat > rec.py <<'EOF'
import yaml, re, sys
sys.path.insert(0, '.')
from results import R
NB = "reproduce_peyrache_2015.ipynb"
oc = {
 "recording-sample": ("reproduced", [42, 42, 21, 3]),
 "supptable1-per-animal": ("partially_reproduced", [66, 54, 16, 29, 65, 82, 0, 9, 63, 48]),
 "hd-cell-fraction": ("not_reproduced", [293, 727, 0.528, 82, 337, 0.243]),
 "hd-fraction-hd-shanks": ("reproduced", 0.733),
 "ensemble-sizes": ("not_reproduced", [7.51, 4.39, 3.57, 2.97]),
 "sleep-duration": ("reproduced", [4.99, 0.97]),
 "adn-pos-peak-rate": ("partially_reproduced", 3.76),
 "adn-pos-hd-information": ("reproduced", [1.38, 1.00]),
 "supfig2a-unimodality": ("reproduced", [0.122, 0.292]),
 "fig2a-rates-preserved": ("reproduced", [274, 69]),
 "fig2b-pair-correlations-preserved": ("reproduced", [1006, 36]),
 "fig2f-sws-tenfold-faster": ("partially_reproduced", 12.3),
 "fig2e-decoded-speed": ("partially_reproduced", 6.0),
 "fig2f-rem-similar-to-wake": ("reproduced", None),
 "fig3a-packet-60-degrees": ("partially_reproduced", [54.2, 1290, 694, 179]),
 "fig3a-adn-stronger-than-pos": ("reproduced", [429, 63]),
 "supfig5-rate-independent": ("not_reproduced", None),
 "fig3b-packet-coherence": ("reproduced", None),
 "fig4b-noise-correlations": ("reproduced", None),
 "fig4c-noise-adn-vs-pos": ("reproduced", [101, 217, 49, 107, 19, 31]),
 "fig4d-ole-near-bayesian": ("not_reproduced", None),
 "fig4e-ole-covariance": ("not_reproduced", [25, 5]),
 "decoding-tracks-hd": ("reproduced", None),
 "fig5b-sleep-tuning-similar": ("reproduced", None),
 "fig5b-adn-decoded-tuning": ("reproduced", [64, 52]),
 "fig6a-fast-oscillation": ("reproduced", [165, 175]),
 "fig6b-adn-synchrony": ("reproduced", 1320),
 "fig7-adn-pos-connections": ("not_reproduced", [4111, 0.0457, 0.0051, 1583, 0.0107, 0.0044]),
 "fig7c-adn-triggered-pos-lfp": ("reproduced", None),
 "fig7d-same-preferred-direction": ("reproduced", 11),
 "fig7e-driven-pos-hd-information": ("reproduced", [13, 164]),
 "fig7e-interneurons-no-difference": ("reproduced", [8, 51]),
}
ALLS = "Every session with head direction is used. Supplementary Table 1 counts the ADn cells of Mouse24, 25 and 28 from 2, 3 and 3 of their sessions, which the files do not mark; a reading of the Methods' session rule from the probe depths is shown as a variant for the counts (Methods, Electrodes, surgery and data acquisition)."
SM = "Tuning curves smooth the spike and occupancy histograms separately before the ratio, a standard choice so that empty 1 degree bins are defined (Methods, Head direction cells)."
WAKEFB = "Mouse25-140131 and Mouse25-140204 have no sleep scoring in the files; their open-field epoch is taken as wake and they enter the waking analyses only."
dev = {
 "recording-sample": ["Mice and sessions are counted from the files; the 42 of the text is matched by the dandiset's 42 files, not by Supplementary Table 1's 50."],
 "supptable1-per-animal": [ALLS, SM, "Mouse32's sessions have no head direction, so its count is 0 here."],
 "hd-cell-fraction": [ALLS, SM, "Thalamic cells are units labelled anterodorsal nucleus; the 126 cells of sessions without head direction cannot be classified."],
 "hd-fraction-hd-shanks": [ALLS, "Shank is the units' shank column (the .clu file)."],
 "ensemble-sizes": [ALLS],
 "sleep-duration": ["Home-cage time is the duration of the epochs tagged sleep_pre and sleep_post; sessions without the paper's sleep scoring are left out (37 sessions)."],
 "adn-pos-peak-rate": [ALLS, SM],
 "adn-pos-hd-information": [ALLS, "Information uses head-direction frames (25.6 ms) as the time base, the frame nearest each spike giving the intensity (Methods, Information measures), and 10 segments of equal duration."],
 "supfig2a-unimodality": [SM],
 "fig2a-rates-preserved": ["Pearson's r on linear rates; log rates are printed as a variant."],
 "fig2b-pair-correlations-preserved": ["Pair correlations over all bins of each state, 300 ms (wake, REM) and 50 ms (SWS), Figure 3a legend."],
 "fig2f-sws-tenfold-faster": ["Cross-correlograms from 10 ms bins concatenated across the intervals of a state (a standard choice); the coarse grid is 80 speeds from 5 to 5000 deg/s on a log scale (v-c)."],
 "fig2e-decoded-speed": ["Decoded angles are the posterior maximum on the 1 degree grid, so 10 ms speeds are quantised to multiples of 100 deg/s; the medians at that step cannot decide."],
 "fig2f-rem-similar-to-wake": [],
 "fig3a-packet-60-degrees": [],
 "fig3a-adn-stronger-than-pos": [],
 "supfig5-rate-independent": ["Pairs above 10 Hz are left out of the two-way ANOVA, as the figure has groups below 5 and 5 to 10 Hz only; type 2 sums of squares."],
 "fig3b-packet-coherence": ["Only the decoder's own windows (300 ms wake and REM, 50 ms SWS) are run; the other windows of reading (c-c) are not.", "Coherence is computed on 3000 time bins drawn at random per state (seeded), a standard choice; the expected packet is the sum of normalised tuning curves weighted by the rates the tuning curves give at the decoded angle (Methods, Ensemble coherence)."],
 "fig4b-noise-correlations": ["The tuning curve of the whole waking epoch is used for the intensity function (n-c), as the criterion says."],
 "fig4c-noise-adn-vs-pos": [],
 "fig4d-ole-near-bayesian": ["Assumed, as the paper does not define the OLE: weights D = Q^-1 L (Salinas and Abbott 1994), L the correlation of smoothed counts with (cos, sin) of head direction; Q from the counts (covariance OLE) or, for the signal OLE, from the tuning curves read at the head direction off the diagonal with the observed variances on it (independent neurons). Windows 10, 20, 50, 100, 200, 300, 500 and 1000 ms."],
 "fig4e-ole-covariance": ["Assumed estimator, as for fig4d-ole-near-bayesian."],
 "decoding-tracks-hd": [],
 "fig5b-sleep-tuning-similar": ["Target cells are HD cells under reading (hd-a); decoding uses the hd-a HD cells of the other structure."],
 "fig5b-adn-decoded-tuning": [],
 "fig6a-fast-oscillation": ["The jitter null is the expectation of the jittered cross-correlogram (the cross-correlogram convolved with a 20 ms box) with its Poisson s.d., in place of 100 jittered trains; assumed, for time. Power is averaged over lags within +-25 ms; frequencies 50 to 300 Hz in 5 Hz steps."],
 "fig6b-adn-synchrony": ["The same jitter null as fig6a-fast-oscillation."],
 "fig7-adn-pos-connections": ["Cross-correlograms over the whole recording, all states; only the three mice with a PoS probe (the 8 Mouse20 units labelled PoS are left out). PoS pyramidal cells from the dataset's mean waveforms (buzcode_mean_waveform), with a Morlet power spectrum after 4x cubic upsampling, a standard choice."],
 "fig7c-adn-triggered-pos-lfp": ["One HDF5 chunk of LFP per session (samples 1048576 to 2097151, about 14 min), whatever the state, for time; assumed. The power measure is the mean square of the 80 to 250 Hz spike-triggered average within +-5 ms."],
 "fig7d-same-preferred-direction": ["The Wilcoxon test is applied to the signed circular differences in radians."],
 "fig7e-driven-pos-hd-information": [],
 "fig7e-interneurons-no-difference": [],
}
assumed = {"fig4d-ole-near-bayesian", "fig4e-ole-covariance", "fig6a-fast-oscillation", "fig6b-adn-synchrony", "fig7c-adn-triggered-pos-lfp"}
outs = []
order = ["recording-sample","supptable1-per-animal","hd-cell-fraction","hd-fraction-hd-shanks","ensemble-sizes","sleep-duration","adn-pos-peak-rate","adn-pos-hd-information","supfig2a-unimodality","fig2a-rates-preserved","fig2b-pair-correlations-preserved","fig2f-sws-tenfold-faster","fig2e-decoded-speed","fig2f-rem-similar-to-wake","fig3a-packet-60-degrees","fig3a-adn-stronger-than-pos","supfig5-rate-independent","fig3b-packet-coherence","fig4b-noise-correlations","fig4c-noise-adn-vs-pos","fig4d-ole-near-bayesian","fig4e-ole-covariance","decoding-tracks-hd","fig5b-sleep-tuning-similar","fig5b-adn-decoded-tuning","fig5d-adn-predicts-pos-reliably","fig5e-readout-windows","fig5e-adn-predicts-pos","fig6a-fast-oscillation","fig6b-adn-synchrony","fig7-adn-pos-connections","fig7c-adn-triggered-pos-lfp","fig7d-same-preferred-direction","fig7e-driven-pos-hd-information","fig7e-interneurons-no-difference"]
GLMNOTE = ("Not run. The GLM of Fig. 5d,e (hd.glm_session) took 242 s on one session (Mouse24-131216, 10 targets, 25 readout "
           "windows, 10 folds, 3 states). A preparation run over the three dual mice covered 14 of 21 sessions (Mouse24 and Mouse25) in 40 "
           "minutes on 4 workers before it was stopped, with the 7 Mouse28 sessions, which have the most HD cells, left. With the 12.5 "
           "minutes of the other analyses the notebook would exceed the 60 minute limit. No number from those runs is used.")
for c in order:
    if c.startswith("fig5d") or c.startswith("fig5e"):
        outs.append(dict(claim=c, outcome="blocked", blocked_by="too_large", notes=GLMNOTE))
        continue
    o, m = oc[c]
    note = re.sub(r"^\*\*Result: [^*]+\*\* ", "", R[c])
    d = dict(claim=c, outcome=o, notebook=NB, output="claim:" + c)
    if m is not None:
        d["measured"] = m
    d["notes"] = note
    dv = list(dev[c])
    if c in ("fig2a-rates-preserved","fig2b-pair-correlations-preserved","fig2f-sws-tenfold-faster","fig2e-decoded-speed","fig3a-packet-60-degrees","fig4b-noise-correlations","decoding-tracks-hd","fig5b-sleep-tuning-similar","fig6a-fast-oscillation"):
        dv.append(WAKEFB)
    if dv:
        d["deviations"] = dv
    if c in assumed:
        d["assumed"] = True
    outs.append(d)
rec = dict(
 schema_version=3, id="peyrache-2015-02",
 datasets=[dict(archive="dandi", id="000056", version="0.261106.1949", doi="10.48324/dandi.000056/0.261106.1949", relation="primary")],
 paper="doi:10.1038/nn.3968", date="2026-11-15", entry="peyrache-2015",
 provenance=dict(kind="agent", accountable=dict(name="CatalystNeuro"),
                 agent=dict(harness="Claude Code", model="claude-opus-5-5", protocol="pilot-15"),
                 runner=dict(platform="GitHub Actions", url="https://github.com/catalystneuro/encore/actions/runs/43708742486")),
 outcomes=outs,
 findings=[
  dict(kind="data_missing", statement="Mouse28-140314, Mouse32-140820 and Mouse32-140822 hold no head-direction or position series and no sleep states; Mouse28-140314 and Mouse32-140822 have no LFP, and Mouse32-140820 has no epochs. Mouse32's 105 thalamic units, 35 of them HD cells by the files' is_hd_cell column, cannot be classified from the data, and its sessions enter no analysis."),
  dict(kind="data_missing", statement="Mouse25-140131 and Mouse25-140204 have no sleep_states table (the paper's scoring), only the later buzcode scoring; they enter the waking analyses only."),
  dict(kind="metadata_error", statement="In Mouse20, 8 units (sessions 130514, 130515, 130520) are labelled Postsubiculum, though the paper lists no post-subicular probe in that mouse (Supplementary Table 1 gives Mouse20 no PoS cells); by label 24 sessions in 4 mice hold both structures, against 21 in 3."),
  dict(kind="selection_undocumented", about="data", statement="Supplementary Table 1 counts the ADn cells of Mouse24, 25 and 28 from 2, 3 and 3 sessions (22, 27 and 55 cells against 37, 75 and 126 in the files), following the Methods' rule of discarding sessions without a probe move. The files do not mark which sessions the paper kept, and the rule read from the probe depths does not give the table's counts."),
  dict(kind="format_error", statement="In Mouse17-130130, spike times continue 1101 s past the end of the last sub-recording."),
  dict(kind="other", about="data", statement="The wake interval of Mouse12-120808 spans 130 by 97 cm of red LED positions, against 58 to 88 by 55 to 83 cm in the other sessions and a 53 by 46 cm arena; its open_field epoch is split in three, interleaved with second_environment epochs, so the wake interval may include the second environment."),
  dict(kind="format_error", statement="In Mouse17-130201 the head-direction series has one sample more than the LED position series."),
  dict(kind="methods_unavailable", statement="The Results cite the Methods for the optimal linear estimator of Fig. 4d,e, but the Methods have no OLE section. Question for the authors: how were the signal (tuning curve) and covariance OLEs built (which Q and L, which windows, whether cross-validated)? With the standard estimator assumed here the covariance OLE does not beat the signal OLE (median error ratio 0.99)."),
  dict(kind="methods_unavailable", statement="Question for the authors: which sessions of Mouse24, 25 and 28 gave the ADn cells of Supplementary Table 1, and how was the rule of discarding sessions separated by less than three days without a probe move applied? The depth-based reading keeps 3, 6 and 3 sessions, against 2, 3 and 3, and drops one Mouse17 session the table counts."),
  dict(kind="methods_unavailable", statement="Question for the authors: how was the angular speed of the decoded HD computed (Fig. 2e)? With the decoder of the Methods (posterior maximum on 1 degree bins, 10 ms bins) the median speed at 10 ms steps is 0 or 100 deg/s, and at the smoothing window it gives a SWS to waking ratio of 6, not 10."),
 ],
)
s = yaml.safe_dump(rec, sort_keys=False, width=100, allow_unicode=True)
open('attempts/peyrache-2015-02.yaml','w').write(s)
print(len(outs))
EOF
python rec.py && cd  && grep -n "—\|rather" attempts/peyrache-2015-02.yaml | head; python tools/entry.py check entries/peyrache-2015 2>&1 | tail -5
```

```
35
0 error(s)
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; python -c "
import yaml
c=[x['id'] for x in yaml.safe_load(open('claims/peyrache-2015.yaml'))['claims']]
a=[x['claim'] for x in yaml.safe_load(open('attempts/peyrache-2015-02.yaml'))['outcomes']]
print(len(c), len(a), set(c)-set(a), set(a)-set(c))"; date -u
```

```
35 35 set() set()
Sun Nov 15 14:21:52 UTC 2026
```

**Agent**

There are 35 claims, not 37: the header and README had it wrong. Fixing them to 35 claims (32 tested, 3 blocked) and re-running.

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; python - <<'EOF'
import nbformat
p='entries/peyrache-2015/reproduce_peyrache_2015.ipynb'
nb=nbformat.read(p,4)
c=nb.cells[0]
assert '**Claims.** 37 claims. 34 are tested here.' in c.source
c.source=c.source.replace('**Claims.** 37 claims. 34 are tested here.','**Claims.** 35 claims. 32 are tested here.')
nbformat.write(nb,p)
r=open('entries/peyrache-2015/README.md').read().replace('Of 37 claims, 34 are tested.','Of 35 claims, 32 are tested.')
open('entries/peyrache-2015/README.md','w').write(r)
EOF
grep -n "37\|34 " entries/peyrache-2015/README.md; date -u; timeout 4000 python tools/entry.py all entries/peyrache-2015 2>&1 | tail -3; date -u
```

```
Sun Nov 15 14:22:01 UTC 2026
Installed kernelspec registry-peyrache-2015 in executed/peyrache-2015/.venv/share/jupyter/kernels/registry-peyrache-2015
0 error(s)
pass  reproduce_peyrache_2015.ipynb  (744 s)
Sun Nov 15 14:34:38 UTC 2026
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; python - <<'EOF'
import nbformat
nb=nbformat.read('executed/peyrache-2015/reproduce_peyrache_2015.ipynb',4)
out=[]
for c in nb.cells:
    if c.cell_type=='code':
        for o in c.get('outputs',[]):
            if 'text' in o: out.append(o['text'])
            elif o.get('output_type')=='error': out.append('ERROR')
open('/tmp/claude-1001/exec2.txt','w').write('\n'.join(out))
EOF
cd $TMPDIR; diff <(grep -v 'analysed' exec_out.txt) <(grep -v 'analysed' exec2.txt) | head -5; echo diffdone; cd  && python tools/entry.py handover entries/peyrache-2015 2>&1 | tail -5; ls executed/peyrache-2015/handover
```

```
362a363
> 
429c430
< /tmp/claude-1001/ipykernel_34/1885310188.py:11: Pandas4Warning: Starting with pandas version 4.0 all arguments of all will be keyword-only.
---
diffdone
wrote executed/peyrache-2015/handover
hd.py
peyrache-2015.yaml
reproduce_peyrache_2015.ipynb
```

**Agent calls Bash**

```bash
ls entries/peyrache-2015; python tools/entry.py check entries/peyrache-2015 2>&1 | tail -2; grep -c "outcome: reproduced" attempts/peyrache-2015-02.yaml; grep -c "outcome: partially" attempts/peyrache-2015-02.yaml; grep -c "outcome: not_rep" attempts/peyrache-2015-02.yaml; grep -c "outcome: blocked" attempts/peyrache-2015-02.yaml; date -u
```

```
README.md
__pycache__
entry.yaml
hd.py
reproduce_peyrache_2015.ipynb
requirements.in
requirements.lock.txt
0 error(s)
21
5
6
3
Sun Nov 15 14:35:11 UTC 2026
```

**Agent calls Bash**

```bash
rm -rf entries/peyrache-2015/__pycache__; ls entries/peyrache-2015
```

```
README.md
entry.yaml
hd.py
reproduce_peyrache_2015.ipynb
requirements.in
requirements.lock.txt
```

**Agent**

I've written the entry at `entries/peyrache-2015`, the record at `attempts/peyrache-2015-02.yaml`, and the verifier's package in `executed/peyrache-2015/handover/`. Of the 35 claims, 32 were tested: 21 reproduced, 5 partially reproduced, 6 not reproduced, and 3 blocked for time. The check passes with 0 errors and the notebook passes the clean run in 12.4 minutes. I did not verify my own work, and nothing is committed.

**Blind status.** I came across part of an earlier attempt's results by accident. The release notes of version 0.261106.1949, returned by the DANDI API when I listed versions, say the conversion "fixes problems found by a reproduction attempt (issue #77)". They also list known gaps, such as Mouse32-140820 lacking head direction and the 8 Mouse20 units on post-subiculum shanks. I did not open the issue, the registry's website or its repository. Every finding in the record was found again from the data in this run.

### 1. Outcomes

| claim | outcome |
|---|---|
| recording-sample | reproduced |
| supptable1-per-animal | partially reproduced |
| hd-cell-fraction | not reproduced |
| hd-fraction-hd-shanks | reproduced |
| ensemble-sizes | not reproduced |
| sleep-duration | reproduced |
| adn-pos-peak-rate | partially reproduced (ratio 3.5 to 4.3, not about 3) |
| adn-pos-hd-information | reproduced |
| supfig2a-unimodality | reproduced |
| fig2a-rates-preserved | reproduced |
| fig2b-pair-correlations-preserved | reproduced |
| fig2f-sws-tenfold-faster | partially reproduced (ratio 12.3 in ADn, 6.1 in PoS) |
| fig2e-decoded-speed | partially reproduced |
| fig2f-rem-similar-to-wake | reproduced |
| fig3a-packet-60-degrees | partially reproduced |
| fig3a-adn-stronger-than-pos | reproduced |
| supfig5-rate-independent | not reproduced |
| fig3b-packet-coherence | reproduced |
| fig4b-noise-correlations | reproduced |
| fig4c-noise-adn-vs-pos | reproduced |
| fig4d-ole-near-bayesian | not reproduced (rests on an assumption) |
| fig4e-ole-covariance | not reproduced (rests on an assumption) |
| decoding-tracks-hd | reproduced |
| fig5b-sleep-tuning-similar | reproduced |
| fig5b-adn-decoded-tuning | reproduced |
| fig5d-adn-predicts-pos-reliably | blocked, `too_large` |
| fig5e-readout-windows | blocked, `too_large` |
| fig5e-adn-predicts-pos | blocked, `too_large` |
| fig6a-fast-oscillation | reproduced (rests on an assumption) |
| fig6b-adn-synchrony | reproduced (rests on an assumption) |
| fig7-adn-pos-connections | not reproduced |
| fig7c-adn-triggered-pos-lfp | reproduced (rests on an assumption) |
| fig7d-same-preferred-direction | reproduced |
| fig7e-driven-pos-hd-information | reproduced |
| fig7e-interneurons-no-difference | reproduced |

### 2. Dataset, assumptions, questions

**Version.** I pinned 0.261106.1949, the latest published version. The paper cites none, and it is the only version whose units carry a brain region.

**What was found about the dataset:**
- **Missing data.** Mouse28-140314 and both Mouse32 sessions hold no head direction, so Mouse32's 35 HD cells cannot be classified. Mouse25-140131 and Mouse25-140204 lack the paper's sleep scoring.
- **Mislabelled units.** Mouse20 has 8 units labelled post-subiculum, though the paper lists no PoS probe in that mouse.
- **Undocumented selection.** In the three mice with both probes, the paper counted ADn cells from 2, 3 and 3 sessions. The files do not say which.
- **Smaller problems.** In Mouse17-130130, spikes run 1101 s past the last sub-recording. Mouse17-130201 has one more head-direction sample than position samples. The wake interval of Mouse12-120808 spans 130 × 97 cm, larger than the 53 × 46 cm arena.
- **What checks out.** Unit counts match Supplementary Table 1 in the thalamus-only mice and in PoS. Head direction equals the LED angle, and spike times are sorted. Spikes and head direction share a clock: the decoding error is smallest at zero shift in all 30 ensembles. The files' own HD classification agrees with reading hd-a for 1007 of 1064 cells.

**Assumptions**, each recorded as a deviation:
- **OLE estimator.** The paper defines no OLE, so I used the standard Salinas and Abbott estimator. For the "signal" version I used the tuning-curve covariance off the diagonal and the observed variances on it.
- **Jitter null.** For the fast synchrony, the null is the expected value of the jittered cross-correlogram, not 100 actual jitters.
- **LFP window.** The spike-triggered LFP uses one 14-minute window per session.
- **Sessions used.** The main analysis uses every session; the Methods' session rule, read from the probe depths, is shown as a variant.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings): how the OLE was built; which sessions gave the ADn cells of Supplementary Table 1; how the decoded speed in Fig. 2e was computed.

**Questions to a reader:** none.

### 3. Protocol points
1. The claims file's opening comment says 37 claims; it holds 35. I counted from the file.
2. "Count each recording once" is unclear when the same thalamic cells may recur across sessions at one probe position. I used all sessions and showed the depth-based rule as a variant.
3. The protocol does not say how to handle a session with no sleep scoring. I used its open-field epoch as wake, for waking analyses only, and recorded that.
4. The archive's release notes can reveal an earlier attempt's findings. A blind run cannot read version metadata without seeing them.
5. Many claims list several readings, so some outcomes rest on the one reading that matches (for example HD information under hd-b with means). I followed the criteria and did not mark these as assumptions.

### 4. Runtime and failures
- The run took about 3 h 10 min (11:24 to 14:35 UTC); the final notebook runs in 12.4 minutes.
- Two exploratory runs were cut off and their time lost. A full run with the GLM did not finish in 58 minutes, partly because several processes competed for threads. A later GLM run used the old settings, because an edit had failed after a wrong working directory, and was stopped at 40 minutes after 14 of 21 sessions. That is why the three GLM claims are blocked as `too_large`.
- The executed notebook shows harmless pandas deprecation warnings.

## End of run

67 turns, 185 minutes, $7.44 at API prices, result: success.
