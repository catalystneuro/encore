# 001037 · claims · run 39854248263

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453 paper/ claims/001037 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml; wc -c paper/*.txt; head -50 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
head -c 30000 claims/001453/*.yaml
```

```
# Claims for Fouke, He, Loring & Naumann (2025) on dandiset 001453.
# Source: the accepted author manuscript in PubMed Central (PMC12218792), full text, read
# from its Results, figure legends and STAR Methods. The version of record is not open access.
#
# When these criteria were written, the author had seen the data check only: the file list,
# subject metadata, frame rates, units, trial structure and stimulus codes of every file, and
# the extent of positions. No claim's analysis had been run. The author had also read the
# outputs printed in the paper's own analysis notebook (Fig1-S1.ipynb, GitLab commit 33a5c29),
# which include per-stimulus median speeds and angular velocities and its statistics.
#
# The dandiset holds only the freely swimming tracking data of Figure 1 and Figure S1. Its
# stimulus codes 0 to 20 carry no names. The names come from the paper's code and from the
# stimulus software's protocol file (see stimulus-code-link), so the claims that need them
# use outside data and depend on that claim.
#
# Method choices fixed here, from the paper's Fig1-S1.ipynb where the Methods are silent: a
# trial is one stim_index; tracked frames only; positions smoothed with a Savitzky-Golay filter
# (21 frames, order 2); trials rejected when the absolute cumulative heading change exceeds
# 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or the mean speed exceeds
# 100 mm/s; measures taken from 3 s to 35 s after the first frame (the 3 s stationary phase is
[... 301 more lines not kept]
```

**Agent calls Bash**

```bash
wc -c paper/*.txt; cat tools/claims_check.py | head -80
```

Result: not kept, because it reads the paper's text.

**Agent**

Now the paper.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41586-024-07915-x.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
t=open('paper/10.1038-s41586-024-07915-x.txt').read()
print(len(t)); print(t[54800:90000])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/96097c86-28f4-4092-9a28-6176e95eb562/tool-results/b7c3eo3w9.txt"
}
```

```
1	121377
2	ailed to do so over the same range of connection densities (Fig. 4d,f ). Extended Data Fig. 11 Deriving network time constant for model simulations. a. Analytical derivation of network time constant from connectivity matrix of purely excitatory recurrent neural network. In these purely excitatory network models, the density of connections that yielded network time constants in the observed range was much lower than the experimentally measured value (36%). To match more accurately the empirically observed connection density, we incorporated excitation-recruited fast-feedback inhibition into our integrate-and-fire network 7 , as VMHvl is known to receive dense GABAergic innervation from surrounding areas 43 , 44 . The addition of global strong feedback inhibition allowed networks to match the observed connection density (36%) but, importantly, maintained the slow nature of the functional connectivity (20 s; Fig. 4g and 4h (left)). Indeed, networks simulated with a long τ s (20s) and dense σ (36%) could integrate digital optogenetic stimulation in a manner like that observed experimentally (Fig. 4i,j ). By contrast, purely glutamatergic networks ( τ s = 100 ms) were unable to integrate at the observed timescales given the measured connectivity density (Fig. 4h (right) and 4k–l ). Together, these results suggest an implementation of the VMHvl Esr1 line attractor that combines slow neurotransmission and relatively dense 41 subnetwork interconnectivity within an attractor-creating ensemble. Attractor stability ties to connectivity The observed dynamics along the integration dimension exhibits two important characteristics that can reflect the stability of the line attractor, ramping activity up; and slow decay down the integrator (Fig. 5a ). Both of these characteristics might either be intrinsic or be driven by external inputs to the line attractor 5 , 40 . Previously, we observed that individual differences in aggressiveness among mice were positively correla
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
t=open('paper/10.1038-s41586-024-07915-x.txt').read()
i=t.find('Acknowledgements We thank'); print(t[i:i+5000])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
git ls-remote https://github.com/lindermanlab/ssm HEAD 2>&1 | head; curl -s https://api.dandiarchive.org/api/dandisets/001037/ | head -c 1500; echo; curl -s https://api.dandiarchive.org/api/dandisets/001037/versions/draft/info/ | python3 -c "import json,sys; d=json.load(sys.stdin); m=d['metadata']; print(m.get('name')); print(m.get('description')); print(m.get('assetsSummary'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/neuralcomputation/hypothalamic-dynamics hd && git clone -q --depth 1 https://github.com/lindermanlab/ssm ssm; cd hd && git log -3 --format='%H %ad %s' && find . -type f -not -path './.git/*' | head -100
```

```
28fee70fce99949ff34f6ae43937d5e99606dd81 Tue Jun 9 12:01:21 2026 +0800 add link to gpslds notebook at end of engaging aggression notebook
a584ca838384b4efdca54abbf9d52b15ef88d1f1 Tue Jun 9 12:00:38 2026 +0800 change markdown text in loading for cv notebook to reflect data
008e04b3827c5dbbb5849d84dd3fd42f61770fbd Tue Jun 9 12:00:07 2026 +0800 link original rslds demo notebook in readme
./processing/nwb_hdf5_loading.py
./processing/data_processing.py
./plotting/rslds_plots_two_photon.py
./plotting/rslds_plots_redux.py
./plotting/rslds_plots_cv.py
./plotting/rslds_plots.py
./plotting/plotting.py
./notebooks/hypothalamus_observing_aggression.ipynb
./notebooks/hypothalamus_observation_two_photon.ipynb
./notebooks/hypothalamus_mating_perturbation.ipynb
./notebooks/hypothalamus_mating_dynamics.ipynb
./notebooks/hypothalamus_engaging_aggression.ipynb
./notebooks/hypothalamus_aggression_cross_validation.ipynb
./example_data/sub-m541_behavior.nwb
./example_data/sub-M70.nwb
./example_data/sub-M30L.nwb
./example_data/sub-M1188.nwb
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/hd && cat README.md && wc -l analysis/*.py processing/*.py plotting/*.py && python3 -c "
import json
for nb in ['notebooks/hypothalamus_observation_two_photon.ipynb','notebooks/hypothalamus_observing_aggression.ipynb']:
    d=json.load(open(nb)); print('=====',nb)
    for c in d['cells']:
        print('---',c['cell_type']); print(''.join(c['source']))
"
```

````
<persisted-output>
Output too large (91.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/96097c86-28f4-4092-9a28-6176e95eb562/tool-results/bbh0khznq.txt

Preview (first 2KB):
# Hypothalamic Dynamics
a one-stop shop for Jupyter Notebooks written in Python for understanding dynamic systems analysis of hypothalamic neural data[1][2][3].

The underlying code for rSLDS comes from the [`ssm`](https://github.com/lindermanlab/ssm) library. For a more general exploration of using rSLDS we recommend [this example notebook](https://github.com/lindermanlab/ssm/blob/master/notebooks/4-Recurrent-SLDS.ipynb) from the same repository.

# Installation
The code within these notebooks requires additional libraries which must be installed. It is recommended that you create a separate conda environment to install the libraries to.

The demo notebooks can be installed by:
1. Cloning the repository or downloading all the individual files themselves.
   * To clone the repository, follow the steps detailed on this page: [cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
   * To download all of the individual files from this repository, click on the button that says '**<> Code**' near the top of page and click 'Download ZIP'
2. Creating a conda environment using the `environment.yml` file within the repository.
   * To create the required conda environment, first navigate to the directory that you downloaded the notebooks and code to using the `cd` command within Anaconda Prompt
   ``` {.console} 
   cd PATH/TO/DIRECTORY
[... 9 more lines not kept]
````

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/96097c86-28f4-4092-9a28-6176e95eb562/tool-results/bbh0khznq.txt"
}
```

````
1	# Hypothalamic Dynamics
2	a one-stop shop for Jupyter Notebooks written in Python for understanding dynamic systems analysis of hypothalamic neural data[1][2][3].
3	
4	The underlying code for rSLDS comes from the [`ssm`](https://github.com/lindermanlab/ssm) library. For a more general exploration of using rSLDS we recommend [this example notebook](https://github.com/lindermanlab/ssm/blob/master/notebooks/4-Recurrent-SLDS.ipynb) from the same repository.
5	
6	# Installation
7	The code within these notebooks requires additional libraries which must be installed. It is recommended that you create a separate conda environment to install the libraries to.
8	
9	The demo notebooks can be installed by:
10	1. Cloning the repository or downloading all the individual files themselves.
11	   * To clone the repository, follow the steps detailed on this page: [cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
12	   * To download all of the individual files from this repository, click on the button that says '**<> Code**' near the top of page and click 'Download ZIP'
13	2. Creating a conda environment using the `environment.yml` file within the repository.
14	   * To create the required conda environment, first navigate to the directory that you downloaded the notebooks and code to using the `cd` command within Anaconda Prompt
15	   ``` {.console} 
16	   cd PATH/TO/DIRECTORY
17	   ```
18	   * After navigating to this folder (which should include the file `environment.yml`), run this command:
19	   ``` {.console} 
20	   conda env create -f environment.yml
[... 1099 more lines not kept]
````

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/96097c86-28f4-4092-9a28-6176e95eb562/tool-results/bbh0khznq.txt",
 "offset": 1240,
 "limit": 670
}
```

```
1240	            num_iters=num_iters,
1241	            alpha=alpha,
1242	        )
1243	
1244	    print("retrieving model results")
1245	    xhat = posterior.mean_continuous_states[0]
1246	    if num_input_terms != 0:
1247	        zhat = rslds.most_likely_states(xhat, rslds_neuraldata, trackdata)
1248	    else:
1249	        zhat = rslds.most_likely_states(xhat, rslds_neuraldata)
1250	    rslds_lem = rslds
1251	
1252	    rslds_results = convert_rslds_model_to_dict(rslds_lem)
1253	
1254	    return elbos, posterior, xhat, zhat, rslds_results
1255	
1256	def calculate_model_prediction(
1257	    behavior_rasters: list[np.ndarray],
1258	    subset_window: list[int],
1259	    xhat: np.ndarray,
[... 648 more lines not kept]
```

**Agent**

Now the loading and analysis helpers.

**Agent calls Bash**

```bash
cd $TMPDIR/hd && cat processing/nwb_hdf5_loading.py plotting/rslds_plots_two_photon.py analysis/analysis_functions.py
```

```
<persisted-output>
Output too large (29.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/96097c86-28f4-4092-9a28-6176e95eb562/tool-results/b6l66btte.txt

Preview (first 2KB):
import h5py
import numpy as np
from os.path import splitext
from pathlib import Path

def load_nwb_h5py(filename: str, datapath):
    """
    From an .nwb file gets out Behavioral Epochs as well as ophys or ephys data to pass
    into ONAM.

    If `neural_data_path` is specified, will look for that data table in 'ophys' or
    'ephys' processing modules.
    """
    if not splitext(filename)[1] == ".nwb":
        raise ValueError("Passed in file must have .nwb extension.")
    nwbfile = h5py.File(filename, "r")
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/hd && grep -n "def \|projection\|weights\|stim\|baseline\|isi\|mean(\|zscore\|z_score" processing/nwb_hdf5_loading.py plotting/rslds_plots_two_photon.py | head -120; grep -n "def " analysis/analysis_functions.py processing/data_processing.py
```

```
processing/nwb_hdf5_loading.py:6:def load_nwb_h5py(filename: str, datapath):
processing/nwb_hdf5_loading.py:39:            and not "ElectricalSeries" in nwbfile["acquisition"].keys()
processing/nwb_hdf5_loading.py:105:def load_nwb_h5py_neural_data(filename:str, datapath: tuple):
processing/nwb_hdf5_loading.py:127:            and not "ElectricalSeries" in nwbfile["acquisition"].keys()
processing/nwb_hdf5_loading.py:161:def load_nwb_h5py_behavior_data(
processing/nwb_hdf5_loading.py:223:def _decode(value):
processing/nwb_hdf5_loading.py:225:    if isinstance(value, bytes):
processing/nwb_hdf5_loading.py:227:    if isinstance(value, np.ndarray):
processing/nwb_hdf5_loading.py:233:    if isinstance(value, np.generic):
processing/nwb_hdf5_loading.py:237:def read_subject_id_from_nwb(path: Path) -> str:
processing/nwb_hdf5_loading.py:242:def read_dynamic_table_column(f: h5py.File, table_base: str, column_name: str):
processing/nwb_hdf5_loading.py:253:def read_activated_neurons_table(path: Path) -> list[tuple[str, int]]:
processing/nwb_hdf5_loading.py:264:def nwb_has_session(path: Path, session_key: str) -> bool:
processing/nwb_hdf5_loading.py:266:        return f"processing/ophys/{session_key}_zscored_activity/data" in f
processing/nwb_hdf5_loading.py:269:def read_zscored_activity_cells_x_frames(path: Path, session_key: str) -> np.ndarray:
processing/nwb_hdf5_loading.py:270:    """NWB stores frames x cells; return cells x frames for projection."""
processing/nwb_hdf5_loading.py:272:        ds_path = f"processing/ophys/{session_key}_zscored_activity/data"
processing/nwb_hdf5_loading.py:279:def read_rslds_factor_weights_cells_x_factors(path: Path) -> np.ndarray:
processing/nwb_hdf5_loading.py:282:        base = "analysis/rSLDS_factor_weights"
processing/nwb_hdf5_loading.py:288:    weights = np.column_stack([w1[order], w2[order]])
[... 64 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/hd && sed -n 237,407p processing/nwb_hdf5_loading.py; sed -n 1,47p plotting/rslds_plots_two_photon.py; sed -n 57,190p processing/data_processing.py
```

```
def read_subject_id_from_nwb(path: Path) -> str:
    with h5py.File(path, "r") as f:
        return _decode(f["general/subject/subject_id"][()])


def read_dynamic_table_column(f: h5py.File, table_base: str, column_name: str):
    candidates = [
        f"{table_base}/{column_name}/data",
        f"{table_base}/{column_name}",
    ]
    for candidate in candidates:
        if candidate in f:
            return f[candidate][()]
    raise KeyError(f"Could not find column {column_name} under {table_base}")


def read_activated_neurons_table(path: Path) -> list[tuple[str, int]]:
    with h5py.File(path, "r") as f:
        base = "analysis/ActivatedNeurons"
        if base not in f:
[... 333 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/hd && python3 -c "
import json,re
for nb in ['notebooks/hypothalamus_engaging_aggression.ipynb','notebooks/hypothalamus_aggression_cross_validation.ipynb']:
    d=json.load(open(nb)); print('=====',nb)
    for c in d['cells']:
        s=''.join(c['source'])
        if c['cell_type']=='markdown': print('MD:',s[:600].replace('\n',' '))
        else: print('CODE:', s[:1500])
" | grep -v "^$" | head -300
```

```
===== notebooks/hypothalamus_engaging_aggression.ipynb
MD: # Understanding hypothalamic aggression dynamics using dynamical systems  This notebook walks through a recurrent switching linear dynamical system (rSLDS) analysis of hypothalamic population activity during aggressive social engagement. The goal is to make the workflow legible as a reusable blueprint: starting from calcium activity and behavioral annotations, we fit low-dimensional dynamical systems, evaluate robustness across random initializations, inspect the inferred state space, and compare autonomous and input-driven versions of the model.  In this example, the neural activity comes fro
MD: ## Set up analysis functions  This first cell defines the helper functions used throughout the notebook. The most important function is `rslds(...)`, a convenience wrapper around the underlying SSM implementation. It handles four common steps:  1. selecting the requested time window; 2. optionally aligning behavioral rasters as inputs; 3. initializing and fitting the rSLDS with Laplace EM; 4. returning the inferred continuous trajectory `xhat`, discrete states `zhat`, ELBOs, and model parameters.  The helper `calculate_model_prediction(...)` uses the learned local linear dynamics to roll the l
CODE: # add parent directory for relative imports
import sys
import os
parent_dir = os.path.abspath(os.path.join('..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
CODE: import numpy as np
import autograd.numpy.random as npr
from ssm import SLDS
from analysis.rslds_patch import SLDS_patch
def convert_rslds_model_to_dict(rslds_model: SLDS) -> dict:
    """
    Converts an SLDS object to a dictionary containnig only Python and numpy types.
    Parameters:
    -----------
    rslds_model : ssm.SLDS
        A fit SLDS model.
[... 281 more lines not kept]
```

**Agent calls Bash**

```bash
cat schemas/claims.schema.json | head -200; sed -n 80,200p tools/claims_check.py
```

```
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
      "description": "The dataset the claims are tested on: the archive and the dataset's identifier there.",
      "type": "object",
      "additionalProperties": false,
[... 213 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d['\$defs'],indent=1))"; sed -n 200,260p schemas/claims.schema.json | grep -n checks
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
[... 83 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ssm && git log -1 --format='%H %ad'; grep -n "def initialize\|l2_penalty_A\|single_subspace" ssm/lds.py | head
```

```
eb6c8aa33e5311d3564075807dec340759dd8081 Fri May 9 09:43:13 2025 -0700
40:                 single_subspace=True,
135:                single_subspace=single_subspace, **emission_kwargs)
161:    def initialize(self, datas, inputs=None, masks=None, tags=None,
418:            if not self.emissions.single_subspace:
901:                single_subspace=True, **emission_kwargs)
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "claims/001037/10.1038-s41586-024-07915-x.yaml",
 "content": "# Claims for Vinograd, Nair, Kim, Linderman & Anderson (2024), \"Causal evidence of a line\n# attractor encoding an affective state\", Nature 634, 910-918, on dandiset 001037.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-22,\n# protocol pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the version of record (open access, corrected publication 2025) as served by\n# Europe PMC (PMC11499281): main text, Methods, the legends of Figures 1 to 5 and of Extended\n# Data Figures 1 to 12. The supplementary information is a Reporting Summary only; no result\n# rests on it. No PDF was supplied, so figure panels were not read; findings shown only in a\n# panel are taken from its legend and the Results.\n#\n# Code read. The paper links only the rSLDS library, github.com/lindermanlab/ssm (read at\n# commit eb6c8aa), which has no analysis of this paper. The dandiset's description links the\n# authors' sample code, github.com/neuralcomputation/hypothalamic-dynamics (read at commit\n# 28fee70; its example data files were not opened). It is ranked below the Methods. It fixes:\n# the time constant of an rSLDS eigenvalue as abs(1/log(abs(lambda))) divided by the frame\n# rate, in seconds (the Methods give 1/log(lambda) in frames); the projection of a session\n# onto x1 or x2 as the stored rSLDS factor weights (rSLDS_factor_1, rSLDS_factor_2) times the\n# z-scored activity, smoothed with a moving average and baseline-subtracted over the window\n# stored per session in ProjectionMetadata (projection_factor names which factor is the\n# integration (x1) and which the \"novel\" (x2) projection); photostimulation pulse onsets at\n# frames 150, 360, 570 and 780 (10 Hz) for the 20 s ISI sessions and 140, 240, 340 and 440 for\n# the 8 s ISI sessions; observation traces aligned so that BALB/c entry falls at 50 s and\n# baseline-subtracted over their first 100 frames; and, for 2P observation fits, an rSLDS of\n# 2 states and 2 latent dimensions (l2_penalty_A 820, l2_penalty 100, alpha 0.9, 150\n# Laplace-EM iterations), and for miniscope fits 3 states and 2 dimensions (l2_penalty_A 10,\n# l2_penalty 500, alpha 0.5, 100 iterations). The notebooks call these \"representative\"\n# settings, so where a claim needs a new fit the number of states is also taken as the Methods\n# give it (fivefold cross-validation), and both are readings.\n#\n# Data the paper used. Male Esr1-Cre mice expressing jGCaMP7s in VMHvl Esr1 neurons.\n# (1) Microendoscope (miniscope) imaging at 30 Hz, downsampled to 10 Hz, CNMF-E traces, in 5\n# freely behaving mice, each recorded engaging in aggression (a BALB/c intruder introduced\n# twice into the home cage) and observing aggression (a Swiss Webster (SW) demonstrator\n# attacking BALB/c intruders), in random order, with a 5 min solitary baseline at the start of\n# each session; annotations of sniff and attack, observed attack, intruder entries and\n# removals (Extended Data Figs 1 to 4). (2) Two-photon imaging at 10 Hz through a GRIN lens in\n# 9 head-fixed mice on a treadmill observing aggression (SW resident and BALB/c intruders);\n# rSLDS fits identify x1 (integration) and x2 neurons (Fig. 1). (3) After removal of the\n# demonstrators, holographic photostimulation (ChRmine) in the same preparation: groups of 5\n# x1 neurons (n = 8 mice) or 5 x2 neurons (n = 7) with four pulses at 20 s ISI, and 8 s ISI\n# (n = 7); 1 mW against 5 mW per neuron; x1 stimulation followed by x2 stimulation; random\n# non-weighted neurons (n = 5); unitary x1 neurons (25 neurons, 8 mice) and unitary x2\n# neurons (18 neurons, 7 mice) with imaging of non-targeted neurons (Figs 2, 3 and 5,\n# Extended Data Figs 6 to 10, 12). Also: motion SVDs from face video of the head-fixed mice\n# (Extended Data Fig. 5) and a calibration of photostimulation spatial resolution on 17\n# reference cells (Extended Data Fig. 6). Figure 4 is a simulation of a spiking network and\n# uses no recorded data except the 36% connection density measured in Fig. 4a.\n#\n# Method details used by several criteria, from the paper unless said otherwise:\n# - Tests. The Methods say all tests are two-tailed and nonparametric. The Mann-Whitney\n#   p-values at n = 5 (0.0079) and n = 4 (0.0286) are the smallest exact two-sided values of\n#   the unpaired test, which a paired signed-rank test cannot reach, so a Mann-Whitney test is\n#   run unpaired even where the Methods say \"binary paired samples\". Kruskal-Wallis tests use\n#   one value per mouse and condition, followed by Dunn's correction, as the legends name them.\n# - Projections onto x1 and x2 follow the sample code (above).\n# - ISI windows (W). The legends compare \"the average z-scored activity ... during the\n#   baseline or ISIs\" without giving the windows. Baseline is the period before the first\n#   pulse. The readings are (Wa) each ISI from the end of the 2 s pulse to the next onset (for\n#   the last pulse, the same length after it), and (Wb) each ISI from one onset to the next.\n# - Dunn comparisons (C). The legends print three or four p-values per panel without saying\n#   which pairs they compare. The readings are (Ca) each ISI against baseline and (Cb) each\n#   ISI against the one before it (the first against baseline).\n# - Pulse parameters. The Results give \"2 s, 20 Hz, 5 mW\" and the Methods \"10 Hz, 2 s, 10 ms\n#   pulse width\". The attempt takes the pulse timing from the stored stimulation frames.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001037\"\npaper: doi:10.1038/s41586-024-07915-x\nclaims:\n# ---------------------------------------------------------------------------------------\n# Freely behaving mice, miniscope (Extended Data Figs 1 to 4)\n- id: ed1n-engaging-x1-slower\n  statement: In freely behaving mice engaging in aggression, rSLDS fits show an integration\n    dimension x1 with a longer time constant than the orthogonal dimension x2, an approximate\n    line attractor.\n  source: Extended Data Fig. 1n and 1o; Results, Line attractor for observing aggression, paragraph 1\n  quote: revealed an approximate line attractor under both conditions, exhibiting ramping and\n    persistent activity aligned and maintained across both performed and observed attack sessions\n  statistics:\n  - test: two-tailed Mann-Whitney U-test\n    p: 0.0079\n    n: 5 mice\n  criterion: For each mouse, an rSLDS with 2 latent dimensions fit to the engaging session\n    (number of states by fivefold cross-validation, Methods, or 3 states with the sample\n    code's settings; both readings run), kept only when its cvR2 is at least 70% (Methods).\n    Time constants from the eigenvalues of each state's dynamics matrix as the sample code\n    computes them; x1 is the dimension with the larger time constant in the state that holds\n    the slow dynamics (the state with the largest time constant). Reproduced when the x1 time\n    constants exceed the x2 time constants across the 5 mice by a two-tailed unpaired\n    Mann-Whitney test at p < 0.05. The line attractor score, log2 of the largest over the\n    second largest time constant (Methods), is reported per mouse.\n- id: ed1p-observing-x1-slower\n  statement: In the same mice observing aggression, rSLDS fits also show an x1 dimension with a\n    longer time constant than x2.\n  source: Extended Data Fig. 1p and 1q; Results, Line attractor for observing aggression, paragraph 1\n  quote: revealed an approximate line attractor under both conditions\n  statistics:\n  - test: two-tailed Mann-Whitney U-test\n    p: 0.0079\n    n: 5 mice\n  criterion: As ed1n-engaging-x1-slower, on the observation sessions.\n- id: ed1m-x1-observe-attack-vs-sniff\n  statement: In freely behaving mice, average x1 activity differs between sniffing the SW mouse\n    and observing the SW mouse attack a BALB/c intruder.\n  source: Extended Data Fig. 1m\n  quote: Average activity in the x 1 dimension during sniffing of the SW mouse, vs observing the SW\n    mouse a BALB\\c intruder (n = 4 mice, *p = 0.0286, Two-tailed Mann Whitney U -test\n  statistics:\n  - test: two-tailed Mann-Whitney U-test\n    p: 0.0286\n    n: 4 mice\n  depends_on:\n  - ed1p-observing-x1-slower\n  criterion: The legend is garbled and the panel was not read, so the direction is not fixed\n    from the text. Per mouse, the mean of the x1 projection of the observation session over\n    frames annotated as sniffing the SW mouse and over frames annotated as observing attack.\n    Reproduced when a two-tailed unpaired Mann-Whitney test over mice gives p < 0.05; the\n    direction is reported. The legend's n of 4 (of 5 mice) is not explained; all mice with\n    both annotations are used and the count is reported.\n- id: ed3c-x1-activity-observe-vs-engage\n  statement: The activity of x1 neurons during observed attack bouts does not differ from their\n    activity during engaged attack.\n  source: Extended Data Fig. 3c\n  quote: comparison of the activity during observing attack bouts and engaging in attack (n = 5 mice,\n    p = 0.42, Two-tailed Mann-Whitney U -test\n  statistics:\n  - test: two-tailed Mann-Whitney U-test\n    p: 0.42\n    n: 5 mice\n  depends_on:\n  - ed1n-engaging-x1-slower\n  - ed1p-observing-x1-slower\n  criterion: A claim of absence, judged on the paper's test. Per mouse, the mean activity of the\n    x1 neurons of each condition during attack bouts (observed or engaged). Reproduced when a\n    two-tailed Mann-Whitney test over mice gives p >= 0.05; not reproduced when p < 0.05. The\n    difference is reported either way. Which neurons are x1 neurons is not fixed beyond the\n    rSLDS weights; the readings are the five neurons with the largest absolute x1 weight (as\n    in Fig. 1i) and the neurons the dataset marks as x1, if it does.\n- id: ed3e-achw-full-session\n  statement: Over the full interaction, autocorrelation half-widths of x1 neurons are similar\n    when observing (25 +/- 0.8 s) and engaging in aggression (20 +/- 1.7 s).\n  source: Extended Data Fig. 3e\n  quote: mean achw during observation:25 ± 0.8s, mean achw during engagement:20 ± 1.7s, n=5 mice,\n    p = 0.125\n  statistics:\n  - test: two-tailed Mann-Whitney U-test\n    p: 0.125\n    n: 5 mice\n  expected:\n  - quantity: mean ACHW of x1 neurons, observation\n    value: 25\n    tolerance: 0.8\n    unit: s\n  - quantity: mean ACHW of x1 neurons, engagement\n    value: 20\n    tolerance: 1.7\n    unit: s\n  depends_on:\n  - ed1n-engaging-x1-slower\n  - ed1p-observing-x1-slower\n  criterion: Autocorrelation per neuron as in Methods equations 7 and 8 (the sample code's\n    autocorr_matlab). The half-width is not defined beyond its name; the reading is the first\n    lag at which the autocorrelation falls to 0.5 or below, in seconds at 10 Hz. Per mouse,\n    the mean over x1 neurons (readings of x1 neurons as in ed3c). Expected values within\n    tolerance, and, as a claim of absence, a two-tailed Mann-Whitney test over mice with p >=\n    0.05.\n- id: ed3f-achw-after-removal\n  statement: Aligned to removal of the last intruder, autocorrelation half-widths of x1 neurons\n    are similar when observing (14 +/- 1 s) and engaging (11 +/- 1.6 s).\n  source: Extended Data Fig. 3f\n  quote: mean achw during observation:14 ± 1s, mean achw during engagement:11 ± 1.6s, n = 5 mice,\n    p = 0.187\n  statistics:\n  - test: two-tailed Mann-Whitney U-test\n    p: 0.187\n    n: 5 mice\n  expected:\n  - quantity: mean ACHW of x1 neurons after last intruder removal, observation\n    value: 14\n    tolerance: 1\n    unit: s\n  - quantity: mean ACHW of x1 neurons after last intruder removal, engagement\n    value: 11\n    tolerance: 1.6\n    unit: s\n  depends_on:\n  - ed3e-achw-full-session\n  criterion: As ed3e-achw-full-session, on activity from the removal of the last intruder to the\n    end of the session (the paper does not give the window's end; the session end is the only\n    reading the legend allows).\n- id: ed3g-decode-observed-attack\n  statement: A decoder trained on x1 activity during observation separates observed attack bouts\n    from non-attack bouts better than shuffled controls.\n  source: Extended Data Fig. 3g\n  quote: A SVM decoder was trained on data from integration dimension activity to separate bouts of\n    observing attack from non attack bouts. Right:Quantification of the decoder accuracy performance\n    (n = 5 mice, p = 0.0079\n  statistics:\n  - test: two-tailed Mann-Whitney U-test\n    p: 0.0079\n    n: 5 mice\n  depends_on:\n  - ed1p-observing-x1-slower\n  criterion: As the Methods describe (Decoding behaviour from integration dimension). Attack\n    bouts separated by less than 5 s merged into trials, classes balanced; a one-dimensional\n    threshold on the normalized x1 signal fit by a linear SVM on training frames and scored on\n    held-out frames; shuffles assign the behaviour labels randomly to bouts, 20 times. The\n    train and test split is not given; the readings are leave-one-trial-out and fivefold\n    over trials. Reproduced when decoder accuracy exceeds shuffled accuracy across mice by a\n    two-tailed Mann-Whitney test at p < 0.05.\n- id: ed3h-decode-engaged-from-observed\n  statement: The decoder trained on observing attack decodes engaged attack from x1 activity\n    better than shuffled data, so x1 encodes a similar variable in both conditions.\n  source: Extended Data Fig. 3h; Results, Line attractor for observing aggression, paragraph 1\n  quote: could be reliably used to decode from held-out data instances of both observation of and\n    engagement in attack, suggesting that this dimension encodes a similar internal state variable\n    under both conditions\n  statistics:\n  - test: two-tailed Mann-Whitney U-test\n    p: 0.0079\n    n: 5 mice\n  depends_on:\n  - ed3g-decode-observed-attack\n  criterion: The decoder of ed3g-decode-observed-attack applied to the engaging session's x1\n    signal (frames of attack against all others); the paper does not say whether the engaging\n    session is projected with the observation model's weights or its own; both readings run.\n    Reproduced when accuracy exceeds that of the shuffled decoder across mice by a two-tailed\n    Mann-Whitney test at p < 0.05.\n- id: ed4c-x1-neuron-overlap\n  statement: Around 70% of the neurons that contribute to the line attractor overlap between\n    observing and engaging in aggression.\n  source: Extended Data Fig. 4c; Results, Line attractor for observing aggression, paragraph 1\n  quote: suggesting that a highly overlapping set of neurons (70%) contributes to line-attractor\n    dynamics during observing or engaging in attack\n  expected:\n    quantity: overlap of x1 neurons between conditions, mean over 5 mice\n    value: 70\n    tolerance: 7\n    unit: percent\n  depends_on:\n  - ed1n-engaging-x1-slower\n  - ed1p-observing-x1-slower\n  criterion: The paper does not say how a neuron is counted as contributing, or the\n    denominator. Readings for contributing are (a) the top five neurons by absolute weight, as\n    in Fig. 1i, and (b) the neurons the dataset marks as x1 neurons, if it does. Readings for\n    the overlap are the shared fraction of (i) the observation set and (ii) the engagement set.\n    Reproduced when one reading gives a mean within tolerance.\n- id: ed4d-weight-dot-product\n  statement: The x1 weight vector during observation is more aligned with the x1 weight vector\n    during engagement than with the x2 weight vector.\n  source: Extended Data Fig. 4d\n  quote: rSLDS weights of the x 1 dimension during observation were compared to model weights of the x\n    1 and x 2 dimensions during engagement using a dot product of the two weight vectors. (n = 5\n    mice, ***p = 0.0079\n  statistics:\n  - test: two-tailed Mann-Whitney U-test\n    p: 0.0079\n    n: 5 mice\n  depends_on:\n  - ed1n-engaging-x1-slower\n  - ed1p-observing-x1-slower\n  criterion: Per mouse, the dot product of the observation x1 weight vector with the engagement\n    x1 vector and with the engagement x2 vector, over neurons present in both sessions. The\n    paper does not say whether vectors are normalized or signs aligned; the readings are the\n    raw dot product and the absolute dot product of unit vectors. Reproduced when x1-x1\n    exceeds x1-x2 across mice by a two-tailed Mann-Whitney test at p < 0.05 under one reading.\n- id: ed4g-x2-more-spontaneous\n  statement: During the solitary baseline, x2 neurons show more frequent spontaneous calcium\n    transients than x1 neurons (2.3 against 1.6 events).\n  source: Extended Data Fig. 4g; Results, Line attractor for observing aggression, paragraph 2\n  quote: we did see a slightly but significantly higher frequency of spontaneous calcium transients\n    in x 2 neurons\n  statistics:\n  - test: two-tailed Mann-Whitney U-test\n    p: 0.012\n    n: 5 mice\n  expected:\n  - quantity: transient frequency of x1 neurons at baseline\n    value: 1.6\n    tolerance: 0.2\n    unit: events\n  - quantity: transient frequency of x2 neurons at baseline\n    value: 2.3\n    tolerance: 0.2\n    unit: events\n  depends_on:\n  - ed1n-engaging-x1-slower\n  - ed1p-observing-x1-slower\n  criterion: A transient is a crossing above 1.5 standard deviations of the z-scored activity\n    (legend) during the 5 min baseline at the start of the session (Methods, Behaviour\n    annotations). The paper does not say per what time the frequency is, which session's\n    baseline, or which model's x1 and x2 neurons are used; readings are events per baseline\n    and per minute, and the engaging and observing sessions' baselines and models. Reproduced\n    when x2 exceeds x1 across mice by a two-tailed Mann-Whitney test at p < 0.05; the values\n    are compared with the expected ones under each reading.\n- id: ed4hi-amplitude-tau-similar\n  statement: Baseline transient amplitude (0.58 against 0.71 z) and decay constant (1.7 against\n    2.3 s) do not differ between x1 and x2 neurons.\n  source: Extended Data Fig. 4h and 4i; Results, Line attractor for observing aggression, paragraph 2\n  quote: We did not detect a difference in amplitude or decay constant (tau) between x 1 and x 2\n    neurons\n  statistics:\n  - about: amplitude, x1 against x2\n    test: two-tailed Mann-Whitney U-test\n    p: 0.188\n    n: 5 mice\n  - about: decay constant, x1 against x2\n    test: two-tailed Mann-Whitney U-test\n    p: 0.34\n    n: 5 mice\n  expected:\n  - quantity: mean transient amplitude, x1\n    value: 0.58\n    tolerance: 0.04\n    unit: z-score\n  - quantity: mean transient amplitude, x2\n    value: 0.71\n    tolerance: 0.08\n    unit: z-score\n  - quantity: mean decay constant, x1\n    value: 1.7\n    tolerance: 0.6\n    unit: s\n  - quantity: mean decay constant, x2\n    value: 2.3\n    tolerance: 0.4\n    unit: s\n  depends_on:\n  - ed4g-x2-more-spontaneous\n  criterion: A claim of absence, judged on the paper's test, two-tailed Mann-Whitney over mice\n    for each measure; reproduced when neither gives p < 0.05. Transients as in\n    ed4g-x2-more-spontaneous. The decay constant fit is not described; the reading is an\n    exponential fit to the mean transient from its peak.\n# ---------------------------------------------------------------------------------------\n# Head-fixed 2P observation (Figure 1)\n- id: fig1e-2p-x1-slower\n  statement: In head-fixed mice observing aggression, rSLDS fits to 2P data show an x1\n    dimension with longer time constants than x2.\n  source: Figure 1e; Results, Line attractor for observing aggression, paragraph 4\n  quote: during observation of aggression by the head-fixed mice, rSLDS analysis identified an\n    integration dimension with slow dynamics ( x 1 ) aligned to an approximate line attractor, and an\n    orthogonal dimension with faster dynamics ( x 2 )\n  statistics:\n  - test: two-tailed Mann-Whitney U-test\n    p: 0.0001\n    p_relation: \"<\"\n    n: 9 mice\n  criterion: As ed1n-engaging-x1-slower, on the 2P observation sessions, with the sample code's\n    2P settings (2 states) as the second reading. Methods add that 2P flow fields were fit\n    with an input term for the presence of the BALB/c intruder; fits with and without that\n    input are both run. The legend's P is read from its star key (four stars, P < 0.0001), the\n    only test in the figure besides panel m.\n- id: fig1f-line-attractor-score\n  statement: The line attractor score is positive across the 9 head-fixed mice.\n  source: Figure 1f\n  inferred: The legend shows the score across mice without a value or test; the statement reads\n    it from the score's definition (Methods) and the Results calling the dynamics an\n    approximate line attractor.\n  depends_on:\n  - fig1e-2p-x1-slower\n  criterion: Score = log2 of the largest time constant over the second largest (Methods,\n    Calculation of line attractor score) of each mouse's fit. The paper gives no threshold;\n    the readings are (a) the mean over mice above 0 and (b) every mouse above 0. Reproduced\n    when both hold; partially reproduced when only (a) holds.\n- id: x1-time-constant-range\n  statement: The experimentally observed network time constants of the integration dimension lie\n    in a range of about 50 to 200 s.\n  source: Results, Line-attractor neurons form ensembles, paragraph 5\n  quote: could yield network time constants ( τ n ) in the experimentally observed range (~50–200 s\n  depends_on:\n  - fig1e-2p-x1-slower\n  expected:\n    quantity: x1 time constants of the 2P observation fits\n    value: 125\n    unit: s\n  criterion: A reported range; reproduced when the x1 time constants of the 9 mice lie within\n    50 to 200 s widened by 10% of each bound (45 to 220 s), with at most one mouse outside;\n    partially reproduced when the median lies inside. The expected value is the midpoint and\n    is not itself tested.\n- id: methods-subspace-angle\n  statement: The x1 and x2 dimensions are nearly orthogonal, with a subspace angle of 88.1 +/-\n    0.87 degrees across 9 mice.\n  source: Methods, Dynamical system models of neural data, paragraph 2\n  quote: we initially confirmed the orthogonality of these dimensions by computing the subspace angle\n    between them (88.1 ± 0.87°, n = 9 mice)\n  expected:\n    quantity: angle between the x1 and x2 columns of the emission matrix C, mean over mice\n    value: 88.1\n    tolerance: 0.87\n    unit: degrees\n  criterion: The angle between the two columns of C (the stored factor weights), per mouse,\n    averaged over the 9 2P mice.\n- id: methods-cvr2\n  statement: rSLDS models of miniscope data explain 84.7% of variance during engagement and\n    67.2% during observation of aggression (cross-validated R2).\n  source: Methods, Dynamical system models of neural data, paragraph 2\n  quote: Models fit to miniscope data during engagement of aggression obtained a cvR 2 = 84.7 ±\n    0.03%, while the same model explains 67.2 ± 0.02% of variance in data obtained from\n    observation of aggression\n  expected:\n  - quantity: cvR2, engagement, miniscope\n    value: 84.7\n    tolerance: 3\n    unit: percent\n  - quantity: cvR2, observation, miniscope\n    value: 67.2\n    tolerance: 2\n    unit: percent\n  criterion: Fivefold cross-validation, training on four portions and testing on the fifth\n    (Methods). The printed spreads (0.03% and 0.02%) are read as fractions (3 and 2 percentage\n    points), the only reading that fits a spread over 5 mice, and are used as tolerances. The\n    paper does not say whether the portions are contiguous blocks or random frames, or how R2\n    is taken (neural activity predicted from inferred latents); readings are contiguous\n    blocks and random frames. The Methods also require 70% cvR2 before downstream use, which\n    the observation value does not meet; this is reported.\n- id: fig1m-achw-x1-longer\n  statement: Neurons contributing to x1 have longer autocorrelation half-widths than those\n    contributing to x2 in head-fixed observation.\n  source: Figure 1l and 1m; Results, Line attractor for observing aggression, paragraph 4\n  quote: Neurons contributing to the integration dimension displayed more persistence than those\n    aligned with the faster dimension\n  statistics:\n  - test: two-tailed Mann-Whitney U-test\n    p: 0.0078\n    n: 9 mice (45 x1 and 45 x2 neurons)\n  depends_on:\n  - fig1e-2p-x1-slower\n  criterion: Five neurons per dimension per mouse (45 each over 9 mice, legend of Fig. 1l), the\n    five with the largest absolute weight on that dimension (Fig. 1i). ACHW as in\n    ed3e-achw-full-session, on the observation session. Per-mouse means compared by a\n    two-tailed Mann-Whitney test; reproduced when x1 exceeds x2 at p < 0.05.\n- id: ed5e-motion-explains-little\n  statement: Only a small fraction of neural activity is explained by the head-fixed observer's\n    movements, and the variance explained does not differ between x1 and x2 neurons.\n  source: Extended Data Fig. 5a-e; Results, Line attractor for observing aggression, paragraph 4\n  quote: Importantly, only a small fraction of the neural activity could be explained by movements of\n    the observer mouse\n  statistics:\n  - test: two-tailed Mann-Whitney U-test\n    p: 0.8125\n    n: 7 mice\n  criterion: GLM of each neuron on the first ten principal components of 500 motion SVDs at lags\n    up to 10 s, ridge, tenfold cross-validation, cvR2 (Methods). Reproduced when the median\n    cvR2 over neurons is below 0.1 (the paper gives no value; \"small fraction\" read as under\n    10% of variance, a reading named here and reported with the full distribution) and a\n    two-tailed Mann-Whitney test of per-mouse x1 against x2 means gives p >= 0.05. Needs the\n    face videos or their SVDs.\n# ---------------------------------------------------------------------------------------\n# Holographic perturbation of groups of five neurons (Figure 2, Extended Data Figs 5 to 9)\n- id: fig2d-x1-integration\n  statement: Photostimulation of five x1 neurons with four pulses at 20 s ISI produces\n    integration in the x1 dimension, with ISI activity rising with each pulse and not returning\n    to baseline.\n  source: Figure 2c and 2d; Results, Holographic activation shows integration, paragraph 2\n  quote: optogenetic reactivation of cohorts of five individual x 1 neurons yielded robust\n    integration of activity in the entire x 1 dimension-weighted population, as evidenced by\n    progressively increasing peak activity during the 20 s ISI after each consecutive pulse\n  statistics:\n  - test: Kruskal-Wallis test with Dunn's correction\n    p: 0.0363\n    n: 8 mice\n  - test: Kruskal-Wallis test with Dunn's correction\n    p: 0.0013\n    n: 8 mice\n  - test: Kruskal-Wallis test with Dunn's correction\n    p: 0.0067\n    n: 8 mice\n  criterion: The x1 projection of the x1-activation session (sample code). Per mouse, the mean\n    over baseline and over each ISI under readings Wa and Wb; Kruskal-Wallis with Dunn's\n    correction under readings Ca and Cb (header). Reproduced when, under one reading, at least\n    three Dunn comparisons give p < 0.05 and the mean over mice rises from the first to the\n    third ISI. Partially reproduced when the rise holds but fewer comparisons are significant.\n- id: fig2gh-x1-moves-along-attractor\n  statement: x1 photostimulation moves the population activity vector progressively along the\n    line attractor; the state-space distance from the initial point grows with each pulse,\n    both at the end of stimulation and at the end of each ISI.\n  source: Figure 2e-h; Results, Holographic activation shows integration, paragraph 3\n  quote: This revealed that the x 1 perturbations resulted in progressive, stable on-manifold\n    movement along the attractor with each consecutive stimulation, as measured by the increase in\n    both metrics\n  statistics:\n  - about: distance at stimulation end\n    test: Kruskal-Wallis test with Dunn's correction\n    p: 0.061\n    n: 8 mice\n  - about: distance at stimulation end\n    test: Kruskal-Wallis test with Dunn's correction\n    p: 0.029\n    n: 8 mice\n  - about: distance at stimulation end\n    test: Kruskal-Wallis test with Dunn's correction\n    p: 0.0018\n    n: 8 mice\n  - about: distance at stimulation end\n    test: Kruskal-Wallis test with Dunn's correction\n    p: 0.0059\n    n: 8 mice\n  - about: distance at ISI end\n    test: Kruskal-Wallis test with Dunn's correction\n    p: 0.1965\n    n: 8 mice\n  - about: distance at ISI end\n    test: Kruskal-Wallis test with Dunn's correction\n    p: 0.0082\n    n: 8 mice\n  - about: distance at ISI end\n    test: Kruskal-Wallis test with Dunn's correction\n    p: 0.0004\n    n: 8 mice\n  - about: distance at ISI end\n    test: Kruskal-Wallis test with Dunn's correction\n    p: 0.016\n    n: 8 mice\n  depends_on:\n  - fig2d-x1-integration\n  criterion: State = (x1 projection, x2 projection) of the x1-activation session. Euclidean\n    distance from t_initial to t_stim-end (onset + 2 s) and to t_post-stim (the frame before\n    the next onset; for the last pulse, onset + 21 s). t_initial is not fixed beyond \"during\n    the baseline period\"; readings are the mean baseline state and the last baseline frame.\n    What the distances are compared with is not given; readings are (a) each pulse against\n    the distances of baseline frames from t_initial and (b) each pulse against the first.\n    Kruskal-Wallis with Dunn's correction. Reproduced when, under one reading, the mean\n    distance rises from pulse 1 to pulse 3 for both metrics and three of four comparisons\n    give p < 0.05 for each metric, as the legends report.\n- id: ed7f-activated-x1-natural-levels\n  statement: Photoactivated x1 neurons reach peak activity comparable to their peak during\n    observation of aggression.\n  source: Extended Data Fig. 7d-f; Results, Holographic activation shows integration, paragraph 2\n  quote: Activated x 1 neurons exhibited activity levels comparable to their response during\n    observation of aggression\n  statistics:\n  - test: two-tailed Mann-Whitney U-test\n    p: 0.05\n    p_relation: \">\"\n    n: 8 mice\n  criterion: A claim of absence, judged on the paper's test. Per mouse, the mean over the five\n    targeted x1 neurons of their peak z-score during observation and during the activation\n    session; reproduced when a two-tailed Mann-Whitney test gives p >= 0.05. The difference is\n    reported.\n- id: ed8a-x1-integration-8s\n  statement: x1 activation with an 8 s ISI also produces integration in the x1 dimension.\n  source: Extended Data Fig. 8a; Results, Holographic activation shows integration, paragraph 2\n  quote: Similar results were obtained using an 8 s ISI\n  statistics:\n  - test: Kruskal-Wallis test with Dunn's correction\n    p: 0.3\n    n: 7 mice\n  - test: Kruskal-Wallis test with Dunn's correction\n    p: 0.0012\n    n: 7 mice\n  - test: Kruskal-Wallis test with Dunn's correction\n    p: 0.0012\n    n: 7 mice\n  - test: Kruskal-Wallis test with Dunn's correction\n    p: 0.0192\n    n: 7 mice\n  criterion: As fig2d-x1-integration, on the 8 s ISI x1-activation session (onsets at frames\n    140, 240, 340, 440). Reproduced when, under one reading, three of four comparisons give p <\n    0.05 and the mean rises from the first to the third ISI.\n- id: ed8ef-x1-scales-with-power\n  statement: x1 integration scales with laser power, being larger with 5 mW than with 1 mW per\n    neuron.\n  source: Extended Data Fig. 8e and 8f; Results, Holographic activation shows integration, paragraph 2\n  quote: This activity also scaled with different laser powers\n  statistics:\n  - test: two-tailed Mann-Whitney U-test\n    p: 0.0295\n    n: 8 mice\n  - test: two-tailed Mann-Whitney U-test\n    p: 0.0186\n    n: 8 mice\n  - test: two-tailed Mann-Whitney U-test\n    p: 0.045\n    n: 8 mice\n  - test: two-tailed Mann-Whitney U-test\n    p: 0.7\n    n: 8 mice\n  criterion: Per mouse and period (baseline and each ISI, readings Wa and Wb), the mean x1\n    projection at 1 mW and at 5 mW; per period, a two-tailed Mann-Whitney test. Reproduced\n    when three of the four ISIs give 5 mW higher at p < 0.05 under one reading (the legend's\n    four values have three below 0.05; the fourth is read as the baseline or one ISI).\n- id: ed8c-model-integrates\n  statement: Given the same pulsed input, the rSLDS model fit to observation data also\n    integrates along x1, as in the data.\n  source: Extended Data Fig. 8c; Results, Holographic activation shows integration, paragraph 2\n  quote: Providing the same (digital optogenetic) input to the fit rSLDS model also resulted in\n    integration by the model along the x 1 dimension, similar to that observed in the data\n  depends_on:\n  - fig1e-2p-x1-slower\n  criterion: The paper does not say how the input enters the model. Readings are (a) the input\n    weight learned for the BALB/c-presence input of the observation fit (Methods, flow fields\n    fit with input terms) driven by a 2 s pulse at each stimulation onset; (b) a pulse added\n    to x1 at each onset, of the size of the first evoked x1 response. The model is simulated\n    forward from the baseline state with its discrete states. Reproduced when the simulated\n    x1 at the end of each ISI rises from the first to the third ISI in at least 6 of the 8\n    mice under one reading; the cross-validated R2 against the data (about 85%, Methods) is\n    reported.\n- id: ed8gi-x1-stim-no-x2\n  statement: x1 stimulation does not evoke appreciable activity in the x2 dimension.\n  source: Extended Data Fig. 8g-i; Results, Holographic activation shows integration, paragraph 2\n  quote: Importantly, x 1 stimulation did not evoke appreciable activity in x 2 dimension neurons\n  statistics:\n  - test: Kruskal-Wallis test with Dunn's correction\n    p: 0.05\n    p_relation: \">\"\n    n: 8 mice\n  criterion: A claim of absence, judged on the paper's test. The x2 projection of the\n    x1-activation session, per mouse means of baseline and ISIs (Wa, Wb), Kruskal-Wallis with\n    Dunn's correction (Ca, Cb). Reproduced when no comparison gives p < 0.05 under the reading\n    used for fig2d-x1-integration; the size of each difference is reported.\n- id: fig2k-x2-no-integration\n  statement: Photostimulation of five x2 neurons does not produce integration; x2 activity is\n    transient and decays to baseline during each ISI.\n  source: Figure 2i-k; Results, Holographic activation shows integration, paragraph 4\n  quote: Importantly, activation of x 2 neurons did not lead to integration\n  statistics:\n  - test: Kruskal-Wallis test with Dunn's correction\n    p: 0.99\n    p_relation: \">\"\n    n: 7 mice\n  criterion: A claim of absence, judged on the paper's test. As fig2d-x1-integration, on the x2\n    projection of the x2-activation session; reproduced when no Dunn comparison gives p < 0.05.\n- id: ed8b-x2-no-integration-8s\n  statement: With an 8 s ISI, x2 activation also produces no integration in x2.\n  source: Extended Data Fig. 8b; Results, Holographic activation shows integration, paragraph 4\n  quote: we observed stimulus-locked transient activity in the x 2 dimension followed by a decay back\n    to the baseline during the ISI period, across stimulation paradigms\n  statistics:\n  - test: Kruskal-Wallis test with Dunn's correction\n    p: 0.05\n    p_relation: \">\"\n    n: 7 mice\n  criterion: As fig2k-x2-no-integration, on the 8 s ISI x2-activation session.\n- id: ed8jl-x2-stim-little-x1\n  statement: x2 activation has little effect on x1 activity; in the paper's test two of four\n    comparisons are not significant (P = 0.276) and two are (P = 0.0072 and 0.03).\n  source: Extended Data Fig. 8j-l; Results, Holographic activation shows integration, paragraph 4\n  quote: with little to no effect on x 1 neurons\n  statistics:\n  - test: Kruskal-Wallis test with Dunn's correction\n    p: 0.276\n    n: 8 mice\n  - test: Kruskal-Wallis test with Dunn's correction\n    p: 0.0072\n    n: 8 mice\n  - test: Kruskal-Wallis test with Dunn's correction\n    p: 0.03\n    n: 8 mice\n  criterion: The x1 projection of the x2-activation session, tested as fig2d-x1-integration.\n    The paper's own test finds two significant comparisons, so the claim is judged against\n    that pattern. Reproduced when, under one reading, at most two comparisons give p < 0.05\n    and the mean ISI x1 response is smaller than under x1 activation (fig2d-x1-integration) in\n    every ISI. The legend reports n = 8, though Fig. 2k has 7 mice with x2 activation; the\n    number found is reported.\n- id: fig2no-x2-off-manifold\n  statement: x2 activation moves the population vector transiently off the attractor during\n    each pulse, after which it relaxes back near its initial location.\n  source: Figure 2l-o; Results, Holographic activation shows integration, paragraph 4\n  quote: we observed that x 2 neuron activation caused transient off-manifold movements of the PAV\n    orthogonal to the attractor axis during each pulse ... After each stimulus, the PAV relaxed\n    back into the attractor, near to the initial location that it occupied before the stimulus\n  statistics:\n  - about: distance at stimulation end\n    test: Kruskal-Wallis test with Dunn's correction\n    p: 0.1554\n    n: 7 mice\n  - about: distance at stimulation end\n    test: Kruskal-Wallis test with Dunn's correction\n    p: 0.042\n    n: 7 mice\n  - about: distance at stimulation end\n    test: Kruskal-Wallis test with Dunn's correction\n    p: 0.029\n    n: 7 mice\n  - about: distance at ISI end\n    test: Kruskal-Wallis test with Dunn's correction\n    p: 0.508\n    n: 7 mice\n  - about: distance at ISI end\n    test: Kruskal-Wallis test with Dunn's correction\n    p: 0.0383\n    n: 7 mice\n  depends_on:\n  - fig2gh-x1-moves-along-attractor\n  criterion: As fig2gh-x1-moves-along-attractor, on the x2-activation session. Reproduced\n    when, under one reading, at least three of four stimulation-end comparisons give p < 0.05\n    and at most one ISI-end comparison does (the legends' pattern), and the mean ISI-end\n    distance is smaller than the mean stimulation-end distance.\n- id: ed9d-attractor-finite\n  statement: Integration of pulses saturates after the third pulse; a model with a finite\n    attractor fits the x1 response better than an infinite one.\n  source: Extended Data Fig. 9a-d; Results, Holographic activation shows integration, paragraph 3\n  quote: we found that integration of optogenetic stimulation pulses saturated in the x 1 dimension\n    after the third pulse, suggesting that the line attractor occupies a finite portion of the\n    neural state space\n  statistics:\n  - about: whole trace\n    test: two-tailed Mann-Whitney U-test\n    p: 0.001\n    p_relation: \"<\"\n    n: 8 mice\n  - about: after the third pulse\n    test: two-tailed Mann-Whitney U-test\n    p: 0.001\n    p_relation: \"<\"\n    n: 8 mice\n  depends_on:\n  - fig2d-x1-integration\n  criterion: The two models are described only by their predictions (further pulses add no ramp\n    once the system reaches a point, against each pulse adding the same step). Readings are\n    (a) a step model fit to the x1 trace whose cumulative level is capped at a fitted maximum,\n    against the same model uncapped; (b) the mean ISI levels compared directly, saturation\n    being ISI4 not above ISI3 while ISI3 is above ISI2. Reproduced when under (a) the capped\n    model has lower mean square error in the whole trace and after the third pulse by\n    Mann-Whitney across mice at p < 0.05, or under (b) the pattern holds across mice.\n- id: ed9i-points-along-line-attractive\n  statement: x2 stimulation after x1 has moved the system along the attractor perturbs it off\n    the line, after which it relaxes to the position reached after x1 stimulation and not to\n    baseline.\n  source: Extended Data Fig. 9e-i; Results, Holographic activation shows integration, paragraph 4\n  quote: This x 2 perturbation also resulted in transient off-manifold movements of the PAV orthogonal\n    to the line attractor, followed by relaxation to the position occupied after the previous x 1\n    stimulation\n  statistics:\n  - test: Kruskal-Wallis test with Dunn's correction\n    p: 0.0025\n    n: 8 mice\n  criterion: In the combined session, the distance from baseline of the state after each\n    stimulation (the legend's \"activity distance from baseline after each photostimulation\").\n    Reproduced when the state after x2 stimulation remains farther from baseline than the\n    baseline state (Dunn p < 0.05 for the post-x1 point) and does not differ from the state\n    before x2 stimulation (p >= 0.05). The time points are not given; readings are the frame\n    before the next onset and the mean over each ISI (Wa).\n- id: ed9mn-random-neurons-no-effect\n  statement: Activating randomly selected neurons that are not weighted by either dimension does\n    not produce activity along x1 or x2.\n  source: Extended Data Fig. 9j-n; Results, Holographic activation shows integration, paragraph 4\n  quote: activation of randomly selected neurons that were not weighted by either dimension did not\n    produce activity along either the x 1 or x 2 dimension\n  statistics:\n  - about: x1 dimension\n    test: Kruskal-Wallis test with Dunn's correction\n    p: 0.05\n    p_relation: \">\"\n    n: 5 mice\n  - about: x2 dimension\n    test: Kruskal-Wallis test with Dunn's correction\n    p: 0.05\n    p_relation: \">\"\n    n: 5 mice\n  criterion: A claim of absence, judged on the paper's test. As fig2d-x1-integration on the x1\n    and on the x2 projection of the random-activation session; reproduced when no comparison\n    gives p < 0.05 in either.\n- id: ed5hj-no-behaviour-change\n  statement: Activating x1 or x2 ensembles does not change the head-fixed mouse's movements.\n  source: Extended Data Fig. 5f-j; Results, Holographic activation shows integration, paragraph 4\n  quote: Activation of either ensemble did not result in overt changes in the behaviour of the\n    head-fixed mouse\n  statistics:\n  - test: two-tailed Mann-Whitney U-test\n    p: 0.05\n    p_relation: \">\"\n    n: 8 mice\n  criterion: A claim of absence, judged on the paper's test. Per mouse, the mean of each of the\n    top five motion SVDs before and during stimulation; reproduced when no two-tailed\n    Mann-Whitney test gives p < 0.05. Needs the face videos or their SVDs.\n- id: ed6k-no-spatial-clustering\n  statement: x1 and x2 neurons are not spatially clustered; distances within and between the two\n    groups do not differ.\n  source: Extended Data Fig. 6i-k; Results, Holographic activation shows integration, paragraph 1\n  quote: did not observe spatial clustering of x 1 or x 2 neurons\n  statistics:\n  - test: Kruskal-Wallis test with Dunn's correction\n    p: 0.05\n    p_relation: \">\"\n    n: 8 mice\n  criterion: A claim of absence, judged on the paper's test. Per mouse, the mean pairwise\n    distance within x1, within x2 and between x1 and x2 neurons, from cell centroids;\n    reproduced when no Dunn comparison gives p < 0.05. Which neurons count as x1 and x2 is read\n    as in ed3c-x1-activity-observe-vs-engage.\n- id: ed7bc-no-spatial-decoding\n  statement: A linear SVM cannot separate x1 from x2 neurons by position better than shuffled\n    labels.\n  source: Extended Data Fig. 7a-c\n  quote: Accuracy of SVM decoder trained on data versus shuffled control (n=10 mice, p=0.156\n  statistics:\n  - about: accuracy\n    test: two-tailed Mann-Whitney U-test\n    p: 0.156\n    n: 10 mice\n  - about: classification width\n    test: two-tailed Mann-Whitney U-test\n    p: 0.578\n    n: 10 mice\n  criterion: A claim of absence, judged on the paper's test. Linear SVM on cell positions per\n    FOV, shuffles by random assignment of identity, 20 repeats, mean accuracy (Methods, Spatial\n    cluster decoder). The cross-validation is not given; readings are leave-one-out and\n    fivefold. Reproduced when the two-tailed Mann-Whitney test of accuracy gives p >= 0.05.\n    The n of 10 mice is more than the 9 of Fig. 1; the number found is reported.\n- id: ed6g-offtarget-15um\n  statement: Photostimulation through the GRIN lens is spatially confined; the response of a\n    reference cell is close to zero when the spiral is 15 um from its soma.\n  source: Extended Data Fig. 6d-h\n  quote: Note that at 15 µm the average response in the reference cells is close to zero\n  criterion: Per reference cell (17 cells), the mean response at each offset from the soma.\n    Reproduced when the mean at 15 um is below 10% of the mean at 0 um (the paper gives no\n    value; \"close to zero\" read as under a tenth of the on-soma response, a reading named\n    here). Needs the calibration recordings.\n# ---------------------------------------------------------------------------------------\n# Follower cells and functional connectivity (Figure 3, Extended Data Fig. 10)\n- id: ed10c-followers-integrate\n  statement: Non-targeted x1 neurons outside 50 um of the targeted cells integrate during group\n    x1 activation.\n  source: Extended Data Fig. 10a-c; Results, Line-attractor neurons form ensembles, paragraph 1\n  quote: even after excluding the targeted x 1 neurons themselves as well as potentially off-target\n    neurons located within a 50 µm radius of the targeted cell ... we observed integration in the\n    remaining x 1 neurons\n  statistics:\n  - test: Kruskal-Wallis test with Dunn's correction\n    p: 0.001\n    p_relation: \"<\"\n    n: 8 mice\n  depends_on:\n  - fig2d-x1-integration\n  criterion: In the x1-activation session, x1 neurons that are not targeted and lie more than 50\n    um from every targeted cell; their weighted average activity (weights from the x1 factor),\n    tested as fig2d-x1-integration. Reproduced when at least one ISI exceeds baseline at p <\n    0.001 under one reading and the mean rises from the first to the third ISI.\n- id: ed10g-follower-decoding\n  statement: Integrated activity of targeted x1 neurons is decoded better from non-targeted x1\n    neurons (about 80% variance explained) than from non-targeted x2 or random neurons (about\n    40%).\n  source: Extended Data Fig. 10d-g; Results, Line-attractor neurons form ensembles, paragraph 1\n  quote: Decoding from non-targeted x 1 neurons can explain significantly more variance (80% versus\n    40%) than non-targeted x 2 or randomly selected neurons (n = 8 mice, *p = 0.01, ***p = 0.0003\n  statistics:\n  - test: Kruskal-Wallis test with Dunn's correction\n    p: 0.01\n    n: 8 mice\n  - test: Kruskal-Wallis test with Dunn's correction\n    p: 0.0003\n    n: 8 mice\n  expected:\n  - quantity: variance explained from non-targeted x1 neurons\n    value: 80\n    tolerance: 8\n    unit: percent\n  - quantity: variance explained from non-targeted x2 or random neurons\n    value: 40\n    tolerance: 4\n    unit: percent\n  depends_on:\n  - ed10c-followers-integrate\n  criterion: A support vector machine decoder (legend) predicting the mean activity of the\n    targeted x1 neurons from non-targeted neurons. Not given and named as open, with readings,\n    are the regression form (linear support vector regression), the number of neurons in each\n    set (equal to the smaller set, random subsets of the same size for the random set), and the\n    validation (fivefold over contiguous blocks). Reproduced when x1 exceeds both x2 and random\n    by Dunn's test at p < 0.05 and the values are within tolerance; partially when the order\n    holds without the values.\n- id: ed10hi-responses-mostly-positive\n  statement: Responses of non-targeted neurons to single x1 neuron stimulation are mostly\n    positive.\n  source: Extended Data Fig. 10h and 10i; Results, Line-attractor neurons form ensembles, paragraph 2\n  quote: These experiments revealed a slowly decaying elevation of activity during the ISI period in\n    non-targeted x 1 neurons after each pulse of activation (Fig. 3b,d ) that was mostly positive\n  criterion: A neuron's response is positive or negative when its mean response after\n    photostimulation is 1.5 standard deviations above or below its baseline (legend of\n    Extended Data Fig. 10h). The post-stimulation window is not given; readings Wa and Wb.\n    Reproduced when positive responders outnumber negative responders, pooled over the unitary\n    x1 stimulation sessions and in at least 5 of 8 mice.\n- id: ed10lm-distance-not-explaining\n  statement: Putative follower x1 neurons lie on average 139 +/- 35 um from the targeted cell,\n    11% within 50 um, and their response is not positively correlated with distance.\n  source: Extended Data Fig. 10j-n; Results, Line-attractor neurons form ensembles, paragraph 2\n  quote: Notably, the strength of functional connectivity was not positively correlated with the\n    distance from the targeted photostimulated cell\n  expected:\n  - quantity: mean distance of putative follower x1 neurons from the targeted x1 neuron\n    value: 139\n    tolerance: 35\n    unit: um\n  - quantity: fraction of putative follower x1 neurons within 50 um\n    value: 11\n    tolerance: 1.1\n    unit: percent\n  criterion: A putative follower is a non-targeted x1 neuron that responded to stimulation (the\n    1.5 SD rule of ed10hi-responses-mostly-positive; Methods, Terminology) of a single\n    targeted x1 neuron. Expected values within tolerance, and the correlation of response with\n    distance (the legend's regression line) not positive at p < 0.05 by a Pearson test.\n- id: ed10p-exclusion-no-change\n  statement: Excluding neurons within 50 um of the targeted cell does not change the follower\n    response to single x1 neuron stimulation.\n  source: Extended Data Fig. 10o and 10p; Results, Line-attractor neurons form ensembles, paragraph 2\n  quote: was still observed even after excluding neurons in a 50 µm zone surrounding the targeted\n    neuron\n  statistics:\n  - test: Kruskal-Wallis test with Dunn's correction\n    p: 0.05\n    p_relation: \">\"\n    n: 8 mice\n  criterion: A claim of absence, judged on the paper's test. Per mouse and ISI, the mean\n    response of non-targeted x1 neurons with and without the exclusion; reproduced when no\n    Dunn comparison gives p < 0.05.\n- id: ed10r-scales-with-number\n  statement: The response of non-targeted x1 neurons scales with the number of targeted x1\n    neurons, larger with five than with one.\n  source: Extended Data Fig. 10q and 10r; Results, Line-attractor neurons form ensembles, paragraph 2\n  quote: revealed that the response strength of the non-targeted x 1 neurons scaled with the number of\n    targeted x 1 neurons\n  statistics:\n  - test: Kruskal-Wallis test with Dunn's correction\n    p: 0.0239\n    n: 8 mice\n  - test: Kruskal-Wallis test with Dunn's correction\n    p: 0.0063\n    n: 8 mice\n  - test: Kruskal-Wallis test with Dunn's correction\n    p: 0.0074\n    n: 8 mice\n  - test: Kruskal-Wallis test with Dunn's correction\n    p: 0.0341\n    n: 8 mice\n  criterion: Per mouse and ISI (Wa, Wb), the mean x1 projection over non-targeted x1 neurons in\n    the one-neuron and the five-neuron sessions, compared per ISI by Dunn's test. Reproduced\n    when five exceeds one in all four ISIs at p < 0.05 under one reading; partially when in two\n    or three.\n- id: fig3d-single-x1-drives-x1\n  statement: Stimulating single x1 neurons raises the activity of non-targeted x1 neurons, with\n    a slowly decaying elevation during the ISI.\n  source: Figure 3a, 3b and 3d; Results, Line-attractor neurons form ensembles, paragraph 2\n  quote: These experiments revealed a slowly decaying elevation of activity during the ISI period in\n    non-targeted x 1 neurons after each pulse of activation\n  statistics:\n  - test: Kruskal-Wallis test with Dunn's correction\n    p: 0.16\n    n: 8 mice (25 targeted neurons)\n  - test: Kruskal-Wallis test with Dunn's correction\n    p: 0.0037\n    n: 8 mice (25 targeted neurons)\n  - test: Kruskal-Wallis test with Dunn's correction\n    p: 0.0005\n    n: 8 mice (25 targeted neurons)\n  - test: Kruskal-Wallis test with Dunn's correction\n    p: 0.0016\n    n: 8 mice (25 targeted neurons)\n  criterion: The average z-scored activity of non-targeted x1 neurons in the unitary x1\n    sessions, per mouse (averaged over its targeted neurons), tested as fig2d-x1-integration.\n    Reproduced when, under one reading, three of four comparisons give p < 0.05, as the legend\n    reports.\n- id: fig3e-single-x1-not-x2\n  statement: Stimulating single x1 neurons does not raise activity in non-targeted x2 neurons.\n  source: Figure 3c and 3e; Results, Line-attractor neurons form ensembles, paragraph 3\n  quote: we observed little activity in non-targeted x 2 neurons after activation of unitary x 1 or x\n    2 neurons\n  statistics:\n  - test: Kruskal-Wallis test with Dunn's correction\n    p: 0.05\n    p_relation: \">\"\n    n: 8 mice\n  criterion: A claim of absence, judged on the paper's test. As fig3d-single-x1-drives-x1 on\n    non-targeted x2 neurons; reproduced when no comparison gives p < 0.05.\n- id: fig3i-single-x2-not-x1\n  statement: Stimulating single x2 neurons gives a trend toward rising activity in non-targeted\n    x1 neurons that the text calls not statistically significant.\n  source: Figure 3f-i; Results, Line-attractor neurons form ensembles, paragraph 3\n  quote: While there was a trend to a gradual increase in activity in non-targeted x 1 neurons after\n    repeated activation of unitary x 2 neurons (Fig. 3f–h ), that increase was not statistically\n    significant\n  statistics:\n  - test: Kruskal-Wallis test with Dunn's correction\n    p: 0.999\n    n: 7 mice (18 targeted neurons)\n  - test: Kruskal-Wallis test with Dunn's correction\n    p: 0.31\n    n: 7 mice (18 targeted neurons)\n  - test: Kruskal-Wallis test with Dunn's correction\n    p: 0.09\n    n: 7 mice (18 targeted neurons)\n  - test: Kruskal-Wallis test with Dunn's correction\n    p: 0.0316\n    n: 7 mice (18 targeted neurons)\n  criterion: A claim of absence, judged on the paper's test, as fig3d-single-x1-drives-x1 on\n    non-targeted x1 neurons in the unitary x2 sessions. Reproduced when no comparison gives p <\n    0.05. The legend itself reports one comparison at P = 0.0316 against the text's \"not\n    statistically significant\"; the attempt reports which comparisons reach 0.05.\n- id: fig3j-single-x2-not-x2\n  statement: Stimulating single x2 neurons does not raise activity in non-targeted x2 neurons.\n  source: Figure 3g and 3j; Results, Line-attractor neurons form ensembles, paragraph 3\n  quote: Quantification of activity in non-targeted x 2 neurons after targeting of single x 2\n    neurons (NS)\n  statistics:\n  - test: Kruskal-Wallis test with Dunn's correction\n    p: 0.05\n    p_relation: \">\"\n    n: 7 mice\n  criterion: A claim of absence, judged on the paper's test. As fig3d-single-x1-drives-x1 on\n    non-targeted x2 neurons in the unitary x2 sessions; reproduced when no comparison gives p <\n    0.05.\n- id: fig4a-dense-x1-connectivity\n  statement: About 36% of x1-to-x1 pairs have influence scores above the highest x1-to-x2 pair\n    (a z-score of about 0.6), a relatively dense functional ensemble.\n  source: Figure 4a; Results, Line-attractor neurons form ensembles, paragraph 4\n  quote: we considered the percentage of x 1 → x 1 pairs that had influence scores higher than the\n    highest x 1 → x 2 pair, which had a z score of around 0.6 ... The fraction of x 1 → x 1 pairs\n    above this threshold was around 36%\n  expected:\n  - quantity: fraction of x1-to-x1 pairs above the highest x1-to-x2 influence score\n    value: 36\n    tolerance: 3.6\n    unit: percent\n  - quantity: highest x1-to-x2 influence score\n    value: 0.6\n    tolerance: 0.06\n    unit: z-score\n  criterion: Influence score = the average evoked z-scored activity of each non-targeted\n    photoactivated neuron after photostimulation of a single targeted cell (Results). The\n    averaging window is not given; readings Wa and Wb pooled over the four ISIs. The legend\n    counts 99 pairs from 7 mice; the pair counts found are reported. Reproduced when both\n    values are within tolerance under one reading.\n# ---------------------------------------------------------------------------------------\n# Network model (Figure 4, Extended Data Fig. 11); a simulation, no recorded data\n- id: fig4ce-excitatory-network\n  statement: In purely excitatory spiking networks, only relatively sparse integration\n    subnetworks (around 8 to 12%) with slow synaptic time constants (around 20 s) give network\n    time constants of 50 to 200 s; fast glutamatergic networks fail over the same densities.\n  source: Figure 4c-f; Results, Line-attractor neurons form ensembles, paragraph 5\n  quote: we found that only artificial networks based on relatively sparse connectivity (around 8–12%)\n    and slow synaptic time constants (around 20 s) could yield network time constants ( τ n ) in the\n    experimentally observed range (~50–200 s; Fig. 4c,e (red shading)). By contrast, networks with\n    fast glutamatergic connectivity failed to do so over the same range of connection densities\n  criterion: A simulation as the Methods give it (Mechanistic modelling), 1,000 neurons, a\n    200-neuron subnetwork, weights U(0, 1/N) and U(0, 1/Np), tau_n = tau_s / (1 - lambda_max).\n    Reproduced when, at tau_s = 20 s, tau_n falls in 50 to 200 s (widened 10%, 45 to 220 s) for\n    some density between 8% and 12% (widened, 7.2% to 13.2%), and at tau_s of 0.6 s or less no\n    stable density gives tau_n of 45 s or more. Uses no recorded data.\n- id: fig4hj-inhibition-slow-dense\n  statement: With fast feedback inhibition, a network with slow transmission (20 s) and the\n    measured 36% density integrates pulsed input like the data, while a fast glutamatergic\n    network (100 ms) does not.\n  source: Figure 4g-l; Results, Line-attractor neurons form ensembles, paragraph 6\n  quote: networks simulated with a long τ s (20s) and dense σ (36%) could integrate digital\n    optogenetic stimulation in a manner like that observed experimentally ... By contrast, purely\n    glutamatergic networks ( τ s = 100 ms) were unable to integrate at the observed timescales given\n    the measured connectivity density\n  depends_on:\n  - fig4a-dense-x1-connectivity\n  criterion: The Methods network with inhibition (tau_I 50 ms, g = 1, g_inh 1.25, 5 or 10), four\n    smoothed input pulses at 20 s ISI to a random 25% of neurons, Euler steps of 1 ms, noise\n    N(0,1)/5. The pulse width and the calcium kernel are not given (readings 2 s, as in vivo,\n    and an exponential kernel of 1 s decay as a standard choice that cannot change whether\n    activity integrates). Reproduced when the subnetwork's mean rate at the end of each ISI\n    rises from the first to the third ISI at tau_s 20 s and does not at tau_s 0.1 s, for one of\n    the g_inh values. Uses no recorded data.\n# ---------------------------------------------------------------------------------------\n# Attractor stability and connectivity (Figure 5, Extended Data Fig. 12)\n- id: fig5g-time-constant-vs-connectivity\n  statement: Across mice, the x1 time constant during observation correlates strongly with the\n    functional connectivity among x1 neurons measured as the AUC of non-targeted x1 neurons\n    after the third pulse (R2 = 0.87).\n  source: Figure 5g; Results, Attractor stability ties to connectivity, paragraph 2\n  quote: The strength of this correlation was higher after the third stimulus ( r 2 = 0.87) compared\n    with after the first stimulus ( r 2 = 0.59)\n  statistics:\n  - test: linear correlation\n    statistic: R2 = 0.87\n    p: 0.001\n    p_relation: \"<\"\n    n: 8 mice\n  expected:\n    quantity: R2 of x1 time constant against AUC after the third stimulus\n    value: 0.87\n    tolerance: 0.087\n  depends_on:\n  - fig1e-2p-x1-slower\n  - fig3d-single-x1-drives-x1\n  criterion: Per mouse, the x1 time constant of its observation fit (the \"intrinsic leak rate\"\n    over the whole session, Methods; readings are the largest time constant over states and\n    the x1 time constant of the state occupied after BALB/c removal) and the AUC of the\n    average z-scored activity of non-targeted x1 neurons in its unitary x1 sessions after the\n    third pulse (readings Wa and Wb for the window). Pearson R2 and its p-value over 8 mice.\n    Reproduced when R2 is within tolerance and p < 0.001 under one reading; partially when p <\n    0.05 with a positive slope.\n- id: ed12-first-stimulus-weaker\n  statement: The correlation is weaker after the first stimulus (R2 = 0.59) than after the third.\n  source: Extended Data Fig. 12c and 12d; Results, Attractor stability ties to connectivity, paragraph 2\n  quote: The strength of this correlation was higher after the third stimulus ( r 2 = 0.87) compared\n    with after the first stimulus ( r 2 = 0.59)\n  expected:\n    quantity: R2 of x1 time constant against AUC after the first stimulus\n    value: 0.59\n    tolerance: 0.059\n  depends_on:\n  - fig5g-time-constant-vs-connectivity\n  criterion: As fig5g-time-constant-vs-connectivity, after the first pulse. Reproduced when R2\n    is within tolerance and below the third-pulse R2 under the same reading. The Extended Data\n    Fig. 12b legend gives r2 0.87 for x2 neurons after the third stimulus, which conflicts with\n    the Results and with Fig. 12e-h; it is not used.\n- id: fig5f-ramp-not-correlated\n  statement: The rate of ramp-up along x1 does not correlate with functional connectivity\n    among x1 neurons (r2 = 0.01).\n  source: Figure 5f; Extended Data Fig. 12b-d; Results, Attractor stability ties to connectivity, paragraph 2\n  quote: By contrast, there was no correlation between functional connectivity and the rate of\n    ramp-up, suggesting that the latter might be driven by extrinsic inputs to the VMHvl\n  statistics:\n  - test: linear correlation\n    statistic: r2 = 0.01\n    p: 0.05\n    p_relation: \">\"\n    n: 8 mice\n  depends_on:\n  - fig5g-time-constant-vs-connectivity\n  criterion: A claim of absence, judged on the paper's test, a linear correlation over 8 mice.\n    The rate of ramp-up is not defined; readings are (a) the slope of a linear fit to x1 from\n    BALB/c entry to the x1 maximum while the intruder is present and (b) the x1 rise over the\n    first 10 s after entry divided by 10 s. AUC after the third pulse as in fig5g. Reproduced\n    when p >= 0.05 under the reading used; r2 is reported.\n- id: ed12eh-x1-to-x2-not-correlated\n  statement: The time constant does not correlate with the influence of targeted x1 neurons on\n    non-targeted x2 neurons, so the relation is specific to the x1 subnetwork.\n  source: Extended Data Fig. 12e-h; Results, Attractor stability ties to connectivity, paragraph 2\n  quote: the correlation between attractor stability and functional connectivity was specific to\n    neurons in the integration ( x 1 ) subnetwork, and did not hold when rSLDS time constants were\n    compared with the influence strength of targeted x 1 neurons on x 2 cells\n  depends_on:\n  - fig5g-time-constant-vs-connectivity\n  criterion: A claim of absence. As fig5g-time-constant-vs-connectivity with non-targeted x2\n    neurons, for AUC and average z-score after the first and the third pulse (the four panels\n    e to h). The legend gives no test; the Pearson test of fig5g is used. Reproduced when none\n    of the four correlations gives p < 0.05.\n"
}
```

```
File created successfully at: claims/001037/10.1038-s41586-024-07915-x.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001037/10.1038-s41586-024-07915-x.yaml paper/10.1038-s41586-024-07915-x.txt; grep -n -- "—\|rather" claims/001037/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent**

Checker passes. Two quotes dropped a space after a colon to keep YAML plain scalars valid; I'll restore them word for word using quoted scalars.

**Agent calls Bash**

```bash
grep -n "[a-z]:[0-9A-Z]" claims/001037/*.yaml | grep -v "^\S*:[0-9]*:#"; python3 - <<'E'
import yaml,re
d=yaml.safe_load(open('claims/001037/10.1038-s41586-024-07915-x.yaml'))
t=open('paper/10.1038-s41586-024-07915-x.txt').read()
t=re.sub(r'\s+',' ',t)
for c in d['claims']:
    q=c.get('quote')
    if not q: continue
    for f in q.split('...'):
        f=re.sub(r'\s+',' ',f).strip(' .,;')
        if f and f not in t: print(c['id'],'|',f[:90])
E
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 - <<'E'
p='claims/001037/10.1038-s41586-024-07915-x.yaml'
s=open(p).read()
s=s.replace('''  quote: mean achw during observation:25 ± 0.8s, mean achw during engagement:20 ± 1.7s, n=5 mice,
    p = 0.125''','''  quote: "mean achw during observation: 25 ± 0.8s, mean achw during engagement: 20 ± 1.7s, n=5 mice,
    p = 0.125"''')
s=s.replace('''  quote: mean achw during observation:14 ± 1s, mean achw during engagement:11 ± 1.6s, n = 5 mice,
    p = 0.187''','''  quote: "mean achw during observation: 14 ± 1s, mean achw during engagement: 11 ± 1.6s, n = 5 mice,
    p = 0.187"''')
s=s.replace('''  quote: A SVM decoder was trained on data from integration dimension activity to separate bouts of
    observing attack from non attack bouts. Right:Quantification of the decoder accuracy performance
    (n = 5 mice, p = 0.0079''','''  quote: "A SVM decoder was trained on data from integration dimension activity to separate bouts of
    observing attack from non attack bouts. Right: Quantification of the decoder accuracy performance
    (n = 5 mice, p = 0.0079"''')
open(p,'w').write(s)
E
python tools/claims_check.py claims/001037/10.1038-s41586-024-07915-x.yaml paper/10.1038-s41586-024-07915-x.txt
python3 - <<'E'
import yaml,re
d=yaml.safe_load(open('claims/001037/10.1038-s41586-024-07915-x.yaml'))
t=re.sub(r'\s+',' ',open('paper/10.1038-s41586-024-07915-x.txt').read())
print(sum(1 for c in d['claims'] for f in c.get('quote','').split('...') if f.strip() and re.sub(r'\s+',' ',f).strip(' .,;') not in t))
print(len(d['claims']), sum('criterion' in c for c in d['claims']), sum(len(c.get('statistics',[])) for c in d['claims']), sum('statistics' in c for c in d['claims']))
E
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote the claims file at `claims/001037/10.1038-s41586-024-07915-x.yaml`. The quote checker reports 0 problems, and every quote also matches the text exactly, spaces included. Nothing is committed.

**Text read.** The version of record from Europe PMC (PMC11499281, corrected publication 2025): main text, Methods, and the legends of Figs 1 to 5 and Extended Data Figs 1 to 12. The supplement is only a Reporting Summary, which no result rests on. No PDF was supplied, so I read no figure panels; findings shown only in a panel come from its legend or the Results.

**Code read.**
- The paper links only `lindermanlab/ssm` (commit eb6c8aa), the general rSLDS fitting library, with no analysis of this paper.
- The dataset's description links the authors' sample code, `neuralcomputation/hypothalamic-dynamics` (commit 28fee70). I read its code and not its example data files, and ranked it below the Methods. It settles four things:
  - the time-constant formula, |1/log|λ|| divided by the frame rate, in seconds;
  - how activity is projected onto x1 and x2, using stored rSLDS weights, smoothing and baseline windows;
  - the stimulation onset frames for the 20 s and 8 s gaps between pulses;
  - the rSLDS fitting settings, which the notebooks call "representative", so I used them as one reading next to the Methods' cross-validated number of states.

**Counts.** 54 claims:
- 53 have quotes; one is `inferred` (Fig. 1f, the line attractor score, which no sentence states).
- 40 claims record statistics, 75 statistical values in all.
- All 54 have criteria. 18 have expected values.
- The 2 network-model claims (Fig. 4) are simulations that use no recorded data.

**Details the paper leaves open, and the readings named:**
- **Gap windows** for "baseline or ISIs": from the end of the 2 s pulse to the next onset, or from onset to onset.
- **Which Dunn comparisons** the printed p-values belong to: each gap against baseline, or each gap against the one before.
- **State-space distance** (Fig. 2g,h,n,o): the starting point is either the mean baseline state or the last baseline frame. Each pulse is compared either with baseline-frame distances or with the first pulse.
- **Which neurons count as x1 and x2**: the top five by absolute weight (as in Fig. 1i), or whatever the dataset marks.
- **Which state's time constant** is x1's: the largest over states, or the state occupied after the intruder is removed.
- **Ramp-up rate** (Fig. 5f): the slope from BALB/c entry to the x1 peak, or the rise over the first 10 s.
- **Shared undefined measures:**
  - the AUC window, and the window for the influence scores;
  - the autocorrelation half-width, read as the first lag at or below 0.5;
  - the transient frequency unit, per baseline or per minute;
  - the decay-constant fit.
- **Decoders:** the train/test split, and for the follower decoder the regression form, the set sizes and the validation.
- **How a model or cross-validation is set up:**
  - how the pulse input enters the rSLDS model (Extended Data Fig. 8c);
  - what the finite and infinite attractor models are (Extended Data Fig. 9);
  - how the cross-validation folds are formed (contiguous blocks or random frames).
- **Thresholds the paper never gives a number for:** "small fraction" of variance explained by movement, "close to zero" at 15 µm, and a cut-off for the line attractor score. For the first two I chose a cut-off (under 10% of variance; under a tenth of the on-soma response) and labelled it as a reading. Under the protocol a threshold that could change the outcome should not be an agent's choice, so a second reader should check these two.
- **Tests:** I ran Mann-Whitney unpaired even where the Methods say "paired". The reported p-values at n = 4 and n = 5 are the smallest the unpaired test can give, and a paired test cannot reach them.

**Inconsistencies in the paper**, recorded in the criteria:
- **Pulse parameters:** the Results say 20 Hz and the Methods say 10 Hz.
- **Model fit:** the observation cvR² is 67.2%, below the Methods' own 70% minimum. Its printed spreads (±0.03% and ±0.02%) only make sense as fractions.
- **Fig. 3i:** the text says "not statistically significant", but the legend lists P = 0.0316.
- **Extended Data Fig. 12b:** the legend gives r² = 0.87 for x2 neurons, which conflicts with the Results.
- **Mouse counts:** Extended Data Fig. 8j–l uses n = 8 and Extended Data Fig. 7b,c uses n = 10, against 7 and 9 elsewhere.

**Missing from the paper.** Nothing a claim needed for the reader step; the full text and Methods are there. Some claims need data the dataset may not hold: face-video motion SVDs (Extended Data Fig. 5), the spatial-resolution calibration cells (Extended Data Fig. 6), and cell positions. Whether they are in the dataset is for the author to find.

## End of run

25 turns, 7 minutes, result: success.
