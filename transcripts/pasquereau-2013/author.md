# pasquereau-2013 · author · run 45857382971

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cd  ls; ls docs entries attempts claims paper; wc -l docs/*.md README.md
```

```
Thu Nov 26 16:21:09 UTC 2026
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
[... 1145 more lines not kept]
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
3	Version: `pilot-19`. Record this version in the attempt's provenance.
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
[... 794 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/pasquereau-2013.yaml"
}
```

```
1	# Claims for Pasquereau & Turner (2013) on dandiset 001636.
2	# Source: the full text in PubMed Central (PMC3840326, open access, CC BY), read from its Methods,
3	# Results, Table 1 and figure legends, and its supplementary data sheet (DataSheet1.PDF), whose
4	# table gives the neuronal results for each monkey separately.
5	# Quotes and statistics added 2026-10-19 from the full text (Europe PMC PMC3840326).
6	#
7	# When these criteria were written, the author had seen the data check only: the file list and
8	# metadata, the contents of the files, the counts of units by subject, MPTP state and projection
9	# type, the number of torque perturbations per direction (none in any monkey L file), the timing
10	# of the torque command against the trials table, the sign of the joint angle, which EMG channels
11	# hold data, and the cross-referenced and repeated files. These counts showed that the monkey V
12	# units with at least 5 perturbations per direction number 112 before and 159 after MPTP, with
13	# 49 and 54 PTNs and 31 and 48 CSNs, as in the supplementary table. No SDF, response detection,
14	# kinematic measure or EMG response had been computed.
15	#
16	# The dandiset marks no torque perturbation in any monkey L file, so every claim is tested on
17	# monkey V (elbow), and the expected values are the paper's monkey V values where it gives them
18	# (supplementary table). Where the paper gives only values pooled over both monkeys, these are
19	# the expected values and the difference is a deviation.
20	#
[... 760 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md | head -80; ls -la entries/fouke-2025 entries/pasquereau-2013; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in; ls papers/datasets | grep pasq; cat papers/datasets/pasquereau-2013.yaml; ls questions | grep pasq; ls papers/author-notes 2>/dev/null | grep pasq
```

```
# Encore Science: the registry

Encore Science checks datasets against the papers they came from. This repository holds its public record, the Encore registry, served at <https://encorescience.org>. The protocol the checks follow, and the `encore` command that runs the same check on your own data, are in [encore-protocol](https://github.com/encorescience/encore-protocol). It is developed by [CatalystNeuro](https://www.catalystneuro.com).

Agents, and people, try to reproduce the key findings of papers from the open
data in public archives, starting with the [DANDI Archive](https://dandiarchive.org), and register the result
here: the notebooks when it works, and the reason when it does not.

- **For the archive:** evidence of whether each dandiset is complete and
  accurate enough to support the findings of its paper.
- **For analysts:** working notebooks to build new analyses on.

Status: pilot. All eight pilot targets have been attempted and checked by an
independent agent.

**Site:** <https://encorescience.org/>, with the registry's dashboard at <https://encorescience.org/registry/> and what Encore offers a journal at <https://encorescience.org/journals/>.

## Reading the outcomes

An outcome says what one attempt could recover from the data in a dandiset,
[... 108 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/fouke-2025-01.yaml | head -150; cat entries/fouke-2025/README.md; sed -n 1,80p entries/fouke-2025/omr.py
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
[... 244 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 150,400p attempts/fouke-2025-01.yaml | grep -n -A12 "^findings\|^verif" | head -60; ls schemas tools; sed -n '/## DANDI/,/^## [A-Z]/p' docs/archives.md | head -120
```

```
95:findings:
96-- kind: data_missing
97-  statement: The dandiset holds only the freely swimming tracking of Figure 1 and Figure S1. The
98-    two-photon imaging and the head-fixed tail tracking behind Figures 2 to 4 are not in it, and
99-    the GitLab repository the paper names for all behavioural and imaging data holds analysis
100-    notebooks only. Nine of the paper's main findings cannot be tested.
101-- kind: metadata_insufficient
102-  statement: The stimulus codes 0 to 20 have no names or description in the files or the
103-    dandiset metadata. They can be named only from the paper's analysis notebook and the protocol
104-    file of its stimulus software.
105-- kind: code_mismatch
106-  statement: The paper's analysis notebook labels code 9 as lateral right and 11 as lateral left,
107-    while its conversion of the stimulus software's names gives the reverse (it carries a remap
--
165:verifications:
166-- date: '2026-10-14'
167-  kind: agent
168-  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
169-  reviewed: The first executed notebook with the conclusion cells and the summary removed, the helper
170-    module and the claims file, with the paper's accepted manuscript (PMC12218792). The verifier
[... 79 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -c paper/*.txt; grep -n "" paper/10.3389-fnsys.2013.00098.txt | sed -n '/[Mm]aterials and [Mm]ethods\|MATERIALS/,$p' | head -5
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.3389-fnsys.2013.00098.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
t=open('paper/10.3389-fnsys.2013.00098.txt').read()
i=t.find('Supplementary Material'); print(len(t)); 
for k in ['SUPPLEMENT','Supplementary Table','Venus','monkey V ']:
  print(k,[j for j in range(len(t)) if t.startswith(k,j)][:20])
"; python3 -c "
t=open('paper/10.3389-fnsys.2013.00098.txt').read()
print(t[-9000:])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/001636/versions/0.261124.1906/ | python3 -c "
import json,sys; d=json.load(sys.stdin); print(json.dumps({k:d.get(k) for k in ['name','description','assetsSummary','version','doi','dateModified','datePublished','relatedResource']},indent=1)[:5000])"; curl -s https://api.dandiarchive.org/api/dandisets/001636/versions/ | python3 -m json.tool | grep -E '"version"|modified|status'
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
import json, urllib.request
url="https://api.dandiarchive.org/api/dandisets/001636/versions/0.261124.1906/assets/?page_size=1000"
assets=[]
while url:
    d=json.load(urllib.request.urlopen(url)); assets+=d['results']; url=d['next']
print(len(assets))
json.dump(assets,open('assets.json','w'))
import collections
subj=collections.Counter(a['path'].split('/')[0] for a in assets); print(subj)
for a in assets[:5]+[a for a in assets if 'Venus' in a['path'] or 'V' in a['path'].split('/')[0]][:10]: print(a['path'],a['size'])
EOF
```

```
439
Counter({'sub-Venus': 291, 'sub-Leu': 148})
sub-Leu/sub-Leu_ses-Leu++l10003++PreMPTP++Depth23680um++19930123_behavior+ecephys.nwb 759682
sub-Leu/sub-Leu_ses-Leu++l10101++PreMPTP++Depth24200um++19930124_behavior+ecephys.nwb 915215
sub-Leu/sub-Leu_ses-Leu++l10002++PreMPTP++Depth23080um++19930123_behavior+ecephys.nwb 801006
sub-Leu/sub-Leu_ses-Leu++l10001++PreMPTP++Depth25700um++19930123_behavior+ecephys.nwb 916332
sub-Leu/sub-Leu_ses-Leu++l10102++PreMPTP++Depth22000um++19930124_behavior+ecephys.nwb 780456
sub-Venus/sub-Venus_ses-Venus++v0502++PreMPTP++Depth22130um++19990406_behavior+ecephys.nwb 4918459
sub-Venus/sub-Venus_ses-Venus++v1002++PreMPTP++Depth19800um++19990409_behavior+ecephys.nwb 4744519
sub-Venus/sub-Venus_ses-Venus++v1001++PreMPTP++Depth19000um++19990409_behavior+ecephys.nwb 4108702
sub-Venus/sub-Venus_ses-Venus++v1003++PreMPTP++Depth20000um++19990409_behavior+ecephys.nwb 4451349
sub-Venus/sub-Venus_ses-Venus++v0601++PreMPTP++Depth19500um++19990407_behavior+ecephys.nwb 4740830
sub-Venus/sub-Venus_ses-Venus++v1005++PreMPTP++Depth17880um++19990412_behavior+ecephys.nwb 4871204
sub-Venus/sub-Venus_ses-Venus++v1006++PreMPTP++Depth18770um++19990412_behavior+ecephys.nwb 5176442
sub-Venus/sub-Venus_ses-Venus++v1004++PreMPTP++Depth20470um++19990409_behavior+ecephys.nwb 3928963
sub-Venus/sub-Venus_ses-Venus++v1102++PreMPTP++Depth17410um++19990413_behavior+ecephys.nwb 2809589
sub-Venus/sub-Venus_ses-Venus++v1101++PreMPTP++Depth17900um++19990413_behavior+ecephys.nwb 2967793
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; uv venv -q env -p 3.12 2>&1 | tail -2; . env/bin/activate; uv pip install -q pynwb remfile h5py dandi numpy scipy pandas matplotlib statsmodels nbformat nbclient ipykernel 2>&1 | tail -3; python -c "import pynwb,remfile;print(pynwb.__version__)"; grep -n "python" tools/entry.py | head -20
```

```
4.2.0
3:    python tools/entry.py lock  entries/<name>   # pin the environment
4:    python tools/entry.py check entries/<name>   # validate metadata and conventions
5:    python tools/entry.py check entries/*/       # the same for every entry, in one process
6:    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
7:    python tools/entry.py all   entries/<name>   # check, then run
8:    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies
206:        if entry.get("python") and locked_for and locked_for.group(1) != str(entry["python"]):
208:                         f"says {entry['python']}; run `tools/entry.py lock`")
496:LOCK_VERSION = re.compile(r"--python-version\s+(\d+\.\d+)")
499:def python_of(entry_dir: Path) -> str:
500:    """The Python version an entry runs on: its entry.yaml's `python`, else the version its lock was compiled for
503:    if entry.get("python"):
504:        return str(entry["python"])
513:def set_python(entry_dir: Path, version: str) -> None:
514:    """Write `python: "<version>"` into entry.yaml, replacing the field or adding it after `license`."""
517:    line = f'python: "{version}"'
518:    if re.search(r"^python:.*$", text, re.M):
519:        text = re.sub(r"^python:.*$", line, text, count=1, flags=re.M)
529:    version = version or python_of(entry_dir)
[... 2 more lines not kept]
```

**Agent**

Environment ready. Now opening a Venus file to list everything it holds.

**Agent calls Bash**

```bash
cd $TMPDIR; . env/bin/activate; python - <<'EOF'
import json, remfile, h5py, pynwb, numpy as np
assets=json.load(open('assets.json'))
a=[a for a in assets if 'v1002' in a['path']][0]
url=f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/"
f=remfile.File(url); h=h5py.File(f,'r')
io=pynwb.NWBHDF5IO(file=h,load_namespaces=True); nwb=io.read()
print(nwb)
print(nwb.session_description, nwb.session_start_time, nwb.subject)
print(nwb.experiment_description)
for k,v in nwb.acquisition.items(): print('ACQ',k,v)
for k,m in nwb.processing.items():
    print('PROC',k,m.description)
    for n,d in m.data_interfaces.items(): print('   ',n,d)
print(nwb.intervals)
t=nwb.trials.to_dataframe(); print(t.columns.tolist()); print(t.head(10).T); print(len(t))
for c in nwb.trials.columns: print(c.name,':',c.description)
u=nwb.units.to_dataframe(); print(u.drop(columns=['spike_times']).T)
for c in nwb.units.columns: print(c.name,':',c.description)
print(nwb.electrodes.to_dataframe())
EOF
```

```
<persisted-output>
Output too large (37.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/155a8601-92de-4a23-b130-93410661849c/tool-results/ba22q7e5x.txt

Preview (first 2KB):
root pynwb.file.NWBFile at 0x132921412575568
Fields:
  acquisition: {
    EMGBrachioradialis <class 'pynwb.base.TimeSeries'>,
    EMGDeltoidPosterior <class 'pynwb.base.TimeSeries'>,
    EMGTrapezius <class 'pynwb.base.TimeSeries'>,
    EMGTricepsLateralis <class 'pynwb.base.TimeSeries'>,
    EMGTricepsLongus1 <class 'pynwb.base.TimeSeries'>,
    EMGTricepsLongus2 <class 'pynwb.base.TimeSeries'>,
    ElbowAngle <class 'pynwb.behavior.SpatialSeries'>,
    ElbowTorque <class 'pynwb.base.TimeSeries'>
  }
  devices: {
    DeviceMicroelectrodeRecording <class 'pynwb.device.Device'>,
    DeviceMicrowirePeduncleStimulation <class 'pynwb.device.Device'>,
    DeviceMicrowirePutamenStimulation1 <class 'pynwb.device.Device'>,
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 40,400p /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/155a8601-92de-4a23-b130-93410661849c/tool-results/ba22q7e5x.txt
```

```
[6 rows x 12 columns]
  file_create_date: [datetime.datetime(2026, 11, 20, 16, 45, 3, 469264, tzinfo=tzoffset(None, -21600))]
  identifier: 29aa0e33-d693-4896-9c6f-7f58a08ade3d
  institution: University of Pittsburgh
  intervals: {
    AntidromicSweepsIntervals <class 'pynwb.epoch.TimeIntervals'>,
    invalid_times <class 'pynwb.epoch.TimeIntervals'>,
    trials <class 'pynwb.epoch.TimeIntervals'>
  }
  invalid_times: invalid_times <class 'pynwb.epoch.TimeIntervals'>
  keywords: <StrDataset for HDF5 dataset "keywords": shape (7,), type "|O">
  lab: Turner Lab
  lab_meta_data: {
    hed_schema <class 'abc.HedLabMetaData'>,
    localization <class 'abc.Localization'>
  }
  notes: TEMPORAL DATA STRUCTURE: This dataset was converted from trialized MATLAB files where all timestamps were relative to individual trial starts. Inter-trial intervals were NOT recorded in the source data.

SESSION TIMING: Recording dates are accurate from experimental logs, but precise session start times within each day are not available. session_start_time is set to midnight (Pittsburgh timezone) for every session, including sessions recorded on the same date.

[... 342 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 400,600p /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/155a8601-92de-4a23-b130-93410661849c/tool-results/ba22q7e5x.txt
```

```
lateral_target_appearance_time : Time (in seconds) when peripheral target appeared (go cue), signaling the monkey to initiate movement toward the flexion or extension target
cursor_departure_time : Time (in seconds) when cursor exited the center target zone following the go cue
reward_time : Time (in seconds) of liquid reward delivery for successful target acquisition and hold
target_amplitude_degrees : Distance from center (home) position to target center in degrees of joint angle (10, 20, or 30). Determines required movement amplitude for target capture. During individual sessions, target amplitude is either always 20 degrees or varies randomly among 10, 20, and 30 degrees.
isolation_monitoring_stim_time : Time (in seconds) of antidromic stimulation pulse delivered during trial to monitor unit isolation. Single pulses were delivered early in some trials (~245 ms after trial start) to activate otherwise silent neurons and verify recording isolation. NaN indicates no stimulation was delivered in that trial
isolation_monitoring_stim_site : Anatomical target of antidromic stimulation for isolation monitoring. Values: 'posterolateral striatum', 'ventrolateral thalamus', 'cerebral peduncle', 'subthalamic nucleus', or empty string if no stimulation was delivered in that trial
movement_type : flexion or extension
source_file : Source MATLAB file of this trial, without the unit number (e.g. 'v1501' for v1501.1.mat). Sessions merged from several files of the same day list each trial's own file.
torque_perturbation_type : direction of torque perturbation causing muscle stretch (flexion/extension/none). 'not_available' in monkey L files, whose source data contain no perturbation times.
torque_perturbation_onset_time : Time (in seconds) of torque perturbation onset, from the lab's event markers (Events.tq_flex and Events.tq_ext). NaN on trials without a perturbation, and in every monkey L trial, where the perturbation times are not available. Note: Pasquereau and Turner (2013)
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/work; cd $TMPDIR/work; . ../env/bin/activate; cat > survey.py <<'EOF'
import json, time, remfile, h5py, numpy as np, pandas as pd, sys
from concurrent.futures import ThreadPoolExecutor
assets=json.load(open('../assets.json'))
def url(a): return f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/"
def survey(a):
    h=h5py.File(remfile.File(url(a)),'r')
    tr=h['intervals/trials']
    out={'path':a['path']}
    def col(n):
        d=tr[n][:]; 
        return d.astype(str) if d.dtype.kind in 'OS' else d
    out['n_trials']=len(tr['start_time'])
    tt=col('torque_perturbation_type'); out['tq']=pd.Series(tt).value_counts().to_dict()
    out['src']=sorted(set(col('source_file')))
    u=h['units']
    out['units']=[dict(name=n.decode() if isinstance(n,bytes) else n, ptype=p.decode() if isinstance(p,bytes) else p, post=bool(q), lat=float(l), lat2=float(l2))
       for n,p,q,l,l2 in zip(u['unit_name'][:],u['neuron_projection_type'][:],u['is_post_mptp'][:],u['antidromic_latency_ms'][:],u['antidromic_latency_2_ms'][:])]
    out['acq']={k:(h['acquisition'][k]['data'].shape) for k in h['acquisition']}
    ts=h['acquisition'][[k for k in h['acquisition'] if 'Angle' in k][0]]['timestamps']
    out['dt']=float(np.median(np.diff(ts[:2000])))
    out['date']=h['session_start_time'][()].decode()
    return out
if __name__=='__main__':
    sel=[a for a in assets if a['path'].endswith('.nwb')]
    if len(sys.argv)>1: sel=sel[:int(sys.argv[1])]
    t=time.time()
    with ThreadPoolExecutor(8) as ex: res=list(ex.map(survey,sel))
    print(time.time()-t)
    json.dump(res,open('survey.json','w'))
EOF
python survey.py 16 && python -c "
import json;r=json.load(open('survey.json'));[print(x['path'][-60:],x['n_trials'],x['tq'],x['src'],len(x['units']),x['dt'],list(x['acq'])) for x in r]"
```

```
6.842933893203735
l10003++PreMPTP++Depth23680um++19930123_behavior+ecephys.nwb 30 {'not_available': 30} ['l10003'] 1 0.009999999999999787 ['WristAngle', 'WristTorque']
l10101++PreMPTP++Depth24200um++19930124_behavior+ecephys.nwb 30 {'not_available': 30} ['l10101'] 2 0.009999999999999787 ['WristAngle', 'WristTorque']
l10002++PreMPTP++Depth23080um++19930123_behavior+ecephys.nwb 30 {'not_available': 30} ['l10002'] 2 0.009999999999999787 ['WristAngle', 'WristTorque']
l10001++PreMPTP++Depth25700um++19930123_behavior+ecephys.nwb 30 {'not_available': 30} ['l10001'] 2 0.009999999999999787 ['WristAngle', 'WristTorque']
l10102++PreMPTP++Depth22000um++19930124_behavior+ecephys.nwb 30 {'not_available': 30} ['l10102'] 2 0.009999999999999787 ['WristAngle', 'WristTorque']
l10103++PreMPTP++Depth22900um++19930124_behavior+ecephys.nwb 30 {'not_available': 30} ['l10103'] 2 0.009999999999999787 ['WristAngle', 'WristTorque']
l10603++PreMPTP++Depth22130um++19930313_behavior+ecephys.nwb 36 {'not_available': 36} ['l10603'] 2 0.009999999999999787 ['WristAngle', 'WristTorque']
l10602++PreMPTP++Depth21820um++19930313_behavior+ecephys.nwb 26 {'not_available': 26} ['l10602'] 2 0.009999999999999787 ['WristAngle', 'WristTorque']
l10601++PreMPTP++Depth22990um++19930313_behavior+ecephys.nwb 36 {'not_available': 36} ['l10601'] 2 0.009999999999999787 ['WristAngle', 'WristTorque']
l10501++PreMPTP++Depth24700um++19930312_behavior+ecephys.nwb 36 {'not_available': 36} ['l10501'] 2 0.009999999999999787 ['WristAngle', 'WristTorque']
l10701++PreMPTP++Depth23030um++19930315_behavior+ecephys.nwb 22 {'not_available': 22} ['l10701'] 1 0.009999999999999787 ['WristAngle', 'WristTorque']
l10802++PreMPTP++Depth22750um++19930315_behavior+ecephys.nwb 36 {'not_available': 36} ['l10802'] 1 0.009999999999999787 ['WristAngle', 'WristTorque']
l10902++PreMPTP++Depth22310um++19930316_behavior+ecephys.nwb 36 {'not_available': 36} ['l10902'] 2 0.009999999999999787 ['WristAngle', 'WristTorque']
l11001++PreMPTP++Depth21850um++1
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/work; . ../env/bin/activate; python survey.py && python - <<'EOF'
import json, pandas as pd, collections
r=json.load(open('survey.json'))
rows=[]
for x in r:
    subj='V' if 'Venus' in x['path'] else 'L'
    for u in x['units']:
        rows.append(dict(subj=subj,path=x['path'],date=x['date'][:10],n_tr=x['n_trials'],flex=x['tq'].get('flexion',0),ext=x['tq'].get('extension',0),na=x['tq'].get('not_available',0),nsrc=len(x['src']),**u))
df=pd.DataFrame(rows); df.to_csv('units.csv',index=False)
print(len(r), df.groupby('subj').size())
print(df.groupby(['subj','post','ptype']).size())
V=df[df.subj=='V']; ok=V[(V.flex>=5)&(V.ext>=5)]
print('V >=5 each', ok.groupby(['post','ptype']).size(), ok.groupby('post').size())
print('L tq', df[df.subj=='L'].na.sum(), df[df.subj=='L'][['flex','ext']].sum())
print('dup names', df.name.duplicated().sum(), df[df.name.duplicated(keep=False)][['path','name']])
print('dt', collections.Counter(round(x['dt'],4) for x in r))
print(collections.Counter(tuple(sorted(x['acq'])) for x in r if 'Venus' in x['path']))
print('multi-src files', [(x['path'][-55:],x['src']) for x in r if len(x['src'])>1][:20])
print('units per file', collections.Counter(len(x['units']) for x in r))
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/work/survey.py", line 27, in <module>
    with ThreadPoolExecutor(8) as ex: res=list(ex.map(survey,sel))
                                          ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/.local/share/uv/python/cpython-3.12.16-linux-x86_64-gnu/lib/python3.12/concurrent/futures/_base.py", line 619, in result_iterator
    yield _result_or_cancel(fs.pop())
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/.local/share/uv/python/cpython-3.12.16-linux-x86_64-gnu/lib/python3.12/concurrent/futures/_base.py", line 317, in _result_or_cancel
    return fut.result(timeout)
           ^^^^^^^^^^^^^^^^^^^
  File "/home/runner/.local/share/uv/python/cpython-3.12.16-linux-x86_64-gnu/lib/python3.12/concurrent/futures/_base.py", line 449, in result
    return self.__get_result()
           ^^^^^^^^^^^^^^^^^^^
  File "/home/runner/.local/share/uv/python/cpython-3.12.16-linux-x86_64-gnu/lib/python3.12/concurrent/futures/_base.py", line 401, in __get_result
    raise self._exception
  File "/home/runner/.local/share/uv/python/cpython-3.12.16-linux-x86_64-gnu/lib/python3.12/concurrent/futures/thread.py", line 59, in run
    result = self.fn(*self.args, **self.kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/work/survey.py", line 19, in survey
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/work; . ../env/bin/activate; sed -i "s/    ts=h\['acquisition'\].*/    ks=[k for k in h['acquisition'] if 'Angle' in k]\n    out['dt']=float(np.median(np.diff(h['acquisition'][ks[0]]['timestamps'][:2000]))) if ks else None/; /out\['dt'\]=float(np.median(np.diff(ts/d" survey.py; grep -n dt survey.py; python survey.py && python - <<'EOF'
import json, pandas as pd, collections
r=json.load(open('survey.json'))
rows=[]
for x in r:
    subj='V' if 'Venus' in x['path'] else 'L'
    for u in x['units']:
        rows.append(dict(subj=subj,path=x['path'],date=x['date'][:10],n_tr=x['n_trials'],flex=x['tq'].get('flexion',0),ext=x['tq'].get('extension',0),na=x['tq'].get('not_available',0),nsrc=len(x['src']),**u))
df=pd.DataFrame(rows); df.to_csv('units.csv',index=False)
print(len(r), df.groupby('subj').size())
print(df.groupby(['subj','post','ptype']).size())
V=df[df.subj=='V']; ok=V[(V.flex>=5)&(V.ext>=5)]
print('V >=5 each', ok.groupby(['post','ptype']).size(), ok.groupby('post').size())
print('L tq', df[df.subj=='L'].na.sum(), df[df.subj=='L'][['flex','ext']].sum())
print('dup names', df.name.duplicated().sum(), df[df.name.duplicated(keep=False)][['path','name']])
print('dt', collections.Counter(None if x['dt'] is None else round(x['dt'],4) for x in r))
print(collections.Counter(tuple(sorted(x['acq'])) for x in r))
print('multi-src files', [(x['path'][-55:],x['src']) for x in r if len(x['src'])>1][:20])
print('units per file', collections.Counter(len(x['units']) for x in r))
EOF
```

```
11:        return d.astype(str) if d.dtype.kind in 'OS' else d
20:    out['dt']=float(np.median(np.diff(h['acquisition'][ks[0]]['timestamps'][:2000]))) if ks else None
294.4026081562042
439 subj
L    210
V    356
dtype: int64
subj  post   ptype                                     
L     False  corticostriatal_neuron                        25
             no_response                                   84
             pyramidal_tract_and_subthalamic_neuron         1
             pyramidal_tract_neuron                        19
             subthalamic_and_corticostriatal_neuron         1
             subthalamic_and_thalamic_neuron                1
             subthalamic_projection_neuron                  7
      True   corticostriatal_neuron                        10
             no_response                                   46
             pyramidal_tract_neuron                        10
             subthalamic_projection_neuron                  6
V     False  corticostriatal_neuron                        51
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/work; . ../env/bin/activate; python - <<'EOF'
import json, remfile, h5py, numpy as np
assets=json.load(open('../assets.json'))
a=[a for a in assets if 'v1002' in a['path']][0]
h=h5py.File(remfile.File(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/"),'r')
tr=h['intervals/trials']
st=tr['start_time'][:]; on=tr['torque_perturbation_onset_time'][:]; ct=tr['center_target_appearance_time'][:]; typ=tr['torque_perturbation_type'][:].astype(str)
print(np.c_[st,ct,on,on-st,on-ct][:12], typ[:12])
u=h['units']; print(list(u.keys())); print(u['obs_intervals_index'][:], u['spike_times_index'][:])
ts=h['acquisition/ElbowAngle/timestamps'][:]; d=h['acquisition/ElbowAngle/data'][:,0]; tq=h['acquisition/ElbowTorque/data'][:]
print(ts[:5], np.unique(np.round(np.diff(ts),4),return_counts=True))
for i in np.where(np.isfinite(on))[0][:6]:
    j=np.searchsorted(ts,on[i]); print(typ[i], np.round(tq[j-5:j+60:5]-tq[j-5],1), np.round(d[j:j+150:15]-d[j],1))
for k in h['acquisition']:
    x=h['acquisition'][k]['data'][:]; print(k, np.nanmin(x),np.nanmax(x),np.isnan(x).sum())
EOF
```

```
[[  0.      2.612   4.351   4.351   1.739]
 [ 12.159  14.819     nan     nan     nan]
 [ 22.495  23.792  25.488   2.993   1.696]
 [ 33.602  36.418     nan     nan     nan]
 [ 45.277  47.478  49.174   3.897   1.696]
 [ 57.106  59.21   60.906   3.8     1.696]
 [ 68.699  71.72   73.417   4.718   1.697]
 [ 81.823  83.461  85.158   3.335   1.697]
 [ 92.765  94.988  96.685   3.92    1.697]
 [104.671 106.681 108.377   3.706   1.696]
 [116.526 118.275     nan     nan     nan]
 [128.141 130.631     nan     nan     nan]] ['flexion' 'none' 'extension' 'none' 'flexion' 'extension' 'extension'
 'flexion' 'extension' 'flexion' 'none' 'none']
['antidromic_latency_2_ms', 'antidromic_latency_ms', 'antidromic_stimulation_sites', 'antidromic_threshold', 'antidromic_threshold_2', 'electrodes', 'electrodes_index', 'id', 'is_post_mptp', 'neuron_projection_type', 'obs_intervals', 'obs_intervals_index', 'receptive_field_location', 'receptive_field_stimulus', 'spike_times', 'spike_times_index', 'unit_name']
[20] [3957]
[0.    0.001 0.002 0.003 0.004] (array([1.000e-03, 3.005e+00, 3.006e+00]), array([169356,      7,     12]))
flexion [ 0.  -0.6  9.  81.8 93.  91.4 91.  90.4 91.  90.4 91.  90.4 85. ] [0.  0.1 0.6 1.6 2.8 3.7 4.  4.  3.6 2.9]
extension [  0.   -0.5 -14.  -86.8 -90.  -91.5 -91.  -92.1 -92.  -92.1 -91.  -91.4
 -82. ] [ 0.  -0.  -0.7 -1.5 -2.7 -3.5 -4.  -3.9 -3.6 -3. ]
flexion [ 0.   0.6 15.  87.4 91.  90.9 92.  91.4 92.  91.4 92.  91.4 83. ] [0.  0.1 0.7 1.5 2.6 3.5 3.8 3.7 3.3 2.6]
[... 14 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/pasquereau-2013/pasq.py",
 "content": "\"\"\"Loading and measures for the torque perturbation data of dandiset 001636 (monkey V).\n\nPasquereau & Turner (2013), Front. Syst. Neurosci. 7:98, doi:10.3389/fnsys.2013.00098.\n\nEach NWB file holds one recording (one or two units) with a trials table whose\n`torque_perturbation_type` and `torque_perturbation_onset_time` mark the perturbations, the elbow\nangle and the torque command at 1 kHz, and up to six EMG channels. Files are streamed from the\narchive at the pinned version with remfile and h5py (reading the NWB paths directly is much\nfaster than building the pynwb objects of 291 files); nothing is written to disk. Only windows\naround each perturbation are kept.\n\nWhere the parameters come from. \"Claims\" means the opening comment and criteria of\nclaims/pasquereau-2013.yaml, which cite the paper's Methods; \"Methods\" means the paper's\nMethods, Data analysis.\n\n- Cells studied: units with at least 5 perturbations of each direction (Methods, \"for neurons\n  studied during at least 5 repetitions of each torque direction\"; claims).\n- SDF: spikes convolved at 1 ms with a gamma kernel, k = 1.5, theta = 20 ms (Methods). The\n  kernel is truncated at 400 ms, where its tail is below 1e-7 of its mass (a standard choice\n  that cannot change a result).\n- Baseline: the 500 ms before onset (Methods; claims). Detection: the trial-averaged SDF of one\n  direction against its baseline mean +/- t * SD of its 500 baseline values, t the two-tailed\n  critical value at p = 0.002 with 499 degrees of freedom (claims; the degrees of freedom are a\n  standard choice for 500 samples). A response starts where the SDF leaves the threshold band\n  between 20 and 60 ms, having been inside it the ms before (claims; Methods, \"between 20-60-ms\").\n- Offset: the first ms after onset where the SDF is back inside the band, searched to the end of\n  the 200 ms post-torque epoch (Methods: \"the time point at which the SDF first returned within\n  the p = 0.002 threshold\"; the 200 ms limit is the Methods' post-torque epoch, and a response\n  still outside the band at 200 ms ends there).\n- Magnitudes over onset to offset, signed so that a response's own direction is positive (claims):\n  mean change from baseline, maximum change, area (spikes), and the mean SDF (the Methods' \"mean\n  firing rate during the response\"). FWHM: the contiguous span around the response's peak, within\n  0 to 400 ms, where the signed change is at least half the peak change (claims; \"full-width\n  half-maximum\" in the Methods).\n- DSI = |1 - NP/P|, NP and P the signed maximum changes from baseline over 0 to 200 ms of the two\n  directions, P the larger in absolute value (Methods).\n- Kinematics (claims): 25 Hz low-pass FIR with a Hamming window applied forwards and backwards\n  (101 taps at 1 kHz, a standard choice), velocity by differences, onset where the velocity first\n  exceeds 5 deg/s in the torque's direction within 0 to 200 ms, peak velocity over 0 to 200 ms,\n  amplitude the largest displacement over 0 to 300 ms, all signed so that the torque's direction\n  is positive. Flexion torque moves the angle to positive values (checked in the notebook).\n- EMG (claims): session-average trace for flexion torques less its mean over the 200 ms before\n  onset; m1 = mean over 15 to 40 ms, m2 = mean over 41 to 80 ms; a response starts at the first\n  ms from 10 to 150 ms above 2 SD of the baseline and lasts while it stays above.\n\"\"\"\n\nfrom __future__ import annotations\n\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nfrom dandi.dandiapi import DandiAPIClient\nfrom scipy import signal, stats\n\nDANDISET_ID = \"001636\"\nDANDISET_VERSION = \"0.261124.1906\"\n\nMIN_PERTURBATIONS = 5\nGAMMA_K, GAMMA_THETA_MS = 1.5, 20.0\nKERNEL_MS = 400\nBASELINE_MS = 500\nEPOCH_MS = 200\nONSET_WINDOW_MS = (20, 60)\nP_THRESHOLD = 0.002\nT_CRIT = float(stats.t.ppf(1 - P_THRESHOLD / 2, BASELINE_MS - 1))\nPSEUDO_SHIFT_MS = 600          # claims, false-positive-rate: pseudo onset 600 ms before torque\n\n# Spike windows kept around each perturbation, ms relative to torque onset. The earliest time is\n# the pseudo onset's baseline (-1100 ms) less the kernel's reach.\nSPIKE_WINDOW_MS = (-1500, 500)\nANGLE_WINDOW_MS = (-200, 400)\nEMG_WINDOW_MS = (-300, 300)\nTORQUE_WINDOW_MS = (-50, 100)\nEMG_CHANNELS = [\"EMGTricepsLongus1\", \"EMGTricepsLongus2\", \"EMGTricepsLateralis\",\n                \"EMGDeltoidPosterior\", \"EMGTrapezius\", \"EMGBrachioradialis\"]\nTRICEPS = [\"EMGTricepsLongus1\", \"EMGTricepsLongus2\", \"EMGTricepsLateralis\"]\n\nLOWPASS_HZ, FIR_TAPS = 25.0, 101\nVELOCITY_THRESHOLD = 5.0       # deg/s, Methods\nEMG_BASELINE_MS = 200\nM1_MS, M2_MS = (15, 40), (41, 80)\nEMG_SEARCH_MS = (10, 150)\n\n\ndef asset_urls(subject: str = \"sub-Venus\") -> list[tuple[str, str]]:\n    \"\"\"(path, streaming URL) of every NWB file of a subject at the pinned version.\"\"\"\n    with DandiAPIClient() as client:\n        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)\n        return sorted((a.path, a.get_content_url(follow_redirects=1, strip_query=True))\n                      for a in dandiset.get_assets()\n                      if a.path.endswith(\".nwb\") and a.path.startswith(subject + \"/\"))\n\n\ndef _str(values) -> np.ndarray:\n    return np.array([v.decode() if isinstance(v, bytes) else str(v) for v in values])\n\n\ndef _ragged(h, name):\n    data, index = h[name][:], h[name + \"_index\"][:]\n    starts = np.r_[0, index[:-1]]\n    return [data[s:e] for s, e in zip(starts, index)]\n\n\ndef _windows(ts, data, onsets, window_ms):\n    \"\"\"Samples of a 1 kHz series from onset + window[0] to onset + window[1] (ms), NaN outside.\"\"\"\n    n = window_ms[1] - window_ms[0]\n    out = np.full((len(onsets), n), np.nan)\n    for i, t in enumerate(onsets):\n        j = np.searchsorted(ts, t + window_ms[0] / 1000 - 1e-7)\n        seg = data[j:j + n]\n        tseg = ts[j:j + n]\n        if len(seg) == n and abs(tseg[-1] - tseg[0] - (n - 1) / 1000) < 1e-6:\n            out[i] = seg\n    return out\n\n\ndef load_file(path: str, url: str) -> dict:\n    \"\"\"Trials, units and perturbation-aligned windows of one file.\"\"\"\n    with h5py.File(remfile.File(url), \"r\") as h:\n        tr = h[\"intervals/trials\"]\n        trials = pd.DataFrame({\n            \"start\": tr[\"start_time\"][:], \"stop\": tr[\"stop_time\"][:],\n            \"center\": tr[\"center_target_appearance_time\"][:],\n            \"torque\": _str(tr[\"torque_perturbation_type\"][:]),\n            \"onset\": tr[\"torque_perturbation_onset_time\"][:],\n            \"movement\": _str(tr[\"movement_type\"][:]),\n            \"source_file\": _str(tr[\"source_file\"][:]),\n        })\n        u = h[\"units\"]\n        spikes = _ragged(u, \"spike_times\")\n        obs = [o.reshape(-1, 2) for o in _ragged(u, \"obs_intervals\")]\n        units = pd.DataFrame({\n            \"unit_name\": _str(u[\"unit_name\"][:]),\n            \"ptype\": _str(u[\"neuron_projection_type\"][:]),\n            \"post\": u[\"is_post_mptp\"][:].astype(bool),\n            \"latency\": u[\"antidromic_latency_ms\"][:],\n            \"latency_2\": u[\"antidromic_latency_2_ms\"][:],\n        })\n        pert = trials[trials.torque.isin([\"flexion\", \"extension\"])].reset_index(drop=True)\n        acq = h[\"acquisition\"]\n        out = {\"path\": path, \"session\": h[\"session_id\"][()].decode(),\n               \"date\": h[\"session_start_time\"][()].decode()[:10], \"trials\": trials,\n               \"units\": units, \"pert\": pert, \"emg\": {}, \"angle\": None, \"torque_cmd\": None}\n        if \"ElbowAngle\" in acq:\n            ts = acq[\"ElbowAngle/timestamps\"][:]\n            out[\"angle\"] = _windows(ts, acq[\"ElbowAngle/data\"][:, 0], pert.onset.values,\n                                    ANGLE_WINDOW_MS)\n            out[\"torque_cmd\"] = _windows(ts, acq[\"ElbowTorque/data\"][:], pert.onset.values,\n                                         TORQUE_WINDOW_MS)\n            for ch in EMG_CHANNELS:\n                if ch in acq:\n                    out[\"emg\"][ch] = _windows(acq[ch + \"/timestamps\"][:], acq[ch + \"/data\"][:],\n                                              pert.onset.values, EMG_WINDOW_MS)\n    # Spike times relative to each perturbation, kept only where the unit was observed over the\n    # whole spike window.\n    w0, w1 = SPIKE_WINDOW_MS[0] / 1000, SPIKE_WINDOW_MS[1] / 1000\n    rel, observed = [], []\n    for st, ob in zip(spikes, obs):\n        r, o = [], []\n        for t in pert.onset.values:\n            inside = np.any((ob[:, 0] <= t + w0) & (ob[:, 1] >= t + w1))\n            o.append(inside)\n            r.append(st[(st >= t + w0) & (st < t + w1)] - t)\n        rel.append(r)\n        observed.append(np.array(o))\n    out[\"rel_spikes\"], out[\"observed\"] = rel, observed\n    out[\"n_spikes\"] = [len(s) for s in spikes]\n    out[\"spikes_all\"] = spikes\n    out[\"obs\"] = obs\n    return out\n\n\ndef load_all(paths_urls, workers: int = 8) -> list[dict]:\n    with ThreadPoolExecutor(workers) as ex:\n        return list(ex.map(lambda pu: load_file(*pu), paths_urls))\n\n\n# ---------------------------------------------------------------- spike density functions\n\ndef gamma_kernel() -> np.ndarray:\n    t = np.arange(KERNEL_MS) + 0.5\n    k = stats.gamma.pdf(t, GAMMA_K, scale=GAMMA_THETA_MS)\n    return k / k.sum() * 1000.0       # spikes/s for one spike\n\n\nKERNEL = gamma_kernel()\n\n\ndef sdf_trials(rel_spikes: list[np.ndarray]) -> np.ndarray:\n    \"\"\"Single-trial SDFs (spikes/s) at 1 ms over SPIKE_WINDOW_MS, causal gamma kernel.\"\"\"\n    n = SPIKE_WINDOW_MS[1] - SPIKE_WINDOW_MS[0]\n    out = np.zeros((len(rel_spikes), n))\n    for i, s in enumerate(rel_spikes):\n        idx = np.floor(s * 1000).astype(int) - SPIKE_WINDOW_MS[0]\n        idx = idx[(idx >= 0) & (idx < n)]\n        train = np.bincount(idx, minlength=n).astype(float)\n        out[i] = np.convolve(train, KERNEL)[:n]\n    return out\n\n\ndef ms_index(t_ms: int) -> int:\n    return t_ms - SPIKE_WINDOW_MS[0]\n\n\ndef detect(mean_sdf: np.ndarray, zero_ms: int = 0) -> dict:\n    \"\"\"Response of one trial-averaged SDF around `zero_ms` (0 = torque onset, -600 = pseudo).\"\"\"\n    z = ms_index(zero_ms)\n    base = mean_sdf[z - BASELINE_MS:z]\n    mu, sd = base.mean(), base.std(ddof=1)\n    lo, hi = mu - T_CRIT * sd, mu + T_CRIT * sd\n    post = mean_sdf[z:z + EPOCH_MS + 200]\n    outside = (post > hi) | (post < lo)\n    res = {\"baseline\": mu, \"sd\": sd, \"responds\": False, \"any_crossing\": bool(outside[:EPOCH_MS].any())}\n    # signed max change over 0-200 ms for the DSI\n    ch = post[:EPOCH_MS] - mu\n    res[\"max_change_signed\"] = float(ch[np.argmax(np.abs(ch))])\n    for t in range(ONSET_WINDOW_MS[0], ONSET_WINDOW_MS[1] + 1):\n        if outside[t] and not outside[t - 1]:\n            sign = 1.0 if post[t] > hi else -1.0\n            end = t\n            while end < EPOCH_MS and outside[end] and np.sign(post[end] - mu) == sign:\n                end += 1\n            seg = sign * (post[t:end] - mu)\n            peak = t + int(np.argmax(seg))\n            half = seg.max() / 2\n            full = sign * (post - mu)\n            a = peak\n            while a > 0 and full[a - 1] >= half:\n                a -= 1\n            b = peak\n            while b < len(full) - 1 and full[b + 1] >= half:\n                b += 1\n            res.update(responds=True, onset=t, offset=end, sign=sign,\n                       mean_change=float(seg.mean()), max_change=float(seg.max()),\n                       area=float(seg.sum() / 1000.0), mean_rate=float(post[t:end].mean()),\n                       fwhm=float(b - a + 1))\n            break\n    return res\n\n\n# ---------------------------------------------------------------- kinematics and EMG\n\n_FIR = signal.firwin(FIR_TAPS, LOWPASS_HZ, fs=1000.0, window=\"hamming\")\n\n\ndef kinematics(angle_windows: np.ndarray, directions: np.ndarray) -> pd.DataFrame:\n    \"\"\"Per perturbation: onset latency (ms), peak velocity (deg/s), amplitude (deg).\"\"\"\n    z = -ANGLE_WINDOW_MS[0]\n    rows = []\n    for a, d in zip(angle_windows, directions):\n        if np.isnan(a).any():\n            rows.append((np.nan, np.nan, np.nan))\n            continue\n        s = 1.0 if d == \"flexion\" else -1.0\n        filt = signal.filtfilt(_FIR, [1.0], a)\n        vel = s * np.gradient(filt) * 1000.0\n        disp = s * (filt - filt[z])\n        above = np.where(vel[z:z + 200] > VELOCITY_THRESHOLD)[0]\n        rows.append((float(above[0]) if len(above) else np.nan,\n                     float(vel[z:z + 200].max()), float(disp[z:z + 300].max())))\n    return pd.DataFrame(rows, columns=[\"latency\", \"peak_velocity\", \"amplitude\"])\n\n\ndef emg_measures(windows: np.ndarray) -> dict:\n    \"\"\"m1, m2, response onset and duration of a session-average EMG trace (flexion torques).\"\"\"\n    z = -EMG_WINDOW_MS[0]\n    trace = np.nanmean(windows, axis=0)\n    base = trace[z - EMG_BASELINE_MS:z]\n    trace = trace - base.mean()\n    sd = base.std(ddof=1)\n    out = {\"m1\": float(trace[z + M1_MS[0]:z + M1_MS[1] + 1].mean()),\n           \"m2\": float(trace[z + M2_MS[0]:z + M2_MS[1] + 1].mean()),\n           \"baseline_sd\": float(sd), \"has_nan\": bool(np.isnan(windows).all(axis=0)[z - EMG_BASELINE_MS:z + 151].any()),\n           \"onset\": np.nan, \"duration\": np.nan}\n    above = trace[z:z + 300] > 2 * sd\n    for t in range(EMG_SEARCH_MS[0], EMG_SEARCH_MS[1] + 1):\n        if above[t]:\n            e = t\n            while e < len(above) and above[e]:\n                e += 1\n            out[\"onset\"], out[\"duration\"] = float(t), float(e - t)\n            break\n    return out\n"
}
```

```
File created successfully at: entries/pasquereau-2013/pasq.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR/work; . ../env/bin/activate; export PYTHONPATH=entries/pasquereau-2013; python - <<'EOF'
import time, pickle, resource, pasq
t=time.time(); pu=pasq.asset_urls(); print(len(pu), time.time()-t)
t=time.time(); d=pasq.load_all(pu[:8]); print('8 files', time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,'GB')
x=d[0]; print(x['session'], x['units'], len(x['pert']), x['angle'].shape, {k:v.shape for k,v in x['emg'].items()}, [o.sum() for o in x['observed']])
EOF
```

```
Exit code 1
291 9.19793152809143
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
  File "entries/pasquereau-2013/pasq.py", line 178, in load_all
    return list(ex.map(lambda pu: load_file(*pu), paths_urls))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/.local/share/uv/python/cpython-3.12.16-linux-x86_64-gnu/lib/python3.12/concurrent/futures/_base.py", line 619, in result_iterator
    yield _result_or_cancel(fs.pop())
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/.local/share/uv/python/cpython-3.12.16-linux-x86_64-gnu/lib/python3.12/concurrent/futures/_base.py", line 317, in _result_or_cancel
    return fut.result(timeout)
           ^^^^^^^^^^^^^^^^^^^
  File "/home/runner/.local/share/uv/python/cpython-3.12.16-linux-x86_64-gnu/lib/python3.12/concurrent/futures/_base.py", line 456, in result
    return self.__get_result()
           ^^^^^^^^^^^^^^^^^^^
  File "/home/runner/.local/share/uv/python/cpython-3.12.16-linux-x86_64-gnu/lib/python3.12/concurrent/futures/_base.py", line 401, in __get_result
    raise self._exception
  File "/home/runner/.local/share/uv/python/cpython-3.12.16-linux-x86_64-gnu/lib/python3.12/concurrent/futures/thread.py", line 59, in run
    result = self.fn(*self.args, **self.kwargs)
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/pasquereau-2013; sed -i 's|out = {"path": path, "session": h\["session_id"\]\[()\].decode(),|out = {"path": path, "session": h["general/session_id"][()].decode(),|' pasq.py; cd $TMPDIR/work; . ../env/bin/activate; export PYTHONPATH=entries/pasquereau-2013; python - <<'EOF'
import time, pickle, resource, pasq
pu=pasq.asset_urls()
t=time.time(); d=pasq.load_all(pu[:8]); print('8 files', time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,'GB')
x=d[0]; print(x['session'], x['units'], len(x['pert']), x['angle'].shape, {k:v.shape for k,v in x['emg'].items()}, [o.sum() for o in x['observed']])
EOF
```

```
8 files 7.110199928283691 0.292204 GB
Venus++v0502++PreMPTP++Depth22130um++19990406   unit_name                   ptype   post  latency  latency_2
0   v0502.1  pyramidal_tract_neuron  False      1.4        NaN 16 (16, 600) {'EMGTricepsLongus1': (16, 600), 'EMGTricepsLongus2': (16, 600), 'EMGTricepsLateralis': (16, 600), 'EMGDeltoidPosterior': (16, 600), 'EMGTrapezius': (16, 600), 'EMGBrachioradialis': (16, 600)} [np.int64(16)]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/work; . ../env/bin/activate; export PYTHONPATH=entries/pasquereau-2013; python - <<'EOF'
import time, pickle, resource, pasq
pu=pasq.asset_urls()
t=time.time(); d=pasq.load_all(pu); print('all', time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,'GB')
pickle.dump(d,open('venus.pkl','wb'))
EOF
ls -la venus.pkl; date -u
```

```
all 269.6495819091797 0.702956 GB
-rw-r--r-- 1 runner runner 179462446 Nov 26 16:35 venus.pkl
Thu Nov 26 16:35:10 UTC 2026
Shell cwd was reset to
```

**Agent**

Loading all 291 Venus files takes about 4.5 minutes and 0.7 GB. Next: per-unit counts and a check for recordings deposited twice.

**Agent calls Bash**

```bash
cd $TMPDIR/work; . ../env/bin/activate; export PYTHONPATH=entries/pasquereau-2013; python - <<'EOF'
import pickle, numpy as np, pandas as pd, collections, itertools
d=pickle.load(open('venus.pkl','rb'))
rows=[]
for fi,x in enumerate(d):
    p=x['pert']
    for ui,u in x['units'].iterrows():
        o=x['observed'][ui]
        rows.append(dict(fi=fi,session=x['session'],date=x['date'],**u.to_dict(),
          nflex=int(((p.torque=='flexion').values&o).sum()), next=int(((p.torque=='extension').values&o).sum()),
          nflex_file=int((p.torque=='flexion').sum()), nspk=x['n_spikes'][ui]))
U=pd.DataFrame(rows)
print(len(U)); print((U.nflex!=U.nflex_file).sum(), 'units with fewer observed than file')
S=U[(U.nflex>=5)&(U.next>=5)]
print(S.groupby(['post','ptype']).size()); print(S.groupby('post').size())
# file name pre/post vs is_post
U['fname_post']=U.session.str.contains('PostMPTP'); print('mismatch post', (U.fname_post!=U.post).sum())
print(U.date.min(), U[~U.post].date.max(), U[U.post].date.min(), U.date.max())
# duplicates: spike trains
sig={}
for fi,x in enumerate(d):
    for ui,s in enumerate(x['spikes_all']):
        # relative to trial start
        tr=x['trials']; 
        rel=[]
        for a,b in zip(tr.start,tr.stop):
            rel.append(np.round(s[(s>=a)&(s<b)]-a,4))
        sig[(fi,ui)]=rel
# compare trial-level spike patterns across units: hash of each trial's spikes (len>=3)
h=collections.defaultdict(set)
for k,rel in sig.items():
    for r in rel:
        if len(r)>=5: h[tuple(r)].add(k)
pairs=collections.Counter()
for k,v in h.items():
    if len(v)>1:
        for a,b in itertools.combinations(sorted(v),2): pairs[(a,b)]+=1
for (a,b),n in pairs.most_common(40):
    print(d[a[0]]['session'],U[(U.fi==a[0])].unit_name.values[a[1]], '|', d[b[0]]['session'], U[(U.fi==b[0])].unit_name.values[b[1]], n, len(sig[a]),len(sig[b]))
EOF
```

```
356
6 units with fewer observed than file
post   ptype                                     
False  corticostriatal_neuron                        32
       no_response                                   29
       not_tested                                     1
       pyramidal_tract_and_corticostriatal_neuron     2
       pyramidal_tract_neuron                        51
True   corticostriatal_neuron                        48
       no_response                                   50
       not_tested                                     1
       pyramidal_tract_and_corticostriatal_neuron     1
       pyramidal_tract_and_thalamic_neuron            1
       pyramidal_tract_neuron                        54
       thalamic_projection_neuron                     2
dtype: int64
post
False    115
True     157
dtype: int64
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/work; . ../env/bin/activate; python - <<'EOF'
import pickle, numpy as np, collections, itertools
d=pickle.load(open('venus.pkl','rb'))
h=collections.defaultdict(set)
for fi,x in enumerate(d):
    t=x['trials']
    for i,r in t.iterrows():
        key=(round(r.stop-r.start,3), round(r.center-r.start,3) if np.isfinite(r.center) else None, r.torque, round(r.onset-r.start,3) if np.isfinite(r.onset) else None)
        h[key].add(fi)
pairs=collections.Counter()
for k,v in h.items():
    if len(v)>1:
        for a,b in itertools.combinations(sorted(v),2): pairs[(a,b)]+=1
for (a,b),n in pairs.most_common(30):
    print(d[a]['session'], len(d[a]['trials']), '|', d[b]['session'], len(d[b]['trials']), n)
# angle traces identical?
EOF
```

```
Venus++v4513++PostMPTP++Depth19480um++20000121 40 | Venus++v4519++PostMPTP++Depth19110um++20000125 24 2
Venus++v4509++PostMPTP++Depth20000um++20000121 17 | Venus++v4518++PostMPTP++Depth19900um++20000124 40 2
Venus++v4511++PostMPTP++Depth18450um++20000121 40 | Venus++v4512++PostMPTP++Depth19360um++20000121 40 2
Venus++v4513++PostMPTP++Depth19480um++20000121 40 | Venus++v4518++PostMPTP++Depth19900um++20000124 40 2
Venus++v1004++PreMPTP++Depth20470um++19990409 17 | Venus++v3607++PreMPTP++Depth19650um++19990729 40 1
Venus++v1304++PreMPTP++Depth19350um++19990415 18 | Venus++v1902++PreMPTP++Depth18500um++19990520 40 1
Venus++v1402++PreMPTP++Depth23700um++19990511 20 | Venus++v4410++PostMPTP++Depth18800um++20000117 40 1
Venus++v4005++PreMPTP++Depth20580um++19990811 20 | Venus++v5805++PostMPTP++Depth17700um++20000330 40 1
Venus++v4410++PostMPTP++Depth18800um++20000117 40 | Venus++v4514++PostMPTP++Depth19130um++20000124 40 1
Venus++v4502++PostMPTP++Depth18380um++20000119 38 | Venus++v4513++PostMPTP++Depth19480um++20000121 40 1
Venus++v4502++PostMPTP++Depth18380um++20000119 38 | Venus++v4516++PostMPTP++Depth19500um++20000124 23 1
Venus++v4502++PostMPTP++Depth18380um++20000119 38 | Venus++v4519++PostMPTP++Depth19110um++20000125 24 1
Venus++v4513++PostMPTP++Depth19480um++20000121 40 | Venus++v4516++PostMPTP++Depth19500um++20000124 23 1
Venus++v4516++PostMPTP++Depth19500um++20000124 23 | Venus++v4519++PostMPTP++Depth19110um++20000125 24 1
Venus++v4502++PostMPTP++Depth18380um++20000119 38 | Venus++v4509++PostMPTP++Depth20000um++20000121 17 1
Venus++v4502++PostMPTP++Depth18380um++20000119 38 | Venus++v4510++PostMPTP++Depth19950um++20000121 40 1
Venus++v4502++PostMPTP++Depth18380um++20000119 38 | Venus++v4511++PostMPTP++Depth18450um++20000121 40 1
Venus++v4502++PostMPTP++Depth18380um++20000119 38 | Venus++v4523++PostMPTP++Depth22420um++20000125 50 1
Venus++v4511++PostMPTP++Depth18450um++20000121 40 | Venus++v4523++PostMPTP++Depth22420um++20000125 50 1
Venus++v4505++PostMPTP++Depth1
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/work; . ../env/bin/activate; python - <<'EOF'
import pickle, numpy as np, collections, itertools
d=pickle.load(open('venus.pkl','rb'))
h=collections.defaultdict(set)
for fi,x in enumerate(d):
    if x['angle'] is None: continue
    for i,a in enumerate(x['angle']):
        if np.isnan(a).any(): continue
        h[tuple(np.round(a[::7],3))].add(fi)
    for ch,w in x['emg'].items():
        for a in w:
            if np.isnan(a).any(): continue
            h[(ch,)+tuple(np.round(a[::7],2))].add(fi)
pairs=collections.Counter()
for k,v in h.items():
    if len(v)>1:
        for a,b in itertools.combinations(sorted(v),2): pairs[(a,b)]+=1
print(len(pairs))
for (a,b),n in pairs.most_common(30):
    print(d[a]['session'], len(d[a]['pert']), '|', d[b]['session'], len(d[b]['pert']), n)
print(sum(x['angle'] is None for x in d), [x['session'] for x in d if x['angle'] is None])
print(collections.Counter(tuple(sorted(x['emg'])) for x in d))
EOF
```

```
0
0 []
Counter({('EMGBrachioradialis', 'EMGDeltoidPosterior', 'EMGTrapezius', 'EMGTricepsLongus1', 'EMGTricepsLongus2'): 205, ('EMGBrachioradialis', 'EMGDeltoidPosterior', 'EMGTrapezius', 'EMGTricepsLateralis', 'EMGTricepsLongus1', 'EMGTricepsLongus2'): 53, ('EMGDeltoidPosterior', 'EMGTrapezius', 'EMGTricepsLateralis', 'EMGTricepsLongus1', 'EMGTricepsLongus2'): 29, (): 4})
Shell cwd was reset to
```

**Agent**

No duplicated spike trains, trial blocks or analog traces between files. Now the neuronal analysis on the cached data.

**Agent calls Bash**

```bash
cd $TMPDIR/work; . ../env/bin/activate; export PYTHONPATH=entries/pasquereau-2013; cat > cells.py <<'EOF'
import pickle, numpy as np, pandas as pd, pasq, time
def cell_table(d):
    rows=[]
    for fi,x in enumerate(d):
        p=x['pert']
        for ui,u in x['units'].iterrows():
            o=x['observed'][ui]
            r=dict(fi=fi,session=x['session'],date=x['date'],**u.to_dict())
            sd_all=[]
            for dname in ['flexion','extension']:
                sel=np.where((p.torque==dname).values & o)[0]
                r['n_'+dname[:3]]=len(sel)
                if len(sel)==0: continue
                S=pasq.sdf_trials([x['rel_spikes'][ui][i] for i in sel]); sd_all.append(S)
                m=S.mean(0)
                res=pasq.detect(m,0); pse=pasq.detect(m,-pasq.PSEUDO_SHIFT_MS)
                for k,v in res.items(): r[f'{dname[:3]}_{k}']=v
                r[f'{dname[:3]}_pseudo_any']=pse['any_crossing']; r[f'{dname[:3]}_pseudo_resp']=pse['responds']
                # variant: one-sample t-test of single-trial SDFs vs baseline mean each ms
                z=pasq.ms_index(0); mu=res['baseline']
                from scipy import stats
                post=S[:,z:z+200]
                tt=stats.ttest_1samp(post,mu,axis=0)
                sig=(tt.pvalue<pasq.P_THRESHOLD)&np.isfinite(tt.pvalue)
                on=[t for t in range(20,61) if sig[t] and not sig[t-1]]
                r[f'{dname[:3]}_ttest_resp']=len(on)>0
                r[f'{dname[:3]}_ttest_onset']=on[0] if on else np.nan
            if sd_all:
                A=np.vstack(sd_all); z=pasq.ms_index(0)
                r['baseline_rate']=A[:,z-500:z].mean()
            rows.append(r)
    return pd.DataFrame(rows)
if __name__=='__main__':
    d=pickle.load(open('venus.pkl','rb'))
    t=time.time(); C=cell_table(d); print(time.time()-t)
    C.to_pickle('cells.pkl')
EOF
python cells.py
```

```
/tmp/claude-1001/env/lib/python3.12/site-packages/scipy/stats/_stats_py.py:1227: RuntimeWarning: divide by zero encountered in divide
  var *= (n / (n-ddof))  # to avoid error on division by zero
/tmp/claude-1001/env/lib/python3.12/site-packages/scipy/stats/_stats_py.py:1227: RuntimeWarning: invalid value encountered in multiply
  var *= (n / (n-ddof))  # to avoid error on division by zero
/tmp/claude-1001/env/lib/python3.12/site-packages/scipy/stats/_stats_py.py:1227: RuntimeWarning: divide by zero encountered in divide
  var *= (n / (n-ddof))  # to avoid error on division by zero
/tmp/claude-1001/env/lib/python3.12/site-packages/scipy/stats/_stats_py.py:1227: RuntimeWarning: invalid value encountered in multiply
  var *= (n / (n-ddof))  # to avoid error on division by zero
/tmp/claude-1001/env/lib/python3.12/site-packages/scipy/stats/_stats_py.py:1227: RuntimeWarning: divide by zero encountered in divide
  var *= (n / (n-ddof))  # to avoid error on division by zero
/tmp/claude-1001/env/lib/python3.12/site-packages/scipy/stats/_stats_py.py:1227: RuntimeWarning: invalid value encountered in multiply
  var *= (n / (n-ddof))  # to avoid error on division by zero
1.1021454334259033
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/work; . ../env/bin/activate; python - <<'EOF' 2>&1 | grep -v Warn
import pandas as pd, numpy as np
from scipy import stats
C=pd.read_pickle('cells.pkl')
S=C[(C.n_fle>=5)&(C.n_ext>=5)].copy()
grp={'M1':S.ptype.notna(),'PTN':S.ptype=='pyramidal_tract_neuron','CSN':S.ptype=='corticostriatal_neuron'}
for g,m in grp.items():
    for post in [False,True]:
        s=S[m&(S.post==post)]
        tr=(s.fle_responds|s.ext_responds)
        print(g,post,len(s),'base %.2f'%s.baseline_rate.mean(),'TR %d %.1f%%'%(tr.sum(),100*tr.mean()))
# FPR
fp=np.r_[S.fle_pseudo_any.values,S.ext_pseudo_any.values]; fr=np.r_[S.fle_pseudo_resp.values,S.ext_pseudo_resp.values]
print('FPR any', fp.mean(), 'resp20-60', fr.mean(), len(fp))
# real any crossing
print('real any', np.r_[S.fle_any_crossing,S.ext_any_crossing].mean())
print('ttest variant TR', (S.fle_ttest_resp|S.ext_ttest_resp).groupby(S.post).mean())
EOF
```

```
M1 False 115 base 12.66 TR 64 55.7%
M1 True 157 base 8.85 TR 78 49.7%
PTN False 51 base 18.49 TR 37 72.5%
PTN True 54 base 14.37 TR 37 68.5%
CSN False 32 base 3.48 TR 5 15.6%
CSN True 48 base 3.36 TR 9 18.8%
FPR any 0.22977941176470587 resp20-60 0.051470588235294115 544
real any 0.6727941176470589
ttest variant TR post
False    0.443478
True     0.598726
dtype: float64
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/work; . ../env/bin/activate; export PYTHONPATH=entries/pasquereau-2013; python - <<'EOF' 2>&1 | grep -v Warn
import pickle, numpy as np, pandas as pd, pasq
from scipy import stats
d=pickle.load(open('venus.pkl','rb'))
res={'main':[],'ttest':[],'se':[],'trialsd':[]}
real={'main':[],'ttest':[],'se':[],'trialsd':[]}
for fi,x in enumerate(d):
    p=x['pert']
    for ui,u in x['units'].iterrows():
        o=x['observed'][ui]
        sels={k:np.where((p.torque==k).values&o)[0] for k in ['flexion','extension']}
        if min(len(v) for v in sels.values())<5: continue
        for k,sel in sels.items():
            S=pasq.sdf_trials([x['rel_spikes'][ui][i] for i in sel])
            for zero,store in [(-600,res),(0,real)]:
                z=pasq.ms_index(zero); B=S[:,z-500:z]; mu=B.mean(); post=S[:,z:z+200]; m=post.mean(0)
                sd=S.mean(0)[z-500:z].std(ddof=1)
                store['main'].append(np.any(np.abs(m-mu)>pasq.T_CRIT*sd))
                tt=stats.ttest_1samp(post,mu,axis=0); store['ttest'].append(np.any(tt.pvalue<0.002))
                # SE reading: SD of single-trial baseline means / sqrt(n)
                bm=B.mean(1); se=bm.std(ddof=1)/np.sqrt(len(bm)); tc=stats.t.ppf(1-0.001,len(bm)-1)
                store['se'].append(np.any(np.abs(m-mu)>tc*se))
                # trial SD: SD over all single-trial baseline samples
                sdt=B.std(ddof=1); store['trialsd'].append(np.any(np.abs(m-mu)>pasq.T_CRIT*sdt))
for k in res: print(k,'pseudo %.3f'%np.mean(res[k]),'real %.3f'%np.mean(real[k]), len(res[k]))
EOF
```

```
main pseudo 0.230 real 0.673 544
ttest pseudo 0.465 real 0.868 544
se pseudo 0.347 real 0.717 544
trialsd pseudo 0.013 real 0.200 544
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/work; . ../env/bin/activate; export PYTHONPATH=entries/pasquereau-2013; python - <<'EOF' 2>&1 | grep -v Warn
import pickle, numpy as np, pandas as pd, pasq
import statsmodels.formula.api as smf, statsmodels.api as sm
d=pickle.load(open('venus.pkl','rb'))
rows=[]
for x in d:
    if x['angle'] is None or len(x['pert'])==0: continue
    K=pasq.kinematics(x['angle'],x['pert'].torque.values); K['dir']=x['pert'].torque.values
    post=bool(x['units'].post.iloc[0])
    for dname,g in K.groupby('dir'):
        rows.append(dict(session=x['session'],post=post,dir=dname,n=len(g),nan_lat=g.latency.isna().sum(),**g[['latency','peak_velocity','amplitude']].mean().to_dict()))
K=pd.DataFrame(rows); print(len(K), K.groupby(['post','dir']).size())
print(K.groupby(['post','dir'])[['latency','peak_velocity','amplitude']].mean())
for meas in ['peak_velocity','amplitude','latency']:
    m=smf.ols(f'{meas} ~ C(post)*C(dir)',data=K).fit(); a=sm.stats.anova_lm(m,typ=2); print(meas); print(a)
    pre=K[~K.post][meas].mean(); po=K[K.post][meas].mean(); print('pooled change %.1f%%'%(100*(po/pre-1)))
    f=K[K.dir=='flexion']; print('flex change %.1f%%'%(100*(f[f.post][meas].mean()/f[~f.post][meas].mean()-1)))
print(K.nan_lat.sum())
EOF
```

```
581 post   dir      
False  extension    154
       flexion      153
True   extension    137
       flexion      137
dtype: int64
                   latency  peak_velocity  amplitude
post  dir                                           
False extension  10.862610      46.100324   2.421914
      flexion     9.650215      58.108764   3.404863
True  extension   5.989076      58.077720   2.901810
      flexion     3.048408      75.367191   3.783067
peak_velocity
                       sum_sq     df          F        PR(>F)
C(post)          30920.126357    1.0  98.504227  1.536336e-21
C(dir)           30534.394075    1.0  97.275375  2.611569e-21
C(post):C(dir)    1009.457757    1.0   3.215894  7.344991e-02
Residual        181118.247505  577.0        NaN           NaN
pooled change 28.1%
flex change 29.7%
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/work; . ../env/bin/activate; export PYTHONPATH=entries/pasquereau-2013; python - <<'EOF' 2>&1 | grep -v Warn
import pickle, numpy as np, pandas as pd, pasq
d=pickle.load(open('venus.pkl','rb'))
rows=[]
for x in d:
    if x['angle'] is None or len(x['pert'])==0: continue
    K=pasq.kinematics(x['angle'],x['pert'].torque.values)
    tq=x['torque_cmd']; s=np.where(x['pert'].torque.values=='flexion',1,-1)
    base=tq[:,:50].mean(1); amp=s*(tq[:,50+10:50+50].mean(1)-base)
    for i in range(len(K)):
        rows.append(dict(session=x['session'],date=x['date'],post=bool(x['units'].post.iloc[0]),dir=x['pert'].torque.values[i],amp=amp[i],**K.iloc[i].to_dict()))
T=pd.DataFrame(rows)
T['amp_r']=(T.amp/5).round()*5
print(T.groupby(['post',pd.cut(T.amp,[-1e9,10,30,60,120,250,1e9])]).agg(n=('peak_velocity','size'),vel=('peak_velocity','mean'),ampl=('amplitude','mean')))
print(T.groupby('post').amp.describe())
# within torque level ~91
for lo,hi in [(30,60),(60,120),(120,250)]:
    s=T[(T.amp>lo)&(T.amp<hi)]; print(lo,hi, s.groupby(['post','dir'])[['peak_velocity','amplitude','latency']].mean().round(1).to_dict())
T.to_pickle('pert_kin.pkl')
EOF
```

```
n         vel      ampl
post  amp                                              
False (-1000000000.0, 10.0]    51   89.968447  4.880719
      (30.0, 60.0]           1372   55.159929  3.139150
      (60.0, 120.0]           483   42.664689  2.215141
      (120.0, 250.0]           41   64.054471  3.593755
True  (10.0, 30.0]              2   20.885266  0.235146
      (30.0, 60.0]             29   18.420675  0.754703
      (60.0, 120.0]           494   58.730001  3.077526
      (120.0, 250.0]         2846   65.413914  3.263351
      (250.0, 1000000000.0]   232  102.474561  5.082957
        count        mean        std  ...         50%         75%         max
post                                  ...                                    
False  1947.0   58.389086  28.096480  ...   45.719352   90.337074  182.703287
True   3603.0  174.676521  47.563024  ...  181.610012  184.467244  343.522349

[2 rows x 8 columns]
30 60 {'peak_velocity': {(False, 'extension'): 47.9, (False, 'flexion'): 62.6, (True, 'extension'): 18.7, (True, 'flexion'): 17.8}, 'amplitude': {(False, 'extension'): 2.5, (False, 'flexion'): 3.8, (True, 'extension'): 0.7, (True, 'flexion'): 0.8}, 'latency': {(False, 'extension'): 12.1, (False, 'flexion'): 10.8, (True, 'extension'): 27.6, (True, 'flexion'): 10.5}}
60 120 {'peak_velocity': {(False, 'extension'): 41.3, (False, 'flexion'): 44.1, (True, 'extension'): 49.3, (True, 'flexion'): 75.7}, 'amplitude': {(False, 'extension'): 2.1, (False, 'flexion'): 2.3, (True, 'extension'): 2.6, (True, 'flexion'): 4.0}, 'latency': {(False, 'extension'): 8.0, (False, 'flexion'): 7.2, (True, 'extension'): 9.0, (True, 'flexion'): 7.0}}
120 250 {'peak_velocity': {(False, 'extension'): 61.6, (False, 'flexion'): 67.5, (True, 'extension'): 58.9, (True, 'flexion'): 71.8}, 'amplitude': {(False, 'extension'): 3.4, (False, 'flexion'): 3.9, (True, 'extension'): 2.9, (True, 'flexion'): 3.6}, 'latency': {(False, 'extension'): 3.8, (False, 'flexion'): 3.3, (True, 'extension'): 4.8, (True, '
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/work; . ../env/bin/activate; export PYTHONPATH=entries/pasquereau-2013; python - <<'EOF' 2>&1 | grep -v Warn
import pickle, numpy as np, pandas as pd, pasq
from scipy import stats
d=pickle.load(open('venus.pkl','rb'))
rows=[]
for x in d:
    fl=x['pert'].torque.values=='flexion'
    if fl.sum()==0: continue
    for ch in pasq.TRICEPS:
        if ch not in x['emg']: continue
        w=x['emg'][ch][fl]
        m=pasq.emg_measures(w)
        rows.append(dict(session=x['session'],post=bool(x['units'].post.iloc[0]),ch=ch,n=fl.sum(),**m))
E=pd.DataFrame(rows)
print(E.groupby(['ch','post']).size())
print(E.baseline_sd.describe()); print((E.baseline_sd<1).groupby([E.ch,E.post]).sum(), E.has_nan.sum())
U=E[(E.baseline_sd>=1)&~E.has_nan]
print(U.groupby(['ch','post'])[['m1','m2','onset','duration']].median())
for ch,g in U.groupby('ch'):
    a,b=g[~g.post].m2,g[g.post].m2; print(ch,'m2 KS p=%.3g'%stats.ks_2samp(a,b).pvalue, a.median(),b.median(),len(a),len(b))
dd=U.dropna(subset=['duration']); print('dur', dd.groupby('post').duration.agg(['mean','count']), stats.ks_2samp(dd[~dd.post].duration,dd[dd.post].duration).pvalue)
print('onset', dd.groupby('post').onset.agg(['mean','median']), stats.ks_2samp(dd[~dd.post].onset,dd[dd.post].onset).pvalue)
for post,g in U.groupby('post'): print(post,'m2>m1 %.2f'%(g.m2>g.m1).mean(),'median m1/m2 %.2f'%(g.m1/g.m2).median())
print('no response', U.duration.isna().groupby(U.post).sum())
E.to_pickle('emg.pkl')
EOF
```

```
trace = np.nanmean(windows, axis=0)
  trace = np.nanmean(windows, axis=0)
  trace = np.nanmean(windows, axis=0)
  trace = np.nanmean(windows, axis=0)
  trace = np.nanmean(windows, axis=0)
  trace = np.nanmean(windows, axis=0)
  trace = np.nanmean(windows, axis=0)
  trace = np.nanmean(windows, axis=0)
  trace = np.nanmean(windows, axis=0)
  trace = np.nanmean(windows, axis=0)
  trace = np.nanmean(windows, axis=0)
  trace = np.nanmean(windows, axis=0)
  trace = np.nanmean(windows, axis=0)
  trace = np.nanmean(windows, axis=0)
  trace = np.nanmean(windows, axis=0)
  trace = np.nanmean(windows, axis=0)
  trace = np.nanmean(windows, axis=0)
  trace = np.nanmean(windows, axis=0)
  trace = np.nanmean(windows, axis=0)
ch                   post 
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/work; . ../env/bin/activate; export PYTHONPATH=entries/pasquereau-2013; python - <<'EOF' 2>&1 | grep -v Warn
import pickle, numpy as np, pandas as pd, pasq
d=pickle.load(open('venus.pkl','rb'))
rows=[]
for x in d:
    fl=x['pert'].torque.values=='flexion'
    if fl.sum()==0: continue
    for ch,w in x['emg'].items():
        w=w[fl]; z=300
        base=np.nanmean(w[:,z-200:z]); rawsd=np.nanstd(w[:,z-200:z])
        rows.append(dict(date=x['date'],post=bool(x['units'].post.iloc[0]),ch=ch,base=base,rawsd=rawsd,peak=np.nanmax(np.nanmean(w,0)[z:z+150])-np.nanmean(np.nanmean(w,0)[z-200:z]), mn=np.nanmin(w)))
B=pd.DataFrame(rows)
print(B.groupby(['ch','post'])[['base','rawsd','peak','mn']].median().round(1))
EOF
```

```
var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR/work; . ../env/bin/activate; python - <<'EOF'
import json, remfile, h5py, numpy as np
assets=json.load(open('../assets.json'))
for key in ['l10003','PostMPTP']:
    a=[a for a in assets if 'Leu' in a['path'] and key in a['path']][0]
    h=h5py.File(remfile.File(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/"),'r')
    tq=h['acquisition/WristTorque/data'][:]; ts=h['acquisition/WristTorque/timestamps'][:]
    print(a['path'][-50:], tq.shape, np.percentile(tq,[0,1,50,99,100]).round(1), h['acquisition/WristTorque'].attrs.get('description'))
    d=np.abs(np.diff(tq)); print('big steps', (d>20).sum(), np.unique(np.round(np.diff(ts),3)))
EOF
```

```
Thu Nov 26 16:37:42 UTC 2026
eMPTP++Depth23680um++19930123_behavior+ecephys.nwb (16576,) [nan nan nan nan nan] Command sent to the torque motor controller, in arbitrary units. The monkey L source files contain no torque perturbation times. The command is NaN in every file before MPTP; after MPTP it is a continuous trace without distinct pulses. No conversion to newton-metres is available: the amplifier and controller gains are not in these MATLAB files, and the original recordings they were exported from were not provided.
big steps 0 [0.01  3.015 3.016 3.017 3.019 3.02  3.021 3.022 3.023 3.024]
tMPTP++Depth23150um++19930612_behavior+ecephys.nwb (28039,) [nan nan nan nan nan] Command sent to the torque motor controller, in arbitrary units. The monkey L source files contain no torque perturbation times. The command is NaN in every file before MPTP; after MPTP it is a continuous trace without distinct pulses. No conversion to newton-metres is available: the amplifier and controller gains are not in these MATLAB files, and the original recordings they were exported from were not provided.
big steps 0 [0.01  3.015 3.016 3.017 3.018 3.019 3.02  3.021 3.022 3.023 3.024]
Shell cwd was reset to
```

**Agent**

Monkey L torque traces are NaN before MPTP and show no pulses after, so the monkey L claim is blocked as data missing. Now I'm moving the analyses into the helper and writing the notebook.

**Agent calls Bash**

```bash
cd entries/pasquereau-2013; cat >> pasq.py <<'EOF'


def load_meta(path: str, url: str) -> dict:
    """Trials' perturbation columns and the units table of one file, without the signals."""
    with h5py.File(remfile.File(url), "r") as h:
        tr = h["intervals/trials"]
        u = h["units"]
        acq = h["acquisition"]
        torque = [k for k in acq if k.endswith("Torque")]
        tq = acq[torque[0] + "/data"][:] if torque else np.array([np.nan])
        return {"path": path,
                "torque_type": _str(tr["torque_perturbation_type"][:]),
                "onset": tr["torque_perturbation_onset_time"][:],
                "torque_cmd_finite": int(np.isfinite(tq).sum()),
                "torque_cmd_steps": int((np.abs(np.diff(tq[np.isfinite(tq)])) > 20).sum()),
                "units": pd.DataFrame({"unit_name": _str(u["unit_name"][:]),
                                       "ptype": _str(u["neuron_projection_type"][:]),
                                       "post": u["is_post_mptp"][:].astype(bool),
                                       "latency": u["antidromic_latency_ms"][:]})}


