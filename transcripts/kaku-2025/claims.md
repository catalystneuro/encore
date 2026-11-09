# 001619 · claims · run 39606566592

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/001619/ claims/001453/ paper/ 2>&1; git log --stat -3 | head -40; wc -l docs/protocol.md
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat transcripts/001619/claims-report.md transcripts/001619/claims-check-report.md
```

```
I wrote no claims for DANDI:001619. The paper text is missing a supplement that the results rest on, and the protocol says to stop in that case. Nothing was written under `claims/001619/`.

**Text read:** `paper/10.1101-2025.01.27.635041.txt`, the bioRxiv preprint as served on its web page (posted January 27, 2025). It has the main text, the legends of Figures 1 to 5, the Methods and the references. There is no PDF and no supplement file.

**What is missing:**
1. **The Extended Data Figures 1 to 12 and their legends.** The text cites them about 60 times, but none of their legends is in it. The page lists a "Supplementary Material" link that was not fetched. Many reported results rest only on these figures:
   - ED 1b-c: licking pauses during swallows, used to check the swallow detector.
   - ED 1d-i: the simulations of one-way coupling between the two oscillators.
   - ED 2: the rat data.
   - ED 4: results unchanged by spike-sorting quality.
   - ED 5f and 6: how the swallowing, licking and breathing tunings overlap, and the swallowing clusters in the inferior colliculus and the nucleus of the lateral lemniscus.
   - ED 7c-h: the model fits on tracked features against the autoencoder embedding, including the exception in the preBötzinger complex.
   - ED 8: preferred phases, and the preference of licking units for ipsilateral licks.
   - ED 10: the brainstem stimulation sites.
   - ED 11: licking rate and breathing rate during ALM stimulation.
   - ED 12: the cross-correlation pairs, including those recorded when the mouse was not licking.

   The Methods also point to these figures for method details: the swallow detector (ED 1a), phase tuning and the modulation index (ED 5a, c, e), and the model's design (ED 7a).
