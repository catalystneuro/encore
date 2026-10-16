# 000044 · author · run 38850565385

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; echo ======; cat README.md; echo =====; cat docs/design.md; ls; ls entries claims attempts tools
```

```
<persisted-output>
Output too large (41.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/7a0ab8ba-8a45-435d-8121-502432cbaf6d/tool-results/b90on88ir.txt

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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/7a0ab8ba-8a45-435d-8121-502432cbaf6d/tool-results/b90on88ir.txt"
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
[... 819 more lines not kept]
```

**Agent**

Now the example entry formats.

**Agent calls Bash**

```bash
ls -la entries/001453-fouke-2025/ claims/001453/; cat entries/001453-fouke-2025/entry.yaml entries/001453-fouke-2025/requirements.in; cat entries/001453-fouke-2025/README.md 2>/dev/null; cat attempts/001453-fouke-2025-01.yaml
```

```
<persisted-output>
Output too large (38.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/7a0ab8ba-8a45-435d-8121-502432cbaf6d/tool-results/bmsxnznz5.txt

Preview (first 2KB):
claims/001453/:
total 24
drwxr-xr-x  2 runner runner  4096 Oct 16 04:25 .
drwxr-xr-x 20 runner runner  4096 Oct 16 04:25 ..
-rw-r--r--  1 runner runner 12471 Oct 16 04:25 10.1016-j.cub.2025.04.027.yaml

entries/001453-fouke-2025/:
total 124
drwxr-xr-x  2 runner runner  4096 Oct 16 04:25 .
drwxr-xr-x 20 runner runner  4096 Oct 16 04:25 ..
-rw-r--r--  1 runner runner  2158 Oct 16 04:25 README.md
-rw-r--r--  1 runner runner   914 Oct 16 04:25 entry.yaml
-rw-r--r--  1 runner runner 16218 Oct 16 04:25 omr.py
-rw-r--r--  1 runner runner 79403 Oct 16 04:25 reproduce_fouke_2025.ipynb
-rw-r--r--  1 runner runner    61 Oct 16 04:25 requirements.in
-rw-r--r--  1 runner runner  5989 Oct 16 04:25 requirements.lock.txt
[... 35 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/7a0ab8ba-8a45-435d-8121-502432cbaf6d/tool-results/bmsxnznz5.txt"
}
```

```
1	claims/001453/:
2	total 24
3	drwxr-xr-x  2 runner runner  4096 Oct 16 04:25 .
4	drwxr-xr-x 20 runner runner  4096 Oct 16 04:25 ..
5	-rw-r--r--  1 runner runner 12471 Oct 16 04:25 10.1016-j.cub.2025.04.027.yaml
6	
7	entries/001453-fouke-2025/:
8	total 124
9	drwxr-xr-x  2 runner runner  4096 Oct 16 04:25 .
10	drwxr-xr-x 20 runner runner  4096 Oct 16 04:25 ..
11	-rw-r--r--  1 runner runner  2158 Oct 16 04:25 README.md
12	-rw-r--r--  1 runner runner   914 Oct 16 04:25 entry.yaml
13	-rw-r--r--  1 runner runner 16218 Oct 16 04:25 omr.py
14	-rw-r--r--  1 runner runner 79403 Oct 16 04:25 reproduce_fouke_2025.ipynb
15	-rw-r--r--  1 runner runner    61 Oct 16 04:25 requirements.in
16	-rw-r--r--  1 runner runner  5989 Oct 16 04:25 requirements.lock.txt
17	schema_version: 1
18	name: 001453-fouke-2025
19	type: reproduction
20	title: Optomotor swimming of zebrafish and Danionella cerebrum (Fouke et al. 2025)
[... 674 more lines not kept]
```

**Agent calls Bash**

```bash
head -80 claims/001453/*.yaml; ls schemas; cat schemas/claims*.json | head -150
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
[... 203 more lines not kept]
```

**Agent calls Bash**

```bash
cat schemas/attempt.schema.json | python -c "import json,sys; d=json.load(sys.stdin); print(json.dumps(d,indent=1)[:6000])"; sed -n 1,80p tools/entry.py
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
[... 333 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/000044/ | python -m json.tool; curl -s "https://api.dandiarchive.org/api/dandisets/000044/versions/" | python -m json.tool
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
for v in 0.210812.1516 0.250624.0426 0.261005.2101; do echo "== $v"; curl -s "https://api.dandiarchive.org/api/dandisets/000044/versions/$v/assets/?page_size=100" | python -c "
import json,sys
d=json.load(sys.stdin)
for a in d['results']: print(a['asset_id'], a['path'], a['size'], a['modified'])
"; done
curl -s "https://api.dandiarchive.org/api/dandisets/000044/versions/0.261005.2101/" > $TMPDIR/meta.json; python -m json.tool $TMPDIR/meta.json | head -300
```

Result: the fetched text is not kept.

**Agent**

Dandiset 000044 has 8 sessions from 4 rats, each file 5 to 9 GB, with three published versions. Next I'm getting the paper.

**Agent calls Bash**

```bash
curl -s "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1126/science.aad1935&format=json&resultType=core" | python -c "
import json,sys; d=json.load(sys.stdin)
for r in d['resultList']['result']: print(r.get('pmid'), r.get('pmcid'), r.get('isOpenAccess'), r.get('inEPMC'), r.get('hasPDF'), r['title']); print(r.get('abstractText','')[:3000])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
mkdir -p paper; curl -sL "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4919122/fullTextXML" -o paper/fulltext.xml; ls -la paper; head -c 600 paper/fulltext.xml; curl -sL "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4919122/supplementaryFiles" -o paper/supp.zip; ls -la paper; file paper/supp.zip
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -sL "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=4919122&rettype=xml" -o paper/pmc4919122.xml; ls -la paper; python - <<'E'
import re
t=open('paper/pmc4919122.xml').read()
print(len(t)); print(t[:500])
E
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
rm paper/fulltext.xml paper/supp.zip; python - <<'E'
import re,html
t=open('paper/pmc4919122.xml').read()
t=re.sub(r'<xref[^>]*>(.*?)</xref>',r'[\1]',t)
t=re.sub(r'</(p|title|caption|label)>','\n',t)
t=re.sub(r'<[^>]+>','',t)
t=html.unescape(t)
open('paper/pmc4919122.txt','w').write(t)
print(t)
E
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -o '<supplementary-material[^>]*>.\{0,600\}' paper/pmc4919122.xml | head; grep -o 'xlink:href="[^"]*"' paper/pmc4919122.xml | sort -u
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; for u in "https://pmc.ncbi.nlm.nih.gov/articles/instance/4919122/bin/NIHMS788765-supplement-Materials_and_Methods__Figs__S1_to_S22__References.pdf" "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4919122/bin/NIHMS788765-supplement-Materials_and_Methods__Figs__S1_to_S22__References.pdf" "https://europepmc.org/articles/PMC4919122/bin/NIHMS788765-supplement-Materials_and_Methods__Figs__S1_to_S22__References.pdf"; do curl -sL -A "Mozilla/5.0" "$u" -o supp.pdf; file supp.pdf; ls -la supp.pdf; done
```

```
supp.pdf: HTML document, ASCII text, with very long lines (4064)
-rw-r--r-- 1 runner runner 21545 Oct 16 04:26 supp.pdf
supp.pdf: HTML document, ASCII text, with very long lines (4064)
-rw-r--r-- 1 runner runner 21529 Oct 16 04:26 supp.pdf
supp.pdf: HTML document, ASCII text, with very long lines (5824), with no line terminators
-rw-r--r-- 1 runner runner 5824 Oct 16 04:26 supp.pdf
```

**Agent calls Bash**

```bash
cd paper; head -c 1500 supp.pdf; echo; for u in "https://www.science.org/doi/suppl/10.1126/science.aad1935/suppl_file/grosmark.sm.pdf" "https://europepmc.org/api/fulltextRepo?pprId=PMC4919122&type=FILE&fileName=NIHMS788765-supplement-Materials_and_Methods__Figs__S1_to_S22__References.pdf&mimeType=application/pdf" ; do curl -sL -A "Mozilla/5.0" "$u" -o s2.pdf; file s2.pdf; ls -la s2.pdf; done
```

```
<!DOCTYPE html><html lang="en-US"><head><title>Just a moment...</title><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=Edge"><meta name="robots" content="noindex,nofollow"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="content-security-policy" content="default-src &#39;none&#39;; script-src &#39;nonce-DhknVG4tEJZBuyb1laxPeq&#39; &#39;unsafe-eval&#39; https://challenges.cloudflare.com; script-src-attr &#39;none&#39;; style-src &#39;unsafe-inline&#39;; img-src &#39;self&#39; https://challenges.cloudflare.com; connect-src &#39;self&#39; https://challenges.cloudflare.com; frame-src &#39;self&#39; https://challenges.cloudflare.com blob:; child-src &#39;self&#39; https://challenges.cloudflare.com blob:; worker-src blob:; form-action http: https:; base-uri &#39;self&#39;"><style>*{box-sizing:border-box;margin:0;padding:0}html{line-height:1.15;-webkit-text-size-adjust:100%;color:#313131;font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji"}body{display:flex;flex-direction:column;height:100vh;min-height:100vh}.main-content{margin:8rem auto;padding-left:1.5rem;max-width:60rem}@media (width <= 720px){.main-content{margin-top:4rem}}#challenge-error-text{background-image:url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zd
s2.pdf: HTML document, ASCII text, with very long lines (5660), with no line terminators
-rw-r--r-- 1 runner runner 5660 Oct 16 04:27 s2.pdf
s2.pdf: JSON text data
-rw-r--r-- 1 runner runner 46 Oct 16 04:27 s2.pdf
```

**Agent calls Bash**

```bash
cd paper; cat s2.pdf; echo; curl -s "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4919122/supplementaryFiles" ; echo; curl -s "https://pmc-oa-opendata.s3.amazonaws.com/?list-type=2&prefix=PMC4919122" | head -c 1500; echo; curl -s "https://pmc-oa-opendata.s3.amazonaws.com/?list-type=2&prefix=author_manuscript/" | head -c 800
```

Result: the fetched text is not kept.

**Agent calls ToolSearch**

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```

Result: no output.

**Agent calls WebFetch**

```json
{
 "url": "https://pmc.ncbi.nlm.nih.gov/articles/instance/4919122/bin/NIHMS788765-supplement-Materials_and_Methods__Figs__S1_to_S22__References.pdf",
 "prompt": "Return the full text of the Materials and Methods verbatim, especially: unit selection, place cell definition, spatial information, place field detection, candidate events / ripple detection, Bayesian decoding, weighted correlation, rZ, PCC, ΔPCC, rigid/plastic definition, firing rate, bursting index, ripple gain, coactivation. Also every number in figure legends S1-S22 (cell counts, medians, p values)."
}
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  rm -f paper/supp.pdf paper/s2.pdf; which python uv; python --version; python -c "import pynwb, h5py, remfile, dandi; print(pynwb.__version__)" 2>&1 | tail -1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
uv venv $TMPDIR/venv -q && VIRTUAL_ENV=$TMPDIR/venv uv pip install -q pynwb h5py remfile dandi numpy scipy pandas matplotlib 2>&1 | tail -3; $TMPDIR/venv/bin/python -c "import pynwb; print(pynwb.__version__)"
```

```
4.2.0
```

**Agent calls Bash**

```bash
cat > $TMPDIR/explore.py <<'E'
import h5py, remfile, sys
from dandi.dandiapi import DandiAPIClient
v=sys.argv[1]; path=sys.argv[2]
with DandiAPIClient() as c:
    a=c.get_dandiset("000044",v).get_asset_by_path(path)
    url=a.get_content_url(follow_redirects=1, strip_query=True)
f=h5py.File(remfile.File(url),'r')
def visit(name,obj):
    if isinstance(obj,h5py.Dataset):
        s=f"D {name} {obj.shape} {obj.dtype}"
        if obj.size<=5 and obj.dtype.kind in 'iufSO': 
            try: s+=f" = {obj[()]}"
            except Exception: pass
        print(s, dict((k,(v if not hasattr(v,'shape') or v.size<5 else v.shape)) for k,v in obj.attrs.items() if k not in ('namespace','object_id')))
    else:
        print(f"G {name}", dict((k,v) for k,v in obj.attrs.items() if k not in ('namespace','object_id')))
f.visititems(visit)
E
$TMPDIR/venv/bin/python $TMPDIR/explore.py 0.261005.2101 sub-Buddy/sub-Buddy_ses-Buddy-06272013_behavior+ecephys.nwb 2>&1 | grep -v "^D .*ElectricalSeries.*/data" | head -300
```

```
<persisted-output>
Output too large (127.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/7a0ab8ba-8a45-435d-8121-502432cbaf6d/tool-results/bwa2dejtm.txt

Preview (first 2KB):
G acquisition {}
G analysis {}
D file_create_date (1,) object = [b'2021-01-24T12:04:29.442727-05:00'] {}
G general {}
G general/devices {}
G general/devices/Device {'description': 'Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the ', 'neurodata_type': 'Device'}
D general/experimenter (1,) object = [b'Andres Grosmark'] {}
G general/extracellular_ephys {}
G general/extracellular_ephys/electrodes {'colnames': array(['x', 'y', 'z', 'imp', 'location', 'filtering', 'group',
       'group_name', 'shank_electrode_number', 'bad_electrode'],
      dtype=object), 'description': 'metadata about extracellular electrodes', 'neurodata_type': 'DynamicTable'}
D general/extracellular_ephys/electrodes/bad_electrode (128,) bool {'description': 'Indicator for if the electrode was removed from analysis due to low-amplitude or instabilities.', 'neurodata_type': 'VectorData'}
D general/extracellular_ephys/electrodes/filtering (128,) object {'description': 'description of hardware filtering', 'neurodata_type': 'VectorData'}
D general/extracellular_ephys/electrodes/group (128,) object {'description': 'a reference to the ElectrodeGroup this electrode is a part of', 'neurodata_type': 'VectorData'}
D general/extracellular_ephys/electrodes/group_name (128,) object {'description': 'the name of the ElectrodeGroup this electrode is a part of', 'neurodata_type': 'VectorData'}
D general/extracellular_ephys/electrodes/id (128,) int64 {'neurodata_type': 'ElementIdentifiers'}
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
grep -v -E "general/extracellular_ephys/(shank|Shank|ElectrodeGroup|electrode_group)|^G general/extracellular_ephys/[^/ ]+ \{'desc" /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/7a0ab8ba-8a45-435d-8121-502432cbaf6d/tool-results/bwa2dejtm.txt | cut -c1-400 | head -150; wc -l /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/7a0ab8ba-8a45-435d-8121-502432cbaf6d/tool-results/bwa2dejtm.txt
```

```
G acquisition {}
G analysis {}
D file_create_date (1,) object = [b'2021-01-24T12:04:29.442727-05:00'] {}
G general {}
G general/devices {}
G general/devices/Device {'description': 'Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the ', 'neurodata_type': 'Device'}
D general/experimenter (1,) object = [b'Andres Grosmark'] {}
G general/extracellular_ephys {}
G general/extracellular_ephys/electrodes {'colnames': array(['x', 'y', 'z', 'imp', 'location', 'filtering', 'group',
       'group_name', 'shank_electrode_number', 'bad_electrode'],
      dtype=object), 'description': 'metadata about extracellular electrodes', 'neurodata_type': 'DynamicTable'}
D general/extracellular_ephys/electrodes/bad_electrode (128,) bool {'description': 'Indicator for if the electrode was removed from analysis due to low-amplitude or instabilities.', 'neurodata_type': 'VectorData'}
D general/extracellular_ephys/electrodes/filtering (128,) object {'description': 'description of hardware filtering', 'neurodata_type': 'VectorData'}
D general/extracellular_ephys/electrodes/group (128,) object {'description': 'a reference to the ElectrodeGroup this electrode is a part of', 'neurodata_type': 'VectorData'}
D general/extracellular_ephys/electrodes/group_name (128,) object {'description': 'the name of the ElectrodeGroup this electrode is a part of', 'neurodata_type': 'VectorData'}
D general/extracellular_ephys/electrodes/id (128,) int64 {'neurodata_type': 'ElementIdentifiers'}
D general/extracellular_ephys/electrodes/imp (128,) float64 {'description': 'the impedance of the channel', 'neurodata_type': 'VectorData'}
D general/extracellular_ephys/electrodes/location (128,) object {'description': 'the location of channel within the subject e.g. brain region', 'neurodata_type': 'VectorData'}
D general/extracellular_ephys/electrodes/shank_electrode_number (128,) int64 {'description': '0-indexed channel within a shank.', 'neurodata_type': 'VectorData'}
D general/extracellular_ephy
[... 82 more lines not kept]
```

**Agent calls Bash**

```bash
grep -E "^(G|D) (acquisition|analysis|stimulus)" /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/7a0ab8ba-8a45-435d-8121-502432cbaf6d/tool-results/bwa2dejtm.txt | cut -c1-300; grep -E "ElectrodeGroup|shank" /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/7a0ab8ba-8a45-435d-8121-502432cbaf6d/tool-results/bwa2dejtm.txt | head -5 | cut -c1-400
```

```
G acquisition {}
G analysis {}
G stimulus {}
G stimulus/presentation {}
G stimulus/templates {}
       'group_name', 'shank_electrode_number', 'bad_electrode'],
D general/extracellular_ephys/electrodes/group (128,) object {'description': 'a reference to the ElectrodeGroup this electrode is a part of', 'neurodata_type': 'VectorData'}
D general/extracellular_ephys/electrodes/group_name (128,) object {'description': 'the name of the ElectrodeGroup this electrode is a part of', 'neurodata_type': 'VectorData'}
D general/extracellular_ephys/electrodes/shank_electrode_number (128,) int64 {'description': '0-indexed channel within a shank.', 'neurodata_type': 'VectorData'}
G general/extracellular_ephys/shank1 {'description': 'shank1 electrodes', 'location': 'unknown', 'neurodata_type': 'ElectrodeGroup'}
```

**Agent calls Bash**

```bash
cat > $TMPDIR/scan.py <<'E'
import h5py, remfile, sys, numpy as np, collections
from dandi.dandiapi import DandiAPIClient
v=sys.argv[1]
with DandiAPIClient() as c:
    assets=sorted(c.get_dandiset("000044",v).get_assets(), key=lambda a:a.path)
    urls=[(a.path,a.get_content_url(follow_redirects=1, strip_query=True)) for a in assets]
for p,u in urls:
    f=h5py.File(remfile.File(u),'r')
    print("=====",p, f['general/session_id'][()])
    ep=f['intervals/epochs']; print(" epochs", list(zip([x.decode() for x in ep['label'][:]], ep['start_time'][:], ep['stop_time'][:])))
    U=f['units']; ct=[x.decode() if isinstance(x,bytes) else x for x in U['cell_type'][:]]; loc=[x.decode() if isinstance(x,bytes) else x for x in U['location'][:]]
    print(" units", len(ct), collections.Counter(ct), collections.Counter(loc), "shank", U['shank_id'][:].min(), U['shank_id'][:].max(), "ids", U['id'][:5])
    idx=U['spike_times_index'][:]; st=U['spike_times'][:]
    starts=np.r_[0,idx[:-1]]; nonsorted=sum(np.any(np.diff(st[a:b])<0) for a,b in zip(starts,idx))
    print(" spikes", len(st), "range", st.min(), st.max(), "units unsorted", nonsorted, "dup spikes", sum(np.sum(np.diff(st[a:b])==0) for a,b in zip(starts,idx)))
    S=f['processing/behavior/states']; lab=[x.decode() for x in S['label'][:]]; d=S['stop_time'][:]-S['start_time'][:]
    print(" states", {k:(lab.count(k), round(float(d[np.array(lab)==k].sum()),1)) for k in set(lab)}, "range", S['start_time'][:].min(), S['stop_time'][:].max())
    for k in f['processing/behavior']:
        if k=='states': continue
        for k2 in f['processing/behavior'][k]:
            g=f['processing/behavior'][k][k2]; dat=g['data'][:]
            ts = g['timestamps'][:] if 'timestamps' in g else None
            print(" pos", k, k2, dat.shape, "nan frac", np.isnan(dat).mean().round(3), "min", np.nanmin(dat,0).round(3), "max", np.nanmax(dat,0).round(3), "start", g['starting_time'][()] if 'starting_time' in g else ts[0], g['starting_time'].attrs.get('rate') if 'starting_time' in g else 'ts')
    L=f['processing/ecephys/LFP/LFP']; print(" LFP", L['data'].shape, L['starting_time'].attrs['rate'], "dur s", L['data'].shape[0]/1250)
    E=f['general/extracellular_ephys/electrodes']; print(" electrodes", len(E['id']), "bad", E['bad_electrode'][:].sum(), set(x.decode() for x in E['location'][:]), "groups", len(set(E['group_name'][:])))
    print(" other in general", [k for k in f['general']], "acq", list(f['acquisition']), "analysis", list(f['analysis']), "intervals", list(f['intervals']))
E
$TMPDIR/venv/bin/python $TMPDIR/scan.py 0.261005.2101 2>&1 | grep -v Warning
```

```
===== sub-Achilles/sub-Achilles_ses-Achilles-10252013_behavior+ecephys.nwb b'Achilles_10252013'
 epochs [('PREEpoch', np.float64(0.0), np.float64(18079.5)), ('MazeEpoch', np.float64(18079.5), np.float64(20147.0)), ('POSTEpoch', np.float64(20147.0), np.float64(34861.1032))]
 units 137 Counter({'excitatory': 120, 'inhibitory': 17}) Counter({'rCA1': 72, 'lCA1': 65}) shank 0 38 ids [1 2 6 7 9]
 spikes 8414607 range 0.03615 34861.09765 units unsorted 0 dup spikes 0
 states {'Awake': (62, 16747.0), 'Non-REM': (60, 15890.0), 'REM': (22, 2071.0)} range 5.0 34856.0
 pos 1.6mLinearMazeLinearizedPosition 1.6mLinearMazeLinearizedTimeSeries (80762, 1) nan frac 0.872 min [0.] max [1.6] start 18079.5 39.06263603480421
 pos 1.6mLinearMazePosition 1.6mLinearMazeSpatialSeries (80762, 2) nan frac 0.214 min [-0.6   -0.572] max [1.385 1.628] start 18079.5 39.06263603480421
 LFP (43576379, 128) 1250.0 dur s 34861.1032
 electrodes 128 bad 0 {'unknown'} groups 14
 other in general ['devices', 'experimenter', 'extracellular_ephys', 'institution', 'lab', 'related_publications', 'session_id', 'subject'] acq [] analysis [] intervals ['epochs']
===== sub-Achilles/sub-Achilles_ses-Achilles-11012013_behavior+ecephys.nwb b'Achilles_11012013'
 epochs [('PREEpoch', np.float64(0.0), np.float64(19330.0)), ('MazeEpoch', np.float64(19330.0), np.float64(22004.1)), ('POSTEpoch', np.float64(22004.1), np.float64(36629.212))]
 units 104 Counter({'excitatory': 92, 'inhibitory': 12}) Counter({'rCA1': 61, 'lCA1': 43}) shank 0 36 ids [1 2 3 4 5]
 spikes 7665373 range 0.00245 36629.2088 units unsorted 0 dup spikes 0
 states {'Awake': (134, 19056.0), 'Non-REM': (133, 16094.0), 'REM': (17, 1186.0)} range 5.0 36624.0
 pos CircularMazeLinearizedPosition CircularMazeLinearizedTimeSeries (104457, 1) nan frac 0.415 min [0.] max [2.9] start 19330.0 39.06248831360942
 pos CircularMazePosition CircularMazeSpatialSeries (104457, 2) nan frac 0.185 min [-0.166 -0.177] max [1.128 1.161] start 19330.0 39.06248831360942
 LFP (45
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/chunk.py <<'E'
import h5py, remfile, time
from dandi.dandiapi import DandiAPIClient
with DandiAPIClient() as c:
    a=c.get_dandiset("000044","0.261005.2101").get_asset_by_path("sub-Buddy/sub-Buddy_ses-Buddy-06272013_behavior+ecephys.nwb")
    u=a.get_content_url(follow_redirects=1, strip_query=True)
f=h5py.File(remfile.File(u),'r')
d=f['processing/ecephys/LFP/LFP/data']; print(d.chunks, d.compression)
print(f['units/spike_times'].chunks, f['units/spike_times'].compression)
t=time.time(); x=d[:1250*600, 5]; print("10 min one ch", time.time()-t)
E
$TMPDIR/venv/bin/python $TMPDIR/chunk.py
```

```
(102807, 1) gzip
None None
10 min one ch 1.5034775733947754
```

**Agent calls Bash**

```bash
cat > $TMPDIR/t2.py <<'E'
import h5py, remfile, time, numpy as np
from concurrent.futures import ThreadPoolExecutor
from dandi.dandiapi import DandiAPIClient
with DandiAPIClient() as c:
    a=c.get_dandiset("000044","0.261005.2101").get_asset_by_path("sub-Buddy/sub-Buddy_ses-Buddy-06272013_behavior+ecephys.nwb")
    u=a.get_content_url(follow_redirects=1, strip_query=True)
t=time.time(); f=h5py.File(remfile.File(u),'r'); st=f['units/spike_times'][:]; print("spikes", time.time()-t, st.nbytes/1e6)
d=f['processing/ecephys/LFP/LFP/data']; n=d.shape[0]; ch=d.chunks[0]
def rd(i):
    g=h5py.File(remfile.File(u),'r'); return g['processing/ecephys/LFP/LFP/data'][i:min(i+ch*20,n),5]
t=time.time()
with ThreadPoolExecutor(8) as ex: parts=list(ex.map(rd, range(0,n,ch*20)))
x=np.concatenate(parts); print("full ch threads", time.time()-t, x.shape)
E
$TMPDIR/venv/bin/python $TMPDIR/t2.py
```

```
spikes 1.3172435760498047 51.29804
full ch threads 53.65725541114807 (26318375,)
```

**Agent calls Bash**

```bash
cd paper; for i in 1 2 3 4; do curl -sL -A "Mozilla/5.0" "https://europepmc.org/articles/PMC4919122/bin/nihms788765f$i.jpg" -o f$i.jpg; file f$i.jpg; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  rm -f paper/f*.jpg; for v in 0.210812.1516 0.261005.2101; do $TMPDIR/venv/bin/python $TMPDIR/explore.py $v sub-Gatsby/sub-Gatsby_ses-Gatsby-08022013_behavior+ecephys.nwb 2>/dev/null | grep -v "^D specifications" > $TMPDIR/l_$v.txt; done; diff $TMPDIR/l_0.210812.1516.txt $TMPDIR/l_0.261005.2101.txt | cut -c1-400
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
nproc; free -g | head -2
```

```
4
               total        used        free      shared  buff/cache   available
Mem:              15           1          10           0           4          14
```

**Agent calls Write**

```json
{
 "file_path": "claims/000044/10.1126-science.aad1935.yaml",
 "content": "# Claims for Grosmark & Buzsaki (2016), Science 351:1440, on dandiset 000044.\n# Source: the NIH author manuscript in PubMed Central (PMC4919122), full main text and the\n# legends of Figures 1 to 4. The supplementary Materials and Methods (figs. S1 to S22) could\n# not be retrieved: PMC and Science serve the supplement only behind a browser check, and\n# Europe PMC does not hold it. Every definition the main text does not give (place cells,\n# candidate events, the shuffles, the PCC test, bursting) is a common choice fixed here, and\n# each is a deviation. Neither the paper nor the dandiset links analysis code.\n#\n# When these criteria were written, the author had seen the data check only: the file list\n# and the full HDF5 listing of one file, and for every file the counts of units by cell type\n# and hemisphere, the epochs, the totals of the sleep-state intervals, the ranges of the\n# positions, the shape of the LFP and the difference between versions. No claim's analysis\n# had been run.\n#\n# Method choices fixed here, for all claims:\n# - Pyramidal cells are units with cell_type \"excitatory\".\n# - Running is MAZE time with a linearized position and a speed above 5 cm/s (speed from the\n#   linearized position smoothed with a 0.25 s Gaussian). On the linear tracks runs are split\n#   by the sign of the velocity into two directions, each with its own template; on the\n#   circular track there is one template.\n# - Rate maps use 2 cm bins smoothed with a Gaussian of 4 cm (2 bins). A place cell is a\n#   pyramidal cell whose smoothed rate map peaks at 1 Hz or more in at least one direction;\n#   it belongs to the template of each direction in which it reaches 1 Hz.\n# - Candidate events are population bursts of all units (1 ms bins, Gaussian of 10 ms,\n#   z-scored over the session): a peak at z 3 or more, bounded where z falls to 0, lasting 50\n#   to 500 ms, during which the ripple envelope (150 to 250 Hz, on the LFP channel with the\n#   most ripple-band power) reaches 3 SD above its non-REM mean. In PRE and POST they are\n#   outside REM; in MAZE the head speed (2D position) is below 5 cm/s. An event needs at least\n#   5 active cells of the template it is decoded with.\n# - Decoding: Poisson Bayesian decoder with a flat prior, 20 ms bins, bins without spikes left\n#   out. The sequence score is the weighted correlation r between position and time, and rZ is\n#   (|r| minus the mean |r| of 200 column-cycle shuffles) over their SD. On the linear tracks an\n#   event takes the template with the larger rZ.\n# - PCC: for each event of PRE or POST and each active cell of its template, the contribution\n#   is |r| minus the mean |r| over 20 decodings with that cell's rate map circularly shifted by\n#   a random amount. A cell's PCC in an epoch is the mean of its contributions there; a cell is\n#   strongly contributing in an epoch when a one-sided Wilcoxon signed-rank test of its\n#   contributions against 0 gives p < 0.05 with at least 5 events. dPCC is PCC in POST minus\n#   PCC in PRE. Rigid cells are strongly contributing cells below the median dPCC of the\n#   session's strongly contributing cells, plastic cells above it.\n# - Statistics across epochs: Kruskal-Wallis on the event rZ of all sessions pooled, then\n#   Tukey's HSD on the ranks (MATLAB's multcompare after kruskalwallis), alpha 0.05.\nschema_version: 1\ndandiset: \"000044\"\npaper: doi:10.1126/science.aad1935\nclaims:\n- id: sessions-and-tracks\n  statement: Recordings were made in four rats, in eight novel exploration sessions, each a\n    PRE sleep, a MAZE epoch on one of two linear tracks or a circular track, and a POST sleep.\n  source: Results, paragraph 2; Figure S1 (as cited in the text)\n  criterion: Reproduced when the dandiset holds 4 subjects and 8 sessions, each with PRE, MAZE\n    and POST epochs in this order, and the MAZE positions come from two linear tracks and one\n    circular track.\n- id: place-cell-count\n  statement: The Bayesian decoder was built from 491 place cells over the eight sessions.\n  source: Results, paragraph 2\n  expected:\n    quantity: place cells over 8 sessions\n    value: 491\n    tolerance: 49\n  criterion: Place cells as defined in the opening comment. The 1 Hz threshold is a choice;\n    0.5 and 2 Hz are shown as variants and do not change the outcome.\n- id: fig1c-post-gt-pre\n  statement: Sequence scores (rZ) of candidate events are higher in POST sleep than in PRE\n    sleep (replay).\n  source: Figure 1C\n  depends_on:\n  - place-cell-count\n  criterion: Reproduced when the mean rZ of POST events exceeds that of PRE events and the\n    Tukey comparison on ranks after Kruskal-Wallis gives p < 0.05. Results per session are\n    shown; partially reproduced when the pooled test holds but fewer than 5 of 8 sessions\n    have a higher POST mean.\n- id: fig1c-maze-gt-pre\n  statement: Sequence content is higher in MAZE immobility events than in PRE sleep events.\n  source: Figure 1C; Figure 2C legend\n  depends_on:\n  - place-cell-count\n  criterion: As for fig1c-post-gt-pre, with MAZE events in place of POST events.\n- id: fig2b-strong-contributors\n  statement: 216 neurons showed significant PCC scores in PRE or POST and were considered to\n    contribute strongly to sequences.\n  source: Results, paragraph 3; Figure 2B\n  depends_on:\n  - place-cell-count\n  expected:\n    quantity: strongly contributing neurons\n    value: 216\n    tolerance: 21.6\n  criterion: Strongly contributing as defined in the opening comment. A false-positive rate\n    for the PCC test is computed by repeating it with every rate map shifted, and shown.\n- id: fig2-pre-post-overlap\n  statement: Most neurons strongly contributing to PRE sequences (73%) also contributed to POST\n    sequences.\n  source: Results, paragraph 3; Figure 2C as cited\n  depends_on:\n  - fig2b-strong-contributors\n  expected:\n    quantity: fraction of PRE strongly contributing neurons also strongly contributing in POST\n    value: 73\n    tolerance: 7.3\n    unit: percent\n  criterion: The fraction is pooled over sessions. Its chance level, the fraction of all\n    place cells that are strongly contributing in POST, is shown.\n- id: fig2d-shuffle-high-dpcc\n  statement: The PRE to POST increase in sequence score is eliminated when the place fields\n    of the 10 to 20% of cells with the highest dPCC are shuffled, and remains after shuffling\n    the bottom 75%.\n  source: Results, paragraph 3; Figure 2D\n  depends_on:\n  - fig2b-strong-contributors\n  criterion: Within each session the place cells are ranked by dPCC; the rate maps of the top\n    or bottom X% (X = 10, 20, 50, 75) are circularly shifted by random amounts and PRE and POST\n    events are decoded again. Replay is present when the mean POST rZ exceeds the mean PRE rZ\n    with a one-sided rank-sum p < 0.05 (pooled over sessions). Reproduced when replay is absent\n    after shuffling the top 10% or the top 20%, and present after shuffling the bottom 75%.\n    Partially reproduced when only one of the two holds.\n- id: fig2e-remove-plastic\n  statement: The PRE to POST increase in sequence content is attributable to a small number of\n    plastic cells; removing them, unlike removing rigid cells, removes the increase.\n  source: Figure 2E\n  depends_on:\n  - fig2b-strong-contributors\n  criterion: Events are decoded again with plastic cells removed from the templates, and with\n    rigid cells removed. Replay as in fig2d-shuffle-high-dpcc. Reproduced when replay is absent\n    without plastic cells and present without rigid cells; partially reproduced when replay\n    remains in both cases but the POST minus PRE difference without plastic cells is less than\n    half of that without rigid cells.\n- id: figs2-track-distribution\n  statement: Rigid and plastic neurons were similarly distributed along the track.\n  source: Results, paragraph 3; fig. S2 as cited\n  depends_on:\n  - fig2b-strong-contributors\n  criterion: The position of each cell's rate-map peak (in its direction of higher peak),\n    as a fraction of the track length, is compared between rigid and plastic cells with a\n    two-sample Kolmogorov-Smirnov test. Reproduced when p >= 0.05 (the claim is of absence;\n    the paper's test is not known, so this test is fixed here).\n- id: fig3a-plastic-specificity\n  statement: Plastic neurons had higher place-specific indices and fewer place fields than\n    rigid cells.\n  source: Results, paragraph 4; Figure 3A\n  depends_on:\n  - fig2b-strong-contributors\n  criterion: Spatial information (Skaggs, bits per spike) and the number of place fields\n    (contiguous runs of at least 3 bins at 1 Hz or more and at 20% of the peak or more), both\n    from the rate map of the direction with the higher peak, compared with rank-sum tests.\n    Reproduced when plastic cells have higher spatial information and fewer fields, each with\n    p < 0.05; partially reproduced when one of the two holds.\n- id: fig3b-plastic-improve\n  statement: Plastic but not rigid neurons increased their spatial specificity (in-field\n    versus out-of-field firing ratio) steadily during the MAZE session.\n  source: Results, paragraph 4; Figure 3B\n  depends_on:\n  - fig2b-strong-contributors\n  criterion: In-field bins are those of the cell's largest field on the whole-session map. For\n    each cell the in-field over out-of-field rate is computed in the first and the last third\n    of its running time; the change (last minus first, of the log ratio) is tested against 0\n    with a one-sided Wilcoxon signed-rank test per group. Reproduced when plastic cells\n    increase with p < 0.05 and rigid cells do not; partially reproduced when both increase;\n    not reproduced when plastic cells do not.\n- id: fig4a-rigid-faster\n  statement: Session-wide firing rates of rigid neurons were higher than those of plastic\n    neurons.\n  source: Results, paragraph 5; Figure 4A\n  depends_on:\n  - fig2b-strong-contributors\n  criterion: Spike count over the whole recording duration, rank-sum test, p < 0.05 with the\n    rigid median higher.\n- id: fig4a-plastic-ripple-burst-coactivation\n  statement: Ripple-related spiking, bursting and pairwise coactivation were higher in plastic\n    than in rigid neurons.\n  source: Results, paragraph 5; Figure 4A\n  depends_on:\n  - fig2b-strong-contributors\n  criterion: Ripple-related spiking is the rate within PRE and POST candidate events over the\n    session rate; bursting is the fraction of spikes with an inter-spike interval of 6 ms or\n    less to a neighbour; coactivation is a cell's mean Pearson correlation of 100 ms spike\n    counts with the session's other place cells over the whole session. Rank-sum tests.\n    Reproduced when all three are higher in plastic cells with p < 0.05, partially reproduced\n    for one or two, not reproduced for none.\n- id: fig4c-pre-fast-coactivation\n  statement: In PRE sleep, coactivation was dominated by fast-firing neurons.\n  source: Results, paragraph 5; Figure 4C\n  depends_on:\n  - place-cell-count\n  criterion: Place cells of each session are sorted by session firing rate and grouped into\n    windows of 20% of the cells, stepped by 1% (as the legend states). For each window the\n    mean pairwise Pearson correlation of 100 ms counts in PRE is computed; curves are averaged\n    over sessions by window position. Reproduced when the Spearman correlation between window\n    position and PRE coactivation on the averaged curve is above 0.5 and at least 5 of 8\n    sessions have a positive correlation.\n- id: fig4c-slow-coactivation-increase\n  statement: Slow-firing neurons showed the strongest increases in coactivation from PRE to\n    POST sleep.\n  source: Results, paragraph 5; Figure 4C\n  depends_on:\n  - place-cell-count\n  criterion: As in fig4c-pre-fast-coactivation, on POST minus PRE coactivation. Reproduced when\n    the Spearman correlation on the averaged curve is below -0.5 and at least 5 of 8 sessions\n    have a negative correlation.\n- id: fig4c-slow-replay\n  statement: Slow-firing cells showed the greatest replay, the partial correlation between RUN\n    and POST coactivation accounting for PRE.\n  source: Figure 4C legend\n  depends_on:\n  - place-cell-count\n  criterion: For each window, the partial correlation across its cell pairs between MAZE\n    running and POST coactivation given PRE coactivation. Reproduced when the Spearman\n    correlation on the averaged curve is below -0.5 and at least 5 of 8 sessions have a\n    negative correlation.\n- id: rate-split-medians\n  statement: Place cells divided into equal groups by sleep firing rate have medians of 0.39\n    Hz (low-rate) and 1.12 Hz (high-rate).\n  source: Results, paragraph 6\n  depends_on:\n  - place-cell-count\n  expected:\n  - quantity: median sleep firing rate of low-rate place cells\n    value: 0.39\n    tolerance: 0.039\n    unit: Hz\n  - quantity: median sleep firing rate of high-rate place cells\n    value: 1.12\n    tolerance: 0.112\n    unit: Hz\n  criterion: Sleep firing rate is the rate over PRE and POST outside REM and awake periods,\n    that is in non-REM sleep. The paper does not say whether the split is per session or\n    pooled; the readings are (a) a median split within each session, (b) a median split of all\n    place cells pooled. Reproduced when both medians are within tolerance under one reading.\n    The rate over the whole of PRE and POST is shown as a variant.\n- id: figs16-low-rate-info-gain\n  statement: Low-rate neurons carried more spatial information per spike on the maze, and\n    increased their within-ripple firing-rate gain from PRE to POST more than high-rate cells.\n  source: Results, paragraph 6; fig. S16 as cited\n  depends_on:\n  - rate-split-medians\n  criterion: Under the reading of rate-split-medians that matches (reading (a) if neither or\n    both do), rank-sum tests of spatial information and of the change in gain (rate within\n    candidate events over the epoch rate, POST minus PRE). Reproduced when low-rate cells are\n    higher on both with p < 0.05, partially reproduced for one.\n- id: fig4d-slow-sequences\n  statement: Slow-firing, but not fast-firing, neurons increased their contribution to\n    sequences from PRE to POST sleep, in a decoding restricted to each group.\n  source: Results, paragraph 6; Figure 4D\n  depends_on:\n  - rate-split-medians\n  criterion: Templates are restricted to the low-rate or the high-rate half (split as in\n    figs16-low-rate-info-gain) and PRE and POST events decoded again. Replay as in\n    fig2d-shuffle-high-dpcc. Reproduced when replay is present for low-rate cells and absent\n    for high-rate cells; partially reproduced when present for both with a larger POST minus\n    PRE difference for low-rate cells.\n- id: fig4e-gain-sequences\n  statement: PRE to POST increases in sequence content were limited to cells with high\n    ripple-specific recruitment (gain).\n  source: Results, paragraph 6; Figure 4E\n  depends_on:\n  - place-cell-count\n  criterion: Gain is the rate within PRE and POST candidate events over the PRE and POST rate;\n    place cells are split at the session median. Decoding and replay as in\n    fig4d-slow-sequences. Reproduced when replay is present for high-gain cells and absent for\n    low-gain cells; partially reproduced when present for both with a larger difference for\n    high-gain cells.\n"
}
```

```
File created successfully at: claims/000044/10.1126-science.aad1935.yaml (file state is current in your context — no need to Read it back)
```

**Agent**

Claims are written (20 claims, criteria fixed before any analysis). Now writing the helper module.

**Agent calls Write**

```json
{
 "file_path": "entries/000044-grosmark-2016/grosmark.py",
 "content": "\"\"\"Loading and measures for dandiset 000044 (Grosmark & Buzsaki 2016, Science 351:1440).\n\nThe dandiset holds eight sessions from four rats. Each file covers PRE sleep in the home cage,\na MAZE epoch on a novel track, and POST sleep, with sorted units (`cell_type` excitatory or\ninhibitory), LFP at 1250 Hz on 128 channels, sleep states and the position on the track.\n\nEvery file is streamed from the archive at a pinned version. `prepare_session` reduces a file\nto what the analysis needs: spike times of every unit, the epochs, the sleep states, the\npositions, one LFP channel's ripple envelope at the candidate events, and the outputs of the\ndata checks.\n\nWhere parameters come from. The paper's supplementary Materials and Methods could not be read\n(see the notebook), so the parameters below are common choices in the hippocampal replay\nliterature unless marked otherwise:\n\n- 20 ms decoding bins: the paper's main text (Results, paragraph 2).\n- 100 ms bins for pairwise coactivation and windows of 20% of cells stepped by 1%: the legend\n  of Figure 4.\n- Speed threshold 5 cm/s, 2 cm position bins, 4 cm Gaussian smoothing, 1 Hz peak for a place\n  cell, field threshold 20% of peak: common choices.\n- Ripple band 150 to 250 Hz, envelope smoothed with an 8 ms Gaussian, threshold 3 SD over\n  non-REM sleep; population bursts from all units in 1 ms bins, 10 ms Gaussian, peak z >= 3,\n  bounded at z = 0, 50 to 500 ms: common choices.\n- Burst ISI 6 ms: a common choice for CA1 pyramidal cells.\n- 200 column-cycle shuffles for rZ, 20 circular shifts per cell for PCC: choices made here.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport numpy as np\nimport h5py\nimport remfile\nfrom scipy import signal\nfrom scipy.ndimage import gaussian_filter1d\n\nDANDISET = \"000044\"\nVERSION = \"0.261005.2101\"\nLFP_RATE = 1250.0\n\nBIN_CM = 2.0            # position bin (cm)\nSMOOTH_BINS = 2.0       # Gaussian SD of the rate map smoothing, in bins (4 cm)\nRUN_SPEED = 5.0         # cm/s\nPLACE_PEAK = 1.0        # Hz\nDECODE_BIN = 0.02       # s, from the paper\nMIN_ACTIVE = 5          # active template cells per event\nN_SHUFFLE = 200         # column-cycle shuffles per event\nN_PCC_SHIFT = 20        # circular shifts per cell and event for PCC\nBURST_ISI = 0.006       # s\n\n\n# ----------------------------------------------------------------------------- access\n\ndef asset_urls(version: str = VERSION) -> list[tuple[str, str]]:\n    \"\"\"(path, S3 URL) of every NWB file of the dandiset version, sorted by path.\"\"\"\n    from dandi.dandiapi import DandiAPIClient\n    with DandiAPIClient() as client:\n        ds = client.get_dandiset(DANDISET, version)\n        assets = sorted(ds.get_assets(), key=lambda a: a.path)\n        return [(a.path, a.get_content_url(follow_redirects=1, strip_query=True)) for a in assets]\n\n\ndef open_nwb(url: str) -> h5py.File:\n    return h5py.File(remfile.File(url), \"r\")\n\n\ndef _text(values) -> list[str]:\n    return [v.decode() if isinstance(v, bytes) else str(v) for v in values]\n\n\n# ----------------------------------------------------------------------------- loading\n\ndef load_session(f: h5py.File) -> dict:\n    \"\"\"Everything but the LFP, from an open file.\"\"\"\n    s = {\"session\": f[\"general/session_id\"][()].decode(),\n         \"subject\": f[\"general/subject/subject_id\"][()].decode()}\n    ep = f[\"intervals/epochs\"]\n    s[\"epochs\"] = {lab: (float(a), float(b)) for lab, a, b in\n                   zip(_text(ep[\"label\"][:]), ep[\"start_time\"][:], ep[\"stop_time\"][:])}\n    st = f[\"processing/behavior/states\"]\n    s[\"states\"] = {\"label\": np.array(_text(st[\"label\"][:])),\n                   \"start\": st[\"start_time\"][:].astype(float),\n                   \"stop\": st[\"stop_time\"][:].astype(float)}\n    u = f[\"units\"]\n    idx = u[\"spike_times_index\"][:]\n    times = u[\"spike_times\"][:]\n    s[\"spikes\"] = np.split(times, idx[:-1])\n    s[\"unit_id\"] = u[\"id\"][:]\n    s[\"cell_type\"] = np.array(_text(u[\"cell_type\"][:]))\n    s[\"location\"] = np.array(_text(u[\"location\"][:]))\n    s[\"shank_id\"] = u[\"shank_id\"][:]\n    beh = f[\"processing/behavior\"]\n    for name in beh:\n        if name == \"states\":\n            continue\n        for sub in beh[name]:\n            g = beh[name][sub]\n            n = g[\"data\"].shape[0]\n            rate = float(g[\"starting_time\"].attrs[\"rate\"])\n            t = float(g[\"starting_time\"][()]) + np.arange(n) / rate\n            key = \"lin\" if \"Linearized\" in name else \"xy\"\n            s[key] = {\"t\": t, \"data\": g[\"data\"][:], \"rate\": rate, \"name\": name,\n                      \"unit\": g[\"data\"].attrs[\"unit\"]}\n    s[\"track\"] = s[\"lin\"][\"name\"].replace(\"LinearizedPosition\", \"\")\n    lfp = f[\"processing/ecephys/LFP/LFP\"]\n    s[\"lfp_shape\"] = lfp[\"data\"].shape\n    s[\"lfp_rate\"] = float(lfp[\"starting_time\"].attrs[\"rate\"])\n    s[\"lfp_conversion\"] = float(lfp[\"data\"].attrs[\"conversion\"])\n    s[\"bad_electrode\"] = f[\"general/extracellular_ephys/electrodes/bad_electrode\"][:]\n    return s\n\n\ndef state_mask(t: np.ndarray, s: dict, label: str) -> np.ndarray:\n    \"\"\"True where t falls in an interval of the given sleep-state label.\"\"\"\n    st = s[\"states\"]\n    sel = st[\"label\"] == label\n    return in_intervals(t, st[\"start\"][sel], st[\"stop\"][sel])\n\n\ndef in_intervals(t, starts, stops) -> np.ndarray:\n    order = np.argsort(starts)\n    starts, stops = np.asarray(starts)[order], np.asarray(stops)[order]\n    i = np.searchsorted(starts, t, side=\"right\") - 1\n    ok = i >= 0\n    out = np.zeros(len(t), bool)\n    out[ok] = t[ok] < stops[i[ok]]\n    return out\n\n\n# ----------------------------------------------------------------------------- LFP\n\ndef read_channel(url: str, ch: int, start: int = 0, stop: int | None = None) -> np.ndarray:\n    with open_nwb(url) as f:\n        d = f[\"processing/ecephys/LFP/LFP/data\"]\n        return d[start:stop, ch].astype(np.float32) * np.float32(d.attrs[\"conversion\"] * 1e6)  # uV\n\n\ndef ripple_band(x: np.ndarray) -> np.ndarray:\n    sos = signal.butter(3, [150, 250], btype=\"band\", fs=LFP_RATE, output=\"sos\")\n    return signal.sosfiltfilt(sos, x).astype(np.float32)\n\n\ndef ripple_envelope(x: np.ndarray) -> np.ndarray:\n    y = ripple_band(x)\n    return np.sqrt(gaussian_filter1d(y * y, 0.008 * LFP_RATE)).astype(np.float32)\n\n\ndef choose_ripple_channel(url: str, s: dict) -> tuple[int, np.ndarray]:\n    \"\"\"The good channel with the most ripple-band power in one LFP chunk of POST non-REM.\n\n    Returns the channel and the ripple-band power of every channel (NaN for bad ones).\"\"\"\n    st = s[\"states\"]\n    post0 = s[\"epochs\"][\"POSTEpoch\"][0]\n    sel = (st[\"label\"] == \"Non-REM\") & (st[\"start\"] >= post0)\n    i = np.argmax(np.where(sel, st[\"stop\"] - st[\"start\"], -1))\n    with open_nwb(url) as f:\n        d = f[\"processing/ecephys/LFP/LFP/data\"]\n        chunk = d.chunks[0]\n        a = int(np.ceil(st[\"start\"][i] * LFP_RATE / chunk)) * chunk\n        b = min(a + chunk, int(st[\"stop\"][i] * LFP_RATE))\n        power = np.full(d.shape[1], np.nan)\n        for ch in range(d.shape[1]):\n            if s[\"bad_electrode\"][ch]:\n                continue\n            x = d[a:b, ch].astype(np.float32) * np.float32(d.attrs[\"conversion\"] * 1e6)\n            power[ch] = float(np.mean(ripple_band(x) ** 2))\n    return int(np.nanargmax(power)), power\n\n\ndef band_power(x: np.ndarray, lo: float, hi: float) -> float:\n    f, p = signal.welch(x, fs=LFP_RATE, nperseg=2048)\n    return float(p[(f >= lo) & (f < hi)].mean())\n\n\ndef theta_delta(x: np.ndarray, s: dict, shift: float = 0.0) -> dict:\n    \"\"\"Mean theta (6-10 Hz) over delta (1-4 Hz) power ratio in REM and non-REM intervals of at\n    least 10 s, with the state labels shifted in time by `shift` seconds.\"\"\"\n    st = s[\"states\"]\n    out = {}\n    for lab in (\"REM\", \"Non-REM\"):\n        ratios = []\n        for a, b in zip(st[\"start\"][st[\"label\"] == lab], st[\"stop\"][st[\"label\"] == lab]):\n            a, b = a + shift, b + shift\n            if b - a < 10 or a < 0 or b * LFP_RATE > len(x):\n                continue\n            seg = x[int(a * LFP_RATE):int(b * LFP_RATE)]\n            ratios.append(band_power(seg, 6, 10) / band_power(seg, 1, 4))\n        out[lab] = float(np.median(ratios)) if ratios else np.nan\n    return out\n\n\n# ----------------------------------------------------------------------------- behaviour\n\ndef lin_speed(s: dict) -> tuple[np.ndarray, np.ndarray, np.ndarray]:\n    \"\"\"Time, linearized position (cm) and signed velocity (cm/s), NaN off the track.\"\"\"\n    t, x = s[\"lin\"][\"t\"], s[\"lin\"][\"data\"][:, 0] * 100.0\n    rate = s[\"lin\"][\"rate\"]\n    ok = np.isfinite(x)\n    xi = np.interp(t, t[ok], x[ok])\n    xs = gaussian_filter1d(xi, 0.25 * rate)\n    v = np.gradient(xs) * rate\n    v[~ok] = np.nan\n    return t, np.where(ok, x, np.nan), v\n\n\ndef xy_speed(s: dict) -> tuple[np.ndarray, np.ndarray]:\n    \"\"\"Time and 2D head speed (cm/s, in the file's units times 100), NaN where untracked.\"\"\"\n    t, xy = s[\"xy\"][\"t\"], s[\"xy\"][\"data\"] * 100.0\n    rate = s[\"xy\"][\"rate\"]\n    ok = np.all(np.isfinite(xy), axis=1)\n    sm = np.column_stack([gaussian_filter1d(np.interp(t, t[ok], xy[ok, k]), 0.25 * rate)\n                          for k in range(2)])\n    sp = np.hypot(*np.gradient(sm, axis=0).T) * rate\n    sp[~ok] = np.nan\n    return t, sp\n\n\ndef track_length(s: dict) -> float:\n    \"\"\"Track length in cm from the name of the position series; the circular track is taken\n    as the largest linearized position.\"\"\"\n    name = s[\"track\"]\n    if name.startswith(\"1.6m\"):\n        return 160.0\n    if name.startswith(\"2m\"):\n        return 200.0\n    return float(np.nanmax(s[\"lin\"][\"data\"]) * 100.0)\n\n\ndef directions(s: dict) -> list[int]:\n    \"\"\"+1 and -1 on the linear tracks; +1 only on the circular track.\"\"\"\n    return [1] if s[\"track\"].startswith(\"Circular\") else [1, -1]\n\n\ndef run_samples(s: dict, direction: int) -> tuple[np.ndarray, np.ndarray]:\n    \"\"\"Times and positions (cm) of running samples in one direction.\"\"\"\n    t, x, v = lin_speed(s)\n    m = np.isfinite(x) & np.isfinite(v) & (direction * v > RUN_SPEED)\n    return t[m], x[m]\n\n\ndef rate_map(spk: np.ndarray, t_run: np.ndarray, x_run: np.ndarray, length: float,\n             dt: float) -> tuple[np.ndarray, np.ndarray]:\n    \"\"\"Smoothed rate map (Hz) and smoothed occupancy (s) on 2 cm bins.\n\n    Spikes are assigned the position of the nearest running sample within one sample.\"\"\"\n    nb = int(np.ceil(length / BIN_CM))\n    edges = np.arange(nb + 1) * BIN_CM\n    occ = np.histogram(x_run, edges)[0] * dt\n    j = np.searchsorted(t_run, spk)\n    j = np.clip(j, 1, len(t_run) - 1)\n    near = np.where(np.abs(t_run[j - 1] - spk) < np.abs(t_run[j] - spk), j - 1, j)\n    keep = np.abs(t_run[near] - spk) <= dt\n    cnt = np.histogram(x_run[near[keep]], edges)[0].astype(float)\n    occ_s = gaussian_filter1d(occ, SMOOTH_BINS)\n    cnt_s = gaussian_filter1d(cnt, SMOOTH_BINS)\n    with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n        rm = np.where(occ_s > 0.05, cnt_s / occ_s, 0.0)\n    return rm, occ\n\n\ndef spatial_info(rm: np.ndarray, occ: np.ndarray) -> float:\n    \"\"\"Skaggs information, bits per spike.\"\"\"\n    p = occ / occ.sum()\n    lam = np.sum(p * rm)\n    if lam <= 0:\n        return np.nan\n    r = rm / lam\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        terms = np.where(r > 0, p * r * np.log2(r), 0.0)\n    return float(np.sum(terms))\n\n\ndef place_fields(rm: np.ndarray) -> list[np.ndarray]:\n    \"\"\"Contiguous runs of at least 3 bins at 1 Hz or more and 20% of the peak or more.\"\"\"\n    above = (rm >= PLACE_PEAK) & (rm >= 0.2 * rm.max())\n    fields, i = [], 0\n    while i < len(rm):\n        if above[i]:\n            j = i\n            while j < len(rm) and above[j]:\n                j += 1\n            if j - i >= 3:\n                fields.append(np.arange(i, j))\n            i = j\n        else:\n            i += 1\n    return fields\n\n\n# ----------------------------------------------------------------------------- events\n\ndef runs_of(mask: np.ndarray) -> tuple[np.ndarray, np.ndarray]:\n    d = np.diff(np.r_[0, mask.astype(np.int8), 0])\n    return np.flatnonzero(d == 1), np.flatnonzero(d == -1)\n\n\ndef population_bursts(spikes: list[np.ndarray], t_end: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:\n    \"\"\"Population bursts of all units: start, stop (s) and peak z of each, before the ripple\n    and immobility conditions.\"\"\"\n    n = int(np.ceil(t_end / 0.001)) + 1\n    cnt = np.bincount((np.concatenate(spikes) / 0.001).astype(np.int64), minlength=n)[:n]\n    z = gaussian_filter1d(cnt.astype(np.float32), 10.0)\n    z = (z - z.mean()) / z.std()\n    a, b = runs_of(z > 0)\n    peak = np.maximum.reduceat(z, a) if len(a) else np.array([])\n    dur = (b - a) * 0.001\n    keep = (peak >= 3) & (dur >= 0.05) & (dur <= 0.5)\n    return a[keep] * 0.001, b[keep] * 0.001, peak[keep]\n\n\ndef segment_max(x: np.ndarray, starts: np.ndarray, stops: np.ndarray) -> np.ndarray:\n    a = np.clip((starts * LFP_RATE).astype(np.int64), 0, len(x) - 1)\n    b = np.clip((stops * LFP_RATE).astype(np.int64), a + 1, len(x))\n    out = np.empty(len(a))\n    for i, (p, q) in enumerate(zip(a, b)):\n        out[i] = x[p:q].max()\n    return out\n\n\ndef prepare_session(path: str, url: str) -> dict:\n    \"\"\"Load one file and reduce it: units, behaviour, the ripple channel, candidate events\n    and the data checks that need the LFP.\"\"\"\n    with open_nwb(url) as f:\n        s = load_session(f)\n    s[\"path\"] = path\n    ch, power = choose_ripple_channel(url, s)\n    s[\"ripple_channel\"], s[\"ripple_power\"] = ch, power\n    x = read_channel(url, ch)\n    s[\"lfp_seconds\"] = len(x) / LFP_RATE\n    env = ripple_envelope(x)\n    nrem = state_mask(np.arange(len(env)) / LFP_RATE, s, \"Non-REM\")\n    mu, sd = float(env[nrem].mean()), float(env[nrem].std())\n    envz = (env - mu) / sd\n    # state clock check: theta/delta in REM and non-REM, with true and shifted labels\n    s[\"theta_delta\"] = {sh: theta_delta(x, s, sh) for sh in (0.0, 600.0)}\n    del x, env\n    t_end = max(s[\"lfp_seconds\"], max(sp.max() for sp in s[\"spikes\"] if len(sp)))\n    a, b, peak = population_bursts(s[\"spikes\"], t_end)\n    rip = segment_max(envz, a, b)\n    # LFP and spike clock check: bursts in non-REM that hold a ripple, with the envelope true\n    # and shifted by 0.5 s\n    mid = (a + b) / 2\n    in_nrem = state_mask(mid, s, \"Non-REM\")\n    s[\"ripple_overlap\"] = {sh: float(np.mean(segment_max(envz, a[in_nrem] + sh, b[in_nrem] + sh) >= 3))\n                           for sh in (0.0, 0.5, 2.0)}\n    del envz\n    # immobility and epoch of each burst\n    rem = state_mask(mid, s, \"REM\")\n    ep = np.full(len(a), \"\", dtype=object)\n    for lab in (\"PREEpoch\", \"MazeEpoch\", \"POSTEpoch\"):\n        lo, hi = s[\"epochs\"][lab]\n        ep[(mid >= lo) & (mid < hi)] = lab.replace(\"Epoch\", \"\").upper()\n    tx, sp = xy_speed(s)\n    sp_ev = np.interp(mid, tx, np.nan_to_num(sp, nan=np.inf), left=np.inf, right=np.inf)\n    immobile = np.where(ep == \"MAZE\", sp_ev < RUN_SPEED, ~rem)\n    s[\"bursts\"] = {\"start\": a, \"stop\": b, \"peak\": peak, \"ripple_z\": rip, \"epoch\": ep,\n                   \"rem\": rem, \"immobile\": immobile}\n    keep = (rip >= 3) & immobile & (ep != \"\")\n    s[\"events\"] = {\"start\": a[keep], \"stop\": b[keep], \"epoch\": ep[keep].astype(str)}\n    s[\"ripple_threshold_sd\"] = (mu, sd)\n    return s\n\n\n# ----------------------------------------------------------------------------- templates\n\ndef build_templates(s: dict) -> dict:\n    \"\"\"Rate maps of every pyramidal cell in each direction, place cells and templates.\"\"\"\n    pyr = np.flatnonzero(s[\"cell_type\"] == \"excitatory\")\n    length = track_length(s)\n    dt = 1.0 / s[\"lin\"][\"rate\"]\n    out = {\"pyr\": pyr, \"length\": length, \"maps\": {}, \"occ\": {}}\n    for d in directions(s):\n        t_run, x_run = run_samples(s, d)\n        maps, occ = [], None\n        for u in pyr:\n            rm, occ = rate_map(s[\"spikes\"][u], t_run, x_run, length, dt)\n            maps.append(rm)\n        out[\"maps\"][d] = np.array(maps)\n        out[\"occ\"][d] = occ\n        out[(\"run\", d)] = (t_run, x_run)\n    peaks = np.max([out[\"maps\"][d].max(1) for d in out[\"maps\"]], axis=0)\n    out[\"peak\"] = peaks\n    return out\n\n\ndef template_cells(tpl: dict, threshold: float = PLACE_PEAK) -> dict:\n    \"\"\"Indices (into pyr) of the cells in each direction's template.\"\"\"\n    return {d: np.flatnonzero(tpl[\"maps\"][d].max(1) >= threshold) for d in tpl[\"maps\"]}\n\n\n# ----------------------------------------------------------------------------- decoding\n\ndef event_counts(spikes: list[np.ndarray], start: float, stop: float) -> np.ndarray:\n    \"\"\"Spike counts (cells x 20 ms bins) of the given spike trains in one event.\"\"\"\n    nb = max(1, int(np.ceil((stop - start) / DECODE_BIN)))\n    edges = start + np.arange(nb + 1) * DECODE_BIN\n    return np.array([np.histogram(sp[(sp >= start) & (sp < edges[-1])], edges)[0] for sp in spikes])\n\n\ndef log_posterior(counts: np.ndarray, maps: np.ndarray) -> np.ndarray:\n    \"\"\"Log posterior (time x position) of a Poisson decoder with a flat prior.\"\"\"\n    f = maps + 1e-3\n    return counts.T @ np.log(f) - DECODE_BIN * f.sum(0)[None, :]\n\n\ndef normalise(lp: np.ndarray) -> np.ndarray:\n    lp = lp - lp.max(-1, keepdims=True)\n    p = np.exp(lp)\n    return p / p.sum(-1, keepdims=True)\n\n\ndef weighted_r(p: np.ndarray) -> np.ndarray:\n    \"\"\"Weighted correlation of position and time for posteriors (..., time, position).\"\"\"\n    T, X = p.shape[-2:]\n    t = np.arange(T, dtype=float)[:, None]\n    x = np.arange(X, dtype=float)[None, :]\n    w = p / p.sum((-2, -1), keepdims=True)\n    mt = (w * t).sum((-2, -1))\n    mx = (w * x).sum((-2, -1))\n    ct = t - mt[..., None, None]\n    cx = x - mx[..., None, None]\n    cov = (w * ct * cx).sum((-2, -1))\n    vt = (w * ct ** 2).sum((-2, -1))\n    vx = (w * cx ** 2).sum((-2, -1))\n    with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n        return cov / np.sqrt(vt * vx)\n\n\ndef column_cycle_null(p: np.ndarray, rng: np.random.Generator, n: int = N_SHUFFLE) -> np.ndarray:\n    \"\"\"|r| of n column-cycle shuffles (each time bin's posterior rotated by a random amount).\"\"\"\n    T, X = p.shape\n    x = np.arange(X, dtype=float)\n    # first and second moments of every rotation of every row\n    rot = np.array([np.roll(x, -k) for k in range(X)])              # rot[k, i] = x[(i - k) % X]\n    m1 = p @ rot.T                                                   # (T, X): sum_i p[t,i] x[(i-k)%X]\n    m2 = p @ (rot ** 2).T\n    k = rng.integers(0, X, size=(n, T))\n    rows = np.arange(T)[None, :]\n    a1, a2 = m1[rows, k], m2[rows, k]                                 # (n, T)\n    t = np.arange(T, dtype=float)\n    mt, mx = t.mean(), a1.mean(1)\n    cov = (t[None, :] * a1).mean(1) - mt * mx\n    vx = a2.mean(1) - mx ** 2\n    vt = (t ** 2).mean() - mt ** 2\n    with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n        return np.abs(cov / np.sqrt(vt * vx))\n\n\ndef score_event(counts: np.ndarray, maps: np.ndarray, rng: np.random.Generator,\n                n_shuffle: int = N_SHUFFLE) -> tuple[float, float, np.ndarray]:\n    \"\"\"(r, rZ, kept time bins) of one event: bins without spikes are left out.\"\"\"\n    keep = counts.sum(0) > 0\n    if keep.sum() < 3:\n        return np.nan, np.nan, keep\n    p = normalise(log_posterior(counts[:, keep], maps))\n    r = float(weighted_r(p))\n    null = column_cycle_null(p, rng, n_shuffle)\n    sd = null.std()\n    return r, float((abs(r) - null.mean()) / sd) if sd > 0 else np.nan, keep\n\n\ndef decode_events(s: dict, tpl: dict, cells: dict, rng: np.random.Generator,\n                  epochs=(\"PRE\", \"MAZE\", \"POST\"), maps: dict | None = None,\n                  n_shuffle: int = N_SHUFFLE) -> dict:\n    \"\"\"Score every candidate event of the given epochs with each direction's template.\n\n    `cells` gives the template cells per direction (indices into tpl['pyr']); `maps` replaces\n    the rate maps (for shuffled templates). An event is scored with a template when at least\n    MIN_ACTIVE of its cells fire; the event takes the template with the larger rZ.\"\"\"\n    maps = maps if maps is not None else tpl[\"maps\"]\n    ev = s[\"events\"]\n    sel = np.flatnonzero(np.isin(ev[\"epoch\"], epochs))\n    out = {\"index\": [], \"epoch\": [], \"r\": [], \"rZ\": [], \"direction\": [], \"n_active\": []}\n    for i in sel:\n        best = None\n        for d, c in cells.items():\n            if len(c) < MIN_ACTIVE:\n                continue\n            cnt = event_counts([s[\"spikes\"][tpl[\"pyr\"][j]] for j in c], ev[\"start\"][i], ev[\"stop\"][i])\n            n_active = int((cnt.sum(1) > 0).sum())\n            if n_active < MIN_ACTIVE:\n                continue\n            r, rz, _ = score_event(cnt, maps[d][c], rng, n_shuffle)\n            if np.isfinite(rz) and (best is None or rz > best[1]):\n                best = (r, rz, d, n_active)\n        if best is None:\n            continue\n        out[\"index\"].append(i)\n        out[\"epoch\"].append(ev[\"epoch\"][i])\n        out[\"r\"].append(best[0])\n        out[\"rZ\"].append(best[1])\n        out[\"direction\"].append(best[2])\n        out[\"n_active\"].append(best[3])\n    return {k: np.array(v) for k, v in out.items()}\n\n\ndef cell_contributions(s: dict, tpl: dict, cells: dict, decoded: dict,\n                       rng: np.random.Generator, maps: dict | None = None) -> list[tuple]:\n    \"\"\"Per event and active cell: (event index, epoch, cell index into pyr, contribution).\n\n    The contribution is |r| minus the mean |r| over N_PCC_SHIFT decodings with that cell's\n    rate map circularly shifted by random amounts, on the template the event was scored with.\"\"\"\n    maps = maps if maps is not None else tpl[\"maps\"]\n    ev = s[\"events\"]\n    rows = []\n    for i, ep, d in zip(decoded[\"index\"], decoded[\"epoch\"], decoded[\"direction\"]):\n        if ep not in (\"PRE\", \"POST\"):\n            continue\n        c = cells[d]\n        m = maps[d][c]\n        cnt = event_counts([s[\"spikes\"][tpl[\"pyr\"][j]] for j in c], ev[\"start\"][i], ev[\"stop\"][i])\n        keep = cnt.sum(0) > 0\n        cnt = cnt[:, keep]\n        f = m + 1e-3\n        lp = cnt.T @ np.log(f) - DECODE_BIN * f.sum(0)[None, :]\n        r0 = abs(float(weighted_r(normalise(lp))))\n        X = m.shape[1]\n        for a in np.flatnonzero(cnt.sum(1) > 0):\n            shifts = rng.integers(1, X, size=N_PCC_SHIFT)\n            fs = np.array([np.roll(f[a], k) for k in shifts])           # (K, X)\n            delta = (cnt[a][None, :, None] * (np.log(fs)[:, None, :] - np.log(f[a])[None, None, :])\n                     - DECODE_BIN * (fs - f[a][None, :])[:, None, :])    # (K, T, X)\n            rs = np.abs(weighted_r(normalise(lp[None] + delta)))\n            rows.append((i, ep, c[a], r0 - float(np.nanmean(rs))))\n    return rows\n\n\ndef shifted_maps(tpl: dict, which: np.ndarray, rng: np.random.Generator) -> dict:\n    \"\"\"Copy of the rate maps with the cells `which` (indices into pyr) circularly shifted.\"\"\"\n    out = {}\n    for d, m in tpl[\"maps\"].items():\n        m = m.copy()\n        for j in which:\n            m[j] = np.roll(m[j], rng.integers(1, m.shape[1]))\n        out[d] = m\n    return out\n\n\n# ----------------------------------------------------------------------------- rates\n\ndef epoch_duration(s: dict, label: str) -> float:\n    a, b = s[\"epochs\"][label]\n    return b - a\n\n\ndef count_in(sp: np.ndarray, starts: np.ndarray, stops: np.ndarray) -> int:\n    i = np.searchsorted(sp, starts)\n    j = np.searchsorted(sp, stops)\n    return int((j - i).sum())\n\n\ndef burst_fraction(sp: np.ndarray) -> float:\n    if len(sp) < 3:\n        return np.nan\n    isi = np.diff(sp)\n    short = isi <= BURST_ISI\n    inb = np.zeros(len(sp), bool)\n    inb[:-1] |= short\n    inb[1:] |= short\n    return float(inb.mean())\n\n\ndef binned(spikes: list[np.ndarray], a: float, b: float, width: float = 0.1,\n           mask_times: np.ndarray | None = None) -> np.ndarray:\n    \"\"\"Counts (cells x bins) of 100 ms bins between a and b; with mask_times, only the bins\n    whose centres are True in it are kept.\"\"\"\n    edges = np.arange(a, b + width / 2, width)\n    m = np.array([np.histogram(sp, edges)[0] for sp in spikes], dtype=float)\n    if mask_times is not None:\n        m = m[:, mask_times]\n    return m\n\n\ndef corr_matrix(m: np.ndarray) -> np.ndarray:\n    with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n        c = np.corrcoef(m)\n    return c\n\n\ndef partial_corr(x: np.ndarray, y: np.ndarray, z: np.ndarray) -> float:\n    \"\"\"Correlation of x and y controlling for z.\"\"\"\n    ok = np.isfinite(x) & np.isfinite(y) & np.isfinite(z)\n    x, y, z = x[ok], y[ok], z[ok]\n    if len(x) < 4:\n        return np.nan\n    rxy = np.corrcoef(x, y)[0, 1]\n    rxz = np.corrcoef(x, z)[0, 1]\n    ryz = np.corrcoef(y, z)[0, 1]\n    return float((rxy - rxz * ryz) / np.sqrt((1 - rxz ** 2) * (1 - ryz ** 2)))\n"
}
```

```
File created successfully at: entries/000044-grosmark-2016/grosmark.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/000044-grosmark-2016 && sed -i 's|# rot\[k, i\] = x\[(i - k) % X\]|# rot[k, i] = x[(i + k) % X]|; s|# (T, X): sum_i p\[t,i\] x\[(i-k)%X\]|# (T, X): sum_i p[t,i] x[(i+k)%X]|' grosmark.py && cat > $TMPDIR/t3.py <<'E'
import time, sys, pickle, numpy as np
sys.path.insert(0,'.')
import grosmark as g
urls=g.asset_urls()
p,u=[x for x in urls if 'Buddy' in x[0]][0]
t=time.time(); s=g.prepare_session(p,u); print("prep", time.time()-t)
print(s['ripple_channel'], s['theta_delta'], s['ripple_overlap'])
ev=s['events']; print({e:(ev['epoch']==e).sum() for e in ('PRE','MAZE','POST')}, len(s['bursts']['start']))
pickle.dump(s, open(sys.argv[1],'wb'))
E
$TMPDIR/venv/bin/python $TMPDIR/t3.py $TMPDIR/buddy.pkl
```

```
prep 60.1027410030365
14 {0.0: {'REM': 3.0618461506488246, 'Non-REM': 0.2591492803677542}, 600.0: {'REM': 0.252200118511709, 'Non-REM': 0.36833492054572775}} {0.0: 0.6498699609882965, 0.5: 0.16775032509752927, 2.0: 0.15312093628088427}
{'PRE': np.int64(1533), 'MAZE': np.int64(121), 'POST': np.int64(1458)} 5008
```

**Agent calls Bash**

```bash
cat > $TMPDIR/t4.py <<'E'
import time, sys, pickle, numpy as np
sys.path.insert(0,'.')
import grosmark as g
s=pickle.load(open(sys.argv[1],'rb'))
tpl=g.build_templates(s); cells=g.template_cells(tpl)
print("pyr", len(tpl['pyr']), "place", (tpl['peak']>=1).sum(), {d:len(c) for d,c in cells.items()}, tpl['length'])
t,x,v=g.lin_speed(s); tx,sp=g.xy_speed(s)
run=np.abs(v)>5; print("run frac", np.nanmean(run), "lin speed med", np.nanmedian(np.abs(v[run])), "xy speed same", np.nanmedian(sp[run]))
rng=np.random.default_rng(0)
t0=time.time(); dec=g.decode_events(s,tpl,cells,rng); print("decode", time.time()-t0, len(dec['rZ']))
for e in ('PRE','MAZE','POST'): m=dec['epoch']==e; print(e, m.sum(), np.nanmean(dec['rZ'][m]).round(3))
t0=time.time(); rows=g.cell_contributions(s,tpl,cells,dec,rng); print("pcc", time.time()-t0, len(rows))
pickle.dump((tpl,dec,rows), open(sys.argv[1]+'.dec','wb'))
E
$TMPDIR/venv/bin/python $TMPDIR/t4.py $TMPDIR/buddy.pkl
```

```
pyr 48 place 30 {1: 23, -1: 26} 160.0
run frac 0.06936289063359063 lin speed med 53.68160663988988 xy speed same 56.94398178422779
decode 7.776845932006836 2458
PRE 1246 1.025
MAZE 76 1.593
POST 1136 1.202
pcc 11.302997827529907 19394
```

**Agent calls Bash**

```bash
python - <<'E'
import re
p='grosmark.py'; t=open(p).read()
t=t.replace('''def event_counts(spikes: list[np.ndarray], start: float, stop: float) -> np.ndarray:
    """Spike counts (cells x 20 ms bins) of the given spike trains in one event."""
    nb = max(1, int(np.ceil((stop - start) / DECODE_BIN)))
    edges = start + np.arange(nb + 1) * DECODE_BIN
    return np.array([np.histogram(sp[(sp >= start) & (sp < edges[-1])], edges)[0] for sp in spikes])
''','''def event_counts(spikes: list[np.ndarray], start: float, stop: float) -> np.ndarray:
    """Spike counts (cells x 20 ms bins) of the given spike trains in one event."""
    nb = max(1, int(np.ceil((stop - start) / DECODE_BIN)))
    edges = start + np.arange(nb + 1) * DECODE_BIN
    return np.array([np.diff(np.searchsorted(sp, edges)) for sp in spikes])


def count_cache(s: dict, tpl: dict) -> list[np.ndarray]:
    """Counts (pyramidal cells x 20 ms bins) of every candidate event, computed once."""
    sp = [s["spikes"][u] for u in tpl["pyr"]]
    ev = s["events"]
    return [event_counts(sp, a, b) for a, b in zip(ev["start"], ev["stop"])]
''')
t=t.replace('''def decode_events(s: dict, tpl: dict, cells: dict, rng: np.random.Generator,''','''def decode_events(s: dict, tpl: dict, cache: list, cells: dict, rng: np.random.Generator,''')
t=t.replace('''            cnt = event_counts([s["spikes"][tpl["pyr"][j]] for j in c], ev["start"][i], ev["stop"][i])
            n_active''','''            cnt = cache[i][c]
            n_active''')
t=t.replace('''def cell_contributions(s: dict, tpl: dict, cells: dict, decoded: dict,''','''def cell_contributions(s: dict, tpl: dict, cache: list, cells: dict, decoded: dict,''')
t=t.replace('''        cnt = event_counts([s["spikes"][tpl["pyr"][j]] for j in c], ev["start"][i], ev["stop"][i])
        keep''','''        cnt = cache[i][c]
        keep''')
open(p,'w').write(t)
E
grep -n "ev = s\[\"events\"\]" grosmark.py
```

```
402:    ev = s["events"]
477:    ev = s["events"]
510:    ev = s["events"]
```

**Agent calls Bash**

```bash
sed -i 's/dec=g.decode_events(s,tpl,cells,rng)/cache=g.count_cache(s,tpl); print("cache",time.time()-t0); dec=g.decode_events(s,tpl,cache,cells,rng)/; s/rows=g.cell_contributions(s,tpl,cells,dec,rng)/rows=g.cell_contributions(s,tpl,cache,cells,dec,rng)/' $TMPDIR/t4.py; $TMPDIR/venv/bin/python $TMPDIR/t4.py $TMPDIR/buddy.pkl
```

```
pyr 48 place 30 {1: 23, -1: 26} 160.0
run frac 0.06936289063359063 lin speed med 53.68160663988988 xy speed same 56.94398178422779
cache 0.76780104637146
decode 5.173765420913696 2458
PRE 1246 1.025
MAZE 76 1.593
POST 1136 1.202
pcc 9.857395648956299 19394
```

**Agent**

Per-session preparation takes about 60 s and the decoding a few seconds, so the full notebook should fit in roughly 10 to 15 minutes. Adding the per-session analysis passes to the helper.

**Agent calls Bash**

```bash
cat >> grosmark.py <<'E'


# ----------------------------------------------------------------------------- data checks

def position_error(s: dict, lags=(-30.0, -5.0, -1.0, 0.0, 1.0, 5.0, 30.0)) -> dict:
    """Median error (cm) of decoding position during running from pyramidal spikes, with rate
    maps from even minutes and 0.5 s windows of odd minutes, for spikes shifted by each lag."""
    t, x, v = lin_speed(s)
    m = np.isfinite(x) & (np.abs(np.nan_to_num(v)) > RUN_SPEED)
    t_run, x_run = t[m], x[m]
    dt = 1.0 / s["lin"]["rate"]
    length = track_length(s)
    even = (np.floor((t_run - t_run[0]) / 60) % 2) == 0
    pyr = np.flatnonzero(s["cell_type"] == "excitatory")
    out = {}
    for lag in lags:
        sp = [s["spikes"][u] + lag for u in pyr]
        maps = np.array([rate_map(q, t_run[even], x_run[even], length, dt)[0] for q in sp])
        # windows: consecutive odd-minute running samples grouped into 0.5 s
        to, xo = t_run[~even], x_run[~even]
        w = np.floor((to - to[0]) / 0.5).astype(int)
        uw, first = np.unique(w, return_index=True)
        errs = []
        for k, i0 in zip(uw, first):
            sel = w == k
            a, b = to[sel][0], to[sel][-1] + dt
            if b - a < 0.4:
                continue
            cnt = np.array([np.searchsorted(q, b) - np.searchsorted(q, a) for q in sp])
            if cnt.sum() == 0:
                continue
            f = maps + 1e-3
            lp = cnt @ np.log(f) - (b - a) * f.sum(0)
            errs.append(abs((np.argmax(lp) + 0.5) * BIN_CM - np.mean(xo[sel])))
        out[lag] = float(np.median(errs))
    return out


# ----------------------------------------------------------------------------- per-session passes

def first_pass(s: dict, seed_decode: int, seed_pcc: int, seed_null: int) -> dict:
    """Templates, the event score of every candidate event, the per-cell contributions, and the
    contributions under a fully shifted template (the PCC test's false-positive rate)."""
    tpl = build_templates(s)
    cells = template_cells(tpl)
    cache = count_cache(s, tpl)
    dec = decode_events(s, tpl, cache, cells, np.random.default_rng(seed_decode))
    rows = cell_contributions(s, tpl, cache, cells, dec, np.random.default_rng(seed_pcc))
    rng = np.random.default_rng(seed_null)
    null_maps = shifted_maps(tpl, np.arange(len(tpl["pyr"])), rng)
    dec_null = decode_events(s, tpl, cache, cells, rng, epochs=("PRE", "POST"), maps=null_maps,
                             n_shuffle=20)
    rows_null = cell_contributions(s, tpl, cache, cells, dec_null, rng, maps=null_maps)
    return {"tpl": tpl, "cells": cells, "decoded": dec, "contrib": rows, "contrib_null": rows_null}


def variant_pass(s: dict, tpl: dict, variants: dict, n_shuffle: int = 100) -> dict:
    """Decode PRE and POST events again for each variant.

    `variants` maps a name to (cells per direction, list of pyr indices to shift or None, seed)."""
    cache = count_cache(s, tpl)
    out = {}
    for name, (cells, shift, seed) in variants.items():
        rng = np.random.default_rng(seed)
        maps = shifted_maps(tpl, np.asarray(shift, int), rng) if shift is not None else None
        out[name] = decode_events(s, tpl, cache, cells, rng, epochs=("PRE", "POST"), maps=maps,
                                  n_shuffle=n_shuffle)
    return out


def cell_measures(s: dict, tpl: dict, place: np.ndarray) -> dict:
    """Per place cell (indices into pyr): rates, gains, bursting, spatial measures, and the
    100 ms coactivation matrices of PRE, POST, MAZE running and the whole session."""
    pyr = tpl["pyr"]
    sp = [s["spikes"][pyr[j]] for j in place]
    T = s["lfp_seconds"]
    pre, post = s["epochs"]["PREEpoch"], s["epochs"]["POSTEpoch"]
    st = s["states"]
    nrem = (st["label"] == "Non-REM")
    def nrem_in(ep):
        a = np.clip(st["start"][nrem], *ep)
        b = np.clip(st["stop"][nrem], *ep)
        return a, b
    na_pre, nb_pre = nrem_in(pre)
    na_post, nb_post = nrem_in(post)
    nrem_dur = (nb_pre - na_pre).sum() + (nb_post - na_post).sum()
    ev = s["events"]
    e_pre = ev["epoch"] == "PRE"
    e_post = ev["epoch"] == "POST"
    d_epre = (ev["stop"][e_pre] - ev["start"][e_pre]).sum()
    d_epost = (ev["stop"][e_post] - ev["start"][e_post]).sum()
    m = {k: [] for k in ("rate_session", "rate_sleep", "rate_prepost", "gain", "gain_pre",
                         "gain_post", "burst", "info", "n_fields", "peak_pos", "best_dir",
                         "infield_change")}
    for j, q in zip(place, sp):
        n_pre = count_in(q, np.array([pre[0]]), np.array([pre[1]]))
        n_post = count_in(q, np.array([post[0]]), np.array([post[1]]))
        r_pre, r_post = n_pre / (pre[1] - pre[0]), n_post / (post[1] - post[0])
        r_pp = (n_pre + n_post) / ((pre[1] - pre[0]) + (post[1] - post[0]))
        c_epre = count_in(q, ev["start"][e_pre], ev["stop"][e_pre])
        c_epost = count_in(q, ev["start"][e_post], ev["stop"][e_post])
        m["rate_session"].append(len(q) / T)
        m["rate_sleep"].append((count_in(q, na_pre, nb_pre) + count_in(q, na_post, nb_post)) / nrem_dur)
        m["rate_prepost"].append(r_pp)
        m["gain"].append(((c_epre + c_epost) / (d_epre + d_epost)) / r_pp if r_pp > 0 else np.nan)
        m["gain_pre"].append((c_epre / d_epre) / r_pre if r_pre > 0 else np.nan)
        m["gain_post"].append((c_epost / d_epost) / r_post if r_post > 0 else np.nan)
        m["burst"].append(burst_fraction(q))
        d = max(tpl["maps"], key=lambda dd: tpl["maps"][dd][j].max())
        rm, occ = tpl["maps"][d][j], tpl["occ"][d]
        m["best_dir"].append(d)
        m["info"].append(spatial_info(rm, occ))
        fields = place_fields(rm)
        m["n_fields"].append(len(fields))
        m["peak_pos"].append((np.argmax(rm) + 0.5) / len(rm))
        # in-field over out-of-field rate, first and last third of running in that direction
        t_run, x_run = tpl[("run", d)]
        if not fields:
            m["infield_change"].append(np.nan)
            continue
        fb = max(fields, key=lambda b: rm[b].sum())
        dt = 1.0 / s["lin"]["rate"]
        bins = np.minimum((x_run / BIN_CM).astype(int), len(rm) - 1)
        inf = np.isin(bins, fb)
        j_near = np.clip(np.searchsorted(t_run, q), 1, len(t_run) - 1)
        near = np.where(np.abs(t_run[j_near - 1] - q) < np.abs(t_run[j_near] - q), j_near - 1, j_near)
        near = near[np.abs(t_run[near] - q) <= dt]
        cnt = np.bincount(near, minlength=len(t_run))
        thirds = np.array_split(np.arange(len(t_run)), 3)
        lr = []
        for th in (thirds[0], thirds[-1]):
            i_in, i_out = th[inf[th]], th[~inf[th]]
            r_in = cnt[i_in].sum() / (len(i_in) * dt) if len(i_in) else np.nan
            r_out = cnt[i_out].sum() / (len(i_out) * dt) if len(i_out) else np.nan
            lr.append(np.log10((r_in + 0.01) / (r_out + 0.01)))
        m["infield_change"].append(lr[1] - lr[0])
    m = {k: np.array(v, float) for k, v in m.items()}
    # coactivation
    t, x, v = lin_speed(s)
    run_t = t[np.isfinite(x) & (np.abs(np.nan_to_num(v)) > RUN_SPEED)]
    maze = s["epochs"]["MazeEpoch"]
    edges = np.arange(maze[0], maze[1], 0.1)
    centres = edges[:-1] + 0.05
    near = np.clip(np.searchsorted(run_t, centres), 1, len(run_t) - 1)
    run_bins = np.minimum(np.abs(run_t[near] - centres), np.abs(run_t[near - 1] - centres)) < 0.05
    m["C_pre"] = corr_matrix(binned(sp, *pre))
    m["C_post"] = corr_matrix(binned(sp, *post))
    m["C_run"] = corr_matrix(binned(sp, maze[0], maze[1], mask_times=run_bins))
    m["C_session"] = corr_matrix(binned(sp, 0.0, T))
    return m
E
$TMPDIR/venv/bin/python -c "import ast;ast.parse(open('grosmark.py').read())"
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
sed -i 's/    edges = np.arange(maze\[0\], maze\[1\], 0.1)/    edges = np.arange(maze[0], maze[1] + 0.05, 0.1)/' grosmark.py && cat > $TMPDIR/t5.py <<'E'
import time, sys, pickle, numpy as np
sys.path.insert(0,'.')
import grosmark as g
s=pickle.load(open(sys.argv[1],'rb'))
t0=time.time(); print(g.position_error(s)); print("poserr", time.time()-t0)
tpl=g.build_templates(s); place=np.flatnonzero(tpl['peak']>=1)
t0=time.time(); m=g.cell_measures(s,tpl,place); print("measures", time.time()-t0)
for k,v in m.items(): print(k, v.shape, np.nanmedian(v) if v.ndim==1 else np.nanmean(v[np.triu_indices(len(v),1)]))
t0=time.time(); fp=g.first_pass(s,1,2,3); print("first", time.time()-t0)
E
$TMPDIR/venv/bin/python $TMPDIR/t5.py $TMPDIR/buddy.pkl
```

```
{-30.0: 41.38372617674085, -5.0: 46.08808354493485, -1.0: 17.523792080058143, 0.0: 11.746669386794327, 1.0: 24.810620552390716, 5.0: 45.76793721328685, 30.0: 41.47908979771954}
poserr 0.39783525466918945
measures 0.42055702209472656
rate_session (30,) 0.4791566728568918
rate_sleep (30,) 0.7037664783427495
rate_prepost (30,) 0.4022620230047099
gain (30,) 4.299100458956967
gain_pre (30,) 4.5559404518285405
gain_post (30,) 4.513569261108792
burst (30,) 0.1334725194481463
info (30,) 0.886524207830812
n_fields (30,) 1.0
peak_pos (30,) 0.25
best_dir (30,) -1.0
infield_change (30,) -0.07347804548798775
C_pre (30, 30) 0.028568462874276442
C_post (30, 30) 0.03442303133203905
C_run (30, 30) 0.01026882167418362
C_session (30, 30) 0.02798271438010313
first 28.303284168243408
```

**Agent**

The position decoding error is lowest with spikes and positions at their stored alignment (11.7 cm, against 17 to 46 cm at shifted lags), so the clocks agree. Writing the notebook now.

**Agent calls Write**

```json
{
 "file_path": "entries/000044-grosmark-2016/make_nb.py",
 "content": "\"\"\"Builds reproduce_grosmark_2016.ipynb (scratch; not part of the entry).\"\"\"\nimport nbformat as nbf\n\ncells = []\n\n\ndef md(text, tags=None):\n    c = nbf.v4.new_markdown_cell(text.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\ndef code(text, tags=None):\n    c = nbf.v4.new_code_cell(text.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\nexec(open(\"nb_cells.py\").read())\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbf.write(nb, \"reproduce_grosmark_2016.ipynb\")\n"
}
```

```
File created successfully at: entries/000044-grosmark-2016/make_nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "entries/000044-grosmark-2016/nb_cells.py",
 "content": "md(r\"\"\"\n# Reproducing Grosmark & Buzsáki (2016) from dandiset 000044\n\nPaper: A. D. Grosmark and G. Buzsáki, \"Diversity in neural firing dynamics supports both rigid and\nlearned hippocampal sequences\", *Science* 351:1440 (2016),\n[doi:10.1126/science.aad1935](https://doi.org/10.1126/science.aad1935).\n\nDandiset: [DANDI:000044](https://dandiarchive.org/dandiset/000044/0.261005.2101), version\n**0.261005.2101**. The paper cites no version (it predates the dandiset and points to CRCNS). This\nis the most recent published version. It is also the one that matches the files best: in the two\nearlier versions (0.210812.1516 and 0.250624.0426) the `rate` of every position series holds the\nsampling period (0.0256 s) in place of the rate (39.06 Hz), so the positions would span about\n60 hours in place of the MAZE epoch. The cell below shows this. Otherwise the versions differ only\nin subject metadata.\n\nText used: the full main text and the legends of Figures 1 to 4, from the NIH author manuscript in\nPubMed Central (PMC4919122). The supplementary Materials and Methods and figs. S1 to S22 could not\nbe retrieved (PMC and Science serve them only behind a browser check), so every definition the\nmain text does not give is a common choice, fixed in the claims file before the analysis. Neither\nthe paper nor the dandiset links analysis code.\n\n| Claim | Status |\n|---|---|\n| sessions-and-tracks: 4 rats, 8 sessions, two linear and one circular track | tested |\n| place-cell-count: 491 place cells | tested |\n| fig1c-post-gt-pre: sequence scores higher in POST than PRE | tested |\n| fig1c-maze-gt-pre: sequence scores higher in MAZE than PRE | tested |\n| fig2b-strong-contributors: 216 strongly contributing neurons | tested |\n| fig2-pre-post-overlap: 73% of PRE contributors also contribute in POST | tested |\n| fig2d-shuffle-high-dpcc: shuffling the top 10 to 20% dPCC cells removes replay | tested |\n| fig2e-remove-plastic: removing plastic cells removes replay | tested |\n| figs2-track-distribution: rigid and plastic cells similarly placed on the track | tested |\n| fig3a-plastic-specificity: plastic cells more specific, fewer fields | tested |\n| fig3b-plastic-improve: plastic cells sharpen during the session | tested |\n| fig4a-rigid-faster: rigid cells fire faster | tested |\n| fig4a-plastic-ripple-burst-coactivation: plastic cells more ripple-related, bursty and coactive | tested |\n| fig4c-pre-fast-coactivation: PRE coactivation dominated by fast cells | tested |\n| fig4c-slow-coactivation-increase: slow cells gain coactivation PRE to POST | tested |\n| fig4c-slow-replay: slow cells show most replay of coactivation | tested |\n| rate-split-medians: low and high-rate medians 0.39 and 1.12 Hz | tested |\n| figs16-low-rate-info-gain: low-rate cells more informative, larger ripple-gain increase | tested |\n| fig4d-slow-sequences: slow but not fast cells increase sequence content | tested |\n| fig4e-gain-sequences: increase limited to high ripple-gain cells | tested |\n\"\"\")\n\ncode(r\"\"\"\nimport os\nfor k in (\"OMP_NUM_THREADS\", \"OPENBLAS_NUM_THREADS\", \"MKL_NUM_THREADS\"):\n    os.environ[k] = \"1\"\nimport warnings\nwarnings.filterwarnings(\"ignore\", category=UserWarning)\nfrom concurrent.futures import ProcessPoolExecutor\n\nimport numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nfrom scipy import stats\n\nimport grosmark as g\n\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 30)\nprint(\"dandiset\", g.DANDISET, \"version\", g.VERSION)\n\"\"\")\n\nmd(r\"\"\"\n### Versions\n\nThe rate of the position series in the first published version and in the pinned one, against\nthe length of the MAZE epoch.\n\"\"\")\n\ncode(r\"\"\"\nOLD = dict(g.asset_urls(\"0.210812.1516\"))\nURLS = g.asset_urls()\nrows = []\nfor path, url in URLS:\n    with g.open_nwb(url) as f:\n        beh = f[\"processing/behavior\"]\n        name = [k for k in beh if \"Linearized\" in k][0]\n        ser = beh[name][list(beh[name])[0]]\n        n = ser[\"data\"].shape[0]\n        rate_new = float(ser[\"starting_time\"].attrs[\"rate\"])\n        ep = f[\"intervals/epochs\"]\n        maze = float(ep[\"stop_time\"][1] - ep[\"start_time\"][1])\n    with g.open_nwb(OLD[path]) as f:\n        beh = f[\"processing/behavior\"]\n        ser = beh[name][list(beh[name])[0]]\n        rate_old = float(ser[\"starting_time\"].attrs[\"rate\"])\n    rows.append(dict(file=path.split(\"/\")[1][:30], samples=n, maze_s=round(maze, 1),\n                     rate_0_210812=rate_old, span_old_h=round(n / rate_old / 3600, 1),\n                     rate_pinned=round(rate_new, 3), span_pinned_s=round(n / rate_new, 1)))\nprint(pd.DataFrame(rows).to_string(index=False))\n\"\"\")\n\nmd(r\"\"\"\n## Data check\n\nEach file is streamed and reduced in parallel: units, epochs, states, positions, one LFP channel\n(the good channel with the most 150 to 250 Hz power in a POST non-REM chunk), the ripple envelope\nat the candidate events, and the checks below. This takes a few minutes.\n\"\"\")\n\ncode(r\"\"\"\nwith ProcessPoolExecutor(4) as ex:\n    S = list(ex.map(g.prepare_session, *zip(*URLS)))\nNAMES = [s[\"session\"] for s in S]\nprint(len(S), \"sessions loaded:\", NAMES)\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor s in S:\n    ep = s[\"epochs\"]\n    ct = pd.Series(s[\"cell_type\"]).value_counts()\n    loc = pd.Series(s[\"location\"][s[\"cell_type\"] == \"excitatory\"]).value_counts()\n    t, x, v = g.lin_speed(s)\n    tx, sp = g.xy_speed(s)\n    run = np.isfinite(x) & (np.abs(np.nan_to_num(v)) > g.RUN_SPEED)\n    last_spike = max(q.max() for q in s[\"spikes\"] if len(q))\n    rows.append(dict(\n        subject=s[\"subject\"], session=s[\"session\"], track=s[\"track\"],\n        PRE_h=round((ep[\"PREEpoch\"][1] - ep[\"PREEpoch\"][0]) / 3600, 2),\n        MAZE_min=round((ep[\"MazeEpoch\"][1] - ep[\"MazeEpoch\"][0]) / 60, 1),\n        POST_h=round((ep[\"POSTEpoch\"][1] - ep[\"POSTEpoch\"][0]) / 3600, 2),\n        epochs_end_s=round(ep[\"POSTEpoch\"][1], 1), lfp_end_s=round(s[\"lfp_seconds\"], 1),\n        last_spike_s=round(last_spike, 1),\n        pyr=int(ct.get(\"excitatory\", 0)), int_=int(ct.get(\"inhibitory\", 0)),\n        pyr_lCA1=int(loc.get(\"lCA1\", 0)), pyr_rCA1=int(loc.get(\"rCA1\", 0)),\n        pos_rate=round(s[\"lin\"][\"rate\"], 2), pos_unit=s[\"lin\"][\"unit\"],\n        lin_max_m=round(float(np.nanmax(s[\"lin\"][\"data\"])), 3),\n        on_track_frac=round(float(np.isfinite(x).mean()), 3), run_s=round(run.sum() / s[\"lin\"][\"rate\"], 0),\n        lin_speed_run=round(float(np.nanmedian(np.abs(v[run]))), 1),\n        xy_speed_run=round(float(np.nanmedian(sp[run])), 1),\n    ))\nDATA = pd.DataFrame(rows)\nprint(DATA.to_string(index=False))\nprint()\nprint(\"subjects\", DATA.subject.nunique(), \"sessions\", len(DATA), \"pyramidal\", DATA.pyr.sum(),\n      \"interneurons\", DATA.int_.sum())\nprint(\"sessions per subject:\", DATA.groupby(\"subject\").size().to_dict())\n\"\"\", tags=[\"sanity\"])\n\ncode(r\"\"\"\n# sleep states, LFP channel and clock checks\nrows = []\nfor s in S:\n    st = s[\"states\"]\n    dur = pd.Series(st[\"stop\"] - st[\"start\"]).groupby(st[\"label\"]).sum()\n    td0, td1 = s[\"theta_delta\"][0.0], s[\"theta_delta\"][600.0]\n    ov = s[\"ripple_overlap\"]\n    ev = pd.Series(s[\"events\"][\"epoch\"]).value_counts()\n    rows.append(dict(session=s[\"session\"], states=\",\".join(sorted(set(st[\"label\"]))),\n                     awake_h=round(dur.get(\"Awake\", 0) / 3600, 2), nrem_h=round(dur.get(\"Non-REM\", 0) / 3600, 2),\n                     rem_h=round(dur.get(\"REM\", 0) / 3600, 2),\n                     states_end_s=round(float(st[\"stop\"].max()), 0),\n                     channel=s[\"ripple_channel\"], bad_ch=int(s[\"bad_electrode\"].sum()),\n                     TD_REM=round(td0[\"REM\"], 2), TD_NREM=round(td0[\"Non-REM\"], 2),\n                     TD_REM_shift600=round(td1[\"REM\"], 2), TD_NREM_shift600=round(td1[\"Non-REM\"], 2),\n                     burst_rip=round(ov[0.0], 3), burst_rip_shift05=round(ov[0.5], 3),\n                     burst_rip_shift2=round(ov[2.0], 3),\n                     ev_PRE=int(ev.get(\"PRE\", 0)), ev_MAZE=int(ev.get(\"MAZE\", 0)), ev_POST=int(ev.get(\"POST\", 0))))\nprint(pd.DataFrame(rows).to_string(index=False))\n\"\"\", tags=[\"sanity\"])\n\ncode(r\"\"\"\n# spikes against positions: median error (cm) of decoding position during running, rate maps from\n# even minutes and 0.5 s windows from odd minutes, with the spikes shifted by each lag (s)\nrows = []\nfor s in S:\n    e = g.position_error(s)\n    rows.append(dict(session=s[\"session\"], **{f\"lag {k:+g}\": round(v, 1) for k, v in e.items()}))\nPOSERR = pd.DataFrame(rows)\nprint(POSERR.to_string(index=False))\nprint(\"lag with the smallest error per session:\",\n      POSERR.set_index(\"session\").astype(float).idxmin(axis=1).to_dict())\n\n# recordings deposited twice: identical spike trains or positions across files\nsig_units = {}\nfor s in S:\n    for u, q in zip(s[\"unit_id\"], s[\"spikes\"]):\n        sig_units.setdefault((len(q), round(float(q[:50].sum()), 5)), []).append((s[\"session\"], int(u)))\ndup_units = [v for v in sig_units.values() if len({x[0] for x in v}) > 1]\nsig_pos = {}\nfor s in S:\n    sig_pos.setdefault(round(float(np.nansum(s[\"xy\"][\"data\"])), 4), []).append(s[\"session\"])\nprint(\"unit spike trains found in more than one file:\", len(dup_units))\nprint(\"position series found in more than one file:\", [v for v in sig_pos.values() if len(v) > 1])\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nChecks of the description against the data, from the outputs above:\n\n- Four subjects and eight sessions, each with PRE, MAZE and POST epochs, as the metadata state.\n  Durations are printed; the description's \"~4 hour\" PRE and POST and \"~45 minute\" MAZE are\n  compared there.\n- Units are labelled `excitatory` or `inhibitory`; pyramidal cells here are the excitatory units.\n  Their hemisphere is in `location` (lCA1 or rCA1); the electrodes' `location` is \"unknown\".\n- Positions are stated in metres. The linearized position spans 0 to 1.6 m on the 1.6 m tracks and\n  0 to 2 m on the 2 m track, consistent with the description. On the circular track (described as\n  1 m in diameter, a circumference of 3.14 m) it reaches about 2.84 to 2.9 m. The running speed\n  from the 2D positions agrees with that from the linearized position, so the 2D positions are\n  consistent with metres.\n- The sleep states are consistent with the LFP: the theta/delta ratio is far higher in REM than in\n  non-REM in every session, and the contrast is lost when the labels are shifted by 600 s.\n- Spikes and LFP share a clock: the population bursts in non-REM hold a ripple far more often with\n  the envelope as stored than shifted by 0.5 or 2 s.\n- Spikes and positions share a clock: the decoding error of position is smallest at lag 0.\n- No unit spike train or position series appears in more than one file.\n- The description mentions neck EMG and accelerometer signals; the files hold neither, and no raw\n  wide-band data (`acquisition` is empty). These are not needed here.\n\"\"\")\n\nmd(r\"\"\"\n## Templates, event scores and per-cell contributions\n\nFor each session: rate maps on running in each direction, place cells, the event scores (rZ) of\nevery candidate event, each active cell's contribution to its events (for PCC), and the same\ncontributions with every rate map shifted (the false-positive rate of the PCC test). Seeds are\nfixed per session and per step.\n\"\"\")\n\ncode(r\"\"\"\ndef _first(i):\n    return g.first_pass(S[i], 1000 + i, 2000 + i, 3000 + i)\n\nwith ProcessPoolExecutor(4) as ex:\n    FP = list(ex.map(g.first_pass, S, [1000 + i for i in range(8)], [2000 + i for i in range(8)],\n                     [3000 + i for i in range(8)]))\nEVENTS = pd.concat([pd.DataFrame(dict(session=s[\"session\"], subject=s[\"subject\"], epoch=fp[\"decoded\"][\"epoch\"],\n                                      rZ=fp[\"decoded\"][\"rZ\"], r=fp[\"decoded\"][\"r\"],\n                                      n_active=fp[\"decoded\"][\"n_active\"]))\n                    for s, fp in zip(S, FP)], ignore_index=True)\nprint(\"candidate events scored, by session and epoch:\")\nprint(EVENTS.groupby([\"session\", \"epoch\"]).size().unstack().to_string())\ncand = pd.DataFrame([pd.Series(s[\"events\"][\"epoch\"]).value_counts() for s in S], index=NAMES)\nprint(\"candidate events before the active-cell condition:\")\nprint(cand.to_string())\n\"\"\")\n\nmd(r\"\"\"\n## sessions-and-tracks\n\n> Recordings were made in four rats, in eight novel exploration sessions, each a PRE sleep, a MAZE\n> epoch on one of two linear tracks or a circular track, and a POST sleep.\n\"\"\")\n\ncode(r\"\"\"\norder_ok = [s[\"epochs\"][\"PREEpoch\"][1] <= s[\"epochs\"][\"MazeEpoch\"][0] + 1e-6 and\n            s[\"epochs\"][\"MazeEpoch\"][1] <= s[\"epochs\"][\"POSTEpoch\"][0] + 1e-6 for s in S]\nprint(DATA[[\"subject\", \"session\", \"track\", \"PRE_h\", \"MAZE_min\", \"POST_h\"]].to_string(index=False))\nprint(\"subjects:\", DATA.subject.nunique(), \" sessions:\", len(DATA), \" epochs in PRE, MAZE, POST order:\",\n      sum(order_ok), \"of\", len(S))\nprint(\"tracks:\", DATA.track.value_counts().to_dict())\n\"\"\", tags=[\"claim:sessions-and-tracks\"])\n\nmd(\"**Result: TBD**\")\n\nmd(r\"\"\"\n## place-cell-count\n\n> The Bayesian decoder was built from 491 place cells over the eight sessions.\n\nA place cell is a pyramidal cell whose smoothed rate map on running (above 5 cm/s) peaks at 1 Hz\nor more in at least one direction. 0.5 and 2 Hz are shown as variants.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor s, fp in zip(S, FP):\n    pk = fp[\"tpl\"][\"peak\"]\n    rows.append(dict(subject=s[\"subject\"], session=s[\"session\"], pyramidal=len(pk),\n                     place_05Hz=int((pk >= 0.5).sum()), place_1Hz=int((pk >= 1).sum()),\n                     place_2Hz=int((pk >= 2).sum()),\n                     **{f\"template_{d:+d}\": len(c) for d, c in fp[\"cells\"].items()}))\nPC = pd.DataFrame(rows)\nprint(PC.to_string(index=False))\nprint(\"totals:\", PC[[\"pyramidal\", \"place_05Hz\", \"place_1Hz\", \"place_2Hz\"]].sum().to_dict())\nprint(\"by subject (1 Hz):\", PC.groupby(\"subject\").place_1Hz.sum().to_dict())\nprint(\"expected 491, tolerance 49; within:\", abs(PC.place_1Hz.sum() - 491) <= 49)\n\"\"\", tags=[\"claim:place-cell-count\"])\n\nmd(\"**Result: TBD**\")\n\nmd(r\"\"\"\n## fig1c-post-gt-pre and fig1c-maze-gt-pre\n\n> Sequence scores (rZ) of candidate events are higher in POST sleep than in PRE sleep (replay).\n> Sequence content is higher in MAZE immobility events than in PRE sleep events.\n\nKruskal-Wallis across the three epochs on all events pooled, then Tukey's HSD on the ranks.\n\"\"\")\n\ncode(r\"\"\"\ndef ranks_tukey(groups):\n    allv = np.concatenate(groups)\n    rk = stats.rankdata(allv)\n    out, i = [], 0\n    for gr in groups:\n        out.append(rk[i:i + len(gr)])\n        i += len(gr)\n    return stats.tukey_hsd(*out)\n\nep_names = [\"PRE\", \"MAZE\", \"POST\"]\ngrp = [EVENTS.loc[EVENTS.epoch == e, \"rZ\"].dropna().values for e in ep_names]\nfor e, v in zip(ep_names, grp):\n    print(f\"{e:5s} n={len(v):5d} mean rZ={v.mean():.3f} SE={v.std(ddof=1) / np.sqrt(len(v)):.3f} \"\n          f\"median={np.median(v):.3f} range {v.min():.2f} to {v.max():.2f}; sign-rank vs 0 p={stats.wilcoxon(v).pvalue:.2g}\")\nkw = stats.kruskal(*grp)\nprint(f\"Kruskal-Wallis H={kw.statistic:.1f} p={kw.pvalue:.2g}\")\ntk = ranks_tukey(grp)\nfor i, j in [(2, 0), (1, 0), (2, 1)]:\n    print(f\"Tukey on ranks {ep_names[i]} vs {ep_names[j]}: p={tk.pvalue[i, j]:.3g}, \"\n          f\"mean difference {grp[i].mean() - grp[j].mean():+.3f}\")\nper = EVENTS.groupby([\"subject\", \"session\", \"epoch\"]).rZ.mean().unstack()[ep_names]\nper[\"POST>PRE\"] = per.POST > per.PRE\nper[\"MAZE>PRE\"] = per.MAZE > per.PRE\nprint(per.round(3).to_string())\nprint(\"sessions POST>PRE:\", int(per[\"POST>PRE\"].sum()), \"of 8; MAZE>PRE:\", int(per[\"MAZE>PRE\"].sum()), \"of 8\")\nprint(\"by subject:\")\nprint(EVENTS.groupby([\"subject\", \"epoch\"]).rZ.mean().unstack()[ep_names].round(3).to_string())\nfig, ax = plt.subplots(figsize=(5, 3.5))\nfor e, v in zip(ep_names, grp):\n    ax.plot(np.sort(v), np.linspace(0, 1, len(v)), label=e)\nax.set_xlabel(\"rZ\"); ax.set_ylabel(\"cumulative fraction\"); ax.legend()\nax.set_xlim(-3, 8)\nprint(\"points outside the x axis:\", int(sum(((v < -3) | (v > 8)).sum() for v in grp)))\n\"\"\", tags=[\"claim:fig1c-post-gt-pre\", \"claim:fig1c-maze-gt-pre\"])\n\nmd(r\"\"\"\nThe weighted correlation threshold is not used here; as a variant, the fraction of events with\nrZ above 1.96 per epoch.\n\"\"\")\n\ncode(r\"\"\"\nprint(EVENTS.assign(sig=EVENTS.rZ > 1.96).groupby(\"epoch\").sig.mean().round(3).to_dict())\n\"\"\", tags=[\"claim:fig1c-post-gt-pre\"])\n\nmd(\"**Result: TBD**\")\n\nmd(r\"\"\"\n## fig2b-strong-contributors\n\n> 216 neurons showed significant PCC scores in PRE or POST and were considered to contribute\n> strongly to sequences.\n\nA cell's contribution to an event is |r| minus the mean |r| over 20 decodings with that cell's rate\nmap circularly shifted. Strongly contributing in an epoch: one-sided Wilcoxon signed-rank test of\nits contributions against 0, p < 0.05, with at least 5 events. The false-positive rate comes from\nthe same test with every rate map shifted.\n\"\"\")\n\ncode(r\"\"\"\ndef pcc_table(rows, s, place):\n    df = pd.DataFrame(rows, columns=[\"event\", \"epoch\", \"cell\", \"contrib\"])\n    out = []\n    for j in place:\n        rec = dict(session=s[\"session\"], subject=s[\"subject\"], cell=j)\n        for e in (\"PRE\", \"POST\"):\n            v = df.loc[(df.cell == j) & (df.epoch == e), \"contrib\"].values\n            rec[f\"n_{e}\"] = len(v)\n            rec[f\"PCC_{e}\"] = v.mean() if len(v) else np.nan\n            rec[f\"p_{e}\"] = stats.wilcoxon(v, alternative=\"greater\").pvalue if len(v) >= 5 and np.any(v != 0) else np.nan\n        out.append(rec)\n    return pd.DataFrame(out)\n\nframes, nulls = [], []\nfor s, fp in zip(S, FP):\n    place = np.flatnonzero(fp[\"tpl\"][\"peak\"] >= g.PLACE_PEAK)\n    frames.append(pcc_table(fp[\"contrib\"], s, place))\n    nulls.append(pcc_table(fp[\"contrib_null\"], s, place))\nCELLS = pd.concat(frames, ignore_index=True)\nNULL = pd.concat(nulls, ignore_index=True)\nfor df in (CELLS, NULL):\n    df[\"strong_PRE\"] = df.p_PRE < 0.05\n    df[\"strong_POST\"] = df.p_POST < 0.05\n    df[\"strong\"] = df.strong_PRE | df.strong_POST\n    df[\"dPCC\"] = df.PCC_POST - df.PCC_PRE\nprint(\"place cells\", len(CELLS), \"; with >= 5 events in PRE:\", int((CELLS.n_PRE >= 5).sum()),\n      \"in POST:\", int((CELLS.n_POST >= 5).sum()))\nprint(\"strongly contributing: PRE\", int(CELLS.strong_PRE.sum()), \" POST\", int(CELLS.strong_POST.sum()),\n      \" either\", int(CELLS.strong.sum()), f\"({CELLS.strong.mean():.1%} of place cells)\")\nprint(\"false-positive rate (all maps shifted): PRE\", f\"{NULL.strong_PRE.mean():.3f}\", \" POST\",\n      f\"{NULL.strong_POST.mean():.3f}\", \" either\", f\"{NULL.strong.mean():.3f}\",\n      f\"-> expected {NULL.strong.mean() * len(CELLS):.0f} cells by chance\")\nprint(\"expected 216, tolerance 21.6; within:\", abs(CELLS.strong.sum() - 216) <= 21.6)\nfor a in (0.01, 0.001):\n    n = int(((CELLS.p_PRE < a) | (CELLS.p_POST < a)).sum())\n    nn = ((NULL.p_PRE < a) | (NULL.p_POST < a)).mean()\n    print(f\"variant alpha={a}: {n} strongly contributing, false-positive rate {nn:.3f}\")\nprint(CELLS.groupby([\"subject\", \"session\"]).agg(place=(\"cell\", \"size\"), strong=(\"strong\", \"sum\"),\n                                                strong_PRE=(\"strong_PRE\", \"sum\"), strong_POST=(\"strong_POST\", \"sum\")).to_string())\n\"\"\", tags=[\"claim:fig2b-strong-contributors\"])\n\nmd(\"**Result: TBD**\")\n\nmd(r\"\"\"\n## fig2-pre-post-overlap\n\n> Most neurons strongly contributing to PRE sequences (73%) also contributed to POST sequences.\n\"\"\")\n\ncode(r\"\"\"\npre = CELLS[CELLS.strong_PRE]\nfrac = pre.strong_POST.mean()\nchance = CELLS.strong_POST.mean()\nprint(f\"PRE strongly contributing: {len(pre)}; also in POST: {int(pre.strong_POST.sum())} ({frac:.1%})\")\nprint(f\"chance (fraction of all place cells strongly contributing in POST): {chance:.1%}\")\ntab = pd.crosstab(CELLS.strong_PRE, CELLS.strong_POST)\nprint(tab.to_string())\nprint(\"Fisher exact test of association p =\", f\"{stats.fisher_exact(tab.values, alternative='greater').pvalue:.2g}\")\nprint(\"by subject:\", pre.groupby(\"subject\").strong_POST.agg([\"size\", \"mean\"]).round(3).to_dict(\"index\"))\nprint(\"expected 73%, tolerance 7.3; within:\", abs(frac * 100 - 73) <= 7.3)\n\"\"\", tags=[\"claim:fig2-pre-post-overlap\"])\n\nmd(\"**Result: TBD**\")\n\nmd(r\"\"\"\n## Rigid and plastic cells\n\nStrongly contributing cells with a PCC in both PRE and POST, split at the median dPCC of the\nsession's strongly contributing cells (reading (a)); reading (b), the median over all of the\nsession's place cells, is a variant.\n\"\"\")\n\ncode(r\"\"\"\nCELLS[\"cls\"] = \"\"\nCELLS[\"cls_b\"] = \"\"\nfor sess, df in CELLS.groupby(\"session\"):\n    ok = df.strong & df.dPCC.notna()\n    med = df.loc[ok, \"dPCC\"].median()\n    CELLS.loc[ok[ok].index, \"cls\"] = np.where(df.loc[ok, \"dPCC\"] < med, \"rigid\", \"plastic\")\n    med_b = df.dPCC.median()\n    CELLS.loc[ok[ok].index, \"cls_b\"] = np.where(df.loc[ok, \"dPCC\"] < med_b, \"rigid\", \"plastic\")\nprint(\"strong cells without a PCC in one epoch (not classified):\", int((CELLS.strong & CELLS.dPCC.isna()).sum()))\nprint(CELLS[CELLS.cls != \"\"].groupby([\"subject\", \"session\", \"cls\"]).size().unstack().to_string())\nprint(\"totals (a):\", CELLS.cls.value_counts().to_dict(), \" (b):\", CELLS.cls_b.value_counts().to_dict())\n\"\"\")\n\nmd(r\"\"\"\nPer-cell measures: rates, ripple gain, bursting, spatial information, fields, the in-field ratio\nover the session, and the 100 ms coactivation matrices.\n\"\"\")\n\ncode(r\"\"\"\nMEAS = []\nfor s, fp in zip(S, FP):\n    place = np.flatnonzero(fp[\"tpl\"][\"peak\"] >= g.PLACE_PEAK)\n    MEAS.append(g.cell_measures(s, fp[\"tpl\"], place))\ncols = [\"rate_session\", \"rate_sleep\", \"rate_prepost\", \"gain\", \"gain_pre\", \"gain_post\", \"burst\", \"info\",\n        \"n_fields\", \"peak_pos\", \"best_dir\", \"infield_change\"]\nCELLS = CELLS.join(pd.concat([pd.DataFrame({c: m[c] for c in cols}) for m in MEAS], ignore_index=True))\nCELLS[\"gain_change\"] = CELLS.gain_post - CELLS.gain_pre\nCELLS[\"coact\"] = np.concatenate([np.nanmean(np.where(np.eye(len(m[\"C_session\"]), dtype=bool), np.nan, m[\"C_session\"]), 1)\n                                 for m in MEAS])\nprint(CELLS[cols + [\"gain_change\", \"coact\"]].describe().T[[\"count\", \"min\", \"50%\", \"max\"]].round(3).to_string())\n\"\"\")\n\nmd(r\"\"\"\n### Re-decoding for the variant templates\n\nWithin each session: the top or bottom 10, 20, 50 and 75% of place cells by dPCC shuffled\n(fig2d), plastic or rigid cells removed (fig2e), templates of the low or high-rate half (fig4d,\nsplit as rate-split-medians selects) and of the low or high-gain half (fig4e). 100 column-cycle\nshuffles per event. The rate split is made here with reading (a), a median split within each\nsession; the section rate-split-medians shows both readings.\n\"\"\")\n\ncode(r\"\"\"\nLEVELS = [10, 20, 50, 75]\ndef variants_for(i, s, fp):\n    df = CELLS[CELLS.session == s[\"session\"]]\n    cells = fp[\"cells\"]\n    def restrict(keep):\n        keep = set(int(k) for k in keep)\n        return {d: np.array([c for c in cl if c in keep], int) for d, cl in cells.items()}\n    def drop(rem):\n        rem = set(int(k) for k in rem)\n        return {d: np.array([c for c in cl if c not in rem], int) for d, cl in cells.items()}\n    v = {\"base\": (cells, None, 5000 + i)}\n    ranked = df[df.dPCC.notna()].sort_values(\"dPCC\")\n    n = len(ranked)\n    for k, X in enumerate(LEVELS):\n        m = int(round(n * X / 100))\n        v[f\"top{X}\"] = (cells, ranked.cell.values[n - m:], 5100 + 10 * k + i)\n        v[f\"bottom{X}\"] = (cells, ranked.cell.values[:m], 5200 + 10 * k + i)\n    v[\"no_plastic\"] = (drop(df.cell[df.cls == \"plastic\"]), None, 6000 + i)\n    v[\"no_rigid\"] = (drop(df.cell[df.cls == \"rigid\"]), None, 6100 + i)\n    rs = df.rate_sleep.rank(method=\"first\").values\n    low = rs <= len(df) // 2\n    v[\"low_rate\"] = (restrict(df.cell[low]), None, 7000 + i)\n    v[\"high_rate\"] = (restrict(df.cell[~low]), None, 7100 + i)\n    gr = df.gain.rank(method=\"first\").values\n    hi = gr > len(df) // 2\n    v[\"high_gain\"] = (restrict(df.cell[hi]), None, 8000 + i)\n    v[\"low_gain\"] = (restrict(df.cell[~hi]), None, 8100 + i)\n    return v\n\nVARS = [variants_for(i, s, fp) for i, (s, fp) in enumerate(zip(S, FP))]\nwith ProcessPoolExecutor(4) as ex:\n    VRES = list(ex.map(g.variant_pass, S, [fp[\"tpl\"] for fp in FP], VARS))\n\ndef replay(name):\n    pre = np.concatenate([r[name][\"rZ\"][r[name][\"epoch\"] == \"PRE\"] for r in VRES])\n    post = np.concatenate([r[name][\"rZ\"][r[name][\"epoch\"] == \"POST\"] for r in VRES])\n    p = stats.mannwhitneyu(post, pre, alternative=\"greater\").pvalue\n    sess = sum(np.nanmean(r[name][\"rZ\"][r[name][\"epoch\"] == \"POST\"]) > np.nanmean(r[name][\"rZ\"][r[name][\"epoch\"] == \"PRE\"])\n               for r in VRES)\n    return dict(variant=name, n_PRE=len(pre), n_POST=len(post), mean_PRE=pre.mean(), mean_POST=post.mean(),\n                diff=post.mean() - pre.mean(), p_one_sided=p, present=p < 0.05, sessions_POST_gt_PRE=sess)\n\nREPLAY = pd.DataFrame([replay(k) for k in VARS[0]]).set_index(\"variant\")\nprint(REPLAY.round(4).to_string())\n\"\"\")\n\nmd(r\"\"\"\n## fig2d-shuffle-high-dpcc\n\n> The PRE to POST increase in sequence score is eliminated when the place fields of the 10 to 20%\n> of cells with the highest dPCC are shuffled, and remains after shuffling the bottom 75%.\n\"\"\")\n\ncode(r\"\"\"\nprint(REPLAY.loc[[\"base\"] + [f\"top{X}\" for X in LEVELS] + [f\"bottom{X}\" for X in LEVELS],\n                 [\"n_PRE\", \"n_POST\", \"mean_PRE\", \"mean_POST\", \"diff\", \"p_one_sided\", \"present\", \"sessions_POST_gt_PRE\"]].round(4).to_string())\nelim = (not REPLAY.loc[\"top10\", \"present\"]) or (not REPLAY.loc[\"top20\", \"present\"])\nremain = REPLAY.loc[\"bottom75\", \"present\"]\nprint(\"replay absent after shuffling top 10% or 20%:\", elim, \"; present after shuffling bottom 75%:\", remain)\ndef by_subject(name):\n    out = {}\n    for s, r in zip(S, VRES):\n        d = out.setdefault(s[\"subject\"], {\"PRE\": [], \"POST\": []})\n        for e in (\"PRE\", \"POST\"):\n            d[e].append(r[name][\"rZ\"][r[name][\"epoch\"] == e])\n    return {k: round(np.concatenate(v[\"POST\"]).mean() - np.concatenate(v[\"PRE\"]).mean(), 3) for k, v in out.items()}\nfor name in (\"base\", \"top10\", \"top20\", \"bottom75\"):\n    print(name, \"POST minus PRE mean rZ by subject:\", by_subject(name))\n\"\"\", tags=[\"claim:fig2d-shuffle-high-dpcc\"])\n\nmd(\"**Result: TBD**\")\n\nmd(r\"\"\"\n## fig2e-remove-plastic\n\n> The PRE to POST increase in sequence content is attributable to a small number of plastic cells;\n> removing them, unlike removing rigid cells, removes the increase.\n\"\"\")\n\ncode(r\"\"\"\nprint(REPLAY.loc[[\"base\", \"no_plastic\", \"no_rigid\"], [\"n_PRE\", \"n_POST\", \"mean_PRE\", \"mean_POST\", \"diff\",\n                                                     \"p_one_sided\", \"present\", \"sessions_POST_gt_PRE\"]].round(4).to_string())\nfor name in (\"no_plastic\", \"no_rigid\"):\n    print(name, \"POST minus PRE mean rZ by subject:\", by_subject(name))\nprint(\"ratio of differences (no plastic / no rigid):\",\n      round(REPLAY.loc[\"no_plastic\", \"diff\"] / REPLAY.loc[\"no_rigid\", \"diff\"], 3))\n\"\"\", tags=[\"claim:fig2e-remove-plastic\"])\n\nmd(\"**Result: TBD**\")\n\nmd(r\"\"\"\n## figs2-track-distribution\n\n> Rigid and plastic neurons were similarly distributed along the track.\n\"\"\")\n\ncode(r\"\"\"\nR = CELLS[CELLS.cls == \"rigid\"]; P = CELLS[CELLS.cls == \"plastic\"]\nks = stats.ks_2samp(R.peak_pos, P.peak_pos)\nprint(f\"peak position (fraction of track): rigid n={len(R)} median {R.peak_pos.median():.3f}; \"\n      f\"plastic n={len(P)} median {P.peak_pos.median():.3f}; KS D={ks.statistic:.3f} p={ks.pvalue:.3g}\")\nRb = CELLS[CELLS.cls_b == \"rigid\"]; Pb = CELLS[CELLS.cls_b == \"plastic\"]\nprint(f\"reading (b): KS p={stats.ks_2samp(Rb.peak_pos, Pb.peak_pos).pvalue:.3g}\")\nprint(\"by subject (median peak position):\")\nprint(CELLS[CELLS.cls != \"\"].groupby([\"subject\", \"cls\"]).peak_pos.median().unstack().round(3).to_string())\n\"\"\", tags=[\"claim:figs2-track-distribution\"])\n\nmd(\"**Result: TBD**\")\n\nmd(r\"\"\"\n## fig3a-plastic-specificity\n\n> Plastic neurons had higher place-specific indices and fewer place fields than rigid cells.\n\"\"\")\n\ncode(r\"\"\"\ndef compare(col, a=\"plastic\", b=\"rigid\", cls=\"cls\", alt=\"greater\"):\n    A = CELLS.loc[CELLS[cls] == a, col].dropna(); B = CELLS.loc[CELLS[cls] == b, col].dropna()\n    p = stats.mannwhitneyu(A, B).pvalue\n    print(f\"{col}: {a} n={len(A)} median {A.median():.3f} mean {A.mean():.3f}; {b} n={len(B)} median \"\n          f\"{B.median():.3f} mean {B.mean():.3f}; rank-sum p={p:.3g}\")\n    return A, B, p\n_, _, p_info = compare(\"info\")\n_, _, p_nf = compare(\"n_fields\")\nprint(\"reading (b):\"); compare(\"info\", cls=\"cls_b\"); compare(\"n_fields\", cls=\"cls_b\")\nprint(CELLS[CELLS.cls != \"\"].groupby([\"subject\", \"cls\"])[[\"info\", \"n_fields\"]].mean().unstack().round(3).to_string())\n\"\"\", tags=[\"claim:fig3a-plastic-specificity\"])\n\nmd(\"**Result: TBD**\")\n\nmd(r\"\"\"\n## fig3b-plastic-improve\n\n> Plastic but not rigid neurons increased their spatial specificity (in-field versus out-of-field\n> firing ratio) steadily during the MAZE session.\n\"\"\")\n\ncode(r\"\"\"\nfor c in (\"plastic\", \"rigid\"):\n    v = CELLS.loc[CELLS.cls == c, \"infield_change\"]\n    print(f\"{c}: n={v.notna().sum()} (no field: {v.isna().sum()}), median change of log10 ratio \"\n          f\"{v.median():.3f}, mean {v.mean():.3f}, cells increasing {(v > 0).sum()}; one-sided sign-rank p=\"\n          f\"{stats.wilcoxon(v.dropna(), alternative='greater').pvalue:.3g}\")\nA = CELLS.loc[CELLS.cls == \"plastic\", \"infield_change\"].dropna(); B = CELLS.loc[CELLS.cls == \"rigid\", \"infield_change\"].dropna()\nprint(f\"plastic vs rigid rank-sum p={stats.mannwhitneyu(A, B).pvalue:.3g}\")\nfor c in (\"plastic\", \"rigid\"):\n    v = CELLS.loc[CELLS.cls_b == c, \"infield_change\"].dropna()\n    print(f\"reading (b) {c}: n={len(v)} median {v.median():.3f} p={stats.wilcoxon(v, alternative='greater').pvalue:.3g}\")\nprint(CELLS[CELLS.cls != \"\"].groupby([\"subject\", \"cls\"]).infield_change.median().unstack().round(3).to_string())\n\"\"\", tags=[\"claim:fig3b-plastic-improve\"])\n\nmd(\"**Result: TBD**\")\n\nmd(r\"\"\"\n## fig4a-rigid-faster\n\n> Session-wide firing rates of rigid neurons were higher than those of plastic neurons.\n\"\"\")\n\ncode(r\"\"\"\ncompare(\"rate_session\", a=\"rigid\", b=\"plastic\")\nprint(\"reading (b):\"); compare(\"rate_session\", a=\"rigid\", b=\"plastic\", cls=\"cls_b\")\nprint(CELLS[CELLS.cls != \"\"].groupby([\"subject\", \"cls\"]).rate_session.median().unstack().round(3).to_string())\n\"\"\", tags=[\"claim:fig4a-rigid-faster\"])\n\nmd(\"**Result: TBD**\")\n\nmd(r\"\"\"\n## fig4a-plastic-ripple-burst-coactivation\n\n> Ripple-related spiking, bursting and pairwise coactivation were higher in plastic than in rigid\n> neurons.\n\"\"\")\n\ncode(r\"\"\"\nres = {}\nfor col in (\"gain\", \"burst\", \"coact\"):\n    A, B, p = compare(col)\n    res[col] = (A.median() > B.median()) and p < 0.05\nprint(\"higher in plastic with p < 0.05:\", res, \"->\", sum(res.values()), \"of 3\")\nprint(\"reading (b):\")\nfor col in (\"gain\", \"burst\", \"coact\"):\n    compare(col, cls=\"cls_b\")\nprint(CELLS[CELLS.cls != \"\"].groupby([\"subject\", \"cls\"])[[\"gain\", \"burst\", \"coact\"]].median().unstack().round(3).to_string())\n\"\"\", tags=[\"claim:fig4a-plastic-ripple-burst-coactivation\"])\n\nmd(\"**Result: TBD**\")\n\nmd(r\"\"\"\n## fig4c: coactivation by firing rate\n\nPlace cells of each session sorted by session firing rate; windows of 20% of the cells stepped\nby 1%. For each window: mean pairwise correlation (100 ms bins) in PRE, the mean POST minus PRE\nchange, and the partial correlation across its pairs of MAZE running and POST coactivation given\nPRE. Curves are averaged over sessions by window position.\n\"\"\")\n\ncode(r\"\"\"\nPOS = np.arange(0, 81)\ncurves = {\"pre\": [], \"change\": [], \"replay\": []}\nfor s, fp, m in zip(S, FP, MEAS):\n    df = CELLS[CELLS.session == s[\"session\"]].reset_index(drop=True)\n    order = np.argsort(df.rate_session.values)\n    N = len(order); w = max(2, int(round(0.2 * N)))\n    cp, cc, cr = [], [], []\n    for p in POS:\n        a = int(round(p / 100 * N)); idx = order[a:a + w]\n        iu = np.triu_indices(len(idx), 1)\n        pre_ = m[\"C_pre\"][np.ix_(idx, idx)][iu]; post_ = m[\"C_post\"][np.ix_(idx, idx)][iu]; run_ = m[\"C_run\"][np.ix_(idx, idx)][iu]\n        cp.append(np.nanmean(pre_)); cc.append(np.nanmean(post_ - pre_)); cr.append(g.partial_corr(run_, post_, pre_))\n    curves[\"pre\"].append(cp); curves[\"change\"].append(cc); curves[\"replay\"].append(cr)\nCURVES = {k: np.array(v) for k, v in curves.items()}\nCOACT = {}\nfor k, v in CURVES.items():\n    mean = np.nanmean(v, 0)\n    rho = stats.spearmanr(POS, mean)\n    per = [stats.spearmanr(POS, row, nan_policy=\"omit\").statistic for row in v]\n    COACT[k] = (rho.statistic, per)\n    print(f\"{k}: averaged curve slowest window {mean[0]:.4f}, fastest window {mean[-1]:.4f}, range {np.nanmin(mean):.4f} \"\n          f\"to {np.nanmax(mean):.4f}; Spearman rho with window position {rho.statistic:.3f} (p={rho.pvalue:.2g}); \"\n          f\"per session rho {np.round(per, 2).tolist()}; positive in {sum(r > 0 for r in per)} of 8\")\nfig, axs = plt.subplots(1, 3, figsize=(11, 3))\nfor ax, k in zip(axs, CURVES):\n    ax.plot(POS, CURVES[k].T, color=\"0.8\", lw=0.8); ax.plot(POS, np.nanmean(CURVES[k], 0), color=\"k\")\n    ax.set_title(k); ax.set_xlabel(\"window start (rate percentile)\")\nprint(\"all values are within the axes (autoscaled)\")\n\"\"\", tags=[\"claim:fig4c-pre-fast-coactivation\", \"claim:fig4c-slow-coactivation-increase\", \"claim:fig4c-slow-replay\"])\n\nmd(r\"\"\"\nBy subject, the averaged curves' Spearman correlations.\n\"\"\")\n\ncode(r\"\"\"\nsubj = np.array([s[\"subject\"] for s in S])\nfor k, v in CURVES.items():\n    print(k, {sb: round(stats.spearmanr(POS, np.nanmean(v[subj == sb], 0)).statistic, 3) for sb in np.unique(subj)})\nfastest = CURVES[\"change\"][:, -1]\nprint(\"POST minus PRE change in the fastest window per session:\", np.round(fastest, 4).tolist(),\n      \"sign-rank p =\", round(stats.wilcoxon(fastest).pvalue, 3))\n\"\"\", tags=[\"claim:fig4c-pre-fast-coactivation\", \"claim:fig4c-slow-coactivation-increase\", \"claim:fig4c-slow-replay\"])\n\nmd(\"**Result: TBD** (fig4c-pre-fast-coactivation)\")\nmd(\"**Result: TBD** (fig4c-slow-coactivation-increase)\")\nmd(\"**Result: TBD** (fig4c-slow-replay)\")\n\nmd(r\"\"\"\n## rate-split-medians\n\n> Place cells divided into equal groups by sleep firing rate have medians of 0.39 Hz (low-rate) and\n> 1.12 Hz (high-rate).\n\nSleep firing rate is the rate in non-REM sleep of PRE and POST. Reading (a): median split within\neach session; reading (b): median split of all place cells pooled. The rate over all of PRE and\nPOST is a variant.\n\"\"\")\n\ncode(r\"\"\"\ndef split_medians(col):\n    out = {}\n    lo_a = CELLS.groupby(\"session\")[col].transform(lambda x: x.rank(method=\"first\") <= len(x) // 2)\n    out[\"a\"] = (CELLS.loc[lo_a, col].median(), CELLS.loc[~lo_a, col].median())\n    lo_b = CELLS[col].rank(method=\"first\") <= len(CELLS) // 2\n    out[\"b\"] = (CELLS.loc[lo_b, col].median(), CELLS.loc[~lo_b, col].median())\n    return out, lo_a, lo_b\nSPLIT, LOW_A, LOW_B = split_medians(\"rate_sleep\")\nfor r, (lo, hi) in SPLIT.items():\n    print(f\"reading ({r}): low median {lo:.3f} Hz, high median {hi:.3f} Hz; within tolerance: \"\n          f\"{abs(lo - 0.39) <= 0.039 and abs(hi - 1.12) <= 0.112}\")\nv, _, _ = split_medians(\"rate_prepost\")\nprint(\"variant, rate over all of PRE and POST:\", {k: tuple(round(x, 3) for x in t) for k, t in v.items()})\nv, _, _ = split_medians(\"rate_session\")\nprint(\"variant, session rate:\", {k: tuple(round(x, 3) for x in t) for k, t in v.items()})\nprint(\"sleep rate of all place cells: median\", round(CELLS.rate_sleep.median(), 3), \"range\",\n      round(CELLS.rate_sleep.min(), 3), \"to\", round(CELLS.rate_sleep.max(), 3))\nprint(CELLS.assign(low=LOW_A).groupby([\"subject\", \"low\"]).rate_sleep.median().unstack().round(3).to_string())\n\"\"\", tags=[\"claim:rate-split-medians\"])\n\nmd(\"**Result: TBD**\")\n\nmd(r\"\"\"\n## figs16-low-rate-info-gain\n\n> Low-rate neurons carried more spatial information per spike on the maze, and increased their\n> within-ripple firing-rate gain from PRE to POST more than high-rate cells.\n\"\"\")\n\ncode(r\"\"\"\ndef low_high(col, low):\n    A = CELLS.loc[low, col].dropna(); B = CELLS.loc[~low, col].dropna()\n    p = stats.mannwhitneyu(A, B).pvalue\n    print(f\"{col}: low-rate n={len(A)} median {A.median():.3f}; high-rate n={len(B)} median {B.median():.3f}; rank-sum p={p:.3g}\")\n    return A.median() > B.median() and p < 0.05\nprint(\"reading (a), split within each session:\")\nok_a = [low_high(\"info\", LOW_A), low_high(\"gain_change\", LOW_A)]\nprint(\"reading (b), pooled split:\")\nok_b = [low_high(\"info\", LOW_B), low_high(\"gain_change\", LOW_B)]\nprint(\"held under (a):\", ok_a, \" under (b):\", ok_b)\nprint(CELLS.assign(low=LOW_A).groupby([\"subject\", \"low\"])[[\"info\", \"gain_change\"]].median().unstack().round(3).to_string())\n\"\"\", tags=[\"claim:figs16-low-rate-info-gain\"])\n\nmd(\"**Result: TBD**\")\n\nmd(r\"\"\"\n## fig4d-slow-sequences\n\n> Slow-firing, but not fast-firing, neurons increased their contribution to sequences from PRE to\n> POST sleep, in a decoding restricted to each group.\n\"\"\")\n\ncode(r\"\"\"\nprint(REPLAY.loc[[\"base\", \"low_rate\", \"high_rate\"], [\"n_PRE\", \"n_POST\", \"mean_PRE\", \"mean_POST\", \"diff\",\n                                                    \"p_one_sided\", \"present\", \"sessions_POST_gt_PRE\"]].round(4).to_string())\nfor name in (\"low_rate\", \"high_rate\"):\n    print(name, \"POST minus PRE mean rZ by subject:\", by_subject(name))\n\"\"\", tags=[\"claim:fig4d-slow-sequences\"])\n\nmd(\"**Result: TBD**\")\n\nmd(r\"\"\"\n## fig4e-gain-sequences\n\n> PRE to POST increases in sequence content were limited to cells with high ripple-specific\n> recruitment (gain).\n\"\"\")\n\ncode(r\"\"\"\nprint(REPLAY.loc[[\"base\", \"high_gain\", \"low_gain\"], [\"n_PRE\", \"n_POST\", \"mean_PRE\", \"mean_POST\", \"diff\",\n                                                    \"p_one_sided\", \"present\", \"sessions_POST_gt_PRE\"]].round(4).to_string())\nfor name in (\"high_gain\", \"low_gain\"):\n    print(name, \"POST minus PRE mean rZ by subject:\", by_subject(name))\n\"\"\", tags=[\"claim:fig4e-gain-sequences\"])\n\nmd(\"**Result: TBD**\")\n\nmd(r\"\"\"\n## Summary\n\nTBD\n\"\"\")\n"
}
```

```
File created successfully at: entries/000044-grosmark-2016/nb_cells.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
sed -i '/^def _first(i):$/,/^$/d' nb_cells.py && grep -n "_first" nb_cells.py; VIRTUAL_ENV=$TMPDIR/venv uv pip install -q nbconvert ipykernel nbformat 2>&1|tail -1; $TMPDIR/venv/bin/python make_nb.py && ls
```

```
__pycache__
grosmark.py
make_nb.py
nb_cells.py
reproduce_grosmark_2016.ipynb
```

**Agent calls Bash**

```bash
time $TMPDIR/venv/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=-1 --output $TMPDIR/exec.ipynb reproduce_grosmark_2016.ipynb 2>&1 | tail -20
```

```
[NbConvertApp] Converting notebook reproduce_grosmark_2016.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 252726 bytes to /tmp/claude-1001/exec.ipynb

real	18m26.399s
user	54m37.654s
sys	0m15.913s
```

**Agent calls Bash**

```bash
cat > $TMPDIR/show.py <<'E'
import nbformat, sys
nb=nbformat.read(sys.argv[1],4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    print(f"---- cell {i} {c.metadata.get('tags','')}")
    for o in c.outputs:
        if o.output_type=='stream': print(o.text[:6000])
        elif o.output_type=='error': print("ERROR", o.ename, o.evalue)
        elif 'text/plain' in o.get('data',{}): print(o['data']['text/plain'][:500])
E
$TMPDIR/venv/bin/python $TMPDIR/show.py $TMPDIR/exec.ipynb
```

```
---- cell 1 
dandiset 000044 version 0.261005.2101

---- cell 3 
                          file  samples  maze_s  rate_0_210812  span_old_h  rate_pinned  span_pinned_s
sub-Achilles_ses-Achilles-1025    80762  2067.5         0.0256       876.3       39.063         2067.5
sub-Achilles_ses-Achilles-1101   104457  2674.1         0.0256      1133.4       39.062         2674.1
sub-Buddy_ses-Buddy-06272013_b    90942  2328.1         0.0256       986.8       39.063         2328.1
sub-Cicero_ses-Cicero-09012014   217235  5561.2         0.0256      2357.2       39.063         5561.2
sub-Cicero_ses-Cicero-09102014   118360  3030.0         0.0256      1284.3       39.063         3030.0
sub-Cicero_ses-Cicero-09172014   120227  3077.8         0.0256      1304.6       39.063         3077.8
sub-Gatsby_ses-Gatsby-08022013    91215  2335.1         0.0256       989.7       39.063         2335.1
sub-Gatsby_ses-Gatsby-08282013   105180  2692.6         0.0256      1141.3       39.063         2692.6

---- cell 5 
8 sessions loaded: ['Achilles_10252013', 'Achilles_11012013', 'Buddy_06272013', 'Cicero_09012014', 'Cicero_09102014', 'Cicero_09172014', 'Gatsby_08022013', 'Gatsby_08282013']

---- cell 6 ['sanity']
 subject           session          track  PRE_h  MAZE_min  POST_h  epochs_end_s  lfp_end_s  last_spike_s  pyr  int_  pyr_lCA1  pyr_rCA1  pos_rate pos_unit  lin_max_m  on_track_frac  run_s  lin_speed_run  xy_speed_run
Achilles Achilles_10252013 1.6mLinearMaze   5.02      34.5    4.09       34861.1    34861.1       34861.1  120    17        57        63     39.06   meters      1.600          0.128  244.0           49.8          52.0
[... 355 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/t6.py <<'E'
import sys, pickle, numpy as np
sys.path.insert(0,'.')
import grosmark as g
urls=dict(g.asset_urls())
p=[k for k in urls if 'Cicero-0910' in k][0]
with g.open_nwb(urls[p]) as f: s=g.load_session(f)
t,x,v=g.lin_speed(s)
ok=np.isfinite(v)
print("v>5", np.mean(v[ok]>5), "v<-5", np.mean(v[ok]<-5))
xx=s['lin']['data'][:,0]; fin=np.isfinite(xx)
d=np.diff(xx); print("jumps >1m", np.sum(np.abs(d)>1), "median step", np.nanmedian(np.abs(d)))
# runs of finite
a,b=g.runs_of(fin); print("segments", len(a), "median len s", np.median(b-a)/39, "start x med", np.median(xx[a]), "end x med", np.median(xx[b-1]))
print(np.histogram(xx[fin], bins=15)[0])
xy=s['xy']['data']; print("xy at lin 0:", np.nanmedian(xy[fin & (xx<0.1)],0), "at lin max:", np.nanmedian(xy[fin & (xx>2.7)],0), "at lin 1.4", np.nanmedian(xy[fin & (np.abs(xx-1.4)<0.1)],0))
pickle.dump(s, open(sys.argv[1],'wb'))
E
$TMPDIR/venv/bin/python $TMPDIR/t6.py $TMPDIR/cic.pkl
```

```
v>5 0.06588041528190347 v<-5 0.6272756683626952
jumps >1m 0 median step 0.004226065377844784
segments 593 median len s 0.41025641025641024 start x med 1.489839678623693 end x med 1.215018103986179
[4853 1106 1638 1410 1322 1494 4889 2327 1513 1602 1785 2577 1822 2108
 3555]
xy at lin 0: [0.47976013 0.20166027] at lin max: [ 0.47969217 -0.21870341] at lin 1.4 [-0.53541816  0.05678049]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/000044-grosmark-2016/grosmark.py",
 "old_string": "def directions(s: dict) -> list[int]:\n    \"\"\"+1 and -1 on the linear tracks; +1 only on the circular track.\"\"\"\n    return [1] if s[\"track\"].startswith(\"Circular\") else [1, -1]",
 "new_string": "def directions(s: dict) -> list[int]:\n    \"\"\"+1 and -1 on the linear tracks. On the circular track, where the animal ran one way, the\n    direction it ran in most (the sign of the velocity in most running samples).\"\"\"\n    if not s[\"track\"].startswith(\"Circular\"):\n        return [1, -1]\n    _, _, v = lin_speed(s)\n    v = v[np.isfinite(v)]\n    return [1] if np.sum(v > RUN_SPEED) >= np.sum(v < -RUN_SPEED) else [-1]"
}
```

```
The file entries/000044-grosmark-2016/grosmark.py has been updated successfully. (note: the file had been modified on disk since you last read it — the edit applied cleanly, but the file contains other changes not in your context. Read it before edits that depend on surrounding content.)
```

**Agent calls Bash**

```bash
cat > $TMPDIR/t7.py <<'E'
import sys, pickle, time, numpy as np
from scipy import stats
sys.path.insert(0,'.')
import grosmark as g
import pandas as pd
for fn in sys.argv[1:]:
    s=pickle.load(open(fn,'rb'))
    if 'events' not in s:
        urls=dict(g.asset_urls()); p=[k for k in urls if s['session'].replace('_','-') in k][0]
        s=g.prepare_session(p, urls[p]); pickle.dump(s, open(fn,'wb'))
    t0=time.time(); fp=g.first_pass(s,1,2,3); print(s['session'], "first", round(time.time()-t0,1), g.directions(s))
    dec=fp['decoded']
    for e in ('PRE','MAZE','POST'): print(e, np.nanmean(dec['rZ'][dec['epoch']==e]).round(3))
    for key in ('contrib','contrib_null'):
        df=pd.DataFrame(fp[key], columns=['ev','ep','cell','c'])
        ps=df.groupby(['cell','ep']).c.apply(lambda v: stats.wilcoxon(v,alternative='greater').pvalue if len(v)>=5 else np.nan).unstack()
        print(key, (ps<0.05).mean().round(3).to_dict(), "mean contrib", df.c.mean().round(4))
E
$TMPDIR/venv/bin/python $TMPDIR/t7.py $TMPDIR/cic.pkl $TMPDIR/buddy.pkl
```

```
Cicero_09102014 first 126.4 [-1]
PRE 0.266
MAZE 0.516
POST 0.335
contrib {np.str_('POST'): 0.204, np.str_('PRE'): 0.111} mean contrib 0.001
contrib_null {np.str_('POST'): 0.259, np.str_('PRE'): 0.185} mean contrib 0.0005
Buddy_06272013 first 29.1 [1, -1]
PRE 1.023
MAZE 1.549
POST 1.209
contrib {np.str_('POST'): 0.867, np.str_('PRE'): 0.867} mean contrib 0.0219
contrib_null {np.str_('POST'): 0.733, np.str_('PRE'): 0.767} mean contrib 0.0133
```

**Agent calls Read**

```json
{
 "file_path": "entries/000044-grosmark-2016/grosmark.py",
 "offset": 505,
 "limit": 50
}
```

```
505	    return {k: np.array(v) for k, v in out.items()}
506	
507	
508	def cell_contributions(s: dict, tpl: dict, cache: list, cells: dict, decoded: dict,
509	                       rng: np.random.Generator, maps: dict | None = None) -> list[tuple]:
510	    """Per event and active cell: (event index, epoch, cell index into pyr, contribution).
511	
512	    The contribution is |r| minus the mean |r| over N_PCC_SHIFT decodings with that cell's
513	    rate map circularly shifted by random amounts, on the template the event was scored with."""
514	    maps = maps if maps is not None else tpl["maps"]
515	    ev = s["events"]
516	    rows = []
517	    for i, ep, d in zip(decoded["index"], decoded["epoch"], decoded["direction"]):
518	        if ep not in ("PRE", "POST"):
519	            continue
520	        c = cells[d]
521	        m = maps[d][c]
522	        cnt = cache[i][c]
523	        keep = cnt.sum(0) > 0
524	        cnt = cnt[:, keep]
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'E'
p='grosmark.py'; t=open(p).read()
old=t[t.index('def cell_contributions('):t.index('def shifted_maps(')]
new='''def cell_contributions(s: dict, tpl: dict, cache: list, cells: dict, decoded: dict,
                       rng: np.random.Generator, maps: dict | None = None) -> list[tuple]:
    """Per event and active cell: (event index, epoch, cell index into pyr, |r|, |r| of each
    shift).

    Each cell's rate map is circularly shifted by N_PCC_SHIFT random amounts, drawn once per cell
    and template and used in all its events; the event is decoded again with each, on the
    template it was scored with. The contribution is |r| minus the mean of the shifted |r|."""
    maps = maps if maps is not None else tpl["maps"]
    shifts = {d: rng.integers(1, maps[d].shape[1], size=(maps[d].shape[0], N_PCC_SHIFT)) for d in maps}
    rows = []
    for i, ep, d in zip(decoded["index"], decoded["epoch"], decoded["direction"]):
        if ep not in ("PRE", "POST"):
            continue
        c = cells[d]
        m = maps[d][c]
        cnt = cache[i][c]
        keep = cnt.sum(0) > 0
        cnt = cnt[:, keep]
        f = m + 1e-3
        lp = cnt.T @ np.log(f) - DECODE_BIN * f.sum(0)[None, :]
        r0 = abs(float(weighted_r(normalise(lp))))
        for a in np.flatnonzero(cnt.sum(1) > 0):
            fs = np.array([np.roll(f[a], k) for k in shifts[d][c[a]]])  # (K, X)
            delta = (cnt[a][None, :, None] * (np.log(fs)[:, None, :] - np.log(f[a])[None, None, :])
                     - DECODE_BIN * (fs - f[a][None, :])[:, None, :])    # (K, T, X)
            rs = np.abs(weighted_r(normalise(lp[None] + delta)))
            rows.append((i, ep, c[a], r0, rs))
    return rows


'''
t=t.replace(old,new)
t=t.replace('''    rows_null = cell_contributions(s, tpl, cache, cells, dec_null, rng, maps=null_maps)''','''    sub = {k: v[::4] for k, v in dec_null.items()}          # every fourth event is enough here
    rows_null = cell_contributions(s, tpl, cache, cells, sub, rng, maps=null_maps)''')
t=t.replace('''    dec_null = decode_events(s, tpl, cache, cells, rng, epochs=("PRE", "POST"), maps=null_maps,
                             n_shuffle=20)''','''    dec_null = decode_events(s, tpl, cache, cells, rng, epochs=("PRE", "POST"), maps=null_maps,
                             n_shuffle=20)''')
t=t.replace('''def variant_pass(s: dict, tpl: dict, variants: dict, n_shuffle: int = 100) -> dict:''','''def variant_pass(s: dict, tpl: dict, variants: dict, n_shuffle: int = 50) -> dict:''')
t=t.replace('''- 200 column-cycle shuffles for rZ, 20 circular shifts per cell for PCC: choices made here.''','''- 200 column-cycle shuffles for rZ (50 when templates are re-decoded for variants), 20
  circular shifts per cell for PCC: choices made here.''')
open(p,'w').write(t)
E
grep -n "contrib_null\|sub = " grosmark.py
```

```
654:    sub = {k: v[::4] for k, v in dec_null.items()}          # every fourth event is enough here
656:    return {"tpl": tpl, "cells": cells, "decoded": dec, "contrib": rows, "contrib_null": rows_null}
```

**Agent calls Bash**

```bash
python - <<'E'
p='nb_cells.py'; t=open(p).read()
old=t[t.index('def pcc_table(rows, s, place):'):t.index('frames, nulls = [], []')]
new='''def pcc_table(rows, s, place):
    df = pd.DataFrame([(e, ep, c, r0 - np.nanmean(rs)) for e, ep, c, r0, rs in rows],
                      columns=["event", "epoch", "cell", "contrib"])
    # per shift k, the cell's mean over events of |r| minus |r| with the map shifted by k
    shift = pd.DataFrame([(ep, c, *(r0 - rs)) for e, ep, c, r0, rs in rows])
    out = []
    for j in place:
        rec = dict(session=s["session"], subject=s["subject"], cell=j)
        for e in ("PRE", "POST"):
            v = df.loc[(df.cell == j) & (df.epoch == e), "contrib"].values
            rec[f"n_{e}"] = len(v)
            rec[f"PCC_{e}"] = v.mean() if len(v) else np.nan
            rec[f"p_{e}"] = stats.wilcoxon(v, alternative="greater").pvalue if len(v) >= 5 and np.any(v != 0) else np.nan
            sh = shift[(shift[1] == j) & (shift[0] == e)].iloc[:, 2:].values
            if len(sh) >= 5:
                k = np.nanmean(sh, 0)
                rec[f"pshift_{e}"] = (1 + np.sum(k <= 0)) / (1 + len(k))
            else:
                rec[f"pshift_{e}"] = np.nan
        out.append(rec)
    return pd.DataFrame(out)

'''
t=t.replace(old,new)
t=t.replace('''    df["dPCC"] = df.PCC_POST - df.PCC_PRE
print(''','''    df["dPCC"] = df.PCC_POST - df.PCC_PRE
    df["strongv_PRE"] = df.pshift_PRE < 0.05
    df["strongv_POST"] = df.pshift_POST < 0.05
    df["strongv"] = df.strongv_PRE | df.strongv_POST
print(''')
t=t.replace('''print(CELLS.groupby(["subject", "session"]).agg(place=("cell", "size"), strong=("strong", "sum"),
                                                strong_PRE=("strong_PRE", "sum"), strong_POST=("strong_POST", "sum")).to_string())''','''print(CELLS.groupby(["subject", "session"]).agg(place=("cell", "size"), strong=("strong", "sum"),
                                                strong_PRE=("strong_PRE", "sum"), strong_POST=("strong_POST", "sum"),
                                                strong_shift_test=("strongv", "sum")).to_string())
print("false-positive rate by track (main test, either epoch):",
      NULL.merge(DATA[["session", "track"]]).groupby("track").strong.mean().round(3).to_dict())
print()
print("variant: cell-level shift test (the cell's mean contribution against each of its 20 shifted maps, "
      "p = (1 + shifts not exceeded) / 21)")
print("strongly contributing: PRE", int(CELLS.strongv_PRE.sum()), " POST", int(CELLS.strongv_POST.sum()),
      " either", int(CELLS.strongv.sum()), f"({CELLS.strongv.mean():.1%} of place cells)")
print("false-positive rate (all maps shifted): PRE", f"{NULL.strongv_PRE.mean():.3f}", " POST",
      f"{NULL.strongv_POST.mean():.3f}", " either", f"{NULL.strongv.mean():.3f}")
pre_v = CELLS[CELLS.strongv_PRE]
print(f"variant: PRE strongly contributing {len(pre_v)}, also in POST {int(pre_v.strongv_POST.sum())} "
      f"({pre_v.strongv_POST.mean():.1%}); chance {CELLS.strongv_POST.mean():.1%}")''')
# classification variant
t=t.replace('''    med_b = df.dPCC.median()
    CELLS.loc[ok[ok].index, "cls_b"] = np.where(df.loc[ok, "dPCC"] < med_b, "rigid", "plastic")''','''    med_b = df.dPCC.median()
    CELLS.loc[ok[ok].index, "cls_b"] = np.where(df.loc[ok, "dPCC"] < med_b, "rigid", "plastic")
    okv = df.strongv & df.dPCC.notna()
    medv = df.loc[okv, "dPCC"].median()
    CELLS.loc[okv[okv].index, "cls_v"] = np.where(df.loc[okv, "dPCC"] < medv, "rigid", "plastic")''')
t=t.replace('''CELLS["cls_b"] = ""
for sess''','''CELLS["cls_b"] = ""
CELLS["cls_v"] = ""
for sess''')
t=t.replace('''print("totals (a):", CELLS.cls.value_counts().to_dict(), " (b):", CELLS.cls_b.value_counts().to_dict())''','''print("totals (a):", CELLS.cls.value_counts().to_dict(), " (b):", CELLS.cls_b.value_counts().to_dict(),
      " shift-test variant:", CELLS.cls_v.value_counts().to_dict())''')
open(p,'w').write(t)
E
grep -n "cls_b" nb_cells.py | head -30
```

```
450:CELLS["cls_b"] = ""
457:    CELLS.loc[ok[ok].index, "cls_b"] = np.where(df.loc[ok, "dPCC"] < med_b, "rigid", "plastic")
463:print("totals (a):", CELLS.cls.value_counts().to_dict(), " (b):", CELLS.cls_b.value_counts().to_dict(),
598:Rb = CELLS[CELLS.cls_b == "rigid"]; Pb = CELLS[CELLS.cls_b == "plastic"]
621:print("reading (b):"); compare("info", cls="cls_b"); compare("n_fields", cls="cls_b")
643:    v = CELLS.loc[CELLS.cls_b == c, "infield_change"].dropna()
658:print("reading (b):"); compare("rate_session", a="rigid", b="plastic", cls="cls_b")
679:    compare(col, cls="cls_b")
```

**Agent calls Bash**

```bash
python - <<'E'
p='nb_cells.py'; t=open(p).read()
rep=[
('''print(f"reading (b): KS p={stats.ks_2samp(Rb.peak_pos, Pb.peak_pos).pvalue:.3g}")''',
'''print(f"reading (b): KS p={stats.ks_2samp(Rb.peak_pos, Pb.peak_pos).pvalue:.3g}")
Rv = CELLS[CELLS.cls_v == "rigid"]; Pv = CELLS[CELLS.cls_v == "plastic"]
print(f"shift-test variant: rigid n={len(Rv)} plastic n={len(Pv)}, KS D={stats.ks_2samp(Rv.peak_pos, Pv.peak_pos).statistic:.3f} "
      f"p={stats.ks_2samp(Rv.peak_pos, Pv.peak_pos).pvalue:.3g}")'''),
('''print("reading (b):"); compare("info", cls="cls_b"); compare("n_fields", cls="cls_b")''',
'''print("reading (b):"); compare("info", cls="cls_b"); compare("n_fields", cls="cls_b")
print("shift-test variant:"); compare("info", cls="cls_v"); compare("n_fields", cls="cls_v")'''),
('''    print(f"reading (b) {c}: n={len(v)} median {v.median():.3f} p={stats.wilcoxon(v, alternative='greater').pvalue:.3g}")''',
'''    print(f"reading (b) {c}: n={len(v)} median {v.median():.3f} p={stats.wilcoxon(v, alternative='greater').pvalue:.3g}")
for c in ("plastic", "rigid"):
    v = CELLS.loc[CELLS.cls_v == c, "infield_change"].dropna()
    print(f"shift-test variant {c}: n={len(v)} median {v.median():.3f} p={stats.wilcoxon(v, alternative='greater').pvalue:.3g}")'''),
('''print("reading (b):"); compare("rate_session", a="rigid", b="plastic", cls="cls_b")''',
'''print("reading (b):"); compare("rate_session", a="rigid", b="plastic", cls="cls_b")
print("shift-test variant:"); compare("rate_session", a="rigid", b="plastic", cls="cls_v")'''),
('''for col in ("gain", "burst", "coact"):
    compare(col, cls="cls_b")''',
'''for col in ("gain", "burst", "coact"):
    compare(col, cls="cls_b")
print("shift-test variant:")
for col in ("gain", "burst", "coact"):
    compare(col, cls="cls_v")'''),
('''    v["no_rigid"] = (drop(df.cell[df.cls == "rigid"]), None, 6000 + i)''','''XX'''),
]
for a,b in rep:
    if a not in t: print("MISSING", a[:60]); continue
    t=t.replace(a,b)
t=t.replace('''    v["no_rigid"] = (drop(df.cell[df.cls == "rigid"]), None, 6100 + i)''','''    v["no_rigid"] = (drop(df.cell[df.cls == "rigid"]), None, 6100 + i)
    v["no_plastic_v"] = (drop(df.cell[df.cls_v == "plastic"]), None, 6200 + i)
    v["no_rigid_v"] = (drop(df.cell[df.cls_v == "rigid"]), None, 6300 + i)''')
t=t.replace('''print(REPLAY.loc[["base", "no_plastic", "no_rigid"],''','''print(REPLAY.loc[["base", "no_plastic", "no_rigid", "no_plastic_v", "no_rigid_v"],''')
t=t.replace('''share 50 column-cycle''','''share 50 column-cycle''')
t=t.replace('''session; the section rate-split-medians shows both readings.''','''session; the section rate-split-medians shows both readings. 50 column-cycle shuffles per event
here, in place of 200. The variants `no_plastic_v` and `no_rigid_v` use the classes from the
cell-level shift test.''')
t=t.replace('''(fig2d), plastic or rigid cells removed (fig2e), templates of the low or high-rate half (fig4d,
split as rate-split-medians selects) and of the low or high-gain half (fig4e). 100 column-cycle
shuffles per event. The rate split''','''(fig2d), plastic or rigid cells removed (fig2e), templates of the low or high-rate half (fig4d)
and of the low or high-gain half (fig4e). The rate split''')
open(p,'w').write(t)
E
grep -n "no_plastic_v\|50 column" nb_cells.py
```

```
MISSING     v["no_rigid"] = (drop(df.cell[df.cls == "rigid"]), None,
492:session; the section rate-split-medians shows both readings. 50 column-cycle shuffles per event
493:here, in place of 200. The variants `no_plastic_v` and `no_rigid_v` use the classes from the
517:    v["no_plastic_v"] = (drop(df.cell[df.cls_v == "plastic"]), None, 6200 + i)
580:print(REPLAY.loc[["base", "no_plastic", "no_rigid", "no_plastic_v", "no_rigid_v"], ["n_PRE", "n_POST", "mean_PRE", "mean_POST", "diff",
```

**Agent**

Re-running the full notebook with the circular-track fix and the shift-test variant.

**Agent calls Bash**

```bash
python - <<'E'
p='nb_cells.py'; t=open(p).read()
t=t.replace('''with ProcessPoolExecutor(4) as ex:
    S = list(ex.map(g.prepare_session, *zip(*URLS)))''','''import time
T0 = time.time()
with ProcessPoolExecutor(4) as ex:
    S = list(ex.map(g.prepare_session, *zip(*URLS)))
print(f"loaded in {time.time() - T0:.0f} s")''')
t=t.replace('''with ProcessPoolExecutor(4) as ex:
    FP = list(''','''T0 = time.time()
with ProcessPoolExecutor(4) as ex:
    FP = list(''')
t=t.replace('''EVENTS = pd.concat([pd.DataFrame(dict(session''','''print(f"first pass in {time.time() - T0:.0f} s")
EVENTS = pd.concat([pd.DataFrame(dict(session''')
t=t.replace('''VARS = [variants_for(i, s, fp) for i, (s, fp) in enumerate(zip(S, FP))]
with''','''VARS = [variants_for(i, s, fp) for i, (s, fp) in enumerate(zip(S, FP))]
T0 = time.time()
with''')
t=t.replace('''def replay(name):''','''print(f"variants in {time.time() - T0:.0f} s")

def replay(name):''')
open(p,'w').write(t)
E
$TMPDIR/venv/bin/python make_nb.py && time $TMPDIR/venv/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=-1 --output $TMPDIR/exec.ipynb reproduce_grosmark_2016.ipynb 2>&1 | grep -v WARNING | tail -5; $TMPDIR/venv/bin/python $TMPDIR/show.py $TMPDIR/exec.ipynb | sed -n '/cell 5 /,$p' | grep -v "^$" | head -400
```

```
[NbConvertApp] Converting notebook reproduce_grosmark_2016.ipynb to notebook
[NbConvertApp] Writing 253482 bytes to /tmp/claude-1001/exec.ipynb

real	16m59.253s
user	49m4.118s
sys	0m16.842s
---- cell 5 
loaded in 137 s
8 sessions loaded: ['Achilles_10252013', 'Achilles_11012013', 'Buddy_06272013', 'Cicero_09012014', 'Cicero_09102014', 'Cicero_09172014', 'Gatsby_08022013', 'Gatsby_08282013']
---- cell 6 ['sanity']
 subject           session          track  PRE_h  MAZE_min  POST_h  epochs_end_s  lfp_end_s  last_spike_s  pyr  int_  pyr_lCA1  pyr_rCA1  pos_rate pos_unit  lin_max_m  on_track_frac  run_s  lin_speed_run  xy_speed_run
Achilles Achilles_10252013 1.6mLinearMaze   5.02      34.5    4.09       34861.1    34861.1       34861.1  120    17        57        63     39.06   meters      1.600          0.128  244.0           49.8          52.0
Achilles Achilles_11012013   CircularMaze   5.37      44.6    4.06       36629.2    36629.2       36629.2   92    12        38        54     39.06   meters      2.900          0.585  984.0           24.0          25.3
   Buddy    Buddy_06272013 1.6mLinearMaze   2.98      38.8    2.22       21054.7    21054.7       21054.7   48    20        46         2     39.06   meters      1.600          0.072  161.0           53.7          56.9
  Cicero   Cicero_09012014 1.6mLinearMaze   4.31      92.7    3.80       34756.8    34756.8       34756.8   55    18        27        28     39.06   meters      1.600          0.218  632.0           18.9          20.5
  Cicero   Cicero_09102014   CircularMaze   4.79      50.5    4.51       36498.6    36498.6       36498.6   81    24        21        60     39.06   meters      2.842          0.287  603.0           22.5          24.7
  Cicero   Cicero_09172014   2mLinearMaze   4.44      51.3    4.02       33560.2    33560.2       33560.2   59    13        22        37     39.06   meters      2.000          0.321  599.0           16.7          18.6
  Gatsby   Gatsby_08022013 1.6mLinearMaze   4.74      38.
[... 341 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'E'
p='grosmark.py'; t=open(p).read()
t=t.replace('''    T, X = p.shape
    x = np.arange(X, dtype=float)
    # first and second moments of every rotation of every row
    rot = np.array([np.roll(x, -k) for k in range(X)])              # rot[k, i] = x[(i + k) % X]
''','''    T, X = p.shape
    x = np.arange(X, dtype=float)
    # first and second moments of every rotation of every row
    rot = x[(np.arange(X)[None, :] + np.arange(X)[:, None]) % X]   # rot[k, i] = x[(i + k) % X]
''')
t=t.replace('''            fs = np.array([np.roll(f[a], k) for k in shifts[d][c[a]]])  # (K, X)''','''            X = f.shape[1]
            fs = f[a][(np.arange(X)[None, :] - shifts[d][c[a]][:, None]) % X]  # np.roll by each shift''')
open(p,'w').write(t)
E
grep -n "rot = \|fs = f\[a\]" grosmark.py
$TMPDIR/venv/bin/python - <<'E'
import numpy as np
X=7; x=np.arange(X,dtype=float); f=np.random.rand(X); sh=np.array([1,3,6])
rot1=np.array([np.roll(x,-k) for k in range(X)]); rot2=x[(np.arange(X)[None,:]+np.arange(X)[:,None])%X]
print(np.array_equal(rot1,rot2), np.array_equal(np.array([np.roll(f,k) for k in sh]), f[(np.arange(X)[None,:]-sh[:,None])%X]))
E
```

```
446:    rot = x[(np.arange(X)[None, :] + np.arange(X)[:, None]) % X]   # rot[k, i] = x[(i + k) % X]
533:            fs = f[a][(np.arange(X)[None, :] - shifts[d][c[a]][:, None]) % X]  # np.roll by each shift
True True
```

**Agent calls Bash**

```bash
python - <<'E'
p='nb_cells.py'; t=open(p).read()
old='''print(EVENTS.assign(sig=EVENTS.rZ > 1.96).groupby("epoch").sig.mean().round(3).to_dict())
""", tags=["claim:fig1c-post-gt-pre"])'''
new='''print(EVENTS.assign(sig=EVENTS.rZ > 1.96).groupby("epoch").sig.mean().round(3).to_dict())
""", tags=["claim:fig1c-post-gt-pre"])

md(r"""
Variant, within sessions: the pooled test mixes sessions whose rZ differ in level (the circular
track sessions, with one template, score lower in every epoch) and in the number of events. A
one-sided rank-sum test of POST against PRE within each session, a sign test over the 8 sessions,
and the pooled comparison after subtracting each session's PRE mean.
""")

code(r"""
rows = []
for (sb, ss), df in EVENTS.groupby(["subject", "session"]):
    a = df.loc[df.epoch == "POST", "rZ"]; b = df.loc[df.epoch == "PRE", "rZ"]; m = df.loc[df.epoch == "MAZE", "rZ"]
    rows.append(dict(subject=sb, session=ss, POST_minus_PRE=a.mean() - b.mean(),
                     p_POST_gt_PRE=stats.mannwhitneyu(a, b, alternative="greater").pvalue,
                     MAZE_minus_PRE=m.mean() - b.mean(),
                     p_MAZE_gt_PRE=stats.mannwhitneyu(m, b, alternative="greater").pvalue))
W = pd.DataFrame(rows)
print(W.round(4).to_string(index=False))
n_pos = int((W.POST_minus_PRE > 0).sum())
print(f"sessions with POST > PRE: {n_pos} of 8, sign test p = {stats.binomtest(n_pos, 8, alternative='greater').pvalue:.4f}; "
      f"with one-sided p < 0.05: {int((W.p_POST_gt_PRE < 0.05).sum())}")
cen = EVENTS.copy()
cen["rZc"] = cen.rZ - cen.groupby("session").rZ.transform(lambda v: v[cen.loc[v.index, "epoch"] == "PRE"].mean())
a = cen.loc[cen.epoch == "POST", "rZc"]; b = cen.loc[cen.epoch == "PRE", "rZc"]
print(f"pooled after subtracting each session's PRE mean: POST {a.mean():+.3f}, rank-sum one-sided p = "
      f"{stats.mannwhitneyu(a, b, alternative='greater').pvalue:.3g}")
print("events per epoch on circular and linear tracks:")
print(EVENTS.merge(DATA[["session", "track"]]).assign(circular=lambda d: d.track == "CircularMaze")
      .groupby(["circular", "epoch"]).rZ.agg(["size", "mean"]).round(3).to_string())
""", tags=["claim:fig1c-post-gt-pre"])'''
assert old in t
t=t.replace(old,new)
open(p,'w').write(t)
E
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
$TMPDIR/venv/bin/python make_nb.py && time $TMPDIR/venv/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=-1 --output $TMPDIR/exec2.ipynb reproduce_grosmark_2016.ipynb 2>&1 | grep -v WARNING | tail -3; $TMPDIR/venv/bin/python $TMPDIR/show.py $TMPDIR/exec2.ipynb > $TMPDIR/out2.txt; $TMPDIR/venv/bin/python $TMPDIR/show.py $TMPDIR/exec.ipynb > $TMPDIR/out1.txt; diff $TMPDIR/out1.txt $TMPDIR/out2.txt
```

```
[NbConvertApp] Converting notebook reproduce_grosmark_2016.ipynb to notebook
[NbConvertApp] Writing 257485 bytes to /tmp/claude-1001/exec2.ipynb

real	8m8.525s
user	19m30.203s
sys	0m16.636s
16c16
< loaded in 137 s
---
> loaded in 135 s
59c59
< first pass in 282 s
---
> first pass in 160 s
142c142,165
< ---- cell 24 ['claim:fig2b-strong-contributors']
---
> ---- cell 23 ['claim:fig1c-post-gt-pre']
>  subject           session  POST_minus_PRE  p_POST_gt_PRE  MAZE_minus_PRE  p_MAZE_gt_PRE
> Achilles Achilles_10252013          0.1984         0.0000          0.5418         0.0000
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'E'
p='nb_cells.py'; t=open(p).read()
old='''    return dict(variant=name, n_PRE=len(pre), n_POST=len(post), mean_PRE=pre.mean(), mean_POST=post.mean(),
                diff=post.mean() - pre.mean(), p_one_sided=p, present=p < 0.05, sessions_POST_gt_PRE=sess)'''
new='''    # variant: each session's PRE mean subtracted from its PRE and POST scores
    pre_c = np.concatenate([r[name]["rZ"][r[name]["epoch"] == "PRE"] - r[name]["rZ"][r[name]["epoch"] == "PRE"].mean() for r in VRES])
    post_c = np.concatenate([r[name]["rZ"][r[name]["epoch"] == "POST"] - r[name]["rZ"][r[name]["epoch"] == "PRE"].mean() for r in VRES])
    pc = stats.mannwhitneyu(post_c, pre_c, alternative="greater").pvalue
    return dict(variant=name, n_PRE=len(pre), n_POST=len(post), mean_PRE=pre.mean(), mean_POST=post.mean(),
                diff=post.mean() - pre.mean(), p_one_sided=p, present=p < 0.05, sessions_POST_gt_PRE=sess,
                diff_within=post_c.mean(), p_within=pc)'''
assert old in t; t=t.replace(old,new)
t=t.replace('''"p_one_sided", "present", "sessions_POST_gt_PRE"]]''','''"p_one_sided", "present", "sessions_POST_gt_PRE", "diff_within", "p_within"]]''')
t=t.replace('''"p_one_sided", "present", "sessions_POST_gt_PRE"]].round(4)''','''"p_one_sided", "present", "sessions_POST_gt_PRE", "diff_within", "p_within"]].round(4)''')
t=t.replace('''shuffles per event. The rate split''','''shuffles per event. The rate split''')
t=t.replace('''here, in place of 200. The variants `no_plastic_v` and `no_rigid_v` use the classes from the
cell-level shift test.''','''here, in place of 200. The variants `no_plastic_v` and `no_rigid_v` use the classes from the
cell-level shift test. Replay is judged, as the criteria fix it, on all events pooled
(`present`); `diff_within` and `p_within` are a variant with each session's PRE mean subtracted
from its PRE and POST scores.''')
open(p,'w').write(t)
import re
print(t.count('diff_within'))
E
```

```
6
```

**Agent calls Bash**

```bash
grep -n "sessions_POST_gt_PRE" nb_cells.py
```

```
584:                diff=post.mean() - pre.mean(), p_one_sided=p, present=p < 0.05, sessions_POST_gt_PRE=sess,
600:                 ["n_PRE", "n_POST", "mean_PRE", "mean_POST", "diff", "p_one_sided", "present", "sessions_POST_gt_PRE", "diff_within", "p_within"]].round(4).to_string())
626:                                                     "p_one_sided", "present", "sessions_POST_gt_PRE", "diff_within", "p_within"]].round(4).to_string())
867:                                                    "p_one_sided", "present", "sessions_POST_gt_PRE", "diff_within", "p_within"]].round(4).to_string())
883:                                                    "p_one_sided", "present", "sessions_POST_gt_PRE", "diff_within", "p_within"]].round(4).to_string())
```

**Agent calls Bash**

```bash
python - <<'E'
p='nb_cells.py'; t=open(p).read()
blocked=["fig2b-strong-contributors","fig2-pre-post-overlap","fig2d-shuffle-high-dpcc","fig2e-remove-plastic","figs2-track-distribution","fig3a-plastic-specificity","fig3b-plastic-improve","fig4a-rigid-faster","fig4a-plastic-ripple-burst-coactivation"]
lines=t.split('\n')
for i,l in enumerate(lines):
    if l.startswith('| ') and l.endswith('| tested |'):
        cid=l[2:].split(':')[0]
        if cid in blocked:
            lines[i]=l.replace('| tested |','| blocked, methods_underspecified (analysis shown) |')
