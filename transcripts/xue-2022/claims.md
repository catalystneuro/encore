# 000223 · claims · run 40008380067

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ claims/000223/ paper/;
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/^## Reader/,/^## Author/p' docs/protocol.md
```

```
## Reader

### 1. Get the paper

The workflow puts the paper's full text, and its PDF where there is one, under
`paper/`: the main text, the Methods, and the supplement. Read the text; open
the PDF only to read a figure or a table the text garbles. If the full text is
not there, or lacks the Methods or a supplement the results rest on, stop:
write no claims, and end with a report that names what is missing, so that it
can be supplied. Never write claims from the abstract. Do not copy figures.
Do not look at the dataset's data: its title and description on the archive
are enough to know which paper and which experiments it is meant to hold.

### 2. Read the paper's code

Read the code the paper links to before writing criteria. Say what it holds,
and record the repository and commit read. Where the Methods leave a choice
open and the code settles it, follow the code and say so. Where they disagree,
follow the Methods for the main result and name the code's choice as a
variant. When more sources disagree (the Methods, the analysis code, the
[... 116 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/001453/ claims/000223/ paper/; wc -c paper/*; head -30 paper/*.txt; cat claims/001453/*.yaml | head -200
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/001453/10.1016-j.cub.2025.04.027.yaml"
}
```

```
1	# Claims for Fouke, He, Loring & Naumann (2025) on dandiset 001453.
2	# Source: the accepted author manuscript in PubMed Central (PMC12218792), full text, read
3	# from its Results, figure legends and STAR Methods. The version of record is not open access.
4	#
5	# When these criteria were written, the author had seen the data check only: the file list,
6	# subject metadata, frame rates, units, trial structure and stimulus codes of every file, and
7	# the extent of positions. No claim's analysis had been run. The author had also read the
8	# outputs printed in the paper's own analysis notebook (Fig1-S1.ipynb, GitLab commit 33a5c29),
9	# which include per-stimulus median speeds and angular velocities and its statistics.
10	#
11	# The dandiset holds only the freely swimming tracking data of Figure 1 and Figure S1. Its
12	# stimulus codes 0 to 20 carry no names. The names come from the paper's code and from the
13	# stimulus software's protocol file (see stimulus-code-link), so the claims that need them
14	# use outside data and depend on that claim.
15	#
16	# Method choices fixed here, from the paper's Fig1-S1.ipynb where the Methods are silent: a
17	# trial is one stim_index; tracked frames only; positions smoothed with a Savitzky-Golay filter
18	# (21 frames, order 2); trials rejected when the absolute cumulative heading change exceeds
19	# 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or the mean speed exceeds
20	# 100 mm/s; measures taken from 3 s to 35 s after the first frame (the 3 s stationary phase is
[... 302 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1088-1741-2552-ac8765.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1088-1741-2552-ac8765.txt",
 "offset": 98
}
```

Result: not kept, because it reads the paper's text.

**Agent**

I've read the paper: full text, Methods, Table 1 and the three-figure supplement are all there. Next I'll read the linked code repository.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/starquakes/mea_spineca_mapping && cd mea_spineca_mapping && git log -1 --format='%H %cd' && find . -type f -not -path './.git/*' | head -100
```

```
99c2a478393341a24c58d6ef6ab5db5b0b528d03 Tue Sep 27 17:45:30 2022 +0200
./notebooks/log_release_Pr.npy
./notebooks/README.md
./notebooks/3_method_validation_and_explore_optimal_thresholds.ipynb
./notebooks/2_simulate_surrogate_data_for_validation.ipynb
./notebooks/1_match-spine-trace-with-spike-trains.ipynb
./notebooks/0_export-to-nwb.ipynb
./imaging_tools.py
./environment.yml
./README.md
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/mea_spineca_mapping && cat README.md notebooks/README.md && wc -l imaging_tools.py && cat imaging_tools.py
```

````
<persisted-output>
Output too large (29.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/33486a47-fcd7-480f-98fb-a6d1f22dc183/tool-results/b51jkvui7.txt

Preview (first 2KB):
# mea_spineca_mapping
The mea-spineca-mapping is an easily adoptable analysis pipeline for paired dendritic spine calcium imaging with large-scale extracellular recording. 

Users can:
1. Reproduce the figures and results in "Inferring monosynaptic connections from paired dendritic spine Ca2+ imaging and large-scale recording of extracellular spiking". Data sets can be downloaded from https://gui.dandiarchive.org/#/dandiset/000223.
2. Adapt and implement the pipeline for their own data sets.

## Citation
```
@article{xue2022measpinecamapping,
  title={Inferring monosynaptic connections from paired dendritic spine Ca$^{2+}$ imaging and large-scale recording of extracellular spiking},
  author={Xue, Xiaohan and Buccino, Alessio Paolo and Saseendran Kumar, Sreedhar and Hierlemann,  Andreas and Bartram, Julian},
  journal={Journal of neural engineering},
  year={2022},
  publisher={IOP Publishing}
}
[... 15 more lines not kept]
````

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/33486a47-fcd7-480f-98fb-a6d1f22dc183/tool-results/b51jkvui7.txt"
}
```

````
1	# mea_spineca_mapping
2	The mea-spineca-mapping is an easily adoptable analysis pipeline for paired dendritic spine calcium imaging with large-scale extracellular recording. 
3	
4	Users can:
5	1. Reproduce the figures and results in "Inferring monosynaptic connections from paired dendritic spine Ca2+ imaging and large-scale recording of extracellular spiking". Data sets can be downloaded from https://gui.dandiarchive.org/#/dandiset/000223.
6	2. Adapt and implement the pipeline for their own data sets.
7	
8	## Citation
9	```
10	@article{xue2022measpinecamapping,
11	  title={Inferring monosynaptic connections from paired dendritic spine Ca$^{2+}$ imaging and large-scale recording of extracellular spiking},
12	  author={Xue, Xiaohan and Buccino, Alessio Paolo and Saseendran Kumar, Sreedhar and Hierlemann,  Andreas and Bartram, Julian},
13	  journal={Journal of neural engineering},
14	  year={2022},
15	  publisher={IOP Publishing}
16	}
17	```
18	
19	## 0_export-to-nwb
20	This notebook is used to convert our data sets into NWB files. Each converted NWB file contains: raw extracellular recordings - spike-sorted units - imaging series - segmentation ROIs (of the target spines and adjacent dendritic shaft). You can download from Dandi Archive (https://gui.dandiarchive.org/#/dandiset/000223). 
[... 787 more lines not kept]
````

**Agent**

Now the notebooks' code cells.

**Agent calls Bash**

```bash
cd $TMPDIR/mea_spineca_mapping/notebooks && for f in 1_*.ipynb 2_*.ipynb 3_*.ipynb; do echo "=========== $f"; python3 -c "
import json,sys
nb=json.load(open('$f'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(f'--- [{i}] {c[\"cell_type\"]}')
    print(src)
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            t=o.get('text') or o.get('data',{}).get('text/plain')
            if t:
                t=''.join(t)
                print('>>OUT:', t[:600])
"; done
```

```
<persisted-output>
Output too large (37.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/33486a47-fcd7-480f-98fb-a6d1f22dc183/tool-results/bfqj3ra6g.txt

Preview (first 2KB):
=========== 1_match-spine-trace-with-spike-trains.ipynb
--- [0] markdown
# Part 1) Match spine trace with extracellular spike trains

In this notebook, we show how to match the corresponding presynaptic cell for a given dendritic spine. More detailed explanation can be found in "Inferring monosynaptic connections from paired dendritic spine Ca2+ imaging and large-scale recording of extracellular spiking" (https://doi.org/10.1101/2022.02.16.480643).

First, the spike trains of all recorded units are convolved with an expotential kernel. This expotnetial kernel is constructed with parameters that fit the calcium indicator's dynamics. We then downsample the convolved spike trains in order to match the sampling rate of calcium imaging for postsynaptic cells.

Second, we extract the spine calcium trace from the imaging. We use robust regression to remove the contribution of dendritic activities from the spine calcium trace in order to obtain the synaptic responses.

Network synchrony (bursts) is detected and excluded for the following correlation analysis. We apply Pearson correlation to the spine calcium trace with convolved spike trains from all recorded units, and rank the correlation R values. In next notebook, we would show whether the unit with the highest R value should be accepted as the corresponding presynaptic cell for the given spine.
--- [1] code
%load_ext autoreload
%autoreload 2
--- [2] code
import numpy as np
[... 28 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/33486a47-fcd7-480f-98fb-a6d1f22dc183/tool-results/bfqj3ra6g.txt"
}
```

```
1	=========== 1_match-spine-trace-with-spike-trains.ipynb
2	--- [0] markdown
3	# Part 1) Match spine trace with extracellular spike trains
4	
5	In this notebook, we show how to match the corresponding presynaptic cell for a given dendritic spine. More detailed explanation can be found in "Inferring monosynaptic connections from paired dendritic spine Ca2+ imaging and large-scale recording of extracellular spiking" (https://doi.org/10.1101/2022.02.16.480643).
6	
7	First, the spike trains of all recorded units are convolved with an expotential kernel. This expotnetial kernel is constructed with parameters that fit the calcium indicator's dynamics. We then downsample the convolved spike trains in order to match the sampling rate of calcium imaging for postsynaptic cells.
8	
9	Second, we extract the spine calcium trace from the imaging. We use robust regression to remove the contribution of dendritic activities from the spine calcium trace in order to obtain the synaptic responses.
10	
11	Network synchrony (bursts) is detected and excluded for the following correlation analysis. We apply Pearson correlation to the spine calcium trace with convolved spike trains from all recorded units, and rank the correlation R values. In next notebook, we would show whether the unit with the highest R value should be accepted as the corresponding presynaptic cell for the given spine.
12	--- [1] code
13	%load_ext autoreload
14	%autoreload 2
15	--- [2] code
16	import numpy as np
17	import roiextractors as re
18	import matplotlib.pyplot as plt
19	import spikeextractors as se
20	import belextractors as be
[... 819 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/t.py <<'EOF'
import numpy as np, scipy.stats as st
rows="""1 0.523 0.091 0.214 0.960 0.296 0.787 yes 78 0.733 0.38
2 0.516 0.162 0.291 0.960 0.271 0.854 yes 132 2.003 0.17
3 0.217 0.172 0.112 0.960 0.190 0.835 yes 66 1.717 0.17
4 0.644 0.162 0.311 0.949 0.489 0.850 yes 185 0.588 0.23
5 0.429 0.162 0.358 0.929 0.520 0.797 no 159 0.318 0.26
6 0.647 0.192 0.448 0.929 0.619 0.599 yes 50 0.189 0.41
7 0.346 0.152 0.503 0.929 0.585 0.604 no 55 0.269 0.48
8 0.340 0.030 0.227 0.929 0.475 0.544 no 66 0.060 0.62
9 0.671 0.222 0.507 0.949 0.639 0.795 yes 179 0.425 0.28
10 0.765 0.222 0.507 0.949 0.639 0.795 yes 179 0.425 0.28
11 0.148 0.232 0.354 0.939 0.351 0.775 no 99 0.783 0.20
12 0.597 0.152 0.353 0.960 0.544 0.870 yes 114 0.719 0.29
13 0.160 0.172 0.267 0.960 0.068 0.860 no 128 0.425 0.36
14 0.394 0.111 0.456 0.869 0.435 0.485 no 133 0.289 0.64
15 0.400 0.091 0.436 0.879 0.604 0.520 no 133 0.222 0.69
16 0.676 0.424 0.383 0.545 0.666 0.525 yes 58 0.171 0.43
17 0.602 0.232 0.500 0.889 0.707 0.537 no 50 0.534 0.31
18 0.311 0.182 0.214 0.949 0.324 0.723 no 100 0.464 0.25
19 0.219 0.182 0.233 0.909 0.298 0.610 no 87 0.272 0.50
20 0.294 0.121 0.414 0.879 0.364 0.577 no 59 0.112 0.53"""
L=[r.split() for r in rows.splitlines()]
bR=np.array([float(r[1]) for r in L]); F=np.array([float(r[6]) for r in L]); acc=np.array([r[7]=='yes' for r in L])
U=np.array([int(r[8]) for r in L]); oi=np.array([float(r[9]) for r in L]); sc=np.array([float(r[10]) for r in L])
gt=np.array([float(r[3]) for r in L]); te=np.array([float(r[5]) for r in L])
print('accept by table rule', (bR>np.maximum(gt,te)) == acc)
m=np.ones(20,bool); m[9]=False
for name,mask in [('20',np.ones(20,bool)),('19',m)]:
    print(name,'F',F[mask].mean(),F[mask].std(),F[mask].std(ddof=1),'units',U[mask].mean(),U[mask].std(),U[mask].std(ddof=1))
    print(' spearman sc',st.spearmanr(sc[mask],F[mask]),' oi',st.spearmanr(oi[mask],F[mask]))
print('acc',acc.sum(),bR[acc].mean(),bR[acc].std(),bR[acc].std(ddof=1),'rej',bR[~acc].mean(),bR[~acc].std(),bR[~acc].std(ddof=1))
r=st.mannwhitneyu(bR[acc],bR[~acc],alternative='two-sided'); print(r)
print(st.mannwhitneyu(bR[~acc],bR[acc],alternative='two-sided'))
# rejection scenarios
rej=~acc
print('below test only',np.sum(rej&(bR<te)&(bR>=gt)),'below gt only',np.sum(rej&(bR<gt)&(bR>=te)),'both',np.sum(rej&(bR<gt)&(bR<te)))
print('test>gt count', np.sum(te>gt), 'gt>test', np.sum(gt>te))
EOF
python3 $TMPDIR/t.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/t.py", line 1, in <module>
    import numpy as np, scipy.stats as st
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
ls; which python python3; python -c "import numpy, scipy; print('ok')"; ls .venv 2>/dev/null | head
```

```
LICENSE
README.md
attempts
bunfig.toml
claims
docs
encore_science
entries
node_modules
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
pyproject.toml
questions
queue
schemas
scripts
targets
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 -m venv v && v/bin/pip -q install numpy scipy 2>&1 | tail -2 && v/bin/python t.py
```

```
[notice] A new release of pip is available: 26.2.1 -> 26.2.2
[notice] To update, run: /tmp/claude-1001/v/bin/python3 -m pip install --upgrade pip
accept by table rule [ True  True  True  True  True  True  True  True  True  True  True  True
  True  True  True  True  True  True  True  True]
20 F 0.6971 0.1346766126690154 0.138175289130567 units 105.5 44.83358116412295 45.99828372084287
 spearman sc SignificanceResult(statistic=np.float64(-0.7369213920494784), pvalue=np.float64(0.00021030411567580837))  oi SignificanceResult(statistic=np.float64(0.6719401653039546), pvalue=np.float64(0.0011749863573595747))
19 F 0.6919473684210526 0.13624029610415736 0.13997359817885122 units 101.63157894736842 42.620986338355586 43.78890083408477
 spearman sc SignificanceResult(statistic=np.float64(-0.7424309622138028), pvalue=np.float64(0.00027227190711814995))  oi SignificanceResult(statistic=np.float64(0.6801229263778924), pvalue=np.float64(0.0013547858381551742))
acc 9 0.5840000000000001 0.14890936840910987 0.15794223627643117 rej 0.3311818181818182 0.12399546779240703 0.13004754375367356
MannwhitneyuResult(statistic=np.float64(87.0), pvalue=np.float64(0.004938355678644229))
MannwhitneyuResult(statistic=np.float64(12.0), pvalue=np.float64(0.004938355678644229))
below test only 4 below gt only 1 both 6
test>gt count 15 gt>test 5
Shell cwd was reset to
```

**Agent calls Bash**

```bash
grep -rl "000223" --include=* targets entries queue papers questions 2>/dev/null | head; ls tools
```

```
targets/dandisets.json
papers/manifest.yaml
__pycache__
agent_run.py
archive_transcripts.sh
build_site.py
build_targets.py
claims_check.py
conversion_issue.py
datasets.py
entry.py
flagged.py
get_papers.sh
notify.py
papers_manifest.py
progress.py
readme_row.py
runner
site_assets
social_card.html
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;d=json.load(open('targets/dandisets.json'))
items=d if isinstance(d,list) else d.get('dandisets',d)
for x in (items if isinstance(items,list) else items.values()):
    if '000223' in json.dumps(x): print(json.dumps(x,indent=1)[:3000])
"; grep -n -B2 -A10 "000223" papers/manifest.yaml; sed -n 1,80p tools/claims_check.py
```

```
[
 {
  "dandiset": "000003",
  "name": "Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells",
  "published_version": "0.260218.2052",
  "asset_count": 101,
  "size_gb": 2559.25,
  "data_standards": [
   "Neurodata Without Borders (NWB)"
  ],
  "species": [
   "House mouse"
  ],
  "approaches": [
   "electrophysiological approach",
   "behavioral approach"
  ],
  "papers": [
   {
    "doi": "10.1016/j.neuron.2016.12.011",
[... 192 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;d=json.load(open('targets/dandisets.json'))
for x in d:
    if x['dandiset']=='000223': print(json.dumps(x,indent=1))
"; python3 -c "import json;print(json.dumps(json.load(open('schemas/claims.schema.json')),indent=1))" | head -250
```

```
Traceback (most recent call last):
  File "<string>", line 4, in <module>
    if x['dandiset']=='000223': print(json.dumps(x,indent=1))
       ~^^^^^^^^^^^^
TypeError: string indices must be integers, not 'str'
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
[... 235 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1))"; python3 -c "
import json;d=json.load(open('targets/dandisets.json'))
print(type(d), list(d)[:5] if isinstance(d,dict) else '')
items=d.get('targets') or d.get('dandisets') or []
for x in items:
    if x.get('dandiset')=='000223': print(json.dumps(x,indent=1))
"
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
[... 110 more lines not kept]
```

**Agent**

I have what I need: the paper, the supplement and the code at commit 99c2a47. I'll write the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/000223/10.1088-1741-2552-ac8765.yaml",
 "content": "# Claims for Xue, Buccino, Saseendran Kumar, Hierlemann & Bartram (2022) on dandiset 000223.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-23,\n# protocol pilot-10 as stated in docs/protocol.md (Reader).\n#\n# Text read: the accepted author manuscript in PubMed Central (PMC7613561, UKPMC funders author\n# manuscript), as served by ncbi_pmc, full text with Methods, figure legends and Table 1, and its\n# one supplement (EMS152915-supplement, three figure supplements of Figure 1: indicator expression,\n# demixing example, burst detection example). The version of record was not read. No PDF of the\n# main text was available; none was needed, as Table 1 is legible in the text.\n#\n# Code read: https://github.com/starquakes/mea_spineca_mapping at commit\n# 99c2a478393341a24c58d6ef6ab5db5b0b528d03 (2022-09-27). It holds imaging_tools.py (dF/F, demixing,\n# NWB loading, peak detection, surrogate generation, R distributions) and four notebooks:\n# 0_export-to-nwb, 1_match-spine-trace-with-spike-trains (convolution, dF/F, burst detection and\n# exclusion, demixing, Pearson R ranking), 2_simulate_surrogate_data_for_validation (noise and signal\n# estimate, GT-R and test-R distributions, acceptance test), 3_method_validation_and_explore_optimal\n# _thresholds (surrogates for all units, TP/FN/TN/FP, F-score grid), and log_release_Pr.npy (one draw\n# of the release probabilities). The notebooks carry no saved numeric outputs for any recording.\n#\n# Data the paper used: primary cortical neurons of E18 Wistar rat embryos cultured on a CMOS\n# HD-MEA (26'400 electrodes at 17.5 um pitch, 1'024 channels recorded at 20 kHz), sparse\n# jGCaMP7b expression, recorded at DIV 18 to 21. 19 paired recordings from 10 cultures, each a\n# confocal time series of a target postsynaptic cell (7 to 15 Hz, typically 2 to 3 min) with a\n# simultaneous HD-MEA recording, aligned by camera TTL pulses. One target spine per recording, two\n# in one recording (20 spines in all; Table 1 rows 9 and 10, culture 3). Per recording the paper\n# uses the curated SpyKING Circus 0.8.4 units (Table 1 \"total #units\", 50 to 185), and per spine the\n# fluorescence trace of a spine ROI and of its adjacent dendritic shaft ROI. Per the Data\n# availability section and the code's README, each NWB file holds the raw extracellular recording,\n# the curated sorted units, the imaging series, and the spine and shaft ROIs with their traces.\n# The paper gives no map from Table 1 rows to files; culture ID and unit count per row (Table 1)\n# are the only keys it offers.\n#\n# Pipeline as the claims use it (Methods 2.4 to 2.8, Results 3.1 to 3.3, and the code, cited in\n# each criterion). Spine and shaft traces are taken from the file's ROI traces (notebook 1, LOAD_DATA)\n# and turned into dF/F with a moving 25th percentile baseline over 100 frames\n# (scipy.ndimage.percentile_filter, imaging_tools.dff method winperc2). Demixing subtracts the\n# shaft trace fitted to the spine trace by robust linear regression (Methods 2.4; the code uses\n# sklearn HuberRegressor with defaults, slope and intercept). Each unit's spike train is convolved\n# with an exponential kernel of decay 0.5 s (elephant ExponentialKernel sigma 0.5 s,\n# instantaneous_rate at the 20 kHz sampling period, center_kernel False), sampled at the imaging\n# frame times (searchsorted of frame times into MEA sample times), 1 is added and the same dF/F is\n# applied, NaN and inf set to 0 (code only). Network bursts are found as in Methods 2.6 and\n# extended by 0.1 s before and 0.5 s after; imaging frames inside the extended bursts are dropped\n# (notebook 1 uses frame times np.linspace(0, MEA duration, number of frames) for this). Pearson R\n# of the demixed spine trace with every convolved trace over the kept frames; the unit with the\n# largest R is the best-matching unit and its R the best-R.\n#\n# Burst detection details (Methods 2.6, notebook 1). Hyperactive units are left out first, by\n# one of the two strategies the Methods give, (i) rate above the 99.75th percentile of unit rates\n# (the code's default, PC = True) or (ii) rate above 15 Hz. Population spike count of the other\n# units in 10 ms bins; f_baseline is the 85th percentile and f_thresh the p_thresh percentile of\n# the bin counts; peaks of height at least f_thresh, prominence at least f_thresh\n# (scipy.signal.peak_prominences), at least 50 ms apart; burst edges where a smoothed trace first\n# falls to f_baseline on each side of the peak, smoothing by locally weighted linear regression\n# over 5 data points (Methods; the code uses statsmodels lowess with frac 0.0002 of the bins, shown\n# as a variant); bursts touching the start or end and bursts with no spikes dropped; bursts closer\n# than 75 ms merged. p_thresh \"was visually chosen for each data set\" and is not reported per\n# recording; the Methods give it as typically between the 96th and 99th percentile, and the code's\n# default is 97.\n#\n# Surrogates (Methods 2.7, Results 3.2, notebook 2, imaging_tools.generate_surrogates). Release\n# probabilities are numpy.random.lognormal(2.5, 0.6) scaled by 0.01, values above 1 replaced by\n# uniform values in 0 to 1, 1'000 of them (the code loads the stored draw log_release_Pr.npy; a\n# fresh draw is the Methods' reading, the stored one a variant). For each surrogate, ceil(Pr N) of\n# the unit's N spikes are kept at random (code; a Bernoulli draw per spike with probability Pr is\n# the other reading of the Methods' wording, shown as a variant), convolved and sampled as above,\n# divided by its standard deviation, scaled by the median over pixels of (signal pixel SD minus\n# noise pixel SD), the median of the spine pixels' medians added as baseline, white noise of SD the\n# median noise pixel SD added, and the 25th percentile, 100 frame dF/F applied. The signal region\n# is the spine ROI; the noise region is \"a background ROI close to the spine\", subsampled at random\n# to the signal region's pixel count. GT-Rs are the R of 1'000 surrogates of the best-matching unit\n# with that unit's convolved trace; test-Rs the R of 1'000 surrogates of the second-best unit with\n# the best unit's convolved trace; all R over the frames outside extended bursts. A connection is\n# accepted when best-R exceeds both the Q_test quantile of the test-Rs and the Q_GT quantile of the\n# GT-Rs (numpy nanquantile).\n#\n# Open details that recur. (1) p_thresh per recording, readings the integer percentiles 96, 97, 98\n# and 99. (2) The hyperactive-unit strategy, readings (i) and (ii) above. (3) The background ROI\n# for the noise estimate, unless the dataset holds it. (4) Random draws (release probabilities,\n# spike retention, noise, pixel subsampling), a standard choice of seed; their effect is shown\n# where a claim names it. Within a recording, the same p_thresh and strategy are used for every\n# claim, and the one carried forward is the pair whose best-R is nearest to Table 1 (the paper\n# fixed one value per data set and reports only its outcome); results at p_thresh 97 with strategy\n# (i), the code's defaults, are shown for every recording as well.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000223\"\npaper: doi:10.1088/1741-2552/ac8765\nclaims:\n- id: data-scale\n  statement: The paper made 19 paired spine Ca2+ imaging and HD-MEA recordings in 10 cultures,\n    tested 20 spines (one per recording, two in one recording), and the recordings have a mean of\n    102 ± 43 sorted units each.\n  source: Results, 3.4 Performance evaluation on experimental data, paragraphs 1 and 2; Table 1\n  quote: we conducted 19 paired spine Ca 2+ imaging and HD-MEA recording experiments in 10 different\n    cell cultures ... based on 19 recordings with a mean of 102 ± 43 units per recording ... (in one\n    of recordings two spines were chosen)\n  expected:\n  - quantity: paired recordings\n    value: 19\n    tolerance: 0\n  - quantity: cultures\n    value: 10\n    tolerance: 0\n  - quantity: tested spines\n    value: 20\n    tolerance: 0\n  - quantity: mean sorted units per recording\n    value: 102\n    tolerance: 10.2\n  - quantity: SD of sorted units per recording\n    value: 43\n    tolerance: 4.3\n  criterion: Counts of recordings, cultures and spines are exact, as they describe the data\n    collected. Units are the curated sorted units of each recording. The paper does not say over\n    which set the mean and spread are taken or which SD is meant; Table 1 settles it, as 19\n    recordings (rows 9 and 10 counted once) with the population SD (ddof 0) give 101.6 ± 42.6,\n    while 20 rows give 105.5 ± 44.8 and the sample SD gives 43.8. That reading is used, and the\n    other is shown. The per-row unit counts of Table 1 are compared with the files as well, each\n    within 10%.\n- id: table1-best-r\n  statement: For each of the 20 tested spines, the best-R (the Pearson R of the demixed spine\n    trace with the convolved trace of its best-matching unit, outside network bursts) has the\n    value given in Table 1, from 0.148 to 0.765.\n  source: Table 1, column best_R; Figure 5(a)\n  inferred: The per-spine values are given only in Table 1 (column best_R); Figure 5(a) plots them.\n    No sentence of the text states them.\n  criterion: The pipeline of the opening comment, from the Methods 2.4 to 2.6 and notebook 1 of the\n    code, with each detail cited there. Each spine is matched to its Table 1 row by culture and unit\n    count; a spine's best-R matches when it is within 10% of the Table 1 value under at least one of\n    the readings of the open details (p_thresh 96 to 99, hyperactive strategy (i) or (ii)), as the\n    paper chose p_thresh per data set without reporting it. Every reading's value is shown.\n    Reproduced when all 20 spines match; partially reproduced when 15 to 19 match; not reproduced\n    otherwise. The lowess variant (frac 0.0002) and the code's default pair (97, (i)) are shown.\n- id: fig1e-best-r-gap\n  statement: In the example recording of Figure 1(e), the best-R shows the largest increase over\n    the next ordered R value among all units.\n  source: Results, 3.1 Identifying the presynaptic unit of a dendritic target spine, last paragraph;\n    Figure 1(e)\n  quote: Moreover, the R value for the best-matching unit ( best-R ) shows the largest increase with\n    respect to the next (ordered) R value among all units\n  depends_on:\n  - table1-best-r\n  criterion: The paper does not say which recording is the example. For each spine, the R values\n    of all units are sorted and the gap between best-R and the second R is compared with every\n    other gap between consecutive sorted values. Reproduced when the first gap is the largest for at\n    least one spine (the example is one of them); the number of spines for which it holds is\n    reported. A claim about one unnamed example, so a weak test.\n- id: table1-optimal-thresholds\n  statement: For each recording, simulated ground-truth connections of every unit give an F-score\n    surface over the quantile pair (Q_test, Q_GT), whose maximum and optimal quantiles are those of\n    Table 1 (max_F 0.485 to 0.870).\n  source: Table 1, columns GT_Q, test_Q and max_F; Figure 4; Results, 3.3 Method validation and\n    threshold optimization\n  inferred: The per-recording values are given only in Table 1; the procedure is in Results 3.3,\n    Methods 2.8 and Figure 4.\n  depends_on:\n  - table1-best-r\n  criterion: As in Results 3.3, Methods 2.8 and notebook 3 of the code. For every unit, 1'000\n    surrogates with the recording's noise and signal estimate (opening comment); for each surrogate\n    the R with every unit's convolved trace over the kept frames; the test-Rs of unit i are the R of\n    the surrogates of each surrogate's second-best unit with unit i's convolved trace (pooled over\n    all 1'000 surrogates, imaging_tools.compute_test_r); the GT-Rs of unit i are the R of its own\n    surrogates with its own trace. For each grid pair (100 values from 0 to 1, np.linspace rounded\n    to 3 decimals, which gives the Table 1 quantiles), the threshold is the larger of the two\n    quantiles; with unit i present, a surrogate whose best unit is i and whose best R passes is TP,\n    else FN; with unit i removed, the best R of the other units passing is FP, else TN. F with beta\n    0.5, summed over all units. The Methods and the code disagree on a surrogate whose best unit is\n    not i in the test with i present; the Methods count it FP if it passes and TN if not (main\n    reading), the code counts it FN (variant). The noise estimate uses the background ROI of claim\n    acceptance-9-of-20; for recording 3 (two spines) both spines' estimates are run. Each recording's\n    max F matches when within 10% of Table 1; ties of the maximum are all reported, and Q_GT and\n    Q_test match when one maximum lies within 10% of the Table 1 values. Reproduced when max F\n    matches for at least 17 of the 19 recordings; partially for 10 to 16; not reproduced below. The\n    quantiles are reported for each recording.\n- id: mean-max-fscore\n  statement: The simulated ground-truth test gives large F-scores across experiments, a mean maximum\n    F-score of 0.692 ± 0.136 over 19 recordings with 1'000 surrogates per unit.\n  source: Results, 3.4 Performance evaluation on experimental data, paragraph 1\n  quote: We obtained typically large F -scores across experiments (mean = 0.692 ± 0.136 based on 19\n    recordings with a mean of 102 ± 43 units per recording and 1’000 generated surrogate spine Ca 2+\n    response traces per unit)\n  depends_on:\n  - table1-optimal-thresholds\n  expected:\n  - quantity: mean of per-recording maximum F-score\n    value: 0.692\n    tolerance: 0.0692\n  - quantity: SD of per-recording maximum F-score\n    value: 0.136\n    tolerance: 0.0136\n  criterion: Mean and population SD (ddof 0) over 19 recordings, recording 3 counted once; this is\n    the reading that gives 0.692 ± 0.136 from Table 1 (20 rows give 0.697 ± 0.135). The ± is the\n    sample spread, not an uncertainty of the mean, so the tolerance is 10% of each value. Under\n    both readings of the classification of a misidentified surrogate (claim\n    table1-optimal-thresholds).\n- id: acceptance-9-of-20\n  statement: The best-matching unit passed the acceptance test, and a monosynaptic connection was\n    accepted, for 9 of the 20 spines (Table 1 rows 1, 2, 3, 4, 6, 9, 10, 12 and 16).\n  source: Results, 3.4 Performance evaluation on experimental data, paragraph 1; Table 1, columns\n    GT_thr, test_thr and accept?; Figure 5(a)\n  quote: For 9 out of 20 spines, the best-matching unit passed the acceptance test, and a\n    monosynaptic connection was confirmed\n  depends_on:\n  - table1-best-r\n  - table1-optimal-thresholds\n  expected:\n  - quantity: accepted spines\n    value: 9\n    tolerance: 0\n  criterion: The acceptance test of Results 3.2, Methods 2.7 and notebook 2, with 1'000 GT and\n    1'000 test surrogates (opening comment); accepted when best-R exceeds both thresholds. The\n    quantiles are read two ways, (a) Table 1's GT_Q and test_Q for each spine, (b) the optimal\n    quantiles found in claim table1-optimal-thresholds. The noise region is the background ROI held\n    in the dataset, if it holds one; the paper says only that it was \"close to the spine\", so\n    otherwise at least three background regions of at least the spine ROI's pixel count, without\n    visible cell structure, are placed near the spine before any R is computed, and each is run.\n    Each spine's GT_thr and test_thr are compared with Table 1 (10%). Reproduced when, under a\n    reading, each spine's decision matches Table 1 (so 9 are accepted) for every noise region;\n    partially reproduced when 17 to 19 decisions match; not reproduced otherwise. When noise\n    regions or readings give different outcomes, the claim is methods_underspecified with every\n    result shown. Rows 3 and 18 lie within 0.03 of a threshold, so their decisions are also reported\n    over five seeds.\n- id: best-r-accepted-vs-rejected\n  statement: Accepted connections have larger best-R values than rejected ones (0.584 ± 0.149\n    against 0.331 ± 0.124; Mann-Whitney U = 12.0, n1 = 9, n2 = 11, P < 0.05).\n  source: Results, 3.4 Performance evaluation on experimental data, paragraph 2; Figure 5(b)\n  quote: the accepted connections had significantly larger best-R values (0.584 ± 0.149) compared to\n    the rejected ones (0.331 ± 0.124) (Mann-Whitney U =12.0, n 1 =9, n 2 =11, P <0.05)\n  statistics:\n  - test: Mann-Whitney U\n    statistic: U = 12.0\n    p: 0.05\n    p_relation: \"<\"\n    n: 9 accepted and 11 rejected spines\n  depends_on:\n  - table1-best-r\n  - acceptance-9-of-20\n  expected:\n  - quantity: mean best-R, accepted\n    value: 0.584\n    tolerance: 0.0584\n  - quantity: mean best-R, rejected\n    value: 0.331\n    tolerance: 0.0331\n  - quantity: Mann-Whitney U\n    value: 12\n    tolerance: 1.2\n  criterion: Over the spines as classified in claim acceptance-9-of-20 and their best-R from claim\n    table1-best-r. Means and population SD (ddof 0), which give the reported ± from Table 1. The\n    paper does not say whether the test is one- or two-sided; from Table 1, U = 12 is the smaller of\n    the two U values and the two-sided p is 0.005, so both readings give P < 0.05 and both are shown.\n    Reproduced when the means and U are within tolerance and the test gives P < 0.05 with the\n    accepted group higher.\n- id: best-r-not-predictive\n  statement: The best-R alone does not predict the outcome of the acceptance test; connections with\n    R as high as about 0.6 were rejected, while an R of about 0.2 was enough for acceptance in\n    another case.\n  source: Results, 3.4 Performance evaluation on experimental data, paragraph 2; Figure 5(b)\n  quote: it is important to note that the value of the best-R alone was not a predictor for the\n    outcome of the test. In fact, as one can see from figure 5(b) , the acceptance test rejected\n    connections with R values as high as ~0.6, while in another case an R value of ~0.2 was enough\n    for acceptance\n  depends_on:\n  - table1-best-r\n  - acceptance-9-of-20\n  expected:\n  - quantity: largest best-R of a rejected spine\n    value: 0.6\n    tolerance: 0.06\n  - quantity: smallest best-R of an accepted spine\n    value: 0.2\n    tolerance: 0.02\n  criterion: Settled by the expected values (Table 1 gives 0.602, row 17, and 0.217, row 3), with\n    the further condition that the largest rejected best-R exceeds the smallest accepted one, so no\n    best-R cut separates the two groups.\n- id: fig5a-rejection-scenarios\n  statement: Connections were rejected in three scenarios, best-R below the test threshold only,\n    below the GT threshold only, or below both, which shows the advantage of having two thresholds.\n  source: Results, 3.4 Performance evaluation on experimental data, paragraph 2; Figure 5(a)\n  quote: we found that putative connections were rejected in three different scenarios: The best-R\n    was smaller than either one of the two thresholds or both thresholds\n  depends_on:\n  - acceptance-9-of-20\n  expected:\n  - quantity: rejected below the test threshold only\n    value: 4\n    tolerance: 0\n  - quantity: rejected below the GT threshold only\n    value: 1\n    tolerance: 0\n  - quantity: rejected below both thresholds\n    value: 6\n    tolerance: 0\n  criterion: The counts are not in the text; they are read from Table 1 (best_R against GT_thr and\n    test_thr; rows 7, 14, 15, 17 below test only, row 19 below GT only, rows 5, 8, 11, 13, 18, 20\n    below both). Reproduced when each of the three scenarios occurs among the rejected spines of\n    claim acceptance-9-of-20; the counts are reported against Table 1's.\n- id: fig5a-threshold-order\n  statement: For some recordings the test threshold is larger than the GT threshold, and for others\n    the reverse.\n  source: Results, 3.4 Performance evaluation on experimental data, paragraph 2; Figure 5(a)\n  quote: Note that for some recordings the test threshold was larger than the GT threshold and vice\n    versa for other recordings\n  depends_on:\n  - acceptance-9-of-20\n  criterion: Over the 20 spines' thresholds from claim acceptance-9-of-20. Reproduced when at least\n    one spine has test_thr above GT_thr and at least one the reverse. Table 1 has 15 and 5; the\n    counts are reported.\n- id: table1-network-measures\n  statement: Each recording's spike contrast (0.17 to 0.69) and ratio of spikes outside to inside\n    network bursts (0.060 to 2.003) have the values given in Table 1.\n  source: Table 1, columns OUT/IN ratio and spike contrast; Results, 3.4 Performance evaluation on\n    experimental data, paragraph 3\n  inferred: The per-recording values are given only in Table 1; the measures are defined in Results\n    3.4, paragraph 3.\n  depends_on:\n  - table1-best-r\n  criterion: Spike contrast from elephant 0.10.0 (Results 3.4), spike_contrast with its default\n    parameters, over the recording's sorted spike trains. OUT/IN is the number of spikes outside\n    network burst periods divided by the number inside, with the bursts of claim table1-best-r. The\n    paper leaves open (a) which units enter, all sorted units or those kept after the hyperactive\n    exclusion, (b) for OUT/IN, burst periods with or without the 0.1 s and 0.5 s extensions, and (c)\n    the time span, the whole MEA recording or the span of simultaneous imaging. Every combination is\n    run. A recording's value matches when within 10% of Table 1 under one combination; reproduced\n    when both measures match for at least 17 of 19 recordings under one combination used for all;\n    partially reproduced for 10 to 16; not reproduced below.\n- id: fig5c-spike-contrast-vs-fscore\n  statement: The network's spike contrast is negatively correlated with the maximum F-score of the\n    recording (Spearman R = -0.737, P = 0.0002), so more synchronous networks give poorer\n    classification.\n  source: Results, 3.4 Performance evaluation on experimental data, paragraph 3; Figure 5(c)\n  quote: We found that both the spike contrast ( R =-0.737, P =0.0002, Spearman’s rank correlation,\n    figure 5(c) ) ... of a network correlated with the classification performance as measured by the\n    maximum F -score of the respective network\n  statistics:\n  - test: Spearman's rank correlation\n    statistic: R = -0.737\n    p: 0.0002\n    n: the rows of Table 1 (its 20 spine rows reproduce the reported R and P)\n  depends_on:\n  - table1-optimal-thresholds\n  - table1-network-measures\n  expected:\n  - quantity: Spearman R, spike contrast against maximum F-score\n    value: -0.737\n    tolerance: 0.0737\n  criterion: Spearman rank correlation of spike contrast (claim table1-network-measures) with\n    maximum F-score (claim table1-optimal-thresholds). The paper says it is per network, but Table 1\n    gives -0.737 (P = 0.00021) over its 20 rows, recording 3 counted twice, and -0.742 (P = 0.00027)\n    over 19 recordings; both readings are run. Reproduced when R is within tolerance and P < 0.05\n    under one reading.\n- id: fig5d-out-in-vs-fscore\n  statement: The ratio of spikes outside to inside network bursts is positively correlated with the\n    maximum F-score of the recording (Spearman R = 0.672, P = 0.0012).\n  source: Results, 3.4 Performance evaluation on experimental data, paragraph 3; Figure 5(d) (the\n    text cites figure 5(c) for both; the legend places this one in 5(d))\n  quote: and the OUT/IN ratio ( R =0.672, P =0.0012, Spearman’s rank correlation, figure 5(c) ) of a\n    network correlated with the classification performance as measured by the maximum F -score of\n    the respective network\n  statistics:\n  - test: Spearman's rank correlation\n    statistic: R = 0.672\n    p: 0.0012\n    n: the rows of Table 1 (its 20 spine rows reproduce the reported R and P)\n  depends_on:\n  - table1-optimal-thresholds\n  - table1-network-measures\n  expected:\n  - quantity: Spearman R, OUT/IN ratio against maximum F-score\n    value: 0.672\n    tolerance: 0.0672\n  criterion: As for claim fig5c-spike-contrast-vs-fscore, with the OUT/IN ratio. Table 1 gives 0.672\n    (P = 0.0012) over its 20 rows and 0.680 (P = 0.0014) over 19 recordings; both readings are run.\n    Reproduced when R is within tolerance and P < 0.05 under one reading.\n"
}
```

```
File created successfully at: claims/000223/10.1088-1741-2552-ac8765.yaml (file state is current in your context — no need to Read it back)
```

**Agent**

The quote in `fig5a-rejection-scenarios` contains a colon followed by a space, which plain YAML scalars may not hold. I'll cut it there.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000223/10.1088-1741-2552-ac8765.yaml",
 "old_string": "  quote: we found that putative connections were rejected in three different scenarios: The best-R\n    was smaller",
 "new_string": "  quote: we found that putative connections were rejected in three different scenarios ... The\n    best-R was smaller"
}
```

```
The file claims/000223/10.1088-1741-2552-ac8765.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
f=claims/000223/10.1088-1741-2552-ac8765.yaml; python tools/claims_check.py $f paper/10.1088-1741-2552-ac8765.txt; echo exit $?; python3 - <<'EOF'
import yaml
d=yaml.safe_load(open('claims/000223/10.1088-1741-2552-ac8765.yaml'))
for c in d['claims']:
    for k,v in c.items():
        if isinstance(v,str) and ': ' in v: print('COLON',c['id'],k)
txt=open('claims/000223/10.1088-1741-2552-ac8765.yaml').read()
print('emdash' , '—' in txt, 'rather', 'rather' in txt.lower())
print(len(d['claims']), sum('quote' in c for c in d['claims']), sum('statistics' in c for c in d['claims']), sum('criterion' in c for c in d['claims']), sum('inferred' in c for c in d['claims']))
EOF
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/000223/10.1088-1741-2552-ac8765.yaml`. The quote checker passes: 13 claims, 10 quotes, 3 statistical values, 0 problems. Nothing is committed.

**Text read.** The accepted author manuscript in PubMed Central (PMC7613561), which is not the version of record. It includes the full text, Methods, figure legends, Table 1 and the one supplement (three figure supplements of Figure 1). Nothing was missing. I also read the linked code, `starquakes/mea_spineca_mapping` at commit 99c2a47: a helper module and three analysis notebooks plus an NWB-export notebook, with no saved numeric outputs.

**Claims.**
- **Count:** 13 claims, all of them findings.
- **Quotes:** 10 have quotes. The other 3 (per-spine best-R values, per-recording optimal thresholds and F-scores, per-recording network measures) have numbers only in Table 1, so they carry an `inferred` note.
- **Statistics:** 3 claims have them: the Mann-Whitney U = 12.0 (P < 0.05), and the two Spearman correlations of spike contrast and OUT/IN ratio with maximum F-score.
- **Criteria:** all 13 have one.
- **Data:** every claim uses the dataset alone.

**Readings settled by recomputing from Table 1**
- **Mean max F-score and units per recording:** 0.692 ± 0.136 and 102 ± 43 come out over 19 recordings (the two-spine recording counted once), with the population SD.
- **Spearman correlations:** the reported values come out over the 20 spine rows (the two-spine recording counted twice). Over 19 recordings they are −0.742 and 0.680. Both readings are run.
- **Accepted against rejected best-R:** the ± values are population SDs, and U = 12 is the smaller U. The two-sided p is 0.005, so a one- or two-sided test both give P < 0.05.
- **Quantile grid:** the code's 100-point grid gives exactly the quantiles printed in Table 1.

**Details the paper leaves open, with the readings named**
- **Burst threshold percentile:** "visually chosen for each data set" and not reported. Readings are the 96th to 99th percentiles, chosen per recording, with the code's default (97th) also shown.
- **Hyperactive-unit exclusion:** the Methods give two strategies, a 99.75th-percentile rate cut (the code's default) or a 15 Hz cut. Both are run.
- **Background region for the noise estimate:** the paper says only "close to the spine". If the dataset doesn't hold this region, at least three placements are fixed before analysis. If they disagree, the claim is blocked as methods underspecified.
- **Quantiles for the acceptance test:** Table 1's values, or the optimal ones re-derived from the F-score grid.
- **Spike contrast and OUT/IN:** which units enter (all sorted, or those left after excluding hyperactive units). For OUT/IN, burst periods with or without the 0.1 s / 0.5 s extensions. The time span, whole recording or imaging span.
- **Example recording of Figure 1(e):** not identified, so the claim holds if any spine shows it.
- **Random seeds:** a standard choice. Table 1 rows 3 and 18 sit near a threshold, so their accept/reject decisions are also reported over five seeds.

**Where the Methods and code disagree** (the Methods are the main reading, the code a variant):
- **Burst-edge smoothing:** the Methods smooth over 5 points; the code uses a lowess fraction of 0.0002.
- **Misidentified surrogate in the F-score test:** the Methods count it FP or TN; the code counts it FN.
- **Release probabilities:** a fresh draw per the Methods, or the stored draw in `log_release_Pr.npy`.
- **Spike retention:** the code keeps a fixed number of spikes; a Bernoulli draw per spike is the other reading of the Methods' wording.

**Missing from the paper.** There is no map from Table 1 rows to dataset files; culture ID and unit count are the only keys. The background region for the noise estimate is never specified.

## End of run

22 turns, 5 minutes, result: success.