2. **Figure 5g.** The Results cite it for the comparison of breathing-adjustment latencies (P < 0.0001, bootstrap), but the Figure 5 legend stops at panel f.
3. **Code.** The paper says "Code used for analyses will be deposited upon publication." It link
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n '^#' docs/protocol.md
```

```
1:# Protocol for an attempt
36:## Reader
38:### 1. Get the paper
49:### 2. Read the paper's code
59:### 3. Write the claims file
142:### 4. Data from outside the paper's own recordings
150:### 5. Check
163:### 6. Answer questions
171:## Author
179:### 1. Establish what can be tested
277:### 2. Check the data against its description
292:### 3. Write the entry
341:### 4. Lock, check and run
352:### 5. Record the attempt
399:### 6. Hand over for verification
433:## Repeat attempts
446:## Verifier
450:### Round 1: without the author's conclusions
468:### Round 2: with the author's conclusions
479:### Round 3: proposed changes
```

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "limit": 170
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-10`. Record this version in the attempt's provenance.
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
18	  claim, and it asks a reader for any method detail the file lacks.
19	- The **verifier** checks the author's work and must not be the author.
20	
[... 150 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -250; wc -l claims/001453/*.yaml paper/*.txt; head -30 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1101-2025.01.27.635041.txt",
 "offset": 30,
 "limit": 340
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1101-2025.01.27.635041.txt",
 "offset": 30,
 "limit": 130
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1101-2025.01.27.635041.txt",
 "offset": 160,
 "limit": 215
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1101-2025.01.27.635041.txt",
 "offset": 374,
 "limit": 540
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
curl -s -m 20 https://api.dandiarchive.org/api/dandisets/001619/ | python3 -c "import json,sys; d=json.load(sys.stdin); print(json.dumps(d,indent=1)[:3000])"; curl -s -m 20 "https://api.dandiarchive.org/api/dandisets/001619/versions/draft/info/" | python3 -c "import json,sys; d=json.load(sys.stdin)['metadata']; print(d.get('name')); print(d.get('description')); print(d.get('assetsSummary'))"
```

Result: the fetched text is not kept.

**Agent**

Supplement is now present (Extended Data legends). The dandiset description names the analysis code repo the paper promised; I'll read it.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/NuoLiLabBCM/KakuEtAl2025 && cd KakuEtAl2025 && git log -3 --format='%H %ad %s' && find . -type f -not -path './.git/*' | head -100 && find . -type f -not -path './.git/*' | wc -l
```

```
fbc0abed27e3d00437c62ec87aff3b5241ba52d5 Thu Jun 18 14:33:03 2026 -0400 Update README.md
5b4fca4ec1941677cf60c4dc7634657d00e53b82 Thu Jun 18 14:32:13 2026 -0400 Create README.md
084976009f61a8a396f6ed10b766bdbff470c504 Thu Jun 18 14:26:47 2026 -0400 Upload Kuramoto simulations
./requirements.yml
./process_mat.py
./plotBrain.m
./nwb2mat/setup.exe
./nwb2mat/nwb2mat.msi
./loadTifFast.m
./generate_figures.py
./generate_activity_maps.m
./crameri_documentation.m
./crameri.m
./README.md
./LICENSE.txt
./Kuramoto_model_simulations/time_since_previous_event.m
./Kuramoto_model_simulations/sim_simple_asym_real.m
./Kuramoto_model_simulations/sim_simple_asym_param_range.m
./Kuramoto_model_simulations/sim_model_comparison_stall_conditional_phase.m
./Kuramoto_model_simulations/sim_model_comparison_kuramoto_conditional_phase.m
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/KakuEtAl2025 && cat README.md Kuramoto_model_simulations/README.md requirements.yml | head -150; wc -l *.py *.m
```

```
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
### Step 1
Download the NWB dataset from [DANDI archive](https://dandiarchive.org/dandiset/001619).
[... 46 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/KakuEtAl2025/process_mat.py"
}
```

```
1	import scipy
2	from scipy.io import loadmat, savemat
3	from scipy import stats, signal
4	import numpy as np
5	import glob
6	import os
7	import time
8	
9	
10	def get_good_trials(mat):
11	    """ """
12	    
13	    tracking = mat['tracking']
14	    side = tracking['camera_3_side']['jaw_likelihood']
15	    bottom = tracking['camera_4_bottom']['jaw_likelihood']
16	    trials_side = tracking['camera_3_side']['trialNum']
17	    trials_bottom = tracking['camera_4_bottom']['trialNum']
18	    trials = np.array(list(set(trials_side) & set(trials_bottom)))
19	    
20	    good_trials, bad_trial_bot, bad_trial_side = [], list(set(trials_side) - set(trials_bottom)), list(set(trials_bottom) - set(trials_side))
[... 997 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/KakuEtAl2025/process_mat.py",
 "offset": 1018,
 "limit": 565
}
```

```
1018	                
1019	        spikes[:] = [ele for i, ele in enumerate(spikes) if ibi[i]<max_ibi]
1020	        lick2_time=lick2_time[ibi<max_ibi]
1021	        n_licks=n_licks[ibi<max_ibi]
1022	        lick_bef_time=lick_bef_time[ibi<max_ibi]
1023	        ibi=ibi[ibi<max_ibi]
1024	        
1025	        idx_all=np.arange(0,len(ibi))
1026	        lick1_rem=np.where((n_licks==1) & (lick_bef_time>-0.05) & (lick_bef_time<0))
1027	        lick2_rem=np.where((n_licks==2) & (lick2_time>(ibi-0.05)) & (lick2_time<ibi))
1028	        idx_keep=np.setdiff1d(idx_all,np.concatenate((lick1_rem[0],lick2_rem[0])))
1029	    
1030	        spikes = [spikes[i] for i in idx_keep]
1031	        n_licks=n_licks[idx_keep]
1032	        lick_bef_time=lick_bef_time[idx_keep]
1033	        ibi=ibi[idx_keep]
1034	        
1035	        sorted_indexes=np.argsort(ibi)
1036	        sorted_indexes=sorted_indexes[::-1]
1037	        
[... 544 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/KakuEtAl2025/generate_figures.py"
}
```

```
1	from scipy.io import loadmat
2	from scipy import stats
3	import numpy as np
4	import matplotlib.pyplot as plt
5	import glob
6	import os
7	
8	def volcano_plot_licking(mat, max_ibi=None):
9	    inspir_onset = mat['processed']['inspir_onset']
10	    lick_onset_time = mat['processed']['lick_bout_onset']
11	    lick_offset_time = mat['processed']['lick_bout_offset']
12	    ton_onset = mat['processed']['tongue_onset']
13	    
14	    inspir_onset_l=[] 
15	    for i,val in enumerate(lick_onset_time):
16	        inspir_onset_l.append(inspir_onset[(inspir_onset>(lick_onset_time[i]+0.2)) & (inspir_onset<(lick_offset_time[i]-0.2))])
17	    inspir_onset_l=np.array(inspir_onset_l)
18	    inspir_onset_l=np.hstack(inspir_onset_l)
19	    
20	    licks = [] 
[... 897 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/KakuEtAl2025 && cat generate_activity_maps.m plotBrain.m; ls Kuramoto_model_simulations; head -60 Kuramoto_model_simulations/sim_simple_asym_real.m
```

```
%% Init
clc; clear all
% Define directory
export_path = 'D:/mat/'; 

% Get all files ending with 'processed.mat'
files = dir(fullfile(export_path, '*processed.mat'));

% Initialize storage
ccf_unitxA = [];
ccf_unityA = [];
ccf_unitzA = [];
jaw_tuning = [];
breath_tuning = [];
swallow_tuning = [];
swallow_ccf_x = [];
swallow_ccf_y = [];
swallow_ccf_z = [];
num_events = [];
swallow_pvals = [];
[... 176 more lines not kept]
```

**Agent calls Bash**

```bash
ls docs tools claims; sed -n 1,80p tools/claims_check.py; grep -rn "open\b\|readings\|kind:" claims/*/*.yaml | head -30
```

```
claims:
000003
000004
000005
000006
000008
000009
000035
000041
000044
000056
000059
000061
000067
000070
000114
000121
000127
000130
000147
[... 203 more lines not kept]
```

**Agent calls Bash**

```bash
ls schemas; python3 -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d,indent=1)[:6000])"; sed -n 1,80p claims/001642/*.yaml
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
{
 "$schema": "https://json-schema.org/draft/2020-12/schema",
 "title": "Claims proposed for one target (a dataset and one of its papers)",
 "description": "Draft. To be revised after the pilot.",
 "type": "object",
 "additionalProperties": false,
 "required": [
  "schema_version",
  "dataset",
  "paper",
  "claims"
 ],
 "properties": {
  "schema_version": {
   "const": 2
  },
  "dataset": {
[... 268 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d['\$defs'],indent=1))"
```

```
{
 "expected": {
  "type": "object",
  "additionalProperties": false,
  "required": [
   "quantity",
   "value"
  ],
  "properties": {
   "quantity": {
    "type": "string"
   },
   "value": {
    "type": "number"
   },
   "tolerance": {
    "type": "number",
    "minimum": 0
   },
   "unit": {
[... 82 more lines not kept]
```

**Agent**

The paper text now includes the Extended Data legends, and the dandiset description names the analysis code (NuoLiLabBCM/KakuEtAl2025, commit fbc0abe), which I've read. Writing the claims file now.

**Agent calls Bash**

```bash
cd $TMPDIR/KakuEtAl2025 && grep -n "trial_len\|video_fs\|traces_len" process_mat.py | head; sed -n 60,140p Kuramoto_model_simulations/sim_simple_asym_real.m | head -30
```

```
117:    traces_len = np.size(session_traces_b_z, axis = 1)
156:        good_breathing[i] = d[breathing_ts[i] < traces_len*3.4/1000]
396:    fs = mat[foi]['video_fs']
467:    traces_length = [len(d) for d in good_traces]
468:    good_trial_ind = np.where(np.array(traces_length) == 5*fs/ds)[0]
625:    traces_len=1471
700:            good_spikes[i] = d[d < traces_len*3.4/1000]+traces_len*3.4/1000*i
898:    traces_len=1471
992:            good_spikes[i] = d[d < traces_len*3.4/1000]+traces_len*3.4/1000*i
1103:    fs = mat[foi]['video_fs']
        w1, w2, ...     % mean frequencies
        sigma1, sigma2, ... % sigma1, sigma2
        5, ...      % tau_omega
        tspan, ...
        theta0);


    % Wrap phases to [0, 2*pi)
    theta_wrapped = mod(theta, 2*pi);

[... 22 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "content": "# Claims for Kaku, Liu et al. (2025), \"A brainstem map of orofacial rhythms\", bioRxiv\n# doi:10.1101/2025.01.27.635041, on dandiset 001619.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-21,\n# protocol pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the bioRxiv preprint, version 1 (posted January 27, 2025), as served on its web\n# page, stored in paper/10.1101-2025.01.27.635041.txt: main text, legends of Figures 1 to 5,\n# Methods and references, and the supplement \"Extended Data Figures\" (the legends of Extended\n# Data Figures 1 to 12, from the supplement PDF, extracted to text). The display equations of\n# the Methods (the circular Gaussian tuning curve and the VAF) are missing from the text; the\n# words around them name every term. The Figure 5 legend stops at panel f, although the\n# Results cite a Figure 5g. No later version was read. Data the dandiset description names: its\n# title and description only (no data or file was looked at).\n#\n# Code read: github.com/NuoLiLabBCM/KakuEtAl2025 at commit fbc0abe (2026-06-18). The preprint\n# says \"Code used for analyses will be deposited upon publication\"; this repository is the one\n# the dandiset description names as \"the corresponding analysis code\", and its README points\n# at the preprint v1 and at dandiset 001619. It holds process_mat.py (unit quality filter,\n# trial filter, tongue and inspiration onsets, lick bouts, licking and breathing phase tuning\n# and modulation index, the lick-to-breath and breath-to-lick timing analyses of Figs 1f-i and\n# 4e-f, the swallow detector, swallow-aligned licks and breaths, swallow modulation index),\n# generate_figures.py (plots of Figs 1, 2 and 4; no statistical test), generate_activity_maps.m\n# (the activity maps of Fig 2f-h) and Kuramoto_model_simulations/ (coupled-oscillator\n# simulations that the preprint v1 does not describe; not used here). The code does not hold\n# the Fig 1d frequency statistics, the GLM and CAE, lick direction tuning, the cross-correlation\n# analysis, the analyses of the cued licking task (Figs 3c-h, 4a-c, 5), the rat analysis, the\n# simulations of Extended Data Fig 1d-i, or any statistical test.\n#\n# Data the paper used, as it reports them (Methods, Mice and following sections).\n#  - Electrophysiology: 31 VGAT-ChR2-EYFP mice (22 male, 9 female), 339 insertions of one or two\n#    Neuropixels 1.0 probes (bank 0, 384 sites), Kilosort 2.5, 20,300 single units after quality\n#    control (5,700 cerebellum, 3,700 pons, 10,900 medulla), each localized in Allen CCFv3. Mice\n#    performed a multi-directional licking task: a 2 uL drop on a spout at one of nine targets,\n#    4 s to lick, 40 trials per target, 2 s intertrial interval. Airflow (breathing) at 25 kHz in\n#    SpikeGLX; side (400 x 480) and bottom (720 x 540) videos at 3.4 ms per frame, DeepLabCut\n#    tracking of jaw, tongue and lickport tips in both views, combined into 3D.\n#  - Simultaneous licking- and breathing-oscillator recordings (Fig 4d-h): 43 recordings in 21\n#    mice, two probes, posterior-dorsal IRN/PARN and preBotzinger complex; Extended Data Fig 12c\n#    places them in the cued licking task.\n#  - ALM photostimulation: 11 mice (9 Sim1_KJ18-Cre and 2 Tlx_PL56-Cre, crossed to Ai32), cued\n#    licking task (3.4 kHz Go cue, 0.1 s; 25-50% of trials replaced by 2 s of 20 Hz light, no\n#    reward), with breathing and video. latSC photostimulation: 3 mice, no task. Brainstem\n#    photostimulation: 27 Phox2b-Cre mice (16 crossed to Ai32, 11 with ChR2 or ChRmine virus),\n#    46 fibre sites, constant light for 2 s.\n#  - Rats: 7 Long-Evans females, freely moving, lickometer contacts and nasal thermocouple.\n#  - Outside data: premotor neurons of the masseter and genioglossus from reference 43 (Takatoh\n#    et al. 2021, eLife 10:e67291) mapped into CCF; ALM and latSC anterograde projections\n#    contributed by co-authors (no source given).\n# The dandiset (title and description) is meant to hold the Neuropixels recordings of the\n# brainstem map, the DeepLabCut tracking and the CCF localization; 31 subjects.\n#\n# Methods fixed by the paper and its code, used by the criteria below.\n#  - Units (Methods, Preprocessing): amplitude > 150 uV, ISI violation < 10, rate > 0.2 Hz,\n#    presence ratio > 0.9, amplitude cutoff < 0.15, drift metric < 0.5. The code\n#    (get_good_units) applies the first five and not the drift metric: variant V1.\n#  - Trials (code, get_good_trials): trials tracked in both cameras with no negative jaw\n#    likelihood.\n#  - Tongue onset (Methods; code get_movement_timing): first frame with the tongue detected,\n#    tongue likelihood > 0.95 in both views. Lick bouts as in get_movement_timing (licks at 3 to\n#    9 Hz, runs of at least three). Inspiration onset: z-scored airflow, 3.4 ms bins, 5th-order\n#    Butterworth 1-15 Hz, Hilbert phase crossing 0, kept only when the trace crosses -0.5\n#    within the cycle (code); the Methods say only \"phase was equal to 0\".\n#  - Lick-to-breath timing, Fig 1f-g (code get_peak_diff_lick_behv): inspirations inside lick\n#    bouts (0.2 s after bout onset to 0.2 s before offset), with licks between this inspiration\n#    and the next; breath cycles longer than the session's longest inter-breath interval\n#    dropped; the code's two exclusions of licks within 50 ms of an inspiration; cycles with\n#    exactly two licks split at the median inter-breath interval into fast and slow halves;\n#    lick PSTHs from -0.4 to 1 s in 20 ms bins; the second-lick peak (find_peaks, threshold\n#    mean + SD of the PSTH, at least 5 per s, 140 ms apart) taken in 0.12-0.32 s (fast) and\n#    0.16-0.36 s (slow); the session value is slow minus fast; sessions with fewer than 40\n#    cycles in either half dropped.\n#  - Breath-to-lick timing, Fig 1h-i (code get_peak_diff_breath_behv): licks inside bouts with\n#    an inspiration before the next lick, split at the median inter-lick interval; inspiration\n#    PSTHs -0.1 to 0.6 s in 20 ms bins; peak (threshold mean + SD, at least 7 per s, 240 ms\n#    apart) in 0-0.22 s (fast) and 0-0.24 s (slow); slow minus fast; at least 100 per half.\n#  - Unit versions, Fig 4e-f (code get_peak_diff_lick_unit, get_peak_diff_breath_unit): the\n#    same splits with spikes in place of licks or breaths; for licking units the 40 fastest and\n#    40 slowest two-lick cycles; peaks above max(mean + SD, 10 spikes/s), in 0.1-0.3 s and\n#    0.16-0.36 s (licking units) or 0-0.24 s and 0.02-0.26 s (breathing units).\n#  - Swallows (Methods; code detect_swallows): negated z-scored airflow at 3.4 ms, 5-sample\n#    moving average, peaks (find_peaks, distance 10) with Hilbert phase between 1.2 and 1.7 rad;\n#    at least 5 licks in the 1.5 s before and 1 in the 0.25 s after, last lick within 0.5 s, the\n#    last four lick frequencies between 3.5 and 13 Hz; inside a pause where the trace velocity\n#    stays within +-0.07 for at least 50 ms; swallow onset is the pause start.\n#  - Swallow-aligned intervals, Fig 1k-n (code plot_licking_swallow_summary,\n#    plot_breath_swallow_summary): events with at least 4 licks (breaths) before and 2 after;\n#    the interval spanning the swallow, cycle 0, between 1/15 and 1/3 s for licks (1/2 s for\n#    breaths); Delta(0,-1) and Delta(1,-1) as in the Fig 1l legend; the code ranks events by\n#    cycle 0, longest first, and keeps the first third (\"bottom 1/3\").\n#  - Phase tuning (Methods; code get_unit_jaw_tuning, get_unit_breath_tuning): jaw (side-camera\n#    jaw_y) bandpassed 3-15 Hz, airflow 1-10 Hz, Butterworth forwards and backwards, Hilbert\n#    phase; the first 5 s of each trial; spike phases in 20 bins divided by the occupancy of each\n#    phase bin; a circular Gaussian (amplitude, preferred phase, width, baseline; distance is the\n#    shortest circular distance) fitted with scipy curve_fit from two starting phases, the\n#    better r2 kept; MI = (r(phi) - r(phi - pi)) / r(phi). Tuned unit, Results and Methods,\n#    P < 0.001 and MI > 0.6.\n#  - Swallow modulation (Methods; code get_swallow_tuning, generate_activity_maps.m): rates in\n#    -0.3 to -0.1 s, -0.05 to 0.05 s and 0.1 to 0.3 s around swallow onset; an MI against the\n#    window before and one against the window after, averaged; 1000 bootstrap resamples of\n#    swallow events, p the fraction of resamples where the difference changes sign; a unit is\n#    swallow-modulated when both p <= 0.01, mean MI > 0.3 and it has at least 20 swallows.\n#\n# Variants (the Methods come first; the code's choice is shown beside it).\n#  - V1, quality filter with or without the drift metric (above).\n#  - V2, phase-tuning filter. The Methods say \"4-pole Butterworth\"; the code uses\n#    scipy.signal.butter(5, band). Readings of the Methods (a) butter(4, band); (b) butter(2,\n#    band), four poles in all. The code's order 5 is shown as a variant.\n#  - V3, significance of the licking and breathing MI. The Methods resample phases 1000 times\n#    and use a Wilcoxon rank-sum test against the resampled distribution; the code makes 100\n#    MIs from resampled spike phases and 100 from random session phases and tests them with a\n#    one-sided Mann-Whitney U. Readings (a) the code's scheme with 1000 resamples of each;\n#    (b) the measured MI ranked against 1000 MIs from random session phases, p the fraction at\n#    least as large. The code's scheme with 100 resamples is shown as a variant.\n#  - V4, swallow MI normalization. The Methods normalize \"to the peak spike rate during\n#    swallowing\"; the code divides each difference by the larger of the two window rates. For\n#    positive MIs the two agree when the peak is read as the mean rate in the swallow window;\n#    reading (b), the peak of the 50 ms-smoothed swallow PSTH within +-50 ms, is also run.\n#\n# Details the paper and the code leave open (each criterion names those it needs).\n#  - O1, the units of a \"breathing unit\" and \"licking unit\" in Fig 4 and Extended Data Fig 8.\n#    The Results use MI > 0.6; Extended Data Fig 8b and e use MI > 0.9; the code's Fig 4e-f\n#    summary uses MI > 0.9 with no p threshold. Readings (a) MI > 0.6 and P < 0.001; (b) MI > 0.9\n#    and P < 0.001; (c) MI > 0.9 alone (code).\n#  - O2, which recordings Fig 4e-f use. Readings (a) every session with tuned units (the code's\n#    plot_summary loops over all files); (b) the 43 simultaneous recordings, units in the\n#    posterior-dorsal IRN/PARN (licking) and near the preBotzinger complex (breathing), as\n#    defined in O3.\n#  - O3, regions the CCF does not label. The preBotzinger complex is not an Allen CCF region;\n#    Extended Data Figs 7c and 8c place it below the nucleus ambiguus (AMB). Readings: units\n#    within (a) 300 um or (b) 500 um ventral of AMB, inside AMB's anterior-posterior and\n#    medial-lateral extent. \"Posterior-dorsal IRN/PARN\" is units labelled IRN or PARN posterior\n#    to the AP midpoint of IRN and dorsal to its DV midpoint, with (a) and (b) the same as for\n#    \"posterior ventral IRN\" (posterior and ventral halves). The paper gives no numbers.\n#  - O4, the statistical unit of Fig 1g and 1i. The text says \"In all mice\"; the legend says\n#    \"for all sessions\"; the code gives one value per session. Readings (a) sessions; (b) the\n#    mean over each mouse's sessions.\n#  - O5, the ranking of swallow events for Fig 1l and 1n. The code ranks by cycle 0 (the\n#    interval spanning the swallow); the Results say \"ordered by their frequencies before the\n#    swallow\". Readings (a) the code's ranking, the third with the longest cycle 0; (b) ranking\n#    by cycle -1, the third with the longest cycle -1; (c) all events. The t-tests are over\n#    swallow events pooled across sessions, as the code pools them; (d) is (a) with session\n#    means as the unit.\n#  - O6, cross-correlation (Fig 4g-h, Extended Data Fig 12). The Results refer to Methods that\n#    have no such section. Readings for the bin (a) 5 ms, (b) 10 ms; window +-250 ms; trial\n#    shuffle as pairing unit 1 on trial i with unit 2 on trial i+1 (all shifts pooled), the 95%\n#    interval pointwise from the shuffled correlograms; a pair is significant when the\n#    measured correlogram leaves the interval at (i) any bin within +-100 ms, or (ii) any bin\n#    within +-100 ms after Bonferroni over the bins of the window; positive or anticorrelated\n#    by the sign of the largest excursion; the lag is the bin of that excursion.\n#  - O7, the Kuiper test of Fig 5c and 5f, \"two sample\" against a \"random distribution\".\n#    Readings for the second sample (a) phases at random times in the same session;\n#    (b) phases at -500 ms from lick onset. Time steps on the 3.4 ms video grid from -500 ms to\n#    lick onset; Bonferroni over the steps; the latency is the earliest step from which every\n#    later step is significant at p < 0.0001; the s.e.m. by 1000 bootstrap resamples of trials.\n#  - O8, the GLM (Extended Data Fig 7). The L1 weight is not given. Readings (a) no penalty;\n#    (b) the weight per unit with the highest validation VAF from 1e-4 to 1 in decades. The\n#    VAF is (i) the best of the 11 lags; (ii) lag 0. The link is (i) log (Poisson canonical);\n#    (ii) logit, as the text says. The CAE follows reference 40 and needs the raw videos.\n#  - O9, the lick angle. Methods: tongue tip at full protraction against the jaw's resting\n#    position; Extended Data Fig 8g: against the midline. Both are run.\n#  - Tolerances. A mean +- SD of pooled single intervals or units describes the spread of the\n#    sample, not the uncertainty of the mean; such means get 10%. Means given +- s.e.m. use the\n#    s.e.m.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001619\"\npaper: doi:10.1101/2025.01.27.635041\nclaims:\n- id: code-dataset-link\n  kind: link\n  statement: The dandiset is the data the paper's analysis code reads, so that the code's\n    choices fixed in this file apply to it.\n  source: Code availability; the dandiset description; README of NuoLiLabBCM/KakuEtAl2025 at\n    commit fbc0abe\n  data: dataset\n  criterion: Reproduced when process_mat.py's inputs can be built from the NWB files (spike\n    times per trial, unit quality metrics, CCF coordinates, airflow at 25 kHz with its\n    timestamps, side and bottom DeepLabCut jaw and tongue traces and likelihoods, 3D jaw and\n    tongue tracks) and the count of units passing get_good_units over all files is within 10%\n    of 20,300 (with or without the drift metric, V1). Partially reproduced when the inputs\n    exist but the count is outside 10%.\n- id: fig1d-lick-breath-frequencies\n  statement: Mice licked at 6.23 +- 2 Hz (95% range 3.59 to 8.91 Hz) and breathed at lower\n    frequencies, 4.02 +- 1.24 Hz (95% range 2.12 to 7.17 Hz).\n  source: Results, Coordination of breathing, licking, and swallowing, paragraph 2; Figure 1d\n  quote: Licking occurred at 6.23 ± 2 Hz (mean ± std, 95% range: 3.59 - 8.91 Hz) while breathing\n    occurred at lower frequencies (4.02 ± 1.24 Hz, 95% range: 2.12 - 7.17 Hz; Figure 1d)\n  expected:\n  - quantity: mean licking frequency\n    value: 6.23\n    tolerance: 0.62\n    unit: Hz\n  - quantity: mean breathing frequency\n    value: 4.02\n    tolerance: 0.4\n    unit: Hz\n  - quantity: licking 95% range, lower bound\n    value: 3.59\n    tolerance: 0.36\n    unit: Hz\n  - quantity: licking 95% range, upper bound\n    value: 8.91\n    tolerance: 0.89\n    unit: Hz\n  - quantity: breathing 95% range, lower bound\n    value: 2.12\n    tolerance: 0.21\n    unit: Hz\n  - quantity: breathing 95% range, upper bound\n    value: 7.17\n    tolerance: 0.72\n    unit: Hz\n  criterion: Neither the Methods nor the code say how the frequencies are taken. Readings\n    (a) the inverse of every interval between consecutive tongue onsets, and between\n    consecutive inspiration onsets, within trials, pooled over all sessions; (b) the same\n    within lick bouts only (code bouts). Onsets as in the header. The 95% range is the 2.5th to\n    97.5th percentile. Reproduced when, under one reading, all six values are within tolerance;\n    partially reproduced when the two means are and a bound is not.\n- id: fig1f-inspiration-between-licks\n  statement: Inspiration always occurred between licks and never coincided with licking;\n    licking preceded inspiration at a fixed latency.\n  source: Results, Coordination of breathing, licking, and swallowing, paragraph 2; Figure 1f\n  quote: Inspiration always occurred between licks and thus never coincided with licking. Licking\n    preceded inspiration at a fixed latency\n  criterion: The paper shows this in raster plots and gives no measure. Measure, from the\n    paper's definitions, the fraction of inspiration onsets inside lick bouts that fall within\n    a tongue protrusion (tongue onset to tongue offset, code get_movement_timing), per session.\n    \"Never\" is read (a) literally, no such inspiration in any session, and (b) as a rounded\n    statement, under 5% of inspirations in pooled data (a standard choice, named here).\n    Reproduced when (b) holds; the result under (a) is reported. The latency from the last\n    lick to the next inspiration is reported per number of licks in the cycle.\n- id: fig1g-lick-delayed-before-slow-breath\n  statement: For breath cycles with two licks, the second lick was delayed preceding a slower\n    breath compared to a fast breath, in all mice (one-sample t-test, two-tailed, p < 0.001),\n    so breathing influences the licking rhythm.\n  source: Results, Coordination of breathing, licking, and swallowing, paragraph 2; Figure 1g\n  quote: In all mice, the lick timing was significantly delayed preceding a slower breath compared\n    to a fast breath (Figure 1g, p<0.001, one sample t-test, two-tailed)\n  statistics:\n  - test: one sample t-test, two-tailed\n    p: 0.001\n    p_relation: \"<\"\n    n: all sessions (legend) or all mice (text)\n  criterion: The per-session peak difference of the header (Lick-to-breath timing, code\n    get_peak_diff_lick_behv), slow minus fast. One-sample two-tailed t-test against 0 under\n    O4 (a) sessions and (b) mice. Reproduced when the mean is positive with p < 0.001 under a\n    reading and every mouse's mean difference is positive; partially reproduced when p < 0.001\n    with a positive mean but one or more mice are not positive.\n- id: fig1f-licking-mode-switch\n  statement: During slow breathing, licking frequency increased abruptly to add licks within\n    the breathing cycle (1, 2, 3 or 4 licks between breaths), keeping the fixed lick latency\n    before the next inspiration, so licking shifted between modes of oscillation with\n    breathing frequency.\n  source: Results, Coordination of breathing, licking, and swallowing, paragraph 3; Figure 1f\n  quote: During slow breathing, when the next lick could not be delayed further to accommodate the\n    next breath, licking frequency abruptly increased to add additional licks within the\n    breathing cycle to maintain the fixed lick latency preceding the next inspiration\n  criterion: The paper shows this in a raster grouped by the number of licks in the cycle\n    (code volcano_plot_licking). With the breath cycles of the header, pooled per session,\n    reproduced when the median inter-breath interval rises strictly from 1 to 2 to 3 licks per\n    cycle (and to 4 where a session has at least 20 such cycles) in most sessions (more than\n    half), and the median latency from the last lick to the next inspiration differs by less\n    than 20% between the groups (a standard choice, named here).\n- id: fig1i-breath-delayed-before-slow-lick\n  statement: Inspirations following licking were significantly delayed for slower licking\n    frequencies, anticipating the next lick (one-sample t-test, two-tailed, p < 0.001), so\n    licking influences breathing.\n  source: Results, Coordination of breathing, licking, and swallowing, paragraph 4; Figure 1i\n  quote: inspirations following licking were significantly delayed for slower licking frequencies\n    to anticipate the next lick (Figure 1i, p<0.001, one sample t-test, two-tailed)\n  statistics:\n  - test: one sample t-test, two-tailed\n    p: 0.001\n    p_relation: \"<\"\n    n: all sessions\n  criterion: The per-session peak difference of the header (Breath-to-lick timing, code\n    get_peak_diff_breath_behv), slow minus fast; one-sample two-tailed t-test against 0 under\n    O4 (a) and (b). Reproduced when the mean is positive with p < 0.001 under a reading.\n- id: ed1-unidirectional-models-fail\n  statement: Neither a free-running breathing oscillator that sets lick timing nor a\n    free-running licking oscillator that sets breath timing reproduces the observed lick-breath\n    relationship, so the two oscillators are bidirectionally coupled.\n  source: Results, Coordination of breathing, licking, and swallowing, paragraph 4; Extended\n    Data Figure 1d-i; Methods, Simulation of licking-breathing coupling\n  quote: This pattern of lick-breath temporal relationship also cannot be produced by a\n    free-running licking oscillator unidirectionally setting the timing of breathing rhythm\n  depends_on:\n  - fig1g-lick-delayed-before-slow-breath\n  - fig1i-breath-delayed-before-slow-lick\n  criterion: Simulate as the Methods say, drawing intervals from the empirical frequency\n    distributions of fig1d-lick-breath-frequencies, Gaussian timing noise SD 10 ms. The fixed\n    latency is the median latency from the last lick to the next inspiration (breathing model)\n    and from the last inspiration to the next lick (licking model) in the data; the number of\n    simulated cycles matches the pooled data. Apply the two peak-difference measures of the\n    header to each simulation. Reproduced when the breathing-driven model gives a Fig 1i\n    difference whose mean is not positive or not significant (two-tailed t-test over simulated\n    sessions of the data's sizes, p >= 0.05) and the licking-driven model fails likewise on\n    the Fig 1g measure, while the data give both differences positive.\n- id: ed2-rats-similar\n  statement: Licking and breathing in freely moving rats showed a similar lick-breath temporal\n    relationship.\n  source: Results, Coordination of breathing, licking, and swallowing, paragraph 4; Extended\n    Data Figure 2\n  quote: Independent analysis of breathing and licking in freely moving rats yielded similar\n    temporal relationship (Extended Data Figure 2)\n  criterion: Rat data (7 rats, lickometer contacts, thermocouple inspiration onsets at 10% of\n    onset amplitude after 1-20 Hz filtering, Methods). Licks from bouts shorter than 1.75 s\n    left out as the Methods say. The two peak-difference measures of the header computed per\n    rat with tongue contacts as licks. Reproduced when both differences are positive in a\n    majority of rats and positive on average (one-sample t-test over rats, two-tailed,\n    p < 0.05, a standard choice named here since the paper reports no test).\n- id: ed1bc-licks-pause-at-swallows\n  statement: Licking was paused during detected swallows but not during ordinary expirations,\n    so the detected events are genuine swallows.\n  source: Extended Data Figure 1b-c; Results, Coordination of breathing, licking, and\n    swallowing, paragraph 1\n  quote: Licking was paused during swallowing. Bottom, lick timing aligned to all expirations as a\n    control. Lick was not paused during expiration.\n  criterion: Swallows detected as in the header. Per session, the probability of a tongue onset\n    in 3.4 ms bins from -0.3 to 0.3 s around swallow onsets and around all expiration onsets\n    (Hilbert phase pi) inside lick bouts. Reproduced when the mean lick probability from 0 to\n    100 ms after onset is lower around swallows than around expirations in most sessions with\n    at least 20 swallows, by a paired Wilcoxon signed-rank test, p < 0.05 (a standard choice,\n    named here).\n- id: fig1k-rhythms-follow-swallow-at-fixed-latency\n  statement: Inspirations and licks followed swallowing at relatively fixed latencies despite\n    different breath and lick timing before the swallow, so swallowing interrupted the ongoing\n    rhythms.\n  source: Results, Coordination of breathing, licking, and swallowing, paragraph 5; Figure 1k and\n    1m\n  quote: Inspirations and licks followed swallowing at relatively fixed latencies despite\n    different breath and lick timing before the swallow (Figure 1k and m)\n  criterion: Swallow events and ranking as in O5 (a) and (b). For licks and for breaths\n    separately, reproduced when the difference in median latency from swallow onset to the\n    first following lick (inspiration) between the top and bottom thirds is smaller than the\n    difference in their median cycle -1 (as Figure 1k right compares the two thirds) under a\n    reading.\n- id: fig1l-lick-interval-preserved\n  statement: The inter-lick interval before and after swallowing was preserved (one-sample\n    t-test, two-tailed, P = 0.649).\n  source: Results, Coordination of breathing, licking, and swallowing, paragraph 5; Figure 1l\n  quote: The inter-lick-interval before and after swallowing was preserved (Figure 1l, P=0.649,\n    one-sampled t-test, two-tailed)\n  statistics:\n  - about: Delta(1,-1), cycle 1 minus cycle -1\n    test: one-sampled t-test, two-tailed\n    p: 0.649\n  criterion: A claim of absence, judged on the paper's test. Delta(1,-1) per swallow event as\n    in the header, bottom third by O5 (a), the code's selection, pooled across sessions.\n    Reproduced when the one-sample two-tailed t-test against 0 gives p >= 0.05; not reproduced\n    when p < 0.05. The mean Delta(1,-1) is reported, and O5 (b), (c) and (d) are shown as\n    variants.\n- id: fig1l-lick-cycle-prolonged\n  statement: The lick cycle in which swallowing occurred was significantly prolonged, by 33.3 ms\n    (one-sample t-test, two-tailed, P < 0.001).\n  source: Results, Coordination of breathing, licking, and swallowing, paragraph 5; Figure 1l\n  quote: whereas the lick cycle in which swallowing occurred was significantly prolonged by 33.3 ms\n    (Figure 1l, P<0.001, one-sampled t-test, two-tailed)\n  statistics:\n  - about: Delta(0,-1), cycle 0 minus cycle -1\n    test: one-sampled t-test, two-tailed\n    p: 0.001\n    p_relation: \"<\"\n  expected:\n    quantity: mean Delta(0,-1) for licks\n    value: 33.3\n    tolerance: 3.3\n    unit: ms\n  criterion: Delta(0,-1) per swallow event, readings O5 (a) to (d). Reproduced when, under one\n    reading, the mean is within tolerance and the one-sample two-tailed t-test gives p < 0.001;\n    partially reproduced when the test holds and the mean is outside tolerance under every\n    reading. Under O5 (a) the selection of the longest cycles 0 favours a positive Delta(0,-1);\n    the result under (b) and (c) is reported beside it.\n- id: fig1n-breath-interval-preserved\n  statement: The inter-breath interval before and after swallowing was preserved (P = 0.225).\n  source: Results, Coordination of breathing, licking, and swallowing, paragraph 5; Figure 1n\n  quote: P=0.225 for inter-breath-interval before vs. after swallowing\n  statistics:\n  - about: Delta(1,-1) for breaths\n    test: one-sample t-test, two-tailed\n    p: 0.225\n  criterion: A claim of absence, judged on the paper's test, as fig1l-lick-interval-preserved\n    with inspiration onsets and the breath limits of the header (cycle 0 between 1/15 and 1/2 s).\n    Reproduced when p >= 0.05 under O5 (a); not reproduced when p < 0.05. The other readings\n    are variants.\n- id: fig1n-breath-cycle-prolonged\n  statement: The breath cycle in which swallowing occurred was significantly prolonged, by 48.0\n    ms (one-sample t-test, two-tailed, P < 0.001).\n  source: Results, Coordination of breathing, licking, and swallowing, paragraph 5; Figure 1n\n  quote: P<0.001 for inter-breath-interval in which swallowing occurred, one-sample t-test,\n    two-tailed, prolonged by 48.0 ms\n  statistics:\n  - about: Delta(0,-1) for breaths\n    test: one-sample t-test, two-tailed\n    p: 0.001\n    p_relation: \"<\"\n  expected:\n    quantity: mean Delta(0,-1) for breaths\n    value: 48.0\n    tolerance: 4.8\n    unit: ms\n  criterion: As fig1l-lick-cycle-prolonged, with breaths.\n- id: units-count\n  statement: Across 339 insertions in 31 mice, 20,300 single units passed quality control (60 +-\n    22 per probe), 5,700 in the cerebellum, 3,700 in the pons and 10,900 in the medulla.\n  source: Results, Brainstem activity maps of orofacial rhythms, paragraph 2; Methods,\n    Preprocessing, spike sorting, and quality metrics, paragraph 2\n  quote: we obtained 20,300 clear single units, including 5,700 units in the cerebellum, 3,700\n    units in the pons, and 10,900 units in the medulla\n  expected:\n  - quantity: single units after quality control\n    value: 20300\n    tolerance: 2030\n  - quantity: units per probe, mean\n    value: 60\n    tolerance: 6\n  - quantity: units in the cerebellum\n    value: 5700\n    tolerance: 570\n  - quantity: units in the pons\n    value: 3700\n    tolerance: 370\n  - quantity: units in the medulla\n    value: 10900\n    tolerance: 1090\n  - quantity: probe insertions\n    value: 339\n    tolerance: 0\n  - quantity: mice\n    value: 31\n    tolerance: 0\n  criterion: Units by the quality filter of the header, V1 both ways; region from the unit's\n    CCF label (cerebellum CB, pons P, medulla MY, with their subregions). Insertions and mice\n    are counted exactly. Extended Data Figure 4c gives 19,000 units with amplitude > 150 uV,\n    a second reading of the total; a count within tolerance of either is reported as such.\n- id: region-spike-rates\n  statement: Neurons in the cerebellum (22 +- 29 spikes/s) and vestibular nucleus (38 +- 32)\n    fired faster than neurons in the medulla (11 +- 14).\n  source: Methods, Preprocessing, spike sorting, and quality metrics, paragraph 2; Figure 2e\n  quote: Neurons in the cerebellum and the vestibular nucleus exhibited higher spike rates than\n    neurons in the medulla (22 ± 29 spikes/s, mean ± std, for cerebellum, 38 ± 32 spikes/s for\n    vestibular nucleus, and 11 ± 14 spikes/s for medulla\n  depends_on:\n  - units-count\n  expected:\n  - quantity: mean rate, cerebellum\n    value: 22\n    tolerance: 2.2\n    unit: spikes/s\n  - quantity: mean rate, vestibular nucleus\n    value: 38\n    tolerance: 3.8\n    unit: spikes/s\n  - quantity: mean rate, medulla\n    value: 11\n    tolerance: 1.1\n    unit: spikes/s\n  criterion: The rate is not defined; readings (a) the quality metric avg_firing_rate; (b) spikes\n    over the session's trial time. Vestibular nucleus is the CCF VNC; medulla is MY with (i)\n    and (ii) without VNC. Reproduced when the three means are within tolerance under one\n    reading.\n- id: fig2-licking-breathing-tuned-counts\n  statement: Units showed significant phase tuning to licking (3551 of 20,300) or breathing\n    (1015 of 20,300), but rarely to both (182 of 20,300).\n  source: Results, Brainstem activity maps of orofacial rhythms, paragraph 3\n  quote: Individual units exhibited significant phase tuning to either licking (3551/20300), or\n    breathing (1015/20300), but rarely to both (182/20300)\n  depends_on:\n  - units-count\n  expected:\n  - quantity: licking-tuned units\n    value: 3551\n    tolerance: 355\n  - quantity: breathing-tuned units\n    value: 1015\n    tolerance: 102\n  - quantity: units tuned to both\n    value: 182\n    tolerance: 18\n  criterion: Phase tuning and MI as in the header, tuned at P < 0.001 and MI > 0.6, readings V2\n    (a) and (b) and V3 (a) and (b). Reproduced when the three counts are within tolerance under\n    one reading; partially reproduced when the counts are not but both-tuned units are under\n    10% of licking-tuned units and under 25% of breathing-tuned units (the proportions the\n    Methods say were robust), under one reading. The code's choices (order 5, 100 resamples)\n    are shown as variants.\n- id: fig2-swallow-modulated-counts\n  statement: Of 18,485 units, 427 were modulated by swallowing only, 175 by both licking and\n    swallowing and 55 by both breathing and swallowing.\n  source: Results, Brainstem activity maps of orofacial rhythms, paragraph 3; Extended Data\n    Figure 5e-f\n  quote: Most units were modulated by swallowing only (427/18485), with a smaller group modulated\n    by both licking and swallowing (175/18485) (Extended Data Figure 5f). Another small subset of\n    units with swallowing-related activity were also modulated by breathing (55/18485)\n  depends_on:\n  - fig2-licking-breathing-tuned-counts\n  expected:\n  - quantity: units in the swallow analysis\n    value: 18485\n    tolerance: 1849\n  - quantity: swallow-only units\n    value: 427\n    tolerance: 43\n  - quantity: licking and swallowing units\n    value: 175\n    tolerance: 18\n  - quantity: breathing and swallowing units\n    value: 55\n    tolerance: 6\n  criterion: Swallow modulation as in the header, readings V4 (a) and (b). The denominator\n    18,485 is not defined; readings (a) units of sessions with at least one detected swallow;\n    (b) units with at least 20 swallows (code). \"Swallowing only\" is read (i) not licking- or\n    breathing-tuned; (ii) not licking-tuned. Reproduced when the four numbers are within\n    tolerance under one reading.\n- id: fig2f-breathing-units-location\n  statement: Units encoding breathing clustered near the preBotzinger complex and in the\n    posterior ventral IRN.\n  source: Results, Brainstem activity maps of orofacial rhythms, paragraph 4; Figure 2f\n  quote: Units encoding breathing were near the preBötzinger complex 22, as well as posterior\n    ventral IRN\n  depends_on:\n  - fig2-licking-breathing-tuned-counts\n  criterion: The paper shows a map and gives no test. Regions by O3 (a) and (b). Reproduced when\n    the fraction of breathing-tuned units among the units of each of the two regions exceeds\n    the fraction among all pons and medulla units, each by a one-sided Fisher exact test at\n    p < 0.05 (a standard choice, named here), under one reading.\n- id: fig2g-licking-units-location\n  statement: Licking-related units were broadly distributed, including the hypoglossal (12N) and\n    trigeminal (5N) motor nuclei, extensive portions of the IRN and parts of the pons.\n  source: Results, Brainstem activity maps of orofacial rhythms, paragraph 4; Figure 2g\n  quote: The regions containing licking-related activity were remarkably broad, including the\n    tongue- and jaw-related motor nuclei (hypoglossal nucleus, 12N; trigeminal nucleus, 5N) as\n    well as extensive portions of the IRN and parts of pons\n  depends_on:\n  - fig2-licking-breathing-tuned-counts\n  criterion: As fig2f-breathing-units-location, with licking-tuned units and the CCF regions XII,\n    V and IRN, and the pons taken whole (P). Reproduced when the fraction exceeds that of all\n    pons and medulla units in XII, V and IRN (Fisher exact, one-sided, p < 0.05) and licking\n    units are present in the pons at more than 1% of its units.\n- id: fig2h-swallow-units-location\n  statement: Swallowing-related units clustered in the trigeminal nucleus (5N), lateral to the\n    nucleus of the solitary tract (NTS) and above the nucleus ambiguus (10N), with further\n    clusters in the inferior colliculus and the nucleus of the lateral lemniscus.\n  source: Results, Brainstem activity maps of orofacial rhythms, paragraph 4; Figure 2h; Extended\n    Data Figure 6a-d\n  quote: Units with swallowing-related activity were clustered in the trigeminal nucleus (5N),\n    lateral to the nucleus of the solitary tract (NTS), and above the nucleus ambiguus (10N)\n  depends_on:\n  - fig2-swallow-modulated-counts\n  criterion: As fig2f-breathing-units-location, with swallow-modulated units. Regions are CCF\n    V, IC and NLL; \"lateral to NTS\" is units within (a) 300 um or (b) 500 um lateral of NTS at\n    its AP extent; \"above 10N\" is units within the same distances dorsal of AMB. Reproduced\n    when the fraction exceeds that of all units of the same sessions in all five regions under\n    one reading; partially reproduced in three or four.\n- id: ed6e-swallow-latencies\n  statement: Swallow-related activity in 5N and IRN leads swallowing, while activity in the\n    inferior colliculus and nucleus of the lateral lemniscus follows it.\n  source: Extended Data Figure 6e; Results, Brainstem activity maps of orofacial rhythms,\n    paragraph 4\n  quote: Activities in 5N and IRN lead swallowing while activities in the IC and NLL follow\n    swallowing.\n  depends_on:\n  - fig2-swallow-modulated-counts\n  criterion: Swallow PSTHs as in the code (1 ms bins, 50 ms boxcar, -1 to 1 s). Per\n    swallow-modulated unit, the time of the PSTH peak within -0.15 to 0.15 s. Reproduced when the\n    median peak time is negative for units in V and IRN and positive for units in IC and NLL,\n    and the two groups differ by a two-sided Mann-Whitney test at p < 0.05 (a standard choice,\n    named here).\n- id: ed7-glm-separate-clusters\n  statement: A GLM on the tracked features found separate clusters of units predicted by\n    licking or by breathing movements.\n  source: Results, Brainstem activity maps of orofacial rhythms, paragraph 5; Extended Data\n    Figure 7c-d\n  quote: The GLM found separate clusters of units predicted by either licking or breathing\n    movement (Extended Data Figure 7c-d)\n  criterion: The GLM of the Methods (17 ms bins, jaw and tongue x, y, z and airflow, z-scored,\n    tongue set to 0 when its likelihood is below 0.05 in both views, every 5th trial held out,\n    lags of +-5 bins), readings O8. Reproduced when units whose largest absolute weight is on\n    airflow and units whose largest is on a jaw or tongue regressor are spatially distinct:\n    the median CCF position of the first lies ventral and posterior to that of the second, and\n    the two sets overlap in fewer than 25% of units with VAF > 0.05 (a standard choice, named\n    here).\n- id: ed7g-cae-better-than-features\n  statement: The autoencoder embedding predicted a larger fraction of activity variance than the\n    tracked features for most units across the brainstem (Wilcoxon signed-rank test, P <\n    0.001).\n  source: Results, Brainstem activity maps of orofacial rhythms, paragraph 6; Extended Data\n    Figure 7g\n  quote: The CAE predicted a larger fraction of activity variance than the tracked features for\n    most units across the brainstem (Extended Data Figure 7g; CAE vs. features, P<0.001,\n    Wilcoxon signed rank test)\n  statistics:\n  - test: Wilcoxon signed rank test\n    p: 0.001\n    p_relation: \"<\"\n  criterion: CAE as in reference 40 and the Methods (two residual blocks of three convolutions,\n    linear readouts of 128 and 32, frames downsampled to 120 x 112, one network per mouse\n    trained on 80% of trials for 20,000 iterations with L2 regularization), which needs the\n    raw videos; GLM readings O8. Reproduced when, over all units, CAE VAF exceeds feature VAF\n    in more than half of the units and the paired Wilcoxon signed-rank test gives P < 0.001.\n- id: ed7h-prebotc-exception\n  statement: Units in the preBotzinger complex were the exception, where the autoencoder gave\n    worse predictions than the tracked features (Wilcoxon signed-rank test, P < 0.001).\n  source: Results, Brainstem activity maps of orofacial rhythms, paragraph 6; Extended Data\n    Figure 7g-h\n  quote: the only exceptions were units in the preBötzinger complex where activity prediction\n    using CAE led to worse predictions (CAE vs. features, P<0.001, Wilcoxon signed rank test\n  statistics:\n  - test: Wilcoxon signed rank test\n    p: 0.001\n    p_relation: \"<\"\n  depends_on:\n  - ed7g-cae-better-than-features\n  criterion: As ed7g-cae-better-than-features, for units near the preBotzinger complex (O3 (a)\n    and (b)), and for breathing-tuned units there (Extended Data Fig 7g marks breathing units).\n    Reproduced when feature VAF exceeds CAE VAF with P < 0.001 under one reading.\n- id: ed8bc-prebotc-inspiration-phase\n  statement: Breathing-related units in the preBotzinger complex preferentially fired at the\n    inspiration phase of breathing.\n  source: Results, Brainstem activity maps of orofacial rhythms, paragraph 5; Extended Data\n    Figure 8a-c\n  quote: units in the preBötzinger complex preferentially fired at inspiration phase of breathing\n  depends_on:\n  - fig2-licking-breathing-tuned-counts\n  criterion: Preferred phases of the fitted tuning curves (header), breathing units by O1 (b)\n    as Extended Data Fig 8b states, located by O3 (a) and (b). Inspiration phase is the half\n    cycle starting at inspiration onset (phase 0 to pi in the convention where inspiration\n    onset is 0). Reproduced when more than half of those units prefer that half cycle and their\n    phases are non-uniform by a Rayleigh test at p < 0.05 (a standard choice, named here).\n- id: ed8e-licking-units-protrusion\n  statement: Licking-related units were mostly active when the tongue was fully protruded.\n  source: Results, Brainstem activity maps of orofacial rhythms, paragraph 5; Extended Data\n    Figure 8d-f\n  quote: Units with licking-related activity were mostly active when the tongue was in the fully\n    protruded state\n  depends_on:\n  - fig2-licking-breathing-tuned-counts\n  criterion: Licking units by O1 (b). For each session, the jaw phase at the frame of maximal\n    tongue protrusion in each lick (the frame of largest 3D tongue distance from its onset\n    position) gives the protrusion phase; a unit's preferred phase is compared with its\n    session's median protrusion phase. Reproduced when more than half of licking units prefer\n    a phase within pi/2 of it.\n- id: ed8i-ipsilateral-lick-selectivity\n  statement: Licking-related neurons showed selectivity for ipsilateral licking, while\n    individual units within each hemisphere had diverse direction preferences, including the\n    center direction.\n  source: Results, Brainstem activity maps of orofacial rhythms, paragraph 7; Extended Data\n    Figure 8g-i\n  quote: Overall, licking-related neurons showed selectivity for ipsilateral licking (Extended Data\n    Figure 8i)\n  depends_on:\n  - fig2-licking-breathing-tuned-counts\n  criterion: Lick angle by O9 (a) and (b); spikes from -50 to 100 ms around each lick onset\n    (Extended Data Fig 8g); left and right licks are those with angle below and above the\n    midline. Per licking unit (O1 (a)), left-lick rate minus right-lick rate. Reproduced when\n    this difference is larger for left-hemisphere than right-hemisphere units (CCF medial-\n    lateral position against the midline) by a one-sided Mann-Whitney test at p < 0.05 (a\n    standard choice, named here) and each hemisphere's median favours the ipsilateral side,\n    under one reading.\n- id: ed4c-licking-map-insensitive-to-sorting\n  statement: The licking activity map was insensitive to spike-sorting quality; raising the\n    amplitude threshold from 150 to 500 uV left 2223 of 19,000 units and the same map.\n  source: Extended Data Figure 4c; Results, Brainstem activity maps of orofacial rhythms,\n    paragraph 2\n  quote: Licking activity map was insensitive to the quality of spike sorting. To obtain units with\n    the highest amplitude, the waveform amplitude quality metric was increased from 150 μV to\n    500 μV. This filtered the 19,000 units with amplitude > 150 μV to 2223 unit with amplitude >\n    500 μV.\n  depends_on:\n  - fig2-licking-breathing-tuned-counts\n  expected:\n    quantity: units with amplitude above 500 uV\n    value: 2223\n    tolerance: 222\n  criterion: Units passing the filter of the header with amplitude > 500 uV. Reproduced when the\n    count is within tolerance and, over CCF regions with at least 20 such units, the mean\n    licking MI per region in this subset correlates with that in all units (Spearman, p < 0.05,\n    positive; a standard choice, named here). The paper's 19,000 against 20,300 units is not\n    resolved here; both are reported.\n- id: fig3a-premotor-regions\n  statement: Premotor neurons of the masseter and genioglossus occupied largely distinct regions\n    of the pons and medulla, overlapping in the dorsal IRN.\n  source: Results, A licking premotor network with autonomous rhythm-generation properties,\n    paragraph 3; Figure 3a; Extended Data Figure 9a-b\n  quote: Premotor neurons for the masseter and genioglossus muscles occupied largely distinct\n    regions of the pons and medulla, with some overlap in the dorsal IRN (Figure 3a)\n  data: elsewhere\n  where: Takatoh et al. 2021, eLife 10:e67291, doi:10.7554/eLife.67291 (reference 43); the paper\n    gives no archive identifier for the mapped neurons\n  criterion: Not testable on the dandiset. From the premotor neuron positions in CCF, the density\n    contours of Extended Data Fig 9a (0.0063 and 0.0019 neurons per mm3); reproduced when the\n    overlap of the two contours is under half of the smaller and lies in IRN dorsal to its DV\n    midpoint.\n- id: fig3b-licking-units-in-premotor-regions\n  statement: Units inside the tongue-jaw premotor regions showed significantly higher licking\n    modulation than position-shuffled populations (Wilcoxon rank-sum test, P < 0.001).\n  source: Results, A licking premotor network with autonomous rhythm-generation properties,\n    paragraph 3; Figure 3b\n  quote: Units inside these regions showed significantly higher licking modulation compared to\n    position-shuffled populations (P < 0.001 Wilcoxon rank sum test)\n  statistics:\n  - test: Wilcoxon rank sum test\n    p: 0.001\n    p_relation: \"<\"\n  data: with_inputs\n  depends_on:\n  - fig2-licking-breathing-tuned-counts\n  criterion: Premotor regions are the union of the two density contours of Extended Data Fig 9a\n    built from reference 43's premotor neurons. Position shuffling is not described; readings\n    (a) licking MI of units inside against the MIs of the same number of units drawn at random\n    from all units (positions shuffled across units); (b) inside against outside. Reproduced\n    when the inside MIs are higher with rank-sum P < 0.001 under one reading.\n- id: fig3ce-descending-stimulation-rhythmic-licking\n  statement: Photostimulation of ALM (n = 11 mice) or latSC (n = 3 mice) elicited sustained\n    rhythmic licking at the naturalistic 7 Hz frequency.\n  source: Results, A licking premotor network with autonomous rhythm-generation properties,\n    paragraph 4; Figure 3c and 3e\n  quote: Photostimulation of ALM or latSC (20 or 40 Hz pulse trains for 2 or 1.3 s) elicited\n    sustained rhythmic licking at the naturalistic 7 Hz frequency (Figure 3c and e)\n  expected:\n    quantity: lick rate during photostimulation\n    value: 7\n    tolerance: 0.7\n    unit: Hz\n  criterion: Photostimulation trials of the ALM mice (cued licking task) and latSC mice. Lick\n    rate as tongue onsets per second from the first lick to the end of the light, mean per\n    mouse then across mice. Reproduced when the mean across mice is within tolerance for each\n    group and licking lasts to the end of the light in most trials (a lick in the last 300 ms).\n- id: fig3dfh-projections-and-rhythm-site\n  statement: ALM and latSC axons targeted the contralateral brainstem and engulfed the\n    tongue-jaw premotor regions; constant photostimulation of Phox2b+ neurons in the\n    posterior-dorsal IRN/PARN elicited rhythmic licking, while anterior sites locked the jaw.\n  source: Results, A licking premotor network with autonomous rhythm-generation properties,\n    paragraphs 4 and 5; Figure 3d, 3f, 3g and 3h\n  quote: In contrast, photostimulating a posterior-dorsal region of IRN and the adjacent region in\n    PARN (anterior-lateral to 12N) elicited rhythmic jaw movement and tongue protrusions\n  criterion: Anatomy and fibre-site data, with no stated deposit. For the fibre sites (46 sites,\n    27 mice, Figure 3h), reproduced when the sites classed rhythmic lie posterior and dorsal of\n    those not rhythmic (median CCF AP and DV positions) and within or next to IRN or PARN.\n- id: ed10-site-classes\n  statement: Of the brainstem photostimulation sites, 18 evoked rhythmic jaw movement with a\n    peak at 7 Hz and rhythmic tongue protrusions, 11 evoked no rhythmic jaw movement and 4\n    evoked only a transient tongue protrusion.\n  source: Extended Data Figure 10b, 10e and 10h\n  inferred: The counts 18, 11 and 4 are in three legends; no sentence gives them together.\n  expected:\n  - quantity: sites with rhythmic jaw movement\n    value: 18\n    tolerance: 2\n  - quantity: sites without rhythmic jaw movement\n    value: 11\n    tolerance: 1\n  - quantity: sites with transient tongue protrusion\n    value: 4\n    tolerance: 0\n  - quantity: jaw movement frequency peak at rhythmic sites\n    value: 7\n    tolerance: 0.7\n    unit: Hz\n  criterion: Jaw position Fourier spectrum during the 2 s of light (Extended Data Fig 10b).\n    Sites are classed rhythmic when the spectrum has a peak between 3 and 15 Hz (the jaw band\n    of the Methods) higher than in the 2 s before the light; classing rules beyond that are not\n    given. Reproduced when the counts are within tolerance and the peak of the mean spectrum of\n    rhythmic sites is within tolerance.\n- id: fig4b-artificial-licking-keeps-lick-timing\n  statement: During ALM-induced licking the lick-breath relationship of voluntary licking was\n    recapitulated; lick timing anticipated the next breath at a fixed latency across breathing\n    frequencies.\n  source: Results, Coupled brainstem oscillators autonomously coordinate licking and breathing,\n    paragraph 2; Figure 4b\n  quote: Notably, the same lick-breath temporal relationship was recapitulated during artificially\n    induced licking. Lick timing anticipated the next breath and proceeded inspiration at a fixed\n    latency across different breathing frequencies (Figure 4b)\n  criterion: Cued licking task of the ALM mice. The Fig 1g measure (header) on photostimulation\n    trials (licks during the 2 s light) and on Go-cue trials separately, pooled per mouse\n    (Figure 4b, \"across all mice\"); session pooling as needed for the minimum of 40 cycles per\n    half. Reproduced when the photostimulation difference is positive on average across mice by\n    a one-sample two-tailed t-test at p < 0.05 (the paper's test of Fig 1g; the threshold is a\n    standard choice, named here).\n- id: fig4c-artificial-licking-breath-timing\n  statement: During ALM-induced licking, inspiration timing was still influenced by future lick\n    timing.\n  source: Results, Coupled brainstem oscillators autonomously coordinate licking and breathing,\n    paragraph 2; Figure 4c\n  quote: Conversely, inspiration timing was influenced by future lick timing (Figure 4c)\n  criterion: As fig4b-artificial-licking-keeps-lick-timing, with the Fig 1i measure of the\n    header.\n- id: ed11b-alm-breathing-rate\n  statement: In a subset of mice, ALM photostimulation also increased breathing rate.\n  source: Results, Coupled brainstem oscillators autonomously coordinate licking and breathing,\n    paragraph 2; Extended Data Figure 11b\n  quote: In a subset of mice, ALM photostimulation also induced an increase in breathing rate\n    (Extended Data Figure 11b)\n  criterion: Breathing rate (inspiration onsets per second) in the 2 s of light against the 1 s\n    before, per photostimulation trial. Reproduced when at least one and fewer than all 11 mice\n    show an increase by a paired two-sided Wilcoxon signed-rank test over trials at p < 0.05\n    (a standard choice, named here).\n- id: fig4e-licking-units-anticipate-breath\n  statement: Preceding a slower breath, the activity of licking neurons was slowed in\n    anticipation of the next inspiration.\n  source: Results, Coupled brainstem oscillators autonomously coordinate licking and breathing,\n    paragraph 3; Figure 4e\n  quote: Preceding a slower breath, the activity of licking neurons was slowed in anticipation of\n    the next inspiration (Figure 4e)\n  depends_on:\n  - fig2-licking-breathing-tuned-counts\n  criterion: The unit peak difference of the header (code get_peak_diff_lick_unit), slow minus\n    fast, per licking unit, units by O1 and recordings by O2. The legend says \"Same as b\", the\n    test of Fig 1g; one-sample two-tailed t-test over units at p < 0.05 (threshold a standard\n    choice, named here). Reproduced when the mean is positive and significant under all\n    readings; blocked as methods_underspecified when the readings disagree.\n- id: fig4f-breathing-units-anticipate-lick\n  statement: Preceding a slower lick, the activity of breathing neurons was slowed in\n    anticipation of the upcoming lick.\n  source: Results, Coupled brainstem oscillators autonomously coordinate licking and breathing,\n    paragraph 3; Figure 4f\n  quote: Preceding a slower lick, the activity of breathing neurons was slowed in anticipation of\n    the upcoming lick (Figure 4f)\n  depends_on:\n  - fig2-licking-breathing-tuned-counts\n  criterion: As fig4e-licking-units-anticipate-breath, with breathing units and the code's\n    get_peak_diff_breath_unit.\n- id: fig4d-simultaneous-recordings\n  statement: Licking and breathing oscillators were recorded simultaneously in 43 recordings from\n    21 mice, with 1 to 28 licking-related and 1 to 12 breathing-related units per recording.\n  source: Results, Coupled brainstem oscillators autonomously coordinate licking and breathing,\n    paragraph 3; Figure 4d\n  quote: 43 recordings in 21 mice; 1-28 licking-related units and 1-12 breathing-related units per\n    recording\n  expected:\n  - quantity: simultaneous recordings\n    value: 43\n    tolerance: 4\n  - quantity: mice with simultaneous recordings\n    value: 21\n    tolerance: 2\n  criterion: Recordings with two probes, one with licking units (O1) in the posterior-dorsal\n    IRN/PARN and one with breathing units near the preBotzinger complex (O3). Reproduced when\n    the counts are within tolerance and the unit ranges per recording are within 1 to 28 and 1\n    to 12 widened by 10%, under one reading.\n- id: fig4g-licking-breathing-pairs-correlated\n  statement: Activity of simultaneously recorded breathing and licking units was significantly\n    correlated for most pairs compared to trial-shuffled controls (103 of 119 pairs; 43\n    positively correlated, 60 anticorrelated).\n  source: Results, Coupled brainstem oscillators autonomously coordinate licking and breathing,\n    paragraph 4; Figure 4g\n  quote: Activity was significantly correlated for most pairs compared to trial-shuffled controls\n    (Figure 4g; 103/119 pairs with significant cross-correlation relative to shuffled control, 43\n    positively correlated, 60 anticorrelated\n  depends_on:\n  - fig4d-simultaneous-recordings\n  expected:\n  - quantity: pairs\n    value: 119\n    tolerance: 12\n  - quantity: significant pairs\n    value: 103\n    tolerance: 10\n  - quantity: positively correlated pairs\n    value: 43\n    tolerance: 4\n  - quantity: anticorrelated pairs\n    value: 60\n    tolerance: 6\n  criterion: Pairs from fig4d-simultaneous-recordings; correlograms by O6. Reproduced when, under\n    one reading, the four counts are within tolerance; partially reproduced when more than\n    three quarters of pairs are significant with anticorrelated pairs outnumbering positive\n    ones.\n- id: fig4g-symmetric-lags\n  statement: The cross-correlation was temporally symmetric; breathing units lagged licking units\n    for 57 pairs, licking units lagged breathing units for 34 pairs, and 12 pairs peaked at zero.\n  source: Results, Coupled brainstem oscillators autonomously coordinate licking and breathing,\n    paragraph 4\n  quote: breathing units lagged licking units for 57 pairs, while other licking units lagged\n    breathing units for 34 pairs, (the remaining 12 pairs had cross-correlation peak at 0)\n  depends_on:\n  - fig4g-licking-breathing-pairs-correlated\n  expected:\n  - quantity: pairs with breathing unit lagging\n    value: 57\n    tolerance: 6\n  - quantity: pairs with licking unit lagging\n    value: 34\n    tolerance: 3\n  - quantity: pairs peaking at 0\n    value: 12\n    tolerance: 1\n  criterion: Significant pairs and lags by O6. Reproduced when the three counts are within\n    tolerance under one reading; partially reproduced when both lag directions each hold at\n    least a quarter of significant pairs.\n- id: ed12c-correlation-without-licking\n  statement: Significant cross-correlation between licking and breathing unit pairs was observed\n    even when mice were not licking.\n  source: Results, Coupled brainstem oscillators autonomously coordinate licking and breathing,\n    paragraph 4; Extended Data Figure 12c\n  quote: Notably, significant cross-correlation between the unit pairs was observed even when mice\n    were not licking, i.e. when the licking oscillator was inactive (Extended Data Figure 12c)\n  depends_on:\n  - fig4g-licking-breathing-pairs-correlated\n  criterion: As fig4g-licking-breathing-pairs-correlated, on the baseline of the cued licking\n    task (trial start to Go cue, no tongue detected; Extended Data Fig 12c). Reproduced when\n    more than half of the pairs are significant under one reading of O6.\n- id: fig4h-fewer-correlations-outside-oscillator\n  statement: Units outside the licking oscillator were less often cross-correlated with breathing\n    units (54 of 110 pairs), a significantly lower proportion than licking-breathing oscillator\n    pairs (Chi-square test, p < 0.0001).\n  source: Results, Coupled brainstem oscillators autonomously coordinate licking and breathing,\n    paragraph 4; Figure 4h\n  quote: units outside of the licking oscillator exhibited less cross correlation with the\n    breathing units (Figure 4h; 54/110 pairs with significant cross correlation; a significantly\n    lower proportion compared to licking-breathing oscillator unit pairs, p<0.0001, Chi-square\n    test)\n  statistics:\n  - test: Chi-square test\n    p: 0.0001\n    p_relation: \"<\"\n    n: 110 and 119 pairs\n  depends_on:\n  - fig4g-licking-breathing-pairs-correlated\n  expected:\n  - quantity: pairs with a non-licking unit\n    value: 110\n    tolerance: 11\n  - quantity: significant pairs with a non-licking unit\n    value: 54\n    tolerance: 5\n  criterion: Non-licking units are not defined; readings (a) units of the licking-oscillator\n    probe not licking-tuned (O1); (b) units of that probe outside the posterior-dorsal IRN/PARN\n    (O3). Correlograms by O6. Chi-square test on the 2 x 2 table of significant and not\n    significant pairs, without continuity correction (i) and with it (ii). Reproduced when the\n    proportion is lower with p < 0.0001 under one reading; the counts are reported against the\n    expected values.\n- id: fig5b-voluntary-lick-latency\n  statement: Mice initiated licking 127.6 +- 29.6 ms after the Go cue (mean +- std across mice,\n    n = 11).\n  source: Results, Descending control patterns oscillators at movement initiation, paragraph 2;\n    Figure 5a-b\n  quote: Mice initiated licking 127.6 ± 29.6 ms after the Go cue onset (defined as the onset of\n    tongue appearance in the video, mean ± std across mice, n=11 mice\n  expected:\n    quantity: lick latency after Go cue, mean across mice\n    value: 127.6\n    tolerance: 12.8\n    unit: ms\n  criterion: Cued licking task, Go-cue trials, first tongue onset after the cue within the 0.5 s\n    response window; mean per mouse, then mean across the 11 mice.\n- id: fig5c-preemptive-breath-adjustment\n  statement: Before voluntary licking, breathing phase deviated from random 115 +- 19 ms before\n    lick onset and became entrained to a phase that put expiration at the first lick (two-sample\n    Kuiper test with Bonferroni correction, p < 0.0001).\n  source: Results, Descending control patterns oscillators at movement initiation, paragraph 2;\n    Figure 5c\n  quote: 115 ± 19 ms before licking onset (mean ± s.e.m., bootstrap), breathing phase began to\n    deviate significantly from random distribution and became entrained to a specific phase\n    (Figure 5c; p<0.0001, two sample Kuiper test with Bonferroni correction)\n  statistics:\n  - test: two sample Kuiper test\n    p: 0.0001\n    p_relation: \"<\"\n    corrected: Bonferroni\n  expected:\n    quantity: onset of breathing-phase entrainment before voluntary lick onset\n    value: 115\n    tolerance: 19\n    unit: ms\n  criterion: Go-cue trials of the cued licking task; breathing phase (Hilbert, header) aligned to\n    the first lick; test and latency by O7 (a) and (b). Reproduced when, under one reading, the\n    latency is within tolerance and the phase at lick onset lies in expiration (phase pi to 2\n    pi).\n- id: fig5e-photostim-lick-latency-longer\n  statement: ALM photostimulation evoked licking with a latency of 230.7 +- 31.5 ms, significantly\n    longer than voluntary licking (paired t-test, two-tailed, p < 0.001).\n  source: Results, Descending control patterns oscillators at movement initiation, paragraph 3;\n    Figure 5e\n  quote: Photostimulation evoked licking with a latency of 230.7 ± 31.5 ms (Figure 5e), which was\n    significantly longer than voluntarily initiated licking (p<0.001, paired t-test, two-tailed)\n  statistics:\n  - test: paired t-test, two-tailed\n    p: 0.001\n    p_relation: \"<\"\n    n: 11 mice\n  expected:\n    quantity: lick latency after photostimulation onset, mean across mice\n    value: 230.7\n    tolerance: 23.1\n    unit: ms\n  depends_on:\n  - fig5b-voluntary-lick-latency\n  criterion: First tongue onset after light onset on photostimulation trials, mean per mouse;\n    paired two-tailed t-test across mice against the Go-cue latencies of\n    fig5b-voluntary-lick-latency. Reproduced when the mean is within tolerance and p < 0.001.\n- id: fig5f-artificial-licking-late-breath-adjustment\n  statement: Artificially induced licking did not recapitulate the pre-emptive breath adjustment;\n    breathing phase changed only 47.6 +- 10 ms before lick onset, a significantly shorter latency\n    than before voluntary licking (bootstrap, P < 0.0001).\n  source: Results, Descending control patterns oscillators at movement initiation, paragraph 3;\n    Figure 5f (the Results also cite a Figure 5g that the legend does not describe)\n  quote: Breathing phase was altered only shortly before licking onset (Figure 5f; 47.6 ± 10 ms),\n    a significantly shorter latency than the pre-emptive adjustment before voluntary licking\n    (Figure 5g; P<0.0001, bootstrap)\n  statistics:\n  - test: bootstrap\n    p: 0.0001\n    p_relation: \"<\"\n  expected:\n    quantity: onset of breathing-phase change before induced lick onset\n    value: 47.6\n    tolerance: 10\n    unit: ms\n  depends_on:\n  - fig5c-preemptive-breath-adjustment\n  criterion: As fig5c-preemptive-breath-adjustment on photostimulation trials, aligned to the\n    first tongue protrusion after light onset. The bootstrap comparison is not described;\n    reading, 10,000 paired resamples of trials in both conditions, p the fraction where the\n    induced latency is at least the voluntary one. Reproduced when, under one reading of O7, the\n    latency is within tolerance and the comparison gives P < 0.0001.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001619/10.1101-2025.01.27.635041.yaml paper/10.1101-2025.01.27.635041.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -nE '\S: ' claims/001619/*.yaml | grep -vE '^[0-9]+:\s*(- )?[a-z_]+: ' | grep -v '^[0-9]*:#'
```

```
188:    occurred at lower frequencies (4.02 ± 1.24 Hz, 95% range: 2.12 - 7.17 Hz; Figure 1d)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "old_string": "  quote: Licking occurred at 6.23 ± 2 Hz (mean ± std, 95% range: 3.59 - 8.91 Hz) while breathing\n    occurred at lower frequencies (4.02 ± 1.24 Hz, 95% range: 2.12 - 7.17 Hz; Figure 1d)",
 "new_string": "  quote: \"Licking occurred at 6.23 ± 2 Hz (mean ± std, 95% range: 3.59 - 8.91 Hz) while breathing\n    occurred at lower frequencies (4.02 ± 1.24 Hz, 95% range: 2.12 - 7.17 Hz; Figure 1d)\""
}
```

```
The file claims/001619/10.1101-2025.01.27.635041.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001619/10.1101-2025.01.27.635041.yaml paper/10.1101-2025.01.27.635041.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -nE '\S:$' claims/001619/*.yaml | grep -vE '^[0-9]+:\s*(- )?[a-z_]+:$'
```

```
579:    airflow and units whose largest is on a jaw or tongue regressor are spatially distinct:
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "old_string": "regressor are spatially distinct:\n    the median",
 "new_string": "regressor are spatially distinct;\n    the median"
}
```

```
The file claims/001619/10.1101-2025.01.27.635041.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001619/10.1101-2025.01.27.635041.yaml paper/10.1101-2025.01.27.635041.txt 2>&1 | tail -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
f=claims/001619/10.1101-2025.01.27.635041.yaml; grep -c '—' $f; grep -ci 'rather' $f; grep -c 'criterion:' $f; grep -c 'statistics:' $f; git status --short
```

```
0
0
48
13
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
?? claims/001619/
?? scripts
```

**Agent**

I wrote the claims file for DANDI:001619: `claims/001619/10.1101-2025.01.27.635041.yaml`. The checker passes with 0 problems. Nothing is committed.

**Text read.** The bioRxiv preprint, version 1 (posted 27 January 2025): main text, the legends of Figures 1 to 5, the Methods, and the supplement with the legends of Extended Data Figures 1 to 12. That supplement was missing in the earlier run, which is why no claims were written then. The two display equations (tuning curve and VAF) are missing from the text, but the words around them name every term. No later version was read.

**Code read.** The paper only says code "will be deposited upon publication". The dandiset description names the analysis code repository, NuoLiLabBCM/KakuEtAl2025, and I read it at commit fbc0abe. It settles these Methods details:
- the unit and trial filters, and lick and inspiration onsets;
- the lick-breath timing analyses (Fig 1f-i, 4e-f);
- the swallow detector and the swallow modulation index;
- phase tuning and the modulation index;
- the activity maps.

It has no statistical tests, and nothing for the GLM, the autoencoder, cross-correlation, the cued-task or photostimulation analyses, or the rats. Its Kuramoto simulations are not described in the preprint, so I didn't use them.

**Counts.**
- 48 claims: 47 findings and one link check.
- 46 claims have quotes. The link check has none, and one is `inferred` (the Extended Data Fig 10 site counts, spread over three legends).
- 13 claims have statistics.
- All 48 have criteria.

**Where the Methods and code disagree.** The Methods version is the main reading; the code's choice is shown as a variant.
- **V1, quality filter:** the code drops the drift-metric threshold.
- **V2, phase filter:** the Methods say "4-pole Butterworth", read as scipy order 4 or order 2; the code uses order 5.
- **V3, significance of the modulation index:** the Methods use 1000 resamples and a rank-sum test; the code uses 100 resamples each side and a one-sided Mann-Whitney. Readings: the code's scheme with 1000 resamples, or the measured index ranked against 1000 random-phase indices.
- **V4, swallow index normalisation:** the mean rate in the swallow window (code), or the PSTH peak.

**Details left open, with the readings named.**
- **O1, tuned-unit threshold:** index > 0.6 (Results) or > 0.9 (Extended Data Fig 8 and the code), with or without the p threshold.
- **O2, recordings for Fig 4e-f:** all sessions (code) or only the 43 simultaneous recordings.
- **O3, regions the Allen atlas doesn't label** (preBötzinger complex, posterior-dorsal or posterior-ventral IRN): within 300 or 500 µm below the nucleus ambiguus, or half-splits of IRN.
- **O4, statistical unit for Fig 1g and 1i:** sessions or mice.
- **O5, ranking of swallow events for Fig 1l and 1n:** by the interval spanning the swallow (code), by the interval before it (text), or all events; plus session means.
- **O6, cross-correlation:** the Results cite a Methods section that doesn't exist. Readings: 5 or 10 ms bins, a trial-shuffle 95% band, and significance with or without Bonferroni.
- **O7, the Kuiper test's second sample:** random-time phases, or phases at −500 ms.
- **O8, GLM:** L1 weight, which lag, and log or logit link.
- **O9, lick angle:** against the jaw at rest (Methods) or the midline (legend).
- Also: how the Fig 1d frequencies were computed, the denominator of 18,485, "position-shuffled", "non-licking units", and the Fig 5g bootstrap.

The paper reports no test for several qualitative claims (locations, ipsilateral preference, preferred phases, Fig 4b-f). Their criteria use a standard test, named in the file as a choice made here.

**Missing from the paper.**
- There is no Figure 5g legend, although the Results cite 5g.
- There is no Methods section for cross-correlation, lick-breath timing or Kuiper entrainment; the code covers the timing analyses only.
- Extended Data Fig 4c gives 19,000 units, against 20,300 in the main text; both are recorded as readings.
- The O5(a) ranking taken from the code favours a positive cycle-0 change, and the file says so.
- The premotor tracing comes from reference 43 (Takatoh et al. 2021) and has no archive identifier. Fig 3a is marked `elsewhere`, and Fig 3b uses outside data (`with_inputs`).
- The autoencoder claims need the raw videos.

## End of run

30 turns, 8 minutes, result: success.