t='\n'.join(lines)
t=t.replace('''| Claim | Status |
|---|---|''','''Nine claims rest on the selection of strongly contributing cells (PCC). The test fixed for it
before the analysis has a false-positive rate of 58%, far from the 5% that "significant" implies,
so these claims are blocked as `methods_underspecified`; their analyses are still shown, with a
better calibrated variant of the test.

| Claim | Status |
|---|---|''')
open(p,'w').write(t)
E
$TMPDIR/venv/bin/python make_nb.py && $TMPDIR/venv/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=-1 --output $TMPDIR/exec3.ipynb reproduce_grosmark_2016.ipynb 2>&1 | grep -v WARNING | tail -1; $TMPDIR/venv/bin/python $TMPDIR/show.py $TMPDIR/exec3.ipynb > $TMPDIR/out3.txt; diff $TMPDIR/out2.txt $TMPDIR/out3.txt | grep -v "^---\|cell"
```

```
[NbConvertApp] Writing 260385 bytes to /tmp/claude-1001/exec3.ipynb
59c59
< first pass in 160 s
> first pass in 163 s
232,251c232,252
< variants in 121 s
<               n_PRE  n_POST  mean_PRE  mean_POST    diff  p_one_sided  present  sessions_POST_gt_PRE
< variant                                                                                             
< base          16448   23801    0.7951     0.7868 -0.0083       0.9160    False                     8
< top10         16448   23801    0.7917     0.7028 -0.0889       1.0000    False                     5
< bottom10      16448   23801    0.7159     0.7571  0.0412       0.0120     True                     8
< top20         16448   23801    0.7672     0.6505 -0.1167       1.0000    False                     4
< bottom20      16448   23801    0.7525     0.7769  0.0244       0.0778    False                     8
< top50         16448   23801    0.6672     0.5293 -0.1378       1.0000    False                     2
< bottom50      16448   23801    0.6788     0.7038  0.0249       0.0259     True                     7
< top75         16448   23801    0.6879     0.5168 -0.1711       1.0000    False                     1
< bottom75      16448   23801    0.6464     0.6560  0.0095       0.3505    False                     7
< no_plastic    14363   20527    0.7652     0.6081 -0.1572       1.0000    False                     3
< no_rigid      13353   20849    0.6399     0.6757  0.0358       0.0202     True                     8
< no_plastic_v  15310   22128    0.7330     0.6014 -0.1316       1.0000    False                     4
[... 92 more lines not kept]
```

**Agent**

The within-session variant shows the paper's pattern for fig2d, fig2e and fig4e, but outcomes are judged on the pooled tests the criteria fixed. Writing the conclusions and summary now.

**Agent calls Bash**

```bash
cat > $TMPDIR/concl.py <<'PYEOF'
C = []
C.append("""**Result: reproduced.** The dandiset holds 4 subjects and 8 sessions, each with PRE, MAZE and
POST epochs in that order (8 of 8), on a 1.6 m linear track (4 sessions), a 2 m linear track (1)
and a circular track (3). The rooms named in the paper are not in the files.""")
C.append("""**Result: not reproduced.** With a 1 Hz peak, 417 of the 562 pyramidal cells are place cells,
below the paper's 491 by more than the tolerance of 49. With a 0.5 Hz peak the count is 480,
within the tolerance, and with 2 Hz it is 352. The paper's definition is in the Methods, which
were not available.""")
C.append("""**Result: fig1c-maze-gt-pre reproduced; fig1c-post-gt-pre not reproduced.** MAZE events score
higher than PRE events (mean rZ 1.270 against 0.770; Tukey on ranks p printed as 0), and MAZE is
higher in all 8 sessions. Pooled over sessions, as the criterion fixes the test, POST does not
exceed PRE (0.763 against 0.770, Tukey on ranks p = 0.412). Within sessions it does: POST is
higher in 8 of 8 sessions (sign test p = 0.0039, one-sided rank-sum p < 0.05 in 6), and with each
session's PRE mean subtracted POST is higher by 0.106 (p = 2.3e-14). The pooled test is
dominated by the circular-track sessions, which score lower in every epoch (PRE 0.161, POST
0.260, against 1.112 and 1.207 on the linear tracks) and contribute 11161 of the 23801 POST
events but 5912 of the 16448 PRE events.""")
C.append("""**Result: blocked (methods_underspecified).** The test fixed in the criterion finds 307 strongly
contributing cells (73.6% of 417 place cells), against the paper's 216, but with every rate map
shifted it calls 57.6% of cells significant, so about 240 would be expected by chance. Its
false-positive rate is 0.853 and 0.905 on the linear tracks and 0.164 on the circular track. The
cell-level shift test (a variant) finds 223 cells, within the paper's tolerance, but its
false-positive rate is also high (0.297). Both are far from the 5% that a significance test
implies, so neither selection is the paper's.""")
C.append("""**Result: blocked (methods_underspecified)**, as it depends on fig2b-strong-contributors. Of 245 PRE
strongly contributing cells, 229 (93.5%) also contribute in POST, against a chance level of
69.8%; with the shift test, 141 of 173 (81.5%) against 45.8%.""")
C.append("""**Result: blocked (methods_underspecified)**, as dPCC comes from the PCC procedure of
fig2b-strong-contributors. On the pooled test of the criterion there is no replay before any
shuffling (POST minus PRE -0.008, p = 0.916), so its removal cannot be shown; after shuffling the
bottom 75% it is also absent (+0.010, p = 0.351). In the within-session variant replay is present
before shuffling (+0.107, p < 0.0001), falls to +0.021 (p = 0.20) after shuffling the top 10% and
to -0.006 (p = 0.83) after the top 20%, and remains after shuffling the bottom 75% (+0.095,
p < 0.0001), the pattern of the paper.""")
C.append("""**Result: blocked (methods_underspecified)**, as it depends on fig2b-strong-contributors. On the
pooled test, removing plastic cells gives POST minus PRE -0.157 (p = 1.0) and removing rigid
cells +0.036 (p = 0.020), the pattern the criterion asks for. In the within-session variant,
without plastic cells -0.032 (p = 0.998) and without rigid cells +0.151 (p < 0.0001); with the
shift-test classes -0.005 and +0.134. Plastic cells are those with the higher dPCC, so this
result follows partly from how they are chosen.""")
C.append("""**Result: blocked (methods_underspecified)**, as it depends on fig2b-strong-contributors. The
peak positions of rigid and plastic cells differ by the KS test fixed in the criterion (medians
0.419 and 0.501 of the track, D = 0.160, p = 0.034); with reading (b) p = 0.051 and with the
shift-test classes p = 0.12.""")
C.append("""**Result: blocked (methods_underspecified)**, as it depends on fig2b-strong-contributors. Plastic
cells carry more spatial information than rigid cells (median 0.887 against 0.592 bits per
spike, p = 0.00028; shift-test classes p = 0.0019), but their number of fields does not differ
(means 1.578 and 1.651, p = 0.52).""")
C.append("""**Result: blocked (methods_underspecified)**, as it depends on fig2b-strong-contributors. Both
groups increase their in-field ratio over the session (plastic median 0.146, p = 0.015; rigid
0.125, p = 0.032; between groups p = 0.61). With the shift-test classes plastic cells do not
increase significantly (p = 0.17) and rigid cells do (p = 0.021).""")
C.append("""**Result: blocked (methods_underspecified)**, as it depends on fig2b-strong-contributors. Rigid
cells fire somewhat faster (median 0.710 against 0.597 Hz) without significance (p = 0.059;
reading (b) p = 0.15; shift-test classes p = 0.39).""")
C.append("""**Result: blocked (methods_underspecified)**, as it depends on fig2b-strong-contributors. Of the
three measures only ripple gain is higher in plastic cells with p < 0.05 (4.412 against 3.927,
p = 0.037); bursting (0.177 against 0.149, p = 0.20) and coactivation (0.028 against 0.027,
p = 0.79) are not. With the shift-test classes none reaches p < 0.05 (gain p = 0.068).""")
C4 = ["""**Result: reproduced** (fig4c-pre-fast-coactivation). PRE coactivation rises with firing rate, from
0.0208 in the slowest window to 0.0486 in the fastest; the Spearman correlation on the averaged
curve is 0.861 and is positive in 6 of 8 sessions. The change in the fastest window does not
differ from 0 over sessions (sign-rank p = 0.383), consistent with the statement that these
correlations remain into POST.""",
"""**Result: not reproduced** (fig4c-slow-coactivation-increase). The POST minus PRE change does not
fall with firing rate (Spearman correlation -0.068 on the averaged curve, negative in 5 of 8
sessions); the criterion needs -0.5 or below.""",
"""**Result: not reproduced** (fig4c-slow-replay). The partial correlation of MAZE running and POST
coactivation given PRE is 0.186 in the slowest window and 0.115 in the fastest, but the Spearman
correlation over windows is 0.095 and is negative in only 4 of 8 sessions; the criterion needs
-0.5 or below and 5 sessions."""]
C.append("""**Result: partially reproduced.** Split by non-REM sleep rate, the low-rate median is 0.435 Hz
under both readings, just outside 0.39 +/- 0.039, and the high-rate median 1.091 (a) or 1.092 (b),
within 1.12 +/- 0.112. With the rate over all of PRE and POST (a variant) both are within
tolerance (0.395 and 1.041). The split is of 417 place cells, not the paper's 491.""")
C.append("""**Result: partially reproduced.** Under reading (a), which the criterion selects as neither
reading matched, low-rate cells carry more spatial information (median 0.975 against 0.622 bits
per spike, p = 4.1e-08), but their ripple-gain change from PRE to POST is not larger than that of
high-rate cells (0.251 against 0.155, p = 0.948). Reading (b) gives the same.""")
C.append("""**Result: not reproduced.** On the pooled test there is no replay with either half (low-rate
POST minus PRE -0.024, p = 0.964; high-rate -0.049, p = 0.9999), as for all cells. In the
within-session variant both halves show replay, larger for low-rate cells (+0.116 against
+0.058, both p <= 0.0001), which is the partial pattern of the criterion.""")
C.append("""**Result: not reproduced.** On the pooled test neither half shows replay (high-gain -0.001,
p = 0.71; low-gain -0.111, p = 1.0). In the within-session variant high-gain cells show replay
(+0.111, p < 0.0001) and low-gain cells do not (+0.016, p = 0.14), the paper's pattern.""")
SUMMARY = r"""## Summary

| Claim | Outcome |
|---|---|
| sessions-and-tracks | reproduced |
| place-cell-count (491) | not reproduced (417; 480 at 0.5 Hz) |
| fig1c-post-gt-pre | not reproduced by the pooled test; higher within all 8 sessions |
| fig1c-maze-gt-pre | reproduced |
| fig2b-strong-contributors (216) | blocked, methods_underspecified |
| fig2-pre-post-overlap (73%) | blocked, methods_underspecified |
| fig2d-shuffle-high-dpcc | blocked, methods_underspecified |
| fig2e-remove-plastic | blocked, methods_underspecified |
| figs2-track-distribution | blocked, methods_underspecified |
| fig3a-plastic-specificity | blocked, methods_underspecified |
| fig3b-plastic-improve | blocked, methods_underspecified |
| fig4a-rigid-faster | blocked, methods_underspecified |
| fig4a-plastic-ripple-burst-coactivation | blocked, methods_underspecified |
| fig4c-pre-fast-coactivation | reproduced |
| fig4c-slow-coactivation-increase | not reproduced |
| fig4c-slow-replay | not reproduced |
| rate-split-medians | partially reproduced |
| figs16-low-rate-info-gain | partially reproduced |
| fig4d-slow-sequences | not reproduced |
| fig4e-gain-sequences | not reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

How the analysis differs from the paper's:

- The supplementary Materials and Methods were not available. Place cells, candidate events
  (population bursts holding a ripple on one LFP channel), the decoder's details, the rZ shuffle,
  the PCC and its test, bursting, ripple gain and the field and in-field measures are common
  choices fixed before the analysis.
- The sequence score is decoded with each direction's template on the linear tracks, the event
  taking the larger rZ, and with one template on the circular track. The circular sessions score
  lower in every epoch, and pooling all events, as the criteria fix it, hides the POST over PRE
  increase that every session shows. The within-session variant recovers the paper's pattern for
  fig2d, fig2e and fig4e, but the outcomes are judged on the pooled test.
- The PCC test fixed in the criterion, a signed-rank test of a cell's contributions over events,
  has a false-positive rate near 58%, as the same random map enters all of a cell's events. This
  blocks the nine claims that rest on it. A cell-level shift test does better (30%) but is still
  far from 5%.

What was found about the dandiset:

- The data hold what the paper's replay analyses need: sorted units with a cell type, positions,
  epochs, sleep states and the LFP, all on one clock (shown by decoding position, ripple-burst
  coincidence and the theta/delta ratio of the sleep states). No candidate events, ripples, place
  cell lists or PCC values are stored, so the paper's selections cannot be checked against it.
- In versions 0.210812.1516 and 0.250624.0426 the position series store the sampling period
  (0.0256 s) as their rate; version 0.261005.2101 corrects it.
- In Gatsby_08022013 the POST epoch ends at 30413.6 s while the spikes, LFP and states run to
  32002 s.
- On the circular track the animals ran toward decreasing linearized position; the description
  says the position increases clockwise but not which way they ran. The linearized position there
  reaches 2.84 to 2.9 m, against the 3.14 m circumference of the described 1 m track.
- The description lists neck EMG and accelerometer signals; the files hold neither.
- Electrode `location` is "unknown" for every channel; the units carry the hemisphere (lCA1 or
  rCA1).
"""
PYEOF
python - <<'E'
import os
exec(open(os.environ['TMPDIR']+'/concl.py').read())
p='nb_cells.py'; t=open(p).read()
for c in C[:12]:
    i=t.index('md("**Result: TBD**")'); t=t[:i]+'md(r"""\n'+c+'\n""")'+t[i+len('md("**Result: TBD**")'):]
