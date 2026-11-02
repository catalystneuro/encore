# 001274 · author · run 41320327294

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls
```

```
<persisted-output>
Output too large (35.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/507178fe-e3ef-4321-8e47-9e85f2d071f7/tool-results/bgxp8q5m9.txt

Preview (first 2KB):
Sun Nov  1 15:20:22 UTC 2026
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
 "file_path": "docs/protocol.md"
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-13`. Record this version in the attempt's provenance.
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
[... 593 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md | head -150; wc -l docs/design.md docs/archives.md; ls claims/001274 paper entries/001453-fouke-2025; cat attempts/001453-fouke-2025-01.yaml | head -50
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
[... 186 more lines not kept]
```

**Agent calls Bash**

```bash
cat docs/design.md; sed -n 1,287p docs/archives.md
```

```
<persisted-output>
Output too large (29.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/507178fe-e3ef-4321-8e47-9e85f2d071f7/tool-results/b983l02f3.txt

Preview (first 2KB):
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
[... 38 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/001274/*.yaml
```

```
<persisted-output>
Output too large (43.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/507178fe-e3ef-4321-8e47-9e85f2d071f7/tool-results/bj6c3ahrd.txt

Preview (first 2KB):
# Claims for Semenov, Kim, Silkuniene & Pakhomov (2025), Cell Reports Physical Science 6, 102660,
# on dandiset 001274.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22, under
# docs/protocol.md version pilot-10, as the reader.
#
# Text read. The NIH author manuscript (NIHMS2098259, PMC12320893) as served by Europe PMC, with
# its main text, figure legends and STAR Methods, and the supplement (NIHMS2098259-supplement-1.pdf,
# Figures S1 to S4 and Table S1, the Key Resource Table), all in
# paper/10.1016-j.xcrp.2025.102660.txt. The version of record was not read. No main-text PDF was
# available, so Figures 1 to 6 could not be looked at; numbers shown only in figures are not used.
#
# Code. The paper states that it does not report original code. Analyses were done with Fiji or
# MetaMorph (ROI intensities), Origin 8.0 (exponential fits), Grapher 16 (linear regression) and,
# per Table S1, RStudio 2024.04.2 (the LOESS fits are read here as R's loess, see below).
#
# Data the paper used. E18 Sprague-Dawley rat hippocampal neurons (BrainBits), cultured about one
[... 11 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/507178fe-e3ef-4321-8e47-9e85f2d071f7/tool-results/bj6c3ahrd.txt"
}
```

```
1	# Claims for Semenov, Kim, Silkuniene & Pakhomov (2025), Cell Reports Physical Science 6, 102660,
2	# on dandiset 001274.
3	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22, under
4	# docs/protocol.md version pilot-10, as the reader.
5	#
6	# Text read. The NIH author manuscript (NIHMS2098259, PMC12320893) as served by Europe PMC, with
7	# its main text, figure legends and STAR Methods, and the supplement (NIHMS2098259-supplement-1.pdf,
8	# Figures S1 to S4 and Table S1, the Key Resource Table), all in
9	# paper/10.1016-j.xcrp.2025.102660.txt. The version of record was not read. No main-text PDF was
10	# available, so Figures 1 to 6 could not be looked at; numbers shown only in figures are not used.
11	#
12	# Code. The paper states that it does not report original code. Analyses were done with Fiji or
13	# MetaMorph (ROI intensities), Origin 8.0 (exponential fits), Grapher 16 (linear regression) and,
14	# per Table S1, RStudio 2024.04.2 (the LOESS fits are read here as R's loess, see below).
15	#
16	# Data the paper used. E18 Sprague-Dawley rat hippocampal neurons (BrainBits), cultured about one
17	# week on coverslips, stained with FluoVolt (Di-8-ANEPPS in Figure S1). Two kinds of recording:
18	# (1) Fast imaging of the optical membrane potential (64 x 64 pixels, 3,130 or 3,086.4 frames/s,
19	# 1,200 images per session, 50 ms before, 250 ms during and about 90 ms after the stimulus), with
20	# 250-ms unmodulated or 20-Hz amplitude-modulated sine waves at 2 and 20 kHz (Figures 1, 2), in
[... 635 more lines not kept]
```

**Agent**

The claims file has 26 claims, most on other dandisets (elsewhere). Next I'll read the archive docs and the example entry, then survey the dataset.

**Agent calls Bash**

```bash
sed -n 1,140p docs/archives.md; cat entries/001453-fouke-2025/entry.yaml entries/001453-fouke-2025/requirements.in; head -60 entries/001453-fouke-2025/omr.py
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
[... 209 more lines not kept]
```

**Agent**

Now survey the dataset 001274 and the related dandisets.

**Agent calls Bash**

```bash
cd $TMPDIR; for d in 001274 001273 001030 001032 001033 001034 001035 001271 001272; do echo "== $d"; curl -s https://api.dandiarchive.org/api/dandisets/$d/ | python -c "import json,sys;j=json.load(sys.stdin);print(j['most_recent_published_version'] and j['most_recent_published_version']['version'], j['draft_version']['name'][:100], j['draft_version']['asset_count'], j['draft_version']['size'])"; curl -s "https://api.dandiarchive.org/api/dandisets/$d/versions/" | python -c "import json,sys;print([ (v['version'],v['asset_count'],v['size']) for v in json.load(sys.stdin)['results']])"; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; python - <<'EOF'
import json,urllib.request
def get(u): return json.load(urllib.request.urlopen(u))
for d,v in [("001274","0.250805.1401")]:
    m=get(f"https://api.dandiarchive.org/api/dandisets/{d}/versions/{v}/")
    print(json.dumps({k:m.get(k) for k in ['name','description','citation','relatedResource','wasGeneratedBy','assetsSummary','contributor']},indent=1)[:6000])
    assets=[];u=f"https://api.dandiarchive.org/api/dandisets/{d}/versions/{v}/assets/?page_size=1000"
    while u:
        r=get(u);assets+=r['results'];u=r['next']
    json.dump(assets,open(f"assets_{d}.json","w"))
    for a in assets[:300]: print(a['path'],a['size'])
EOF
```

```
{
 "name": "Characterization of Plasma Membrane Polarization in Hippocampal Neurons During Sine Wave and Modulated Sine Wave Stimulation",
 "description": "This experimental series aimed to visualize and characterize plasma membrane (PM) polarization dynamics in hippocampal neurons exposed to 2 kHz sine waves or 2 kHz sine waves modulated at 100 Hz or 154 Hz. Neurons were pre-loaded with FluoVolt potentiometric dye to enable visualization of membrane polarization changes. This study was partially supported by the NIH Brain Initiative (NEI R21EY034803).",
 "citation": "Silkuniene, Giedre; Kim, Vitalii; Semenov, Iurii ; Pakhomov, Andrei (2025) Characterization of Plasma Membrane Polarization in Hippocampal Neurons During Sine Wave and Modulated Sine Wave Stimulation (Version 0.250805.1401) [Data set]. DANDI Archive. https://doi.org/10.48324/dandi.001274/0.250805.1401",
 "relatedResource": [
  {
   "url": "https://doi.org/10.1016/j.xcrp.2025.102660",
   "name": "Excitation and polarization of isolated neurons by high-frequency sine waves for temporal interference stimulation",
   "relation": "dcite:IsPublishedIn",
   "schemaKey": "Resource",
   "identifier": "doi.org/10.1016/j.xcrp.2025.102660",
   "resourceType": "dcite:JournalArticle"
  }
 ],
 "wasGeneratedBy": [
  {
   "name": "Next Gen Temporal Interference Stimulation Non-Invasive Neuromodulation",
   "schemaKey": "Project",
   "identifier": "5R21EY034803"
  },
[... 314 more lines not kept]
```

**Agent**

Subjects sub-1 to sub-9 look like cells C1 to C9. Let me open a file and list its contents.

**Agent calls Bash**

```bash
cd $TMPDIR; python -c "import pynwb,remfile,h5py,dandi;print(pynwb.__version__)" ; python - <<'EOF'
import json,urllib.request
a=json.load(open("assets_001274.json"))
m=json.load(urllib.request.urlopen(f"https://api.dandiarchive.org/api/dandisets/001274/versions/0.250805.1401/assets/{a[0]['asset_id']}/"))
print(json.dumps(m,indent=1)[:5000])
EOF
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pynwb,remfile,h5py,dandi;print(pynwb.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pynwb'
{
 "id": "dandiasset:ed7c99c4-0d96-4202-aab2-3db06a2ae6df",
 "path": "sub-1-20240522/sub-1-20240522_obj-sx69sf_image.nwb",
 "access": [
  {
   "schemaKey": "AccessRequirements",
   "status": "dandi:OpenAccess"
  }
 ],
 "digest": {
  "dandi:dandi-etag": "23ef7684c7edfda96a6346a1dffa3d7d-1",
  "dandi:sha2-256": "af4cad9284f78ee585c0535101fb8e0782b9ac6472f9f31d4e986d3fc3632e5a"
 },
 "@context": "https://raw.githubusercontent.com/dandi/schema/master/releases/0.6.8/context.json",
 "approach": [],
[... 82 more lines not kept]
```

**Agent**

Set up a working environment and collect every asset's session description.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q work && . work/bin/activate && uv pip install -q pynwb remfile h5py dandi numpy scipy pandas matplotlib statsmodels 2>&1 | tail -2; python -c "import pynwb;print(pynwb.__version__)"
```

```
4.2.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && python - <<'EOF'
import json,urllib.request
from concurrent.futures import ThreadPoolExecutor
a=json.load(open("assets_001274.json"))
def f(x):
    m=json.load(urllib.request.urlopen(f"https://api.dandiarchive.org/api/dandisets/001274/versions/0.250805.1401/assets/{x['asset_id']}/"))
    s=[w for w in m['wasGeneratedBy'] if w['schemaKey']=='Session'][0]
    return dict(path=x['path'],size=x['size'],asset_id=x['asset_id'],url=m['contentUrl'][1],name=s['name'],desc=s['description'],start=s.get('startDate'),sha=m['digest'].get('dandi:sha2-256'))
with ThreadPoolExecutor(16) as ex: r=list(ex.map(f,a))
json.dump(r,open("meta_001274.json","w"))
import collections
print(collections.Counter(x['name'] for x in r))
import re
c=collections.Counter(re.sub(r'Subject ID: \S+\.','',x['desc']) for x in r)
for k,v in c.items(): print(v,k[:600]);print()
EOF
```

```
Counter({'PM polarization with sinewaves and modulated sine waves (spindles)': 232})
16  Stimulation was applied with a single 2 µs long rectangular pulse at 10,0V amplitude . The experiment was performed without tetrodotoxin (vehicle control). The recording was performed in a forward manner, following the sequence of pulse application to mimic the real-time progression of events. Electrode position not specified. Distance between electrodes 0.12 mm, electrode diameter 0.1 mm. Neuron action potentials were visualized using the voltage-sensitive fluorescent dye FluoVolt and a FITC filter cube. All experiments were performed in standard physiological solution containing (in mM): 14

47  Stimulation was applied with a spindle (sine wave modulated at 154Hz frequency) delivered at 2kHz at 7,0V amplitude from peak to peak . The experiment was performed without tetrodotoxin (vehicle control). The recording was performed in a forward manner, following the sequence of pulse application to mimic the real-time progression of events. Electrode position not specified. Distance between electrodes 0.12 mm, electrode diameter 0.1 mm. Neuron action potentials were visualized using the voltage-sensitive fluorescent dye FluoVolt and a FITC filter cube. All experiments were performed in stand

1  Stimulation was applied with a sine wave delivered at 2kHz at 10,0V amplitude from peak to peak . The experiment was performed without tetrodotoxin (vehicle control). The recording was performed in a forward manner, following the sequence of pulse application to mimic the real-time progression of events. Electrode position not specified. Distance between electrodes 0.12 mm, electrode diameter 0.1 mm. Neuron action potentials were visualized using the voltage-sensitive fluorescent dye FluoVolt and a FITC filter cube. All experiments were performed in standard physiological solution containing 

56  Stimulation was applied with a spindle (sine wave modulated at 154Hz frequency) delivered at 2kHz
[... 17 more lines not kept]
```

**Agent**

Dataset holds pulses and sine/spindle sessions, many labelled with TTX. Now I'll read the paper.

**Agent calls Bash**

```bash
wc -c paper/*.txt; grep -n -i "tetrodotoxin\|TTX" paper/*.txt | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && fold -s -w 250 paper/10.1016-j.xcrp.2025.102660.txt > paper.txt; wc -l paper.txt; grep -n "Asymmetric and less-efficient\|Pulsed laser\|Kinetics of membrane\|Data and code\|STAR\|Quantification" paper.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/paper.txt",
 "offset": 100,
 "limit": 180
}
```

```
100	those observed with FluoVolt dye. Tetrodotoxin blocks sustained depolarization The sustained depolarization induced by intense unmodulated sine waves ( Figures 1 and 3 ) was immediately reversible upon stimulus cessation. It was not related to 
101	membrane electroporation, which would take seconds or longer to repair. 36 Instead, the sustained depolarization could result from overactivation of voltage-gated Na + channels by cycling de- and hyperpolarizations of the membrane by sine waves. 
102	Hyperpolarizations would remove the inactivation of channels opened by depolarizations, making them repeatedly available for activation. Consistent with this hypothesis, the inhibition of sodium channels with 1 μM tetrodotoxin not only abolished the 
103	APs but also fully blocked the sustained depolarization ( Figure S2 ). Kinetics of membrane charging by pulsed electric fields Excitation evoked by sine wave stimuli is a consequence of membrane charging that culminates in its depolarization to the 
104	AP threshold. Cells in the electric field depolarize at the cathode-facing pole and hyperpolarize at the anode-facing pole, while the integral membrane potential stays unchanged if no channels are activated. With sine wave stimuli, the poles keep 
105	charging to the opposite potentials in alternation. The induced transmembrane potential (TMP) is determined by the electric field strength and duration, as well as by the charging rate time constant. A large time constant would slow down charging 
106	and impede excitation by high-frequency sinusoids. Time constants of charging by external electric fields (also called “cellular time constants”) are orders of magnitude smaller than those in response to intracellular current injection. 37 For 
107	spherical cells, they can be calculated from intra- and extracellular conductivities, specific membrane capacitance, and cell radius. 42 , 44 However, for randomly shaped cells like neurons, analytical solutions are too complicated. W
[... 172 more lines not kept]
```

**Agent**

Read the paper's key sections. Now open an NWB file from 001274 and one from each related dandiset to see what they hold.

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . work/bin/activate && cat > survey.py <<'EOF'
import sys,json,urllib.request,h5py,remfile
def walk(f):
    def v(name,obj):
        if isinstance(obj,h5py.Dataset):
            print(" D",name,obj.shape,obj.dtype,dict((k,(obj.attrs[k] if not isinstance(obj.attrs[k],bytes) else obj.attrs[k].decode())) for k in obj.attrs if k not in('namespace','object_id')))
            if obj.size<20 and obj.dtype.kind in 'OSUfiu': print("   =",obj[()])
        else:
            print(" G",name,{k:obj.attrs[k] for k in obj.attrs if k not in('namespace','object_id')})
    f.visititems(v)
url=sys.argv[1]
f=h5py.File(remfile.File(url),'r'); walk(f)
EOF
python - <<'EOF'
import json
m=json.load(open("meta_001274.json"))
print(m[0]['url'])
EOF
```

```
Sun Nov  1 15:21:26 UTC 2026
https://dandiarchive.s3.amazonaws.com/blobs/65d/fa2/65dfa2c6-bd93-49de-845f-59ffb7a35663
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && time python survey.py https://dandiarchive.s3.amazonaws.com/blobs/65d/fa2/65dfa2c6-bd93-49de-845f-59ffb7a35663 2>&1 | head -80
```

```
<persisted-output>
Output too large (143.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/507178fe-e3ef-4321-8e47-9e85f2d071f7/tool-results/b5f0ti8xj.txt

Preview (first 2KB):
 G acquisition {}
 G acquisition/StrobeImaging {'comments': 'no comments', 'description': 'Optical time-lapse (strobe imaging) recordings of plasma membrane (PM) polarization were performed at 6 Hz (image frames were taken at this rate, but the data represent events occurring at MHz rates). Exposures began 1 µs after the start of recording for single pulse exposures and immediately at the start of the recordings for sine wave exposures. The strobe imaging method utilizes pulsed laser fluorescence microscopy, where a single short-pulse laser flash is delivered at a precise time interval before, during, or after the event (application of an electric pulse (EP)). Cells were pre-loaded with a voltage-sensitive FluoVolt dye, which responds to transmembrane potential changes within nanoseconds.', 'neurodata_type': 'ImageSeries'}
 D acquisition/StrobeImaging/data (140, 512, 512) uint16 {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(96.0), 'unit': 'n.a.'}
 D acquisition/StrobeImaging/dimension (3,) int32 {}
   = [140 512 512]
 D acquisition/StrobeImaging/starting_time () float64 {'rate': np.float64(6.0), 'unit': 'seconds'}
   = 1716430429.0
 G analysis {}
 D file_create_date (1,) object {}
   = [b'2025-01-03T15:45:21.563917-05:00']
 G general {}
 D general/experimenter (1,) object {}
   = [b'Iurii Semenov']
 D general/institution () object {}
   = b'Old Dominion University'
 D general/lab () object {}
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && cut -c1-400 /home/runner/.claude/projects/-home-runner-work-encore-encore/507178fe-e3ef-4321-8e47-9e85f2d071f7/tool-results/b5f0ti8xj.txt | grep -v "^   = \[" | sed -n 20,120p
```

```
D general/subject/description () object {}
   = b'Dissociated primary neurons from E18 Sprague Dawley rat hippocampal cells'
 D general/subject/sex () object {}
   = b'U'
 D general/subject/species () object {}
   = b'Rattus norvegicus'
 D general/subject/strain () object {}
   = b'Sprague Dawley'
 D general/subject/subject_id () object {}
   = b'1_20240522'
 D identifier () object {}
   = b'15ff1671-b435-4fa6-a1aa-8a314fb873ad'
 G processing {}
 D session_description () object {}
   = b'Subject ID: 1_20240522. Stimulation was applied with a single 2 \xc2\xb5s long rectangular pulse at 10,0V amplitude . The experiment was performed without tetrodotoxin (vehicle control). The recording was performed in a forward manner, following the sequence of pulse application to mimic the real-time progression of events. Electrode position not specified. Distance between electrodes 0.12 
 D session_start_time () object {}
   = b'2024-05-22T22:13:49-04:00'
 G specifications {}
 G specifications/core {}
 G specifications/core/2.6.0-alpha {}
[... 43 more lines not kept]
```

**Agent**

Each 001274 file holds only the raw strobe image stack (no ROIs, no stimulus waveform, no field values). Now survey the related dandisets.

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && cat > meta.py <<'EOF'
import json,urllib.request,sys,re,collections
from concurrent.futures import ThreadPoolExecutor
def get(u): return json.load(urllib.request.urlopen(u))
d,v=sys.argv[1],sys.argv[2]
assets=[];u=f"https://api.dandiarchive.org/api/dandisets/{d}/versions/{v}/assets/?page_size=1000"
while u:
    r=get(u);assets+=r['results'];u=r['next']
def f(x):
    m=get(f"https://api.dandiarchive.org/api/dandisets/{d}/versions/{v}/assets/{x['asset_id']}/")
    s=[w for w in m['wasGeneratedBy'] if w['schemaKey']=='Session'][0]
    return dict(path=x['path'],size=x['size'],asset_id=x['asset_id'],url=m['contentUrl'][1],name=s['name'],desc=s.get('description',''),start=s.get('startDate'),sha=m['digest'].get('dandi:sha2-256'))
with ThreadPoolExecutor(16) as ex: r=list(ex.map(f,assets))
json.dump(r,open(f"meta_{d}.json","w"))
print(d,len(r),collections.Counter(x['name'] for x in r))
print(r[0]['path'],r[0]['desc'][:1500])
print(len(set(x['sha'] for x in r)),"distinct sha")
EOF
for d in 001030:0.240520.1924 001032:0.240527.1432 001033:0.240527.1432 001034:0.240527.1431 001035:0.240527.1432 001271:0.250805.1352 001272:0.250805.1358 001273:0.250805.1356; do python meta.py ${d%%:*} ${d##*:}; echo; done
```

```
001030 17 Counter({'2kHz_stimulation_1,0V': 4, '2kHz_stimulation_1,25V': 3, '2kHz_stimulation_2,0V': 3, '2kHz_stimulation_1,5V': 2, '2kHz_stimulation_1,45V': 2, '2kHz_stimulation_1,7V': 1, '2kHz_stimulation_2,3V': 1, '2kHz_stimulation_1,75V': 1})
sub-c6-1-25V/sub-c6-1-25V_ses-2kHz-stimulation-1-25V_image.nwb 2 kHz stimulation of hippocampal neurons under 1.25V amplitude (measured as one polarity, V; peak-to-peak would be two-fold larger). Sine wave amplitude is gradually increased during the initial 0.25 s, then stays constant at the indicated voltage. Sine wave stimulation begins at 25 ms and lasts 2 s. For the employed electrode configuration, 1V translates into 36 V/cm. All experiments were performed in a low-conductance physiological solution containing (in mM): 140 NaGluconate, 5.4 KCl, 2 CaCl2, 1.5 MgCl2, 10 D-glucose, and 10 HEPES (pH 7.3, 290-300 mOsm/kg, 0.8 S/m).
17 distinct sha

001032 178 Counter({'2kHz_sine_stimulation_4V': 10, '2kHz_sine_stimulation_5V': 8, '2kHz_spindle_stimulation_5V': 8, '2kHz_spindle_stimulation_8V': 7, '2kHz_sine_stimulation_6V': 7, '2kHz_sine_stimulation_8V': 7, '20Hz_sine_stimulation_5V': 6, '2kHz_sine_stimulation_4.5V': 6, '2kHz_sine_stimulation_7.5V': 6, '2kHz_sine_stimulation_7V': 6, '2kHz_sine_stimulation_6.5V': 5, '2kHz_spindle_stimulation_6V': 5, '20Hz_sine_stimulation_6V': 4, '20Hz_sine_stimulation_8V': 4, '20kHz_sine_stimulation_10V': 4, '20kHz_sine_stimulation_11V': 4, '20kHz_sine_stimulation_14V': 4, '20kHz_sine_stimulation_8V': 4, '2kHz_sine_stimulation_10V': 4, '2kHz_sine_stimulation_5.7V': 4, '2kHz_sine_stimulation_5.5V': 3, '2kHz_spindle_stimulation_4.5V': 3, '2kHz_spindle_stimulation_7V': 3, '20kHz_sine_stimulation_12V': 3, '20kHz_sine_stimulation_13V': 3, '2kHz_sine_stimulation_18V': 3, '20kHz_sine_stimulation_9V': 3, '2kHz_sine_stimulation_3V': 3, '20Hz_sine_stimulation_4.5V': 3, '2kHz_spindle_stimulation_7.5V': 3, '2kHz_spindle_stimulation_4V': 3, '20Hz_sine_stimulation_4V': 2, '20Hz_sine_stimulation_7V': 2, '2
[... 27 more lines not kept]
```

**Agent**

Possible duplicate: 001032 and 001034 have identical session counts and total size. Checking checksums across dandisets.

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && python - <<'EOF'
import json,collections
D=["001030","001032","001033","001034","001035","001271","001272","001273","001274"]
M={d:json.load(open(f"meta_{d}.json")) for d in D}
sha=collections.defaultdict(list)
for d in D:
    for x in M[d]: sha[x['sha']].append((d,x['path']))
dups=[v for v in sha.values() if len(v)>1]
print(len(dups)); 
c=collections.Counter(tuple(sorted(set(a for a,b in v))) for v in dups); print(c)
for v in dups[:5]: print(v)
# subjects
for d in D:
    subs=collections.Counter(x['path'].split('/')[0] for x in M[d]); print(d,len(subs),dict(list(subs.items())[:40]))
EOF
```

```
0
Counter()
001030 17 {'sub-c6-1-25V': 1, 'sub-c6-1-0V': 1, 'sub-c5-1-0V': 1, 'sub-c5-1-5V': 1, 'sub-c5-2-0V': 1, 'sub-c7-1-25V': 1, 'sub-c7-1-7V': 1, 'sub-c7-1-45V': 1, 'sub-c7-1-0V': 1, 'sub-c6-1-45V': 1, 'sub-c8-1-5V': 1, 'sub-c8-1-0V': 1, 'sub-c7-2-3V': 1, 'sub-c8-1-25V': 1, 'sub-c7-2-0V': 1, 'sub-c8-2-0V': 1, 'sub-c8-1-75V': 1}
001032 14 {'sub-1-1': 9, 'sub-10-1': 17, 'sub-11-1': 19, 'sub-12-1': 7, 'sub-13-1': 13, 'sub-14-1': 15, 'sub-2-1': 19, 'sub-3-1': 17, 'sub-4-1': 4, 'sub-5-1': 15, 'sub-6-1': 14, 'sub-7-1': 15, 'sub-8-1': 4, 'sub-9-1': 10}
001033 10 {'sub-1-2': 8, 'sub-10-2': 33, 'sub-2-2': 19, 'sub-3-2': 21, 'sub-4-2': 10, 'sub-5-2': 11, 'sub-6-2': 32, 'sub-7-2': 19, 'sub-8-2': 15, 'sub-9-2': 25}
001034 14 {'sub-1-3': 9, 'sub-10-3': 17, 'sub-11-3': 19, 'sub-12-3': 7, 'sub-13-3': 13, 'sub-14-3': 15, 'sub-2-3': 19, 'sub-3-3': 17, 'sub-4-3': 4, 'sub-5-3': 15, 'sub-6-3': 14, 'sub-7-3': 15, 'sub-8-3': 4, 'sub-9-3': 10}
001035 15 {'sub-1-4': 10, 'sub-10-4': 12, 'sub-11-4': 14, 'sub-12-4': 14, 'sub-13-4': 14, 'sub-18-4': 8, 'sub-2-4': 19, 'sub-20-4': 37, 'sub-3-4': 20, 'sub-4-4': 6, 'sub-5-4': 11, 'sub-6-4': 30, 'sub-7-4': 28, 'sub-8-4': 12, 'sub-9-4': 19}
001271 20 {'sub-10-20240731': 19, 'sub-10-20240801': 33, 'sub-12-20240731': 11, 'sub-13-20240731': 13, 'sub-13-20240801': 12, 'sub-14-20240731': 25, 'sub-14-20240801': 10, 'sub-15-20240731': 11, 'sub-15-20240801': 12, 'sub-16-20240801': 15, 'sub-17-20240801': 7, 'sub-18-20240801': 12, 'sub-2-20240730': 14, 'sub-4-20240730': 13, 'sub-5-20240730': 13, 'sub-5-20240801': 17, 'sub-6-20240801': 9, 'sub-7-20240801': 10, 'sub-8-20240801': 18, 'sub-9-20240801': 13}
001272 3 {'sub-2-20240806': 20, 'sub-3-20240806': 29, 'sub-4-20240806': 16}
001273 13 {'sub-1-20240117': 15, 'sub-1-20240119': 16, 'sub-1-20240311': 8, 'sub-2-20240117': 16, 'sub-2-20240119': 17, 'sub-2-20240311': 8, 'sub-3-20240117': 16, 'sub-3-20240119': 19, 'sub-3-20240311': 8, 'sub-4-20240117': 16, 'sub-4-20240119': 18, 'sub-4-20240311': 8, 'sub-6-20240
[... 2 more lines not kept]
```

**Agent**

001032 and 001034 have the same subjects and per-subject session counts (sub-N-1 vs sub-N-3); checksums differ, so compare their data arrays.

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && python - <<'EOF'
import json
M2=json.load(open("meta_001032.json"));M4=json.load(open("meta_001034.json"))
x=sorted(M2,key=lambda x:x['path'])[0]; print(x['path'],x['url'])
EOF
python survey.py $(python -c "
import json;M=json.load(open('meta_001032.json'));print(sorted(M,key=lambda x:x['path'])[0]['url'])") | cut -c1-300 | grep -v specifications
```

```
sub-1-1/sub-1-1_ses-20Hz-sine-stimulation-3V_image.nwb https://dandiarchive.s3.amazonaws.com/blobs/0d4/3c1/0d43c1aa-11fc-4a3c-8529-fc4f38088346
 G acquisition {}
 G acquisition/TimeLapseImaging {'comments': 'no comments', 'description': 'TimeLapseImaging method utilizes fluorescence microscopy. Cells are loaded with a voltage-sensitive FluoVolt dye, which responds to Transmembrane Membrane Potential (TMP) changes within nanoseconds, allowing optical time-lap
 D acquisition/TimeLapseImaging/data (900, 16, 16) uint16 {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(24.0), 'unit': 'n.a.'}
 D acquisition/TimeLapseImaging/dimension (3,) int32 {}
   = [900  16  16]
 D acquisition/TimeLapseImaging/starting_time () float64 {'rate': np.float64(3086.4), 'unit': 'seconds'}
   = 1715301059.0
 G analysis {}
 D file_create_date (1,) object {}
   = [b'2024-05-25T16:52:00.463560-04:00']
 G general {}
 D general/experimenter (1,) object {}
   = [b'Iurii, Semenov']
 D general/institution () object {}
   = b'Old Dominion University'
 D general/lab () object {}
   = b'Pakhomov Lab'
 D general/session_id () object {}
   = b'20Hz_sine_stimulation_3V'
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && python - <<'EOF'
import json,collections,re
for d in ["001030","001032","001033","001034","001035","001271","001272","001273"]:
    M=json.load(open(f"meta_{d}.json"))
    c=collections.Counter()
    for x in M:
        s=re.sub(r'Subject ID: \S+\.','',x['desc'])
        s=re.sub(r'\d+(\.\d+)?(,\d+)?V','<V>',s); s=re.sub(r'\d+(\.\d+)?k?Hz','<F>',s)
        c[s]+=1
    print("==",d,len(c))
    for k,v in c.items(): print(v, k[:2500]); print()
EOF
```

```
== 001030 1
17 2 kHz stimulation of hippocampal neurons under <V> amplitude (measured as one polarity, V; peak-to-peak would be two-fold larger). Sine wave amplitude is gradually increased during the initial 0.25 s, then stays constant at the indicated voltage. Sine wave stimulation begins at 25 ms and lasts 2 s. For the employed electrode configuration, <V> translates into 36 V/cm. All experiments were performed in a low-conductance physiological solution containing (in mM): 140 NaGluconate, 5.4 KCl, 2 CaCl2, 1.5 MgCl2, 10 D-glucose, and 10 HEPES (pH 7.3, 290-300 mOsm/kg, 0.8 S/m).

== 001032 2
138  A sine wave stimulation applied at <F> using <V> (peak-to-peak) amplitude. Note: this is not the actual amplitude measured on the oscilloscope, which will be somewhat smaller (calibration factors are frequency-dependent and will be reported separately after the calibration is completed). For the employed electrode configuration, <V> translates into 36 V/cm at the location of neurons. Neuron action potentials were visualized using the voltage-sensitive fluorescent dye, FluoVolt. All experiments were performed in a standard physiological solution containing (in mM): 140 NaCl, 5.4 KCl, 2 CaCl2, 1.5 MgCl2, 10 D-glucose, and 10 HEPES (pH 7.3, 290-300 mOsm/kg). The exposure system comprised a Siglent SDG1032X waveform generator (Siglent Technologies, Solon, OH), the 'EasywaveX' software, and a pair of tungsten electrodes (100 μm diameter, 140 μm inter-electrode gap) precisely positioned 50 µm above a chosen neuron using a robotic micromanipulator MPC-200 (Sutter Instrument, Novato, CA). Sine waves and modulated sine waves were generated using Excel software, uploaded to the Siglent generator, and exposure parameters (frequency, amplitude, and duration) were set. Exposure was triggered 50 ms after the start of fluorescence time-lapse recording. The applied electric field between electrodes was determined using a finite element method simulation (Sim4Life V5.2, Zurich Med Tech)
[... 41 more lines not kept]
```

**Agent**

No session in 001032 to 001035 is labelled as sodium gluconate, so Figure 3B can't be identified. Next: compare 001032 and 001034 data directly.

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && python - <<'EOF'
import json,h5py,remfile,numpy as np,re,collections
M2=json.load(open("meta_001032.json"));M4=json.load(open("meta_001034.json"))
def key(x,suf):
    p=x['path'].split('/')[1]; return re.sub(r'sub-(\d+)-'+suf,r'sub-\1',p)
k4={}
for x in M4: k4.setdefault(key(x,'3'),[]).append(x)
k2={}
for x in M2: k2.setdefault(key(x,'1'),[]).append(x)
print(len(k2),len(k4),len(set(k2)&set(k4)))
def load(u):
    with h5py.File(remfile.File(u),'r') as f:
        d=f['acquisition/TimeLapseImaging/data'][:]; st=f['session_start_time'][()]; r=f['acquisition/TimeLapseImaging/starting_time'].attrs['rate']
    return d,st,r
same=0;n=0
for k in sorted(set(k2)&set(k4))[:6]:
    a,sa,ra=load(k2[k][0]['url']); b,sb,rb=load(k4[k][0]['url'])
    print(k,a.shape,b.shape,sa,sb,ra,rb, a.shape==b.shape and np.array_equal(a,b))
EOF
```

```
178 178 116
sub-10_ses-2kHz-sine-stimulation-4V_image.nwb (1200, 16, 16) (1200, 16, 16) b'2024-05-09T22:42:04-04:00' b'2024-05-09T22:42:04-04:00' 3086.4 3086.4 True
sub-10_ses-2kHz-sine-stimulation-5-5V_image.nwb (1200, 16, 16) (1200, 16, 16) b'2024-05-09T22:44:00-04:00' b'2024-05-09T22:44:00-04:00' 3086.4 3086.4 True
sub-10_ses-2kHz-sine-stimulation-5V_image.nwb (1200, 16, 16) (1200, 16, 16) b'2024-05-09T22:43:32-04:00' b'2024-05-09T22:43:32-04:00' 3086.4 3086.4 True
sub-10_ses-2kHz-sine-stimulation-6-5V_image.nwb (1200, 16, 16) (1200, 16, 16) b'2024-05-09T22:45:13-04:00' b'2024-05-09T22:45:13-04:00' 3086.4 3086.4 True
sub-10_ses-2kHz-sine-stimulation-6V_image.nwb (1200, 16, 16) (1200, 16, 16) b'2024-05-09T22:44:40-04:00' b'2024-05-09T22:44:40-04:00' 3086.4 3086.4 True
sub-10_ses-2kHz-sine-stimulation-7-5V_image.nwb (1200, 16, 16) (1200, 16, 16) b'2024-05-09T22:46:11-04:00' b'2024-05-09T22:46:11-04:00' 3086.4 3086.4 True
Shell cwd was reset to
```

**Agent**

001034 is a second deposit of 001032 (identical arrays and start times); I'll count it once. Next, time loading all fast-imaging files and look at a few traces.

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && cat > loadall.py <<'EOF'
import json,h5py,remfile,numpy as np,time,sys,hashlib
from concurrent.futures import ThreadPoolExecutor
d=sys.argv[1]
M=json.load(open(f"meta_{d}.json"))
def load(x):
    for t in range(3):
        try:
            with h5py.File(remfile.File(x['url']),'r') as f:
                g=f['acquisition'][list(f['acquisition'].keys())[0]]
                a=g['data'][:]; r=g['starting_time'].attrs['rate']; st=f['session_start_time'][()].decode()
            return x['path'],a,r,st
        except Exception as e: err=e
    raise err
t=time.time()
with ThreadPoolExecutor(16) as ex: R=list(ex.map(load,M))
print(d,len(R),time.time()-t)
np.savez_compressed(f"cache_{d}.npz",**{p.replace('/','|'):a for p,a,r,st in R})
json.dump({p:dict(rate=r,start=st,shape=a.shape,h=hashlib.md5(a.tobytes()).hexdigest()) for p,a,r,st in R},open(f"info_{d}.json","w"))
EOF
for d in 001032 001033 001035 001030 001271 001272; do python loadall.py $d; done
```

```
001032 178 114.29517793655396
001033 193 122.46687030792236
001035 254 164.36447525024414
001030 17 18.538688898086548
001271 287 182.1055040359497
001272 65 41.12548065185547
Shell cwd was reset to
```

**Agent**

Loading takes about 10 minutes for all fast-imaging dandisets. Now check data duplicates across them, shapes and rates.

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . work/bin/activate && python - <<'EOF'
import json,collections
I={}
for d in ["001032","001033","001035","001030","001271","001272"]:
    for p,v in json.load(open(f"info_{d}.json")).items(): I[(d,p)]=v
h=collections.defaultdict(list)
for k,v in I.items(): h[v['h']].append(k)
d=[v for v in h.values() if len(v)>1]; print("dup groups",len(d)); [print(x) for x in d[:10]]
st=collections.defaultdict(list)
for k,v in I.items(): st[v['start']].append(k)
d=[v for v in st.values() if len(v)>1]; print("same start",len(d)); [print(x) for x in d[:10]]
for ds in ["001032","001033","001035","001030","001271","001272"]:
    print(ds,collections.Counter((tuple(v['shape']),v['rate']) for k,v in I.items() if k[0]==ds))
EOF
```

```
Sun Nov  1 15:34:36 UTC 2026
dup groups 0
same start 0
001032 Counter({((1200, 16, 16), 3086.4): 117, ((900, 16, 16), 3086.4): 59, ((1400, 16, 16), 3086.4): 1, ((1800, 16, 16), 3086.4): 1})
001033 Counter({((1200, 16, 16), 3086.4): 193})
001035 Counter({((1200, 16, 16), 3086.4): 253, ((6000, 16, 16), 3086.4): 1})
001030 Counter({((7000, 16, 16), 3134.8): 15, ((6000, 16, 16), 3134.8): 2})
001271 Counter({((1200, 16, 16), 3086.4): 287})
001272 Counter({((1200, 16, 16), 3086.4): 65})
Shell cwd was reset to
```

**Agent**

Now look at images and traces for one neuron to design the soma ROI and AP detection.

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && python - <<'EOF'
import numpy as np,json
Z=np.load("cache_001032.npz")
keys=sorted(k for k in Z.files if k.startswith("sub-10-1|"))
a=Z[keys[0]].astype(float)
m=a[:150].mean(0)
np.set_printoptions(linewidth=250,precision=0,suppress=True)
print(keys[0]); print(m)
for k in keys:
    a=Z[k].astype(float); fr=a.mean((1,2)); F0=fr[:150].mean(); dF=100*(fr-F0)/F0
    # mask: top pixels
    m=a[:150].mean(0); thr=(m.max()+m.min())/2; mk=m>thr
    s=a[:,mk].mean(1); dS=100*(s-s[:150].mean())/s[:150].mean()
    print(k.split('|')[1][:45], mk.sum(), "whole: max %.1f sd %.2f"%(dF[154:925].max(),dF[:150].std()), "mask: max %.1f sd %.2f"%(dS[154:925].max(),dS[:150].std()))
EOF
```

```
sub-10-1|sub-10-1_ses-2kHz-sine-stimulation-4-5V_obj-10w1in9_image.nwb
[[3164. 3586. 4915. 4600. 3839. 3602. 3450. 3257. 3395. 3215. 3934. 5425. 7360. 4947. 2638. 1882.]
 [3024. 4266. 5119. 4232. 4063. 4083. 3587. 3388. 3362. 3321. 3640. 4360. 6623. 5385. 2818. 2071.]
 [3110. 4770. 5089. 4133. 4061. 3778. 3703. 3613. 3572. 3360. 3344. 3784. 5627. 6783. 3027. 2199.]
 [4350. 4923. 4496. 3926. 3814. 3704. 3535. 3525. 3442. 3131. 3063. 3316. 4491. 6891. 4264. 2360.]
 [4787. 5473. 4397. 3898. 3668. 3472. 3320. 3250. 3042. 2878. 2841. 3141. 3993. 5685. 5943. 3908.]
 [4165. 5351. 4518. 3938. 3440. 3127. 2896. 2836. 2738. 2703. 2715. 2975. 3564. 4511. 6558. 6138.]
 [3818. 5346. 4813. 3837. 3246. 2832. 2680. 2639. 2662. 2668. 2664. 2791. 3137. 3718. 5372. 6395.]
 [3892. 5602. 4923. 3679. 3017. 2667. 2600. 2664. 2774. 2833. 2768. 2696. 2839. 3270. 4545. 5355.]
 [4982. 6153. 4834. 3426. 2867. 2620. 2649. 2884. 3348. 3419. 3052. 2854. 2762. 3134. 4205. 5243.]
 [5620. 6279. 4373. 3203. 2835. 2643. 2807. 3378. 4300. 3947. 3139. 2880. 2903. 2984. 3831. 5383.]
 [5090. 5285. 4045. 3082. 2745. 2689. 2938. 3775. 4346. 4018. 3435. 3074. 2921. 3028. 3646. 4803.]
 [4669. 5410. 4338. 3059. 2688. 2700. 2971. 3364. 3543. 3701. 3647. 3311. 2937. 3047. 3680. 4869.]
 [3852. 6318. 5015. 3177. 2778. 2643. 2662. 2803. 2772. 3083. 3282. 3125. 2916. 2962. 3564. 4627.]
 [3403. 5554. 5425. 3592. 2845. 2629. 2500. 2504. 2498. 2583. 2757. 2807. 2905. 3026. 3605. 4302.]
 [3094. 3514. 3994. 4224. 3178. 2758. 2637. 2606. 2498. 2534. 2570. 2667. 2919. 3283. 3981. 4034.]
 [2232. 2018. 2414. 3878. 3995. 3111. 2861. 2747. 2526. 2457. 2563. 2605. 2886. 3524. 4216. 3654.]]
sub-10-1_ses-2kHz-sine-stimulation-4-5V_obj-1 45 whole: max 12.9 sd 17.68 mask: max 12.5 sd 16.09
sub-10-1_ses-2kHz-sine-stimulation-4-5V_obj-g 39 whole: max 13.9 sd 15.20 mask: max 11.8 sd 16.12
sub-10-1_ses-2kHz-sine-stimulation-4V_image.n 41 whole: max 13.9 sd 11.96 mask: max 12.0 sd 14.59
[... 15 more lines not kept]
```

**Agent**

Pre-stimulus SD is very large; look at the raw time course.

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && python - <<'EOF'
import numpy as np
Z=np.load("cache_001032.npz")
keys=sorted(k for k in Z.files if k.startswith("sub-10-1|"))
np.set_printoptions(linewidth=250,precision=0,suppress=True)
a=Z[keys[2]].astype(float); fr=a.mean((1,2))
print(keys[2]); print(fr[:40]); print(fr[140:200]); 
print(np.round(fr.reshape(-1,20).mean(1)))
EOF
```

```
sub-10-1|sub-10-1_ses-2kHz-sine-stimulation-4V_image.nwb
[10904.  4193.  4206.  4212.  4253.  4300.  4285.  4339.  4349.  4381.  4343.  4370.  4370.  4425.  4308.  4366.  4415.  4436.  4381.  4401.  4428.  4418.  4408.  4425.  4426.  4402.  4398.  4415.  4402.  4418.  4372.  4382.  4416.  4424.  4423.
  4382.  4396.  4453.  4400.  4355.]
[4362. 4373. 4394. 4425. 4380. 4406. 4421. 4367. 4379. 4368. 4370. 4403. 4423. 4411. 4387. 4467. 4420. 4428. 4377. 4376. 4374. 4459. 4415. 4468. 4382. 4454. 4430. 4352. 4417. 4380. 4345. 4400. 4399. 4453. 4387. 4405. 4403. 4416. 4431. 4416. 4447.
 4364. 4389. 4424. 4453. 4432. 4442. 4394. 4436. 4437. 4422. 4491. 4461. 4470. 4381. 4479. 4378. 4507. 4480. 4527.]
[4662. 4407. 4413. 4405. 4407. 4407. 4404. 4397. 4409. 4441. 4682. 4417. 4394. 4406. 4384. 4386. 4404. 4406. 4407. 4665. 4444. 4394. 4391. 4371. 4368. 4376. 4374. 4378. 4392. 4407. 4653. 4407. 4376. 4364. 4352. 4358. 4371. 4369. 4376. 4385. 4569.
 4492. 4371. 4352. 4350. 4354. 4362. 4337. 4339. 4335. 4340. 4334. 4344. 4331. 4337. 4343. 4340. 4338. 4347. 4342.]
Shell cwd was reset to
```

**Agent**

The first frame of each session is a bright artifact (excluded from F0); single-frame noise is about 0.6% and APs about 6%. Now tabulate neurons, dates and conditions in the fast-imaging sets.

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && python - <<'EOF'
import json,collections,re
for d in ["001032","001033","001035","001271","001272","001030"]:
    M=json.load(open(f"meta_{d}.json")); I=json.load(open(f"info_{d}.json"))
    print("==",d)
    by=collections.defaultdict(list)
    for x in M:
        s=x['path'].split('/')[0]
        by[s].append((I[x['path']]['start'][:16],x['name'] if d not in("001271","001272") else re.search(r'Stimulation was applied with (.*?)\. The experiment was performed (\w+)',x['desc']).group(0)[28:120]))
    for s,v in sorted(by.items(), key=lambda kv: min(t for t,_ in kv[1])):
        v=sorted(v); days=sorted(set(t[:10] for t,_ in v))
        c=collections.Counter(re.sub(r'_[\d.,]+V$','',n) if d not in("001271","001272") else ('TTX' if 'without' not in n else 'veh')+' '+re.sub(r'with [\d.,]+V','',n.split('. The')[0]) for _,n in v)
        print(s,days,v[0][0][11:],v[-1][0][11:],dict(c))
EOF
```

```
== 001032
sub-1-1 ['2024-05-09'] 20:30 20:38 {'20Hz_sine_stimulation': 8, '2kHz_spindle_stimulation': 1}
sub-2-1 ['2024-05-09'] 20:43 21:01 {'20Hz_sine_stimulation': 2, '2kHz_spindle_stimulation': 8, '2kHz_sine_stimulation': 9}
sub-3-1 ['2024-05-09'] 21:05 21:21 {'20Hz_sine_stimulation': 5, '2kHz_spindle_stimulation': 3, '2kHz_sine_stimulation': 9}
sub-4-1 ['2024-05-09'] 21:27 21:28 {'20Hz_sine_stimulation': 4}
sub-5-1 ['2024-05-09'] 21:32 21:46 {'20Hz_sine_stimulation': 2, '2kHz_spindle_stimulation': 6, '2kHz_sine_stimulation': 7}
sub-6-1 ['2024-05-09'] 21:53 22:05 {'2kHz_sine_stimulation': 4, '2kHz_spindle_stimulation': 6, '20Hz_sine_stimulation': 4}
sub-7-1 ['2024-05-09'] 22:12 22:24 {'2kHz_sine_stimulation': 12, '2kHz_spindle_stimulation': 3}
sub-8-1 ['2024-05-09'] 22:28 22:30 {'2kHz_spindle_stimulation': 4}
sub-9-1 ['2024-05-09'] 22:32 22:38 {'2kHz_spindle_stimulation': 2, '2kHz_sine_stimulation': 8}
sub-10-1 ['2024-05-09'] 22:42 22:54 {'2kHz_sine_stimulation': 10, '2kHz_spindle_stimulation': 7}
sub-11-1 ['2024-05-09'] 23:02 23:13 {'2kHz_sine_stimulation': 5, '20kHz_sine_stimulation': 14}
sub-12-1 ['2024-05-09'] 23:18 23:23 {'2kHz_sine_stimulation': 7}
sub-13-1 ['2024-05-09'] 23:26 23:37 {'2kHz_sine_stimulation': 4, '20kHz_sine_stimulation': 9}
sub-14-1 ['2024-05-09'] 23:33 23:46 {'2kHz_sine_stimulation': 5, '20kHz_sine_stimulation': 10}
== 001033
sub-1-2 ['2024-05-13'] 18:08 18:12 {'20Hz_sine_stimulation': 8}
sub-2-2 ['2024-05-13'] 18:15 18:27 {'20Hz_sine_stimulation': 2, '2kHz_sine_stimulation': 7, '2kHz_spindle_stimulation': 10}
sub-3-2 ['2024-05-13'] 18:31 18:41 {'2kHz_spindle_stimulation': 6, '2kHz_sine_stimulation': 15}
sub-4-2 ['2024-05-13'] 18:46 18:55 {'20Hz_sine_stimulation': 4, '50Hz_sine_stimulation': 4, '100Hz_sine_stimulation': 1, '500Hz_sine_stimulation': 1}
[... 66 more lines not kept]
```

**Agent**

Read the Results for Figures 1 to 3 to match the conditions.

**Agent calls Bash**

```bash
cd $TMPDIR && grep -n "" paper.txt | sed -n 60,100p | cut -c1-260
```

```
60:beats. As the field strength increased, single APs emerged near the peak of each beat, so the firing rate equaled the modulation rate, and the number of evoked APs equaled the number of beats ( Figures 2A and 2B ). At the highest field strengths, 
61:each beat could elicit a pair of APs, so the maximum number of APs evoked by five beats was limited to ten. Unlike pure sine waves, modulated stimuli did not trigger sustained firing or sustained depolarization. Figure 2. Modulated sine waves 
62:stimulate less efficiently and elicit different firing patterns compared to unmodulated sine waves (A) Effect of the electric field strength (V/cm) on the response of a representative neuron to a 250-ms-long, 2-kHz sine wave modulated at 20 Hz. The 
63:same neuron was also tested by unmodulated 2-kHz sine waves just above the excitation threshold (lower traces). The stimulation signals (2 kHz/20 Hz and 2 kHz) are shown underneath the traces. See Figure 1 and the main text for more details. (B) 
64:Same as (A) but for 20-kHz carrier frequency. (C) Comparison of firing patterns when the same neuron was stimulated by modulated and unmodulated sine waves at the same electric field strengths. (D) Electric field thresholds for 2- and 20-kHz sine 
65:waves, with and without 20-Hz amplitude modulation. The thresholds were defined as the minimum electric field strength that elicits 1 or 5 action potentials (APs #1 and #5) during a 250-ms-long stimulation. Bars represent the threshold means ± SEM 
66:for n individual neurons in each group. * p < 0.02 for the difference in thresholds of modulated and unmodulated signals, with a two-tailed unpaired t test. When modulated and unmodulated sine waves of the same carrier frequency were tested in the 
67:same cell, the threshold was typically lower for unmodulated signals ( Figures 2A - 2C ). At the same field strengths, pure sine waves triggered a larger number of APs ( Figure 2C ). This finding questioned the core idea of TI stimulation, w
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -n 38,60p paper.txt | cut -c1-260
```

```
neurons. When synaptic transmission was blocked, pure sine waves excited both PV and pyramidal neurons. The activation thresholds for PV neurons by pure and modulated sinusoids were similar, and the firing rate was higher with pure ones. Peripheral 
nerve fibers can be excited by pure sine waves even at frequencies as high as 50–100 kHz. 30 , 33 , 34 The stimulation threshold for a giant non-myelinated motor nerve of a locust in the 0.5–12.5 kHz carrier frequency range was not reduced by 1-Hz 
amplitude modulation, no matter whether a premodulated sine wave was delivered with a pair of electrodes or it was created as amplitude beats using the TI approach. 30 Likewise, 1-Hz modulation did not lower the motor nerve excitation threshold in 
human volunteers. For sensory nerve stimulation, TI thresholds were about 30% lower than those for unmodulated sine waves across the entire 0.5–12.5 kHz carrier frequency range. However, this small difference was likely a psychophysiological effect 
of more acute perception of intermittent signals compared to continuous ones and did not indicate a difference in stimulation mechanism. 30 The above studies complement each other, making a strong case that pure high-frequency sinusoids have a high 
potency to elicit or modify neural activity. This conclusion challenges TI studies in animal and human brains that reported negligible or no off-target stimulation near the electrodes. The fundamental importance of this dispute for TI applications 
has motivated us to compare excitation by pure and modulated high-frequency sine waves in isolated neurons. Electrophysiological recordings are inherently prone to electric interference pickup from the electric field oscillations, requiring heavy 
filtering. In active feedback systems like current clamp, such interference can induce erroneous command signals, leading to unpredictable outcomes. To eliminate potential artifacts, we opted for a fast optical detection of APs. We demonstrate that 
the n
[... 15 more lines not kept]
```

**Agent**

I'll prototype AP detection on all 2-kHz and 20-kHz sessions of 001032 to check it behaves.

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . work/bin/activate && cat > proto.py <<'EOF'
import numpy as np,json,re
from scipy.signal import find_peaks
RATE=3086.4; ON=int(round(0.05*RATE)); OFF=ON+int(round(0.25*RATE))
def traces(a):
    a=a.astype(float); m=a[1:ON].mean(0)
    mk=m>np.median(m)
    out={}
    for name,s in [("whole",a.mean((1,2))),("bright",a[:,mk].mean(1))]:
        F0=s[1:ON].mean(); out[name]=100*(s-F0)/F0
    return out
def aps(dF,reading):
    w=int(round(0.005*RATE))
    if reading=="a":
        p,_=find_peaks(dF,height=5,distance=w,prominence=2.5)
    else:
        p,_=find_peaks(dF,distance=w)
        p=np.array([i for i in p if i>=w and dF[i]-dF[i-w:i].min()>=5],int)
    return p[(p>=ON)&(p<OFF+w)]
if __name__=="__main__":
    Z=np.load("cache_001032.npz")
    for k in sorted(Z.files):
        if '20Hz' in k: continue
        T=traces(Z[k]); s=k.split('|')[1]
        r=[len(aps(T[roi],rd)) for roi in T for rd in "ab"]
        print(k.split('|')[0], re.search(r'ses-(.*?)_(obj|image)',s).group(1), r, "pre sd %.2f"%T['whole'][1:ON].std(), "last100 %.1f"%T['whole'][OFF-309:OFF].mean())
EOF
python proto.py | head -120
```

```
Sun Nov  1 15:35:45 UTC 2026
sub-1-1 2kHz-spindle-stimulation-8V [0, 0, 0, 0] pre sd 1.01 last100 -0.6
sub-10-1 2kHz-sine-stimulation-4-5V [5, 5, 6, 5] pre sd 0.85 last100 1.0
sub-10-1 2kHz-sine-stimulation-4-5V [7, 7, 7, 7] pre sd 0.95 last100 1.0
sub-10-1 2kHz-sine-stimulation-4V [4, 4, 4, 4] pre sd 0.95 last100 -0.1
sub-10-1 2kHz-sine-stimulation-5-5V [12, 12, 12, 12] pre sd 0.93 last100 3.0
sub-10-1 2kHz-sine-stimulation-5V [9, 9, 9, 9] pre sd 0.77 last100 1.9
sub-10-1 2kHz-sine-stimulation-6-5V [17, 17, 17, 17] pre sd 0.87 last100 4.3
sub-10-1 2kHz-sine-stimulation-6V [15, 15, 16, 15] pre sd 0.94 last100 3.7
sub-10-1 2kHz-sine-stimulation-7-5V [18, 18, 18, 16] pre sd 0.93 last100 5.1
sub-10-1 2kHz-sine-stimulation-7V [18, 18, 18, 18] pre sd 0.99 last100 4.8
sub-10-1 2kHz-sine-stimulation-8V [18, 5, 20, 12] pre sd 0.85 last100 5.0
sub-10-1 2kHz-spindle-stimulation-4-5V [3, 3, 3, 3] pre sd 0.93 last100 -0.1
sub-10-1 2kHz-spindle-stimulation-5V [7, 2, 13, 2] pre sd 0.82 last100 2.6
sub-10-1 2kHz-spindle-stimulation-5V [5, 5, 6, 5] pre sd 0.84 last100 1.2
sub-10-1 2kHz-spindle-stimulation-5V [7, 2, 16, 2] pre sd 0.89 last100 4.3
sub-10-1 2kHz-spindle-stimulation-6V [5, 5, 5, 5] pre sd 0.89 last100 1.5
sub-10-1 2kHz-spindle-stimulation-7V [6, 5, 8, 5] pre sd 0.87 last100 1.6
sub-10-1 2kHz-spindle-stimulation-8V [11, 6, 15, 6] pre sd 0.88 last100 4.5
sub-11-1 20kHz-sine-stimulation-10V [2, 2, 2, 3] pre sd 0.97 last100 -0.4
[... 102 more lines not kept]
```

**Agent**

AP detection behaves sensibly and the two readings mostly agree near threshold. Now get shapes for every 001274 strobe file and tabulate sessions per subject.

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && python - <<'EOF'
import json,h5py,remfile,re,collections
from concurrent.futures import ThreadPoolExecutor
M=json.load(open("meta_001274.json"))
def f(x):
    with h5py.File(remfile.File(x['url']),'r') as h:
        g=h['acquisition/StrobeImaging']; return x['path'],g['data'].shape,g['starting_time'][()],h['session_start_time'][()].decode()
with ThreadPoolExecutor(16) as ex: R=list(ex.map(f,M))
S={p:(s,t,st) for p,s,t,st in R}
def kind(d):
    if 'rectangular pulse' in d: k='pulse'
    elif '100Hz' in d: k='sp100'
    elif '154Hz' in d: k='sp154'
    else: k='sine'
    v=re.search(r'at ([\d,]+)V',d).group(1)
    ttx='TTX' if 'presence of the sodium' in d else 'veh'
    dirn='fwd' if 'forward manner' in d else ('bwd' if 'backward' in d else '?')
    return k,v,ttx,dirn
rows=[]
for x in M:
    k=kind(x['desc']); s,t,st=S[x['path']]
    rows.append(dict(path=x['path'],sub=x['path'].split('/')[0],kind=k[0],V=k[1],ttx=k[2],dir=k[3],n=s[0],start=st,size=x['size']))
json.dump(rows,open("rows_001274.json","w"))
by=collections.defaultdict(list)
for r in rows: by[r['sub']].append(r)
for s in sorted(by,key=lambda s:min(r['start'] for r in by[s])):
    v=sorted(by[s],key=lambda r:r['start'])
    print(s, v[0]['start'][11:16], v[-1]['start'][11:16], dict(collections.Counter((r['kind'],r['V'],r['ttx'],r['dir'],r['n']) for r in v)))
EOF
```

```
sub-1-20240522 22:12 22:20 {('pulse', '10,0', 'veh', 'fwd', 140): 2, ('sine', '10,0', 'veh', 'fwd', 300): 1}
sub-2-20240522 22:27 22:48 {('pulse', '10,0', 'veh', 'fwd', 140): 2, ('sine', '5,0', 'veh', 'fwd', 300): 2, ('sp100', '5,0', 'veh', 'fwd', 500): 5}
sub-3-20240522 22:56 23:11 {('pulse', '10,0', 'veh', 'fwd', 140): 1, ('sine', '7,0', 'veh', 'fwd', 300): 1, ('sp100', '7,0', 'veh', 'fwd', 500): 4}
sub-4-20240522 23:24 23:38 {('pulse', '15,0', 'veh', 'fwd', 140): 1, ('sine', '7,0', 'veh', 'fwd', 300): 3, ('sp100', '7,0', 'veh', 'fwd', 500): 4}
sub-1-20240523 19:56 19:56 {('pulse', '10,0', 'veh', 'fwd', 140): 1}
sub-2-20240523 20:03 20:26 {('pulse', '10,0', 'veh', 'fwd', 140): 1, ('sp100', '7,0', 'veh', 'fwd', 500): 4, ('sp154', '7,0', 'veh', 'fwd', 325): 4}
sub-3-20240523 20:35 20:52 {('pulse', '10,0', 'veh', 'fwd', 140): 1, ('sp154', '7,0', 'veh', 'fwd', 325): 4, ('sp100', '7,0', 'veh', 'fwd', 500): 4}
sub-4-20240523 21:03 21:21 {('pulse', '10,0', 'veh', 'fwd', 140): 1, ('sp100', '7,0', 'veh', 'fwd', 500): 4, ('sp154', '7,0', 'veh', 'fwd', 325): 3}
sub-5-20240523 21:31 21:49 {('pulse', '10,0', 'veh', 'fwd', 140): 1, ('sp154', '7,0', 'veh', 'fwd', 325): 4, ('sp100', '7,0', 'veh', 'fwd', 500): 4}
sub-6-20240523 22:16 22:31 {('pulse', '10,0', 'veh', 'fwd', 140): 1, ('sp100', '7,0', 'veh', 'fwd', 500): 4, ('sp154', '7,0', 'veh', 'fwd', 325): 4}
sub-7-20240523 22:37 22:52 {('pulse', '10,0', 'veh', 'fwd', 140): 1, ('sp154', '7,0', 'veh', 'fwd', 325): 4, ('sp100', '7,0', 'veh', 'fwd', 500): 4}
sub-8-20240523 22:54 23:06 {('sp154', '7,0', 'veh', 'fwd', 325): 4, ('sp100', '7,0', 'veh', 'fwd', 500): 4}
sub-9-20240523 23:10 23:21 {('sp154', '7,0', 'veh', 'fwd', 325): 4, ('sp100', '7,0', 'veh', 'fwd', 500): 4}
sub-1-20240824 18:10 19:13 {('pulse', '10,0', 'veh', 'fwd', 160): 4, ('pulse', '10,0', 'veh', 'bwd', 160): 4, ('sp154', '7,0', 'veh', 'fwd', 325): 8, ('sp154', '7,0', 'TTX', 'fwd', 325): 8, ('pulse', '10,0', 'TTX', 'fwd', 160): 4, ('pulse', '10,0', 'TTX', 'bwd', 160):
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && python - <<'EOF'
import json,re,collections
for d in ["001032","001033"]:
    M=json.load(open(f"meta_{d}.json"))
    print(d,collections.Counter(re.search(r'A spindle \(sine wave modulated at (\S+) frequency\) stimulation applied at (\S+)',x['desc']).groups() for x in M if 'spindle' in x['desc']))
    print(collections.Counter(re.search(r'applied at (\S+) using',x['desc']).group(1) for x in M if 'spindle' not in x['desc']))
EOF
```

```
001032 Counter({('20Hz', '2kHz'): 40})
Counter({'2kHz': 80, '20kHz': 33, '20Hz': 25})
001033 Counter({('20Hz', '2kHz'): 31, ('20Hz', '20kHz'): 13})
Counter({'2kHz': 56, '20kHz': 47, '20Hz': 33, '50Hz': 4, '40kHz': 3, '100Hz': 1, '500Hz': 1, '160Hz': 1, '1280Hz': 1, '320Hz': 1, '640Hz': 1})
Shell cwd was reset to
```

**Agent**

Spindles are 2- or 20-kHz carriers modulated at 20 Hz, as in the paper. Now I'll write the helper module.

**Agent calls Bash**

```bash
mkdir -p entries/001274-semenov-2025; cat entries/001453-fouke-2025/README.md | head -30; python tools/entry.py --help 2>&1 | head; ls schemas; grep -n "relation\|runtime" schemas/*entry* | head
```

```
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
| Values from representative trials (Figure 1C, E, F) | Blocked: metadata insufficient |
[... 27 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/001274-semenov-2025/ti_sine.py",
 "content": "\"\"\"Loading and measures for the optical recordings of Semenov, Kim, Silkuniene & Pakhomov (2025).\n\nCell Reports Physical Science 6, 102660, doi:10.1016/j.xcrp.2025.102660.\n\nThe paper deposited its raw images in ten dandisets (Data and code availability). The target,\nDANDI:001274, holds the pulsed laser strobe images of Figures 5, 6 and S3. The claims file assigns\nthe fast optical recordings of Figures 1 to 3, S1 and S2 to other dandisets of the same paper\n(`data: elsewhere`), read here at their pinned published versions (`VERSIONS`).\n\nEvery file holds one image stack (`acquisition/<name>/data`, frames x rows x columns, uint16) and\nnothing else: no ROIs, no traces, no stimulus waveform and no trial table. The stimulus of a\nsession is read from its session description (frequency, modulation, voltage, tetrodotoxin).\nFiles are streamed from the archive; each stack is reduced to two traces as it loads.\n\nWhere the parameters come from:\n\n- Stimulus timing. The fast recordings start the stimulus 50 ms after the start of imaging and\n  last 250 ms (Methods, \"Recording of the optical APs\": \"The standard imaging protocol started 50\n  ms before sine wave stimulation and continued for 250 ms\"; the files' descriptions say the same).\n  The 2-s recordings of DANDI:001030 start it at 25 ms (their description). The first frame of\n  every fast recording is a bright camera artifact (about 2.5 times the others) and is left out\n  of F0, a standard choice that cannot change a result.\n- F and dF. dF = 100% (F - F0) / F0 with F0 the mean before the stimulus (Methods). F is the\n  emission \"over the entire cell soma\" (Methods); the files have 16 x 16 pixels and no soma\n  outline, so two readings are run (assumption, see the notebook): `whole`, the mean of the\n  whole frame, and `bright`, the mean of the pixels brighter than the median of the\n  pre-stimulus mean image.\n- AP detection. The Methods give \"APs were readily identifiable as brief emission upticks\" in\n  neurons whose APs peak above 5% dF and last about 10 ms. The claims file names two readings:\n  (a) a peak of dF above 5%; (b) a rise of at least 5% dF within 5 ms. Peaks closer than 5 ms\n  are merged in both (a standard choice; APs last about 8 ms, Methods), and in (a) a peak must\n  stand 2.5% above its surroundings (scipy prominence; a standard choice, half the 5% level, to\n  keep noise on a depolarized plateau from counting as APs; pre-stimulus SD is about 1%).\n- Field. The session descriptions give the generator voltage, peak to peak, and say \"1V\n  translates into 36 V/cm at the location of neurons\" (DANDI:001030 says its voltages are of\n  one polarity, \"peak-to-peak would be two-fold larger\"). The claims file takes the field from\n  the dataset's metadata; two readings are run (assumption, see the notebook): `half`, field =\n  36 V/cm x Vpp / 2, the peak field, and `full`, field = 36 V/cm x Vpp.\n- Strobe images (DANDI:001274). RATIO image as in the Methods (\"Pulsed laser fluorescence\n  microscopy\"): CONTROL is the mean of the frames before the pulse, POLARIZED the mean of the\n  frames of the last 0.5 us of the pulse, both low-pass filtered over 12 x 12 pixels; RATIO =\n  1000 x POLARIZED / CONTROL. The frame times are not in the files; their description says\n  \"Exposures began 1 us after the start of recording\", and the Methods give 50-ns steps from 1\n  us before the pulse, so frame i is at -1 + 0.05 i us (assumption, see the notebook).\n\"\"\"\n\nfrom __future__ import annotations\n\nimport json\nimport re\nimport urllib.request\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport h5py\nimport numpy as np\nimport remfile\nfrom scipy.ndimage import uniform_filter\nfrom scipy.signal import find_peaks\n\nAPI = \"https://api.dandiarchive.org/api\"\nVERSIONS = {\n    \"001274\": \"0.250805.1401\",  # strobe imaging, Figures 5, 6, S3 (the target)\n    \"001273\": \"0.250805.1356\",  # 2-us pulse kinetics, Figure 4\n    \"001030\": \"0.240520.1924\",  # 2-s ramped 2-kHz sine waves in NaGlu, Figure 3C\n    \"001032\": \"0.240527.1432\",  # 2- and 20-kHz sine waves, modulated and not (Figures 1, 2)\n    \"001033\": \"0.240527.1432\",\n    \"001034\": \"0.240527.1431\",  # a second deposit of 001032 (see the notebook)\n    \"001035\": \"0.240527.1432\",\n    \"001271\": \"0.250805.1352\",  # tetrodotoxin, Figure S2\n    \"001272\": \"0.250805.1358\",  # Di-8-ANEPPS, Figure S1\n}\nV_TO_V_PER_CM = 36.0          # session descriptions: \"1V translates into 36 V/cm\"\nAP_LEVEL = 5.0                # % dF, Methods\nAP_WIDTH_S = 0.005            # 5 ms: rise window of reading (b) and the merge distance\nPROMINENCE = 2.5              # % dF, reading (a), standard choice\nSTIM_START_S = 0.050          # fast recordings, Methods\nSTIM_DUR_S = 0.250\nROIS = (\"whole\", \"bright\")\nAP_READINGS = (\"a\", \"b\")\n\n\ndef _get(url):\n    with urllib.request.urlopen(url, timeout=120) as r:\n        return json.load(r)\n\n\ndef list_assets(dandiset, threads=16):\n    \"\"\"Assets of a dandiset at its pinned version, with S3 URL and session description.\"\"\"\n    version = VERSIONS[dandiset]\n    base = f\"{API}/dandisets/{dandiset}/versions/{version}/assets/\"\n    assets, url = [], base + \"?page_size=1000\"\n    while url:\n        page = _get(url)\n        assets += page[\"results\"]\n        url = page[\"next\"]\n\n    def meta(a):\n        m = _get(base + a[\"asset_id\"] + \"/\")\n        ses = [w for w in m[\"wasGeneratedBy\"] if w[\"schemaKey\"] == \"Session\"][0]\n        s3 = [u for u in m[\"contentUrl\"] if \"s3\" in u][0]\n        return dict(path=a[\"path\"], size=a[\"size\"], url=s3, session=ses[\"name\"],\n                    description=ses.get(\"description\", \"\"))\n\n    with ThreadPoolExecutor(threads) as ex:\n        return sorted(ex.map(meta, assets), key=lambda r: r[\"path\"])\n\n\ndef parse_fast(desc, session=\"\"):\n    \"\"\"Stimulus of a fast recording from its session description.\"\"\"\n    d = dict(tetrodotoxin=\"presence of the sodium channel inhibitor\" in desc,\n             sham=\"sham\" in desc.lower() or \"sham\" in session.lower())\n    m = re.search(r\"modulated at (\\S+?)Hz frequency\\) stimulation applied at (\\S+?)Hz using \"\n                  r\"([\\d.,]+)V\", desc)\n    if m:\n        d.update(modulated=True, carrier=m.group(2), voltage=float(m.group(3).replace(\",\", \".\")))\n        return d\n    m = re.search(r\"applied at (\\S+?)Hz using ([\\d.,]+)V\", desc)\n    if m:\n        d.update(modulated=False, carrier=m.group(1), voltage=float(m.group(2).replace(\",\", \".\")))\n        return d\n    m = re.search(r\"sine wave at (\\S+?)Hz with ([\\d.,]+)V\", desc)\n    if m:\n        d.update(modulated=False, carrier=m.group(1), voltage=float(m.group(2).replace(\",\", \".\")))\n        return d\n    m = re.search(r\"under ([\\d.,]+)V amplitude\", desc)      # DANDI:001030, one polarity\n    if m:\n        d.update(modulated=False, carrier=\"2k\", voltage=2 * float(m.group(1).replace(\",\", \".\")))\n        return d\n    d.update(modulated=False, carrier=None, voltage=0.0)\n    return d\n\n\ndef field(vpp, reading=\"half\"):\n    \"\"\"Electric field (V/cm) from the generator voltage, peak to peak (see module docstring).\"\"\"\n    return V_TO_V_PER_CM * vpp * (0.5 if reading == \"half\" else 1.0)\n\n\ndef _reduce(stack, onset):\n    \"\"\"Two dF traces (%) from an image stack: whole frame and bright pixels.\"\"\"\n    a = stack.astype(np.float64)\n    pre = a[1:onset].mean(0)\n    mask = pre > np.median(pre)\n    out = {}\n    for name, s in ((\"whole\", a.mean((1, 2))), (\"bright\", a[:, mask].mean(1))):\n        f0 = s[1:onset].mean()\n        out[name] = (100.0 * (s - f0) / f0).astype(np.float32)\n    out[\"mean_image\"] = pre.astype(np.float32)\n    return out\n\n\ndef load_fast(assets, stim_start_s=STIM_START_S, threads=24):\n    \"\"\"Stream every fast recording and reduce it to dF traces as it loads.\"\"\"\n    def one(a):\n        for attempt in range(4):\n            try:\n                with h5py.File(remfile.File(a[\"url\"]), \"r\") as f:\n                    g = f[\"acquisition\"][list(f[\"acquisition\"].keys())[0]]\n                    stack = g[\"data\"][:]\n                    rate = float(g[\"starting_time\"].attrs[\"rate\"])\n                    start = f[\"session_start_time\"][()].decode()\n                break\n            except OSError:\n                if attempt == 3:\n                    raise\n        onset = int(round(stim_start_s * rate))\n        r = dict(a, rate=rate, start=start, n_frames=stack.shape[0], shape=stack.shape,\n                 onset=onset, first_frame_ratio=float(stack[0].mean() / stack[1:onset].mean()),\n                 raw_f0=float(stack[1:onset].mean()))\n        r.update(_reduce(stack, onset))\n        return r\n\n    with ThreadPoolExecutor(threads) as ex:\n        return list(ex.map(one, assets))\n\n\ndef detect_aps(dF, rate, reading=\"a\", level=AP_LEVEL, invert=False):\n    \"\"\"Frame indices of AP peaks under reading (a) or (b) (module docstring).\"\"\"\n    x = -dF if invert else dF\n    w = int(round(AP_WIDTH_S * rate))\n    if reading == \"a\":\n        p, _ = find_peaks(x, height=level, distance=w, prominence=PROMINENCE)\n    else:\n        p, _ = find_peaks(x, distance=w)\n        p = np.array([i for i in p if i >= w and x[i] - x[i - w:i].min() >= level], dtype=int)\n    return p\n\n\ndef aps_in_window(dF, rate, onset, dur_s=STIM_DUR_S, reading=\"a\", level=AP_LEVEL, invert=False):\n    \"\"\"AP peak times (s from stimulus onset) during the stimulus, plus 5 ms for the last AP.\"\"\"\n    p = detect_aps(dF, rate, reading, level, invert)\n    end = onset + int(round((dur_s + AP_WIDTH_S) * rate))\n    p = p[(p >= onset) & (p < end)]\n    return (p - onset) / rate\n\n\ndef window_mean(dF, rate, onset, t0, t1, invert=False):\n    \"\"\"Mean dF (%) from t0 to t1 s after stimulus onset.\"\"\"\n    x = -dF if invert else dF\n    return float(x[onset + int(round(t0 * rate)):onset + int(round(t1 * rate))].mean())\n\n\n# --- strobe images (DANDI:001274) ---------------------------------------------------------\n\ndef frame_times_pulse(n):\n    \"\"\"Frame times (us from pulse onset) of a 2-us pulse recording: 50-ns steps from -1 us.\"\"\"\n    return -1.0 + 0.05 * np.arange(n)\n\n\ndef ratio_image(stack, t):\n    \"\"\"RATIO image of the Methods (1000 = no change) from a pulse stack and its frame times.\"\"\"\n    a = stack.astype(np.float64)\n    control = a[t < 0].mean(0)\n    polarized = a[(t >= 1.5) & (t < 2.0)].mean(0)\n    control = uniform_filter(control, 12)\n    polarized = uniform_filter(polarized, 12)\n    return 1000.0 * polarized / control, control\n\n\ndef rebuilt_rois(ratio, control, size=8, cell_quantile=0.75):\n    \"\"\"ROI 1 and 2 rebuilt from the RATIO image: size x size pixel squares centred on its\n    minimum (most hyperpolarized) and maximum (most depolarized) within the cell, the cell\n    being the pixels of the filtered CONTROL image above `cell_quantile`. A variant only: the\n    paper's ROIs were drawn by hand and are not in the dataset.\"\"\"\n    cell = control > np.quantile(control, cell_quantile)\n    r = np.where(cell, ratio, np.nan)\n    i1 = np.unravel_index(np.nanargmin(r), r.shape)\n    i2 = np.unravel_index(np.nanargmax(r), r.shape)\n    h = size // 2\n\n    def box(i):\n        m = np.zeros(r.shape, bool)\n        m[max(i[0] - h, 0):i[0] + h, max(i[1] - h, 0):i[1] + h] = True\n        return m\n\n    return box(i1), box(i2), cell\n\n\ndef load_strobe(url, rois=None):\n    \"\"\"Stream a strobe stack; return the stack's per-frame means in the given masks, or the\n    stack itself when no masks are given.\"\"\"\n    with h5py.File(remfile.File(url), \"r\") as f:\n        stack = f[\"acquisition/StrobeImaging/data\"][:]\n    if rois is None:\n        return stack\n    return {k: stack[:, m].mean(1) for k, m in rois.items()}\n"
}
```

```
File created successfully at: entries/001274-semenov-2025/ti_sine.py (file state is current in your context — no need to Read it back)
```

**Agent**

Now a scratch harness that builds the same records from the cached stacks, so I can develop the analyses quickly.

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && cat > dev.py <<'EOF'
import sys,json,numpy as np,pickle
sys.path.insert(0,"entries/001274-semenov-2025")
import ti_sine as T
def recs(d,start=T.STIM_START_S):
    M=json.load(open(f"meta_{d}.json")); I=json.load(open(f"info_{d}.json")); Z=np.load(f"cache_{d}.npz")
    out=[]
    for x in M:
        st=Z[x['path'].replace('/','|')]; rate=I[x['path']]['rate']; on=int(round(start*rate))
        r=dict(path=x['path'],url=x['url'],session=x['name'],description=x['desc'],rate=rate,start=I[x['path']]['start'],n_frames=st.shape[0],onset=on,shape=st.shape,first_frame_ratio=float(st[0].mean()/st[1:on].mean()))
        r.update(T._reduce(st,on)); out.append(r)
    return out
if __name__=="__main__":
    R={}
    for d in ["001032","001033","001035","001271","001272"]: R[d]=recs(d)
    R["001030"]=recs("001030",0.025)
    pickle.dump(R,open("recs.pkl","wb"))
EOF
time python dev.py
```

```
real	0m3.723s
user	0m4.211s
sys	0m0.131s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && cat > cells_core.py <<'EOF'
import pandas as pd, numpy as np, re
from scipy import stats
READINGS=[(roi,rd) for roi in T.ROIS for rd in T.AP_READINGS]
def rkey(roi,rd): return f"{roi}/{rd}"
def session_table(recs, dandiset, dur_s=T.STIM_DUR_S, invert=False, extra_levels=()):
    rows=[]
    for r in recs:
        p=parse=T.parse_fast(r["description"], r["session"])
        sub=r["path"].split("/")[0]
        neuron=re.match(r"sub-(c\d+)",sub).group(1) if dandiset=="001030" else sub
        row=dict(dandiset=dandiset,neuron=f"{dandiset}/{neuron}",path=r["path"],start=r["start"],
                 carrier=p["carrier"],modulated=p["modulated"],voltage=p["voltage"],ttx=p["tetrodotoxin"],sham=p["sham"],
                 rate=r["rate"],onset=r["onset"],n_frames=r["n_frames"],first_frame_ratio=r["first_frame_ratio"])
        for roi in T.ROIS:
            dF=r[roi]
            row[f"pre_sd/{roi}"]=float(dF[1:r["onset"]].std())
            for rd in T.AP_READINGS:
                row[f"aps/{roi}/{rd}"]=T.aps_in_window(dF,r["rate"],r["onset"],dur_s,rd,invert=invert)
                # peaks before the stimulus, same length window, for the clock check
                pre=T.detect_aps(dF,r["rate"],rd,invert=invert); row[f"pre_aps/{roi}/{rd}"]=int(((pre>=1)&(pre<r["onset"])).sum())
            for lvl_name,lvl in extra_levels:
                L=lvl*row[f"pre_sd/{roi}"]
                for rd in T.AP_READINGS:
                    row[f"aps/{roi}/{rd}{lvl_name}"]=T.aps_in_window(dF,r["rate"],r["onset"],dur_s,rd,level=L,invert=invert)
            row[f"last100/{roi}"]=T.window_mean(dF,r["rate"],r["onset"],dur_s-0.1,dur_s,invert)
            row[f"half2/{roi}"]=T.window_mean(dF,r["rate"],r["onset"],dur_s/2,dur_s,invert)
        rows.append(row)
    df=pd.DataFrame(rows)
    for c in [c for c in df.columns if c.startswith("aps/")]:
        df["n"+c]=df[c].apply(len)
    return df.sort_values(["neuron","start"]).reset_index(drop=True)
EOF
cat > run_dev.py <<'EOF'
import pickle,sys
sys.path.insert(0,"entries/001274-semenov-2025")
import ti_sine as T
R=pickle.load(open("recs.pkl","rb"))
for f in sys.argv[1:]: exec(open(f).read())
EOF
cat > c1.py <<'EOF'
fast=pd.concat([session_table(R[d],d) for d in ["001032","001033","001035"]],ignore_index=True)
print(fast.shape); print(fast.groupby(["dandiset","carrier","modulated"]).size())
print(fast[[c for c in fast.columns if c.startswith("pre_aps")]].sum())
print("first frame ratio",fast.first_frame_ratio.describe())
pickle.dump(fast,open("fast.pkl","wb"))
EOF
time python run_dev.py cells_core.py c1.py
```

```
(625, 31)
dandiset  carrier  modulated
001032    20       False        25
          20k      False        33
          2k       False        80
                   True         40
001033    100      False         1
          1280     False         1
          160      False         1
          20       False        33
          20k      False        47
                   True         13
          2k       False        56
                   True         31
          320      False         1
          40k      False         3
          50       False         4
          500      False         1
          640      False         1
001035    100k     False         2
[... 32 more lines not kept]
```

**Agent**

Reading (b) on the bright-pixel ROI finds many "APs" before the stimulus (183 in 625 pre-stimulus windows), so it is noisy. Compare AP amplitudes of the two ROIs with the paper's typical 11.3%.

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && cat > c2.py <<'EOF'
fast=pickle.load(open("fast.pkl","rb"))
rec={r["path"]:r for d in ["001032","001033","001035"] for r in R[d]}
for roi in T.ROIS:
    h=[];sd=[]
    for _,s in fast.iterrows():
        r=rec[s.path]; sd.append(s[f"pre_sd/{roi}"])
        for t in s[f"aps/{roi}/a"][:1]:
            i=int(round(t*s.rate))+s.onset; h.append(r[roi][i])
    print(roi,"first-AP peak dF median %.1f IQR %.1f-%.1f n=%d; pre-stim SD median %.2f"%(np.median(h),*np.percentile(h,[25,75]),len(h),np.median(sd)))
for k in [c for c in fast.columns if c.startswith("pre_aps")]:
    print(k, fast[k].sum(), "events in", len(fast), "pre-stimulus windows of 49 ms; per 250 ms: %.2f"%(fast[k].sum()/len(fast)*250/49))
EOF
python run_dev.py cells_core.py c2.py
```

```
whole first-AP peak dF median 11.4 IQR 9.6-13.6 n=473; pre-stim SD median 0.83
bright first-AP peak dF median 11.2 IQR 9.6-13.3 n=473; pre-stim SD median 1.03
pre_aps/whole/a 0 events in 625 pre-stimulus windows of 49 ms; per 250 ms: 0.00
pre_aps/whole/b 24 events in 625 pre-stimulus windows of 49 ms; per 250 ms: 0.20
pre_aps/bright/a 0 events in 625 pre-stimulus windows of 49 ms; per 250 ms: 0.00
pre_aps/bright/b 183 events in 625 pre-stimulus windows of 49 ms; per 250 ms: 1.49
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . work/bin/activate && cat > c3.py <<'EOF'
fast=pickle.load(open("fast.pkl","rb"))
OUT_READ=[("whole","a"),("whole","b")]; VAR_READ=[("bright","a"),("bright","b")]
unmod=fast[(fast.carrier.isin(["2k","20k"]))&(~fast.modulated)].copy()
unmod["field"]=T.field(unmod.voltage,"half")
# --- fig1-pure-sine-excites-all
def excited(df,roi,rd):
    g=df.groupby(["carrier","neuron"])[f"naps/{roi}/{rd}"].max()>0
    return g.groupby(level=0).agg(["sum","count"])
for roi,rd in OUT_READ+VAR_READ:
    e=excited(unmod,roi,rd); print("excited",roi,rd,{c:f"{int(e.loc[c,'sum'])}/{int(e.loc[c,'count'])} = {100*e.loc[c,'sum']/e.loc[c,'count']:.0f}%" for c in e.index})
# --- per neuron x carrier: by field
def per_field(df,roi,rd):
    # sessions at the same field: mean count, first-AP latency mean over sessions with APs, mean last100
    d=df.assign(n=df[f"naps/{roi}/{rd}"],lat=df[f"aps/{roi}/{rd}"].apply(lambda a: a[0] if len(a) else np.nan),
                rate=df[f"aps/{roi}/{rd}"].apply(lambda a: 1/(a[1]-a[0]) if len(a)>1 else np.nan),last=df[f"last100/{roi}"],half2=df[f"half2/{roi}"])
    return d.groupby(["neuron","carrier","field"]).agg(n=("n","mean"),nmin=("n","min"),lat=("lat","mean"),rate=("rate","max"),last=("last","mean"),half2=("half2","mean"),k=("n","size")).reset_index()
for roi,rd in OUT_READ+VAR_READ:
    pf=per_field(unmod,roi,rd)
    nt=pf[pf.n>0].sort_values("field").groupby(["neuron","carrier"]).first()
    lat=nt.lat*1000
    rho=[];ok=[]
    for (nr,c),g in pf[pf.n>0].groupby(["neuron","carrier"]):
        if len(g)>=3:
            r=stats.spearmanr(g.field,g.lat).statistic; rho.append(r)
    rho=np.array(rho)
    print(f"onset {roi}/{rd}: near-threshold first-AP latency median {np.median(lat):.0f} ms (IQR {np.percentile(lat,25):.0f}-{np.percentile(lat,75):.0f}, n={len(lat)}); by carrier",lat.groupby(level=1).median().round(0).to_dict(),
          f"; Spearman<0 in {np.sum(rho<0)}/{len(rho)}")
    ceil=pf.groupby("neuron").rate.max().dropna()
    print(f"  ceiling median {np.median(ceil):.1f} Hz IQR {np.percentile(ceil,25):.0f}-{np.percentile(ceil,75):.0f} n={len(ceil)}")
    hi=pf.sort_values("field").groupby(["neuron","carrier"]).last()
    j=hi.join(nt[["last","field"]],rsuffix="_nt")
    blk=(j["last"]>5)&(j["last"]>j["last_nt"])
    blk2=(j["half2"]>5)
    print(f"  block: {blk.sum()}/{len(j)} pairs; highest-field last100 median {j['last'].median():.1f}%")
EOF
python run_dev.py cells_core.py c3.py
```

```
Sun Nov  1 15:41:28 UTC 2026
<string>:31: Pandas4Warning: The 'lsuffix' and 'rsuffix' keywords in DataFrame.join are deprecated and will be removed in a future version. Use the 'suffixes' keyword instead.
<string>:31: Pandas4Warning: The 'lsuffix' and 'rsuffix' keywords in DataFrame.join are deprecated and will be removed in a future version. Use the 'suffixes' keyword instead.
<string>:31: Pandas4Warning: The 'lsuffix' and 'rsuffix' keywords in DataFrame.join are deprecated and will be removed in a future version. Use the 'suffixes' keyword instead.
<string>:31: Pandas4Warning: The 'lsuffix' and 'rsuffix' keywords in DataFrame.join are deprecated and will be removed in a future version. Use the 'suffixes' keyword instead.
excited whole a {'20k': '15/17 = 88%', '2k': '27/28 = 96%'}
excited whole b {'20k': '15/17 = 88%', '2k': '27/28 = 96%'}
excited bright a {'20k': '15/17 = 88%', '2k': '27/28 = 96%'}
excited bright b {'20k': '15/17 = 88%', '2k': '28/28 = 100%'}
onset whole/a: near-threshold first-AP latency median 64 ms (IQR 41-128, n=42); by carrier {'20k': 124.0, '2k': 54.0} ; Spearman<0 in 38/38
  ceiling median 61.1 Hz IQR 36-173 n=30
  block: 3/45 pairs; highest-field last100 median 0.9%
onset whole/b: near-threshold first-AP latency median 67 ms (IQR 42-123, n=42); by carrier {'20k': 101.0, '2k': 56.0} ; Spearman<0 in 39/39
  ceiling median 42.9 Hz IQR 29-82 n=31
  block: 3/45 pairs; highest-field last100 median 0.9%
onset bright/a: near-threshold first-AP latency median 67 ms (IQR 41-128, n=42); by carrier {'20k': 124.0, '2k': 54.0} ; Spearman<0 in 38/38
  ceiling median 87.0 Hz IQR 36-193 n=30
  block: 3/45 pairs; highest-field last100 median 0.7%
onset bright/b: near-threshold first-AP latency median 54 ms (IQR 17-120, n=43); by carrier {'20k': 43.0, '2k': 57.0} ; Spearman<0 in 40/41
  ceiling median 85.7 Hz IQR 46-114 n=31
[... 2 more lines not kept]
```

**Agent**

Most neurons are excited and latency falls with field in every neuron. Some ceilings above 150 Hz look like double detections; inspecting those traces.

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && cat > c4.py <<'EOF'
fast=pickle.load(open("fast.pkl","rb"))
rec={r["path"]:r for d in ["001032","001033","001035"] for r in R[d]}
unmod=fast[(fast.carrier.isin(["2k","20k"]))&(~fast.modulated)].copy()
unmod["r"]=unmod["aps/whole/a"].apply(lambda a: 1/(a[1]-a[0]) if len(a)>1 else np.nan)
hi=unmod[unmod.r>120]
print(len(hi), "sessions with first-two-AP rate >120 Hz of", unmod.r.notna().sum())
np.set_printoptions(precision=1,suppress=True,linewidth=220)
for _,s in hi.head(4).iterrows():
    r=rec[s.path]; a=s["aps/whole/a"]; i0=s.onset+int(a[0]*s.rate)
    print(s.neuron,s.carrier,s.voltage,len(a),np.round(a[:6]*1000,1)); print(r["whole"][i0-10:i0+45])
nex=unmod.groupby(["carrier","neuron"])["naps/whole/a"].max()
print(nex[nex==0]); print(unmod[unmod.neuron.isin([n for c,n in nex[nex==0].index])][["neuron","carrier","voltage"]].groupby(["neuron","carrier"]).voltage.agg(["min","max","count"]))
EOF
python run_dev.py cells_core.py c4.py
```

```
16 sessions with first-two-AP rate >120 Hz of 249
001032/sub-11-1 20k 15.0 5 [ 10.7  17.5  80.  142.6 203.1]
[ 1.1  0.1  1.4 -0.3  0.8  1.1  1.   6.   9.6 10.4 10.8 10.7  8.7  6.4  8.3  9.   6.9  6.1  7.2  5.   5.7  5.9  5.   5.5  5.9  4.2  4.6  4.1  4.8  3.7  3.3  5.8  3.7  4.2  3.1  2.8  3.1  3.7  1.7  3.1  2.3  1.7  1.
  0.5  1.1  0.3 -1.1 -0.9  0.6  0.8 -0.2  0.9 -0.4 -0.8  0.6]
001032/sub-11-1 20k 16.0 6 [  8.7  15.6  69.7 123.1 175.  224.9]
[ 1.4  0.4  1.1  1.7  0.2  0.9  1.5  5.7  8.2  9.8 10.7  9.3  8.7  9.9  9.3  8.3  7.2  7.3  6.5  6.5  6.5  5.8  6.5  5.6  6.   4.8  4.9  4.2  4.8  4.5  3.7  6.5  3.   4.7  4.1  3.8  3.1  1.5  3.3  2.5  2.3  1.6  1.8
  2.   1.2  1.2  0.6  1.1  1.3 -0.3 -1.3 -0.4  1.6 -0.9  0.8]
001032/sub-12-1 2k 15.0 37 [ 1.9 10.  15.6 22.  27.5 33. ]
[-1.1 -0.5  0.5 -0.4  0.4  1.6  1.1  8.6 10.1 14.1 15.5 10.3  8.9  8.9  3.   5.8  3.7  1.6  5.8  2.1  0.9  5.2  2.   4.2  7.   2.   3.9  5.8  2.   4.6  6.1  2.   4.8  5.2  1.8  6.8  3.8  2.8  7.8  2.6  4.   6.4  2.
  5.7  7.   2.7  5.9  7.2  1.9  6.4  5.4  2.3  9.   3.9  2.2]
001032/sub-2-1 2k 9.0 7 [ 20.7  26.2  84.2 131.9 195.4 223.9]
[ 3.   0.8  0.3  0.3  0.1  2.   0.9  2.8  6.4 12.2 12.3 11.4 10.  10.   9.   6.9  8.1  6.4  5.1  6.4  6.1  5.7  7.   4.5  3.7  5.1  2.4  5.5  3.3  2.3  3.3  2.2  2.5  2.1  2.9  2.7  1.7  0.7  1.4  3.5  1.9  1.1  2.5
  0.7  2.4  1.6  1.   1.5  2.1  0.6  1.8  0.3  0.   0.9  0.9]
carrier  neuron         
20k      001033/sub-7-2     0
         001035/sub-10-4    0
2k       001032/sub-13-1    0
Name: naps/whole/a, dtype: int64
                          min   max  count
neuron          carrier                   
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001274-semenov-2025 && python - <<'EOF'
p="ti_sine.py"; s=open(p).read()
s=s.replace("""  (a) a peak of dF above 5%; (b) a rise of at least 5% dF within 5 ms. Peaks closer than 5 ms
  are merged in both (a standard choice; APs last about 8 ms, Methods), and in (a) a peak must
  stand 2.5% above its surroundings (scipy prominence; a standard choice, half the 5% level, to
  keep noise on a depolarized plateau from counting as APs; pre-stimulus SD is about 1%).""",
"""  (a) a peak of dF above 5%; (b) a rise of at least 5% dF within 5 ms. In both, peaks closer
  than 8 ms are merged into one AP, as an AP lasts 8 ms (Methods: "typical values: 11.3% +-
  0.9% dF and 8 +- 0.7 ms duration"); this caps the rate the detection can see at 125 Hz, above
  the 60 to 90 Hz the paper reports. In (a) a peak must stand 2.5% above its surroundings
  (scipy prominence; a standard choice, half the 5% level, to keep noise on a depolarized
  plateau from counting as APs; the pre-stimulus SD is about 1%).""")
s=s.replace("AP_WIDTH_S = 0.005            # 5 ms: rise window of reading (b) and the merge distance",
"AP_WIDTH_S = 0.005            # 5 ms: rise window of reading (b), claims file\nAP_MERGE_S = 0.008            # 8 ms: AP duration, Methods")
s=s.replace("""    w = int(round(AP_WIDTH_S * rate))
    if reading == "a":
        p, _ = find_peaks(x, height=level, distance=w, prominence=PROMINENCE)
    else:
        p, _ = find_peaks(x, distance=w)""","""    w = int(round(AP_WIDTH_S * rate))
    dist = int(round(AP_MERGE_S * rate))
    if reading == "a":
        p, _ = find_peaks(x, height=level, distance=dist, prominence=PROMINENCE)
    else:
        p, _ = find_peaks(x, distance=dist)""")
open(p,"w").write(s)
EOF
cd $TMPDIR && . work/bin/activate && python run_dev.py cells_core.py c1.py >/dev/null && python run_dev.py cells_core.py c2.py c3.py c4.py 2>&1 | grep -v Warn
```

```
whole first-AP peak dF median 11.4 IQR 9.7-13.6 n=473; pre-stim SD median 0.83
bright first-AP peak dF median 11.2 IQR 9.6-13.3 n=473; pre-stim SD median 1.03
pre_aps/whole/a 0 events in 625 pre-stimulus windows of 49 ms; per 250 ms: 0.00
pre_aps/whole/b 19 events in 625 pre-stimulus windows of 49 ms; per 250 ms: 0.16
pre_aps/bright/a 0 events in 625 pre-stimulus windows of 49 ms; per 250 ms: 0.00
pre_aps/bright/b 144 events in 625 pre-stimulus windows of 49 ms; per 250 ms: 1.18
excited whole a {'20k': '15/17 = 88%', '2k': '27/28 = 96%'}
excited whole b {'20k': '15/17 = 88%', '2k': '27/28 = 96%'}
excited bright a {'20k': '15/17 = 88%', '2k': '27/28 = 96%'}
excited bright b {'20k': '15/17 = 88%', '2k': '28/28 = 100%'}
onset whole/a: near-threshold first-AP latency median 64 ms (IQR 41-128, n=42); by carrier {'20k': 124.0, '2k': 54.0} ; Spearman<0 in 38/38
  ceiling median 59.9 Hz IQR 32-83 n=30
  block: 3/45 pairs; highest-field last100 median 0.9%
onset whole/b: near-threshold first-AP latency median 67 ms (IQR 42-123, n=42); by carrier {'20k': 101.0, '2k': 54.0} ; Spearman<0 in 39/39
  ceiling median 42.9 Hz IQR 29-82 n=31
  block: 3/45 pairs; highest-field last100 median 0.9%
onset bright/a: near-threshold first-AP latency median 67 ms (IQR 41-128, n=42); by carrier {'20k': 124.0, '2k': 54.0} ; Spearman<0 in 38/38
  ceiling median 62.4 Hz IQR 32-86 n=30
  block: 3/45 pairs; highest-field last100 median 0.7%
onset bright/b: near-threshold first-AP latency median 54 ms (IQR 20-120, n=43); by carrier {'20k': 43.0, '2k': 56.0} ; Spearman<0 in 38/40
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && cat > c5.py <<'EOF'
fast=pickle.load(open("fast.pkl","rb"))
st=fast[fast.carrier.isin(["2k","20k"])].copy()
st["stim"]=st.carrier+np.where(st.modulated,"/mod","/unmod")
def thresholds(df,roi,rd,freading="half"):
    d=df.assign(field=T.field(df.voltage,freading),n=df[f"naps/{roi}/{rd}"])
    rows=[]
    for (nr,s),g in d.groupby(["neuron","stim"]):
        for k in (1,5):
            ok=g[g.n>=k]
            rows.append(dict(neuron=nr,stim=s,aps=k,thr=ok.field.min() if len(ok) else np.nan,
                             bracketed=bool(len(ok) and (g.field<ok.field.min()).any())))
    return pd.DataFrame(rows)
for roi,rd in [("whole","a"),("whole","b"),("bright","a"),("bright","b")]:
    th=thresholds(st,roi,rd)
    print(f"== {roi}/{rd}")
    tab=th.groupby(["aps","stim"]).thr.agg(["mean","sem","count"]).round(1); print(tab.unstack(0).to_string())
    for k in (1,5):
        for m in ("unmod","mod"):
            a=th[(th.aps==k)&(th.stim==f"2k/{m}")].thr.dropna(); b=th[(th.aps==k)&(th.stim==f"20k/{m}")].thr.dropna()
            print(f"  {k}AP {m}: ratio {b.mean()/a.mean():.2f} t-test p={stats.ttest_ind(b,a).pvalue:.2g} (n {len(a)},{len(b)})")
    a=th[th.stim.str.startswith("2k/")].thr.dropna(); b=th[th.stim.str.startswith("20k/")].thr.dropna()
    print(f"  pooled ratio {b.mean()/a.mean():.2f} p={stats.ttest_ind(b,a).pvalue:.2g}")
    for c,k in [("2k",5),("20k",1),("20k",5),("2k",1)]:
        u=th[(th.aps==k)&(th.stim==f"{c}/unmod")].set_index("neuron").thr; m_=th[(th.aps==k)&(th.stim==f"{c}/mod")].set_index("neuron").thr
        u2,m2=u.dropna(),m_.dropna(); both=pd.concat([u,m_],axis=1).dropna()
        print(f"  mod vs unmod {c} {k}AP: {m2.mean():.1f} vs {u2.mean():.1f} p={stats.ttest_ind(m2,u2).pvalue:.3g} (n {len(m2)},{len(u2)}); paired n={len(both)} p={stats.ttest_rel(both.iloc[:,1],both.iloc[:,0]).pvalue if len(both)>1 else np.nan:.3g}")
    u=th[(th.aps==1)&(th.stim=="2k/unmod")].thr.dropna()
    print(f"  2k unmod 1AP threshold half {u.mean():.1f} +- {u.sem():.1f} (n={len(u)}), full {2*u.mean():.1f}; bracketed only: {th[(th.aps==1)&(th.stim=='2k/unmod')&th.bracketed].thr.mean():.1f} n={int(th[(th.aps==1)&(th.stim=='2k/unmod')].bracketed.sum())}")
EOF
python run_dev.py cells_core.py c5.py 2>&1 | grep -v Warn
```

```
== whole/a
            mean          sem       count    
aps            1      5     1     5     1   5
stim                                         
20k/mod    252.0  272.4  37.5  47.2     3   3
20k/unmod  171.5  211.1  12.1  12.1    15  14
2k/mod      96.2  109.2   8.2   8.4    13  12
2k/unmod    75.6   90.1   6.2   6.1    27  27
  1AP unmod: ratio 2.27 t-test p=1.4e-09 (n 27,15)
  1AP mod: ratio 2.62 t-test p=1.1e-05 (n 13,3)
  5AP unmod: ratio 2.34 t-test p=2.4e-12 (n 27,14)
  5AP mod: ratio 2.49 t-test p=4.1e-05 (n 12,3)
  pooled ratio 2.28 p=1e-24
  mod vs unmod 2k 5AP: 109.2 vs 90.1 p=0.0817 (n 12,27); paired n=11 p=0.0952
  mod vs unmod 20k 1AP: 252.0 vs 171.5 p=0.0205 (n 3,15); paired n=3 p=0.121
  mod vs unmod 20k 5AP: 272.4 vs 211.1 p=0.0816 (n 3,14); paired n=3 p=0.267
  mod vs unmod 2k 1AP: 96.2 vs 75.6 p=0.0595 (n 13,27); paired n=12 p=0.000116
  2k unmod 1AP threshold half 75.6 +- 6.2 (n=27), full 151.2; bracketed only: 88.0 n=16
== whole/b
            mean          sem       count    
[... 53 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . work/bin/activate && cat > c6.py <<'EOF'
fast=pickle.load(open("fast.pkl","rb"))
mod=fast[fast.carrier.isin(["2k","20k"])&fast.modulated]
for roi,rd in [("whole","a"),("whole","b"),("bright","a"),("bright","b")]:
    n=mod[f"naps/{roi}/{rd}"]
    allt=np.concatenate(mod[f"aps/{roi}/{rd}"].values)
    ph=(allt*1000)%50
    sel=mod[n>=5]
    frac=[np.mean(((a*1000)%50>=12.5)&((a*1000)%50<=37.5)) for a in sel[f"aps/{roi}/{rd}"]]
    pooled=np.concatenate(sel[f"aps/{roi}/{rd}"].values); pf=np.mean(((pooled*1000)%50>=12.5)&((pooled*1000)%50<=37.5))
    blk=(mod[f"last100/{roi}"]>5).sum()
    hist=np.histogram(ph,bins=10,range=(0,50))[0]
    print(f"{roi}/{rd}: sessions {len(mod)}, max APs {n.max()}, >10: {(n>10).sum()}; sessions>=5 APs {len(sel)}, fraction of those with >=80% in window {np.mean(np.array(frac)>=0.8):.2f}, pooled {pf:.2f}; block {blk}; phase hist(5ms) {hist}")
# fig2c pairs
both=fast[fast.carrier.isin(["2k","20k"])]
for roi,rd in [("whole","a"),("whole","b"),("bright","a"),("bright","b")]:
    g=both.groupby(["neuron","carrier","voltage","modulated"])[f"naps/{roi}/{rd}"].mean().unstack("modulated").dropna()
    d=g[False]-g[True]
    print(f"{roi}/{rd}: pairs {len(g)} neurons {g.reset_index().neuron.nunique()}, unmod>mod {int((d>0).sum())}, mod>unmod {int((d<0).sum())}, tie {int((d==0).sum())}, mean diff {d.mean():.2f}, paired t p={stats.ttest_rel(g[False],g[True]).pvalue:.3g}")
EOF
python run_dev.py cells_core.py c6.py 2>&1 | grep -v Warn
```

```
Sun Nov  1 15:42:49 UTC 2026
whole/a: sessions 84, max APs 12, >10: 2; sessions>=5 APs 28, fraction of those with >=80% in window 0.82, pooled 0.87; block 1; phase hist(5ms) [ 6  3  4 18 50 76 79 17  8  3]
whole/b: sessions 84, max APs 6, >10: 0; sessions>=5 APs 22, fraction of those with >=80% in window 0.95, pooled 0.98; block 1; phase hist(5ms) [ 2  1  2 16 50 72 71 12  1  0]
bright/a: sessions 84, max APs 13, >10: 4; sessions>=5 APs 32, fraction of those with >=80% in window 0.72, pooled 0.83; block 1; phase hist(5ms) [ 8  1  6 21 48 76 82 23 17  4]
bright/b: sessions 84, max APs 11, >10: 1; sessions>=5 APs 32, fraction of those with >=80% in window 0.78, pooled 0.84; block 1; phase hist(5ms) [ 4  7 14 27 57 76 83 19  8  8]
whole/a: pairs 52 neurons 12, unmod>mod 46, mod>unmod 1, tie 5, mean diff 3.61, paired t p=3.3e-09
whole/b: pairs 52 neurons 12, unmod>mod 46, mod>unmod 1, tie 5, mean diff 3.70, paired t p=2.55e-09
bright/a: pairs 52 neurons 12, unmod>mod 43, mod>unmod 2, tie 7, mean diff 3.52, paired t p=7.89e-09
bright/b: pairs 52 neurons 12, unmod>mod 44, mod>unmod 2, tie 6, mean diff 4.02, paired t p=1.08e-09
Shell cwd was reset to
```

**Agent**

Beat locking is strong (APs concentrate 15 to 35 ms into each beat), and unmodulated waves give more APs in 46 of 52 pairs. Now Figure 3C (001030), S1 (001272) and S2 (001271).

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && cat > c7.py <<'EOF'
r30=R["001030"]
for r in sorted(r30,key=lambda r:r["path"]):
    dF=r["whole"]; on=r["onset"]
    a=T.aps_in_window(dF,r["rate"],on,2.0,"a"); b=T.aps_in_window(dF,r["rate"],on,2.0,"b")
    print(r["path"].split("/")[0], r["n_frames"], "%.0f"%r["rate"], len(a),len(b), "last250 APs a",np.sum(a>1.75),"after250 APs",np.sum(a>0.25), "mean dF 0.25-2s %.1f"%T.window_mean(dF,r["rate"],on,0.25,2.0), "end-of-rec dF %.1f"%dF[-300:].mean(), "pre sd %.2f"%dF[1:on].std())
EOF
python run_dev.py cells_core.py c7.py 2>&1 | grep -v Warn
```

```
sub-c5-1-0V 7000 3135 5 0 last250 APs a 0 after250 APs 2 mean dF 0.25-2s -1.3 end-of-rec dF -4.4 pre sd 1.15
sub-c5-1-5V 6000 3135 55 65 last250 APs a 1 after250 APs 48 mean dF 0.25-2s 1.0 end-of-rec dF -1.3 pre sd 1.18
sub-c5-2-0V 6000 3135 23 10 last250 APs a 0 after250 APs 12 mean dF 0.25-2s 0.6 end-of-rec dF -1.5 pre sd 1.08
sub-c6-1-0V 7000 3135 10 11 last250 APs a 1 after250 APs 9 mean dF 0.25-2s -3.0 end-of-rec dF -5.8 pre sd 1.22
sub-c6-1-25V 7000 3135 29 30 last250 APs a 2 after250 APs 26 mean dF 0.25-2s -1.3 end-of-rec dF -5.2 pre sd 1.18
sub-c6-1-45V 7000 3135 30 35 last250 APs a 0 after250 APs 26 mean dF 0.25-2s -0.2 end-of-rec dF -5.4 pre sd 1.19
sub-c7-1-0V 7000 3135 0 0 last250 APs a 0 after250 APs 0 mean dF 0.25-2s -3.0 end-of-rec dF -5.9 pre sd 1.12
sub-c7-1-25V 7000 3135 17 17 last250 APs a 2 after250 APs 16 mean dF 0.25-2s -1.9 end-of-rec dF -5.9 pre sd 1.10
sub-c7-1-45V 7000 3135 73 73 last250 APs a 8 after250 APs 69 mean dF 0.25-2s 0.4 end-of-rec dF -5.5 pre sd 1.14
sub-c7-1-7V 7000 3135 89 89 last250 APs a 10 after250 APs 83 mean dF 0.25-2s 2.2 end-of-rec dF -5.3 pre sd 1.08
sub-c7-2-0V 7000 3135 89 79 last250 APs a 8 after250 APs 81 mean dF 0.25-2s 3.1 end-of-rec dF -5.5 pre sd 1.17
sub-c7-2-3V 7000 3135 78 7 last250 APs a 0 after250 APs 68 mean dF 0.25-2s 3.7 end-of-rec dF -5.0 pre sd 1.11
sub-c8-1-0V 7000 3135 28 30 last250 APs a 2 after250 APs 25 mean dF 0.25-2s -2.6 end-of-rec dF -6.8 pre sd 1.12
sub-c8-1-25V 7000 3135 45 45 last250 APs a 5 after250 APs 41 mean dF 0.25-2s -0.1 end-of-rec dF -4.8 pre sd 1.11
sub-c8-1-5V 7000 3135 53 49 last250 APs a 4 after250 APs 47 mean dF 0.25-2s 1.0 end-of-rec dF -4.9 pre sd 1.07
sub-c8-1-75V 7000 3135 32 26 last250 APs a 0 after250 APs 26 mean dF 0.25-2s 0.9 end-of-rec dF -5.4 pre sd 0.96
sub-c8-2-0V 7000 3135 25 2 last250 APs a 0 after250 APs 16 mean dF 0.25-2s 0.6 end-of-rec dF -5.3 pre sd 1.05
Shell cwd was reset to
```

**Agent**

Traces of 001030 bleach by about 5% over 2 s; only neuron c7 has a trace without APs (1.0 V), which the Methods' correction needs. Compute the Figure 3C test with that correction, then S1 and S2.

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && cat > c8.py <<'EOF'
r30={r["path"].split("/")[0]:r for r in R["001030"]}
ref=r30["sub-c7-1-0V"]["whole"]
for k in sorted(r30):
    r=r30[k]; n=min(len(ref),len(r["whole"])); dF=r["whole"][:n]-ref[:n]; on=r["onset"]; rate=r["rate"]
    out=[]
    for rd in "ab":
        a=T.aps_in_window(dF,rate,on,2.0,rd)
        out.append(f"{rd}: n={len(a)} after250={np.sum(a>0.25)} last250={np.sum(a>1.75)}")
    rest=T.window_mean(dF,rate,on,0.25,min(2.0,(n-on)/rate))
    print(k, "; ".join(out), "mean dF 0.25-2 s %.1f"%rest, "frames",n)
EOF
python run_dev.py cells_core.py c8.py 2>&1 | grep -v Warn
```

```
sub-c5-1-0V a: n=22 after250=17 last250=0; b: n=3 after250=2 last250=0 mean dF 0.25-2 s 1.7 frames 7000
sub-c5-1-5V a: n=82 after250=75 last250=6; b: n=65 after250=58 last250=5 mean dF 0.25-2 s 3.8 frames 6000
sub-c5-2-0V a: n=106 after250=95 last250=5; b: n=19 after250=9 last250=0 mean dF 0.25-2 s 3.5 frames 6000
sub-c6-1-0V a: n=11 after250=10 last250=2; b: n=13 after250=12 last250=3 mean dF 0.25-2 s 0.0 frames 7000
sub-c6-1-25V a: n=41 after250=38 last250=5; b: n=33 after250=29 last250=4 mean dF 0.25-2 s 1.7 frames 7000
sub-c6-1-45V a: n=72 after250=65 last250=7; b: n=41 after250=35 last250=5 mean dF 0.25-2 s 2.8 frames 7000
sub-c7-1-0V a: n=0 after250=0 last250=0; b: n=0 after250=0 last250=0 mean dF 0.25-2 s 0.0 frames 7000
sub-c7-1-25V a: n=17 after250=16 last250=2; b: n=19 after250=18 last250=2 mean dF 0.25-2 s 1.1 frames 7000
sub-c7-1-45V a: n=73 after250=69 last250=8; b: n=75 after250=69 last250=8 mean dF 0.25-2 s 3.3 frames 7000
sub-c7-1-7V a: n=100 after250=94 last250=12; b: n=90 after250=83 last250=10 mean dF 0.25-2 s 5.2 frames 7000
sub-c7-2-0V a: n=116 after250=108 last250=15; b: n=80 after250=72 last250=10 mean dF 0.25-2 s 6.1 frames 7000
sub-c7-2-3V a: n=142 after250=131 last250=19; b: n=8 after250=1 last250=0 mean dF 0.25-2 s 6.7 frames 7000
sub-c8-1-0V a: n=30 after250=27 last250=4; b: n=39 after250=35 last250=5 mean dF 0.25-2 s 0.4 frames 7000
sub-c8-1-25V a: n=57 after250=53 last250=9; b: n=52 after250=48 last250=6 mean dF 0.25-2 s 2.9 frames 7000
sub-c8-1-5V a: n=84 after250=78 last250=10; b: n=50 after250=45 last250=6 mean dF 0.25-2 s 4.0 frames 7000
sub-c8-1-75V a: n=101 after250=92 last250=12; b: n=43 after250=38 last250=3 mean dF 0.25-2 s 3.9 frames 7000
sub-c8-2-0V a: n=159 after250=146 last250=20; b: n=33 after250=29 last250=5 mean dF 0.25-2 s 3.6 frames 7000
Shell cwd was reset to
```

**Agent**

On 001030, reading (a) counts plateau oscillations as APs at high fields (131 after 250 ms in c7 at 2.3 V) while reading (b) finds 1. Now S2 (tetrodotoxin) and S1 (Di-8-ANEPPS).

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && cat > c9.py <<'EOF'
t71=session_table(R["001271"],"001271")
for nr,g in t71.groupby("neuron"):
    if not g.ttx.any(): continue
    print("==",nr)
    for _,s in g.iterrows(): print("  ",s.start[11:19],"TTX" if s.ttx else "veh","sham" if s.sham else "", s.voltage, "APs a/b",s["naps/whole/a"],s["naps/whole/b"],"last100 %.1f"%s["last100/whole"])
pickle.dump(t71,open("t71.pkl","wb"))
t72=session_table(R["001272"],"001272",invert=True,extra_levels=(("5sd",5.0),))
print(t72.groupby("neuron").size())
for _,s in t72.iterrows(): print(s.neuron[-14:],s.start[11:19],s.voltage,"APs a/b",s["naps/whole/a"],s["naps/whole/b"],"5sd",s["naps/whole/a5sd"],s["naps/whole/b5sd"],"pre_sd %.2f"%s["pre_sd/whole"],"last100 %.1f"%s["last100/whole"])
pickle.dump(t72,open("t72.pkl","wb"))
EOF
python run_dev.py cells_core.py c9.py 2>&1 | grep -v Warn
```

```
== 001271/sub-10-20240731
   19:31:11 veh  4.0 APs a/b 1 1 last100 1.6
   19:31:51 veh  3.0 APs a/b 4 4 last100 0.5
   19:32:34 veh  3.5 APs a/b 8 7 last100 1.4
   19:33:00 veh  4.0 APs a/b 7 1 last100 2.1
   19:33:40 veh  4.5 APs a/b 2 1 last100 2.3
   19:38:56 veh  3.0 APs a/b 3 3 last100 0.0
   19:39:24 veh  3.5 APs a/b 7 7 last100 1.1
   19:39:51 veh  4.0 APs a/b 9 2 last100 2.2
   19:40:19 veh  4.5 APs a/b 8 1 last100 2.7
   19:50:16 TTX  3.0 APs a/b 0 0 last100 -0.7
   19:50:39 TTX  3.5 APs a/b 0 0 last100 -0.6
   19:50:57 TTX  4.0 APs a/b 0 0 last100 -0.5
   19:51:18 TTX  4.5 APs a/b 0 0 last100 -0.8
   19:51:39 TTX  6.0 APs a/b 0 0 last100 -0.6
   19:52:02 TTX  8.0 APs a/b 0 0 last100 -0.8
   19:52:23 TTX  10.0 APs a/b 0 0 last100 -0.7
   19:52:50 TTX  12.0 APs a/b 0 0 last100 0.4
   19:52:57 TTX  12.0 APs a/b 0 0 last100 -1.5
   19:53:07 TTX  12.0 APs a/b 0 5 last100 0.3
[... 173 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . work/bin/activate && python - <<'EOF'
import json,time,h5py,remfile,numpy as np
rows=json.load(open("rows_001274.json")); M={x['path']:x for x in json.load(open("meta_001274.json"))}
r=[r for r in rows if r['kind']=='sp100'][0]; p=[r for r in rows if r['kind']=='pulse'][0]
for x in (p,r):
    t=time.time()
    with h5py.File(remfile.File(M[x['path']]['url']),'r') as f: a=f['acquisition/StrobeImaging/data'][:]
    print(x['path'],a.shape,x['size']/1e6,"MB",time.time()-t,"s")
EOF
```

```
Sun Nov  1 15:44:03 UTC 2026
sub-1-20240522/sub-1-20240522_obj-sx69sf_image.nwb (140, 512, 512) 47.598226 MB 3.950371742248535 s
sub-2-20240522/sub-2-20240522_obj-19keurh_image.nwb (500, 512, 512) 171.804571 MB 8.79849624633789 s
Shell cwd was reset to
```

**Agent**

Strobe files stream at about 20 MB/s each, so a rebuilt-ROI variant on the candidate cells is affordable. Writing the notebook now (fast-imaging claims first).

**Agent calls Bash**

```bash
cat claims/001274/*.yaml | grep -n "^- id:" ; ls tools/; grep -n "tag\|sanity\|claim:" tools/entry.py | head -40
```

```
83:- id: fig1-pure-sine-excites-all
104:- id: fig1-onset-delay
122:- id: fig1-max-rate-ceiling
138:- id: fig1-excitation-block
154:- id: fig2d-20khz-twofold-threshold
184:- id: fig2d-modulated-thresholds-higher
213:- id: threshold-2khz-unmodulated
230:- id: fig2-modulated-locks-to-beats
247:- id: fig2c-pure-more-aps
259:- id: fig3b-low-conductivity-halves-threshold
278:- id: fig3c-sustained-firing-2s
296:- id: figs1-di8-anepps-control
314:- id: figs2-ttx-blocks-depolarization
327:- id: fig4-orientation-time-constants
366:- id: fig4-no-pole-difference
383:- id: fig4-discharging-slower
404:- id: fig4-pooled-time-constants
440:- id: fig5-carrier-antiphasic
457:- id: fig5-whole-cell-depolarization
471:- id: fig5-sine-asymmetry-c7
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 150,330p tools/entry.py
```

```
report.error(rel / "entry.yaml", f"name {entry.get('name')!r} must match the directory name")

    listed = [n["path"] for n in entry.get("notebooks", [])]
    present = sorted(p.name for p in entry_dir.glob("*.ipynb"))
    for name in sorted(set(present) - set(listed)):
        report.error(rel / name, "notebook is not listed in entry.yaml")
    for name in sorted(set(listed) - set(present)):
        report.error(rel / "entry.yaml", f"listed notebook {name!r} does not exist")
    helpers = entry.get("helpers", [])
    for name in helpers:
        if not (entry_dir / name).is_file():
            report.error(rel / "entry.yaml", f"listed helper {name!r} does not exist")

    requirements, lock = entry_dir / "requirements.in", entry_dir / "requirements.lock.txt"
    if not requirements.is_file():
        report.error(rel, "no requirements.in")
    elif not lock.is_file():
        report.error(rel, "no requirements.lock.txt; run `tools/entry.py lock`")
    else:
        pinned = {re.split(r"[=<>!~\[ ]", line, maxsplit=1)[0].lower().replace("_", "-")
[... 160 more lines not kept]
```

**Agent**

I'll move the session table and threshold measures into the helper so the notebook stays readable.

**Agent calls Bash**

```bash
cd entries/001274-semenov-2025 && cat >> ti_sine.py <<'EOF'


# --- session tables and per-neuron measures (fast recordings) ------------------------------

def neuron_of(dandiset, path):
    """Neuron of a fast recording. Subjects are neurons; DANDI:001030 makes one subject per
    session (`sub-c7-1-45V`), whose neuron is the `c7` part."""
    sub = path.split("/")[0]
    if dandiset == "001030":
        sub = re.match(r"sub-(c\d+)", sub).group(1)
    return f"{dandiset}/{sub}"


def session_table(recs, dandiset, dur_s=STIM_DUR_S, invert=False, sd_levels=(), traces=None):
    """One row per session: stimulus, AP times under each ROI and AP reading, and window means.

    `invert` flips traces whose dye loses emission on depolarization (Di-8-ANEPPS, Methods).
    `sd_levels` adds AP readings at a level of k pre-stimulus SDs (suffix `<k>sd`).
    `traces` replaces the stored traces by name (used for the bleaching correction of Figure 3C).
    """
    import pandas as pd
    rows = []
    for r in recs:
        p = parse_fast(r["description"], r["session"])
        row = dict(dandiset=dandiset, neuron=neuron_of(dandiset, r["path"]), path=r["path"],
                   start=r["start"], carrier=p["carrier"], modulated=p["modulated"],
                   voltage=p["voltage"], ttx=p["tetrodotoxin"], sham=p["sham"], rate=r["rate"],
                   onset=r["onset"], n_frames=r["n_frames"])
        for roi in ROIS:
            dF = r[roi] if traces is None else traces[r["path"]][roi]
            rate, on = r["rate"], r["onset"]
            sd = float(dF[1:on].std())
            row[f"pre_sd/{roi}"] = sd
            for rd in AP_READINGS:
                row[f"aps/{roi}/{rd}"] = aps_in_window(dF, rate, on, dur_s, rd, invert=invert)
                pre = detect_aps(dF, rate, rd, invert=invert)
                row[f"pre_aps/{roi}/{rd}"] = int(((pre >= 1) & (pre < on)).sum())
                for k in sd_levels:
                    row[f"aps/{roi}/{rd}{k:g}sd"] = aps_in_window(dF, rate, on, dur_s, rd,
                                                                  level=k * sd, invert=invert)
            end = min(dur_s, (len(dF) - on) / rate)
            row[f"last100/{roi}"] = window_mean(dF, rate, on, end - 0.1, end, invert)
            row[f"half2/{roi}"] = window_mean(dF, rate, on, end / 2, end, invert)
        rows.append(row)
    df = pd.DataFrame(rows)
    for c in [c for c in df.columns if c.startswith("aps/")]:
        df["n" + c] = df[c].apply(len)
    return df.sort_values(["neuron", "start"]).reset_index(drop=True)


def per_field(df, key, field_reading="half"):
    """Per neuron, carrier and field: mean AP count, first-AP latency (s, mean over sessions
    with APs), highest first-two-AP rate (Hz, Methods: "the inverse of the peak-to-peak time
    interval between the first two APs"), and mean dF of the last 100 ms and the second half.
    Sessions repeated at one field are averaged (a standard choice). `key` is `<roi>/<reading>`."""
    roi = key.split("/")[0]
    aps = df[f"aps/{key}"]
    d = df.assign(field=field(df.voltage, field_reading), n=df[f"naps/{key}"],
                  lat=aps.apply(lambda a: a[0] if len(a) else np.nan),
                  rate_hz=aps.apply(lambda a: 1 / (a[1] - a[0]) if len(a) > 1 else np.nan),
                  last=df[f"last100/{roi}"], half2=df[f"half2/{roi}"])
    return d.groupby(["neuron", "carrier", "field"]).agg(
        n=("n", "mean"), lat=("lat", "mean"), rate_hz=("rate_hz", "max"), last=("last", "mean"),
        half2=("half2", "mean"), sessions=("n", "size")).reset_index()


def thresholds(df, key, field_reading="half"):
    """Per neuron and stimulus, the lowest field of a session with at least 1 and at least 5
    APs during the 250-ms stimulus (Figure 2D legend). `bracketed` says whether a session at a
    lower field was recorded (it then had fewer APs)."""
    import pandas as pd
    d = df.assign(field=field(df.voltage, field_reading), n=df[f"naps/{key}"],
                  stim=df.carrier + np.where(df.modulated, "/mod", "/unmod"))
    rows = []
    for (nr, s), g in d.groupby(["neuron", "stim"]):
        for k in (1, 5):
            ok = g[g.n >= k]
            thr = ok.field.min() if len(ok) else np.nan
            rows.append(dict(neuron=nr, stim=s, aps=k, thr=thr,
                             bracketed=bool(len(ok) and (g.field < thr).any())))
    return pd.DataFrame(rows)
EOF
python -c "import ast;ast.parse(open('ti_sine.py').read())"
```

```
(Bash completed with no output)
```

**Agent**

Now the notebook builder. Loading cells produce `recs`, so I can test the analysis cells against my cached records before the full streamed run.

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build_nb.py",
 "content": "import nbformat as nbf, sys\ncells = []\ndef md(s): cells.append((\"markdown\", s.strip(\"\\n\"), []))\ndef code(s, *tags): cells.append((\"code\", s.strip(\"\\n\"), list(tags)))\n\nmd(r\"\"\"\n# Semenov, Kim, Silkuniene & Pakhomov (2025): sine waves and temporal interference stimulation\n\n**Paper.** Semenov I, Kim V, Silkuniene G, Pakhomov AG (2025). Excitation and polarization of isolated\nneurons by high-frequency sine waves for temporal interference stimulation. *Cell Reports Physical\nScience* 6, 102660. doi:10.1016/j.xcrp.2025.102660. The claims file was written from the NIH author\nmanuscript (PMC12320893) with its STAR Methods and supplement.\n\n**Dataset.** DANDI:001274, version 0.250805.1401 (the most recent published version). The paper names\nno version. The dandiset has two published versions, 0.250701.1622 and 0.250805.1401, with the same 232\nassets and the same number of bytes; the later one is pinned as the protocol asks (author, step 1.3), and\nthe notebook checks below that the asset lists are the same. DANDI:001274 holds the strobe images of\nFigures 5, 6 and S3. The claims file assigns the other figures to other dandisets of the paper, read at\ntheir most recent published versions, for the same reason: 001030 (0.240520.1924), 001032\n(0.240527.1432), 001033 (0.240527.1432), 001035 (0.240527.1432), 001271 (0.250805.1352), 001272\n(0.250805.1358) and 001273 (0.250805.1356). 001034 (0.240527.1431) is checked and found to be a second\ndeposit of 001032.\n\n**Claims** (claims/001274/10.1016-j.xcrp.2025.102660.yaml):\n\n| Claim | Data | Here |\n|---|---|---|\n| fig1-pure-sine-excites-all | 001032, 001033, 001035 | tested |\n| fig1-onset-delay | same | tested |\n| fig1-max-rate-ceiling | same | tested |\n| fig1-excitation-block | same | tested |\n| fig2d-20khz-twofold-threshold | same | tested |\n| fig2d-modulated-thresholds-higher | same | tested |\n| threshold-2khz-unmodulated | same | tested |\n| fig2-modulated-locks-to-beats | same | tested |\n| fig2c-pure-more-aps | same | tested |\n| fig3b-low-conductivity-halves-threshold | none labelled | blocked: no 250-ms session is labelled as sodium gluconate |\n| fig3c-sustained-firing-2s | 001030 | tested |\n| figs1-di8-anepps-control | 001272 | tested |\n| figs2-ttx-blocks-depolarization | 001271 | tested |\n| fig4-orientation-time-constants | 001273 | blocked: no ROIs, no cell shape or orientation groups |\n| fig4-no-pole-difference | 001273 | blocked: no ROIs |\n| fig4-discharging-slower | 001273 | blocked: no ROIs, no groups |\n| fig4-pooled-time-constants | 001273 | blocked: no ROIs |\n| fig5-carrier-antiphasic, fig5-whole-cell-depolarization, fig5-sine-asymmetry-c7, figs3-sine-asymmetry-c8, fig5fg-no-migration | 001274 | blocked: no ROIs, cells C7 and C8 cannot be identified |\n| fig6b-pulse-sensitivity, fig6c-sine-sensitivity, fig6d-sine-less-than-pulse | 001274 | blocked: no ROIs; rebuilt ROIs shown as a variant |\n| threshold-depolarization-estimate | 001274 and 001032 to 001035 | blocked: depends on fig6d |\n\nMethod details the claims file leaves open are taken from the paper and cited in `ti_sine.py`. Two\nchoices are assumptions, run under each reading: the soma ROI (the whole 16 x 16 frame, or its brighter\nhalf) and the field (36 V/cm times half the peak-to-peak voltage, or times the whole of it).\n\"\"\")\n\ncode(r\"\"\"\nimport json, re, time, collections\nimport numpy as np\nimport pandas as pd\nimport h5py, remfile\nimport matplotlib.pyplot as plt\nfrom scipy import stats\nimport ti_sine as T\n\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 200)\nt_start = time.time()\nprint({d: v for d, v in T.VERSIONS.items()})\n\"\"\")\n\nmd(r\"\"\"\n## 1. What the dandisets hold\n\nAsset lists and session descriptions for every dandiset the claims use, read from the DANDI API at the\npinned versions.\n\"\"\")\n\ncode(r\"\"\"\nassets = {d: T.list_assets(d) for d in T.VERSIONS}\nfor d, a in assets.items():\n    subjects = {x[\"path\"].split(\"/\")[0] for x in a}\n    print(f\"{d} {T.VERSIONS[d]}: {len(a)} assets, {len(subjects)} subjects, \"\n          f\"{sum(x['size'] for x in a) / 1e9:.2f} GB\")\n# the two published versions of DANDI:001274\nolder = T._get(f\"{T.API}/dandisets/001274/versions/0.250701.1622/assets/?page_size=1000\")\nolder_paths = {(x[\"path\"], x[\"size\"]) for x in older[\"results\"]}\nnewer_paths = {(x[\"path\"], x[\"size\"]) for x in assets[\"001274\"]}\nprint(\"001274 versions 0.250701.1622 and 0.250805.1401 have the same paths and sizes:\",\n      older_paths == newer_paths, f\"({len(older_paths)} and {len(newer_paths)} assets)\")\n\"\"\")\n\ncode(r\"\"\"\n# One strobe file of DANDI:001274, everything it holds (the long schema strings are left out).\ndef listing(url):\n    out = []\n    with h5py.File(remfile.File(url), \"r\") as f:\n        def visit(name, obj):\n            if name.startswith(\"specifications\"):\n                return\n            if isinstance(obj, h5py.Dataset):\n                v = obj[()] if obj.size < 4 else None\n                out.append(f\"D {name} {obj.shape} {obj.dtype} {'' if v is None else str(v)[:120]}\")\n            else:\n                out.append(f\"G {name} {dict(obj.attrs).get('neurodata_type', '')}\")\n        f.visititems(visit)\n    return out\nprint(\"\\n\".join(listing(assets[\"001274\"][0][\"url\"])))\nprint()\nprint(\"\\n\".join(listing(assets[\"001032\"][0][\"url\"])))\n\"\"\")\n\nmd(r\"\"\"\n### DANDI:001274: sessions per subject\n\nThe stimulus, voltage and tetrodotoxin are read from each session's description. Frame counts and\nsession start times are read from the files' headers, without the images.\n\"\"\")\n\ncode(r\"\"\"\ndef strobe_kind(desc):\n    k = (\"pulse\" if \"rectangular pulse\" in desc else \"sine 100 Hz\" if \"100Hz\" in desc\n         else \"sine 154 Hz\" if \"154Hz\" in desc else \"sine\")\n    v = float(re.search(r\"at ([\\d,]+)V\", desc).group(1).replace(\",\", \".\"))\n    return k, v, \"TTX\" if \"presence of the sodium\" in desc else \"vehicle\"\n\ndef strobe_header(a):\n    with h5py.File(remfile.File(a[\"url\"]), \"r\") as f:\n        return f[\"acquisition/StrobeImaging/data\"].shape, f[\"session_start_time\"][()].decode()\n\nfrom concurrent.futures import ThreadPoolExecutor\nwith ThreadPoolExecutor(16) as ex:\n    heads = list(ex.map(strobe_header, assets[\"001274\"]))\nstrobe = pd.DataFrame([dict(subject=a[\"path\"].split(\"/\")[0], path=a[\"path\"], url=a[\"url\"],\n                            kind=strobe_kind(a[\"description\"])[0], volts=strobe_kind(a[\"description\"])[1],\n                            solution=strobe_kind(a[\"description\"])[2], frames=h[0][0],\n                            shape=h[0], start=h[1]) for a, h in zip(assets[\"001274\"], heads)])\nprint(strobe.groupby([\"subject\", \"kind\", \"volts\", \"solution\", \"frames\"]).size().to_string())\nprint(\"image sizes:\", strobe[\"shape\"].apply(lambda s: s[1:]).value_counts().to_dict())\n\"\"\")\n\nmd(r\"\"\"\nThe strobe files hold the raw image stacks only: no ROIs, no RATIO images, no field per session (the\ndescriptions give generator volts, not V/cm) and no frame times. The paper's nine cells C1 to C9 each had\na 2-us pulse and 100-Hz modulated sine waves; nine subjects here have a pulse and 100-Hz sessions\n(listed below), which is consistent with them being C1 to C9 but does not show it. The cell of Figure 5\n(C7) had 12 sessions at each of 100 and 154 Hz; no subject has 12 sessions at 100 Hz.\nMany sessions recorded on 2024-08-24 are labelled as made in 1 uM tetrodotoxin, which the paper does not\nmention for Figures 5, 6 or S3.\n\"\"\")\n\ncode(r\"\"\"\nhas = strobe.groupby(\"subject\").kind.agg(lambda k: set(k))\ncand = sorted(s for s, k in has.items() if \"pulse\" in k and \"sine 100 Hz\" in k)\nprint(\"subjects with a pulse and 100-Hz sessions:\", len(cand), cand)\nc = strobe[(strobe.kind != \"pulse\")].groupby([\"subject\", \"kind\"]).size().unstack(fill_value=0)\nprint(\"most 100-Hz sessions in one subject:\", c.get(\"sine 100 Hz\", pd.Series([0])).max(),\n      \"; most 154-Hz sessions:\", c.get(\"sine 154 Hz\", pd.Series([0])).max())\n\"\"\")\n\nmd(r\"\"\"\n### DANDI:001034 is a second deposit of 001032\n\nThe two dandisets have the same subjects (`sub-N-1` in 001032, `sub-N-3` in 001034), the same sessions\nand the same sizes. The check below compares session names and start times for every asset, and the image\narrays of ten pairs.\n\"\"\")\n\ncode(r\"\"\"\ndef strip(p, k):\n    return re.sub(rf\"sub-(\\d+)-{k}\", r\"sub-\\1\", p.split(\"/\")[1])\na32 = {strip(x[\"path\"], 1): x for x in assets[\"001032\"]}\na34 = {strip(x[\"path\"], 3): x for x in assets[\"001034\"]}\nprint(\"asset names in common:\", len(set(a32) & set(a34)), \"of\", len(a32), \"and\", len(a34))\nsame_meta = sum(a32[k][\"description\"].replace(\"1_1\", \"\") is not None and a32[k][\"session\"] == a34[k][\"session\"]\n                and a32[k][\"size\"] == a34[k][\"size\"] for k in set(a32) & set(a34))\nprint(\"same session name and size:\", same_meta)\ndef stack_and_start(url):\n    with h5py.File(remfile.File(url), \"r\") as f:\n        g = f[\"acquisition/TimeLapseImaging\"]\n        return g[\"data\"][:], f[\"session_start_time\"][()].decode()\ncommon = sorted(set(a32) & set(a34))\npairs = common[:: max(1, len(common) // 10)][:10]\nidentical = 0\nfor k in pairs:\n    x, sx = stack_and_start(a32[k][\"url\"]); y, sy = stack_and_start(a34[k][\"url\"])\n    identical += int(x.shape == y.shape and np.array_equal(x, y) and sx == sy)\nprint(f\"identical arrays and start times: {identical} of {len(pairs)} pairs compared\")\n\"\"\")\n\nmd(r\"\"\"\n## 2. Load the fast recordings\n\nEvery fast recording of 001032, 001033, 001035 (Figures 1 and 2), 001030 (Figure 3C), 001271 (Figure S2)\nand 001272 (Figure S1) is streamed and reduced to two dF traces as it loads (`ti_sine.load_fast`). 001034 is\nleft out as a duplicate. This takes about ten minutes.\n\"\"\")\n\ncode(r\"\"\"\nFAST = [\"001032\", \"001033\", \"001035\", \"001271\", \"001272\"]\nrecs = {}\nfor d in FAST:\n    t = time.time()\n    recs[d] = T.load_fast(assets[d])\n    print(d, len(recs[d]), f\"files in {time.time() - t:.0f} s\")\nrecs[\"001030\"] = T.load_fast(assets[\"001030\"], stim_start_s=0.025)   # 001030: stimulus at 25 ms\nprint(\"001030\", len(recs[\"001030\"]))\n\"\"\")\n\nmd(r\"\"\"\n## 3. Data check\n\"\"\")\n\ncode(r\"\"\"\nfast = pd.concat([T.session_table(recs[d], d) for d in [\"001032\", \"001033\", \"001035\"]], ignore_index=True)\nt71 = T.session_table(recs[\"001271\"], \"001271\")\nt72 = T.session_table(recs[\"001272\"], \"001272\", invert=True, sd_levels=(5,))\nallrec = [r for d in recs for r in recs[d]]\nprint(\"files:\", {d: len(v) for d, v in recs.items()})\nprint(\"frame shapes and rates:\")\nprint(pd.DataFrame([dict(dandiset=r[\"path\"] and d, shape=str(r[\"shape\"]), rate=r[\"rate\"]) for d in recs for r in recs[d]])\n      .groupby([\"dandiset\", \"shape\", \"rate\"]).size().to_string())\nprint(\"\\nneurons per dandiset:\", {d: len({T.neuron_of(d, r['path']) for r in recs[d]}) for d in recs})\nprint(\"\\nsessions by carrier and modulation (001032, 001033, 001035):\")\nprint(fast.groupby([\"dandiset\", \"carrier\", \"modulated\"]).size().unstack(fill_value=0).to_string())\nprint(\"\\ngenerator voltage (V peak to peak), range by dandiset:\",\n      {d: (g.voltage.min(), g.voltage.max()) for d, g in fast.groupby(\"dandiset\")})\nff = np.array([r[\"first_frame_ratio\"] for r in allrec])\nprint(f\"\\nfirst frame over the mean of the other pre-stimulus frames: median {np.median(ff):.2f}, \"\n      f\"range {ff.min():.2f} to {ff.max():.2f} (left out of F0)\")\nprint(\"raw F0 (camera counts), range:\", f\"{min(r['raw_f0'] for r in allrec):.0f} to {max(r['raw_f0'] for r in allrec):.0f}\")\nfor roi in T.ROIS:\n    sd = fast[f\"pre_sd/{roi}\"]\n    print(f\"pre-stimulus SD of dF ({roi}): median {sd.median():.2f}%, range {sd.min():.2f} to {sd.max():.2f}\")\n\"\"\", \"sanity\")\n\nmd(r\"\"\"\nChecks of the descriptions against the data:\n\n- The paper's fast recordings have 64 x 64 pixels and 1,200 frames per session at 3,130 or 3,086.4 frames/s\n  (Methods). The files have 16 x 16 pixels; most have 1,200 frames at 3,086.4 frames/s, some 900, 1,400\n  or 1,800 (001032) and one 6,000 (a long sham, 001035). The 2-s recordings of 001030 have 6,000 or 7,000\n  frames at 3,134.8 frames/s; at 6,000 frames the recording ends before the 2-s stimulus does.\n- The description of 001032 to 001035 gives a 140-um electrode gap; the Methods give 120 um.\n- AP size: the Methods give typical APs of 11.3% +- 0.9% dF. The first AP of each session, whole-frame\n  trace, is printed below and serves to choose the soma reading.\n- Stimulus timing: the files carry no stimulus channel. Two checks support the 50-ms onset of the Methods:\n  APs are found during the stimulus and almost never before it, and in sessions with 20-Hz modulation the\n  APs lock to the beats counted from that onset, which they do not when the beats are shifted by half a\n  beat (25 ms).\n\"\"\")\n\ncode(r\"\"\"\nfor roi in T.ROIS:\n    h = []\n    for d in [\"001032\", \"001033\", \"001035\"]:\n        for r in recs[d]:\n            a = T.aps_in_window(r[roi], r[\"rate\"], r[\"onset\"], reading=\"a\")\n            if len(a):\n                h.append(r[roi][r[\"onset\"] + int(round(a[0] * r[\"rate\"]))])\n    print(f\"first-AP peak dF, {roi} trace: median {np.median(h):.1f}%, IQR {np.percentile(h, 25):.1f} to \"\n          f\"{np.percentile(h, 75):.1f}%, n = {len(h)} sessions\")\nfor key in [f\"{roi}/{rd}\" for roi in T.ROIS for rd in T.AP_READINGS]:\n    pre = fast[f\"pre_aps/{key}\"].sum()\n    dur = fast[f\"naps/{key}\"].sum()\n    print(f\"{key}: {pre} APs in {len(fast)} pre-stimulus windows (49 ms each; {pre / len(fast) * 250 / 49:.2f} \"\n          f\"per 250 ms) against {dur} during the 250-ms stimuli ({dur / len(fast):.2f} per session)\")\n\"\"\", \"sanity\")\n\ncode(r\"\"\"\nmod = fast[fast.carrier.isin([\"2k\", \"20k\"]) & fast.modulated]\ndef in_peak_window(times_s, shift_s=0.0):\n    ph = ((times_s - shift_s) * 1000) % 50\n    return (ph >= 12.5) & (ph <= 37.5)\nfor key in [\"whole/a\", \"whole/b\"]:\n    t = np.concatenate(mod[f\"aps/{key}\"].values)\n    print(f\"{key}: {len(t)} APs in {len(mod)} modulated sessions; in the middle half of the beat: \"\n          f\"{in_peak_window(t).mean():.2f} with beats from the 50-ms onset, \"\n          f\"{in_peak_window(t, 0.025).mean():.2f} with beats shifted by 25 ms (chance 0.5)\")\n\"\"\", \"sanity\")\n\nmd(r\"\"\"\nThe whole-frame trace gives APs of the size the Methods report, so it is adopted as the soma reading\n(assumption); the bright-pixel trace is shown as a variant throughout. Reading (b) on the bright-pixel\ntrace finds more than one AP per 250 ms in the pre-stimulus windows, so it is the noisiest of the four.\n\nThe field: the descriptions of 001032 to 001035, 001271 and 001272 say \"1V translates into 36 V/cm at the\nlocation of neurons\" and give peak-to-peak volts; 001030 gives volts of one polarity. The claims file takes\nthe field from this metadata. The adopted reading is the peak field, 36 V/cm x Vpp / 2 (assumption: it is\nhow 001030 states its voltages, and Figure 3A's 63 V/cm near threshold matches the 1.75 V of one polarity\nthere), and 36 V/cm x Vpp is run as the other reading. The descriptions also say the generator voltage is\n\"not the actual amplitude measured on the oscilloscope, which will be somewhat smaller (calibration factors\nare frequency-dependent and will be reported separately)\"; those factors are not in the dandisets.\n\"\"\")\n\nKEYS = '[\"whole/a\", \"whole/b\", \"bright/a\", \"bright/b\"]'\n\nmd(r\"\"\"\n## 4. fig1-pure-sine-excites-all\n\n> Unmodulated 250-ms sine waves at 2 kHz and at 20 kHz excited every neuron tested, never as an on-off\n> response.\n\nPer neuron, excited when at least one session with an unmodulated 2- or 20-kHz sine wave has an AP during\nthe stimulus. Reproduced when, under each AP reading, at least 90% of neurons tested with each frequency\nare excited. The Methods select neurons whose APs peak above 5% dF, so a variant counts only neurons with\nan AP in some session of any kind.\n\"\"\")\n\ncode(r\"\"\"\nunmod = fast[fast.carrier.isin([\"2k\", \"20k\"]) & ~fast.modulated].copy()\nfired_any = fast.groupby(\"neuron\")[\"naps/whole/a\"].max() > 0\nfor key in \"\"\" + KEYS + r\"\"\":\n    e = unmod.groupby([\"carrier\", \"neuron\"])[f\"naps/{key}\"].max() > 0\n    res = {c: f\"{int(g.sum())}/{len(g)} = {100 * g.mean():.0f}%\" for c, g in e.groupby(level=0)}\n    sel = e[[fired_any[n] for _, n in e.index]]\n    res_sel = {c: f\"{int(g.sum())}/{len(g)}\" for c, g in sel.groupby(level=0)}\n    print(f\"{key}: excited {res}; among neurons with an AP in any session {res_sel}\")\ne = unmod.groupby([\"carrier\", \"neuron\"])[\"naps/whole/a\"].max()\nfor (c, n) in e[e == 0].index:\n    g = unmod[(unmod.neuron == n) & (unmod.carrier == c)]\n    print(f\"not excited at {c}: {n}, {len(g)} sessions, fields {T.field(g.voltage.min()):.0f} to \"\n          f\"{T.field(g.voltage.max()):.0f} V/cm; APs in its other sessions: {int(fast[fast.neuron == n]['naps/whole/a'].sum())}\")\nprint(\"neurons by dandiset:\", unmod.groupby([\"dandiset\", \"carrier\"]).neuron.nunique().to_dict())\n\"\"\", \"claim:fig1-pure-sine-excites-all\")\n\nmd(r\"\"\"\n**Result: ...**\n\"\"\")\n\nmd(r\"\"\"\n## 5. fig1-onset-delay\n\n> Near threshold, isolated APs appear 100 to 200 ms after the sine wave onset, and stronger fields shorten\n> this delay and evoke sustained firing.\n\nPer neuron and frequency, the near-threshold session is the lowest field with at least one AP. Reproduced\nwhen the median first-AP latency of those sessions lies within 90 to 220 ms and the Spearman correlation of\nfirst-AP latency with field is below zero in more than half of the neuron-frequency pairs with at least\nthree fields with APs. The latency does not depend on the field reading.\n\"\"\")\n\ncode(r\"\"\"\nonset = {}\nfor key in \"\"\" + KEYS + r\"\"\":\n    pf = T.per_field(unmod, key)\n    nt = pf[pf.n > 0].sort_values(\"field\").groupby([\"neuron\", \"carrier\"]).first()\n    lat = nt.lat * 1000\n    rho = np.array([stats.spearmanr(g.field, g.lat).statistic\n                    for _, g in pf[pf.n > 0].groupby([\"neuron\", \"carrier\"]) if len(g) >= 3])\n    onset[key] = (lat, rho)\n    by_c = {c: f\"{g.median():.0f} ms (n = {len(g)})\" for c, g in lat.groupby(level=1)}\n    print(f\"{key}: near-threshold first-AP latency median {lat.median():.0f} ms, IQR {lat.quantile(.25):.0f} \"\n          f\"to {lat.quantile(.75):.0f}, n = {len(lat)}; by carrier {by_c}; latency falls with field \"\n          f\"(rho < 0) in {np.sum(rho < 0)} of {len(rho)} (median rho {np.median(rho):.2f})\")\n# variant: thresholds bracketed by a lower-field session without APs\npf = T.per_field(unmod, \"whole/a\")\nbr = []\nfor (n, c), g in pf.groupby([\"neuron\", \"carrier\"]):\n    g = g.sort_values(\"field\"); fired = g[g.n > 0]\n    if len(fired) and (g.field < fired.field.iloc[0]).any():\n        br.append(dict(neuron=n, carrier=c, lat=fired.lat.iloc[0] * 1000))\nbr = pd.DataFrame(br)\nprint(f\"variant, whole/a, near-threshold sessions with a lower-field session without APs: median \"\n      f\"{br.lat.median():.0f} ms, n = {len(br)}; by carrier {br.groupby('carrier').lat.median().round(0).to_dict()}\")\nprint(\"by dandiset (whole/a):\", onset[\"whole/a\"][0].groupby(lambda i: i[0].split('/')[0]).median().round(0).to_dict())\n\"\"\", \"claim:fig1-onset-delay\")\n\ncode(r\"\"\"\nlat, rho = onset[\"whole/a\"]\nfig, ax = plt.subplots(1, 2, figsize=(9, 3.2))\nax[0].hist(lat, bins=np.arange(0, 260, 20), color=\"0.4\")\nax[0].axvspan(100, 200, color=\"C1\", alpha=0.2, label=\"paper, 100 to 200 ms\")\nax[0].set_xlabel(\"near-threshold first-AP latency (ms)\"); ax[0].set_ylabel(\"neuron-carrier pairs\"); ax[0].legend()\nax[1].hist(rho, bins=np.linspace(-1, 1, 11), color=\"0.4\"); ax[1].set_xlabel(\"Spearman rho, latency against field\")\nplt.tight_layout(); plt.show()\nprint(f\"latency range {lat.min():.0f} to {lat.max():.0f} ms (all inside the axis); rho range {rho.min():.2f} to {rho.max():.2f}\")\n\"\"\", \"claim:fig1-onset-delay\")\n\nmd(r\"\"\"\n**Result: ...**\n\"\"\")\n\nmd(r\"\"\"\n## 6. fig1-max-rate-ceiling\n\n> The maximum firing rate increases linearly with field strength until it reaches a ceiling of 60 to 90 Hz.\n\nThe maximum firing rate of a session is the inverse of the interval between its first two APs (Methods);\nthe ceiling of a neuron is its highest over unmodulated sessions. Reproduced when the median ceiling over\nneurons lies within 54 to 99 Hz. The AP detection cannot see rates above 125 Hz (8-ms merge, `ti_sine`).\n\"\"\")\n\ncode(r\"\"\"\nfor key in \"\"\" + KEYS + r\"\"\":\n    pf = T.per_field(unmod, key)\n    ceil = pf.groupby(\"neuron\").rate_hz.max().dropna()\n    slopes = []\n    for _, g in pf.dropna(subset=[\"rate_hz\"]).groupby([\"neuron\", \"carrier\"]):\n        g = g.sort_values(\"field\")\n        upto = g.iloc[: int(np.argmax(g.rate_hz.values)) + 1]\n        if len(upto) >= 3:\n            slopes.append(stats.linregress(upto.field, upto.rate_hz).slope)\n    print(f\"{key}: ceiling median {ceil.median():.1f} Hz (IQR {ceil.quantile(.25):.1f} to {ceil.quantile(.75):.1f}, \"\n          f\"range {ceil.min():.1f} to {ceil.max():.1f}, n = {len(ceil)} neurons); slope of rate on field before the \"\n          f\"ceiling: median {np.median(slopes):.2f} Hz per V/cm, positive in {np.sum(np.array(slopes) > 0)} of {len(slopes)}\")\nprint(\"neurons with fewer than two APs in every unmodulated session have no rate:\",\n      unmod.neuron.nunique() - T.per_field(unmod, 'whole/a').groupby('neuron').rate_hz.max().notna().sum())\n\"\"\", \"claim:fig1-max-rate-ceiling\")\n\nmd(r\"\"\"\n**Result: ...**\n\"\"\")\n\nmd(r\"\"\"\n## 7. fig1-excitation-block\n\n> At the highest field strengths, APs coalesce into low-amplitude oscillations on a continuous\n> depolarization, which can flatten and leave the membrane depolarized for the rest of the sine wave (an\n> excitation block).\n\nPer neuron and frequency, the highest-field unmodulated session against the near-threshold session.\nReproduced when, in more than half, the mean dF over the last 100 ms of the stimulus at the highest field\nis above 5% and above that of the near-threshold session. The mean over the second half of the stimulus is a\nvariant.\n\"\"\")\n\ncode(r\"\"\"\nfor key in \"\"\" + KEYS + r\"\"\":\n    pf = T.per_field(unmod, key)\n    nt = pf[pf.n > 0].sort_values(\"field\").groupby([\"neuron\", \"carrier\"]).first()\n    hi = pf.sort_values(\"field\").groupby([\"neuron\", \"carrier\"]).last()\n    j = hi.join(nt[[\"last\", \"field\"]].rename(columns={\"last\": \"last_nt\", \"field\": \"field_nt\"}), how=\"inner\")\n    blk = (j[\"last\"] > 5) & (j[\"last\"] > j[\"last_nt\"])\n    blk2 = j[\"half2\"] > 5\n    print(f\"{key}: block in {blk.sum()} of {len(j)} neuron-carrier pairs; highest-field last-100-ms dF median \"\n          f\"{j['last'].median():.1f}% (range {j['last'].min():.1f} to {j['last'].max():.1f}); near-threshold median \"\n          f\"{j['last_nt'].median():.1f}%; highest over near-threshold field median {np.median(j.index.map(lambda i: hi.loc[i, 'field']) / j.field_nt):.2f}; \"\n          f\"variant second half > 5%: {blk2.sum()}\")\nd = unmod.assign(field=T.field(unmod.voltage))\nprint(\"sessions with last-100-ms dF above 5% (whole):\", int((d['last100/whole'] > 5).sum()), \"of\", len(d),\n      \"; highest field per carrier:\", d.groupby(\"carrier\").field.max().to_dict())\n\"\"\", \"claim:fig1-excitation-block\")\n\nmd(r\"\"\"\n**Result: ...**\n\"\"\")\n\nmd(r\"\"\"\n## 8. fig2d-20khz-twofold-threshold, fig2d-modulated-thresholds-higher, threshold-2khz-unmodulated\n\nThresholds per neuron and stimulus are the lowest field with at least 1 (5) APs (Figure 2D legend).\n\n> All excitation thresholds at 20 kHz were about twice those at 2 kHz (p < 0.0001, two-tailed unpaired t test).\n\nReproduced when each of the four 20 to 2 kHz ratios of mean thresholds is within 1.8 to 2.2 and the t test\ngives p < 0.0001 per group and pooled.\n\"\"\")\n\ncode(r\"\"\"\nstim = fast[fast.carrier.isin([\"2k\", \"20k\"])]\nthr = {(key, fr): T.thresholds(stim, key, fr) for key in \"\"\" + KEYS + r\"\"\" for fr in (\"half\", \"full\")}\nth = thr[(\"whole/a\", \"half\")]\nprint(\"whole/a, field = 36 V/cm x Vpp / 2: mean, SEM and n of thresholds (V/cm)\")\nprint(th.groupby([\"aps\", \"stim\"]).thr.agg([\"mean\", \"sem\", \"count\"]).round(1).unstack(0).to_string())\nfor key in \"\"\" + KEYS + r\"\"\":\n    th = thr[(key, \"half\")]\n    out = []\n    for k in (1, 5):\n        for m in (\"unmod\", \"mod\"):\n            a = th[(th.aps == k) & (th.stim == f\"2k/{m}\")].thr.dropna()\n            b = th[(th.aps == k) & (th.stim == f\"20k/{m}\")].thr.dropna()\n            out.append(f\"{k} AP {m} {b.mean() / a.mean():.2f} (p = {stats.ttest_ind(b, a).pvalue:.1g}, n {len(a)}/{len(b)})\")\n    a = th[th.stim.str.startswith(\"2k/\")].thr.dropna(); b = th[th.stim.str.startswith(\"20k/\")].thr.dropna()\n    out.append(f\"pooled {b.mean() / a.mean():.2f} (p = {stats.ttest_ind(b, a).pvalue:.1g})\")\n    print(f\"{key}: 20/2 kHz ratio \" + \"; \".join(out))\n\"\"\", \"claim:fig2d-20khz-twofold-threshold\")\n\nmd(r\"\"\"\n**Result: ...**\n\"\"\")\n\nmd(r\"\"\"\n> Thresholds for sine waves modulated at 20 Hz were significantly higher than for pure sine waves of the\n> same carrier, for 5 APs at 2 kHz and for 1 and 5 APs at 20 kHz.\n\nTwo-tailed unpaired t test per pair; reproduced when all three have the modulated mean higher with p < 0.05,\npartially when one or two do. The paired test on neurons with both is a variant; the 2-kHz 1-AP pair is\nreported.\n\"\"\")\n\ncode(r\"\"\"\nfor key in \"\"\" + KEYS + r\"\"\":\n    th = thr[(key, \"half\")]\n    out = []\n    for c, k in [(\"2k\", 5), (\"20k\", 1), (\"20k\", 5), (\"2k\", 1)]:\n        u = th[(th.aps == k) & (th.stim == f\"{c}/unmod\")].set_index(\"neuron\").thr\n        m = th[(th.aps == k) & (th.stim == f\"{c}/mod\")].set_index(\"neuron\").thr\n        both = pd.concat([u, m], axis=1, keys=[\"u\", \"m\"]).dropna()\n        pp = stats.ttest_rel(both.m, both.u).pvalue if len(both) > 1 else np.nan\n        out.append(f\"{c} {k} AP: mod {m.mean():.0f} vs unmod {u.mean():.0f} V/cm, unpaired p = \"\n                   f\"{stats.ttest_ind(m.dropna(), u.dropna()).pvalue:.3f} (n {m.count()}/{u.count()}); paired p = {pp:.3f} (n {len(both)})\")\n    print(key + \":\\n  \" + \"\\n  \".join(out))\n\"\"\", \"claim:fig2d-modulated-thresholds-higher\")\n\nmd(r\"\"\"\n**Result: ...**\n\"\"\")\n\nmd(r\"\"\"\n> The AP threshold for unmodulated 2-kHz sine waves was 57.7 plus or minus 3.6 V/cm.\n\nMean 1-AP threshold over neurons, under both AP readings and both field readings.\n\"\"\")\n\ncode(r\"\"\"\nfor key in \"\"\" + KEYS + r\"\"\":\n    for fr in (\"half\", \"full\"):\n        th = thr[(key, fr)]\n        u = th[(th.aps == 1) & (th.stim == \"2k/unmod\")]\n        ub = u[u.bracketed]\n        print(f\"{key}, field {fr}: {u.thr.mean():.1f} +- {u.thr.sem():.1f} V/cm (n = {u.thr.count()}); \"\n              f\"only thresholds with a lower-field session without APs: {ub.thr.mean():.1f} (n = {len(ub)})\")\nu = thr[(\"whole/a\", \"half\")]; u = u[(u.aps == 1) & (u.stim == \"2k/unmod\")]\nprint(\"by dandiset (whole/a, half):\", u.groupby(u.neuron.str[:6]).thr.agg([\"mean\", \"count\"]).round(1).to_dict(\"index\"))\n\"\"\", \"claim:threshold-2khz-unmodulated\")\n\nmd(r\"\"\"\n**Result: ...**\n\"\"\")\n\nmd(r\"\"\"\n## 9. fig2-modulated-locks-to-beats\n\n> With 20-Hz modulation, firing above threshold is locked to the beats, one AP near the peak of each of the\n> five beats and at most two per beat (ten in all), and modulated sine waves trigger no sustained firing or\n> sustained depolarization.\n\nReproduced when (i) no modulated session has more than 10 APs, (ii) in sessions with 5 APs or more at least\n80% of APs fall 12.5 to 37.5 ms into a 50-ms beat counted from the onset, and (iii) no modulated session has\na last-100-ms mean dF above 5%. (ii) is read on the APs pooled over those sessions; the fraction of sessions\nthat pass on their own is also shown.\n\"\"\")\n\ncode(r\"\"\"\nfor key in \"\"\" + KEYS + r\"\"\":\n    roi = key.split(\"/\")[0]\n    n = mod[f\"naps/{key}\"]\n    sel = mod[n >= 5]\n    pooled = np.concatenate(sel[f\"aps/{key}\"].values)\n    per = np.array([in_peak_window(a).mean() for a in sel[f\"aps/{key}\"]])\n    hist = np.histogram((np.concatenate(mod[f\"aps/{key}\"].values) * 1000) % 50, bins=10, range=(0, 50))[0]\n    print(f\"{key}: {len(mod)} sessions; most APs {n.max()}, sessions above 10: {(n > 10).sum()}; \"\n          f\"{len(sel)} sessions with >= 5 APs, pooled fraction in window {in_peak_window(pooled).mean():.2f}, \"\n          f\"sessions with >= 80%: {np.sum(per >= 0.8)} of {len(sel)}; sessions with last-100-ms dF > 5%: \"\n          f\"{(mod[f'last100/{roi}'] > 5).sum()}; APs per 5 ms of the beat {hist.tolist()}\")\nprint(mod.assign(field=T.field(mod.voltage)).loc[(mod[\"naps/whole/a\"] > 10) | (mod[\"last100/whole\"] > 5),\n      [\"neuron\", \"carrier\", \"field\", \"naps/whole/a\", \"naps/whole/b\", \"last100/whole\"]].to_string())\n\"\"\", \"claim:fig2-modulated-locks-to-beats\")\n\nmd(r\"\"\"\n**Result: ...**\n\"\"\")\n\nmd(r\"\"\"\n## 10. fig2c-pure-more-aps\n\n> In the same neuron at the same field strength, pure sine waves trigger more APs than modulated ones.\n\nPairs are a neuron's modulated and unmodulated sessions at one carrier and one field (counts averaged over\nrepeats). Reproduced when the unmodulated count is higher in more pairs than the reverse, with a two-sided\npaired t test at p < 0.05.\n\"\"\")\n\ncode(r\"\"\"\nfor key in \"\"\" + KEYS + r\"\"\":\n    g = stim.groupby([\"neuron\", \"carrier\", \"voltage\", \"modulated\"])[f\"naps/{key}\"].mean().unstack(\"modulated\").dropna()\n    d = g[False] - g[True]\n    print(f\"{key}: {len(g)} pairs in {g.reset_index().neuron.nunique()} neurons; unmodulated more in {(d > 0).sum()}, \"\n          f\"modulated more in {(d < 0).sum()}, equal in {(d == 0).sum()}; mean difference {d.mean():.2f} APs; \"\n          f\"paired t p = {stats.ttest_rel(g[False], g[True]).pvalue:.2g}; by carrier \"\n          f\"{d.groupby(level=1).agg(lambda x: f'{(x > 0).sum()}/{len(x)}').to_dict()}\")\n\"\"\", \"claim:fig2c-pure-more-aps\")\n\nmd(r\"\"\"\n**Result: ...**\n\"\"\")\n\nmd(r\"\"\"\n## 11. fig3c-sustained-firing-2s (DANDI:001030)\n\n> In the low-conductivity solution, a 2-s unmodulated 2-kHz sine wave ramped up over 250 ms evoked sustained\n> firing for the whole stimulus; firing rate rose with field strength until replaced by a firing block with\n> sustained depolarization, which developed before the end of the ramp.\n\nTraces are corrected for bleaching by subtracting a trace without APs (Methods). The only trace without APs\nin 001030 is neuron c7 at 1.0 V (one polarity, 36 V/cm), so the test is made on c7, the neuron recorded at the\nmost fields, and the other neurons are shown with the same correction. Reproduced when (i) at an intermediate\nfield APs occur in the last 250 ms, (ii) the AP count rises with field up to some field, and (iii) at the\nhighest field there are no APs after 250 ms and the mean dF over the rest of the stimulus is above 5%.\n\"\"\")\n\ncode(r\"\"\"\nr30 = {r[\"path\"]: r for r in recs[\"001030\"]}\nt30_raw = T.session_table(recs[\"001030\"], \"001030\", dur_s=2.0)\nnoap = t30_raw[(t30_raw[\"naps/whole/a\"] == 0) & (t30_raw[\"naps/whole/b\"] == 0)]\nprint(\"sessions without APs under both readings (uncorrected):\", noap[[\"neuron\", \"voltage\"]].values.tolist())\nref = r30[noap.path.iloc[0]]\ncorr = {}\nfor p, r in r30.items():\n    n = min(len(r[\"whole\"]), len(ref[\"whole\"]))\n    corr[p] = {roi: r[roi][:n] - ref[roi][:n] for roi in T.ROIS}\nt30 = T.session_table(recs[\"001030\"], \"001030\", dur_s=2.0, traces=corr)\nt30[\"field\"] = T.field(t30.voltage)          # voltage holds 2 x the one-polarity volts\nrows = []\nfor _, s in t30.iterrows():\n    rate, on = s.rate, s.onset\n    n = len(corr[s.path][\"whole\"])\n    row = dict(neuron=s.neuron, field=s.field, frames=s.n_frames, rest_dF=round(s[\"half2/whole\"], 1))\n    end = min(2.0, (n - on) / rate)\n    row[\"rest_dF\"] = round(T.window_mean(corr[s.path][\"whole\"], rate, on, 0.25, end), 1)\n    for rd in \"ab\":\n        a = s[f\"aps/whole/{rd}\"]\n        row[f\"{rd}: all\"] = len(a); row[f\"{rd}: after 250 ms\"] = int((a > 0.25).sum()); row[f\"{rd}: last 250 ms\"] = int((a > 1.75).sum())\n    rows.append(row)\nf3c = pd.DataFrame(rows).sort_values([\"neuron\", \"field\"])\nprint(f3c.to_string(index=False))\nc7 = f3c[f3c.neuron.str.endswith(\"c7\")]\ntop = c7.iloc[-1]\na_top = t30[(t30.neuron == top.neuron) & (t30.field == top.field)][\"aps/whole/b\"].iloc[0]\nprint(f\"c7 at the highest field ({top.field:.0f} V/cm), reading b AP times (s): {np.round(a_top, 3).tolist()}\")\n\"\"\", \"claim:fig3c-sustained-firing-2s\")\n\nmd(r\"\"\"\n**Result: ...**\n\"\"\")\n\nmd(r\"\"\"\n## 12. figs1-di8-anepps-control (DANDI:001272)\n\n> With Di-8-ANEPPS instead of FluoVolt, in eight neurons, stimulation near threshold elicited one or a few\n> delayed APs and stronger fields induced sustained firing ending in sustained depolarization, as with\n> FluoVolt.\n\nTraces inverted (Di-8-ANEPPS emission falls with depolarization, Methods). AP readings: (a) and (b) at 5% dF,\nand both at 5 pre-stimulus SDs. Reproduced when, under every reading, every neuron is excited, latency falls\nwith field in more than half, and the highest field meets the block test in more than half; blocked as\nmethods_underspecified when the readings disagree.\n\"\"\")\n\ncode(r\"\"\"\nprint(\"neurons:\", t72.neuron.nunique(), \"(the paper: eight);\", t72.groupby(\"neuron\").size().to_dict())\nprint(f\"pre-stimulus SD of the inverted whole-frame dF: median {t72['pre_sd/whole'].median():.2f}%\")\nfor key in [\"whole/a\", \"whole/b\", \"whole/a5sd\", \"whole/b5sd\"]:\n    roi = \"whole\"\n    d = t72.assign(field=T.field(t72.voltage), n=t72[f\"naps/{key}\"],\n                   lat=t72[f\"aps/{key}\"].apply(lambda a: a[0] if len(a) else np.nan), last=t72[\"last100/whole\"])\n    pf = d.groupby([\"neuron\", \"field\"]).agg(n=(\"n\", \"mean\"), lat=(\"lat\", \"mean\"), last=(\"last\", \"mean\")).reset_index()\n    exc = pf.groupby(\"neuron\").n.max() > 0\n    rho = {nr: stats.spearmanr(g.field, g.lat).statistic for nr, g in pf[pf.n > 0].groupby(\"neuron\") if len(g) >= 3}\n    blk = {}\n    for nr, g in pf.groupby(\"neuron\"):\n        f = g[g.n > 0].sort_values(\"field\")\n        hi = g.sort_values(\"field\").iloc[-1]\n        blk[nr] = bool(len(f) and hi[\"last\"] > 5 and hi[\"last\"] > f.iloc[0][\"last\"])\n    print(f\"{key}: excited {int(exc.sum())}/{len(exc)}; rho {dict((k[-14:], round(v, 2)) for k, v in rho.items())}; \"\n          f\"block {sum(blk.values())}/{len(blk)}; APs per neuron {d.groupby('neuron').n.sum().to_dict()}\")\nprint(\"last-100-ms inverted dF at the highest field per neuron:\",\n      t72.assign(field=T.field(t72.voltage)).sort_values(\"field\").groupby(\"neuron\")[\"last100/whole\"].last().round(1).to_dict())\n\"\"\", \"claim:figs1-di8-anepps-control\")\n\nmd(r\"\"\"\n**Result: ...**\n\"\"\")\n\nmd(r\"\"\"\n## 13. figs2-ttx-blocks-depolarization (DANDI:001271)\n\n> 1 uM tetrodotoxin abolished both the APs and the sustained depolarization caused by intense unmodulated\n> 2-kHz sine waves.\n\nPer neuron, the session in normal solution and the session in TTX at the same field (the highest field\nrecorded in both; the latest normal session and the first TTX session at it). Reproduced when, in every TTX\nneuron, APs present before are absent after, and the last-100-ms mean dF is above 5% before and below 5% after,\nwhile a vehicle neuron keeps its response.\n\"\"\")\n\ncode(r\"\"\"\nd71 = t71.assign(field=T.field(t71.voltage))\nrows = []\nfor nr, g in d71.groupby(\"neuron\"):\n    tt = g[g.ttx & ~g.sham]; vv = g[~g.ttx & ~g.sham]\n    if not len(tt):\n        if g.ttx.any():\n            print(f\"{nr}: tetrodotoxin sessions are shams only ({int((g.ttx & g.sham).sum())})\")\n        continue\n    common = sorted(set(tt.field) & set(vv.field))\n    f = common[-1]\n    b = vv[vv.field == f].iloc[-1]; a = tt[tt.field == f].iloc[0]\n    rows.append(dict(neuron=nr, field=f, minutes_apart=round((pd.Timestamp(a.start) - pd.Timestamp(b.start)).total_seconds() / 60, 1),\n                     aps_before_a=b[\"naps/whole/a\"], aps_after_a=a[\"naps/whole/a\"],\n                     aps_before_b=b[\"naps/whole/b\"], aps_after_b=a[\"naps/whole/b\"],\n                     last100_before=round(b[\"last100/whole\"], 1), last100_after=round(a[\"last100/whole\"], 1),\n                     max_last100_vehicle=round(vv[\"last100/whole\"].max(), 1), max_last100_ttx=round(tt[\"last100/whole\"].max(), 1),\n                     ttx_sessions=len(tt), ttx_sessions_with_aps_a=int((tt[\"naps/whole/a\"] > 0).sum()),\n                     ttx_sessions_with_aps_b=int((tt[\"naps/whole/b\"] > 0).sum())))\ns2 = pd.DataFrame(rows)\nprint(s2.to_string(index=False))\nprint(\"TTX neurons where APs before and none after: reading a\", int(((s2.aps_before_a > 0) & (s2.aps_after_a == 0)).sum()),\n      \", reading b\", int(((s2.aps_before_b > 0) & (s2.aps_after_b == 0)).sum()), \"of\", len(s2))\nprint(\"TTX neurons with last-100-ms dF > 5% before and < 5% after:\",\n      int(((s2.last100_before > 5) & (s2.last100_after < 5)).sum()), \"of\", len(s2))\nveh = d71[~d71.neuron.isin(s2.neuron)]\nprint(\"neurons never in TTX:\", veh.neuron.nunique(), \"; sessions with last-100-ms dF > 5% among them:\",\n      int((veh[\"last100/whole\"] > 5).sum()), \"of\", len(veh))\nprint(\"all TTX sessions, last-100-ms dF range:\", round(d71[d71.ttx][\"last100/whole\"].min(), 1), \"to\",\n      round(d71[d71.ttx][\"last100/whole\"].max(), 1))\n\"\"\", \"claim:figs2-ttx-blocks-depolarization\")\n\nmd(r\"\"\"\n**Result: ...**\n\"\"\")\n\nmd(r\"\"\"\n## 14. Blocked claims, and the strobe images as a variant\n\n**fig3b-low-conductivity-halves-threshold.** No session of 001032, 001033 or 001035 is described as made in\nthe sodium gluconate solution; every description gives the NaCl solution. 001030 is in sodium gluconate but\nholds only 2-s ramped stimuli. The NaCl to NaGlu comparison cannot be found in the deposited files.\n\n**Figure 4 (001273).** The files hold raw strobe stacks only. The paper's ROIs over the most de- and\nhyperpolarized regions are not deposited, and no file says which cell is elongated or random, nor (in most\nfiles) which way the field was applied. The session counts are printed below.\n\n**Figures 5, 6 and S3 (001274).** No ROIs (the claims file's O1 blocks these claims as\nmetadata_insufficient when the dataset holds none), no field values in V/cm, and cells C7 and C8 cannot be\nidentified (O4). As the claims file asks, ROIs rebuilt from the RATIO image of the Methods are shown as a\nvariant only, for the pulse measure of Figure 6B, on the nine subjects that have a pulse and 100-Hz sine\nwaves. The field is taken as the paper's 257 V/cm for every pulse (Figure 6A legend), which the files do\nnot state.\n\"\"\")\n\ncode(r\"\"\"\nd73 = pd.DataFrame([dict(subject=a[\"path\"].split(\"/\")[0],\n                         direction=(\"up-bottom\" if \"Up\" in a[\"description\"] else \"right-left\" if \"Right and Left\" in a[\"description\"] else \"not specified\"),\n                         volts=re.search(r\"pulse at ([\\d,]+)V\", a[\"description\"]).group(1)) for a in assets[\"001273\"]])\nprint(\"001273:\", len(d73), \"files,\", d73.subject.nunique(), \"subjects; field direction in descriptions:\",\n      d73.direction.value_counts().to_dict())\nprint(d73.groupby([\"subject\", \"direction\"]).size().unstack(fill_value=0).to_string())\n\"\"\")\n\ncode(r\"\"\"\npulses = strobe[strobe.subject.isin(cand) & (strobe.kind == \"pulse\")].sort_values(\"start\").groupby(\"subject\").first()\ndef pulse_variant(row):\n    stack = T.load_strobe(row.url)\n    t = T.frame_times_pulse(stack.shape[0])\n    ratio, control = T.ratio_image(stack, t)\n    roi1, roi2, cell = T.rebuilt_rois(ratio, control)\n    f = {k: stack[:, m].mean(1).astype(float) for k, m in ((\"roi1\", roi1), (\"roi2\", roi2))}\n    out = dict(frames=stack.shape[0], volts=row.volts)\n    for k, x in f.items():\n        f0 = x[t < 0].mean()\n        dF = 100 * (x - f0) / f0\n        out[f\"{k} dF 1-2 us\"] = dF[(t >= 1.0) & (t <= 2.0)].mean()\n    out[\"ratio min\"], out[\"ratio max\"] = np.nanmin(np.where(cell, ratio, np.nan)), np.nanmax(np.where(cell, ratio, np.nan))\n    return out\nwith ThreadPoolExecutor(8) as ex:\n    pv = pd.DataFrame(list(ex.map(pulse_variant, [r for _, r in pulses.iterrows()])), index=pulses.index)\nfor k in (\"roi1\", \"roi2\"):\n    pv[f\"{k} %/kV/cm\"] = pv[f\"{k} dF 1-2 us\"].abs() / 0.257\nprint(pv.round(2).to_string())\ns = pd.concat([pv[\"roi1 %/kV/cm\"], pv[\"roi2 %/kV/cm\"]])\nprint(f\"variant only: mean |dF| per kV/cm over the {len(s)} rebuilt ROIs {s.mean():.1f} +- {s.sem():.1f}, range \"\n      f\"{s.min():.1f} to {s.max():.1f} (paper: 28 +- 2.5, range 15 to 47)\")\n\"\"\", \"variant:fig6b-pulse-sensitivity\")\n\nmd(r\"\"\"\n## 15. Summary\n\n| Claim | Outcome |\n|---|---|\n| ... | ... |\n\"\"\")\n\ncode(r\"\"\"\nprint(f\"notebook ran in {(time.time() - t_start) / 60:.1f} min\")\n\"\"\")\n\nnb = nbf.v4.new_notebook()\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nfor kind, src, tags in cells:\n    c = nbf.v4.new_markdown_cell(src) if kind == \"markdown\" else nbf.v4.new_code_cell(src)\n    if tags:\n        c.metadata[\"tags\"] = tags\n    nb.cells.append(c)\nnbf.write(nb, sys.argv[1])\n"
}
```

```
File created successfully at: /tmp/claude-1001/build_nb.py (file state is current in your context — no need to Read it back)
```

**Agent**

Test the analysis cells against the cached records (substituting the load cell), to catch errors before the full streamed run.

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && python - <<'EOF'
s=open("build_nb.py").read()
s=s.replace('pd.DataFrame([dict(dandiset=r["path"] and d, shape=str(r["shape"]), rate=r["rate"]) for d in recs for r in recs[d]])','pd.DataFrame([dict(dandiset=d, shape=str(r["shape"]), rate=r["rate"]) for d in recs for r in recs[d]])')
s=s.replace('''same_meta = sum(a32[k]["description"].replace("1_1", "") is not None and a32[k]["session"] == a34[k]["session"]
                and a32[k]["size"] == a34[k]["size"] for k in set(a32) & set(a34))''','''same_meta = sum(a32[k]["session"] == a34[k]["session"] and a32[k]["size"] == a34[k]["size"]
                for k in set(a32) & set(a34))''')
open("build_nb.py","w").write(s)
EOF
python build_nb.py nb_dev.ipynb && cat > devrun.py <<'EOF'
import nbformat,pickle,sys,os,time
os.chdir("entries/001274-semenov-2025"); sys.path.insert(0,".")
nb=nbformat.read(sys.argv[1],4)
R=pickle.load(open(os.environ["TMPDIR"]+"/recs.pkl","rb"))
for d in R:
    for r in R[d]: r.setdefault("raw_f0",float("nan"))
g={}
skip=set(sys.argv[2].split(",")) if len(sys.argv)>2 else set()
for i,c in enumerate(nb.cells):
    if c.cell_type!="code": continue
    src=c.source
    if "recs[d] = T.load_fast" in src:
        g["recs"]=R; print("[load substituted]"); continue
    if str(i) in skip: print(f"[skip {i}]"); continue
    t=time.time(); print(f"--- cell {i} {c.metadata.get('tags','')}")
    exec(compile(src,f"cell{i}","exec"),g)
    print(f"[{time.time()-t:.0f}s]")
EOF
python devrun.py nb_dev.ipynb 2>&1 | grep -v Warning | head -300
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/build_nb.py", line 1, in <module>
    import nbformat as nbf, sys
ModuleNotFoundError: No module named 'nbformat'
python: can't open file '/tmp/claude-1001/devrun.py': [Errno 2] No such file or directory
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && uv pip install -q nbformat nbclient ipykernel 2>&1|tail -1; python build_nb.py nb_dev.ipynb && cat > devrun.py <<'EOF'
import nbformat,pickle,sys,os,time
os.chdir("entries/001274-semenov-2025"); sys.path.insert(0,".")
nb=nbformat.read(sys.argv[1],4)
R=pickle.load(open(os.environ["TMPDIR"]+"/recs.pkl","rb"))
for d in R:
    for r in R[d]: r.setdefault("raw_f0",float("nan"))
g={}
skip=set(sys.argv[2].split(",")) if len(sys.argv)>2 else set()
for i,c in enumerate(nb.cells):
    if c.cell_type!="code": continue
    src=c.source
    if "recs[d] = T.load_fast" in src:
        g["recs"]=R; print("[load substituted]"); continue
    if str(i) in skip: print(f"[skip {i}]"); continue
    t=time.time(); print(f"--- cell {i} {c.metadata.get('tags','')}")
    exec(compile(src,f"cell{i}","exec"),g)
    print(f"[{time.time()-t:.0f}s]")
EOF
MPLBACKEND=Agg python devrun.py nb_dev.ipynb 2>&1 | grep -v Warning | head -300
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/work/lib/python3.13/site-packages/nbformat/__init__.py", line 169, in read
    buf = fp.read()
          ^^^^^^^
AttributeError: 'str' object has no attribute 'read'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/tmp/claude-1001/devrun.py", line 3, in <module>
    nb=nbformat.read(sys.argv[1],4)
  File "/tmp/claude-1001/work/lib/python3.13/site-packages/nbformat/__init__.py", line 171, in read
    with open(fp, encoding="utf8") as f:  # noqa: PTH123
         ~~~~^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'nb_dev.ipynb'
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && MPLBACKEND=Agg python devrun.py $TMPDIR/nb_dev.ipynb 2>&1 | grep -v Warning | head -300
```

```
--- cell 1 
{'001274': '0.250805.1401', '001273': '0.250805.1356', '001030': '0.240520.1924', '001032': '0.240527.1432', '001033': '0.240527.1432', '001034': '0.240527.1431', '001035': '0.240527.1432', '001271': '0.250805.1352', '001272': '0.250805.1358'}
[1s]
--- cell 3 
001274 0.250805.1401: 232 assets, 20 subjects, 25.02 GB
001273 0.250805.1356: 181 assets, 13 subjects, 10.63 GB
001030 0.240520.1924: 17 assets, 17 subjects, 0.05 GB
001032 0.240527.1432: 178 assets, 14 subjects, 0.12 GB
001033 0.240527.1432: 193 assets, 10 subjects, 0.13 GB
001034 0.240527.1431: 178 assets, 14 subjects, 0.12 GB
001035 0.240527.1432: 254 assets, 15 subjects, 0.18 GB
001271 0.250805.1352: 287 assets, 20 subjects, 0.20 GB
001272 0.250805.1358: 65 assets, 3 subjects, 0.04 GB
001274 versions 0.250701.1622 and 0.250805.1401 have the same paths and sizes: True (232 and 232 assets)
[33s]
--- cell 4 
G acquisition 
G acquisition/StrobeImaging ImageSeries
D acquisition/StrobeImaging/data (140, 512, 512) uint16 
D acquisition/StrobeImaging/dimension (3,) int32 [140 512 512]
[... 281 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && MPLBACKEND=Agg python devrun.py $TMPDIR/nb_dev.ipynb 3,4,6,8,10 2>&1 | grep -v Warning | sed -n '/cell 45/,$p'
```

```
--- cell 45 ['claim:fig2c-pure-more-aps']
whole/a: 52 pairs in 12 neurons; unmodulated more in 46, modulated more in 1, equal in 5; mean difference 3.61 APs; paired t p = 3.3e-09; by carrier {'20k': '7/8', '2k': '39/44'}
whole/b: 52 pairs in 12 neurons; unmodulated more in 46, modulated more in 1, equal in 5; mean difference 3.70 APs; paired t p = 2.5e-09; by carrier {'20k': '8/8', '2k': '38/44'}
bright/a: 52 pairs in 12 neurons; unmodulated more in 43, modulated more in 2, equal in 7; mean difference 3.52 APs; paired t p = 7.9e-09; by carrier {'20k': '7/8', '2k': '36/44'}
bright/b: 52 pairs in 12 neurons; unmodulated more in 44, modulated more in 2, equal in 6; mean difference 4.02 APs; paired t p = 1.1e-09; by carrier {'20k': '8/8', '2k': '36/44'}
[0s]
--- cell 48 ['claim:fig3c-sustained-firing-2s']
sessions without APs under both readings (uncorrected): [['001030/c7', 2.0]]
   neuron  field  frames  rest_dF  a: all  a: after 250 ms  a: last 250 ms  b: all  b: after 250 ms  b: last 250 ms
001030/c5   36.0    7000      1.7      22               17               0       3                2               0
001030/c5   54.0    6000      3.8      82               75               6      65               58               5
001030/c5   72.0    6000      3.5     106               95               5      19                9               0
001030/c6   36.0    7000      0.0      11               10               2      13               12               3
001030/c6   45.0    7000      1.7      41               38               5      33               29               4
001030/c6   52.2    7000      2.8      72               65               7      41               35               5
001030/c7   36.0    7000      0.0       0                0               0       0                0               0
001030/c7   45.0    7000      1.1      17               16               2      19               18               2
001030/c7   52.2    7000      3.3      73               69        
[... 40 more lines not kept]
```

**Agent**

All analysis cells run on the cached data. Now the entry files, lock, and the first full streamed run.

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && sed -i 's/with ThreadPoolExecutor(16) as ex:\n    heads/X/' build_nb.py && python - <<'EOF'
s=open("/tmp/claude-1001/build_nb.py").read()
s=s.replace("with ThreadPoolExecutor(16) as ex:\n    heads","with ThreadPoolExecutor(32) as ex:\n    heads")
open("/tmp/claude-1001/build_nb.py","w").write(s)
EOF
E=entries/001274-semenov-2025
cat > $E/requirements.in <<'EOF'
h5py
ipykernel
matplotlib
numpy
pandas
remfile
scipy
EOF
cat > $E/entry.yaml <<'EOF'
schema_version: 1
name: 001274-semenov-2025
type: reproduction
title: Excitation and polarization of neurons by high-frequency sine waves (Semenov et al. 2025)
description: Tests the findings of Semenov, Kim, Silkuniene and Pakhomov (2025) on dandiset 001274,
  which holds the strobe images of membrane polarization by pulses and sine waves (Figures 5, 6 and
  S3), and on the other dandisets of the same paper that hold the fast optical recordings of action
  potentials (001030, 001032, 001033, 001035, 001271, 001272). The strobe claims are blocked, as the
  dandisets hold no ROIs; the fast recordings test excitation by 2- and 20-kHz sine waves, thresholds,
  beat locking, the 2-s ramped stimulus and tetrodotoxin.
license: Apache-2.0
notebooks:
- path: reproduce_semenov_2025.ipynb
  title: Reproducing Semenov et al. (2025) from dandiset 001274 and the paper's other dandisets
  runtime_minutes: 20
helpers:
- ti_sine.py
related:
- id: dandi:001274/0.250805.1401
  relation: uses_data
- id: dandi:001273/0.250805.1356
  relation: uses_data
- id: dandi:001030/0.240520.1924
  relation: uses_data
- id: dandi:001032/0.240527.1432
  relation: uses_data
- id: dandi:001033/0.240527.1432
  relation: uses_data
- id: dandi:001034/0.240527.1431
  relation: uses_data
- id: dandi:001035/0.240527.1432
  relation: uses_data
- id: dandi:001271/0.250805.1352
  relation: uses_data
- id: dandi:001272/0.250805.1358
  relation: uses_data
- id: doi:10.1016/j.xcrp.2025.102660
  relation: reproduces
EOF
cd $TMPDIR && . work/bin/activate && python build_nb.py $E/reproduce_semenov_2025.ipynb && cd  && time python tools/entry.py lock entries/001274-semenov-2025 2>&1 | tail -5
```

```
Sun Nov  1 15:52:42 UTC 2026
wrote entries/001274-semenov-2025/requirements.lock.txt

real	0m0.229s
user	0m0.131s
sys	0m0.048s
```

**Agent calls Bash**

```bash
python tools/entry.py check entries/001274-semenov-2025 2>&1 | tail -20
```

```
0 error(s)
```

**Agent calls Bash**

```bash
time python tools/entry.py run entries/001274-semenov-2025 2>&1 | tail -20
```

```
Installed kernelspec registry-001274-semenov-2025 in executed/001274-semenov-2025/.venv/share/jupyter/kernels/registry-001274-semenov-2025
pass  reproduce_semenov_2025.ipynb  (903 s)

real	15m6.369s
user	0m32.275s
sys	0m6.571s
```

**Agent**

The full run passed in 15 minutes. Reading the executed outputs I haven't seen yet (raw F0, the 001273 table, the strobe variant).

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && python - <<'EOF'
import nbformat
nb=nbformat.read("executed/001274-semenov-2025/reproduce_semenov_2025.ipynb",4)
for i,c in enumerate(nb.cells):
    if c.cell_type!="code": continue
    if i in (10,12,14,57,58,60) or 'variant' in str(c.metadata.get('tags')):
        print("---",i,c.metadata.get("tags"))
        for o in c.outputs:
            print(o.get("text","")[:4000] if o.output_type=="stream" else o.output_type)
EOF
```

```
--- 10 None
asset names in common: 116 of 178 and 178
same session name and size: 116

identical arrays and start times: 10 of 10 pairs compared

--- 12 None
001032 178 files in 110 s

001033 193 files in 121 s

001035 254 files in 164 s

001271 287 files in 182 s

001272 65 files in 41 s

001030 17

--- 14 ['sanity']
[... 90 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . work/bin/activate && cat > sinev.py <<'EOF'
import json,sys,time,numpy as np,h5py,remfile
sys.path.insert(0,"entries/001274-semenov-2025"); import ti_sine as T
rows=json.load(open("rows_001274.json")); M={x['path']:x for x in json.load(open("meta_001274.json"))}
sub="sub-7-20240523"
p=[r for r in rows if r['sub']==sub and r['kind']=='pulse'][0]
st=T.load_strobe(M[p['path']]['url']); t=T.frame_times_pulse(st.shape[0])
ratio,control=T.ratio_image(st,t); r1,r2,cell=T.rebuilt_rois(ratio,control)
S=[r for r in rows if r['sub']==sub and r['kind']=='sp100']
tt=time.time()
tr=[T.load_strobe(M[r['path']]['url'],{"roi1":r1,"roi2":r2}) for r in S]
print("load",time.time()-tt,len(S))
np.save("sinev.npy",np.array([[x["roi1"],x["roi2"]] for x in tr]))
EOF
python sinev.py
```

```
Sun Nov  1 16:08:16 UTC 2026
load 28.694578409194946 4
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && python - <<'EOF'
import numpy as np
x=np.load("sinev.npy").astype(float)  # sessions, roi, frames
print(x.shape)
np.set_printoptions(precision=1,suppress=True,linewidth=200)
m=x.mean(0)
for k in range(2):
    f=m[k]; F0=np.r_[f[:25],f[-25:]].mean(); dF=100*(f-F0)/F0
    print("roi",k+1); print(dF[::5][:100])
    sp=np.abs(np.fft.rfft(dF-dF.mean())); fr=np.fft.rfftfreq(500,20e-6); print("peak freq above 500 Hz", fr[fr>500][np.argmax(sp[fr>500])])
EOF
```

```
(4, 2, 500)
roi 1
[-11.4  -0.4  -0.9   0.    1.4  -1.2   0.8   1.9  -0.5   1.5  -1.1  -2.   -0.3  -0.3   1.4   2.6  -1.8   0.8  -1.4  -1.    0.2  -2.5   1.7  -0.4   0.3  -2.9  -2.3  -0.7   0.1   1.1  -0.9  -3.4  -2.6
   1.2  -1.4  -1.   -1.1  -0.7  -1.2   1.   -2.9   0.7  -2.3   2.4   2.    2.7  -1.6   1.1   4.6   1.2   0.8   1.4   2.7   2.5   6.2   0.7   0.2  -1.3   3.3   2.8   2.5   0.3   2.    3.2   3.4   1.6
   1.4   0.5   4.2   2.8  -0.2   0.   -0.1   2.6   2.    1.9   1.    1.7  -0.9   1.    0.2   0.5   1.5   1.8  -4.1   0.2   0.3   1.2  -0.4  -1.5  -2.3  -0.3   1.5  -1.2  -0.    2.3   2.2  -3.1  -1.4
  -1.6]
peak freq above 500 Hz 2000.0
roi 2
[-13.4  -1.7   2.5   0.4   0.6  -0.7   0.3  -0.5   0.8  -0.7   0.9  -0.3  -0.3   0.9  -2.3  -0.8  -1.4  -1.3  -2.2   1.8   2.    1.5  -0.3  -1.5  -1.4   1.6  -0.4  -2.   -1.1  -1.3  -0.2  -0.6  -0.6
   0.8  -1.7  -1.8  -0.5  -3.4  -0.1  -0.5  -1.4  -0.1  -2.2   4.3  -0.5   0.4   2.4   1.4   3.    2.2   0.5   1.6   4.1   2.9   2.5   1.   -0.2   0.2   4.7   3.6   2.2   2.4   0.4   6.3   2.4   0.4
   0.6  -0.6  -0.8   1.9   3.9   1.6   4.   -0.5   1.1  -1.1   3.7   2.1  -0.5   2.    3.3   2.3   2.6  -1.9  -0.2   2.4  -0.9  -2.5  -1.9  -0.8  -0.   -2.4  -0.7   0.7  -1.6   0.2  -0.8  -1.2   1.3
  -1.1]
peak freq above 500 Hz 14600.0
Shell cwd was reset to
```

**Agent**

Frame 0 of the sine stacks is also an artifact, and ROI 1 shows the 2-kHz carrier. Adding a LOESS and the per-cycle regression (claims file O3 reading b) to the helper.

**Agent calls Bash**

```bash
cd entries/001274-semenov-2025 && cat >> ti_sine.py <<'EOF'


# --- sine wave strobe measures (variant only) -----------------------------------------------

SINE_STEP_US = 20.0           # Methods: "with 20-us steps for sine wave stimuli"
CARRIER_HZ = 2000.0
LOESS_SPANS = (0.75, 0.5, 0.25)   # claims file O2: R's loess default span 0.75, and 0.5, 0.25


def loess(y, span=0.75):
    """Local quadratic regression with tricube weights over the nearest span x n points, as R's
    loess(degree = 2, family = "gaussian") computes it at the data points (claims file O2)."""
    n = len(y)
    x = np.arange(n, dtype=float)
    k = int(np.ceil(span * n))
    out = np.empty(n)
    for i in range(n):
        d = np.abs(x - x[i])
        h = np.sort(d)[k - 1]
        w = np.clip(1 - (d / h) ** 3, 0, None) ** 3
        X = np.vstack([np.ones(n), x - x[i], (x - x[i]) ** 2]).T
        sw = np.sqrt(w)
        beta = np.linalg.lstsq(X * sw[:, None], y * sw, rcond=None)[0]
        out[i] = beta[0]
    return out


def sine_dF(trace):
    """dF (%) of a sine wave stack trace: F0 is the mean of the first and the last carrier
    cycle (Methods), leaving out frame 0, a bright artifact as in the fast recordings."""
    per = int(round(1e6 / CARRIER_HZ / SINE_STEP_US))
    f = np.asarray(trace, float)
    f0 = np.r_[f[1:1 + per], f[-per:]].mean()
    return 100 * (f - f0) / f0


def cycle_regression(sub, peak_field, intercept=True):
    """Claims file O3 reading (b): per carrier cycle, half the peak-to-peak of the LOESS-subtracted
    dF against the peak field of that cycle, for a single beat whose envelope rises from zero to
    `peak_field` and back as a half sine (an assumption: the files hold no waveform). Returns
    slope (% per V/cm), its p-value and the number of cycles."""
    from scipy import stats
    per = int(round(1e6 / CARRIER_HZ / SINE_STEP_US))
    n = (len(sub) - 1) // per
    amp, fld = [], []
    for c in range(n):
        seg = sub[1 + c * per:1 + (c + 1) * per]
        amp.append((seg.max() - seg.min()) / 2)
        tc = (c + 0.5) / n
        fld.append(peak_field * np.sin(np.pi * tc))
    amp, fld = np.array(amp), np.array(fld)
    if intercept:
        r = stats.linregress(fld, amp)
        return r.slope, r.pvalue, n
    slope = (fld @ amp) / (fld @ fld)
    resid = amp - slope * fld
    se = np.sqrt(resid @ resid / (n - 1) / (fld @ fld))
    p = 2 * stats.t.sf(abs(slope / se), n - 1)
    return slope, p, n
EOF
cd $TMPDIR && . work/bin/activate && python - <<'EOF'
import sys,numpy as np,time
sys.path.insert(0,"entries/001274-semenov-2025"); import ti_sine as T
x=np.load("sinev.npy").astype(float).mean(0)
for k in range(2):
    d=T.sine_dF(x[k])
    for sp in T.LOESS_SPANS:
        t=time.time(); L=T.loess(d,sp); sub=d-L
        for ic in (True,False):
            s,p,n=T.cycle_regression(sub,136.0,ic)
            print(k+1,sp,ic,"%.1f %%/kV/cm p=%.2g n=%d"%(s*1000,p,n),"%.1fs"%(time.time()-t))
EOF
```

```
1 0.75 True 1.2 %/kV/cm p=0.81 n=19 0.0s
1 0.75 False 35.7 %/kV/cm p=2.3e-07 n=19 0.0s
1 0.5 True 0.7 %/kV/cm p=0.88 n=19 0.0s
1 0.5 False 35.7 %/kV/cm p=2.6e-07 n=19 0.0s
1 0.25 True 0.6 %/kV/cm p=0.91 n=19 0.0s
1 0.25 False 35.7 %/kV/cm p=2.8e-07 n=19 0.0s
2 0.75 True -7.0 %/kV/cm p=0.35 n=19 0.0s
2 0.75 False 30.3 %/kV/cm p=1.8e-05 n=19 0.0s
2 0.5 True -7.1 %/kV/cm p=0.35 n=19 0.0s
2 0.5 False 30.2 %/kV/cm p=1.9e-05 n=19 0.0s
2 0.25 True -6.5 %/kV/cm p=0.39 n=19 0.0s
2 0.25 False 29.9 %/kV/cm p=1.7e-05 n=19 0.0s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/001274-semenov-2025 && cat >> ti_sine.py <<'EOF'


def signed_field(n, peak_field, phase):
    """Instantaneous field (V/cm) of a single 2-kHz beat over n frames at 20-us steps: a half-sine
    envelope peaking at `peak_field` times the carrier at the given phase (assumption: the files
    hold no waveform; frame 0 is taken as the start of the beat)."""
    t = np.arange(n) * SINE_STEP_US * 1e-6
    T_beat = n * SINE_STEP_US * 1e-6
    return peak_field * np.sin(np.pi * t / T_beat) * np.sin(2 * np.pi * CARRIER_HZ * t + phase)


def fit_phase(sub, peak_field):
    """Carrier phase that best fits a LOESS-subtracted trace (least squares on the sine and cosine
    components under the envelope); frame 0 is left out."""
    n = len(sub)
    a = signed_field(n, 1.0, 0.0)[1:]
    b = signed_field(n, 1.0, np.pi / 2)[1:]
    coef = np.linalg.lstsq(np.vstack([a, b]).T, sub[1:], rcond=None)[0]
    return float(np.arctan2(coef[1], coef[0]))


def frame_regression(sub, fld):
    """Claims file O3 reading (a): dF after LOESS subtraction on the signed field, frame by frame
    (frame 0 left out). Returns slope (% per V/cm), its standard error and p-value."""
    from scipy import stats
    r = stats.linregress(fld[1:], sub[1:])
    return r.slope, r.stderr, r.pvalue
EOF
cd $TMPDIR && . work/bin/activate && python - <<'EOF'
import sys,numpy as np
sys.path.insert(0,"entries/001274-semenov-2025"); import ti_sine as T
x=np.load("sinev.npy").astype(float).mean(0)
d=[T.sine_dF(x[k]) for k in range(2)]
for sp in T.LOESS_SPANS:
    sub=[dd-T.loess(dd,sp) for dd in d]
    ph=fit_phase=T.fit_phase(sub[0],136.)
    f=T.signed_field(500,136.,ph)
    res=[T.frame_regression(s,f) for s in sub]
    print(sp,"phase %.2f"%ph, ["%.1f +- %.1f %%/kV/cm p=%.1g"%(r[0]*1000,r[1]*1000,r[2]) for r in res], "corr r1 r2 %.2f"%np.corrcoef(sub[0][1:],sub[1][1:])[0,1])
EOF
```

```
0.75 phase -2.89 ['12.9 +- 1.1 %/kV/cm p=9e-28', '0.2 +- 1.1 %/kV/cm p=0.8'] corr r1 r2 0.21
0.5 phase -2.89 ['12.9 +- 1.1 %/kV/cm p=8e-29', '0.2 +- 1.1 %/kV/cm p=0.8'] corr r1 r2 0.19
0.25 phase -2.89 ['12.9 +- 1.1 %/kV/cm p=4e-29', '0.2 +- 1.1 %/kV/cm p=0.8'] corr r1 r2 0.18
Shell cwd was reset to
```

**Agent**

The variant works (ROI 1 12.9 ± 1.1 %/kV/cm, ROI 2 near zero in this subject). Adding it to the notebook and testing it standalone.

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && python - <<'EOF'
s=open("build_nb.py").read()
anchor='''md(r"""
## 15. Summary'''
new='''md(r"""
The same rebuilt ROIs on the 100-Hz sine wave sessions of these subjects (Figure 6C), averaged over sessions,
LOESS-subtracted at each span of the claims file's O2, and regressed frame by frame on the signed field (O3
reading a). The files hold neither the waveform nor the field, so the peak field is taken as the paper's 136
V/cm (Figure 5 legend) and the carrier phase is fitted to ROI 1; the sign of ROI 2 then says whether it
oscillates in antiphase. Reading (b) of O3 (half the peak-to-peak per cycle) is dominated by the noise of
single frames and is not shown. A variant only.
""")

code(r"""
def sine_variant(subject):
    row = pulses.loc[subject]
    stack = T.load_strobe(row.url)
    t = T.frame_times_pulse(stack.shape[0])
    ratio, control = T.ratio_image(stack, t)
    roi1, roi2, _ = T.rebuilt_rois(ratio, control)
    files = strobe[(strobe.subject == subject) & (strobe.kind == "sine 100 Hz")]
    tr = [T.load_strobe(u, {"roi1": roi1, "roi2": roi2}) for u in files.url]
    out = []
    mean = {k: np.mean([x[k] for x in tr], axis=0) for k in ("roi1", "roi2")}
    dF = {k: T.sine_dF(v) for k, v in mean.items()}
    for span in T.LOESS_SPANS:
        sub = {k: v - T.loess(v, span) for k, v in dF.items()}
        phase = T.fit_phase(sub["roi1"], 136.0)
        fld = T.signed_field(len(sub["roi1"]), 136.0, phase)
        for k in ("roi1", "roi2"):
            slope, se, p = T.frame_regression(sub[k], fld)
            out.append(dict(subject=subject, span=span, roi=k, sessions=len(tr), slope=1000 * slope,
                            se=1000 * se, p=p))
    return out
with ThreadPoolExecutor(9) as ex:
    sv = pd.DataFrame([r for rows in ex.map(sine_variant, cand) for r in rows])
sv["sens"] = sv.slope.abs()
print(sv[sv.span == 0.75].round(4).to_string(index=False))
for span, g in sv.groupby("span"):
    pul = pd.concat([pv["roi1 %/kV/cm"].rename("roi1"), pv["roi2 %/kV/cm"].rename("roi2")], axis=1).stack()
    sens = g.set_index(["subject", "roi"]).sens
    ratio = (sens / pul.reindex(sens.index)).dropna()
    print(f"span {span}: mean sine sensitivity {sens.mean():.1f} +- {sens.sem():.1f} %/kV/cm (range {sens.min():.1f} to "
          f"{sens.max():.1f}); p < 0.0001 in {int((g.p < 1e-4).sum())} of {len(g)} ROIs; ROI 2 slope negative in "
          f"{int((g[g.roi == 'roi2'].slope < 0).sum())} of {g.subject.nunique()}; sine below pulse in {int((ratio < 1).sum())} of "
          f"{len(ratio)} ROIs; mean sine over mean pulse {sens.mean() / pul.mean():.2f}")
""", "variant:fig6c-sine-sensitivity")

''' + anchor
s=s.replace(anchor,new,1)
open("build_nb.py","w").write(s)
EOF
python build_nb.py nb_dev.ipynb && python - <<'EOF'
# run only the cells needed for the strobe variants: imports, assets, strobe table, cand, pulse variant, sine variant
import nbformat,os,sys,time
os.chdir("entries/001274-semenov-2025"); sys.path.insert(0,".")
nb=nbformat.read(os.environ["TMPDIR"]+"/nb_dev.ipynb",4)
g={}
code=[c for c in nb.cells if c.cell_type=="code"]
want=[0,1,3,4]  # imports, assets, strobe table, cand
for i in want:
    exec(code[i].source,g)
for c in code:
    if "variant:" in str(c.metadata.get("tags")):
        t=time.time(); exec(c.source,g); print(f"[{time.time()-t:.0f}s]")
EOF
```

```
{'001274': '0.250805.1401', '001273': '0.250805.1356', '001030': '0.240520.1924', '001032': '0.240527.1432', '001033': '0.240527.1432', '001034': '0.240527.1431', '001035': '0.240527.1432', '001271': '0.250805.1352', '001272': '0.250805.1358'}
001274 0.250805.1401: 232 assets, 20 subjects, 25.02 GB
001273 0.250805.1356: 181 assets, 13 subjects, 10.63 GB
001030 0.240520.1924: 17 assets, 17 subjects, 0.05 GB
001032 0.240527.1432: 178 assets, 14 subjects, 0.12 GB
001033 0.240527.1432: 193 assets, 10 subjects, 0.13 GB
001034 0.240527.1431: 178 assets, 14 subjects, 0.12 GB
001035 0.240527.1432: 254 assets, 15 subjects, 0.18 GB
001271 0.250805.1352: 287 assets, 20 subjects, 0.20 GB
001272 0.250805.1358: 65 assets, 3 subjects, 0.04 GB
001274 versions 0.250701.1622 and 0.250805.1401 have the same paths and sizes: True (232 and 232 assets)
subject         kind         volts  solution  frames
sub-1-20240522  pulse        10.0   vehicle   140       2
                sine         10.0   vehicle   300       1
sub-1-20240523  pulse        10.0   vehicle   140       1
sub-1-20240824  pulse        10.0   TTX       160       8
                                    vehicle   160       8
                sine 154 Hz  7.0    TTX       325       8
                                    vehicle   325       8
sub-2-20240522  pulse        10.0   vehicle   140       2
[... 83 more lines not kept]
```

**Agent**

The sine variant adds 6 minutes (notebook about 22 minutes in all). Now the schema for the attempt record, then the conclusions.

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s,indent=1)[:9000])"
```

```
{
 "$schema": "https://json-schema.org/draft/2020-12/schema",
 "title": "One attempt at reproducing the claims of a target",
 "description": "Draft. To be revised after the pilot. An attempt is recorded whether or not it produced a working notebook.",
 "type": "object",
 "additionalProperties": false,
 "required": [
  "schema_version",
  "id",
  "dataset",
  "paper",
  "date",
  "provenance",
  "outcomes"
 ],
 "properties": {
  "schema_version": {
   "const": 2
  },
  "id": {
[... 357 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/attempt.schema.json'));p=s['properties'];print(json.dumps({k:p[k] for k in ['inputs','findings']},indent=1)[:5000])"; sed -n 50,140p attempts/001453-fouke-2025-01.yaml
```

```
{
 "inputs": {
  "description": "Everything the attempt used that is not in the dataset.",
  "type": "array",
  "items": {
   "type": "object",
   "additionalProperties": false,
   "required": [
    "what",
    "source"
   ],
   "properties": {
    "what": {
     "type": "string",
     "minLength": 1
    },
    "source": {
     "description": "A DOI, or a repository URL with the commit read.",
     "type": "string",
     "minLength": 1
[... 134 more lines not kept]
```

**Agent**

Now writing the conclusions into the notebook builder, in order of the placeholders.

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && cat > concl.py <<'PYEOF'
s=open("build_nb.py").read()
R=[
# fig1 excites all
"""**Result: partially reproduced.** At 2 kHz, 27 of 28 neurons (96%) fired at least one AP under both AP
readings, and at 20 kHz 15 of 17 (88%), below the 90% the criterion asks; the bright-pixel trace gives the
same counts except 28 of 28 at 2 kHz under reading (b). The two neurons never excited at 20 kHz were tested
up to 288 and 324 V/cm and fired in other sessions, so the Methods' selection of neurons with APs does not
remove them. Whether firing was ever an on-off response is not tested by the criterion.""",
# onset
"""**Result: partially reproduced.** The median first-AP latency of the near-threshold sessions is 64 ms
(reading a) and 67 ms (reading b), below the 90 to 220 ms the criterion asks; it is 54 ms at 2 kHz and 124 ms
(a) or 101 ms (b) at 20 kHz. Restricting to thresholds with a lower-field session without APs gives 67 ms. The
second part holds: the latency falls with field in 38 of 38 (a) and 39 of 39 (b) neuron-carrier pairs.""",
# ceiling
"""**Result: reproduced, resting on an assumption.** The readings disagree: the median ceiling is 59.9 Hz
under reading (a), within 54 to 99 Hz, and 42.9 Hz under reading (b), outside it (the bright-pixel trace gives
62.4 and 61.7 Hz). Reading (a) is adopted: the Methods select APs that "peaked at a more than 5% dF", which is
reading (a), and reading (b) misses an AP that starts on the falling phase of the one before, which is the
case that sets the maximum rate. The rate rises with field before the ceiling in 31 of 31 neuron-carrier
pairs (median slope 0.64 Hz per V/cm).""",
# block
"""**Result: not reproduced.** The highest-field session has a mean last-100-ms dF above 5% and above the
near-threshold session in 3 of 42 neuron-carrier pairs under both readings (3 of 43 with the bright trace),
far from more than half; the second-half variant also gives 3. The highest field tested was a median 1.36
times the near-threshold field, and 11 of 370 unmodulated sessions have a last-100-ms dF above 5%.""",
# twofold
"""**Result: partially reproduced.** Every 20-kHz threshold is higher than the 2-kHz one with p below 0.0001
(per group from 1e-05 to 2e-12, pooled 1e-24), but the ratios are 2.27, 2.62, 2.34 and 2.49 (reading a) and
2.29, 2.63, 2.28 and 2.82 (reading b), all above the 1.8 to 2.2 of the criterion. The ratio does not depend on
the field reading. The modulated 20-kHz groups have 2 or 3 neurons. The voltages are the generator's,
uncalibrated for frequency, which the descriptions say makes the true amplitude "somewhat smaller".""",
# mod higher
"""**Result: partially reproduced.** The modulated mean is higher in all three pairs under both readings.
Under reading (a) only the 20-kHz 1-AP pair reaches p < 0.05 (p = 0.021; 2 kHz 5 APs p = 0.082, 20 kHz 5
APs p = 0.082); under reading (b) two do (20 kHz 1 AP p = 0.021, 20 kHz 5 APs p = 0.012; 2 kHz 5 APs p =
0.155). Both give one or two of three. The 2-kHz 1-AP pair, for which the paper reports no difference, gives
p = 0.059 (a) and 0.045 (b) unpaired, and p = 0.0001 paired on 12 neurons.""",
# threshold
"""**Result: not reproduced.** The mean 1-AP threshold for unmodulated 2-kHz sine waves is 75.6 +- 6.2 V/cm
(n = 27, reading a) and 74.8 +- 5.9 (reading b) with the field as 36 V/cm times half the peak-to-peak
voltage, and 151.2 and 149.6 V/cm with the whole of it; none is within 57.7 +- 3.6. By dandiset it is 92.2
(001032), 76.6 (001033) and 58.3 V/cm (001035).""",
# locks
"""**Result: partially reproduced.** Firing locks to the beats: of the APs in modulated sessions with 5 APs or
more, 0.87 (reading a) and 0.98 (reading b) fall in the middle half of a beat, and 0.10 and 0.04 do when
the beats are shifted by 25 ms. But under reading (a) 2 sessions have more than 10 APs (12 and 11), and under
both readings one session (001032/sub-2-1, 198 V/cm) ends with a last-100-ms dF of 5.9%, so (i) fails under
(a) and (iii) under both.""",
# fig2c
"""**Result: reproduced.** In 52 pairs of sessions from 12 neurons at the same carrier and field, the
unmodulated sine wave gave more APs in 46 and fewer in 1 (5 equal), a mean of 3.61 more APs (reading a,
paired t p = 3.3e-09; reading b 46 and 1, p = 2.5e-09).""",
# fig3c
"""**Result: partially reproduced.** In neuron c7, (i) APs occur in the last 250 ms at 52, 61 and 72 V/cm (8
to 15 under reading a, 8 to 10 under b), and (ii) the AP count rises from 0 at 36 V/cm to 116 (a) or 90 (b)
before falling at the highest field. At the highest field, 83 V/cm, the mean dF over 0.25 to 2 s is 6.7%,
above 5%, and under reading (b) the APs stop at 0.21 s, within the ramp, with one more at 1.68 s, about the
number reading (b) finds by chance in 1.75 s (0.16 per 250 ms before stimuli). Reading (a) counts 131 peaks
after 250 ms on the depolarized plateau. So (iii) does not hold as written under either reading: "no APs"
fails by one event under (b). The other three neurons have no AP-free trace of their own and none reaches a
block.""",
# s1
"""**Result: not reproduced.** 001272 holds 3 neurons, where the paper used eight. The readings disagree on
excitation (3 of 3 neurons under reading a and both 5-SD readings, 1 of 3 under reading b at 5%), but under
every reading no neuron meets the block test at its highest field (0 of 3; inverted last-100-ms dF 0.7%,
3.3% and 1.6%), so the claim fails under all readings. Latency falls with field in 1 of 2 neurons with
three fields with APs under reading (a), and in 2 of 3 under the 5-SD readings.""",
# s2
"""**Result: partially reproduced.** In all 6 neurons recorded in tetrodotoxin, APs present in normal
solution at the same field are absent in tetrodotoxin under reading (a) (5 of 6 under reading b, which finds
rises of 5% in 15 of 17 tetrodotoxin sessions of one neuron where reading a finds none). The last-100-ms dF
in tetrodotoxin is at most 0.4% in every session. But only 1 of the 6 neurons had a last-100-ms dF above 5%
before tetrodotoxin (5.4%), and none of 171 sessions of the 14 neurons never put in tetrodotoxin did, so the
block of sustained depolarization is shown in one neuron and the criterion, which asks it of every neuron,
fails.""",
]
for r in R:
    assert "**Result: ...**" in s
    s=s.replace("**Result: ...**",r,1)
assert "**Result: ...**" not in s
summary='''## 15. Summary

| Claim | Outcome |
|---|---|
| fig1-pure-sine-excites-all | partially reproduced (2 kHz 96%, 20 kHz 88% of neurons) |
| fig1-onset-delay | partially reproduced (latency falls with field; median 64 ms, not 100 to 200) |
| fig1-max-rate-ceiling | reproduced, resting on an assumption (59.9 Hz; reading b 42.9 Hz) |
| fig1-excitation-block | not reproduced (3 of 42) |
| fig2d-20khz-twofold-threshold | partially reproduced (p < 0.0001, ratios 2.27 to 2.82) |
| fig2d-modulated-thresholds-higher | partially reproduced (1 or 2 of 3 pairs) |
| threshold-2khz-unmodulated | not reproduced (75.6 V/cm against 57.7) |
| fig2-modulated-locks-to-beats | partially reproduced |
| fig2c-pure-more-aps | reproduced |
| fig3b-low-conductivity-halves-threshold | blocked: metadata insufficient |
| fig3c-sustained-firing-2s | partially reproduced |
| figs1-di8-anepps-control | not reproduced (3 of 8 neurons deposited) |
| figs2-ttx-blocks-depolarization | partially reproduced |
| fig4 (four claims) | blocked: metadata insufficient |
| fig5, figs3, fig6 (eight claims) | blocked: metadata insufficient |
| threshold-depolarization-estimate | blocked: metadata insufficient |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the
differences from the paper's method.

**How the analysis differs from the paper's.** The soma ROI is the whole 16 x 16 frame (assumption; the
bright half is a variant), APs are detected by the two readings of the claims file with an 8-ms merge, and the
field is 36 V/cm times half the generator's peak-to-peak voltage (assumption; the whole of it is a
variant), with no frequency calibration. Neurons from 001032, 001033 and 001035 are pooled, as the paper
does not say which neurons form which figure.

**What was found about the dandisets.** 001274 and 001273 hold raw strobe stacks only: no ROIs, no field
values, no frame times, no cell shapes or groups, and no identifier for the paper's cells C1 to C9.
001034 is a second deposit of 001032. No 250-ms session is labelled as sodium gluconate, so Figure 3B cannot
be found. 001272 holds 3 of the 8 Di-8-ANEPPS neurons. The descriptions say tetrodotoxin "caused sustained
depolarization", where the paper and the data show none in tetrodotoxin. The voltages are uncalibrated, with
calibration factors "to be reported separately". The images are 16 x 16 pixels where the paper gives 64 x 64,
and the first frame of every recording is an artifact. 001030 makes one subject per session.'''
s=s.replace('''## 15. Summary

| Claim | Outcome |
|---|---|
| ... | ... |''',summary)
# blocked section results for variants
s=s.replace('''md(r"""
## 15. Summary''','''md(r"""
The rebuilt ROIs give a pulse value of 20.6 +- 2.7 %/kV/cm over 18 ROIs and a sine value of about 5.5 +- 0.8,
26% of the pulse value, below it in 17 of 18 ROIs, with ROI 2 in antiphase in 7 of 9 subjects. These are
variants on ROIs and a field the paper does not give, and decide no outcome.
""")

md(r"""
## 15. Summary''')
open("build_nb.py","w").write(s)
PYEOF
python concl.py && python build_nb.py entries/001274-semenov-2025/reproduce_semenov_2025.ipynb && date -u
```

```
Sun Nov  1 16:21:04 UTC 2026
Shell cwd was reset to
```

**Agent**

A few conclusion sentences don't quite match the printed numbers (p range, the bright-trace counts, the Figure 3C count under reading a). Fixing them.

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && python - <<'EOF'
s=open("build_nb.py").read()
rep=[("""near-threshold session in 3 of 42 neuron-carrier pairs under both readings (3 of 43 with the bright trace),""",
"""near-threshold session in 3 of 42 neuron-carrier pairs under both readings (3 of 42 and 3 of 43 with the
bright trace),"""),
("""with p below 0.0001
(per group from 1e-05 to 2e-12, pooled 1e-24)""","""with p below 0.0001
(per group at most 4e-05, pooled 1e-24)"""),
("""and (ii) the AP count rises from 0 at 36 V/cm to 116 (a) or 90 (b)
before falling at the highest field.""","""and (ii) the AP count rises with field: from 0 at 36 V/cm to 142 at
83 V/cm under reading (a), and to 90 at 61 V/cm under reading (b), which then falls to 80 and 8."""),
]
for a,b in rep:
    assert a in s,a[:40]; s=s.replace(a,b)
open("build_nb.py","w").write(s)
EOF
python build_nb.py entries/001274-semenov-2025/reproduce_semenov_2025.ipynb && cd  && python tools/entry.py lock entries/001274-semenov-2025 | tail -1 && python tools/entry.py check entries/001274-semenov-2025 | tail -3
```

```
wrote entries/001274-semenov-2025/requirements.lock.txt
0 error(s)
```

**Agent**

Writing the attempt record and README before the final full run.

**Agent calls Write**

```json
{
 "file_path": "attempts/001274-semenov-2025-01.yaml",
 "content": "schema_version: 2\nid: 001274-semenov-2025-01\ndataset:\n  archive: dandi\n  id: \"001274\"\n  version: 0.250805.1401\n  doi: 10.48324/dandi.001274/0.250805.1401\npaper: doi:10.1016/j.xcrp.2025.102660\ndate: 2026-11-01\nentry: 001274-semenov-2025\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-13\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/41320327294\ninputs:\n- what: Fast optical recordings of the paper's Figures 1 and 2 (2- and 20-kHz sine waves, modulated\n    at 20 Hz or not), DANDI:001032, streamed.\n  source: doi:10.48324/dandi.001032/0.240527.1432\n- what: Fast optical recordings of the paper's Figures 1 and 2, DANDI:001033, streamed.\n  source: doi:10.48324/dandi.001033/0.240527.1432\n- what: Fast optical recordings of the paper's Figures 1 and 2, DANDI:001035, streamed.\n  source: doi:10.48324/dandi.001035/0.240527.1432\n- what: DANDI:001034, compared with 001032 and found to be a second deposit of it; not analysed.\n  source: doi:10.48324/dandi.001034/0.240527.1431\n- what: 2-s ramped 2-kHz sine waves in sodium gluconate (Figure 3C), DANDI:001030, streamed.\n  source: doi:10.48324/dandi.001030/0.240520.1924\n- what: Tetrodotoxin recordings (Figure S2), DANDI:001271, streamed.\n  source: doi:10.48324/dandi.001271/0.250805.1352\n- what: Di-8-ANEPPS recordings (Figure S1), DANDI:001272, streamed.\n  source: doi:10.48324/dandi.001272/0.250805.1358\n- what: Asset list and session descriptions of the 2-us pulse kinetics recordings (Figure 4),\n    DANDI:001273; no images analysed.\n  source: doi:10.48324/dandi.001273/0.250805.1356\noutcomes:\n- claim: fig1-pure-sine-excites-all\n  outcome: partially_reproduced\n  notebook: reproduce_semenov_2025.ipynb\n  output: claim:fig1-pure-sine-excites-all\n  measured: 88\n  notes: At 2 kHz 27 of 28 neurons (96%) fired at least one AP under both AP readings, at 20 kHz 15\n    of 17 (88%), below the criterion's 90% (measured gives the 20-kHz value, the lower of the two).\n    The bright-pixel trace gives the same, except 28 of 28 at 2 kHz under reading (b). The two\n    neurons not excited at 20 kHz (001033/sub-7-2, 001035/sub-10-4) were tested up to 288 and 324\n    V/cm and fired in other sessions (26 and 11 APs), so the Methods' selection of neurons with APs\n    does not remove them. The statement's \"never as an on-off response\" is not tested by the\n    criterion. Neurons are pooled over 001032, 001033 and 001035 (28 at 2 kHz, 17 at 20 kHz).\n  deviations:\n  - The paper does not say which neurons or dandisets form Figure 1; all neurons tested with\n    unmodulated 2- or 20-kHz sine waves in 001032, 001033 and 001035 are pooled.\n  - F is the mean of the whole 16 x 16 frame (assumption; Methods, \"The emission intensity over the\n    entire cell soma (F)\", but the files have no soma outline). It gives first APs of median 11.4%\n    dF against the Methods' typical 11.3%. The brighter half of the frame is run as a variant and\n    gives the same outcome.\n  - AP peaks closer than 8 ms are merged, the AP duration of the Methods (\"8 +- 0.7 ms duration\");\n    reading (a) also asks a prominence of 2.5% dF, a standard choice. The first frame of every\n    recording, a camera artifact, is left out of F0.\n- claim: fig1-onset-delay\n  outcome: partially_reproduced\n  notebook: reproduce_semenov_2025.ipynb\n  output: claim:fig1-onset-delay\n  notes: The median first-AP latency of the near-threshold sessions is 64 ms (reading a, IQR 41 to\n    128, n = 42 neuron-carrier pairs) and 67 ms (reading b), below 90 to 220 ms. By carrier it is\n    54 ms at 2 kHz (n = 27) and 124 ms (a) or 101 ms (b) at 20 kHz (n = 15). With only thresholds\n    that have a lower-field session without APs it is 67 ms (n = 27). The second part holds; the\n    latency falls with field (Spearman rho below 0) in 38 of 38 (a) and 39 of 39 (b) pairs with\n    three or more fields with APs. The bright-pixel trace gives 67 and 54 ms. The latency does not\n    depend on the field reading.\n  deviations:\n  - Neuron-carrier pairs are the units for both parts (the criterion says per neuron and\n    frequency); sessions repeated at one field are averaged, a standard choice.\n  - Soma ROI and AP detection as in fig1-pure-sine-excites-all.\n- claim: fig1-max-rate-ceiling\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_semenov_2025.ipynb\n  output: claim:fig1-max-rate-ceiling\n  measured: 59.9\n  notes: The median ceiling over 30 neurons is 59.9 Hz under AP reading (a) (IQR 31.7 to 83.4, range\n    16.1 to 110.2), within 54 to 99 Hz, and 42.9 Hz under reading (b), outside it; the bright-pixel\n    trace gives 62.4 (a) and 61.7 (b). The rate rises with field before the ceiling in 31 of 31\n    neuron-carrier pairs with three fields or more (median slope 0.64 Hz per V/cm). Two neurons\n    never fired two APs in one unmodulated session and have no rate.\n  deviations:\n  - Assumption. The AP readings disagree; reading (a) is adopted. The Methods select neurons whose\n    \"APs peaked at a more than 5% dF\", which is reading (a); reading (b), a rise of 5% within 5 ms,\n    misses an AP that starts on the falling phase of the one before, the case that sets the maximum\n    rate. Both readings are shown.\n  - The detection cannot see rates above 125 Hz (8-ms merge, Methods' AP duration).\n- claim: fig1-excitation-block\n  outcome: not_reproduced\n  notebook: reproduce_semenov_2025.ipynb\n  output: claim:fig1-excitation-block\n  notes: The highest-field unmodulated session has a last-100-ms mean dF above 5% and above the\n    near-threshold session in 3 of 42 neuron-carrier pairs under both AP readings (3 of 42 and 3 of\n    43 with the bright-pixel trace), against more than half. The second-half variant also gives 3.\n    The highest-field last-100-ms dF has a median of 1.3% (range -0.7 to 9.8). The highest field\n    tested was a median 1.36 times the near-threshold field, and 11 of 370 unmodulated sessions have\n    a last-100-ms dF above 5%, so most neurons may not have been driven far enough above threshold\n    in the deposited sessions.\n  deviations:\n  - Soma ROI as in fig1-pure-sine-excites-all. Sessions repeated at one field are averaged.\n- claim: fig2d-20khz-twofold-threshold\n  outcome: partially_reproduced\n  notebook: reproduce_semenov_2025.ipynb\n  output: claim:fig2d-20khz-twofold-threshold\n  measured:\n  - 2.27\n  - 2.62\n  - 2.34\n  - 2.49\n  notes: Every 20-kHz threshold group is higher than the 2-kHz one with p below 0.0001 under both\n    test readings (per group at most 4e-05, pooled 1e-24), but the ratios of mean thresholds (1 AP\n    unmodulated, 1 AP modulated, 5 APs unmodulated, 5 APs modulated) are 2.27, 2.62, 2.34 and 2.49\n    under AP reading (a) and 2.29, 2.63, 2.28 and 2.82 under (b), all above 1.8 to 2.2. The\n    modulated 20-kHz groups have 2 or 3 neurons (all in 001033). The ratio does not depend on the\n    field reading. The descriptions say the generator voltages are not the measured amplitude,\n    with frequency-dependent calibration factors to be reported separately; a smaller true\n    amplitude at 20 kHz would lower the ratio.\n  deviations:\n  - Neurons of 001032, 001033 and 001035 pooled; the paper does not say which form Figure 2D.\n  - The field per session is 36 V/cm times half the generator's peak-to-peak voltage, from the\n    session descriptions, without frequency calibration (not in the dandisets).\n- claim: fig2d-modulated-thresholds-higher\n  outcome: partially_reproduced\n  notebook: reproduce_semenov_2025.ipynb\n  output: claim:fig2d-modulated-thresholds-higher\n  notes: The modulated mean is higher in all three pairs under both readings. Under reading (a) one\n    pair reaches p < 0.05 (20 kHz 1 AP, p = 0.021; 2 kHz 5 APs p = 0.082; 20 kHz 5 APs p = 0.082);\n    under reading (b) two do (20 kHz 1 AP p = 0.021, 20 kHz 5 APs p = 0.012; 2 kHz 5 APs p =\n    0.155). The 20-kHz modulated groups have 3 neurons (2 for 5 APs under b). The 2-kHz 1-AP pair,\n    for which the paper reports no difference, gives unpaired p = 0.059 (a) and 0.045 (b), and\n    paired p = 0.0001 on 12 neurons. Paired tests on the three pairs give p from 0.095 to 0.29.\n  deviations:\n  - As in fig2d-20khz-twofold-threshold.\n- claim: threshold-2khz-unmodulated\n  outcome: not_reproduced\n  notebook: reproduce_semenov_2025.ipynb\n  output: claim:threshold-2khz-unmodulated\n  measured: 75.6\n  notes: The mean 1-AP threshold for unmodulated 2-kHz sine waves is 75.6 +- 6.2 V/cm (n = 27,\n    reading a) and 74.8 +- 5.9 (reading b) with the field as 36 V/cm times half the peak-to-peak\n    voltage, and 151.2 and 149.6 V/cm with the whole of it; none is within 57.7 +- 3.6. By\n    dandiset it is 92.2 (001032, n = 10), 76.6 (001033, n = 7) and 58.3 V/cm (001035, n = 10).\n    With only thresholds bracketed by a lower-field session without APs, 88.0 V/cm (n = 16).\n  deviations:\n  - The field conversion is the dandisets' (36 V/cm per volt) with two readings of the voltage;\n    both give the same outcome. The uncalibrated generator voltage may be above the true one.\n- claim: fig2-modulated-locks-to-beats\n  outcome: partially_reproduced\n  notebook: reproduce_semenov_2025.ipynb\n  output: claim:fig2-modulated-locks-to-beats\n  notes: Firing locks to the beats; of the APs in the 28 (a) or 22 (b) modulated sessions with 5 APs\n    or more, 0.87 and 0.98 fall 12.5 to 37.5 ms into a beat, and over all modulated sessions 0.90\n    and 0.96 do, against 0.10 and 0.04 with the beats shifted by 25 ms. Part (i) fails under reading\n    (a), with 2 of 84 sessions above 10 APs (12 and 11), and holds under (b) (at most 6). Part (iii)\n    fails under both, with one session (001032/sub-2-1, 198 V/cm) ending with a last-100-ms dF of\n    5.9%.\n  deviations:\n  - The beats are counted from the stimulus onset at 50 ms, with the envelope at zero there (the\n    claims file's reading of the beat); the data support it, as the shifted beats show.\n  - Part (ii) is read on the APs pooled over the sessions with 5 APs or more; per session, 23 of 28\n    (a) and 21 of 22 (b) sessions have 80% or more in the window.\n- claim: fig2c-pure-more-aps\n  outcome: reproduced\n  notebook: reproduce_semenov_2025.ipynb\n  output: claim:fig2c-pure-more-aps\n  notes: In 52 pairs from 12 neurons (same neuron, carrier and generator voltage), the unmodulated\n    sine wave gave more APs in 46, fewer in 1 and as many in 5, a mean of 3.61 more (reading a,\n    paired t p = 3.3e-09); reading (b) 46 and 1, p = 2.5e-09; the bright-pixel trace 43 or 44 and\n    2. By carrier, 39 of 44 pairs at 2 kHz and 7 of 8 at 20 kHz (reading a).\n  deviations:\n  - Counts repeated at one field are averaged per pair, a standard choice.\n- claim: fig3b-low-conductivity-halves-threshold\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: No session of 001032, 001033 or 001035 is described as recorded in the sodium gluconate\n    solution; every description gives the standard NaCl solution. 001030 is in sodium gluconate but\n    holds only 2-s ramped stimuli. The NaCl and NaGlu sessions of Figures 3A and 3B, if deposited,\n    cannot be told apart.\n- claim: fig3c-sustained-firing-2s\n  outcome: partially_reproduced\n  notebook: reproduce_semenov_2025.ipynb\n  output: claim:fig3c-sustained-firing-2s\n  notes: Tested on neuron c7 of 001030, the only neuron with a trace without APs (1.0 V), which the\n    Methods' bleaching correction needs. (i) APs occur in the last 250 ms at 52, 61 and 72 V/cm (8\n    to 15 under reading a, 8 to 10 under b). (ii) The AP count rises with field, from 0 at 36 V/cm\n    to 142 at 83 V/cm under (a), and to 90 at 61 V/cm under (b), then 80 and 8. (iii) At the\n    highest field, 83 V/cm, the mean dF over 0.25 to 2 s is 6.7% and under (b) the APs stop at 0.21\n    s, within the ramp, with one more at 1.68 s, about what reading (b) finds by chance in 1.75 s;\n    reading (a) counts 131 peaks on the depolarized plateau after 250 ms. \"No APs after 250 ms\"\n    fails under both readings, by one event under (b). The other three neurons, corrected with the\n    same trace, reach no block (mean dF at most 4.0%).\n  deviations:\n  - The field is 36 V/cm times the one-polarity voltage that 001030 gives.\n  - The other neurons are corrected with c7's AP-free trace, as they have none of their own.\n  - Two recordings of neuron c5 have 6,000 frames, which end before the 2-s stimulus does.\n- claim: figs1-di8-anepps-control\n  outcome: not_reproduced\n  notebook: reproduce_semenov_2025.ipynb\n  output: claim:figs1-di8-anepps-control\n  notes: 001272 holds 3 neurons, where the paper used eight. The readings disagree on excitation (3\n    of 3 neurons under reading a at 5% and under both 5-SD readings, 1 of 3 under reading b at 5%),\n    but under every reading no neuron meets the block test at its highest field (0 of 3; inverted\n    last-100-ms dF 0.7%, 3.3% and 1.6%), so the claim fails under all of them and the\n    disagreement does not decide the outcome. Latency falls with field in 1 of 2 neurons with\n    three fields with APs under reading (a), and 2 of 3 under the 5-SD readings.\n  deviations:\n  - Only 3 of the paper's 8 neurons are in the dandiset.\n- claim: figs2-ttx-blocks-depolarization\n  outcome: partially_reproduced\n  notebook: reproduce_semenov_2025.ipynb\n  output: claim:figs2-ttx-blocks-depolarization\n  notes: In all 6 neurons recorded in tetrodotoxin (4 to 11 min after the normal-solution session at\n    the same field), APs present before are absent under reading (a); under reading (b) 5 of 6, as\n    (b) finds 5% rises in 15 of 17 tetrodotoxin sessions of one neuron where (a) finds none. The\n    last-100-ms dF in tetrodotoxin is at most 0.4% in every session. Only 1 of the 6 neurons had a\n    last-100-ms dF above 5% before tetrodotoxin (5.4%, falling to -0.7%), and no session of the 14\n    neurons never put in tetrodotoxin did (0 of 171), so the vehicle neuron of the criterion cannot\n    be shown to keep a sustained depolarization, and the criterion, which asks the depolarization\n    block of every tetrodotoxin neuron, fails in 5 of 6.\n  deviations:\n  - The compared field is the highest recorded both before and in tetrodotoxin, with the latest\n    normal session and the first tetrodotoxin session at it; the paper says \"about 5 min after\".\n  - No neuron is labelled as the vehicle control of Figure S2; all normal-solution sessions carry\n    the same \"vehicle control\" text.\n- claim: fig4-orientation-time-constants\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: 001273 holds raw strobe stacks only (181 files, 13 subjects). The ROIs over the most de-\n    and hyperpolarized regions are not deposited (claims file O1), no file says which cell is\n    elongated or random, and the field direction is in the descriptions of 118 of 181 files only\n    (up-bottom or right-left). The parallel, perpendicular and random groups cannot be formed.\n- claim: fig4-no-pole-difference\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: Depends on fig4-orientation-time-constants; the paper's ROIs are not in 001273, and the 19\n    experiments cannot be matched to its 13 subjects.\n- claim: fig4-discharging-slower\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: Depends on fig4-orientation-time-constants (no ROIs, no shape groups in 001273).\n- claim: fig4-pooled-time-constants\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: Depends on fig4-orientation-time-constants; no ROIs in 001273, and its 13 subjects cannot\n    be matched to the 19 experiments.\n- claim: fig5-carrier-antiphasic\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: 001274 holds raw strobe stacks only; the ROIs 1 and 2 are not deposited (claims file O1),\n    and cell C7 cannot be identified (O4). No subject has 12 sessions at 100 Hz (at most 5), as the\n    cell of Figure 5 had. With ROIs rebuilt from the RATIO image (a variant only, section 14),\n    ROI 2 oscillates in antiphase to ROI 1 in 7 of 9 candidate subjects.\n- claim: fig5-whole-cell-depolarization\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: As fig5-carrier-antiphasic; cell C7 and its ROIs cannot be identified in 001274.\n- claim: fig5-sine-asymmetry-c7\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: Depends on fig6c-sine-sensitivity; cell C7 and its ROIs cannot be identified in 001274.\n- claim: figs3-sine-asymmetry-c8\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: Depends on fig5-sine-asymmetry-c7; cell C8 and its ROIs cannot be identified in 001274.\n- claim: fig5fg-no-migration\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: The 16 further ROIs of Figure 5E and their split between Figures 5F and 5G are not in\n    001274, and cell C7 cannot be identified.\n- claim: fig6b-pulse-sensitivity\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: No ROIs in 001274 (claims file O1), no field in V/cm, and no identifier for cells C1 to\n    C9. Nine subjects have a pulse and 100-Hz sessions, consistent with C1 to C9 but not shown to\n    be them. As a variant only, ROIs rebuilt from the Methods' RATIO image (8 x 8 pixel squares at\n    its extremes in the cell) with the paper's 257 V/cm give 20.6 +- 2.7 %/kV/cm over 18 ROIs,\n    range 4.3 to 43.9 (paper 28 +- 2.5, 15 to 47). The frame times are an assumption (50-ns steps\n    from 1 us before the pulse).\n- claim: fig6c-sine-sensitivity\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: No ROIs, no waveform and no field in 001274. As a variant only, the rebuilt ROIs on the\n    100-Hz sessions of the nine candidate subjects, regressed frame by frame on a signed field\n    built from the paper's 136 V/cm peak and a carrier phase fitted to ROI 1, give 5.5 +- 0.8\n    %/kV/cm (span 0.75; range 0.2 to 12.9), with p below 0.0001 in 8 of 18 ROIs, and the same at\n    spans 0.5 and 0.25.\n- claim: fig6d-sine-less-than-pulse\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: Depends on fig6b-pulse-sensitivity and fig6c-sine-sensitivity. In the variant with\n    rebuilt ROIs the sine value is below the pulse value in 17 of 18 ROIs, and the mean sine\n    value is 26% of the mean pulse value (paper 42%).\n- claim: threshold-depolarization-estimate\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: Depends on fig6d-sine-less-than-pulse, blocked. Its other input, the 2-kHz threshold, is\n    not reproduced here (75.6 V/cm against 57.7).\nfindings:\n- kind: metadata_insufficient\n  statement: DANDI:001274 holds only raw strobe image stacks (512 x 512 pixels). It has no ROIs, no\n    RATIO images, no frame times, no electric field in V/cm (only generator volts) and no\n    identifier linking its 20 subjects to the paper's cells C1 to C9, C7 (Figure 5) and C8 (Figure\n    S3). The claims of Figures 5, 6 and S3 cannot be tested as the paper made them.\n- kind: metadata_insufficient\n  statement: DANDI:001273 (Figure 4) holds only raw strobe stacks. The ROIs, each cell's shape\n    group (elongated or random) and, in 63 of 181 files, the field direction are not given, so the\n    paper's 19 experiments and groups cannot be formed from its 13 subjects.\n- kind: other\n  statement: DANDI:001034 is a second deposit of DANDI:001032. The subjects (sub-N-3 against sub-N-1),\n    session names and sizes match for every asset, and the image arrays and start times of ten\n    compared pairs are identical. Each recording is counted once here.\n- kind: metadata_error\n  statement: The session descriptions of tetrodotoxin recordings in DANDI:001271 and DANDI:001274\n    say that tetrodotoxin \"abolished the action potentials and caused sustained depolarization\".\n    The paper says it \"fully blocked the sustained depolarization\", and in 001271 the mean dF over\n    the last 100 ms of the stimulus is at most 0.4% in every tetrodotoxin session.\n- kind: metadata_insufficient\n  statement: No 250-ms session in DANDI:001032, 001033 or 001035 is described as recorded in the\n    sodium gluconate solution of Figures 3A and 3B; all give the NaCl solution.\n- kind: metadata_insufficient\n  statement: The fast recordings give the generator's peak-to-peak voltage and \"1V translates into\n    36 V/cm\", but say the voltage is not the measured amplitude and that frequency-dependent\n    calibration factors \"will be reported separately\"; they are not in the dandisets. DANDI:001030\n    gives one-polarity volts. Whether the 36 V/cm applies to the peak-to-peak or the peak voltage\n    is not stated.\n- kind: data_missing\n  statement: DANDI:001272 holds 3 neurons recorded with Di-8-ANEPPS; the paper reports eight.\n- kind: other\n  statement: The fast recordings are 16 x 16 pixels, where the paper's Methods give 64 x 64 after\n    binning, and 59 of 178 sessions of 001032 have 900 frames, 2 have 1,400 and 1,800, against 1,200\n    in the Methods. The first frame of every fast and strobe recording is a bright artifact (median\n    3.05 times the next frames in the fast recordings).\n- kind: metadata_error\n  statement: The descriptions of DANDI:001032 to 001035 give a 140-um gap between the stimulating\n    electrodes; the paper's Methods and DANDI:001274 give 120 um.\n- kind: metadata_error\n  statement: DANDI:001030 makes one subject per session (sub-c7-1-45V and so on), so its 17\n    subjects are 4 neurons (c5 to c8). Two of its recordings (c5) have 6,000 frames and end before\n    the 2-s stimulus does.\n- kind: other\n  statement: Many strobe sessions of DANDI:001274 recorded on 2024-08-24 are described as made in\n    1 uM tetrodotoxin, which the paper does not mention for Figures 5, 6 or S3.\n- kind: methods_unavailable\n  statement: Question for the paper's authors. Which pixels form the soma ROI (F) of the fast\n    recordings, given the deposited 16 x 16 frames? This attempt assumed the whole frame, whose APs\n    have the Methods' typical size (median 11.4% dF against 11.3%), and ran the brighter half as a\n    variant; the outcomes do not change between them.\n- kind: methods_unavailable\n  statement: Question for the paper's authors. How were the generator voltages of the fast\n    recordings converted to the field in V/cm (peak or peak-to-peak, and with which frequency\n    calibration)? This attempt assumed 36 V/cm times half the peak-to-peak voltage; the 2-kHz\n    threshold is 75.6 V/cm with it and 151 V/cm with the whole voltage, against the paper's 57.7.\n- kind: methods_unavailable\n  statement: Question for the paper's authors. What rule counted APs, for example two APs close\n    together or APs riding on a depolarization? The maximum firing rate ceiling is 59.9 Hz with a\n    peak above 5% dF and 42.9 Hz with a 5% rise within 5 ms; this attempt assumed the first, as\n    the Methods' wording (\"APs peaked at a more than 5% dF\") reads.\n"
}
```

```
File created successfully at: attempts/001274-semenov-2025-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent**

Two fixes: the tetrodotoxin interval range, and the strobe first-frame claim (that frame is dim, and the notebook doesn't show it for every strobe file).

**Agent calls Bash**

```bash
python - <<'EOF'
p="attempts/001274-semenov-2025-01.yaml"; s=open(p).read()
for a,b in [("(4 to 11 min after the normal-solution session at\n    the same field)","(3.6 to 11 min after the normal-solution session\n    at the same field)"),
            ("The first frame of every fast and strobe recording is a bright artifact (median\n    3.05 times the next frames in the fast recordings).","The first frame of every fast recording is a bright artifact (median 3.05 times\n    the other pre-stimulus frames).")]:
    assert a in s; s=s.replace(a,b)
open(p,"w").write(s)
p="entries/001274-semenov-2025/ti_sine.py"; s=open(p).read()
a="cycle (Methods), leaving out frame 0, a bright artifact as in the fast recordings."
assert a in s; s=s.replace(a,"cycle (Methods), leaving out frame 0, an artifact as in the fast recordings.")
open(p,"w").write(s)
EOF
python -c "import yaml;d=yaml.safe_load(open('attempts/001274-semenov-2025-01.yaml'));print(len(d['outcomes']))"; grep -n ": " attempts/001274-semenov-2025-01.yaml | grep -v "^[0-9]*: *[-a-z_]*:" | grep -v "^[0-9]*: *- [a-z_]*:" | head
```

```
26
```

**Agent**

The YAML parses with 26 outcomes. The notebook has bold labels besides the Result openers, which I must remove; also checking for em dashes and the word "rather".

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
import re
s=open("build_nb.py").read()
for lab in ["Paper.","Dataset.","Claims","fig3b-low-conductivity-halves-threshold.","Figure 4 (001273).","Figures 5, 6 and S3 (001274).","How the analysis differs from the paper's.","What was found about the dandisets."]:
    assert f"**{lab}**" in s, lab
    s=s.replace(f"**{lab}**",lab)
open("build_nb.py","w").write(s)
print(sorted(set(re.findall(r"\*\*[^*]{0,30}",s))))
EOF
cd  && grep -n "—\|rather" attempts/001274-semenov-2025-01.yaml entries/001274-semenov-2025/ti_sine.py $TMPDIR/build_nb.py | head
```

```
['** 001272 holds 3 neurons, where', '** At 2 kHz, 27 of 28 neurons (9', '** Every 20-kHz threshold is hig', '** Firing locks to the beats: of', '** In 52 pairs of sessions from ', '** In all 6 neurons recorded in ', '** In neuron c7, (i) APs occur i', '** The highest-field session has', '** The mean 1-AP threshold for u', '** The median first-AP latency o', '** The modulated mean is higher ', '** The readings disagree: the me', '**Result: not reproduced.', '**Result: partially reproduced.', '**Result: reproduced, resting on', '**Result: reproduced.']
```

**Agent**

Now the entry README.

**Agent calls Write**

```json
{
 "file_path": "entries/001274-semenov-2025/README.md",
 "content": "# Semenov, Kim, Silkuniene & Pakhomov (2025) from dandiset 001274 and the paper's other dandisets\n\nTests the findings of [Semenov et al. (2025)](https://doi.org/10.1016/j.xcrp.2025.102660) that can be\ntested on [DANDI:001274](https://dandiarchive.org/dandiset/001274/0.250805.1401), which holds the strobe\nimages of membrane polarization by 2-us pulses and 2-kHz sine waves (Figures 5, 6 and S3), and on the\nother dandisets the paper deposited: the fast optical recordings of action potentials in 001032, 001033\nand 001035 (Figures 1 and 2), 001030 (Figure 3C), 001271 (Figure S2) and 001272 (Figure S1). 001034 is a\nsecond deposit of 001032.\n\n| Claim | Outcome |\n|---|---|\n| Unmodulated 2- and 20-kHz sine waves excite every neuron | Partially reproduced |\n| Near-threshold APs come 100 to 200 ms after onset; stronger fields shorten the delay | Partially reproduced |\n| The maximum firing rate reaches a ceiling of 60 to 90 Hz | Reproduced (resting on an assumption) |\n| The highest fields give an excitation block | Not reproduced |\n| 20-kHz thresholds are about twice the 2-kHz ones | Partially reproduced |\n| Modulated sine waves have higher thresholds | Partially reproduced |\n| The 2-kHz threshold is 57.7 V/cm | Not reproduced |\n| Firing locks to the 20-Hz beats, with no sustained depolarization | Partially reproduced |\n| Pure sine waves give more APs than modulated ones at the same field | Reproduced |\n| Low conductivity halves thresholds (Figure 3B) | Blocked: metadata insufficient |\n| 2-s ramped sine waves give sustained firing, then a block (Figure 3C) | Partially reproduced |\n| Di-8-ANEPPS gives the same responses (Figure S1) | Not reproduced |\n| Tetrodotoxin abolishes APs and the sustained depolarization (Figure S2) | Partially reproduced |\n| Membrane charging kinetics (Figure 4, four claims) | Blocked: metadata insufficient |\n| Polarization by sine waves and pulses (Figures 5, 6, S3, nine claims) | Blocked: metadata insufficient |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the\ndifferences from the paper's method.\n\nThe strobe dandisets (001274, 001273) hold raw image stacks only, with no ROIs, field values or cell\nidentifiers, so their claims are blocked; ROIs rebuilt from the paper's RATIO image are shown as a\nvariant. The attempt record, with the reasons and the differences from the paper's method, is\n[`attempts/001274-semenov-2025-01.yaml`](../../attempts/001274-semenov-2025-01.yaml).\n"
}
```

```
File created successfully at: entries/001274-semenov-2025/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
date -u; sed -i 's/runtime_minutes: 20/runtime_minutes: 25/' entries/001274-semenov-2025/entry.yaml && cd $TMPDIR && . work/bin/activate && python build_nb.py entries/001274-semenov-2025/reproduce_semenov_2025.ipynb && cd  && python tools/entry.py lock entries/001274-semenov-2025 | tail -1 && time python tools/entry.py all entries/001274-semenov-2025 2>&1 | tail -15
```

```
Sun Nov  1 16:23:15 UTC 2026
wrote entries/001274-semenov-2025/requirements.lock.txt
Installed kernelspec registry-001274-semenov-2025 in executed/001274-semenov-2025/.venv/share/jupyter/kernels/registry-001274-semenov-2025
0 error(s)
pass  reproduce_semenov_2025.ipynb  (1230 s)

real	20m36.874s
user	1m23.105s
sys	0m15.138s
```

**Agent**

Passed in 20.5 minutes with 0 check errors. Verifying the executed outputs against the conclusions.

**Agent calls Bash**

```bash
cd $TMPDIR && . work/bin/activate && python - <<'EOF'
import nbformat
nb=nbformat.read("executed/001274-semenov-2025/reproduce_semenov_2025.ipynb",4)
for i,c in enumerate(nb.cells):
    if c.cell_type!="code": continue
    t=c.metadata.get("tags",[])
    if any(x.startswith(("claim","variant","sanity")) for x in t) or i>=60:
        print("---",i,t)
        for o in c.outputs:
            if o.output_type=="stream": print(o.text[:2500])
            elif o.output_type=="error": print("ERROR",o.ename,o.evalue)
EOF
```

```
--- 14 ['sanity']
files: {'001032': 178, '001033': 193, '001035': 254, '001271': 287, '001272': 65, '001030': 17}
frame shapes and rates:
dandiset  shape           rate  
001030    (6000, 16, 16)  3134.8      2
          (7000, 16, 16)  3134.8     15
001032    (1200, 16, 16)  3086.4    117
          (1400, 16, 16)  3086.4      1
          (1800, 16, 16)  3086.4      1
          (900, 16, 16)   3086.4     59
001033    (1200, 16, 16)  3086.4    193
001035    (1200, 16, 16)  3086.4    253
          (6000, 16, 16)  3086.4      1
001271    (1200, 16, 16)  3086.4    287
001272    (1200, 16, 16)  3086.4     65

neurons per dandiset: {'001032': 14, '001033': 10, '001035': 15, '001271': 20, '001272': 3, '001030': 4}

sessions by carrier and modulation (001032, 001033, 001035):
modulated         False  True 
[... 230 more lines not kept]
```

**Agent**

All printed numbers match the conclusions and the record. Running the final check and the handover.

**Agent calls Bash**

```bash
python tools/entry.py check entries/001274-semenov-2025 | tail -3 && python tools/entry.py handover entries/001274-semenov-2025 2>&1 | tail -5; ls executed/001274-semenov-2025/handover/; git status --short | head; date -u
```

```
0 error(s)
wrote executed/001274-semenov-2025/handover
10.1016-j.xcrp.2025.102660.yaml
reproduce_semenov_2025.ipynb
ti_sine.py
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
Sun Nov  1 16:44:11 UTC 2026
```

**Agent calls Bash**

```bash
git status --short | grep -v "^?? \.\(bash\|zsh\|z\|git\|idea\|mcp\|profile\|ripgrep\|vscode\)"
```

```
?? attempts/001274-semenov-2025-01.yaml
?? entries/001274-semenov-2025/
?? scripts
```

**Agent calls Bash**

```bash
ls -la scripts | head; ls entries/001274-semenov-2025/
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  1 15:15 scripts
README.md
__pycache__
entry.yaml
reproduce_semenov_2025.ipynb
requirements.in
requirements.lock.txt
ti_sine.py
```

**Agent**

`scripts` and the dotfiles predate my run (sandbox artifacts), so I leave them. Removing the `__pycache__` my dev runs left in the entry.

**Agent calls Bash**

```bash
rm -rf entries/001274-semenov-2025/__pycache__ && ls entries/001274-semenov-2025/ && python tools/entry.py check entries/001274-semenov-2025 | tail -1; date -u
```

```
README.md
entry.yaml
reproduce_semenov_2025.ipynb
requirements.in
requirements.lock.txt
ti_sine.py
0 error(s)
Sun Nov  1 16:44:20 UTC 2026
```

**Agent**

I've finished steps 1 to 6: the entry is written, locked, checked and run from a clean environment (0 errors), the attempt record is written, and the handover is built. Of 26 claims, 2 are reproduced (one rests on an assumption), 7 partially reproduced, 3 not reproduced and 14 blocked.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig1-pure-sine-excites-all | partially reproduced (2 kHz excites 27 of 28 neurons, 20 kHz 15 of 17 = 88%, criterion asks 90%) |
| fig1-onset-delay | partially reproduced (latency falls with field in 38 of 38 pairs; median delay 64 ms, criterion asks 90 to 220) |
| fig1-max-rate-ceiling | reproduced, resting on an assumption (59.9 Hz under AP reading a; 42.9 Hz under reading b) |
| fig1-excitation-block | not reproduced (3 of 42 neuron-frequency pairs) |
| fig2d-20khz-twofold-threshold | partially reproduced (all p < 0.0001, but ratios 2.27 to 2.82 against 1.8 to 2.2) |
| fig2d-modulated-thresholds-higher | partially reproduced (1 of 3 pairs significant under reading a, 2 of 3 under b) |
| threshold-2khz-unmodulated | not reproduced (75.6 ± 6.2 V/cm against 57.7 ± 3.6) |
| fig2-modulated-locks-to-beats | partially reproduced (firing locks to the beats; one session ends depolarized) |
| fig2c-pure-more-aps | reproduced (46 of 52 pairs, p = 3e-09) |
| fig3c-sustained-firing-2s | partially reproduced |
| figs1-di8-anepps-control | not reproduced (only 3 of the paper's 8 neurons are deposited; no block under any reading) |
| figs2-ttx-blocks-depolarization | partially reproduced (APs gone in 6 of 6 neurons; only 1 had the sustained depolarization before) |
| fig3b, the four Figure 4 claims, the eight Figure 5/6/S3 claims, threshold-depolarization-estimate | blocked: metadata insufficient |

## 2. Dataset, assumptions, questions

**Dataset version.** Pinned 001274 at 0.250805.1401, the latest published version; the paper cites none, and the earlier version has the same assets. The other dandisets are also pinned at their latest versions and listed under `inputs`.

**What 001274 and 001273 hold.** Raw strobe image stacks only: no ROIs, no field in V/cm, no frame times, no cell shape groups, and nothing linking subjects to the paper's cells C1 to C9. That blocks all Figure 4, 5, 6 and S3 claims. As the claims file asks, I show ROIs rebuilt from the paper's RATIO image as a variant only:
- pulse: 20.6 ± 2.7 %/kV/cm (paper 28 ± 2.5);
- sine: about 5.5 %/kV/cm, 26% of the pulse value (paper 42%).

**Other findings about the dandisets:**
- 001034 is a second deposit of 001032: identical arrays and start times in the 10 pairs compared.
- No 250-ms session is labelled as sodium gluconate, which is why Figure 3B is blocked.
- The tetrodotoxin sessions are described as "caused sustained depolarization". The paper says tetrodotoxin blocked it, and in the data no tetrodotoxin session shows any.
- The voltage calibration factors are "to be reported separately" and are not in the dandisets.
- The images are 16×16 pixels; the paper gives 64×64.
- The first frame of every fast recording is a camera artifact.
- The electrode gap in the descriptions is 140 µm; the paper gives 120 µm.
- 001030 makes one subject per session (17 subjects for 4 neurons).
- 001272 holds 3 neurons; the paper used 8.
- Many 001274 strobe sessions are labelled tetrodotoxin, which the paper does not mention for these figures.

**Assumptions**, each recorded as a question for the paper's authors:
- **Soma ROI:** the whole frame. Its first APs have a median of 11.4% dF against the Methods' typical 11.3%. The brighter half of the frame, run as a variant, changes no outcome.
- **Field:** 36 V/cm times half the peak-to-peak voltage. The full voltage was also run; it changes no outcome.
- **AP reading for the firing-rate ceiling:** reading (a), a peak above 5%, which is how the Methods word it.

**Questions to a reader:** none.

## 3. Protocol gaps

1. **Most claims use other archives' data.** 13 of 26 claims are `data: elsewhere`, on six other dandisets, and the protocol assumes one dataset per entry. I put every dandiset under `related` and `inputs`, and the record names 001274.
2. **Repeated readings.** Step 1.6 has every reading run, and many criteria add their own, so the AP readings, ROIs and field conversions multiply into grids. I chose one adopted reading, showed the others as variants, and recorded an assumption only where the readings changed an outcome.
3. **Readings that disagree on a part that doesn't decide the outcome.** In the Di-8-ANEPPS claim the criterion says to block when readings disagree. They disagree on excitation, but the claim fails the block test under every reading. I recorded it as not reproduced and said why.
4. **Clock check.** "Every data stream shares the clock of the trial tables" doesn't fit image files with no stimulus channel. I used two substitutes: no APs before the stimulus under reading (a), and AP locking to the 20-Hz beats, which drops from 0.90 to 0.10 when the beats are shifted by 25 ms.
5. **No fit for duplicate deposits.** A duplicate across dandisets (001034 of 001032) has no finding kind of its own; I recorded it as `other`.

## 4. Runtime and failures

- The notebook runs in 20.4 minutes from a clean environment. It streams about 1,000 small files plus about 7 GB of strobe stacks.
- The whole session took about 1.5 hours (15:16 to 16:44 UTC).
- An early AP detector counted the shoulder of one AP twice, and noise peaks on the aliased 2-kHz carrier at high fields as APs. I fixed this by merging peaks closer than the paper's 8-ms AP duration.
- A per-cycle reading of the sine regression (reading b in the claims file) was swamped by single-frame noise. I dropped it and say so in the notebook.
- Nothing else failed. Nothing is committed.

## End of run

79 turns, 84 minutes, result: success.
