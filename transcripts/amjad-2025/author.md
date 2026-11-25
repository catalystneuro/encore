# amjad-2025 · author · run 45504266872

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; ls; ls docs entries claims attempts paper tools | head -80
```

```
Tue Nov 24 22:56:30 UTC 2026
LICENSE
LICENSE-data
README.md
attempts
bunfig.toml
claims
docs
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
protocol.lock
[... 90 more lines not kept]
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
9	([pilot notes](https://github.com/encorescience/encore-registry/blob/main/docs/pilot-notes.md)); the reasons for the rules are there.
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

**Agent calls Bash**

```bash
cat claims/amjad-2025.yaml; ls paper; cat papers/datasets/amjad-2025.yaml; ls papers/author-notes | grep amjad; ls questions | grep amjad; ls entries/amjad-2025 attempts | grep amjad
```

```
# Claims for Amjad, Mahajan, Choi, Shrivastav, Murray, Somich, Coyne and Schwerdt (2025),
# "Microinvasive Probes for Monitoring Electrical and Chemical Neural Activity in Nonhuman
# Primates", ACS Chem Neurosci 16:2237-2247, on dandiset 002013.
# Source: the full text, open access under CC-BY 4.0 (PMC12183687), read from its Results,
# figure legends and Methods.
#
# The paper is mostly about fabrication. Its numbers are the insertion yields, the days
# post-implant of the example sites and the recording parameters; its neural results
# (Figures 3 to 5) are example traces and trial averages shown without statistics. The claims
# below turn each figure panel into a test that can be run on the dandiset.
#
# When these criteria were written the author had seen the data check only: the file
# contents; the event codes, which repeat about five times each in the events tables and were
# deduplicated; the trial conditions decoded from the event codes, and that the 09/26/2024
# selections match the paper's trial lists on Zenodo (zenodo-link); the applied FSCV waveform;
# the sampling rates and filter settings; that the raw 09/26/2024 ephys is offset from the
# trial clock, that the raw FSCV current could not be matched to the trial-aligned FSCV traces
# and shows no reward contrast at its stored times, and that Monkey P's spike times are offset
# from its raw signal. For zenodo-link the author had also already seen that beta power computed
# here correlates with the paper's example trace at r = 0.94, so that criterion was written after
[... 262 more lines not kept]
```

**Agent calls Bash**

```bash
wc -c paper/*; cat paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/f80e1467-32f6-4c5c-abb5-e96c0dfb8bda/tool-results/b72lkb4fk.txt"
}
```

```
1	82540 paper/10.1021-acschemneuro.5c00071.txt
2	DOI: 10.1021/acschemneuro.5c00071
3	Version: as served by europe_pmc
4	Source: europe_pmc+crossref (paper-text-fetcher)
5	Stored: 2026-10-20
6	Extracted: as fetched
7	------------------------------------------------------------------------
8	822 acssd ACS Chemical Neuroscience ACS Chem Neurosci PMC12183687 12183687 12183687 40446210 10.1021/acschemneuro.5c00071 Microinvasive
9	Probes for Monitoring Electrical and
10	Chemical Neural Activity in Nonhuman Primates Amjad Usamma † Mahajan Shreya † Choi Jiwon † Shrivastav Ritesh † Murray Raymond † Somich Abby † Coyne Olivia † Schwerdt Helen N † ‡ * † Department
11	of Bioengineering, University of Pittsburgh, Pittsburgh, Pennsylvania
12	15213, United States ‡ Aligning
13	Science Across Parkinson’s (ASAP) Collaborative Research Network, Chevy Chase, Maryland
14	20815, United States * Email: [removed: an e-mail address] . 30 5 2025 16 12 2237 2237–2247 24 6 2025 © 2025 The Authors. Published by American Chemical Society This article is licensed under CC-BY 4.0 Previous version available: This article is based on a previously available preprint posted on bioRxiv on February 5, 2025: " Micro-invasive probes for monitoring electrical and chemical neural activity in nonhuman primates ". Abstract We leveraged carbon
15	fiber materials for creating sensors
16	that provide
17	dual neurochemical and electrical neural activity recording at microinvasive
18	(10 μm) spatial footprints proximal to recording sites, and
19	enabling these measurements from deep brain targets of primates with
20	conventional cranial chambers. These shaft-assisted microinvasive
[... 711 more lines not kept]
```

**Agent**

Paper read. Now the registry docs and the example entry.

**Agent calls Bash**

```bash
sed -n 1,200p docs/archives.md | head -150; ls entries/fouke-2025; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in
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
[... 165 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/fouke-2025-01.yaml | head -250; wc -l attempts/fouke-2025-01.yaml
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
[... 231 more lines not kept]
```

**Agent calls Bash**

```bash
ls schemas; grep -l "pilot-18" attempts/*.yaml | head; sed -n 250,330p attempts/fouke-2025-01.yaml
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
attempts/du-2026-01.yaml
attempts/dvali-2025-01.yaml
attempts/elliott-2026-01.yaml
attempts/fritsche-2022-01.yaml
attempts/gable-2026-01.yaml
attempts/hasnain-2025-01.yaml
attempts/jarzebowski-2026-01.yaml
attempts/kim-2025-01.yaml
attempts/lakshminarasimhan-2024-01.yaml
attempts/mansvelder-2026-01.yaml
- kind: metadata_insufficient
  statement: The stimulus codes 0 to 20 have no names or description in the files or the
    dandiset metadata. They can be named only from the paper's analysis notebook and the protocol
    file of its stimulus software.
- kind: code_mismatch
  statement: The paper's analysis notebook labels code 9 as lateral right and 11 as lateral left,
[... 75 more lines not kept]
```

**Agent calls Bash**

```bash
ls -la entries/ | grep -E "kim-2025|du-2026|gable"; sed -n 1,60p attempts/gable-2026-01.yaml; grep -n "severity\|found:\|assumed\|seed_sensitive" attempts/gable-2026-01.yaml | head
```

```
drwxr-xr-x   2 runner runner  4096 Nov 24 22:48 du-2026
drwxr-xr-x   2 runner runner  4096 Nov 24 22:48 gable-2026
drwxr-xr-x   2 runner runner  4096 Nov 24 22:48 kim-2025
schema_version: 3
id: gable-2026-01
datasets:
- archive: dandi
  id: '000010'
  version: 0.220126.1905
  doi: 10.48324/dandi.000010/0.220126.1905
  relation: reuses
paper: doi:10.1523/jneurosci.0974-26.2026
date: '2026-11-22'
entry: gable-2026
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
[... 53 more lines not kept]
```

**Agent**

Now the dataset itself.

**Agent calls Bash**

```bash
cd $TMPDIR && curl -s "https://api.dandiarchive.org/api/dandisets/002013/versions/" | python -m json.tool | head -60; curl -s "https://api.dandiarchive.org/api/dandisets/002013/versions/0.261120.1306/assets/?page_size=100" | python -c "
import json,sys; d=json.load(sys.stdin); print(d['count'])
for a in d['results']: print(a['asset_id'], a['path'], a['size'], a['modified'])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q scratch && . scratch/bin/activate && uv pip install -q pynwb h5py remfile dandi numpy scipy pandas matplotlib nbformat 2>&1 | tail -3; python -c "import pynwb; print(pynwb.__version__)"; curl -s "https://api.dandiarchive.org/api/dandisets/002013/versions/0.261120.1306/" | python -m json.tool | head -120
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s "https://api.dandiarchive.org/api/dandisets/002013/versions/0.261120.1306/" | python3 -c "
import json,sys; d=json.load(sys.stdin)
for k in ['description','relatedResource','assetsSummary','wasGeneratedBy','ethicsApproval']: print(k, json.dumps(d.get(k),indent=1)[:3000])"
```

Result: the fetched text is not kept.

**Agent**

Now open each file and list its contents.

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/w && cat > $TMPDIR/w/survey.py <<'EOF'
import sys, h5py, remfile, requests, pynwb, time
V="0.261120.1306"
aid=sys.argv[1]
url=requests.get(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=False).headers["Location"]
t=time.time()
f=h5py.File(remfile.File(url),"r")
io=pynwb.NWBHDF5IO(file=f,load_namespaces=True); nwb=io.read()
print(nwb)
print("start", nwb.session_start_time, "desc", nwb.session_description)
print("subject", nwb.subject)
print("devices", {k:(v.description) for k,v in nwb.devices.items()})
print("electrode groups", {k:(v.description, v.location) for k,v in nwb.electrode_groups.items()})
if nwb.electrodes is not None:
    df=nwb.electrodes.to_dataframe(); 
    import pandas as pd; pd.set_option("display.width",250); pd.set_option("display.max_columns",50); pd.set_option("display.max_colwidth",200)
    print(df.T)
def walk(name,obj):
    if isinstance(obj,h5py.Dataset): print(name, obj.shape, obj.dtype, dict((k,(v if not hasattr(v,'shape') or v.size<5 else '...')) for k,v in obj.attrs.items() if k not in ('object_id','namespace','neurodata_type')))
f.visititems(walk)
print("time",time.time()-t)
EOF
cd $TMPDIR && . scratch/bin/activate && python w/survey.py 45c1c0d6-6d9f-4498-bc00-f033f638aaa7 2>&1 | grep -v "^specifications\|^general/" | head -150
```

```
root pynwb.file.NWBFile at 0x139253640786144
Fields:
  acquisition: {
    fscv_response_series <class 'abc.FSCVResponseSeries'>
  }
  devices: {
    device_ecephys <class 'pynwb.device.Device'>
  }
  electrode_groups: {
    FSCVElectrodeGroup <class 'pynwb.ecephys.ElectrodeGroup'>
  }
  electrodes: electrodes <class 'pynwb.ecephys.ElectrodesTable'>
  experiment_description: This experiment contains in vivo recordings of reward- and movement-related dopamine, spikes, and local field potentials obtained using single- and dual-channel shaft-assisted micro-invasive probes (s-µIPs) chronically implanted in the striatum of task-performing rhesus monkeys. The s-µIPs leverage carbon fiber materials to enable dual neurochemical and electrical neural activity recording at micro-invasive (10 µm) spatial footprints near the recording sites, while a wider shaft provides rigidity for deep brain targeting using standard cranial chambers. These probes allow for measurements from deep brain targets with minimal tissue disruption at the recording site. Recordings were made during performance of reward-biased eye movement tasks, enabling simultaneous measurement of dopamine transients, spikes, and local field potentials with micrometer spatial resolution. Chronic implants demonstrated stable, multi-modal neural activity measurements from micro-invasive devices over extended periods post-implantation.
  experimenter: ['Schwerdt, Helen N.' 'Amjad, Usamma']
  file_create_date: [datetime.datetime(2026, 11, 18, 12, 0, 49, 103895, tzinfo=tzoffset(None, 3600))]
  identifier: cd8ba2af-ddc1-49fb-9e9e-b250e45dc6e2
  institution: University of Pittsburgh
  intervals: {
    trials <class 'pynwb.epoch.TimeIntervals'>
  }
[... 78 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . scratch/bin/activate && python w/survey.py ee853893-622e-4ee9-b0cf-6e0cf25999a1 2>&1 | grep -v "^specifications" | sed -n '/^devices/,$p' | head -80; python w/survey.py 45c1c0d6-6d9f-4498-bc00-f033f638aaa7 2>&1 | grep "^general/"
```

```
devices {'device_ecephys': 'Neuralynx recording'}
electrode groups {'ElectrodeGroup': ('Electrodes implanted in the striatum, recorded with Neuralynx (Digital Lynx SX).', 'striatum')}
id                                                                                                                                                                                                                             0  \
location                                                                                                                                                                                                                    c3bs   
group                    ElectrodeGroup pynwb.ecephys.ElectrodeGroup at 0x133907769827616\nFields:\n  description: Electrodes implanted in the striatum, recorded with Neuralynx (Digital Lynx SX).\n  device: device_ecephys...   
group_name                                                                                                                                                                                                        ElectrodeGroup   
channel_name                                                                                                                                                                                                               CSC37   
DSPHighCutFilterEnabled                                                                                                                                                                                                     True   
recording_closed                                                                                                                                                                                             2024-09-26 16:02:14   
DspLowCutFilterType                                                                                                                                                                                                         
[... 89 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . scratch/bin/activate && python w/survey.py ee853893-622e-4ee9-b0cf-6e0cf25999a1 2>&1 | grep -v "^specifications\|^general" | sed -n '/^acquisition/,$p'; python w/survey.py 6eaaf54b-e743-4642-b699-702b19fe3722 2>&1 | grep -v "^specifications" | sed -n '/^start/,$p' | grep -v "^general/extracellular_ephys/electrodes/D"
```

```
acquisition/electrical_series/data (722978367, 2) int16 {'conversion': np.float64(3.0517578125e-08), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'volts'}
acquisition/electrical_series/electrodes (2,) int64 {'description': 'electrode_table_region', 'table': <HDF5 object reference>}
acquisition/electrical_series/starting_time () float64 {'rate': np.float64(31999.962403839356), 'unit': 'seconds'}
file_create_date (1,) object {}
identifier () object {}
intervals/trials/id (1501,) int64 {}
intervals/trials/midpoint_time (1501,) float64 {'description': 'Time of the trial start event (code 128), the centre of the 60 s window.'}
intervals/trials/start_time (1501,) float64 {'description': 'Start time of epoch, in seconds'}
intervals/trials/stop_time (1501,) float64 {'description': 'Stop time of epoch, in seconds'}
intervals/trials/tags (1501,) object {'description': 'user-defined tags'}
intervals/trials/tags_index (1501,) uint16 {'description': "Index for VectorData 'tags'", 'target': <HDF5 object reference>}
intervals/trials/timeseries (1501,) [('idx_start', '<i4'), ('count', '<i4'), ('timeseries', 'O')] {'description': 'index into a TimeSeries object'}
intervals/trials/timeseries_index (1501,) uint16 {'description': "Index for VectorData 'timeseries'", 'target': <HDF5 object reference>}
processing/ecephys/FilteredEphys/bipolar_lfp_series/data (19246352, 1) float64 {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'volts'}
processing/ecephys/FilteredEphys/bipolar_lfp_series/electrodes (1,) int64 {'description': 'The electrode of site c3bs; the signal is referenced to site c3a.', 'table': <HDF5 object reference>}
processing/ecephys/FilteredEphys/bipolar_lfp_series/timestamps (19246352,) float64 {'interval': np.int64(1), 'unit': 'seconds'}
processing/events/events_table/event_description (20,) object {'description': 'Description for each event type.'}
processing/events/events_table/event_times (15437,) fl
[... 74 more lines not kept]
```

**Agent**

Let me read the small tables: events, trial tags, units, notes.

**Agent calls Bash**

```bash
cat > $TMPDIR/w/small.py <<'EOF'
import sys, h5py, remfile, requests, pynwb, numpy as np, pandas as pd, collections
pd.set_option("display.width",250); pd.set_option("display.max_colwidth",160); pd.set_option("display.max_rows",100)
aid=sys.argv[1]
url=requests.get(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=False).headers["Location"]
f=h5py.File(remfile.File(url),"r")
nwb=pynwb.NWBHDF5IO(file=f,load_namespaces=True).read()
print("notes:", nwb.notes)
ev=nwb.processing["events"]["events_table"]
print(ev.description if hasattr(ev,'description') else '')
df=ev.to_dataframe()
df["n"]=df.event_times.apply(len); df["first"]=df.event_times.apply(lambda x: x[0] if len(x) else np.nan); df["last"]=df.event_times.apply(lambda x: x[-1] if len(x) else np.nan)
print(df.drop(columns="event_times"))
if nwb.trials is not None:
    tr=nwb.trials.to_dataframe()
    print(tr.drop(columns=[c for c in tr.columns if c=="timeseries"]).head(5))
    print(nwb.trials.description if hasattr(nwb.trials,'description') else '')
    c=collections.Counter(t for tags in tr.tags for t in tags); print(c)
    print("start-mid", (tr.midpoint_time-tr.start_time).describe(), "stop-mid",(tr.stop_time-tr.midpoint_time).describe())
    print("diff mid", np.diff(tr.midpoint_time).min(), np.median(np.diff(tr.midpoint_time)))
if nwb.units is not None:
    u=nwb.units.to_dataframe(); print(u.assign(n=u.spike_times.apply(len)).drop(columns='spike_times'))
    print(nwb.units.description)
    tu=nwb.processing["ecephys"]["thresholded_units"]; print(tu.description); t=tu.to_dataframe(); print(t.assign(n=t.spike_times.apply(len)).drop(columns=['spike_times','waveforms']))
EOF
cd $TMPDIR && . scratch/bin/activate && for a in 45c1c0d6-6d9f-4498-bc00-f033f638aaa7 ee853893-622e-4ee9-b0cf-6e0cf25999a1 6eaaf54b-e743-4642-b699-702b19fe3722; do echo "=== $a"; python w/small.py $a 2>&1; done
```

```
=== 45c1c0d6-6d9f-4498-bc00-f033f638aaa7
notes: None
Task events from the 8-bit Neuralynx event codes, named by the event map of the trial list. Each event is stored once, in time order. Codes missing from the event map are named 'TTL code <code>'. The meaning of the reward condition codes is inferred from the reward events of the session.
                                     label  ...          last
id                                          ...              
0                               TTL code 0  ...  25848.077432
1                               TTL code 8  ...  20184.650041
2                              start trial  ...  25710.143671
3                                end trial  ...  25718.022527
4                                 feedback  ...  25702.827219
5                       value object start  ...  25698.995033
6                          central cue end  ...  25711.974463
7                                    onedr  ...  25697.164086
8              left cue reward condition 1  ...  25467.672079
9              left cue reward condition 2  ...  25710.209202
10            right cue reward condition 1  ...  25710.208921
11            right cue reward condition 2  ...  25697.163523
12            central cue fixation started  ...  25710.541233
13              value cue fixation started  ...  25712.607305
14       forced trial valuecue fix started  ...  25699.394950
[... 170 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/w/ev.py <<'EOF'
import sys, h5py, remfile, requests, pynwb, numpy as np
aid=sys.argv[1]
url=requests.get(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=False).headers["Location"]
f=h5py.File(remfile.File(url),"r")
nwb=pynwb.NWBHDF5IO(file=f,load_namespaces=True).read()
df=nwb.processing["events"]["events_table"].to_dataframe()
for i,r in df.iterrows(): print(i, repr(r.label), len(r.event_times), round(r.event_times[0],2) if len(r.event_times) else None, "|", r.event_description)
if nwb.units is not None: print(nwb.units.unit_name[:])
EOF
cd $TMPDIR && . scratch/bin/activate && for a in 45c1c0d6-6d9f-4498-bc00-f033f638aaa7 ee853893-622e-4ee9-b0cf-6e0cf25999a1; do echo "=== $a"; python w/ev.py $a 2>&1; done; python w/ev.py 6eaaf54b-e743-4642-b699-702b19fe3722 | cut -c1-200
```

```
=== 45c1c0d6-6d9f-4498-bc00-f033f638aaa7
0 'TTL code 0' 2 11039.57 | The event times for code 0, which is not in the event map.
1 'TTL code 8' 1 20184.65 | The event times for code 8, which is not in the event map.
2 'start trial' 1468 6919.16 | The event times for code 9.
3 'end trial' 1468 6932.5 | The event times for code 18.
4 'feedback' 303 6925.85 | The event times for code 21.
5 'value object start' 323 6922.07 | The event times for code 23.
6 'central cue end' 977 6944.73 | The event times for code 24.
7 'onedr' 358 6920.17 | The event times for code 28.
8 'left cue reward condition 1' 639 6957.46 | The event times for code 30. Choice trials: the left cue is the big-reward cue (code 101 after choosing it).
9 'left cue reward condition 2' 471 6934.6 | The event times for code 31. Choice trials: the left cue is the cue without the big reward (no code 101 after choosing it).
10 'right cue reward condition 1' 652 6920.17 | The event times for code 35. The right cue in choice trials, or the single cue on either side in forced trials (side given by codes 117 and 118), is the big-reward cue (code 101).
11 'right cue reward condition 2' 816 6957.46 | The event times for code 36. The right cue in choice trials, or the single cue on either side in forced trials (side given by codes 117 and 118), is the cue without the big reward (no code 101).
12 'central cue fixation started' 1404 6920.63 | The event times for code 50.
13 'value cue fixation started' 977 6945.06 | The event times for code 51.
14 'forced trial valuecue fix started' 323 6922.42 | The event times for code 53.
15 'error fixation break target' 104 7046.39 | The event times for code 60.
16 'error fixation break initial' 2 22135.46 | The event times for code 61.
17 'error fixation never started' 62 6936.63 | The event times for code 62.
18 'error choice value initial fix break' 1 20346.43 | The event times for code 65.
[... 75 more lines not kept]
```

**Agent**

Events are deduplicated and carry their codes in descriptions. Monkey P's session has no code map and no trials table. Checking the paper's Zenodo deposits next.

**Agent calls Bash**

```bash
for r in 14826579 10955583 10397773; do curl -s https://zenodo.org/api/records/$r | python3 -c "
import json,sys; d=json.load(sys.stdin); m=d['metadata']; print(d['id'], m['title'], m.get('version'), m.get('publication_date')); print(m.get('description','')[:800])
for f in d['files']: print('  ', f['key'], f['size'], f['links']['self'])
print([ (x.get('identifier'),x.get('relation')) for x in m.get('related_identifiers',[])])"; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && curl -sL https://zenodo.org/api/records/10955583 | head -c 1500; echo; curl -sL -o w/s126.mat "https://zenodo.org/api/records/14826579/files/session126_events.mat/content"; for n in ISI_Plot.m spikes_PCA.m readme.txt; do echo "--- $n"; curl -sL "https://zenodo.org/api/records/10397773/files/$n/content"; done; . scratch/bin/activate; python -c "
import scipy.io as s, h5py
try:
  d=s.loadmat('w/s126.mat'); print({k:(getattr(v,'shape',None),getattr(v,'dtype',None)) for k,v in d.items()})
except Exception as e:
  print(e); f=h5py.File('w/s126.mat'); f.visititems(lambda n,o: print(n,getattr(o,'shape',''),getattr(o,'dtype','')))
"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && . scratch/bin/activate; python -c "
import scipy.io as s, collections
d=s.loadmat('w/s126.mat'); es=[x[0][0] if len(x[0]) else '' for x in d['dg_Nlx2Mat_EventStrings']]
print(collections.Counter(es).most_common(8)); print(d['dg_Nlx2Mat_Timestamps'][0][:5]); print(d['dg_Nlx2Mat_TTL'][0][:40])"; date -u
```

```
[(np.str_('TTL Input on AcqSystem1_0 board 0 port 0 value (0x0022).'), 1854), (np.str_('TTL Input on AcqSystem1_0 board 0 port 0 value (0x0021).'), 1853), (np.str_('TTL Input on AcqSystem1_0 board 0 port 0 value (0x0064).'), 1660), (np.str_('TTL Input on AcqSystem1_0 board 0 port 0 value (0x0004).'), 932), (np.str_('TTL Input on AcqSystem1_0 board 0 port 0 value (0x0023).'), 825), (np.str_('TTL Input on AcqSystem1_0 board 0 port 0 value (0x0014).'), 825), (np.str_('TTL Input on AcqSystem1_0 board 0 port 0 value (0x001B).'), 825), (np.str_('TTL Input on AcqSystem1_0 board 0 port 0 value (0x0024).'), 824)]
[6.80066578e+09 6.84622983e+09 6.84629516e+09 6.84798266e+09
 6.84838113e+09]
[  0  33  34  33  34  33  34  33  34  33  35  34  20  25  27  29  32 100
 110 100  36   3   4   8   5   0   7  10  11  18  45  13  26  33  34  33
  34  33  34  35]
Tue Nov 24 22:58:34 UTC 2026
Shell cwd was reset to
```

**Agent**

Time is fine (22:58). Let me look at a recent pilot-18 entry's layout and the entry tool, then build the helper.

**Agent calls Bash**

```bash
ls entries/gable-2026; cat entries/gable-2026/entry.yaml; python3 -c "
import json; nb=json.load(open('entries/gable-2026/'+[f for f in __import__('os').listdir('entries/gable-2026') if f.endswith('.ipynb')][0]))
for c in nb['cells'][:6]: print(c['cell_type'], c.get('metadata'), ''.join(c['source'])[:1500]); print('----')
print(nb['metadata'])"; sed -n 1,80p tools/entry.py | head -80
```

```
README.md
alm_coupling.py
entry.yaml
reproduce_gable_2026.ipynb
requirements.in
requirements.lock.txt
schema_version: 1
name: gable-2026
type: reproduction
title: Population coupling in ALM silicon-probe recordings (Gable et al. 2026, Figure S4)
description: Tests the Figure S4 and Table 5 findings of Gable, Newman, Young, Scheib, Bliese,
  Miller and Kerlin (2026) on dandiset 000010, the ALM silicon-probe recordings of Li et al. (2015)
  that the paper reanalyses. It repeats the session selection, computes the population coupling of
  each neuron from trial-specific activity, and compares pairwise correlations within and across
  coupling bins with the paper's session bootstrap. The paper's own two-photon imaging is not public.
license: Apache-2.0
python: "3.13"
notebooks:
- path: reproduce_gable_2026.ipynb
  title: Reproducing Gable et al. (2026), Figure S4, from dandiset 000010
[... 201 more lines not kept]
```

**Agent**

Now exploring the 09/13 FSCV data (on a subset).

**Agent calls Bash**

```bash
cat > $TMPDIR/w/fscv1.py <<'EOF'
import h5py, remfile, requests, numpy as np, time, resource
aid="45c1c0d6-6d9f-4498-bc00-f033f638aaa7"
url=requests.get(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=False).headers["Location"]
f=h5py.File(remfile.File(url),"r")
t0=time.time()
v=f["stimulus/presentation/fscv_excitation_series/data"][:200000]
tv=f["stimulus/presentation/fscv_excitation_series/timestamps"][:200000]
i=f["acquisition/fscv_response_series/data"][:200000]
ti=f["acquisition/fscv_response_series/timestamps"][:200000]
print("read", time.time()-t0)
print("same ts", np.array_equal(tv,ti), tv[:3], tv[-1])
d=np.diff(tv); print("dt uniq", np.unique(np.round(d,7))[:10], np.percentile(d,[0,50,99,100]))
big=np.where(d>1e-3)[0]; print("gaps", len(big), big[:10], d[big[:5]])
print("V range", v.min(), v.max(), "I range", i.min(), i.max())
# per-scan
seg=np.split(np.arange(len(v)), big+1)
print("scan lengths", np.unique([len(s) for s in seg], return_counts=True))
s=seg[1]; print(np.round(v[s][:5],3), np.round(v[s][len(s)//2-3:len(s)//2+3],3), np.round(v[s][-5:],3))
starts=tv[[s[0] for s in seg]]; print("scan intervals", np.unique(np.round(np.diff(starts),4),return_counts=True))
n=f["stimulus/presentation/fscv_excitation_series/timestamps"].shape[0]; print("total", n, n/850 if True else 0)
ts_last=f["stimulus/presentation/fscv_excitation_series/timestamps"][-3:]; print("first, last time", tv[0], ts_last)
EOF
cd $TMPDIR && . scratch/bin/activate && python w/fscv1.py
```

```
read 1.6963090896606445
same ts True [1717.96696536 1717.96700536 1717.96704536] 1811.3728329677872
dt uniq [4.00000e-05 9.14809e-02] [4.00004058e-05 4.00004058e-05 4.00004060e-05 9.14809281e-02]
gaps 934 [ 213  427  641  855 1069 1283 1497 1711 1925 2139] [0.09148093 0.09148093 0.09148093 0.09148093 0.09148093]
V range -0.34735225277847875 1.3400425957748434 I range -1526.457953716921 1556.9812444299505
scan lengths (array([124, 214]), array([  1, 934]))
[-0.347 -0.34  -0.329 -0.316 -0.301] [1.297 1.313 1.329 1.34  1.339 1.332] [-0.257 -0.273 -0.289 -0.305 -0.321]
scan intervals (array([0.1]), array([934]))
total 51616800 60725.64705882353
first, last time 1717.9669653572664 [25838.12010638 25838.12014638 25838.12018638]
Shell cwd was reset to
```

**Agent**

Scans are 214 samples at 25 kHz, every 0.1 s; the stored voltage runs -0.347 to 1.340 V. Checking chunking and the trial-aligned table timing.

**Agent calls Bash**

```bash
cat > $TMPDIR/w/fscv2.py <<'EOF'
import h5py, remfile, requests, numpy as np, time, pandas as pd
aid="45c1c0d6-6d9f-4498-bc00-f033f638aaa7"
url=requests.get(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=False).headers["Location"]
f=h5py.File(remfile.File(url),"r")
T=f["acquisition/fscv_response_series/timestamps"]; print(T.chunks, T.compression)
t0=time.time(); ts=T[:]; print("full ts read", time.time()-t0)
d=np.diff(ts); gap=np.where(d>1e-3)[0]
starts=np.r_[0,gap+1]; L=np.diff(np.r_[starts,len(ts)]); print(np.unique(L,return_counts=True))
st=ts[starts]; dd=np.diff(st); print("scan interval", np.unique(np.round(dd,4),return_counts=True))
np.save("/tmp/claude/scanstarts.npy" if False else __import__('os').environ['TMPDIR']+"/w/scanstarts.npy", np.c_[starts,st])
g="processing/fscv/trial_aligned_fscv_table/"
tab=pd.DataFrame({k:f[g+k][:] for k in ["start_time","stop_time","trial_index","good","rate"]})
mid=f["intervals/trials/midpoint_time"][:]
tab["mid"]=mid[tab.trial_index]; print((tab.start_time-tab.mid).describe()); print(tab.head()); print(tab.good.value_counts(), tab.rate.unique())
print("trial idx range", tab.trial_index.min(), tab.trial_index.max(), "unique", tab.trial_index.nunique())
EOF
cd $TMPDIR && . scratch/bin/activate && python w/fscv2.py
```

```
(1250000,) gzip
full ts read 7.174645900726318
(array([214]), array([241200]))
scan interval (array([0.1]), array([241199]))
count    734.0
mean     -30.0
std        0.0
min      -30.0
25%      -30.0
50%      -30.0
75%      -30.0
max      -30.0
dtype: float64
    start_time    stop_time  trial_index  good  rate          mid
0  6890.167919  6950.167919            0  True  10.0  6920.167919
1  6904.596687  6964.596687            1  True  10.0  6934.596687
2  6912.777150  6972.777150            2  True  10.0  6942.777150
3  6927.455969  6987.455969            3  True  10.0  6957.455969
4  6935.819853  6995.819853            4  True  10.0  6965.819853
good
[... 4 more lines not kept]
```

**Agent**

The trial-aligned FSCV table covers trials 0 to 733, each a 60 s window centred on code 128. Now I'll draft the helper with event decoding and check the raw current against the table's `iox`.

**Agent calls Bash**

```bash
mkdir -p entries/amjad-2025 && cat > entries/amjad-2025/amjad.py <<'EOF'
"""Loading and measures for Amjad et al. (2025) on DANDI:002013.

Every parameter says where it comes from: the claims file (claims/amjad-2025.yaml, which cites the
paper), a passage of the paper (author, step 1.6), an assumption, or a standard choice that cannot
change a result.
"""

import re

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from scipy import signal

DANDISET_ID = "002013"
DANDISET_VERSION = "0.261120.1306"  # the version this attempt was asked to test
API = "https://api.dandiarchive.org/api"

PATHS = {
    "shape": "sub-Monkey-T/sub-Monkey-T_ses-09132024_ecephys.nwb",      # 09/13/2024, FSCV c8dg
    "direction": "sub-Monkey-T/sub-Monkey-T_ses-09262024_ecephys.nwb",  # 09/26/2024, LFP c3bs-c3a
    "monkey_p": "sub-Monkey-P/sub-Monkey-P_ses-08132018_ecephys.nwb",   # 08/13/2018, spikes
}

# Zenodo deposit of the paper's processed data (Data Availability Statement), used by zenodo-link.
ZENODO_RECORD = "14826579"


def assets():
    """Path -> (asset id, size) for every asset of the pinned version."""
    r = requests.get(f"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/",
                     params={"page_size": 100}).json()
    return {a["path"]: (a["asset_id"], a["size"]) for a in r["results"]}


def open_file(path):
    """Stream one NWB file of the pinned version as an h5py File (no download to disk)."""
    asset_id = assets()[path][0]
    url = requests.get(f"{API}/assets/{asset_id}/download/", allow_redirects=False).headers["Location"]
    return h5py.File(remfile.File(url), "r")


def events(f):
    """Events table as {code: sorted times}. The code of each row is read from its description
    ("The event times for code N"), as the labels are names from the trial list's event map."""
    g = f["processing/events/events_table"]
    desc = [d.decode() if isinstance(d, bytes) else d for d in g["event_description"][:]]
    labels = [d.decode() if isinstance(d, bytes) else d for d in g["label"][:]]
    times = g["event_times"][:]
    idx = g["event_times_index"][:]
    out, names = {}, {}
    lo = 0
    for d, lab, hi in zip(desc, labels, idx):
        code = int(re.search(r"code (\d+)", d).group(1))
        out[code] = np.sort(times[lo:hi])
        names[code] = lab
        lo = hi
    return out, names


def decode_trials(ev, n_trials):
    """One row per trial. A trial runs from one "intended trial start" code (128) to the next
    (claims file, method choices). Its value cue is the first code 23 in it. Flags say whether the
    trial holds each condition code."""
    starts = ev[128]
    assert len(starts) == n_trials
    bounds = np.r_[starts, np.inf]
    rows = []
    which = {c: np.searchsorted(bounds, t, side="right") - 1 for c, t in ev.items()}
    for k in range(n_trials):
        row = {"trial": k, "start": starts[k]}
        for c, w in which.items():
            row[f"has_{c}"] = bool(np.any(w == k))
        vc = ev.get(23, np.array([]))[which.get(23, np.array([], int)) == k]
        row["value_cue"] = vc[0] if len(vc) else np.nan
        rows.append(row)
    return pd.DataFrame(rows)
EOF
cat > $TMPDIR/w/dec.py <<'EOF'
import sys; sys.path.insert(0,"entries/amjad-2025")
import amjad as A, numpy as np, pandas as pd
f=A.open_file(A.PATHS["shape"])
ev,names=A.events(f); n=len(f["intervals/trials/id"])
tr=A.decode_trials(ev,n)
mid=f["intervals/trials/midpoint_time"][:]; print("128 == midpoint:", np.allclose(tr.start, mid))
forced=tr.has_119; print("forced", forced.sum(), n, forced.mean())
succ=forced & tr.has_21; print("forced success", succ.sum(), "large", (succ&tr.has_101).sum(), "small", (succ&~tr.has_101).sum(), "has100", tr.has_100.sum() if 'has_100' in tr else None)
print("value cue missing in forced success", tr.value_cue[succ].isna().sum())
print("vc - start", (tr.value_cue-tr.start)[succ].describe())
tr.to_pickle(__import__('os').environ['TMPDIR']+"/w/tr0913.pkl")
EOF
cd $TMPDIR && . scratch/bin/activate && cd - >/dev/null && python $TMPDIR/w/dec.py
```

```
128 == midpoint: True
forced 358 1468 0.2438692098092643
forced success 303 large 164 small 139 has100 None
value cue missing in forced success 0
vc - start count    303.000000
mean       1.972331
std        0.342297
min        1.549078
25%        1.782870
50%        1.849557
75%        2.015967
max        3.565785
dtype: float64
```

**Agent**

Now the raw FSCV current against the table's `iox` (clock check), on a few trials.

**Agent calls Bash**

```bash
cat > $TMPDIR/w/clk.py <<'EOF'
import sys, os, time; sys.path.insert(0,"entries/amjad-2025")
import amjad as A, numpy as np, pandas as pd
W=os.environ['TMPDIR']+"/w/"
f=A.open_file(A.PATHS["shape"])
ss=np.load(W+"scanstarts.npy"); sidx=ss[:,0].astype(int); st=ss[:,1]
tr=pd.read_pickle(W+"tr0913.pkl")
g="processing/fscv/trial_aligned_fscv_table/"
iox=f[g+"iox"]; da=f[g+"da"]; tix=f[g+"trial_index"][:]; t_start=f[g+"start_time"][:]
V=f["stimulus/presentation/fscv_excitation_series/data"][:214]; I=f["acquisition/fscv_response_series/data"]
j06=int(np.argmin(np.abs(V[:107]-0.6))); print("sample at 0.6V", j06, V[j06])
t0=time.time()
for row in [5,50,200,400]:
    k=tix[row]; s0=np.searchsorted(st, t_start[row]-0.05)
    raw=I[sidx[s0]:sidx[s0]+600*214].reshape(600,214)[:,j06]
    tab=iox[row]
    best=[]
    for lag in range(-50,51):
        a=raw[max(0,lag):600+min(0,lag)]; b=tab[max(0,-lag):600-max(0,lag)]
        m=np.isfinite(a)&np.isfinite(b)
        best.append((np.corrcoef(np.diff(a[m]),np.diff(b[m]))[0,1],lag))
    print(row, k, "scan t - start", st[s0]-t_start[row], "best", max(best), "lag0", [b for b in best if b[1]==0])
print(time.time()-t0)
EOF
python $TMPDIR/w/clk.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/w/clk.py", line 2, in <module>
    import amjad as A, numpy as np, pandas as pd
  File "entries/amjad-2025/amjad.py", line 10, in <module>
    import h5py
ModuleNotFoundError: No module named 'h5py'
```

**Agent calls Bash**

```bash
. $TMPDIR/scratch/bin/activate && python $TMPDIR/w/clk.py
```

```
sample at 0.6V 61 0.6077541265082923
5 5 scan t - start -0.04520223424970027 best (np.float64(0.03224073614856838), 1) lag0 [(np.float64(0.02609449968942936), 0)]
50 50 scan t - start 0.04180722730689013 best (np.float64(0.03080323658729834), 6) lag0 [(np.float64(-0.0008235927658632591), 0)]
200 200 scan t - start 0.010129649339432945 best (np.float64(0.022182415148811963), -14) lag0 [(np.float64(0.003026379370067341), 0)]
400 400 scan t - start -0.013406312429651734 best (np.float64(0.03959243395731657), -28) lag0 [(np.float64(0.0053925248850505165), 0)]
1.5395288467407227
```

**Agent**

No match at small lags. I'll read the whole raw current at 0.6 V and search over a wide lag range.

**Agent calls Bash**

```bash
cat > $TMPDIR/w/clk2.py <<'EOF'
import sys, os, time; sys.path.insert(0,"entries/amjad-2025")
import amjad as A, numpy as np, pandas as pd
W=os.environ['TMPDIR']+"/w/"
f=A.open_file(A.PATHS["shape"])
ss=np.load(W+"scanstarts.npy"); st=ss[:,1]
I=f["acquisition/fscv_response_series/data"]
t0=time.time(); col=[]
for a in range(0, I.shape[0], 1250000*4):
    x=I[a:a+1250000*4].reshape(-1,214); col.append(x[:, [61, 40, 150, 107]])
col=np.concatenate(col); print("read", time.time()-t0, col.shape)
np.save(W+"col.npy", col)
g="processing/fscv/trial_aligned_fscv_table/"
iox=f[g+"iox"][:]; t_start=f[g+"start_time"][:]
r=col[:,0]
def hp(x,w=50):  # remove slow drift: minus 5 s moving mean
    k=np.ones(w)/w; return x-np.convolve(x,k,'same')
rh=hp(r)
for row in [5,50,200,400,700]:
    b=iox[row].copy(); m=np.isfinite(b); b[~m]=np.nanmean(b); bh=hp(b)[60:-60]
    s0=np.searchsorted(st, t_start[row])
    res=[]
    for lag in range(-3000,3001):
        a=rh[s0+60+lag:s0+540+lag]
        if len(a)<480: continue
        res.append((np.corrcoef(a,bh)[0,1],lag))
    res.sort(reverse=True); print(row, res[:3], [x for x in res if x[1]==0])
EOF
. $TMPDIR/scratch/bin/activate && python $TMPDIR/w/clk2.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/w/clk2.py", line 9, in <module>
    x=I[a:a+1250000*4].reshape(-1,214); col.append(x[:, [61, 40, 150, 107]])
ValueError: cannot reshape array of size 5000000 into shape (214)
```

**Agent calls Bash**

```bash
sed -i 's/1250000\*4/214*25000/g' $TMPDIR/w/clk2.py && . $TMPDIR/scratch/bin/activate && python $TMPDIR/w/clk2.py
```

```
Exit code 1
read 8.852816104888916 (241200, 4)
Traceback (most recent call last):
  File "/tmp/claude-1001/w/clk2.py", line 25, in <module>
    res.append((np.corrcoef(a,bh)[0,1],lag))
                ~~~~~~~~~~~^^^^^^
  File "/tmp/claude-1001/scratch/lib/python3.13/site-packages/numpy/lib/_function_base_impl.py", line 3029, in corrcoef
    c = cov(x, y, rowvar, dtype=dtype)
  File "/tmp/claude-1001/scratch/lib/python3.13/site-packages/numpy/lib/_function_base_impl.py", line 2837, in cov
    X = np.concatenate((X, y), axis=0)
ValueError: all the input array dimensions except for the concatenation axis must match exactly, but along dimension 1, the array at index 0 has size 480 and the array at index 1 has size 481
```

**Agent calls Bash**

```bash
cd $TMPDIR/w && sed -i 's/\[60:-60\]/[60:540]/' clk2.py && sed -i 's/^t0=time.time(); col=\[\]/col=np.load(W+"col.npy"); t0=time.time()/; s/^for a in range(0, I.shape\[0\].*$/if False:/' clk2.py && sed -i 's/^np.save(W+"col.npy", col)//' clk2.py && . $TMPDIR/scratch/bin/activate && cd  && python $TMPDIR/w/clk2.py
```

```
Exit code 1
read 0.07140588760375977 (964800,)
Traceback (most recent call last):
  File "/tmp/claude-1001/w/clk2.py", line 14, in <module>
    r=col[:,0]
      ~~~^^^^^
IndexError: too many indices for array: array is 1-dimensional, but 2 were indexed
```

**Agent calls Bash**

```bash
cat > $TMPDIR/w/clk3.py <<'EOF'
import sys, os; sys.path.insert(0,"entries/amjad-2025")
import amjad as A, numpy as np
W=os.environ['TMPDIR']+"/w/"
f=A.open_file(A.PATHS["shape"])
st=np.load(W+"scanstarts.npy")[:,1]; col=np.load(W+"col.npy")
g="processing/fscv/trial_aligned_fscv_table/"
iox=f[g+"iox"][:]; da=f[g+"da"][:]; t_start=f[g+"start_time"][:]
def hp(x,w=50): return x-np.convolve(x,np.ones(w)/w,'same')
rh=hp(col[:,0])
for row in [5,50,200,400,700]:
    b=iox[row].copy(); b[~np.isfinite(b)]=np.nanmean(b); bh=hp(b)[60:540]
    s0=np.searchsorted(st, t_start[row]); res=[]
    for lag in range(-3000,3001):
        a=rh[s0+60+lag:s0+540+lag]
        if len(a)==480: res.append((round(np.corrcoef(a,bh)[0,1],3),lag))
    res.sort(reverse=True); print(row, res[:3], [x for x in res if x[1]==0])
print("iox units/range", np.nanpercentile(iox,[1,50,99]), "raw col range", np.percentile(col[:,0],[1,50,99]))
EOF
. $TMPDIR/scratch/bin/activate && python $TMPDIR/w/clk3.py
```

```
5 [(np.float64(0.156), -2426), (np.float64(0.152), -2427), (np.float64(0.143), -2425)] [(np.float64(0.118), 0)]
50 [(np.float64(0.163), -989), (np.float64(0.16), -990), (np.float64(0.158), -988)] [(np.float64(0.124), 0)]
200 [(np.float64(0.157), -2890), (np.float64(0.155), -2891), (np.float64(0.153), -1092)] [(np.float64(0.107), 0)]
400 [(np.float64(0.215), 2996), (np.float64(0.213), 2997), (np.float64(0.208), 2995)] [(np.float64(0.086), 0)]
700 [(np.float64(0.22), 387), (np.float64(0.211), 388), (np.float64(0.208), 386)] [(np.float64(0.043), 0)]
iox units/range [-0.80499345 -0.07305515  0.59860916] raw col range [1145.00569743 1153.0150209  1270.24976768]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/w/redox.py <<'EOF'
import sys, os, time; sys.path.insert(0,"entries/amjad-2025")
import amjad as A, numpy as np, pandas as pd
from scipy import stats
W=os.environ['TMPDIR']+"/w/"
f=A.open_file(A.PATHS["shape"])
st=np.load(W+"scanstarts.npy")[:,1]
tr=pd.read_pickle(W+"tr0913.pkl")
succ=tr.has_119&tr.has_21; large=succ&tr.has_101; small=succ&~tr.has_101
V=f["stimulus/presentation/fscv_excitation_series/data"][:214]
I=f["acquisition/fscv_response_series/data"]
t0=time.time()
allI=np.empty((len(st),214),np.float32)
B=214*25000
for a in range(0,I.shape[0],B): allI[a//214:(a+B)//214]=I[a:a+B].reshape(-1,214)
print("read",time.time()-t0)
def vgram(vc_times, shift=0.0):
    out=[]
    for vc in vc_times+shift:
        r=np.argmin(np.abs(st-vc)); post=(st>=vc+0.5)&(st<=vc+2.0)
        out.append(allI[post].mean(0)-allI[r])
    return np.array(out)
up=np.arange(0,107); down=np.arange(107,214)
print("V up range", V[up].min(), V[up].max(), "down", V[down].max(), V[down].min())
for shift in [0, -5, 5, -10, 10]:
    L=vgram(tr.value_cue[large].values, shift); S=vgram(tr.value_cue[small].values, shift)
    m=L.mean(0); iu=up[np.argmax(m[up])]; idn=down[np.argmin(m[down])]
    j=61
    print(f"shift {shift}: large n={len(L)} max rising at V={V[iu]:.3f} ({m[iu]:.2f}), min falling at V={V[idn]:.3f} ({m[idn]:.2f}); "
          f"0.6V large med {np.median(L[:,j]):.3f} small {np.median(S[:,j]):.3f} p={stats.mannwhitneyu(L[:,j],S[:,j]).pvalue:.3g}")
np.save(W+"allI_shape.npy", allI[:1])  # placeholder
EOF
. $TMPDIR/scratch/bin/activate && python $TMPDIR/w/redox.py
```

```
read 8.53427267074585
V up range -0.34695178890751177 1.3285893231683474 down 1.3394819460648983 -0.3205211734297573
shift 0: large n=164 max rising at V=0.512 (0.07), min falling at V=0.897 (-0.05); 0.6V large med -0.029 small 0.042 p=0.0502
shift -5: large n=164 max rising at V=-0.240 (0.04), min falling at V=0.112 (-0.04); 0.6V large med 0.048 small 0.029 p=0.799
shift 5: large n=164 max rising at V=1.329 (0.03), min falling at V=1.217 (-0.03); 0.6V large med -0.029 small 0.018 p=0.391
shift -10: large n=164 max rising at V=0.864 (0.04), min falling at V=1.308 (-0.05); 0.6V large med -0.025 small -0.012 p=0.0896
shift 10: large n=164 max rising at V=-0.144 (0.04), min falling at V=0.080 (-0.06); 0.6V large med -0.009 small 0.051 p=0.0793
```

**Agent**

Raw FSCV at the stored times: rising-sweep peak at 0.51 V but falling-sweep minimum at 0.90 V, and no large-over-small contrast; shifted labels look the same. Now the trial-aligned dopamine (fig4a).

**Agent calls Bash**

```bash
cat > $TMPDIR/w/f4a.py <<'EOF'
import sys, os; sys.path.insert(0,"entries/amjad-2025")
import amjad as A, numpy as np, pandas as pd
from scipy import stats
W=os.environ['TMPDIR']+"/w/"
f=A.open_file(A.PATHS["shape"])
tr=pd.read_pickle(W+"tr0913.pkl")
g="processing/fscv/trial_aligned_fscv_table/"
T={k:f[g+k][:] for k in ["da","iox","ph","m","trial_index"]}
print("NaN frac da", np.isnan(T["da"]).mean())
tab=tr.iloc[T["trial_index"]].reset_index(drop=True)
succ=(tab.has_119&tab.has_21).values; large=succ&tab.has_101.values
vi=np.rint(300+(tab.value_cue-tab.start).values*10)
print("forced success in table", succ.sum(), "large", large.sum(), "small", (succ&~large).sum())
def measure(x, w=(0,3), reref=True):
    out=[]
    for r in np.where(succ)[0]:
        i=int(vi[r]); y=x[r]-(x[r,i] if reref else 0)
        out.append(np.nanmean(y[i+int(w[0]*10)+ (1 if w[0]==0 else 0): i+int(w[1]*10)+1]))
    return np.array(out)
L=large[succ]
for name,x,w,rr in [("da",T["da"],(0,3),True),("da raw",T["da"],(0,3),False),("iox",T["iox"],(0,3),True),("da 0-1.5",T["da"],(0,1.5),True),("da 1.5-3",T["da"],(1.5,3),True)]:
    v=measure(x,w,rr); a=v[L]; b=v[~L]; a=a[np.isfinite(a)]; b=b[np.isfinite(b)]
    print(name, "large med", np.median(a), "small", np.median(b), "n", len(a), len(b), "p", stats.mannwhitneyu(a,b).pvalue)
# fig3a single-site: fraction of large forced trials with positive change
v=measure(T["da"]); print("frac positive large", np.mean(v[L]>0))
# shifted labels within table: random shift of vc
for sh in [-10,-5,5,10]:
    vi0=vi.copy(); vi[:]=vi0+sh*10; v=measure(T["da"]); a=v[L];b=v[~L]
    print("shift",sh, np.nanmedian(a)-np.nanmedian(b), stats.mannwhitneyu(a[np.isfinite(a)],b[np.isfinite(b)]).pvalue); vi[:]=vi0
EOF
. $TMPDIR/scratch/bin/activate && python $TMPDIR/w/f4a.py
```

```
/tmp/claude-1001/w/f4a.py:18: RuntimeWarning: Mean of empty slice
  out.append(np.nanmean(y[i+int(w[0]*10)+ (1 if w[0]==0 else 0): i+int(w[1]*10)+1]))
NaN frac da 0.02659055978455526
forced success in table 168 large 87 small 81
da large med 1.3667422986040783 small 0.1906372757474719 n 85 80 p 0.022565683092877577
da raw large med -3.3725688685853594 small -3.8345072617438585 n 87 81 p 0.2977996236106464
iox large med -0.015111245365418805 small -0.0005452614625445069 n 87 81 p 0.4461632465843963
da 0-1.5 large med 0.42506435860896025 small 0.016720668852026024 n 85 80 p 0.3336772178256613
da 1.5-3 large med 1.916600850447633 small 0.6916215633771161 n 84 80 p 0.006355470892150884
frac positive large 0.6436781609195402
shift -10 -0.21309244513053838 0.4886270527964037
shift -5 0.003978404810912384 0.9457282120081306
shift 5 -0.4374836536785318 0.46410739210367735
shift 10 -0.8897580180746653 0.0057728987531306805
```

**Agent**

fig4a: re-referenced `da` is higher after large-reward cues (median 1.37 vs 0.19, p = 0.023). Now the 09/26 LFP session and the Zenodo trial lists.

**Agent calls Bash**

```bash
cd $TMPDIR/w && for n in "09262024_trialids_value%20object%20start_big%20rew%20and%20success_tr1-1501.mat" "09262024_trialids_value%20object%20start_small%20rew%20and%20success_tr1-1501.mat" "09262024_trialids_value%20object%20start_left%20and%20success_tr1-1501.mat" "09262024_trialids_value%20object%20start_right%20and%20success_tr1-1501.mat" "09262024_c3bs-c3a_data_trial35bigrewardexample.mat"; do curl -sL -o "z_$(echo $n | cut -c1-60 | tr -d '%').mat" "https://zenodo.org/api/records/14826579/files/$n/content"; done; ls -la z_*; . $TMPDIR/scratch/bin/activate; python -c "
import scipy.io as s, glob, numpy as np
for fn in sorted(glob.glob('z_*.mat')):
    d=s.loadmat(fn, squeeze_me=True); print(fn, {k:(getattr(v,'shape',None), getattr(v,'dtype',None)) for k,v in d.items() if not k.startswith('__')})
    for k,v in d.items():
        if not k.startswith('__'): print('   ', k, np.ravel(v)[:12] if getattr(v,'dtype',None)!=object else v)
"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cat > $TMPDIR/w/lfp.py <<'EOF'
import sys, os, time; sys.path.insert(0,"entries/amjad-2025")
import amjad as A, numpy as np, pandas as pd, scipy.io as sio
from scipy import signal, stats
W=os.environ['TMPDIR']+"/w/"
f=A.open_file(A.PATHS["direction"])
t0=time.time()
x=f["processing/ecephys/FilteredEphys/bipolar_lfp_series/data"][:,0]; t=f["processing/ecephys/FilteredEphys/bipolar_lfp_series/timestamps"][:]
print("read", time.time()-t0, x.shape, np.percentile(x,[0.1,50,99.9]), "nan", np.isnan(x).sum())
d=np.diff(t); print("dt", np.percentile(d,[0,50,100]), "gaps>1.5ms", (d>0.0015).sum(), t[0], t[-1])
gi=np.where(d>0.0015)[0]; print(gi[:10], d[gi[:10]])
ev,names=A.events(f); n=len(f["intervals/trials/id"]); tr=A.decode_trials(ev,n)
tr["success"]=tr.has_100|tr.has_101
print("success", tr.success.sum(), "large", (tr.success&tr.has_101).sum(), "small", (tr.success&tr.has_100).sum(), "both", (tr.has_100&tr.has_101).sum(),
 "left",(tr.success&tr.has_117).sum(),"right",(tr.success&tr.has_118).sum(), "feedback&!succ", (tr.has_21&~tr.success).sum())
tr.to_pickle(W+"tr0926.pkl"); np.save(W+"lfp.npy", np.c_[t,x])
EOF
. $TMPDIR/scratch/bin/activate && python $TMPDIR/w/lfp.py
```

```
read 4.811906814575195 (19246352,) [-5.03680415e-04 -7.94809915e-06  8.98161283e-04] nan 0
dt [0.0005 0.001  0.0015] gaps>1.5ms 1 5719.053511 24965.400297
[9885874] [0.0015]
success 1172 large 570 small 602 both 0 left 594 right 578 feedback&!succ 0
```

**Agent calls Bash**

```bash
cat > $TMPDIR/w/beta.py <<'EOF'
import sys, os, time, glob; sys.path.insert(0,"entries/amjad-2025")
import numpy as np, pandas as pd, scipy.io as sio
from scipy import signal, stats
W=os.environ['TMPDIR']+"/w/"
tr=pd.read_pickle(W+"tr0926.pkl"); tx=np.load(W+"lfp.npy"); t=tx[:,0]; x=tx[:,1]
Z={k:sio.loadmat(glob.glob(W+f"z_*{k}*.mat")[0],squeeze_me=True)["trids_out"] for k in ["big","small","left","right"]}
mine={"big":tr.success&tr.has_101,"small":tr.success&tr.has_100,"left":tr.success&tr.has_117,"right":tr.success&tr.has_118}
for k in Z:
    a=set(Z[k].tolist()); b=set((np.where(mine[k])[0]+1).tolist())
    print(k, len(a), len(b), "both", len(a&b), "only zenodo", sorted(a-b)[:10], "only here", sorted(b-a)[:10])
t0=time.time()
b,a=signal.butter(4,[13,28],btype="bandpass",fs=1000)
y=signal.filtfilt(b,a,x); env=np.abs(signal.hilbert(y))**2
w=np.hanning(250); w/=w.sum(); bp=np.convolve(env,w,"same")
print("beta", time.time()-t0)
np.save(W+"bp.npy", bp)
ex=sio.loadmat(glob.glob(W+"z_*example*.mat")[0],squeeze_me=True)
k=Z["big"][34]-1; vc=tr.value_cue[k]; print("trial", k+1, "vc", vc)
i0=np.searchsorted(t, vc-3); seg=bp[i0:i0+15001]; ref=ex["trial35bigrewardataBetaPower"]
for lag in [0]:
    pass
res=[(np.corrcoef(bp[i0+L:i0+L+15001],ref)[0,1],L) for L in range(-200,201)]
print("lag0 r", np.corrcoef(seg,ref)[0,1], "best", max(res), "ratio", np.median(seg/ref))
print("is 'data' == TS:", np.array_equal(ex["trial35bigrewardata"], ex["trial35bigrewardataTS"]))
EOF
. $TMPDIR/scratch/bin/activate && python $TMPDIR/w/beta.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/w/beta.py", line 6, in <module>
    Z={k:sio.loadmat(glob.glob(W+f"z_*{k}*.mat")[0],squeeze_me=True)["trids_out"] for k in ["big","small","left","right"]}
         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
KeyError: 'trids_out'
```

**Agent calls Bash**

```bash
sed -i 's/z_\*{k}\*.mat/z_*start_{k}*.mat/' $TMPDIR/w/beta.py && . $TMPDIR/scratch/bin/activate && python $TMPDIR/w/beta.py
```

```
big 569 570 both 569 only zenodo [] only here [1501]
small 602 602 both 602 only zenodo [] only here []
left 594 594 both 594 only zenodo [] only here []
right 577 578 both 577 only zenodo [] only here [1501]
beta 3.0254788398742676
trial 84 vc 6847.825767
lag0 r 0.942107589461277 best (np.float64(0.9427475135116132), 6) ratio 0.9427662369585176
is 'data' == TS: True
```

**Agent**

Zenodo lists agree (one extra trial, 1501, in this dataset's large and right lists) and the example beta trace correlates at r = 0.94, lag 6 ms. Now fig4b, fig4c and the burst claim.

**Agent calls Bash**

```bash
cat > $TMPDIR/w/f4.py <<'EOF'
import sys, os; sys.path.insert(0,"entries/amjad-2025")
import numpy as np, pandas as pd
from scipy import stats
W=os.environ['TMPDIR']+"/w/"
tr=pd.read_pickle(W+"tr0926.pkl"); t=np.load(W+"lfp.npy")[:,0]; bp=np.load(W+"bp.npy")
s=tr[tr.success]; vc=s.value_cue.values; i0=np.searchsorted(t,vc)
print("vc nan", np.isnan(vc).sum())
def win(a,b): return np.array([bp[i+int(a*1000):i+int(b*1000)].mean() for i in i0])
def basel(): return np.array([bp[i-500:i].mean() for i in i0])
L=s.has_101.values; left=s.has_117.values
for nm,(a,b) in {"0-0.5":(0,.5),"0-1":(0,1),".25-.75":(.25,.75)}.items():
    for norm in [False,True]:
        v=win(a,b)/(basel() if norm else 1)
        p=stats.mannwhitneyu(v[L],v[~L]).pvalue; p2=stats.mannwhitneyu(v[L&left],v[L&~left]).pvalue
        print(nm,"norm" if norm else "", f"large {np.median(v[L]):.3g} small {np.median(v[~L]):.3g} p={p:.3g} | left {np.median(v[L&left]):.3g} right {np.median(v[L&~left]):.3g} p={p2:.3g}")
# bursts
mid=tr.start.values  # code 128
mask=np.zeros(len(bp),bool)
for m in mid:
    a,b=np.searchsorted(t,[m-30,m+30]); mask[a:b]=True
for q in [75,50,90]:
    thr=np.percentile(bp[mask],q); above=bp>thr
    edges=np.diff(np.r_[0,above.astype(int),0]); on=np.where(edges==1)[0]; off=np.where(edges==-1)[0]
    keep=(off-on)>=50; on=on[keep]
    sl=s[s.has_101]; ii=np.searchsorted(t,sl.value_cue.values)
    pre=np.array([((on>=i-1000)&(on<i)).sum() for i in ii]); post=np.array([((on>=i)&(on<i+1000)).sum() for i in ii])
    print(q, "thr", thr, "pre mean", pre.mean(), "post", post.mean(), "wilcoxon p", stats.wilcoxon(pre,post).pvalue, "n", len(ii))
EOF
. $TMPDIR/scratch/bin/activate && python $TMPDIR/w/f4.py; date -u
```

```
vc nan 0
0-0.5  large 2.75e-10 small 3.27e-10 p=1.03e-08 | left 2.45e-10 right 3.02e-10 p=1.61e-06
0-0.5 norm large 0.455 small 0.553 p=1.09e-06 | left 0.389 right 0.546 p=2.07e-09
0-1  large 3.24e-10 small 3.11e-10 p=0.09 | left 3.07e-10 right 3.41e-10 p=0.0188
0-1 norm large 0.556 small 0.515 p=0.0723 | left 0.493 right 0.601 p=0.000136
.25-.75  large 2.13e-10 small 2.14e-10 p=0.658 | left 2.14e-10 right 2.1e-10 p=0.75
.25-.75 norm large 0.367 small 0.356 p=0.794 | left 0.344 right 0.393 p=0.0751
75 thr 3.562033143446841e-10 pre mean 1.512280701754386 post 1.207017543859649 wilcoxon p 9.470661770132047e-10 n 570
50 thr 1.5919906919062757e-10 pre mean 0.6947368421052632 post 1.4210526315789473 wilcoxon p 2.496375634122597e-47 n 570
90 thr 6.786568944482189e-10 pre mean 1.475438596491228 post 0.6614035087719298 wilcoxon p 2.400067939203724e-45 n 570
Tue Nov 24 23:03:33 UTC 2026
```

**Agent**

fig4b, fig4c and the burst test all come out as the claims expect. Next, clock checks: raw 09/26 ephys against the bipolar LFP, and Monkey P spikes against the raw signal.

**Agent calls Bash**

```bash
cat > $TMPDIR/w/rawclk.py <<'EOF'
import sys, os, time; sys.path.insert(0,"entries/amjad-2025")
import amjad as A, numpy as np
from scipy import signal
W=os.environ['TMPDIR']+"/w/"
f=A.open_file(A.PATHS["direction"])
es=f["acquisition/electrical_series"]; rate=es["starting_time"].attrs["rate"]; t0=es["starting_time"][()]
print("raw start", t0, "rate", rate, "n", es["data"].shape, "dur", es["data"].shape[0]/rate, "chunks", es["data"].chunks)
tb=np.load(W+"lfp.npy"); t=tb[:,0]; x=tb[:,1]
b,a=signal.butter(4,[13,28],btype="bandpass",fs=1000)
for T in [8000.0, 15000.0, 22000.0]:
    i=int((T-t0)*rate); n=int(60*rate)
    r=es["data"][i:i+n,:].astype(float)*es["data"].attrs["conversion"]
    bip=r[:,0]-r[:,1]
    # downsample to 1 kHz on the raw clock
    tr_=t0+(i+np.arange(n))/rate
    bl=signal.sosfiltfilt(signal.butter(4,400,fs=rate,output="sos"),bip)
    grid=np.arange(T+1,T+59,0.001); rr=np.interp(grid,tr_,bl); ll=np.interp(grid,t,x)
    rf=signal.filtfilt(b,a,rr); lf=signal.filtfilt(b,a,ll)
    lags=np.arange(-3000,3001); c=[np.corrcoef(rf[3000+L:-3000+L], lf[3000:-3000])[0,1] for L in lags]
    k=int(np.argmax(c)); print(T, "best lag ms", lags[k], "r", round(c[k],3), "r at 0", round(c[3000],3), "amp ratio", np.std(rr)/np.std(ll))
EOF
. $TMPDIR/scratch/bin/activate && python $TMPDIR/w/rawclk.py
```

```
Exit code 1
raw start 2631.34465 rate 31999.962403839356 n (722978367, 2) dur 22593.100512932386 chunks (2500000, 2)
Traceback (most recent call last):
  File "/tmp/claude-1001/w/rawclk.py", line 19, in <module>
    lags=np.arange(-3000,3001); c=[np.corrcoef(rf[3000+L:-3000+L], lf[3000:-3000])[0,1] for L in lags]
                                   ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/scratch/lib/python3.13/site-packages/numpy/lib/_function_base_impl.py", line 3029, in corrcoef
    c = cov(x, y, rowvar, dtype=dtype)
  File "/tmp/claude-1001/scratch/lib/python3.13/site-packages/numpy/lib/_function_base_impl.py", line 2837, in cov
    X = np.concatenate((X, y), axis=0)
ValueError: all the input array dimensions except for the concatenation axis must match exactly, but along dimension 1, the array at index 0 has size 0 and the array at index 1 has size 52000
```

**Agent calls Bash**

```bash
sed -i 's/c=\[np.corrcoef(rf\[3000+L:-3000+L\], lf\[3000:-3000\])\[0,1\] for L in lags\]/N=len(rf); c=[np.corrcoef(rf[3000+L:N-3000+L], lf[3000:N-3000])[0,1] for L in lags]/' $TMPDIR/w/rawclk.py && . $TMPDIR/scratch/bin/activate && python $TMPDIR/w/rawclk.py
```

```
raw start 2631.34465 rate 31999.962403839356 n (722978367, 2) dur 22593.100512932386 chunks (2500000, 2)
8000.0 best lag ms 1 r 0.748 r at 0 0.748 amp ratio 1.0290932012226057
15000.0 best lag ms 0 r 0.74 r at 0 0.74 amp ratio 1.036479708502
22000.0 best lag ms 0 r 0.709 r at 0 0.709 amp ratio 1.0293403185022485
```

**Agent**

Raw ephys and the bipolar LFP share a clock (lag 0 to 1 ms, r about 0.74). Now Monkey P.

**Agent calls Bash**

```bash
cat > $TMPDIR/w/mp.py <<'EOF'
import sys, os, time; sys.path.insert(0,"entries/amjad-2025")
import amjad as A, numpy as np
from scipy import signal
f=A.open_file(A.PATHS["monkey_p"])
es=f["acquisition/electrical_series"]; T=es["timestamps"]; print("chunks", es["data"].chunks, T.chunks)
t0=time.time(); ts=T[:]; print("ts read", time.time()-t0)
d=np.diff(ts); print("dt pct", np.percentile(d,[0,50,100]), "gaps", (d>1.5/30000).sum(), ts[0], ts[-1], "1/median", 1/np.median(d))
gi=np.where(d>1.5/30000)[0]; print("gap sizes", np.round(d[gi][:10],4), len(gi))
u=f["units"]; idx=u["spike_times_index"][:]; st=u["spike_times"][:]; names=u["unit_name"][:]
s1=st[idx[0]:idx[1]]; print(names, len(s1), "first", s1[:3])
isi=np.diff(s1)*1000; print("ISI<1ms frac", np.mean(isi<1), "<1.5", np.mean(isi<1.5), "median", np.median(isi), "sorted", np.all(isi>=0))
tu=f["processing/ecephys/thresholded_units"]; tidx=tu["spike_times_index"][:]; tst=tu["spike_times"][:]; tn=tu["unit_name"][:]
w=tu["waveforms"]; wi=tu["waveforms_index"][:]; wii=tu["waveforms_index_index"][:]
print(tn, tidx, wii, wi[:3])
u1=tst[tidx[1]:tidx[2]]; print("thresholded unit1 equals units#1", np.array_equal(u1, s1))
lo=wi[tidx[1]-1] if tidx[1]>0 else 0; hi=wi[tidx[2]-1]
W1=w[lo:hi,0].reshape(-1,48); print("waveforms", W1.shape, "mean trough uV", W1.mean(0).min()*1e6, "peak", W1.mean(0).max()*1e6, "argmin", W1.mean(0).argmin())
np.save(os.environ['TMPDIR']+"/w/mp_ts.npy", ts); np.save(os.environ['TMPDIR']+"/w/mp_s1.npy", s1); np.save(os.environ['TMPDIR']+"/w/mp_w1.npy", W1.mean(0))
EOF
. $TMPDIR/scratch/bin/activate && python $TMPDIR/w/mp.py
```

```
chunks (5000000, 1) (1250000,)
ts read 47.544941425323486
dt pct [3.26666632e-05 3.33333337e-05 9.83333333e-03] gaps 19 6800.665797 18786.083118 1/median 29999.999666470107
gap sizes [0.0094 0.0014 0.0014 0.0023 0.0007 0.0019 0.0001 0.0023 0.0015 0.0076] 19
[b'ch33#0' b'ch33#1'] 31247 first [6800.750629 6800.977929 6801.360396]
ISI<1ms frac 3.200409652435512e-05 <1.5 0.00016002048262177558 median 90.25049999945622 sorted True
[b'-1' b'0' b'1'] [10878 30758 62005] [10878 30758 62005] [ 48  96 144]
thresholded unit1 equals units#1 True
waveforms (31247, 48) mean trough uV -30.64031798689871 peak 17.932581531268653 argmin 9
```

**Agent calls Bash**

```bash
cat > $TMPDIR/w/mp2.py <<'EOF'
import sys, os, time; sys.path.insert(0,"entries/amjad-2025")
import amjad as A, numpy as np
from scipy import signal
W=os.environ['TMPDIR']+"/w/"
f=A.open_file(A.PATHS["monkey_p"])
es=f["acquisition/electrical_series"]; conv=es["data"].attrs["conversion"]
s1=np.load(W+"mp_s1.npy"); w1=np.load(W+"mp_w1.npy")
sos=signal.butter(4,[300,6000],btype="bandpass",fs=30000,output="sos")
for start in [0, 150_000_000, 300_000_000]:
    t0=time.time()
    r=es["data"][start:start+18_000_000,0].astype(float)*conv; ts=es["timestamps"][start:start+18_000_000]
    y=signal.sosfiltfilt(sos,r); noise=np.median(np.abs(y-np.median(y)))/0.6745
    print(start, "read+filter", round(time.time()-t0,1), "noise uV", noise*1e6, "trough/noise", -w1.min()/noise, "raw range uV", r.min()*1e6, r.max()*1e6)
    sp=s1[(s1>ts[100])&(s1<ts[-100])]; ii=np.searchsorted(ts,sp)
    # STA at lags
    best=[]
    for lag in range(-60,61):
        sta=np.mean([y[i+lag-9:i+lag+39] for i in ii[(ii+lag>60)&(ii+lag<len(y)-60)]],axis=0)
        best.append((np.corrcoef(sta,w1)[0,1], lag, sta.min()*1e6))
    b=max(best); print("  spikes", len(ii), "best lag samples", b[1], "r", round(b[0],3), "STA trough uV", round(b[2],1), "r at 0", [round(x[0],3) for x in best if x[1]==0])
EOF
. $TMPDIR/scratch/bin/activate && python $TMPDIR/w/mp2.py
```

```
0 read+filter 6.6 noise uV 6.6947041147296895 trough/noise 4.576799431581133 raw range uV -999.9694824218751 999.9694824218751
  spikes 1195 best lag samples 3 r 0.699 STA trough uV -34.9 r at 0 [np.float64(0.44)]
150000000 read+filter 4.4 noise uV 5.453862105875721 trough/noise 5.618095469243411 raw range uV -401.153564453125 999.9694824218751
  spikes 1868 best lag samples 3 r 0.711 STA trough uV -35.5 r at 0 [np.float64(0.465)]
300000000 read+filter 4.4 noise uV 5.566089062343311 trough/noise 5.504819927189452 raw range uV -945.4345703125 999.9694824218751
  spikes 792 best lag samples 3 r 0.729 STA trough uV -35.5 r at 0 [np.float64(0.496)]
```

**Agent**

Spikes sit on the raw clock (STA trough -35 µV, best lag 3 samples = 0.1 ms). Now the shape-task block structure.

**Agent calls Bash**

```bash
cat > $TMPDIR/w/blk.py <<'EOF'
import os, numpy as np, pandas as pd
W=os.environ['TMPDIR']+"/w/"
tr=pd.read_pickle(W+"tr0913.pkl")
fs=tr[tr.has_119&tr.has_21]
print("forced succ with 81,88:", pd.crosstab(fs.has_81, fs.has_88))
print("choice trials with both images", (tr.has_120 & tr.has_81 & tr.has_88).sum(), tr.has_120.sum())
img=np.where(fs.has_81,81,88); large=fs.has_101.values
big_img=np.where(large, img, np.where(img==81,88,81))
seq=pd.Series(big_img,index=fs.trial.values)
print(seq.values[:60])
ch=np.where(np.diff(big_img)!=0)[0]; print("changes", len(ch), list(zip(seq.index[ch], seq.index[ch+1])))
EOF
. $TMPDIR/scratch/bin/activate && python $TMPDIR/w/blk.py
```

```
forced succ with 81,88: has_88  False  True 
has_81              
False       0    161
True      142      0
choice trials with both images 1110 1110
[81 81 81 81 81 81 81 81 81 81 81 81 81 81 81 81 81 81 81 81 81 88 88 88
 88 88 88 88 88 88 88 88 88 88 88 88 88 88 88 88 88 88 88 88 88 88 88 88
 88 88 88 88 88 88 88 81 81 81 81 81]
changes 9 [(60, 69), (232, 243), (385, 391), (506, 515), (577, 591), (771, 782), (864, 866), (1000, 1017), (1273, 1297)]
```

**Agent**

Blocks are 71 to 273 trials and forced trials 24.4%. Before deciding the raw-FSCV claim, a session-wide lag search between the raw current and the table's `iox`.

**Agent calls Bash**

```bash
cat > $TMPDIR/w/glag.py <<'EOF'
import sys, os; sys.path.insert(0,"entries/amjad-2025")
import amjad as A, numpy as np
from scipy import signal
W=os.environ['TMPDIR']+"/w/"
f=A.open_file(A.PATHS["shape"])
st=np.load(W+"scanstarts.npy")[:,1]; col=np.load(W+"col.npy")
g="processing/fscv/trial_aligned_fscv_table/"
iox=f[g+"iox"][:]; ts=f[g+"start_time"][:]
tab=np.zeros(len(st)); cnt=np.zeros(len(st))
for r in range(len(ts)):
    s0=np.searchsorted(st,ts[r]); d=np.diff(iox[r]); d[~np.isfinite(d)]=0
    n=min(599,len(st)-s0-1); tab[s0+1:s0+1+n]+=d[:n]; cnt[s0+1:s0+1+n]+=1
tab[cnt>0]/=cnt[cnt>0]
for c,name in [(0,"0.6V"),(1,"~0.25V"),(2,"falling"),(3,"top")]:
    raw=np.r_[0,np.diff(col[:,c])]; raw=raw-np.mean(raw)
    m=cnt>0
    xc=signal.fftconvolve(raw, (tab*m)[::-1], mode="full"); lags=np.arange(-len(st)+1,len(st))
    sel=np.abs(lags)<=20000; xs=xc[sel]; ls=lags[sel]
    z=(xs-np.median(xs))/np.std(xs); k=np.argmax(np.abs(z)); print(name, "best lag (scans)", ls[k], "z", round(z[k],1), "z at 0", round(z[ls==0][0],1))
EOF
. $TMPDIR/scratch/bin/activate && python $TMPDIR/w/glag.py
```

```
0.6V best lag (scans) -1 z 19.4 z at 0 18.4
~0.25V best lag (scans) -1 z 18.4 z at 0 16.5
falling best lag (scans) -9 z -11.1 z at 0 -3.8
top best lag (scans) 4 z 10.0 z at 0 -3.6
```

**Agent**

Session-wide, the raw 0.6 V current tracks the table's `iox` at lag 0 to 1 scan (z about 19), so the raw FSCV is on the trial clock. I have every result I need. Writing the helper module now.

**Agent calls Write**

```json
{
 "file_path": "entries/amjad-2025/amjad.py",
 "content": "\"\"\"Loading and measures for Amjad et al. (2025) on DANDI:002013.\n\nEvery parameter says where it comes from: the claims file (claims/amjad-2025.yaml, which cites the\npaper), a passage of the paper (author, step 1.6), an assumption, or a standard choice that cannot\nchange a result.\n\"\"\"\n\nimport io\nimport re\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nimport requests\nimport scipy.io\nfrom scipy import signal\n\nDANDISET_ID = \"002013\"\nDANDISET_VERSION = \"0.261120.1306\"  # the version this attempt was asked to test\nAPI = \"https://api.dandiarchive.org/api\"\n\nPATHS = {\n    \"shape\": \"sub-Monkey-T/sub-Monkey-T_ses-09132024_ecephys.nwb\",      # 09/13/2024, FSCV c8dg\n    \"direction\": \"sub-Monkey-T/sub-Monkey-T_ses-09262024_ecephys.nwb\",  # 09/26/2024, LFP c3bs-c3a\n    \"monkey_p\": \"sub-Monkey-P/sub-Monkey-P_ses-08132018_ecephys.nwb\",   # 08/13/2018, spikes\n}\n\n# Zenodo deposit of the paper's processed data (Data Availability Statement,\n# doi:10.5281/zenodo.14826579), used by zenodo-link only.\nZENODO_RECORD = \"14826579\"\nZENODO_LISTS = {\n    \"large\": \"09262024_trialids_value object start_big rew and success_tr1-1501.mat\",\n    \"small\": \"09262024_trialids_value object start_small rew and success_tr1-1501.mat\",\n    \"left\": \"09262024_trialids_value object start_left and success_tr1-1501.mat\",\n    \"right\": \"09262024_trialids_value object start_right and success_tr1-1501.mat\",\n}\nZENODO_EXAMPLE = \"09262024_c3bs-c3a_data_trial35bigrewardexample.mat\"\n\n# Event codes, from the claims file's method choices (the events table names each code in its\n# description).\nTRIAL_START = 128       # \"intended trial start\"; a trial runs from one to the next\nVALUE_CUE = 23          # \"value object start\"; the first one in a trial is its value cue\nFEEDBACK = 21\nBIG_REWARD, SMALL_REWARD = 101, 100\nLEFT, RIGHT = 117, 118\nFORCED = 119\nIMAGES = (81, 88)\n\nFSCV_RATE = 10.0        # trial-aligned FSCV table, 10 Hz; trial start at sample 300 (claims file)\nFSCV_T0_SAMPLE = 300\nLFP_RATE = 1000.0       # bipolar LFP, 1 kHz (paper, Methods, FSCV and EPhys Recordings, para 4)\n\n\ndef assets():\n    \"\"\"Path -> (asset id, size) for every asset of the pinned version.\"\"\"\n    r = requests.get(f\"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/\",\n                     params={\"page_size\": 100}).json()\n    return {a[\"path\"]: (a[\"asset_id\"], a[\"size\"]) for a in r[\"results\"]}\n\n\ndef open_file(path):\n    \"\"\"Stream one NWB file of the pinned version as an h5py File (no download to disk).\"\"\"\n    asset_id = assets()[path][0]\n    url = requests.get(f\"{API}/assets/{asset_id}/download/\", allow_redirects=False).headers[\"Location\"]\n    return h5py.File(remfile.File(url), \"r\")\n\n\ndef _str(x):\n    return x.decode() if isinstance(x, bytes) else str(x)\n\n\ndef events(f):\n    \"\"\"Events table as ({code: sorted times}, {code: label}). The code of each row is read from its\n    description (\"The event times for code N\").\"\"\"\n    g = f[\"processing/events/events_table\"]\n    desc = [_str(d) for d in g[\"event_description\"][:]]\n    labels = [_str(d) for d in g[\"label\"][:]]\n    times = g[\"event_times\"][:]\n    idx = g[\"event_times_index\"][:]\n    out, names, lo = {}, {}, 0\n    for d, lab, hi in zip(desc, labels, idx):\n        code = int(re.search(r\"code (\\d+)\", d).group(1))\n        out[code] = times[lo:hi]\n        names[code] = lab\n        lo = hi\n    return out, names\n\n\ndef decode_trials(ev, n_trials):\n    \"\"\"One row per trial: its start (code 128), its value cue (first code 23 in it) and, for each\n    code, whether the trial holds it (`has_<code>`). A trial runs from one code 128 to the next\n    (claims file, method choices).\"\"\"\n    starts = np.sort(ev[TRIAL_START])\n    assert len(starts) == n_trials\n    bounds = np.r_[starts, np.inf]\n    which = {c: np.searchsorted(bounds, np.sort(t), side=\"right\") - 1 for c, t in ev.items()}\n    cols = {\"trial\": np.arange(n_trials), \"start\": starts}\n    for c, w in which.items():\n        has = np.zeros(n_trials, bool)\n        has[w[(w >= 0) & (w < n_trials)]] = True\n        cols[f\"has_{c}\"] = has\n    vc = np.full(n_trials, np.nan)\n    t23, w23 = np.sort(ev[VALUE_CUE]), which[VALUE_CUE]\n    for t, w in zip(t23[::-1], w23[::-1]):   # reversed, so the first code 23 of a trial is kept\n        if 0 <= w < n_trials:\n            vc[w] = t\n    cols[\"value_cue\"] = vc\n    return pd.DataFrame(cols)\n\n\n# ---------------------------------------------------------------------------- FSCV (09/13/2024)\n\ndef fscv_scans(f):\n    \"\"\"Raw FSCV current and applied voltage reshaped to one row per scan. Scans are the runs of\n    samples between gaps in the timestamps (214 samples at 25 kHz each). Returns\n    (scan start times, current [scans x samples] in nA, voltage of the first scan in V,\n    sampling interval in s). The current is read in blocks of whole scans to keep memory low.\"\"\"\n    ts_ds = f[\"acquisition/fscv_response_series/timestamps\"]\n    ts = ts_ds[:]\n    gaps = np.where(np.diff(ts) > 1e-3)[0]\n    starts = np.r_[0, gaps + 1]\n    lengths = np.diff(np.r_[starts, len(ts)])\n    n = int(np.median(lengths))\n    assert (lengths == n).all(), \"scans of unequal length\"\n    dt = float(np.median(np.diff(ts[:n])))\n    t_scan = ts[starts]\n    del ts\n    data = f[\"acquisition/fscv_response_series/data\"]\n    conv = data.attrs[\"conversion\"] / 1e-9           # to nA\n    cur = np.empty((len(starts), n), np.float32)\n    block = n * 25000\n    for a in range(0, data.shape[0], block):\n        cur[a // n:(a + block) // n] = data[a:a + block].reshape(-1, n) * conv\n    volt = f[\"stimulus/presentation/fscv_excitation_series/data\"][:n]\n    return t_scan, cur, volt, dt\n\n\ndef waveform_parameters(volt, t_scan, dt):\n    \"\"\"Lowest and highest applied potential, sweep rate and scan frequency (fscv-waveform\n    criterion: sweep rate = median absolute step of the rising ramp x sampling rate; scan frequency\n    = 1 / median interval between scan starts).\"\"\"\n    top = int(np.argmax(volt))\n    rising = volt[:top + 1]\n    return {\n        \"lowest_V\": float(volt.min()),\n        \"highest_V\": float(volt.max()),\n        \"sweep_V_per_s\": float(np.median(np.abs(np.diff(rising))) / dt),\n        \"scan_Hz\": float(1 / np.median(np.diff(t_scan))),\n    }\n\n\ndef voltammograms(t_scan, cur, cue_times, post=(0.5, 2.0)):\n    \"\"\"Background-subtracted voltammogram per trial: mean of the scans starting `post` s after the\n    cue minus the scan nearest the cue (fig3a-redox-peaks criterion).\"\"\"\n    out = []\n    for c in cue_times:\n        ref = int(np.argmin(np.abs(t_scan - c)))\n        sel = (t_scan >= c + post[0]) & (t_scan <= c + post[1])\n        out.append(cur[sel].mean(0) - cur[ref])\n    return np.array(out)\n\n\ndef fscv_table(f):\n    g = f[\"processing/fscv/trial_aligned_fscv_table\"]\n    return {k: g[k][:] for k in [\"da\", \"iox\", \"ph\", \"m\", \"trial_index\", \"start_time\", \"stop_time\",\n                                 \"good\", \"rate\"]}\n\n\ndef cue_sample(trials_rows):\n    \"\"\"Sample of the value cue in the trial-aligned series: trial start (code 128) at sample 300,\n    10 Hz, nearest sample (claims file, method choices).\"\"\"\n    return np.rint(FSCV_T0_SAMPLE + (trials_rows.value_cue.values - trials_rows.start.values)\n                   * FSCV_RATE).astype(int)\n\n\ndef window_mean(x, i_cue, window, reref=True):\n    \"\"\"Mean of a 10 Hz trial-aligned series over `window` s after the cue, re-referenced to the\n    sample at the cue (claims file: the Methods background-subtract at the value cue). The window\n    takes the samples after the cue up to and including its end (0 to 3 s is samples +1 to +30); a\n    standard choice. NaN samples are left out (claims file); a trial whose cue sample is NaN has\n    no re-referenced value and is dropped.\"\"\"\n    a = int(round(window[0] * FSCV_RATE)) + (1 if window[0] == 0 else 0)\n    b = int(round(window[1] * FSCV_RATE)) + 1\n    out = np.full(len(x), np.nan)\n    for r, i in enumerate(i_cue):\n        y = x[r] - (x[r, i] if reref else 0.0)\n        seg = y[i + a:i + b]\n        if np.isfinite(seg).any():\n            out[r] = np.nanmean(seg)\n    return out\n\n\n# ------------------------------------------------------------------------ LFP (09/26/2024)\n\ndef beta_power(x, fs=LFP_RATE):\n    \"\"\"Beta power of the continuous bipolar LFP: 13 to 28 Hz 4th-order Butterworth run forwards and\n    backwards, squared Hilbert envelope, smoothed with a 0.25 s Hanning window of unit sum\n    (claims file, method choices; paper, Methods: \"bandpass filtered around 13 to 28 Hz, squared,\n    enveloped, and then smoothed with a Hanning window of 0.25 s\"). Unit sum keeps the units V^2.\"\"\"\n    b, a = signal.butter(4, [13, 28], btype=\"bandpass\", fs=fs)\n    y = signal.filtfilt(b, a, x)\n    env = np.abs(signal.hilbert(y)) ** 2\n    w = np.hanning(int(0.25 * fs))\n    return np.convolve(env, w / w.sum(), mode=\"same\")\n\n\ndef window_power(bp, t, cues, window, baseline=None):\n    \"\"\"Mean beta power over `window` s from each cue; divided by the mean over `baseline` when\n    given (the variant of fig4b and fig4c).\"\"\"\n    i0 = np.searchsorted(t, cues)\n    a, b = int(window[0] * LFP_RATE), int(window[1] * LFP_RATE)\n    v = np.array([bp[i + a:i + b].mean() for i in i0])\n    if baseline is not None:\n        c, d = int(baseline[0] * LFP_RATE), int(baseline[1] * LFP_RATE)\n        v = v / np.array([bp[i + c:i + d].mean() for i in i0])\n    return v\n\n\ndef burst_onsets(bp, threshold, min_len):\n    \"\"\"Onsets (sample indices) of runs of beta power above `threshold` lasting at least `min_len`\n    samples (fig3b-beta-bursts criterion: 50 ms, one cycle at 20 Hz).\"\"\"\n    above = np.r_[0, (bp > threshold).astype(np.int8), 0]\n    d = np.diff(above)\n    on, off = np.where(d == 1)[0], np.where(d == -1)[0]\n    return on[(off - on) >= min_len]\n\n\n# ------------------------------------------------------------------------ Zenodo (zenodo-link)\n\ndef zenodo_file(name):\n    \"\"\"Read one small file of the Zenodo deposit into memory.\"\"\"\n    url = f\"https://zenodo.org/api/records/{ZENODO_RECORD}/files/{requests.utils.quote(name)}/content\"\n    r = requests.get(url, timeout=120)\n    r.raise_for_status()\n    return scipy.io.loadmat(io.BytesIO(r.content), squeeze_me=True)\n\n\n# ------------------------------------------------------------------------ spikes (Monkey P)\n\ndef noise_level(x, fs):\n    \"\"\"Noise of the raw signal: median absolute deviation / 0.6745 of the 300 to 6000 Hz\n    band-passed signal (fig5bc-unit-isolation criterion). The filter is a 4th-order Butterworth run\n    forwards and backwards, a standard choice.\"\"\"\n    sos = signal.butter(4, [300, 6000], btype=\"bandpass\", fs=fs, output=\"sos\")\n    y = signal.sosfiltfilt(sos, x)\n    return float(np.median(np.abs(y - np.median(y))) / 0.6745), y\n"
}
```

```
The file entries/amjad-2025/amjad.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Now the notebook. I'll build it with a script, run it in the scratch environment, and then write the conclusions from its printed numbers.

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/w/build.py",
 "content": "import json, sys\nimport nbformat as nbf\n\ncells = []\ndef md(s, tags=None):\n    c = nbf.v4.new_markdown_cell(s.strip())\n    if tags: c.metadata[\"tags\"] = tags\n    cells.append(c)\ndef code(s, tags=None):\n    c = nbf.v4.new_code_cell(s.strip())\n    if tags: c.metadata[\"tags\"] = tags\n    cells.append(c)\n\nR = json.load(open(sys.argv[2])) if len(sys.argv) > 2 else {}\ndef result(cid):\n    return R.get(cid, \"**Result: (to be written from the outputs).**\")\n\nmd(r\"\"\"\n# Reproducing Amjad et al. (2025) from DANDI:002013\n\n**Paper.** Amjad U, Mahajan S, Choi J, Shrivastav R, Murray R, Somich A, Coyne O, Schwerdt HN (2025).\nMicroinvasive Probes for Monitoring Electrical and Chemical Neural Activity in Nonhuman Primates.\n*ACS Chem Neurosci* 16(12) 2237-2247, [doi:10.1021/acschemneuro.5c00071](https://doi.org/10.1021/acschemneuro.5c00071).\nThe claims file (`claims/amjad-2025.yaml`) was written from the open-access full text (PMC12183687):\nthe Results, the figure legends and the Methods. The paper has no supplement.\n\n**Dataset.** [DANDI:002013](https://dandiarchive.org/dandiset/002013/0.261120.1306), version\n0.261120.1306, doi:10.48324/dandi.002013/0.261120.1306. This version was asked for: this attempt\ntests what the dataset holds now. The paper cites no DANDI version (it cites its Zenodo deposit,\ndoi:10.5281/zenodo.14826579). The dataset has two published versions, 0.261012.0921 and\n0.261120.1306; their files differ in size (listed below), and only 0.261120.1306 is analysed here.\n\nThree NWB files: Monkey T, session 09/13/2024 (shape task; raw FSCV of site c8dg and trial-aligned\nPCA dopamine); Monkey T, session 09/26/2024 (direction task; raw EPhys of c3bs and c3a and the\nbipolar beta-band LFP); Monkey P, session 08/13/2018 (direction task; raw EPhys and sorted spikes).\nFiles are streamed from the archive; nothing is downloaded to disk.\n\n**Outside data.** Only `zenodo-link` (`data: with_inputs`) uses the paper's Zenodo deposit,\ndoi:10.5281/zenodo.14826579: the four trial lists of session 09/26/2024 and the example beta trace.\n\n| claim | tested or blocked |\n|---|---|\n| insertion-yield | blocked, data_missing |\n| chronic-duration | blocked, data_missing |\n| fscv-waveform | tested |\n| ephys-acquisition | tested |\n| shape-task-structure | tested |\n| zenodo-link | tested (with Zenodo inputs) |\n| fig3a-dual-channel | blocked, data_missing |\n| fig3a-redox-peaks | tested |\n| fig3b-beta-bursts | tested |\n| fig4a-dopamine-reward | tested |\n| fig4b-beta-reward | tested |\n| fig4c-beta-side | tested |\n| fig5a-spike-reward | blocked, metadata_insufficient |\n| fig5bc-unit-isolation | tested |\n\nNo claim uses random draws, so no seed is set.\n\"\"\")\n\ncode(r\"\"\"\nimport re, time, resource\nimport numpy as np\nimport pandas as pd\nimport requests\nimport matplotlib.pyplot as plt\nfrom scipy import stats, signal\n\nimport amjad as A\n\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 40)\nstarted = time.time()\ndef mem_gb():\n    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6\nprint(\"dandiset\", A.DANDISET_ID, \"version\", A.DANDISET_VERSION)\n\"\"\")\n\nmd(\"## Data check\\n\\nEach check of the metadata against the values is stated under its output.\")\n\ncode(r\"\"\"\nlisting = {}\nfor v in [\"0.261012.0921\", A.DANDISET_VERSION]:\n    r = requests.get(f\"{A.API}/dandisets/{A.DANDISET_ID}/versions/{v}/assets/\", params={\"page_size\": 100}).json()\n    listing[v] = {a[\"path\"]: a[\"size\"] for a in r[\"results\"]}\nprint(pd.DataFrame(listing).to_string())\nmeta = requests.get(f\"{A.API}/dandisets/{A.DANDISET_ID}/versions/{A.DANDISET_VERSION}/\").json()\nprint(\"\\nsubjects in the metadata:\", meta[\"assetsSummary\"][\"numberOfSubjects\"], \" files:\", meta[\"assetsSummary\"][\"numberOfFiles\"])\nprint(\"\\ndescription:\", meta[\"description\"])\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\nThe pinned version holds the three files the description names, one per session, two subjects.\nThe earlier published version has the same paths with different sizes; its contents are not\ncompared here.\n\"\"\")\n\ncode(r\"\"\"\nF = {k: A.open_file(p) for k, p in A.PATHS.items()}\ndef s(x): return A._str(x[()]) if isinstance(x, h5py.Dataset) else x\nimport h5py\nrows = []\nfor k, f in F.items():\n    el = f[\"general/extracellular_ephys/electrodes\"]\n    rows.append({\n        \"file\": k, \"subject\": A._str(f[\"general/subject/subject_id\"][()]),\n        \"session_start\": A._str(f[\"session_start_time\"][()]),\n        \"trials\": f[\"intervals/trials/id\"].shape[0] if \"intervals/trials\" in f else 0,\n        \"event codes\": f[\"processing/events/events_table/id\"].shape[0],\n        \"electrode locations\": [A._str(x) for x in el[\"location\"][:]],\n        \"channels\": [A._str(x) for x in el[\"channel_name\"][:]] if \"channel_name\" in el else None,\n        \"units\": [A._str(x) for x in f[\"units/unit_name\"][:]] if \"units\" in f else None,\n    })\nprint(pd.DataFrame(rows).to_string())\nfor k, f in F.items():\n    print(f\"\\n{k}: datasets with their shapes\")\n    f.visititems(lambda n, o: print(\"  \", n, o.shape, o.dtype, A._str(o.attrs.get(\"unit\", \"\"))) if isinstance(o, h5py.Dataset)\n                 and not n.startswith((\"general\", \"specifications\")) and o.ndim > 0 and o.shape[0] > 1 else None)\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\nMonkey T has two sessions with a trials table; Monkey P's session has none. The location of Monkey\nP's electrode is `cl3`, while its sorted units are named `ch33#0` and `ch33#1` and the paper names\nthe site c33: the files name the site two ways. No file holds an implantation date, a list of\nimplanted sensors, or the second channel c8ds of the dual-channel probe.\n\"\"\")\n\ncode(r\"\"\"\nEV, NAMES, TR = {}, {}, {}\nfor k in [\"shape\", \"direction\", \"monkey_p\"]:\n    EV[k], NAMES[k] = A.events(F[k])\n    rep = sum(len(t) - len(np.unique(t)) for t in EV[k].values())\n    print(f\"{k}: {len(EV[k])} codes, {sum(len(t) for t in EV[k].values())} events, repeated times within a code: {rep}\")\nfor k in [\"shape\", \"direction\"]:\n    n = F[k][\"intervals/trials/id\"].shape[0]\n    TR[k] = A.decode_trials(EV[k], n)\n    mid = F[k][\"intervals/trials/midpoint_time\"][:]\n    st, sp = F[k][\"intervals/trials/start_time\"][:], F[k][\"intervals/trials/stop_time\"][:]\n    print(f\"{k}: {n} trials; code 128 times equal the trials' midpoint_time: {np.allclose(TR[k].start, mid)}; \"\n          f\"windows midpoint -30 s to +30 s: {np.allclose(mid - st, 30) and np.allclose(sp - mid, 30)}; \"\n          f\"trials without a value cue: {int(TR[k].value_cue.isna().sum())}\")\nprint(\"\\nshape task codes:\", {c: (NAMES['shape'][c], len(t)) for c, t in sorted(EV['shape'].items())})\nprint(\"\\ndirection task codes:\", {c: (NAMES['direction'][c], len(t)) for c, t in sorted(EV['direction'].items())})\nprint(\"\\nMonkey P codes:\", {c: len(t) for c, t in sorted(EV['monkey_p'].items())})\nprint(\"Monkey P event description:\", A._str(F[\"monkey_p\"][\"processing/events/events_table/event_description\"][0]))\n\"\"\", [\"sanity\"])\n\ncode(r\"\"\"\nsh, di = TR[\"shape\"], TR[\"direction\"]\nsh[\"forced\"] = sh.has_119\nsh[\"success\"] = sh.forced & sh.has_21\nprint(\"shape task (09/13/2024): forced\", int(sh.forced.sum()), \"choice (code 120)\", int(sh.has_120.sum()),\n      \"forced and choice\", int((sh.forced & sh.has_120).sum()), \"neither\", int((~sh.forced & ~sh.has_120).sum()))\nprint(\"   forced with feedback (success):\", int(sh.success.sum()), \" large (101):\", int((sh.success & sh.has_101).sum()),\n      \" small:\", int((sh.success & ~sh.has_101).sum()), \" trials with code 100:\", int(sh.get(\"has_100\", pd.Series(False)).sum()))\nprint(\"   feedback in non-forced trials:\", int((sh.has_21 & ~sh.forced).sum()))\nprint(\"   value cue minus trial start in successful forced trials (s):\", (sh.value_cue - sh.start)[sh.success].describe().round(3).to_dict())\ndi[\"success\"] = di.has_100 | di.has_101\nprint(\"\\ndirection task (09/26/2024): successful (reward 100 or 101)\", int(di.success.sum()), \" large\", int((di.success & di.has_101).sum()),\n      \" small\", int((di.success & di.has_100).sum()), \" both codes\", int((di.has_100 & di.has_101).sum()),\n      \" left\", int((di.success & di.has_117).sum()), \" right\", int((di.success & di.has_118).sum()),\n      \" left and right\", int((di.has_117 & di.has_118).sum()))\nprint(\"   feedback (21) without reward:\", int((di.has_21 & ~di.success).sum()), \" reward without feedback:\", int((di.success & ~di.has_21).sum()))\nprint(\"   value cue minus trial start in successful trials (s):\", (di.value_cue - di.start)[di.success].describe().round(3).to_dict())\nprint(\"   reward condition code 41 (all big) vs 101:\", pd.crosstab(di.has_41[di.success], di.has_101[di.success]).to_dict())\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\nThe decoded conditions agree with the event descriptions: in the direction task every rewarded\ntrial with code 41 got the big reward, and no trial has both reward codes or both sides. In the\nshape task only forced trials carry feedback, and code 100 does not occur, as the claims file says.\n\"\"\")\n\nmd(\"### FSCV, session 09/13/2024\")\n\ncode(r\"\"\"\nf = F[\"shape\"]\nt_scan, cur, volt, dt = A.fscv_scans(f)\nprint(f\"scans: {len(t_scan)} of {cur.shape[1]} samples; sampling {1/dt:.1f} Hz; scan duration {cur.shape[1]*dt*1e3:.2f} ms; \"\n      f\"intervals between scan starts {np.unique(np.round(np.diff(t_scan), 4))} s\")\nprint(f\"session covered: {t_scan[0]:.1f} to {t_scan[-1]:.1f} s; trials from {sh.start.min():.1f} to {sh.start.max():.1f} s\")\nprint(\"current unit:\", A._str(f[\"acquisition/fscv_response_series/data\"].attrs[\"unit\"]),\n      \" conversion:\", f[\"acquisition/fscv_response_series/data\"].attrs[\"conversion\"])\nprint(f\"current (nA): 1st to 99th percentile over all samples {np.percentile(cur[::50], 1):.1f} to {np.percentile(cur[::50], 99):.1f}\")\nprint(f\"voltage of a scan (V): {volt.min():.3f} to {volt.max():.3f}; all scans read the same voltage: \"\n      f\"{np.allclose(f['stimulus/presentation/fscv_excitation_series/data'][214*1000:214*1001], volt)}\")\nT = A.fscv_table(f)\nprint(\"\\ntrial-aligned table:\", T[\"da\"].shape, \"rate\", np.unique(T[\"rate\"]), \"good\", np.unique(T[\"good\"]),\n      \"trial_index\", T[\"trial_index\"].min(), \"to\", T[\"trial_index\"].max())\nprint(\"start_time equals trial start - 30 s:\", np.allclose(T[\"start_time\"], sh.start.values[T[\"trial_index\"]] - 30))\nfor k in [\"da\", \"iox\", \"ph\", \"m\"]:\n    print(f\"  {k}: NaN fraction {np.isnan(T[k]).mean():.4f}, 1st-99th percentile {np.nanpercentile(T[k], 1):.3f} to {np.nanpercentile(T[k], 99):.3f};\",\n          A._str(f[f'processing/fscv/trial_aligned_fscv_table/{k}'].attrs['description']))\nprint(f\"memory so far {mem_gb():.2f} GB, {time.time()-started:.0f} s\")\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\nThe raw FSCV is 214-sample scans at 25 kHz (8.56 ms) every 0.1 s, the 10 Hz of the paper and the\n25 kHz of the description. The current is stored in amperes with a conversion of 1e-9, so the\nvalues are nA. The trial-aligned table covers trials 0 to 733 of 1468 (the first half), as the\nname of its Zenodo source file says (\"firsthalf\"); the table's descriptions do not say so.\n\nClock check. The table's `iox` is defined on trial time (trial start at sample 300). Below, its\nscan-to-scan changes, placed at session time, are cross-correlated with those of the raw current\nat the sample nearest 0.6 V on the rising sweep, over the whole session. A peak at lag 0 shows\nthat the raw current and the trial clock agree.\n\"\"\")\n\ncode(r\"\"\"\nj06 = int(np.argmin(np.abs(volt[:int(np.argmax(volt))] - 0.6)))\ntab = np.zeros(len(t_scan)); cnt = np.zeros(len(t_scan))\nfor r in range(len(T[\"start_time\"])):\n    s0 = int(np.searchsorted(t_scan, T[\"start_time\"][r]))\n    d = np.diff(T[\"iox\"][r]); d[~np.isfinite(d)] = 0\n    n = min(len(d), len(t_scan) - s0 - 1)\n    tab[s0 + 1:s0 + 1 + n] += d[:n]; cnt[s0 + 1:s0 + 1 + n] += 1\ntab[cnt > 0] /= cnt[cnt > 0]\nraw = np.r_[0, np.diff(cur[:, j06].astype(float))]; raw -= raw.mean()\nxc = signal.fftconvolve(raw, tab[::-1], mode=\"full\"); lags = np.arange(-len(t_scan) + 1, len(t_scan))\nsel = np.abs(lags) <= 20000\nz = (xc[sel] - np.median(xc[sel])) / np.std(xc[sel]); ls = lags[sel]\nk = int(np.argmax(np.abs(z)))\nprint(f\"raw current at {volt[j06]:.3f} V against table iox: largest |z| {z[k]:.1f} at lag {ls[k]} scans ({ls[k]*0.1:.1f} s); \"\n      f\"z at lag 0: {z[ls == 0][0]:.1f}; next largest |z| outside lags -2 to 2: {np.max(np.abs(z[np.abs(ls) > 2])):.1f}\")\nok = cnt > 0\nprint(f\"slope of table iox change on raw change (lag 0): {np.polyfit(raw[ok], tab[ok], 1)[0]:.3f}\")\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\n### LFP and raw EPhys, session 09/26/2024\n\"\"\")\n\ncode(r\"\"\"\nf = F[\"direction\"]\nlfp = f[\"processing/ecephys/FilteredEphys/bipolar_lfp_series\"]\nt_lfp = lfp[\"timestamps\"][:]; x_lfp = lfp[\"data\"][:, 0]\nd = np.diff(t_lfp)\nprint(f\"bipolar LFP: {len(x_lfp)} samples, {t_lfp[0]:.1f} to {t_lfp[-1]:.1f} s, median rate {1/np.median(d):.1f} Hz, \"\n      f\"intervals {d.min()*1e3:.2f} to {d.max()*1e3:.2f} ms, unit {A._str(lfp['data'].attrs['unit'])}, \"\n      f\"0.1-99.9 percentile {np.percentile(x_lfp, 0.1)*1e6:.0f} to {np.percentile(x_lfp, 99.9)*1e6:.0f} uV, NaN {int(np.isnan(x_lfp).sum())}\")\nprint(\"electrode note:\", A._str(lfp[\"electrodes\"].attrs[\"description\"]))\nprint(f\"trials from {di.start.min():.1f} to {di.start.max():.1f} s; last trial window ends {di.start.max()+30:.1f} s\")\nes = f[\"acquisition/electrical_series\"]\nrate_T = es[\"starting_time\"].attrs[\"rate\"]; t0_raw = es[\"starting_time\"][()]\nprint(f\"raw EPhys: {es['data'].shape} at {rate_T:.4f} Hz from {t0_raw:.2f} s, conversion {es['data'].attrs['conversion']} V per bit\")\nel = f[\"general/extracellular_ephys/electrodes\"]\nprint(pd.DataFrame({c: [A._str(v) for v in el[c][:]] for c in [\"location\", \"channel_name\", \"DspLowCutFrequency\", \"DspHighCutFrequency\",\n                    \"DspLowCutFilterType\", \"DspHighCutFilterType\", \"InputRange\"]}).to_string())\n\"\"\", [\"sanity\"])\n\ncode(r\"\"\"\n# raw c3bs minus c3a against the stored bipolar LFP, in three 60 s segments: lag of the 13-28 Hz signals\nb, a = signal.butter(4, [13, 28], btype=\"bandpass\", fs=1000)\nfor T0 in [8000.0, 15000.0, 22000.0]:\n    i = int((T0 - t0_raw) * rate_T); n = int(60 * rate_T)\n    r = es[\"data\"][i:i + n, :].astype(float) * es[\"data\"].attrs[\"conversion\"]\n    tr_ = t0_raw + (i + np.arange(n)) / rate_T\n    bl = signal.sosfiltfilt(signal.butter(4, 400, fs=rate_T, output=\"sos\"), r[:, 0] - r[:, 1])\n    grid = np.arange(T0 + 1, T0 + 59, 0.001)\n    rf = signal.filtfilt(b, a, np.interp(grid, tr_, bl)); lf = signal.filtfilt(b, a, np.interp(grid, t_lfp, x_lfp))\n    N = len(rf); lg = np.arange(-3000, 3001)\n    c = np.array([np.corrcoef(rf[3000 + L:N - 3000 + L], lf[3000:N - 3000])[0, 1] for L in lg])\n    print(f\"segment at {T0:.0f} s: best lag {lg[np.argmax(c)]} ms, r {c.max():.3f}; r at lag 0 {c[3000]:.3f}; \"\n          f\"raw range {r.min()*1e6:.0f} to {r.max()*1e6:.0f} uV\")\n\"\"\", [\"sanity\"])\n\ncode(r\"\"\"\n# trial clock of the LFP: large against small reward in beta power 0 to 0.5 s after the value cue,\n# with the event times as stored and shifted\nbp = A.beta_power(x_lfp)\nds = di[di.success]\nL = ds.has_101.values\nfor shift in [0, -2, -1, 1, 2, 5]:\n    v = A.window_power(bp, t_lfp, ds.value_cue.values + shift, (0, 0.5))\n    print(f\"shift {shift:+d} s: large median {np.median(v[L])*1e12:.1f}, small {np.median(v[~L])*1e12:.1f} (1e-12 V^2), \"\n          f\"Mann-Whitney p = {stats.mannwhitneyu(v[L], v[~L]).pvalue:.2g}\")\nprint(f\"memory so far {mem_gb():.2f} GB, {time.time()-started:.0f} s\")\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\n### Monkey P, session 08/13/2018\n\"\"\")\n\ncode(r\"\"\"\nf = F[\"monkey_p\"]\nesp = f[\"acquisition/electrical_series\"]\ntsp = esp[\"timestamps\"][:2_000_000]\nprint(f\"raw EPhys: {esp['data'].shape}, first time {tsp[0]:.3f} s, median rate over the first 2e6 samples \"\n      f\"{1/np.median(np.diff(tsp)):.2f} Hz, conversion {esp['data'].attrs['conversion']} V per bit\")\nprint(\"notes:\", A._str(f[\"general/notes\"][()]))\nu = f[\"units\"]; ui = u[\"spike_times_index\"][:]; ust = u[\"spike_times\"][:]\nunits = {A._str(nm): ust[(ui[j-1] if j else 0):ui[j]] for j, nm in enumerate(u[\"unit_name\"][:])}\nprint(\"units:\", {k: len(v) for k, v in units.items()}, \" description:\", A._str(u.attrs.get(\"description\", \"\")))\ntu = f[\"processing/ecephys/thresholded_units\"]; ti = tu[\"spike_times_index\"][:]; tst = tu[\"spike_times\"][:]\ntn = [A._str(x) for x in tu[\"unit_name\"][:]]\nthr = {tn[j]: tst[(ti[j-1] if j else 0):ti[j]] for j in range(len(tn))}\nprint(\"thresholded units:\", {k: len(v) for k, v in thr.items()})\nprint(\"units ch33#1 equals thresholded unit 1:\", np.array_equal(units[\"ch33#1\"], thr[\"1\"]),\n      \"; ch33#0 holds thresholded -1 and 0:\", np.array_equal(np.sort(units[\"ch33#0\"]), np.sort(np.r_[thr[\"-1\"], thr[\"0\"]])))\nfor k, v in units.items():\n    print(f\"  {k}: {v[0]:.2f} to {v[-1]:.2f} s, sorted {bool(np.all(np.diff(v) >= 0))}\")\n\"\"\", [\"sanity\"])\n\ncode(r\"\"\"\n# spikes against the raw signal: spike-triggered average of the 300-6000 Hz signal at shifted spike times,\n# compared with the unit's mean stored waveform, in three 600 s segments\nwv = tu[\"waveforms\"]; wvi = tu[\"waveforms_index\"][:]\nlo = wvi[ti[1] - 1]; hi = wvi[ti[2] - 1]\nW1 = wv[lo:hi, 0].reshape(-1, 48)\nw1 = W1.mean(0)\nprint(f\"unit 1 stored waveforms: {W1.shape}, mean trough {w1.min()*1e6:.1f} uV at sample {int(np.argmin(w1))}, peak {w1.max()*1e6:.1f} uV\")\nrate_P = 30000.0\nnoise_seg = {}\nfor start in [0, 150_000_000, 300_000_000]:\n    r = esp[\"data\"][start:start + 18_000_000, 0].astype(float) * esp[\"data\"].attrs[\"conversion\"]\n    ts = esp[\"timestamps\"][start:start + 18_000_000]\n    nz, y = A.noise_level(r, rate_P)\n    noise_seg[start] = (ts[0], nz, float(np.mean(np.abs(r) >= 0.99e-3)))\n    sp = units[\"ch33#1\"]; sp = sp[(sp > ts[100]) & (sp < ts[-100])]; ii = np.searchsorted(ts, sp)\n    res = []\n    for lag in range(-60, 61):\n        jj = ii[(ii + lag > 60) & (ii + lag < len(y) - 60)]\n        sta = np.mean([y[i + lag - 9:i + lag + 39] for i in jj], axis=0)\n        res.append((np.corrcoef(sta, w1)[0, 1], lag, sta.min()))\n    best = max(res); at0 = [x for x in res if x[1] == 0][0]\n    print(f\"segment from {ts[0]:.0f} s: {len(ii)} spikes; STA best lag {best[1]} samples (r {best[0]:.3f}, trough {best[2]*1e6:.1f} uV); \"\n          f\"r at lag 0 {at0[0]:.3f}; samples at the +-1 mV input range {noise_seg[start][2]:.4f}\")\nprint(f\"memory so far {mem_gb():.2f} GB, {time.time()-started:.0f} s\")\n\"\"\", [\"sanity\"])\n\n# ---------------------------------------------------------------- claims\nmd(r\"\"\"\n## insertion-yield (blocked)\n\n> Insertion yields were low, 21.4% (3 of 14 sensors) in monkey T and 33% (3 of 9) in monkey P,\n> counted as recording sites that stayed functional after insertion until the end of the study.\n\nBlocked, `data_missing`: the criterion needs the list of implanted sensors per monkey and whether\neach kept recording. The files hold only the recorded sites (c8dg; c3bs and c3a; cl3/ch33), listed\nin the data check above; no file or the dataset metadata lists the implanted sensors.\n\"\"\")\n\nmd(r\"\"\"\n## chronic-duration (blocked)\n\n> The s-µIPs kept recording for more than a year after implantation; the example sites were\n> recorded 483 days (c8dg), 496 days (c3bs-c3a) and 390 days (monkey P) after implantation.\n\nBlocked, `data_missing`: the criterion needs the implantation date of each site. The cell below\nsearches every text field and attribute of the three files for an implantation date.\n\"\"\")\n\ncode(r\"\"\"\nhits = {}\nfor k, f in F.items():\n    found = []\n    def look(n, o):\n        if isinstance(o, h5py.Dataset) and o.dtype.kind in \"OSU\" and o.size < 100:\n            for v in np.ravel(o[()]):\n                if \"implant\" in A._str(v).lower():\n                    found.append((n, A._str(v)[:120]))\n    f.visititems(look)\n    hits[k] = found\nfor k, v in hits.items():\n    print(k, \"fields mentioning 'implant':\", len(v))\n    for n, t in v:\n        print(\"   \", n, \"|\", t)\nprint(\"dandiset metadata mentions 'implant' with a date:\", bool(re.search(r\"implant\\w*\\s+(on|in)\\s+\\d\", meta[\"description\"])))\n\"\"\", [\"claim:chronic-duration\"])\n\nmd(r\"\"\"\nThe fields that mention implants are descriptions; none gives a date. The subjects' ages\n(P11Y and P8Y) are not implantation dates.\n\"\"\")\n\nmd(r\"\"\"\n## fscv-waveform\n\n> FSCV applied a triangular waveform from -0.4 to 1.3 V at 400 V/s, every 100 ms (10 Hz).\n\nCriterion: measured from the applied voltage series of session 09/13/2024; the sweep rate is the\nmedian absolute step of the rising ramp times the sampling rate, the scan frequency one over the\nmedian interval between scan starts. Reproduced when all four are within tolerance (-0.4 +- 0.04 V,\n1.3 +- 0.13 V, 400 +- 40 V/s, 10 +- 1 Hz), partially when three are.\n\"\"\")\n\ncode(r\"\"\"\nwp = A.waveform_parameters(volt, t_scan, dt)\nexp = {\"lowest_V\": (-0.4, 0.04), \"highest_V\": (1.3, 0.13), \"sweep_V_per_s\": (400, 40), \"scan_Hz\": (10, 1)}\nwithin = {k: abs(wp[k] - e) <= tol for k, (e, tol) in exp.items()}\nfor k in exp:\n    print(f\"{k}: measured {wp[k]:.4f}, expected {exp[k][0]} +- {exp[k][1]}, within: {within[k]}\")\nprint(\"values within tolerance:\", sum(within.values()), \"of 4\")\n# the voltage over the whole session: minimum and maximum of every 1000th scan\nvv = f = F[\"shape\"][\"stimulus/presentation/fscv_excitation_series/data\"]\nmins, maxs = [], []\nfor s0 in range(0, len(t_scan), 24000):\n    blk = vv[s0 * 214:(s0 + 1000) * 214].reshape(-1, 214)\n    mins.append(blk.min()); maxs.append(blk.max())\nprint(f\"over {len(mins)} blocks of 1000 scans across the session: minimum {min(mins):.4f} to {max(mins):.4f} V, maximum {min(maxs):.4f} to {max(maxs):.4f} V\")\nfig, ax = plt.subplots(figsize=(5, 2.5))\nax.plot(np.arange(214) * dt * 1e3, volt, \".-\", ms=2); ax.set_xlabel(\"ms from scan start\"); ax.set_ylabel(\"applied V\")\nax.set_title(\"one scan, 09/13/2024 (all points shown)\"); plt.show()\n\"\"\", [\"claim:fscv-waveform\"])\n\nmd(result(\"fscv-waveform\"))\n\nmd(r\"\"\"\n## ephys-acquisition\n\n> EPhys was sampled at 30 kHz in monkey P and 32 kHz in monkey T, and band-pass filtered from 0.1\n> to 7500 Hz.\n\nCriterion: sampling rates from the timestamps or rate of the raw series; the filter from the\nNeuralynx settings in the electrodes table (Monkey P's file has none). Reproduced when all four\nvalues are within tolerance (30000 +- 3000, 32000 +- 3200, 0.1 +- 0.01, 7500 +- 750 Hz).\n\"\"\")\n\ncode(r\"\"\"\nelT = F[\"direction\"][\"general/extracellular_ephys/electrodes\"]\nlow = np.unique(elT[\"DspLowCutFrequency\"][:]); high = np.unique(elT[\"DspHighCutFrequency\"][:])\nvals = {\"rate monkey P\": (1 / np.median(np.diff(tsp)), 30000, 3000), \"rate monkey T\": (rate_T, 32000, 3200),\n        \"low cut monkey T\": (float(low[0]), 0.1, 0.01), \"high cut monkey T\": (float(high[0]), 7500, 750)}\nfor k, (m, e, tol) in vals.items():\n    print(f\"{k}: measured {m:.4f} Hz, expected {e} +- {tol}, within: {abs(m - e) <= tol}\")\nprint(\"filter settings identical on both channels:\", len(low) == 1 and len(high) == 1,\n      \"; Monkey P electrodes table has filter columns:\", \"DspHighCutFrequency\" in F[\"monkey_p\"][\"general/extracellular_ephys/electrodes\"])\nprint(\"Monkey T 09/13/2024 file holds raw EPhys:\", \"electrical_series\" in F[\"shape\"][\"acquisition\"])\n\"\"\", [\"claim:ephys-acquisition\"])\n\nmd(result(\"ephys-acquisition\"))\n\nmd(r\"\"\"\n## shape-task-structure\n\n> In the shape task, forced trials made up 25% of all trials, and the cue-reward association was\n> reversed after blocks of 50 to 300 trials.\n\nCriterion: forced trials carry code 119, as a share of all trials in the trials table. A block is a\nrun of trials in which the same cue image (81 or 88) signals the large reward in the successful\nforced trials; a reversal is placed at the first trial after the last forced trial of the earlier\nassociation; block lengths count all trials; the first and last blocks are reported, not judged.\nReproduced when the share is 25 +- 2.5% and every complete block is 45 to 330 trials.\n\"\"\")\n\ncode(r\"\"\"\nshare = 100 * sh.forced.mean()\nprint(f\"forced trials {int(sh.forced.sum())} of {len(sh)} = {share:.2f}%\")\nfs = sh[sh.success]\nprint(\"successful forced trials with image 81 only / 88 only / both / neither:\",\n      int((fs.has_81 & ~fs.has_88).sum()), int((~fs.has_81 & fs.has_88).sum()), int((fs.has_81 & fs.has_88).sum()), int((~fs.has_81 & ~fs.has_88).sum()))\nimg = np.where(fs.has_81, 81, 88)\nbig_img = np.where(fs.has_101, img, np.where(img == 81, 88, 81))\nch = np.where(np.diff(big_img) != 0)[0]\nrev = fs.trial.values[ch] + 1          # first trial after the last forced trial of the earlier association\nedges = np.r_[0, rev, len(sh)]\nblocks = pd.DataFrame({\"first_trial\": edges[:-1], \"end_trial\": edges[1:], \"length\": np.diff(edges),\n                       \"large_image\": [big_img[0]] + list(big_img[ch + 1]),\n                       \"forced_successes\": [int(((fs.trial >= a) & (fs.trial < b)).sum()) for a, b in zip(edges[:-1], edges[1:])]})\nblocks[\"complete\"] = [0 < i < len(blocks) - 1 for i in range(len(blocks))]\nprint(blocks.to_string())\ncomp = blocks[blocks.complete].length\nprint(f\"complete blocks: {len(comp)}, lengths {comp.min()} to {comp.max()}; all within 45-330: {bool(((comp >= 45) & (comp <= 330)).all())}\")\nprint(f\"share within 22.5-27.5%: {22.5 <= share <= 27.5}\")\n\"\"\", [\"claim:shape-task-structure\"])\n\nmd(result(\"shape-task-structure\"))\n\nmd(r\"\"\"\n## zenodo-link (link claim, with Zenodo inputs)\n\n> The dandiset reproduces the processed data the paper deposited on Zenodo; the trial selections\n> and the beta power of the paper's example trial computed from the dandiset agree with the paper's\n> own files.\n\nCriterion: trials matched by number (1 to 1501 in the trials table of 09/26/2024). The four Zenodo\nlists of successful trials are compared with the selections decoded here; the beta power of the\n35th trial of the large-reward list is compared with the Zenodo example trace (-3 to 12 s from the\nvalue cue). Reproduced when each list agrees for at least 99% of the trials in either and the\ntraces correlate at r >= 0.9 at a lag of at most 10 ms.\n\"\"\")\n\ncode(r\"\"\"\nZ = {k: np.atleast_1d(A.zenodo_file(n)[\"trids_out\"]).astype(int) for k, n in A.ZENODO_LISTS.items()}\nmine = {\"large\": di.success & di.has_101, \"small\": di.success & di.has_100,\n        \"left\": di.success & di.has_117, \"right\": di.success & di.has_118}\nagree = {}\nfor k in Z:\n    a = set(Z[k].tolist()); b = set((np.where(mine[k])[0] + 1).tolist())\n    agree[k] = min(len(a & b) / len(a), len(a & b) / len(b))\n    print(f\"{k}: Zenodo {len(a)}, here {len(b)}, in both {len(a & b)}, only Zenodo {sorted(a - b)}, only here {sorted(b - a)}; \"\n          f\"agreement {100*agree[k]:.2f}%\")\nprint(f\"trial 1501 starts at {di.start.iloc[-1]:.1f} s; its 60 s window ends {di.start.iloc[-1]+30:.1f} s; LFP ends {t_lfp[-1]:.1f} s\")\nex = A.zenodo_file(A.ZENODO_EXAMPLE)\nprint(\"example file fields:\", {k: np.shape(v) for k, v in ex.items() if not k.startswith(\"__\")})\nprint(\"field 'trial35bigrewardata' equals its time axis:\", np.array_equal(ex[\"trial35bigrewardata\"], ex[\"trial35bigrewardataTS\"]))\nref = ex[\"trial35bigrewardataBetaPower\"]; tt = ex[\"trial35bigrewardataTS\"]\nk35 = Z[\"large\"][34] - 1\nvc = di.value_cue.iloc[k35]\ni0 = int(np.searchsorted(t_lfp, vc + tt[0]))\nlags = np.arange(-200, 201)\nrs = np.array([np.corrcoef(bp[i0 + L:i0 + L + len(ref)], ref)[0, 1] for L in lags])\nkb = int(np.argmax(rs))\nprint(f\"35th large trial = trial {k35+1}; value cue at {vc:.3f} s; r at lag 0 {rs[200]:.4f}; best r {rs[kb]:.4f} at lag {lags[kb]} ms; \"\n      f\"median ratio here/Zenodo {np.median(bp[i0:i0+len(ref)] / ref):.3f}\")\nfig, ax = plt.subplots(figsize=(7, 2.5))\nax.plot(tt, ref * 1e12, label=\"Zenodo\"); ax.plot(tt, bp[i0:i0 + len(ref)] * 1e12, label=\"here\", alpha=.7)\nax.set_xlabel(\"s from value cue\"); ax.set_ylabel(\"beta power (1e-12 V^2)\"); ax.legend(); plt.show()\nprint(f\"plotted range: Zenodo {ref.min()*1e12:.1f} to {ref.max()*1e12:.1f}, here {bp[i0:i0+len(ref)].min()*1e12:.1f} to {bp[i0:i0+len(ref)].max()*1e12:.1f}\")\n\"\"\", [\"claim:zenodo-link\"])\n\nmd(result(\"zenodo-link\"))\n\nmd(r\"\"\"\n## fig3a-dual-channel (blocked)\n\n> Dopamine was measured from two neighbouring channels of one dual-channel s-µIP (sites c8dg and\n> c8ds, 0.1 to 0.2 mm apart), and both showed dopamine increases after the value cue in a single\n> forced large-reward trial.\n\nBlocked, `data_missing`: the criterion needs the trial-aligned dopamine of both c8dg and c8ds. The\n09/13/2024 file holds c8dg only (electrodes table above), and the Zenodo deposit holds only a c8dg\nfile (`FSCV_trlists_c8dg_09132024_firsthalf.mat`). The c8dg half alone is shown below; it does not\ndecide the claim.\n\"\"\")\n\ncode(r\"\"\"\ntabrows = sh.iloc[T[\"trial_index\"]].reset_index(drop=True)\nicue = A.cue_sample(tabrows)\nv03 = A.window_mean(T[\"da\"], icue, (0, 3))\nsel = (tabrows.success & tabrows.has_101).values\nprint(f\"c8dg only: forced large-reward trials in the table {int(sel.sum())}, with a value {int(np.isfinite(v03[sel]).sum())}; \"\n      f\"mean change over 0-3 s above zero in {np.mean(v03[sel][np.isfinite(v03[sel])] > 0)*100:.1f}%\")\n\"\"\", [\"claim:fig3a-dual-channel\"])\n\nmd(r\"\"\"\n## fig3a-redox-peaks\n\n> The single-trial FSCV colour plot shows dopamine redox current, with changes near 0.6 V\n> (oxidation) and -0.2 V (reduction) after the value cue.\n\nCriterion: the background-subtracted voltammogram (mean of 0.5 to 2 s after the value cue minus\nthe scan at the value cue), averaged over forced large-reward trials, should have its largest\npositive value on the rising sweep within 0.45 to 0.75 V and its most negative value on the falling\nsweep within -0.35 to -0.05 V. Reproduced when both hold. The raw current is on the trial clock\n(data check). All successful forced large-reward trials of the session are used, as the raw current\ncovers the whole session; the first half (the trials of the table) is shown as a variant.\n\"\"\")\n\ncode(r\"\"\"\ntop = int(np.argmax(volt)); up = np.arange(0, top + 1); down = np.arange(top + 1, len(volt))\ndef peaks(vg):\n    m = vg.mean(0)\n    iu = up[np.argmax(m[up])]; idn = down[np.argmin(m[down])]\n    return volt[iu], m[iu], volt[idn], m[idn]\nlg = sh[sh.success & sh.has_101]; sm = sh[sh.success & ~sh.has_101]\nVL = A.voltammograms(t_scan, cur, lg.value_cue.values); VS = A.voltammograms(t_scan, cur, sm.value_cue.values)\nfor name, vg in [(\"all large\", VL), (\"large, trials 0-733\", VL[lg.trial.values < 734]), (\"small (reference)\", VS)]:\n    vu, au, vd, ad = peaks(vg)\n    print(f\"{name} (n={len(vg)}): largest rising value {au:.3f} nA at {vu:.3f} V (in 0.45-0.75: {0.45 <= vu <= 0.75}); \"\n          f\"most negative falling value {ad:.3f} nA at {vd:.3f} V (in -0.35 to -0.05: {-0.35 <= vd <= -0.05})\")\nm = VL.mean(0); sem = VL.std(0) / np.sqrt(len(VL))\nfor vtarget in [0.6, -0.2]:\n    seg = up if vtarget > 0 else down\n    j = seg[np.argmin(np.abs(volt[seg] - vtarget))]\n    print(f\"mean at {volt[j]:.3f} V ({'rising' if vtarget > 0 else 'falling'}): {m[j]:.3f} +- {sem[j]:.3f} nA (SEM)\")\n# per-trial variant: trials whose own peaks fall in both ranges\nok = []\nfor vg in VL:\n    iu = up[np.argmax(vg[up])]; idn = down[np.argmin(vg[down])]\n    ok.append((0.45 <= volt[iu] <= 0.75) and (-0.35 <= volt[idn] <= -0.05))\nprint(f\"single trials meeting both ranges: {sum(ok)} of {len(ok)}\")\n# shifted cue times (null reference for the peak positions)\nfor shift in [-5, 5]:\n    vu, au, vd, ad = peaks(A.voltammograms(t_scan, cur, lg.value_cue.values + shift))\n    print(f\"cue shifted {shift:+d} s: rising max at {vu:.3f} V ({au:.3f} nA), falling min at {vd:.3f} V ({ad:.3f} nA)\")\nfig, ax = plt.subplots(figsize=(6, 3))\nax.plot(volt[up], m[up], label=\"rising\"); ax.plot(volt[down], m[down], label=\"falling\")\nax.axvspan(0.45, 0.75, alpha=.1); ax.axvspan(-0.35, -0.05, alpha=.1, color=\"r\")\nax.set_xlabel(\"applied V\"); ax.set_ylabel(\"nA\"); ax.legend(); ax.set_title(\"mean background-subtracted voltammogram, large forced trials\")\nplt.show(); print(f\"plotted range {m.min():.3f} to {m.max():.3f} nA\")\n\"\"\", [\"claim:fig3a-redox-peaks\"])\n\nmd(result(\"fig3a-redox-peaks\"))\n\nmd(r\"\"\"\n## fig3b-beta-bursts\n\n> Single-trial bipolar LFP from site c3bs-c3a shows beta bursts (one to a few cycles of high beta\n> power) whose frequency changes around the cue and other task events.\n\nCriterion: successful large-reward trials of 09/26/2024. A burst is a run of beta power above the\n75th percentile of the beta power over all trial windows of the session lasting at least 50 ms. Per\ntrial the burst rate is counted in -1 to 0 s and 0 to 1 s from the value cue. Reproduced when the\nrates differ by a two-sided Wilcoxon signed-rank test at p < 0.05. 50th and 90th percentiles are\nvariants. \"All trial windows\" is read as the union of the 60 s windows of the trials table.\n\"\"\")\n\ncode(r\"\"\"\nmask = np.zeros(len(bp), bool)\nfor m0 in di.start.values:\n    a0, b0 = np.searchsorted(t_lfp, [m0 - 30, m0 + 30]); mask[a0:b0] = True\nprint(f\"samples in trial windows: {mask.sum()} of {len(mask)}\")\ndl = di[di.success & di.has_101]; ii = np.searchsorted(t_lfp, dl.value_cue.values)\nfor q in [75, 50, 90]:\n    thr_q = np.percentile(bp[mask], q)\n    on = A.burst_onsets(bp, thr_q, 50)\n    pre = np.array([((on >= i - 1000) & (on < i)).sum() for i in ii]); post = np.array([((on >= i) & (on < i + 1000)).sum() for i in ii])\n    w = stats.wilcoxon(pre, post)\n    print(f\"{q}th percentile ({thr_q*1e12:.1f}e-12 V^2): n={len(ii)}, bursts/s before {pre.mean():.3f}, after {post.mean():.3f}; \"\n          f\"trials with more after / fewer / equal {int((post>pre).sum())}/{int((post<pre).sum())}/{int((post==pre).sum())}; Wilcoxon p = {w.pvalue:.2g}\")\n\"\"\", [\"claim:fig3b-beta-bursts\"])\n\nmd(result(\"fig3b-beta-bursts\"))\n\nmd(r\"\"\"\n## fig4a-dopamine-reward\n\n> Trial-averaged dopamine at site c8dg is higher after large-reward than after small-reward value\n> cues, in successful forced trials of the shape task.\n\nCriterion: successful forced trials of 09/13/2024 with a row in the trial-aligned table; per trial\nthe mean of the re-referenced dopamine over 0 to 3 s after the value cue. Reproduced when the\nlarge-reward median exceeds the small-reward median and the Mann-Whitney test gives p < 0.05.\nVariants (not deciding): `da` without re-referencing, `iox` re-referenced, windows 0-1.5 s and\n1.5-3 s.\n\"\"\")\n\ncode(r\"\"\"\nsucc_t = tabrows.success.values; large_t = (tabrows.success & tabrows.has_101).values\nprint(f\"successful forced trials in the table: {int(succ_t.sum())} (large {int(large_t.sum())}, small {int((succ_t & ~large_t).sum())})\")\nres4a = {}\nfor name, x, w, rr in [(\"da re-referenced, 0-3 s (deciding)\", T[\"da\"], (0, 3), True), (\"da as stored, 0-3 s\", T[\"da\"], (0, 3), False),\n                       (\"iox re-referenced, 0-3 s\", T[\"iox\"], (0, 3), True), (\"da re-referenced, 0-1.5 s\", T[\"da\"], (0, 1.5), True),\n                       (\"da re-referenced, 1.5-3 s\", T[\"da\"], (1.5, 3), True)]:\n    v = A.window_mean(x, icue, w, rr)\n    a_, b_ = v[large_t], v[succ_t & ~large_t]\n    dropped = int((~np.isfinite(a_)).sum() + (~np.isfinite(b_)).sum())\n    a_, b_ = a_[np.isfinite(a_)], b_[np.isfinite(b_)]\n    p = stats.mannwhitneyu(a_, b_).pvalue\n    eff = stats.mannwhitneyu(a_, b_).statistic / (len(a_) * len(b_))\n    res4a[name] = (np.median(a_), np.median(b_), p)\n    print(f\"{name}: large median {np.median(a_):.3f} (n={len(a_)}), small {np.median(b_):.3f} (n={len(b_)}), \"\n          f\"dropped {dropped}, P(large > small) {eff:.3f}, Mann-Whitney p = {p:.3g}\")\nfor shift in [-10, -5, 5, 10]:\n    v = A.window_mean(T[\"da\"], icue + shift * 10, (0, 3))\n    a_, b_ = v[large_t], v[succ_t & ~large_t]; a_, b_ = a_[np.isfinite(a_)], b_[np.isfinite(b_)]\n    print(f\"cue shifted {shift:+d} s: large {np.median(a_):.3f}, small {np.median(b_):.3f}, p = {stats.mannwhitneyu(a_, b_).pvalue:.3g}\")\nt_ax = (np.arange(601) - 300) / 10\nfig, ax = plt.subplots(figsize=(6, 3))\nfor lab, s_ in [(\"large\", large_t), (\"small\", succ_t & ~large_t)]:\n    rows_ = np.where(s_)[0]\n    al = np.array([T[\"da\"][r, icue[r] - 50:icue[r] + 101] - T[\"da\"][r, icue[r]] for r in rows_])\n    mu = np.nanmean(al, 0); ax.plot(np.arange(-50, 101) / 10, mu, label=lab)\n    print(f\"{lab}: plotted mean range {np.nanmin(mu):.3f} to {np.nanmax(mu):.3f}\")\nax.axvline(0, color=\"k\", lw=.5); ax.set_xlabel(\"s from value cue\"); ax.set_ylabel(\"da, re-referenced\"); ax.legend(); plt.show()\n\"\"\", [\"claim:fig4a-dopamine-reward\"])\n\nmd(result(\"fig4a-dopamine-reward\"))\n\nmd(r\"\"\"\n## fig4b-beta-reward\n\n> Beta-band LFP power at c3bs-c3a in the direction task is more suppressed (stronger event-related\n> desynchronization) after large-reward than after small-reward value cues, in a brief window after\n> the cue.\n\nCriterion: successful trials of 09/26/2024, large against small; per trial the mean beta power over\n0 to 0.5 s after the value cue. Reproduced when the large median is below the small median and the\nMann-Whitney test gives p < 0.05. Variants: 0-1 s, 0.25-0.75 s, and power divided by each trial's\nmean over -0.5 to 0 s.\n\"\"\")\n\ndef beta_cell(group_a, group_b, la, lb):\n    return rf\"\"\"\nfor w in [(0, 0.5), (0, 1), (0.25, 0.75)]:\n    for base in [None, (-0.5, 0)]:\n        v = A.window_power(bp, t_lfp, ds.value_cue.values, w, base)\n        a_, b_ = v[{group_a}], v[{group_b}]\n        mw = stats.mannwhitneyu(a_, b_)\n        scale = 1 if base else 1e12\n        print(f\"window {{w}}{{' / baseline' if base else ''}}: {la} median {{np.median(a_)*scale:.3f}} (n={{len(a_)}}), \"\n              f\"{lb} {{np.median(b_)*scale:.3f}} (n={{len(b_)}}){{'' if base else ' (1e-12 V^2)'}}; P({la} < {lb}) {{1 - mw.statistic/(len(a_)*len(b_)):.3f}}; p = {{mw.pvalue:.3g}}\")\n\"\"\"\n\ncode(\"L = ds.has_101.values\\n\" + beta_cell(\"L\", \"~L\", \"large\", \"small\") + r\"\"\"\nfig, ax = plt.subplots(figsize=(6, 3))\nfor lab, s_ in [(\"large\", L), (\"small\", ~L)]:\n    ii_ = np.searchsorted(t_lfp, ds.value_cue.values[s_])\n    mu = np.mean([bp[i - 1000:i + 2000] for i in ii_], 0) * 1e12\n    ax.plot(np.arange(-1000, 2000) / 1000, mu, label=lab); print(f\"{lab}: plotted mean range {mu.min():.1f} to {mu.max():.1f}\")\nax.axvspan(0, 0.5, alpha=.1); ax.set_xlabel(\"s from value cue\"); ax.set_ylabel(\"beta power (1e-12 V^2)\"); ax.legend(); plt.show()\n\"\"\", [\"claim:fig4b-beta-reward\"])\n\nmd(result(\"fig4b-beta-reward\"))\n\nmd(r\"\"\"\n## fig4c-beta-side\n\n> With the reward fixed at large, beta-band LFP power is more suppressed when the cue is on the\n> left (contralateral) than on the right (ipsilateral).\n\nCriterion: successful large-reward trials of 09/26/2024, left against right; per trial the mean\nbeta power over 0 to 0.5 s after the value cue. Reproduced when the left median is below the right\nmedian and the Mann-Whitney test gives p < 0.05. Variants as for fig4b.\n\"\"\")\n\ncode(\"Lf = ds.has_101.values & ds.has_117.values; Rt = ds.has_101.values & ds.has_118.values\\n\"\n     + beta_cell(\"Lf\", \"Rt\", \"left\", \"right\") + r\"\"\"\nprint(\"small-reward trials, left against right (not deciding):\")\nv = A.window_power(bp, t_lfp, ds.value_cue.values, (0, 0.5))\nsl, sr = ~ds.has_101.values & ds.has_117.values, ~ds.has_101.values & ds.has_118.values\nprint(f\"  left {np.median(v[sl])*1e12:.1f}, right {np.median(v[sr])*1e12:.1f}, p = {stats.mannwhitneyu(v[sl], v[sr]).pvalue:.3g}\")\nprint(\"side by reward:\", pd.crosstab(ds.has_101, ds.has_117).to_dict())\n\"\"\", [\"claim:fig4c-beta-side\"])\n\nmd(result(\"fig4c-beta-side\"))\n\nmd(r\"\"\"\n## fig5a-spike-reward (blocked)\n\n> Spikes recorded from an s-µIP in the caudate of monkey P (site c33, 390 days post implant) fire\n> at a different rate for large and small reward during the value cue fixation of the direction\n> task.\n\nBlocked, `metadata_insufficient`: the criterion needs the value cue time and the reward size of\neach trial. Monkey P's file has no trials table, and its events are bare TTL codes whose\ndescription says \"The code map for this session is not available\" (data check). The Zenodo file\n`session126_events.mat` holds the same strobed codes as Neuralynx TTL strings, without names, and\nthe paper's code (spikes_PCA.m, ISI_Plot.m, doi:10.5281/zenodo.10397773) does not name them. Which\ncode is the value cue and which marks a large reward cannot be read from the data.\n\"\"\")\n\nmd(r\"\"\"\n## fig5bc-unit-isolation\n\n> The s-µIP recorded a spike-sorted unit in monkey P, shown by its average waveform and its\n> interspike interval histogram.\n\nCriterion: the sorted unit is Plexon unit 1. Reproduced when fewer than 1% of its interspike\nintervals are under 1 ms and the trough of its mean stored waveform is deeper than 3 times the\nnoise of the raw signal (MAD / 0.6745 of the 300-6000 Hz signal over 600 s). Partially when only one\nholds. The 600 s is the first 600 s of the recording (a standard choice); two later segments are\nshown.\n\"\"\")\n\ncode(r\"\"\"\ns1 = units[\"ch33#1\"]\nisi = np.diff(s1) * 1e3\nprint(f\"unit ch33#1: {len(s1)} spikes; ISIs under 1 ms {np.sum(isi < 1)} of {len(isi)} = {100*np.mean(isi < 1):.4f}%; \"\n      f\"under 2 ms {100*np.mean(isi < 2):.3f}%; median ISI {np.median(isi):.1f} ms\")\ntrough = -w1.min()\nfor start, (tstart, nz, sat) in noise_seg.items():\n    print(f\"600 s from {tstart:.0f} s: noise {nz*1e6:.2f} uV, trough {trough*1e6:.1f} uV = {trough/nz:.2f} x noise\")\ns0 = units[\"ch33#0\"]; isi0 = np.diff(s0) * 1e3\nprint(f\"unit ch33#0 (unsorted, reference): ISIs under 1 ms {100*np.mean(isi0 < 1):.3f}%\")\nfig, ax = plt.subplots(1, 2, figsize=(9, 3))\ntw = (np.arange(48) - 8) / 30\nax[0].plot(tw, w1 * 1e6); ax[0].fill_between(tw, (w1 - W1.std(0)) * 1e6, (w1 + W1.std(0)) * 1e6, alpha=.3)\nax[0].set_xlabel(\"ms\"); ax[0].set_ylabel(\"uV\")\nax[1].hist(isi[isi < 100], bins=np.arange(0, 101)); ax[1].set_xlabel(\"ISI (ms), 1 ms bins\")\nplt.show(); print(f\"ISIs above 100 ms not plotted: {np.sum(isi >= 100)}\")\n\"\"\", [\"claim:fig5bc-unit-isolation\"])\n\nmd(result(\"fig5bc-unit-isolation\"))\n\ncode(r\"\"\"\nprint(f\"total run time {time.time()-started:.0f} s, peak memory {mem_gb():.2f} GB\")\n\"\"\")\n\nmd(R.get(\"summary\", \"## Summary\\n\\n(to be written)\"))\n\nnb = nbf.v4.new_notebook(); nb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"display_name\": \"Python 3\", \"language\": \"python\", \"name\": \"python3\"}\nnbf.write(nb, sys.argv[1])\n"
}
```

```
File created successfully at: /tmp/claude-1001/w/build.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR/w && sed -i 's/^def s(x): return A._str(x\[()\]) if isinstance(x, h5py.Dataset) else x$//; s/^import h5py$//; s/^import re, time, resource$/import re, time, resource\nimport h5py/; s/^vv = f = F\[/vv = F[/' build.py && . $TMPDIR/scratch/bin/activate && uv pip install -q nbconvert ipykernel 2>&1 | tail -1; python build.py entries/amjad-2025/reproduce_amjad_2025.ipynb && cd entries/amjad-2025 && date -u && time jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 --output $TMPDIR/w/exec1.ipynb reproduce_amjad_2025.ipynb 2>&1 | tail -5
```

```
Tue Nov 24 23:10:17 UTC 2026
[32m    188[39m     seg = y[i + a:i + b]
[32m    189[39m     [38;5;28;01mif[39;00m np.isfinite(seg).any():

[31mIndexError[39m: index -9223372036854775808 is out of bounds for axis 1 with size 601


real	1m8.282s
user	0m22.667s
sys	0m2.934s
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p="amjad.py"; s=open(p).read()
s=s.replace('''    return np.rint(FSCV_T0_SAMPLE + (trials_rows.value_cue.values - trials_rows.start.values)
                   * FSCV_RATE).astype(int)''','''    i = np.rint(FSCV_T0_SAMPLE + (trials_rows.value_cue.values - trials_rows.start.values) * FSCV_RATE)
    return np.where(np.isfinite(i), i, -1).astype(int)   # -1: the trial has no value cue''')
s=s.replace('''    for r, i in enumerate(i_cue):
        y = x[r]''','''    for r, i in enumerate(i_cue):
        if i < 0 or i >= x.shape[1]:
            continue
        y = x[r]''')
open(p,"w").write(s)
EOF
. $TMPDIR/scratch/bin/activate && time jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 --output $TMPDIR/w/exec1.ipynb reproduce_amjad_2025.ipynb 2>&1 | tail -5
```

```
[NbConvertApp] Converting notebook reproduce_amjad_2025.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 377581 bytes to /tmp/claude-1001/w/exec1.ipynb

real	2m48.287s
user	0m23.704s
sys	0m3.452s
```

**Agent calls Bash**

```bash
python3 -c "
import json; nb=json.load(open('$TMPDIR/w/exec1.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    print('=== cell',i, c['metadata'].get('tags'))
    for o in c.get('outputs',[]):
        if 'text' in o: print(''.join(o['text'])[:6000])
        elif o.get('output_type')=='error': print('ERROR', o['ename'], o['evalue'])
"
```

```
=== cell 1 None
dandiset 002013 version 0.261120.1306

=== cell 3 ['sanity']
                                                    0.261012.0921  0.261120.1306
sub-Monkey-T/sub-Monkey-T_ses-09132024_ecephys.nwb      635366923      870350366
sub-Monkey-T/sub-Monkey-T_ses-09262024_ecephys.nwb     2677518722     2681648047
sub-Monkey-P/sub-Monkey-P_ses-08132018_ecephys.nwb     1376700802     2040584384


subjects in the metadata: 2  files: 3

description: This dataset contains chronic neurochemical and electrophysiological recordings from the striatum of two adult female rhesus monkeys (Macaca mulatta; Monkey P and Monkey T), obtained with shaft-assisted micro-invasive probes (s-µIPs) and collected by the Schwerdt Lab at the University of Pittsburgh. It includes the processed data published on Zenodo (https://doi.org/10.5281/zenodo.14826579) together with the raw recordings from which they were derived. Recordings were made while the monkeys performed reward-biased eye movement tasks, in which the animal fixates a central cue, is shown a value cue signaling a large or small reward, and makes a saccade to a left or right target to obtain reward; trials include forced and free-choice conditions. Electrophysiology was acquired with a Neuralynx Digital Lynx SX system through a unity-gain headstage (HS-36, ±1 mV input range) at 30 kHz (Monkey P) or 32 kHz (Monkey T), bandpass filtered 0.1–7500 Hz. FSCV was performed with a triangular waveform (−0.35 to 1.34 V, 400 V/s) applied at 10 Hz, with current sampled at 25 kHz. For Monkey P (session 08/13/2018), the dataset includes raw broadband electrophysiology from striatal site cl3, spike-sorted units from Plexon Offline Sorter, and threshold-detected spikes with 48-sample waveforms. For Monkey T, session 09/13/2024 includes raw FSCV current and applied voltage from site c8dg together with trial-aligned, PCA-extracted dopamine, pH, motion, and oxidation current (at 0.6 V) time series (10 Hz, 60 s per trial); session 09/26/2024 inc
[... 312 more lines not kept]
```

**Agent**

The full run takes 166 s at 3.3 GB peak. Outcomes are clear. Let me check the attempt schema before writing the record.

**Agent calls Bash**

```bash
cd  && python3 -c "
import json; s=json.load(open('schemas/attempt.schema.json'))
print(json.dumps(s.get('required')), list(s['properties'].keys()))
d=s.get('\$defs',s.get('definitions',{}))
for k in d: 
  if k in ('outcome','finding','dataset','provenance','input'): print(k, json.dumps(d[k])[:1500])
" ; ls questions | head -3; date -u
```

```
["schema_version", "id", "datasets", "paper", "date", "provenance", "outcomes"] ['schema_version', 'id', 'datasets', 'missing_datasets', 'paper', 'date', 'entry', 'deprecated', 'provenance', 'outcomes', 'verifications', 'findings', 'reconciliation', 'inputs', 'findings_review']
README.md
asari-2009.yaml
ashworth-2025.yaml
Tue Nov 24 23:15:04 UTC 2026
```

**Agent calls Bash**

```bash
python3 -c "
import json; s=json.load(open('schemas/attempt.schema.json'))
p=s['properties']
for k in ['outcomes','findings','inputs','provenance']: print(k, json.dumps(p[k])[:2500]); print()
"
```

```
outcomes {"description": "One per claim attempted.", "type": "array", "minItems": 1, "items": {"type": "object", "additionalProperties": false, "required": ["claim", "outcome"], "properties": {"claim": {"description": "Claim id from the target's claims file.", "type": "string"}, "outcome": {"enum": ["reproduced", "partially_reproduced", "not_reproduced", "blocked"], "description": "Describes the result, not the method: whether the effect the claim states was found. Differences in method from the paper go in `deviations`."}, "blocked_by": {"description": "Required when outcome is blocked.", "enum": ["data_missing", "metadata_insufficient", "methods_underspecified", "data_unreadable", "dataset_missing", "too_large", "not_runnable", "other"]}, "notes": {"description": "What differs, or what was missing, stated factually.", "type": "string"}, "notebook": {"description": "Path of the notebook within the entry.", "type": "string"}, "output": {"description": "Which output shows the result, e.g. a cell tag.", "type": "string"}, "measured": {"description": "The values obtained, for claims with expected values: one number, or one per expected value, in the same order.", "oneOf": [{"type": "number"}, {"type": "array", "minItems": 1, "items": {"type": "number"}}]}, "deviations": {"description": "How the test differed from the paper's method or data, e.g. one session of four, or a substituted model.", "type": "array", "items": {"type": "string", "minLength": 1}}, "assumed": {"description": "True when the outcome rests on an assumption about a method the paper leaves open: a choice the paper best supports, stated in a deviation that says what was assumed and why (docs/protocol.md, Author, step 1.6).", "type": "boolean"}, "seed_sensitive": {"type": "boolean", "description": "True when the outcome is not the same under all five seeds the protocol asks for (docs/protocol.md, Author, step 3)."}, "proposed": {"description": "A change of outcome found after the last verification round,
[... 6 more lines not kept]
```

**Agent**

Now the conclusions and summary, written from the printed numbers, plus two small fixes (the spike window uses spikes_PCA.m's 8 pre-threshold samples; the voltage check prints a difference).

**Agent calls Bash**

```bash
cd $TMPDIR/w && python3 - <<'EOF'
p="build.py"; s=open(p).read()
s=s.replace("sta = np.mean([y[i + lag - 9:i + lag + 39] for i in jj], axis=0)","sta = np.mean([y[i + lag - 8:i + lag + 40] for i in jj], axis=0)")
s=s.replace("# compared with the unit's mean stored waveform, in three 600 s segments","# compared with the unit's mean stored waveform, in three 600 s segments. The waveform starts 8 samples before\n# the spike time (prethresholdsamps = 8 in the paper's spikes_PCA.m, doi:10.5281/zenodo.10397773)")
s=s.replace('''f"{volt.min():.3f} to {volt.max():.3f}; all scans read the same voltage: "
      f"{np.allclose(f['stimulus/presentation/fscv_excitation_series/data'][214*1000:214*1001], volt)}")''','''f"{volt.min():.3f} to {volt.max():.3f}; largest difference between scan 1000 and the first scan: "
      f"{np.abs(f['stimulus/presentation/fscv_excitation_series/data'][214*1000:214*1001] - volt).max()*1e3:.2f} mV")''')
open(p,"w").write(s)
EOF
grep -n "prethreshold\|largest difference between scan" build.py | head
```

```
308:# the spike time (prethresholdsamps = 8 in the paper's spikes_PCA.m, doi:10.5281/zenodo.10397773)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
grep -n "all scans read the same" -A1 $TMPDIR/w/build.py; grep -n "i + lag - " $TMPDIR/w/build.py
```

```
186:print(f"voltage of a scan (V): {volt.min():.3f} to {volt.max():.3f}; all scans read the same voltage: "
187-      f"{np.allclose(f['stimulus/presentation/fscv_excitation_series/data'][214*1000:214*1001], volt)}")
325:        sta = np.mean([y[i + lag - 8:i + lag + 40] for i in jj], axis=0)
```

**Agent calls Bash**

```bash
cd $TMPDIR/w && python3 - <<'EOF'
p="build.py"; L=open(p).read().split("\n")
i=[k for k,l in enumerate(L) if "all scans read the same voltage" in l][0]
L[i]='print(f"voltage of a scan (V): {volt.min():.3f} to {volt.max():.3f}; largest difference between scan 1000 and the first scan: "'
L[i+1]="      f\"{np.abs(f['stimulus/presentation/fscv_excitation_series/data'][214*1000:214*1001] - volt).max()*1e3:.2f} mV\")"
open(p,"w").write("\n".join(L))
EOF
sed -n 186,187p build.py
```

```
print(f"voltage of a scan (V): {volt.min():.3f} to {volt.max():.3f}; largest difference between scan 1000 and the first scan: "
      f"{np.abs(f['stimulus/presentation/fscv_excitation_series/data'][214*1000:214*1001] - volt).max()*1e3:.2f} mV")
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/w && python3 - <<'EOF'
p="build.py"; s=open(p).read()
anchor1='''print(f"memory so far {mem_gb():.2f} GB, {time.time()-started:.0f} s")
""", ["sanity"])

md(r"""
### Monkey P, session 08/13/2018
""")'''
assert anchor1 in s
s=s.replace(anchor1, '''print(f"memory so far {mem_gb():.2f} GB, {time.time()-started:.0f} s")
""", ["sanity"])

md(r"""
The bipolar LFP is continuous at 1 kHz over the trials (one interval of 0.5 ms and one of 1.5 ms),
in volts with values within the +-1 mV input range. The raw c3bs minus c3a signal matches it at a
lag of 0 to 1 ms in three segments, so the raw EPhys and the LFP share a clock. The stored filter
setting is 0.1 to 8000 Hz on both channels; the paper and the dataset description give 0.1 to
7500 Hz. Against the trial clock, beta power 0 to 0.5 s after the value cue differs between large
and small reward with the times as stored; with the times moved 1 or 2 s earlier it does not, and
moved later it differs in the other direction, as other task periods follow the cue. This is
consistent with the LFP being on the trial clock, and the shared trial-start codes (description)
fit it; it does not prove it.
""")

md(r"""
### Monkey P, session 08/13/2018
""")''')
anchor2='''print(f"memory so far {mem_gb():.2f} GB, {time.time()-started:.0f} s")
""", ["sanity"])

# ---------------------------------------------------------------- claims'''
assert anchor2 in s
s=s.replace(anchor2, '''print(f"memory so far {mem_gb():.2f} GB, {time.time()-started:.0f} s")
""", ["sanity"])

md(r"""
Monkey P's raw signal is sampled at 30 kHz on the Neuralynx acquisition clock, which the session
description explains. Sorted unit ch33#1 is the thresholded unit 1, and ch33#0 holds units -1 and
0, as the descriptions say. The spike-triggered average of the raw signal at the stored spike
times matches the unit's stored waveform best at a lag of a few samples (printed above, 0.1 ms or
less), so the spikes are on the raw signal's clock. Monkey P has no trials table and its event
codes are not named, so its events cannot be checked against the spikes. A share of the raw
samples sit at the +-1 mV limit of the input range (printed above).
""")

# ---------------------------------------------------------------- claims''')
anchor3='''print(f"slope of table iox change on raw change (lag 0): {np.polyfit(raw[ok], tab[ok], 1)[0]:.3f}")
""", ["sanity"])'''
assert anchor3 in s
s=s.replace(anchor3, anchor3+'''

md(r"""
The raw current at 0.6 V and the table's `iox` change together at lag 0 to 1 scan (z about 18 to
19, against at most about 10 at other lags), so the raw FSCV current, the trial-aligned table and
the trial clock agree to within 0.1 s. The regression slope of the `iox` change on the raw change
(in nA) is about 0.001; `iox` and the other table series are stored with "Units unknown".
""")''')
open(p,"w").write(s)
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent**

Now the result texts and summary.

**Agent calls Bash**

```bash
cat > $TMPDIR/w/results.py <<'PYEOF'
import json, os
R = {}
R["fscv-waveform"] = """**Result: partially reproduced.** Three of four values are within tolerance: the highest
applied potential (1.3395 V), the sweep rate (400.46 V/s) and the scan frequency (9.9999 Hz). The
lowest stored potential is -0.3470 V, outside -0.4 +- 0.04 V, and it is the same across the session
(-0.3479 to -0.3474 V). The dataset description gives -0.35 to 1.34 V, as the stored voltage does;
the paper gives -0.4 to 1.3 V. The holding potential between scans is not stored (the series has a
gap between scans), so whether the electrode was held at -0.4 V there cannot be seen."""
R["ephys-acquisition"] = """**Result: reproduced.** Monkey P's raw series is sampled at 29999.9997 Hz and Monkey T's at
31999.9624 Hz; the Neuralynx settings of both 09/26/2024 channels give a 0.1 Hz low cut and an
8000 Hz high cut. All four are within tolerance, though the stored high cut is 8000 Hz where the
paper and the dataset description state 7500 Hz. Monkey P's file stores no filter settings."""
R["shape-task-structure"] = """**Result: reproduced.** Forced trials are 358 of 1468, 24.39% (within 22.5 to 27.5%). The
large-reward image changes 9 times in the successful forced trials, giving 8 complete blocks of 71
to 273 trials, all within 45 to 330; the first and last blocks, cut by the file, are 61 and 194
trials."""
R["zenodo-link"] = """**Result: reproduced.** The small and left lists agree with the selections decoded here for all
602 and 594 trials; the large and right lists agree for 569 of 570 and 577 of 578 (99.82% and
99.83%). The one trial only here is trial 1501, whose 60 s window ends at 24978.4 s, after the end
of the LFP (24965.4 s). The beta power computed here for the 35th large-reward trial (trial 84)
correlates with the Zenodo trace at r = 0.9421 at lag 0 (best 0.9427 at 6 ms), with a median ratio
of 0.943. The Zenodo example file's field `trial35bigrewardata` holds its time axis, not the LFP,
so the raw example trace itself could not be compared."""
R["fig3a-redox-peaks"] = """**Result: not reproduced.** In the mean background-subtracted voltammogram of the 164
successful forced large-reward trials, the largest value on the rising sweep is at 0.512 V (inside
0.45 to 0.75 V), but the most negative value on the falling sweep is at 0.897 V, outside -0.35 to
-0.05 V. The changes are small: 0.074 nA at most, and -0.014 +- 0.020 nA at 0.608 V and
-0.006 +- 0.018 nA at -0.192 V (mean +- SEM). With the trials of the table only (n=87) neither peak
is in its range; 8 of 164 single trials meet both ranges. With the cue moved by 5 s either way the
peaks fall elsewhere (rising -0.240 and 1.329 V). The raw current is on the trial clock (data
check), so the redox signature of Figure 3A is not visible in the raw current on average. Figure
3A shows one trial, which cannot be identified in the files."""
R["fig3b-beta-bursts"] = """**Result: reproduced.** With the 75th percentile threshold (356.2e-12 V^2) the burst rate over
the 570 successful large-reward trials falls from 1.512 bursts/s before the value cue to 1.207
after it (240 trials fewer, 123 more, 207 equal), Wilcoxon p = 9.5e-10. The rates also differ at
the 50th percentile (0.695 to 1.421, p = 2.5e-47) and the 90th (1.475 to 0.661, p = 2.4e-45), but
the direction depends on the threshold. Every LFP sample lies in some trial window, so the threshold
is the percentile of the whole series."""
R["fig4a-dopamine-reward"] = """**Result: reproduced.** Over 0 to 3 s after the value cue, the re-referenced dopamine has a
median of 1.367 in large-reward trials (n=85) against 0.191 in small-reward trials (n=80),
P(large > small) = 0.603, Mann-Whitney p = 0.0226; 3 trials were dropped for a NaN at the cue. Of
the variants, 1.5 to 3 s gives p = 0.00636 and 0 to 1.5 s p = 0.334; `da` without re-referencing
(p = 0.298) and the re-referenced `iox` (large -0.015, small -0.001, p = 0.446) show no
significant difference. With the cue moved by -10, -5 and +5 s there is no difference (p 0.46 to
0.95); at +10 s the small-reward median is higher (p = 0.00577)."""
R["fig4b-beta-reward"] = """**Result: reproduced.** Over 0 to 0.5 s after the value cue the median beta power is
275.1e-12 V^2 for large reward (n=570) against 327.2e-12 for small (n=602), P(large < small) =
0.597, p = 1.03e-08; divided by the -0.5 to 0 s baseline, 0.455 against 0.553 (p = 1.09e-06). The
difference is confined to this brief window: over 0 to 1 s (p = 0.09) and 0.25 to 0.75 s
(p = 0.658), with or without the baseline, it is not significant, and over 0 to 1 s the large median
is the higher."""
R["fig4c-beta-side"] = """**Result: reproduced.** In large-reward trials the median beta power over 0 to 0.5 s is
244.5e-12 V^2 for left cues (n=282) against 301.9e-12 for right (n=288), P(left < right) = 0.616,
p = 1.61e-06; with the baseline, 0.389 against 0.546 (p = 2.07e-09). Over 0 to 1 s left is also
lower (p = 0.0188; 0.000136 with the baseline); over 0.25 to 0.75 s it is not (p = 0.75 and 0.0751).
Small-reward trials show the same side difference (left 290.3, right 394.2, p = 1.48e-10)."""
R["fig5bc-unit-isolation"] = """**Result: reproduced.** Unit ch33#1 (Plexon unit 1) has 1 interspike interval under 1 ms of
31246 (0.0032%), and its mean stored waveform has a trough of 30.6 uV, 4.58 times the noise of
6.69 uV over the first 600 s of the recording (5.62 and 5.50 times in two later segments). Both
conditions hold. The unsorted cluster ch33#0 has 11.633% of its intervals under 1 ms."""
R["summary"] = """## Summary

| claim | outcome |
|---|---|
| insertion-yield | blocked, data_missing |
| chronic-duration | blocked, data_missing |
| fscv-waveform | partially reproduced |
| ephys-acquisition | reproduced |
| shape-task-structure | reproduced |
| zenodo-link | reproduced (link claim, with Zenodo inputs) |
| fig3a-dual-channel | blocked, data_missing |
| fig3a-redox-peaks | not reproduced |
| fig3b-beta-bursts | reproduced |
| fig4a-dopamine-reward | reproduced |
| fig4b-beta-reward | reproduced |
| fig4c-beta-side | reproduced |
| fig5a-spike-reward | blocked, metadata_insufficient |
| fig5bc-unit-isolation | reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

**How the analysis differs from the paper's.** The paper reports no statistics for Figures 3 to 5;
the tests are those the claims file fixed (Mann-Whitney and Wilcoxon tests on per-trial values),
and its figures show trial averages and single trials. The trial-aligned dopamine is the PCA
output stored in the dataset, re-referenced at the value cue as the claims file says; the PCA was
not re-run. The beta power is computed here from the stored bipolar LFP with the paper's filter
description; it matches the paper's example trace (r = 0.94). For the burst claim the paper does
not define a burst, and the claims file's definition was used. The raw FSCV voltammograms average
all successful forced large-reward trials, where Figure 3A shows one trial.

**What was found about the dataset.** The events, the trials tables, the bipolar LFP, the raw EPhys
and the raw FSCV current agree on one clock (raw against LFP at 0 to 1 ms; raw FSCV against the
trial-aligned table within 0.1 s), and Monkey P's spikes sit on its raw signal. The trial
selections of 09/26/2024 match the paper's Zenodo lists. The dataset lacks the second dopamine
channel (c8ds), the implantation dates and the list of implanted sensors, and a code map for
Monkey P's events, which blocks four claims. The stored acquisition filter is 0.1 to 8000 Hz where
the paper and the description say 7500 Hz; the stored FSCV waveform runs from -0.347 V where the
paper says -0.4 V. Monkey P's site is named cl3 in the electrodes table and ch33 in the unit names
(c33 in the paper). The trial-aligned FSCV series have no units and cover only the first 734 of
1468 trials. The raw FSCV current shows no dopamine redox signature after large-reward cues,
while the stored PCA dopamine of the same trials shows the reward effect."""
json.dump(R, open(os.environ["TMPDIR"] + "/w/results.json", "w"), indent=1)
PYEOF
cd $TMPDIR/w && . $TMPDIR/scratch/bin/activate && python results.py && python build.py entries/amjad-2025/reproduce_amjad_2025.ipynb results.json && echo built
```

```
built
Shell cwd was reset to
```

**Agent**

Now entry.yaml, requirements.in and README, then lock and run.

**Agent calls Bash**

```bash
cd entries/amjad-2025 && cat > entry.yaml <<'EOF'
schema_version: 1
name: amjad-2025
type: reproduction
title: Microinvasive probes for dopamine, LFP and spike recording in monkeys (Amjad et al. 2025)
description: Tests the findings of Amjad, Mahajan, Choi, Shrivastav, Murray, Somich, Coyne and
  Schwerdt (2025) on dandiset 002013, which holds the raw FSCV and trial-aligned dopamine of site
  c8dg (shape task), the raw EPhys and bipolar beta-band LFP of sites c3bs and c3a (direction task)
  of Monkey T, and the raw EPhys and sorted spikes of Monkey P. It checks the recording parameters,
  the task structure, the link to the paper's Zenodo deposit, the reward and side contrasts of
  dopamine and beta power, beta bursts, the raw FSCV voltammograms and the isolation of the sorted
  unit.
license: Apache-2.0
notebooks:
- path: reproduce_amjad_2025.ipynb
  title: Reproducing Amjad et al. (2025) from dandiset 002013
  runtime_minutes: 4
helpers:
- amjad.py
related:
- id: dandi:002013/0.261120.1306
  relation: uses_data
- id: doi:10.1021/acschemneuro.5c00071
  relation: reproduces
EOF
printf "h5py\nmatplotlib\nnumpy\npandas\nremfile\nrequests\nscipy\n" > requirements.in
cat > README.md <<'EOF'
# Amjad et al. (2025) on DANDI:002013

Tests the claims in `claims/amjad-2025.yaml` on version 0.261120.1306 of
[DANDI:002013](https://dandiarchive.org/dandiset/002013/0.261120.1306), streaming the three NWB
files. `reproduce_amjad_2025.ipynb` holds the analysis; `amjad.py` holds the loading and the
measures, each parameter with its source. The claim `zenodo-link` also reads the paper's Zenodo
deposit (doi:10.5281/zenodo.14826579).

Of 14 claims, 8 are reproduced, 1 partially reproduced (fscv-waveform), 1 not reproduced
(fig3a-redox-peaks) and 4 blocked (the second dopamine channel, the implantation dates and list of
implanted sensors, and a code map for Monkey P's events are not in the dataset).

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

Run with `python tools/entry.py all entries/amjad-2025`; it takes about 4 minutes and 3.5 GB of
memory.
EOF
cd ../.. && date -u && python tools/entry.py lock entries/amjad-2025 2>&1 | tail -3
```

```
Tue Nov 24 23:16:12 UTC 2026
wrote amjad-2025/requirements.lock.txt (Python 3.13, with hashes)
```

**Agent calls Bash**

```bash
time python tools/entry.py all entries/amjad-2025 2>&1 | tail -15
```

```
Installed kernelspec registry-amjad-2025 in executed/amjad-2025/.venv/share/jupyter/kernels/registry-amjad-2025
0 error(s)
pass  reproduce_amjad_2025.ipynb  (74 s)

real	1m19.325s
user	0m30.598s
sys	0m4.441s
```

**Agent**

Passed in 74 s. Checking that the executed outputs match the conclusions, especially the cells I changed.

**Agent calls Bash**

```bash
python3 -c "
import json; nb=json.load(open('executed/amjad-2025/reproduce_amjad_2025.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    t=c['metadata'].get('tags') or []
    out=''.join(''.join(o.get('text','')) for o in c.get('outputs',[]))
    if any(e.get('output_type')=='error' for e in c.get('outputs',[])): print('ERROR in', i)
    if i in (11,13,17,21) or any(x.startswith('claim:') for x in t): print('===',i,t); print(out[:2500])
" | grep -v "^$" | head -150
```

```
=== 11 ['sanity']
scans: 241200 of 214 samples; sampling 24999.7 Hz; scan duration 8.56 ms; intervals between scan starts [0.1] s
session covered: 1718.0 to 25838.1 s; trials from 6920.2 to 25710.2 s
current unit: amperes  conversion: 1e-09
current (nA): 1st to 99th percentile over all samples -1392.1 to 1252.9
voltage of a scan (V): -0.347 to 1.339; largest difference between scan 1000 and the first scan: 0.48 mV
trial-aligned table: (734, 601) rate [10.] good [ True] trial_index 0 to 733
start_time equals trial start - 30 s: True
  da: NaN fraction 0.0266, 1st-99th percentile -30.902 to 20.835; PCA-extracted dopamine component. Units unknown. Some samples are NaN in the source data; the reason is not documented.
  iox: NaN fraction 0.0000, 1st-99th percentile -0.805 to 0.599; Oxidation current at about 0.6 V, where dopamine oxidizes. Units unknown.
  ph: NaN fraction 0.0000, 1st-99th percentile -1.168 to 1.159; PCA-extracted pH component. Units unknown.
  m: NaN fraction 0.0000, 1st-99th percentile -0.332 to 0.372; PCA-extracted motion artifact component. Units unknown.
memory so far 1.36 GB, 29 s
=== 13 ['sanity']
raw current at 0.608 V against table iox: largest |z| 19.3 at lag -1 scans (-0.1 s); z at lag 0: 18.4; next largest |z| outside lags -2 to 2: 9.8
slope of table iox change on raw change (lag 0): 0.001
=== 17 ['sanity']
segment at 8000 s: best lag 1 ms, r 0.748; r at lag 0 0.748; raw range -568 to 502 uV
segment at 15000 s: best lag 0 ms, r 0.740; r at lag 0 0.740; raw range -528 to 521 uV
segment at 22000 s: best lag 0 ms, r 0.709; r at lag 0 0.709; raw range -594 to 495 uV
[... 121 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json; nb=json.load(open('executed/amjad-2025/reproduce_amjad_2025.ipynb'))
for i in (18,19,22,23):
    c=nb['cells'][i]; print('===',i,c['cell_type']); print(''.join(''.join(o.get('text','')) for o in c.get('outputs',[])) if c['cell_type']=='code' else ''.join(c['source'])[:300])
"
```

```
=== 18 code
shift +0 s: large median 275.1, small 327.2 (1e-12 V^2), Mann-Whitney p = 1e-08
shift -2 s: large median 123.0, small 115.8 (1e-12 V^2), Mann-Whitney p = 0.84
shift -1 s: large median 525.6, small 532.0 (1e-12 V^2), Mann-Whitney p = 0.71
shift +1 s: large median 431.8, small 343.2 (1e-12 V^2), Mann-Whitney p = 4.7e-08
shift +2 s: large median 351.3, small 332.3 (1e-12 V^2), Mann-Whitney p = 0.075
shift +5 s: large median 434.8, small 261.6 (1e-12 V^2), Mann-Whitney p = 5.1e-34
memory so far 2.99 GB, 44 s

=== 19 markdown
The bipolar LFP is continuous at 1 kHz over the trials (one interval of 0.5 ms and one of 1.5 ms),
in volts with values within the +-1 mV input range. The raw c3bs minus c3a signal matches it at a
lag of 0 to 1 ms in three segments, so the raw EPhys and the LFP share a clock. The stored filter
setti
=== 22 code
unit 1 stored waveforms: (31247, 48), mean trough -30.6 uV at sample 9, peak 17.9 uV
segment from 6801 s: 1195 spikes; STA best lag 2 samples (r 0.699, trough -34.9 uV); r at lag 0 0.595; samples at the +-1 mV input range 0.1069
segment from 11801 s: 1868 spikes; STA best lag 2 samples (r 0.711, trough -35.5 uV); r at lag 0 0.620; samples at the +-1 mV input range 0.0302
segment from 16801 s: 792 spikes; STA best lag 2 samples (r 0.729, trough -35.5 uV); r at lag 0 0.649; samples at the +-1 mV input range 0.0295
memory so far 3.35 GB, 60 s
[... 6 more lines not kept]
```

**Agent**

One sentence in the LFP clock note overstates the +2 s shift (p = 0.075). Fixing it and re-running.

**Agent calls Bash**

```bash
python3 - <<'EOF'
import nbformat
p="entries/amjad-2025/reproduce_amjad_2025.ipynb"
nb=nbformat.read(p,4)
c=nb.cells[19]; old="""and small reward with the times as stored; with the times moved 1 or 2 s earlier it does not, and
moved later it differs in the other direction, as other task periods follow the cue."""
assert old in c.source
c.source=c.source.replace(old,"""and small reward with the times as stored (p = 1e-08); with the times moved 1 or 2 s earlier it does
not (p = 0.71 and 0.84); moved 1 or 5 s later it differs in the other direction, large above small,
and 2 s later it does not (p = 0.075), as other task periods follow the cue.""")
nbformat.write(nb,p)
EOF
python tools/entry.py all entries/amjad-2025 2>&1 | tail -3; date -u
```

```
Installed kernelspec registry-amjad-2025 in executed/amjad-2025/.venv/share/jupyter/kernels/registry-amjad-2025
0 error(s)
pass  reproduce_amjad_2025.ipynb  (73 s)
Tue Nov 24 23:19:07 UTC 2026
```

**Agent**

Entry passes. Now the attempt record, written from a Python dict so the YAML is well-formed.

**Agent calls Bash**

```bash
cat > $TMPDIR/w/record.py <<'PYEOF'
import yaml
NB = "reproduce_amjad_2025.ipynb"
def o(claim, outcome, notes, **kw):
    d = {"claim": claim, "outcome": outcome}
    if outcome == "blocked":
        d["blocked_by"] = kw.pop("blocked_by")
    else:
        d["notebook"] = NB
        d["output"] = f"claim:{claim}"
    if "measured" in kw: d["measured"] = kw.pop("measured")
    d["notes"] = " ".join(notes.split())
    if kw.get("deviations"): d["deviations"] = [" ".join(x.split()) for x in kw.pop("deviations")]
    d.update(kw)
    return d

outcomes = [
 o("insertion-yield", "blocked", """The criterion needs the list of implanted sensors per monkey and whether each
   kept recording. The files hold only the recorded sites (c8dg; c3bs and c3a; cl3, named ch33 in the
   units), and neither the files nor the dandiset metadata list the implanted sensors (14 in monkey T and 9
   in monkey P by the paper).""", blocked_by="data_missing"),
 o("chronic-duration", "blocked", """The criterion needs the implantation date of each site. No text field or
   attribute of the three files and nothing in the dandiset metadata gives one; the fields that mention
   implants are descriptions (notebook cell claim:chronic-duration). The subjects' ages (P11Y, P8Y) are not
   implantation dates.""", blocked_by="data_missing"),
 o("fscv-waveform", "partially_reproduced", """Three of four values are within tolerance. Highest applied
   potential 1.3395 V, sweep rate 400.46 V/s (median step of the rising ramp times 24999.7 Hz), scan
   frequency 9.9999 Hz. The lowest stored potential is -0.3470 V, outside -0.4 +- 0.04 V, and the same across
   the session (-0.3479 to -0.3474 V over 11 blocks of 1000 scans). The dandiset description gives -0.35 to
   1.34 V, as the stored voltage does. The holding potential between scans is not stored (the series has a
   gap between the 214-sample scans), so whether the electrode was held at -0.4 V between scans cannot be
   seen.""", measured=[-0.347, 1.3395, 400.46, 9.9999]),
 o("ephys-acquisition", "reproduced", """Monkey P 29999.9997 Hz from the median timestamp interval of the first
   2e6 samples; Monkey T 31999.9624 Hz from the rate of the 09/26/2024 raw series; the Neuralynx settings of
   both 09/26/2024 channels give DspLowCutFrequency 0.1 Hz and DspHighCutFrequency 8000 Hz. All four are
   within tolerance. The stored high cut is 8000 Hz where the paper and the dandiset description state 7500
   Hz. Monkey P's electrodes table stores no filter settings, and the 09/13/2024 file holds no raw
   EPhys.""", measured=[29999.9997, 31999.9624, 0.1, 8000]),
 o("shape-task-structure", "reproduced", """Forced trials (code 119) are 358 of 1468, 24.39%. In the 303
   successful forced trials (142 with image 81, 161 with image 88, none with both) the large-reward image
   changes 9 times, giving 8 complete blocks of 71, 93, 121, 136, 153, 172, 194 and 273 trials (in session
   order 172, 153, 121, 71, 194, 93, 136, 273), all within 45 to 330; the first and last blocks, cut by the
   file, are 61 and 194 trials. Forced and choice trials (code 120) are disjoint and cover every
   trial.""", measured=[24.39]),
 o("zenodo-link", "reproduced", """Trials matched by number. The Zenodo small and left lists agree with the
   selections decoded here for all 602 and 594 trials; the large and right lists for 569 of 570 and 577 of
   578 (99.82% and 99.83%). The one trial only here is trial 1501, whose 60 s window ends at 24978.4 s, after
   the end of the LFP at 24965.4 s, which likely explains its absence from the paper's lists. The beta power
   computed here for the 35th large-reward trial (trial 84) correlates with the Zenodo trace at r = 0.9421 at
   lag 0 and 0.9427 at the best lag of 6 ms, median ratio 0.943. The dataset's measures match the paper's
   published values (the trace) and the dataset's own trial codes give the paper's lists, so the link holds on
   both sides. The example file's field trial35bigrewardata holds the time axis, not the LFP, so the raw
   example trace could not be compared.""", deviations=["The 35th trial of the large-reward list is read as the
   35th entry of the Zenodo list (trial 84), as the file name and the claims file say."]),
 o("fig3a-dual-channel", "blocked", """The criterion needs the trial-aligned dopamine of both c8dg and c8ds. The
   09/13/2024 file holds c8dg only, and the paper's Zenodo deposit holds only a c8dg file
   (FSCV_trlists_c8dg_09132024_firsthalf.mat). Not deciding, the c8dg half alone has a mean change above zero
   over 0 to 3 s in 65.9% of 85 forced large-reward trials with a value.""", blocked_by="data_missing"),
 o("fig3a-redox-peaks", "not_reproduced", """In the mean background-subtracted voltammogram of the 164
   successful forced large-reward trials, the largest rising-sweep value (0.074 nA) is at 0.512 V, inside
   0.45 to 0.75 V, but the most negative falling-sweep value (-0.048 nA) is at 0.897 V, outside -0.35 to
   -0.05 V. At 0.608 V the mean change is -0.014 +- 0.020 nA and at -0.192 V -0.006 +- 0.018 nA (SEM). With
   the 87 trials of the trial-aligned table (trials 0 to 733) neither peak is in range (1.152 and 0.865 V); 8
   of 164 single trials meet both ranges. Small-reward trials (reference) peak at 1.217 and -0.321 V. With the
   cue moved by 5 s either way the peaks fall elsewhere. The raw current is on the trial clock (session-wide
   cross-correlation of the raw 0.6 V current with the table's iox peaks at lag 0 to 1 scan, z 18.4 to 19.3).
   Figure 3A shows a single trial that cannot be identified in the files, so the mean over trials is the
   criterion's test, not the paper's display.""", deviations=["All 164 successful forced large-reward trials of the
   session are averaged, as the raw current covers the whole session; the 87 in the trial-aligned table are
   shown as a variant and give the same outcome."]),
 o("fig3b-beta-bursts", "reproduced", """With the 75th percentile threshold (356.2e-12 V^2) and bursts of at
   least 50 ms, the burst rate over 570 successful large-reward trials is 1.512 bursts/s in -1 to 0 s and
   1.207 in 0 to 1 s from the value cue (240 trials fewer after, 123 more, 207 equal), Wilcoxon p = 9.5e-10.
   The variants also differ, at the 50th percentile 0.695 to 1.421 (p = 2.5e-47) and at the 90th 1.475 to
   0.661 (p = 2.4e-45), so the rate changes at every threshold but its direction depends on the
   threshold.""", deviations=["The threshold is the percentile over all trial windows, read as the union of the
   60 s windows of the trials table; they cover every LFP sample, so it is the percentile of the whole
   series."]),
 o("fig4a-dopamine-reward", "reproduced", """168 successful forced trials have a row in the trial-aligned table
   (87 large, 81 small); 3 are dropped for a NaN at the value cue. Mean re-referenced da over 0 to 3 s,
   median 1.367 for large (n=85) and 0.191 for small (n=80), P(large > small) 0.603, Mann-Whitney p = 0.0226.
   Variants, not deciding; 1.5 to 3 s p = 0.00636, 0 to 1.5 s p = 0.334, da as stored p = 0.298, and the
   re-referenced iox shows no difference (large -0.015, small -0.001, p = 0.446). With the cue moved by -10,
   -5 and +5 s there is no difference (p 0.46 to 0.95); at +10 s small is higher (p = 0.00577). The table
   covers only trials 0 to 733 of 1468, as the paper's Zenodo file does.""", deviations=["The window 0 to 3 s
   takes the 30 samples after the cue sample (samples +1 to +30), a standard choice; the cue sample is the
   nearest 10 Hz sample, as the claims file says."]),
 o("fig4b-beta-reward", "reproduced", """Mean beta power over 0 to 0.5 s after the value cue, median 275.1e-12
   V^2 for large reward (n=570) against 327.2e-12 for small (n=602), P(large < small) 0.597, p = 1.03e-08;
   divided by the -0.5 to 0 s baseline 0.455 against 0.553 (p = 1.09e-06). The difference is confined to the
   brief window; over 0 to 1 s (p = 0.09, large median higher) and 0.25 to 0.75 s (p = 0.658) it is not
   significant, with or without the baseline."""),
 o("fig4c-beta-side", "reproduced", """In successful large-reward trials, mean beta power over 0 to 0.5 s,
   median 244.5e-12 V^2 for left cues (n=282) against 301.9e-12 for right (n=288), P(left < right) 0.616,
   p = 1.61e-06; with the baseline 0.389 against 0.546 (p = 2.07e-09). Over 0 to 1 s left is also lower
   (p = 0.0188; 0.000136 with the baseline), over 0.25 to 0.75 s not (p = 0.75 and 0.0751). Small-reward
   trials show the same side difference (290.3 against 394.2, p = 1.48e-10)."""),
 o("fig5a-spike-reward", "blocked", """The criterion needs the value cue time and reward size of each trial.
   Monkey P's file has no trials table, and its 36 event codes are stored as 'TTL code N' with the
   description 'The code map for this session is not available'. The paper's Zenodo deposit holds the same
   20812 events (session126_events.mat, inspected while preparing, not in the notebook) as Neuralynx TTL
   strings without names, and the paper's code (doi:10.5281/zenodo.10397773, spikes_PCA.m, ISI_Plot.m,
   percent_recovery.mlx) does not name them. The direction-task code map of the 2024 sessions cannot be
   carried over, as the 2018 codes differ (for example no code 128 and no code 101).""",
   blocked_by="metadata_insufficient"),
 o("fig5bc-unit-isolation", "reproduced", """Unit ch33#1 (Plexon unit 1, identical to thresholded unit 1) has 1
   interspike interval under 1 ms of 31246 (0.0032%). Its mean stored waveform has a trough of 30.6 uV, 4.58
   times the noise of 6.69 uV (MAD/0.6745 of the 300 to 6000 Hz signal) over the first 600 s of the
   recording, and 5.62 and 5.50 times in two later 600 s segments. The unsorted cluster ch33#0 has 11.633% of
   its intervals under 1 ms. In the first segment 10.7% of raw samples sit at the +-1 mV input
   limit.""", measured=[0.0032, 4.58], deviations=["The 600 s of the noise estimate are the first 600 s of the
   recording, a standard choice; two later segments are shown and give the same outcome. The band-pass is a
   4th-order Butterworth run forwards and backwards, a standard choice."]),
]

findings = [
 {"kind": "data_missing", "severity": "major", "statement": """The second channel of the dual-channel probe
   (site c8ds), whose dopamine the paper shows with c8dg in Figure 3A, is not in the dataset; the 09/13/2024
   file holds c8dg only."""},
 {"kind": "metadata_insufficient", "severity": "major", "statement": """Monkey P's session (08/13/2018) has no
   trials table and its event codes have no names ('The code map for this session is not available'), so the
   value cue, the reward size and the trials of the direction task cannot be identified, and the
   reward-related spiking of Figure 5A cannot be tested."""},
 {"kind": "data_missing", "severity": "minor", "statement": """No implantation dates and no list of implanted
   sensors are given in the files or the dandiset metadata, so the days post-implant and the insertion yields
   the paper reports cannot be checked."""},
 {"kind": "metadata_error", "severity": "minor", "statement": """The Neuralynx settings stored for both
   09/26/2024 channels give a high cut of 8000 Hz, while the dandiset description (and the paper) state a
   band-pass of 0.1 to 7500 Hz."""},
 {"kind": "other", "about": "data", "severity": "minor", "statement": """The stored FSCV applied voltage runs from
   -0.347 to 1.340 V, as the dandiset description says (-0.35 to 1.34 V), where the paper states -0.4 to 1.3
   V. The holding potential between scans is not stored."""},
 {"kind": "metadata_insufficient", "severity": "minor", "statement": """Monkey P's recording site is named cl3 in
   the electrodes table and the descriptions, while the sorted units are named ch33#0 and ch33#1 and the paper
   names the site c33."""},
 {"kind": "metadata_insufficient", "severity": "minor", "statement": """The trial-aligned FSCV series (da, iox,
   ph, m) are stored with 'Units unknown', and the table covers only trials 0 to 733 of the 1468 trials of
   09/13/2024 without saying so. The regression slope of the iox change on the raw current change in nA is
   about 0.001."""},
 {"kind": "other", "about": "data", "severity": "minor", "statement": """The raw FSCV current of c8dg, which is on
   the trial clock, shows no dopamine redox signature after large-reward value cues on average (falling-sweep
   minimum at 0.897 V, change at 0.6 V of -0.014 +- 0.020 nA), and the stored iox shows no reward
   difference, while the stored PCA dopamine of the same trials does (p = 0.0226). The data do not show
   whether this is an error or a small signal."""},
 {"kind": "other", "about": "data", "severity": "minor", "statement": """Monkey P's raw signal reaches the +-1 mV
   limit of the input range in 3.0 to 10.7% of samples in the three 600 s segments checked."""},
 {"kind": "other", "about": "data", "severity": "none", "statement": """The events, the trials tables, the bipolar
   LFP, the raw EPhys and the raw FSCV current agree on one clock (raw against LFP at lag 0 to 1 ms, raw FSCV
   against the trial-aligned table within 0.1 s), Monkey P's spikes lie on its raw signal within 0.1 ms, the
   events are stored once each, and the trial selections of 09/26/2024 match the paper's Zenodo lists except
   the last trial."""},
 {"kind": "other", "about": "paper", "statement": """In the paper's Zenodo deposit the file
   09262024_c3bs-c3a_data_trial35bigrewardexample.mat stores the time axis in the field meant for the example
   LFP (trial35bigrewardata equals trial35bigrewardataTS), so the example trace of Figure 3B is not
   deposited."""},
]
for fd in findings:
    fd["statement"] = " ".join(fd["statement"].split())
    # put statement after kind for readability
rec = {
 "schema_version": 3,
 "id": "amjad-2025-02",
 "datasets": [{"archive": "dandi", "id": "002013", "version": "0.261120.1306",
               "doi": "10.48324/dandi.002013/0.261120.1306", "relation": "primary"}],
 "paper": "doi:10.1021/acschemneuro.5c00071",
 "date": "2026-11-24",
 "entry": "amjad-2025",
 "provenance": {"kind": "agent", "accountable": {"name": "CatalystNeuro"},
                "agent": {"harness": "Claude Code", "model": "claude-opus-5-5", "protocol": "pilot-18"},
                "runner": {"platform": "GitHub Actions",
                           "url": "https://github.com/encorescience/encore-registry/actions/runs/45504266872"}},
 "inputs": [
  {"what": " ".join("""The paper's processed data on Zenodo; the four trial lists of session 09/26/2024 (large
     reward, small reward, left, right; successful trials) and the example beta power trace of the 35th
     large-reward trial, used by zenodo-link only. session126_events.mat was inspected for a code map of
     Monkey P's events and has none.""".split()), "source": "doi:10.5281/zenodo.14826579"},
  {"what": " ".join("""The paper's spike plotting code (spikes_PCA.m, ISI_Plot.m), read for the sorted unit
     (unit 1) and the 8 samples before threshold of the stored waveforms, used to align the spike-triggered
     average in the data check.""".split()), "source": "doi:10.5281/zenodo.10397773"},
 ],
 "outcomes": outcomes,
 "findings": findings,
}
yaml.SafeDumper.ignore_aliases = lambda *a: True
open("attempts/amjad-2025-02.yaml", "w").write(yaml.safe_dump(rec, sort_keys=False, allow_unicode=True, width=105))
PYEOF
python3 $TMPDIR/w/record.py && grep -n ": .*: " attempts/amjad-2025-02.yaml | grep -v "^\s*[0-9]*:\s*-\? *[a-z_]*: ['\"]" | head; python tools/entry.py check entries/amjad-2025 2>&1 | tail -3
```

```
File "/tmp/claude-1001/w/record.py", line 52
    example trace could not be compared.""", deviations=["The 35th trial of the large-reward list is read as the
                                                         ^
SyntaxError: unterminated string literal (detected at line 52)
0 error(s)
```

**Agent calls Bash**

```bash
cd $TMPDIR/w && python3 - <<'EOF'
s=open("record.py").read()
s=s.replace('deviations=["','deviations=["""')
import re
s=re.sub(r'\."\]\)', '."""])', s)
s=s.replace('give the same outcome."]', 'give the same outcome."""]').replace('a standard choice."])','a standard choice."""])')
open("record.py","w").write(s)
EOF
grep -n 'deviations=\|"""\])' record.py | head -20; cd  && python3 $TMPDIR/w/record.py && python tools/entry.py check entries/amjad-2025 2>&1 | tail -3
```

```
52:   example trace could not be compared.""", deviations=["""The 35th trial of the large-reward list is read as the
53:   35th entry of the Zenodo list (trial 84), as the file name and the claims file say."""]),
67:   criterion's test, not the paper's display.""", deviations=["""All 164 successful forced large-reward trials of the
69:   shown as a variant and give the same outcome."""]),
75:   threshold.""", deviations=["""The threshold is the percentile over all trial windows, read as the union of the
77:   series."""]),
84:   covers only trials 0 to 733 of 1468, as the paper's Zenodo file does.""", deviations=["""The window 0 to 3 s
86:   nearest 10 Hz sample, as the claims file says."""]),
110:   limit.""", measured=[0.0032, 4.58], deviations=["""The 600 s of the noise estimate are the first 600 s of the
112:   4th-order Butterworth run forwards and backwards, a standard choice."""]),
0 error(s)
```

**Agent calls Bash**

```bash
sed -i 's/limit.""", measured=\[0.0032, 4.58\], deviations/limit.""", deviations/' $TMPDIR/w/record.py && python3 $TMPDIR/w/record.py && python3 - <<'EOF'
import yaml,re
t=open("attempts/amjad-2025-02.yaml").read()
d=yaml.safe_load(t); print(len(d["outcomes"]), [ (x["claim"],x["outcome"]) for x in d["outcomes"]])
# plain scalar lines containing ': ' beyond the key
for i,l in enumerate(t.splitlines()):
    m=re.match(r"^\s*-?\s*[A-Za-z_]+: (.*)$", l)
    rest = m.group(1) if m else l.strip()
    if ": " in rest and not rest.startswith(("'",'"')): print(i+1, l[:120])
EOF
python tools/entry.py check entries/amjad-2025 2>&1 | tail -2; sed -n 1,40p attempts/amjad-2025-02.yaml
```

```
14 [('insertion-yield', 'blocked'), ('chronic-duration', 'blocked'), ('fscv-waveform', 'partially_reproduced'), ('ephys-acquisition', 'reproduced'), ('shape-task-structure', 'reproduced'), ('zenodo-link', 'reproduced'), ('fig3a-dual-channel', 'blocked'), ('fig3a-redox-peaks', 'not_reproduced'), ('fig3b-beta-bursts', 'reproduced'), ('fig4a-dopamine-reward', 'reproduced'), ('fig4b-beta-reward', 'reproduced'), ('fig4c-beta-side', 'reproduced'), ('fig5a-spike-reward', 'blocked'), ('fig5bc-unit-isolation', 'reproduced')]
0 error(s)
schema_version: 3
id: amjad-2025-02
datasets:
- archive: dandi
  id: '002013'
  version: 0.261120.1306
  doi: 10.48324/dandi.002013/0.261120.1306
  relation: primary
paper: doi:10.1021/acschemneuro.5c00071
date: '2026-11-24'
entry: amjad-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
sed -i 's/limit of the input range in 3.0 to 10.7% of samples/limit of the input range in 2.9 to 10.7% of samples/' $TMPDIR/w/record.py && python3 $TMPDIR/w/record.py && grep -c "2.9 to 10.7" attempts/amjad-2025-02.yaml && python tools/entry.py all entries/amjad-2025 2>&1 | tail -2 && python tools/entry.py handover entries/amjad-2025 2>&1 | tail -5; ls executed/amjad-2025/handover; date -u
```

```
1
pass  reproduce_amjad_2025.ipynb  (73 s, reused)
reused the executed copies of 2026-11-24 23:19 UTC: nothing the run reads has changed since (hash efdad61de651). Nothing was executed and no environment was built; --fresh runs it again.
wrote executed/amjad-2025/handover
amjad-2025.yaml
amjad.py
reproduce_amjad_2025.ipynb
Tue Nov 24 23:20:53 UTC 2026
```

**Agent calls Bash**

```bash
python3 -c "
import json; nb=json.load(open('executed/amjad-2025/handover/reproduce_amjad_2025.ipynb'))
print(len(nb['cells']), sum(''.join(c['source']).startswith('**Result') for c in nb['cells']), any('## Summary' in ''.join(c['source']) for c in nb['cells']))"; ls entries/amjad-2025
```

```
52 0 False
README.md
__pycache__
amjad.py
entry.yaml
reproduce_amjad_2025.ipynb
requirements.in
requirements.lock.txt
```

**Agent calls Bash**

```bash
rm -rf entries/amjad-2025/__pycache__ && python tools/entry.py check entries/amjad-2025 2>&1 | tail -1
```

```
0 error(s)
```

**Agent**

I tested all 14 claims on DANDI:002013 version 0.261120.1306: 8 reproduced, 1 partially reproduced, 1 not reproduced and 4 blocked. The entry is at `entries/amjad-2025/` and the record at `attempts/amjad-2025-02.yaml`. `python tools/entry.py all` passed with 0 errors, and the handover package is in `executed/amjad-2025/handover/`. I did not verify my own work, and nothing is committed.

**1. Outcomes**

| claim | outcome | key numbers |
|---|---|---|
| insertion-yield | blocked, data_missing | the list of implanted sensors is not in the dataset |
| chronic-duration | blocked, data_missing | no implantation dates anywhere in the files or metadata |
| fscv-waveform | partially reproduced | lowest potential -0.347 V (paper says -0.4 ± 0.04); 1.34 V, 400.5 V/s and 10 Hz are within tolerance |
| ephys-acquisition | reproduced | 30000 Hz and 31999.96 Hz; stored filter 0.1 to 8000 Hz (paper says 7500, still within tolerance) |
| shape-task-structure | reproduced | forced trials 24.39%; 8 complete blocks of 71 to 273 trials |
| zenodo-link (uses Zenodo data) | reproduced | trial lists agree 99.82 to 100%; example beta trace r = 0.94 at a 6 ms lag |
| fig3a-dual-channel | blocked, data_missing | the second channel (c8ds) is not in the dataset or on Zenodo |
| fig3a-redox-peaks | not reproduced | in the raw current, the most negative value on the falling sweep is at 0.897 V, not near -0.2 V; changes are under 0.08 nA |
| fig3b-beta-bursts | reproduced | burst rate 1.51 → 1.21 per s, p = 9.5e-10 (the direction flips with the threshold) |
| fig4a-dopamine-reward | reproduced | large-reward median 1.37 vs small 0.19, p = 0.023 |
| fig4b-beta-reward | reproduced | p = 1e-8 over 0 to 0.5 s; not significant over wider windows |
| fig4c-beta-side | reproduced | left vs right p = 1.6e-6 |
| fig5a-spike-reward | blocked, metadata_insufficient | Monkey P's event codes have no names and there is no trials table |
| fig5bc-unit-isolation | reproduced | 0.0032% of spike intervals under 1 ms; waveform trough 4.58 times the noise |

**2. The dataset**
- **Clocks:** the events, trials tables, bipolar LFP, raw EPhys and raw FSCV share one clock. Raw EPhys and the LFP line up within 0 to 1 ms. The raw FSCV current lines up with the trial-aligned table within 0.1 s, but only when compared across the whole session; single trials are too noisy to show it. Monkey P's spikes sit on its raw signal within 0.1 ms.
- **Missing:** the second dopamine channel (c8ds), the implantation dates, the list of implanted sensors, and a code map and trials table for Monkey P.
- **Mismatches with the paper:** the stored filter high cut is 8000 Hz where the paper and the description say 7500 Hz. The stored FSCV waveform starts at -0.347 V where the paper says -0.4 V; the dataset description agrees with the files.
- **Smaller problems:** Monkey P's site is named cl3 in the electrodes table, ch33 in the unit names and c33 in the paper. The trial-aligned FSCV series have no units and cover only trials 0 to 733 of 1468, without saying so. Monkey P's raw signal sits at the ±1 mV input limit in 2.9 to 10.7% of samples.
- **Raw FSCV:** the raw current, and the stored oxidation current at 0.6 V, show no dopamine signal after large-reward cues, while the stored PCA dopamine of the same trials does. I rated this minor because the data do not show whether it is an error or a small signal.
- **Zenodo deposit:** the example-trial file stores its time axis in the field meant for the LFP trace, so the Figure 3B example trace is not deposited. I recorded this as a finding about the paper.
- **Assumptions:** no outcome rests on one. The details I chose (the 600 s noise segment, the edges of the dopamine window, and reading "all trial windows" as the union of the 60 s windows, which turns out to cover every sample) are standard choices that do not change any outcome.
- **Questions:** none for the paper's authors, and none for a reader.
- **Earlier results:** I did not seek out earlier attempts. However, the claims file's opening comment describes an earlier look at the data: it says the raw 09/26 EPhys and Monkey P's spikes were offset from the trial clock, that events repeated about five times, and that the raw FSCV could not be matched to the trial-aligned traces. I read this before my own analysis. In this version the events are stored once each and the offsets are not present. The finding that the raw FSCV current shows no dopamine contrast at the value cue is the same as that comment reports.

**3. Where the protocol was unclear**
1. Step 1.3 asks to show how versions differ, but this is a blind repeat. I only listed the file sizes of both published versions and did not compare their contents.
2. Link claims are meant to be written by the author, but `zenodo-link` was already in the claims file. I tested it as written.
3. The protocol does not say whether a blocked claim may have a tagged output cell. I added one to fig3a-dual-channel showing the c8dg half, marked as not deciding.
4. The severity scale gives only a ceiling ("at most major") for problems the data cannot settle. I rated the raw-FSCV finding minor and said why.
5. Findings about the paper's own Zenodo deposit fit neither the "data" nor the "paper" category cleanly. I filed it under the paper, since the deposit is not the dataset.
6. `measured` is described as being for claims with expected values, so I left it out of claims that have none.
7. The Zenodo events file for Monkey P was inspected while preparing but is not read in the notebook. Its finding (no code map) is only cited in the notes and decides no number.

**4. Runtime and failures**
The notebook runs in 73 s with a peak of 3.35 GB of memory; my work took about 32 minutes (22:48 to 23:21 UTC). Nothing failed in the final run. During development there were a few script bugs (an array reshape, string quoting, a cast from a missing value), all fixed before the final run.

## End of run

67 turns, 25 minutes, $5.42 at API prices, result: success.