def load_meta_all(paths_urls, workers: int = 8) -> list[dict]:
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(lambda pu: load_meta(*pu), paths_urls))


# ---------------------------------------------------------------- per-cell responses

DIRECTIONS = ["flexion", "extension"]


def cell_responses(files: list[dict]) -> pd.DataFrame:
    """One row per unit: perturbation counts, baseline rate, and the response to each direction
    at the torque onset and at the pseudo onset (prefix `pse_`)."""
    rows = []
    for fi, x in enumerate(files):
        p = x["pert"]
        for ui, u in x["units"].iterrows():
            obs = x["observed"][ui]
            r = {"file": fi, "session": x["session"], "date": x["date"], **u.to_dict()}
            sdfs = []
            for dname in DIRECTIONS:
                d = dname[:3]
                sel = np.where((p.torque == dname).values & obs)[0]
                r[f"n_{d}"] = len(sel)
                if len(sel) == 0:
                    continue
                S = sdf_trials([x["rel_spikes"][ui][i] for i in sel])
                sdfs.append(S)
                m = S.mean(0)
                for k, v in detect(m, 0).items():
                    r[f"{d}_{k}"] = v
                for k, v in detect(m, -PSEUDO_SHIFT_MS).items():
                    r[f"pse_{d}_{k}"] = v
                # Variant of the claims file: one-sample t-test of the single-trial SDFs against
                # the baseline mean at each ms (not deciding).
                z = ms_index(0)
                sig = stats.ttest_1samp(S[:, z:z + EPOCH_MS], r[f"{d}_baseline"], axis=0).pvalue < P_THRESHOLD
                on = [t for t in range(ONSET_WINDOW_MS[0], ONSET_WINDOW_MS[1] + 1) if sig[t] and not sig[t - 1]]
                r[f"{d}_ttest_responds"] = bool(on)
            if sdfs:
                z = ms_index(0)
                r["baseline_rate"] = float(np.vstack(sdfs)[:, z - BASELINE_MS:z].mean())
            rows.append(r)
    return pd.DataFrame(rows)


