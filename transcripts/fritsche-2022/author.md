# fritsche-2022 · author · run 44870457733

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cd  ls; cat docs/protocol.md; wc -c README.md docs/*.md
```

```
<persisted-output>
Output too large (47.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/608c7f18-d957-4533-9fe5-a8cc5e876afc/tool-results/bzbodv2cp.txt

Preview (first 2KB):
Sat Nov 21 05:26:18 UTC 2026
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
[... 46 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/608c7f18-d957-4533-9fe5-a8cc5e876afc/tool-results/bzbodv2cp.txt"
}
```

```
1	Sat Nov 21 05:26:18 UTC 2026
2	LICENSE
3	LICENSE-data
4	README.md
5	attempts
6	bunfig.toml
7	claims
8	docs
9	encore_science
10	entries
11	n-desk.png
12	n-phone.png
13	n-phone2.png
14	node_modules
15	ov-papers-rows.png
16	package-lock.json
17	package.json
18	paper
19	papers
20	pnpm-lock.yaml
[... 807 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md docs/design.md; grep -n "DANDI" -A3 docs/archives.md | head -50
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
[... 445 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat claims/fritsche-2022.yaml; ls paper/ entries/fouke-2025; cat papers/datasets/fritsche-2022.yaml; ls papers/author-notes/ | grep fritsche; ls questions | grep fritsche
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/608c7f18-d957-4533-9fe5-a8cc5e876afc/tool-results/bt3i815uz.txt"
}
```

```
1	# Claims for Fritsche, Solomon & de Lange (2022), "Brief Stimuli Cast a Persistent Long-Term Trace
2	# in Visual Cortex", J Neurosci 42(10):1999-2010, doi:10.1523/JNEUROSCI.1350-21.2021, on dandiset
3	# 000021 (Allen Institute, Visual Coding, Neuropixels, Brain Observatory 1.1 Stimulus Set), which the
4	# paper reuses.
5	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-21,
6	# protocol as stated in docs/protocol.md (pilot-18).
7	#
8	# Text read. The version of record, full text from PubMed Central (PMC8916757), in
9	# paper/10.1523-jneurosci.1350-21.2021.txt: abstract, Introduction, Materials and Methods, Results,
10	# Discussion, the legends of Figures 1 to 8 and Tables 1 and 2. The paper has no supplement. The
11	# extracted text drops the display equations; these were read from the MathML of the same PMC page
12	# (pmc.ncbi.nlm.nih.gov/articles/PMC8916757). They are (1) adaptation ratio = fr_repeat /
13	# fr_orthogonal; (2) the double exponential, printed as r(n) = 1 - a_fast * exp(-(n-1)/tau_fast) +
14	# a_slow * exp(-(n-1)/tau_slow); (3) the single exponential r(n) = 1 - a * exp(-(n-1)/tau); (4) OSI =
15	# (fr_preferred - fr_non-preferred) / (fr_preferred + fr_non-preferred); (5) the cumulative ratio of
16	# Fig. 4, ar_2-8 = product over n = 2 to 8 of ar_n. Figures were not opened (there is no PDF under
17	# paper/); no number below is read from a figure.
18	#
19	# Code. The paper links its analysis code at the Donders Repository, doi:10.34973/kpt9-y956
20	# (collection DSC_3018000.01_830, version 1). Its file list can be read without a login. It holds
[... 872 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -c paper/*; grep -n -i "Materials and Methods" paper/*.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 434,520p paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 170,222p paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 224,241p paper/*.txt; sed -n 243,300p paper/*.txt | cut -c1-3000
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 300,340p paper/*.txt | cut -c1-2500
```

Result: not kept, because it reads the paper's text.

**Agent**

Now the format examples.

**Agent calls Bash**

```bash
cd  cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in entries/fouke-2025/README.md; cat attempts/fouke-2025-01.yaml | head -150
```

```
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
helpers:
- omr.py
related:
- id: dandi:001453/0.250518.1950
  relation: uses_data
- id: doi:10.1016/j.cub.2025.04.027
[... 193 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 150,400p attempts/fouke-2025-01.yaml | grep -v "^    " | head -80; grep -n "findings:" -A40 attempts/fouke-2025-01.yaml | head -60; ls schemas; ls entries | head -50
```

```
outcome: not_reproduced
  notebook: reproduce_fouke_2025.ipynb
  output: claim:fig1h-zf-higher-angular-acceleration
  notes: With angular acceleration as the Methods define it, DC are higher than ZF for all nine
  deviations:
  - Follows the Methods' definition (degrees per second squared) on heading resampled to 30 Hz;
  - Heading is taken from the cumulative sum of `f0_vtheta`, as the code does; in DC files it does
- claim: figs1e-dc-respond-less-monocular
  outcome: reproduced
  notebook: reproduce_fouke_2025.ipynb
  output: claim:figs1e-dc-respond-less-monocular
  notes: Species effect F = 23.3, p = 2.5e-06. DC turn less toward the stimulus than ZF for
  deviations:
  - Codes 9 and 11 are assigned as the figure code has them; the stimulus software's conversion
- claim: fig1c-continuous-vs-bouts
  outcome: reproduced
  notebook: reproduce_fouke_2025.ipynb
  output: claim:fig1c-continuous-vs-bouts
  notes: The median-to-mean ratio of instantaneous speed is 0.306 in ZF (25 fish, 0.244 to 0.580)
  deviations:
[... 174 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/000021/ | python -m json.tool | head -40; curl -s https://api.dandiarchive.org/api/dandisets/000021/versions/ | python -m json.tool | head -60
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; python - <<'EOF'
import json,urllib.request
url="https://api.dandiarchive.org/api/dandisets/000021/versions/0.251116.2246/assets/?page_size=500"
out=[]
while url:
    d=json.load(urllib.request.urlopen(url)); out+=d['results']; url=d['next']
json.dump(out,open('assets21.json','w'))
print(len(out))
main=[a for a in out if '_probe-' not in a['path']]
print(len(main))
for a in sorted(main,key=lambda a:a['path']): print(a['path'], round(a['size']/1e9,2), a['asset_id'])
print([a['path'] for a in out if '_probe-' in a['path']][:3])
EOF
```

```
214
32
sub-699733573/sub-699733573_ses-715093703.nwb 2.86 58703c97-c0a9-4736-b684-73c85c1a444a
sub-703279277/sub-703279277_ses-719161530.nwb 3.07 02291b99-e583-498b-9929-b68bba2c50e2
sub-707296975/sub-707296975_ses-721123822.nwb 1.74 224b57e5-c9a3-46ef-85db-966713f3ccbe
sub-716813540/sub-716813540_ses-739448407.nwb 2.16 c7f32379-adce-4961-9211-d07790be9cab
sub-717038285/sub-717038285_ses-732592105.nwb 2.91 b4aeeb19-cdc6-4895-ab7b-bc8a688cf6f5
sub-718643564/sub-718643564_ses-737581020.nwb 2.18 106e84a7-1c41-43f1-a675-7df17e4aba69
sub-719817799/sub-719817799_ses-744228101.nwb 2.65 eb36f94f-d6e7-45c6-aa02-7d4ed23453d3
sub-719828686/sub-719828686_ses-754312389.nwb 1.86 5a58bf3d-a1b9-444b-8ab0-ef5478aa42a6
sub-722882751/sub-722882751_ses-743475441.nwb 2.12 522e8054-34ca-4579-ae80-350d0b24e0f4
sub-723627600/sub-723627600_ses-742951821.nwb 2.92 96c200cf-29c2-457a-b2f3-99f11de5b039
sub-726141242/sub-726141242_ses-750332458.nwb 3.24 286c7b06-3cde-4261-9090-e6fbe6c81945
sub-726162193/sub-726162193_ses-750749662.nwb 2.82 3876c5f1-f38a-4c89-8f54-6128538f0066
sub-726170927/sub-726170927_ses-746083955.nwb 2.56 2e6df882-f31a-440b-a572-ba717a95bf80
sub-726298249/sub-726298249_ses-754829445.nwb 2.7 488a9bea-96fb-4028-a33a-08650f50be63
sub-730756767/sub-730756767_ses-757970808.nwb 2.38 dfc3db15-066a-4a07-b615-a4d7e85c44e1
sub-730760263/sub-730760263_ses-755434585.nwb 2.24 edf10182-5a4c-454f-ad23-47987a5ca256
sub-732548371/sub-732548371_ses-751348571.nwb 3.07 be9f8fd8-8f16-4a66-acc6-9e04697650f3
sub-733457986/sub-733457986_ses-757216464.nwb 3.04 5f204c90-2005-4143-b880-07d80aa32b20
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "import h5py, remfile, numpy, scipy, pandas; print('ok')"; which python; ls tools; nproc; free -g
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import h5py, remfile, numpy, scipy, pandas; print('ok')
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'h5py'
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
__pycache__
agent_run.py
archive_transcripts.sh
archives
author_notes.py
authors.py
backfill_summaries.py
blind.sh
build_dryad_targets.py
build_figshare_targets.py
build_openneuro_targets.py
build_reuse_targets.py
build_site.py
build_sparc_targets.py
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && source dev/bin/activate && uv pip install -q h5py remfile numpy scipy pandas statsmodels matplotlib pingouin pynwb 2>&1 | tail -3; python -c "import h5py, remfile; print(h5py.__version__)"
```

```
3.16.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && cat > explore.py <<'EOF'
import h5py, remfile, json, time
t=time.time()
aid="58703c97-c0a9-4736-b684-73c85c1a444a"
url=f"https://api.dandiarchive.org/api/assets/{aid}/download/"
import urllib.request
req=urllib.request.Request(url,method='HEAD')
r=urllib.request.urlopen(req); s3=r.geturl(); print(s3[:100])
f=h5py.File(remfile.File(s3),'r')
def show(name,obj):
    if isinstance(obj,h5py.Dataset): print(name, obj.shape, obj.dtype)
    else: print(name+'/')
for k in f.keys():
    if k in ('acquisition','processing'):
        print(k, list(f[k].keys()))
        continue
f['units'].visititems(show)
print(list(f['intervals'].keys()))
for k in f['intervals']:
    if 'drifting' in k or 'static' in k or 'spontaneous' in k:
        print(k, [(c, f['intervals'][k][c].shape) for c in f['intervals'][k].keys()])
f['general'].visititems(lambda n,o: print(n, o[()] if isinstance(o,h5py.Dataset) and o.size<5 else getattr(o,'shape','')))
print(time.time()-t)
EOF
python explore.py 2>&1 | head -200
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/explore.py", line 7, in <module>
    r=urllib.request.urlopen(req); s3=r.geturl(); print(s3[:100])
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/urllib/request.py", line 189, in urlopen
    return opener.open(url, data, timeout)
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/urllib/request.py", line 495, in open
    response = meth(req, response)
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/urllib/request.py", line 604, in http_response
    response = self.parent.error(
        'http', request, response, code, msg, hdrs)
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/urllib/request.py", line 527, in error
    result = self._call_chain(*args)
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/urllib/request.py", line 466, in _call_chain
    result = func(*args)
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/urllib/request.py", line 720, in http_error_302
    return self.parent.open(new, timeout=req.timeout)
           ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/urllib/request.py", line 495, in open
    response = meth(req, response)
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && sed -n 25,36p ~/work/encore/encore/docs/archives.md; python - <<'EOF'
import json,urllib.request
d=json.load(urllib.request.urlopen("https://api.dandiarchive.org/api/dandisets/000021/versions/0.251116.2246/assets/58703c97-c0a9-4736-b684-73c85c1a444a/"))
print(d['contentUrl']); print({k:d[k] for k in d if k in ('wasAttributedTo','variableMeasured')})
EOF
```

```
- **Reading.** List the assets and read metadata with the DANDI REST API
  (`https://api.dandiarchive.org/api/dandisets/<id>/versions/<version>/` and its
  `assets/` endpoint). Read NWB files by streaming them: open each asset's S3
  URL with `remfile` and `h5py`, and read it with `pynwb`. Do not download files
  to disk.
- **In an entry.** The entry names the dataset as `dandi:<id>/<version>` under
  `related`. The helper module keeps the version in one constant.

## CRCNS

- **Datasets.** A CRCNS data set, identified by its short name (`ret-1`,
  `hc-3`), with a DOI of its own (`10.6080/...`). The registry's list is
['https://api.dandiarchive.org/api/assets/58703c97-c0a9-4736-b684-73c85c1a444a/download/', 'https://dandiarchive.s3.amazonaws.com/blobs/f5f/175/f5f1752f-5227-47d5-8f75-cd71937878aa']
{'wasAttributedTo': [{'age': {'value': 'P118D', 'unitText': 'ISO-8601 duration', 'schemaKey': 'PropertyValue'}, 'sex': {'name': 'Male', 'schemaKey': 'SexType', 'identifier': 'http://purl.obolibrary.org/obo/PATO_0000384'}, 'species': {'name': 'House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}, 'genotype': 'Sst-IRES-Cre/wt;Ai32(RCL-ChR2(H134R)_EYFP)/wt', 'schemaKey': 'Participant', 'identifier': '699733573'}], 'variableMeasured': [{'value': 'Units', 'schemaKey': 'PropertyValue'}]}
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && sed -i 's|^req=.*|s3="https://dandiarchive.s3.amazonaws.com/blobs/f5f/175/f5f1752f-5227-47d5-8f75-cd71937878aa"|; s|^r=urllib.*||' explore.py && python explore.py 2>&1 | head -250
```

```
acquisition ['raw_running_wheel_rotation', 'running_wheel_signal_voltage', 'running_wheel_supply_voltage']
processing ['eye_tracking_rig_metadata', 'optotagging', 'running', 'stimulus']
PT_ratio (2779,) float64
amplitude (2779,) float64
amplitude_cutoff (2779,) float64
cluster_id (2779,) int64
cumulative_drift (2779,) float64
d_prime (2779,) float64
firing_rate (2779,) float64
id (2779,) int64
isi_violations (2779,) float64
isolation_distance (2779,) float64
l_ratio (2779,) float64
local_index (2779,) int64
max_drift (2779,) float64
nn_hit_rate (2779,) float64
nn_miss_rate (2779,) float64
peak_channel_id (2779,) int64
presence_ratio (2779,) float64
quality (2779,) object
[... 59 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && cat > ex2.py <<'EOF'
import h5py, remfile, time, numpy as np, pandas as pd
s3="https://dandiarchive.s3.amazonaws.com/blobs/f5f/175/f5f1752f-5227-47d5-8f75-cd71937878aa"
f=h5py.File(remfile.File(s3),'r')
st=f['units/spike_times']; print(st.chunks, st.compression)
u=f['units']
df=pd.DataFrame({k:u[k][:] for k in ['id','isi_violations','amplitude_cutoff','presence_ratio','peak_channel_id','firing_rate','spike_times_index']})
e=f['general/extracellular_ephys/electrodes']
el=pd.Series(e['location'][:].astype(str), index=e['id'][:])
df['loc']=el.loc[df.peak_channel_id].values
q=(df.isi_violations<=0.5)&(df.amplitude_cutoff<=0.1)&(df.presence_ratio>=0.9)
print(len(df), q.sum()); print(df[q]['loc'].value_counts())
print(u['quality'][:5])
dg=f['intervals/drifting_gratings_presentations']
d=pd.DataFrame({k:dg[k][:] for k in ['start_time','stop_time','orientation','temporal_frequency','stimulus_block','contrast']})
print(d.head(10)); print(d.orientation.value_counts(dropna=False)); print(d.stimulus_block.value_counts())
print(d.contrast.value_counts(dropna=False))
print(dg['stimulus_name'][:3], dg['orientation'].attrs.items())
sg=f['intervals/static_gratings_presentations']
s=pd.DataFrame({k:sg[k][:] for k in ['start_time','stop_time','orientation','spatial_frequency','phase','stimulus_block']})
print(s.head()); print(s.orientation.value_counts(dropna=False)); print(s.stimulus_block.value_counts()); print(np.diff(s.start_time).min(), np.median(np.diff(s.start_time)), np.diff(s.start_time).max())
sp=f['intervals/spontaneous_presentations']; print(sp['start_time'][:], sp['stop_time'][:])
# time read
t=time.time(); x=st[0:5_000_000]; print('5M read', time.time()-t)
EOF
python ex2.py
```

```
None None
2779 993
loc
CA1      177
LP       152
grey     124
PO        89
VISrl     87
LGd       84
VISp      62
VISpm     53
VISl      50
DG        34
VISam     34
APN       29
CA3       17
PoT        1
Name: count, dtype: int64
[b'good' b'good' b'good' b'good' b'good']
    start_time    stop_time  ...  stimulus_block  contrast
[... 63 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && source dev/bin/activate && python -c "import remfile,inspect; print(inspect.signature(remfile.File.__init__))"
```

```
Sat Nov 21 05:28:30 UTC 2026
(self, url: Union[str, Any], *, verbose: bool = False, disk_cache: Optional[remfile.DiskCache.DiskCache] = None, timeout: Union[float, Tuple[float, float], NoneType] = (30, 60), _min_chunk_size: int = 102400, _max_cache_size: int = 1000000000.0, _chunk_increment_factor: int = 1.7, _bytes_per_thread: int = 4194304, _max_threads: int = 1, _max_chunk_size: int = 104857600, _impose_request_failures_for_testing: bool = False, _size: Optional[int] = None, _use_session: bool = True)
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "entries/fritsche-2022/adaptation.py",
 "content": "\"\"\"Loading and adaptation measures for Fritsche, Solomon & de Lange (2022) on DANDI:000021.\n\nThe paper is \"Brief Stimuli Cast a Persistent Long-Term Trace in Visual Cortex\", J Neurosci\n42(10):1999-2010, doi:10.1523/JNEUROSCI.1350-21.2021. The claims file is\nclaims/fritsche-2022.yaml; its header names the open details O1 to O6 used below.\n\nWhere each parameter comes from:\n\n- Unit quality: ISI violations <= 0.5, amplitude cutoff <= 0.1, presence ratio >= 0.9 (Methods,\n  \"Unit exclusion\", the AllenSDK defaults).\n- Response windows: 0 to 100 ms from onset for drifting gratings, 0 to 250 ms for static\n  gratings, and 0 to 100 ms for static gratings as a variant (Methods, \"Unit exclusion\" and\n  \"Orientation-specific adaptation to static gratings\").\n- Responsiveness: rate to the preferred orientation over 5 Hz (2.5 and 10 Hz as variants) and\n  over 1 SD of the gray-screen rate in the same window (Methods, \"Unit exclusion\"). The readings\n  of O4 are all computed (`responsive`).\n- Regions kept: at least 50 responsive units (Methods, \"Unit exclusion\").\n- Repeat is the same orientation (direction modulo 180 for drifting gratings), orthogonal is 90\n  degrees apart, temporal frequency, spatial frequency and phase are ignored (Methods,\n  \"Orientation-specific adaptation to drifting gratings\").\n- The readings of O1 (ratio per unit) and O3 (how blanks and blocks enter the n-back sequence)\n  are all computed (`nback_rates`, `ratios`).\n- Exponential models and their bounds: Methods, equations 2 and 3 and the paragraph after them;\n  the sign of the second term is O5, both readings are fitted (`fit_models`).\n- Rates are spike counts divided by the window length (a standard choice; it cannot change a\n  ratio).\n\"\"\"\nfrom __future__ import annotations\n\nimport json\nimport urllib.request\nfrom concurrent.futures import ProcessPoolExecutor\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nfrom scipy import optimize, stats\n\nDANDISET = \"000021\"\nVERSION = \"0.251116.2246\"\nAPI = \"https://api.dandiarchive.org/api\"\n\n# Allen CCF acronyms of the regions the paper names (Figure 1 legend: V1, LM, AL, RL, PM, AM; LGN\n# is the dorsolateral geniculate, LGd; LP).\nAREA_NAMES = {\"VISp\": \"V1\", \"VISl\": \"LM\", \"VISal\": \"AL\", \"VISrl\": \"RL\", \"VISpm\": \"PM\",\n              \"VISam\": \"AM\", \"LGd\": \"LGN\", \"LP\": \"LP\"}\nCORTEX = [\"V1\", \"LM\", \"AL\", \"RL\", \"PM\", \"AM\"]\nTHALAMUS = [\"LGN\", \"LP\"]\n\nDG_WIN = 0.1      # drifting gratings, 0 to 100 ms (Methods)\nSG_WIN = 0.25     # static gratings, 0 to 250 ms (Methods)\nSG_WIN_SHORT = 0.1\n\n\ndef session_assets():\n    \"\"\"The 32 session files (not the per-probe LFP files) of the pinned version.\"\"\"\n    url = f\"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=400\"\n    out = []\n    while url:\n        d = json.load(urllib.request.urlopen(url))\n        out += d[\"results\"]\n        url = d[\"next\"]\n    return sorted([a for a in out if \"_probe-\" not in a[\"path\"]], key=lambda a: a[\"path\"])\n\n\ndef s3_url(asset_id):\n    d = json.load(urllib.request.urlopen(\n        f\"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/{asset_id}/\"))\n    return [u for u in d[\"contentUrl\"] if \"s3\" in u][0]\n\n\ndef _counts(spk, starts, width):\n    return (np.searchsorted(spk, starts + width) - np.searchsorted(spk, starts)).astype(np.int32)\n\n\ndef _bins(intervals, width):\n    \"\"\"Start times of consecutive bins of `width` s inside each interval.\"\"\"\n    out = [np.arange(a, b - width, width) for a, b in intervals]\n    return np.concatenate(out) if out else np.zeros(0)\n\n\ndef load_session(path_and_id):\n    \"\"\"Stream one session file and reduce it to spike counts per unit and presentation.\n\n    Returns a dict with the unit table (quality metrics, area), the drifting and static grating\n    tables, the spontaneous epochs, and count matrices (units x presentations). Every unit in the\n    file is described; counts are computed for units that pass the quality metrics.\n    \"\"\"\n    path, asset_id = path_and_id\n    url = s3_url(asset_id)\n    rf = remfile.File(url, _max_cache_size=150_000_000, _max_threads=4)\n    with h5py.File(rf, \"r\") as f:\n        u = f[\"units\"]\n        units = pd.DataFrame({k: u[k][:] for k in [\n            \"id\", \"isi_violations\", \"amplitude_cutoff\", \"presence_ratio\", \"peak_channel_id\",\n            \"firing_rate\", \"quality\"]})\n        units[\"quality\"] = units[\"quality\"].astype(str)\n        idx = u[\"spike_times_index\"][:]\n        e = f[\"general/extracellular_ephys/electrodes\"]\n        loc = pd.Series(e[\"location\"][:].astype(str), index=e[\"id\"][:])\n        units[\"location\"] = loc.reindex(units.peak_channel_id).values\n        units[\"area\"] = units[\"location\"].map(AREA_NAMES)\n        units[\"passes_quality\"] = ((units.isi_violations <= 0.5) & (units.amplitude_cutoff <= 0.1)\n                                   & (units.presence_ratio >= 0.9))\n\n        def table(name, cols):\n            g = f[f\"intervals/{name}\"]\n            return pd.DataFrame({c: g[c][:] for c in cols})\n        dg = table(\"drifting_gratings_presentations\", [\n            \"id\", \"start_time\", \"stop_time\", \"orientation\", \"temporal_frequency\",\n            \"stimulus_block\", \"contrast\"])\n        sg = table(\"static_gratings_presentations\", [\n            \"id\", \"start_time\", \"stop_time\", \"orientation\", \"spatial_frequency\", \"phase\",\n            \"stimulus_block\"])\n        sg[\"phase\"] = pd.to_numeric(sg[\"phase\"].astype(str), errors=\"coerce\")\n        sp = table(\"spontaneous_presentations\", [\"start_time\", \"stop_time\"])\n        inv = (table(\"invalid_times\", [\"start_time\", \"stop_time\"])\n               if \"invalid_times\" in f[\"intervals\"] else pd.DataFrame())\n        meta = {k: f[f\"general/subject/{k}\"][()].decode() for k in\n                [\"subject_id\", \"genotype\", \"sex\", \"age\"]}\n        meta[\"session_id\"] = f[\"general/session_id\"][()].decode()\n        meta[\"path\"] = path\n\n        sel = np.flatnonzero(units.passes_quality.values)\n        starts = np.r_[0, idx[:-1]]\n        sp_iv = list(zip(sp.start_time, sp.stop_time))\n        bins100 = _bins(sp_iv, DG_WIN)\n        bins250 = _bins(sp_iv, SG_WIN)\n        n = len(sel)\n        dg_c = np.zeros((n, len(dg)), np.int32)\n        dg_pre = np.zeros((n, len(dg)), np.int32)\n        sg_c = np.zeros((n, len(sg)), np.int32)\n        sg_c100 = np.zeros((n, len(sg)), np.int32)\n        sp100 = np.zeros((n, len(bins100)), np.int32)\n        sp250 = np.zeros((n, len(bins250)), np.int32)\n        st = u[\"spike_times\"]\n        # Read runs of consecutive selected units in one request each (at most 15M spikes).\n        i = 0\n        while i < n:\n            j = i\n            while (j + 1 < n and sel[j + 1] == sel[j] + 1\n                   and idx[sel[j + 1]] - starts[sel[i]] < 15_000_000):\n                j += 1\n            a, b = starts[sel[i]], idx[sel[j]]\n            block = st[a:b]\n            for k in range(i, j + 1):\n                s = block[starts[sel[k]] - a: idx[sel[k]] - a]\n                dg_c[k] = _counts(s, dg.start_time.values, DG_WIN)\n                dg_pre[k] = _counts(s, dg.start_time.values - DG_WIN, DG_WIN)\n                sg_c[k] = _counts(s, sg.start_time.values, SG_WIN)\n                sg_c100[k] = _counts(s, sg.start_time.values, SG_WIN_SHORT)\n                sp100[k] = _counts(s, bins100, DG_WIN)\n                sp250[k] = _counts(s, bins250, SG_WIN)\n            i = j + 1\n    return dict(meta=meta, units=units, sel=sel, dg=dg, sg=sg, spont=sp, invalid=inv,\n                dg_counts=dg_c, dg_pre=dg_pre, sg_counts=sg_c, sg_counts100=sg_c100,\n                sp100=sp100, sp250=sp250)\n\n\ndef load_all(assets, workers=4):\n    items = [(a[\"path\"], a[\"asset_id\"]) for a in assets]\n    with ProcessPoolExecutor(workers) as ex:\n        return list(ex.map(load_session, items))\n\n\n# ---------------------------------------------------------------------------------------------\n# Trial sequences\n\n\ndef sequence(table, kind, blanks=\"hold\", blocks=\"within\"):\n    \"\"\"The presentation sequence used to form n-back pairs (O3).\n\n    Returns (ori, blk, keep): the orientation modulo 180 (NaN for blanks), the block of each\n    position, and the indices into `table` of the positions. blanks=\"hold\" keeps blank trials as\n    positions (O3a), \"remove\" drops them first (O3b); blocks=\"within\" forms pairs within each\n    stimulus block (O3c), \"across\" over the concatenated sequence (O3d).\n    \"\"\"\n    t = table.sort_values(\"start_time\")\n    order = t.index.values\n    ori = np.mod(t[\"orientation\"].values, 180.0)\n    blk = t[\"stimulus_block\"].values.copy()\n    if blanks == \"remove\":\n        ok = ~np.isnan(ori)\n        order, ori, blk = order[ok], ori[ok], blk[ok]\n    if blocks == \"across\":\n        blk = np.zeros_like(blk)\n    return ori, blk, order\n\n\ndef pair_masks(ori, blk, n):\n    \"\"\"Masks over current positions i (with i-n valid) for repeat and orthogonal at n-back.\"\"\"\n    cur = ori[n:]\n    prev = ori[:-n]\n    same_blk = blk[n:] == blk[:-n]\n    valid = same_blk & ~np.isnan(cur) & ~np.isnan(prev)\n    d = np.abs(cur - prev)\n    d = np.minimum(d, 180 - d)\n    rep = valid & (d < 1e-6)\n    orth = valid & (np.abs(d - 90) < 1e-6)\n    blank_prev = same_blk & ~np.isnan(cur) & np.isnan(prev)\n    return rep, orth, blank_prev\n\n\ndef nback_rates(counts, table, n_max=50, blanks=\"hold\", blocks=\"within\", win=DG_WIN):\n    \"\"\"Per unit, n and current orientation: summed counts and trial numbers for repeat and\n    orthogonal pairs. Returns arrays (units x n_max x n_ori) of rep_sum, rep_n, orth_sum, orth_n\n    and the orientation list.\"\"\"\n    ori, blk, order = sequence(table, None, blanks, blocks)\n    c = counts[:, order].astype(float)\n    oris = np.unique(ori[~np.isnan(ori)])\n    U = c.shape[0]\n    out = {k: np.zeros((U, n_max, len(oris))) for k in [\"rs\", \"rn\", \"os\", \"on\"]}\n    for n in range(1, n_max + 1):\n        rep, orth, _ = pair_masks(ori, blk, n)\n        cur_ori = ori[n:]\n        cc = c[:, n:]\n        for j, o in enumerate(oris):\n            m = cur_ori == o\n            out[\"rs\"][:, n - 1, j] = cc[:, rep & m].sum(1)\n            out[\"rn\"][:, n - 1, j] = (rep & m).sum()\n            out[\"os\"][:, n - 1, j] = cc[:, orth & m].sum(1)\n            out[\"on\"][:, n - 1, j] = (orth & m).sum()\n    return out, oris\n\n\ndef ratios(nb, how=\"pooled\"):\n    \"\"\"Adaptation ratio per unit and n (O1). how=\"pooled\": mean rate over all repeat trials over\n    mean over all orthogonal trials (O1a); \"per_ori\": ratio per current orientation, averaged\n    arithmetically (O1b); \"per_ori_geo\": geometric mean over orientations (O1b, geometric).\"\"\"\n    if how == \"pooled\":\n        r = nb[\"rs\"].sum(2) / nb[\"rn\"].sum(2)\n        o = nb[\"os\"].sum(2) / nb[\"on\"].sum(2)\n        with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n            return r / o\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        rr = (nb[\"rs\"] / nb[\"rn\"]) / (nb[\"os\"] / nb[\"on\"])\n    if how == \"per_ori\":\n        rr = np.where(np.isfinite(rr), rr, np.nan)\n        return np.nanmean(rr, 2)\n    lr = np.log(rr)\n    lr = np.where(np.isfinite(lr), lr, np.nan)\n    return np.exp(np.nanmean(lr, 2))\n\n\ndef region_value(ar, how=\"geo\"):\n    \"\"\"Region ratio from unit ratios (O2): \"geo\" exp(mean log ratio) (O2a), \"mean\" (O2b).\n    Units with a non-finite or zero ratio are left out (counted by `finite_log`).\"\"\"\n    lr = np.log(ar)\n    ok = np.isfinite(lr)\n    if how == \"geo\":\n        return float(np.exp(lr[ok].mean()))\n    return float(ar[ok].mean())\n\n\ndef ttest_log(ar):\n    \"\"\"Two-tailed one-sample t test of unit log ratios against zero (Methods).\"\"\"\n    lr = np.log(ar)\n    lr = lr[np.isfinite(lr)]\n    t, p = stats.ttest_1samp(lr, 0.0)\n    return float(t), float(p), int(lr.size)\n\n\ndef fdr(p, alpha=0.05):\n    \"\"\"Benjamini-Hochberg (Methods). Returns adjusted p values and the rejections.\"\"\"\n    p = np.asarray(p, float)\n    m = p.size\n    o = np.argsort(p)\n    adj = np.empty(m)\n    adj[o] = np.minimum.accumulate((p[o] * m / np.arange(1, m + 1))[::-1])[::-1]\n    adj = np.minimum(adj, 1)\n    return adj, adj < alpha\n\n\n# ---------------------------------------------------------------------------------------------\n# Exponential decay models (Methods, equations 2 and 3)\n\n\ndef model_double(n, af, tf, as_, ts, sign=-1):\n    \"\"\"Double exponential. sign=-1: both terms reduce the response (O5a, as Tables 1 and 2 give\n    both amplitudes as response reductions); sign=+1: as printed (O5b).\"\"\"\n    return 1 - af * np.exp(-(n - 1) / tf) + sign * as_ * np.exp(-(n - 1) / ts)\n\n\ndef model_single(n, a, t):\n    return 1 - a * np.exp(-(n - 1) / t)\n\n\n# Bounds of the Methods: a <= 0.5 (lower -Inf), tau in [-50, 50]. A tau of exactly 0 is\n# undefined; the fits start from positive values.\nB_D = ([-np.inf, -50, -np.inf, -50], [0.5, 50, 0.5, 50])\nB_S = ([-np.inf, -50], [0.5, 50])\nSTARTS_D = [(0.15, 0.8, 0.04, 6.0), (0.1, 0.3, 0.05, 3.0), (0.1, 1.5, 0.02, 15.0),\n            (0.05, 0.1, 0.05, 25.0)]\nSTARTS_S = [(0.1, 0.5), (0.1, 2.0), (0.05, 5.0)]\n\n\ndef _fit(fun, n, y, starts, bounds):\n    best = None\n    for p0 in starts:\n        try:\n            with np.errstate(all=\"ignore\"):\n                p, _ = optimize.curve_fit(lambda x, *q: np.log(np.clip(fun(x, *q), 1e-9, None)),\n                                          n, y, p0=p0, bounds=bounds, maxfev=20000)\n        except (RuntimeError, ValueError):\n            continue\n        rss = float(np.sum((y - np.log(np.clip(fun(n, *p), 1e-9, None))) ** 2))\n        if best is None or rss < best[1]:\n            best = (p, rss)\n    return best\n\n\ndef on_bound(p, bounds, tol=1e-3):\n    lo, hi = np.asarray(bounds[0]), np.asarray(bounds[1])\n    return bool(np.any(np.isfinite(lo) & (np.abs(p - lo) < tol)) or\n                np.any(np.abs(p - hi) < tol))\n\n\ndef fit_models(mean_log, sign=-1):\n    \"\"\"Least-squares fits to the region's mean log ratio at n = 1 to len(mean_log) (O5a; the\n    unit-level fit O5b has the same estimates when every unit has every n).\"\"\"\n    n = np.arange(1, len(mean_log) + 1, dtype=float)\n    d = _fit(lambda x, *q: model_double(x, *q, sign=sign), n, mean_log, STARTS_D, B_D)\n    s = _fit(model_single, n, mean_log, STARTS_S, B_S)\n    return d, s\n\n\ndef ftest(rss_s, rss_d, n_obs, k_s=2, k_d=4):\n    \"\"\"F test of nested models (Methods).\"\"\"\n    df1, df2 = k_d - k_s, n_obs - k_d\n    if rss_d <= 0:\n        return np.inf, 0.0\n    F = ((rss_s - rss_d) / df1) / (rss_d / df2)\n    return float(F), float(stats.f.sf(F, df1, df2))\n"
}
```

```
File created successfully at: entries/fritsche-2022/adaptation.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && cat > t1.py <<'EOF'
import sys, time, resource, pickle
sys.path.insert(0,'entries/fritsche-2022')
import adaptation as A
assets=A.session_assets(); print(len(assets))
t=time.time()
s=A.load_session((assets[0]['path'],assets[0]['asset_id']))
print('time',time.time()-t,'maxrss MB',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e3)
print(s['meta'], s['dg_counts'].shape, s['sg_counts'].shape, s['sp100'].shape)
pickle.dump(s,open('s0.pkl','wb'))
EOF
python t1.py
```

```
32
time 17.671013355255127 maxrss MB 797.708
{'subject_id': '699733573', 'genotype': 'Sst-IRES-Cre/wt;Ai32(RCL-ChR2(H134R)_EYFP)/wt', 'sex': 'M', 'age': 'P118D', 'session_id': '715093703', 'path': 'sub-699733573/sub-699733573_ses-715093703.nwb'} (993, 628) (993, 6000) (993, 12365)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && cat > t2.py <<'EOF'
import sys, time, pickle
sys.path.insert(0,'entries/fritsche-2022')
import adaptation as A
t=time.time()
S=A.load_all(A.session_assets())
print('time',time.time()-t)
pickle.dump(S,open('all.pkl','wb'))
EOF
python t2.py; date -u
```

```
time 133.52186274528503
Sat Nov 21 05:32:17 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && cat > t3.py <<'EOF'
import sys, pickle, numpy as np, pandas as pd
sys.path.insert(0,'entries/fritsche-2022')
import adaptation as A
S=pickle.load(open('all.pkl','rb'))
rows=[]
for s in S:
    dg,sg=s['dg'],s['sg']
    rows.append(dict(sub=s['meta']['subject_id'],ses=s['meta']['session_id'],gen=s['meta']['genotype'][:8],
      units=len(s['units']),q=int(s['units'].passes_quality.sum()),dg=len(dg),dg_blank=int(dg.orientation.isna().sum()),
      dg_blocks=dg.stimulus_block.nunique(), sg=len(sg), sg_blank=int(sg.orientation.isna().sum()),sg_blocks=sg.stimulus_block.nunique(),
      tf=sorted(dg.temporal_frequency.dropna().unique()), contr=sorted(dg.contrast.dropna().unique()), sf=len(sg.spatial_frequency.dropna().unique()),
      inv=len(s['invalid']), spont=round(float((s['spont'].stop_time-s['spont'].start_time).sum())),
      dgdur=round(float((dg.stop_time-dg.start_time).median()),3), dgisi=round(float(np.median(np.diff(dg.sort_values('start_time').start_time))),3)))
d=pd.DataFrame(rows); pd.set_option('display.width',250); pd.set_option('display.max_columns',30); print(d)
print(d.sub.nunique(), d.ses.nunique())
# areas
for s in S:
    u=s['units'][s['units'].passes_quality]
print(pd.concat([s['units'][s['units'].passes_quality].location for s in S]).value_counts().head(40))
EOF
python t3.py
```

```
Exit code 1
          sub        ses       gen  units     q   dg  dg_blank  dg_blocks    sg  sg_blank  sg_blocks                          tf  contr  sf  inv  spont  dgdur  dgisi
0   699733573  715093703  Sst-IRES   2779   993  628        30          3  6000       189          3  [1.0, 2.0, 4.0, 8.0, 15.0]  [0.8]   5    8   1237  2.002  3.003
1   703279277  719161530  Sst-IRES   3232   851  628        30          3  6000       195          3  [1.0, 2.0, 4.0, 8.0, 15.0]  [0.8]   5    1   1237  2.002  3.003
2   707296975  721123822  Pvalb-IR   1603   497  628        30          3  6000       196          3  [1.0, 2.0, 4.0, 8.0, 15.0]  [0.8]   5    5   1237  2.002  3.003
3   716813540  739448407     wt/wt   2370   703  630        30          3  6000       192          3  [1.0, 2.0, 4.0, 8.0, 15.0]  [0.8]   5    4   1237  2.002  3.003
4   717038285  732592105     wt/wt   3076   870  628        30          3  6000       193          3  [1.0, 2.0, 4.0, 8.0, 15.0]  [0.8]   5    4   1237  2.002  3.003
5   718643564  737581020     wt/wt   2055   640  630        30          3  6000       191          3  [1.0, 2.0, 4.0, 8.0, 15.0]  [0.8]   5    9   1237  2.002  3.003
6   719817799  744228101     wt/wt   2695   745  630        30          3  6000       194          3  [1.0, 2.0, 4.0, 8.0, 15.0]  [0.8]   5    0   1237  2.002  3.003
7   719828686  754312389     wt/wt   1891   553  630        30          3  6000       194          3  [1.0, 2.0, 4.0, 8.0, 15.0]  [0.8]   5    1   1237  2.002  3.003
8   722882751  743475441     wt/wt   2133   629  630        30          3  6000       194          3  [1.0, 2.0, 4.0, 8.0, 15.0]  [0.8]   5    8   1237  2.002  3.003
9   723627600  742951821     wt/wt   3008  1004  630        30          3  6000       194          3  [1.0, 2.0, 4.0, 8.0, 15.0]  [0.8]   5    7   1237  2.002  3.003
10  726141242  750332458     wt/wt   3047   997  630        30          3  6000       191          3  [1.0, 2.0, 4.0, 8.0, 15.0]  [0.8]   5    0   1237  2.002  3.
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && cat >> ~/work/encore/encore/entries/fritsche-2022/adaptation.py <<'EOF'


# ---------------------------------------------------------------------------------------------
# Responsiveness (Methods, "Unit exclusion"; readings O4)


def preferred(counts, table, win, by="orientation"):
    """Preferred orientation and its mean rate. by="orientation": orientation (modulo 180) with
    the highest mean rate over all its trials (O4e); by="condition": the single stimulus
    condition with the highest mean rate (O4f; direction and temporal frequency for drifting
    gratings, orientation, spatial frequency and phase for static gratings), and its
    orientation. Returns (pref_ori, pref_rate, rate_by_ori, oris)."""
    ori = np.mod(table["orientation"].values, 180.0)
    ok = ~np.isnan(ori)
    rate = counts[:, ok] / win
    o = ori[ok]
    oris = np.unique(o)
    by_ori = np.stack([rate[:, o == x].mean(1) for x in oris], 1)
    if by == "orientation":
        k = by_ori.argmax(1)
        return oris[k], by_ori[np.arange(len(k)), k], by_ori, oris
    if "temporal_frequency" in table:
        keys = table.loc[ok, ["orientation", "temporal_frequency"]].astype(str).agg("|".join, 1)
    else:
        keys = table.loc[ok, ["orientation", "spatial_frequency", "phase"]].astype(str).agg(
            "|".join, 1)
    codes, uniq = pd.factorize(keys)
    cond_rate = np.stack([rate[:, codes == c].mean(1) for c in range(len(uniq))], 1)
    k = cond_rate.argmax(1)
    cond_ori = np.array([o[codes == c][0] for c in range(len(uniq))])
    return cond_ori[k], cond_rate[np.arange(len(k)), k], by_ori, oris


def gray_stats(counts, table, spont_counts, win, source="blank"):
    """Mean and SD of the gray-screen rate in the response window: source="blank" from the blank
    presentations of the same stimulus set (O4c), "spont" from consecutive bins of the
    spontaneous epochs (O4d)."""
    if source == "blank":
        g = counts[:, np.isnan(table["orientation"].values)] / win
    else:
        g = spont_counts / win
    return g.mean(1), g.std(1, ddof=1)


def responsive(pref_rate, gray_mean, gray_sd, threshold=5.0, rule="mean_plus_sd"):
    """Rate over `threshold` Hz and over 1 SD of the gray rate: rule="mean_plus_sd" reads it as
    over the gray mean plus 1 SD (O4a), "sd" as over the SD itself (O4b)."""
    ref = gray_mean + gray_sd if rule == "mean_plus_sd" else gray_sd
    return (pref_rate > threshold) & (pref_rate > ref)
EOF
cat > t4.py <<'EOF'
import sys, pickle, numpy as np, pandas as pd, itertools
sys.path.insert(0,'entries/fritsche-2022')
import adaptation as A
S=pickle.load(open('all.pkl','rb'))
for stim in ['dg','sg']:
  for rule,src,by in itertools.product(['mean_plus_sd','sd'],['blank','spont'],['orientation','condition']):
    locs=[]
    for s in S:
        c = s['dg_counts'] if stim=='dg' else s['sg_counts']; sp = s['sp100'] if stim=='dg' else s['sp250']
        w = A.DG_WIN if stim=='dg' else A.SG_WIN
        _,pr,_,_=A.preferred(c,s[stim],w,by); gm,gs=A.gray_stats(c,s[stim],sp,w,src)
        r=A.responsive(pr,gm,gs,5,rule)
        locs.append(s['units'].location.values[s['sel']][r])
    vc=pd.Series(np.concatenate(locs)).value_counts()
    keep=vc[vc>=50]
    print(stim,rule,src,by,'total kept',keep.sum(), dict(keep))
EOF
python t4.py
```

```
dg mean_plus_sd blank orientation total kept 2722 {'VISp': np.int64(606), 'VISal': np.int64(450), 'VISam': np.int64(377), 'VISrl': np.int64(335), 'VISl': np.int64(284), 'VISpm': np.int64(216), 'LGd': np.int64(149), 'grey': np.int64(132), 'LP': np.int64(101), 'VIS': np.int64(72)}
dg mean_plus_sd blank condition total kept 7366 {'VISp': np.int64(975), 'grey': np.int64(961), 'VISal': np.int64(739), 'VISam': np.int64(667), 'VISrl': np.int64(656), 'CA1': np.int64(625), 'LP': np.int64(521), 'VISl': np.int64(444), 'VISpm': np.int64(383), 'LGd': np.int64(368), 'VIS': np.int64(183), 'DG': np.int64(181), 'APN': np.int64(180), 'VPM': np.int64(94), 'CA3': np.int64(90), 'PO': np.int64(84), 'SUB': np.int64(83), 'Eth': np.int64(73), 'LGv': np.int64(59)}
dg mean_plus_sd spont orientation total kept 2502 {'VISp': np.int64(548), 'VISal': np.int64(402), 'VISam': np.int64(359), 'VISrl': np.int64(288), 'VISl': np.int64(243), 'VISpm': np.int64(213), 'LGd': np.int64(153), 'grey': np.int64(134), 'LP': np.int64(92), 'VIS': np.int64(70)}
dg mean_plus_sd spont condition total kept 5855 {'VISp': np.int64(863), 'grey': np.int64(730), 'VISal': np.int64(682), 'VISam': np.int64(629), 'VISrl': np.int64(559), 'VISl': np.int64(403), 'VISpm': np.int64(380), 'LGd': np.int64(370), 'LP': np.int64(338), 'CA1': np.int64(323), 'VIS': np.int64(183), 'APN': np.int64(163), 'DG': np.int64(118), 'Eth': np.int64(61), 'VPM': np.int64(53)}
dg sd blank orientation total kept 8162 {'grey': np.int64(1212), 'VISp': np.int64(931), 'VISal': np.int64(700), 'VISam': np.int64(690), 'CA1': np.int64(653), 'VISrl': np.int64(628), 'LP': np.int64(452), 'LGd': np.int64(452), 'VISl': np.int64(412), 'VISpm': np.int64(400), 'APN': np.int64(326), 'SUB': np.int64(261), 'DG': np.int64(210), 'VIS': np.int64(207), 'CA3': np.int64(164), 'VPM': np.int64(113), 'PO': np.int64(97), 'LGv': np.int64(79), 'Eth': np.int64(65), 'ProS': np.int64(58), 'SGN': np.int64(52)}
dg sd blank condition total kept 16517 {'grey': np.int64(2930), 'CA1': np.int6
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && cat > t5.py <<'EOF'
import sys, pickle, numpy as np, pandas as pd, itertools
sys.path.insert(0,'entries/fritsche-2022')
import adaptation as A
S=pickle.load(open('all.pkl','rb'))
print(pd.concat([s['units'].quality for s in S]).value_counts())
for stim in ['dg','sg']:
  for rule,src,by in itertools.product(['mean_plus_sd','sd'],['blank','spont'],['orientation','condition']):
    locs=[]
    for s in S:
        c = s['dg_counts'] if stim=='dg' else s['sg_counts']; sp = s['sp100'] if stim=='dg' else s['sp250']
        w = A.DG_WIN if stim=='dg' else A.SG_WIN
        _,pr,_,_=A.preferred(c,s[stim],w,by); gm,gs=A.gray_stats(c,s[stim],sp,w,src)
        r=A.responsive(pr,gm,gs,5,rule)
        locs.append(s['units'].area.values[s['sel']][r])
    vc=pd.Series(np.concatenate(locs)).value_counts()
    print(stim,rule,src,by, vc.sum(), dict(vc))
EOF
python t5.py
```

```
quality
good     54476
noise    20182
Name: count, dtype: int64
dg mean_plus_sd blank orientation 2518 {'V1': np.int64(606), 'AL': np.int64(450), 'AM': np.int64(377), 'RL': np.int64(335), 'LM': np.int64(284), 'PM': np.int64(216), 'LGN': np.int64(149), 'LP': np.int64(101)}
dg mean_plus_sd blank condition 4753 {'V1': np.int64(975), 'AL': np.int64(739), 'AM': np.int64(667), 'RL': np.int64(656), 'LP': np.int64(521), 'LM': np.int64(444), 'PM': np.int64(383), 'LGN': np.int64(368)}
dg mean_plus_sd spont orientation 2298 {'V1': np.int64(548), 'AL': np.int64(402), 'AM': np.int64(359), 'RL': np.int64(288), 'LM': np.int64(243), 'PM': np.int64(213), 'LGN': np.int64(153), 'LP': np.int64(92)}
dg mean_plus_sd spont condition 4224 {'V1': np.int64(863), 'AL': np.int64(682), 'AM': np.int64(629), 'RL': np.int64(559), 'LM': np.int64(403), 'PM': np.int64(380), 'LGN': np.int64(370), 'LP': np.int64(338)}
dg sd blank orientation 4665 {'V1': np.int64(931), 'AL': np.int64(700), 'AM': np.int64(690), 'RL': np.int64(628), 'LP': np.int64(452), 'LGN': np.int64(452), 'LM': np.int64(412), 'PM': np.int64(400)}
dg sd blank condition 7626 {'V1': np.int64(1335), 'LP': np.int64(1174), 'AL': np.int64(1048), 'AM': np.int64(1033), 'RL': np.int64(1008), 'LGN': np.int64(775), 'LM': np.int64(633), 'PM': np.int64(620)}
dg sd spont orientation 4400 {'V1': np.int64(889), 'AL': np.int64(676), 'AM': np.int64(668), 'RL': np.int64(597), 'LGN': np.int64(431), 'LM': np.int64(390), 'PM': np.int64(388), 'LP': np.int64(361)}
dg sd spont condition 7485 {'V1': np.int64(1290), 'LP': np.int64(1116), 'AL': np.int64(1054), 'AM': np.int64(1022), 'RL': np.int64(990), 'LGN': np.int64(768), 'LM': np.int64(625), 'PM': np.int64(620)}
sg mean_plus_sd blank orientation 1557 {'V1': np.int64(564), 'AL': np.int64(237), 'AM': np.int64(186), 'LM': np.int64(184), 'PM': np.int64(163), 'RL': np.int64(133), 'LGN': np.int64(68), 'LP': np.int64(22)}
sg mean_plus_sd blank condition 5753 {'V1': np.int64(1586), 'AL': np.int64(865), 'RL': np.int64(7
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && cat > t6.py <<'EOF'
import sys, pickle, numpy as np, pandas as pd, itertools
sys.path.insert(0,'entries/fritsche-2022')
import adaptation as A
S=pickle.load(open('all.pkl','rb'))
for stim in ['dg','sg']:
  for rule,src,by in itertools.product(['mean_plus_sd'],['blank','spont'],['orientation']):
    locs=[]; allloc=[]
    for s in S:
        c = s['dg_counts'] if stim=='dg' else s['sg_counts']; sp = s['sp100'] if stim=='dg' else s['sp250']
        w = A.DG_WIN if stim=='dg' else A.SG_WIN
        _,pr,_,_=A.preferred(c,s[stim],w,by); gm,gs=A.gray_stats(c,s[stim],sp,w,src)
        good=s['units'].quality.values[s['sel']]=='good'
        r=A.responsive(pr,gm,gs,5,rule)&good
        locs.append(s['units'].area.values[s['sel']][r]); allloc.append(s['units'].location.values[s['sel']][r])
    vc=pd.Series(np.concatenate(locs)).value_counts()
    va=pd.Series(np.concatenate(allloc)).value_counts()
    print(stim,rule,src,by, vc.sum(), dict(vc), dict(va[va>=50]))
EOF
python t6.py
```

```
dg mean_plus_sd blank orientation 2422 {'V1': np.int64(580), 'AL': np.int64(435), 'AM': np.int64(367), 'RL': np.int64(325), 'LM': np.int64(272), 'PM': np.int64(210), 'LGN': np.int64(142), 'LP': np.int64(91)} {'VISp': np.int64(580), 'VISal': np.int64(435), 'VISam': np.int64(367), 'VISrl': np.int64(325), 'VISl': np.int64(272), 'VISpm': np.int64(210), 'LGd': np.int64(142), 'grey': np.int64(122), 'LP': np.int64(91), 'VIS': np.int64(71)}
dg mean_plus_sd spont orientation 2214 {'V1': np.int64(529), 'AL': np.int64(392), 'AM': np.int64(348), 'RL': np.int64(279), 'LM': np.int64(234), 'PM': np.int64(208), 'LGN': np.int64(145), 'LP': np.int64(79)} {'VISp': np.int64(529), 'VISal': np.int64(392), 'VISam': np.int64(348), 'VISrl': np.int64(279), 'VISl': np.int64(234), 'VISpm': np.int64(208), 'LGd': np.int64(145), 'grey': np.int64(119), 'LP': np.int64(79), 'VIS': np.int64(68)}
sg mean_plus_sd blank orientation 1495 {'V1': np.int64(545), 'AL': np.int64(230), 'AM': np.int64(179), 'LM': np.int64(176), 'PM': np.int64(159), 'RL': np.int64(128), 'LGN': np.int64(61), 'LP': np.int64(17)} {'VISp': np.int64(545), 'VISal': np.int64(230), 'VISam': np.int64(179), 'VISl': np.int64(176), 'VISpm': np.int64(159), 'VISrl': np.int64(128), 'LGd': np.int64(61)}
sg mean_plus_sd spont orientation 2067 {'V1': np.int64(553), 'AL': np.int64(358), 'AM': np.int64(356), 'PM': np.int64(238), 'RL': np.int64(230), 'LM': np.int64(209), 'LGN': np.int64(80), 'LP': np.int64(43)} {'VISp': np.int64(553), 'VISal': np.int64(358), 'VISam': np.int64(356), 'VISpm': np.int64(238), 'VISrl': np.int64(230), 'VISl': np.int64(209), 'LGd': np.int64(80), 'grey': np.int64(78), 'VIS': np.int64(55)}
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && cat > t7.py <<'EOF'
import sys, pickle, numpy as np, pandas as pd, itertools, time
sys.path.insert(0,'entries/fritsche-2022')
import adaptation as A
S=pickle.load(open('all.pkl','rb'))
t=time.time()
def select(s, stim):
    c = s['dg_counts'] if stim=='dg' else s['sg_counts']; sp = s['sp100'] if stim=='dg' else s['sp250']
    w = A.DG_WIN if stim=='dg' else A.SG_WIN
    _,pr,_,_=A.preferred(c,s[stim],w,'orientation'); gm,gs=A.gray_stats(c,s[stim],sp,w,'blank')
    good=s['units'].quality.values[s['sel']]=='good'
    area=s['units'].area.values[s['sel']]
    return A.responsive(pr,gm,gs,5,'mean_plus_sd')&good&pd.notna(area), area
res={}
for stim in ['dg','sg']:
  for bl,bk in itertools.product(['hold','remove'],['within','across']):
    ars={h:[] for h in ['pooled','per_ori','per_ori_geo']}; areas=[]
    for s in S:
        r,area=select(s,stim)
        c=(s['dg_counts'] if stim=='dg' else s['sg_counts'])[r]
        nb,_=A.nback_rates(c,s[stim],50,bl,bk)
        for h in ars: ars[h].append(A.ratios(nb,h))
        areas.append(area[r])
    areas=np.concatenate(areas)
    for h in ars:
        ar=np.concatenate(ars[h]); res[(stim,bl,bk,h)]=(ar,areas)
print(time.time()-t)
pickle.dump(res,open('res.pkl','wb'))
for k,(ar,areas) in res.items():
    row=[]
    for a in A.CORTEX+A.THALAMUS:
        x=ar[areas==a,0]; 
        if len(x)==0: continue
        tt=A.ttest_log(x)
        row.append(f"{a} {A.region_value(x,'geo'):.3f}/{A.region_value(x,'mean'):.3f} p={tt[1]:.1e} n={tt[2]}")
    print(k, '; '.join(row))
EOF
python t7.py
```

```
entries/fritsche-2022/adaptation.py:241: RuntimeWarning: divide by zero encountered in log
  lr = np.log(rr)
entries/fritsche-2022/adaptation.py:241: RuntimeWarning: divide by zero encountered in log
  lr = np.log(rr)
entries/fritsche-2022/adaptation.py:241: RuntimeWarning: divide by zero encountered in log
  lr = np.log(rr)
entries/fritsche-2022/adaptation.py:241: RuntimeWarning: divide by zero encountered in log
  lr = np.log(rr)
entries/fritsche-2022/adaptation.py:241: RuntimeWarning: divide by zero encountered in log
  lr = np.log(rr)
entries/fritsche-2022/adaptation.py:241: RuntimeWarning: divide by zero encountered in log
  lr = np.log(rr)
entries/fritsche-2022/adaptation.py:241: RuntimeWarning: divide by zero encountered in log
  lr = np.log(rr)
entries/fritsche-2022/adaptation.py:241: RuntimeWarning: divide by zero encountered in log
  lr = np.log(rr)
entries/fritsche-2022/adaptation.py:241: RuntimeWarning: divide by zero encountered in log
  lr = np.log(rr)
entries/fritsche-2022/adaptation.py:241: RuntimeWarning: divide by zero encountered in log
  lr = np.log(rr)
[... 278 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd ~/work/encore/encore/entries/fritsche-2022 && python - <<'EOF'
p='adaptation.py'; s=open(p).read()
s=s.replace("""    lr = np.log(rr)
    lr = np.where(np.isfinite(lr), lr, np.nan)
    return np.exp(np.nanmean(lr, 2))""","""    with np.errstate(divide="ignore", invalid="ignore"):
        lr = np.log(rr)
    lr = np.where(np.isfinite(lr), lr, np.nan)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        return np.exp(np.nanmean(lr, 2))""")
s=s.replace("""        rr = np.where(np.isfinite(rr), rr, np.nan)
        return np.nanmean(rr, 2)""","""        rr = np.where(np.isfinite(rr), rr, np.nan)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", RuntimeWarning)
            return np.nanmean(rr, 2)""")
s=s.replace("import json\n","import json\nimport warnings\n")
s=s.replace('''    lr = np.log(ar)
    ok = np.isfinite(lr)''','''    with np.errstate(divide="ignore", invalid="ignore"):
        lr = np.log(ar)
    ok = np.isfinite(lr)''')
s=s.replace('''    lr = np.log(ar)
    lr = lr[np.isfinite(lr)]''','''    with np.errstate(divide="ignore", invalid="ignore"):
        lr = np.log(ar)
    lr = lr[np.isfinite(lr)]''')
open(p,'w').write(s)
EOF
```

```
Sat Nov 21 05:34:44 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && cat > t8.py <<'EOF'
import sys, pickle, numpy as np, time
sys.path.insert(0,'entries/fritsche-2022')
import adaptation as A
res=pickle.load(open('res.pkl','rb'))
for stim in ['dg','sg']:
    ar,areas=res[(stim,'hold','within','pooled')]
    lr=np.log(ar); print(stim,'nonfinite',(~np.isfinite(lr)).sum(), lr.shape)
    nmax=10 if stim=='dg' else 50
    for a in A.CORTEX+A.THALAMUS:
        x=lr[areas==a]
        ps=[A.ttest_log(ar[areas==a,n])[1] for n in range(nmax)]
        adj,rej=A.fdr(ps)
        sig=np.flatnonzero(rej)+1
        m=np.array([np.nanmean(np.where(np.isfinite(x[:,n]),x[:,n],np.nan)) for n in range(50)])
        t=time.time()
        for sign in (-1,1):
            d,s=A.fit_models(m,sign)
            F,p=A.ftest(s[1],d[1],50)
            print(stim,a,'sig n',list(sig),'sign',sign,'double',np.round(d[0],3),'single',np.round(s[0],3),'F',round(F,2),'p',f"{p:.2g}", f"{time.time()-t:.2f}s")
EOF
python t8.py
```

```
dg nonfinite 0 (2422, 50)
dg V1 sig n [np.int64(1), np.int64(2), np.int64(3), np.int64(4), np.int64(5), np.int64(6), np.int64(7), np.int64(8)] sign -1 double [0.142 0.816 0.038 6.714] single [0.176 1.415] F 7.5 p 0.0015 0.02s
dg V1 sig n [np.int64(1), np.int64(2), np.int64(3), np.int64(4), np.int64(5), np.int64(6), np.int64(7), np.int64(8)] sign 1 double [ 0.142  0.816 -0.038  6.714] single [0.176 1.415] F 7.5 p 0.0015 0.05s
dg LM sig n [np.int64(1), np.int64(2), np.int64(5), np.int64(7), np.int64(8)] sign -1 double [0.138 0.508 0.033 5.662] single [0.17  0.907] F 4.48 p 0.017 0.03s
dg LM sig n [np.int64(1), np.int64(2), np.int64(5), np.int64(7), np.int64(8)] sign 1 double [ 0.138  0.508 -0.033  5.66 ] single [0.17  0.907] F 4.48 p 0.017 0.06s
dg AL sig n [np.int64(1), np.int64(2), np.int64(3), np.int64(4), np.int64(5), np.int64(7)] sign -1 double [0.103 0.026 0.069 3.929] single [0.164 1.381] F 11.66 p 8e-05 0.02s
dg AL sig n [np.int64(1), np.int64(2), np.int64(3), np.int64(4), np.int64(5), np.int64(7)] sign 1 double [ 0.103  0.019 -0.069  3.929] single [0.164 1.381] F 11.66 p 8e-05 0.05s
dg RL sig n [np.int64(1), np.int64(2), np.int64(3), np.int64(4), np.int64(5)] sign -1 double [0.043 0.269 0.082 2.827] single [0.118 1.953] F 1.54 p 0.22 0.02s
dg RL sig n [np.int64(1), np.int64(2), np.int64(3), np.int64(4), np.int64(5)] sign 1 double [ 0.043  0.269 -0.082  2.827] single [0.118 1.953] F 1.54 p 0.22 0.04s
dg PM sig n [np.int64(1), np.int64(2), np.int64(3), np.int64(4), np.int64(5), np.int64(7)] sign -1 double [0.136 0.007 0.069 4.274] single [0.2   1.104] F 6.2 p 0.0041 0.02s
dg PM sig n [np.int64(1), np.int64(2), np.int64(3), np.int64(4), np.int64(5), np.int64(7)] sign 1 double [ 0.136  0.017 -0.069  4.274] single [0.2   1.104] F 6.2 p 0.0041 0.05s
dg AM sig n [np.int64(1), np.int64(2), np.int64(3), np.int64(4), np.int64(5), np.int64(6)] sign -1 double [0.096 0.342 0.084 3.232] single [0.174 1.465] F 5.0 p 0.011 0.02s
dg AM sig n [np.int64(1), np.int64(2), np.int6
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd ~/work/encore/encore/entries/fritsche-2022 && cat >> adaptation.py <<'EOF'


# ---------------------------------------------------------------------------------------------
# Mixed ANOVA (Methods: 3 x 3 mixed ANOVA, relative orientation within units, OSI tertile
# between units). Sums of squares as in the usual split-plot decomposition, without a
# sphericity correction (the paper names none).


def mixed_anova(Y, group):
    """Y: units x levels; group: tertile label per unit. Returns dict of F and p for the
    within factor ("within"), the between factor ("between") and their interaction."""
    Y = np.asarray(Y, float)
    group = np.asarray(group)
    N, J = Y.shape
    gs = np.unique(group)
    G = len(gs)
    grand = Y.mean()
    m_i = Y.mean(1)
    m_j = Y.mean(0)
    ss_bs = J * np.sum((m_i - grand) ** 2)
    ss_g = sum(J * (group == g).sum() * (Y[group == g].mean() - grand) ** 2 for g in gs)
    ss_sw = ss_bs - ss_g
    ss_within = np.sum((Y - m_i[:, None]) ** 2)
    ss_rel = N * np.sum((m_j - grand) ** 2)
    ss_cells = sum((group == g).sum() * np.sum((Y[group == g].mean(0) - grand) ** 2) for g in gs)
    ss_int = ss_cells - ss_g - ss_rel
    ss_err = ss_within - ss_rel - ss_int
    df_rel, df_int, df_err = J - 1, (J - 1) * (G - 1), (J - 1) * (N - G)
    df_g, df_sw = G - 1, N - G
    F_rel = (ss_rel / df_rel) / (ss_err / df_err)
    F_int = (ss_int / df_int) / (ss_err / df_err)
    F_g = (ss_g / df_g) / (ss_sw / df_sw)
    return {"within": (F_rel, stats.f.sf(F_rel, df_rel, df_err), df_rel, df_err),
            "interaction": (F_int, stats.f.sf(F_int, df_int, df_err), df_int, df_err),
            "between": (F_g, stats.f.sf(F_g, df_g, df_sw), df_g, df_sw)}


# ---------------------------------------------------------------------------------------------
# Bootstrap of the decay fits (Methods: units resampled with replacement 1000 times, fits on a
# bound discarded, 2.5 and 97.5 percentiles)


def bootstrap_fits(lr, model, seed, n_boot=1000, sign=-1):
    """lr: units x n log ratios of one region. model "double" or "single". Returns the array of
    accepted parameter sets and the number discarded on a bound or failed."""
    rng = np.random.default_rng(seed)
    U = lr.shape[0]
    out, dropped = [], 0
    n = np.arange(1, lr.shape[1] + 1, dtype=float)
    p0d, p0s = fit_models(lr.mean(0), sign)
    for _ in range(n_boot):
        m = lr[rng.integers(0, U, U)].mean(0)
        if model == "double":
            r = _fit(lambda x, *q: model_double(x, *q, sign=sign), n, m,
                     [tuple(p0d[0])] + STARTS_D[:2], B_D)
            bounds = B_D
        else:
            r = _fit(model_single, n, m, [tuple(p0s[0])] + STARTS_S[:1], B_S)
            bounds = B_S
        if r is None or on_bound(r[0], bounds):
            dropped += 1
            continue
        out.append(r[0])
    return np.array(out), dropped


def _boot_task(args):
    lr, model, seed = args
    return bootstrap_fits(lr, model, seed)


def bootstrap_many(tasks, workers=4):
    """Run several (lr, model, seed) bootstraps in parallel processes."""
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(_boot_task, tasks))
EOF
cd $TMPDIR && source dev/bin/activate && cat > t9.py <<'EOF'
import sys, pickle, numpy as np, time
sys.path.insert(0,'entries/fritsche-2022')
import adaptation as A
res=pickle.load(open('res.pkl','rb'))
ar,areas=res[('dg','hold','within','pooled')]
lr=np.log(ar)
t=time.time(); b,d=A.bootstrap_fits(lr[areas=='V1'],'double',1,n_boot=100); print(time.time()-t, d, np.percentile(b,[2.5,97.5],0))
t=time.time(); b,d=A.bootstrap_fits(lr[areas=='LGN'],'single',1,n_boot=100); print(time.time()-t, d, np.percentile(b,[2.5,97.5],0))
EOF
python t9.py
```

```
1.161076307296753 0 [[ 0.11816308  0.61332916  0.02075341  3.74153257]
 [ 0.16498394  1.05731687  0.06571082 12.53868638]]
0.525629997253418 0 [[0.04660682 0.0127425 ]
 [0.09181325 0.56453537]]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > build_nb.py <<'EOF'
import nbformat, sys, re
src=open(sys.argv[1]).read()
cells=[]
for chunk in re.split(r'^# %%', src, flags=re.M)[1:]:
    head, _, body = chunk.partition('\n')
    head=head.strip(); body=body.strip('\n')
    if head.startswith('md'):
        text='\n'.join(l[2:] if l.startswith('# ') else l.lstrip('#') for l in body.split('\n'))
        cells.append(nbformat.v4.new_markdown_cell(text))
    else:
        tags=[t.strip() for t in head.replace('tags=','').split(',') if t.strip()]
        c=nbformat.v4.new_code_cell(body); 
        if tags: c.metadata['tags']=tags
        cells.append(c)
nb=nbformat.v4.new_notebook(); nb.cells=cells
nb.metadata['kernelspec']={'name':'python3','display_name':'Python 3','language':'python'}
nbformat.write(nb, sys.argv[2])
EOF
source dev/bin/activate; uv pip install -q nbformat nbclient ipykernel 2>&1|tail -1; date -u
```

```
Sat Nov 21 05:36:13 UTC 2026
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb_part1.py",
 "content": "# %% md\n# # Fritsche, Solomon & de Lange (2022) on DANDI:000021\n#\n# HEADER_PLACEHOLDER\n\n# %%\nimport os\nos.environ.setdefault(\"OMP_NUM_THREADS\", \"1\")\nos.environ.setdefault(\"OPENBLAS_NUM_THREADS\", \"1\")\nimport itertools, resource, time, zlib, warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nimport matplotlib.pyplot as plt\nimport adaptation as A\n\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 200)\nKEY = \"fritsche-2022\"\ndef seed(claim):\n    return zlib.crc32(f\"{KEY}/{claim}\".encode())\nT0 = time.time()\n\n# %%\nassets = A.session_assets()\nprint(len(assets), \"session files at version\", A.VERSION)\nS = A.load_all(assets)\nprint(f\"loaded in {time.time() - T0:.0f} s; peak memory of this process \"\n      f\"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n\n# %% md\n# ## Data check\n#\n# The dandiset's 214 assets are 32 session files and 182 per-probe LFP files; only the session\n# files are used. Each session file holds the units table (with the AllenSDK quality metrics),\n# the electrodes table (with the CCF area of each channel), and the stimulus tables of every\n# stimulus, of which the drifting and static grating tables and the spontaneous (gray screen)\n# epochs are used.\n\n# %% tags=sanity\nrows = []\nfor s in S:\n    m, dg, sg, u = s[\"meta\"], s[\"dg\"], s[\"sg\"], s[\"units\"]\n    rows.append(dict(\n        subject=m[\"subject_id\"], session=m[\"session_id\"], genotype=m[\"genotype\"].split(\"/\")[0],\n        sex=m[\"sex\"], age=m[\"age\"], units=len(u), good=int((u.quality == \"good\").sum()),\n        pass_metrics=int(u.passes_quality.sum()),\n        dg_rows=len(dg), dg_blank=int(dg.orientation.isna().sum()),\n        dg_blocks=dg.stimulus_block.nunique(), sg_rows=len(sg),\n        sg_blank=int(sg.orientation.isna().sum()), sg_blocks=sg.stimulus_block.nunique(),\n        spont_s=round(float((s[\"spont\"].stop_time - s[\"spont\"].start_time).sum())),\n        invalid_intervals=len(s[\"invalid\"])))\nsess = pd.DataFrame(rows)\nprint(sess.to_string())\nprint(\"\\nsubjects\", sess.subject.nunique(), \"sessions\", sess.session.nunique())\nprint(sess.genotype.value_counts().to_string())\nprint(\"\\nsex\", sess.sex.value_counts().to_dict())\n\n# %% tags=sanity\n# Stimulus parameters, durations and spacing.\ndg_all = pd.concat([s[\"dg\"].assign(sess=i) for i, s in enumerate(S)])\nsg_all = pd.concat([s[\"sg\"].assign(sess=i) for i, s in enumerate(S)])\nprint(\"drifting directions\", sorted(dg_all.orientation.dropna().unique()))\nprint(\"temporal frequencies\", sorted(dg_all.temporal_frequency.dropna().unique()))\nprint(\"contrast\", sorted(dg_all.contrast.dropna().unique()))\ndur = dg_all.stop_time - dg_all.start_time\nprint(f\"drifting duration {dur.min():.3f} to {dur.max():.3f} s\")\nisi = np.concatenate([np.diff(s[\"dg\"].sort_values(\"start_time\").start_time) for s in S])\nprint(f\"drifting onset spacing within blocks: median {np.median(isi):.3f} s, \"\n      f\"10th to 90th percentile {np.percentile(isi, 10):.3f} to {np.percentile(isi, 90):.3f} s\")\nprint(\"static orientations\", sorted(sg_all.orientation.dropna().unique()))\nprint(\"static spatial frequencies\", sorted(sg_all.spatial_frequency.dropna().unique()))\nprint(\"static phases\", sorted(sg_all.phase.dropna().unique()))\nsd = sg_all.stop_time - sg_all.start_time\nprint(f\"static duration {sd.min():.3f} to {sd.max():.3f} s\")\ngaps = np.concatenate([np.diff(s[\"sg\"].sort_values(\"start_time\").start_time.values) for s in S])\nprint(f\"static onset spacing: median {np.median(gaps):.4f} s, 99th percentile \"\n      f\"{np.percentile(gaps, 99):.4f} s, {np.sum(gaps > 1)} gaps over 1 s (between blocks)\")\nper = dg_all.dropna(subset=[\"orientation\"]).groupby([\"sess\", \"orientation\", \"temporal_frequency\"]).size()\nprint(\"drifting presentations per direction and frequency per session:\", per.min(), \"to\", per.max())\ncnt = sg_all.dropna(subset=[\"orientation\"]).groupby([\"sess\", \"orientation\", \"spatial_frequency\", \"phase\"]).size()\nprint(\"static presentations per condition per session:\", cnt.min(), \"to\", cnt.max())\nfor i in [0, 1, 2]:\n    d = S[i][\"dg\"].dropna(subset=[\"orientation\"])\n    print(sess.session[i], \"drifting gratings\", len(d), d.groupby(\"orientation\").size().to_dict())\n\n# %% tags=sanity\n# Invalid intervals and whether they overlap the grating epochs.\nfor i, s in enumerate(S):\n    inv = s[\"invalid\"]\n    if len(inv) == 0:\n        continue\n    ep = {\"dg\": (s[\"dg\"].start_time.min(), s[\"dg\"].stop_time.max()),\n          \"sg\": (s[\"sg\"].start_time.min(), s[\"sg\"].stop_time.max())}\n    ov = {k: int(((inv.start_time < b) & (inv.stop_time > a)).sum()) for k, (a, b) in ep.items()}\n    print(sess.session[i], len(inv), \"invalid intervals, overlapping drifting\", ov[\"dg\"],\n          \"static\", ov[\"sg\"], \"total length\", round(float((inv.stop_time - inv.start_time).sum())), \"s\")\n\n# %% tags=sanity\n# Unit areas and the AllenSDK metrics.\nU = pd.concat([s[\"units\"].assign(sess=i) for i, s in enumerate(S)])\nprint(\"units\", len(U), \"quality labels\", U.quality.value_counts().to_dict())\nfor c in [\"isi_violations\", \"amplitude_cutoff\", \"presence_ratio\", \"firing_rate\"]:\n    v = U[c].replace([np.inf, -np.inf], np.nan)\n    print(f\"{c}: {v.min():.3g} to {v.max():.3g}, NaN {int(v.isna().sum())}\")\nprint(\"units with no area label in the electrodes table\", int(U.location.isna().sum()))\nq = U[U.passes_quality & (U.quality == \"good\")]\nprint(\"pass metrics and labelled good:\", len(q))\nprint(q.location.value_counts().head(30).to_string())\n\n# %% tags=sanity\n# Recordings deposited more than once: identical stimulus timing, or identical spike count\n# vectors of units across or within sessions.\nt0 = [round(float(s[\"dg\"].start_time.min()), 4) for s in S]\nprint(\"distinct first drifting onsets\", len(set(t0)), \"of\", len(S))\nh = {}\ndup_within, dup_across = 0, 0\nfor i, s in enumerate(S):\n    seen = set()\n    for k in range(s[\"dg_counts\"].shape[0]):\n        v = np.r_[s[\"dg_counts\"][k], s[\"sg_counts\"][k]]\n        if v.sum() < 50:\n            continue\n        key = hash(v.tobytes())\n        if key in seen:\n            dup_within += 1\n        seen.add(key)\n        if key in h and h[key] != i:\n            dup_across += 1\n        h.setdefault(key, i)\nprint(\"units with identical count vectors: within a session\", dup_within, \"across sessions\", dup_across)\n\n# %% tags=sanity\n# Clock check. In each session, the orientation tuning of V1 units is estimated from even trials\n# and tested on odd trials, with the true orientation labels and with labels shifted by whole\n# presentations. A response locked to the table's onsets gives a positive index with the true\n# labels only. The onset response (0 to 100 ms against the 100 ms before onset) is also given.\ndef tuning_index(c, ori, shift):\n    o = np.roll(ori, shift)\n    ok = ~np.isnan(o)\n    idx = np.flatnonzero(ok)\n    ev, od = idx[::2], idx[1::2]\n    oris = np.unique(o[ok])\n    me = np.stack([c[:, ev][:, o[ev] == x].mean(1) for x in oris], 1)\n    mo = np.stack([c[:, od][:, o[od] == x].mean(1) for x in oris], 1)\n    k = me.argmax(1)\n    pref = mo[np.arange(len(k)), k]\n    orth = mo[np.arange(len(k)), (k + len(oris) // 2) % len(oris)]\n    with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n        return np.nanmean((pref - orth) / (pref + orth))\nclock = []\nfor i, s in enumerate(S):\n    v1 = (s[\"units\"].location.values[s[\"sel\"]] == \"VISp\")\n    if v1.sum() < 5:\n        clock.append(dict(session=sess.session[i], v1_units=int(v1.sum())))\n        continue\n    dg = s[\"dg\"]\n    order = np.argsort(dg.start_time.values)\n    ori = np.mod(dg.orientation.values[order], 180)\n    c = s[\"dg_counts\"][v1][:, order].astype(float)\n    sgo = np.argsort(s[\"sg\"].start_time.values)\n    sori = np.mod(s[\"sg\"].orientation.values[sgo], 180)\n    cs = s[\"sg_counts\"][v1][:, sgo].astype(float)\n    on = s[\"dg_counts\"][v1][:, ~np.isnan(dg.orientation.values)].mean()\n    pre = s[\"dg_pre\"][v1][:, ~np.isnan(dg.orientation.values)].mean()\n    clock.append(dict(session=sess.session[i], v1_units=int(v1.sum()),\n                      dg_true=tuning_index(c, ori, 0), dg_shift_p1=tuning_index(c, ori, 1),\n                      dg_shift_m1=tuning_index(c, ori, -1),\n                      sg_true=tuning_index(cs, sori, 0), sg_shift_p10=tuning_index(cs, sori, 10),\n                      sg_shift_m10=tuning_index(cs, sori, -10),\n                      onset_spikes=on, pre_spikes=pre))\nclock = pd.DataFrame(clock)\nprint(clock.round(3).to_string())\n\n# %% md\n# ## Unit selection\n#\n# Units pass the AllenSDK quality metrics (ISI violations <= 0.5, amplitude cutoff <= 0.1,\n# presence ratio >= 0.9; Methods, \"Unit exclusion\"). The NWB files also label 20182 of the 74658\n# units `noise`; the AllenSDK's units table leaves these out by default, which the Methods'\n# \"default quality metrics of the AllenSDK\" is read to include (an assumption; the variant\n# without it is shown). Responsiveness follows Methods, \"Unit exclusion\", with the readings of O4.\n\n# %%\ndef select(s, stim, rule=\"mean_plus_sd\", src=\"blank\", by=\"orientation\", thr=5.0, good=True,\n           win=None):\n    if stim == \"dg\":\n        c, sp, w = s[\"dg_counts\"], s[\"sp100\"], A.DG_WIN\n    elif win == A.SG_WIN_SHORT:\n        c, sp, w = s[\"sg_counts100\"], s[\"sp100\"], A.SG_WIN_SHORT\n    else:\n        c, sp, w = s[\"sg_counts\"], s[\"sp250\"], A.SG_WIN\n    table = s[stim]\n    pref_ori, pr, by_ori, oris = A.preferred(c, table, w, by)\n    gm, gs = A.gray_stats(c, table, sp, w, src)\n    r = A.responsive(pr, gm, gs, thr, rule)\n    if good:\n        r &= s[\"units\"].quality.values[s[\"sel\"]] == \"good\"\n    return r, pref_ori, by_ori, oris\n\ndef count_regions(stim, **kw):\n    loc = []\n    for s in S:\n        r = select(s, stim, **kw)[0]\n        loc.append(s[\"units\"].location.values[s[\"sel\"]][r])\n    return pd.Series(np.concatenate(loc)).value_counts()\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb_part1.py (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb_part2.py",
 "content": "# %% md\n# ## units-responsive-count\n#\n# > The drifting grating analysis rests on 2365 visually responsive neurons in visual cortex and\n# > thalamus of 32 mice, with 562 in V1, 140 in LGN and 90 in LP.\n#\n# Every reading of O4 is run: (a) over gray mean + 1 SD or (b) over 1 SD; gray from (c) the\n# blank trials or (d) the spontaneous epochs (100 ms bins); preferred orientation (e) pooled over\n# directions and temporal frequencies or (f) the best single condition. Each also without the\n# `noise` label filter. Unlabelled channels (`grey`, `VIS`) are not regions the paper names and are\n# listed apart. \"Kept\" is the set of the paper's eight regions with at least 50 units.\n\n# %% tags=claim:units-responsive-count\nNAMED = set(A.AREA_NAMES)\nrows = []\nfor good in [True, False]:\n    for rule, src, by in itertools.product([\"mean_plus_sd\", \"sd\"], [\"blank\", \"spont\"],\n                                           [\"orientation\", \"condition\"]):\n        vc = count_regions(\"dg\", rule=rule, src=src, by=by, good=good)\n        named = vc[vc.index.isin(NAMED)]\n        kept = named[named >= 50]\n        other50 = sorted(vc[(~vc.index.isin(NAMED)) & (vc >= 50)].index)\n        g = lambda k: int(named.get(k, 0))\n        tot = int(kept.sum())\n        ok = (abs(tot - 2365) <= 236.5 and abs(g(\"VISp\") - 562) <= 56.2\n              and abs(g(\"LGd\") - 140) <= 14 and abs(g(\"LP\") - 90) <= 9 and len(kept) == 8)\n        rows.append(dict(good_only=good, O4=f\"{'a' if rule == 'mean_plus_sd' else 'b'}\"\n                         f\"{'c' if src == 'blank' else 'd'}{'e' if by == 'orientation' else 'f'}\",\n                         total=tot, V1=g(\"VISp\"), LM=g(\"VISl\"), AL=g(\"VISal\"), RL=g(\"VISrl\"),\n                         PM=g(\"VISpm\"), AM=g(\"VISam\"), LGN=g(\"LGd\"), LP=g(\"LP\"),\n                         named_kept=len(kept), other_labels_50=\",\".join(other50),\n                         all_within_tolerance=ok))\ncounts_tab = pd.DataFrame(rows)\nprint(counts_tab.to_string())\nprint(\"\\npaper: total 2365 (tolerance 236.5), V1 562 (56.2), LGN 140 (14), LP 90 (9)\")\n\n# %% md\n# The analyses below use the reading that the counts single out for both stimulus sets (see also\n# the static counts below): `noise` units left out, gray mean + 1 SD of the blank presentations,\n# preferred orientation pooled over the other stimulus parameters (O4 a, c, e).\n#\n# Ratios use the main reading of O1 to O3: per unit the mean rate over all repeat trials over the\n# mean over all orthogonal trials (O1a); the region value is exp(mean log ratio) (O2a); blank\n# trials hold a position in the sequence and pairs are formed within each stimulus block (O3a, c).\n# The other readings are shown for the 1-back values.\n\n# %%\nMAIN = dict(rule=\"mean_plus_sd\", src=\"blank\", by=\"orientation\", good=True)\ndef build(stim, sel_kw=MAIN, blanks=\"hold\", blocks=\"within\", n_max=50, win=None):\n    \"\"\"Per responsive unit: area, session index, n-back structures and preferred orientation.\"\"\"\n    out = dict(area=[], sess=[], pref=[], nb=[], by_ori=[], oris=None)\n    for i, s in enumerate(S):\n        r, pref, by_ori, oris = select(s, stim, win=win, **sel_kw)\n        area = s[\"units\"].area.values[s[\"sel\"]]\n        r &= pd.notna(area)\n        if stim == \"dg\":\n            c = s[\"dg_counts\"]\n        else:\n            c = s[\"sg_counts100\"] if win == A.SG_WIN_SHORT else s[\"sg_counts\"]\n        nb, nb_oris = A.nback_rates(c[r], s[stim], n_max, blanks, blocks)\n        out[\"area\"].append(area[r]); out[\"sess\"].append(np.full(r.sum(), i))\n        out[\"pref\"].append(pref[r]); out[\"nb\"].append(nb); out[\"by_ori\"].append(by_ori[r])\n        out[\"oris\"] = nb_oris\n    out[\"area\"] = np.concatenate(out[\"area\"]); out[\"sess\"] = np.concatenate(out[\"sess\"])\n    out[\"pref\"] = np.concatenate(out[\"pref\"]); out[\"by_ori\"] = np.concatenate(out[\"by_ori\"])\n    out[\"nb\"] = {k: np.concatenate([nb[k] for nb in out[\"nb\"]]) for k in [\"rs\", \"rn\", \"os\", \"on\"]}\n    return out\n\nt = time.time()\nD = {}\nfor blanks, blocks in itertools.product([\"hold\", \"remove\"], [\"within\", \"across\"]):\n    D[(\"dg\", blanks, blocks)] = build(\"dg\", blanks=blanks, blocks=blocks)\n    D[(\"sg\", blanks, blocks)] = build(\"sg\", blanks=blanks, blocks=blocks)\nprint(f\"n-back tables built in {time.time() - t:.0f} s\")\nDG, SG = D[(\"dg\", \"hold\", \"within\")], D[(\"sg\", \"hold\", \"within\")]\nAR = {k: {h: A.ratios(v[\"nb\"], h) for h in [\"pooled\", \"per_ori\", \"per_ori_geo\"]} for k, v in D.items()}\nar_dg, ar_sg = AR[(\"dg\", \"hold\", \"within\")][\"pooled\"], AR[(\"sg\", \"hold\", \"within\")][\"pooled\"]\nfor name, ar in [(\"drifting\", ar_dg), (\"static\", ar_sg)]:\n    lr = np.log(ar)\n    print(f\"{name}: {ar.shape[0]} units x {ar.shape[1]} n; non-finite log ratios {int((~np.isfinite(lr)).sum())}\")\n    print(f\"  ratio range {np.nanmin(ar):.3f} to {np.nanmax(ar):.3f}\")\n    print(\"  units per area\", pd.Series(D[('dg' if name == 'drifting' else 'sg', 'hold', 'within')]['area']).value_counts().to_dict())\nprint(\"repeat pairs per unit at 1-back (drifting), median\", np.median(DG[\"nb\"][\"rn\"][:, 0].sum(1)),\n      \"orthogonal\", np.median(DG[\"nb\"][\"on\"][:, 0].sum(1)))\nprint(\"repeat pairs per unit at 1-back (static), median\", np.median(SG[\"nb\"][\"rn\"][:, 0].sum(1)),\n      \"orthogonal\", np.median(SG[\"nb\"][\"on\"][:, 0].sum(1)))\n\ndef onebak_table(stim):\n    rows = []\n    for (st, blanks, blocks), d in D.items():\n        if st != stim:\n            continue\n        for how in [\"pooled\", \"per_ori\", \"per_ori_geo\"]:\n            ar = AR[(st, blanks, blocks)][how]\n            for agg in [\"geo\", \"mean\"]:\n                row = dict(O1=how, O2=agg, blanks=blanks, blocks=blocks)\n                for a in A.CORTEX + A.THALAMUS:\n                    x = ar[d[\"area\"] == a, 0]\n                    row[a] = round(A.region_value(x, agg), 3) if len(x) else np.nan\n                rows.append(row)\n    return pd.DataFrame(rows)\n\ndef region_stats(ar, area, n=0, regions=A.CORTEX + A.THALAMUS):\n    rows = []\n    for a in regions:\n        x = ar[area == a, n]\n        lr = np.log(x); lr = lr[np.isfinite(lr)]\n        if len(lr) < 2:\n            continue\n        t_, p, k = A.ttest_log(x)\n        ci = np.exp(lr.mean() + np.array([-1, 1]) * stats.t.ppf(0.975, k - 1) * lr.std(ddof=1) / np.sqrt(k))\n        rows.append(dict(area=a, n_units=k, ratio=np.exp(lr.mean()), ci_low=ci[0], ci_high=ci[1],\n                         t=t_, p=p))\n    df = pd.DataFrame(rows)\n    df[\"p_fdr\"] = A.fdr(df.p.values)[0]\n    return df\n\n# %% md\n# ## fig1d-v1-1back\n#\n# > In V1 the immediate repetition of orientation reduces the early (0 to 100 ms) response to\n# > drifting gratings by 17%, a 1-back adaptation ratio of 0.83.\n\n# %% tags=claim:fig1d-v1-1back\nr1 = region_stats(ar_dg, DG[\"area\"])\nprint(\"main reading (O1a, O2a, O3a+c); CI is the t interval of the mean log ratio\")\nprint(r1.round(4).to_string())\ntab1 = onebak_table(\"dg\")\nprint(\"\\n1-back ratio under every reading of O1 to O3 (drifting)\")\nprint(tab1.to_string())\nv1 = tab1[\"V1\"]\nprint(f\"\\nV1 range over readings {v1.min():.3f} to {v1.max():.3f}; readings inside [0.81, 0.84]: \"\n      f\"{int(((v1 >= 0.81) & (v1 <= 0.84)).sum())} of {len(v1)}\")\nfor (st, bl, bk), d in D.items():\n    if st == \"dg\":\n        for how in [\"pooled\", \"per_ori\", \"per_ori_geo\"]:\n            t_, p, k = A.ttest_log(AR[(st, bl, bk)][how][d[\"area\"] == \"V1\", 0])\n            print(f\"V1 t test, {how}, {bl}, {bk}: t = {t_:.2f}, p = {p:.1e}, n = {k}\")\nprint(\"by session: V1 ratio per mouse (units)\")\nv1m = pd.Series(ar_dg[DG[\"area\"] == \"V1\", 0]).groupby(DG[\"sess\"][DG[\"area\"] == \"V1\"]).apply(\n    lambda x: f\"{np.exp(np.log(x).mean()):.3f} ({len(x)})\")\nprint(v1m.to_dict())\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb_part2.py (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb_part3.py",
 "content": "# %% md\n# ## fig1d-extrastriate-1back\n#\n# > Extrastriate areas show similar 1-back adaptation to drifting gratings, with ratios between\n# > 0.80 and 0.88, all significant.\n#\n# Correction (O6): Benjamini-Hochberg over the eight areas (`p_fdr` above); Bonferroni over five\n# is shown as a variant.\n\n# %% tags=claim:fig1d-extrastriate-1back\nex = r1[r1.area.isin([\"LM\", \"AL\", \"RL\", \"PM\", \"AM\"])].copy()\nex[\"p_bonf5\"] = np.minimum(ex.p * 5, 1)\nprint(ex.round(4).to_string())\nprint(f\"\\nmain reading: range {ex.ratio.min():.3f} to {ex.ratio.max():.3f}; all in [0.72, 0.968]: \"\n      f\"{bool(ex.ratio.between(0.72, 0.968).all())}; largest corrected p {ex.p_fdr.max():.1e}\")\nrng_tab = tab1[[\"O1\", \"O2\", \"blanks\", \"blocks\"]].copy()\nrng_tab[\"ex_min\"] = tab1[[\"LM\", \"AL\", \"RL\", \"PM\", \"AM\"]].min(1)\nrng_tab[\"ex_max\"] = tab1[[\"LM\", \"AL\", \"RL\", \"PM\", \"AM\"]].max(1)\nrng_tab[\"all_in_range\"] = (rng_tab.ex_min >= 0.72) & (rng_tab.ex_max <= 0.968)\nprint(rng_tab.to_string())\n\n# %% md\n# ## fig1d-thalamus-1back\n#\n# > LGN and LP also show orientation-specific 1-back adaptation to drifting gratings, with ratios\n# > of 0.93 and 0.83.\n\n# %% tags=claim:fig1d-thalamus-1back\nth = r1[r1.area.isin(A.THALAMUS)]\nprint(th.round(5).to_string())\nprint(\"\\npaper: LGN 0.93 [0.91, 0.96] p = 8e-7 (n = 140); LP 0.83 [0.79, 0.88] p = 3e-10 (n = 90)\")\nprint(tab1[[\"O1\", \"O2\", \"blanks\", \"blocks\", \"LGN\", \"LP\"]].to_string())\nboth = tab1.LGN.between(0.91, 0.96) & tab1.LP.between(0.79, 0.88)\nprint(\"readings with both inside their CIs:\", int(both.sum()), \"of\", len(tab1))\n\n# %% md\n# ## fig1e-consistent-across-mice\n#\n# > The 1-back response reduction is consistent across mice, in thalamus and in cortex.\n#\n# Per mouse (one session each), the mean over its responsive units of the 0 to 100 ms rate on\n# 1-back repeat and orthogonal trials (Figure 1E legend). Readings: (a) every mouse has orthogonal\n# above repeat; (b) a two-sided sign test across mice at p < 0.05.\n\ndef mouse_rates(d, group, ns, win):\n    \"\"\"Per session: mean over units of the repeat and orthogonal rates, trials pooled over the\n    n in `ns` (pooled) or rates averaged over n (averaged).\"\"\"\n    nb = d[\"nb\"]; idx = np.array(ns) - 1\n    out = []\n    for pooled in [True, False]:\n        if pooled:\n            rep = nb[\"rs\"][:, idx].sum((1, 2)) / nb[\"rn\"][:, idx].sum((1, 2)) / win\n            orth = nb[\"os\"][:, idx].sum((1, 2)) / nb[\"on\"][:, idx].sum((1, 2)) / win\n        else:\n            rep = (nb[\"rs\"][:, idx].sum(2) / nb[\"rn\"][:, idx].sum(2)).mean(1) / win\n            orth = (nb[\"os\"][:, idx].sum(2) / nb[\"on\"][:, idx].sum(2)).mean(1) / win\n        m = np.isin(d[\"area\"], group)\n        df = pd.DataFrame(dict(sess=d[\"sess\"][m], rep=rep[m], orth=orth[m]))\n        g = df.groupby(\"sess\").agg(rep=(\"rep\", \"mean\"), orth=(\"orth\", \"mean\"), units=(\"rep\", \"size\"))\n        g[\"pooled\"] = pooled\n        out.append(g)\n    return out\n\ndef consistency(g, label):\n    above = int((g.orth > g.rep).sum()); n = len(g)\n    p = stats.binomtest(above, n, 0.5).pvalue if n else np.nan\n    ok_a = above == n and n > 0\n    ok_b = (p < 0.05) and above > n / 2\n    print(f\"{label}: {n} mice, {above} with orthogonal above repeat, sign test p = {p:.2g}, \"\n          f\"median orth - rep {np.median(g.orth - g.rep):.3f} Hz; (a) {ok_a}, (b) {ok_b}\")\n    return ok_a, ok_b\n\n# %% tags=claim:fig1e-consistent-across-mice\nfor grp, name in [(A.THALAMUS, \"thalamus\"), (A.CORTEX, \"cortex\")]:\n    g = mouse_rates(DG, grp, [1], A.DG_WIN)[0]\n    consistency(g, f\"drifting 1-back, {name}\")\n    print(f\"  rates {g[['rep', 'orth']].min().min():.2f} to {g[['rep', 'orth']].max().max():.2f} Hz\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb_part3.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > dev.sh <<'EOF'
#!/bin/bash
# usage: dev.sh part files... ; runs concatenated parts as a script with cached data
cd entries/fritsche-2022
source /tmp/claude-1001/dev/bin/activate
cat "$@" | sed 's|^S = A.load_all(assets)|import pickle; S = pickle.load(open("/tmp/claude-1001/all.pkl","rb"))|' > /tmp/claude-1001/run.py
python /tmp/claude-1001/run.py
EOF
chmod +x dev.sh; ./dev.sh nb_part1.py nb_part2.py nb_part3.py 2>&1 | tail -150
```

```
cat: nb_part1.py: No such file or directory
cat: nb_part2.py: No such file or directory
cat: nb_part3.py: No such file or directory
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && ./dev.sh $TMPDIR/nb_part1.py $TMPDIR/nb_part2.py $TMPDIR/nb_part3.py 2>&1 | tail -170
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/run.py", line 15, in <module>
    import adaptation as A
ModuleNotFoundError: No module named 'adaptation'
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i 's|^python /tmp/claude-1001/run.py|PYTHONPATH=. python /tmp/claude-1001/run.py|' dev.sh && ./dev.sh $TMPDIR/nb_part1.py $TMPDIR/nb_part2.py $TMPDIR/nb_part3.py 2>&1 | tail -170
```

```
15  755434585        89    0.194        0.023       -0.005    0.225        -0.012        -0.002         0.552       0.343
16  751348571        53    0.242        0.103        0.027    0.169        -0.003        -0.006         0.686       0.444
17  757216464        93    0.253       -0.011        0.005    0.227         0.004        -0.019         0.684       0.439
18  756029989        55    0.236        0.021       -0.110    0.216        -0.013        -0.011         0.738       0.454
19  758798717        47    0.250       -0.024       -0.046    0.231        -0.008        -0.010         0.855       0.546
20  760693773        99    0.364       -0.002       -0.047    0.265         0.003         0.003         0.469       0.360
21  760345702        85    0.274        0.085        0.027    0.276        -0.007         0.005         0.605       0.366
22  759883607        75    0.170       -0.002        0.018    0.207        -0.001        -0.002         0.670       0.393
23  763673393        79    0.199        0.038        0.019    0.231        -0.003         0.006         0.728       0.610
24  761418226        43    0.218        0.007        0.021    0.289         0.000        -0.014         0.849       0.563
25  762602078        86    0.417        0.092        0.032    0.328        -0.012         0.020         0.583       0.222
26  762120172        93    0.246        0.037       -0.021    0.276        -0.003         0.003         0.587       0.364
27  773418906        44    0.212        0.024        0.036    0.207         0.004         0.001         0.544       0.452
28  791319847       107    0.240        0.046       -0.030    0.223        -0.006         0.005         0.640       0.398
29  799864342        81    0.337        0.036       -0.040    0.309         0.005        -0.011         0.576       0.374
30  798911424       101    0.259       -0.022        0.019    0.272        -0.007        -0.003         0.597       0.389
31  797828357        92    0.236        0.041   
[... 154 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb_part4.py",
 "content": "# %% md\n# ## fig2-v1-tuning-main-effect\n#\n# > In V1, 1-back adaptation is strongest when adaptor and test match the neuron's preferred\n# > orientation and weakens for less preferred orientations, a main effect of relative\n# > orientation.\n#\n# Per region, OSI from the 0 to 100 ms rates to the preferred orientation and its orthogonal\n# (Methods, equation 4), split into tertiles. Per unit, the 1-back ratio of each test orientation\n# preceded by itself over preceded by its orthogonal, at 0, 45 and 90 degrees from preferred.\n# Readings: ANOVA on (a) log ratios or (b) ratios; the 45 degree level (c) pools the trials of +45\n# and -45 or (d) averages their two ratios.\n\n# %%\ndef tuning_cells(d, region):\n    m = d[\"area\"] == region\n    nb = {k: v[m][:, 0, :] for k, v in d[\"nb\"].items()}   # 1-back, per current orientation\n    oris = d[\"oris\"]; k = len(oris)\n    by_ori = d[\"by_ori\"][m]\n    pi = np.array([int(np.flatnonzero(oris == p)[0]) for p in d[\"pref\"][m]])\n    rows = np.arange(m.sum())\n    def ratio_at(j_list, pool=True):\n        if pool:\n            rs = sum(nb[\"rs\"][rows, j] for j in j_list); rn = sum(nb[\"rn\"][rows, j] for j in j_list)\n            os_ = sum(nb[\"os\"][rows, j] for j in j_list); on = sum(nb[\"on\"][rows, j] for j in j_list)\n            return (rs / rn) / (os_ / on)\n        return np.mean([(nb[\"rs\"][rows, j] / nb[\"rn\"][rows, j]) / (nb[\"os\"][rows, j] / nb[\"on\"][rows, j])\n                        for j in j_list], 0)\n    half = k // 2\n    out = {}\n    for pool in [True, False]:\n        r0 = ratio_at([pi])\n        r45 = ratio_at([(pi + 1) % k, (pi - 1) % k], pool)\n        r90 = ratio_at([(pi + half) % k])\n        out[pool] = np.stack([r0, r45, r90], 1)\n    pref = by_ori[rows, pi]; orth = by_ori[rows, (pi + half) % k]\n    osi = (pref - orth) / (pref + orth)\n    tert = pd.qcut(pd.Series(osi).rank(method=\"first\"), 3, labels=[\"low\", \"medium\", \"high\"]).values\n    return out, osi, np.asarray(tert)\n\nANOVA = {}\nCELLS = {}\nfor region in A.CORTEX + A.THALAMUS:\n    out, osi, tert = tuning_cells(DG, region)\n    for pool in [True, False]:\n        R = out[pool]\n        ok = np.all(np.isfinite(np.log(R)), 1)\n        CELLS[(region, pool)] = (R[ok], tert[ok], int((~ok).sum()))\n        for scale in [\"log\", \"ratio\"]:\n            Y = np.log(R[ok]) if scale == \"log\" else R[ok]\n            ANOVA[(region, pool, scale)] = A.mixed_anova(Y, tert[ok])\ndef anova_table(regions):\n    rows = []\n    for (region, pool, scale), r in ANOVA.items():\n        if region not in regions:\n            continue\n        R, tert, dropped = CELLS[(region, pool)]\n        gm = np.exp(np.log(R).mean(0))\n        rows.append(dict(region=region, level45=\"pooled (c)\" if pool else \"averaged (d)\", scale=scale,\n                         units=len(R), dropped=dropped,\n                         F_rel=r[\"within\"][0], p_rel=f\"{r['within'][1]:.2g}\",\n                         F_int=r[\"interaction\"][0], p_int=f\"{r['interaction'][1]:.2g}\",\n                         df=f\"{r['within'][2]},{r['within'][3]}\",\n                         ratio0=gm[0], ratio45=gm[1], ratio90=gm[2]))\n    return pd.DataFrame(rows)\n\n# %% tags=claim:fig2-v1-tuning-main-effect\nprint(anova_table([\"V1\"]).round(3).to_string())\nR, tert, _ = CELLS[(\"V1\", True)]\nprint(\"\\nV1 ratio by tertile (rows) and relative orientation 0, 45, 90 (pooled 45):\")\nfor t_ in [\"low\", \"medium\", \"high\"]:\n    print(t_, np.round(np.exp(np.log(R[tert == t_]).mean(0)), 3), \"units\", int((tert == t_).sum()))\nprint(\"\\nother cortical areas, main effect and interaction (log, pooled 45):\")\nprint(anova_table([\"LM\", \"AL\", \"RL\", \"PM\", \"AM\"]).query(\"scale == 'log' and level45 == 'pooled (c)'\").round(3).to_string())\n\n# %% md\n# ## fig2-v1-tuning-interaction\n#\n# > The dependence of V1 adaptation on relative orientation is strongest in highly\n# > orientation-selective neurons (interaction of relative orientation and OSI).\n\n# %% tags=claim:fig2-v1-tuning-interaction\nfor pool in [True, False]:\n    R, tert, _ = CELLS[(\"V1\", pool)]\n    for scale in [\"log\", \"ratio\"]:\n        r = ANOVA[(\"V1\", pool, scale)][\"interaction\"]\n        spread = {t_: float(np.ptp(np.exp(np.log(R[tert == t_]).mean(0)))) for t_ in [\"low\", \"medium\", \"high\"]}\n        print(f\"45 {'pooled' if pool else 'averaged'}, {scale}: interaction F = {r[0]:.2f}, p = {r[1]:.2g}; \"\n              f\"spread of ratios over relative orientation by tertile {np.round(list(spread.values()), 3)}; \"\n              f\"largest in high: {max(spread, key=spread.get) == 'high'}\")\n\n# %% md\n# ## fig2-v1-adaptation-at-all-orientations\n#\n# > V1 neurons adapt for all adaptor orientations relative to their preference, except\n# > nonpreferred (90 degree) adaptor and test in the most selective units.\n#\n# Per cell of tertile and relative orientation, a t test of log ratios against zero, corrected by\n# Benjamini-Hochberg (O6) over (a) the nine V1 cells or (b) all 72 cells of the eight areas;\n# Bonferroni as a variant.\n\n# %% tags=claim:fig2-v1-adaptation-at-all-orientations\ndef cell_tests(pool):\n    rows = []\n    for region in A.CORTEX + A.THALAMUS:\n        R, tert, _ = CELLS[(region, pool)]\n        for t_ in [\"low\", \"medium\", \"high\"]:\n            for j, rel in enumerate([0, 45, 90]):\n                x = np.log(R[tert == t_, j])\n                tt = stats.ttest_1samp(x, 0)\n                rows.append(dict(region=region, tertile=t_, rel=rel, n=len(x), ratio=np.exp(x.mean()),\n                                 t=tt.statistic, p=tt.pvalue))\n    df = pd.DataFrame(rows)\n    df[\"p_bh_all\"] = A.fdr(df.p.values)[0]\n    df[\"p_bonf_all\"] = np.minimum(df.p * len(df), 1)\n    v = df.region == \"V1\"\n    df.loc[v, \"p_bh_v1\"] = A.fdr(df.p[v].values)[0]\n    df.loc[v, \"p_bonf_v1\"] = np.minimum(df.p[v] * 9, 1)\n    return df\nfor pool in [True, False]:\n    ct = cell_tests(pool)\n    v = ct[ct.region == \"V1\"].copy()\n    print(f\"45 {'pooled (c)' if pool else 'averaged (d)'}\")\n    show = v.copy()\n    for c in [\"p\", \"p_bh_all\", \"p_bonf_all\", \"p_bh_v1\", \"p_bonf_v1\"]:\n        show[c] = show[c].map(lambda x: f\"{x:.2g}\")\n    print(show.round(3).to_string())\n    for col in [\"p_bh_v1\", \"p_bh_all\", \"p_bonf_v1\", \"p_bonf_all\"]:\n        other = v[~((v.tertile == \"high\") & (v.rel == 90))]\n        hi90 = v[(v.tertile == \"high\") & (v.rel == 90)].iloc[0]\n        n_ok = int(((other[col] < 0.05) & (other.ratio < 1)).sum())\n        print(f\"  {col}: {n_ok} of 8 other cells below 1 at corrected p < 0.05; high OSI at 90: \"\n              f\"ratio {hi90.ratio:.3f}, corrected p {hi90[col]:.2g}\")\n\n# %% md\n# ## fig2-thalamus-no-tuning-dependence\n#\n# > In LGN and LP, 1-back adaptation does not depend on the adaptor and test orientation relative\n# > to preference, nor does that dependence interact with orientation selectivity.\n#\n# A claim of absence, judged on the paper's test: the 3 x 3 mixed ANOVA at alpha 0.05, in the main\n# reading of the V1 claim (log ratios, pooled 45 degrees); the other readings are shown.\n\n# %% tags=claim:fig2-thalamus-no-tuning-dependence\nprint(anova_table(A.THALAMUS).round(3).to_string())\nfor region in A.THALAMUS:\n    R, tert, _ = CELLS[(region, True)]\n    for t_ in [\"low\", \"medium\", \"high\"]:\n        print(region, t_, \"ratios at 0, 45, 90:\", np.round(np.exp(np.log(R[tert == t_]).mean(0)), 3),\n              \"units\", int((tert == t_).sum()))\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb_part4.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && ./dev.sh $TMPDIR/nb_part{1,2,3,4}.py 2>&1 | sed -n '/fig2\|scale\|ratio by/,$p' | tail -110
```

```
region       level45  scale  units  dropped   F_rel    p_rel  F_int    p_int     df  ratio0  ratio45  ratio90
0     V1    pooled (c)    log    502       78  19.972  3.1e-09  3.280    0.011  2,998   0.799    0.875    0.927
1     V1    pooled (c)  ratio    502       78  27.918  1.6e-12  8.123  1.9e-06  2,998   0.799    0.875    0.927
2     V1  averaged (d)    log    484       96  22.594  2.6e-10  2.987    0.018  2,962   0.802    0.918    0.923
3     V1  averaged (d)  ratio    484       96  30.956  9.4e-14  8.739  6.3e-07  2,962   0.802    0.918    0.923

V1 ratio by tertile (rows) and relative orientation 0, 45, 90 (pooled 45):
low [0.841 0.883 0.898] units 194
medium [0.792 0.878 0.918] units 192
high [0.745 0.857 0.993] units 116

other cortical areas, main effect and interaction (log, pooled 45):
   region     level45 scale  units  dropped   F_rel    p_rel  F_int    p_int     df  ratio0  ratio45  ratio90
0      LM  pooled (c)   log    250       22   3.821    0.023  1.117     0.35  2,494   0.816    0.851    0.892
4      AL  pooled (c)   log    413       22   9.853  5.9e-05  5.580   0.0002  2,820   0.826    0.864    0.922
8      RL  pooled (c)   log    300       25  24.696    5e-11  7.897  3.3e-06  2,594   0.843    0.889    1.029
12     PM  pooled (c)   log    200       10   3.663    0.027  5.136  0.00048  2,394   0.790    0.806    0.867
16     AM  pooled (c)   log    349       18   4.959   0.0073  6.340  5.2e-05  2,692   0.807    0.856    0.875
45 pooled, log: interaction F = 3.28, p = 0.011; spread of ratios over relative orientation by tertile [0.057 0.125 0.248]; largest in high: True
45 pooled, ratio: interaction F = 8.12, p = 1.9e-06; spread of ratios over relative orientation by tertile [0.057 0.125 0.248]; largest in high: True
[... 48 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb_part5.py",
 "content": "# %% md\n# ## fig3a-v1-long-term\n#\n# > V1 neurons adapt significantly to drifting gratings seen up to eight presentations (22 s)\n# > earlier, despite intervening stimuli.\n#\n# t tests of unit log ratios against zero for n = 1 to 10, Benjamini-Hochberg at 0.05 per region\n# (Methods). Every reading of O1 and O3 is run.\n\n# %%\ndef nback_tests(ar, area, region, n_range):\n    x = ar[area == region]\n    ps, ts, ms = [], [], []\n    for n in n_range:\n        t_, p, k = A.ttest_log(x[:, n - 1])\n        ps.append(p); ts.append(t_)\n        lr = np.log(x[:, n - 1]); ms.append(np.exp(lr[np.isfinite(lr)].mean()))\n    adj, rej = A.fdr(ps)\n    sig = [n for n, r_, m in zip(n_range, rej, ms) if r_ and m < 1]\n    return pd.DataFrame(dict(n=list(n_range), ratio=ms, t=ts, p=ps, p_fdr=adj, sig=rej)), sig\n\ndef readings_sig(stim, region, n_range):\n    rows = []\n    for (st, bl, bk), d in D.items():\n        if st != stim:\n            continue\n        for how in [\"pooled\", \"per_ori\", \"per_ori_geo\"]:\n            _, sig = nback_tests(AR[(st, bl, bk)][how], d[\"area\"], region, n_range)\n            rows.append(dict(O1=how, blanks=bl, blocks=bk, significant=sig,\n                             largest=max(sig) if sig else 0))\n    return pd.DataFrame(rows)\n\n# %% tags=claim:fig3a-v1-long-term\ntv1, sig_v1 = nback_tests(ar_dg, DG[\"area\"], \"V1\", range(1, 11))\nshow = tv1.copy(); show[[\"p\", \"p_fdr\"]] = show[[\"p\", \"p_fdr\"]].map(lambda x: f\"{x:.2g}\")\nprint(show.round(4).to_string())\nprint(\"main reading: significant n\", sig_v1, \"largest\", max(sig_v1))\nrs_v1 = readings_sig(\"dg\", \"V1\", range(1, 11))\nprint(rs_v1.to_string())\n# By session: the number of mice whose V1 units' mean 8-back log ratio is below zero.\nlr8 = np.log(ar_dg[DG[\"area\"] == \"V1\", 7])\nby = pd.Series(lr8).groupby(DG[\"sess\"][DG[\"area\"] == \"V1\"]).mean()\nprint(f\"8-back: {int((by < 0).sum())} of {len(by)} mice with mean V1 log ratio below zero\")\n\n# %% md\n# ## fig3a-v1-double-exponential\n#\n# > The decay of V1 adaptation over n-back trials is captured by a double exponential with a fast\n# > (13.99%, 0.85 trials) and a slow (3.45%, 6.82 trials) component.\n#\n# Least squares on log ratios against the log of the model, n = 1 to 50, bounds of the Methods\n# (O5). The fit to the region's mean log ratio (O5a) and to every unit's log ratio (O5b) have the\n# same estimates here, as every unit has a finite value at every n; they differ only in the F test\n# below. Sign reading (a) both terms reduce the response; (b) as printed.\n\n# %%\ndef mean_log(ar, area, region):\n    lr = np.log(ar[area == region])\n    return lr, lr.mean(0)\n\ndef fits_for(ar, area, regions):\n    rows = {}\n    for region in regions:\n        lr, m = mean_log(ar, area, region)\n        for sign in (-1, 1):\n            d, s = A.fit_models(m, sign)\n            F, p = A.ftest(s[1], d[1], len(m))\n            # unit-level F test (O5b): residuals of every unit's log ratio about the model\n            n = np.arange(1, len(m) + 1)\n            rss_d = float(np.sum((lr - np.log(A.model_double(n, *d[0], sign=sign))) ** 2))\n            rss_s = float(np.sum((lr - np.log(A.model_single(n, *s[0]))) ** 2))\n            Fu, pu = A.ftest(rss_s, rss_d, lr.size)\n            rows[(region, sign)] = dict(region=region, sign=\"minus (a)\" if sign < 0 else \"plus (b)\",\n                                        a_fast=100 * d[0][0], tau_fast=d[0][1], a_slow=100 * d[0][2],\n                                        tau_slow=d[0][3], a_single=100 * s[0][0], tau_single=s[0][1],\n                                        F=F, p_F=p, F_units=Fu, p_F_units=pu,\n                                        double_on_bound=A.on_bound(d[0], A.B_D),\n                                        single_on_bound=A.on_bound(s[0], A.B_S))\n    return rows\n\nFIT_DG = fits_for(ar_dg, DG[\"area\"], A.CORTEX + A.THALAMUS)\ndef fit_table(F_, regions):\n    df = pd.DataFrame([v for (r, s), v in F_.items() if r in regions])\n    for c in [\"p_F\", \"p_F_units\"]:\n        df[c] = df[c].map(lambda x: f\"{x:.2g}\")\n    return df\n\n# %% tags=claim:fig3a-v1-double-exponential\nprint(fit_table(FIT_DG, [\"V1\"]).round(3).to_string())\nv = FIT_DG[(\"V1\", -1)]\nci = {\"a_fast\": (10.73, 16.14), \"tau_fast\": (0.59, 1.13), \"a_slow\": (1.71, 6.64), \"tau_slow\": (3.39, 13.5)}\nfor k_, (lo, hi) in ci.items():\n    print(f\"{k_}: {v[k_]:.3f} against Table 1 CI [{lo}, {hi}]: inside {lo <= v[k_] <= hi}\")\nvb = FIT_DG[(\"V1\", 1)]\nprint(f\"sign reading (b): a_slow {vb['a_slow']:.3f}% (the same curve with the slow amplitude's sign flipped)\")\nfit_rows = []\nfor (st, bl, bk), d in D.items():\n    if st != \"dg\":\n        continue\n    for how in [\"pooled\", \"per_ori\", \"per_ori_geo\"]:\n        ar = AR[(st, bl, bk)][how]\n        lr = np.log(ar[d[\"area\"] == \"V1\"])\n        lr = np.where(np.isfinite(lr), lr, np.nan)\n        dd, ss = A.fit_models(np.nanmean(lr, 0), -1)\n        inside = all(lo <= x <= hi for x, (lo, hi) in zip(\n            [100 * dd[0][0], dd[0][1], 100 * dd[0][2], dd[0][3]], ci.values()))\n        fit_rows.append(dict(O1=how, blanks=bl, blocks=bk, a_fast=100 * dd[0][0], tau_fast=dd[0][1],\n                             a_slow=100 * dd[0][2], tau_slow=dd[0][3], all_inside=inside))\nprint(pd.DataFrame(fit_rows).round(3).to_string())\n\n# %% md\n# ## fig3a-v1-half-life\n#\n# > Adaptation in this study has a half-life of about 14 s; read here as the slow V1 component for\n# > drifting gratings.\n#\n# tau_slow x 3 s per trial x ln 2 (criterion).\n\n# %% tags=claim:fig3a-v1-half-life\ntrial_s = float(np.median(isi))\nhl = FIT_DG[(\"V1\", -1)][\"tau_slow\"] * 3 * np.log(2)\nprint(f\"tau_slow {FIT_DG[('V1', -1)]['tau_slow']:.3f} trials; half-life {hl:.2f} s with 3 s per trial \"\n      f\"(measured median onset spacing {trial_s:.3f} s gives {FIT_DG[('V1', -1)]['tau_slow'] * trial_s * np.log(2):.2f} s)\")\nprint(f\"inside 14 +- 1.4 s: {abs(hl - 14) <= 1.4}\")\n\n# %% md\n# ## fig4-cumulative-adaptation\n#\n# > Taken together, 2- to 8-back stimuli would reduce the V1 response by 19%, more than the 17%\n# > reduction from the 1-back stimulus, assuming linear accumulation.\n\n# %% tags=claim:fig4-cumulative-adaptation\nrows = []\nfor (st, bl, bk), d in D.items():\n    if st != \"dg\":\n        continue\n    for how in [\"pooled\", \"per_ori\", \"per_ori_geo\"]:\n        ar = AR[(st, bl, bk)][how]\n        for agg in [\"geo\", \"mean\"]:\n            rv = [A.region_value(ar[d[\"area\"] == \"V1\", n], agg) for n in range(8)]\n            cum = 100 * (1 - np.prod(rv[1:8])); one = 100 * (1 - rv[0])\n            rows.append(dict(O1=how, O2=agg, blanks=bl, blocks=bk, one_back=one, cumulative_2_8=cum,\n                             both_within=abs(cum - 19) <= 1.9 and abs(one - 17) <= 1.7,\n                             cum_exceeds=cum > one))\ncum_tab = pd.DataFrame(rows)\nprint(cum_tab.round(2).to_string())\nprint(\"main reading:\", cum_tab.iloc[0].round(2).to_dict())\n\n# %% md\n# ## fig4b-linear-accumulation\n#\n# > When two adjacent past stimuli both had the current orientation, the observed adaptation\n# > roughly matches that predicted by multiplying the single n-back effects.\n#\n# Observed: rate when the n-back and (n+1)-back gratings both had the current orientation over\n# (c) the rate when both were orthogonal, or (d) the n-back orthogonal and the (n+1)-back any\n# orientation. Predicted: the product of the region's single n-back and (n+1)-back ratios. Pairs\n# (a) 1-2 or (b) every pair from 1-2 to 7-8. 95% CI of the observed ratio by bootstrap over V1\n# units (1000 resamples, the claim's seed).\n\n# %%\ndef pair_ratios(region, blanks=\"hold\", blocks=\"within\"):\n    out = {\"c\": [], \"d\": []}\n    for i, s in enumerate(S):\n        r = select(s, \"dg\", **MAIN)[0]\n        area = s[\"units\"].area.values[s[\"sel\"]]\n        r &= area == region\n        if r.sum() == 0:\n            continue\n        ori, blk, order = A.sequence(s[\"dg\"], None, blanks, blocks)\n        c = s[\"dg_counts\"][r][:, order].astype(float)\n        per = {\"c\": [], \"d\": []}\n        for n in range(1, 8):\n            cur = ori[n + 1:]; p1 = ori[1:-n] if n > 0 else None\n            p1 = ori[n + 1 - n: len(ori) - n]       # n-back of position i is i - n\n            p2 = ori[: len(ori) - n - 1]            # (n+1)-back\n            same = (blk[n + 1:] == blk[: len(ori) - n - 1])\n            def rel(a, b):\n                dlt = np.abs(a - b); return np.minimum(dlt, 180 - dlt)\n            v = same & ~np.isnan(cur) & ~np.isnan(p1) & ~np.isnan(p2)\n            both_rep = v & (rel(cur, p1) == 0) & (rel(cur, p2) == 0)\n            both_orth = v & (rel(cur, p1) == 90) & (rel(cur, p2) == 90)\n            n_orth = v & (rel(cur, p1) == 90)\n            cc = c[:, n + 1:]\n            rep = cc[:, both_rep].mean(1)\n            per[\"c\"].append(rep / cc[:, both_orth].mean(1))\n            per[\"d\"].append(rep / cc[:, n_orth].mean(1))\n        for k in per:\n            out[k].append(np.stack(per[k], 1))\n    return {k: np.concatenate(v) for k, v in out.items()}\n\n# %% tags=claim:fig4b-linear-accumulation\nPR = pair_ratios(\"V1\")\nrng = np.random.default_rng(seed(\"fig4b-linear-accumulation\"))\nsingle = [A.region_value(ar_dg[DG[\"area\"] == \"V1\", n], \"geo\") for n in range(8)]\ndef boot_ci(lr, rng, n_boot=1000):\n    U = len(lr)\n    b = np.array([lr[rng.integers(0, U, U)].mean() for _ in range(n_boot)])\n    return np.exp(np.percentile(b, [2.5, 97.5]))\ndef fig4b_eval(rng, verbose=True):\n    res = {}\n    for base in [\"c\", \"d\"]:\n        lr = np.log(PR[base])\n        rows = []\n        for n in range(1, 8):\n            x = lr[:, n - 1]; ok = np.isfinite(x)\n            lo, hi = boot_ci(x[ok], rng)\n            pred = single[n - 1] * single[n]\n            rows.append(dict(pair=f\"{n}-{n + 1}\", units=int(ok.sum()), dropped=int((~ok).sum()),\n                             observed=np.exp(x[ok].mean()), ci_low=lo, ci_high=hi, predicted=pred,\n                             inside=lo <= pred <= hi))\n        res[base] = pd.DataFrame(rows)\n    return res\nF4 = fig4b_eval(rng)\nfor base, df in F4.items():\n    print(f\"baseline ({base})\"); print(df.round(4).to_string())\n    print(f\"  (a) pair 1-2 inside: {bool(df.inside.iloc[0])}; (b) all pairs inside: {bool(df.inside.all())} \"\n          f\"({int(df.inside.sum())} of 7)\")\nfor k in [1000, 2000, 3000, 4000]:\n    alt = fig4b_eval(np.random.default_rng(seed(\"fig4b-linear-accumulation\") + k))\n    print(f\"seed + {k}: inside per pair, baseline (c) {alt['c'].inside.astype(int).tolist()}, \"\n          f\"(d) {alt['d'].inside.astype(int).tolist()}\")\n\n# %% md\n# ## fig3b-thalamus-short-term\n#\n# > Adaptation to drifting gratings in the thalamus is limited to the 1-back trial in LGN and the\n# > 2-back trial in LP, while cortical areas stay significant for about 6 to 8 trials.\n\n# %% tags=claim:fig3b-thalamus-short-term\nrows = []\nfor region in A.CORTEX + A.THALAMUS:\n    df, sig = nback_tests(ar_dg, DG[\"area\"], region, range(1, 11))\n    rows.append(dict(region=region, significant=sig, largest=max(sig) if sig else 0,\n                     ratios_1_10=np.round(df.ratio.values, 3).tolist()))\nsig_tab = pd.DataFrame(rows)\nprint(sig_tab.to_string())\nfor region in A.THALAMUS + [\"RL\"]:\n    print(region, \"under every reading of O1 and O3:\")\n    print(readings_sig(\"dg\", region, range(1, 11)).to_string())\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb_part5.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='/tmp/claude-1001/nb_part5.py'; s=open(p).read()
s=s.replace("            cur = ori[n + 1:]; p1 = ori[1:-n] if n > 0 else None\n            p1 = ori[n + 1 - n: len(ori) - n]       # n-back of position i is i - n\n","            cur = ori[n + 1:]\n            p1 = ori[1: len(ori) - n]               # n-back of position i is i - n\n")
open(p,'w').write(s)
EOF
./dev.sh $TMPDIR/nb_part{1,2,3,4,5}.py 2>&1 | sed -n '/^     n    ratio/,$p' | tail -150
```

```
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && ./dev.sh $TMPDIR/nb_part{1,2,3,4,5}.py > out5.txt 2>&1; grep -n "significant n\|Traceback\|Error" out5.txt | head; sed -n '/main reading: significant/,$p' out5.txt | head -150
```

```
437:main reading: significant n [1, 2, 3, 4, 5, 6, 7, 8] largest 8
500:Traceback (most recent call last):
510:TypeError: type str doesn't define __round__ method
main reading: significant n [1, 2, 3, 4, 5, 6, 7, 8] largest 8
             O1  blanks  blocks               significant  largest
0        pooled    hold  within  [1, 2, 3, 4, 5, 6, 7, 8]        8
1       per_ori    hold  within                    [1, 2]        2
2   per_ori_geo    hold  within  [1, 2, 3, 4, 5, 6, 7, 8]        8
3        pooled    hold  across  [1, 2, 3, 4, 5, 6, 7, 8]        8
4       per_ori    hold  across                    [1, 2]        2
5   per_ori_geo    hold  across  [1, 2, 3, 4, 5, 6, 7, 8]        8
6        pooled  remove  within        [1, 2, 3, 4, 5, 8]        8
7       per_ori  remove  within                    [1, 2]        2
8   per_ori_geo  remove  within              [1, 2, 4, 5]        5
9        pooled  remove  across        [1, 2, 3, 4, 5, 8]        8
10      per_ori  remove  across                    [1, 2]        2
11  per_ori_geo  remove  across           [1, 2, 4, 5, 8]        8
8-back: 22 of 32 mice with mean V1 log ratio below zero
  region       sign  a_fast  tau_fast  a_slow  tau_slow  a_single  tau_single      F     p_F  F_units p_F_units  double_on_bound  single_on_bound
0     V1  minus (a)  14.209     0.816   3.755     6.714    17.558       1.415  7.495  0.0015   12.395   4.2e-06            False            False
[... 58 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i 's|^print("main reading:", cum_tab.iloc\[0\].round(2).to_dict())|print("main reading (row 0): 1-back", round(cum_tab.one_back[0], 2), "% and 2- to 8-back", round(cum_tab.cumulative_2_8[0], 2), "%")|' nb_part5.py && ./dev.sh $TMPDIR/nb_part{1,2,3,4,5}.py > out5.txt 2>&1; sed -n '/main reading (row 0)/,$p' out5.txt | head -150
```

```
main reading (row 0): 1-back 17.88 % and 2- to 8-back 20.36 %
baseline (c)
  pair  units  dropped  observed  ci_low  ci_high  predicted  inside
0  1-2    578        2    0.7648  0.7381   0.7925     0.7536    True
1  2-3    579        1    0.8985  0.8709   0.9270     0.8989    True
2  3-4    580        0    0.9546  0.9262   0.9853     0.9453    True
3  4-5    580        0    0.9259  0.8982   0.9503     0.9394    True
4  5-6    580        0    0.9525  0.9244   0.9832     0.9524    True
5  6-7    579        1    0.9503  0.9227   0.9782     0.9589    True
6  7-8    579        1    0.9585  0.9292   0.9896     0.9639    True
  (a) pair 1-2 inside: True; (b) all pairs inside: True (7 of 7)
baseline (d)
  pair  units  dropped  observed  ci_low  ci_high  predicted  inside
0  1-2    578        2    0.7882  0.7649   0.8105     0.7536   False
1  2-3    579        1    0.8976  0.8745   0.9223     0.8989    True
2  3-4    580        0    0.9489  0.9271   0.9715     0.9453    True
3  4-5    580        0    0.9256  0.9028   0.9482     0.9394    True
4  5-6    580        0    0.9493  0.9255   0.9736     0.9524    True
5  6-7    579        1    0.9375  0.9142   0.9606     0.9589    True
6  7-8    580        0    0.9458  0.9218   0.9691     0.9639    True
[... 57 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat >> nb_part5.py <<'EOF'
# Significance regardless of direction (a two-tailed test can also find a ratio above 1).
for region in A.THALAMUS:
    df, _ = nback_tests(ar_dg, DG["area"], region, range(1, 11))
    print(region, "significant in either direction:", df.n[df.sig].tolist(),
          "ratios there", np.round(df.ratio[df.sig].values, 3).tolist())
rows = []
for (st, bl, bk), d in D.items():
    if st != "dg":
        continue
    for how in ["pooled", "per_ori", "per_ori_geo"]:
        ar = AR[(st, bl, bk)][how]
        lg = {}
        for region in A.CORTEX + A.THALAMUS:
            df, sig = nback_tests(ar, d["area"], region, range(1, 11))
            lg[region] = max(sig) if sig else 0
            lg[region + "_any"] = df.n[df.sig].tolist()
        ok = (lg["LGN"] <= 1 and lg["LP"] <= 2 and all(lg[c] >= 6 for c in A.CORTEX))
        rows.append(dict(O1=how, blanks=bl, blocks=bk, **{k: v for k, v in lg.items() if not k.endswith("_any")},
                         LGN_any=lg["LGN_any"], LP_any=lg["LP_any"], criterion_met=ok))
print(pd.DataFrame(rows).to_string())
EOF
cat > nb_part6.py <<'EOF'
# %% md
# ## v1-vs-thalamus-welch
#
# > Adaptation to remote stimuli is stronger in V1 than in LGN (2-, 4- and 9-back) and LP
# > (3-back), even after normalizing to each region's 1-back adaptation.
#
# Per n, a two-sided Welch t test of unit values in V1 against LGN and against LP. Values: the
# unnormalized log ratio, (a) each unit's n-back log ratio divided by its own 1-back log ratio,
# (b) divided by its region's mean 1-back log ratio. Normalized values are signed so that larger
# means more adaptation; for the unnormalized log ratio, more negative is more adaptation. n in
# (c) 2 to 10 or (d) 2 to 50, Benjamini-Hochberg within each pair of regions (O6).

# %% tags=claim:v1-vs-thalamus-welch
lr_dg = np.log(ar_dg)
def welch(region, norm, n_max):
    a = lr_dg[DG["area"] == "V1"]; b = lr_dg[DG["area"] == region]
    if norm == "unit":
        a = a / a[:, [0]]; b = b / b[:, [0]]
    elif norm == "region":
        a = a / a[:, 0].mean(); b = b / b[:, 0].mean()
    else:
        a, b = -a, -b
    ns = list(range(2, n_max + 1))
    res = [stats.ttest_ind(a[:, n - 1], b[:, n - 1], equal_var=False) for n in ns]
    t_ = np.array([r.statistic for r in res]); p = np.array([r.pvalue for r in res])
    adj = A.fdr(p)[0]
    stronger = [n for n, tt, q in zip(ns, t_, adj) if q < 0.05 and tt > 0]
    weaker = [n for n, tt, q in zip(ns, t_, adj) if q < 0.05 and tt < 0]
    return pd.DataFrame(dict(n=ns, t=t_, p=p, p_fdr=adj)), stronger, weaker
rows = []
for norm in ["none", "unit", "region"]:
    for n_max in [10, 50]:
        _, sL, wL = welch("LGN", norm, n_max)
        _, sP, wP = welch("LP", norm, n_max)
        hits = [n in sL for n in (2, 4, 9)] + [3 in sP]
        rows.append(dict(normalization=norm, n_range=f"2-{n_max}", V1_stronger_than_LGN=sL,
                         V1_stronger_than_LP=sP, V1_weaker_LGN=wL, V1_weaker_LP=wP,
                         of_four=int(sum(hits))))
print(pd.DataFrame(rows).to_string())
df, _, _ = welch("LGN", "region", 10)
print("\nV1 against LGN, normalized by region (b), n = 2 to 10")
print(df.assign(p=df.p.map(lambda x: f"{x:.2g}"), p_fdr=df.p_fdr.map(lambda x: f"{x:.2g}")).round(3).to_string())
df, _, _ = welch("LP", "region", 10)
print("\nV1 against LP, normalized by region (b), n = 2 to 10")
print(df.assign(p=df.p.map(lambda x: f"{x:.2g}"), p_fdr=df.p_fdr.map(lambda x: f"{x:.2g}")).round(3).to_string())
u1 = lr_dg[:, 0]
print(f"\nunit 1-back log ratios within 0.02 of zero (unstable under (a)): "
      f"{int((np.abs(u1[DG['area'] == 'V1']) < 0.02).sum())} V1, {int((np.abs(u1[DG['area'] == 'LGN']) < 0.02).sum())} LGN, "
      f"{int((np.abs(u1[DG['area'] == 'LP']) < 0.02).sum())} LP")

# %% md
# ## fig3c-mice-long-term
#
# > Long-term (4- to 8-back) adaptation is consistent across mice in cortex but not in thalamus.

# %% tags=claim:fig3c-mice-long-term
for pooled_i, lab in [(0, "trials pooled over 4 to 8"), (1, "rates averaged over 4 to 8")]:
    gC = mouse_rates(DG, A.CORTEX, range(4, 9), A.DG_WIN)[pooled_i]
    gT = mouse_rates(DG, A.THALAMUS, range(4, 9), A.DG_WIN)[pooled_i]
    print(lab)
    ca = consistency(gC, "  cortex")
    ta = consistency(gT, "  thalamus")
    print(f"  cortex meets (a) or (b): {ca[0] or ca[1]}; thalamus meets neither: {not (ta[0] or ta[1])}")

# %% md
# ## decay-cortex-double-better
#
# > Recovery from adaptation to drifting gratings in cortical areas is better fit by a double than
# > a single exponential, in all areas but RL.
#
# F tests of the nested fits (O5): on the region's mean log ratio over n = 1 to 50 (O5a, 50
# observations) and on every unit's log ratio (O5b).

# %% tags=claim:decay-cortex-double-better
ft = fit_table(FIT_DG, A.CORTEX)
print(ft[ft.sign == "minus (a)"].round(3).to_string())
for col in ["p_F", "p_F_units"]:
    pv = {r: float(FIT_DG[(r, -1)][col]) for r in A.CORTEX}
    print(f"{col}: below 0.05 in V1, LM, AL, PM, AM: {all(pv[r] < 0.05 for r in ['V1', 'LM', 'AL', 'PM', 'AM'])}; "
          f"RL p = {pv['RL']:.2g}")
EOF
./dev.sh $TMPDIR/nb_part{1,2,3,4,5,6}.py > out6.txt 2>&1; sed -n '/significant in either/,$p' out6.txt | head -150
```

```
LGN significant in either direction: [1] ratios there [0.935]
LP significant in either direction: [1, 2, 3] ratios there [0.833, 0.939, 1.03]
             O1  blanks  blocks  V1  LM  AL  RL  PM  AM  LGN  LP              LGN_any        LP_any  criterion_met
0        pooled    hold  within   8   8   7   5   7   6    1   2                  [1]     [1, 2, 3]          False
1       per_ori    hold  within   2   1   1   1   1   1    1   1  [1, 2, 3, 4, 9, 10]     [1, 3, 6]          False
2   per_ori_geo    hold  within   8   7   5   6   7   4    1   2               [1, 9]        [1, 2]          False
3        pooled    hold  across   8   8   7   6   7   6    1   2               [1, 9]        [1, 2]           True
4       per_ori    hold  across   2   1   1   1   1   1    1   1  [1, 2, 3, 4, 9, 10]     [1, 3, 6]          False
5   per_ori_geo    hold  across   8   7   6   5   7   4    1   2               [1, 9]        [1, 2]          False
6        pooled  remove  within   8  10   7   5   7   8    7   2               [1, 7]     [1, 2, 3]          False
7       per_ori  remove  within   2   1   1   0   1   2    1   1         [1, 3, 4, 9]     [1, 3, 6]          False
8   per_ori_geo  remove  within   5   4   5   5   7   6    7   2               [1, 7]        [1, 2]          False
9        pooled  remove  across   8  10   7   5   7   8    7   2               [1, 7]     [1, 2, 3]          False
10      per_ori  remove  across   2   1   1   0   1   2    1   1         [1, 3, 4, 9]  [1, 3, 5, 6]          False
11  per_ori_geo  remove  across   8   4   5   5   4   6    7   2               [1, 7]        [1, 2]          False
  normalization n_range V1_stronger_than_LGN V1_stronger_than_LP V1_weaker_LGN V1_weaker_LP  of_four
0          none    2-10            [2, 4, 9]              [3, 4]            []           []        4
1          none    2-50               [2, 4]                 [3]            []         [44]        3
2          unit    2-10                   []                
[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > nb_part7.py <<'EOF'
# %% md
# ## table1-extrastriate-tau-slow
#
# > Recovery from adaptation to drifting gratings is slowest in V1 (tau_slow 6.82 trials), and
# > relatively similar in extrastriate areas, whose slow time constants range from 3.12 to 5.52
# > trials with all 95% CIs overlapping.
#
# Bootstrap of the double-exponential fit (O5): units resampled with replacement 1000 times, fits
# on a bound discarded, 2.5 and 97.5 percentiles (Methods). The claim's seed, and four more for
# the seed's effect.

# %% tags=claim:table1-extrastriate-tau-slow
T1 = {"V1": (3.39, 13.5), "AL": (3.1, 5.94), "AM": (2.37, 6.5), "LM": (3.42, 10.6),
      "PM": (2.75, 9.28), "RL": (2.19, 34.41)}
T1_other = {"V1": [(10.73, 16.14), (0.59, 1.13), (1.71, 6.64)], "AL": [(8.14, 12.71), (1e-3, 0.47), (4.90, 8.54)],
            "AM": [(6.88, 14.30), (5e-3, 0.87), (3.83, 11.04)], "LM": [(10.37, 16.07), (0.02, 0.72), (1.89, 5.84)],
            "PM": [(10.43, 16.32), (2e-3, 0.45), (3.91, 9.26)], "RL": [(1.97, 12.00), (5e-3, 1.83), (0.7, 9.82)]}
t = time.time()
base_seed = seed("table1-extrastriate-tau-slow")
tasks = [(np.log(ar_dg[DG["area"] == r]), "double", base_seed + k) for k in [0, 1000, 2000, 3000, 4000] for r in A.CORTEX]
BOOT_DG = dict(zip([(k, r) for k in [0, 1000, 2000, 3000, 4000] for r in A.CORTEX], A.bootstrap_many(tasks)))
print(f"bootstraps in {time.time() - t:.0f} s")
def overlap_all(cis):
    lo = max(c[0] for c in cis.values()); hi = min(c[1] for c in cis.values())
    return lo <= hi
for k in [0, 1000, 2000, 3000, 4000]:
    cis = {r: tuple(np.percentile(BOOT_DG[(k, r)][0][:, 3], [2.5, 97.5])) for r in A.CORTEX}
    if k == 0:
        rows = []
        for r in A.CORTEX:
            b, dropped = BOOT_DG[(0, r)]
            ci4 = np.percentile(b, [2.5, 97.5], 0)
            est = FIT_DG[(r, -1)]
            rows.append(dict(region=r, tau_slow=est["tau_slow"], boot_low=ci4[0, 3], boot_high=ci4[1, 3],
                             table1_ci=T1[r], inside=T1[r][0] <= est["tau_slow"] <= T1[r][1],
                             a_fast=est["a_fast"], a_fast_in=T1_other[r][0][0] <= est["a_fast"] <= T1_other[r][0][1],
                             tau_fast=est["tau_fast"], tau_fast_in=T1_other[r][1][0] <= est["tau_fast"] <= T1_other[r][1][1],
                             a_slow=est["a_slow"], a_slow_in=T1_other[r][2][0] <= est["a_slow"] <= T1_other[r][2][1],
                             kept=len(b), dropped=dropped))
        t1 = pd.DataFrame(rows)
        print(t1.round(3).to_string())
        ex5 = t1[t1.region != "V1"]
        print(f"extrastriate tau_slow inside Table 1 CI: {int(ex5.inside.sum())} of 5; "
              f"range {ex5.tau_slow.min():.2f} to {ex5.tau_slow.max():.2f}; V1 largest of six: "
              f"{t1.tau_slow.idxmax() == 0}")
    print(f"seed + {k}: all six bootstrapped tau_slow CIs overlap: {overlap_all(cis)}; "
          f"CIs {', '.join(f'{r} [{c[0]:.2f}, {c[1]:.2f}]' for r, c in cis.items())}")

# %% md
# ## decay-thalamus-single
#
# > Recovery in LGN and LP is best described by a single exponential with very short time
# > constants (0.02 and 0.71 trials).

# %% tags=claim:decay-thalamus-single
print(fit_table(FIT_DG, A.THALAMUS).round(4).to_string())
lims = {"LGN": [(0.004, 0.63), (4.04, 8.85)], "LP": [(0.03, 0.93), (12.68, 21.02)]}
for r in A.THALAMUS:
    e = FIT_DG[(r, -1)]
    print(f"{r}: tau {e['tau_single']:.3f} in {lims[r][0]}: {lims[r][0][0] <= e['tau_single'] <= lims[r][0][1]}; "
          f"a {e['a_single']:.2f}% in {lims[r][1]}: {lims[r][1][0] <= e['a_single'] <= lims[r][1][1]}; "
          f"F test p (mean) {e['p_F']:.2g}, (units) {e['p_F_units']:.2g}")
bt = A.bootstrap_many([(np.log(ar_dg[DG["area"] == r]), "single", seed("decay-thalamus-single")) for r in A.THALAMUS])
for r, (b, dropped) in zip(A.THALAMUS, bt):
    print(f"{r} bootstrap (seed of the claim): tau CI [{np.percentile(b[:, 1], 2.5):.3f}, {np.percentile(b[:, 1], 97.5):.3f}], "
          f"a CI [{100 * np.percentile(b[:, 0], 2.5):.2f}, {100 * np.percentile(b[:, 0], 97.5):.2f}]%, dropped {dropped}")

# %% md
# ## fig5-repeat-suppression
#
# > Against a blank baseline, both repeated and orthogonal 1-back gratings suppress cortical
# > responses, but only the suppression by repeated orientations persists, up to eight trials back.
#
# All cortical units pooled. Per unit and n, the rate when the n-back trial was a repeat over the
# rate when it was a blank, and orthogonal over blank; repeat and orthogonal trials are subsampled
# per session to the number of n-back blank trials (Methods). Blanks hold positions (O3a), pairs
# within blocks. Readings of "significant": (a) the bootstrapped 95% CI over units excludes 1;
# (b) t tests of log ratios against zero, n = 1 to 10, Benjamini-Hochberg.

# %%
def blank_ratios(rng, n_max=10):
    rep_all, orth_all = [], []
    for i, s in enumerate(S):
        r = select(s, "dg", **MAIN)[0]
        area = s["units"].area.values[s["sel"]]
        r &= np.isin(area, A.CORTEX)
        if r.sum() == 0:
            continue
        ori, blk, order = A.sequence(s["dg"], None, "hold", "within")
        c = s["dg_counts"][r][:, order].astype(float)
        R, O = np.full((r.sum(), n_max), np.nan), np.full((r.sum(), n_max), np.nan)
        for n in range(1, n_max + 1):
            rep, orth, blank = A.pair_masks(ori, blk, n)
            cc = c[:, n:]
            nb_ = int(blank.sum())
            ri = rng.choice(np.flatnonzero(rep), nb_, replace=False)
            oi = rng.choice(np.flatnonzero(orth), nb_, replace=False)
            b = cc[:, blank].mean(1)
            R[:, n - 1] = cc[:, ri].mean(1) / b
            O[:, n - 1] = cc[:, oi].mean(1) / b
        rep_all.append(R); orth_all.append(O)
    return np.concatenate(rep_all), np.concatenate(orth_all)

def fig5_eval(R, O, rng_boot):
    rows = []
    for name, X in [("repeat/blank", R), ("orthogonal/blank", O)]:
        lr = np.log(X)
        ps = []
        for n in range(1, X.shape[1] + 1):
            x = lr[:, n - 1]; x = x[np.isfinite(x)]
            lo, hi = boot_ci(x, rng_boot, 1000)
            p = stats.ttest_1samp(x, 0).pvalue; ps.append(p)
            rows.append(dict(ratio=name, n=n, units=len(x), value=np.exp(x.mean()), ci_low=lo, ci_high=hi, p=p))
    df = pd.DataFrame(rows)
    for name in ["repeat/blank", "orthogonal/blank"]:
        m = df.ratio == name
        df.loc[m, "p_fdr"] = A.fdr(df.p[m].values)[0]
    df["below_ci"] = df.ci_high < 1
    df["below_t"] = (df.p_fdr < 0.05) & (df.value < 1)
    return df

def fig5_criterion(df, col):
    r = df[df.ratio == "repeat/blank"].set_index("n"); o = df[df.ratio == "orthogonal/blank"].set_index("n")
    ok = (r.value[1] < 1 and o.value[1] < 1 and not o[col].loc[2:10].any()
          and bool(r[col][8]) and int(r[col].loc[2:8].sum()) >= 4)
    return ok, r[col].loc[1:10].astype(int).tolist(), o[col].loc[1:10].astype(int).tolist()

# %% tags=claim:fig5-repeat-suppression
s5 = seed("fig5-repeat-suppression")
blank_counts = [int(A.pair_masks(*A.sequence(s["dg"], None, "hold", "within")[:2], 1)[2].sum()) for s in S]
print("1-back blank trials per session:", min(blank_counts), "to", max(blank_counts))
R5, O5 = blank_ratios(np.random.default_rng(s5))
df5 = fig5_eval(R5, O5, np.random.default_rng(s5 + 1))
show = df5.copy(); show[["p", "p_fdr"]] = show[["p", "p_fdr"]].map(lambda x: f"{x:.2g}")
print(show.round(4).to_string())
for col, lab in [("below_ci", "(a) bootstrap CI"), ("below_t", "(b) t test with FDR")]:
    ok, rr, oo = fig5_criterion(df5, col)
    print(f"{lab}: criterion met {ok}; repeat below 1 at n=1..10 {rr}; orthogonal {oo}")
for k in [1000, 2000, 3000, 4000]:
    Rk, Ok = blank_ratios(np.random.default_rng(s5 + k))
    dk = fig5_eval(Rk, Ok, np.random.default_rng(s5 + k + 1))
    print(f"seed + {k}: (a) {fig5_criterion(dk, 'below_ci')}, (b) {fig5_criterion(dk, 'below_t')}")
# Variant: 100 subsampling draws, the unit ratios averaged in log over draws.
rngv = np.random.default_rng(s5 + 2)
acc_r, acc_o = [], []
for _ in range(100):
    Rk, Ok = blank_ratios(rngv)
    acc_r.append(np.log(Rk)); acc_o.append(np.log(Ok))
with warnings.catch_warnings():
    warnings.simplefilter("ignore", RuntimeWarning)
    Rv = np.exp(np.nanmean(np.where(np.isfinite(acc_r), acc_r, np.nan), 0))
    Ov = np.exp(np.nanmean(np.where(np.isfinite(acc_o), acc_o, np.nan), 0))
dv = fig5_eval(Rv, Ov, np.random.default_rng(s5 + 3))
print("100 draws:", "(a)", fig5_criterion(dv, "below_ci"), "(b)", fig5_criterion(dv, "below_t"))
print(dv[["ratio", "n", "value", "ci_low", "ci_high"]].round(4).to_string())
EOF
./dev.sh $TMPDIR/nb_part{1,2,3,4,5,6,7}.py > out7.txt 2>&1; sed -n '/bootstraps in/,$p' out7.txt | head -150; date -u
```

```
bootstraps in 154 s
  region  tau_slow  boot_low  boot_high      table1_ci  inside  a_fast  a_fast_in  tau_fast  tau_fast_in  a_slow  a_slow_in  kept  dropped
0     V1     6.714     3.788     11.588   (3.39, 13.5)    True  14.209       True     0.816         True   3.755       True  1000        0
1     LM     5.662     3.131     11.934   (3.42, 10.6)    True  13.846       True     0.508         True   3.344       True   995        5
2     AL     3.929     2.879      6.411    (3.1, 5.94)    True  10.287       True     0.032         True   6.877       True  1000        0
3     RL     2.827     1.967     35.112  (2.19, 34.41)    True   4.285       True     0.269         True   8.155       True   977       23
4     PM     4.274     2.454     12.771   (2.75, 9.28)    True  13.579       True     0.007         True   6.928       True   999        1
5     AM     3.232     2.276      5.949    (2.37, 6.5)    True   9.646       True     0.342         True   8.428       True  1000        0
extrastriate tau_slow inside Table 1 CI: 5 of 5; range 2.83 to 5.66; V1 largest of six: True
seed + 0: all six bootstrapped tau_slow CIs overlap: True; CIs V1 [3.79, 11.59], LM [3.13, 11.93], AL [2.88, 6.41], RL [1.97, 35.11], PM [2.45, 12.77], AM [2.28, 5.95]
seed + 1000: all six bootstrapped tau_slow CIs overlap: True; CIs V1 [3.88, 11.08], LM [3.37, 11.92], AL [2.78, 6.71], RL [2.01, 33.53], PM [2.54, 13.65], AM [2.34, 5.43]
seed + 2000: all six bootstrapped tau_slow CIs overlap: True; CIs V1 [3.92, 11.58], LM [3.18, 13.92], AL [2.83, 6.38], RL [1.95, 32.23], PM [2.41, 15.53], AM [2.33, 5.78]
seed + 3000: all six bootstrapped tau_slow CIs overlap: True; CIs V1 [3.76, 11.77], LM [3.55, 13.39], AL [2.85, 5.94], RL [1.80, 33.52], PM [2.35, 12.39], AM [2.35, 5.61]
seed + 4000: all six bootstrapped tau_slow CIs overlap: True; CIs V1 [3.83, 11.29], LM [3.38, 15.45], AL [2.88, 6.78], RL [1.98, 34.42], PM [2.48, 13.63], AM [2.30, 5.68]
  region       sign   a_fast  tau_fast   a_slow  tau_slow  a_s
[... 137 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='/tmp/claude-1001/nb_part7.py'; s=open(p).read()
s=s.replace("""            b = cc[:, blank].mean(1)
            R[:, n - 1] = cc[:, ri].mean(1) / b
            O[:, n - 1] = cc[:, oi].mean(1) / b""","""            b = cc[:, blank].mean(1)
            with np.errstate(divide="ignore", invalid="ignore"):
                R[:, n - 1] = cc[:, ri].mean(1) / b
                O[:, n - 1] = cc[:, oi].mean(1) / b""")
s=s.replace("""        lr = np.log(X)
        ps = []""","""        with np.errstate(divide="ignore", invalid="ignore"):
            lr = np.log(X)
        ps = []""")
s=s.replace("""            p = stats.ttest_1samp(x, 0).pvalue; ps.append(p)
            rows.append(dict(ratio=name, n=n, units=len(x),""","""            p = stats.ttest_1samp(x, 0).pvalue; ps.append(p)
            rows.append(dict(ratio=name, n=n, units=len(x), dropped=int(np.sum(~np.isfinite(lr[:, n - 1]))),""")
s=s.replace("""    acc_r.append(np.log(Rk)); acc_o.append(np.log(Ok))""","""    with np.errstate(divide="ignore", invalid="ignore"):
        acc_r.append(np.log(Rk)); acc_o.append(np.log(Ok))""")
open(p,'w').write(s)
EOF
./dev.sh $TMPDIR/nb_part{1,2,3,4,5,6,7}.py > out7.txt 2>&1; sed -n '/1-back blank trials/,$p' out7.txt | head -150; date -u
```

```
1-back blank trials per session: 24 to 30
               ratio   n  units  dropped   value  ci_low  ci_high         p     p_fdr  below_ci  below_t
0       repeat/blank   1   2186        3  0.7574  0.7423   0.7713  7.9e-154  7.9e-153      True     True
1       repeat/blank   2   2185        4  0.9154  0.9010   0.9301   1.4e-25   6.8e-25      True     True
2       repeat/blank   3   2184        5  0.9680  0.9518   0.9842   6.7e-05   0.00017      True     True
3       repeat/blank   4   2189        0  0.9684  0.9537   0.9828   6.3e-05   0.00017      True     True
4       repeat/blank   5   2187        2  0.9810  0.9643   0.9975     0.031     0.052      True    False
5       repeat/blank   6   2187        2  0.9856  0.9715   1.0022     0.076     0.085     False    False
6       repeat/blank   7   2187        2  0.9692  0.9537   0.9859   0.00018   0.00035      True     True
7       repeat/blank   8   2184        5  0.9987  0.9839   1.0152      0.87      0.87     False    False
8       repeat/blank   9   2185        4  0.9841  0.9695   0.9992     0.046     0.058      True    False
9       repeat/blank  10   2186        3  1.0167  1.0012   1.0330     0.043     0.058     False    False
10  orthogonal/blank   1   2189        0  0.9223  0.9086   0.9371   1.4e-23   1.4e-22      True     True
11  orthogonal/blank   2   2186        3  0.9716  0.9571   0.9859   0.00018   0.00089      True     True
12  orthogonal/blank   3   2184        5  1.0131  0.9975   1.0286     0.097      0.24     False    False
13  orthogonal/blank   4   2187        2  0.9833  0.9688   0.9983     0.033      0.11      True    False
14  orthogonal/blank   5   2183        6  0.9973  0.9789   1.0156      0.77      0.85     False    False
15  orthogonal/blank   6   2189        0  1.0013  0.9869   1.0173      0.86      0.86     False    False
16  orthogonal/blank   7   2186        3  0.9973  0.9803   1.0134      0.75      0.85     False    False
17  orthogonal/blank   8   2183        6  0.9888  0.9727   1.0044   
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > nb_part8.py <<'EOF'
# %% md
# ## fig6c-static-v1-1back
#
# > With brief back-to-back static gratings, orientation repetition reduces the V1 response over 0
# > to 250 ms, a 1-back ratio of 0.90.
#
# Rates and responsiveness over 0 to 250 ms; orthogonal is 90 degrees apart; spatial frequency
# and phase pooled; blank sweeps hold positions (O3 with blank sweeps in place of blank trials).

# %% tags=claim:fig6c-static-v1-1back
rows = []
for good in [True, False]:
    for src in ["blank", "spont"]:
        vc = count_regions("sg", rule="mean_plus_sd", src=src, by="orientation", good=good)
        rows.append(dict(good_only=good, gray=src, **{A.AREA_NAMES[k]: int(vc.get(k, 0)) for k in A.AREA_NAMES},
                         other_labels_50=",".join(sorted(vc[(~vc.index.isin(NAMED)) & (vc >= 50)].index))))
print("static responsive units (O4 a, e), by gray source and noise filter")
print(pd.DataFrame(rows).to_string())
print("paper: V1 530 (tolerance 53), LGN 60 (6), LP 16 (1.6)")
r6 = region_stats(ar_sg, SG["area"])
show = r6.copy(); show[["p", "p_fdr"]] = show[["p", "p_fdr"]].map(lambda x: f"{x:.2g}")
print(show.round(4).to_string())
tab6 = onebak_table("sg")
print(tab6.to_string())
print("readings with V1 in [0.89, 0.91]:", int(tab6.V1.between(0.89, 0.91).sum()), "of", len(tab6))

# %% md
# ## fig6c-static-other-areas-1back
#
# > Extrastriate areas show similar 1-back adaptation to static gratings (0.89 to 0.93), and the
# > few responsive LGN and LP neurons also adapt (0.93 and 0.85).

# %% tags=claim:fig6c-static-other-areas-1back
ex6 = r6[r6.area.isin(["LM", "AL", "RL", "PM", "AM"])]
print(f"extrastriate: {ex6.ratio.min():.3f} to {ex6.ratio.max():.3f}, all in [0.801, 1.023]: "
      f"{bool(ex6.ratio.between(0.801, 1.023).all())}, largest corrected p {ex6.p_fdr.max():.2g}")
for a_, (lo, hi), n_paper in [("LGN", (0.93 - 0.093, 0.98), 60), ("LP", (0.85 - 0.085, 0.96), 16)]:
    row = r6[r6.area == a_].iloc[0]
    print(f"{a_}: ratio {row.ratio:.3f}, widened CI [{lo:.3f}, {hi}], match {lo <= row.ratio <= hi}; "
          f"p {row.p:.2g} (corrected {row.p_fdr:.2g}); units {row.n_units} against {n_paper}")
tab6["ex_min"] = tab6[["LM", "AL", "RL", "PM", "AM"]].min(axis=1)
tab6["ex_max"] = tab6[["LM", "AL", "RL", "PM", "AM"]].max(axis=1)
print(tab6[["O1", "O2", "blanks", "blocks", "ex_min", "ex_max", "LGN", "LP"]].to_string())

# %% md
# ## fig6d-static-consistent-across-mice
#
# > Static grating 1-back adaptation is consistent across mice.

# %% tags=claim:fig6d-static-consistent-across-mice
for grp, name in [(A.THALAMUS, "thalamus"), (A.CORTEX, "cortex")]:
    g = mouse_rates(SG, grp, [1], A.SG_WIN)[0]
    consistency(g, f"static 1-back, {name}")

# %% md
# ## fig7a-static-v1-long-term
#
# > After brief static gratings V1 adaptation persists for stimuli up to 20 presentations (5 s)
# > back, with a double exponential decay whose slow time constant is 9.12 trials.
#
# FDR family (a) n = 1 to 20 or (b) 1 to 50; fits as for drifting gratings.

# %% tags=claim:fig7a-static-v1-long-term
FIT_SG = fits_for(ar_sg, SG["area"], A.CORTEX + A.THALAMUS)
for n_max in [20, 50]:
    df, sig = nback_tests(ar_sg, SG["area"], "V1", range(1, n_max + 1))
    print(f"family 1-{n_max}: significant n {sig}; largest {max(sig)}; 20-back significant {20 in sig}; "
          f"20-back ratio {df.ratio[19]:.4f}, corrected p {df.p_fdr[19]:.2g}")
print(fit_table(FIT_SG, ["V1"]).round(3).to_string())
ci2 = {"a_fast": (7.11, 9.23), "tau_fast": (0.37, 0.71), "a_slow": (1.33, 2.91), "tau_slow": (6.09, 14.82)}
e = FIT_SG[("V1", -1)]
for k_, (lo, hi) in ci2.items():
    print(f"{k_}: {e[k_]:.3f} in Table 2 CI [{lo}, {hi}]: {lo <= e[k_] <= hi}")
rs7 = readings_sig("sg", "V1", range(1, 21))
print("family 1-20 under every reading of O1 and O3:"); print(rs7.to_string())

# %% md
# ## fig7b-static-cortex-decay
#
# > Extrastriate areas show similar decay after static gratings, with slow time constants from
# > 6.54 (AM) to 21.78 trials (PM), all better fit by a double exponential.

# %% tags=claim:fig7b-static-cortex-decay
T2 = {"V1": (6.09, 14.82), "AL": (5.24, 39.75), "AM": (3.82, 19.11), "LM": (5.42, 13.36),
      "PM": (13.07, 37.0), "RL": (10.99, 37.51)}
ft2 = fit_table(FIT_SG, A.CORTEX)
print(ft2[ft2.sign == "minus (a)"].round(3).to_string())
t = time.time()
b7 = seed("fig7b-static-cortex-decay")
tasks = [(np.log(ar_sg[SG["area"] == r]), "double", b7 + k) for k in [0, 1000, 2000, 3000, 4000] for r in A.CORTEX]
BOOT_SG = dict(zip([(k, r) for k in [0, 1000, 2000, 3000, 4000] for r in A.CORTEX], A.bootstrap_many(tasks)))
print(f"bootstraps in {time.time() - t:.0f} s")
for k in [0, 1000, 2000, 3000, 4000]:
    cis = {r: tuple(np.percentile(BOOT_SG[(k, r)][0][:, 3], [2.5, 97.5])) for r in A.CORTEX}
    inside = {r: T2[r][0] <= FIT_SG[(r, -1)]["tau_slow"] <= T2[r][1] for r in A.CORTEX}
    print(f"seed + {k}: CIs {', '.join(f'{r} [{c[0]:.2f}, {c[1]:.2f}]' for r, c in cis.items())}; "
          f"all overlap {overlap_all(cis)}; dropped {[BOOT_SG[(k, r)][1] for r in A.CORTEX]}")
print("tau_slow inside Table 2 CI:", inside)
print("F test p (mean):", {r: FIT_SG[(r, -1)]["p_F"] for r in A.CORTEX})
print("F test p (units):", {r: FIT_SG[(r, -1)]["p_F_units"] for r in A.CORTEX})

# %% md
# ## fig7-static-lgn-single
#
# > After static gratings LGN is better described by a single exponential with a shorter time
# > constant (2.93 trials), and the cortex and thalamus difference is less pronounced than for
# > drifting gratings.

# %% tags=claim:fig7-static-lgn-single
e = FIT_SG[("LGN", -1)]
print(fit_table(FIT_SG, ["LGN"]).round(4).to_string())
print(f"LGN single: tau {e['tau_single']:.3f} in [1.36, 7.32]: {1.36 <= e['tau_single'] <= 7.32}; "
      f"a {e['a_single']:.2f}% in [1.80, 6.59]: {1.80 <= e['a_single'] <= 6.59}; F test p {e['p_F']:.2g} "
      f"(units {e['p_F_units']:.2g})")
print(f"reported only: LGN tau static {e['tau_single']:.2f} against drifting {FIT_DG[('LGN', -1)]['tau_single']:.3f} trials")

# %% md
# ## fig7b-static-areas-long-term
#
# > After static gratings, cortical areas show significant adaptation to orientations presented up
# > to 20 trials back, whereas in the thalamus long-term adaptation is less evident.

# %% tags=claim:fig7b-static-areas-long-term
rows = []
for n_max in [20, 50]:
    lg = {}
    for region in A.CORTEX + A.THALAMUS:
        df, sig = nback_tests(ar_sg, SG["area"], region, range(1, n_max + 1))
        lg[region] = max(sig) if sig else 0
        rows.append(dict(family=f"1-{n_max}", region=region, largest=lg[region], significant=sig))
    cort = [lg[r] for r in A.CORTEX]
    some = any(18 <= x <= 22 for x in cort); every = all(18 <= x <= 22 for x in cort)
    thal = all(lg[t_] < min(cort) for t_ in A.THALAMUS)
    print(f"family 1-{n_max}: cortical largest {dict(zip(A.CORTEX, cort))}; thalamic {lg['LGN']}, {lg['LP']}; "
          f"(c) some area in 18-22 {some}; (d) every area {every}; thalamus below every cortical area {thal}")
print(pd.DataFrame(rows).to_string())

# %% md
# ## fig7c-static-long-term-across-mice
#
# > Long-term adaptation to static gratings (5- to 20-back) is consistent across mice.

# %% tags=claim:fig7c-static-long-term-across-mice
for pooled_i, lab in [(0, "trials pooled over 5 to 20"), (1, "rates averaged over 5 to 20")]:
    print(lab)
    consistency(mouse_rates(SG, A.CORTEX, range(5, 21), A.SG_WIN)[pooled_i], "  (a) cortex")
    consistency(mouse_rates(SG, ["V1"], range(5, 21), A.SG_WIN)[pooled_i], "  (b) V1")
    consistency(mouse_rates(SG, A.THALAMUS, range(5, 21), A.SG_WIN)[pooled_i], "  thalamus (reported only)")
EOF
./dev.sh $TMPDIR/nb_part{1,2,3,4,5,6,7,8}.py > out8.txt 2>&1; sed -n '/static responsive units/,$p' out8.txt | head -190; date -u
```

```
static responsive units (O4 a, e), by gray source and noise filter
   good_only   gray   V1   LM   AL   RL   PM   AM  LGN  LP other_labels_50
0       True  blank  545  176  230  128  159  179   61  17                
1       True  spont  553  209  358  230  238  356   80  43        VIS,grey
2      False  blank  564  184  237  133  163  186   68  22            grey
3      False  spont  575  217  369  240  243  373   88  55        VIS,grey
paper: V1 530 (tolerance 53), LGN 60 (6), LP 16 (1.6)
  area  n_units   ratio  ci_low  ci_high        t        p    p_fdr
0   V1      545  0.8968  0.8886   0.9049 -23.5612    4e-85  3.2e-84
1   LM      176  0.8913  0.8749   0.9079 -12.2573  2.5e-25  6.6e-25
2   AL      230  0.9102  0.8965   0.9241 -12.1887  1.1e-26  4.6e-26
3   RL      128  0.9297  0.9094   0.9504  -6.5570  1.3e-09  1.7e-09
4   PM      159  0.8957  0.8768   0.9150 -10.1917  4.6e-19  7.4e-19
5   AM      179  0.9102  0.8964   0.9243 -12.0898    6e-25  1.2e-24
6  LGN       61  0.9569  0.9305   0.9840  -3.1534   0.0025   0.0029
7   LP       17  0.9002  0.8414   0.9631  -3.2980   0.0045   0.0045
             O1    O2  blanks  blocks     V1     LM     AL     RL     PM     AM    LGN     LP
0        pooled   geo    hold  within  0.897  0.891  0.910  0.930  0.896  0.910  0.957  0.900
1        pooled  mean    hold  within  0.902  0.898  0.916  0.937  0.904  0.915  0.962  0.907
2       per_ori   geo    hold  within  0.861  0.856  0.878  0.878  0.855  0.865  0.960  0.903
[... 125 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > nb_part9.py <<'EOF'
# %% md
# ## fig8-no-spurious-long-term
#
# > A simulated neuron with only 1-back adaptation, shown the experiments' own stimulus sequences,
# > shows no spurious adaptation to stimuli further back, for drifting or static gratings.
#
# For each session's sequence (blanks holding positions, pairs within blocks), a neuron that
# responds equally to every grating, reduced by the empirical V1 1-back ratio of that stimulus set
# when the 1-back grating had the same orientation (Figure 8 legend). Noise readings: (a) Poisson
# counts at the V1 median rate on orthogonal 1-back trials, the claim's seed; (b) no noise. The
# simulated responses are analysed as the data (pooled ratio per n). 95% CI across the 32
# sequences (t interval of the mean log ratio). Ranges of n: (c) 2 to 10, (d) 2 to 50.

# %% tags=claim:fig8-no-spurious-long-term
def simulate(stim, truth, rate, win, rng, noise):
    out = []
    for s in S:
        table = s[stim]
        ori, blk, order = A.sequence(table, None, "hold", "within")
        rep1 = np.zeros(len(ori), bool)
        r_, o_, b_ = A.pair_masks(ori, blk, 1)
        rep1[1:] = r_
        lam = rate * win * np.where(rep1, truth, 1.0)
        c = rng.poisson(lam) if noise else lam
        counts = np.zeros(len(table)); counts[order] = c
        nb, _ = A.nback_rates(counts[None, :], table, 50, "hold", "within")
        out.append(np.log(A.ratios(nb, "pooled")[0]))
    return np.array(out)
s8 = seed("fig8-no-spurious-long-term")
for stim, ar, d, win in [("dg", ar_dg, DG, A.DG_WIN), ("sg", ar_sg, SG, A.SG_WIN)]:
    truth = A.region_value(ar[d["area"] == "V1", 0], "geo")
    v1 = d["area"] == "V1"
    rate = float(np.median(d["nb"]["os"][v1, 0].sum(1) / d["nb"]["on"][v1, 0].sum(1) / win))
    print(f"{'drifting' if stim == 'dg' else 'static'}: ground truth {truth:.4f}, rate {rate:.2f} Hz")
    for noise, k in [(True, 0), (True, 1000), (True, 2000), (True, 3000), (True, 4000), (False, 0)]:
        L = simulate(stim, truth, rate, win, np.random.default_rng(s8 + k + (0 if stim == "dg" else 1)), noise)
        L = np.where(np.isfinite(L), L, np.nan)
        m = np.nanmean(L, 0); se = np.nanstd(L, 0, ddof=1) / np.sqrt(np.sum(np.isfinite(L), 0))
        lo, hi = np.exp(m - stats.t.ppf(0.975, 31) * se), np.exp(m + stats.t.ppf(0.975, 31) * se)
        ok1 = lo[0] <= truth <= hi[0]
        exc = [n for n in range(2, 51) if not (lo[n - 1] <= 1 <= hi[n - 1])]
        exc10 = [n for n in exc if n <= 10]
        far10 = [n for n in exc10 if abs(np.exp(m[n - 1]) - 1) > 0.01]
        lab = f"Poisson, seed + {k}" if noise else "no noise"
        print(f"  {lab}: 1-back {np.exp(m[0]):.4f} [{lo[0]:.4f}, {hi[0]:.4f}] contains truth {ok1}; "
              f"n in 2-10 whose CI excludes 1 {exc10} (beyond 0.01 of 1: {far10}); in 2-50 {exc}; "
              f"ratios 2-50 from {np.exp(m[1:]).min():.4f} to {np.exp(m[1:]).max():.4f}")

# %% md
# ## robust-threshold-preferred-window
#
# > The results are qualitatively similar with a responsiveness threshold of 2.5 or 10 Hz, when
# > only trials at the neuron's preferred orientation are used (drifting gratings), and with a 0
# > to 100 ms window for static gratings.
#
# Each variant: V1 adaptation significant beyond 1-back (FDR as in the main analysis: n = 1 to 10
# for drifting, 1 to 20 for static, reading (a) of fig7a), V1 better fit by the double exponential
# (F test on the mean, p < 0.05), and for drifting gratings no LGN n beyond 2 significant. The
# preferred-orientation variant uses trials whose current orientation is the unit's preferred and
# whose n-back is the preferred (repeat) or its orthogonal (Methods).

# %% tags=claim:robust-threshold-preferred-window
def variant_eval(ar, area, stim, label):
    n_fam = 10 if stim == "dg" else 20
    _, sig = nback_tests(ar, area, "V1", range(1, n_fam + 1))
    lr = np.log(ar[area == "V1"]); lr = np.where(np.isfinite(lr), lr, np.nan)
    m = np.nanmean(lr, 0)
    dd, ss = A.fit_models(m, -1)
    F, p = A.ftest(ss[1], dd[1], len(m))
    row = dict(variant=label, V1_units=int((area == "V1").sum()),
               V1_nonfinite=int(np.sum(~np.isfinite(np.log(ar[area == "V1"])))),
               V1_sig=sig, V1_beyond_1=any(n > 1 for n in sig), V1_tau_slow=dd[0][3], F_p=p,
               double_better=p < 0.05)
    if stim == "dg":
        _, sl = nback_tests(ar, area, "LGN", range(1, 11))
        row.update(LGN_units=int((area == "LGN").sum()), LGN_sig=sl, LGN_ok=all(n <= 2 for n in sl))
    row["meets"] = row["V1_beyond_1"] and row["double_better"] and row.get("LGN_ok", True)
    return row
rows = []
for thr in [2.5, 10.0]:
    kw = dict(MAIN, thr=thr)
    d = build("dg", sel_kw=kw); rows.append(variant_eval(A.ratios(d["nb"], "pooled"), d["area"], "dg", f"drifting {thr} Hz"))
    d = build("sg", sel_kw=kw); rows.append(variant_eval(A.ratios(d["nb"], "pooled"), d["area"], "sg", f"static {thr} Hz"))
# Preferred orientation only (drifting).
pi = np.array([int(np.flatnonzero(DG["oris"] == p)[0]) for p in DG["pref"]])
u = np.arange(len(pi))
nbp = {k: v[u, :, pi][:, :, None] for k, v in DG["nb"].items()}
nbp = {k: v.reshape(len(pi), -1, 1) for k, v in nbp.items()}
with np.errstate(divide="ignore", invalid="ignore"):
    ar_pref = A.ratios(nbp, "pooled")
rows.append(variant_eval(ar_pref, DG["area"], "dg", "drifting, preferred orientation only"))
d = build("sg", win=A.SG_WIN_SHORT)
rows.append(variant_eval(A.ratios(d["nb"], "pooled"), d["area"], "sg", "static 0-100 ms"))
rob = pd.DataFrame(rows)
print(rob.round(4).to_string())
print(f"variants meeting the reading: {int(rob.meets.sum())} of {len(rob)}")
EOF
./dev.sh $TMPDIR/nb_part{1,2,3,4,5,6,7,8,9}.py > out9.txt 2>&1; sed -n '/ground truth/,$p' out9.txt | head -190; date -u
```

```
drifting: ground truth 0.8212, rate 9.97 Hz
  Poisson, seed + 0: 1-back 0.8032 [0.7694, 0.8385] contains truth True; n in 2-10 whose CI excludes 1 [] (beyond 0.01 of 1: []); in 2-50 [13, 18, 46]; ratios 2-50 from 0.9419 to 1.0482
  Poisson, seed + 1000: 1-back 0.8019 [0.7705, 0.8346] contains truth True; n in 2-10 whose CI excludes 1 [] (beyond 0.01 of 1: []); in 2-50 [40]; ratios 2-50 from 0.9582 to 1.0481
  Poisson, seed + 2000: 1-back 0.8062 [0.7665, 0.8480] contains truth True; n in 2-10 whose CI excludes 1 [8, 9] (beyond 0.01 of 1: [8, 9]); in 2-50 [8, 9, 12, 20, 21, 29, 32, 33]; ratios 2-50 from 0.9502 to 1.0804
  Poisson, seed + 3000: 1-back 0.8324 [0.7929, 0.8740] contains truth True; n in 2-10 whose CI excludes 1 [] (beyond 0.01 of 1: []); in 2-50 [40]; ratios 2-50 from 0.9429 to 1.0508
  Poisson, seed + 4000: 1-back 0.8166 [0.7800, 0.8549] contains truth True; n in 2-10 whose CI excludes 1 [] (beyond 0.01 of 1: []); in 2-50 [14, 21, 32]; ratios 2-50 from 0.9419 to 1.0387
  no noise: 1-back 0.8212 [0.8212, 0.8212] contains truth False; n in 2-10 whose CI excludes 1 [2, 6] (beyond 0.01 of 1: []); in 2-50 [2, 6, 42]; ratios 2-50 from 0.9949 to 1.0034
static: ground truth 0.8968, rate 9.04 Hz
  Poisson, seed + 0: 1-back 0.8961 [0.8840, 0.9084] contains truth True; n in 2-10 whose CI excludes 1 [5, 6] (beyond 0.01 of 1: [5, 6]); in 2-50 [5, 6]; ratios 2-50 from 0.9858 to 1.0090
  Poisson, seed + 1000: 1-back 0.8997 [0.8896, 0.9098] contains truth True; n in 2-10 whose CI excludes 1 [] (beyond 0.01 of 1: []); in 2-50 [33, 37, 38]; ratios 2-50 from 0.9880 to 1.0129
  Poisson, seed + 2000: 1-back 0.8984 [0.8909, 0.9059] contains truth True; n in 2-10 whose CI excludes 1 [] (beyond 0.01 of 1: []); in 2-50 [25, 29, 32]; ratios 2-50 from 0.9901 to 1.0148
  Poisson, seed + 3000: 1-back 0.8895 [0.8797, 0.8994] contains truth True; n in 2-10 whose CI excludes 1 [6] (beyond 0.01 of 1: [6]); in 2-50 [6, 22, 26, 27, 40]; ratios 2-50 from 0.9837 to 1.0126
  Poisson, seed + 
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='/tmp/claude-1001/nb_part2.py'; s=open(p).read()
s=s.replace('def build(stim, sel_kw=MAIN, blanks="hold", blocks="within", n_max=50, win=None):','def build(stim, sel_kw=MAIN, blanks="hold", blocks="within", n_max=50, win=None, short_counts=False):')
s=s.replace('            c = s["sg_counts100"] if win == A.SG_WIN_SHORT else s["sg_counts"]','            c = s["sg_counts100"] if (win == A.SG_WIN_SHORT or short_counts) else s["sg_counts"]')
open(p,'w').write(s)
p='/tmp/claude-1001/nb_part9.py'; s=open(p).read()
s=s.replace('''d = build("sg", win=A.SG_WIN_SHORT)
rows.append(variant_eval(A.ratios(d["nb"], "pooled"), d["area"], "sg", "static 0-100 ms"))''','''d = build("sg", short_counts=True)
rows.append(variant_eval(A.ratios(d["nb"], "pooled"), d["area"], "sg", "static 0-100 ms, units selected on 0-250 ms"))
d = build("sg", win=A.SG_WIN_SHORT)
rows.append(variant_eval(A.ratios(d["nb"], "pooled"), d["area"], "sg", "static 0-100 ms, units selected on 0-100 ms"))''')
# fig8 restructure
old=s[s.index('s8 = seed("fig8-no-spurious-long-term")'):s.index('# %% md\n# ## robust')]
new='''s8 = seed("fig8-no-spurious-long-term")
def sim_eval(L, truth):
    L = np.where(np.isfinite(L), L, np.nan)
    m = np.nanmean(L, 0); se = np.nanstd(L, 0, ddof=1) / np.sqrt(np.sum(np.isfinite(L), 0))
    lo, hi = np.exp(m - stats.t.ppf(0.975, 31) * se), np.exp(m + stats.t.ppf(0.975, 31) * se)
    ok1 = lo[0] - 1e-9 <= truth <= hi[0] + 1e-9
    exc = [n for n in range(2, 51) if not (lo[n - 1] <= 1 <= hi[n - 1])]
    return dict(one_back=np.exp(m[0]), one_low=lo[0], one_high=hi[0], truth_in=ok1,
                excl_2_10=[n for n in exc if n <= 10], excl_2_50=exc,
                excl_2_10_ratios=[round(float(np.exp(m[n - 1])), 4) for n in exc if n <= 10],
                min_2_50=np.exp(m[1:]).min(), max_2_50=np.exp(m[1:]).max(),
                max_dev_2_10=float(np.max(np.abs(np.exp(m[1:10]) - 1))))
SIM = {}
for stim, ar, d, win in [("dg", ar_dg, DG, A.DG_WIN), ("sg", ar_sg, SG, A.SG_WIN)]:
    truth = A.region_value(ar[d["area"] == "V1", 0], "geo")
    v1 = d["area"] == "V1"
    rate = float(np.median(d["nb"]["os"][v1, 0].sum(1) / d["nb"]["on"][v1, 0].sum(1) / win))
    print(f"{'drifting' if stim == 'dg' else 'static'}: ground truth {truth:.4f}, rate {rate:.2f} Hz")
    for noise, k in [(True, 0), (True, 1000), (True, 2000), (True, 3000), (True, 4000), (False, 0)]:
        L = simulate(stim, truth, rate, win, np.random.default_rng(s8 + k + (0 if stim == "dg" else 1)), noise)
        SIM[(stim, noise, k)] = r_ = sim_eval(L, truth)
        print(f"  {'Poisson, seed + ' + str(k) if noise else 'no noise'}: " + ", ".join(
            f"{a}={round(b, 4) if isinstance(b, float) else b}" for a, b in r_.items()))
def fig8_reading(noise, k, rng_n):
    res = {}
    for stim in ["dg", "sg"]:
        r_ = SIM[(stim, noise, k)]
        ex = r_["excl_2_10"] if rng_n == "c" else r_["excl_2_50"]
        res[stim] = r_["truth_in"] and not ex
    return res["dg"] and res["sg"]
for noise in [True, False]:
    for rng_n in ["c", "d"]:
        ks = [0, 1000, 2000, 3000, 4000] if noise else [0]
        print(f"reading ({'a' if noise else 'b'}, {rng_n}): criterion met under seed +k: "
              + ", ".join(f"{k}: {fig8_reading(noise, k, rng_n)}" for k in ks))
for noise in [True, False]:
    part = all(len(SIM[(st, noise, 0)]["excl_2_10"]) <= 1 and all(abs(x - 1) <= 0.01 for x in SIM[(st, noise, 0)]["excl_2_10_ratios"]) for st in ["dg", "sg"])
    print(f"partial rule (no more than one n in 2-10 excluding 1, within 0.01 of 1), {'Poisson' if noise else 'no noise'}: {part}")

'''
s=s.replace(old,new)
open(p,'w').write(s)
EOF
./dev.sh $TMPDIR/nb_part{1,2,3,4,5,6,7,8,9}.py > out9.txt 2>&1; sed -n '/ground truth/,$p' out9.txt | head -190; date -u
```

```
drifting: ground truth 0.8212, rate 9.97 Hz
  Poisson, seed + 0: one_back=0.8032, one_low=0.7694, one_high=0.8385, truth_in=True, excl_2_10=[], excl_2_50=[13, 18, 46], excl_2_10_ratios=[], min_2_50=0.9419, max_2_50=1.0482, max_dev_2_10=0.0336
  Poisson, seed + 1000: one_back=0.8019, one_low=0.7705, one_high=0.8346, truth_in=True, excl_2_10=[], excl_2_50=[40], excl_2_10_ratios=[], min_2_50=0.9582, max_2_50=1.0481, max_dev_2_10=0.0277
  Poisson, seed + 2000: one_back=0.8062, one_low=0.7665, one_high=0.848, truth_in=True, excl_2_10=[8, 9], excl_2_50=[8, 9, 12, 20, 21, 29, 32, 33], excl_2_10_ratios=[0.9578, 0.9563], min_2_50=0.9502, max_2_50=1.0804, max_dev_2_10=0.048
  Poisson, seed + 3000: one_back=0.8324, one_low=0.7929, one_high=0.874, truth_in=True, excl_2_10=[], excl_2_50=[40], excl_2_10_ratios=[], min_2_50=0.9429, max_2_50=1.0508, max_dev_2_10=0.0251
  Poisson, seed + 4000: one_back=0.8166, one_low=0.78, one_high=0.8549, truth_in=True, excl_2_10=[], excl_2_50=[14, 21, 32], excl_2_10_ratios=[], min_2_50=0.9419, max_2_50=1.0387, max_dev_2_10=0.0351
  no noise: one_back=0.8212, one_low=0.8212, one_high=0.8212, truth_in=True, excl_2_10=[2, 6], excl_2_50=[2, 6, 42], excl_2_10_ratios=[0.9963, 1.003], min_2_50=0.9949, max_2_50=1.0034, max_dev_2_10=0.0037
static: ground truth 0.8968, rate 9.04 Hz
  Poisson, seed + 0: one_back=0.8961, one_low=0.884, one_high=0.9084, truth_in=True, excl_2_10=[5, 6], excl_2_50=[5, 6], excl_2_10_ratios=[0.9858, 0.987], min_2_50=0.9858, max_2_50=1.009, max_dev_2_10=0.0142
  Poisson, seed + 1000: one_back=0.8997, one_low=0.8896, one_high=0.9098, truth_in=True, excl_2_10=[], excl_2_50=[33, 37, 38], excl_2_10_ratios=[], min_2_50=0.988, max_2_50=1.0129, max_dev_2_10=0.0096
  Poisson, seed + 2000: one_back=0.8984, one_low=0.8909, one_high=0.9059, truth_in=True, excl_2_10=[], excl_2_50=[25, 29, 32], excl_2_10_ratios=[], min_2_50=0.9901, max_2_50=1.0148, max_dev_2_10=0.0113
  Poisson, seed + 3000: one_back=0.8895, one_low=0.8797, one_high=0.8994, tr
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && head -120 out9.txt
```

```
32 session files at version 0.251116.2246
loaded in 2 s; peak memory of this process 3.16 GB
      subject    session        genotype sex    age  units  good  pass_metrics  dg_rows  dg_blank  dg_blocks  sg_rows  sg_blank  sg_blocks  spont_s  invalid_intervals
0   699733573  715093703    Sst-IRES-Cre   M  P118D   2779  2110           993      628        30          3     6000       189          3     1237                  8
1   703279277  719161530    Sst-IRES-Cre   M  P122D   3232  1852           851      628        30          3     6000       195          3     1237                  1
2   707296975  721123822  Pvalb-IRES-Cre   M  P125D   1603  1191           497      628        30          3     6000       196          3     1237                  5
3   716813540  739448407              wt   M  P112D   2370  1704           703      630        30          3     6000       192          3     1237                  4
4   717038285  732592105              wt   M  P100D   3076  2816           870      628        30          3     6000       193          3     1237                  4
5   718643564  737581020              wt   M  P108D   2055  1463           640      630        30          3     6000       191          3     1237                  9
6   719817799  744228101              wt   M  P122D   2695  1784           745      630        30          3     6000       194          3     1237                  0
7   719828686  754312389              wt   M  P140D   1891  1193           553      630        30          3     6000       194          3     1237                  1
8   722882751  743475441              wt   M  P121D   2133  1459           629      630        30          3     6000       194          3     1237                  8
9   723627600  742951821              wt   M  P120D   3008  2175          1004      630        30          3     6000       194          3     1237                  7
10  726141242  750332458              wt   M   P91D   3047  2127      
[... 107 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && python - <<'EOF'
import h5py, remfile
s3="https://dandiarchive.s3.amazonaws.com/blobs/f5f/175/f5f1752f-5227-47d5-8f75-cd71937878aa"
f=h5py.File(remfile.File(s3),'r')
g=f['intervals/invalid_times']; print(list(g.keys())); print(g['tags'][:20], g['tags_index'][:], g['start_time'][:], g['stop_time'][:])
print(dict(g.attrs))
u=f['units']
for k in ['quality','spike_times','amplitude_cutoff','presence_ratio','isi_violations']: print(k, dict(u[k].attrs).get('description'))
print(dict(f['general/extracellular_ephys/electrodes/location'].attrs))
EOF
```

```
['id', 'start_time', 'stop_time', 'tags', 'tags_index']
[b'EcephysProbe' b'810755801' b'probeC' b'EcephysProbe' b'810755801'
 b'probeC' b'EcephysProbe' b'810755801' b'probeC' b'EcephysProbe'
 b'810755801' b'probeC' b'EcephysProbe' b'810755801' b'probeC'
 b'EcephysProbe' b'810755801' b'probeC' b'EcephysProbe' b'810755801'] [ 3  6  9 12 15 18 21 24] [1830.7  3196.68 4500.09 5589.68 6627.92 7829.74 8850.86  830.52] [1910.47 3281.44 4578.29 5661.9  6854.53 7903.81 8937.06 1846.17]
{'colnames': array(['start_time', 'stop_time', 'tags'], dtype=object), 'description': 'experimental intervals', 'namespace': 'core', 'neurodata_type': 'TimeIntervals', 'object_id': 'a9e2ab43-3e8d-4523-8bfb-28a0d90d254e'}
quality no description
spike_times times (s) of detected spiking events
amplitude_cutoff no description
presence_ratio no description
isi_violations no description
{'description': 'the location of channel within the subject e.g. brain region', 'namespace': 'hdmf-common', 'neurodata_type': 'VectorData', 'object_id': 'b578db4c-b00d-4149-9f72-6341b9f42720'}
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -n 120,160p out9.txt
```

```
6   744228101        39    0.230       -0.019       -0.003    0.155        -0.002         0.012         0.740       0.382
7   754312389       113    0.254        0.033       -0.044    0.174        -0.001        -0.010         0.424       0.337
8   743475441        59    0.251        0.078       -0.035    0.132        -0.003         0.002         0.261       0.156
9   742951821        36    0.241       -0.067       -0.024    0.186         0.004         0.017         0.776       0.511
10  750332458        70    0.350        0.033        0.078    0.235         0.012         0.011         0.637       0.358
11  750749662        61    0.325        0.093       -0.083    0.198        -0.010        -0.003         0.582       0.292
12  746083955        14    0.179        0.141       -0.042    0.195        -0.004         0.005         1.227       0.837
13  754829445       102    0.252        0.032        0.045    0.213         0.010        -0.016         0.826       0.485
14  757970808        93    0.269        0.006        0.005    0.211        -0.017         0.007         0.476       0.288
15  755434585        89    0.194        0.023       -0.005    0.225        -0.012        -0.002         0.552       0.343
16  751348571        53    0.242        0.103        0.027    0.169        -0.003        -0.006         0.686       0.444
17  757216464        93    0.253       -0.011        0.005    0.227         0.004        -0.019         0.684       0.439
18  756029989        55    0.236        0.021       -0.110    0.216        -0.013        -0.011         0.738       0.454
19  758798717        47    0.250       -0.024       -0.046    0.231        -0.008        -0.010         0.855       0.546
20  760693773        99    0.364       -0.002       -0.047    0.265         0.003         0.003         0.469       0.360
21  760345702        85    0.274        0.085        0.027    0.276        -0.007         0.005         0.605       0.366
22  759883607        75    0.170       -0.002   
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='/tmp/claude-1001/nb_part1.py'; s=open(p).read()
s=s.replace("""clock = pd.DataFrame(clock)
print(clock.round(3).to_string())""","""clock = pd.DataFrame(clock)
print(clock.round(3).to_string())
c_ = clock.dropna()
m_dg = c_.dg_true - c_[["dg_shift_p1", "dg_shift_m1"]].max(axis=1)
m_sg = c_.sg_true - c_[["sg_shift_p10", "sg_shift_m10"]].max(axis=1)
print(f"sessions checked {len(c_)}; drifting: true labels above both shifts in {int((m_dg > 0).sum())}, "
      f"margin {m_dg.min():.3f} to {m_dg.max():.3f}; static: in {int((m_sg > 0).sum())}, margin "
      f"{m_sg.min():.3f} to {m_sg.max():.3f}; onset spikes above pre-onset in {int((c_.onset_spikes > c_.pre_spikes).sum())}")""")
open(p,'w').write(s)
EOF
grep -n "HEADER_PLACEHOLDER" nb_part1.py
```

```
4:# HEADER_PLACEHOLDER
Shell cwd was reset to
```

**Agent**

Now the header, results and summary text.

**Agent calls Bash**

```bash
cd $TMPDIR && cat > header.md <<'EOF'
# Paper: Fritsche, Solomon & de Lange (2022), "Brief Stimuli Cast a Persistent Long-Term Trace in
# Visual Cortex", J Neurosci 42(10):1999-2010, doi:10.1523/JNEUROSCI.1350-21.2021. The paper reuses
# the Allen Brain Observatory Visual Coding Neuropixels data.
#
# Dataset: DANDI:000021 (Allen Institute, Visual Coding, Neuropixels, Brain Observatory 1.1
# stimulus set), version 0.251116.2246, doi:10.48324/dandi.000021/0.251116.2246. The paper names
# the dandiset but no version. This is the only published version, and it is the most recent;
# the draft has the same 214 assets and size. It holds the 32 sessions (one per mouse) the paper
# describes, so no earlier version could match the claims file better.
#
# Claims: claims/fritsche-2022.yaml, written from the version of record (PMC8916757; no
# supplement). The paper's code (doi:10.34973/kpt9-y956) is restricted and was not read.
#
# Data are streamed from the archive; nothing is downloaded. Loading reduces each session to spike
# counts per unit and presentation (about 2 to 3 minutes for the 32 files with four processes).
#
# | Claim | Tested |
# |---|---|
# | units-responsive-count | tested |
# | fig1d-v1-1back | tested |
# | fig1d-extrastriate-1back | tested |
# | fig1d-thalamus-1back | tested |
# | fig1e-consistent-across-mice | tested |
# | fig2-v1-tuning-main-effect | tested |
# | fig2-v1-tuning-interaction | tested |
# | fig2-v1-adaptation-at-all-orientations | tested |
# | fig2-thalamus-no-tuning-dependence | tested |
# | fig3a-v1-long-term | tested |
# | fig3a-v1-double-exponential | tested |
# | fig3a-v1-half-life | tested |
# | fig4-cumulative-adaptation | tested |
# | fig4b-linear-accumulation | tested |
# | fig3b-thalamus-short-term | tested |
# | v1-vs-thalamus-welch | tested |
# | fig3c-mice-long-term | tested |
# | decay-cortex-double-better | tested |
# | table1-extrastriate-tau-slow | tested |
# | decay-thalamus-single | tested |
# | fig5-repeat-suppression | tested |
# | fig6c-static-v1-1back | tested |
# | fig6c-static-other-areas-1back | tested |
# | fig6d-static-consistent-across-mice | tested |
# | fig7a-static-v1-long-term | tested |
# | fig7b-static-cortex-decay | tested |
# | fig7-static-lgn-single | tested |
# | fig7b-static-areas-long-term | tested |
# | fig7c-static-long-term-across-mice | tested |
# | fig8-no-spurious-long-term | tested |
# | robust-threshold-preferred-window | tested |
#
# No claim is blocked.
EOF
python - <<'EOF'
p='/tmp/claude-1001/nb_part1.py'; s=open(p).read()
h=open('/tmp/claude-1001/header.md').read().rstrip('\n')
s=s.replace("# # Fritsche, Solomon & de Lange (2022) on DANDI:000021\n#\n# HEADER_PLACEHOLDER","# # Fritsche, Solomon & de Lange (2022) on DANDI:000021\n#\n"+h)
open(p,'w').write(s)
EOF
head -5 nb_part1.py
```

```
# %% md
# # Fritsche, Solomon & de Lange (2022) on DANDI:000021
#
# Paper: Fritsche, Solomon & de Lange (2022), "Brief Stimuli Cast a Persistent Long-Term Trace in
# Visual Cortex", J Neurosci 42(10):1999-2010, doi:10.1523/JNEUROSCI.1350-21.2021. The paper reuses
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/results.py",
 "content": "R = {}\nR[\"sanity\"] = \"\"\"Checks of the description against the data. The files hold 32 mice, one session each: 16\nwild type, 6 Sst-IRES-Cre, 5 Pvalb-IRES-Cre and 5 Vip-IRES-Cre, as the paper says. Drifting\ngratings have the eight directions, five temporal frequencies and contrast 0.8 of the Methods,\nlast 1.985 to 2.018 s and start every 3.003 s, in three blocks with 30 blank trials per session.\nThree sessions (715093703, 719161530, 721123822) hold 598 gratings, not 600; one or two conditions\nthere have 14 presentations. Static gratings have the six orientations, five spatial frequencies\nand four phases, last 0.200 to 0.317 s (median spacing 0.2502 s) with no gap within a block, and\nthere are 189 to 197 blank sweeps among 6000 presentations, about one in 31 (the Methods say\nroughly one in 25). The units table holds every sorted unit, 74658 in all, of which 20182 are\nlabelled `noise` in a `quality` column that has no description; the AllenSDK quality metrics are\nin columns without descriptions or units. Every unit's peak channel has an area label; 3723 of the\nunits that pass the metrics are on channels labelled `grey` and 686 on `VIS`, which name no area.\nNo recording is deposited twice: the first drifting onsets differ in all 32 sessions, and no unit's\ncount vector repeats within or across sessions. Thirteen sessions list invalid intervals, tagged\nwith a probe, some of which overlap the grating epochs; the paper does not mention them and they\nare not applied here. The clock of the spike times and the stimulus tables is consistent with one\nclock: in every session the V1 orientation tuning measured with the true labels exceeds that with\nlabels shifted by one drifting or ten static presentations, and the 0 to 100 ms count exceeds the\ncount in the 100 ms before onset.\"\"\"\n\nR[\"units-responsive-count\"] = \"\"\"**Result: reproduced.** With `noise` units left out and the reading\nO4 a, c, e (over the gray mean + 1 SD of the blank trials, preferred orientation pooled), 2422 units\nare responsive in the eight regions (V1 580, LGN 142, LP 91), each count within tolerance, and all\neight named regions have at least 50. Without the `noise` filter, reading a, d, e also matches\n(2298; V1 548, LGN 153, LP 92). Units on channels labelled `grey` or `VIS` also reach 50; they name\nno region and are not counted as regions.\"\"\"\n\nR[\"fig1d-v1-1back\"] = \"\"\"**Result: reproduced.** Under the main reading the V1 1-back ratio is\n0.821 (t interval 0.804 to 0.839) over 580 units, t = -18.02, p = 6.0e-58, inside [0.81, 0.84].\nFour of the 24 readings fall inside the interval, all with the pooled per-unit ratio (O1a) and the\ngeometric region value (O2a); the per-orientation readings give 0.849 to 0.931.\"\"\"\n\nR[\"fig1d-extrastriate-1back\"] = \"\"\"**Result: reproduced.** The five extrastriate ratios run from 0.795\n(PM) to 0.876 (RL), inside [0.72, 0.968], and the largest corrected p is 2.0e-24. All but the four\nper-orientation arithmetic readings keep every area inside the range.\"\"\"\n\nR[\"fig1d-thalamus-1back\"] = \"\"\"**Result: reproduced.** LGN 0.935 (t interval 0.912 to 0.959, 142\nunits) and LP 0.833 (0.793 to 0.876, 91 units) lie in the paper's intervals, both below 1 at p of\nthe order of 1e-7 and 1e-10 (the table above). Twenty of the 24 readings put both inside.\"\"\"\n\nR[\"fig1e-consistent-across-mice\"] = \"\"\"**Result: partially reproduced.** In cortex all 32 mice have the\northogonal rate above the repeat rate (sign test p = 4.7e-10), reading (a). In thalamus 21 of the\n23 mice with thalamic units do (p = 6.6e-05), so only reading (b) holds there.\"\"\"\n\nR[\"fig2-v1-tuning-main-effect\"] = \"\"\"**Result: reproduced.** In V1 the main effect of relative\norientation is significant under all four readings (p = 3.1e-09 on log ratios with the 45 degree\ntrials pooled, 1.6e-12 to 2.6e-10 under the others), and the 0 degree ratio is the lowest (0.799\nagainst 0.875 at 45 and 0.927 at 90). 78 of 580 V1 units (96 with averaged 45) are left out for a\ncell with no spikes, so the ANOVA has 502 units.\"\"\"\n\nR[\"fig2-v1-tuning-interaction\"] = \"\"\"**Result: reproduced.** The interaction of relative orientation and\nOSI tertile has p = 0.011 (log, pooled 45; 1.9e-06 to 0.018 under the other readings), and the\nspread of ratios over relative orientation grows from 0.057 (low) to 0.125 (medium) to 0.248\n(high OSI).\"\"\"\n\nR[\"fig2-v1-adaptation-at-all-orientations\"] = \"\"\"**Result: reproduced.** With the 45 degree trials\npooled and Benjamini-Hochberg over the nine V1 cells, all eight other cells are below 1 at\ncorrected p < 0.05 (largest 0.012, medium OSI at 90 degrees), and the high OSI cell at 90 degrees\nis not (ratio 0.993, p = 0.92). The same holds with the family of all 72 cells. With Bonferroni 7\n(V1 family) or 6 (all cells) of 8 pass, and with the 45 degree ratios averaged 7 of 8 pass under\nBenjamini-Hochberg.\"\"\"\n\nR[\"fig2-thalamus-no-tuning-dependence\"] = \"\"\"**Result: reproduced.** On the paper's test (log ratios,\npooled 45 degrees) neither LGN (main effect F = 2.17, p = 0.12; interaction F = 1.37, p = 0.25)\nnor LP (F = 0.10, p = 0.91; F = 0.19, p = 0.95) shows an effect at 0.05. No reading reaches 0.05;\nthe smallest p is 0.073 (LGN main effect, averaged 45, log). The LGN ratios per cell run from 0.879\nto 0.991 and LP from 0.795 to 0.863.\"\"\"\n\nR[\"fig3a-v1-long-term\"] = \"\"\"**Result: reproduced.** Under the main reading V1 adaptation is\nsignificant at every n from 1 to 8 and not at 9 or 10 (8-back ratio 0.984), so the largest\nsignificant n is 8. Eight of 12 readings give 8; the per-orientation arithmetic readings stop at\n2, and one geometric reading at 5. In 22 of 32 mice the mean V1 8-back log ratio is below zero.\"\"\"\n\nR[\"fig3a-v1-double-exponential\"] = \"\"\"**Result: reproduced.** The fit gives a_fast 14.21%, tau_fast 0.816\ntrials, a_slow 3.76% and tau_slow 6.71 trials, each inside its Table 1 interval, under sign reading\n(a). Reading (b) fits the same curve with a_slow = -3.76%, which is outside its interval as a\nsigned value. Eight of 12 readings of O1 and O3 put all four inside; the per-orientation arithmetic\nreadings put tau_slow on its bound of 50.\"\"\"\n\nR[\"fig3a-v1-half-life\"] = \"\"\"**Result: reproduced.** tau_slow of 6.714 trials at 3 s per trial gives\na half-life of 13.96 s, within 14 +- 1.4 s (13.97 s with the measured 3.003 s spacing).\"\"\"\n\nR[\"fig4-cumulative-adaptation\"] = \"\"\"**Result: reproduced.** Under the main reading the 1-back\nreduction is 17.88% and the cumulative 2- to 8-back reduction 20.36%, both within tolerance, and\nthe cumulative one is larger. The four pooled geometric readings all match (19.59 to 20.36%\nagainst 16.80 to 17.88%); the arithmetic and per-orientation readings do not.\"\"\"\n\nR[\"fig4b-linear-accumulation\"] = \"\"\"**Result: reproduced.** With the both-orthogonal baseline (c) the\npredicted ratio lies inside the bootstrapped 95% interval of the observed one for all seven pairs\nfrom 1-2 to 7-8 (1-2: observed 0.765, interval 0.738 to 0.793, predicted 0.754), so readings (a)\nand (b) both hold, under all five seeds. With baseline (d) six of seven pairs hold and pair 1-2 does\nnot (0.788, 0.765 to 0.811, predicted 0.754), under all five seeds.\"\"\"\n\nR[\"fig3b-thalamus-short-term\"] = \"\"\"**Result: reproduced, resting on an assumption.** Counting\nsignificant adaptation (a corrected p < 0.05 with the ratio below 1), the reading with pairs formed\nacross blocks (O1a, O3a, d) meets the criterion: LGN only at 1-back, LP to 2-back, and every\ncortical area to 6-back or further (V1 8, LM 8, AL 7, RL 6, PM 7, AM 6). Under the main reading\n(pairs within blocks) RL stops at 5-back and the criterion fails. Counting significance in either\ndirection, LP is also significant at 3-back under the main reading (ratio 1.03, a facilitation),\nand LGN at 9-back under the across-blocks reading; then only the partial rule holds.\"\"\"\n\nR[\"v1-vs-thalamus-welch\"] = \"\"\"**Result: reproduced.** With n = 2 to 10 and correction within each\npair of regions, V1 adaptation is stronger than LGN at exactly 2, 4 and 9 back and than LP at 3\nback, both without normalization (and also LP at 4) and with each region's 1-back mean as the\nnormalization (b). Normalizing each unit by its own 1-back log ratio (a) finds no difference; 38\nV1, 11 LGN and 8 LP units have a 1-back log ratio within 0.02 of zero, which makes that measure\nunstable. Over n = 2 to 50 the corrections leave 1 to 3 of the four.\"\"\"\n\nR[\"fig3c-mice-long-term\"] = \"\"\"**Result: reproduced.** For 4- to 8-back, 31 of 32 mice (pooled\ntrials; 30 with averaged rates) have the cortical orthogonal rate above the repeat rate (sign test\np = 1.5e-08), so cortex meets (b). In thalamus 14 of 23 mice do (p = 0.4), so neither reading holds,\nas the claim expects.\"\"\"\n\nR[\"decay-cortex-double-better\"] = \"\"\"**Result: reproduced.** The F test favours the double exponential\nin V1 (p = 0.0015), LM (0.017), AL (8.0e-05), PM (0.0041) and AM (0.011) on the region means, and\nin all five also with every unit's values (p = 4.2e-06 to 0.0021). RL is not significant (p = 0.22,\nunits 0.12), as in the paper (0.072). Three of the five p values are above the paper's bound of\n0.006.\"\"\"\n\nR[\"table1-extrastriate-tau-slow\"] = \"\"\"**Result: reproduced.** The five extrastriate tau_slow (AL 3.93,\nAM 3.23, LM 5.66, PM 4.27, RL 2.83 trials) are each inside their Table 1 intervals, and the six\nbootstrapped intervals overlap under all five seeds. V1's tau_slow (6.71) is the largest of the\nsix. All a_fast, tau_fast and a_slow estimates are inside their Table 1 intervals too.\"\"\"\n\nR[\"decay-thalamus-single\"] = \"\"\"**Result: reproduced.** The F test does not favour the double\nexponential in LGN (p = 0.81) or LP (p = 0.57; 0.62 and 0.19 with unit values), and the single\nexponential gives LGN tau 0.031 trials and a 6.48%, LP tau 0.712 and a 16.85%, each inside its\nTable 1 interval. The double-exponential fits reach a bound in both.\"\"\"\n\nR[\"fig5-repeat-suppression\"] = \"\"\"**Result: partially reproduced.** Against blank trials both 1-back\nratios are below 1 (repeat 0.757, orthogonal 0.922). Repeat suppression persists longer than\northogonal suppression: by the t tests repeat is significant at 1 to 4 and 7, orthogonal at 1 and\n2. Two parts of the criterion fail under the claim's seed and under all four other seeds: the\northogonal ratio is still below 1 at 2-back (0.972), and repeat is not significant at 8-back\n(0.999). Averaged over 100 subsampling draws, repeat is significant to 8-back, and orthogonal\nstill at 2-back.\"\"\"\n\nR[\"fig6c-static-v1-1back\"] = \"\"\"**Result: reproduced.** Over 0 to 250 ms the V1 static 1-back ratio\nis 0.897 (t interval 0.889 to 0.905) over 545 units, p = 4e-85, inside [0.89, 0.91], and 545 is\nwithin 53 of 530. LGN 61 and LP 17 units match the paper's 60 and 16 with the same selection.\"\"\"\n\nR[\"fig6c-static-other-areas-1back\"] = \"\"\"**Result: reproduced.** Extrastriate ratios run from 0.891 to\n0.930 (largest corrected p 1.7e-09); LGN 0.957 (p = 0.0025) and LP 0.900 (p = 0.0045) are inside\ntheir widened intervals, and the counts (61, 17) are within tolerance.\"\"\"\n\nR[\"fig6d-static-consistent-across-mice\"] = \"\"\"**Result: partially reproduced.** All 32 mice have the\ncortical orthogonal rate above the repeat rate (p = 4.7e-10); in thalamus 15 of 17 mice do (p =\n0.0023), so only reading (b) holds there.\"\"\"\n\nR[\"fig7a-static-v1-long-term\"] = \"\"\"**Result: reproduced.** With the FDR family n = 1 to 20 (a), V1\nadaptation is significant at 20-back (ratio 0.991, corrected p = 9.3e-05), the largest significant\nn; with 1 to 50 (b) the largest is 49, outside 18 to 22. The fit gives a_fast 8.26%, tau_fast\n0.533, a_slow 2.07% and tau_slow 9.47 trials, all inside their Table 2 intervals.\"\"\"\n\nR[\"fig7b-static-cortex-decay\"] = \"\"\"**Result: reproduced.** Every cortical area favours the double\nexponential (F test p from 9.5e-12 to 1.4e-05), every extrastriate tau_slow (AL 13.58, AM 6.29,\nLM 8.24, PM 19.07, RL 19.70) is inside its Table 2 interval, and the six bootstrapped intervals\noverlap under all five seeds. Three of the six p values are above the paper's bound of 1e-5.\"\"\"\n\nR[\"fig7-static-lgn-single\"] = \"\"\"**Result: reproduced.** In LGN the F test does not favour the double\nexponential (p = 0.20; 0.14 with unit values), and the single exponential gives tau 2.77 trials and\na 4.00%, inside their Table 2 intervals. As reported only, the LGN static tau (2.77) is longer than\nthe drifting one (0.031).\"\"\"\n\nR[\"fig7b-static-areas-long-term\"] = \"\"\"**Result: reproduced.** With the family 1 to 20, V1, AL, PM and\nAM are significant at 20-back and LM and RL stop at 15 and 17, so reading (c), some area in 18 to\n22, holds and (d), every area, does not. LGN (largest 5) and LP (9) stay below every cortical\narea. With the family 1 to 50, five cortical areas reach 46 to 49.\"\"\"\n\nR[\"fig7c-static-long-term-across-mice\"] = \"\"\"**Result: partially reproduced.** For 5- to 20-back, 30 of\n32 mice have the cortical orthogonal rate above the repeat rate (p = 2.5e-07) and 29 of 32 for V1\n(p = 2.6e-06), so (b) holds and (a) does not under both readings of the group.\"\"\"\n\nR[\"fig8-no-spurious-long-term\"] = \"\"\"**Result: not reproduced.** The simulated neuron's 1-back ratio\nrecovers the ground truth under every run. Under the claim's seed with Poisson noise (a), no\ndrifting n from 2 to 10 excludes 1, but static 5- and 6-back do (0.986, 0.987); with no noise (b),\nstatic passes and drifting 2- and 6-back exclude 1 (0.996, 1.003). No reading meets the criterion\nor its partial rule under the claim's seed; reading (a, c) meets it under one of the four other\nseeds. The spurious ratios are small: within 0.0037 of 1 for drifting and 0.0007 for static over n\n= 2 to 10 without noise, against V1 drifting ratios of 0.918 to 0.984 at 2- to 8-back.\"\"\"\n\nR[\"robust-threshold-preferred-window\"] = \"\"\"**Result: reproduced.** All seven variants meet the\nreading: V1 adaptation is significant beyond 1-back, V1 favours the double exponential (F test p\n<= 0.0105), and for drifting gratings LGN is significant only at 1-back. This holds at 2.5 and 10\nHz for both stimulus sets, for the preferred-orientation trials, and for static 0 to 100 ms rates\nwith units selected on 0 to 250 ms (545 V1 units) or on 0 to 100 ms (97 V1 units).\"\"\"\n"
}
```

```
File created successfully at: /tmp/claude-1001/results.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='/tmp/claude-1001/results.py'; s=open(p).read()
rep=[("(PM) to 0.876 (RL), inside [0.72, 0.968], and the largest corrected p is 2.0e-24. All but the four\nper-orientation arithmetic readings keep every area inside the range.","(PM) to 0.876 (RL), inside [0.72, 0.968], and the largest corrected p is 2.0e-24. Every reading\nkeeps all five inside the range except the four that average per-orientation ratios and take the\narithmetic region mean."),
("(p = 3.1e-09 on log ratios with the 45 degree\ntrials pooled, 1.6e-12 to 2.6e-10 under the others)","(p = 3.1e-09 on log ratios with the 45 degree\ntrials pooled, 9.4e-14 to 2.6e-10 under the others)"),
("(log, pooled 45; 1.9e-06 to 0.018 under the other readings)","(log, pooled 45; 6.3e-07 to 0.018 under the other readings)"),
("The four pooled geometric readings all match (19.59 to 20.36%\nagainst 16.80 to 17.88%)","The four pooled geometric readings all match (18.89 to 20.36%\nagainst 16.80 to 17.88%)"),
("unstable. Over n = 2 to 50 the corrections leave 1 to 3 of the four.","unstable. Over n = 2 to 50, 3 of the four remain unnormalized and 1 with reading (b)."),
("as in the paper (0.072). Three of the five p values are above the paper's bound of\n0.006.","as in the paper (0.072). Two of the five p values (LM, AM) are above the paper's bound\nof 0.006."),
("overlap under all five seeds. Three of the six p values are above the paper's bound of 1e-5.","overlap under all five seeds. One p value (AM, 1.4e-05) is above the paper's bound of 1e-5."),
]
for a,b in rep:
    assert a in s, a[:40]; s=s.replace(a,b)
open(p,'w').write(s)
p='/tmp/claude-1001/nb_part2.py'; s=open(p).read()
s=s.replace('''r1 = region_stats(ar_dg, DG["area"])
print("main reading (O1a, O2a, O3a+c); CI is the t interval of the mean log ratio")
print(r1.round(4).to_string())''','''r1 = region_stats(ar_dg, DG["area"])
def show_p(df):
    out = df.copy()
    for c in [c for c in out.columns if c.startswith("p")]:
        out[c] = out[c].map(lambda x: f"{x:.2g}")
    return out.round(4).to_string()
print("main reading (O1a, O2a, O3a+c); CI is the t interval of the mean log ratio")
print(show_p(r1))''')
open(p,'w').write(s)
p='/tmp/claude-1001/nb_part3.py'; s=open(p).read()
s=s.replace('print(ex.round(4).to_string())','print(show_p(ex))').replace('print(th.round(5).to_string())','print(show_p(th))')
s=s.replace('rng_tab["ex_min"] = tab1[["LM", "AL", "RL", "PM", "AM"]].min(1)','rng_tab["ex_min"] = tab1[["LM", "AL", "RL", "PM", "AM"]].min(axis=1)').replace('rng_tab["ex_max"] = tab1[["LM", "AL", "RL", "PM", "AM"]].max(1)','rng_tab["ex_max"] = tab1[["LM", "AL", "RL", "PM", "AM"]].max(axis=1)')
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
cd $TMPDIR && cat > summary.md <<'EOF'
# ## Summary
#
# | Claim | Outcome |
# |---|---|
# | units-responsive-count | reproduced |
# | fig1d-v1-1back | reproduced |
# | fig1d-extrastriate-1back | reproduced |
# | fig1d-thalamus-1back | reproduced |
# | fig1e-consistent-across-mice | partially reproduced |
# | fig2-v1-tuning-main-effect | reproduced |
# | fig2-v1-tuning-interaction | reproduced |
# | fig2-v1-adaptation-at-all-orientations | reproduced |
# | fig2-thalamus-no-tuning-dependence | reproduced |
# | fig3a-v1-long-term | reproduced |
# | fig3a-v1-double-exponential | reproduced |
# | fig3a-v1-half-life | reproduced |
# | fig4-cumulative-adaptation | reproduced |
# | fig4b-linear-accumulation | reproduced |
# | fig3b-thalamus-short-term | reproduced (rests on an assumption) |
# | v1-vs-thalamus-welch | reproduced |
# | fig3c-mice-long-term | reproduced |
# | decay-cortex-double-better | reproduced |
# | table1-extrastriate-tau-slow | reproduced |
# | decay-thalamus-single | reproduced |
# | fig5-repeat-suppression | partially reproduced |
# | fig6c-static-v1-1back | reproduced |
# | fig6c-static-other-areas-1back | reproduced |
# | fig6d-static-consistent-across-mice | partially reproduced |
# | fig7a-static-v1-long-term | reproduced |
# | fig7b-static-cortex-decay | reproduced |
# | fig7-static-lgn-single | reproduced |
# | fig7b-static-areas-long-term | reproduced |
# | fig7c-static-long-term-across-mice | partially reproduced |
# | fig8-no-spurious-long-term | not reproduced (seed sensitive) |
# | robust-threshold-preferred-window | reproduced |
#
# A failure to reproduce here may be a failure of this attempt, not of the paper: see the
# reasoning and the differences from the paper's method.
#
# How the analysis differs from the paper's. The paper's code is restricted and was not read.
# The open details of the claims file were each run; the adopted main reading (pooled per-unit
# ratio, geometric region value, blank trials holding positions, pairs within blocks, gray mean
# + 1 SD of the blank trials, preferred orientation pooled, `noise` units left out) is the one the
# unit counts single out, and it gives the paper's 1-back values to within 0.01. The invalid
# intervals listed in the files are not applied. The simulated neuron of Figure 8 needs a rate and
# a noise model the paper does not give; the V1 median rate with Poisson counts, and no noise, were
# run.
#
# What was found about the dataset. The files hold the 32 mice and both stimulus sets the paper
# describes. The units table holds every sorted unit, with a `quality` column marking 20182 of
# 74658 as `noise` and quality metric columns, none of them described in the file; the paper's
# counts are matched when the `noise` units are left out, as the AllenSDK does. Three sessions
# hold 598 drifting gratings in place of 600. Thirteen sessions list probe-tagged invalid
# intervals, some inside the grating epochs. Units on channels labelled `grey` or `VIS` have no
# area.
EOF
cat > build_full.py <<'EOF'
import nbformat, re, sys
exec(open('/tmp/claude-1001/results.py').read())
parts=[open(f'/tmp/claude-1001/nb_part{i}.py').read() for i in range(1,10)]
src='\n'.join(parts)+'\n# %% md\n'+open('/tmp/claude-1001/summary.md').read()
cells=[]
for chunk in re.split(r'^# %%', src, flags=re.M)[1:]:
    head, _, body = chunk.partition('\n')
    head=head.strip(); body=body.strip('\n')
    if head.startswith('md'):
        text='\n'.join(l[2:] if l.startswith('# ') else l.lstrip('#') for l in body.split('\n'))
        cells.append(nbformat.v4.new_markdown_cell(text))
    else:
        tags=[t.strip() for t in head.replace('tags=','').split(',') if t.strip()]
        c=nbformat.v4.new_code_cell(body)
        if tags: c.metadata['tags']=tags
        cells.append(c)
# insert results after the last cell of each tag
out=[]
for i,c in enumerate(cells):
    out.append(c)
    tags=c.metadata.get('tags',[])
    nxt=cells[i+1].metadata.get('tags',[]) if i+1<len(cells) else []
    for t in tags:
        key='sanity' if t=='sanity' else t.split(':',1)[1] if t.startswith('claim:') else None
        if key and t not in nxt:
            out.append(nbformat.v4.new_markdown_cell(' '.join(R[key].split('\n')) if key!='sanity' else R[key].replace('\n',' ')))
missing=[k for k in R if not any(('claim:'+k) in cc.metadata.get('tags',[]) for cc in cells) and k!='sanity']
assert not missing, missing
nb=nbformat.v4.new_notebook(); nb.cells=out
nb.metadata['kernelspec']={'name':'python3','display_name':'Python 3','language':'python'}
nbformat.write(nb, sys.argv[1])
print(len(out),'cells')
EOF
source dev/bin/activate; python build_full.py ~/work/encore/encore/entries/fritsche-2022/reproduce_fritsche_2022.ipynb
```

```
114 cells
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd ~/work/encore/encore && python -c "import json;d=json.load(open('schemas/entry.schema.json'));print(json.dumps(d,indent=0)[:2500])"; grep -n "def check\|error(\|fail(" tools/entry.py | head -60
```

```
{
"$schema": "https://json-schema.org/draft/2020-12/schema",
"title": "An entry: a directory of notebooks with its metadata (entry.yaml)",
"description": "Draft. To be revised after the pilot.",
"type": "object",
"additionalProperties": false,
"required": [
"schema_version",
"name",
"type",
"title",
"description",
"license",
"notebooks",
"related"
],
"properties": {
"schema_version": {
"const": 1
},
[... 149 more lines not kept]
```

**Agent calls Bash**

```bash
cd ~/work/encore/encore/entries/fritsche-2022 && sed -i '/^import matplotlib.pyplot as plt$/d' $TMPDIR/nb_part1.py && cat > entry.yaml <<'EOF'
schema_version: 1
name: fritsche-2022
type: reproduction
title: Long-term orientation adaptation in mouse visual cortex and thalamus (Fritsche et al. 2022)
description: Tests the findings of Fritsche, Solomon and de Lange (2022) on dandiset 000021, the
  Allen Brain Observatory Visual Coding Neuropixels sessions of the Brain Observatory 1.1 stimulus
  set (32 mice). It selects visually responsive units, measures orientation-specific adaptation to
  drifting and static gratings from 1 to 50 presentations back, fits exponential decay models,
  compares cortex with thalamus, and repeats the paper's control analyses.
license: Apache-2.0
notebooks:
- path: reproduce_fritsche_2022.ipynb
  title: Reproducing Fritsche et al. (2022) from dandiset 000021
  runtime_minutes: 15
helpers:
- adaptation.py
related:
- id: dandi:000021/0.251116.2246
  relation: uses_data
- id: doi:10.1523/jneurosci.1350-21.2021
  relation: reproduces
EOF
printf "h5py\nnumpy\npandas\nremfile\nscipy\n" > requirements.in
cd $TMPDIR && source dev/bin/activate && python build_full.py ~/work/encore/encore/entries/fritsche-2022/reproduce_fritsche_2022.ipynb && cd ~/work/encore/encore && python tools/entry.py lock entries/fritsche-2022 2>&1 | tail -5
```

```
114 cells
Traceback (most recent call last):
  File "tools/entry.py", line 59, in <module>
    import yaml
ModuleNotFoundError: No module named 'yaml'
```

**Agent calls Bash**

```bash
cd ~/work/encore/encore && source $TMPDIR/dev/bin/activate && uv pip install -q pyyaml jsonschema nbformat 2>&1 | tail -2; python tools/entry.py lock entries/fritsche-2022 2>&1 | tail -5; python tools/entry.py check entries/fritsche-2022 2>&1 | tail -20
```

```
wrote fritsche-2022/requirements.lock.txt (Python 3.13, with hashes)
0 error(s)
```

**Agent calls Bash**

```bash
date -u; cd ~/work/encore/encore && source $TMPDIR/dev/bin/activate && time python tools/entry.py all entries/fritsche-2022 2>&1 | tail -20; date -u
```

```
Sat Nov 21 06:11:26 UTC 2026
for grp, name in [(A.THALAMUS, "thalamus"), (A.CORTEX, "cortex")]:
    g = mouse_rates(DG, grp, [1], A.DG_WIN)[0]
    consistency(g, f"drifting 1-back, {name}")
    print(f"  rates {g[['rep', 'orth']].min().min():.2f} to {g[['rep', 'orth']].max().max():.2f} Hz")
------------------


[31m---------------------------------------------------------------------------[39m
[31mNameError[39m                                 Traceback (most recent call last)
[36mCell[39m[36m [39m[32mIn[15][39m[32m, line 2[39m
[32m      1[39m [38;5;28;01mfor[39;00m grp, name [38;5;28;01min[39;00m [(A.THALAMUS, [33m"thalamus"[39m), (A.CORTEX, [33m"cortex"[39m)]:
[32m----> [39m[32m2[39m     g = mouse_rates(DG, grp, [[32m1[39m], A.DG_WIN)[[32m0[39m]
[32m      3[39m     consistency(g, f"drifting 1-back, {name}")
[32m      4[39m     print(f"  rates {g[[[33m'rep'[39m, [33m'orth'[39m]].min().min():.2f} to {g[[[33m'rep'[39m, [33m'orth'[39m]].max().max():.2f} Hz")

[31mNameError[39m: name 'mouse_rates' is not defined


0 error(s)
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='/tmp/claude-1001/nb_part3.py'; s=open(p).read()
s=s.replace("# above repeat; (b) a two-sided sign test across mice at p < 0.05.\n\ndef mouse_rates","# above repeat; (b) a two-sided sign test across mice at p < 0.05.\n\n# %%\ndef mouse_rates")
open(p,'w').write(s)
EOF
grep -n "^def \|^# %%" nb_part*.py | awk -F: '{print $1": "$3}' | grep -B1 "def " | head -40
```

```
nb_part1.py: # %%
nb_part1.py: def seed(claim)
--
nb_part1.py: # %% tags=sanity
nb_part1.py: def tuning_index(c, ori, shift)
--
nb_part1.py: # %%
nb_part1.py: def select(s, stim, rule="mean_plus_sd", src="blank", by="orientation", thr=5.0, good=True,
nb_part1.py: def count_regions(stim, **kw)
--
nb_part2.py: # %%
nb_part2.py: def build(stim, sel_kw=MAIN, blanks="hold", blocks="within", n_max=50, win=None, short_counts=False)
nb_part2.py: def onebak_table(stim)
nb_part2.py: def region_stats(ar, area, n=0, regions=A.CORTEX + A.THALAMUS)
--
nb_part2.py: # %% tags=claim
nb_part2.py: def show_p(df)
--
nb_part3.py: # %%
nb_part3.py: def mouse_rates(d, group, ns, win)
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && python build_full.py ~/work/encore/encore/entries/fritsche-2022/reproduce_fritsche_2022.ipynb && python - <<'EOF'
import nbformat
nb=nbformat.read('entries/fritsche-2022/reproduce_fritsche_2022.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type=='markdown' and ('print(' in c.source or 'def ' in c.source or ' = ' in c.source): print(i, c.source[:200])
EOF
cd ~/work/encore/encore && date -u && python tools/entry.py all entries/fritsche-2022 2>&1 | tail -30; date -u
```

```
115 cells
20 **Result: reproduced.** Under the main reading the V1 1-back ratio is 0.821 (t interval 0.804 to 0.839) over 580 units, t = -18.02, p = 6.0e-58, inside [0.81, 0.84]. Four of the 24 readings fall insid
30 **Result: partially reproduced.** In cortex all 32 mice have the orthogonal rate above the repeat rate (sign test p = 4.7e-10), reading (a). In thalamus 21 of the 23 mice with thalamic units do (p = 6
34 **Result: reproduced.** In V1 the main effect of relative orientation is significant under all four readings (p = 3.1e-09 on log ratios with the 45 degree trials pooled, 9.4e-14 to 2.6e-10 under the o
37 **Result: reproduced.** The interaction of relative orientation and OSI tertile has p = 0.011 (log, pooled 45; 6.3e-07 to 0.018 under the other readings), and the spread of ratios over relative orient
40 **Result: reproduced.** With the 45 degree trials pooled and Benjamini-Hochberg over the nine V1 cells, all eight other cells are below 1 at corrected p < 0.05 (largest 0.012, medium OSI at 90 degrees
43 **Result: reproduced.** On the paper's test (log ratios, pooled 45 degrees) neither LGN (main effect F = 2.17, p = 0.12; interaction F = 1.37, p = 0.25) nor LP (F = 0.10, p = 0.91; F = 0.19, p = 0.95)
44 ## fig3a-v1-long-term

> V1 neurons adapt significantly to drifting gratings seen up to eight presentations (22 s)
> earlier, despite intervening stimuli.

t tests of unit log ratios against zero for 
48 ## fig3a-v1-double-exponential

> The decay of V1 adaptation over n-back trials is captured by a double exponential with a fast
> (13.99%, 0.85 trials) and a slow (3.45%, 6.82 trials) component.

Leas
51 **Result: reproduced.** The fit gives a_fast 14.21%, tau_fast 0.816 trials, a_slow 3.76% and tau_slow 6.71 trials, each inside its Table 1 interval, under sign reading (a). Reading (b) fits the same c
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
cd ~/work/encore/encore && ls executed/fritsche-2022/ && source $TMPDIR/dev/bin/activate && python - <<'EOF' > $TMPDIR/exec_out.txt
import nbformat
nb=nbformat.read('executed/fritsche-2022/reproduce_fritsche_2022.ipynb',4)
for c in nb.cells:
    if c.cell_type=='code':
        print('=== CELL', c.metadata.get('tags'))
        for o in c.outputs:
            if 'text' in o: print(o['text'])
            elif 'data' in o and 'text/plain' in o['data']: print(o['data']['text/plain'])
    else:
        if c.source.startswith('**Result'): print('### ', c.source[:100])
EOF
wc -l $TMPDIR/exec_out.txt; diff <(grep -v "loaded in\|bootstraps in\|built in" $TMPDIR/exec_out.txt | grep -v "^===\|^###" ) <(grep -v "loaded in\|bootstraps in\|built in" $TMPDIR/out9.txt) | head -60
```

```
reproduce_fritsche_2022.ipynb
result.json
1046 /tmp/claude-1001/exec_out.txt
2,3d1
< 
< 
46d43
< 
62d58
< 
76d71
< 
115d109
< 
117d110
< 
119d111
< 
153,154d144
< sessions checked 32; drifting: true labels above both shifts in 32, margin 0.038 to 0.366; static: in 32, margin 0.130 to 0.308; onset spikes above pre-onset in 32
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -n "criterion met\|reading (\|variants meeting\|seed + 0:\|extrastriate tau_slow\|family 1-20:\|LGN: tau\|LP: tau\|main reading: sig" exec_out.txt | head -40
```

```
199:main reading (O1a, O2a, O3a+c); CI is the t interval of the mean log ratio
486:main reading: significant n [1, 2, 3, 4, 5, 6, 7, 8] largest 8
513:sign reading (b): a_slow -3.756% (the same curve with the slow amplitude's sign flipped)
561:main reading (row 0): 1-back 17.88 % and 2- to 8-back 20.36 %
749:extrastriate tau_slow inside Table 1 CI: 5 of 5; range 2.83 to 5.66; V1 largest of six: True
750:seed + 0: all six bootstrapped tau_slow CIs overlap: True; CIs V1 [3.79, 11.59], LM [3.13, 11.93], AL [2.88, 6.41], RL [1.97, 35.11], PM [2.45, 12.77], AM [2.28, 5.95]
756:###  **Result: reproduced.** The five extrastriate tau_slow (AL 3.93, AM 3.23, LM 5.66, PM 4.27, RL 2.83 
763:LGN: tau 0.031 in (0.004, 0.63): True; a 6.48% in (4.04, 8.85): True; F test p (mean) 0.81, (units) 0.62
764:LP: tau 0.712 in (0.03, 0.93): True; a 16.85% in (12.68, 21.02): True; F test p (mean) 0.57, (units) 0.19
795:(a) bootstrap CI: criterion met False; repeat below 1 at n=1..10 [1, 1, 1, 1, 1, 0, 1, 0, 1, 0]; orthogonal [1, 1, 0, 1, 0, 0, 0, 0, 0, 0]
796:(b) t test with FDR: criterion met False; repeat below 1 at n=1..10 [1, 1, 1, 1, 0, 0, 1, 0, 0, 0]; orthogonal [1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
912:family 1-20: significant n [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 17, 18, 20]; largest 20; 20-back significant True; 20-back ratio 0.9912, corrected p 9.3e-05
947:seed + 0: CIs V1 [6.64, 14.75], LM [5.41, 14.45], AL [5.36, 38.26], RL [10.63, 39.36], PM [11.71, 31.26], AM [3.45, 18.91]; all overlap True; dropped [0, 0, 27, 12, 0, 2]
966:family 1-20: cortical largest {'V1': 20, 'LM': 15, 'AL': 20, 'RL': 17, 'PM': 20, 'AM': 20}; thalamic 5, 9; (c) some area in 18-22 True; (d) every area False; thalamus below every cortical area True
1003:  Poisson, seed + 0: one_back=0.8032, one_low=0.7694, one_high=0.8385, truth_in=True, excl_2_10=[], excl_2_50=[13, 18, 46], excl_2_10_ratios=[], min_2_50=0.9419, max_2_50=1.0482, max_dev_2_10=0.0336
1016:  Poisson, seed + 0: one_back=0.8961, one_low=0.884, one_high=
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > variant.py <<'EOF'

# %% tags=claim:units-responsive-count
# Variant: the main analyses with `noise` units kept (O4 a, c, e otherwise), to show how much the
# adopted filter matters downstream.
NOISE_KW = dict(MAIN, good=False)
dgv = build("dg", sel_kw=NOISE_KW); sgv = build("sg", sel_kw=NOISE_KW)
arv, arsv = A.ratios(dgv["nb"], "pooled"), A.ratios(sgv["nb"], "pooled")
print("drifting 1-back, noise units kept:", {a: round(A.region_value(arv[dgv["area"] == a, 0]), 3) for a in A.CORTEX + A.THALAMUS})
print("static 1-back, noise units kept:", {a: round(A.region_value(arsv[sgv["area"] == a, 0]), 3) for a in A.CORTEX + A.THALAMUS})
for region in ["V1", "LGN", "LP"]:
    lr = np.log(arv[dgv["area"] == region]); lr = np.where(np.isfinite(lr), lr, np.nan)
    ps = [stats.ttest_1samp(lr[:, n][np.isfinite(lr[:, n])], 0).pvalue for n in range(10)]
    adj, rej = A.fdr(ps)
    m = np.nanmean(lr, 0)
    sig = [n + 1 for n in range(10) if rej[n] and m[n] < 0]
    dd, ss = A.fit_models(m, -1)
    print(f"{region}, noise units kept: {int((dgv['area'] == region).sum())} units; significant n {sig}; "
          f"double fit a_fast {100 * dd[0][0]:.2f}%, tau_fast {dd[0][1]:.3f}, a_slow {100 * dd[0][2]:.2f}%, "
          f"tau_slow {dd[0][3]:.2f}; single tau {ss[0][1]:.3f}")
EOF
python - <<'EOF'
p='/tmp/claude-1001/nb_part2.py'; s=open(p).read()
v=open('/tmp/claude-1001/variant.py').read()
anchor='print("\\npaper: total 2365 (tolerance 236.5), V1 562 (56.2), LGN 140 (14), LP 90 (9)")\n'
assert anchor in s
# variant must come after build() is defined; place it right after the D/AR computation cell instead
anchor2='print("repeat pairs per unit at 1-back (static), median", np.median(SG["nb"]["rn"][:, 0].sum(1)),\n      "orthogonal", np.median(SG["nb"]["on"][:, 0].sum(1)))\n'
assert anchor2 in s
s=s.replace(anchor2, anchor2+v)
open(p,'w').write(s)
EOF
grep -n "tags=claim:units" nb_part2.py
```

```
13:# %% tags=claim:units-responsive-count
88:# %% tags=claim:units-responsive-count
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='/tmp/claude-1001/nb_part2.py'; s=open(p).read()
v=open('/tmp/claude-1001/variant.py').read()
s=s.replace(v,'',1)
a='# %% md\n# ## fig1d-v1-1back'
assert a in s
s=s.replace(a, v.lstrip('\n')+'\n'+a)
open(p,'w').write(s)
p='/tmp/claude-1001/build_full.py'; s=open(p).read()
s=s.replace("""out=[]
for i,c in enumerate(cells):
    out.append(c)
    tags=c.metadata.get('tags',[])
    nxt=cells[i+1].metadata.get('tags',[]) if i+1<len(cells) else []
    for t in tags:
        key='sanity' if t=='sanity' else t.split(':',1)[1] if t.startswith('claim:') else None
        if key and t not in nxt:""","""out=[]
last={}
for i,c in enumerate(cells):
    for t in c.metadata.get('tags',[]): last[t]=i
for i,c in enumerate(cells):
    out.append(c)
    tags=c.metadata.get('tags',[])
    for t in tags:
        key='sanity' if t=='sanity' else t.split(':',1)[1] if t.startswith('claim:') else None
        if key and last[t]==i:""")
open(p,'w').write(s)
EOF
source dev/bin/activate; python build_full.py ~/work/encore/encore/entries/fritsche-2022/reproduce_fritsche_2022.ipynb; ./dev.sh $TMPDIR/nb_part1.py $TMPDIR/nb_part2.py 2>&1 | tail -8
```

```
116 cells
V1 t test, pooled, remove, within: t = -18.00, p = 7.4e-58, n = 580
V1 t test, per_ori, remove, within: t = -9.05, p = 2.2e-18, n = 580
V1 t test, per_ori_geo, remove, within: t = -13.30, p = 2.1e-35, n = 580
V1 t test, pooled, remove, across: t = -17.95, p = 1.3e-57, n = 580
V1 t test, per_ori, remove, across: t = -8.94, p = 5.2e-18, n = 580
V1 t test, per_ori_geo, remove, across: t = -13.16, p = 8.4e-35, n = 580
by session: V1 ratio per mouse (units)
{0: '0.785 (22)', 1: '0.895 (21)', 2: '0.805 (21)', 3: '0.849 (9)', 4: '0.879 (19)', 5: '0.884 (13)', 6: '0.744 (14)', 7: '0.846 (19)', 8: '0.925 (5)', 9: '0.850 (11)', 10: '0.738 (18)', 11: '0.782 (22)', 12: '0.698 (2)', 13: '0.889 (34)', 14: '0.848 (22)', 15: '0.781 (20)', 16: '0.844 (14)', 17: '0.894 (26)', 18: '0.770 (12)', 19: '0.854 (13)', 20: '0.756 (18)', 21: '0.741 (26)', 22: '0.938 (13)', 23: '0.724 (13)', 24: '0.823 (16)', 25: '0.784 (32)', 26: '0.790 (22)', 27: '0.965 (7)', 28: '0.785 (29)', 29: '0.857 (23)', 30: '0.886 (23)', 31: '0.791 (21)'}
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -A8 "noise units kept:" run.py | head -3; source dev/bin/activate; cd ~/work/encore/encore/entries/fritsche-2022; PYTHONPATH=. python /tmp/claude-1001/run.py 2>&1 | grep "noise units kept"
```

```
print("drifting 1-back, noise units kept:", {a: round(A.region_value(arv[dgv["area"] == a, 0]), 3) for a in A.CORTEX + A.THALAMUS})
print("static 1-back, noise units kept:", {a: round(A.region_value(arsv[sgv["area"] == a, 0]), 3) for a in A.CORTEX + A.THALAMUS})
for region in ["V1", "LGN", "LP"]:
drifting 1-back, noise units kept: {'V1': 0.822, 'LM': 0.826, 'AL': 0.829, 'RL': 0.879, 'PM': 0.799, 'AM': 0.821, 'LGN': 0.93, 'LP': 0.837}
static 1-back, noise units kept: {'V1': 0.895, 'LM': 0.892, 'AL': 0.914, 'RL': 0.926, 'PM': 0.894, 'AM': 0.912, 'LGN': 0.956, 'LP': 0.893}
V1, noise units kept: 606 units; significant n [1, 2, 3, 4, 5, 6, 7, 8]; double fit a_fast 13.98%, tau_fast 0.838, a_slow 3.94%, tau_slow 6.93; single tau 1.511
LGN, noise units kept: 149 units; significant n [1, 7]; double fit a_fast 50.00%, tau_fast 0.777, a_slow -43.04%, tau_slow 0.88; single tau 0.000
LP, noise units kept: 101 units; significant n [1, 2]; double fit a_fast 17.09%, tau_fast 0.732, a_slow -0.62%, tau_slow 50.00; single tau 0.671
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='/tmp/claude-1001/results.py'; s=open(p).read()
a='no region and are not counted as regions."""'
s=s.replace(a,'''no region and are not counted as regions. With `noise` units kept, the 1-back ratios of the eight
regions move by at most 0.007 for either stimulus set and V1 stays significant to 8-back with a
tau_slow of 6.93, but LGN gains a significant 7-back and its single-exponential tau falls to
0.000; the claims on the thalamic decay rest on the filter."""''')
open(p,'w').write(s)
EOF
grep -c "0.000; the claims" results.py; date -u
```

```
1
Sat Nov 21 06:24:19 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd ~/work/encore/encore && python -c "
import json;d=json.load(open('schemas/attempt.schema.json'))
print(d['required']); p=d['properties']
print(list(p.keys()))
o=p['outcomes']['items']; print(o.get('required'), list(o['properties'].keys()))
f=p['findings']['items']; print(f.get('required'), list(f['properties'].keys()), f['properties'].get('kind'))
print(json.dumps(p['provenance'])[:1500])
print(json.dumps(p['datasets'])[:800])
"
```

```
['schema_version', 'id', 'datasets', 'paper', 'date', 'provenance', 'outcomes']
['schema_version', 'id', 'datasets', 'missing_datasets', 'paper', 'date', 'entry', 'deprecated', 'provenance', 'outcomes', 'verifications', 'findings', 'reconciliation', 'inputs', 'findings_review']
['claim', 'outcome'] ['claim', 'outcome', 'blocked_by', 'notes', 'notebook', 'output', 'measured', 'deviations', 'assumed', 'seed_sensitive', 'proposed']
['kind', 'statement'] ['kind', 'statement', 'found', 'about', 'severity', 'datasets'] {'enum': ['metadata_error', 'data_missing', 'identifier_missing', 'metadata_insufficient', 'selection_undocumented', 'methods_unavailable', 'format_error', 'code_mismatch', 'paper_inconsistency', 'other']}
{"type": "object", "additionalProperties": false, "required": ["kind", "accountable"], "properties": {"kind": {"enum": ["agent", "person"]}, "accountable": {"description": "The person or organisation responsible for this attempt.", "type": "object", "additionalProperties": false, "required": ["name"], "properties": {"name": {"type": "string"}, "orcid": {"type": "string", "pattern": "^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]$"}, "ror": {"type": "string"}}}, "agent": {"description": "Required when kind is agent.", "type": "object", "additionalProperties": false, "required": ["harness", "model", "protocol"], "properties": {"harness": {"type": "string"}, "model": {"type": "string"}, "protocol": {"description": "Version of the reproduction protocol the agent followed.", "type": "string"}}}, "runner": {"description": "Where the attempt was run: the platform, and the run that wrote this record. Its other runs (verification rounds, revisions) are linked from their transcripts.", "type": "object", "additionalProperties": false, "required": ["platform"], "properties": {"platform": {"description": "The platform that ran it, e.g. GitHub Actions, or local for a person's machine.", "type": "string", "minLength": 1}, "url": {"description": "The run that wrote the recor
[... 1 more lines not kept]
```

**Agent**

Now the attempt record.

**Agent calls Write**

```json
{
 "file_path": "attempts/fritsche-2022-01.yaml",
 "content": "schema_version: 3\nid: fritsche-2022-01\ndatasets:\n- archive: dandi\n  id: \"000021\"\n  version: 0.251116.2246\n  doi: 10.48324/dandi.000021/0.251116.2246\n  relation: reuses\npaper: doi:10.1523/jneurosci.1350-21.2021\ndate: 2026-11-21\nentry: fritsche-2022\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-18\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/44870457733\noutcomes:\n- claim: units-responsive-count\n  outcome: reproduced\n  notebook: reproduce_fritsche_2022.ipynb\n  output: claim:units-responsive-count\n  measured:\n  - 2422\n  - 580\n  - 142\n  - 91\n  notes: With `noise` units left out and reading O4 a, c, e (rate over the mean plus 1 SD of the\n    blank trials, preferred orientation pooled over directions and temporal frequencies), 2422\n    units are responsive in the eight regions, V1 580, LGN 142, LP 91, all within tolerance, and\n    all eight named regions have at least 50 units. Without the `noise` filter reading a, d, e also\n    matches (2298; V1 548, LGN 153, LP 92). The other O4 readings give 2214 to 7626 and fail. Units\n    on channels labelled `grey` (122) and `VIS` (71) also pass 50; these labels name no area.\n  deviations:\n  - Units the files label `noise` are left out, read as part of the \"default quality metrics of the\n    AllenSDK\" (Methods, Unit exclusion), whose units table omits them; the unit counts support this\n    reading. The variant without it is shown.\n  - Channels labelled `grey` or `VIS` are not counted as regions; the paper names only areas.\n  - The invalid intervals listed in 13 sessions are not applied; the paper does not mention them.\n- claim: fig1d-v1-1back\n  outcome: reproduced\n  notebook: reproduce_fritsche_2022.ipynb\n  output: claim:fig1d-v1-1back\n  measured: 0.821\n  notes: Main reading (O1a pooled per-unit ratio, O2a geometric region value, O3a blanks holding\n    positions, O3c pairs within blocks) gives 0.821 (t interval 0.804 to 0.839), 580 units, t =\n    -18.02, p = 6.0e-58 (paper 4e-57). The four readings with O1a and O2a lie in [0.821, 0.832];\n    the other 20 readings give 0.848 to 0.931. Per mouse the V1 ratio runs from 0.698 to 0.965.\n  deviations:\n  - The ratio is pooled over current orientations within each unit (O1a); the Methods' \"dividing the\n    firing rate of each neuron for repeat by that for orthogonal\" (Figure 1D legend) reads most\n    directly this way. All readings are shown.\n- claim: fig1d-extrastriate-1back\n  outcome: reproduced\n  notebook: reproduce_fritsche_2022.ipynb\n  output: claim:fig1d-extrastriate-1back\n  measured:\n  - 0.795\n  - 0.876\n  notes: LM 0.828, AL 0.828, RL 0.876, PM 0.795, AM 0.819, all inside [0.72, 0.968]; largest\n    corrected p 2.0e-24 (paper below 2e-21). Twenty of 24 readings keep all five inside.\n- claim: fig1d-thalamus-1back\n  outcome: reproduced\n  notebook: reproduce_fritsche_2022.ipynb\n  output: claim:fig1d-thalamus-1back\n  measured:\n  - 0.935\n  - 0.833\n  notes: LGN 0.935 (0.912 to 0.959), 142 units, p = 6.7e-07 (paper 8e-7); LP 0.833 (0.793 to\n    0.876), 91 units, p = 1.7e-10 (paper 3e-10). Twenty of 24 readings put both inside the paper's\n    intervals.\n- claim: fig1e-consistent-across-mice\n  outcome: partially_reproduced\n  notebook: reproduce_fritsche_2022.ipynb\n  output: claim:fig1e-consistent-across-mice\n  notes: Cortex, 32 of 32 mice have the orthogonal rate above the repeat rate (sign test p =\n    4.7e-10), reading (a). Thalamus, 21 of the 23 mice with thalamic units (p = 6.6e-05), so only\n    reading (b) holds there, which the criterion rates as partial.\n- claim: fig2-v1-tuning-main-effect\n  outcome: reproduced\n  notebook: reproduce_fritsche_2022.ipynb\n  output: claim:fig2-v1-tuning-main-effect\n  notes: Mixed ANOVA on log ratios with the 45 degree trials pooled, relative orientation F(2, 998) =\n    19.97, p = 3.1e-09 (paper 4e-11); the other three readings give p from 9.4e-14 to 2.6e-10. Ratios\n    0.799 at 0 degrees, 0.875 at 45, 0.927 at 90. 78 of 580 V1 units (96 with averaged 45) are left\n    out for a cell with a zero rate. Every other cortical area also has a significant main effect\n    (p from 5e-11 to 0.027).\n  deviations:\n  - Tertiles are formed on all responsive units of the region before units with a zero-rate cell\n    are left out, so the tertiles are not equal in the ANOVA (194, 192, 116 in V1); the paper does\n    not say how such units were handled.\n  - The mixed ANOVA is computed with the standard split-plot sums of squares and no sphericity\n    correction; the paper names no correction.\n- claim: fig2-v1-tuning-interaction\n  outcome: reproduced\n  notebook: reproduce_fritsche_2022.ipynb\n  output: claim:fig2-v1-tuning-interaction\n  notes: Interaction F = 3.28, p = 0.011 (log, pooled 45; paper 0.005); 6.3e-07 to 0.018 under the\n    other readings. The spread of ratios over relative orientation is 0.057 (low OSI), 0.125\n    (medium), 0.248 (high).\n- claim: fig2-v1-adaptation-at-all-orientations\n  outcome: reproduced\n  notebook: reproduce_fritsche_2022.ipynb\n  output: claim:fig2-v1-adaptation-at-all-orientations\n  notes: Pooled 45 degrees, Benjamini-Hochberg over the nine V1 cells, all eight other cells below\n    1 at corrected p < 0.05 (largest 0.012, medium OSI at 90); high OSI at 90 has ratio 0.993, p =\n    0.92 (paper 0.88). The same with the family of 72 cells. With Bonferroni 7 of 8 (V1 family) or\n    6 of 8 (all cells); with averaged 45, 7 of 8 under Benjamini-Hochberg.\n  deviations:\n  - The legend's \"corrected for multiple comparisons\" names no method; Benjamini-Hochberg, the\n    paper's stated method, is used (O6), and Bonferroni is shown.\n- claim: fig2-thalamus-no-tuning-dependence\n  outcome: reproduced\n  notebook: reproduce_fritsche_2022.ipynb\n  output: claim:fig2-thalamus-no-tuning-dependence\n  notes: Log ratios, pooled 45. LGN main effect F = 2.17, p = 0.12 (paper 0.28), interaction F =\n    1.37, p = 0.25 (0.24); LP F = 0.10, p = 0.91 (0.91), interaction F = 0.19, p = 0.95 (0.92). No\n    reading reaches 0.05; the smallest p is 0.073 (LGN main effect, averaged 45, log); on the ratio\n    scale LGN gives 0.28 and 0.30. Ratios per cell, LGN 0.879 to 0.991, LP 0.795 to 0.863.\n- claim: fig3a-v1-long-term\n  outcome: reproduced\n  notebook: reproduce_fritsche_2022.ipynb\n  output: claim:fig3a-v1-long-term\n  measured: 8\n  notes: Significant (FDR over n = 1 to 10) at every n from 1 to 8, not at 9 or 10; 8-back ratio\n    0.984. Eight of 12 readings of O1 and O3 give 8, the four per-orientation arithmetic readings\n    give 2, and one geometric reading 5. In 22 of 32 mice the mean V1 8-back log ratio is below\n    zero.\n- claim: fig3a-v1-double-exponential\n  outcome: reproduced\n  notebook: reproduce_fritsche_2022.ipynb\n  output: claim:fig3a-v1-double-exponential\n  measured:\n  - 14.21\n  - 0.816\n  - 3.755\n  - 6.714\n  notes: All four inside their Table 1 intervals under sign reading (a). Reading (b) fits the same\n    curve with a_slow = -3.76%, outside its interval as a signed value. Fits to the region's mean\n    log ratio (O5a) and to all unit values (O5b) give the same estimates, as every unit has a value\n    at every n. Eight of 12 readings of O1 and O3 put all four inside; the per-orientation\n    arithmetic readings put tau_slow on its bound of 50.\n  deviations:\n  - Fits start from four fixed starting points and keep the lowest residual; the paper does not\n    give its optimizer (a standard choice).\n- claim: fig3a-v1-half-life\n  outcome: reproduced\n  notebook: reproduce_fritsche_2022.ipynb\n  output: claim:fig3a-v1-half-life\n  measured: 13.96\n  notes: tau_slow 6.714 trials x 3 s x ln 2 = 13.96 s (13.97 s with the measured 3.003 s spacing).\n- claim: fig4-cumulative-adaptation\n  outcome: reproduced\n  notebook: reproduce_fritsche_2022.ipynb\n  output: claim:fig4-cumulative-adaptation\n  measured:\n  - 20.36\n  - 17.88\n  notes: Main reading 1-back 17.88% and cumulative 2- to 8-back 20.36%. The four pooled geometric\n    readings give 18.89 to 20.36% against 16.80 to 17.88%; the arithmetic and per-orientation\n    readings do not match.\n- claim: fig4b-linear-accumulation\n  outcome: reproduced\n  notebook: reproduce_fritsche_2022.ipynb\n  output: claim:fig4b-linear-accumulation\n  notes: With the both-orthogonal baseline (c) the predicted ratio is inside the bootstrapped 95%\n    interval of the observed one for all seven pairs (1-2 observed 0.765, 0.738 to 0.793, predicted\n    0.754), so pair readings (a) and (b) both hold, under all five seeds. With baseline (d) six of\n    seven pairs hold and pair 1-2 does not (0.788, 0.765 to 0.811), under all five seeds.\n- claim: fig3b-thalamus-short-term\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_fritsche_2022.ipynb\n  output: claim:fig3b-thalamus-short-term\n  notes: Counting significant adaptation (corrected p < 0.05 with the ratio below 1), the reading\n    O1a, O3a with pairs across blocks (O3d) meets the criterion, LGN only 1-back, LP to 2, cortex V1\n    8, LM 8, AL 7, RL 6, PM 7, AM 6. Under the main reading (pairs within blocks) RL stops at 5 and\n    the criterion fails, while LGN and LP still stop at 1 and 2. Counting significance in either\n    direction, LP is also significant at 3-back in the main reading (ratio 1.03) and LGN at 9-back\n    in the across-blocks reading, so only the partial rule would hold. With `noise` units kept LGN\n    also gains a significant 7-back. The question of what Figure 3B's borders mark is for the\n    paper's authors (finding).\n  deviations:\n  - Assumed that \"significant adaptation\" counts only ratios below 1; a two-tailed test also flags\n    ratios above 1, and the paper does not say whether Figure 3B's borders include those.\n  - Rests on the `noise` unit filter (see units-responsive-count).\n- claim: v1-vs-thalamus-welch\n  outcome: reproduced\n  notebook: reproduce_fritsche_2022.ipynb\n  output: claim:v1-vs-thalamus-welch\n  notes: Over n = 2 to 10 with Benjamini-Hochberg within each pair of regions, V1 is stronger than\n    LGN at exactly 2, 4 and 9 and than LP at 3, both unnormalized (LP also at 4) and normalized by\n    the region's mean 1-back log ratio (b); for reading (b), V1 against LP at 3-back t = 3.77,\n    corrected p = 0.002. Normalizing each unit by its own 1-back log ratio (a) finds none; 38 V1, 11\n    LGN and 8 LP units have a 1-back log ratio within 0.02 of zero. Over n = 2 to 50, 3 of the four\n    remain unnormalized and 1 under (b).\n- claim: fig3c-mice-long-term\n  outcome: reproduced\n  notebook: reproduce_fritsche_2022.ipynb\n  output: claim:fig3c-mice-long-term\n  notes: 4- to 8-back, cortex 31 of 32 mice (trials pooled; 30 with rates averaged) have orthogonal\n    above repeat, sign test p = 1.5e-08 (reading b); thalamus 14 of 23, p = 0.4, neither reading.\n- claim: decay-cortex-double-better\n  outcome: reproduced\n  notebook: reproduce_fritsche_2022.ipynb\n  output: claim:decay-cortex-double-better\n  notes: F tests on the region means, V1 p = 0.0015, LM 0.017, AL 8.0e-05, PM 0.0041, AM 0.011, RL\n    0.22 (paper RL 0.072); with all unit values, 4.2e-06 to 0.0021 and RL 0.12. Two of the five p\n    values (LM, AM) are above the paper's bound of 0.006.\n- claim: table1-extrastriate-tau-slow\n  outcome: reproduced\n  notebook: reproduce_fritsche_2022.ipynb\n  output: claim:table1-extrastriate-tau-slow\n  measured:\n  - 3.929\n  - 3.232\n  - 5.662\n  - 4.274\n  - 2.827\n  notes: AL, AM, LM, PM and RL tau_slow inside their Table 1 intervals; the six bootstrapped\n    intervals overlap under all five seeds (claim seed, V1 3.79 to 11.59, RL 1.97 to 35.11). V1's\n    tau_slow, 6.71, is the largest. All a_fast, tau_fast and a_slow are inside their intervals.\n    Bootstrap fits on a bound, dropped, 0 to 23 of 1000 per area (RL 23).\n- claim: decay-thalamus-single\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_fritsche_2022.ipynb\n  output: claim:decay-thalamus-single\n  measured:\n  - 0.031\n  - 0.712\n  - 6.48\n  - 16.85\n  notes: F tests not significant, LGN p = 0.81, LP 0.57 (unit values 0.62, 0.19); LGN tau 0.031 and\n    a 6.48%, LP tau 0.712 and a 16.85%, each inside its Table 1 interval. The double fits reach a\n    bound in both. With `noise` units kept the LGN tau falls to 0.000, outside its interval.\n  deviations:\n  - Rests on the `noise` unit filter (see units-responsive-count).\n- claim: fig5-repeat-suppression\n  outcome: partially_reproduced\n  notebook: reproduce_fritsche_2022.ipynb\n  output: claim:fig5-repeat-suppression\n  measured:\n  - 0.757\n  - 0.922\n  notes: 2189 cortical units. 1-back repeat over blank 0.757 and orthogonal over blank 0.922, both\n    below 1. Repeat suppression lasts longer, significant by t tests with FDR at 1 to 4 and 7, by the\n    bootstrap interval at 1 to 5, 7 and 9; orthogonal at 1 and 2 (and 4 by the interval). The\n    criterion fails on two parts, under the claim's seed and the four others; orthogonal is still\n    below 1 at 2-back (0.972), and repeat is not significant at 8-back (0.999). Averaged over 100\n    subsampling draws, repeat is significant to 8-back and orthogonal still at 2-back. 24 to 30\n    blank trials per session serve as the 1-back baseline.\n  deviations:\n  - Repeat and orthogonal trials are subsampled per session and per n to the number of n-back blank\n    trials (Methods); the paper does not say whether it drew per session or per n.\n- claim: fig6c-static-v1-1back\n  outcome: reproduced\n  notebook: reproduce_fritsche_2022.ipynb\n  output: claim:fig6c-static-v1-1back\n  measured:\n  - 0.897\n  - 545\n  notes: 0.897 (t interval 0.889 to 0.905), p = 4e-85 (paper 2e-81), 545 V1 units. Eight of 24\n    readings fall in [0.89, 0.91], all with the pooled ratio.\n- claim: fig6c-static-other-areas-1back\n  outcome: reproduced\n  notebook: reproduce_fritsche_2022.ipynb\n  output: claim:fig6c-static-other-areas-1back\n  measured:\n  - 0.891\n  - 0.930\n  - 0.957\n  - 0.900\n  - 61\n  - 17\n  notes: Extrastriate 0.891 to 0.930 (largest corrected p 1.7e-09); LGN 0.957, p = 0.0025; LP\n    0.900, p = 0.0045; counts 61 and 17.\n- claim: fig6d-static-consistent-across-mice\n  outcome: partially_reproduced\n  notebook: reproduce_fritsche_2022.ipynb\n  output: claim:fig6d-static-consistent-across-mice\n  notes: Cortex 32 of 32 mice (p = 4.7e-10); thalamus 15 of 17 mice with static-responsive thalamic\n    units (p = 0.0023), so only reading (b) holds there.\n- claim: fig7a-static-v1-long-term\n  outcome: reproduced\n  notebook: reproduce_fritsche_2022.ipynb\n  output: claim:fig7a-static-v1-long-term\n  measured:\n  - 20\n  - 8.255\n  - 0.533\n  - 2.065\n  - 9.47\n  notes: FDR family 1 to 20 (a), largest significant n 20 (20-back ratio 0.991, corrected p =\n    9.3e-05); family 1 to 50 (b) gives 49. Fit a_fast 8.26%, tau_fast 0.533, a_slow 2.07%, tau_slow\n    9.47, all inside Table 2.\n- claim: fig7b-static-cortex-decay\n  outcome: reproduced\n  notebook: reproduce_fritsche_2022.ipynb\n  output: claim:fig7b-static-cortex-decay\n  measured:\n  - 13.582\n  - 6.287\n  - 8.24\n  - 19.072\n  - 19.696\n  notes: F tests p from 9.5e-12 to 1.4e-05 over the six cortical areas (AM 1.4e-05 is above the\n    paper's bound of 1e-5); AL, AM, LM, PM, RL tau_slow inside Table 2; bootstrapped intervals\n    overlap under all five seeds.\n- claim: fig7-static-lgn-single\n  outcome: reproduced\n  notebook: reproduce_fritsche_2022.ipynb\n  output: claim:fig7-static-lgn-single\n  measured:\n  - 2.771\n  - 4.00\n  notes: F test p = 0.20 (paper 0.22; unit values 0.14); tau 2.77 trials and a 4.00%, inside Table\n    2. The LGN static tau is longer than the drifting one (0.031), reported only.\n- claim: fig7b-static-areas-long-term\n  outcome: reproduced\n  notebook: reproduce_fritsche_2022.ipynb\n  output: claim:fig7b-static-areas-long-term\n  measured: 20\n  notes: Family 1 to 20, largest significant n V1 20, LM 15, AL 20, RL 17, PM 20, AM 20, LGN 5, LP 9;\n    reading (c) holds (some area in 18 to 22), (d) does not (LM, RL), and both thalamic nuclei stay\n    below every cortical area. Family 1 to 50, five cortical areas reach 46 to 49, AM 22.\n- claim: fig7c-static-long-term-across-mice\n  outcome: partially_reproduced\n  notebook: reproduce_fritsche_2022.ipynb\n  output: claim:fig7c-static-long-term-across-mice\n  notes: 5- to 20-back, cortex 30 of 32 mice (p = 2.5e-07), V1 29 of 32 (p = 2.6e-06); reading (b)\n    holds and (a) does not. Thalamus 11 of 17 (p = 0.33), reported only.\n- claim: fig8-no-spurious-long-term\n  outcome: not_reproduced\n  seed_sensitive: true\n  notebook: reproduce_fritsche_2022.ipynb\n  output: claim:fig8-no-spurious-long-term\n  notes: The recovered 1-back ratio contains the ground truth in every run (drifting 0.821, static\n    0.897). Claim seed, Poisson noise at the V1 median rate (9.97 Hz drifting, 9.04 Hz static),\n    drifting has no n in 2 to 10 whose interval excludes 1, but static 5- and 6-back do (0.986,\n    0.987). No noise, static passes and drifting 2- and 6-back exclude 1 (0.996, 1.003). No reading\n    meets the criterion or its partial rule under the claim's seed. Of the four other seeds, one\n    (+1000) meets reading (a, c); the others fail. Without noise the spurious ratios stay within\n    0.0037 of 1 (drifting) and 0.0007 (static) over n = 2 to 10, against V1 drifting ratios of\n    0.918 to 0.984 at 2- to 8-back.\n  deviations:\n  - The paper does not give the simulated neuron's rate or noise; Poisson counts at the V1 median\n    orthogonal 1-back rate, and no noise, were run. A question for the authors (finding).\n- claim: robust-threshold-preferred-window\n  outcome: reproduced\n  notebook: reproduce_fritsche_2022.ipynb\n  output: claim:robust-threshold-preferred-window\n  notes: All seven variants meet the reading. Drifting 2.5 Hz (656 V1 units, significant to 7) and\n    10 Hz (430, to 8), preferred-orientation trials (to 8); static 2.5 Hz, 10 Hz and 0 to 100 ms all\n    reach 20 within the family 1 to 20. V1 F tests p <= 0.0105; LGN only at 1-back for drifting.\n  deviations:\n  - For the static 0 to 100 ms window, units are selected on 0 to 250 ms (545 V1) as the main\n    variant, and on 0 to 100 ms (97 V1) as a second; the Methods do not say which.\nfindings:\n- kind: metadata_insufficient\n  statement: The units table holds every sorted unit (74658), with a `quality` column marking 20182\n    as `noise` and the AllenSDK quality metric columns (isi_violations, amplitude_cutoff,\n    presence_ratio and others), none of which has a description in the files. The paper's unit\n    counts are matched when the `noise` units are left out, as the AllenSDK's units table does;\n    nothing in the files says that they should be, and keeping them changes the thalamic decay\n    results.\n  about: data\n  severity: minor\n- kind: other\n  about: data\n  statement: Three sessions (715093703, 719161530, 721123822) hold 598 drifting gratings in place\n    of the 600 the paper and the stimulus design give; one or two direction and frequency\n    conditions there have 14 presentations.\n  severity: minor\n- kind: other\n  about: data\n  statement: Thirteen sessions list invalid intervals tagged with a probe, totalling 12 to 2931 s,\n    and several overlap the drifting or static grating epochs. Their meaning is not described in\n    the files; the paper does not mention them, and they are not applied here.\n  severity: minor\n- kind: metadata_insufficient\n  about: data\n  statement: 3723 of the units that pass the quality metrics sit on channels whose area is `grey`\n    and 686 on `VIS`, labels that name no structure; they reach 50 responsive units, the paper's\n    rule for a region, and are left out here.\n  severity: minor\n- kind: other\n  about: data\n  statement: Checks that passed. 32 mice, one session each, with the genotypes the paper gives;\n    stimulus parameters, durations and spacing as the Methods describe; no recording or unit\n    deposited twice; the V1 orientation tuning is locked to the stimulus tables in every session\n    (true labels against labels shifted by whole presentations).\n  severity: none\n- kind: other\n  about: data\n  statement: Static blank sweeps number 189 to 197 of 6000 presentations per session, about one in\n    31, where the Methods say roughly one in 25.\n  severity: minor\n- kind: methods_unavailable\n  statement: For Figure 3B, do the borders marking significance (p < 0.05, FDR per area) include\n    n-back ratios significantly above 1? Here LP is significant at 3-back with a ratio of 1.03, and\n    the outcome of fig3b-thalamus-short-term depends on whether that counts; adaptation below 1 was\n    assumed.\n- kind: methods_unavailable\n  statement: For the simulated neuron of Figure 8, what rate and noise model were used, and was the\n    95% interval across the 32 sequences a t interval or a bootstrap? With Poisson noise at about 10\n    Hz single n-back intervals exclude 1 at chance-like rates, and the claim's outcome depends on\n    the seed.\n- kind: methods_unavailable\n  statement: Were units the Allen files label `noise` left out (the AllenSDK units table omits them)?\n    The paper's counts are matched with that filter, and the thalamic decay fits change without it.\n    The analysis code at doi:10.34973/kpt9-y956 is restricted and could not be read.\n"
}
```

```
File created successfully at: attempts/fritsche-2022-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='/tmp/claude-1001/summary.md'; s=open(p).read()
s=s.replace("# | decay-thalamus-single | reproduced |","# | decay-thalamus-single | reproduced (rests on an assumption) |")
s=s.replace("# unit counts single out, and it gives the paper's 1-back values to within 0.01. The invalid","# unit counts single out, and it gives the paper's 1-back values to within 0.01. Leaving out the\n# `noise` units is an assumption; with them kept the thalamic decay results change, so the two\n# thalamic claims marked above rest on it, as does the direction rule of fig3b. The invalid")
open(p,'w').write(s)
p='/tmp/claude-1001/results.py'; s=open(p).read()
s=s.replace('R["decay-thalamus-single"] = """**Result: reproduced.**','R["decay-thalamus-single"] = """**Result: reproduced, resting on an assumption.**')
s=s.replace('Table 1 interval. The double-exponential fits reach a bound in both."""','Table 1 interval. The double-exponential fits reach a bound in both. With `noise` units kept\n(variant above) the LGN tau falls to 0.000, so the outcome rests on that filter."""')
open(p,'w').write(s)
EOF
cat > ~/work/encore/encore/entries/fritsche-2022/README.md <<'EOF'
# Fritsche, Solomon & de Lange (2022) from dandiset 000021

Tests the findings of [Fritsche et al. (2022)](https://doi.org/10.1523/JNEUROSCI.1350-21.2021) on
[DANDI:000021](https://dandiarchive.org/dandiset/000021/0.251116.2246), the Allen Brain
Observatory Visual Coding Neuropixels sessions of the Brain Observatory 1.1 stimulus set (32
mice), which the paper reuses.

| Claims | Outcome |
|---|---|
| Unit counts, 1-back adaptation to drifting gratings in cortex and thalamus (4) | Reproduced |
| Dependence of 1-back adaptation on orientation preference (Figure 2, four claims) | Reproduced |
| Long-term adaptation in V1, its double-exponential decay, half-life, cumulative and linear accumulation (5) | Reproduced |
| Short-term adaptation in thalamus, V1 against thalamus, decay fits per area (5) | Reproduced (two rest on an assumption) |
| Consistency across mice of long-term drifting adaptation | Reproduced |
| Consistency across mice of 1-back adaptation (drifting and static) and of long-term static adaptation (3) | Partially reproduced |
| Repeat and orthogonal suppression against a blank baseline (Figure 5) | Partially reproduced |
| Static gratings, 1-back and long-term adaptation and decay fits (6) | Reproduced |
| Simulated neuron with only 1-back adaptation (Figure 8) | Not reproduced (depends on the seed) |
| Robustness to threshold, preferred-orientation trials and window | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/fritsche-2022-01.yaml`](../../attempts/fritsche-2022-01.yaml).

- `reproduce_fritsche_2022.ipynb`: the analysis. It takes about ten minutes; streaming the 32
  session files takes two to three of them.
- `adaptation.py`: streaming the files and reducing them to spike counts per unit and
  presentation, the responsiveness rule, the n-back adaptation ratios, the exponential decay fits
  and their bootstrap, and the mixed ANOVA. Other notebooks on this dandiset can import it.
EOF
source dev/bin/activate; python build_full.py ~/work/encore/encore/entries/fritsche-2022/reproduce_fritsche_2022.ipynb; cd ~/work/encore/encore; sed -i 's/runtime_minutes: 15/runtime_minutes: 10/' entries/fritsche-2022/entry.yaml; date -u; python tools/entry.py all entries/fritsche-2022 2>&1 | tail -15; date -u
```

```
116 cells
Sat Nov 21 06:25:59 UTC 2026
Installed kernelspec registry-fritsche-2022 in executed/fritsche-2022/.venv/share/jupyter/kernels/registry-fritsche-2022
0 error(s)
pass  reproduce_fritsche_2022.ipynb  (492 s)
Sat Nov 21 06:34:21 UTC 2026
```

**Agent calls Bash**

```bash
cd ~/work/encore/encore && source $TMPDIR/dev/bin/activate && python - <<'EOF' > $TMPDIR/exec_out2.txt
import nbformat
nb=nbformat.read('executed/fritsche-2022/reproduce_fritsche_2022.ipynb',4)
for c in nb.cells:
    if c.cell_type=='code':
        print('=== CELL', c.metadata.get('tags'))
        for o in c.outputs:
            if 'text' in o: print(o['text'])
            elif 'data' in o and 'text/plain' in o['data']: print(o['data']['text/plain'])
            elif o.get('output_type')=='error': print('ERROR', o['ename'])
EOF
grep -n "noise units kept\|ERROR\|Warning" $TMPDIR/exec_out2.txt | head; diff <(grep -v "loaded in\|bootstraps in\|built in" $TMPDIR/exec_out.txt | grep -v "^###") <(grep -v "loaded in\|bootstraps in\|built in" $TMPDIR/exec_out2.txt) | head -20; python tools/entry.py check entries/fritsche-2022; python tools/entry.py handover entries/fritsche-2022 2>&1 | tail -5
```

```
198:drifting 1-back, noise units kept: {'V1': 0.822, 'LM': 0.826, 'AL': 0.829, 'RL': 0.879, 'PM': 0.799, 'AM': 0.821, 'LGN': 0.93, 'LP': 0.837}
199:static 1-back, noise units kept: {'V1': 0.895, 'LM': 0.892, 'AL': 0.914, 'RL': 0.926, 'PM': 0.894, 'AM': 0.912, 'LGN': 0.956, 'LP': 0.893}
200:V1, noise units kept: 606 units; significant n [1, 2, 3, 4, 5, 6, 7, 8]; double fit a_fast 13.98%, tau_fast 0.838, a_slow 3.94%, tau_slow 6.93; single tau 1.511
201:LGN, noise units kept: 149 units; significant n [1, 7]; double fit a_fast 50.00%, tau_fast 0.777, a_slow -43.04%, tau_slow 0.88; single tau 0.000
202:LP, noise units kept: 101 units; significant n [1, 2]; double fit a_fast 17.09%, tau_fast 0.732, a_slow -0.62%, tau_slow 50.00; single tau 0.671
335:/tmp/claude-1001/ipykernel_47/1536358084.py:12: RuntimeWarning: divide by zero encountered in divide
337:/tmp/claude-1001/ipykernel_47/1536358084.py:12: RuntimeWarning: invalid value encountered in divide
339:/tmp/claude-1001/ipykernel_47/1536358084.py:13: RuntimeWarning: divide by zero encountered in divide
341:/tmp/claude-1001/ipykernel_47/1536358084.py:13: RuntimeWarning: invalid value encountered in divide
343:/tmp/claude-1001/ipykernel_47/1536358084.py:33: RuntimeWarning: divide by zero encountered in log
194a195,201
> === CELL ['claim:units-responsive-count']
> drifting 1-back, noise units kept: {'V1': 0.822, 'LM': 0.826, 'AL': 0.829, 'RL': 0.879, 'PM': 0.799, 'AM': 0.821, 'LGN': 0.93, 'LP': 0.837}
> static 1-back, noise units kept: {'V1': 0.895, 'LM': 0.892, 'AL': 0.914, 'RL': 0.926, 'PM': 0.894, 'AM': 0.912, 'LGN': 0.956, 'LP': 0.893}
> V1, noise units kept: 606 units; significant n [1, 2, 3, 4, 5, 6, 7, 8]; double fit a_fast 13.98%, tau_fast 0.838, a_slow 3.94%, tau_slow 6.93; single tau 1.511
> LGN, noise units kept: 149 units; significant n [1, 7]; double fit a_fast 50.00%, tau_fast 0.777, a_slow -43.04%, tau_slow 0.88; single tau 0.000
> LP, noise units kept: 101 units; significant n [1, 2]; double fit a_fast 17.0
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='/tmp/claude-1001/nb_part4.py'; s=open(p).read()
s=s.replace("ANOVA = {}\nCELLS = {}\nfor region in A.CORTEX + A.THALAMUS:\n    out, osi, tert = tuning_cells(DG, region)","ANOVA = {}\nCELLS = {}\nfor region in A.CORTEX + A.THALAMUS:\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        out, osi, tert = tuning_cells(DG, region)")
s=s.replace("        R = out[pool]\n        ok = np.all(np.isfinite(np.log(R)), 1)","        R = out[pool]\n        with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n            ok = np.all(np.isfinite(np.log(R)), 1)")
open(p,'w').write(s)
EOF
grep -n "errstate" nb_part4.py; ls ~/work/encore/encore/executed/fritsche-2022/handover
```

```
44:    with np.errstate(divide="ignore", invalid="ignore"):
48:        with np.errstate(divide="ignore", invalid="ignore"):
adaptation.py
fritsche-2022.yaml
reproduce_fritsche_2022.ipynb
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && python build_full.py ~/work/encore/encore/entries/fritsche-2022/reproduce_fritsche_2022.ipynb && cd ~/work/encore/encore && python tools/entry.py all entries/fritsche-2022 2>&1 | tail -3 && python - <<'EOF'
import nbformat
nb=nbformat.read('executed/fritsche-2022/reproduce_fritsche_2022.ipynb',4)
n=0
for c in nb.cells:
    if c.cell_type=='code':
        for o in c.outputs:
            if o.get('name')=='stderr' or o.get('output_type')=='error': n+=1; print(o.get('text','')[:300])
print('stderr/error outputs', n)
EOF
python tools/entry.py handover entries/fritsche-2022 | tail -2; date -u
```

```
116 cells
Installed kernelspec registry-fritsche-2022 in executed/fritsche-2022/.venv/share/jupyter/kernels/registry-fritsche-2022
0 error(s)
pass  reproduce_fritsche_2022.ipynb  (492 s)
/tmp/claude-1001/ipykernel_30/3240907760.py:25: RuntimeWarning: divide by zero encountered in divide
  per["c"].append(rep / cc[:, both_orth].mean(1))
/tmp/claude-1001/ipykernel_30/83981602.py:11: RuntimeWarning: divide by zero encountered in log
  lr = np.log(PR[base])
/tmp/claude-1001/ipykernel_30
/tmp/claude-1001/ipykernel_30/83981602.py:11: RuntimeWarning: divide by zero encountered in log
  lr = np.log(PR[base])
/tmp/claude-1001/ipykernel_30/83981602.py:11: RuntimeWarning: divide by zero encountered in log
  lr = np.log(PR[base])

/tmp/claude-1001/ipykernel_30/83981602.py:11: RuntimeWarning: divide by zero encountered in log
  lr = np.log(PR[base])

stderr/error outputs 3
wrote executed/fritsche-2022/handover
Sat Nov 21 06:43:39 UTC 2026
```

**Agent calls Bash**

```bash
cd ~/work/encore/encore && git status --short && grep -n -i "rather\|—" attempts/fritsche-2022-01.yaml entries/fritsche-2022/README.md entries/fritsche-2022/entry.yaml entries/fritsche-2022/adaptation.py $TMPDIR/results.py $TMPDIR/summary.md $TMPDIR/nb_part*.py; grep -c "\*\*" entries/fritsche-2022/reproduce_fritsche_2022.ipynb; python -c "
import yaml;d=yaml.safe_load(open('attempts/fritsche-2022-01.yaml'));print(len(d['outcomes']))
import collections;print(collections.Counter(o['outcome'] for o in d['outcomes']))"
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
?? attempts/fritsche-2022-01.yaml
?? entries/fritsche-2022/
?? scripts
40
31
Counter({'reproduced': 26, 'partially_reproduced': 4, 'not_reproduced': 1})
```

**Agent calls Bash**

```bash
cd ~/work/encore/encore && grep -n "\*\*" entries/fritsche-2022/reproduce_fritsche_2022.ipynb | grep -v '"\*\*Result' | cut -c1-200
```

```
368:    "def count_regions(stim, **kw):\n",
371:    "        r = select(s, stim, **kw)[0]\n",
455:    "        r, pref, by_ori, oris = select(s, stim, win=win, **sel_kw)\n",
1139:    "            rss_d = float(np.sum((lr - np.log(A.model_double(n, *d[0], sign=sign))) ** 2))\n",
1140:    "            rss_s = float(np.sum((lr - np.log(A.model_single(n, *s[0]))) ** 2))\n",
1313:    "        r = select(s, \"dg\", **MAIN)[0]\n",
1441:    "        rows.append(dict(O1=how, blanks=bl, blocks=bk, **{k: v for k, v in lg.items() if not k.endswith(\"_any\")},\n",
1749:    "        r = select(s, \"dg\", **MAIN)[0]\n",
1874:    "        rows.append(dict(good_only=good, gray=src, **{A.AREA_NAMES[k]: int(vc.get(k, 0)) for k in A.AREA_NAMES},\n",
```

**Agent**

I've finished steps 1 to 6 of the Author section. `tools/entry.py all` passes: the notebook runs in 492 s with 0 check errors. `handover` built `executed/fritsche-2022/handover/`. Nothing is committed.

## 1. Outcomes (31 claims, none blocked)

| Claim | Outcome |
|---|---|
| units-responsive-count | reproduced (2422 units; V1 580, LGN 142, LP 91) |
| fig1d-v1-1back | reproduced (0.821, p = 6e-58) |
| fig1d-extrastriate-1back | reproduced (0.795 to 0.876) |
| fig1d-thalamus-1back | reproduced (LGN 0.935, LP 0.833) |
| fig1e-consistent-across-mice | partially reproduced (thalamus 21 of 23 mice) |
| fig2-v1-tuning-main-effect | reproduced |
| fig2-v1-tuning-interaction | reproduced |
| fig2-v1-adaptation-at-all-orientations | reproduced |
| fig2-thalamus-no-tuning-dependence | reproduced |
| fig3a-v1-long-term | reproduced (significant up to 8-back) |
| fig3a-v1-double-exponential | reproduced (14.2%, 0.82, 3.8%, 6.71) |
| fig3a-v1-half-life | reproduced (13.96 s) |
| fig4-cumulative-adaptation | reproduced (20.4% against 17.9%) |
| fig4b-linear-accumulation | reproduced |
| fig3b-thalamus-short-term | reproduced, rests on an assumption |
| v1-vs-thalamus-welch | reproduced (exactly 2, 4, 9 against LGN and 3 against LP) |
| fig3c-mice-long-term | reproduced |
| decay-cortex-double-better | reproduced |
| table1-extrastriate-tau-slow | reproduced |
| decay-thalamus-single | reproduced, rests on an assumption |
| fig5-repeat-suppression | partially reproduced |
| fig6c-static-v1-1back | reproduced (0.897, 545 units) |
| fig6c-static-other-areas-1back | reproduced |
| fig6d-static-consistent-across-mice | partially reproduced |
| fig7a-static-v1-long-term | reproduced |
| fig7b-static-cortex-decay | reproduced |
| fig7-static-lgn-single | reproduced |
| fig7b-static-areas-long-term | reproduced |
| fig7c-static-long-term-across-mice | partially reproduced |
| fig8-no-spurious-long-term | not reproduced, seed sensitive |
| robust-threshold-preferred-window | reproduced |

Totals: 26 reproduced, 4 partially reproduced, 1 not reproduced.

## 2. Dataset, assumptions, questions

**Version.** I pinned 0.251116.2246. The paper cites no version, and this is the only published one. The notebook header says why.

**What the files hold.** All 32 mice are there, with the genotypes and stimuli the paper describes. Spike times share the clock of the stimulus tables in every session: orientation tuning measured with the true labels beats tuning with labels shifted by whole presentations. No recording or unit was deposited twice.

**Findings (all minor):**
- The units table holds every sorted unit and labels 20182 of 74658 `noise`. Neither that column nor the quality metric columns are described in the files.
- Three sessions have 598 drifting gratings, not 600.
- 13 sessions list invalid intervals tagged by probe, some inside the grating epochs. I did not apply them.
- Some units sit on channels labelled `grey` or `VIS`, which name no area.
- Static blank sweeps come about one in 31, where the Methods say about one in 25.

**Adopted reading.** Of all the readings the claims file lists, the unit counts point to one: leave out `noise` units, require a rate above the gray mean plus 1 SD from blank trials, and pool the preferred orientation over the other stimulus parameters. Under it the per-unit ratio pools over orientations, the region value is a geometric mean, and blanks hold their positions in the sequence. With this reading the 1-back values match the paper to within about 0.01.

**Assumptions:**
- **The `noise` filter.** It affects two claims. If the noise units are kept, LGN becomes significant at 7-back and its decay time constant (tau) drops to 0.000. So decay-thalamus-single and fig3b rest on the filter.
- **Significance means a ratio below 1 (fig3b).** A two-tailed test also flags LP at 3-back, where the ratio is 1.03, i.e. facilitation, not adaptation.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- Do the significance borders in Figure 3B include ratios above 1?
- What rate and noise model did the Figure 8 simulated neuron use?
- Were the `noise` units excluded?

**Questions to a reader:** none.

## 3. Where the protocol was unclear or missing something

1. **Any reading or all readings.** Author step 1.6 says the outcome is the one all readings give. The claims file's criteria say "reproduced under one reading". I followed the claims file.
2. **Direction of a two-tailed test.** Nothing covers whether "significant n-back" counts ratios above 1. I assumed adaptation only, and showed both.
3. **Filters outside the listed readings.** The `noise` label is not among the claims file's readings. I treated it as an assumption, and ran the key results without it as a variant, not every claim.
4. **Seeds for one bootstrap per region.** It is unclear whether each region's generator should take seed +1, +2 and so on. I gave every region the claim's seed (plus 1000·k for the four extra runs).
5. **Streaming URL.** `archives.md` doesn't say how to get the S3 URL. Following the download redirect returned 403, so I took the S3 address from the asset metadata's `contentUrl`.
6. **Missing partial rules.** The fig5 criterion has no partial rule, so I rated it partially reproduced from the protocol's general definition. The fig8 criterion is strict about confidence intervals at every n, so tiny, chance-level exclusions fail it.

## 4. Runtime and failures

- The notebook takes about 8 minutes (492 s); streaming the 32 files is 2 to 3 minutes of that. Peak memory is about 3.2 GB.
- The first full run failed because a cell boundary was missing, which left a function inside a markdown cell. I fixed it and the later runs passed.
- Some harmless RuntimeWarnings (division by zero) remain in the fig4b cells; the units they come from are reported as dropped.

## End of run

80 turns, 78 minutes, $7.81 at API prices, result: success.
