# clark-2026 · author · run 45814018831

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; ls; ls docs entries claims paper; wc -l docs/*.md README.md
```

```
Thu Nov 26 11:58:37 UTC 2026
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
[... 701 more lines not kept]
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
3	Version: `pilot-18`. Record this version in the attempt's provenance.
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
[... 760 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/clark-2026.yaml"
}
```

```
1	# Claims for Clark, Abbott & Sompolinsky (2026), Nature Neuroscience, "Symmetries and continuous
2	# attractors in disordered neural circuits", doi:10.1038/s41593-026-02452-4, on dandiset 000939.
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-26,
4	# protocol pilot-18 as stated in docs/protocol.md (Reader, steps 1 to 4).
5	#
6	# Text read. The version of record (PDF supplied by a person, extracted to text): main text,
7	# figure legends, Methods, Data and Code availability and the Reporting Summary, and the
8	# Supplementary Information PDF (41593_2026_2452_MOESM1_ESM.pdf, Supplementary Notes 1 to 4 with
9	# Supplementary Figs. 1 to 16). No figure page was opened; no number below is read from a figure.
10	#
11	# Data the paper used, as it reports them. Recordings of Duszkiewicz et al. (Nat. Neurosci. 2024)
12	# from the postsubiculum of freely moving mice, DANDI 000939 (version cited 0.240528.1542). 31
13	# recording sessions, one per mouse, 2,691 units, of which 1,533 carry the dataset's
14	# head-direction label (significant head-direction information against a time-reversed control,
15	# a label set by the original authors and distributed with the dataset). Only the epoch of
16	# square-environment exploration is analysed (tag wake_square in the NWB epochs table). Nine mice
17	# also had an optogenetic epoch, recorded separately and never analysed; they contribute 315 of
18	# the 1,533 cells. Where a session has a file named +ogen.nwb, ring/data.py reads that file and
19	# takes the wake_square epoch from it. Measured variables used are the head direction
20	# (processing/behavior/CompassDirection/head-direction, with timestamps), the spike times of each
[... 710 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md | head -80; sed -n 1,120p docs/archives.md
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
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
ls -R entries/fouke-2025 | head -30; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in; ls papers/datasets/ | grep clark; cat papers/datasets/clark-2026.yaml; ls attempts | grep -E "clark|fouke"; ls questions | grep clark; ls papers/author-notes 2>/dev/null | grep clark
```

```
entries/fouke-2025:
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
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/fouke-2025-01.yaml | head -250
```

```
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
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
    protocol: pilot-5
  runner:
[... 230 more lines not kept]
```

**Agent calls Bash**

```bash
wc -c paper/*.txt; ls schemas; curl -s -o /dev/null -w "%{http_code}\n" https://api.dandiarchive.org/api/dandisets/000939/versions/; curl -s -o /dev/null -w "%{http_code}\n" https://github.com/davidclark1/symmetries-continuous-attractors; curl -s -o /dev/null -w "%{http_code}\n" https://zenodo.org/api/records/21827768
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000939/versions/ | python -m json.tool | grep -E '"version"|"status"|"modified"|"name"' ; curl -s "https://api.dandiarchive.org/api/dandisets/000939/versions/0.240528.1542/assets/?page_size=200" | python -c "
import json,sys; d=json.load(sys.stdin); print(d['count'])
for a in d['results']: print(a['path'], a['size'], a['asset_id'])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/davidclark1/symmetries-continuous-attractors repo && cd repo && git checkout -q 245726fa78457e10cdcf17e6be36fba1dec98061 && git log -1 --format=%H && ls -R | head -60 && wc -l ring/*.py; curl -s https://zenodo.org/api/records/21827768 | python -c "
import json,sys; d=json.load(sys.stdin); print(d.get('doi'), d['metadata'].get('title'), d['metadata'].get('version'))
for f in d['files']: print(f['key'], f['size'], f['links']['self'])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -sL https://zenodo.org/api/records/21827768/files/CHECKSUMS.md5/content; cd $TMPDIR/repo; cat data/README.md | head -60; cat README.md | head -80
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/repo; cat pyproject.toml; cat ring/data.py
```

```
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "ring"
version = "0.1.0"
description = "Code for the Symmetries and Continuous Attractors in Disordered Neural Circuits paper"
requires-python = ">=3.10"

[tool.setuptools.packages.find]
where = ["."]
include = ["ring*"]
"""Mouse head-direction tuning-curve producer.

Walks the Peyrache lab NWB sessions on disk, computes per-unit tuning
curves (with Poisson-likelihood-optimized Gaussian smoothing per
cross-validation fold), and writes
``tc_data.npz``, the tuning-curve file consumed by ``notebooks/data_and_generative_model.ipynb``
and the ``data_driven`` chain.
[... 361 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/repo; cat ring/analysis.py ring/fn.py ring/tc.py ring/seed.py
```

```
"""Tuning-curve statistics + model-vs-data comparison for the paper analysis.

Provides circular-statistics primitives (COM, centering, peak-finding),
per-mouse aggregate computations, scalar comparison metrics (peak counts,
peak values, flip symmetry, bits-per-spike), and a Kuiper-test-with-
FDR-correction pipeline. The top-level ``analyze_tuning_curves`` runs all
four comparison metrics on data vs model and returns a dict; the npz
serialization round-trip uses ``save_analysis_results`` /
``load_analysis_results``. Consumed by
``notebooks/data_and_generative_model.ipynb`` and ``ring/plot.py``.
"""
import numpy as np
from astropy.stats import kuiper
from scipy.stats import pearsonr
from statsmodels.stats.multitest import multipletests


# --- Core tuning-curve operations ------------------------------------------

def circular_center_of_mass(tuning_curves):
[... 624 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/repo; cat ring/gp_opt.py; cat ring/regression.py
```

```
"""Grid-search optimizer for the (scale, bias, beta) tuning-curve generative parameters.

Walks a (scale, bias, beta) grid, generates ``Phi_m`` samples from each parameter
triple, computes the resulting Fourier-space covariance, and compares to a
target ``Gamma_phi_data_ft`` (typically derived from real mouse data in
``notebooks/data_and_generative_model.ipynb``).

Run as a script to (re)produce ``grid_search_results.npz``::

    python -m ring.gp_opt

Public surface used by notebooks: ``gen_Phi_m`` and ``compute_cov_from_params``
(see e.g. ``data_and_generative_model.ipynb``); the other functions support the
script flow.
"""
from pathlib import Path

import numpy as np
import torch

[... 365 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev 2>&1 | tail -2; source dev/bin/activate && uv pip install -q pynwb remfile h5py numpy scipy astropy statsmodels pandas matplotlib dandi jupyter nbconvert ipykernel 2>&1 | tail -3; python -c "import pynwb, remfile, astropy; print(pynwb.__version__)"; nproc; free -g
```

```
4.2.0
4
               total        used        free      shared  buff/cache   available
Mem:              15           1          10           0           4          14
Swap:              0           0           0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && cat > survey.py <<'EOF'
import h5py, remfile, requests, time, numpy as np
VER="0.240528.1542"
def url(aid):
    r=requests.get(f"https://api.dandiarchive.org/api/dandisets/000939/versions/{VER}/assets/{aid}/")
    return [u for u in r.json()['contentUrl'] if 's3' in u][0]
t=time.time()
f=h5py.File(remfile.File(url("4aa9c44e-922c-4397-9d58-e5ad96d9f48c")),'r')
def show(name,obj):
    if isinstance(obj,h5py.Dataset): print(name,obj.shape,obj.dtype, dict((k,str(v)[:60]) for k,v in obj.attrs.items() if k in('unit','conversion','rate','description')))
    else: print(name+'/')
f.visititems(show)
print(time.time()-t)
EOF
python survey.py 2>&1 | grep -v "^acquisition/.*/" | head -120
```

```
acquisition/
analysis/
file_create_date (1,) object {}
general/
general/devices/
general/devices/Cambridge Neurotech H5 probe/
general/experiment_description () object {}
general/experimenter (1,) object {}
general/extracellular_ephys/
general/extracellular_ephys/electrodes/
general/extracellular_ephys/electrodes/filtering (64,) object {'description': 'description of hardware filtering, including the filter name'}
general/extracellular_ephys/electrodes/group (64,) object {'description': 'a reference to the ElectrodeGroup this electrode is a part o'}
general/extracellular_ephys/electrodes/group_name (64,) object {'description': 'the name of the ElectrodeGroup this electrode is a part of'}
general/extracellular_ephys/electrodes/id (64,) int64 {}
general/extracellular_ephys/electrodes/is_faulty (64,) bool {'description': 'Boolean column to indicate faulty electrodes'}
general/extracellular_ephys/electrodes/label (64,) object {'description': 'label of electrode'}
general/extracellular_ephys/electrodes/location (64,) object {'description': 'the location of channel within the subject e.g. brain region'}
general/extracellular_ephys/electrodes/x (64,) float64 {'description': 'the x coordinate of the position (+x is posterior)'}
general/extracellular_ephys/electrodes/y (64,) float64 {'description': 'the y coordinate of the position (+y is inferior)'}
general/extracellular_ephys/electrodes/z (64,) float64 {'description': 'the z coordinate of the position (+z is right)'}
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && cat > t2.py <<'EOF'
import h5py, remfile, requests, time, numpy as np
VER="0.240528.1542"
def url(aid):
    r=requests.get(f"https://api.dandiarchive.org/api/dandisets/000939/versions/{VER}/assets/{aid}/")
    return [u for u in r.json()['contentUrl'] if 's3' in u][0]
for aid in ["4aa9c44e-922c-4397-9d58-e5ad96d9f48c","03683ad0-e0c4-4281-8328-8882df292728"]:
    t=time.time()
    f=h5py.File(remfile.File(url(aid)),'r')
    print(list(f['acquisition'].keys()), list(f['intervals'].keys()), list(f['stimulus/presentation'].keys()))
    e=f['intervals/epochs']; print(e['start_time'][:], e['stop_time'][:], e['tags'][:], e['tags_index'][:])
    hdt=f['processing/behavior/CompassDirection/head-direction/timestamps'][:]
    hd=f['processing/behavior/CompassDirection/head-direction/data'][:]
    print('hd', hdt[:3], hdt[-1], np.nanmin(hd), np.nanmax(hd), np.isnan(hd).mean(), np.median(np.diff(hdt)))
    idx=f['units/spike_times_index'][:]; ishd=f['units/is_head_direction'][:]
    print(len(idx), ishd.sum(), f['units/is_excitatory'][:].sum(), (ishd&f['units/is_excitatory'][:]).sum(), time.time()-t)
    st=f['units/spike_times']
    t=time.time(); starts=np.r_[0,idx[:-1]]
    x=[st[starts[i]:idx[i]] for i in np.where(ishd)[0][:20]]
    print('20 units', sum(len(a) for a in x), time.time()-t)
    print(f['general/session_id'][()], f['general/subject/subject_id'][()], f['session_description'][()][:200])