def pseudo_readings(files: list[dict], studied: set) -> pd.DataFrame:
    """Any threshold crossing over 0 to 200 ms after the pseudo onset (600 ms before torque) and
    after the torque onset, per cell and direction, under four readings of the threshold:
    `mean_sd` the claims file's (SD of the trial-averaged SDF over the baseline), `ttest` the
    claims file's variant, `trial_se` the standard error of the single-trial baseline means,
    `trial_sd` the SD of all single-trial baseline values."""
    rows = []
    for fi, x in enumerate(files):
        p = x["pert"]
        for ui, u in x["units"].iterrows():
            if (fi, ui) not in studied:
                continue
            for dname in DIRECTIONS:
                sel = np.where((p.torque == dname).values & x["observed"][ui])[0]
                S = sdf_trials([x["rel_spikes"][ui][i] for i in sel])
                for label, zero in [("pseudo", -PSEUDO_SHIFT_MS), ("torque", 0)]:
                    z = ms_index(zero)
                    B, post = S[:, z - BASELINE_MS:z], S[:, z:z + EPOCH_MS]
                    mu, m = B.mean(), post.mean(0)
                    bm = B.mean(1)
                    t_n = stats.t.ppf(1 - P_THRESHOLD / 2, len(bm) - 1)
                    rows.append({"file": fi, "unit": ui, "direction": dname, "onset": label,
                                 "mean_sd": bool(np.any(np.abs(m - mu) > T_CRIT * S.mean(0)[z - BASELINE_MS:z].std(ddof=1))),
                                 "ttest": bool(np.any(stats.ttest_1samp(post, mu, axis=0).pvalue < P_THRESHOLD)),
                                 "trial_se": bool(np.any(np.abs(m - mu) > t_n * bm.std(ddof=1) / np.sqrt(len(bm)))),
                                 "trial_sd": bool(np.any(np.abs(m - mu) > T_CRIT * B.std(ddof=1)))})
    return pd.DataFrame(rows)