for c,suf in zip(C4,['fig4c-pre-fast-coactivation','fig4c-slow-coactivation-increase','fig4c-slow-replay']):
    s=f'md("**Result: TBD** ({suf})")'; assert s in t; t=t.replace(s,'md(r"""\n'+c+'\n""")')
for c in C[12:]:
    i=t.index('md("**Result: TBD**")'); t=t[:i]+'md(r"""\n'+c+'\n""")'+t[i+len('md("**Result: TBD**")'):]
old='''md(r"""
## Summary

TBD
""")'''
assert old in t
t=t.replace(old,'md(r"""\n'+SUMMARY+'""")')
assert 'TBD' not in t
open(p,'w').write(t)
E
grep -c "Result:" nb_cells.py
```

```
19
```

**Agent calls Bash**

```bash
python - <<'E'
p='nb_cells.py'; t=open(p).read()
old='''        xy_speed_run=round(float(np.nanmedian(sp[run])), 1),
    ))'''
new='''        xy_speed_run=round(float(np.nanmedian(sp[run])), 1),
        run_up_frac=round(float(np.mean(v[np.isfinite(v)] > g.RUN_SPEED)), 3),
        run_down_frac=round(float(np.mean(v[np.isfinite(v)] < -g.RUN_SPEED)), 3),
        directions=str(g.directions(s)),
    ))'''
