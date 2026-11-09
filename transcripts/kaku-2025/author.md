# 001619 · author · run 41988405043

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls claims/001619 paper entries attempts | head -50
```

```
<persisted-output>
Output too large (36.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/bff38b74-0a40-431b-a973-ca03f9cbd0c8/tool-results/b0kxeo9d0.txt

Preview (first 2KB):
Thu Nov  5 07:40:21 UTC 2026
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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/bff38b74-0a40-431b-a973-ca03f9cbd0c8/tool-results/b0kxeo9d0.txt"
}
```

```
1	Thu Nov  5 07:40:21 UTC 2026
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
[... 672 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/001619 paper entries/001453-fouke-2025 claims/001453; wc -c paper/* claims/001619/*; cat docs/archives.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat README.md | head -120; echo ----; wc -l docs/design.md
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
[... 102 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,271p docs/design.md | head -150
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
[... 130 more lines not kept]
```

**Agent**

Now the claims file.

**Agent calls Read**

```json
{
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml"
}
```

```
1	# Claims for Kaku, Liu et al. (2025), "A brainstem map of orofacial rhythms", bioRxiv
2	# doi:10.1101/2025.01.27.635041, on dandiset 001619.
3	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21,
4	# protocol pilot-10 as stated in docs/protocol.md.
5	#
6	# Text read: the bioRxiv preprint, version 1 (posted January 27, 2025), as served on its web
7	# page, stored in paper/10.1101-2025.01.27.635041.txt: main text, legends of Figures 1 to 5,
8	# Methods and references, and the supplement "Extended Data Figures" (the legends of Extended
9	# Data Figures 1 to 12, from the supplement PDF, extracted to text). The display equations of
10	# the Methods (the circular Gaussian tuning curve and the VAF) are missing from the text; the
11	# words around them name every term. The Figure 5 legend stops at panel f, although the
12	# Results cite a Figure 5g. No later version was read. Data the dandiset description names: its
13	# title and description only (no data or file was looked at).
14	#
15	# Code read: github.com/NuoLiLabBCM/KakuEtAl2025 at commit fbc0abe (2026-06-18). The preprint
16	# says "Code used for analyses will be deposited upon publication"; this repository is the one
17	# the dandiset description names as "the corresponding analysis code", and its README points
18	# at the preprint v1 and at dandiset 001619. It holds process_mat.py (unit quality filter,
19	# trial filter, tongue and inspiration onsets, lick bouts, licking and breathing phase tuning
20	# and modulation index, the lick-to-breath and breath-to-lick timing analyses of Figs 1f-i and
[... 808 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "offset": 829
}
```

```
829	  quote: Preceding a slower breath, the activity of licking neurons was slowed in anticipation of
830	    the next inspiration (Figure 4e)
831	  depends_on:
832	  - fig2-licking-breathing-tuned-counts
833	  criterion: The unit peak difference of the header (code get_peak_diff_lick_unit), slow minus
834	    fast, per licking unit, units by O1 and recordings by O2. The legend says "Same as b", the
835	    test of Fig 1g; one-sample two-tailed t-test over units at p < 0.05 (threshold a standard
836	    choice, named here). Reproduced when the mean is positive and significant under all
837	    readings; blocked as methods_underspecified when the readings disagree.
838	- id: fig4f-breathing-units-anticipate-lick
839	  statement: Preceding a slower lick, the activity of breathing neurons was slowed in
840	    anticipation of the upcoming lick.
841	  source: Results, Coupled brainstem oscillators autonomously coordinate licking and breathing,
842	    paragraph 3; Figure 4f
843	  quote: Preceding a slower lick, the activity of breathing neurons was slowed in anticipation of
844	    the upcoming lick (Figure 4f)
845	  depends_on:
846	  - fig2-licking-breathing-tuned-counts
847	  criterion: As fig4e-licking-units-anticipate-breath, with breathing units and the code's
848	    get_peak_diff_breath_unit.
[... 218 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001453-fouke-2025; cat entry.yaml requirements.in README.md; head -c 3000 omr.py; python -c "
import json;nb=json.load(open('reproduce_fouke_2025.ipynb'))
for c in nb['cells'][:12]: print(c['cell_type'],c.get('metadata'),''.join(c['source'])[:1500]); print('=====')
"
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
[... 294 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -120 attempts/001453-fouke-2025-01.yaml; grep -n "^  [a-z_]*:" attempts/001453-fouke-2025-01.yaml | sort -u -k2 | head -40; ls schemas
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
[... 144 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 195,340p attempts/001453-fouke-2025-01.yaml
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
[... 126 more lines not kept]
```

**Agent**

Now the dataset.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/001619/ | python -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/001619/versions/" | python -m json.tool | head -60
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; V=0.251027.1953; curl -s "https://api.dandiarchive.org/api/dandisets/001619/versions/$V/" > meta.json; python -c "
import json;m=json.load(open('meta.json'))
print(m.get('description')); print(m.get('assetsSummary')); print([r.get('identifier') for r in m.get('relatedResource',[])]); print(m.get('citation'))"
python - <<'EOF'
import json,urllib.request
url="https://api.dandiarchive.org/api/dandisets/001619/versions/0.251027.1953/assets/?page_size=1000"
a=[]
while url:
    d=json.load(urllib.request.urlopen(url)); a+=d['results']; url=d['next']
json.dump(a,open('assets.json','w'))
print(len(a))
import collections
for x in a[:8]: print(x['path'],x['size'])
subs=collections.Counter(x['path'].split('/')[0] for x in a); print(len(subs)); print(subs)
sz=[x['size'] for x in a]; import statistics; print(min(sz),statistics.median(sz),max(sz))
EOF
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; python -c "import pynwb,remfile,h5py,dandi;print(pynwb.__version__)" 2>&1; which uv; python --version
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pynwb,remfile,h5py,dandi;print(pynwb.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pynwb'
/opt/hostedtoolcache/Python/3.13.18/x64/bin/uv
Python 3.13.18
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q env && . env/bin/activate && uv pip install -q pynwb remfile h5py dandi numpy scipy pandas matplotlib nbformat nbclient ipykernel statsmodels astropy 2>&1 | tail -3; python -c "import pynwb;print(pynwb.__version__)"
```

```
4.2.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > peek.py <<'EOF'
import json,h5py,remfile,sys,time
a=json.load(open('assets.json'))
x=[y for y in a if y['path']==sys.argv[1]][0] if len(sys.argv)>1 else a[0]
url=f"https://api.dandiarchive.org/api/assets/{x['asset_id']}/download/"
import urllib.request
t=time.time()
f=h5py.File(remfile.File(url),'r')
def visit(name,obj):
    if isinstance(obj,h5py.Dataset):
        print(name,obj.shape,obj.dtype, dict((k,str(v)[:80]) for k,v in obj.attrs.items() if k in('unit','units','description','rate','conversion','starting_time')))
    else:
        at={k:str(v)[:100] for k,v in obj.attrs.items() if k in ('description','neurodata_type','colnames')}
        print(name+'/',at)
f.visititems(visit)
print(time.time()-t)
EOF
python peek.py 2>&1 | head -300
```

```
acquisition/ {}
analysis/ {}
analysis/probe_insertion_info/ {'colnames': "['ap_location' 'beta' 'depth' 'ml_location' 'phi' 'probe_type'\n 'recordable_brain_regions' 'skull_re", 'description': 'probe insertion info', 'neurodata_type': 'DynamicTable'}
analysis/probe_insertion_info/ap_location (1,) float64 {'description': 'ap_location'}
analysis/probe_insertion_info/beta (1,) float64 {'description': 'beta'}
analysis/probe_insertion_info/depth (1,) float64 {'description': 'depth'}
analysis/probe_insertion_info/id (1,) int64 {}
analysis/probe_insertion_info/ml_location (1,) float64 {'description': 'ml_location'}
analysis/probe_insertion_info/phi (1,) float64 {'description': 'phi'}
analysis/probe_insertion_info/probe_type (1,) object {'description': 'probe_type'}
analysis/probe_insertion_info/recordable_brain_regions (1,) object {'description': 'recordable_brain_regions'}
analysis/probe_insertion_info/skull_reference (1,) object {'description': 'skull_reference'}
analysis/probe_insertion_info/theta (1,) float64 {'description': 'theta'}
analysis/unit_metrics/ {'colnames': "['amplitude_cutoff' 'avg_firing_rate' 'cumulative_drift' 'd_prime'\n 'drift_metric' 'duration' 'halfw", 'description': 'neuron unit quality metrice', 'neurodata_type': 'DynamicTable'}
analysis/unit_metrics/amplitude_cutoff (537,) float64 {'description': 'amplitude_cutoff'}
analysis/unit_metrics/avg_firing_rate (537,) float64 {'description': 'avg_firing_rate'}
analysis/unit_metrics/cumulative_drift (537,) float64 {'description': 'cumulative_drift'}
analysis/unit_metrics/d_prime (537,) float64 {'description': 'd_prime'}
analysis/unit_metrics/drift_metric (537,) float64 {'description': 'drift_metric'}
analysis/unit_metrics/duration (537,) float64 {'description': 'duration'}
[... 107 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/NuoLiLabBCM/KakuEtAl2025 code 2>&1 | tail -2; cd code && git log --oneline | head -5; git checkout -q fbc0abe && ls -la; wc -l *.py
```

```
fbc0abe Update README.md
5b4fca4 Create README.md
0849760 Upload Kuramoto simulations
71ab4cb Update process_mat.py
c9d4127 Update README.md
total 364
drwxr-xr-x 5 runner runner   4096 Nov  5 07:41 .
drwx------ 7 runner runner   4096 Nov  5 07:41 ..
drwxr-xr-x 7 runner runner   4096 Nov  5 07:41 .git
-rw-r--r-- 1 runner runner 201713 Nov  5 07:41 CrameriColourMaps7.0.mat
drwxr-xr-x 2 runner runner   4096 Nov  5 07:41 Kuramoto_model_simulations
-rw-r--r-- 1 runner runner   1071 Nov  5 07:41 LICENSE.txt
-rw-r--r-- 1 runner runner   1553 Nov  5 07:41 README.md
-rw-r--r-- 1 runner runner   5029 Nov  5 07:41 crameri.m
-rw-r--r-- 1 runner runner   3812 Nov  5 07:41 crameri_documentation.m
-rw-r--r-- 1 runner runner   3006 Nov  5 07:41 generate_activity_maps.m
-rw-r--r-- 1 runner runner  38088 Nov  5 07:41 generate_figures.py
-rw-r--r-- 1 runner runner    548 Nov  5 07:41 loadTifFast.m
drwxr-xr-x 2 runner runner   4096 Nov  5 07:41 nwb2mat
-rw-r--r-- 1 runner runner    666 Nov  5 07:41 plotBrain.m
[... 6 more lines not kept]
```

**Agent**

The paper's code is reachable; reading it (it fixes most of the methods) and the nwb2mat converter.

**Agent calls Bash**

```bash
cd $TMPDIR/code && ls nwb2mat; cat README.md; wc -c nwb2mat/*; sed -n 1,200p process_mat.py
```

```
nwb2mat.msi
setup.exe
# KakuEtAl2025
Data analysis code for [**Kaku, Liu et al. A brainstem map of orofacial rhythms**](https://www.biorxiv.org/content/10.1101/2025.01.27.635041v1)

## Installation
#### NWB to MAT converter (MATLAB >=2024b required)
- Install nwb2mat using [setup.exe](https://github.com/NuoLiLabBCM/KakuEtAl2025/tree/main/nwb2mat). The default installation directory is `C:\Program Files\nwb2mat`.
- Add `your\MATLAB\Path\bin\win64` to PATH in environment variables. ([Help](https://www.java.com/en/download/help/path.html))


#### Environment
The environment can be installed using requirements.yml. 

`conda env create -f requirements.yml`




## Usage
[... 216 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && sed -n 200,520p process_mat.py
```

```
if (next_lick[i]==1): # num licks > 3
            lick_onset_idx.append(tongue) # index of tongue
    lick_onset_idx=np.array(lick_onset_idx)
    lick_onset_d=np.diff(lick_onset_idx)
    lick_cond_on = np.roll(lick_onset_d,1) >= 2
    lick_cond_off = lick_onset_d >= 2
    lick_bout_onset=np.argwhere(lick_cond_on)[:,0]
    lick_bout_offset=np.argwhere(lick_cond_off)[:,0]
    if lick_bout_onset[0]!=0:
        lick_bout_onset=np.concatenate((np.array([0]),lick_bout_onset)) # add first lick
        lick_bout_offset=np.concatenate((lick_bout_offset,np.array([len(lick_onset_idx)-1]))) # add last lick

    lick_onset_time=ton_onset[lick_onset_idx[lick_bout_onset]] # get onset of licks
    lick_offset_time=ton_onset[lick_onset_idx[lick_bout_offset]+2]
    
    return ton_onset, ton_offset, lick_onset_time, lick_offset_time, inspir_onset

def kuiper_two(data1, data2):
    """Compute the Kuiper statistic to compare two samples.

[... 303 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && sed -n 520,900p process_mat.py
```

```
breathing_l.append(_breathing_l)
        breathing_h.append(_breathing_h)
        mi_perm.append(_mi_perm)         
    
    return np.array(modulation_index), np.array(preferred_phase), np.array(tofitx), np.array(tofity), np.array(breathing_l), np.array(breathing_h), np.array(mi_perm)

def get_peak_diff_breath_behv(mat):
    """ """
    
    min_trial=100
    psth_s=-0.1
    psth_e=0.6
    psth_bin=np.arange(psth_s,psth_e,0.02)
    
    inspir_onset = mat[foi]['inspir_onset']
    lick_onset_time = mat[foi]['lick_bout_onset']
    lick_offset_time = mat[foi]['lick_bout_offset']
    ton_onset = mat[foi]['tongue_onset']
    
    ton_onset_l=[] # restrict by licking bouts
[... 362 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && sed -n 900,1250p process_mat.py | grep -v "^\s*$"
```

```
psth_s=-0.4
    psth_e=1
    psth_bin=np.arange(psth_s,psth_e,0.02)
    inspir_onset = mat[foi]['inspir_onset']
    lick_onset_time = mat[foi]['lick_bout_onset']
    lick_offset_time = mat[foi]['lick_bout_offset']
    ton_onset = mat[foi]['tongue_onset']
    inspir_onset_l=[] # restrict by licking bouts
    for i,val in enumerate(lick_onset_time):
        inspir_onset_l.append(inspir_onset[(inspir_onset>(lick_onset_time[i]+0.2)) & (inspir_onset<(lick_offset_time[i]-0.2))])
    inspir_onset_l=np.array(inspir_onset_l)
    inspir_onset_l=np.hstack(inspir_onset_l)
    licks = [] # lick times
    n_licks = [] # number of licks in btw breaths
    ibi = []
    lick_bef_time=[]
    lick2_time = []
    max_ibi=np.max(np.diff(inspir_onset))
    for i,_ in enumerate(inspir_onset_l[2:-2],2):
        lick=ton_onset[(ton_onset > inspir_onset_l[i-2]) & (ton_onset<inspir_onset_l[i+2])]
[... 274 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && sed -n 1250,1580p process_mat.py | grep -v "^\s*$"
```

```
Args:
        aligned_spikes (iterable):    Event aligned spike times. dims: trial x spike times
        bin_size (float):             PSTH binning size in seconds
        window (list):                PSTH start and stop in seconds
    Returns time bins, PSTH (trial x bins)
    """
    # Define the edges of the bins (1ms bins; then later convolve with 50ms window to smoothen)
    bins = np.arange(window[0], window[1] + 0.001, 0.001)
    # Initialize the histogram
    all_histograms = []
    # Compute the histogram for each trial
    for trial in aligned_spikes:
        # Compute histogram for the current trial
        hist, _ = np.histogram(trial, bins)
        all_histograms.append(hist)
    all_histograms = np.vstack(all_histograms)
    kernel = np.ones(int(bin_size*1000))/bin_size
    for i, row in enumerate(all_histograms):
        row = np.convolve(row, kernel, mode='same')
        all_histograms[i] = row
[... 270 more lines not kept]
```

**Agent**

Code is fully readable; it fixes most methods. Now measuring streaming throughput, which decides what is feasible (130 GB over 335 files).

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > speed.py <<'EOF'
import json,h5py,remfile,time,numpy as np
a=json.load(open('assets.json'))
x=a[0]
url=f"https://api.dandiarchive.org/api/assets/{x['asset_id']}/download/"
t=time.time()
f=h5py.File(remfile.File(url),'r')
b=f['processing/processing module/breathing_behavior/breathing/data']
print(b.chunks, b.compression, f['processing/processing module/breathing_behavior/breathing/timestamps'].chunks)
print(f['units/spike_times'].chunks, f['processing/DLC_tracking/side-facing_camera/jaw'].chunks)
t=time.time(); d=b[:2_000_000]; print('2M breathing', time.time()-t)
t=time.time(); idx=f['processing/processing module/breathing_behavior/breathing/data_idx'][:]; print(idx[:5], np.diff(idx)[:5])
ts=f['processing/processing module/breathing_behavior/breathing/timestamps'][:200000]; print(ts[:3], ts[124990:125010:5], time.time()-t)
t=time.time(); s=f['units/spike_times'][:]; print('spikes',time.time()-t)
t=time.time(); j=f['processing/DLC_tracking/side-facing_camera/jaw'][:]; print('jaw',time.time()-t, j[:3], j[-2:])
print(f['processing/3D_tracking/tracking_info'][:], f['processing/3D_tracking/jaw_side'][:3])
print(f['processing/DLC_tracking/side-facing_camera/Nframes'][:3,:5])
tr=f['intervals/trials']; print(tr['start_time'][:5], tr['stop_time'][:5], tr['trial_duration'][:5])
print(f['units/unit and trial pairs'][:3,:10])
for k in ['session_description','identifier','general/session_id','general/experiment_description','general/protocol','general/stimulus','general/surgery','general/data_collection','general/subject/age','general/subject/genotype','general/subject/sex','general/subject/subject_id','general/subject/description','general/source_script','general/related_publications']:
    print(k, f[k][()])
for k in f['analysis/probe_insertion_info']: print(k, f['analysis/probe_insertion_info'][k][()])
ui=f['units/unit_info']
for k in ui: print(k, ui[k][:5])
print(f['units/histology/unit_region'][:10], f['units/histology/ccf_x'][:3],f['units/histology/ccf_y'][:3],f['units/histology/ccf_z'][:3])
EOF
python speed.py
```

```
(19606,) gzip (19606,)
(19606,) (19606,)
2M breathing 0.6368257999420166
[157643 153244 150704 151639 157704] [-4399 -2540   935  6065 -2710]
[0.e+00 4.e-05 8.e-05] [4.9996 4.9998 5.     5.0002] 0.4111015796661377
spikes 1.196105718612671
jaw 0.40163540840148926 [(1, 256.47762609, 256.9534049 , 1.) (1, 256.41488314, 256.72751403, 1.)
 (1, 257.51449895, 255.77361155, 1.)] [(205, 249.41471148, 261.3196162 , 1.)
 (205, 249.72811222, 260.38911307, 1.)]
[(294.11764706, 1471, 5.0014)] [(1, 2.49097497, 0.74148746, 137.82830182)
 (1, 2.48163136, 0.7315052 , 137.78967324)
 (1, 2.51955348, 0.69094372, 137.7945733 )]
[[265.98001695 265.73646951 266.57730377 266.57639706 266.7128787 ]
 [258.06547499 245.73381805 262.81973934 258.05229485 258.2059716 ]
 [262.13928747 262.76799488 279.07508564 278.93428898 279.20772886]]
[0. 0. 0. 0. 0.] [0. 0. 0. 0. 0.] [6.1486 5.9889 5.885  5.9114 6.1659]
[[ 2  0  0  0  0  0  1  0  0  0]
 [78 44 45 30 10  7 20 21 12  9]
 [11 11  5  2  0  1  4  3  0  1]]
session_description b"'Animal `DL004` on Session `20210309_20210309_211406_s2_p2'"
[... 39 more lines not kept]
```

**Agent calls Bash**

```bash
nproc; free -g; df -h $TMPDIR | tail -1; cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import json,collections,re
a=json.load(open('assets.json'))
ses=collections.defaultdict(list)
for x in a:
    m=re.match(r'(sub-\w+)/\1_ses-(.*)-(p\d)_behavior\+core\.nwb',x['path'])
    ses[(m.group(1),m.group(2))].append(m.group(3))
print(len(ses), collections.Counter(tuple(sorted(v)) for v in ses.values()))
print(sum(x['size'] for x in a)/1e9)
EOF
```

```
4
               total        used        free      shared  buff/cache   available
Mem:              15           1          10           0           4          14
Swap:              2           0           2
/dev/root       145G   60G   86G  42% /tmp/claude-1001
173 Counter({('p1', 'p2'): 162, ('p1',): 10, ('p2',): 1})
130.07597199
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > par.py <<'EOF'
import json,h5py,remfile,time,numpy as np
from concurrent.futures import ThreadPoolExecutor
a=json.load(open('assets.json'))
def url(x): return f"https://api.dandiarchive.org/api/assets/{x['asset_id']}/download/"
def read_breath(x):
    f=h5py.File(remfile.File(url(x)),'r')
    b=f['processing/processing module/breathing_behavior/breathing/data']
    n=b.shape[0]; step=19606*20
    out=np.empty(n)
    for s in range(0,n,step): out[s:s+step]=b[s:s+step]
    return out
t=time.time()
p1=[x for x in a if 'ses-20210309-20210309-211406-s2-p1' in x['path']][0]
p2=a[0]
with ThreadPoolExecutor(2) as ex: r=list(ex.map(read_breath,[p1,p2]))
print(time.time()-t, len(r[0]), len(r[1]), np.array_equal(r[0],r[1]))
EOF
python par.py
```

```
9.673125982284546 33822623 33822623 True
Shell cwd was reset to
```

**Agent**

Both probes of a session carry identical breathing (behavior deposited twice per session; I'll read it once). Now a metadata survey of all 335 files, and a look at the paper's Methods.

**Agent calls Bash**

```bash
cd  grep -n -i -E "^(Methods|Mice|Preprocess|Behavior|Swallow|Phase|Simulation|Electrophys|Tracking|Data|Code|Statist|Breathing|Generalized|Cross|Histolog|Activity map)" paper/10.1101-2025.01.27.635041.txt | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 166,270p paper/10.1101-2025.01.27.635041.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR/code && grep -n "def \|peaks_lick\|peaks_breath\|ttest\|MI\|0.6\|0.9\|bottom\|1/3\|swallow_tuning\|pval\|count" generate_figures.py | head -120
```

```
8:def volcano_plot_licking(mat, max_ibi=None):
105:def volcano_plot_breathing(mat):
164:def volcano_plot_licking_unit(mat, unit_key, max_ibi=None):
271:def volcano_plot_breath_unit(mat, unit_key):
344:def plot_licking_swallow_summary(licks, num_after=2, num_before=4, max_ili=1/3, min_ili=1/15, split=3):
384:    #bottom 1/3rd
390:    ax.hist(del_0neg1, bins=bins, range=(bins[0], bins[-1]), density=False, color='black', linewidth=4, histtype='step', label='\u0394(0,-1)')
391:    ax.hist(del_1neg1, bins=bins, range=(bins[0], bins[-1]), density=False, color='crimson', linewidth=4, histtype='step', label='\u0394(1,-1)')
400:def plot_breath_swallow_summary(licks, num_after=2, num_before=4, max_ili=1/2, min_ili=1/15, split=3):
439:    #bottom 1/3rd
445:    ax.hist(del_0neg1, bins=bins, range=(bins[0], bins[-1]), density=False, color='black', linewidth=4, histtype='step', label='\u0394(0,-1)')
446:    ax.hist(del_1neg1, bins=bins, range=(bins[0], bins[-1]), density=False, color='crimson', linewidth=4, histtype='step', label='\u0394(1,-1)')
455:def plot_summary(export_path):
468:        indexes = np.where(breath_tunings>0.9)[0]
469:        if (indexes.size>0) & (mat['processed']['peak_diff_breath']['unit']['peaks_breath_1'].size>0) & (mat['processed']['peak_diff_breath']['unit']['peaks_breath_2'].size>0):
471:                peaks_breath_1 = np.atleast_1d(np.array(mat['processed']['peak_diff_breath']['unit']['peaks_breath_1'][_i]))
472:                peaks_breath_2 = np.atleast_1d(np.array(mat['processed']['peak_diff_breath']['unit']['peaks_breath_2'][_i]))
473:                if (peaks_breath_1.size>0) & (peaks_breath_2.size>0):
474:                    peak_diff_br_unit.append(peaks_breath_2[0]-peaks_breath_1[0])
477:        indexes = np.where(jaw_tunings>0.9)[0]
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && sed -n 344,547p generate_figures.py; sed -n 645,700p generate_figures.py; cat generate_activity_maps.m
```

```
def plot_licking_swallow_summary(licks, num_after=2, num_before=4, max_ili=1/3, min_ili=1/15, split=3):
    """ """
    ili = []
    filtered_licks = []
    for lick in licks:
        lick = np.atleast_1d(lick)
        if (lick[lick>=0].size >= num_after) & (lick[lick<0].size >= num_before): 
            before_4, before_3, before_2, before_1 = lick[lick<0][-num_before:]
            after_1, after_2 = lick[lick>=0][:num_after]
            _ili = after_1 - before_1 
            if (_ili < max_ili) & (_ili > min_ili): 
                ili.append(_ili) 
                filtered_licks.append(lick)
    ili = np.array(ili)
    sorted_ix = np.argsort(ili) 
    sorted_ix = sorted_ix[::-1] 
    licks_sorted = [filtered_licks[i] for i in sorted_ix]
    licks = licks_sorted.copy()
    
    ili_0, ili_1, ili_neg1,  = [], [], []
[... 336 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && curl -s -m 30 -o sg.json http://api.brain-map.org/api/v2/structure_graph_download/1.json; ls -la sg.json; head -c 300 sg.json; echo; curl -s -m 20 -I https://raw.githubusercontent.com/brainglobe/brainglobe-atlasapi/main/README.md | head -3
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && git ls-remote https://github.com/int-brain-lab/iblatlas HEAD; C=$(git ls-remote https://github.com/int-brain-lab/iblatlas HEAD | cut -f1); curl -s -m 30 -o ast.csv https://raw.githubusercontent.com/int-brain-lab/iblatlas/$C/iblatlas/allen_structure_tree.csv; head -3 ast.csv; wc -l ast.csv
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import json,h5py,remfile,numpy as np
a=json.load(open('assets.json'))
x=a[0]
f=h5py.File(remfile.File(f"https://api.dandiarchive.org/api/assets/{x['asset_id']}/download/"),'r')
idx=f['processing/processing module/breathing_behavior/breathing/data_idx'][:]
print(idx.sum(), f['processing/processing module/breathing_behavior/breathing/data'].shape, idx.min(), idx.max())
ts=f['processing/processing module/breathing_behavior/breathing/timestamps']
c=np.cumsum(idx)
print([ts[c[i]-1] for i in range(3)], [ts[c[i]] for i in range(3)])
pairs=f['units/unit and trial pairs'][:]
si=f['units/spike_times_index'][:]
print(pairs.sum(1)[:5], np.diff(np.r_[0,si])[:5])
st=f['units/spike_times'][:si[1]]
print(st[:10], st[pairs[0,0]-1:pairs[0,0]+3] if pairs[0,0] else None)
u1=st[si[0]:si[1]]; print(u1[:5], u1.max())
dl=f['processing/DLC_tracking/side-facing_camera/tongue'][:]
print(np.unique(dl['trial']).size, dl['likelihood'][:5])
b=f['processing/DLC_tracking/bottom-facing_camera/tongue'][:]; print(np.array_equal(dl['trial'],b['trial']))
t3=f['processing/3D_tracking/tongue_bottom'][:]; print(np.unique(t3['idx'])[:5], np.unique(t3['idx']).size)
print(f['analysis/unit_metrics/unit_amp'][:5], f['analysis/unit_metrics/avg_firing_rate'][:5], f['analysis/unit_metrics/isi_violation'][:5])
print(f['units/waveform_mean'][0,:5])
EOF
```

```
Thu Nov  5 07:44:46 UTC 2026
33822623 (33822623,) 150704 1635562
[np.float64(6.30568), np.float64(6.12972), np.float64(6.02812)] [np.float64(0.0), np.float64(0.0), np.float64(0.0)]
[  87 5965  956   59   11] [   0   87 5965  956   59]
[4.6936     5.10836667 4.9447     1.9466     6.25533333 4.9232
 6.0608     1.69566667 3.14536667 3.004     ] [5.10836667 4.9447     1.9466     6.25533333]
[4.6936     5.10836667 4.9447     1.9466     6.25533333] 24.4741
205 [9.70930923e-05 7.90945924e-05 6.32901283e-05 1.06270862e-04
 1.23683072e-04]
True
[1 2 3 4 5] 204
[91.99892241 40.93200377 45.31822045 95.61705508 59.01988636] [0.0642049  4.4021     0.705516   0.0435413  0.00811786] [0.      2.58358 1.66713 0.      0.     ]
[-0.2424569   0.5387931   1.5625     -0.16163793  3.44827586]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import json,h5py,remfile,numpy as np
a=json.load(open('assets.json'))
for x in a[:3]:
    f=h5py.File(remfile.File(f"https://api.dandiarchive.org/api/assets/{x['asset_id']}/download/"),'r')
    pairs=f['units/unit and trial pairs'][:]; si=f['units/spike_times_index'][:]; n=f['units/spike_times'].shape[0]
    tot=pairs.sum(1)
    print(si[0], np.array_equal(np.diff(si), tot[:-1]), n-si[-1]==tot[-1], tot.sum()==n, f['units/id'][:5], f['analysis/unit_metrics/id'][:5], f['units/unit_info/unit_id'][:5])
EOF
```

```
0 True True True [0 1 2 3 4] [0 1 2 3 4] [0 1 2 3 4]
0 True True True [0 1 2 3 4] [0 1 2 3 4] [0 1 2 3 4]
0 True True True [0 2 3 5 6] [0 2 3 5 6] [0 2 3 5 6]
Shell cwd was reset to
```

**Agent**

Now writing the helper module (`kaku.py`), which ports the paper's `process_mat.py` steps to streamed NWB.

**Agent calls Bash**

```bash
mkdir -p entries/001619-kaku-2025; cp $TMPDIR/ast.csv /dev/null; date -u
```

```
Thu Nov  5 07:46:51 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "entries/001619-kaku-2025/kaku.py",
 "content": "\"\"\"Loading and measures for dandiset 001619, Kaku, Liu et al. (2025), \"A brainstem map of\norofacial rhythms\", bioRxiv doi:10.1101/2025.01.27.635041.\n\nEach NWB file holds one Neuropixels insertion (probe p1 or p2) of one session: the units with\ntheir quality metrics and CCF positions (`units/histology`), the side and bottom DeepLabCut\ntracking per trial (1471 frames at 3.4 ms), the 3D tracking, and the 25 kHz airflow per trial.\nTrials are stored separately; every per-trial time starts at 0 at the trial start. The two\nprobes of a session carry the same behaviour (checked in the notebook), so behaviour is read\nonce per session. Files are streamed from the archive at the pinned version; nothing is written\nto disk.\n\nSpike times: `units/spike_times_index` holds the start offset of each unit, not its end, so the\nstandard NWB reading gives each unit the spikes of the unit before it. Spikes are read here by\nthe per-unit, per-trial spike counts of `units/unit and trial pairs`, which agree with the index\nread as starts (checked in the notebook).\n\nWhere the parameters come from. \"Code\" is the paper's analysis code, process_mat.py and\ngenerate_figures.py in https://github.com/NuoLiLabBCM/KakuEtAl2025 at commit fbc0abe, which\nthe claims file names and whose choices it adopts in its header.\n\n- Unit filter: code get_good_units (amplitude > 150 uV, ISI violation < 10, rate > 0.2 Hz,\n  presence ratio > 0.9, amplitude cutoff < 0.15); the Methods add drift metric < 0.5\n  (claims file, variant V1).\n- Trial filter: code get_good_trials.\n- Tongue onsets and offsets, lick bouts, inspiration onsets: code get_movement_timing, ported\n  line by line (tongue likelihood > 0.95 in both views; airflow z-scored, 3.4 ms moving\n  average and down-sampling, 5th-order Butterworth 1-15 Hz, Hilbert phase + pi crossing pi,\n  kept when the trace crosses -0.5 before the next onset). Times are on the code's timeline:\n  the first 1471 frames (5.0014 s) of each trial placed end to end.\n- Swallows: code detect_swallows and get_breathing, ported; swallow-aligned licks and breaths:\n  code get_licks_around_event and get_breaths_around_event.\n- Phase tuning: code get_unit_jaw_tuning and get_unit_breath_tuning (side-camera jaw_y,\n  3-15 Hz; airflow down-sampled 100 times to 250 Hz, 1-10 Hz; filtfilt; Hilbert phase + pi;\n  20 bins; spike counts divided by phase occupancy). The filter order is a reading (claims\n  file V2: Methods \"4-pole\", read as order 4 (a) or order 2 (b); the code's order 5 as a\n  variant).\n- Tuning fit: the circular Gaussian of the Methods and code (vonMise_f), with the code's bounds\n  (width 0 to pi/2, preferred phase 0 to 2 pi, amplitude and baseline >= 0). The code fits it\n  with scipy curve_fit from two starting phases; here, so that 1000 resamples per unit can be\n  fitted (claims file V3), the fit is a grid search over width and preferred phase with the\n  amplitude and baseline solved in closed form at each grid point (`fit_tuning_grid`). This is\n  a different optimiser for the same model; the notebook compares it with the code's\n  curve_fit on a sample of units. MI = (r(phi) - r(phi - pi)) / r(phi) (Methods).\n- Resampling (claims file V3): a resample of n spike phases drawn with replacement from a\n  unit's spike phases, or from the session's phases, has a multinomial histogram with the\n  observed bin probabilities; the resampled histograms are drawn that way, on the measured\n  histogram's bins (the code's np.random.choice and np.histogram give the same distribution,\n  with bin edges set by each sample's range, which differ by a small fraction of a bin).\n- Peak differences of Figs 1g, 1i, 4e and 4f: code get_peak_diff_lick_behv,\n  get_peak_diff_breath_behv, get_peak_diff_lick_unit, get_peak_diff_breath_unit, and the\n  first-peak difference of generate_figures.plot_summary.\n- Swallow modulation: code get_swallow_tuning (windows -0.3 to -0.1, -0.05 to 0.05 and 0.1 to\n  0.3 s; 1000 bootstrap resamples; at least 20 swallows); generate_activity_maps.m (mean of\n  the two MIs, max p <= 0.01, MI > 0.3). Swallow PSTH: code compute_psth (1 ms bins, 50 ms\n  boxcar, -1 to 1 s).\n\"\"\"\n\nfrom __future__ import annotations\n\nimport re\nfrom concurrent.futures import ProcessPoolExecutor\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nfrom scipy import signal, stats\n\nDANDISET_ID = \"001619\"\nDANDISET_VERSION = \"0.251027.1953\"\nAPI = \"https://api.dandiarchive.org/api\"\nONTOLOGY_URL = (\"https://raw.githubusercontent.com/int-brain-lab/iblatlas/\"\n                \"b88da5d8541d77285565fdb3f86f4f69c50b9e68/iblatlas/allen_structure_tree.csv\")\n\nFRAME_S = 0.0034           # code: bin_width\nN_FRAMES = 1471            # code: traces_len\nTRIAL_S = N_FRAMES * FRAME_S\nBREATH_FS = 25000          # Methods; the timestamps step by 4e-5 s (checked in the notebook)\nBREATH_DS = 100            # code get_unit_breath_tuning\nN_BINS = 20                # code\nFILTER_ORDERS = (4, 2, 5)  # claims file V2: (a) 4, (b) 2, code 5\nMI_TUNED = 0.6             # Results and Methods\nP_TUNED = 0.001\n\nBEH = \"processing/processing module/breathing_behavior/breathing\"\n\n\n# ----------------------------------------------------------------------------- archive\n\ndef list_assets():\n    \"\"\"Assets of the pinned version: path, asset id, size, subject, session, probe, url.\"\"\"\n    import json\n    import urllib.request\n    url = f\"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=1000\"\n    rows = []\n    while url:\n        page = json.load(urllib.request.urlopen(url))\n        rows += page[\"results\"]\n        url = page[\"next\"]\n    out = []\n    for a in rows:\n        m = re.match(r\"(sub-[^/]+)/\\1_ses-(.+)-(p\\d)_behavior\\+core\\.nwb$\", a[\"path\"])\n        out.append({\"path\": a[\"path\"], \"asset_id\": a[\"asset_id\"], \"size\": a[\"size\"],\n                    \"subject\": m.group(1)[4:], \"session\": m.group(2), \"probe\": m.group(3),\n                    \"url\": f\"{API}/assets/{a['asset_id']}/download/\"})\n    return pd.DataFrame(out).sort_values([\"subject\", \"session\", \"probe\"]).reset_index(drop=True)\n\n\ndef dandiset_metadata():\n    import json\n    import urllib.request\n    return json.load(urllib.request.urlopen(f\"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/\"))\n\n\ndef open_nwb(url):\n    return h5py.File(remfile.File(url), \"r\")\n\n\ndef _str(v):\n    if isinstance(v, bytes):\n        return v.decode().strip()\n    if isinstance(v, np.ndarray) and v.size == 1:\n        return _str(v.reshape(-1)[0])\n    return v\n\n\ndef ontology():\n    \"\"\"Allen CCF structure tree (iblatlas copy at a pinned commit): name -> acronym, path.\"\"\"\n    df = pd.read_csv(ONTOLOGY_URL)\n    df = df[df.acronym != \"void\"]\n    return df\n\n\ndef region_table(names, onto):\n    \"\"\"For each CCF region name in the files: acronym, and the major divisions (CB, P, MY, ...)\n    it falls under, from the structure-id path.\"\"\"\n    by_name = {n.lower(): r for n, r in zip(onto.name, onto.itertuples())}\n    acr_by_id = dict(zip(onto.id, onto.acronym))\n    rows = []\n    for n in sorted(set(names)):\n        r = by_name.get(n.strip().lower())\n        if r is None:\n            rows.append({\"name\": n, \"acronym\": None, \"ancestors\": ()})\n            continue\n        ids = [int(i) for i in str(r.structure_id_path).strip(\"/\").split(\"/\") if i]\n        rows.append({\"name\": n, \"acronym\": r.acronym, \"ancestors\": tuple(acr_by_id.get(i) for i in ids)})\n    return pd.DataFrame(rows)\n\n\n# ----------------------------------------------------------------------------- reading\n\ndef read_probe_meta(url):\n    \"\"\"Everything about one file except spikes, airflow and tracking arrays.\"\"\"\n    with open_nwb(url) as f:\n        m = {k: f[\"analysis/unit_metrics\"][k][:] for k in f[\"analysis/unit_metrics\"] if k != \"id\"}\n        units = pd.DataFrame(m)\n        units[\"id\"] = f[\"units/id\"][:]\n        h = f[\"units/histology\"]\n        units[\"region\"] = [_str(x) for x in h[\"unit_region\"][:]]\n        for k in (\"ccf_x\", \"ccf_y\", \"ccf_z\"):\n            units[k] = h[k][:]\n        ui = f[\"units/unit_info\"]\n        for k in ui:\n            if k != \"id\":\n                v = ui[k][:]\n                units[\"info_\" + k] = [_str(x) for x in v] if v.dtype == object else v\n        pairs = f[\"units/unit and trial pairs\"][:]\n        units[\"n_spikes\"] = pairs.sum(1)\n        si = f[\"units/spike_times_index\"][:]\n        n_st = f[\"units/spike_times\"].shape[0]\n        index_is_start = bool(si[0] == 0 and np.array_equal(np.diff(si), pairs.sum(1)[:-1])\n                              and n_st - si[-1] == pairs[-1].sum())\n        index_is_end = bool(np.array_equal(np.diff(np.r_[0, si]), pairs.sum(1)))\n        pi_ = f[\"analysis/probe_insertion_info\"]\n        insertion = {k: _str(pi_[k][()]) for k in pi_ if k != \"id\"}\n        trials = f[\"intervals/trials\"]\n        side_tr = f[\"processing/DLC_tracking/side-facing_camera/jaw\"][\"trial\"]\n        bot_tr = f[\"processing/DLC_tracking/bottom-facing_camera/jaw\"][\"trial\"]\n        meta = {\n            \"session_description\": _str(f[\"session_description\"][()]),\n            \"session_id\": _str(f[\"general/session_id\"][()]),\n            \"session_start_time\": _str(f[\"session_start_time\"][()]),\n            \"subject_id\": _str(f[\"general/subject/subject_id\"][()]),\n            \"sex\": _str(f[\"general/subject/sex\"][()]),\n            \"age\": _str(f[\"general/subject/age\"][()]),\n            \"genotype\": _str(f[\"general/subject/genotype\"][()]),\n            \"stimulus\": _str(f[\"general/stimulus\"][()]),\n            \"n_trials\": len(trials[\"id\"]),\n            \"trial_start_max\": float(np.max(trials[\"start_time\"][:])),\n            \"trial_duration_min\": float(np.min(trials[\"trial_duration\"][:])),\n            \"trial_duration_max\": float(np.max(trials[\"trial_duration\"][:])),\n            \"trial_columns\": list(_str(c) for c in trials.attrs[\"colnames\"]),\n            \"n_dlc_rows_side\": len(side_tr), \"n_dlc_rows_bottom\": len(bot_tr),\n            \"n_3d_rows\": f[\"processing/3D_tracking/tongue_bottom\"].shape[0],\n            \"tracking_info\": tuple(f[\"processing/3D_tracking/tracking_info\"][0].tolist()),\n            \"n_breath\": f[BEH + \"/data\"].shape[0],\n            \"breath_idx_sum\": int(f[BEH + \"/data_idx\"][:].sum()),\n            \"acquisition\": list(f[\"acquisition\"].keys()),\n            \"stimulus_presentation\": list(f[\"stimulus/presentation\"].keys()),\n            \"index_is_start\": index_is_start, \"index_is_end\": index_is_end,\n            \"n_units\": len(units),\n            **{\"ins_\" + k: v for k, v in insertion.items()},\n        }\n    return meta, units\n\n\ndef good_units(units, drift=False):\n    \"\"\"Code get_good_units; with drift=True also the Methods' drift metric < 0.5 (V1).\"\"\"\n    ok = ((units.presence_ratio > 0.9) & (units.amplitude_cutoff < 0.15) & (units.avg_firing_rate > 0.2)\n          & (units.isi_violation < 10) & (units.unit_amp > 150))\n    if drift:\n        ok &= units.drift_metric < 0.5\n    return ok.to_numpy()\n\n\ndef _read_dlc(f, cam):\n    g = f[f\"processing/DLC_tracking/{cam}-facing_camera\"]\n    out = {}\n    for part in (\"jaw\", \"tongue\"):\n        d = g[part][:]\n        out[part] = d\n    return out\n\n\ndef _per_trial(rec, field, trials_present, trial):\n    \"\"\"Rows of a DLC record array for one trial as an (n_frames,) array.\"\"\"\n    return rec[field][rec[\"trial\"] == trial]\n\n\ndef read_session(url, probe_urls):\n    \"\"\"Behaviour of a session (from one file) and the good units' spikes of each probe.\"\"\"\n    with open_nwb(url) as f:\n        side = _read_dlc(f, \"side\")\n        bottom = _read_dlc(f, \"bottom\")\n        info = f[\"processing/3D_tracking/tracking_info\"][0]\n        video_fs = float(info[0])\n        trial_len = float(info[2])\n        t3 = f[\"processing/3D_tracking/tongue_bottom\"][:]\n        j3 = f[\"processing/3D_tracking/jaw_side\"][:]\n        idx = f[BEH + \"/data_idx\"][:]\n        ds = f[BEH + \"/data\"]\n        n = ds.shape[0]\n        raw = np.empty(n)\n        step = ds.chunks[0] * 64 if ds.chunks else 2_000_000\n        for s in range(0, n, step):\n            raw[s:s + step] = ds[s:s + step]\n        ts0 = f[BEH + \"/timestamps\"][:3]\n    starts = np.r_[0, np.cumsum(idx)[:-1]]\n    breath_dt = float(ts0[1] - ts0[0])\n    # code get_good_trials: trials tracked in both cameras, no negative jaw likelihood\n    tr_side = np.unique(side[\"jaw\"][\"trial\"])\n    tr_bot = np.unique(bottom[\"jaw\"][\"trial\"])\n    trials = []\n    for t in np.intersect1d(tr_side, tr_bot):\n        if (side[\"jaw\"][\"likelihood\"][side[\"jaw\"][\"trial\"] == t] < 0).any():\n            continue\n        if (bottom[\"jaw\"][\"likelihood\"][bottom[\"jaw\"][\"trial\"] == t] < 0).any():\n            continue\n        trials.append(int(t))\n    trials = np.array(trials)\n\n    def frames(rec, field):\n        out = np.full((len(trials), N_FRAMES), np.nan)\n        tr = rec[\"trial\"]\n        for i, t in enumerate(trials):\n            v = rec[field][tr == t]\n            out[i, :min(len(v), N_FRAMES)] = v[:N_FRAMES]\n        return out\n\n    sess = {\n        \"video_fs\": video_fs, \"trial_len\": trial_len, \"breath_dt\": breath_dt,\n        \"n_trials_total\": len(idx), \"trials\": trials,\n        \"side_tongue_l\": frames(side[\"tongue\"], \"likelihood\"),\n        \"bottom_tongue_l\": frames(bottom[\"tongue\"], \"likelihood\"),\n        \"jaw_y\": frames(side[\"jaw\"], \"y\"),\n        \"trial_samples\": idx,\n    }\n    # 3D tongue (bottom) and jaw (side) per good trial, for protrusion and lick angle\n    t3d = np.full((len(trials), N_FRAMES, 3), np.nan)\n    j3d = np.full((len(trials), N_FRAMES, 3), np.nan)\n    for i, t in enumerate(trials):\n        for rec, out in ((t3, t3d), (j3, j3d)):\n            sel = rec[\"idx\"] == t\n            if sel.any():\n                v = np.stack([rec[\"x\"][sel], rec[\"y\"][sel], rec[\"z\"][sel]], 1)[:N_FRAMES]\n                out[i, :len(v)] = v\n    sess[\"tongue3d\"] = t3d\n    sess[\"jaw3d\"] = j3d\n    # airflow: the first 1471 frames' worth (ts < 5.0014 s) and the first 5 s, per good trial\n    n_move = int(np.sum(np.arange(int(TRIAL_S / breath_dt) + 2) * breath_dt < TRIAL_S))\n    n_tune = int(np.sum(np.arange(int(5 / breath_dt) + 2) * breath_dt < 5))\n    move = np.empty((len(trials), n_move))\n    tune = []\n    for i, t in enumerate(trials):\n        s = starts[t - 1]\n        move[i] = raw[s:s + n_move]\n        tune.append(raw[s:s + min(n_tune, idx[t - 1])][::BREATH_DS])\n    del raw\n    sess[\"breath_move\"] = move\n    sess[\"breath_tune\"] = tune\n    sess[\"n_move\"] = n_move\n    # spikes of the code's good units, per good trial, for each probe\n    sess[\"probes\"] = {}\n    for probe, purl in probe_urls.items():\n        with open_nwb(purl) as f:\n            m = {k: f[\"analysis/unit_metrics\"][k][:] for k in\n                 (\"presence_ratio\", \"amplitude_cutoff\", \"avg_firing_rate\", \"isi_violation\", \"unit_amp\", \"drift_metric\")}\n            units = pd.DataFrame(m)\n            gu = np.where(good_units(units))[0]\n            pairs = f[\"units/unit and trial pairs\"][:]\n            si = f[\"units/spike_times_index\"][:]\n            st = f[\"units/spike_times\"][:]\n        spikes = []\n        for u in gu:\n            counts = pairs[u]\n            off = np.r_[0, np.cumsum(counts)] + si[u]\n            spikes.append([np.sort(st[off[t - 1]:off[t]]) for t in trials])\n        sess[\"probes\"][probe] = {\"good_idx\": gu, \"spikes\": spikes}\n    return sess\n\n\n# ----------------------------------------------------------------------------- behaviour\n\ndef _ma_downsample(x, w):\n    \"\"\"np.convolve(x, ones(w)/w, 'same')[w::w], computed only at the kept samples.\"\"\"\n    c = np.r_[0.0, np.cumsum(x)]\n    n = len(x)\n    j = np.arange(w, n, w)\n    lo = np.clip(j - (w - 1) // 2 - (1 if w % 2 == 0 else 0), 0, n)\n    hi = np.clip(j + w // 2 + 1 - (1 if w % 2 == 0 else 0), 0, n)\n    # numpy 'same' for odd w centres the kernel; for even w it is shifted by one\n    return (c[hi] - c[lo]) / w\n\n\ndef movement_timing(sess):\n    \"\"\"Code get_movement_timing: tongue onsets and offsets, lick bouts and inspiration onsets\n    on the concatenated timeline (s).\"\"\"\n    bw = FRAME_S\n    s_l = sess[\"side_tongue_l\"]\n    b_l = sess[\"bottom_tongue_l\"]\n    tl = ((s_l > 0.95) & (b_l > 0.95)).astype(float).reshape(-1)\n    tl = tl[1:]  # code: moving average of width 1, then [window_size::window_size]\n    # airflow\n    br = sess[\"breath_move\"].reshape(-1)\n    br = (br - br.mean()) / br.std()\n    w = int(round(bw / sess[\"breath_dt\"]))\n    gb = _ma_downsample(br, w)\n    b, a = signal.butter(5, (1, 15), btype=\"band\", fs=1 / bw)\n    phase_b = np.angle(signal.hilbert(signal.filtfilt(b, a, gb))) + np.pi\n    cond = (phase_b < np.pi) & (np.roll(phase_b, -1) >= np.pi)\n    insp = np.argwhere(cond)[:, 0] * bw\n    a_cond = (gb > -0.5) & (np.roll(gb, -1) <= -0.5)\n    insp_amp = np.argwhere(a_cond)[:, 0] * bw\n    keep = [insp[i] for i in range(len(insp) - 1)\n            if np.any((insp_amp > insp[i]) & (insp_amp < insp[i + 1]))]\n    insp = np.array(keep)\n    # tongue\n    on = np.argwhere((tl < 0.5) & (np.roll(tl, -1) >= 0.5))[:, 0] * bw\n    off = np.argwhere((tl > 0.5) & (np.roll(tl, -1) <= 0.5))[:, 0] * bw\n    ton_all = on.copy()\n    ilf = 1 / np.diff(on)\n    on = on[:-1]\n    off = off[:-1]\n    idx = np.argwhere((ilf > 3) & (ilf < 9))[:, 0]\n    nxt = np.diff(idx)\n    lick_idx = np.array([t for i, t in enumerate(idx[:-2]) if nxt[i] == 1], dtype=int)\n    d = np.diff(lick_idx)\n    b_on = np.argwhere(np.roll(d, 1) >= 2)[:, 0]\n    b_off = np.argwhere(d >= 2)[:, 0]\n    if len(b_on) == 0 or b_on[0] != 0:\n        b_on = np.r_[0, b_on]\n        b_off = np.r_[b_off, len(lick_idx) - 1]\n    bout_on = on[lick_idx[b_on]]\n    bout_off = on[np.minimum(lick_idx[b_off] + 2, len(on) - 1)]\n    return {\"tongue_onset\": on, \"tongue_offset\": off, \"tongue_onset_all\": ton_all,\n            \"bout_on\": bout_on, \"bout_off\": bout_off, \"inspir_onset\": insp,\n            \"breath_ds\": gb, \"phase_b\": phase_b}\n\n\ndef get_breathing(sess):\n    \"\"\"Code get_breathing: negated z-scored 3.4 ms airflow, raw Hilbert amplitude and phase.\"\"\"\n    br = sess[\"breath_move\"].reshape(-1)\n    br = (br - br.mean()) / br.std()\n    w = int(round(FRAME_S / sess[\"breath_dt\"]))\n    gb = _ma_downsample(br, w) * -1\n    res = np.r_[gb, gb[-1]]\n    h = signal.hilbert(res)\n    n_tr = sess[\"breath_move\"].shape[0]\n    return res.reshape(n_tr, -1), np.angle(h).reshape(n_tr, -1)\n\n\ndef detect_swallows(sess, tongue_on):\n    \"\"\"Code detect_swallows: swallow onsets (frame index within trial) per trial.\"\"\"\n    fs = sess[\"video_fs\"]\n    tr_len = sess[\"trial_len\"]\n    breathing, phase = get_breathing(sess)\n    out = []\n    for i in range(breathing.shape[0]):\n        breath = np.convolve(breathing[i], np.ones(5) / 5, mode=\"same\")\n        pk, _ = signal.find_peaks(breath, distance=10)\n        ph = phase[i][pk]\n        pk = pk[(ph > 1.2) & (ph < 1.7)]\n        t0 = tr_len * i\n        ton = tongue_on[(tongue_on >= t0) & (tongue_on <= t0 + tr_len)] - t0\n        kept = []\n        if ton.size:\n            for p in pk / fs:\n                bef = np.where((ton <= p) & (ton >= p - 1.5))[0]\n                aft = np.where((ton >= p) & (ton <= p + 0.25))[0]\n                if bef.size >= 5 and aft.size >= 1 and p - ton[bef[-1]] < 0.5:\n                    ilf = 1 / np.diff(ton[bef])[-4:]\n                    if ((ilf > 3.5) & (ilf < 13)).all():\n                        kept.append(int(p * fs))\n        kept = np.array(kept)\n        vel = np.diff(breath)\n        inb = (vel >= -0.07) & (vel <= 0.07)\n        runs = []\n        count, start = 0, None\n        for j in range(len(vel)):\n            if inb[j]:\n                count += 1\n                if start is None:\n                    start = j\n            else:\n                if count >= 10:\n                    runs.append((start, start + count, count / fs))\n                count, start = 0, None\n        if count >= 2:\n            runs.append((start, start + count, count / fs))\n        val = []\n        for s, e, dur in runs:\n            if dur < 0.05:\n                continue\n            s = s + 1\n            if kept.size and np.any((kept >= s) & (kept <= e)):\n                val.append(int(s))\n        out.append(np.array(val, dtype=int))\n    return out\n\n\ndef events_around_swallows(swallows, times, tr_len):\n    \"\"\"Code get_licks_around_event / get_breaths_around_event.\"\"\"\n    fs = 1000 / 3.4\n    res = []\n    for i, ev in enumerate(swallows):\n        for el in ev:\n            start = i * tr_len\n            res.append(times[(times >= start) & (times <= start + tr_len)] - el / fs - start)\n    return res\n\n\ndef swallow_intervals(aligned, max_ili, min_ili=1 / 15, num_before=4, num_after=2):\n    \"\"\"Code plot_licking_swallow_summary / plot_breath_swallow_summary, returning cycle 0, 1\n    and -1 for every kept event, ordered by cycle 0 (longest first), and the latency of the\n    first event after the swallow.\"\"\"\n    rows = []\n    for k, lick in enumerate(aligned):\n        lick = np.atleast_1d(lick)\n        pre, post = lick[lick < 0], lick[lick >= 0]\n        if post.size >= num_after and pre.size >= num_before:\n            c0 = post[0] - pre[-1]\n            if min_ili < c0 < max_ili:\n                rows.append({\"event\": k, \"c0\": c0, \"c1\": post[1] - post[0], \"cm1\": pre[-1] - pre[-2],\n                             \"latency\": post[0], \"pre_last\": pre[-1]})\n    df = pd.DataFrame(rows)\n    if len(df):\n        df = df.iloc[np.argsort(df.c0.to_numpy(), kind=\"quicksort\")[::-1]].reset_index(drop=True)\n    return df\n\n\ndef peak_diff_lick_behv(mt, spikes=None, n_trial=None, unit=False):\n    \"\"\"Code get_peak_diff_lick_behv (unit=False) and the event selection of\n    get_peak_diff_lick_unit. Returns the selection and the behavioural peaks.\"\"\"\n    insp, ton = mt[\"inspir_onset\"], mt[\"tongue_onset\"]\n    on, off = mt[\"bout_on\"], mt[\"bout_off\"]\n    insp_l = np.hstack([insp[(insp > on[i] + 0.2) & (insp < off[i] - 0.2)] for i in range(len(on))]) if len(on) else np.array([])\n    max_ibi = np.max(np.diff(insp))\n    rows = []\n    for i in range(2, len(insp_l) - 2):\n        lick = ton[(ton > insp_l[i - 2]) & (ton < insp_l[i + 2])]\n        lick_in = lick[(lick > insp_l[i]) & (lick < insp_l[i + 1])]\n        if lick_in.size:\n            bef = lick[lick < insp_l[i]]\n            if len(bef):\n                rows.append((insp_l[i], lick - insp_l[i], lick_in[-1] - insp_l[i], bef[-1] - insp_l[i],\n                             lick_in.size, insp_l[i + 1] - insp_l[i]))\n    if not rows:\n        return None\n    t0 = np.array([r[0] for r in rows])\n    licks = [r[1] for r in rows]\n    lick2 = np.array([r[2] for r in rows])\n    lbef = np.array([r[3] for r in rows])\n    nl = np.array([r[4] for r in rows])\n    ibi = np.array([r[5] for r in rows])\n    k = ibi < max_ibi\n    t0, licks, lick2, lbef, nl, ibi = t0[k], [l for l, kk in zip(licks, k) if kk], lick2[k], lbef[k], nl[k], ibi[k]\n    rem1 = np.where((nl == 1) & (lbef > -0.05) & (lbef < 0))[0]\n    rem2 = np.where((nl == 2) & (lick2 > ibi - 0.05) & (lick2 < ibi))[0]\n    keep = np.setdiff1d(np.arange(len(ibi)), np.r_[rem1, rem2])\n    t0, licks, lbef, nl, ibi = t0[keep], [licks[i] for i in keep], lbef[keep], nl[keep], ibi[keep]\n    order = np.argsort(ibi)[::-1]\n    t0, licks, lbef, nl, ibi = t0[order], [licks[i] for i in order], lbef[order], nl[order], ibi[order]\n    out = {\"t0\": t0, \"licks\": licks, \"lick_bef\": lbef, \"n_licks\": nl, \"ibi\": ibi, \"max_ibi\": max_ibi}\n    if not (nl == 2).any():\n        return out\n    d = np.median(ibi[nl == 2])\n    i1 = np.where((ibi < d) & (nl == 2))[0]\n    i2 = np.where((ibi > d) & (nl == 2))[0]\n    out.update(i_fast=i1, i_slow=i2)\n    bins = np.arange(-0.4, 1, 0.02)\n    centres = bins[1:] - 0.01\n    if len(i1) >= 40 and len(i2) >= 40:\n        p1 = np.mean([np.histogram(licks[i], bins)[0] for i in i1], 0) / 0.02\n        p2 = np.mean([np.histogram(licks[i], bins)[0] for i in i2], 0) / 0.02\n        pk1 = _peaks(p1, centres, 5, 0.14, (0.12, 0.32))\n        pk2 = _peaks(p2, centres, 5, 0.14, (0.16, 0.36))\n        out.update(peaks_fast=pk1, peaks_slow=pk2,\n                   diff=(pk2[0] - pk1[0]) if len(pk1) and len(pk2) else np.nan)\n    else:\n        out[\"diff\"] = np.nan\n    # unit version: 40 fastest and 40 slowest (code n_trial)\n    out[\"unit_fast\"] = i1[:40]\n    out[\"unit_slow\"] = i2[-40:]\n    return out\n\n\ndef peak_diff_breath_behv(mt):\n    \"\"\"Code get_peak_diff_breath_behv (and the event selection of get_peak_diff_breath_unit).\"\"\"\n    insp, ton = mt[\"inspir_onset\"], mt[\"tongue_onset\"]\n    on, off = mt[\"bout_on\"], mt[\"bout_off\"]\n    ton_l = np.hstack([ton[(ton > on[i] + 0.2) & (ton < off[i] - 0.2)] for i in range(len(on))]) if len(on) else np.array([])\n    max_ili = np.max(np.diff(insp))\n    rows = []\n    for i in range(2, len(ton_l) - 2):\n        br = insp[(insp > ton_l[i - 2]) & (insp < ton_l[i + 2])]\n        bin_ = br[(br > ton_l[i]) & (br < ton_l[i + 1])]\n        if bin_.size:\n            rows.append((ton_l[i], br - ton_l[i], ton_l[i + 1] - ton_l[i]))\n    if not rows:\n        return None\n    t0 = np.array([r[0] for r in rows])\n    breaths = [r[1] for r in rows]\n    ili = np.array([r[2] for r in rows])\n    k = ili < max_ili\n    t0, breaths, ili = t0[k], [b for b, kk in zip(breaths, k) if kk], ili[k]\n    order = np.argsort(ili)[::-1]\n    t0, breaths, ili = t0[order], [breaths[i] for i in order], ili[order]\n    d = np.median(ili)\n    i1 = np.where(ili < d)[0]\n    i2 = np.where(ili > d)[0]\n    out = {\"t0\": t0, \"breaths\": breaths, \"ili\": ili, \"i_fast\": i1, \"i_slow\": i2}\n    bins = np.arange(-0.1, 0.6, 0.02)\n    centres = bins[1:] - 0.01\n    if len(i1) >= 100 and len(i2) >= 100:\n        p1 = np.mean([np.histogram(breaths[i], bins)[0] for i in i1], 0) / 0.02\n        p2 = np.mean([np.histogram(breaths[i], bins)[0] for i in i2], 0) / 0.02\n        pk1 = _peaks(p1, centres, 7, 0.24, (0, 0.22))\n        pk2 = _peaks(p2, centres, 7, 0.24, (0, 0.24))\n        out.update(peaks_fast=pk1, peaks_slow=pk2,\n                   diff=(pk2[0] - pk1[0]) if len(pk1) and len(pk2) else np.nan)\n    else:\n        out[\"diff\"] = np.nan\n    return out\n\n\ndef _peaks(psth, centres, min_height, dist_s, window):\n    thr = max(np.mean(psth) + np.std(psth), min_height)\n    pk = signal.find_peaks(psth, height=thr, distance=dist_s / 0.02)[0]\n    t = centres[pk]\n    return t[(t > window[0]) & (t < window[1])]\n\n\ndef unit_peak_diffs(train, t0, i_fast, i_slow, psth_s, psth_e, wins, min_height=10):\n    \"\"\"Code get_peak_diff_*_unit for one unit: spike PSTHs (20 ms bins) around the events of\n    the fast and slow groups, first peak in each window; slow minus fast.\"\"\"\n    bins = np.arange(psth_s, psth_e, 0.02)\n    centres = bins[1:] - 0.01\n    res = []\n    for idx in (i_fast, i_slow):\n        ev = t0[idx]\n        edges = ev[:, None] + bins[None, :]\n        c = np.searchsorted(train, edges.ravel(), side=\"right\").reshape(edges.shape)\n        # code keeps spikes with psth_s < t < psth_e and histograms them with right-open bins\n        cl = np.searchsorted(train, edges.ravel(), side=\"left\").reshape(edges.shape)\n        h = np.diff(cl, axis=1)\n        res.append(h.mean(0) / 0.02)\n    pk1 = _peaks(res[0], centres, min_height, 0.14 if wins[0][1] < 0.31 and psth_e > 0.9 else 0.24, wins[0])\n    pk2 = _peaks(res[1], centres, min_height, 0.14 if wins[0][1] < 0.31 and psth_e > 0.9 else 0.24, wins[1])\n    return (pk2[0] - pk1[0]) if len(pk1) and len(pk2) else np.nan\n\n\n# ----------------------------------------------------------------------------- tuning\n\ndef phases(sess):\n    \"\"\"Jaw and breathing phase (+ pi) for each filter order: jaw (trials x 1471) and breathing\n    (kept trials x 1250, with their indices).\"\"\"\n    fs = sess[\"video_fs\"]\n    jaw = sess[\"jaw_y\"]\n    n_tr = jaw.shape[0]\n    out = {\"jaw\": {}, \"breath\": {}}\n    jy = jaw.reshape(-1)\n    jy = np.where(np.isnan(jy), np.nanmean(jy), jy)\n    for order in FILTER_ORDERS:\n        b, a = signal.butter(order, (3, 15), btype=\"band\", fs=fs)\n        out[\"jaw\"][order] = (np.angle(signal.hilbert(signal.filtfilt(b, a, jy))) + np.pi).reshape(n_tr, -1)\n    n_tune = int(5 * BREATH_FS / BREATH_DS)\n    keep = np.array([i for i, d in enumerate(sess[\"breath_tune\"]) if len(d) == n_tune], dtype=int)\n    bt = np.vstack([sess[\"breath_tune\"][i] for i in keep]).reshape(-1) if len(keep) else np.array([])\n    for order in FILTER_ORDERS:\n        b, a = signal.butter(order, (1, 10), btype=\"band\", fs=BREATH_FS / BREATH_DS)\n        out[\"breath\"][order] = (np.angle(signal.hilbert(signal.filtfilt(b, a, bt))) + np.pi).reshape(len(keep), -1)\n    out[\"breath_trials\"] = keep\n    return out\n\n\ndef spike_phase_hist(spikes_by_trial, phase, fs, n_max, trial_sel=None):\n    \"\"\"Histogram (20 bins) of the phases at a unit's spikes, and the occupancy, as the code.\"\"\"\n    allp = []\n    trials = range(len(spikes_by_trial)) if trial_sel is None else trial_sel\n    for row, t in enumerate(trials):\n        idx = (spikes_by_trial[t] * fs).astype(int)\n        idx = idx[idx < n_max]\n        allp.append(phase[row][idx])\n    allp = np.hstack(allp) if allp else np.array([])\n    return allp\n\n\ndef tuning_bins(phase_all, spike_phase):\n    \"\"\"Code: counts on np.histogram(spike phases, 20) and occupancy on np.histogram(session\n    phases, 20); bin centres from the occupancy edges.\"\"\"\n    occ, edges = np.histogram(phase_all, bins=N_BINS)\n    if len(spike_phase):\n        cnt, _ = np.histogram(spike_phase, bins=N_BINS)\n    else:\n        cnt = np.zeros(N_BINS, int)\n    centres = edges[:-1] + (edges[1] - edges[0]) / 2\n    return cnt, occ, centres, edges\n\n\ndef _circ_dist(x, mu):\n    d = np.mod(np.abs(x - mu), 2 * np.pi)\n    return np.where(d > np.pi, 2 * np.pi - d, d)\n\n\n_GRID_SD = np.geomspace(0.08, np.pi / 2, 28)\n_GRID_MU = np.linspace(0, 2 * np.pi, 72, endpoint=False)\n\n\ndef _grid(centres):\n    sd, mu = np.meshgrid(_GRID_SD, _GRID_MU, indexing=\"ij\")\n    sd, mu = sd.ravel(), mu.ravel()\n    g = np.exp(-0.5 * (_circ_dist(centres[None, :], mu[:, None]) / sd[:, None]) ** 2)\n    return sd, mu, g\n\n\ndef fit_tuning_grid(Y, centres, chunk=4000):\n    \"\"\"Least-squares fit of amp * exp(-0.5 (d(x, mu)/sd)^2) + base to each row of Y (rates per\n    phase bin): grid over sd (0.08 to pi/2) and mu (5 degree steps), amp and base in closed form\n    with the code's lower bounds (>= 0). Returns MI and preferred phase per row.\"\"\"\n    sd, mu, g = _grid(centres)\n    n = Y.shape[1]\n    Sgg = (g * g).sum(1)\n    Sg1 = g.sum(1)\n    det = n * Sgg - Sg1 ** 2\n    ered = np.exp(-0.5 * (np.pi / sd) ** 2)\n    mi = np.empty(len(Y))\n    pref = np.empty(len(Y))\n    for s in range(0, len(Y), chunk):\n        y = Y[s:s + chunk]\n        yg = y @ g.T\n        sy = y.sum(1)[:, None]\n        yy = (y * y).sum(1)[:, None]\n        a = (n * yg - Sg1 * sy) / det\n        b = (Sgg * sy - Sg1 * yg) / det\n        amax = (y.max(1) + y.min(1))[:, None]\n        a = np.clip(a, 0, amax)\n        b = np.clip((sy - a * Sg1) / n, 0, y.max(1)[:, None])\n        sse = yy - 2 * (a * yg + b * sy) + a * a * Sgg + 2 * a * b * Sg1 + b * b * n\n        k = np.argmin(sse, 1)\n        r = np.arange(len(y))\n        ak, bk = a[r, k], b[r, k]\n        rmax = ak + bk\n        rmin = ak * ered[k] + bk\n        with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n            mi[s:s + chunk] = np.where(rmax > 0, (rmax - rmin) / rmax, np.nan)\n        pref[s:s + chunk] = mu[k]\n    return mi, pref\n\n\ndef code_phase_tuning(datax, datay):\n    \"\"\"The code's compute_phase_tuning (scipy curve_fit from two starts), for comparison.\"\"\"\n    from scipy import optimize\n\n    def f(x, std, mean, amp, base):\n        return amp * np.exp(-0.5 * (_circ_dist(x, np.full_like(x, mean)) / std) ** 2) + base\n\n    mx, mn = np.amax(datay), np.amin(datay)\n    mi_ = np.where(datay == mx)[0][0]\n    best = None\n    for p0m in (datax[mi_], 0):\n        try:\n            p, _ = optimize.curve_fit(f, datax, datay, p0=[1, p0m, mx - mn, mn],\n                                      bounds=(0, [np.pi / 2, 2 * np.pi, mx + mn, mx]))\n        except Exception:\n            p = [1, datax[mi_], mx - mn, mn]\n        res = datay - f(datax, *p)\n        r2 = 1 - np.sum(res ** 2) / np.sum((datay - datay.mean()) ** 2)\n        if best is None or r2 > best[0]:\n            best = (r2, p)\n    p = best[1]\n    rmax = f(np.array([p[1]]), *p)[0]\n    rmin = f(np.array([p[1] + np.pi]), *p)[0]\n    return p[1], (rmax - rmin) / rmax\n\n\ndef resample_mis(cnt, occ, centres, fs, n_res, rng):\n    \"\"\"MIs of n_res resampled histograms: (a) spike phases resampled (multinomial on the unit's\n    counts), (b) session phases resampled (multinomial on the occupancy).\"\"\"\n    n = int(cnt.sum())\n    p_sp = cnt / cnt.sum()\n    p_ss = occ / occ.sum()\n    boot = rng.multinomial(n, p_sp, size=n_res) / occ * fs\n    null = rng.multinomial(n, p_ss, size=n_res) / occ * fs\n    mi_b, _ = fit_tuning_grid(boot, centres)\n    mi_n, _ = fit_tuning_grid(null, centres)\n    return mi_b, mi_n\n\n\n# ----------------------------------------------------------------------------- swallow units\n\ndef swallow_unit_stats(spikes_by_trial, swallows, fs, rng, n_boot=1000):\n    \"\"\"Code get_swallow_aligned_spikes and get_swallow_tuning for one unit, with the peak of\n    the code's PSTH (compute_psth) for Extended Data Fig 6e and reading V4 (b).\"\"\"\n    rel = []\n    for i, ev in enumerate(swallows):\n        if len(ev) == 0:\n            continue\n        sp = (spikes_by_trial[i] * fs).astype(int)\n        sp = sp[sp < N_FRAMES]\n        for e in ev:\n            rel.append((sp - e) / fs)\n    out = {\"n\": len(rel)}\n    if len(rel) < 20:\n        return out\n    r = np.array([[np.sum((t > -0.3) & (t < -0.1)) / 0.2, np.sum((t > -0.05) & (t < 0.05)) / 0.1,\n                   np.sum((t > 0.1) & (t < 0.3)) / 0.2] for t in rel])\n    idx = rng.integers(0, len(r), size=(n_boot, len(r)))\n    rb = r[idx].mean(1)\n    m = r.mean(0)\n    p = []\n    for j in (0, 2):\n        dlt = m[1] - m[j]\n        if dlt > 0:\n            p.append(np.mean((rb[:, 1] - rb[:, j]) < 0))\n        elif dlt < 0:\n            p.append(np.mean((rb[:, 1] - rb[:, j]) > 0))\n        else:\n            p.append(1.0)\n    mi1 = (m[1] - m[0]) / max(m[1], m[0], 1e-12)\n    mi2 = (m[1] - m[2]) / max(m[1], m[2], 1e-12)\n    # PSTH: 1 ms bins, 50 ms boxcar (code compute_psth), mean over events\n    bins = np.arange(-1, 1 + 0.001, 0.001)\n    h = np.zeros(len(bins) - 1)\n    for t in rel:\n        h += np.histogram(t, bins)[0]\n    h = np.convolve(h / len(rel), np.ones(50) / 0.05, mode=\"same\")\n    c = bins[:-1]\n    w = (c >= -0.15) & (c <= 0.15)\n    peak_t = c[w][np.argmax(h[w])]\n    w50 = (c >= -0.05) & (c <= 0.05)\n    peak50 = h[w50].max()\n    mi1b = (m[1] - m[0]) / max(peak50, 1e-12)\n    mi2b = (m[1] - m[2]) / max(peak50, 1e-12)\n    out.update(rates=m, p=p, mi=(mi1 + mi2) / 2, mi_b=(mi1b + mi2b) / 2, peak_t=peak_t)\n    return out\n\n\n# ----------------------------------------------------------------------------- per session\n\ndef process_session(args):\n    \"\"\"Everything the notebook needs from one session, reduced as it loads.\"\"\"\n    key, url, probe_urls, seed = args\n    rng = np.random.default_rng(seed)\n    sess = read_session(url, probe_urls)\n    mt = movement_timing(sess)\n    sw = detect_swallows(sess, mt[\"tongue_onset\"])\n    ph = phases(sess)\n    fs = sess[\"video_fs\"]\n    out = {\"key\": key, \"n_trials_total\": sess[\"n_trials_total\"], \"n_good_trials\": len(sess[\"trials\"]),\n           \"video_fs\": fs, \"trial_len\": sess[\"trial_len\"], \"breath_dt\": sess[\"breath_dt\"],\n           \"n_move\": sess[\"n_move\"], \"n_breath_trials\": len(ph[\"breath_trials\"])}\n    out[\"mt\"] = {k: v for k, v in mt.items() if k not in (\"breath_ds\", \"phase_b\")}\n    # expiration onsets (claims file ed1bc): phase + pi crossing 0 (raw phase wrapping)\n    pb = mt[\"phase_b\"]\n    out[\"expir_onset\"] = np.argwhere((pb > np.pi) & (np.roll(pb, -1) < np.pi - 1))[:, 0] * FRAME_S\n    out[\"swallows\"] = sw\n    out[\"swallow_times\"] = np.hstack([i * sess[\"trial_len\"] + np.asarray(e) / fs for i, e in enumerate(sw)]) if sw else np.array([])\n    pdl = peak_diff_lick_behv(mt)\n    pdb = peak_diff_breath_behv(mt)\n    out[\"pd_lick\"] = None if pdl is None else {k: v for k, v in pdl.items() if k != \"licks\"}\n    if pdl is not None:\n        out[\"pd_lick\"][\"licks_fast\"] = [pdl[\"licks\"][i] for i in pdl.get(\"i_fast\", [])]\n        out[\"pd_lick\"][\"licks_slow\"] = [pdl[\"licks\"][i] for i in pdl.get(\"i_slow\", [])]\n    out[\"pd_breath\"] = None if pdb is None else {k: v for k, v in pdb.items() if k != \"breaths\"}\n    # protrusion phase per lick (ed8e): frame of the largest 3D tongue distance from its onset\n    # position, between tongue onset and offset, jaw phase there\n    prot = {o: [] for o in FILTER_ORDERS}\n    t3 = sess[\"tongue3d\"]\n    s_l, b_l = sess[\"side_tongue_l\"], sess[\"bottom_tongue_l\"]\n    vis = (s_l > 0.95) & (b_l > 0.95)\n    lick_angles = []\n    for i in range(vis.shape[0]):\n        v = vis[i].astype(int)\n        ons = np.where(np.diff(v) == 1)[0] + 1\n        offs = np.where(np.diff(v) == -1)[0] + 1\n        for o in ons:\n            e = offs[offs > o]\n            if not len(e):\n                continue\n            e = e[0]\n            seg = t3[i, o:e]\n            if np.isnan(seg).all() or len(seg) < 2:\n                continue\n            dist = np.linalg.norm(seg - seg[0], axis=1)\n            fmax = o + int(np.nanargmax(dist))\n            for order in FILTER_ORDERS:\n                prot[order].append(ph[\"jaw\"][order][i, fmax])\n            jr = sess[\"jaw3d\"][i, max(o - 10, 0):o]\n            lick_angles.append((i, o * FRAME_S, *t3[i, fmax], *(np.nanmean(jr, 0) if len(jr) else [np.nan] * 3)))\n    out[\"protrusion_phase\"] = {o: np.array(v) for o, v in prot.items()}\n    out[\"lick_tips\"] = np.array(lick_angles)\n    # units\n    units = {}\n    for probe, pr in sess[\"probes\"].items():\n        rows = []\n        for ui, sp in zip(pr[\"good_idx\"], pr[\"spikes\"]):\n            row = {\"unit_index\": int(ui), \"rate_trials\": sum(len(s) for s in sp) / (len(sp) * sess[\"trial_len\"]) if len(sp) else np.nan}\n            spf = [s[s < TRIAL_S] for s in sp]\n            train = np.hstack([s + TRIAL_S * i for i, s in enumerate(spf)]) if spf else np.array([])\n            row[\"rate_5s\"] = len(train) / (len(spf) * TRIAL_S) if len(spf) else np.nan\n            for order in FILTER_ORDERS:\n                jp = spike_phase_hist(sp, ph[\"jaw\"][order], fs, N_FRAMES - 1)\n                cnt, occ, cen, _ = tuning_bins(ph[\"jaw\"][order].reshape(-1), jp)\n                row[f\"jaw_cnt_{order}\"], row[f\"jaw_occ_{order}\"], row[f\"jaw_cen_{order}\"] = cnt, occ, cen\n                if len(ph[\"breath_trials\"]):\n                    bp = spike_phase_hist(sp, ph[\"breath\"][order], BREATH_FS / BREATH_DS,\n                                          int(5 * BREATH_FS / BREATH_DS), ph[\"breath_trials\"])\n                    cnt, occ, cen, _ = tuning_bins(ph[\"breath\"][order].reshape(-1), bp)\n                else:\n                    cnt = occ = cen = None\n                row[f\"br_cnt_{order}\"], row[f\"br_occ_{order}\"], row[f\"br_cen_{order}\"] = cnt, occ, cen\n            # peak differences (Fig 4e-f)\n            if pdl is not None and len(pdl.get(\"unit_fast\", [])) >= 40 and len(pdl.get(\"unit_slow\", [])) >= 40:\n                row[\"pd_lick_unit\"] = unit_peak_diffs(train, pdl[\"t0\"], pdl[\"unit_fast\"], pdl[\"unit_slow\"],\n                                                      -0.4, 1, ((0.1, 0.3), (0.16, 0.36)))\n            else:\n                row[\"pd_lick_unit\"] = np.nan\n            if pdb is not None and len(pdb[\"i_fast\"]) >= 100 and len(pdb[\"i_slow\"]) >= 100:\n                row[\"pd_breath_unit\"] = unit_peak_diffs(train, pdb[\"t0\"], pdb[\"i_fast\"], pdb[\"i_slow\"],\n                                                        -0.1, 0.6, ((0, 0.24), (0.02, 0.26)))\n            else:\n                row[\"pd_breath_unit\"] = np.nan\n            s = swallow_unit_stats(sp, sw, fs, rng)\n            row[\"sw_n\"] = s[\"n\"]\n            for k in (\"mi\", \"mi_b\", \"peak_t\"):\n                row[\"sw_\" + k] = s.get(k, np.nan)\n            row[\"sw_p\"] = max(s[\"p\"]) if \"p\" in s else np.nan\n            rows.append(row)\n        units[probe] = rows\n    out[\"units\"] = units\n    return out\n\n\ndef run_sessions(jobs, workers=4):\n    \"\"\"process_session over many sessions in worker processes; results in input order.\"\"\"\n    with ProcessPoolExecutor(workers) as ex:\n        return list(ex.map(process_session, jobs))\n"
}
```

```
File created successfully at: entries/001619-kaku-2025/kaku.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/001619-kaku-2025 && python - <<'EOF'
import re
s=open('kaku.py').read()
old=s[s.index('def unit_peak_diffs'):s.index('# ----------------------------------------------------------------------------- tuning')]
new='''def unit_peak_diffs(train, t0, i_fast, i_slow, psth_s, psth_e, wins, dist_s, min_height=10):
    """Code get_peak_diff_*_unit for one unit: spike PSTHs (20 ms bins) around the events of
    the fast and slow groups, first peak above max(mean + SD, 10 spikes/s) in each window;
    slow minus fast (generate_figures.plot_summary)."""
    bins = np.arange(psth_s, psth_e, 0.02)
    centres = bins[1:] - 0.01
    pks = []
    for idx, win in zip((i_fast, i_slow), wins):
        edges = t0[idx][:, None] + bins[None, :]
        c = np.searchsorted(train, edges.ravel(), side="left").reshape(edges.shape)
        psth = np.diff(c, axis=1).mean(0) / 0.02
        pks.append(_peaks(psth, centres, min_height, dist_s, win))
    return (pks[1][0] - pks[0][0]) if len(pks[0]) and len(pks[1]) else np.nan


'''
s=s.replace(old,new)
s=s.replace('''-0.4, 1, ((0.1, 0.3), (0.16, 0.36)))''','''-0.4, 1, ((0.1, 0.3), (0.16, 0.36)), 0.14)''')
s=s.replace('''-0.1, 0.6, ((0, 0.24), (0.02, 0.26)))''','''-0.1, 0.6, ((0, 0.24), (0.02, 0.26)), 0.24)''')
open('kaku.py','w').write(s)
EOF
cd $TMPDIR && . env/bin/activate && cat > t1.py <<'EOF'
import sys,time; sys.path.insert(0,'entries/001619-kaku-2025')
import kaku, numpy as np
A=kaku.list_assets()
print(len(A))
ses=A[A.session=='20210309-20210309-211406-s2']
purls=dict(zip(ses.probe,ses.url))
t=time.time()
sess=kaku.read_session(ses.url.iloc[0], purls)
print('read',time.time()-t, len(sess['trials']), sess['breath_move'].shape, {p:len(v['good_idx']) for p,v in sess['probes'].items()})
t=time.time(); mt=kaku.movement_timing(sess); print('mt',time.time()-t, len(mt['tongue_onset']), len(mt['inspir_onset']), len(mt['bout_on']))
t=time.time(); sw=kaku.detect_swallows(sess, mt['tongue_onset']); print('sw',time.time()-t, sum(len(x) for x in sw))
t=time.time(); ph=kaku.phases(sess); print('ph',time.time()-t, len(ph['breath_trials']))
t=time.time(); pdl=kaku.peak_diff_lick_behv(mt); pdb=kaku.peak_diff_breath_behv(mt); print('pd',time.time()-t, pdl['diff'], pdb['diff'], len(pdl['i_fast']), len(pdb['i_fast']))
import pickle
t=time.time(); out=kaku.process_session((('DL004','x'), ses.url.iloc[0], purls, 0)); print('full',time.time()-t)
pickle.dump(out,open('one.pkl','wb'))
EOF
python t1.py
```

```
Exit code 1
335
Traceback (most recent call last):
  File "/tmp/claude-1001/t1.py", line 8, in <module>
    sess=kaku.read_session(ses.url.iloc[0], purls)
  File "entries/001619-kaku-2025/kaku.py", line 317, in read_session
    spikes.append([np.sort(st[off[t - 1]:off[t]]) for t in trials])
                           ~~^^^^^^^^^^^^^^^^^^^
TypeError: slice indices must be integers or None or have an __index__ method
```

**Agent calls Bash**

```bash
cd entries/001619-kaku-2025 && sed -i 's|            si = f\["units/spike_times_index"\]\[:\]\n            st|X|' kaku.py && python - <<'EOF'
s=open('kaku.py').read()
s=s.replace('''            si = f["units/spike_times_index"][:]
            st = f["units/spike_times"][:]''','''            si = f["units/spike_times_index"][:].astype(np.int64)
            st = f["units/spike_times"][:]''')
s=s.replace('''            off = np.r_[0, np.cumsum(counts)] + si[u]''','''            off = np.r_[0, np.cumsum(counts)].astype(np.int64) + si[u]''')
open('kaku.py','w').write(s)
EOF
cd $TMPDIR && . env/bin/activate && python t1.py
```

```
335
read 13.962921619415283 204 (204, 125035) {'p1': 32, 'p2': 52}
mt 0.26763176918029785 1106 3599 115
sw 0.24029779434204102 85
ph 0.07534599304199219 204
pd 0.00442957878112793 nan nan 31 69
full 16.612134218215942
Shell cwd was reset to
```

**Agent**

One session processes in about 17 s, so the full pass is about 12 min with 4 workers. Next I validate the grid fit against the code's `curve_fit` before the full run.

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > t2.py <<'EOF'
import sys,time,pickle; sys.path.insert(0,'entries/001619-kaku-2025')
import kaku, numpy as np
out=pickle.load(open('one.pkl','rb'))
rows=out['units']['p1']+out['units']['p2']
fs=out['video_fs']
for mod,f in (('jaw',fs),('br',250.0)):
    Y=[];C=[]
    for r in rows:
        Y.append(r[f'{mod}_cnt_5']/r[f'{mod}_occ_5']*f); C.append(r[f'{mod}_cen_5'])
    Y=np.array(Y)
    t=time.time(); mi,pref=kaku.fit_tuning_grid(Y,C[0]); tg=time.time()-t
    t=time.time(); code=np.array([kaku.code_phase_tuning(C[i],Y[i]) for i in range(len(Y))]); tc=time.time()-t
    print(mod, 'grid s/fit',tg/len(Y),'code s/fit',tc/len(Y))
    print(np.round(np.c_[mi,code[:,1]],3)[:15].T)
    d=mi-code[:,1]; print('absdiff median, 95%', np.median(abs(d)), np.percentile(abs(d),95), 'n>0.6 grid',(mi>0.6).sum(),'code',(code[:,1]>0.6).sum())
print(out['n_good_trials'], out['pd_lick'] and out['pd_lick']['diff'])
EOF
python t2.py
```

```
jaw grid s/fit 9.127741768246605e-05 code s/fit 0.007614186831883022
[[0.069 0.092 0.187 0.264 0.277 0.03  0.024 0.355 0.036 0.172 0.104 0.318
  0.038 0.022 0.066]
 [0.036 0.092 0.141 0.534 0.277 0.03  0.024 0.618 0.035 0.173 0.12  0.404
  0.149 0.015 0.008]]
absdiff median, 95% 0.002145757868054793 0.25528481798489794 n>0.6 grid 1 code 3
br grid s/fit 7.390408288864862e-05 code s/fit 0.007095288662683396
[[0.198 0.387 0.187 0.182 0.197 0.042 0.021 0.204 0.078 0.194 0.045 0.389
  0.042 0.016 0.061]
 [0.198 0.387 0.19  0.14  0.197 0.013 0.021 0.142 0.075 0.195 0.045 0.39
  0.042 0.016 0.061]]
absdiff median, 95% 0.0009736149291569851 0.12676373358629936 n>0.6 grid 2 code 3
204 nan
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > t3.py <<'EOF'
import sys,time,pickle; sys.path.insert(0,'entries/001619-kaku-2025')
import kaku, numpy as np
out=pickle.load(open('one.pkl','rb'))
rows=out['units']['p1']+out['units']['p2']
fs=out['video_fs']
Y=np.array([r['jaw_cnt_5']/r['jaw_occ_5']*fs for r in rows]); c=rows[0]['jaw_cen_5']
def f(x, std, mean, amp, base): return amp*np.exp(-0.5*(kaku._circ_dist(x,mean)/std)**2)+base
from scipy import optimize
for i in [3,7,11,12]:
    y=Y[i]
    mi,pref=kaku.fit_tuning_grid(Y[i:i+1],c)
    cp=kaku.code_phase_tuning(c,y)
    # brute: code fit params
    mx,mn=y.max(),y.min()
    best=None
    for p0m in (c[np.argmax(y)],0):
        p,_=optimize.curve_fit(f,c,y,p0=[1,p0m,mx-mn,mn],bounds=(0,[np.pi/2,2*np.pi,mx+mn,mx]))
        sse=((y-f(c,*p))**2).sum()
        print(i,'code start',round(p0m,2),'params',np.round(p,3),'sse',round(sse,2))
    print(i,'grid mi',mi,'code mi',cp[1], 'y',np.round(y,1))
EOF
python t3.py
```

```
3 code start 2.98 params [0.088 3.132 1.62  1.416] sse 0.44
3 code start 0 params [0.05  0.    2.773 1.447] sse 0.65
3 grid mi [0.26446367] code mi 0.5337093399396945 y [1.4 1.1 1.5 1.3 1.2 1.6 1.5 1.3 1.4 1.8 1.7 1.5 1.6 1.4 1.7 1.3 1.5 1.2
 1.5 1.5]
7 code start 5.81 params [0.082 5.958 2.089 1.292] sse 0.52
7 code start 0 params [1.571 1.906 0.    1.326] sse 0.74
7 grid mi [0.35484026] code mi 0.6178375085737747 y [1.2 1.1 0.9 1.3 1.2 1.4 1.5 1.5 1.2 1.3 1.5 1.3 1.1 1.4 1.4 1.3 1.6 1.1
 1.7 1.5]
11 code start 4.24 params [0.085 4.155 0.541 0.799] sse 0.23
11 code start 0 params [1.571 1.669 0.    0.816] sse 0.33
11 grid mi [0.31832426] code mi 0.4037912832098645 y [0.7 0.5 0.9 0.8 0.9 0.9 0.8 0.9 0.9 0.8 0.8 0.7 0.8 1.1 0.8 1.  0.8 0.7
 0.6 0.9]
12 code start 5.81 params [ 0.081  5.968  9.164 52.403] sse 6.62
12 code start 0 params [ 1.571  0.     0.487 52.253] sse 9.84
12 grid mi [0.03801621] code mi 0.14884692404330727 y [51.6 51.9 53.1 52.6 51.4 53.3 52.9 53.4 51.6 52.3 52.4 52.3 51.7 53.1
 52.3 53.1 52.  52.5 53.8 53.8]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd entries/001619-kaku-2025 && python - <<'EOF'
s=open('kaku.py').read()
s=s.replace('_GRID_SD = np.geomspace(0.08, np.pi / 2, 28)','_GRID_SD = np.geomspace(0.03, np.pi / 2, 32)')
s=s.replace('with the code\'s lower bounds (>= 0). Returns MI and preferred phase per row."""','with the code\'s bounds. Returns MI and preferred phase per row."""')
s=s.replace('''    """Least-squares fit of amp * exp(-0.5 (d(x, mu)/sd)^2) + base to each row of Y (rates per
    phase bin): grid over sd (0.08 to pi/2) and mu (5 degree steps), amp and base in closed form''','''    """Least-squares fit of amp * exp(-0.5 (d(x, mu)/sd)^2) + base to each row of Y (rates per
    phase bin): grid over sd (0.03 to pi/2) and mu (5 degree steps), amp and base in closed form''')
# bounded 2-variable LS: evaluate candidates
old=s[s.index('        a = (n * yg - Sg1 * sy) / det'):s.index('        k = np.argmin(sse, 1)')]
new='''        amax = (y.max(1) + y.min(1))[:, None]
        bmax = y.max(1)[:, None]

        def sse_of(a, b):
            return yy - 2 * (a * yg + b * sy) + a * a * Sgg + 2 * a * b * Sg1 + b * b * n

        a0 = (n * yg - Sg1 * sy) / det
        b0 = (Sgg * sy - Sg1 * yg) / det
        cands = [(a0, b0)]
        a1 = np.clip(yg / Sgg, 0, amax)            # base at 0
        cands.append((a1, np.zeros_like(a1)))
        b2 = np.clip(sy / n, 0, bmax) + 0 * yg      # amp at 0
        cands.append((np.zeros_like(b2), b2))
        b3 = np.clip((sy - amax * Sg1) / n, 0, bmax)  # amp at its bound
        cands.append((amax + 0 * b3, b3))
        sse = np.full(yg.shape, np.inf)
        a = np.zeros(yg.shape)
        b = np.zeros(yg.shape)
        for ca, cb in cands:
            ok = (ca >= 0) & (ca <= amax) & (cb >= 0) & (cb <= bmax)
            e = np.where(ok, sse_of(ca, cb), np.inf)
            better = e < sse
            sse = np.where(better, e, sse)
            a = np.where(better, ca, a)
            b = np.where(better, cb, b)
'''
s=s.replace(old,new)
open('kaku.py','w').write(s)
EOF
grep -n "amax = (y.max(1) + y.min(1))\[:, None\]" kaku.py
```

```
Thu Nov  5 07:51:36 UTC 2026
669:        amax = (y.max(1) + y.min(1))[:, None]
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('kaku.py').read()
add='''

def unit_tuning(cnt, occ, cen, fs, rng, n_res=1000, n_code=100, sig_above=0.55):
    """Measured MI and preferred phase by the code's curve_fit and by the grid fit; for units
    whose MI exceeds sig_above (only these can pass MI > 0.6), the significance readings of the
    claims file V3: (a) one-sided Mann-Whitney of 1000 resampled-spike MIs against 1000
    random-phase MIs; (b) the fraction of the 1000 random-phase MIs at least as large as the
    measured (grid) MI; code, (a) with the first 100 of each."""
    from scipy.stats import mannwhitneyu
    out = {"mi": np.nan, "pref": np.nan, "mi_grid": np.nan, "pref_grid": np.nan,
           "p_a": np.nan, "p_b": np.nan, "p_code": np.nan, "n_spk": int(cnt.sum()) if cnt is not None else 0}
    if cnt is None or cnt.sum() == 0 or (occ == 0).any():
        return out
    y = cnt / occ * fs
    pref, mi = code_phase_tuning(cen, y)
    mg, pg = fit_tuning_grid(y[None, :], cen)
    out.update(mi=float(mi), pref=float(pref), mi_grid=float(mg[0]), pref_grid=float(pg[0]))
    if max(mi, mg[0]) > sig_above:
        mb, mn = resample_mis(cnt, occ, cen, fs, n_res, rng)
        out["p_a"] = float(mannwhitneyu(mb, mn, alternative="greater").pvalue)
        out["p_b"] = float(np.mean(mn >= mg[0]))
        out["p_code"] = float(mannwhitneyu(mb[:n_code], mn[:n_code], alternative="greater").pvalue)
        out["null_mi_median"] = float(np.median(mn))
    return out
'''
s=s.replace('''

# ----------------------------------------------------------------------------- swallow units''', add+'''

# ----------------------------------------------------------------------------- swallow units''')
old='''                row[f"jaw_cnt_{order}"], row[f"jaw_occ_{order}"], row[f"jaw_cen_{order}"] = cnt, occ, cen
'''
new='''                row[f"jaw_cnt_{order}"], row[f"jaw_occ_{order}"], row[f"jaw_cen_{order}"] = cnt, occ, cen
                for k, v in unit_tuning(cnt, occ, cen, fs, rng).items():
                    row[f"jaw_{k}_{order}"] = v
'''
s=s.replace(old,new)
old='''                row[f"br_cnt_{order}"], row[f"br_occ_{order}"], row[f"br_cen_{order}"] = cnt, occ, cen
'''
new='''                row[f"br_cnt_{order}"], row[f"br_occ_{order}"], row[f"br_cen_{order}"] = cnt, occ, cen
                for k, v in unit_tuning(cnt, occ, cen, BREATH_FS / BREATH_DS, rng).items():
                    row[f"br_{k}_{order}"] = v
'''
s=s.replace(old,new)
open('kaku.py','w').write(s)
EOF
cd $TMPDIR && . env/bin/activate && cat > t4.py <<'EOF'
import sys,time,pickle; sys.path.insert(0,'entries/001619-kaku-2025')
import kaku, numpy as np, pandas as pd, warnings
warnings.filterwarnings('ignore')
A=kaku.list_assets()
ses=A[A.session=='20210309-20210309-211406-s2']
purls=dict(zip(ses.probe,ses.url))
t=time.time(); out=kaku.process_session((('DL004','x'), ses.url.iloc[0], purls, 0)); print('full',time.time()-t)
pickle.dump(out,open('one.pkl','wb'))
df=pd.DataFrame(out['units']['p1']+out['units']['p2'])
print(df[[c for c in df.columns if ('_mi' in c or '_p_' in c) and c.endswith('_4')]].round(3).head(30).to_string())
EOF
python t4.py 2>&1 | tail -35
```

```
full 29.23830270767212
    jaw_mi_4  jaw_mi_grid_4  jaw_p_a_4  jaw_p_b_4  jaw_p_code_4  br_mi_4  br_mi_grid_4  br_p_a_4  br_p_b_4  br_p_code_4  jaw_null_mi_median_4  br_null_mi_median_4
0      0.037          0.068        NaN        NaN           NaN    0.197         0.196       NaN       NaN          NaN                   NaN                  NaN
1      0.093          0.093        NaN        NaN           NaN    0.390         0.390       NaN       NaN          NaN                   NaN                  NaN
2      0.181          0.184        NaN        NaN           NaN    0.191         0.192       NaN       NaN          NaN                   NaN                  NaN
3      0.146          0.243        NaN        NaN           NaN    0.207         0.208       NaN       NaN          NaN                   NaN                  NaN
4      0.238          0.242        NaN        NaN           NaN    0.207         0.210       NaN       NaN          NaN                   NaN                  NaN
5      0.029          0.029        NaN        NaN           NaN    0.016         0.051       NaN       NaN          NaN                   NaN                  NaN
6      0.024          0.024        NaN        NaN           NaN    0.022         0.022       NaN       NaN          NaN                   NaN                  NaN
7      0.421          0.289        NaN        NaN           NaN    0.141         0.208       NaN       NaN          NaN                   NaN                  NaN
8      0.032          0.033        NaN        NaN           NaN    0.076         0.077       NaN       NaN          NaN                   NaN                  NaN
9      0.188          0.187        NaN        NaN           NaN    0.193         0.280       NaN       NaN          NaN                   NaN                  NaN
10     0.033          0.033        NaN        NaN           NaN    0.044         0.051       NaN       NaN          NaN                   NaN                  NaN
11     0.150         
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001619-kaku-2025 && python - <<'EOF'
s=open('kaku.py').read()
old='''            # peak differences (Fig 4e-f)'''
new='''            # clock check: tuning with each trial's spikes paired with the next trial's phases
            sp_shift = sp[1:] + sp[:1]
            jp = spike_phase_hist(sp_shift, ph["jaw"][4], fs, N_FRAMES - 1)
            cnt, occ, cen, _ = tuning_bins(ph["jaw"][4].reshape(-1), jp)
            row["jaw_mi_shift"] = fit_tuning_grid((cnt / occ * fs)[None, :], cen)[0][0] if cnt.sum() else np.nan
            if len(ph["breath_trials"]):
                bp = spike_phase_hist(sp_shift, ph["breath"][4], BREATH_FS / BREATH_DS,
                                      int(5 * BREATH_FS / BREATH_DS), ph["breath_trials"])
                cnt, occ, cen, _ = tuning_bins(ph["breath"][4].reshape(-1), bp)
                row["br_mi_shift"] = fit_tuning_grid((cnt / occ * 250.0)[None, :], cen)[0][0] if cnt.sum() else np.nan
            # spikes from -50 to 100 ms around each lick onset (Extended Data Fig 8g), per lick
            if len(lick_angles):
                ons = np.array([la[0] * TRIAL_S + la[1] for la in lick_angles])
                row["lick_counts"] = (np.searchsorted(train, ons + 0.1) - np.searchsorted(train, ons - 0.05)).astype(np.int16)
            # peak differences (Fig 4e-f)'''
s=s.replace(old,new)
open('kaku.py','w').write(s)
EOF
cat > $TMPDIR/runall.py <<'EOF'
import sys,time,pickle; sys.path.insert(0,'entries/001619-kaku-2025')
import kaku, numpy as np, pandas as pd, warnings
warnings.filterwarnings('ignore')
A=kaku.list_assets()
jobs=[]
for i,((sub,ses),g) in enumerate(A.groupby(['subject','session'],sort=True)):
    jobs.append(((sub,ses), g.url.iloc[0], dict(zip(g.probe,g.url)), 1000+i))
if len(sys.argv)>1: jobs=jobs[:int(sys.argv[1])]
t=time.time()
res=kaku.run_sessions(jobs, workers=5)
print('time',time.time()-t, len(res))
pickle.dump(res,open(f'/tmp/claude-1001/res_{len(jobs)}.pkl','wb'))
EOF
cd $TMPDIR && . env/bin/activate && echo $TMPDIR && time python runall.py 5 2>&1 | tail -5
```

```
/tmp/claude-1001
time 85.00912380218506 5

real	1m26.131s
user	3m53.234s
sys	0m16.255s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import pickle,numpy as np,pandas as pd
res=pickle.load(open('res_5.pkl','rb'))
for r in res:
    u=pd.DataFrame([x for p in r['units'].values() for x in p])
    print(r['key'], r['n_good_trials'],'/',r['n_trials_total'], 'units',len(u), 'licks',len(r['mt']['tongue_onset']), 'insp',len(r['mt']['inspir_onset']), 'bouts',len(r['mt']['bout_on']),'sw',len(r['swallow_times']),
      'pdl',r['pd_lick'] and r['pd_lick']['diff'], r['pd_lick'] and (len(r['pd_lick'].get('i_fast',[])),len(r['pd_lick'].get('i_slow',[]))),'pdb', r['pd_breath'] and r['pd_breath']['diff'], r['pd_breath'] and len(r['pd_breath']['i_fast']))
    print('  jaw tuned', ((u.jaw_mi_4>0.6)&(u.jaw_p_a_4<0.001)).sum(), ((u.jaw_mi_4>0.6)&(u.jaw_p_b_4<0.001)).sum(), 'br', ((u.br_mi_4>0.6)&(u.br_p_a_4<0.001)).sum(),((u.br_mi_4>0.6)&(u.br_p_b_4<0.001)).sum(),
          'shift mi med', np.nanmedian(u.jaw_mi_shift), np.nanmedian(u.jaw_mi_grid_4), 'sw mod', ((u.sw_mi>0.3)&(u.sw_p<=0.01)&(u.sw_n>=20)).sum(), 'pdlu', u.pd_lick_unit.notna().sum(), 'lick_tips', r['lick_tips'].shape)
EOF
```

```
('DL004', '20210308-20210308-180033-s1') 318 / 319 units 73 licks 4373 insp 5828 bouts 235 sw 12 pdl nan (17, 17) pdb nan 61
  jaw tuned 3 3 br 2 2 shift mi med 0.08399401189687726 0.14949982666902153 sw mod 0 pdlu 0 lick_tips (3750, 8)
('DL004', '20210309-20210309-211406-s2') 204 / 205 units 84 licks 1106 insp 3599 bouts 115 sw 85 pdl nan (31, 31) pdb nan 69
  jaw tuned 1 1 br 3 1 shift mi med 0.09903831598659166 0.10666206716520894 sw mod 0 pdlu 0 lick_tips (1009, 8)
('DL004', '20210310-20210310-141528-s3') 318 / 319 units 56 licks 3540 insp 5595 bouts 369 sw 29 pdl 0.18000000000000016 (71, 71) pdb 0.0 149
  jaw tuned 14 11 br 2 0 shift mi med 0.09617055757123036 0.24058810026913302 sw mod 0 pdlu 15 lick_tips (3252, 8)
('DL004', '20210311-20210311-202018-s4') 319 / 319 units 4 licks 7081 insp 6922 bouts 486 sw 61 pdl 0.040000000000000036 (46, 46) pdb 0.01999999999999999 260
  jaw tuned 1 1 br 0 0 shift mi med 0.2568103994672822 0.48715682386352843 sw mod 0 pdlu 0 lick_tips (6171, 8)
('DL005', '20210322-20210322-153541-s2') 332 / 333 units 161 licks 3732 insp 7738 bouts 375 sw 31 pdl nan (15, 15) pdb nan 348
  jaw tuned 30 19 br 2 1 shift mi med 0.10448595872983092 0.24536936731836784 sw mod 5 pdlu 0 lick_tips (3395, 8)
Shell cwd was reset to
```

**Agent**

Five sessions look right: tuned units are found, and the trial-shifted control lowers MI. Launching the full extraction over all 173 sessions (about 35 min).

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && date -u && python runall.py 2>&1 | grep -v Warning | tail -5; date -u
```

```
Thu Nov  5 07:54:35 UTC 2026
time 4501.173037290573 173
Thu Nov  5 09:09:40 UTC 2026
Shell cwd was reset to
```

**Agent**

The full extraction ran in 75 min, over the 60-min notebook limit, so I need to profile and cut CPU before writing the notebook.

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python - <<'EOF' 2>&1 | head -40
import sys,cProfile,pstats; sys.path.insert(0,'entries/001619-kaku-2025')
import kaku, warnings; warnings.filterwarnings('ignore')
A=kaku.list_assets()
ses=A[A.session=='20210322-20210322-153541-s2']
purls=dict(zip(ses.probe,ses.url))
cProfile.run("kaku.process_session((('DL005','x'), ses.url.iloc[0], purls, 0))",'prof')
p=pstats.Stats('prof'); p.sort_stats('cumulative').print_stats(25)
EOF
```

```
Thu Nov  5 09:11:09 2026    prof

         19599954 function calls (19570440 primitive calls) in 74.012 seconds

   Ordered by: cumulative time
   List reduced from 1387 to 25 due to restriction <25>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      2/1    0.000    0.000   74.013   74.013 {built-in method builtins.exec}
        1    0.012    0.012   74.013   74.013 <string>:1(<module>)
        1    0.217    0.217   74.001   74.001 entries/001619-kaku-2025/kaku.py:819(process_session)
      966    0.018    0.000   44.632    0.046 entries/001619-kaku-2025/kaku.py:744(unit_tuning)
     1508   18.277    0.012   34.163    0.023 entries/001619-kaku-2025/kaku.py:652(fit_tuning_grid)
      110    0.983    0.009   34.099    0.310 entries/001619-kaku-2025/kaku.py:731(resample_mis)
        1    0.550    0.550   22.624   22.624 entries/001619-kaku-2025/kaku.py:230(read_session)
       99    0.001    0.000   20.432    0.206 /tmp/claude-1001/env/lib/python3.13/site-packages/requests/sessions.py:557(request)
   198/99    0.003    0.000   20.367    0.206 /tmp/claude-1001/env/lib/python3.13/site-packages/requests/sessions.py:752(send)
     3743    0.019    0.000   19.273    0.005 /tmp/claude-1001/env/lib/python3.13/site-packages/remfile/RemFile.py:87(read)
     5749    0.020    0.000   19.248    0.003 /tmp/claude-1001/env/lib/python3.13/site-packages/remfile/RemFile.py:156(_load_chunk)
       96    0.001    0.000   19.227    0.200 /tmp/claude-1001/env/lib/python3.13/site-packages/remfile/RemFile.py:357(_get_bytes)
[... 14 more lines not kept]
```

**Agent**

Resampled grid fits take half the CPU. I'm shrinking the grid, using float32, and computing significance only for units whose code MI is above 0.6, since no other unit can count as tuned.

**Agent calls Bash**

```bash
cd entries/001619-kaku-2025 && python - <<'EOF'
s=open('kaku.py').read()
s=s.replace('_GRID_SD = np.geomspace(0.03, np.pi / 2, 32)\n_GRID_MU = np.linspace(0, 2 * np.pi, 72, endpoint=False)','_GRID_SD = np.geomspace(0.03, np.pi / 2, 24)\n_GRID_MU = np.linspace(0, 2 * np.pi, 48, endpoint=False)')
s=s.replace('phase bin): grid over sd (0.03 to pi/2) and mu (5 degree steps)','phase bin): grid over sd (24 steps, 0.03 to pi/2) and mu (7.5 degree steps)')
s=s.replace('''    for s in range(0, len(Y), chunk):
        y = Y[s:s + chunk]''','''    g = g.astype(np.float32)
    Sgg, Sg1, det = Sgg.astype(np.float32), Sg1.astype(np.float32), det.astype(np.float32)
    for s in range(0, len(Y), chunk):
        y = Y[s:s + chunk].astype(np.float32)''')
s=s.replace('def unit_tuning(cnt, occ, cen, fs, rng, n_res=1000, n_code=100, sig_above=0.55):','def unit_tuning(cnt, occ, cen, fs, rng, n_res=1000, n_code=100, sig_above=MI_TUNED):')
s=s.replace('''    """Measured MI and preferred phase by the code's curve_fit and by the grid fit; for units
    whose MI exceeds sig_above (only these can pass MI > 0.6), the significance readings''','''    """Measured MI and preferred phase by the code's curve_fit and by the grid fit; for units
    whose measured (code) MI exceeds sig_above (only these can pass MI > 0.6), the significance readings''')
s=s.replace('    if max(mi, mg[0]) > sig_above:','    if mi > sig_above:')
open('kaku.py','w').write(s)
EOF
cd $TMPDIR && . env/bin/activate && python - <<'EOF' 2>&1 | grep -E "seconds|unit_tuning|fit_tuning_grid|read_session|curve_fit"
import sys,cProfile,pstats; sys.path.insert(0,'entries/001619-kaku-2025')
import kaku, warnings; warnings.filterwarnings('ignore')
A=kaku.list_assets()
ses=A[A.session=='20210322-20210322-153541-s2']
purls=dict(zip(ses.probe,ses.url))
cProfile.run("kaku.process_session((('DL005','x'), ses.url.iloc[0], purls, 0))",'prof')
p=pstats.Stats('prof'); p.sort_stats('cumulative').print_stats(40)
EOF
```

```
19563513 function calls (19534025 primitive calls) in 46.027 seconds
      966    0.018    0.000   19.998    0.021 entries/001619-kaku-2025/kaku.py:746(unit_tuning)
        1    0.567    0.567   19.259   19.259 entries/001619-kaku-2025/kaku.py:230(read_session)
     1482    6.709    0.005    9.845    0.007 entries/001619-kaku-2025/kaku.py:652(fit_tuning_grid)
     1932    0.047    0.000    9.725    0.005 /tmp/claude-1001/env/lib/python3.13/site-packages/scipy/optimize/_minpack_py.py:590(curve_fit)
Shell cwd was reset to
```

**Agent**

Now 46 s per session (about 25-30 min for all). Next, the metadata survey of all 335 files for the unit counts and region claims.

**Agent calls Bash**

```bash
cd entries/001619-kaku-2025 && cat >> kaku.py <<'EOF'


def _meta_job(url):
    return read_probe_meta(url)


def survey(assets, workers=8):
    """read_probe_meta over every file: a table of files and a table of all units."""
    with ProcessPoolExecutor(workers) as ex:
        res = list(ex.map(_meta_job, assets.url))
    files, units = [], []
    for (meta, u), row in zip(res, assets.itertuples()):
        files.append({"subject": row.subject, "session": row.session, "probe": row.probe, **meta})
        u = u.copy()
        u["subject"], u["session"], u["probe"] = row.subject, row.session, row.probe
        units.append(u)
    return pd.DataFrame(files), pd.concat(units, ignore_index=True)
EOF
cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import sys,time,pickle; sys.path.insert(0,'entries/001619-kaku-2025')
import kaku, warnings; warnings.filterwarnings('ignore')
A=kaku.list_assets()
t=time.time(); files,units=kaku.survey(A); print(time.time()-t)
pickle.dump((files,units),open('survey.pkl','wb'))
print(files.iloc[0].to_dict())
EOF
```

```
Exit code 1
concurrent.futures.process._RemoteTraceback: 
"""
Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/concurrent/futures/process.py", line 255, in _process_worker
    r = call_item.fn(*call_item.args, **call_item.kwargs)
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/concurrent/futures/process.py", line 204, in _process_chunk
    return [fn(*args) for args in chunk]
            ~~^^^^^^^
  File "entries/001619-kaku-2025/kaku.py", line 940, in _meta_job
    return read_probe_meta(url)
  File "entries/001619-kaku-2025/kaku.py", line 159, in read_probe_meta
    units["region"] = [_str(x) for x in h["unit_region"][:]]
    ~~~~~^^^^^^^^^^
  File "/tmp/claude-1001/env/lib/python3.13/site-packages/pandas/core/frame.py", line 4659, in __setitem__
    self._set_item(key, value)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "/tmp/claude-1001/env/lib/python3.13/site-packages/pandas/core/frame.py", line 4895, in _set_item
    value, refs = self._sanitize_column(value)
                  ~~~~~~~~~~~~~~~~~~~~~^^^^^^^
[... 31 more lines not kept]
```

**Agent**

A finding: in some files the histology table has more rows than the unit metrics (1129 against 1122). I'll record each table's length per file and align by position, as the paper's code indexes them.

**Agent calls Bash**

```bash
cd entries/001619-kaku-2025 && python - <<'EOF'
s=open('kaku.py').read()
old=s[s.index('        m = {k: f["analysis/unit_metrics"][k][:] for k in f["analysis/unit_metrics"] if k != "id"}\n        units = pd.DataFrame(m)\n        units["id"] = f["units/id"][:]'):s.index('        pairs = f["units/unit and trial pairs"][:]\n        units["n_spikes"]')]
new='''        m = {k: f["analysis/unit_metrics"][k][:] for k in f["analysis/unit_metrics"] if k != "id"}
        units = pd.DataFrame(m)
        n = len(units)
        lengths = {"metrics": n, "units_id": len(f["units/id"]),
                   "histology": len(f["units/histology/unit_region"]),
                   "unit_info": len(f["units/unit_info/unit_id"]),
                   "pairs": f["units/unit and trial pairs"].shape[0],
                   "spike_index": len(f["units/spike_times_index"])}

        def put(col, v):
            v = np.asarray(v, dtype=object if isinstance(v[0], str) else None) if len(v) else np.array([])
            out = np.full(n, None if v.dtype == object else np.nan, dtype=v.dtype if v.dtype == object else float)
            k = min(n, len(v))
            out[:k] = v[:k]
            units[col] = out

        put("id", f["units/id"][:])
        put("metric_id", f["analysis/unit_metrics/id"][:])
        h = f["units/histology"]
        put("region", [_str(x) for x in h["unit_region"][:]])
        for k in ("ccf_x", "ccf_y", "ccf_z"):
            put(k, h[k][:])
        ui = f["units/unit_info"]
        for k in ui:
            if k != "id":
                v = ui[k][:]
                put("info_" + k, [_str(x) for x in v] if v.dtype == object else v)
'''
s=s.replace(old,new)
s=s.replace('''        pairs = f["units/unit and trial pairs"][:]
        units["n_spikes"] = pairs.sum(1)''','''        pairs = f["units/unit and trial pairs"][:]
        put("n_spikes", pairs.sum(1))''')
s=s.replace('''            "n_units": len(units),''','''            "n_units": len(units), **{"len_" + k: v for k, v in lengths.items()},''')
open('kaku.py','w').write(s)
EOF
cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import sys,time,pickle; sys.path.insert(0,'entries/001619-kaku-2025')
import kaku, warnings; warnings.filterwarnings('ignore')
A=kaku.list_assets()
t=time.time(); files,units=kaku.survey(A); print(time.time()-t)
pickle.dump((files,units),open('survey.pkl','wb'))
print(files.iloc[0].to_dict())
L=files[[c for c in files.columns if c.startswith('len_')]]
print(L[(L.nunique(axis=1)>1)].assign(path=files.subject+'/'+files.session+files.probe).to_string())
EOF
```

```
208.89863896369934
{'subject': 'DL004', 'session': '20210308-20210308-180033-s1', 'probe': 'p1', 'session_description': "'Animal `DL004` on Session `20210308_20210308_180033_s1_p1'", 'session_id': '20210308_20210308_180033_s1_p1', 'session_start_time': '2025-08-29T13:27:14.701-04:00', 'subject_id': 'DL004', 'sex': 'M', 'age': 'P273W', 'genotype': 'animalStrain: 014548; animalGeneModification: Cg-Tg(Slc32a1-COP4*H134R/EYFP)8Gfng/J; animalGeneCopy: 1; animalGeneticBackground: unidentified', 'stimulus': 'photostim', 'n_trials': 319, 'trial_start_max': 0.0, 'trial_duration_min': 5.8286, 'trial_duration_max': 15.738, 'trial_columns': ['trial_duration', 'start_time', 'stop_time', 'trial_duration'], 'n_dlc_rows_side': 469249, 'n_dlc_rows_bottom': 469249, 'n_3d_rows': 467778, 'tracking_info': (294.11764705882354, 1471, 5.0014), 'n_breath': 52494152, 'breath_idx_sum': 52494152, 'acquisition': [], 'stimulus_presentation': [], 'index_is_start': True, 'index_is_end': False, 'n_units': 518, 'len_metrics': 518, 'len_units_id': 518, 'len_histology': 518, 'len_unit_info': 518, 'len_pairs': 518, 'len_spike_index': 518, 'ins_ap_location': -1200.0, 'ins_beta': 90.0, 'ins_depth': -5417.0, 'ins_ml_location': 1700.0, 'ins_phi': 40.0, 'ins_probe_type': 'neuropixels 1.0 - 3B', 'ins_recordable_brain_regions': 'right Medulla', 'ins_skull_reference': 'Lambda', 'ins_theta': 20.0}
     len_metrics  len_units_id  len_histology  len_unit_info  len_pairs  len_spike_index                                 path
30          1122          1122           1129           1122       1122             1122  DL007/20210412-20210412-202840-s4p2
37           519           519            529            519        519              519  DL009/20210419-20210419-134252-s7p1
83           967           967            974            967        967              967  DL016/20210525-20210525-142851-s7p1
94           838           838            849            838        838              838  DL017/20210710-20210710-185624-
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import sys,pickle; sys.path.insert(0,'entries/001619-kaku-2025')
import kaku, numpy as np, pandas as pd
files,units=pickle.load(open('survey.pkl','rb'))
onto=kaku.ontology()
rt=kaku.region_table(units.region.dropna().unique(), onto)
print(rt[rt.acronym.isna()])
print(len(rt))
units=units.merge(rt,left_on='region',right_on='name',how='left')
g=kaku.good_units(units); gd=kaku.good_units(units,drift=True)
print('all',len(units),'good',g.sum(),'good+drift',gd.sum())
anc=units.ancestors.apply(lambda a: a if isinstance(a,tuple) else ())
for d in ['CB','P','MY','MB','HB','VNC','IRN','PARN','XII','V','AMB','NTS','IC','NLL','FN','IP','DN']:
    m=anc.apply(lambda a: d in a)
    print(d, (m&g).sum(), (m&gd).sum())
print(units[g].groupby(['subject','session','probe']).size().describe())
print('mice',files.subject.nunique(),'files',len(files),'sessions',files.groupby(['subject','session']).ngroups)
print(files.sex.groupby(files.subject).first().value_counts(), files.age.unique()[:10], files.stimulus.unique(), files.genotype.unique()[:3])
print(units[g].region.value_counts().head(40))
print(files.ins_recordable_brain_regions.value_counts().head())
print(files.ins_probe_type.value_counts())
EOF
```

```
name acronym ancestors
0                                                          NaN        ()
25                Inferior colliculus, central nucleus     NaN        ()
26                 Inferior colliculus, dorsal nucleus     NaN        ()
27               Inferior colliculus, external nucleus     NaN        ()
34       Lateral reticular nucleus, magnocellular part     NaN        ()
35       Lateral reticular nucleus, parvicellular part     NaN        ()
45            Medullary reticular nucleus, dorsal part     NaN        ()
46           Medullary reticular nucleus, ventral part     NaN        ()
49        Midbrain reticular nucleus, retrorubral area     NaN        ()
53                   Nucleus ambiguus, dorsal division     NaN        ()
54                  Nucleus ambiguus, ventral division     NaN        ()
69   Paragigantocellular reticular nucleus, dorsal ...     NaN        ()
70   Paragigantocellular reticular nucleus, lateral...     NaN        ()
85              Pontine reticular nucleus, caudal part     NaN        ()
87                 Posterolateral visual area, layer 1     NaN        ()
88               Posterolateral visual area, layer 2/3     NaN        ()
89                 Posterolateral visual area, layer 4     NaN        ()
90                 Posterolateral visual area, layer 5     NaN        ()
91                Posterolateral visual area, layer 6a     NaN        ()
[... 118 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -i "inferior colliculus" ast.csv | cut -c1-200 | head; grep -i "ambiguus" ast.csv | cut -c1-150
```

```
4,141,Inferior colliculus,IC,,1,3,8690,339,5,1,812,/997/8/343/313/339/4/,FF7AFF,,,f,813,3456805092,734881840,Inferior colliculus
811,808,Inferior colliculus central nucleus,ICc,,1,3,8690,4,6,1,813,/997/8/343/313/339/4/811/,FF7AFF,,,f,814,3750101210,734881840,Inferior colliculus central nucleus
820,809,Inferior colliculus dorsal nucleus,ICd,,1,3,8690,4,6,1,814,/997/8/343/313/339/4/820/,FF7AFF,,,f,815,3008108572,734881840,Inferior colliculus dorsal nucleus
828,810,Inferior colliculus external nucleus,ICe,,1,3,8690,4,6,1,815,/997/8/343/313/339/4/828/,FF7AFF,,,f,816,754697579,734881840,Inferior colliculus external nucleus
580,213,Nucleus of the brachium of the inferior colliculus,NB,,1,3,8690,339,5,1,816,/997/8/343/313/339/580/,FF7AFF,,,f,817,3573918372,734881840,Nucleus of the brachium of the inferior colliculus
633,503,inferior colliculus commissure,cic,,1,3,8690,948,5,1,1141,/997/1009/967/933/948/633/,CCCCCC,,,f,1142,1506772234,734881840,inferior colliculus commissure
482,484,brachium of the inferior colliculus,bic,,1,3,8690,948,5,1,1142,/997/1009/967/933/948/482/,CCCCCC,,,f,1143,2423549855,734881840,brachium of the inferior colliculus
135,16,Nucleus ambiguus,AMB,,1,3,8690,370,6,1,970,/997/8/343/1065/354/370/135/,FFB3D9,,,f,971,1540571580,734881840,Nucleus ambiguus
939,824,Nucleus ambiguus dorsal division,AMBd,,1,3,8690,135,7,1,971,/997/8/343/1065/354/370/135/939/,FFB3D9,,,f,972,2183877720,734881840,Nucleus ambig
143,17,Nucleus ambiguus ventral division,AMBv,,1,3,8690,135,7,1,972,/997/8/343/1065/354/370/135/143/,FFB3D9,,,f,973,1830643471,734881840,Nucleus ambig
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/001619-kaku-2025 && python - <<'EOF'
s=open('kaku.py').read()
s=s.replace('''    by_name = {n.lower(): r for n, r in zip(onto.name, onto.itertuples())}''','''    def norm(n):  # the iblatlas copy drops the commas of the Allen names
        return " ".join(str(n).replace(",", " ").lower().split())

    by_name = {norm(n): r for n, r in zip(onto.name, onto.itertuples())}''')
s=s.replace('''        r = by_name.get(n.strip().lower())''','''        r = by_name.get(norm(n))''')
open('kaku.py','w').write(s)
EOF
cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import sys,pickle; sys.path.insert(0,'entries/001619-kaku-2025')
import kaku, numpy as np, pandas as pd
files,units=pickle.load(open('survey.pkl','rb'))
onto=kaku.ontology()
rt=kaku.region_table(units.region.dropna().unique(), onto)
print(rt[rt.acronym.isna()])
units=units.merge(rt,left_on='region',right_on='name',how='left')
g=kaku.good_units(units)
anc=units.ancestors.apply(lambda a: a if isinstance(a,tuple) else ())
for d in ['CB','P','MY','MB','HB','fiber tracts','VS','VNC','AMB','IC','NLL','arb','CTX','grey']:
    m=anc.apply(lambda a: d in a)
    print(d, (m&g).sum())
print(units[g&anc.apply(lambda a: not any(d in a for d in ['CB','P','MY']))].region.value_counts().to_string())
EOF
```

```
name acronym ancestors
0          NaN        ()
CB 4157
P 3021
MY 8992
MB 1250
HB 12013
fiber tracts 2257
VS 17
VNC 1276
AMB 5
IC 352
NLL 197
arb 1222
CTX 389
grey 17809
region
arbor vitae                                                     1222
Midbrain                                                         277
Inferior colliculus, external nucleus                            276
[... 58 more lines not kept]
```

**Agent**

Unit counts: 20,109 pass the code's filter (paper: 20,300), but the regional counts fall short. Adding a duplicate check of behaviour between the two probes to the survey, then writing the analysis.

**Agent calls Bash**

```bash
cd entries/001619-kaku-2025 && python - <<'EOF'
s=open('kaku.py').read()
s=s.replace('''            "n_breath": f[BEH + "/data"].shape[0],''','''            "n_breath": f[BEH + "/data"].shape[0],
            "breath_head_hash": hash(f[BEH + "/data"][:200_000].tobytes()),
            "jaw_head_hash": hash(f["processing/DLC_tracking/side-facing_camera/jaw"][:20_000].tobytes()),''')
open('kaku.py','w').write(s)
EOF
grep -n "head_hash" kaku.py
```

```
215:            "breath_head_hash": hash(f[BEH + "/data"][:200_000].tobytes()),
216:            "jaw_head_hash": hash(f["processing/DLC_tracking/side-facing_camera/jaw"][:20_000].tobytes()),
```

**Agent calls Bash**

```bash
sed -i 's|"breath_head_hash": hash(f\[BEH + "/data"\]\[:200_000\].tobytes()),|"breath_head_hash": hashlib.md5(f[BEH + "/data"][:200_000].tobytes()).hexdigest(),|; s|"jaw_head_hash": hash(f\["processing/DLC_tracking/side-facing_camera/jaw"\]\[:20_000\].tobytes()),|"jaw_head_hash": hashlib.md5(f["processing/DLC_tracking/side-facing_camera/jaw"][:20_000].tobytes()).hexdigest(),|; s|^import re$|import hashlib\nimport re|' kaku.py && grep -n "hashlib" kaku.py
```

```
60:import hashlib
216:            "breath_head_hash": hashlib.md5(f[BEH + "/data"][:200_000].tobytes()).hexdigest(),
217:            "jaw_head_hash": hashlib.md5(f["processing/DLC_tracking/side-facing_camera/jaw"][:20_000].tobytes()).hexdigest(),
```

**Agent**

Writing the analysis now. First a small helper change so the lick-mode claim can use the latency from each cycle's last lick to the next inspiration.

**Agent calls Bash**

```bash
date -u; python - <<'EOF'
p='entries/001619-kaku-2025/kaku.py'
s=open(p).read()
s=s.replace('''    keep = np.setdiff1d(np.arange(len(ibi)), np.r_[rem1, rem2])
    t0, licks, lbef, nl, ibi = t0[keep], [licks[i] for i in keep], lbef[keep], nl[keep], ibi[keep]
    order = np.argsort(ibi)[::-1]
    t0, licks, lbef, nl, ibi = t0[order], [licks[i] for i in order], lbef[order], nl[order], ibi[order]
    out = {"t0": t0, "licks": licks, "lick_bef": lbef, "n_licks": nl, "ibi": ibi, "max_ibi": max_ibi}''','''    keep = np.setdiff1d(np.arange(len(ibi)), np.r_[rem1, rem2])
    t0, licks, lbef, nl, ibi, lick2 = t0[keep], [licks[i] for i in keep], lbef[keep], nl[keep], ibi[keep], lick2[keep]
    order = np.argsort(ibi)[::-1]
    t0, licks, lbef, nl, ibi, lick2 = t0[order], [licks[i] for i in order], lbef[order], nl[order], ibi[order], lick2[order]
    out = {"t0": t0, "licks": licks, "lick_bef": lbef, "n_licks": nl, "ibi": ibi, "max_ibi": max_ibi,
           "last_lick_to_next_insp": ibi - lick2}''')
open(p,'w').write(s)
EOF
```

```
Thu Nov  5 09:18:27 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/cells.py",
 "content": "\n# Each cell: (kind, tags, source). Built into the notebook by build_nb.py.\nCELLS = []\n\n\ndef md(s):\n    CELLS.append((\"markdown\", [], s.strip(\"\\n\")))\n\n\ndef code(s, tags=()):\n    CELLS.append((\"code\", list(tags), s.strip(\"\\n\")))\n\n\nmd(r'''\n# Reproducing Kaku, Liu et al. (2025) from dandiset 001619\n\n**Paper.** Kaku H, Liu LD, Gao R, West S, Liao S-M, Finkelstein A, Kleinfeld D, Thomas A, Tipparaju SL,\nSvoboda K, Li N (2025). A brainstem map of orofacial rhythms. bioRxiv,\n[doi:10.1101/2025.01.27.635041](https://doi.org/10.1101/2025.01.27.635041). The claims file was written\nfrom the preprint, version 1 (January 27, 2025), its Methods and the Extended Data legends, and from the\npaper's analysis code (github.com/NuoLiLabBCM/KakuEtAl2025 at commit fbc0abe).\n\n**Dandiset.** [DANDI:001619](https://dandiarchive.org/dandiset/001619/0.251027.1953), version\n0.251027.1953. The paper cites no version (its data statement says the data will be deposited upon\npublication; the dandiset was created later). This is the only published version, and it is the\nmost recent; the draft has the same 335 assets and size. It holds the brainstem Neuropixels recordings\nof the multi-directional licking task: one NWB file per probe insertion, with units, quality metrics,\nCCF positions, DeepLabCut tracking and the airflow (breathing) trace, per trial.\n\n**What is not in it.** The cued licking task with ALM, latSC and brainstem photostimulation, the rat\nrecordings, the raw videos, and the premotor tracing data are not in the dandiset.\n\n**Outside input.** Region names in the files are Allen CCF names; their acronyms and parent regions\ncome from the Allen structure tree, read from the iblatlas repository at a pinned commit\n(`kaku.ONTOLOGY_URL`). It maps names only.\n\n| Claim | Tested here |\n|---|---|\n| code-dataset-link, units-count, region-spike-rates | yes |\n| fig1d, fig1f (two), fig1g, fig1i, ed1, ed1bc, fig1k, fig1l (two), fig1n (two) | yes |\n| fig2 tuned counts, swallow counts, fig2f, fig2g, fig2h, ed6e, ed8bc, ed8e, ed4c | yes |\n| fig4e, fig4f, fig4d | yes |\n| ed8i (lick direction) | blocked, metadata_insufficient |\n| ed7 (GLM) | blocked, too_large |\n| ed7g, ed7h (CAE) | blocked, data_missing (raw videos) |\n| fig4g, fig4g lags, fig4h, ed12c (cross-correlation) | blocked (see the record) |\n| ed2 (rats), fig3a, fig3b, fig3ce, fig3dfh, ed10, fig4b, fig4c, ed11b, fig5b, fig5c, fig5e, fig5f | blocked, data_missing |\n\nThe notebook streams every file once (about 30 minutes, most of it reading the 25 kHz airflow and\nfitting tuning curves) and computes each claim from what it reads.\n''')\n\ncode(r'''\nimport time\nimport warnings\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\n\nimport kaku\n\nwarnings.filterwarnings(\"ignore\")\npd.set_option(\"display.width\", 220)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 200)\nt_start = time.time()\n\nassets = kaku.list_assets()\nfiles, units = kaku.survey(assets)\nonto = kaku.ontology()\nregions = kaku.region_table(units.region.dropna().unique(), onto)\nprint(f\"{len(assets)} files, {assets['size'].sum() / 1e9:.1f} GB, read in {time.time() - t_start:.0f} s (metadata)\")\n''')\n\ncode(r'''\njobs = []\nfor i, ((sub, ses), g) in enumerate(assets.groupby([\"subject\", \"session\"], sort=True)):\n    jobs.append(((sub, ses), g.url.iloc[0], dict(zip(g.probe, g.url)), 1000 + i))\nt0 = time.time()\nres = kaku.run_sessions(jobs, workers=5)\nprint(f\"{len(res)} sessions processed in {(time.time() - t0) / 60:.1f} min\")\n''')\n\ncode(r'''\n# Unit table: every unit of the survey, with the per-session results joined to the code's good units.\nunits[\"pos\"] = units.groupby([\"subject\", \"session\", \"probe\"]).cumcount()\nunits = units.merge(regions.rename(columns={\"name\": \"region\"}), on=\"region\", how=\"left\")\nunits[\"ancestors\"] = units[\"ancestors\"].apply(lambda a: a if isinstance(a, tuple) else ())\nunits[\"good\"] = kaku.good_units(units)\nunits[\"good_drift\"] = kaku.good_units(units, drift=True)\nrows = []\nfor r in res:\n    sub, ses = r[\"key\"]\n    for probe, us in r[\"units\"].items():\n        for u in us:\n            rows.append({\"subject\": sub, \"session\": ses, \"probe\": probe, \"pos\": u[\"unit_index\"],\n                         **{k: v for k, v in u.items() if not k.endswith((\"_cnt_4\", \"_cnt_2\", \"_cnt_5\", \"_occ_4\", \"_occ_2\", \"_occ_5\", \"_cen_4\", \"_cen_2\", \"_cen_5\")) and k != \"lick_counts\"}})\nT = pd.DataFrame(rows).merge(units, on=[\"subject\", \"session\", \"probe\", \"pos\"], how=\"left\")\nT[\"hemi\"] = np.where(T.ccf_x < 5700, \"left\", \"right\")\ndef under(d):\n    return T.ancestors.apply(lambda a: d in a).to_numpy()\nfor d in (\"CB\", \"P\", \"MY\", \"VNC\", \"IRN\", \"PARN\", \"XII\", \"V\", \"AMB\", \"NTS\", \"IC\", \"NLL\"):\n    T[\"in_\" + d] = under(d)\nprint(\"Good units with session results:\", len(T), \"of\", int(units.good.sum()))\n''')\n\nmd(r'''\n## Data check\n''')\n\ncode(r'''\nfs_ = files.copy()\nprint(\"Subjects:\", fs_.subject.nunique(), \"; sessions:\", fs_.groupby([\"subject\", \"session\"]).ngroups, \"; files (insertions):\", len(fs_))\nprint(\"Sex per subject:\", fs_.groupby(\"subject\").sex.first().value_counts().to_dict())\nprint(\"Age field values (first 8):\", sorted(fs_.age.unique())[:8], \"...\")\nprint(\"Genotype field:\", fs_.genotype.unique().tolist())\nprint(\"Stimulus field:\", fs_.stimulus.unique().tolist(), \"; acquisition groups:\", sorted({a for x in fs_.acquisition for a in x}),\n      \"; stimulus/presentation:\", sorted({a for x in fs_.stimulus_presentation for a in x}))\nprint(\"Trial table columns:\", sorted({c for x in fs_.trial_columns for c in x}), \"; largest start_time over all files:\", fs_.trial_start_max.max())\nprint(\"Trial duration range (s):\", fs_.trial_duration_min.min(), \"to\", fs_.trial_duration_max.max())\nprint(\"Trials per file:\", fs_.n_trials.describe()[[\"min\", \"50%\", \"max\"]].to_dict())\nprint(\"Files per session:\", fs_.groupby([\"subject\", \"session\"]).size().value_counts().to_dict())\nprint(\"Probe insertions per subject:\")\nprint(fs_.groupby(\"subject\").size().to_string())\nprint(\"Tracking info (video Hz, frames per trial, seconds) values:\", fs_.tracking_info.unique().tolist())\nprint(\"Probe types:\", fs_.ins_probe_type.unique().tolist(), \"; insertion targets:\", fs_.ins_recordable_brain_regions.value_counts().to_dict())\n''', tags=[\"sanity\"])\n\ncode(r'''\n# Formats: spike index, table lengths, DLC rows, airflow samples\nprint(\"spike_times_index read as start offsets matches the per-trial spike counts in\", int(fs_.index_is_start.sum()), \"of\", len(fs_), \"files;\",\n      \"read as end offsets (the NWB convention) in\", int(fs_.index_is_end.sum()))\nL = fs_[[c for c in fs_.columns if c.startswith(\"len_\")]]\nodd = fs_[L.nunique(axis=1) > 1]\nprint(\"Files whose units tables differ in length:\", len(odd))\nprint(odd[[\"subject\", \"session\", \"probe\", \"len_metrics\", \"len_units_id\", \"len_unit_info\", \"len_pairs\", \"len_histology\"]].to_string(index=False))\nprint(\"DLC rows = trials x 1471 in\", int((fs_.n_dlc_rows_side == fs_.n_trials * 1471).sum()), \"files (side),\",\n      int((fs_.n_dlc_rows_bottom == fs_.n_trials * 1471).sum()), \"(bottom); 3D rows = (trials - 1) x 1471 in\",\n      int((fs_.n_3d_rows == (fs_.n_trials - 1) * 1471).sum()), \"files\")\nprint(\"Airflow samples equal the sum of data_idx in\", int((fs_.n_breath == fs_.breath_idx_sum).sum()), \"files\")\ntwo = fs_.groupby([\"subject\", \"session\"]).filter(lambda g: len(g) == 2)\nsame = two.groupby([\"subject\", \"session\"]).agg(b=(\"breath_head_hash\", \"nunique\"), j=(\"jaw_head_hash\", \"nunique\"), n=(\"n_breath\", \"nunique\"))\nprint(\"Two-probe sessions:\", len(same), \"; with identical airflow (first 200,000 samples), identical side jaw tracking (first 20,000 rows) and equal airflow length:\",\n      int(((same.b == 1) & (same.j == 1) & (same.n == 1)).sum()))\nrs = pd.DataFrame([{\"subject\": r[\"key\"][0], \"session\": r[\"key\"][1], \"trials\": r[\"n_trials_total\"], \"good_trials\": r[\"n_good_trials\"],\n                    \"video_fs\": r[\"video_fs\"], \"trial_len\": r[\"trial_len\"], \"breath_dt\": r[\"breath_dt\"], \"breath_trials\": r[\"n_breath_trials\"],\n                    \"licks\": len(r[\"mt\"][\"tongue_onset\"]), \"inspirations\": len(r[\"mt\"][\"inspir_onset\"]), \"bouts\": len(r[\"mt\"][\"bout_on\"]),\n                    \"swallows\": len(r[\"swallow_times\"])} for r in res])\nprint(\"\\nPer session (173):\")\nprint(rs.describe().round(4).to_string())\nprint(\"Airflow sampling interval (s):\", rs.breath_dt.unique().tolist(), \"(Methods: 25 kHz)\")\n''', tags=[\"sanity\"])\n\nmd(r'''\nEvery file stores each unit's spikes in `units/spike_times` with `spike_times_index` holding the\noffset where the unit starts. In NWB the index holds where each unit ends, so a standard reader (pynwb)\ngives each unit the spikes of the unit before it. The per-unit, per-trial spike counts (`unit and\ntrial pairs`) agree with the start-offset reading in every file, and spikes are read that way here.\nIn the files listed above the histology table (region and CCF position) has more rows than the units,\nso its rows cannot be matched to units with certainty; like the paper's code, the rows are taken by\nposition. Spike times are relative to the trial start; every trial starts at time 0 in the trial\ntable, so the trials cannot be placed on a session clock. The behaviour of the two probes of a session\nis the same recording deposited twice: it is read once per session. The age field (for example\n`P273W`, 273 weeks) is not plausible for these mice. The stimulus field says `photostim`, but the\nfiles hold no photostimulation or cue times.\n''')\n\ncode(r'''\ngu = units[units.good]\nprint(\"Unit metrics of the code's good units (ranges):\")\nprint(gu[[\"unit_amp\", \"avg_firing_rate\", \"isi_violation\", \"presence_ratio\", \"amplitude_cutoff\", \"drift_metric\"]].describe().round(3).to_string())\nprint(\"\\nCCF coordinates of good units (um): x\", gu.ccf_x.min(), \"to\", gu.ccf_x.max(), \"; y\", gu.ccf_y.min(), \"to\", gu.ccf_y.max(), \"; z\", gu.ccf_z.min(), \"to\", gu.ccf_z.max())\nprint(\"Region names not found in the Allen structure tree:\", regions[regions.acronym.isna()].name.tolist())\nlab = units.dropna(subset=[\"ccf_x\"])\nprint(\"Units whose 'left'/'right' unit_location agrees with ccf_x on the side of 5700 um:\",\n      round(float(np.mean((lab.info_unit_location.str.startswith(\"left\")) == (lab.ccf_x < 5700))), 3))\n# axes: which CCF coordinate runs anterior-posterior? cerebellum units should be dorsal (small y) and medulla ventral\nprint(\"Median ccf_y (DV) of CB units:\", T[T.in_CB].ccf_y.median(), \"; of MY units:\", T[T.in_MY].ccf_y.median())\nprint(\"Median ccf_z (AP) of P units:\", T[T.in_P].ccf_z.median(), \"; of MY units:\", T[T.in_MY].ccf_z.median())\n''', tags=[\"sanity\"])\n\nmd(r'''\n`ccf_x` is medial-lateral (the midline of the CCF is at 5700 um, and the side agrees with the\n`unit_location` text for almost every unit), `ccf_y` dorsal-ventral (cerebellum above medulla) and\n`ccf_z` anterior-posterior (pons anterior of medulla), in um. This is consistent with the Allen CCF and\nwith the paper's code, which plots them that way; the files do not name the axes.\n''')\n\ncode(r'''\n# Clock check. Spikes, tracking and airflow are stored per trial on separate arrays. If they share the\n# trial clock, phase tuning to jaw and breathing should fall when each trial's spikes are paired with the\n# next trial's phases.\nfor mod, col in ((\"jaw\", \"jaw_mi_grid_4\"), (\"breathing\", \"br_mi_grid_4\")):\n    shift = \"jaw_mi_shift\" if mod == \"jaw\" else \"br_mi_shift\"\n    top = T[T[col] > 0.6]\n    print(f\"{mod}: units with grid MI > 0.6, true pairing {len(top)}; their median MI {top[col].median():.3f} true, \"\n          f\"{top[shift].median():.3f} with the next trial's phases; units above 0.6 after the shift: {(T[shift] > 0.6).sum()}\")\nby = T.groupby(\"subject\").apply(lambda g: pd.Series({\"n_true\": (g.jaw_mi_grid_4 > 0.6).sum(), \"n_shift\": (g.jaw_mi_shift > 0.6).sum(),\n                                                     \"br_true\": (g.br_mi_grid_4 > 0.6).sum(), \"br_shift\": (g.br_mi_shift > 0.6).sum()}))\nprint(\"\\nPer subject, units with MI > 0.6, true and shifted pairing:\")\nprint(by.T.to_string())\n# Behaviour: inspirations and tongue onsets lie on the same per-trial clock; the lick-breath relation is tested in fig1f.\n''', tags=[\"sanity\"])\n\nmd(r'''\nPhase tuning to the jaw and to breathing is present with the true pairing and falls sharply when spikes\nare paired with the next trial's tracking or airflow, in every subject with tuned units (table above).\nSpikes, tracking and airflow therefore share the trial clock. This shows alignment within trials; the\ntrials themselves cannot be placed on one session clock, since every trial starts at 0.\n''')\n\n# ------------------------------------------------------------------------------------- link and units\nmd(r'''\n## code-dataset-link\n\n> The dandiset is the data the paper's analysis code reads, so that the code's choices fixed in this\n> file apply to it.\n''')\n\ncode(r'''\nneed = {\"spike times per trial\": \"units/spike_times with unit and trial pairs\",\n        \"unit quality metrics\": \"analysis/unit_metrics (presence_ratio, amplitude_cutoff, avg_firing_rate, isi_violation, unit_amp, drift_metric)\",\n        \"CCF coordinates\": \"units/histology (ccf_x, ccf_y, ccf_z, unit_region)\",\n        \"airflow at 25 kHz with timestamps\": \"breathing data, timestamps and data_idx\",\n        \"side and bottom DLC jaw and tongue with likelihoods\": \"DLC_tracking side- and bottom-facing camera jaw, tongue, lickport\",\n        \"3D jaw and tongue tracks\": \"3D_tracking jaw_side, tongue_bottom, lickport_bottom\"}\nfor k, v in need.items():\n    print(f\"{k:55s} <- {v}\")\nn_code = int(units.good.sum()); n_drift = int(units.good_drift.sum())\nprint(f\"\\nUnits passing get_good_units over all files: {n_code} ({n_code / 20300 - 1:+.1%} from 20,300); with the drift metric: {n_drift} ({n_drift / 20300 - 1:+.1%})\")\nprint(\"Sessions processed through the code's steps without error:\", len(res), \"of\", len(jobs))\n''', tags=[\"claim:code-dataset-link\"])\n\nmd(r'''\n**Result: reproduced.** Every input of process_mat.py can be built from the NWB files (listed above), and\nthe code's unit filter keeps 20,109 units, 0.9% below 20,300. With the Methods' drift metric added it\nkeeps 16,957 (16.5% below). The spike index needs the reading described in the data check.\n''')\n\nmd(r'''\n## units-count\n\n> Across 339 insertions in 31 mice, 20,300 single units passed quality control (60 +- 22 per probe),\n> 5,700 in the cerebellum, 3,700 in the pons and 10,900 in the medulla.\n''')\n\ncode(r'''\ndef counts(mask):\n    g = units[mask]\n    per = g.groupby([\"subject\", \"session\", \"probe\"]).size().reindex(pd.MultiIndex.from_frame(files[[\"subject\", \"session\", \"probe\"]]), fill_value=0)\n    anc = g.ancestors\n    cb = anc.apply(lambda a: \"CB\" in a)\n    arb = g.acronym.isin([\"arb\", \"cbc\", \"cbp\", \"scp\", \"mcp\", \"icp\"])\n    return {\"units\": len(g), \"per probe mean\": per.mean(), \"per probe sd\": per.std(),\n            \"CB\": int(cb.sum()), \"CB + cerebellar white matter\": int((cb | arb).sum()),\n            \"P\": int(anc.apply(lambda a: \"P\" in a).sum()), \"MY\": int(anc.apply(lambda a: \"MY\" in a).sum()),\n            \"other\": int((~anc.apply(lambda a: any(d in a for d in (\"CB\", \"P\", \"MY\"))) & ~arb).sum())}\ntab = pd.DataFrame({\"code filter\": counts(units.good), \"with drift metric\": counts(units.good_drift)}).T\nprint(tab.round(1).to_string())\nprint(\"\\nPaper: 20,300 units (tolerance 2,030), 60 +- 22 per probe, CB 5,700 (570), P 3,700 (370), MY 10,900 (1,090); 339 insertions, 31 mice\")\nprint(\"Dandiset: insertions (files)\", len(files), \"; mice\", files.subject.nunique())\nprint(\"Units with amplitude > 150 uV (all other metrics ignored):\", int((units.unit_amp > 150).sum()), \"(Extended Data Fig 4c: 19,000)\")\nprint(\"\\nGood units outside CB, P and MY, by region (top 15):\")\ng = units[units.good]\nout = g[~g.ancestors.apply(lambda a: any(d in a for d in (\"CB\", \"P\", \"MY\")))]\nprint(out.region.value_counts().head(15).to_string())\nprint(\"\\nPer subject (code filter):\")\nprint(units[units.good].groupby(\"subject\").size().to_string())\n''', tags=[\"claim:units-count\"])\n\nmd(r'''\n**Result: partially reproduced.** The total (20,109 by the code's filter) and the mean per probe (61)\nare within tolerance, and there are 31 mice, but the dandiset holds 335 insertions, not 339, and the\ncounts by region are all below the paper's: 4,157 in the cerebellum (5,379 with the arbor vitae and\ncerebellar peduncles), 3,021 in the pons and 8,992 in the medulla. About 1,900 good units lie in fibre\ntracts, the midbrain and other regions. The spread per probe is 32 where the paper gives 22.\n''')\n\nmd(r'''\n## region-spike-rates\n\n> Neurons in the cerebellum (22 +- 29 spikes/s) and vestibular nucleus (38 +- 32) fired faster than\n> neurons in the medulla (11 +- 14).\n''')\n\ncode(r'''\nrows = []\nfor rate_name, col in ((\"(a) avg_firing_rate\", \"avg_firing_rate\"), (\"(b) spikes in the first 5 s of good trials\", \"rate_5s\")):\n    for med_name, med in ((\"(i) MY with VNC\", T.in_MY), (\"(ii) MY without VNC\", T.in_MY & ~T.in_VNC)):\n        r = {\"rate\": rate_name, \"medulla\": med_name}\n        for name, m in ((\"CB\", T.in_CB), (\"VNC\", T.in_VNC), (\"MY\", med)):\n            v = T.loc[m, col]\n            r[name + \" mean\"], r[name + \" sd\"], r[name + \" n\"] = v.mean(), v.std(), int(m.sum())\n        rows.append(r)\nrr = pd.DataFrame(rows)\nprint(rr.round(2).to_string(index=False))\nprint(\"\\nPaper: CB 22 (+-2.2), VNC 38 (+-3.8), MY 11 (+-1.1) spikes/s\")\nrr[\"all within\"] = (abs(rr[\"CB mean\"] - 22) <= 2.2) & (abs(rr[\"VNC mean\"] - 38) <= 3.8) & (abs(rr[\"MY mean\"] - 11) <= 1.1)\nprint(rr[[\"rate\", \"medulla\", \"all within\"]].to_string(index=False))\nprint(\"\\nCB mean rate with cerebellar white matter included, reading (a):\", round(T.loc[T.in_CB | T.acronym.isin([\"arb\"]), \"avg_firing_rate\"].mean(), 2))\n''', tags=[\"claim:region-spike-rates\"])\n\nmd(r'''\n**Result: see the table.** The conclusion is in the summary and the record; the means of each reading\nare printed above against the paper's values.\n''')\n"
}
```

```
File created successfully at: /tmp/claude-1001/cells.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cat > $TMPDIR/dev.py <<'EOF'
import sys, pickle, io, contextlib, traceback
sys.path.insert(0,'entries/001619-kaku-2025'); sys.path.insert(0,'/tmp/claude-1001')
import importlib, cells; importlib.reload(cells)
start = int(sys.argv[1]) if len(sys.argv)>1 else 0
ns = {}
codes = [c for c in cells.CELLS if c[0]=='code']
for i,(k,tags,src) in enumerate(codes):
    if i==0:
        src = src.replace("files, units = kaku.survey(assets)", "files, units = pickle.load(open('/tmp/claude-1001/survey.pkl','rb'))")
        src = "import pickle\n" + src
    if i==1:
        src = "jobs=[]\nres = pickle.load(open('/tmp/claude-1001/res_173.pkl','rb'))"
    if 'hash' in src and 'breath_head_hash' not in ns.get('files', {}).__class__.__name__:
        src = src.replace('two = fs_.groupby', 'fs_["breath_head_hash"]=0; fs_["jaw_head_hash"]=0\ntwo = fs_.groupby')
    if i < start and i>3: continue
    print(f"===== cell {i} {tags}")
    try:
        exec(src, ns)
    except Exception:
        traceback.print_exc()
        break
if len(sys.argv)>2: pickle.dump({k:v for k,v in ns.items() if k in ('T','units','files','res','regions','rs')}, open('/tmp/claude-1001/ns.pkl','wb'))
EOF
cd $TMPDIR && . env/bin/activate && python dev.py 0 2>&1 | tail -150
```

```
===== cell 4 ['sanity']
spike_times_index read as start offsets matches the per-trial spike counts in 335 of 335 files; read as end offsets (the NWB convention) in 0
Files whose units tables differ in length: 19
subject                     session probe  len_metrics  len_units_id  len_unit_info  len_pairs  len_histology
  DL007 20210412-20210412-202840-s4    p2         1122          1122           1122       1122           1129
  DL009 20210419-20210419-134252-s7    p1          519           519            519        519            529
  DL016 20210525-20210525-142851-s7    p1          967           967            967        967            974
  DL017 20210710-20210710-185624-s4    p2          838           838            838        838            849
  DL024 20210615-20210615-142740-s1    p1          841           841            841        841            842
  DL024 20210617-20210617-180836-s3    p2          753           753            753        753            754
  DL024 20210618-20210618-152516-s4    p1          346           346            346        346            348
  DL024 20210618-20210618-152516-s4    p2          633           633            633        633            634
  DL028 20211221-20211221-151820-s5    p2          827           827            827        827            828
  DL028 20211224-20211224-153012-s8    p1          529           529            529        529            530
  DL030 20220110-20220110-141133-s6    p1          417           417            417        417            421
  DL030 20220111-20220111-131653-s7    p1          879           879            879        879            887
  DL030 20220113-20220113-115659-s9    p1          553           553            553        553            558
  DL030 20220113-20220113-115659-s9    p2         1326          1326           1326       1326           1332
  DL034 20220205-20220205-205500-s2    p1         1115          1115           1115       1115           1125
  DL034 20220205-20220205-20
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('cells.py').read()
s=s.replace('''    arb = g.acronym.isin(["arb", "cbc", "cbp", "scp", "mcp", "icp"])''','''    arb = g.acronym.isin(["arb", "cbc"])''')
s=s.replace('"CB + cerebellar white matter"','"CB + arbor vitae"')
s=s.replace('''print("\\nCB mean rate with cerebellar white matter included, reading (a):", round(T.loc[T.in_CB | T.acronym.isin(["arb"]), "avg_firing_rate"].mean(), 2))''','''print("\\nCB mean rate with the arbor vitae included, reading (a):", round(T.loc[T.in_CB | T.acronym.isin(["arb", "cbc"]), "avg_firing_rate"].mean(), 2))''')
s=s.replace('''`ccf_x` is medial-lateral (the midline of the CCF is at 5700 um, and the side agrees with the
`unit_location` text for almost every unit), `ccf_y` dorsal-ventral (cerebellum above medulla) and
`ccf_z` anterior-posterior (pons anterior of medulla), in um. This is consistent with the Allen CCF and
with the paper's code, which plots them that way; the files do not name the axes.''','''`ccf_x` is medial-lateral, `ccf_y` dorsal-ventral (cerebellum above medulla) and `ccf_z`
anterior-posterior (pons anterior of medulla), in um, as the paper's code plots them; the files do not
name the axes. The midline of the CCF is at 5700 um, but the `unit_location` text ("left Medulla",
"right Medulla") puts almost every unit on the side opposite to the one that reading of `ccf_x` gives
if it increases to the right. Which side is left is therefore not settled by the files; no claim tested
here depends on it.''')
open('cells.py','w').write(s)
EOF
cat >> $TMPDIR/cells.py <<'EOF'

# ------------------------------------------------------------------------------------- behaviour
md(r'''
## Behaviour: licking, breathing and swallowing (Figure 1, Extended Data Figure 1)

Tongue onsets, lick bouts, inspiration onsets and swallows follow the paper's code (helper docstring).
Times are on the code's timeline: the first 1471 frames of each good trial placed end to end. The two
probes of a session share one behaviour recording, so behaviour is counted once per session.
''')

code(r'''
sess = pd.DataFrame([{"subject": r["key"][0], "session": r["key"][1]} for r in res])
def trial_of(t):
    return np.floor(t / kaku.TRIAL_S).astype(int)
def within_trial_freq(times, mask=None):
    t = np.asarray(times)
    d = np.diff(t)
    same = trial_of(t[:-1]) == trial_of(t[1:])
    if mask is not None:
        same &= mask[:-1] & mask[1:]
    return 1 / d[same & (d > 0)]
def in_bouts(t, mt):
    on, off = mt["bout_on"], mt["bout_off"]
    i = np.searchsorted(on, t, side="right") - 1
    ok = i >= 0
    ok[ok] = t[ok] <= off[i[ok]]
    return ok
lf_a, bf_a, lf_b, bf_b = [], [], [], []
for r in res:
    mt = r["mt"]
    ton, ins = mt["tongue_onset_all"], mt["inspir_onset"]
    lf_a.append(within_trial_freq(ton)); bf_a.append(within_trial_freq(ins))
    lf_b.append(within_trial_freq(ton, in_bouts(ton, mt))); bf_b.append(within_trial_freq(ins, in_bouts(ins, mt)))
rows = []
for name, lf, bf in (("(a) within trials", lf_a, bf_a), ("(b) within lick bouts", lf_b, bf_b)):
    L, B = np.hstack(lf), np.hstack(bf)
    rows.append({"reading": name, "lick mean": L.mean(), "lick sd": L.std(), "lick 2.5%": np.percentile(L, 2.5), "lick 97.5%": np.percentile(L, 97.5),
                 "breath mean": B.mean(), "breath sd": B.std(), "breath 2.5%": np.percentile(B, 2.5), "breath 97.5%": np.percentile(B, 97.5),
                 "n licks": len(L), "n breaths": len(B)})
fq = pd.DataFrame(rows)
print(fq.round(2).to_string(index=False))
exp = {"lick mean": (6.23, .62), "breath mean": (4.02, .4), "lick 2.5%": (3.59, .36), "lick 97.5%": (8.91, .89), "breath 2.5%": (2.12, .21), "breath 97.5%": (7.17, .72)}
for _, r in fq.iterrows():
    print(r.reading, {k: bool(abs(r[k] - v) <= t) for k, (v, t) in exp.items()})
print("\nPer session median frequencies, reading (b): licking", np.round(np.percentile([np.median(x) for x in lf_b if len(x)], [5, 50, 95]), 2),
      "breathing", np.round(np.percentile([np.median(x) for x in bf_b if len(x)], [5, 50, 95]), 2), "(5th, 50th, 95th percentiles over sessions)")
''', tags=["claim:fig1d-lick-breath-frequencies"])

md(r'''
**Result: FIG1D**
''')

code(r'''
rows = []
lat_by_n = []
for r, (_, s) in zip(res, sess.iterrows()):
    mt = r["mt"]
    ton = mt["tongue_onset_all"]
    # protrusion intervals: each tongue onset to the first offset after it (code onsets and offsets)
    off = np.sort(mt["tongue_offset"])
    j = np.searchsorted(off, ton, side="right")
    ok = j < len(off)
    on_i, off_i = ton[ok], off[j[ok]]
    ins = mt["inspir_onset"]
    ins_b = ins[in_bouts(ins, mt)]
    k = np.searchsorted(on_i, ins_b, side="right") - 1
    inside = (k >= 0) & (ins_b <= off_i[np.clip(k, 0, None)]) & (ins_b >= on_i[np.clip(k, 0, None)])
    rows.append({"subject": s.subject, "session": s.session, "inspirations in bouts": len(ins_b), "within protrusion": int(inside.sum())})
pr = pd.DataFrame(rows)
pr["fraction"] = pr["within protrusion"] / pr["inspirations in bouts"]
print("Per session fraction of in-bout inspiration onsets that fall inside a tongue protrusion:")
print(pr.fraction.describe().round(4).to_string())
pooled = pr["within protrusion"].sum() / pr["inspirations in bouts"].sum()
print(f"\nPooled: {pr['within protrusion'].sum()} of {pr['inspirations in bouts'].sum()} = {pooled:.4f}; reading (b) holds (< 5%): {pooled < 0.05}")
print("Reading (a), no such inspiration in any session:", bool((pr['within protrusion'] == 0).all()), "; sessions with none:", int((pr['within protrusion'] == 0).sum()), "of", len(pr))
print("By subject (pooled fraction):")
print((pr.groupby("subject")["within protrusion"].sum() / pr.groupby("subject")["inspirations in bouts"].sum()).round(4).to_string())
# latency from the last lick to the next inspiration, per number of licks in the cycle (code cycles)
lat = []
for r in res:
    p = r["pd_lick"]
    if p is None:
        continue
    lat.append(pd.DataFrame({"n_licks": p["n_licks"], "lat": p.get("last_lick_to_next_insp", np.full(len(p["n_licks"]), np.nan)), "ibi": p["ibi"]}))
lat = pd.concat(lat)
print("\nLatency from the last lick in a breath cycle to the next inspiration (s), pooled:")
print(lat.groupby("n_licks").lat.describe()[["count", "25%", "50%", "75%"]].round(3).head(6).to_string())
''', tags=["claim:fig1f-inspiration-between-licks"])

md(r'''
**Result: FIG1F**
''')

code(r'''
pdl = pd.DataFrame([{"subject": s.subject, "session": s.session, "diff": (r["pd_lick"] or {}).get("diff", np.nan),
                     "n_fast": len((r["pd_lick"] or {}).get("i_fast", [])), "n_slow": len((r["pd_lick"] or {}).get("i_slow", []))}
                    for r, (_, s) in zip(res, sess.iterrows())])
v = pdl.dropna(subset=["diff"])
print(f"Sessions with at least 40 two-lick cycles in each half and a peak in each window: {len(v)} of {len(pdl)} "
      f"({(pdl.n_fast >= 40).sum()} with enough cycles)")
print("Session peak differences, slow minus fast (s):", v["diff"].describe().round(4).to_dict())
t_a = stats.ttest_1samp(v["diff"], 0)
m = v.groupby("subject")["diff"].mean()
t_b = stats.ttest_1samp(m, 0)
print(f"(a) sessions: mean {v['diff'].mean() * 1000:.1f} ms, t = {t_a.statistic:.2f}, p = {t_a.pvalue:.2e}, n = {len(v)}")
print(f"(b) mice: mean {m.mean() * 1000:.1f} ms, t = {t_b.statistic:.2f}, p = {t_b.pvalue:.2e}, n = {len(m)}")
print("Mice with a positive mean:", int((m > 0).sum()), "of", len(m), "; zero:", int((m == 0).sum()), "; negative:", int((m < 0).sum()))
print("Per mouse mean (ms) and sessions:")
print(pd.DataFrame({"mean_ms": (m * 1000).round(1), "sessions": v.groupby("subject").size()}).T.to_string())
print("Sessions with difference > 0:", int((v['diff'] > 0).sum()), "; = 0:", int((v['diff'] == 0).sum()), "; < 0:", int((v['diff'] < 0).sum()))
''', tags=["claim:fig1g-lick-delayed-before-slow-breath"])

md(r'''
**Result: FIG1G**
''')

code(r'''
rows = []
for r, (_, s) in zip(res, sess.iterrows()):
    p = r["pd_lick"]
    if p is None:
        continue
    d = pd.DataFrame({"n": p["n_licks"], "ibi": p["ibi"], "lat": p.get("last_lick_to_next_insp", np.full(len(p["ibi"]), np.nan))})
    g = d.groupby("n").agg(med_ibi=("ibi", "median"), med_lat=("lat", "median"), count=("ibi", "size"))
    row = {"subject": s.subject, "session": s.session}
    for n in (1, 2, 3, 4):
        row[f"ibi{n}"] = g.med_ibi.get(n, np.nan); row[f"lat{n}"] = g.med_lat.get(n, np.nan); row[f"n{n}"] = int(g["count"].get(n, 0))
    rows.append(row)
ms = pd.DataFrame(rows)
ok3 = (ms.n1 > 0) & (ms.n2 > 0) & (ms.n3 > 0)
rise = (ms.ibi1 < ms.ibi2) & (ms.ibi2 < ms.ibi3)
rise4 = rise & ((ms.n4 < 20) | (ms.ibi3 < ms.ibi4))
print(f"Sessions with cycles of 1, 2 and 3 licks: {ok3.sum()} of {len(ms)}")
print(f"Median inter-breath interval rises from 1 to 2 to 3 licks (and to 4 where >= 20 cycles): {int((rise4 & ok3).sum())} of {int(ok3.sum())} sessions; "
      f"without the 4-lick condition {int((rise & ok3).sum())}")
print("Median over sessions of the session medians (s):", ms.loc[ok3, ["ibi1", "ibi2", "ibi3", "ibi4"]].median().round(3).to_dict())
lat_med = lat.groupby("n_licks").lat.median()
print("Pooled median latency last lick -> next inspiration (s) by licks in cycle:", lat_med.head(4).round(4).to_dict())
l4 = lat_med.loc[[1, 2, 3]]
print(f"Largest relative difference between groups 1 to 3: {(l4.max() - l4.min()) / l4.min():.1%}; with group 4: {(lat_med.loc[[1, 2, 3, 4]].max() - lat_med.loc[[1, 2, 3, 4]].min()) / lat_med.loc[[1, 2, 3, 4]].min():.1%}")
sl = ms.loc[ok3, ["lat1", "lat2", "lat3"]]
rel = (sl.max(1) - sl.min(1)) / sl.min(1)
print(f"Per session, groups 1 to 3 within 20% of each other: {int((rel < 0.2).sum())} of {len(sl)}")
print("Cycles per group, pooled:", lat.groupby('n_licks').size().head(6).to_dict())
''', tags=["claim:fig1f-licking-mode-switch"])

md(r'''
**Result: FIG1FMODE**
''')

code(r'''
pdb = pd.DataFrame([{"subject": s.subject, "session": s.session, "diff": (r["pd_breath"] or {}).get("diff", np.nan),
                     "n_fast": len((r["pd_breath"] or {}).get("i_fast", []))} for r, (_, s) in zip(res, sess.iterrows())])
v2 = pdb.dropna(subset=["diff"])
print(f"Sessions with at least 100 cycles per half and a peak in each window: {len(v2)} of {len(pdb)}")
print("Session peak differences (s):", v2["diff"].describe().round(4).to_dict())
t_a2 = stats.ttest_1samp(v2["diff"], 0)
m2 = v2.groupby("subject")["diff"].mean()
t_b2 = stats.ttest_1samp(m2, 0)
print(f"(a) sessions: mean {v2['diff'].mean() * 1000:.1f} ms, t = {t_a2.statistic:.2f}, p = {t_a2.pvalue:.2e}, n = {len(v2)}")
print(f"(b) mice: mean {m2.mean() * 1000:.1f} ms, t = {t_b2.statistic:.2f}, p = {t_b2.pvalue:.2e}, n = {len(m2)}")
print("Mice with a positive mean:", int((m2 > 0).sum()), "of", len(m2))
print("Sessions > 0:", int((v2['diff'] > 0).sum()), "; = 0:", int((v2['diff'] == 0).sum()), "; < 0:", int((v2['diff'] < 0).sum()))
''', tags=["claim:fig1i-breath-delayed-before-slow-lick"])

md(r'''
**Result: FIG1I**
''')
EOF
cd $TMPDIR && . env/bin/activate && python dev.py 10 2>&1 | tail -120
```

```
DL007     8
DL008     2
DL009     7
DL010     8
DL011     8
DL012     8
DL014     6
DL015     7
DL016    10
DL017    15
DL018     9
DL019     6
DL020     8
DL021    10
DL022     8
DL023    15
DL024    18
DL025    18
DL026    18
DL027     6
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import pickle,numpy as np
res=pickle.load(open('res_173.pkl','rb'))
H=np.zeros(60); H2=np.zeros(60); D=[]
bins=np.arange(-0.3,0.3001,0.01)
for r in res[:60]:
    mt=r['mt']; ton=mt['tongue_onset_all']; ins=mt['inspir_onset']
    on=mt['bout_on']; off=mt['bout_off']
    i=np.searchsorted(on,ins,side='right')-1; ok=(i>=0); ok[ok]=ins[ok]<=off[i[ok]]
    ib=ins[ok]
    # relative to nearest tongue onsets
    for t in ib:
        k=np.searchsorted(ton,t)
        rel=ton[max(k-3,0):k+3]-t
        H+=np.histogram(rel,bins)[0]
    off_=np.sort(mt['tongue_offset']); j=np.searchsorted(off_,ton,side='right'); okk=j<len(off_)
    D.append(off_[j[okk]]-ton[okk])
print('tongue onsets relative to in-bout inspirations (10 ms bins, -0.3..0.3):')
print(np.c_[bins[:-1].round(2),H.astype(int)].T)
D=np.hstack(D); print('protrusion durations pct', np.percentile(D,[5,25,50,75,95]).round(3))
EOF
```

```
tongue onsets relative to in-bout inspirations (10 ms bins, -0.3..0.3):
[[-3.0000e-01 -2.9000e-01 -2.8000e-01 -2.7000e-01 -2.6000e-01 -2.5000e-01
  -2.4000e-01 -2.3000e-01 -2.2000e-01 -2.1000e-01 -2.0000e-01 -1.9000e-01
  -1.8000e-01 -1.7000e-01 -1.6000e-01 -1.5000e-01 -1.4000e-01 -1.3000e-01
  -1.2000e-01 -1.1000e-01 -1.0000e-01 -9.0000e-02 -8.0000e-02 -7.0000e-02
  -6.0000e-02 -5.0000e-02 -4.0000e-02 -3.0000e-02 -2.0000e-02 -1.0000e-02
   0.0000e+00  1.0000e-02  2.0000e-02  3.0000e-02  4.0000e-02  5.0000e-02
   6.0000e-02  7.0000e-02  8.0000e-02  9.0000e-02  1.0000e-01  1.1000e-01
   1.2000e-01  1.3000e-01  1.4000e-01  1.5000e-01  1.6000e-01  1.7000e-01
   1.8000e-01  1.9000e-01  2.0000e-01  2.1000e-01  2.2000e-01  2.3000e-01
   2.4000e-01  2.5000e-01  2.6000e-01  2.7000e-01  2.8000e-01  2.9000e-01]
 [ 7.3580e+03  7.6190e+03  7.7180e+03  7.8310e+03  7.7350e+03  7.3830e+03
   6.7460e+03  5.8440e+03  5.2220e+03  4.8990e+03  4.8620e+03  5.7900e+03
   5.5060e+03  5.5750e+03  7.2050e+03  7.8030e+03  8.4370e+03  9.3240e+03
   1.0338e+04  1.1022e+04  1.0558e+04  9.1510e+03  7.4630e+03  5.7400e+03
   4.4600e+03  3.9760e+03  4.2570e+03  5.3420e+03  6.3860e+03  6.8640e+03
   4.4870e+03  6.9470e+03  7.6500e+03  8.5520e+03  9.1320e+03  9.4590e+03
   9.3010e+03  8.7140e+03  7.8830e+03  6.7210e+03  6.0990e+03  5.5540e+03
   5.7280e+03  6.1100e+03  6.3980e+03  6.7780e+03  5.7320e+03  6.1700e+03
   7.4940e+03  7.8970e+03  7.7270e+03  7.7700e+03  7.6930e+03  7.0850e+03
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/cells.py <<'EOF'

code(r'''
# Extended Data Fig 1d-i: unidirectional models, simulated as the Methods describe.
rng = np.random.default_rng(11)
ibi_emp = 1 / np.hstack(bf_a)          # inter-breath intervals within trials (fig1d reading (a))
ili_emp = 1 / np.hstack(lf_b)          # inter-lick intervals within lick bouts (fig1d reading (b))
ili_range = np.percentile(ili_emp, [2.5, 97.5])
ibi_range = np.percentile(ibi_emp, [2.5, 97.5])
lat_ll = lat.lat.median() if lat.lat.notna().any() else np.nan       # last lick -> next inspiration
# last inspiration -> next lick, from the breath-to-lick cycles of the data
lat_il = []
for r in res:
    mt = r["mt"]
    ton, ins = mt["tongue_onset"], mt["inspir_onset"]
    tb = ton[in_bouts(ton, mt)]
    k = np.searchsorted(ins, tb) - 1
    ok = k >= 0
    lat_il.append(tb[ok] - ins[k[ok]])
lat_il = np.median(np.hstack(lat_il))
print(f"Empirical ranges: inter-lick {ili_range.round(3)} s, inter-breath {ibi_range.round(3)} s; latencies: last lick -> inspiration {lat_ll:.3f} s, inspiration -> next lick {lat_il:.3f} s")

def sim_breath_driven(n_breaths):
    ins = np.cumsum(rng.choice(ibi_emp, n_breaths))
    licks = list(ins - lat_ll)
    licks = np.sort(np.array(licks))
    out = [licks[0]]
    for a, b in zip(licks[:-1], licks[1:]):
        gap = b - a
        k = int(np.ceil(gap / ili_range[1])) - 1 if gap > ili_range[1] else 0
        out += list(a + gap * np.arange(1, k + 1) / (k + 1)) + [b]
    licks = np.sort(np.array(out) + rng.normal(0, 0.01, len(out)))
    return licks, ins

def sim_lick_driven(n_licks):
    licks = np.cumsum(rng.choice(ili_emp, n_licks))
    cand = licks - lat_il
    ins = [cand[0]]
    for c in cand[1:]:
        if ibi_range[0] <= c - ins[-1]:
            ins.append(c)
    ins = np.array(ins)
    keep = np.r_[True, np.diff(ins) <= ibi_range[1]] | True
    ins = ins + rng.normal(0, 0.01, len(ins))
    return licks, np.sort(ins)

def measures(licks, ins):
    mt = {"tongue_onset": licks, "inspir_onset": ins, "bout_on": np.array([licks[0]]), "bout_off": np.array([licks[-1]])}
    a = kaku.peak_diff_lick_behv(mt)
    b = kaku.peak_diff_breath_behv(mt)
    return (a or {}).get("diff", np.nan), (b or {}).get("diff", np.nan)

sim = []
for r in res:
    mt = r["mt"]
    nb = int(in_bouts(mt["inspir_onset"], mt).sum()); nl = int(in_bouts(mt["tongue_onset"], mt).sum())
    if nb < 50:
        continue
    l, i = sim_breath_driven(nb)
    g_b, i_b = measures(l, i)
    l, i = sim_lick_driven(nl)
    g_l, i_l = measures(l, i)
    sim.append({"breath_model_fig1g": g_b, "breath_model_fig1i": i_b, "lick_model_fig1g": g_l, "lick_model_fig1i": i_l})
sim = pd.DataFrame(sim)
for col in sim.columns:
    v_ = sim[col].dropna()
    tt = stats.ttest_1samp(v_, 0) if len(v_) > 2 else None
    print(f"{col}: sessions with a value {len(v_)}, mean {v_.mean() * 1000 if len(v_) else np.nan:.1f} ms, "
          f"p = {tt.pvalue if tt else np.nan:.3g}")
print(f"Data: Fig 1g mean {v['diff'].mean() * 1000:.1f} ms (p = {t_a.pvalue:.2e}); Fig 1i mean {v2['diff'].mean() * 1000:.1f} ms (p = {t_a2.pvalue:.2e})")
''', tags=["claim:ed1-unidirectional-models-fail"])

md(r'''
**Result: ED1**
''')

code(r'''
# Extended Data Fig 1b-c: lick probability around swallows and around expirations inside bouts
bins = np.arange(-0.3, 0.3 + 1e-9, kaku.FRAME_S)
rows = []
for r, (_, s) in zip(res, sess.iterrows()):
    sw = r["swallow_times"]
    if len(sw) < 20:
        continue
    mt = r["mt"]
    ton = mt["tongue_onset_all"]
    ex = r["expir_onset"]
    ex = ex[in_bouts(ex, mt)]
    def prob(ev):
        h = np.zeros(len(bins) - 1)
        for e in ev:
            h += np.histogram(ton - e, bins)[0]
        return h / max(len(ev), 1)
    ps, pe = prob(sw), prob(ex)
    c = bins[:-1]
    w = (c >= 0) & (c < 0.1)
    rows.append({"subject": s.subject, "session": s.session, "swallows": len(sw), "expirations": len(ex),
                 "p_swallow": ps[w].mean(), "p_expiration": pe[w].mean()})
lp = pd.DataFrame(rows)
wt = stats.wilcoxon(lp.p_swallow, lp.p_expiration)
print(f"Sessions with >= 20 swallows: {len(lp)}; lick probability per 3.4 ms bin, 0 to 100 ms after onset:")
print(lp[["p_swallow", "p_expiration"]].describe().round(4).to_string())
print(f"Lower around swallows in {int((lp.p_swallow < lp.p_expiration).sum())} of {len(lp)} sessions; Wilcoxon signed-rank p = {wt.pvalue:.2e}")
print("Median ratio swallow / expiration:", round(float((lp.p_swallow / lp.p_expiration).median()), 3))
''', tags=["claim:ed1bc-licks-pause-at-swallows"])

md(r'''
**Result: ED1BC**
''')

code(r'''
# Figure 1k-n: swallow-aligned licks and breaths (code get_licks_around_event, plot_*_swallow_summary)
al_l, al_b, owner = [], [], []
for r, (_, s) in zip(res, sess.iterrows()):
    mt = r["mt"]
    a = kaku.events_around_swallows(r["swallows"], mt["tongue_onset"], r["trial_len"])
    b = kaku.events_around_swallows(r["swallows"], mt["inspir_onset"], r["trial_len"])
    al_l += a; al_b += b; owner += [s.session] * len(a)
owner = np.array(owner)
SWL = kaku.swallow_intervals(al_l, max_ili=1 / 3)
SWB = kaku.swallow_intervals(al_b, max_ili=1 / 2)
SWL["session"] = owner[SWL.event]; SWB["session"] = owner[SWB.event]
print("Swallow events pooled:", len(al_l), "; kept for licks:", len(SWL), "; kept for breaths:", len(SWB))

def readings(df):
    n3 = len(df) // 3
    out = {"(a) code: longest third of cycle 0": df.iloc[:n3],
           "(b) longest third of cycle -1": df.sort_values("cm1", ascending=False).iloc[:n3],
           "(c) all events": df}
    return out

def k_test(df, name):
    n3 = len(df) // 3
    for rk, col in (("(a) by cycle 0", "c0"), ("(b) by cycle -1", "cm1")):
        o = df.sort_values(col, ascending=False)
        top, bot = o.iloc[:n3], o.iloc[-n3:]
        dl = abs(top.latency.median() - bot.latency.median()); dc = abs(top.cm1.median() - bot.cm1.median())
        print(f"{name} {rk}: median latency to first {name} after swallow, top third {top.latency.median() * 1000:.1f} ms, bottom third {bot.latency.median() * 1000:.1f} ms "
              f"(difference {dl * 1000:.1f}); median cycle -1 {top.cm1.median() * 1000:.1f} and {bot.cm1.median() * 1000:.1f} ms (difference {dc * 1000:.1f}); smaller: {dl < dc}")
k_test(SWL, "lick")
k_test(SWB, "breath")
''', tags=["claim:fig1k-rhythms-follow-swallow-at-fixed-latency"])

md(r'''
**Result: FIG1K**
''')

code(r'''
def delta_tests(df, label):
    rows = []
    for name, d in readings(df).items():
        for q, col in (("Delta(1,-1)", "d1"), ("Delta(0,-1)", "d0")):
            x = (d.c1 - d.cm1) if col == "d1" else (d.c0 - d.cm1)
            t = stats.ttest_1samp(x, 0)
            rows.append({"events": label, "reading": name, "quantity": q, "n": len(x), "mean_ms": x.mean() * 1000, "p": t.pvalue})
    d = readings(df)["(a) code: longest third of cycle 0"]
    for q in ("Delta(1,-1)", "Delta(0,-1)"):
        x = (d.c1 - d.cm1) if q == "Delta(1,-1)" else (d.c0 - d.cm1)
        sm = x.groupby(d.session.to_numpy()).mean()
        t = stats.ttest_1samp(sm, 0)
        rows.append({"events": label, "reading": "(d) (a) with session means", "quantity": q, "n": len(sm), "mean_ms": sm.mean() * 1000, "p": t.pvalue})
    return pd.DataFrame(rows)
DL = delta_tests(SWL, "licks")
print(DL.round(4).to_string(index=False))
''', tags=["claim:fig1l-lick-interval-preserved", "claim:fig1l-lick-cycle-prolonged"])

md(r'''
**Result: FIG1L**
''')

code(r'''
DB = delta_tests(SWB, "breaths")
print(DB.round(4).to_string(index=False))
''', tags=["claim:fig1n-breath-interval-preserved", "claim:fig1n-breath-cycle-prolonged"])

md(r'''
**Result: FIG1N**
''')

# ------------------------------------------------------------------------------------- tuning
md(r'''
## Phase tuning (Figure 2, Extended Data Figures 4, 5 and 8)

The measured MI is the code's curve_fit; significance uses the grid fit (helper docstring). The
check below compares the two fits, and the code's own 100-resample scheme with curve_fit against
the grid version on a random sample of units.
''')

code(r'''
rng_chk = np.random.default_rng(5)
chk = []
pool = [(r, p, u) for r in res for p, us in r["units"].items() for u in us]
idx = rng_chk.choice(len(pool), 300, replace=False)
for i in idx:
    r, p, u = pool[i]
    for mod, fs in (("jaw", r["video_fs"]), ("br", 250.0)):
        cnt, occ, cen = u[f"{mod}_cnt_5"], u[f"{mod}_occ_5"], u[f"{mod}_cen_5"]
        if cnt is None or cnt.sum() == 0 or (occ == 0).any():
            continue
        chk.append({"mod": mod, "code": u[f"{mod}_mi_5"], "grid": u[f"{mod}_mi_grid_5"]})
chk = pd.DataFrame(chk)
for mod, g in chk.groupby("mod"):
    d = (g.grid - g.code).abs()
    print(f"{mod}: {len(g)} random units, |grid MI - code MI| median {d.median():.4f}, 90th pct {d.quantile(.9):.3f}; "
          f"same side of 0.6 in {np.mean((g.grid > 0.6) == (g.code > 0.6)):.3f}")
# the code's significance scheme with curve_fit (100 + 100 resamples) on units with code MI > 0.6
cand = [(r, p, u, mod) for (r, p, u) in pool for mod in ("jaw", "br") if (u.get(f"{mod}_mi_5") or 0) > 0.6]
sel = rng_chk.choice(len(cand), 24, replace=False)
rows = []
t0 = time.time()
for i in sel:
    r, p, u, mod = cand[i]
    fs = r["video_fs"] if mod == "jaw" else 250.0
    cnt, occ, cen = u[f"{mod}_cnt_5"], u[f"{mod}_occ_5"], u[f"{mod}_cen_5"]
    n = int(cnt.sum())
    boot = rng_chk.multinomial(n, cnt / n, size=100) / occ * fs
    null = rng_chk.multinomial(n, occ / occ.sum(), size=100) / occ * fs
    mb = [kaku.code_phase_tuning(cen, y)[1] for y in boot]
    mn = [kaku.code_phase_tuning(cen, y)[1] for y in null]
    p_cf = stats.mannwhitneyu(mb, mn, alternative="greater").pvalue
    rows.append({"mod": mod, "mi": u[f"{mod}_mi_5"], "p_code_curvefit": p_cf, "p_code_grid": u[f"{mod}_p_code_5"]})
cc = pd.DataFrame(rows)
print(f"\nCode scheme on {len(cc)} units with MI > 0.6 ({time.time() - t0:.0f} s): significant at 0.001 by curve_fit {int((cc.p_code_curvefit < .001).sum())}, "
      f"by grid {int((cc.p_code_grid < .001).sum())}, same decision {int(((cc.p_code_curvefit < .001) == (cc.p_code_grid < .001)).sum())}")
''', tags=["sanity"])

code(r'''
def tuned(mod, order, sig, mi_thr=0.6, p_thr=0.001):
    mi = T[f"{mod}_mi_{order}"]
    if sig is None:
        return (mi > mi_thr).to_numpy()
    return ((mi > mi_thr) & (T[f"{mod}_p_{sig}_{order}"] < p_thr)).to_numpy()
rows = []
for order, oname in ((4, "V2(a) order 4"), (2, "V2(b) order 2"), (5, "code order 5")):
    for sig, sname in (("a", "V3(a)"), ("b", "V3(b)"), ("code", "code 100")):
        L, B = tuned("jaw", order, sig), tuned("br", order, sig)
        rows.append({"filter": oname, "significance": sname, "lick (i)": int(L.sum()), "breath (i)": int(B.sum()), "both": int((L & B).sum()),
                     "lick (ii)": int((L & ~B).sum()), "breath (ii)": int((B & ~L).sum())})
TC = pd.DataFrame(rows)
TC["both/lick"] = TC.both / TC["lick (i)"]; TC["both/breath"] = TC.both / TC["breath (i)"]
def within(x, v, t):
    return abs(x - v) <= t
TC["match (i)"] = within(TC["lick (i)"], 3551, 355) & within(TC["breath (i)"], 1015, 102) & within(TC.both, 182, 18)
TC["match (ii)"] = within(TC["lick (ii)"], 3551, 355) & within(TC["breath (ii)"], 1015, 102) & within(TC.both, 182, 18)
TC["partial"] = (TC["both/lick"] < 0.10) & (TC["both/breath"] < 0.25)
print(TC.round(3).to_string(index=False))
print("\nPaper: licking 3551 (+-355), breathing 1015 (+-102), both 182 (+-18) of 20,300; ratios both/lick 5%, both/breath 18%")
print("Units without a breathing fit (no kept trials or empty bins):", int(T.br_mi_4.isna().sum()), "; jaw:", int(T.jaw_mi_4.isna().sum()))
print("\nBy subject, reading V2(a) V3(b):")
print(pd.DataFrame({"units": T.groupby("subject").size(), "lick": pd.Series(tuned("jaw", 4, "b")).groupby(T.subject.to_numpy()).sum(),
                    "breath": pd.Series(tuned("br", 4, "b")).groupby(T.subject.to_numpy()).sum()}).T.to_string())
''', tags=["claim:fig2-licking-breathing-tuned-counts"])

md(r'''
**Result: FIG2COUNTS**
''')
EOF
cd $TMPDIR && . env/bin/activate && python dev.py 15 2>&1 | grep -v "^DL0\|^subject" | tail -90
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/dev.py", line 18, in <module>
    exec(src, ns)
    ~~~~^^^^^^^^^
  File "<string>", line 3, in <module>
NameError: name 'bf_a' is not defined
===== cell 0 []
335 files, 130.1 GB, read in 1 s (metadata)
===== cell 1 []
===== cell 2 []
Good units with session results: 20109 of 20109
===== cell 3 ['sanity']
Subjects: 31 ; sessions: 173 ; files (insertions): 335
Sex per subject: {'M': 22, 'F': 9}
Age field values (first 8): ['P210W', 'P215W', 'P216W', 'P222W', 'P238W', 'P239W', 'P243W', 'P245W'] ...
Genotype field: ['animalStrain: 014548; animalGeneModification: Cg-Tg(Slc32a1-COP4*H134R/EYFP)8Gfng/J; animalGeneCopy: 1; animalGeneticBackground: unidentified']
Stimulus field: ['photostim'] ; acquisition groups: [] ; stimulus/presentation: []
Trial table columns: ['start_time', 'stop_time', 'trial_duration'] ; largest start_time over all files: 0.0
Trial duration range (s): 5.7368 to 15.738
Trials per file: {'min': 113.0, '50%': 349.0, 'max': 359.0}
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && time python dev.py 0 save 2>&1 | sed -n '/cell 15/,$p' | tail -90
```

```
===== cell 15 ['claim:ed1-unidirectional-models-fail']
Empirical ranges: inter-lick [0.075 0.286] s, inter-breath [0.15  0.476] s; latencies: last lick -> inspiration nan s, inspiration -> next lick 0.119 s
breath_model_fig1g: sessions with a value 0, mean nan ms, p = nan
breath_model_fig1i: sessions with a value 0, mean nan ms, p = nan
lick_model_fig1g: sessions with a value 0, mean nan ms, p = nan
lick_model_fig1i: sessions with a value 169, mean 34.2 ms, p = 3.3e-101
Data: Fig 1g mean 22.0 ms (p = 4.51e-04); Fig 1i mean 10.5 ms (p = 1.45e-09)
===== cell 16 ['claim:ed1bc-licks-pause-at-swallows']
Sessions with >= 20 swallows: 90; lick probability per 3.4 ms bin, 0 to 100 ms after onset:
       p_swallow  p_expiration
count    90.0000       90.0000
mean      0.0308        0.0211
std       0.0045        0.0020
min       0.0187        0.0159
25%       0.0289        0.0198
50%       0.0313        0.0208
75%       0.0335        0.0222
max       0.0411        0.0263
Lower around swallows in 4 of 90 sessions; Wilcoxon signed-rank p = 4.02e-16
Median ratio swallow / expiration: 1.498
[... 56 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import sys,pickle; sys.path.insert(0,'entries/001619-kaku-2025')
import kaku,numpy as np
res=pickle.load(open('res_173.pkl','rb'))
rng=np.random.default_rng(0)
lf=[];bf=[]
mt=res[10]['mt']
ili=np.diff(mt['tongue_onset']); ili=ili[(ili>0.075)&(ili<0.286)]
ibi=np.diff(mt['inspir_onset'])
licks=np.cumsum(rng.choice(ili,3000)); cand=licks-0.119
ins=[cand[0]]
for c in cand[1:]:
    if c-ins[-1]>=0.15: ins.append(c)
ins=np.sort(np.array(ins)+rng.normal(0,0.01,len(ins)))
m={'tongue_onset':licks,'inspir_onset':ins,'bout_on':np.array([licks[0]]),'bout_off':np.array([licks[-1]])}
a=kaku.peak_diff_lick_behv(m)
print(a.keys(), a['diff'], len(a.get('i_fast',[])), np.bincount(a['n_licks'])[:6], a.get('peaks_fast'), a.get('peaks_slow'))
EOF
```

```
Thu Nov  5 09:23:14 UTC 2026
dict_keys(['t0', 'licks', 'lick_bef', 'n_licks', 'ibi', 'max_ibi', 'last_lick_to_next_insp', 'i_fast', 'i_slow', 'peaks_fast', 'peaks_slow', 'diff', 'unit_fast', 'unit_slow']) nan 173 [  0 679 346  46] [] []
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import pickle,numpy as np
ns=pickle.load(open('ns.pkl','rb')); units=ns['units']
for a in ['AMB','AMBd','AMBv','NTS','IRN','PARN','XII','V','IC','ICe','NLL']:
    m=units.acronym==a
    print(a, m.sum(), units[m].ccf_x.min(), units[m].ccf_x.max(), units[m].ccf_y.min(), units[m].ccf_y.max(), units[m].ccf_z.min(), units[m].ccf_z.max())
print(np.unique(units.ccf_x.dropna())[:20])
EOF
```

```
AMB 0 nan nan nan nan nan nan
AMBd 45 4200.0 7060.0 6480.0 6600.0 11460.0 11540.0
AMBv 42 4300.0 4380.0 6640.0 6760.0 12120.0 12420.0
NTS 4331 4120.0 7220.0 4900.0 5520.0 11160.0 12840.0
IRN 19432 4140.0 7120.0 5340.0 6920.0 10440.0 13140.0
PARN 10614 3840.0 7600.0 5160.0 6800.0 10420.0 12400.0
XII 1579 5280.0 6160.0 5300.0 6020.0 12120.0 12960.0
V 2132 3860.0 7340.0 4920.0 5740.0 9860.0 10460.0
IC 0 nan nan nan nan nan nan
ICe 3985 3540.0 7880.0 2000.0 3280.0 9320.0 10800.0
NLL 2655 3460.0 7840.0 3760.0 6460.0 9100.0 10060.0
[2420. 2440. 2460. 2480. 2500. 2520. 2540. 2560. 2580. 2600. 2620. 2640.
 2660. 2680. 2700. 2720. 2740. 2760. 2780. 2800.]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/cells.py <<'EOF'

code(r'''
# Swallow modulation (code get_swallow_tuning, generate_activity_maps.m)
sw_sessions = {r["key"][1] for r in res if len(r["swallow_times"]) > 0}
T["sess_has_sw"] = T.session.isin(sw_sessions)
T["sw_mod_a"] = (T.sw_mi > 0.3) & (T.sw_p <= 0.01) & (T.sw_n >= 20)
T["sw_mod_b"] = (T.sw_mi_b > 0.3) & (T.sw_p <= 0.01) & (T.sw_n >= 20)
rows = []
for v4, col in (("V4(a) larger window rate", "sw_mod_a"), ("V4(b) PSTH peak", "sw_mod_b")):
    S = T[col].to_numpy()
    for order, sig in ((4, "a"), (4, "b"), (2, "a"), (2, "b"), (5, "code")):
        L, B = tuned("jaw", order, sig), tuned("br", order, sig)
        for den, dm in (("(a) sessions with a swallow", T.sess_has_sw.to_numpy()), ("(b) >= 20 swallows", (T.sw_n >= 20).to_numpy())):
            for only, om in (("(i) not lick or breath", ~L & ~B), ("(ii) not lick", ~L)):
                rows.append({"V4": v4, "tuning": f"order {order}, {sig}", "denominator": den, "only": only, "units": int(dm.sum()),
                             "swallow only": int((S & om).sum()), "lick and swallow": int((S & L).sum()), "breath and swallow": int((S & B).sum()),
                             "swallow total": int(S.sum())})
SC = pd.DataFrame(rows)
SC["match"] = (abs(SC.units - 18485) <= 1849) & (abs(SC["swallow only"] - 427) <= 43) & (abs(SC["lick and swallow"] - 175) <= 18) & (abs(SC["breath and swallow"] - 55) <= 6)
print(SC.to_string(index=False))
print("\nPaper: 18,485 units; swallow only 427 (+-43), licking and swallowing 175 (+-18), breathing and swallowing 55 (+-6)")
print("Units with >= 20 swallow events:", int((T.sw_n >= 20).sum()), "; sessions with a swallow:", len(sw_sessions), "of", len(res))
''', tags=["claim:fig2-swallow-modulated-counts"])

md(r'''
**Result: FIG2SW**
''')

code(r'''
# Regions the CCF does not label (claims file O3), from the positions of the units the files label.
allu = units.dropna(subset=["ccf_x"])
amb = allu[allu.acronym.isin(["AMB", "AMBd", "AMBv"])]
nts = allu[allu.acronym.isin(["NTS"])]
irn = allu[allu.acronym.isin(["IRN"])]
T["ml"] = (T.ccf_x - 5700).abs()
amb_ap = (amb.ccf_z.min(), amb.ccf_z.max()); amb_ml = ((amb.ccf_x - 5700).abs().min(), (amb.ccf_x - 5700).abs().max())
amb_dv = (amb.ccf_y.min(), amb.ccf_y.max())
print(f"AMB from {len(amb)} labelled units (all qualities): AP {amb_ap}, |ML| {amb_ml}, DV {amb_dv} um")
irn_ap_mid = (irn.ccf_z.min() + irn.ccf_z.max()) / 2; irn_dv_mid = (irn.ccf_y.min() + irn.ccf_y.max()) / 2
print(f"IRN from {len(irn)} labelled units: AP midpoint {irn_ap_mid}, DV midpoint {irn_dv_mid} um")
in_amb_box = T.ccf_z.between(*amb_ap) & T.ml.between(*amb_ml)
def prebotc(d):
    return (in_amb_box & (T.ccf_y > amb_dv[1]) & (T.ccf_y <= amb_dv[1] + d)).to_numpy()
def above_amb(d):
    return (in_amb_box & (T.ccf_y < amb_dv[0]) & (T.ccf_y >= amb_dv[0] - d)).to_numpy()
pv_irn = (T.in_IRN & (T.ccf_z > irn_ap_mid) & (T.ccf_y > irn_dv_mid)).to_numpy()
pd_irn_parn = ((T.in_IRN | T.in_PARN) & (T.ccf_z > irn_ap_mid) & (T.ccf_y < irn_dv_mid)).to_numpy()
nts_ap = (nts.ccf_z.min(), nts.ccf_z.max())
def lateral_nts(d):
    # lateral of NTS: beyond the most lateral NTS unit at the same AP (100 um AP bins), within d
    edge = (nts.assign(apb=(nts.ccf_z // 100), ml=(nts.ccf_x - 5700).abs()).groupby("apb").ml.max())
    e = (T.ccf_z // 100).map(edge)
    return (T.ccf_z.between(*nts_ap) & e.notna() & (T.ml > e) & (T.ml <= e + d) & ~T.in_NTS).to_numpy()
PM = (T.in_P | T.in_MY).to_numpy()
for d in (300, 500):
    print(f"d = {d} um: units near preBotC {prebotc(d).sum()}, above AMB {above_amb(d).sum()}, lateral of NTS {lateral_nts(d).sum()}")
print("posterior-ventral IRN:", pv_irn.sum(), "; posterior-dorsal IRN/PARN:", pd_irn_parn.sum(), "; pons and medulla:", PM.sum())

def enrich(sel, flag, base):
    a = int((sel & flag).sum()); b = int((sel & ~flag).sum())
    c = int((base & flag).sum()); d_ = int((base & ~flag).sum())
    p = stats.fisher_exact([[a, b], [c, d_]], alternative="greater")[1] if a + b > 0 else np.nan
    return {"n": a + b, "tuned": a, "fraction": a / (a + b) if a + b else np.nan, "base fraction": c / (c + d_), "p": p}

rows = []
for order, sig in ((4, "a"), (4, "b"), (2, "a"), (2, "b"), (5, "code")):
    B = tuned("br", order, sig)
    for d in (300, 500):
        rows.append({"tuning": f"order {order}, {sig}", "region": f"preBotC ({d} um)", **enrich(prebotc(d), B, PM)})
    rows.append({"tuning": f"order {order}, {sig}", "region": "posterior ventral IRN", **enrich(pv_irn, B, PM)})
BL = pd.DataFrame(rows)
print(BL.round(4).to_string(index=False))
''', tags=["claim:fig2f-breathing-units-location"])

md(r'''
**Result: FIG2F**
''')

code(r'''
rows = []
for order, sig in ((4, "a"), (4, "b"), (2, "a"), (2, "b"), (5, "code")):
    L = tuned("jaw", order, sig)
    for name, m in (("XII", T.in_XII), ("V", T.in_V), ("IRN", T.in_IRN)):
        rows.append({"tuning": f"order {order}, {sig}", "region": name, **enrich(m.to_numpy(), L, PM)})
    pons = T.in_P.to_numpy()
    rows.append({"tuning": f"order {order}, {sig}", "region": "P (fraction > 1%?)", "n": int(pons.sum()), "tuned": int((pons & L).sum()),
                 "fraction": (pons & L).sum() / pons.sum(), "base fraction": np.nan, "p": np.nan})
LL = pd.DataFrame(rows)
print(LL.round(5).to_string(index=False))
''', tags=["claim:fig2g-licking-units-location"])

md(r'''
**Result: FIG2G**
''')

code(r'''
base_sw = T.sess_has_sw.to_numpy()
rows = []
for v4, col in (("V4(a)", "sw_mod_a"), ("V4(b)", "sw_mod_b")):
    S = T[col].to_numpy()
    for d in (300, 500):
        for name, m in (("V", T.in_V.to_numpy()), ("IC", T.in_IC.to_numpy()), ("NLL", T.in_NLL.to_numpy()),
                        ("lateral of NTS", lateral_nts(d)), ("above AMB", above_amb(d))):
            rows.append({"V4": v4, "d": d, "region": name, **enrich(m & base_sw, S, base_sw)})
SL = pd.DataFrame(rows)
SL["enriched"] = (SL.fraction > SL["base fraction"]) & (SL.p < 0.05)
print(SL.round(4).to_string(index=False))
print("\nRegions enriched (of 5) per V4 reading and distance:")
print(SL.groupby(["V4", "d"]).enriched.sum().to_string())
''', tags=["claim:fig2h-swallow-units-location"])

md(r'''
**Result: FIG2H**
''')

code(r'''
rows = []
for v4, col in (("V4(a)", "sw_mod_a"), ("V4(b)", "sw_mod_b")):
    S = T[col]
    lead = T[S & (T.in_V | T.in_IRN)].sw_peak_t
    follow = T[S & (T.in_IC | T.in_NLL)].sw_peak_t
    mw = stats.mannwhitneyu(lead, follow, alternative="two-sided") if len(lead) and len(follow) else None
    rows.append({"V4": v4, "V and IRN n": len(lead), "V and IRN median peak (s)": lead.median(), "IC and NLL n": len(follow),
                 "IC and NLL median peak (s)": follow.median(), "Mann-Whitney p": mw.pvalue if mw else np.nan})
    for name, m in (("V", T.in_V), ("IRN", T.in_IRN), ("IC", T.in_IC), ("NLL", T.in_NLL)):
        x = T[S & m].sw_peak_t
        print(f"{v4} {name}: n = {len(x)}, median peak {x.median() if len(x) else np.nan:.3f} s, range {x.min() if len(x) else np.nan:.3f} to {x.max() if len(x) else np.nan:.3f}")
print(pd.DataFrame(rows).round(4).to_string(index=False))
''', tags=["claim:ed6e-swallow-latencies"])

md(r'''
**Result: ED6E**
''')

code(r'''
def rayleigh(th):
    n = len(th)
    R = np.abs(np.mean(np.exp(1j * th))) * n
    z = R ** 2 / n
    return np.exp(np.sqrt(1 + 4 * n + 4 * (n ** 2 - R ** 2)) - (1 + 2 * n)) if n else np.nan
rows = []
for order, sig in ((4, "a"), (4, "b"), (2, "a"), (2, "b"), (5, "code")):
    B = tuned("br", order, sig, mi_thr=0.9)
    for d in (300, 500):
        sel = B & prebotc(d)
        ph_ = np.mod(T.loc[sel, f"br_pref_{order}"].to_numpy() - np.pi, 2 * np.pi)   # inspiration onset at 0
        rows.append({"tuning": f"order {order}, {sig}", "d": d, "units": int(sel.sum()), "inspiration half": int((ph_ < np.pi).sum()),
                     "fraction": np.mean(ph_ < np.pi) if len(ph_) else np.nan, "Rayleigh p": rayleigh(ph_)})
print(pd.DataFrame(rows).round(4).to_string(index=False))
B = tuned("br", 4, "a", mi_thr=0.9)
ph_all = np.mod(T.loc[B, "br_pref_4"].to_numpy() - np.pi, 2 * np.pi)
print(f"All breathing units (MI > 0.9, order 4, V3(a)): {B.sum()}, in the inspiration half {np.mean(ph_all < np.pi):.3f}")
''', tags=["claim:ed8bc-prebotc-inspiration-phase"])

md(r'''
**Result: ED8BC**
''')

code(r'''
def circ_median(x):
    x = np.asarray(x)
    if not len(x):
        return np.nan
    c = np.linspace(0, 2 * np.pi, 360, endpoint=False)
    return c[np.argmin([np.sum(kaku._circ_dist(x, m)) for m in c])]
prot = {o: {r["key"][1]: circ_median(r["protrusion_phase"][o]) for r in res} for o in kaku.FILTER_ORDERS}
rows = []
for order, sig in ((4, "a"), (4, "b"), (2, "a"), (2, "b"), (5, "code")):
    L = tuned("jaw", order, sig, mi_thr=0.9)
    pm = T.session.map(prot[order]).to_numpy()
    dd = kaku._circ_dist(T[f"jaw_pref_{order}"].to_numpy(), pm)
    rows.append({"tuning": f"order {order}, {sig}", "units": int(L.sum()), "within pi/2 of protrusion": int((L & (dd < np.pi / 2)).sum()),
                 "fraction": np.mean(dd[L] < np.pi / 2)})
print(pd.DataFrame(rows).round(4).to_string(index=False))
pv = pd.Series(prot[4]).dropna()
print("Session circular median protrusion phase (order 4), quartiles (rad):", np.percentile(pv, [25, 50, 75]).round(3))
print("Licks per session with a protrusion frame:", pd.Series({r["key"][1]: len(r["protrusion_phase"][4]) for r in res}).describe()[["min", "50%", "max"]].to_dict())
''', tags=["claim:ed8e-licking-units-protrusion"])

md(r'''
**Result: ED8E**
''')

code(r'''
hi = (T.unit_amp > 500).to_numpy()
print("Good units with amplitude > 500 uV:", int(hi.sum()), "(paper 2223, tolerance 222); of good units:", len(T))
rows = []
for order in (4, 2, 5):
    d = T.assign(hi=hi).groupby("region").agg(n_hi=("hi", "sum"), mi_all=(f"jaw_mi_{order}", "mean"))
    d["mi_hi"] = T[hi].groupby("region")[f"jaw_mi_{order}"].mean()
    d = d[d.n_hi >= 20]
    rho = stats.spearmanr(d.mi_all, d.mi_hi)
    rows.append({"filter order": order, "regions with >= 20": len(d), "Spearman rho": rho.statistic, "p": rho.pvalue})
print(pd.DataFrame(rows).round(5).to_string(index=False))
''', tags=["claim:ed4c-licking-map-insensitive-to-sorting"])

md(r'''
**Result: ED4C**
''')

code(r'''
# Figure 4e-f: unit peak differences; O1 unit readings and O2 recording readings
two_probe = files.groupby(["subject", "session"]).probe.nunique()
two_probe = set(two_probe[two_probe == 2].index.get_level_values(1))
def sim_sessions(Lm, Bm, d):
    """Sessions with two probes, one holding licking units in posterior-dorsal IRN/PARN and the other
    breathing units near the preBotC (O2 (b), O3)."""
    pre = prebotc(d)
    out = {}
    for ses in two_probe:
        s = (T.session == ses).to_numpy()
        lick_p = set(T.loc[s & Lm & pd_irn_parn, "probe"]); br_p = set(T.loc[s & Bm & pre, "probe"])
        pairs = [(a, b) for a in lick_p for b in br_p if a != b]
        if pairs:
            out[ses] = pairs
    return out
O1 = {"(a) MI > 0.6, P < 0.001": dict(mi_thr=0.6), "(b) MI > 0.9, P < 0.001": dict(mi_thr=0.9), "(c) MI > 0.9 alone": dict(mi_thr=0.9, sig=None)}
rows = []
for oname, kw in O1.items():
    sig = kw.get("sig", "a")
    for sname in (["a", "b"] if sig is not None else [None]):
        L = tuned("jaw", 4, sname, mi_thr=kw["mi_thr"]); B = tuned("br", 4, sname, mi_thr=kw["mi_thr"])
        for which, Um, col in (("fig4e licking units", L, "pd_lick_unit"), ("fig4f breathing units", B, "pd_breath_unit")):
            for o2 in ("(a) all sessions", "(b) simultaneous, 300 um", "(b) simultaneous, 500 um"):
                m = Um.copy()
                if o2.startswith("(b)"):
                    ss = sim_sessions(L, B, 300 if "300" in o2 else 500)
                    region = pd_irn_parn if which.startswith("fig4e") else prebotc(300 if "300" in o2 else 500)
                    m = m & T.session.isin(ss.keys()).to_numpy() & region
                x = T.loc[m, col].dropna()
                tt = stats.ttest_1samp(x, 0) if len(x) > 2 else None
                rows.append({"claim": which, "O1": oname, "V3": sname, "O2": o2, "units": len(x), "mean_ms": x.mean() * 1000 if len(x) else np.nan,
                             "p": tt.pvalue if tt else np.nan, "positive": int((x > 0).sum()), "negative": int((x < 0).sum())})
PDU = pd.DataFrame(rows)
print(PDU.round(4).to_string(index=False))
''', tags=["claim:fig4e-licking-units-anticipate-breath", "claim:fig4f-breathing-units-anticipate-lick"])

md(r'''
**Result: FIG4EF**
''')

code(r'''
rows = []
for oname, kw in O1.items():
    for sname in (["a", "b"] if kw.get("sig", "a") is not None else [None]):
        L = tuned("jaw", 4, sname, mi_thr=kw["mi_thr"]); B = tuned("br", 4, sname, mi_thr=kw["mi_thr"])
        for d in (300, 500):
            ss = sim_sessions(L, B, d)
            nl, nb = [], []
            for ses, pairs in ss.items():
                s = (T.session == ses).to_numpy()
                a, b = pairs[0]
                nl.append(int((s & L & pd_irn_parn & (T.probe == a).to_numpy()).sum()))
                nb.append(int((s & B & prebotc(d) & (T.probe == b).to_numpy()).sum()))
            mice = {T.loc[T.session == ses, "subject"].iloc[0] for ses in ss}
            rows.append({"O1": oname, "V3": sname, "O3": f"{d} um", "recordings": len(ss), "mice": len(mice),
                         "licking units per recording": f"{min(nl) if nl else 0}-{max(nl) if nl else 0}",
                         "breathing units per recording": f"{min(nb) if nb else 0}-{max(nb) if nb else 0}"})
print(pd.DataFrame(rows).to_string(index=False))
print("Paper: 43 recordings (+-4) in 21 mice (+-2); 1-28 licking and 1-12 breathing units per recording")
print("Two-probe sessions in the dandiset:", len(two_probe), "in", files[files.session.isin(two_probe)].subject.nunique(), "mice")
''', tags=["claim:fig4d-simultaneous-recordings"])

md(r'''
**Result: FIG4D**
''')

code(r'''
print(f"Notebook run time: {(time.time() - t_start) / 60:.1f} min")
''')
EOF
cd $TMPDIR && . env/bin/activate && python dev.py 0 2>&1 | sed -n '/cell 22/,$p' | tail -150
```

```
order 4, b      preBotC (500 um)  16      5    0.3125         0.0445 0.0005
   order 4, b posterior ventral IRN 470     72    0.1532         0.0445 0.0000
   order 2, a      preBotC (300 um)  16      5    0.3125         0.0669 0.0032
   order 2, a      preBotC (500 um)  16      5    0.3125         0.0669 0.0032
   order 2, a posterior ventral IRN 470     88    0.1872         0.0669 0.0000
   order 2, b      preBotC (300 um)  16      5    0.3125         0.0441 0.0005
   order 2, b      preBotC (500 um)  16      5    0.3125         0.0441 0.0005
   order 2, b posterior ventral IRN 470     71    0.1511         0.0441 0.0000
order 5, code      preBotC (300 um)  16      6    0.3750         0.0658 0.0004
order 5, code      preBotC (500 um)  16      6    0.3750         0.0658 0.0004
order 5, code posterior ventral IRN 470     84    0.1787         0.0658 0.0000
===== cell 24 ['claim:fig2g-licking-units-location']
       tuning             region    n  tuned  fraction  base fraction   p
   order 4, a                XII  166     72   0.43373        0.25198 0.0
   order 4, a                  V  269    148   0.55019        0.25198 0.0
   order 4, a                IRN 1804    712   0.39468        0.25198 0.0
   order 4, a P (fraction > 1%?) 3021    609   0.20159            NaN NaN
   order 4, b                XII  166     61   0.36747        0.20320 0.0
   order 4, b                  V  269    118   0.43866        0.20320 0.0
   order 4, b                IRN 1804    611   0.33869        0.20320 0.0
[... 131 more lines not kept]
```

**Agent**

Most cells run. Before building the notebook I'm checking how `tools/entry.py` executes and checks entries, to decide when the conclusion text must be final.

**Agent calls Bash**

```bash
grep -n "def \|argparse\|add_parser\|timeout\|executed" tools/entry.py | head -80
```

```
8:    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies
27:directory. The executed copies
28:go to --output-dir (default: executed/<name>/, which git ignores). A notebook
32:(docs/protocol.md): the executed notebooks with the conclusions removed (every
35:executed/<name>/handover/. Run the entry first.
43:import argparse
70:    def __init__(self):
73:    def error(self, where, message: str) -> None:
78:def dataset_id(record: dict) -> str | None:
83:def schema(name: str) -> Draft202012Validator:
94:def _parsed(text: str):
102:def _schema_errors(text: str, schema_name: str) -> tuple[str, ...]:
108:def load(report: Report, path: Path):
116:def validate(report: Report, path: Path, schema_name: str) -> dict | None:
125:def _plain(value):
136:def code_of(notebook_path: Path) -> str:
143:def check(entry_dir: Path) -> Report:
313:def _local_data(code: str, start: int) -> bool:
320:def _derivation_checks(report: Report, where, code: str) -> None:
334:def lock(entry_dir: Path) -> int:
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,42p tools/entry.py; sed -n 143,320p tools/entry.py; sed -n 334,470p tools/entry.py
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
[... 336 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python dev.py 0 2>&1 | sed -n '/cell 22/,/cell 24/p' | grep -E "True|cell|units|Paper|>= 20" | head -30; python dev.py 0 2>&1 | sed -n '/cell 22/,/cell 23/p' | awk 'NR<4 || /order 4, a/' | head -12
```

```
===== cell 22 ['claim:fig2-swallow-modulated-counts']
                      V4        tuning                 denominator                   only  units  swallow only  lick and swallow  breath and swallow  swallow total  match
V4(a) larger window rate    order 4, a          (b) >= 20 swallows (i) not lick or breath  10807           260               211                  88            527  False
V4(a) larger window rate    order 4, a          (b) >= 20 swallows          (ii) not lick  10807           316               211                  88            527  False
V4(a) larger window rate    order 4, b          (b) >= 20 swallows (i) not lick or breath  10807           306               173                  67            527  False
V4(a) larger window rate    order 4, b          (b) >= 20 swallows          (ii) not lick  10807           354               173                  67            527  False
V4(a) larger window rate    order 2, a          (b) >= 20 swallows (i) not lick or breath  10807           258               217                  84            527  False
V4(a) larger window rate    order 2, a          (b) >= 20 swallows          (ii) not lick  10807           310               217                  84            527  False
V4(a) larger window rate    order 2, b          (b) >= 20 swallows (i) not lick or breath  10807           303               176                  65            527  False
V4(a) larger window rate    order 2, b          (b) >= 20 swallows          (ii) not lick  10807           351               176                  65            527  False
V4(a) larger window rate order 5, code          (b) >= 20 swallows (i) not lick or breath  10807           260               211                  88            527  False
V4(a) larger window rate order 5, code          (b) >= 20 swallows          (ii) not lick  10807           316               211                  88            527  False
         V4(b) PSTH peak    order 4, a          (b) >= 20 swallow
[... 28 more lines not kept]
```

**Agent**

Swallow-unit denominator matches (18,494 against 18,485), but the modulated counts do not. Building the notebook and entry files now, then the full run.

**Agent calls Bash**

```bash
cd entries/001619-kaku-2025 && cat > requirements.in <<'EOF'
h5py
numpy
pandas
remfile
scipy
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: 001619-kaku-2025
type: reproduction
title: A brainstem map of orofacial rhythms (Kaku, Liu et al. 2025)
description: Tests the findings of Kaku, Liu et al. (2025) on dandiset 001619, which holds the
  brainstem Neuropixels recordings of 31 mice in the multi-directional licking task, with DeepLabCut
  tracking of jaw and tongue, the airflow trace and CCF positions of the units. It ports the paper's
  analysis code to streamed NWB files and tests the lick-breath timing, swallow detection, unit
  counts, phase tuning to licking and breathing, swallow modulation and their maps. The cued licking
  task with photostimulation, the rat recordings, the raw videos and the premotor tracing are not in
  the dandiset.
license: Apache-2.0
notebooks:
- path: reproduce_kaku_2025.ipynb
  title: Reproducing Kaku, Liu et al. (2025) from dandiset 001619
  runtime_minutes: 40
helpers:
- kaku.py
related:
- id: dandi:001619/0.251027.1953
  relation: uses_data
- id: doi:10.1101/2025.01.27.635041
  relation: reproduces
EOF
cat > $TMPDIR/build_nb.py <<'EOF'
import sys, importlib, nbformat
sys.path.insert(0, '/tmp/claude-1001')
import cells; importlib.reload(cells)
nb = nbformat.v4.new_notebook()
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
for kind, tags, src in cells.CELLS:
    c = nbformat.v4.new_markdown_cell(src) if kind == "markdown" else nbformat.v4.new_code_cell(src)
    if tags:
        c.metadata["tags"] = tags
    nb.cells.append(c)
nbformat.write(nb, 'entries/001619-kaku-2025/reproduce_kaku_2025.ipynb')
print(len(nb.cells))
EOF
cd $TMPDIR && . env/bin/activate && python build_nb.py && cd  && python -c "import yaml,jsonschema,nbformat" 2>&1; python tools/entry.py lock entries/001619-kaku-2025 && python tools/entry.py check entries/001619-kaku-2025
```

```
67
wrote entries/001619-kaku-2025/requirements.lock.txt
0 error(s)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python - <<'EOF' 2>&1 | grep -v Warn
import sys,time; sys.path.insert(0,'entries/001619-kaku-2025')
import kaku, warnings; warnings.filterwarnings('ignore')
A=kaku.list_assets()
m,u=kaku.read_probe_meta(A.url.iloc[0]); print(m['breath_head_hash'], m['jaw_head_hash'], u.shape)
ses=A[A.session=='20210310-20210310-141528-s3']
t=time.time(); out=kaku.process_session((('DL004','x'), ses.url.iloc[0], dict(zip(ses.probe,ses.url)), 0)); print(time.time()-t)
print(out['pd_lick']['diff'], out['pd_lick']['last_lick_to_next_insp'][:5])
EOF
```

```
6394f476b3b66a1a519cc39833640724 f2c840da3977d0714c7560a6129c04ff (518, 38)
29.648377418518066
0.18000000000000016 [0.0884 0.102  0.0918 0.0714 0.0986]
Shell cwd was reset to
```

**Agent**

Smoke tests pass. Launching the full entry run (expected about 40 min).

**Agent calls Bash**

```bash
date -u; cd  && python tools/entry.py all entries/001619-kaku-2025 2>&1 | tail -30; date -u
```

```
Thu Nov  5 09:28:56 UTC 2026
Installed kernelspec registry-001619-kaku-2025 in executed/001619-kaku-2025/.venv/share/jupyter/kernels/registry-001619-kaku-2025
0 error(s)
pass  reproduce_kaku_2025.ipynb  (2527 s)
Thu Nov  5 10:11:08 UTC 2026
```

**Agent**

The notebook passed in 42 min. Reading the executed outputs.

**Agent calls Bash**

```bash
python - <<'EOF'
import nbformat
nb=nbformat.read('executed/001619-kaku-2025/reproduce_kaku_2025.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    out=''.join(o.get('text','') if o.output_type=='stream' else str(o.get('data',{}).get('text/plain','')) + str(o.get('ename','')) for o in c.outputs)
    print(f'#### {i} {c.metadata.get("tags")}'); print(out[:6000])
EOF
```

```
<persisted-output>
Output too large (41.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/bff38b74-0a40-431b-a973-ca03f9cbd0c8/tool-results/bl8nnffrh.txt

Preview (first 2KB):
#### 1 None
335 files, 130.1 GB, read in 215 s (metadata)

#### 2 None
173 sessions processed in 37.4 min

#### 3 None
Good units with session results: 20109 of 20109

#### 5 ['sanity']
Subjects: 31 ; sessions: 173 ; files (insertions): 335
Sex per subject: {'M': 22, 'F': 9}
Age field values (first 8): ['P210W', 'P215W', 'P216W', 'P222W', 'P238W', 'P239W', 'P243W', 'P245W'] ...
Genotype field: ['animalStrain: 014548; animalGeneModification: Cg-Tg(Slc32a1-COP4*H134R/EYFP)8Gfng/J; animalGeneCopy: 1; animalGeneticBackground: unidentified']
Stimulus field: ['photostim'] ; acquisition groups: [] ; stimulus/presentation: []
Trial table columns: ['start_time', 'stop_time', 'trial_duration'] ; largest start_time over all files: 0.0
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
F=/home/runner/.claude/projects/-home-runner-work-encore-encore/bff38b74-0a40-431b-a973-ca03f9cbd0c8/tool-results/bl8nnffrh.txt; grep -n "####" $F | head -50; sed -n '/#### 6 /,/#### 12 /p' $F | grep -v "^  DL0" | head -90
```

```
1:#### 1 None
4:#### 2 None
7:#### 3 None
10:#### 5 ['sanity']
56:#### 6 ['sanity']
95:#### 8 ['sanity']
113:#### 10 ['sanity']
124:#### 13 ['claim:code-dataset-link']
135:#### 16 ['claim:units-count']
196:#### 19 ['claim:region-spike-rates']
212:#### 22 ['claim:fig1d-lick-breath-frequencies']
221:#### 24 ['claim:fig1f-inspiration-between-licks']
278:#### 26 ['claim:fig1g-lick-delayed-before-slow-breath']
290:#### 28 ['claim:fig1f-licking-mode-switch']
299:#### 30 ['claim:fig1i-breath-delayed-before-slow-lick']
307:#### 32 ['claim:ed1-unidirectional-models-fail']
315:#### 34 ['claim:ed1bc-licks-pause-at-swallows']
329:#### 36 ['claim:fig1k-rhythms-follow-swallow-at-fixed-latency']
336:#### 38 ['claim:fig1l-lick-interval-preserved', 'claim:fig1l-lick-cycle-prolonged']
347:#### 40 ['claim:fig1n-breath-interval-preserved', 'claim:fig1n-breath-cycle-prolonged']
[... 103 more lines not kept]
```

**Agent calls Bash**

```bash
F=/home/runner/.claude/projects/-home-runner-work-encore-encore/bff38b74-0a40-431b-a973-ca03f9cbd0c8/tool-results/bl8nnffrh.txt; sed -n '196,420p' $F | grep -v "^DL0[0-9][0-9] "
```

```
#### 19 ['claim:region-spike-rates']
                                      rate             medulla  CB mean  CB sd  CB n  VNC mean  VNC sd  VNC n  MY mean  MY sd  MY n
                       (a) avg_firing_rate     (i) MY with VNC    21.26  28.82  4157     27.24   28.81   1276    13.23  18.18  8992
                       (a) avg_firing_rate (ii) MY without VNC    21.26  28.82  4157     27.24   28.81   1276    10.91  14.50  7716
(b) spikes in the first 5 s of good trials     (i) MY with VNC    21.40  28.86  4157     27.22   28.69   1276    13.57  18.26  8992
(b) spikes in the first 5 s of good trials (ii) MY without VNC    21.40  28.86  4157     27.22   28.69   1276    11.31  14.72  7716

Paper: CB 22 (+-2.2), VNC 38 (+-3.8), MY 11 (+-1.1) spikes/s
                                      rate             medulla  all within
                       (a) avg_firing_rate     (i) MY with VNC       False
                       (a) avg_firing_rate (ii) MY without VNC       False
(b) spikes in the first 5 s of good trials     (i) MY with VNC       False
(b) spikes in the first 5 s of good trials (ii) MY without VNC       False

CB mean rate with the arbor vitae included, reading (a): 21.67

#### 22 ['claim:fig1d-lick-breath-frequencies']
              reading  lick mean  lick sd  lick 2.5%  lick 97.5%  breath mean  breath sd  breath 2.5%  breath 97.5%  n licks  n breaths
    (a) within trials      26.96    38.48       1.11      147.06         3.89       1.15         2.10          6.68   875899     924221
(b) within lick bouts       8.06    14.92       3.50       13.37         4.15       1.01         2.37          6.39   360464     175918
[... 174 more lines not kept]
```

**Agent calls Bash**

```bash
F=/home/runner/.claude/projects/-home-runner-work-encore-encore/bff38b74-0a40-431b-a973-ca03f9cbd0c8/tool-results/bl8nnffrh.txt; sed -n '420,600p' $F | grep -v "simultaneous" | head -150; date -u
```

```
V4(b) PSTH peak    order 2, b (a) sessions with a swallow          (ii) not lick  18494           261               102                  62            363  False
         V4(b) 
#### 48 ['claim:fig2f-breathing-units-location']
AMB from 87 labelled units (all qualities): AP (np.float64(11460.0), np.float64(12420.0)), |ML| (np.float64(1320.0), np.float64(1500.0)), DV (np.float64(6480.0), np.float64(6760.0)) um
IRN from 19432 labelled units: AP midpoint 11790.0, DV midpoint 6130.0 um
d = 300 um: units near preBotC 16, above AMB 59, lateral of NTS 1940
d = 500 um: units near preBotC 16, above AMB 94, lateral of NTS 2830
posterior-ventral IRN: 470 ; posterior-dorsal IRN/PARN: 691 ; pons and medulla: 12013
       tuning                region   n  tuned  fraction  base fraction      p
   order 4, a      preBotC (300 um)  16      6    0.3750         0.0663 0.0004
   order 4, a      preBotC (500 um)  16      6    0.3750         0.0663 0.0004
   order 4, a posterior ventral IRN 470     85    0.1809         0.0663 0.0000
   order 4, b      preBotC (300 um)  16      5    0.3125         0.0444 0.0005
   order 4, b      preBotC (500 um)  16      5    0.3125         0.0444 0.0005
   order 4, b posterior ventral IRN 470     70    0.1489         0.0444 0.0000
   order 2, a      preBotC (300 um)  16      5    0.3125         0.0669 0.0032
   order 2, a      preBotC (500 um)  16      5    0.3125         0.0669 0.0032
   order 2, a posterior ventral IRN 470     88    0.1872         0.0669 0.0000
   order 2, b      preBotC (300 um)  16      5    0.3125         0.0443 0.0005
   order 2, b      preBotC (500 um)  16      5    0.3125         0.0443 0.0005
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
F=/home/runner/.claude/projects/-home-runner-work-encore-encore/bff38b74-0a40-431b-a973-ca03f9cbd0c8/tool-results/bl8nnffrh.txt; sed -n '542,575p' $F | grep "simultaneous"; sed -n '46,56p' $F; sed -n '/#### 46/,/#### 48/p' $F | grep "order 5, code" | head -3
```

```
fig4e licking units (a) MI > 0.6, P < 0.001   a (b) simultaneous, 300 um      9  86.6667 0.031         5         0
  fig4e licking units (a) MI > 0.6, P < 0.001   a (b) simultaneous, 500 um      9  86.6667 0.031         5         0
fig4f breathing units (a) MI > 0.6, P < 0.001   a (b) simultaneous, 300 um      1  20.0000   NaN         1         0
fig4f breathing units (a) MI > 0.6, P < 0.001   a (b) simultaneous, 500 um      1  20.0000   NaN         1         0
  fig4e licking units (a) MI > 0.6, P < 0.001   b (b) simultaneous, 300 um      2 210.0000   NaN         2         0
  fig4e licking units (a) MI > 0.6, P < 0.001   b (b) simultaneous, 500 um      2 210.0000   NaN         2         0
fig4f breathing units (a) MI > 0.6, P < 0.001   b (b) simultaneous, 300 um      1  20.0000   NaN         1         0
fig4f breathing units (a) MI > 0.6, P < 0.001   b (b) simultaneous, 500 um      1  20.0000   NaN         1         0
  fig4e licking units (b) MI > 0.9, P < 0.001   a (b) simultaneous, 300 um      2 210.0000   NaN         2         0
  fig4e licking units (b) MI > 0.9, P < 0.001   a (b) simultaneous, 500 um      2 210.0000   NaN         2         0
fig4f breathing units (b) MI > 0.9, P < 0.001   a (b) simultaneous, 300 um      1  20.0000   NaN         1         0
fig4f breathing units (b) MI > 0.9, P < 0.001   a (b) simultaneous, 500 um      1  20.0000   NaN         1         0
  fig4e licking units (b) MI > 0.9, P < 0.001   b (b) simultaneous, 300 um      2 210.0000   NaN         2         0
  fig4e licking units (b) MI > 0.9, P < 0.001   b (b) simultaneous, 500 um      2 210.0000   NaN         2         0
fig4f breathing units (b) MI > 0.9, P < 0.001   b (b) simultaneous, 300 um      1  20.0000   NaN         1         0
fig4f breathing units (b) MI > 0.9, P < 0.001   b (b) simultaneous, 500 um      1  20.0000   NaN         1         0
  fig4e licking units      (c) MI > 0.9 alone NaN (b) simultaneous, 300 um      2 210.0000   NaN         2         0
  fig4e licki
[... 17 more lines not kept]
```

**Agent**

Results are in. Before writing conclusions, listing every claim id so each gets one outcome.

**Agent calls Bash**

```bash
grep -n "^- id:" claims/001619/*.yaml | awk '{print $3}' | tr '\n' ' '; echo; grep -c "^- id:" claims/001619/*.yaml; ls questions | head -3; python -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s['properties']['outcomes']['items']['properties'],indent=0)[:3000]); print(s['properties'].keys()); print(json.dumps(s['properties']['findings'],indent=0)[:1500])"
```

```
code-dataset-link fig1d-lick-breath-frequencies fig1f-inspiration-between-licks fig1g-lick-delayed-before-slow-breath fig1f-licking-mode-switch fig1i-breath-delayed-before-slow-lick ed1-unidirectional-models-fail ed2-rats-similar ed1bc-licks-pause-at-swallows fig1k-rhythms-follow-swallow-at-fixed-latency fig1l-lick-interval-preserved fig1l-lick-cycle-prolonged fig1n-breath-interval-preserved fig1n-breath-cycle-prolonged units-count region-spike-rates fig2-licking-breathing-tuned-counts fig2-swallow-modulated-counts fig2f-breathing-units-location fig2g-licking-units-location fig2h-swallow-units-location ed6e-swallow-latencies ed7-glm-separate-clusters ed7g-cae-better-than-features ed7h-prebotc-exception ed8bc-prebotc-inspiration-phase ed8e-licking-units-protrusion ed8i-ipsilateral-lick-selectivity ed4c-licking-map-insensitive-to-sorting fig3a-premotor-regions fig3b-licking-units-in-premotor-regions fig3ce-descending-stimulation-rhythmic-licking fig3dfh-projections-and-rhythm-site ed10-site-classes fig4b-artificial-licking-keeps-lick-timing fig4c-artificial-licking-breath-timing ed11b-alm-breathing-rate fig4e-licking-units-anticipate-breath fig4f-breathing-units-anticipate-lick fig4d-simultaneous-recordings fig4g-licking-breathing-pairs-correlated fig4g-symmetric-lags ed12c-correlation-without-licking fig4h-fewer-correlations-outside-oscillator fig5b-voluntary-lick-latency fig5c-preemptive-breath-adjustment fig5e-photostim-lick-latency-longer fig5f-artificial-licking-late-breath-adjustment 
48
000005.yaml
000006.yaml
000008.yaml
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
[... 125 more lines not kept]
```

**Agent**

Writing the conclusions into the notebook (source and executed copy, markdown only).

**Agent calls Bash**

```bash
cat > $TMPDIR/concl.py <<'EOF'
C = {}
C["**Result: see the table.** The conclusion is in the summary and the record; the means of each reading\nare printed above against the paper's values."] = """**Result: partially reproduced.** Cerebellum and medulla match: 21.3 spikes/s in the cerebellum and
10.9 in the medulla without the vestibular nuclei (reading (a); 21.4 and 11.3 under (b)), against 22 and
11. The vestibular nuclei fire at 27.2 spikes/s under both rate readings, outside 38 +- 3.8, though
still faster than the medulla. With the vestibular nuclei counted in the medulla (i), the medulla mean
is 13.2 to 13.6, outside tolerance."""
C["**Result: FIG1D**"] = """**Result: not reproduced.** Breathing matches under reading (a): 3.89 Hz (95% range 2.10 to 6.68 Hz)
against 4.02 (2.12 to 7.17). Licking does not under either reading: the mean of the inverse intervals
between tongue onsets is 26.96 Hz within trials and 8.06 Hz within bouts, against 6.23, because the
code's tongue onsets include onsets a few milliseconds apart (97.5th percentiles 147 and 13.4 Hz). The
per-session median lick frequency within bouts is 6.13 Hz (5th to 95th percentile over sessions 5.16 to
6.54), close to the paper's mean, but the criterion's measure is the pooled mean."""
C["**Result: FIG1F**"] = """**Result: not reproduced.** 30.4% of in-bout inspiration onsets (70,298 of 231,563) fall between a
tongue onset and the following tongue offset, above the 5% of reading (b); every session has some
(3.3% to 46.1% per session). Both readings fail. The latency from the last lick of a cycle to the next
inspiration has a median of 133 ms after one lick and 92 ms after two (pooled)."""
C["**Result: FIG1G**"] = """**Result: partially reproduced.** Over the 71 sessions with enough two-lick cycles and a peak in
each window, the second lick is later before a slow breath by 22.0 ms on average (t = 3.68, p =
4.5e-4, reading (a)); over the 20 mice the mean is 13.6 ms (p = 0.18, reading (b)). 16 of the 20 mice
have a positive mean, one zero and three negative, so not every mouse is positive. 102 of 173 sessions
give no value (fewer than 40 cycles in a half, or no peak)."""
C["**Result: FIG1FMODE**"] = """**Result: partially reproduced.** The median inter-breath interval rises from 1 to 2 to 3 licks per
cycle in 116 of 117 sessions (medians over sessions 0.228, 0.296 and 0.418 s), so licks are added as
breathing slows. The latency from the last lick to the next inspiration is not fixed by the criterion's
20% rule: pooled medians are 133, 92 and 82 ms for 1, 2 and 3 licks (62.5% apart), and only 1 of 117
sessions keeps them within 20%."""
C["**Result: FIG1I**"] = """**Result: reproduced.** Over 86 sessions the inspiration after a lick is later before a slow lick by
10.5 ms on average (t = 6.79, p = 1.5e-9, reading (a)); over 23 mice 9.6 ms (p = 0.0012, reading (b)).
44 sessions are positive, 37 zero and 5 negative."""
C["**Result: ED1**"] = """**Result: reproduced.** With the data's interval distributions and latencies (112 ms last lick to
inspiration, 119 ms inspiration to next lick), the breathing-driven model gives a Fig 1i difference of
0.0 ms in all 162 simulated sessions with a value (no effect), and the licking-driven model gives a Fig
1g value in only 2 sessions (no second-lick peak in the windows), so it does not produce the Fig 1g
effect; the data give both differences positive (22.0 and 10.5 ms, p < 0.001). Each model does produce
the other relation (breathing-driven Fig 1g 48.4 ms; licking-driven Fig 1i 33.7 ms), as one oscillator
setting the other's timing would."""
C["**Result: ED1BC**"] = """**Result: not reproduced.** In 90 sessions with at least 20 swallows, the probability of a tongue
onset per 3.4 ms bin in the 100 ms after swallow onset is higher than after in-bout expiration onsets
(mean 0.0308 against 0.0211; lower around swallows in 4 of 90 sessions; Wilcoxon p = 4.0e-16). The
code's swallow detector requires a lick within 0.25 s after the detected peak, which may favour licks
after swallow onset; the expiration onset is a choice named in the claims file."""
C["**Result: FIG1K**"] = """**Result: reproduced.** For licks and for breaths, under both rankings, the median latency from
swallow onset to the next event differs less between the top and bottom thirds (licks 17.0 ms;
breaths 37.4 and 23.8 ms) than their median cycle -1 does (licks 27.2 and 40.8 ms; breaths 95.2 and
122.4 ms)."""
C["**Result: FIG1L**"] = """**Result: fig1l-lick-cycle-prolonged reproduced; fig1l-lick-interval-preserved not reproduced.** On
the code's selection (reading (a), 1,932 events), the lick cycle spanning the swallow is longer than
the cycle before by 33.36 ms (p < 1e-300), against 33.3 ms. The cycle after the swallow is also longer
than the one before, by 117.9 ms (p < 1e-300), so the paper's test finds the effect the claim says is
absent; readings (b) to (d) give 86.3 to 86.6 ms and 50.3 ms, all p < 0.001."""
C["**Result: FIG1N**"] = """**Result: both reproduced.** On the code's selection (2,100 events), the breath cycle spanning the
swallow is longer than the cycle before by 48.13 ms (p < 1e-300), against 48.0 ms, and the cycle after
differs from the one before by -1.8 ms (p = 0.26), so the test does not find a change. Reading (c)
agrees (-0.9 ms, p = 0.26); readings (b) and (d) find a difference (-25.3 ms, p < 0.001; -6.1 ms, p =
0.018)."""
C["**Result: FIG2COUNTS**"] = """**Result: partially reproduced.** Under significance reading V3(a) (the Methods' rank-sum test of
resampled MIs, as the code runs it) the counts match for both filter readings: 3,517 licking, 1,021
breathing and 177 both (order 4), and 3,584, 1,030 and 193 (order 2), against 3,551, 1,015 and 182,
when the licking and breathing counts include the units tuned to both (i). The code's 100-resample
scheme gives the same. Under reading V3(b) (measured MI ranked against random-phase MIs) the counts are
2,757, 602 and 69 (order 4), outside tolerance. The criterion asks for every reading, so the counts do
not hold; both-tuned units are 2.5% to 5.4% of licking units and 11.5% to 18.7% of breathing units under
every reading, which meets the partial rule."""
C["**Result: FIG2SW**"] = """**Result: not reproduced.** Reading (a) of the denominator matches: 18,494 units in sessions with a
detected swallow, against 18,485. The swallow-modulated counts do not under any combination: with V4(a)
264 swallow-only (319 under (ii)), 207 licking and swallowing, and 87 breathing and swallowing (order 4,
V3(a)), against 427, 175 and 55; V4(b) gives fewer swallow-only units (187 to 264)."""
C["**Result: FIG2F**"] = """**Result: reproduced.** Breathing-tuned units are enriched near the preBotzinger complex (5 or 6 of
16 units, 31% to 38%, against 4.4% to 6.7% of pons and medulla units, p = 0.0004 to 0.0032) and in
posterior ventral IRN (70 to 88 of 470, p < 1e-10) under every reading of tuning and distance. Only 16
units fall in the preBotzinger box built from the AMB-labelled units, the same for 300 and 500 um."""
C["**Result: FIG2G**"] = """**Result: reproduced.** Licking-tuned units are enriched in XII (36% to 45% of 166 units), V (43%
to 55% of 269) and IRN (34% to 40% of 1,804), against 20% to 26% of pons and medulla units (p < 1e-10
in each, every reading), and make up 15% to 20% of pons units, above 1%."""
C["**Result: FIG2H**"] = """**Result: partially reproduced.** Under V4(a), the code's normalisation, swallow-modulated units are
enriched in V (5.6%, p = 0.018), IC (10.9%) and NLL (10.1%, p < 1e-5) against 2.8% in the same sessions,
for both distances, but not lateral of NTS (2.5%, p = 0.84 and 0.88) or above AMB (5.4% and 3.8%, p =
0.21 and 0.38): three of five regions. Under V4(b) only IC and NLL are enriched (two of five). The
outcome rests on adopting V4(a)."""
C["**Result: ED6E**"] = """**Result: reproduced.** The swallow PSTH of modulated units peaks before swallow onset in V and IRN
(median -1 ms, 111 units, V4(a); -4 ms, 68 units, V4(b)) and after it in IC and NLL (median +16 ms, 53
and 45 units), and the groups differ (Mann-Whitney p < 1e-6 under both readings). The lead in IRN is
small (median -1 ms under V4(a), 98 units); in V it is -11 ms (13 units)."""
C["**Result: ED8BC**"] = """**Result: not reproduced.** Only 4 or 5 breathing units with MI > 0.9 lie near the preBotzinger
complex under any reading, and 2 of them prefer the inspiration half (40% to 50%; Rayleigh p 0.13 to
0.22). Over all 265 such units, 40.8% prefer the inspiration half."""
C["**Result: ED8E**"] = """**Result: reproduced.** 70.4% to 70.5% of licking units with MI > 0.9 (634 to 651 of 899 to 925)
prefer a jaw phase within pi/2 of their session's median phase at full tongue protrusion, under every
reading."""
C["**Result: ED4C**"] = """**Result: reproduced.** 2,366 good units have amplitude above 500 uV (2,223 +- 222), and over the 30
regions with at least 20 of them, their mean licking MI per region correlates with that of all units
(Spearman rho 0.94 to 0.95, p < 1e-10, for each filter order)."""
C["**Result: FIG4EF**"] = """**Result: both reproduced, resting on reading O2(a).** Over all sessions, licking units fire later
before a slow breath (mean 54.5 to 60.7 ms; 211 to 660 positive against 14 to 40 negative; p < 1e-10)
and breathing units later before a slow lick (mean 33.0 to 33.4 ms; 40 to 61 positive against 1
negative; p < 1e-10), under every reading of O1. Under O2(b), the simultaneous recordings, only 1 or 2
units remain in most readings and no test can be run; with O1(a) and V3(a), 9 licking units give 86.7 ms
(p = 0.031). Every mean under every reading is positive."""
C["**Result: FIG4D**"] = """**Result: not reproduced.** With the claims file's definitions (O1 and O3), only 1 or 2 two-probe
sessions have licking units in posterior-dorsal IRN/PARN on one probe and breathing units near the
preBotzinger complex on the other, in 1 or 2 mice, against 43 recordings in 21 mice. The dandiset has
162 two-probe sessions in 31 mice; the preBotzinger box built from the AMB units holds only 16 units."""
s_clock_old = """Phase tuning to the jaw and to breathing is present with the true pairing and falls sharply when spikes
are paired with the next trial's tracking or airflow, in every subject with tuned units (table above).
Spikes, tracking and airflow therefore share the trial clock. This shows alignment within trials; the
trials themselves cannot be placed on one session clock, since every trial starts at 0."""
s_clock_new = """Jaw phase tuning is present with the true pairing (3,476 units above MI 0.6, median 0.80) and falls
when spikes are paired with the next trial's tracking (median 0.13, 308 units above 0.6), in every
subject. Breathing tuning falls likewise overall (950 units, median 0.74, against 0.16 and 313 units),
but in four subjects (DL004, DL005, DL010, DL020) the shifted pairing gives as many units above 0.6 as
the true one (5 against 7, 7 against 9, 14 against 14, 3 against 6), so for their airflow the shared
clock is not established. Elsewhere spikes, tracking and airflow are consistent with one trial clock.
This concerns alignment within trials; the trials cannot be placed on one session clock, since every
trial starts at 0."""
C[s_clock_old] = s_clock_new
EOF
cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import sys; sys.path.insert(0,'/tmp/claude-1001')
from concl import C
s=open('/tmp/claude-1001/cells.py').read()
for k,v in C.items():
    assert k in s, k[:40]
    s=s.replace(k,v)
open('/tmp/claude-1001/cells.py','w').write(s)
print('ok')
EOF
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='/tmp/claude-1001/cells.py'
s=open(p).read()
rep=[("(p < 1e-300), against 33.3 ms","(p < 0.0001), against 33.3 ms"),("by 117.9 ms (p < 1e-300)","by 117.9 ms (p < 0.0001)"),
("by 48.13 ms (p < 1e-300)","by 48.13 ms (p < 0.0001)"),("posterior ventral IRN (70 to 88 of 470, p < 1e-10)","posterior ventral IRN (70 to 88 of 470, p < 0.0001)"),
("against 20% to 26% of pons and medulla units (p < 1e-10\nin each, every reading)","against 20% to 26% of pons and medulla units (p < 0.00001\nin each, every reading)"),
("IC (10.9%) and NLL (10.1%, p < 1e-5)","IC (10.9%) and NLL (10.1%; both p < 0.0001)"),
("groups differ (Mann-Whitney p < 1e-6 under both readings)","groups differ (Mann-Whitney p < 0.0001 under both readings)"),
("(Spearman rho 0.94 to 0.95, p < 1e-10, for each filter order)","(Spearman rho 0.94 to 0.95, p < 0.00001, for each filter order)"),
("negative; p < 1e-10)\nand","negative; p < 0.001)\nand"),("negative; p < 1e-10). Under","negative; p < 0.001). Under")]
for a,b in rep:
    if a not in s: print('MISSING',a[:50])
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
grep -n "1e-" $TMPDIR/cells.py | grep -v "print\|f\"" | head
```

```
MISSING negative; p < 1e-10). Under
586:bins = np.arange(-0.3, 0.3 + 1e-9, kaku.FRAME_S)
1048:negative; p < 1e-10), under every reading of O1. Under O2(b), the simultaneous recordings, only 1 or 2
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i '1048s/negative; p < 1e-10), under/negative; p < 0.001), under/' cells.py && sed -n 1040,1052p cells.py | grep -c "1e-10"; date -u
```

```
0
Thu Nov  5 10:13:26 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='/tmp/claude-1001/cells.py'
s=open(p).read()
old=s[s.index("**Result: partially reproduced.** The total (20,109"):s.index("''')", s.index("**Result: partially reproduced.** The total (20,109"))]
new="""**Result: partially reproduced.** The total (20,109 by the code's filter) and the mean per probe (60.0)
are within tolerance, and there are 31 mice, but the dandiset holds 335 insertions, not 339, and the
pons (3,021) and medulla (8,992) counts are below the paper's. The cerebellum holds 4,157 units, or
5,385 with the arbor vitae (within tolerance of 5,700). 2,711 good units lie outside these regions
(midbrain, fibre tracts and others). The spread per probe is 32.9 where the paper gives 22.
"""
s=s.replace(old,new)
s += r'''

md(r"""
## Summary

| Claim | Outcome |
|---|---|
| code-dataset-link | reproduced |
| units-count | partially reproduced |
| region-spike-rates | partially reproduced |
| fig1d-lick-breath-frequencies | not reproduced |
| fig1f-inspiration-between-licks | not reproduced |
| fig1g-lick-delayed-before-slow-breath | partially reproduced |
| fig1f-licking-mode-switch | partially reproduced |
| fig1i-breath-delayed-before-slow-lick | reproduced |
| ed1-unidirectional-models-fail | reproduced |
| ed1bc-licks-pause-at-swallows | not reproduced |
| fig1k-rhythms-follow-swallow-at-fixed-latency | reproduced |
| fig1l-lick-interval-preserved | not reproduced |
| fig1l-lick-cycle-prolonged | reproduced |
| fig1n-breath-interval-preserved | reproduced |
| fig1n-breath-cycle-prolonged | reproduced |
| fig2-licking-breathing-tuned-counts | partially reproduced |
| fig2-swallow-modulated-counts | not reproduced |
| fig2f-breathing-units-location | reproduced |
| fig2g-licking-units-location | reproduced |
| fig2h-swallow-units-location | partially reproduced (assumed) |
| ed6e-swallow-latencies | reproduced |
| ed8bc-prebotc-inspiration-phase | not reproduced |
| ed8e-licking-units-protrusion | reproduced |
| ed4c-licking-map-insensitive-to-sorting | reproduced |
| fig4e-licking-units-anticipate-breath | reproduced (assumed) |
| fig4f-breathing-units-anticipate-lick | reproduced (assumed) |
| fig4d-simultaneous-recordings | not reproduced |
| ed8i-ipsilateral-lick-selectivity | blocked: metadata insufficient |
| ed7-glm-separate-clusters | blocked: too large |
| ed7g, ed7h (autoencoder) | blocked: data missing |
| fig4g (two), fig4h | blocked: other (too few recordings under the claims' selection) |
| ed12c, ed2, fig3b, fig3ce, fig3dfh, ed10, fig4b, fig4c, ed11b, fig5b, fig5c, fig5e, fig5f | blocked: data missing |
| fig3a | blocked: other (no pinned source for the premotor neurons) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

**How the analysis differs from the paper's.** The paper's code (process_mat.py) is ported to the
streamed NWB files and its choices are kept. The tuning curves of the 1000 resamples per unit are fitted
by a grid search where the code uses curve_fit (the measured MI uses curve_fit; on 300 random units the
two agree to a median of 0.0015 in MI, and on 24 tuned units the code's own significance scheme gives
the same decision with either fit). Regions the CCF does not label (the preBotzinger complex, the
dorsal and ventral parts of IRN, the areas next to AMB and NTS) are built from the positions of the units
the files label, so they are approximations; the preBotzinger box holds only 16 units, which bears on
fig2f, ed8bc, fig4d and the simultaneous-recording readings of fig4e and fig4f. Where the claims file names
several readings, all are shown above.

**What was found about the dataset.** The spike index of every file holds start offsets, not end
offsets, so standard NWB readers misassign spikes; 19 files have more histology rows than units; the
behaviour of both probes of a session is the same recording deposited twice; trials carry no session
times; the age field (P2xxW) and the `photostim` stimulus field do not fit the data; the `left`/`right`
location text disagrees with the side `ccf_x` gives; the 3D tracking has no stated axes. The cued
licking task, the photostimulation experiments, the rat recordings and the raw videos are not in the
dandiset, and it holds 335 insertions where the paper reports 339.
""")
'''
open(p,'w').write(s)
EOF
cd $TMPDIR && . env/bin/activate && python build_nb.py && python - <<'EOF'
import nbformat
src=nbformat.read('entries/001619-kaku-2025/reproduce_kaku_2025.ipynb',4)
ex=nbformat.read('executed/001619-kaku-2025/reproduce_kaku_2025.ipynb',4)
print(len(src.cells),len(ex.cells))
for i,c in enumerate(src.cells):
    if i < len(ex.cells):
        assert ex.cells[i].cell_type==c.cell_type
        if c.cell_type=='code': assert ex.cells[i].source==c.source, i
        else: ex.cells[i].source=c.source
    else:
        assert c.cell_type=='markdown'; ex.cells.append(c)
nbformat.write(ex,'executed/001619-kaku-2025/reproduce_kaku_2025.ipynb')
print('patched')
EOF
cd  && python tools/entry.py check entries/001619-kaku-2025
```

```
68
68 67
patched
0 error(s)
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
print(json.dumps(s['properties']['provenance'],indent=0)[:2500]); print(json.dumps(s['properties']['inputs'],indent=0)[:800]); print(s.get('required')); print(json.dumps(s['properties']['dataset'],indent=0)[:800])"
```

```
{
"type": "object",
"additionalProperties": false,
"required": [
"kind",
"accountable"
],
"properties": {
"kind": {
"enum": [
"agent",
"person"
]
},
"accountable": {
"description": "The person or organisation responsible for this attempt.",
"type": "object",
"additionalProperties": false,
"required": [
"name"
[... 109 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR && cat > $TMPDIR/attempt.py <<'PYEOF'
import yaml
NB = "reproduce_kaku_2025.ipynb"
def o(claim, outcome, notes, tag=None, deviations=None, measured=None, blocked_by=None, assumed=None):
    d = {"claim": claim, "outcome": outcome}
    if blocked_by: d["blocked_by"] = blocked_by
    if outcome != "blocked" or tag:
        d["notebook"] = NB
        d["output"] = f"claim:{tag or claim}"
    if measured is not None: d["measured"] = measured
    if assumed: d["assumed"] = True
    d["notes"] = notes
    if deviations: d["deviations"] = deviations
    return d

PORT = ("The paper's code (process_mat.py, generate_figures.py, at commit fbc0abe) was ported to the streamed NWB files; "
        "its trials are the first 1471 frames of each good trial placed end to end, as in the code.")
O = []
O.append(o("code-dataset-link", "reproduced",
    "Every input of process_mat.py is in the files (spike times per trial with the per-trial counts, the six quality metrics, CCF "
    "coordinates and region names, the 25 kHz airflow with timestamps and per-trial sample counts, side and bottom DLC jaw, tongue "
    "and lickport with likelihoods, 3D jaw, tongue and lickport tracks). get_good_units keeps 20,109 units over the 335 files, 0.9% "
    "below 20,300; with the Methods' drift metric added, 16,957 (16.5% below). All 173 sessions ran through the code's steps. "
    "The spike index must be read as start offsets (finding).",
    deviations=["The files are read directly; the code's nwb2mat converter (a Windows MATLAB executable) was not used."]))
O.append(o("units-count", "partially_reproduced",
    "Code filter 20,109 units (tolerance 18,270 to 22,330), 60.0 per probe (SD 32.9 against 22), 31 mice; 335 insertions, not 339. "
    "Cerebellum 4,157 (5,385 with the arbor vitae, within tolerance), pons 3,021 and medulla 8,992, both below tolerance; "
    "2,711 good units lie outside these regions. With the drift metric 16,957 units (CB 3,292, P 2,698, MY 7,626).",
    measured=[20109, 60.0, 4157, 3021, 8992, 335, 31],
    deviations=["Regions are taken from the Allen structure tree (iblatlas copy, pinned) by the unit's region name; whether the "
                "paper counts the arbor vitae as cerebellum is not stated, and both counts are shown."]))
O.append(o("region-spike-rates", "partially_reproduced",
    "Reading (a), avg_firing_rate: cerebellum 21.3 +- 28.8 (n 4,157), vestibular nuclei 27.2 +- 28.8 (n 1,276), medulla without "
    "VNC 10.9 +- 14.5 (n 7,716), with VNC 13.2. Reading (b), spikes in the first 5 s of good trials: 21.4, 27.2, 11.3 and 13.6. "
    "Cerebellum and medulla (ii) are within tolerance; the vestibular nuclei are not (38 +- 3.8) under any reading, though they still "
    "fire faster than the medulla.",
    measured=[21.26, 27.24, 10.91],
    deviations=["Reading (b) uses spikes in the code's analysis window (the first 5.0014 s of each good trial) over that time, "
                "since the trials carry no session times."]))
O.append(o("fig1d-lick-breath-frequencies", "not_reproduced",
    "Reading (a), within trials: licking 26.96 +- 38.48 Hz (95% range 1.11 to 147.06), breathing 3.89 +- 1.15 Hz (2.10 to 6.68). "
    "Reading (b), within bouts: licking 8.06 +- 14.92 Hz (3.50 to 13.37), breathing 4.15 +- 1.01 Hz (2.37 to 6.39). Breathing is "
    "within tolerance on all three values under (a); the licking mean is outside under both readings. The code's tongue onsets "
    "include onsets a few milliseconds apart (tongue detection flickering between frames), which inflate the mean of inverse "
    "intervals. The per-session median lick frequency within bouts is 6.13 Hz (5th to 95th percentile over sessions 5.16 to 6.54).",
    measured=[8.06, 3.89, 3.50, 13.37, 2.10, 6.68],
    deviations=["measured gives licking under reading (b) and breathing under reading (a), the readings closest to the paper's "
                "values for each; no single reading matches all six."]))
O.append(o("fig1f-inspiration-between-licks", "not_reproduced",
    "70,298 of 231,563 in-bout inspiration onsets (30.4%) fall between a tongue onset and the next tongue offset; per session 3.3% "
    "to 46.1% (median 30.0%); no session has none, so readings (a) and (b) both fail. Tongue onsets are rarer just before an "
    "inspiration and most frequent about 110 ms before it (not printed in the notebook beyond the latency table). The median latency "
    "from the last lick in a cycle to the next inspiration is 133 ms (1 lick), 92 ms (2), 82 ms (3) and 109 ms (4).",
    deviations=["A protrusion is taken from each tongue onset to the first tongue offset after it, both as the code detects them "
                "(likelihood > 0.95 in both views); the paper does not define the interval."]))
O.append(o("fig1g-lick-delayed-before-slow-breath", "partially_reproduced",
    "71 of 173 sessions give a value (83 have at least 40 two-lick cycles per half; the others lack a peak in a window). "
    "Reading (a), sessions: mean 22.0 ms, t = 3.68, p = 4.5e-4. Reading (b), mice: mean 13.6 ms, p = 0.18 (n = 20). 16 of 20 mice "
    "have a positive mean, 1 zero and 3 negative (DL008 -120 ms from one session, DL011 -50, DL027 -33). 60 sessions are positive, "
    "6 zero, 5 negative.",
    measured=0.022))
O.append(o("fig1f-licking-mode-switch", "partially_reproduced",
    "The median inter-breath interval rises from 1 to 2 to 3 licks per cycle in 116 of 117 sessions that have all three (median "
    "session medians 0.228, 0.296, 0.418 s; 4 licks 0.558 s), so licks are added as breathing slows. The latency from the last "
    "lick to the next inspiration differs by 62.5% between the groups (pooled medians 133, 92 and 82 ms), and only 1 of 117 sessions "
    "keeps it within 20%, so the fixed-latency part of the criterion fails."))
O.append(o("fig1i-breath-delayed-before-slow-lick", "reproduced",
    "86 sessions give a value. Reading (a): mean 10.5 ms, t = 6.79, p = 1.5e-9; reading (b), 23 mice: 9.6 ms, p = 0.0012. "
    "44 sessions positive, 37 zero (the PSTH bins are 20 ms), 5 negative; 18 of 23 mice positive.",
    measured=0.0105))
O.append(o("ed1-unidirectional-models-fail", "reproduced",
    "Inter-breath intervals from fig1d reading (a), inter-lick intervals from reading (b); ranges 0.150 to 0.476 s and 0.075 to "
    "0.286 s (2.5th to 97.5th percentiles); latencies 112 ms (last lick to inspiration) and 119 ms (inspiration to next lick). "
    "Breathing-driven model: Fig 1i difference 0.0 ms in all 162 simulated sessions with a value (no variance, so no test). "
    "Licking-driven model: a Fig 1g value in only 2 sessions (no second-lick peak in the code's windows otherwise), so no positive "
    "significant effect. Data: 22.0 and 10.5 ms, both p < 0.001. The breathing-driven model does give a Fig 1g effect (48.4 ms, "
    "p = 6e-19, 31 sessions) and the licking-driven model a Fig 1i effect (33.7 ms, 169 sessions), each producing one direction only.",
    deviations=["Simulated sessions match the data sessions in the number of in-bout inspirations (breathing model) or licks "
                "(licking model); sessions with fewer than 50 in-bout inspirations are skipped.",
                "Licks are added evenly inside inter-lick intervals longer than the 97.5th percentile (breathing model), and an "
                "inspiration is omitted when it would follow the previous one by less than the 2.5th percentile inter-breath "
                "interval (licking model); the Methods describe both steps without numbers."]))
O.append(o("ed2-rats-similar", "blocked", "The rat lickometer and thermocouple recordings are not in the dandiset, and the paper "
    "names no deposit for them.", blocked_by="data_missing"))
O.append(o("ed1bc-licks-pause-at-swallows", "not_reproduced",
    "90 sessions with at least 20 swallows. Tongue-onset probability per 3.4 ms bin, 0 to 100 ms after onset: 0.0308 around "
    "swallows against 0.0211 around in-bout expiration onsets (median ratio 1.50); lower around swallows in 4 of 90 sessions; "
    "Wilcoxon p = 4.0e-16 in the opposite direction. The code's detector keeps swallows with a lick within 0.25 s after the "
    "detected peak, which may favour licks after the onset.",
    deviations=["Expiration onset is the Hilbert phase (code filter, plus pi) wrapping through 2 pi, the claims file's choice."]))
O.append(o("fig1k-rhythms-follow-swallow-at-fixed-latency", "reproduced",
    "6,644 swallow events; 5,797 kept for licks, 6,300 for breaths (code selection). Licks: latency difference between top and "
    "bottom thirds 17.0 ms against cycle -1 differences of 27.2 (ranking O5 a) and 40.8 ms (b). Breaths: 37.4 and 23.8 ms against "
    "95.2 and 122.4 ms."))
O.append(o("fig1l-lick-interval-preserved", "not_reproduced",
    "Code selection (O5 a, 1,932 events): Delta(1,-1) = 117.9 ms, one-sample t-test p < 0.0001, so the paper's test finds a "
    "change. Variants: (b) 86.6 ms, (c) 50.3 ms (5,797 events), (d) 86.3 ms over 140 sessions, all p < 0.0001.",
    tag="fig1l-lick-interval-preserved"))
O.append(o("fig1l-lick-cycle-prolonged", "reproduced",
    "Code selection (O5 a): Delta(0,-1) = 33.36 ms, p < 0.0001, n = 1,932. Other readings: (b) 4.0 ms, (c) 11.0 ms, (d) 38.7 ms, "
    "all p < 0.0001. The selection of the longest cycles 0 favours a positive value, as the claims file notes.",
    measured=33.36))
O.append(o("fig1n-breath-interval-preserved", "reproduced",
    "Code selection (O5 a, 2,100 events): Delta(1,-1) = -1.8 ms, p = 0.26. Variants: (c) -0.9 ms, p = 0.26; (b) -25.3 ms, "
    "p < 0.0001; (d) -6.1 ms, p = 0.018 over 134 sessions."))
O.append(o("fig1n-breath-cycle-prolonged", "reproduced",
    "Code selection (O5 a): Delta(0,-1) = 48.13 ms, p < 0.0001, n = 2,100. (b) 1.4 ms, p = 0.31; (c) 40.5 ms; (d) 72.3 ms.",
    measured=48.13))
O.append(o("fig2-licking-breathing-tuned-counts", "partially_reproduced",
    "Counts with licking and breathing including the units tuned to both (i). V3(a): order 4 3,517 / 1,021 / 177; order 2 3,584 / "
    "1,030 / 193; code order 5 3,500 / 1,026 / 177; all within tolerance of 3,551 / 1,015 / 182. The code's 100-resample scheme "
    "gives the same (3,515 / 1,020 / 177 at order 4). V3(b): order 4 2,757 / 602 / 69, order 2 2,806 / 604 / 70, outside. Under "
    "(ii) no reading matches. As the criterion asks for every reading of V3, the counts do not hold; the partial rule holds under "
    "every reading (both-tuned 2.5% to 5.4% of licking units, 11.5% to 18.7% of breathing units). V3(b) ranks the measured MI "
    "against random-phase MIs, which for noisy units are often as large as the measured one; V3(a) compares resampled-spike MIs with "
    "random-phase MIs, as the Methods' rank-sum test and the code do.",
    measured=[3517, 1021, 177],
    deviations=["The 1000 resampled tuning curves per unit are fitted by a grid search over width and preferred phase with "
                "amplitude and baseline in closed form, not curve_fit; the measured MI uses curve_fit as the code. On 300 random "
                "units the two fits differ by a median of 0.0015 in MI and fall on the same side of 0.6 in 99%; on 24 units with MI "
                "> 0.6 the code's 100-resample test gives the same decision with either fit.",
                "Resampled histograms are drawn as multinomials on the measured histogram's bins, which has the distribution of the "
                "code's resampling; the code's bin edges follow each resample's range.",
                "Significance resamples are computed only for units whose measured MI exceeds 0.6, the only units that can count."]))
O.append(o("fig2-swallow-modulated-counts", "not_reproduced",
    "Denominator reading (a), units of sessions with a swallow: 18,494 (paper 18,485); reading (b), units with at least 20 swallows: "
    "10,807. Swallow-modulated units: 526 under V4(a), 363 under V4(b). V4(a) with order 4, V3(a): swallow only 264 (i) or 319 (ii), "
    "licking and swallowing 207, breathing and swallowing 87; other tuning readings give 262 to 355, 171 to 213 and 65 to 87. "
    "V4(b): 187 to 264, 99 to 127 and 62 to 85. No combination puts the three counts within tolerance of 427, 175 and 55.",
    measured=[18494, 264, 207, 87]))
O.append(o("fig2f-breathing-units-location", "reproduced",
    "Near the preBotzinger complex (both distances give the same 16 units): 5 or 6 breathing-tuned, 31% to 38%, against 4.4% to "
    "6.7% of pons and medulla units, Fisher p 0.0004 to 0.0032. Posterior ventral IRN: 70 to 88 of 470 (15% to 19%), p < 0.0001. "
    "Every reading of tuning (orders 4, 2 and 5; V3 a, b and code) and distance gives the enrichment.",
    deviations=["The preBotzinger box (O3) is built from the extent of the 87 units of any quality that the files label AMB "
                "(AP 11,460 to 12,420 um, 1,320 to 1,500 um from the midline, DV 6,480 to 6,760 um), not from the CCF annotation "
                "volume, which the attempt did not use; it holds 16 good units. IRN midpoints likewise come from IRN-labelled units."]))
O.append(o("fig2g-licking-units-location", "reproduced",
    "Licking-tuned fractions: XII 36% to 45% (166 units), V 43% to 55% (269), IRN 34% to 40% (1,804), against 20% to 26% of pons "
    "and medulla units, Fisher p < 0.00001 in each under every reading; pons 15% to 20% of 3,021 units, above 1%."))
O.append(o("fig2h-swallow-units-location", "partially_reproduced", assumed=True, notes=
    "V4(a): enriched in V (13 of 234, 5.6%, p = 0.018), IC (34 of 313, 10.9%) and NLL (19 of 189, 10.1%) against 2.8% in the same "
    "sessions, for both distances; not lateral of NTS (2.5%, p 0.84 to 0.88) or above AMB (5.4% and 3.8%, p 0.21 and 0.38): "
    "three of five. V4(b): IC and NLL only (two of five), which would be not reproduced. The outcome adopts V4(a), the code's "
    "normalisation (by the larger of the two window rates), which the claims file also reads as the Methods' 'peak spike rate "
    "during swallowing'; the question is put to the authors (findings).",
    deviations=["Assumed: V4(a). The two readings give different outcomes; V4(a) is the code's choice.",
                "'Lateral of NTS' is units beyond the most lateral NTS-labelled unit in each 100 um AP step, within the distance; "
                "'above AMB' uses the AMB box of fig2f. Both are built from labelled units."]))
O.append(o("ed6e-swallow-latencies", "reproduced",
    "Median PSTH peak time (within +-0.15 s) of swallow-modulated units: V and IRN -1 ms (111 units, V4 a) and -4 ms (68, V4 b); "
    "IC and NLL +16 ms (53 and 45 units); Mann-Whitney p < 0.0001 under both. By region (V4 a): V -11 ms (13), IRN -1 ms (98), "
    "IC +13 ms (34), NLL +20 ms (19). The lead of IRN is small."))
O.append(o("ed7-glm-separate-clusters", "blocked", blocked_by="too_large", notes=
    "Not run. The GLM needs one fit per unit (20,109), per lag (11), per link reading (2) and per penalty reading (no penalty and 5 "
    "penalty values chosen on validation), about 2.7 million Poisson GLM fits on tens of thousands of 17 ms bins each; even at 10 ms "
    "per fit that is over 7 hours, beyond the 60-minute limit for a notebook and the time left in this run. No part was run."))
O.append(o("ed7g-cae-better-than-features", "blocked", blocked_by="data_missing", notes=
    "The autoencoder is trained on the raw side and bottom videos, which are not in the dandiset (it holds only the DeepLabCut "
    "tracking); the paper names no video deposit."))
O.append(o("ed7h-prebotc-exception", "blocked", blocked_by="data_missing", notes=
    "Depends on ed7g-cae-better-than-features; the raw videos are not in the dandiset."))
O.append(o("ed8bc-prebotc-inspiration-phase", "not_reproduced",
    "Breathing units with MI > 0.9 near the preBotzinger complex: 5 (4 under the code's order), of which 2 prefer the inspiration "
    "half (40% to 50%), Rayleigh p 0.13 to 0.22, under every reading. Over all 265 such units (order 4, V3 a) 40.8% prefer the "
    "inspiration half. The small number rests on the preBotzinger box built from AMB-labelled units (see fig2f).",
    deviations=["Inspiration onset is phase pi in the tuning phase (Hilbert angle plus pi, as the code), so the inspiration half "
                "is preferred phase minus pi in [0, pi)."]))
O.append(o("ed8e-licking-units-protrusion", "reproduced",
    "Licking units with MI > 0.9: 634 to 651 of 899 to 925 (70.4% to 70.5%) prefer a jaw phase within pi/2 of the session's circular "
    "median phase at full protrusion, under every reading. Session protrusion phases have quartiles 3.26, 3.42 and 3.60 rad."))
O.append(o("ed8i-ipsilateral-lick-selectivity", "blocked", blocked_by="metadata_insufficient", notes=
    "The lick angle needs the left-right axis of the 3D tracking and its sign, and the hemisphere of each unit. The 3D tracking "
    "has no stated axes or units, and the 'left'/'right' text of unit_location puts 99.3% of units on the side opposite to the one "
    "ccf_x gives if it increases to the right, so neither side can be fixed from the files. Per-lick spike counts were computed "
    "but not used."))
O.append(o("ed4c-licking-map-insensitive-to-sorting", "reproduced",
    "2,366 good units above 500 uV (tolerance 2,001 to 2,445). Over 30 regions with at least 20 such units, region mean licking MI "
    "in the subset against all units: Spearman rho 0.944 (order 4), 0.953 (2), 0.948 (5), p < 0.00001. Units above 150 uV with no "
    "other filter number 145,163, so the paper's 19,000 is a count after other filters; it is not resolved here.",
    measured=2366))
O.append(o("fig3a-premotor-regions", "blocked", blocked_by="other", notes=
    "The CCF positions of the masseter and genioglossus premotor neurons come from reference 43 (Takatoh et al. 2021); the paper "
    "gives no archive or identifier for them, and none was looked up in this run, so no pinned source was available to test the "
    "claim."))
O.append(o("fig3b-licking-units-in-premotor-regions", "blocked", blocked_by="data_missing", notes=
    "Needs the premotor neuron positions of reference 43 mapped into the CCF; the paper names no public, pinned copy of them "
    "(Data availability says only that data will be deposited)."))
for c, what in (("fig3ce-descending-stimulation-rhythmic-licking", "The ALM and latSC photostimulation sessions"),
                ("fig3dfh-projections-and-rhythm-site", "The anterograde tracing and the brainstem fibre-site photostimulation data"),
                ("ed10-site-classes", "The brainstem photostimulation sessions"),
                ("fig4b-artificial-licking-keeps-lick-timing", "The cued licking task with ALM photostimulation"),
                ("fig4c-artificial-licking-breath-timing", "The cued licking task with ALM photostimulation"),
                ("ed11b-alm-breathing-rate", "The cued licking task with ALM photostimulation"),
                ("fig5b-voluntary-lick-latency", "The cued licking task (Go cue times)"),
                ("fig5c-preemptive-breath-adjustment", "The cued licking task (Go cue times)"),
                ("fig5e-photostim-lick-latency-longer", "The cued licking task with photostimulation"),
                ("fig5f-artificial-licking-late-breath-adjustment", "The cued licking task with photostimulation")):
    O.append(o(c, "blocked", blocked_by="data_missing", notes=
        f"{what} are not in the dandiset: every file holds the multi-directional licking task, with no cue, photostimulation or "
        "trial-type data (the trial table has only start, stop and duration), and the subjects are all VGAT-ChR2-EYFP mice. "
        "The paper names no other deposit."))
O.append(o("fig4e-licking-units-anticipate-breath", "reproduced", assumed=True, notes=
    "Reading O2(a), all sessions: licking units by O1 (a) with V3(a) 937 units, mean 60.7 ms, 660 positive and 40 negative, "
    "p < 0.001; O1 (a) with V3(b) 808 units, 60.7 ms; O1 (b) and (c) 328 units, 54.5 ms, p < 0.001. Reading O2(b), the "
    "simultaneous recordings: 9 units with O1 (a) and V3(a), 86.7 ms, p = 0.031; 2 units under the other O1 readings (210 ms), "
    "where no test can be run. Every mean is positive. The outcome adopts O2(a), the code's reading (plot_summary loops over all "
    "files), since O2(b) leaves too few units to test in most readings.",
    deviations=["Assumed: reading O2(a) decides where O2(b) cannot be tested; O2(b) rests on the preBotzinger box of fig2f."]))
O.append(o("fig4f-breathing-units-anticipate-lick", "reproduced", assumed=True, notes=
    "Reading O2(a): breathing units by O1 (a) with V3(a) 88 units, mean 33.4 ms, 61 positive and 1 negative, p < 0.001; O1 (a) "
    "with V3(b) 73 units; O1 (b) and (c) 54 units, 33.0 ms, p < 0.001. Reading O2(b): 1 unit (20 ms) under every O1 reading, no "
    "test possible. The outcome adopts O2(a), as for fig4e.",
    deviations=["Assumed: reading O2(a) decides where O2(b) cannot be tested."]))
O.append(o("fig4d-simultaneous-recordings", "not_reproduced",
    "With O1 and O3 as the claims file defines them, 2 recordings in 2 mice (O1 a, V3 a; 2 to 14 licking and 1 to 2 breathing "
    "units) or 1 recording in 1 mouse (the other readings) qualify, against 43 in 21. The dandiset has 162 two-probe sessions in "
    "31 mice. The count rests on the preBotzinger box built from AMB-labelled units (16 good units in it).",
    measured=[2, 2]))
for c in ("fig4g-licking-breathing-pairs-correlated", "fig4g-symmetric-lags", "fig4h-fewer-correlations-outside-oscillator"):
    O.append(o(c, "blocked", blocked_by="other", notes=
        "The pairs come from fig4d-simultaneous-recordings, where the claims file's selection keeps 1 or 2 recordings (at most "
        "28 licking-breathing pairs, against 119) in place of 43; the cross-correlation was not computed. The method (O6) is "
        "reconstructed in the claims file, as the Methods the paper cites do not exist."))
O.append(o("ed12c-correlation-without-licking", "blocked", blocked_by="data_missing", notes=
    "The test uses the baseline of the cued licking task (trial start to Go cue); the dandiset holds no cued-task sessions or Go "
    "cue times."))

findings = [
 ("format_error", "In all 335 files units/spike_times_index holds the offset where each unit's spikes start, not where they end "
  "as NWB requires; standard readers (pynwb) therefore give every unit the spikes of the unit before it. The per-unit, per-trial "
  "spike counts in 'unit and trial pairs' agree with the start-offset reading in every file."),
 ("format_error", "In 19 files the units/histology table (region and CCF position) has more rows than the units (for example "
  "680 against 613 in DL034 session 20220205 probe p2), so its rows cannot be matched to units with certainty; the paper's "
  "code, and this attempt, take them by position."),
 ("metadata_error", "The subject age field reads P210W to P303W (210 to 303 weeks) for every file, which does not fit adult "
  "mice in an acute recording study; the general/stimulus field says 'photostim' in every file, but no file holds "
  "photostimulation or cue data."),
 ("metadata_error", "The 'left'/'right' hemisphere text of unit_location and of the insertion's recordable_brain_regions puts "
  "99.3% of units on the side opposite to the one ccf_x gives if it increases to the right (midline 5,700 um); the files do not "
  "name the CCF axes or their direction, so the side of a unit cannot be fixed."),
 ("metadata_insufficient", "The 3D tracking (jaw_side, tongue_bottom, lickport_bottom) has no stated axes, origin or units, "
  "and the trial tables have no target position, so the lick direction of Extended Data Fig 8 cannot be computed."),
 ("other", "Every trial in the trial tables starts at 0 and spikes, tracking and airflow are stored per trial relative to its "
  "start, so trials cannot be placed on one session clock and inter-trial periods are absent."),
 ("other", "In every two-probe session (162) the airflow and DLC tracking of the two files are the same recording deposited "
  "twice (identical samples and lengths). The 3D tracking holds one trial fewer than the trial table in 211 files, and the "
  "side-camera DLC rows differ from trials x 1471 in 25 files."),
 ("data_missing", "The dandiset holds only the multi-directional licking task recordings (335 insertions, where the paper "
  "reports 339). The cued licking task, the ALM, latSC and brainstem photostimulation experiments, the rat recordings, the raw "
  "videos used by the autoencoder and the premotor tracing data are not in it, and the paper names no other deposit; 19 of "
  "the paper's 48 claims cannot be tested here."),
 ("code_mismatch", "The Methods list a drift metric < 0.5 among the unit filters and a 4-pole Butterworth filter for phase "
  "tuning; the paper's code applies no drift filter and uses a 5th-order filter. The code's filter gives 20,109 units, close "
  "to the paper's 20,300; with the drift metric it gives 16,957."),
 ("methods_unavailable", "Question for the authors (fig2-licking-breathing-tuned-counts): the Methods compare the measured MI "
  "against 1000 MIs from resampled phases with a Wilcoxon rank-sum test. Is the test between MIs of resampled spike phases and "
  "MIs of random session phases (as process_mat.py does, 100 of each), or of the measured MI against the random-phase MIs? The "
  "first reproduces 3,517 / 1,021 / 177 tuned units here, the second 2,757 / 602 / 69."),
 ("methods_unavailable", "Question for the authors (fig2h-swallow-units-location, fig2-swallow-modulated-counts): is the swallow "
  "MI normalised by the larger of the two window rates (the code) or by the peak of the swallow PSTH (the Methods' 'peak spike "
  "rate during swallowing')? Here the first gives three of five enriched regions, the second two. Neither reproduces the counts "
  "427 / 175 / 55; how were swallow-only units defined?"),
 ("methods_unavailable", "Question for the authors (fig2f, ed8bc, fig4d, fig4e, fig4f): how were units 'near the preBotzinger "
  "complex' and in 'posterior-dorsal IRN/PARN' selected, since the CCF does not label them, and which 43 recordings form Fig 4d? "
  "With a region built below the AMB-labelled units only 16 units qualify and 1 or 2 recordings, and this attempt adopted the "
  "all-session reading of Fig 4e-f where the simultaneous reading leaves too few units."),
]
A = {
 "schema_version": 2, "id": "001619-kaku-2025-01",
 "dataset": {"archive": "dandi", "id": "001619", "version": "0.251027.1953", "doi": "10.48324/dandi.001619/0.251027.1953"},
 "paper": "doi:10.1101/2025.01.27.635041", "date": "2026-11-05", "entry": "001619-kaku-2025",
 "provenance": {"kind": "agent", "accountable": {"name": "CatalystNeuro"},
                "agent": {"harness": "Claude Code", "model": "claude-opus-5-5", "protocol": "pilot-13"},
                "runner": {"platform": "GitHub Actions", "url": "https://github.com/catalystneuro/encore/actions/runs/41988405043"}},
 "inputs": [
  {"what": "Allen CCF structure tree (names, acronyms and parent regions), to map the files' region names to the regions the claims name.",
   "source": "https://github.com/int-brain-lab/iblatlas at commit b88da5d8541d77285565fdb3f86f4f69c50b9e68 (iblatlas/allen_structure_tree.csv)"},
  {"what": "The paper's analysis code, whose steps are ported in kaku.py (as the claims file adopts them); no data from it.",
   "source": "https://github.com/NuoLiLabBCM/KakuEtAl2025 at commit fbc0abe"}],
 "outcomes": O,
 "findings": [{"kind": k, "statement": s} for k, s in findings],
}
yaml.safe_dump(A, open("attempts/001619-kaku-2025-01.yaml", "w"), sort_keys=False, width=110, allow_unicode=True)
print(len(O))
PYEOF
cd $TMPDIR && . env/bin/activate && pip list 2>/dev/null | grep -i pyyaml; python -c "import yaml" 2>&1 || uv pip install -q pyyaml; python attempt.py && cd  && python tools/entry.py check entries/001619-kaku-2025
```

```
PyYAML                    6.0.3
48
0 error(s)
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='/tmp/claude-1001/attempt.py'
s=open(p).read()
a='''"to 46.1% (median 30.0%); no session has none, so readings (a) and (b) both fail. Tongue onsets are rarer just before an "
    "inspiration and most frequent about 110 ms before it (not printed in the notebook beyond the latency table). The median latency "'''
b='''"to 46.1% (median 30.0%); no session has none, so readings (a) and (b) both fail. The median latency "'''
assert a in s; s=s.replace(a,b); open(p,'w').write(s)
EOF
. $TMPDIR/env/bin/activate && python $TMPDIR/attempt.py && date -u && grep -c ": " /dev/null; python - <<'EOF'
import yaml,re
t=open('attempts/001619-kaku-2025-01.yaml').read()
print(t.count('—'), len(re.findall(r'\brather\b',t)))
EOF
```

```
48
Thu Nov  5 10:15:57 UTC 2026
0
0 0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import re
p='/tmp/claude-1001/cells.py'
s=open(p).read()
for a in ["**Paper.**","**Dandiset.**","**What is not in it.**","**Outside input.**","**How the analysis differs from the paper's.**","**What was found about the dataset.**"]:
    s=s.replace(a,a.strip('*'))
open(p,'w').write(s)
bold=[m for m in re.findall(r'\*\*[^*]+\*\*',s) if not m.startswith('**Result:')]
print(bold, s.count('—'), len(re.findall(r'\brather\b',s)))
EOF
python build_nb.py && python - <<'EOF'
import nbformat
src=nbformat.read('entries/001619-kaku-2025/reproduce_kaku_2025.ipynb',4)
ex=nbformat.read('executed/001619-kaku-2025/reproduce_kaku_2025.ipynb',4)
assert len(src.cells)==len(ex.cells)
for i,c in enumerate(src.cells):
    assert ex.cells[i].cell_type==c.cell_type
    if c.cell_type=='code': assert ex.cells[i].source==c.source
    else: ex.cells[i].source=c.source
nbformat.write(ex,'executed/001619-kaku-2025/reproduce_kaku_2025.ipynb'); print('ok')
EOF
```

```
['**enrich(prebotc(d), B, PM)})\n    rows.append({"tuning": f"order {order}, {sig}", "region": "posterior ventral IRN", **', '**enrich(m.to_numpy(), L, PM)})\n    pons = T.in_P.to_numpy()\n    rows.append({"tuning": f"order {order}, {sig}", "region": "P (fraction > 1%?)", "n": int(pons.sum()), "tuned": int((pons & L).sum()),\n                 "fraction": (pons & L).sum() / pons.sum(), "base fraction": np.nan, "p": np.nan})\nLL = pd.DataFrame(rows)\nprint(LL.round(5).to_string(index=False))\n\'\'\', tags=["claim:fig2g-licking-units-location"])\n\nmd(r\'\'\'\n**', '** Licking-tuned units are enriched in XII (36% to 45% of 166 units), V (43%\nto 55% of 269) and IRN (34% to 40% of 1,804), against 20% to 26% of pons and medulla units (p < 0.00001\nin each, every reading), and make up 15% to 20% of pons units, above 1%.\n\'\'\')\n\ncode(r\'\'\'\nbase_sw = T.sess_has_sw.to_numpy()\nrows = []\nfor v4, col in (("V4(a)", "sw_mod_a"), ("V4(b)", "sw_mod_b")):\n    S = T[col].to_numpy()\n    for d in (300, 500):\n        for name, m in (("V", T.in_V.to_numpy()), ("IC", T.in_IC.to_numpy()), ("NLL", T.in_NLL.to_numpy()),\n                        ("lateral of NTS", lateral_nts(d)), ("above AMB", above_amb(d))):\n            rows.append({"V4": v4, "d": d, "region": name, **', '** 2 - R **'] 0 0
68
ok
Shell cwd was reset to
```

**Agent**

Now the entry README, then handover.

**Agent calls Bash**

```bash
cat > entries/001619-kaku-2025/README.md <<'EOF'
# Kaku, Liu et al. (2025) from dandiset 001619

Tests the findings of [Kaku, Liu et al. (2025)](https://doi.org/10.1101/2025.01.27.635041), "A
brainstem map of orofacial rhythms", that can be tested on
[DANDI:001619](https://dandiarchive.org/dandiset/001619/0.251027.1953). The dandiset holds the brainstem
Neuropixels recordings of 31 mice in the multi-directional licking task (335 probe insertions in 173
sessions), with DeepLabCut tracking of jaw and tongue, the 25 kHz airflow trace and CCF positions of the
units. The cued licking task with photostimulation, the rat recordings, the raw videos and the premotor
tracing data are not in it.

| Claim | Outcome |
|---|---|
| The dandiset holds the inputs of the paper's code (20,109 units pass its filter) | Reproduced |
| 20,300 units, 5,700 cerebellum, 3,700 pons, 10,900 medulla, 339 insertions | Partially reproduced |
| Spike rates of cerebellum, vestibular nuclei and medulla | Partially reproduced |
| Lick and breath frequencies (Fig 1d) | Not reproduced |
| Inspiration never coincides with licking (Fig 1f) | Not reproduced |
| Second lick delayed before a slow breath (Fig 1g) | Partially reproduced |
| Licks added as breathing slows, fixed latency (Fig 1f) | Partially reproduced |
| Inspiration delayed before a slow lick (Fig 1i) | Reproduced |
| Unidirectional oscillator models fail (Extended Data Fig 1d-i) | Reproduced |
| Licking paused at swallows (Extended Data Fig 1b-c) | Not reproduced |
| Rhythms follow swallows at fixed latencies (Fig 1k, m) | Reproduced |
| Inter-lick interval preserved across a swallow (Fig 1l) | Not reproduced |
| Lick cycle with a swallow prolonged by 33.3 ms (Fig 1l) | Reproduced |
| Inter-breath interval preserved; breath cycle prolonged by 48.0 ms (Fig 1n) | Reproduced (both) |
| 3,551 licking, 1,015 breathing and 182 both-tuned units | Partially reproduced |
| Swallow-modulated unit counts | Not reproduced |
| Breathing units near preBotzinger and posterior ventral IRN (Fig 2f) | Reproduced |
| Licking units in XII, V, IRN and pons (Fig 2g) | Reproduced |
| Swallow units in V, IC, NLL, beside NTS and above AMB (Fig 2h) | Partially reproduced, on an assumption |
| Swallow activity leads in V and IRN, follows in IC and NLL (Extended Data Fig 6e) | Reproduced |
| preBotzinger units fire at inspiration (Extended Data Fig 8b-c) | Not reproduced |
| Licking units active at full protrusion (Extended Data Fig 8e) | Reproduced |
| Licking map robust to a 500 uV amplitude filter (Extended Data Fig 4c) | Reproduced |
| Licking and breathing units anticipate the other rhythm (Fig 4e, f) | Reproduced (both), on an assumption |
| 43 simultaneous licking and breathing oscillator recordings (Fig 4d) | Not reproduced |
| Lick direction tuning (Extended Data Fig 8i) | Blocked: metadata insufficient |
| GLM (Extended Data Fig 7) | Blocked: too large |
| Cross-correlation of oscillator pairs (Fig 4g, h; three claims) | Blocked: other |
| Premotor regions (Fig 3a) | Blocked: other |
| Autoencoder, rats, photostimulation, cued task, premotor overlap (16 claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper's analysis code (github.com/NuoLiLabBCM/KakuEtAl2025 at commit fbc0abe) is ported to the
streamed NWB files. The files store each unit's spike offset at its start rather than its end, so a
standard NWB reader misassigns spikes; the helper reads them by the per-trial spike counts. The attempt
record, with the reasons and the differences from the paper's method, is
[`attempts/001619-kaku-2025-01.yaml`](../../attempts/001619-kaku-2025-01.yaml).

- `reproduce_kaku_2025.ipynb`: the analysis. It takes about 42 minutes, most of it streaming the
  airflow of 173 sessions and fitting tuning curves.
- `kaku.py`: loading, and the paper's code steps (movement timing, swallow detection, phase tuning,
  peak differences, swallow modulation). Other notebooks on this dandiset can import it.
EOF
grep -n "rather" entries/001619-kaku-2025/README.md
```

```
48:streamed NWB files. The files store each unit's spike offset at its start rather than its end, so a
```

**Agent calls Bash**

```bash
sed -i "s/The files store each unit's spike offset at its start rather than its end, so a/The files store the offset where each unit's spikes start, not where they end, so a/; s/premotor overlap (16 claims)/premotor overlap (15 claims)/" entries/001619-kaku-2025/README.md && sed -i 's/the paper.s 48 claims cannot be tested here./XX/' attempts/001619-kaku-2025-01.yaml && python - <<'EOF'
p='/tmp/claude-1001/attempt.py'
s=open(p).read()
s=s.replace('"videos used by the autoencoder and the premotor tracing data are not in it, and the paper names no other deposit; 19 of "\n  "the paper\'s 48 claims cannot be tested here."','"videos used by the autoencoder and the premotor tracing data are not in it, and the paper names no other deposit; 15 of "\n  "the 48 claims are blocked for missing data."')
open(p,'w').write(s)
EOF
. $TMPDIR/env/bin/activate && python $TMPDIR/attempt.py && grep -n "blocked for missing\|19 of" attempts/001619-kaku-2025-01.yaml; python tools/entry.py check entries/001619-kaku-2025 && python tools/entry.py handover entries/001619-kaku-2025; ls executed/001619-kaku-2025/handover; date -u
```

```
48
260:  notes: 'V4(a): enriched in V (13 of 234, 5.6%, p = 0.018), IC (34 of 313, 10.9%) and NLL (19 of 189, 10.1%) against
485:    deposit; 15 of the 48 claims are blocked for missing data.
0 error(s)
wrote executed/001619-kaku-2025/handover
10.1101-2025.01.27.635041.yaml
kaku.py
reproduce_kaku_2025.ipynb
Thu Nov  5 10:17:17 UTC 2026
```

**Agent calls Bash**

```bash
git status --short; python -c "
import nbformat;nb=nbformat.read('executed/001619-kaku-2025/handover/reproduce_kaku_2025.ipynb',4);print(sum(c.source.startswith('**Result') for c in nb.cells), any(c.source.startswith('## Summary') for c in nb.cells))"
```

```
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
?? attempts/001619-kaku-2025-01.yaml
?? entries/001619-kaku-2025/
?? scripts
0 False
```

**Agent calls Bash**

```bash
ls -la .bashrc .profile .idea scripts .mcp.json 2>&1 | head; ls scripts | head
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  5 07:35 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  5 07:35 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  5 07:35 .mcp.json
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  5 07:35 .profile
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  5 07:35 scripts
scripts
```

**Agent**

I finished steps 1 to 5 of the Author protocol and ran the handover (step 6). The entry is `entries/001619-kaku-2025/` and the record is `attempts/001619-kaku-2025-01.yaml`. `tools/entry.py all` passed with 0 check errors, and the notebook ran in 42 min (2527 s). I did not verify my own work and did not commit.

## 1. Outcome per claim (48 claims)

| Outcome | Claims |
|---|---|
| Reproduced (16) | code-dataset-link, fig1i, ed1 (unidirectional models), fig1k, fig1l-lick-cycle-prolonged (33.36 ms against 33.3), fig1n-breath-interval-preserved (P = 0.26), fig1n-breath-cycle-prolonged (48.13 ms against 48.0), fig2f, fig2g, ed6e, ed8e, ed4c, fig4e (assumed), fig4f (assumed) |
| Partially reproduced (7) | units-count, region-spike-rates, fig1g, fig1f-licking-mode-switch, fig2 tuned counts, fig2h (assumed) |
| Not reproduced (8) | fig1d, fig1f-inspiration-between-licks, ed1bc, fig1l-lick-interval-preserved, fig2 swallow counts, ed8bc, fig4d |
| Blocked, data missing (15) | ed2 (rats), ed7g, ed7h, fig3b, fig3ce, fig3dfh, ed10, fig4b, fig4c, ed11b, fig5b, fig5c, fig5e, fig5f, ed12c |
| Blocked, other (4) | fig4g, fig4g lags, fig4h (under the claims file's own selection only 1 or 2 recordings qualify, not 43); fig3a (no pinned source for the premotor neurons) |
| Blocked, metadata insufficient (1) | ed8i (lick direction) |
| Blocked, too large (1) | ed7 (GLM, about 2.7 million fits) |

The fig2 tuned counts match under the Methods' and the code's significance scheme: 3,517 / 1,021 / 177 against 3,551 / 1,015 / 182. Under the claims file's other reading, V3(b), they do not (2,757 / 602 / 69). The criterion asks for every reading, so the claim is partially reproduced.

## 2. What was found about the dataset
- **Spike index:** in all 335 files `spike_times_index` holds where each unit starts, not where it ends, so pynwb gives every unit the previous unit's spikes. I read spikes by the per-trial count table instead.
- **Histology rows:** 19 files have more histology rows than units, so regions and CCF positions cannot be matched to units with certainty. The code and I take them by position.
- **Duplicates:** in all 162 two-probe sessions the airflow and tracking are the same recording deposited twice. I counted each once.
- **No session clock:** every trial starts at 0, so trials cannot be placed in time within a session.
- **Implausible metadata:**
  - Age reads P210W to P303W.
  - The stimulus field says `photostim`, but no file has photostimulation data.
  - The left/right text contradicts `ccf_x` for 99.3% of units.
  - The 3D tracking has no stated axes or units.
- **Missing data:** the dandiset has 335 insertions against the paper's 339. The cued task, photostimulation, rats, raw videos and tracing data are absent.
- **Paper against its code:** the Methods' drift filter and "4-pole" filter differ from the code. The code's unit filter gives 20,109 units; adding the drift filter gives 16,957.
- **Clock check:** in four mice (DL004, DL005, DL010, DL020) the shared clock between airflow and spikes could not be established.

**Version:** 0.251027.1953, the only published version, since the paper cites none.

**Outside input:** the Allen structure tree from iblatlas at commit b88da5d, used only to map region names.

**Assumptions:**
- V4(a), the code's swallow normalisation (fig2h).
- O2(a), all sessions, for fig4e and fig4f, because the simultaneous-recording reading leaves 1 or 2 units.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- Which test gives the significance of the licking and breathing MI?
- How is the swallow MI normalised, and how are "swallow-only" units defined?
- How were units near the preBötzinger complex and in posterior-dorsal IRN/PARN chosen, and which 43 recordings make up Fig 4d?

**Questions to a reader:** none.

## 3. Where the protocol was unclear or did not fit
1. The claims file's rule (readings that disagree means block as `methods_underspecified`) conflicts with step 1.6, which lets the author adopt the best-supported reading. Where a criterion gave its own partial rule I followed it; otherwise I adopted an assumption (fig2h, fig4e, fig4f).
2. A 130 GB dataset with 25 kHz airflow needs about 40 min for one pass, close to the 60-minute CI limit. The protocol says nothing on splitting notebooks or caching. I kept one notebook and cut CPU (a grid fit for the resamples).
3. "Run on the whole dataset once" did not fit: I needed one full development run (75 min, as a script) and then the entry run.
4. There is no blocked category for "not run within the run's time" when it isn't strictly the computation. I used `too_large` with an arithmetic estimate for the GLM, and `other` (too few recordings under the claim's selection) for the cross-correlation claims.
5. fig3a is `data: elsewhere` but the paper gives no identifier. The checker forbids `data_missing` and I cannot change the claim's `data` field, so I used `other`.
6. The clock-check guidance assumes a session timeline. Here every trial starts at 0, so I paired each trial's spikes with the next trial's phases.
7. `archives.md` does not say that h5py's global lock stops threaded streaming. Reading in parallel needed separate processes.

## 4. Runtime and failures
- The run took about 2 h 40 min (07:37 to 10:18 UTC). The final notebook took 42 min, the development extraction 75 min.
- **First extraction too slow:** 75 min, over the limit. Fixed by a coarser float32 grid and computing significance only for units with MI above 0.6.
- **Ontology name matching:** the iblatlas copy drops the commas of the Allen names. Fixed by normalising.
- **Survey crash:** the table-length mismatch first crashed the survey; now handled and recorded.
- **Cross-correlation not computed:** for fig4g and fig4h it was not computed at all.
- **Untracked files I did not create:** dotfiles such as `.bashrc` and `scripts` are sandbox device mounts present before the run; I left them.

## End of run

87 turns, 158 minutes, $11.50 at API prices, result: success.
