# 000067 · author · run 38917959176

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls; ls entries claims attempts | tail -20
```

```
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
kept in [`transcripts/<dandiset>/`](../transcripts).

## Author

[... 378 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md docs/design.md | head -300; ls entries/001453-fouke-2025 claims/001453; cat attempts/001453-fouke-2025-01.yaml
```

```
<persisted-output>
Output too large (51.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/c499576e-dbd4-49be-9a39-3fcbda08dcd8/tool-results/bd20m5918.txt

Preview (first 2KB):
# Reproduction registry (working name)

Agents, and people, try to reproduce the key findings of papers from the open
data on the [DANDI Archive](https://dandiarchive.org), and register the result
here: the notebooks when it works, and the reason when it does not.

- **For the archive:** evidence of whether each dandiset is complete and
  accurate enough to support the findings of its paper.
- **For analysts:** working notebooks to build new analyses on.

Status: pilot. All eight pilot targets have been attempted and checked by an
independent agent.

**Dashboard:** <https://catalystneuro.github.io/reproduction-registry/>

## Reading the outcomes
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001453-fouke-2025; cat entry.yaml requirements.in README.md 2>/dev/null; ls; cat ../../claims/001453/*.yaml
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
[... 258 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,400p docs/design.md | head -250
```

```
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
   reproduced, with the reason, tells the data owner and the archive what is
   missing.
2. **Give analysts a starting point.** Someone who wants to test a new
   hypothesis on a dandiset starts from notebooks that already load the data
[... 229 more lines not kept]
```

**Agent**

Now the example notebook and helper format, and the tools.

**Agent calls Bash**

```bash
cd  python -c "
import json;nb=json.load(open('entries/001453-fouke-2025/reproduce_fouke_2025.ipynb'))
for c in nb['cells'][:12]:
  print('----',c['cell_type'],c.get('metadata'));print(''.join(c['source'])[:2500])
print(len(nb['cells']))
"; ls tools; python tools/entry.py --help
```

```
---- markdown {}
# Reproducing Fouke et al. (2025) from dandiset 001453

**Paper.** Fouke KE, He Z, Loring MD, Naumann EA (2025). Neural circuits underlying divergent
visuomotor strategies of zebrafish and *Danionella cerebrum*. *Current Biology*.
[doi:10.1016/j.cub.2025.04.027](https://doi.org/10.1016/j.cub.2025.04.027). This attempt used the
full text of the accepted author manuscript in PubMed Central (PMC12218792); the version of record
is not open access.

**Dandiset.** [DANDI:001453](https://dandiarchive.org/dandiset/001453/0.250518.1950), version
0.250518.1950. The paper cites no DANDI version (its data statement points to a GitLab repository
that holds code only). This is the only published version. The draft holds the same 37 files
(same blobs and sizes); it differs only in metadata added later (authors, keywords, and a
`relatedResource` link to the paper), none of which the analysis uses.

**What the dandiset holds.** Freely swimming tracking of 25 zebrafish (ZF) and 12 *D. cerebrum*
(DC) larvae during the optomotor protocol of Figure 1 and Figure S1. The two-photon imaging and the
head-fixed tail tracking of Figures 2 to 4 are not in it.

**Outside inputs.** The stimulus codes in the files have no names. The names come from the paper's
[... 271 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;nb=json.load(open('entries/001453-fouke-2025/reproduce_fouke_2025.ipynb'))
for c in nb['cells'][12:]:
  print('----',c['cell_type'],c.get('metadata'));print(''.join(c['source'])[:1200])
" | tail -150; sed -n 1,80p entries/001453-fouke-2025/omr.py
```

```
fz = sub[sub.species == "ZF"].groupby("fish").accel.median()
        fd = sub[sub.species == "DC"].groupby("fish").accel.median()
        rows.append({"name": omr.STIMULUS_NAMES[c], "ZF_median": z.median(), "DC_median": d.median(),
                     "n_ZF": len(z), "n_DC": len(d), "kruskal_p": stats.kruskal(z, d).pvalue,
                     "ZF_fish_median": fz.median(), "DC_fish_median": fd.median(),
                     "fish_mannwhitney_p": stats.mannwhitneyu(fz, fd).pvalue})
    out = pd.DataFrame(rows)
    out["zf_higher_and_sig"] = (out.ZF_median > out.DC_median) 
---- code {'tags': ['claim:fig1h-zf-higher-angular-acceleration']}
coded = accel_tests("code")
print("Variant: Fig1-S1.ipynb's quantity (per-frame heading change / file mean frame interval):")
print(coded.to_string(index=False, float_format=lambda v: f"{v:.3g}"))
print(f"\nStimuli with ZF higher and p < 0.05/9: {int(coded.zf_higher_and_sig.sum())} of 9")
ratio = pd.DataFrame([{"fish": omr.fish_key(s), "frame_interval_median_ms": 1000 / s["frame_hz"], "code_dt_ms": 1000 * s["code_dt"]} for s in sessions])
ratio["code_dt_over_frame_interval"] = ratio.code_dt_ms / ratio.frame_interval_median_ms
fast_fish = {f for f, v in hz.items() if v > 100}
sub = accel[(accel.kind == "methods") & accel.fish.isin(fast_fish)]
fm = sub.groupby(["species", "fish"]).accel.median()
print("\nMethods definition, files at 128-171 Hz only: per-fish median over all whole-field frames (deg/s^2):",
      f"ZF {fm.loc['ZF'].median():.1f} (n {len(fm.loc['ZF'])}), DC {fm.loc['DC'].median():.1f} (n {len(fm.loc['DC'])}),",
[... 210 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls schemas; head -c 9000 attempts/001453-fouke-2025-01.yaml; echo; grep -n "verifications" -A30 attempts/001453-fouke-2025-01.yaml | head -50; tail -30 attempts/001453-fouke-2025-01.yaml
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
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
[... 194 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat schemas/attempt.schema.json | head -250; grep -n "blocked" -B2 -A8 attempts/001453-fouke-2025-01.yaml | sed -n 1,40p; grep -n "^findings" -A25 attempts/001453-fouke-2025-01.yaml
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
    "dandiset",
    "paper",
    "date",
    "provenance",
    "outcomes"
  ],
  "properties": {
    "schema_version": {
      "const": 1
    },
    "id": {
[... 296 more lines not kept]
```

**Agent calls Bash**

```bash
cd  curl -s https://api.dandiarchive.org/api/dandisets/000067/ | python -m json.tool; curl -s https://api.dandiarchive.org/api/dandisets/000067/versions/ | python -m json.tool
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  for v in 0.250624.0419 0.210812.1457; do echo "=== $v"; curl -s "https://api.dandiarchive.org/api/dandisets/000067/versions/$v/" > $TMPDIR/meta_$v.json; curl -s "https://api.dandiarchive.org/api/dandisets/000067/versions/$v/assets/?page_size=100" | python -c "
import json,sys; d=json.load(sys.stdin)
for a in d['results']: print(a['asset_id'], a['blob'] if 'blob' in a else '', a['size'], a['path'])"; done; python -m json.tool $TMPDIR/meta_0.250624.0419.json | head -200
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; python -m json.tool meta_0.250624.0419.json | sed -n 200,400p; python - <<'E'
import json
a=json.load(open('meta_0.250624.0419.json'));b=json.load(open('meta_0.210812.1457.json'))
for k in sorted(set(a)|set(b)):
    if a.get(k)!=b.get(k): print('DIFF',k, json.dumps(b.get(k))[:600])
E
```

```
],
        "numberOfBytes": 94565736755,
        "numberOfFiles": 28,
        "numberOfSubjects": 3,
        "variableMeasured": [
            "LFP",
            "ProcessingModule",
            "Units",
            "ElectricalSeries"
        ],
        "measurementTechnique": [
            {
                "name": "signal filtering technique",
                "schemaKey": "MeasurementTechniqueType"
            },
            {
                "name": "analytical technique",
                "schemaKey": "MeasurementTechniqueType"
            },
            {
[... 45 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1038/nn.2134&format=json&resultType=core" | python -c "
import json,sys;d=json.load(sys.stdin)
for r in d['resultList']['result']: print(r.get('pmid'),r.get('pmcid'),r.get('isOpenAccess'),r.get('inPMC'),r.get('hasPDF'),r.get('title'));print(r.get('fullTextUrlList'))"
```

Result: the fetched text is not kept.

**Agent**

The author manuscript is free in PMC (PMC2562676). Fetching its full text.

**Agent calls Bash**

```bash
mkdir -p paper; curl -sL "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2562676/fullTextXML" -o paper/PMC2562676.xml; ls -la paper; head -c 600 paper/PMC2562676.xml
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -sL "https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id=PMC2562676" | head -c 500; echo; curl -sL -A "Mozilla/5.0" "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=2562676&rettype=xml" -o paper/PMC2562676.xml; ls -la paper; head -c 1000 paper/PMC2562676.xml
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; curl -sL -A "Mozilla/5.0" "https://europepmc.org/articles/PMC2562676?pdf=render" -o PMC2562676.pdf; file PMC2562676.pdf; ls -la; curl -sL -A "Mozilla/5.0 (X11; Linux x86_64)" "https://pmc.ncbi.nlm.nih.gov/articles/PMC2562676/" -o PMC2562676.html; ls -la; grep -c "<p" PMC2562676.html
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; rm PMC2562676.pdf; python - <<'E'
import re,html
s=open('PMC2562676.html').read()
m=re.search(r'<section[^>]*class="body main-article-body"[^>]*>(.*)',s,re.S)
body=m.group(1) if m else s
body=re.sub(r'<(script|style)[^>]*>.*?</\1>','',body,flags=re.S)
body=re.sub(r'</(p|h[1-6]|li|figcaption|tr|div)>','\n',body)
body=re.sub(r'<[^>]+>','',body)
t=html.unescape(body)
t=re.sub(r'\n\s*\n+','\n\n',t)
open('fujisawa2008.txt','w').write(t)
print(len(t))
E
wc -w fujisawa2008.txt
```

```
66718
9477 fujisawa2008.txt
```

**Agent calls Read**

```json
{
 "file_path": "paper/fujisawa2008.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -o 'href="[^"]*supplement[^"]*"' paper/PMC2562676.html | head;
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  curl -sL -A "Mozilla/5.0 (X11; Linux x86_64)" "https://pmc.ncbi.nlm.nih.gov/articles/instance/2562676/bin/NIHMS52220-supplement-Suppl.pdf" -o paper/suppl.pdf; file paper/suppl.pdf; which pdftotext; python -c "import pypdf" 2>&1
```

Result: the fetched text is not kept.

**Agent**

Supplement PDF is behind a bot check; I'll proceed with the main text. Now setting up a scratch environment to inspect the NWB files.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q scratch && . scratch/bin/activate && uv pip install -q dandi pynwb remfile h5py numpy pandas scipy 2>&1 | tail -3; python -c "import pynwb,dandi;print(pynwb.__version__, dandi.__version__)"
```

```
4.2.0 0.81.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
. $TMPDIR/scratch/bin/activate; cat > $TMPDIR/inspect.py <<'E'
import sys, h5py, remfile
from dandi.dandiapi import DandiAPIClient
path=sys.argv[1]
with DandiAPIClient() as c:
    a=c.get_dandiset("000067","0.250624.0419").get_asset_by_path(path)
    url=a.get_content_url(follow_redirects=1, strip_query=True)
f=h5py.File(remfile.File(url),'r')
def show(name,obj):
    if isinstance(obj,h5py.Dataset):
        s=f"DS {name} {obj.shape} {obj.dtype}"
        if obj.size<=3 and obj.dtype.kind in 'OSU': s+=f" = {obj[()]!r}"[:300]
        print(s, dict((k,(v if not hasattr(v,'shape') or v.size<5 else v.shape)) for k,v in obj.attrs.items() if k not in ('object_id',)))
    else:
        print(f"GR {name}", dict((k,v) for k,v in obj.attrs.items() if k not in ('object_id',)))
f.visititems(show)
E
python $TMPDIR/inspect.py sub-EE/sub-EE_ses-EE-088_behavior+ecephys.nwb 2>&1 | head -300
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/inspect.py", line 1, in <module>
    import sys, h5py, remfile
  File "/tmp/claude-1001/scratch/lib/python3.13/site-packages/h5py/__init__.py", line 33, in <module>
    from . import version
  File "/tmp/claude-1001/scratch/lib/python3.13/site-packages/h5py/version.py", line 17, in <module>
    import numpy
  File "/tmp/claude-1001/scratch/lib/python3.13/site-packages/numpy/__init__.py", line 109, in <module>
    from numpy.__config__ import show_config
  File "/tmp/claude-1001/scratch/lib/python3.13/site-packages/numpy/__config__.py", line 4, in <module>
    from numpy._core._multiarray_umath import (
    ...<3 lines>...
    )
  File "/tmp/claude-1001/scratch/lib/python3.13/site-packages/numpy/_core/__init__.py", line 24, in <module>
    from . import multiarray
  File "/tmp/claude-1001/scratch/lib/python3.13/site-packages/numpy/_core/multiarray.py", line 11, in <module>
    from . import _multiarray_umath, overrides
  File "/tmp/claude-1001/scratch/lib/python3.13/site-packages/numpy/_core/overrides.py", line 4, in <module>
    import inspect
  File "/tmp/claude-1001/inspect.py", line 1, in <module>
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/scratch/bin/activate; mv $TMPDIR/inspect.py $TMPDIR/lsnwb.py; python $TMPDIR/lsnwb.py sub-EE/sub-EE_ses-EE-088_behavior+ecephys.nwb 2>&1 | head -300
```

```
GR acquisition {}
GR analysis {}
DS file_create_date (1,) object = array([b'2021-04-18T19:31:52.908609-04:00'], dtype=object) {}
GR general {}
GR general/devices {}
GR general/devices/Device {'description': 'Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).', 'namespace': 'core', 'neurodata_type': 'Device'}
DS general/experimenter (1,) object = array([b'Shigeyoshi Fujisawa'], dtype=object) {}
GR general/extracellular_ephys {}
GR general/extracellular_ephys/electrodes {'colnames': array(['x', 'y', 'z', 'imp', 'location', 'filtering', 'group',
       'group_name', 'shank_electrode_number'], dtype=object), 'description': 'metadata about extracellular electrodes', 'namespace': 'hdmf-common', 'neurodata_type': 'DynamicTable'}
DS general/extracellular_ephys/electrodes/filtering (104,) object {'description': 'description of hardware filtering', 'namespace': 'hdmf-common', 'neurodata_type': 'VectorData'}
DS general/extracellular_ephys/electrodes/group (104,) object {'description': 'a reference to the ElectrodeGroup this electrode is a part of', 'namespace': 'hdmf-common', 'neurodata_type': 'VectorData'}
DS general/extracellular_ephys/electrodes/group_name (104,) object {'description': 'the name of the ElectrodeGroup this electrode is a part of', 'namespace': 'hdmf-common', 'neurodata_type': 'VectorData'}
DS general/extracellular_ephys/electrodes/id (104,) int64 {'namespace': 'hdmf-common', 'neurodata_type': 'ElementIdentifiers'}
DS general/extracellular_ephys/electrodes/imp (104,) float64 {'description': 'the impedance of the channel', 'namespace': 'hdm
[... 96 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/scratch/bin/activate; for p in sub-EE/sub-EE_ses-EE-044_ecephys.nwb sub-GG/sub-GG_ses-GG-097_behavior+ecephys.nwb; do echo "=== $p"; python $TMPDIR/lsnwb.py $p 2>&1 | grep -v specifications | grep -v "shank[0-9]* {" ; done
```

```
=== sub-EE/sub-EE_ses-EE-044_ecephys.nwb
GR acquisition {}
GR acquisition/ElectricalSeries {'comments': 'Generated from SpikeInterface::NwbRecordingExtractor', 'description': 'Raw acquisition traces.', 'namespace': 'core', 'neurodata_type': 'ElectricalSeries'}
DS acquisition/ElectricalSeries/data (26000, 104) int16 {'conversion': np.float64(1e-06), 'resolution': np.float64(-1.0), 'unit': 'volts'}
DS acquisition/ElectricalSeries/electrodes (104,) int64 {'description': 'electrode_table_region', 'namespace': 'hdmf-common', 'neurodata_type': 'DynamicTableRegion', 'table': <HDF5 object reference>}
DS acquisition/ElectricalSeries/starting_time () float64 {'rate': np.float64(20000.0), 'unit': 'seconds'}
GR analysis {}
DS file_create_date (1,) object = array([b'2021-04-18T19:52:33.188070-04:00'], dtype=object) {}
GR general {}
GR general/devices {}
GR general/devices/Device {'description': 'Rats were implanted with silicon probes in the prefrontal cortex, layer 2/3 or layer 5 (anteroposterior = 3.0–4.4 mm, medio-lateral = 0.5 mm). The recording silicon probe was attached to a micromanipulator and moved gradually to its desired depth position. The probe consisted of eight shanks (200-μm shank separation) and each shank had eight recording sites (160 μm2 each site; 1–3 MΩ impedance), staggered to provide a two-dimensional arrangement (20-μm vertical separation).', 'namespace': 'core', 'neurodata_type': 'Device'}
DS general/experimenter (1,) object = array([b'Shigeyoshi Fujisawa'], dtype=object) {}
GR general/extracellular_ephys {}
GR general/extracellular_ephys/electrodes {'colnames': array(['x', 'y', 'z', 'imp', 'location', 'filtering', 'group',
       'group_name', 'shank_electrode_number'], dtype=object), 'description': 'metadata about extracellular electrodes', 'namespace': 'hdmf-common', 'neurodata_type': 'DynamicTable'}
DS general/extracellular_ephys/electrodes/filtering (104,) object {'description': 'description of hardware filtering', 'namespace': 'hdmf-common', 'neur
[... 109 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/scratch/bin/activate; cat > $TMPDIR/survey.py <<'E'
import h5py, remfile, numpy as np, json
from concurrent.futures import ThreadPoolExecutor
from dandi.dandiapi import DandiAPIClient
with DandiAPIClient() as c:
    assets=[(a.path,a.get_content_url(follow_redirects=1, strip_query=True)) for a in c.get_dandiset("000067","0.250624.0419").get_assets()]
def dec(x): return x.decode() if isinstance(x,bytes) else x
def one(pu):
    p,u=pu
    f=h5py.File(remfile.File(u),'r')
    r={'path':p}
    r['session']=dec(f['general/session_id'][()]); r['start']=dec(f['session_start_time'][()])
    e=f['general/extracellular_ephys/electrodes']
    r['n_el']=len(e['id']); r['loc']=sorted(set(dec(v) for v in e['location'][:])); r['groups']=len(set(dec(v) for v in e['group_name'][:]))
    r['filtering']=sorted(set(dec(v) for v in e['filtering'][:]))
    r['xyz']=[float(np.nanmin(e[k][:])) for k in 'xyz']+[float(np.nanmax(e[k][:])) for k in 'xyz']
    r['imp']=sorted(set(np.round(e['imp'][:],3).tolist()))[:5]
    if 'acquisition/ElectricalSeries' in f:
        d=f['acquisition/ElectricalSeries/data']; r['raw_s']=d.shape[0]/20000
    lf=f['processing/ecephys/LFP/LFP/data']; r['lfp_s']=lf.shape[0]/1250
    if 'units' in f:
        st=f['units/spike_times'][:]; idx=f['units/spike_times_index'][:]
        r['n_units']=len(idx); r['n_spikes']=len(st)
        r['spk_range']=[float(st.min()),float(st.max())]
        b=np.concatenate([[0],idx]); 
        uns=[np.all(np.diff(st[b[i]:b[i+1]])>=0) for i in range(len(idx))]
        r['unsorted_units']=int(len(idx)-sum(uns))
        n=np.diff(b); r['spikes_per_unit_min_med_max']=[int(n.min()),float(np.median(n)),int(n.max())]
        r['unit_ids_head']=f['units/id'][:5].tolist()
    if 'intervals/trials' in f:
        t=f['intervals/trials']
        r['n_trials']=len(t['id']); lr=[dec(v) for v in t['left_or_right'][:]]
        r['lr']={k:lr.count(k) for k in set(lr)}
        r['trial_span']=[float(t['start_time'][0]),float(t['stop_time'][-1])]
        r['trial_dur_med']=float(np.median(t['stop_time'][:]-t['start_time'][:]))
        r['reward_in_trial']=float(np.mean((t['reward_time'][:]>=t['start_time'][:])&(t['reward_time'][:]<=t['stop_time'][:])))
    if 'processing/behavior' in f:
        lp=f['processing/behavior/LinearizedPosition/LinearizedTimeSeries/data'][:]
        r['lin_n']=len(lp); r['lin_range']=[float(np.nanmin(lp)),float(np.nanmax(lp))]; r['lin_nan']=float(np.isnan(lp).mean()); r['lin_zero']=float((lp==0).mean())
        for k in ('SpatialSeries1','SpatialSeries2'):
            x=f[f'processing/behavior/Position/{k}/data'][:,0]
            r[k]=[float(np.nanmin(x)),float(np.nanmax(x)),float(np.isnan(x).mean()), float((x==-1).mean())]
    return r
with ThreadPoolExecutor(8) as ex: res=list(ex.map(one,sorted(assets)))
json.dump(res,open('/tmp/claude-1001/survey.json','w'),indent=0)
for r in res: print(json.dumps(r))
E
time python $TMPDIR/survey.py
```

```
/tmp/claude-1001/survey.py:15: RuntimeWarning: All-NaN slice encountered
  r['xyz']=[float(np.nanmin(e[k][:])) for k in 'xyz']+[float(np.nanmax(e[k][:])) for k in 'xyz']
{"path": "sub-EE/sub-EE_ses-EE-042_ecephys.nwb", "session": "EE.042", "start": "2008-06-22T00:00:00-04:00", "n_el": 104, "loc": ["unknown"], "groups": 13, "filtering": ["none"], "xyz": [NaN, NaN, NaN, NaN, NaN, NaN], "imp": [-1.0], "lfp_s": 993.0}
{"path": "sub-EE/sub-EE_ses-EE-043_ecephys.nwb", "session": "EE.043", "start": "2008-06-22T00:00:00-04:00", "n_el": 104, "loc": ["unknown"], "groups": 13, "filtering": ["none"], "xyz": [NaN, NaN, NaN, NaN, NaN, NaN], "imp": [-1.0], "raw_s": 1.6384, "lfp_s": 1.6384}
{"path": "sub-EE/sub-EE_ses-EE-044_ecephys.nwb", "session": "EE.044", "start": "2008-06-22T00:00:00-04:00", "n_el": 104, "loc": ["unknown"], "groups": 13, "filtering": ["none"], "xyz": [NaN, NaN, NaN, NaN, NaN, NaN], "imp": [-1.0], "raw_s": 1.3, "lfp_s": 1.3}
{"path": "sub-EE/sub-EE_ses-EE-045_ecephys.nwb", "session": "EE.045", "start": "2008-06-22T00:00:00-04:00", "n_el": 104, "loc": ["unknown"], "groups": 13, "filtering": ["none"], "xyz": [NaN, NaN, NaN, NaN, NaN, NaN], "imp": [-1.0], "raw_s": 2340.4544, "lfp_s": 2340.4544}
{"path": "sub-EE/sub-EE_ses-EE-046_ecephys.nwb", "session": "EE.046", "start": "2008-06-22T00:00:00-04:00", "n_el": 104, "loc": ["unknown"], "groups": 13, "filtering": ["none"], "xyz": [NaN, NaN, NaN, NaN, NaN, NaN], "imp": [-1.0], "raw_s": 140.0832, "lfp_s": 140.0832}
{"path": "sub-EE/sub-EE_ses-EE-047_ecephys.nwb", "session": "EE.047", "start": "2008-06-22T00:00:00-04:00", "n_el": 104, "loc": ["unknown"], "groups": 13, "filtering": ["none"], "xyz": [NaN, NaN, NaN, NaN, NaN, NaN], "imp": [-1.0], "raw_s": 1210.368, "lfp_s": 1210.368}
{"path": "sub-EE/sub-EE_ses-EE-048_ecephys.nwb", "session": "EE.048", "start": "2008-06-22T00:00:00-04:00", "n_el": 104, "loc": ["unknown"], "groups": 13, "filtering": ["none"], "xyz": [NaN, NaN, NaN, NaN, NaN, NaN], "imp": [-1.0], "raw_s": 103
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
curl -sL -m 30 "https://crcns.org/data-sets/pfc/pfc-2" | python -c "
import sys,re,html;s=sys.stdin.read();s=re.sub(r'<(script|style)[^>]*>.*?</\1>','',s,flags=re.S);t=html.unescape(re.sub(r'<[^>]+>',' ',s));print(re.sub(r'\s+',' ',t)[:6000])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -sL -m 30 "https://crcns.org/data-sets/pfc/pfc-2/about-pfc-2" | python -c "
import sys,re,html;s=sys.stdin.read();s=re.sub(r'<(script|style)[^>]*>.*?</\1>','',s,flags=re.S);t=html.unescape(re.sub(r'<[^>]+>',' ',s));t=re.sub(r'\s+',' ',t);i=t.find('About pfc-2 Information');print(t[i:i+9000])" | tee paper/crcns_pfc2_about.txt
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; curl -sL -m 60 "https://crcns.org/data-sets/pfc/pfc-2/about-pfc-2" | grep -o 'href="[^"]*\.pdf[^"]*"' ; curl -sL -m 60 -o crcns_pfc2_desc.pdf "https://crcns.org/files/data/pfc-2/crcns_pfc-2_data_description.pdf"; file crcns_pfc2_desc.pdf; curl -sI -m 30 https://buzsakilab.nyumc.org/datasets/FujisawaS/ | head -5
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  . $TMPDIR/scratch/bin/activate; uv pip install -q pypdf; python -c "
import pypdf;r=pypdf.PdfReader('paper/crcns_pfc2_desc.pdf');t='\n'.join(p.extract_text() for p in r.pages);open('paper/crcns_pfc2_desc.txt','w').write(t);print(t)"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
. $TMPDIR/scratch/bin/activate; cat > $TMPDIR/look.py <<'E'
import h5py, remfile, numpy as np
from dandi.dandiapi import DandiAPIClient
p="sub-GG/sub-GG_ses-GG-097_behavior+ecephys.nwb"
with DandiAPIClient() as c:
    u=c.get_dandiset("000067","0.250624.0419").get_asset_by_path(p).get_content_url(follow_redirects=1, strip_query=True)
f=h5py.File(remfile.File(u),'r')
t=f['intervals/trials']
import pandas as pd
df=pd.DataFrame({k:t[k][:] for k in ['start_time','stop_time','reward_time']}); df['lr']=[x.decode() for x in t['left_or_right'][:]]
print(df.head(10)); print((df.reward_time-df.stop_time).describe()); print((df.start_time.shift(-1)-df.reward_time).describe())
lp=f['processing/behavior/LinearizedPosition/LinearizedTimeSeries/data'][:]
x=f['processing/behavior/Position/SpatialSeries1/data'][:,0]; y=f['processing/behavior/Position/SpatialSeries2/data'][:,0]
tt=np.arange(len(lp))/39.0625
print('lin unique count',len(np.unique(lp)), np.percentile(lp[lp>0],[0,1,50,99,100]))
for i in range(3):
    m=(tt>=df.start_time[i]-1)&(tt<=df.reward_time[i]+1)
    print(i, df.lr[i], np.round(lp[m][::8],2)); print(np.round(x[m][::8]))
# where lin >0 relative to trials
inn=np.zeros(len(lp),bool)
for a,b in zip(df.start_time,df.reward_time): inn|=(tt>=a)&(tt<=b)
print('frac lin>0 inside start..reward',(lp[inn]>0).mean(),'outside',(lp[~inn]>0).mean())
inn2=np.zeros(len(lp),bool)
for a,b in zip(df.stop_time,df.reward_time): inn2|=(tt>=a)&(tt<=b)
print('frac lin>0 inside stop..reward',(lp[inn2]>0).mean(), 'lin>0 frames covered by stop..reward', inn2[lp>0].mean())
d=f['acquisition/ElectricalSeries/data']; print(d.chunks, d.compression, d.shape)
print(f['units/spike_times'].chunks)
E
python $TMPDIR/look.py
```

```
start_time  stop_time  reward_time     lr
0     29.4496    56.2184      62.4776   Left
1    114.4712   120.3032     126.0168   Left
2    135.9048   197.7144     204.4808   Left
3    217.3584   223.2128     228.2120  Right
4    260.2576   269.3232     273.5240  Right
5    287.0584   291.2488     297.5880  Right
6    311.3208   324.1040     329.2552   Left
7    343.6416   361.6776     368.6024   Left
8    382.6128   395.6608     401.3704  Right
9    419.5888   442.5976     447.2200  Right
count    38.000000
mean      6.058400
std       0.987406
min       4.200800
25%       5.309850
50%       6.039600
75%       6.622650
max       8.433600
dtype: float64
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
curl -sL -m 30 https://buzsakilab.com/wp/datasets/ | grep -io '[^"]*fujisawa[^"]*\|[^"]*pfc-2[^"]*\|[^"]*pfc2[^"]*' | head; curl -sL -m 30 https://buzsakilab.nyumc.org/datasets/ | head -c 1500
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -sL -m 30 -o $TMPDIR/bl.html -w "%{http_code} %{url_effective}\n" https://buzsakilab.com/wp/datasets/; wc -c $TMPDIR/bl.html; grep -o 'href="[^"]*"' $TMPDIR/bl.html | grep -i "dataset\|nyumc\|share" | head -20; curl -sL -m 30 -o /dev/null -w "%{http_code} %{url_effective}\n" "https://buzsakilab.nyumc.org/datasets/FujisawaS/"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -skL -m 30 "https://buzsakilab.nyumc.org/datasets/FujisawaS/" | head -c 2000; echo; curl -skL -m 30 "https://buzsakilab.com/wp/datasets/" | grep -io 'fujisawa[^<]\{0,200\}' | head
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s -m 30 "https://api.github.com/search/code?q=fujisawa+repo:catalystneuro/buzsaki-lab-to-nwb" | head -c 300; echo; curl -s -m 30 "https://api.github.com/repos/catalystneuro/buzsaki-lab-to-nwb/contents/" | python -c "import json,sys;[print(x['path']) for x in json.load(sys.stdin)]"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s -m 30 "https://api.github.com/repos/catalystneuro/buzsaki-lab-to-nwb/contents/buzsaki_lab_to_nwb" | python -c "import json,sys;[print(x['path']) for x in json.load(sys.stdin)]"; curl -s -m 30 "https://api.github.com/repos/catalystneuro/buzsaki-lab-to-nwb/commits?per_page=1" | python -c "import json,sys;d=json.load(sys.stdin);print(d[0]['sha'],d[0]['commit']['committer']['date'])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
SHA=5f6a3750fffd999c4757d8a198cba6007f85fb12; mkdir -p paper/conv; for f in $(curl -s -m 30 "https://api.github.com/repos/catalystneuro/buzsaki-lab-to-nwb/contents/buzsaki_lab_to_nwb/fujisawa?ref=$SHA" | python -c "import json,sys;[print(x['path']) for x in json.load(sys.stdin)]"); do echo "== $f"; curl -s -m 30 "https://raw.githubusercontent.com/catalystneuro/buzsaki-lab-to-nwb/$SHA/$f" -o paper/conv/$(basename $f); done; ls -la paper/conv; curl -s "https://api.github.com/repos/catalystneuro/buzsaki-lab-to-nwb/commits?path=buzsaki_lab_to_nwb/fujisawa&per_page=5" | python -c "import json,sys;[print(c['sha'][:8],c['commit']['committer']['date'],c['commit']['message'][:60]) for c in json.load(sys.stdin)]"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cat paper/conv/convert_fujisawa.py paper/conv/fujisawamiscdatainterface.py paper/conv/fujisawanwbconverter.py
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
. $TMPDIR/scratch/bin/activate; cat > $TMPDIR/units.py <<'E'
import h5py, remfile, numpy as np, sys
from dandi.dandiapi import DandiAPIClient
with DandiAPIClient() as c:
    ds=c.get_dandiset("000067","0.250624.0419")
    for p in sys.argv[1:]:
        u=ds.get_asset_by_path(p).get_content_url(follow_redirects=1, strip_query=True)
        f=h5py.File(remfile.File(u),'r')
        st=f['units/spike_times'][:]; idx=f['units/spike_times_index'][:]; b=np.concatenate([[0],idx])
        dur=st.max()
        rates=np.diff(b)/dur
        uns=[i for i in range(len(idx)) if np.any(np.diff(st[b[i]:b[i+1]])<0)]
        print(p, 'units',len(idx),'unsorted',uns)
        print(' '.join(f"{i}:{r:.1f}" for i,r in enumerate(rates)))
        for i in uns:
            s=st[b[i]:b[i+1]]; d=np.diff(s); print('unit',i,'n',len(s),'neg diffs',(d<0).sum(), 'min diff',d.min(), 'first', s[:3], 'max',s.max(), 'dups', (d==0).sum())
E
python $TMPDIR/units.py sub-GG/sub-GG_ses-GG-097_behavior+ecephys.nwb sub-EE/sub-EE_ses-EE-049_behavior+ecephys.nwb sub-FF/sub-FF_ses-FF-103_behavior+ecephys.nwb
```

```
sub-GG/sub-GG_ses-GG-097_behavior+ecephys.nwb units 69 unsorted []
0:34.4 1:13.0 2:17.2 3:13.0 4:13.7 5:1.2 6:0.5 7:0.6 8:0.6 9:25.0 10:1.0 11:1.1 12:0.8 13:1.1 14:0.3 15:0.7 16:0.8 17:0.5 18:0.5 19:12.1 20:0.6 21:0.7 22:0.2 23:21.9 24:0.6 25:1.7 26:1.7 27:6.6 28:0.6 29:1.2 30:12.4 31:0.1 32:0.1 33:10.1 34:0.4 35:0.4 36:1.3 37:0.4 38:4.1 39:3.4 40:1.7 41:1.4 42:12.1 43:12.2 44:6.1 45:0.8 46:3.2 47:1.6 48:3.9 49:22.8 50:1.0 51:16.1 52:2.0 53:7.8 54:0.0 55:0.3 56:0.2 57:0.0 58:0.0 59:0.1 60:0.1 61:0.1 62:0.0 63:0.0 64:0.0 65:0.4 66:0.1 67:0.1 68:0.0
sub-EE/sub-EE_ses-EE-049_behavior+ecephys.nwb units 118 unsorted [1]
0:24.2 1:111.9 2:1.5 3:0.8 4:2.4 5:0.2 6:1.8 7:2.9 8:95.3 9:0.3 10:2.6 11:7.9 12:1.5 13:0.6 14:1.2 15:1.5 16:1.4 17:1.6 18:0.2 19:0.6 20:8.1 21:2.9 22:127.8 23:0.3 24:1.4 25:1.1 26:1.4 27:1.7 28:0.3 29:0.3 30:4.8 31:0.8 32:2.6 33:0.9 34:2.2 35:0.1 36:0.1 37:0.2 38:0.1 39:129.2 40:0.4 41:0.8 42:1.2 43:0.7 44:0.9 45:1.3 46:0.1 47:0.3 48:0.3 49:0.8 50:95.6 51:0.7 52:1.1 53:0.2 54:3.1 55:1.9 56:0.3 57:0.4 58:1.0 59:2.3 60:10.4 61:0.1 62:107.4 63:0.5 64:1.2 65:0.6 66:0.4 67:0.4 68:4.4 69:0.6 70:99.8 71:1.1 72:0.1 73:0.6 74:2.2 75:1.2 76:2.0 77:0.2 78:0.0 79:10.9 80:107.3 81:0.0 82:48.7 83:1.1 84:2.3 85:3.2 86:2.0 87:0.4 88:0.1 89:62.3 90:1.9 91:0.7 92:1.3 93:2.0 94:2.4 95:56.3 96:2.5 97:1.1 98:1.5 99:0.2 100:0.9 101:0.3 102:2.0 103:24.9 104:10.0 105:7.0 106:44.7 107:7.4 108:0.6 109:1.1 110:0.9 111:1.6 112:0.8 113:2.5 114:0.4 115:0.2 116:26.4 117:481.7
unit 1 n 200169 neg diffs 1 min diff -1777.0319000000002 first [352.4563 352.4692 352.4743] max 1788.7986 dups 0
sub-FF/sub-FF_ses-FF-103_behavior+ecephys.nwb units 78 unsorted [1]
0:6.4 1:126.4 2:0.8 3:3.4 4:0.9 5:1.7 6:3.7 7:121.2 8:2.6 9:0.8 10:4.6 11:1.4 12:0.9 13:0.9 14:0.6 15:0.9 16:0.8 17:0.8 18:262.7 19:126.7 20:0.5 21:4.9 22:2.1 23:3.5 24:1.1 25:0.4 26:0.8 27:0.3 28:2.1 29:116.2 30:1.1 31:0.6 32:8.8 33:1.9 34:6.0 35:9.6 36:2.1 37:1.1 38:2.0 39:0.8 40:1.3 41:81.8 42:13.3 43:1.6 44:2.1 45:1.5 46:1.4 47:0.9
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/scratch/bin/activate; cat > $TMPDIR/rawtest.py <<'E'
import h5py, remfile, numpy as np, time
from dandi.dandiapi import DandiAPIClient
p="sub-GG/sub-GG_ses-GG-097_behavior+ecephys.nwb"
with DandiAPIClient() as c:
    u=c.get_dandiset("000067","0.250624.0419").get_asset_by_path(p).get_content_url(follow_redirects=1, strip_query=True)
f=h5py.File(remfile.File(u),'r')
d=f['acquisition/ElectricalSeries/data']
t=time.time(); x=d[136719*50:136719*51,:]; print('one window all channels',time.time()-t,'s', x.shape)
t=time.time(); x=d[136719*80:136719*81,0:64]; print('64ch',time.time()-t)
print(f['processing/ecephys/LFP/LFP/data'].chunks)
E
python $TMPDIR/rawtest.py
```

```
one window all channels 1.3207972049713135 s (136719, 101)
64ch 1.0244901180267334
(34180, 2)
```

**Agent calls Bash**

```bash
cd paper; for u in "https://static-content.springer.com/esm/art%3A10.1038%2Fnn.2134/MediaObjects/41593_2008_BFnn2134_MOESM1_ESM.pdf" "https://europepmc.org/articles/PMC2562676/bin/NIHMS52220-supplement-Suppl.pdf" "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2562676/bin/NIHMS52220-supplement-Suppl.pdf"; do curl -sL -m 60 -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36" -o s.pdf "$u"; file s.pdf; done
```

```
s.pdf: XML 1.0 document, ASCII text, with very long lines (457), with no line terminators
s.pdf: HTML document, ASCII text, with very long lines (5813), with no line terminators
s.pdf: HTML document, ASCII text, with very long lines (3728)
```

**Agent calls Bash**

```bash
cd paper; head -c 400 s.pdf; echo; curl -sL -m 60 "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2562676/supplementaryFiles" -o supp.zip; file supp.zip; ls -la supp.zip
```

Result: the fetched text is not kept.

**Agent**

Supplement is unreachable (reCAPTCHA); I'll use the main text only. Now testing shank assignment by spike-triggered averages of the raw signal.

**Agent calls Bash**

```bash
cd  rm -f paper/s.pdf paper/supp.zip; . $TMPDIR/scratch/bin/activate; cat > $TMPDIR/sta.py <<'E'
import h5py, remfile, numpy as np, sys, time
from scipy.signal import butter, sosfiltfilt
from dandi.dandiapi import DandiAPIClient
p=sys.argv[1]; nwin=int(sys.argv[2])
with DandiAPIClient() as c:
    u=c.get_dandiset("000067","0.250624.0419").get_asset_by_path(p).get_content_url(follow_redirects=1, strip_query=True)
f=h5py.File(remfile.File(u),'r')
gn=[x.decode() for x in f['general/extracellular_ephys/electrodes/group_name'][:]]
print('groups by channel:', [gn[i] for i in range(0,len(gn),8)], gn[60:70])
el=f['general/extracellular_ephys/electrodes']; print('shank_el_no', el['shank_electrode_number'][:20])
d=f['acquisition/ElectricalSeries/data']; C=136719; nch=d.shape[1]; nchunks=d.shape[0]//C
st=f['units/spike_times'][:]; idx=f['units/spike_times_index'][:]; b=np.concatenate([[0],idx])
wins=np.linspace(1,nchunks-2,nwin).astype(int)
sos=butter(3,[800,5000],btype='band',fs=20000,output='sos')
nu=len(idx); acc=np.zeros((nu,nch,32)); cnt=np.zeros(nu)
t0=time.time()
for w in wins:
    x=d[w*C:(w+1)*C,:96].astype(np.float32); x=sosfiltfilt(sos,x,axis=0)
    a,bnd=w*C/20000,(w+1)*C/20000
    for i in range(nu):
        s=st[b[i]:b[i+1]]; s=s[(s>a+0.002)&(s<bnd-0.002)]
        if len(s)==0: continue
        k=np.round((s-a)*20000).astype(int)
        if len(k)>200: k=k[:200]
        seg=x[k[:,None]+np.arange(-12,20)]  # n,32,ch
        acc[i,:96]+=seg.sum(0).T; cnt[i]+=len(k)
print('read',time.time()-t0)
wf=acc/np.maximum(cnt,1)[:,None,None]
amp=wf.max(2)-wf.min(2)
best=amp.argmax(1)
for i in range(nu):
    sh=gn[best[i]]
    a2=np.sort(amp[i])[::-1]
    print(i, int(cnt[i]), 'best ch',best[i], sh, f"amp {a2[0]:.0f} 2nd-shank-max {max(amp[i][[j for j in range(96) if gn[j]!=sh]]):.0f}", f"rate {(b[i+1]-b[i])/st.max():.1f}")
E
python $TMPDIR/sta.py sub-GG/sub-GG_ses-GG-097_behavior+ecephys.nwb 6
```

Result: not kept, because it reads the paper's text.

**Agent**

Units are ordered by shank, and the first unit of each shank block is a broad, high-rate multi-unit cluster. Now checking the nose-poke sensor channels against the trial table.

**Agent calls Bash**

```bash
. $TMPDIR/scratch/bin/activate; cat > $TMPDIR/sens.py <<'E'
import h5py, remfile, numpy as np, sys
from dandi.dandiapi import DandiAPIClient
p=sys.argv[1]
with DandiAPIClient() as c:
    u=c.get_dandiset("000067","0.250624.0419").get_asset_by_path(p).get_content_url(follow_redirects=1, strip_query=True)
f=h5py.File(remfile.File(u),'r')
L=f['processing/ecephys/LFP/LFP/data']; n=L.shape[0]
s=L[:,96:98].astype(float)
print('ch96/97 percentiles', np.percentile(s,[0,1,50,99,100],axis=0))
t=f['intervals/trials']; st=t['start_time'][:]; sp=t['stop_time'][:]; rw=t['reward_time'][:]; side=[x.decode() for x in t['left_or_right'][:]]
med=np.median(s,0)
for i in range(min(8,len(st))):
    a,b=int(st[i]*1250),int(sp[i]*1250); c2=int(rw[i]*1250)
    np_=np.abs(s[a:b]-med).mean(0); run=np.abs(s[b:c2]-med).mean(0)
    print(side[i], 'nosepoke', np.round(np_), 'run', np.round(run))
E
python $TMPDIR/sens.py sub-GG/sub-GG_ses-GG-097_behavior+ecephys.nwb; python $TMPDIR/sens.py sub-EE/sub-EE_ses-EE-088_behavior+ecephys.nwb
```

```
ch96/97 percentiles [[-3337. -2927.]
 [-1245. -1248.]
 [   58.  -139.]
 [ 1602.  1146.]
 [ 4364.  3929.]]
Left nosepoke [449. 408.] run [427. 376.]
Left nosepoke [425. 401.] run [403. 392.]
Left nosepoke [459. 419.] run [452. 388.]
Right nosepoke [443. 438.] run [497. 394.]
Right nosepoke [485. 426.] run [459. 354.]
Right nosepoke [458. 416.] run [399. 375.]
Left nosepoke [513. 430.] run [375. 356.]
Left nosepoke [494. 385.] run [482. 397.]
ch96/97 percentiles [[-3.2768e+04 -3.2747e+04]
 [-3.0138e+04 -3.0100e+02]
 [-1.2000e+01 -5.0000e+00]
 [ 3.5000e+01  4.4000e+01]
 [ 2.8290e+03  2.6580e+03]]
Right nosepoke [123. 386.] run [23.  7.]
Right nosepoke [19036.   184.] run [23.  7.]
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/scratch/bin/activate; cat > $TMPDIR/sens2.py <<'E'
import h5py, remfile, numpy as np, sys
from dandi.dandiapi import DandiAPIClient
p=sys.argv[1]
with DandiAPIClient() as c:
    u=c.get_dandiset("000067","0.250624.0419").get_asset_by_path(p).get_content_url(follow_redirects=1, strip_query=True)
f=h5py.File(remfile.File(u),'r')
L=f['processing/ecephys/LFP/LFP/data']; nch=L.shape[1]
t=f['intervals/trials']; st=t['start_time'][:]; sp=t['stop_time'][:]; rw=t['reward_time'][:]; side=np.array([x.decode() for x in t['left_or_right'][:]])
end=int(rw[11]*1250)+1250
s=L[:end,94:nch].astype(float); med=np.median(s,0)
for i in range(10):
    a,b=int(st[i]*1250),int(sp[i]*1250); c2=int(rw[i]*1250)
    print(side[i], 'np', np.round(np.abs(s[a:b]-med).mean(0)).astype(int), 'run', np.round(np.abs(s[b:c2]-med).mean(0)).astype(int))
E
python $TMPDIR/sens2.py sub-GG/sub-GG_ses-GG-097_behavior+ecephys.nwb; python $TMPDIR/sens2.py sub-FF/sub-FF_ses-FF-130_behavior+ecephys.nwb
```

```
Left np [545 421 449 408 434 395 136] run [487 406 428 376 399 363 132]
Left np [421 412 425 401 420 386 131] run [421 401 403 392 393 384 129]
Left np [475 434 459 419 458 405 139] run [436 409 452 388 447 377 129]
Right np [470 453 443 438 438 419 123] run [429 406 497 394 492 376 133]
Right np [441 444 486 426 485 413 129] run [383 372 459 354 477 343 136]
Right np [436 416 458 416 433 399 134] run [411 390 399 375 387 367 135]
Left np [444 447 513 430 494 411 130] run [398 384 375 356 364 345 132]
Left np [399 402 494 385 454 369 131] run [424 419 482 397 454 381 129]
Right np [396 393 450 384 441 372 130] run [397 391 408 369 399 357 133]
Right np [547 428 459 419 439 404 130] run [399 382 599 357 535 342 130]
Right np [ 434  417 3019   40    3    4    2    1    1 7558] run [ 422  424   22    7    3    4    2    1    1 6907]
Right np [  391   410 20517   236     3     4     2     1     2  7906] run [ 422  424   21    7    3    4    2    1    1 7295]
Right np [  387   397 19670   226     3     4     2     1     1  6780] run [ 432  450   21    7    3    4    2    1    1 7636]
Left np [ 382  355   91 7568    3    4    2    1    1 4301] run [ 441  440    7   21    3    4    2    1    1 8585]
Left np [  398   356   340 30032     4     4     2     1     2   116] run [ 405  388    7   21    3    4    2    1    2 7839]
Left np [  382   383   238 20807     3     4     3     1     2 12876] run [ 396  389    7   21    3    4    2    1    2 7079]
Right np [  404   401 13649   159     3     4     2     1     2  7742] run [ 418  409   21    7    3    4    2    1    2 7448]
Right np [  387   377 10383   123     3     4     2     1     2  7880] run [ 392  381   22    7    3    4    2    1    2 6791]
Left np [  432   446   339 30027     4     4     2     1     2    20] run [ 429  416    7   21    3    4    2    1    2 8193]
Left np [  404   388   339 29973     4     4     2     1     2 12674] run [ 422  413    7   21    3    4    2    1    2 6842]
```

**Agent calls Bash**

```bash
. $TMPDIR/scratch/bin/activate; sed -i 's/s=L\[:end,94:nch\]/s=L[:end,:]/; s/for i in range(10):/r=[]\nfor i in range(10):/' $TMPDIR/sens2.py; cat >> $TMPDIR/sens2.py <<'E'
E
python - <<'E'
import re
s=open('/tmp/claude-1001/sens2.py').read()
s=s.replace("""    print(side[i], 'np', np.round(np.abs(s[a:b]-med).mean(0)).astype(int), 'run', np.round(np.abs(s[b:c2]-med).mean(0)).astype(int))""","""    r.append(np.abs(s[a:b]-med).mean(0)/np.abs(s[b:c2]-med).mean(0))
r=np.array(r); print('max ratio per channel', np.round(r.max(0),1)); print('std of log ratio', np.round(np.log(r).std(0),2))""")
open('/tmp/claude-1001/sens2.py','w').write(s)
E
python $TMPDIR/sens2.py sub-GG/sub-GG_ses-GG-097_behavior+ecephys.nwb
```

```
max ratio per channel [  1.2   1.2   1.2   1.2   1.6   1.2   1.3   1.3   1.3   1.2   1.2   1.2
   1.3   1.6   1.3   1.6   1.2   1.2   1.2   1.3   1.2   1.5   1.2   1.2
   1.3   1.2   1.3   1.2   1.2   1.2   1.5   1.2   1.3   1.3   1.2   1.2
   1.2   1.2   1.3   1.2   1.2   1.2   1.2   1.2   1.3   1.2   1.2   1.3
   1.3   1.2   1.2   1.2   1.2   1.2   1.4   1.2   1.2   1.3   1.2   1.2
   1.2   1.3   1.2   1.3 530.7 255.2   1.    1.1   1.2   1.    1.    1.1
   1.1   1.3   1.1   1.4   1.1   0.9   1.    0.9   0.9   1.5   1.2   1.
   1.1   1.    1.    1.    1.3   1.1   1.1   1.2   1.1   1.1   1.4   1.2
   1.4   1.2   1.4   1.2   1.1]
std of log ratio [0.05 0.05 0.06 0.11 0.25 0.06 0.06 0.09 0.07 0.05 0.05 0.06 0.08 0.27
 0.07 0.28 0.08 0.07 0.06 0.07 0.05 0.22 0.05 0.06 0.09 0.08 0.07 0.07
 0.09 0.06 0.12 0.06 0.07 0.07 0.07 0.06 0.07 0.06 0.07 0.06 0.06 0.06
 0.05 0.06 0.06 0.05 0.06 0.21 0.1  0.09 0.09 0.09 0.08 0.08 0.09 0.09
 0.09 0.09 0.09 0.09 0.08 0.09 0.08 0.09 2.21 2.1  0.02 0.02 0.08 0.04
 0.04 0.04 0.04 0.12 0.04 0.22 0.07 0.05 0.1  0.04 0.04 0.23 0.16 0.06
 0.05 0.04 0.04 0.04 0.15 0.05 0.05 0.06 0.06 0.05 0.1  0.06 0.14 0.07
 0.13 0.07 0.04]
```

**Agent**

In rat GG the nose-poke sensors sit on channels 65-66, not 97-98 as the CRCNS description says. Checking which channels carry hippocampal theta to place the CA1 probe in each rat.

**Agent calls Bash**

```bash
. $TMPDIR/scratch/bin/activate; cat > $TMPDIR/theta.py <<'E'
import h5py, remfile, numpy as np, sys
from scipy.signal import welch
from dandi.dandiapi import DandiAPIClient
with DandiAPIClient() as c:
  ds=c.get_dandiset("000067","0.250624.0419")
  for p in sys.argv[1:]:
    u=ds.get_asset_by_path(p).get_content_url(follow_redirects=1, strip_query=True)
    f=h5py.File(remfile.File(u),'r')
    L=f['processing/ecephys/LFP/LFP/data']; nch=L.shape[1]
    t=f['intervals/trials']; sp=t['stop_time'][:]; rw=t['reward_time'][:]
    end=int(rw[min(15,len(rw)-1)]*1250)+10
    s=L[:end,:].astype(float)
    segs=[s[int(a*1250):int(b*1250)] for a,b in zip(sp[:15],rw[:15]) if b-a>1.7]
    P=[]
    for x in segs:
        fr,pw=welch(x,fs=1250,nperseg=1024,axis=0); P.append(pw)
    pw=np.mean(P,0)
    th=pw[(fr>=6)&(fr<=10)].sum(0)/pw[(fr>=1)&(fr<=40)].sum(0)
    print(p); print(np.round(th.reshape(-1) ,2).tolist())
    g=np.array([x.decode() for x in f['general/extracellular_ephys/electrodes/group_name'][:]])
    for sh in dict.fromkeys(g): print(sh, np.round(np.median(th[g==sh]),2), end='; ')
    print()
E
python $TMPDIR/theta.py sub-GG/sub-GG_ses-GG-097_behavior+ecephys.nwb sub-EE/sub-EE_ses-EE-088_behavior+ecephys.nwb sub-FF/sub-FF_ses-FF-130_behavior+ecephys.nwb
```

```
sub-GG/sub-GG_ses-GG-097_behavior+ecephys.nwb
[0.23, 0.23, 0.23, 0.22, 0.19, 0.25, 0.25, 0.25, 0.2, 0.2, 0.2, 0.19, 0.21, 0.16, 0.21, 0.16, 0.22, 0.22, 0.22, 0.22, 0.22, 0.16, 0.22, 0.23, 0.23, 0.22, 0.23, 0.22, 0.22, 0.22, 0.22, 0.23, 0.21, 0.21, 0.21, 0.22, 0.22, 0.22, 0.22, 0.22, 0.23, 0.23, 0.23, 0.23, 0.22, 0.24, 0.24, 0.13, 0.22, 0.22, 0.23, 0.23, 0.23, 0.23, 0.23, 0.23, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.22, 0.21, 0.21, 0.22, 0.18, 0.06, 0.59, 0.56, 0.53, 0.52, 0.48, 0.51, 0.43, 0.5, 0.68, 0.61, 0.67, 0.62, 0.49, 0.51, 0.51, 0.51, 0.65, 0.64, 0.59, 0.5, 0.53, 0.51, 0.49, 0.44, 0.57, 0.51, 0.52, 0.45, 0.53, 0.45, 0.53, 0.32]
shank1 0.23; shank2 0.2; shank3 0.22; shank4 0.22; shank5 0.22; shank6 0.23; shank7 0.23; shank8 0.21; shank9 0.22; shank10 0.51; shank11 0.55; shank12 0.51; shank13 0.45; 
sub-EE/sub-EE_ses-EE-088_behavior+ecephys.nwb
[0.2, 0.2, 0.2, 0.2, 0.2, 0.19, 0.19, 0.19, 0.19, 0.19, 0.2, 0.19, 0.2, 0.19, 0.2, 0.2, 0.2, 0.23, 0.23, 0.21, 0.23, 0.23, 0.22, 0.22, 0.22, 0.22, 0.2, 0.23, 0.23, 0.21, 0.22, 0.11, 0.2, 0.2, 0.21, 0.19, 0.21, 0.21, 0.22, 0.21, 0.22, 0.22, 0.22, 0.22, 0.23, 0.23, 0.23, 0.19, 0.25, 0.25, 0.25, 0.25, 0.26, 0.26, 0.26, 0.25, 0.21, 0.2, 0.21, 0.21, 0.21, 0.23, 0.23, 0.23, 0.73, 0.71, 0.73, 0.73, 0.73, 0.72, 0.71, 0.71, 0.67, 0.7, 0.72, 0.72, 0.71, 0.7, 0.68, 0.68, 0.69, 0.69, 0.65, 0.67, 0.65, 0.64, 0.62, 0.63, 0.65, 0.65, 0.65, 0.65, 0.64, 0.62, 0.65, 0.65, 0.23, 0.23, 0.27, 0.19, 0.15, 0.21, 0.22, 0.06]
shank1 0.2; shank2 0.19; shank3 0.22; shank4 0.22; shank5 0.21; shank6 0.22; shank7 0.25; shank8 0.21; shank9 0.73; shank10 0.7; shank11 0.65; shank12 0.65; shank13 0.22; 
sub-FF/sub-FF_ses-FF-130_behavior+ecephys.nwb
[0.24, 0.23, 0.24, 0.24, 0.23, 0.23, 0.23, 0.22, 0.23, 0.23, 0.23, 0.23, 0.23, 0.23, 0.23, 0.23, 0.21, 0.22, 0.22, 0.22, 0.22, 0.22, 0.22, 0.22, 0.2, 0.21, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.21, 0.2, 0.21, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.21, 0.2, 0.21, 0.22, 0.22, 0.21, 0.21, 0.18, 0.21, 0.22,
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s -m 30 "https://api.github.com/repos/SpikeInterface/spikeextractors/commits?per_page=1" | python -c "import json,sys;d=json.load(sys.stdin);print(d[0]['sha'])"; curl -s -m 30 https://raw.githubusercontent.com/SpikeInterface/spikeextractors/master/spikeextractors/extractors/neuroscopeextractors/neuroscopeextractors.py -o $TMPDIR/neuroscope.py; grep -n "keep_mua\|class \|unit_ids\|shank\|def __init__\|sorted\|concat\|res_file\|clu_file" $TMPDIR/neuroscope.py | head -120
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
sed -n 386,425p $TMPDIR/neuroscope.py
```

```
clufile_path = clu_files[0]

        SortingExtractor.__init__(self)

        res_sorting_name = resfile_path.name[:resfile_path.name.find('.res')]
        clu_sorting_name = clufile_path.name[:clufile_path.name.find('.clu')]

        assert res_sorting_name == clu_sorting_name, "The .res and .clu files do not share the same name! " \
                                                     f"{res_sorting_name}  -- {clu_sorting_name}"

        xml_file_path = handle_xml_file_path(folder_path=folder_path, initial_xml_file_path=xml_file_path)
        xml_root = et.parse(str(xml_file_path)).getroot()
        self._sampling_frequency = float(xml_root.find('acquisitionSystem').find('samplingRate').text)

        with open(resfile_path) as f:
            res = np.array([int(line) for line in f], np.int64)
        with open(clufile_path) as f:
            clu = np.array([int(line) for line in f], np.int64)

        n_spikes = len(res)
[... 20 more lines not kept]
```

**Agent**

I have enough to start the helper module. Creating the entry directory and a first version of `pfc.py`.

**Agent calls Bash**

```bash
mkdir -p entries/000067-fujisawa-2008; cat entries/001453-fouke-2025/requirements.lock.txt | head -20; sed -n 80,200p entries/001453-fouke-2025/omr.py
```

```
# This file was autogenerated by uv via the following command:
#    uv pip compile --python-version 3.13 requirements.in -o requirements.lock.txt
acres==0.5.0
    # via bidsschematools
aiohappyeyeballs==2.7.1
    # via aiohttp
aiohttp==3.14.5
    # via nwbinspector
aiosignal==1.4.0
    # via aiohttp
annotated-types==0.8.0
    # via pydantic
arrow==1.4.0
    # via isoduration
attrs==26.1.0
    # via
    #   aiohttp
    #   jsonschema
    #   referencing
bids-validator-deno==3.0.2
[... 121 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/000067-fujisawa-2008/pfc.py",
 "content": "\"\"\"Loading and measures for dandiset 000067 (Fujisawa, Amarasingham, Harrison & Buzsaki 2008).\n\nFujisawa S, Amarasingham A, Harrison MT, Buzsaki G (2008). Behavior-dependent short-term\nassembly dynamics in the medial prefrontal cortex. Nature Neuroscience 11, 823-833.\ndoi:10.1038/nn.2134.\n\nEach NWB file is one recording session of one rat (EE, FF or GG). Working memory sessions hold\nthe spike times of every sorted cluster of the session, the trial table (correct trials only),\nthe linearized position, the x coordinate of the head LEDs, the LFP at 1250 Hz and, in most of\nthem, the wideband signal at 20 kHz. Files are streamed from the archive at the pinned version;\nnothing is written to disk.\n\nWhat the files do not say, and where it is taken from here:\n\n- The units table holds spike times only: no shank, channel, brain region or cell type, and no\n  flag for multi-unit clusters. The shank of each unit is found from the data: the mean\n  wideband waveform (800 to 5000 Hz, the band the Methods give for spike sorting) of its spikes\n  in a few windows of the raw signal, on every channel; the unit's channel is the one with the\n  largest peak-to-trough amplitude. The region of a channel comes from the CRCNS pfc-2 data\n  description (doi:10.6080/K01V5BWK, version 0.7 of the document): channels 1 to 64 are the\n  64-site prefrontal probe (8 shanks of 8 sites, so shank = channel // 8 counting from 0) and\n  the next 32 are the CA1 probe. The notebook checks this map against the LFP.\n- Multi-unit clusters: the conversion read the clusters with spikeextractors'\n  NeuroscopeSortingExtractor, which keeps cluster 1 (multi-unit activity) and puts it first in\n  each shank's block of units, and puts the shanks one after another. `MUA_RULE` flags the first\n  unit of each shank block as multi-unit; the notebook shows the evidence.\n- The trial table's columns are those of the CRCNS SessionNP matrix: `start_time` is the start\n  of the first nose poke, `stop_time` the end of the last nose poke (the paper's trial start,\n  position 0) and `reward_time` the start of reward consumption (the paper's trial end, position\n  1). Here they are named nosepoke_start, run_start and run_end.\n- The linearized position runs from 1 (start) to 2 (reward) and is 0 outside trials; the paper's\n  normalized position is d - 1.\n\nParameters, and where they come from:\n\n- JITTER_S = 0.005, N_JITTER = 1000, CCG window of +-5 ms, significance when the cross-\n  correlogram breaks the 99% global band anywhere from 1 to 4 ms: the paper's Methods.\n  The bin width of the cross-correlogram (1 ms) is not given in the main text and is chosen here.\n- KERNEL_SIGMA = 0.05 (normalized length), the permutation test of left against right with\n  pointwise and global bands at alpha 0.05: the paper's Methods. The number of permutations\n  (N_PERM = 1000) and the position grid (101 points) are chosen here.\n- Coincidence lags of 1 to 4 ms for position dependence of monosynaptic interactions, and the\n  one-sided global band at 0.01: the paper's Methods.\n- First spikes after at least 200 ms of silence and later spikes within 40 ms of the previous\n  one, a permutation test of the labels at two-sided P < 0.10: the paper's Results and Figure 6\n  legend. The measure of transmission (excess spikes from 1 to 4 ms per presynaptic spike, over\n  the jitter expectation) is chosen here; the paper's \"rate-normalized height\" is defined in a\n  supplementary figure that could not be retrieved.\n- The 1 Hz minimum of peak rate in trials for position analyses is the \"Cells\" criterion of\n  the CRCNS pfc-2 description, not the paper.\n\"\"\"\n\nfrom __future__ import annotations\n\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nfrom dandi.dandiapi import DandiAPIClient\nfrom scipy.signal import butter, decimate, sosfiltfilt, welch\n\nDANDISET_ID = \"000067\"\nDANDISET_VERSION = \"0.250624.0419\"\n\nRAW_HZ = 20000.0\nLFP_HZ = 1250.0\nPOS_HZ = 20000.0 / 512          # 39.0625 Hz, the rate of the position series\nRAW_CHUNK = 136719              # rows per HDF5 chunk of the wideband series (one channel each)\nN_PFC_CHANNELS = 64             # CRCNS pfc-2: channels 1-64 are the prefrontal probe\nCA1_CHANNELS = {\"EE\": range(64, 96), \"FF\": range(64, 96), \"GG\": range(69, 101)}\n# Nose-poke sensors. CRCNS pfc-2 gives channels 97 (right) and 98 (left), 1-based; in rat GG the\n# data show them at 65 and 66 (see the notebook), so the map is per rat (0-based here).\nNOSEPOKE_CHANNELS = {\"EE\": (96, 97), \"FF\": (96, 97), \"GG\": (64, 65)}\nSPIKE_BAND = (800.0, 5000.0)\n\nJITTER_S = 0.005\nN_JITTER = 1000\nCCG_BIN_S = 0.001\nCCG_LAGS_MS = np.arange(-5, 6)      # bin centres, ms\nTEST_LAGS_MS = (1, 2, 3, 4)\nKERNEL_SIGMA = 0.05\nN_PERM = 1000\nGRID = np.linspace(0, 1, 101)\nMIN_PEAK_HZ = 1.0\nMUA_RULE = \"first unit of each shank block\"\n\n# Working memory sessions in CRCNS pfc-2's session table that have a trial table here.\nWM_SESSIONS = [\"EE.049\", \"EE.088\", \"EE.196\", \"FF.103\", \"FF.130\", \"FF.167\", \"GG.069\", \"GG.097\",\n               \"GG.149\"]\n\n\ndef asset_urls() -> dict[str, str]:\n    \"\"\"{path: streaming URL} of every NWB file at the pinned version.\"\"\"\n    with DandiAPIClient() as client:\n        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)\n        return {a.path: a.get_content_url(follow_redirects=1, strip_query=True)\n                for a in dandiset.get_assets() if a.path.endswith(\".nwb\")}\n\n\ndef _text(value) -> str:\n    value = value[()]\n    if isinstance(value, np.ndarray):\n        value = value.ravel()[0]\n    return value.decode() if isinstance(value, bytes) else str(value)\n\n\ndef describe_file(path: str, url: str) -> dict:\n    \"\"\"What one file holds, without reading the large series.\"\"\"\n    with h5py.File(remfile.File(url), \"r\") as f:\n        out = {\"path\": path, \"session\": _text(f[\"general/session_id\"]),\n               \"subject\": _text(f[\"general/subject/subject_id\"]),\n               \"start\": _text(f[\"session_start_time\"])[:10]}\n        el = f[\"general/extracellular_ephys/electrodes\"]\n        out[\"channels\"] = len(el[\"id\"])\n        out[\"locations\"] = sorted({v.decode() for v in el[\"location\"][:]})\n        out[\"groups\"] = len({v.decode() for v in el[\"group_name\"][:]})\n        out[\"xyz_all_nan\"] = bool(all(np.isnan(el[k][:]).all() for k in \"xyz\"))\n        out[\"raw_s\"] = (f[\"acquisition/ElectricalSeries/data\"].shape[0] / RAW_HZ\n                        if \"acquisition/ElectricalSeries\" in f else 0.0)\n        out[\"lfp_s\"] = f[\"processing/ecephys/LFP/LFP/data\"].shape[0] / LFP_HZ\n        out[\"units\"] = len(f[\"units/id\"]) if \"units\" in f else 0\n        out[\"unit_columns\"] = list(f[\"units\"].attrs[\"colnames\"]) if \"units\" in f else []\n        out[\"spikes\"] = len(f[\"units/spike_times\"]) if \"units\" in f else 0\n        out[\"trials\"] = len(f[\"intervals/trials/id\"]) if \"intervals/trials\" in f else 0\n        out[\"position\"] = \"processing/behavior\" in f\n        # fingerprints used to look for recordings deposited twice\n        lfp = f[\"processing/ecephys/LFP/LFP/data\"]\n        out[\"lfp_head\"] = lfp[:1250, 0].astype(np.int64).tobytes().hex()[:64] if lfp.shape[0] else \"\"\n        out[\"spike_head\"] = (np.round(f[\"units/spike_times\"][:50] * RAW_HZ).astype(np.int64).tobytes().hex()[:64]\n                             if out[\"spikes\"] else \"\")\n    return out\n\n\ndef _sorted_trains(times: np.ndarray, index: np.ndarray):\n    bounds = np.concatenate([[0], index]).astype(np.int64)\n    trains, unsorted = [], []\n    for i in range(len(index)):\n        s = times[bounds[i]:bounds[i + 1]]\n        if np.any(np.diff(s) < 0):\n            unsorted.append(i)\n            s = np.sort(s)\n        trains.append(s)\n    return trains, unsorted\n\n\ndef _raw_windows(trials: pd.DataFrame, n_chunks: int, n_windows: int) -> np.ndarray:\n    \"\"\"Chunks of the raw series that overlap trials most, spread over the session.\"\"\"\n    t0 = np.arange(n_chunks) * RAW_CHUNK / RAW_HZ\n    t1 = t0 + RAW_CHUNK / RAW_HZ\n    overlap = np.zeros(n_chunks)\n    for a, b in zip(trials.nosepoke_start, trials.run_end):\n        overlap += np.clip(np.minimum(t1, b) - np.maximum(t0, a), 0, None)\n    candidates = np.flatnonzero(overlap > 0)\n    if len(candidates) <= n_windows:\n        return candidates\n    picks = np.linspace(0, len(candidates) - 1, n_windows).round().astype(int)\n    return candidates[picks]\n\n\ndef load_session(path: str, url: str, n_windows: int = 12) -> dict:\n    \"\"\"One working memory session: spikes, trials, position, unit channels and LFP checks.\"\"\"\n    s = {\"path\": path}\n    with h5py.File(remfile.File(url), \"r\") as f:\n        s[\"session\"] = _text(f[\"general/session_id\"])\n        s[\"subject\"] = _text(f[\"general/subject/subject_id\"])\n        s[\"trains\"], s[\"unsorted_units\"] = _sorted_trains(f[\"units/spike_times\"][:],\n                                                          f[\"units/spike_times_index\"][:])\n        tr = f[\"intervals/trials\"]\n        s[\"trials\"] = pd.DataFrame({\n            \"nosepoke_start\": tr[\"start_time\"][:], \"run_start\": tr[\"stop_time\"][:],\n            \"run_end\": tr[\"reward_time\"][:],\n            \"side\": [v.decode() for v in tr[\"left_or_right\"][:]]})\n        s[\"trial_descriptions\"] = {k: tr[k].attrs.get(\"description\") for k in tr.attrs[\"colnames\"]}\n        beh = f[\"processing/behavior\"]\n        lin = beh[\"LinearizedPosition/LinearizedTimeSeries\"]\n        s[\"lin\"] = lin[\"data\"][:]\n        s[\"lin_rate\"] = float(lin[\"starting_time\"].attrs[\"rate\"])\n        s[\"lin_unit\"] = lin[\"data\"].attrs[\"unit\"]\n        s[\"x1\"] = beh[\"Position/SpatialSeries1/data\"][:, 0]\n        s[\"x2\"] = beh[\"Position/SpatialSeries2/data\"][:, 0]\n        s[\"pos_unit\"] = beh[\"Position/SpatialSeries1/data\"].attrs[\"unit\"]\n        lfp = f[\"processing/ecephys/LFP/LFP/data\"]\n        s[\"lfp_rate\"] = float(f[\"processing/ecephys/LFP/LFP/starting_time\"].attrs[\"rate\"])\n        s[\"duration\"] = lfp.shape[0] / s[\"lfp_rate\"]\n        s[\"n_channels\"] = lfp.shape[1]\n        right, left = NOSEPOKE_CHANNELS[s[\"subject\"]]\n        s[\"sensors\"] = lfp[:, [right, left]].astype(np.float32)\n        s[\"has_raw\"] = \"acquisition/ElectricalSeries\" in f\n        s[\"sta_amp\"] = None\n        if s[\"has_raw\"]:\n            raw = f[\"acquisition/ElectricalSeries/data\"]\n            s[\"raw_rate\"] = float(f[\"acquisition/ElectricalSeries/starting_time\"].attrs[\"rate\"])\n            windows = _raw_windows(s[\"trials\"], raw.shape[0] // RAW_CHUNK, n_windows)\n            s.update(_waveforms_and_theta(raw, windows, s[\"trains\"]))\n    return s\n\n\ndef _waveforms_and_theta(raw, windows, trains, per_window: int = 200) -> dict:\n    \"\"\"Mean wideband waveform amplitude of each unit on each channel, and LFP theta per channel.\n\n    Theta ratio: power from 6 to 10 Hz over power from 1 to 40 Hz of the raw signal decimated to\n    1250 Hz, averaged over the windows (which overlap trials, when the rat runs).\n    \"\"\"\n    sos = butter(3, SPIKE_BAND, btype=\"band\", fs=RAW_HZ, output=\"sos\")\n    n_ch = raw.shape[1]\n    acc = np.zeros((len(trains), n_ch, 32))\n    count = np.zeros(len(trains), int)\n    spectra = []\n    for w in windows:\n        x = raw[w * RAW_CHUNK:(w + 1) * RAW_CHUNK, :].astype(np.float32)\n        low = decimate(decimate(x, 4, axis=0), 4, axis=0)\n        freq, p = welch(low, fs=RAW_HZ / 16, nperseg=1024, axis=0)\n        spectra.append(p)\n        hp = sosfiltfilt(sos, x, axis=0)\n        a, b = w * RAW_CHUNK / RAW_HZ, (w + 1) * RAW_CHUNK / RAW_HZ\n        for i, st in enumerate(trains):\n            k = st[(st > a + 0.002) & (st < b - 0.002)]\n            if len(k) == 0:\n                continue\n            k = np.round((k[:per_window] - a) * RAW_HZ).astype(int)\n            acc[i] += hp[k[:, None] + np.arange(-12, 20)].sum(0).T\n            count[i] += len(k)\n    mean = acc / np.maximum(count, 1)[:, None, None]\n    power = np.mean(spectra, axis=0)\n    theta = power[(freq >= 6) & (freq <= 10)].sum(0) / power[(freq >= 1) & (freq <= 40)].sum(0)\n    return {\"sta_amp\": mean.max(2) - mean.min(2), \"sta_count\": count, \"theta_ratio\": theta,\n            \"raw_windows\": list(map(int, windows))}\n\n\ndef load_sessions(paths: list[str], workers: int = 5, n_windows: int = 12) -> list[dict]:\n    urls = asset_urls()\n    with ThreadPoolExecutor(workers) as pool:\n        return list(pool.map(lambda p: load_session(p, urls[p], n_windows), paths))\n\n\ndef assign_units(s: dict, min_spikes: int = 5) -> pd.DataFrame:\n    \"\"\"One row per unit: rate, refractory violations, best channel, shank, region, multi-unit flag.\n\n    Channel: largest peak-to-trough amplitude of the mean waveform, for units with at least\n    `min_spikes` spikes in the raw windows. A unit with fewer takes the shank of its neighbours in\n    the unit order when both neighbours share it (units are stored shank by shank).\n    \"\"\"\n    rows = []\n    for i, st in enumerate(s[\"trains\"]):\n        isi = np.diff(st)\n        rows.append({\"unit\": i, \"n_spikes\": len(st), \"rate_hz\": len(st) / s[\"duration\"],\n                     \"isi_lt2ms\": float(np.mean(isi < 0.002)) if len(isi) else np.nan})\n    u = pd.DataFrame(rows)\n    amp, count = s[\"sta_amp\"], s[\"sta_count\"]\n    u[\"sta_spikes\"] = count\n    best = amp.argmax(1)\n    u[\"channel\"] = np.where(count >= min_spikes, best, -1)\n    u[\"amp_uv\"] = amp[np.arange(len(u)), best] * 0.3815 / 0.3815   # stored in microvolts (conversion 1e-6)\n    sh = np.where(u.channel >= 0, u.channel // 8, -1)\n    for i in np.flatnonzero(sh < 0):\n        lo = sh[:i][sh[:i] >= 0]\n        hi = sh[i + 1:][sh[i + 1:] >= 0]\n        if len(lo) and len(hi) and lo[-1] == hi[0]:\n            sh[i] = lo[-1]\n    u[\"shank\"] = sh\n    u[\"region\"] = np.where(sh < 0, \"unassigned\",\n                           np.where(sh < N_PFC_CHANNELS // 8, \"PFC\", \"other\"))\n    starts = np.r_[True, sh[1:] != sh[:-1]]\n    u[\"first_of_block\"] = starts & (sh >= 0)\n    u[\"mua\"] = u.first_of_block\n    u[\"session\"] = s[\"session\"]\n    u[\"subject\"] = s[\"subject\"]\n    return u\n"
}
```

```
File created successfully at: entries/000067-fujisawa-2008/pfc.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/000067-fujisawa-2008; sed -i 's|    u\["amp_uv"\] = amp\[np.arange(len(u)), best\] \* 0.3815 / 0.3815   # stored in microvolts (conversion 1e-6)|    u["amp_uv"] = amp[np.arange(len(u)), best]     # int16 values with conversion 1e-6: microvolts|' pfc.py; grep -n amp_uv pfc.py; . $TMPDIR/scratch/bin/activate; cat > $TMPDIR/drv.py <<'E'
import sys, time, pickle
sys.path.insert(0,'.')
import pfc
t=time.time()
urls=pfc.asset_urls()
paths=sorted(p for p in urls if any(p.split('_ses-')[1].startswith(s.replace('.','-')) for s in pfc.WM_SESSIONS))
print(paths)
S=pfc.load_sessions(paths)
print('loaded',time.time()-t)
pickle.dump(S,open('/tmp/claude-1001/S.pkl','wb'))
E
python $TMPDIR/drv.py
```

```
255:    u["amp_uv"] = amp[np.arange(len(u)), best]     # int16 values with conversion 1e-6: microvolts
['sub-EE/sub-EE_ses-EE-049_behavior+ecephys.nwb', 'sub-EE/sub-EE_ses-EE-088_behavior+ecephys.nwb', 'sub-EE/sub-EE_ses-EE-196_behavior+ecephys.nwb', 'sub-FF/sub-FF_ses-FF-103_behavior+ecephys.nwb', 'sub-FF/sub-FF_ses-FF-130_behavior+ecephys.nwb', 'sub-FF/sub-FF_ses-FF-167_behavior+ecephys.nwb', 'sub-GG/sub-GG_ses-GG-069_behavior+ecephys.nwb', 'sub-GG/sub-GG_ses-GG-097_behavior+ecephys.nwb', 'sub-GG/sub-GG_ses-GG-149_behavior+ecephys.nwb']
loaded 342.8583996295929
```

**Agent**

Loading takes about 6 minutes. Now examining unit assignment across sessions.

**Agent calls Bash**

```bash
cd entries/000067-fujisawa-2008; . $TMPDIR/scratch/bin/activate; python - <<'E'
import pickle, sys, numpy as np, pandas as pd
sys.path.insert(0,'.'); import pfc
S=pickle.load(open('/tmp/claude-1001/S.pkl','rb'))
pd.set_option('display.width',250)
allu=[]
for s in S:
    if not s['has_raw']: print(s['session'],'no raw'); continue
    u=pfc.assign_units(s); allu.append(u)
    print(s['session'], 'units',len(u),'unsorted',s['unsorted_units'], 'windows',len(s['raw_windows']))
    print(' shank seq:', ''.join('x' if v<0 else ('ABCDEFGHIJKLMNOP'[v]) for v in u.shank))
    print(' theta by shank:', np.round([np.median(s['theta_ratio'][g*8:(g+1)*8]) for g in range(s['n_channels']//8)],2))
U=pd.concat(allu)
print(U.groupby(['region','mua']).agg(n=('unit','size'),rate=('rate_hz','median'),isi=('isi_lt2ms','median'),amp=('amp_uv','median')))
print(U[U.mua & (U.region=='PFC')][['session','unit','rate_hz','isi_lt2ms','amp_uv']].to_string())
print(U.groupby(['session','region']).size().unstack())
print('unsorted unit rows:'); 
for s in S:
    for i in s['unsorted_units']:
        u=U[(U.session==s['session'])&(U.unit==i)]; print(s['session'],i,u[['shank','mua','rate_hz','isi_lt2ms']].values)
E
```

```
EE.049 units 118 unsorted [1] windows 12
 shank seq: AAAAAAAABBBBBBBBBBBBBBCCCCCCCCCCCCCCCCxDDDDDDDDDDxEEEEEEEEEEEEFFFFFFFFGGGGGGGGGGHxIIIIIIIJJJJJJKKKKKKKKKKKLLLLLLLLLLLM
 theta by shank: [0.25 0.25 0.28 0.28 0.28 0.28 0.28 0.23 0.53 0.53 0.51 0.49 0.11]
EE.088 no raw
EE.196 units 161 unsorted [1] windows 12
 shank seq: AAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDDDDDDDDMEEEEEEEEEEEEEEFFFFFFMFFFFFFGGGGMGGGGGGGGGGGGGGGHHHHHMHHHHHHHIIIIIIIIJJJJJJJJKKLM
 theta by shank: [0.21 0.21 0.22 0.16 0.22 0.21 0.21 0.22 0.56 0.54 0.52 0.52 0.19]
FF.103 units 78 unsorted [1] windows 12
 shank seq: AAAAAAABBBBBBBBBBBCDDDDDDDDDDEEEEEEEEEEEEFFFFFFFFFFFFFFFGGHIIIIIIIJJJJJKKLMMBB
 theta by shank: [0.2  0.19 0.19 0.19 0.19 0.19 0.21 0.18 0.44 0.42 0.42 0.45 0.18]
FF.130 units 90 unsorted [1] windows 12
 shank seq: AAAAAAAAAAAAABBBBBBBBBBBBBBCCCCDDDDDDDDDDDDDDEEEEEEEEEEEEEEEEEEFFFFFFFGHHHHHIIIJJJJJJJKKLD
 theta by shank: [0.2  0.2  0.2  0.19 0.2  0.21 0.22 0.21 0.56 0.53 0.53 0.55 0.18]
FF.167 units 64 unsorted [] windows 12
 shank seq: ABBBBCCCCCCCCCCCCCCDDDDDEEEEEFFFFFFFGGGGGGGGGGGHHHHIJJJJFKKKFLLM
 theta by shank: [0.21 0.21 0.21 0.22 0.21 0.21 0.23 0.23 0.51 0.49 0.49 0.52 0.15]
GG.069 units 76 unsorted [1] windows 12
 shank seq: AABCDEEEEEFFFFFFFFFFGGGHHHHJJIIJJJIIIJJJJJJKJJJJJKKKLLLLLLLKLKLLKLLMLLLLLMLI
 theta by shank: [0.18 0.17 0.17 0.17 0.17 0.18 0.21 0.19 0.23 0.37 0.43 0.38]
GG.097 units 69 unsorted [] windows 12
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000067-fujisawa-2008; . $TMPDIR/scratch/bin/activate; python - <<'E'
import pickle, sys, numpy as np, pandas as pd
sys.path.insert(0,'.'); import pfc
S=pickle.load(open('/tmp/claude-1001/S.pkl','rb'))
U=pd.concat([pfc.assign_units(s) for s in S if s['has_raw']])
v=U.isi_lt2ms.values
print(np.histogram(v,[0,0.001,0.002,0.005,0.01,0.02,0.05,0.1,0.2,0.5,1]))
print(pd.crosstab(U.first_of_block, pd.cut(U.isi_lt2ms,[-1,0.01,0.05,0.1,1])))
print(U[(U.isi_lt2ms>0.01)&(U.isi_lt2ms<0.1)][['session','unit','rate_hz','isi_lt2ms','first_of_block','region']])
E
```

```
Exit code 1
(array([417,  95,  79,  12,   2,   5,   5,  20,  75,   8]), array([0.   , 0.001, 0.002, 0.005, 0.01 , 0.02 , 0.05 , 0.1  , 0.2  ,
       0.5  , 1.   ]))
Traceback (most recent call last):
  File "<stdin>", line 7, in <module>
  File "/tmp/claude-1001/scratch/lib/python3.13/site-packages/pandas/core/reshape/pivot.py", line 1099, in crosstab
    df = DataFrame(data, index=common_idx)
  File "/tmp/claude-1001/scratch/lib/python3.13/site-packages/pandas/core/frame.py", line 769, in __init__
    mgr = dict_to_mgr(data, index, columns, dtype=dtype, copy=copy)
  File "/tmp/claude-1001/scratch/lib/python3.13/site-packages/pandas/core/internals/construction.py", line 460, in dict_to_mgr
    return arrays_to_mgr(arrays, columns, index, dtype=dtype, consolidate=copy)
  File "/tmp/claude-1001/scratch/lib/python3.13/site-packages/pandas/core/internals/construction.py", line 118, in arrays_to_mgr
    arrays, refs = _homogenize(arrays, index, dtype)
                   ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/scratch/lib/python3.13/site-packages/pandas/core/internals/construction.py", line 568, in _homogenize
    val = val.reindex(index)
  File "/tmp/claude-1001/scratch/lib/python3.13/site-packages/pandas/core/series.py", line 5525, in reindex
    return super().reindex(
           ~~~~~~~~~~~~~~~^
        index=index,
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000067-fujisawa-2008; python - <<'E'
s=open('pfc.py').read()
old_start=s.index('def assign_units')
s=s[:old_start]+'''def neural_channels(subject: str) -> np.ndarray:
    """Channels of the two probes (0-based): the prefrontal 0-63 and the CA1 probe of the rat."""
    return np.r_[np.arange(N_PFC_CHANNELS), np.array(CA1_CHANNELS[subject])]


def assign_units(s: dict, min_spikes: int = 5) -> pd.DataFrame:
    """One row per unit: rate, refractory violations, best channel, shank, region, multi-unit flag.

    Channel: the neural channel with the largest peak-to-trough amplitude of the mean waveform,
    for units with at least `min_spikes` spikes in the raw windows. A unit with fewer takes the
    shank of its neighbours in the unit order when both neighbours share it (the units are stored
    shank by shank). Multi-unit: more than `MAX_ISI_VIOLATION` of inter-spike intervals below
    2 ms (`mua`); `first_of_block` is the conversion's ordering rule, shown as a variant.
    """
    rows = []
    for i, st in enumerate(s["trains"]):
        isi = np.diff(st)
        rows.append({"unit": i, "n_spikes": len(st), "rate_hz": len(st) / s["duration"],
                     "isi_lt2ms": float(np.mean(isi < 0.002)) if len(isi) else 0.0})
    u = pd.DataFrame(rows)
    chans = neural_channels(s["subject"])
    amp, count = s["sta_amp"][:, chans], s["sta_count"]
    best = chans[amp.argmax(1)]
    u["sta_spikes"] = count
    u["channel"] = np.where(count >= min_spikes, best, -1)
    u["amp_uv"] = np.where(count >= min_spikes, amp.max(1), np.nan)  # int16 x 1e-6 V: microvolts
    sh = np.where(u.channel >= 0, u.channel // 8, -1)
    for i in np.flatnonzero(sh < 0):
        lo = sh[:i][sh[:i] >= 0]
        hi = sh[i + 1:][sh[i + 1:] >= 0]
        if len(lo) and len(hi) and lo[-1] == hi[0]:
            sh[i] = lo[-1]
    u["shank"] = sh
    u["region"] = np.where(sh < 0, "unassigned", np.where(sh < N_PFC_CHANNELS // 8, "PFC", "CA1"))
    u["first_of_block"] = np.r_[True, sh[1:] != sh[:-1]] & (sh >= 0)
    u["mua"] = u.isi_lt2ms > MAX_ISI_VIOLATION
    u["session"] = s["session"]
    u["subject"] = s["subject"]
    return u
'''
s=s.replace('MUA_RULE = "first unit of each shank block"','MAX_ISI_VIOLATION = 0.02      # fraction of ISIs < 2 ms above which a cluster is multi-unit (chosen here)')
open('pfc.py','w').write(s)
E
grep -n "MUA_RULE\|MAX_ISI" pfc.py
```

```
25:  each shank's block of units, and puts the shanks one after another. `MUA_RULE` flags the first
87:MAX_ISI_VIOLATION = 0.02      # fraction of ISIs < 2 ms above which a cluster is multi-unit (chosen here)
249:    shank by shank). Multi-unit: more than `MAX_ISI_VIOLATION` of inter-spike intervals below
273:    u["mua"] = u.isi_lt2ms > MAX_ISI_VIOLATION
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/000067-fujisawa-2008/pfc.py",
 "old_string": "  each shank's block of units, and puts the shanks one after another. `MUA_RULE` flags the first\n  unit of each shank block as multi-unit; the notebook shows the evidence.",
 "new_string": "  each shank's block of units, and puts the shanks one after another. Here a cluster is taken as\n  multi-unit when more than `MAX_ISI_VIOLATION` of its inter-spike intervals are shorter than\n  2 ms (a common choice); the conversion's rule, the first unit of each shank block, is a\n  variant. The notebook shows the evidence for both."
}
```

```
The file entries/000067-fujisawa-2008/pfc.py has been updated successfully. (note: the file had been modified on disk since you last read it — the edit applied cleanly, but the file contains other changes not in your context. Read it before edits that depend on surrounding content.)
```

**Agent calls Bash**

```bash
cd entries/000067-fujisawa-2008; . $TMPDIR/scratch/bin/activate; python - <<'E'
import pickle, sys, numpy as np, pandas as pd
sys.path.insert(0,'.'); import pfc
S=pickle.load(open('/tmp/claude-1001/S.pkl','rb'))
U=pd.concat([pfc.assign_units(s) for s in S if s['has_raw']],ignore_index=True)
for s in S:
    if not s['has_raw']: continue
    u=U[U.session==s['session']]
    print(s['session'], ''.join('x' if v<0 else ('ABCDEFGHIJKLMNOP'[v]) for v in u.shank), ''.join('m' if m else '.' for m in u.mua))
print(pd.crosstab([U.region],[U.mua,U.first_of_block]))
print(U[~U.mua].groupby(['subject','session','region']).size().unstack())
E
```

```
EE.049 AAAAAAAABBBBBBBBBBBBBBCCCCCCCCCCCCCCCCxDDDDDDDDDDxEEEEEEEEEEEEFFFFFFFFGGGGGGGGGGHxIIIIIIIJJJJJJKKKKKKKKKKKLLLLLLLLLLLC mm......m.............m................m..........m...........m.......m.........m.m......m.....m..........m..........m
EE.196 AAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBCCCCCCCCCCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDDDDDDDDDEEEEEEEEEEEEEEFFFFFFFFFFFFFGGGGGGGGGGGGGGGGGGGGHHHHHHHHHHHHHIIIIIIIIJJJJJJJJKKLK mm.........m.....................m........................m......................m.............m............m...................m............m.......m.......m.m.
FF.103 AAAAAAABBBBBBBBBBBCDDDDDDDDDDEEEEEEEEEEEEFFFFFFFFFFFFFFFGGHIIIIIIIJJJJJKKLBEBB mm.....m..........mm.........m...........m..............m.mm......m....m.mmmmm
FF.130 AAAAAAAAAAAAABBBBBBBBBBBBBBCCCCDDDDDDDDDDDDDDEEEEEEEEEEEEEEEEEEFFFFFFFGHHHHHIIIJJJJJJJKKLD mm...........m.............m...m.............m.................m......mm....m..m......m.mm
FF.167 ABBBBCCCCCCCCCCCCCCDDDDDEEEEEFFFFFFFGGGGGGGGGGGHHHHIJJJJFKKKFLLF mm...m.............m....m....m......m..........m...mm...m...m...
GG.069 AABCDEEEEEFFFFFFFFFFGGGHHHHJJIIJJJIIIJJJJJJKJJJJJKKKLLLLLLLKLKLLKLLMLLLLLMLL mmmmmm....m.........m..m...m...............m......mmm............mm........m
GG.097 ABCDEEEEEFFFFFFFFFFGGGGHHHHJJJJJxKKKKKKKKKKLKLLLLLKMLMxJHxxLIJJJJJGKx mmmmm....m.........m...m...m.....m.........m.......m..m..............
GG.149 AAAABBBBBBBBBBAADDEEFFFGHHJJKJKKKJKKKKJKKKKLLLLKKLLMMMLMxLLLFKH m...m.........mm..m.m..mm.m.m..............m......m.....m......
mua            False       True       
first_of_block False True  False True 
region                                
CA1              136    41     5    29
PFC              416     6     7    70
unassigned         7     0     2     0
region            CA1    PFC  unassigned
subject session                         
EE      EE.049   31.0   70.0         3.0
        EE.196   16.0  132.0         NaN
FF      FF.103   11.0   50.0         NaN
        FF.130    9.0   67.0         NaN
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000067-fujisawa-2008; . $TMPDIR/scratch/bin/activate; python - <<'E'
import pickle, sys, numpy as np, pandas as pd
sys.path.insert(0,'.'); import pfc
S=pickle.load(open('/tmp/claude-1001/S.pkl','rb'))
for s in S:
    if not s['has_raw']: continue
    ch=pfc.neural_channels(s['subject']); aux=np.setdiff1d(np.arange(s['n_channels']),ch)
    A=s['sta_amp']; u=pfc.assign_units(s)
    for i in range(len(A)):
        if s['sta_count'][i]>0 and A[i].argmax() in aux:
            print(s['session'],i,'count',s['sta_count'][i],'aux amp',int(A[i,aux].max()),'neural amp',int(A[i,ch].max()),'neural ch',u.channel[i],'rate',round(u.rate_hz[i],2),'isi',round(u.isi_lt2ms[i],3))
E
```

```
EE.049 117 count 2400 aux amp 37 neural amp 5 neural ch 22 rate 481.74 isi 0.803
EE.196 80 count 24 aux amp 727 neural amp 516 neural ch 27 rate 0.38 isi 0.0
EE.196 101 count 23 aux amp 1026 neural amp 381 neural ch 43 rate 0.69 isi 0.0
EE.196 112 count 31 aux amp 565 neural amp 389 neural ch 51 rate 0.65 isi 0.003
EE.196 133 count 30 aux amp 1011 neural amp 369 neural ch 59 rate 0.51 isi 0.0
EE.196 160 count 111 aux amp 6106 neural amp 29 neural ch 82 rate 0.97 isi 0.0
FF.103 74 count 145 aux amp 4565 neural amp 23 neural ch 10 rate 1.51 isi 0.241
FF.103 75 count 25 aux amp 1501 neural amp 59 neural ch 39 rate 4.43 isi 0.942
FF.167 63 count 157 aux amp 4186 neural amp 35 neural ch 47 rate 1.22 isi 0.016
GG.069 75 count 2400 aux amp 24 neural amp 6 neural ch 91 rate 380.02 isi 0.929
GG.097 55 count 26 aux amp 7598 neural amp 154 neural ch 76 rate 0.28 isi 0.0
GG.097 56 count 13 aux amp 7494 neural amp 63 neural ch 58 rate 0.15 isi 0.0
GG.097 57 count 3 aux amp 5133 neural amp 166 neural ch -1 rate 0.04 isi 0.0
GG.097 59 count 7 aux amp 7004 neural amp 85 neural ch 88 rate 0.07 isi 0.0
GG.097 60 count 6 aux amp 9031 neural amp 106 neural ch 70 rate 0.07 isi 0.0
GG.097 61 count 7 aux amp 9119 neural amp 263 neural ch 76 rate 0.05 isi 0.0
GG.097 62 count 3 aux amp 5735 neural amp 139 neural ch -1 rate 0.03 isi 0.0
GG.097 63 count 3 aux amp 5618 neural amp 482 neural ch -1 rate 0.03 isi 0.0
GG.097 64 count 1 aux amp 7833 neural amp 320 neural ch -1 rate 0.03 isi 0.0
GG.097 65 count 36 aux amp 7614 neural amp 63 neural ch 76 rate 0.44 isi 0.0
[... 10 more lines not kept]
```

**Agent**

Some "units" are clusters of the sensor channels (amplitude 4 to 9 mV on the auxiliary channels, under 200 µV on the probes). Adding that rule.

**Agent calls Bash**

```bash
cd entries/000067-fujisawa-2008; python - <<'E'
s=open('pfc.py').read()
s=s.replace('''    u["region"] = np.where(sh < 0, "unassigned", np.where(sh < N_PFC_CHANNELS // 8, "PFC", "CA1"))''','''    u["region"] = np.where(sh < 0, "unassigned", np.where(sh < N_PFC_CHANNELS // 8, "PFC", "CA1"))
    aux = np.setdiff1d(np.arange(s["sta_amp"].shape[1]), chans)
    u["aux_amp_uv"] = s["sta_amp"][:, aux].max(1) if len(aux) else 0.0
    sensor = (s["sta_amp"].argmax(1) >= 0) & np.isin(s["sta_amp"].argmax(1), aux) & (amp.max(1) < MAX_AUX_NEURAL_UV)
    u.loc[sensor & (count > 0), "region"] = "sensor"''')
s=s.replace('''MAX_ISI_VIOLATION = 0.02''','''MAX_AUX_NEURAL_UV = 200.0     # largest on a sensor channel and below this on the probes: a sensor cluster
MAX_ISI_VIOLATION = 0.02''')
s=s.replace('''    shank by shank). Multi-unit:''','''    shank by shank). A unit whose waveform is largest on a non-neural channel and below
    `MAX_AUX_NEURAL_UV` on every probe channel is a cluster of the sensor signals ("sensor").
    Multi-unit:''')
open('pfc.py','w').write(s)
E
. $TMPDIR/scratch/bin/activate; python - <<'E'
import pickle, sys, numpy as np, pandas as pd
sys.path.insert(0,'.'); import pfc
S=pickle.load(open('/tmp/claude-1001/S.pkl','rb'))
U=pd.concat([pfc.assign_units(s) for s in S if s['has_raw']],ignore_index=True)
print(pd.crosstab([U.session],[U.region,U.mua]))
E
```

```
region    CA1         PFC       sensor       unassigned      
mua     False True  False True   False True       False True 
session                                                      
EE.049     31     4    70     9      0     1          3     0
EE.196     15     4   132     9      1     0          0     0
FF.103     11     4    50    11      0     2          0     0
FF.130      9     4    67    10      0     0          0     0
FF.167      8     2    43    10      1     0          0     0
GG.069     41     7    18     9      0     1          0     0
GG.097     25     4    19     8      9     0          3     1
GG.149     26     4    18     8      6     0          0     1
```

**Agent**

Unit assignment works. Now writing the analysis functions (positions, rate maps, permutation test, jitter connections, position-dependent coupling, first/later spike efficacy, coincidence summation).

**Agent calls Read**

```json
{
 "file_path": "entries/000067-fujisawa-2008/pfc.py",
 "offset": 150,
 "limit": 80
}
```

```
150	
151	def _raw_windows(trials: pd.DataFrame, n_chunks: int, n_windows: int) -> np.ndarray:
152	    """Chunks of the raw series that overlap trials most, spread over the session."""
153	    t0 = np.arange(n_chunks) * RAW_CHUNK / RAW_HZ
154	    t1 = t0 + RAW_CHUNK / RAW_HZ
155	    overlap = np.zeros(n_chunks)
156	    for a, b in zip(trials.nosepoke_start, trials.run_end):
157	        overlap += np.clip(np.minimum(t1, b) - np.maximum(t0, a), 0, None)
158	    candidates = np.flatnonzero(overlap > 0)
159	    if len(candidates) <= n_windows:
160	        return candidates
161	    picks = np.linspace(0, len(candidates) - 1, n_windows).round().astype(int)
162	    return candidates[picks]
163	
164	
165	def load_session(path: str, url: str, n_windows: int = 12) -> dict:
166	    """One working memory session: spikes, trials, position, unit channels and LFP checks."""
167	    s = {"path": path}
168	    with h5py.File(remfile.File(url), "r") as f:
169	        s["session"] = _text(f["general/session_id"])
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000067-fujisawa-2008; python - <<'E'
s=open('pfc.py').read()
s=s.replace('''    acc = np.zeros((len(trains), n_ch, 32))
    count''','''    acc = np.zeros((len(trains), n_ch, 32))
    shifted = np.zeros((len(trains), n_ch, 32))
    count''')
s=s.replace('''            k = st[(st > a + 0.002) & (st < b - 0.002)]
            if len(k) == 0:
                continue
            k = np.round((k[:per_window] - a) * RAW_HZ).astype(int)
            acc[i] += hp[k[:, None] + np.arange(-12, 20)].sum(0).T
            count[i] += len(k)
    mean = acc / np.maximum(count, 1)[:, None, None]''','''            k = st[(st > a + 0.002) & (st < b - 0.006)]
            if len(k) == 0:
                continue
            k = np.round((k[:per_window] - a) * RAW_HZ).astype(int)
            acc[i] += hp[k[:, None] + np.arange(-12, 20)].sum(0).T
            shifted[i] += hp[k[:, None] + SHIFT_SAMPLES + np.arange(-12, 20)].sum(0).T
            count[i] += len(k)
    mean = acc / np.maximum(count, 1)[:, None, None]
    mean_shifted = shifted / np.maximum(count, 1)[:, None, None]''')
s=s.replace('''    return {"sta_amp": mean.max(2) - mean.min(2), "sta_count": count,''','''    return {"sta_amp": mean.max(2) - mean.min(2), "sta_count": count,
            "sta_amp_shifted": mean_shifted.max(2) - mean_shifted.min(2),''')
s=s.replace('''    Theta ratio:''','''    The same amplitude with every spike time moved 3 ms later (`sta_amp_shifted`) is the check
    that the spike times share the clock of the raw signal.
    Theta ratio:''')
s=s.replace('''SPIKE_BAND = (800.0, 5000.0)''','''SPIKE_BAND = (800.0, 5000.0)
SHIFT_SAMPLES = 60              # 3 ms, for the clock check of spike times against the raw signal''')
open('pfc.py','w').write(s)
E
grep -n "SHIFT_SAMPLES\|sta_amp_shifted" pfc.py
```

```
79:SHIFT_SAMPLES = 60              # 3 ms, for the clock check of spike times against the raw signal
207:    The same amplitude with every spike time moved 3 ms later (`sta_amp_shifted`) is the check
231:            shifted[i] += hp[k[:, None] + SHIFT_SAMPLES + np.arange(-12, 20)].sum(0).T
238:            "sta_amp_shifted": mean_shifted.max(2) - mean_shifted.min(2), "theta_ratio": theta,
```

**Agent calls Bash**

```bash
cd entries/000067-fujisawa-2008; cat >> pfc.py <<'E'


# ---------------------------------------------------------------------------------------------
# Behaviour

def frame_times(s: dict) -> np.ndarray:
    return np.arange(len(s["lin"])) / s["lin_rate"]


def positions_at(s: dict, times: np.ndarray):
    """Normalized position (d - 1, 0 at the end of the nose poke, 1 at the reward) and trial index
    of each time; NaN and -1 outside runs (run_start to run_end) or where d is 0 (no position)."""
    tr = s["trials"]
    times = np.asarray(times, float)
    idx = np.searchsorted(tr.run_start.values, times, side="right") - 1
    ok = (idx >= 0) & (times <= tr.run_end.values[np.clip(idx, 0, None)])
    frame = np.clip(np.round(times * s["lin_rate"]).astype(int), 0, len(s["lin"]) - 1)
    d = s["lin"][frame]
    ok &= d > 0
    return np.where(ok, d - 1, np.nan), np.where(ok, idx, -1)


def sensor_check(s: dict, shift_s: float = 0.0) -> pd.DataFrame:
    """Per trial, activity of the right and left nose-poke sensors in the nose-poke period.

    Activity is the mean absolute deviation from the session median of the LFP copy of each
    sensor channel; `shift_s` moves the trial times (the clock check).
    """
    x = s["sensors"]
    dev = np.abs(x - np.median(x, axis=0))
    rows = []
    for k, tr in s["trials"].iterrows():
        a = int((tr.nosepoke_start + shift_s) * s["lfp_rate"])
        b = int((tr.run_start + shift_s) * s["lfp_rate"])
        c = int((tr.run_end + shift_s) * s["lfp_rate"])
        if a < 0 or c > len(x) or b <= a:
            continue
        poke, run = dev[a:b].mean(0), dev[b:c].mean(0)
        rows.append({"trial": k, "side": tr.side, "right_poke": poke[0], "left_poke": poke[1],
                     "right_run": run[0], "left_run": run[1]})
    out = pd.DataFrame(rows)
    out["sensor_side"] = np.where(out.right_poke > out.left_poke, "Right", "Left")
    return out


# ---------------------------------------------------------------------------------------------
# Position-dependent firing

def _gauss(x: np.ndarray, sigma: float = KERNEL_SIGMA) -> np.ndarray:
    """Gaussian kernel of each value (rows) evaluated on GRID (columns)."""
    return np.exp(-0.5 * ((GRID[None, :] - x[:, None]) / sigma) ** 2) / (np.sqrt(2 * np.pi) * sigma)


def trial_densities(pos: np.ndarray, trial: np.ndarray, n_trials: int) -> np.ndarray:
    """(trials, GRID) kernel density of spike positions per trial (unnormalized sums)."""
    out = np.zeros((n_trials, len(GRID)))
    ok = trial >= 0
    if ok.any():
        np.add.at(out, trial[ok], _gauss(pos[ok]))
    return out


def band_test(stats: np.ndarray, alpha: float, two_sided: bool = True):
    """Pointwise and global bands from resampled statistics, as in the paper's Methods.

    `stats` is (1 + M, G): row 0 the original statistic, the others the resampled ones. Returns
    the positions where the original breaks the global band, the original's pointwise P-values,
    and the global level `a` (pointwise level of the global band). The global band is the
    narrowest pointwise band within which at least 1 - alpha of all 1 + M data sets lie
    completely.
    """
    n = stats.shape[0]
    srt = np.sort(stats, axis=0)
    p_up = np.empty_like(stats)
    p_lo = np.empty_like(stats)
    for g in range(stats.shape[1]):
        p_up[:, g] = (n - np.searchsorted(srt[:, g], stats[:, g], side="left")) / n
        p_lo[:, g] = np.searchsorted(srt[:, g], stats[:, g], side="right") / n
    p = np.minimum(1, 2 * np.minimum(p_up, p_lo)) if two_sided else p_up
    m = np.sort(p.min(axis=1))
    allowed = int(np.floor(alpha * n))
    level = 0.0
    for v in np.unique(m):
        if np.sum(m <= v) <= allowed:
            level = v
        else:
            break
    return p[0] <= level, p[0], level


def lr_test(dens: np.ndarray, is_left: np.ndarray, rng, n_perm: int = N_PERM, alpha: float = 0.05):
    """Permutation test of left against right spike-position densities (paper's Methods).

    Returns the positions (GRID) where the difference breaks the global band, and D0(x).
    """
    labels = np.vstack([is_left] + [rng.permutation(is_left) for _ in range(n_perm)]).astype(float)
    nl = labels.sum(1, keepdims=True)
    d = labels @ dens / nl - (1 - labels) @ dens / (len(is_left) - nl)
    sig, _, _ = band_test(d, alpha)
    return sig, d[0]


def rate_maps(s: dict, units: list[int], n_bins: int = 100) -> dict:
    """Occupancy-normalized rate maps (Hz) by side, smoothed with the paper's kernel (sigma 0.05)."""
    from scipy.ndimage import gaussian_filter1d
    t = frame_times(s)
    pos, trial = positions_at(s, t)
    side = s["trials"].side.values
    edges = np.linspace(0, 1, n_bins + 1)
    occ = {}
    for sd in ("Left", "Right"):
        m = (trial >= 0) & (side[np.clip(trial, 0, None)] == sd)
        occ[sd] = gaussian_filter1d(np.histogram(pos[m], edges)[0] / s["lin_rate"], KERNEL_SIGMA * n_bins,
                                    mode="nearest")
    maps = {}
    for u in units:
        p, tr = positions_at(s, s["trains"][u])
        maps[u] = {}
        for sd in ("Left", "Right"):
            m = (tr >= 0) & (side[np.clip(tr, 0, None)] == sd)
            c = gaussian_filter1d(np.histogram(p[m], edges)[0].astype(float), KERNEL_SIGMA * n_bins, mode="nearest")
            maps[u][sd] = c / np.maximum(occ[sd], 1e-9)
    return maps


def field_size(rate: np.ndarray, contiguous: bool = True) -> float:
    """Length (normalized) where the rate is at least half its peak: the contiguous run around the
    peak, or (contiguous=False) all bins."""
    above = rate >= 0.5 * rate.max()
    if not contiguous:
        return float(above.mean())
    k = int(rate.argmax())
    lo, hi = k, k
    while lo > 0 and above[lo - 1]:
        lo -= 1
    while hi < len(rate) - 1 and above[hi + 1]:
        hi += 1
    return (hi - lo + 1) / len(rate)


def active_fraction(s: dict, units: list[int], window: float = 0.1) -> pd.DataFrame:
    """For every 100 ms window inside a run: fraction of `units` firing at least one spike, and
    the window's position (at its centre)."""
    rows = []
    trains = [s["trains"][u] for u in units]
    for k, tr in s["trials"].iterrows():
        edges = np.arange(tr.run_start, tr.run_end - window / 2, window)
        if len(edges) < 2:
            continue
        edges = np.r_[edges, edges[-1] + window]
        active = np.zeros(len(edges) - 1)
        for st in trains:
            active += np.histogram(st, edges)[0] > 0
        pos, _ = positions_at(s, edges[:-1] + window / 2)
        rows.append(pd.DataFrame({"trial": k, "side": tr.side, "pos": pos, "fraction": active / len(units)}))
    return pd.concat(rows, ignore_index=True)


def decode_side(s: dict, units: list[int], offsets: np.ndarray, width: float = 1.0) -> pd.DataFrame:
    """Leave-one-out nearest-centroid decoding of the trial side from spike counts in windows of
    `width` s starting at run_start + offset (z-scored per unit). No random numbers."""
    tr = s["trials"]
    y = (tr.side.values == "Left").astype(int)
    rows = []
    for off in offsets:
        a = tr.run_start.values + off
        X = np.array([[np.searchsorted(s["trains"][u], b + width) - np.searchsorted(s["trains"][u], b)
                       for u in units] for b in a], float)
        sd = X.std(0)
        X = (X[:, sd > 0] - X[:, sd > 0].mean(0)) / sd[sd > 0]
        correct = 0
        for i in range(len(y)):
            keep = np.arange(len(y)) != i
            c0 = X[keep & (y == 0)].mean(0)
            c1 = X[keep & (y == 1)].mean(0)
            pred = int(np.sum((X[i] - c1) ** 2) < np.sum((X[i] - c0) ** 2))
            correct += pred == y[i]
        rows.append({"offset_s": off, "accuracy": correct / len(y), "n_trials": len(y)})
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------------------------
# Monosynaptic interactions

CCG_EDGES_MS = np.arange(-5, 6)          # 10 bins of 1 ms from -5 to 5 ms
TEST_BINS = [6, 7, 8]                    # [1,2), [2,3), [3,4) ms: lags of b after a
TEST_BINS_REVERSE = [3, 2, 1]            # the same lags for the other direction


def near_lags(a: np.ndarray, b: np.ndarray, max_lag: float):
    """All lags b_j - a_i with |lag| <= max_lag, with the indices i and j."""
    lo = np.searchsorted(b, a - max_lag, side="left")
    hi = np.searchsorted(b, a + max_lag, side="right")
    n = hi - lo
    i = np.repeat(np.arange(len(a)), n)
    start = np.repeat(np.cumsum(n) - n, n)
    j = np.arange(n.sum()) - start + np.repeat(lo, n)
    return b[j] - a[i], i, j


def ccg_counts(lags_s: np.ndarray) -> np.ndarray:
    return np.histogram(lags_s * 1000, CCG_EDGES_MS)[0]


def _tri_cdf(x_ms: np.ndarray) -> np.ndarray:
    """CDF of the difference of two independent uniform jitters on [-5, 5] ms."""
    x = np.clip(x_ms, -10, 10)
    return np.where(x <= 0, (x + 10) ** 2 / 200, 1 - (10 - x) ** 2 / 200)


def jitter_expectation(lags_s: np.ndarray) -> np.ndarray:
    """Expected CCG counts when both spike trains are jittered uniformly by +-5 ms (exact mean)."""
    d = lags_s * 1000
    lo, hi = CCG_EDGES_MS[:-1], CCG_EDGES_MS[1:]
    return (_tri_cdf(hi[None, :] - d[:, None]) - _tri_cdf(lo[None, :] - d[:, None])).sum(0)


def jitter_ccgs(lags_s, i, j, rng, n_jitter: int = N_JITTER, chunk: int = 100) -> np.ndarray:
    """CCG counts of `n_jitter` surrogates in which every spike of both trains is jittered
    independently and uniformly by +-5 ms (paper's Methods). Only spike pairs within 15 ms can
    reach the +-5 ms window, so only those are jittered."""
    ui, ii = np.unique(i, return_inverse=True)
    uj, jj = np.unique(j, return_inverse=True)
    out = np.zeros((n_jitter, len(CCG_EDGES_MS) - 1), int)
    for c0 in range(0, n_jitter, chunk):
        c = min(chunk, n_jitter - c0)
        ea = rng.uniform(-JITTER_S, JITTER_S, (c, len(ui)))
        eb = rng.uniform(-JITTER_S, JITTER_S, (c, len(uj)))
        lag = (lags_s[None, :] + eb[:, jj] - ea[:, ii]) * 1000
        k = np.floor(lag - CCG_EDGES_MS[0]).astype(int)
        ok = (k >= 0) & (k < len(CCG_EDGES_MS) - 1)
        rows = np.broadcast_to(np.arange(c)[:, None], lag.shape)
        out[c0:c0 + c] = np.bincount((rows[ok] * (len(CCG_EDGES_MS) - 1) + k[ok]),
                                     minlength=c * (len(CCG_EDGES_MS) - 1)).reshape(c, -1)
    return out


def _direction_result(ccg, upper, lower, test_bins):
    exc_bins = [b for b in test_bins if ccg[b] > upper]
    inh_bins = [b for b in test_bins if ccg[b] < lower]
    width = 0
    if exc_bins:   # width of the run of bins above the global band that holds a test bin
        b = exc_bins[0]
        lo, hi = b, b
        while lo > 0 and ccg[lo - 1] > upper:
            lo -= 1
        while hi < len(ccg) - 1 and ccg[hi + 1] > upper:
            hi += 1
        width = hi - lo + 1
    return bool(exc_bins), width, bool(inh_bins)


def connections(s: dict, units: list[int], rng, screen_p: float = 0.01, check_sample: int = 0) -> pd.DataFrame:
    """Jitter test of every ordered pair of `units` (paper's Methods).

    For each pair the exact jitter mean gives a Poisson screen (any test bin beyond the pointwise
    `screen_p` quantile in either direction); screened pairs get the Monte Carlo test with
    N_JITTER surrogates: global bands at 99% from the maximum and minimum of each surrogate over
    the +-5 ms window, excitatory when a bin from 1 to 4 ms is above the upper band, inhibitory
    when below the lower band. `check_sample` unscreened pairs also get the Monte Carlo test, to
    show that the screen misses nothing.
    """
    from scipy.stats import poisson
    rows = []
    unscreened = []
    for x in range(len(units)):
        for y in range(x + 1, len(units)):
            a, b = s["trains"][units[x]], s["trains"][units[y]]
            lags, i, j = near_lags(a, b, 0.0155)
            ccg = ccg_counts(lags)
            mu = jitter_expectation(lags)
            hi_q = poisson.ppf(1 - screen_p, mu)
            lo_q = poisson.ppf(screen_p, mu)
            cand = bool(np.any(ccg[TEST_BINS] > hi_q[TEST_BINS]) or np.any(ccg[TEST_BINS] < lo_q[TEST_BINS])
                        or np.any(ccg[TEST_BINS_REVERSE] > hi_q[TEST_BINS_REVERSE])
                        or np.any(ccg[TEST_BINS_REVERSE] < lo_q[TEST_BINS_REVERSE]))
            base = {"a": units[x], "b": units[y], "n_near": len(lags), "screened": cand}
            if not cand:
                unscreened.append((x, y))
                rows.append(base)
                continue
            rows.append({**base, **_mc_pair(lags, i, j, ccg, rng)})
    if check_sample and unscreened:
        pick = rng.choice(len(unscreened), min(check_sample, len(unscreened)), replace=False)
        for k in pick:
            x, y = unscreened[k]
            a, b = s["trains"][units[x]], s["trains"][units[y]]
            lags, i, j = near_lags(a, b, 0.0155)
            r = _mc_pair(lags, i, j, ccg_counts(lags), rng)
            rows.append({"a": units[x], "b": units[y], "n_near": len(lags), "screened": False,
                         "check": True, **r})
    out = pd.DataFrame(rows)
    out["check"] = out.get("check", False)
    out["check"] = out["check"].fillna(False).astype(bool)
    return out


def _mc_pair(lags, i, j, ccg, rng) -> dict:
    sur = jitter_ccgs(lags, i, j, rng)
    upper = np.quantile(sur.max(1), 0.99)
    lower = np.quantile(sur.min(1), 0.01)
    ab = _direction_result(ccg, upper, lower, TEST_BINS)
    ba = _direction_result(ccg, upper, lower, TEST_BINS_REVERSE)
    return {"upper": upper, "lower": lower,
            "exc_ab": ab[0], "width_ab": ab[1], "inh_ab": ab[2],
            "exc_ba": ba[0], "width_ba": ba[1], "inh_ba": ba[2]}


def directed(conn: pd.DataFrame, max_width: int = 2) -> pd.DataFrame:
    """One row per ordered pair (pre, post), with exc (narrow peak) and inh (trough) flags."""
    c = conn[~conn.check]
    ab = pd.DataFrame({"pre": c.a, "post": c.b, "exc_any": c.get("exc_ab", False), "width": c.get("width_ab", 0),
                       "inh": c.get("inh_ab", False)})
    ba = pd.DataFrame({"pre": c.b, "post": c.a, "exc_any": c.get("exc_ba", False), "width": c.get("width_ba", 0),
                       "inh": c.get("inh_ba", False)})
    d = pd.concat([ab, ba], ignore_index=True)
    d[["exc_any", "inh"]] = d[["exc_any", "inh"]].fillna(False).astype(bool)
    d["width"] = d.width.fillna(0)
    d["exc"] = d.exc_any & (d.width <= max_width)
    return d


def coincidence_test(s: dict, pre: int, post: int, rng, trials_mask: np.ndarray | None = None,
                     n_jitter: int = N_JITTER, alpha: float = 0.01) -> dict:
    """Position dependence of excess coincidences (post 1 to 4 ms after pre), paper's Methods.

    Coincidence rate along the track: kernel density (sigma 0.05) of the positions of coincident
    events (taken at the presynaptic spike). Surrogates jitter both trains by +-5 ms; the
    positions of the events are kept at the original presynaptic spike (a 5 ms shift moves the rat
    by well under 1% of the track). One-sided global band at `alpha`.
    """
    a, b = s["trains"][pre], s["trains"][post]
    pos, trial = positions_at(s, a)
    keep = trial >= 0
    if trials_mask is not None:
        keep &= trials_mask[np.clip(trial, 0, None)]
    ia = np.flatnonzero(keep)
    lags, i, j = near_lags(a[ia], b, 0.0145)
    events = _gauss(pos[ia][i])                       # (K, G)
    obs = ((lags >= 0.001) & (lags <= 0.004)).astype(float)
    ui, ii = np.unique(i, return_inverse=True)
    uj, jj = np.unique(j, return_inverse=True)
    stats = np.zeros((n_jitter + 1, len(GRID)))
    stats[0] = obs @ events
    for c0 in range(0, n_jitter, 100):
        c = min(100, n_jitter - c0)
        ea = rng.uniform(-JITTER_S, JITTER_S, (c, len(ui)))
        eb = rng.uniform(-JITTER_S, JITTER_S, (c, len(uj)))
        lag = lags[None, :] + eb[:, jj] - ea[:, ii]
        stats[1 + c0:1 + c0 + c] = ((lag >= 0.001) & (lag <= 0.004)).astype(float) @ events
    sig, p, level = band_test(stats, alpha, two_sided=False)
    return {"n_coincidences": int(obs.sum()), "sig_fraction": float(sig.mean()), "any_sig": bool(sig.any()),
            "level": level}


def transmission(a: np.ndarray, b: np.ndarray, which: np.ndarray) -> np.ndarray:
    """Per presynaptic spike in `which`: post spikes 1 to 4 ms after it, minus the expectation
    when the post spikes are jittered uniformly by +-5 ms. The mean over a set of spikes is the
    excess transmission per presynaptic spike."""
    lags, i, j = near_lags(a[which], b, 0.0095)
    d = lags * 1000
    obs = ((d >= 1) & (d <= 4)).astype(float)
    exp = (np.clip(np.minimum(d + 5, 4) - np.maximum(d - 5, 1), 0, None)) / 10
    out = np.zeros(len(which))
    np.add.at(out, i, obs - exp)
    return out


def first_vs_later(a: np.ndarray, b: np.ndarray, rng, n_perm: int = 1000) -> dict:
    """Excess transmission of first spikes (after >= 200 ms of silence) against later spikes
    (< 40 ms after the previous spike), with a permutation test of the labels (two-sided)."""
    isi = np.diff(a, prepend=-np.inf)
    first = np.flatnonzero(isi >= 0.2)
    later = np.flatnonzero(isi < 0.04)
    if len(first) == 0 or len(later) == 0:
        return {"n_first": len(first), "n_later": len(later)}
    v = transmission(a, b, np.r_[first, later])
    lab = np.r_[np.ones(len(first), bool), np.zeros(len(later), bool)]
    diff0 = v[lab].mean() - v[~lab].mean()
    null = np.empty(n_perm)
    for k in range(n_perm):
        p = rng.permutation(lab)
        null[k] = v[p].mean() - v[~p].mean()
    p_two = min(1.0, 2 * min((np.sum(null >= diff0) + 1) / (n_perm + 1), (np.sum(null <= diff0) + 1) / (n_perm + 1)))
    return {"n_first": len(first), "n_later": len(later), "eff_first": v[lab].mean(),
            "eff_later": v[~lab].mean(), "diff": diff0, "p": p_two}


def coincidence_gain(pres: list[np.ndarray], post: np.ndarray, duration: float, window: float = 0.005) -> pd.DataFrame:
    """Transmission by the number of distinct presynaptic partners firing together.

    Spikes of all partners are merged; an event starts at a spike and takes every partner spike
    within `window` after it (events do not overlap). For each event, whether the post unit fires
    1 to 4 ms after the event's last spike. Excess = that probability minus the chance of a post
    spike in any 3 ms window (rate x 3 ms, Poisson).
    """
    t = np.concatenate(pres)
    who = np.concatenate([np.full(len(p), k) for k, p in enumerate(pres)])
    o = np.argsort(t, kind="stable")
    t, who = t[o], who[o]
    rows = []
    k = 0
    n = len(t)
    while k < n:
        e = np.searchsorted(t, t[k] + window, side="right")
        rows.append((t[e - 1], len(np.unique(who[k:e]))))
        k = e
    ev = np.array(rows)
    last, n_part = ev[:, 0], ev[:, 1].astype(int)
    hit = (np.searchsorted(post, last + 0.004, side="right") - np.searchsorted(post, last + 0.001, side="left")) > 0
    p0 = 1 - np.exp(-len(post) / duration * 0.003)
    out = pd.DataFrame({"n_partners": n_part, "hit": hit})
    g = out.groupby("n_partners").hit.agg(["mean", "size"]).rename(columns={"mean": "p_hit", "size": "events"})
    g["excess"] = g.p_hit - p0
    return g.reset_index()
E
python -c "import ast;ast.parse(open('pfc.py').read())"
```

```
(Bash completed with no output)
```

**Agent**

Quick synthetic tests of the jitter and band functions.

**Agent calls Bash**

```bash
cd entries/000067-fujisawa-2008; . $TMPDIR/scratch/bin/activate; python - <<'E'
import sys, numpy as np, time
sys.path.insert(0,'.'); import pfc
rng=np.random.default_rng(0)
T=2000
a=np.sort(rng.uniform(0,T,4000)); b0=np.sort(rng.uniform(0,T,20000))
# coupled: 15% of a spikes evoke b spike at +2ms
ev=a[rng.random(len(a))<0.15]+0.002+rng.normal(0,0.0003,size=None or 1)[0]*0
b=np.sort(np.r_[b0,ev+rng.uniform(-0.0003,0.0003,len(ev))])
s={'trains':[a,b,np.sort(rng.uniform(0,T,5000))]}
lags,i,j=pfc.near_lags(a,b,0.0155)
print('ccg',pfc.ccg_counts(lags)); print('exp',np.round(pfc.jitter_expectation(lags),1))
sur=pfc.jitter_ccgs(lags,i,j,rng); print('mc mean',np.round(sur.mean(0),1))
t=time.time(); c=pfc.connections(s,[0,1,2],rng,check_sample=2); print(time.time()-t); print(c.T)
print(pfc.directed(c))
# band test: null data
st=rng.normal(size=(1001,101)); sig,p,l=pfc.band_test(st,0.05); print('null any sig',sig.any(),'level',l)
fp=np.mean([pfc.band_test(rng.normal(size=(1001,50)).cumsum(1),0.05)[0].any() for _ in range(100)]); print('FWER on smooth null',fp)
E
```

```
ccg [ 42  33  33  41  42  40 348 353  36  34]
exp [61.6 67.5 73.5 79.5 85.5 91.4 97.4 97.3 91.2 85.1]
mc mean [61.6 67.5 73.8 79.6 85.  91.6 97.1 97.4 90.9 85. ]
0.13218450546264648
              0      1      2      3      4
a             0      0      1      0      1
b             1      2      2      2      2
n_near     1868    315   1621    315   1621
screened   True  False  False  False  False
upper     124.0    NaN    NaN  21.01   76.0
lower     44.99    NaN    NaN    2.0   31.0
exc_ab     True    NaN    NaN  False  False
width_ab    2.0    NaN    NaN    0.0    0.0
inh_ab     True    NaN    NaN  False  False
exc_ba    False    NaN    NaN  False  False
width_ba    0.0    NaN    NaN    0.0    0.0
inh_ba     True    NaN    NaN  False  False
check     False  False  False   True   True
   pre  post  exc_any  width    inh    exc
0    0     1     True    2.0   True   True
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000067-fujisawa-2008; . $TMPDIR/scratch/bin/activate; python - <<'E'
import sys, numpy as np
sys.path.insert(0,'.'); import pfc
rng=np.random.default_rng(1)
res=[]
for _ in range(200):
    st=rng.normal(size=(1001,50)).cumsum(1)
    sig,p,l=pfc.band_test(st,0.05)
    res.append((sig.any(),l))
r=np.array(res); print(r[:,0].mean(), np.unique(r[:,1])[:5])
# exchangeability check: fraction of rows that would be significant
st=rng.normal(size=(1001,50)).cumsum(1)
n=st.shape[0]; srt=np.sort(st,0)
pu=np.array([(n-np.searchsorted(srt[:,g],st[:,g],'left'))/n for g in range(50)]).T
pl=np.array([np.searchsorted(srt[:,g],st[:,g],'right')/n for g in range(50)]).T
p=np.minimum(1,2*np.minimum(pu,pl)); m=p.min(1); _,_,l=pfc.band_test(st,0.05)
print('level',l,'frac rows m<=level',np.mean(m<=l))
E
```

```
0.035 [0.001998   0.003996   0.00599401]
level 0.003996003996003996 frac rows m<=level 0.04195804195804196
```

**Agent calls Bash**

```bash
cd entries/000067-fujisawa-2008; . $TMPDIR/scratch/bin/activate; python - <<'E'
import sys, numpy as np
sys.path.insert(0,'.'); import pfc
for seed in (0,5):
    rng=np.random.default_rng(seed)
    print(seed, np.mean([pfc.band_test(rng.normal(size=(1001,50)).cumsum(1),0.05)[0].any() for _ in range(500)]))
E
```

```
0 0.036
5 0.056
```

**Agent**

The band test controls the family-wise rate near 5%. Now timing the connection analysis on real sessions.

**Agent calls Bash**

```bash
cd entries/000067-fujisawa-2008; sed -i 's/    d\["exc"\] = d.exc_any \& (d.width <= max_width)/    d["exc"] = d.exc_any \& (d.width <= max_width)\n    d["inh"] = d.inh \& ~d.exc_any      # a trough beside a peak is not counted as inhibition/' pfc.py; . $TMPDIR/scratch/bin/activate; python - <<'E'
import pickle, sys, numpy as np, pandas as pd, time
sys.path.insert(0,'.'); import pfc
S=pickle.load(open('/tmp/claude-1001/S.pkl','rb'))
for s in S:
    if not s['has_raw']: continue
    u=pfc.assign_units(s); units=u[(u.region=='PFC')&~u.mua].unit.tolist()
    t=time.time(); rng=np.random.default_rng(0)
    c=pfc.connections(s,units,rng,check_sample=100)
    d=pfc.directed(c)
    chk=c[c.check]
    print(s['session'],len(units),'pairs',len(d),'screened',int(c[~c.check].screened.sum()),'exc',int(d.exc.sum()),'exc_any',int(d.exc_any.sum()),'inh',int(d.inh.sum()),'check sig',int((chk[['exc_ab','exc_ba','inh_ab','inh_ba']].fillna(False).astype(bool)).any(axis=1).sum()),'time',round(time.time()-t,1))
    pickle.dump(c,open(f"/tmp/claude-1001/conn_{s['session']}.pkl",'wb'))
E
```

```
EE.049 70 pairs 4830 screened 86 exc 32 exc_any 32 inh 3 check sig 0 time 2.9
EE.196 132 pairs 17292 screened 430 exc 160 exc_any 166 inh 44 check sig 0 time 33.9
FF.103 50 pairs 2450 screened 81 exc 24 exc_any 24 inh 3 check sig 0 time 3.9
FF.130 67 pairs 4422 screened 160 exc 51 exc_any 57 inh 17 check sig 0 time 8.7
FF.167 43 pairs 1806 screened 81 exc 16 exc_any 16 inh 6 check sig 0 time 3.5
GG.069 18 pairs 306 screened 12 exc 6 exc_any 6 inh 0 check sig 0 time 0.5
GG.097 19 pairs 342 screened 4 exc 2 exc_any 2 inh 0 check sig 0 time 0.3
GG.149 18 pairs 306 screened 3 exc 2 exc_any 2 inh 0 check sig 0 time 0.4
```

**Agent calls Bash**

```bash
cd  cat schemas/claims.schema.json | python -c "import json,sys;d=json.load(sys.stdin);print(json.dumps(d,indent=1)[:5000])"
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
[... 120 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/000067/doi-10.1038-nn.2134.yaml",
 "content": "# Claims for Fujisawa, Amarasingham, Harrison & Buzsaki (2008) on dandiset 000067.\n# Source: the author manuscript in PubMed Central (PMC2562676), full text of the Results,\n# figure legends and Methods. The supplementary information (which defines some measures, for\n# example the rate-normalized peak height of Figure 6 and the satellites of Figure 7) could not\n# be retrieved: PubMed Central and the publisher answered with a reCAPTCHA page.\n#\n# What had been seen when these criteria were written: the file list and metadata of every\n# file; the contents of the units, trials, position and electrode tables; spikes per unit and\n# firing rates; the shank and region of each unit from its mean wideband waveform; the\n# refractory violations used to flag multi-unit clusters; the nose-poke sensor channels; the\n# theta ratio of every channel. In addition, a timing run of the jitter test for monosynaptic\n# connections printed, per session, the number of PFC single units, of ordered pairs, and of\n# excitatory and inhibitory connections (293 and 73 of 31754 ordered pairs in total). That run\n# came before the criteria of fig3-connection-rates, fig3-cell-classes and fig3f-distance were\n# written; no method choice of those claims was changed after it. No other claim's analysis had\n# been run.\n#\n# Fixed for every claim that uses units. Sessions: the eight working memory sessions that have\n# a trial table and the wideband signal (EE.049, EE.196, FF.103, FF.130, FF.167, GG.069,\n# GG.097, GG.149). EE.088 has no wideband signal, so its units cannot be placed on a probe, and\n# is used only for checks of the trial table. PFC single units: units whose mean wideband\n# waveform (800 to 5000 Hz) is largest on one of the 64 channels of the prefrontal probe, with\n# at most 2% of inter-spike intervals shorter than 2 ms. Units are not matched across sessions;\n# each session's units are counted as distinct, and results are also given per session. The\n# trial runs from the end of the last nose poke (the file's stop_time) to the start of reward\n# consumption (reward_time), positions 0 to 1 (the file's linearized position minus 1).\n#\n# Layers: the paper recorded layer 2/3 in three rats and layer 5 in one. Neither the dandiset\n# nor the CRCNS description says which rat is which, so claims with values by layer allow\n# each of the three rats here to be either layer, with at most one rat in layer 5, and are\n# judged rat by rat.\nschema_version: 1\ndandiset: \"000067\"\npaper: doi:10.1038/nn.2134\nclaims:\n- id: channel-region-link\n  statement: The dandiset's recording channels can be assigned to the prefrontal probe, the CA1\n    probe and the nose-poke sensors by the channel map of the CRCNS pfc-2 description of the\n    same recordings (channels 1 to 64 prefrontal, 65 to 96 CA1, 97 right and 98 left nose-poke\n    sensors), and the data agree with that map.\n  source: Methods (8-shank, 64-site probe in mPFC); CRCNS pfc-2 data description, version 0.7\n  data: with_labels\n  criterion: Two checks in each of the eight sessions with the wideband signal, and the sensor\n    check also in EE.088. (i) The median theta ratio (6 to 10 Hz over 1 to 40 Hz power, during\n    trials) of the CA1 channels is above that of channels 1 to 64. (ii) In at least 90% of\n    trials the sensor channel with more activity during the nose poke is the one of the trial's\n    side. Reproduced when both hold in every session with the CRCNS channel numbers; partially\n    reproduced when both hold in every session only with a per-rat correction of the channel\n    numbers found in the data; not reproduced otherwise.\n- id: rats-and-units\n  statement: 633 well-isolated units were recorded from the mPFC of four rats.\n  source: Results, first paragraph\n  data: with_labels\n  depends_on:\n  - channel-region-link\n  expected:\n  - quantity: rats\n    value: 4\n    tolerance: 0\n  - quantity: well-isolated mPFC units\n    value: 633\n    tolerance: 63.3\n  criterion: Readings of the unit count, all over the eight sessions; (a) PFC single units; (b)\n    PFC single units with a peak rate of at least 1 Hz during runs; (c) all units placed on the\n    prefrontal probe, multi-unit clusters included. Reproduced when the dandiset holds four\n    rats and one reading is within tolerance; partially reproduced when only one of the two\n    holds; not reproduced when neither does.\n- id: task-performance\n  statement: Rats performed the odor-place matching task at 92% correct (91.9% in the recording\n    sessions).\n  source: Results, second section; Methods, Behavioral task\n  expected:\n    quantity: correct trials\n    value: 91.9\n    tolerance: 9.19\n    unit: percent\n- id: fig2c-active-fraction\n  statement: About 10% (layer 2/3) and 20% (layer 5) of the recorded neurons fire at least one\n    spike in any 100 ms window, a fraction that is relatively constant along the maze.\n  source: Results, first section; Figure 2c; Discussion\n  data: with_labels\n  depends_on:\n  - channel-region-link\n  criterion: Per session, the mean over the 100 ms windows tiling each run of the fraction of\n    PFC single units with at least one spike, and the same mean in ten position bins of 0.1.\n    Per rat, the median over its sessions. Reproduced when each rat's value is within 10% of\n    10% (9 to 11%) or of 20% (18 to 22%), at most one rat at 20%, and in every session the\n    largest of the ten position-bin means is at most twice the smallest (the threshold for\n    \"relatively constant\" is chosen here). Partially reproduced when one of the two parts holds.\n- id: fig2-field-size\n  statement: Neurons are active over similar standardized distances of the maze, 0.27 (62 cm)\n    plus or minus 0.17 (39 cm) (mean and s.d.), from the 50% boundaries of the peak firing rate.\n  source: Results, first section; Figure 2a\n  data: with_labels\n  depends_on:\n  - channel-region-link\n  expected:\n  - quantity: mean field size\n    value: 0.27\n    tolerance: 0.17\n    unit: normalized length\n  - quantity: s.d. of field size\n    value: 0.17\n    tolerance: 0.017\n    unit: normalized length\n  criterion: Occupancy-normalized rate maps on 100 bins of the normalized track, by side,\n    smoothed with the paper's Gaussian kernel (sigma 0.05). Units are PFC single units with a\n    peak rate of at least 1 Hz on either side (the \"Cells\" rule of the CRCNS description; the\n    paper states none). The tolerance of the mean is the paper's stated spread, as the protocol\n    asks; the s.d. takes 10%. Readings; (a) the contiguous run of bins at or above half the peak\n    around the peak, on the side with the higher peak; (b) the same on each side, each side a\n    separate value; (c) all bins at or above half the peak on the side with the higher peak.\n    Reproduced when, under one reading, both values are within tolerance; partially reproduced\n    when only the mean is.\n- id: fig2b-trajectory-selective\n  statement: The fraction of neurons with significantly different firing on left and right\n    trials is 16% (layer 2/3) and 18% (layer 5) in the central arm (positions 0 to 0.3), where\n    the trajectories overlap, and 22% (layer 2/3) and 40% (layer 5) in the side arms (0.5 to\n    1).\n  source: Results, first section; Figure 2b; Methods, permutation tests and global bands\n  data: with_labels\n  depends_on:\n  - channel-region-link\n  criterion: The Methods' test; per-trial kernel densities of spike positions (sigma 0.05) on\n    101 points of the track, difference of left and right means, 1000 permutations of the trial\n    labels, global band at alpha 0.05. A unit is selective in a segment when the difference\n    breaks the global band anywhere in it. Units as in fig2-field-size. The chance rate is the\n    same procedure on one random relabelling of each unit's trials. Per rat, reproduced when the\n    central-arm fraction is within 14.4 to 19.8% (the range 16 to 18% widened by 10% of each\n    bound) and the side-arm fraction is within 10% of the value of one layer (19.8 to 24.2% for\n    layer 2/3, 36 to 44% for layer 5), with at most one rat in layer 5. The claim is reproduced\n    when every rat is; partially reproduced when the pooled central-arm fraction is above the\n    chance fraction (one-sided Fisher exact test, p < 0.05) but not every rat matches; not\n    reproduced otherwise.\n- id: traj-diverge\n  statement: Left and right trajectories overlap in the central arm and begin to differ\n    significantly at position 0.3.\n  source: Results, first section; Supplementary Figure 3\n- id: odor-nosepoke\n  statement: About one quarter of the neurons fire at significantly different rates (P < 0.05\n    per cell) during nose poking for the two odors.\n  source: Results, first section; Supplementary Figure 6\n  data: with_labels\n  depends_on:\n  - channel-region-link\n  expected:\n    quantity: fraction of neurons with odor-dependent rates\n    value: 25\n    tolerance: 5\n    unit: percent\n  criterion: The trial table holds correct trials only, so the odor is given by the side\n    (chocolate for one side, cheese for the other). Per PFC single unit with at least 10 spikes\n    in nose-poke periods, its rate in each trial from the start of the first nose poke to the\n    end of the last; left against right trials by a two-sided Mann-Whitney test at P < 0.05 (the\n    paper names no test). The tolerance is wider than 10% because the paper says\n    \"approximately\". Reproduced when the pooled fraction is within tolerance; partially\n    reproduced when it is outside but above the chance fraction from one random relabelling of\n    each unit's trials (one-sided Fisher exact test, p < 0.05); not reproduced otherwise.\n- id: fig3-connection-rates\n  statement: Of all ordered pairs of simultaneously recorded neurons, 0.79% had short-latency,\n    narrow peaks or troughs in their cross-correlograms (0.55% excitatory, 0.24% inhibitory),\n    found with a jitter test.\n  source: Results, second section; Figure 3a and 3e; Methods, identifying monosynaptic\n    interactions\n  data: with_labels\n  depends_on:\n  - channel-region-link\n  expected:\n  - quantity: ordered pairs with a connection\n    value: 0.79\n    tolerance: 0.079\n    unit: percent\n  - quantity: excitatory\n    value: 0.55\n    tolerance: 0.055\n    unit: percent\n  - quantity: inhibitory\n    value: 0.24\n    tolerance: 0.024\n    unit: percent\n  criterion: Every ordered pair of PFC single units in a session, whole session. Cross-\n    correlogram in 1 ms bins from -5 to 5 ms (the bin width is chosen here); 1000 surrogates\n    with every spike jittered uniformly by +-5 ms; global bands at 99% from the maximum and\n    minimum of each surrogate over the window. Excitatory when a bin from 1 to 4 ms is above the\n    upper band and the run of bins above it is at most 2 ms wide; inhibitory when a bin from 1\n    to 4 ms is below the lower band and the pair is not excitatory in that direction. To save\n    time, pairs whose correlogram is within the pointwise 1% Poisson quantiles of the exact\n    jitter mean in every test bin are not given the Monte Carlo test; a random sample of them\n    is, to show the screen misses nothing. Reproduced when all three rates are within\n    tolerance; partially reproduced when one or two are; not reproduced otherwise.\n- id: fig3-cell-classes\n  statement: By their connections, 32.5% of units are putative pyramidal cells and 12.5%\n    putative interneurons, a ratio of 2.82 plus or minus 0.51 (s.d.), and 50.7% of the\n    postsynaptic targets of putative excitatory cells themselves inhibit other neurons.\n  source: Results, second section\n  data: with_labels\n  depends_on:\n  - fig3-connection-rates\n  expected:\n  - quantity: putative pyramidal cells\n    value: 32.5\n    tolerance: 3.25\n    unit: percent\n  - quantity: putative interneurons\n    value: 12.5\n    tolerance: 1.25\n    unit: percent\n  - quantity: pyramidal to interneuron ratio\n    value: 2.82\n    tolerance: 0.51\n  - quantity: targets of excitatory cells that are interneurons\n    value: 50.7\n    tolerance: 5.07\n    unit: percent\n  criterion: A unit is a putative pyramidal cell when it has at least one excitatory outgoing\n    connection, a putative interneuron when it has at least one inhibitory one; a unit with both\n    is counted in neither. Fractions over all PFC single units. The ratio's tolerance is the\n    paper's s.d. Readings of the ratio; (a) the mean of per-session ratios (sessions with at\n    least one interneuron); (b) the pooled ratio; (c) the mean of per-rat pooled ratios. Targets;\n    distinct postsynaptic units of excitatory connections that are putative interneurons.\n    Reproduced when all four values are within tolerance under one reading; partially\n    reproduced when two or three are; not reproduced otherwise.\n- id: fig3f-distance\n  statement: Most connected pairs were recorded on the same shank, and the probability of a\n    connection falls with the distance between the neurons, though connections were found up to\n    1200 micrometres apart.\n  source: Results, second section; Figure 3f\n  data: with_labels\n  depends_on:\n  - fig3-connection-rates\n  criterion: Distance between two units taken as 200 micrometres times the number of shanks\n    between them (the probe's shank spacing; positions within a shank are not used). Reproduced\n    when the connection probability (excitatory or inhibitory, ordered pairs) is higher on the\n    same shank than across shanks (two-sided Fisher exact test, p < 0.05), the Spearman\n    correlation of probability with shank distance over distances 0 to 1400 micrometres is\n    negative with p < 0.05, and some connection is at least 1000 micrometres apart; partially\n    reproduced when the first two hold.\n- id: fig4-position-dependence\n  statement: Out of 343 excitatory monosynaptic pairs, 67 showed position dependence of their\n    short-latency coincidences in the maze (P < 0.01), beyond what the firing rates explain.\n  source: Results, third section; Figure 4; Methods, identifying position dependence\n  data: with_labels\n  depends_on:\n  - fig3-connection-rates\n  expected:\n    quantity: excitatory pairs with position-dependent coincidences\n    value: 19.5\n    tolerance: 1.95\n    unit: percent\n  criterion: For each excitatory pair, coincident events (postsynaptic spike 1 to 4 ms after a\n    presynaptic spike) during runs, located at the presynaptic spike; kernel density (sigma\n    0.05) on 101 points; 1000 surrogates with both trains jittered by +-5 ms; one-sided global\n    band at 0.01. Readings; (a) left and right trials together, significant excess anywhere on\n    the track; (b) left and right trials tested separately, significant in either. Reproduced\n    when the fraction is within tolerance under one reading; not reproduced otherwise. The\n    fraction of the track that is significant is reported for every pair.\n- id: fig6-facilitation-depression\n  statement: About equal fractions of connected pairs show firing pattern-dependent depression\n    (12.7%) and facilitation (10.7%), comparing the transmission of the first spike of a train\n    with that of later spikes.\n  source: Results, fourth section; Figure 6c\n  data: with_labels\n  depends_on:\n  - fig3-connection-rates\n  expected:\n  - quantity: depressing pairs\n    value: 12.7\n    tolerance: 1.27\n    unit: percent\n  - quantity: facilitating pairs\n    value: 10.7\n    tolerance: 1.07\n    unit: percent\n  criterion: Excitatory pairs with at least 20 first spikes (after at least 200 ms of\n    presynaptic silence) and 20 later spikes (less than 40 ms after the previous presynaptic\n    spike). Transmission of a set of presynaptic spikes is the mean number of postsynaptic\n    spikes 1 to 4 ms after each, minus its expectation under +-5 ms jitter of the postsynaptic\n    spikes (chosen here, as the supplementary definition was not available). 1000 permutations\n    of the first and later labels, two-sided P < 0.10; depressing when first spikes transmit\n    more, facilitating when later spikes do. Reproduced when both fractions are within\n    tolerance; partially reproduced when both are above the 5% that the test gives each side\n    under its null (one-sided binomial test, p < 0.05) but not both within tolerance; not\n    reproduced otherwise.\n- id: fig7-supralinear\n  statement: Coincident firing of two or more presynaptic neurons within 5 ms on a common target\n    is more effective than the sum of their separate effects (supralinear), while spikes spread\n    over windows longer than 10 ms add linearly.\n  source: Results, fourth section; Figure 7\n  data: with_labels\n  depends_on:\n  - fig3-connection-rates\n  criterion: Satellites are PFC single units with at least two excitatory presynaptic partners.\n    Partner spikes are merged into events (a spike and every partner spike within 5 ms after\n    it); for each event, whether the target fires 1 to 4 ms after its last spike, minus the\n    chance of a target spike in any 3 ms window. Supralinear in a satellite when the excess for\n    events with two partners exceeds twice that for events with one. Satellites with at least\n    20 two-partner events are tested. Reproduced when more than half of them are supralinear and\n    a one-sided Wilcoxon signed-rank test of the difference gives p < 0.05; partially\n    reproduced when more than half are but p is 0.05 or more; not reproduced otherwise. The same\n    with 20 ms events is shown as a variant for the linear part.\n- id: fig3-trajectory-by-class\n  statement: Large fractions of putative pyramidal cells (72.2% in layer 2/3, 84.7% in layer 5)\n    and of interneurons (58.3% and 83%) are trajectory specific.\n  source: Results, second section\n  data: with_labels\n  depends_on:\n  - fig3-cell-classes\n  - fig2b-trajectory-selective\n  criterion: A unit is trajectory specific when the test of fig2b-trajectory-selective finds a\n    significant left-right difference anywhere on the track (units of any peak rate). Per rat,\n    the fractions of its putative pyramidal cells and interneurons. Reproduced when every rat\n    matches one layer's two values within 10% of each, at most one rat in layer 5; partially\n    reproduced when in every rat both fractions are above the chance fraction of\n    fig2b-trajectory-selective; not reproduced otherwise.\n- id: ee188-example-session\n  statement: In the example layer 2/3 session, 117 neurons gave 1172 pairs with 48 excitatory\n    and 30 inhibitory connections, 39 of the 117 cells formed one connected hub, 15 of 36\n    excitatory connections were active in particular maze segments, and the example pairs\n    (156-136, 197-201, 49-52, 186-201, 197 and 186 onto one interneuron, a satellite on cell\n    135) show position-dependent, depressing, facilitating and supralinear transmission.\n  source: Figures 2a, 3b to 3d, 4, 5, 6b and 7a\n"
}
```

```
File created successfully at: claims/000067/doi-10.1038-nn.2134.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  grep -n ": .*: " claims/000067/doi-10.1038-nn.2134.yaml | grep -v "^ *#"; python -c "
import yaml,json,jsonschema;d=yaml.safe_load(open('claims/000067/doi-10.1038-nn.2134.yaml'));jsonschema.validate(d,json.load(open('schemas/claims.schema.json')));print(len(d['claims']),'claims ok')"
```

```
16 claims ok
```

**Agent**

Claims are written and validate. Now developing each claim's analysis on the cached data.

**Agent calls Bash**

```bash
cd entries/000067-fujisawa-2008; . $TMPDIR/scratch/bin/activate; cat > $TMPDIR/an1.py <<'E'
import pickle, sys, numpy as np, pandas as pd, time
from scipy import stats
sys.path.insert(0,'.'); import pfc
pd.set_option('display.width',250)
S=pickle.load(open('/tmp/claude-1001/S.pkl','rb'))
S=[s for s in S if s['has_raw']]
U={s['session']:pfc.assign_units(s) for s in S}
single={k:u[(u.region=='PFC')&~u.mua].unit.tolist() for k,u in U.items()}
# active fraction
t=time.time()
rows=[]
for s in S:
    af=pfc.active_fraction(s,single[s['session']])
    b=pd.cut(af.pos,np.linspace(0,1,11),include_lowest=True)
    bm=af.groupby(b,observed=True).fraction.mean()
    rows.append({'session':s['session'],'rat':s['subject'],'n_units':len(single[s['session']]),'windows':len(af),'mean':af.fraction.mean()*100,'bin_min':bm.min()*100,'bin_max':bm.max()*100,'ratio':bm.max()/bm.min()})
print(pd.DataFrame(rows).round(2)); print('t',time.time()-t)
# field size
t=time.time(); rows=[]
for s in S:
    m=pfc.rate_maps(s,single[s['session']])
    for u,mm in m.items():
        pk={sd:mm[sd].max() for sd in mm}
        if max(pk.values())<1: continue
        pref=max(pk,key=pk.get)
        rows.append({'session':s['session'],'rat':s['subject'],'unit':u,'a':pfc.field_size(mm[pref]),'c':pfc.field_size(mm[pref],False),'bL':pfc.field_size(mm['Left']),'bR':pfc.field_size(mm['Right'])})
F=pd.DataFrame(rows); print(len(F)); print(F[['a','c']].agg(['mean','std']).round(3)); b=np.r_[F.bL,F.bR]; print('b',b.mean().round(3),b.std(ddof=1).round(3)); print(F.groupby('rat')[['a','c']].agg(['mean','std']).round(3)); print('t',time.time()-t)
E
python $TMPDIR/an1.py
```

```
session rat  n_units  windows   mean  bin_min  bin_max  ratio
0  EE.049  EE       70     2346   9.67     8.45    11.12   1.32
1  EE.196  EE      132     2315  10.73     7.37    13.43   1.82
2  FF.103  FF       50     2655  14.25    12.94    15.05   1.16
3  FF.130  FF       67     2955  20.73    18.90    22.74   1.20
4  FF.167  FF       43     2650  19.68    17.87    21.75   1.22
5  GG.069  GG       18     3781   7.61     5.88     9.81   1.67
6  GG.097  GG       19     2302   5.75     4.38     8.24   1.88
7  GG.149  GG       18     1851   6.16     3.62     9.28   2.57
t 1.3373513221740723
346
          a      c
mean  0.270  0.331
std   0.196  0.220
b 0.281 0.206
         a             c       
      mean    std   mean    std
rat                            
EE   0.221  0.163  0.277  0.200
FF   0.322  0.223  0.392  0.233
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000067-fujisawa-2008; . $TMPDIR/scratch/bin/activate; cat > $TMPDIR/an2.py <<'E'
import pickle, sys, numpy as np, pandas as pd, time
from scipy import stats
sys.path.insert(0,'.'); import pfc
pd.set_option('display.width',250)
S=pickle.load(open('/tmp/claude-1001/S.pkl','rb'))
S=[s for s in S if s['has_raw']]
U={s['session']:pfc.assign_units(s) for s in S}
single={k:u[(u.region=='PFC')&~u.mua].unit.tolist() for k,u in U.items()}
t=time.time(); rows=[]
for si,s in enumerate(S):
    rng=np.random.default_rng([2, si])
    m=pfc.rate_maps(s,single[s['session']])
    isl=(s['trials'].side=='Left').values
    for u in single[s['session']]:
        pos,tr=pfc.positions_at(s,s['trains'][u])
        dens=pfc.trial_densities(pos,tr,len(isl))
        sig,_=pfc.lr_test(dens,isl,rng)
        sh=rng.permutation(isl)
        sig0,_=pfc.lr_test(dens,sh,rng)
        peak=max(m[u]['Left'].max(),m[u]['Right'].max())
        rows.append({'session':s['session'],'rat':s['subject'],'unit':u,'peak':peak,
          'central':sig[pfc.GRID<=0.3].any(),'side':sig[pfc.GRID>=0.5].any(),'any':sig.any(),
          'central0':sig0[pfc.GRID<=0.3].any(),'side0':sig0[pfc.GRID>=0.5].any(),'any0':sig0.any()})
T=pd.DataFrame(rows); print('t',time.time()-t)
A=T[T.peak>=1]
print(A.groupby('rat')[['central','side','any','central0','side0','any0']].mean().round(3)*100, A.groupby('rat').size())
print('pooled',A[['central','side','any','central0','side0','any0']].mean().round(3)*100)
print('all units',T.groupby('rat')[['central','side']].mean().round(3)*100)
T.to_pickle('/tmp/claude-1001/T.pkl')
# odor
rows=[]
for si,s in enumerate(S):
    rng=np.random.default_rng([3, si])
    tr=s['trials']; dur=(tr.run_start-tr.nosepoke_start).values; isl=(tr.side=='Left').values
    for u in single[s['session']]:
        st=s['trains'][u]
        c=np.searchsorted(st,tr.run_start.values)-np.searchsorted(st,tr.nosepoke_start.values)
        if c.sum()<10: continue
        r=c/dur
        p=stats.mannwhitneyu(r[isl],r[~isl]).pvalue
        sh=rng.permutation(isl); p0=stats.mannwhitneyu(r[sh],r[~sh]).pvalue
        rows.append({'session':s['session'],'rat':s['subject'],'p':p,'p0':p0})
O=pd.DataFrame(rows); print('odor n',len(O),'frac',(O.p<0.05).mean(),'chance',(O.p0<0.05).mean()); print(O.groupby('rat').apply(lambda d: pd.Series({'n':len(d),'f':(d.p<0.05).mean(),'f0':(d.p0<0.05).mean()})))
print('nosepoke dur', pd.concat([ (s['trials'].run_start-s['trials'].nosepoke_start) for s in S]).describe())
E
python $TMPDIR/an2.py
```

```
t 23.900765419006348
     central  side   any  central0  side0  any0
rat                                            
EE      24.8  49.7  62.4       3.2    5.1   8.9
FF      24.5  59.9  64.6       2.0    2.0   4.8
GG      21.4  50.0  64.3       4.8    0.0   4.8 rat
EE    157
FF    147
GG     42
dtype: int64
pooled central     24.3
side        54.0
any         63.6
central0     2.9
side0        3.2
any0         6.6
dtype: float64
all units      central  side
rat               
EE      20.8  42.1
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000067-fujisawa-2008; . $TMPDIR/scratch/bin/activate; cat > $TMPDIR/an3.py <<'E'
import pickle, sys, numpy as np, pandas as pd, time
from scipy import stats
sys.path.insert(0,'.'); import pfc
pd.set_option('display.width',250)
S=pickle.load(open('/tmp/claude-1001/S.pkl','rb'))
S=[s for s in S if s['has_raw']]
U={s['session']:pfc.assign_units(s) for s in S}
single={k:u[(u.region=='PFC')&~u.mua].unit.tolist() for k,u in U.items()}
D=[]
for s in S:
    c=pickle.load(open(f"/tmp/claude-1001/conn_{s['session']}.pkl",'rb'))
    d=pfc.directed(c); d['session']=s['session']; d['rat']=s['subject']
    sh=U[s['session']].set_index('unit').shank
    d['dist']=200*np.abs(sh[d.pre].values-sh[d.post].values); D.append(d)
D=pd.concat(D,ignore_index=True)
n=len(D); print('pairs',n,'exc',D.exc.sum(),D.exc.mean()*100,'inh',D.inh.sum(),D.inh.mean()*100,'total',(D.exc|D.inh).mean()*100)
# reciprocal
key=D.set_index(['session','pre','post']); conn=(D.exc|D.inh).values
cs=set(map(tuple,D.loc[D.exc|D.inh,['session','pre','post']].values))
rec=sum(1 for (se,a,b) in cs if (se,b,a) in cs)//2
print('reciprocal unordered',rec, rec/(n/2)*100, 'per ordered', 2*rec/n*100)
# classes
rows=[]
for s in S:
    d=D[D.session==s['session']]
    for u in single[s['session']]:
        e=d[(d.pre==u)].exc.any(); i=d[(d.pre==u)].inh.any()
        rows.append({'session':s['session'],'rat':s['subject'],'unit':u,'pyr':e and not i,'int':i and not e,'both':e and i})
C=pd.DataFrame(rows)
print('pyr',C.pyr.mean()*100,'int',C.int.mean()*100,'both',C.both.sum())
g=C.groupby('session')[['pyr','int']].sum(); g=g[g.int>0]; print(g.assign(r=g.pyr/g.int)); print('ratio mean sess',(g.pyr/g.int).mean(),(g.pyr/g.int).std(), 'pooled',C.pyr.sum()/C.int.sum())
gr=C.groupby('rat')[['pyr','int']].sum(); print('rat ratios',(gr.pyr/gr.int))
intset=set(map(tuple,C[C.int][['session','unit']].values))
tg=D[D.exc][['session','post']].drop_duplicates(); print('targets',len(tg),'int frac',np.mean([ (a,b) in intset for a,b in tg.values])*100)
# distance
con=D.exc|D.inh
same=D.dist==0
tab=[[con[same].sum(),(~con[same]).sum()],[con[~same].sum(),(~con[~same]).sum()]]
print('same shank prob',con[same].mean()*100,'diff',con[~same].mean()*100, stats.fisher_exact(tab))
pr=D.assign(c=con).groupby('dist').c.agg(['mean','size','sum']); print(pr); print(stats.spearmanr(pr.index,pr['mean'])); print('max dist conn',D[con].dist.max())
print('frac of connections on same shank', (con&same).sum()/con.sum())
D.to_pickle('/tmp/claude-1001/D.pkl'); C.to_pickle('/tmp/claude-1001/C.pkl')
E
python $TMPDIR/an3.py
```

```
pairs 31754 exc 293 0.9227183976821818 inh 73 0.2298922970334446 total 1.1526106947156265
reciprocal unordered 39 0.24563834477546137 per ordered 0.24563834477546137
pyr 39.08872901678657 int 2.6378896882494005 both 20
         pyr  int     r
session                
EE.049    24    1  24.0
EE.196    74    4  18.5
FF.103    15    2   7.5
FF.130    33    2  16.5
FF.167     9    2   4.5
ratio mean sess 14.2 8.043631020876083 pooled 14.818181818181818
rat ratios rat
EE    19.6
FF     9.5
GG     inf
dtype: float64
targets 126 int frac 6.349206349206349
same shank prob 4.623791509037411 diff 0.5408208623499778 SignificanceResult(statistic=np.float64(8.915580456057523), pvalue=np.float64(2.7779704105859645e-88))
          mean  size  sum
dist                     
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000067-fujisawa-2008; . $TMPDIR/scratch/bin/activate; cat > $TMPDIR/an4.py <<'E'
import pickle, sys, numpy as np, pandas as pd, time
from scipy import stats
sys.path.insert(0,'.'); import pfc
pd.set_option('display.width',250)
S=pickle.load(open('/tmp/claude-1001/S.pkl','rb'))
S={s['session']:s for s in S if s['has_raw']}
D=pd.read_pickle('/tmp/claude-1001/D.pkl')
print('inh by same shank', D[D.inh].groupby(D.dist==0).size())
E=D[D.exc]
t=time.time(); rows=[]
for k,(i,r) in enumerate(E.iterrows()):
    s=S[r.session]; rng=np.random.default_rng([5,k])
    isl=(s['trials'].side=='Left').values
    a=pfc.coincidence_test(s,r.pre,r.post,rng)
    l=pfc.coincidence_test(s,r.pre,r.post,rng,isl)
    rr=pfc.coincidence_test(s,r.pre,r.post,rng,~isl)
    rows.append({'session':r.session,'pre':r.pre,'post':r.post,'n':a['n_coincidences'],'a_sig':a['any_sig'],'a_frac':a['sig_fraction'],'b_sig':l['any_sig'] or rr['any_sig']})
P=pd.DataFrame(rows); print('t',time.time()-t)
print(len(P),'a',P.a_sig.mean()*100,'b',P.b_sig.mean()*100); print(P.a_frac.describe()); print((P.a_frac==1).sum())
P.to_pickle('/tmp/claude-1001/P.pkl')
t=time.time(); rows=[]
for k,(i,r) in enumerate(E.iterrows()):
    s=S[r.session]; rng=np.random.default_rng([6,k])
    res=pfc.first_vs_later(s['trains'][r.pre],s['trains'][r.post],rng)
    rows.append({**res,'session':r.session})
Q=pd.DataFrame(rows); print('t',time.time()-t)
ok=Q[(Q.n_first>=20)&(Q.n_later>=20)]
print(len(Q),len(ok),'dep',((ok.p<0.10)&(ok['diff']>0)).mean()*100,'fac',((ok.p<0.10)&(ok['diff']<0)).mean()*100)
# supralinear
t=time.time(); rows=[]
for se in E.session.unique():
    s=S[se]; e=E[E.session==se]
    for post,g in e.groupby('post'):
        if len(g)<2: continue
        pres=[s['trains'][p] for p in g.pre]
        for w in (0.005,0.02):
            cg=pfc.coincidence_gain(pres,s['trains'][post],s['duration'],w).set_index('n_partners')
            if 1 in cg.index and 2 in cg.index:
                rows.append({'session':se,'post':post,'n_pre':len(g),'w':w,'e1':cg.excess[1],'e2':cg.excess[2],'n2':cg.events[2]})
G=pd.DataFrame(rows); print('t',time.time()-t)
for w in (0.005,0.02):
    g=G[(G.w==w)&(G.n2>=20)]
    d=g.e2-2*g.e1
    print(w,len(G[G.w==w]),len(g),'supra',(d>0).mean(), stats.wilcoxon(d,alternative='greater').pvalue if len(g)>0 else None, g[['e1','e2']].median().values)
E
python $TMPDIR/an4.py
```

```
inh by same shank dist
False    47
True     26
dtype: int64
t 16.138126850128174
293 a 1.023890784982935 b 2.7303754266211606
count    293.000000
mean       0.001960
std        0.024817
min        0.000000
25%        0.000000
50%        0.000000
75%        0.000000
max        0.386139
Name: a_frac, dtype: float64
0
t 38.41315984725952
293 292 dep 4.794520547945205 fac 14.383561643835616
t 13.497144222259521
0.005 42 41 supra 0.3170731707317073 0.9966731455015179 [0.01319725 0.01827794]
[... 1 more lines not kept]
```

**Agent**

Position dependence is rarely significant (1 to 3% of pairs). Checking the coincidence test on a synthetic pair with known position-limited coupling before trusting that.

**Agent calls Bash**

```bash
cd entries/000067-fujisawa-2008; . $TMPDIR/scratch/bin/activate; python - <<'E'
import sys, numpy as np, pandas as pd
sys.path.insert(0,'.'); import pfc
rng=np.random.default_rng(0)
# 40 trials, run 6 s each, position linear 0..1 over run
n=40; rs=np.arange(n)*50.0+10; re=rs+6
rate=39.0625; T=n*50+20; nf=int(T*rate); lin=np.zeros(nf)
tt=np.arange(nf)/rate
for a,b in zip(rs,re):
    m=(tt>=a)&(tt<=b); lin[m]=1+(tt[m]-a)/6
s={'trials':pd.DataFrame({'nosepoke_start':rs-2,'run_start':rs,'run_end':re,'side':np.where(np.arange(n)%2,'Left','Right')}),'lin':lin,'lin_rate':rate}
pre=np.sort(rng.uniform(0,T,int(10*T))); post0=np.sort(rng.uniform(0,T,int(10*T)))
pos,tr=pfc.positions_at(s,pre)
for eff in (0.05,0.1,0.2):
    m=(pos>0.4)&(pos<0.6)&(rng.random(len(pre))<eff)
    post=np.sort(np.r_[post0,pre[m]+0.002])
    s['trains']=[pre,post]
    r=pfc.coincidence_test(s,0,1,rng); print(eff, r)
s['trains']=[pre,post0]; print('null',pfc.coincidence_test(s,0,1,rng))
E
```

```
0.05 {'n_coincidences': 121, 'sig_fraction': 0.0, 'any_sig': False, 'level': 0.0}
0.1 {'n_coincidences': 142, 'sig_fraction': 0.0, 'any_sig': False, 'level': 0.0}
0.2 {'n_coincidences': 180, 'sig_fraction': 0.0, 'any_sig': False, 'level': 0.0}
null {'n_coincidences': 95, 'sig_fraction': 0.0, 'any_sig': False, 'level': 0.0}
```

**Agent calls Bash**

```bash
cd entries/000067-fujisawa-2008; python - <<'E'
s=open('pfc.py').read()
old=s[s.index('def band_test'):s.index('def lr_test')]
new='''def band_test(stats: np.ndarray, alpha: float, two_sided: bool = True, kind: str = "rank"):
    """Pointwise and global bands from resampled statistics, as in the paper's Methods.

    `stats` is (1 + M, G): row 0 the original statistic, the others the resampled ones. The
    global band is the narrowest of a family of pointwise bands within which at least 1 - alpha
    of all 1 + M data sets lie completely. kind="rank": the pointwise bands are the quantiles of
    the resampled values at each point (the Methods' bands). kind="sd": the pointwise bands are
    the resampled mean plus or minus c times their s.d.; used where the rank family cannot reach
    the level (with 1000 surrogates and smooth statistics on 101 points, more than 1% of the data
    sets reach the most extreme rank somewhere, so no one-sided rank band reaches 0.01).
    Returns the positions where the original breaks the global band, and the global band's
    pointwise level (rank) or its c (sd).
    """
    n = stats.shape[0]
    if kind == "sd":
        mu = stats[1:].mean(0)
        sd = stats[1:].std(0)
        sd = np.where(sd > 0, sd, np.inf)
        z = (stats - mu) / sd
        z = np.abs(z) if two_sided else z
        m = np.sort(z.max(axis=1))
        c = m[int(np.ceil((1 - alpha) * n)) - 1]
        return z[0] > c, c
    srt = np.sort(stats, axis=0)
    p_up = np.empty_like(stats)
    p_lo = np.empty_like(stats)
    for g in range(stats.shape[1]):
        p_up[:, g] = (n - np.searchsorted(srt[:, g], stats[:, g], side="left")) / n
        p_lo[:, g] = np.searchsorted(srt[:, g], stats[:, g], side="right") / n
    p = np.minimum(1, 2 * np.minimum(p_up, p_lo)) if two_sided else p_up
    m = np.sort(p.min(axis=1))
    allowed = int(np.floor(alpha * n))
    level = 0.0
    for v in np.unique(m):
        if np.sum(m <= v) <= allowed:
            level = v
        else:
            break
    return p[0] <= level, level


'''
s=s.replace(old,new)
s=s.replace('''    sig, _, _ = band_test(d, alpha)
    return sig, d[0]''','''    sig, _ = band_test(d, alpha, kind=kind)
    return sig, d[0]''')
s=s.replace('''def lr_test(dens: np.ndarray, is_left: np.ndarray, rng, n_perm: int = N_PERM, alpha: float = 0.05):''','''def lr_test(dens: np.ndarray, is_left: np.ndarray, rng, n_perm: int = N_PERM, alpha: float = 0.05,
            kind: str = "rank"):''')
s=s.replace('''                     n_jitter: int = N_JITTER, alpha: float = 0.01) -> dict:''','''                     n_jitter: int = N_JITTER, alpha: float = 0.01, kinds=("sd", "rank")) -> dict:''')
s=s.replace('''    sig, p, level = band_test(stats, alpha, two_sided=False)
    return {"n_coincidences": int(obs.sum()), "sig_fraction": float(sig.mean()), "any_sig": bool(sig.any()),
            "level": level}''','''    out = {"n_coincidences": int(obs.sum())}
    for kind in kinds:
        sig, level = band_test(stats, alpha, two_sided=False, kind=kind)
        out.update({f"{kind}_sig": bool(sig.any()), f"{kind}_fraction": float(sig.mean()), f"{kind}_level": level})
    return out''')
s=s.replace('''    by well under 1% of the track). One-sided global band at `alpha`.''','''    by well under 1% of the track). One-sided global band at `alpha`, of each kind of band_test.''')
open('pfc.py','w').write(s)
E
. $TMPDIR/scratch/bin/activate; python - <<'E'
import sys, numpy as np, pandas as pd
sys.path.insert(0,'.'); import pfc
rng=np.random.default_rng(0)
n=40; rs=np.arange(n)*50.0+10; re=rs+6
rate=39.0625; T=n*50+20; nf=int(T*rate); lin=np.zeros(nf)
tt=np.arange(nf)/rate
for a,b in zip(rs,re):
    m=(tt>=a)&(tt<=b); lin[m]=1+(tt[m]-a)/6
s={'trials':pd.DataFrame({'nosepoke_start':rs-2,'run_start':rs,'run_end':re,'side':np.where(np.arange(n)%2,'Left','Right')}),'lin':lin,'lin_rate':rate}
pre=np.sort(rng.uniform(0,T,int(10*T))); post0=np.sort(rng.uniform(0,T,int(10*T)))
pos,tr=pfc.positions_at(s,pre)
for eff in (0.05,0.1,0.2):
    m=(pos>0.4)&(pos<0.6)&(rng.random(len(pre))<eff)
    s['trains']=[pre,np.sort(np.r_[post0,pre[m]+0.002])]
    print(eff, pfc.coincidence_test(s,0,1,rng))
s['trains']=[pre,post0]
print('null FWER sd', np.mean([pfc.coincidence_test(s,0,1,np.random.default_rng(k),n_jitter=300)['sd_sig'] for k in range(0)]) if False else '')
# null FWER using pure null stats
fw=[]
for k in range(200):
    st=rng.poisson(5,size=(1001,1)).astype(float)+0  # placeholder
fw=np.mean([pfc.band_test(np.cumsum(rng.normal(size=(1001,60)),1),0.01,False,'sd')[0].any() for _ in range(300)]); print('sd FWER',fw)
fw=np.mean([pfc.band_test(np.cumsum(rng.normal(size=(1001,60)),1),0.05,True,'rank')[0].any() for _ in range(300)]); print('rank 2-sided FWER',fw)
E
```

```
0.05 {'n_coincidences': 121, 'sd_sig': True, 'sd_fraction': 0.2376237623762376, 'sd_level': np.float64(3.5050177309439476), 'rank_sig': False, 'rank_fraction': 0.0, 'rank_level': 0.0}
0.1 {'n_coincidences': 142, 'sd_sig': True, 'sd_fraction': 0.2871287128712871, 'sd_level': np.float64(3.4421013280950064), 'rank_sig': False, 'rank_fraction': 0.0, 'rank_level': 0.0}
0.2 {'n_coincidences': 180, 'sd_sig': True, 'sd_fraction': 0.32673267326732675, 'sd_level': np.float64(3.5761004388175874), 'rank_sig': False, 'rank_fraction': 0.0, 'rank_level': 0.0}
null FWER sd 
sd FWER 0.006666666666666667
rank 2-sided FWER 0.04
```

**Agent calls Bash**

```bash
cd entries/000067-fujisawa-2008; . $TMPDIR/scratch/bin/activate; python - <<'E'
import pickle, sys, numpy as np, pandas as pd, time
sys.path.insert(0,'.'); import pfc
S=pickle.load(open('/tmp/claude-1001/S.pkl','rb')); S={s['session']:s for s in S if s['has_raw']}
D=pd.read_pickle('/tmp/claude-1001/D.pkl'); E=D[D.exc]
t=time.time(); rows=[]
for k,(i,r) in enumerate(E.iterrows()):
    s=S[r.session]; rng=np.random.default_rng([5,k]); isl=(s['trials'].side=='Left').values
    a=pfc.coincidence_test(s,r.pre,r.post,rng); l=pfc.coincidence_test(s,r.pre,r.post,rng,isl); rr=pfc.coincidence_test(s,r.pre,r.post,rng,~isl)
    rows.append({'n':a['n_coincidences'],'a_sd':a['sd_sig'],'a_frac':a['sd_fraction'],'b_sd':l['sd_sig'] or rr['sd_sig'],'a_rank':a['rank_sig'],'b_rank':l['rank_sig'] or rr['rank_sig']})
P=pd.DataFrame(rows); print(time.time()-t); print(P.mean()); print(P.a_frac[P.a_sd].describe())
E
```

```
16.812813997268677
n         22.706485
a_sd       0.027304
a_frac     0.004934
b_sd       0.017065
a_rank     0.010239
b_rank     0.027304
dtype: float64
count    8.000000
mean     0.180693
std      0.189325
min      0.019802
25%      0.076733
50%      0.103960
75%      0.205446
max      0.544554
Name: a_frac, dtype: float64
```

**Agent calls Bash**

```bash
cd entries/000067-fujisawa-2008; . $TMPDIR/scratch/bin/activate; python - <<'E'
import pickle, sys, numpy as np, pandas as pd, time
sys.path.insert(0,'.'); import pfc
S=pickle.load(open('/tmp/claude-1001/S.pkl','rb'))
for s in S:
    r=[]
    for sh in (0,-3,3,-10):
        c=pfc.sensor_check(s,sh); r.append(round((c.side==c.sensor_side).mean(),3))
    c=pfc.sensor_check(s)
    act=np.where(c.side=='Right',c.right_poke,c.left_poke)/np.where(c.side=='Right',c.right_run,c.left_run)
    print(s['session'],len(c),r,'poke/run activity median',round(np.median(act),1))
t=time.time()
for s in S:
    if not s['has_raw']: continue
    u=pfc.assign_units(s); units=u[(u.region=='PFC')&~u.mua].unit.tolist()
    d=pfc.decode_side(s,units,np.arange(-20,8,2.0))
    print(s['session'], d.accuracy.round(2).tolist())
print(time.time()-t)
E
```

```
EE.049 19 [np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0)] poke/run activity median 784.8
EE.088 31 [np.float64(0.968), np.float64(0.968), np.float64(0.968), np.float64(0.806)] poke/run activity median 647.4
EE.196 48 [np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(0.875)] poke/run activity median 687.7
FF.103 39 [np.float64(1.0), np.float64(0.949), np.float64(1.0), np.float64(0.949)] poke/run activity median 1151.8
FF.130 46 [np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(0.978)] poke/run activity median 908.9
FF.167 43 [np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(0.953)] poke/run activity median 241.9
GG.069 40 [np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.05)] poke/run activity median 2.3
GG.097 38 [np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.053)] poke/run activity median 2.1
GG.149 31 [np.float64(0.0), np.float64(0.032), np.float64(0.0), np.float64(0.097)] poke/run activity median 2.9
EE.049 [0.68, 0.42, 0.32, 0.63, 0.68, 0.74, 0.68, 0.68, 0.58, 0.84, 0.63, 0.84, 0.79, 0.74]
EE.196 [0.73, 0.67, 0.58, 0.81, 0.56, 0.69, 0.69, 0.83, 0.85, 0.92, 0.96, 0.98, 0.94, 0.94]
FF.103 [0.54, 0.62, 0.49, 0.54, 0.62, 0.69, 0.56, 0.49, 0.54, 0.41, 0.69, 0.72, 0.85, 0.9]
FF.130 [0.59, 0.54, 0.63, 0.72, 0.48, 0.48, 0.57, 0.67, 0.74, 0.89, 0.91, 0.93, 0.89, 0.96]
FF.167 [0.51, 0.51, 0.37, 0.35, 0.42, 0.42, 0.51, 0.63, 0.74, 0.88, 0.79, 0.95, 0.91, 0.86]
GG.069 [0.5, 0.45, 0.48, 0.45, 0.6, 0.68, 0.6, 0.48, 0.45, 0.57, 0.57, 0.75, 0.68, 0.8]
GG.097 [0.61, 0.5, 0.66, 0.63, 0.55, 0.66, 0.63, 0.58, 0.66, 0.61, 0.42, 0.42, 0.71, 0.84]
GG.149 [0.35, 0.52, 0.52, 0.52, 0.55, 0.48, 0.52, 0.29, 0.61, 0.55, 0.52, 0.61, 0.77, 0.87]
1.2185614109039307
```

**Agent calls Bash**

```bash
cd entries/000067-fujisawa-2008; python - <<'E'
s=open('pfc.py').read()
s=s.replace('''CA1_CHANNELS = {"EE": range(64, 96), "FF": range(64, 96), "GG": range(69, 101)}
# Nose-poke sensors. CRCNS pfc-2 gives channels 97 (right) and 98 (left), 1-based; in rat GG the
# data show them at 65 and 66 (see the notebook), so the map is per rat (0-based here).
NOSEPOKE_CHANNELS = {"EE": (96, 97), "FF": (96, 97), "GG": (64, 65)}''','''# Channels are 0-based here. CRCNS pfc-2 gives, 1-based, 65-96 for CA1 and 97 (right) and 98
# (left) for the nose-poke sensors in every rat. The data agree for rats EE and FF; in rat GG
# the sensors are at 65 and 66 and the CA1 probe at 70-101 (see the notebook's data check), and
# the sensor at 66 is the one active on trials labelled Right.
CRCNS_CA1 = range(64, 96)
CRCNS_NOSEPOKE = (96, 97)                      # (right, left)
CA1_CHANNELS = {"EE": range(64, 96), "FF": range(64, 96), "GG": range(69, 101)}
NOSEPOKE_CHANNELS = {"EE": (96, 97), "FF": (96, 97), "GG": (65, 64)}
SENSOR_READ = (64, 65, 96, 97)                 # LFP columns read for the sensor checks''')
s=s.replace('''        right, left = NOSEPOKE_CHANNELS[s["subject"]]
        s["sensors"] = lfp[:, [right, left]].astype(np.float32)''','''        cols = [c for c in SENSOR_READ if c < lfp.shape[1]]
        s["sensors"] = dict(zip(cols, lfp[:, cols].astype(np.float32).T))''')
s=s.replace('''def sensor_check(s: dict, shift_s: float = 0.0) -> pd.DataFrame:
    """Per trial, activity of the right and left nose-poke sensors in the nose-poke period.

    Activity is the mean absolute deviation from the session median of the LFP copy of each
    sensor channel; `shift_s` moves the trial times (the clock check).
    """
    x = s["sensors"]
    dev = np.abs(x - np.median(x, axis=0))''','''def sensor_activity(s: dict, channels=None) -> np.ndarray:
    """(samples, 2) absolute deviation from the session median of the (right, left) sensors."""
    right, left = channels or NOSEPOKE_CHANNELS[s["subject"]]
    x = np.stack([s["sensors"][right], s["sensors"][left]], axis=1)
    return np.abs(x - np.median(x, axis=0))


def sensor_check(s: dict, channels=None, shift_s: float = 0.0) -> pd.DataFrame:
    """Per trial, activity of the right and left nose-poke sensors in the nose-poke period and
    in the run. Activity is the mean absolute deviation from the session median of the LFP copy
    of each sensor channel; `shift_s` moves the trial times."""
    dev = sensor_activity(s, channels)
    x = dev''')
open('pfc.py','w').write(s)
E
grep -n "def sensor_check" -A 25 pfc.py | head -40
```

```
327:def sensor_check(s: dict, channels=None, shift_s: float = 0.0) -> pd.DataFrame:
328-    """Per trial, activity of the right and left nose-poke sensors in the nose-poke period and
329-    in the run. Activity is the mean absolute deviation from the session median of the LFP copy
330-    of each sensor channel; `shift_s` moves the trial times."""
331-    dev = sensor_activity(s, channels)
332-    x = dev
333-    rows = []
334-    for k, tr in s["trials"].iterrows():
335-        a = int((tr.nosepoke_start + shift_s) * s["lfp_rate"])
336-        b = int((tr.run_start + shift_s) * s["lfp_rate"])
337-        c = int((tr.run_end + shift_s) * s["lfp_rate"])
338-        if a < 0 or c > len(x) or b <= a:
339-            continue
340-        poke, run = dev[a:b].mean(0), dev[b:c].mean(0)
341-        rows.append({"trial": k, "side": tr.side, "right_poke": poke[0], "left_poke": poke[1],
342-                     "right_run": run[0], "left_run": run[1]})
343-    out = pd.DataFrame(rows)
344-    out["sensor_side"] = np.where(out.right_poke > out.left_poke, "Right", "Left")
345-    return out
346-
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000067-fujisawa-2008; python - <<'E'
s=open('pfc.py').read()
s=s.replace('''# ---------------------------------------------------------------------------------------------
# Position-dependent firing''','''def sensor_edges(s: dict, window: float = 1.0) -> pd.DataFrame:
    """Mean activity of the trial's own sensor around the start of the first nose poke and the
    end of the last one, each trial scaled to its maximum (the clock check of the trial table
    against the recorded signals)."""
    dev = sensor_activity(s)
    n = int(window * s["lfp_rate"])
    lags = np.arange(-n, n + 1) / s["lfp_rate"]
    on, off = [], []
    for _, tr in s["trials"].iterrows():
        col = 0 if tr.side == "Right" else 1
        for t, store in ((tr.nosepoke_start, on), (tr.run_start, off)):
            k = int(round(t * s["lfp_rate"]))
            if k - n >= 0 and k + n < len(dev):
                seg = dev[k - n:k + n + 1, col]
                store.append(seg / max(seg.max(), 1e-9))
    return pd.DataFrame({"lag_s": lags, "at_poke_start": np.mean(on, 0), "at_poke_end": np.mean(off, 0)})


# ---------------------------------------------------------------------------------------------
# Position-dependent firing''')
open('pfc.py','w').write(s)
E
python -c "import ast;ast.parse(open('pfc.py').read())"
```

```
(Bash completed with no output)
```

**Agent**

Progress: helper module done, claims written, analyses prototyped. Now writing the notebook.

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/make_nb.py",
 "content": "import nbformat as nbf\nimport sys\n\nnb = nbf.v4.new_notebook()\ncells = []\n\n\ndef md(text, tags=None):\n    c = nbf.v4.new_markdown_cell(text.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\ndef code(text, tags=None):\n    c = nbf.v4.new_code_cell(text.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\nRESULTS = {}\nif len(sys.argv) > 1:\n    import json\n    RESULTS = json.load(open(sys.argv[1]))\n\n\ndef result(key):\n    md(RESULTS.get(key, f\"**Result: TODO {key}.**\"))\n\n\nmd(r\"\"\"\n# Reproducing Fujisawa et al. (2008) from dandiset 000067\n\n**Paper.** Fujisawa S, Amarasingham A, Harrison MT, Buzsáki G (2008). Behavior-dependent\nshort-term assembly dynamics in the medial prefrontal cortex. *Nature Neuroscience* 11, 823-833.\n[doi:10.1038/nn.2134](https://doi.org/10.1038/nn.2134). This attempt used the full text of the\nauthor manuscript in PubMed Central (PMC2562676): Results, figure legends and Methods. The\nsupplementary information could not be retrieved (PubMed Central and the publisher returned a\nreCAPTCHA page), so measures it defines are fixed in the claims file instead.\n\n**Dandiset.** [DANDI:000067](https://dandiarchive.org/dandiset/000067/0.250624.0419), version\n0.250624.0419. The paper (2008) cites no DANDI version. There are two published versions,\n0.210812.1457 and 0.250624.0419; the data check below shows that both, and the draft, hold the\nsame 28 assets (same asset and blob ids). The later one differs only in metadata (contributor\nidentifiers and affiliations, a fuller link to the paper). The most recent published version is\npinned.\n\n**What the dandiset holds.** 28 sessions of three rats (EE, FF, GG): spike times of every sorted\ncluster, the LFP, in most files the wideband signal, and in ten files a trial table and position.\nThe units table has no channel, shank, brain region or cell type. The recordings combine a 64-site\nprefrontal probe and a 32-site CA1 probe. The paper's four rats and its example session (EE.188)\nare not all here.\n\n**Outside inputs.** The channel map (which channels are the prefrontal probe, the CA1 probe and\nthe nose-poke sensors) comes from the CRCNS pfc-2 data description (version 0.7,\ndoi:10.6080/K01V5BWK), which documents the same recordings; the link claim tests it against the\ndata. Claims marked \"with labels\" use it. The analysis itself runs on the dandiset's data only.\n\n**Randomness.** Each claim's section draws from its own generator, seeded by a fixed number and\nthe session's index.\n\n| Claim | Data | Status |\n|---|---|---|\n| channel-region-link | with labels | tested |\n| rats-and-units | with labels | tested |\n| task-performance | dandiset | blocked: data missing (only correct trials are in the files) |\n| fig2c-active-fraction | with labels | tested |\n| fig2-field-size | with labels | tested |\n| fig2b-trajectory-selective | with labels | tested |\n| traj-diverge | dandiset | blocked: data missing (no y coordinate) |\n| odor-nosepoke | with labels | tested |\n| fig3-connection-rates | with labels | tested |\n| fig3-cell-classes | with labels | tested |\n| fig3f-distance | with labels | tested |\n| fig4-position-dependence | with labels | tested |\n| fig6-facilitation-depression | with labels | tested |\n| fig7-supralinear | with labels | tested |\n| fig3-trajectory-by-class | with labels | tested |\n| ee188-example-session | dandiset | blocked: data missing (session EE.188 is not in the dandiset) |\n\"\"\")\n\ncode(r\"\"\"\nimport time\nimport warnings\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nfrom concurrent.futures import ThreadPoolExecutor\nfrom dandi.dandiapi import DandiAPIClient\nfrom scipy import stats\n\nimport pfc\n\npd.set_option(\"display.width\", 220)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 300)\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nstarted = time.time()\nurls = pfc.asset_urls()\nwith ThreadPoolExecutor(8) as pool:\n    files = pd.DataFrame(list(pool.map(lambda p: pfc.describe_file(p, urls[p]), sorted(urls))))\nwm_paths = [p for p in sorted(urls) if any(f\"ses-{s.replace('.', '-')}_\" in p for s in pfc.WM_SESSIONS)]\nsessions = pfc.load_sessions(wm_paths, workers=9)\nby_name = {s[\"session\"]: s for s in sessions}\nanalysed = [s for s in sessions if s[\"has_raw\"]]\nprint(f\"{len(files)} files described and {len(sessions)} working memory sessions loaded from dandiset \"\n      f\"{pfc.DANDISET_ID} version {pfc.DANDISET_VERSION} in {time.time() - started:.0f} s\")\n\"\"\")\n\nmd(\"\"\"\n## Data check\n\nEach check of the description against the data is stated under its output.\n\"\"\")\n\ncode(r\"\"\"\nwith DandiAPIClient() as client:\n    versions = [v.identifier for v in client.get_dandiset(pfc.DANDISET_ID).get_versions()]\n    blobs = {}\n    for v in versions:\n        ds = client.get_dandiset(pfc.DANDISET_ID, v)\n        blobs[v] = sorted((a.path, a.identifier, a.size) for a in ds.get_assets())\nprint(\"Versions:\", versions)\nfor v in versions:\n    print(f\"  {v}: {len(blobs[v])} assets, {sum(b[2] for b in blobs[v]) / 1e9:.1f} GB, \"\n          f\"identical to {pfc.DANDISET_VERSION}: {blobs[v] == blobs[pfc.DANDISET_VERSION]}\")\nshow = files.drop(columns=[\"lfp_head\", \"spike_head\", \"path\"])\nprint(\"\\nEvery file (raw_s, lfp_s: duration of the wideband and LFP series in seconds):\")\nprint(show.to_string(index=False))\nprint(\"\\nSubjects:\", files.subject.value_counts().to_dict())\nprint(\"Channel locations:\", sorted({l for ls in files.locations for l in ls}),\n      \"; electrode x, y, z all NaN in every file:\", bool(files.xyz_all_nan.all()),\n      \"; electrode groups per file:\", sorted(files.groups.unique()))\nprint(\"Unit table columns:\", sorted({c for cs in files.unit_columns for c in cs}))\ndup_lfp = files[files.lfp_head.duplicated(keep=False) & (files.lfp_s > 2)]\ndup_spk = files[(files.spike_head != \"\") & files.spike_head.duplicated(keep=False)]\nprint(\"\\nFiles sharing the first second of LFP (channel 1):\", dup_lfp.session.tolist() or \"none\")\nprint(\"Files sharing their first 50 spike times:\", dup_spk.session.tolist() or \"none\")\n\"\"\", tags=[\"sanity\"])\n\nmd(\"\"\"\nAll versions hold the same assets, so the pinned version's content is the content of every\nversion. The dandiset has three rats; the paper recorded four. Ten files have a trial table and\nposition. Session EE.088 and the eleven other sessions of its day have units but no wideband\nsignal, and the test sessions EE.043 and EE.044 last about a second. Channel locations are\n\"unknown\", electrode coordinates are missing, and the 104 (EE, FF) or 101 (GG) channels are cut\ninto 13 groups of 8 called \"shank1\" to \"shank13\", although the probes have 8 and 4 shanks and\nsome channels are sensors. The units table holds spike times only. No two files share their first\nsecond of LFP or their first spike times, so no recording is deposited twice; the sessions of\none day of rat EE were sorted together (the CRCNS description says so), so their units share\nnumbers but not spikes.\n\nThe CRCNS description lists 13 working memory sessions. Of these, EE.152, EE.165 and EE.188 are\nnot in the dandiset and EE.210 has no trial table, which leaves the nine loaded here. GG.063, a\nspontaneous alternation session in the CRCNS table, also has a trial table; it is not used.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor s in sessions:\n    tr = s[\"trials\"]\n    t = pfc.frame_times(s)\n    pos, trial = pfc.positions_at(s, t)\n    in_run = np.zeros(len(t), bool)\n    for a, b in zip(tr.run_start, tr.run_end):\n        in_run |= (t >= a) & (t <= b)\n    start_frame = np.round(tr.run_start.values * s[\"lin_rate\"]).astype(int)\n    end_frame = np.round(tr.run_end.values * s[\"lin_rate\"]).astype(int) - 1\n    rows.append({\n        \"session\": s[\"session\"], \"trials\": len(tr), \"left\": int((tr.side == \"Left\").sum()),\n        \"right\": int((tr.side == \"Right\").sum()),\n        \"poke_s_median\": np.median(tr.run_start - tr.nosepoke_start),\n        \"run_s_median\": np.median(tr.run_end - tr.run_start),\n        \"reward_after_stop\": bool((tr.run_end > tr.run_start).all()),\n        \"d_at_run_start\": np.median(s[\"lin\"][start_frame]), \"d_at_run_end\": np.median(s[\"lin\"][end_frame]),\n        \"run_frames_d>0\": np.mean(s[\"lin\"][in_run] > 0), \"frames_d>0_outside_trials\": np.mean(s[\"lin\"][~in_run] > 0),\n        \"lin_min\": s[\"lin\"].min(), \"lin_max\": s[\"lin\"].max(), \"lin_unit\": s[\"lin_unit\"],\n        \"x1_range\": (s[\"x1\"].min(), s[\"x1\"].max()), \"x2_all_zero\": bool(np.all(s[\"x2\"] == 0)),\n        \"pos_unit\": s[\"pos_unit\"], \"duration_s\": round(s[\"duration\"], 1)})\nprint(pd.DataFrame(rows).round(3).to_string(index=False))\nprint(\"\\nTrial column descriptions:\", sessions[0][\"trial_descriptions\"])\n\"\"\", tags=[\"sanity\"])\n\nmd(\"\"\"\nThe trial table's `start_time`, `stop_time` and `reward_time` are the three columns of the CRCNS\nSessionNP matrix: the start of the first nose poke, the end of the last nose poke (the paper's\ntrial start, position 0) and the start of reward consumption (the paper's trial end, position 1).\nThe data agree: the linearized position is 1 at `stop_time` and 2 at `reward_time` (medians\nprinted above), it is above 0 in nearly every frame of the runs and almost never outside the\ntrials. `stop_time` is therefore not the end of the trial, and the description of\n`left_or_right` (\"Time when subject began consuming reward\") is wrong. The linearized position is\nstated in metres but runs from 0 to 2 (0 outside trials), and the two \"(x,y) coordinates\" series\nare both x coordinates, of the two head LEDs (the conversion code takes columns 1 and 3 of the\nposition file); they are stated in metres but are in pixels, and the second LED's is zero\nthroughout. There is no y coordinate, so the side arms cannot be told apart by position. The\nsession durations match the CRCNS table (for example EE.049, 29.81 min). The trial table holds\ncorrect trials only (CRCNS description), so the task performance cannot be computed.\n\"\"\")\n\ncode(r\"\"\"\nunits = pd.concat([pfc.assign_units(s) for s in analysed], ignore_index=True)\nprint(\"Units by session and class (PFC and CA1 split into single units and multi-unit clusters):\")\ncls = np.where(units.region.isin([\"PFC\", \"CA1\"]), units.region + np.where(units.mua, \" multi\", \" single\"), units.region)\nprint(pd.crosstab(units.session, cls, margins=True).to_string())\nprint(\"\\nUnits whose spike times were not in order (sorted on loading):\",\n      {s[\"session\"]: s[\"unsorted_units\"] for s in sessions if s[\"unsorted_units\"]})\nprint(\"\\nFraction of ISIs < 2 ms over all units placed on a probe (bins):\")\nprint(pd.cut(units.isi_lt2ms, [-0.001, 0.001, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1]).value_counts(sort=False).to_string())\nprint(\"\\nMulti-unit rule (ISIs) against the conversion's ordering rule (first unit of a shank block), probe units:\")\nprobe = units[units.region.isin([\"PFC\", \"CA1\"])]\nprint(pd.crosstab(probe.mua.map({True: \"ISI multi-unit\", False: \"ISI single\"}),\n                  probe.first_of_block.map({True: \"first of block\", False: \"not first\"})).to_string())\nprint(\"\\nMedian rate (Hz) and amplitude (uV) by class:\")\nprint(probe.groupby([\"region\", \"mua\"]).agg(n=(\"unit\", \"size\"), rate_hz=(\"rate_hz\", \"median\"),\n                                          amp_uv=(\"amp_uv\", \"median\"), isi_lt2ms=(\"isi_lt2ms\", \"median\")).round(3).to_string())\nsens = units[units.region == \"sensor\"]\nprint(\"\\nSensor clusters (largest on a sensor channel, under 200 uV on the probes):\", len(sens),\n      \"; their sensor-channel amplitude (uV) ranges\", round(sens.aux_amp_uv.min()), \"to\", round(sens.aux_amp_uv.max()))\n\"\"\", tags=[\"sanity\"])\n\nmd(\"\"\"\nUnits are placed by their mean waveform. The fraction of inter-spike intervals under 2 ms is\nbimodal: most units have under 1%, and about one in seven has more than 10%. Those are the\nmulti-unit clusters; they are almost exactly the first unit of each shank block, which is where\nthe conversion's reader puts cluster 1 (multi-unit activity), so the two rules agree on nearly\nevery unit. Multi-unit clusters fire at a median of tens of hertz with small amplitudes. Some\nunits are clusters of the sensor signals (millivolts on a sensor channel, almost nothing on the\nprobes). In six sessions one unit's spike times are two sorted runs one after the other (the\nfile breaks the rule that spike times are in order); these are multi-unit clusters and are\nsorted on loading. From here on, PFC single units are the units placed on the prefrontal probe\nthat are not multi-unit clusters.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor s in analysed:\n    th = s[\"theta_ratio\"]\n    sub = s[\"subject\"]\n    ca1 = np.array(pfc.CA1_CHANNELS[sub])\n    rows.append({\"session\": s[\"session\"], \"theta_pfc_1_64\": np.median(th[:64]),\n                 \"theta_crcns_ca1_65_96\": np.median(th[list(pfc.CRCNS_CA1)]),\n                 \"theta_ca1_used\": np.median(th[ca1]), \"ca1_used\": f\"{ca1[0] + 1}-{ca1[-1] + 1}\",\n                 \"theta_channels_65_69\": np.round(th[64:69], 2).tolist()})\nprint(\"Theta ratio (6-10 Hz over 1-40 Hz power, raw signal in windows during trials), medians (1-based channels):\")\nprint(pd.DataFrame(rows).round(3).to_string(index=False))\nrows = []\nfor s in sessions:\n    crcns = pfc.sensor_check(s, pfc.CRCNS_NOSEPOKE)\n    used = pfc.sensor_check(s)\n    act = np.where(used.side == \"Right\", used.right_poke, used.left_poke) / np.where(used.side == \"Right\", used.right_run, used.left_run)\n    rows.append({\"session\": s[\"session\"], \"trials\": len(used),\n                 \"agree_crcns_97_98\": (crcns.side == crcns.sensor_side).mean(),\n                 \"agree_used\": (used.side == used.sensor_side).mean(),\n                 \"used_channels_r_l\": tuple(c + 1 for c in pfc.NOSEPOKE_CHANNELS[s[\"subject\"]]),\n                 \"poke_over_run_activity\": np.median(act)})\nprint(\"\\nNose-poke sensors: fraction of trials whose more active sensor during the nose poke is the trial's side:\")\nprint(pd.DataFrame(rows).round(3).to_string(index=False))\n\"\"\", tags=[\"sanity\"])\n\nmd(\"\"\"\nThe CA1 channels have a theta ratio two to three times that of the prefrontal channels in every\nsession, as a hippocampal probe should. In rats EE and FF the CRCNS map holds: CA1 on 65 to 96,\nsensors on 97 (right) and 98 (left). In rat GG it does not: channels 65 to 69 carry no theta,\nthe nose-poke sensors are on 65 and 66, and the CA1 probe is on 70 to 101; and the sensor at 65\nis the one active on trials labelled Right, so either the sensors or the side labels of rat GG\nare swapped relative to the other rats. The data cannot tell which. Left-right tests below do\nnot depend on which side is called left. The prefrontal probe is channels 1 to 64 in all three\nrats (no theta).\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor s in analysed:\n    u = units[units.session == s[\"session\"]]\n    ok = (u.sta_spikes >= 5) & u.region.isin([\"PFC\", \"CA1\"])\n    true_amp = u.amp_uv[ok]\n    chans = pfc.neural_channels(s[\"subject\"])\n    shifted = s[\"sta_amp_shifted\"][:, chans].max(1)[u.unit[ok].values]\n    rows.append({\"session\": s[\"session\"], \"units\": int(ok.sum()), \"amp_uv_median\": np.median(true_amp),\n                 \"amp_uv_spikes_moved_3ms\": np.median(shifted), \"ratio\": np.median(shifted / true_amp.values)})\nprint(\"Mean waveform amplitude at the spike times and with every spike moved 3 ms later:\")\nprint(pd.DataFrame(rows).round(3).to_string(index=False))\nedges = pd.concat([pfc.sensor_edges(s).assign(session=s[\"session\"]) for s in sessions])\ndef crossing(df, col, rising):\n    v = df[col].values\n    half = (v.max() + v.min()) / 2\n    k = np.flatnonzero(v > half)\n    return df.lag_s.values[k[0]] if rising else df.lag_s.values[k[-1]]\nprint(\"\\nTime (s) at which the trial's sensor activity crosses half its range, relative to the table's times:\")\nprint(edges.groupby(\"session\").apply(lambda d: pd.Series({\n    \"onset_vs_poke_start\": crossing(d, \"at_poke_start\", True),\n    \"offset_vs_poke_end\": crossing(d, \"at_poke_end\", False)})).round(3).to_string())\n\"\"\", tags=[\"sanity\"])\n\nmd(\"\"\"\nThe spikes share the clock of the wideband signal: the mean waveform at the spike times is several\ntimes larger than with every spike moved by 3 ms. The trial table shares the clock of the\nrecorded signals: the trial's sensor turns on at the start of the first nose poke and off at the\nend of the last, within a few tens of milliseconds in rats EE and FF (where the sensors are\nstrong). In rat GG the sensor signals are weak and the crossings are less precise.\n\"\"\")\n\ncode(r\"\"\"\noffsets = np.arange(-20, 8, 2.0)\ndec = []\nfor s in analysed:\n    single = units[(units.session == s[\"session\"]) & (units.region == \"PFC\") & ~units.mua].unit.tolist()\n    d = pfc.decode_side(s, single, offsets)\n    d[\"session\"] = s[\"session\"]\n    dec.append(d)\ndec = pd.concat(dec)\ntable = dec.pivot(index=\"session\", columns=\"offset_s\", values=\"accuracy\")\nprint(\"Leave-one-out decoding of the trial side from PFC single units, 1 s windows starting at run start + offset (s):\")\nprint(table.round(2).to_string())\nfar = table[[c for c in table.columns if c <= -10]].mean(1)\nnear = table[[c for c in table.columns if 0 <= c <= 4]].mean(1)\nprint(\"\\nMean accuracy, windows from -20 to -10 s:\", far.round(2).to_dict())\nprint(\"Mean accuracy, windows from 0 to 4 s:\", near.round(2).to_dict())\nprint(\"Sessions where 0-4 s exceeds -20 to -10 s:\", int((near > far).sum()), \"of\", len(near))\n\"\"\", tags=[\"sanity\"])\n\nmd(\"\"\"\nThe side of the trial is decoded from PFC spikes in the second after the run starts and later\n(accuracy 0.7 to 1.0 in most sessions), and much less well 10 to 20 s before it, when the rat is\nbetween trials. So the spikes share the clock of the trial table, in every session.\n\"\"\")\n\n# ---------------------------------------------------------------------------------------------\nmd(\"\"\"\n## channel-region-link\n\n> The dandiset's recording channels can be assigned to the prefrontal probe, the CA1 probe and the\n> nose-poke sensors by the channel map of the CRCNS pfc-2 description of the same recordings, and\n> the data agree with that map.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor s in sessions:\n    th = s.get(\"theta_ratio\")\n    crcns = pfc.sensor_check(s, pfc.CRCNS_NOSEPOKE)\n    used = pfc.sensor_check(s)\n    rows.append({\"session\": s[\"session\"], \"rat\": s[\"subject\"],\n                 \"theta_check_crcns\": None if th is None else bool(np.median(th[list(pfc.CRCNS_CA1)]) > np.median(th[:64])),\n                 \"theta_check_corrected\": None if th is None else bool(np.median(th[list(pfc.CA1_CHANNELS[s[\"subject\"]])]) > np.median(th[:64])),\n                 \"sensor_agree_crcns\": (crcns.side == crcns.sensor_side).mean(),\n                 \"sensor_agree_corrected\": (used.side == used.sensor_side).mean()})\nlink = pd.DataFrame(rows)\nprint(link.round(3).to_string(index=False))\ncrcns_ok = link.theta_check_crcns.dropna().all() and (link.sensor_agree_crcns >= 0.9).all()\ncorr_ok = link.theta_check_corrected.dropna().all() and (link.sensor_agree_corrected >= 0.9).all()\nprint(\"\\nBoth checks hold in every session with the CRCNS numbers:\", bool(crcns_ok))\nprint(\"Both checks hold in every session with the per-rat correction:\", bool(corr_ok))\n\"\"\", tags=[\"claim:channel-region-link\"])\n\nresult(\"channel-region-link\")\n\n# ---------------------------------------------------------------------------------------------\nmd(\"\"\"\n## rats-and-units\n\n> 633 well-isolated units were recorded from the mPFC of four rats.\n\"\"\")\n\ncode(r\"\"\"\nmaps = {s[\"session\"]: None for s in analysed}\npeak = {}\nfor s in analysed:\n    single = units[(units.session == s[\"session\"]) & (units.region == \"PFC\") & ~units.mua].unit.tolist()\n    m = pfc.rate_maps(s, single)\n    maps[s[\"session\"]] = m\n    for u, mm in m.items():\n        peak[(s[\"session\"], u)] = max(mm[\"Left\"].max(), mm[\"Right\"].max())\nunits[\"peak_hz\"] = [peak.get((a, b), np.nan) for a, b in zip(units.session, units.unit)]\npfc_units = units[units.region == \"PFC\"]\ncounts = pd.DataFrame({\n    \"a_single\": pfc_units[~pfc_units.mua].groupby(\"session\").size(),\n    \"b_single_peak_1hz\": pfc_units[~pfc_units.mua & (pfc_units.peak_hz >= 1)].groupby(\"session\").size(),\n    \"c_all_on_probe\": pfc_units.groupby(\"session\").size()}).fillna(0).astype(int)\ncounts.loc[\"total\"] = counts.sum()\nprint(counts.to_string())\nprint(\"\\nRats in the dandiset:\", files.subject.nunique(), \"(\", sorted(files.subject.unique()), \"); paper: 4\")\nprint(\"Session EE.088 (no wideband signal) has\", len(by_name[\"EE.088\"][\"trains\"]), \"units that cannot be placed on a probe.\")\n\"\"\", tags=[\"claim:rats-and-units\"])\n\nresult(\"rats-and-units\")\n\nmd(\"\"\"\n## task-performance\n\n> Rats performed the odor-place matching task at 92% correct (91.9% in the recording sessions).\n\nBlocked: the trial table holds correct trials only (CRCNS description of SessionNP), and the\nmissing y coordinate leaves no way to recover the choice of error trials from the position.\n\"\"\")\n\n# ---------------------------------------------------------------------------------------------\nmd(\"\"\"\n## fig2c-active-fraction\n\n> About 10% (layer 2/3) and 20% (layer 5) of the recorded neurons fire at least one spike in any\n> 100 ms window, a fraction that is relatively constant along the maze.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor s in analysed:\n    single = units[(units.session == s[\"session\"]) & (units.region == \"PFC\") & ~units.mua].unit.tolist()\n    af = pfc.active_fraction(s, single)\n    bins = pd.cut(af.pos, np.linspace(0, 1, 11), include_lowest=True)\n    bm = af.groupby(bins, observed=True).fraction.mean()\n    rows.append({\"session\": s[\"session\"], \"rat\": s[\"subject\"], \"units\": len(single), \"windows\": len(af),\n                 \"mean_pct\": 100 * af.fraction.mean(), \"bin_min_pct\": 100 * bm.min(), \"bin_max_pct\": 100 * bm.max(),\n                 \"max_over_min\": bm.max() / bm.min()})\nact = pd.DataFrame(rows)\nprint(act.round(2).to_string(index=False))\nper_rat = act.groupby(\"rat\").mean_pct.median()\nprint(\"\\nPer rat, median over sessions (%):\", per_rat.round(2).to_dict())\nlayer = {r: (\"2/3\" if 9 <= v <= 11 else \"5\" if 18 <= v <= 22 else \"none\") for r, v in per_rat.items()}\nprint(\"Layer reading matched per rat:\", layer)\npart1 = all(v != \"none\" for v in layer.values()) and sum(v == \"5\" for v in layer.values()) <= 1\npart2 = bool((act.max_over_min <= 2).all())\nprint(\"Every rat matches a layer value, at most one at 20%:\", part1, \"; every session's max/min over position bins <= 2:\", part2)\n\"\"\", tags=[\"claim:fig2c-active-fraction\"])\n\nresult(\"fig2c-active-fraction\")\n\n# ---------------------------------------------------------------------------------------------\nmd(\"\"\"\n## fig2-field-size\n\n> Neurons are active over similar standardized distances of the maze, 0.27 (62 cm) plus or minus\n> 0.17 (39 cm) (mean and s.d.), from the 50% boundaries of the peak firing rate.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor s in analysed:\n    for u, mm in maps[s[\"session\"]].items():\n        pk = {sd: mm[sd].max() for sd in mm}\n        if max(pk.values()) < pfc.MIN_PEAK_HZ:\n            continue\n        pref = max(pk, key=pk.get)\n        rows.append({\"session\": s[\"session\"], \"rat\": s[\"subject\"], \"unit\": u,\n                     \"a_contiguous_pref\": pfc.field_size(mm[pref]), \"c_all_bins_pref\": pfc.field_size(mm[pref], False),\n                     \"b_left\": pfc.field_size(mm[\"Left\"]), \"b_right\": pfc.field_size(mm[\"Right\"])})\nfields = pd.DataFrame(rows)\nb_vals = np.r_[fields.b_left, fields.b_right]\nsummary = pd.DataFrame({\n    \"a\": [fields.a_contiguous_pref.mean(), fields.a_contiguous_pref.std()],\n    \"b\": [b_vals.mean(), b_vals.std(ddof=1)],\n    \"c\": [fields.c_all_bins_pref.mean(), fields.c_all_bins_pref.std()]}, index=[\"mean\", \"sd\"])\nprint(\"Units with a peak of at least 1 Hz:\", len(fields), \"of\", int(counts.loc[\"total\", \"a_single\"]), \"PFC single units\")\nprint(summary.round(3).to_string())\nfor k in summary:\n    m, sd = summary.loc[\"mean\", k], summary.loc[\"sd\", k]\n    print(f\"reading {k}: mean within 0.27 +- 0.17: {abs(m - 0.27) <= 0.17}; s.d. within 0.17 +- 0.017: {abs(sd - 0.17) <= 0.017}\")\nprint(\"\\nBy rat, reading a:\")\nprint(fields.groupby(\"rat\").a_contiguous_pref.agg([\"mean\", \"std\", \"size\"]).round(3).to_string())\nprint(\"By session, reading a:\")\nprint(fields.groupby(\"session\").a_contiguous_pref.agg([\"mean\", \"std\", \"size\"]).round(3).to_string())\nfor thr in (0.5, 2.0):\n    sel = [r for r in rows]  # same units, other peak thresholds below\nsub = []\nfor thr in (0.0, 0.5, 1.0, 2.0, 5.0):\n    vals = []\n    for s in analysed:\n        for u, mm in maps[s[\"session\"]].items():\n            pk = {sd: mm[sd].max() for sd in mm}\n            if max(pk.values()) >= thr and max(pk.values()) > 0:\n                vals.append(pfc.field_size(mm[max(pk, key=pk.get)]))\n    sub.append({\"min_peak_hz\": thr, \"units\": len(vals), \"mean\": np.mean(vals), \"sd\": np.std(vals, ddof=1)})\nprint(\"\\nReading a with other peak-rate thresholds:\")\nprint(pd.DataFrame(sub).round(3).to_string(index=False))\nfig, ax = plt.subplots(figsize=(5, 3))\nax.hist(fields.a_contiguous_pref, bins=np.linspace(0, 1, 21), color=\"0.4\")\nax.set_xlabel(\"field size (normalized length), reading a\")\nax.set_ylabel(\"units\")\nplt.show()\nprint(\"Plotted range:\", fields.a_contiguous_pref.min(), \"to\", fields.a_contiguous_pref.max(), \"(all within the axis)\")\n\"\"\", tags=[\"claim:fig2-field-size\"])\n\nresult(\"fig2-field-size\")\n\n# ---------------------------------------------------------------------------------------------\nmd(\"\"\"\n## fig2b-trajectory-selective\n\n> The fraction of neurons with significantly different firing on left and right trials is 16%\n> (layer 2/3) and 18% (layer 5) in the central arm (positions 0 to 0.3), where the trajectories\n> overlap, and 22% (layer 2/3) and 40% (layer 5) in the side arms (0.5 to 1).\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor si, s in enumerate(analysed):\n    rng = np.random.default_rng([2008, 2, si])\n    is_left = (s[\"trials\"].side == \"Left\").values\n    single = units[(units.session == s[\"session\"]) & (units.region == \"PFC\") & ~units.mua].unit.tolist()\n    for u in single:\n        pos, tr = pfc.positions_at(s, s[\"trains\"][u])\n        dens = pfc.trial_densities(pos, tr, len(is_left))\n        sig, _ = pfc.lr_test(dens, is_left, rng)\n        sig_sd, _ = pfc.lr_test(dens, is_left, rng, kind=\"sd\")\n        sig0, _ = pfc.lr_test(dens, rng.permutation(is_left), rng)\n        rows.append({\"session\": s[\"session\"], \"rat\": s[\"subject\"], \"unit\": u, \"peak_hz\": peak[(s[\"session\"], u)],\n                     \"central\": sig[pfc.GRID <= 0.3].any(), \"side\": sig[pfc.GRID >= 0.5].any(), \"any\": sig.any(),\n                     \"central_sd\": sig_sd[pfc.GRID <= 0.3].any(), \"side_sd\": sig_sd[pfc.GRID >= 0.5].any(),\n                     \"central_chance\": sig0[pfc.GRID <= 0.3].any(), \"side_chance\": sig0[pfc.GRID >= 0.5].any(),\n                     \"any_chance\": sig0.any()})\nlr = pd.DataFrame(rows)\nsel = lr[lr.peak_hz >= pfc.MIN_PEAK_HZ]\ncols = [\"central\", \"side\", \"central_chance\", \"side_chance\", \"central_sd\", \"side_sd\"]\nprint(\"Units with a peak of at least 1 Hz; percent selective, by rat:\")\nprint((100 * sel.groupby(\"rat\")[cols].mean()).round(1).join(sel.groupby(\"rat\").size().rename(\"units\")).to_string())\nprint(\"\\nBy session:\")\nprint((100 * sel.groupby(\"session\")[cols].mean()).round(1).join(sel.groupby(\"session\").size().rename(\"units\")).to_string())\npooled = 100 * sel[cols].mean()\nprint(\"\\nPooled (%):\", pooled.round(1).to_dict())\nrat_ok = {}\nfor rat, g in sel.groupby(\"rat\"):\n    c, sd = 100 * g.central.mean(), 100 * g.side.mean()\n    rat_ok[rat] = {\"central_in_range\": 14.4 <= c <= 19.8, \"side_layer\": \"2/3\" if 19.8 <= sd <= 24.2 else \"5\" if 36 <= sd <= 44 else \"none\"}\nprint(\"Per rat against the criterion:\", rat_ok)\ntable = [[int(sel.central.sum()), int((~sel.central).sum())], [int(sel.central_chance.sum()), int((~sel.central_chance).sum())]]\nprint(\"Central arm, real against chance: Fisher one-sided p =\", f\"{stats.fisher_exact(table, alternative='greater')[1]:.3g}\")\nprint(\"\\nAll PFC single units (no peak threshold), percent:\", (100 * lr[[\"central\", \"side\", \"any\"]].mean()).round(1).to_dict(), \"of\", len(lr))\n\"\"\", tags=[\"claim:fig2b-trajectory-selective\"])\n\nresult(\"fig2b-trajectory-selective\")\n\nmd(\"\"\"\n## traj-diverge\n\n> Left and right trajectories overlap in the central arm and begin to differ significantly at\n> position 0.3.\n\nBlocked: the two position series in the files are the x coordinates of the two LEDs (the second\nis zero throughout); the y coordinate, along which the side arms differ, is not in the dandiset.\n\"\"\")\n\n# ---------------------------------------------------------------------------------------------\nmd(\"\"\"\n## odor-nosepoke\n\n> About one quarter of the neurons fire at significantly different rates (P < 0.05 per cell)\n> during nose poking for the two odors.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor si, s in enumerate(analysed):\n    rng = np.random.default_rng([2008, 8, si])\n    tr = s[\"trials\"]\n    dur = (tr.run_start - tr.nosepoke_start).values\n    is_left = (tr.side == \"Left\").values\n    single = units[(units.session == s[\"session\"]) & (units.region == \"PFC\") & ~units.mua].unit.tolist()\n    for u in single:\n        st = s[\"trains\"][u]\n        c = np.searchsorted(st, tr.run_start.values) - np.searchsorted(st, tr.nosepoke_start.values)\n        if c.sum() < 10:\n            continue\n        r = c / dur\n        sh = rng.permutation(is_left)\n        rows.append({\"session\": s[\"session\"], \"rat\": s[\"subject\"], \"unit\": u,\n                     \"p\": stats.mannwhitneyu(r[is_left], r[~is_left]).pvalue,\n                     \"p_t\": stats.ttest_ind(r[is_left], r[~is_left]).pvalue,\n                     \"p_chance\": stats.mannwhitneyu(r[sh], r[~sh]).pvalue})\nodor = pd.DataFrame(rows)\nn_single = int(counts.loc[\"total\", \"a_single\"])\nprint(\"Units tested (at least 10 spikes in nose pokes):\", len(odor), \"of\", n_single)\nprint(\"Nose-poke duration (s): median\", round(float(np.median(np.concatenate([(s['trials'].run_start - s['trials'].nosepoke_start).values for s in analysed]))), 2))\nfrac = 100 * (odor.p < 0.05).mean()\nchance = 100 * (odor.p_chance < 0.05).mean()\nprint(f\"Mann-Whitney P < 0.05: {frac:.1f}%  (chance, relabelled trials: {chance:.1f}%)\")\nprint(f\"Variant, t-test P < 0.05: {100 * (odor.p_t < 0.05).mean():.1f}%\")\nprint(\"By rat (%):\", (100 * odor.groupby(\"rat\").p.apply(lambda p: (p < 0.05).mean())).round(1).to_dict())\nprint(\"By session (%):\", (100 * odor.groupby(\"session\").p.apply(lambda p: (p < 0.05).mean())).round(1).to_dict())\ntable = [[int((odor.p < 0.05).sum()), int((odor.p >= 0.05).sum())], [int((odor.p_chance < 0.05).sum()), int((odor.p_chance >= 0.05).sum())]]\nprint(\"Real against chance: Fisher one-sided p =\", f\"{stats.fisher_exact(table, alternative='greater')[1]:.3g}\")\nprint(\"Within 20 to 30%:\", 20 <= frac <= 30)\n\"\"\", tags=[\"claim:odor-nosepoke\"])\n\nresult(\"odor-nosepoke\")\n\n# ---------------------------------------------------------------------------------------------\nmd(\"\"\"\n## fig3-connection-rates\n\n> Of all ordered pairs of simultaneously recorded neurons, 0.79% had short-latency, narrow peaks or\n> troughs in their cross-correlograms (0.55% excitatory, 0.24% inhibitory), found with a jitter\n> test.\n\"\"\")\n\ncode(r\"\"\"\nt0 = time.time()\nconn, directed = {}, []\nfor si, s in enumerate(analysed):\n    rng = np.random.default_rng([2008, 9, si])\n    single = units[(units.session == s[\"session\"]) & (units.region == \"PFC\") & ~units.mua].unit.tolist()\n    c = pfc.connections(s, single, rng, check_sample=100)\n    conn[s[\"session\"]] = c\n    d = pfc.directed(c)\n    sh = units[units.session == s[\"session\"]].set_index(\"unit\").shank\n    d[\"session\"], d[\"rat\"] = s[\"session\"], s[\"subject\"]\n    d[\"dist_um\"] = 200 * np.abs(sh[d.pre].values - sh[d.post].values)\n    directed.append(d)\ndirected = pd.concat(directed, ignore_index=True)\ndirected[\"conn\"] = directed.exc | directed.inh\nrows = []\nfor name, c in conn.items():\n    d = directed[directed.session == name]\n    chk = c[c.check]\n    rows.append({\"session\": name, \"units\": len(set(c.a) | set(c.b)), \"ordered_pairs\": len(d),\n                 \"screened_unordered\": int(c[~c.check].screened.sum()), \"exc\": int(d.exc.sum()),\n                 \"exc_wider_than_2ms\": int((d.exc_any & ~d.exc).sum()), \"inh\": int(d.inh.sum()),\n                 \"check_sample\": len(chk),\n                 \"check_sample_significant\": int(chk[[\"exc_ab\", \"exc_ba\", \"inh_ab\", \"inh_ba\"]].fillna(False).astype(bool).any(axis=1).sum())})\nper = pd.DataFrame(rows)\nprint(per.to_string(index=False))\nn = len(directed)\nrates = {\"total\": 100 * directed.conn.mean(), \"excitatory\": 100 * directed.exc.mean(), \"inhibitory\": 100 * directed.inh.mean()}\nprint(f\"\\n{n} ordered pairs: connections {rates['total']:.3f}%, excitatory {rates['excitatory']:.3f}%, inhibitory {rates['inhibitory']:.3f}%\")\nfor k, (v, tol) in {\"total\": (0.79, 0.079), \"excitatory\": (0.55, 0.055), \"inhibitory\": (0.24, 0.024)}.items():\n    print(f\"  {k}: {rates[k]:.3f} against {v} +- {tol}: within {abs(rates[k] - v) <= tol}\")\ncs = set(map(tuple, directed.loc[directed.conn, [\"session\", \"pre\", \"post\"]].values))\nrecip = sum(1 for (se, a, b) in cs if (se, b, a) in cs) // 2\nprint(f\"Reciprocally connected unordered pairs: {recip}, {100 * recip / (n / 2):.3f}% of unordered pairs (paper 0.17%)\")\nprint(\"\\nBy rat (%):\")\nprint((100 * directed.groupby(\"rat\")[[\"conn\", \"exc\", \"inh\"]].mean()).round(3).join(directed.groupby(\"rat\").size().rename(\"pairs\")).to_string())\nsame = directed.dist_um == 0\nprint(\"\\nSame shank (%):\", (100 * directed[same][[\"exc\", \"inh\"]].mean()).round(3).to_dict(),\n      \"; different shanks (%):\", (100 * directed[~same][[\"exc\", \"inh\"]].mean()).round(3).to_dict())\nprint(\"Variant, peaks of any width counted as excitatory:\", f\"{100 * directed.exc_any.mean():.3f}%\")\nprint(f\"time {time.time() - t0:.0f} s\")\n\"\"\", tags=[\"claim:fig3-connection-rates\"])\n\nresult(\"fig3-connection-rates\")\n\n# ---------------------------------------------------------------------------------------------\nmd(\"\"\"\n## fig3-cell-classes\n\n> By their connections, 32.5% of units are putative pyramidal cells and 12.5% putative\n> interneurons, a ratio of 2.82 plus or minus 0.51 (s.d.), and 50.7% of the postsynaptic targets\n> of putative excitatory cells themselves inhibit other neurons.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor s in analysed:\n    d = directed[directed.session == s[\"session\"]]\n    single = units[(units.session == s[\"session\"]) & (units.region == \"PFC\") & ~units.mua].unit.tolist()\n    for u in single:\n        e, i = d[d.pre == u].exc.any(), d[d.pre == u].inh.any()\n        rows.append({\"session\": s[\"session\"], \"rat\": s[\"subject\"], \"unit\": u, \"pyr\": e and not i, \"int\": i and not e, \"both\": e and i})\ncells = pd.DataFrame(rows)\nprint(f\"PFC single units {len(cells)}: putative pyramidal {100 * cells.pyr.mean():.1f}%, putative interneurons \"\n      f\"{100 * cells.int.mean():.1f}%, both kinds of outgoing connection {int(cells.both.sum())} units\")\ng = cells.groupby(\"session\")[[\"pyr\", \"int\", \"both\"]].sum()\ng[\"ratio\"] = g.pyr / g.int.replace(0, np.nan)\nprint(g.to_string())\ngr = cells.groupby(\"rat\")[[\"pyr\", \"int\"]].sum()\nratios = {\"a_mean_of_sessions\": g.ratio.mean(), \"a_sd\": g.ratio.std(), \"b_pooled\": cells.pyr.sum() / cells.int.sum(),\n          \"c_mean_of_rats\": (gr.pyr / gr.int.replace(0, np.nan)).mean()}\nprint(\"Ratios:\", {k: round(v, 2) for k, v in ratios.items()}, \"; per rat:\", (gr.pyr / gr.int.replace(0, np.nan)).round(2).to_dict())\ninter = set(map(tuple, cells[cells.int][[\"session\", \"unit\"]].values))\ntargets = directed[directed.exc][[\"session\", \"post\"]].drop_duplicates()\ntfrac = 100 * np.mean([(a, b) in inter for a, b in targets.values])\ninhib_any = set(map(tuple, directed[directed.inh][[\"session\", \"pre\"]].values))\ntfrac_any = 100 * np.mean([(a, b) in inhib_any for a, b in targets.values])\nprint(f\"Targets of excitatory connections: {len(targets)} units, {tfrac:.1f}% putative interneurons \"\n      f\"({tfrac_any:.1f}% with any inhibitory outgoing connection)\")\nchecks = {\"pyramidal\": abs(100 * cells.pyr.mean() - 32.5) <= 3.25, \"interneurons\": abs(100 * cells.int.mean() - 12.5) <= 1.25,\n          \"ratio_a\": abs(ratios[\"a_mean_of_sessions\"] - 2.82) <= 0.51, \"ratio_b\": abs(ratios[\"b_pooled\"] - 2.82) <= 0.51,\n          \"ratio_c\": abs(ratios[\"c_mean_of_rats\"] - 2.82) <= 0.51, \"targets\": abs(tfrac - 50.7) <= 5.07}\nprint(\"Within tolerance:\", checks)\nprint(\"\\nInhibitory connections by the presynaptic unit's class:\",\n      directed[directed.inh].merge(cells, left_on=[\"session\", \"pre\"], right_on=[\"session\", \"unit\"]).pipe(\n          lambda d: {\"interneuron\": int(d.int.sum()), \"both\": int(d.both.sum())}))\nprint(\"Inhibitory connections on the same shank:\", int((directed.inh & (directed.dist_um == 0)).sum()), \"of\", int(directed.inh.sum()))\n\"\"\", tags=[\"claim:fig3-cell-classes\"])\n\nresult(\"fig3-cell-classes\")\n\n# ---------------------------------------------------------------------------------------------\nmd(\"\"\"\n## fig3f-distance\n\n> Most connected pairs were recorded on the same shank, and the probability of a connection falls\n> with the distance between the neurons, though connections were found up to 1200 micrometres\n> apart.\n\"\"\")\n\ncode(r\"\"\"\nsame = directed.dist_um == 0\ntab = [[int(directed.conn[same].sum()), int((~directed.conn[same]).sum())],\n       [int(directed.conn[~same].sum()), int((~directed.conn[~same]).sum())]]\nodds, p_f = stats.fisher_exact(tab)\nprob = directed.groupby(\"dist_um\").conn.agg([\"mean\", \"sum\", \"size\"])\nprob[\"mean\"] *= 100\nprint(\"Connection probability (%) by distance:\")\nprint(prob.round(3).to_string())\nrho, p_s = stats.spearmanr(prob.index, prob[\"mean\"])\nprint(f\"\\nSame shank {100 * directed.conn[same].mean():.2f}% against different shanks {100 * directed.conn[~same].mean():.2f}%: \"\n      f\"Fisher p = {p_f:.3g}\")\nprint(f\"Spearman correlation over distances 0 to 1400 um: rho = {rho:.3f}, p = {p_s:.3g}\")\nprint(\"Largest distance of a connection (um):\", int(directed[directed.conn].dist_um.max()),\n      \"; connections at 1000 um or more:\", int((directed.conn & (directed.dist_um >= 1000)).sum()))\nprint(f\"Share of connections on the same shank: {100 * (directed.conn & same).sum() / directed.conn.sum():.1f}%\")\nfor sub in (\"exc\", \"inh\"):\n    pr = directed.groupby(\"dist_um\")[sub].mean()\n    r, p = stats.spearmanr(pr.index, pr.values)\n    print(f\"Variant, {sub} only: rho = {r:.3f}, p = {p:.3g}\")\npr = prob[prob.index <= 1200]\nr, p = stats.spearmanr(pr.index, pr[\"mean\"])\nprint(f\"Variant, distances 0 to 1200 um only: rho = {r:.3f}, p = {p:.3g}\")\n\"\"\", tags=[\"claim:fig3f-distance\"])\n\nresult(\"fig3f-distance\")\n\n# ---------------------------------------------------------------------------------------------\nmd(\"\"\"\n## fig4-position-dependence\n\n> Out of 343 excitatory monosynaptic pairs, 67 showed position dependence of their short-latency\n> coincidences in the maze (P < 0.01), beyond what the firing rates explain.\n\nThe Methods' rank-based global band cannot reach a one-sided level of 0.01 here: with 1000\nsurrogates and a smooth statistic on 101 points, more than 1% of the data sets reach the most\nextreme rank somewhere on the track, so the band is empty and nothing can be significant. The\nmain test uses bands of the surrogate mean plus c times its s.d., with c searched as the Methods\nsearch the band; the rank version is shown as a variant.\n\"\"\")\n\ncode(r\"\"\"\nt0 = time.time()\nexc = directed[directed.exc].reset_index(drop=True)\nrows = []\nfor k, r in exc.iterrows():\n    s = by_name[r.session]\n    rng = np.random.default_rng([2008, 12, k])\n    is_left = (s[\"trials\"].side == \"Left\").values\n    both = pfc.coincidence_test(s, r.pre, r.post, rng)\n    left = pfc.coincidence_test(s, r.pre, r.post, rng, is_left)\n    right = pfc.coincidence_test(s, r.pre, r.post, rng, ~is_left)\n    rows.append({\"session\": r.session, \"pre\": r.pre, \"post\": r.post, \"coincidences\": both[\"n_coincidences\"],\n                 \"a_sig\": both[\"sd_sig\"], \"a_fraction\": both[\"sd_fraction\"],\n                 \"b_sig\": left[\"sd_sig\"] or right[\"sd_sig\"],\n                 \"a_rank\": both[\"rank_sig\"], \"b_rank\": left[\"rank_sig\"] or right[\"rank_sig\"]})\npos_dep = pd.DataFrame(rows)\nprint(\"Excitatory pairs:\", len(pos_dep), \"; coincidences in runs per pair: median\", pos_dep.coincidences.median(),\n      \", range\", pos_dep.coincidences.min(), \"to\", pos_dep.coincidences.max())\nfor kcol, name in ((\"a_sig\", \"a, left and right together\"), (\"b_sig\", \"b, left or right\"),\n                   (\"a_rank\", \"variant, rank band, together\"), (\"b_rank\", \"variant, rank band, left or right\")):\n    print(f\"{name}: {int(pos_dep[kcol].sum())} pairs, {100 * pos_dep[kcol].mean():.1f}%\")\nprint(\"Within 19.5 +- 1.95%:\", {k: abs(100 * pos_dep[k].mean() - 19.5) <= 1.95 for k in (\"a_sig\", \"b_sig\")})\nprint(\"Fraction of the track significant, pairs significant under a:\", pos_dep.a_fraction[pos_dep.a_sig].round(3).tolist())\nprint(\"By session (% under a):\", (100 * pos_dep.groupby(\"session\").a_sig.mean()).round(1).to_dict())\nfor lo in (50, 100):\n    sub = pos_dep[pos_dep.coincidences >= lo]\n    print(f\"Pairs with at least {lo} coincidences: {len(sub)}, significant under a: {100 * sub.a_sig.mean() if len(sub) else float('nan'):.1f}%\")\nprint(f\"time {time.time() - t0:.0f} s\")\n\"\"\", tags=[\"claim:fig4-position-dependence\"])\n\nresult(\"fig4-position-dependence\")\n\n# ---------------------------------------------------------------------------------------------\nmd(\"\"\"\n## fig6-facilitation-depression\n\n> About equal fractions of connected pairs show firing pattern-dependent depression (12.7%) and\n> facilitation (10.7%), comparing the transmission of the first spike of a train with that of\n> later spikes.\n\"\"\")\n\ncode(r\"\"\"\nt0 = time.time()\nrows = []\nfor k, r in exc.iterrows():\n    s = by_name[r.session]\n    rng = np.random.default_rng([2008, 13, k])\n    rows.append({\"session\": r.session, \"pre\": r.pre, \"post\": r.post,\n                 **pfc.first_vs_later(s[\"trains\"][r.pre], s[\"trains\"][r.post], rng)})\nfl = pd.DataFrame(rows)\nok = fl[(fl.n_first >= 20) & (fl.n_later >= 20)].copy()\nok[\"depressing\"] = (ok.p < 0.10) & (ok[\"diff\"] > 0)\nok[\"facilitating\"] = (ok.p < 0.10) & (ok[\"diff\"] < 0)\ndep, fac = 100 * ok.depressing.mean(), 100 * ok.facilitating.mean()\nprint(f\"Excitatory pairs {len(fl)}, with at least 20 first and 20 later spikes {len(ok)}\")\nprint(f\"Depressing {int(ok.depressing.sum())} ({dep:.1f}%), facilitating {int(ok.facilitating.sum())} ({fac:.1f}%)\")\nprint(\"Within tolerance:\", {\"depressing\": abs(dep - 12.7) <= 1.27, \"facilitating\": abs(fac - 10.7) <= 1.07})\nfor name, col in ((\"depressing\", \"depressing\"), (\"facilitating\", \"facilitating\")):\n    p = stats.binomtest(int(ok[col].sum()), len(ok), 0.05, alternative=\"greater\").pvalue\n    print(f\"{name} above 5%: binomial p = {p:.3g}\")\nprint(\"Median transmission per presynaptic spike: first\", round(ok.eff_first.median(), 4), \", later\", round(ok.eff_later.median(), 4),\n      \"; Wilcoxon of first minus later: p =\", f\"{stats.wilcoxon(ok['diff']).pvalue:.3g}\")\nprint(\"By session:\", ok.groupby(\"session\")[[\"depressing\", \"facilitating\"]].sum().to_dict())\nfor lo in (50, 200):\n    sub = ok[(ok.n_first >= lo) & (ok.n_later >= lo)]\n    print(f\"Pairs with at least {lo} of each: {len(sub)}, depressing {100 * sub.depressing.mean():.1f}%, facilitating {100 * sub.facilitating.mean():.1f}%\")\nprint(f\"time {time.time() - t0:.0f} s\")\n\"\"\", tags=[\"claim:fig6-facilitation-depression\"])\n\nresult(\"fig6-facilitation-depression\")\n\n# ---------------------------------------------------------------------------------------------\nmd(\"\"\"\n## fig7-supralinear\n\n> Coincident firing of two or more presynaptic neurons within 5 ms on a common target is more\n> effective than the sum of their separate effects (supralinear), while spikes spread over windows\n> longer than 10 ms add linearly.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor name in exc.session.unique():\n    s = by_name[name]\n    e = exc[exc.session == name]\n    for post, g in e.groupby(\"post\"):\n        if len(g) < 2:\n            continue\n        pres = [s[\"trains\"][p] for p in g.pre]\n        for w in (0.005, 0.02):\n            cg = pfc.coincidence_gain(pres, s[\"trains\"][post], s[\"duration\"], w).set_index(\"n_partners\")\n            row = {\"session\": name, \"post\": post, \"partners\": len(g), \"window_ms\": int(w * 1000)}\n            for n_p in (1, 2, 3):\n                row[f\"excess_{n_p}\"] = cg.excess.get(n_p, np.nan)\n                row[f\"events_{n_p}\"] = int(cg.events.get(n_p, 0))\n            rows.append(row)\nsat = pd.DataFrame(rows)\nprint(\"Satellites (targets with at least two excitatory partners):\", int((sat.window_ms == 5).sum()))\nfor w in (5, 20):\n    g = sat[(sat.window_ms == w) & (sat.events_2 >= 20)].copy()\n    g[\"supra\"] = g.excess_2 - 2 * g.excess_1\n    p = stats.wilcoxon(g.supra, alternative=\"greater\").pvalue if len(g) else np.nan\n    print(f\"\\n{w} ms events: {len(g)} satellites with at least 20 two-partner events; supralinear in {int((g.supra > 0).sum())} \"\n          f\"({100 * (g.supra > 0).mean():.0f}%); median excess one partner {g.excess_1.median():.4f}, two partners \"\n          f\"{g.excess_2.median():.4f}; Wilcoxon (two > twice one) p = {p:.3g}\")\n    three = g[g.events_3 >= 20]\n    if len(three):\n        print(f\"  with at least 20 three-partner events: {len(three)}; median excess three partners {three.excess_3.median():.4f}\")\nprint(sat[sat.window_ms == 5].round(4).to_string(index=False))\n\"\"\", tags=[\"claim:fig7-supralinear\"])\n\nresult(\"fig7-supralinear\")\n\n# ---------------------------------------------------------------------------------------------\nmd(\"\"\"\n## fig3-trajectory-by-class\n\n> Large fractions of putative pyramidal cells (72.2% in layer 2/3, 84.7% in layer 5) and of\n> interneurons (58.3% and 83%) are trajectory specific.\n\"\"\")\n\ncode(r\"\"\"\nm = cells.merge(lr[[\"session\", \"unit\", \"any\", \"any_chance\"]], on=[\"session\", \"unit\"])\nrows = []\nfor rat, g in m.groupby(\"rat\"):\n    rows.append({\"rat\": rat, \"pyramidal\": int(g.pyr.sum()), \"pyr_specific_pct\": 100 * g[g.pyr][\"any\"].mean() if g.pyr.any() else np.nan,\n                 \"interneurons\": int(g.int.sum()), \"int_specific_pct\": 100 * g[g.int][\"any\"].mean() if g.int.any() else np.nan,\n                 \"chance_pct\": 100 * g.any_chance.mean()})\nbyclass = pd.DataFrame(rows)\nprint(byclass.round(1).to_string(index=False))\ndef layer_match(p, i):\n    out = []\n    for name, (vp, vi) in {\"2/3\": (72.2, 58.3), \"5\": (84.7, 83.0)}.items():\n        if abs(p - vp) <= 0.1 * vp and abs(i - vi) <= 0.1 * vi:\n            out.append(name)\n    return out\nprint(\"Layer readings matched per rat:\", {r.rat: layer_match(r.pyr_specific_pct, r.int_specific_pct) for r in byclass.itertuples()})\nprint(\"All units, trajectory specific (%):\", round(100 * m[\"any\"].mean(), 1), \"; chance:\", round(100 * m.any_chance.mean(), 1))\n\"\"\", tags=[\"claim:fig3-trajectory-by-class\"])\n\nresult(\"fig3-trajectory-by-class\")\n\nmd(\"\"\"\n## ee188-example-session\n\n> In the example layer 2/3 session, 117 neurons gave 1172 pairs with 48 excitatory and 30\n> inhibitory connections, 39 of the 117 cells formed one connected hub, and the example pairs show\n> position-dependent, depressing, facilitating and supralinear transmission.\n\nBlocked: the CRCNS description names EE.188 as the session of Figures 2a and 3d, and the\ndandiset holds no file of that session (nor of EE.152 or EE.165).\n\"\"\")\n\ncode(r\"\"\"\nprint(f\"Notebook ran in {time.time() - started:.0f} s\")\n\"\"\")\n\nmd(RESULTS.get(\"summary\", \"## Summary\\n\\nTODO\"))\n\nnb[\"cells\"] = cells\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbf.write(nb, \"entries/000067-fujisawa-2008/reproduce_fujisawa_2008.ipynb\")\nprint(\"cells\", len(cells))\n"
}
```

```
File created successfully at: /tmp/claude-1001/make_nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001; python - <<'E'
s=open('make_nb.py').read()
s=s.replace('''for thr in (0.5, 2.0):
    sel = [r for r in rows]  # same units, other peak thresholds below
''','')
open('make_nb.py','w').write(s)
E
. $TMPDIR/scratch/bin/activate; uv pip install -q nbformat 2>&1|tail -1; python make_nb.py
```

```
cells 59
Shell cwd was reset to
```

**Agent**

Now the entry metadata, requirements, and lock.

**Agent calls Bash**

```bash
cd entries/000067-fujisawa-2008; cat > requirements.in <<'E'
dandi
h5py
matplotlib
numpy
pandas
remfile
scipy
E
cat > entry.yaml <<'E'
schema_version: 1
name: 000067-fujisawa-2008
type: reproduction
title: Prefrontal assemblies and monosynaptic dynamics in a working memory task (Fujisawa et al. 2008)
description: Tests the findings of Fujisawa, Amarasingham, Harrison and Buzsaki (2008) on dandiset
  000067, which holds recordings of three rats from a 64-site prefrontal probe and a CA1 probe
  during an odor-place matching task. Units are placed on the probes from their waveforms in the
  wideband signal. It tests the population activity, field sizes and trajectory selectivity of
  prefrontal neurons, monosynaptic connections found with a jitter test, the cell classes and
  distances they imply, and the task dependence, short-term plasticity and summation of the
  connections. The paper's example session and fourth rat are not in the dandiset.
license: Apache-2.0
notebooks:
- path: reproduce_fujisawa_2008.ipynb
  title: Reproducing Fujisawa et al. (2008) from dandiset 000067
  runtime_minutes: 12
helpers:
- pfc.py
related:
- id: dandi:000067/0.250624.0419
  relation: uses_data
- id: doi:10.1038/nn.2134
  relation: reproduces
E
cat ../../schemas/entry.schema.json | python -c "import json,sys;d=json.load(sys.stdin);print(list(d['properties']));print(d['properties']['related'])" ; cd ../..; python tools/entry.py lock entries/000067-fujisawa-2008 2>&1 | tail -5
```

```
['schema_version', 'name', 'type', 'title', 'description', 'license', 'notebooks', 'helpers', 'related']
{'type': 'array', 'minItems': 1, 'items': {'type': 'object', 'additionalProperties': False, 'required': ['id', 'relation'], 'properties': {'id': {'description': 'dandi:<id>[/<version>], doi:<doi>, or entry:<name>.', 'type': 'string', 'pattern': '^(dandi:[0-9]{6}(/.+)?|doi:10\\.[0-9]{4,9}/.+|entry:[a-z0-9]+(-[a-z0-9]+)*)$'}, 'relation': {'enum': ['uses_data', 'reproduces', 'derived_from', 'references']}}}}
wrote entries/000067-fujisawa-2008/requirements.lock.txt
```

**Agent calls Bash**

```bash
cd  python tools/entry.py check entries/000067-fujisawa-2008 2>&1 | tail -20
```

```
0 error(s)
```

**Agent calls Bash**

```bash
cd  time python tools/entry.py run entries/000067-fujisawa-2008 2>&1 | tail -30
```

```
Installed kernelspec registry-000067-fujisawa-2008 in executed/000067-fujisawa-2008/.venv/share/jupyter/kernels/registry-000067-fujisawa-2008
pass  reproduce_fujisawa_2008.ipynb  (606 s)

real	10m10.004s
user	6m51.646s
sys	0m24.536s
```

**Agent**

It ran in about 10 minutes. Reading the outputs.

**Agent calls Bash**

```bash
cd  ls executed/000067-fujisawa-2008/; python - <<'E'
import json
nb=json.load(open('executed/000067-fujisawa-2008/reproduce_fujisawa_2008.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    print(f'==== cell {i}', c['metadata'].get('tags'))
    for o in c.get('outputs',[]):
        if 'text' in o: print(''.join(o['text'])[:6000])
        elif 'data' in o and 'text/plain' in o['data']: print(''.join(o['data']['text/plain'])[:300])
E
```

```
<persisted-output>
Output too large (31.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/c499576e-dbd4-49be-9a39-3fcbda08dcd8/tool-results/bf9r4dlet.txt

Preview (first 2KB):
reproduce_fujisawa_2008.ipynb
result.json
==== cell 1 None
28 files described and 9 working memory sessions loaded from dandiset 000067 version 0.250624.0419 in 436 s

==== cell 3 ['sanity']
Versions: ['draft', '0.210812.1457', '0.250624.0419']
  draft: 28 assets, 94.6 GB, identical to 0.250624.0419: True
  0.210812.1457: 28 assets, 94.6 GB, identical to 0.250624.0419: True
  0.250624.0419: 28 assets, 94.6 GB, identical to 0.250624.0419: True

Every file (raw_s, lfp_s: duration of the wideband and LFP series in seconds):
session subject      start  channels locations  groups  xyz_all_nan     raw_s     lfp_s  units  unit_columns  spikes  trials  position
 EE.042      EE 2008-06-22       104 [unknown]      13         True    0.0000  993.0000      0            []       0       0     False
 EE.043      EE 2008-06-22       104 [unknown]      13         True    1.6384    1.6384      0            []       0       0     False
 EE.044      EE 2008-06-22       104 [unknown]      13         True    1.3000    1.3000      0            []       0       0     False
[... 8 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/c499576e-dbd4-49be-9a39-3fcbda08dcd8/tool-results/bf9r4dlet.txt",
 "offset": 40
}
```

```
40	 GG.097      GG 2008-04-01       101 [unknown]      13         True 1750.0000 1750.0000     69 [spike_times]  526073      38      True
41	 GG.149      GG 2008-04-06       101 [unknown]      13         True 2846.2000 2846.2000     63 [spike_times]  721786      31      True
42	
43	Subjects: {'EE': 21, 'GG': 4, 'FF': 3}
44	Channel locations: ['unknown'] ; electrode x, y, z all NaN in every file: True ; electrode groups per file: [np.int64(13)]
45	Unit table columns: ['spike_times']
46	
47	Files sharing the first second of LFP (channel 1): none
48	Files sharing their first 50 spike times: none
49	
50	==== cell 5 ['sanity']
51	session  trials  left  right  poke_s_median  run_s_median  reward_after_stop  d_at_run_start  d_at_run_end  run_frames_d>0  frames_d>0_outside_trials  lin_min  lin_max lin_unit         x1_range  x2_all_zero pos_unit  duration_s
52	 EE.049      19     9     10          3.282         9.894               True           0.000         1.964           0.850                      0.029      0.0      2.0   meters    (-1.0, 564.0)         True   meters      1788.8
53	 EE.088      31    11     20          2.657         5.005               True           1.041         0.000           0.986                      0.072      0.0      2.0   meters    (-1.0, 284.0)         True   meters      2165.1
54	 EE.196      48    21     27          4.551         4.593               True           1.022         0.000           0.971                      0.093      0.0      2.0   meters (-1.0, 592.2105)         True   meters      2844.3
55	 FF.103      39    19     20          0.842         6.579               True           1.025         0.000           0.990                      0.122      0.0      2.0   meters (-1.0, 605.4951)         True   meters      2866.8
56	 FF.130      46    23     23          1.366         6.037               True           1.024         0.000           0.986                      0.068      0.0      2.0   meters    (-1.0, 610.0)         True   met
[... 400 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000067-fujisawa-2008; . $TMPDIR/scratch/bin/activate; python - <<'E'
import pickle, sys, numpy as np, pandas as pd
sys.path.insert(0,'.'); import pfc
S=pickle.load(open('/tmp/claude-1001/S.pkl','rb')); s=[x for x in S if x['session']=='EE.049'][0]
tr=s['trials']; lin=s['lin']; r=s['lin_rate']
for k in range(5):
    a,b,c=tr.nosepoke_start[k],tr.run_start[k],tr.run_end[k]
    i0,i1,i2=int(a*r),int(b*r),int(c*r)
    print(k,tr.side[k],round(a,2),round(b,2),round(c,2), 'd around run_start',np.round(lin[i1-3:i1+4],2),'d around end',np.round(lin[i2-4:i2+3],2))
    seg=lin[i1:i2]; print('   frac>0 in run',np.mean(seg>0), 'first >0 at', np.argmax(seg>0)/r, 's; max', seg.max())
E
```

```
0 Left 64.06 88.14 104.74 d around run_start [0. 0. 0. 0. 0. 0. 0.] d around end [1.98 1.98 1.98 1.98 0.   0.   0.  ]
   frac>0 in run 0.9137134052388289 first >0 at 0.2816 s; max 1.9816257706059126
1 Right 311.09 313.17 321.8 d around run_start [1.02 1.02 1.02 1.02 1.02 1.02 1.02] d around end [1.99 1.99 1.99 1.99 0.   0.   0.  ]
   frac>0 in run 0.8902077151335311 first >0 at 0.0 s; max 1.9929339142747837
2 Right 348.96 350.2 358.46 d around run_start [0.   0.   0.   0.   0.   0.   1.02] d around end [1.97 1.97 1.97 1.97 0.   0.   0.  ]
   frac>0 in run 0.7863777089783281 first >0 at 0.0768 s; max 1.9705309685762469
3 Left 391.88 409.93 445.35 d around run_start [0. 0. 0. 0. 0. 0. 0.] d around end [1.93 1.93 1.94 1.94 0.   0.   0.  ]
   frac>0 in run 0.934971098265896 first >0 at 0.5632 s; max 1.946341294118806
4 Left 491.3 494.59 503.6 d around run_start [1.04 1.04 1.04 1.04 1.04 1.04 1.04] d around end [1.97 1.97 1.97 1.97 0.   0.   0.  ]
   frac>0 in run 0.8323863636363636 first >0 at 0.0 s; max 1.9711479648726233
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001; python - <<'E'
s=open('make_nb.py').read()
old=s[s.index('''    in_run = np.zeros(len(t), bool)'''):s.index('''        "lin_min": s["lin"].min()''')]
new='''    in_run = np.zeros(len(t), bool)
    in_trial = np.zeros(len(t), bool)
    first_d, last_d = [], []
    for a0, a, b in zip(tr.nosepoke_start, tr.run_start, tr.run_end):
        m = (t >= a) & (t <= b)
        in_run |= m
        in_trial |= (t >= a0) & (t <= b)
        d = s["lin"][m]
        if (d > 0).any():
            first_d.append(d[d > 0][0])
            last_d.append(d[d > 0][-1])
    rows.append({
        "session": s["session"], "trials": len(tr), "left": int((tr.side == "Left").sum()),
        "right": int((tr.side == "Right").sum()),
        "poke_s_median": np.median(tr.run_start - tr.nosepoke_start),
        "run_s_median": np.median(tr.run_end - tr.run_start),
        "reward_after_stop": bool((tr.run_end > tr.run_start).all()),
        "first_d_in_run": np.median(first_d), "last_d_in_run": np.median(last_d),
        "run_frames_d>0": np.mean(s["lin"][in_run] > 0), "frames_d>0_outside_trials": np.mean(s["lin"][~in_trial] > 0),
'''
s=s.replace(old,new)
s=s.replace('''    start_frame = np.round(tr.run_start.values * s["lin_rate"]).astype(int)
    end_frame = np.round(tr.run_end.values * s["lin_rate"]).astype(int) - 1
''','')
s=s.replace('''far = table[[c for c in table.columns if c <= -10]].mean(1)
near = table[[c for c in table.columns if 0 <= c <= 4]].mean(1)''','''far = table[[c for c in table.columns if c <= -10]].mean(axis=1)
near = table[[c for c in table.columns if 0 <= c <= 4]].mean(axis=1)''')
s=s.replace('''print(edges.groupby("session").apply(lambda d: pd.Series({
    "onset_vs_poke_start": crossing(d, "at_poke_start", True),
    "offset_vs_poke_end": crossing(d, "at_poke_end", False)})).round(3).to_string())''','''def at(d, col, lag):
    return d[col].values[np.argmin(np.abs(d.lag_s.values - lag))]
print(edges.groupby("session").apply(lambda d: pd.Series({
    "onset_vs_poke_start": crossing(d, "at_poke_start", True),
    "offset_vs_poke_end": crossing(d, "at_poke_end", False),
    "level_0.5s_before_start": at(d, "at_poke_start", -0.5), "level_0.5s_after_start": at(d, "at_poke_start", 0.5),
    "level_0.5s_before_end": at(d, "at_poke_end", -0.5), "level_0.5s_after_end": at(d, "at_poke_end", 0.5)})).round(3).to_string())''')
open('make_nb.py','w').write(s)
E
grep -n "first_d_in_run\|level_0.5s" make_nb.py | head
```

```
184:        "first_d_in_run": np.median(first_d), "last_d_in_run": np.median(last_d),
304:    "level_0.5s_before_start": at(d, "at_poke_start", -0.5), "level_0.5s_after_start": at(d, "at_poke_start", 0.5),
305:    "level_0.5s_before_end": at(d, "at_poke_end", -0.5), "level_0.5s_after_end": at(d, "at_poke_end", 0.5)})).round(3).to_string())
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/000067-fujisawa-2008; . $TMPDIR/scratch/bin/activate; python - <<'E'
import pickle, sys, numpy as np, pandas as pd
sys.path.insert(0,'.'); import pfc
S=pickle.load(open('/tmp/claude-1001/S.pkl','rb'))
for s in S:
    tr=s['trials']; t=pfc.frame_times(s)
    in_run=np.zeros(len(t),bool); in_trial=np.zeros(len(t),bool); f=[];l=[]
    for a0,a,b in zip(tr.nosepoke_start,tr.run_start,tr.run_end):
        m=(t>=a)&(t<=b); in_run|=m; in_trial|=(t>=a0)&(t<=b); d=s['lin'][m]
        if (d>0).any(): f.append(d[d>0][0]); l.append(d[d>0][-1])
    e=pfc.sensor_edges(s)
    g=lambda c,x: e[c].values[np.argmin(np.abs(e.lag_s.values-x))]
    print(s['session'],round(np.median(f),3),round(np.median(l),3),round(np.mean(s['lin'][in_run]>0),3),round(np.mean(s['lin'][~in_trial]>0),3), [round(g('at_poke_start',-0.5),3),round(g('at_poke_start',0.5),3),round(g('at_poke_end',-0.5),3),round(g('at_poke_end',0.5),3)])
E
```

```
/tmp/claude-1001/scratch/lib/python3.13/site-packages/numpy/_core/fromnumeric.py:3862: RuntimeWarning: Mean of empty slice
  return _methods._mean(a, axis=axis, dtype=dtype,
/tmp/claude-1001/scratch/lib/python3.13/site-packages/numpy/_core/_methods.py:142: RuntimeWarning: invalid value encountered in scalar divide
  ret = ret.dtype.type(ret / rcount)
/tmp/claude-1001/scratch/lib/python3.13/site-packages/numpy/_core/fromnumeric.py:3862: RuntimeWarning: Mean of empty slice
  return _methods._mean(a, axis=axis, dtype=dtype,
/tmp/claude-1001/scratch/lib/python3.13/site-packages/numpy/_core/_methods.py:142: RuntimeWarning: invalid value encountered in scalar divide
  ret = ret.dtype.type(ret / rcount)
/tmp/claude-1001/scratch/lib/python3.13/site-packages/numpy/_core/fromnumeric.py:3862: RuntimeWarning: Mean of empty slice
  return _methods._mean(a, axis=axis, dtype=dtype,
/tmp/claude-1001/scratch/lib/python3.13/site-packages/numpy/_core/_methods.py:142: RuntimeWarning: invalid value encountered in scalar divide
  ret = ret.dtype.type(ret / rcount)
/tmp/claude-1001/scratch/lib/python3.13/site-packages/numpy/_core/fromnumeric.py:3862: RuntimeWarning: Mean of empty slice
  return _methods._mean(a, axis=axis, dtype=dtype,
/tmp/claude-1001/scratch/lib/python3.13/site-packages/numpy/_core/_methods.py:142: RuntimeWarning: invalid value encountered in scalar divide
  ret = ret.dtype.type(ret / rcount)
/tmp/claude-1001/scratch/lib/python3.13/site-packages/numpy/_core/fromnumeric.py:3862: RuntimeWarning: Mean of empty slice
  return _methods._mean(a, axis=axis, dtype=dtype,
/tmp/claude-1001/scratch/lib/python3.13/site-packages/numpy/_core/_methods.py:142: RuntimeWarning: invalid value encountered in scalar divide
  ret = ret.dtype.type(ret / rcount)
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000067-fujisawa-2008; . $TMPDIR/scratch/bin/activate; python - 2>/dev/null <<'E'
import pickle, sys, numpy as np, pandas as pd
sys.path.insert(0,'.'); import pfc
S=pickle.load(open('/tmp/claude-1001/S.pkl','rb'))
for s in S:
    arr=s['sensors']
    if s['subject']=='GG': s['sensors']={65:arr[:,1],64:arr[:,0]}
    else: s['sensors']={96:arr[:,0],97:arr[:,1]}
    e=pfc.sensor_edges(s)
    g=lambda c,x: round(float(e[c].values[np.argmin(np.abs(e.lag_s.values-x))]),3)
    print(s['session'],[g('at_poke_start',-0.5),g('at_poke_start',-0.01),g('at_poke_start',0.5),g('at_poke_end',-0.5),g('at_poke_end',0.01),g('at_poke_end',0.5)])
E
```

```
EE.049 [0.001, 0.001, 0.489, 0.689, 0.001, 0.001]
EE.088 [0.001, 0.001, 0.393, 0.692, 0.001, 0.001]
EE.196 [0.001, 0.001, 0.689, 0.842, 0.001, 0.001]
FF.103 [0.002, 0.002, 0.407, 0.456, 0.001, 0.001]
FF.130 [0.001, 0.001, 0.365, 0.285, 0.001, 0.001]
FF.167 [0.002, 0.002, 0.365, 0.389, 0.001, 0.001]
GG.069 [0.002, 0.002, 0.439, 0.233, 0.001, 0.002]
GG.097 [0.005, 0.002, 0.374, 0.17, 0.001, 0.001]
GG.149 [0.003, 0.004, 0.418, 0.451, 0.001, 0.002]
```

**Agent**

The clock checks hold in every session. Writing the conclusion cells, summary and data-check prose.

**Agent calls Bash**

```bash
cd /tmp/claude-1001; python - <<'E'
s=open('make_nb.py').read()
def rep(a,b):
    global s
    assert a in s, a[:60]
    s=s.replace(a,b)
rep('''All versions hold the same assets, so the pinned version's content is the content of every
version. The dandiset has three rats; the paper recorded four. Ten files have a trial table and
position. Session EE.088 and the eleven other sessions of its day have units but no wideband
signal, and the test sessions EE.043 and EE.044 last about a second.''','''All versions hold the same assets, so the pinned version's content is the content of every
version. The dandiset has three rats; the paper recorded four. Ten files have a trial table and
position, and twenty have units. EE.042 and the ten sessions of 2008-06-27 (EE.080 to EE.089,
EE.088 among them) have no wideband signal, and the test sessions EE.043 and EE.044 last under
two seconds.''')
rep('''The data agree: the linearized position is 1 at `stop_time` and 2 at `reward_time` (medians
printed above), it is above 0 in nearly every frame of the runs and almost never outside the
trials.''','''The data agree: the first tracked linearized position after `stop_time` is 1.02 to 1.05 and the
last before `reward_time` is 1.89 to 1.99 (medians over trials), the position is above 0 in 85%
(EE.049) to 99.6% of run frames, and in at most 0.5% of frames outside the trials (from the first
nose poke to the reward).''')
rep('''The CA1 channels have a theta ratio two to three times that of the prefrontal channels in every
session, as a hippocampal probe should. In rats EE and FF the CRCNS map holds: CA1 on 65 to 96,
sensors on 97 (right) and 98 (left). In rat GG it does not: channels 65 to 69 carry no theta,
the nose-poke sensors are on 65 and 66, and the CA1 probe is on 70 to 101; and the sensor at 65
is the one active on trials labelled Right, so either the sensors or the side labels of rat GG
are swapped relative to the other rats. The data cannot tell which. Left-right tests below do
not depend on which side is called left. The prefrontal probe is channels 1 to 64 in all three
rats (no theta).''','''The CA1 channels have a theta ratio about twice that of the prefrontal channels in every session
(0.37 to 0.54 against 0.16 to 0.27), as a hippocampal probe should. In rats EE and FF the CRCNS
map holds: CA1 on 65 to 96, the right and left sensors on 97 and 98 (agreement 0.97 to 1.00). In
rat GG it does not: channels 65 to 69 carry little theta (0.06 to 0.25), channels 97 and 98 are
not sensors (agreement 0.35 to 0.42), the CA1 probe is on 70 to 101, and the nose-poke sensors are
on 65 and 66, with 66 active on trials labelled Right (agreement 1.00). The order of the two
sensors, or the side labels, of rat GG is therefore reversed relative to rats EE and FF; the data
cannot tell which. The left-right tests below do not depend on which side is called left. The
prefrontal probe is channels 1 to 64 in all three rats.''')
rep('''The spikes share the clock of the wideband signal: the mean waveform at the spike times is several
times larger than with every spike moved by 3 ms. The trial table shares the clock of the
recorded signals: the trial's sensor turns on at the start of the first nose poke and off at the
end of the last, within a few tens of milliseconds in rats EE and FF (where the sensors are
strong). In rat GG the sensor signals are weak and the crossings are less precise.''','''The spikes share the clock of the wideband signal: the mean waveform at the spike times is 12 to
26 times larger than with every spike moved 3 ms later. The trial table shares the clock of the
recorded signals: in every session the trial's sensor turns on within 2 ms of the start of the
first nose poke and off within 2 ms of the end of the last, and it is off 0.5 s before the start
and 0.5 s after the end. The table's times were evidently taken from these sensor signals.''')
rep('''The side of the trial is decoded from PFC spikes in the second after the run starts and later
(accuracy 0.7 to 1.0 in most sessions), and much less well 10 to 20 s before it, when the rat is
between trials. So the spikes share the clock of the trial table, in every session.''','''The side of the trial is decoded from PFC spikes better from 0 to 4 s after the run starts than
10 to 20 s before it, between trials, in 7 of 8 sessions (for example EE.196, 0.96 against 0.67).
In GG.097 (19 units) the accuracy rises only at 6 s (0.84). With the sensor check above, this is
consistent with spikes, trials and positions sharing one clock in every session; for GG.097 it is
shown by the sensors and the waveforms, and only weakly by the spikes.''')
open('make_nb.py','w').write(s)
E
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001; sed -i 's/The CA1 channels have a theta ratio about twice that of the prefrontal channels in every session/The CA1 channels have a theta ratio 1.9 to 2.7 times that of the prefrontal channels in every session/' make_nb.py; grep -c "1.9 to 2.7 times" make_nb.py
```

```
1
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat > /tmp/claude-1001/results.json <<'E'
{
"channel-region-link": "**Result: partially reproduced.** Channels 1 to 64 carry the prefrontal probe in all three rats, and in rats EE and FF the CRCNS map holds in every session: the CA1 channels have the higher theta ratio and the sensors agree with the trial side on 0.97 to 1.00 of trials. In rat GG the CRCNS sensor channels agree on 0.35 to 0.42 of trials. With the sensors on channels 65 and 66 (right on 66) and the CA1 probe on 70 to 101, both checks hold in every session (agreement 1.00).",
"rats-and-units": "**Result: not reproduced.** The dandiset holds three rats, against the paper's four. The eight sessions hold 417 PFC single units (346 with a peak of at least 1 Hz, 491 counting multi-unit clusters), all outside 633 plus or minus 63. The 350 units of EE.088 cannot be placed on a probe.",
"fig2c-active-fraction": "**Result: not reproduced.** The per-rat medians are 10.2% (EE), 19.7% (FF) and 6.2% (GG): EE matches the layer 2/3 value and FF the layer 5 value, but GG matches neither. Along the track the fraction varies by a factor of 1.16 to 1.88 in seven sessions and 2.57 in GG.149, above the threshold of 2. Neither part of the criterion holds for all rats, though both hold for rats EE and FF.",
"fig2-field-size": "**Result: partially reproduced.** The mean field size is 0.270 over 346 units, the paper's value, but the s.d. is 0.196, outside 0.17 plus or minus 0.017. Readings b and c give means of 0.281 and 0.331 with s.d. of 0.206 and 0.220. For peak thresholds from 0 to 5 Hz the s.d. is 0.189 to 0.243. Per rat the means are 0.221 to 0.322.",
"fig2b-trajectory-selective": "**Result: partially reproduced.** Units that fire differently on left and right trials are common in the central arm, where the paths overlap: 24.0% of 346 units pooled (22.9 to 26.2% per rat), against 0.9% with relabelled trials (Fisher p = 7.3e-24). Every rat is above the paper's 16 to 18%, and in the side arms 51.6 to 59.9% of units per rat are selective, above both the 22% and the 40% of the paper. Per session the central-arm fraction ranges from 1.9% to 69.2%. The s.d. band gives 24.3% and 59.8%.",
"odor-nosepoke": "**Result: partially reproduced.** 37.8% of 397 units fire at different rates during the nose poke for the two odors (Mann-Whitney P < 0.05), against 4.0% with relabelled trials (Fisher p = 5.5e-35), so odor-dependent firing is common, but the fraction is above the 20 to 30% of the criterion. A t-test gives 28.5%. Per rat the fraction is 34.9% (EE), 50.3% (FF) and 11.1% (GG).",
"fig3-connection-rates": "**Result: partially reproduced.** Of 31754 ordered pairs of PFC single units, 1.131% are connected, 0.898% excitatory and 0.233% inhibitory. The inhibitory rate matches the paper's 0.24%; the excitatory rate is 1.6 times the paper's 0.55%, so the total is above 0.79%. Excitatory connections are found in 4.01% of same-shank pairs and 0.35% of pairs on different shanks. None of the 800 unscreened pairs given the Monte Carlo test was significant. 40 unordered pairs (0.252%) are connected both ways, against the paper's 0.17%.",
"fig3-cell-classes": "**Result: not reproduced.** 37.9% of 417 units are putative pyramidal cells and 3.1% putative interneurons, against 32.5% and 12.5%, and 21 units have outgoing connections of both kinds. The pyramidal to interneuron ratio is 11.92 plus or minus 7.46 over sessions (12.15 pooled), against 2.82 plus or minus 0.51. Of the 124 targets of excitatory connections, 7.3% are putative interneurons (20.2% have some inhibitory connection), against 50.7%. 54 of the 74 inhibitory connections come from units that also excite other units.",
"fig3f-distance": "**Result: not reproduced.** Connections are far more likely on the same shank (4.60% of pairs against 0.52%, Fisher p = 1.1e-89; 61.0% of all connections), and 8 connections are 1000 micrometres or more apart (the largest 1400). The Spearman correlation over all distances is -0.619 with p = 0.102, which fails the criterion: the 1400 micrometre bin (2 of 310 pairs, 0.645%) is above the bins from 600 to 1200. Over 0 to 1200 micrometres the correlation is -0.964 (p = 0.00045).",
"fig4-position-dependence": "**Result: not reproduced.** Of 285 excitatory pairs, 10 (3.5%) show significant position-dependent excess coincidences with left and right trials together and 6 (2.1%) with each side tested alone, against the paper's 19.5% (67 of 343). The rank band gives 1.4% and 1.8%. The pairs have a median of 7 coincidences during runs (0 to 442); among the 28 pairs with at least 50, 21.4% are significant, so the low fraction is consistent with low power in these runs.",
"fig6-facilitation-depression": "**Result: not reproduced.** Of 284 excitatory pairs with enough spikes, 4.9% are depressing and 15.5% facilitating, against 12.7% and 10.7%. Facilitation is above the 5% the test gives by chance (binomial p = 3.5e-11) and depression is not (p = 0.56). Later spikes transmit more than first spikes (median excess 0.0099 against 0.0068 per presynaptic spike, Wilcoxon p = 6.1e-08). Pairs with at least 50 or 200 spikes of each kind give the same fractions within 0.5 points.",
"fig7-supralinear": "**Result: not reproduced.** Of 40 satellites with at least 20 two-partner events, 15 (38%) are supralinear. The median excess transmission is 0.0145 after one partner and 0.0197 after two, less than twice the single effect, and the Wilcoxon test gives p = 0.993. With 20 ms events 29% are supralinear (p = 0.998).",
"fig3-trajectory-by-class": "**Result: not reproduced.** In rats EE and FF, 58.5% and 66.7% of putative pyramidal cells and 60.0% and 62.5% of putative interneurons are trajectory specific, far above the chance of 2.5% and 1.9%; FF matches the layer 2/3 values within 10% and EE matches neither layer. Rat GG has 7 putative pyramidal cells (14.3% specific) and no putative interneuron, so the criterion, which asks this of every rat, fails.",
"summary": "## Summary\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning\nand the differences from the paper's method.\n\n| Claim | Data | Outcome |\n|---|---|---|\n| channel-region-link | with labels | partially reproduced |\n| rats-and-units | with labels | not reproduced |\n| task-performance | dandiset | blocked: data missing |\n| fig2c-active-fraction | with labels | not reproduced |\n| fig2-field-size | with labels | partially reproduced |\n| fig2b-trajectory-selective | with labels | partially reproduced |\n| traj-diverge | dandiset | blocked: data missing |\n| odor-nosepoke | with labels | partially reproduced |\n| fig3-connection-rates | with labels | partially reproduced |\n| fig3-cell-classes | with labels | not reproduced |\n| fig3f-distance | with labels | not reproduced |\n| fig4-position-dependence | with labels | not reproduced |\n| fig6-facilitation-depression | with labels | not reproduced |\n| fig7-supralinear | with labels | not reproduced |\n| fig3-trajectory-by-class | with labels | not reproduced |\n| ee188-example-session | dandiset | blocked: data missing |\n\n**How the analysis differs from the paper's.** Units are placed on the prefrontal probe by their\nmean waveform in the wideband signal, with the CRCNS channel map corrected for rat GG, and\nmulti-unit and sensor clusters are left out by rules chosen here; the paper's own selection of\nwell-isolated units is not known. Eight of the paper's sessions are used; EE.088 is left out\nbecause its units cannot be placed. Units are not matched across sessions. The layer of each rat\nis not known, so values by layer are matched rat by rat. The cross-correlogram bin (1 ms), the\nnumber of permutations, the Poisson screen before the jitter test, the measure of transmission for\nfirst and later spikes, the definition of satellites and the 1 Hz rule for position analyses are\nchoices made here, as the supplementary information was not available. The test of position\ndependence uses a band of mean plus c times s.d. because the rank band cannot reach 0.01.\n\n**What was found about the dandiset.** It holds three of the paper's four rats, and not the\nexample session EE.188 (nor EE.152 and EE.165). The units table has no channel, shank, region,\ncell type or multi-unit flag, and mixes prefrontal units, CA1 units, multi-unit clusters and\nclusters of the sensor signals; channel locations are \"unknown\" and the electrode groups are cut\nevery eight channels whatever the probe. In rat GG the channel order differs from the CRCNS map,\nand the nose-poke sensors are in reverse order relative to the side labels. In six files one\nunit's spike times are out of order. The trial table's `stop_time` is the end of the nose poke\n(the paper's trial start), `left_or_right` carries the description of `reward_time`, and only\ncorrect trials are listed. The two position series are the x coordinates of the two LEDs, in\npixels though stated in metres, the second all zero; there is no y coordinate. The linearized\nposition is stated in metres but runs from 0 to 2. EE.088 and the other sessions of its day have\nno wideband signal."
}
E
cd /tmp/claude-1001 && . scratch/bin/activate && python make_nb.py results.json
```

```
cells 59
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/000067-fujisawa-2008; for v in CCG_BIN_S CCG_LAGS_MS TEST_LAGS_MS RAW_HZ POS_HZ LFP_HZ SHIFT_SAMPLES MIN_PEAK_HZ N_PERM WM_SESSIONS; do echo "$v $(grep -c "$v" pfc.py) $(grep -c "$v" reproduce_fujisawa_2008.ipynb)"; done
```

```
CCG_BIN_S 1 0
CCG_LAGS_MS 1 0
TEST_LAGS_MS 1 0
RAW_HZ 9 0
POS_HZ 1 0
LFP_HZ 2 0
SHIFT_SAMPLES 2 0
MIN_PEAK_HZ 1 2
N_PERM 3 0
WM_SESSIONS 1 1
```

**Agent calls Bash**

```bash
cd entries/000067-fujisawa-2008; python - <<'E'
s=open('pfc.py').read()
for line in ['CCG_BIN_S = 0.001\n','CCG_LAGS_MS = np.arange(-5, 6)      # bin centres, ms\n','TEST_LAGS_MS = (1, 2, 3, 4)\n','POS_HZ = 20000.0 / 512          # 39.0625 Hz, the rate of the position series\n']:
    assert line in s, line
    s=s.replace(line,'')
open('pfc.py','w').write(s)
E
sed -n 40,100p pfc.py
```

```
The bin width of the cross-correlogram (1 ms) is not given in the main text and is chosen here.
- KERNEL_SIGMA = 0.05 (normalized length), the permutation test of left against right with
  pointwise and global bands at alpha 0.05: the paper's Methods. The number of permutations
  (N_PERM = 1000) and the position grid (101 points) are chosen here.
- Coincidence lags of 1 to 4 ms for position dependence of monosynaptic interactions, and the
  one-sided global band at 0.01: the paper's Methods.
- First spikes after at least 200 ms of silence and later spikes within 40 ms of the previous
  one, a permutation test of the labels at two-sided P < 0.10: the paper's Results and Figure 6
  legend. The measure of transmission (excess spikes from 1 to 4 ms per presynaptic spike, over
  the jitter expectation) is chosen here; the paper's "rate-normalized height" is defined in a
  supplementary figure that could not be retrieved.
- The 1 Hz minimum of peak rate in trials for position analyses is the "Cells" criterion of
  the CRCNS pfc-2 description, not the paper.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

import h5py
[... 41 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/000067-fujisawa-2008/pfc.py",
 "old_string": "- Coincidence lags of 1 to 4 ms for position dependence of monosynaptic interactions, and the\n  one-sided global band at 0.01: the paper's Methods.",
 "new_string": "  The Poisson screen before the Monte Carlo test (`connections`) is chosen here, to save time.\n- Coincidence lags of 1 to 4 ms for position dependence of monosynaptic interactions, and the\n  one-sided global band at 0.01: the paper's Methods. The band is built from the surrogates'\n  mean and s.d. (`band_test`, kind \"sd\"), chosen here because the Methods' rank band cannot\n  reach 0.01 with 1000 surrogates."
}
```

```
The file entries/000067-fujisawa-2008/pfc.py has been updated successfully. (note: the file had been modified on disk since you last read it — the edit applied cleanly, but the file contains other changes not in your context. Read it before edits that depend on surrounding content.)
```

**Agent calls Bash**

```bash
cd  python tools/entry.py all entries/000067-fujisawa-2008 2>&1 | tail -5
```

```
Installed kernelspec registry-000067-fujisawa-2008 in executed/000067-fujisawa-2008/.venv/share/jupyter/kernels/registry-000067-fujisawa-2008
0 error(s)
pass  reproduce_fujisawa_2008.ipynb  (611 s)
```

**Agent**

Passed in 611 s. Verifying that the executed outputs still match the conclusions.

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
nb=json.load(open('executed/000067-fujisawa-2008/reproduce_fujisawa_2008.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    tags=c['metadata'].get('tags')
    if i in (5,11) or (tags and tags[0].startswith('claim')):
        out=''.join(''.join(o.get('text','')) for o in c.get('outputs',[]))
        print(f'==== {i} {tags}'); print(out[:2500])
E
```

```
==== 5 ['sanity']
session  trials  left  right  poke_s_median  run_s_median  reward_after_stop  first_d_in_run  last_d_in_run  run_frames_d>0  frames_d>0_outside_trials  lin_min  lin_max lin_unit         x1_range  x2_all_zero pos_unit  duration_s
 EE.049      19     9     10          3.282         9.894               True           1.018          1.971           0.850                      0.000      0.0      2.0   meters    (-1.0, 564.0)         True   meters      1788.8
 EE.088      31    11     20          2.657         5.005               True           1.047          1.890           0.986                      0.003      0.0      2.0   meters    (-1.0, 284.0)         True   meters      2165.1
 EE.196      48    21     27          4.551         4.593               True           1.023          1.967           0.971                      0.003      0.0      2.0   meters (-1.0, 592.2105)         True   meters      2844.3
 FF.103      39    19     20          0.842         6.579               True           1.026          1.954           0.990                      0.003      0.0      2.0   meters (-1.0, 605.4951)         True   meters      2866.8
 FF.130      46    23     23          1.366         6.037               True           1.024          1.941           0.986                      0.004      0.0      2.0   meters    (-1.0, 610.0)         True   meters      2030.2
 FF.167      43    21     22          4.385         5.869               True           1.027          1.970           0.981                      0.004      0.0      2.0   meters    (-1.0, 605.0)         True   meters      1977.8
 GG.069      40    20     20         10.714         9.375               True           1.027          1.977           0.994                      0.001      0.0      2.0   meters    (-1.0, 611.0)         True   meters      2375.8
 GG.097      38    20     18          9.694         6.040               True           1.024          1.984           0.994                      0.005
[... 275 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001; python - <<'E'
s=open('make_nb.py').read()
def rep(a,b):
    global s
    assert a in s, a[:70]
    s=s.replace(a,b)
rep('''print("\\nUnits whose spike times were not in order (sorted on loading):",
      {s["session"]: s["unsorted_units"] for s in sessions if s["unsorted_units"]})''','''print("\\nUnits whose spike times were not in order (sorted on loading):",
      {s["session"]: s["unsorted_units"] for s in sessions if s["unsorted_units"]})
for s in analysed:
    for i in s["unsorted_units"]:
        st = s["trains"][i]
        raw_order = np.diff(st)  # already sorted; report what the unit is
        r = units[(units.session == s["session"]) & (units.unit == i)].iloc[0]
        print(f"  {s['session']} unit {i}: {len(st)} spikes, {r.rate_hz:.1f} Hz, ISIs < 2 ms {r.isi_lt2ms:.3f}, region {r.region}")''')
rep('''Units are placed by their mean waveform. The fraction of inter-spike intervals under 2 ms is
bimodal: most units have under 1%, and about one in seven has more than 10%. Those are the
multi-unit clusters; they are almost exactly the first unit of each shank block, which is where
the conversion's reader puts cluster 1 (multi-unit activity), so the two rules agree on nearly
every unit. Multi-unit clusters fire at a median of tens of hertz with small amplitudes. Some
units are clusters of the sensor signals (millivolts on a sensor channel, almost nothing on the
probes). In six sessions one unit's spike times are two sorted runs one after the other (the
file breaks the rule that spike times are in order); these are multi-unit clusters and are
sorted on loading.''','''Units are placed by their mean waveform. The fraction of inter-spike intervals under 2 ms is
bimodal: 604 of 719 units have at most 1%, 103 have more than 10%, and 12 lie between. The units
above 2% are taken as multi-unit clusters. 96 of these 107 are the first unit of a shank block,
which is where the conversion's reader puts cluster 1 (multi-unit activity), and 35 first units
are single units by the ISI rule, so the two rules mostly agree. Multi-unit clusters fire at a
median of 29 (CA1) and 56 Hz (PFC) with about half the amplitude of single units. 21 units are
clusters of the sensor signals (up to 9 mV on a sensor channel, under 200 uV on the probes). In
six sessions the spike times of unit 1 are not in order, which breaks the format; they are sorted
on loading, and in the analysed sessions these units are multi-unit clusters.''')
open('make_nb.py','w').write(s)
E
. scratch/bin/activate; python make_nb.py results.json
```

```
cells 59
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001; python - <<'E'
s=open('make_nb.py').read()
a='print("\\nFraction of ISIs < 2 ms over all units placed on a probe (bins):")'
assert a in s
s=s.replace(a,'print("\\nFraction of ISIs < 2 ms, all units of the eight sessions (bins):")')
a='''The units
above 2% are taken as multi-unit clusters. 96 of these 107 are the first unit of a shank block,'''
assert a in s
s=s.replace(a,'''The units
above 2% are taken as multi-unit clusters. Of the 107 such units on the probes, 96 are the first
unit of a shank block,''')
s=s.replace('''        raw_order = np.diff(st)  # already sorted; report what the unit is
''','')
open('make_nb.py','w').write(s)
E
. scratch/bin/activate; python make_nb.py results.json; cd  python tools/entry.py all entries/000067-fujisawa-2008 2>&1 | tail -3
```

```
cells 59
Installed kernelspec registry-000067-fujisawa-2008 in executed/000067-fujisawa-2008/.venv/share/jupyter/kernels/registry-000067-fujisawa-2008
0 error(s)
pass  reproduce_fujisawa_2008.ipynb  (605 s)
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
nb=json.load(open('executed/000067-fujisawa-2008/reproduce_fujisawa_2008.ipynb'))
c=nb['cells'][7]; print(''.join(''.join(o.get('text','')) for o in c['outputs']))
for i in (36,45,48,51):
    out=''.join(''.join(o.get('text','')) for o in nb['cells'][i]['outputs']); print(out[:700])
E
```

```
Units by session and class (PFC and CA1 split into single units and multi-unit clusters):
col_0    CA1 multi  CA1 single  PFC multi  PFC single  sensor  unassigned  All
session                                                                       
EE.049           4          31          9          70       1           3  118
EE.196           4          15          9         132       1           0  161
FF.103           4          11         11          50       2           0   78
FF.130           4           9         10          67       0           0   90
FF.167           2           8         10          43       1           0   64
GG.069           7          41          9          18       1           0   76
GG.097           4          25          8          19       9           4   69
GG.149           4          26          8          18       6           1   63
All             33         166         74         417      21           8  719

Units whose spike times were not in order (sorted on loading): {'EE.049': [1], 'EE.088': [1], 'EE.196': [1], 'FF.103': [1], 'FF.130': [1], 'GG.069': [1]}
  EE.049 unit 1: 200169 spikes, 111.9 Hz, ISIs < 2 ms 0.400, region PFC
  EE.196 unit 1: 133213 spikes, 46.8 Hz, ISIs < 2 ms 0.493, region PFC
  FF.103 unit 1: 362233 spikes, 126.4 Hz, ISIs < 2 ms 0.311, region PFC
  FF.130 unit 1: 135295 spikes, 66.6 Hz, ISIs < 2 ms 0.393, region PFC
  GG.069 unit 1: 197824 spikes, 83.3 Hz, ISIs < 2 ms 0.327, region PFC

[... 62 more lines not kept]
```

**Agent**

Final run is consistent. Now the entry README and the attempt record.

**Agent calls Write**

```json
{
 "file_path": "entries/000067-fujisawa-2008/README.md",
 "content": "# Fujisawa, Amarasingham, Harrison & Buzsáki (2008) from dandiset 000067\n\nTests the findings of [Fujisawa et al. (2008)](https://doi.org/10.1038/nn.2134) that can be tested\non [DANDI:000067](https://dandiarchive.org/dandiset/000067/0.250624.0419), which holds recordings\nof three rats from a 64-site prefrontal probe and a 32-site CA1 probe during an odor-place\nmatching task. The paper's fourth rat and its example session (EE.188) are not in it.\n\n| Claim | Outcome |\n|---|---|\n| The channels can be mapped to the probes and sensors with the CRCNS description | Partially reproduced |\n| 633 mPFC units from four rats | Not reproduced |\n| Task performance of 92% correct | Blocked: data missing |\n| About 10% (layer 2/3) and 20% (layer 5) of neurons active per 100 ms, constant along the maze | Not reproduced |\n| Field sizes of 0.27 plus or minus 0.17 of the track | Partially reproduced |\n| Trajectory-selective neurons in the central and side arms | Partially reproduced |\n| Trajectories diverge at position 0.3 | Blocked: data missing |\n| About a quarter of neurons respond differently to the two odors | Partially reproduced |\n| 0.79% of pairs connected (0.55% excitatory, 0.24% inhibitory) | Partially reproduced |\n| 32.5% pyramidal cells and 12.5% interneurons by their connections | Not reproduced |\n| Connection probability falls with distance | Not reproduced |\n| 67 of 343 excitatory pairs depend on position | Not reproduced |\n| 12.7% depressing and 10.7% facilitating pairs | Not reproduced |\n| Supralinear effect of coincident presynaptic spikes | Not reproduced |\n| Most pyramidal cells and interneurons are trajectory specific | Not reproduced |\n| Values of the example session (Figures 2a, 3b to 3d, 4 to 7) | Blocked: data missing |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe units table holds spike times only, so each unit is placed on a probe from its mean waveform\nin the wideband signal, and the probes are named with the channel map of the CRCNS pfc-2\ndescription of the same recordings, which the data confirm for two rats and correct for the\nthird. The attempt record, with the reasons and the differences from the paper's method, is\n[`attempts/000067-fujisawa-2008-01.yaml`](../../attempts/000067-fujisawa-2008-01.yaml).\n\n- `reproduce_fujisawa_2008.ipynb`: the analysis. It takes about ten minutes, most of it streaming\n  the files.\n- `pfc.py`: loading, the placement of units on the probes, and the measures: rate maps, the\n  permutation test of left against right, the jitter test for monosynaptic connections, the\n  position dependence of coincidences, first against later spikes, and coincident inputs. Other\n  notebooks on this dandiset can import it.\n"
}
```

```
File created successfully at: entries/000067-fujisawa-2008/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python -c "
import json;d=json.load(open('schemas/attempt.schema.json'))
for k in ('inputs','findings'): print(k, json.dumps(d['properties'][k])[:1500])"
```

```
inputs {"description": "Everything the attempt used that is not in the dandiset.", "type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["what", "source"], "properties": {"what": {"type": "string", "minLength": 1}, "source": {"description": "A DOI, or a repository URL with the commit read.", "type": "string", "minLength": 1}}}}
findings {"description": "What the attempt found about the dandiset itself, whatever the outcomes. These roll up into the per-dandiset report.", "type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["kind", "statement"], "properties": {"kind": {"enum": ["metadata_error", "data_missing", "identifier_missing", "metadata_insufficient", "selection_undocumented", "methods_unavailable", "format_error", "code_mismatch", "paper_inconsistency", "other"]}, "statement": {"type": "string", "minLength": 1}}}}
```

**Agent calls Write**

```json
{
 "file_path": "attempts/000067-fujisawa-2008-01.yaml",
 "content": "schema_version: 1\nid: 000067-fujisawa-2008-01\ndandiset: \"000067\"\ndandiset_version: 0.250624.0419\npaper: doi:10.1038/nn.2134\ndate: 2026-10-16\nentry: 000067-fujisawa-2008\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code (GitHub Actions)\n    model: claude-opus-5-5\n    protocol: pilot-7\ninputs:\n- what: Channel map of the recordings (channels 1-64 prefrontal probe, 65-96 CA1 probe, 97 and 98\n    the right and left nose-poke sensors), the meaning of the SessionNP trial columns, the note\n    that only correct trials are listed, the session table (task of each session, EE.188 as the\n    session of Figures 2a and 3d), and the \"Cells\" rule of a peak rate above 1 Hz. From the CRCNS\n    pfc-2 data description, version 0.7 (2021-07-14), a public document of the same recordings.\n    The data themselves on CRCNS need an account and were not used.\n  source: doi:10.6080/K01V5BWK (https://crcns.org/files/data/pfc-2/crcns_pfc-2_data_description.pdf)\n- what: The conversion code of the dandiset, read to interpret the files (which columns of the\n    position file became the two position series, which SessionNP columns became the trial\n    columns, and that every shank's clusters were read with multi-unit clusters kept). Not\n    linked by the paper or the dandiset; no code of the paper's analysis is published.\n  source: https://github.com/catalystneuro/buzsaki-lab-to-nwb at commit\n    5f6a3750fffd999c4757d8a198cba6007f85fb12 (buzsaki_lab_to_nwb/fujisawa)\n- what: The reader the conversion used (NeuroscopeSortingExtractor), read for the order of units\n    and the handling of cluster 1 (multi-unit activity, kept and put first in each shank).\n  source: https://github.com/SpikeInterface/spikeextractors at commit\n    d24335cc2fa6e407469b790dc8fea2fdadb2b2a3\noutcomes:\n- claim: channel-region-link\n  outcome: partially_reproduced\n  notebook: reproduce_fujisawa_2008.ipynb\n  output: claim:channel-region-link\n  notes: Records are matched by channel number. In rats EE and FF the CRCNS map holds in every\n    session; the CA1 channels have a theta ratio 1.9 to 2.7 times that of channels 1 to 64, and\n    the more active sensor during the nose poke is the trial's side in 0.97 to 1.00 of trials. In\n    rat GG channels 97 and 98 are not sensors (agreement 0.35 to 0.42); the sensors are on 65 and\n    66 and the CA1 probe on 70 to 101, and with that correction both checks hold in every session\n    (agreement 1.00). The sensor on 66 is active on trials labelled Right, so in GG the order of\n    the sensors, or the side labels, is reversed relative to EE and FF. Channels 1 to 64 carry no\n    hippocampal theta in any rat, so the prefrontal probe is placed as the description says in\n    all three rats; every claim that uses PFC units depends on that part, which holds.\n  deviations:\n  - The map is used with the per-rat correction found in the data, not as published.\n  - The sensor check of EE.088 uses its LFP only; it has no wideband signal for the theta check.\n- claim: rats-and-units\n  outcome: not_reproduced\n  notebook: reproduce_fujisawa_2008.ipynb\n  output: claim:rats-and-units\n  measured:\n  - 3\n  - 417\n  notes: The dandiset holds three rats (EE, FF, GG), against four. The eight analysed sessions hold\n    417 PFC single units under reading (a), 346 under (b) and 491 under (c), all outside 633 plus\n    or minus 63. The 350 units of EE.088 cannot be placed on a probe, and EE.152, EE.165 and\n    EE.188, working memory sessions in the CRCNS table, are not in the dandiset; the paper does not\n    say which sessions its 633 units come from, nor whether units recorded on several days were\n    counted once.\n  deviations:\n  - Units are counted per session; the paper's way of counting is not stated.\n  - Well-isolated units are selected by a refractory rule chosen here.\n- claim: task-performance\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The trial table lists correct trials only (the CRCNS description of SessionNP; every\n    file's table has correct trials only by that description), so the fraction of correct trials\n    cannot be computed. The position has no y coordinate, so the choice on other trials cannot be\n    recovered from the path. Error trials are not in the dandiset, and the CRCNS data need an\n    account.\n- claim: fig2c-active-fraction\n  outcome: not_reproduced\n  notebook: reproduce_fujisawa_2008.ipynb\n  output: claim:fig2c-active-fraction\n  notes: Per-rat medians of the session means are 10.2% (EE), 19.7% (FF) and 6.2% (GG); EE fits the\n    layer 2/3 value and FF the layer 5 value, GG fits neither. The ratio of the largest to the\n    smallest position-bin mean is 1.16 to 1.88 in seven sessions and 2.57 in GG.149. Neither part\n    of the criterion holds for every rat; both hold for EE and FF. GG's sessions have 18 or 19 PFC\n    single units each.\n  deviations:\n  - The layer of each rat is not known; values are matched rat by rat under the layer readings.\n  - The threshold for \"relatively constant\" (a factor of 2) is chosen here.\n- claim: fig2-field-size\n  outcome: partially_reproduced\n  notebook: reproduce_fujisawa_2008.ipynb\n  output: claim:fig2-field-size\n  measured:\n  - 0.27\n  - 0.196\n  notes: Reading (a), 346 units, mean 0.270 and s.d. 0.196; (b) 0.281 and 0.206; (c) 0.331 and\n    0.220. The mean is within tolerance under every reading and the s.d. under none (0.17 plus or\n    minus 0.017). With peak thresholds from 0 to 5 Hz the mean of (a) is 0.254 to 0.330 and the\n    s.d. 0.189 to 0.243. Per rat the means are 0.221 (EE), 0.322 (FF) and 0.272 (GG).\n  deviations:\n  - The mean's tolerance is the paper's stated s.d. of the neurons, as the protocol asks, which\n    accepts a wide range of means; the s.d. carries the test.\n  - The 1 Hz peak rule is the CRCNS \"Cells\" rule, not the paper's.\n  - The paper does not say how the 50% boundaries are taken or which trajectory is used; three\n    readings are shown.\n- claim: fig2b-trajectory-selective\n  outcome: partially_reproduced\n  notebook: reproduce_fujisawa_2008.ipynb\n  output: claim:fig2b-trajectory-selective\n  notes: Central arm, 22.9% (EE), 24.5% (FF) and 26.2% (GG) of units with a peak of at least 1 Hz\n    (24.0% of 346 pooled), against 0.9% with relabelled trials (Fisher p = 7.3e-24); every rat is\n    above the 14.4 to 19.8% range. Side arms, 51.6%, 59.9% and 52.4%, above both layer values.\n    Per session the central-arm fraction is 1.9% to 69.2%. With the s.d. band, 24.3% and 59.8%\n    pooled. The procedure's chance rate (0.9% for each segment) is below the global 5%, as\n    expected for a segment of the track. The selective fractions are higher than the paper's in\n    every rat, so units selective by this test are more common here.\n  deviations:\n  - The number of permutations (1000) and the 101-point grid are chosen here.\n  - Layers are matched rat by rat, as the layer of each rat is not known.\n  - In rat GG the side labels may be swapped (see channel-region-link); this does not change a\n    left-right test.\n- claim: traj-diverge\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The two position series are the x coordinates of the two head LEDs (the conversion took\n    columns 1 and 3 of the position file), and the second is zero in every file. The y coordinate,\n    along which the side arms differ, is not in the dandiset; only the linearized position is,\n    which by construction does not separate the arms.\n- claim: odor-nosepoke\n  outcome: partially_reproduced\n  notebook: reproduce_fujisawa_2008.ipynb\n  output: claim:odor-nosepoke\n  measured: 37.8\n  notes: 37.8% of 397 units (Mann-Whitney P < 0.05) against 4.0% with relabelled trials (Fisher\n    p = 5.5e-35); outside 20 to 30%. A t-test gives 28.5%, which would be within, but the test was\n    fixed beforehand. Per rat 34.9% (EE), 50.3% (FF), 11.1% (GG). Odor and side are the same\n    variable here, as only correct trials are listed, so the difference can come from the odor or\n    from the coming choice; the paper's Supplementary Figure 6 analysis of that point was not\n    available.\n  deviations:\n  - The paper names no test; a Mann-Whitney test of per-trial rates was chosen.\n  - The nose-poke period is from the start of the first nose poke to the end of the last (median\n    4.66 s), as the trial table gives; the paper's window is not stated in the main text.\n- claim: fig3-connection-rates\n  outcome: partially_reproduced\n  notebook: reproduce_fujisawa_2008.ipynb\n  output: claim:fig3-connection-rates\n  measured:\n  - 1.131\n  - 0.898\n  - 0.233\n  notes: 31754 ordered pairs; connections 1.131%, excitatory 0.898%, inhibitory 0.233%. Only the\n    inhibitory rate is within tolerance. Excitatory connections are 4.01% of same-shank pairs and\n    0.35% of pairs across shanks; per rat the excitatory rate is 0.84% (EE), 1.05% (FF), 0.94% (GG).\n    The Poisson screen passed 857 unordered pairs to the Monte Carlo test, and none of the 800\n    unscreened pairs tested anyway was significant. 40 unordered pairs (0.252%) are connected both\n    ways (paper 0.17%). Counting peaks of any width gives 0.938% excitatory. The excess of\n    same-shank peaks may include pairs of clusters split from one neuron, which the paper's\n    curated units may not contain.\n  deviations:\n  - Bins of 1 ms (not stated in the main text) and a Poisson screen before the Monte Carlo test.\n  - A trough beside a peak in the same direction is not counted as inhibition (chosen here).\n  - The set of well-isolated units is selected here, not by the paper.\n- claim: fig3-cell-classes\n  outcome: not_reproduced\n  notebook: reproduce_fujisawa_2008.ipynb\n  output: claim:fig3-cell-classes\n  measured:\n  - 37.9\n  - 3.1\n  - 11.92\n  - 7.3\n  notes: Of 417 units, 37.9% putative pyramidal and 3.1% putative interneurons, and 21 units have\n    outgoing connections of both kinds. The ratio is 11.92 plus or minus 7.46 over the five\n    sessions with an interneuron (pooled 12.15, mean of rats 12.96), against 2.82 plus or minus\n    0.51. Of 124 targets of excitatory connections 7.3% are putative interneurons (20.2% have any\n    inhibitory connection), against 50.7%. 54 of the 74 inhibitory connections come from units\n    that also excite others. No value is within tolerance under any reading; the shortfall of\n    interneurons drives the ratio and the targets.\n  deviations:\n  - Units with both kinds of connection are counted in neither class (chosen here).\n- claim: fig3f-distance\n  outcome: not_reproduced\n  notebook: reproduce_fujisawa_2008.ipynb\n  output: claim:fig3f-distance\n  notes: Same shank 4.60% against 0.52% across shanks (Fisher p = 1.1e-89), 61.0% of connections\n    on the same shank, and 8 connections at 1000 micrometres or more (largest 1400). The Spearman\n    correlation over 0 to 1400 micrometres is -0.619, p = 0.102, so the second condition fails and\n    the criterion gives not reproduced. The probability falls from 4.60% at 0 to 0.24% at 600\n    micrometres and is 0.17 to 0.19% from 800 to 1200; the 1400 bin (2 of 310 pairs, 0.645%)\n    breaks the rank order. Over 0 to 1200 micrometres rho = -0.964, p = 0.00045. The fall with\n    distance is present; the outcome comes from the test fixed beforehand on eight points.\n  deviations:\n  - Distance is the shank separation only; positions within a shank were not estimated.\n- claim: fig4-position-dependence\n  outcome: not_reproduced\n  notebook: reproduce_fujisawa_2008.ipynb\n  output: claim:fig4-position-dependence\n  measured: 3.5\n  notes: Reading (a) 10 of 285 excitatory pairs (3.5%); reading (b) 6 (2.1%); rank band 1.4% and\n    1.8%. The median pair has 7 coincidences during runs (range 0 to 442); of the 28 pairs with at\n    least 50, 21.4% are significant, of the 13 with at least 100, 7.7%. The paper's pairs may have\n    had more spikes, or its runs may have been defined over more of the trial; the low fraction\n    here is consistent with low power.\n  deviations:\n  - The band is mean plus c times s.d. of the surrogates, not the Methods' rank band, because the\n    rank band cannot reach a one-sided 0.01 with 1000 surrogates on 101 points (it is empty when\n    more than 1% of data sets reach the extreme rank somewhere). This was found after a first run\n    of the rank version gave 1.0% and a synthetic test showed that it could not detect a strong\n    position-limited coupling; the rank result is shown as a variant.\n  - Event positions are kept at the original presynaptic spike in the surrogates.\n- claim: fig6-facilitation-depression\n  outcome: not_reproduced\n  notebook: reproduce_fujisawa_2008.ipynb\n  output: claim:fig6-facilitation-depression\n  measured:\n  - 4.9\n  - 15.5\n  notes: Of 284 excitatory pairs with enough spikes, 14 (4.9%) depressing and 44 (15.5%)\n    facilitating. Facilitation is above chance (binomial p = 3.5e-11), depression is not (p =\n    0.56). Overall later spikes transmit more than first spikes (median 0.0099 against 0.0068,\n    Wilcoxon p = 6.1e-08). With at least 50 or 200 spikes of each kind, 5.0 to 5.3% depressing and\n    15.4 to 15.9% facilitating. The paper's measure (rate-normalized peak height) was not\n    available, and a measure that normalizes by the postsynaptic rate in each condition could\n    give a different balance.\n  deviations:\n  - Transmission measured as excess spikes from 1 to 4 ms over the jitter expectation, chosen\n    here in place of the paper's rate-normalized peak height.\n  - Later spikes are any spike within 40 ms of the previous one (the Figure 6 legend), not only\n    spikes inside trains that began after 200 ms of silence.\n- claim: fig7-supralinear\n  outcome: not_reproduced\n  notebook: reproduce_fujisawa_2008.ipynb\n  output: claim:fig7-supralinear\n  notes: 41 satellites, 40 with at least 20 two-partner events; 15 (38%) supralinear; median excess\n    0.0145 for one partner and 0.0197 for two; Wilcoxon p = 0.993. Two coincident partners\n    transmit more than one, but less than twice as much. With 20 ms events, 29% supralinear (p =\n    0.998). The paper had 14 satellites; its definition of a satellite and of transmission\n    probability is in the supplementary information, which was not available.\n  deviations:\n  - Satellites, events and the excess measure are defined here.\n- claim: fig3-trajectory-by-class\n  outcome: not_reproduced\n  notebook: reproduce_fujisawa_2008.ipynb\n  output: claim:fig3-trajectory-by-class\n  notes: EE, 58.5% of 94 putative pyramidal cells and 60.0% of 5 interneurons are trajectory\n    specific; FF, 66.7% of 57 and 62.5% of 8; GG, 14.3% of 7 and no interneuron. Chance is 1.9 to\n    2.5%. FF matches the layer 2/3 values within 10%, EE matches neither layer, and GG cannot meet\n    the criterion without interneurons. Large fractions of both classes are trajectory specific in\n    EE and FF, which is the qualitative part of the claim; the interneuron counts are small, as\n    fig3-cell-classes found few interneurons.\n  deviations:\n  - Layers are matched rat by rat; trajectory specificity is the test of\n    fig2b-trajectory-selective over the whole track.\n- claim: ee188-example-session\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The CRCNS description names EE.188 (day EE0708) as the session of Figures 2a and 3d, and\n    Figure 5 uses the same session; the dandiset has no file of that day, nor of EE.152 and EE.165.\n    The CRCNS copy needs an account. The example cell numbers cannot be matched to the dandiset's\n    units in any case, as its units carry no original cluster numbers.\nfindings:\n- kind: data_missing\n  statement: The dandiset holds three rats (EE, FF, GG); the paper recorded four. Of the 13 working\n    memory sessions in the CRCNS session table, EE.152, EE.165 and EE.188 are not in the\n    dandiset, and EE.210 has no trial table or position. EE.188 is the paper's example session\n    (Figures 2a, 3b to 3d, 4 and 5).\n- kind: metadata_insufficient\n  statement: The units table holds spike times only. It has no channel, shank, brain region, cell\n    type or quality label, and mixes prefrontal units, CA1 units, multi-unit clusters (cluster 1 of\n    each shank, kept by the conversion) and clusters of the sensor signals. Units can be placed\n    only from their waveforms in the wideband signal, which EE.042 and the ten sessions of\n    2008-06-27 (EE.080 to EE.089, among them the working memory session EE.088) do not have.\n- kind: metadata_insufficient\n  statement: Electrode locations are \"unknown\", coordinates are missing and impedances are -1. The\n    electrode groups \"shank1\" to \"shank13\" are cuts of eight consecutive channels, whatever the\n    probe, so they do not identify the prefrontal shanks, the CA1 shanks or the sensor channels.\n    The layer recorded in each rat is not stated.\n- kind: metadata_error\n  statement: In rat GG the channel order differs from the CRCNS description. The nose-poke sensors\n    are on channels 65 and 66 (1-based) and the CA1 probe on 70 to 101, where the description gives\n    97 and 98 and 65 to 96. The sensor on 66 is active on trials labelled Right, the reverse of the\n    order in rats EE and FF, so either the sensors or the trial side labels of rat GG are swapped.\n- kind: metadata_error\n  statement: The trial table's stop_time is the end of the last nose poke, the paper's trial start,\n    and reward_time is the paper's trial end; the column left_or_right carries the description of\n    reward_time (\"Time when subject began consuming reward.\"). Only correct trials are listed,\n    which the files do not say.\n- kind: metadata_error\n  statement: The two \"(x,y) coordinates\" series SpatialSeries1 and SpatialSeries2 are the x\n    coordinates of the two head LEDs, in pixels although stated in metres, and the second is zero\n    in every file; the y coordinates are not in the dandiset. The linearized position is stated in\n    metres but runs from 1 (trial start) to 2 (reward), with 0 outside trials.\n- kind: format_error\n  statement: In six files (EE.049, EE.088, EE.196, FF.103, FF.130, GG.069) the spike times of unit 1\n    are not in ascending order. In the files examined they are two sorted runs one after the other,\n    a multi-unit cluster.\n- kind: other\n  statement: GG.063, a spontaneous alternation session in the CRCNS table, has a trial table with\n    left and right trials like the working memory sessions; the files do not say which task a\n    session is.\n- kind: metadata_insufficient\n  statement: The session description of every file is the paper's abstract, and session start\n    times are dates at midnight; the files do not say which sessions are sleep, test, spontaneous\n    alternation or working memory sessions.\n"
}
```

```
File created successfully at: attempts/000067-fujisawa-2008-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python - <<'E'
p='attempts/000067-fujisawa-2008-01.yaml'
s=open(p).read()
reps=[('''  notes: The trial table lists correct trials only (the CRCNS description of SessionNP; every
    file's table has correct trials only by that description), so the fraction of correct trials
    cannot be computed.''','''  notes: The trial table lists correct trials only (the CRCNS description of SessionNP, from which
    the conversion built the table), so the fraction of correct trials cannot be computed.'''),
('''are not in ascending order. In the files examined they are two sorted runs one after the other,
    a multi-unit cluster.''','''are not in ascending order. In EE.049 and FF.103, examined in detail, they are two sorted runs
    one after the other; in the five analysed files the unit is a multi-unit cluster.'''),
('''specific; FF, 66.7% of 57 and 62.5% of 8; GG, 14.3% of 7 and no interneuron. Chance is 1.9 to
    2.5%.''','''specific; FF, 66.7% of 57 and 62.5% of 8; GG, 14.3% of 7 and no interneuron. Chance is 0.0 to
    2.5%.''')]
for a,b in reps:
    assert a in s, a[:50]; s=s.replace(a,b)
open(p,'w').write(s)
E
grep -n ": .*: " attempts/000067-fujisawa-2008-01.yaml | grep -v "https\?:" ; python tools/entry.py check entries/000067-fujisawa-2008 2>&1 | tail -5
```

```
0 error(s)
```

**Agent calls Bash**

```bash
cd  git status --short; grep -n "—\|rather\|TODO" entries/000067-fujisawa-2008/* attempts/000067-fujisawa-2008-01.yaml claims/000067/*.yaml | grep -v lock.txt | head; git check-ignore paper executed && echo ignored
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
?? attempts/000067-fujisawa-2008-01.yaml
?? claims/000067/
?? entries/000067-fujisawa-2008/
?? scripts
grep: entries/000067-fujisawa-2008/__pycache__: Is a directory
paper
executed
ignored
```

**Agent calls Bash**

```bash
cd  git check-ignore entries/000067-fujisawa-2008/__pycache__ && echo pyc-ignored; ls -la .bashrc .idea scripts 2>&1 | head; git log --oneline -1 -- scripts
```

```
entries/000067-fujisawa-2008/__pycache__
pyc-ignored
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 16 14:41 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 16 14:41 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 16 14:41 scripts
```

**Agent**

The stray root dotfiles are sandbox placeholder devices, not repository content. Running the handover (step 6).

**Agent calls Bash**

```bash
cd  python tools/entry.py handover entries/000067-fujisawa-2008 2>&1 | tail -5; ls -R executed/000067-fujisawa-2008/handover | head; python - <<'E'
import json
nb=json.load(open('executed/000067-fujisawa-2008/handover/reproduce_fujisawa_2008.ipynb'))
print(len(nb['cells']), sum(1 for c in nb['cells'] if c['cell_type']=='markdown' and ''.join(c['source']).startswith('**Result')), any('## Summary' in ''.join(c['source']) for c in nb['cells']))
E
```

```
wrote executed/000067-fujisawa-2008/handover
executed/000067-fujisawa-2008/handover:
doi-10.1038-nn.2134.yaml
pfc.py
reproduce_fujisawa_2008.ipynb
45 0 False
```

**Agent**

I finished steps 1 to 5 and ran the handover (step 6). `entry.py check` reports 0 errors and the notebook passes `entry.py run` in 605 s. Nothing is committed.

**Paper and version.** I used the full text of the author manuscript in PubMed Central (PMC2562676), saved under `paper/`. The supplementary PDF could not be fetched: PubMed Central and the publisher returned a reCAPTCHA page. I pinned 0.250624.0419, the most recent published version. The paper cites no version, and both published versions and the draft hold the same 28 assets with the same blob ids.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| channel-region-link | partially reproduced |
| rats-and-units | not reproduced |
| task-performance | blocked: data missing |
| fig2c-active-fraction | not reproduced |
| fig2-field-size | partially reproduced |
| fig2b-trajectory-selective | partially reproduced |
| traj-diverge | blocked: data missing |
| odor-nosepoke | partially reproduced |
| fig3-connection-rates | partially reproduced |
| fig3-cell-classes | not reproduced |
| fig3f-distance | not reproduced |
| fig4-position-dependence | not reproduced |
| fig6-facilitation-depression | not reproduced |
| fig7-supralinear | not reproduced |
| fig3-trajectory-by-class | not reproduced |
| ee188-example-session | blocked: data missing |

## 2. What was found about the dandiset

- **Missing data:** it holds 3 of the paper's 4 rats. The paper's example session EE.188, and also EE.152 and EE.165, are absent. EE.210 has no trial table.
- **Units table:** it holds spike times only. It mixes mPFC units, CA1 units, multi-unit clusters and clusters of the nose-poke sensor signals, with no channel, shank, region or cell type.
  - I placed each unit on a probe from its mean waveform in the wideband signal.
  - That is impossible for EE.088 and the other sessions of its day, which have no wideband signal.
  - Electrode locations are "unknown", and the electrode groups are just cuts of 8 consecutive channels.
- **Rat GG channel map:** it differs from the CRCNS description of the same recordings. The sensors are on channels 65 and 66, CA1 is on 70 to 101, and the sensor order (or the side labels) is reversed relative to rats EE and FF.
- **Trial table:**
  - `stop_time` is the end of the nose poke, which is the paper's trial start.
  - `left_or_right` carries the description of `reward_time`.
  - Only correct trials are listed.
- **Position:** both position series are the x coordinates of the two head LEDs, in pixels though labelled metres; the second is all zeros. There is no y coordinate. The linearized position is labelled metres but runs from 0 to 2.
- **Spike order:** in six files, unit 1's spike times are not in ascending order.
- **Clocks:** spikes, trials and LFP share one clock. Shown with the sensor edges, the spike waveforms and side decoding; decoding is weak in GG.097.

## 3. Where the protocol was unclear, wrong or missing something

1. **Outside labels the paper does not rely on.** The only channel-to-region map is in the CRCNS documentation, not something the paper uses. I treated it as `with_labels`, listed it under inputs, and tested it with a link claim.
2. **"Stated spread" as tolerance.** The paper's ±0.17 is the spread across neurons, not the uncertainty of the mean. I followed the protocol literally for the mean and added the s.d. as a second expected value with a 10% tolerance, which is the part that actually tests the claim.
3. **Values given by layer, with no layer per subject.** The protocol has no rule for this. I matched rat by rat, allowing each rat either layer with at most one in layer 5.
4. **Criteria written after seeing some results.** A timing run of the connection test printed per-session connection counts before I wrote three of the criteria. The protocol only covers seeing the data check first. I disclosed this in the claims file and changed none of those method choices afterwards.
5. **The Methods' test cannot work here.** The rank-based global band can never reach a one-sided 1% with 1000 surrogates on 101 smooth points. I found this after a first run gave 1.0% significant pairs. I switched to a mean ± c·s.d. band, kept the rank version as a variant, and recorded when and why as a deviation. The protocol's tie-break rule does not cover a test that cannot fire.
6. **No paper code.** The protocol only asks about code the paper or dandiset links to. I read the conversion code and the spike-sorting reader it used, recorded both at their commits, and used them to interpret the files.
7. **Supplement unavailable.** There is no rule for when the supplement is what defines the methods. I fixed those measures in the criteria and recorded them as deviations.
8. **A label link that holds only after a correction.** There is no outcome rule for this. I wrote it into the criterion beforehand as partially reproduced.
9. **A "per rat" criterion one rat cannot meet.** Rat GG has no putative interneurons, so fig3-trajectory-by-class fails its criterion. The protocol's rule for blocks that depend on a selection might have allowed `blocked: other` instead; I applied the criterion as written.
10. **Units shared across sessions.** Rat EE's sessions of one day were spike-sorted together, so they may share units. I counted units per session and stated this as an assumption.

## 4. Runtime and failures

- The notebook takes about 10 minutes, most of it streaming. I made three full clean runs, and the conclusions were checked against the final executed copy.
- The PubMed Central XML endpoint and the supplement could not be downloaded. The Buzsáki lab mirror of the data is not open. The CRCNS data files need an account and were not used; only their public description PDF was.
- Bugs I found and fixed before the final run:
  - The rank band could not reach significance (point 5).
  - A data-check cell read the position on the frame where it had already dropped to 0.
- Some untracked files in the repo root (`.bashrc`, `.idea`, `scripts` and others) are sandbox placeholder devices, not my output; I left them in place.

## End of run

107 turns, 77 minutes, result: success.