assert old in t; t=t.replace(old,new)
old='''- No unit spike train or position series appears in more than one file.'''
new='''- No unit spike train or position series appears in more than one file.
- In Gatsby_08022013 the POST epoch ends at 30413.6 s, while the LFP, the spikes and the sleep
  states run to about 32000 s. Firing rates over the session use the LFP duration.
- On the circular track the linearized position mostly decreases while the animal runs
  (`run_down_frac` against `run_up_frac`), so its single template is built from running toward
  decreasing position. The description says the position increases clockwise, not which way the
  animals ran.'''
assert old in t; t=t.replace(old,new)
t=t.replace('''has a false-positive rate near 58%, as the same random map enters all of a cell's events.''','''has a false-positive rate near 58%, likely because the same map enters all of a cell's events,
which the test treats as independent.''')
open(p,'w').write(t)
E
mv make_nb.py nb_cells.py $TMPDIR/ && cd $TMPDIR && sed -i 's|exec(open("nb_cells.py").read())|exec(open("'$TMPDIR'/nb_cells.py").read())|; s|nbf.write(nb, "reproduce_grosmark_2016.ipynb")|nbf.write(nb, "entries/000044-grosmark-2016/reproduce_grosmark_2016.ipynb")|' make_nb.py && $TMPDIR/venv/bin/python make_nb.py && ls entries/000044-grosmark-2016/
```

```
__pycache__
grosmark.py
reproduce_grosmark_2016.ipynb
Shell cwd was reset to
```

**Agent**

Now the entry files, then lock and run.

**Agent calls Bash**

```bash
cd entries/000044-grosmark-2016 && rm -rf __pycache__ && cat > entry.yaml <<'E'
schema_version: 1
name: 000044-grosmark-2016
type: reproduction
title: Rigid and plastic hippocampal sequences (Grosmark and Buzsaki 2016)
description: Tests the findings of Grosmark and Buzsaki (2016) on dandiset 000044, which holds eight
  sessions of CA1 units, LFP, sleep states and track positions from four rats, each with sleep
  before and after exploring a novel track. It decodes candidate ripple events with a Bayesian
  decoder, compares sequence scores across PRE, MAZE and POST, estimates each place cell's
  contribution to sequences, and relates firing rate and ripple gain to coactivation and replay.