def no_torque_crossings(files: list[dict], studied: set) -> pd.DataFrame:
    """The claims file's detection on trials without a perturbation, aligned where the file's
    perturbations fall after the centre target (its median delay): a null with no torque at all."""
    rows = []
    for fi, x in enumerate(files):
        t, p = x["trials"], x["pert"]
        if len(p) == 0:
            continue
        delay = np.nanmedian(p.onset - p.center)
        none = t[(t.torque == "none") & np.isfinite(t.center)]
        onsets = (none.center + delay).values
        for ui, u in x["units"].iterrows():
            if (fi, ui) not in studied:
                continue
            ob = x["obs"][ui]
            st = x["spikes_all"][ui]
            w0, w1 = SPIKE_WINDOW_MS[0] / 1000, SPIKE_WINDOW_MS[1] / 1000
            ok = [o for o in onsets if np.any((ob[:, 0] <= o + w0) & (ob[:, 1] >= o + w1))]
            if len(ok) < MIN_PERTURBATIONS:
                continue
            S = sdf_trials([st[(st >= o + w0) & (st < o + w1)] - o for o in ok])
            res = detect(S.mean(0), 0)
            rows.append({"file": fi, "unit": ui, "n_trials": len(ok),
                         "any_crossing": res["any_crossing"], "responds": res["responds"]})
    return pd.DataFrame(rows)


def session_kinematics(files: list[dict]) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Per-perturbation kinematics with the torque command's pulse size, and session means per
    direction. The pulse size is the command over 10 to 50 ms after onset less its mean over the
    50 ms before, signed so that the torque's direction is positive (arbitrary units)."""
    rows = []
    for fi, x in enumerate(files):
        if x["angle"] is None or len(x["pert"]) == 0:
            continue
        dirs = x["pert"].torque.values
        k = kinematics(x["angle"], dirs)
        sign = np.where(dirs == "flexion", 1.0, -1.0)
        z = -TORQUE_WINDOW_MS[0]
        cmd = x["torque_cmd"]
        k["command"] = sign * (cmd[:, z + 10:z + 50].mean(1) - cmd[:, :z].mean(1))
        k["direction"], k["file"], k["session"] = dirs, fi, x["session"]
        k["post"] = bool(x["units"].post.iloc[0])
        rows.append(k)
    trials = pd.concat(rows, ignore_index=True)
    sessions = (trials.groupby(["file", "session", "post", "direction"])
                [["latency", "peak_velocity", "amplitude", "command"]].mean().reset_index())
    return trials, sessions


def session_emg(files: list[dict], channels=TRICEPS, direction: str = "flexion") -> pd.DataFrame:
    """EMG measures of each session and channel for one torque direction. A channel is used when
    no window holds a NaN; `baseline_sd` (of the session-average trace) and `raw_sd` (of the
    single-trial baseline samples) are given for the inclusion rule."""
    rows = []
    z = -EMG_WINDOW_MS[0]
    for fi, x in enumerate(files):
        sel = x["pert"].torque.values == direction
        if sel.sum() == 0:
            continue
        for ch in channels:
            if ch not in x["emg"]:
                continue
            w = x["emg"][ch][sel]
            has_nan = bool(np.isnan(w[:, z - EMG_BASELINE_MS:z + EMG_SEARCH_MS[1] + 1]).any())
            m = emg_measures(w) if not has_nan else {}
            rows.append({"file": fi, "session": x["session"], "post": bool(x["units"].post.iloc[0]),
                         "channel": ch, "n": int(sel.sum()), "has_nan": has_nan,
                         "raw_sd": float(np.nanstd(w[:, z - EMG_BASELINE_MS:z], ddof=1)), **m})
    return pd.DataFrame(rows)
EOF
python - <<'EOF'
import re
p='entries/pasquereau-2013/pasq.py'
s=open(p).read()
s=s.replace('''    trace = np.nanmean(windows, axis=0)''','''    trace = windows.mean(axis=0)''')
s=s.replace('''           "baseline_sd": float(sd), "has_nan": bool(np.isnan(windows).all(axis=0)[z - EMG_BASELINE_MS:z + 151].any()),
''','''           "baseline_sd": float(sd),
''')
open(p,'w').write(s)
EOF
grep -n "has_nan\|windows.mean" pasq.py
```

```
270:    trace = windows.mean(axis=0)
447:            has_nan = bool(np.isnan(w[:, z - EMG_BASELINE_MS:z + EMG_SEARCH_MS[1] + 1]).any())
448:            m = emg_measures(w) if not has_nan else {}
450:                         "channel": ch, "n": int(sel.sum()), "has_nan": has_nan,
```

**Agent calls Bash**

```bash
cd $TMPDIR/work; . ../env/bin/activate; export PYTHONPATH=entries/pasquereau-2013; python - <<'EOF' 2>&1 | grep -v Warn
import pickle, numpy as np, pandas as pd, pasq, time
from scipy import stats
d=pickle.load(open('venus.pkl','rb'))
t=time.time(); C=pasq.cell_responses(d); print(time.time()-t)
S=C[(C.n_fle>=5)&(C.n_ext>=5)]; studied=set(zip(S.file,S.index.map(lambda i: 0)))
# unit index within file
C['unit']=C.groupby('file').cumcount(); S=C[(C.n_fle>=5)&(C.n_ext>=5)]
studied=set(zip(S.file,S.unit))
t=time.time(); N=pasq.no_torque_crossings(d,studied); print(time.time()-t, len(N), N.any_crossing.mean(), N.responds.mean(), N.n_trials.median())
E=pasq.session_emg(d); print(E.has_nan.sum(), len(E))
for rule in ['baseline_sd','raw_sd']:
    U=E[~E.has_nan & (E[rule]>=1)]
    for post,g in U.groupby('post'): print(rule, post, len(g), 'm2>m1 %.3f'%(g.m2>g.m1).mean(),'median m1/m2 %.2f'%(g.m1/g.m2).median())
    dd=U.dropna(subset=['duration']); print(' dur', dd.groupby('post').duration.mean().round(1).to_dict(), stats.ks_2samp(dd[~dd.post].duration,dd[dd.post].duration).pvalue, 'onset', dd.groupby('post').onset.mean().round(1).to_dict(), stats.ks_2samp(dd[~dd.post].onset,dd[dd.post].onset).pvalue)
    for ch,g in U.groupby('channel'): print(' ',ch, stats.ks_2samp(g[~g.post].m2,g[g.post].m2).pvalue, g.groupby('post').m2.median().round(1).to_dict())