EOF
python t2.py
```

```
[] ['epochs', 'nrem', 'rem'] []
[5.00000e-05 3.30210e+03 5.10984e+03 9.90288e+03] [ 3302.1   5109.84  9902.88 11142.43] [b'home_cage' b'wake_square' b'home_cage' b'wake_triangle'] [1 2 3 4]
hd [3304.24 3304.25 3304.26] 11139.55 2.424262331020124e-05 6.283168935991203 0.0008822319150687186 0.010000000000218279
185 117 125 117 2.0847437381744385
20 units 357915 0.42298412322998047
b'200317' b'A3707' b'Open field and sleep recording'
[] ['epochs', 'nrem', 'rem'] []
[5.000000e-05 2.762496e+03 3.970260e+03 6.393132e+03] [2762.496 3970.26  6393.132 9105.48 ] [b'home_cage' b'wake_square' b'home_cage' b'wake_opto'] [1 2 3 4]
hd [2765.746 2765.756 2765.766] 9102.392 0.0 6.283180385351096 0.0033574565219616553 0.010000000000218279
70 39 40 39 2.2776596546173096
20 units 319141 0.5309491157531738
b'190827' b'A1824' b'Open field and sleep recording'
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/repo/notebooks && ls && python - <<'EOF'
import json
nb=json.load(open('data_and_generative_model.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='code':
        print(f'--- [{i}]'); print(''.join(c['source']))
        for o in c.get('outputs',[]):
            if 'text' in o: print('OUT:', ''.join(o['text'])[:600])
EOF
```

```
<persisted-output>
Output too large (42.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/c72abc4e-3061-4e0b-9fc5-690e0e537888/tool-results/bnhnghs7u.txt

Preview (first 2KB):
closing_the_loop.ipynb
data_and_generative_model.ipynb
data_driven_attractor.ipynb
data_driven_reconstruction.ipynb
dmft.ipynb
grid_sims.ipynb
mexican_hat_and_asymmetry.ipynb
reservoir_rnn.ipynb
spectra.ipynb
spurious_fixed_points.ipynb
weight_matrix_analyses.ipynb
--- [1]
# Regeneration switches (default off so a normal run cannot overwrite committed figures/caches):
SAVE_FIGURES = False
REGENERATE_CACHES = False

[... 72 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/c72abc4e-3061-4e0b-9fc5-690e0e537888/tool-results/bnhnghs7u.txt"
}
```

```
1	closing_the_loop.ipynb
2	data_and_generative_model.ipynb
3	data_driven_attractor.ipynb
4	data_driven_reconstruction.ipynb
5	dmft.ipynb
6	grid_sims.ipynb
7	mexican_hat_and_asymmetry.ipynb
8	reservoir_rnn.ipynb
9	spectra.ipynb
10	spurious_fixed_points.ipynb
11	weight_matrix_analyses.ipynb
12	--- [1]
13	# Regeneration switches (default off so a normal run cannot overwrite committed figures/caches):
14	SAVE_FIGURES = False
15	REGENERATE_CACHES = False
16	
17	# Standard library
18	
19	# Third-party libraries
20	import numpy as np
[... 1042 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && uv pip install -q fsspec aiohttp && cat > z.py <<'EOF'
import fsspec, tarfile, time, numpy as np, io
t=time.time()
u="https://zenodo.org/api/records/21827768/files/symmetries_caches_v1.tar/content"
f=fsspec.open(u, block_size=2**20).open()
tf=tarfile.open(fileobj=f, mode='r:')
for m in tf.getmembers(): print(m.name, m.size, m.offset_data)
print(time.time()-t)
EOF
python z.py
```

```
. 0 512
./mouse_data 0 1024
./mouse_data/tc_data.npz 8755282 1536
./analysis_results.npz 2584049 8757760
./jacobian_results.npz 129518 11342336
./gridness_hist_digitized.npz 2100 11472384
./simulation_results_updated_again.npz 6133222 11475456
./dmft_simulation_results.npz 72145262 17609216
./ring_attractor_noise_results.npz 145021203 89755136
./spectra_results_updated_again.npz 123912 234777088
./grid_search_results.npz 146574 234902016
./experimental_gridness_scores.npy 4936 235049472
./spectra_cache.npz 200122176 235055104
./pc_convergence_grid.npz 70567320 435177984
./actual_hd_timeseries_2.npz 1442934 505745920
./grid_analysis_results.npz 5106228 507189760
./integration_sim_results_updated_again.npz 1443062357 512296960
./distances_updated_again.npz 1600272 1955360256
./pcs_updated_again.npz 7440508 1956961280
./gamma_phi_info.npz 1756 1964402688
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/repo; python - <<'EOF'
import re
src=open('ring/plot.py').read()
for name in ['plot_covariance_grid','plot_mean_std_profiles','plot_mouse_coms']:
    i=src.find('def '+name); j=src.find('\ndef ',i+5); print(src[i:j])
EOF
```

```
def plot_covariance_grid(axes, mouse_nums, mouse_nums_to_plot, mouse_names,
                         Phi_m_data, subsample_sizes):
    """Grid of per-mouse subsampled covariance matrices, demonstrating convergence.

    Rows = mice in ``mouse_nums_to_plot``; columns = subsample sizes in
    ``subsample_sizes``. Each cell shows the empirical covariance of a
    random N_sub subset of that mouse's tuning curves.

    Parameters
    ----------
    axes : ndarray of matplotlib axes, shape (N_mice_to_plot, N_subsample_sizes)
    mouse_nums : ndarray
    mouse_nums_to_plot : sequence of int
    mouse_names : ndarray
    Phi_m_data : ndarray, shape (N_curves, N_theta)
    subsample_sizes : sequence of int

    Returns
    -------
    im : matplotlib image handle (last drawn)
[... 121 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p entries/clark-2026 && date -u
```

```
Thu Nov 26 12:02:16 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "entries/clark-2026/hdring.py",
 "content": "\"\"\"Loading and measures for the attempt on Clark, Abbott & Sompolinsky (2026) on DANDI:000939.\n\nEvery procedure here follows the paper's code, github.com/davidclark1/symmetries-continuous-attractors\nat commit 245726fa78457e10cdcf17e6be36fba1dec98061 (the \"ring\" package), as the claims file\n(claims/clark-2026.yaml) cites it. Each function names the function of the paper's code it\nrepeats. The paper's code imports torch; the parts used here are rewritten in numpy so that the\nentry needs no GPU stack. Where a parameter comes from somewhere else it is said so.\n\nData are streamed from the DANDI archive (remfile and h5py); nothing is downloaded to disk.\n\"\"\"\nimport hashlib\nimport io\nimport zlib\n\nimport h5py\nimport numpy as np\nimport remfile\nimport requests\nfrom scipy.ndimage import gaussian_filter1d\n\nDANDISET = \"000939\"\n# The version the paper cites (claims file, opening comment).\nVERSION = \"0.240528.1542\"\nAPI = \"https://api.dandiarchive.org/api\"\nPAPER_KEY = \"clark-2026\"\n\n# Paper's code, ring/data.py: DATA_DT, process_file defaults.\nDATA_DT = 0.01\nN_THETA = 100\nSIGMA_VALS = np.logspace(-1, 2, 100)\nK_FOLDS = 4\n\n# Zenodo record of the paper's cached results (claims file, tuning-curves-match-cache).\nZENODO_TAR = \"https://zenodo.org/api/records/21827768/files/symmetries_caches_v1.tar/content\"\nZENODO_MD5 = \"https://zenodo.org/api/records/21827768/files/CHECKSUMS.md5/content\"\n\n\ndef seed(claim_id, k=0):\n    \"\"\"Seed of a claim's k-th generator (protocol, \"Take every random seed from the claim\").\"\"\"\n    return zlib.crc32(f\"{PAPER_KEY}/{claim_id}\".encode()) + k\n\n\ndef list_assets(version=VERSION):\n    \"\"\"All assets of the dandiset at the pinned version, as dicts (path, size, asset_id).\"\"\"\n    url = f\"{API}/dandisets/{DANDISET}/versions/{version}/assets/?page_size=200\"\n    out = []\n    while url:\n        r = requests.get(url, timeout=60)\n        r.raise_for_status()\n        d = r.json()\n        out += d[\"results\"]\n        url = d[\"next\"]\n    return out\n\n\ndef asset_s3_url(asset_id, version=VERSION):\n    r = requests.get(f\"{API}/dandisets/{DANDISET}/versions/{version}/assets/{asset_id}/\", timeout=60)\n    r.raise_for_status()\n    return [u for u in r.json()[\"contentUrl\"] if \"amazonaws\" in u][0]\n\n\ndef session_order(assets):\n    \"\"\"Sessions in the order of the paper's code (ring/data.py, get_session_info).\n\n    The code takes one file per subject folder, the +ogen.nwb file where one exists, and\n    sorts by the full path, which sorts by subject. Session index = position in this list.\n    \"\"\"\n    by_subj = {}\n    for a in assets:\n        if not a[\"path\"].endswith(\".nwb\"):\n            continue\n        subj = a[\"path\"].split(\"/\")[0].split(\"-\")[-1]\n        ogen = a[\"path\"].endswith(\"+ogen.nwb\")\n        if subj not in by_subj or ogen:\n            by_subj[subj] = (a[\"path\"], a[\"asset_id\"], ogen)\n    return [(p, aid, subj, ogen) for subj, (p, aid, ogen) in sorted(by_subj.items(), key=lambda kv: kv[1][0])]\n\n\ndef _strs(x):\n    return [v.decode() if isinstance(v, bytes) else str(v) for v in x]\n\n\ndef load_session(asset_id, hd_only=True, version=VERSION):\n    \"\"\"Read what the analysis needs from one NWB file, by streaming.\n\n    Returns a dict with the epochs table, the head-direction series (data, timestamps), the\n    unit labels (is_head_direction, is_excitatory, is_fast_spiking), the unit count, and the\n    spike times of the head-direction units only (hd_only) or of all units.\n    \"\"\"\n    f = h5py.File(remfile.File(asset_s3_url(asset_id, version)), \"r\")\n    ep = f[\"intervals/epochs\"]\n    tags_idx = ep[\"tags_index\"][:]\n    tags = _strs(ep[\"tags\"][:])\n    starts = np.r_[0, tags_idx[:-1]]\n    ep_tags = [\",\".join(tags[s:e]) for s, e in zip(starts, tags_idx)]\n    hd_ss = f[\"processing/behavior/CompassDirection/head-direction\"]\n    out = dict(\n        epochs=list(zip(ep_tags, ep[\"start_time\"][:], ep[\"stop_time\"][:])),\n        hd=hd_ss[\"data\"][:],\n        hd_t=hd_ss[\"timestamps\"][:],\n        hd_unit=hd_ss[\"data\"].attrs.get(\"unit\"),\n        is_hd=f[\"units/is_head_direction\"][:].astype(bool),\n        is_exc=f[\"units/is_excitatory\"][:].astype(bool),\n        is_fs=f[\"units/is_fast_spiking\"][:].astype(bool),\n        subject=f[\"general/subject/subject_id\"][()].decode(),\n        session_id=f[\"general/session_id\"][()].decode(),\n    )\n    idx = f[\"units/spike_times_index\"][:]\n    out[\"n_units\"] = len(idx)\n    out[\"unit_ids\"] = f[\"units/id\"][:]\n    st = f[\"units/spike_times\"]\n    first = np.r_[0, idx[:-1]]\n    keep = np.where(out[\"is_hd\"])[0] if hd_only else np.arange(len(idx))\n    out[\"spike_units\"] = keep\n    out[\"spikes\"] = [st[first[i]:idx[i]] for i in keep]\n    f.close()\n    return out\n\n\ndef epoch_bins(sess, tag=\"wake_square\", N_theta=N_THETA):\n    \"\"\"Head-direction bin index per 10-ms sample in the epoch (ring/data.py, process_file).\n\n    The epoch runs from the head-direction sample nearest the epoch start to the one nearest\n    its stop; NaN samples get index -1 (dropped); bins are floor(hd / (2 pi / N_theta)).\n    \"\"\"\n    ti_nom, tf_nom = [(s, e) for t, s, e in sess[\"epochs\"] if t == tag][0]\n    t_full = sess[\"hd_t\"]\n    ti_idx = np.argmin((ti_nom - t_full) ** 2)\n    tf_idx = np.argmin((tf_nom - t_full) ** 2)\n    ti, tf = t_full[ti_idx], t_full[tf_idx]\n    hd = sess[\"hd\"][ti_idx:tf_idx].copy()\n    hd[np.isnan(hd)] = -1\n    hd_idx = np.floor(hd / (2 * np.pi / N_theta)).astype(int)\n    return hd_idx, ti, tf, ti_idx, tf_idx\n\n\ndef alternating_mask(N_bins, K=K_FOLDS):\n    \"\"\"ring/data.py, generate_alternating_mask: 2K contiguous chunks, alternating True/False.\"\"\"\n    chunk, rem = divmod(N_bins, 2 * K)\n    mask = np.zeros(N_bins, dtype=bool)\n    val, s = True, 0\n    for _ in range(2 * K):\n        n = chunk + (1 if rem > 0 else 0)\n        rem -= 1\n        mask[s:s + n] = val\n        s += n\n        val = not val\n    return mask\n\n\ndef spike_counts(spike_times, ti, tf, N_bins):\n    \"\"\"10-ms spike counts from the epoch start (ring/data.py, process_file).\"\"\"\n    s = spike_times[(spike_times >= ti) & (spike_times < tf)]\n    idx = np.floor((s - ti) / DATA_DT).astype(int)\n    idx = idx[(idx >= 0) & (idx < N_bins)]\n    return np.bincount(idx, minlength=N_bins).astype(float)\n\n\ndef tuning_curves_session(sess, N_theta=N_THETA, sigma_vals=SIGMA_VALS, K=K_FOLDS):\n    \"\"\"Cross-validated tuning curves of the loaded units (ring/data.py, process_file).\n\n    For each partition (the alternating mask and its complement): the occupancy-normalized\n    curve, with zero bins set to 1e-3 times its mean (compute_tuning_curve); smoothed with a\n    circular Gaussian of each width in sigma_vals; the width kept is the one maximizing the\n    Poisson log-likelihood of the other partition's 10-ms counts. The log-likelihood is\n    computed from per-angle sums of counts and occupancy, sum_a [S_a log(mu_a) - n_a mu_a],\n    which differs from the code's sum of poisson.logpmf only by a term that does not depend\n    on the curve (sum of log k!), so the chosen width is the same.\n\n    Returns plain (n, 2, N_theta), opt (n, 2, N_theta), opt_sigma (n, 2), and the bin data.\n    \"\"\"\n    hd_idx, ti, tf, _, _ = epoch_bins(sess, N_theta=N_theta)\n    N_bins = len(hd_idx)\n    m = alternating_mask(N_bins, K)\n    valid = hd_idx >= 0\n    folds = [m & valid, (~m) & valid]\n    occ = [np.bincount(hd_idx[fm], minlength=N_theta).astype(float) for fm in folds]\n    n = len(sess[\"spikes\"])\n    plain = np.zeros((n, 2, N_theta))\n    opt = np.zeros((n, 2, N_theta))\n    opt_sig = np.zeros((n, 2))\n    # the smoothing operators, one per width, as matrices acting on a curve (mode wrap)\n    eye = np.eye(N_theta)\n    S = np.stack([gaussian_filter1d(eye, s, axis=0, mode=\"wrap\") for s in sigma_vals])\n    for u, st in enumerate(sess[\"spikes\"]):\n        counts = spike_counts(st, ti, tf, N_bins)\n        sc = [np.bincount(hd_idx[fm], weights=counts[fm], minlength=N_theta) for fm in folds]\n        for k in range(2):\n            with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n                tc = sc[k] / (occ[k] * DATA_DT)\n            tc[tc == 0.0] = tc.mean() * 1e-3\n            plain[u, k] = tc\n            sm = np.einsum(\"sij,j->si\", S, tc)  # (n_sigma, N_theta)\n            mu = sm * DATA_DT\n            other = 1 - k\n            with np.errstate(divide=\"ignore\"):\n                ll = (sc[other][None, :] * np.log(mu)).sum(1) - (occ[other][None, :] * mu).sum(1)\n            j = int(np.nanargmax(ll))\n            opt[u, k] = sm[j]\n            opt_sig[u, k] = sigma_vals[j]\n    return plain, opt, opt_sig\n\n\ndef read_zenodo_member(name):\n    \"\"\"Read one member of the Zenodo cache tar by range requests, and check its MD5.\n\n    Returns (bytes, md5 computed, md5 listed in the record's CHECKSUMS.md5).\n    \"\"\"\n    import fsspec\n    import tarfile\n\n    listed = {}\n    for line in requests.get(ZENODO_MD5, timeout=60).text.splitlines():\n        if line.strip():\n            h, p = line.split()\n            listed[p] = h\n    with fsspec.open(ZENODO_TAR, block_size=2**20).open() as fh:\n        tf = tarfile.open(fileobj=fh, mode=\"r:\")\n        for mem in tf:\n            if mem.name.lstrip(\"./\") == name:\n                fh.seek(mem.offset_data)\n                b = fh.read(mem.size)\n                break\n            if mem.offset_data > 3e9:\n                raise KeyError(name)\n    return b, hashlib.md5(b).hexdigest(), listed.get(name)\n\n\ndef load_npz_bytes(b):\n    return np.load(io.BytesIO(b), allow_pickle=False)\n\n\n# ---------------------------------------------------------------- tuning-curve statistics\n# ring/analysis.py\n\n\ndef circular_center_of_mass(tcs):\n    \"\"\"ring/analysis.py, circular_center_of_mass; Methods equation (14).\"\"\"\n    theta = np.linspace(0, 2 * np.pi, tcs.shape[1], endpoint=False)\n    return np.arctan2((tcs * np.sin(theta)).sum(1), (tcs * np.cos(theta)).sum(1)) % (2 * np.pi)\n\n\ndef center_tuning_curves(tcs):\n    \"\"\"ring/analysis.py, center_tuning_curves: roll so the center of mass falls on bin 0.\"\"\"\n    n = tcs.shape[1]\n    shifts = (-(n * circular_center_of_mass(tcs) / (2 * np.pi)).round()).astype(int)\n    return np.stack([np.roll(t, s) for t, s in zip(tcs, shifts)])\n\n\ndef find_local_maxima(signal, z_thresh):\n    \"\"\"ring/analysis.py, find_local_maxima; Methods equation (17). Circular.\"\"\"\n    diff = np.concatenate(([signal[0] - signal[-1]], np.diff(signal)))\n    sign_change = np.sign(np.roll(diff, -1)) - np.sign(diff)\n    maxima = np.where(sign_change == -2)[0]\n    return maxima[(signal[maxima] - signal.mean()) / signal.std() > z_thresh]\n\n\ndef peak_counts(tcs, z_thresh):\n    return np.array([len(find_local_maxima(t, z_thresh)) for t in tcs])\n\n\ndef peak_count_hist(tcs, z_thresh, max_peaks=6):\n    \"\"\"ring/analysis.py, compute_peak_counts: histogram of 1 to 5 peaks, normalized over those.\"\"\"\n    pc = peak_counts(tcs, z_thresh)\n    c = np.array([(pc == i).sum() for i in range(1, max_peaks)], float)\n    return c / c.sum()\n\n\ndef get_peak_values(tcs, num_peaks=3):\n    \"\"\"ring/analysis.py, get_peak_values (zthresh 1).\"\"\"\n    res = np.full((len(tcs), num_peaks), np.nan)\n    for i, t in enumerate(tcs):\n        v = np.sort(t[find_local_maxima(t, 1)])[::-1][:num_peaks]\n        res[i, :len(v)] = v\n    return res\n\n\ndef symmetry_scores(tcs):\n    \"\"\"ring/analysis.py, compute_symmetry_scores; Methods equation (15).\"\"\"\n    out = []\n    for x in tcs:\n        theta = np.arange(len(x)) * 2 * np.pi / len(x)\n        ang = np.mod(np.arctan2(np.average(np.sin(theta), weights=x), np.average(np.cos(theta), weights=x)), 2 * np.pi)\n        com = int(np.round(ang * len(x) / (2 * np.pi)))\n        rev = np.roll(x, -2 * com - 1)[::-1]\n        out.append(np.corrcoef(x, rev)[0, 1])\n    return np.array(out)\n\n\ndef bits_per_spike(tcs):\n    \"\"\"ring/analysis.py, compute_bits_per_spike; Methods equation (16).\"\"\"\n    return (tcs * np.log2(tcs)).mean(1)\n\n\ndef calc_C(X):\n    \"\"\"ring/fn.py, calc_C: mean over rows of |rfft(norm forward)|^2, and its inverse transform.\"\"\"\n    C_ft = np.mean(np.abs(np.fft.rfft(X, axis=1, norm=\"forward\")) ** 2, axis=0)\n    return np.fft.irfft(C_ft, norm=\"forward\"), C_ft\n\n\ndef softplus(x, beta=1.0):\n    \"\"\"ring/fn.py, softplus, numerically stable.\"\"\"\n    return np.where(x >= 0, x + np.log1p(np.exp(-beta * np.abs(x))) / beta,\n                    np.log1p(np.exp(-beta * np.abs(x))) / beta)\n\n\ndef inv_softplus(y, beta=1.0):\n    return np.log(np.expm1(beta * y)) / beta\n\n\ndef wrapped_gaussian_ft(scale, N_theta=N_THETA, eq_var=1.0):\n    \"\"\"ring/tc.py, wrapped_gaussian_cov (Fourier side).\"\"\"\n    n = np.arange(N_theta // 2 + 1)\n    return (eq_var / np.sqrt(2 * np.pi) / scale) * np.exp(-n ** 2 / (2 * scale ** 2))\n\n\ndef sample_z(rng, N_samples, N_freq, dtype=np.float64):\n    \"\"\"ring/gp_opt.py, sample_z (numpy branch), from a seeded Generator.\"\"\"\n    z = (rng.standard_normal((N_samples, N_freq), dtype=dtype)\n         + 1j * rng.standard_normal((N_samples, N_freq), dtype=dtype)) / np.sqrt(2)\n    z[:, 0] = z[:, 0].real * np.sqrt(2)\n    return z\n\n\ndef gen_Phi_m(scale, bias, beta, N_samples, rng, N_theta=N_THETA, normalize=True, z=None):\n    \"\"\"ring/gp_opt.py, gen_Phi_m: wrapped-Gaussian process through softplus(x - b, beta).\"\"\"\n    if z is None:\n        z = sample_z(rng, N_samples, N_theta // 2 + 1)\n    X = np.fft.irfft(z * np.sqrt(wrapped_gaussian_ft(scale, N_theta))[None, :], axis=1, norm=\"forward\")\n    Phi = softplus(X - bias, beta)\n    if normalize:\n        Phi = Phi / (Phi.mean(1, keepdims=True) + 1e-30)\n    return Phi\n"
}
```

```
File created successfully at: entries/clark-2026/hdring.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && cat > t3.py <<'EOF'
import sys, time, resource; sys.path.insert(0,'entries/clark-2026')
import hdring as H, numpy as np
assets=H.list_assets(); order=H.session_order(assets)
print(len(assets), len(order)); print([o[2] for o in order])
b,m1,m2=H.read_zenodo_member('mouse_data/tc_data.npz'); print(m1,m2)
z=H.load_npz_bytes(b); print(list(z.keys())); 
for k in z.keys(): print(k, z[k].shape, z[k].dtype, z[k][:3] if z[k].ndim==1 else '')
np.savez('/tmp/claude/cache_tc.npz', **{k:z[k] for k in z.keys()}) if False else None
t=time.time(); i=[o[2] for o in order].index('A3707')
s=H.load_session(order[i][1]); print('load',time.time()-t)
t=time.time(); plain,opt,sig=H.tuning_curves_session(s); print('tc',time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
mn=z['mouse_nums']; hdm=z['hd_mask']
c_opt=z['opt_tcs'][(mn==i)&hdm]; c_sig=z['opt_sigmas'][(mn==i)&hdm]
print(c_opt.shape, opt.shape)
r=[np.corrcoef(a.mean(0),b.mean(0))[0,1] for a,b in zip(opt,c_opt)]
print(np.min(r), np.median(r), (sig==c_sig).mean(), np.abs(opt-c_opt).max())
EOF
python t3.py
```

```
31 31
['A1808', 'A1813', 'A1815', 'A1821', 'A1824', 'A3701', 'A3702', 'A3703', 'A3705', 'A3706', 'A3707', 'A3708', 'A3709', 'A3710', 'A3711', 'A3712', 'A3713', 'A3716', 'A3717', 'A3723', 'A3728', 'A3730', 'A5505', 'A5506', 'A5507', 'A5508', 'A5801', 'A6211', 'A6215', 'A6216', 'A9701']
6e1f3a17ab67e2e0eb8fac35d89e2d57 6e1f3a17ab67e2e0eb8fac35d89e2d57
['hd_mask', 'exc_mask', 'fs_mask', 'plain_tcs', 'opt_tcs', 'opt_sigmas', 'fnames', 'unit_counts', 'mouse_nums', 'mouse_names', 'has_ogen']
hd_mask (2691,) bool [False False  True]
exc_mask (2691,) bool [False False  True]
fs_mask (2691,) bool [False False False]
plain_tcs (2691, 2, 100) float64 
opt_tcs (2691, 2, 100) float64 
opt_sigmas (2691, 2) float64 
fnames (31,) <U96 ['/media/davidclark/DATA/PeyracheData/updated/000939/sub-A1808/sub-A1808_behavior+ecephys+ogen.nwb'
 '/media/davidclark/DATA/PeyracheData/updated/000939/sub-A1813/sub-A1813_behavior+ecephys+ogen.nwb'
 '/media/davidclark/DATA/PeyracheData/updated/000939/sub-A1815/sub-A1815_behavior+ecephys+ogen.nwb']
unit_counts (31,) int64 [101  70  65]
mouse_nums (2691,) int64 [0 0 0]
mouse_names (2691,) <U5 ['A1808' 'A1808' 'A1808']
has_ogen (2691,) bool [ True  True  True]
load 5.966079473495483
tc 0.22675204277038574 0.198568
(117, 2, 100) (117, 2, 100)
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/repo; cat ring/data_driven.py
```

```
"""Data-driven ring-attractor toolkit.

Builds the empirical weight matrix ``J`` from mouse tuning curves, runs
the resulting recurrent network with closed-loop head-direction drive,
projects trajectories into PC space, and plots them. Consumed primarily
by ``notebooks/data_driven_attractor.ipynb`` (Fig 3 producer) and the
``data_driven_analyses`` / ``grid_sims`` chains.
"""
from pathlib import Path

import numpy as np
import torch
from scipy.ndimage import gaussian_filter1d
from tqdm import tqdm

from . import sim
from . import fn
from . import regression
from . import analysis
from . import style  # noqa: F401  (imported for the matplotlib rcParams side effect)
[... 651 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/repo; cat ring/sim.py; python - <<'EOF'
import json
nb=json.load(open('notebooks/data_driven_attractor.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='code':
        s=''.join(c['source'])
        print(f'--- [{i}]'); print(s[:3500])
        for o in c.get('outputs',[]):
            if 'text' in o: print('OUT:', ''.join(o['text'])[-400:])
EOF
```

```
"""ODE simulation of the ring-attractor dynamical system.

``run_sim`` performs Euler integration of

    tau * dx/dt = -x + J @ phi(x) + omega(t) * J' @ phi(x) + stabilizer

on GPU/CPU torch tensors, with optional periodic save of state and an
early-stop check that fires when per-batch derivatives plateau.
"""
import numpy as np
import torch
from . import fn


def run_sim(T, tau, dt, T_eval, J, x_init,
            nonlin=fn.unity_erf,
            omega_func=None, J_prime=None,
            target_mean=None, const=np.nan,
            return_derivs=False,
            break_if_stopped=True,
[... 630 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/repo; python - <<'EOF'
import json
for nbn in ['data_driven_reconstruction','spurious_fixed_points']:
    nb=json.load(open(f'notebooks/{nbn}.ipynb'))
    print('=========',nbn)
    for i,c in enumerate(nb['cells']):
        if c['cell_type']=='code':
            s=''.join(c['source'])
            if 'plot' in s[:200].lower() and 'def run' not in s and 'run_' not in s: 
                print(f'--- [{i}] (plot cell, {len(s)} chars) first line:', s.splitlines()[0][:100]); continue
            print(f'--- [{i}]'); print(s[:3000])
            for o in c.get('outputs',[]):
                if 'text' in o: print('OUT:', ''.join(o['text'])[-300:])
EOF
```

```
========= data_driven_reconstruction
--- [1] (plot cell, 318 chars) first line: # Regeneration switches (default off so a normal run cannot overwrite committed figures/caches):
--- [3]

# Load data
Phi_raw = data_driven.load_data_Phi()

# Compute weights

# Compute 'old' weights
X, Phi = data_driven.prepare_smoothed_normalized_resampled_tuning_curves(Phi_raw, N_theta=10000)
J, J_prime = data_driven.compute_weights(X, Phi, lamda=1e-8)


print("err =", np.mean((X - Phi @ J.T)**2))

OUT: err = 1.7152363818838536e-08

--- [5]
w = np.linalg.eigvals(J)
[... 378 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && cat > t4.py <<'EOF'
import sys, time, resource; sys.path.insert(0,'entries/clark-2026')
import hdring as H, numpy as np
assets=H.list_assets(); order=H.session_order(assets)
t=time.time(); res={}
rows=[]
for i,(p,aid,subj,ogen) in enumerate(order):
    s=H.load_session(aid)
    plain,opt,sig=H.tuning_curves_session(s)
    hd_idx,ti,tf,_,_=H.epoch_bins(s)
    rows.append((subj, s['n_units'], s['is_hd'].sum(), (s['is_hd']&s['is_exc']).sum(), [e[0] for e in s['epochs']], tf-ti, (hd_idx<0).mean()))
    res[subj]=(plain,opt,sig)
    print(i, rows[-1], round(time.time()-t), flush=True)
np.savez('tcs_dev.npz', **{k+'_opt':v[1] for k,v in res.items()}, **{k+'_sig':v[2] for k,v in res.items()})
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
EOF
python t4.py
```

```
0 ('A1808', 101, np.int64(29), np.int64(29), ['home_cage', 'wake_square', 'home_cage', 'wake_opto'], np.float64(906.52), np.float64(0.00138993072408772)) 3
1 ('A1813', 70, np.int64(30), np.int64(30), ['home_cage', 'wake_square', 'home_cage', 'wake_opto'], np.float64(1036.0900000000001), np.float64(0.0057234410138115414)) 7
2 ('A1815', 65, np.int64(33), np.int64(33), ['home_cage', 'wake_square', 'home_cage', 'wake_opto'], np.float64(901.5900000000001), np.float64(0.016359986246520037)) 11
3 ('A1821', 74, np.int64(37), np.int64(37), ['home_cage', 'wake_square', 'home_cage', 'wake_opto'], np.float64(2701.5399999999995), np.float64(0.009794413556712098)) 15
4 ('A1824', 70, np.int64(39), np.int64(39), ['home_cage', 'wake_square', 'home_cage', 'wake_opto'], np.float64(1201.08), np.float64(0.004329436840177174)) 18
5 ('A3701', 102, np.int64(71), np.int64(71), ['home_cage', 'wake_square', 'home_cage', 'wake_triangle'], np.float64(2534.2199999999993), np.float64(0.004877240334304046)) 22
6 ('A3702', 90, np.int64(61), np.int64(61), ['home_cage', 'wake_square', 'home_cage', 'wake_triangle'], np.float64(2545.8100000000004), np.float64(0.00206614004972877)) 27
7 ('A3703', 103, np.int64(65), np.int64(65), ['home_cage', 'wake_square', 'home_cage', 'wake_triangle'], np.float64(2411.6799999999994), np.float64(0.001982020831951171)) 31
8 ('A3705', 117, np.int64(66), np.int64(66), ['home_cage', 'wake_square', 'home_cage', 'wake_triangle'], np.float64(2631.4699999999993), np.float64(0.002173689990765618)) 38
9 ('A3706', 126, np.int64(86), np.int64(86), ['home_cage', 'wake_square', 'home_cage', 'wake_triangle'], np.float64(2401.8399999999997), np.float64(0.002006794790660494)) 42
10 ('A3707', 185, np.int64(117), np.int64(117), ['home_cage', 'wake_square', 'home_cage', 'wake_triangle'], np.float64(1803.04), np.float64(0.001253438636968675)) 48
11 ('A3708', 78, np.int64(44), np.int64(44), ['home_cage', 'wake_square', 'home_cage', 'wake_triangle'], np.float64(1900.039999999999), np.float64
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && cat > t5.py <<'EOF'
import sys, time; sys.path.insert(0,'entries/clark-2026')
import hdring as H, numpy as np
rng=np.random.default_rng(1)
for N in [50000]:
    z=H.sample_z(rng,N,51,dtype=np.float32).astype(np.complex64)
    t=time.time()
    X=np.fft.irfft(z*np.sqrt(H.wrapped_gaussian_ft(1.4)).astype(np.float32)[None,:],axis=1,norm='forward').astype(np.float32)
    print('X',time.time()-t, X.dtype)
    t=time.time()
    for k in range(10):
        P=H.softplus(X-1.7,2.7); P=P/P.mean(1,keepdims=True)
        C=np.mean(np.abs(np.fft.rfft(P,axis=1,norm='forward')[:, :20])**2,0)
    print('eval',(time.time()-t)/10, P.dtype)
EOF
python t5.py
```

```
X 0.031455278396606445 float32
eval 0.040715146064758304 float32
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/repo; python - <<'EOF'
import json
nb=json.load(open('notebooks/closing_the_loop.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='code':
        s=''.join(c['source']); print(f'--- [{i}]'); print(s[:4000])
        for o in c.get('outputs',[]):
            if 'text' in o: print('OUT:', ''.join(o['text'])[-300:])
EOF
```

```
--- [1]
# Regeneration switches (default off so a normal run cannot overwrite committed figures/caches):
REGENERATE_CACHES = False

import numpy as np
from pynwb import NWBHDF5IO
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
from ring import data
from ring import style
#from ring.data_driven import circular_com
--- [2]
def circular_com(data, return_idx=False):
    #data = (N_curves, N_theta)
    theta = np.linspace(0, 2*np.pi, data.shape[1], endpoint=False)
    x_comp = np.sum(data * np.cos(theta), axis=1)
    y_comp = np.sum(data * np.sin(theta), axis=1)
    result = np.arctan2(y_comp, x_comp) % (2*np.pi)
    if not return_idx:
        return result
[... 213 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/src && cat > $TMPDIR/src/build.py <<'EOF'
"""Convert a percent-format script to ipynb. Markers: '# %%' code, '# %% [markdown]' markdown, optional 'tags=a,b'."""
import json, sys, re
def build(src, dst):
    cells=[]; cur=None
    for line in open(src).read().split('\n'):
        if line.startswith('# %%'):
            if cur: cells.append(cur)
            md='[markdown]' in line
            m=re.search(r'tags=(\S+)', line)
            tags=m.group(1).split(',') if m else []
            cur={'cell_type':'markdown' if md else 'code','metadata':({'tags':tags} if tags else {}),'source':[]}
            if not md: cur.update(execution_count=None, outputs=[])
            continue
        cur['source'].append(line)
    cells.append(cur)
    for c in cells:
        s=c['source']
        while s and not s[-1].strip(): s.pop()
        while s and not s[0].strip(): s.pop(0)
        if c['cell_type']=='markdown': s=[l[2:] if l.startswith('# ') else (l[1:] if l.startswith('#') else l) for l in s]
        c['source']=[l+'\n' for l in s[:-1]]+s[-1:] if s else []
    nb={'cells':cells,'metadata':{'kernelspec':{'display_name':'Python 3','language':'python','name':'python3'},'language_info':{'name':'python'}},'nbformat':4,'nbformat_minor':5}
    for i,c in enumerate(cells): c['id']=f'c{i:03d}'
    json.dump(nb, open(dst,'w'), indent=1)
if __name__=='__main__': build(sys.argv[1], sys.argv[2])
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd paper; grep -n -i "two-point correlation\|C(θ, θ′)\|circulant form\|(4)$" 10.1038-s41593-026-02452-4.txt | head -20; grep -n "Fig. 5" 10.1038-s41593-026-02452-4.txt | head; grep -n -i "time-reversed\|excitatory" 10.1038-s41593-026-02452-4.txt | head
```

```
437:(4)
438:is the two-point correlation function of the target firing rates. Equation 
691:As a stronger test, we computed the two-point correlation function 
693:circulant form (Fig. 3c), as does the centered and variance-normalized 
721:two-point correlation function, pooled across mice, and that of the 
838:Fig. 3 | Tuning-curve center-of-mass angles and two-point correlation 
842:for visual comparison. c, Empirical two-point correlation functions Cφ(θ, θ′) 
1115:dot marks the minimum, (b, β) ≈ (1.73, 2.77). f, Two-point correlation function of 
3274:Two-point correlation function of the target
3293:Two-point correlation functions of the input
3521:(4)
3575:It will often be useful to regard two-point correlation functions as matrices, written in bold, once their arguments
4280:vectors U x and U φ are the eigenvectors of the empirical two-point correlation matrices
6094:Supplementary Figure 13: Centered and variance-normalized two-point correlation functions and their eigenvectors
6097:uncentered, unnormalized two-point correlation function. b, The five leading eigenvectors, PC1 to PC5, of the centered
7050:teacher correlation matrix has the circulant form Ψμν = Ψ(θμ −θν), with
724:We validated the process against several statistical features (Fig. 5 
725:and Methods). The predicted center-of-mass-aligned mean and fluctuation profiles match the data (Fig. 5a,b and ‘Failure of classical 
851:with strongest agreement at higher thresholds (Fig. 5c), and the full 
852:distributions of tuning-curve values at the three highest peaks (Fig. 5d). 
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 420,445p 10.1038-s41593-026-02452-4.txt; sed -n 685,730p 10.1038-s41593-026-02452-4.txt; sed -n 836,860p 10.1038-s41593-026-02452-4.txt; sed -n 1320,1345p 10.1038-s41593-026-02452-4.txt
```

```
dθ′K−1
i,λ(θ, θ′)x∗
i (θ)φ∗
j (θ′),
(3)
where Ki,λ(θ, θ′) = Cφ(θ, θ′) −N−1φ∗
i (θ)φ∗
i (θ′) + 2πλδ(θ −θ′). The second term is related to the constraint Jii = 0 and vanishes at large N. The 
first term,
Cφ(θ, θ′) = 1
N
N
∑
i=1
φ∗
i (θ)φ∗
i (θ′),
(4)
is the two-point correlation function of the target firing rates. Equation 
(3) is Hebbian in form, with φ∗
[... 103 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && python -c "
import requests
for v in ['0.240528.1542','0.261016.2310']:
    d=requests.get(f'https://api.dandiarchive.org/api/dandisets/000939/versions/{v}/assets/?page_size=200').json()
    print(v, d['count'], d['results'][0])
r=requests.get('https://api.dandiarchive.org/api/dandisets/000939/versions/0.261016.2310/').json(); print(r.get('metadata',{}).get('description','')[:1500]); print(r['metadata'].get('relatedResource'))
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 6, in <module>
    r=requests.get('https://api.dandiarchive.org/api/dandisets/000939/versions/0.261016.2310/').json(); print(r.get('metadata',{}).get('description','')[:1500]); print(r['metadata'].get('relatedResource'))
                                                                                                                                                                        ~^^^^^^^^^^^^
KeyError: 'metadata'
0.240528.1542 31 {'asset_id': '03683ad0-e0c4-4281-8328-8882df292728', 'blob': '1fe572ba-dcf5-46cd-a333-094f13223b16', 'zarr': None, 'path': 'sub-A1824/sub-A1824_behavior+ecephys+ogen.nwb', 'size': 1496267621, 'created': '2024-05-28T15:03:37.035149Z', 'modified': '2024-05-28T15:42:26.470967Z'}
0.261016.2310 31 {'asset_id': 'bc970cdf-cb90-418f-97ce-2db498cd292f', 'blob': 'f395168c-11e6-4cb8-b775-5fd28b03c2a2', 'zarr': None, 'path': 'sub-A1813/sub-A1813_ses-190408_behavior+ecephys+ogen.nwb', 'size': 24185684139, 'created': '2026-05-12T12:29:39.849911Z', 'modified': '2026-05-12T16:11:07.553710Z'}
```

**Agent calls Bash**

```bash
cat >> entries/clark-2026/hdring.py <<'EOF'


# ---------------------------------------------------------------- measures chosen in the claims file


def circulant_projection(M):
    """Average of a square matrix along its circular diagonals (claims file, fig3c criterion)."""
    n = M.shape[0]
    i = np.arange(n)
    prof = np.array([M[i, (i + d) % n].mean() for d in range(n)])
    return prof[(i[None, :] - i[:, None]) % n]


def rel_dist_from_circulant(M):
    """||M - circ(M)||_F / ||M||_F (claims file, fig3c criterion)."""
    return np.linalg.norm(M - circulant_projection(M)) / np.linalg.norm(M)


def fourier_purity(v):
    """Fraction of a vector's power at its dominant frequency, counting +k and -k together,
    and that frequency (claims file, fig3c criterion)."""
    F = np.abs(np.fft.fft(v)) ** 2
    n = len(v)
    p = np.array([F[0]] + [F[k] + F[n - k] for k in range(1, n // 2)] + ([F[n // 2]] if n % 2 == 0 else []))
    k = int(np.argmax(p))
    return p[k] / p.sum(), k


def circ_diff(a, b):
    """Absolute circular difference in [0, pi]."""
    return np.abs(np.angle(np.exp(1j * (np.asarray(a) - np.asarray(b)))))


def ks_distance(a, b):
    from scipy.stats import ks_2samp
    return ks_2samp(a, b).statistic


def tv_distance(p, q):
    return 0.5 * np.abs(np.asarray(p) - np.asarray(q)).sum()


def hellinger(p, q):
    return np.sqrt(0.5 * ((np.sqrt(p) - np.sqrt(q)) ** 2).sum())
EOF
echo ok
```

```
ok
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude/placeholder",
 "content": "x\n"
}
```

```
File created successfully at: /tmp/claude/placeholder (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
echo $TMPDIR
```

```
/tmp/claude-1001
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/src/nb1.py",
 "content": "# %% [markdown]\n# # Clark, Abbott & Sompolinsky (2026): the tuning-curve claims, on DANDI:000939\n#\n# **Paper.** D. G. Clark, L. F. Abbott, H. Sompolinsky, \"Symmetries and continuous attractors in\n# disordered neural circuits\", Nature Neuroscience (2026), doi:10.1038/s41593-026-02452-4. The\n# claims file `claims/clark-2026.yaml` was written from the version of record (main text, Methods,\n# figure legends and the Supplementary Information).\n#\n# **Dataset.** DANDI:000939 (Duszkiewicz et al. 2024, postsubiculum of freely moving mice), pinned\n# at version **0.240528.1542** (doi:10.48324/dandi.000939/0.240528.1542). This is the version the\n# paper cites (claims file, opening comment). Later versions exist (0.250207.0025 to\n# 0.261016.2310); the cell below shows that every file changed after this version (new names with\n# session ids and sizes of about 24 GB), so the cited version is the one that holds the files the\n# paper's code read. The paper reuses this dataset (`relation: reuses`).\n#\n# **Outside input.** The paper's cached tuning curves, `mouse_data/tc_data.npz` in Zenodo\n# doi:10.5281/zenodo.21827768 (version 1.0), read by range requests from the record's tar and\n# checked against the record's MD5. It is used only by the link claim `tuning-curves-match-cache`.\n# Everything else is computed from the NWB files, streamed from the archive.\n#\n# **Code followed.** github.com/davidclark1/symmetries-continuous-attractors at commit 245726f\n# (the claims file cites it); `hdring.py` in this entry repeats the parts used, in numpy, and names\n# the function of the paper's code each one repeats.\n#\n# This notebook tests the claims on the tuning curves and the generative process. The claims on\n# the data-derived network are in `network.ipynb`.\n#\n# | claim | tested here |\n# |---|---|\n# | hd-cell-selection (link) | yes |\n# | tuning-curves-match-cache (link, with inputs) | yes |\n# | fig1e-heterogeneous-peaks | yes |\n# | fig5d-peak-numbers | yes |\n# | fig1fg-mean-and-fluctuation-profiles | yes |\n# | fig3ab-centers-of-mass-uniform | yes |\n# | fig3c-correlation-approaches-circulant | yes |\n# | fig4-generative-fit | yes |\n# | fig5ab-profiles-match | yes |\n# | fig5c-peak-counts-match | yes |\n# | fig5d-peak-heights-match | yes |\n# | fig5e-flip-symmetry-match | yes |\n# | fig5f-information-match | yes |\n# | fig2l-recorded-bump-tracks-hd | yes |\n# | network claims (fig2b to figs14) | in network.ipynb |\n# | simulation-only claims (data: elsewhere) | see the attempt record |\n\n# %%\nimport os, time, resource\nos.environ.setdefault(\"OMP_NUM_THREADS\", \"4\")\nimport numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nimport requests\nfrom astropy.stats import kuiper, circcorrcoef\nfrom statsmodels.stats.multitest import multipletests\nimport hdring as H\n\nT0 = time.time()\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 30)\nprint(\"dandiset\", H.DANDISET, \"version\", H.VERSION)\n\n# %% [markdown]\n# ## Files and versions\n\n# %%\nassets = H.list_assets()\norder = H.session_order(assets)\nprint(len(assets), \"assets at\", H.VERSION)\nfor a in sorted(assets, key=lambda a: a[\"path\"]):\n    print(f\"  {a['path']:50s} {a['size']/1e9:6.2f} GB\")\n# compare with the latest published version\nvers = requests.get(f\"{H.API}/dandisets/{H.DANDISET}/versions/?page_size=100\").json()[\"results\"]\npub = [v[\"version\"] for v in vers if v[\"version\"] != \"draft\"]\nlatest = sorted(pub)[-1]\nla = H.list_assets(latest)\nblobs_pinned = {a[\"blob\"] for a in assets}\nprint(\"published versions:\", \", \".join(sorted(pub)))\nprint(f\"latest {latest}: {len(la)} assets, sizes {min(a['size'] for a in la)/1e9:.1f} to {max(a['size'] for a in la)/1e9:.1f} GB;\",\n      \"files shared with the pinned version (same blob):\", sum(a[\"blob\"] in blobs_pinned for a in la))\nprint(\"example path in latest:\", la[0][\"path\"])\n\n# %% [markdown]\n# ## Load every session\n#\n# One file per subject (the `+ogen.nwb` file where a session has one, as `ring/data.py`\n# `get_session_info` chooses; at this version each subject has exactly one file), in the code's\n# sorted order, which fixes the session index. For each file the epochs, the head direction and\n# the units table are read; spike times are read for the head-direction units only. The\n# cross-validated tuning curves are computed as `ring/data.py` `process_file` does (helper,\n# `tuning_curves_session`).\n\n# %%\nsessions = []\nt = time.time()\nfor i, (path, aid, subj, ogen) in enumerate(order):\n    s = H.load_session(aid)\n    plain, opt, sig = H.tuning_curves_session(s)\n    hd_idx, ti, tf, ti_idx, tf_idx = H.epoch_bins(s)\n    sessions.append(dict(idx=i, subject=subj, path=path, ogen=ogen, sess=s, plain=plain, opt=opt, sig=sig,\n                         hd_idx=hd_idx, ti=ti, tf=tf))\nprint(f\"loaded {len(sessions)} sessions in {time.time()-t:.0f} s; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6:.2f} GB\")\n\n# %% tags=sanity\nrows = []\nfor d in sessions:\n    s = d[\"sess\"]\n    hd = s[\"hd\"]\n    dt = np.diff(s[\"hd_t\"])\n    ep = {t: (a, b) for t, a, b in s[\"epochs\"]}\n    rows.append(dict(\n        session=d[\"idx\"], subject=d[\"subject\"], file_ogen=d[\"ogen\"], units=s[\"n_units\"],\n        hd_units=int(s[\"is_hd\"].sum()), exc_units=int(s[\"is_exc\"].sum()), fs_units=int(s[\"is_fs\"].sum()),\n        hd_and_exc=int((s[\"is_hd\"] & s[\"is_exc\"]).sum()), hd_not_exc=int((s[\"is_hd\"] & ~s[\"is_exc\"]).sum()),\n        epochs=\"/\".join(t for t, _, _ in s[\"epochs\"]),\n        square_s=round(d[\"tf\"] - d[\"ti\"], 1), hd_dt_median_ms=round(np.median(dt) * 1e3, 3),\n        hd_dt_max_in_square_ms=round(np.max(np.diff(s[\"hd_t\"][(s[\"hd_t\"] >= d[\"ti\"]) & (s[\"hd_t\"] <= d[\"tf\"])])) * 1e3, 1),\n        hd_min=round(np.nanmin(hd), 4), hd_max=round(np.nanmax(hd), 4), hd_nan_square=round((d[\"hd_idx\"] < 0).mean(), 4),\n        spikes_in_square=int(sum(((x >= d[\"ti\"]) & (x < d[\"tf\"])).sum() for x in s[\"spikes\"])),\n        unsorted_spike_trains=int(sum(np.any(np.diff(x) < 0) for x in s[\"spikes\"])),\n    ))\ntab = pd.DataFrame(rows)\nprint(tab.to_string(index=False))\nprint(\"head-direction unit:\", sessions[0][\"sess\"][\"hd_unit\"])\nprint(\"totals: sessions\", len(tab), \"| units\", tab.units.sum(), \"| head-direction units\", tab.hd_units.sum(),\n      \"| of which excitatory\", tab.hd_and_exc.sum(), \"| sessions with a +ogen file\", int(tab.file_ogen.sum()),\n      \"| sessions with a wake_opto epoch\", int(tab.epochs.str.contains(\"wake_opto\").sum()))\nprint(\"one subject per session:\", tab.subject.nunique() == len(tab))\nprint(\"bins of the 100-bin head-direction grid never visited in a square epoch, per session (max):\",\n      max(int((np.bincount(d['hd_idx'][d['hd_idx'] >= 0], minlength=100) == 0).sum()) for d in sessions))\n\n# %% [markdown]\n# ### Recordings deposited more than once, and the shared clock\n#\n# Duplicates: the number of head-direction samples and the first spike time of the first unit are\n# compared across sessions. Clock: for every session, the head-direction information of the plain\n# (unsmoothed) tuning curves of its head-direction units over the square epoch is computed with\n# the spike times shifted by a lag between -2 s and +2 s. If spikes and head direction share a\n# clock, the information peaks near lag 0 (a head-direction cell's tuning is sharpest at a lag of\n# a few tens of ms, its anticipatory time interval).\n\n# %%\nsig_keys = [(len(d[\"sess\"][\"hd\"]), round(float(d[\"sess\"][\"spikes\"][0][0]), 6) if len(d[\"sess\"][\"spikes\"][0]) else None) for d in sessions]\ndups = [(sessions[i][\"subject\"], sessions[j][\"subject\"]) for i in range(len(sessions)) for j in range(i + 1, len(sessions)) if sig_keys[i] == sig_keys[j]]\nprint(\"sessions with identical head-direction sample count and first spike time:\", dups if dups else \"none\")\nnhd = [len(d[\"sess\"][\"hd\"]) for d in sessions]\nprint(\"distinct head-direction sample counts:\", len(set(nhd)), \"of\", len(nhd))\n\nlags = np.array([-2, -1, -0.5, -0.2, -0.1, -0.05, -0.02, 0, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2])\ndef info_at_lag(d, lag):\n    hd_idx, ti = d[\"hd_idx\"], d[\"ti\"]\n    N = len(hd_idx); ok = hd_idx >= 0\n    occ = np.bincount(hd_idx[ok], minlength=100).astype(float)\n    vals = []\n    for st in d[\"sess\"][\"spikes\"]:\n        c = H.spike_counts(st + lag, ti, d[\"tf\"], N)\n        r = np.bincount(hd_idx[ok], weights=c[ok], minlength=100) / np.maximum(occ, 1)\n        p = occ / occ.sum(); lam = (p * r).sum()\n        if lam <= 0: continue\n        q = r / lam\n        vals.append(np.nansum(p * q * np.log2(np.where(q > 0, q, 1))))\n    return np.mean(vals)\nclock = np.array([[info_at_lag(d, L) for L in lags] for d in sessions])\nbest = lags[clock.argmax(1)]\nct = pd.DataFrame(clock.round(3), columns=[f\"{L:+g}s\" for L in lags]); ct.insert(0, \"subject\", [d[\"subject\"] for d in sessions])\nprint(\"mean information (bits per spike) of the head-direction units, spikes shifted by the lag:\")\nprint(ct.to_string(index=False))\nprint(\"lag of maximum information per session:\", dict(zip([d['subject'] for d in sessions], best)))\nprint(\"sessions whose maximum is within 0.1 s of lag 0:\", int((np.abs(best) <= 0.1).sum()), \"of\", len(best))\nprint(\"ratio of information at lag 0 to that at +-2 s (median over sessions):\",\n      round(float(np.median(clock[:, lags == 0][:, 0] / np.maximum(clock[:, 0], clock[:, -1]))), 2))\n\n# %% [markdown]\n# ## hd-cell-selection (link)\n#\n# > The dandiset holds the 31 sessions, one per mouse, with 2,691 units, of which 1,533 carry the\n# > head-direction label; nine of the mice, which also underwent optogenetic manipulation in a\n# > separate epoch, contribute 315 of those cells; the four mice with most head-direction cells\n# > have 117, 93, 90 and 86.\n\n# %% tags=claim:hd-cell-selection\nunits = tab.units.sum()\nhd_a = tab.hd_units.sum()                     # reading (a), is_head_direction\nhd_b = tab.hd_and_exc.sum()                   # reading (b), is_head_direction and is_excitatory\nopt_mean = [d[\"opt\"].mean(1) for d in sessions]\nnz = np.concatenate([~np.all(o == 0, axis=1) for o in opt_mean])\nopto = tab[tab.epochs.str.contains(\"wake_opto\")]\nprint(\"sessions (mice):\", len(tab), \"(expected 31)\")\nprint(\"units in all sessions:\", units, \"(expected 2691)\")\nprint(\"head-direction units, reading (a) is_head_direction:\", hd_a, \"(expected 1533)\")\nprint(\"head-direction units, reading (b) is_head_direction and is_excitatory:\", hd_b)\nprint(\"reading (a) after the code's drop of all-zero final curves (nz_mask):\", int(nz.sum()), \"dropped:\", int((~nz).sum()))\nprint(\"mice with a wake_opto epoch:\", len(opto), list(opto.subject), \"; their head-direction cells:\", opto.hd_units.sum(), \"(expected 315)\")\ntop = tab.sort_values(\"hd_units\", ascending=False).head(4)\nprint(\"four mice with most head-direction cells:\", list(zip(top.subject, top.hd_units)), \"(expected A3707 117, A3716 93, A3711 90, A3706 86)\")\nprint(\"head-direction cells of A3707:\", int(tab.set_index('subject').loc['A3707', 'hd_units']), \"(expected 117)\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## tuning-curves-match-cache (link, with the Zenodo input)\n#\n# > Tuning curves computed from the dandiset with the paper's procedure agree with the tuning\n# > curves in the paper's cached results on Zenodo.\n\n# %% tags=claim:tuning-curves-match-cache\nb, md5_calc, md5_listed = H.read_zenodo_member(\"mouse_data/tc_data.npz\")\nprint(\"tc_data.npz MD5\", md5_calc, \"listed\", md5_listed, \"match:\", md5_calc == md5_listed)\ncache = H.load_npz_bytes(b)\nc_names = cache[\"mouse_names\"]; c_nums = cache[\"mouse_nums\"]; c_hd = cache[\"hd_mask\"]\nprint(\"cache: units\", len(c_hd), \"head-direction\", int(c_hd.sum()), \"sessions\", len(cache[\"unit_counts\"]))\nprint(\"cache session order equals ours:\", [str(n) for n in pd.unique(c_names)] == [d[\"subject\"] for d in sessions])\nprint(\"cache unit counts equal ours:\", list(cache[\"unit_counts\"]) == list(tab.units))\nprint(\"cache hd labels equal ours:\", np.array_equal(c_hd, np.concatenate([d[\"sess\"][\"is_hd\"] for d in sessions])),\n      \"| exc labels:\", np.array_equal(cache[\"exc_mask\"], np.concatenate([d[\"sess\"][\"is_exc\"] for d in sessions])),\n      \"| fs labels:\", np.array_equal(cache[\"fs_mask\"], np.concatenate([d[\"sess\"][\"is_fs\"] for d in sessions])))\nours_opt = np.concatenate([d[\"opt\"] for d in sessions]); ours_sig = np.concatenate([d[\"sig\"] for d in sessions])\nours_plain = np.concatenate([d[\"plain\"] for d in sessions])\nc_opt = cache[\"opt_tcs\"][c_hd]; c_sig = cache[\"opt_sigmas\"][c_hd]; c_plain = cache[\"plain_tcs\"][c_hd]\nr = np.array([np.corrcoef(a.mean(0), b_.mean(0))[0, 1] for a, b_ in zip(ours_opt, c_opt)])\nprint(\"units compared:\", len(r))\nprint(f\"Pearson r of partition-averaged curves: min {r.min():.6f}, median {np.median(r):.6f}; fraction >= 0.99: {(r >= 0.99).mean():.4f}\")\nprint(\"max abs difference of partition-averaged curves (Hz):\", float(np.abs(ours_opt.mean(1) - c_opt.mean(1)).max()))\nprint(\"max abs difference of plain curves (Hz):\", float(np.abs(ours_plain - c_plain).max()))\nsame_sig = ours_sig == c_sig\nprint(f\"chosen widths equal for both partitions: {same_sig.all(1).mean():.4f} of units; per partition: {same_sig.mean():.4f}\")\ndiff_curve = np.abs(ours_opt - c_opt).max(2)\nprint(\"where the widths differ, max abs curve difference:\", float(diff_curve[~same_sig].max()) if (~same_sig).any() else None,\n      \"| our width range there:\", (float(ours_sig[~same_sig].min()), float(ours_sig[~same_sig].max())) if (~same_sig).any() else None,\n      \"| cache width range there:\", (float(c_sig[~same_sig].min()), float(c_sig[~same_sig].max())) if (~same_sig).any() else None)\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## The curves used below\n#\n# As `data_and_generative_model.ipynb` cell 3: the partition-averaged curves of the units with\n# `is_head_direction` and a non-zero curve, each divided by its mean over the 100 bins.\n\n# %%\nhdmask_all = np.concatenate([d[\"sess\"][\"is_hd\"][d[\"sess\"][\"spike_units\"]] for d in sessions])  # all True (hd units loaded)\nPhi_list, mouse_nums = [], []\nfor d in sessions:\n    o = d[\"opt\"].mean(1)\n    keep = ~np.all(o == 0, axis=1)\n    o = o[keep]\n    Phi_list.append(o / o.mean(1, keepdims=True)); mouse_nums += [d[\"idx\"]] * len(o)\nPhi_data = np.concatenate(Phi_list); mouse_nums = np.array(mouse_nums)\nnames = np.array([d[\"subject\"] for d in sessions])\nprint(\"Phi_data\", Phi_data.shape, \"range\", Phi_data.min().round(4), Phi_data.max().round(3), \"row means\", Phi_data.mean(1).min().round(6), Phi_data.mean(1).max().round(6))\n\n# %% [markdown]\n# ## fig1e-heterogeneous-peaks\n#\n# > Mouse head-direction cells are heterogeneous, with variable numbers of irregularly spaced\n# > peaks, unlike the classical prediction of tuning curves identical up to shifts.\n\n# %% tags=claim:fig1e-heterogeneous-peaks\npc1 = H.peak_counts(Phi_data, 1.0)\nprint(\"peak-count distribution at zthresh 1:\", dict(zip(*np.unique(pc1, return_counts=True))))\nseps = []\nfor tcv in Phi_data[pc1 >= 2]:\n    mx = H.find_local_maxima(tcv, 1.0)\n    top2 = mx[np.argsort(tcv[mx])[::-1][:2]]\n    seps.append(H.circ_diff(*(2 * np.pi * top2 / 100)))\nseps = np.array(seps)\nq = np.percentile(seps, [0, 10, 25, 50, 75, 90, 100])\nprint(\"multi-peaked curves:\", len(seps))\nprint(\"separation of the two highest peaks (rad), percentiles 0,10,25,50,75,90,100:\", q.round(3))\nprint(f\"interquartile range {q[4]-q[2]:.3f} rad against pi/4 = {np.pi/4:.3f}\")\nprint(\"histogram of separations (8 bins over 0 to pi):\", np.histogram(seps, bins=8, range=(0, np.pi))[0])\nfor z in (0.5, 0.0):\n    pcz = H.peak_counts(Phi_data, z)\n    print(f\"variant, zthresh {z}: peak-count distribution\", dict(zip(*np.unique(pcz, return_counts=True))))\nby_mouse = pd.DataFrame(dict(subject=names[mouse_nums], multi=pc1 >= 2)).groupby(\"subject\").multi.agg([\"sum\", \"count\"])\nprint(\"curves with 2 or more peaks by mouse (sum of count):\", by_mouse.apply(lambda r: f\"{r['sum']}/{r['count']}\", axis=1).to_dict())\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig5d-peak-numbers\n#\n# > At zthresh 1, all 1,533 experimental curves have at least one peak, 412 have at least two and\n# > 55 at least three; of 100,000 generative-process samples, 24,271 have at least two and 1,043 at\n# > least three.\n#\n# The generative samples are drawn at the paper's fitted parameters, as the criterion says, from\n# this claim's seed (protocol); the paper's notebook used numpy seed 42 with the legacy global\n# generator, whose draws a seeded `Generator` does not repeat. The tolerance covers this. The\n# result is also given under four more seeds.\n\n# %% tags=claim:fig5d-peak-numbers\nPAPER_PARAMS = (1.4211, 1.7307, 2.7659)   # scale, bias, beta (claims file; notebook printout)\nprint(\"data, at least 1, 2, 3 peaks:\", [(pc1 >= k).sum() for k in (1, 2, 3)], \"(expected 1533, 412, 55)\")\ngen_counts = {}\nfor k in range(5):\n    sd = H.seed(\"fig5d-peak-numbers\") + 1000 * k\n    G = H.gen_Phi_m(*PAPER_PARAMS, 100000, np.random.default_rng(sd))\n    pg = H.peak_counts(G, 1.0)\n    gen_counts[sd] = [(pg >= j).sum() for j in (1, 2, 3)]\n    print(f\"seed {sd}: generative, at least 1, 2, 3 peaks of 100,000:\", gen_counts[sd], \"(expected 100000, 24271, 1043)\")\nv2 = [c[1] for c in gen_counts.values()]; v3 = [c[2] for c in gen_counts.values()]\nprint(\"range over five seeds: >=2\", min(v2), max(v2), \"| >=3\", min(v3), max(v3))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig1fg-mean-and-fluctuation-profiles\n#\n# > Aligned by their circular centers of mass within each of the 31 mice, the tuning curves have\n# > unimodal, symmetric mean profiles, but fluctuations about them comparable in magnitude to the\n# > means, and both profiles are consistent across mice.\n\n# %% tags=claim:fig1fg-mean-and-fluctuation-profiles\ndef mouse_profiles(Phi, mn):\n    mus, sds = [], []\n    for m in range(mn.max() + 1):\n        c = H.center_tuning_curves(Phi[mn == m]); mus.append(c.mean(0)); sds.append(c.std(0))\n    return np.array(mus), np.array(sds)\nmus, sds = mouse_profiles(Phi_data, mouse_nums)\nmu_avg, sd_avg = mus.mean(0), sds.mean(0)\nrefl = lambda p: np.roll(p[::-1], 1)\nmaxima = np.where((mu_avg > np.roll(mu_avg, 1)) & (mu_avg > np.roll(mu_avg, -1)))[0]\noff = lambda i: (i + 50) % 100 - 50\nprint(\"mouse-average mean profile: local maxima at offsets\", [off(i) for i in maxima], \"| peak\", mu_avg.max().round(3), \"at offset\", off(mu_avg.argmax()))\nunimodal = len(maxima) == 1 and abs(off(maxima[0])) <= 2\nr_sym = np.corrcoef(mu_avg, refl(mu_avg))[0, 1]\nprint(\"unimodal:\", unimodal, \"| symmetry r with reflection:\", round(r_sym, 4), \"(>= 0.9)\")\nra = 0.5 * mu_avg.max() <= sd_avg.max() <= 2 * mu_avg.max()\nrb = sd_avg[0] > 0.5 * mu_avg[0]\nprint(f\"peak of sd profile {sd_avg.max():.3f}, peak of mean profile {mu_avg.max():.3f}, ratio {sd_avg.max()/mu_avg.max():.3f}; reading (a) holds: {ra}\")\nprint(f\"at offset 0: sd {sd_avg[0]:.3f}, mean {mu_avg[0]:.3f}, ratio {sd_avg[0]/mu_avg[0]:.3f}; reading (b) holds: {rb}\")\nr_mu = np.array([np.corrcoef(m, mu_avg)[0, 1] for m in mus]); r_sd = np.array([np.corrcoef(s_, sd_avg)[0, 1] for s_ in sds])\nprint(f\"consistency: median r of mouse mean profiles with the average {np.median(r_mu):.3f} (min {r_mu.min():.3f}); of sd profiles {np.median(r_sd):.3f} (min {r_sd.min():.3f})\")\nper = pd.DataFrame(dict(subject=names, n=[(mouse_nums == m).sum() for m in range(31)], mean_peak=mus.max(1).round(2), sd_peak=sds.max(1).round(2),\n                        sd_over_mean_at0=(sds[:, 0] / mus[:, 0]).round(2), r_mean=r_mu.round(3), r_sd=r_sd.round(3), sym_r=[round(np.corrcoef(m, refl(m))[0, 1], 3) for m in mus]))\nprint(per.to_string(index=False))\nfig, ax = plt.subplots(1, 2, figsize=(7, 2.3))\nx = np.arange(-50, 50) * 2 * np.pi / 100\nfor m in range(31):\n    ax[0].plot(x, np.roll(mus[m], 50), c=\"0.7\", lw=0.5); ax[1].plot(x, np.roll(sds[m], 50), c=\"0.7\", lw=0.5)\nax[0].plot(x, np.roll(mu_avg, 50), c=\"k\"); ax[1].plot(x, np.roll(sd_avg, 50), c=\"k\")\nax[0].set_title(\"mean profile\"); ax[1].set_title(\"sd profile\"); ax[0].set_xlabel(\"offset (rad)\"); ax[1].set_xlabel(\"offset (rad)\")\nplt.show()\nprint(\"plotted ranges: mean\", mus.min().round(3), mus.max().round(3), \"| sd\", sds.min().round(3), sds.max().round(3))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig3ab-centers-of-mass-uniform\n#\n# > Within each session the tuning-curve centers of mass are distributed uniformly; the Kuiper test\n# > rejects uniformity in 2 of 31 sessions before correction and in none after Benjamini-Hochberg\n# > correction, with corrected P values from 0.59 to 0.97.\n\n# %% tags=claim:fig3ab-centers-of-mass-uniform\ncoms = H.circular_center_of_mass(Phi_data)\npv, stat = [], []\nfor m in range(31):\n    D, p = kuiper(coms[mouse_nums == m], lambda x: x / (2 * np.pi)); pv.append(p); stat.append(D)\npv = np.array(pv)\nrej, pcor, _, _ = multipletests(pv, alpha=0.05, method=\"fdr_bh\")\nprint(\"sessions with uncorrected P < 0.05:\", int((pv < 0.05).sum()), \"(expected 2)\")\nprint(\"sessions significant after BH:\", int(rej.sum()), \"(expected 0)\")\nprint(f\"corrected P range {pcor.min():.3f} to {pcor.max():.3f} (expected 0.59 to 0.97); uncorrected {pv.min():.3f} to {pv.max():.3f}\")\nprint(pd.DataFrame(dict(subject=names, n=[(mouse_nums == m).sum() for m in range(31)], kuiper_V=np.round(stat, 3), p=pv.round(4), p_bh=pcor.round(4))).to_string(index=False))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig3c-correlation-approaches-circulant\n#\n# > Within a mouse, the two-point correlation function of the tuning curves approaches a circulant\n# > form as more neurons are included, as does the centered and variance-normalized correlation\n# > function, whose eigenvectors converge to Fourier modes, as circular symmetry predicts.\n\n# %% tags=claim:fig3c-correlation-approaches-circulant\ntop4 = [int(np.where(names == n)[0][0]) for n in [\"A3707\", \"A3716\", \"A3711\", \"A3706\"]]\nsizes = [5, 10, 20, 40, 80]\ndef circ_dists(rng):\n    out = {}\n    for m in top4:\n        tcs = Phi_data[mouse_nums == m]\n        for kind in (\"raw\", \"norm\"):\n            row = []\n            for n in sizes:\n                ds = []\n                for _ in range(100):\n                    sub = tcs[rng.choice(len(tcs), n, replace=False)]\n                    if kind == \"norm\":\n                        sub = (sub - sub.mean(0)) / sub.std(0)\n                    ds.append(H.rel_dist_from_circulant(sub.T @ sub / n))\n                row.append(np.mean(ds))\n            out[(names[m], kind)] = row\n    return out\ndef falls(row):\n    return row[-1] < row[0] and int((np.diff(row) > 0).sum()) <= 1\nres3c = {}\nfor k in range(5):\n    sd = H.seed(\"fig3c-correlation-approaches-circulant\") + 1000 * k\n    res3c[sd] = circ_dists(np.random.default_rng(sd))\nsd0 = H.seed(\"fig3c-correlation-approaches-circulant\")\ntab3c = pd.DataFrame({f\"{a} {b}\": np.round(v, 4) for (a, b), v in res3c[sd0].items()}, index=[f\"N={n}\" for n in sizes]).T\nprint(\"mean relative distance from circulant form, 100 subsets per size, claim seed:\")\nprint(tab3c.to_string())\npart1 = {s_: all(falls(v) for v in r_.values()) for s_, r_ in res3c.items()}\nprint(\"part 1 (distance falls, 80 < 5, at most one increase) for all mice and both functions, per seed:\", part1)\nprint(\"distance at N=80 over five seeds, range:\", {k_: (round(min(r_[k_][-1] for r_ in res3c.values()), 4), round(max(r_[k_][-1] for r_ in res3c.values()), 4)) for k_ in res3c[sd0]})\npart2 = True\nfor m in top4:\n    tcs = Phi_data[mouse_nums == m]; c = (tcs - tcs.mean(0)) / tcs.std(0); C = c.T @ c / len(c)\n    w, V = np.linalg.eigh(C); V = V[:, ::-1]\n    pur = [H.fourier_purity(V[:, j]) for j in range(5)]\n    ok = all(p >= 0.8 for p, _ in pur[:4]) and pur[0][1] == 1 and pur[1][1] == 1\n    part2 &= ok\n    print(f\"{names[m]} (N={len(tcs)}): leading eigenvectors (power fraction, frequency):\", [(round(p, 3), f) for p, f in pur], \"| holds:\", ok)\nprint(\"part 2 holds for all four mice:\", part2)\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig4-generative-fit\n#\n# > A single parameter set of the generative process, fitted to the two-point correlation\n# > function pooled over mice, is (sigma, beta, b) of about (1.42, 2.77, 1.73).\n#\n# The grid is the criterion's (`ring/gp_opt.py`: sigma in linspace(1, 2, 20), b in linspace(0.01,\n# 5, 30), beta in linspace(0.01, 10, 30); error over the first 20 coefficients). The criterion\n# asks for 500,000 samples per evaluation; on this runner's CPUs that is about 3 hours for the\n# 18,000 points. So the whole grid is first evaluated with 25,000 samples, the same draws for every\n# point (common random numbers, float32 as the paper's torch run on a GPU), and the 30 best points\n# are then evaluated again with 500,000 fresh samples each, which decide the minimum. This is a\n# deviation, recorded in the attempt; the shortlist pass and the final pass are both shown.\n\n# %% tags=claim:fig4-generative-fit\n_, Gdata_ft = H.calc_C(Phi_data)\nscale_vals = np.linspace(1, 2, 20); bias_vals = np.linspace(0.01, 5, 30); beta_vals = np.linspace(0.01, 10, 30)\ndef grid_pass(rng, N=25000):\n    z = H.sample_z(rng, N, 51, dtype=np.float32).astype(np.complex64)\n    L = np.zeros((20, 30, 30), dtype=np.float64)\n    for i, sc in enumerate(scale_vals):\n        X = np.fft.irfft(z * np.sqrt(H.wrapped_gaussian_ft(sc)).astype(np.float32)[None, :], axis=1, norm=\"forward\").astype(np.float32)\n        for j, b_ in enumerate(bias_vals):\n            Xb = X - np.float32(b_)\n            for k, be in enumerate(beta_vals):\n                P = H.softplus(Xb, np.float32(be)); P = P / (P.mean(1, keepdims=True) + 1e-30)\n                C = np.mean(np.abs(np.fft.rfft(P, axis=1, norm=\"forward\")[:, :20]) ** 2, 0)\n                L[i, j, k] = np.sqrt(((C - Gdata_ft[:20]) ** 2).sum())\n    return L\ndef final_pass(L, rng, n_best=30, N=500000):\n    idx = np.argsort(L.ravel())[:n_best]\n    out = []\n    for f in idx:\n        i, j, k = np.unravel_index(f, L.shape)\n        errs = []\n        for chunk in range(5):   # 5 x 100,000 = 500,000 samples, in chunks to bound memory\n            P = H.gen_Phi_m(scale_vals[i], bias_vals[j], beta_vals[k], 100000, rng)\n            errs.append(np.mean(np.abs(np.fft.rfft(P, axis=1, norm=\"forward\")[:, :20]) ** 2, 0))\n        C = np.mean(errs, 0)\n        out.append((np.sqrt(((C - Gdata_ft[:20]) ** 2).sum()), scale_vals[i], bias_vals[j], beta_vals[k], L[i, j, k]))\n    return sorted(out)\nt = time.time()\nsd0 = H.seed(\"fig4-generative-fit\")\nL = grid_pass(np.random.default_rng(sd0))\ni, j, k = np.unravel_index(L.argmin(), L.shape)\nprint(f\"shortlist pass (25,000 samples) in {time.time()-t:.0f} s: minimum at sigma {scale_vals[i]:.4f}, b {bias_vals[j]:.4f}, beta {beta_vals[k]:.4f}, error {L.min():.5f}\")\nfits = {}\nfor kk in range(5):\n    sd = sd0 + 1000 * kk\n    fp = final_pass(L, np.random.default_rng(sd + 1))   # second generator of the claim: seed + 1\n    fits[sd] = fp[0]\n    print(f\"seed {sd}: final pass (500,000 samples) best sigma {fp[0][1]:.4f}, b {fp[0][2]:.4f}, beta {fp[0][3]:.4f}, error {fp[0][0]:.5f}\")\nfp0 = final_pass(L, np.random.default_rng(sd0 + 1))\nprint(\"final pass, claim seed, the ten best of the 30:\")\nprint(pd.DataFrame(fp0[:10], columns=[\"error_500k\", \"sigma\", \"b\", \"beta\", \"error_25k\"]).round(4).to_string(index=False))\nFIT = (fits[sd0][1], fits[sd0][2], fits[sd0][3])\nprint(f\"fitted (sigma, beta, b) = ({FIT[0]:.4f}, {FIT[2]:.4f}, {FIT[1]:.4f}); expected (1.42 +- 0.142, 2.77 +- 0.345, 1.73 +- 0.173)\")\nprint(\"over five seeds: sigma\", sorted({round(v[1], 4) for v in fits.values()}), \"beta\", sorted({round(v[3], 4) for v in fits.values()}), \"b\", sorted({round(v[2], 4) for v in fits.values()}))\nprint(\"grid point nearest the paper's parameters: sigma\", scale_vals[8].round(4), \"b\", bias_vals[10].round(4), \"beta\", beta_vals[8].round(4),\n      \"| shortlist error there\", L[8, 10, 8].round(5), \"| rank of that point in the shortlist pass:\", int((L < L[8, 10, 8]).sum()) + 1)\nprint(\"minimum error over b and beta at each sigma (shortlist pass):\", dict(zip(scale_vals.round(3), L.min((1, 2)).round(5))))\nprint(f\"time {time.time()-t:.0f} s\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## Generative samples for Fig. 5\n#\n# 100,000 samples, each divided by its mean, at the parameters fitted above (the claims depend on\n# fig4-generative-fit), and as a variant at the paper's parameters. One set per claim, from each\n# claim's seed; four more seeds for the seed check.\n\n# %%\ndef gen(params, claim, k=0):\n    return H.gen_Phi_m(*params, 100000, np.random.default_rng(H.seed(claim) + 1000 * k))\nprint(\"fitted parameters (scale, bias, beta):\", np.round(FIT, 4), \"| paper's:\", PAPER_PARAMS)\n\n# %% [markdown]\n# ## fig5ab-profiles-match\n#\n# > The center-of-mass-aligned mean and fluctuation profiles predicted by the fitted generative\n# > process match those of the data.\n\n# %% tags=claim:fig5ab-profiles-match\ndef prof_match(G):\n    c = H.center_tuning_curves(G); gm, gs = c.mean(0), c.std(0)\n    out = {}\n    for lab, g, ms_, avg in ((\"mean\", gm, mus, mu_avg), (\"sd\", gs, sds, sd_avg)):\n        within = ((g >= ms_.min(0)) & (g <= ms_.max(0))).mean()\n        peak_rel = abs(g.max() - avg.max()) / avg.max()\n        out[lab] = dict(within=within, peak_rel=peak_rel, a=within >= 0.9, b=peak_rel <= 0.1, gpeak=g.max(), dpeak=avg.max())\n    return out\nfor lab, params in ((\"fitted\", FIT), (\"paper\", PAPER_PARAMS)):\n    for k in range(5):\n        o = prof_match(gen(params, \"fig5ab-profiles-match\", k))\n        print(f\"{lab} params, seed +{1000*k}: \" + \"; \".join(f\"{p}: within range {v['within']:.2f}, peak {v['gpeak']:.3f} vs {v['dpeak']:.3f} (rel {v['peak_rel']:.3f}), (a) {v['a']}, (b) {v['b']}\" for p, v in o.items()))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig5c-peak-counts-match\n#\n# > The generative process reproduces the distribution of peak counts per tuning curve across\n# > detection thresholds, with the strongest agreement at the higher thresholds.\n\n# %% tags=claim:fig5c-peak-counts-match\nfor lab, params in ((\"fitted\", FIT), (\"paper\", PAPER_PARAMS)):\n    for k in range(5):\n        G = gen(params, \"fig5c-peak-counts-match\", k)\n        line = []\n        for z in (1.0, 0.5, 0.0):\n            p, qq = H.peak_count_hist(Phi_data, z), H.peak_count_hist(G, z)\n            line.append(f\"z {z}: TV {H.tv_distance(p, qq):.3f}, Hellinger {H.hellinger(p, qq):.3f}\")\n            if k == 0:\n                print(f\"  {lab} z {z}: data {np.round(p, 3)}, generative {np.round(qq, 3)}\")\n        print(f\"{lab} params, seed +{1000*k}: \" + \"; \".join(line))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig5d-peak-heights-match\n#\n# > The generative process reproduces the full distributions of tuning-curve values at the three\n# > highest peaks.\n\n# %% tags=claim:fig5d-peak-heights-match\npv_data = H.get_peak_values(Phi_data, 3)\nfor lab, params in ((\"fitted\", FIT), (\"paper\", PAPER_PARAMS)):\n    for k in range(5):\n        pvg = H.get_peak_values(gen(params, \"fig5d-peak-heights-match\", k), 3)\n        line = []\n        for j in range(3):\n            a_, b_ = pv_data[:, j][~np.isnan(pv_data[:, j])], pvg[:, j][~np.isnan(pvg[:, j])]\n            rel = abs(np.median(b_) - np.median(a_)) / np.median(a_)\n            line.append(f\"peak {j+1}: n {len(a_)}/{len(b_)}, median {np.median(a_):.3f}/{np.median(b_):.3f} (rel {rel:.3f}), KS {H.ks_distance(a_, b_):.3f}\")\n        print(f\"{lab} params, seed +{1000*k}: \" + \"; \".join(line))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig5e-flip-symmetry-match\n#\n# > The generative process captures the distribution of flip-symmetry correlations, particularly\n# > its strongly asymmetric tail.\n\n# %% tags=claim:fig5e-flip-symmetry-match\nsym_data = H.symmetry_scores(Phi_data)\nprint(f\"data: median {np.median(sym_data):.3f}; fraction below 0.5 {np.mean(sym_data < 0.5):.4f} ({(sym_data < 0.5).sum()} curves); below 0 {np.mean(sym_data < 0):.4f} ({(sym_data < 0).sum()} curves)\")\nfor lab, params in ((\"fitted\", FIT), (\"paper\", PAPER_PARAMS)):\n    for k in range(5):\n        sg = H.symmetry_scores(gen(params, \"fig5e-flip-symmetry-match\", k))\n        fa, fb = np.mean(sg < 0.5), np.mean(sg < 0)\n        print(f\"{lab} params, seed +{1000*k}: median {np.median(sg):.3f}; below 0.5 {fa:.4f} (ratio to data {fa/np.mean(sym_data < 0.5):.2f}); below 0 {fb:.4f} (ratio {fb/max(np.mean(sym_data < 0), 1e-12):.2f})\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig5f-information-match\n#\n# > The generative process captures the distribution of head-direction information.\n\n# %% tags=claim:fig5f-information-match\ninf_data = H.bits_per_spike(Phi_data)\nprint(f\"data: median {np.median(inf_data):.4f}, range {inf_data.min():.4f} to {inf_data.max():.4f}\")\nfor lab, params in ((\"fitted\", FIT), (\"paper\", PAPER_PARAMS)):\n    for k in range(5):\n        ig = H.bits_per_spike(gen(params, \"fig5f-information-match\", k))\n        print(f\"{lab} params, seed +{1000*k}: median {np.median(ig):.4f} (rel {abs(np.median(ig)-np.median(inf_data))/np.median(inf_data):.3f}), KS {H.ks_distance(inf_data, ig):.3f}\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig2l-recorded-bump-tracks-hd\n#\n# > The overlap order parameter computed directly from the recordings, with the measured tuning\n# > curves and binned spike counts of one mouse, forms a bump that tracks the animal's head\n# > direction.\n#\n# As `closing_the_loop.ipynb`: the session with most head-direction cells (A3707), 10-ms counts\n# from the first head-direction sample of the square epoch, averaged in blocks of 10 bins (100 ms);\n# each cell's counts and curve are divided by the mean of its curve; m is the mean over cells of\n# curve times counts. The angle of the peak of m is the centre of its bin (a standard choice; the\n# bins are floor(hd / (2 pi / 100))). The head direction of a 100-ms bin is the circular mean of\n# its samples; bins with any untracked sample are left out of the comparison.\n\n# %% tags=claim:fig2l-recorded-bump-tracks-hd\nd = sessions[int(np.where(names == \"A3707\")[0][0])]\ns = d[\"sess\"]\nhd_idx = d[\"hd_idx\"]; N_bins = len(hd_idx)\nt_hd = s[\"hd_t\"]; i0 = np.argmin((t_hd - d[\"ti\"]) ** 2)\nhd_raw = s[\"hd\"][i0:i0 + N_bins]\ncounts = np.stack([H.spike_counts(st, d[\"ti\"], d[\"tf\"], N_bins) for st in s[\"spikes\"]], 1)  # (T, 117)\ndef bump_track(tc_full, counts, hd_raw, sel=None):\n    fac = 1.0 / (tc_full.mean(1) + 1e-12)\n    Xc = tc_full * fac[:, None]\n    nb = len(counts) // 10\n    cc = counts[:nb * 10].reshape(nb, 10, -1).mean(1) * fac[None, :]\n    m = Xc.T @ cc.T / len(fac)                       # (100, nb)\n    peak = (m.argmax(0) + 0.5) * 2 * np.pi / 100\n    hh = hd_raw[:nb * 10].reshape(nb, 10)\n    ok = ~np.isnan(hh).any(1)\n    if sel is not None:\n        ok &= sel\n    hm = np.angle(np.exp(1j * hh[ok]).mean(1)) % (2 * np.pi)\n    err = H.circ_diff(peak[ok], hm)\n    return np.median(err), circcorrcoef(peak[ok], hm), ok.sum(), nb, m, err\nmed, rc, nok, nb, m_rec, err = bump_track(d[\"opt\"].mean(1), counts, hd_raw)\nprint(f\"A3707: {counts.shape[1]} cells, {nb} bins of 100 ms, {nok} with tracked head direction\")\nprint(f\"median |peak of m - head direction| = {med:.3f} rad (pi/8 = {np.pi/8:.3f}); circular correlation {rc:.3f} (>= 0.9)\")\nprint(\"error percentiles 25, 50, 75, 90:\", np.percentile(err, [25, 50, 75, 90]).round(3))\n# variant: curves of one partition applied to the other partition's spikes\nmask = H.alternating_mask(N_bins)\nbmask = mask[:nb * 10].reshape(nb, 10)\nfor part, sel in ((0, ~bmask.any(1)), (1, bmask.all(1))):\n    med_v, rc_v, nok_v, _, _, _ = bump_track(d[\"opt\"][:, part], counts, hd_raw, sel)\n    print(f\"variant: curves of partition {part} on the other partition's bins ({nok_v}): median error {med_v:.3f} rad, circular r {rc_v:.3f}\")\n# null: head direction shifted by 60 s against m\nsh = 600\nmed_n = np.median(H.circ_diff(((m_rec.argmax(0) + 0.5) * 2 * np.pi / 100)[:-sh], np.angle(np.exp(1j * hd_raw[:nb * 10].reshape(nb, 10)).mean(1))[sh:]))\nprint(f\"reference: with the head direction shifted by 60 s, median error {med_n:.3f} rad (uniform chance pi/2 = {np.pi/2:.3f})\")\nfig, ax = plt.subplots(figsize=(8, 1.6))\nax.imshow(m_rec[:, :900], aspect=\"auto\", origin=\"lower\", extent=(0, 90, 0, 2 * np.pi), vmax=np.percentile(m_rec, 97.5))\nhh = np.angle(np.exp(1j * hd_raw[:9000].reshape(900, 10)).mean(1)) % (2 * np.pi)\nax.plot(np.arange(900) * 0.1, hh, \"r.\", ms=1); ax.set_xlabel(\"time (s)\"); ax.set_ylabel(\"theta\")\nplt.show()\nprint(\"first 90 s shown; m range\", m_rec.min().round(3), m_rec.max().round(3))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## Summary\n#\n# (written after the run)\n\n# %%\nprint(f\"total time {time.time()-T0:.0f} s; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6:.2f} GB\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/src/nb1.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001/src && python - <<'EOF'
s=open('nb1.py').read()
s=s.replace("""fits = {}
for kk in range(5):
    sd = sd0 + 1000 * kk
    fp = final_pass(L, np.random.default_rng(sd + 1))   # second generator of the claim: seed + 1
    fits[sd] = fp[0]""","""fits = {}
for kk in range(5):
    sd = sd0 + 1000 * kk
    fp = final_pass(L, np.random.default_rng(sd + 1))   # second generator of the claim: seed + 1
    fits[sd] = fp[0]
    if kk == 0:
        fp0 = fp""")
s=s.replace("fp0 = final_pass(L, np.random.default_rng(sd0 + 1))\n","")
open('nb1.py','w').write(s)
EOF
grep -n "fp0" nb1.py; python build.py nb1.py entries/clark-2026/tuning_curves.ipynb && date -u
```

```
480:        fp0 = fp
483:print(pd.DataFrame(fp0[:10], columns=["error_500k", "sigma", "b", "beta", "error_25k"]).round(4).to_string(index=False))
Thu Nov 26 12:10:24 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/clark-2026 && source /tmp/claude-1001/dev/bin/activate && time jupyter nbconvert --to notebook --execute tuning_curves.ipynb --output-dir /tmp/claude-1001/out --ExecutePreprocessor.timeout=3600 2>&1 | tail -30
```

```
[NbConvertApp] Making directory /tmp/claude-1001/out
[NbConvertApp] Converting notebook tuning_curves.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 328351 bytes to /tmp/claude-1001/out/tuning_curves.ipynb

real	17m0.224s
user	13m4.522s
sys	1m49.159s
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001 && cat > show.py <<'EOF'
import json,sys
nb=json.load(open(sys.argv[1]))
for c in nb['cells']:
    if c['cell_type']!='code': continue
    tags=c['metadata'].get('tags',[])
    out=''.join(''.join(o.get('text','')) if 'text' in o else (''.join(o['data'].get('text/plain','')) if 'data' in o and 'image/png' not in o['data'] else ('[image]' if 'data' in o else o.get('ename','')+' '+o.get('evalue',''))) for o in c['outputs'])
    print('=====',tags, ''.join(c['source'])[:60].replace('\n',' '))
    print(out[:int(sys.argv[2]) if len(sys.argv)>2 else 6000])
EOF
source dev/bin/activate; python show.py out/tuning_curves.ipynb 5000 | sed -n 1,400p
```

```
<persisted-output>
Output too large (34.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/c72abc4e-3061-4e0b-9fc5-690e0e537888/tool-results/b4xf8nb9v.txt

Preview (first 2KB):
===== [] import os, time, resource os.environ.setdefault("OMP_NUM_THR
dandiset 000939 version 0.240528.1542

===== [] assets = H.list_assets() order = H.session_order(assets) pri
31 assets at 0.240528.1542
  sub-A1808/sub-A1808_behavior+ecephys+ogen.nwb        1.61 GB
  sub-A1813/sub-A1813_behavior+ecephys+ogen.nwb        1.86 GB
  sub-A1815/sub-A1815_behavior+ecephys+ogen.nwb        1.60 GB
  sub-A1821/sub-A1821_behavior+ecephys+ogen.nwb        1.84 GB
  sub-A1824/sub-A1824_behavior+ecephys+ogen.nwb        1.50 GB
  sub-A3701/sub-A3701_behavior+ecephys.nwb             2.31 GB
  sub-A3702/sub-A3702_behavior+ecephys.nwb             2.01 GB
  sub-A3703/sub-A3703_behavior+ecephys.nwb             1.07 GB
  sub-A3705/sub-A3705_behavior+ecephys.nwb             1.87 GB
  sub-A3706/sub-A3706_behavior+ecephys.nwb             1.82 GB
  sub-A3707/sub-A3707_behavior+ecephys.nwb             1.80 GB
[... 20 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/c72abc4e-3061-4e0b-9fc5-690e0e537888/tool-results/b4xf8nb9v.txt",
 "offset": 38
}
```

```
38	latest 0.261016.2310: 31 assets, sizes 12.7 to 30.2 GB; files shared with the pinned version (same blob): 0
39	example path in latest: sub-A1813/sub-A1813_ses-190408_behavior+ecephys+ogen.nwb
40	
41	===== [] sessions = [] t = time.time() for i, (path, aid, subj, ogen)
42	loaded 31 sessions in 126 s; peak memory 0.84 GB
43	
44	===== ['sanity'] rows = [] for d in sessions:     s = d["sess"]     hd = s["h
45	 session subject  file_ogen  units  hd_units  exc_units  fs_units  hd_and_exc  hd_not_exc                                        epochs  square_s  hd_dt_median_ms  hd_dt_max_in_square_ms  hd_min  hd_max  hd_nan_square  spikes_in_square  unsorted_spike_trains
46	       0   A1808       True    101        29         32        11          29           0     home_cage/wake_square/home_cage/wake_opto     906.5             10.0                    10.0  0.0000  6.2831         0.0014             68638                      0
47	       1   A1813       True     70        30         31        17          30           0     home_cage/wake_square/home_cage/wake_opto    1036.1             10.0                    10.0  0.0001  6.2832         0.0057             82907                      0
48	       2   A1815       True     65        33         35        14          33           0     home_cage/wake_square/home_cage/wake_opto     901.6             10.0                    10.0  0.0000  6.2832         0.0164            112303                      0
49	       3   A1821       True     74        37         38        16          37           0     home_cage/wake_square/home_cage/wake_opto    2701.5             10.0                    10.0  0.0000  6.2832         0.0098            313247                      0
50	       4   A1824       True     70        39         40        16          39           0     home_cage/wake_square/home_cage/wake_opto    1201.1             10.0                    10.0  0.0000  6.2832         0.0043            134008                      0
51	       5   A3701
[... 303 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd /tmp/claude-1001/src && python - <<'EOF'
s=open('nb1.py').read()
old="""sh = 600
med_n = np.median(H.circ_diff(((m_rec.argmax(0) + 0.5) * 2 * np.pi / 100)[:-sh], np.angle(np.exp(1j * hd_raw[:nb * 10].reshape(nb, 10)).mean(1))[sh:]))"""
new="""sh = 600
pk = (m_rec.argmax(0) + 0.5) * 2 * np.pi / 100
hb = np.angle(np.exp(1j * hd_raw[:nb * 10].reshape(nb, 10)).mean(1))
okn = ~np.isnan(hb[sh:])
med_n = np.median(H.circ_diff(pk[:-sh][okn], hb[sh:][okn]))"""
assert old in s; s=s.replace(old,new)
old="""print("minimum error over b and beta at each sigma (shortlist pass):\""""
new="""# variant: the two best points again, with 500,000 samples drawn and transformed in float32, as the
# paper's torch run on a GPU computes them
def err32(params, rng):
    Cs = []
    for chunk in range(5):
        z = H.sample_z(rng, 100000, 51, dtype=np.float32).astype(np.complex64)
        X = np.fft.irfft(z * np.sqrt(H.wrapped_gaussian_ft(params[0])).astype(np.float32)[None, :], axis=1, norm="forward").astype(np.float32)
        P = H.softplus(X - np.float32(params[1]), np.float32(params[2])); P = P / (P.mean(1, keepdims=True) + 1e-30)
        Cs.append(np.mean(np.abs(np.fft.rfft(P, axis=1, norm="forward")[:, :20]) ** 2, 0))
    return np.sqrt(((np.mean(Cs, 0) - Gdata_ft[:20]) ** 2).sum())
best_pt = (fits[sd0][1], fits[sd0][2], fits[sd0][3])
paper_pt = (scale_vals[8], bias_vals[10], beta_vals[8])
for kk in range(5):
    rng32 = np.random.default_rng(sd0 + 2 + 1000 * kk)   # third generator of the claim: seed + 2
    print(f"float32 variant, seed {sd0 + 1000*kk}: error at the best point {err32(best_pt, rng32):.5f}, at the paper's grid point {err32(paper_pt, rng32):.5f}")
print("minimum error over b and beta at each sigma (shortlist pass):\""""
assert old in s; s=s.replace(old,new)
open('nb1.py','w').write(s)
EOF
```

```
Thu Nov 26 12:28:17 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001/repo; python - <<'EOF'
import json
nb=json.load(open('notebooks/spurious_fixed_points.ipynb'))
s=''.join(nb['cells'][3]['source']); i=s.find('Second row'); print(s[i:i+2500])
EOF
```

```
Second row: the DATA-DERIVED (Setting 1) network -------------------
    # The main-text global-stability claim is about this network, but the figure
    # only ever showed the generative one. Same protocol, same noise levels.
    set_global_seed(42)
    Phi_raw = data_driven.load_data_Phi()
    X_dd, Phi_dd = data_driven.prepare_smoothed_normalized_resampled_tuning_curves(
        Phi_raw, N_theta=10000
    )
    J_dd, _ = data_driven.compute_weights(X_dd, Phi_dd, lamda=lamda)
    mu_dd = X_dd.mean(0)
    # full_matrices=False: X_dd is 10000 x N_data, so the full U would be 10000 x 10000.
    U_dd, s_dd, Vt_dd = np.linalg.svd(X_dd - mu_dd, full_matrices=False)
    V_dd = Vt_dd.T
    pcs_dd = (X_dd - mu_dd) @ V_dd

    inits_dd, finals_dd = [], []
    for std_val in std_values:
        x0_dd = np.random.randn(X_dd.shape[1], N_init) * std_val
        x_dd_final, X_dd_dyn, _ = sim.run_sim(
            T=T_total, tau=tau, dt=dt, T_eval=T_eval,
[... 17 more lines not kept]
```

**Agent**

Now the network helpers.

**Agent calls Bash**

```bash
cat >> entries/clark-2026/hdring.py <<'EOF'


# ---------------------------------------------------------------- loading every session at once


def load_all_curves(version=VERSION):
    """Stream every session and compute its tuning curves (as ring/data.py process_all_tcs).

    Returns (sessions, Phi_data, mouse_nums, names): Phi_data holds the partition-averaged
    curves of the head-direction units with a non-zero curve, each divided by its mean
    (data_and_generative_model.ipynb cell 3; data_driven.load_data_Phi).
    """
    order = session_order(list_assets(version))
    sessions = []
    for i, (path, aid, subj, ogen) in enumerate(order):
        s = load_session(aid, version=version)
        plain, opt, sig = tuning_curves_session(s)
        hd_idx, ti, tf, _, _ = epoch_bins(s)
        sessions.append(dict(idx=i, subject=subj, path=path, ogen=ogen, sess=s, plain=plain, opt=opt,
                             sig=sig, hd_idx=hd_idx, ti=ti, tf=tf))
    Phi, mn = [], []
    for d in sessions:
        o = d["opt"].mean(1)
        o = o[~np.all(o == 0, axis=1)]
        Phi.append(o / o.mean(1, keepdims=True))
        mn += [d["idx"]] * len(o)
    names = np.array([d["subject"] for d in sessions])
    return sessions, np.concatenate(Phi), np.array(mn), names


# ---------------------------------------------------------------- the data-derived network
# ring/data_driven.py, ring/regression.py, ring/sim.py


def nonlin(x, beta=2.0):
    """data_driven.nonlin: softplus with beta 2."""
    return softplus(x, beta)


def resample_curves_fft(X, N_new):
    """data_driven.resample_curves_fft (zero-padded Fourier resampling)."""
    N0, Nc = X.shape
    F = np.fft.rfft(X, axis=0)
    G = np.zeros((N_new // 2 + 1, Nc), dtype=complex)
    k = min(F.shape[0], G.shape[0])
    G[:k] = F[:k]
    G *= N_new / N0
    return np.fft.irfft(G, n=N_new, axis=0)


def prepare_network_curves(Phi_data, N_theta=10000, sigma=2, n_sinkhorn=1000):
    """data_driven.prepare_smoothed_normalized_resampled_tuning_curves (Supplementary Note 3,
    section 8.1): inverse softplus (beta 2), circular Gaussian smoothing of 2 bins, softplus,
    Sinkhorn-Knopp normalization of both axes (1,000 sweeps), inverse softplus, Fourier
    resampling to N_theta angles, softplus. Input (N, 100); returns X, Phi of shape (N_theta, N)."""
    P = Phi_data.T.copy()
    X = inv_softplus(P, 2.0)
    Ps = nonlin(gaussian_filter1d(X, sigma=sigma, axis=0, mode="wrap"))
    for _ in range(n_sinkhorn):
        Ps /= Ps.mean(1, keepdims=True)
        Ps /= Ps.mean(0, keepdims=True)
    Xr = resample_curves_fft(inv_softplus(Ps, 2.0), N_theta)
    return Xr, nonlin(Xr)


def compute_J(X, Phi, lamda):
    """regression.compute_J (method opt): primal when N_theta >= N, else dual. Zero diagonal."""
    N_theta, N = Phi.shape
    if N_theta >= N:
        M = (Phi.T @ Phi) / N_theta + np.eye(N) * (N * lamda)
        Mi = np.linalg.inv(M)
        J_uc = ((X.T @ Phi) / N_theta) @ Mi
        return J_uc - Mi * (np.diag(J_uc) / np.diag(Mi))[:, None]
    K = (Phi @ Phi.T) / N + (lamda * N_theta) * np.eye(N_theta)
    Ki = np.linalg.inv(K)
    A = np.eye(N) - (1 / N) * (Phi.T @ Ki @ Phi)
    J_uc = (1 / N) * (X.T @ Ki @ Phi)
    return J_uc - A * (np.diag(J_uc) / np.diag(A))[:, None]


def compute_weights(X, Phi, lamda=1e-8):
    """data_driven.compute_weights: J, and J' for the angular derivative of X (Methods eq. 41)."""
    J = compute_J(X, Phi, lamda)
    dth = 2 * np.pi / X.shape[0]
    dX = np.concatenate(((X[0:1] - X[-1:]) / dth, np.diff(X, axis=0) / dth), axis=0)
    return J, compute_J(dX, Phi, lamda)


def simulate(J, x0, T, tau=0.05, dt=0.001, c=1.0, save_every=None, J_prime=None, omega=None,
             on_save=None, dtype=np.float32):
    """sim.run_sim as data_driven.run_simulation calls it: Euler steps of
    tau dx/dt = -x + J phi(x) + c (1 - mean_i phi(x)) [+ tau omega(t) J' phi(x)],
    phi the softplus of beta 2, in float32 as the paper's torch tensors. x0 (N, B).
    omega, when given, is a function of time returning one value or one per column.
    on_save(t, x) is called at t = 0 and every save_every seconds. Returns the final state.
    Steps are numbered as in run_sim: i = 1 .. int(T/dt) - 1, so the last state is at
    t = T - dt (run_sim's loop is range(1, N_t))."""
    J = J.astype(dtype)
    Jp = J_prime.astype(dtype) if J_prime is not None else None
    x = x0.astype(dtype).copy()
    N_t = int(round(T / dt))
    every = int(round(save_every / dt)) if save_every else None
    if on_save:
        on_save(0.0, x)
    a = dtype(dt / tau)
    with np.errstate(over="ignore", invalid="ignore"):
        for i in range(1, N_t):
            r = nonlin(x)
            drive = J @ r + dtype(c) * (dtype(1.0) - r.mean(0))[None, :]
            if Jp is not None:
                w = np.asarray(omega(i * dt), dtype=dtype)
                drive += dtype(tau) * w * (Jp @ r)
            x += a * (-x + drive)
            if every and i % every == 0 and on_save:
                on_save(i * dt, x)
    return x


def nearest_target(Phi_t, r, Phi_sq=None):
    """Index of the nearest target firing-rate point and the distance / sqrt(N)
    (data_driven.compute_distances_to_ring). Phi_t (N_theta, N), r (N, B)."""
    if Phi_sq is None:
        Phi_sq = (Phi_t ** 2).sum(1)
    d2 = Phi_sq[:, None] + (r ** 2).sum(0)[None, :] - 2 * (Phi_t @ r)
    idx = d2.argmin(0)
    dist = np.sqrt(np.maximum(d2[idx, np.arange(r.shape[1])], 0)) / np.sqrt(Phi_t.shape[1])
    return idx, dist


def circularized_profile(J_sorted):
    """First row of data_driven_attractor.ipynb create_circularized_matrix: mean over i of
    np.roll(J_sorted[i], -i), the mean of the sorted matrix along each circular diagonal."""
    n = J_sorted.shape[0]
    i = np.arange(n)
    return np.array([J_sorted[i, (i + d) % n].mean() for d in range(n)])


def count_states(pos, n, width):
    """Number of distinct final positions on a ring of n sites, for the readings of the claims
    file's merging rule (positions within `width` of each other are one state): single linkage
    (chains of gaps up to width), greedy (a new state when farther than width from the first
    member of the current one), and bins (occupied bins of width `width`)."""
    p = np.sort(np.asarray(pos) % n)
    if len(p) == 0:
        return dict(single=0, greedy=0, bins=0)
    gaps = np.diff(np.r_[p, p[0] + n])
    single = max(int((gaps > width).sum()), 1)
    # greedy, starting after the largest gap so a state does not straddle the start
    s = int(np.argmax(gaps)) + 1
    q = np.r_[p[s:], p[:s] + n]
    greedy, start = 1, q[0]
    for v in q[1:]:
        if v - start > width:
            greedy += 1
            start = v
    bins = len(np.unique(np.floor(p / width).astype(int)))
    return dict(single=single, greedy=greedy, bins=bins)
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001 && source dev/bin/activate && cat > t6.py <<'EOF'
import sys, time; sys.path.insert(0,'entries/clark-2026')
import hdring as H, numpy as np
z=np.load('tcs_dev.npz'); subs=[k[:-4] for k in z.files if k.endswith('_opt')]
P=np.concatenate([z[s+'_opt'].mean(1) for s in subs]); P=P/P.mean(1,keepdims=True); print(P.shape)
t=time.time(); X,Phi=H.prepare_network_curves(P); print('prep',time.time()-t, X.shape)
t=time.time(); J,Jp=H.compute_weights(X,Phi); print('J',time.time()-t)
print('err', np.mean((X-Phi@J.T)**2))
np.save('J.npy',J); np.save('Jp.npy',Jp); np.save('X.npy',X); np.save('Phi.npy',Phi)
x0=X[::100].T.copy()
t=time.time(); xf=H.simulate(J,x0,T=0.2); print('200 steps 100 ICs',time.time()-t)
t=time.time(); xf=H.simulate(J,X[0:1].T.repeat(2,1),T=0.2,J_prime=Jp,omega=lambda t: np.array([0.8,0.1])); print('200 steps 2 cols omega',time.time()-t)
t=time.time(); idx,d=H.nearest_target(Phi.astype(np.float32), H.nonlin(x0.astype(np.float32))); print('dist',time.time()-t, d[:3], idx[:5])
EOF
python t6.py
```

```
(1533, 100)
prep 0.6818900108337402 (10000, 1533)
J 1.246518850326538
err 1.715236380313137e-08
200 steps 100 ICs 0.5200583934783936
200 steps 2 cols omega 0.1686248779296875
dist 0.04942893981933594 [0. 0. 0.] [  0 100 200 300 400]
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/src/nb2.py",
 "content": "# %% [markdown]\n# # Clark, Abbott & Sompolinsky (2026): the data-derived network, on DANDI:000939\n#\n# **Paper.** doi:10.1038/s41593-026-02452-4; claims file `claims/clark-2026.yaml`, written from the\n# version of record and its supplement.\n#\n# **Dataset.** DANDI:000939 at version **0.240528.1542**, the version the paper cites; every file\n# was replaced in later versions (see `tuning_curves.ipynb`, \"Files and versions\").\n#\n# The tuning curves are computed from the streamed NWB files as in `tuning_curves.ipynb`\n# (`hdring.load_all_curves`). The network is built and run as in the paper's\n# `notebooks/data_driven_attractor.ipynb`, `spurious_fixed_points.ipynb` and `ring/data_driven.py`\n# (commit 245726f), in numpy and float32 (the paper's simulations use float32 torch tensors).\n# The lambda and c grid of Supplementary Figs. 8 and 9 is in `network_grid.ipynb`.\n#\n# | claim | tested here |\n# |---|---|\n# | fig2b-sorted-weights-mexican-hat | yes |\n# | fig2ef-data-network-quasicontinuous | yes |\n# | fig2gi-circulant-noise-collapses | yes |\n# | fig2jk-velocity-integration | yes |\n# | figs14-data-spectrum-doublets | yes |\n# | figs11b-data-network-global-stability | yes |\n# | figs8-s9-lambda-and-c | in network_grid.ipynb |\n\n# %%\nimport os, time, resource\nimport numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nfrom scipy.ndimage import gaussian_filter1d\nfrom scipy.interpolate import interp1d\nfrom astropy.stats import circcorrcoef\nimport hdring as H\n\nT0 = time.time()\nprint(\"dandiset\", H.DANDISET, \"version\", H.VERSION)\n\n# %%\nsessions, Phi_data, mouse_nums, names = H.load_all_curves()\nprint(f\"loaded in {time.time()-T0:.0f} s\")\n\n# %% tags=sanity\nprint(\"sessions\", len(sessions), \"| units\", sum(d[\"sess\"][\"n_units\"] for d in sessions),\n      \"| head-direction units\", sum(int(d[\"sess\"][\"is_hd\"].sum()) for d in sessions), \"| curves used\", Phi_data.shape)\nprint(\"curve values: min\", Phi_data.min().round(5), \"max\", Phi_data.max().round(3), \"| row means 1:\", np.allclose(Phi_data.mean(1), 1))\nprint(\"cells per mouse:\", dict(zip(names, np.bincount(mouse_nums))))\n\n# %% [markdown]\n# ## The network\n#\n# Supplementary Note 3, section 8.1, as `prepare_smoothed_normalized_resampled_tuning_curves` and\n# `compute_weights` (lambda 1e-8). The paper's notebook prints the mean squared reconstruction\n# error, `err = 1.7152363818838536e-08`; the same number from these data is printed below.\n\n# %%\nt = time.time()\nX, Phi = H.prepare_network_curves(Phi_data)\nJ, J_prime = H.compute_weights(X, Phi, lamda=1e-8)\nerr = np.mean((X - Phi @ J.T) ** 2)\nN = J.shape[0]\nprint(f\"X, Phi {X.shape}; J {J.shape}; built in {time.time()-t:.0f} s\")\nprint(f\"err = {err!r} (paper's notebook: 1.7152363818838536e-08)\")\nprint(\"diagonal of J is zero:\", np.allclose(np.diag(J), 0), \"| J range\", J.min().round(4), J.max().round(4))\nprint(\"Sinkhorn result: mean over neurons of Phi at each angle, range\", Phi.mean(1).min().round(4), Phi.mean(1).max().round(4))\nPhi32 = Phi.astype(np.float32); Phi_sq = (Phi32 ** 2).sum(1)\n\n# %% [markdown]\n# ## fig2b-sorted-weights-mexican-hat\n#\n# > The optimized data-derived weight matrix looks unstructured in arbitrary order, and ordering\n# > neurons by their tuning-curve centers of mass reveals a noisy approximate Mexican hat\n# > structure.\n\n# %% tags=claim:fig2b-sorted-weights-mexican-hat\ncom_idx = np.floor(H.circular_center_of_mass(Phi.T) * Phi.shape[0] / (2 * np.pi)).astype(int)   # data_driven.circular_com(Phi.T, True)\norder = np.argsort(com_idx)\nJ_srt = J[order][:, order]\nprof = H.circularized_profile(J_srt)\nprof_arb = H.circularized_profile(J)\noffs = (np.arange(N) + N // 2) % N - N // 2\nnear = (np.abs(offs) <= N // 20) & (offs != 0)\nmid = (np.abs(offs) >= N // 8) & (np.abs(offs) <= 3 * N // 8)\nprint(f\"sorted profile: maximum {prof.max():.5f} at offset {offs[prof.argmax()]} (within N/20 = {N//20}: {abs(offs[prof.argmax()]) <= N//20})\")\nprint(f\"mean over offsets {prof.mean():.6f}; minimum over intermediate offsets (N/8 to 3N/8) {prof[mid].min():.6f} at offset {offs[mid][prof[mid].argmin()]}\")\nprint(f\"fraction of intermediate offsets below the mean {np.mean(prof[mid] < prof.mean()):.2f}; below 0 {np.mean(prof[mid] < 0):.2f}\")\nprint(f\"near offsets (1 to N/20) mean {prof[near].mean():.6f} (positive: local excitation)\")\nprint(f\"arbitrary order: profile range {prof_arb[offs != 0].min():.6f} to {prof_arb.max():.6f}, sd {prof_arb[offs != 0].std():.6f}; sorted profile sd {prof[offs != 0].std():.6f}\")\nprint(\"sorted profile at offsets 0, +-10, +-50, +-100, +-200, +-400, +-766:\", {o: round(float(prof[o % N]), 6) for o in [0, 10, -10, 50, -50, 100, -100, 200, -200, 400, -400, 766]})\nrows_sorted_signal = np.mean([np.corrcoef(np.roll(J_srt[i], -i), prof)[0, 1] for i in range(N)])\nprint(f\"mean correlation of each sorted row (aligned) with the profile: {rows_sorted_signal:.3f}; same for arbitrary order: {np.mean([np.corrcoef(np.roll(J[i], -i), prof_arb)[0, 1] for i in range(N)]):.3f}\")\nfig, ax = plt.subplots(1, 3, figsize=(9, 2.6))\nax[0].imshow(J, vmin=-0.005, vmax=0.005, cmap=\"RdBu_r\"); ax[0].set_title(\"J, arbitrary order\")\nax[1].imshow(J_srt, vmin=-0.005, vmax=0.005, cmap=\"RdBu_r\"); ax[1].set_title(\"J, sorted by center of mass\")\nax[2].plot(offs[np.argsort(offs)], prof[np.argsort(offs)]); ax[2].axhline(0, c=\"k\", lw=0.5); ax[2].set_title(\"diagonal profile\"); ax[2].set_xlabel(\"offset (neurons)\")\nplt.show()\nprint(\"colour limits +-0.005; entries of J outside them:\", int((np.abs(J) > 0.005).sum()), \"of\", J.size)\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig2ef-data-network-quasicontinuous\n#\n# > Started at regularly spaced manifold points perturbed by noise, the data-derived network's\n# > trajectories return to the manifold within about 1 s and then persist over 30 s, an\n# > order-of-magnitude separation between convergence and drift timescales.\n#\n# `run_convergence_analysis`: T 30 s, tau 50 ms, step 1 ms, c 1; 100 initial conditions at every\n# 100th target angle with Gaussian noise of standard deviation 3 on the input currents. The\n# distance to the manifold (nearest of the 10,000 target firing-rate points, over sqrt(N)) and the\n# manifold angle (angle of that point) are taken every 100 ms; the paper's notebook saves every\n# 10 ms, a plotting detail that cannot change the result at the times the criterion reads.\n\n# %% tags=claim:fig2ef-data-network-quasicontinuous\ndef run_2ef(sd):\n    rng = np.random.default_rng(sd)\n    x0 = X[::100].T + rng.standard_normal((N, 100)) * 3.0\n    rec_t, rec_d, rec_i = [], [], []\n    def on_save(tt, x):\n        idx, dist = H.nearest_target(Phi32, H.nonlin(x), Phi_sq)\n        rec_t.append(tt); rec_d.append(dist); rec_i.append(idx)\n    xf = H.simulate(J, x0, T=30.0, dt=0.001, c=1.0, save_every=0.1, on_save=on_save)\n    return np.array(rec_t), np.array(rec_d), np.array(rec_i), xf\ndef judge_2ef(tt, dd, ii):\n    k0, k1, k20 = 0, np.argmin(np.abs(tt - 1)), np.argmin(np.abs(tt - 20))\n    m0, m1, m20 = np.median(dd[k0]), np.median(dd[k1]), np.median(dd[k20])\n    ang = 2 * np.pi * ii / X.shape[0]\n    move = H.circ_diff(ang[-1], ang[k1])\n    nbins = len(np.unique(np.floor(ang[-1] / (2 * np.pi / 100)).astype(int)))\n    return dict(med0=m0, med1=m1, med20=m20, a=m1 <= m0 / 10, b=m1 <= 2 * m20,\n                c_frac=np.mean(move < 2 * np.pi / 20), c=np.mean(move < 2 * np.pi / 20) >= 0.9, d_bins=nbins, d=nbins >= 50,\n                t_last=tt[-1], med_last=np.median(dd[-1]), max20=dd[k20].max(), move_med=np.median(move))\nres2ef = {}\nt = time.time()\nfor k in range(5):\n    sd = H.seed(\"fig2ef-data-network-quasicontinuous\") + 1000 * k\n    tt, dd, ii, xf = run_2ef(sd)\n    res2ef[sd] = (tt, dd, ii)\n    j = judge_2ef(tt, dd, ii)\n    print(f\"seed {sd}: median distance at 0 s {j['med0']:.4f}, 1 s {j['med1']:.5f}, 20 s {j['med20']:.5f}, {j['t_last']:.2f} s {j['med_last']:.5f}; \"\n          f\"(a) {j['a']} (b) {j['b']}; angle moved under 2pi/20 between 1 s and the end: {j['c_frac']:.2f} (c) {j['c']}; \"\n          f\"final angles in {j['d_bins']} of 100 bins (d) {j['d']}; median movement {j['move_med']:.4f} rad\")\n    if k == 0:\n        sd0 = sd\n        print(\"   median distance over time (s):\", {round(float(tt[q]), 1): round(float(np.median(dd[q])), 5) for q in [0, 1, 2, 3, 5, 10, 20, 50, 100, 200, len(tt) - 1]})\nprint(f\"time {time.time()-t:.0f} s\")\ntt, dd, ii = res2ef[sd0]\nfig, ax = plt.subplots(1, 2, figsize=(8, 2.4))\nax[0].semilogy(tt, dd, lw=0.3); ax[0].set_xlabel(\"time (s)\"); ax[0].set_ylabel(\"distance / sqrt(N)\")\nax[1].plot(tt, np.unwrap(2 * np.pi * ii / X.shape[0], axis=0), lw=0.3); ax[1].set_xlabel(\"time (s)\"); ax[1].set_ylabel(\"manifold angle\")\nplt.show()\nprint(\"distance range\", dd.min(), dd.max())\nD20_MAX = res2ef[sd0][1][np.argmin(np.abs(tt - 20))].max(); D20_MED = np.median(res2ef[sd0][1][np.argmin(np.abs(tt - 20))])\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig2gi-circulant-noise-collapses\n#\n# > The optimal weights keep a continuum of stable heterogeneous states; their circulant average\n# > gives bumps identical up to translation, while the circulant matrix plus the scrambled\n# > residuals collapses onto a few discrete states within 30 s, so the optimal weights are not a\n# > noisy circulant matrix.\n#\n# As `compute_new_matrices` and `run_all_simulations`: the sorted matrix; its circulant average;\n# the circulant plus the residuals shuffled over all off-diagonal entries (asymmetric version,\n# Fig. 2d,i), and the symmetric version as a variant; both surrogates times 1.275. 100 initial\n# conditions at regularly spaced points of the sorted targets, noise of standard deviation 2.5,\n# c 1, 30 s. The final position is the peak of the final input currents smoothed across sorted\n# neurons with a Gaussian of 2.5 neurons (`plot_simulation_results`, gaussian_filter1d default\n# mode). The claims file merges positions within 31 neurons into one state; it does not say how,\n# so three readings are counted (helper, `count_states`): single linkage, greedy, and occupied\n# bins of 31 neurons. With 100 initial conditions about 15 neurons apart, only the bins reading\n# can reach the 50 states the criterion asks of the optimal matrix.\n\n# %% tags=claim:fig2gi-circulant-noise-collapses\nX_srt = X[:, order]\nJ_circ = np.asarray(H.circulant_projection(J_srt))\ndef scrambled(rng):\n    Jn = J_circ - J_srt\n    iu = np.triu_indices(N, k=1)\n    z = np.concatenate((Jn[iu], Jn.T[iu])); z = rng.permutation(z)\n    A = np.zeros_like(Jn); A[iu] = z[:len(z) // 2]; A.T[iu] = z[len(z) // 2:]\n    S = np.zeros_like(Jn); S[iu] = z[:len(z) // 2]; S.T[iu] = z[:len(z) // 2]\n    return A, S\ndef run_final(M, sd):\n    rng = np.random.default_rng(sd)\n    x0 = X_srt[::int(X_srt.shape[0] / 100)].T + rng.standard_normal((N, 100)) * 2.5\n    return H.simulate(M, x0, T=30.0, dt=0.001, c=1.0)\ndef positions(xf):\n    return gaussian_filter1d(xf.astype(np.float64), sigma=2.5, axis=0).argmax(0)\ndef shift_corr(xf):\n    ref = xf[:, 0]\n    best = []\n    for b in range(1, xf.shape[1]):\n        v = xf[:, b]\n        F = np.fft.ifft(np.fft.fft(ref - ref.mean()) * np.conj(np.fft.fft(v - v.mean()))).real\n        best.append(F.max() / (np.linalg.norm(ref - ref.mean()) * np.linalg.norm(v - v.mean())))\n    return np.array(best)\nW = 31\nsd0 = H.seed(\"fig2gi-circulant-noise-collapses\")\nt = time.time()\nres_gi = {}\nA_noise, S_noise = scrambled(np.random.default_rng(sd0))\nmats = {\"sorted\": J_srt, \"circulant\": 1.275 * J_circ, \"circ_plus_noise\": 1.275 * (J_circ + A_noise), \"circ_plus_noise_sym\": 1.275 * (J_circ + S_noise)}\nfor key, M in mats.items():\n    xf = run_final(M, sd0 + 1)   # second generator of the claim: initial-condition noise\n    pos = positions(xf)\n    res_gi[key] = (xf, pos)\n    cs = H.count_states(pos, N, W)\n    extra = \"\"\n    if key == \"circulant\":\n        sc = shift_corr(xf); extra = f\"; correlation with the best shift of the first state: min {sc.min():.4f}, median {np.median(sc):.4f}\"\n    print(f\"{key}: states single {cs['single']}, greedy {cs['greedy']}, bins {cs['bins']}; distinct peak neurons {len(np.unique(pos))}; peak height range {xf.max(0).min():.2f} to {xf.max(0).max():.2f}{extra}\")\nprint(f\"time {time.time()-t:.0f} s\")\nsc_circ = shift_corr(res_gi[\"circulant\"][0])\nprint(\"circulant states are shifts (all >= 0.99):\", bool((sc_circ >= 0.99).all()))\nprint(\"reference: initial positions, states\", H.count_states(positions(X_srt[::int(X_srt.shape[0] / 100)].T), N, W))\n# seed check on the random parts (shuffle and initial noise) of the circulant plus noise matrix\nfor k in range(1, 5):\n    sd = sd0 + 1000 * k\n    A_k, _ = scrambled(np.random.default_rng(sd))\n    pos = positions(run_final(1.275 * (J_circ + A_k), sd + 1))\n    print(f\"seed {sd}: circ_plus_noise states\", H.count_states(pos, N, W))\nprint(f\"time {time.time()-t:.0f} s\")\nfig, ax = plt.subplots(4, 1, figsize=(7, 5))\nfor a_, (key, (xf, pos)) in zip(ax, res_gi.items()):\n    a_.imshow(gaussian_filter1d(xf, 2.5, axis=0), aspect=\"auto\", vmin=0, vmax=6); a_.set_title(key, fontsize=8)\nplt.tight_layout(); plt.show()\nprint(\"final input currents range over the four runs:\", min(v[0].min() for v in res_gi.values()).round(2), max(v[0].max() for v in res_gi.values()).round(2), \"(colour 0 to 6)\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig2jk-velocity-integration\n#\n# > With the velocity-coupling weights added, the data-derived network's overlap order parameter\n# > tracks a constant angular velocity input of 0.8 rad/s accurately and follows the more complex\n# > trajectory of the mouse's own head-direction behaviour.\n#\n# As `run_analysis` in `data_driven_attractor.ipynb`: started at the target state of angle 0, c 1,\n# tau 50 ms, step 1 ms, 110 s; omega 0.8 rad/s from 20 s (j), or the angular velocity of A3707's\n# square-epoch head direction (`closing_the_loop.ipynb` saves `hd_full[ti_idx:tf_idx]` at 10 ms;\n# `preprocess_hd_data`: gaps interpolated on the circle, unwrapped, 2,000 still samples\n# prepended, Gaussian of 10 samples, differenced), linearly interpolated in time. Saved every 10\n# ms; the target is the cumulative sum of omega at the save times times 10 ms; the first 20 s\n# are dropped. The two inputs run as two columns of one simulation. The angle of the peak of\n# m = Phi r is compared with the target modulo 2 pi.\n\n# %% tags=claim:fig2jk-velocity-integration\nd7 = sessions[int(np.where(names == \"A3707\")[0][0])]\ns7 = d7[\"sess\"]\nti_nom, tf_nom = [(a, b) for tg, a, b in s7[\"epochs\"] if tg == \"wake_square\"][0]\nti_idx = np.argmin((ti_nom - s7[\"hd_t\"]) ** 2); tf_idx = np.argmin((tf_nom - s7[\"hd_t\"]) ** 2)\nhd_ts = s7[\"hd\"][ti_idx:tf_idx].copy()\ndef interpolate_angle_nans(hd):\n    ok = np.where(~np.isnan(hd))[0]\n    if len(ok) in (0, len(hd)): return hd\n    zz = np.exp(1j * hd[ok]); ia = np.arange(len(hd))\n    return np.mod(np.angle(np.interp(ia, ok, zz.real) + 1j * np.interp(ia, ok, zz.imag)), 2 * np.pi)\nhu = np.unwrap(interpolate_angle_nans(hd_ts))\nhu = np.concatenate((np.ones(2000) * hu[0], hu))\nhs = gaussian_filter1d(hu, sigma=10)\nomega_data = np.diff(np.unwrap(hs)) / 0.01\nom_interp = interp1d(np.arange(len(omega_data)) * 0.01, omega_data)\nprint(f\"A3707 square epoch: {len(hd_ts)} samples, {np.isnan(hd_ts).sum()} untracked; omega range {omega_data.min():.2f} to {omega_data.max():.2f} rad/s, median |omega| {np.median(np.abs(omega_data)):.3f}\")\nomega_fn = lambda tt: np.array([0.8 * (tt > 20.0), om_interp(tt)])\npeaks, saves_t = [], []\ndef on_save_jk(tt, x):\n    saves_t.append(tt); peaks.append((Phi32 @ H.nonlin(x)).argmax(0))\nt = time.time()\nH.simulate(J, np.repeat(X[0:1].T, 2, axis=1), T=110.0, dt=0.001, c=1.0, save_every=0.01, J_prime=J_prime, omega=omega_fn, on_save=on_save_jk)\nprint(f\"simulated in {time.time()-t:.0f} s\")\npeaks = np.array(peaks); saves_t = np.array(saves_t)\nang = 2 * np.pi * peaks / X.shape[0]\nskip = int(20 / 0.01)\nfor col, lab in ((0, \"constant 0.8 rad/s\"), (1, \"A3707 behaviour\")):\n    om = np.array([omega_fn(tt)[col] for tt in saves_t])\n    target = np.cumsum(om) * 0.01\n    a_, t_ = ang[skip:, col], np.mod(target[skip:], 2 * np.pi)\n    e = H.circ_diff(a_, t_)\n    rc = circcorrcoef(a_, t_)\n    off = np.angle(np.mean(np.exp(1j * (a_ - t_))))\n    e_off = H.circ_diff(a_ - off, t_)\n    print(f\"{lab}: {len(a_)} samples from 20 to {saves_t[-1]:.2f} s; median |error| {np.median(e):.3f} rad (pi/8 {np.pi/8:.3f}), 90th percentile {np.percentile(e, 90):.3f}; circular r {rc:.3f}; \"\n          f\"mean offset {off:.3f} rad, median |error| after removing it {np.median(e_off):.3f}; total turn of target {np.abs(target[-1]-target[skip]):.1f} rad\")\n    if col == 0:\n        e_j, rc_j = np.median(e), rc\n    else:\n        e_k, rc_k = np.median(e), rc\nprint(\"bump angle at 0, 10 and 20 s (constant input column):\", ang[[0, 1000, 2000], 0].round(3))\nfig, ax = plt.subplots(2, 1, figsize=(8, 3))\nfor col in (0, 1):\n    om = np.array([omega_fn(tt)[col] for tt in saves_t]); target = np.mod(np.cumsum(om) * 0.01, 2 * np.pi)\n    ax[col].plot(saves_t[skip:], ang[skip:, col], \".\", ms=0.5); ax[col].plot(saves_t[skip:], target[skip:], \"r.\", ms=0.3)\nplt.show()\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## figs14-data-spectrum-doublets\n#\n# > In the data-derived weight matrix the leading eigenvalues are approximately real and come in\n# > visible but inexact doublets.\n\n# %% tags=claim:figs14-data-spectrum-doublets\nt = time.time()\nw, V = np.linalg.eig(J)\no = np.argsort(w.real)[::-1]\nw, V = w[o], V[:, o]\nlead = w[:10]\nprint(f\"eigendecomposition in {time.time()-t:.0f} s\")\nuni = np.abs(V[:, :10].sum(0)) / (np.sqrt(N) * np.linalg.norm(V[:, :10], axis=0))\nprint(\"leading 10 eigenvalues:\", [f\"{z.real:.4f}{z.imag:+.4f}i\" for z in lead])\nprint(\"overlap of each eigenvector with the uniform vector:\", uni.round(3))\nreal_ok = np.all(np.abs(lead.imag) < 0.1 * lead.real)\nprint(\"approximately real (|Im| < 0.1 Re for all 10):\", real_ok, \"| max |Im|/Re\", (np.abs(lead.imag) / lead.real).max().round(4))\nu = int(np.argmax(uni))\nrest = np.delete(lead.real, u)\npairs = [(rest[2 * p], rest[2 * p + 1]) for p in range(4)]\nwithin = [a_ - b_ for a_, b_ in pairs]\nto_next = [rest[2 * p + 1] - rest[2 * p + 2] for p in range(4)]\nok_pairs = [wi < tn for wi, tn in zip(within, to_next)]\nprint(f\"set aside eigenvalue {u+1} ({lead[u].real:.4f}), the most uniform eigenvector\")\nprint(\"pairs (real parts):\", [tuple(np.round(p, 4)) for p in pairs])\nprint(\"gap within each pair:\", np.round(within, 4), \"| gap to the next pair:\", np.round(to_next, 4), \"| within < next:\", ok_pairs)\nprint(\"doublets (>= 3 of 4):\", sum(ok_pairs) >= 3, \"| not exact (some pair differs by more than 1e-6 relative):\", any(abs(wi) > 1e-6 * abs(p[0]) for wi, p in zip(within, pairs)))\n# variant: pairs taken without setting any eigenvalue aside\npairs0 = [(lead.real[2 * p], lead.real[2 * p + 1]) for p in range(4)]\nprint(\"variant, no eigenvalue set aside: within\", np.round([a_ - b_ for a_, b_ in pairs0], 4), \"next\", np.round([lead.real[2 * p + 1] - lead.real[2 * p + 2] for p in range(4)], 4))\nprint(\"eigenvalues: real range\", w.real.min().round(3), w.real.max().round(3), \"| imag range\", w.imag.min().round(3), w.imag.max().round(3))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## figs11b-data-network-global-stability\n#\n# > In the data-derived network, initial conditions far from the manifold converge to points on\n# > it, with no spurious attractors, and initial conditions close to the origin converge to one or\n# > a few states on the ring.\n#\n# As the data-derived part of `compute_spurious_analysis` (`spurious_fixed_points.ipynb`): 34\n# initial states i.i.d. Gaussian with zero mean and standard deviation 1, 10, 50, 100 or 1,000 per\n# neuron, softplus network with c 1, step tau/10 = 5 ms, 30 s. The final firing rates are compared\n# with the distance to the manifold reached at 20 s in fig2ef (the largest over its 100\n# trajectories, reading 1, or their median, reading 2). The final manifold angles at standard\n# deviation 1 are counted as states with the merging readings of fig2gi (width 2 pi / 50).\n\n# %% tags=claim:figs11b-data-network-global-stability\ndef run_s11b(sd):\n    rng = np.random.default_rng(sd)\n    out = {}\n    for sv in (1, 10, 50, 100, 1000):\n        x0 = rng.standard_normal((N, 34)) * sv\n        xf = H.simulate(J, x0, T=30.0, dt=0.005, c=1.0)\n        idx, dist = H.nearest_target(Phi32, H.nonlin(xf), Phi_sq)\n        out[sv] = (idx, dist, np.isfinite(xf).all())\n    return out\nt = time.time()\nprint(f\"thresholds from fig2ef at 20 s: largest {D20_MAX:.5f}, median {D20_MED:.5f}\")\nfor k in range(5):\n    sd = H.seed(\"figs11b-data-network-global-stability\") + 1000 * k\n    out = run_s11b(sd)\n    line = []\n    for sv, (idx, dist, fin) in out.items():\n        line.append(f\"sd {sv}: finite {fin}, median dist {np.median(dist):.5f}, max {dist.max():.5f}, within largest {np.mean(dist <= D20_MAX):.2f}, within median {np.mean(dist <= D20_MED):.2f}\")\n    cs = H.count_states(out[1][0], X.shape[0], X.shape[0] / 50)\n    print(f\"seed {sd}: \" + \"; \".join(line) + f\"; sd 1 final angles as states: {cs}\")\n    if k == 0:\n        out0 = out\nprint(f\"time {time.time()-t:.0f} s\")\nprint(\"sd 1 final manifold angles (rad), claim seed:\", np.sort(2 * np.pi * out0[1][0] / X.shape[0]).round(2))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## Summary\n#\n# (written after the run)\n\n# %%\nprint(f\"total time {time.time()-T0:.0f} s; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6:.2f} GB\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/src/nb2.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001/src && python - <<'EOF'
s=open('nb2.py').read()
s=s.replace('sessions, Phi_data, mouse_nums, names = H.load_all_curves()','''import pickle
if os.path.exists("/tmp/claude-1001/sess.pkl"):
    sessions, Phi_data, mouse_nums, names = pickle.load(open("/tmp/claude-1001/sess.pkl","rb"))
else:
    sessions, Phi_data, mouse_nums, names = H.load_all_curves(); pickle.dump((sessions, Phi_data, mouse_nums, names), open("/tmp/claude-1001/sess.pkl","wb"))''')
s=s.replace('T=30.0','T=0.6').replace('T=110.0','T=21.0').replace('range(5)','range(2)').replace('range(1, 5)','range(1, 2)')
open('nb2_test.py','w').write(s)
EOF
python build.py nb2_test.py /tmp/claude-1001/nb2_test.ipynb && cd entries/clark-2026 && source /tmp/claude-1001/dev/bin/activate && cp /tmp/claude-1001/nb2_test.ipynb . && (time jupyter nbconvert --to notebook --execute nb2_test.ipynb --output-dir /tmp/claude-1001/out --ExecutePreprocessor.timeout=3600 2>&1 | tail -5); rm nb2_test.ipynb; python /tmp/claude-1001/show.py /tmp/claude-1001/out/nb2_test.ipynb 3000
```

```
Exit code 1
[32m     33[39m tt, dd, ii = res2ef[sd0]
[32m     34[39m fig, ax = plt.subplots([32m1[39m, [32m2[39m, figsize=([32m8[39m, [32m2.4[39m))

[31mIndexError[39m: index 10 is out of bounds for axis 0 with size 6


real	2m13.801s
user	0m24.710s
sys	0m1.636s
Traceback (most recent call last):
  File "/tmp/claude-1001/show.py", line 2, in <module>
    nb=json.load(open(sys.argv[1]))
                 ~~~~^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/claude-1001/out/nb2_test.ipynb'
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001/src && python - <<'EOF'
for f in ['nb2.py']:
    s=open(f).read()
    s=s.replace("for q in [0, 1, 2, 3, 5, 10, 20, 50, 100, 200, len(tt) - 1]})","for q in [0, 1, 2, 3, 5, 10, 20, 50, 100, 200, len(tt) - 1] if q < len(tt)})")
    open(f,'w').write(s)
s=open('nb2.py').read()
s=s.replace('sessions, Phi_data, mouse_nums, names = H.load_all_curves()','''import pickle
if os.path.exists("/tmp/claude-1001/sess.pkl"):
    sessions, Phi_data, mouse_nums, names = pickle.load(open("/tmp/claude-1001/sess.pkl","rb"))
else:
    sessions, Phi_data, mouse_nums, names = H.load_all_curves(); pickle.dump((sessions, Phi_data, mouse_nums, names), open("/tmp/claude-1001/sess.pkl","wb"))''')
s=s.replace('T=30.0','T=0.6').replace('T=110.0','T=21.0').replace('range(5)','range(2)').replace('range(1, 5)','range(1, 2)')
open('nb2_test.py','w').write(s)
EOF
ls -la /tmp/claude-1001/sess.pkl; python build.py nb2_test.py /tmp/claude-1001/nb2_test.ipynb && cd entries/clark-2026 && source /tmp/claude-1001/dev/bin/activate && cp /tmp/claude-1001/nb2_test.ipynb . && (time jupyter nbconvert --to notebook --execute nb2_test.ipynb --output-dir /tmp/claude-1001/out --ExecutePreprocessor.timeout=3600 2>&1 | tail -5); rm nb2_test.ipynb; python /tmp/claude-1001/show.py /tmp/claude-1001/out/nb2_test.ipynb 3000
```

```
-rw-r--r-- 1 runner runner 591137879 Nov 26 12:33 /tmp/claude-1001/sess.pkl
[NbConvertApp] Converting notebook nb2_test.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 595755 bytes to /tmp/claude-1001/out/nb2_test.ipynb

real	0m47.918s
user	2m55.173s
sys	0m0.892s
===== [] import os, time, resource import numpy as np import pandas a
dandiset 000939 version 0.240528.1542

===== [] import pickle if os.path.exists("/tmp/claude-1001/sess.pkl")
loaded in 0 s

===== ['sanity'] print("sessions", len(sessions), "| units", sum(d["sess"]["n
sessions 31 | units 2691 | head-direction units 1533 | curves used (1533, 100)
curve values: min 0.001 max 13.805 | row means 1: True
cells per mouse: {np.str_('A1808'): np.int64(29), np.str_('A1813'): np.int64(30), np.str_('A1815'): np.int64(33), np.str_('A1821'): np.int64(37), np.str_('A1824'): np.int64(39), np.str_('A3701'): np.int64(71), np.str_('A3702'): np.int64(61), np.str_('A3703'): np.int64(65), np.str_('A3705'): np.int64(66), np.str_('A3706'): np.int64(86), np.str_('A3707'): np.int64(117), np.str_('A3708'): np.int64(44), np.str_('A3709'): np.int64(21), np.str_('A3710'): np.int64(80), np.str_('A3711'): np.int64(90), np.str_('A3712'): np.int64(73), np.str_('A3713'): np.int64(25), np.str_('A3716'): np.int64(93), np.str_('A3717'): np.int64(59), np.str_('A3723'): np.int64(37), np.str_('A3728'): np.int64(27), np.str_('A3730'): np.int64(47), np.str_('A5505'): np.int64(30), np.str_('A5506'): np.int64(24), np.str_('A5507'): np.int64(43), np.str_('A5508'): np.int64(33), np.str_('A5801'): np.int64(26), np.str_('A6211'): np.int64(36), np.str_('A6215'): np.int64(29), np.str_('A6216'): np.int64(44), np.str_('A9701'): np.int64(38)}

===== [] t = time.time() X, Phi = H.prepar
[... 64 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001/repo; grep -n "^def \|^    def " ring/dmft.py; python - <<'EOF'
import json
nb=json.load(open('notebooks/dmft.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='code':
        s=''.join(c['source'])
        if 'velocity' in s.lower() or 'omega' in s or 'hd' in s:
            print(f'--- [{i}]'); print(s[:2500])
EOF
```

```
67:    def __init__(self, N_theta=1000, scale=1.5, g=2.0, lamda=1e-12):
80:    def compute_F_function(self):
113:    def compute_Gamma(self):
120:    def compute_J_and_U(self):
132:    def rfft_sum(self, x):
136:    def J_m_prod(self, m):
141:    def J_deriv_m_hat_prod(self, m_hat):
149:    def compute_Q(self, m, m_hat):
185:    def simulate(self, T, dt, T_eval, omega_func=None, m_init=None,
259:    def compute_bump_jacobian(self, exclude_Q=False):
285:    def find_homogeneous_solution(self, tol=1e-14, max_iter=2000, exclude_Q=False):
326:    def compute_homogeneous_jacobian(self, m0=None, exclude_Q=False, exclude_Q_for_m0=False):
--- [11]
from scipy.interpolate import interp1d


def run_sim():
    """Run simulation and save results"""
    # Simulation parameters
    N_theta = 1000
[... 115 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001/repo; head -5 LICENSE; sed -n 1,260p ring/dmft.py | grep -v '^\s*$' | head -230
```

```
MIT License

Copyright (c) 2026 David G. Clark

Permission is hereby granted, free of charge, to any person obtaining a copy
"""Dynamical mean-field theory (DMFT) for the ring-attractor model.
Single class ``DMFTModel`` constructs the wraparound Gaussian covariance,
derives the analytical recurrent weights J and the deviation operator U,
and simulates the DMFT equations (Euler integration of the order parameter
``m`` and its conjugate ``m_hat``). Used by ``notebooks/dmft.ipynb`` and
``notebooks/weight_matrix_analyses.ipynb``.
Public API on a ``DMFTModel`` instance:
    ``F``, ``J``                                  analytical functions / weights
    ``simulate``                                  Euler integration
    ``compute_bump_jacobian``                     Jacobian at the bump fixed point
    ``compute_homogeneous_jacobian``              Jacobian at the homogeneous solution
Other attributes (``Gamma_*``, ``U``, ``dF_*``, ``compute_*``,
``rfft_sum``, ``J_m_prod`` etc.) are internal implementation detail.
"""
import numpy as np
[... 204 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001/repo; sed -n 259,361p ring/dmft.py | grep -v '^\s*$'; python - <<'EOF'
import json
nb=json.load(open('notebooks/dmft.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='code':
        s=''.join(c['source'])
        if 'jacobian' in s.lower() or 'logspace' in s or 'exclude_Q' in s:
            print(f'--- [{i}]'); print(s[:3000])
EOF
```

```
def compute_bump_jacobian(self, exclude_Q=False):
        """Compute the Jacobian and eigenvalues at the bump solution.
        Parameters
        ----------
        exclude_Q : bool, default False
            If True, omit the Q-fluctuation contribution.
        Returns
        -------
        jac : ndarray, shape (N_theta, N_theta)
            Jacobian matrix at the bump.
        eigenvals : ndarray, shape (N_theta,)
            Eigenvalues sorted by descending real part.
        """
        G1 = self.dF_dC12(self.Gamma_x[0], self.Gamma_x[0], self.Gamma_x)
        G2 = self.dF_dC11(self.Gamma_x[0], self.Gamma_x[0], self.Gamma_x)
        T1 = G1[:, None] * circulant(self.J)
        T2 = G2[:, None] * 2 * self.J[None, :] if not exclude_Q else 0.
        jac = -np.eye(self.N_theta) + (T1 + T2) / self.N_theta
        eigenvals = np.linalg.eigvals(jac)
        eigenvals = eigenvals[np.argsort(eigenvals.real)[::-1]]
[... 246 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001/repo; python - <<'EOF'
import json
nb=json.load(open('notebooks/dmft.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='code':
        s=''.join(c['source'])
        if 'def plot_weights' in s:
            print(f'--- [{i}]'); print(s[:2500])
nb=json.load(open('notebooks/spectra.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='code':
        s=''.join(c['source'])
        print(f'--- [{i}]'); print(s[:1800])
        for o in c.get('outputs',[]):
            if 'text' in o: print('OUT:', ''.join(o['text'])[-300:])
EOF
```

```
--- [5]
"""
Plot weights
"""

def plot_weights(axes):
    scales = [1, 2, 4]
    g_values = [1.5, 3, 5, 10]
    # beta takes the warm 'ember' ramp while Q in the panel below takes
    # 'ocean', keeping the two DMFT parameter families distinct.
    colors = style.sweep_colors(len(g_values), 'ember')
    
    x = np.linspace(-np.pi, np.pi, 1000)
    
    for i, scale in enumerate(scales):
        for j, g in enumerate(g_values):
            model = dmft.DMFTModel(N_theta=1000, g=g, scale=scale)
            axes[i].plot(x, np.roll(model.J, 500), color=colors[j], label=f'$\\beta={g}$')
        
        axes[i].set_title(f'$\\sigma$ = {scale}')
[... 165 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/src/nb3.py",
 "content": "# %% [markdown]\n# # Clark, Abbott & Sompolinsky (2026): the lambda and c grid of the data-derived network\n#\n# **Paper.** doi:10.1038/s41593-026-02452-4; claims file `claims/clark-2026.yaml`. **Dataset.**\n# DANDI:000939 at version **0.240528.1542**, the version the paper cites (see\n# `tuning_curves.ipynb` for why).\n#\n# One claim: `figs8-s9-lambda-and-c` (Supplementary Note 3, section 8.4; Supplementary Figs. 8 and\n# 9), run as `data_driven_reconstruction.ipynb` cell 10: lambda in 1e-12 to 1e-2, c in 0 to 1.5,\n# T 30 s, tau 50 ms, step tau/10 = 5 ms, initial conditions at regularly spaced target angles with\n# noise of standard deviation 3. The paper's notebook runs 100 initial conditions at each of the\n# 42 grid points; here 20 are run at each point (every 500th target angle), to keep the notebook\n# within its time limit, and 100 at the points the criterion reads at c 0 and c 1 (a deviation,\n# recorded in the attempt).\n\n# %%\nimport time, resource\nimport numpy as np\nimport pandas as pd\nimport hdring as H\n\nT0 = time.time()\nsessions, Phi_data, mouse_nums, names = H.load_all_curves()\nX, Phi = H.prepare_network_curves(Phi_data)\nN = X.shape[1]\nprint(f\"loaded and prepared in {time.time()-T0:.0f} s; curves {Phi_data.shape}; X {X.shape}\")\n\n# %% tags=sanity\nprint(\"sessions\", len(sessions), \"| head-direction units\", sum(int(d[\"sess\"][\"is_hd\"].sum()) for d in sessions), \"| curves\", Phi_data.shape[0])\nmu = Phi.mean(0)\nU_, s_, Vt_ = np.linalg.svd(Phi - mu, full_matrices=False)\nV2 = Vt_[:2].T\nring_pc = (Phi - mu) @ V2\nring_norm = np.linalg.norm(Phi, axis=1).mean()\nprint(f\"target manifold: mean firing-rate norm {ring_norm:.3f}; top-2 PC radius range {np.linalg.norm(ring_pc, axis=1).min():.3f} to {np.linalg.norm(ring_pc, axis=1).max():.3f}\")\n\n# %% [markdown]\n# ## figs8-s9-lambda-and-c\n#\n# > In the data-derived network, with no uniform inhibition activity diverges or collapses to the\n# > origin, any c above 0 in the grid prevents the divergence but small c leaves the collapse, a\n# > large regularization destroys the manifold, and the flow error rises at both large and small\n# > lambda, with lambda 1e-8 just above its minimum.\n#\n# Per run: divergence, a non-finite final state or a final firing-rate norm above 10 times the\n# manifold's (and growing over the last 5 s); collapse, a final firing-rate norm below one tenth of\n# the manifold's (claims file). Flow error, the mean squared flow on the target manifold, which with\n# the Sinkhorn-normalized targets (stabilizer zero on the manifold) is the reconstruction error\n# mean((X - Phi J^T)^2) the paper's notebook saves as err_grid.\n\n# %% tags=claim:figs8-s9-lambda-and-c\nlamdas = [1e-12, 1e-10, 1e-8, 1e-6, 1e-4, 1e-2]\ncs = [0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5]\ndef run_point(J, c, n_ic, sd):\n    rng = np.random.default_rng(sd)\n    step = X.shape[0] // n_ic\n    x0 = X[::step][:n_ic].T + rng.standard_normal((N, n_ic)) * 3.0\n    norms = {}\n    def on_save(t, x):\n        norms[round(t, 3)] = np.linalg.norm(H.nonlin(x.astype(np.float64)), axis=0)\n    xf = H.simulate(J, x0, T=30.0, dt=0.005, c=c, save_every=5.0, on_save=on_save)\n    r = H.nonlin(xf.astype(np.float64))\n    fin = np.isfinite(xf).all(0)\n    nr = np.where(fin, np.linalg.norm(np.nan_to_num(r), axis=0), np.inf)\n    ts = sorted(norms)\n    growing = norms[ts[-1]] > 1.01 * norms[ts[-2]]\n    diverge = (~fin) | ((nr > 10 * ring_norm) & growing)\n    collapse = fin & (nr < 0.1 * ring_norm)\n    pc = (np.nan_to_num(r).T - mu) @ V2\n    rad = np.linalg.norm(pc, axis=1)\n    return dict(diverge=int(diverge.sum()), collapse=int(collapse.sum()), n=n_ic, norm_med=float(np.median(nr[fin])) if fin.any() else np.inf,\n                pc_radius_med=float(np.median(rad[fin])) if fin.any() else np.nan)\nsd0 = H.seed(\"figs8-s9-lambda-and-c\")\nrows, errs = [], {}\nt = time.time()\nfor lam in lamdas:\n    J, _ = H.compute_weights(X, Phi, lamda=lam)\n    errs[lam] = float(np.mean((X - Phi @ J.T) ** 2))\n    for c in cs:\n        n_ic = 100 if (c in (0, 1.0) and lam in (1e-12, 1e-8, 1e-4, 1e-2)) else 20\n        o = run_point(J, c, n_ic, sd0)\n        rows.append(dict(lamda=lam, c=c, **o))\n    print(f\"lambda {lam:g} done at {time.time()-t:.0f} s\", flush=True)\ngrid = pd.DataFrame(rows)\nprint(grid.to_string(index=False))\nprint(\"flow error (mean squared flow on the manifold) by lambda:\", {f\"{k:g}\": f\"{v:.3e}\" for k, v in errs.items()})\nprint(f\"manifold firing-rate norm {ring_norm:.3f}; collapse below {0.1*ring_norm:.3f}\")\nc0 = grid[grid.c == 0]\npart1 = bool(((c0.diverge + c0.collapse) > 0).all())\npart1_any = bool(((c0.diverge + c0.collapse) > 0).any())\npart2 = bool((grid[(grid.c > 0) & (grid.lamda <= 1e-4)].diverge == 0).all())\npart3 = bool((grid[(grid.c == 1.0) & (grid.lamda == 1e-2)].collapse > 0).all())\npart4 = errs[1e-8] < errs[1e-2] and errs[1e-8] < errs[1e-12]\nprint(\"c 0 gives divergence or collapse: at every lambda\", part1, \"| at some lambda\", part1_any)\nprint(\"no c above 0 diverges at any lambda up to 1e-4:\", part2)\nprint(\"largest lambda (1e-2) collapses at c 1:\", part3, \"| collapsed:\", grid[(grid.c == 1.0) & (grid.lamda == 1e-2)][[\"collapse\", \"n\"]].values.tolist())\nprint(\"flow error at 1e-8 below that at 1e-2 and at 1e-12:\", part4)\nprint(\"small c leaves the collapse (collapse at c 0.25 at lambda 1e-8):\", grid[(grid.c == 0.25) & (grid.lamda == 1e-8)][[\"collapse\", \"n\"]].values.tolist())\n# seed check: the points the criterion reads, under four more seeds\nfor k in range(1, 5):\n    sd = sd0 + 1000 * k\n    line = []\n    for lam, c in ((1e-8, 0), (1e-8, 1.0), (1e-2, 1.0), (1e-4, 0.25)):\n        J, _ = H.compute_weights(X, Phi, lamda=lam)\n        o = run_point(J, c, 20, sd)\n        line.append(f\"lambda {lam:g} c {c}: diverge {o['diverge']}, collapse {o['collapse']} of {o['n']}\")\n    print(f\"seed {sd}: \" + \"; \".join(line))\nprint(f\"time {time.time()-t:.0f} s\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## Summary\n#\n# (written after the run)\n\n# %%\nprint(f\"total time {time.time()-T0:.0f} s; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6:.2f} GB\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/src/nb3.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001/src && python - <<'EOF'
s=open('nb3.py').read()
s=s.replace('sessions, Phi_data, mouse_nums, names = H.load_all_curves()','''import pickle
sessions, Phi_data, mouse_nums, names = pickle.load(open("/tmp/claude-1001/sess.pkl","rb"))''')
s=s.replace('T=30.0','T=10.0').replace('range(1, 5)','range(1, 2)').replace('lamdas = [1e-12, 1e-10, 1e-8, 1e-6, 1e-4, 1e-2]','lamdas = [1e-12, 1e-8, 1e-4, 1e-2]')
open('nb3_test.py','w').write(s)
EOF
python build.py nb3_test.py /tmp/claude-1001/nb3_test.ipynb && cd entries/clark-2026 && source /tmp/claude-1001/dev/bin/activate && cp /tmp/claude-1001/nb3_test.ipynb . && (time jupyter nbconvert --to notebook --execute nb3_test.ipynb --output-dir /tmp/claude-1001/out --ExecutePreprocessor.timeout=3600 2>&1 | tail -3); rm nb3_test.ipynb; python /tmp/claude-1001/show.py /tmp/claude-1001/out/nb3_test.ipynb 5000
```

```
[NbConvertApp] Converting notebook nb3_test.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 13730 bytes to /tmp/claude-1001/out/nb3_test.ipynb

real	1m36.706s
user	6m15.388s
sys	0m1.279s
===== [] import time, resource import numpy as np import pandas as pd
loaded and prepared in 1 s; curves (1533, 100); X (10000, 1533)

===== ['sanity'] print("sessions", len(sessions), "| head-direction units", s
sessions 31 | head-direction units 1533 | curves 1533
target manifold: mean firing-rate norm 72.456; top-2 PC radius range 34.691 to 40.852

===== ['claim:figs8-s9-lambda-and-c'] lamdas = [1e-12, 1e-8, 1e-4, 1e-2] cs = [0, 0.25, 0.5, 0.75,
lambda 1e-12 done at 20 s
lambda 1e-08 done at 40 s
lambda 0.0001 done at 60 s
lambda 0.01 done at 80 s
       lamda    c  diverge  collapse   n  norm_med  pc_radius_med
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001/repo; python - <<'EOF'
import json
nb=json.load(open('notebooks/data_driven_reconstruction.ipynb'))
for i in [10,12,14]:
    s=''.join(nb['cells'][i]['source'])
    j=s.find('err_grid'); print(i, s[-1500:] if i==10 else s[:2500]); print('----')
EOF
grep -n -i "mean squared flow\|ill-conditioned" paper/*.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd /tmp/claude-1001/src && python - <<'EOF'
s=open('nb3.py').read()
s=s.replace("""    pc = (np.nan_to_num(r).T - mu) @ V2
    rad = np.linalg.norm(pc, axis=1)
    return dict(diverge=int(diverge.sum()), collapse=int(collapse.sum()), n=n_ic,""","""    pc = (np.nan_to_num(r).T - mu) @ V2
    rad = np.linalg.norm(pc, axis=1)
    collapse_pc = fin & (rad < 0.1 * ring_rad)
    return dict(diverge=int(diverge.sum()), collapse=int(collapse.sum()), collapse_pc=int(collapse_pc.sum()), n=n_ic,""")
s=s.replace("""ring_norm = np.linalg.norm(Phi, axis=1).mean()""","""ring_norm = np.linalg.norm(Phi, axis=1).mean()
ring_rad = np.median(np.linalg.norm(ring_pc, axis=1))""")
s=s.replace("""# Per run: divergence, a non-finite final state or a final firing-rate norm above 10 times the
# manifold's (and growing over the last 5 s); collapse, a final firing-rate norm below one tenth of
# the manifold's (claims file).""","""# Per run: divergence, a non-finite final state or a final firing-rate norm above 10 times the
# manifold's (and growing over the last 5 s; a standard choice, as the claims file says only
# "non-finite or growing states"). Collapse to the origin, a final firing-rate norm below one
# tenth of the manifold's (claims file). The claims file reads collapse in the plane of the top
# two principal components of the target manifold, where the origin is the manifold's mean, and
# the firing-rate norm of the homogeneous state is not small; so the norm is read two ways:
# (i) the norm of the firing rates, as the criterion's words, and (ii) the radius of the projection
# on the two principal components, below one tenth of the manifold's median radius there.""")
s=s.replace("""c0 = grid[grid.c == 0]
part1 = bool(((c0.diverge + c0.collapse) > 0).all())
part1_any = bool(((c0.diverge + c0.collapse) > 0).any())
part2 = bool((grid[(grid.c > 0) & (grid.lamda <= 1e-4)].diverge == 0).all())
part3 = bool((grid[(grid.c == 1.0) & (grid.lamda == 1e-2)].collapse > 0).all())""","""print(f"manifold median radius in the PC plane {ring_rad:.3f}; collapse (ii) below {0.1*ring_rad:.3f}")
c0 = grid[grid.c == 0]
part2 = bool((grid[(grid.c > 0) & (grid.lamda <= 1e-4)].diverge == 0).all())
for col, lab in (("collapse", "(i) firing-rate norm"), ("collapse_pc", "(ii) PC-plane radius")):
    p1 = bool(((c0.diverge + c0[col]) > 0).all()); p1a = bool(((c0.diverge + c0[col]) > 0).any())
    p3 = bool((grid[(grid.c == 1.0) & (grid.lamda == 1e-2)][col] > 0).all())
    p5 = grid[(grid.c == 0.25) & (grid.lamda == 1e-8)][[col, "n"]].values.tolist()
    print(f"reading {lab}: c 0 gives divergence or collapse at every lambda {p1}, at some lambda {p1a}; lambda 1e-2 collapses at c 1: {p3}; collapse at c 0.25, lambda 1e-8: {p5}")""")
s=s.replace("""print("c 0 gives divergence or collapse: at every lambda", part1, "| at some lambda", part1_any)
""","")
s=s.replace("""print("largest lambda (1e-2) collapses at c 1:", part3, "| collapsed:", grid[(grid.c == 1.0) & (grid.lamda == 1e-2)][["collapse", "n"]].values.tolist())
""","")
s=s.replace("""print("small c leaves the collapse (collapse at c 0.25 at lambda 1e-8):", grid[(grid.c == 0.25) & (grid.lamda == 1e-8)][["collapse", "n"]].values.tolist())
""","")
s=s.replace("""line.append(f"lambda {lam:g} c {c}: diverge {o['diverge']}, collapse {o['collapse']} of {o['n']}")""","""line.append(f"lambda {lam:g} c {c}: diverge {o['diverge']}, collapse (i) {o['collapse']}, (ii) {o['collapse_pc']} of {o['n']}")""")
s=s.replace("""print("flow error at 1e-8 below that at 1e-2 and at 1e-12:", part4)""","""print("flow error at 1e-8 below that at 1e-2 and at 1e-12:", part4, "| lambda of the minimum flow error:", min(errs, key=errs.get))""")
open('nb3.py','w').write(s)
EOF
grep -n "part1\|part3" nb3.py
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
date -u; cd /tmp/claude-1001/repo && python - <<'EOF'
s=open('ring/dmft.py').read()
s=s.replace('''"""Dynamical mean-field theory (DMFT) for the ring-attractor model.''','''"""Copy of ring/dmft.py from github.com/davidclark1/symmetries-continuous-attractors at commit
245726fa78457e10cdcf17e6be36fba1dec98061 (MIT License, Copyright (c) 2026 David G. Clark),
used by the attempt clark-2026 for the mean-field claims. The only changes: the imports of
ring.fn and ring.tc (which import torch) are replaced by their numpy functions, defined below,
and the progress bar is off by default.

Dynamical mean-field theory (DMFT) for the ring-attractor model.''')
s=s.replace('''from tqdm import tqdm
from scipy.linalg import circulant
from . import fn, tc
''','''from scipy.linalg import circulant
from scipy.special import erf


class fn:
    """ring/fn.py, unity_erf (numpy branch)."""
    @staticmethod
    def unity_erf(x):
        return erf(np.sqrt(np.pi) * x / 2.)


class tc:
    """ring/tc.py, wrapped_gaussian_cov (numpy branch)."""
    @staticmethod
    def wrapped_gaussian_cov(eq_var, scale, N_theta, backend='numpy'):
        N_freq = N_theta // 2 + 1
        freq_range = np.arange(N_freq)
        Gamma_ft = (eq_var / np.sqrt(2 * np.pi) / scale) * np.exp(-freq_range**2 / (2 * scale**2))
        Gamma = np.fft.irfft(Gamma_ft, norm='forward')
        return Gamma, Gamma_ft
''')
s=s.replace("use_tqdm=True, tau=1., exclude_Q=False):","use_tqdm=False, tau=1., exclude_Q=False):")
s=s.replace("iterator = tqdm(range(1, N_t)) if use_tqdm else range(1, N_t)","iterator = range(1, N_t)")
assert 'tqdm(' not in s
open('entries/clark-2026/ring_dmft.py','w').write(s)
EOF
cd /tmp/claude-1001 && source dev/bin/activate && cd entries/clark-2026 && python -c "
import ring_dmft as D, numpy as np, time
t=time.time(); m=D.DMFTModel(N_theta=500, scale=1.4211, g=2.7659); _,wb=m.compute_bump_jacobian(); _,wh=m.compute_homogeneous_jacobian(); print(time.time()-t, wb[:3], wh[:3])
t=time.time(); m=D.DMFTModel(N_theta=1000, scale=1.4211, g=2.7659); r=m.simulate(T=1.0, dt=0.001, T_eval=0.01, tau=0.05, omega_func=lambda t: 0.8*np.ones_like(t)); print('1s sim', time.time()-t)
"
```

```
Thu Nov 26 12:38:40 UTC 2026
0.04215884208679199 [-1.35788644e-11+0.j -1.61136390e-01+0.j -1.81981889e-01+0.j] [0.55790081+0.j 0.55790081+0.j 0.4173324 +0.j]
1s sim 0.11405253410339355
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/src/nb4.py",
 "content": "# %% [markdown]\n# # Clark, Abbott & Sompolinsky (2026): the mean-field theory and the large-N spectra\n#\n# **Paper.** doi:10.1038/s41593-026-02452-4; claims file `claims/clark-2026.yaml`. **Dataset.**\n# DANDI:000939 at version **0.240528.1542**, the version the paper cites (see\n# `tuning_curves.ipynb`).\n#\n# These claims are on the paper's theory and simulations (`data: elsewhere`, the paper's code at\n# commit 245726f), except `fig7c-dmft-integrates-behavior`, which drives the mean-field equations\n# with the head direction of mouse A3707 from the dataset. The mean-field code is a copy of the\n# paper's `ring/dmft.py` (`ring_dmft.py` in this entry, MIT licence, imports of torch removed).\n#\n# | claim | data | tested here |\n# |---|---|---|\n# | fig7-dmft-mexican-hat-and-stability | elsewhere | yes |\n# | fig7de-dmft-timescales | elsewhere | yes |\n# | fig7c-dmft-integrates-behavior | dataset | yes |\n# | fig6cd-eigenvalues-real-degenerate | elsewhere | yes |\n# | fig6fg-disordered-eigenvectors | elsewhere | yes |\n\n# %%\nimport time, resource\nimport numpy as np\nimport pandas as pd\nimport scipy.linalg\nfrom scipy.special import erf\nfrom scipy.ndimage import gaussian_filter1d\nfrom scipy.interpolate import interp1d\nfrom astropy.stats import circcorrcoef\nimport hdring as H\nimport ring_dmft as D\n\nT0 = time.time()\n\n# %% [markdown]\n# ## Data: the head direction of A3707\n#\n# The session with most head-direction cells (`closing_the_loop.ipynb` picks it by count; A3707,\n# 117 cells). Its square-epoch head direction is prepared as in `data_driven.preprocess_hd_data`.\n\n# %% tags=sanity\norder = H.session_order(H.list_assets())\naid = [o[1] for o in order if o[2] == \"A3707\"][0]\ns7 = H.load_session(aid)\nprint(\"A3707: units\", s7[\"n_units\"], \"| head-direction units\", int(s7[\"is_hd\"].sum()), \"| epochs\", s7[\"epochs\"])\nti_nom, tf_nom = [(a, b) for tg, a, b in s7[\"epochs\"] if tg == \"wake_square\"][0]\nti_idx = np.argmin((ti_nom - s7[\"hd_t\"]) ** 2); tf_idx = np.argmin((tf_nom - s7[\"hd_t\"]) ** 2)\nhd_ts = s7[\"hd\"][ti_idx:tf_idx].copy()\nprint(f\"square epoch {s7['hd_t'][ti_idx]:.2f} to {s7['hd_t'][tf_idx]:.2f} s; {len(hd_ts)} samples at median step {np.median(np.diff(s7['hd_t'][ti_idx:tf_idx]))*1e3:.2f} ms; \"\n      f\"untracked {np.isnan(hd_ts).sum()}; range {np.nanmin(hd_ts):.4f} to {np.nanmax(hd_ts):.4f} rad ({s7['hd_unit']})\")\ndef interpolate_angle_nans(hd):\n    ok = np.where(~np.isnan(hd))[0]\n    if len(ok) in (0, len(hd)): return hd\n    zz = np.exp(1j * hd[ok]); ia = np.arange(len(hd))\n    return np.mod(np.angle(np.interp(ia, ok, zz.real) + 1j * np.interp(ia, ok, zz.imag)), 2 * np.pi)\nhu = np.unwrap(interpolate_angle_nans(hd_ts))\nhu = np.concatenate((np.ones(2000) * hu[0], hu))\nomega_data = np.diff(np.unwrap(gaussian_filter1d(hu, sigma=10))) / 0.01\nprint(f\"omega: {len(omega_data)} samples, range {omega_data.min():.2f} to {omega_data.max():.2f} rad/s, zero for the first 20 s: {np.allclose(omega_data[:1990], 0, atol=1e-3)}\")\n\n# %% [markdown]\n# ## fig7-dmft-mexican-hat-and-stability\n#\n# > In the mean-field theory the effective interactions are circulant with a Mexican hat profile\n# > set by sigma and beta; at a bump state all Jacobian eigenvalues have negative real parts except\n# > the symmetry-induced zero, the uniform state has a real positive eigenvalue for all sigma and\n# > beta (a Turing instability), and fixing Q destabilizes the bump.\n#\n# As `dmft.ipynb`: the profiles of Fig. 7a (`plot_weights`, N_theta 1,000, sigma 1, 2, 4, beta\n# 1.5, 3, 5, 10) and the stability grid (`run_analysis`, beta logspace(-2, 2, 40), sigma\n# logspace(0, 2, 20), N_theta 500, five eigenvalues kept), and the spectrum with Q fixed\n# (`plot_exclude_Q_spectra`, N_theta 500, sigma 1.4211, beta 2.7659).\n\n# %% tags=claim:fig7-dmft-mexican-hat-and-stability\nprof_ok = []\nfor sc in (1, 2, 4):\n    for g in (1.5, 3, 5, 10):\n        Jp = D.DMFTModel(N_theta=1000, g=g, scale=sc).J\n        prof_ok.append(dict(sigma=sc, beta=g, J0=Jp[0], Jmin=Jp.min(), argmin_rad=2 * np.pi * min(Jp.argmin(), 1000 - Jp.argmin()) / 1000, mexican=Jp[0] > 0 and Jp.min() < 0))\nprint(pd.DataFrame(prof_ok).round(4).to_string(index=False))\nt = time.time()\ng_vals = np.logspace(-2, 2, 40); s_vals = np.logspace(0, 2, 20)\nbump = np.zeros((40, 20, 5), complex); homo = np.zeros((40, 20, 5), complex)\nfor i, g in enumerate(g_vals):\n    for j, sc in enumerate(s_vals):\n        mdl = D.DMFTModel(N_theta=500, scale=sc, g=g)\n        bump[i, j] = mdl.compute_bump_jacobian()[1][:5]\n        homo[i, j] = mdl.compute_homogeneous_jacobian()[1][:5]\nprint(f\"stability grid in {time.time()-t:.0f} s\")\nprint(f\"bump eigenvalue 1 (symmetry zero): max |Re| {np.abs(bump[..., 0].real).max():.2e}\")\nprint(f\"bump eigenvalue 2: Re max {bump[..., 1].real.max():.4e}, negative at every grid point: {bool((bump[..., 1].real < 0).all())}\")\nprint(f\"uniform state eigenvalue 1: Re min {homo[..., 0].real.min():.4e}, positive at every point: {bool((homo[..., 0].real > 0).all())}; max |Im| {np.abs(homo[..., 0].imag).max():.2e}\")\nmq = D.DMFTModel(N_theta=500, scale=1.4211, g=2.7659)\nw_full = mq.compute_bump_jacobian()[1]; w_noQ = mq.compute_bump_jacobian(exclude_Q=True)[1]\nprint(\"bump spectrum (leading 5 real parts):\", w_full.real[:5].round(4), \"| with Q fixed:\", w_noQ.real[:5].round(4), \"| positive with Q fixed:\", bool(w_noQ.real[0] > 1e-6))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig7de-dmft-timescales\n#\n# > In the mean-field theory, the convergence time to the bump manifold (-tau over the bump\n# > Jacobian's second eigenvalue) and the divergence time from the uniform state (tau over its\n# > leading eigenvalue) are both a few tau for beta of about 1 and above, decreasing with beta and\n# > insensitive to sigma.\n\n# %% tags=claim:fig7de-dmft-timescales\nt_bump = -1 / bump[..., 1].real      # in units of tau\nt_homo = 1 / homo[..., 0].real\nsel = g_vals >= 1\nsel10 = sel & (g_vals <= 10)\nprint(\"beta values with beta >= 1:\", g_vals[sel].round(3))\nfor lab, tt in ((\"convergence (bump)\", t_bump), (\"divergence (uniform)\", t_homo)):\n    few = bool(((tt[sel10] >= 0.5) & (tt[sel10] <= 10)).all())\n    incs = [int((np.diff(tt[sel, j]) > 0).sum()) for j in range(20)]\n    dec = all(n <= 1 for n in incs)\n    ratio = tt[sel].max(1) / tt[sel].min(1)\n    print(f\"{lab}: t*/tau over beta 1 to 10 from {tt[sel10].min():.3f} to {tt[sel10].max():.3f}, few tau (0.5 to 10): {few}; \"\n          f\"increases along beta per sigma {incs}, decreasing: {dec}; max/min over sigma per beta {ratio.round(3)}, \"\n          f\"max {ratio.max():.3f}: (a) <= 2 {bool(ratio.max() <= 2)}, (b) <= 3 {bool(ratio.max() <= 3)}\")\n    print(f\"   t*/tau at beta 1.0 to 100 for sigma 1 and 100:\", tt[sel][:, 0].round(3), tt[sel][:, -1].round(3))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig7c-dmft-integrates-behavior\n#\n# > Under angular velocity input from mouse behaviour, the mean-field traveling-bump solutions\n# > track head direction by integrating angular velocity, matching the network simulations and the\n# > recordings.\n#\n# As `dmft.ipynb` `run_sim`: N_theta 1,000, sigma 1.4211, beta 2.7659, T 110 s, step 1 ms, saved\n# every 10 ms, tau 50 ms, omega of A3707 interpolated linearly; the target is the cumulative sum\n# of omega at the save times times 10 ms; the first 20 s are dropped. The angle of the peak of m is\n# compared with the target, as in fig2jk-velocity-integration.\n\n# %% tags=claim:fig7c-dmft-integrates-behavior\nom_interp = interp1d(np.arange(len(omega_data)) * 0.01, omega_data)\nt = time.time()\nmdl = D.DMFTModel(N_theta=1000, scale=1.4211, g=2.7659)\ntt, m, m_hat, g_dyn = mdl.simulate(T=110, dt=0.001, T_eval=0.01, omega_func=om_interp, tau=0.05)\nprint(f\"simulated in {time.time()-t:.0f} s; m {m.shape}, range {m.min():.3f} to {m.max():.3f}\")\ntarget = np.mod(np.cumsum(om_interp(tt)) * (tt[1] - tt[0]), 2 * np.pi)\nkeep = tt >= 20\nang = 2 * np.pi * m.argmax(1) / 1000\ne = H.circ_diff(ang[keep], target[keep])\nrc = circcorrcoef(ang[keep], target[keep])\nprint(f\"{keep.sum()} samples from 20 s; median |peak angle - target| {np.median(e):.4f} rad (pi/8 {np.pi/8:.3f}); 90th percentile {np.percentile(e, 90):.4f}; circular r {rc:.4f}\")\nprint(f\"bump contrast (max - min of m) at 20 s and at the end: {np.ptp(m[keep][0]):.3f}, {np.ptp(m[-1]):.3f}\")\n# reference: the target shifted by 30 s\nsh = 3000\nprint(f\"reference, target shifted by 30 s: median error {np.median(H.circ_diff(ang[keep][:-sh], target[keep][sh:])):.3f} rad\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig6cd-eigenvalues-real-degenerate\n#\n# > For tuning curves from the generative process at large N, the optimal weight matrix has real,\n# > doubly degenerate eigenvalues, the ratios of the input-current to the firing-rate Fourier\n# > coefficients scaled by the average activation slope, and they match numerical\n# > diagonalization at N = 2,500, with the ninth eigenvalue the unpaired constant mode.\n#\n# As `spectra.ipynb` cells 3 to 7: the mean-field eigenvalues alpha Gamma_x_n / (Gamma_phi_n +\n# 1e-12), from 50,000 idealized curves (error-function activation, sigma 1.4211, beta 2.7659) on\n# 2,500 angles (accumulated over chunks of 5,000 to bound memory), with alpha the mean activation\n# slope; and the finite network, N 2,500 idealized curves on 500 angles, J by `compute_weights`\n# with lambda 1e-8, eigenvalues by np.linalg.eigvals. The draws come from the claim's seed (the\n# notebook uses numpy seeds 42 and 45).\n\n# %% tags=claim:fig6cd-eigenvalues-real-degenerate\nBETA, SCALE = 2.7659, 1.4211\ndef unity_erf(x): return erf(np.sqrt(np.pi) * x / 2.0)\ndef gen_idealized(n, n_theta, rng):\n    \"\"\"ring/tc.py gen_tuning_curves_idealized with sample_tcs, from a Generator.\"\"\"\n    gft = H.wrapped_gaussian_ft(SCALE, n_theta)\n    nf = len(gft)\n    Z = (rng.standard_normal((nf, n)) + 1j * rng.standard_normal((nf, n))) / np.sqrt(2.0)\n    Z[0] = Z[0].real * np.sqrt(2.0)\n    Xg = np.fft.irfft(Z * np.sqrt(gft)[:, None], axis=0, norm=\"forward\")\n    return Xg, 1 + unity_erf(BETA * Xg)\ndef theory_eigs(rng, n_samples=50000, n_theta=2500, chunk=5000):\n    gx = np.zeros(n_theta); gp = np.zeros(n_theta); slope = 0.0\n    for c0 in range(0, n_samples, chunk):\n        Xg, Pg = gen_idealized(chunk, n_theta, rng)\n        gx += (np.abs(np.fft.fft(Xg, axis=0, norm=\"forward\")) ** 2).sum(1)\n        gp += (np.abs(np.fft.fft(Pg, axis=0, norm=\"forward\")) ** 2).sum(1)\n        slope += (BETA * np.exp(-np.pi * (BETA * Xg) ** 2 / 4)).sum()\n    gx /= n_samples; gp /= n_samples\n    alpha = slope / (n_samples * n_theta)\n    return alpha * gx / (gp + 1e-12), alpha\ndef finite_J(rng, n=2500, n_theta=500):\n    Xg, Pg = gen_idealized(n, n_theta, rng)\n    Jg = H.compute_J(Xg, Pg, 1e-8)\n    o = np.argsort(H.circular_center_of_mass(Pg.T))\n    return Jg[o][:, o], Xg[:, o], Pg[:, o]\nsd0 = H.seed(\"fig6cd-eigenvalues-real-degenerate\")\nt = time.time()\nlam_th, alpha = theory_eigs(np.random.default_rng(sd0 + 1))\nth_sorted = np.sort(lam_th)[::-1]\nn_idx = np.arange(2500)\nprint(f\"alpha {alpha:.4f}; theory eigenvalues computed in {time.time()-t:.0f} s\")\nprint(\"theory, leading 11:\", th_sorted[:11].round(4), \"| Fourier index of each:\", [int(min(k, 2500 - k)) for k in np.argsort(lam_th)[::-1][:11]])\ndef judge_6cd(J6):\n    w6 = np.linalg.eigvals(J6)\n    w6 = w6[np.argsort(w6.real)[::-1]]\n    lead = w6[:11]\n    rel = np.abs(lead.real - th_sorted[:11]) / np.abs(th_sorted[:11])\n    imag_ok = bool(np.all(np.abs(lead.imag) < 0.1 * np.abs(lead.real)))\n    return w6, lead, rel, imag_ok\nfor k in range(5):\n    sd = sd0 + 1000 * k\n    t = time.time()\n    J6, X6, P6 = finite_J(np.random.default_rng(sd))\n    w6, lead, rel, imag_ok = judge_6cd(J6)\n    within8 = [lead.real[2 * p] - lead.real[2 * p + 1] for p in range(4)]\n    between8 = [lead.real[2 * p + 1] - lead.real[2 * p + 2] for p in range(4)]\n    print(f\"seed {sd} ({time.time()-t:.0f} s): leading 11 real parts {lead.real.round(4)}; relative difference from theory max over the 11 {rel.max():.4f} \"\n          f\"(within 10%: {bool((rel <= 0.1).all())}); |Im| < 0.1 Re: {imag_ok}; gaps within pairs 1-4 {np.round(within8, 4)}, to the next {np.round(between8, 4)}; \"\n          f\"ninth eigenvalue {lead.real[8]:.4f}, tenth {lead.real[9]:.4f}\")\n    if k == 0:\n        J6_0, X6_0, P6_0, w6_0 = J6, X6, P6, w6\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig6fg-disordered-eigenvectors\n#\n# > Spectral embedding finds rings in a circulant matrix with weak noise, whose eigenvectors are\n# > Fourier modes, but not in the model, whose eigenvector point clouds are structureless, while\n# > eigenvalue degeneracy is present in every case, so degeneracy is proposed as a robust signature\n# > of ring-attractor structure.\n#\n# As `spectra.ipynb` cell 7: the model matrix of fig6cd (neurons sorted by center of mass) and\n# the circulant matrix alpha circulant(J_dmft) / N plus Gaussian noise of standard deviation\n# 0.1 / sqrt(N). The leading singular vectors of each (eigenvectors of J J^T) are grouped into\n# pairs after setting aside the one closest to uniform; each neuron's point in a pair's plane has\n# a radius, and the coefficient of variation of the radii decides ring (below 0.2) or\n# structureless (above 0.4). The doublets are tested on the eigenvalues, as in fig6cd.\n\n# %% tags=claim:fig6fg-disordered-eigenvectors\nJ_dmft = np.fft.ifft(lam_th / alpha, norm=\"forward\").real    # spectra.ipynb, compute_eff_weights: J = ifft(J_ft)\ndef pair_cvs(M, n_pairs=2):\n    U, sv, Vt = np.linalg.svd(M)\n    uni = np.abs(U[:, :2 * n_pairs + 1].sum(0)) / np.sqrt(M.shape[0])\n    drop = int(np.argmax(uni))\n    keep = [i for i in range(2 * n_pairs + 1) if i != drop][:2 * n_pairs]\n    cvs = []\n    for p in range(n_pairs):\n        a_, b_ = U[:, keep[2 * p]], U[:, keep[2 * p + 1]]\n        rad = np.hypot(a_, b_)\n        cvs.append(rad.std() / rad.mean())\n    return np.array(cvs), sv[:2 * n_pairs + 1], drop\ndef doublets(M):\n    w = np.linalg.eigvals(M); w = np.sort(w.real)[::-1][:11]\n    # set aside the unpaired eigenvalue: the one farthest from both neighbours among the leading 9\n    d = np.array([min(abs(w[i] - w[i - 1]) if i > 0 else np.inf, abs(w[i] - w[i + 1])) for i in range(9)])\n    u = int(np.argmax(d)); r = np.delete(w, u)\n    within = [r[2 * p] - r[2 * p + 1] for p in range(4)]; nxt = [r[2 * p + 1] - r[2 * p + 2] for p in range(4)]\n    return sum(a_ < b_ for a_, b_ in zip(within, nxt)), u\nfor k in range(5):\n    sd = sd0 + 1000 * k\n    rng = np.random.default_rng(sd + 2)   # third generator of the claim: the circulant's noise\n    Jm = J6_0 if k == 0 else finite_J(np.random.default_rng(sd))[0]\n    Jc = alpha * scipy.linalg.circulant(J_dmft) / 2500 + rng.standard_normal((2500, 2500)) * 0.1 / np.sqrt(2500)\n    cv_m, sv_m, drop_m = pair_cvs(Jm); cv_c, sv_c, drop_c = pair_cvs(Jc)\n    dm, um = doublets(Jm); dc, uc = doublets(Jc)\n    print(f\"seed {sd}: model pair CVs {cv_m.round(3)} (set aside singular vector {drop_m+1}); circulant+noise pair CVs {cv_c.round(3)} (set aside {drop_c+1}); \"\n          f\"doublets in 4 leading pairs: model {dm}/4 (unpaired at {um+1}), circulant {dc}/4 (unpaired at {uc+1})\")\n    print(f\"   singular values model {sv_m.round(3)}, circulant {sv_c.round(3)}\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## Summary\n#\n# (written after the run)\n\n# %%\nprint(f\"total time {time.time()-T0:.0f} s; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6:.2f} GB\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/src/nb4.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001/src && python - <<'EOF'
s=open('nb4.py').read()
s=s.replace("""    if k == 0:
        J6_0, X6_0, P6_0, w6_0 = J6, X6, P6, w6""","""    Js6[k] = J6""")
s=s.replace("""for k in range(5):
    sd = sd0 + 1000 * k
    t = time.time()
    J6, X6, P6 = finite_J""","""Js6 = {}
for k in range(5):
    sd = sd0 + 1000 * k
    t = time.time()
    J6, X6, P6 = finite_J""")
s=s.replace("Jm = J6_0 if k == 0 else finite_J(np.random.default_rng(sd))[0]","Jm = Js6[k]")
open('nb4.py','w').write(s)
EOF
python build.py nb4.py entries/clark-2026/theory.ipynb && cd entries/clark-2026 && source /tmp/claude-1001/dev/bin/activate && (time jupyter nbconvert --to notebook --execute theory.ipynb --output-dir /tmp/claude-1001/out --ExecutePreprocessor.timeout=3600 2>&1 | tail -3); python /tmp/claude-1001/show.py /tmp/claude-1001/out/theory.ipynb 5000
```

```
[NbConvertApp] Converting notebook theory.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 31241 bytes to /tmp/claude-1001/out/theory.ipynb

real	2m35.041s
user	8m33.685s
sys	0m4.227s
===== [] import time, resource import numpy as np import pandas as pd

===== ['sanity'] order = H.session_order(H.list_assets()) aid = [o[1] for o i
A3707: units 185 | head-direction units 117 | epochs [('home_cage', np.float64(5e-05), np.float64(3302.1)), ('wake_square', np.float64(3302.1), np.float64(5109.84)), ('home_cage', np.float64(5109.84), np.float64(9902.88)), ('wake_triangle', np.float64(9902.88), np.float64(11142.43))]
square epoch 3304.24 to 5107.28 s; 180304 samples at median step 10.00 ms; untracked 226; range 0.0000 to 6.2832 rad (radians)
omega: 182303 samples, range -5.86 to 6.48 rad/s, zero for the first 20 s: False

===== ['claim:fig7-dmft-mexican-hat-and-stability'] prof_ok = [] for sc in (1, 2, 4):     for g in (1.5, 3, 5, 1
 sigma  beta      J0    Jmin  argmin_rad  mexican
     1   1.5  8.5376 -2.5906      1.5268     True
     1   3.0  5.9153 -1.7814      1.7027     True
     1   5.0  5.2516 -1.5862      1.7719     True
     1  10.0  4.9056 -1.4874      1.8158     True
[... 64 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001/src && python - <<'EOF'
s=open('nb4.py').read()
old=s[s.find("def pair_cvs(M, n_pairs=2):"):s.find("def doublets(M):")]
new='''def pair_cvs(M, n_pairs=2):
    U, sv, Vt = np.linalg.svd(M)
    k = 2 * n_pairs + 1
    uni = np.abs(U[:, :k].sum(0)) / np.sqrt(M.shape[0])     # overlap with the uniform unit vector
    keep = [i for i in range(k) if uni[i] < 0.5][:2 * n_pairs]   # consecutive pairs, skipping a constant mode
    cvs = []
    for p in range(n_pairs):
        a_, b_ = U[:, keep[2 * p]], U[:, keep[2 * p + 1]]
        rad = np.hypot(a_, b_)
        cvs.append(rad.std() / rad.mean())
    return np.array(cvs), sv[:k], [i for i in range(k) if i not in keep]
'''
s=s.replace(old,new)
s=s.replace("""pairs after setting aside the one closest to uniform;""","""consecutive pairs, skipping a singular vector whose overlap with the uniform vector exceeds 0.5
(the constant mode; none of the leading five does here);""")
s=s.replace("(set aside singular vector {drop_m+1})","(skipped {[i+1 for i in drop_m]})").replace("(set aside {drop_c+1})","(skipped {[i+1 for i in drop_c]})")
s=s.replace("""print(f"bump eigenvalue 1 (symmetry zero): max |Re| {np.abs(bump[..., 0].real).max():.2e}")""","""print(f"bump eigenvalue 1 (symmetry zero): max |Re| {np.abs(bump[..., 0].real).max():.2e}; grid points where it is above 1e-6: {int((bump[..., 0].real > 1e-6).sum())} of 800")
bad = np.argwhere(bump[..., 0].real > 1e-6)
if len(bad):
    print("   at (beta, sigma):", [(round(g_vals[a], 3), round(s_vals[b], 2)) for a, b in bad[:10]], "...; there eigenvalues 1 and 2 are", [bump[a, b, :2].real.round(4).tolist() for a, b in bad[:3]])
print("bump eigenvalue 3 (first after the zero and eigenvalue 2): Re max", f"{bump[..., 2].real.max():.4e}")""")
open('nb4.py','w').write(s)
EOF
grep -n "drop_m\|keep = " nb4.py | head
```

```
150:keep = tt >= 20
256:    keep = [i for i in range(k) if uni[i] < 0.5][:2 * n_pairs]   # consecutive pairs, skipping a constant mode
275:    cv_m, sv_m, drop_m = pair_cvs(Jm); cv_c, sv_c, drop_c = pair_cvs(Jc)
277:    print(f"seed {sd}: model pair CVs {cv_m.round(3)} (skipped {[i+1 for i in drop_m]}); circulant+noise pair CVs {cv_c.round(3)} (skipped {[i+1 for i in drop_c]}); "
Shell cwd was reset to
```

**Agent calls Bash**

```bash
python tools/entry.py --help 2>&1 | head -30; python -c "
import json; s=json.load(open('schemas/entry.schema.json')); print(json.dumps(s, indent=1)[:3000])"; cat entries/fouke-2025/README.md | head -40
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
[... 157 more lines not kept]
```

**Agent**

Now entry.yaml and requirements, then lock and run everything.

**Agent calls Bash**

```bash
cd /tmp/claude-1001/src && for n in 1 2 3; do :; done; python build.py nb1.py entries/clark-2026/tuning_curves.ipynb && python build.py nb2.py entries/clark-2026/network.ipynb && python build.py nb3.py entries/clark-2026/network_grid.ipynb && python build.py nb4.py entries/clark-2026/theory.ipynb
cd entries/clark-2026
cat > entry.yaml <<'EOF'
schema_version: 1
name: clark-2026
type: reproduction
title: Symmetries and continuous attractors in disordered neural circuits (Clark, Abbott and Sompolinsky 2026)
description: Tests the findings of Clark, Abbott and Sompolinsky (2026) on dandiset 000939, the
  postsubiculum recordings of Duszkiewicz et al. (2024) that the paper reuses. It rebuilds the
  1,533 head-direction tuning curves from the NWB files with the paper's procedure, checks them
  against the paper's cached curves, and tests the tuning-curve statistics, the fitted
  generative process, the data-derived network and its dynamics, and the mean-field theory.
license: Apache-2.0
notebooks:
- path: tuning_curves.ipynb
  title: Tuning curves, their statistics and the generative process
  runtime_minutes: 18
- path: network.ipynb
  title: The data-derived network and its dynamics
  runtime_minutes: 25
- path: network_grid.ipynb
  title: The lambda and c grid of the data-derived network
  runtime_minutes: 10
- path: theory.ipynb
  title: Mean-field theory and large-N spectra
  runtime_minutes: 4
helpers:
- hdring.py
- ring_dmft.py
related:
- id: dandi:000939/0.240528.1542
  relation: uses_data
- id: doi:10.1038/s41593-026-02452-4
  relation: reproduces
- id: doi:10.5281/zenodo.21827768
  relation: uses_data
- id: doi:10.5281/zenodo.21829584
  relation: references
EOF
cat > requirements.in <<'EOF'
aiohttp
astropy
fsspec
h5py
ipykernel
matplotlib
numpy
pandas
remfile
requests
scipy
statsmodels
EOF
cd  && python tools/entry.py lock entries/clark-2026 2>&1 | tail -5 && python tools/entry.py check entries/clark-2026 2>&1 | tail -20
```

```
wrote clark-2026/requirements.lock.txt (Python 3.13, with hashes)
0 error(s)
```

**Agent calls Bash**

```bash
date -u; cd  && time python tools/entry.py all entries/clark-2026 2>&1 | tail -15; date -u
```

```
Thu Nov 26 12:43:31 UTC 2026
Installed kernelspec registry-clark-2026 in executed/clark-2026/.venv/share/jupyter/kernels/registry-clark-2026
0 error(s)
pass  tuning_curves.ipynb  (1031 s)
pass  network.ipynb  (1476 s)
pass  network_grid.ipynb  (533 s)
pass  theory.ipynb  (151 s)

real	53m16.124s
user	138m13.602s
sys	2m3.139s
Thu Nov 26 13:36:47 UTC 2026
```

**Agent calls Bash**

```bash
ls executed/clark-2026/; source /tmp/claude-1001/dev/bin/activate; python /tmp/claude-1001/show.py executed/clark-2026/tuning_curves.ipynb 3000 | sed -n '/claim:fig4/,/claim:fig5ab/p'; python /tmp/claude-1001/show.py executed/clark-2026/tuning_curves.ipynb 3000 | sed -n '/claim:fig2l/,$p'
```

```
network.ipynb
network_grid.ipynb
result.json
theory.ipynb
tuning_curves.ipynb
===== ['claim:fig4-generative-fit'] _, Gdata_ft = H.calc_C(Phi_data) scale_vals = np.linspace(1,
shortlist pass (25,000 samples) in 312 s: minimum at sigma 1.4211, b 1.7307, beta 2.7659, error 0.00613
seed 444120632: final pass (500,000 samples) best sigma 1.4737, b 1.2145, beta 3.1103, error 0.00894
seed 444121632: final pass (500,000 samples) best sigma 1.4737, b 1.2145, beta 3.1103, error 0.00874
seed 444122632: final pass (500,000 samples) best sigma 1.4737, b 1.2145, beta 3.1103, error 0.00853
seed 444123632: final pass (500,000 samples) best sigma 1.4737, b 1.2145, beta 3.1103, error 0.00885
seed 444124632: final pass (500,000 samples) best sigma 1.4737, b 1.2145, beta 3.1103, error 0.00893
final pass, claim seed, the ten best of the 30:
 error_500k  sigma      b   beta  error_25k
     0.0089 1.4737 1.2145 3.1103     0.0066
     0.0095 1.4211 1.7307 2.7659     0.0061
     0.0106 1.4737 0.5262 4.8328     0.0093
     0.0122 1.4737 0.3541 6.2107     0.0116
     0.0123 1.4737 1.5586 2.7659     0.0141
     0.0125 1.5263 0.5262 4.8328     0.0123
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
source /tmp/claude-1001/dev/bin/activate; python /tmp/claude-1001/show.py executed/clark-2026/network.ipynb 4000 | sed -n '/claim:fig2b/,$p' | cut -c1-1200
```

```
===== ['claim:fig2b-sorted-weights-mexican-hat'] com_idx = np.floor(H.circular_center_of_mass(Phi.T) * Phi.sh
sorted profile: maximum 0.00527 at offset -8 (within N/20 = 76: True)
mean over offsets 0.000209; minimum over intermediate offsets (N/8 to 3N/8) -0.000985 at offset 571
fraction of intermediate offsets below the mean 0.88; below 0 0.80
near offsets (1 to N/20) mean 0.003988 (positive: local excitation)
arbitrary order: profile range -0.000386 to 0.000997, sd 0.000149; sorted profile sd 0.001470
sorted profile at offsets 0, +-10, +-50, +-100, +-200, +-400, +-766: {0: 0.0, 10: 0.004555, -10: 0.004544, 50: 0.003518, -50: 0.00346, 100: 0.001868, -100: 0.001761, 200: 0.000466, -200: 0.000646, 400: -0.00049, -400: -0.000658, 766: -0.000771}
mean correlation of each sorted row (aligned) with the profile: 0.356; same for arbitrary order: 0.026
[image]colour limits +-0.005; entries of J outside them: 426030 of 2350089

===== ['claim:fig2ef-data-network-quasicontinuous'] def run_2ef(sd):     rng = np.random.default_rng(sd)     x0 
seed 944155936: median distance at 0 s 1.9661, 1 s 0.08162, 20 s 0.00000, 29.90 s 0.00000; (a) True (b) False; angle moved under 2pi/20 between 1 s and the end: 1.00 (c) True; final angles in 77 of 100 bins (d) True; median movement 0.0025 rad
   median distance over time (s): {0.0: 1.96608, 0.1: 0.34277, 0.2: 0.20625, 0.3: 0.17918, 0.5: 0.14231, 1.0: 0.08162, 2.0: 0.02744, 5.0: 0.00113, 10.0: 0.0, 20.0: 0.0, 29.9: 0.0}
seed 944156936: median distance at 0 s 1.9693, 1 s 0.08004, 20 s 0.00000, 29.90 s 0.00000; (a) True (b) False; angle moved under 2pi/20 between 1 s and the end: 1.00 (c) True; final angles in 76 of 100 bins (d) True; median movement 0.0025 rad
seed 944157936: median distance at 0 s 1.9800, 1 s 0.08095, 20 s 0.00000, 29.90 s 0.00000; (a) True (b) False; angle moved under 2pi/20 between 1 s and the end: 1.00 (c) True; final angles in 75 of 100 bins (d) True; median movement 0.0031 rad
seed 944158936: median distance at 0 s 1.9
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
source /tmp/claude-1001/dev/bin/activate; python /tmp/claude-1001/show.py executed/clark-2026/network_grid.ipynb 6000 | sed -n '/claim:figs8/,$p' | cut -c1-600; python /tmp/claude-1001/show.py executed/clark-2026/theory.ipynb 6000 | sed -n '/claim:fig7-dmft/,/claim:fig7de/p;/claim:fig6fg/,$p' | cut -c1-700
```

```
===== ['claim:figs8-s9-lambda-and-c'] lamdas = [1e-12, 1e-10, 1e-8, 1e-6, 1e-4, 1e-2] cs = [0, 0.2
lambda 1e-12 done at 61 s
lambda 1e-10 done at 101 s
lambda 1e-08 done at 158 s
lambda 1e-06 done at 196 s
lambda 0.0001 done at 251 s
lambda 0.01 done at 305 s
       lamda    c  diverge  collapse  collapse_pc   n  norm_med  pc_radius_med
1.000000e-12 0.00        4         0           96 100 17.668937       0.648707
1.000000e-12 0.25        0         0            8  20 65.773961      33.184797
1.000000e-12 0.50        0         0            0  20 72.178908      38.962199
1.000000e-12 0.75        0         0            0  20 72.184394      38.967148
1.000000e-12 1.00        0         0            0 100 72.308227      38.963028
1.000000e-12 1.25        0         0            0  20 72.187263      38.969989
1.000000e-12 1.50        0         0            0  20 72.187790      38.970655
1.000000e-10 0.00        4         0           16  20 17.580749       0.799268
1.000000e-10 0.25        0         0           12  20 21.693958       1.584957
1.000000e-10 0.50        0         0            0  20 72.192925      38.978269
1.000000e-10 0.75        0         0            0  20 72.192799      38.978683
1.000000e-10 1.00        0         0            0  20 72.192803      38.978912
[... 82 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/clark-2026 && python - <<'EOF'
s=open('hdring.py').read()
old=s[s.find("def nearest_target(Phi_t, r, Phi_sq=None):"):s.find("def circularized_profile(J_sorted):")]
new='''def nearest_target(Phi_t, r, Phi_sq=None, refine=50):
    """Index of the nearest target firing-rate point and the distance / sqrt(N)
    (data_driven.compute_distances_to_ring). Phi_t (N_theta, N), r (N, B).
    The nearest point is first located with the expansion |a|^2 + |b|^2 - 2 a.b in the dtype
    of the inputs (float32), whose rounding hides distances below about 1e-3; the distance is
    then computed directly, as the paper's code does (norm of the difference), in float64, to
    the 2 * refine + 1 target points around that one, and the nearest of these is kept."""
    if Phi_sq is None:
        Phi_sq = (Phi_t ** 2).sum(1)
    d2 = Phi_sq[:, None] + (r ** 2).sum(0)[None, :] - 2 * (Phi_t @ r)
    idx = d2.argmin(0)
    n_t, N = Phi_t.shape
    cols = np.arange(r.shape[1])
    if not refine:
        dist = np.sqrt(np.maximum(d2[idx, cols], 0)) / np.sqrt(N)
        return idx, dist
    cand = (idx[None, :] + np.arange(-refine, refine + 1)[:, None]) % n_t
    rr = r.T.astype(np.float64)
    d = np.stack([np.linalg.norm(Phi_t[cand[k]].astype(np.float64) - rr, axis=1) for k in range(cand.shape[0])])
    j = d.argmin(0)
    return cand[j, cols], d[j, cols] / np.sqrt(N)


'''
s=s.replace(old,new)
open('hdring.py','w').write(s)
EOF
cd /tmp/claude-1001/src && python - <<'EOF'
s=open('nb2.py').read()
old="""sc_circ = shift_corr(res_gi["circulant"][0])"""
new="""Phi_srt32 = Phi32[:, order]; Phi_srt_sq = (Phi_srt32 ** 2).sum(1)
for key, (xf, pos) in res_gi.items():
    idx, dist = H.nearest_target(Phi_srt32, H.nonlin(xf), Phi_srt_sq)
    cs = H.count_states(idx, X.shape[0], X.shape[0] / 50)
    print(f"variant, position as the manifold angle of the nearest target point: {key}: states single {cs['single']}, greedy {cs['greedy']}, bins of 2 pi / 50 {cs['bins']}; median distance to the manifold {np.median(dist):.4f}")
sc_circ = shift_corr(res_gi["circulant"][0])"""
assert old in s; s=s.replace(old,new)
s=s.replace("""# bins of 31 neurons. With 100 initial conditions about 15 neurons apart, only the bins reading
# can reach the 50 states the criterion asks of the optimal matrix.""","""# bins of 31 neurons. The neuron at the peak of the smoothed currents is often the same for nearby
# angles (the initial states themselves give only 24 to 33 states under these readings), so the
# 50 states the criterion asks of the optimal matrix are out of reach of this position measure.
# As a variant, the position is taken as the manifold angle of the nearest target point, which can
# give up to 50 bins of 2 pi / 50.""")
open('nb2.py','w').write(s)
s=open('nb4.py').read()
s=s.replace("(skipped {[i+1 for i in drop_m]})","(unused {[i+1 for i in drop_m]})").replace("(skipped {[i+1 for i in drop_c]})","(unused {[i+1 for i in drop_c]})")
s=s.replace("""print("bump eigenvalue 3 (first after the zero and eigenvalue 2): Re max",""","""print(f"grid points where bump eigenvalue 1 is below -1e-6 (no zero mode found): {int((bump[..., 0].real < -1e-6).sum())} of 800;",
      "at (beta, sigma):", [(round(g_vals[a], 3), round(s_vals[b], 2)) for a, b in np.argwhere(bump[..., 0].real < -1e-6)[:8]])
print("bump eigenvalue 3 (first after the zero and eigenvalue 2): Re max",""")
open('nb4.py','w').write(s)
EOF
python build.py nb2.py entries/clark-2026/network.ipynb && python build.py nb4.py entries/clark-2026/theory.ipynb
cd /tmp/claude-1001 && source dev/bin/activate && python -c "
import sys; sys.path.insert(0,'entries/clark-2026')
import hdring as H, numpy as np, time
Phi=np.load('Phi.npy'); X=np.load('X.npy'); P32=Phi.astype(np.float32)
r=H.nonlin(X[::100].T.astype(np.float32)+np.float32(1e-3))
t=time.time(); i,d=H.nearest_target(P32,r); print(time.time()-t, d[:3], i[:5])
"
```

```
0.06534647941589355 [0.00062093 0.00062162 0.00062313] [  0 100 200 300 400]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd  && python tools/entry.py check entries/clark-2026 2>&1 | tail -3 && time python tools/entry.py all entries/clark-2026 2>&1 | tail -8; date -u
```

```
Thu Nov 26 13:38:18 UTC 2026
0 error(s)
Installed kernelspec registry-clark-2026 in executed/clark-2026/.venv/share/jupyter/kernels/registry-clark-2026
0 error(s)
pass  tuning_curves.ipynb  (974 s)
pass  network.ipynb  (1449 s)
pass  network_grid.ipynb  (529 s)
pass  theory.ipynb  (151 s)

real	51m49.637s
user	135m27.715s
sys	1m45.660s
Thu Nov 26 14:30:12 UTC 2026
```

**Agent calls Bash**

```bash
source /tmp/claude-1001/dev/bin/activate; python /tmp/claude-1001/show.py executed/clark-2026/network.ipynb 4000 | sed -n '/claim:fig2ef/,/claim:fig2jk/p;/claim:figs11b/,$p' | cut -c1-900; python /tmp/claude-1001/show.py executed/clark-2026/theory.ipynb 3000 | grep -A3 "bump eigenvalue 1"
```

```
===== ['claim:fig2ef-data-network-quasicontinuous'] def run_2ef(sd):     rng = np.random.default_rng(sd)     x0 
seed 944155936: median distance at 0 s 1.9661, 1 s 0.08163, 20 s 0.00068, 29.90 s 0.00062; (a) True (b) False; angle moved under 2pi/20 between 1 s and the end: 1.00 (c) True; final angles in 77 of 100 bins (d) True; median movement 0.0025 rad
   median distance over time (s): {0.0: 1.96608, 0.1: 0.34276, 0.2: 0.20625, 0.3: 0.17919, 0.5: 0.1423, 1.0: 0.08163, 2.0: 0.02749, 5.0: 0.00122, 10.0: 0.0007, 20.0: 0.00068, 29.9: 0.00062}
seed 944156936: median distance at 0 s 1.9694, 1 s 0.08004, 20 s 0.00070, 29.90 s 0.00076; (a) True (b) False; angle moved under 2pi/20 between 1 s and the end: 1.00 (c) True; final angles in 76 of 100 bins (d) True; median movement 0.0025 rad
seed 944157936: median distance at 0 s 1.9800, 1 s 0.08096, 20 s 0.00068, 29.90 s 0.00072; (a) True (b) False; angle moved under 2pi/20 between 1 s and the end: 1.00 (c) True; final angles in 75 of 100 bins (d) True; median movement 0.0028 rad
seed 944158936: median distance at 0 s 1.9585, 1 s 0.07638, 20 s 0.00067, 29.90 s 0.00066; (a) True (b) False; angle moved under 2pi/20 between 1 s and the end: 1.00 (c) True; final angles in 70 of 100 bins (d) True; median movement 0.0025 rad
seed 944159936: median distance at 0 s 1.9766, 1 s 0.07784, 20 s 0.00067, 29.90 s 0.00074; (a) True (b) False; angle moved under 2pi/20 between 1 s and the end: 1.00 (c) True; final angles in 77 of 100 bins (d) True; median movement 0.0028 rad
time 434 s
[image]distance range 7.036138078279505e-05 2.1230659900698385

===== ['claim:fig2gi-circulant-noise-collapses'] X_srt = X[:, order] J_circ = np.asarray(H.circulant_projecti
sorted: states single 24, greedy 25, bins 31; distinct peak neurons 41; peak height range 7.84 to 11.49
circulant: states single 2, greedy 39, bins 50; distinct peak neurons 100; peak height range 4.77 to 4.77; correlation with the best shift of the first state: min 1.0000, median 1.0000
cir
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "stamp" tools/entry.py | head -30; cat executed/clark-2026/result.json | head -30
```

```
30:A run that passes leaves a stamp beside the executed copies (.clean-run.json):
608:    """The stamp of executed copies that a run now would only make again: made from this hash, each copy still as
611:        stamp = json.loads((output_dir / STAMP).read_text())
613:        if stamp["hash"] != entry_hash(entry_dir) or time.time() - stamp["finished"] > REUSE_DAYS * 86400:
615:        if [n["path"] for n in entry["notebooks"]] != [r["notebook"] for r in stamp["results"]]:
617:        for r in stamp["results"]:
620:        return stamp
627:    stamp = None if fresh else reusable(entry_dir, output_dir, max_minutes)
628:    if stamp:
629:        when = time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime(stamp["finished"]))
630:        for r in stamp["results"]:
633:              f"{stamp['hash'][:12]}). Nothing was executed and no environment was built; --fresh runs it again.")
{
 "entry": "clark-2026",
 "python": "3.13",
 "results": [
  {
   "notebook": "tuning_curves.ipynb",
   "ok": true,
   "seconds": 974,
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "def entry_hash" -A30 tools/entry.py | head -45
```

```
593:def entry_hash(entry_dir: Path) -> str:
594-    """A hash of everything a run of the entry's notebooks reads from the repository: every file of the entry (its
595-    notebooks, helpers, lock and entry.yaml, which names the Python and the dataset versions), the packages `run`
596-    adds, and RUN_VERSION. Two runs from the same hash execute the same code on the same data versions."""
597-    import hashlib
598-    h = hashlib.sha256(f"run {RUN_VERSION}; harness {' '.join(HARNESS)}; python {python_of(entry_dir)}\n".encode())
599-    for path in sorted(p for p in entry_dir.rglob("*") if p.is_file()):
600-        rel = path.relative_to(entry_dir)
601-        if any(part in ("__pycache__", ".ipynb_checkpoints", ".venv") or part.endswith(".pyc") for part in rel.parts):
602-            continue
603-        h.update(f"{rel.as_posix()}\0{file_hash(path)}\n".encode())
604-    return h.hexdigest()
605-
606-
607-def reusable(entry_dir: Path, output_dir: Path, max_minutes: float) -> dict | None:
608-    """The stamp of executed copies that a run now would only make again: made from this hash, each copy still as
609-    the run left it, each within the time limit asked for now, and not older than REUSE_DAYS. Else None."""
610-    try:
611-        stamp = json.loads((output_dir / STAMP).read_text())
612-        entry = yaml.safe_load((entry_dir / "entry.yaml").read_text())
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001/src && grep -n "Result: \.\.\." nb1.py nb2.py nb3.py nb4.py | head -40
```

```
nb1.py:199:# **Result: ...**
nb1.py:234:# **Result: ...**
nb1.py:281:# **Result: ...**
nb1.py:309:# **Result: ...**
nb1.py:352:# **Result: ...**
nb1.py:374:# **Result: ...**
nb1.py:426:# **Result: ...**
nb1.py:508:# **Result: ...**
nb1.py:543:# **Result: ...**
nb1.py:564:# **Result: ...**
nb1.py:585:# **Result: ...**
nb1.py:603:# **Result: ...**
nb1.py:619:# **Result: ...**
nb1.py:681:# **Result: ...**
nb2.py:100:# **Result: ...**
nb2.py:157:# **Result: ...**
nb2.py:243:# **Result: ...**
nb2.py:310:# **Result: ...**
nb2.py:346:# **Result: ...**
nb2.py:388:# **Result: ...**
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001/src && cat > concl.py <<'PYEOF'
import re
R = {
'nb1.py': [
"**Result: reproduced.** The files hold 31 sessions, one per subject, with 2,691 units, of which 1,533 carry `is_head_direction`; all 1,533 are also `is_excitatory`, so readings (a) and (b) give the same count, and the code's drop of all-zero curves removes none. The nine mice with a `wake_opto` epoch hold 315 head-direction cells, and the four largest sessions are A3707 (117), A3716 (93), A3711 (90) and A3706 (86).",
"**Result: reproduced.** The record's MD5 matches, and the cache has the same session order, unit counts and labels as the files. All 1,533 recomputed partition-averaged curves correlate at r = 1.000000 with the cached ones (largest absolute difference 1.4e-14 Hz). The chosen widths agree for both partitions in 78% of units; where they differ the curves still agree to 2e-14 Hz, so those widths give the same smoothed curve (ties).",
"**Result: reproduced.** Peak counts at zthresh 1 range from 1 to 6 (1,121 curves with one peak, 357 with two, 48 with three). The two highest peaks of the 412 multi-peaked curves are separated by 0.13 to 3.14 rad, with an interquartile range of 1.38 rad, above pi/4 (0.79).",
"**Result: reproduced.** The data give 1,533, 412 and 55 curves with at least 1, 2 and 3 peaks, the paper's numbers exactly. Of 100,000 generative samples at the paper's parameters, 23,908 have at least two and 1,052 at least three under the claim's seed (expected 24,271 within 2,427 and 1,043 within 104); over five seeds 23,908 to 24,267 and 1,001 to 1,082, all within tolerance.",
"**Result: reproduced.** The mouse-average mean profile has one local maximum, at offset 0, and correlates with its reflection at r = 0.9998. The peak of the standard deviation profile is 0.56 times the peak of the mean (2.64 against 4.72), which satisfies both readings of comparable. The median correlation of a mouse's profile with the average is 0.996 for the mean and 0.974 for the standard deviation.",
"**Result: reproduced.** Two sessions have uncorrected P < 0.05 (A3711, 0.044; A9701, 0.048), none is significant after Benjamini-Hochberg correction, and the corrected P values range from 0.592 to 0.968, as the paper reports (0.59 to 0.97).",
"**Result: reproduced.** For all four mice and both functions the distance from circulant form falls at every step from 5 to 80 neurons (for example A3707, 0.73 to 0.27 raw and 0.71 to 0.16 centered and normalized), under all five seeds. The leading four eigenvectors of each mouse's centered and normalized function have 89% to 98% of their power at one frequency, eigenvectors 1 and 2 at frequency 1 and 3 and 4 at frequency 2.",
"**Result: partially reproduced.** With the final pass of 500,000 samples the minimum is at sigma 1.4737, b 1.2145, beta 3.1103 under all five seeds: sigma (1.42 within 0.142) and beta (2.77 within 0.345) match and b (1.73 within 0.173) does not. The paper's grid point (1.4211, 1.7307, 2.7659) is the minimum of the 25,000-sample shortlist pass and the second best in the final pass (error 0.0095 against 0.0089); in the float32 variant it is the better of the two under the claim's seed (0.00902 against 0.00920) and the worse under the other four. The error surface has two near-equal minima, and which one wins depends on the draws and the arithmetic.",
"**Result: reproduced.** At the fitted parameters the generative mean profile lies within the range of the 31 mouse profiles at all 100 offsets and the standard deviation profile at 97, and their peaks are within 3.0% and 1.3% of the mouse-average peaks; both readings hold for both profiles under all five seeds. At the paper's parameters the same holds (within range at 100 offsets, peaks within 0.2% and 1.9%).",
"**Result: reproduced.** At zthresh 1 the total variation distance between the data and generative peak-count histograms is 0.022 and the Hellinger distance 0.061, the smallest of the three thresholds (0.065 and 0.086 at 0.5, 0.128 and 0.124 at 0), and below 0.15, under all five seeds. At the paper's parameters the order is the same (0.026, 0.040, 0.105).",
"**Result: reproduced.** Under reading (a) the median generative heights of the three highest peaks are within 0.8%, 1.5% and 5.3% of the data medians (5.63, 2.90 and 2.26). Under reading (b) the Kolmogorov-Smirnov distance is 0.058 and 0.054 for the first two peaks and 0.186 for the third (55 data curves), so (b) holds for two of three. Both hold the same way under the five seeds and at the paper's parameters (third peak 8.8% and KS 0.253).",
"**Result: reproduced.** 23.7% of data curves have a flip-symmetry correlation below 0.5 and 10.3% below 0; the generative process gives 28.1% and 11.8%, ratios of 1.19 and 1.14, within the factor 1.5 under both readings and all five seeds. The medians are 0.927 (data) and 0.834 (generative).",
"**Result: reproduced.** The median head-direction information is 1.288 for the data and 1.368 for the generative process, 6.2% apart, and the Kolmogorov-Smirnov distance is 0.138, below 0.15; both readings hold under all five seeds, and at the paper's parameters (4.3%, 0.109).",
"**Result: reproduced.** In A3707, over 17,990 bins of 100 ms with tracked head direction, the median absolute difference between the angle of the peak of m and the head direction is 0.168 rad, below pi/8 (0.393), against 1.294 rad with the head direction shifted by 60 s. The circular correlation is 0.896, just below the 0.9 of reading (b), so the claim holds under reading (a). With curves from one partition applied to the other partition's spikes the median error is 0.172 and 0.177 rad.",
],
'nb2.py': [
"**Result: reproduced.** Sorted by center of mass, the mean of the weights along each circular diagonal peaks at offset -8 (0.0053), stays positive over offsets up to N/20 (mean 0.0040), and falls below its mean at 88% of intermediate offsets and below zero at 80%, down to -0.00099 at offset 571: local excitation and longer-range inhibition. In arbitrary order the same profile is flat (sd 0.00015 against 0.00147 sorted), and an aligned sorted row correlates with the profile at 0.356 on average against 0.026 in arbitrary order.",
"**Result: reproduced.** The median distance to the manifold falls from 1.966 at 0 s to 0.0816 at 1 s, under one tenth (reading a), and to 0.00068 at 20 s; reading (b) fails, as the distance keeps falling after 1 s. Between 1 s and the end, every trajectory's manifold angle moves by less than 2 pi / 20 (median 0.0025 rad, reading c), and the 100 final angles occupy 77 of 100 bins (reading d). The outcome is the same under all five seeds.",
"**Result: partially reproduced.** The circulant plus scrambled residuals collapses to 4 states (2 to 7 over five seeds; the symmetric version to 2), and the circulant matrix's 100 final states are exact shifts of one another (correlation 1.0000). The sorted optimal matrix keeps 24, 25 or 31 states under the three merging readings, short of the criterion's 50; its initial states already give only 24 to 33 under this position measure, so the 50 cannot be reached by it. With the position read as the manifold angle of the nearest target point (variant), the sorted matrix keeps all 50 bins of 2 pi / 50, at a median distance of 0.0008 from the manifold, and the circulant plus noise 7. The contrast between the optimal matrix and the circulant plus noise holds.",
"**Result: reproduced.** Over 20 to 110 s the angle of the peak of m follows the integrated constant input of 0.8 rad/s with a median absolute error of 0.011 rad and circular correlation 1.000, and the integrated angular velocity of A3707 (13.2 rad of net turning) with a median error of 0.013 rad and circular correlation 1.000, under both readings.",
"**Result: reproduced.** The leading 10 eigenvalues have imaginary parts at most 6.8% of their real parts. After setting aside the fifth (1.0894, whose eigenvector is closest to uniform), the four leading pairs have gaps of 0.027, 0.000, 0.0002 and 0.000 within, each smaller than the gap to the next pair (0.139, 0.183, 0.036, 0.0002); the first pair (1.4384 and 1.4113) is not exact.",
"**Result: partially reproduced.** Every final state is on the manifold at the resolution of the fig2ef reference (largest final distance 0.0015 against 2 at the start of fig2ef), with none elsewhere, and at standard deviation 1 all 34 final angles fall in one state (1.69 to 1.70 rad), under all five seeds. The criterion's threshold, the largest distance at 20 s in fig2ef (0.00132), is met by 91% to 100% of final states, below the 95% asked at standard deviations 10, 50 and 1000 under the claim's seed (0.94, 0.91, 0.94), and under the median reading by 29% to 74%.",
],
'nb3.py': [
"**Result: partially reproduced.** At c 0 some runs diverge at every lambda up to 1e-4 (1 to 4 of 100), and under reading (ii) of collapse nearly all others fall to the homogeneous state (96 to 100 of 100, radius 0.65 to 0.80 against 39 for the manifold) at every lambda; under reading (i) no run collapses, since the homogeneous state keeps a firing-rate norm of 17.3 to 17.7. No c above 0 diverges up to lambda 1e-4, and c 0.25 still leaves the collapse (12 of 20 at lambda 1e-8 under reading ii). At lambda 1e-2 the manifold is lost for c up to 0.75 (all 20 collapse under reading ii), but at c 1 the states keep a radius of 4.6, just above the collapse threshold of 3.9, so the criterion's test at c 1 fails. The flow error rises at large lambda (2.1e-2 at 1e-2) and at small lambda from 1.3e-10 at 1e-10 to 2.6e-9 at 1e-12, but 1e-8 (1.7e-8) is not below 1e-12, so that part of the criterion fails too.",
],
'nb4.py': [
"**Result: reproduced.** All twelve interaction profiles of Fig. 7a are positive at 0 (4.9 to 38.5) and negative at some offset (minimum -1.5 to -6.0). Over the 40 by 20 grid the bump's second eigenvalue is negative at every point (largest -4.7e-8) and the uniform state's leading eigenvalue is real and positive at every point (smallest 4.7e-5). With Q fixed the bump at sigma 1.4211 and beta 2.7659 has a positive eigenvalue (0.446). At 293 of the 800 grid points no zero eigenvalue is found at the bump (the leading one is below -1e-6), mostly at small beta and large sigma.",
"**Result: not reproduced.** The convergence time falls with beta for every sigma and varies across sigma by at most a factor of 2.55 at each beta (reading b holds, a does not), but it reaches 20.5 tau at beta 1.1 and sigma 100, outside 0.5 to 10 tau. The divergence time ranges from 0.15 to 3.83 tau over beta 1 to 10, rises with beta at small sigma (up to 11 increases), and varies by up to a factor of 24 across sigma. Neither the first two parts nor the third hold for both timescales. The thresholds are the claims file's.",
"**Result: reproduced.** Driven by A3707's angular velocity, the peak of the mean-field bump follows the integrated angular velocity with a median absolute error of 0.032 rad and circular correlation 0.998 over 20 to 110 s, against 1.359 rad with the target shifted by 30 s. The bump keeps its contrast (0.749 at 20 s, 0.728 at the end).",
"**Result: reproduced.** Under the claim's seed the leading 11 eigenvalues at N 2,500 are within 5.0% of the mean-field values alpha Gamma_x_n / Gamma_phi_n (alpha 0.767), their imaginary parts are under 10% of their real parts, the first four pairs are closer within than to the next pair, and the ninth (0.181 against 0.182, Fourier index 0) is the unpaired constant mode. Under one of the four other seeds the largest difference is 13.6%, so the outcome is seed sensitive.",
"**Result: reproduced.** For the circulant matrix plus weak noise the radii in the planes of the two leading singular-vector pairs have coefficients of variation 0.063 and 0.070 (rings, below 0.2); for the model they are 0.53 and 0.52 (structureless, above 0.4). Both spectra show four of four leading doublets with the unpaired eigenvalue ninth. The same holds under all five seeds.",
],
}
SUMM = {
'nb1.py': """# ## Summary
#
# | claim | outcome |
# |---|---|
# | hd-cell-selection (link) | reproduced |
# | tuning-curves-match-cache (link, with inputs) | reproduced |
# | fig1e-heterogeneous-peaks | reproduced |
# | fig5d-peak-numbers | reproduced |
# | fig1fg-mean-and-fluctuation-profiles | reproduced |
# | fig3ab-centers-of-mass-uniform | reproduced |
# | fig3c-correlation-approaches-circulant | reproduced |
# | fig4-generative-fit | partially reproduced |
# | fig5ab-profiles-match | reproduced |
# | fig5c-peak-counts-match | reproduced |
# | fig5d-peak-heights-match | reproduced |
# | fig5e-flip-symmetry-match | reproduced |
# | fig5f-information-match | reproduced |
# | fig2l-recorded-bump-tracks-hd | reproduced |
#
# A failure to reproduce here may be a failure of this attempt, not of the paper: see the
# reasoning and the differences from the paper's method.
#
# **Differences from the paper's method.** The generative fit evaluates the whole grid with 25,000
# samples and only the 30 best points with 500,000, where the paper uses 500,000 at every point;
# random draws come from each claim's seed, not numpy seed 42; the Poisson likelihood that picks
# the smoothing width drops a term that does not depend on the curve.
#
# **The dataset.** At version 0.240528.1542 the files hold what the paper describes: 31 sessions,
# 2,691 units, 1,533 head-direction units (all also labelled excitatory), the wake_square epoch in
# every file, head direction in radians at 10 ms, and nine files with an optogenetic epoch. The
# tuning curves rebuilt from them match the paper's cached curves to 1e-14 Hz. Spikes and head
# direction share a clock: in every session the head-direction information peaks within 0.05 s of
# lag 0. No recording appears twice.""",
'nb2.py': """# ## Summary
#
# | claim | outcome |
# |---|---|
# | fig2b-sorted-weights-mexican-hat | reproduced |
# | fig2ef-data-network-quasicontinuous | reproduced |
# | fig2gi-circulant-noise-collapses | partially reproduced |
# | fig2jk-velocity-integration | reproduced |
# | figs14-data-spectrum-doublets | reproduced |
# | figs11b-data-network-global-stability | partially reproduced |
#
# A failure to reproduce here may be a failure of this attempt, not of the paper: see the
# reasoning and the differences from the paper's method.
#
# **Differences from the paper's method.** Simulations in numpy float32 in place of torch float32;
# the distance to the manifold is read every 100 ms (the paper saves every 10 ms); random draws
# come from each claim's seed. The network built from the dataset reproduces the paper's printed
# reconstruction error (1.7152e-08) to five digits.""",
'nb3.py': """# ## Summary
#
# | claim | outcome |
# |---|---|
# | figs8-s9-lambda-and-c | partially reproduced |
#
# A failure to reproduce here may be a failure of this attempt, not of the paper: see the
# reasoning and the differences from the paper's method.
#
# **Differences from the paper's method.** 20 initial conditions at most grid points, 100 at the
# points the criterion reads; collapse is read in two ways, as the claims file's words leave open.""",
'nb4.py': """# ## Summary
#
# | claim | outcome |
# |---|---|
# | fig7-dmft-mexican-hat-and-stability | reproduced |
# | fig7de-dmft-timescales | not reproduced |
# | fig7c-dmft-integrates-behavior | reproduced |
# | fig6cd-eigenvalues-real-degenerate | reproduced (seed sensitive) |
# | fig6fg-disordered-eigenvectors | reproduced |
#
# A failure to reproduce here may be a failure of this attempt, not of the paper: see the
# reasoning and the differences from the paper's method.
#
# **Differences from the paper's method.** The paper's `ring/dmft.py` is run as it is, without
# torch; the idealized tuning curves are drawn from each claim's seed (the paper's notebook uses
# numpy seeds 42 and 45), and the 50,000-curve spectrum is accumulated in chunks.""",
}
for f, texts in R.items():
    s = open(f).read()
    parts = s.split("# **Result: ...**")
    assert len(parts) - 1 == len(texts), (f, len(parts) - 1, len(texts))
    out = parts[0]
    for t, p in zip(texts, parts[1:]):
        # wrap at ~100 chars as markdown comment lines
        words, lines, cur = t.split(), [], "#"
        for w in words:
            if len(cur) + len(w) + 1 > 100:
                lines.append(cur); cur = "# " + w
            else:
                cur = cur + " " + w
        lines.append(cur)
        out += "\n".join(lines) + p
    old = "# ## Summary\n#\n# (written after the run)"
    assert old in out, f
    out = out.replace(old, SUMM[f])
    open(f, "w").write(out)
print("ok")
PYEOF
python concl.py && grep -c "Result: " nb1.py nb2.py nb3.py nb4.py && grep -n "—\|rather\|\*\*" nb*.py | grep -v "Result:\|\*\*Paper\|\*\*Dataset\|\*\*Outside\|\*\*Code\|\*\*Differences\|\*\*The dataset" | head
```

```
ok
nb1.py:14
nb2.py:6
nb3.py:1
nb4.py:5
nb1.py:10:# at version **0.240528.1542** (doi:10.48324/dandi.000939/0.240528.1542). This is the version the
nb1.py:477:                C = np.mean(np.abs(np.fft.rfft(P, axis=1, norm="forward")[:, :20]) ** 2, 0)
nb1.py:478:                L[i, j, k] = np.sqrt(((C - Gdata_ft[:20]) ** 2).sum())
nb1.py:488:            errs.append(np.mean(np.abs(np.fft.rfft(P, axis=1, norm="forward")[:, :20]) ** 2, 0))
nb1.py:490:        out.append((np.sqrt(((C - Gdata_ft[:20]) ** 2).sum()), scale_vals[i], bias_vals[j], beta_vals[k], L[i, j, k]))
nb1.py:520:        Cs.append(np.mean(np.abs(np.fft.rfft(P, axis=1, norm="forward")[:, :20]) ** 2, 0))
nb1.py:521:    return np.sqrt(((np.mean(Cs, 0) - Gdata_ft[:20]) ** 2).sum())
nb1.py:683:t_hd = s["hd_t"]; i0 = np.argmin((t_hd - d["ti"]) ** 2)
nb2.py:60:err = np.mean((X - Phi @ J.T) ** 2)
nb2.py:66:Phi32 = Phi.astype(np.float32); Phi_sq = (Phi32 ** 2).sum(1)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001/src && python - <<'EOF'
import re
for f in ['nb1.py','nb2.py','nb3.py','nb4.py']:
    s=open(f).read()
    s=re.sub(r'\*\*(Paper\.|Dataset\.|Outside input\.|Code followed\.|Differences from the paper\'s method\.|The dataset\.)\*\*', r'\1', s)
    s=s.replace('**0.240528.1542**','0.240528.1542')
    bad=[l for l in s.split('\n') if '**' in l and l.startswith('#') and 'Result:' not in l]
    print(f, bad[:3])
    open(f,'w').write(s)
EOF
for n in 1 2 3 4; do :; done
python build.py nb1.py entries/clark-2026/tuning_curves.ipynb && python build.py nb2.py entries/clark-2026/network.ipynb && python build.py nb3.py entries/clark-2026/network_grid.ipynb && python build.py nb4.py entries/clark-2026/theory.ipynb; grep -c "—" *.py; date -u
```

```
nb1.py []
nb2.py []
nb3.py []
nb4.py []
build.py:0
concl.py:0
nb1.py:0
nb2.py:0
nb2_test.py:0
nb3.py:0
nb3_test.py:0
nb4.py:0
Thu Nov 26 14:32:00 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
s=json.load(open('schemas/attempt.schema.json'))
print(s.get('required'))
p=s['properties']
for k in p: print(k, json.dumps(p[k])[:400])
EOF
```

```
['schema_version', 'id', 'datasets', 'paper', 'date', 'provenance', 'outcomes']
schema_version {"const": 3}
id {"type": "string", "pattern": "^[a-z0-9]+(-[a-z0-9]+)*$"}
datasets {"description": "Every dataset the attempt used (docs/protocol.md, \"Record the attempt\").", "type": "array", "minItems": 1, "items": {"description": "A dataset the attempt used: the archive, the dataset's identifier there, the pinned version, and how the paper relates to it.", "type": "object", "additionalProperties": false, "required": ["archive", "id", "version", "relation"], "properties": {"a
missing_datasets {"description": "Datasets the paper's claims rest on that this attempt could not use; claims that need one are blocked with dataset_missing.", "type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["why"], "properties": {"archive": {"type": "string"}, "id": {"type": "string"}, "name": {"type": "string"}, "why": {"type": "string"}}}}
paper {"type": "string", "pattern": "^doi:10\\.[0-9]{4,9}/.+$"}
date {"type": "string", "format": "date"}
entry {"description": "The entry this attempt produced (its name), if any.", "type": "string"}
deprecated {"description": "Set when the attempt no longer stands, for example because its claims were written without the paper's full text. The record is kept as it was; its outcomes are shown but not counted.", "type": "object", "additionalProperties": false, "required": ["date", "reason"], "properties": {"date": {"type": "string", "format": "date"}, "reason": {"type": "string", "minLength": 1}, "supersed
provenance {"type": "object", "additionalProperties": false, "required": ["kind", "accountable"], "properties": {"kind": {"enum": ["agent", "person"]}, "accountable": {"description": "The person or organisation responsible for this attempt.", "type": "object", "additionalProperties": false, "required": ["name"], "properties": {"name": {"type": "string"}, "orcid": {"type": "string", "pattern": "^[0-9]{4}-[0-9
outcomes {
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
s=json.load(open('schemas/attempt.schema.json'))
p=s['properties']
print(json.dumps(p['provenance'])[:1500]); print(json.dumps(p['outcomes']['items']['properties'])[:2500]); print(json.dumps(p['findings']['items']['properties'])[:1200]); print(json.dumps(p['datasets']['items']['properties']))
EOF
```

```
{"type": "object", "additionalProperties": false, "required": ["kind", "accountable"], "properties": {"kind": {"enum": ["agent", "person"]}, "accountable": {"description": "The person or organisation responsible for this attempt.", "type": "object", "additionalProperties": false, "required": ["name"], "properties": {"name": {"type": "string"}, "orcid": {"type": "string", "pattern": "^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]$"}, "ror": {"type": "string"}}}, "agent": {"description": "Required when kind is agent.", "type": "object", "additionalProperties": false, "required": ["harness", "model", "protocol"], "properties": {"harness": {"type": "string"}, "model": {"type": "string"}, "protocol": {"description": "Version of the reproduction protocol the agent followed.", "type": "string"}}}, "runner": {"description": "Where the attempt was run: the platform, and the run that wrote this record. Its other runs (verification rounds, revisions) are linked from their transcripts.", "type": "object", "additionalProperties": false, "required": ["platform"], "properties": {"platform": {"description": "The platform that ran it, e.g. GitHub Actions, or local for a person's machine.", "type": "string", "minLength": 1}, "url": {"description": "The run that wrote the record, e.g. https://github.com/<owner>/<repo>/actions/runs/<id>.", "type": "string", "pattern": "^https://"}}}, "author_notes": {"description": "The notes from the paper's authors that this attempt used (papers/author-notes/<pape
{"claim": {"description": "Claim id from the target's claims file.", "type": "string"}, "outcome": {"enum": ["reproduced", "partially_reproduced", "not_reproduced", "blocked"], "description": "Describes the result, not the method: whether the effect the claim states was found. Differences in method from the paper go in `deviations`."}, "blocked_by": {"description": "Required when outcome is blocked.", "enum": ["data_missing", "metadata_insufficient", "methods_underspecified", "data_unreadable",
[... 2 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/clark-2026/README.md",
 "content": "# Clark, Abbott & Sompolinsky (2026) on dandiset 000939\n\nTests the findings of [Clark, Abbott & Sompolinsky (2026)](https://doi.org/10.1038/s41593-026-02452-4)\non [DANDI:000939](https://dandiarchive.org/dandiset/000939/0.240528.1542), the postsubiculum\nrecordings of Duszkiewicz et al. (2024) that the paper reuses, at the version the paper cites. The\n1,533 head-direction tuning curves are rebuilt from the NWB files with the paper's procedure; they\nmatch the paper's cached curves on Zenodo to 1e-14 Hz.\n\n| Claim | Outcome |\n|---|---|\n| Session, unit and head-direction cell counts (link) | Reproduced |\n| Tuning curves match the paper's cache (link, with the Zenodo input) | Reproduced |\n| Heterogeneous, irregularly spaced peaks (Fig. 1e) | Reproduced |\n| Peak numbers, data and generative process (Fig. 5d legend) | Reproduced |\n| Mean and fluctuation profiles (Fig. 1f,g) | Reproduced |\n| Centers of mass uniform, Kuiper test (Fig. 3a,b) | Reproduced |\n| Correlation function approaches circulant form (Fig. 3c, S13) | Reproduced |\n| Generative fit (sigma, beta, b) of about (1.42, 2.77, 1.73) (Fig. 4) | Partially reproduced |\n| Generative profiles, peak counts, peak heights, flip symmetry, information (Fig. 5a to f) | Reproduced (5 claims) |\n| Recorded bump tracks head direction (Fig. 2l) | Reproduced |\n| Sorted weights show a Mexican hat (Fig. 2b) | Reproduced |\n| Data network is quasi-continuous (Fig. 2e,f) | Reproduced |\n| Circulant plus noise collapses (Fig. 2g to i) | Partially reproduced |\n| Velocity integration (Fig. 2j,k) | Reproduced |\n| Lambda and c grid (Supplementary Figs. 8, 9) | Partially reproduced |\n| Global stability of the data network (Supplementary Fig. 11b) | Partially reproduced |\n| Spectrum doublets of the data network (Supplementary Fig. 14) | Reproduced |\n| Mean-field theory: Mexican hat and stability (Fig. 7) | Reproduced |\n| Mean-field timescales (Fig. 7d,e) | Not reproduced |\n| Mean-field bump integrates behaviour (Fig. 7c) | Reproduced |\n| Large-N eigenvalues and eigenvectors (Fig. 6c,d,f,g) | Reproduced (2 claims) |\n| Grid cells, weight noise, finite-N stability of the model, rank-four ensembles | Blocked: too large for the run's time |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe attempt record, with the reasons and the differences from the paper's method, is\n[`attempts/clark-2026-01.yaml`](../../attempts/clark-2026-01.yaml).\n\n- `tuning_curves.ipynb`: the files, the tuning curves and their statistics, and the generative\n  process (about 17 minutes, most of it the generative fit).\n- `network.ipynb`: the data-derived network, its weights, dynamics and spectrum (about 25 minutes).\n- `network_grid.ipynb`: the lambda and c grid (about 9 minutes).\n- `theory.ipynb`: the mean-field theory and the large-N spectra (about 3 minutes).\n- `hdring.py`: streaming the files, the paper's tuning-curve procedure, the statistics, the\n  generative process and the network, in numpy, each function naming the function of the paper's\n  code it repeats. Other notebooks on this dandiset can import it.\n- `ring_dmft.py`: a copy of the paper's `ring/dmft.py` (MIT licence) without its torch imports.\n"
}
```

```
File created successfully at: entries/clark-2026/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
date -u; cd  && python tools/entry.py check entries/clark-2026 2>&1 | tail -2 && time python tools/entry.py all entries/clark-2026 2>&1 | tail -8; date -u
```

**Agent calls Write**

```json
{
 "file_path": "attempts/clark-2026-01.yaml",
 "content": "schema_version: 3\nid: clark-2026-01\ndatasets:\n- archive: dandi\n  id: \"000939\"\n  version: 0.240528.1542\n  doi: 10.48324/dandi.000939/0.240528.1542\n  relation: reuses\npaper: doi:10.1038/s41593-026-02452-4\ndate: 2026-11-26\nentry: clark-2026\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-18\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/encorescience/encore-registry/actions/runs/45814018831\ninputs:\n- what: The paper's cached tuning curves, mouse_data/tc_data.npz of the record's tar\n    symmetries_caches_v1.tar, read by range requests and checked against the record's\n    CHECKSUMS.md5 (MD5 6e1f3a17ab67e2e0eb8fac35d89e2d57). Used only by the link claim\n    tuning-curves-match-cache.\n  source: doi:10.5281/zenodo.21827768\n- what: The paper's code (package ring and its notebooks), read for every method detail and\n    repeated in numpy in hdring.py; ring/dmft.py is copied as ring_dmft.py without its torch\n    imports (MIT licence). The simulation-only claims (data elsewhere) run this code.\n  source: https://github.com/davidclark1/symmetries-continuous-attractors at commit\n    245726fa78457e10cdcf17e6be36fba1dec98061\noutcomes:\n- claim: hd-cell-selection\n  outcome: reproduced\n  notebook: tuning_curves.ipynb\n  output: claim:hd-cell-selection\n  measured:\n  - 31\n  - 2691\n  - 1533\n  - 315\n  - 117\n  notes: 31 files, one per subject, 2,691 units, 1,533 with is_head_direction. All 1,533 are also\n    is_excitatory, so readings (a) and (b) give the same count; the code's drop of all-zero curves\n    removes none. The nine sessions with a wake_opto epoch (A1808, A1813, A1815, A1821, A1824,\n    A6211, A6215, A6216, A9701) are the nine +ogen.nwb files and hold 315 head-direction cells.\n    The four largest sessions are A3707 117, A3716 93, A3711 90 and A3706 86. Every file holds the\n    wake_square epoch, including the +ogen.nwb files, which settles the claims file's open\n    question.\n- claim: tuning-curves-match-cache\n  outcome: reproduced\n  notebook: tuning_curves.ipynb\n  output: claim:tuning-curves-match-cache\n  notes: The cache's session order, unit counts and three label columns equal the files'. All\n    1,533 recomputed partition-averaged curves correlate with the cached ones at r = 1.000000\n    (largest absolute difference 1.4e-14 Hz; plain curves identical). The chosen smoothing widths\n    are equal for both partitions in 78.4% of units (88.6% of partition curves); where they differ\n    the smoothed curves still agree to 2e-14 Hz, so the widths are ties (scipy's kernel is the\n    identity for the smallest widths, and the largest flatten the curve). The labels in the files\n    match the paper's per-unit table, and the dataset's measures match the cached values unit by\n    unit.\n  deviations:\n  - The held-out Poisson log-likelihood is computed from per-angle sums of counts and occupancy,\n    which leaves out the sum of log k!, a term that does not depend on the curve (hdring.py,\n    tuning_curves_session); the chosen curve is the same.\n- claim: fig1e-heterogeneous-peaks\n  outcome: reproduced\n  notebook: tuning_curves.ipynb\n  output: claim:fig1e-heterogeneous-peaks\n  notes: At zthresh 1 the curves have 1 to 6 peaks (1,121 with one, 357 with two, 48 with three,\n    5 with four, one each with five and six). The separation of the two highest peaks of the 412\n    multi-peaked curves runs from 0.13 to 3.14 rad, interquartile range 1.38 rad against pi/4\n    (0.79).\n- claim: fig5d-peak-numbers\n  outcome: reproduced\n  notebook: tuning_curves.ipynb\n  output: claim:fig5d-peak-numbers\n  measured:\n  - 1533\n  - 412\n  - 55\n  - 23908\n  - 1052\n  notes: The data counts (1,533, 412, 55) equal the paper's. Of 100,000 generative samples at the\n    paper's parameters, 23,908 have at least two peaks and 1,052 at least three under the claim's\n    seed; over the five seeds 23,908 to 24,267 and 1,001 to 1,082, all within tolerance.\n  deviations:\n  - Samples drawn from the claim's seed with numpy's Generator; the paper's notebook uses numpy\n    seed 42 with the legacy generator, whose draws are not repeated.\n- claim: fig1fg-mean-and-fluctuation-profiles\n  outcome: reproduced\n  notebook: tuning_curves.ipynb\n  output: claim:fig1fg-mean-and-fluctuation-profiles\n  notes: The mouse-average mean profile has one local maximum, at offset 0 (4.72), and correlates\n    with its reflection at r = 0.9998. The standard deviation profile peaks at 2.64, 0.56 times\n    the mean's peak and 0.56 times the mean at offset 0, so both readings of comparable hold.\n    The median correlation of a mouse's profile with the average is 0.996 for the mean (lowest\n    0.966) and 0.974 for the standard deviation (lowest 0.952).\n- claim: fig3ab-centers-of-mass-uniform\n  outcome: reproduced\n  notebook: tuning_curves.ipynb\n  output: claim:fig3ab-centers-of-mass-uniform\n  measured:\n  - 2\n  - 0\n  - 0.592\n  - 0.968\n  notes: Two sessions have uncorrected P < 0.05 (A3711, 0.044; A9701, 0.048); none is significant\n    after Benjamini-Hochberg correction; corrected P from 0.592 to 0.968, the paper's 0.59 to 0.97.\n- claim: fig3c-correlation-approaches-circulant\n  outcome: reproduced\n  notebook: tuning_curves.ipynb\n  output: claim:fig3c-correlation-approaches-circulant\n  notes: Mean relative distance from circulant form, 100 subsets per size, falls at every step from\n    5 to 80 neurons for all four mice and both functions (A3707, 0.73 to 0.27 raw and 0.71 to 0.16\n    centered and normalized; A3706, 0.77 to 0.33 and 0.73 to 0.19), under all five seeds (range at\n    80 neurons within 0.02 of the claim seed's). The leading four eigenvectors of each mouse's\n    full centered and normalized function hold 89% to 98% of their power at one frequency, the\n    first two at frequency 1 and the next two at frequency 2.\n- claim: fig4-generative-fit\n  outcome: partially_reproduced\n  notebook: tuning_curves.ipynb\n  output: claim:fig4-generative-fit\n  measured:\n  - 1.4737\n  - 3.1103\n  - 1.2145\n  notes: The final pass (500,000 samples) puts the minimum at sigma 1.4737, beta 3.1103, b 1.2145\n    under all five seeds (errors 0.0085 to 0.0089). Sigma and beta are within tolerance (beta by\n    0.34 of 0.345); b is 0.52 from 1.73, outside 0.173. The paper's grid point (sigma 1.4211, b\n    1.7307, beta 2.7659) is the minimum of the 25,000-sample shortlist pass (error 0.0061) and\n    second in the final pass (0.0095). In the float32 variant (draws and transform in float32, as\n    the paper's torch run) the paper's point has the lower error under the claim's seed (0.00902\n    against 0.00920) and the higher under the other four seeds. The error surface has two\n    near-equal minima along a ridge in b and beta, and which wins depends on the draws and the\n    arithmetic; the claims file's tolerance does not cover the second one.\n  deviations:\n  - The criterion asks for 500,000 samples at each of the 18,000 grid points, about 3 hours on\n    this runner. The whole grid was evaluated with 25,000 samples (the same draws at every point,\n    float32), and the 30 best points again with 500,000 fresh samples each (float64), which decide\n    the minimum.\n  - Draws from the claim's seed, not seed 42 on a CUDA device.\n- claim: fig5ab-profiles-match\n  outcome: reproduced\n  notebook: tuning_curves.ipynb\n  output: claim:fig5ab-profiles-match\n  notes: At the fitted parameters the generative mean profile is within the range of the 31 mouse\n    profiles at 100 of 100 offsets and the standard deviation profile at 97; the peaks are within\n    3.0% (4.57 against 4.72) and 1.3% (2.68 against 2.64) of the mouse-average peaks. Both\n    readings hold for both profiles under all five seeds. At the paper's parameters (variant),\n    100 and 100 offsets, peaks within 0.2% and 1.9%.\n  deviations:\n  - The generative parameters are those of fig4-generative-fit, which differ from the paper's in\n    b and beta; the paper's are shown as a variant and give the same outcome.\n- claim: fig5c-peak-counts-match\n  outcome: reproduced\n  notebook: tuning_curves.ipynb\n  output: claim:fig5c-peak-counts-match\n  notes: Total variation distance 0.022, 0.065 and 0.128 at zthresh 1, 0.5 and 0, Hellinger 0.061,\n    0.086 and 0.124; the distance at zthresh 1 is the smallest and below 0.15 under both readings\n    and all five seeds. At the paper's parameters 0.026, 0.040 and 0.105 (TV).\n- claim: fig5d-peak-heights-match\n  outcome: reproduced\n  notebook: tuning_curves.ipynb\n  output: claim:fig5d-peak-heights-match\n  notes: Under reading (a) the generative medians of the three highest peaks are within 0.8%, 1.5%\n    and 5.3% of the data medians (5.63, 2.90, 2.26). Under reading (b) the KS distances are 0.058,\n    0.054 and 0.186, so (b) holds for two of three peaks; the third rests on 55 data curves. The\n    same under all five seeds; at the paper's parameters the third peak is 8.8% and KS 0.253.\n- claim: fig5e-flip-symmetry-match\n  outcome: reproduced\n  notebook: tuning_curves.ipynb\n  output: claim:fig5e-flip-symmetry-match\n  notes: Data, 23.7% of curves below 0.5 (363) and 10.3% below 0 (158), median 0.927; generative,\n    28.1% and 11.8%, median 0.834; ratios 1.19 and 1.14, within the factor 1.5 under both readings\n    and all five seeds (1.17 to 1.19 and 1.13 to 1.16).\n- claim: fig5f-information-match\n  outcome: reproduced\n  notebook: tuning_curves.ipynb\n  output: claim:fig5f-information-match\n  notes: Median information 1.288 (data) and 1.368 (generative), 6.2% apart; KS 0.138; both\n    readings hold under all five seeds (KS 0.138 to 0.141). At the paper's parameters 4.3% and\n    0.109.\n- claim: fig2l-recorded-bump-tracks-hd\n  outcome: reproduced\n  notebook: tuning_curves.ipynb\n  output: claim:fig2l-recorded-bump-tracks-hd\n  notes: A3707, 117 cells, 18,030 bins of 100 ms of which 17,990 have tracked head direction.\n    Median absolute difference between the angle of the peak of m and the head direction 0.168\n    rad, below pi/8 (reading a); circular correlation 0.896, just below 0.9 (reading b fails).\n    With the head direction shifted by 60 s the median error is 1.294 rad. Curves of one partition\n    applied to the other's spikes give 0.172 and 0.177 rad (r 0.899 and 0.889).\n  deviations:\n  - The angle of a bin of m is its centre, (a + 0.5) 2 pi / 100, a standard choice that moves the\n    angle by 0.03 rad.\n- claim: fig2b-sorted-weights-mexican-hat\n  outcome: reproduced\n  notebook: network.ipynb\n  output: claim:fig2b-sorted-weights-mexican-hat\n  notes: The network built from these data gives the paper's printed reconstruction error\n    (1.715236380e-08 against 1.7152363819e-08). Sorted, the diagonal profile peaks at offset -8\n    (0.0053), stays positive up to N/20 (mean 0.0040), and is below its mean at 88% of the offsets\n    from N/8 to 3N/8 and below zero at 80% (minimum -0.00099 at offset 571). In arbitrary order\n    the profile is flat (sd 0.00015 against 0.00147). An aligned sorted row correlates with the\n    profile at 0.356 on average (0.026 in arbitrary order), which is the noise the claim names.\n  deviations:\n  - Near the diagonal is read as within N/20 neurons and intermediate offsets as N/8 to 3N/8, a\n    standard reading of the criterion's words.\n- claim: fig2ef-data-network-quasicontinuous\n  outcome: reproduced\n  notebook: network.ipynb\n  output: claim:fig2ef-data-network-quasicontinuous\n  notes: Median distance to the manifold 1.966 at 0 s, 0.0816 at 1 s (under one tenth, reading a)\n    and 0.00068 at 20 s; reading (b) fails because the distance keeps falling after 1 s (0.027 at\n    2 s, 0.0012 at 5 s). Every trajectory's manifold angle moves by less than 2 pi / 20 between 1 s\n    and 29.9 s (median 0.0025 rad, reading c), and the final angles occupy 77 of 100 bins (reading\n    d). Same outcome under all five seeds (70 to 77 bins).\n  deviations:\n  - Distance and angle read every 100 ms (the paper saves every 10 ms); the last state is at 29.9\n    s, as the paper's run_sim loop ends one step before T.\n  - Simulated in numpy float32 (the paper's torch float32).\n- claim: fig2gi-circulant-noise-collapses\n  outcome: partially_reproduced\n  notebook: network.ipynb\n  output: claim:fig2gi-circulant-noise-collapses\n  notes: The circulant plus scrambled residuals ends in 4 states under all three merging readings\n    (2 to 7 over five seeds; the symmetric version 2), and the circulant's 100 final states are\n    exact shifts (correlation 1.0000 with the best shift of the first). The sorted optimal matrix\n    keeps 24 (single linkage), 25 (greedy) or 31 (bins) states, short of 50. The position measure\n    the criterion fixes (peak neuron of the smoothed currents) gives only 24 to 33 states even for\n    the 100 initial states, so 50 is out of its reach; with the position read as the manifold angle\n    of the nearest target point (variant), the sorted matrix keeps all 50 bins at a median distance\n    of 0.0008 from the manifold, the circulant 47 and the circulant plus noise 7. The contrast\n    between the optimal matrix and the circulant plus noise holds, which the criterion rates\n    partial.\n  deviations:\n  - The criterion does not say how positions within 31 neurons are merged; single linkage,\n    greedy and bins were all run and give the same outcome.\n  - The residual shuffle and initial noise come from the claim's seed (numpy seed 42 in the\n    paper). The seed check reruns only the circulant plus noise matrix, the one with a random\n    construction.\n- claim: fig2jk-velocity-integration\n  outcome: reproduced\n  notebook: network.ipynb\n  output: claim:fig2jk-velocity-integration\n  notes: Over 20 to 110 s the peak of m follows the integrated constant input with a median error\n    of 0.011 rad (90th percentile 0.029) and circular correlation 1.000, and the integrated\n    angular velocity of A3707 (13.2 rad of net turning) with 0.013 rad and 1.000. Both readings\n    hold for both inputs. The inputs are deterministic; no seed is involved.\n  deviations:\n  - The two inputs run as two columns of one simulation, which changes nothing in the dynamics.\n- claim: figs14-data-spectrum-doublets\n  outcome: reproduced\n  notebook: network.ipynb\n  output: claim:figs14-data-spectrum-doublets\n  notes: The leading 10 eigenvalues have |Im| at most 6.8% of Re. Setting aside the fifth (1.0894,\n    the eigenvector closest to uniform), the gaps within the first four pairs (0.027, 0.000,\n    0.0002, 0.000) are each below the gap to the next pair (0.139, 0.183, 0.036, 0.0002); the first\n    pair (1.4384, 1.4113) is not exact. Without setting one aside, two of the four pairs pass.\n  deviations:\n  - The unpaired eigenvalue is identified as the one whose eigenvector overlaps most with the\n    uniform vector (the constant mode, as the criterion says), a standard choice.\n- claim: figs11b-data-network-global-stability\n  outcome: partially_reproduced\n  notebook: network.ipynb\n  output: claim:figs11b-data-network-global-stability\n  notes: From every initial spread (standard deviation 1 to 1,000) all 34 final states lie within\n    0.0016 of the manifold, against about 2 for the noisy starts of fig2ef, with none elsewhere,\n    and at standard deviation 1 all 34 end in one state (1.69 to 1.70 rad), under all five seeds.\n    Against the criterion's threshold, the largest distance at 20 s in fig2ef (0.00132), the\n    fraction within is 0.97, 0.94, 0.91, 0.97 and 0.94 at standard deviations 1, 10, 50, 100 and\n    1,000 under the claim's seed (0.91 to 1.00 over the five seeds), below the 95% asked at three\n    of five; against the median at 20 s (0.00068) 29% to 74%. Convergence to points on the\n    manifold and to one state from near the origin hold; the threshold test fails narrowly at\n    the resolution of the final distances (about 1e-3).\n- claim: figs8-s9-lambda-and-c\n  outcome: partially_reproduced\n  notebook: network_grid.ipynb\n  output: claim:figs8-s9-lambda-and-c\n  notes: At c 0 some runs diverge at every lambda up to 1e-4 (1 to 4 of 100) and, reading collapse\n    in the plane of the top two principal components (ii), 96 to 100 of 100 fall to the\n    homogeneous state (radius 0.65 to 0.80 against the manifold's 39.0) at every lambda; read as\n    the firing-rate norm (i) none collapses, as the homogeneous state keeps a norm of 17.3 to 17.7\n    against 72.5. No c above 0 diverges up to lambda 1e-4, and c 0.25 leaves the collapse (12 to\n    17 of 20 under ii). At lambda 1e-2 all runs with c up to 0.75 collapse (ii), but at c 1 the\n    states keep a radius of 4.6, just above the threshold of 3.9, so the criterion's test at c 1\n    fails under both readings. The flow error is 2.6e-9, 1.3e-10, 1.7e-8, 4.6e-6, 4.9e-4 and\n    2.1e-2 from lambda 1e-12 to 1e-2: it rises at both ends with its minimum at 1e-10, just\n    below 1e-8 as the supplement says, but 1e-8 is not below 1e-12, so that part of the\n    criterion fails. Two of the criterion's four parts hold. Seed check at four grid points: same\n    counts within 3 runs of 20.\n  deviations:\n  - 20 initial conditions at most grid points (every 500th target angle) and 100 at lambda 1e-12,\n    1e-8, 1e-4 and 1e-2 with c 0 and 1; the paper runs 100 everywhere.\n  - Divergence is a non-finite state or a firing-rate norm above 10 times the manifold's and still\n    growing over the last 5 s, a standard reading of the criterion's \"growing states\".\n  - Collapse was read two ways, the firing-rate norm and the radius in the principal-component\n    plane, as the criterion places the test in that plane; the outcome is the same.\n- claim: fig7-dmft-mexican-hat-and-stability\n  outcome: reproduced\n  notebook: theory.ipynb\n  output: claim:fig7-dmft-mexican-hat-and-stability\n  notes: All twelve profiles of Fig. 7a are positive at 0 (4.9 to 38.5) and negative at some\n    offset (minimum -1.5 to -6.0). On the 40 by 20 grid the bump's second eigenvalue is negative\n    everywhere (largest -4.7e-8) and the uniform state's leading eigenvalue is real (|Im| below\n    1e-16) and positive everywhere (smallest 4.7e-5). With Q fixed, the bump at sigma 1.4211 and\n    beta 2.7659 has eigenvalue 0.446. At 293 of 800 grid points, mostly small beta and large\n    sigma, no zero eigenvalue is found at the bump (the leading one is below -1e-6); the criterion\n    does not test this.\n- claim: fig7de-dmft-timescales\n  outcome: not_reproduced\n  notebook: theory.ipynb\n  output: claim:fig7de-dmft-timescales\n  notes: Convergence time (bump) falls with beta at every sigma and varies across sigma by at\n    most 2.55 times (reading b holds), but reaches 20.5 tau at beta 1.1 and sigma 100, outside 0.5\n    to 10 tau. Divergence time (uniform) runs from 0.15 to 3.83 tau for beta 1 to 10, rises with\n    beta at small sigma (up to 11 increases) and varies by up to 24 times across sigma. The first\n    two parts do not hold for both timescales, so neither the full nor the partial rule is met.\n    Over sigma 1 to 10 the timescales stay within a few tau; the failures come from the grid's\n    large sigma, which the claims file's thresholds include.\n- claim: fig7c-dmft-integrates-behavior\n  outcome: reproduced\n  notebook: theory.ipynb\n  output: claim:fig7c-dmft-integrates-behavior\n  notes: The peak of the mean-field bump follows the integrated angular velocity of A3707 over 20\n    to 110 s with a median error of 0.032 rad (90th percentile 0.10) and circular correlation\n    0.998, against 1.359 rad with the target shifted by 30 s; the bump keeps its contrast (0.75\n    to 0.73). Deterministic; no seed.\n- claim: fig6cd-eigenvalues-real-degenerate\n  outcome: reproduced\n  notebook: theory.ipynb\n  output: claim:fig6cd-eigenvalues-real-degenerate\n  seed_sensitive: true\n  notes: Under the claim's seed the leading 11 eigenvalues at N 2,500 are within 5.0% of alpha\n    Gamma_x_n / Gamma_phi_n (alpha 0.767), all with |Im| under 10% of Re, the first four pairs\n    closer within (0.023, 0, 0, 0.018) than to the next pair, and the ninth (0.181) is the\n    unpaired constant mode (theory 0.182, Fourier index 0). Over the five seeds the largest\n    difference from theory is 5.0%, 8.6%, 13.6%, 5.2% and 6.6%; one seed exceeds 10%.\n  deviations:\n  - Draws from the claim's seed (the paper's numpy seeds 42 and 45); the 50,000-curve theory\n    spectrum accumulated in chunks of 5,000.\n- claim: fig6fg-disordered-eigenvectors\n  outcome: reproduced\n  notebook: theory.ipynb\n  output: claim:fig6fg-disordered-eigenvectors\n  notes: Coefficient of variation of the radii in the planes of the two leading singular-vector\n    pairs, circulant plus noise 0.063 and 0.070 (rings), model 0.53 and 0.52 (structureless).\n    Both spectra show doublets in four of the four leading pairs, the unpaired eigenvalue ninth.\n    Same under all five seeds (circulant 0.063 to 0.072, model 0.516 to 0.534).\n  deviations:\n  - Pairs are consecutive singular vectors, skipping one whose overlap with the uniform vector\n    exceeds 0.5 (none among the leading five), a standard choice.\n- claim: fig8-grid-scores-and-torus\n  outcome: blocked\n  blocked_by: too_large\n  notes: Not started. The network of 25,000 neurons needs a 25,000 by 25,000 weight matrix (5 GB\n    in float64) fitted by regression and simulated, and the grid-score sweep 1,000 maps for each\n    eta; with the four notebooks of this entry taking 52 minutes per run and two full runs needed,\n    it did not fit in the five hours of the author run.\n- claim: figs10-robustness-comparable\n  outcome: blocked\n  blocked_by: too_large\n  notes: Not started. Two networks of 2,500 neurons, 34 initial conditions, 120 s at a 5-ms step\n    (24,000 steps) for each noise level; estimated at about 2 minutes per run on this runner from\n    the 1,533-neuron timings, so about 45 minutes for 11 levels, more than the run's time left.\n- claim: figs11-s12-global-stability-model\n  outcome: blocked\n  blocked_by: too_large\n  notes: Not started for lack of time in the author run (estimated 10 minutes of simulation for\n    N 2,500 at five initial spreads and N 50 to 1,000, plus a full re-run of the entry).\n- claim: figs1-s2-spectrum-does-not-fix-symmetry\n  outcome: blocked\n  blocked_by: too_large\n  notes: Not started for lack of time in the author run (rank-four networks of 10,000 neurons, two\n    ensembles, and their eigenvalues).\nfindings:\n- kind: other\n  about: data\n  severity: none\n  statement: At version 0.240528.1542, the version the paper cites, the 31 files hold what the paper\n    describes, one session per subject, 2,691 units of which 1,533 are labelled head-direction\n    (all also labelled excitatory), a wake_square epoch in every file, head direction in radians\n    sampled every 10 ms, and nine files with a wake_opto epoch holding 315 head-direction cells.\n    Tuning curves rebuilt from them match the paper's cached curves to 1e-14 Hz. Spikes and head\n    direction share a clock (in every session the head-direction information peaks within 0.05 s\n    of lag 0 and falls 4.5 times by 2 s), no recording appears twice, and no spike train is\n    unsorted.\n- kind: other\n  about: data\n  severity: none\n  statement: Every file was replaced after the cited version. In the latest published version,\n    0.261016.2310, the 31 assets have new names with session ids and sizes of 12.7 to 30.2 GB,\n    and none shares a blob with 0.240528.1542. The paper's code reads the cited version's file\n    names (sub-<id>_behavior+ecephys[+ogen].nwb); a user of a later version has to map the files.\n- kind: other\n  about: paper\n  statement: The generative fit of Fig. 4 has two near-equal minima on the paper's grid, (sigma, b,\n    beta) = (1.4211, 1.7307, 2.7659) and (1.4737, 1.2145, 3.1103), whose errors differ by less than\n    the sampling noise of 500,000 samples (0.0089 to 0.0095 depending on the draws and on float32\n    or float64 arithmetic). The reported b of 1.73 is one of two choices the fitting procedure\n    can return.\n- kind: other\n  about: paper\n  statement: In the mean-field stability grid of Fig. 7d,e (dmft.ipynb, run_analysis), at 293 of\n    the 800 grid points, mostly beta below 0.1 or sigma near 100, the bump Jacobian has no zero\n    eigenvalue (its leading eigenvalue is below -1e-6), so at those points the analytic bump\n    the code linearizes about does not show the symmetry-induced zero mode the Results describe.\n"
}
```

```
Thu Nov 26 14:32:47 UTC 2026
0 error(s)
Installed kernelspec registry-clark-2026 in executed/clark-2026/.venv/share/jupyter/kernels/registry-clark-2026
0 error(s)
pass  tuning_curves.ipynb  (971 s)
pass  network.ipynb  (1443 s)
pass  network_grid.ipynb  (541 s)
pass  theory.ipynb  (152 s)

real	51m53.682s
user	135m13.055s
sys	1m46.342s
Thu Nov 26 15:24:45 UTC 2026
```

```
File created successfully at: attempts/clark-2026-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
source /tmp/claude-1001/dev/bin/activate; for nb in tuning_curves network network_grid theory; do python /tmp/claude-1001/show.py executed/clark-2026/$nb.ipynb 2500 > /tmp/claude-1001/out_$nb.txt; done; grep -h "fitted (sigma\|float32 variant, seed 444120632\|circular correlation\|corrected P range\|data, at least\|seed 754901717\|interquartile\|ratio 0.56\|median r of mouse" /tmp/claude-1001/out_tuning_curves.txt; grep -h "sorted: states\|circ_plus_noise: states\|variant, position.*sorted\|constant 0.8\|A3707 behaviour\|seed 944155936\|seed 4133639115\|thresholds from" /tmp/claude-1001/out_network.txt | cut -c1-400; grep -h "flow error\|reading (\|no c above" /tmp/claude-1001/out_network_grid.txt; grep -h "relative difference\|median |peak\|293\|pair CVs" /tmp/claude-1001/out_theory.txt | head -4 | cut -c1-300
```

```
interquartile range 1.382 rad against pi/4 = 0.785
data, at least 1, 2, 3 peaks: [np.int64(1533), np.int64(412), np.int64(55)] (expected 1533, 412, 55)
seed 754901717: generative, at least 1, 2, 3 peaks of 100,000: [np.int64(100000), np.int64(23908), np.int64(1052)] (expected 100000, 24271, 1043)
peak of sd profile 2.643, peak of mean profile 4.716, ratio 0.560; reading (a) holds: True
at offset 0: sd 2.643, mean 4.716, ratio 0.560; reading (b) holds: True
consistency: median r of mouse mean profiles with the average 0.996 (min 0.966); of sd profiles 0.974 (min 0.952)
corrected P range 0.592 to 0.968 (expected 0.59 to 0.97); uncorrected 0.044 to 0.968
fitted (sigma, beta, b) = (1.4737, 3.1103, 1.2145); expected (1.42 +- 0.142, 2.77 +- 0.345, 1.73 +- 0.173)
float32 variant, seed 444120632: error at the best point 0.00920, at the paper's grid point 0.00902
median |peak of m - head direction| = 0.168 rad (pi/8 = 0.393); circular correlation 0.896 (>= 0.9)
seed 944155936: median distance at 0 s 1.9661, 1 s 0.08163, 20 s 0.00068, 29.90 s 0.00062; (a) True (b) False; angle moved under 2pi/20 between 1 s and the end: 1.00 (c) True; final angles in 77 of 100 bins (d) True; median movement 0.0025 rad
sorted: states single 24, greedy 25, bins 31; distinct peak neurons 41; peak height range 7.84 to 11.49
circ_plus_noise: states single 4, greedy 4, bins 4; distinct peak neurons 6; peak height range 5.86 to 6.35
variant, position as the manifold angle of the nearest target point: sorted: states single 1, greedy 37, bins of 2 pi / 50 50; median distance to the manifold 0.0008
variant, position as the manifold angle of the nearest target point: circ_plus_noise: states single 5, greedy 6, bins of 2 pi / 50 7; median distance to the manifold 1.1143
constant 0.8 rad/s: 9000 samples from 20 to 109.99 s; median |error| 0.011 rad (pi/8 0.393), 90th percentile 0.029; circular r 1.000; mean offset -0.008 rad, median |error| after removing it 0.009; total turn of target 72.0 rad
A3707 beha
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
grep -h "flow error\|reading (\|no c above\|seed 1787" /tmp/claude-1001/out_network_grid.txt | cut -c1-400; wc -l /tmp/claude-1001/out_network_grid.txt; cd  && python tools/entry.py check entries/clark-2026 2>&1 | tail -5
```

```
47 /tmp/claude-1001/out_network_grid.txt
error: attempts/clark-2026-01.yaml: not valid YAML: mapping values are not allowed in this context
  in "<unicode string>", line 290, column 37
1 error(s)
```

**Agent calls Bash**

```bash
sed -n 288,292p attempts/clark-2026-01.yaml; sed -n 1,47p /tmp/claude-1001/out_network_grid.txt | tail -12 | cut -c1-300
```

```
states keep a radius of 4.6, just above the threshold of 3.9, so the criterion's test at c 1
    fails under both readings. The flow error is 2.6e-9, 1.3e-10, 1.7e-8, 4.6e-6, 4.9e-4 and
    2.1e-2 from lambda 1e-12 to 1e-2: it rises at both ends with its minimum at 1e-10, just
    below 1e-8 as the supplement says, but 1e-8 is not below 1e-12, so that part of the
    criterion fails. Two of the criterion's four parts hold. Seed check at four grid points: same
1.000000e-08 1.50        0         0            0  20 72.194552      38.982458
1.000000e-06 0.00        3         0           17  20 17.408164       0.789021
1.000000e-06 0.25        0         0           12  20 21.450442       1.531747
1.000000e-06 0.50        0         0            0  20 72.193118      38.958084
1.000000e-06 0.75        0         0            0  20 72.180951      38.954600
1.000000e-06 1.00        0         0            0  20 72.177212      38.953110
1.000000e-06 1.25        0         0            0  20 72.175360      38.952310
1.000000e-06 1.50        0         0            0  20 72.174293      38.951872
1.000000e-04 0.00        1         0           99
===== [] print(f"total time {time.time()-T0:.0f} s; peak memory {reso
total time 539 s; peak memory 1.55 GB
```

**Agent calls Bash**

```bash
sed -i 's/2.1e-2 from lambda 1e-12 to 1e-2: it rises/2.1e-2 from lambda 1e-12 to 1e-2; it rises/' attempts/clark-2026-01.yaml && grep -n "[a-z0-9)]: " attempts/clark-2026-01.yaml | grep -v "^[0-9]*:\s*-\? \?[a-z_]*: " | head; python tools/entry.py check entries/clark-2026 2>&1 | tail -5; source /tmp/claude-1001/dev/bin/activate; python /tmp/claude-1001/show.py executed/clark-2026/network_grid.ipynb 9000 | grep "flow error\|reading (\|no c above\|seed 1787" | cut -c1-330
```

```
292:    criterion fails. Two of the criterion's four parts hold. Seed check at four grid points: same
error: attempts/clark-2026-01.yaml: not valid YAML: mapping values are not allowed in this context
  in "<unicode string>", line 292, column 92
1 error(s)
flow error (mean squared flow on the manifold) by lambda: {'1e-12': '2.646e-09', '1e-10': '1.346e-10', '1e-08': '1.715e-08', '1e-06': '4.643e-06', '0.0001': '4.872e-04', '0.01': '2.084e-02'}
reading (i) firing-rate norm: c 0 gives divergence or collapse at every lambda False, at some lambda True; lambda 1e-2 collapses at c 1: False; collapse at c 0.25, lambda 1e-8: [[0, 20]]
reading (ii) PC-plane radius: c 0 gives divergence or collapse at every lambda True, at some lambda True; lambda 1e-2 collapses at c 1: False; collapse at c 0.25, lambda 1e-8: [[12, 20]]
no c above 0 diverges at any lambda up to 1e-4: True
flow error at 1e-8 below that at 1e-2 and at 1e-12: False | lambda of the minimum flow error: 1e-10
seed 1787312230: lambda 1e-08 c 0: diverge 3, collapse (i) 0, (ii) 17 of 20; lambda 1e-08 c 1.0: diverge 0, collapse (i) 0, (ii) 0 of 20; lambda 0.01 c 1.0: diverge 0, collapse (i) 0, (ii) 0 of 20; lambda 0.0001 c 0.25: diverge 0, collapse (i) 0, (ii) 18 of 20
seed 1787313230: lambda 1e-08 c 0: diverge 1, collapse (i) 0, (ii) 19 of 20; lambda 1e-08 c 1.0: diverge 0, collapse (i) 0, (ii) 0 of 20; lambda 0.01 c 1.0: diverge 0, collapse (i) 0, (ii) 0 of 20; lambda 0.0001 c 0.25: diverge 0, collapse (i) 0, (ii) 19 of 20
seed 1787314230: lambda 1e-08 c 0: diverge 1, collapse (i) 0, (ii) 19 of 20; lambda 1e-08 c 1.0: diverge 0, collapse (i) 0, (ii) 0 of 20; lambda 0.01 c 1.0: diverge 0, collapse (i) 0, (ii) 0 of 20; lambda 0.0001 c 0.25: diverge 0, collapse (i) 0, (ii) 18 of 20
seed 1787315230: lambda 1e-08 c 0: diverge 0, collapse (i) 0, (ii) 20 of 20; lambda 1e-08 c 1.0: diverge 0, collapse (i) 0, (ii) 0 of 20; lambda 0.01 c 1.0: diverge 0, collapse (i) 0, (ii) 0 of 20; lambda 0.0001 c 0.25: diverge 0, collapse (i
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='attempts/clark-2026-01.yaml'
s=open(p).read()
old="""criterion fails. Two of the criterion's four parts hold. Seed check at four grid points: same
    counts within 3 runs of 20."""
new="""criterion fails. Two of the criterion's four parts hold. Under four more seeds (20 initial
    conditions) the points the criterion reads give the same pattern (lambda 1e-8 and c 0, 0 to 3
    diverge and 17 to 20 collapse under ii; lambda 1e-2 and c 1, none collapses)."""
assert old in s; s=s.replace(old,new)
old="and c 0.25 leaves the collapse (12 to\n    17 of 20 under ii)."
assert old in s
s=s.replace(old,"and c 0.25 leaves the collapse (8 to\n    20 of 20 across lambda under ii, 12 at 1e-8).")
open(p,'w').write(s)
import yaml; yaml.safe_load(s); print('yaml ok')
EOF
python tools/entry.py check entries/clark-2026 2>&1 | tail -5; date -u
```

```
yaml ok
0 error(s)
Thu Nov 26 15:25:32 UTC 2026
```

**Agent calls Bash**

```bash
python tools/entry.py handover entries/clark-2026 2>&1 | tail -8; ls executed/clark-2026/handover/; git status --short | grep -v "^ M tools\|^?? tools\|^?? docs" | head -20
```

```
wrote executed/clark-2026/handover
clark-2026.yaml
hdring.py
network.ipynb
network_grid.ipynb
ring_dmft.py
theory.ipynb
tuning_curves.ipynb
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
?? attempts/clark-2026-01.yaml
?? entries/clark-2026/
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
ls -la entries/clark-2026/; git check-ignore -q executed && echo "executed ignored"; date -u
```

```
total 384
drwxr-xr-x   4 runner runner   4096 Nov 26 14:32 .
drwxr-xr-x 332 runner runner  16384 Nov 26 12:02 ..
drwxr-xr-x   3 runner runner   4096 Nov 26 12:27 .claude
-rw-r--r--   1 runner runner   3250 Nov 26 14:32 README.md
drwxr-xr-x   2 runner runner   4096 Nov 26 13:38 __pycache__
-rw-r--r--   1 runner runner   1360 Nov 26 12:43 entry.yaml
-rw-r--r--   1 runner runner  22210 Nov 26 13:38 hdring.py
-rw-r--r--   1 runner runner  32164 Nov 26 14:32 network.ipynb
-rw-r--r--   1 runner runner  10308 Nov 26 14:32 network_grid.ipynb
-rw-r--r--   1 runner runner     97 Nov 26 12:43 requirements.in
-rw-r--r--   1 runner runner 180404 Nov 26 12:43 requirements.lock.txt
-rw-r--r--   1 runner runner  15966 Nov 26 12:38 ring_dmft.py
-rw-r--r--   1 runner runner  23846 Nov 26 14:32 theory.ipynb
-rw-r--r--   1 runner runner  56449 Nov 26 14:32 tuning_curves.ipynb
executed ignored
Thu Nov 26 15:25:54 UTC 2026
```

**Agent calls Bash**

```bash
find entries/clark-2026/.claude -type f | head; git check-ignore -v entries/clark-2026/.claude entries/clark-2026/__pycache__ 2>&1 | head
```

```
.gitignore:1:__pycache__/	entries/clark-2026/__pycache__
```

**Agent calls Bash**

```bash
find entries/clark-2026/.claude -depth -type d -empty -delete; ls -a entries/clark-2026 | head -3; python tools/entry.py check entries/clark-2026 2>&1 | tail -1
```

```
.
..
README.md
0 error(s)
```

**Agent**

I've built the entry `entries/clark-2026` (four notebooks, two helpers), written `attempts/clark-2026-01.yaml` and built the handover package. `python tools/entry.py all` passed, `check` reports 0 errors, and nothing is committed.

## 1. Outcomes

| claim | outcome |
|---|---|
| hd-cell-selection (link) | reproduced: all counts exact (31, 2,691, 1,533, 315, 117/93/90/86) |
| tuning-curves-match-cache (link, uses the Zenodo cache) | reproduced: r = 1.000000 on all 1,533 curves |
| fig1e-heterogeneous-peaks | reproduced |
| fig5d-peak-numbers | reproduced: data counts exact |
| fig1fg-mean-and-fluctuation-profiles | reproduced |
| fig3ab-centers-of-mass-uniform | reproduced: 2 sessions, 0 after correction, corrected P 0.592 to 0.968 |
| fig3c-correlation-approaches-circulant | reproduced |
| fig4-generative-fit | partially reproduced: (σ, β, b) = (1.474, 3.110, 1.215), b is outside tolerance |
| fig5ab, fig5c, fig5d-peak-heights, fig5e, fig5f | reproduced (5 claims) |
| fig2l-recorded-bump-tracks-hd | reproduced under reading (a); circular r is 0.896, just under the 0.9 of reading (b) |
| fig2b-sorted-weights-mexican-hat | reproduced |
| fig2ef-data-network-quasicontinuous | reproduced |
| fig2gi-circulant-noise-collapses | partially reproduced |
| fig2jk-velocity-integration | reproduced |
| figs14-data-spectrum-doublets | reproduced |
| figs11b-data-network-global-stability | partially reproduced |
| figs8-s9-lambda-and-c | partially reproduced |
| fig7-dmft-mexican-hat-and-stability (elsewhere) | reproduced |
| fig7de-dmft-timescales (elsewhere) | not reproduced, by the claims file's thresholds |
| fig7c-dmft-integrates-behavior | reproduced |
| fig6cd-eigenvalues-real-degenerate (elsewhere) | reproduced; seed sensitive (1 of 5 seeds is 13.6% off) |
| fig6fg-disordered-eigenvectors (elsewhere) | reproduced |
| fig8, figs10, figs11-s12, figs1-s2 (elsewhere) | blocked, `too_large`: not started for lack of time |

## 2. Dataset, assumptions, questions

- **Version pinned.** 0.240528.1542, the version the paper cites. Every file was replaced in later versions (new names, 12.7 to 30.2 GB each, no file shared), so the paper's code only fits the cited one.
- **The files match the paper.**
  - All 1,533 head-direction units are also labelled excitatory.
  - Every file, including the `+ogen.nwb` ones, holds the `wake_square` epoch. That answers the claims file's open question.
  - Spikes and head direction share a clock: in all 31 sessions the information peaks within 0.05 s of lag 0.
  - No recording appears twice.
  - The rebuilt tuning curves match the paper's cache to 1e-14 Hz, and my network gives the paper's printed reconstruction error (1.7152e-08).
- **Findings about the paper.**
  - The Fig. 4 fit has two near-equal minima on the grid: the paper's point and (1.47, 1.21, 3.11). Which one wins depends on the random draws and on float32 versus float64.
  - At 293 of the 800 grid points of the mean-field stability analysis, the bump has no zero eigenvalue.
- **Assumptions and reader questions.** I made no assumptions, so no outcome is marked `assumed`, and I asked a reader nothing.

## 3. Protocol points

1. The claims file names "numpy seed 42", but the protocol requires seeds from crc32 of the claim id. I used the protocol's seeds and recorded it as a deviation.
2. The fig4 criterion asks for 500,000 samples at all 18,000 grid points, about 3 hours here. The protocol has no rule for a criterion that is too costly to run as written. I ran the whole grid at 25,000 samples, then the best 30 points at 500,000, and recorded the deviation.
3. The fig2gi criterion asks for at least 50 states, which its own position measure cannot reach (the starting states alone give 24 to 33). The protocol handles ties, not thresholds that cannot be met. I applied it as written and showed a variant measure.
4. The run stamp hashes every file in the entry, so writing conclusions or the README after a run makes the next run a full one (52 min here). Writing results from outputs therefore costs two full runs. The protocol does not mention this.
5. `data: elsewhere` is defined for data deposited in another archive. It fits poorly for claims that are pure simulation with no data. I treated the paper's code at its commit as the input.
6. For claims never started because time ran out, the protocol only names `too_large` "where the computation stopped it". I used `too_large` with cost estimates.
7. The criteria leave "collapse" (figs8-s9) and "merged into one state" (fig2gi) open. I ran every reading; the outcome is the same under each.

## 4. Runtime and failures

- The entry takes about 52 minutes per run: 16, 24, 9 and 2.5 minutes for the four notebooks; peak memory 1.7 GB. I ran it in full three times.
- The second run was needed because my first distance computation, in float32, rounded distances below about 1e-3 to zero. That changed two numbers the criteria read, so I fixed it and reran.
- Nothing failed in the final run. The run ended at 15:25 UTC.

## End of run

89 turns, 208 minutes, $9.96 at API prices, result: success.