license: Apache-2.0
notebooks:
- path: reproduce_grosmark_2016.ipynb
  title: Reproducing Grosmark and Buzsaki (2016) from dandiset 000044
  runtime_minutes: 9
helpers:
- grosmark.py
related:
- id: dandi:000044/0.261005.2101
  relation: uses_data
- id: doi:10.1126/science.aad1935
  relation: reproduces
E
printf "dandi\nh5py\nmatplotlib\nnumpy\npandas\nremfile\nscipy\n" > requirements.in
cat ../001453-fouke-2025/entry.yaml | head -3 >/dev/null
cd ../.. && python -c "import yaml,jsonschema,nbformat" && python tools/entry.py lock entries/000044-grosmark-2016 2>&1 | tail -3
```

```
wrote entries/000044-grosmark-2016/requirements.lock.txt
```

**Agent calls Bash**

```bash
time python tools/entry.py all entries/000044-grosmark-2016 2>&1 | tail -15
```

```
Installed kernelspec registry-000044-grosmark-2016 in executed/000044-grosmark-2016/.venv/share/jupyter/kernels/registry-000044-grosmark-2016
0 error(s)
pass  reproduce_grosmark_2016.ipynb  (493 s)

real	8m18.933s
user	19m42.704s
sys	0m18.719s
```

**Agent calls Bash**

```bash
ls executed/000044-grosmark-2016/; $TMPDIR/venv/bin/python $TMPDIR/show.py executed/000044-grosmark-2016/reproduce_grosmark_2016.ipynb > $TMPDIR/out4.txt; diff $TMPDIR/out3.txt $TMPDIR/out4.txt | grep -v "^---" | grep -v "cell [0-9]"
```

```
reproduce_grosmark_2016.ipynb
result.json
16c16
< loaded in 135 s
> loaded in 134 s
20,28c20,28
<  subject           session          track  PRE_h  MAZE_min  POST_h  epochs_end_s  lfp_end_s  last_spike_s  pyr  int_  pyr_lCA1  pyr_rCA1  pos_rate pos_unit  lin_max_m  on_track_frac  run_s  lin_speed_run  xy_speed_run
< Achilles Achilles_10252013 1.6mLinearMaze   5.02      34.5    4.09       34861.1    34861.1       34861.1  120    17        57        63     39.06   meters      1.600          0.128  244.0           49.8          52.0
< Achilles Achilles_11012013   CircularMaze   5.37      44.6    4.06       36629.2    36629.2       36629.2   92    12        38        54     39.06   meters      2.900          0.585  984.0           24.0          25.3
<    Buddy    Buddy_06272013 1.6mLinearMaze   2.98      38.8    2.22       21054.7    21054.7       21054.7   48    20        46         2     39.06   meters      1.600          0.072  161.0           53.7          56.9
<   Cicero   Cicero_09012014 1.6mLinearMaze   4.31      92.7    3.80       34756.8    34756.8       34756.8   55    18        27        28     39.06   meters      1.600          0.218  632.0           18.9          20.5
<   Cicero   Cicero_09102014   CircularMaze   4.79      50.5    4.51       36498.6    36498.6       36498.6   81    24        21        60     39.06   meters      2.842          0.287  603.0           22.5          24.7
<   Cicero   Cicero_09172014   2mLinearMaze   4.44      51.3    4.02       33560.2    33560.2       33560.2   59    13        22        37     39.06   meters      2.000          0.321  599.0           16.7          18.6
<   Gatsby   Gatsby_08022013 1.6mLinearMaze   4.74      38.9    3.06       30413.6    32002.4       32002.4   66    14        18        48     39.06   meters      1.600          0.187  340.0           36.8          37.9
<   Gatsby   Gatsby_08282013   CircularMaze   4.66      44.9    4.42       35347.9    35347.9       35347.9   41    10        41         0     3
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'E'
import os
p=os.environ['TMPDIR']+'/nb_cells.py'; t=open(p).read()
old='''0 to 2 m on the 2 m track, consistent with the description. On the circular track (described as
  1 m in diameter, a circumference of 3.14 m) it reaches about 2.84 to 2.9 m. The running speed'''
