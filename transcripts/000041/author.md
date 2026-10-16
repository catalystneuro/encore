# 000041 · author · run 38839151188

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; echo ======; cat README.md; echo =====; cat docs/design.md; ls; ls entries claims attempts tools
```

```
<persisted-output>
Output too large (41.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/c6e465f9-3bcb-41d0-8e31-80cf12f4e240/tool-results/bqhrxly57.txt

Preview (first 2KB):
# Protocol for an attempt

Version: `pilot-7`. Record this version in the attempt's provenance.

This is what an agent, or a person, does to attempt a target and deposit the
result. It is written from the eight pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

There are two roles. The **author** makes the attempt. The **verifier** checks
it and must not be the author: for agents, a separate run with a separate
context that has not seen the author's reasoning.

Agent runs are made with the [Agent run](../.github/workflows/attempt.yml)
workflow, one role at a time: `author`, `verifier-1`, `author-revise-1`,
`verifier-2`, `author-revise-2`, and, when the last of these proposes changes
of outcome, `verifier-3` and `author-revise-3`. Each run's transcript and final report are
[... 25 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/c6e465f9-3bcb-41d0-8e31-80cf12f4e240/tool-results/bqhrxly57.txt"
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-7`. Record this version in the attempt's provenance.
4	
5	This is what an agent, or a person, does to attempt a target and deposit the
6	result. It is written from the eight pilot attempts
7	([pilot notes](pilot-notes.md)); the reasons for the rules are there.
8	
9	There are two roles. The **author** makes the attempt. The **verifier** checks
10	it and must not be the author: for agents, a separate run with a separate
11	context that has not seen the author's reasoning.
12	
13	Agent runs are made with the [Agent run](../.github/workflows/attempt.yml)
14	workflow, one role at a time: `author`, `verifier-1`, `author-revise-1`,
15	`verifier-2`, `author-revise-2`, and, when the last of these proposes changes
16	of outcome, `verifier-3` and `author-revise-3`. Each run's transcript and final report are
17	kept in [`transcripts/<dandiset>/`](../transcripts).
18	
19	## Author
20	
[... 814 more lines not kept]
```

**Agent**

Now the example entry.

**Agent calls Bash**

```bash
ls -la entries/001453-fouke-2025/ claims/001453/; cat entries/001453-fouke-2025/entry.yaml entries/001453-fouke-2025/requirements.in; cat entries/001453-fouke-2025/README.md 2>/dev/null; cat claims/001453/*.yaml
```

```
claims/001453/:
total 24
drwxr-xr-x  2 runner runner  4096 Oct 16 02:11 .
drwxr-xr-x 19 runner runner  4096 Oct 16 02:11 ..
-rw-r--r--  1 runner runner 12471 Oct 16 02:11 10.1016-j.cub.2025.04.027.yaml

entries/001453-fouke-2025/:
total 124
drwxr-xr-x  2 runner runner  4096 Oct 16 02:11 .
drwxr-xr-x 19 runner runner  4096 Oct 16 02:11 ..
-rw-r--r--  1 runner runner  2158 Oct 16 02:11 README.md
-rw-r--r--  1 runner runner   914 Oct 16 02:11 entry.yaml
-rw-r--r--  1 runner runner 16218 Oct 16 02:11 omr.py
-rw-r--r--  1 runner runner 79403 Oct 16 02:11 reproduce_fouke_2025.ipynb
-rw-r--r--  1 runner runner    61 Oct 16 02:11 requirements.in
-rw-r--r--  1 runner runner  5989 Oct 16 02:11 requirements.lock.txt
schema_version: 1
name: 001453-fouke-2025
type: reproduction
title: Optomotor swimming of zebrafish and Danionella cerebrum (Fouke et al. 2025)
[... 268 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/001453-fouke-2025-01.yaml | head -150; ls schemas;
```

```
schema_version: 1
id: 001453-fouke-2025-01
dandiset: "001453"
dandiset_version: 0.250518.1950
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
inputs:
- what: Names of the stimulus codes (the conversion of stimulus names to codes, its printed list of
    codes, and its own labels for codes 9 to 13), the trial processing parameters, the spatial
    scale of 10 pixels per mm, the per-stimulus medians it printed, used as reference values
    for the link claim, and the DC pairs its printed Tukey test for Figure 1D finds significant,
[... 133 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 150,400p attempts/001453-fouke-2025-01.yaml; cat schemas/attempt.schema.json | head -300
```

```
gives ZF higher with p below 0.05/9 for 7 of 9 stimuli; it divides the heading change per
    frame by the file's mean frame interval, which in DC files is a median 8.73 times the frame
    interval (ZF 1.37), as DC files hold only trial frames. Part of the DC values may be tracking
    noise. In the 3 s stationary phase the DC median is 205 deg/s2, higher than the 171 during
    motion (per fish median ratio 1.24, p = 0.016), but ZF are also higher at rest (66.9 and 60.8,
    ratio 1.07, p = 0.00012), so this does not separate the species. In frames where the fish is
    still (below 1 mm/s) DC are higher than ZF (per-fish medians 72.4 and 34.9 deg/s2, Mann-Whitney
    p = 0.00014), and DC are higher in every speed band (at 5 mm/s or more, 207 and 85.8). The
    outputs cannot say whether the higher values in moving DC are noise or turning during
    continuous swimming. With the heading from the unwrapped `f0_theta` DC are higher still (218
    to 278 against ZF 61.8 to 77.3 deg/s2, 0 of 9). The reversal should not be read as evidence
    against the paper.
  deviations:
  - Follows the Methods' definition (degrees per second squared) on heading resampled to 30 Hz;
    the code's quantity, which disagrees with the Methods, is shown as a variant.
  - Heading is taken from the cumulative sum of `f0_vtheta`, as the code does; in DC files it does
    not match `f0_theta`.
- claim: figs1e-dc-respond-less-monocular
  outcome: reproduced
  notebook: reproduce_fouke_2025.ipynb
[... 531 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/000041/ | python -m json.tool | head -40; curl -s https://api.dandiarchive.org/api/dandisets/000041/versions/ | python -m json.tool | head -60
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
for v in 0.210812.1515 0.250624.0419; do echo "== $v"; curl -s "https://api.dandiarchive.org/api/dandisets/000041/versions/$v/assets/?page_size=100" | python -c "
import json,sys; d=json.load(sys.stdin)
for a in d['results']: print(a['asset_id'], a['path'], a['size'], a.get('modified'))"; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000041/versions/0.250624.0419/ | python -m json.tool > $TMPDIR/meta.json; cat $TMPDIR/meta.json | head -200; diff <(curl -s https://api.dandiarchive.org/api/dandisets/000041/versions/0.210812.1515/ | python -m json.tool) $TMPDIR/meta.json
```

Result: the fetched text is not kept.

**Agent**

Pinning 0.250624.0419 (assets identical to 0.210812.1515). Now the paper.

**Agent calls Bash**

```bash
curl -s "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/j.neuron.2016.03.036&format=json&resultType=core" | python -c "
import json,sys; d=json.load(sys.stdin)
for r in d['resultList']['result']: print(r.get('pmid'), r.get('pmcid'), r.get('isOpenAccess'), r.get('inEPMC'), r.get('hasPDF'), r.get('license'), r.get('title'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
mkdir -p paper; curl -s -o paper/PMC4873379.xml "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4873379/fullTextXML"; ls -la paper; head -c 600 paper/PMC4873379.xml
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s -L -A "Mozilla/5.0" -o paper/PMC4873379.html "https://pmc.ncbi.nlm.nih.gov/articles/PMC4873379/"; ls -la paper; grep -o "<title>[^<]*" paper/PMC4873379.html
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
rm paper/*; curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=4873379&rettype=xml" -o paper/PMC4873379.xml; ls -la paper; python -c "
import re;t=open('paper/PMC4873379.xml').read();print(len(t));print(re.sub('<[^>]+>','',t)[:1500])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
python - <<'EOF'
import re
t=open('paper/PMC4873379.xml').read()
t=re.sub(r'<(title)>',r'\n\n## ',t)
t=re.sub(r'</p>|</title>|</caption>','\n',t)
t=re.sub(r'<fig ','\n[FIG] <fig ',t)
t=re.sub(r'<[^>]+>','',t)
t=re.sub(r'\n{3,}','\n\n',t)
open('paper/watson2016.txt','w').write(t)
print(len(t.split()))
EOF
wc -l paper/watson2016.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/watson2016.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/watson2016.txt",
 "offset": 86
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Got the full text (NIH author manuscript, PMC4873379). Now inspecting an NWB file by streaming.

**Agent calls Bash**

```bash
grep -o '<supplementary-material[^>]*>.\{0,300\}' paper/PMC4873379.xml | head; grep -o 'xlink:href="[^"]*"' paper/PMC4873379.xml | sort -u | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; curl -s "https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id=PMC4873379"; echo; for f in NIHMS776601-supplement-1.pdf NIHMS776601-supplement-2.pdf; do curl -s -L -A "Mozilla/5.0" -o $f "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4873379/bin/$f"; file $f; done; curl -s -L -A "Mozilla/5.0" -o s1b.pdf "https://europepmc.org/articles/PMC4873379/bin/NIHMS776601-supplement-1.pdf"; file s1b.pdf
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; rm -f *.pdf; curl -s -L -o supp.zip "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4873379/supplementaryFiles"; file supp.zip; ls -la
```

Result: the fetched text is not kept.

**Agent**

Supplement PDFs are behind a captcha; I'll work from the main text and record that. Setting up a scratch environment to inspect the files.

**Agent calls Bash**

```bash
cd  rm paper/supp.zip; ls -la paper/.claude; uv venv -q $TMPDIR/venv && VIRTUAL_ENV=$TMPDIR/venv uv pip install -q pynwb h5py remfile dandi numpy scipy pandas matplotlib 2>&1 | tail -3; $TMPDIR/venv/bin/python -c "import pynwb, h5py; print(pynwb.__version__, h5py.__version__)"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat > $TMPDIR/inspect.py <<'EOF'
import h5py, remfile, sys
from dandi.dandiapi import DandiAPIClient
path=sys.argv[1]
with DandiAPIClient() as c:
    a=c.get_dandiset("000041","0.250624.0419").get_asset_by_path(path)
    url=a.get_content_url(follow_redirects=1, strip_query=True)
f=h5py.File(remfile.File(url),'r')
def show(name,obj):
    if isinstance(obj,h5py.Dataset):
        print(name, obj.shape, obj.dtype, dict((k,(v if not hasattr(v,'shape') or v.size<5 else '...')) for k,v in obj.attrs.items() if k not in ('namespace','object_id')))
    else:
        print(name+'/', {k:v for k,v in obj.attrs.items() if k not in ('namespace','object_id')})
f.visititems(show)
EOF
$TMPDIR/venv/bin/python $TMPDIR/inspect.py sub-BWRat17/sub-BWRat17_ses-BWRat17-121912_ecephys.nwb 2>&1 | head -300
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/inspect.py", line 1, in <module>
    import h5py, remfile, sys
  File "/tmp/claude-1001/venv/lib/python3.13/site-packages/h5py/__init__.py", line 33, in <module>
    from . import version
  File "/tmp/claude-1001/venv/lib/python3.13/site-packages/h5py/version.py", line 17, in <module>
    import numpy
  File "/tmp/claude-1001/venv/lib/python3.13/site-packages/numpy/__init__.py", line 109, in <module>
    from numpy.__config__ import show_config
  File "/tmp/claude-1001/venv/lib/python3.13/site-packages/numpy/__config__.py", line 4, in <module>
    from numpy._core._multiarray_umath import (
    ...<3 lines>...
    )
  File "/tmp/claude-1001/venv/lib/python3.13/site-packages/numpy/_core/__init__.py", line 24, in <module>
    from . import multiarray
  File "/tmp/claude-1001/venv/lib/python3.13/site-packages/numpy/_core/multiarray.py", line 11, in <module>
    from . import _multiarray_umath, overrides
  File "/tmp/claude-1001/venv/lib/python3.13/site-packages/numpy/_core/overrides.py", line 4, in <module>
    import inspect
  File "/tmp/claude-1001/inspect.py", line 1, in <module>
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/w; mv $TMPDIR/inspect.py $TMPDIR/w/h5list.py; $TMPDIR/venv/bin/python $TMPDIR/w/h5list.py sub-BWRat17/sub-BWRat17_ses-BWRat17-121912_ecephys.nwb 2>&1 | head -300
```

```
acquisition/ {}
analysis/ {}
file_create_date (1,) object {}
general/ {}
general/devices/ {}
general/devices/implant/ {'description': 'silicon probe electrodes; see BWRat17_121912.xml or BWRat17_121912.sessionInfo.mat for more information', 'neurodata_type': 'Device'}
general/experimenter (1,) object {}
general/extracellular_ephys/ {}
general/extracellular_ephys/electrodes/ {'colnames': array(['x', 'y', 'z', 'imp', 'location', 'filtering', 'group',
       'group_name', 'shank_electrode_number', 'up_reference',
       'spindle_reference', 'theta_reference', 'rel_x', 'rel_y'],
      dtype=object), 'description': 'metadata about extracellular electrodes', 'neurodata_type': 'DynamicTable'}
general/extracellular_ephys/electrodes/filtering (68,) object {'description': 'description of hardware filtering', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/group (68,) object {'description': 'a reference to the ElectrodeGroup this electrode is a part of', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/group_name (68,) object {'description': 'the name of the ElectrodeGroup this electrode is a part of', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/id (68,) int32 {'neurodata_type': 'ElementIdentifiers'}
general/extracellular_ephys/electrodes/imp (68,) float64 {'description': 'the impedance of the channel', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/location (68,) object {'description': 'the location of channel within the subject e.g. brain region', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/rel_x (68,) float64 {'description': 'the x coordinate within the electrode group', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/rel_y (68,) float64 {'description': 'the y coordinate within the electrode group', 'neurodata_type': 'VectorData'}
[... 137 more lines not kept]
```

**Agent**

The files hold units (spike times, cell type, global id), a sleep-state interval table, 1250 Hz LFP and waveforms. Surveying all 22 files now.

**Agent calls Bash**

```bash
cat > $TMPDIR/w/survey.py <<'EOF'
import h5py, remfile, numpy as np, json, collections
from dandi.dandiapi import DandiAPIClient
out={}
with DandiAPIClient() as c:
    ds=c.get_dandiset("000041","0.250624.0419")
    assets=sorted(ds.get_assets(), key=lambda a:a.path)
    for a in assets:
        url=a.get_content_url(follow_redirects=1, strip_query=True)
        f=h5py.File(remfile.File(url),'r')
        r={}
        for k in ['session_description','identifier','session_start_time','timestamps_reference_time','general/session_id','general/institution','general/lab','general/subject/age','general/subject/genotype','general/subject/species','general/subject/subject_id','general/subject/weight']:
            v=f[k][()]; r[k]=v.decode() if isinstance(v,bytes) else str(v)
        r['related']=[x.decode() if isinstance(x,bytes) else x for x in f['general/related_publications'][()]]
        st=f['processing/behavior/states']
        lab=[x.decode() if isinstance(x,bytes) else x for x in st['label'][()]]
        s=st['start_time'][()]; e=st['stop_time'][()]
        r['states']={L:[int(sum(1 for x in lab if x==L)), float(sum(e[i]-s[i] for i in range(len(lab)) if lab[i]==L))] for L in set(lab)}
        r['states_range']=[float(s.min()),float(e.max())]
        r['states_sorted']=bool(np.all(np.diff(s)>=0)); r['overlap']=int(np.sum(s[1:]<e[:-1]-1e-6))
        r['gaps']=float(np.sum(np.clip(s[1:]-e[:-1],0,None)))
        u=f['units']
        ct=[x.decode() if isinstance(x,bytes) else x for x in u['cell_type'][()]]
        rg=[x.decode() if isinstance(x,bytes) else x for x in u['region'][()]]
        r['cell_type']=dict(collections.Counter(ct)); r['region']=dict(collections.Counter(rg))
        r['n_units']=len(ct)
        r['global_id_range']=[int(u['global_id'][()].min()), int(u['global_id'][()].max())]
        stimes=u['spike_times'][()]; idx=u['spike_times_index'][()]
        r['n_spikes']=len(stimes); r['spk_range']=[float(stimes.min()),float(stimes.max())]
        b=np.concatenate([[0],idx]); r['unsorted_units']=int(sum(np.any(np.diff(stimes[b[i]:b[i+1]])<0) for i in range(len(idx))))
        lfp=f['processing/ecephys/LFP/lfp']
        r['lfp_shape']=list(lfp['data'].shape); r['lfp_rate']=float(lfp['starting_time'].attrs['rate']); r['lfp_start']=float(lfp['starting_time'][()])
        r['lfp_dur']=lfp['data'].shape[0]/r['lfp_rate']
        r['lfp_conv']=str(lfp['data'].attrs['conversion'])
        el=f['general/extracellular_ephys/electrodes']
        r['el_loc']=dict(collections.Counter([x.decode() if isinstance(x,bytes) else x for x in el['location'][()]]))
        r['n_el']=len(el['id'][()])
        for k in ['up_reference','spindle_reference','theta_reference']: r[k]=[int(i) for i in np.where(el[k][()])[0]]
        r['acq']=list(f['acquisition'].keys()); r['proc']={k:list(f['processing'][k].keys()) for k in f['processing']}
        r['intervals']=list(f['intervals'].keys()) if 'intervals' in f else []
        out[a.path]=r
        print(a.path, r['general/subject/subject_id'], r['n_units'], r['cell_type'], r['states'], round(r['lfp_dur']), r['spk_range'], r['states_range'], flush=True)
json.dump(out, open('/tmp/claude-1001/w/survey.json','w'), indent=1, default=str)
EOF
time $TMPDIR/venv/bin/python $TMPDIR/w/survey.py
```

```
Exit code 1
sub-BWRat17/sub-BWRat17_ses-BWRat17-121712_ecephys.nwb BWRat17 50 {'excitatory': 44, 'inhibitory': 6} {'Non-REM': [13, 1453.0], 'REM': [3, 108.0], 'Awake': [17, 4456.0]} 6059 [0.04275, 6059.355] [5.0, 6054.0]
sub-BWRat17/sub-BWRat17_ses-BWRat17-121912_ecephys.nwb BWRat17 29 {'excitatory': 29} {'Non-REM': [31, 3665.0], 'REM': [5, 216.0], 'Awake': [35, 2573.0]} 6535 [0.0196, 6534.6878] [5.0, 6529.0]
sub-BWRat18/sub-BWRat18_ses-BWRat18-020513_ecephys.nwb BWRat18 40 {'excitatory': 35, 'inhibitory': 5} {'Non-REM': [19, 4390.0], 'REM': [13, 533.0], 'Awake': [21, 2606.0]} 7591 [0.03305, 7590.45115] [5.0, 7586.0]
sub-BWRat19/sub-BWRat19_ses-BWRat19-032413_ecephys.nwb BWRat19 49 {'excitatory': 37, 'inhibitory': 12} {'Non-REM': [16, 2143.0], 'REM': [1, 12.0], 'Awake': [17, 2815.0]} 5013 [0.007, 5013.39155] [5.0, 5008.0]
sub-BWRat19/sub-BWRat19_ses-BWRat19-032513_ecephys.nwb BWRat19 59 {'excitatory': 50, 'inhibitory': 9} {'Non-REM': [18, 2223.0], 'REM': [5, 289.0], 'Awake': [19, 1365.0]} 3929 [0.00995, 3928.79205] [5.0, 3923.0]
sub-BWRat20/sub-BWRat20_ses-BWRat20-101013_ecephys.nwb BWRat20 18 {'inhibitory': 5, 'excitatory': 13} {'Non-REM': [26, 4167.0], 'REM': [10, 768.0], 'Awake': [26, 8358.0]} 13364 [0.0032, 13364.28915] [5.0, 13359.0]
sub-BWRat20/sub-BWRat20_ses-BWRat20-101513_ecephys.nwb BWRat20 61 {'excitatory': 58, 'inhibitory': 3} {'Non-REM': [107, 12105.0], 'REM': [58, 2310.0], 'Awake': [133, 8290.0]} 23012 [0.00525, 23011.9931] [5.0, 23007.0]
Traceback (most recent call last):
  File "/tmp/claude-1001/w/survey.py", line 37, in <module>
    for k in ['up_reference','spindle_reference','theta_reference']: r[k]=[int(i) for i in np.where(el[k][()])[0]]
                                                                                                    ~~^^^
  File "/tmp/claude-1001/venv/lib/python3.13/site-packages/h5py/_hl/group.py", line 407, in __getitem__
    return self._get(name)
           ~~~~~~~~~^^^^^^
  File "h5py/_objects.pyx", line 54, in h5py._obj
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/w; sed -i "s/for k in \['up_reference','spindle_reference','theta_reference'\]: r\[k\]=/for k in ['up_reference','spindle_reference','theta_reference']: r[k]=None if k not in el else /" survey.py; sed -i "s/r\['n_el'\]=len(el\['id'\]\[()\])/r['n_el']=len(el['id'][()]); r['el_cols']=list(el.attrs['colnames'])/" survey.py; time $TMPDIR/venv/bin/python survey.py
```

```
sub-BWRat17/sub-BWRat17_ses-BWRat17-121712_ecephys.nwb BWRat17 50 {'excitatory': 44, 'inhibitory': 6} {'Non-REM': [13, 1453.0], 'Awake': [17, 4456.0], 'REM': [3, 108.0]} 6059 [0.04275, 6059.355] [5.0, 6054.0]
sub-BWRat17/sub-BWRat17_ses-BWRat17-121912_ecephys.nwb BWRat17 29 {'excitatory': 29} {'Non-REM': [31, 3665.0], 'Awake': [35, 2573.0], 'REM': [5, 216.0]} 6535 [0.0196, 6534.6878] [5.0, 6529.0]
sub-BWRat18/sub-BWRat18_ses-BWRat18-020513_ecephys.nwb BWRat18 40 {'excitatory': 35, 'inhibitory': 5} {'Non-REM': [19, 4390.0], 'Awake': [21, 2606.0], 'REM': [13, 533.0]} 7591 [0.03305, 7590.45115] [5.0, 7586.0]
sub-BWRat19/sub-BWRat19_ses-BWRat19-032413_ecephys.nwb BWRat19 49 {'excitatory': 37, 'inhibitory': 12} {'Non-REM': [16, 2143.0], 'Awake': [17, 2815.0], 'REM': [1, 12.0]} 5013 [0.007, 5013.39155] [5.0, 5008.0]
sub-BWRat19/sub-BWRat19_ses-BWRat19-032513_ecephys.nwb BWRat19 59 {'excitatory': 50, 'inhibitory': 9} {'Non-REM': [18, 2223.0], 'Awake': [19, 1365.0], 'REM': [5, 289.0]} 3929 [0.00995, 3928.79205] [5.0, 3923.0]
sub-BWRat20/sub-BWRat20_ses-BWRat20-101013_ecephys.nwb BWRat20 18 {'inhibitory': 5, 'excitatory': 13} {'Non-REM': [26, 4167.0], 'Awake': [26, 8358.0], 'REM': [10, 768.0]} 13364 [0.0032, 13364.28915] [5.0, 13359.0]
sub-BWRat20/sub-BWRat20_ses-BWRat20-101513_ecephys.nwb BWRat20 61 {'excitatory': 58, 'inhibitory': 3} {'Non-REM': [107, 12105.0], 'Awake': [133, 8290.0], 'REM': [58, 2310.0]} 23012 [0.00525, 23011.9931] [5.0, 23007.0]
sub-BWRat21/sub-BWRat21_ses-BWRat21-121113_ecephys.nwb BWRat21 32 {'excitatory': 28, 'inhibitory': 4} {'Non-REM': [67, 10257.0], 'Awake': [89, 7559.0], 'REM': [57, 3845.0]} 21883 [0.0011, 21883.1913] [5.0, 21878.0]
sub-BWRat21/sub-BWRat21_ses-BWRat21-121613_ecephys.nwb BWRat21 44 {'excitatory': 20, 'inhibitory': 1, 'unknown': 23} {'Non-REM': [59, 9142.0], 'Awake': [79, 9113.0], 'REM': [45, 3095.0]} 21542 [0.126, 21541.61065] [5.0, 21537.0]
sub-BWRat21/sub-BWRat21_ses-BWRat21-121813_ecephys.nwb BWRat21 12 {'excitatory': 11, 'inhib
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/w; $TMPDIR/venv/bin/python - <<'EOF'
import json,collections
d=json.load(open('survey.json'))
tot=collections.Counter()
for p,r in d.items():
    tot.update(r['cell_type'])
print(tot, sum(tot.values()))
k0=list(d)[0]; r=d[k0]
for k,v in r.items():
    if k not in ('states',): print(k, v)
print()
for p,r in d.items():
    print(p.split('/')[1][:-13], r['general/subject/age'], r['general/subject/weight'], r['session_start_time'], r['region'], r['el_loc'], r['n_el'], r['lfp_shape'], r['lfp_conv'], r['unsorted_units'], r['overlap'], round(r['gaps']), r['global_id_range'], r['up_reference'], r['spindle_reference'], r['theta_reference'], r['acq'], r['intervals'], r['el_cols'] if r['el_cols']!=d[k0]['el_cols'] else '')
EOF
```

```
Counter({'excitatory': 826, 'inhibitory': 96, 'unknown': 23}) 945
session_description Data was recorded using silicon probe electrodes in the frontal cortices of male Long Evans rats between 4-7 months of age. The design was to have no specific behavior, task or stimulus, rather the animal was left alone in it’s home cage (which it lives in at all times).
identifier BWRat17_121712
session_start_time 2012-12-17T00:00:00-05:00
timestamps_reference_time 2012-12-17T00:00:00-05:00
general/session_id BWRat17_121712
general/institution NYU
general/lab Buzsaki
general/subject/age 3-7 months
general/subject/genotype Wild type
general/subject/species Rattus norvegicus domestica - Long Evans
general/subject/subject_id BWRat17
general/subject/weight 250-500g
related ['Network Homeostasis and State Dynamics of Neocortical SleepWatson BO, Levenstein D, Greene JP, Gelinas JN, Buzsáki G.Neuron. 2016 Apr 27. pii: S0896-6273(16)30056-3.doi: 10.1016/j.neuron.2016.03.036']
states_range [5.0, 6054.0]
states_sorted True
overlap 0
gaps 32.0
cell_type {'excitatory': 44, 'inhibitory': 6}
region {'CTX': 50}
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s "https://api.github.com/search/code?q=watson+repo:catalystneuro/buzsaki-lab-to-nwb" | head -5; curl -s https://api.github.com/repos/catalystneuro/buzsaki-lab-to-nwb | python -c "import json,sys;d=json.load(sys.stdin);print(d.get('full_name'),d.get('default_branch'),d.get('pushed_at'))"; curl -s "https://api.github.com/repos/catalystneuro/buzsaki-lab-to-nwb/git/trees/HEAD?recursive=1" | python -c "
import json,sys;d=json.load(sys.stdin)
for t in d.get('tree',[]):
  if 'watson' in t['path'].lower(): print(t['path'])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/w; SHA=$(curl -s https://api.github.com/repos/catalystneuro/buzsaki-lab-to-nwb/commits/master | python -c "import json,sys;print(json.load(sys.stdin)['sha'])"); echo $SHA; for f in convert_watson.py watsonbehaviordatainterface.py watsonsortinginterface.py watsonlfpdatainterface.py; do echo "=== $f"; curl -s https://raw.githubusercontent.com/catalystneuro/buzsaki-lab-to-nwb/$SHA/buzsaki_lab_to_nwb/watson/$f; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/w; cat > chk.py <<'EOF'
import h5py, remfile, numpy as np
from dandi.dandiapi import DandiAPIClient
with DandiAPIClient() as c:
    ds=c.get_dandiset("000041","0.250624.0419")
    def op(p):
        return h5py.File(remfile.File(ds.get_asset_by_path(p).get_content_url(follow_redirects=1, strip_query=True)),'r')
    for p in ['sub-BWRat17/sub-BWRat17_ses-BWRat17-121912_ecephys.nwb','sub-Dino/sub-Dino_ses-Dino-072114_ecephys.nwb']:
        f=op(p); d=f['processing/ecephys/LFP/lfp/data']
        print(p, d.chunks, d.compression, f['processing/ecephys/SpindleDecompositionSeries/data'].chunks)
        u=f['units']; st=u['spike_times'][()]; idx=u['spike_times_index'][()]
        print('nspk', len(st), 'max', st.max(), 'max*20000', st.max()*20000, 'min diff', np.min(np.diff(np.sort(st))))
        wt=f['processing/ecephys/SpikeWaveforms1/timestamps'][()]; print('waveform ts range', wt.min(), wt.max(), len(wt))
        s=f['processing/behavior/states']; lab=s['label'][()]; a=s['start_time'][()]; b=s['stop_time'][()]
        for i in range(min(40,len(lab))): print(lab[i].decode() if isinstance(lab[i],bytes) else lab[i], a[i], b[i], b[i]-a[i])
EOF
$TMPDIR/venv/bin/python chk.py
```

```
sub-BWRat17/sub-BWRat17_ses-BWRat17-121912_ecephys.nwb (63816, 1) gzip None
nspk 113783 max 6534.6878 max*20000 130693756.0 min diff 0.0
waveform ts range 0.03505 6534.69995 33804
Awake 5.0 613.0 608.0
Non-REM 614.0 630.0 16.0
Awake 631.0 1191.0 560.0
Non-REM 1192.0 1308.0 116.0
Awake 1309.0 1318.0 9.0
Non-REM 1319.0 1402.0 83.0
Awake 1403.0 1452.0 49.0
Non-REM 1453.0 1493.0 40.0
Awake 1494.0 1530.0 36.0
Non-REM 1531.0 1575.0 44.0
Awake 1576.0 1613.0 37.0
Non-REM 1614.0 1665.0 51.0
Awake 1666.0 1680.0 14.0
Non-REM 1681.0 1816.0 135.0
Awake 1817.0 1857.0 40.0
Non-REM 1858.0 1881.0 23.0
Awake 1882.0 1927.0 45.0
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/w; cat > chk2.py <<'EOF'
import h5py, remfile, numpy as np
from dandi.dandiapi import DandiAPIClient
with DandiAPIClient() as c:
    ds=c.get_dandiset("000041","0.250624.0419")
    f=h5py.File(remfile.File(ds.get_asset_by_path('sub-Dino/sub-Dino_ses-Dino-072114_ecephys.nwb').get_content_url(follow_redirects=1, strip_query=True)),'r')
    u=f['units']; st=u['spike_times'][()]; idx=u['spike_times_index'][()]
    x=st*20000
    print('frac nonint', np.mean(np.abs(x-np.round(x))>1e-3), 'unique', len(np.unique(st)), len(st))
    print(np.unique(np.round(x))[:20], np.round(x).max())
    print(np.histogram(x, bins=20)[0])
    print(u['cell_type'][()], u['global_id'][()])
    print(f['units'].attrs['colnames'])
EOF
$TMPDIR/venv/bin/python chk2.py
```

```
frac nonint 0.0 unique 8451 215233
[ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12. 13. 14. 15. 16. 17.
 18. 19.] 8504.0
[11749 11354 11006 11149 10085  7469 15110 15136 10633 10449  9762 12444
 13786 11028 12360  9608  8374  9425 11592  2714]
[b'excitatory' b'excitatory' b'excitatory' b'excitatory' b'excitatory'
 b'excitatory' b'excitatory' b'excitatory' b'excitatory' b'excitatory'
 b'excitatory' b'excitatory' b'inhibitory' b'inhibitory' b'excitatory'
 b'excitatory' b'inhibitory' b'inhibitory' b'inhibitory' b'inhibitory'
 b'inhibitory'] [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21]
['shank_id' 'global_id' 'region' 'electrode_group' 'cell_type'
 'spike_times']
Shell cwd was reset to
```

**Agent calls Bash**

```bash
python - <<'EOF'
import re
t=open('paper/PMC4873379.xml').read()
for m in re.finditer(r'<table-wrap.*?</table-wrap>', t, re.S):
    s=m.group(0); s=re.sub(r'</t[dh]>',' | ',s); s=re.sub(r'</tr>','\n',s); print(re.sub(r'<[^>]+>','',s))
EOF
```

Result: not kept, because it reads the paper's text.

**Agent**

No Table 1 in the manuscript. Timing a one-channel LFP read on the longest session to decide whether LFP-based claims are feasible.

**Agent calls Bash**

```bash
cd $TMPDIR/w; cat > lfpt.py <<'EOF'
import h5py, remfile, numpy as np, time
from dandi.dandiapi import DandiAPIClient
with DandiAPIClient() as c:
    ds=c.get_dandiset("000041","0.250624.0419")
    url=ds.get_asset_by_path('sub-Rizzo/sub-Rizzo_ses-Rizzo-022615_ecephys.nwb').get_content_url(follow_redirects=1, strip_query=True)
t=time.time()
f=h5py.File(remfile.File(url, verbose=False),'r')
d=f['processing/ecephys/LFP/lfp/data']
x=d[:5_000_000,17]
print(time.time()-t, x.dtype, x[:10], np.percentile(x,[1,50,99]))
EOF
$TMPDIR/venv/bin/python lfpt.py
```

```
8.771227836608887 int16 [  43   37   41   13 -102 -120 -117  -47    4   85] [-3241.  -146.  2402.]
Shell cwd was reset to
```

**Agent**

About 9 s per 5M samples, so one channel for all sessions would take roughly 14 min serially. Before deciding on LFP claims, one more try at the supplement, which holds the detection methods.

**Agent calls Bash**

```bash
cd $TMPDIR/w; curl -s -A "Mozilla/5.0" -L "https://www.cell.com/neuron/fulltext/S0896-6273(16)30056-3" -o cell.html; ls -la cell.html; grep -o 'mmc[0-9]\.pdf' cell.html | sort -u; grep -o '<title>[^<]*' cell.html; curl -s "https://pmc-oa-opendata.s3.amazonaws.com/?list-type=2&prefix=PMC4873379" | head -c 1500
```

Result: the fetched text is not kept.

**Agent**

No supplement anywhere reachable, so the attempt uses the main text of the NIH author manuscript. Next I check the claims schema and then write the claims file before running any claim analysis.

**Agent calls Bash**

```bash
cat schemas/claims.schema.json; sed -n 1,80p tools/entry.py; grep -n "def \|argparse\|add_parser" tools/entry.py | head -60
```

```
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Claims proposed for one target (a dandiset and one of its papers)",
  "description": "Draft. To be revised after the pilot.",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schema_version",
    "dandiset",
    "paper",
    "claims"
  ],
  "properties": {
    "schema_version": {
      "const": 1
    },
    "dandiset": {
      "type": "string",
      "pattern": "^[0-9]{6}$"
    },
[... 217 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 116,260p tools/entry.py
```

```
def check(entry_dir: Path) -> Report:
    report = Report()
    rel = entry_dir.relative_to(ROOT)
    entry = validate(report, entry_dir / "entry.yaml", "entry")
    if entry is None:
        return report
    if entry.get("name") != entry_dir.name:
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

[... 126 more lines not kept]
```

**Agent**

I have enough from the data check to write the claims and criteria. Writing the claims file now, before any claim's analysis is run.

**Agent calls Write**

```json
{
 "file_path": "claims/000041/10.1016-j.neuron.2016.03.036.yaml",
 "content": "# Claims for Watson, Levenstein, Greene, Gelinas and Buzsaki (2016) on dandiset 000041.\n# Source: the NIH author manuscript in PubMed Central (PMC4873379), full text of the main\n# article, read from its Results, Experimental Procedures and figure legends. The Supplemental\n# Experimental Procedures and the supplementary figures (NIHMS776601-supplement-1 and -2) could\n# not be retrieved (PMC and the publisher answer with a browser check), and Table 1 is not in\n# the manuscript text. Where the main text leaves a method open, the choice is fixed below.\n#\n# When these criteria were written, the author had seen the data check only: the file list and\n# dandiset metadata; for every file the subject, session, scalar metadata, unit counts by\n# cell_type and region, spike-time ranges, the number and total duration of each state label,\n# LFP shape, rate and chunking, electrode columns; the first 40 rows of the state table in two\n# sessions; and the spike times of Dino-072114, which are whole seconds divided by 20000. No\n# claim's analysis had been run. The paper links no analysis code; the NWB conversion code\n# (catalystneuro/buzsaki-lab-to-nwb at commit 5f6a375) was read.\n#\n# Method choices fixed here, before the analysis:\n# - Sessions. The 21 files whose spike times are usable; Dino-072114 is left out (see the data\n#   check). Each session's units are treated as distinct cells, as the paper counts cells per\n#   session; units have no identifier across sessions.\n# - Cells. Putative pyramidal (pE) cells are units with cell_type \"excitatory\", putative\n#   interneurons (pI) those with \"inhibitory\"; the 23 \"unknown\" units are left out.\n# - States. The dandiset's state table has only Awake, Non-REM and REM. A microarousal (MA) is\n#   an Awake epoch shorter than 40 s whose previous and next epochs are both Non-REM (Results,\n#   identification of brain states). WAKE is every other Awake epoch. A nonREM packet is one\n#   Non-REM epoch. A nonREM episode is a maximal run of packets and MAs, beginning and ending\n#   with a packet. A SLEEP period is a maximal run of epochs that begins with the first\n#   non-Awake epoch after an Awake epoch longer than 120 s and holds no Awake epoch longer than\n#   120 s; it ends at the last non-Awake epoch before an Awake epoch longer than 120 s, must\n#   last at least 20 min from its first start to its last stop, and must be followed by such an\n#   Awake epoch (SLEEP is \"terminated by prolonged (>120 sec) WAKE\"). A WAKE-SLEEP cycle is a\n#   SLEEP period whose preceding Awake epoch lasts at least 7 min.\n# - Rates. A cell's rate over a set of intervals is its spike count over their total duration.\n# - Sextiles. Each pE cell's WAKE rate is its rate over all WAKE epochs of its session; the six\n#   groups are cut at the sextiles of these rates over all pE cells of all sessions (Results:\n#   \"divided pE cells from across the dataset into 6 sextile groups based on their WAKE firing\n#   rates\"). Sextile 1 is the slowest, 6 the fastest.\n# - Time courses. Within packets, episodes, WAKE and REM epochs, 10 bins of normalized time;\n#   packets and episodes of at least 20 s, WAKE epochs of at least 40 s, REM epochs of at least\n#   20 s; for episodes and SLEEP, only Non-REM time within a bin counts. A group's value in a\n#   bin is the mean rate of its cells, divided by the mean of that value over the bins of the\n#   same packet, episode or epoch (units with no spikes in the whole interval are dropped as\n#   undefined). R is the Pearson correlation of these values with bin centre, pooled over all\n#   intervals of all sessions. Other bin counts (5, 20) and a longer minimum (60 s) are shown\n#   as variants.\n# - LFP. One channel per session, the electrode flagged spindle_reference in the electrodes\n#   table (the first when several), read in raw int16 units as the file gives no conversion\n#   factor. Power from 2 s Hann windows stepped by 1 s; bands delta 0.5 to 4 Hz, sigma 9 to 25\n#   Hz, gamma 40 to 100 Hz (Results); log10 of the mean power in band. Only Non-REM time is read.\nschema_version: 1\ndandiset: \"000041\"\npaper: doi:10.1016/j.neuron.2016.03.036\nclaims:\n- id: dataset-composition\n  statement: The recordings come from 11 rats and 27 sessions of 294 plus or minus 137 min,\n    yielding 995 putative pyramidal cells and 126 putative interneurons.\n  source: Results, identification of brain states and assessment of firing patterns;\n    Experimental Procedures\n  expected:\n  - quantity: rats\n    value: 11\n    tolerance: 1.1\n  - quantity: sessions\n    value: 27\n    tolerance: 2.7\n  - quantity: mean session duration\n    value: 294\n    tolerance: 137\n    unit: min\n  - quantity: putative pyramidal cells\n    value: 995\n    tolerance: 99.5\n  - quantity: putative interneurons\n    value: 126\n    tolerance: 12.6\n  criterion: Counted over the files as deposited (22 files), with session duration from the\n    first start to the last stop of the state table (the session's spike span is shown too).\n    The spread given for duration is used as its tolerance. Reproduced when all five values\n    are within tolerance, partially reproduced when at least three are, not reproduced\n    otherwise. The counts in the 21 usable sessions are reported as well.\n- id: fig2a-median-rates\n  statement: Median firing rates of pE cells are 0.76 Hz in WAKE, 0.69 Hz in nonREM and 0.88 Hz\n    in REM; of pI cells 5.59, 4.69 and 4.25 Hz.\n  source: Results, assessment of firing patterns; Figure 2A\n  expected:\n  - quantity: pE median rate, WAKE\n    value: 0.76\n    tolerance: 0.076\n    unit: Hz\n  - quantity: pE median rate, nonREM\n    value: 0.69\n    tolerance: 0.069\n    unit: Hz\n  - quantity: pE median rate, REM\n    value: 0.88\n    tolerance: 0.088\n    unit: Hz\n  - quantity: pI median rate, WAKE\n    value: 5.59\n    tolerance: 0.559\n    unit: Hz\n  - quantity: pI median rate, nonREM\n    value: 4.69\n    tolerance: 0.469\n    unit: Hz\n  - quantity: pI median rate, REM\n    value: 4.25\n    tolerance: 0.425\n    unit: Hz\n  criterion: Each cell's rate over all epochs of a state in its session. Readings (a) WAKE\n    without MAs, as defined above; (b) WAKE as every Awake epoch, MAs included. Reproduced\n    when under one reading all six medians are within tolerance; partially reproduced when at\n    least three are; not reproduced otherwise.\n- id: fig2a-skewed-wide-distribution\n  statement: The distribution of pE firing rates is strongly positively skewed and spans three\n    orders of magnitude, from 0.05 to 5 Hz.\n  source: Results, assessment of firing patterns; Figure 2A\n  criterion: On WAKE rates of pE cells (zero rates kept). Reproduced when the skewness of the\n    rates in Hz is above 1 and the 2.5th and 97.5th percentiles lie within a factor of 2 of\n    0.05 Hz and 5 Hz. The range is read from a log axis (\"three orders of magnitude\"), so the\n    tolerance is a factor on that scale, not 10% of each bound. Partially reproduced when only\n    one of the two holds. The same numbers for nonREM and REM are reported.\n- id: fig2a-fraction-above-2hz\n  statement: The fraction of pE cells firing above 2 Hz is 19.2% in WAKE, 19.2% in REM and 8.8%\n    in nonREM (chi-square, p < 1e-10).\n  source: Results, assessment of firing patterns; Figure 2A\n  expected:\n  - quantity: fraction above 2 Hz, WAKE\n    value: 19.2\n    tolerance: 1.92\n    unit: '%'\n  - quantity: fraction above 2 Hz, REM\n    value: 19.2\n    tolerance: 1.92\n    unit: '%'\n  - quantity: fraction above 2 Hz, nonREM\n    value: 8.8\n    tolerance: 0.88\n    unit: '%'\n  criterion: Rates as in fig2a-median-rates, reading (a). Chi-square tests on the 2 x 2 tables\n    of cells above and below 2 Hz, nonREM against WAKE and nonREM against REM. Reproduced when\n    the three fractions are within tolerance and both tests give p < 1e-10 with nonREM lower;\n    partially reproduced when the tests hold but a fraction is outside tolerance.\n- id: fig2b-wake-nrem-slope\n  statement: Per-cell nonREM and WAKE rates are highly correlated (R = 0.82), and the slope of\n    their relation is below 1 (95% confidence interval 0.66 to 0.71), so state transitions act\n    differently across the rate spectrum.\n  source: Results, assessment of firing patterns; Figure 2B\n  expected:\n  - quantity: Pearson R, nonREM against WAKE rates\n    value: 0.82\n    tolerance: 0.082\n  - quantity: slope of nonREM on WAKE rate\n    value: 0.685\n    tolerance: 0.096\n  criterion: The slope is judged against the reported interval widened by 10% of each bound,\n    0.594 to 0.781 (given above as its centre and half width). Readings (a) log10 rates,\n    cells with a zero rate in either state left out, OLS of nonREM on WAKE; (b) rates in Hz,\n    all pE cells. Reproduced when under one reading R is within tolerance, the slope is in the\n    widened interval and its 95% confidence interval excludes 1; partially reproduced when the\n    slope is below 1 with its interval excluding 1 under some reading but the values miss.\n    The reverse regression (WAKE on nonREM) is shown as a check on regression to the mean.\n- id: fig2-burst-index-by-state\n  statement: The burst index (fraction of spikes with inter-spike intervals under 15 ms) is\n    highest in nonREM (median 11.8%), lowest in WAKE (4.0%), with REM (5.5%) slightly above\n    WAKE (Kruskal-Wallis, p < 0.05).\n  source: Results, assessment of firing patterns\n  expected:\n  - quantity: median burst index, nonREM\n    value: 11.8\n    tolerance: 1.18\n    unit: '%'\n  - quantity: median burst index, WAKE\n    value: 4.0\n    tolerance: 0.4\n    unit: '%'\n  - quantity: median burst index, REM\n    value: 5.5\n    tolerance: 0.55\n    unit: '%'\n  criterion: Per pE cell and state, intervals between consecutive spikes in the same epoch of\n    that state; cells with fewer than 10 such intervals in a state are left out of it.\n    Readings (a) the fraction of intervals under 15 ms; (b) the fraction of spikes with an\n    interval under 15 ms to the previous or the next spike. Reproduced when under one reading\n    the three medians are within tolerance, the order is nonREM > REM > WAKE, and a\n    Kruskal-Wallis test across the three states gives p < 0.05; partially reproduced when the\n    order and test hold but a median misses.\n- id: fig2c-acg-peaks\n  statement: The average spike autocorrelogram of pE cells peaks near 8 ms in nonREM, with a\n    smaller peak near 125 ms (theta) in REM and WAKE.\n  source: Results, assessment of firing patterns; Figure 2C\n  criterion: Per pE cell and state, counts of spike-time differences at 1 ms resolution from 0\n    to 300 ms, pairs within the same epoch, divided by the cell's spike count in the state;\n    averaged over cells with at least 100 spikes in the state. NREM peak is the argmax from 2\n    to 50 ms. The theta peak is the location of the maximum of the mean autocorrelogram\n    smoothed with a 21 ms moving average between 60 and 250 ms, required to lie at least 3 ms\n    inside that window. Reproduced when the nonREM peak is at 7 to 9 ms (8 ms plus or minus\n    10%, rounded to whole bins) and the theta peak in both REM and WAKE is within 112.5 to\n    137.5 ms; partially reproduced when one of the two parts holds.\n- id: fig2c-acg-decay\n  statement: The autocorrelogram of pE cells decays faster in nonREM than in WAKE and REM (decay\n    fit exponent medians -1.35, -0.83 and -0.80; Kruskal-Wallis p < 0.05).\n  source: Results, assessment of firing patterns; Figure 2C\n- id: fig2f-rate-group-correlations\n  statement: In nonREM, pairs of fast-firing pE cells are positively correlated, while pairs of\n    one slow and one fast cell are negatively correlated.\n  source: Results, assessment of firing patterns; Figure 2F\n  criterion: Pearson correlation of spike counts in 100 ms bins over nonREM packets, for every\n    pair of pE cells in the same session; mean correlation for each of the 21 combinations of\n    six rate groups. Readings for the groups (a) WAKE-rate sextiles as above; (b) sextiles of\n    the rate over the whole session. Reproduced when under one reading the mean correlation of\n    group (6,6) pairs is positive and the largest of the 21, and that of (1,6) pairs is below\n    zero by a two-sided one-sample t-test at p < 0.05; partially reproduced when only the\n    (6,6) part holds.\n- id: ma-statistics\n  statement: Microarousals have a median duration of 15.9 plus or minus 3.3 s, occur 0.32 plus\n    or minus 0.12 times per minute and occupy 9.1 plus or minus 3.5% of SLEEP (790 in total).\n  source: Results, identification of brain states\n  expected:\n  - quantity: median MA duration\n    value: 15.9\n    tolerance: 3.3\n    unit: s\n  - quantity: MA frequency\n    value: 0.32\n    tolerance: 0.12\n    unit: per min\n  - quantity: fraction of SLEEP time in MA\n    value: 9.1\n    tolerance: 3.5\n    unit: '%'\n  criterion: MAs derived from the state table as defined above; the paper's spreads are the\n    tolerances. Readings (a) MAs inside SLEEP periods, frequency and fraction per session over\n    SLEEP time, then averaged over sessions, median duration over all those MAs; (b) all MAs,\n    pooled over sessions, frequency per minute of nonREM episode time. Reproduced when under\n    one reading the three values are within tolerance; partially reproduced when two are. The\n    total count is reported but not judged, as the dandiset holds 21 of 27 usable sessions.\n- id: ma-fraction-over-nrem-episodes\n  statement: The fraction of time occupied by MAs decreases over the course of nonREM episodes\n    (R = -0.85, p < 1e-10).\n  source: Results, identification of brain states\n  expected:\n    quantity: Pearson R, MA fraction against normalized episode time\n    value: -0.85\n    tolerance: 0.085\n  criterion: For each nonREM episode with at least one MA, the fraction of each of 10\n    normalized-time bins spent in MA. Readings (a) the mean fraction per bin over episodes,\n    correlated with bin centre (10 points); (b) all episode bins pooled. Reproduced when under\n    one reading R is within tolerance and p < 1e-10; partially reproduced when R is negative\n    with p < 0.05 under some reading.\n- id: packet-duration\n  statement: The duration of nonREM packets spans two orders of magnitude, with a median of 111\n    s.\n  source: Results, identification of brain states\n  expected:\n    quantity: median packet duration\n    value: 111\n    tolerance: 11.1\n    unit: s\n  criterion: Readings (a) every Non-REM epoch; (b) Non-REM epochs inside SLEEP periods.\n    Reproduced when the median is within tolerance under one reading.\n- id: wake-sleep-cycles\n  statement: The dataset holds 54 WAKE-SLEEP episodes (at least 7 min of WAKE followed by at\n    least 20 min of SLEEP), an average of 2.0 per session, and sessions without one were\n    discarded.\n  source: Results, identification of brain states and firing pattern changes across sleep\n  expected:\n    quantity: WAKE-SLEEP cycles per session\n    value: 2.0\n    tolerance: 0.2\n  criterion: Cycles as defined above. Reproduced when the mean per session is within tolerance\n    and every usable session has at least one; partially reproduced when one of the two holds.\n    A variant that also accepts SLEEP ended by the end of the recording is shown.\n- id: fig3b-population-decline\n  statement: The mean firing rate of pE cells declines over the course of SLEEP, restricted to\n    nonREM (R = -0.11, p < 1e-3).\n  source: Results, firing pattern and LFP changes across sleep; Figure 3B\n  depends_on:\n  - wake-sleep-cycles\n  expected:\n    quantity: Pearson R, population rate against normalized SLEEP time\n    value: -0.11\n    tolerance: 0.011\n  criterion: Over the SLEEP periods of WAKE-SLEEP cycles. Readings (a) one point per nonREM\n    packet at the normalized time of its midpoint, its population mean rate divided by the\n    mean of these values over the period's packets; (b) 10 bins of normalized SLEEP time,\n    Non-REM time only, bins with under 10 s of Non-REM dropped, normalized the same way.\n    Reproduced when under one reading R is within tolerance and p < 1e-3; partially\n    reproduced when R is negative with p < 1e-3 but outside tolerance.\n- id: fig3-first-last-packet\n  statement: The mean pE rate is lower in the last than in the first nonREM packet of SLEEP\n    (1.04 plus or minus 1.20 against 0.88 plus or minus 0.91 Hz; Wilcoxon p < 0.02).\n  source: Results, firing pattern and LFP changes across sleep\n  depends_on:\n  - wake-sleep-cycles\n  expected:\n  - quantity: mean rate, first packet\n    value: 1.04\n    tolerance: 0.104\n    unit: Hz\n  - quantity: mean rate, last packet\n    value: 0.88\n    tolerance: 0.088\n    unit: Hz\n  criterion: Over cell and cycle pairs, first and last Non-REM epochs of each SLEEP period of a\n    WAKE-SLEEP cycle. Reproduced when both means are within tolerance and a two-sided Wilcoxon\n    signed-rank test gives p < 0.02 with the last lower; partially reproduced when the test\n    holds but a mean misses.\n- id: fig3d-first-last-slope\n  statement: Comparing the same neurons in the first and last nonREM packets of SLEEP, the\n    regression slope departs from 1 (95% confidence interval 0.827 to 0.880), as fast cells\n    slow down and slow cells speed up.\n  source: Results, firing pattern and LFP changes across sleep; Figure 3D\n  depends_on:\n  - wake-sleep-cycles\n  expected:\n    quantity: slope of last on first packet rate\n    value: 0.8535\n    tolerance: 0.1118\n  criterion: The interval widened by 10% of each bound is 0.744 to 0.968, given as centre and\n    half width. Readings (a) log10 rates, OLS of last on first, pairs with a zero rate left\n    out; (b) rates in Hz. Reproduced when under one reading the slope is in the widened\n    interval and its 95% confidence interval excludes 1; partially reproduced when the slope\n    is below 1 with its interval excluding 1 but outside the widened interval. The reverse\n    regression and the same slope for two halves of one packet are shown as checks on\n    regression to the mean; they do not change the outcome.\n- id: fig3e-wake-before-after\n  statement: pE rates are lower in the 5 min of WAKE after SLEEP than in the 5 min before (p <\n    1e-6, Wilcoxon), with a decrease in the top three sextiles and an increase in the lowest.\n  source: Results, firing pattern changes across sleep and sleep sub-states induce lasting\n    changes; Figure 3E\n  depends_on:\n  - wake-sleep-cycles\n  criterion: The last 300 s of the WAKE epoch before each cycle's SLEEP and the first 300 s\n    of the Awake epoch that ends it (all of it when shorter). Readings for the unit of\n    analysis (a) cell and cycle pairs; (b) per cell, the mean over its session's cycles.\n    Population test, two-sided Wilcoxon signed-rank; sextile tests one-tailed Wilcoxon in the\n    stated direction. Reproduced when under one reading the population decrease has p < 1e-6\n    and sextiles 4, 5 and 6 decrease and sextile 1 increases, each at p < 0.05; partially\n    reproduced when the population decrease holds and at least two of the four sextile\n    effects do.\n- id: fig3b-sextiles-over-sleep\n  statement: Over SLEEP, restricted to nonREM, the fastest sextile decreases its rate while the\n    slowest shows a marginal increase.\n  source: Results, firing pattern changes across sleep; Figure 3B\n  depends_on:\n  - wake-sleep-cycles\n  criterion: Readings (a) and (b) of fig3b-population-decline, per sextile. Reproduced when\n    under one reading sextile 6 has R < 0 with p < 0.05 and sextile 1 has R > 0 (any p, as\n    the paper calls it marginal); partially reproduced when only one of the two holds.\n- id: fig3b-cv-over-sleep\n  statement: The coefficient of variation of pE firing rates decreases over the course of SLEEP\n    (R = -0.05, p < 0.01).\n  source: Results, firing pattern changes across sleep\n  depends_on:\n  - wake-sleep-cycles\n  criterion: CV across a session's pE cells of their rates at each point, readings (a) per\n    packet and (b) 10 bins as in fig3b-population-decline, without normalization. The value of\n    R depends on the binning, which the paper does not give, so it is not judged by\n    tolerance. Reproduced when under one reading R < 0 with p < 0.01.\n- id: fig4iv-sextiles-within-nrem\n  statement: Within both nonREM episodes and nonREM packets, the fastest sextiles decrease\n    their rates while the slowest increase.\n  source: Results, firing rate and LFP changes within nonREM; Figure 4A and 4B, panel iv\n  criterion: Time courses as defined above. Reproduced when sextile 6 has R < 0 and sextile 1\n    has R > 0, each at p < 0.05, in both episodes and packets; partially reproduced when this\n    holds in one of the two, or when one sextile's direction holds in both.\n- id: fig4v-cv-within-nrem\n  statement: The coefficient of variation of binned population rates decreases within nonREM\n    episodes (R = -0.13) and packets (R = -0.12), both p < 1e-10.\n  source: Results, firing rate and LFP changes within nonREM; Figure 4A and 4B, panel v\n  criterion: CV across the session's pE cells of their rates in each bin, pooled. As the\n    binning is not given, R is not judged by tolerance. Reproduced when R < 0 with p < 1e-10\n    in both episodes and packets; partially reproduced when in one.\n- id: fig4vi-burst-within-nrem\n  statement: The 15 ms burst index of pE cells increases within nonREM episodes (R = 0.09) and\n    packets (R = 0.08), both p < 1e-10.\n  source: Results, firing rate and LFP changes within nonREM; Figure 4A and 4B, panel vi\n  criterion: In each bin, the fraction of intervals under 15 ms among the intervals of the\n    session's pE cells whose two spikes lie in the same packet and whose later spike falls in\n    the bin; pooled R against bin centre. Reproduced when R > 0 with p < 1e-10 in both episodes\n    and packets; partially reproduced when in one.\n- id: fig4i-band-power-within-nrem\n  statement: Delta and sigma power increase over nonREM episodes and packets, while gamma power\n    decreases over episodes but not over packets.\n  source: Results, firing rate and LFP changes within nonREM; Figure 4A and 4B, panel i\n  criterion: Log band power per bin minus its mean over the bins of the same packet or\n    episode, pooled R against bin centre. Reproduced when delta and sigma have R > 0 with p <\n    0.05 in both episodes and packets, and gamma has R < 0 with p < 0.05 in episodes and p >=\n    0.05 or R >= 0 in packets; partially reproduced when the delta and sigma part holds and\n    the gamma part does not.\n- id: fig4-delta-packet-length\n  statement: Mean delta power within whole packets, normalized by nonREM delta power, is\n    positively correlated with packet length (R = 0.31, p < 0.05).\n  source: Results, firing rate and LFP changes within nonREM\n  expected:\n    quantity: Pearson R, packet delta power against packet length\n    value: 0.31\n    tolerance: 0.031\n  criterion: Per packet of at least 20 s, mean delta power over the packet divided by the mean\n    over all Non-REM time of its session, against packet duration in s, pooled. Reproduced\n    when R is within tolerance and p < 0.05; partially reproduced when R > 0 with p < 0.05.\n- id: fig4cd-packet-rate-lfp\n  statement: Per packet, the rate of the fastest sextile is negatively correlated with delta\n    power (R = -0.28) and positively with gamma power (R = 0.44), and the rate of the slowest\n    sextile is positively correlated with sigma power in the last 20 s of the packet (R =\n    0.25), all p < 1e-10.\n  source: Results, firing rate and LFP changes within nonREM; Figure 4C and 4D\n  expected:\n  - quantity: R, sextile 6 rate against packet delta power\n    value: -0.28\n    tolerance: 0.028\n  - quantity: R, sextile 6 rate against packet gamma power\n    value: 0.44\n    tolerance: 0.044\n  - quantity: R, sextile 1 rate against sigma power in the last 20 s\n    value: 0.25\n    tolerance: 0.025\n  criterion: Packets of at least 20 s. Group mean rate per packet and log band power, each\n    z-scored over the packets of its session, pooled. Reproduced when all three R are within\n    tolerance with p < 1e-10; partially reproduced when at least two have the stated sign with\n    p < 0.05.\n- id: fig5b-nrem-between-ma\n  statement: An intervening nonREM packet reduces the rates of the top two sextiles from one MA\n    to the next (both p < 0.01).\n  source: Results, sleep sub-states induce lasting changes; Figure 5B\n  criterion: Triplets of consecutive epochs MA, packet, MA. Change per pE cell and triplet is\n    the rate in the second MA minus the first. Two-sided Wilcoxon signed-rank per sextile over\n    cell and triplet pairs. Reproduced when sextiles 5 and 6 both have a negative mean change\n    with p < 0.01; partially reproduced when one does. The per-cell mean over triplets is\n    shown as a variant.\n- id: fig5b-wake-between-packets\n  statement: An intervening WAKE episode increases the rate of the fastest sextile from one\n    nonREM packet to the next (24 triplets).\n  source: Results, sleep sub-states induce lasting changes; Figure 5B\n  criterion: Triplets packet, WAKE, packet; change is the rate in the second packet minus the\n    first; tests as in fig5b-nrem-between-ma. Reproduced when sextile 6 has a positive mean\n    change with p < 0.05. The number of triplets is reported against the paper's 24.\n- id: fig5b-ma-between-packets\n  statement: An intervening MA increases the rates of slow-firing pE cells from one packet to\n    the next and does not affect fast-firing cells.\n  source: Results, sleep sub-states induce lasting changes; Figure 5B\n  criterion: Triplets packet, MA, packet; tests as in fig5b-nrem-between-ma. Reproduced when\n    sextile 1 has a positive mean change with p < 0.05 and sextile 6 has p >= 0.05; partially\n    reproduced when sextile 1 increases but sextile 6 changes too.\n- id: fig5b-rem-between-packets\n  statement: An intervening REM episode decreases the rates of all sextiles from one packet to\n    the next.\n  source: Results, sleep sub-states induce lasting changes; Figure 5B\n  criterion: Triplets packet, REM, packet; tests as in fig5b-nrem-between-ma. Reproduced when\n    all six sextiles have a negative mean change with p < 0.05; partially reproduced when at\n    least three do and none increases significantly.\n- id: fig5c-rem-duration\n  statement: Longer REM episodes produce a proportionally larger decrease of rates from one\n    packet to the next (R = -0.22, p < 1e-2).\n  source: Results, sleep sub-states induce lasting changes; Figure 5C\n  expected:\n    quantity: Pearson R, rate change against REM duration\n    value: -0.22\n    tolerance: 0.022\n  criterion: Triplets packet, REM, packet. Readings (a) per triplet, the fractional change of\n    the pE population mean rate, (post - pre) / pre; (b) per cell and triplet, the fractional\n    change, cells with a pre rate above 0. Reproduced when under one reading R is within\n    tolerance with p < 0.01; partially reproduced when R < 0 with p < 0.01.\n- id: fig5c-sigma-ma\n  statement: Sigma power in the last 20 s of a packet between two MAs correlates with a larger\n    increase of the slowest sextile from one MA to the next (R = 0.181, p < 0.01).\n  source: Results, sleep sub-states induce lasting changes; Figure 5C\n  expected:\n    quantity: Pearson R, sigma power against sextile 1 change\n    value: 0.181\n    tolerance: 0.0181\n  criterion: MA, packet, MA triplets; log sigma power of the last 20 s of the packet z-scored\n    over the session's packets; change of the sextile 1 mean rate from the first to the second\n    MA. Reproduced when R is within tolerance with p < 0.01; partially reproduced when R > 0\n    with p < 0.01.\n- id: fig5c-delta-change\n  statement: The increase of the slowest sextile's rate from one packet to the next is\n    positively correlated with the change of delta power between the packets, regardless of\n    the intervening state.\n  source: Results, sleep sub-states induce lasting changes; Figure 5C\n  criterion: Consecutive packets (any intervening epochs, within a nonREM episode or SLEEP\n    period or not), each at least 20 s; change of the sextile 1 mean rate against the change of\n    the session-normalized delta power (packet mean divided by the session's Non-REM mean).\n    Reproduced when R > 0 with p < 0.05.\n- id: figs5-within-wake-rem\n  statement: Within WAKE the two fastest sextiles increase and the two slowest decrease their\n    rates; within REM all sextiles except the fourth increase.\n  source: Results, firing rate and LFP changes within nonREM, last paragraph (Figure S5A and\n    S5B)\n  criterion: Time courses within WAKE epochs of at least 40 s and REM epochs of at least 20 s.\n    The WAKE part holds when sextiles 5 and 6 have R > 0 and sextiles 1 and 2 R < 0, each at p\n    < 0.05; the REM part when sextiles 1, 2, 3, 5 and 6 have R > 0 at p < 0.05. Reproduced when\n    both parts hold, partially reproduced when one does.\n- id: fig5c-wake-movement\n  statement: WAKE periods with more movement have a larger effect on the rate increase of the\n    fastest sextile from one packet to the next (R = 0.43, p < 0.05).\n  source: Results, sleep sub-states induce lasting changes; Figure 5C\n- id: updown-durations\n  statement: DOWN states have a median duration of 0.19 s and UP states 0.47 s.\n  source: Results, assessment of firing patterns (Figure S4A)\n- id: fig3c-slow-oscillation-spindles-over-sleep\n  statement: Over SLEEP, the incidence of spindles (R = -0.093), UP states (R = -0.10) and DOWN\n    states (R = -0.08) decreases and DOWN state duration increases, while spindle duration,\n    frequency and amplitude do not change.\n  source: Results, firing pattern and LFP changes across sleep; Figure 3C\n- id: fig4ii-iii-updown-spindles-within-packets\n  statement: Within packets the incidence of UP and DOWN states increases, UP states shorten and\n    DOWN states lengthen, and spindle incidence and duration increase.\n  source: Results, firing rate and LFP changes within nonREM; Figure 4A and 4B, panels ii and\n    iii\n- id: fig2de-up-state-sequences\n  statement: pE cells fire in stable sequences early in UP states, and the latency of a cell's\n    first spike is negatively correlated with its firing rate.\n  source: Results, assessment of firing patterns; Figure 2D and 2E\n- id: fig3f-4e-within-up-rates\n  statement: Within UP states, the fastest sextile and pI cells decrease and the slowest sextile\n    increases from early to late SLEEP, and within packets the fastest sextile drops while pI\n    cells increase.\n  source: Results; Figure 3F and Figure 4E\n"
}
```

```
File created successfully at: claims/000041/10.1016-j.neuron.2016.03.036.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python -c "
import yaml,json,jsonschema
d=yaml.safe_load(open('claims/000041/10.1016-j.neuron.2016.03.036.yaml'))
jsonschema.validate(d, json.load(open('schemas/claims.schema.json')))
print(len(d['claims']))
import re
for c in d['claims']:
  for k,v in c.items():
    if isinstance(v,str) and ': ' in v: print('COLON', c['id'], k)
"
```

```
39
```

**Agent**

Claims file validates (39 claims). Now the helper module.

**Agent calls Write**

```json
{
 "file_path": "entries/000041-watson-2016/sleepstates.py",
 "content": "\"\"\"Loading and sleep-state measures for dandiset 000041 (Watson et al. 2016, Neuron).\n\nThe dandiset holds one NWB file per session: sorted units with spike times and a cell type,\na table of sleep states (Awake, Non-REM, REM, at 1 s resolution), LFP at 1250 Hz and spike\nwaveforms. Files are streamed from the DANDI Archive at a pinned version; nothing is\nwritten to disk.\n\nWhere parameters come from:\n\n- Microarousal (MA): an Awake epoch shorter than 40 s between two Non-REM epochs. Paper,\n  Results (\"Shorter epochs (<40 sec) ... restricted ... to only those which occur between\n  nonREM periods\").\n- SLEEP: alternating nonREM and REM of at least 20 min, terminated by Awake longer than\n  120 s; a WAKE-SLEEP cycle needs at least 7 min of WAKE before it. Paper, Results.\n- Burst index: fraction of inter-spike intervals under 15 ms. Paper, Results.\n- Frequency bands: delta 0.5-4 Hz, sigma 9-25 Hz, gamma 40-100 Hz. Paper, Results.\n- Sextiles of WAKE rate over all pE cells of the dataset. Paper, Results and Methods.\n- Choices the paper's main text leaves open, made here as common defaults: 10 bins of\n  normalized time; 2 s Hann windows stepped by 1 s for LFP power; the LFP channel flagged\n  `spindle_reference` in the electrodes table; packets of at least 20 s for time courses.\n\"\"\"\n\nfrom __future__ import annotations\n\nfrom dataclasses import dataclass, field\n\nimport h5py\nimport numpy as np\nimport remfile\nfrom dandi.dandiapi import DandiAPIClient\nfrom scipy import signal\n\nDANDISET_ID = \"000041\"\nDANDISET_VERSION = \"0.250624.0419\"\n\n# Spike times of this file are whole seconds divided by 20000 (8451 distinct values from 0 to\n# 0.4252 s, against a recording of 7959 s); the conversion set a 20 kHz rate on times already in\n# seconds. Its spikes cannot be placed in time, so the session is left out of every analysis.\nEXCLUDED = {\n    \"sub-Dino/sub-Dino_ses-Dino-072114_ecephys.nwb\":\n        \"spike times are whole seconds divided by 20000\",\n}\n\nLFP_RATE = 1250.0\nBANDS = {\"delta\": (0.5, 4.0), \"sigma\": (9.0, 25.0), \"gamma\": (40.0, 100.0)}\nMA_MAX = 40.0          # s, longest microarousal\nSLEEP_BREAK = 120.0    # s, Awake longer than this ends SLEEP\nSLEEP_MIN = 20 * 60.0  # s, shortest SLEEP period\nWAKE_MIN = 7 * 60.0    # s, shortest WAKE before a WAKE-SLEEP cycle\nBURST_ISI = 0.015      # s\n\n\ndef asset_urls() -> list[tuple[str, str]]:\n    \"\"\"(path, streaming URL) for every NWB file of the pinned version, sorted by path.\"\"\"\n    with DandiAPIClient() as client:\n        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)\n        return sorted((a.path, a.get_content_url(follow_redirects=1, strip_query=True))\n                      for a in ds.get_assets())\n\n\ndef open_nwb(url: str) -> h5py.File:\n    return h5py.File(remfile.File(url), \"r\")\n\n\ndef _str(values) -> np.ndarray:\n    return np.array([v.decode() if isinstance(v, bytes) else str(v) for v in values])\n\n\n@dataclass\nclass Session:\n    path: str\n    subject: str\n    session_id: str\n    spikes: list            # one sorted array of spike times (s) per unit\n    cell_type: np.ndarray   # 'excitatory', 'inhibitory' or 'unknown'\n    starts: np.ndarray      # state table\n    stops: np.ndarray\n    labels: np.ndarray      # 'Awake', 'Non-REM', 'REM'\n    state: np.ndarray = field(default=None)  # 'WAKE', 'MA', 'NREM', 'REM'\n    lfp_channel: int = -1\n    lfp_samples: int = 0\n    lfp: dict = field(default_factory=dict)  # per packet index, band power series\n\n    @property\n    def pe(self) -> np.ndarray:\n        return np.where(self.cell_type == \"excitatory\")[0]\n\n    @property\n    def pi(self) -> np.ndarray:\n        return np.where(self.cell_type == \"inhibitory\")[0]\n\n\ndef load_session(path: str, url: str, f: h5py.File | None = None) -> Session:\n    \"\"\"Units, states and the LFP reference channel of one file; LFP itself is not read.\"\"\"\n    f = f or open_nwb(url)\n    u = f[\"units\"]\n    times = u[\"spike_times\"][()]\n    idx = u[\"spike_times_index\"][()]\n    bounds = np.concatenate([[0], idx])\n    spikes = [np.sort(times[bounds[i]:bounds[i + 1]]) for i in range(len(idx))]\n    st = f[\"processing/behavior/states\"]\n    el = f[\"general/extracellular_ephys/electrodes\"]\n    ref = np.where(el[\"spindle_reference\"][()])[0]\n    lfp_el = f[\"processing/ecephys/LFP/lfp/electrodes\"][()]\n    # column of the LFP matrix that holds the reference electrode\n    col = int(np.where(lfp_el == ref[0])[0][0]) if len(ref) and ref[0] in lfp_el else -1\n    s = Session(path=path,\n                subject=_str([f[\"general/subject/subject_id\"][()]])[0],\n                session_id=_str([f[\"general/session_id\"][()]])[0],\n                spikes=spikes, cell_type=_str(u[\"cell_type\"][()]),\n                starts=st[\"start_time\"][()].astype(float), stops=st[\"stop_time\"][()].astype(float),\n                labels=_str(st[\"label\"][()]),\n                lfp_channel=col, lfp_samples=f[\"processing/ecephys/LFP/lfp/data\"].shape[0])\n    s.state = classify_states(s.starts, s.stops, s.labels)\n    return s\n\n\ndef classify_states(starts, stops, labels) -> np.ndarray:\n    \"\"\"WAKE, MA, NREM or REM for each row of the state table (MA as in the module docstring).\"\"\"\n    out = np.array([\"WAKE\" if L == \"Awake\" else \"NREM\" if L == \"Non-REM\" else \"REM\" for L in labels],\n                   dtype=object)\n    dur = stops - starts\n    for i in range(1, len(labels) - 1):\n        if labels[i] == \"Awake\" and dur[i] < MA_MAX and labels[i - 1] == \"Non-REM\" and labels[i + 1] == \"Non-REM\":\n            out[i] = \"MA\"\n    return out\n\n\ndef nrem_episodes(state) -> list[tuple[int, int]]:\n    \"\"\"(first, last) row of each maximal run of NREM and MA, beginning and ending with NREM.\"\"\"\n    runs, i, n = [], 0, len(state)\n    while i < n:\n        if state[i] == \"NREM\":\n            j = i\n            while j + 1 < n and state[j + 1] in (\"NREM\", \"MA\"):\n                j += 1\n            while state[j] != \"NREM\":\n                j -= 1\n            runs.append((i, j))\n            i = j + 1\n        else:\n            i += 1\n    return runs\n\n\ndef sleep_periods(starts, stops, labels, require_wake_end: bool = True) -> list[dict]:\n    \"\"\"SLEEP periods as defined in the claims file, with the Awake rows before and after.\"\"\"\n    dur = stops - starts\n    long_wake = (labels == \"Awake\") & (dur > SLEEP_BREAK)\n    out, n, i = [], len(labels), 0\n    while i < n:\n        if labels[i] != \"Awake\" and (i == 0 or long_wake[i - 1] or labels[i - 1] != \"Awake\"):\n            # a period begins at the first non-Awake row after a long Awake row\n            if i > 0 and not long_wake[i - 1]:\n                i += 1\n                continue\n            j = i\n            while j + 1 < n and not long_wake[j + 1]:\n                j += 1\n            last = j\n            while labels[last] == \"Awake\":\n                last -= 1\n            ended = j + 1 < n\n            if (ended or not require_wake_end) and stops[last] - starts[i] >= SLEEP_MIN:\n                out.append(dict(first=i, last=last, start=starts[i], stop=stops[last],\n                                pre=i - 1 if i > 0 else None, post=j + 1 if ended else None))\n            i = j + 1\n        else:\n            i += 1\n    return out\n\n\ndef cycles(s: Session, require_wake_end: bool = True) -> list[dict]:\n    \"\"\"WAKE-SLEEP cycles: SLEEP periods preceded by an Awake epoch of at least 7 min.\"\"\"\n    return [p for p in sleep_periods(s.starts, s.stops, s.labels, require_wake_end)\n            if p[\"pre\"] is not None and s.stops[p[\"pre\"]] - s.starts[p[\"pre\"]] >= WAKE_MIN]\n\n\ndef counts(spk: np.ndarray, starts, stops) -> np.ndarray:\n    \"\"\"Spike counts of one unit in each interval [start, stop).\"\"\"\n    return np.searchsorted(spk, stops) - np.searchsorted(spk, starts)\n\n\ndef rates(spikes: list, units, starts, stops) -> np.ndarray:\n    \"\"\"Rate of each unit over the union of the intervals (Hz); intervals must not overlap.\"\"\"\n    starts, stops = np.atleast_1d(starts), np.atleast_1d(stops)\n    T = float(np.sum(stops - starts))\n    return np.array([counts(spikes[u], starts, stops).sum() / T for u in units])\n\n\ndef state_rates(s: Session, units, states) -> np.ndarray:\n    m = np.isin(s.state, states)\n    return rates(s.spikes, units, s.starts[m], s.stops[m])\n\n\ndef binned_intervals(start, stop, nbins, include=None):\n    \"\"\"For each of nbins equal bins of [start, stop), the sub-intervals that fall in `include`\n    (a list of (start, stop)); all of the bin when include is None. Returns a list of\n    (starts, stops) arrays, one per bin.\"\"\"\n    edges = np.linspace(start, stop, nbins + 1)\n    out = []\n    for a, b in zip(edges[:-1], edges[1:]):\n        if include is None:\n            out.append((np.array([a]), np.array([b])))\n        else:\n            ss = [max(a, x) for x, y in include if y > a and x < b]\n            ee = [min(b, y) for x, y in include if y > a and x < b]\n            out.append((np.array(ss), np.array(ee)))\n    return out\n\n\ndef bin_rates(s: Session, units, bins) -> tuple[np.ndarray, np.ndarray]:\n    \"\"\"Rates (units x bins) and durations per bin for the output of binned_intervals.\"\"\"\n    dur = np.array([np.sum(e - a) for a, e in bins])\n    r = np.full((len(units), len(bins)), np.nan)\n    for k, (a, e) in enumerate(bins):\n        if dur[k] > 0:\n            r[:, k] = [counts(s.spikes[u], a, e).sum() / dur[k] for u in units]\n    return r, dur\n\n\ndef isis_in(spk: np.ndarray, starts, stops):\n    \"\"\"Intervals between consecutive spikes whose two spikes lie in the same interval; returns\n    (isi, time of the later spike, index of the interval).\"\"\"\n    if len(spk) < 2:\n        return np.array([]), np.array([]), np.array([], int)\n    k = np.searchsorted(starts, spk, side=\"right\") - 1\n    inside = (k >= 0) & (spk < np.asarray(stops)[np.clip(k, 0, None)])\n    same = inside[1:] & inside[:-1] & (k[1:] == k[:-1])\n    return np.diff(spk)[same], spk[1:][same], k[1:][same]\n\n\ndef burst_index(spk, starts, stops, reading: str = \"a\", min_isi: int = 10) -> float:\n    \"\"\"Reading a: fraction of intervals under 15 ms. Reading b: fraction of spikes with an\n    interval under 15 ms to the previous or next spike (same interval only).\"\"\"\n    if len(spk) < 2:\n        return np.nan\n    starts, stops = np.asarray(starts), np.asarray(stops)\n    k = np.searchsorted(starts, spk, side=\"right\") - 1\n    inside = (k >= 0) & (spk < stops[np.clip(k, 0, None)])\n    same = inside[1:] & inside[:-1] & (k[1:] == k[:-1])\n    if same.sum() < min_isi:\n        return np.nan\n    short = (np.diff(spk) < BURST_ISI) & same\n    if reading == \"a\":\n        return short.sum() / same.sum()\n    part = np.zeros(len(spk), bool)\n    part[1:] |= short\n    part[:-1] |= short\n    return part[inside].sum() / inside.sum()\n\n\ndef autocorrelogram(spk, starts, stops, max_lag=0.3, bin_ms=1.0) -> tuple[np.ndarray, int]:\n    \"\"\"Counts of spike-time differences in 1 ms bins from 0 to max_lag, pairs within the same\n    interval, and the number of spikes inside the intervals.\"\"\"\n    starts, stops = np.asarray(starts), np.asarray(stops)\n    k = np.searchsorted(starts, spk, side=\"right\") - 1\n    inside = (k >= 0) & (spk < stops[np.clip(k, 0, None)])\n    t, k = spk[inside], k[inside]\n    edges = np.arange(0, max_lag * 1000 + bin_ms, bin_ms) / 1000.0\n    h = np.zeros(len(edges) - 1)\n    lag = 1\n    while lag < len(t):\n        d = t[lag:] - t[:-lag]\n        ok = (k[lag:] == k[:-lag]) & (d < max_lag)\n        if not ok.any() and np.min(d) >= max_lag:\n            break\n        h += np.histogram(d[ok], edges)[0]\n        lag += 1\n    return h, len(t)\n\n\ndef band_power(x: np.ndarray, fs: float = LFP_RATE):\n    \"\"\"Log10 mean power in each band for 2 s Hann windows stepped by 1 s; returns the window\n    centres (s, from the start of x) and a dict of arrays.\"\"\"\n    nper = int(2 * fs)\n    if len(x) < nper:\n        return np.array([]), {b: np.array([]) for b in BANDS}\n    f, t, S = signal.spectrogram(x.astype(float), fs=fs, window=\"hann\", nperseg=nper,\n                                 noverlap=nper - int(fs), detrend=\"constant\", scaling=\"density\")\n    out = {}\n    for b, (lo, hi) in BANDS.items():\n        m = (f >= lo) & (f <= hi)\n        out[b] = np.log10(S[m].mean(axis=0))\n    return t, out\n\n\ndef read_packet_lfp(f: h5py.File, s: Session, min_dur: float = 2.0) -> None:\n    \"\"\"Band power series of every NREM packet of at least min_dur seconds, from the reference\n    channel, into s.lfp[row] = (window centre times in s, dict of log10 band power).\"\"\"\n    d = f[\"processing/ecephys/LFP/lfp/data\"]\n    for i in np.where(s.state == \"NREM\")[0]:\n        a, b = s.starts[i], s.stops[i]\n        if b - a < min_dur:\n            continue\n        i0, i1 = int(round(a * LFP_RATE)), min(int(round(b * LFP_RATE)), s.lfp_samples)\n        if i1 - i0 < int(2 * LFP_RATE):\n            continue\n        x = d[i0:i1, s.lfp_channel]\n        t, p = band_power(x)\n        s.lfp[i] = (a + t, p)\n\n\ndef wake_sextiles(sessions: list[Session]) -> tuple[np.ndarray, dict]:\n    \"\"\"Sextile edges of WAKE rate over all pE cells, and for each session path the WAKE rate\n    and sextile (1 to 6) of each of its pE cells.\"\"\"\n    wr = {s.path: state_rates(s, s.pe, [\"WAKE\"]) for s in sessions}\n    allr = np.concatenate(list(wr.values()))\n    edges = np.quantile(allr, np.linspace(0, 1, 7))\n    out = {}\n    for p, r in wr.items():\n        g = np.searchsorted(edges[1:-1], r, side=\"right\") + 1\n        out[p] = (r, g)\n    return edges, out\n"
}
```

```
File created successfully at: entries/000041-watson-2016/sleepstates.py (file state is current in your context — no need to Read it back)
```

**Agent**

The `sleep_periods` logic is needlessly tangled; replacing it with a segment-based version.

**Agent calls Bash**

```bash
cd entries/000041-watson-2016 && python - <<'EOF'
src=open('sleepstates.py').read()
a=src.index('def sleep_periods(')
b=src.index('def cycles(')
new='''def sleep_periods(starts, stops, labels, require_wake_end: bool = True) -> list[dict]:
    """SLEEP periods as defined in the claims file. Awake rows longer than 120 s split the
    session into segments; in each, leading and trailing Awake rows are trimmed and what remains
    is a SLEEP period if it lasts at least 20 min. `pre` and `post` are the long Awake rows
    around it (None at the start or end of the recording)."""
    long_wake = np.where((labels == "Awake") & (stops - starts > SLEEP_BREAK))[0]
    cuts = [-1] + list(long_wake) + [len(labels)]
    out = []
    for lo, hi in zip(cuts[:-1], cuts[1:]):
        rows = [r for r in range(lo + 1, hi) if labels[r] != "Awake"]
        if not rows:
            continue
        first, last = rows[0], rows[-1]
        pre = lo if lo >= 0 else None
        post = hi if hi < len(labels) else None
        if post is None and require_wake_end:
            continue
        if stops[last] - starts[first] >= SLEEP_MIN:
            out.append(dict(first=first, last=last, start=starts[first], stop=stops[last],
                            pre=pre, post=post))
    return out


'''
open('sleepstates.py','w').write(src[:a]+new+src[b:])
EOF
```

```
(Bash completed with no output)
```

**Agent**

Quick synthetic tests of the helpers, then a timed load of all sessions with LFP.

**Agent calls Bash**

```bash
$TMPDIR/venv/bin/python - <<'EOF'
import numpy as np, sleepstates as ss
L=np.array(['Awake','Non-REM','Awake','Non-REM','REM','Awake','Non-REM','Awake','Non-REM','Awake'])
st=np.array([0,500,1500,1510,2000,2100,2150,2900,2930,3500.]); sp=np.r_[st[1:]-1,4000.]
print(ss.classify_states(st,sp,L))
print(ss.nrem_episodes(ss.classify_states(st,sp,L)))
print(ss.sleep_periods(st,sp,L), ss.sleep_periods(st,sp,L,False))
spk=np.array([0.0,0.01,0.02,0.1,0.5,0.505,1.2,1.21]);
print(ss.burst_index(spk,[0],[1],'a',1), ss.burst_index(spk,[0],[1],'b',1), ss.burst_index(spk,[0,1],[1,2],'a',1))
h,n=ss.autocorrelogram(spk,[0],[1]); print(n, np.nonzero(h)[0], h[np.nonzero(h)])
x=np.sin(2*np.pi*2*np.arange(0,20,1/1250)); t,p=ss.band_power(x); print(t[:3], {k:v[:2].round(2) for k,v in p.items()})
print(ss.binned_intervals(0,10,2,[(1,3),(4,8)]))
EOF
```

```
['WAKE' 'NREM' 'MA' 'NREM' 'REM' 'WAKE' 'NREM' 'MA' 'NREM' 'WAKE']
[(1, 3), (6, 8)]
[{'first': 1, 'last': 8, 'start': np.float64(500.0), 'stop': np.float64(3499.0), 'pre': np.int64(0), 'post': np.int64(9)}] [{'first': 1, 'last': 8, 'start': np.float64(500.0), 'stop': np.float64(3499.0), 'pre': np.int64(0), 'post': np.int64(9)}]
0.6 0.8333333333333334 0.6666666666666666
6 [  5  10  20  80  90 100] [1. 2. 1. 1. 1. 1.]
[1. 2. 3.] {'delta': array([-0.9, -0.9]), 'sigma': array([-32.79, -32.08]), 'gamma': array([-33.01, -33.2 ])}
[(array([1, 4]), array([3., 5.])), (array([5.]), array([8]))]
```

**Agent**

Helpers behave as intended. Now a timed full load (units, states, packet LFP power) to check runtime.

**Agent calls Bash**

```bash
cat > $TMPDIR/w/loadall.py <<'EOF'
import sys, time, pickle
sys.path.insert(0, 'entries/000041-watson-2016')
import sleepstates as ss
t0=time.time(); sessions=[]
for path,url in ss.asset_urls():
    if path in ss.EXCLUDED: continue
    f=ss.open_nwb(url); s=ss.load_session(path,url,f); t1=time.time()
    ss.read_packet_lfp(f,s)
    print(path, s.lfp_channel, len(s.lfp), round(t1-t0), round(time.time()-t0), flush=True)
    sessions.append(s)
pickle.dump(sessions, open('/tmp/claude-1001/w/sessions.pkl','wb'))
print('total', time.time()-t0)
EOF
cd $TMPDIR/w && $TMPDIR/venv/bin/python loadall.py
```

```
sub-BWRat17/sub-BWRat17_ses-BWRat17-121712_ecephys.nwb 13 13 3 8
sub-BWRat17/sub-BWRat17_ses-BWRat17-121912_ecephys.nwb 13 31 10 23
sub-BWRat18/sub-BWRat18_ses-BWRat18-020513_ecephys.nwb 59 19 25 41
sub-BWRat19/sub-BWRat19_ses-BWRat19-032413_ecephys.nwb 54 16 42 53
sub-BWRat19/sub-BWRat19_ses-BWRat19-032513_ecephys.nwb 24 18 55 68
sub-BWRat20/sub-BWRat20_ses-BWRat20-101013_ecephys.nwb 59 26 70 84
sub-BWRat20/sub-BWRat20_ses-BWRat20-101513_ecephys.nwb 61 107 86 118
sub-BWRat21/sub-BWRat21_ses-BWRat21-121113_ecephys.nwb 7 67 120 147
sub-BWRat21/sub-BWRat21_ses-BWRat21-121613_ecephys.nwb 12 59 149 173
sub-BWRat21/sub-BWRat21_ses-BWRat21-121813_ecephys.nwb 12 49 175 199
sub-Bogey/sub-Bogey_ses-Bogey-012615_ecephys.nwb 46 91 201 236
sub-Dino/sub-Dino_ses-Dino-061814_ecephys.nwb 92 61 239 272
sub-Dino/sub-Dino_ses-Dino-061914_ecephys.nwb 83 42 274 300
sub-Dino/sub-Dino_ses-Dino-062014_ecephys.nwb 83 60 303 335
sub-Dino/sub-Dino_ses-Dino-072314_ecephys.nwb 106 24 337 353
sub-Dino/sub-Dino_ses-Dino-072414_ecephys.nwb 106 26 355 373
sub-Rizzo/sub-Rizzo_ses-Rizzo-022615_ecephys.nwb 17 110 375 435
sub-Rizzo/sub-Rizzo_ses-Rizzo-022715_ecephys.nwb 52 61 437 463
sub-Splinter/sub-Splinter_ses-Splinter-020515_ecephys.nwb 42 53 464 494
sub-Splinter/sub-Splinter_ses-Splinter-020915_ecephys.nwb 43 51 496 521
[... 3 more lines not kept]
```

**Agent**

Full load takes about 9 min serially, mostly LFP. I'll add a parallel loader (4 processes) to the helper to bring this down, then prototype the analyses against a cached copy in scratch space.

**Agent calls Bash**

```bash
cat >> entries/000041-watson-2016/sleepstates.py <<'EOF'


def _load_with_lfp(item) -> Session:
    path, url = item
    f = open_nwb(url)
    s = load_session(path, url, f)
    read_packet_lfp(f, s)
    return s


def load_all(workers: int = 4) -> tuple[list[Session], dict]:
    """Every usable session with its packet LFP power, streamed in parallel, in path order;
    and the excluded paths with the reason."""
    from concurrent.futures import ProcessPoolExecutor
    items = [(p, u) for p, u in asset_urls() if p not in EXCLUDED]
    with ProcessPoolExecutor(workers) as ex:
        sessions = list(ex.map(_load_with_lfp, items))
    return sessions, dict(EXCLUDED)
EOF
cat > $TMPDIR/w/t_par.py <<'EOF'
import sys,time
sys.path.insert(0,'entries/000041-watson-2016')
import sleepstates as ss
if __name__=='__main__':
    t=time.time(); s,e=ss.load_all(6); print(len(s), time.time()-t)
EOF
cd $TMPDIR/w && $TMPDIR/venv/bin/python t_par.py
```

```
21 111.13154864311218
Shell cwd was reset to
```

**Agent**

Parallel load takes 111 s with 6 workers. Now prototyping the full analysis as a cell-marked script (later turned into the notebook), run against a cached copy of the loaded sessions.

**Agent calls Bash**

```bash
cd $TMPDIR/w && cat > cache.py <<'EOF'
import sys,pickle
sys.path.insert(0,'entries/000041-watson-2016')
import sleepstates as ss
if __name__=='__main__':
    s,e=ss.load_all(6); pickle.dump((s,e),open('cache.pkl','wb'))
EOF
$TMPDIR/venv/bin/python cache.py && ls -la cache.pkl
```

```
-rw-r--r-- 1 runner runner 204831315 Oct 16 02:38 cache.pkl
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/w/nb_src.py",
 "content": "# %% [markdown]\n# # Reproducing Watson et al. (2016) from dandiset 000041\n#\n# **Paper.** Watson BO, Levenstein D, Greene JP, Gelinas JN, Buzsáki G (2016). Network homeostasis\n# and state dynamics of neocortical sleep. *Neuron* 90:839-852.\n# [doi:10.1016/j.neuron.2016.03.036](https://doi.org/10.1016/j.neuron.2016.03.036)\n#\n# **Text used.** The full text of the NIH author manuscript in PubMed Central (PMC4873379): Results,\n# Experimental Procedures and figure legends. The Supplemental Experimental Procedures and the\n# supplementary figures could not be retrieved, and Table 1 is not in the manuscript text, so methods\n# described only there (UP/DOWN state and spindle detection, the autocorrelogram decay fit) are not\n# available to this attempt.\n#\n# **Data.** [DANDI:000041 version 0.250624.0419](https://dandiarchive.org/dandiset/000041/0.250624.0419),\n# streamed from the archive. The paper cites no dandiset version (it points to CRCNS). There are two\n# published versions, 0.210812.1515 and 0.250624.0419; they hold the same 22 assets (same asset ids,\n# sizes and modification dates) and differ only in dandiset metadata (contributor affiliations and\n# identifiers, a data curator, the related-resource record). The most recent published version is\n# pinned, as no earlier one matches the paper better.\n#\n# **Code.** The paper links no analysis code, and the dandiset links none. The NWB conversion code,\n# [catalystneuro/buzsaki-lab-to-nwb](https://github.com/catalystneuro/buzsaki-lab-to-nwb) at commit\n# 5f6a3750fffd999c4757d8a198cba6007f85fb12 (`buzsaki_lab_to_nwb/watson/`), was read: the state table\n# comes from each session's `SleepState.states.mat` with only WAKE, NREM and REM intervals, and the\n# units of Dino_072114 were read from a `spikes.cellinfo.mat` file with a hard-coded 20 kHz rate.\n#\n# | Claim | Tested or blocked |\n# |---|---|\n# | dataset-composition | tested |\n# | fig2a-median-rates | tested |\n# | fig2a-skewed-wide-distribution | tested |\n# | fig2a-fraction-above-2hz | tested |\n# | fig2b-wake-nrem-slope | tested |\n# | fig2-burst-index-by-state | tested |\n# | fig2c-acg-peaks | tested |\n# | fig2c-acg-decay | blocked: methods underspecified |\n# | fig2f-rate-group-correlations | tested |\n# | ma-statistics | tested |\n# | ma-fraction-over-nrem-episodes | tested |\n# | packet-duration | tested |\n# | wake-sleep-cycles | tested |\n# | fig3b-population-decline | tested |\n# | fig3-first-last-packet | tested |\n# | fig3d-first-last-slope | tested |\n# | fig3e-wake-before-after | tested |\n# | fig3b-sextiles-over-sleep | tested |\n# | fig3b-cv-over-sleep | tested |\n# | fig4iv-sextiles-within-nrem | tested |\n# | fig4v-cv-within-nrem | tested |\n# | fig4vi-burst-within-nrem | tested |\n# | fig4i-band-power-within-nrem | tested |\n# | fig4-delta-packet-length | tested |\n# | fig4cd-packet-rate-lfp | tested |\n# | fig5b-nrem-between-ma | tested |\n# | fig5b-wake-between-packets | tested |\n# | fig5b-ma-between-packets | tested |\n# | fig5b-rem-between-packets | tested |\n# | fig5c-rem-duration | tested |\n# | fig5c-sigma-ma | tested |\n# | fig5c-delta-change | tested |\n# | figs5-within-wake-rem | tested |\n# | fig5c-wake-movement | blocked: data missing |\n# | updown-durations | blocked: methods underspecified |\n# | fig3c-slow-oscillation-spindles-over-sleep | blocked: methods underspecified |\n# | fig4ii-iii-updown-spindles-within-packets | blocked: methods underspecified |\n# | fig2de-up-state-sequences | blocked: methods underspecified |\n# | fig3f-4e-within-up-rates | blocked: methods underspecified |\n#\n# The criteria for each claim are in `claims/000041/10.1016-j.neuron.2016.03.036.yaml`, written before\n# the analysis. The definitions used throughout (microarousals, packets, episodes, SLEEP, WAKE-SLEEP\n# cycles, sextiles, time courses) are in that file's opening comment and in `sleepstates.py`.\n\n# %%\nimport numpy as np\nimport pandas as pd\nimport scipy.stats as st\nimport matplotlib.pyplot as plt\n\nimport sleepstates as ss\n\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 30)\npd.set_option(\"display.max_rows\", 200)\n\n# Streams every usable file: units, states, and the LFP power of the reference channel in\n# Non-REM epochs. About two minutes with six processes.\nsessions, excluded = ss.load_all(workers=6)\nedges, sext = ss.wake_sextiles(sessions)\nprint(len(sessions), \"sessions loaded; excluded:\", excluded)\n\n# %% [markdown]\n# ## Data check\n\n# %% tags=[\"sanity\"]\nimport collections\nimport h5py, remfile\n\nurls = dict(ss.asset_urls())\nrows = []\nfor s in sessions:\n    dur = s.stops - s.starts\n    spk_all = np.concatenate([x for x in s.spikes if len(x)])\n    rows.append(dict(\n        subject=s.subject, session=s.session_id,\n        pE=int((s.cell_type == \"excitatory\").sum()), pI=int((s.cell_type == \"inhibitory\").sum()),\n        unknown=int((s.cell_type == \"unknown\").sum()),\n        states_min=round((s.stops[-1] - s.starts[0]) / 60, 1),\n        spikes_first=round(spk_all.min(), 2), spikes_last_min=round(spk_all.max() / 60, 1),\n        lfp_min=round(s.lfp_samples / ss.LFP_RATE / 60, 1),\n        WAKE_min=round(dur[s.state == \"WAKE\"].sum() / 60, 1), MA_n=int((s.state == \"MA\").sum()),\n        NREM_min=round(dur[s.state == \"NREM\"].sum() / 60, 1), REM_min=round(dur[s.state == \"REM\"].sum() / 60, 1),\n        epochs=len(s.labels), lfp_packets=len(s.lfp)))\ntab = pd.DataFrame(rows)\nprint(tab.to_string())\nprint(\"\\nTotals over the 21 usable sessions:\", tab[[\"pE\", \"pI\", \"unknown\", \"MA_n\"]].sum().to_dict())\nprint(\"Subjects:\", tab.subject.nunique(), \"| sessions per subject:\", tab.groupby(\"subject\").size().to_dict())\nprint(\"pE cells per subject:\", tab.groupby(\"subject\").pE.sum().to_dict())\nprint(\"State labels in the files:\", sorted(set(np.concatenate([s.labels for s in sessions]))))\n\n# Units, ranges and timing of what is used.\nfor s in sessions:\n    dur = s.stops - s.starts\n    assert np.all(np.diff(s.starts) > 0) and np.all(dur >= 0)\n    assert all(np.all(np.diff(x) >= 0) for x in s.spikes)\ngaps = np.concatenate([s.starts[1:] - s.stops[:-1] for s in sessions])\nallstart = np.concatenate([s.starts for s in sessions])\nprint(\"\\nState table: start times are whole seconds:\", bool(np.all(allstart == np.round(allstart))),\n      \"| gaps between consecutive epochs (s), values and counts:\",\n      dict(zip(*[x.tolist() for x in np.unique(gaps, return_counts=True)])))\nprint(\"State durations (s): min\", min((s.stops - s.starts).min() for s in sessions),\n      \"max\", max((s.stops - s.starts).max() for s in sessions))\nprint(\"Spikes after the end of the state table (fraction of spikes), per session:\",\n      {s.session_id: round(float(np.mean(np.concatenate(s.spikes) > s.stops[-1])), 3) for s in sessions})\nisi_viol = []\nfor s in sessions:\n    for u in s.pe:\n        x = s.spikes[u]\n        if len(x) > 1:\n            isi_viol.append(np.mean(np.diff(x) < 0.001))\nisi_viol = np.array(isi_viol)\nprint(\"pE units: fraction of intervals under 1 ms, median %.4f, 95th percentile %.4f, max %.4f\"\n      % (np.median(isi_viol), np.percentile(isi_viol, 95), isi_viol.max()))\nprint(\"pE spike counts per unit: min\", min(len(s.spikes[u]) for s in sessions for u in s.pe),\n      \"median\", int(np.median([len(s.spikes[u]) for s in sessions for u in s.pe])))\nprint(\"LFP reference column per session:\", {s.session_id: s.lfp_channel for s in sessions})\n\n# The excluded file: spike times are whole seconds divided by 20000.\np = list(excluded)[0]\nf = h5py.File(remfile.File(urls[p]), \"r\")\nt = f[\"units/spike_times\"][()]\nprint(\"\\n%s: %d spikes, %d distinct values, max %.4f s; max x 20000 = %.0f; times x 20000 all integers: %s;\"\n      \" LFP lasts %.0f s, states end at %.0f s\" % (\n          p, len(t), len(np.unique(t)), t.max(), t.max() * 20000, bool(np.all(np.round(t * 20000) == t * 20000)),\n          f[\"processing/ecephys/LFP/lfp/data\"].shape[0] / 1250, f[\"processing/behavior/states/stop_time\"][()].max()))\nprint(\"LFP data attributes: unit %r, conversion %r\" % (\n    f[\"processing/ecephys/LFP/lfp/data\"].attrs[\"unit\"], f[\"processing/ecephys/LFP/lfp/data\"].attrs[\"conversion\"]))\nel = f[\"general/extracellular_ephys/electrodes\"]\nprint(\"electrode location values:\", set(ss._str(el[\"location\"][()])),\n      \"| electrode group locations:\", sorted({f[\"general/extracellular_ephys\"][g].attrs.get(\"location\", \"\")\n                                             for g in f[\"general/extracellular_ephys\"] if g.startswith(\"shank\")}))\nprint(\"subject age, weight:\", f[\"general/subject/age\"][()], f[\"general/subject/weight\"][()])\n\n# Recordings deposited more than once: identical spike trains or state tables across files.\nsig_units = collections.defaultdict(list)\nfor s in sessions:\n    for u, x in enumerate(s.spikes):\n        if len(x) >= 5:\n            sig_units[(len(x), tuple(np.round(x[:5], 5)))].append((s.session_id, u))\ndups = [v for v in sig_units.values() if len({a for a, _ in v}) > 1]\nprint(\"\\nUnits with identical spike trains in different files:\", dups if dups else \"none\")\nst_sig = collections.defaultdict(list)\nfor s in sessions:\n    st_sig[(len(s.starts), tuple(s.starts[:10]), tuple(s.stops[-3:]))].append(s.session_id)\nprint(\"Identical state tables in different files:\", [v for v in st_sig.values() if len(v) > 1] or \"none\")\nsame_counts = collections.Counter(tuple(sorted(len(x) for x in s.spikes)) for s in sessions)\nprint(\"Files with identical sets of per-unit spike counts:\", [k for k, v in same_counts.items() if v > 1] or \"none\")\n\n# %% [markdown]\n# ### Do the spikes, the states and the LFP share one clock?\n#\n# The state labels are tested against the spikes by a contrast that an offset would destroy: the\n# fraction of 50 ms bins in which no pE cell fires (DOWN states make this high in Non-REM) in Non-REM\n# minus WAKE, with the state table shifted in time. If the clocks agree, the contrast is largest at\n# zero shift. The LFP is tested against the spikes inside Non-REM packets: the correlation between\n# each 2 s window's delta power and the pE spike count in the same window, with the spikes shifted.\n\n# %% tags=[\"sanity\"]\nshifts = np.array([-300, -120, -60, -20, -5, 0, 5, 20, 60, 120, 300])\nclock = []\nfor s in sessions:\n    pop = np.sort(np.concatenate([s.spikes[u] for u in s.pe]))\n    T = s.stops[-1]\n    edges50 = np.arange(0, T, 0.05)\n    silent = np.histogram(pop, edges50)[0] == 0\n    centres = edges50[:-1] + 0.025\n    row = {\"session\": s.session_id, \"pE\": len(s.pe)}\n    for d in shifts:\n        k = np.searchsorted(s.starts + d, centres, side=\"right\") - 1\n        ok = (k >= 0) & (centres < (s.stops + d)[np.clip(k, 0, None)])\n        lab = np.where(ok, s.state[np.clip(k, 0, None)], \"none\")\n        row[int(d)] = silent[lab == \"NREM\"].mean() - silent[lab == \"WAKE\"].mean()\n    # LFP against spikes, inside packets\n    xs, ys = [], []\n    for i, (tt, pw) in s.lfp.items():\n        xs.append(pw[\"delta\"])\n        ys.append(np.array([((pop >= c - 1) & (pop < c + 1)).sum() for c in tt]) if len(tt) else np.array([]))\n    x = np.concatenate(xs)\n    lag_r = {}\n    for d in [-10, -2, 0, 2, 10]:\n        yy = []\n        for i, (tt, pw) in s.lfp.items():\n            yy.append(counts_d := np.searchsorted(pop, tt + d + 1) - np.searchsorted(pop, tt + d - 1))\n        lag_r[d] = st.pearsonr(x, np.concatenate(yy))[0]\n    row.update({f\"lfp r lag {d}s\": round(v, 3) for d, v in lag_r.items()})\n    clock.append(row)\nclock = pd.DataFrame(clock)\nbest = clock[[int(d) for d in shifts]].idxmax(axis=1)\nprint(\"Contrast of silent-bin fraction, NREM minus WAKE, by shift of the state table (s):\")\nprint(clock.round(3).to_string())\nprint(\"\\nShift with the largest contrast, per session:\", best.tolist())\nprint(\"Sessions whose largest contrast is not within 5 s of zero shift:\", list(clock.session[best.abs() > 5]) or \"none\")\nprint(\"Sessions whose LFP-spike correlation is not most negative at lag 0:\",\n      [r.session for _, r in clock.iterrows()\n       if r[\"lfp r lag 0s\"] != min(r[f\"lfp r lag {d}s\"] for d in [-10, -2, 0, 2, 10])] or \"none\")\n\n# %% [markdown]\n# The data check against the description:\n#\n# - The dandiset description and the paper give 11 rats and 27 sessions; the files hold 10 rats\n#   (the archive's own summary says 10 subjects) and 22 sessions, one of which (Dino-072114) has\n#   unusable spike times. The description's unit counts (1360 recorded, 1121 stable, 995 pE, 126 pI)\n#   are those of the paper; the files hold 945 units: 826 excitatory, 96 inhibitory and 23 unknown.\n# - The state table has only Awake, Non-REM and REM, at 1 s resolution with 1 s gaps between epochs.\n#   Microarousals, which the paper scores as a state of their own, are not labelled; they are derived\n#   here from the Awake epochs under 40 s between two Non-REM epochs.\n# - LFP data are stored as int16 with unit \"volts\" and conversion NaN, so they cannot be put in volts;\n#   analyses use log power in raw units, normalized within session. The electrode `location` column\n#   is \"unknown\" for every electrode, while the electrode groups carry a region.\n# - Subject age and weight are the same range in every file (\"3-7 months\", \"250-500g\"); the dandiset\n#   description says 4-7 months and the paper 3-7 months.\n# - The clock checks above are printed per session; the outcome of each is stated in the summary.\n\n# %% [markdown]\n# ## dataset-composition\n#\n# > The recordings come from 11 rats and 27 sessions of 294 plus or minus 137 min, yielding 995\n# > putative pyramidal cells and 126 putative interneurons.\n\n# %% tags=[\"claim:dataset-composition\"]\nn_files = len(sessions) + len(excluded)\ndep = dict(rats=tab.subject.nunique(), sessions=n_files)\n# the excluded file's units are counted from its own table\nct_ex = collections.Counter(ss._str(f[\"units/cell_type\"][()]))\nst_ex = f[\"processing/behavior/states\"]\ndur_ex = (st_ex[\"stop_time\"][()].max() - st_ex[\"start_time\"][()].min()) / 60\ndurs = list(tab.states_min) + [dur_ex]\ndep.update(mean_duration_min=np.mean(durs), sd_duration_min=np.std(durs, ddof=1),\n           pE=int(tab.pE.sum() + ct_ex[\"excitatory\"]), pI=int(tab.pI.sum() + ct_ex[\"inhibitory\"]),\n           unknown=int(tab.unknown.sum() + ct_ex[\"unknown\"]))\nprint(\"As deposited (22 files):\", {k: (round(v, 1) if isinstance(v, float) else v) for k, v in dep.items()})\nprint(\"Usable (21 sessions): rats %d, sessions %d, pE %d, pI %d\" % (tab.subject.nunique(), len(tab), tab.pE.sum(), tab.pI.sum()))\nprint(\"Mean spike span of the usable sessions: %.1f min\" % tab.spikes_last_min.mean())\nexp = dict(rats=(11, 1.1), sessions=(27, 2.7), mean_duration_min=(294, 137), pE=(995, 99.5), pI=(126, 12.6))\nok = {k: abs(dep[k] - v) <= t for k, (v, t) in exp.items()}\nprint(\"Within tolerance:\", ok, \"->\", sum(ok.values()), \"of 5\")\nprint(\"pE cells per session: mean %.1f, range %d to %d (paper: mean 36.9, range 10 to 104)\" % (\n    tab.pE.mean(), tab.pE.min(), tab.pE.max()))\nprint(\"pI cells per session: mean %.2f, range %d to %d (paper: mean 4.67, range 0 to 13)\" % (\n    tab.pI.mean(), tab.pI.min(), tab.pI.max()))\n\n# %% [markdown]\n# ## fig2a-median-rates\n#\n# > Median firing rates of pE cells are 0.76 Hz in WAKE, 0.69 Hz in nonREM and 0.88 Hz in REM; of pI\n# > cells 5.59, 4.69 and 4.25 Hz.\n\n# %% tags=[\"claim:fig2a-median-rates\"]\ndef cell_table(wake_states):\n    out = []\n    for s in sessions:\n        for cls, units in ((\"pE\", s.pe), (\"pI\", s.pi)):\n            r = {lab: ss.state_rates(s, units, sts) for lab, sts in\n                 ((\"WAKE\", wake_states), (\"NREM\", [\"NREM\"]), (\"REM\", [\"REM\"]))}\n            for k, u in enumerate(units):\n                out.append(dict(subject=s.subject, session=s.session_id, unit=u, cls=cls,\n                                WAKE=r[\"WAKE\"][k], NREM=r[\"NREM\"][k], REM=r[\"REM\"][k]))\n    return pd.DataFrame(out)\n\ncells_a = cell_table([\"WAKE\"])\ncells_b = cell_table([\"WAKE\", \"MA\"])\nexpected = {(\"pE\", \"WAKE\"): 0.76, (\"pE\", \"NREM\"): 0.69, (\"pE\", \"REM\"): 0.88,\n            (\"pI\", \"WAKE\"): 5.59, (\"pI\", \"NREM\"): 4.69, (\"pI\", \"REM\"): 4.25}\nfor name, cells in ((\"(a) WAKE without MA\", cells_a), (\"(b) WAKE with MA\", cells_b)):\n    med = cells.groupby(\"cls\")[[\"WAKE\", \"NREM\", \"REM\"]].median()\n    sd = cells.groupby(\"cls\")[[\"WAKE\", \"NREM\", \"REM\"]].std()\n    n_in = sum(abs(med.loc[c, s_] - v) <= 0.1 * v for (c, s_), v in expected.items())\n    print(name, \"| medians (Hz):\\n\", med.round(3).to_string(), \"\\nSD:\\n\", sd.round(2).to_string(),\n          \"\\nwithin 10%:\", n_in, \"of 6\\n\")\nprint(\"n cells:\", cells_a.cls.value_counts().to_dict())\nprint(\"Per subject, pE medians (reading a):\")\nprint(cells_a[cells_a.cls == \"pE\"].groupby(\"subject\")[[\"WAKE\", \"NREM\", \"REM\"]].median().round(3).to_string())\nprint(\"\\nPer subject, pI medians (reading a):\")\nprint(cells_a[cells_a.cls == \"pI\"].groupby(\"subject\")[[\"WAKE\", \"NREM\", \"REM\"]].agg([\"median\", \"size\"]).round(2).to_string())\n\n# %% [markdown]\n# ## fig2a-skewed-wide-distribution\n#\n# > The distribution of pE firing rates is strongly positively skewed and spans three orders of\n# > magnitude, from 0.05 to 5 Hz.\n\n# %% tags=[\"claim:fig2a-skewed-wide-distribution\"]\npe_a = cells_a[cells_a.cls == \"pE\"]\nfor state in (\"WAKE\", \"NREM\", \"REM\"):\n    r = pe_a[state].values\n    lo, hi = np.percentile(r, [2.5, 97.5])\n    pos = r[r > 0]\n    print(\"%s: skewness %.2f, skewness of log10 (rates > 0) %.2f, 2.5th pct %.4f Hz, 97.5th pct %.3f Hz, \"\n          \"min %.4f, max %.2f, zero rates %d of %d\" % (state, st.skew(r), st.skew(np.log10(pos)), lo, hi,\n                                                        r.min(), r.max(), (r == 0).sum(), len(r)))\nr = pe_a.WAKE.values\nlo, hi = np.percentile(r, [2.5, 97.5])\nprint(\"\\nWAKE: skewness > 1:\", st.skew(r) > 1, \"| 2.5th pct within 0.025-0.1 Hz:\", 0.025 <= lo <= 0.1,\n      \"| 97.5th pct within 2.5-10 Hz:\", 2.5 <= hi <= 10)\nfig, ax = plt.subplots(figsize=(5, 3.5))\nfor state, c in ((\"WAKE\", \"k\"), (\"NREM\", \"tab:blue\"), (\"REM\", \"tab:red\")):\n    x = np.sort(pe_a[state].values)\n    x = x[x > 0]\n    ax.plot(x, np.arange(1, len(x) + 1) / len(x), color=c, label=state)\nfor e in edges[1:-1]:\n    ax.axvline(e, color=\"0.7\", lw=0.5)\nax.set_xscale(\"log\"); ax.set_xlabel(\"rate (Hz)\"); ax.set_ylabel(\"cumulative fraction of pE cells\"); ax.legend()\nax.set_title(\"pE rates by state (zero rates not drawn)\")\nplt.show()\nprint(\"Rates drawn: from %.4f to %.2f Hz; zero rates not drawn: WAKE %d, NREM %d, REM %d\" % (\n    min(pe_a[s_][pe_a[s_] > 0].min() for s_ in (\"WAKE\", \"NREM\", \"REM\")),\n    max(pe_a[s_].max() for s_ in (\"WAKE\", \"NREM\", \"REM\")),\n    (pe_a.WAKE == 0).sum(), (pe_a.NREM == 0).sum(), (pe_a.REM == 0).sum()))\nprint(\"WAKE-rate sextile edges (Hz):\", np.round(edges, 4))\n\n# %% [markdown]\n# ## fig2a-fraction-above-2hz\n#\n# > The fraction of pE cells firing above 2 Hz is 19.2% in WAKE, 19.2% in REM and 8.8% in nonREM\n# > (chi-square, p < 1e-10).\n\n# %% tags=[\"claim:fig2a-fraction-above-2hz\"]\nfrac = {s_: 100 * np.mean(pe_a[s_] > 2) for s_ in (\"WAKE\", \"REM\", \"NREM\")}\nprint(\"Percent of pE cells above 2 Hz:\", {k: round(v, 2) for k, v in frac.items()})\nfor other in (\"WAKE\", \"REM\"):\n    a = (pe_a.NREM > 2).sum(); b = (pe_a[other] > 2).sum(); n = len(pe_a)\n    chi2, p, _, _ = st.chi2_contingency([[a, n - a], [b, n - b]])\n    print(\"NREM against %s: chi2 = %.1f, p = %.2g\" % (other, chi2, p))\nprint(\"Within tolerance:\", {k: abs(frac[k] - v) <= 0.1 * v for k, v in ((\"WAKE\", 19.2), (\"REM\", 19.2), (\"NREM\", 8.8))})\nprint(\"\\nPer subject, percent above 2 Hz:\")\nprint((pe_a.groupby(\"subject\")[[\"WAKE\", \"REM\", \"NREM\"]].agg(lambda x: 100 * np.mean(x > 2))).round(1).to_string())\n\n# %% [markdown]\n# ## fig2b-wake-nrem-slope\n#\n# > Per-cell nonREM and WAKE rates are highly correlated (R = 0.82), and the slope of their relation\n# > is below 1 (95% confidence interval 0.66 to 0.71).\n\n# %% tags=[\"claim:fig2b-wake-nrem-slope\"]\ndef ols(x, y):\n    res = st.linregress(x, y)\n    t = st.t.ppf(0.975, len(x) - 2)\n    return res.slope, res.slope - t * res.stderr, res.slope + t * res.stderr, res.rvalue, res.pvalue, len(x)\n\nkeep = (pe_a.WAKE > 0) & (pe_a.NREM > 0)\nfits = {\"(a) log10\": ols(np.log10(pe_a.WAKE[keep]), np.log10(pe_a.NREM[keep])),\n        \"(b) Hz\": ols(pe_a.WAKE, pe_a.NREM),\n        \"(a) reverse, WAKE on NREM\": ols(np.log10(pe_a.NREM[keep]), np.log10(pe_a.WAKE[keep])),\n        \"(b) reverse\": ols(pe_a.NREM, pe_a.WAKE)}\nfor k, (b, lo, hi, r, p, n) in fits.items():\n    print(\"%s: slope %.3f (95%% CI %.3f to %.3f), R = %.3f, p = %.2g, n = %d\" % (k, b, lo, hi, r, p, n))\nprint(\"Dropped for zero rate in the log reading:\", (~keep).sum())\nfor k in (\"(a) log10\", \"(b) Hz\"):\n    b, lo, hi, r, p, n = fits[k]\n    print(k, \"| R within 0.738-0.902:\", 0.738 <= r <= 0.902, \"| slope within 0.594-0.781:\", 0.594 <= b <= 0.781,\n          \"| CI excludes 1:\", hi < 1)\nprint(\"\\nPer subject, reading (a):\")\nfor subj, g in pe_a[keep].groupby(\"subject\"):\n    b, lo, hi, r, p, n = ols(np.log10(g.WAKE), np.log10(g.NREM))\n    print(\"  %s: slope %.2f (%.2f to %.2f), R %.2f, n %d\" % (subj, b, lo, hi, r, n))\nfig, ax = plt.subplots(figsize=(4, 4))\nax.loglog(pe_a.WAKE[keep], pe_a.NREM[keep], \".\", ms=3)\nax.plot([1e-3, 30], [1e-3, 30], \"k--\", lw=0.8)\nax.set_xlabel(\"WAKE rate (Hz)\"); ax.set_ylabel(\"nonREM rate (Hz)\"); ax.set_title(\"pE cells\")\nplt.show()\nprint(\"Plotted: WAKE %.4f to %.2f Hz, NREM %.4f to %.2f Hz; %d cells with a zero rate not drawn\" % (\n    pe_a.WAKE[keep].min(), pe_a.WAKE[keep].max(), pe_a.NREM[keep].min(), pe_a.NREM[keep].max(), (~keep).sum()))\n\n# %% [markdown]\n# ## fig2-burst-index-by-state\n#\n# > The burst index (fraction of spikes with inter-spike intervals under 15 ms) is highest in\n# > nonREM (median 11.8%), lowest in WAKE (4.0%), with REM (5.5%) slightly above WAKE\n# > (Kruskal-Wallis, p < 0.05).\n\n# %% tags=[\"claim:fig2-burst-index-by-state\"]\nbi = []\nfor s in sessions:\n    for u in s.pe:\n        row = dict(subject=s.subject, session=s.session_id, unit=u)\n        for state in (\"WAKE\", \"NREM\", \"REM\"):\n            m = s.state == state\n            for rd in (\"a\", \"b\"):\n                row[f\"{state}_{rd}\"] = ss.burst_index(s.spikes[u], s.starts[m], s.stops[m], rd)\n        bi.append(row)\nbi = pd.DataFrame(bi)\nfor rd in (\"a\", \"b\"):\n    cols = [f\"{x}_{rd}\" for x in (\"NREM\", \"WAKE\", \"REM\")]\n    med = 100 * bi[cols].median()\n    h, p = st.kruskal(*[bi[c].dropna() for c in cols])\n    print(\"Reading (%s): medians %% NREM %.2f, WAKE %.2f, REM %.2f; n %s; Kruskal-Wallis H = %.1f, p = %.2g\" % (\n        rd, *med.values, bi[cols].notna().sum().to_dict(), h, p))\n    print(\"   within tolerance:\", [abs(m_ - v) <= 0.1 * v for m_, v in zip(med.values, (11.8, 4.0, 5.5))],\n          \"| order NREM > REM > WAKE:\", med.iloc[0] > med.iloc[2] > med.iloc[1])\n    pair = st.wilcoxon(bi[f\"REM_{rd}\"], bi[f\"WAKE_{rd}\"], nan_policy=\"omit\")\n    print(\"   REM against WAKE, paired Wilcoxon p = %.2g\" % pair.pvalue)\nprint(\"Cells left out for fewer than 10 intervals:\", bi[[f\"{x}_a\" for x in (\"NREM\", \"WAKE\", \"REM\")]].isna().sum().to_dict())\nprint(\"\\nPer subject, median burst index % (reading a):\")\nprint((100 * bi.groupby(\"subject\")[[\"NREM_a\", \"WAKE_a\", \"REM_a\"]].median()).round(2).to_string())\n\n# %% [markdown]\n# ## fig2c-acg-peaks\n#\n# > The average spike autocorrelogram of pE cells peaks near 8 ms in nonREM, with a smaller peak near\n# > 125 ms (theta) in REM and WAKE.\n\n# %% tags=[\"claim:fig2c-acg-peaks\"]\nacg = {state: [] for state in (\"NREM\", \"WAKE\", \"REM\")}\nfor s in sessions:\n    for u in s.pe:\n        for state in acg:\n            m = s.state == state\n            h, n = ss.autocorrelogram(s.spikes[u], s.starts[m], s.stops[m])\n            if n >= 100:\n                acg[state].append(h / n)\nlags = np.arange(300) + 0.5\nres = {}\nfor state, hs in acg.items():\n    mean = np.mean(hs, axis=0)\n    early = np.argmax(mean[2:50]) + 2\n    sm = np.convolve(mean, np.ones(21) / 21, mode=\"same\")\n    w = (lags >= 60) & (lags <= 250)\n    k = np.where(w)[0][np.argmax(sm[w])]\n    res[state] = (lags[early], lags[k], len(hs), k)\n    print(\"%s: cells %d; peak 2-50 ms at %.1f ms; smoothed maximum 60-250 ms at %.1f ms (%s the window edges)\" % (\n        state, len(hs), lags[early], lags[k], \"inside\" if 63 <= lags[k] <= 247 else \"at\"))\nprint(\"\\nNREM peak within 7-9 ms:\", 7 <= res[\"NREM\"][0] <= 9,\n      \"| theta peak within 112.5-137.5 ms in REM:\", 112.5 <= res[\"REM\"][1] <= 137.5,\n      \"and WAKE:\", 112.5 <= res[\"WAKE\"][1] <= 137.5)\nfig, ax = plt.subplots(1, 2, figsize=(9, 3))\nfor state, c in ((\"WAKE\", \"k\"), (\"NREM\", \"tab:blue\"), (\"REM\", \"tab:red\")):\n    mean = np.mean(acg[state], axis=0)\n    ax[0].plot(lags[:50], mean[:50], color=c, label=state)\n    ax[1].plot(lags[30:], np.convolve(mean, np.ones(21) / 21, mode=\"same\")[30:] / mean[30:].mean(), color=c)\nax[0].set_xlabel(\"lag (ms)\"); ax[0].set_ylabel(\"count per spike per ms\"); ax[0].legend()\nax[1].set_xlabel(\"lag (ms)\"); ax[1].set_ylabel(\"smoothed, relative to mean 30-300 ms\")\nplt.show()\nfor state in acg:\n    mean = np.mean(acg[state], axis=0)\n    print(\"%s mean ACG range 0-50 ms %.4f to %.4f; smoothed relative 30-300 ms %.3f to %.3f\" % (\n        state, mean[:50].min(), mean[:50].max(),\n        *(lambda v: (v.min(), v.max()))((np.convolve(mean, np.ones(21) / 21, mode=\"same\")[30:] / mean[30:].mean())[10:-10])))\nprint(\"\\nPer subject, NREM early peak (ms) and theta-window maximum in REM and WAKE (ms):\")\nfor subj in sorted(tab.subject.unique()):\n    out = []\n    for state in (\"NREM\", \"REM\", \"WAKE\"):\n        hs = []\n        for s in sessions:\n            if s.subject != subj:\n                continue\n            for u in s.pe:\n                m = s.state == state\n                h, n = ss.autocorrelogram(s.spikes[u], s.starts[m], s.stops[m])\n                if n >= 100:\n                    hs.append(h / n)\n        if not hs:\n            out.append(None); continue\n        mean = np.mean(hs, axis=0)\n        sm = np.convolve(mean, np.ones(21) / 21, mode=\"same\")\n        w = (lags >= 60) & (lags <= 250)\n        out.append(lags[np.argmax(mean[2:50]) + 2] if state == \"NREM\" else lags[np.where(w)[0][np.argmax(sm[w])]])\n    print(\"  %s: NREM %s, REM %s, WAKE %s\" % (subj, *out))\n\n# %% [markdown]\n# ## fig2f-rate-group-correlations\n#\n# > In nonREM, pairs of fast-firing pE cells are positively correlated, while pairs of one slow and\n# > one fast cell are negatively correlated.\n\n# %% tags=[\"claim:fig2f-rate-group-correlations\"]\n# sextiles of the whole-session rate, reading (b)\nwhole = {s.path: np.array([len(s.spikes[u]) / (s.stops[-1] - s.starts[0]) for u in s.pe]) for s in sessions}\nedges_b = np.quantile(np.concatenate(list(whole.values())), np.linspace(0, 1, 7))\ngroups_b = {p: np.searchsorted(edges_b[1:-1], r, side=\"right\") + 1 for p, r in whole.items()}\npairs = []\nfor s in sessions:\n    m = s.state == \"NREM\"\n    binned = []\n    for a, b in zip(s.starts[m], s.stops[m]):\n        e = np.arange(a, b, 0.1)\n        if len(e) > 1:\n            binned.append(np.array([np.diff(np.searchsorted(s.spikes[u], e)) for u in s.pe]))\n    X = np.concatenate(binned, axis=1)\n    C = np.corrcoef(X)\n    ga, gb = sext[s.path][1], groups_b[s.path]\n    iu = np.triu_indices(len(s.pe), 1)\n    for i, j in zip(*iu):\n        if np.isfinite(C[i, j]):\n            pairs.append(dict(subject=s.subject, session=s.session_id, r=C[i, j],\n                              a=tuple(sorted((ga[i], ga[j]))), b=tuple(sorted((gb[i], gb[j])))))\npairs = pd.DataFrame(pairs)\nprint(\"pairs:\", len(pairs), \"| overall mean r %.4f, fraction negative %.3f\" % (pairs.r.mean(), np.mean(pairs.r < 0)))\nfor rd in (\"a\", \"b\"):\n    g = pairs.groupby(rd).r.agg([\"mean\", \"size\"])\n    mat = np.full((6, 6), np.nan)\n    for (i, j), v in g[\"mean\"].items():\n        mat[i - 1, j - 1] = mat[j - 1, i - 1] = v\n    print(\"\\nReading (%s), mean r by group pair (rows and columns: groups 1 to 6):\" % rd)\n    print(pd.DataFrame(mat, index=range(1, 7), columns=range(1, 7)).round(4).to_string())\n    r16 = pairs[pairs[rd] == (1, 6)].r\n    t = st.ttest_1samp(r16, 0)\n    top = g[\"mean\"].idxmax()\n    print(\"(6,6) mean %.4f, largest pair is %s; (1,6) mean %.4f, n %d, t = %.2f, p = %.2g\" % (\n        g[\"mean\"][(6, 6)], top, r16.mean(), len(r16), t.statistic, t.pvalue))\nprint(\"\\nPer subject, reading (a): mean r of (6,6) and (1,6) pairs\")\nprint(pairs.groupby([\"subject\", \"a\"]).r.mean().unstack()[[(6, 6), (1, 6)]].round(4).to_string())\n\n# %% [markdown]\n# ## ma-statistics\n#\n# > Microarousals have a median duration of 15.9 plus or minus 3.3 s, occur 0.32 plus or minus 0.12\n# > times per minute and occupy 9.1 plus or minus 3.5% of SLEEP (790 in total).\n\n# %% tags=[\"claim:ma-statistics\"]\nrows = []\nall_ma = []\nep_time = ep_ma_n = 0\nfor s in sessions:\n    dur = s.stops - s.starts\n    all_ma.append(dur[s.state == \"MA\"])\n    periods = ss.sleep_periods(s.starts, s.stops, s.labels)\n    n = T = tma = 0\n    durs_in = []\n    for p_ in periods:\n        rr = np.arange(p_[\"first\"], p_[\"last\"] + 1)\n        ma = rr[s.state[rr] == \"MA\"]\n        n += len(ma); tma += dur[ma].sum(); T += p_[\"stop\"] - p_[\"start\"]; durs_in += list(dur[ma])\n    for a, b in ss.nrem_episodes(s.state):\n        ep_time += s.stops[b] - s.starts[a]\n        ep_ma_n += int(np.sum(s.state[a:b + 1] == \"MA\"))\n    rows.append(dict(subject=s.subject, session=s.session_id, periods=len(periods), MA_in_sleep=n,\n                     sleep_min=T / 60, freq=n / (T / 60) if T else np.nan, frac=100 * tma / T if T else np.nan,\n                     durs=durs_in))\nma = pd.DataFrame(rows)\nin_durs = np.concatenate([np.array(x, float) for x in ma.durs])\nall_ma = np.concatenate(all_ma)\nprint(ma.drop(columns=\"durs\").round(3).to_string())\na = (np.median(in_durs), ma.freq.mean(), ma.frac.mean())\nb = (np.median(all_ma), ep_ma_n / (ep_time / 60), 100 * all_ma.sum() / ep_time)\nfor name, v in ((\"(a) inside SLEEP, per-session means\", a), (\"(b) all MAs, pooled, per nonREM episode time\", b)):\n    ok = [abs(v[0] - 15.9) <= 3.3, abs(v[1] - 0.32) <= 0.12, abs(v[2] - 9.1) <= 3.5]\n    print(\"%s: median duration %.1f s, frequency %.3f per min, fraction %.2f%%; within tolerance %s\" % (name, *v, ok))\nprint(\"SD over sessions (a): frequency %.3f, fraction %.2f\" % (ma.freq.std(), ma.frac.std()))\nprint(\"MAs: %d in all, %d inside SLEEP periods (paper: 790 in 27 sessions)\" % (len(all_ma), len(in_durs)))\nprint(\"MA durations (s): min %.0f, max %.0f; the state table has 1 s resolution\" % (all_ma.min(), all_ma.max()))\nprint(\"Awake epochs under 40 s not between two Non-REM epochs (left as WAKE):\",\n      sum(int(np.sum((s.labels == \"Awake\") & (s.stops - s.starts < 40) & (s.state == \"WAKE\"))) for s in sessions))\n\n# %% [markdown]\n# ## ma-fraction-over-nrem-episodes\n#\n# > The fraction of time occupied by MAs decreases over the course of nonREM episodes (R = -0.85,\n# > p < 1e-10).\n\n# %% tags=[\"claim:ma-fraction-over-nrem-episodes\"]\nfr = []\nfor s in sessions:\n    for a, b in ss.nrem_episodes(s.state):\n        rr = np.arange(a, b + 1)\n        mas = [(s.starts[i], s.stops[i]) for i in rr if s.state[i] == \"MA\"]\n        if not mas:\n            continue\n        bins = ss.binned_intervals(s.starts[a], s.stops[b], 10, mas)\n        width = (s.stops[b] - s.starts[a]) / 10\n        fr.append([np.sum(e - st_) / width for st_, e in bins])\nfr = np.array(fr)\nx = np.tile(np.arange(10) + 0.5, len(fr))\nra = st.pearsonr(np.arange(10) + 0.5, fr.mean(axis=0))\nrb = st.pearsonr(x, fr.ravel())\nprint(\"Episodes with at least one MA:\", len(fr))\nprint(\"Mean MA fraction per bin:\", np.round(fr.mean(axis=0), 4))\nprint(\"(a) bin means: R = %.3f, p = %.2g | (b) pooled: R = %.3f, p = %.2g\" % (ra[0], ra[1], rb[0], rb[1]))\nprint(\"Within -0.935 to -0.765:\", {\"a\": -0.935 <= ra[0] <= -0.765, \"b\": -0.935 <= rb[0] <= -0.765})\n# the first and last bins start and end in a packet by construction\nprint(\"Variant without the first and last bins: (a) R = %.3f, p = %.2g\" % st.pearsonr(np.arange(1, 9) + 0.5, fr.mean(axis=0)[1:-1]))\n\n# %% [markdown]\n# ## packet-duration\n#\n# > The duration of nonREM packets spans two orders of magnitude, with a median of 111 s.\n\n# %% tags=[\"claim:packet-duration\"]\npa, pb = [], []\nfor s in sessions:\n    dur = s.stops - s.starts\n    pa.append(dur[s.state == \"NREM\"])\n    for p_ in ss.sleep_periods(s.starts, s.stops, s.labels):\n        rr = np.arange(p_[\"first\"], p_[\"last\"] + 1)\n        pb.append(dur[rr][s.state[rr] == \"NREM\"])\npa, pb = np.concatenate(pa), np.concatenate(pb)\nfor name, v in ((\"(a) all\", pa), (\"(b) inside SLEEP\", pb)):\n    print(\"%s: n %d, median %.1f s, 5th to 95th pct %.0f to %.0f s, min %.0f, max %.0f; within 99.9-122.1: %s\" % (\n        name, len(v), np.median(v), *np.percentile(v, [5, 95]), v.min(), v.max(), 99.9 <= np.median(v) <= 122.1))\nprint(\"Per subject median (a):\", {subj: float(np.median(np.concatenate([(s.stops - s.starts)[s.state == \"NREM\"]\n      for s in sessions if s.subject == subj]))) for subj in sorted(tab.subject.unique())})\n\n# %% [markdown]\n# ## wake-sleep-cycles\n#\n# > The dataset holds 54 WAKE-SLEEP episodes, an average of 2.0 per session, and sessions without one\n# > were discarded.\n\n# %% tags=[\"claim:wake-sleep-cycles\"]\ncyc = {s.path: ss.cycles(s) for s in sessions}\ncyc_open = {s.path: ss.cycles(s, require_wake_end=False) for s in sessions}\nnc = pd.Series({s.session_id: len(cyc[s.path]) for s in sessions})\nnco = pd.Series({s.session_id: len(cyc_open[s.path]) for s in sessions})\nprint(pd.DataFrame({\"cycles\": nc, \"cycles incl. SLEEP ended by the recording\": nco}).to_string())\nprint(\"Total %d, mean per session %.2f, sessions with none: %d | variant: total %d, mean %.2f, none: %d\" % (\n    nc.sum(), nc.mean(), (nc == 0).sum(), nco.sum(), nco.mean(), (nco == 0).sum()))\nprint(\"Within 1.8-2.2:\", 1.8 <= nc.mean() <= 2.2)\npw = [s.stops[p_[\"pre\"]] - s.starts[p_[\"pre\"]] for s in sessions for p_ in cyc[s.path]]\nsl = [(p_[\"stop\"] - p_[\"start\"]) / 60 for s in sessions for p_ in cyc[s.path]]\nprint(\"Pre-sleep WAKE (min): %.1f to %.1f; SLEEP duration (min): median %.1f, range %.1f to %.1f\" % (\n    min(pw) / 60, max(pw) / 60, np.median(sl), min(sl), max(sl)))\n\n# %% [markdown]\n# ## fig3b-population-decline\n#\n# > The mean firing rate of pE cells declines over the course of SLEEP, restricted to nonREM\n# > (R = -0.11, p < 1e-3).\n\n# %% tags=[\"claim:fig3b-population-decline\"]\ndef group_mean(rmat, units_mask):\n    \"\"\"Mean over the cells in the mask, cells with no spikes over the whole interval dropped,\n    divided by its mean over the points; None when undefined.\"\"\"\n    sub = rmat[units_mask]\n    sub = sub[np.nansum(sub, axis=1) > 0]\n    if len(sub) == 0:\n        return None\n    m = np.nanmean(sub, axis=0)\n    mu = np.nanmean(m)\n    return m / mu if mu > 0 else None\n\ndef sleep_points(nbins=10, min_nrem=10.0):\n    \"\"\"Per cycle and reading: x, rate matrix (pE x points), session path.\"\"\"\n    out = {\"a\": [], \"b\": []}\n    for s in sessions:\n        for p_ in cyc[s.path]:\n            rr = np.arange(p_[\"first\"], p_[\"last\"] + 1)\n            pk = rr[s.state[rr] == \"NREM\"]\n            T = p_[\"stop\"] - p_[\"start\"]\n            xa = ((s.starts[pk] + s.stops[pk]) / 2 - p_[\"start\"]) / T\n            ra = np.array([[ss.counts(s.spikes[u], s.starts[i], s.stops[i]) / (s.stops[i] - s.starts[i]) for i in pk] for u in s.pe])\n            out[\"a\"].append((xa, ra, s))\n            bins = ss.binned_intervals(p_[\"start\"], p_[\"stop\"], nbins, list(zip(s.starts[pk], s.stops[pk])))\n            rb, dur = ss.bin_rates(s, s.pe, bins)\n            ok = dur >= min_nrem\n            out[\"b\"].append(((np.arange(nbins) + 0.5)[ok] / nbins, rb[:, ok], s))\n    return out\n\npts = sleep_points()\n\ndef pooled_r(pts_r, groups=None):\n    \"\"\"Pooled Pearson R of normalized group means against x. groups None = all pE cells.\"\"\"\n    xs, ys = [], []\n    for x, rmat, s in pts_r:\n        mask = np.ones(len(s.pe), bool) if groups is None else np.isin(sext[s.path][1], groups)\n        v = group_mean(rmat, mask)\n        if v is not None:\n            xs.append(x); ys.append(v)\n    x, y = np.concatenate(xs), np.concatenate(ys)\n    ok = np.isfinite(y)\n    r, p = st.pearsonr(x[ok], y[ok])\n    return r, p, ok.sum()\n\nfor rd in (\"a\", \"b\"):\n    r, p, n = pooled_r(pts[rd])\n    print(\"Reading (%s): R = %.3f, p = %.2g, points %d; within -0.121 to -0.099: %s\" % (rd, r, p, n, -0.121 <= r <= -0.099))\nprint(\"\\nPer subject, reading (a):\")\nfor subj in sorted(tab.subject.unique()):\n    sub = [t_ for t_ in pts[\"a\"] if t_[2].subject == subj]\n    if sub:\n        r, p, n = pooled_r(sub)\n        print(\"  %s: R = %.3f, p = %.2g, points %d, cycles %d\" % (subj, r, p, n, len(sub)))\n\n# %% [markdown]\n# ## fig3-first-last-packet\n#\n# > The mean pE rate is lower in the last than in the first nonREM packet of SLEEP (1.04 plus or minus\n# > 1.20 against 0.88 plus or minus 0.91 Hz; Wilcoxon p < 0.02).\n\n# %% tags=[\"claim:fig3-first-last-packet\"]\nfl = []\nfor s in sessions:\n    for c, p_ in enumerate(cyc[s.path]):\n        rr = np.arange(p_[\"first\"], p_[\"last\"] + 1)\n        pk = rr[s.state[rr] == \"NREM\"]\n        r1 = ss.rates(s.spikes, s.pe, s.starts[pk[0]], s.stops[pk[0]])\n        r2 = ss.rates(s.spikes, s.pe, s.starts[pk[-1]], s.stops[pk[-1]])\n        for k, u in enumerate(s.pe):\n            fl.append(dict(subject=s.subject, session=s.session_id, cycle=c, unit=u, first=r1[k], last=r2[k],\n                           sextile=sext[s.path][1][k], first_dur=s.stops[pk[0]] - s.starts[pk[0]],\n                           last_dur=s.stops[pk[-1]] - s.starts[pk[-1]],\n                           first_half=ss.rates(s.spikes, [u], s.starts[pk[0]], (s.starts[pk[0]] + s.stops[pk[0]]) / 2)[0],\n                           second_half=ss.rates(s.spikes, [u], (s.starts[pk[0]] + s.stops[pk[0]]) / 2, s.stops[pk[0]])[0]))\nfl = pd.DataFrame(fl)\nw = st.wilcoxon(fl[\"first\"], fl[\"last\"])\nprint(\"cell-cycle pairs %d (cycles %d); first %.3f +- %.3f Hz, last %.3f +- %.3f Hz; Wilcoxon p = %.2g; last lower: %s\" % (\n    len(fl), fl.groupby([\"session\", \"cycle\"]).ngroups, fl[\"first\"].mean(), fl[\"first\"].std(), fl[\"last\"].mean(),\n    fl[\"last\"].std(), w.pvalue, fl[\"last\"].mean() < fl[\"first\"].mean()))\nprint(\"Within tolerance: first\", abs(fl[\"first\"].mean() - 1.04) <= 0.104, \"last\", abs(fl[\"last\"].mean() - 0.88) <= 0.088)\nprint(\"Medians: first %.3f, last %.3f; first packet duration median %.0f s, last %.0f s\" % (\n    fl[\"first\"].median(), fl[\"last\"].median(), fl.groupby([\"session\", \"cycle\"]).first_dur.first().median(),\n    fl.groupby([\"session\", \"cycle\"]).last_dur.first().median()))\nprint(\"\\nPer subject:\")\nfor subj, g in fl.groupby(\"subject\"):\n    print(\"  %s: first %.3f, last %.3f, n %d, Wilcoxon p = %.2g\" % (subj, g[\"first\"].mean(), g[\"last\"].mean(), len(g),\n                                                                    st.wilcoxon(g[\"first\"], g[\"last\"]).pvalue))\n\n# %% [markdown]\n# ## fig3d-first-last-slope\n#\n# > Comparing the same neurons in the first and last nonREM packets of SLEEP, the regression slope\n# > departs from 1 (95% confidence interval 0.827 to 0.880).\n\n# %% tags=[\"claim:fig3d-first-last-slope\"]\nk2 = (fl[\"first\"] > 0) & (fl[\"last\"] > 0)\nfits = {\"(a) log10, last on first\": ols(np.log10(fl[\"first\"][k2]), np.log10(fl[\"last\"][k2])),\n        \"(b) Hz, last on first\": ols(fl[\"first\"], fl[\"last\"]),\n        \"(a) reverse, first on last\": ols(np.log10(fl[\"last\"][k2]), np.log10(fl[\"first\"][k2]))}\nk3 = (fl.first_half > 0) & (fl.second_half > 0)\nfits[\"check: second half on first half of the first packet, log10\"] = ols(np.log10(fl.first_half[k3]), np.log10(fl.second_half[k3]))\nfor k, (b, lo, hi, r, p, n) in fits.items():\n    print(\"%s: slope %.3f (95%% CI %.3f to %.3f), R = %.3f, n = %d\" % (k, b, lo, hi, r, n))\nprint(\"Pairs dropped for a zero rate (a): %d\" % (~k2).sum())\nfor k in (\"(a) log10, last on first\", \"(b) Hz, last on first\"):\n    b, lo, hi = fits[k][:3]\n    print(k, \"| slope within 0.744-0.968:\", 0.744 <= b <= 0.968, \"| CI excludes 1:\", hi < 1)\n\n# %% [markdown]\n# ## fig3e-wake-before-after\n#\n# > pE rates are lower in the 5 min of WAKE after SLEEP than in the 5 min before (p < 1e-6,\n# > Wilcoxon), with a decrease in the top three sextiles and an increase in the lowest.\n\n# %% tags=[\"claim:fig3e-wake-before-after\"]\nba = []\nfor s in sessions:\n    for c, p_ in enumerate(cyc[s.path]):\n        pre, post = p_[\"pre\"], p_[\"post\"]\n        r1 = ss.rates(s.spikes, s.pe, s.stops[pre] - 300, s.stops[pre])\n        r2 = ss.rates(s.spikes, s.pe, s.starts[post], min(s.starts[post] + 300, s.stops[post]))\n        for k, u in enumerate(s.pe):\n            ba.append(dict(subject=s.subject, session=s.session_id, cycle=c, unit=u, pre=r1[k], post=r2[k],\n                           sextile=sext[s.path][1][k], post_len=min(300, s.stops[post] - s.starts[post])))\nba = pd.DataFrame(ba)\nprint(\"Post-sleep WAKE windows shorter than 300 s: %d of %d cycles\" % (\n    (ba.groupby([\"session\", \"cycle\"]).post_len.first() < 300).sum(), ba.groupby([\"session\", \"cycle\"]).ngroups))\nfor rd, d in ((\"(a) cell-cycle pairs\", ba),\n              (\"(b) per-cell means\", ba.groupby([\"session\", \"unit\"]).agg(pre=(\"pre\", \"mean\"), post=(\"post\", \"mean\"),\n                                                                         sextile=(\"sextile\", \"first\")).reset_index())):\n    w = st.wilcoxon(d.pre, d.post)\n    print(\"\\n%s: n %d, mean pre %.3f, post %.3f Hz, median change %.4f, Wilcoxon p = %.2g\" % (\n        rd, len(d), d.pre.mean(), d.post.mean(), (d.post - d.pre).median(), w.pvalue))\n    for g in range(1, 7):\n        x = d[d.sextile == g]\n        alt = \"greater\" if g == 1 else \"less\"\n        pv = st.wilcoxon(x.post, x.pre, alternative=alt).pvalue\n        print(\"  sextile %d: n %d, mean pre %.3f, post %.3f, mean change %+.3f, one-tailed (%s) p = %.2g\" % (\n            g, len(x), x.pre.mean(), x.post.mean(), (x.post - x.pre).mean(), \"increase\" if g == 1 else \"decrease\", pv))\nprint(\"\\nPer subject, (a): mean change post - pre (Hz) for all pE, sextile 1 and sextile 6\")\nprint(ba.assign(ch=ba.post - ba.pre).groupby(\"subject\").apply(\n    lambda g: pd.Series({\"all\": g.ch.mean(), \"s1\": g.ch[g.sextile == 1].mean(), \"s6\": g.ch[g.sextile == 6].mean(), \"n\": len(g)}),\n    include_groups=False).round(3).to_string())\n\n# %% [markdown]\n# ## fig3b-sextiles-over-sleep\n#\n# > Over SLEEP, restricted to nonREM, the fastest sextile decreases its rate while the slowest shows\n# > a marginal increase.\n\n# %% tags=[\"claim:fig3b-sextiles-over-sleep\"]\nfor rd in (\"a\", \"b\"):\n    print(\"Reading (%s):\" % rd)\n    for g in range(1, 7):\n        r, p, n = pooled_r(pts[rd], [g])\n        print(\"  sextile %d: R = %+.3f, p = %.2g, points %d\" % (g, r, p, n))\nprint(\"\\nPer subject, reading (a), sextiles 1 and 6:\")\nfor subj in sorted(tab.subject.unique()):\n    sub = [t_ for t_ in pts[\"a\"] if t_[2].subject == subj]\n    if sub:\n        out = []\n        for g in (1, 6):\n            try:\n                out.append(\"%+.3f (p %.2g)\" % pooled_r(sub, [g])[:2])\n            except ValueError:\n                out.append(\"n/a\")\n        print(\"  %s: sextile 1 %s, sextile 6 %s\" % (subj, *out))\n\n# %% [markdown]\n# ## fig3b-cv-over-sleep\n#\n# > The coefficient of variation of pE firing rates decreases over the course of SLEEP (R = -0.05,\n# > p < 0.01).\n\n# %% tags=[\"claim:fig3b-cv-over-sleep\"]\nfor rd in (\"a\", \"b\"):\n    xs, ys = [], []\n    for x, rmat, s in pts[rd]:\n        mu = rmat.mean(axis=0); sd = rmat.std(axis=0)\n        ok = mu > 0\n        xs.append(x[ok]); ys.append(sd[ok] / mu[ok])\n    r, p = st.pearsonr(np.concatenate(xs), np.concatenate(ys))\n    print(\"Reading (%s): R = %.3f, p = %.2g, points %d\" % (rd, r, p, len(np.concatenate(xs))))\n\n# %% [markdown]\n# ## Time courses within nonREM packets and episodes\n#\n# The next claims use the same time courses: 10 bins of normalized time within packets of at least\n# 20 s and within nonREM episodes of at least 20 s (Non-REM time only).\n\n# %%\ndef intervals_of(kind, min_dur=20.0):\n    \"\"\"(session, span start, span stop, included intervals) for packets, episodes, WAKE or REM epochs.\"\"\"\n    out = []\n    for s in sessions:\n        if kind in (\"packet\", \"WAKE\", \"REM\"):\n            lab = \"NREM\" if kind == \"packet\" else kind\n            for i in np.where(s.state == lab)[0]:\n                if s.stops[i] - s.starts[i] >= min_dur:\n                    out.append((s, s.starts[i], s.stops[i], None, [i]))\n        else:\n            for a, b in ss.nrem_episodes(s.state):\n                if s.stops[b] - s.starts[a] >= min_dur:\n                    rows_ = [i for i in range(a, b + 1) if s.state[i] == \"NREM\"]\n                    out.append((s, s.starts[a], s.stops[b], [(s.starts[i], s.stops[i]) for i in rows_], rows_))\n    return out\n\ndef course(kind, nbins=10, min_dur=20.0):\n    \"\"\"Per interval: bin centres, pE rate matrix, burst counts per bin (short, all), session.\"\"\"\n    res = []\n    for s, a, b, inc, rows_ in intervals_of(kind, min_dur):\n        bins = ss.binned_intervals(a, b, nbins, inc)\n        rmat, dur = ss.bin_rates(s, s.pe, bins)\n        ok = dur > 0\n        # burst: intervals within the same packet (or epoch), later spike binned\n        pk_s = np.array([s.starts[i] for i in rows_]); pk_e = np.array([s.stops[i] for i in rows_])\n        short = np.zeros(nbins); alln = np.zeros(nbins)\n        for u in s.pe:\n            isi, t2, _ = ss.isis_in(s.spikes[u], pk_s, pk_e)\n            k = np.clip(((t2 - a) / (b - a) * nbins).astype(int), 0, nbins - 1)\n            alln += np.bincount(k, minlength=nbins)\n            short += np.bincount(k[isi < ss.BURST_ISI], minlength=nbins)\n        x = (np.arange(nbins) + 0.5) / nbins\n        res.append((x[ok], rmat[:, ok], s, short[ok], alln[ok]))\n    return res\n\ncourses = {k: course(k) for k in (\"episode\", \"packet\")}\nprint({k: len(v) for k, v in courses.items()}, \"intervals\")\nprint(\"Packets of at least 20 s by subject:\", collections.Counter(c[2].subject for c in courses[\"packet\"]))\n\n# %% [markdown]\n# ## fig4iv-sextiles-within-nrem\n#\n# > Within both nonREM episodes and nonREM packets, the fastest sextiles decrease their rates while\n# > the slowest increase.\n\n# %% tags=[\"claim:fig4iv-sextiles-within-nrem\"]\ndef sextile_table(cs):\n    out = {}\n    for g in range(1, 7):\n        out[g] = pooled_r([(x, r, s) for x, r, s, *_ in cs], [g])\n    out[\"all pE\"] = pooled_r([(x, r, s) for x, r, s, *_ in cs], None)\n    return out\n\nfor kind in (\"episode\", \"packet\"):\n    t = sextile_table(courses[kind])\n    print(\"%s: \" % kind + \"; \".join(\"%s R = %+.3f (p %.2g)\" % ((\"sextile %d\" % g) if g != \"all pE\" else g, v[0], v[1])\n                                     for g, v in t.items()))\nprint(\"\\nVariants (sextile 1 and sextile 6 R, p):\")\nfor kind in (\"episode\", \"packet\"):\n    for nb, md in ((5, 20.0), (20, 20.0), (10, 60.0)):\n        t = sextile_table(course(kind, nb, md))\n        print(\"  %s, %d bins, min %d s: s1 %+.3f (p %.2g), s6 %+.3f (p %.2g)\" % (kind, nb, md, *t[1][:2], *t[6][:2]))\nprint(\"\\nPer subject, packets, sextile 1 and 6:\")\nfor subj in sorted(tab.subject.unique()):\n    cs = [c for c in courses[\"packet\"] if c[2].subject == subj]\n    out = []\n    for g in (1, 6):\n        try:\n            out.append(\"%+.3f (p %.2g, n %d)\" % pooled_r([(x, r, s) for x, r, s, *_ in cs], [g]))\n        except ValueError:\n            out.append(\"n/a\")\n    print(\"  %s: s1 %s, s6 %s\" % (subj, *out))\nfig, ax = plt.subplots(1, 2, figsize=(9, 3), sharey=True)\nfor j, kind in enumerate((\"episode\", \"packet\")):\n    for g, c in zip(range(1, 7), plt.cm.viridis(np.linspace(0, 1, 6))):\n        vals = []\n        for x, r, s, *_ in courses[kind]:\n            if len(x) == 10:\n                v = group_mean(r, sext[s.path][1] == g)\n                if v is not None:\n                    vals.append(v)\n        m = np.nanmean(vals, axis=0)\n        ax[j].plot(np.arange(10) + 0.5, m, color=c, label=f\"sextile {g}\")\n        print(\"%s, sextile %d: mean normalized rate per bin from %.3f to %.3f\" % (kind, g, np.nanmin(m), np.nanmax(m)))\n    ax[j].set_title(kind); ax[j].set_xlabel(\"normalized time (bin)\")\nax[0].set_ylabel(\"rate / interval mean\"); ax[1].legend(fontsize=7)\nplt.show()\n\n# %% [markdown]\n# ## fig4v-cv-within-nrem\n#\n# > The coefficient of variation of binned population rates decreases within nonREM episodes\n# > (R = -0.13) and packets (R = -0.12), both p < 1e-10.\n\n# %% tags=[\"claim:fig4v-cv-within-nrem\"]\ndef cv_r(cs):\n    xs, ys = [], []\n    for x, r, s, *_ in cs:\n        mu, sd = r.mean(axis=0), r.std(axis=0)\n        ok = mu > 0\n        xs.append(x[ok]); ys.append(sd[ok] / mu[ok])\n    return st.pearsonr(np.concatenate(xs), np.concatenate(ys)) + (len(np.concatenate(xs)),)\n\nfor kind in (\"episode\", \"packet\"):\n    r, p, n = cv_r(courses[kind])\n    print(\"%s: R = %.3f, p = %.2g, points %d\" % (kind, r, p, n))\n    for nb, md in ((5, 20.0), (20, 20.0), (10, 60.0)):\n        print(\"   variant %d bins, min %d s: R = %.3f, p = %.2g, points %d\" % (nb, md, *cv_r(course(kind, nb, md))))\n\n# %% [markdown]\n# ## fig4vi-burst-within-nrem\n#\n# > The 15 ms burst index of pE cells increases within nonREM episodes (R = 0.09) and packets\n# > (R = 0.08), both p < 1e-10.\n\n# %% tags=[\"claim:fig4vi-burst-within-nrem\"]\ndef burst_r(cs):\n    xs, ys = [], []\n    for x, r, s, short, alln in cs:\n        ok = alln > 0\n        xs.append(x[ok]); ys.append(short[ok] / alln[ok])\n    return st.pearsonr(np.concatenate(xs), np.concatenate(ys)) + (len(np.concatenate(xs)),)\n\nfor kind in (\"episode\", \"packet\"):\n    r, p, n = burst_r(courses[kind])\n    print(\"%s: R = %.3f, p = %.2g, points %d\" % (kind, r, p, n))\n    for nb, md in ((5, 20.0), (20, 20.0), (10, 60.0)):\n        print(\"   variant %d bins, min %d s: R = %.3f, p = %.2g, points %d\" % (nb, md, *burst_r(course(kind, nb, md))))\n\n# %% [markdown]\n# ## fig4i-band-power-within-nrem\n#\n# > Delta and sigma power increase over nonREM episodes and packets, while gamma power decreases over\n# > episodes but not over packets.\n\n# %% tags=[\"claim:fig4i-band-power-within-nrem\"]\ndef lfp_course(kind, nbins=10, min_dur=20.0):\n    out = {b: ([], []) for b in ss.BANDS}\n    for s, a, b, inc, rows_ in intervals_of(kind, min_dur):\n        rows_ = [i for i in rows_ if i in s.lfp]\n        if not rows_:\n            continue\n        t = np.concatenate([s.lfp[i][0] for i in rows_])\n        k = np.clip(((t - a) / (b - a) * nbins).astype(int), 0, nbins - 1)\n        for band in ss.BANDS:\n            v = np.concatenate([s.lfp[i][1][band] for i in rows_])\n            m = np.array([v[k == j].mean() if np.any(k == j) else np.nan for j in range(nbins)])\n            ok = np.isfinite(m)\n            if ok.sum() < 2:\n                continue\n            out[band][0].append(((np.arange(nbins) + 0.5) / nbins)[ok]); out[band][1].append(m[ok] - m[ok].mean())\n    return {band: st.pearsonr(np.concatenate(x), np.concatenate(y)) + (len(np.concatenate(x)),) for band, (x, y) in out.items()}\n\nfor kind in (\"episode\", \"packet\"):\n    res = lfp_course(kind)\n    print(\"%s: \" % kind + \"; \".join(\"%s R = %+.3f (p %.2g, n %d)\" % (b, *v) for b, v in res.items()))\n    for nb, md in ((5, 20.0), (20, 20.0), (10, 60.0)):\n        res = lfp_course(kind, nb, md)\n        print(\"   variant %d bins, min %d s: \" % (nb, md) + \"; \".join(\"%s %+.3f (p %.2g)\" % (b, v[0], v[1]) for b, v in res.items()))\nprint(\"\\nPer subject, packets:\")\nall_sessions = sessions\nfor subj in sorted(tab.subject.unique()):\n    sessions = [s for s in all_sessions if s.subject == subj]\n    res = lfp_course(\"packet\")\n    print(\"  %s: \" % subj + \"; \".join(\"%s %+.3f (p %.2g)\" % (b, v[0], v[1]) for b, v in res.items()))\nsessions = all_sessions\n\n# %% [markdown]\n# ## fig4-delta-packet-length\n#\n# > Mean delta power within whole packets, normalized by nonREM delta power, is positively correlated\n# > with packet length (R = 0.31, p < 0.05).\n\n# %% tags=[\"claim:fig4-delta-packet-length\"]\npk = []\nfor s in sessions:\n    allv = {b: np.concatenate([10 ** s.lfp[i][1][b] for i in s.lfp]) for b in ss.BANDS}\n    for i, (t, pw) in s.lfp.items():\n        if s.stops[i] - s.starts[i] < 20:\n            continue\n        rr = {}\n        for g in (1, 6):\n            units = s.pe[sext[s.path][1] == g]\n            rr[g] = np.mean(ss.rates(s.spikes, units, s.starts[i], s.stops[i])) if len(units) else np.nan\n        last = t >= s.stops[i] - 20\n        pk.append(dict(subject=s.subject, session=s.session_id, row=i, dur=s.stops[i] - s.starts[i],\n                       delta_norm=np.mean(10 ** pw[\"delta\"]) / allv[\"delta\"].mean(),\n                       delta=pw[\"delta\"].mean(), gamma=pw[\"gamma\"].mean(), sigma_last20=pw[\"sigma\"][last].mean(),\n                       s1=rr[1], s6=rr[6]))\npk = pd.DataFrame(pk)\nr, p = st.pearsonr(pk.dur, pk.delta_norm)\nprint(\"Packets of at least 20 s with LFP: %d; R = %.3f, p = %.2g; within 0.279-0.341: %s\" % (len(pk), r, p, 0.279 <= r <= 0.341))\nprint(\"Spearman rho = %.3f; R with log10 duration = %.3f\" % (st.spearmanr(pk.dur, pk.delta_norm)[0], st.pearsonr(np.log10(pk.dur), pk.delta_norm)[0]))\nprint(\"Normalized delta power: %.2f to %.2f; durations %.0f to %.0f s\" % (pk.delta_norm.min(), pk.delta_norm.max(), pk.dur.min(), pk.dur.max()))\nprint(\"Per subject R:\", {subj: round(st.pearsonr(g.dur, g.delta_norm)[0], 3) for subj, g in pk.groupby(\"subject\")})\n\n# %% [markdown]\n# ## fig4cd-packet-rate-lfp\n#\n# > Per packet, the rate of the fastest sextile is negatively correlated with delta power (R = -0.28)\n# > and positively with gamma power (R = 0.44), and the rate of the slowest sextile is positively\n# > correlated with sigma power in the last 20 s of the packet (R = 0.25), all p < 1e-10.\n\n# %% tags=[\"claim:fig4cd-packet-rate-lfp\"]\nz = lambda v: (v - v.mean()) / v.std() if v.std() > 0 else v * np.nan\npz = pk.copy()\nfor c in (\"delta\", \"gamma\", \"sigma_last20\", \"s1\", \"s6\"):\n    pz[c] = pk.groupby(\"session\")[c].transform(z)\nout = {}\nfor name, a, b, exp_, tol in ((\"s6 vs delta\", \"s6\", \"delta\", -0.28, 0.028), (\"s6 vs gamma\", \"s6\", \"gamma\", 0.44, 0.044),\n                              (\"s1 vs sigma last 20 s\", \"s1\", \"sigma_last20\", 0.25, 0.025)):\n    d = pz[[a, b]].dropna()\n    r, p = st.pearsonr(d[a], d[b])\n    out[name] = (r, p)\n    print(\"%s: R = %.3f, p = %.2g, n %d; within tolerance %s; sign as stated %s\" % (\n        name, r, p, len(d), abs(r - exp_) <= tol, np.sign(r) == np.sign(exp_)))\nprint(\"\\nPer subject:\")\nfor subj, g in pz.groupby(\"subject\"):\n    vals = []\n    for a, b in ((\"s6\", \"delta\"), (\"s6\", \"gamma\"), (\"s1\", \"sigma_last20\")):\n        d = g[[a, b]].dropna()\n        vals.append(st.pearsonr(d[a], d[b])[0] if len(d) > 2 else np.nan)\n    print(\"  %s: s6-delta %.3f, s6-gamma %.3f, s1-sigma %.3f, packets %d\" % (subj, *vals, len(g)))\n\n# %% [markdown]\n# ## State triplets\n#\n# Triplets of consecutive epochs A, B, A in the state table; the change per pE cell is its rate in the\n# second A minus the first.\n\n# %%\ndef triplets(a_state, b_state):\n    out = []\n    for s in sessions:\n        for i in range(1, len(s.state) - 1):\n            if s.state[i - 1] == a_state and s.state[i] == b_state and s.state[i + 1] == a_state:\n                r1 = ss.rates(s.spikes, s.pe, s.starts[i - 1], s.stops[i - 1])\n                r2 = ss.rates(s.spikes, s.pe, s.starts[i + 1], s.stops[i + 1])\n                for k, u in enumerate(s.pe):\n                    out.append(dict(subject=s.subject, session=s.session_id, row=i, unit=u, sextile=sext[s.path][1][k],\n                                    pre=r1[k], post=r2[k], ch=r2[k] - r1[k], mid_dur=s.stops[i] - s.starts[i]))\n    return pd.DataFrame(out)\n\ndef triplet_report(d, alpha):\n    print(\"triplets %d, cell-triplet pairs %d\" % (d.groupby([\"session\", \"row\"]).ngroups, len(d)))\n    res = {}\n    for g in range(1, 7):\n        x = d[d.sextile == g]\n        p = st.wilcoxon(x.ch).pvalue if (x.ch != 0).any() else 1.0\n        cm = x.groupby([\"session\", \"unit\"]).ch.mean()\n        pc = st.wilcoxon(cm).pvalue if (cm != 0).any() else 1.0\n        res[g] = (x.ch.mean(), p)\n        print(\"  sextile %d: n %d, mean change %+.4f Hz (pre mean %.3f), Wilcoxon p = %.2g%s | per-cell means: n %d, mean %+.4f, p = %.2g\" % (\n            g, len(x), x.ch.mean(), x.pre.mean(), p, \" *\" if p < alpha else \"\", len(cm), cm.mean(), pc))\n    return res\n\ndef triplet_by_subject(d, gs):\n    print(\"  per subject, mean change (Hz) for sextiles %s:\" % (gs,))\n    print(d[d.sextile.isin(gs)].groupby([\"subject\", \"sextile\"]).ch.mean().unstack().round(4).to_string())\n\ntrip = {k: triplets(*k) for k in ((\"MA\", \"NREM\"), (\"NREM\", \"WAKE\"), (\"NREM\", \"MA\"), (\"NREM\", \"REM\"))}\n\n# %% [markdown]\n# ## fig5b-nrem-between-ma\n#\n# > An intervening nonREM packet reduces the rates of the top two sextiles from one MA to the next\n# > (both p < 0.01).\n\n# %% tags=[\"claim:fig5b-nrem-between-ma\"]\nres_ma = triplet_report(trip[(\"MA\", \"NREM\")], 0.01)\ntriplet_by_subject(trip[(\"MA\", \"NREM\")], [5, 6])\n\n# %% [markdown]\n# ## fig5b-wake-between-packets\n#\n# > An intervening WAKE episode increases the rate of the fastest sextile from one nonREM packet to\n# > the next (24 triplets).\n\n# %% tags=[\"claim:fig5b-wake-between-packets\"]\nres_w = triplet_report(trip[(\"NREM\", \"WAKE\")], 0.05)\nd = trip[(\"NREM\", \"WAKE\")]\nprint(\"WAKE durations in these triplets (s): median %.0f, range %.0f to %.0f\" % (\n    d.groupby([\"session\", \"row\"]).mid_dur.first().median(), d.mid_dur.min(), d.mid_dur.max()))\ntriplet_by_subject(d, [1, 6])\n\n# %% [markdown]\n# ## fig5b-ma-between-packets\n#\n# > An intervening MA increases the rates of slow-firing pE cells from one packet to the next and does\n# > not affect fast-firing cells.\n\n# %% tags=[\"claim:fig5b-ma-between-packets\"]\nres_m = triplet_report(trip[(\"NREM\", \"MA\")], 0.05)\ntriplet_by_subject(trip[(\"NREM\", \"MA\")], [1, 6])\n\n# %% [markdown]\n# ## fig5b-rem-between-packets\n#\n# > An intervening REM episode decreases the rates of all sextiles from one packet to the next.\n\n# %% tags=[\"claim:fig5b-rem-between-packets\"]\nres_r = triplet_report(trip[(\"NREM\", \"REM\")], 0.05)\ntriplet_by_subject(trip[(\"NREM\", \"REM\")], [1, 6])\nprint(\"REM epochs followed by Non-REM: %d of %d REM epochs\" % (\n    sum(int(np.sum((s.state[:-1] == \"REM\") & (s.state[1:] == \"NREM\"))) for s in sessions),\n    sum(int(np.sum(s.state == \"REM\")) for s in sessions)))\n\n# %% [markdown]\n# ## fig5c-rem-duration\n#\n# > Longer REM episodes produce a proportionally larger decrease of rates from one packet to the next\n# > (R = -0.22, p < 1e-2).\n\n# %% tags=[\"claim:fig5c-rem-duration\"]\nd = trip[(\"NREM\", \"REM\")]\nper = d.groupby([\"session\", \"row\"]).agg(pre=(\"pre\", \"mean\"), post=(\"post\", \"mean\"), dur=(\"mid_dur\", \"first\"),\n                                        subject=(\"subject\", \"first\"))\nper = per[per.pre > 0]\nra = st.pearsonr(per.dur, (per.post - per.pre) / per.pre)\ndc = d[d.pre > 0]\nrb = st.pearsonr(dc.mid_dur, (dc.post - dc.pre) / dc.pre)\nprint(\"(a) per triplet: R = %.3f, p = %.2g, n %d | (b) per cell and triplet: R = %.3f, p = %.2g, n %d\" % (\n    ra[0], ra[1], len(per), rb[0], rb[1], len(dc)))\nprint(\"Within -0.242 to -0.198:\", {\"a\": -0.242 <= ra[0] <= -0.198, \"b\": -0.242 <= rb[0] <= -0.198})\nprint(\"REM durations %.0f to %.0f s; fractional change (a) %.2f to %.2f\" % (\n    per.dur.min(), per.dur.max(), ((per.post - per.pre) / per.pre).min(), ((per.post - per.pre) / per.pre).max()))\nprint(\"Spearman (a): rho = %.3f, p = %.2g\" % st.spearmanr(per.dur, (per.post - per.pre) / per.pre))\n\n# %% [markdown]\n# ## fig5c-sigma-ma\n#\n# > Sigma power in the last 20 s of a packet between two MAs correlates with a larger increase of the\n# > slowest sextile from one MA to the next (R = 0.181, p < 0.01).\n\n# %% tags=[\"claim:fig5c-sigma-ma\"]\nsig_all = {}\nfor s in sessions:\n    v = {i: s.lfp[i][1][\"sigma\"][s.lfp[i][0] >= s.stops[i] - 20].mean() for i in s.lfp}\n    vals = np.array(list(v.values()))\n    sig_all[s.path] = {i: (x - np.nanmean(vals)) / np.nanstd(vals) for i, x in v.items()}\nd = trip[(\"MA\", \"NREM\")]\nd1 = d[d.sextile == 1].groupby([\"session\", \"row\"]).agg(ch=(\"ch\", \"mean\")).reset_index()\npath_of = {s.session_id: s.path for s in sessions}\nd1[\"sigma\"] = [sig_all[path_of[a]].get(b, np.nan) for a, b in zip(d1.session, d1.row)]\nd1 = d1.dropna()\nr, p = st.pearsonr(d1.sigma, d1.ch)\nprint(\"MA-packet-MA triplets with sextile 1 cells and LFP: %d; R = %.3f, p = %.2g; within 0.163-0.199: %s\" % (len(d1), r, p, 0.163 <= r <= 0.199))\nprint(\"Spearman rho = %.3f, p = %.2g\" % st.spearmanr(d1.sigma, d1.ch))\n\n# %% [markdown]\n# ## fig5c-delta-change\n#\n# > The increase of the slowest sextile's rate from one packet to the next is positively correlated\n# > with the change of delta power between the packets, regardless of the intervening state.\n\n# %% tags=[\"claim:fig5c-delta-change\"]\ndd = []\nfor sess, g in pk.groupby(\"session\", sort=False):\n    g = g.sort_values(\"row\")\n    dd.append(pd.DataFrame({\"subject\": g.subject.values[1:], \"d_s1\": np.diff(g.s1.values), \"d_delta\": np.diff(g.delta_norm.values),\n                            \"d_s6\": np.diff(g.s6.values)}))\ndd = pd.concat(dd).dropna()\nr, p = st.pearsonr(dd.d_delta, dd.d_s1)\nprint(\"Consecutive packet pairs (both at least 20 s): %d; sextile 1: R = %.3f, p = %.2g\" % (len(dd), r, p))\nprint(\"Sextile 6 for comparison: R = %.3f, p = %.2g\" % st.pearsonr(dd.d_delta, dd.d_s6))\nprint(\"Per subject, sextile 1 R:\", {subj: round(st.pearsonr(g.d_delta, g.d_s1)[0], 3) for subj, g in dd.groupby(\"subject\") if len(g) > 2})\n\n# %% [markdown]\n# ## figs5-within-wake-rem\n#\n# > Within WAKE the two fastest sextiles increase and the two slowest decrease their rates; within REM\n# > all sextiles except the fourth increase.\n\n# %% tags=[\"claim:figs5-within-wake-rem\"]\nwk = course(\"WAKE\", 10, 40.0)\nrm = course(\"REM\", 10, 20.0)\ntw, trm = sextile_table(wk), sextile_table(rm)\nprint(\"WAKE epochs %d, REM epochs %d\" % (len(wk), len(rm)))\nfor name, t in ((\"WAKE\", tw), (\"REM\", trm)):\n    print(name + \": \" + \"; \".join(\"%s R = %+.3f (p %.2g)\" % (g, v[0], v[1]) for g, v in t.items()))\nwake_ok = all(tw[g][0] > 0 and tw[g][1] < 0.05 for g in (5, 6)) and all(tw[g][0] < 0 and tw[g][1] < 0.05 for g in (1, 2))\nrem_ok = all(trm[g][0] > 0 and trm[g][1] < 0.05 for g in (1, 2, 3, 5, 6))\nprint(\"WAKE part holds:\", wake_ok, \"| REM part holds:\", rem_ok)\n\n# %% [markdown]\n# ## Summary\n"
}
```

```
File created successfully at: /tmp/claude-1001/w/nb_src.py (file state is current in your context — no need to Read it back)
```

**Agent**

Now running the prototype against the cache to check it executes and see the outputs.

**Agent calls Bash**

```bash
cd $TMPDIR/w && cat > runproto.py <<'EOF'
import sys, re, pickle, time, matplotlib
matplotlib.use("Agg")
sys.path.insert(0,'entries/000041-watson-2016')
src=open('nb_src.py').read()
src=src.replace("sessions, excluded = ss.load_all(workers=6)", "sessions, excluded = pickle.load(open('/tmp/claude-1001/w/cache.pkl','rb'))")
cells=re.split(r'^# %%.*$', src, flags=re.M)
heads=re.findall(r'^# %%.*$', src, flags=re.M)
g={'pickle':pickle}
only=sys.argv[1:] 
for h,c in zip(heads,cells[1:]):
    if '[markdown]' in h: 
        m=re.search(r'^# ## (.*)$', c, re.M)
        if m: print('\n=====', m.group(1), flush=True)
        continue
    t=time.time()
    exec(compile(c,'cell','exec'), g)
    print('[%.1fs]'%(time.time()-t), flush=True)
EOF
$TMPDIR/venv/bin/python runproto.py 2>&1 | tail -400
```

```
7     BWRat21    BWRat21_121113        6           11    221.750  0.050  1.841
8     BWRat21    BWRat21_121613        3           10    149.933  0.067  2.034
9     BWRat21    BWRat21_121813        4            7    185.750  0.038  1.355
10      Bogey      Bogey_012615        4           38    256.417  0.148  6.181
11       Dino       Dino_061814        4           15    151.267  0.099  2.666
12       Dino       Dino_061914        2            6     60.367  0.099  4.307
13       Dino       Dino_062014        5           14    186.300  0.075  2.308
14       Dino       Dino_072314        3            4     88.883  0.045  1.669
15       Dino       Dino_072414        2            4     70.433  0.057  1.514
16      Rizzo      Rizzo_022615       11           25    372.267  0.067  2.306
17      Rizzo      Rizzo_022715        3           14    201.467  0.069  1.911
18   Splinter   Splinter_020515        5           12    211.767  0.057  1.850
19   Splinter   Splinter_020915        4           17    246.717  0.069  2.229
20  Templeton  Templeton_032415        3           22    131.367  0.167  5.950
(a) inside SLEEP, per-session means: median duration 19.0 s, frequency 0.096 per min, fraction 3.22%; within tolerance [np.True_, np.False_, np.False_]
(b) all MAs, pooled, per nonREM episode time: median duration 19.0 s, frequency 0.127 per min, fraction 4.23%; within tolerance [np.True_, np.False_, np.False_]
SD over sessions (a): frequency 0.051, fraction 1.97
MAs: 391 in all, 262 inside SLEEP periods (paper: 790 in 27 sessions)
MA durations (s): min 7, max 39; the state table has 1 s resolution
Awake epochs under 40 s not between two Non-REM epochs (left as WAKE): 345
[... 381 more lines not kept]
```

**Agent**

The prototype runs end to end. Let me see the first part of the output (data check through MA statistics).

**Agent calls Bash**

```bash
cd $TMPDIR/w && $TMPDIR/venv/bin/python runproto.py 2>&1 | head -260 > head.txt; cat head.txt | head -260
```

```
21 sessions loaded; excluded: {'sub-Dino/sub-Dino_ses-Dino-072114_ecephys.nwb': 'spike times are whole seconds divided by 20000'}
[1.8s]

===== Data check
      subject           session   pE  pI  unknown  states_min  spikes_first  spikes_last_min  lfp_min  WAKE_min  MA_n  NREM_min  REM_min  epochs  lfp_packets
0     BWRat17    BWRat17_121712   44   6        0       100.8          0.04            101.0    101.0      72.2     6      24.2      1.8      33           13
1     BWRat17    BWRat17_121912   29   0        0       108.7          0.02            108.9    108.9      37.0    16      61.1      3.6      71           31
2     BWRat18    BWRat18_020513   35   5        0       126.4          0.03            126.5    126.5      42.8     2      73.2      8.9      53           19
3     BWRat19    BWRat19_032413   37  12        0        83.4          0.01             83.6     83.6      43.4     9      35.7      0.2      34           16
4     BWRat19    BWRat19_032513   50   9        0        65.3          0.01             65.5     65.5      19.6     9      37.0      4.8      42           18
5     BWRat20    BWRat20_101013   13   5        0       222.6          0.00            222.7    222.7     136.4     9      69.4     12.8      62           26
6     BWRat20    BWRat20_101513   58   3        0       383.4          0.01            383.5    383.5     126.4    47     201.8     38.5     298          107
7     BWRat21    BWRat21_121113   28   4        0       364.6          0.00            364.7    364.7     119.9    17     171.0     64.1     213           67
8     BWRat21    BWRat21_121613   20   1       23       358.9          0.13            359.0    359.0     144.5    20     152.4     51.6     183           59
9     BWRat21    BWRat21_121813   11   1        0       361.6          0.45            361.8    361.8     143.7    11     155.5     56.4     148           49
10      Bogey      Bogey_012615   32   4        0       404.2          0.01            404.4    404.4     1
[... 245 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000041-watson-2016 && python - <<'EOF'
src=open('sleepstates.py').read()
src=src.replace("""    lfp: dict = field(default_factory=dict)  # per packet index, band power series
""","""    lfp: dict = field(default_factory=dict)  # per packet index, band power series
    lfp_raw: list = field(default_factory=list)  # (start time, int16 samples) for the clock check
""")
old='''def read_packet_lfp(f: h5py.File, s: Session, min_dur: float = 2.0) -> None:
    """Band power series of every NREM packet of at least min_dur seconds, from the reference
    channel, into s.lfp[row] = (window centre times in s, dict of log10 band power)."""
    d = f["processing/ecephys/LFP/lfp/data"]
    for i in np.where(s.state == "NREM")[0]:'''
new='''def read_packet_lfp(f: h5py.File, s: Session, min_dur: float = 2.0, raw_seconds: float = 300.0) -> None:
    """Band power series of every NREM packet of at least min_dur seconds, from the reference
    channel, into s.lfp[row] = (window centre times in s, dict of log10 band power). The raw
    samples of the first packets of at least 30 s, up to raw_seconds in all, are kept in
    s.lfp_raw for checking the LFP clock against the spikes."""
    d = f["processing/ecephys/LFP/lfp/data"]
    kept = 0.0
    for i in np.where(s.state == "NREM")[0]:'''
assert old in src; src=src.replace(old,new)
old2='''        x = d[i0:i1, s.lfp_channel]
        t, p = band_power(x)
        s.lfp[i] = (a + t, p)'''
new2='''        x = d[i0:i1, s.lfp_channel]
        t, p = band_power(x)
        s.lfp[i] = (a + t, p)
        if b - a >= 30 and kept < raw_seconds:
            s.lfp_raw.append((i0 / LFP_RATE, x))
            kept += len(x) / LFP_RATE'''
assert old2 in src; src=src.replace(old2,new2)
open('sleepstates.py','w').write(src)
EOF
cd $TMPDIR/w && $TMPDIR/venv/bin/python cache.py && ls -la cache.pkl
```

```
-rw-r--r-- 1 runner runner 228408425 Oct 16 02:52 cache.pkl
Shell cwd was reset to
```

**Agent**

Now updating the clock-check cell, the excluded-file check, the ACG variant and the course caching in the notebook source.

**Agent calls Bash**

```bash
cd $TMPDIR/w && python3 - <<'EOF'
src=open('nb_src.py').read()
# 1. clock check cell
a=src.index('# %% tags=["sanity"]\nshifts =')
b=src.index('# %% [markdown]\n# The data check against the description')
new='''# %% tags=["sanity"]
shifts = np.array([-300, -120, -60, -20, -5, 0, 5, 20, 60, 120, 300])
clock = []
for s in sessions:
    pop = np.sort(np.concatenate([s.spikes[u] for u in s.pe]))
    edges50 = np.arange(0, s.stops[-1], 0.05)
    silent = np.histogram(pop, edges50)[0] == 0
    centres = edges50[:-1] + 0.025
    row = {"session": s.session_id, "pE": len(s.pe)}
    for d in shifts:
        k = np.searchsorted(s.starts + d, centres, side="right") - 1
        ok = (k >= 0) & (centres < (s.stops + d)[np.clip(k, 0, None)])
        lab = np.where(ok, s.state[np.clip(k, 0, None)], "none")
        row[int(d)] = silent[lab == "NREM"].mean() - silent[lab == "WAKE"].mean()
    # LFP against spikes: cross-correlation of LFP and pE spike count in 8 ms bins (10 samples)
    lags = np.arange(-125, 126)
    acc = np.zeros(len(lags)); nseg = 0
    for t0, x in s.lfp_raw:
        nb = len(x) // 10
        lf = x[:nb * 10].reshape(nb, 10).mean(axis=1)
        sp = np.diff(np.searchsorted(pop, t0 + np.arange(nb + 1) * 0.008))
        lf = (lf - lf.mean()) / lf.std(); sp = (sp - sp.mean()) / (sp.std() or 1)
        acc += np.array([np.mean(lf[max(0, -L):nb - max(0, L)] * sp[max(0, L):nb - max(0, -L)]) for L in lags]); nseg += 1
    cc = acc / nseg
    j = np.argmax(np.abs(cc))
    row.update({"lfp seconds": round(sum(len(x) for _, x in s.lfp_raw) / ss.LFP_RATE), "xcorr extreme lag ms": lags[j] * 8,
                "xcorr extreme": round(cc[j], 3), "xcorr at -1 s": round(cc[0], 3), "xcorr at +1 s": round(cc[-1], 3)})
    clock.append(row)
clock = pd.DataFrame(clock)
best = clock[[int(d) for d in shifts]].idxmax(axis=1)
clock["best shift"] = best
clock["labels consistent"] = (best.abs() <= 60) & (clock[0] > clock[[-300, 300]].max(axis=1))
clock["lfp consistent"] = (clock["xcorr extreme lag ms"].abs() <= 50) & (clock["xcorr extreme"].abs() > 3 * clock[["xcorr at -1 s", "xcorr at +1 s"]].abs().max(axis=1))
print("Contrast of silent-bin fraction, NREM minus WAKE, by shift of the state table (s), and the LFP-spike cross-correlation:")
print(clock.round(3).to_string())
print("\\nState labels consistent with the spikes (largest contrast within 60 s of zero shift and above the contrast at +-300 s):",
      int(clock["labels consistent"].sum()), "of", len(clock), "| not established:", list(clock.session[~clock["labels consistent"]]))
print("LFP consistent with the spikes (largest |r| within 50 ms of zero lag and over 3 times |r| at +-1 s):",
      int(clock["lfp consistent"].sum()), "of", len(clock), "| not established:", list(clock.session[~clock["lfp consistent"]]))
print("Shift with the largest contrast, counts:", best.value_counts().sort_index().to_dict())

'''
src=src[:a]+new+src[b:]
# 2. excluded file integer check
src=src.replace('bool(np.all(np.round(t * 20000) == t * 20000))','bool(np.allclose(t * 20000, np.round(t * 20000), atol=1e-6))')
# 3. course cache
src=src.replace('''courses = {k: course(k) for k in ("episode", "packet")}''','''_cache = {}
def course_c(kind, nbins=10, min_dur=20.0):
    if (kind, nbins, min_dur) not in _cache:
        _cache[(kind, nbins, min_dur)] = course(kind, nbins, min_dur)
    return _cache[(kind, nbins, min_dur)]

courses = {k: course_c(k) for k in ("episode", "packet")}''')
src=src.replace('t = sextile_table(course(kind, nb, md))','t = sextile_table(course_c(kind, nb, md))')
src=src.replace('*cv_r(course(kind, nb, md))','*cv_r(course_c(kind, nb, md))')
src=src.replace('*burst_r(course(kind, nb, md))','*burst_r(course_c(kind, nb, md))')
# 4. ACG variant
old='''print("\\nNREM peak within 7-9 ms:", 7 <= res["NREM"][0] <= 9,'''
new_='''for state, hs in acg.items():
    mean = np.mean(hs, axis=0)
    hp = np.convolve(mean, np.ones(21) / 21, mode="same") / np.convolve(mean, np.ones(101) / 101, mode="same")
    w = (lags >= 80) & (lags <= 200)
    print("Variant, %s: 21 ms over 101 ms moving average, maximum 80-200 ms at %.1f ms (ratio %.3f)" % (
        state, lags[w][np.argmax(hp[w])], hp[w].max()))
print("\\nNREM peak within 7-9 ms:", 7 <= res["NREM"][0] <= 9,'''
assert old in src; src=src.replace(old,new_,1)
open('nb_src.py','w').write(src)
EOF
grep -n "course(kind" nb_src.py
```

```
862:def course(kind, nbins=10, min_dur=20.0):
884:        _cache[(kind, nbins, min_dur)] = course(kind, nbins, min_dur)
988:def lfp_course(kind, nbins=10, min_dur=20.0):
1006:    res = lfp_course(kind)
1009:        res = lfp_course(kind, nb, md)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/w && $TMPDIR/venv/bin/python runproto.py > out2.txt 2>&1; grep -n "^\[" out2.txt | awk -F'[][]' '{print $2}' | tr '\n' ' '; echo; sed -n '/one clock/,/dataset-composition/p' out2.txt | head -5; grep -n -A40 "Contrast of silent" out2.txt | head -45; grep -n -A12 "fig2c-acg-peaks" out2.txt | head -16; grep -n "times x 20000" out2.txt
```

```
1.8s 3.1s 7.7s 0.1s 0.1s 0.0s 0.0s 0.0s 1.4s 4.0s 2.6s 0.0s 0.0s 0.0s 0.0s 0.1s 0.1s 0.0s 0.1s 0.1s 0.0s 14.8s 47.3s 0.2s 0.0s 2.7s 0.2s 0.1s 0.6s 0.0s 0.0s 0.0s 0.0s 0.0s 0.1s 0.0s 8.4s 
49:Contrast of silent-bin fraction, NREM minus WAKE, by shift of the state table (s), and the LFP-spike cross-correlation:
50-             session   pE   -300   -120    -60    -20     -5      0      5     20     60    120    300  lfp seconds  xcorr extreme lag ms  xcorr extreme  xcorr at -1 s  xcorr at +1 s best shift  labels consistent  lfp consistent
51-0     BWRat17_121712   44  0.057  0.114  0.128  0.159  0.168  0.167  0.161  0.144  0.125  0.110  0.092          310                     0         -0.150          0.014         -0.010         -5               True            True
52-1     BWRat17_121912   29  0.050  0.054  0.075  0.100  0.106  0.103  0.102  0.086  0.074  0.064  0.055          334                     0         -0.057          0.021         -0.016         -5               True           False
53-2     BWRat18_020513   35  0.108  0.131  0.150  0.159  0.159  0.156  0.161  0.172  0.167  0.160  0.115          494                   -40         -0.118          0.006          0.003         20               True            True
54-3     BWRat19_032413   37  0.127  0.166  0.179  0.230  0.257  0.257  0.251  0.232  0.198  0.191  0.153          316                   -16         -0.169          0.003         -0.026          0               True            True
55-4     BWRat19_032513   50  0.044  0.099  0.128  0.156  0.169  0.172  0.170  0.160  0.129  0.105  0.008          322                   -16         -0.189         -0.013          0.022          0               True            True
56-5     BWRat20_101013   13  0.159  0.227  0.259  0.291  0.308  0.308  0.307  0.297  0.264  0.228  0.150          710                     8         -0.142          0.003         -0.006          0               True            True
57-6     BWRat20_101513   58  0.034  0.076  0.100  0.134  0.151  
[... 47 more lines not kept]
```

**Agent**

Clock checks now take 8 s and the whole analysis about 2 min after loading. Let me view the remaining outputs I haven't seen (fig2f reading b).

**Agent calls Bash**

```bash
cd $TMPDIR/w && sed -n '/Reading (b), mean r/,/ma-statistics/p' out2.txt; sed -n '/===== ma-statistics/,/^\[/p' out2.txt | head -8
```

```
Reading (b), mean r by group pair (rows and columns: groups 1 to 6):
        1       2       3       4       5       6
1  0.0057  0.0073  0.0062  0.0080  0.0083  0.0087
2  0.0073  0.0125  0.0133  0.0118  0.0119  0.0148
3  0.0062  0.0133  0.0145  0.0155  0.0152  0.0186
4  0.0080  0.0118  0.0155  0.0256  0.0197  0.0220
5  0.0083  0.0119  0.0152  0.0197  0.0221  0.0258
6  0.0087  0.0148  0.0186  0.0220  0.0258  0.0401
(6,6) mean 0.0401, largest pair is (np.int64(6), np.int64(6)); (1,6) mean 0.0087, n 896, t = 13.45, p = 1e-37

Per subject, reading (a): mean r of (6,6) and (1,6) pairs
a          (6, 6)  (1, 6)
subject                  
BWRat17    0.0558  0.0067
BWRat18       NaN -0.0021
BWRat19    0.0551  0.0066
BWRat20    0.0663  0.0144
BWRat21       NaN     NaN
Bogey      0.0606  0.0073
Dino       0.0319  0.0074
[... 15 more lines not kept]
```

**Agent**

Dino_061914's LFP is 331.7 min long against 292 min of spikes and states, has 125 columns for 128 electrodes, and shows no spike-LFP correlation. Checking whether its LFP is scrambled.

**Agent calls Bash**

```bash
cd $TMPDIR/w && cat > dino.py <<'EOF'
import sys; sys.path.insert(0,'entries/000041-watson-2016')
import sleepstates as ss, numpy as np
u=dict(ss.asset_urls())
for p in ['sub-Dino/sub-Dino_ses-Dino-061914_ecephys.nwb','sub-Dino/sub-Dino_ses-Dino-062014_ecephys.nwb','sub-Dino/sub-Dino_ses-Dino-061814_ecephys.nwb']:
    f=ss.open_nwb(u[p]); d=f['processing/ecephys/LFP/lfp/data']
    x=d[5_000_000:5_012_500,:8].astype(float)
    lag1=[np.corrcoef(x[:-1,c],x[1:,c])[0,1] for c in range(8)]
    adj=[np.corrcoef(x[:,c],x[:,c+1])[0,1] for c in range(7)]
    el=f['processing/ecephys/LFP/lfp/electrodes'][()]
    print(p.split('/')[1], d.shape, 'n electrodes table', len(f['general/extracellular_ephys/electrodes/id'][()]), 'lfp el refs', len(el), 'lag-1 autocorr', np.round(lag1,3), 'adjacent ch corr', np.round(adj,2))
EOF
$TMPDIR/venv/bin/python dino.py
```

```
sub-Dino_ses-Dino-061914_ecephys.nwb (24877761, 125) n electrodes table 128 lfp el refs 125 lag-1 autocorr [0.477 0.469 0.467 0.458 0.466 0.497 0.466 0.491] adjacent ch corr [0.7  0.7  0.7  0.68 0.71 0.7  0.71]
sub-Dino_ses-Dino-062014_ecephys.nwb (27954000, 128) n electrodes table 128 lfp el refs 128 lag-1 autocorr [0.964 0.965 0.961 0.988 0.965 0.96  0.96  0.961] adjacent ch corr [0.98 0.98 0.39 0.56 0.93 0.95 0.98]
sub-Dino_ses-Dino-061814_ecephys.nwb (24557750, 128) n electrodes table 128 lfp el refs 128 lag-1 autocorr [0.965 0.949 0.95  0.965 0.966 0.955 0.939 0.932] adjacent ch corr [0.86 0.92 0.88 0.84 0.86 0.85 0.96]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/w && python3 - <<'EOF'
src=open('nb_src.py').read()
anchor='# %% [markdown]\n# ### Do the spikes, the states and the LFP share one clock?'
new='''# %% tags=["sanity"]
# LFP: the lag-1 sample autocorrelation of the reference channel, from the raw samples kept at
# load time. LFP at 1250 Hz is smooth (near 1); scrambled samples are not.
lag1 = {s.session_id: float(np.mean([np.corrcoef(x[:-1].astype(float), x[1:].astype(float))[0, 1] for _, x in s.lfp_raw]))
        for s in sessions}
print("LFP lag-1 autocorrelation per session:", {k: round(v, 3) for k, v in lag1.items()})
lfp_bad = [s.session_id for s in sessions if lag1[s.session_id] < 0.8]
print("Sessions whose LFP is left out of the LFP analyses (lag-1 autocorrelation under 0.8):", lfp_bad)
for s in sessions:
    if s.session_id in lfp_bad:
        print("  %s: LFP has %d columns for %d electrodes and lasts %.1f min; states end at %.1f min" % (
            s.session_id, len(h5py.File(remfile.File(urls[s.path]), "r")["processing/ecephys/LFP/lfp/electrodes"][()]),
            len(h5py.File(remfile.File(urls[s.path]), "r")["general/extracellular_ephys/electrodes/id"][()]),
            s.lfp_samples / ss.LFP_RATE / 60, s.stops[-1] / 60))
        s.lfp = {}

'''
assert anchor in src
src=src.replace(anchor, new+anchor)
src=src.replace('''for s in sessions:
    allv = {b: np.concatenate''','''for s in sessions:
    if not s.lfp:
        continue
    allv = {b: np.concatenate''')
src=src.replace('''for s in sessions:
    v = {i: s.lfp[i][1]["sigma"]''','''for s in sessions:
    if not s.lfp:
        continue
    v = {i: s.lfp[i][1]["sigma"]''')
src=src.replace('d1["sigma"] = [sig_all[path_of[a]].get(b, np.nan)','d1["sigma"] = [sig_all.get(path_of[a], {}).get(b, np.nan)')
src=src.replace('''print("cell-cycle pairs %d (cycles %d); first %.3f +- %.3f Hz, last %.3f +- %.3f Hz;''','''print("cell-cycle pairs %d (cycles %d); first %.4f +- %.3f Hz, last %.4f +- %.3f Hz;''')
# corrcoef warnings and dropped pairs
src=src.replace('''    C = np.corrcoef(X)''','''    with np.errstate(invalid="ignore", divide="ignore"):
        C = np.corrcoef(X)
    n_pairs_all = globals().get("n_pairs_all", 0) + len(s.pe) * (len(s.pe) - 1) // 2''')
src=src.replace('''print("pairs:", len(pairs), "| overall''','''print("pairs with a defined correlation %d of %d (cells without Non-REM spikes have none)" % (len(pairs), n_pairs_all))
print("pairs:", len(pairs), "| overall''')
open('nb_src.py','w').write(src)
EOF
$TMPDIR/venv/bin/python runproto.py > out3.txt 2>&1; grep -n "Traceback\|Error" out3.txt; grep -n "lag-1\|left out of the LFP\|columns for" out3.txt; grep -n "cell-cycle pairs\|pairs with a defined" out3.txt; sed -n '/===== fig4i-band/,/===== State triplets/p' out3.txt | grep -v "^  [A-Z]" ; sed -n '/===== fig5c-sigma/,/===== figs5/p' out3.txt
```

```
49:LFP lag-1 autocorrelation per session: {np.str_('BWRat17_121712'): 0.998, np.str_('BWRat17_121912'): 0.998, np.str_('BWRat18_020513'): 0.999, np.str_('BWRat19_032413'): 0.998, np.str_('BWRat19_032513'): 0.998, np.str_('BWRat20_101013'): 0.995, np.str_('BWRat20_101513'): 0.993, np.str_('BWRat21_121113'): 0.996, np.str_('BWRat21_121613'): 0.997, np.str_('BWRat21_121813'): 0.996, np.str_('Bogey_012615'): 0.997, np.str_('Dino_061814'): 0.993, np.str_('Dino_061914'): 0.28, np.str_('Dino_062014'): 0.998, np.str_('Dino_072314'): 0.996, np.str_('Dino_072414'): 0.995, np.str_('Rizzo_022615'): 0.997, np.str_('Rizzo_022715'): 0.989, np.str_('Splinter_020515'): 0.999, np.str_('Splinter_020915'): 0.999, np.str_('Templeton_032415'): 0.999}
50:Sessions whose LFP is left out of the LFP analyses (lag-1 autocorrelation under 0.8): [np.str_('Dino_061914')]
51:  Dino_061914: LFP has 125 columns for 128 electrodes and lasts 331.7 min; states end at 291.9 min
251:pairs with a defined correlation 20764 of 20933 (cells without Non-REM spikes have none)
379:cell-cycle pairs 1070 (cycles 30); first 1.0915 +- 1.483 Hz, last 0.9679 +- 1.241 Hz; Wilcoxon p = 3.9e-06; last lower: True
408:(a) cell-cycle pairs: n 1070, mean pre 1.341, post 1.180 Hz, median change -0.0394, Wilcoxon p = 4.1e-09
===== fig4i-band-power-within-nrem
episode: delta R = +0.069 (p 1.1e-07, n 5880); sigma R = +0.135 (p 3.1e-25, n 5880); gamma R = +0.062 (p 1.7e-06, n 5880)
   variant 5 bins, min 20 s: delta +0.104 (p 1.6e-08); sigma +0.193 (p 3.7e-26); gamma +0.065 (p 0.00036)
   variant 20 bins, min 20 s: delta +0.049 (p 1.4e-07); sigma +0.101 (p 6e-28); gamma +0.054 (p 5.4e-09)
   variant 10 bins, min 60 s: delta +0.135 (p 1.6e-21); sigma +0.249 (p 8.4e-71); gamma +0.009 (p 0.51)
packet: delta R = -0.005 (p 0.61, n 9150); sigma R = +0.104 (p 1.6e-23, n 9150); gamma R = +0.182 (p 4.5e-69, n 9150)
   variant 5 bins, min 20 s: delta +0.009 (p 0.53); sigma +0.154 (p 8.6e-26); gamma +0.213 (p 3.5e-48)
   variant 20 bins, m
[... 34 more lines not kept]
```

**Agent**

All numbers are in. Writing the conclusion cells and the summary into the notebook source.

**Agent calls Bash**

```bash
cd $TMPDIR/w && cat > results.py <<'PYEOF'
R = {
"dataset-composition": """**Result: not reproduced.** Two of the five values are within tolerance: 10 rats (11 expected) and a mean session duration of 286.8 min (294 plus or minus 137). The files hold 22 sessions (27 expected), 826 pE cells (995) and 96 pI cells (126); in the 21 usable sessions 812 pE and 89 pI. Per session the pE counts are close to the paper's (mean 38.7, range 10 to 105, against 36.9 and 10 to 104), so the shortfall comes from the missing sessions and rat.""",
"fig2a-median-rates": """**Result: partially reproduced.** Three of six medians are within tolerance under both readings, all three pE values: 0.755, 0.662 and 0.825 Hz in WAKE, nonREM and REM under reading (a). The pI medians are 3.92, 2.73 and 3.06 Hz, below the paper's 5.59, 4.69 and 4.25; the pI sample is 89 cells, and its medians vary by subject from 0.07 to 13.4 Hz.""",
"fig2a-skewed-wide-distribution": """**Result: partially reproduced.** WAKE rates are strongly skewed (skewness 4.57) and the 97.5th percentile, 7.17 Hz, is within a factor of 2 of 5 Hz, but the 2.5th percentile, 0.0124 Hz, is about four times below 0.05 Hz, so the distribution spans more than the paper's range at the low end. On a log scale the rates are skewed to the left (skewness of log10 rates -0.74), which agrees with the paper's description of a heavier tail toward low rates.""",
"fig2a-fraction-above-2hz": """**Result: not reproduced.** The fractions above 2 Hz are 17.0% in WAKE (outside 17.3 to 21.1), 18.7% in REM and 9.1% in nonREM (both within tolerance). nonREM is lower than WAKE (chi-square p = 3.5e-06) and REM (p = 3.4e-08), but neither test reaches the paper's p < 1e-10. The direction of the effect is as in the paper.""",
"fig2b-wake-nrem-slope": """**Result: reproduced.** Under reading (a), log10 rates, R = 0.862 and the slope of nonREM on WAKE is 0.757 (95% CI 0.727 to 0.788), inside the widened interval 0.594 to 0.781 and below 1. In Hz the slope is 0.583, outside the interval. The reverse regression, WAKE on nonREM, gives 0.982 (0.942 to 1.022), so part of the slope below 1 can come from regression to the mean; the criterion does not use this check.""",
"fig2-burst-index-by-state": """**Result: partially reproduced.** The order nonREM > REM > WAKE holds under both readings (Kruskal-Wallis p = 5.7e-36 under (a)), and REM is above WAKE (paired Wilcoxon p = 1e-32). The medians match only in part: reading (a) gives 6.35, 2.64 and 3.65%, none within tolerance; reading (b) gives 11.67% in nonREM (within tolerance), 4.95% in WAKE and 6.71% in REM (both above).""",
"fig2c-acg-peaks": """**Result: partially reproduced.** The nonREM autocorrelogram peaks at 7.5 ms, within 7 to 9 ms. No theta peak is found by the criterion: the smoothed REM and WAKE autocorrelograms are highest at the 60 ms edge of the 60 to 250 ms window, as they decline from short lags. In the variant that divides by a 101 ms moving average, WAKE has a maximum at 118.5 ms (ratio 1.017) and REM at 149.5 ms (1.018); this does not change the outcome.""",
"fig2f-rate-group-correlations": """**Result: partially reproduced.** Under both readings the mean correlation of (6,6) pairs is positive and the largest of the 21 combinations (0.0424 under reading (a)), and correlations rise with the rates of both cells. No pair group is negatively correlated: (1,6) pairs have a mean of 0.0089 (t = 10.85, p = 8.7e-26, above zero), and 22.8% of all pairs are negative. Correlations of raw 100 ms counts may differ from the paper's measure, whose definition is in the supplement that was not available.""",
"ma-statistics": """**Result: not reproduced.** The median MA duration, 19.0 s, is within the paper's spread, but MAs are rarer: 0.096 per min of SLEEP and 3.22% of SLEEP time under reading (a), 0.127 per min and 4.23% under (b), against 0.32 plus or minus 0.12 per min and 9.1 plus or minus 3.5%. The 21 sessions give 391 MAs (262 inside SLEEP periods), against 790 in 27 sessions. MAs are derived here from the Awake label; 345 short Awake epochs that are not between two Non-REM epochs are left as WAKE.""",
"ma-fraction-over-nrem-episodes": """**Result: partially reproduced.** Over 243 episodes with an MA, the MA fraction pooled over episode bins decreases with time (R = -0.087, p = 1.7e-05), but neither reading reaches R = -0.85 or p < 1e-10: the bin means give R = -0.451 (p = 0.19). The mean fraction rises over the first half of the episode (0.067 to 0.157) and falls in the second (to 0.010); the first and last bins start and end in a packet by construction.""",
"packet-duration": """**Result: reproduced.** Over all 1069 Non-REM epochs the median duration is 108 s (within 99.9 to 122.1), with a 5th to 95th percentile of 12 to 484 s and a range of 6 to 1199 s, two orders of magnitude. Inside SLEEP periods the median is 128 s. Per subject the median ranges from 76 to 219 s.""",
"wake-sleep-cycles": """**Result: not reproduced.** The definitions give 30 WAKE-SLEEP cycles in 21 sessions, a mean of 1.43 per session (1.8 to 2.2 expected), and 3 sessions have none, although the paper kept only sessions with a full cycle. Accepting SLEEP ended by the end of the recording gives 34 cycles, a mean of 1.62, and one session without a cycle. The state table may not be the scoring the paper used (see the data check), so this may reflect the scoring as much as the definitions.""",
"fig3b-population-decline": """**Result: partially reproduced.** The population rate declines over SLEEP under both readings, more steeply than reported: R = -0.267 (p = 4.3e-06, 287 packets) per packet and R = -0.285 (p = 7.6e-07) in bins, against R = -0.11. The per-packet R is negative in 8 of 9 subjects with a cycle, and below p = 0.05 in 3.""",
"fig3-first-last-packet": """**Result: reproduced.** Over 1070 cell and cycle pairs the mean rate is 1.0915 Hz in the first packet and 0.9679 Hz in the last (both within tolerance, the last at its edge, 0.968), and the decrease is significant (Wilcoxon p = 3.9e-06). It is significant in 3 of 9 subjects alone.""",
"fig3d-first-last-slope": """**Result: reproduced.** The slope of last on first packet rates is 0.801 (95% CI 0.768 to 0.834) on log10 rates, inside the widened interval and below 1; in Hz it is 0.723. The checks do not separate this from regression to the mean: the reverse regression is also below 1 (0.864, CI 0.829 to 0.900), and the second half of the first packet regressed on its first half gives 0.855 (0.829 to 0.881), as low as the first-to-last slope. The outcome follows the criterion; the slope alone does not show that sleep tilts the rates.""",
"fig3e-wake-before-after": """**Result: partially reproduced.** pE rates are lower in the 5 min of WAKE after SLEEP (1.180 against 1.341 Hz, Wilcoxon p = 4.1e-09, reading (a)), and sextiles 4, 5 and 6 decrease (one-tailed p = 0.03, 0.00063 and 2.4e-05). The slowest sextile does not increase (mean change -0.002 Hz, p = 0.3); sextiles 2 and 3 decrease as well. Reading (b) gives the same pattern. In 23 of 30 cycles the WAKE after SLEEP is shorter than 300 s.""",
"fig3b-sextiles-over-sleep": """**Result: reproduced.** Per packet over SLEEP, sextile 6 decreases (R = -0.447, p = 3.1e-11) and sextile 1 increases (R = +0.163, p = 0.0074); sextile 5 also decreases and sextile 2 increases. In bins, sextile 6 gives R = -0.430 and sextile 1 R = +0.094 (p = 0.11). Sextile 6 has a negative R in all 7 subjects where it can be computed.""",
"fig3b-cv-over-sleep": """**Result: not reproduced.** The CV of pE rates does not change detectably over SLEEP: R = -0.026 (p = 0.66) per packet and R = -0.014 (p = 0.81) in bins.""",
"fig4iv-sextiles-within-nrem": """**Result: reproduced.** Within episodes sextile 6 decreases (R = -0.083, p = 3.7e-08) and sextile 1 increases (R = +0.060, p = 6.3e-06); within packets R = -0.055 (p = 4.4e-06) and +0.061 (p = 2e-08). The signs hold for 5 and 20 bins and for a 60 s minimum. The effects are small (normalized rates vary by under 10% across bins) and differ between subjects: within packets sextile 6 increases in Rizzo (R = +0.121) and BWRat19 and BWRat20 show no decrease.""",
"fig4v-cv-within-nrem": """**Result: not reproduced.** The CV of binned pE rates does not decrease within episodes (R = -0.005, p = 0.71) or packets (R = 0.011, p = 0.28), nor in any variant (largest absolute R 0.011).""",
"fig4vi-burst-within-nrem": """**Result: not reproduced.** The burst index rises slightly within episodes (R = 0.029, p = 0.022) and packets (R = 0.024, p = 0.021), far from the paper's p < 1e-10; the variants give R = 0.020 to 0.047. The direction is as reported, the size is not.""",
"fig4i-band-power-within-nrem": """**Result: not reproduced.** Sigma power increases within episodes and packets (R = 0.135 and 0.104, both p < 1e-20), and delta power increases within episodes (R = 0.069, p = 1.1e-07) but not within packets (R = -0.005, p = 0.61). Gamma power increases within episodes (R = +0.062) and packets (R = +0.182), the opposite of the reported decrease over episodes. One channel per session (the conversion's spindle reference) is used, which may differ from the paper's.""",
"fig4-delta-packet-length": """**Result: reproduced.** Over 915 packets, normalized delta power correlates with packet length, R = 0.334 (p = 2.8e-25), within 0.279 to 0.341, near its upper edge. The correlation is positive in 9 of 10 subjects.""",
"fig4cd-packet-rate-lfp": """**Result: partially reproduced.** All three correlations have the stated sign: sextile 6 rate against delta power R = -0.416 (p = 1.3e-28) and against gamma power R = 0.570 (p = 4.2e-57), stronger than the paper's -0.28 and 0.44, and sextile 1 rate against sigma power in the last 20 s R = 0.104 (p = 0.0029), weaker than 0.25. None is within tolerance.""",
"fig5b-nrem-between-ma": """**Result: not reproduced.** Across MA, packet, MA triplets (148 triplets), sextile 6 changes by -0.104 Hz (p = 0.077) and sextile 5 by -0.011 Hz (p = 0.24), neither at p < 0.01. With per-cell means sextile 6 decreases at p = 0.029. The direction for sextile 6 is as reported.""",
"fig5b-wake-between-packets": """**Result: not reproduced.** Across 265 packet, WAKE, packet triplets (the paper had 24), sextile 6 does not increase: its mean change is -0.051 Hz (p = 0.092). Sextiles 1 and 3 increase slightly (p = 0.0063 and 0.015). The WAKE definition here admits every Awake epoch of at least 40 s between packets (median 102 s), which likely differs from the paper's selection.""",
"fig5b-ma-between-packets": """**Result: not reproduced.** Across 391 packet, MA, packet triplets, sextile 1 does not increase significantly (+0.0034 Hz, p = 0.082), and sextiles 5 and 6 decrease (p = 0.0023 and 6.8e-05), where the paper reports no effect on fast cells. Sextile 2 increases (p = 0.00019).""",
"fig5b-rem-between-packets": """**Result: not reproduced.** Only 17 packet, REM, packet triplets exist, as 485 of 534 REM epochs are followed by Awake. Sextiles 4 and 5 decrease (p = 0.022 and 0.011) and the others do not change significantly; sextiles 1 and 2 have positive mean changes. Two of six sextiles is below the three needed for a partial result.""",
"fig5c-rem-duration": """**Result: not reproduced.** The fractional rate change across REM is not correlated with REM duration: R = -0.047 (p = 0.86) over 17 triplets, and R = -0.061 (p = 0.21) over 436 cell and triplet pairs.""",
"fig5c-sigma-ma": """**Result: not reproduced.** Over 125 MA, packet, MA triplets, sigma power in the last 20 s of the packet is not correlated with the change of sextile 1 from one MA to the next (R = 0.033, p = 0.71).""",
"fig5c-delta-change": """**Result: reproduced.** Over 613 pairs of consecutive packets, the change of sextile 1 rate correlates positively with the change of normalized delta power (R = 0.183, p = 5.3e-06), while sextile 6 correlates negatively (R = -0.368). Per subject the sextile 1 correlation is positive in 4 of 8 subjects, so the pooled result rests on some animals.""",
"figs5-within-wake-rem": """**Result: not reproduced.** Within 495 WAKE epochs, sextiles 5 and 6 decrease (R = -0.122 and -0.120, both p < 1e-12), the opposite of the reported increase, and sextiles 1 and 2 do not decrease (sextile 2 increases, R = +0.067). Within 388 REM epochs no sextile changes at p < 0.05 (largest R +0.028).""",
}
PYEOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent**

Fixing a few sentences that overstated the printed numbers, then adding the summary and building the notebook.

**Agent calls Bash**

```bash
cd $TMPDIR/w && python3 - <<'EOF'
s=open('results.py').read()
s=s.replace("and its medians vary by subject from 0.07 to 13.4 Hz.","and its per-subject medians range from 0.07 to 13.4 Hz across subjects and states.")
s=s.replace("The per-packet R is negative in 8 of 9 subjects with a cycle, and below p = 0.05 in 3.","The per-packet R is negative in 8 of 9 subjects with a cycle; two of them have p < 0.05 and one p = 0.05.")
s=s.replace("The effects are small (normalized rates vary by under 10% across bins)","The effects are small (the mean normalized rate of each sextile stays within 0.92 to 1.15 of the interval mean)")
s=s.replace("Only 17 packet, REM, packet triplets exist, as 485 of 534 REM epochs are followed by Awake.","Only 17 packet, REM, packet triplets exist, as only 49 of 534 REM epochs are followed directly by Non-REM.")
open('results.py','w').write(s)
EOF
cat > $TMPDIR/w/summary.md <<'EOF'
## Summary

| Claim | Outcome |
|---|---|
| dataset-composition | not reproduced |
| fig2a-median-rates | partially reproduced |
| fig2a-skewed-wide-distribution | partially reproduced |
| fig2a-fraction-above-2hz | not reproduced |
| fig2b-wake-nrem-slope | reproduced |
| fig2-burst-index-by-state | partially reproduced |
| fig2c-acg-peaks | partially reproduced |
| fig2c-acg-decay | blocked (methods underspecified) |
| fig2f-rate-group-correlations | partially reproduced |
| ma-statistics | not reproduced |
| ma-fraction-over-nrem-episodes | partially reproduced |
| packet-duration | reproduced |
| wake-sleep-cycles | not reproduced |
| fig3b-population-decline | partially reproduced |
| fig3-first-last-packet | reproduced |
| fig3d-first-last-slope | reproduced |
| fig3e-wake-before-after | partially reproduced |
| fig3b-sextiles-over-sleep | reproduced |
| fig3b-cv-over-sleep | not reproduced |
| fig4iv-sextiles-within-nrem | reproduced |
| fig4v-cv-within-nrem | not reproduced |
| fig4vi-burst-within-nrem | not reproduced |
| fig4i-band-power-within-nrem | not reproduced |
| fig4-delta-packet-length | reproduced |
| fig4cd-packet-rate-lfp | partially reproduced |
| fig5b-nrem-between-ma | not reproduced |
| fig5b-wake-between-packets | not reproduced |
| fig5b-ma-between-packets | not reproduced |
| fig5b-rem-between-packets | not reproduced |
| fig5c-rem-duration | not reproduced |
| fig5c-sigma-ma | not reproduced |
| fig5c-delta-change | reproduced |
| figs5-within-wake-rem | not reproduced |
| fig5c-wake-movement | blocked (data missing) |
| updown-durations | blocked (methods underspecified) |
| fig3c-slow-oscillation-spindles-over-sleep | blocked (methods underspecified) |
| fig4ii-iii-updown-spindles-within-packets | blocked (methods underspecified) |
| fig2de-up-state-sequences | blocked (methods underspecified) |
| fig3f-4e-within-up-rates | blocked (methods underspecified) |

Of 39 claims, 8 are reproduced, 9 partially reproduced, 15 not reproduced and 7 blocked.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method.

**Blocked claims.** UP and DOWN states, spindles and the autocorrelogram decay fit are detected or fitted by procedures described in the Supplemental Experimental Procedures, which could not be retrieved; the main text names the approach (spike and LFP criteria after Vyazovskiy et al. 2009; spindles "after filtering and integration") without thresholds, so the procedures are not fixed for this attempt. The movement of the animal during WAKE is not in the dandiset (no accelerometer, video or EMG).

**How the analysis differs from the paper's.**

- 21 of the paper's 27 sessions and 10 of its 11 rats: the dandiset holds 22 sessions, and one (Dino-072114) has unusable spike times. 812 pE and 89 pI cells, against 995 and 126.
- The states are the dandiset's table (Awake, Non-REM, REM). Microarousals are derived from Awake epochs under 40 s between two Non-REM epochs, without the paper's EMG and theta criteria. WAKE-SLEEP cycles, packets and episodes are rebuilt from the Results' definitions; the paper's Table 1 was not available.
- Time courses use 10 normalized bins, packets and episodes of at least 20 s, and group means normalized within each interval; the paper does not give its binning. Variants with 5 and 20 bins and a 60 s minimum are shown.
- LFP is one channel per session (the electrode the conversion flags as spindle reference), in raw units, with power from 2 s windows; the LFP of Dino-061914 is left out as its samples are scrambled.
- Statistics are over cells, or cell and interval pairs, pooled across sessions, as the paper's per-cell statistics; the per-subject results are printed for each claim. No random numbers are used.

**What was found about the dandiset.**

- The dandiset description and the paper give 11 animals and 27 sessions; the files hold 10 animals and 22 sessions, and 945 units (826 excitatory, 96 inhibitory, 23 unknown) where the description gives 995 pE and 126 pI.
- Dino-072114: spike times are whole seconds divided by 20000 (8451 distinct values, from 0 to 0.4252 s, in a 7959 s recording).
- Dino-061914: the LFP has 125 columns for 128 electrodes, lasts 331.7 min against 291.9 min of states and spikes, and its samples are scrambled (lag-1 autocorrelation 0.28, against 0.99 or more elsewhere).
- The state table has no microarousal label, though the paper scores MAs as a state; the derived MAs are rarer than the paper reports (391 in 21 sessions against 790 in 27), and only 49 of 534 REM epochs are followed directly by Non-REM.
- The LFP is stored as int16 with unit volts and conversion NaN, so it cannot be put in volts. Every electrode's location is "unknown" (the electrode groups carry a region), and every unit's region is "CTX" or "unknown".
- 23 units of BWRat21-121613 have cell type and region "unknown", with no description.
- The state labels are consistent with the spikes in 20 of 21 sessions (not established for BWRat21-121813); the best match is often with the table shifted 5 to 60 s earlier. The LFP is consistent with the spikes at 50 ms precision in 14 of 21 sessions.
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent**

Building the notebook, entry files, and running lock and the full check-and-run.

**Agent calls Bash**

```bash
cd $TMPDIR/w && cat > build.py <<'EOF'
import re, nbformat, sys
sys.path.insert(0,'.')
from results import R
src=open('nb_src.py').read()
parts=re.split(r'^(# %%.*)$', src, flags=re.M)
nb=nbformat.v4.new_notebook()
cells=[]
for i in range(1,len(parts),2):
    head, body = parts[i], parts[i+1].strip('\n')
    if '[markdown]' in head:
        text='\n'.join(l[2:] if l.startswith('# ') else ('' if l=='#' else l) for l in body.splitlines())
        if text.strip()=='## Summary':
            text=open('summary.md').read().strip()
        cells.append(nbformat.v4.new_markdown_cell(text))
    else:
        m=re.search(r'tags=\[(.*)\]', head)
        tags=[t.strip().strip('"') for t in m.group(1).split(',')] if m else []
        c=nbformat.v4.new_code_cell(body); c.metadata['tags']=tags
        cells.append(c)
        for t in tags:
            if t.startswith('claim:'):
                cells.append(nbformat.v4.new_markdown_cell(R[t[6:]]))
nb.cells=cells
nb.metadata['kernelspec']={'name':'python3','display_name':'Python 3','language':'python'}
nb.metadata['language_info']={'name':'python'}
nbformat.write(nb, 'entries/000041-watson-2016/reproduce_watson_2016.ipynb')
missing=set(R)-{t[6:] for c in cells if c.cell_type=='code' for t in c.metadata['tags'] if t.startswith('claim:')}
print(len(cells),'cells; results without cell:',missing)
EOF
$TMPDIR/venv/bin/python build.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/w/build.py", line 1, in <module>
    import re, nbformat, sys
ModuleNotFoundError: No module named 'nbformat'
```

**Agent calls Bash**

```bash
cd $TMPDIR/w && python3 build.py
```

```
109 cells; results without cell: set()
Shell cwd was reset to
```

**Agent**

Now entry.yaml, requirements.in and README.

**Agent calls Bash**

```bash
cd entries/000041-watson-2016 && cat > entry.yaml <<'EOF'
schema_version: 1
name: 000041-watson-2016
type: reproduction
title: Firing rates across sleep states in rat frontal cortex (Watson et al. 2016)
description: Tests the findings of Watson, Levenstein, Greene, Gelinas and Buzsaki (2016) on dandiset
  000041, which holds silicon probe recordings of units, LFP and sleep states from the frontal cortex
  of 10 rats in their home cage. It compares firing rates and bursting across WAKE, nonREM and REM,
  how rates of fast and slow firing cells change over sleep and within nonREM packets, how they relate
  to LFP band power, and the rate changes across state triplets. UP and DOWN state and spindle
  analyses are blocked, as their methods are in the unavailable supplement.
license: Apache-2.0
notebooks:
- path: reproduce_watson_2016.ipynb
  title: Reproducing Watson et al. (2016) from dandiset 000041
  runtime_minutes: 6
helpers:
- sleepstates.py
related:
- id: dandi:000041/0.250624.0419
  relation: uses_data
- id: doi:10.1016/j.neuron.2016.03.036
  relation: reproduces
EOF
cat > requirements.in <<'EOF'
dandi
h5py
matplotlib
numpy
pandas
remfile
scipy
EOF
cat ../001453-fouke-2025/requirements.lock.txt | head -5; cat ../../schemas/entry.schema.json | python3 -c "import json,sys; d=json.load(sys.stdin); print(d['properties'].keys())"
```

```
# This file was autogenerated by uv via the following command:
#    uv pip compile --python-version 3.13 requirements.in -o requirements.lock.txt
acres==0.5.0
    # via bidsschematools
aiohappyeyeballs==2.7.1
dict_keys(['schema_version', 'name', 'type', 'title', 'description', 'license', 'notebooks', 'helpers', 'related'])
```

**Agent calls Bash**

```bash
cd  && python tools/entry.py lock entries/000041-watson-2016 2>&1 | tail -3 && python tools/entry.py check entries/000041-watson-2016 2>&1 | tail -20
```

```
wrote entries/000041-watson-2016/requirements.lock.txt
0 error(s)
```

**Agent calls Bash**

```bash
time python tools/entry.py all entries/000041-watson-2016 2>&1 | tail -30
```

```
Installed kernelspec registry-000041-watson-2016 in executed/000041-watson-2016/.venv/share/jupyter/kernels/registry-000041-watson-2016
0 error(s)
pass  reproduce_watson_2016.ipynb  (233 s)

real	3m59.459s
user	2m19.640s
sys	0m8.560s
```

**Agent**

Ran in 233 s. Now reading the executed notebook to confirm the conclusions match the printed numbers.

**Agent calls Bash**

```bash
ls executed/000041-watson-2016/ && python3 - <<'EOF' > $TMPDIR/w/exec_out.txt
import nbformat
nb=nbformat.read('executed/000041-watson-2016/reproduce_watson_2016.ipynb',4)
for c in nb.cells:
    if c.cell_type=='code':
        print('---', c.metadata.get('tags'))
        for o in c.outputs:
            if o.output_type=='stream': print(o.text)
            elif o.output_type=='error': print('ERROR', o.ename, o.evalue)
            elif 'text/plain' in o.get('data',{}): print(o['data']['text/plain'][:200])
EOF
wc -l $TMPDIR/w/exec_out.txt; grep -c ERROR $TMPDIR/w/exec_out.txt; grep -n "Warning" $TMPDIR/w/exec_out.txt | head; diff <(grep -v "^\[\|=====" $TMPDIR/w/out3.txt | grep -v "^$" | head -100) <(grep -v "^---" $TMPDIR/w/exec_out.txt | grep -v "^$" | head -100) | head -40
```

```
reproduce_watson_2016.ipynb
result.json
697 /tmp/claude-1001/w/exec_out.txt
0
```

**Agent calls Bash**

```bash
cd $TMPDIR/w; diff <(grep -v "^\[[0-9.]*s\]$\|^=====" out3.txt | grep -v "^$" | grep -v "Warning\|c /= stddev") <(grep -v "^---" exec_out.txt | grep -v "^$") | head -40; echo; grep -n "Figure\|<Figure" exec_out.txt | head
```

```
128a129
> <Figure size 500x350 with 1 Axes>
165a167
> <Figure size 400x400 with 1 Axes>
193a196
> <Figure size 900x300 with 2 Axes>
420a424
> <Figure size 900x300 with 2 Axes>

155:<Figure size 500x350 with 1 Axes>
200:<Figure size 400x400 with 1 Axes>
236:<Figure size 900x300 with 2 Axes>
519:<Figure size 900x300 with 2 Axes>
Shell cwd was reset to
```

**Agent**

Executed outputs are identical to the prototype run the conclusions were written from. A last spot check of numbers quoted in the summary:

**Agent calls Bash**

```bash
cd $TMPDIR/w; grep -n "of 21 |\|Shift with the largest contrast, counts\|REM epochs followed\|MAs: \|Awake epochs under 40" exec_out.txt
```

```
82:State labels consistent with the spikes (largest contrast within 60 s of zero shift and above the contrast at +-300 s): 20 of 21 | not established: [np.str_('BWRat21_121813')]
83:LFP consistent with the spikes (largest |r| within 50 ms of zero lag and over 3 times |r| at +-1 s): 14 of 21 | not established: [np.str_('BWRat17_121912'), np.str_('BWRat21_121113'), np.str_('BWRat21_121613'), np.str_('BWRat21_121813'), np.str_('Bogey_012615'), np.str_('Dino_061914'), np.str_('Dino_072414')]
84:Shift with the largest contrast, counts: {-60: 3, -20: 4, -5: 7, 0: 6, 20: 1}
322:MAs: 391 in all, 262 inside SLEEP periods (paper: 790 in 27 sessions)
324:Awake epochs under 40 s not between two Non-REM epochs (left as WAKE): 345
675:REM epochs followed by Non-REM: 49 of 534 REM epochs
Shell cwd was reset to
```

**Agent**

Everything matches. Writing the entry README, setting the runtime to 4 min, and writing the attempt record.

**Agent calls Bash**

```bash
cd entries/000041-watson-2016 && sed -i 's/runtime_minutes: 6/runtime_minutes: 4/' entry.yaml && cat > README.md <<'EOF'
# Watson, Levenstein, Greene, Gelinas & Buzsáki (2016) from dandiset 000041

Tests the findings of [Watson et al. (2016)](https://doi.org/10.1016/j.neuron.2016.03.036) that can be
tested on [DANDI:000041](https://dandiarchive.org/dandiset/000041/0.250624.0419), which holds units,
LFP and sleep states recorded with silicon probes in the frontal cortex of rats in their home cage.
The dandiset holds 22 of the paper's 27 sessions and 10 of its 11 rats; one session's spike times
are unusable.

| Claim | Outcome |
|---|---|
| 11 rats, 27 sessions, 995 pE and 126 pI cells | Not reproduced |
| Median rates by state (pE 0.76, 0.69, 0.88 Hz; pI 5.59, 4.69, 4.25 Hz) | Partially reproduced |
| pE rates skewed, spanning 0.05 to 5 Hz | Partially reproduced |
| Fraction of pE cells above 2 Hz lower in nonREM | Not reproduced |
| nonREM against WAKE rates, slope below 1 | Reproduced |
| Burst index highest in nonREM, lowest in WAKE | Partially reproduced |
| Autocorrelogram peaks at 8 ms (nonREM) and 125 ms (REM, WAKE) | Partially reproduced |
| Pairwise correlations by rate group in nonREM | Partially reproduced |
| Microarousal duration, frequency and share of SLEEP | Not reproduced |
| MA fraction decreases over nonREM episodes | Partially reproduced |
| Median nonREM packet 111 s | Reproduced |
| About 2 WAKE-SLEEP cycles per session | Not reproduced |
| Population rate declines over SLEEP | Partially reproduced |
| Lower rate in the last than the first packet of SLEEP | Reproduced |
| First against last packet slope below 1 | Reproduced |
| Lower rates in WAKE after SLEEP, by sextile | Partially reproduced |
| Fastest sextile slows and slowest speeds up over SLEEP | Reproduced |
| CV of rates decreases over SLEEP | Not reproduced |
| Fastest sextile slows and slowest speeds up within nonREM | Reproduced |
| CV and burst index change within nonREM | Not reproduced (two claims) |
| Band power changes within nonREM | Not reproduced |
| Packet delta power grows with packet length | Reproduced |
| Packet rates against delta, gamma and sigma power | Partially reproduced |
| Rate changes across MA, WAKE and REM triplets (four claims) | Not reproduced |
| REM duration and packet-end sigma against rate changes | Not reproduced (two claims) |
| Slow sextile change against delta power change | Reproduced |
| Rate changes within WAKE and REM | Not reproduced |
| WAKE movement against rate change | Blocked: data missing |
| UP/DOWN states, spindles, autocorrelogram decay (six claims) | Blocked: methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The state table in the files has no microarousal label, so microarousals are derived from short Awake
epochs between Non-REM epochs; the claims on state triplets depend on this. The supplement, which
describes UP/DOWN state and spindle detection, could not be retrieved. The attempt record, with the
reasons and the differences from the paper's method, is
[`attempts/000041-watson-2016-01.yaml`](../../attempts/000041-watson-2016-01.yaml).

- `reproduce_watson_2016.ipynb`: the analysis. It takes about four minutes, two of them streaming the
  files with six processes.
- `sleepstates.py`: loading the files, the derived states (microarousals, packets, episodes, SLEEP
  periods and WAKE-SLEEP cycles), rates, burst index, autocorrelograms and LFP band power. Other
  notebooks on this dandiset can import it.
EOF
echo done
```

```
done
```

**Agent calls Write**

```json
{
 "file_path": "attempts/000041-watson-2016-01.yaml",
 "content": "schema_version: 1\nid: 000041-watson-2016-01\ndandiset: \"000041\"\ndandiset_version: 0.250624.0419\npaper: doi:10.1016/j.neuron.2016.03.036\ndate: 2026-10-16\nentry: 000041-watson-2016\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code (GitHub Actions)\n    model: claude-opus-5-5\n    protocol: pilot-7\noutcomes:\n- claim: dataset-composition\n  outcome: not_reproduced\n  notebook: reproduce_watson_2016.ipynb\n  output: claim:dataset-composition\n  measured:\n  - 10\n  - 22\n  - 286.8\n  - 826\n  - 96\n  notes: Two of five values are within tolerance, 10 rats and a mean session duration of 286.8 min\n    (SD 150.2). The files hold 22 sessions, 826 excitatory and 96 inhibitory units (and 23 of\n    unknown type); the 21 usable sessions hold 812 pE and 89 pI cells. Per session the pE count is\n    close to the paper's (mean 38.7, range 10 to 105, against 36.9 and 10 to 104).\n  deviations:\n  - Counted on the files as deposited, with session duration from the state table.\n- claim: fig2a-median-rates\n  outcome: partially_reproduced\n  notebook: reproduce_watson_2016.ipynb\n  output: claim:fig2a-median-rates\n  measured:\n  - 0.755\n  - 0.662\n  - 0.825\n  - 3.917\n  - 2.73\n  - 3.062\n  notes: Under reading (a) the three pE medians are within tolerance (0.755, 0.662 and 0.825 Hz)\n    and the three pI medians are below it (3.92, 2.73 and 3.06 Hz, against 5.59, 4.69 and 4.25).\n    Reading (b) gives the same counts (pE WAKE 0.748). The pI sample is 89 cells in 9 subjects,\n    with per-subject medians from 0.07 to 13.4 Hz across subjects and states.\n  deviations:\n  - 812 pE and 89 pI cells from 21 sessions, against 995 and 126 from 27.\n  - WAKE excludes microarousals derived from the Awake label, not the paper's scored MAs.\n- claim: fig2a-skewed-wide-distribution\n  outcome: partially_reproduced\n  notebook: reproduce_watson_2016.ipynb\n  output: claim:fig2a-skewed-wide-distribution\n  notes: WAKE rates have skewness 4.57 and a 97.5th percentile of 7.17 Hz (within a factor of 2 of 5\n    Hz), but the 2.5th percentile is 0.0124 Hz, about four times below 0.05 Hz. 13 of 812 cells have\n    a WAKE rate of zero. The log10 rates are skewed to the left (-0.74).\n  deviations:\n  - The paper's range is read from a log axis; the factor-of-2 tolerance was fixed in the\n    criterion.\n- claim: fig2a-fraction-above-2hz\n  outcome: not_reproduced\n  notebook: reproduce_watson_2016.ipynb\n  output: claim:fig2a-fraction-above-2hz\n  measured:\n  - 17.0\n  - 18.72\n  - 9.11\n  notes: REM (18.7%) and nonREM (9.1%) are within tolerance, WAKE (17.0%) is not. nonREM is lower\n    than WAKE (chi-square 21.5, p = 3.5e-06) and REM (30.5, p = 3.4e-08), but neither test reaches\n    p < 1e-10, which the criterion requires. The direction of the effect is as in the paper, with\n    fewer cells than the paper had.\n- claim: fig2b-wake-nrem-slope\n  outcome: reproduced\n  notebook: reproduce_watson_2016.ipynb\n  output: claim:fig2b-wake-nrem-slope\n  measured:\n  - 0.862\n  - 0.757\n  notes: On log10 rates (799 cells, 13 with a zero rate left out), R = 0.862 and the slope of\n    nonREM on WAKE is 0.757 (95% CI 0.727 to 0.788). In Hz the slope is 0.583 (0.560 to 0.607),\n    outside the widened interval. The reverse regression on log10 rates gives 0.982 (0.942 to\n    1.022), so the slope below 1 may in part be regression to the mean. Per subject the slope ranges\n    from 0.41 to 0.91.\n  deviations:\n  - The paper does not say whether the slope is on log or linear rates; both readings are shown and\n    the log reading matches.\n- claim: fig2-burst-index-by-state\n  outcome: partially_reproduced\n  notebook: reproduce_watson_2016.ipynb\n  output: claim:fig2-burst-index-by-state\n  measured:\n  - 6.35\n  - 2.64\n  - 3.65\n  notes: The order nonREM > REM > WAKE holds under both readings, with Kruskal-Wallis p = 5.7e-36\n    (a) and 7.3e-38 (b), and REM above WAKE (paired Wilcoxon p = 1e-32). Reading (a), the fraction\n    of intervals under 15 ms, gives medians of 6.35, 2.64 and 3.65%, none within tolerance; reading\n    (b), the fraction of spikes in such an interval, gives 11.67% in nonREM (within tolerance), 4.95%\n    in WAKE and 6.71% in REM (above). The measured values are those of reading (a), the first listed.\n  deviations:\n  - The definition \"fraction of spikes with ISIs under 15 ms\" can be read two ways; both are shown\n    and neither matches all three medians.\n- claim: fig2c-acg-peaks\n  outcome: partially_reproduced\n  notebook: reproduce_watson_2016.ipynb\n  output: claim:fig2c-acg-peaks\n  notes: The nonREM autocorrelogram peaks at 7.5 ms. The smoothed REM and WAKE autocorrelograms are\n    highest at the 60 ms edge of the 60 to 250 ms window, so the criterion finds no theta peak. In a\n    variant that divides the 21 ms smoothing by a 101 ms one, WAKE has a maximum at 118.5 ms (ratio\n    1.017) and REM at 149.5 ms (1.018). Per subject the REM maximum falls within 112.5 to 137.5 ms in\n    two subjects (Bogey 135.5, Dino 125.5).\n  deviations:\n  - The peak location criteria (windows, 21 ms smoothing) were fixed here; the paper shows the peaks\n    in a figure only.\n- claim: fig2c-acg-decay\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notes: The main text gives decay fit exponents but not what is fitted (function, lag range); the\n    Supplemental Experimental Procedures, which would say, could not be retrieved (PubMed Central\n    and the publisher answer with a browser check). The autocorrelograms themselves are computed for\n    fig2c-acg-peaks.\n- claim: fig2f-rate-group-correlations\n  outcome: partially_reproduced\n  notebook: reproduce_watson_2016.ipynb\n  output: claim:fig2f-rate-group-correlations\n  notes: Over 20764 same-session pE pairs (169 without a defined correlation), the (6,6) mean\n    correlation of 100 ms counts in nonREM is 0.0424, the largest of the 21 group combinations, and\n    correlations rise with the rates of both cells. The (1,6) mean is 0.0089, above zero (t = 10.85,\n    p = 8.7e-26); 22.8% of all pairs are negative, but no group combination has a negative mean.\n    Reading (b) gives the same pattern ((6,6) 0.0401, (1,6) 0.0087).\n  deviations:\n  - The correlation measure is Pearson correlation of raw counts in 100 ms bins; the paper's\n    measure and test are in the unavailable supplement and may differ (for example a correction\n    for the shared UP/DOWN modulation).\n- claim: ma-statistics\n  outcome: not_reproduced\n  notebook: reproduce_watson_2016.ipynb\n  output: claim:ma-statistics\n  measured:\n  - 19.0\n  - 0.096\n  - 3.22\n  notes: Under reading (a), median MA duration 19.0 s (within the spread), 0.096 MAs per minute of\n    SLEEP and 3.22% of SLEEP time; reading (b) gives 19.0 s, 0.127 per min and 4.23%. The paper\n    reports 0.32 and 9.1%. 391 MAs in 21 sessions (262 inside SLEEP periods), against 790 in 27.\n  deviations:\n  - The dandiset has no microarousal label. MAs are derived from Awake epochs under 40 s between two\n    Non-REM epochs, without the paper's EMG and theta criteria; 345 short Awake epochs elsewhere are\n    left as WAKE.\n  - The state table has 1 s resolution and may not be the scoring the paper used.\n- claim: ma-fraction-over-nrem-episodes\n  outcome: partially_reproduced\n  notebook: reproduce_watson_2016.ipynb\n  output: claim:ma-fraction-over-nrem-episodes\n  measured: -0.451\n  notes: Over 243 episodes with an MA, pooled episode bins give R = -0.087 (p = 1.7e-05); the bin\n    means give R = -0.451 (p = 0.19). Neither reaches -0.85 or p < 1e-10. The mean fraction rises\n    from 0.067 to 0.157 over the first six bins and falls to 0.010 in the last.\n  deviations:\n  - MAs derived from the Awake label (see ma-statistics); the binning was fixed here.\n- claim: packet-duration\n  outcome: reproduced\n  notebook: reproduce_watson_2016.ipynb\n  output: claim:packet-duration\n  measured: 108\n  notes: Over all 1069 Non-REM epochs the median is 108 s (5th to 95th percentile 12 to 484 s, range\n    6 to 1199 s). Inside SLEEP periods (685 epochs) the median is 128 s, outside tolerance. Per\n    subject medians range from 76 to 219 s.\n  deviations:\n  - A packet is one Non-REM epoch of the dandiset's state table.\n- claim: wake-sleep-cycles\n  outcome: not_reproduced\n  notebook: reproduce_watson_2016.ipynb\n  output: claim:wake-sleep-cycles\n  measured: 1.43\n  notes: 30 cycles in 21 sessions, 1.43 per session, and 3 sessions (BWRat18-020513, BWRat19-032413,\n    BWRat20-101013) have none. Accepting SLEEP ended by the end of the recording gives 34 cycles (1.62\n    per session) and one session without a cycle.\n  deviations:\n  - SLEEP and cycles are rebuilt from the Results' definitions on the dandiset's state table; the\n    paper's Table 1 was not available, and its state scoring and MAs may differ.\n- claim: fig3b-population-decline\n  outcome: partially_reproduced\n  notebook: reproduce_watson_2016.ipynb\n  output: claim:fig3b-population-decline\n  measured: -0.267\n  notes: Per packet R = -0.267 (p = 4.3e-06, 287 packets in 30 cycles); in 10 bins R = -0.285 (p =\n    7.6e-07). The decline is steeper than the reported R = -0.11. R is negative in 8 of 9 subjects\n    with a cycle.\n  deviations:\n  - The paper does not give its binning or normalization; two readings were fixed in the criterion.\n  - 30 cycles from 21 sessions, against 54 from 27.\n  depends_on_note: null\n- claim: fig3-first-last-packet\n  outcome: reproduced\n  notebook: reproduce_watson_2016.ipynb\n  output: claim:fig3-first-last-packet\n  measured:\n  - 1.0915\n  - 0.9679\n  notes: Over 1070 cell and cycle pairs, 1.0915 plus or minus 1.483 Hz in the first packet and 0.9679\n    plus or minus 1.241 Hz in the last (the upper bound of tolerance is 0.968), Wilcoxon p = 3.9e-06.\n    The decrease is significant within 3 of 9 subjects.\n  deviations:\n  - 30 cycles from 21 sessions, against 54 from 27.\n- claim: fig3d-first-last-slope\n  outcome: reproduced\n  notebook: reproduce_watson_2016.ipynb\n  output: claim:fig3d-first-last-slope\n  measured: 0.801\n  notes: On log10 rates (1021 pairs, 49 with a zero rate left out) the slope of last on first is\n    0.801 (95% CI 0.768 to 0.834); in Hz 0.723. The reverse regression gives 0.864 (0.829 to 0.900),\n    and the second half of the first packet regressed on its first half gives 0.855 (0.829 to\n    0.881). A slope below 1 of this size thus arises within a single packet, so it does not by itself\n    show a change across sleep; the criterion, fixed before the analysis, judges the slope alone.\n  deviations:\n  - The paper does not say whether the regression is on log or linear rates; both are shown.\n- claim: fig3e-wake-before-after\n  outcome: partially_reproduced\n  notebook: reproduce_watson_2016.ipynb\n  output: claim:fig3e-wake-before-after\n  notes: Reading (a), 1070 cell and cycle pairs, mean 1.341 Hz before and 1.180 Hz after, Wilcoxon p\n    = 4.1e-09. Sextiles 4, 5 and 6 decrease (one-tailed p = 0.03, 0.00063, 2.4e-05); sextile 1 does\n    not increase (mean change -0.002 Hz, p = 0.3), and sextiles 2 and 3 decrease. Reading (b), 727\n    cells, gives the same pattern (population p = 1.4e-09, sextile 1 p = 0.36). In 23 of 30 cycles the\n    WAKE after SLEEP is shorter than 300 s.\n  deviations:\n  - Where the WAKE after SLEEP is shorter than 5 min, all of it is used.\n- claim: fig3b-sextiles-over-sleep\n  outcome: reproduced\n  notebook: reproduce_watson_2016.ipynb\n  output: claim:fig3b-sextiles-over-sleep\n  notes: Per packet, sextile 6 R = -0.447 (p = 3.1e-11) and sextile 1 R = +0.163 (p = 0.0074);\n    sextile 5 R = -0.341 and sextile 2 R = +0.143. In bins, sextile 6 R = -0.430 (p = 2e-11) and\n    sextile 1 R = +0.094 (p = 0.11). Sextile 6 has a negative R in all 7 subjects where it can be\n    computed.\n  deviations:\n  - Binning and normalization fixed here (see fig3b-population-decline).\n- claim: fig3b-cv-over-sleep\n  outcome: not_reproduced\n  notebook: reproduce_watson_2016.ipynb\n  output: claim:fig3b-cv-over-sleep\n  notes: R = -0.026 (p = 0.66) per packet and R = -0.014 (p = 0.81) in bins.\n  deviations:\n  - The CV is taken across a session's pE cells at each point; the paper does not define it\n    further.\n- claim: fig4iv-sextiles-within-nrem\n  outcome: reproduced\n  notebook: reproduce_watson_2016.ipynb\n  output: claim:fig4iv-sextiles-within-nrem\n  notes: Within 622 episodes, sextile 6 R = -0.083 (p = 3.7e-08) and sextile 1 R = +0.060 (p =\n    6.3e-06); within 952 packets, R = -0.055 (p = 4.4e-06) and +0.061 (p = 2e-08). The signs hold\n    with 5 or 20 bins and with a 60 s minimum. The effects are small, and per subject within packets\n    sextile 6 increases in Rizzo (R = +0.121) and does not decrease in BWRat19 and BWRat20.\n  deviations:\n  - 10 bins, a 20 s minimum and normalization within each interval were fixed here.\n- claim: fig4v-cv-within-nrem\n  outcome: not_reproduced\n  notebook: reproduce_watson_2016.ipynb\n  output: claim:fig4v-cv-within-nrem\n  notes: Episodes R = -0.005 (p = 0.71), packets R = 0.011 (p = 0.28); no variant exceeds an absolute\n    R of 0.011.\n- claim: fig4vi-burst-within-nrem\n  outcome: not_reproduced\n  notebook: reproduce_watson_2016.ipynb\n  output: claim:fig4vi-burst-within-nrem\n  notes: Episodes R = 0.029 (p = 0.022), packets R = 0.024 (p = 0.021); variants give R = 0.020 to\n    0.047 with p from 0.069 to 0.0008. The burst index rises in the reported direction, but far from\n    p < 1e-10.\n  deviations:\n  - The burst index per bin is pooled over the session's pE cells (fraction of intervals under 15\n    ms).\n- claim: fig4i-band-power-within-nrem\n  outcome: not_reproduced\n  notebook: reproduce_watson_2016.ipynb\n  output: claim:fig4i-band-power-within-nrem\n  notes: Sigma rises within episodes (R = 0.135) and packets (R = 0.104), both p < 1e-20. Delta rises\n    within episodes (R = 0.069, p = 1.1e-07) but not within packets (R = -0.005, p = 0.61; with a 60 s\n    minimum R = 0.022, p = 0.063). Gamma rises within episodes (R = 0.062) and packets (R = 0.182),\n    where the paper reports a fall over episodes.\n  deviations:\n  - One LFP channel per session, the one the conversion flags as spindle reference, in raw units;\n    the paper's channel choice is not stated in the main text.\n  - The LFP of Dino-061914 is left out (scrambled samples).\n- claim: fig4-delta-packet-length\n  outcome: reproduced\n  notebook: reproduce_watson_2016.ipynb\n  output: claim:fig4-delta-packet-length\n  measured: 0.334\n  notes: Over 915 packets of at least 20 s, R = 0.334 (p = 2.8e-25), near the upper edge of 0.279 to\n    0.341; Spearman rho = 0.555. Positive in 9 of 10 subjects (Templeton -0.101).\n  deviations:\n  - One LFP channel per session; Dino-061914 left out.\n- claim: fig4cd-packet-rate-lfp\n  outcome: partially_reproduced\n  notebook: reproduce_watson_2016.ipynb\n  output: claim:fig4cd-packet-rate-lfp\n  measured:\n  - -0.416\n  - 0.57\n  - 0.104\n  notes: All three signs as stated. Sextile 6 against delta R = -0.416 (p = 1.3e-28) and against\n    gamma R = 0.570 (p = 4.2e-57), both stronger than reported; sextile 1 against sigma in the last\n    20 s R = 0.104 (p = 0.0029), weaker than 0.25 and above p < 1e-10. None within tolerance.\n  deviations:\n  - One LFP channel per session; Dino-061914 left out; z-scoring per session fixed here.\n- claim: fig5b-nrem-between-ma\n  outcome: not_reproduced\n  notebook: reproduce_watson_2016.ipynb\n  output: claim:fig5b-nrem-between-ma\n  notes: 148 triplets, 6073 cell and triplet pairs. Sextile 6 mean change -0.104 Hz (p = 0.077),\n    sextile 5 -0.011 Hz (p = 0.24). With per-cell means, sextile 6 -0.120 Hz (p = 0.029) and\n    sextile 5 p = 0.79.\n  deviations:\n  - MAs derived from the Awake label (see ma-statistics).\n- claim: fig5b-wake-between-packets\n  outcome: not_reproduced\n  notebook: reproduce_watson_2016.ipynb\n  output: claim:fig5b-wake-between-packets\n  notes: 265 triplets (the paper had 24). Sextile 6 mean change -0.051 Hz (p = 0.092); sextiles 1 and\n    3 increase slightly (p = 0.0063 and 0.015). The intervening WAKE lasts 40 to 3945 s (median 102).\n  deviations:\n  - Every Awake epoch of at least 40 s between two Non-REM epochs counts as WAKE here; the paper's\n    24 triplets suggest a narrower selection that the main text does not describe.\n- claim: fig5b-ma-between-packets\n  outcome: not_reproduced\n  notebook: reproduce_watson_2016.ipynb\n  output: claim:fig5b-ma-between-packets\n  notes: 391 triplets. Sextile 1 mean change +0.0034 Hz (p = 0.082); sextiles 5 and 6 decrease (p =\n    0.0023 and 6.8e-05), and sextile 2 increases (p = 0.00019).\n  deviations:\n  - MAs derived from the Awake label (see ma-statistics).\n- claim: fig5b-rem-between-packets\n  outcome: not_reproduced\n  notebook: reproduce_watson_2016.ipynb\n  output: claim:fig5b-rem-between-packets\n  notes: Only 17 triplets, as 49 of 534 REM epochs are followed directly by Non-REM. Sextiles 4 and 5\n    decrease (p = 0.022 and 0.011); the other four do not change significantly, and sextiles 1 and 2\n    have positive mean changes.\n  deviations:\n  - The paper does not give its number of REM triplets; the dandiset's state table yields few.\n- claim: fig5c-rem-duration\n  outcome: not_reproduced\n  notebook: reproduce_watson_2016.ipynb\n  output: claim:fig5c-rem-duration\n  measured: -0.047\n  notes: Per triplet R = -0.047 (p = 0.86, 17 triplets); per cell and triplet R = -0.061 (p = 0.21,\n    436 pairs). REM durations 8 to 157 s.\n- claim: fig5c-sigma-ma\n  outcome: not_reproduced\n  notebook: reproduce_watson_2016.ipynb\n  output: claim:fig5c-sigma-ma\n  measured: 0.033\n  notes: Over 125 MA, packet, MA triplets with sextile 1 cells and LFP, R = 0.033 (p = 0.71).\n  deviations:\n  - MAs derived from the Awake label; one LFP channel per session; Dino-061914 left out.\n- claim: fig5c-delta-change\n  outcome: reproduced\n  notebook: reproduce_watson_2016.ipynb\n  output: claim:fig5c-delta-change\n  notes: Over 613 consecutive packet pairs, R = 0.183 (p = 5.3e-06) for sextile 1, and R = -0.368 for\n    sextile 6. Per subject the sextile 1 correlation is positive in 4 of 8 subjects, so the pooled\n    result rests on some animals.\n  deviations:\n  - One LFP channel per session; Dino-061914 left out.\n- claim: figs5-within-wake-rem\n  outcome: not_reproduced\n  notebook: reproduce_watson_2016.ipynb\n  output: claim:figs5-within-wake-rem\n  notes: Within 495 WAKE epochs sextiles 5 and 6 decrease (R = -0.122 and -0.120, p < 1e-12),\n    opposite to the claim, and sextile 2 increases (R = +0.067). Within 388 REM epochs no sextile\n    changes at p < 0.05.\n  deviations:\n  - The paper's analysis for this claim is in Figure S5, which was not available; entry into WAKE\n    may have been analysed differently (for example aligned to WAKE onset).\n- claim: fig5c-wake-movement\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The dandiset holds no movement, accelerometer, video or EMG data (acquisition is empty; the\n    files hold units, LFP, spike waveforms and the state table), and no other public source of the\n    movement measurements was found.\n- claim: updown-durations\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notes: UP and DOWN states were detected with spike and LFP criteria whose thresholds are given only\n    in the Supplemental Experimental Procedures, which could not be retrieved. The spikes and LFP\n    needed are in the dandiset.\n- claim: fig3c-slow-oscillation-spindles-over-sleep\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notes: Needs UP/DOWN state and spindle detection, described only in the unavailable supplement (see\n    updown-durations); the main text says only that spindles were detected after filtering and\n    integration.\n- claim: fig4ii-iii-updown-spindles-within-packets\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notes: Needs UP/DOWN state and spindle detection (see fig3c-slow-oscillation-spindles-over-sleep).\n- claim: fig2de-up-state-sequences\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notes: Needs UP state onsets (see updown-durations).\n- claim: fig3f-4e-within-up-rates\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notes: Needs UP state detection (see updown-durations).\nfindings:\n- kind: data_missing\n  statement: The dandiset holds 22 sessions from 10 rats, where the paper and the dandiset's own\n    description report 27 sessions from 11 rats; the files hold 945 units (826 excitatory, 96\n    inhibitory, 23 unknown) against the 995 putative pyramidal cells and 126 interneurons analysed.\n    Which sessions and units were left out, and why, is not stated.\n- kind: format_error\n  statement: In sub-Dino_ses-Dino-072114 the spike times are whole seconds divided by 20000 (8451\n    distinct values from 0 to 0.4252 s, in a recording of 7959 s). The conversion read this session's\n    spikes from a CellExplorer file with a hard-coded 20 kHz rate. The session's spikes cannot be used.\n- kind: format_error\n  statement: In sub-Dino_ses-Dino-061914 the LFP has 125 columns for 128 electrodes, lasts 331.7 min\n    against 291.9 min of states and spikes, and its samples are scrambled (lag-1 autocorrelation\n    0.28 on the reference channel, against 0.99 or more in every other session), consistent with a\n    128-channel file read as 125 channels.\n- kind: data_missing\n  statement: The state table holds only Awake, Non-REM and REM. The paper scores microarousals as a\n    state of their own and builds WAKE-SLEEP episodes, nonREM packets and episodes, UP/DOWN states\n    and spindles, none of which is in the dandiset. MAs derived from short Awake epochs are fewer\n    than the paper reports (391 in 21 sessions, against 790 in 27).\n- kind: selection_undocumented\n  statement: The dandiset does not say how the state table was scored. The conversion code takes it\n    from each session's SleepState.states.mat; it yields 30 WAKE-SLEEP cycles in 21 sessions (3\n    sessions with none, though the paper kept only sessions with a full cycle), and only 49 of 534\n    REM epochs are followed directly by Non-REM, so it may not be the scoring the paper used.\n- kind: metadata_error\n  statement: The dandiset description gives 11 animals, 27 sessions and 1360 units, the paper's\n    numbers, while the files hold 10 animals, 22 sessions and 945 units (the archive's summary\n    counts 10 subjects). The description gives an age of 4-7 months, the files 3-7 months.\n- kind: format_error\n  statement: The LFP is stored as int16 with unit volts and conversion NaN, so it cannot be converted\n    to volts.\n- kind: metadata_insufficient\n  statement: Every electrode's location is \"unknown\" and every unit's region is \"CTX\" or \"unknown\",\n    although the paper records from medial prefrontal, orbitofrontal, anterior cingulate and\n    secondary motor cortex; only the electrode groups carry a region.\n- kind: metadata_insufficient\n  statement: 23 units of sub-BWRat21_ses-BWRat21-121613 have cell type and region \"unknown\", with no\n    description of what the label means.\n- kind: data_missing\n  statement: No movement, accelerometer or EMG data are in the dandiset, though the paper uses EMG to\n    score states and movement to define WAKE and to relate WAKE to rate changes.\n- kind: other\n  statement: The state labels are consistent with the spikes in 20 of 21 sessions (not established\n    for BWRat21-121813), but in 14 sessions the best agreement is with the table shifted 5 to 60 s\n    earlier, so state boundaries may lag the activity. The LFP agrees with the spikes to within 50 ms\n    in 14 of 21 sessions and within 128 ms in all.\n"
}
```

```
File created successfully at: attempts/000041-watson-2016-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  && python3 - <<'EOF'
p='attempts/000041-watson-2016-01.yaml'
s=open(p).read()
s=s.replace("  depends_on_note: null\n","")
s=s.replace("The LFP agrees with the spikes to within 50 ms\n    in 14 of 21 sessions and within 128 ms in all.","The LFP agrees with the spikes to within 50 ms\n    in 14 of 21 sessions, and to within 88 ms in all but Dino-061914, whose LFP is scrambled.")
open(p,'w').write(s)
import yaml
d=yaml.safe_load(open(p))
def walk(x,path=''):
    if isinstance(x,dict):
        for k,v in x.items(): walk(v,path+'/'+str(k))
    elif isinstance(x,list):
        for i,v in enumerate(x): walk(v,path+f'[{i}]')
    elif isinstance(x,str) and ': ' in x: print('COLON',path)
walk(d); print(len(d['outcomes']))
import collections; print(collections.Counter(o['outcome'] for o in d['outcomes']))
EOF
python tools/entry.py check entries/000041-watson-2016
```

```
39
Counter({'not_reproduced': 15, 'partially_reproduced': 9, 'reproduced': 8, 'blocked': 7})
0 error(s)
```

**Agent**

Check passes with 39 outcomes. Now the handover (step 6).

**Agent calls Bash**

```bash
python tools/entry.py handover entries/000041-watson-2016 && ls -R executed/000041-watson-2016/handover | head; python3 -c "
import nbformat
nb=nbformat.read('executed/000041-watson-2016/handover/reproduce_watson_2016.ipynb',4)
print(sum(1 for c in nb.cells if c.cell_type=='markdown' and c.source.startswith('**Result')), 'result cells left;', any('## Summary' in c.source for c in nb.cells), 'summary present')"; git status --short
```

```
wrote executed/000041-watson-2016/handover
executed/000041-watson-2016/handover:
10.1016-j.neuron.2016.03.036.yaml
reproduce_watson_2016.ipynb
sleepstates.py
0 result cells left; False summary present
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
?? attempts/000041-watson-2016-01.yaml
?? claims/000041/
?? entries/000041-watson-2016/
?? scripts
```

**Agent**

Handover built (no result cells, no summary). Some untracked dotfiles appeared at the repository root that I did not create; checking what they are before reporting.

**Agent calls Bash**

```bash
ls -la .bash_profile .bashrc .gitconfig .mcp.json .profile .ripgreprc .zprofile .zshrc .idea .vscode scripts 2>&1 | head -30; git log --oneline -1 -- scripts
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 16 02:07 .bash_profile
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 16 02:07 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 16 02:07 .gitconfig
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 16 02:07 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 16 02:07 .mcp.json
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 16 02:07 .profile
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 16 02:07 .ripgreprc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 16 02:07 .vscode
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 16 02:07 .zprofile
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 16 02:07 .zshrc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 16 02:07 scripts
```

**Agent**

I've done steps 1 to 6. The entry is locked, passes `check` with 0 errors, runs from a clean environment in 233 s, and the verifier's package is in `executed/000041-watson-2016/handover/`. Of 39 claims, 8 are reproduced, 9 partially reproduced, 15 not reproduced and 7 blocked. Nothing is committed.

**Text and version used.** I used the full text of the NIH author manuscript (PMC4873379), which is free to read but not under an open licence. The supplement could not be downloaded: PMC and Cell answer with a browser check. Table 1 is not in the manuscript. The pinned version is 0.250624.0419. The paper cites no dandiset version, and the two published versions hold the same 22 files; they differ only in metadata, so I pinned the most recent and said so in the notebook header.

### (1) Outcomes per claim

| Claim | Outcome |
|---|---|
| dataset-composition | not reproduced |
| fig2a-median-rates | partially (all three pE medians match; the pI medians are low) |
| fig2a-skewed-wide-distribution | partially |
| fig2a-fraction-above-2hz | not reproduced (direction right, p = 3.5e-06, short of the paper's p < 1e-10) |
| fig2b-wake-nrem-slope | reproduced |
| fig2-burst-index-by-state | partially |
| fig2c-acg-peaks | partially (the 8 ms peak is there; no theta peak found) |
| fig2c-acg-decay | blocked, methods underspecified |
| fig2f-rate-group-correlations | partially |
| ma-statistics | not reproduced |
| ma-fraction-over-nrem-episodes | partially |
| packet-duration | reproduced (median 108 s) |
| wake-sleep-cycles | not reproduced |
| fig3b-population-decline | partially |
| fig3-first-last-packet | reproduced (last-packet mean 0.9679 against a bound of 0.968) |
| fig3d-first-last-slope | reproduced, but a split-half check gives the same slope, so regression to the mean can explain it |
| fig3e-wake-before-after | partially |
| fig3b-sextiles-over-sleep | reproduced |
| fig3b-cv-over-sleep | not reproduced |
| fig4iv-sextiles-within-nrem | reproduced (small effects, varying by subject) |
| fig4v-cv-within-nrem, fig4vi-burst-within-nrem | not reproduced |
| fig4i-band-power-within-nrem | not reproduced |
| fig4-delta-packet-length | reproduced |
| fig4cd-packet-rate-lfp | partially |
| fig5b, all four triplet claims | not reproduced |
| fig5c-rem-duration, fig5c-sigma-ma | not reproduced |
| fig5c-delta-change | reproduced |
| figs5-within-wake-rem | not reproduced |
| fig5c-wake-movement | blocked, data missing |
| UP/DOWN-state and spindle claims (5) | blocked, methods underspecified |

### (2) What was found about the dandiset
- **Missing data:** it holds 22 sessions from 10 rats and 945 units. The paper, and the dandiset's own description, report 27 sessions, 11 rats, 995 putative pyramidal cells and 126 interneurons.
- **Dino-072114:** the spike times are whole seconds divided by 20000. The conversion code set a 20 kHz rate on this one session. Its spikes are unusable, so I excluded the session.
- **Dino-061914:** the LFP is scrambled. It has 125 columns for 128 electrodes and runs 40 min longer than the spikes, and its sample-to-sample correlation is 0.28 against 0.99 elsewhere. I kept the session's spikes and dropped its LFP.
- **No microarousal label:** the state table has only Awake, Non-REM and REM. I derived microarousals from short Awake epochs between Non-REM epochs. They come out at about half the paper's count (391 in 21 sessions against 790 in 27).
- **The state scoring may not be the paper's:**
  - It gives 30 wake-then-sleep cycles in 21 sessions, and 3 sessions have none, although the paper kept only sessions that had one.
  - Only 49 of 534 REM epochs are followed directly by Non-REM, so the REM triplet claims rest on 17 triplets.
  - The dandiset does not say how the states were scored.
- **Metadata problems:**
  - The LFP has unit "volts" but a NaN conversion factor, so it cannot be put in volts.
  - Every electrode location is "unknown".
  - 23 units have cell type "unknown" with no description.
  - The description's counts and age range do not match the files.
- **Clocks:** the state labels agree with the spikes in 20 of 21 sessions, and the LFP agrees to within 50 ms in 14 of 21.

### (3) Where the protocol was unclear, wrong or missing something
1. "Open access" is not defined. I treated a free-to-read author manuscript as full text.
2. There is no rule for when the main text is available but the supplement is not. I blocked the claims whose methods are only in the supplement as `methods_underspecified`, although that reason is defined as "neither the paper nor its code fixes the procedure".
3. Neither the paper nor the dandiset links any code. The protocol does not say whether to search for some. I read the NWB conversion code (catalystneuro/buzsaki-lab-to-nwb at 5f6a375) and recorded the commit; it explained both corrupt files.
4. The prescribed clock check (decoding labels shifted in time) is coarse when states last minutes, and it does not apply to LFP, which has no labels. I used a contrast against shifts of ±5 to ±300 s for the labels and a spike-LFP cross-correlation for the LFP, and set my own pass thresholds.
5. There is no guidance on a label the paper uses but the dandiset lacks. I derived microarousals and recorded this as both a deviation and a finding.
6. Session-level corruption inside an otherwise usable dandiset is not covered. I excluded the affected data and recorded findings.
7. The 10% default tolerance is not meaningful for correlation coefficients that depend on binning the paper does not give, so I judged those on sign and significance and stated why. Separately, fixed p-value thresholds become stricter with fewer cells, which made fig2a-fraction-above-2hz "not reproduced" although the effect is there.
8. The `measured` rule covers only the case where some reading matches. When none did, I recorded the first reading listed.
9. A check can show a criterion is not diagnostic (the fig3d slope), but the protocol gives no way to act on that. I kept the outcome the criterion gives and said so in the notes.
10. I found the scrambled Dino-061914 LFP after the criteria were written and after seeing some LFP results. The protocol does not say how to handle that. I recorded the exclusion as a deviation on each claim that uses LFP.

### (4) Runtime and failures
- The notebook takes 233 s in a clean environment; about two minutes of that is streaming the files in 6 parallel processes.
- The final run had no failures.
- Earlier failures:
  - Europe PMC's full-text endpoint returned a server error.
  - PMC and Cell blocked the HTML and supplement downloads with a browser check.
  - GitHub code search needs authentication, so I found the conversion code through the repository tree instead.
- The sandbox mounted about 10 dotfiles and `scripts` at the repository root as `/dev/null` devices, so they show as untracked. They are not real files and git will not add them.

## End of run

66 turns, 55 minutes, result: success.
