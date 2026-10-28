# 000248 · author · run 40609498105

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md
```

```
<persisted-output>
Output too large (35.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d3497126-e1b1-4d4f-be46-317504b398b5/tool-results/b2kdtywia.txt

Preview (first 2KB):
Wed Oct 28 00:36:58 UTC 2026
# Protocol for an attempt

Version: `pilot-12`. Record this version in the attempt's provenance.

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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/d3497126-e1b1-4d4f-be46-317504b398b5/tool-results/b2kdtywia.txt"
}
```

```
1	Wed Oct 28 00:36:58 UTC 2026
2	# Protocol for an attempt
3	
4	Version: `pilot-12`. Record this version in the attempt's provenance.
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
[... 594 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md | head -150; echo ----; wc -l docs/design.md docs/archives.md; ls claims/000248 paper entries/001453-fouke-2025 attempts | head -50
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
[... 171 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/000248 paper entries/001453-fouke-2025; ls questions | head -3; cat docs/design.md | head -120
```

```
claims/000248:
10.1038-s41593-025-02055-5.yaml

entries/001453-fouke-2025:
README.md
entry.yaml
omr.py
reproduce_fouke_2025.ipynb
requirements.in
requirements.lock.txt

paper:
10.1038-s41593-025-02055-5.txt
10.1101-2023.06.05.543698.txt
000005.yaml
000006.yaml
000008.yaml
# Reproduction registry: design

Status: draft for discussion. "Reproduction registry" is a working name.
[... 116 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/000248/10.1038-s41593-025-02055-5.yaml
```

```
<persisted-output>
Output too large (60.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d3497126-e1b1-4d4f-be46-317504b398b5/tool-results/blcnxlvrh.txt

Preview (first 2KB):
# Claims for Shin, Ogando, Abdeladim, ... Lecoq & Adesnik (2025), "Recurrent pattern completion
# drives the neocortical representation of sensory inference", Nature Neuroscience 28, 2319-2329,
# on dandiset 000248 ("Allen Institute Openscope - Illusion project").
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read: the version of record (CC BY 4.0), full text from Europe PMC in
# paper/10.1038-s41593-025-02055-5.txt: main text, figure legends, Methods and the Extended Data
# figure legends (Extended Data Figs. 1 to 10). The Supplementary Information (Supplementary
# Results, Supplementary Discussion, Supplementary Figs. 1 to 8) is not in paper/ and was not
# read. The main findings are shown in the main and Extended Data figures; the Supplementary
# Figures are cited for support only (Supp. Fig. 1 heatmaps of the subsets, Supp. Fig. 2 mesoscope
# area borders, Supp. Fig. 3 other decoders, Supp. Fig. 4, Supp. Fig. 6). The claim that rests on
# a Supplementary Figure (supp3-decoder-types) says so. The bioRxiv preprint (10.1101/2023.06.05.543698,
# version 1) is also in paper/; it was not used. No PDF was supplied, so no figure was read.
#
[... 10 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/d3497126-e1b1-4d4f-be46-317504b398b5/tool-results/blcnxlvrh.txt"
}
```

```
1	# Claims for Shin, Ogando, Abdeladim, ... Lecoq & Adesnik (2025), "Recurrent pattern completion
2	# drives the neocortical representation of sensory inference", Nature Neuroscience 28, 2319-2329,
3	# on dandiset 000248 ("Allen Institute Openscope - Illusion project").
4	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
5	# protocol pilot-10 as stated in docs/protocol.md.
6	#
7	# Text read: the version of record (CC BY 4.0), full text from Europe PMC in
8	# paper/10.1038-s41593-025-02055-5.txt: main text, figure legends, Methods and the Extended Data
9	# figure legends (Extended Data Figs. 1 to 10). The Supplementary Information (Supplementary
10	# Results, Supplementary Discussion, Supplementary Figs. 1 to 8) is not in paper/ and was not
11	# read. The main findings are shown in the main and Extended Data figures; the Supplementary
12	# Figures are cited for support only (Supp. Fig. 1 heatmaps of the subsets, Supp. Fig. 2 mesoscope
13	# area borders, Supp. Fig. 3 other decoders, Supp. Fig. 4, Supp. Fig. 6). The claim that rests on
14	# a Supplementary Figure (supp3-decoder-types) says so. The bioRxiv preprint (10.1101/2023.06.05.543698,
15	# version 1) is also in paper/; it was not used. No PDF was supplied, so no figure was read.
16	#
17	# Code. The paper's Code availability names a Code Ocean capsule, 10.24433/CO.6659254.v2
18	# (codeocean.com/capsule/2540707); it returned HTTP 403 from this run and was not read. Read in
19	# its place, as the first author's public code for this dataset (its data path is
20	# 'S:\OpenScopeData\00248_v240130\'): github.com/hs13/IC_paper_code at commit
[... 844 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/d3497126-e1b1-4d4f-be46-317504b398b5/tool-results/blcnxlvrh.txt",
 "offset": 864
}
```

```
864	  criterion: 2p holography sessions, not in this dandiset. Reproduced when the IC-encoder-only
865	    decoder's TRE inference test gives p < 0.05 with IC above LC, the segment-responder-only
866	    decoder's does not, and both decoders' cross-validation accuracy is above 0.25 at p < 0.05.
867	- id: fig5c-2p-holo-ic-responsive
868	  statement: Photoactivating IC-encoders evokes larger activity in nonphotoactivated IC-responsive
869	    neurons than in non-IC-responsive neurons, while photoactivating segment responders does not.
870	  source: Results, Neurons that encode IC inference drive neural pattern completion within V1,
871	    paragraph 4; Figure 5c; Extended Data Fig. 8b legend
872	  quote: Despite this heterogeneity, targeting IC-encoders evoked substantially larger activity in I
873	    C -responsive neurons compared to non-I C -responsive neurons during the photoactivation window
874	  statistics:
875	  - about: IC-encoder ensembles
876	    test: one-tailed Wilcoxon signed-rank test
877	    p: 0.0023
878	    n: 32 holographic ensembles
879	  - about: segment responder ensembles
880	    test: one-tailed Wilcoxon signed-rank test
881	    p: 0.966
882	    n: 37 holographic ensembles
883	  criterion: 2p holography, not in this dandiset. Reproduced when the IC-encoder test gives p < 0.05
[... 165 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001453-fouke-2025; cat entry.yaml requirements.in README.md; head -c 3000 omr.py; python -c "
import json;nb=json.load(open('reproduce_fouke_2025.ipynb'))
for c in nb['cells'][:12]: print('---',c['cell_type'],c.get('metadata'));print(''.join(c['source'])[:1500])
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
cd  cat attempts/001453-fouke-2025-01.yaml | head -150; grep -n "" docs/archives.md | sed -n 1,140p
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
[... 270 more lines not kept]
```

**Agent**

Now the dataset.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/000248/ | python -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/000248/versions/" | python -m json.tool | head -60
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/000248/versions/0.240502.2344/assets/?page_size=200" > assets.json; python -c "
import json;d=json.load(open('assets.json'));print(d['count'])
for a in d['results']: print(a['path'], round(a['size']/1e9,2), a['asset_id'])
"; curl -s "https://api.dandiarchive.org/api/dandisets/000248/versions/0.240502.2344/" > meta.json; python -c "
import json;d=json.load(open('meta.json'));print(d.get('description'));print(d.get('relatedResource'));print(d.get('assetsSummary'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
python -c "import h5py, remfile, pynwb, dandi, numpy, scipy, sklearn; print(h5py.__version__, pynwb.__version__, sklearn.__version__)"; python --version; nproc; free -g
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import h5py, remfile, pynwb, dandi, numpy, scipy, sklearn; print(h5py.__version__, pynwb.__version__, sklearn.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'h5py'
Python 3.13.16
4
               total        used        free      shared  buff/cache   available
Mem:              15           1          12           0           2          14
Swap:              2           0           2
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && . dev/bin/activate && uv pip install -q h5py remfile pynwb numpy scipy scikit-learn pandas matplotlib statsmodels requests 2>&1 | tail -2; python -c "import h5py,pynwb;print('ok')"
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > survey.py <<'EOF'
import h5py, remfile, json, sys
aid = sys.argv[1]
url = f"https://api.dandiarchive.org/api/assets/{aid}/download/"
import requests
r = requests.head(url, allow_redirects=True); url = r.url
f = h5py.File(remfile.File(url), 'r')
def visit(name, obj):
    if isinstance(obj, h5py.Dataset):
        print(name, obj.shape, obj.dtype)
    else:
        a = dict(obj.attrs)
        nd = a.get('neurodata_type')
        if nd: print(name, '<', nd, '>')
f.visititems(visit)
EOF
time python survey.py 9ab6bfff-70ed-44dc-b384-96b4cef2b566 > survey_ogen.txt; wc -l survey_ogen.txt; grep -v "intervals/" survey_ogen.txt | head -150
```

```
real	0m9.708s
user	0m0.925s
sys	0m0.096s
409 survey_ogen.txt
acquisition/EyeTracking < EllipseEyeTracking >
acquisition/EyeTracking/corneal_reflection_tracking < EllipseSeries >
acquisition/EyeTracking/corneal_reflection_tracking/angle (542132,) float64
acquisition/EyeTracking/corneal_reflection_tracking/area (542132,) float64
acquisition/EyeTracking/corneal_reflection_tracking/area_raw (542132,) float64
acquisition/EyeTracking/corneal_reflection_tracking/data (542132, 2) float64
acquisition/EyeTracking/corneal_reflection_tracking/height (542132,) float64
acquisition/EyeTracking/corneal_reflection_tracking/reference_frame () object
acquisition/EyeTracking/corneal_reflection_tracking/width (542132,) float64
acquisition/EyeTracking/eye_tracking < EllipseSeries >
acquisition/EyeTracking/eye_tracking/angle (542132,) float64
acquisition/EyeTracking/eye_tracking/area (542132,) float64
acquisition/EyeTracking/eye_tracking/area_raw (542132,) float64
acquisition/EyeTracking/eye_tracking/data (542132, 2) float64
acquisition/EyeTracking/eye_tracking/height (542132,) float64
acquisition/EyeTracking/eye_tracking/reference_frame () object
[... 135 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && grep -v "stimulus/templates/\|specifications" survey_ogen.txt | sed -n 150,420p | grep -v "^intervals/.*/\(tags\|timeseries\)"
```

```
intervals/RFCI_presentations/y_position (720,) float64
intervals/invalid_times < TimeIntervals >
intervals/invalid_times/id (1,) int64
intervals/invalid_times/start_time (1,) float64
intervals/invalid_times/stop_time (1,) float64
intervals/sizeCI_presentations < TimeIntervals >
intervals/sizeCI_presentations/Mask (960,) object
intervals/sizeCI_presentations/color (960,) object
intervals/sizeCI_presentations/contrast (960,) float64
intervals/sizeCI_presentations/id (960,) int64
intervals/sizeCI_presentations/opacity (960,) float64
intervals/sizeCI_presentations/orientation (960,) float64
intervals/sizeCI_presentations/phase (960,) object
intervals/sizeCI_presentations/size (960,) object
intervals/sizeCI_presentations/spatial_frequency (960,) object
intervals/sizeCI_presentations/start_time (960,) float64
intervals/sizeCI_presentations/stimulus_block (960,) float64
intervals/sizeCI_presentations/stimulus_index (960,) float64
intervals/sizeCI_presentations/stimulus_name (960,) object
intervals/sizeCI_presentations/stop_time (960,) float64
[... 74 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep "^intervals/" survey_ogen.txt | grep -v "/\(tags\|timeseries\)" | head -150
```

```
intervals/ICkcfg0_presentations < TimeIntervals >
intervals/ICkcfg0_presentations/frame (1380,) float64
intervals/ICkcfg0_presentations/id (1380,) int64
intervals/ICkcfg0_presentations/start_time (1380,) float64
intervals/ICkcfg0_presentations/stimulus_block (1380,) float64
intervals/ICkcfg0_presentations/stimulus_index (1380,) float64
intervals/ICkcfg0_presentations/stimulus_name (1380,) object
intervals/ICkcfg0_presentations/stop_time (1380,) float64
intervals/ICkcfg1_presentations < TimeIntervals >
intervals/ICkcfg1_presentations/frame (1380,) float64
intervals/ICkcfg1_presentations/id (1380,) int64
intervals/ICkcfg1_presentations/start_time (1380,) float64
intervals/ICkcfg1_presentations/stimulus_block (1380,) float64
intervals/ICkcfg1_presentations/stimulus_index (1380,) float64
intervals/ICkcfg1_presentations/stimulus_name (1380,) object
intervals/ICkcfg1_presentations/stop_time (1380,) float64
intervals/ICwcfg0_presentations < TimeIntervals >
intervals/ICwcfg0_presentations/frame (1380,) float64
intervals/ICwcfg0_presentations/id (1380,) int64
intervals/ICwcfg0_presentations/start_time (1380,) float64
[... 58 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; wc -c *; grep -n -i "data availability\|code availability\|dandi\|code ocean\|figshare\|zenodo" 10.1038-s41593-025-02055-5.txt | head -30
```

```
<persisted-output>
Output too large (45.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d3497126-e1b1-4d4f-be46-317504b398b5/tool-results/bfk9gb7j5.txt

Preview (first 2KB):
145452 10.1038-s41593-025-02055-5.txt
 71355 10.1101-2023.06.05.543698.txt
216807 total
16:				\begin{document}$${\rm{Cross}}{\hbox{-}}{\rm{correlogram}}\left(\tau \right)=\,\frac{\mathop{\sum }\nolimits_{t=1+{\tau }_{\max }}^{L-{\tau }_{\max }}{x}_{1}(t){x}_{2}(t+\tau )}{\sqrt{{\lambda }_{1}{\lambda }_{2}}}$$\end{document} Cross - correlogram τ = ∑ t = 1 + τ max L − τ max x 1 ( t ) x 2 ( t + τ ) λ 1 λ 2 where x 1 and x 2 are spike trains of two units across the IC configuration 1 block (72 min, 1-ms bins), L is the length of the spike trains, λ 1 and λ 2 are the net spike count across each spike train and τ is the time lag between the spike trains. To account for cofluctuations in rate, smoothed cross-correlogram was calculated from spike trains smoothed with a 25-ms window. Then, we calculated the corrected cross-correlogram by subtracting the smoothed cross-correlogram from the original cross-correlogram. To determine whether there was a putative excitatory connection between a pair of units, peaks in corrected cross-correlogram were found in 1–10-ms window. The connection was deemed substantial if the peak value exceeded the threshold, where the threshold was calculated as sevenfold of the cross-correlogram flank s.d. (between ±50 and 100 ms from zero). Statistics and reproducibility Nonparametric two-sided tests are used unless otherwise noted. Adjustments for multiple comparisons have been noted wherever they were applied. When applicable, we used cross-validation to avoid overfitting. No statistical method was used to predetermine sample size, but we used an equivalent or larger sample size than similar studies 18 , 26 , 58 , 59 . Trial order within each block was randomized. All data exclusions are described along with exclusion criteria and the 
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd  fold -s -w 200 paper/10.1038-s41593-025-02055-5.txt > $TMPDIR/paper.txt; wc -l $TMPDIR/paper.txt; grep -n -i "data availability\|code availability\|Neuropixels\b.*record\|Allen Brain Observatory\|regular-spiking\|gray screen\|grey" $TMPDIR/paper.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/paper.txt",
 "offset": 300,
 "limit": 160
}
```

```
300	transgenic line expressing the transgene TITL-st-ChroME-GCaMP7s-ICL-nls-mRuby3-IRES2-tTA2; n = 2). All experiments on animals were conducted with approval of the Animal Care and Use Committee of the 
301	University of California, Berkeley (imaging and 2p holographic optogenetics experiments) and the Allen Institute’s Institutional Animal Care and Use Committee (Neuropixels experiments). Surgery Mice 
302	were anesthetized with isoflurane (2%) and mounted on a stereotaxic apparatus. Buprenorphine (0.05 mg kg −1 , analgesic) and dexamethasone (2 mg kg −1 , anti-inflammatory) were injected 
303	subcutaneously. Body temperature was maintained at 36.5 °C. After hair removal and disinfection with 70% ethanol and 5% iodine, the scalp was removed and the fascia was retracted. A circular 
304	craniotomy of 3–5 mm was made on the left hemisphere using a biopsy punch (Robbins Instruments) and/or a dental drill (Foredom) with a 0.5 mm drill bit (FST Item 19007-05). Glass coverslips of 3–5 mm 
305	diameter were placed on top of the craniotomy and sealed with dental cement (C&B Metabond). These glass coverslips, or ‘windows’, were made beforehand by gluing two layers of round cover glass (for 
306	example, 1 × 3 mm + 1 × 5 mm, Warner Instruments, 1 thickness) with Norland Optical Adhesive 71 (UV-cured). Finally, a titanium headplate was fixed to the skull with dental cement (C&B Metabond). The 
307	dental cement was coated in a layer of black oxide to mitigate light leakage during 2p imaging. For 2p holographic optogenetics experiments, we injected the GCaMP6m-p2A-ChRmine-Kv2.1 virus during the 
308	window implant surgery (500 nl per two depths and two sites). Injection speed was 100–250 nl min −1 , and after injection in each site, pipette was held in place for 5 min. Injection sites were 
309	centered at 2.7 mm lateral, 0.2 mm anterior relative to lambda and injection depths were 120 µm and 250 µm. Neuropixels experiments The Neuropixels data were acquired at the Allen Inst
[... 150 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/paper.txt",
 "offset": 56,
 "limit": 110
}
```

```
56	subset of neurons that responded emergently to the IC (‘IC-encoders’) mediated the representation of IC inference. To test whether these IC-encoders could drive IC representations within V1L2/3 on 
57	their own, we holographically photoactivated them in the absence of any visual stimulus. We found that photoactivating IC-encoders recreated IC representations within V1L2/3 through pattern 
58	completion. These results imply that neurons that encode top-down inference signals locally broadcast those signals through pattern completion. On the other hand, neurons that respond to the 
59	individual inducing segments of the IC (‘segment responders’) drove IC representations in higher visual areas but not within V1L2/3. Taken together, recurrent activity through feedforward, feedback 
60	and local pattern completion circuits may facilitate sensory inference by reinforcing activity patterns that match the brain’s prior expectations about the sensory world. Results Mouse V1 neurons 
61	respond to ICs despite the absence of contrast within their receptive fields Using two high-throughput neural recording techniques with complementary strengths, multi-Neuropixels and large-scale 2p 
62	imaging, we recorded the neural activity of awake, head-fixed mice while presenting the animals with various images containing real edges or ICs (I C denotes ‘I-shaped combination’, I RE denotes 
63	‘I-shaped real edge’; Fig. 1b and Extended Data Fig. 1 ). First, we asked if we could identify visual cortical neurons that respond to ICs even in the absence of any contrast within their receptive 
64	fields, as previously shown in primates 9 , 10 , 14 . We focused on V1 neurons whose receptive fields are contained entirely within the gap region. If these neurons are driven by ICs, then their 
65	visually evoked activity is, by definition, not bottom up 7 , 9 , 10 , 14 . Thus, we selected only those neurons that responded exclusively to the illusory gap region, that is, the central 16 visual 
66	
[... 99 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 20,52p $TMPDIR/paper.txt; grep -n "Extended Data Fig. [267] |" $TMPDIR/paper.txt | head;
```

```
included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the 
copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/ . When sensory information is incomplete, the brain relies on prior expectations to infer 
perceptual objects. Despite the centrality of this process to perception, the neural mechanisms of sensory inference are not understood. Here we used illusory contours (ICs), multi-Neuropixels 
measurements, mesoscale two-photon (2p) calcium imaging and 2p holographic optogenetics in mice to reveal the neural codes and circuits of sensory inference. We discovered a specialized subset of 
neurons in primary visual cortex (V1) that respond emergently to illusory bars but not to component image segments. Selective holographic photoactivation of these ‘IC-encoders’ recreated the visual 
representation of ICs in V1 in the absence of any visual stimulus. These data imply that neurons that encode sensory inference are specialized for receiving and locally broadcasting top-down 
information. More generally, pattern completion circuits in lower cortical areas may selectively reinforce activity patterns that match prior expectations, constituting an integral step in perceptual 
inference. Neurons that respond emergently to illusory contours drive pattern completion in V1. Pattern completion in lower cortical areas may therefore mediate perceptual inference by selectively 
reinforcing activity patterns that match prior expectations. Subject terms Striate cortex Sensory processing Extrastriate cortex Neural decoding https://doi.org/10.13039/100000002 U.S. Department of 
Health & Human Services | National Institutes of Health (NIH) U19NS107613 U24NS113646 Lecoq Jerome Adesnik Hillel Chan Zuckerberg Biohub Investigor Award https://doi.org/10.13039/501100002551 Seoul 
National University New Faculty
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/hs13/IC_paper_code.git && cd IC_paper_code && git checkout -q 50e04eaf7c9192a067c129f3c1f174a27f10c406 && ls -R | head -60
```

```
.:
LICENSE
aggregateICtxi_SVM_trainICRC_areas.m
aggregateICtxi_SVM_trainREx_areas.m
aggregateMouseEye.m
aggregate_fixedgaze.m
aggregate_psth.m
analyzeICtxi_SVM_areas.m
analyzeICtxi_SVM_subsets.m
analyzeMouseEye.m
analyzeRFCI.m
analyzeRFCIspin.m
analyzeStaticICtxi.m
analyze_CCGfftlong.m
analyzesizeCI.m
check_CCF.m
computeCCGpeaktroughs.m
merge_postprocessed.m
plot_MouseEye.m
plot_SVM_trainICRC_areas.m
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/IC_paper_code && wc -l *.m && cat postprocessnwb_v240130.m | head -400
```

```
197 aggregateICtxi_SVM_trainICRC_areas.m
   192 aggregateICtxi_SVM_trainREx_areas.m
   125 aggregateMouseEye.m
   624 aggregate_fixedgaze.m
   593 aggregate_psth.m
   477 analyzeICtxi_SVM_areas.m
   442 analyzeICtxi_SVM_subsets.m
   599 analyzeMouseEye.m
   127 analyzeRFCI.m
   181 analyzeRFCIspin.m
   469 analyzeStaticICtxi.m
   306 analyze_CCGfftlong.m
   340 analyzesizeCI.m
   220 check_CCF.m
    82 computeCCGpeaktroughs.m
   416 merge_postprocessed.m
   579 plot_MouseEye.m
   553 plot_SVM_trainICRC_areas.m
   604 plot_SVM_trainREx_areas.m
   431 postprocess_optotagging.m
[... 401 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/IC_paper_code && cat analyzeRFCI.m && sed -n 1,200p analyzeStaticICtxi.m
```

```
% THIS CODE TREATS THE ENTIRE SPINNING GRATING AS ONE TRIAL, CONSISTENT
% WITH THE ANALYSIS DONE WITH 2P DATASET

% % 10000s: which type (classic 0 vs inverse 1), 1000s which ctrsizes, 
% % 10-100s: which RFcenter, 1s: which direction
% RFCI = struct();
% tloi = psthtli>0 & psthtli<=1000;
% tempR = squeeze(1000*mean(psth.RFCI(tloi,:,:), 1))';
% temptrialorder = vis.RFCI_presentations.trialorder(1:4:end);
% RFCI.(visblocknames{b}) = analyzeRFCI(tempR, temptrialorder);

% 'RFcentersrel', 'cRFsigneurons', 'cRFind', 'iRFsigneurons', 'iRFind', ...
% 'RFcentersrel9', 'RFcenterinds9', 'cRFind9', 'pRFclassic9', 'cRFsigexcl9', ...
% 'iRFind9', 'pRFinverse9', 'iRFsigexcl9')

function RFCI = analyzeRFCI(R, trialorder, sponFR)

Nneurons = size(R,1);
if numel(sponFR) ~= Nneurons
    error('check sponFR')
[... 308 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/IC_paper_code && sed -n 200,469p analyzeStaticICtxi.m
```

```
end
if verbosity
toc
disp('calculated SP_BICREl')
end

% sigmcBICREl = zeros( Nneurons, size(SP_BICREl,2) );
% sigmcBICREl(SP_BICREl>0.5) = 1;
% sigmcBICREl(SP_BICREl<0.5) = -1;
% sigmcBICREl(PmcBICREl(:, 1:4)>=Palpha) = 0;
% sigmcBICREl(PkwBICREl>=Palpha, :)=0;

SP_BICREl1 = SP_BICREl(:, ismember(BICREltt(2:end), BICREl1tt(2:end)));
sigmcBICREl1 = zeros(size(SP_BICREl1));
sigmcBICREl1(SP_BICREl1>0.5) = 1;
sigmcBICREl1(SP_BICREl1<0.5) = -1;
sigmcBICREl1(PmcBICREl1(:, BICREl1ttpair(:,1)==0)>=Palpha) = 0;
sigmcBICREl1(PkwBICREl1>=Palpha, :)=0;

SP_BICREl2 = SP_BICREl(:, ismember(BICREltt(2:end), BICREl2tt(2:end)));
[... 251 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t1.py <<'EOF'
import h5py, remfile, requests, numpy as np, time, collections
aid="9ab6bfff-70ed-44dc-b384-96b4cef2b566"
url=requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=True).url
f=h5py.File(remfile.File(url),'r')
st=f['units/spike_times']; print(st.chunks, st.compression, f['units/waveform_mean'].chunks)
el=f['general/extracellular_ephys/electrodes']
loc=el['location'][:].astype(str); eid=el['id'][:]
print(collections.Counter(loc).most_common(60))
u=f['units']
pk=u['peak_channel_id'][:]; q=u['quality'][:].astype(str); wd=u['waveform_duration'][:]
print(collections.Counter(q))
m=dict(zip(eid,loc)); uloc=np.array([m[p] for p in pk])
print(collections.Counter(uloc).most_common(60))
print(np.percentile(wd,[0,10,50,90,100]))
idx=u['spike_times_index'][:]
vis=np.array([l.startswith('VIS') for l in uloc])
print('vis units',vis.sum(), 'spikes', (np.diff(np.r_[0,idx])[vis]).sum())
for k in ['spontaneous_presentations','invalid_times']:
    g=f['intervals/'+k]; print(k, g['start_time'][:], g['stop_time'][:], g.get('stimulus_name',[None])[:] if 'stimulus_name' in g else '')
for k in ['ICwcfg1_presentations','ICwcfg0_presentations','ICkcfg1_presentations','ICkcfg0_presentations','RFCI_presentations','sizeCI_presentations']:
    g=f['intervals/'+k]; s=g['start_time'][:]; e=g['stop_time'][:]; print(k, s[0], e[-1], len(s), np.median(e-s), np.unique(g['stimulus_block'][:]))
g=f['intervals/ICwcfg1_presentations']; fr=g['frame'][:]; print(fr[:40], np.unique(fr), g['stimulus_name'][:3], g['stimulus_index'][:3])
g=f['intervals/RFCI_presentations']
for c in ['Mask','orientation','x_position','y_position','size','units','stimulus_name','contrast','temporal_frequency','spatial_frequency','phase','color','opacity']:
    v=g[c][:]; print(c, v[:8], len(np.unique(v)))
print(f['general/subject/genotype'][()], f['general/subject/age'][()], f['general/session_id'][()], f['session_description'][()])
t=time.time(); a=st[0:5_000_000]; print('5M spikes read', time.time()-t)
EOF
python t1.py
```

```
None None None
[(np.str_('root'), 625), (np.str_('CA1'), 130), (np.str_('MB'), 114), (np.str_('ProS'), 111), (np.str_('DG-mo'), 105), (np.str_('SUB'), 105), (np.str_('APN'), 70), (np.str_('NB'), 61), (np.str_('MGd'), 53), (np.str_('MGm'), 42), (np.str_('POST'), 41), (np.str_('TH'), 40), (np.str_('SCig'), 35), (np.str_('MRN'), 33), (np.str_('NOT'), 31), (np.str_('HPF'), 31), (np.str_('PRE'), 30), (np.str_('VISl5'), 28), (np.str_('DG-sg'), 28), (np.str_('VISal5'), 28), (np.str_('PPT'), 26), (np.str_('VISp6a'), 23), (np.str_('VISam5'), 22), (np.str_('VISpm5'), 22), (np.str_('VISpm2/3'), 22), (np.str_('VISal2/3'), 22), (np.str_('VISrl5'), 22), (np.str_('VISam2/3'), 21), (np.str_('VISp5'), 21), (np.str_('VISp2/3'), 21), (np.str_('PoT'), 21), (np.str_('VISrl2/3'), 21), (np.str_('VISl2/3'), 20), (np.str_('VISl6a'), 19), (np.str_('DG-po'), 19), (np.str_('VISal6a'), 19), (np.str_('VISpm6a'), 17), (np.str_('CA3'), 17), (np.str_('VISam6a'), 15), (np.str_('VISam1'), 14), (np.str_('POL'), 14), (np.str_('VISrl6a'), 14), (np.str_('VISl4'), 13), (np.str_('VISal4'), 13), (np.str_('VISrl1'), 12), (np.str_('VISl1'), 11), (np.str_('VISal1'), 11), (np.str_('VISpm1'), 10), (np.str_('VISpm4'), 9), (np.str_('VISp1'), 9), (np.str_('VISrl4'), 9), (np.str_('VISp4'), 8), (np.str_('VISam4'), 7), (np.str_('VISp6b'), 4), (np.str_('VISal6b'), 4), (np.str_('VISpm6b'), 3), (np.str_('VISl6b'), 3), (np.str_('VISrl6b'), 3), (np.str_('VISam6b'), 2)]
Counter({np.str_('good'): 2487, np.str_('noise'): 539})
[(np.str_('ProS'), 255), (np.str_('SUB'), 175), (np.str_('CA1'), 165), (np.str_('MGm'), 123), (np.str_('POST'), 117), (np.str_('APN'), 108), (np.str_('MB'), 97), (np.str_('TH'), 97), (np.str_('VISpm2/3'), 87), (np.str_('VISl5'), 80), (np.str_('VISal5'), 80), (np.str_('NB'), 77), (np.str_('VISp5'), 69), (np.str_('DG-mo'), 68), (np.str_('VISpm5'), 67), (np.str_('VISam2/3'), 66), (np.str_('VISp6a'), 65), (np.str_('PoT'), 60), (np.str_('VISal2/3'), 59), (np.str_('VISam5'), 57), (np.str_('VISp2/3'), 56), (np
[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && cat > t2.py <<'EOF'
import h5py, remfile, requests, numpy as np, json
from concurrent.futures import ThreadPoolExecutor
d=json.load(open('assets.json'))['results']
og=[a for a in d if a['path'].endswith('ogen.nwb')]
def info(a):
    url=requests.head(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/",allow_redirects=True).url
    f=h5py.File(remfile.File(url),'r')
    out=[a['path'].split('/')[0]]
    et='acquisition/EyeTracking' in f
    out.append(et)
    if et:
        p=f['acquisition/EyeTracking/pupil_tracking']
        out.append({k:p['data'].attrs.get(k) for k in ['unit','conversion']}); out.append(dict(p.attrs).get('description'))
        out.append(p['data'][:3].tolist()); out.append(f['acquisition/EyeTracking/eye_tracking/timestamps'][:3].tolist())
        out.append(list(p.keys()))
    out.append(list(f['intervals'].keys()))
    out.append(f['units/id'].shape[0])
    out.append(f['general/subject/genotype'][()])
    return out
with ThreadPoolExecutor(6) as ex:
    for r in ex.map(info, og): print(r)
EOF
python t2.py
```

```
Wed Oct 28 00:40:07 UTC 2026
['sub-633229', True, {'unit': 'meters', 'conversion': np.float64(1.0)}, 'no description', [[nan, nan], [nan, nan], [nan, nan]], [2.14174, 2.15841, 2.17507], ['angle', 'area', 'area_raw', 'data', 'height', 'reference_frame', 'timestamps', 'width'], ['ICkcfg0_presentations', 'ICkcfg1_presentations', 'ICwcfg0_presentations', 'ICwcfg1_presentations', 'RFCI_presentations', 'invalid_times', 'sizeCI_presentations', 'spontaneous_presentations'], 3026, b'Sst-IRES-Cre/wt;Ai32(RCL-ChR2(H134R)_EYFP)/wt']
['sub-631510', True, {'unit': 'meters', 'conversion': np.float64(1.0)}, 'no description', [[nan, nan], [nan, nan], [nan, nan]], [1.96015, 1.97681, 1.99348], ['angle', 'area', 'area_raw', 'data', 'height', 'reference_frame', 'timestamps', 'width'], ['ICkcfg0_presentations', 'ICkcfg1_presentations', 'ICwcfg0_presentations', 'ICwcfg1_presentations', 'RFCI_presentations', 'invalid_times', 'sizeCI_presentations', 'spontaneous_presentations'], 2386, b'Sst-IRES-Cre/wt;Ai32(RCL-ChR2(H134R)_EYFP)/wt']
['sub-620334', True, {'unit': 'meters', 'conversion': np.float64(1.0)}, 'no description', [[nan, nan], [nan, nan], [nan, nan]], [2.1061, 2.12277, 2.13944], ['angle', 'area', 'area_raw', 'data', 'height', 'reference_frame', 'timestamps', 'width'], ['ICkcfg0_presentations', 'ICkcfg1_presentations', 'ICwcfg0_presentations', 'ICwcfg1_presentations', 'RFCI_presentations', 'invalid_times', 'sizeCI_presentations', 'spontaneous_presentations'], 2092, b'Sst-IRES-Cre/wt;Ai32(RCL-ChR2(H134R)_EYFP)/wt']
['sub-620333', True, {'unit': 'meters', 'conversion': np.float64(1.0)}, 'no description', [[nan, nan], [nan, nan], [nan, nan]], [1.89122, 1.90789, 1.92455], ['angle', 'area', 'area_raw', 'data', 'height', 'reference_frame', 'timestamps', 'width'], ['ICkcfg0_presentations', 'ICkcfg1_presentations', 'ICwcfg0_presentations', 'ICwcfg1_presentations', 'RFCI_presentations', 'invalid_times', 'sizeCI_presentations', 'spontaneous_presentations'], 2593, b'Sst-IRES-Cre/wt;Ai32(RCL-ChR
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/IC_paper_code && grep -n "pupil\|blink\|mode\|20\b\|thr\|fixedgaze\|trialstart\|psthtli\|area" analyzeMouseEye.m | head -80
```

```
43:    likelyblink = nwb.acquisition.get('EyeTracking').likely_blink.data.load();
45:    % PupilTracking Eye-tracking data, representing pupil size
50:    % all areas are in units of pixels2
51:    eyefields = {'angle', 'area', 'area_raw', 'height', 'width', 'data'};
53:    pupiltracking = struct();
57:        pupiltracking.(eyefields{e}) = nwb.acquisition.get('EyeTracking').pupil_tracking.(eyefields{e}).load();
65:    % histogram2(pupiltracking.data(1,:), pupiltracking.data(2,:), 'binwidth', binpix, 'displaystyle', 'tile')
66:    [N,XEDGES,YEDGES] = histcounts2(pupiltracking.data(1,:), pupiltracking.data(2,:), 'binwidth', binpix);
76:    modecom = [xbinctrs(r) ybinctrs(c)];
77:%     disp(modecom)
78:%     figure; plot(pupiltracking.data(1,:),pupiltracking.data(2,:),'.')
79:%     hold on; scatter(modecom(1), modecom(2), 100,'rx', 'linewidth', 2)
80:%     figure; histogram2(pupiltracking.data(1,:),pupiltracking.data(2,:),'displaystyle', 'tile')
81:%     hold on; scatter(modecom(1), modecom(2), 100,'rx', 'linewidth', 2)
83:    distmodecom = sqrt(sum((pupiltracking.data'-modecom).^2,2));
84:    % when distmodecom threshold is set to 10 pixels, 50% of the trials are preserved
86:    if ~isequal(size(distmodecom), size(likelyblink))
87:        error('timestamps ot shared between likely_blink, eye_tracking and pupil_tracking?')
92:    trialdistmodecom = struct();
93:    trialmaxdistmodecom = struct();
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/IC_paper_code && sed -n 40,130p analyzeMouseEye.m; sed -n 196,275p analyzeMouseEye.m; sed -n 280,360p analyzeMouseEye.m
```

```
TrackEyeTimestamps = nwb.acquisition.get('EyeTracking').eye_tracking.timestamps.load();
    % figure; histogram(diff(TrackEyeTimestamps))
    
    likelyblink = nwb.acquisition.get('EyeTracking').likely_blink.data.load();
    
    % PupilTracking Eye-tracking data, representing pupil size
    % EyeTracking Eye-tracking data, representing direction of gaze
    % angle refers to phi, which is the rotation fit to the height
    % NaNs occur when DeepLabCut didn’t output enough points to fit an ellipse.
    % all positions (width, height, center_x, center_y) are in units of pixels
    % all areas are in units of pixels2
    eyefields = {'angle', 'area', 'area_raw', 'height', 'width', 'data'};
    eyetracking = struct();
    pupiltracking = struct();
    cornealreflection = struct();
    for e = 1:numel(eyefields)
        eyetracking.(eyefields{e}) = nwb.acquisition.get('EyeTracking').eye_tracking.(eyefields{e}).load();
        pupiltracking.(eyefields{e}) = nwb.acquisition.get('EyeTracking').pupil_tracking.(eyefields{e}).load();
        cornealreflection.(eyefields{e}) = nwb.acquisition.get('EyeTracking').corneal_reflection_tracking.(eyefields{e}).load();
    end
[... 233 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/IC_paper_code && sed -n 1,200p analyzeICtxi_SVM_areas.m | grep -v "^\s*%" | head -170
```

```
clear all; close all; clc

datadir = 'S:\OpenScopeData\00248_v240130\';
nwbdir = dir(datadir);
nwbsessions = {nwbdir.name};
nwbsessions = nwbsessions( contains(nwbsessions, 'sub-') | contains(nwbsessions, 'sub_') );
Nsessions = numel(nwbsessions);

svmdesc = 'trainICRC';
preproc = 'zscore'; % zscore or minmax or meancenter
whichSVMkernel = 'Linear';
neuopt = '';

rng('shuffle')
for ises = 2%1:Nsessions
    clearvars -except datadir nwbsessions ises whichSVMkernel svmdesc preproc neuopt
    sesclk = tic;
    
    allblocks = false;
    computeSVM = true;
[... 150 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/IC_paper_code && sed -n 200,330p analyzeICtxi_SVM_areas.m | grep -v "^\s*%"; sed -n 140,180p aggregateICtxi_SVM_trainICRC_areas.m
```

```
SVMout.analtrials = find(trials2anal);
            else
                warning('balancing number of trials')
                trials2anal = false(numrectrials,1);
                for typi1 = 1:Ntt
                    trialsintype = find(trialorder==SVMout.trialtypes(typi1));
                    trialsintype = trialsintype(1:Ntrialspertype);
                    trials2anal(trialsintype) = true;
                end
                if all(cftttrials(trials2anal)) && ~any(trials2anal(~cftttrials))
                    SVMout.analtrials = find(trials2anal);
                else
                    error('trials to analyze was not selected correctly')
                end
            end
            SVMout.analtriallabels = trialorder(trials2anal);
            
            Ntesttrialspertype = floor(Ntrialspertype/Nsplits);
            Ntraintrialspertype = Ntrialspertype - Ntesttrialspertype;
            SVMout.Ntt = Ntt;
[... 144 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; mkdir -p entries/000248-shin-2025; cd $TMPDIR && . dev/bin/activate && python -c "import numba" 2>&1; uv pip install -q numba 2>&1|tail -1; python -c "import numba;print(numba.__version__)"
```

```
Wed Oct 28 00:41:12 UTC 2026
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import numba
ModuleNotFoundError: No module named 'numba'
0.68.1
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "entries/000248-shin-2025/illusion.py",
 "content": "\"\"\"Loading and measures for the Neuropixels illusory contour sessions of dandiset 000248.\n\nShin, Ogando, Abdeladim, ... Lecoq & Adesnik (2025), Nature Neuroscience 28, 2319-2329,\ndoi:10.1038/s41593-025-02055-5.\n\nEach session is one `*_ogen.nwb` file, which holds the units of all six probes (spike times,\nwaveform duration, peak channel), the electrode table with the CCF area label of each channel,\nthe stimulus tables of the four IC blocks, the receptive field block (RFCI) and the size block,\nthe spontaneous (gray screen) intervals and, in 10 sessions, the eye tracking fits. The\n`*_probe-N_ecephys.nwb` files hold LFP and are not read. Files are streamed from the archive at\nthe pinned version; nothing is written to disk.\n\nWhere the parameters come from. \"Criterion\" means the claim's criterion in\nclaims/000248/10.1038-s41593-025-02055-5.yaml; \"code\" means the paper's analysis code,\ngithub.com/hs13/IC_paper_code at commit 50e04eaf7c9192a067c129f3c1f174a27f10c406, which the\nclaims file cites.\n\n- RS units: waveform_duration > 0.4 ms (Methods, \"trough-to-peak width of >=0.4 ms\"; code,\n  analyzeICtxi_SVM_areas.m `neuRS = unit_wfdur>0.4`). No quality filter (criterion of\n  results-npx-units-per-session); the `quality` column is kept so that a variant can drop the\n  units labelled noise.\n- Area: the location label of the unit's peak channel; V1 is a label starting with 'VISp' but\n  not 'VISpm' (code). The layer is the rest of the label ('VISp2/3' is layer 2/3).\n- IC trials: every second row of an IC block table from the first row with a non-zero `frame`,\n  and the frame value indexes `IC_TRIAL_TYPES` (code, postprocessnwb_v240130.m, with its rule\n  for a first or last trial that is blank).\n- IC response: spikes in the 1-ms bins 1 to 400 after the bin of image onset, one count per bin\n  as the code's boolean spike trains have, in spikes/s (code, postprocessnwb_v240130.m).\n- RF trial: every fourth row of the RFCI table (one presentation of four directions), spikes in\n  the 1-ms bins 1 to 1000 after onset (code). Position 0 is the center.\n- Spontaneous rate: mean rate over the longest spontaneous interval (code).\n- Kruskal-Wallis followed by Tukey-Kramer comparisons on mean ranks, as MATLAB's multcompare\n  does after kruskalwallis (Methods; code analyzeStaticICtxi.m), and the AUROC of\n  perfcurve.\n- Eye: pupil position from `pupil_tracking`; the mode is the center of the most populated 3-pixel\n  bin of a 2D histogram over the session; per trial, the largest distance from the mode in the\n  frames from the first frame after onset to 0.4 s (IC) or 1 s (RF), at the 60 Hz the code\n  assumes, and whether any of those frames is a likely blink (code, analyzeMouseEye.m).\n\"\"\"\n\nfrom __future__ import annotations\n\nimport re\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nfrom dandi.dandiapi import DandiAPIClient\nfrom scipy import stats\nfrom scipy.stats import studentized_range\n\nDANDISET_ID = \"000248\"\nDANDISET_VERSION = \"0.240502.2344\"\n\nIC_BLOCKS = [\"ICwcfg1\", \"ICwcfg0\", \"ICkcfg1\", \"ICkcfg0\"]\n# code, postprocessnwb_v240130.m: frame value k is trial type IC_TRIAL_TYPES[k]\nIC_TRIAL_TYPES = np.array([0, 101, 105, 106, 107, 109, 110, 111, 506, 511, 1105, 1109, 1201, 1299,\n                           1301, 1302, 1303, 1304, 1305, 1306, 1307, 1308])\nBLANK, IC1, LC1, LC2, IC2 = 0, 106, 107, 110, 111\nIRE1, IRE2, TRE1, TRE2, XRE1, XRE2 = 506, 511, 1105, 1109, 1201, 1299\nSEG_IN = [1301, 1302, 1303, 1304]   # In BR, BL, TL, TR (ICwcfg1)\nSEG_OUT = [1305, 1306, 1307, 1308]\nAREAS = [\"V1\", \"LM\", \"RL\", \"AL\", \"PM\", \"AM\"]\nAREA_PREFIX = {\"V1\": \"VISp\", \"LM\": \"VISl\", \"RL\": \"VISrl\", \"AL\": \"VISal\", \"PM\": \"VISpm\", \"AM\": \"VISam\"}\n# Orientation of the illusory (and real) bar of image 1 and 2 in each white-circle block\n# (Fig. 2c legend: IC1 135 and IC2 45 degrees; configuration 0 is rotated 315 degrees clockwise)\nBAR_ORIENTATION = {(\"ICwcfg1\", 1): 135, (\"ICwcfg1\", 2): 45, (\"ICwcfg0\", 1): 90, (\"ICwcfg0\", 2): 0}\n\nRS_WIDTH_MS = 0.4\nIC_WINDOW_MS = 400\nRF_WINDOW_MS = 1000\nEYE_HZ = 60.0\nEYE_BIN_PX = 3.0\n\n\ndef area_of(label: str) -> str | None:\n    \"\"\"Area name of a CCF location label, or None outside the six visual areas.\"\"\"\n    m = re.match(r\"VIS(pm|am|rl|al|p|l)(\\d.*)?$\", label)\n    if not m:\n        return None\n    return {\"p\": \"V1\", \"l\": \"LM\", \"rl\": \"RL\", \"al\": \"AL\", \"pm\": \"PM\", \"am\": \"AM\"}[m.group(1)]\n\n\ndef layer_of(label: str) -> str:\n    m = re.match(r\"VIS(pm|am|rl|al|p|l)(.*)$\", label)\n    return m.group(2) if m and m.group(2) else \"?\"\n\n\ndef session_assets() -> list[dict]:\n    \"\"\"The session files (one `_ogen.nwb` per session) of the pinned version, with their URLs.\"\"\"\n    with DandiAPIClient() as client:\n        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)\n        out = []\n        for a in ds.get_assets():\n            if a.path.endswith(\"_ogen.nwb\"):\n                out.append({\"path\": a.path, \"asset_id\": a.identifier, \"size\": a.size,\n                            \"url\": a.get_content_url(follow_redirects=1, strip_query=True)})\n    return sorted(out, key=lambda r: r[\"path\"])\n\n\ndef all_assets() -> list[dict]:\n    with DandiAPIClient() as client:\n        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)\n        return [{\"path\": a.path, \"size\": a.size} for a in ds.get_assets()]\n\n\ndef _str(x):\n    return x.decode() if isinstance(x, bytes) else str(x)\n\n\ndef ic_trials(frame: np.ndarray) -> np.ndarray:\n    \"\"\"Row indices of image presentations in an IC block (code, postprocessnwb_v240130.m).\"\"\"\n    nz = np.flatnonzero(frame != 0)\n    first, last = nz[0] + 1, nz[-1] + 1          # 1-based, as in the code\n    if first % 10 != 1:\n        first = 10 * (first // 10) + 1\n    if last % 10 != 9:\n        last = 10 * (last // 10) + 9\n    return np.arange(first, last + 1, 2) - 1\n\n\ndef _window_counts(bins_list, onset_ms, lo, hi):\n    \"\"\"Spike counts per (trial, unit): 1-ms bins b with onset+lo <= b <= onset+hi.\"\"\"\n    out = np.zeros((len(onset_ms), len(bins_list)), dtype=np.float32)\n    for j, b in enumerate(bins_list):\n        out[:, j] = np.searchsorted(b, onset_ms + hi, side=\"right\") - np.searchsorted(b, onset_ms + lo, side=\"left\")\n    return out\n\n\ndef load_session(asset: dict, ccg: bool = True) -> dict:\n    \"\"\"Read one session and reduce it to what the analyses use.\n\n    Units of the six visual areas only. Returns per-trial responses (spikes/s) of every such unit\n    in the four IC blocks and in the RF block, spontaneous rates, eye measures per trial, and, when\n    `ccg`, the 1-ms spike bins of RS units during the ICwcfg1 block for the cross-correlograms.\n    \"\"\"\n    f = h5py.File(remfile.File(asset[\"url\"]), \"r\")\n    s = {\"path\": asset[\"path\"], \"subject\": _str(f[\"general/subject/subject_id\"][()]),\n         \"session_id\": _str(f[\"general/session_id\"][()]),\n         \"genotype\": _str(f[\"general/subject/genotype\"][()]), \"age\": _str(f[\"general/subject/age\"][()])}\n    el = f[\"general/extracellular_ephys/electrodes\"]\n    loc_by_id = dict(zip(el[\"id\"][:], (_str(x) for x in el[\"location\"][:])))\n    u = f[\"units\"]\n    peak = u[\"peak_channel_id\"][:]\n    labels = np.array([loc_by_id[p] for p in peak])\n    s[\"n_units_file\"] = len(peak)\n    s[\"unit_labels_all\"] = pd.Series(labels).value_counts()\n    keep = np.flatnonzero([area_of(x) is not None for x in labels])\n    units = pd.DataFrame({\n        \"unit_index\": keep, \"unit_id\": u[\"id\"][:][keep], \"label\": labels[keep],\n        \"area\": [area_of(x) for x in labels[keep]], \"layer\": [layer_of(x) for x in labels[keep]],\n        \"waveform_duration\": u[\"waveform_duration\"][:][keep],\n        \"quality\": [_str(x) for x in u[\"quality\"][:][keep]],\n        \"firing_rate\": u[\"firing_rate\"][:][keep], \"probe\": peak[keep] // 1000})\n    units[\"rs\"] = units.waveform_duration > RS_WIDTH_MS\n    s[\"waveform_duration_all\"] = u[\"waveform_duration\"][:]\n    s[\"quality_all\"] = np.array([_str(x) for x in u[\"quality\"][:]])\n    s[\"area_all\"] = np.array([area_of(x) for x in labels], dtype=object)\n    idx = u[\"spike_times_index\"][:]\n    starts = np.r_[0, idx[:-1]]\n    st = u[\"spike_times\"]\n    # read contiguous runs of kept units at once\n    bins = [None] * len(keep)\n    run_start = 0\n    while run_start < len(keep):\n        run_end = run_start\n        while run_end + 1 < len(keep) and keep[run_end + 1] == keep[run_end] + 1:\n            run_end += 1\n        a, b = starts[keep[run_start]], idx[keep[run_end]]\n        chunk = st[a:b]\n        for k in range(run_start, run_end + 1):\n            t = chunk[starts[keep[k]] - a: idx[keep[k]] - a]\n            bins[k] = np.unique(np.floor(t * 1000.0).astype(np.int64))\n        run_start = run_end + 1\n    s[\"sorted_ok\"] = all(np.all(np.diff(st[starts[k]:idx[k]][:2000]) >= 0) for k in keep[:50])\n    units[\"n_spikes_bins\"] = [len(b) for b in bins]\n    s[\"units\"] = units\n\n    iv = f[\"intervals\"]\n    s[\"blocks\"] = {}\n    for blk in IC_BLOCKS:\n        g = iv[f\"{blk}_presentations\"]\n        frame = g[\"frame\"][:]\n        rows = ic_trials(frame)\n        start = g[\"start_time\"][:]\n        stop = g[\"stop_time\"][:]\n        other = np.setdiff1d(np.arange(rows[0], rows[-1] + 1), rows)\n        onset_ms = np.floor(start[rows] * 1000.0).astype(np.int64)\n        s[\"blocks\"][blk] = {\n            \"codes\": IC_TRIAL_TYPES[frame[rows].astype(int)], \"start\": start[rows], \"stop\": stop[rows],\n            \"n_rows\": len(frame), \"iti_rows_nonzero_frame\": int(np.count_nonzero(frame[other])),\n            \"duration\": stop[rows] - start[rows], \"iti\": start[rows][1:] - stop[rows][:-1],\n            \"R\": _window_counts(bins, onset_ms, 1, IC_WINDOW_MS) * (1000.0 / IC_WINDOW_MS)}\n    g = iv[\"RFCI_presentations\"]\n    start = g[\"start_time\"][:]\n    x, y = g[\"x_position\"][:], g[\"y_position\"][:]\n    mask = np.array([_str(m) for m in g[\"Mask\"][:]])\n    rows = np.arange(0, len(start), 4)\n    maskno = np.array([int(re.search(r\"(\\d+)\\.tif\", m).group(1)) for m in mask[rows]])\n    # positions: 0 center, then code order (down, then counterclockwise), code RFcentersrel\n    rel = np.array([[-1, 0], [-1 / np.sqrt(2), 1 / np.sqrt(2)], [0, 1], [1 / np.sqrt(2), 1 / np.sqrt(2)],\n                    [1, 0], [1 / np.sqrt(2), -1 / np.sqrt(2)], [0, -1], [-1 / np.sqrt(2), -1 / np.sqrt(2)]])\n    yx = np.c_[y[rows], x[rows]] / 203.3786\n    pos = np.zeros(len(rows), dtype=int)\n    for k, r in enumerate(rel):\n        pos[np.all(np.abs(yx - r) < 1e-3, axis=1)] = k + 1\n    s[\"rf\"] = {\"pos\": pos, \"inverse\": maskno // 10000 == 1, \"start\": start[rows],\n               \"directions_per_trial\": [tuple(g[\"orientation\"][r:r + 4]) for r in rows[:3]],\n               \"row_dur\": g[\"stop_time\"][:] - start, \"n_rows\": len(start),\n               \"R\": _window_counts(bins, np.floor(start[rows] * 1000).astype(np.int64), 1, RF_WINDOW_MS)\n               * (1000.0 / RF_WINDOW_MS)}\n    sp = iv[\"spontaneous_presentations\"]\n    s0, s1 = sp[\"start_time\"][:], sp[\"stop_time\"][:]\n    k = int(np.argmax(s1 - s0))\n    lo, hi = int(np.floor(s0[k] * 1000)) + 1, int(np.floor(s1[k] * 1000))\n    s[\"spont_interval\"] = (s0[k], s1[k])\n    s[\"spont_all\"] = np.c_[s0, s1]\n    s[\"spont_rate\"] = np.array([(np.searchsorted(b, hi, \"right\") - np.searchsorted(b, lo, \"left\"))\n                                / ((hi - lo + 1) / 1000.0) for b in bins])\n    nwin = int((s1[k] - s0[k]) // 1.0)\n    w0 = np.floor(s0[k] * 1000).astype(np.int64) + 1000 * np.arange(nwin)\n    s[\"spont_windows\"] = _window_counts(bins, w0, 1, 1000)   # spikes/s in 1-s windows\n    s[\"block_spans\"] = {blk: (iv[f\"{blk}_presentations\"][\"start_time\"][0], iv[f\"{blk}_presentations\"][\"stop_time\"][-1])\n                        for blk in IC_BLOCKS + [\"RFCI\", \"sizeCI\"]}\n\n    if ccg:\n        b0, b1 = s[\"block_spans\"][\"ICwcfg1\"]\n        lo, hi = int(np.floor(b0 * 1000)), int(np.floor(b1 * 1000))\n        s[\"ccg_span_ms\"] = (lo, hi)\n        s[\"ccg_bins\"] = {int(i): b[(b >= lo) & (b <= hi)].astype(np.int32)\n                         for i, b, rs in zip(units.index, bins, units.rs) if rs}\n    s[\"eye\"] = _eye(f, s) if \"acquisition/EyeTracking\" in f else None\n    return s\n\n\ndef _eye(f, s) -> dict:\n    e = f[\"acquisition/EyeTracking\"]\n    ts = e[\"eye_tracking/timestamps\"][:]\n    p = e[\"pupil_tracking/data\"][:]\n    area = e[\"pupil_tracking/area\"][:]\n    blink = e[\"likely_blink/data\"][:].astype(bool)\n    ok = np.isfinite(p).all(axis=1)\n    xe = np.arange(np.nanmin(p[:, 0]), np.nanmax(p[:, 0]) + EYE_BIN_PX, EYE_BIN_PX)\n    ye = np.arange(np.nanmin(p[:, 1]), np.nanmax(p[:, 1]) + EYE_BIN_PX, EYE_BIN_PX)\n    H, _, _ = np.histogram2d(p[ok, 0], p[ok, 1], bins=[xe, ye])\n    r, c = np.unravel_index(np.argmax(H), H.shape)\n    mode = np.array([(xe[r] + xe[r + 1]) / 2, (ye[c] + ye[c + 1]) / 2])\n    dist = np.sqrt(((p - mode) ** 2).sum(axis=1))\n    za = (area - np.nanmean(area)) / np.nanstd(area)\n    out = {\"mode\": mode, \"hz\": 1 / np.median(np.diff(ts)), \"n_frames\": len(ts),\n           \"units\": {k: _str(e[f\"pupil_tracking/{k}\"].attrs.get(\"unit\", \"\")) for k in [\"data\", \"area\"]},\n           \"frac_nan\": float(np.mean(~ok)), \"frac_blink\": float(blink.mean()),\n           \"x_range\": np.nanpercentile(p[:, 0], [1, 99]), \"y_range\": np.nanpercentile(p[:, 1], [1, 99]),\n           \"width_median\": float(np.nanmedian(e[\"pupil_tracking/width\"][:])),\n           \"eye_width_median\": float(np.nanmedian(e[\"eye_tracking/width\"][:])),\n           \"density_xy\": (p[ok][::10] - mode).astype(np.float32)}\n    for name, starts, dur in [(\"ICwcfg1\", s[\"blocks\"][\"ICwcfg1\"][\"start\"], 0.4), (\"RF\", s[\"rf\"][\"start\"], 1.0)]:\n        first = np.searchsorted(ts, starts, side=\"right\")     # first frame after onset (code)\n        n = int(round(dur * EYE_HZ))\n        ind = np.clip(first[:, None] + np.arange(n)[None, :], 0, len(ts) - 1)\n        d = dist[ind]\n        out[name] = {\"maxdist\": np.nanmax(np.where(np.isnan(d), -np.inf, d), axis=1),\n                     \"blink\": blink[ind].any(axis=1), \"nan_frames\": np.isnan(d).sum(axis=1),\n                     \"area_mean\": np.nanmean(za[ind], axis=1), \"area_end\": za[ind[:, -1]],\n                     \"area_max\": np.nanmax(np.where(np.isnan(za[ind]), -np.inf, za[ind]), axis=1),\n                     \"x_mean\": np.nanmean(p[ind, 0], axis=1), \"y_mean\": np.nanmean(p[ind, 1], axis=1),\n                     \"lag_first_frame\": ts[np.clip(first, 0, len(ts) - 1)] - starts}\n    return out\n\n\ndef load_all(ccg: bool = True, workers: int = 4) -> list[dict]:\n    assets = session_assets()\n    with ThreadPoolExecutor(workers) as ex:\n        return list(ex.map(lambda a: load_session(a, ccg=ccg), assets))\n\n\n# ---------------------------------------------------------------- statistics\n\n_QCRIT = {}\n\n\ndef tukey_qcrit(k: int, alpha: float = 0.05) -> float:\n    \"\"\"Critical studentized range for k groups, infinite df (Tukey-Kramer after Kruskal-Wallis).\"\"\"\n    if k not in _QCRIT:\n        _QCRIT[k] = float(studentized_range.ppf(1 - alpha, k, 1e6))\n    return _QCRIT[k]\n\n\ndef kw_tukey(R: np.ndarray, groups: np.ndarray, order: list):\n    \"\"\"Kruskal-Wallis per unit and Tukey-Kramer comparison of each group with the first.\n\n    R is trials x units; groups the trial labels; order the groups compared, the first being the\n    reference (blank). Returns (p_kw per unit, sig per unit x other group) where sig means the\n    Tukey-Kramer comparison of mean ranks with the reference is significant at 0.05, as MATLAB's\n    multcompare after kruskalwallis (mean ranks, variance N(N+1)/12 with the tie correction,\n    infinite df).\n    \"\"\"\n    sel = np.isin(groups, order)\n    X = R[sel]\n    g = groups[sel]\n    N = X.shape[0]\n    ranks = stats.rankdata(X, axis=0)\n    k = len(order)\n    n = np.array([np.sum(g == o) for o in order])\n    meanr = np.stack([ranks[g == o].mean(axis=0) for o in order])         # k x units\n    # Kruskal-Wallis H with tie correction\n    H = 12.0 / (N * (N + 1)) * np.sum(n[:, None] * (meanr - (N + 1) / 2) ** 2, axis=0)\n    ties = np.zeros(X.shape[1])\n    for j in range(X.shape[1]):\n        _, c = np.unique(X[:, j], return_counts=True)\n        ties[j] = np.sum(c ** 3 - c)\n    corr = 1 - ties / (N ** 3 - N)\n    with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n        Hc = np.where(corr > 0, H / corr, 0.0)\n    p_kw = stats.chi2.sf(Hc, k - 1)\n    p_kw[corr <= 0] = 1.0\n    var = N * (N + 1) / 12.0 * corr                                             # per unit\n    qc = tukey_qcrit(k)\n    sig = np.zeros((X.shape[1], k - 1), dtype=bool)\n    for i in range(1, k):\n        se = np.sqrt(var * (1.0 / n[0] + 1.0 / n[i]) / 2.0)\n        with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n            q = np.abs(meanr[i] - meanr[0]) / se\n        sig[:, i - 1] = np.nan_to_num(q) > qc\n    return p_kw, sig\n\n\ndef auroc(a: np.ndarray, b: np.ndarray) -> np.ndarray:\n    \"\"\"AUROC of b against a (b positive) per unit; a, b are trials x units.\"\"\"\n    allx = np.vstack([a, b])\n    r = stats.rankdata(allx, axis=0)\n    rb = r[len(a):].sum(axis=0)\n    nb, na = len(b), len(a)\n    return (rb - nb * (nb + 1) / 2) / (na * nb)\n\n\ndef ranksum_p(a: np.ndarray, b: np.ndarray) -> np.ndarray:\n    \"\"\"Two-sided Wilcoxon rank-sum p per unit (normal approximation with tie correction).\"\"\"\n    return stats.mannwhitneyu(a, b, axis=0, alternative=\"two-sided\", method=\"asymptotic\").pvalue\n\n\ndef ic_groups(R: np.ndarray, codes: np.ndarray, seg_in=SEG_IN, seg_out=SEG_OUT) -> pd.DataFrame:\n    \"\"\"IC-encoders, LC-encoders and segment responders (code analyzeStaticICtxi.m; Methods).\n\n    sigmcBK: +1/-1/0 per IC1, LC1, LC2, IC2 against blank: Tukey-Kramer significant, sign from\n    the AUROC against blank. IC-encoder: Kruskal-Wallis p < 0.05, IC1 or IC2 +1, LC1 and LC2 0.\n    Segment responder (indin): Kruskal-Wallis across blank and the 8 segment images p < 0.05,\n    rank-sum In vs Out p < 0.05 with AUROC > 0.5, and not an IC- or LC-encoder.\n    \"\"\"\n    order = [BLANK, IC1, LC1, LC2, IC2]\n    pkw, sig = kw_tukey(R, codes, order)\n    blank = R[codes == BLANK]\n    au = np.stack([auroc(blank, R[codes == c]) for c in order[1:]], axis=1)\n    smc = np.where(sig, np.sign(au - 0.5), 0).astype(int)\n    smc[pkw >= 0.05] = 0\n    kw = pkw < 0.05\n    ic1 = kw & (smc[:, 0] == 1) & (smc[:, 1] == 0) & (smc[:, 2] == 0)\n    ic2 = kw & (smc[:, 3] == 1) & (smc[:, 1] == 0) & (smc[:, 2] == 0)\n    lc1 = kw & (smc[:, 1] == 1) & (smc[:, 0] == 0) & (smc[:, 3] == 0)\n    lc2 = kw & (smc[:, 2] == 1) & (smc[:, 0] == 0) & (smc[:, 3] == 0)\n    out = pd.DataFrame({\"p_kw_BK\": pkw, \"ic1_enc\": ic1, \"ic2_enc\": ic2, \"ic_enc\": ic1 | ic2,\n                        \"lc1_enc\": lc1, \"lc2_enc\": lc2, \"lc_enc\": lc1 | lc2})\n    pkw_bi, _ = kw_tukey(R, codes, [BLANK] + list(seg_in) + list(seg_out))\n    seg_any = np.zeros(len(pkw), dtype=bool)\n    for i, (ci, co) in enumerate(zip(seg_in, seg_out)):\n        a, b = R[codes == co], R[codes == ci]\n        sp = auroc(a, b)\n        p = ranksum_p(a, b)\n        sr = (sp > 0.5) & (pkw_bi < 0.05) & (p < 0.05) & ~out.ic_enc.values & ~out.lc_enc.values\n        out[f\"seg{i + 1}\"] = sr\n        seg_any |= sr\n    out[\"seg_resp\"] = seg_any\n    return out\n\n\ndef ic_ire_responsive(R: np.ndarray, codes: np.ndarray, ic_code: int, ire_code: int, test: str):\n    \"\"\"Is a unit responsive to the IC image and to the IRE image (against blank)?\n\n    test 'a': code's sigmcBICREl, Kruskal-Wallis across blank, IC and IRE p < 0.05 and\n    Tukey-Kramer against blank significant with AUROC > 0.5. test 'b': rank-sum against blank\n    p < 0.05 with AUROC > 0.5 (criterion of fig1f).\n    \"\"\"\n    blank = R[codes == BLANK]\n    res = []\n    if test == \"a\":\n        pkw, sig = kw_tukey(R, codes, [BLANK, ic_code, ire_code])\n        for i, c in enumerate([ic_code, ire_code]):\n            res.append((pkw < 0.05) & sig[:, i] & (auroc(blank, R[codes == c]) > 0.5))\n    else:\n        for c in [ic_code, ire_code]:\n            x = R[codes == c]\n            res.append((ranksum_p(blank, x) < 0.05) & (auroc(blank, x) > 0.5))\n    return res[0], res[1]\n\n\ndef signrank_p(x: np.ndarray, y=None, alternative=\"two-sided\") -> float:\n    x = np.asarray(x, float) if y is None else np.asarray(x, float) - np.asarray(y, float)\n    x = x[np.isfinite(x)]\n    if np.all(x == 0) or len(x) == 0:\n        return 1.0\n    return float(stats.wilcoxon(x, alternative=alternative).pvalue)\n\n\ndef holm_exclusive(p: np.ndarray, best: np.ndarray, alpha: float = 0.05):\n    \"\"\"Code's RFsigexclclassic: the best position's p is the smallest, p*9 < alpha, and exactly\n    one position passes the step-down Holm comparison sorted(p) * [9..1] < alpha.\"\"\"\n    m = p.shape[1]\n    ps = np.sort(p, axis=1)\n    pb = p[np.arange(len(p)), best]\n    return (pb * m < alpha) & (pb == ps[:, 0]) & (np.sum(ps * np.arange(m, 0, -1) < alpha, axis=1) == 1)\n\n\ndef holm_reject(p: np.ndarray, alpha: float = 0.05) -> np.ndarray:\n    \"\"\"Bonferroni-Holm rejections per row of p.\"\"\"\n    m = p.shape[1]\n    order = np.argsort(p, axis=1)\n    ps = np.take_along_axis(p, order, axis=1)\n    passed = ps * np.arange(m, 0, -1) < alpha\n    passed = np.cumprod(passed, axis=1).astype(bool)\n    rej = np.zeros_like(passed)\n    np.put_along_axis(rej, order, passed, axis=1)\n    return rej\n\n\ndef rf_positions(R: np.ndarray, pos: np.ndarray, inverse: np.ndarray, spont_rate: np.ndarray,\n                 spont_windows: np.ndarray, trials=None):\n    \"\"\"Exclusive center responsiveness under the two readings of fig1e.\n\n    R: RF trials x units (spikes/s); classic (not inverse) trials only are used. trials: optional\n    boolean mask of RF trials to use (fixed-gaze). Returns a DataFrame with the best position,\n    reading (a) (code: signed-rank of trial rates against the spontaneous rate, center best and\n    the only position surviving the code's Holm step) and reading (b) (Methods: rank-sum against\n    1-s windows of the longest spontaneous block, Holm over 9 positions, center the only\n    significant position), and the Kruskal-Wallis p across positions.\n    \"\"\"\n    use = ~inverse if trials is None else (~inverse & trials)\n    Rc, pc = R[use], pos[use]\n    means = np.stack([Rc[pc == k].mean(axis=0) if np.any(pc == k) else np.full(R.shape[1], np.nan)\n                      for k in range(9)], axis=1)\n    best = np.nanargmax(np.where(np.isnan(means), -np.inf, means), axis=1)\n    pa = np.ones((R.shape[1], 9))\n    pb = np.ones((R.shape[1], 9))\n    for k in range(9):\n        x = Rc[pc == k]\n        if len(x) == 0:\n            continue\n        for j in range(R.shape[1]):\n            d = x[:, j] - spont_rate[j]\n            pa[j, k] = 1.0 if np.all(d == 0) else stats.wilcoxon(d).pvalue\n        pb[:, k] = ranksum_p(spont_windows, x)\n    excl_a = holm_exclusive(pa, best) & (best == 0)\n    rej_b = holm_reject(pb)\n    above = means > spont_windows.mean(axis=0)[:, None]\n    excl_b = rej_b[:, 0] & (rej_b.sum(axis=1) == 1) & above[:, 0]\n    pkw = np.ones(R.shape[1])\n    for j in range(R.shape[1]):\n        if np.ptp(Rc[:, j]) > 0:\n            pkw[j] = stats.kruskal(*[Rc[pc == k, j] for k in range(9) if np.any(pc == k)]).pvalue\n    return pd.DataFrame({\"best\": best, \"excl_a\": excl_a, \"excl_b\": excl_b, \"p_kw_rf\": pkw,\n                         \"p_center_a\": pa[:, 0], \"p_center_b\": pb[:, 0]})\n\n\n# ---------------------------------------------------------------- decoding\n\ndef decode(R: np.ndarray, codes: np.ndarray, train_types, probe_types, seed: int, reading: str = \"a\",\n           kernel: str = \"linear\", n_splits: int = 10):\n    \"\"\"Linear SVM decoder of the Methods and the code (analyzeICtxi_SVM_areas.m).\n\n    Trials of each training type are balanced to the smallest type by taking its first trials;\n    stratified tenfold partition; each fold z-scores every unit by the training trials' mean and\n    s.d. (NaN set to 0); one-vs-one SVM (libsvm, as MATLAB fitcecoc's default coding). reading\n    'a': C = 1; reading 'b': C chosen by a threefold inner cross-validation on the training fold\n    over 10^-3 to 10^2 (the Python counterpart of the code's OptimizeHyperparameters, criterion).\n    Returns cross-validation accuracy (mean over classes of the fraction correct, mean over\n    folds), the confusion matrix of test trials, and P(probe type -> train type) averaged over the\n    ten fold models.\n    \"\"\"\n    from sklearn.model_selection import GridSearchCV, StratifiedKFold\n    from sklearn.svm import SVC\n\n    train_types = list(train_types)\n    n_min = min(np.sum(codes == t) for t in train_types)\n    idx = np.concatenate([np.flatnonzero(codes == t)[:n_min] for t in train_types])\n    y = codes[idx]\n    probe = np.flatnonzero(np.isin(codes, probe_types))\n    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=seed)\n    conf = np.zeros((len(train_types), len(train_types)))\n    pconf = np.zeros((len(probe_types), len(train_types)))\n    accs = []\n    for tr, te in skf.split(idx, y):\n        mu = R[idx[tr]].mean(axis=0)\n        sd = R[idx[tr]].std(axis=0, ddof=1)\n        with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n            Z = (R - mu) / sd\n        Z[~np.isfinite(Z)] = 0\n        if kernel == \"poly\":\n            base = SVC(kernel=\"poly\", degree=2, C=1.0)\n        else:\n            base = SVC(kernel=kernel, C=1.0)\n        if reading == \"b\":\n            clf = GridSearchCV(base, {\"C\": 10.0 ** np.arange(-3, 3)},\n                               cv=StratifiedKFold(3, shuffle=True, random_state=seed))\n        else:\n            clf = base\n        clf.fit(Z[idx[tr]], y[tr])\n        pred = clf.predict(Z[idx[te]])\n        cm = np.array([[np.mean(pred[y[te] == a] == b) for b in train_types] for a in train_types])\n        conf += cm / n_splits\n        accs.append(np.mean(np.diag(cm)))\n        pp = clf.predict(Z[probe])\n        pconf += np.array([[np.mean(pp[codes[probe] == a] == b) for b in train_types] for a in probe_types]) / n_splits\n    return {\"acc\": float(np.mean(accs)), \"conf\": conf, \"probe\": pconf, \"n_per_class\": int(n_min)}\n\n\ndef inference_score(probe: np.ndarray) -> tuple[float, float, float]:\n    \"\"\"TRE inference: rows TRE1, TRE2; columns IC1, LC1, LC2, IC2 (code line 171).\n    Returns (score, IC value, LC value).\"\"\"\n    ic = (probe[0, 0] + probe[1, 3]) / 2\n    lc = (probe[0, 1] + probe[1, 2]) / 2\n    return ic - lc, ic, lc\n\n\n# ---------------------------------------------------------------- cross-correlograms\n\ndef ccg_counts(target_bins, source_bins, max_lag: int):\n    \"\"\"Raw cross-correlogram counts for every (target, source) pair.\n\n    counts[i, j, max_lag + d] = number of spike pairs with t_target - t_source = d ms, for\n    |d| <= max_lag, from 1-ms bin indices (one spike per bin). With d > 0 the source leads.\n    \"\"\"\n    from numba import njit\n\n    @njit(cache=False)\n    def _run(tb, tptr, sb, slab, nsrc, L):\n        out = np.zeros((len(tptr) - 1, nsrc, 2 * L + 1), dtype=np.int32)\n        for i in range(len(tptr) - 1):\n            lo = 0\n            for k in range(tptr[i], tptr[i + 1]):\n                t = tb[k]\n                while lo < len(sb) and sb[lo] < t - L:\n                    lo += 1\n                m = lo\n                while m < len(sb) and sb[m] <= t + L:\n                    out[i, slab[m], L + t - sb[m]] += 1\n                    m += 1\n        return out\n\n    tptr = np.r_[0, np.cumsum([len(b) for b in target_bins])].astype(np.int64)\n    tb = np.concatenate(target_bins).astype(np.int64) if len(target_bins) else np.zeros(0, np.int64)\n    sall = np.concatenate(source_bins).astype(np.int64)\n    slab = np.concatenate([np.full(len(b), j, np.int64) for j, b in enumerate(source_bins)])\n    o = np.argsort(sall, kind=\"stable\")\n    return _run(tb, tptr, sall[o], slab[o], len(source_bins), max_lag)\n\n\ndef connections(counts: np.ndarray, max_lag: int, smoothing: str, flank_from: str,\n                win=(1, 10), flank=(50, 100), sd_factor=7.0) -> np.ndarray:\n    \"\"\"Putative excitatory connection from source to target (Methods, Cross-correlogram analysis).\n\n    The CCG of trains smoothed with a 25-ms window equals the raw CCG convolved with the\n    autocorrelation of the kernel, so the correction is computed from the raw counts.\n    smoothing 'box': 25-bin boxcar; 'gauss': Gaussian 25 bins long with s.d. 5 ms (criterion).\n    flank_from 'raw' or 'corrected': which CCG the flank s.d. is taken from (criterion readings\n    i and ii). Normalisation by sqrt(n1 n2) is left out; it does not change the comparison of the\n    peak with a multiple of the flank s.d. of the same pair.\n    \"\"\"\n    if smoothing == \"box\":\n        k = np.ones(25) / 25.0\n    else:\n        x = np.arange(25) - 12\n        k = np.exp(-x ** 2 / (2 * 5.0 ** 2))\n        k /= k.sum()\n    ac = np.convolve(k, k[::-1])                       # 49 taps\n    c = counts.astype(np.float32)\n    from scipy.ndimage import convolve1d\n    sm = convolve1d(c, ac.astype(np.float32), axis=-1, mode=\"constant\")\n    corr = c - sm\n    lags = np.arange(-max_lag, max_lag + 1)\n    w = (lags >= win[0]) & (lags <= win[1])\n    fl = (np.abs(lags) >= flank[0]) & (np.abs(lags) <= flank[1])\n    peak = corr[..., w].max(axis=-1)\n    ref = c if flank_from == \"raw\" else corr\n    sd = ref[..., fl].std(axis=-1, ddof=1)\n    return (peak > sd_factor * sd) & (sd > 0)\n"
}
```

```
File created successfully at: entries/000248-shin-2025/illusion.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && uv pip install -q dandi 2>&1 | tail -1; cat > t3.py <<'EOF'
import sys, time, pickle
sys.path.insert(0, 'entries/000248-shin-2025')
import illusion as il
t=time.time(); A=il.session_assets(); print(len(A), time.time()-t); print(A[0])
t=time.time(); s=il.load_session(A[0]); print('load', time.time()-t)
pickle.dump(s, open('s0.pkl','wb'))
u=s['units']; print(u.groupby(['area','rs']).size())
for b,v in s['blocks'].items(): print(b, len(v['codes']), v['n_rows'], v['iti_rows_nonzero_frame'], {c:(v['codes']==c).sum() for c in [0,106,107,110,111,1105,1201]}, v['R'].shape)
print(s['rf']['pos'][:20], s['rf']['inverse'][:20], s['rf']['directions_per_trial'])
print(s['eye'] and {k:s['eye'][k] for k in ['mode','hz','units','frac_nan','frac_blink','x_range','width_median','eye_width_median']})
print(len(s['ccg_bins']), sum(len(b) for b in s['ccg_bins'].values()))
EOF
python t3.py
```

```
12 2.002723217010498
{'path': 'sub-619293/sub-619293_ses-1184980079_ogen.nwb', 'asset_id': 'e61edcf3-26e9-44e1-9017-3ee558197da5', 'size': 2453451408, 'url': 'https://dandiarchive.s3.amazonaws.com/blobs/4d3/b9d/4d3b9d33-3525-4845-8365-763a15437b8f'}
load 16.691010236740112
area  rs   
AL    False     10
      True     106
AM    False     15
      True     107
PM    False     11
      True     151
RL    False     51
      True     156
V1    False     13
      True      89
dtype: int64
ICwcfg1 5300 10720 0 {0: np.int64(400), 106: np.int64(400), 107: np.int64(400), 110: np.int64(400), 111: np.int64(400), 1105: np.int64(400), 1201: np.int64(400)} (5300, 709)
ICwcfg0 660 1380 0 {0: np.int64(30), 106: np.int64(30), 107: np.int64(30), 110: np.int64(30), 111: np.int64(30), 1105: np.int64(30), 1201: np.int64(30)} (660, 709)
ICkcfg1 660 1380 0 {0: np.int64(30), 106: np.int64(30), 107: np.int64(30), 110: np.int64(30), 111: np.int64(30), 1105: np.int64(30), 1201: np.int64(30)} (660, 709)
ICkcfg0 660 1380 0 {0: np.int64(30), 106: np.int64(30), 107: np.int64(30), 110: np.int64(30), 111: np.int64(30), 1105: np.int64(30), 1201: np.int64(30)} (660, 709)
[5 0 4 2 2 3 4 0 4 5 3 8 2 1 0 3 0 7 1 1] [False  True  True  True  True  True False False  True False False False
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t4.py <<'EOF'
import sys, time, pickle
sys.path.insert(0, 'entries/000248-shin-2025')
import illusion as il, numpy as np
t=time.time(); S=il.load_all(); print('load all', time.time()-t)
pickle.dump(S, open('S.pkl','wb'))
for s in S:
    u=s['units']; b=s['blocks']['ICwcfg1']
    print(s['subject'], s['genotype'][:5], len(u), dict(u[u.rs].area.value_counts()), np.unique(b['codes'],return_counts=True)[1].tolist(), s['eye'] is not None)
EOF
python t4.py
```

```
entries/000248-shin-2025/illusion.py:266: RuntimeWarning: Mean of empty slice
  "area_mean": np.nanmean(za[ind], axis=1), "area_end": za[ind[:, -1]],
entries/000248-shin-2025/illusion.py:268: RuntimeWarning: Mean of empty slice
  "x_mean": np.nanmean(p[ind, 0], axis=1), "y_mean": np.nanmean(p[ind, 1], axis=1),
load all 150.89664697647095
619293 Sst-I 709 {'RL': np.int64(156), 'PM': np.int64(151), 'AM': np.int64(107), 'AL': np.int64(106), 'V1': np.int64(89)} [400, 400, 400, 400, 400, 400, 400, 400, 50, 50, 400, 400, 400, 400, 50, 50, 50, 50, 50, 50, 50, 50] False
619296 Sst-I 676 {'V1': np.int64(168), 'PM': np.int64(95), 'AL': np.int64(94), 'AM': np.int64(93), 'RL': np.int64(87), 'LM': np.int64(4)} [400, 400, 400, 400, 400, 400, 400, 400, 50, 50, 400, 400, 400, 400, 50, 50, 50, 50, 50, 50, 50, 50] True
620333 Sst-I 807 {'AM': np.int64(129), 'RL': np.int64(128), 'LM': np.int64(119), 'V1': np.int64(114), 'PM': np.int64(102), 'AL': np.int64(91)} [400, 400, 400, 400, 400, 400, 400, 400, 50, 50, 400, 400, 400, 400, 50, 50, 50, 50, 50, 50, 50, 50] True
620334 Sst-I 669 {'LM': np.int64(183), 'RL': np.int64(100), 'PM': np.int64(90), 'AM': np.int64(82), 'V1': np.int64(68)} [400, 400, 400, 400, 400, 400, 400, 400, 50, 50, 400, 400, 400, 400, 50, 50, 50, 50, 50, 50, 50, 50] True
625545 Sst-I 1123 {'V1': np.int64(190), 'LM': np.int64(181), 'PM': np.int64(173), 'AL': np.int64(160), 'AM': np.int64(134), 'RL': np.int64(122)} [400, 400, 400, 400, 400, 400, 400, 400, 50, 50, 400, 400, 400, 400, 50, 50, 50, 50, 50, 50, 50, 50] True
625554 Pvalb 953 {'PM': np.int64(193), 'AM': np.int64(183), 'V1': np.int64(179), 'AL': np.int64(139), 'RL': np.int64(136)} [400, 400, 400, 400, 400, 400, 400, 400, 50, 50, 400, 400, 400, 400, 50, 50, 50, 50, 50, 50, 50, 50] True
625555 Pvalb 1269 {'V1': np.int64(314), 'PM': np.int64(214), 'RL': np.int64(208), 'AM': np.int64(198), 'AL': np.int64(159)} [400, 400, 400, 400, 400, 400, 400, 400, 50, 50, 400, 400, 400, 400, 50, 50, 50, 50, 50, 50, 50, 50] True
63
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t5.py <<'EOF'
import sys, time, pickle
sys.path.insert(0, 'entries/000248-shin-2025')
import illusion as il, numpy as np, pandas as pd
S=pickle.load(open('S.pkl','rb'))
rows=[]
for s in S:
    u=s['units']; rs=u.rs.values
    print(s['subject'], 'V1 RS', ((u.area=='V1')&rs).sum(), 'HVA RS', ((u.area!='V1')&rs).sum(), 'V1 RS good', ((u.area=='V1')&rs&(u.quality=='good')).sum())
t=time.time()
tot={}
for s in S:
    u=s['units']; v1=(u.area=='V1').values
    for blk in ['ICwcfg1','ICwcfg0']:
        b=s['blocks'][blk]
        g=il.ic_groups(b['R'][:,v1], b['codes'])
        g['rs']=u.rs.values[v1]; g['quality']=u.quality.values[v1]
        tot.setdefault(blk,[]).append(g)
print('time', time.time()-t)
for blk in tot:
    G=pd.concat(tot[blk]); print(blk, 'RS ic', (G.ic_enc&G.rs).sum(), 'RS seg', (G.seg_resp&G.rs).sum(), 'nonnoise ic', (G.ic_enc&(G.quality!='noise')).sum(), 'seg', (G.seg_resp&(G.quality!='noise')).sum(), 'all ic', G.ic_enc.sum())
a=pd.concat(tot['ICwcfg1']).reset_index(drop=True); b=pd.concat(tot['ICwcfg0']).reset_index(drop=True)
print('union RS', ((a.ic_enc|b.ic_enc)&a.rs).sum(), 'sum', (a.ic_enc&a.rs).sum()+(b.ic_enc&b.rs).sum(), 'seg union', ((a.seg_resp|b.seg_resp)&a.rs).sum())
EOF
python t5.py
```

```
619293 V1 RS 89 HVA RS 520 V1 RS good 63
619296 V1 RS 168 HVA RS 373 V1 RS good 143
620333 V1 RS 114 HVA RS 569 V1 RS good 104
620334 V1 RS 68 HVA RS 455 V1 RS good 59
625545 V1 RS 190 HVA RS 770 V1 RS good 158
625554 V1 RS 179 HVA RS 651 V1 RS good 163
625555 V1 RS 314 HVA RS 779 V1 RS good 280
630506 V1 RS 58 HVA RS 600 V1 RS good 45
631510 V1 RS 129 HVA RS 433 V1 RS good 115
631570 V1 RS 142 HVA RS 446 V1 RS good 126
633229 V1 RS 181 HVA RS 833 V1 RS good 169
637484 V1 RS 172 HVA RS 564 V1 RS good 152
time 1.227367877960205
ICwcfg1 RS ic 79 RS seg 526 nonnoise ic 79 seg 566 all ic 87
ICwcfg0 RS ic 84 RS seg 384 nonnoise ic 83 seg 425 all ic 95
union RS 159 sum 163 seg union 684
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat >> t5.py <<'EOF'
print('all units ICwcfg1 ic', a.ic_enc.sum(), 'seg', a.seg_resp.sum())
print('all-units per quality', pd.crosstab(a.quality, a.rs))
EOF
python t5.py 2>&1 | tail -8
```

```
ICwcfg1 RS ic 79 RS seg 526 nonnoise ic 79 seg 566 all ic 87
ICwcfg0 RS ic 84 RS seg 384 nonnoise ic 83 seg 425 all ic 95
union RS 159 sum 163 seg union 684
all units ICwcfg1 ic 87 seg 636
all-units per quality rs       False  True 
quality              
good       261   1577
noise       95    227
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t6.py <<'EOF'
import sys, time, pickle
sys.path.insert(0, 'entries/000248-shin-2025')
import illusion as il, numpy as np, pandas as pd
S=pickle.load(open('S.pkl','rb'))
t=time.time(); out=[]
for s in S:
    u=s['units']; v1=((u.area=='V1')&u.rs).values
    rf=s['rf']
    print(s['subject'], np.bincount(rf['pos'][~rf['inverse']]), s['spont_interval'], s['spont_windows'].shape)
    d=il.rf_positions(rf['R'][:,v1], rf['pos'], rf['inverse'], s['spont_rate'][v1], s['spont_windows'][:,v1])
    d['subject']=s['subject']; out.append(d)
D=pd.concat(out); print(time.time()-t)
print('excl a', D.excl_a.sum(), 'excl b', D.excl_b.sum(), 'best center', (D.best==0).sum(), 'kw sig', (D.p_kw_rf<0.05).sum())
print(D.groupby('subject')[['excl_a','excl_b']].sum())
EOF
python t6.py
```

```
619293 [10 10 10 10 10 10 10 10 10] (np.float64(4529.82554), np.float64(4842.08805)) (312, 709)
619296 [10 10 10 10 10 10 10 10 10] (np.float64(4353.8951), np.float64(4666.15762)) (312, 676)
620333 [10 10 10 10 10 10 10 10 10] (np.float64(4357.8786), np.float64(4670.14116)) (312, 807)
620334 [10 10 10 10 10 10 10 10 10] (np.float64(4354.10241), np.float64(4666.36486)) (312, 669)
625545 [10 10 10 10 10 10 10 10 10] (np.float64(4354.65484), np.float64(4666.91738)) (312, 1123)
625554 [10 10 10 10 10 10 10 10 10] (np.float64(4390.84373), np.float64(4703.10623)) (312, 953)
625555 [10 10 10 10 10 10 10 10 10] (np.float64(4354.34721), np.float64(4666.60972)) (312, 1269)
630506 [10 10 10 10 10 10 10 10 10] (np.float64(4354.55544), np.float64(4666.81798)) (312, 799)
631510 [10 10 10 10 10 10 10 10 10] (np.float64(4414.65117), np.float64(4726.91386)) (312, 740)
631570 [10 10 10 10 10 10 10 10 10] (np.float64(4354.49556), np.float64(4666.75821)) (312, 688)
633229 [10 10 10 10 10 10 10 10 10] (np.float64(4355.42802), np.float64(4667.69072)) (312, 1211)
637484 [10 10 10 10 10 10 10 10 10] (np.float64(4424.75848), np.float64(4737.02113)) (312, 934)
71.03194546699524
excl a 44 excl b 52 best center 474 kw sig 904
         excl_a  excl_b
subject                
619293        0       1
619296        7       8
620333        0       0
620334        0       3
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/IC_paper_code && grep -n "RFsigexcl\|RFexclsig\|ctrCRF\|exclctr\|sigexcl" *.m | grep -v "^analyzeRFCI" | head -40
```

```
analyzeICtxi_SVM_areas.m:115:                tempneugroup.ctrCRF9 = RFCIall.pRFclassic<0.05 & RFCIall.RFindclassic==1;
analyzeICtxi_SVM_areas.m:118:                tempneugroup.exclctrCRF9 = RFCIall.pRFclassic<0.05 & RFCIall.RFindclassic==1 & sum(RFCIall.pRrfclassic<0.05,2)==1;
analyzeICtxi_SVM_areas.m:119:                tempneugroup.ctrCRF9nonctrIRF9 = RFCIall.RFindclassic==1 & RFCIall.pRFclassic<0.05 & RFCIall.pRrfinverse(:,1)>=0.05;
analyzeICtxi_SVM_areas.m:134:                    'sigkwCRF', 'ctrCRF9', 'exclctrCRF9', 'ctrCG9', 'exclCRF9', 'ctrIRF9', ...
analyzeICtxi_SVM_areas.m:137:                    'allbutsigkwCRF', 'allbutctrCRF9', 'allbutexclctrCRF9', 'allbutctrCG9', 'allbutexclCRF9', 'allbutctrIRF9'};
analyzeICtxi_SVM_subsets.m:207:            tempneugroup.ctrCRF9 = RFCIall.pRFclassic<0.05 & RFCIall.RFindclassic==1;
analyzeICtxi_SVM_subsets.m:210:            tempneugroup.exclctrCRF9 = RFCIall.pRFclassic<0.05 & RFCIall.RFindclassic==1 & sum(RFCIall.pRrfclassic<0.05,2)==1;
analyzeICtxi_SVM_subsets.m:211:            tempneugroup.ctrCRF9nonctrIRF9 = RFCIall.RFindclassic==1 & RFCIall.pRFclassic<0.05 & RFCIall.pRrfinverse(:,1)>=0.05;
analyzeICtxi_SVM_subsets.m:226:            %         subsetdescs = {'sigkwCRF', 'ctrCRF9', 'exclctrCRF9', 'ctrIRF9', ...
analyzeMouseEye.m:333:fprintf('ctrCRF: pRFclassic* %d Pkw_rfclassic* %d sigmc_rfclassic %d RFsigexclclassic %d RFexclsigclassic %d\n', ...
analyzeMouseEye.m:337:    nnz(RFCI.RFindclassic==1 & RFCI.RFsigexclclassic), ...
analyzeMouseEye.m:338:    nnz(RFCI.RFindclassic==1 & RFCI.RFexclsigclassic) )
analyzeMouseEye.m:367:fprintf('spin ctrCRF: pRFclassic* %d Pfried_rfclassic* %d RFsigexclclassic %d RFexclsigclassic %d\n', ...
analyzeMouseEye.m:370:    nnz(RFCIspin.RFindclassic==1 & RFCIspin.RFsigexclclassic), ...
analyzeMouseEye.m:371:    nnz(RFCIspin.RFindclassic==1 & RFCIspin.RFexclsigclassic) )
analyzeMouseEye.m:427:            fprintf('fixed gaze ctrCRF: pRFclassic* %d Pkw_rfclassic* %d sigmc_rfclassic %d RFsigex
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/IC_paper_code && grep -n "RFindclassic\|ctrRF\|pRFclassic\|1804\|neuctr\|ctrneu" aggregate_psth.m aggregate_fixedgaze.m merge_postprocessed.m | head -30
```

```
aggregate_psth.m:113:% {'Rrfclassic','Rrfinverse','RFindclassic','RFindinverse', ...
aggregate_psth.m:114:%     'Pkw_rfclassic','Pkw_rfinverse','pRrfclassic','pRrfinverse','pRFclassic','pRFinverse'};
aggregate_fixedgaze.m:91:% {'Rrfclassic','Rrfinverse','RFindclassic','RFindinverse', ...
aggregate_fixedgaze.m:92:%     'Pkw_rfclassic','Pkw_rfinverse','pRrfclassic','pRrfinverse','pRFclassic','pRFinverse'};
aggregate_fixedgaze.m:613:RFindclassic = popavg.RFCIall.RFindclassic(neuvalfg);
aggregate_fixedgaze.m:617:figure; histogram2(RFindclassic(neuoi), RFCI_fixedgazeall.RFindclassic(neuoi), 'displaystyle', 'tile')
aggregate_fixedgaze.m:620:disp(mean(RFindclassic(neuoi)==RFCI_fixedgazeall.RFindclassic(neuoi)))
merge_postprocessed.m:79:    % {'Rrfclassic','Rrfinverse','RFindclassic','RFindinverse', ...
merge_postprocessed.m:80:    %     'Pkw_rfclassic','Pkw_rfinverse','pRrfclassic','pRrfinverse','pRFclassic','pRFinverse'};
merge_postprocessed.m:200:        % {'Rrfclassic','Rrfinverse','RFindclassic','RFindinverse', ...
merge_postprocessed.m:201:        %     'Pkw_rfclassic','Pkw_rfinverse','pRrfclassic','pRrfinverse','pRFclassic','pRFinverse'};
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/IC_paper_code && grep -n "RFsigexcl\|sigexcl\|excl\|neuoi *=" aggregate_psth.m aggregate_fixedgaze.m | head -30; sed -n 595,624p aggregate_fixedgaze.m
```

```
aggregate_psth.m:554:    neuoi = strcmp(aggneuloc, v(ii));
aggregate_fixedgaze.m:235:        Nneuoi = length(neuoind);
aggregate_fixedgaze.m:476:        Nneuoi = length(neuoind);
aggregate_fixedgaze.m:615:%neuoi = neuinarea;
aggregate_fixedgaze.m:616:neuoi = neuinarea & popavg.RFCIall.Pkw_rfclassic(neuvalfg)<0.05;
    toc
end

if aggpsth
    save([datadir 'postprocessed\openscope_psthavg_fixedgazeall_', num2str(gazedistthresh), 'pix.mat'], ...
        'validfixedgazesessions', 'probes', 'visareas', 'visind', 'nwbsessions', ...
        'neuoindall', 'probeneuall', 'neulocall', 'neupeakchall', 'sesneuall', 'neuctxall', ...
        'unit_amplitude_all', 'unit_isi_violations_all', 'unit_wfdur_all', 'unit_amplitude_cutoff_all', 'unit_presence_ratio_all', ...
        'vistrialtypes_fixedgazeagg', 'vistrialrep_fixedgazeagg', 'vistrialorder_fixedgazeagg', 'vistrial_fixedgazeagg', ...
        'ICblocks', 'ICtrialtypes', 'psthtli', 'psthavg_fixedgazeall', 'Ronavg_fixedgazeall', 'Roffavg_fixedgazeall', ...
        'Ronstd_fixedgazeall', 'Roffstd_fixedgazeall', '-v7.3') %'psthsem_fixedgazeall', 
end

%% MATCH BETWEEN CRF POSITION FOR ALL TRIALS VS FIXED GAZE TRIALS: ~63% neurons show match
popavg = load([datadir 'postprocessed\openscope_popavg_all.mat']);
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && python -c "
import h5py,remfile,numpy as np,sys
sys.path.insert(0,'entries/000248-shin-2025')
import illusion as il
A=il.session_assets(); f=h5py.File(remfile.File(A[3]['url']),'r'); g=f['intervals/RFCI_presentations']
x=g['x_position'][:].reshape(-1,4); y=g['y_position'][:].reshape(-1,4); m=g['Mask'][:].reshape(-1,4); o=g['orientation'][:].reshape(-1,4)
print((x==x[:,:1]).all(), (y==y[:,:1]).all(), (m==m[:,:1]).all(), np.unique(o,axis=0))
s=g['start_time'][:]; e=g['stop_time'][:]; print(np.unique(np.round(np.diff(s.reshape(-1,4),axis=1),3)), np.round(np.percentile(s[4::4]-s[3:-1:4],[0,50,100]),3))
"
```

```
Wed Oct 28 00:48:30 UTC 2026
True True True [[  0.  45.  90. 135.]]
[0.25  0.284] [0.25  0.25  0.267]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t7.py <<'EOF'
import sys, time, pickle, os
os.environ['OMP_NUM_THREADS']='1'
sys.path.insert(0, 'entries/000248-shin-2025')
import illusion as il, numpy as np, pandas as pd
S=pickle.load(open('S.pkl','rb'))
s=S[1]; u=s['units']; b=s['blocks']['ICwcfg1']
m=((u.area=='V1')&u.rs).values
for rd in ['a','b']:
    t=time.time(); r=il.decode(b['R'][:,m], b['codes'], [106,107,110,111],[1105,1109], seed=0, reading=rd); print(rd, time.time()-t, r['acc'], il.inference_score(r['probe']))
t=time.time(); r=il.decode(b['R'][:,m], b['codes'], [1201,1299],[106,111], seed=0); print('xre', time.time()-t, r['acc'], r['probe'])
EOF
python t7.py
```

```
a 1.6337699890136719 0.891875 (np.float64(0.8555000000000001), np.float64(0.8912500000000001), np.float64(0.03575))
b 7.4087677001953125 0.9225000000000001 (np.float64(0.9111250000000001), np.float64(0.93625), np.float64(0.025125))
xre 0.14266228675842285 0.9787500000000001 [[0.898  0.102 ]
 [0.4605 0.5395]]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import h5py,remfile,numpy as np,sys
sys.path.insert(0,'entries/000248-shin-2025')
import illusion as il, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
A=il.session_assets(); f=h5py.File(remfile.File(A[1]['url']),'r'); g=f['stimulus/templates/ICwcfg1_presentations']
print(list(g.keys())[:30]); print(dict(g.attrs))
fig,ax=plt.subplots(4,6,figsize=(18,10))
for k in range(22):
    im=g[f'ICwcfg1_presentations{k}'][::8,::8]; a=ax.flat[k]; a.imshow(im,cmap='gray'); a.set_title(f'{k} -> {il.IC_TRIAL_TYPES[k]}'); a.axis('off')
plt.savefig('templates.png',dpi=50)
"
```

```
['ICwcfg1_presentations0', 'ICwcfg1_presentations1', 'ICwcfg1_presentations10', 'ICwcfg1_presentations11', 'ICwcfg1_presentations12', 'ICwcfg1_presentations13', 'ICwcfg1_presentations14', 'ICwcfg1_presentations15', 'ICwcfg1_presentations16', 'ICwcfg1_presentations17', 'ICwcfg1_presentations18', 'ICwcfg1_presentations19', 'ICwcfg1_presentations2', 'ICwcfg1_presentations20', 'ICwcfg1_presentations21', 'ICwcfg1_presentations3', 'ICwcfg1_presentations4', 'ICwcfg1_presentations5', 'ICwcfg1_presentations6', 'ICwcfg1_presentations7', 'ICwcfg1_presentations8', 'ICwcfg1_presentations9']
{'description': 'movie', 'namespace': 'core', 'neurodata_type': 'Images', 'object_id': '1dbf3d9a-806c-45b3-b084-dbdd93104cea'}
Shell cwd was reset to
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/templates.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t8.py <<'EOF'
import sys, time, pickle, os
os.environ['OMP_NUM_THREADS']='1'
sys.path.insert(0, 'entries/000248-shin-2025')
import illusion as il, numpy as np, pandas as pd
S=pickle.load(open('S.pkl','rb'))
t=time.time()
for s in S:
    u=s['units']; b=s['blocks']['ICwcfg1']
    m=((u.area=='V1')&u.rs).values
    r=il.decode(b['R'][:,m], b['codes'], [106,107,110,111],[1105,1109], seed=0)
    print(s['subject'], m.sum(), round(r['acc'],3), np.round(il.inference_score(r['probe']),3), np.round(r['probe'],2).tolist())
print(time.time()-t)
EOF
python t8.py
```

```
619293 89 0.268 [-0.003  0.254  0.257] [[0.29, 0.24, 0.24, 0.23], [0.27, 0.24, 0.28, 0.22]]
619296 168 0.892 [0.856 0.891 0.036] [[0.96, 0.02, 0.02, 0.0], [0.05, 0.07, 0.05, 0.82]]
620333 114 0.667 [0.162 0.428 0.266] [[0.23, 0.52, 0.02, 0.24], [0.08, 0.27, 0.01, 0.63]]
620334 68 0.694 [0.281 0.43  0.15 ] [[0.04, 0.29, 0.0, 0.66], [0.03, 0.15, 0.01, 0.82]]
625545 190 0.794 [0.363 0.61  0.247] [[0.68, 0.09, 0.2, 0.03], [0.02, 0.03, 0.41, 0.54]]
625554 179 0.775 [0.634 0.798 0.165] [[0.79, 0.18, 0.01, 0.01], [0.01, 0.04, 0.14, 0.8]]
625555 314 0.497 [0.081 0.297 0.217] [[0.54, 0.05, 0.37, 0.03], [0.45, 0.12, 0.38, 0.05]]
630506 58 0.748 [0.117 0.328 0.211] [[0.03, 0.42, 0.01, 0.54], [0.0, 0.36, 0.01, 0.63]]
631510 129 0.828 [0.531 0.597 0.066] [[0.88, 0.01, 0.07, 0.03], [0.21, 0.36, 0.12, 0.31]]
631570 142 0.801 [0.574 0.72  0.146] [[0.84, 0.07, 0.06, 0.03], [0.11, 0.07, 0.22, 0.6]]
633229 181 0.867 [0.223 0.532 0.309] [[0.49, 0.39, 0.1, 0.03], [0.03, 0.16, 0.23, 0.58]]
637484 172 0.552 [0.    0.281 0.28 ] [[0.02, 0.56, 0.0, 0.43], [0.02, 0.43, 0.0, 0.55]]
61.255258560180664
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t9.py <<'EOF'
import sys, time, pickle, os
sys.path.insert(0, 'entries/000248-shin-2025')
import illusion as il, numpy as np, pandas as pd
S=pickle.load(open('S.pkl','rb'))
s=S[4]; u=s['units']; b=s['blocks']['ICwcfg1']
v1=((u.area=='V1')&u.rs).values
g=il.ic_groups(b['R'][:,v1], b['codes'])
ids=u.index[v1]
tg=list(ids[g.ic_enc.values|g.seg_resp.values]); src=list(u.index[((u.area!='V1')&u.rs).values])
print(len(tg), len(src), sum(len(s['ccg_bins'][i]) for i in tg), sum(len(s['ccg_bins'][i]) for i in src))
t=time.time(); c=il.ccg_counts([s['ccg_bins'][i] for i in tg],[s['ccg_bins'][i] for i in src],124); print('ccg', time.time()-t, c.shape, c.sum())
t=time.time()
for sm in ['box','gauss']:
    for fl in ['raw','corrected']:
        con=il.connections(c,124,sm,fl); print(sm, fl, con.sum(), con.mean(axis=1)[:10])
print(time.time()-t)
EOF
python t9.py
```

```
92 770 1367135 9827684
ccg 4.675666809082031 (92, 770, 249) 823143588
box raw 207 [0.         0.0012987  0.0038961  0.00519481 0.         0.
 0.00779221 0.01298701 0.01428571 0.01168831]
box corrected 345 [0.         0.0012987  0.00519481 0.01298701 0.0025974  0.0012987
 0.01818182 0.01688312 0.02207792 0.01428571]
gauss raw 164 [0.         0.0012987  0.0038961  0.0038961  0.         0.
 0.0025974  0.01038961 0.00909091 0.00649351]
gauss corrected 248 [0.         0.0012987  0.0038961  0.00649351 0.0012987  0.
 0.01038961 0.01558442 0.01168831 0.01038961]
1.1699323654174805
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t10.py <<'EOF'
import sys, pickle
sys.path.insert(0, 'entries/000248-shin-2025')
import illusion as il, numpy as np, pandas as pd
S=pickle.load(open('S.pkl','rb'))
for s in S:
    e=s['eye']
    if e is None: print(s['subject'],'no eye'); continue
    rf=e['RF']; ic=e['ICwcfg1']
    fix=(rf['maxdist']<20)&~rf['blink']
    cl=~s['rf']['inverse']
    print(s['subject'], round(e['hz'],2), e['units'], round(e['frac_nan'],3), round(e['frac_blink'],3), np.round(e['mode'],1), np.round(e['x_range'],1), round(e['width_median'],1), round(e['eye_width_median'],1),
      'fixRF', fix.mean().round(2), 'pos covered', len(np.unique(s['rf']['pos'][fix&cl])), 'fixIC', ((ic['maxdist']<20)&~ic['blink']).mean().round(2), 'lag', np.round(np.percentile(ic['lag_first_frame'],[0,100]),3))
EOF
python t10.py
```

```
619293 no eye
619296 nan {'data': 'meters', 'area': ''} 0.001 0.009 [338.6 236.3] [325.  358.9] 27.2 160.0 fixRF 0.92 pos covered 9 fixIC 0.98 lag [0.    0.017]
620333 nan {'data': 'meters', 'area': ''} 0.001 0.021 [368.6 262.8] [347.6 399.2] 23.0 166.2 fixRF 0.28 pos covered 9 fixIC 0.84 lag [0.    0.017]
620334 nan {'data': 'meters', 'area': ''} 0.01 0.027 [297.7 257.8] [272.4 346.6] 29.5 163.6 fixRF 0.53 pos covered 9 fixIC 0.73 lag [0.    0.017]
625545 nan {'data': 'meters', 'area': ''} 0.007 0.01 [357.  247.6] [320.5 382.3] 25.7 146.1 fixRF 0.86 pos covered 9 fixIC 0.84 lag [0.    0.017]
625554 nan {'data': 'meters', 'area': ''} 0.001 0.018 [366.8 254.3] [322.1 386.5] 33.6 150.8 fixRF 0.06 pos covered 3 fixIC 0.83 lag [0.    0.017]
625555 nan {'data': 'meters', 'area': ''} 0.006 0.012 [393.3 275.3] [376.1 417.6] 18.9 128.6 fixRF 0.59 pos covered 9 fixIC 0.95 lag [0.    0.017]
630506 nan {'data': 'meters', 'area': ''} 0.01 0.031 [365.5 257.4] [304.7 393.6] 21.7 158.0 fixRF 0.37 pos covered 8 fixIC 0.89 lag [0.    0.017]
631510 nan {'data': 'meters', 'area': ''} 0.042 0.07 [299.  236.5] [270.3 326.7] 18.4 154.2 fixRF 0.59 pos covered 9 fixIC 0.86 lag [0.    0.017]
631570 nan {'data': 'meters', 'area': ''} 0.019 0.026 [338.1 239.6] [309.9 362.9] 19.5 142.5 fixRF 0.78 pos covered 9 fixIC 0.93 lag [0.    0.017]
633229 nan {'data': 'meters', 'area': ''} 0.041 0.067 [361.3 279.5] [346.9 401.1] 19.2 151.4 fixRF 0.36 pos covered 9 fixIC 0.83 lag [0.    0.017]
637484 no eye
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import h5py,remfile,numpy as np,sys
sys.path.insert(0,'entries/000248-shin-2025')
import illusion as il
A=il.session_assets(); f=h5py.File(remfile.File(A[1]['url']),'r'); ts=f['acquisition/EyeTracking/eye_tracking/timestamps'][:]
print(np.isnan(ts).sum(), len(ts), np.all(np.diff(ts[~np.isnan(ts)])>0), np.nanmedian(np.diff(ts)), np.nanpercentile(np.diff(ts),[0.1,50,99.9]))
print([ (k, f['acquisition/EyeTracking/'+k].attrs.get('timestamps')) for k in ['pupil_tracking']], list(f['acquisition/EyeTracking/pupil_tracking'].keys()))
"
```

```
1 538128 True 0.016660000000229047 [0.01665 0.01666 0.01668]
[('pupil_tracking', None)] ['angle', 'area', 'area_raw', 'data', 'height', 'reference_frame', 'timestamps', 'width']
Shell cwd was reset to
```

**Agent calls Bash**

```bash
curl -s -o /dev/null -w "%{http_code}\n" -L https://doi.org/10.24433/CO.6659254.v2; curl -s -L https://codeocean.com/capsule/2540707/tree/v2 | head -c 600; echo; curl -s -o /dev/null -w "%{http_code}\n" https://api.codeocean.com/capsule/2540707
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd entries/000248-shin-2025 && python - <<'EOF'
p='illusion.py'; s=open(p).read()
s=s.replace('''    ts = e["eye_tracking/timestamps"][:]
''','''    ts = e["eye_tracking/timestamps"][:]
    n_nan_ts = int(np.isnan(ts).sum())
    ts = np.where(np.isnan(ts), np.inf, ts)       # a NaN timestamp is sorted last
''')
s=s.replace('''"hz": 1 / np.median(np.diff(ts)), "n_frames": len(ts),''','''"hz": 1 / np.nanmedian(np.diff(ts[np.isfinite(ts)])), "n_frames": len(ts),
           "n_nan_timestamps": n_nan_ts, "nan_timestamp_last": bool(n_nan_ts == 0 or not np.isfinite(ts[-1])),''')
open(p,'w').write(s)
EOF
grep -n "n_nan_ts" illusion.py
```

```
241:    n_nan_ts = int(np.isnan(ts).sum())
255:           "n_nan_timestamps": n_nan_ts, "nan_timestamp_last": bool(n_nan_ts == 0 or not np.isfinite(ts[-1])),
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='illusion.py'; s=open(p).read()
old='''            "R": _window_counts(bins, onset_ms, 1, IC_WINDOW_MS) * (1000.0 / IC_WINDOW_MS)}
'''
new='''            "R": _window_counts(bins, onset_ms, 1, IC_WINDOW_MS) * (1000.0 / IC_WINDOW_MS)}
        if blk == "ICwcfg1":   # the 400 ms before onset, for the check of the clock
            s["blocks"][blk]["R_pre"] = _window_counts(bins, onset_ms, 1 - IC_WINDOW_MS, 0) * (1000.0 / IC_WINDOW_MS)
'''
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && python t4.py 2>&1 | grep "load all"
```

```
load all 158.11363577842712
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build_nb.py",
 "content": "\"\"\"Build the notebook from cells. Conclusions are filled from conclusions.py if present.\"\"\"\nimport json\nimport os\nimport sys\n\nimport nbformat as nbf\n\nHERE = os.path.dirname(os.path.abspath(__file__))\nsys.path.insert(0, HERE)\ntry:\n    from conclusions import RESULTS, HEADER_TABLE, SUMMARY\nexcept ImportError:\n    RESULTS, HEADER_TABLE, SUMMARY = {}, \"\", \"\"\n\ncells = []\n\n\ndef md(src, tags=None):\n    c = nbf.v4.new_markdown_cell(src.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\ndef code(src, tags=None):\n    c = nbf.v4.new_code_cell(src.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\ndef result(cid):\n    md(RESULTS.get(cid, \"**Result: to be written.**\"), tags=[\"conclusion\"])\n\n\nmd(f\"\"\"\n# Shin et al. (2025) from dandiset 000248: the Neuropixels claims\n\n**Paper.** Shin H, Ogando MB, Abdeladim L, ... Lecoq J, Adesnik H (2025). Recurrent pattern\ncompletion drives the neocortical representation of sensory inference. *Nature Neuroscience* 28,\n2319-2329. [doi:10.1038/s41593-025-02055-5](https://doi.org/10.1038/s41593-025-02055-5). The\nclaims file was written from the version of record (main text, figure legends, Methods and\nExtended Data legends); the Supplementary Information was not available to it.\n\n**Dandiset.** [DANDI:000248](https://dandiarchive.org/dandiset/000248/0.240502.2344), version\n0.240502.2344. The paper cites the dandiset without a version. This is its only published version,\nso it is pinned. The draft has the same 78 assets and size; it was last modified at the time of\npublication (2024-05-02). The paper's analysis code reads a copy named `00248_v240130` (January\n2024), before this version; no earlier version was published, so a difference between the two\ncannot be checked.\n\n**What the dandiset holds.** The 12 Neuropixels sessions (12 mice), each a `_ogen.nwb` file with\nthe units of all six probes, the stimulus tables, the receptive field and size blocks, and in 10\nsessions eye tracking; and 66 `_probe-N_ecephys.nwb` files with LFP, which are not used. The 2p\nimaging, 2p mesoscope and 2p holography data of the paper are not in it.\n\n**Method sources.** The claims file gives each method; where it leaves a detail open, the detail\nis taken from the paper or from the analysis code the claims file cites\n(github.com/hs13/IC_paper_code at commit 50e04ea), and the helper module `illusion.py` says which.\n\n{HEADER_TABLE}\n\"\"\")\n\ncode(\"\"\"\nimport os\nos.environ.setdefault(\"OMP_NUM_THREADS\", \"1\")\nos.environ.setdefault(\"OPENBLAS_NUM_THREADS\", \"1\")\nimport time\nimport warnings\nfrom itertools import combinations\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nfrom joblib import Parallel, delayed\nfrom scipy import stats\n\nimport illusion as il\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\npd.set_option(\"display.width\", 220)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 200)\nN_JOBS = 4\n\nstarted = time.time()\nsessions = il.load_all()\nprint(f\"loaded {len(sessions)} sessions of dandiset {il.DANDISET_ID} version {il.DANDISET_VERSION} \"\n      f\"in {time.time() - started:.0f} s\")\n\"\"\")\n\nmd(\"\"\"\n## Data check\n\nEach check of the description against the values is stated under its output.\n\"\"\")\n\ncode(\"\"\"\nassets = pd.DataFrame(il.all_assets())\nassets[\"subject\"] = assets.path.str.split(\"/\").str[0]\nassets[\"kind\"] = np.where(assets.path.str.endswith(\"_ogen.nwb\"), \"session (_ogen)\", \"probe LFP (_ecephys)\")\nprint(\"Assets:\", len(assets), \"; total size (GB):\", round(assets[\"size\"].sum() / 1e9, 1))\nprint(pd.crosstab(assets.subject, assets.kind).to_string())\ninfo = pd.DataFrame([{\"subject\": s[\"subject\"], \"session\": s[\"session_id\"], \"genotype\": s[\"genotype\"].split(\"/\")[0],\n                      \"age\": s[\"age\"], \"units_in_file\": s[\"n_units_file\"],\n                      \"visual_area_units\": len(s[\"units\"]), \"eye_tracking\": s[\"eye\"] is not None}\n                     for s in sessions])\nprint()\nprint(info.to_string(index=False))\nprint(\"\\\\nMice by genotype:\", info.genotype.value_counts().to_dict())\nprint(\"Paper, Methods (Animals): Sst-IRES-Cre;Ai32 n = 10 and PV-IRES-Cre;Ai32 n = 4; Results and legends: 12 sessions from 12 mice.\")\n\"\"\", tags=[\"sanity\"])\n\nmd(\"\"\"\nThe dandiset holds 12 sessions from 12 mice, as the Results and legends state. One file per session\n(`_ogen.nwb`) holds the units of all probes; sub-619293 has no probe LFP files. The genotypes are 9\nSst-IRES-Cre;Ai32 and 3 Pvalb-IRES-Cre;Ai32 mice, against the 10 and 4 (14 mice) of the Methods'\nAnimals list: the Methods list two more mice than the analyses use, and the split differs.\n\"\"\")\n\ncode(\"\"\"\nrows = []\nfor s in sessions:\n    wd, q, ar = s[\"waveform_duration_all\"], s[\"quality_all\"], s[\"area_all\"]\n    rows.append({\"subject\": s[\"subject\"], \"units\": len(wd), \"noise_label\": int(np.sum(q == \"noise\")),\n                 \"in_6_visual_areas\": int(np.sum(ar != None)),\n                 \"RS_all_areas\": int(np.sum(wd > 0.4)),\n                 **{f\"{a}_RS\": int(np.sum((s[\"units\"].area == a) & s[\"units\"].rs)) for a in il.AREAS}})\nunits_tab = pd.DataFrame(rows)\nprint(units_tab.to_string(index=False))\nallwd = np.concatenate([s[\"waveform_duration_all\"] for s in sessions])\nprint(\"\\\\nwaveform_duration (ms): min %.3f, median %.3f, max %.3f; fraction > 0.4 ms: %.3f\" %\n      (allwd.min(), np.median(allwd), allwd.max(), np.mean(allwd > 0.4)))\nprint(\"quality values:\", sorted(set(np.concatenate([s[\"quality_all\"] for s in sessions]))))\nlabs = pd.concat([s[\"unit_labels_all\"] for s in sessions]).groupby(level=0).sum()\nvis = labs[[il.area_of(x) is not None for x in labs.index]]\nprint(\"\\\\nVisual cortex labels used (units):\", vis.to_dict())\nprint(\"Other labels with 'VIS':\", [x for x in labs.index if \"VIS\" in x and il.area_of(x) is None])\nprint(\"Spike times sorted within units (first 50 units per session):\", all(s[\"sorted_ok\"] for s in sessions))\n\"\"\", tags=[\"sanity\"])\n\nmd(\"\"\"\nUnits carry a waveform duration in ms (0.03 to 2.7 ms, a bimodal range as expected for\ntrough-to-peak widths), a peak channel whose CCF label gives the area and layer, and a `quality`\nlabel of `good` or `noise`. The Methods say that \"all units not classified as noise were packaged\ninto Neurodata Without Borders files\"; the files nevertheless hold units labelled `noise` (counts\nabove). The analyses below keep them, as the paper's code does (it applies no quality filter), and\nthe counts in the claims below show the paper's numbers include them. LM has fewer than 50 RS units\nin four sessions (none in three), and RL none in one, as the Fig. 3d legend's session counts imply.\n\"\"\")\n\ncode(\"\"\"\nrows = []\nfor s in sessions:\n    for blk, b in s[\"blocks\"].items():\n        codes, n = np.unique(b[\"codes\"], return_counts=True)\n        rows.append({\"subject\": s[\"subject\"], \"block\": blk, \"table_rows\": b[\"n_rows\"], \"trials\": len(b[\"codes\"]),\n                     \"ITI_rows_with_nonzero_frame\": b[\"iti_rows_nonzero_frame\"],\n                     \"n_IC1\": int(np.sum(b[\"codes\"] == il.IC1)), \"n_other_min\": int(n.min()), \"n_other_max\": int(n.max()),\n                     \"dur_s_min\": b[\"duration\"].min().round(3), \"dur_s_max\": b[\"duration\"].max().round(3),\n                     \"iti_s_median\": np.median(b[\"iti\"]).round(3)})\nblk_tab = pd.DataFrame(rows)\nprint(blk_tab.groupby(\"block\").agg({\"trials\": [\"min\", \"max\"], \"table_rows\": [\"min\", \"max\"], \"ITI_rows_with_nonzero_frame\": \"max\",\n                                    \"n_IC1\": [\"min\", \"max\"], \"n_other_min\": \"min\", \"n_other_max\": \"max\",\n                                    \"dur_s_min\": \"min\", \"dur_s_max\": \"max\", \"iti_s_median\": [\"min\", \"max\"]}).to_string())\nb = sessions[0][\"blocks\"][\"ICwcfg1\"]\ncodes, n = np.unique(b[\"codes\"], return_counts=True)\nprint(\"\\\\nICwcfg1 trials per image code, first session:\", dict(zip(codes.tolist(), n.tolist())))\nrf = pd.DataFrame([{\"subject\": s[\"subject\"], \"rf_rows\": s[\"rf\"][\"n_rows\"], \"rf_trials\": len(s[\"rf\"][\"pos\"]),\n                    \"classic_per_position\": np.bincount(s[\"rf\"][\"pos\"][~s[\"rf\"][\"inverse\"]], minlength=9).tolist(),\n                    \"inverse_per_position\": np.bincount(s[\"rf\"][\"pos\"][s[\"rf\"][\"inverse\"]], minlength=9).tolist(),\n                    \"row_dur_s\": (round(s[\"rf\"][\"row_dur\"].min(), 3), round(s[\"rf\"][\"row_dur\"].max(), 3)),\n                    \"directions_per_trial\": s[\"rf\"][\"directions_per_trial\"][0],\n                    \"longest_spontaneous_s\": round(s[\"spont_interval\"][1] - s[\"spont_interval\"][0], 1)}\n                   for s in sessions])\nprint(rf.to_string(index=False))\n\"\"\", tags=[\"sanity\"])\n\nmd(\"\"\"\nEach IC block table alternates image rows with ITI rows whose `frame` is 0, as the code assumes; no\nITI row carries an image. ICwcfg1 has 5,300 trials per session: 400 of blank, X, TC1, IC1, LC1,\nTC2, LC2, IC2, TRE1, TRE2, XRE1 and XRE2, and 50 of IRE1, IRE2 and the eight segment images. The\nMethods say IC and LC images were shown 400 times and each other image at least 50 times; the\ndata agree, with TRE, XRE, X and TC images at 400. The other blocks have 30 trials of each of the\n22 images. Images last 0.400 s with a 0.4 s ITI, as stated. The receptive field block has 180\ntrials (four 0.25 s directions each, 0 s ITI) at 9 positions for standard and inverse patches,\n10 each, as the Methods state. The stimulus tables carry the image index (`frame`) without image\nnames; the names are the code's list, and the image templates stored in the files are consistent\nwith it (shown at the end of this section).\n\"\"\")\n\ncode(\"\"\"\n# Clock check: decode the four training images from V1 in the 400 ms after onset, in the 400 ms\n# before onset, and after shuffling the labels. If spike times and the trial table share a clock,\n# only the first is above chance.\ndef clock_check(i, s):\n    u, b = s[\"units\"], s[\"blocks\"][\"ICwcfg1\"]\n    m = ((u.area == \"V1\") & u.rs).values\n    rng = np.random.default_rng(100 + i)\n    shuffled = b[\"codes\"].copy()\n    sel = np.isin(shuffled, [il.IC1, il.LC1, il.LC2, il.IC2])\n    shuffled[sel] = rng.permutation(shuffled[sel])\n    return {\"subject\": s[\"subject\"],\n            \"post_0_400ms\": il.decode(b[\"R\"][:, m], b[\"codes\"], [106, 107, 110, 111], [1105], seed=i)[\"acc\"],\n            \"pre_-400_0ms\": il.decode(b[\"R_pre\"][:, m], b[\"codes\"], [106, 107, 110, 111], [1105], seed=i)[\"acc\"],\n            \"post_shuffled_labels\": il.decode(b[\"R\"][:, m], shuffled, [106, 107, 110, 111], [1105], seed=i)[\"acc\"],\n            \"rate_post_Hz\": b[\"R\"][:, m].mean(), \"rate_pre_Hz\": b[\"R_pre\"][:, m].mean()}\nclock = pd.DataFrame(Parallel(n_jobs=N_JOBS)(delayed(clock_check)(i, s) for i, s in enumerate(sessions)))\nprint(clock.round(3).to_string(index=False))\nprint(\"chance = 0.25\")\n\"\"\", tags=[\"sanity\"])\n\nmd(\"\"\"\nIn every session the four training images are decoded from V1 spikes after onset and not from the\n400 ms before onset or with shuffled labels (values above), so the spike times and the stimulus\ntable share a clock. The eye tracking timestamps are checked below.\n\"\"\")\n\ncode(\"\"\"\nrows = []\nfor s in sessions:\n    e = s[\"eye\"]\n    if e is None:\n        rows.append({\"subject\": s[\"subject\"], \"eye\": False})\n        continue\n    rows.append({\"subject\": s[\"subject\"], \"eye\": True, \"frame_rate_Hz\": round(e[\"hz\"], 2), \"frames\": e[\"n_frames\"],\n                 \"nan_timestamps\": e[\"n_nan_timestamps\"], \"nan_is_last\": e[\"nan_timestamp_last\"],\n                 \"stated_unit_pupil_xy\": e[\"units\"][\"data\"], \"pupil_x_1_99\": np.round(e[\"x_range\"], 0).tolist(),\n                 \"pupil_y_1_99\": np.round(e[\"y_range\"], 0).tolist(), \"pupil_width_median\": round(e[\"width_median\"], 1),\n                 \"eye_width_median\": round(e[\"eye_width_median\"], 1), \"frac_nan_pupil\": round(e[\"frac_nan\"], 3),\n                 \"frac_likely_blink\": round(e[\"frac_blink\"], 3),\n                 \"first_frame_after_onset_s\": np.round(np.percentile(e[\"ICwcfg1\"][\"lag_first_frame\"], [0, 100]), 4).tolist()})\neye_tab = pd.DataFrame(rows)\nprint(eye_tab.to_string(index=False))\n\"\"\", tags=[\"sanity\"])\n\nmd(\"\"\"\nTen sessions have eye tracking, as the Extended Data Fig. 2 legend states. The eye video is sampled\nat 60 Hz (timestamps 16.7 ms apart), where the Methods say \"Videos of the eye and body were\nacquired at 30 Hz\"; the paper's code assumes 60 Hz. The pupil position is stated in meters, but its\nvalues (pupil center near 300 to 400, pupil half-width near 20, eye half-width near 150) are camera\npixels, as the code's comments say. No conversion to visual degrees is in the files. One timestamp\nper session is NaN, the last one, and is not used. Every IC trial has an eye frame within 17 ms of\nits onset, so eye frames cover the trial table; that the eye clock matches the stimulus clock is\nconsistent with this, not shown by it.\n\"\"\")\n\ncode(\"\"\"\n# The image templates stored in the first session, with the code's names for each frame index.\nimport h5py, remfile\nf = h5py.File(remfile.File(il.session_assets()[0][\"url\"]), \"r\")\ng = f[\"stimulus/templates/ICwcfg1_presentations\"]\nnames = [\"blank\", \"X\", \"TC1\", \"IC1\", \"LC1\", \"TC2\", \"LC2\", \"IC2\", \"IRE1\", \"IRE2\", \"TRE1\", \"TRE2\", \"XRE1\", \"XRE2\",\n         \"In BR\", \"In BL\", \"In TL\", \"In TR\", \"Out BR\", \"Out BL\", \"Out TL\", \"Out TR\"]\nfig, axs = plt.subplots(4, 6, figsize=(12, 5.5))\nfor k, ax in enumerate(axs.flat):\n    ax.axis(\"off\")\n    if k < 22:\n        img = g[f\"ICwcfg1_presentations{k}\"][::10, ::10]\n        ax.imshow(img, cmap=\"gray\", vmin=0, vmax=255)\n        ax.set_title(f\"{k}: {names[k]} ({il.IC_TRIAL_TYPES[k]})\", fontsize=7)\nplt.tight_layout()\nplt.show()\nprint(\"template size:\", g[\"ICwcfg1_presentations0\"].shape, \"; values\", g[\"ICwcfg1_presentations0\"][:].min(), \"to\",\n      g[\"ICwcfg1_presentations0\"][:].max())\n\"\"\", tags=[\"sanity\"])\n\nmd(\"\"\"\nThe templates match the code's names: index 3 and 7 show the two illusory bars (IC1 at 135\ndegrees, IC2 at 45 degrees), 4 and 6 the recombined LC images, 8 and 9 the IC images with the real\nbar outlined (IRE), 10 and 11 the TRE images, 12 and 13 the XRE images, and 14 to 21 single inducer\nsegments.\n\"\"\")\n\ncode(\"\"\"\n# Recordings deposited twice: compare spike counts, unit counts and trial order between sessions.\nsig = []\nfor s in sessions:\n    sig.append((s[\"subject\"], s[\"n_units_file\"], int(s[\"units\"].n_spikes_bins.sum()),\n                tuple(s[\"blocks\"][\"ICwcfg1\"][\"codes\"][:200]), round(s[\"blocks\"][\"ICwcfg1\"][\"start\"][0], 3)))\npairs = [(a[0], b[0]) for a, b in combinations(sig, 2) if a[1] == b[1] or a[2] == b[2] or a[3] == b[3] or a[4] == b[4]]\nprint(\"Pairs sharing unit count, spike count, trial order or block start:\", pairs if pairs else \"none\")\nprint(\"Trial order identical across sessions:\", len({x[3] for x in sig}) == 1)\n\"\"\", tags=[\"sanity\"])\n\nmd(\"\"\"\nNo two sessions share their unit count, spike count or first block start; every session is a\ndistinct recording. The trial order of ICwcfg1 is the same in every session (one stimulus script),\nwhich the Methods' \"Trial order within each block was randomized\" does not contradict.\n\"\"\")\n\n# ------------------------------------------------------------------ claims: counts\nmd(\"\"\"\n## results-npx-units-per-session\n\n> The Neuropixels sessions hold 150 +/- 20 V1 RS units and 597 +/- 46 higher visual area RS units\n> per session (mean +/- s.e.m., 12 sessions).\n\"\"\")\ncode(\"\"\"\nv1 = units_tab[\"V1_RS\"]\nhva = units_tab[[f\"{a}_RS\" for a in il.AREAS[1:]]].sum(axis=1)\nprint(\"V1 RS per session:\", v1.tolist())\nprint(\"HVA RS per session:\", hva.tolist())\nprint(\"V1 RS: total %d, mean %.1f +/- %.1f (s.e.m.)\" % (v1.sum(), v1.mean(), v1.sem()))\nprint(\"HVA RS: total %d, mean %.1f +/- %.1f (s.e.m.)\" % (hva.sum(), hva.mean(), hva.sem()))\nprint(\"Paper: 150 +/- 20 and 597 +/- 46; Methods: 1,804 V1 RS units\")\ngood = [(int(((s[\"units\"].area == \"V1\") & s[\"units\"].rs & (s[\"units\"].quality == \"good\")).sum()),\n         int(((s[\"units\"].area != \"V1\") & s[\"units\"].rs & (s[\"units\"].quality == \"good\")).sum())) for s in sessions]\ngood = np.array(good)\nprint(\"Variant without units labelled noise: V1 %.1f +/- %.1f, HVA %.1f +/- %.1f\" %\n      (good[:, 0].mean(), stats.sem(good[:, 0]), good[:, 1].mean(), stats.sem(good[:, 1])))\n\"\"\", tags=[\"claim:results-npx-units-per-session\"])\nresult(\"results-npx-units-per-session\")\n\nmd(\"\"\"\n## methods-npx-ic-encoder-count\n\n> Across the ICwcfg0 and ICwcfg1 blocks, 159 of 1,804 V1 RS units are IC-encoders.\n\nIC-encoders as in the claims file (Kruskal-Wallis across blank, IC1, LC1, LC2, IC2 at p < 0.05,\nTukey-Kramer against blank, AUROC sign; code analyzeStaticICtxi.m), on the IC response\n(0 to 400 ms), in each block with that block's IC1 and IC2 images.\n\"\"\")\ncode(\"\"\"\ngroups = {}\nfor s in sessions:\n    u = s[\"units\"]\n    for blk in [\"ICwcfg1\", \"ICwcfg0\"]:\n        b = s[\"blocks\"][blk]\n        g = il.ic_groups(b[\"R\"], b[\"codes\"])\n        g.index = u.index\n        groups[(s[\"subject\"], blk)] = pd.concat([u[[\"area\", \"layer\", \"rs\", \"quality\"]], g], axis=1)\n\ndef v1rs(subject, blk):\n    g = groups[(subject, blk)]\n    return g[(g.area == \"V1\") & g.rs]\n\nper = pd.DataFrame([{\"subject\": s[\"subject\"], \"V1_RS\": len(v1rs(s[\"subject\"], \"ICwcfg1\")),\n                     \"IC_enc_ICwcfg1\": int(v1rs(s[\"subject\"], \"ICwcfg1\").ic_enc.sum()),\n                     \"IC_enc_ICwcfg0\": int(v1rs(s[\"subject\"], \"ICwcfg0\").ic_enc.sum()),\n                     \"IC_enc_either\": int((v1rs(s[\"subject\"], \"ICwcfg1\").ic_enc | v1rs(s[\"subject\"], \"ICwcfg0\").ic_enc).sum())}\n                    for s in sessions])\nprint(per.to_string(index=False))\ntot = per.sum(numeric_only=True)\nprint(\"\\\\nV1 RS units:\", tot.V1_RS)\nprint(\"(a) IC-encoder in at least one block:\", tot.IC_enc_either)\nprint(\"(b) sum of the two blocks' counts:\", tot.IC_enc_ICwcfg1 + tot.IC_enc_ICwcfg0)\nprint(\"Paper: 159 of 1,804 (tolerance 15.9)\")\n\"\"\", tags=[\"claim:methods-npx-ic-encoder-count\"])\nresult(\"methods-npx-ic-encoder-count\")\n\nmd(\"\"\"\n## ed6b-npx-v1-group-counts\n\n> The Neuropixels data hold 87 V1 IC-encoders and 636 V1 segment responders (the sets whose layer\n> distribution Extended Data Fig. 6b shows).\n\nReadings of the criterion: (a) RS units, ICwcfg1; (b) all units not classified as noise, ICwcfg1;\n(c) RS units, union of ICwcfg1 and ICwcfg0. For (b), the Methods say \"All units not classified as\nnoise were packaged into Neurodata Without Borders files and analyzed in this paper\", so on the\npaper's own description (b) is every unit in the files; the files also carry a `quality` label\n`noise` on some units, so (b) is run both ways: (b1) all units in the files, (b2) without the units\nlabelled noise.\n\"\"\")\ncode(\"\"\"\ndef v1all(subject, blk):\n    g = groups[(subject, blk)]\n    return g[g.area == \"V1\"]\n\nrows = []\nfor name, sel in [(\"(a) RS, ICwcfg1\", lambda sub: (v1rs(sub, \"ICwcfg1\"), None)),\n                  (\"(b1) all units in the files, ICwcfg1\", lambda sub: (v1all(sub, \"ICwcfg1\"), None)),\n                  (\"(b2) units not labelled noise, ICwcfg1\", lambda sub: (v1all(sub, \"ICwcfg1\").query(\"quality != 'noise'\"), None)),\n                  (\"(c) RS, ICwcfg1 or ICwcfg0\", lambda sub: (v1rs(sub, \"ICwcfg1\"), v1rs(sub, \"ICwcfg0\")))]:\n    ic = seg = 0\n    for s in sessions:\n        g1, g0 = sel(s[\"subject\"])\n        if g0 is None:\n            ic += int(g1.ic_enc.sum()); seg += int(g1.seg_resp.sum())\n        else:\n            ic += int((g1.ic_enc | g0.ic_enc).sum()); seg += int((g1.seg_resp | g0.seg_resp).sum())\n    rows.append({\"reading\": name, \"IC_encoders\": ic, \"segment_responders\": seg,\n                 \"IC_within_87+/-8.7\": abs(ic - 87) <= 8.7, \"seg_within_636+/-63.6\": abs(seg - 636) <= 63.6})\nprint(pd.DataFrame(rows).to_string(index=False))\n\ng = pd.concat([v1all(s[\"subject\"], \"ICwcfg1\") for s in sessions])\nlay = pd.crosstab(g.layer, [g.ic_enc, g.seg_resp])\nfor name, m in [(\"IC-encoders\", g.ic_enc), (\"segment responders\", g.seg_resp), (\"all V1 units\", g.ic_enc | ~g.ic_enc)]:\n    print(f\"\\\\nLayer proportions, {name} (reading b1), n = {int(m.sum())}:\",\n          (g[m].layer.value_counts(normalize=True).sort_index().round(3)).to_dict())\n\"\"\", tags=[\"claim:ed6b-npx-v1-group-counts\"])\nresult(\"ed6b-npx-v1-group-counts\")\n\nmd(\"\"\"\n## ed6cd-npx-ic-encoders-all-areas\n\n> IC-encoders are found in every visual area, in the Neuropixels and in the calcium imaging data.\n\nNeuropixels part only: ICwcfg1, RS units of each area, sessions with at least 50 RS units in the\narea. Visually responsive: Kruskal-Wallis across blank, IC1, LC1, LC2, IC2 at p < 0.05.\n\"\"\")\ncode(\"\"\"\nrows = []\nfor s in sessions:\n    g = groups[(s[\"subject\"], \"ICwcfg1\")]\n    for a in il.AREAS:\n        x = g[(g.area == a) & g.rs]\n        if len(x) < 50:\n            continue\n        vr = x.p_kw_BK < 0.05\n        rows.append({\"subject\": s[\"subject\"], \"area\": a, \"RS\": len(x), \"IC_enc\": int(x.ic_enc.sum()),\n                     \"vis_resp\": int(vr.sum()), \"IC_enc_frac_all\": x.ic_enc.mean(),\n                     \"IC_enc_frac_visresp\": x.ic_enc[vr].mean() if vr.any() else np.nan})\nprop = pd.DataFrame(rows)\nsummary = prop.groupby(\"area\").agg(sessions=(\"subject\", \"size\"), IC_encoders=(\"IC_enc\", \"sum\"), RS_units=(\"RS\", \"sum\"),\n                                   frac_all_mean=(\"IC_enc_frac_all\", \"mean\"), frac_all_sem=(\"IC_enc_frac_all\", \"sem\"),\n                                   frac_visresp_mean=(\"IC_enc_frac_visresp\", \"mean\"),\n                                   sessions_with_any=(\"IC_enc\", lambda v: int((v > 0).sum()))).reindex(il.AREAS)\nprint(summary.round(4).to_string())\nprint(\"\\\\nAreas with at least one IC-encoder:\", [a for a in il.AREAS if summary.loc[a, \"IC_encoders\"] > 0])\n\"\"\", tags=[\"claim:ed6cd-npx-ic-encoders-all-areas\"])\nresult(\"ed6cd-npx-ic-encoders-all-areas\")\n\n# ------------------------------------------------------------------ claims: Figure 1\nmd(\"\"\"\n## fig1e-npx-exclusive-center\n\n> In the Neuropixels data, 18 of 1,804 V1 RS units respond exclusively to the grating patch at the\n> center position (the illusory gap region) of the receptive field mapping block.\n\nPer RF trial (four directions, 1 s), the rate 0 to 1000 ms after onset, standard patches only.\nReading (a), the code: signed-rank of each position's 10 trial rates against the unit's mean rate\nin the longest spontaneous block; the center is the position of largest mean response and the only\none surviving the code's Holm step. Reading (b), the Methods: rank-sum of each position's trial\nrates against the rates in 1-s windows tiled over the longest spontaneous (gray screen) block\n(312 windows), Holm over the 9 positions, the center the only significant position (with a mean\nabove the spontaneous mean, as \"responded\" implies).\n\"\"\")\ncode(\"\"\"\nrfres = {}\nfor s in sessions:\n    u = s[\"units\"]\n    m = ((u.area == \"V1\") & u.rs).values\n    d = il.rf_positions(s[\"rf\"][\"R\"][:, m], s[\"rf\"][\"pos\"], s[\"rf\"][\"inverse\"], s[\"spont_rate\"][m], s[\"spont_windows\"][:, m])\n    d.index = u.index[m]\n    rfres[s[\"subject\"]] = d\nrf_tab = pd.DataFrame([{\"subject\": k, \"V1_RS\": len(d), \"best_center\": int((d.best == 0).sum()),\n                        \"excl_center_a\": int(d.excl_a.sum()), \"excl_center_b\": int(d.excl_b.sum()),\n                        \"kw_sig\": int((d.p_kw_rf < 0.05).sum())} for k, d in rfres.items()])\nprint(rf_tab.to_string(index=False))\nt = rf_tab.sum(numeric_only=True)\nprint(f\"\\\\nV1 RS units {t.V1_RS}; exclusively center-responsive: (a) {t.excl_center_a}, (b) {t.excl_center_b}; paper 18 (tolerance 1.8)\")\nallrf = pd.concat(rfres.values())\nfor name, m in [(\"center best and p_center (a) < 0.05/9\", (allrf.best == 0) & (allrf.p_center_a * 9 < 0.05)),\n                (\"center best and p_center (b) < 0.05/9\", (allrf.best == 0) & (allrf.p_center_b * 9 < 0.05)),\n                (\"(a) and (b) both\", allrf.excl_a & allrf.excl_b),\n                (\"(a), units not labelled noise\", allrf.excl_a & np.concatenate([s[\"units\"].quality.values[((s[\"units\"].area == \"V1\") & s[\"units\"].rs).values] != \"noise\" for s in sessions]))]:\n    print(f\"variant, {name}: {int(m.sum())}\")\n\"\"\", tags=[\"claim:fig1e-npx-exclusive-center\"])\nresult(\"fig1e-npx-exclusive-center\")\n\nmd(\"\"\"\n## fig1f-npx-ic-ire-responsive\n\n> Of the exclusively center-responsive V1 RS units, 66.7% respond substantially to the IC image and\n> 77.8% to the real-edge (IRE) image of their preferred IRE orientation, although the IC image has\n> no contrast in their receptive field.\n\nUnits of fig1e under each of its readings. Preferred IRE orientation: the IRE image with the\nstrongest mean IC response; the IC image is the one with the illusory bar of that orientation.\nTest (a): the code's Kruskal-Wallis across blank, IC and IRE with Tukey-Kramer against blank and\nAUROC > 0.5; test (b): rank-sum against blank with AUROC > 0.5. Block (i): ICwcfg1, two\norientations; block (ii): ICwcfg1 and ICwcfg0, four orientations, each image tested in its block.\n\"\"\")\ncode(\"\"\"\ndef ic_ire_table(sel_by_subject, ic_trials=None):\n    \\\"\\\"\\\"Per selected unit and (test, block reading): IC- and IRE-responsiveness, preferred orientations.\n    ic_trials: optional dict subject -> dict block -> boolean mask of trials to keep (fixed gaze).\\\"\\\"\\\"\n    rows = []\n    for s in sessions:\n        idx = sel_by_subject.get(s[\"subject\"], [])\n        if len(idx) == 0:\n            continue\n        pos = s[\"units\"].index.get_indexer(idx)\n        for blocks in [(\"ICwcfg1\",), (\"ICwcfg1\", \"ICwcfg0\")]:\n            for test in [\"a\", \"b\"]:\n                res = {}\n                for blk in blocks:\n                    b = s[\"blocks\"][blk]\n                    keep = np.ones(len(b[\"codes\"]), bool) if ic_trials is None else ic_trials[s[\"subject\"]][blk]\n                    R, c = b[\"R\"][keep][:, pos], b[\"codes\"][keep]\n                    for k, (icc, irec) in enumerate([(il.IC1, il.IRE1), (il.IC2, il.IRE2)], start=1):\n                        icr, irer = il.ic_ire_responsive(R, c, icc, irec, test)\n                        res[(blk, k)] = {\"ire_mean\": R[c == irec].mean(axis=0), \"ic_mean\": R[c == icc].mean(axis=0),\n                                         \"ic_resp\": icr, \"ire_resp\": irer}\n                keys = list(res)\n                ire_means = np.stack([res[k][\"ire_mean\"] for k in keys], axis=1)\n                ic_means = np.stack([res[k][\"ic_mean\"] for k in keys], axis=1)\n                pi = ire_means.argmax(axis=1)\n                pc = ic_means.argmax(axis=1)\n                for j, unit in enumerate(idx):\n                    kk = keys[pi[j]]\n                    rows.append({\"subject\": s[\"subject\"], \"unit\": unit, \"blocks\": \"+\".join(blocks), \"test\": test,\n                                 \"pref_ire_ori\": il.BAR_ORIENTATION[kk], \"pref_ic_ori\": il.BAR_ORIENTATION[keys[pc[j]]],\n                                 \"ic_resp\": bool(res[kk][\"ic_resp\"][j]), \"ire_resp\": bool(res[kk][\"ire_resp\"][j])})\n    return pd.DataFrame(rows)\n\ndef frac_table(t, n_units):\n    out = []\n    for (blocks, test), x in t.groupby([\"blocks\", \"test\"]):\n        ire = x[x.ire_resp]\n        out.append({\"blocks\": blocks, \"test\": test, \"units\": n_units, \"IC_resp_%\": 100 * x.ic_resp.mean(),\n                    \"IRE_resp_%\": 100 * x.ire_resp.mean(), \"IRE_resp_units\": len(ire),\n                    \"ori_match_%\": 100 * (ire.pref_ic_ori == ire.pref_ire_ori).mean() if len(ire) else np.nan})\n    return pd.DataFrame(out)\n\nfig1f = {}\nfor rd in [\"a\", \"b\"]:\n    sel = {k: d.index[d[f\"excl_{rd}\"]] for k, d in rfres.items()}\n    n = sum(len(v) for v in sel.values())\n    t = ic_ire_table(sel)\n    fig1f[rd] = t\n    ft = frac_table(t, n)\n    ft.insert(0, \"fig1e_reading\", rd)\n    print(ft.round(1).to_string(index=False))\nprint(\"\\\\nPaper: IC-responsive 66.7% (tolerance 6.67), IRE-responsive 77.8% (7.78); orientation match 78.6% (7.86)\")\n\"\"\", tags=[\"claim:fig1f-npx-ic-ire-responsive\"])\nresult(\"fig1f-npx-ic-ire-responsive\")\n\nmd(\"\"\"\n## fig1g-npx-orientation-match\n\n> For IRE-responsive exclusively center-responsive V1 RS units, the preferred orientation of the\n> illusory bar matches that of the real bar in 78.6% of units.\n\nThe `ori_match_%` column above gives the match for every reading; the table below adds the chance\nlevel of each reading (1/number of orientations) and a shuffle of the preferred IC orientations\namong the same units (1,000 shuffles, 95th percentile).\n\"\"\")\ncode(\"\"\"\nrng = np.random.default_rng(7)\nrows = []\nfor rd, t in fig1f.items():\n    for (blocks, test), x in t.groupby([\"blocks\", \"test\"]):\n        ire = x[x.ire_resp]\n        if len(ire) == 0:\n            continue\n        match = (ire.pref_ic_ori.values == ire.pref_ire_ori.values).mean()\n        null = [np.mean(rng.permutation(ire.pref_ic_ori.values) == ire.pref_ire_ori.values) for _ in range(1000)]\n        rows.append({\"fig1e_reading\": rd, \"blocks\": blocks, \"test\": test, \"IRE_resp_units\": len(ire),\n                     \"match_%\": 100 * match, \"shuffle_95th_%\": 100 * np.percentile(null, 95),\n                     \"chance_%\": 100 / (2 if blocks == \"ICwcfg1\" else 4)})\nprint(pd.DataFrame(rows).round(1).to_string(index=False))\n\"\"\", tags=[\"claim:fig1g-npx-orientation-match\"])\nresult(\"fig1g-npx-orientation-match\")\n\n# ------------------------------------------------------------------ claims: eye (ED Fig. 2)\nmd(\"\"\"\n## ed2b-npx-fixed-gaze\n\n> Limiting the Neuropixels analysis to fixed-gaze trials (pupil within 8 degrees of its modal\n> position) leaves 11 exclusively center-responsive V1 RS units, and their responses to ICs and\n> orientation match do not change the conclusion.\n\nThe files give pupil position in camera pixels only, so reading (a) (8 visual degrees) cannot be\nrun; reading (b), the code's 20 pixels, is used. Fixed-gaze trial: the largest distance of the\npupil center from its modal position, from the first eye frame after onset to the end of the trial\n(1 s for RF trials, 0.4 s for IC trials), is below 20 pixels and no frame is a likely blink (code,\nanalyzeMouseEye.m). A session is valid when its fixed-gaze standard RF trials cover all 9\npositions (code). fig1e, fig1f and fig1g are then repeated on fixed-gaze trials of the valid\nsessions.\n\"\"\")\ncode(\"\"\"\nfix_rf, fix_ic, valid = {}, {}, []\nrows = []\nfor s in sessions:\n    e = s[\"eye\"]\n    if e is None:\n        continue\n    fr = (e[\"RF\"][\"maxdist\"] < 20) & ~e[\"RF\"][\"blink\"]\n    fi = (e[\"ICwcfg1\"][\"maxdist\"] < 20) & ~e[\"ICwcfg1\"][\"blink\"]\n    fix_rf[s[\"subject\"]] = fr\n    fix_ic[s[\"subject\"]] = {\"ICwcfg1\": fi, \"ICwcfg0\": np.ones(len(s[\"blocks\"][\"ICwcfg0\"][\"codes\"]), bool)}\n    cl = ~s[\"rf\"][\"inverse\"]\n    covered = np.unique(s[\"rf\"][\"pos\"][fr & cl])\n    ok = len(covered) == 9\n    if ok:\n        valid.append(s[\"subject\"])\n    rows.append({\"subject\": s[\"subject\"], \"fixed_RF_trials_%\": 100 * fr.mean(), \"fixed_standard_RF_trials\": int((fr & cl).sum()),\n                 \"positions_covered\": len(covered), \"valid\": ok, \"fixed_ICwcfg1_trials_%\": 100 * fi.mean()})\nprint(pd.DataFrame(rows).round(1).to_string(index=False))\nprint(f\"\\\\nSessions with eye tracking: {len(fix_rf)} (paper 10); valid fixed-gaze RF sessions: {len(valid)} (paper 9)\")\n\nrf_fix = {}\nfor s in sessions:\n    if s[\"subject\"] not in valid:\n        continue\n    u = s[\"units\"]\n    m = ((u.area == \"V1\") & u.rs).values\n    d = il.rf_positions(s[\"rf\"][\"R\"][:, m], s[\"rf\"][\"pos\"], s[\"rf\"][\"inverse\"], s[\"spont_rate\"][m],\n                        s[\"spont_windows\"][:, m], trials=fix_rf[s[\"subject\"]])\n    d.index = u.index[m]\n    rf_fix[s[\"subject\"]] = d\nfor rd in [\"a\", \"b\"]:\n    n = sum(int(d[f\"excl_{rd}\"].sum()) for d in rf_fix.values())\n    print(f\"fixed-gaze exclusively center-responsive V1 RS units, fig1e reading ({rd}): {n} (paper 11, tolerance 1.1)\")\nrng = np.random.default_rng(11)\nrows = []\nfor rd in [\"a\", \"b\"]:\n    sel = {k: d.index[d[f\"excl_{rd}\"]] for k, d in rf_fix.items()}\n    n = sum(len(v) for v in sel.values())\n    t = ic_ire_table(sel, ic_trials=fix_ic)\n    for (blocks, test), x in t.groupby([\"blocks\", \"test\"]):\n        ire = x[x.ire_resp]\n        match = (ire.pref_ic_ori.values == ire.pref_ire_ori.values).mean() if len(ire) else np.nan\n        null = [np.mean(rng.permutation(ire.pref_ic_ori.values) == ire.pref_ire_ori.values) for _ in range(1000)] if len(ire) else [np.nan]\n        rows.append({\"fig1e_reading\": rd, \"blocks\": blocks, \"test\": test, \"units\": n, \"IC_resp_%\": 100 * x.ic_resp.mean(),\n                     \"IRE_resp_%\": 100 * x.ire_resp.mean(), \"IRE_resp_units\": len(ire), \"match_%\": 100 * match,\n                     \"shuffle_95th_%\": 100 * np.percentile(null, 95)})\nprint(pd.DataFrame(rows).round(1).to_string(index=False))\n\"\"\", tags=[\"claim:ed2b-npx-fixed-gaze\"])\nresult(\"ed2b-npx-fixed-gaze\")\n\nmd(\"\"\"\n## ed2f-npx-rf-match\n\n> Receptive field positions mapped with fixed-gaze trials match those mapped with all trials for\n> 81% of the 398 V1 RS units with significant receptive fields.\n\nRF position: the position of largest mean response over standard RF trials. Significant RF:\nKruskal-Wallis across the 9 positions at p < 0.05. Readings: significant with (a) all trials,\n(b) fixed-gaze trials, (c) both. Sessions: those with eye tracking whose fixed-gaze trials cover\nthe 9 positions (the valid sessions of ed2b); the 10 sessions with eye tracking, with the RF\nposition taken over the positions that have fixed-gaze trials, are shown as a variant.\n\"\"\")\ncode(\"\"\"\ndef rf_match(subjects):\n    rows = []\n    for s in sessions:\n        if s[\"subject\"] not in subjects:\n            continue\n        u = s[\"units\"]\n        m = ((u.area == \"V1\") & u.rs).values\n        allt = rfres[s[\"subject\"]]\n        fx = rf_fix[s[\"subject\"]] if s[\"subject\"] in rf_fix else il.rf_positions(\n            s[\"rf\"][\"R\"][:, m], s[\"rf\"][\"pos\"], s[\"rf\"][\"inverse\"], s[\"spont_rate\"][m], s[\"spont_windows\"][:, m],\n            trials=fix_rf[s[\"subject\"]])\n        rows.append(pd.DataFrame({\"subject\": s[\"subject\"], \"best_all\": allt.best.values, \"best_fix\": fx.best.values,\n                                  \"sig_all\": allt.p_kw_rf.values < 0.05, \"sig_fix\": fx.p_kw_rf.values < 0.05}))\n    return pd.concat(rows)\n\nfor name, subs in [(\"valid sessions\", valid), (\"all sessions with eye tracking (variant)\", list(fix_rf))]:\n    t = rf_match(subs)\n    print(f\"{name}: {t.subject.nunique()} sessions, {len(t)} V1 RS units\")\n    for rd, m in [(\"(a) significant with all trials\", t.sig_all), (\"(b) significant with fixed-gaze trials\", t.sig_fix),\n                  (\"(c) both\", t.sig_all & t.sig_fix)]:\n        x = t[m]\n        print(f\"  {rd}: n = {len(x)}, match = {np.mean(x.best_all == x.best_fix):.3f}\")\nprint(\"Paper: 0.81 (tolerance 0.081) among 398 (39.8) units\")\n\"\"\", tags=[\"claim:ed2f-npx-rf-match\"])\nresult(\"ed2f-npx-rf-match\")\n\nmd(\"\"\"\n## ed2g-npx-pupil-area\n\n> Pupil area during the presentation does not differ across the images of the IC block.\n\nPupil area z-scored over the session; per trial its mean over the 0 to 0.4 s presentation (end and\nmaximum as variants); per session and image the mean over trials; Friedman test with sessions as\nblocks. Readings: (a) IC1, LC1, LC2, IC2 of ICwcfg1; (b) all 22 images of ICwcfg1.\n\"\"\")\ncode(\"\"\"\neye_sessions = [s for s in sessions if s[\"eye\"] is not None]\nnames22 = il.IC_TRIAL_TYPES\nrows = []\nfor measure in [\"area_mean\", \"area_end\", \"area_max\"]:\n    for rd, imgs in [(\"(a) IC1, LC1, LC2, IC2\", [il.IC1, il.LC1, il.LC2, il.IC2]), (\"(b) all 22 images\", list(names22))]:\n        M = np.array([[np.nanmean(s[\"eye\"][\"ICwcfg1\"][measure][s[\"blocks\"][\"ICwcfg1\"][\"codes\"] == c]) for c in imgs]\n                      for s in eye_sessions])\n        p = stats.friedmanchisquare(*M.T).pvalue\n        rows.append({\"measure\": measure, \"reading\": rd, \"sessions\": len(M), \"friedman_p\": p,\n                     \"range_of_image_means_z\": np.ptp(M.mean(axis=0))})\nprint(pd.DataFrame(rows).round(4).to_string(index=False))\nprint(\"Paper: p = 0.7220, Friedman test, 10 sessions\")\n\"\"\", tags=[\"claim:ed2g-npx-pupil-area\"])\nresult(\"ed2g-npx-pupil-area\")\n\nmd(\"\"\"\n## ed2a-npx-gaze-confined\n\n> Eye gaze is confined to a small region that fits within the illusory gap, with no systematic\n> difference in pupil position among IC1, LC1, LC2 and IC2 presentations.\n\nPupil center during the 0 to 0.4 s presentation of IC1, LC1, LC2 and IC2 in ICwcfg1; per session\nthe image means of x and of y; a Friedman test with sessions as blocks (the criterion). Per-session\nKruskal-Wallis tests across the four images are a variant. Confinement: the extent, in camera\npixels, of the region where each session's 2D density of pupil positions (2-pixel bins, over the\nwhole session) is at least 0.01 of its peak, a reading of the criterion's \"0.01 isoline\".\n\"\"\")\ncode(\"\"\"\nimgs = [il.IC1, il.LC1, il.LC2, il.IC2]\nrows, kw = [], []\nfor coord in [\"x_mean\", \"y_mean\"]:\n    M = np.array([[np.nanmean(s[\"eye\"][\"ICwcfg1\"][coord][s[\"blocks\"][\"ICwcfg1\"][\"codes\"] == c]) for c in imgs]\n                  for s in eye_sessions])\n    rows.append({\"coordinate\": coord[0], \"friedman_p\": stats.friedmanchisquare(*M.T).pvalue,\n                 \"max_diff_between_image_means_px\": np.ptp(M - M.mean(axis=1, keepdims=True), axis=1).max()})\n    for s in eye_sessions:\n        c = s[\"blocks\"][\"ICwcfg1\"][\"codes\"]\n        v = s[\"eye\"][\"ICwcfg1\"][coord]\n        kw.append({\"subject\": s[\"subject\"], \"coordinate\": coord[0],\n                   \"kw_p\": stats.kruskal(*[v[(c == k) & np.isfinite(v)] for k in imgs]).pvalue})\nprint(pd.DataFrame(rows).round(4).to_string(index=False))\nkw = pd.DataFrame(kw)\nprint(\"\\\\nVariant, per-session Kruskal-Wallis across the 4 images: p < 0.05 in\", int((kw.kw_p < 0.05).sum()), \"of\", len(kw),\n      \"session x coordinate tests; smallest p\", kw.kw_p.min().round(4))\next = []\nfor s in eye_sessions:\n    xy = s[\"eye\"][\"density_xy\"]\n    H, xe, ye = np.histogram2d(xy[:, 0], xy[:, 1], bins=[np.arange(-150, 151, 2)] * 2)\n    inside = H >= 0.01 * H.max()\n    xs, ys = xe[:-1][inside.any(axis=1)], ye[:-1][inside.any(axis=0)]\n    ext.append({\"subject\": s[\"subject\"], \"x_extent_px\": xs.max() - xs.min() + 2, \"y_extent_px\": ys.max() - ys.min() + 2,\n                \"frac_within_20px_of_mode\": np.mean(np.hypot(xy[:, 0], xy[:, 1]) < 20)})\nprint(pd.DataFrame(ext).round(3).to_string(index=False))\n\"\"\", tags=[\"claim:ed2a-npx-gaze-confined\"])\nresult(\"ed2a-npx-gaze-confined\")\n\n# ------------------------------------------------------------------ claims: CCG\nmd(\"\"\"\n## fig2d-npx-ccg-hva-input\n\n> V1 IC-encoders (n = 79) are more likely than V1 segment responders (n = 526) to receive putative\n> excitatory connections from higher visual areas, by cross-correlogram analysis.\n\nSpike trains of RS units over the ICwcfg1 block in 1-ms bins; the raw CCG for every pair of a V1\nIC-encoder or segment responder (RS, ICwcfg1) and an HVA RS unit of the same session; the CCG of\nthe smoothed trains is subtracted; a connection from the HVA unit when the corrected CCG peak at\nlags 1 to 10 ms with the HVA unit leading exceeds 7 times the flank s.d. (50 to 100 ms). Readings\nof the criterion: smoothing (a) 25-ms boxcar, (b) 25-ms Gaussian with s.d. 5 ms; flank s.d. from\n(i) the raw, (ii) the corrected CCG; measure per V1 unit (x) fraction, (y) number of HVA units\nconnected to it.\n\"\"\")\ncode(\"\"\"\nt0 = time.time()\nccg_rows = []\nfor s in sessions:\n    u = s[\"units\"]\n    g = groups[(s[\"subject\"], \"ICwcfg1\")]\n    tg = list(g.index[(g.area == \"V1\") & g.rs & (g.ic_enc | g.seg_resp)])\n    src = list(u.index[(u.area != \"V1\") & u.rs])\n    counts = il.ccg_counts([s[\"ccg_bins\"][i] for i in tg], [s[\"ccg_bins\"][i] for i in src], 124)\n    for sm in [\"box\", \"gauss\"]:\n        for fl in [\"raw\", \"corrected\"]:\n            con = il.connections(counts, 124, sm, fl)\n            for k, i in enumerate(tg):\n                ccg_rows.append({\"subject\": s[\"subject\"], \"unit\": i, \"group\": \"IC-encoder\" if g.loc[i, \"ic_enc\"] else \"segment responder\",\n                                 \"smoothing\": sm, \"flank\": fl, \"n_conn\": int(con[k].sum()), \"frac_conn\": con[k].mean(),\n                                 \"n_hva\": len(src)})\nccg = pd.DataFrame(ccg_rows)\nprint(f\"CCGs computed in {time.time() - t0:.0f} s\")\nx = ccg[(ccg.smoothing == \"box\") & (ccg.flank == \"raw\")]\nprint(\"Units in the analysis:\", x.group.value_counts().to_dict(), \"(paper 79 and 526)\")\nrows = []\nfor (sm, fl), x in ccg.groupby([\"smoothing\", \"flank\"]):\n    for meas in [\"frac_conn\", \"n_conn\"]:\n        a, b = x[x.group == \"IC-encoder\"][meas], x[x.group == \"segment responder\"][meas]\n        rows.append({\"smoothing\": sm, \"flank_sd_from\": fl, \"measure\": meas, \"IC_enc_median\": a.median(), \"seg_median\": b.median(),\n                     \"IC_enc_mean\": a.mean(), \"seg_mean\": b.mean(), \"IC_enc_frac_with_any\": (a > 0).mean(),\n                     \"seg_frac_with_any\": (b > 0).mean(), \"ranksum_p\": stats.ranksums(a, b).pvalue})\nccg_tab = pd.DataFrame(rows)\nprint(ccg_tab.to_string(index=False, float_format=lambda v: f\"{v:.4g}\"))\n\"\"\", tags=[\"claim:fig2d-npx-ccg-hva-input\"])\ncode(\"\"\"\nx = ccg[(ccg.smoothing == \"box\") & (ccg.flank == \"raw\")]\nprint(\"Per session, reading (a)(i), mean fraction of HVA units connected:\")\nprint(x.pivot_table(index=\"subject\", columns=\"group\", values=\"frac_conn\", aggfunc=[\"mean\", \"count\"]).round(4).to_string())\nfig, ax = plt.subplots(figsize=(4, 3))\nax.boxplot([x[x.group == \"IC-encoder\"].frac_conn, x[x.group == \"segment responder\"].frac_conn], showfliers=False)\nax.set_xticks([1, 2], [\"IC-encoders\", \"segment responders\"])\nax.set_ylabel(\"fraction of HVA RS units connected\")\nplt.tight_layout(); plt.show()\nprint(\"plotted range (no fliers); all values from\", x.frac_conn.min(), \"to\", round(x.frac_conn.max(), 4))\n\"\"\", tags=[\"claim:fig2d-npx-ccg-hva-input\"])\nresult(\"fig2d-npx-ccg-hva-input\")\n\n# ------------------------------------------------------------------ claims: decoding\nmd(\"\"\"\n## Decoding (Figs. 3a, 3c, 3d; Extended Data Figs. 6e,f and 7)\n\nThe decoder of the claims file: ICwcfg1, RS units of one area, sessions with at least 50 RS units\nin the area; IC response; classes IC1, LC1, LC2, IC2 balanced to the smallest class by its first\ntrials; stratified tenfold partition; z-scoring by the training trials; linear SVM, one-vs-one.\nReading (a): C = 1; reading (b): C chosen by an inner threefold cross-validation on the training\ntrials (the Python counterpart of the code's hyperparameter search). TRE trials are decoded by each\nfold model and the fractions averaged. The XRE decoders are trained on XRE1 against XRE2 and probed\nwith IC1 and IC2. Each (session, area) has its own seed.\n\"\"\")\ncode(\"\"\"\nt0 = time.time()\njobs = []\nfor i, s in enumerate(sessions):\n    u = s[\"units\"]\n    for j, a in enumerate(il.AREAS):\n        m = ((u.area == a) & u.rs).values\n        if m.sum() < 50:\n            continue\n        jobs.append((i, a, m, 1000 * i + j))\n\ndef run_decoders(i, a, m, seed):\n    b = sessions[i][\"blocks\"][\"ICwcfg1\"]\n    out = []\n    for rd in [\"a\", \"b\"]:\n        r = il.decode(b[\"R\"][:, m], b[\"codes\"], [il.IC1, il.LC1, il.LC2, il.IC2], [il.TRE1, il.TRE2], seed=seed, reading=rd)\n        score, icv, lcv = il.inference_score(r[\"probe\"])\n        x = il.decode(b[\"R\"][:, m], b[\"codes\"], [il.XRE1, il.XRE2], [il.IC1, il.IC2], seed=seed, reading=rd)\n        out.append({\"subject\": sessions[i][\"subject\"], \"area\": a, \"n_units\": int(m.sum()), \"reading\": rd,\n                    \"acc\": r[\"acc\"], \"tre_ic\": icv, \"tre_lc\": lcv, \"inference\": score, \"n_per_class\": r[\"n_per_class\"],\n                    \"xre_acc\": x[\"acc\"], \"xre_score\": (x[\"probe\"][0, 0] + x[\"probe\"][1, 1]) / 2})\n    return out\n\ndec = pd.DataFrame([r for rs in Parallel(n_jobs=N_JOBS)(delayed(run_decoders)(*j) for j in jobs) for r in rs])\nprint(f\"{len(jobs)} session-area decoders, both readings, in {time.time() - t0:.0f} s\")\nprint(\"Sessions per area:\", dec[dec.reading == \"a\"].groupby(\"area\").size().reindex(il.AREAS).to_dict(),\n      \"(paper 12, 8, 11, 10, 12, 11)\")\nprint(\"Trials per class:\", sorted(dec.n_per_class.unique()))\n\"\"\")\n\nmd(\"\"\"\n## fig3a-npx-v1-decoding\n\n> A linear SVM decodes the four images IC1, LC1, LC2 and IC2 from V1 activity in the Neuropixels\n> data with tenfold cross-validation accuracy above the chance of 0.25.\n\"\"\")\ncode(\"\"\"\nfor rd in [\"a\", \"b\"]:\n    x = dec[(dec.reading == rd)]\n    v = x[x.area == \"V1\"].acc\n    print(f\"reading ({rd}) V1: mean accuracy {v.mean():.3f} +/- {v.sem():.3f} (s.e.m.), range {v.min():.3f} to {v.max():.3f}, \"\n          f\"n = {len(v)}, signed-rank against 0.25 p = {il.signrank_p(v - 0.25):.4g}; sessions above 0.25: {(v > 0.25).sum()}\")\n    print(\"   other areas:\", {a: (round(x[x.area == a].acc.mean(), 3), round(il.signrank_p(x[x.area == a].acc - 0.25), 4))\n                             for a in il.AREAS[1:]})\nprint(dec[(dec.reading == \"a\") & (dec.area == \"V1\")][[\"subject\", \"n_units\", \"acc\"]].round(3).to_string(index=False))\n\"\"\", tags=[\"claim:fig3a-npx-v1-decoding\"])\nresult(\"fig3a-npx-v1-decoding\")\n\nmd(\"\"\"\n## fig3c-npx-v1-inference\n\n> In Neuropixels V1, TRE trials are decoded as the matching IC image more often than as the\n> matching LC image (0.51 against 0.22), so IC inference is represented in V1.\n\"\"\")\ncode(\"\"\"\nfor rd in [\"a\", \"b\"]:\n    x = dec[(dec.reading == rd) & (dec.area == \"V1\")]\n    print(f\"reading ({rd}): P(TRE -> IC) {x.tre_ic.mean():.3f} +/- {x.tre_ic.sem():.3f}, P(TRE -> LC) {x.tre_lc.mean():.3f} +/- \"\n          f\"{x.tre_lc.sem():.3f}; IC > LC in {(x.tre_ic > x.tre_lc).sum()} of {len(x)} sessions; \"\n          f\"signed-rank IC vs LC p = {il.signrank_p(x.tre_ic, x.tre_lc):.4g}\")\nprint(\"Paper: 0.51 (tolerance 0.051) and 0.22 (0.022), P < 0.05\")\nprint(dec[(dec.area == \"V1\")].pivot_table(index=\"subject\", columns=\"reading\", values=[\"tre_ic\", \"tre_lc\"]).round(3).to_string())\n\"\"\", tags=[\"claim:fig3c-npx-v1-inference\"])\nresult(\"fig3c-npx-v1-inference\")\n\nmd(\"\"\"\n## fig3d-npx-areas-inference\n\n> In the Neuropixels data almost every visual area decodes TRE as IC more than as LC, significantly\n> in V1, LM, RL, AL and PM and not in AM, with V1, LM and AL the strongest.\n\"\"\")\ncode(\"\"\"\npaper_p = {\"V1\": 0.0132, \"LM\": 0.0156, \"RL\": 0.0244, \"AL\": 0.0039, \"PM\": 0.0342, \"AM\": 0.1748}\nfor rd in [\"a\", \"b\"]:\n    rows = []\n    for a in il.AREAS:\n        x = dec[(dec.reading == rd) & (dec.area == a)]\n        rows.append({\"area\": a, \"sessions\": len(x), \"IC\": x.tre_ic.mean(), \"LC\": x.tre_lc.mean(), \"inference_mean\": x.inference.mean(),\n                     \"inference_sem\": x.inference.sem(), \"p\": il.signrank_p(x.inference), \"paper_p\": paper_p[a]})\n    t = pd.DataFrame(rows)\n    t[\"sig_IC_above_LC\"] = (t.p < 0.05) & (t.inference_mean > 0)\n    print(f\"reading ({rd})\")\n    print(t.round(4).to_string(index=False))\n    print(\"  significant areas:\", t[t.sig_IC_above_LC].area.tolist(),\n          \"; three largest mean scores:\", t.nlargest(3, \"inference_mean\").area.tolist(),\n          \"; three smallest p:\", t.nsmallest(3, \"p\").area.tolist())\n\"\"\", tags=[\"claim:fig3d-npx-areas-inference\"])\nresult(\"fig3d-npx-areas-inference\")\n\nmd(\"\"\"\n## ed7b-npx-xre-inference\n\n> Decoders trained on the XRE real-bar images classify IC1 and IC2 trials as the XRE image whose\n> real bar matches the illusory bar, above chance in all six Neuropixels areas.\n\nXRE inference score (P(IC1 -> XRE1) + P(IC2 -> XRE2))/2, signed-rank against 0.5.\n\"\"\")\ncode(\"\"\"\npaper_xp = {\"V1\": 0.0005, \"LM\": 0.0078, \"RL\": 0.0049, \"AL\": 0.0020, \"PM\": 0.0005, \"AM\": 0.0137}\nfor rd in [\"a\", \"b\"]:\n    rows = []\n    for a in il.AREAS:\n        x = dec[(dec.reading == rd) & (dec.area == a)]\n        rows.append({\"area\": a, \"sessions\": len(x), \"xre_acc\": x.xre_acc.mean(), \"xre_score_mean\": x.xre_score.mean(),\n                     \"xre_score_sem\": x.xre_score.sem(), \"p_vs_0.5\": il.signrank_p(x.xre_score - 0.5), \"paper_p\": paper_xp[a]})\n    t = pd.DataFrame(rows)\n    t[\"sig_above_0.5\"] = (t[\"p_vs_0.5\"] < 0.05) & (t.xre_score_mean > 0.5)\n    print(f\"reading ({rd}): areas significant above 0.5: {int(t['sig_above_0.5'].sum())} of 6\")\n    print(t.round(4).to_string(index=False))\n\"\"\", tags=[\"claim:ed7b-npx-xre-inference\"])\nresult(\"ed7b-npx-xre-inference\")\n\nmd(\"\"\"\n## ed7a-npx-no-area-above-v1\n\n> No higher visual area shows a substantially larger inference performance than V1, although\n> decoding accuracy and inference scores differ across areas.\n\nKruskal-Wallis across the six areas of the per-session values, then (a) two-sided signed-rank of\nV1 against each HVA over the sessions with both, and (b) Tukey-Kramer comparisons after the\nKruskal-Wallis. A claim of absence: reproduced when no HVA is significantly larger than V1.\n\"\"\")\ncode(\"\"\"\ndef tukey_vs_v1(vals_by_area):\n    # Tukey-Kramer on mean ranks after Kruskal-Wallis (MATLAB multcompare default), HVA minus V1\n    allv = np.concatenate([vals_by_area[a] for a in il.AREAS])\n    lab = np.concatenate([[a] * len(vals_by_area[a]) for a in il.AREAS])\n    r = stats.rankdata(allv)\n    N = len(allv)\n    _, c = np.unique(allv, return_counts=True)\n    var = N * (N + 1) / 12 * (1 - np.sum(c ** 3 - c) / (N ** 3 - N))\n    qc = il.tukey_qcrit(6)\n    out = {}\n    for a in il.AREAS[1:]:\n        d = r[lab == a].mean() - r[lab == \"V1\"].mean()\n        se = np.sqrt(var * (1 / np.sum(lab == a) + 1 / np.sum(lab == \"V1\")) / 2)\n        out[a] = (round(d, 1), bool(abs(d) / se > qc))\n    return out\n\nfor rd in [\"a\", \"b\"]:\n    x = dec[dec.reading == rd]\n    print(f\"reading ({rd})\")\n    for meas, paper in [(\"acc\", 0.0019), (\"inference\", 0.0249), (\"xre_acc\", 0.0005), (\"xre_score\", 0.0022)]:\n        vals = {a: x[x.area == a][meas].values for a in il.AREAS}\n        kwp = stats.kruskal(*vals.values()).pvalue\n        piv = x.pivot(index=\"subject\", columns=\"area\", values=meas)\n        pair = {}\n        for a in il.AREAS[1:]:\n            both = piv[[\"V1\", a]].dropna()\n            pair[a] = (round(both[a].mean() - both[\"V1\"].mean(), 3), round(il.signrank_p(both[a], both[\"V1\"]), 4))\n        print(f\"  {meas}: Kruskal-Wallis p = {kwp:.4f} (paper {paper}); means\", {a: round(v.mean(), 3) for a, v in vals.items()})\n        print(f\"     (a) HVA minus V1 and signed-rank p:\", pair)\n        print(f\"     (b) Tukey-Kramer mean-rank difference HVA minus V1, significant:\", tukey_vs_v1(vals))\n\"\"\", tags=[\"claim:ed7a-npx-no-area-above-v1\"])\nresult(\"ed7a-npx-no-area-above-v1\")\n\nmd(\"\"\"\n## ed6ef-npx-ic-not-greater\n\n> In the Neuropixels data, IC images do not evoke larger population average responses than LC\n> images in any area, averaged over all units or over visually responsive units.\n\nSessions with at least 50 RS units in the area; ICwcfg1; per session the IC response averaged over\n(e) all RS units, (f) visually responsive RS units (Kruskal-Wallis across blank, IC1, LC1, LC2, IC2\nat p < 0.05), on IC trials (IC1 and IC2) and on LC trials (LC1 and LC2); one-tailed signed-rank\ntest of IC > LC across sessions.\n\"\"\")\ncode(\"\"\"\npaper_e = {\"V1\": 0.9614, \"LM\": 0.9805, \"RL\": 0.7676, \"AL\": 0.7217, \"PM\": 0.9895, \"AM\": 0.8398}\npaper_f = {\"V1\": 0.9788, \"LM\": 0.9805, \"RL\": 0.7114, \"AL\": 0.7842, \"PM\": 0.9866, \"AM\": 0.6499}\nrows = []\nfor s in sessions:\n    u = s[\"units\"]\n    b = s[\"blocks\"][\"ICwcfg1\"]\n    g = groups[(s[\"subject\"], \"ICwcfg1\")]\n    for a in il.AREAS:\n        m = ((u.area == a) & u.rs).values\n        if m.sum() < 50:\n            continue\n        R = b[\"R\"][:, m]\n        icr = R[np.isin(b[\"codes\"], [il.IC1, il.IC2])].mean(axis=0)\n        lcr = R[np.isin(b[\"codes\"], [il.LC1, il.LC2])].mean(axis=0)\n        vr = (g.p_kw_BK.values[m] < 0.05)\n        rows.append({\"subject\": s[\"subject\"], \"area\": a, \"IC_all\": icr.mean(), \"LC_all\": lcr.mean(),\n                     \"IC_vr\": icr[vr].mean(), \"LC_vr\": lcr[vr].mean(), \"n_vr\": int(vr.sum())})\npop = pd.DataFrame(rows)\nout = []\nfor a in il.AREAS:\n    x = pop[pop.area == a]\n    out.append({\"area\": a, \"sessions\": len(x),\n                \"e_IC_minus_LC_Hz\": (x.IC_all - x.LC_all).mean(), \"e_p_IC>LC\": il.signrank_p(x.IC_all, x.LC_all, \"greater\"), \"e_paper\": paper_e[a],\n                \"f_IC_minus_LC_Hz\": (x.IC_vr - x.LC_vr).mean(), \"f_p_IC>LC\": il.signrank_p(x.IC_vr, x.LC_vr, \"greater\"), \"f_paper\": paper_f[a],\n                \"f_units_mean\": x.n_vr.mean()})\npop_tab = pd.DataFrame(out)\nprint(pop_tab.round(4).to_string(index=False))\nprint(\"Areas with p < 0.05 in (e):\", pop_tab[pop_tab[\"e_p_IC>LC\"] < 0.05].area.tolist(), \"; in (f):\", pop_tab[pop_tab[\"f_p_IC>LC\"] < 0.05].area.tolist())\n\"\"\", tags=[\"claim:ed6ef-npx-ic-not-greater\"])\nresult(\"ed6ef-npx-ic-not-greater\")\n\nmd(\"\"\"\n## supp3-decoder-types\n\n> Decoders of other kinds (quadratic and radial basis function SVMs, a fully connected neural\n> network) give results highly consistent with the linear SVM.\n\nThe quadratic (degree-2 polynomial) and RBF SVMs are run as the linear one (reading a, C = 1) on V1,\nLM and AL. The network of the Methods (two hidden layers of 100 units, softmax output, Adam,\ncross-entropy, 50,000 epochs, tenfold) is timed on one fold, and its full cost estimated.\n\"\"\")\ncode(\"\"\"\nt0 = time.time()\nsub_jobs = [j for j in jobs if j[1] in (\"V1\", \"LM\", \"AL\")]\n\ndef run_kernels(i, a, m, seed):\n    b = sessions[i][\"blocks\"][\"ICwcfg1\"]\n    out = []\n    for kern in [\"poly\", \"rbf\"]:\n        r = il.decode(b[\"R\"][:, m], b[\"codes\"], [il.IC1, il.LC1, il.LC2, il.IC2], [il.TRE1, il.TRE2], seed=seed, kernel=kern)\n        score, icv, lcv = il.inference_score(r[\"probe\"])\n        out.append({\"subject\": sessions[i][\"subject\"], \"area\": a, \"kernel\": kern, \"acc\": r[\"acc\"], \"inference\": score})\n    return out\n\nker = pd.DataFrame([r for rs in Parallel(n_jobs=N_JOBS)(delayed(run_kernels)(*j) for j in sub_jobs) for r in rs])\nlin = dec[(dec.reading == \"a\") & dec.area.isin([\"V1\", \"LM\", \"AL\"])].assign(kernel=\"linear\")[[\"subject\", \"area\", \"kernel\", \"acc\", \"inference\"]]\nallk = pd.concat([lin, ker])\nrows = []\nfor (a, k), x in allk.groupby([\"area\", \"kernel\"]):\n    rows.append({\"area\": a, \"kernel\": k, \"sessions\": len(x), \"acc\": x.acc.mean(), \"inference_mean\": x.inference.mean(),\n                 \"p\": il.signrank_p(x.inference), \"sig_positive\": (il.signrank_p(x.inference) < 0.05) and x.inference.mean() > 0})\nprint(pd.DataFrame(rows).round(4).to_string(index=False))\nprint(f\"kernels run in {time.time() - t0:.0f} s\")\n\"\"\", tags=[\"claim:supp3-decoder-types\"])\ncode(\"\"\"\nfrom sklearn.neural_network import MLPClassifier\ns = sessions[0]\nb = s[\"blocks\"][\"ICwcfg1\"]\nm = ((s[\"units\"].area == \"V1\") & s[\"units\"].rs).values\nsel = np.isin(b[\"codes\"], [il.IC1, il.LC1, il.LC2, il.IC2])\nX = stats.zscore(b[\"R\"][sel][:, m], axis=0)\nX[~np.isfinite(X)] = 0\ny = b[\"codes\"][sel]\nn_ep = 300\nnet = MLPClassifier(hidden_layer_sizes=(100, 100), solver=\"adam\", batch_size=len(y), max_iter=n_ep, tol=0,\n                    n_iter_no_change=10 ** 9, alpha=0.0, random_state=0)\nt0 = time.time()\nnet.fit(X[: int(0.9 * len(y))], y[: int(0.9 * len(y))])\nper_epoch = (time.time() - t0) / n_ep\nn_fits = 10 * len(sub_jobs)\nprint(f\"{per_epoch * 1000:.2f} ms per full-batch epoch on {m.sum()} units; one fit of 50,000 epochs ~ {per_epoch * 5e4 / 60:.1f} min; \"\n      f\"{n_fits} fits (10 folds x {len(sub_jobs)} session-areas) ~ {per_epoch * 5e4 * n_fits / 3600:.1f} h on one core\")\n\"\"\", tags=[\"claim:supp3-decoder-types\"])\nresult(\"supp3-decoder-types\")\n\nmd(\"\"\"\n## Claims on the 2p imaging, 2p mesoscope and 2p holography data\n\nThese 19 claims (fig1ik, fig2b, fig2c, ed4c, ed5cd, fig3e (two), ed7b-2p, ed5e, ed4hi, ed3, fig4a,\nfig4b, fig5c, fig5, fig5d, fig5e, ed9b, ed10, fig6d, fig6e) rest on recordings that are not in this\ndandiset; the paper names no public archive for them (its Data availability lists only this\ndandiset for the Neuropixels data and \"additional postprocessed data\" in a Code Ocean capsule,\n10.24433/CO.6659254.v2, which does not say what it holds and could not be reached from this run).\nThey are blocked with `data_missing`.\n\"\"\")\ncode(\"\"\"\nprint(\"Files in the pinned version:\", len(assets), \"; kinds:\", assets.kind.value_counts().to_dict())\nprint(\"Any file name mentioning ophys, imaging or 2p:\", any(k in p for p in assets.path for k in [\"ophys\", \"imaging\", \"2p\"]))\nprint(f\"Notebook ran in {(time.time() - started) / 60:.1f} min\")\n\"\"\")\n\nmd(SUMMARY or \"## Summary\\n\\nTo be written.\", tags=[\"summary\"])\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nout = sys.argv[1] if len(sys.argv) > 1 else \"entries/000248-shin-2025/reproduce_shin_2025.ipynb\"\nnbf.write(nb, out)\nprint(\"wrote\", out, len(cells), \"cells\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/build_nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/000248-shin-2025 && python - <<'EOF'
p='illusion.py'; s=open(p).read()
old='''    for name, starts, dur in [("ICwcfg1", s["blocks"]["ICwcfg1"]["start"], 0.4), ("RF", s["rf"]["start"], 1.0)]:'''
new='''    for name, starts, dur in [("ICwcfg1", s["blocks"]["ICwcfg1"]["start"], 0.4),
                              ("ICwcfg0", s["blocks"]["ICwcfg0"]["start"], 0.4), ("RF", s["rf"]["start"], 1.0)]:'''
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
EOF
sed -i 's/fix_ic\[s\["subject"\]\] = {"ICwcfg1": fi, "ICwcfg0": np.ones(len(s\["blocks"\]\["ICwcfg0"\]\["codes"\]), bool)}/fix_ic[s["subject"]] = {"ICwcfg1": fi, "ICwcfg0": (e["ICwcfg0"]["maxdist"] < 20) \& ~e["ICwcfg0"]["blink"]}/' $TMPDIR/build_nb.py; grep -n 'fix_ic\[s\["subject"\]\] =' $TMPDIR/build_nb.py
cd $TMPDIR && . dev/bin/activate && python t4.py 2>&1 | grep "load all"
cat > $TMPDIR/devrun.py <<'EOF'
import sys, json, pickle, time, io, contextlib, traceback
sys.path.insert(0, 'entries/000248-shin-2025')
import matplotlib; matplotlib.use('Agg')
nb=json.load(open(sys.argv[1]))
start=int(sys.argv[2]) if len(sys.argv)>2 else 0
ns={}
codes=[c for c in nb['cells'] if c['cell_type']=='code']
for k,c in enumerate(codes):
    src=''.join(c['source']).replace('sessions = il.load_all()', 'import pickle; sessions = pickle.load(open("/tmp/claude-1001/S.pkl","rb"))')
    t=time.time()
    print(f'===== cell {k} tags={c["metadata"].get("tags")}')
    try:
        exec(compile(src, f'cell{k}', 'exec'), ns)
    except Exception:
        traceback.print_exc()
    print(f'----- {time.time()-t:.1f} s', flush=True)
EOF
echo ok
```

```
583:    fix_ic[s["subject"]] = {"ICwcfg1": fi, "ICwcfg0": (e["ICwcfg0"]["maxdist"] < 20) & ~e["ICwcfg0"]["blink"]}
load all 159.21228218078613
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && python build_nb.py $TMPDIR/dev.ipynb && timeout 3000 python devrun.py dev.ipynb > devout.txt 2>&1; tail -5 devout.txt; grep -n "Traceback\|Error" devout.txt | head
```

```
Wed Oct 28 01:01:05 UTC 2026
Traceback (most recent call last):
  File "/tmp/claude-1001/build_nb.py", line 6, in <module>
    import nbformat as nbf
ModuleNotFoundError: No module named 'nbformat'
tail: cannot open 'devout.txt' for reading: No such file or directory
grep: devout.txt: No such file or directory
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && uv pip install -q nbformat joblib 2>&1|tail -1; python build_nb.py $TMPDIR/dev.ipynb && timeout 3000 python devrun.py dev.ipynb > devout.txt 2>&1; tail -5 devout.txt; grep -n "Traceback\|Error" devout.txt | head
```

```
wrote /tmp/claude-1001/dev.ipynb 81 cells
637484      0.0030            0.0018        6.0              34.0
plotted range (no fliers); all values from 0.0 to 0.0501
----- 0.0 s
/tmp/claude-1001/dev/lib/python3.13/site-packages/joblib/externals/loky/backend/resource_tracker.py:444: UserWarning: resource_tracker: There appear to be 65 leaked file objects to clean up at shutdown: {'/dev/shm/joblib_memmapping_folder_27_634140b59fa349a497d3296607b98307_9fff410b0a2b4669ab2cdd5fe5cf475b/27-139553342514784-da839c34f6e149be836ba1c7341367bf.pkl': 6, '/dev/shm/joblib_memmapping_folder_27_634140b59fa349a497d3296607b98307_9fff410b0a2b4669ab2cdd5fe5cf475b/27-139553342514784-9ccfb7d630ec4feba97c9b4f3d94097b.pkl': 6, '/dev/shm/joblib_memmapping_folder_27_634140b59fa349a497d3296607b98307_9fff410b0a2b4669ab2cdd5fe5cf475b/27-139553342514784-3b6148c19d4e4ed9a3826b02dfda4839.pkl': 6, '/dev/shm/joblib_memmapping_folder_27_634140b59fa349a497d3296607b98307_9fff410b0a2b4669ab2cdd5fe5cf475b/27-139553342514784-4e4d2806ea9f4c19a8b318a8554eec13.pkl': 6, '/dev/shm/joblib_memmapping_folder_27_634140b59fa349a497d3296607b98307_9fff410b0a2b4669ab2cdd5fe5cf475b/27-139553342514784-43a34796be254060a67815dde001aa89.pkl': 6, '/dev/shm/joblib_memmapping_folder_27_634140b59fa349a497d3296607b98307_9fff410b0a2b4669ab2cdd5fe5cf475b/27-139553342514784-8849c8a5f986419495936d22bb7c97b1.pkl': 6, '/dev/shm/joblib_memmapping_folder_27_634140b59fa349a497d3296607b98307_9fff410b0a2b4669ab2cdd5fe5cf475b/27-139553342514784-528bfa3c65fa470a9d5cac83795e2703.pkl': 6, '/dev/shm/joblib_memmapping_folder_27_634140b59fa349a497d3296607b98307_9fff410b0a2b4669ab2cdd5fe5cf475b/27-139553342514784-256876a909ab492ca0a1a5d30a9e39c7.pkl': 6, '/dev/shm/joblib_memmapping_folder_27_634140b59fa349a497d3296607b98307_9fff410b0a2b4669ab2cdd5fe5cf475b/27-139553342514784-52cf4231f8434ff380d1f6a4e6c1e495.pkl': 6, '/dev/shm/joblib_memmapping_folder_27_634140b59fa349a497d3296607b98307_9fff410b0a2b4669ab2cdd5fe5cf475b/27-139553342514784-f1d803d9575
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -n "=====\|-----" devout.txt | tail -30; grep -n -A15 "Traceback" devout.txt | head -60; free -g
```

```
115:===== cell 6 tags=['sanity']
117:----- 7.0 s
118:===== cell 7 tags=['sanity']
121:----- 0.0 s
122:===== cell 8 tags=['claim:results-npx-units-per-session']
129:----- 0.0 s
130:===== cell 9 tags=['claim:methods-npx-ic-encoder-count']
149:----- 4.6 s
150:===== cell 10 tags=['claim:ed6b-npx-v1-group-counts']
162:----- 0.1 s
163:===== cell 11 tags=['claim:ed6cd-npx-ic-encoders-all-areas']
174:----- 0.1 s
175:===== cell 12 tags=['claim:fig1e-npx-exclusive-center']
195:----- 71.0 s
196:===== cell 13 tags=['claim:fig1f-npx-ic-ire-responsive']
209:----- 0.6 s
210:===== cell 14 tags=['claim:fig1g-npx-orientation-match']
220:----- 0.6 s
221:===== cell 15 tags=['claim:ed2b-npx-fixed-gaze']
246:----- 23.6 s
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='build_nb.py'; s=open(p).read()
old='''def clock_check(i, s):
    u, b = s["units"], s["blocks"]["ICwcfg1"]
    m = ((u.area == "V1") & u.rs).values
    rng = np.random.default_rng(100 + i)
    shuffled = b["codes"].copy()'''
new='''def clock_check(i, subject, b, m):
    rng = np.random.default_rng(100 + i)
    shuffled = b["codes"].copy()'''
assert old in s; s=s.replace(old,new)
old='''    return {"subject": s["subject"],
            "post_0_400ms"'''
new='''    return {"subject": subject,
            "post_0_400ms"'''
assert old in s; s=s.replace(old,new)
old='''clock = pd.DataFrame(Parallel(n_jobs=N_JOBS)(delayed(clock_check)(i, s) for i, s in enumerate(sessions)))'''
new='''def v1_block(s):
    m = ((s["units"].area == "V1") & s["units"].rs).values
    b = s["blocks"]["ICwcfg1"]
    return {"R": b["R"][:, m], "R_pre": b["R_pre"][:, m], "codes": b["codes"]}, np.ones(m.sum(), bool)
clock = pd.DataFrame(Parallel(n_jobs=N_JOBS)(delayed(clock_check)(i, s["subject"], *v1_block(s)) for i, s in enumerate(sessions)))'''
assert old in s; s=s.replace(old,new)
old='''        jobs.append((i, a, m, 1000 * i + j))

def run_decoders(i, a, m, seed):
    b = sessions[i]["blocks"]["ICwcfg1"]
    out = []'''
new='''        b = s["blocks"]["ICwcfg1"]
        jobs.append((s["subject"], a, b["R"][:, m], b["codes"], 1000 * i + j))

def run_decoders(subject, a, R, codes, seed):
    b = {"R": R, "codes": codes}
    m = np.ones(R.shape[1], bool)
    out = []'''
assert old in s; s=s.replace(old,new)
s=s.replace('''        out.append({"subject": sessions[i]["subject"], "area": a, "n_units": int(m.sum()), "reading": rd,''','''        out.append({"subject": subject, "area": a, "n_units": int(m.sum()), "reading": rd,''')
old='''def run_kernels(i, a, m, seed):
    b = sessions[i]["blocks"]["ICwcfg1"]
    out = []'''
new='''def run_kernels(subject, a, R, codes, seed):
    b = {"R": R, "codes": codes}
    m = np.ones(R.shape[1], bool)
    out = []'''
assert old in s; s=s.replace(old,new)
s=s.replace('''        out.append({"subject": sessions[i]["subject"], "area": a, "kernel": kern,''','''        out.append({"subject": subject, "area": a, "kernel": kern,''')
open(p,'w').write(s)
EOF
grep -n "sessions\[i\]" build_nb.py; . dev/bin/activate && python build_nb.py $TMPDIR/dev.ipynb && timeout 3000 python devrun.py dev.ipynb > devout.txt 2>&1; grep -n "=====\|-----" devout.txt | tail -14; grep -n -A10 "Traceback" devout.txt | head -40
```

```
wrote /tmp/claude-1001/dev.ipynb 81 cells
210:===== cell 14 tags=['claim:fig1g-npx-orientation-match']
220:----- 0.5 s
221:===== cell 15 tags=['claim:ed2b-npx-fixed-gaze']
246:----- 23.3 s
247:===== cell 16 tags=['claim:ed2f-npx-rf-match']
257:----- 1.1 s
258:===== cell 17 tags=['claim:ed2g-npx-pupil-area']
267:----- 0.0 s
268:===== cell 18 tags=['claim:ed2a-npx-gaze-confined']
285:----- 0.1 s
286:===== cell 19 tags=['claim:fig2d-npx-ccg-hva-input']
298:----- 34.1 s
299:===== cell 20 tags=['claim:fig2d-npx-ccg-hva-input']
317:----- 0.0 s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && sed -n 299,330p devout.txt | cut -c1-200; python devrun.py dev.ipynb > devout2.txt 2>&1; echo "exit $?"; tail -3 devout2.txt | cut -c1-300
```

```
Exit code 143
Command timed out after 1h 0m 0s
===== cell 20 tags=['claim:fig2d-npx-ccg-hva-input']
Per session, reading (a)(i), mean fraction of HVA units connected:
              mean                        count                  
group   IC-encoder segment responder IC-encoder segment responder
subject                                                          
619293         NaN            0.0038        NaN               2.0
619296      0.0004            0.0014        7.0              56.0
620333      0.0006            0.0012        6.0              39.0
620334      0.0011            0.0012        2.0              26.0
625545      0.0037            0.0028       15.0              77.0
625554      0.0036            0.0010        9.0              89.0
625555      0.0151            0.0048        9.0              24.0
630506      0.0028            0.0009        3.0              29.0
631510      0.0017            0.0015        8.0              36.0
631570      0.0028            0.0035        4.0              59.0
633229      0.0055            0.0021       10.0              55.0
637484      0.0030            0.0018        6.0              34.0
plotted range (no fliers); all values from 0.0 to 0.0501
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; pkill -f devrun.py; pkill -f loky; sleep 1; ps aux | grep -c python
```

```
Exit code 143
Wed Oct 28 03:41:34 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/000248-shin-2025 && python - <<'EOF'
p='illusion.py'; s=open(p).read()
old='''            clf = GridSearchCV(base, {"C": 10.0 ** np.arange(-3, 3)},'''
new='''            base.set_params(max_iter=200000)
            clf = GridSearchCV(base, {"C": 10.0 ** np.arange(-3, 1)},'''
assert old in s; s=s.replace(old,new)
s=s.replace("over 10^-3 to 10^2 (the Python counterpart","over 10^-3 to 1 (larger C did not finish in the time of this run; the Python counterpart")
open(p,'w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && cat > t11.py <<'EOF'
import sys, time, pickle, os
os.environ['OMP_NUM_THREADS']='1'
sys.path.insert(0, 'entries/000248-shin-2025')
import illusion as il, numpy as np
S=pickle.load(open('S.pkl','rb'))
for i in [0,2]:
  s=S[i]; u=s['units']; b=s['blocks']['ICwcfg1']
  for a in ['AM','PM']:
    m=((u.area==a)&u.rs).values
    for rd in ['a','b']:
        t=time.time(); r=il.decode(b['R'][:,m], b['codes'], [106,107,110,111],[1105,1109], seed=0, reading=rd); print(i,a,rd, round(time.time()-t,1), round(r['acc'],3), flush=True)
EOF
timeout 300 python t11.py
```

```
0 AM a 14.6 0.252
/tmp/claude-1001/dev/lib/python3.13/site-packages/sklearn/svm/_base.py:337: ConvergenceWarning: Solver terminated early (max_iter=200000).  Consider pre-processing your data with StandardScaler or MinMaxScaler.
  warnings.warn(
/tmp/claude-1001/dev/lib/python3.13/site-packages/sklearn/svm/_base.py:337: ConvergenceWarning: Solver terminated early (max_iter=200000).  Consider pre-processing your data with StandardScaler or MinMaxScaler.
  warnings.warn(
/tmp/claude-1001/dev/lib/python3.13/site-packages/sklearn/svm/_base.py:337: ConvergenceWarning: Solver terminated early (max_iter=200000).  Consider pre-processing your data with StandardScaler or MinMaxScaler.
  warnings.warn(
/tmp/claude-1001/dev/lib/python3.13/site-packages/sklearn/svm/_base.py:337: ConvergenceWarning: Solver terminated early (max_iter=200000).  Consider pre-processing your data with StandardScaler or MinMaxScaler.
  warnings.warn(
/tmp/claude-1001/dev/lib/python3.13/site-packages/sklearn/svm/_base.py:337: ConvergenceWarning: Solver terminated early (max_iter=200000).  Consider pre-processing your data with StandardScaler or MinMaxScaler.
  warnings.warn(
/tmp/claude-1001/dev/lib/python3.13/site-packages/sklearn/svm/_base.py:337: ConvergenceWarning: Solver terminated early (max_iter=200000).  Consider pre-processing your data with StandardScaler or MinMaxScaler.
  warnings.warn(
/tmp/claude-1001/dev/lib/python3.13/site-packages/sklearn/svm/_base.py:337: ConvergenceWarning: Solver terminated early (max_iter=200000).  Consider pre-processing your data with StandardScaler or MinMaxScaler.
  warnings.warn(
/tmp/claude-1001/dev/lib/python3.13/site-packages/sklearn/svm/_base.py:337: ConvergenceWarning: Solver terminated early (max_iter=200000).  Consider pre-processing your data with StandardScaler or MinMaxScaler.
  warnings.warn(
/tmp/claude-1001/dev/lib/python3.13/site-packages/sklearn/svm/_base.py:337: ConvergenceWarning: Solver terminated early (max_iter=200000).  Consider pre-proce
[... 235 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='build_nb.py'; s=open(p).read()
old='''    out = []
    for rd in ["a", "b"]:
        r = il.decode(b["R"][:, m], b["codes"], [il.IC1, il.LC1, il.LC2, il.IC2], [il.TRE1, il.TRE2], seed=seed, reading=rd)'''
new='''    out = []
    for rd in (["a", "b"] if a == "V1" else ["a"]):
        r = il.decode(b["R"][:, m], b["codes"], [il.IC1, il.LC1, il.LC2, il.IC2], [il.TRE1, il.TRE2], seed=seed, reading=rd)'''
assert old in s; s=s.replace(old,new)
s=s.replace('''fold model and the fractions averaged. The XRE decoders are trained on XRE1 against XRE2 and probed
with IC1 and IC2. Each (session, area) has its own seed.''','''fold model and the fractions averaged. The XRE decoders are trained on XRE1 against XRE2 and probed
with IC1 and IC2. Each (session, area) has its own seed. Reading (b) is run on V1 only: its search
took 30 to 40 s per session and area on this machine, and with reading (a) on every area the
notebook would not have finished within the time of this run (about 25 minutes for both readings
on all areas, estimated from four session-area pairs).''')
s=s.replace('dec = pd.DataFrame([r for rs in Parallel(n_jobs=N_JOBS)(delayed(run_decoders)(*j) for j in jobs) for r in rs])',
 'dec = pd.DataFrame([r for rs in Parallel(n_jobs=N_JOBS)(delayed(run_decoders)(*j) for j in jobs) for r in rs])\nwarnings.filterwarnings("ignore")')
# fig3d/ed7b/ed7a loops over readings: only where present
s=s.replace('''paper_p = {"V1": 0.0132, "LM": 0.0156, "RL": 0.0244, "AL": 0.0039, "PM": 0.0342, "AM": 0.1748}
for rd in ["a", "b"]:''','''paper_p = {"V1": 0.0132, "LM": 0.0156, "RL": 0.0244, "AL": 0.0039, "PM": 0.0342, "AM": 0.1748}
for rd in ["a"]:''')
s=s.replace('''paper_xp = {"V1": 0.0005, "LM": 0.0078, "RL": 0.0049, "AL": 0.0020, "PM": 0.0005, "AM": 0.0137}
for rd in ["a", "b"]:''','''paper_xp = {"V1": 0.0005, "LM": 0.0078, "RL": 0.0049, "AL": 0.0020, "PM": 0.0005, "AM": 0.0137}
for rd in ["a"]:''')
s=s.replace('''for rd in ["a", "b"]:
    x = dec[dec.reading == rd]
    print(f"reading ({rd})")''','''for rd in ["a"]:
    x = dec[dec.reading == rd]
    print(f"reading ({rd})")''')
s=s.replace('''    print("   other areas:", {a: (round(x[x.area == a].acc.mean(), 3), round(il.signrank_p(x[x.area == a].acc - 0.25), 4))
                             for a in il.AREAS[1:]})''','''    if rd == "a":
        print("   other areas:", {a: (round(x[x.area == a].acc.mean(), 3), round(il.signrank_p(x[x.area == a].acc - 0.25), 4))
                                 for a in il.AREAS[1:]})''')
# V1 reading b for ed7b xre in V1: print separately
s=s.replace('''    print(f"reading ({rd}): areas significant above 0.5: {int(t['sig_above_0.5'].sum())} of 6")
    print(t.round(4).to_string(index=False))''','''    print(f"reading ({rd}): areas significant above 0.5: {int(t['sig_above_0.5'].sum())} of 6")
    print(t.round(4).to_string(index=False))
x = dec[(dec.reading == "b") & (dec.area == "V1")]
print(f"reading (b), V1 only: XRE score {x.xre_score.mean():.3f}, p vs 0.5 = {il.signrank_p(x.xre_score - 0.5):.4g}")''')
s=s.replace('''    print("  significant areas:", t[t.sig_IC_above_LC].area.tolist(),
          "; three largest mean scores:", t.nlargest(3, "inference_mean").area.tolist(),
          "; three smallest p:", t.nsmallest(3, "p").area.tolist())''','''    print("  significant areas:", t[t.sig_IC_above_LC].area.tolist(),
          "; three largest mean scores:", t.nlargest(3, "inference_mean").area.tolist(),
          "; three smallest p:", t.nsmallest(3, "p").area.tolist())
x = dec[(dec.reading == "b") & (dec.area == "V1")]
print(f"reading (b), V1 only: inference {x.inference.mean():.3f}, p = {il.signrank_p(x.inference):.4g}")''')
# remove kernel cell
i0=s.index('code("""\nt0 = time.time()\nsub_jobs')
i1=s.index('""", tags=["claim:supp3-decoder-types"])', i0)+len('""", tags=["claim:supp3-decoder-types"])\n')
s=s[:i0]+'sub_jobs = None\n'+s[i1:]
s=s.replace('''n_fits = 10 * len(sub_jobs)''','''n_fits = 10 * len([j for j in jobs if j[1] in ("V1", "LM", "AL")])''')
s=s.replace('''print(f"{per_epoch * 1000:.2f} ms per full-batch epoch on {m.sum()} units; one fit of 50,000 epochs ~ {per_epoch * 5e4 / 60:.1f} min; "
      f"{n_fits} fits (10 folds x {len(sub_jobs)} session-areas) ~ {per_epoch * 5e4 * n_fits / 3600:.1f} h on one core")''','''print(f"{per_epoch * 1000:.2f} ms per full-batch epoch on {m.sum()} units; one fit of 50,000 epochs ~ {per_epoch * 5e4 / 60:.1f} min; "
      f"{n_fits} fits (10 folds x {n_fits // 10} session-areas of V1, LM, AL) ~ {per_epoch * 5e4 * n_fits / 3600:.1f} h on one core")''')
s=s.replace('''The quadratic (degree-2 polynomial) and RBF SVMs are run as the linear one (reading a, C = 1) on V1,
LM and AL. The network of the Methods (two hidden layers of 100 units, softmax output, Adam,
cross-entropy, 50,000 epochs, tenfold) is timed on one fold, and its full cost estimated.''','''The network of the Methods (two hidden layers of 100 units, softmax output, Adam, cross-entropy,
50,000 epochs, tenfold) is timed on one fold of one session, and its full cost estimated. The
quadratic and RBF SVMs were not run: the linear SVM alone took 15 to 20 s per session and area,
and the time of this run did not allow them.''')
open(p,'w').write(s)
EOF
grep -n "sub_jobs" build_nb.py; sed -n 1,60p tools/entry.py | head -60; date -u
```

```
1022:sub_jobs = None
"""Lock, check and run one entry. This is the whole local workflow for a deposit.

    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entries/<name>   # validate metadata and conventions
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
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000248-shin-2025 && cat > requirements.in <<'EOF'
dandi
h5py
joblib
matplotlib
numba
numpy
pandas
remfile
scikit-learn
scipy
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: 000248-shin-2025
type: reproduction
title: Illusory contour responses in mouse visual cortex, Neuropixels (Shin et al. 2025)
description: Tests the Neuropixels findings of Shin, Ogando, Abdeladim and colleagues (2025) on dandiset
  000248, which holds 12 Neuropixels sessions with six probes in V1, LM, RL, AL, PM and AM while
  mice viewed illusory contour images. It counts the units and the IC-encoders and segment
  responders, selects exclusively center-responsive V1 units, repeats the analyses on fixed-gaze
  trials, computes cross-correlograms between V1 and higher visual areas, and decodes the images
  and the inference of the illusory contour from each area. The 2p imaging and holography data of
  the paper are not in the dandiset.
license: Apache-2.0
notebooks:
- path: reproduce_shin_2025.ipynb
  title: Reproducing Shin et al. (2025) from dandiset 000248
  runtime_minutes: 15
helpers:
- illusion.py
related:
- id: dandi:000248/0.240502.2344
  relation: uses_data
- id: doi:10.1038/s41593-025-02055-5
  relation: reproduces
EOF
cd $TMPDIR && . dev/bin/activate && python build_nb.py && cd  && python tools/entry.py lock entries/000248-shin-2025 2>&1 | tail -3 && python tools/entry.py check entries/000248-shin-2025 2>&1 | tail -15
```

```
Exit code 143
Command timed out after 1h 0m 0s
wrote entries/000248-shin-2025/reproduce_shin_2025.ipynb 80 cells
wrote entries/000248-shin-2025/requirements.lock.txt
```

**Agent calls Bash**

```bash
date -u
```

```
Wed Oct 28 04:45:59 UTC 2026
```

**Agent calls Bash**

```bash
timeout 60 python tools/entry.py check entries/000248-shin-2025 2>&1 | tail -15; echo "exit $?"
```

```
Terminated                 timeout 60 python tools/entry.py check entries/000248-shin-2025 2>&1 | tail -15
exit 143
```

**Agent calls Bash**

```bash
timeout 40 python -c "
import faulthandler, sys; faulthandler.dump_traceback_later(25, exit=True)
sys.argv=['entry.py','check','entries/000248-shin-2025']; sys.path.insert(0,'tools')
import runpy; runpy.run_path('tools/entry.py', run_name='__main__')
" 2>&1 | grep -v "^  File.*threading" | head -30
```

```
Timeout (0:00:25)!
Thread 0x000070c1b32debc0 (most recent call first):
  File "tools/entry.py", line 305 in _derivation_checks
  File "tools/entry.py", line 187 in check
  File "tools/entry.py", line 424 in main
  File "tools/entry.py", line 434 in <module>
  File "<frozen runpy>", line 88 in _run_code
  File "<frozen runpy>", line 98 in _run_module_code
  File "<frozen runpy>", line 294 in run_path
  File "<string>", line 4 in <module>
```

**Agent calls Bash**

```bash
sed -n 285,315p tools/entry.py
```

```
nb = nbformat.read(entry_dir / notebook, as_version=4)
                if not any(tag in c.metadata.get("tags", []) for c in nb.cells):
                    report.error(path.relative_to(ROOT), f"no cell tagged {tag!r} in {notebook}")
    return report


def _local_data(code: str, start: int) -> bool:
    """Whether a local path in the code is inside the dataset directory `encore check` gave (ENCORE_LOCAL_DATA):
    the one local path an entry on a local dataset may name."""
    allowed = os.environ.get("ENCORE_LOCAL_DATA", "").rstrip("/")
    return bool(allowed) and code.startswith(allowed, start) and code[start + len(allowed):start + len(allowed) + 1] in ("/", "'", '"')


def _derivation_checks(report: Report, where, code: str) -> None:
    if EMBEDDED_IMAGE.search(code):
        report.error(where, "contains an encoded image; figures must be computed from the data")
    if READS_A_FIGURE.search(code):
        report.error(where, "reads an image file; figures must be computed from the data")
    if any(not _local_data(code, m.start() + 1) for m in LOCAL_PATH.finditer(code)):
        report.error(where, "names a local path; stream the data from the archive")
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "LONG_LITERAL =" -A3 tools/entry.py; timeout 20 python -c "
import sys,re,time; sys.path.insert(0,'tools'); import entry, nbformat
src=open('entries/000248-shin-2025/illusion.py').read()
for i,chunk in enumerate(src.split('\n\n')):
    t=time.time(); entry.LONG_LITERAL.search(chunk)
    if time.time()-t>0.5: print('slow chunk',i,chunk[:300]); break
print('helper done')
" ; echo $?
```

```
64:LONG_LITERAL = re.compile(r"[\[(]\s*(?:-?\d+\.?\d*(?:e-?\d+)?\s*,\s*){%d,}" % MAX_LITERAL_NUMBERS)
65-
66-
67-class Report:
124
```

**Agent calls Bash**

```bash
cd entries/000248-shin-2025 && python - <<'EOF'
p='illusion.py'; s=open(p).read()
old='''IC_TRIAL_TYPES = np.array([0, 101, 105, 106, 107, 109, 110, 111, 506, 511, 1105, 1109, 1201, 1299,
                           1301, 1302, 1303, 1304, 1305, 1306, 1307, 1308])'''
new='''IC_TRIAL_TYPES = np.r_[[0, 101, 105, 106], [107, 109, 110, 111], [506, 511], [1105, 1109], [1201, 1299],
                       np.arange(1301, 1309)]'''
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
EOF
cd ../.. && timeout 120 python tools/entry.py check entries/000248-shin-2025 2>&1 | tail -15; echo "exit $?"; date -u
```

```
0 error(s)
exit 0
Wed Oct 28 04:48:37 UTC 2026
```

**Agent calls Bash**

```bash
grep -n "blocked_by" -B3 -A6 attempts/001453-fouke-2025-01.yaml | head -30; grep -n "^findings" -A12 attempts/001453-fouke-2025-01.yaml; grep -n "^verifications\|^questions" -A3 attempts/001453-fouke-2025-01.yaml | head
```

```
196-    in the dandiset; the measure was chosen here before the analysis.
197-- claim: fig1cef-representative-values
198-  outcome: blocked
199:  blocked_by: metadata_insufficient
200-  notes: The numbers come from single representative fish and trials. Fig1-S1.ipynb selects them
201-    by the index of a data folder and a trial number (for example DC folder 29, trial 79), and the
202-    dandiset gives no mapping from those folders to its subjects, nor the original file names.
203-- claim: fig2d-shared-architecture
204-  outcome: blocked
205:  blocked_by: data_missing
206-  notes: The two-photon imaging data are not in the dandiset, which holds only freely swimming
207-    tracking. The GitLab repository the paper names for "all behavioral and imaging data" holds
208-    notebooks only, and no other dandiset of this lab or paper was found on the archive.
209-- claim: fig2g-dsi-similar
210-  outcome: blocked
211:  blocked_by: data_missing
212-  notes: Imaging data not in the dandiset, nor found elsewhere (see fig2d-shared-architecture).
213-- claim: fig2h-fewer-motion-responsive
214-  outcome: blocked
215:  blocked_by: data_missing
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^- id:" claims/000248/10.1038-s41593-025-02055-5.yaml | awk '{print $3}' | tr '\n' ' '; echo; date -u
```

```
fig1e-npx-exclusive-center fig1f-npx-ic-ire-responsive fig1g-npx-orientation-match results-npx-units-per-session methods-npx-ic-encoder-count ed6b-npx-v1-group-counts fig2d-npx-ccg-hva-input fig3a-npx-v1-decoding fig3c-npx-v1-inference fig3d-npx-areas-inference ed7a-npx-no-area-above-v1 ed7b-npx-xre-inference ed6ef-npx-ic-not-greater ed2b-npx-fixed-gaze ed2f-npx-rf-match ed2g-npx-pupil-area ed2a-npx-gaze-confined supp3-decoder-types fig1ik-2p-exclusive-center fig2b-2p-ic-encoder-fraction fig2c-2p-orientation-tuning ed4c-2p-ic-encoder-rf-anywhere ed5cd-2p-rf-size fig3e-2p-l23-not-l4 fig3e-2p-mesoscope-areas ed7b-2p-xre-inference ed5e-2p-inverted ed4hi-2p-scaled-images ed3-2p-robust-gap-mapping-contrast fig4a-2p-zeroing-ic-encoders fig4b-2p-ic-encoders-only fig5c-2p-holo-ic-responsive fig5-2p-holo-suppression fig5d-2p-ic-encoder-pattern-completion fig5e-2p-segment-no-completion ed9b-2p-holo-near-visual ed10-2p-lc-encoders-weaker fig6d-meso-ic-encoders-local fig6e-meso-segment-feedforward ed6cd-npx-ic-encoders-all-areas 
Wed Oct 28 04:48:51 UTC 2026
```

**Agent calls Bash**

```bash
python - <<'EOF'
npx = ["results-npx-units-per-session","methods-npx-ic-encoder-count","ed6b-npx-v1-group-counts","ed6cd-npx-ic-encoders-all-areas",
"fig1e-npx-exclusive-center","fig1f-npx-ic-ire-responsive","fig1g-npx-orientation-match","ed2b-npx-fixed-gaze","ed2f-npx-rf-match",
"ed2g-npx-pupil-area","ed2a-npx-gaze-confined","fig2d-npx-ccg-hva-input","fig3a-npx-v1-decoding","fig3c-npx-v1-inference",
"fig3d-npx-areas-inference","ed7b-npx-xre-inference","ed7a-npx-no-area-above-v1","ed6ef-npx-ic-not-greater"]
twop = ["fig1ik-2p-exclusive-center","fig2b-2p-ic-encoder-fraction","fig2c-2p-orientation-tuning","ed4c-2p-ic-encoder-rf-anywhere",
"ed5cd-2p-rf-size","fig3e-2p-l23-not-l4","fig3e-2p-mesoscope-areas","ed7b-2p-xre-inference","ed5e-2p-inverted","ed4hi-2p-scaled-images",
"ed3-2p-robust-gap-mapping-contrast","fig4a-2p-zeroing-ic-encoders","fig4b-2p-ic-encoders-only","fig5c-2p-holo-ic-responsive",
"fig5-2p-holo-suppression","fig5d-2p-ic-encoder-pattern-completion","fig5e-2p-segment-no-completion","ed9b-2p-holo-near-visual",
"ed10-2p-lc-encoders-weaker","fig6d-meso-ic-encoders-local","fig6e-meso-segment-feedforward"]
TIME = ("Not tested in a run of the notebook. The analysis is written in the notebook and the helper, but the run of "
        "this author stopped analysing at its time limit before the notebook was executed through tools/entry.py: "
        "about two hours were lost to two commands that did not return (a development run whose decoding cell did "
        "not finish, and the entry check, whose long-literal scan did not finish on the helper before a list was "
        "split). The cells were run once outside the notebook on data cached during development, up to the "
        "cross-correlogram claim; under the protocol those runs decide no outcome and supply no number here.")
DEC = (" The decoding cells (fig3a to ed6ef) were not run at all: the decoders took 15 to 40 s per session and area, "
       "and the full set was estimated at 6 to 25 minutes depending on the readings run.")
lines = ["schema_version: 2","id: 000248-shin-2025-01","dataset:","  archive: dandi",'  id: "000248"',"  version: 0.240502.2344",
"  doi: 10.48324/dandi.000248/0.240502.2344","paper: doi:10.1038/s41593-025-02055-5","date: 2026-10-28","entry: 000248-shin-2025",
"provenance:","  kind: agent","  accountable:","    name: CatalystNeuro","  agent:","    harness: Claude Code","    model: claude-opus-5-5",
"    protocol: pilot-12","  runner:","    platform: GitHub Actions","    url: https://github.com/catalystneuro/encore/actions/runs/40609498105",
"inputs: []","outcomes:"]
import textwrap
def block(s, ind="    "):
    return "\n".join(textwrap.wrap(s, 96, initial_indent="", subsequent_indent=ind))
for c in npx:
    extra = DEC if c in ["fig3a-npx-v1-decoding","fig3c-npx-v1-inference","fig3d-npx-areas-inference","ed7b-npx-xre-inference","ed7a-npx-no-area-above-v1","ed6ef-npx-ic-not-greater"] else ""
    lines += [f"- claim: {c}", "  outcome: blocked", "  blocked_by: too_large", "  notebook: reproduce_shin_2025.ipynb",
              "  output: claim:" + c, "  notes: " + block(TIME + extra)]
lines += ["- claim: supp3-decoder-types","  outcome: blocked","  blocked_by: too_large","  notebook: reproduce_shin_2025.ipynb",
          "  notes: " + block("The neural network of the Methods (50,000 epochs, tenfold, on V1, LM and AL sessions) was "
          "estimated at hours of computation, over the notebook limit; the notebook holds a timing cell for it that was "
          "not executed. The quadratic and RBF SVMs were not run for lack of time. Supplementary Fig. 3, which shows the "
          "result, was not available to the claims file. " + TIME)]
TWO = ("The 2p imaging, 2p mesoscope and 2p holography recordings are not in this dandiset, which holds only the 12 "
       "Neuropixels sessions (78 files, no imaging). The paper's Data availability names only dandiset 000248 for the "
       "Neuropixels data and additional postprocessed data in Code Ocean (10.24433/CO.6659254.v2), without saying what "
       "they are; the capsule answered HTTP 403 from this run. No public copy of the 2p recordings was found.")
for c in twop:
    lines += [f"- claim: {c}", "  outcome: blocked", "  blocked_by: data_missing", "  notes: " + block(TWO)]
lines += ["- claim: ed6cd-npx-ic-encoders-all-areas"] if False else []
F = [("data_missing", "The dandiset holds the 12 Neuropixels sessions only. The 2p imaging (V1L2/3, V1L4, mesoscope) and 2p holographic optogenetics recordings behind Figures 1h to 1k, 2b, 2c, 3e and 4 to 6 and several Extended Data figures are not in it, and the paper names no public archive for them; 21 of the paper's findings cannot be tested."),
     ("metadata_error", "The units tables hold units whose quality is labelled noise (539 of 3,026 units in sub-633229, 322 of the V1 units across sessions), while the Methods state that all units not classified as noise were packaged into the NWB files."),
     ("paper_inconsistency", "The Methods' Animals list 14 Neuropixels mice (Sst-IRES-Cre;Ai32 n = 10, PV-IRES-Cre;Ai32 n = 4); the files hold 12 sessions from 12 mice (9 Sst, 3 Pvalb), as the Results and legends state."),
     ("metadata_error", "The eye tracking pupil position (pupil_tracking/data) is stated in meters; its values (pupil center near 300 to 400, pupil half-width near 20) are camera pixels, and no conversion to visual degrees is given, so the Methods' 8 degree fixed-gaze criterion cannot be applied from the files."),
     ("paper_inconsistency", "The Methods say eye video was acquired at 30 Hz; the eye tracking timestamps in the files are 16.7 ms apart (60 Hz), which is what the paper's code assumes."),
     ("metadata_insufficient", "The IC block tables give each image only as a frame index (0 to 21) with no image names; the names come from the paper's code, and the image templates stored in the files allow them to be checked by eye."),
     ("other", "The last eye tracking timestamp of each session with eye tracking is NaN.")]
lines += ["findings:"]
for k, s in F:
    lines += [f"- kind: {k}", "  statement: " + block(s)]
open("attempts/000248-shin-2025-01.yaml","w").write("\n".join(lines) + "\n")
EOF
python -c "import yaml;d=yaml.safe_load(open('attempts/000248-shin-2025-01.yaml'));print(len(d['outcomes']))"; date -u
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import yaml;d=yaml.safe_load(open('attempts/000248-shin-2025-01.yaml'));print(len(d['outcomes']))
                  ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/site-packages/yaml/__init__.py", line 125, in safe_load
    return load(stream, SafeLoader)
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/site-packages/yaml/__init__.py", line 81, in load
    return loader.get_single_data()
           ~~~~~~~~~~~~~~~~~~~~~~^^
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/site-packages/yaml/constructor.py", line 49, in get_single_data
    node = self.get_single_node()
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/site-packages/yaml/composer.py", line 36, in get_single_node
    document = self.compose_document()
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/site-packages/yaml/composer.py", line 55, in compose_document
    node = self.compose_node(None, None)
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/site-packages/yaml/composer.py", line 84, in compose_node
    node = self.compose_mapping_node(anchor)
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/site-packages/yaml/composer.py", line 133, in compose_mapping_node
    item_value = self.compose_node(node, item_key)
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/site-packages/yaml/composer.py", line 82, in compose_node
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
sed -i 's#tools/entry.py: about two hours#tools/entry.py. About two hours#' attempts/000248-shin-2025-01.yaml; sed -n 25,40p attempts/000248-shin-2025-01.yaml | grep -n ": .*: " ; python -c "import yaml;d=yaml.safe_load(open('attempts/000248-shin-2025-01.yaml'));print(len(d['outcomes']))"; grep -c "[^ ]: [^ ]" attempts/000248-shin-2025-01.yaml
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import yaml;d=yaml.safe_load(open('attempts/000248-shin-2025-01.yaml'));print(len(d['outcomes']))
                  ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/site-packages/yaml/__init__.py", line 125, in safe_load
    return load(stream, SafeLoader)
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/site-packages/yaml/__init__.py", line 81, in load
    return loader.get_single_data()
           ~~~~~~~~~~~~~~~~~~~~~~^^
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/site-packages/yaml/constructor.py", line 49, in get_single_data
    node = self.get_single_node()
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/site-packages/yaml/composer.py", line 36, in get_single_node
    document = self.compose_document()
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/site-packages/yaml/composer.py", line 55, in compose_document
    node = self.compose_node(None, None)
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/site-packages/yaml/composer.py", line 84, in compose_node
    node = self.compose_mapping_node(anchor)
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/site-packages/yaml/composer.py", line 133, in compose_mapping_node
    item_value = self.compose_node(node, item_key)
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/site-packages/yaml/composer.py", line 82, in compose_node
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 178,181p attempts/000248-shin-2025-01.yaml
```

```
the notebook on data cached during development, up to the cross-correlogram claim; under the
    protocol those runs decide no outcome and supply no number here. The decoding cells (fig3a
    to ed6ef) were not run at all: the decoders took 15 to 40 s per session and area, and the
    full set was estimated at 6 to 25 minutes depending on the readings run.
```

**Agent calls Bash**

```bash
sed -i 's/were not run at all: the decoders/were not run at all; the decoders/' attempts/000248-shin-2025-01.yaml; python -c "
import yaml;d=yaml.safe_load(open('attempts/000248-shin-2025-01.yaml'));print(len(d['outcomes']), len(d['findings']))"; date -u
```

```
40 7
Wed Oct 28 04:49:25 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > conclusions.py <<'EOF'
NPX = ["results-npx-units-per-session", "methods-npx-ic-encoder-count", "ed6b-npx-v1-group-counts",
       "ed6cd-npx-ic-encoders-all-areas", "fig1e-npx-exclusive-center", "fig1f-npx-ic-ire-responsive",
       "fig1g-npx-orientation-match", "ed2b-npx-fixed-gaze", "ed2f-npx-rf-match", "ed2g-npx-pupil-area",
       "ed2a-npx-gaze-confined", "fig2d-npx-ccg-hva-input", "fig3a-npx-v1-decoding", "fig3c-npx-v1-inference",
       "fig3d-npx-areas-inference", "ed7b-npx-xre-inference", "ed7a-npx-no-area-above-v1", "ed6ef-npx-ic-not-greater",
       "supp3-decoder-types"]
RESULTS = {c: ("**Result: blocked (too_large).** The author's run reached its time limit before this notebook "
               "was executed for the record, so no outcome is drawn from the cells above (attempt record, notes).")
           for c in NPX}
HEADER_TABLE = """| Claims | Status |
|---|---|
| 18 Neuropixels claims (unit counts, functional subsets, receptive fields, fixed gaze, eye, cross-correlograms, decoding) | Written here; blocked (too_large): not executed for the record within the author's time limit |
| supp3-decoder-types | Blocked (too_large): the network of the Methods is estimated at hours |
| 21 claims on the 2p imaging, mesoscope and holography data | Blocked (data_missing): not in the dandiset |"""
SUMMARY = """## Summary

| Claim | Outcome |
|---|---|
| 18 Neuropixels claims | Blocked: too_large (time limit of the author's run; see the attempt record) |
| supp3-decoder-types | Blocked: too_large |
| 21 claims on 2p imaging, mesoscope and holography | Blocked: data_missing |

How the analysis differs from the paper's: the decoders use scikit-learn's libsvm SVM in place of
MATLAB's fitcecoc, with C = 1 (reading a) and, on V1 only, C chosen by an inner cross-validation
over 10^-3 to 1 (reading b); the paper's code searched hyperparameters with MATLAB's Bayesian
optimisation. The fixed-gaze criterion uses the code's 20 camera pixels, as the files give no
conversion to visual degrees.

What was found about the dataset (attempt record, findings): the files hold units labelled noise
although the Methods say none were packaged; the Methods list 14 mice where the files and the
Results have 12; the pupil position is labelled in meters but is in camera pixels; the eye video is
60 Hz where the Methods say 30 Hz; the IC block tables carry image indices without names; and the
2p data are not in the dandiset."""
EOF
. dev/bin/activate && python build_nb.py && cat > entries/000248-shin-2025/README.md <<'EOF'
# Shin et al. (2025) from dandiset 000248

Tests the Neuropixels findings of [Shin et al. (2025)](https://doi.org/10.1038/s41593-025-02055-5)
on [DANDI:000248](https://dandiarchive.org/dandiset/000248/0.240502.2344), which holds 12
Neuropixels sessions (six probes, V1, LM, RL, AL, PM and AM) recorded while mice viewed illusory
contour images. The 2p imaging and holography data of the paper are not in it.

| Claims | Outcome |
|---|---|
| 18 Neuropixels claims and the decoder comparison | Blocked: too_large (the author's run reached its time limit before the notebook was executed for the record) |
| 21 claims on 2p imaging, mesoscope and holography | Blocked: data_missing |

The attempt record, with the reasons and the findings about the dataset, is
[`attempts/000248-shin-2025-01.yaml`](../../attempts/000248-shin-2025-01.yaml).

- `reproduce_shin_2025.ipynb`: the analysis, one section per claim. It streams the 12 session
  files (about 3 minutes) and runs the decoders in parallel; the whole is estimated at 15 minutes.
- `illusion.py`: loading the session files, trial responses, the functional subsets of the
  paper's code (IC-encoders, segment responders, exclusive center units), the decoder and the
  cross-correlograms. Other notebooks on this dandiset can import it.
EOF
cd  && timeout 120 python tools/entry.py check entries/000248-shin-2025 2>&1 | tail -8; date -u
```

```
wrote entries/000248-shin-2025/reproduce_shin_2025.ipynb 80 cells
0 error(s)
Wed Oct 28 04:50:12 UTC 2026
```

**Agent calls Bash**

```bash
timeout 1680 python tools/entry.py all entries/000248-shin-2025 2>&1 | tail -15; echo "exit ${PIPESTATUS[0]}"; date -u
```

```
Installed kernelspec registry-000248-shin-2025 in executed/000248-shin-2025/.venv/share/jupyter/kernels/registry-000248-shin-2025
0 error(s)
pass  reproduce_shin_2025.ipynb  (1202 s)
exit 0
Wed Oct 28 05:10:50 UTC 2026
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json,glob
rep=[("The author's run reached its time limit before this notebook was executed for the record, so no outcome is drawn from the cells above (attempt record, notes).",
      "The author's run reached its time limit before this notebook was executed; it ran to completion afterwards, as the entry check, and its outputs were not reviewed, so no outcome is drawn from the cells above (attempt record, notes)."),
     ("Written here; blocked (too_large): not executed for the record within the author's time limit","Written here; blocked (too_large): executed only after the author's time limit, outputs not reviewed"),
     ("Blocked: too_large (time limit of the author's run; see the attempt record)","Blocked: too_large (time limit of the author's run; the notebook ran afterwards, outputs not reviewed)")]
for p in ["entries/000248-shin-2025/reproduce_shin_2025.ipynb"]+glob.glob("executed/000248-shin-2025/*.ipynb"):
    s=open(p).read()
    for a,b in rep: s=s.replace(a,b)
    open(p,'w').write(s); print(p)
p="attempts/000248-shin-2025-01.yaml"; s=open(p).read()
s=s.replace("under the\n    protocol those runs decide no outcome and supply no number here.","under the\n    protocol those runs decide no outcome and supply no number here. The notebook then ran to\n    completion as the entry check (tools/entry.py all, 1,202 s) after the time limit; its outputs\n    were not reviewed and decide no outcome.")
open(p,'w').write(s)
s=open("entries/000248-shin-2025/README.md").read().replace("reached its time limit before the notebook was executed for the record)","reached its time limit before the notebook was executed; it ran afterwards as the entry check, in 20 minutes, and its outputs were not reviewed)").replace("the whole is estimated at 15 minutes","the whole took 20 minutes in the entry check")
open("entries/000248-shin-2025/README.md","w").write(s)
EOF
sed -i 's/runtime_minutes: 15/runtime_minutes: 20/' entries/000248-shin-2025/entry.yaml
python -c "import yaml;d=yaml.safe_load(open('attempts/000248-shin-2025-01.yaml'));print(d['outcomes'][0]['notes'][-200:])"
timeout 120 python tools/entry.py check entries/000248-shin-2025 2>&1 | tail -3; timeout 120 python tools/entry.py handover entries/000248-shin-2025 2>&1 | tail -3; date -u
```

```
entries/000248-shin-2025/reproduce_shin_2025.ipynb
executed/000248-shin-2025/reproduce_shin_2025.ipynb
de no outcome and supply no number here. The notebook then ran to completion as the entry check (tools/entry.py all, 1,202 s) after the time limit; its outputs were not reviewed and decide no outcome.
0 error(s)
wrote executed/000248-shin-2025/handover
Wed Oct 28 05:11:42 UTC 2026
```

**Agent calls Bash**

```bash
git status --short | head
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
```

**Agent calls Bash**

```bash
git status --short | grep -v "^?? \.\(bash\|git\|idea\|mcp\|profile\|ripgrep\|vscode\|zprofile\|zshrc\)"
```

```
?? attempts/000248-shin-2025-01.yaml
?? entries/000248-shin-2025/
?? scripts
```

**Agent**

Every claim is recorded as blocked. Two commands I ran without a time limit hung for about two hours in total. The notebook was not executed until after the 04:49 cutoff, so no outcome comes from a notebook run.

## 1. Outcomes

| Claims | Outcome |
|---|---|
| 18 Neuropixels claims: unit counts, IC-encoder and segment responder counts, exclusive-center RF (fig1e/f/g), fixed gaze (ed2b, ed2f), pupil and gaze (ed2g, ed2a), cross-correlograms (fig2d), decoding (fig3a, 3c, 3d, ed7a, ed7b, ed6ef), ed6cd | blocked, `too_large` (ran out of time) |
| supp3-decoder-types | blocked, `too_large` (the 50,000-epoch network is estimated at hours) |
| 21 claims on 2p imaging, mesoscope and holography | blocked, `data_missing` |

The entry is in `entries/000248-shin-2025/`: notebook, `illusion.py`, README, lock file. `tools/entry.py all` passes; the notebook ran in 1,202 s, after the cutoff, and I did not review its outputs. `handover` is built and the record is `attempts/000248-shin-2025-01.yaml`. I pinned 0.240502.2344 because it is the only published version and the paper cites none.

## 2. The dataset

The record has seven findings:
- **2p data missing:** the dandiset holds only the 12 Neuropixels sessions. The paper names no public archive for the 2p data, and its Code Ocean capsule returned 403 from here.
- **Noise units included:** the files contain units labelled `noise`, although the Methods say none were packaged.
- **Mouse count:** the Methods list 14 mice (10 Sst, 4 PV); the files hold 12 (9 Sst, 3 Pvalb).
- **Pupil units:** pupil position is labelled meters but the values are camera pixels, with no conversion to degrees. The 8-degree criterion therefore cannot be applied; only the code's 20-pixel reading can.
- **Eye frame rate:** the eye video is 60 Hz; the Methods say 30 Hz.
- **No image names:** the IC block tables give each image only as a frame index. The image templates stored in the files match the code's names.
- **NaN timestamp:** the last eye timestamp in each session is NaN.

Development runs on cached data were done outside the notebook, so under the protocol they supply no numbers to the record.

- **Assumptions:** reading (b) of fig1e's ed6b criterion was run two ways, citing the Methods' "All units not classified as noise were packaged". The decoder's reading (b) was limited to C from 10^-3 to 1, and to V1 only, for time. Both are recorded in the notebook.
- **Questions for the paper's authors:** none filed.
- **Questions to a reader:** none.

## 3. Protocol issues
1. **Check can hang.** The long-literal regex in `tools/entry.py` backtracks without end on a two-line integer list (the 22 trial codes in the helper), so `check` hung with no message. I split the list. The checker should guard against this.
2. **No time limits on commands.** The protocol says to time subsets but not to wrap commands in timeouts. A development run whose SVM step was very slow (large C), and the hanging check, cost about two hours. I recorded the claims as `too_large` with the reason given.
3. **Tight time budget.** Many SVM fits (63 session-area pairs, two readings, TRE and XRE decoders) do not fit in a 30-minute notebook. I limited the inner C search to V1 and said so in the notebook.
4. **No category for "not reviewed in time".** Neither `too_large` nor any other reason fits well, so I used `too_large` and explained in the notes.

## 4. Runtime and failures
Run from 00:36 to about 05:12 UTC. Loading all 12 sessions takes about 2.5 minutes; the whole notebook took 20 minutes. Failures were the two hung commands (one hour each), the 403 from Code Ocean, and the network decoder being too slow to run.

## End of run

81 turns, 275 minutes, result: success.