new='''0 to 2 m on the 2 m track, consistent with the description. On the circular track (described as
  1 m in diameter, a circumference of 3.14 m) it reaches 2.84 to 2.9 m, consistent with the series
  description, which has it run from one edge of the reward area to the other. The running speed'''
assert old in t; t=t.replace(old,new)
old='''- On the circular track the animals ran toward decreasing linearized position; the description
  says the position increases clockwise but not which way they ran. The linearized position there
  reaches 2.84 to 2.9 m, against the 3.14 m circumference of the described 1 m track.'''
new='''- On the circular track the animals ran toward decreasing linearized position; the description
  says the position increases clockwise but not which way they ran.'''
assert old in t; t=t.replace(old,new)
open(p,'w').write(t)
E
$TMPDIR/venv/bin/python $TMPDIR/make_nb.py && echo regenerated
```

```
regenerated
```

**Agent**

Now the entry README and the attempt record.

**Agent calls Write**

```json
{
 "file_path": "entries/000044-grosmark-2016/README.md",
 "content": "# Grosmark & Buzsáki (2016) from dandiset 000044\n\nTests the findings of [Grosmark and Buzsáki (2016)](https://doi.org/10.1126/science.aad1935) on\n[DANDI:000044](https://dandiarchive.org/dandiset/000044/0.261005.2101), which holds eight sessions\nof CA1 units, LFP, sleep states and track positions from four rats, each with sleep before (PRE)\nand after (POST) a first exploration of a novel track (MAZE). The supplementary Methods could not\nbe read, so the definitions the main text leaves open are common choices fixed before the\nanalysis.\n\n| Claim | Outcome |\n|---|---|\n| Four rats, eight sessions, two linear tracks and a circular one | Reproduced |\n| 491 place cells | Not reproduced (417; 480 at a 0.5 Hz threshold) |\n| Sequence scores higher in POST than in PRE | Not reproduced by the pooled test; higher within all 8 sessions |\n| Sequence scores higher in MAZE than in PRE | Reproduced |\n| PRE coactivation dominated by fast-firing cells | Reproduced |\n| Slow-firing cells gain the most coactivation from PRE to POST | Not reproduced |\n| Slow-firing cells show the most replay of coactivation | Not reproduced |\n| Low and high-rate medians of 0.39 and 1.12 Hz | Partially reproduced |\n| Low-rate cells more informative, with a larger ripple-gain increase | Partially reproduced |\n| Slow but not fast cells increase sequence content | Not reproduced |\n| Increase in sequence content limited to high ripple-gain cells | Not reproduced |\n| Nine claims on strongly contributing, rigid and plastic cells (PCC) | Blocked: methods underspecified |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe attempt record, with the reasons and the differences from the paper's method, is\n[`attempts/000044-grosmark-2016-01.yaml`](../../attempts/000044-grosmark-2016-01.yaml).\n\n- `reproduce_grosmark_2016.ipynb`: the analysis. It takes about nine minutes on four cores, two of\n  them streaming one LFP channel per session.\n- `grosmark.py`: loading the files, ripple detection on one channel, candidate events, rate maps,\n  the Bayesian decoder with its weighted-correlation score, the per-cell contributions and the\n  cell measures. Other notebooks on this dandiset can import it.\n"
}
```

```
File created successfully at: entries/000044-grosmark-2016/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "attempts/000044-grosmark-2016-01.yaml",
 "content": "schema_version: 1\nid: 000044-grosmark-2016-01\ndandiset: \"000044\"\ndandiset_version: 0.261005.2101\npaper: doi:10.1126/science.aad1935\ndate: 2026-10-16\nentry: 000044-grosmark-2016\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code (GitHub Actions)\n    model: claude-opus-5-5\n    protocol: pilot-7\noutcomes:\n- claim: sessions-and-tracks\n  outcome: reproduced\n  notebook: reproduce_grosmark_2016.ipynb\n  output: claim:sessions-and-tracks\n  notes: 4 subjects and 8 sessions, each with PRE, MAZE and POST epochs in that order (8 of 8), on\n    a 1.6 m linear track (4 sessions), a 2 m linear track (1) and a circular track (3). PRE lasts\n    2.98 to 5.37 h, MAZE 34.5 to 92.7 min and POST 2.22 to 4.51 h. The rooms the paper names are not\n    in the files.\n- claim: place-cell-count\n  outcome: not_reproduced\n  notebook: reproduce_grosmark_2016.ipynb\n  output: claim:place-cell-count\n  measured: 417\n  notes: 417 of the 562 pyramidal units have a smoothed rate-map peak of 1 Hz or more on running,\n    below 491 by more than the tolerance of 49. At 0.5 Hz the count is 480 (within tolerance), at\n    2 Hz 352. By subject, Achilles 181, Buddy 30, Cicero 127, Gatsby 79.\n  deviations:\n  - The place-cell definition is a common choice (peak of 1 Hz or more on running above 5 cm/s, 2\n    cm bins, 4 cm smoothing); the paper's definition is in the supplementary Methods, which were\n    not available.\n- claim: fig1c-post-gt-pre\n  outcome: not_reproduced\n  notebook: reproduce_grosmark_2016.ipynb\n  output: claim:fig1c-post-gt-pre\n  notes: Pooled over sessions, as the criterion fixes the test, POST does not exceed PRE (mean rZ\n    0.763 against 0.770, Tukey on ranks after Kruskal-Wallis p = 0.412). Within sessions it does;\n    POST is higher in 8 of 8 sessions (sign test p = 0.0039; one-sided rank-sum p < 0.05 in 6), and\n    with each session's PRE mean subtracted POST is higher by 0.106 (p = 2.3e-14). The pooled test\n    is dominated by the three circular-track sessions, which score lower in every epoch (PRE 0.161\n    and POST 0.260 against 1.112 and 1.207 on the linear tracks, where the event takes the better\n    of two templates) and supply 11161 of 23801 POST events but 5912 of 16448 PRE events. By\n    subject, POST minus PRE is +0.089 (Achilles), +0.185 (Buddy), +0.021 (Cicero) and -0.173\n    (Gatsby) when pooled within subject.\n  deviations:\n  - Candidate events are population bursts of all units holding a ripple (150 to 250 Hz envelope\n    above 3 SD on one LFP channel per session), outside REM in PRE and POST and below 5 cm/s in\n    MAZE; the paper's detection is in the unavailable Methods.\n  - The rZ null is 200 column-cycle shuffles of the posterior; the paper's shuffle is not stated in\n    the main text.\n  - On the linear tracks each event takes the better of the two direction templates, which raises\n    their scores over those of the single-template circular track.\n- claim: fig1c-maze-gt-pre\n  outcome: reproduced\n  notebook: reproduce_grosmark_2016.ipynb\n  output: claim:fig1c-maze-gt-pre\n  notes: MAZE events score higher than PRE events (mean rZ 1.270 against 0.770, n = 2460 and 16448;\n    Tukey on ranks p printed as 0), and MAZE is higher in all 8 sessions (one-sided rank-sum p from\n    below 0.0001 to 0.0405).\n  deviations:\n  - Events and scores as for fig1c-post-gt-pre.\n- claim: fig2b-strong-contributors\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_grosmark_2016.ipynb\n  output: claim:fig2b-strong-contributors\n  notes: The test fixed in the criterion (one-sided signed-rank test of a cell's contributions over\n    its events, p < 0.05) finds 307 strongly contributing cells (73.6% of 417 place cells), against\n    216. With every rate map shifted it calls 57.6% of cells significant (0.853 and 0.905 on the\n    linear tracks, 0.164 on the circular track), so about 240 would be expected by chance. The\n    paper calls these PCC scores significant, which implies a 5% false-positive rate; this test is\n    far from it, so it is not the paper's procedure. A cell-level shift test (the cell's mean\n    contribution against each of its 20 shifted maps) finds 223 cells, within the tolerance, but\n    its false-positive rate is 0.297. The PCC definition and its test are in the unavailable\n    Methods.\n  deviations:\n  - The PCC and its significance test are choices made here, as the Methods were not available.\n- claim: fig2-pre-post-overlap\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_grosmark_2016.ipynb\n  output: claim:fig2-pre-post-overlap\n  notes: Blocked as it depends on fig2b-strong-contributors. Of 245 PRE strongly contributing\n    cells, 229 (93.5%) also contribute in POST, against a chance level of 69.8%. With the shift-test\n    variant 141 of 173 (81.5%) against 45.8%.\n- claim: fig2d-shuffle-high-dpcc\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_grosmark_2016.ipynb\n  output: claim:fig2d-shuffle-high-dpcc\n  notes: Blocked as dPCC comes from the procedure of fig2b-strong-contributors. On the pooled test\n    of the criterion there is no replay before shuffling (POST minus PRE -0.008, p = 0.916), and\n    none after shuffling the bottom 75% (+0.010, p = 0.351) or the top 10% (-0.089). In the\n    within-session variant replay is present before shuffling (+0.107, p < 0.0001), falls to +0.021\n    (p = 0.20) after shuffling the top 10% and -0.006 (p = 0.83) after the top 20%, and remains after\n    the bottom 75% (+0.095, p < 0.0001), the paper's pattern.\n  deviations:\n  - Variant decodes use 50 column-cycle shuffles per event in place of 200.\n- claim: fig2e-remove-plastic\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_grosmark_2016.ipynb\n  output: claim:fig2e-remove-plastic\n  notes: Blocked as it depends on fig2b-strong-contributors. On the pooled test, removing plastic\n    cells gives POST minus PRE -0.157 (p = 1.0) and removing rigid cells +0.036 (p = 0.020). In the\n    within-session variant, -0.032 (p = 0.998) and +0.151 (p < 0.0001); with the shift-test classes\n    -0.005 and +0.134. Plastic cells are those with the higher dPCC, so the result follows partly\n    from how they are chosen.\n- claim: figs2-track-distribution\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_grosmark_2016.ipynb\n  output: claim:figs2-track-distribution\n  notes: Blocked as it depends on fig2b-strong-contributors. Rate-map peaks of rigid and plastic\n    cells differ by the KS test (medians 0.419 and 0.501 of the track, D = 0.160, p = 0.034); with\n    the split over all place cells p = 0.051, with the shift-test classes p = 0.12.\n- claim: fig3a-plastic-specificity\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_grosmark_2016.ipynb\n  output: claim:fig3a-plastic-specificity\n  notes: Blocked as it depends on fig2b-strong-contributors. Plastic cells carry more spatial\n    information (median 0.887 against 0.592 bits per spike, p = 0.00028; shift-test classes p =\n    0.0019), but the number of fields does not differ (means 1.578 and 1.651, p = 0.52).\n- claim: fig3b-plastic-improve\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_grosmark_2016.ipynb\n  output: claim:fig3b-plastic-improve\n  notes: Blocked as it depends on fig2b-strong-contributors. Both groups raise their in-field\n    ratio over the session (change of log10 ratio, plastic median 0.146, p = 0.015; rigid 0.125, p =\n    0.032; between groups p = 0.61). With the shift-test classes plastic p = 0.17 and rigid p =\n    0.021.\n- claim: fig4a-rigid-faster\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_grosmark_2016.ipynb\n  output: claim:fig4a-rigid-faster\n  notes: Blocked as it depends on fig2b-strong-contributors. Rigid cells fire somewhat faster\n    (median 0.710 against 0.597 Hz) without significance (p = 0.059; split over all place cells p =\n    0.15; shift-test classes p = 0.39).\n- claim: fig4a-plastic-ripple-burst-coactivation\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_grosmark_2016.ipynb\n  output: claim:fig4a-plastic-ripple-burst-coactivation\n  notes: Blocked as it depends on fig2b-strong-contributors. Ripple gain is higher in plastic\n    cells (4.412 against 3.927, p = 0.037); bursting (0.177 against 0.149, p = 0.20) and\n    coactivation (0.028 against 0.027, p = 0.79) are not. With the shift-test classes none reaches\n    p < 0.05 (gain p = 0.068).\n- claim: fig4c-pre-fast-coactivation\n  outcome: reproduced\n  notebook: reproduce_grosmark_2016.ipynb\n  output: claim:fig4c-pre-fast-coactivation\n  notes: PRE coactivation rises with firing rate, from 0.0208 in the slowest window to 0.0486 in\n    the fastest; Spearman correlation 0.861 on the averaged curve, positive in 6 of 8 sessions. The\n    POST minus PRE change of the fastest window does not differ from 0 over sessions (sign-rank p =\n    0.383), which fits the statement that these correlations remain into POST.\n  deviations:\n  - Coactivation over whole epochs, all states; the paper's restriction, if any, is not stated in\n    the main text.\n- claim: fig4c-slow-coactivation-increase\n  outcome: not_reproduced\n  notebook: reproduce_grosmark_2016.ipynb\n  output: claim:fig4c-slow-coactivation-increase\n  notes: The POST minus PRE change does not fall with firing rate; Spearman correlation -0.068 on\n    the averaged curve (p = 0.55), negative in 5 of 8 sessions. The averaged change is 0.0019 in\n    the slowest window and -0.0007 in the fastest, with a maximum of 0.0090.\n  deviations:\n  - Coactivation over whole epochs, all states.\n- claim: fig4c-slow-replay\n  outcome: not_reproduced\n  notebook: reproduce_grosmark_2016.ipynb\n  output: claim:fig4c-slow-replay\n  notes: The partial correlation of MAZE running and POST coactivation given PRE is 0.186 in the\n    slowest window and 0.115 in the fastest, but the Spearman correlation over windows is 0.095\n    and negative in only 4 of 8 sessions. By subject it is -0.588 (Achilles), -0.646 (Buddy),\n    -0.070 (Cicero) and 0.671 (Gatsby).\n  deviations:\n  - MAZE coactivation is taken over running bins (above 5 cm/s on the track).\n- claim: rate-split-medians\n  outcome: partially_reproduced\n  notebook: reproduce_grosmark_2016.ipynb\n  output: claim:rate-split-medians\n  measured:\n  - 0.435\n  - 1.091\n  notes: Split by non-REM sleep rate, the low-rate median is 0.435 Hz under both readings, just\n    outside 0.39 +/- 0.039, and the high-rate median 1.091 Hz (a, within sessions) or 1.092 (b,\n    pooled), within 1.12 +/- 0.112. With the rate over all of PRE and POST (a variant) both are\n    within tolerance (0.395 and 1.041 under reading a). The split is of 417 place cells, not 491.\n  deviations:\n  - The paper does not say whether the split is within sessions or pooled; both readings are shown\n    and give the same medians.\n  - Off-line sleep rate is taken as the non-REM rate in PRE and POST; the rate over all of PRE and\n    POST is a variant.\n- claim: figs16-low-rate-info-gain\n  outcome: partially_reproduced\n  notebook: reproduce_grosmark_2016.ipynb\n  output: claim:figs16-low-rate-info-gain\n  notes: Under reading (a), which the criterion selects as neither reading of rate-split-medians\n    matched, low-rate cells carry more spatial information (median 0.975 against 0.622 bits per\n    spike, p = 4.1e-08), but their ripple-gain change from PRE to POST is not larger (0.251 against\n    0.155, p = 0.948). Reading (b) gives the same.\n  deviations:\n  - Ripple gain is the rate within candidate events over the epoch rate; the paper's definition is\n    in fig. S16, which was not available.\n- claim: fig4d-slow-sequences\n  outcome: not_reproduced\n  notebook: reproduce_grosmark_2016.ipynb\n  output: claim:fig4d-slow-sequences\n  notes: On the pooled test neither half shows replay (low-rate POST minus PRE -0.024, p = 0.964;\n    high-rate -0.049, p = 0.9999), as for all cells (-0.008, p = 0.916). In the within-session\n    variant both halves show replay, larger for low-rate cells (+0.116 against +0.058, p below\n    0.0001 for each), which would be the criterion's partial pattern.\n  deviations:\n  - Variant decodes use 50 column-cycle shuffles per event in place of 200.\n- claim: fig4e-gain-sequences\n  outcome: not_reproduced\n  notebook: reproduce_grosmark_2016.ipynb\n  output: claim:fig4e-gain-sequences\n  notes: On the pooled test neither half shows replay (high-gain -0.001, p = 0.71; low-gain -0.111,\n    p = 1.0). In the within-session variant high-gain cells show replay (+0.111, p < 0.0001) and\n    low-gain cells do not (+0.016, p = 0.14), the paper's pattern.\n  deviations:\n  - Gain is the rate within PRE and POST candidate events over the PRE and POST rate, split at the\n    session median.\n  - Variant decodes use 50 column-cycle shuffles per event in place of 200.\nfindings:\n- kind: metadata_error\n  statement: In versions 0.210812.1516 and 0.250624.0426 every position series stores its sampling\n    period (0.0256 s) as its rate, so the positions span about 900 to 2400 hours in place of the\n    MAZE epoch. Version 0.261005.2101 stores 39.06 Hz, which matches the epoch lengths.\n- kind: metadata_error\n  statement: In Gatsby_08022013 the POST epoch ends at 30413.6 s, while the LFP, the spikes and the\n    sleep states run to about 32000 s.\n- kind: data_missing\n  statement: The dandiset description lists neck EMG and head-mounted accelerometer signals, and\n    the files hold neither; they also hold no wide-band data (acquisition is empty), only the LFP at\n    1250 Hz.\n- kind: data_missing\n  statement: The paper's derived data are not deposited. There are no candidate or ripple events,\n    no place-cell list, no sequence scores and no PCC values or rigid and plastic labels, so the\n    paper's selections cannot be checked against the dandiset and every one must be rebuilt.\n- kind: methods_unavailable\n  statement: Neither the paper nor the dandiset links analysis code, and the supplementary\n    Materials and Methods, which define the candidate events, place cells, the PCC and its test,\n    are not openly available (PMC and Science serve them only behind a browser check).\n- kind: metadata_insufficient\n  statement: Every electrode's location is \"unknown\" and no depth or layer is given, so the\n    channel for ripple detection has to be chosen from the signals. Units carry only the\n    hemisphere (lCA1 or rCA1). Subject age is \"/\".\n- kind: metadata_insufficient\n  statement: On the circular track the animals ran toward decreasing linearized position (47 to 63%\n    of samples against 7 to 16% the other way). The series description says the position increases\n    clockwise but not which way the animals ran.\n"
}
```

```
File created successfully at: attempts/000044-grosmark-2016-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
sed -i 's/period (0.0256 s) as its rate, so the positions span about 900 to 2400 hours in place of the/period (0.0256 s) as its rate, so the positions span about 880 to 2360 hours in place of the/' attempts/000044-grosmark-2016-01.yaml && python - <<'E'
import os
p=os.environ['TMPDIR']+'/nb_cells.py'; t=open(p).read()
old="sampling period (0.0256 s) in place of the rate (39.06 Hz), so the positions would span about\n60 hours in place of the MAZE epoch."
assert old in t
t=t.replace(old,"sampling period (0.0256 s) in place of the rate (39.06 Hz), so the positions would span 880 to\n2360 hours in place of the MAZE epoch.")
open(p,'w').write(t)
E
$TMPDIR/venv/bin/python $TMPDIR/make_nb.py && python -c "
import yaml;d=yaml.safe_load(open('attempts/000044-grosmark-2016-01.yaml'));print(len(d['outcomes']))
import collections;print(collections.Counter(o['outcome'] for o in d['outcomes']))" && grep -n ': .*: ' attempts/000044-grosmark-2016-01.yaml claims/000044/*.yaml | grep -v "^\S*:\s*-\? \?[a-z_]*: " | head
```

```
20
Counter({'blocked': 9, 'not_reproduced': 6, 'reproduced': 3, 'partially_reproduced': 2})
```

**Agent calls Bash**

```bash
grep -n -i "—\|\brather\b" attempts/000044-grosmark-2016-01.yaml claims/000044/*.yaml entries/000044-grosmark-2016/README.md entries/000044-grosmark-2016/grosmark.py entries/000044-grosmark-2016/reproduce_grosmark_2016.ipynb | head; grep -c "\*\*" entries/000044-grosmark-2016/README.md
```

```
0
```

**Agent calls Bash**

```bash
grep -o '\*\*[^*]*\*\*' $TMPDIR/nb_cells.py | grep -v "Result" ; sed -i 's/version\n\*\*0.261005.2101\*\*/X/; s/\*\*0\.261005\.2101\*\*/0.261005.2101/' $TMPDIR/nb_cells.py; grep -o '\*\*[^*]*\*\*' $TMPDIR/nb_cells.py | grep -v "Result"; $TMPDIR/venv/bin/python $TMPDIR/make_nb.py && time python tools/entry.py all entries/000044-grosmark-2016 2>&1 | tail -3
```

```
**0.261005.2101**
Installed kernelspec registry-000044-grosmark-2016 in executed/000044-grosmark-2016/.venv/share/jupyter/kernels/registry-000044-grosmark-2016
0 error(s)
pass  reproduce_grosmark_2016.ipynb  (498 s)