EOF
```

```
var *= (n / (n-ddof))  # to avoid error on division by zero
  var *= (n / (n-ddof))  # to avoid error on division by zero
  var *= (n / (n-ddof))  # to avoid error on division by zero
  var *= (n / (n-ddof))  # to avoid error on division by zero
  var *= (n / (n-ddof))  # to avoid error on division by zero
  var *= (n / (n-ddof))  # to avoid error on division by zero
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
[... 21 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/work/make_nb.py",
 "content": "import nbformat as nbf\n\nnb = nbf.v4.new_notebook()\ncells = []\n\n\ndef md(s, tags=None):\n    c = nbf.v4.new_markdown_cell(s.strip())\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\ndef code(s, tags=None):\n    c = nbf.v4.new_code_cell(s.strip())\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\nmd(\"\"\"\n# Pasquereau & Turner (2013) on DANDI:001636\n\nPaper: Pasquereau B, Turner RS (2013). Primary motor cortex of the parkinsonian monkey: altered\nneuronal responses to muscle stretch. *Front. Syst. Neurosci.* 7:98,\n[doi:10.3389/fnsys.2013.00098](https://doi.org/10.3389/fnsys.2013.00098).\n\nDataset: [DANDI:001636](https://dandiarchive.org/dandiset/001636/0.261124.1906), version\n`0.261124.1906` (doi:10.48324/dandi.001636/0.261124.1906). This version was asked for in the\nprompt of this attempt; it is also the newest published version (published 2026-11-24). The\npaper cites no version.\n\nClaims: `claims/pasquereau-2013.yaml`, written from the full text in PubMed Central\n(PMC3840326), its Methods, Results, Table 1, figure legends and supplementary data sheet\n(DataSheet1.PDF), whose table gives the results for each monkey.\n\nThe files of monkey L mark no torque perturbation, so every claim is tested on monkey V\n(Venus, elbow), as the claims file says.\n\n| Claim | Tested or blocked |\n|---|---|\n| cell-counts | tested |\n| monkey-l-perturbations | blocked, data missing |\n| baseline-rate | tested |\n| ptn-faster-than-csn | tested |\n| antidromic-latency | tested |\n| false-positive-rate | computed; blocked, methods underspecified (the false-positive rate is far from the paper's) |\n| torque-related-fractions, prevalence-unchanged, ptn-more-responsive, one-direction-half, excitatory-majority, magnitude-unchanged, venus-response-magnitudes, latency-shorter, latency-not-training, fwhm-shorter-ptn, dsi-reduced, venus-dsi, dsi-not-baseline, velocity-matched-magnitude, session-correlations | blocked through false-positive-rate; their results are computed and shown, not deciding |\n| kinematics-slower | tested |\n| kinematic-latency-unchanged | tested |\n| emg-m2-larger | tested |\n| emg-duration-longer | tested |\n| emg-onset-unchanged | tested |\n| emg-m1-weak | tested |\n| trial-correlations | blocked, methods underspecified |\n\nMethod details come from the claims file, which cites the Methods; details it lacks are taken\nfrom the paper and cited in `pasq.py`'s docstring and below.\n\"\"\")\n\ncode(\"\"\"\nimport time\nimport warnings\n\nimport numpy as np\nimport pandas as pd\nimport pynwb\nimport remfile\nimport h5py\nimport statsmodels.api as sm\nimport statsmodels.formula.api as smf\nfrom scipy import stats\n\nimport pasq\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\npd.set_option(\"display.width\", 160)\npd.set_option(\"display.max_columns\", 30)\nt0 = time.time()\nvenus_urls = pasq.asset_urls(\"sub-Venus\")\nleu_urls = pasq.asset_urls(\"sub-Leu\")\nprint(f\"{len(venus_urls)} Venus files, {len(leu_urls)} Leu files at version {pasq.DANDISET_VERSION}\")\n\"\"\")\n\nmd(\"\"\"\n## What one file holds\n\nOne Venus file opened with pynwb: its acquisition and processing series, its interval tables\nwith every column, and the units table's columns.\n\"\"\")\n\ncode(\"\"\"\npath, url = venus_urls[0]\nwith pynwb.NWBHDF5IO(file=h5py.File(remfile.File(url), \"r\"), load_namespaces=True) as io:\n    nwb = io.read()\n    print(path)\n    for name, ts in nwb.acquisition.items():\n        print(f\"acquisition {name}: {ts.data.shape}, unit {ts.unit}\")\n    for mod_name, mod in nwb.processing.items():\n        for name, obj in mod.data_interfaces.items():\n            print(f\"processing/{mod_name}/{name}: {type(obj).__name__}\")\n    for name, table in nwb.intervals.items():\n        print(f\"intervals {name}: {len(table)} rows, columns {list(table.colnames)}\")\n    print(\"units columns\", list(nwb.units.colnames))\n    print(nwb.units.to_dataframe().drop(columns=[\"spike_times\", \"obs_intervals\", \"electrodes\"]).T)\n\"\"\")\n\nmd(\"\"\"\n## Loading\n\nEvery Venus file is streamed once; only windows around each perturbation are kept (spikes from\n-1500 to +500 ms, angle -200 to +400 ms, EMG -300 to +300 ms, torque command -50 to +100 ms).\nThe Leu files are read for their trials' perturbation columns, torque command and units table.\n\"\"\")\n\ncode(\"\"\"\nvenus = pasq.load_all(venus_urls)\nleu = pasq.load_meta_all(leu_urls)\nprint(f\"loaded in {time.time() - t0:.0f} s\")\n\"\"\")\n\ncode(\"\"\"\ncells = pasq.cell_responses(venus)\ncells[\"unit\"] = cells.groupby(\"file\").cumcount()\ncells[\"studied\"] = (cells.n_fle >= pasq.MIN_PERTURBATIONS) & (cells.n_ext >= pasq.MIN_PERTURBATIONS)\nstudied = cells[cells.studied].copy()\nstudied[\"state\"] = np.where(studied.post, \"post\", \"pre\")\nPTN, CSN = \"pyramidal_tract_neuron\", \"corticostriatal_neuron\"\ngroups = {\"M1\": studied.index == studied.index, \"PTN\": (studied.ptype == PTN).values,\n          \"CSN\": (studied.ptype == CSN).values}\nfirst_day = pd.to_datetime(cells.date).min()\n\"\"\")\n\nmd(\"## Data check\")\n\ncode(\"\"\"\nall_units = pd.concat([x[\"units\"].assign(subject=\"Venus\", path=x[\"path\"]) for x in venus]\n                      + [x[\"units\"].assign(subject=\"Leu\", path=x[\"path\"]) for x in leu], ignore_index=True)\nprint(\"units by subject, MPTP state and projection type\")\nprint(all_units.groupby([\"subject\", \"post\", \"ptype\"]).size().to_string())\nprint(\"unit names repeated across files:\", all_units.unit_name.duplicated().sum())\nfname_post = all_units.path.str.contains(\"PostMPTP\")\nprint(\"units whose is_post_mptp disagrees with the file name:\", int((fname_post != all_units.post).sum()))\n\npert = pd.concat([x[\"pert\"].assign(file=i, post=bool(x[\"units\"].post.iloc[0])) for i, x in enumerate(venus)])\nprint(\"\\\\nVenus perturbations by state and direction\")\nprint(pert.groupby([\"post\", \"torque\"]).size().to_string())\nprint(\"Venus files without any perturbation:\", sum(len(x[\"pert\"]) == 0 for x in venus))\nprint(\"Leu trials by torque_perturbation_type:\",\n      pd.Series(np.concatenate([x[\"torque_type\"] for x in leu])).value_counts().to_dict())\nprint(\"Leu perturbation onset times that are not NaN:\", int(sum(np.isfinite(x[\"onset\"]).sum() for x in leu)))\n\ndates = pd.to_datetime(cells.date)\nprint(\"\\\\nVenus recording dates: pre\", dates[~cells.post].min().date(), \"to\", dates[~cells.post].max().date(),\n      \"; post\", dates[cells.post].min().date(), \"to\", dates[cells.post].max().date())\ndelay = (pert.onset - pert.center)\nprint(\"perturbation onset after centre target appearance (s): median %.3f, 5th to 95th percentile %.3f to %.3f\"\n      % (delay.median(), delay.quantile(0.05), delay.quantile(0.95)))\nprint(\"units with fewer observed perturbations than their file has:\",\n      int((cells.n_fle + cells.n_ext < [len(venus[f][\"pert\"]) for f in cells.file]).sum()))\n\nang = np.concatenate([x[\"angle\"].ravel() for x in venus if x[\"angle\"] is not None and len(x[\"pert\"])])\nprint(\"\\\\nelbow angle around perturbations (degrees): %.1f to %.1f\" % (np.nanmin(ang), np.nanmax(ang)))\nemg_vals = {ch: np.concatenate([x[\"emg\"][ch].ravel() for x in venus if ch in x[\"emg\"]]) for ch in pasq.EMG_CHANNELS}\nfor ch, v in emg_vals.items():\n    print(f\"{ch}: {sum(ch in x['emg'] for x in venus)} files, values {np.nanmin(v):.0f} to {np.nanmax(v):.0f} (a.u.)\")\nprint(\"SDF kernel: gamma k = %.1f, theta = %.0f ms, mode %.0f ms, mean %.0f ms; t threshold %.3f\"\n      % (pasq.GAMMA_K, pasq.GAMMA_THETA_MS, (pasq.GAMMA_K - 1) * pasq.GAMMA_THETA_MS,\n         pasq.GAMMA_K * pasq.GAMMA_THETA_MS, pasq.T_CRIT))\n\"\"\", tags=[\"sanity\"])\n\nmd(\"\"\"\n### Recordings deposited twice\n\nEach trial's spikes, relative to its trial start, and each perturbation's angle and EMG windows\nare compared across all Venus files.\n\"\"\")\n\ncode(\"\"\"\nfrom collections import defaultdict\nfrom itertools import combinations\n\ndef shared(keys_by_file):\n    owners = defaultdict(set)\n    for f, keys in keys_by_file.items():\n        for k in keys:\n            owners[k].add(f)\n    pairs = defaultdict(int)\n    for fs in owners.values():\n        for a, b in combinations(sorted(fs), 2):\n            pairs[(a, b)] += 1\n    return pairs\n\nspike_keys = {}\nfor fi, x in enumerate(venus):\n    keys = []\n    for ui, st in enumerate(x[\"spikes_all\"]):\n        for a, b in zip(x[\"trials\"].start, x[\"trials\"].stop):\n            s = np.round(st[(st >= a) & (st < b)] - a, 4)\n            if len(s) >= 5:\n                keys.append(tuple(s))\n    spike_keys[fi] = keys\nanalog_keys = {}\nfor fi, x in enumerate(venus):\n    keys = []\n    for name, arr in [(\"angle\", x[\"angle\"])] + list(x[\"emg\"].items()):\n        if arr is None:\n            continue\n        keys += [(name,) + tuple(np.round(w[::7], 2)) for w in arr if not np.isnan(w).any()]\n    analog_keys[fi] = keys\nprint(\"pairs of units sharing a trial's spike train:\", len(shared(spike_keys)))\nprint(\"pairs of files sharing an angle or EMG window:\", len(shared(analog_keys)))\n\"\"\", tags=[\"sanity\"])\n\nmd(\"\"\"\n### Clocks\n\nThe torque command, the elbow angle and the spikes are checked against the trials table's\nperturbation onsets. The command should leave rest a few ms after onset and the joint should move\nin the torque's direction after it. For the spikes, a contrast: threshold crossings by the claims\nfile's detection after the real onset against a pseudo onset 600 ms earlier and against trials\nwithout a perturbation aligned where the file's perturbations fall.\n\"\"\")\n\ncode(\"\"\"\nzt = -pasq.TORQUE_WINDOW_MS[0]\nfor post in [False, True]:\n    cmd = []\n    for x in venus:\n        if x[\"torque_cmd\"] is None or bool(x[\"units\"].post.iloc[0]) != post or len(x[\"pert\"]) == 0:\n            continue\n        s = np.where(x[\"pert\"].torque.values == \"flexion\", 1.0, -1.0)[:, None]\n        cmd.append(s * (x[\"torque_cmd\"] - x[\"torque_cmd\"][:, :zt].mean(1, keepdims=True)))\n    m = np.nanmean(np.vstack(cmd), 0)\n    half = np.where(m[zt:] > m[zt:zt + 50].max() / 2)[0][0]\n    leave = np.where(m[zt:] > 0.05 * m[zt:zt + 50].max())[0][0]\n    print(f\"{'post' if post else 'pre'}-MPTP: mean command leaves rest (5% of pulse) at {leave} ms and reaches half its peak at {half} ms after onset\")\nza = -pasq.ANGLE_WINDOW_MS[0]\nfor dname, sgn in [(\"flexion\", 1), (\"extension\", -1)]:\n    a = np.vstack([x[\"angle\"][x[\"pert\"].torque.values == dname] for x in venus if x[\"angle\"] is not None and len(x[\"pert\"])])\n    disp = np.nanmean(a - a[:, [za]], 0)\n    print(f\"{dname} torque: mean angle change at 0, 20, 50, 100 ms: \"\n          + \", \".join(f\"{disp[za + t]:+.2f}\" for t in [0, 20, 50, 100]) + \" deg (positive = flexion)\")\n\npr = pasq.pseudo_readings(venus, set(zip(studied.file, studied.unit)))\nnt = pasq.no_torque_crossings(venus, set(zip(studied.file, studied.unit)))\nprint(\"\\\\nany crossing of the claims file's threshold over 0 to 200 ms, per cell-direction:\")\nprint(\"  after torque onset %.3f (n = %d), after pseudo onset %.3f, after the no-torque alignment %.3f (n = %d cells)\"\n      % (pr[pr.onset == \"torque\"].mean_sd.mean(), (pr.onset == \"torque\").sum(),\n         pr[pr.onset == \"pseudo\"].mean_sd.mean(), nt.any_crossing.mean(), len(nt)))\non = np.concatenate([studied.fle_onset.dropna(), studied.ext_onset.dropna()])\nprint(\"response onsets after torque (ms): median %.0f, inside 20 to 60 by construction\" % np.median(on))\n\"\"\", tags=[\"sanity\"])\n\nmd(\"\"\"\nThe command leaves rest a few ms after the marked onset and the joint moves in the torque's\ndirection, so the analog series and the trials table share a clock (consistent with the data, as\nfar as a mean trace can show it). Spikes cross the threshold far more often after the real onset\nthan after the pseudo onset or in trials without a torque, so the spike times share it too.\n\"\"\")\n\nmd(\"\"\"\n### Findings about the data\n\nEach cell below shows one problem, loading only what it needs.\n\"\"\")\n\ncode(\"\"\"\n# Monkey L: no perturbation times, and no pulses in the torque command.\ntypes = pd.Series(np.concatenate([x[\"torque_type\"] for x in leu])).value_counts().to_dict()\nprint(\"Leu trials by torque_perturbation_type:\", types)\nprint(\"Leu files whose torque command has any finite value:\", sum(x[\"torque_cmd_finite\"] > 0 for x in leu), \"of\", len(leu))\nprint(\"Leu files with a step of more than 20 units in the command:\", sum(x[\"torque_cmd_steps\"] > 0 for x in leu))\n\"\"\", tags=[\"finding-leu-no-perturbations\"])\n\ncode(\"\"\"\n# The torque command's pulse is about three times larger after MPTP; the paper gives one 0.1 Nm pulse.\nkin_trials, kin_sessions = pasq.session_kinematics(venus)\nprint(kin_trials.groupby(\"post\").command.describe().round(1))\nprint(\"\\\\nsessions by median pulse size (a.u.), pre and post:\")\nprint(pd.crosstab(kin_trials.groupby(\"file\").post.first(),\n                  pd.cut(kin_trials.groupby(\"file\").command.median(), [0, 30, 60, 120, 250, 400])))\n\"\"\", tags=[\"finding-torque-command-levels\"])\n\ncode(\"\"\"\n# Torque-evoked displacements: the paper's mean is 10 degrees, and slower, smaller displacements after MPTP.\nprint(kin_sessions.groupby([\"post\", \"direction\"])[[\"peak_velocity\", \"amplitude\", \"latency\"]].mean().round(2))\nprint(\"perturbations with displacement >= 10 deg: %.1f%%\" % (100 * (kin_trials.amplitude >= 10).mean()))\nprint(\"sessions with mean peak velocity 130 to 200 deg/s:\",\n      int(kin_sessions.peak_velocity.between(130, 200).sum()), \"of\", len(kin_sessions))\n\"\"\", tags=[\"finding-kinematics-vs-paper\"])\n\nmd(\"## Claims\")\n\nmd(\"\"\"\n### cell-counts\n\n> In monkey V, 112 neurons were studied before MPTP and 159 after, of which 49 and 54 were PTNs\n> and 31 and 48 CSNs; three neurons in all were activated from both the peduncle and the putamen.\n\nCriterion: counts of monkey V units with at least 5 perturbations per direction, by MPTP state and\nprojection type; dual-projecting units counted over all files.\n\"\"\")\n\ncode(\"\"\"\nexpected = {\"M1\": (112, 159), \"PTN\": (49, 54), \"CSN\": (31, 48)}\nfor g, m in groups.items():\n    n = studied[m].groupby(\"post\").size()\n    print(f\"{g}: pre {n.get(False, 0)} (expected {expected[g][0]}), post {n.get(True, 0)} (expected {expected[g][1]})\")\ndual = all_units[all_units.ptype == \"pyramidal_tract_and_corticostriatal_neuron\"]\nprint(\"activated from both peduncle and putamen, all files:\", len(dual), dual.groupby(\"subject\").size().to_dict(),\n      \"; of these studied:\", int((studied.ptype == \"pyramidal_tract_and_corticostriatal_neuron\").sum()))\nprint(\"other types among the studied cells:\", studied[~studied.ptype.isin([PTN, CSN])].groupby([\"post\", \"ptype\"]).size().to_dict())\nprint(\"Venus units left out for fewer than 5 perturbations in a direction:\",\n      cells[~cells.studied].groupby(\"post\").size().to_dict())\n\"\"\", tags=[\"claim:cell-counts\"])\n\nmd(\"\"\"\n**Result: reproduced.** 115 and 157 cells before and after MPTP (112 and 159 expected), 51 and 54\nPTNs (49 and 54), 32 and 48 CSNs (31 and 48), and 3 dual-projecting cells, all within tolerance.\n\"\"\")\n\nmd(\"\"\"\n### monkey-l-perturbations\n\n> In monkey L, 57 of 115 neurons before MPTP and 35 of 73 after responded to torque perturbations\n> of the wrist, and the monkey L responses enter all pooled results.\n\nBlocked: no Leu trial marks a perturbation (cell `finding-leu-no-perturbations`), and the torque\ncommand is NaN or without pulses, so the perturbations cannot be found.\n\"\"\")\n\ncode(\"\"\"\nprint(\"Leu units by state:\", all_units[all_units.subject == \"Leu\"].groupby(\"post\").size().to_dict())\nprint(\"Leu trials with a perturbation onset:\", int(sum(np.isfinite(x[\"onset\"]).sum() for x in leu)))\n\"\"\", tags=[\"claim:monkey-l-perturbations\"])\n\nmd(\"\"\"\n**Result: blocked (data missing).** The Leu files hold 128 and 72 units but no perturbation\ntimes.\n\"\"\")\n\nmd(\"\"\"\n### baseline-rate\n\n> Before torque onset, the firing rate of M1 neurons was lower after MPTP, because PTN rates fell\n> (Mann-Whitney p < 0.001) while CSN rates did not change (p = 0.5). In monkey V the rates were 12.6\n> and 8.9 spikes/s for all cells, 20.3 and 14.8 for PTNs, and 3.5 and 3.4 for CSNs.\n\nBaseline rate: the mean over all perturbations of the SDF over the 500 ms before onset (claims).\n\"\"\")\n\ncode(\"\"\"\nexp = {\"M1\": (12.6, 1.98, 8.9, 1.33), \"PTN\": (20.3, 2.46, 14.8, 2.72), \"CSN\": (3.5, 1.47, 3.4, 1.01)}\nfor g, m in groups.items():\n    s = studied[m]\n    a, b = s[~s.post].baseline_rate, s[s.post].baseline_rate\n    p = stats.mannwhitneyu(a, b, alternative=\"two-sided\").pvalue\n    e = exp[g]\n    print(f\"{g}: pre {a.mean():.2f} +/- {a.std():.2f} (expected {e[0]} +/- {e[1]}, n {len(a)}), \"\n          f\"post {b.mean():.2f} +/- {b.std():.2f} (expected {e[2]} +/- {e[3]}, n {len(b)}); \"\n          f\"change {100 * (b.mean() / a.mean() - 1):+.0f}%, Mann-Whitney p = {p:.3g}\")\n\"\"\", tags=[\"claim:baseline-rate\"])\n\nmd(\"\"\"\n**Result: reproduced.** All six means are within tolerance (M1 12.66 and 8.85, PTN 18.49 and\n14.37, CSN 3.48 and 3.36 spikes/s); the PTN rate is lower after MPTP (p = 0.0066) and the CSN\nrate does not differ (p = 0.92). The PTN test does not reach the paper's p < 0.001.\n\"\"\")\n\nmd(\"\"\"\n### ptn-faster-than-csn\n\n> Before MPTP, PTNs fired much faster than CSNs at rest (Mann-Whitney p < 0.001).\n\"\"\")\n\ncode(\"\"\"\npre = studied[~studied.post]\na, b = pre[pre.ptype == PTN].baseline_rate, pre[pre.ptype == CSN].baseline_rate\nprint(f\"pre-MPTP PTN {a.mean():.2f} spikes/s (range {a.min():.1f} to {a.max():.1f}, n {len(a)}), \"\n      f\"CSN {b.mean():.2f} (range {b.min():.1f} to {b.max():.1f}, n {len(b)}); \"\n      f\"Mann-Whitney p = {stats.mannwhitneyu(a, b, alternative='two-sided').pvalue:.2g}\")\nprint(\"reported, not judged: text 16.3 and 3.6, Table 1 18.3 and 3.2 spikes/s (both monkeys)\")\n\"\"\", tags=[\"claim:ptn-faster-than-csn\"])\n\nmd(\"**Result: reproduced.** PTNs 18.49 against CSNs 3.48 spikes/s, Mann-Whitney p far below 0.001.\")\n\nmd(\"\"\"\n### antidromic-latency\n\n> PTN antidromic latencies did not change after MPTP (1.9 ms, p = 0.9), while CSN latencies were\n> longer (5.1 against 6.1 ms, p < 0.05/3).\n\"\"\")\n\ncode(\"\"\"\nexp = {\"PTN\": (1.9, 0.22, 1.9, 0.2), \"CSN\": (5.1, 0.61, 6.1, 0.89)}\nleu_units = all_units[all_units.subject == \"Leu\"]\nfor label, data in [(\"monkey V studied\", studied), (\"variant, + every Leu unit\", None)]:\n    for g, t in [(\"PTN\", PTN), (\"CSN\", CSN)]:\n        s = studied[studied.ptype == t][[\"post\", \"latency\"]]\n        if data is None:\n            s = pd.concat([s, leu_units[leu_units.ptype == t][[\"post\", \"latency\"]]])\n        a, b = s[~s.post].latency.dropna(), s[s.post].latency.dropna()\n        p = stats.mannwhitneyu(a, b, alternative=\"two-sided\").pvalue\n        e = exp[g]\n        print(f\"{label} {g}: pre {a.mean():.2f} ms (expected {e[0]} +/- {e[1]}, n {len(a)}), \"\n              f\"post {b.mean():.2f} (expected {e[2]} +/- {e[3]}, n {len(b)}), Mann-Whitney p = {p:.3g}\")\n\"\"\", tags=[\"claim:antidromic-latency\"])\n\nmd(\"\"\"\n**Result: partially reproduced.** The PTN latency does not differ (p >= 0.05) and three of the four\nmeans are within tolerance, but the CSN latency is not longer after MPTP with p < 0.05/3; see the\nnumbers above.\n\"\"\")\n\nmd(\"\"\"\n### false-positive-rate\n\n> The detection threshold, p < 0.01 divided by 5 independent comparisons, holds the chance of a\n> false response over the 200 ms epoch near 0.01.\n\nCriterion: the same detection at a pseudo onset 600 ms before the torque, on the studied cells,\nboth directions; reproduced when the fraction of cell-directions with any threshold crossing over\n0 to 200 ms is between 0.0033 and 0.03. The other readings of the Methods' test (step 1.6) are\nshown with the fraction of real cell-directions each would call responsive.\n\"\"\")\n\ncode(\"\"\"\npse = pr[pr.onset == \"pseudo\"]\nprint(\"claims file's detection, pseudo onset: any crossing over 0 to 200 ms %.3f, response with onset in 20 to 60 ms %.3f (n = %d cell-directions)\"\n      % (pse.mean_sd.mean(), np.r_[studied.pse_fle_responds, studied.pse_ext_responds].mean(), len(pse)))\nprint(\"no-torque trials, same detection: any crossing %.3f, response 20 to 60 ms %.3f (n = %d cells)\"\n      % (nt.any_crossing.mean(), nt.responds.mean(), len(nt)))\nprint(\"\\\\nreadings of the test (fraction of cell-directions with any crossing over 0 to 200 ms):\")\nprint(pr.groupby(\"onset\")[[\"mean_sd\", \"ttest\", \"trial_se\", \"trial_sd\"]].mean().round(3).T)\nfor label, s in [(\"pre\", studied[~studied.post]), (\"post\", studied[studied.post])]:\n    print(f\"pseudo any-crossing rate {label}-MPTP: \"\n          f\"{np.r_[s.pse_fle_any_crossing, s.pse_ext_any_crossing].mean():.3f}\")\n\"\"\", tags=[\"claim:false-positive-rate\"])\n\nmd(\"\"\"\n**Result: blocked (methods underspecified).** The claims file's detection crosses its threshold in\n0.23 of cell-directions after a pseudo onset (0.20 in trials without a torque), far above the\npaper's 0.01 and outside 0.0033 to 0.03, so this procedure is not the paper's. Of the other\nreadings, only a threshold from the SD of all single-trial baseline values comes near 0.01\n(0.013), and it calls only 0.20 of real cell-directions responsive, far below the paper's 62 to\n75% of cells; no reading gives both.\n\"\"\")\n\nmd(\"\"\"\n### Claims that use the selection of responses (blocked, shown)\n\nThese claims depend on `torque-related-fractions`, which depends on `false-positive-rate`, and are\nblocked with it. Their results under the claims file's detection are computed here so that a later\nattempt, or the authors, can see them; they decide nothing.\n\"\"\")\n\ncode(\"\"\"\nstudied[\"tr\"] = studied.fle_responds.fillna(False).astype(bool) | studied.ext_responds.fillna(False).astype(bool)\nexp = {\"M1\": (75, 68), \"PTN\": (55, 68), \"CSN\": (45, 21)}\nfor g, m in groups.items():\n    s = studied[m]\n    f = s.groupby(\"post\").tr.agg([\"sum\", \"size\", \"mean\"])\n    print(f\"{g}: pre {int(f.loc[False, 'sum'])}/{int(f.loc[False, 'size'])} ({100 * f.loc[False, 'mean']:.1f}%, expected {exp[g][0]}), \"\n          f\"post {int(f.loc[True, 'sum'])}/{int(f.loc[True, 'size'])} ({100 * f.loc[True, 'mean']:.1f}%, expected {exp[g][1]})\")\nstudied[\"tr_ttest\"] = studied.fle_ttest_responds.fillna(False).astype(bool) | studied.ext_ttest_responds.fillna(False).astype(bool)\nprint(\"variant (t-test of single trials):\", (100 * studied.groupby(\"post\").tr_ttest.mean()).round(1).to_dict())\n\"\"\", tags=[\"claim:torque-related-fractions\"])\n\ncode(\"\"\"\ndef yates(table):\n    chi2, p, _, _ = stats.chi2_contingency(np.asarray(table), correction=True)\n    return chi2, p\n\nfor g, m in groups.items():\n    s = studied[m]\n    t = pd.crosstab(s.post, s.tr)\n    chi2, p = yates(t)\n    print(f\"{g}: torque-related pre {100 * s[~s.post].tr.mean():.1f}%, post {100 * s[s.post].tr.mean():.1f}%, \"\n          f\"Yates chi2 = {chi2:.2f}, p = {p:.3g}\")\n\"\"\", tags=[\"claim:prevalence-unchanged\"])\n\ncode(\"\"\"\ns = studied[studied.ptype.isin([PTN, CSN])]\nt = pd.crosstab(s.ptype, s.tr)\nchi2, p = yates(t)\nprint(f\"PTN {100 * s[s.ptype == PTN].tr.mean():.1f}% (expected 62.1), CSN {100 * s[s.ptype == CSN].tr.mean():.1f}% (expected 30.4); \"\n      f\"Yates chi2 = {chi2:.1f}, p = {p:.2g}\")\n\"\"\", tags=[\"claim:ptn-more-responsive\"])\n\ncode(\"\"\"\ntr = studied[studied.tr]\none = tr.fle_responds.fillna(False).astype(bool) ^ tr.ext_responds.fillna(False).astype(bool)\nprint(f\"one direction only: {one.sum()}/{len(tr)} ({100 * one.mean():.1f}%, expected 44)\")\n\"\"\", tags=[\"claim:one-direction-half\"])\n\nresp_cell = \"\"\"\nrows = []\nfor _, c in studied.iterrows():\n    for d in [\"fle\", \"ext\"]:\n        if c.get(f\"{d}_responds\") is True:\n            rows.append({\"file\": c.file, \"unit\": c.unit, \"post\": c.post, \"ptype\": c.ptype, \"direction\": d,\n                         \"date\": c.date, \"baseline_rate\": c.baseline_rate,\n                         **{k: c[f\"{d}_{k}\"] for k in [\"onset\", \"offset\", \"sign\", \"mean_change\", \"max_change\",\n                                                         \"area\", \"mean_rate\", \"fwhm\"]}})\nresp = pd.DataFrame(rows)\nresp[\"increase\"] = resp.sign > 0\nprint(f\"{len(resp)} responses in {resp.groupby(['file', 'unit']).ngroups} cells\")\nfor g, sel in [(\"M1\", resp.index == resp.index), (\"PTN\", resp.ptype == PTN)]:\n    s = resp[sel]\n    print(f\"{g}: increases pre {100 * s[~s.post].increase.mean():.1f}%, post {100 * s[s.post].increase.mean():.1f}%\")\ns = resp[resp.ptype == PTN]\nchi2, p = yates(pd.crosstab(s.post, s.increase))\nprint(f\"PTN increases against decreases, pre against post: Yates chi2 = {chi2:.2f}, p = {p:.3g}\")\nprint(\"expected: M1 86 and 88, PTN 70 and 75\")\n\"\"\"\ncode(resp_cell, tags=[\"claim:excitatory-majority\"])\n\ncode(\"\"\"\nfor g, sel in [(\"M1\", resp.index == resp.index), (\"PTN\", resp.ptype == PTN)]:\n    s = resp[sel]\n    for meas in [\"mean_change\", \"max_change\", \"area\"]:\n        a, b = s[~s.post][meas], s[s.post][meas]\n        print(f\"{g} {meas}: pre median {a.median():.2f}, post {b.median():.2f}; KS p = {stats.ks_2samp(a, b).pvalue:.3g}, \"\n              f\"Mann-Whitney p = {stats.mannwhitneyu(a, b, alternative='two-sided').pvalue:.3g}\")\n\"\"\", tags=[\"claim:magnitude-unchanged\"])\n\ncode(\"\"\"\nexp = {(\"M1\", \"fle\"): (42.4, 37.9), (\"M1\", \"ext\"): (50.9, 42.6), (\"PTN\", \"fle\"): (33.4, 26.1), (\"PTN\", \"ext\"): (38.8, 29.3)}\nfor reading in [\"max_change\", \"mean_rate\", \"mean_change\"]:\n    out = []\n    for (g, d), e in exp.items():\n        s = resp[(resp.direction == d) & ((resp.ptype == PTN) if g == \"PTN\" else True)]\n        out.append(f\"{g} {d} {s[~s.post][reading].mean():.1f}/{s[s.post][reading].mean():.1f} (exp {e[0]}/{e[1]})\")\n    print(reading + \": \" + \"; \".join(out))\n\"\"\", tags=[\"claim:venus-response-magnitudes\"])\n\ncode(\"\"\"\nexp = {(\"M1\", \"fle\"): (39.2, 34.56), (\"M1\", \"ext\"): (40.4, 33.4), (\"PTN\", \"fle\"): (43.9, 35.5), (\"PTN\", \"ext\"): (44.4, 36.7)}\nfor (g, d), e in exp.items():\n    s = resp[(resp.direction == d) & ((resp.ptype == PTN) if g == \"PTN\" else True)]\n    a, b = s[~s.post].onset, s[s.post].onset\n    print(f\"{g} {d}: pre {a.mean():.1f} ms (exp {e[0]}, n {len(a)}), post {b.mean():.1f} (exp {e[1]}, n {len(b)}), \"\n          f\"KS p = {stats.ks_2samp(a, b).pvalue:.3g}\")\nearliest = resp.groupby([\"file\", \"unit\", \"post\", \"ptype\", \"date\"]).onset.min().reset_index()\nfor g, s in [(\"M1\", earliest), (\"PTN\", earliest[earliest.ptype == PTN])]:\n    print(f\"{g} earliest per cell: pre {s[~s.post].onset.mean():.1f}, post {s[s.post].onset.mean():.1f} ms\")\n\"\"\", tags=[\"claim:latency-shorter\"])\n\ncode(\"\"\"\nearliest[\"day\"] = (pd.to_datetime(earliest.date) - first_day).dt.days\nrho, p = stats.spearmanr(earliest.day, earliest.onset)\nprint(f\"latency against days since the first Venus session: Spearman rho = {rho:.3f}, p = {p:.3g}, n = {len(earliest)}\")\nfor post, s in earliest.groupby(\"post\"):\n    r, pp = stats.spearmanr(s.day, s.onset)\n    print(f\"  {'post' if post else 'pre'} only: rho = {r:.3f}, p = {pp:.3g}, n = {len(s)}\")\n\"\"\", tags=[\"claim:latency-not-training\"])\n\ncode(\"\"\"\nexp = {\"fle\": (97, 52), \"ext\": (57, 41)}\nfor d, e in exp.items():\n    s = resp[(resp.ptype == PTN) & (resp.direction == d)]\n    inc = s[s.increase]\n    a, b = inc[~inc.post].fwhm, inc[inc.post].fwhm\n    print(f\"PTN {d} increases: FWHM pre {a.mean():.1f} ms (exp {e[0]}, n {len(a)}), post {b.mean():.1f} (exp {e[1]}, n {len(b)}), \"\n          f\"Mann-Whitney p = {stats.mannwhitneyu(a, b, alternative='two-sided').pvalue:.3g}; all responses \"\n          f\"{s[~s.post].fwhm.mean():.1f} and {s[s.post].fwhm.mean():.1f}\")\n\"\"\", tags=[\"claim:fwhm-shorter-ptn\"])\n\ncode(\"\"\"\ndef dsi(c):\n    f, e = c.fle_max_change_signed, c.ext_max_change_signed\n    p_, np_ = (f, e) if abs(f) >= abs(e) else (e, f)\n    return abs(1 - np_ / p_)\n\ndef category(c):\n    fr, er = c.fle_responds is True, c.ext_responds is True\n    if fr != er:\n        return \"unidirectional\"\n    if c.fle_sign != c.ext_sign:\n        return \"reciprocal\"\n    return \"bidirectional\" if c.dsi > 0.5 else \"non-directional\"\n\ntr = studied[studied.tr].copy()\ntr[\"dsi\"] = tr.apply(dsi, axis=1)\ntr[\"category\"] = tr.apply(category, axis=1)\nt = pd.crosstab(tr.post, tr.category)\nprint(t)\nchi2, p, _, _ = stats.chi2_contingency(t)\nhi = tr.category.isin([\"reciprocal\", \"unidirectional\"])\nprint(f\"reciprocal + unidirectional: pre {100 * hi[~tr.post].mean():.1f}%, post {100 * hi[tr.post].mean():.1f}%; \"\n      f\"chi2 = {chi2:.1f}, p = {p:.3g}\")\n\"\"\", tags=[\"claim:dsi-reduced\"])\n\ncode(\"\"\"\nexp = {\"M1\": (0.72, 0.66), \"PTN\": (0.73, 0.75), \"CSN\": (0.81, 0.83)}\nfor g, e in exp.items():\n    s = tr if g == \"M1\" else tr[tr.ptype == (PTN if g == \"PTN\" else CSN)]\n    print(f\"{g}: DSI pre {s[~s.post].dsi.mean():.2f} (exp {e[0]}, n {(~s.post).sum()}), \"\n          f\"post {s[s.post].dsi.mean():.2f} (exp {e[1]}, n {s.post.sum()})\")\n\"\"\", tags=[\"claim:venus-dsi\"])\n\ncode(\"\"\"\ngroups_dsi = [g.baseline_rate.values for _, g in tr.groupby(\"category\")]\nF, p = stats.f_oneway(*groups_dsi)\nprint(f\"baseline rate across {tr.category.nunique()} categories: F = {F:.2f}, p = {p:.3g}\")\ntr[\"cat3\"] = tr.category.replace({\"reciprocal\": \"high\", \"unidirectional\": \"high\"})\nF3, p3 = stats.f_oneway(*[g.baseline_rate.values for _, g in tr.groupby(\"cat3\")])\nprint(f\"variant, three groups: F = {F3:.2f}, p = {p3:.3g}\")\n\"\"\", tags=[\"claim:dsi-not-baseline\"])\n\ncode(\"\"\"\nvel = kin_sessions.set_index([\"file\", \"direction\"]).peak_velocity\nfor d, dn in [(\"fle\", \"flexion\"), (\"ext\", \"extension\")]:\n    s = resp[resp.direction == d]\n    v = np.array([vel.get((f, dn), np.nan) for f in s.file])\n    s = s[(v >= 130) & (v <= 200)]\n    print(f\"{dn}: responses from sessions with mean peak velocity 130 to 200 deg/s: pre {(~s.post).sum()}, post {s.post.sum()}\")\n\"\"\", tags=[\"claim:velocity-matched-magnitude\"])\n\ncode(\"\"\"\nemg = pasq.session_emg(venus)\nptn_lat = earliest[earliest.ptype == PTN].groupby(\"file\").onset.mean()\nv_both = kin_sessions.groupby(\"file\").peak_velocity.mean()\nm2_tl1 = emg[(emg.channel == \"EMGTricepsLongus1\") & ~emg.has_nan & (emg.baseline_sd >= 1)].set_index(\"file\").m2\nfor label, other in [(\"peak velocity\", v_both), (\"triceps longus 1 m2\", m2_tl1)]:\n    j = pd.concat([ptn_lat, other], axis=1, join=\"inner\").dropna()\n    rho, p = stats.spearmanr(j.iloc[:, 0], j.iloc[:, 1])\n    print(f\"mean PTN latency against {label}: rho = {rho:.3f}, p = {p:.3g}, n = {len(j)} sessions\")\n\"\"\", tags=[\"claim:session-correlations\"])\n\nmd(\"\"\"\n**Result: blocked (methods underspecified), through false-positive-rate.** The numbers above use a\ndetection whose false-positive rate is 0.23 per cell-direction, about 20 times the paper's, and\ndecide nothing. No session has a mean peak velocity in the 130 to 200 deg/s range of\nvelocity-matched-magnitude.\n\"\"\")\n\nmd(\"\"\"\n### kinematics-slower\n\n> After MPTP, torque-induced displacements were slower and smaller; mean peak velocity fell by\n> 16.2% and amplitude by 6.6% (ANOVA, F > 515 and F > 49).\n\nCriterion: session means per direction, monkey V; two-way ANOVA (type II) of MPTP state and\ndirection with their interaction; the change is the post mean over the pre mean, minus 1;\nreadings (a) both directions pooled, (b) flexion only. Kinematic parameters: `pasq.py` docstring.\n\"\"\")\n\ncode(\"\"\"\ndef anova(df, meas):\n    model = smf.ols(f\"{meas} ~ C(post) * C(direction)\", data=df).fit()\n    return sm.stats.anova_lm(model, typ=2)\n\nprint(\"sessions:\", kin_sessions.groupby([\"post\", \"direction\"]).size().to_dict())\nprint(\"perturbations without a movement onset within 200 ms:\", int(kin_trials.latency.isna().sum()), \"of\", len(kin_trials))\nfor meas in [\"peak_velocity\", \"amplitude\"]:\n    a = anova(kin_sessions, meas)\n    pooled = 100 * (kin_sessions[kin_sessions.post][meas].mean() / kin_sessions[~kin_sessions.post][meas].mean() - 1)\n    f = kin_sessions[kin_sessions.direction == \"flexion\"]\n    flex = 100 * (f[f.post][meas].mean() / f[~f.post][meas].mean() - 1)\n    print(f\"\\\\n{meas}: change (a) pooled {pooled:+.1f}%, (b) flexion {flex:+.1f}%; MPTP F = {a.loc['C(post)', 'F']:.1f}, \"\n          f\"p = {a.loc['C(post)', 'PR(>F)']:.2g}\")\n    print(a.round(4))\n\"\"\", tags=[\"claim:kinematics-slower\"])\n\nmd(\"\"\"\nA variant, not deciding: the pulse of the torque command is about three times larger after MPTP\n(cell `finding-torque-command-levels`). Restricting to perturbations whose command pulse is 60 to\n250 units, the range both states share, gives the comparison at similar torques.\n\"\"\")\n\ncode(\"\"\"\nmatched = kin_trials[kin_trials.command.between(60, 250)]\nms = matched.groupby([\"file\", \"post\", \"direction\"])[[\"latency\", \"peak_velocity\", \"amplitude\"]].mean().reset_index()\nprint(\"perturbations kept:\", matched.groupby(\"post\").size().to_dict(), \"; sessions:\", ms.groupby(\"post\").size().to_dict())\nfor meas in [\"peak_velocity\", \"amplitude\", \"latency\"]:\n    a = anova(ms, meas)\n    ch = 100 * (ms[ms.post][meas].mean() / ms[~ms.post][meas].mean() - 1)\n    print(f\"{meas}: pre {ms[~ms.post][meas].mean():.2f}, post {ms[ms.post][meas].mean():.2f}, change {ch:+.1f}%, \"\n          f\"MPTP F = {a.loc['C(post)', 'F']:.1f}, p = {a.loc['C(post)', 'PR(>F)']:.2g}\")\n\"\"\", tags=[\"claim:kinematics-slower\"])\n\nmd(\"\"\"\n**Result: not reproduced.** Under both readings the displacements are faster and larger after\nMPTP, not slower and smaller (peak velocity +28.1% pooled and +29.7% for flexion; amplitude +14.8%\nand +11.1%). At the torque levels both states share, peak velocity changes by +9.1% and amplitude\nby -0.5%, neither significant at 0.05 (variant above).\n\"\"\")\n\nmd(\"\"\"\n### kinematic-latency-unchanged\n\n> The latency of torque-induced displacements did not change after MPTP (F < 0.2, p > 0.05).\n\"\"\")\n\ncode(\"\"\"\na = anova(kin_sessions, \"latency\")\nprint(kin_sessions.groupby([\"post\", \"direction\"]).latency.mean().round(2))\nprint(a.round(4))\n\"\"\", tags=[\"claim:kinematic-latency-unchanged\"])\n\nmd(\"\"\"\n**Result: not reproduced.** The movement onset latency is shorter after MPTP, MPTP effect F = 709,\np < 1e-100; the MPTP by direction interaction is F = 16.1 (the paper's F > 94). At matched torque\nlevels (variant above) the latency effect is much smaller.\n\"\"\")\n\nmd(\"\"\"\n### EMG claims\n\nSession-average EMG of the three triceps channels for flexion torques (claims). A channel is used\nin a session when no window holds a NaN and its baseline SD is at least 1 A/D unit; the claims\nfile does not say whether this is the SD of the session-average trace (main, the SD the response\nthreshold uses) or of the single-trial samples (shown as a variant).\n\"\"\")\n\ncode(\"\"\"\ndef emg_used(rule):\n    return emg[~emg.has_nan & (emg[rule] >= 1)]\n\nprint(\"channel-sessions:\", emg.groupby([\"channel\", \"post\"]).size().to_dict())\nprint(\"with NaN in a window:\", int(emg.has_nan.sum()))\nfor rule in [\"baseline_sd\", \"raw_sd\"]:\n    print(f\"used under {rule} >= 1:\", emg_used(rule).groupby([\"channel\", \"post\"]).size().to_dict())\n\"\"\")\n\ncode(\"\"\"\nfor rule in [\"baseline_sd\", \"raw_sd\"]:\n    print(\"rule\", rule)\n    for ch, g in emg_used(rule).groupby(\"channel\"):\n        a, b = g[~g.post].m2, g[g.post].m2\n        print(f\"  {ch}: m2 median pre {a.median():.1f}, post {b.median():.1f} (a.u.), n {len(a)} and {len(b)}, \"\n              f\"KS p = {stats.ks_2samp(a, b).pvalue:.2g}\")\n\"\"\", tags=[\"claim:emg-m2-larger\"])\n\nmd(\"\"\"\n**Result: reproduced.** m2 is larger after MPTP in all three triceps channels (KS p < 1e-14 in\neach) under both channel rules. The torque pulses are also about three times larger after MPTP\n(cell `finding-torque-command-levels`), which this comparison cannot separate from the effect of\nMPTP.\n\"\"\")\n\ncode(\"\"\"\nfor rule in [\"baseline_sd\", \"raw_sd\"]:\n    u = emg_used(rule)\n    d = u.dropna(subset=[\"duration\"])\n    a, b = d[~d.post].duration, d[d.post].duration\n    print(f\"rule {rule}: duration pre {a.mean():.1f} ms (exp 57 +/- 6, n {len(a)}), post {b.mean():.1f} (exp 79 +/- 3, n {len(b)}), \"\n          f\"KS p = {stats.ks_2samp(a, b).pvalue:.2g}; channel-sessions without a response: \"\n          f\"{u.duration.isna().groupby(u.post).sum().to_dict()}\")\n    print(\"  by channel:\", d.groupby([\"channel\", \"post\"]).duration.mean().round(1).to_dict())\n\"\"\", tags=[\"claim:emg-duration-longer\"])\n\nmd(\"\"\"\n**Result: partially reproduced.** Durations are longer after MPTP (22.2 against 51.5 ms, KS\np < 1e-30), but both means are far outside the paper's 57 +/- 6 and 79 +/- 3 ms.\n\"\"\")\n\ncode(\"\"\"\nfor rule in [\"baseline_sd\", \"raw_sd\"]:\n    d = emg_used(rule).dropna(subset=[\"duration\"])\n    a, b = d[~d.post].onset, d[d.post].onset\n    print(f\"rule {rule}: onset pre {a.mean():.1f} ms (median {a.median():.0f}), post {b.mean():.1f} (median {b.median():.0f}), \"\n          f\"KS p = {stats.ks_2samp(a, b).pvalue:.2g}\")\n\"\"\", tags=[\"claim:emg-onset-unchanged\"])\n\nmd(\"\"\"\n**Result: not reproduced.** The earliest EMG responses start earlier after MPTP (44.2 against 25.0\nms on average, KS p < 1e-20).\n\"\"\")\n\ncode(\"\"\"\nfor rule in [\"baseline_sd\", \"raw_sd\"]:\n    u = emg_used(rule)\n    for post, g in u.groupby(\"post\"):\n        print(f\"rule {rule}, {'post' if post else 'pre'}: m2 > m1 in {(g.m2 > g.m1).sum()}/{len(g)} \"\n              f\"({100 * (g.m2 > g.m1).mean():.1f}%), median m1/m2 {(g.m1 / g.m2).median():.2f}\")\n\"\"\", tags=[\"claim:emg-m1-weak\"])\n\nmd(\"\"\"\n**Result: partially reproduced.** After MPTP m2 exceeds m1 in 98.3% of channel-sessions and the\nmedian m1/m2 is 0.25; before MPTP the median ratio is 0.14 but m2 exceeds m1 in 74.0%, just under\nthe 75% the criterion asks (74.3% under the other channel rule).\n\"\"\")\n\nmd(\"\"\"\n### trial-correlations\n\n> Trial by trial, PTN response latencies did not correlate with the peak velocity or the m2 EMG\n> response (Spearman |rho| < 0.34, p > 0.05).\n\n**Result: blocked (methods underspecified).** The criterion needs a single-trial response latency,\nwhich the Methods do not define; it also uses the response selection blocked above.\n\"\"\")\n\nmd(\"\"\"\n## Summary\n\n| Claim | Outcome |\n|---|---|\n| cell-counts | reproduced |\n| monkey-l-perturbations | blocked (data missing) |\n| baseline-rate | reproduced |\n| ptn-faster-than-csn | reproduced |\n| antidromic-latency | partially reproduced |\n| false-positive-rate | blocked (methods underspecified) |\n| 15 claims on the response selection | blocked (methods underspecified), results shown |\n| kinematics-slower | not reproduced |\n| kinematic-latency-unchanged | not reproduced |\n| emg-m2-larger | reproduced |\n| emg-duration-longer | partially reproduced |\n| emg-onset-unchanged | not reproduced |\n| emg-m1-weak | partially reproduced |\n| trial-correlations | blocked (methods underspecified) |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nHow the analysis differs from the paper's: monkey V only; units are this dataset's files' units;\nthe response detection is the claims file's, whose false-positive rate is about 20 times the\npaper's, so no claim that rests on the response selection is decided; kinematic and EMG\nparameters the paper does not give are the claims file's or standard choices (`pasq.py`).\n\nWhat was found about the dataset: the counts of cells by state and projection type match the\npaper's monkey V table; no recording is deposited twice; the Leu files hold no perturbation\ntimes; the torque command's pulses are about three times larger after MPTP than before, and the\nevoked displacements (about 3 to 4 degrees) are smaller than the paper's 10 degrees and faster,\nnot slower, after MPTP.\n\"\"\")\n\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbf.write(nb, \"entries/pasquereau-2013/reproduce_pasquereau_2013.ipynb\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/work/make_nb.py (file state is current in your context — no need to Read it back)
```

**Agent**

Before the full run I'll execute a development copy of the notebook against the cached data.

**Agent calls Bash**

```bash
cd $TMPDIR/work; . ../env/bin/activate; export PYTHONPATH=entries/pasquereau-2013; python make_nb.py && python - <<'EOF'
import pickle, pasq, time
t=time.time(); leu=pasq.load_meta_all(pasq.asset_urls("sub-Leu")); print(time.time()-t)
pickle.dump(leu,open('leu.pkl','wb'))
EOF
python - <<'EOF'
import nbformat
nb=nbformat.read('entries/pasquereau-2013/reproduce_pasquereau_2013.ipynb',4)
for c in nb.cells:
    if c.cell_type=='code' and 'venus = pasq.load_all' in c.source:
        c.source="import pickle\nvenus=pickle.load(open('/tmp/claude-1001/work/venus.pkl','rb'))\nleu=pickle.load(open('/tmp/claude-1001/work/leu.pkl','rb'))"
nbformat.write(nb,'dev.ipynb')
EOF
time jupyter nbconvert --to notebook --execute dev.ipynb --output dev_out.ipynb --ExecutePreprocessor.timeout=1800 2>&1 | tail -3
```

```
50.86906099319458
trust

Jupyter command `jupyter-nbconvert` not found.

real	0m0.049s
user	0m0.042s
sys	0m0.009s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/work; . ../env/bin/activate; export PYTHONPATH=entries/pasquereau-2013; cat > run_nb.py <<'EOF'
import nbformat, sys
from nbclient import NotebookClient
nb=nbformat.read(sys.argv[1],4)
try:
    NotebookClient(nb,timeout=1800,kernel_name='python3').execute()
finally:
    nbformat.write(nb,sys.argv[2])
for c in nb.cells:
    if c.cell_type=='code':
        out=''.join(o.get('text','') if o.output_type=='stream' else (o.get('data',{}).get('text/plain','') if 'data' in o else o.get('ename','')+' '+o.get('evalue','')) for o in c.outputs)
        print('-----',c.metadata.get('tags'),'\n',out[:3000])
EOF
time python run_nb.py dev.ipynb dev_out.ipynb 2>&1 | tail -400
```

```
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
----- None 
 291 Venus files, 148 Leu files at version 0.261124.1906

----- None 
 sub-Venus/sub-Venus_ses-Venus++v0502++PreMPTP++Depth22130um++19990406_behavior+ecephys.nwb
acquisition EMGBrachioradialis: (165170,), unit a.u.
acquisition EMGDeltoidPosterior: (165170,), unit a.u.
acquisition EMGTrapezius: (165170,), unit a.u.
acquisition EMGTricepsLateralis: (165170,), unit a.u.
acquisition EMGTricepsLongus1: (165170,), unit a.u.
acquisition EMGTricepsLongus2: (165170,), unit a.u.
acquisition ElbowAngle: (165170, 1), unit degrees
acquisition ElbowTorque: (165170,), unit arbitrary
processing/antidromic_identification/AntidromicResponse_v0502.1_Peduncle: ElectricalSeries
processing/antidromic_identification/AntidromicStimulation_v0502.1_Peduncle: TimeSeries
processing/antidromic_identification/StimulationElectrodesTable: DynamicTable
processing/behavior/ElbowVelocity: TimeSeries
intervals AntidromicSweepsIntervals: 31 rows, columns ['start_time', 'stop_time', 'stimulation_onset_time', 'unit_name', 'unit', 'location', 'stimulation_protocol', 'source_label', 'sweep_number', 'response', 'stimulation', 'stimulation_electrode']
intervals invalid_times: 19 rows, columns ['start_time', 'stop_time', 'tags']
[... 303 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/work; . ../env/bin/activate; python - <<'EOF'
import pickle, json, remfile, h5py, numpy as np
leu=pickle.load(open('leu.pkl','rb'))
fin=[x for x in leu if x['torque_cmd_finite']>0]
print(len(fin), sum(x['units'].post.iloc[0] for x in fin), [x['path'][-58:-26] for x in fin[:3]])
assets=json.load(open('../assets.json')); a=[a for a in assets if a['path']==fin[0]['path']][0]
h=h5py.File(remfile.File(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/"),'r')
tq=h['acquisition/WristTorque/data'][:]; ts=h['acquisition/WristTorque/timestamps'][:]
tr=h['intervals/trials']; st=tr['start_time'][:]; ct=tr['center_target_appearance_time'][:]
d=np.diff(tq); big=np.where(np.abs(d)>20)[0]
print(len(tq), np.nanpercentile(tq,[1,50,99]), len(big))
for j in big[:15]:
    k=np.searchsorted(st,ts[j])-1
    print(round(ts[j],3), round(d[j],1), 'trial',k, 't-center %.3f'%(ts[j]-ct[k]), np.round(tq[j-2:j+8],0))
EOF
```

```
34 34 ['001++PostMPTP++Depth22890um++199', '002++PostMPTP++Depth23240um++199', '101++PostMPTP++Depth23270um++199']
33876 [-1.14694927e+02 -7.98354121e-04  1.70574659e+02] 1138
0.5 21.5 trial 0 t-center 0.000 [  5.  11.  24.  46.  73. 101. 124. 139. 145. 145.]
0.51 27.1 trial 0 t-center 0.010 [ 11.  24.  46.  73. 101. 124. 139. 145. 145. 143.]
0.52 28.0 trial 0 t-center 0.020 [ 24.  46.  73. 101. 124. 139. 145. 145. 143. 143.]
0.53 23.5 trial 0 t-center 0.030 [ 46.  73. 101. 124. 139. 145. 145. 143. 143. 147.]
0.64 -22.9 trial 0 t-center 0.140 [163. 163. 153. 130.  97.  58.  21. -10. -30. -40.]
0.65 -33.3 trial 0 t-center 0.150 [163. 153. 130.  97.  58.  21. -10. -30. -40. -39.]
0.66 -38.6 trial 0 t-center 0.160 [153. 130.  97.  58.  21. -10. -30. -40. -39. -33.]
0.67 -37.4 trial 0 t-center 0.170 [130.  97.  58.  21. -10. -30. -40. -39. -33. -23.]
0.68 -30.6 trial 0 t-center 0.180 [ 97.  58.  21. -10. -30. -40. -39. -33. -23. -14.]
0.69 -20.2 trial 0 t-center 0.190 [ 58.  21. -10. -30. -40. -39. -33. -23. -14.  -5.]
4.78 27.4 trial 0 t-center 4.280 [  3.  10.  27.  54.  89. 124. 154. 175. 188. 194.]
4.79 34.5 trial 0 t-center 4.290 [ 10.  27.  54.  89. 124. 154. 175. 188. 194. 201.]
4.8 35.5 trial 0 t-center 4.300 [ 27.  54.  89. 124. 154. 175. 188. 194. 201. 211.]
4.81 30.2 trial 0 t-center 4.310 [ 54.  89. 124. 154. 175. 188. 194. 201. 211. 224.]
4.82 21.1 trial 0 t-center 4.320 [ 89. 124. 154. 175. 188. 194. 201. 211. 224. 235.]
Shell cwd was reset to
```

**Agent**

The Leu post-MPTP command is a smooth trace with excursions lasting hundreds of ms, not 50 ms pulses, so the file description holds and the monkey L block stands. Correcting the notebook text now.

**Agent calls Bash**

```bash
cd $TMPDIR/work; python - <<'EOF'
p='make_nb.py'; s=open(p).read()
rep=[
('''print("Leu files whose torque command has any finite value:", sum(x["torque_cmd_finite"] > 0 for x in leu), "of", len(leu))
print("Leu files with a step of more than 20 units in the command:", sum(x["torque_cmd_steps"] > 0 for x in leu))''',
'''finite = [x for x in leu if x["torque_cmd_finite"] > 0]
print("Leu files whose torque command has any finite value:", len(finite), "of", len(leu),
      "; of these after MPTP:", sum(bool(x["units"].post.iloc[0]) for x in finite))'''),
('''**Result: blocked (data missing).** The Leu files hold 128 and 72 units but no perturbation
times.''','''**Result: blocked (data missing).** The Leu files hold 138 and 72 units but no perturbation
times, and the torque command is NaN in every file before MPTP.'''),
('''**Result: reproduced.** All six means are within tolerance (M1 12.66 and 8.85, PTN 18.49 and
14.37, CSN 3.48 and 3.36 spikes/s); the PTN rate is lower after MPTP (p = 0.0066) and the CSN
rate does not differ (p = 0.92). The PTN test does not reach the paper's p < 0.001.''',
'''**Result: reproduced.** All six means are within tolerance (M1 12.66 and 8.85, PTN 18.49 and
14.37, CSN 3.48 and 3.36 spikes/s); the PTN rate is lower after MPTP (Mann-Whitney p = 0.020) and
the CSN rate does not differ (p = 0.65). The PTN test does not reach the paper's p < 0.001; the M1
rate is also lower (p = 0.0022, below the paper's 0.05/2).'''),
('''**Result: partially reproduced.** The PTN latency does not differ (p >= 0.05) and three of the four
means are within tolerance, but the CSN latency is not longer after MPTP with p < 0.05/3; see the
numbers above.''','''**Result: partially reproduced.** All four means are within tolerance (PTN 1.92 and 1.86 ms, CSN
4.91 and 6.85 ms) and the PTN latency does not differ (p = 0.68), but the CSN latency, longer after
MPTP, has p = 0.019, above the 0.05/3 the criterion asks. With every Leu unit added (variant), the
CSN test gives p = 0.0072.'''),
('''**Result: not reproduced.** Under both readings the displacements are faster and larger after
MPTP, not slower and smaller (peak velocity +28.1% pooled and +29.7% for flexion; amplitude +14.8%
and +11.1%). At the torque levels both states share, peak velocity changes by +9.1% and amplitude
by -0.5%, neither significant at 0.05 (variant above).''','''**Result: not reproduced.** Under both readings the displacements are faster and larger after
MPTP, not slower and smaller (peak velocity +28.1% pooled and +29.7% for flexion; amplitude +14.8%
and +11.1%; MPTP F = 98.5 and 25.0). Restricted to command pulses of 60 to 250 units the increase
remains (+47.0% and +40.4%), so the command's arbitrary units do not explain it.'''),
('''p < 1e-100; the MPTP by direction interaction is F = 16.1 (the paper's F > 94). At matched torque
levels (variant above) the latency effect is much smaller.''','''p < 1e-100; the MPTP by direction interaction is F = 16.1 (the paper's F > 94). At command pulses
of 60 to 250 units (variant above) the latency is also shorter after MPTP (F = 238.6).'''),
]
for a,b in rep:
    assert a in s, a[:60]; s=s.replace(a,b)
open(p,'w').write(s)
EOF
date -u
```

```
Thu Nov 26 16:43:13 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/entry.schema.json'));print(json.dumps(s,indent=0)[:2500])"; cat protocol.lock; ls entries/*/entry.yaml | head -400 | xargs grep -l "^python:" | tail -2 | xargs cat
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
[... 140 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/pasquereau-2013; cat > entry.yaml <<'EOF'
schema_version: 1
name: pasquereau-2013
type: reproduction
title: Motor cortex responses to muscle stretch in the parkinsonian monkey (Pasquereau & Turner 2013)
description: Tests the findings of Pasquereau and Turner (2013) on dandiset 001636, which holds the
  single-unit recordings from primary motor cortex of two macaques before and after MPTP, with the
  torque perturbations, elbow angle and EMG of monkey V. It counts the cells studied, compares
  baseline rates and antidromic latencies, checks the false-positive rate of the response detection,
  and tests the behavioural and EMG effects of MPTP on the torque-evoked stretch. The monkey L files
  mark no perturbations.
license: Apache-2.0
notebooks:
- path: reproduce_pasquereau_2013.ipynb
  title: Reproducing Pasquereau & Turner (2013) from dandiset 001636
  runtime_minutes: 7
helpers:
- pasq.py
related:
- id: dandi:001636/0.261124.1906
  relation: uses_data
- id: doi:10.3389/fnsys.2013.00098
  relation: reproduces
EOF
printf "dandi\nh5py\nmatplotlib\nnumpy\npandas\npynwb\nremfile\nscipy\nstatsmodels\n" > requirements.in
cd $TMPDIR/work && . ../env/bin/activate && python make_nb.py && cd  && python tools/entry.py lock entries/pasquereau-2013 2>&1 | tail -5; cat entries/pasquereau-2013/entry.yaml | grep python
```

```
wrote pasquereau-2013/requirements.lock.txt (Python 3.13, with hashes)
python: "3.13"
```

**Agent calls Bash**

```bash
cd  sed -i '/matplotlib/d' entries/pasquereau-2013/requirements.in; python tools/entry.py lock entries/pasquereau-2013 2>&1 | tail -2; cat > entries/pasquereau-2013/README.md <<'EOF'
# Pasquereau & Turner (2013) from dandiset 001636

Tests the findings of [Pasquereau and Turner (2013)](https://doi.org/10.3389/fnsys.2013.00098) that
can be tested on [DANDI:001636](https://dandiarchive.org/dandiset/001636/0.261124.1906), which holds
single-unit recordings from primary motor cortex of monkeys V (Venus) and L (Leu) before and after
MPTP. Only the monkey V files mark the torque perturbations, so every claim is tested on monkey V.

| Claim | Outcome |
|---|---|
| Cells studied in monkey V, by state and projection type | Reproduced |
| Monkey L responses to wrist perturbations | Blocked: data missing |
| Baseline rate lower after MPTP for PTNs, not CSNs | Reproduced |
| PTNs fire faster than CSNs at rest | Reproduced |
| CSN antidromic latency longer after MPTP, PTN unchanged | Partially reproduced |
| False-positive rate of the response detection near 0.01 | Blocked: methods underspecified |
| 15 claims on the selected responses (prevalence, magnitude, latency, FWHM, directionality, correlations) | Blocked: methods underspecified |
| Torque-induced displacements slower and smaller after MPTP | Not reproduced |
| Latency of torque-induced displacements unchanged | Not reproduced |
| Long-latency (m2) EMG response larger after MPTP | Reproduced |
| EMG responses last longer after MPTP | Partially reproduced |
| Onset of EMG responses unchanged | Not reproduced |
| Short-latency (m1) EMG response weak | Partially reproduced |
| Trial-by-trial latency correlations | Blocked: methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The response detection the claims file specifies crosses its threshold in 23% of cell-directions
at a pseudo onset, about 20 times the paper's stated 1%, so the claims that rest on the selection
of responses are blocked; their results are shown in the notebook. The torque command's pulses are
about three times larger after MPTP than before, and the evoked displacements are faster and
larger after MPTP, the reverse of the paper's. The attempt record, with the reasons and the
differences from the paper's method, is
[`attempts/pasquereau-2013-03.yaml`](../../attempts/pasquereau-2013-03.yaml).

- `reproduce_pasquereau_2013.ipynb`: the analysis. It takes about seven minutes, most of it
  streaming the files.
- `pasq.py`: loading the files, spike density functions, response detection, kinematics and EMG
  measures, with where each parameter comes from. Other notebooks on this dandiset can import it.
EOF
date -u; time python tools/entry.py all entries/pasquereau-2013 2>&1 | tail -20
```

```
wrote pasquereau-2013/requirements.lock.txt (Python 3.13, with hashes)
Thu Nov 26 16:43:39 UTC 2026
Installed kernelspec registry-pasquereau-2013 in executed/pasquereau-2013/.venv/share/jupyter/kernels/registry-pasquereau-2013
0 error(s)
pass  reproduce_pasquereau_2013.ipynb  (348 s)

real	5m56.811s
user	0m59.027s
sys	0m5.922s
```

**Agent**

The full run passes in 348 s. Checking that the executed copy prints the same numbers as the development run.

**Agent calls Bash**

```bash
cd  ls executed/pasquereau-2013/; python3 - <<'EOF'
import json
nb=json.load(open('executed/pasquereau-2013/reproduce_pasquereau_2013.ipynb'))
for c in nb['cells']:
    if c['cell_type']=='code':
        tags=c['metadata'].get('tags')
        out=''.join(''.join(o.get('text','')) if o['output_type']=='stream' else str(o.get('ename','')) for o in c['outputs'])
        if tags and any(t.startswith(('claim:antid','claim:baseline','finding','claim:kinematic','claim:false')) for t in tags): print(tags, out[:1500])
EOF
```

```
reproduce_pasquereau_2013.ipynb
result.json
['finding-leu-no-perturbations'] Leu trials by torque_perturbation_type: {'not_available': 5952}
Leu files whose torque command has any finite value: 34 of 148 ; of these after MPTP: 34

['finding-torque-command-levels']         count   mean   std   min    25%    50%    75%    max
post                                                        
False  1947.0   58.4  28.1  -0.7   45.3   45.7   90.3  182.7
True   3603.0  174.7  47.6  26.0  155.3  181.6  184.5  343.5

sessions by median pulse size (a.u.), pre and post:
command  (30, 60]  (60, 120]  (120, 250]
post                                    
False         105         43           3
True            0         12         125

['finding-kinematics-vs-paper']                  peak_velocity  amplitude  latency
post  direction                                   
False extension          46.10       2.42    10.86
      flexion            58.11       3.40     9.65
[... 59 more lines not kept]
```

**Agent**

Executed outputs match. Now the attempt record; checking the schema and a recent record's format first.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json
s=json.load(open('schemas/attempt.schema.json'))
print(s.get('required')); 
P=s['properties']
for k in ['provenance','outcomes','findings','datasets','inputs']:
    print(k, json.dumps(P[k])[:1500]); print()
print(json.dumps(s.get('$defs',{}))[:3000])
EOF
ls -t attempts | head -3
```

```
['schema_version', 'id', 'datasets', 'paper', 'date', 'provenance', 'outcomes']
provenance {"type": "object", "additionalProperties": false, "required": ["kind", "accountable"], "properties": {"kind": {"enum": ["agent", "person"]}, "accountable": {"description": "The person or organisation responsible for this attempt.", "type": "object", "additionalProperties": false, "required": ["name"], "properties": {"name": {"type": "string"}, "orcid": {"type": "string", "pattern": "^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]$"}, "ror": {"type": "string"}}}, "agent": {"description": "Required when kind is agent.", "type": "object", "additionalProperties": false, "required": ["harness", "model", "protocol"], "properties": {"harness": {"type": "string"}, "model": {"type": "string"}, "protocol": {"description": "Version of the reproduction protocol the agent followed.", "type": "string"}}}, "runner": {"description": "Where the attempt was run: the platform, and the run that wrote this record. Its other runs (verification rounds, revisions) are linked from their transcripts.", "type": "object", "additionalProperties": false, "required": ["platform"], "properties": {"platform": {"description": "The platform that ran it, e.g. GitHub Actions, or local for a person's machine.", "type": "string", "minLength": 1}, "url": {"description": "The run that wrote the record, e.g. https://github.com/<owner>/<repo>/actions/runs/<id>.", "type": "string", "pattern": "^https://"}}}, "author_notes": {"description": "The notes from the paper's authors that this attempt used (papers/author-notes/<pape

outcomes {"description": "One per claim attempted.", "type": "array", "minItems": 1, "items": {"type": "object", "additionalProperties": false, "required": ["claim", "outcome"], "properties": {"claim": {"description": "Claim id from the target's claims file.", "type": "string"}, "outcome": {"enum": ["reproduced", "partially_reproduced", "not_reproduced", "blocked"], "description": "Describes the result, 
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json
s=json.load(open('schemas/attempt.schema.json'))
P=s['properties']
print(json.dumps(P['findings']['items']['properties'])[1400:4000])
print(json.dumps(P['outcomes']['items']['properties'])[1500:3500])
print(s['properties']['schema_version'], [k for k in P])
EOF
grep -n "^findings" -A30 attempts/zheng-2024-01.yaml | head -50
```

```
around, a wrong unit label included. `none`: no problem, a check that passed. Required from protocol pilot-18.", "enum": ["critical", "major", "minor", "none"]}, "datasets": {"description": "For a finding about the data, in an attempt that used several datasets: the folders of the datasets it is about (000147, crcns-hc-18). Unset: the attempt's one dataset, or all of them.", "type": "array", "minItems": 1, "items": {"type": "string"}}, "versions": {"description": "For a finding about the data: the versions of the dataset the finding was seen in, as the archive names them (0.240503.0152). Unset: the version the attempt read. Give it when the finding was seen in another version, such as the one the paper cites, and list the version the attempt read too if the finding is there as well. With several `datasets`, the versions are of the one dataset the finding names.", "type": "array", "minItems": 1, "uniqueItems": true, "items": {"type": "string", "minLength": 1}}, "fixed_in": {"description": "For a finding about the data: the first version of the dataset in which the attempt looked for the problem and it was gone. Unset: not known to be fixed. A fixed finding is kept in the record: it still matters for a paper that used the earlier version.", "type": "string", "minLength": 1}, "notebook": {"description": "Path of the notebook within the entry whose code shows the finding.", "type": "string", "minLength": 1}, "output": {"description": "Which output of that notebook shows the finding: a cell tag, as for an outcome.", "type": "string", "minLength": 1}}
md, Author, step 1.6).", "type": "boolean"}, "seed_sensitive": {"type": "boolean", "description": "True when the outcome is not the same under all five seeds the protocol asks for (docs/protocol.md, Author, step 3)."}, "proposed": {"description": "A change of outcome found after the last verification round, held until a further round agrees with it.", "type": "object", "additionalProperties": false, "required": ["outcome", "
[... 32 more lines not kept]
```

**Agent**

Writing the attempt record now, generated from Python so the YAML is valid.

**Agent calls Bash**

```bash
cd $TMPDIR/work; . ../env/bin/activate; cat > make_record.py <<'EOF'
import yaml
NB = "reproduce_pasquereau_2013.ipynb"

def o(claim, outcome, notes, output=None, blocked_by=None, measured=None, deviations=None, assumed=None):
    d = {"claim": claim, "outcome": outcome}
    if blocked_by: d["blocked_by"] = blocked_by
    d["notebook"] = NB
    d["output"] = output or f"claim:{claim}"
    if measured is not None: d["measured"] = measured
    d["notes"] = notes
    if deviations: d["deviations"] = deviations
    if assumed: d["assumed"] = True
    return d

SEL = ("Blocked with false-positive-rate, through torque-related-fractions; the claims file's detection, "
       "whose false-positive rate is 0.23 per cell-direction, gives the numbers here, which decide nothing.")
MONKEY_V = "Monkey V only; the paper's values pool both monkeys where the claim says so."

outcomes = [
 o("cell-counts", "reproduced",
   "Monkey V units with at least 5 observed perturbations per direction number 115 before and 157 after MPTP "
   "(112 and 159 expected), with 51 and 54 PTNs (49 and 54) and 32 and 48 CSNs (31 and 48). Three units in all "
   "files are pyramidal_tract_and_corticostriatal_neuron, all in monkey V and all studied; Leu has none. The "
   "studied cells also include 29 and 50 not activated, 1 and 1 not tested, and after MPTP one PTN-and-thalamic "
   "and two thalamic projection units. 79 pre and 5 post Venus units have fewer than 5 perturbations in a "
   "direction. No unit name repeats across files, and no trial spike train, angle or EMG window is shared "
   "between files.",
   measured=[115, 157, 51, 54, 32, 48, 3]),
 o("monkey-l-perturbations", "blocked",
   "All 5952 Leu trials have torque_perturbation_type not_available and no onset time. The Leu torque command "
   "is NaN in all 114 files before MPTP and, in the 34 after, a smooth trace without 50 ms pulses, so the "
   "perturbations cannot be recovered. The Leu files hold 138 and 72 units.",
   blocked_by="data_missing"),
 o("baseline-rate", "reproduced",
   "Mean baseline rates (spikes/s) M1 12.66 and 8.85, PTN 18.49 and 14.37, CSN 3.48 and 3.36, all within "
   "tolerance. PTN rate lower after MPTP (-22%, Mann-Whitney p = 0.020), CSN unchanged (p = 0.65), M1 lower "
   "(-30%, p = 0.0022, below the paper's 0.05/2). The PTN test does not reach the p < 0.001 of the statement.",
   measured=[12.66, 8.85, 18.49, 14.37, 3.48, 3.36]),
 o("ptn-faster-than-csn", "reproduced",
   "Pre-MPTP PTNs 18.49 spikes/s (n 51, range 2.6 to 49.0) against CSNs 3.48 (n 32, range 0.0 to 20.7), "
   "Mann-Whitney p = 6.3e-12. The pooled values 16.3 and 3.6 (text) and 18.3 and 3.2 (Table 1) are reported, not "
   "judged."),
 o("antidromic-latency", "partially_reproduced",
   "PTN latency 1.92 and 1.86 ms (n 49 and 48, Mann-Whitney p = 0.68); CSN 4.91 and 6.85 ms (n 32 and 38, "
   "p = 0.019). All four means are within tolerance and the PTN test holds, but the CSN test does not reach "
   "0.05/3 (0.0167). Two studied PTNs before and one after, and ten CSNs after MPTP, have no antidromic "
   "latency in the files. With every Leu PTN and CSN added (variant) the means are 1.80, 1.83, 5.38 and 7.01 ms "
   "and the CSN test gives p = 0.0072.",
   measured=[1.92, 1.86, 4.91, 6.85],
   deviations=["The expected values pool both monkeys; the test uses monkey V's studied cells (criterion)."]),
 o("false-positive-rate", "blocked",
   "With the claims file's detection at a pseudo onset 600 ms before the torque, 0.230 of 544 cell-directions "
   "cross the threshold over 0 to 200 ms (0.257 before and 0.210 after MPTP), and 0.051 have a response with "
   "onset in 20 to 60 ms. On trials without a perturbation, aligned where the file's perturbations fall, 0.196 "
   "of 255 cells cross. Both are far above 0.03, so by the claims file's rule and the protocol's the "
   "procedure is not the paper's. Other readings of the Methods' t-test give 0.465 (single-trial t-test, the "
   "claims file's variant), 0.347 (standard error of trial baselines) and 0.013 (SD of all single-trial "
   "baseline values); the last is near 0.01 but calls only 0.200 of real cell-directions responsive "
   "(0.673 with the claims file's detection), far below the paper's 62 to 75% of cells. No reading gives both "
   "the paper's false-positive rate and its response rates. Question for the authors, in findings.",
   blocked_by="methods_underspecified", measured=0.23,
   deviations=["The t threshold uses 499 degrees of freedom (500 baseline values), a standard choice.",
               "The kernel is truncated at 400 ms, a standard choice that cannot change a result."]),
 o("torque-related-fractions", "blocked",
   SEL + " Torque-related M1 64/115 (55.7%) and 78/157 (49.7%), PTN 37/51 (72.5%) and 37/54 (68.5%), CSN 5/32 "
   "(15.6%) and 9/48 (18.8%), against 75, 68, 55, 68, 45 and 21% expected. With the single-trial t-test 44.3% "
   "and 59.9% of cells.", blocked_by="methods_underspecified"),
 o("prevalence-unchanged", "blocked",
   SEL + " Yates chi-square, pre against post, M1 p = 0.40, PTN p = 0.81, CSN p = 0.95.",
   blocked_by="methods_underspecified"),
 o("ptn-more-responsive", "blocked",
   SEL + " PTN 70.5% and CSN 17.5% torque-related (62.1 and 30.4 expected), Yates chi2 = 49.0, p = 2.6e-12.",
   blocked_by="methods_underspecified"),
 o("one-direction-half", "blocked",
   SEL + " 75 of 142 torque-related cells (52.8%) respond to one direction only (44% expected).",
   blocked_by="methods_underspecified"),
 o("excitatory-majority", "blocked",
   SEL + " Increases are 83.3% and 76.5% of M1 responses and 70.6% and 58.3% of PTN responses before and after "
   "MPTP (86, 88, 70 and 75 expected); PTN Yates chi2 = 1.30, p = 0.25.",
   blocked_by="methods_underspecified"),
 o("magnitude-unchanged", "blocked",
   SEL + " Magnitudes are smaller after MPTP in all 12 tests (M1 and PTN; mean change, maximum change, area), "
   "KS p 0.00013 to 0.047 and Mann-Whitney p 1.9e-05 to 0.043.",
   blocked_by="methods_underspecified"),
 o("venus-response-magnitudes", "blocked",
   SEL + " Maximum change (reading a), pre and post, M1 flexion 38.1 and 30.7, M1 extension 45.3 and 31.5, PTN "
   "flexion 31.6 and 19.6, PTN extension 35.6 and 23.8 spikes/s; mean rate (b) and mean change (c) are in "
   "the notebook.", blocked_by="methods_underspecified"),
 o("latency-shorter", "blocked",
   SEL + " Latencies are shorter after MPTP in all four comparisons (KS p 0.0077 to 0.010); means M1 flexion "
   "40.9 and 35.5, M1 extension 42.9 and 36.1, PTN flexion 44.9 and 38.1, PTN extension 45.3 and 38.0 ms.",
   blocked_by="methods_underspecified"),
 o("latency-not-training", "blocked",
   SEL + " Earliest latency against days since the first Venus session, pre and post pooled, Spearman "
   "rho = -0.26, p = 0.0016 (n 142); within each state p = 0.33 and 0.16.",
   blocked_by="methods_underspecified"),
 o("fwhm-shorter-ptn", "blocked",
   SEL + " FWHM of PTN increases, flexion 87.7 and 50.3 ms (p = 0.060), extension 66.0 and 41.2 ms (p = 0.55).",
   blocked_by="methods_underspecified"),
 o("dsi-reduced", "blocked",
   SEL + " Reciprocal plus unidirectional 59.4% before and 52.6% after MPTP, chi-square p = 0.093.",
   blocked_by="methods_underspecified"),
 o("venus-dsi", "blocked",
   SEL + " Mean DSI M1 0.60 and 0.47, PTN 0.71 and 0.46, CSN 0.66 and 0.69.",
   blocked_by="methods_underspecified"),
 o("dsi-not-baseline", "blocked",
   SEL + " One-way ANOVA of baseline rate across the four categories F = 1.21, p = 0.31.",
   blocked_by="methods_underspecified"),
 o("velocity-matched-magnitude", "blocked",
   SEL + " Only 2 of 581 session-directions have a mean peak velocity of 130 to 200 deg/s, with one response "
   "in all (cell finding-kinematics-vs-paper), so the subset could not be formed under any detection.",
   blocked_by="methods_underspecified"),
 o("session-correlations", "blocked",
   SEL + " Session mean PTN latency against peak velocity rho = -0.17, p = 0.15 (70 sessions); against triceps "
   "longus 1 m2 rho = -0.38, p = 0.0076 (49 sessions).", blocked_by="methods_underspecified"),
 o("kinematics-slower", "not_reproduced",
   "Session means (154 and 153 pre, 137 and 137 post session-directions). After MPTP peak velocity is higher, "
   "+28.1% pooled and +29.7% for flexion (MPTP F = 98.5, p = 1.5e-21), and amplitude larger, +14.8% and +11.1% "
   "(F = 25.0, p = 7.5e-07). Restricted to command pulses of 60 to 250 units, the range both states share, "
   "the changes are +47.0% and +40.4%. Mean displacements are 2.4 to 3.8 degrees, where the paper gives a mean "
   "of 10. No file repeats another's trials, so none was left out.",
   measured=[28.1, 14.8],
   deviations=["Monkey V only, so the ANOVA has no animal factor (criterion).",
               "The FIR filter has 101 taps at 1 kHz, a standard choice; onset, peak velocity and amplitude "
               "windows are the claims file's."]),
 o("kinematic-latency-unchanged", "not_reproduced",
   "Movement onset latency is shorter after MPTP (pre 9.7 and 10.9 ms, post 3.0 and 6.0 ms for flexion and "
   "extension), MPTP F = 709, p < 1e-100; the MPTP by direction interaction is F = 16.1 (the paper's F > 94). "
   "At command pulses of 60 to 250 units the latency is also shorter (F = 239)."),
 o("emg-m2-larger", "reproduced",
   "m2 medians pre and post (a.u.) triceps lateralis 5.4 and 78.9 (KS p = 3.6e-15, 35 and 32 sessions), triceps "
   "longus 1 4.6 and 165.6 (p = 3e-46), triceps longus 2 10.3 and 301.1 (p = 7.5e-41); the same under the other "
   "channel rule. The torque pulses are about three times larger after MPTP, which this comparison cannot "
   "separate from the effect of MPTP.",
   deviations=["The claims file does not say whether a channel's baseline SD is that of the session-average "
               "trace or of the single-trial samples; both were run and give the same outcome."]),
 o("emg-duration-longer", "partially_reproduced",
   "Mean duration 22.2 ms before (181 channel-sessions) and 51.5 ms after MPTP (241), KS p = 5.2e-33; both far "
   "outside 57 +/- 6 and 79 +/- 3 ms. 23 channel-sessions before MPTP have no response. Under the other channel "
   "rule 21.3 and 50.0 ms.", measured=[22.2, 51.5],
   deviations=["Both readings of the channel rule were run (see emg-m2-larger); they give the same outcome."]),
 o("emg-onset-unchanged", "not_reproduced",
   "Onset of the EMG responses 44.2 ms before (median 36) and 25.0 ms after MPTP (median 25), KS p = 5.8e-22; "
   "under the other channel rule 41.2 and 24.2 ms, p = 7.1e-21.",
   deviations=["Both readings of the channel rule were run; they give the same outcome."]),
 o("emg-m1-weak", "partially_reproduced",
   "After MPTP m2 exceeds m1 in 237 of 241 channel-sessions (98.3%) and the median m1/m2 is 0.25; before MPTP the "
   "median ratio is 0.14 but m2 exceeds m1 in 151 of 204 (74.0%), just under 75%. Under the other channel rule "
   "74.3% and 0.11 before, 96.3% and 0.23 after, the same outcome.",
   deviations=["Both readings of the channel rule were run; they give the same outcome."]),
 o("trial-correlations", "blocked",
   "The Methods do not define a single-trial response latency, and the claim also uses the response selection "
   "blocked with false-positive-rate. Question for the authors, in findings.",
   output="claim:session-correlations", blocked_by="methods_underspecified"),
]

findings = [
 {"kind": "data_missing", "severity": "major", "notebook": NB, "output": "finding-leu-no-perturbations",
  "statement": "The monkey L (Leu) files mark no torque perturbation; all 5952 trials have "
  "torque_perturbation_type not_available. The torque command is NaN in every file before MPTP and, in the 34 "
  "after, a continuous trace without pulses, so the perturbations cannot be recovered. The paper's monkey L "
  "torque results (57 of 115 and 35 of 73 responsive cells), which enter its pooled values, cannot be tested. "
  "The dandiset description says so."},
 {"kind": "other", "about": "data", "severity": "major", "notebook": NB, "output": "finding-kinematics-vs-paper",
  "statement": "The torque-evoked elbow displacements in the files differ from the paper's. Their session mean "
  "amplitude is 2.4 to 3.8 degrees and 0.1% of perturbations reach 10 degrees, where the paper gives a mean of "
  "10 degrees; session mean peak velocities are 46 to 75 deg/s, and only 2 of 581 session-directions fall in the "
  "130 to 200 deg/s range the paper uses for its velocity-matched sessions. After MPTP the displacements are "
  "faster (+28%) and larger (+15%), where the paper reports them slower (-16.2%) and smaller (-6.6%)."},
 {"kind": "other", "about": "data", "severity": "minor", "notebook": NB, "output": "finding-torque-command-levels",
  "statement": "The torque command's pulse is about three times larger after MPTP than before (median 181.6 "
  "against 45.7 units; 125 of 137 post-MPTP sessions have a median pulse of 120 to 250 units, 3 of 151 before), "
  "where the paper describes one 0.1 Nm pulse throughout. The units have no conversion to newton-metres, so "
  "whether the applied torque changed cannot be told; the ElbowTorque description notes the varying levels. "
  "Comparisons of evoked movements and EMG before and after MPTP cannot separate the torque from the effect of "
  "MPTP."},
 {"kind": "other", "about": "data", "severity": "none", "notebook": NB, "output": "sanity",
  "statement": "Checks that passed. The monkey V counts of cells studied by MPTP state and projection type match "
  "the paper's supplementary table within 3 cells; is_post_mptp agrees with every file name; no unit name repeats "
  "across files and no trial spike train, angle or EMG window is shared between files. The torque command leaves "
  "rest 4 ms after the marked onset and the joint moves in the torque's direction, and spikes cross the "
  "response threshold in 0.67 of cell-directions after the onset against 0.23 after a pseudo onset, so the "
  "analog series and spikes are consistent with the trials table's clock."},
 {"kind": "methods_unavailable",
  "statement": "Question for the authors. The Methods detect responses by a millisecond-by-millisecond two-tailed "
  "t-test of the SDF against the baseline rate at p < 0.002, and state that this holds the false-positive rate "
  "near 0.01 over 200 ms. How was the test computed (which variance, over trials or over baseline time, and of "
  "single-trial or trial-averaged SDFs)? On these data, a threshold from the SD of the trial-averaged SDF's "
  "baseline crosses after a pseudo onset in 23% of cell-directions, a single-trial t-test in 47%, and a "
  "threshold from the SD of all single-trial baseline values in 1.3% but finds responses in only 20% of real "
  "cell-directions; none gives both the stated false-positive rate and the reported 62 to 75% of cells "
  "responding. All claims on the response selection are blocked until this is known."},
 {"kind": "methods_unavailable",
  "statement": "Question for the authors. The trial-by-trial correlations of PTN response latency with peak "
  "velocity and m2 need a single-trial response latency, which the Methods do not define (the response onset is "
  "defined on the trial-averaged SDF). How was it measured?"},
]

rec = {
 "schema_version": 3,
 "id": "pasquereau-2013-03",
 "datasets": [{"archive": "dandi", "id": "001636", "version": "0.261124.1906",
               "doi": "10.48324/dandi.001636/0.261124.1906", "relation": "primary"}],
 "paper": "doi:10.3389/fnsys.2013.00098",
 "date": "2026-11-26",
 "entry": "pasquereau-2013",
 "provenance": {"kind": "agent", "accountable": {"name": "CatalystNeuro"},
                "agent": {"harness": "Claude Code", "model": "claude-opus-5-5", "protocol": "pilot-19"},
                "runner": {"platform": "GitHub Actions",
                           "url": "https://github.com/encorescience/encore-registry/actions/runs/45857382971"}},
 "outcomes": outcomes,
 "findings": findings,
}
yaml.safe_dump(rec, open("attempts/pasquereau-2013-03.yaml", "w"),
               sort_keys=False, width=100, allow_unicode=True)
EOF
python make_record.py && grep -n '": \|: .*: ' attempts/pasquereau-2013-03.yaml | head; head -30 attempts/pasquereau-2013-03.yaml
```

```
schema_version: 3
id: pasquereau-2013-03
datasets:
- archive: dandi
  id: '001636'
  version: 0.261124.1906
  doi: 10.48324/dandi.001636/0.261124.1906
  relation: primary
paper: doi:10.3389/fnsys.2013.00098
date: '2026-11-26'
entry: pasquereau-2013
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-19
  runner:
[... 11 more lines not kept]
```

**Agent**

A few notes need correcting against the printed numbers (antidromic latency counts, p-value ranges, wording of the kinematic ranges). I'm also giving trial-correlations its own tagged cell.

**Agent calls Bash**

```bash
cd $TMPDIR/work; . ../env/bin/activate; python - <<'EOF'
p='make_record.py'; s=open(p).read()
rep=[("Two studied PTNs before and one after, and ten CSNs after MPTP, have no antidromic \"\n   \"latency in the files.",
      "Of the studied cells, 2 of 51 PTNs before and 6 of 54 after, and 10 of 48 CSNs after MPTP, have no \"\n   \"antidromic latency in the files."),
     ("is NaN in all 114 files before MPTP and, in the 34 after,", "is NaN in 114 files, and in the other 34, all after MPTP, it is"),
     ("The torque command is NaN in every file before MPTP and, in the 34 \"\n  \"after, a continuous trace without pulses,",
      "The torque command is NaN in 114 files and, in the other 34, all after \"\n  \"MPTP, a continuous trace without 50 ms pulses,"),
     ("Their session mean \"\n  \"amplitude is 2.4 to 3.8 degrees", "Averaged over sessions, the \"\n  \"amplitude is 2.4 to 3.8 degrees per state and direction"),
     ("session mean peak velocities are 46 to 75 deg/s,", "the peak velocity 46 to 75 deg/s,"),
     ("KS p 0.00013 to 0.047", "KS p 9.8e-05 to 0.047"),
     ("output=\"claim:session-correlations\", blocked_by=\"methods_underspecified\"),", "blocked_by=\"methods_underspecified\"),"),
]
for a,b in rep:
    assert a in s, a[:50]; s=s.replace(a,b)
open(p,'w').write(s)
p='make_nb.py'; s=open(p).read()
a='''**Result: blocked (methods underspecified).** The criterion needs a single-trial response latency,
which the Methods do not define; it also uses the response selection blocked above.
""")'''
b='''The Methods define a response's onset on the trial-averaged SDF only. The trials a single-trial
latency would be needed for:
""")

code("""
ptn_resp = resp[resp.ptype == PTN]
n_trials = sum(int(studied.loc[(studied.file == r.file) & (studied.unit == r.unit), f"n_{r.direction}"].iloc[0])
               for r in ptn_resp.itertuples())
print(f"PTN responses (claims file's detection): {len(ptn_resp)}, over {n_trials} perturbation trials")
""", tags=["claim:trial-correlations"])

md("""
**Result: blocked (methods underspecified).** The criterion needs a single-trial response latency,
which the Methods do not define; it also uses the response selection blocked above.
""")'''
assert a in s; s=s.replace(a,b)
s=s.replace("""The Leu files hold 138 and 72 units but no perturbation
times, and the torque command is NaN in every file before MPTP.""","""The Leu files hold 138 and 72 units but no perturbation
times, and the torque command is NaN in 114 of 148 files and without pulses in the rest.""")
open(p,'w').write(s)
EOF
grep -n "NaN in" make_nb.py | head; python make_record.py && python make_nb.py && python - <<'EOF'
import nbformat
nb=nbformat.read('entries/pasquereau-2013/reproduce_pasquereau_2013.ipynb',4)
for c in nb.cells:
    if c.cell_type=='code' and 'venus = pasq.load_all' in c.source:
        c.source="import pickle\nvenus=pickle.load(open('/tmp/claude-1001/work/venus.pkl','rb'))\nleu=pickle.load(open('/tmp/claude-1001/work/leu.pkl','rb'))"
nbformat.write(nb,'dev.ipynb')
EOF
export PYTHONPATH=entries/pasquereau-2013; python run_nb.py dev.ipynb dev_out.ipynb 2>&1 | grep -A3 "trial-corr\|Error"
```

```
341:times, and the torque command is NaN in 114 of 148 files and without pulses in the rest.
726:print("with NaN in a window:", int(emg.has_nan.sum()))
----- ['claim:trial-correlations'] 
 PTN responses (claims file's detection): 111, over 1301 perturbation trials
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/work; . ../env/bin/activate; python - <<'EOF'
p='make_nb.py'; s=open(p).read()
s=s.replace("torque command is NaN in 114 of 148 files and without pulses in the rest.","torque command is NaN in 114 of 148 files (the other 34, all after MPTP, hold a trace that\nthe file description says has no distinct pulses).")
s=s.replace("""Blocked: no Leu trial marks a perturbation (cell `finding-leu-no-perturbations`), and the torque
command is NaN or without pulses, so the perturbations cannot be found.""","""Blocked: no Leu trial marks a perturbation (cell `finding-leu-no-perturbations`), and the torque
command is NaN in most files.""")
open(p,'w').write(s)
p='make_record.py'; s=open(p).read()
s=s.replace("is NaN in 114 files, and in the other 34, all after MPTP, it is a smooth trace without 50 ms pulses, so the \"\n   \"perturbations cannot be recovered.",
 "is NaN in 114 files; the other 34, all after MPTP, hold a trace that the file description says has no \"\n   \"distinct pulses (looked at in one file while preparing, where it moves smoothly over hundreds of ms).")
s=s.replace("The torque command is NaN in 114 files and, in the other 34, all after \"\n  \"MPTP, a continuous trace without 50 ms pulses, so the perturbations cannot be recovered.",
 "The torque command is NaN in 114 files; the other 34, all after MPTP, hold \"\n  \"a trace that the file description says has no distinct pulses.")
open(p,'w').write(s)
EOF
grep -n "distinct pulses" make_record.py make_nb.py | cut -c1-150; python make_record.py; python make_nb.py
```

```
make_record.py:32:   "distinct pulses (looked at in one file while preparing, where it moves smoothly over hundreds of ms). The Leu files hold 138 and
make_record.py:161:  "a trace that the file description says has no distinct pulses. The paper's monkey L "
make_nb.py:342:the file description says has no distinct pulses).
Shell cwd was reset to
```

**Agent**

Re-running the entry from a clean environment.

**Agent calls Bash**

```bash
cd  date -u; python tools/entry.py all entries/pasquereau-2013 2>&1 | tail -5; python3 - <<'EOF'
import json
nb=json.load(open('executed/pasquereau-2013/reproduce_pasquereau_2013.ipynb'))
for c in nb['cells']:
    if c['cell_type']=='code':
        tags=c['metadata'].get('tags') or []
        out=''.join(''.join(o.get('text','')) if o['output_type']=='stream' else str(o.get('ename','')) for o in c['outputs'])
        if any(t in ('claim:trial-correlations','claim:emg-m1-weak','finding-leu-no-perturbations','claim:cell-counts') for t in tags) or 'Error' in out: print(tags, out[:800])
EOF
```

```
Thu Nov 26 16:51:56 UTC 2026
Installed kernelspec registry-pasquereau-2013 in executed/pasquereau-2013/.venv/share/jupyter/kernels/registry-pasquereau-2013
0 error(s)
pass  reproduce_pasquereau_2013.ipynb  (344 s)
['finding-leu-no-perturbations'] Leu trials by torque_perturbation_type: {'not_available': 5952}
Leu files whose torque command has any finite value: 34 of 148 ; of these after MPTP: 34

['claim:cell-counts'] M1: pre 115 (expected 112), post 157 (expected 159)
PTN: pre 51 (expected 49), post 54 (expected 54)
CSN: pre 32 (expected 31), post 48 (expected 48)
activated from both peduncle and putamen, all files: 3 {'Venus': 3} ; of these studied: 3
other types among the studied cells: {(False, 'no_response'): 29, (False, 'not_tested'): 1, (False, 'pyramidal_tract_and_corticostriatal_neuron'): 2, (True, 'no_response'): 50, (True, 'not_tested'): 1, (True, 'pyramidal_tract_and_corticostriatal_neuron'): 1, (True, 'pyramidal_tract_and_thalamic_neuron'): 1, (True, 'thalamic_projection_neuron'): 2}
Venus units left out for fewer than 5 perturbations in a direction: {False: 79, True: 5}

['claim:emg-m1-weak'] rule baseline_sd, pre: m2 > m1 in 151/204 (74.0%), median m1/m2 0.14
rule baseline_sd, post: m2 > m1 in 237/241 (98.3%), median m1/m2 0.25
rule raw_sd, pre: m2 > m1 in 205/276 (74.3%), median m1/m2 0.11
rule raw_sd, post: m2 > m1 in 263/273 (96.3%), median m1/m2 0.23

['claim:trial-correlations'] PTN responses (claims file's detection): 111, over 1301 perturbation trials
```

**Agent calls Bash**

```bash
cd  . $TMPDIR/env/bin/activate; uv pip install -q jsonschema pyyaml 2>/dev/null; python - <<'EOF'
import json, yaml, jsonschema
s=json.load(open('schemas/attempt.schema.json')); r=yaml.safe_load(open('attempts/pasquereau-2013-03.yaml'))
jsonschema.validate(r,s); print('valid', len(r['outcomes']))
c=yaml.safe_load(open('claims/pasquereau-2013.yaml')); ids=[x['id'] for x in c['claims']]
print(set(ids)^set(o['claim'] for o in r['outcomes']))
EOF
deactivate; python tools/entry.py check entries/pasquereau-2013 2>&1 | tail -3; python tools/entry.py handover entries/pasquereau-2013 2>&1 | tail -5; ls executed/pasquereau-2013/handover
```

```
valid 28
set()
0 error(s)
wrote executed/pasquereau-2013/handover
pasq.py
pasquereau-2013.yaml
reproduce_pasquereau_2013.ipynb
```

**Agent calls Bash**

```bash
cd  grep -c "Result:" executed/pasquereau-2013/handover/reproduce_pasquereau_2013.ipynb; grep -c "## Summary" executed/pasquereau-2013/handover/reproduce_pasquereau_2013.ipynb; ls tests | head -40; grep -n ": " attempts/pasquereau-2013-03.yaml | grep -v "^[0-9]*: *[-a-z_]*: \|^[0-9]*: *- [a-z_]*: " | head
```

```
0
0
conftest.py
test_build_osf_targets.py
test_build_site.py
test_build_targets.py
test_build_zenodo_targets.py
test_intake.py
test_notify.py
test_protocol_pin.py
test_publish_site.py
test_readme_row.py
test_replicates.py
test_reuse_targets.py
test_run_requests.py
test_runner.py
```

**Agent**

I've built and run the entry at `entries/pasquereau-2013`, written the record at `attempts/pasquereau-2013-03.yaml`, and built the handover. I did not verify my own work and committed nothing. The notebook says that version 0.261124.1906 was asked for; it is also the newest published version.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| cell-counts | reproduced (115/157 cells, 51/54 PTNs, 32/48 CSNs, 3 dual-projecting) |
| monkey-l-perturbations | blocked, data_missing |
| baseline-rate | reproduced (all 6 means in tolerance; PTN p = 0.020, CSN p = 0.65) |
| ptn-faster-than-csn | reproduced (p = 6.3e-12) |
| antidromic-latency | partially reproduced (means hold; CSN p = 0.019, above 0.05/3) |
| false-positive-rate | blocked, methods_underspecified (measured 0.23) |
| torque-related-fractions, prevalence-unchanged, ptn-more-responsive, one-direction-half, excitatory-majority, magnitude-unchanged, venus-response-magnitudes, latency-shorter, latency-not-training, fwhm-shorter-ptn, dsi-reduced, venus-dsi, dsi-not-baseline, velocity-matched-magnitude, session-correlations | blocked, methods_underspecified (they depend on false-positive-rate); results computed and shown, not deciding |
| kinematics-slower | not reproduced (+28% velocity, +15% amplitude after MPTP) |
| kinematic-latency-unchanged | not reproduced (F = 709) |
| emg-m2-larger | reproduced |
| emg-duration-longer | partially reproduced (22 and 52 ms against 57 and 79 ms) |
| emg-onset-unchanged | not reproduced (44 to 25 ms, p = 6e-22) |
| emg-m1-weak | partially reproduced (pre-MPTP 74.0%, just under the 75% asked) |
| trial-correlations | blocked, methods_underspecified |

## 2. Dataset, assumptions and questions

**What the dataset shows:**
- **Counts match.** Cell counts by MPTP state and projection type match the paper's monkey V table to within 3 cells.
- **No duplicates.** No recording is deposited twice (spike trains, angle and EMG windows compared across files), and every unit's MPTP flag agrees with its file name.
- **Clocks are consistent.** The torque command leaves rest 4 ms after the marked onset, and spikes cross the threshold far more often after the onset than after a pseudo onset.
- **Monkey L has no perturbations.** No Leu file marks one, and the torque command is NaN in 114 of 148 files. Finding rated major.
- **Kinematics differ from the paper.** Displacements are about 3 to 4 deg, where the paper gives 10 deg. After MPTP they are faster and larger, the reverse of the paper. Finding rated major.
- **Torque pulses are about 3 times larger after MPTP** (in arbitrary units), where the paper describes one fixed 0.1 Nm pulse. This confounds the before/after comparisons of movement and EMG. Finding rated minor, because the file description notes the varying levels.

**The detection problem.** The claims file's detection crosses its threshold in 23% of cell-directions after a pseudo onset, and in 20% of trials with no torque at all. The paper implies about 1%. I ran three other readings of the Methods' t-test (47%, 35%, 1.3%). The one that matches the paper's rate finds a response in only 20% of real cell-directions, against the paper's 62 to 75% of cells. No reading gives both, so the selection-based claims are blocked.

**Questions for the paper's authors** (recorded as methods_unavailable findings):
- How was the detection t-test computed?
- How was the single-trial response latency defined?

**Assumptions:** none adopted. The two readings of the EMG channel rule give the same outcomes.

**Questions to a reader:** none.

**Earlier attempts:** I came across none. The claims file's own header says its author had seen a data check and mentions "repeated files". That is from the claims file, not an earlier attempt's results; I found no repeated files in this version.

## 3. Protocol points

1. The rule to block a claim when its false-positive rate is far from the paper's does not say what happens to a claim that is itself the false-positive rate. I blocked false-positive-rate as methods_underspecified, recorded the measured value, and blocked its dependents through `depends_on`.
2. The protocol does not say whether a claim blocked through a dependency should still show its numbers. I computed and showed them all, marked as not deciding.
3. "Break down by session when there is one subject" does not fit 291 sessions. I broke key results down by MPTP state instead.
4. archives.md says to read NWB files with pynwb. I list one file with pynwb and read the other 438 directly with h5py, because building the pynwb objects for every file is too slow. The helper's docstring says so.

## 4. Runtime and failures

- The notebook runs in 344 s from a clean environment; `entry.py all` passes with 0 errors.
- The record validates against the schema and has one outcome for each of the 28 claims.
- Nothing failed. The run finished at about 17:00 UTC.

## End of run

54 turns, 37 minutes, $5.23 at API prices, result: success.