real	8m24.795s
user	19m46.388s
sys	0m19.195s
```

**Agent calls Bash**

```bash
$TMPDIR/venv/bin/python $TMPDIR/show.py executed/000044-grosmark-2016/reproduce_grosmark_2016.ipynb > $TMPDIR/out5.txt; diff $TMPDIR/out4.txt $TMPDIR/out5.txt | grep -v "^---" | grep -v " in [0-9]* s"; python tools/entry.py handover entries/000044-grosmark-2016 2>&1 | tail -5; ls executed/000044-grosmark-2016/handover; git status --short
```

```
16c16
59c59
233c233
367a368
> 
wrote executed/000044-grosmark-2016/handover
10.1126-science.aad1935.yaml
grosmark.py
reproduce_grosmark_2016.ipynb
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
?? attempts/000044-grosmark-2016-01.yaml
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
ls -la .bashrc .gitconfig .idea .mcp.json scripts .vscode 2>&1 | head -20; ls scripts | head
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 16 04:25 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 16 04:25 .gitconfig
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 16 04:25 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 16 04:25 .mcp.json
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 16 04:25 .vscode
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 16 04:25 scripts
scripts
```

**Agent**

I've finished steps 1 to 6 for dandiset 000044 (Grosmark & Buzsáki 2016). Locking, checking and running the entry from a clean environment passed (`0 error(s)`), and the handover package is in `executed/000044-grosmark-2016/handover/`. Nothing is committed. The files are the claims in `claims/000044/10.1126-science.aad1935.yaml`, the attempt in `attempts/000044-grosmark-2016-01.yaml`, and the entry in `entries/000044-grosmark-2016/` (notebook, `grosmark.py`, README, lock).

Paper text used: the full main text and the Figure 1 to 4 legends, from the NIH author manuscript (PMC4919122). The supplementary Materials and Methods and the figure images could not be downloaded: PMC and Science serve them only behind a browser check.

### 1. Outcomes

| Claim | Outcome |
|---|---|
| sessions-and-tracks | reproduced |
| place-cell-count (491) | not reproduced: 417 at a 1 Hz threshold, 480 at 0.5 Hz |
| fig1c-post-gt-pre | not reproduced by the pooled test; POST is higher within all 8 sessions (sign test p = 0.0039) |
| fig1c-maze-gt-pre | reproduced |
| fig2b-strong-contributors, fig2-pre-post-overlap, fig2d, fig2e, figs2, fig3a, fig3b, fig4a-rigid-faster, fig4a-plastic-ripple-burst-coactivation | blocked, methods_underspecified (analyses still shown) |
| fig4c-pre-fast-coactivation | reproduced |
| fig4c-slow-coactivation-increase | not reproduced |
| fig4c-slow-replay | not reproduced |
| rate-split-medians | partially reproduced (0.435 and 1.091 Hz) |
| figs16-low-rate-info-gain | partially reproduced |
| fig4d-slow-sequences | not reproduced |
| fig4e-gain-sequences | not reproduced |

Totals: 3 reproduced, 2 partially reproduced, 6 not reproduced, 9 blocked.

The pooled replay test that the criteria fixed is swamped by the three circular-track sessions. They score low in every epoch and supply nearly half the POST events. With each session's PRE mean subtracted (a variant, which does not change outcomes), the paper's pattern appears for fig2d, fig2e and fig4e.

### 2. The dandiset

- **Contents:** 8 sessions from 4 rats: 562 pyramidal units and 128 interneurons, LFP at 1250 Hz, sleep states, epochs and positions. Spikes, LFP, sleep states and positions all share one clock; three contrast checks confirm it.
- **Version pinned:** 0.261005.2101, the latest. The paper cites no version, and the two earlier versions store the position sampling period (0.0256 s) as the rate.
- **Epoch error:** in Gatsby_08022013 the POST epoch ends at 30413.6 s, while the data run to about 32002 s.
- **Missing data:** the description lists EMG and accelerometer signals, but the files hold neither, and no raw wide-band data.
- **Missing derived data:** no events, place-cell lists, PCC values or rigid/plastic labels are deposited, so the paper's selections can't be checked.
- **No code:** neither the paper nor the dandiset links analysis code.
- **Sparse metadata:** electrode location is "unknown" on every channel and subject age is "/".
- **Running direction:** on the circular track the animals ran toward decreasing linearized position, which the metadata doesn't say.
- **No duplicate recordings found.**

### 3. Where the protocol was unclear, wrong or missing something

1. **Chance-level rule.** It applies "when the paper states a chance level". The main text only says "significant". I read that as a 5% false-positive rate. My pre-registered PCC test has a 58% false-positive rate (a calibrated variant has 30%), so I blocked fig2b as methods_underspecified.
2. **Blocking dependents.** fig2d uses dPCC, not the significance test, but it lists fig2b in `depends_on`. I applied "a dependent of a blocked claim is blocked" literally.
3. **Main text open, supplement not.** The protocol only distinguishes full text from abstract. I used the main text, said so, and treated every Methods detail as a common choice fixed in advance.
4. **A pre-registered test can be confounded.** The pooled test hides a within-session effect (Simpson's paradox), and the protocol gives no guidance. I judged outcomes on the pooled test and showed the within-session test as a variant.
5. **Code bugs found after running claim analyses.** The protocol is silent on this. I had assumed the circular track was run in the increasing direction. I fixed it because the criterion says templates come from running, and the fix is recorded in the notebook.
6. **Some criteria define no partial outcome.** For rate-split-medians, where one of two values falls in tolerance, I used the protocol's general definition of partially reproduced.
7. **Unreadable figures.** I couldn't see the figure images, and the text doesn't state Fig. 1D's result, so I made no claim for it.
8. **Thresholds.** "Show how the result changes with a threshold" covers many choices here. I varied the place-cell peak and the PCC alpha and split, but not the ripple or burst thresholds.

### 4. Runtime and failures

- **Notebook:** about 8.3 minutes from a clean environment (498 s), on 4 processes. About 2 minutes of that is streaming one LFP channel per session.
- **Failed downloads:** the supplement PDF and figure images, from PMC, Europe PMC and Science.
- **First draft:** took 18 minutes and had the circular-direction bug; both are fixed and re-run.
- **Untracked items:** `git status` lists dotfiles and `scripts` that I didn't create. They are sandbox `/dev/null` mounts; I left them alone.

## End of run

70 turns, 99 minutes, result: success.
