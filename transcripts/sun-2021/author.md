# 001878 · author · run 39216993021

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls; ls entries claims attempts tools
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

[... 533 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md docs/design.md | head -400
```

```
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

An outcome says what one attempt could recover from the data in a dandiset,
with the methods available to it. **A "not reproduced" or "partially
reproduced" outcome is not a finding that the paper is wrong.** It can come
[... 380 more lines not kept]
```

**Agent calls Bash**

```bash
ls -la entries/001453-fouke-2025 claims/001453; cat entries/001453-fouke-2025/entry.yaml entries/001453-fouke-2025/requirements.in; cat claims/001453/*.yaml; cat attempts/001453-fouke-2025-01.yaml
```

```
<persisted-output>
Output too large (48.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/9a1084b9-1c21-4d8e-b8d5-de1f52858937/tool-results/bs6812jt6.txt

Preview (first 2KB):
claims/001453:
total 24
drwxr-xr-x  2 runner runner  4096 Oct 19 07:35 .
drwxr-xr-x 54 runner runner  4096 Oct 19 07:35 ..
-rw-r--r--  1 runner runner 12471 Oct 19 07:35 10.1016-j.cub.2025.04.027.yaml

entries/001453-fouke-2025:
total 124
drwxr-xr-x  2 runner runner  4096 Oct 19 07:35 .
drwxr-xr-x 54 runner runner  4096 Oct 19 07:35 ..
-rw-r--r--  1 runner runner  2158 Oct 19 07:35 README.md
-rw-r--r--  1 runner runner   914 Oct 19 07:35 entry.yaml
-rw-r--r--  1 runner runner 16218 Oct 19 07:35 omr.py
-rw-r--r--  1 runner runner 79403 Oct 19 07:35 reproduce_fouke_2025.ipynb
-rw-r--r--  1 runner runner    61 Oct 19 07:35 requirements.in
-rw-r--r--  1 runner runner  5989 Oct 19 07:35 requirements.lock.txt
[... 35 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/9a1084b9-1c21-4d8e-b8d5-de1f52858937/tool-results/bs6812jt6.txt"
}
```

```
1	claims/001453:
2	total 24
3	drwxr-xr-x  2 runner runner  4096 Oct 19 07:35 .
4	drwxr-xr-x 54 runner runner  4096 Oct 19 07:35 ..
5	-rw-r--r--  1 runner runner 12471 Oct 19 07:35 10.1016-j.cub.2025.04.027.yaml
6	
7	entries/001453-fouke-2025:
8	total 124
9	drwxr-xr-x  2 runner runner  4096 Oct 19 07:35 .
10	drwxr-xr-x 54 runner runner  4096 Oct 19 07:35 ..
11	-rw-r--r--  1 runner runner  2158 Oct 19 07:35 README.md
12	-rw-r--r--  1 runner runner   914 Oct 19 07:35 entry.yaml
13	-rw-r--r--  1 runner runner 16218 Oct 19 07:35 omr.py
14	-rw-r--r--  1 runner runner 79403 Oct 19 07:35 reproduce_fouke_2025.ipynb
15	-rw-r--r--  1 runner runner    61 Oct 19 07:35 requirements.in
16	-rw-r--r--  1 runner runner  5989 Oct 19 07:35 requirements.lock.txt
17	schema_version: 1
18	name: 001453-fouke-2025
19	type: reproduction
20	title: Optomotor swimming of zebrafish and Danionella cerebrum (Fouke et al. 2025)
[... 849 more lines not kept]
```

**Agent calls Bash**

```bash
cat entries/001453-fouke-2025/README.md; python -c "
import nbformat
nb=nbformat.read('entries/001453-fouke-2025/reproduce_fouke_2025.ipynb',4)
for i,c in enumerate(nb.cells[:8]):
    print('----',i,c.cell_type,c.metadata.get('tags'))
    print(c.source[:2500])
print(len(nb.cells))
for i,c in enumerate(nb.cells): print(i,c.cell_type,c.metadata.get('tags'),c.source[:80].replace('\n',' '))
"
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
[... 238 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l tools/entry.py; grep -n "def \|error(\|fail(" tools/entry.py | head -120; ls schemas
```

```
396 tools/entry.py
68:    def __init__(self):
71:    def error(self, where, message: str) -> None:
75:def schema(name: str) -> Draft202012Validator:
79:def load(report: Report, path: Path):
84:        report.error(path.relative_to(ROOT), f"not valid YAML: {e}")
88:def validate(report: Report, path: Path, schema_name: str) -> dict | None:
94:        report.error(path.relative_to(ROOT), f"{where}: {err.message}")
98:def _plain(value):
109:def code_of(notebook_path: Path) -> str:
116:def check(entry_dir: Path) -> Report:
123:        report.error(rel / "entry.yaml", f"name {entry.get('name')!r} must match the directory name")
128:        report.error(rel / name, "notebook is not listed in entry.yaml")
130:        report.error(rel / "entry.yaml", f"listed notebook {name!r} does not exist")
134:            report.error(rel / "entry.yaml", f"listed helper {name!r} does not exist")
138:        report.error(rel, "no requirements.in")
140:        report.error(rel, "no requirements.lock.txt; run `tools/entry.py lock`")
147:                report.error(rel / "requirements.lock.txt", f"{name} is required but not locked; re-run lock")
155:            report.error(rel / "entry.yaml", "an orientation or reproduction entry must relate to a dandiset")
158:                report.error(rel / "entry.yaml", f"pin the version of dandiset {d}, as dandi:{d}/<version>")
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,66p tools/entry.py; sed -n 260,396p tools/entry.py
```

```
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
- each notebook, or a helper it imports, names the dandiset the entry uses;
- each notebook has a cell tagged `sanity` that prints what was loaded;
[... 183 more lines not kept]
```

**Agent**

Now the dandiset metadata.

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/001878/ | python -m json.tool; curl -s "https://api.dandiarchive.org/api/dandisets/001878/versions/" | python -m json.tool
```

Result: the fetched text is not kept.

**Agent**

No published version exists; only a draft (modified 2026-06-25). Let me see its metadata and files.

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/001878/versions/draft/ | python -m json.tool; curl -s "https://api.dandiarchive.org/api/dandisets/001878/versions/draft/assets/?page_size=100" | python -m json.tool
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
sed -n 116,258p tools/entry.py; python -m json.tool schemas/attempt.schema.json | head -150
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

[... 274 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p paper; curl -sL -H "Accept: application/vnd.citationstyles.csl+json" https://doi.org/10.22002/d1.1991 | head -c 4000; echo; curl -sL "https://data.caltech.edu/api/records?q=doi:%2210.22002/D1.1991%22" | head -c 3000
```

Result: the fetched text is not kept.

**Agent**

The target DOI is a CaltechDATA dataset record, not a paper. The paper describing it is Sun et al. 2021 (arXiv 2104.02710, NeurIPS Datasets and Benchmarks), which is open access. I'll fetch it.

**Agent calls Bash**

```bash
cd paper && curl -sL -o sun2021.pdf https://arxiv.org/pdf/2104.02710 && file sun2021.pdf && (pdftotext -layout sun2021.pdf sun2021.txt 2>&1 || python -c "print('no pdftotext')"); ls -la; curl -sL "https://export.arxiv.org/api/query?id_list=2104.02710" | grep -E "<title>|<updated>|<arxiv:journal_ref|<arxiv:comment|version" | head
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  && pip list 2>/dev/null | grep -iE "pypdf|pdfminer|fitz|pymupdf|pynwb|h5py|remfile|dandi|numpy|pandas|sklearn|scikit"
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  && uv venv -q $TMPDIR/wk && uv pip install -q --python $TMPDIR/wk/bin/python pypdf pynwb h5py remfile dandi numpy pandas scipy scikit-learn ndx-pose 2>&1 | tail -3; $TMPDIR/wk/bin/python -c "
import pypdf
r=pypdf.PdfReader('paper/sun2021.pdf'); print(len(r.pages))
open('paper/sun2021.txt','w').write('\n\n=====PAGE=====\n'.join(p.extract_text() for p in r.pages))
"; wc paper/sun2021.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/sun2021.txt",
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/sun2021.txt",
 "offset": 880,
 "limit": 900
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Now let me open the CalMS21 file in the dandiset and list everything in it.

**Agent calls Bash**

```bash
cd $TMPDIR && cat > insp.py <<'EOF'
import h5py, remfile, requests, sys
aid = sys.argv[1]
url = requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/", allow_redirects=True).url
f = h5py.File(remfile.File(url), "r")
def show(name, obj):
    if isinstance(obj, h5py.Dataset):
        v = ""
        if obj.size < 20 or obj.dtype.kind in "SOU" and obj.size < 60:
            try: v = obj[()]
            except Exception as e: v = e
        print(f"D {name} {obj.shape} {obj.dtype} {dict(obj.attrs)} {v}")
    else:
        print(f"G {name} {dict(obj.attrs)}")
f.visititems(show)
EOF
$TMPDIR/wk/bin/python insp.py 667350e9-70cd-4201-95c5-cdf318d79de4 2>&1 | grep -v "^G specifications\|^D specifications" | head -300
```

```
G acquisition {}
G acquisition/behavior_video {'comments': 'no comments', 'description': 'CalMS21 resident-intruder social behavior (mouse071).', 'namespace': 'core', 'neurodata_type': 'ImageSeries', 'object_id': '304bc772-9d15-41a5-80bd-bc57dcd5c9b9'}
D acquisition/behavior_video/data (0, 0, 0) uint8 {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'Frames'} []
D acquisition/behavior_video/external_file (1,) object {'starting_frame': array([0])} [b'sub-mouse071-resident-intruder_ses-mouse071-task1_image/304bc772-9d15-41a5-80bd-bc57dcd5c9b9_external_file_0.mp4']
D acquisition/behavior_video/format () object {} b'external'
D acquisition/behavior_video/starting_time () float64 {'rate': np.float64(30.0), 'unit': 'seconds'} 0.0
G analysis {}
D file_create_date (1,) object {} [b'2026-06-24T20:05:42.384387-06:00']
G general {}
G general/devices {}
G general/devices/behavior_video Camera Device {'description': 'Video camera used for recording.', 'namespace': 'core', 'neurodata_type': 'Device', 'object_id': '0db756aa-6654-4094-a651-f7ca42ecbaca'}
D general/experiment_description () object {} b'Resident-intruder social interaction; expert human annotation of social behaviors (CalMS21), derived to ethogram bouts.'
D general/experimenter (4,) object {} [b'Sun, Jennifer J.' b'Karigo, Tomomi' b'Anderson, David J.'
 b'Perona, Pietro']
D general/institution () object {} b'California Institute of Technology'
D general/keywords (6,) object {} [b'behavior' b'ethogram' b'social behavior' b'manual annotation'
 b'CalMS21' b'ndx-ethogram']
D general/lab () object {} b'Anderson Lab'
D general/related_publications (1,) object {} [b'https://doi.org/10.22002/D1.1991']
D general/session_id () object {} b'mouse071_task1'
[... 126 more lines not kept]
```

**Agent calls Bash**

```bash
curl -sL https://data.caltech.edu/api/records/1991 | python -c "import json,sys; d=json.load(sys.stdin); print(json.dumps({k:d[k] for k in d if k not in ('metadata',)},indent=1)[:3000])"; curl -sL https://data.caltech.edu/api/records/1991/files | python -c "
import json,sys; d=json.load(sys.stdin)
for e in d.get('entries',[]): print(e['key'], e['size'], e.get('checksum'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -sIL https://data.caltech.edu/records/1991 | grep -iE "^location|^HTTP"; curl -sL "https://data.caltech.edu/api/records?q=CalMS21" | python -c "
import json,sys; d=json.load(sys.stdin)
for h in d['hits']['hits']: print(h['id'], h['metadata']['title'], h.get('pids'), h['metadata'].get('publication_date'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -sL https://data.caltech.edu/api/records/s0vdx-0k302/files | python -c "
import json,sys; d=json.load(sys.stdin)
for e in d.get('entries',[]): print(e['key'], e['size'], e.get('checksum'))"; curl -sL https://data.caltech.edu/api/records/s0vdx-0k302 | python -c "import json,sys; d=json.load(sys.stdin); m=d['metadata']; print(m.get('version'), d.get('updated')); print(m.get('description','')[:3000])"
```

Result: the fetched text is not kept.

**Agent**

The full Task 1 pose and annotation set (457 MB zip) is public on CaltechDATA. Let me read its readme and the zip's member list via range requests.

**Agent calls Bash**

```bash
cd $TMPDIR && curl -sL https://data.caltech.edu/records/s0vdx-0k302/files/readme.md?download=1 -o readme.md; head -c 11000 readme.md; curl -sL "https://data.caltech.edu/records/s0vdx-0k302/files/calms21_convert_to_npy.py?download=1" | head -120
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && $TMPDIR/wk/bin/python -c "
import remfile, zipfile, requests, time
u='https://data.caltech.edu/records/s0vdx-0k302/files/task1_classic_classification.zip?download=1'
r=requests.head(u,allow_redirects=True); print(r.url[:120], r.headers.get('content-length'), r.headers.get('accept-ranges'))
t=time.time()
z=zipfile.ZipFile(remfile.File(r.url))
for i in z.infolist(): print(i.filename, i.file_size, i.compress_size, i.compress_type)
print(time.time()-t)
"
```

```
https://caltech2.osn.mghpcc.org/caltechdata/06/7f/f1dd-1ef3-4a0f-8ab2-6b1d0d211b8e/data?response-content-type=applicatio 217 bytes
task1_classic_classification/ 0 0 0
task1_classic_classification/taskprog_features_task1_train.json 685378203 164867714 8
task1_classic_classification/calms21_task1_test.json 632160323 70398599 8
task1_classic_classification/taskprog_features_task1_test.json 354031913 85168513 8
task1_classic_classification/calms21_task1_train.json 1224936223 136921944 8
0.2418508529663086
Shell cwd was reset to
```

**Agent**

Range requests work, so single members can be streamed. Let me find which sequence keys exist and where mouse071 sits.

**Agent calls Bash**

```bash
cd $TMPDIR && time $TMPDIR/wk/bin/python -c "
import remfile, zipfile, requests, re
u='https://data.caltech.edu/records/s0vdx-0k302/files/task1_classic_classification.zip?download=1'
url=requests.head(u,allow_redirects=True).url
z=zipfile.ZipFile(remfile.File(url))
for name in ['calms21_task1_test.json','calms21_task1_train.json']:
    keys=[]; n=0
    with z.open('task1_classic_classification/'+name) as f:
        tail=b''
        while True:
            b=f.read(1<<24)
            if not b: break
            s=tail+b
            keys+= re.findall(rb'\"(task1/[^\"]+)\"', s)
            tail=s[-200:]
            n+=len(b)
    ks=sorted(set(keys)); print(name, n, len(ks)); print([k.decode() for k in ks])
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 8, in <module>
    with z.open('task1_classic_classification/'+name) as f:
         ~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/zipfile/__init__.py", line 1695, in open
    zef_file = _SharedFile(self.fp, zinfo.header_offset,
                           self._fpclose, self._lock, lambda: self._writing)
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/zipfile/__init__.py", line 839, in __init__
    self.seekable = file.seekable
                    ^^^^^^^^^^^^^
AttributeError: 'RemFile' object has no attribute 'seekable'

real	0m0.724s
user	0m0.181s
sys	0m0.013s
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > zs.py <<'EOF'
import requests, struct, zlib, zipfile, io
U='https://data.caltech.edu/records/s0vdx-0k302/files/task1_classic_classification.zip?download=1'
class HTTPRange(io.RawIOBase):
    def __init__(s,url): s.url=url; s.pos=0; s.size=int(requests.head(url).headers['content-length']) if False else None
    def seekable(s): return True
    def readable(s): return True
    def tell(s): return s.pos
    def seek(s,o,w=0):
        if w==0: s.pos=o
        elif w==1: s.pos+=o
        else:
            if s.size is None:
                r=requests.get(s.url,headers={'Range':'bytes=0-0'}); s.size=int(r.headers['content-range'].split('/')[1])
            s.pos=s.size+o
        return s.pos
    def read(s,n=-1):
        if n is None or n<0: n=(s.size or 0)-s.pos
        if n==0: return b''
        r=requests.get(s.url,headers={'Range':f'bytes={s.pos}-{s.pos+n-1}'}); b=r.content; s.pos+=len(b); return b
def members():
    url=requests.head(U,allow_redirects=True).url
    return url, zipfile.ZipFile(HTTPRange(url))
def stream(url, zi, chunk=1<<22):
    h=requests.get(url,headers={'Range':f'bytes={zi.header_offset}-{zi.header_offset+29}'}).content
    nl,el=struct.unpack('<HH',h[26:30]); start=zi.header_offset+30+nl+el
    d=zlib.decompressobj(-15)
    with requests.get(url,headers={'Range':f'bytes={start}-{start+zi.compress_size-1}'},stream=True) as r:
        for b in r.iter_content(chunk):
            yield d.decompress(b)
    yield d.flush()
EOF
time $TMPDIR/wk/bin/python -c "
import re, zs
url,z=zs.members()
for name in ['calms21_task1_test.json','calms21_task1_train.json']:
    zi=z.getinfo('task1_classic_classification/'+name)
    keys=[]; n=0; tail=b''
    for b in zs.stream(url,zi):
        s=tail+b; keys+=re.findall(rb'\"(task1/[^\"]+)\"', s); tail=s[-200:]; n+=len(b)
    ks=sorted(set(keys)); print(name, n, len(ks)); print([k.decode().split('/')[-1] for k in ks])
"
```

```
calms21_task1_test.json 632160323 19
['mouse071_task1_annotator1', 'mouse072_task1_annotator1', 'mouse073_task1_annotator1', 'mouse074_task1_annotator1', 'mouse075_task1_annotator1', 'mouse076_task1_annotator1', 'mouse077_task1_annotator1', 'mouse078_task1_annotator1', 'mouse079_task1_annotator1', 'mouse080_task1_annotator1', 'mouse081_task1_annotator1', 'mouse082_task1_annotator1', 'mouse083_task1_annotator1', 'mouse084_task1_annotator1', 'mouse085_task1_annotator1', 'mouse086_task1_annotator1', 'mouse087_task1_annotator1', 'mouse088_task1_annotator1', 'mouse089_task1_annotator1']
calms21_task1_train.json 1224936223 70
['mouse001_task1_annotator1', 'mouse002_task1_annotator1', 'mouse003_task1_annotator1', 'mouse004_task1_annotator1', 'mouse005_task1_annotator1', 'mouse006_task1_annotator1', 'mouse007_task1_annotator1', 'mouse008_task1_annotator1', 'mouse009_task1_annotator1', 'mouse010_task1_annotator1', 'mouse011_task1_annotator1', 'mouse012_task1_annotator1', 'mouse013_task1_annotator1', 'mouse014_task1_annotator1', 'mouse015_task1_annotator1', 'mouse016_task1_annotator1', 'mouse017_task1_annotator1', 'mouse018_task1_annotator1', 'mouse019_task1_annotator1', 'mouse020_task1_annotator1', 'mouse021_task1_annotator1', 'mouse022_task1_annotator1', 'mouse023_task1_annotator1', 'mouse024_task1_annotator1', 'mouse025_task1_annotator1', 'mouse026_task1_annotator1', 'mouse027_task1_annotator1', 'mouse028_task1_annotator1', 'mouse029_task1_annotator1', 'mouse030_task1_annotator1', 'mouse031_task1_annotator1', 'mouse032_task1_annotator1', 'mouse033_task1_annotator1', 'mouse034_task1_annotator1', 'mouse035_task1_annotator1', 'mouse036_task1_annotator1', 'mouse037_task1_annotator1', 'mouse038_task1_annotator1', 'mouse039_task1_annotator1', 'mouse040_task1_annotator1', 'mouse041_task1_annotator1', 'mouse042_task1_annotator1', 'mouse043_task1_annotator1', 'mouse044_task1_annotator1', 'mouse045_task1_annotator1', 'mouse046_task1_annotator1', 'mouse047_task1_annotator1', 'mouse04
[... 5 more lines not kept]
```

**Agent**

mouse071 is the first of the 19 Task 1 test sequences. Next, step 5: the code the paper links to (the MABe baselines on AIcrowd GitLab).

**Agent calls Bash**

```bash
curl -s -m 20 "https://gitlab.aicrowd.com/api/v4/projects/aicrowd%2Fresearch%2Fmab-e%2Fmab-e-baselines" | head -c 1500; echo; curl -s -m 20 "https://gitlab.aicrowd.com/api/v4/projects/aicrowd%2Fresearch%2Fmab-e%2Fmab-e-baselines/repository/commits?per_page=3" | head -c 1500
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -sv -m 20 -o /dev/null https://gitlab.aicrowd.com/aicrowd/research/mab-e/mab-e-baselines 2>&1 | grep -E "^< HTTP|Could not|resolve|timed|Connected" | head; curl -s "https://api.github.com/search/repositories?q=mab-e-baselines" | python -c "import json,sys; d=json.load(sys.stdin); [print(r['full_name'], r['html_url'], r['pushed_at']) for r in d.get('items',[])]"; curl -s "https://api.github.com/repos/neuroethology/TREBA/commits?per_page=1" | python -c "import json,sys; d=json.load(sys.stdin); print(d[0]['sha'], d[0]['commit']['committer']['date'])"
```

Result: the fetched text is not kept.

**Agent**

The AIcrowd GitLab timed out. That may be the sandbox's network filter, so I'll retry once outside it.

**Agent calls Bash**

```bash
curl -s -m 30 -o /dev/null -w "%{http_code}\n" https://gitlab.aicrowd.com/aicrowd/research/mab-e/mab-e-baselines; curl -s -m 30 -o /dev/null -w "%{http_code}\n" https://gitlab.aicrowd.com/
```

Result: the fetched text is not kept.

**Agent**

Unreachable outside the sandbox too. Let me check for an archived copy (Software Heritage, web archive).

**Agent calls Bash**

```bash
curl -s -m 30 "https://archive.softwareheritage.org/api/1/origin/https://gitlab.aicrowd.com/aicrowd/research/mab-e/mab-e-baselines/get/" | head -c 600; echo; curl -s -m 30 "https://archive.softwareheritage.org/api/1/origin/search/mab-e-baselines/?limit=10" | head -c 1500; echo; curl -s -m 30 "http://archive.org/wayback/available?url=gitlab.aicrowd.com/aicrowd/research/mab-e/mab-e-baselines" | head -c 600
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && $TMPDIR/wk/bin/python -c "
import zs, requests, zipfile
U='https://data.caltech.edu/records/s0vdx-0k302/files/task1_videos_mp4.zip?download=1'
url=requests.head(U,allow_redirects=True).url
z=zipfile.ZipFile(zs.HTTPRange(url))
L=z.infolist(); print(len(L))
for i in L:
    if '071' in i.filename or len(L)<12: print(i.filename,i.file_size,i.compress_size,hex(i.CRC),i.compress_type)
print([i.filename for i in L[:8]])
"
```

```
92
task1_videos_mp4/test/mouse071_task1_annotator1.mp4 964451532 921968852 0x365042f1 8
['task1_videos_mp4/', 'task1_videos_mp4/test/', 'task1_videos_mp4/test/mouse078_task1_annotator1.mp4', 'task1_videos_mp4/test/mouse087_task1_annotator1.mp4', 'task1_videos_mp4/test/mouse083_task1_annotator1.mp4', 'task1_videos_mp4/test/mouse074_task1_annotator1.mp4', 'task1_videos_mp4/test/mouse089_task1_annotator1.mp4', 'task1_videos_mp4/test/mouse081_task1_annotator1.mp4']
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv pip install -q --python $TMPDIR/wk/bin/python av 2>&1|tail -1; time $TMPDIR/wk/bin/python -c "
import av, requests, time, numpy as np
aid='4433fa7b-5149-445e-9c4e-fcb6eef8f05f'
url=requests.head(f'https://api.dandiarchive.org/api/assets/{aid}/download/',allow_redirects=True).url
c=av.open(url); s=c.streams.video[0]
print(s.frames, s.average_rate, s.codec_context.width, s.codec_context.height, s.duration, s.time_base, c.duration, s.codec_context.name)
s.thread_type='AUTO'
t=time.time(); n=0; prev=None; e=[]
for fr in c.decode(s):
    a=fr.to_ndarray(format='gray')[::4,::4].astype(np.int16)
    if prev is not None: e.append(np.abs(a-prev).mean())
    prev=a; n+=1
    if n==3000: break
print(n, time.time()-t, fr.pts, fr.time)
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 5, in <module>
    c=av.open(url); s=c.streams.video[0]
  File "av/container/core.py", line 564, in av.container.core.open
    return InputContainer(
    ^^^
  File "av/container/core.py", line 336, in av.container.core.Container.__cinit__
    self.err_check(res)
    
  File "av/container/core.py", line 361, in av.container.core.Container.err_check
    return err_check(value, filename=self.name)
    ^^^
  File "av/error.py", line 354, in av.error.err_check
    raise cls(code, message, filename, log)
    ^^^
av.error.OSError: [Errno 5] Input/output error: 'https://dandiarchive.s3.amazonaws.com/blobs/737/81d/73781d39-da5a-41c9-9f25-9e009ca260d1?response-content-disposition=attachment%3B%20filename%3D%22304bc772-9d15-41a5-80bd-bc57dcd5c9b9_external_file_0.mp4%22&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=[removed: an AWS key]%2F20261019%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Date=20261019T074229Z&X-Amz-Expires=21600&X-Amz-SignedHeaders=host&X-Amz-Signature=01731ef0e3ba0219bfe500433688003bd49aca030eb49ff9fafbaec530f16717'

real	0m1.007s
user	0m0.560s
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && time $TMPDIR/wk/bin/python -c "
import av, requests, time, numpy as np, remfile
aid='4433fa7b-5149-445e-9c4e-fcb6eef8f05f'
url=requests.head(f'https://api.dandiarchive.org/api/assets/{aid}/download/',allow_redirects=True).url
c=av.open(remfile.File(url)); s=c.streams.video[0]
print(s.frames, s.average_rate, s.codec_context.width, s.codec_context.height, s.duration, s.time_base, c.duration, s.codec_context.name)
s.thread_type='AUTO'
t=time.time(); n=0; prev=None; e=[]
for fr in c.decode(s):
    a=fr.to_ndarray(format='gray')[::4,::4].astype(np.int16)
    if prev is not None: e.append(np.abs(a-prev).mean())
    prev=a; n+=1
    if n==3000: break
print(n, time.time()-t, fr.pts, fr.time)
"
```

```
23810 30/1 1024 570 12190720 1/15360 793666667 h264
3000 4.096182346343994 1535488 99.96666666666667

real	0m5.892s
user	0m8.636s
sys	0m0.341s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && $TMPDIR/wk/bin/python -c "
import zs, requests, zipfile
for n in ['task2_annotation_styles.zip','task3_new_behaviors.zip','unlabeled_videos.zip']:
    U=f'https://data.caltech.edu/records/s0vdx-0k302/files/{n}?download=1'
    url=requests.head(U,allow_redirects=True).url
    z=zipfile.ZipFile(zs.HTTPRange(url))
    for i in z.infolist(): print(n, i.filename,i.file_size,i.compress_size)
"
```

```
task2_annotation_styles.zip task2_annotation_styles/ 0 0
task2_annotation_styles.zip task2_annotation_styles/taskprog_features_task2_test.json 1290138014 310274538
task2_annotation_styles.zip task2_annotation_styles/calms21_task2_train.json 1405759133 156255669
task2_annotation_styles.zip task2_annotation_styles/taskprog_features_task2_train.json 787487086 189523975
task2_annotation_styles.zip task2_annotation_styles/calms21_task2_test.json 2302454965 256037535
task3_new_behaviors.zip task3_new_behaviors/ 0 0
task3_new_behaviors.zip task3_new_behaviors/taskprog_features_task3_test.json 962507840 231584408
task3_new_behaviors.zip task3_new_behaviors/calms21_task3_train.json 537970053 59864875
task3_new_behaviors.zip task3_new_behaviors/taskprog_features_task3_train.json 301038484 72346569
task3_new_behaviors.zip task3_new_behaviors/calms21_task3_test.json 1720486180 192373221
unlabeled_videos.zip unlabeled_videos/ 0 0
unlabeled_videos.zip unlabeled_videos/calms21_unlabeled_videos_part3.json 3041018734 340969423
unlabeled_videos.zip unlabeled_videos/taskprog_features_unlabeled_videos_part1.json 2252339317 541961333
unlabeled_videos.zip unlabeled_videos/calms21_unlabeled_videos_part1.json 3985907694 446939981
unlabeled_videos.zip unlabeled_videos/taskprog_features_unlabeled_videos_part3.json 1718658575 413485445
unlabeled_videos.zip unlabeled_videos/calms21_unlabeled_videos_part4.json 4070966397 457187677
unlabeled_videos.zip unlabeled_videos/taskprog_features_unlabeled_videos_part2.json 1767594351 425441965
unlabeled_videos.zip unlabeled_videos/calms21_unlabeled_videos_part2.json 3129025790 351124664
unlabeled_videos.zip unlabeled_videos/taskprog_features_unlabeled_videos_part4.json 2300466097 553624568
Shell cwd was reset to
```

**Agent calls Bash**

```bash
mkdir -p entries/001878-sun-2021; curl -s "https://api.dandiarchive.org/api/dandisets/001878/versions/draft/assets/?page_size=100&metadata=1" | python -c "
import json,sys; d=json.load(sys.stdin)
for a in d['results']: print(a['path'], a['blob'], a['size'])"; curl -s "https://api.dandiarchive.org/api/assets/667350e9-70cd-4201-95c5-cdf318d79de4/" | python -m json.tool | head -80
```

Result: the fetched text is not kept.

**Agent calls Write**

```json
{
 "file_path": "entries/001878-sun-2021/calms21.py",
 "content": "\"\"\"Loading CalMS21 (Sun et al. 2021) from dandiset 001878 and from its CaltechDATA deposit.\n\nDandiset 001878 has no published version. The entry reads the draft and pins it by the blob id of\neach asset it uses: if an asset changes, `asset_url` raises, so that a changed draft cannot pass\nunnoticed. The draft's modification time when the entry was written is DRAFT_MODIFIED.\n\nThe dandiset holds one CalMS21 sequence, Task 1 test sequence mouse071, as an NWB file with MARS\npose (ndx-pose), the frame annotations as bouts (ndx-ethogram), two per-frame series the converter\nderived from the pose, and the source video as an external mp4.\n\nThe paper's full dataset is on CaltechDATA (doi:10.22002/D1.1991, record s0vdx-0k302, version\n1.0), as zip files of JSON. `caltech_sequences` streams one JSON member of a zip with HTTP range\nrequests and yields its sequences one at a time, without writing anything to disk.\n\nParameters and conventions:\n- Keypoint order (nose, left ear, right ear, neck, left hip, right hip, tail base), mouse 0 the\n  resident and mouse 1 the intruder, image size 1024 x 570, 30 Hz, and the Task 1 vocabulary\n  {attack: 0, investigation: 1, mount: 2, other: 3}: the paper's Appendix C and D.\n- Array layout of keypoints (frames, mouse, x/y, body part): the paper's Appendix C and the\n  CaltechDATA readme.\n- A frame's label from the bouts: the bout whose [start, stop) holds the frame's time, with times\n  taken at frame index / 30. This is a choice made here; the NWB file does not say whether\n  stop_time is inclusive.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport io\nimport json\nimport re\nimport struct\nimport zipfile\nimport zlib\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nimport requests\n\nDANDISET_ID = \"001878\"\nDANDISET_VERSION = \"draft\"\nDRAFT_MODIFIED = \"2026-06-25T18:32:10.096594Z\"\nAPI = \"https://api.dandiarchive.org/api\"\n\nCALMS21_NWB = \"sub-mouse071-resident-intruder/sub-mouse071-resident-intruder_ses-mouse071-task1_image.nwb\"\nCALMS21_MP4 = (\"sub-mouse071-resident-intruder/sub-mouse071-resident-intruder_ses-mouse071-task1_image/\"\n               \"304bc772-9d15-41a5-80bd-bc57dcd5c9b9_external_file_0.mp4\")\nBLOBS = {  # blob id of each asset of the draft when the entry was written\n    CALMS21_NWB: \"e169899a-5a31-44d1-aa7a-93c33e5d3e73\",\n    CALMS21_MP4: \"73781d39-da5a-41c9-9f25-9e009ca260d1\",\n}\n\nPARTS = [\"nose\", \"ear_left\", \"ear_right\", \"neck\", \"hip_left\", \"hip_right\", \"tail_base\"]\nMICE = [\"resident\", \"intruder\"]\nRATE = 30.0\nIMAGE_W, IMAGE_H = 1024, 570\nTASK1_VOCAB = {\"attack\": 0, \"investigation\": 1, \"mount\": 2, \"other\": 3}\n\nCALTECH_RECORD = \"s0vdx-0k302\"\nCALTECH_DOI = \"10.22002/D1.1991\"\n\n\n# --- dandiset -----------------------------------------------------------------\n\ndef draft_info() -> dict:\n    \"\"\"The draft's metadata summary: modification time and asset count.\"\"\"\n    r = requests.get(f\"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/info/\", timeout=60)\n    r.raise_for_status()\n    return r.json()\n\n\ndef list_assets() -> pd.DataFrame:\n    r = requests.get(f\"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/\",\n                     params={\"page_size\": 200}, timeout=60)\n    r.raise_for_status()\n    return pd.DataFrame(r.json()[\"results\"])[[\"path\", \"size\", \"blob\", \"asset_id\", \"modified\"]]\n\n\ndef asset_url(path: str) -> str:\n    \"\"\"Download URL of an asset of the draft, after checking its blob is the one pinned here.\"\"\"\n    r = requests.get(f\"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/\",\n                     params={\"path\": path, \"page_size\": 10}, timeout=60)\n    r.raise_for_status()\n    hits = [a for a in r.json()[\"results\"] if a[\"path\"] == path]\n    if len(hits) != 1:\n        raise RuntimeError(f\"asset {path} not found in dandiset {DANDISET_ID} {DANDISET_VERSION}\")\n    if path in BLOBS and hits[0][\"blob\"] != BLOBS[path]:\n        raise RuntimeError(f\"asset {path} has changed (blob {hits[0]['blob']}, pinned {BLOBS[path]})\")\n    return requests.head(f\"{API}/assets/{hits[0]['asset_id']}/download/\", allow_redirects=True,\n                         timeout=60).url\n\n\ndef _text(x):\n    return x.decode() if isinstance(x, bytes) else str(x)\n\n\ndef load_session(path: str = CALMS21_NWB) -> dict:\n    \"\"\"Everything the analysis uses from the CalMS21 NWB file, as arrays.\n\n    keypoints: (frames, mouse, x/y, part), the CalMS21 layout; scores: (frames, mouse, part).\n    \"\"\"\n    f = h5py.File(remfile.File(asset_url(path)), \"r\")\n    beh = f[\"processing/behavior\"]\n    pe = beh[\"PoseEstimation\"]\n    series = {}\n    for m in MICE:\n        for p in PARTS:\n            g = pe[f\"{m}_{p}\"]\n            series[(m, p)] = {\n                \"data\": g[\"data\"][:], \"confidence\": g[\"confidence\"][:],\n                \"rate\": float(g[\"starting_time\"].attrs[\"rate\"]), \"start\": float(g[\"starting_time\"][()]),\n                \"unit\": g[\"data\"].attrs[\"unit\"], \"reference_frame\": _text(g[\"reference_frame\"][()])}\n    n = len(series[(\"resident\", \"nose\")][\"data\"])\n    kp = np.empty((n, 2, 2, 7))\n    sc = np.empty((n, 2, 7))\n    for i, m in enumerate(MICE):\n        for j, p in enumerate(PARTS):\n            kp[:, i, :, j] = series[(m, p)][\"data\"]\n            sc[:, i, j] = series[(m, p)][\"confidence\"]\n    b = beh[\"CalMS21\"]\n    bouts = pd.DataFrame({c: (b[c][:] if b[c].dtype.kind != \"O\" else [_text(v) for v in b[c][:]])\n                          for c in b.attrs[\"colnames\"]})\n    eth = beh[\"CalMS21_ethogram\"]\n    ethogram = pd.DataFrame({c: (eth[c][:] if eth[c].dtype.kind != \"O\" else [_text(v) for v in eth[c][:]])\n                             for c in eth.attrs[\"colnames\"]})\n    vid = f[\"acquisition/behavior_video\"]\n    out = {\n        \"keypoints\": kp, \"scores\": sc, \"n_frames\": n, \"series\": series,\n        \"pose_dimensions\": pe[\"dimensions\"][:].tolist(), \"pose_software\": _text(pe[\"source_software\"][()]),\n        \"skeleton_nodes\": [_text(v) for v in beh[\"Skeletons/two_mice/nodes\"][:]],\n        \"skeleton_edges\": beh[\"Skeletons/two_mice/edges\"][:].tolist(),\n        \"bouts\": bouts, \"ethogram\": ethogram, \"annotator\": _text(b.attrs.get(\"annotator\", \"\")),\n        \"bouts_description\": _text(b.attrs.get(\"description\", \"\")),\n        \"centroid_speed\": beh[\"centroid_speed/data\"][:],\n        \"centroid_speed_unit\": beh[\"centroid_speed/data\"].attrs[\"unit\"],\n        \"centroid_speed_rate\": float(beh[\"centroid_speed/starting_time\"].attrs[\"rate\"]),\n        \"interanimal_distance\": beh[\"interanimal_distance/data\"][:],\n        \"interanimal_distance_rate\": float(beh[\"interanimal_distance/starting_time\"].attrs[\"rate\"]),\n        \"video_rate\": float(vid[\"starting_time\"].attrs[\"rate\"]),\n        \"video_external_file\": [_text(v) for v in vid[\"external_file\"][:]],\n        \"session_id\": _text(f[\"general/session_id\"][()]),\n        \"identifier\": _text(f[\"identifier\"][()]),\n        \"session_start_time\": _text(f[\"session_start_time\"][()]),\n        \"related_publications\": [_text(v) for v in f[\"general/related_publications\"][:]],\n        \"subject\": {k: _text(f[f\"general/subject/{k}\"][()]) for k in f[\"general/subject\"].keys()},\n    }\n    f.close()\n    return out\n\n\ndef frame_labels(bouts: pd.DataFrame, n_frames: int, rate: float = RATE) -> np.ndarray:\n    \"\"\"Label name of each frame from the bouts table; '' where no bout covers the frame.\n\n    Raises if two bouts cover one frame.\n    \"\"\"\n    t = np.arange(n_frames) / rate\n    labels = np.full(n_frames, \"\", dtype=object)\n    covered = np.zeros(n_frames, int)\n    for start, stop, lab in zip(bouts.start_time, bouts.stop_time, bouts.label):\n        sel = (t >= start - 1e-9) & (t < stop - 1e-9)\n        labels[sel] = lab\n        covered += sel\n    if covered.max() > 1:\n        raise ValueError(\"bouts overlap\")\n    return labels\n\n\ndef centroids(kp: np.ndarray) -> np.ndarray:\n    \"\"\"Centroid of each mouse, the mean of its seven keypoints: (frames, mouse, x/y).\"\"\"\n    return kp.mean(axis=3)\n\n\ndef speed(xy: np.ndarray, rate: float = RATE) -> np.ndarray:\n    \"\"\"Speed (pixels/s) of a (frames, 2) trajectory; the first frame repeats the second.\"\"\"\n    v = np.hypot(*np.diff(xy, axis=0).T) * rate\n    return np.concatenate([v[:1], v])\n\n\ndef nose_to_intruder(kp: np.ndarray) -> np.ndarray:\n    \"\"\"Distance (pixels) from the resident's nose to the nearest intruder keypoint, per frame.\"\"\"\n    nose = kp[:, 0, :, 0][:, :, None]\n    return np.sqrt(((kp[:, 1] - nose) ** 2).sum(axis=1)).min(axis=1)\n\n\ndef block_bootstrap_diff(values: np.ndarray, group: np.ndarray, block: int, n_boot: int,\n                         rng: np.random.Generator, stat=np.median) -> tuple[float, float, float]:\n    \"\"\"Difference stat(values[group]) - stat(values[~group]) with a 95% CI from a moving-block\n    bootstrap over frames (contiguous blocks of `block` frames, resampled with replacement).\"\"\"\n    n = len(values)\n    obs = stat(values[group]) - stat(values[~group])\n    starts = np.arange(0, n - block + 1)\n    k = int(np.ceil(n / block))\n    diffs = []\n    for _ in range(n_boot):\n        s = rng.choice(starts, size=k, replace=True)\n        idx = (s[:, None] + np.arange(block)[None, :]).ravel()[:n]\n        g, v = group[idx], values[idx]\n        if g.all() or not g.any():\n            continue\n        diffs.append(stat(v[g]) - stat(v[~g]))\n    lo, hi = np.percentile(diffs, [2.5, 97.5])\n    return float(obs), float(lo), float(hi)\n\n\n# --- video --------------------------------------------------------------------\n\ndef video_frames(every: int = 1, step: int = 4):\n    \"\"\"Stream the source video of mouse071 and yield (frame index, gray image downsampled by `step`)\n    for every `every`-th frame. Every frame is decoded, so the indices are exact.\"\"\"\n    import av\n    container = av.open(remfile.File(asset_url(CALMS21_MP4)))\n    stream = container.streams.video[0]\n    stream.thread_type = \"AUTO\"\n    for i, frame in enumerate(container.decode(stream)):\n        if i % every == 0:\n            yield i, frame.to_ndarray(format=\"gray\")[::step, ::step]\n    container.close()\n\n\ndef video_info() -> dict:\n    import av\n    container = av.open(remfile.File(asset_url(CALMS21_MP4)))\n    s = container.streams.video[0]\n    info = {\"frames\": s.frames, \"rate\": float(s.average_rate), \"width\": s.codec_context.width,\n            \"height\": s.codec_context.height, \"codec\": s.codec_context.name,\n            \"duration_s\": float(s.duration * s.time_base) if s.duration else None}\n    container.close()\n    return info\n\n\n# --- CaltechDATA ----------------------------------------------------------------\n\ndef caltech_url(filename: str) -> str:\n    \"\"\"Direct (presigned) URL of a file of the CalMS21 record.\"\"\"\n    r = requests.head(f\"https://data.caltech.edu/records/{CALTECH_RECORD}/files/{filename}?download=1\",\n                      allow_redirects=True, timeout=60)\n    r.raise_for_status()\n    return r.url\n\n\ndef caltech_files() -> pd.DataFrame:\n    r = requests.get(f\"https://data.caltech.edu/api/records/{CALTECH_RECORD}/files\", timeout=60)\n    r.raise_for_status()\n    return pd.DataFrame([{\"file\": e[\"key\"], \"size\": e[\"size\"], \"checksum\": e[\"checksum\"]}\n                         for e in r.json()[\"entries\"]])\n\n\ndef caltech_record() -> dict:\n    r = requests.get(f\"https://data.caltech.edu/api/records/{CALTECH_RECORD}\", timeout=60)\n    r.raise_for_status()\n    d = r.json()\n    return {\"doi\": d[\"pids\"][\"doi\"][\"identifier\"], \"version\": d[\"metadata\"].get(\"version\"),\n            \"publication_date\": d[\"metadata\"].get(\"publication_date\"), \"updated\": d.get(\"updated\"),\n            \"rights\": [x.get(\"id\") or x.get(\"title\", {}).get(\"en\") for x in d[\"metadata\"].get(\"rights\", [])]}\n\n\nclass _HTTPRange(io.RawIOBase):\n    \"\"\"A read-only seekable file over HTTP range requests, enough for zipfile's central directory.\"\"\"\n\n    def __init__(self, url):\n        self.url, self.pos, self.size = url, 0, None\n\n    def seekable(self):\n        return True\n\n    def readable(self):\n        return True\n\n    def tell(self):\n        return self.pos\n\n    def seek(self, offset, whence=0):\n        if whence == 2 and self.size is None:\n            r = requests.get(self.url, headers={\"Range\": \"bytes=0-0\"}, timeout=60)\n            self.size = int(r.headers[\"content-range\"].split(\"/\")[1])\n        self.pos = {0: offset, 1: self.pos + offset, 2: (self.size or 0) + offset}[whence]\n        return self.pos\n\n    def read(self, n=-1):\n        if n is None or n < 0:\n            n = self.size - self.pos\n        if n == 0:\n            return b\"\"\n        r = requests.get(self.url, headers={\"Range\": f\"bytes={self.pos}-{self.pos + n - 1}\"}, timeout=120)\n        r.raise_for_status()\n        self.pos += len(r.content)\n        return r.content\n\n\ndef zip_members(zip_name: str) -> pd.DataFrame:\n    \"\"\"The members of a zip of the CalMS21 record, read from its central directory.\"\"\"\n    url = caltech_url(zip_name)\n    z = zipfile.ZipFile(_HTTPRange(url))\n    return pd.DataFrame([{\"member\": i.filename, \"size\": i.file_size, \"compressed\": i.compress_size,\n                          \"crc32\": i.CRC} for i in z.infolist()])\n\n\ndef _member_bytes(zip_name: str, member: str, chunk: int = 1 << 23):\n    \"\"\"Decompressed bytes of one deflated zip member, streamed in chunks.\"\"\"\n    url = caltech_url(zip_name)\n    zi = zipfile.ZipFile(_HTTPRange(url)).getinfo(member)\n    head = requests.get(url, headers={\"Range\": f\"bytes={zi.header_offset}-{zi.header_offset + 29}\"},\n                        timeout=60).content\n    name_len, extra_len = struct.unpack(\"<HH\", head[26:30])\n    start = zi.header_offset + 30 + name_len + extra_len\n    d = zlib.decompressobj(-15)\n    total, crc = 0, 0\n    with requests.get(url, headers={\"Range\": f\"bytes={start}-{start + zi.compress_size - 1}\"},\n                      stream=True, timeout=600) as r:\n        r.raise_for_status()\n        for b in r.iter_content(chunk):\n            out = d.decompress(b)\n            total += len(out)\n            crc = zlib.crc32(out, crc)\n            yield out\n    out = d.flush()\n    total += len(out)\n    crc = zlib.crc32(out, crc)\n    yield out\n    if total != zi.file_size or crc != zi.CRC:\n        raise RuntimeError(f\"{member}: decompressed {total} bytes with CRC {crc:#x}, \"\n                           f\"expected {zi.file_size} and {zi.CRC:#x}\")\n\n\nKEY = re.compile(rb'\"((?:task[123]|unlabeled_videos)/[^\"]+)\"\\s*:\\s*\\{')\n\n\ndef caltech_sequences(zip_name: str, member: str):\n    \"\"\"Yield (sequence key, raw JSON text of the sequence) for each sequence in a CalMS21 JSON member.\n\n    A sequence's text runs from its opening brace to the next sequence key; parse it with\n    `parse_sequence` (all fields) or `sequence_summary` (counts and annotations only, fast).\n    \"\"\"\n    buf = b\"\"\n    current = None  # (key, offset of its opening brace in buf)\n    for chunk in _member_bytes(zip_name, member):\n        buf += chunk\n        search_from = current[1] + 1 if current else 0\n        while True:\n            m = KEY.search(buf, search_from)\n            if not m:\n                break\n            if current is not None:\n                yield current[0], buf[current[1]:m.start()]\n            current = (m.group(1).decode(), m.end() - 1)\n            buf = buf[current[1]:]\n            current = (current[0], 0)\n            search_from = 1\n        if current is None:\n            buf = buf[-300:]\n    if current is not None:\n        yield current[0], buf[current[1]:]\n\n\ndef parse_sequence(text: bytes) -> dict:\n    obj, _ = json.JSONDecoder().raw_decode(text.decode())\n    return obj\n\n\ndef sequence_summary(text: bytes) -> dict:\n    \"\"\"Frame count, annotations and metadata of a sequence, without parsing its keypoints.\n\n    Frames are counted in the `scores` field, where each frame is [[7 scores], [7 scores]], so each\n    frame ends with one \"]]\" (the last frame's \"]]]\" holds one non-overlapping \"]]\").\n    \"\"\"\n    dec = json.JSONDecoder()\n    i = text.find(b'\"scores\"')\n    if i < 0:\n        raise ValueError(\"no scores field\")\n    j = text.find(b'\"annotations\"', i)\n    k = text.find(b'\"metadata\"', i)\n    ends = [x for x in (j, k) if x > 0]\n    scores_text = text[i:min(ends)] if ends else text[i:]\n    out = {\"n_frames\": scores_text.count(b\"]]\"), \"annotations\": None, \"metadata\": None,\n           \"keypoints_head\": text[:text.find(b'\"keypoints\"') + 4000] if b'\"keypoints\"' in text[:200] else None}\n    if j > 0:\n        a = text.index(b\"[\", j)\n        out[\"annotations\"] = np.array(dec.raw_decode(text[a:a + 20_000_000].decode(\"ascii\", \"ignore\"))[0])\n    if k > 0:\n        a = text.index(b\"{\", k)\n        out[\"metadata\"] = dec.raw_decode(text[a:a + 100_000].decode())[0]\n    kp = text.find(b'\"keypoints\"')\n    if kp >= 0:\n        out[\"keypoints_head\"] = text[kp:kp + 4000]\n    return out\n"
}
```

```
File created successfully at: entries/001878-sun-2021/calms21.py (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/001878-sun-2021/calms21.py",
 "old_string": "    out = {\"n_frames\": scores_text.count(b\"]]\"), \"annotations\": None, \"metadata\": None,\n           \"keypoints_head\": text[:text.find(b'\"keypoints\"') + 4000] if b'\"keypoints\"' in text[:200] else None}",
 "new_string": "    out = {\"n_frames\": scores_text.count(b\"]]\"), \"annotations\": None, \"metadata\": None,\n           \"keypoints_head\": None}"
}
```

```
The file entries/001878-sun-2021/calms21.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/001878-sun-2021 && time $TMPDIR/wk/bin/python -c "
import calms21 as c, numpy as np, json, time
t=time.time()
n=0
for key, text in c.caltech_sequences('task1_classic_classification.zip','task1_classic_classification/calms21_task1_test.json'):
    s=c.sequence_summary(text)
    if n<3 or key.endswith('mouse071_task1_annotator1'):
        full=c.parse_sequence(text)
        kp=np.array(full['keypoints']); sc=np.array(full['scores'])
        print(key, s['n_frames'], kp.shape, sc.shape, len(full['annotations']), full['metadata'], (s['annotations']==np.array(full['annotations'])).all())
    n+=1
print(n, time.time()-t)
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 5, in <module>
    for key, text in c.caltech_sequences('task1_classic_classification.zip','task1_classic_classification/calms21_task1_test.json'):
                     ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "entries/001878-sun-2021/calms21.py", line 337, in caltech_sequences
    for chunk in _member_bytes(zip_name, member):
                 ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "entries/001878-sun-2021/calms21.py", line 301, in _member_bytes
    url = caltech_url(zip_name)
  File "entries/001878-sun-2021/calms21.py", line 238, in caltech_url
    r.raise_for_status()
    ~~~~~~~~~~~~~~~~~~^^
  File "/tmp/claude-1001/wk/lib/python3.13/site-packages/requests/models.py", line 1167, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 403 Client Error: Forbidden for url: https://caltech2.osn.mghpcc.org/caltechdata/06/7f/f1dd-1ef3-4a0f-8ab2-6b1d0d211b8e/data?response-content-type=application%2Foctet-stream&response-content-disposition=attachment%3B%20filename%3Dtask1_classic_classification.zip&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=P8ERST8CRWUQEKBPZDRB%2F20261019%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261019T074509Z&X-Amz-Expires=60&X-Amz-SignedHeaders=host&X-Amz-Signature=e19fb808b7d1213f033b42cee8811fa2a0c312b293b36b1fd2491ea4bb49c687

real	0m1.745s
user	0m1.432s
sys	0m0.067s
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/001878-sun-2021/calms21.py",
 "old_string": "    \"\"\"Direct (presigned) URL of a file of the CalMS21 record.\"\"\"\n    r = requests.head(f\"https://data.caltech.edu/records/{CALTECH_RECORD}/files/{filename}?download=1\",\n                      allow_redirects=True, timeout=60)\n    r.raise_for_status()\n    return r.url",
 "new_string": "    \"\"\"Direct URL of a file of the CalMS21 record. It is presigned for 60 s, so a fresh one is\n    taken for each read.\"\"\"\n    with requests.get(f\"https://data.caltech.edu/records/{CALTECH_RECORD}/files/{filename}?download=1\",\n                      allow_redirects=True, stream=True, timeout=60) as r:\n        r.raise_for_status()\n        return r.url"
}
```

```
The file entries/001878-sun-2021/calms21.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/001878-sun-2021 && time $TMPDIR/wk/bin/python -c "
import calms21 as c, numpy as np, json, time
t=time.time()
n=0
for key, text in c.caltech_sequences('task1_classic_classification.zip','task1_classic_classification/calms21_task1_test.json'):
    s=c.sequence_summary(text)
    if n<3 or key.endswith('mouse071_task1_annotator1'):
        full=c.parse_sequence(text)
        kp=np.array(full['keypoints']); sc=np.array(full['scores'])
        print(key, s['n_frames'], kp.shape, sc.shape, len(full['annotations']), full['metadata'], (s['annotations']==np.array(full['annotations'])).all())
    n+=1
print(n, time.time()-t)
"
```

```
task1/test/mouse071_task1_annotator1 0 (23810, 2, 2, 7) (23810, 2, 7) 23810 {'annotator-id': 0, 'vocab': {'attack': 0, 'investigation': 1, 'mount': 2, 'other': 3}} False
task1/test/mouse072_task1_annotator1 0 (18164, 2, 2, 7) (18164, 2, 7) 18164 {'annotator-id': 0, 'vocab': {'attack': 0, 'investigation': 1, 'mount': 2, 'other': 3}} False
task1/test/mouse073_task1_annotator1 0 (19156, 2, 2, 7) (19156, 2, 7) 19156 {'annotator-id': 0, 'vocab': {'attack': 0, 'investigation': 1, 'mount': 2, 'other': 3}} False
19 4.746833086013794

real	0m5.177s
user	0m3.754s
sys	0m0.499s
```

**Agent calls Bash**

```bash
$TMPDIR/wk/bin/python -c "
import calms21 as c
for key, text in c.caltech_sequences('task1_classic_classification.zip','task1_classic_classification/calms21_task1_test.json'):
    for f in [b'\"keypoints\"',b'\"scores\"',b'\"annotations\"',b'\"metadata\"']: print(f, text.find(f))
    i=text.find(b'\"scores\"'); print(text[i:i+300]); print(text[-200:]); break
"
```

```
b'"keypoints"' 452447
b'"scores"' 39866583
b'"annotations"' 14
b'"metadata"' 39866326
b'"scores": [\n                [\n                    [\n                        0.7722973823547363,\n                        0.7741022706031799,\n                        0.7775892615318298,\n                        0.8869567513465881,\n                        0.7078347206115723,\n                        0.77'
b'                      0.7970012426376343,\n                        0.68226158618927,\n                        0.9036930799484253\n                    ]\n                ]\n            ]\n        },\n        '
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/001878-sun-2021/calms21.py",
 "old_string": "    Frames are counted in the `scores` field, where each frame is [[7 scores], [7 scores]], so each\n    frame ends with one \"]]\" (the last frame's \"]]]\" holds one non-overlapping \"]]\").\n    \"\"\"\n    dec = json.JSONDecoder()\n    i = text.find(b'\"scores\"')\n    if i < 0:\n        raise ValueError(\"no scores field\")\n    j = text.find(b'\"annotations\"', i)\n    k = text.find(b'\"metadata\"', i)\n    ends = [x for x in (j, k) if x > 0]\n    scores_text = text[i:min(ends)] if ends else text[i:]\n    out = {\"n_frames\": scores_text.count(b\"]]\"), \"annotations\": None, \"metadata\": None,\n           \"keypoints_head\": None}\n    if j > 0:\n        a = text.index(b\"[\", j)\n        out[\"annotations\"] = np.array(dec.raw_decode(text[a:a + 20_000_000].decode(\"ascii\", \"ignore\"))[0])\n    if k > 0:\n        a = text.index(b\"{\", k)\n        out[\"metadata\"] = dec.raw_decode(text[a:a + 100_000].decode())[0]\n    kp = text.find(b'\"keypoints\"')\n    if kp >= 0:\n        out[\"keypoints_head\"] = text[kp:kp + 4000]\n    return out",
 "new_string": "    Frames are counted in the `scores` field, where each frame is [[7 scores], [7 scores]]: with\n    whitespace removed, each frame ends with one \"]]\" (the last frame's \"]]]\" holds one\n    non-overlapping \"]]\"). `keypoints_head` is the start of the keypoints field without whitespace,\n    used to find sequences deposited twice.\n    \"\"\"\n    dec = json.JSONDecoder()\n    pos = {f: text.find(b'\"%s\"' % f.encode()) for f in (\"keypoints\", \"scores\", \"annotations\", \"metadata\")}\n    if pos[\"scores\"] < 0:\n        raise ValueError(\"no scores field\")\n\n    def field(name):\n        start = pos[name]\n        later = [p for p in pos.values() if p > start]\n        return text[start:min(later)] if later else text[start:]\n\n    out = {\"n_frames\": field(\"scores\").translate(None, b\" \\n\\r\\t\").count(b\"]]\"),\n           \"annotations\": None, \"metadata\": None, \"keypoints_head\": None}\n    if pos[\"annotations\"] >= 0:\n        a = field(\"annotations\").translate(None, b\" \\n\\r\\t\")\n        out[\"annotations\"] = np.array(dec.raw_decode(a[a.index(b\"[\"):].decode())[0])\n    if pos[\"metadata\"] >= 0:\n        m = field(\"metadata\")\n        out[\"metadata\"] = dec.raw_decode(m[m.index(b\"{\"):].decode())[0]\n    if pos[\"keypoints\"] >= 0:\n        out[\"keypoints_head\"] = text[pos[\"keypoints\"]:pos[\"keypoints\"] + 20000].translate(None, b\" \\n\\r\\t\")[:3000]\n    return out"
}
```

```
The file entries/001878-sun-2021/calms21.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
time $TMPDIR/wk/bin/python -c "
import calms21 as c, numpy as np, json, time
t=time.time()
n=0
for key, text in c.caltech_sequences('task1_classic_classification.zip','task1_classic_classification/calms21_task1_test.json'):
    s=c.sequence_summary(text)
    if n<2 or n==18:
        full=c.parse_sequence(text)
        print(key, s['n_frames'], len(full['scores']), len(full['annotations']), s['metadata'], (s['annotations']==np.array(full['annotations'])).all())
    n+=1
print(n, time.time()-t)
"
```

```
task1/test/mouse071_task1_annotator1 23810 23810 23810 {'annotator-id': 0, 'vocab': {'attack': 0, 'investigation': 1, 'mount': 2, 'other': 3}} True
task1/test/mouse072_task1_annotator1 18164 18164 18164 {'annotator-id': 0, 'vocab': {'attack': 0, 'investigation': 1, 'mount': 2, 'other': 3}} True
task1/test/mouse089_task1_annotator1 11274 11274 11274 {'annotator-id': 0, 'vocab': {'attack': 0, 'investigation': 1, 'mount': 2, 'other': 3}} True
19 4.167662620544434

real	0m4.580s
user	0m3.678s
sys	0m0.494s
```

**Agent**

Streaming works: the whole Task 1 test file goes through in about 4 s. Now the data check on the dandiset file.

**Agent calls Bash**

```bash
time $TMPDIR/wk/bin/python -c "
import calms21 as c, numpy as np, pandas as pd
pd.set_option('display.width',200)
s=c.load_session()
kp,sc=s['keypoints'],s['scores']
print(s['n_frames'], s['pose_dimensions'], s['pose_software'], s['annotator'], s['bouts_description'])
print({k:(v['rate'],v['start'],v['unit']) for k,v in list(s['series'].items())[:2]})
print('x range', np.nanmin(kp[:,:,0]), np.nanmax(kp[:,:,0]), 'y', np.nanmin(kp[:,:,1]), np.nanmax(kp[:,:,1]), 'nan', np.isnan(kp).sum())
print('scores', sc.min(), sc.max(), np.isnan(sc).sum())
print(s['ethogram'])
b=s['bouts']; print(b.head(12)); print(b.label.value_counts())
print('dur', (b.stop_time-b.start_time).describe())
st=b.sort_values('start_time'); gaps=st.start_time.values[1:]-st.stop_time.values[:-1]; print('gaps', np.unique(np.round(gaps,6)))
print('first start, last stop', st.start_time.min(), st.stop_time.max(), s['n_frames']/30)
print('starts*30 frac', np.unique(np.round((b.start_time*30)%1,4))[:10], np.unique(np.round((b.stop_time*30)%1,4))[:10])
print(s['subject'], s['session_start_time'], s['video_external_file'], s['video_rate'], s['skeleton_edges'])
cs=s['centroid_speed']; d=s['interanimal_distance']; print('cs', cs[:5], cs.min(), cs.max(), 'dist', d[:5], d.min(), d.max())
"
```

```
23810 [[570, 1024]] MARS CalMS21 annotator 0 CalMS21 task1 social-behavior annotation (single-label partition).
{('resident', 'nose'): (30.0, 0.0, 'pixels'), ('resident', 'ear_left'): (30.0, 0.0, 'pixels')}
x range 5.0 991.1630859375 y 9.0 563.3221459388733 nan 0
scores nan nan 333340
        behavior definition  native_code
0         attack                       0
1  investigation                       1
2          mount                       2
3          other                       3
    start_time  stop_time  ... mean_interanimal_distance  min_interanimal_distance
0     0.000000   0.033333  ...                254.062391                254.062391
1     0.033333  12.200000  ...                120.834142                 66.363565
2    12.200000  13.033333  ...                287.627104                170.411422
3    13.033333  25.566667  ...                154.463032                 99.566391
4    25.566667  26.400000  ...                258.849391                212.210890
5    26.400000  32.166667  ...                111.585364                 60.155968
6    32.166667  32.700000  ...                268.034310                215.176231
7    32.700000  42.633333  ...                 92.378685                 65.960334
8    42.633333  44.266667  ...                135.826806                 82.166120
9    44.266667  48.566667  ...                128.229840                 77.643838
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
$TMPDIR/wk/bin/python -c "
import calms21 as c, numpy as np
s=c.load_session(); kp=s['keypoints']
cen=c.centroids(kp)
d=np.hypot(*(cen[:,0]-cen[:,1]).T); print('dist maxdiff', np.nanmax(np.abs(d-s['interanimal_distance'])))
allc=kp.mean(axis=(1,3)); v=np.r_[np.nan, np.hypot(*np.diff(allc,axis=0).T)*30]
print('speed all14 maxdiff', np.nanmax(np.abs(v-s['centroid_speed'])))
for m in (0,1):
  vm=np.r_[np.nan, np.hypot(*np.diff(cen[:,m],axis=0).T)*30]; print('speed mouse',m, np.nanmax(np.abs(vm-s['centroid_speed'])))
"
```

```
dist maxdiff 1.1368683772161603e-13
speed all14 maxdiff 2.0314416815381264e-11
speed mouse 0 1384.1564003105784
speed mouse 1 1319.7214488650961
```

**Agent**

`centroid_speed` is the speed of the mean of all 14 keypoints, i.e. the midpoint of the two mice, not either animal's speed. Quick look at the other two NWB files, to rule out duplicates.

**Agent calls Bash**

```bash
$TMPDIR/wk/bin/python -c "
import calms21 as c, h5py, remfile
for p in ['sub-mouse-21-11-8-one-mouse/sub-mouse-21-11-8-one-mouse_ses-21-11-8-one-mouse_image.nwb','sub-mlost-batch2-1-mouse/sub-mlost-batch2-1-mouse_ses-batch2-1_image.nwb']:
    f=h5py.File(remfile.File(c.asset_url(p)),'r')
    pe=[k for k in f['processing/behavior'].keys()]
    print(p, f['session_description'][()], f['general/related_publications'][()] if 'related_publications' in f['general'] else None, pe)
    g=f['processing/behavior/PoseEstimation']; k=[x for x in g.keys() if hasattr(g[x],'keys') and 'data' in g[x]][0]; print(k, g[k]['data'].shape)
"
```

```
sub-mouse-21-11-8-one-mouse/sub-mouse-21-11-8-one-mouse_ses-21-11-8-one-mouse_image.nwb b'keypoint-MoSeq full-triple (Weinreb2024, our run): syllable bouts with DeepLabCut pose and video.' [b'https://doi.org/10.5281/zenodo.10636983'] ['PoseEstimation', 'Skeletons', 'centroid_speed', 'kpMoseq_syllable_sequence', 'kpMoseq_syllables', 'kpMoseq_syllables_ethogram']
head (71524, 2)
sub-mlost-batch2-1-mouse/sub-mlost-batch2-1-mouse_ses-batch2-1_image.nwb b'Mlost2025 benchmark batch2_1 (trial 1): four unsupervised motif tools side by side, with DeepLabCut pose and video.' [b'https://doi.org/10.5281/zenodo.14382973'] ['PoseEstimation', 'Skeletons', 'bfa', 'bfa_ethogram', 'bfa_observed_intervals', 'bsoid', 'bsoid_ethogram', 'centroid_speed', 'kpMoseq', 'kpMoseq_ethogram', 'vame', 'vame_ethogram', 'vame_observed_intervals']
bcl (14991, 2)
```

**Agent**

The other two files are keypoint-MoSeq and Mlost data, not CalMS21. Let me check how the target names the paper, then write the claims.

**Agent calls Bash**

```bash
cd  && python -c "
import json; d=json.load(open('targets/dandisets.json'))
items=d if isinstance(d,list) else d.get('targets', d)
for t in (items if isinstance(items,list) else []):
    if '001878' in json.dumps(t): print(json.dumps(t,indent=1)[:1500])
"; python -m json.tool schemas/claims.schema.json | head -120
```

```
{
 "dandiset": "001878",
 "name": "Standardized behavioral segmentation datasets",
 "published_version": null,
 "asset_count": 6,
 "size_gb": 0.23,
 "data_standards": [
  "Neurodata Without Borders (NWB)"
 ],
 "species": [
  "Mus musculus - House mouse"
 ],
 "approaches": [],
 "papers": [
  {
   "doi": "10.22002/d1.1991",
   "title": "CalMS21 - Caltech Mouse Social Interactions (Sun et al., 2021)",
   "relation": "IsDerivedFrom",
   "resource_type": null,
   "preprint": false
[... 126 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/001878/10.22002-d1.1991.yaml",
 "content": "# Claims for the CalMS21 dataset (Sun et al. 2021) on dandiset 001878.\n#\n# The target's DOI, 10.22002/D1.1991, is the CaltechDATA record of the dataset, not a paper. The\n# paper that describes the dataset and is cited by that record is Sun, Karigo, Chakraborty,\n# Mohanty, Wild, Sun, Chen, Anderson, Perona, Yue and Kennedy (2021), \"The Multi-Agent Behavior\n# Dataset: Mouse Dyadic Social Interactions\", NeurIPS 2021 Datasets and Benchmarks track,\n# arXiv:2104.02710v4. Its full text is open access and was used, including the appendix with the\n# datasheet (Appendix B), the data format (C), the dataset preparation (D) and the results tables.\n#\n# Dandiset 001878 is a collection of conversions from three source datasets. It holds one CalMS21\n# sequence, the Task 1 test sequence mouse071 (pose, annotations as bouts, and the video). The rest\n# of CalMS21 is public on CaltechDATA (record s0vdx-0k302, version 1.0), so the claims about the\n# dataset as a whole are `data: elsewhere` and are tested on those files.\n#\n# When these criteria were written, the author had seen: the dandiset's file list and metadata;\n# every object of the CalMS21 NWB file and the values of its data check (14 keypoint series at 30\n# Hz, positions within the image, every confidence value NaN, bouts that tile the session with the\n# labels investigation, other and mount and no attack, the derived speed and distance series);\n# the frame count, rate and size of its video; the list of members of the CaltechDATA zips, and the\n# sequence keys of the Task 1 files (70 train and 19 test sequences, mouse071 the first test\n# sequence) with the frame counts and metadata of three test sequences. No claim's analysis had\n# been run otherwise: no comparison of the dandiset's sequence with CaltechDATA, no counts or label\n# fractions of any set, no analysis of pose errors, contact or coat colour.\n#\n# The code the paper links for its baselines (gitlab.aicrowd.com/aicrowd/research/mab-e/\n# mab-e-baselines) did not answer from here, and no copy of it was found in Software Heritage or on\n# GitHub; the web archive holds its landing page only. The task programming code (GitHub\n# neuroethology/TREBA) is public. The code of the challenge's top entries is not linked.\nschema_version: 1\ndandiset: \"001878\"\npaper: doi:10.22002/d1.1991\nclaims:\n- id: format-keypoints\n  statement: Each frame holds seven MARS keypoints (nose, left ear, right ear, neck, left hip,\n    right hip, tail base) for each of two mice, the resident (mouse 0) and the intruder (mouse 1),\n    in pixel coordinates of a 1024 x 570 image, at 30 Hz, with a confidence score from 0 to 1 for\n    each keypoint.\n  source: Section 3 and Figure 3; Appendix C (data format); Appendix D.1\n  criterion: Judged on the dandiset's CalMS21 file. Reproduced when it holds 14 keypoint series\n    named for these seven parts on the resident and the intruder, in pixels, sampled at 30 Hz,\n    with every coordinate within 0 to 1024 (x) and 0 to 570 (y), and a confidence value for each\n    keypoint and frame within 0 to 1. Partially reproduced when the positions meet all of this but\n    the confidence values are missing or out of range. Not reproduced otherwise.\n- id: resident-is-black\n  statement: Mouse 0, the resident, is the black C57Bl/6J mouse, and mouse 1, the intruder, is\n    the white BALB/c mouse.\n  source: Appendix C; Appendix B (Collection Process); Appendix D.1\n  criterion: On the dandiset's video and pose. Every 30th frame, the mean grey level of the video\n    in a patch of 12 x 12 pixels centred on each mouse's body centre (the mean of its neck and two\n    hip keypoints), using frames where the two body centres are at least 60 pixels apart.\n    Reproduced when the resident's patch is darker than the intruder's in at least 90% of these\n    frames; partially reproduced for 50% to 90%; not reproduced below 50%.\n- id: task1-vocab\n  statement: Task 1 frames are annotated by one annotator (annotator id 0) with exactly one label\n    per frame from the vocabulary attack 0, investigation 1, mount 2 and other 3.\n  source: Section 3; Appendix C (metadata and vocab)\n  criterion: On the dandiset's CalMS21 file. Reproduced when its catalogue of behaviors holds\n    these four names with these integer codes, the annotator is given as 0, and the bouts give\n    exactly one label to every frame of the session (no frame uncovered, none covered twice).\n    Partially reproduced when the names and codes hold but the annotator or the one-label rule\n    does not. Not reproduced when the names or codes differ.\n- id: task1-video\n  statement: The source videos of Task 1 are released, recorded at 30 Hz and 1024 x 570 pixels.\n  source: Section 3.1; Appendix D.1\n  criterion: On the dandiset's video of mouse071. Reproduced when it is 1024 x 570 pixels at 30\n    frames per second and has as many frames as the pose. Partially reproduced when it is\n    present but one of the three differs; not reproduced when it is absent or unreadable.\n- id: contact-during-social-behaviors\n  statement: Close investigation, attack and mount are behaviors in which the resident is in\n    close contact with the intruder; other frames include the animals apart.\n  source: Appendix D.2 (behavior definitions)\n  criterion: On the dandiset's pose and bouts. Per frame, the distance from the resident's nose\n    to the nearest intruder keypoint. Reproduced when, for each social label present in the\n    session, the median distance in its frames is below the median in \"other\" frames, with a 95%\n    moving-block bootstrap interval (blocks of 300 frames, 2000 resamples) of the difference that\n    excludes 0. Partially reproduced when this holds for some labels only. A label with no frames\n    in the session is reported as untested.\n- id: pose-errors-close-fast\n  statement: Errors in pose estimation are most common on frames when the two animals are in\n    close contact or moving very quickly.\n  source: Appendix B (Composition, errors and noise)\n  criterion: On the dandiset's pose alone, as it holds no usable confidence values. A frame is\n    counted as a pose error when any of four body lengths of either mouse (nose to neck, neck to\n    tail base, left to right ear, left to right hip) lies outside the session's quartiles widened\n    by 3 times the interquartile range. Close frames are the lowest 10% of the distance between\n    the two mice's centroids; fast frames are the highest 10% of the faster mouse's centroid speed\n    after a 15-frame running median. Reproduced when the error fraction is higher in close frames\n    than in the others and higher in fast frames than in the others, each with a 95% moving-block\n    bootstrap interval (blocks of 300 frames, 2000 resamples) of the difference that excludes 0.\n    Partially reproduced when this holds for one of the two. Thresholds of 5% and 20%, and a\n    factor of 1.5, are shown as variants.\n- id: link-mouse071\n  statement: The dandiset's CalMS21 sequence is the CalMS21 Task 1 test sequence mouse071, with\n    the same keypoints, confidence scores and frame annotations.\n  source: Appendix C; CaltechDATA record 10.22002/D1.1991, file task1_classic_classification.zip\n  data: with_inputs\n  criterion: Records are matched by name (session mouse071_task1 against the key\n    task1/test/mouse071_task1_annotator1). Reproduced when the frame counts are equal, every\n    keypoint coordinate agrees within 0.001 pixel with mice, parts and axes in the stated order,\n    and the frame labels from the bouts agree with the CaltechDATA annotations (through the\n    catalogue's codes) on every frame. Partially reproduced when at least 99% of coordinates and\n    of frames agree. Not reproduced otherwise. The confidence scores are compared and reported;\n    the dandiset's are known to be empty (data check), which is recorded under format-keypoints\n    and as a finding, and does not decide the link.\n- id: pose-errors-close-fast-confidence\n  statement: Errors in pose estimation are most common on frames when the two animals are in\n    close contact or moving very quickly, as shown by the MARS confidence scores.\n  source: Appendix B (Composition, errors and noise)\n  data: with_inputs\n  depends_on:\n  - link-mouse071\n  criterion: The confidence scores come from CaltechDATA's copy of mouse071, matched frame by\n    frame; positions, distances and speeds come from the dandiset. Per frame, the mean confidence\n    over the 14 keypoints. Close and fast frames as in pose-errors-close-fast. Reproduced when the\n    median confidence is lower in close frames than in the others and lower in fast frames than in\n    the others, each with a 95% moving-block bootstrap interval (blocks of 300 frames, 2000\n    resamples) that excludes 0; partially reproduced when this holds for one of the two.\n- id: table5-task1-counts\n  statement: Task 1 has 70 training sequences with 507,738 frames and 19 test sequences with\n    262,107 frames.\n  source: Table 5; Section 3.1; Figure 4A\n  data: elsewhere\n  where: CaltechDATA doi:10.22002/D1.1991 (record s0vdx-0k302, version 1.0)\n  expected:\n  - quantity: Task 1 training frames\n    value: 507738\n    tolerance: 0\n  - quantity: Task 1 training sequences\n    value: 70\n    tolerance: 0\n  - quantity: Task 1 test frames\n    value: 262107\n    tolerance: 0\n  - quantity: Task 1 test sequences\n    value: 19\n    tolerance: 0\n  criterion: Counts of a fixed deposited file, so the tolerance is 0. Frames are counted as the\n    length of each sequence's annotations, checked against its scores. Reproduced when all four\n    match; partially reproduced when all are within 10% of the reported value; not reproduced\n    otherwise.\n- id: table5-task2-counts\n  statement: Task 2 has, for annotators 1 to 5, 6 training sequences each with 139,112, 135,623,\n    107,420, 108,325 and 92,383 frames, and 13, 6, 4, 4 and 20 test sequences with 286,810,\n    150,919, 77,079, 76,174 and 364,007 frames.\n  source: Table 5; Section 3.2\n  data: elsewhere\n  where: CaltechDATA doi:10.22002/D1.1991 (record s0vdx-0k302, version 1.0)\n  expected:\n  - {quantity: annotator 1 training frames, value: 139112, tolerance: 0}\n  - {quantity: annotator 1 training sequences, value: 6, tolerance: 0}\n  - {quantity: annotator 1 test frames, value: 286810, tolerance: 0}\n  - {quantity: annotator 1 test sequences, value: 13, tolerance: 0}\n  - {quantity: annotator 2 training frames, value: 135623, tolerance: 0}\n  - {quantity: annotator 2 training sequences, value: 6, tolerance: 0}\n  - {quantity: annotator 2 test frames, value: 150919, tolerance: 0}\n  - {quantity: annotator 2 test sequences, value: 6, tolerance: 0}\n  - {quantity: annotator 3 training frames, value: 107420, tolerance: 0}\n  - {quantity: annotator 3 training sequences, value: 6, tolerance: 0}\n  - {quantity: annotator 3 test frames, value: 77079, tolerance: 0}\n  - {quantity: annotator 3 test sequences, value: 4, tolerance: 0}\n  - {quantity: annotator 4 training frames, value: 108325, tolerance: 0}\n  - {quantity: annotator 4 training sequences, value: 6, tolerance: 0}\n  - {quantity: annotator 4 test frames, value: 76174, tolerance: 0}\n  - {quantity: annotator 4 test sequences, value: 4, tolerance: 0}\n  - {quantity: annotator 5 training frames, value: 92383, tolerance: 0}\n  - {quantity: annotator 5 training sequences, value: 6, tolerance: 0}\n  - {quantity: annotator 5 test frames, value: 364007, tolerance: 0}\n  - {quantity: annotator 5 test sequences, value: 20, tolerance: 0}\n  criterion: As table5-task1-counts, over the 20 counts.\n- id: table5-task3-counts\n  statement: Task 3 has, for approach, disengaged, grooming, intromission, mount attempt, sniff\n    face and white rearing, 3, 2, 2, 1, 4, 3 and 2 training sequences with 20,624, 35,751, 45,174,\n    19,200, 46,847, 19,244 and 36,181 frames, and 25, 1, 13, 10, 12, 47 and 1 test sequences with\n    126,468, 19,088, 156,664, 55,218, 85,836, 251,793 and 17,939 frames.\n  source: Table 5; Section 3.3; Figure 4A\n  data: elsewhere\n  where: CaltechDATA doi:10.22002/D1.1991 (record s0vdx-0k302, version 1.0)\n  expected:\n  - {quantity: approach training frames, value: 20624, tolerance: 0}\n  - {quantity: approach training sequences, value: 3, tolerance: 0}\n  - {quantity: approach test frames, value: 126468, tolerance: 0}\n  - {quantity: approach test sequences, value: 25, tolerance: 0}\n  - {quantity: disengaged training frames, value: 35751, tolerance: 0}\n  - {quantity: disengaged training sequences, value: 2, tolerance: 0}\n  - {quantity: disengaged test frames, value: 19088, tolerance: 0}\n  - {quantity: disengaged test sequences, value: 1, tolerance: 0}\n  - {quantity: grooming training frames, value: 45174, tolerance: 0}\n  - {quantity: grooming training sequences, value: 2, tolerance: 0}\n  - {quantity: grooming test frames, value: 156664, tolerance: 0}\n  - {quantity: grooming test sequences, value: 13, tolerance: 0}\n  - {quantity: intromission training frames, value: 19200, tolerance: 0}\n  - {quantity: intromission training sequences, value: 1, tolerance: 0}\n  - {quantity: intromission test frames, value: 55218, tolerance: 0}\n  - {quantity: intromission test sequences, value: 10, tolerance: 0}\n  - {quantity: mount attempt training frames, value: 46847, tolerance: 0}\n  - {quantity: mount attempt training sequences, value: 4, tolerance: 0}\n  - {quantity: mount attempt test frames, value: 85836, tolerance: 0}\n  - {quantity: mount attempt test sequences, value: 12, tolerance: 0}\n  - {quantity: sniff face training frames, value: 19244, tolerance: 0}\n  - {quantity: sniff face training sequences, value: 3, tolerance: 0}\n  - {quantity: sniff face test frames, value: 251793, tolerance: 0}\n  - {quantity: sniff face test sequences, value: 47, tolerance: 0}\n  - {quantity: white rearing training frames, value: 36181, tolerance: 0}\n  - {quantity: white rearing training sequences, value: 2, tolerance: 0}\n  - {quantity: white rearing test frames, value: 17939, tolerance: 0}\n  - {quantity: white rearing test sequences, value: 1, tolerance: 0}\n  criterion: As table5-task1-counts, over the 28 counts.\n- id: table6-task1-label-fractions\n  statement: In the Task 1 training set, 2.76% of frames are labelled attack, 28.9%\n    investigation, 5.64% mount and 62.7% other.\n  source: Table 6; Figure 4B\n  data: elsewhere\n  where: CaltechDATA doi:10.22002/D1.1991 (record s0vdx-0k302, version 1.0)\n  expected:\n  - {quantity: attack, value: 2.76, tolerance: 0.005, unit: percent of frames}\n  - {quantity: investigation, value: 28.9, tolerance: 0.05, unit: percent of frames}\n  - {quantity: mount, value: 5.64, tolerance: 0.005, unit: percent of frames}\n  - {quantity: other, value: 62.7, tolerance: 0.05, unit: percent of frames}\n  criterion: Percentages of a fixed deposited file, so the tolerance is half a unit of the last\n    digit reported. Readings of the frames counted are (a) the training split, as the table\n    says, and (b) training and test together. Reproduced when all four are within tolerance\n    under one reading; partially reproduced when all four are within 10% of the reported value\n    under one reading; not reproduced otherwise.\n- id: fig4b-task2-label-fractions\n  statement: The five Task 2 annotators label different fractions of frames as other,\n    investigation, mount and attack (annotator 1 60.0, 20.6, 16.2 and 3.2%; annotator 2 65.5,\n    25.8, 3.4 and 5.3%; annotator 3 68.9, 13.5, 9.5 and 8.1%; annotator 4 75.2, 11.6, 4.5 and\n    8.7%; annotator 5 69.5, 26.4, 1.0 and 3.0%).\n  source: Figure 4B\n  data: elsewhere\n  where: CaltechDATA doi:10.22002/D1.1991 (record s0vdx-0k302, version 1.0)\n  expected:\n  - {quantity: annotator 1 other, value: 60.0, tolerance: 0.05, unit: percent of frames}\n  - {quantity: annotator 1 investigation, value: 20.6, tolerance: 0.05, unit: percent of frames}\n  - {quantity: annotator 1 mount, value: 16.2, tolerance: 0.05, unit: percent of frames}\n  - {quantity: annotator 1 attack, value: 3.2, tolerance: 0.05, unit: percent of frames}\n  - {quantity: annotator 2 other, value: 65.5, tolerance: 0.05, unit: percent of frames}\n  - {quantity: annotator 2 investigation, value: 25.8, tolerance: 0.05, unit: percent of frames}\n  - {quantity: annotator 2 mount, value: 3.4, tolerance: 0.05, unit: percent of frames}\n  - {quantity: annotator 2 attack, value: 5.3, tolerance: 0.05, unit: percent of frames}\n  - {quantity: annotator 3 other, value: 68.9, tolerance: 0.05, unit: percent of frames}\n  - {quantity: annotator 3 investigation, value: 13.5, tolerance: 0.05, unit: percent of frames}\n  - {quantity: annotator 3 mount, value: 9.5, tolerance: 0.05, unit: percent of frames}\n  - {quantity: annotator 3 attack, value: 8.1, tolerance: 0.05, unit: percent of frames}\n  - {quantity: annotator 4 other, value: 75.2, tolerance: 0.05, unit: percent of frames}\n  - {quantity: annotator 4 investigation, value: 11.6, tolerance: 0.05, unit: percent of frames}\n  - {quantity: annotator 4 mount, value: 4.5, tolerance: 0.05, unit: percent of frames}\n  - {quantity: annotator 4 attack, value: 8.7, tolerance: 0.05, unit: percent of frames}\n  - {quantity: annotator 5 other, value: 69.5, tolerance: 0.05, unit: percent of frames}\n  - {quantity: annotator 5 investigation, value: 26.4, tolerance: 0.05, unit: percent of frames}\n  - {quantity: annotator 5 mount, value: 1.0, tolerance: 0.05, unit: percent of frames}\n  - {quantity: annotator 5 attack, value: 3.0, tolerance: 0.05, unit: percent of frames}\n  criterion: The pie charts carry no class names for Task 2; the order is read from the Task 1\n    pie (other, investigation, mount, attack). Tolerance is half a unit of the last digit, as in\n    table6-task1-label-fractions. Readings are (a) the training split and (b) training and test\n    together, and for the classes (i) the Task 1 order and (ii) the four values of each annotator\n    matched to the four classes in whatever order fits best. Reproduced when all 20 values are\n    within tolerance under one combination of readings; partially reproduced when at least 16\n    are; not reproduced otherwise.\n- id: table7-task3-label-fractions\n  statement: In Task 3 the behaviors occupy 3.25% (approach), 1.47% (disengaged), 14.0%\n    (groom), 19.3% (intromission), 0.90% (mount attempt), 4.74% (sniff face) and 9.29% (white\n    rearing) of frames.\n  source: Table 7; Figure 4B\n  data: elsewhere\n  where: CaltechDATA doi:10.22002/D1.1991 (record s0vdx-0k302, version 1.0)\n  expected:\n  - {quantity: approach, value: 3.25, tolerance: 0.005, unit: percent of frames}\n  - {quantity: disengaged, value: 1.47, tolerance: 0.005, unit: percent of frames}\n  - {quantity: groom, value: 14.0, tolerance: 0.05, unit: percent of frames}\n  - {quantity: intromission, value: 19.3, tolerance: 0.05, unit: percent of frames}\n  - {quantity: mount attempt, value: 0.90, tolerance: 0.005, unit: percent of frames}\n  - {quantity: sniff face, value: 4.74, tolerance: 0.005, unit: percent of frames}\n  - {quantity: white rearing, value: 9.29, tolerance: 0.005, unit: percent of frames}\n  criterion: Tolerance is half a unit of the last digit, as in table6-task1-label-fractions.\n    Readings are (a) the training split of each behavior and (b) training and test together.\n    Reproduced when all seven are within tolerance under one reading; partially reproduced when\n    all are within 10% of the reported value; not reproduced otherwise.\n- id: dataset-size\n  statement: The unlabeled set has 282 videos and about 6 million frames; the dataset holds over\n    1 million annotated frames, over 70 hours of tracked poses and over 10 hours of frame-by-frame\n    annotation.\n  source: Abstract; Section 3; Figure 4A; Section 5 (Discussion)\n  data: elsewhere\n  where: CaltechDATA doi:10.22002/D1.1991 (record s0vdx-0k302, version 1.0)\n  expected:\n  - {quantity: unlabeled sequences, value: 282, tolerance: 0}\n  - {quantity: unlabeled frames, value: 6000000, tolerance: 600000}\n  criterion: Unlabeled frames are counted from the scores of each sequence. The statements \"over\"\n    a value are read (a) over Task 1 only (training and test), (b) over all labelled sets of the\n    three tasks, and (c) as (b) with sequences deposited more than once counted once; tracked\n    poses add the unlabeled set to each reading. Hours are frames / 30 / 3600. Reproduced when the\n    two expected values hold and each of the three \"over\" statements holds under at least one\n    reading; partially reproduced when only some of these hold; not reproduced when none does.\n- id: table10-task3-difficulty\n  statement: On Task 3, classifier performance depends on the percentage of frames in which a\n    behavior is observed and on its average bout duration, with shorter bouts giving lower\n    performance.\n  source: Section 4.4; Tables 7 and 10\n  data: elsewhere\n  where: CaltechDATA doi:10.22002/D1.1991 (record s0vdx-0k302, version 1.0)\n  criterion: Across the seven behaviors, Spearman correlations of the baseline model's F1 score\n    in Table 10 with (i) the percentage of frames labelled with the behavior and (ii) its mean\n    bout length (runs of consecutive labelled frames), computed from the data on (a) the training\n    split or (b) the test split. Reproduced when, under one reading, both correlations are\n    positive with a one-sided exact permutation p below 0.05; partially reproduced when both are\n    positive under one reading but not both significant; not reproduced otherwise. The F1 of the\n    baseline with task programming features is shown as a variant.\n- id: table1-architectures\n  statement: Among baseline architectures trained on Task 1, the 1D convolutional network\n    performs best (F1 0.793, MAP 0.856), ahead of fully connected (0.659), LSTM (0.675) and\n    self-attention (0.610) models.\n  source: Table 1; Section 4.1\n  data: elsewhere\n  where: CaltechDATA doi:10.22002/D1.1991 (record s0vdx-0k302, version 1.0)\n- id: table2-task-programming\n  statement: Adding task programming features learned from the unlabeled set raises Task 1 F1\n    from 0.793 to 0.829, and the challenge's top entry reaches 0.864.\n  source: Table 2 and Table 8; Section 4.2\n  data: elsewhere\n  where: CaltechDATA doi:10.22002/D1.1991 (record s0vdx-0k302, version 1.0)\n- id: table3-task2-style-transfer\n  statement: On Task 2 the fine-tuned baseline reaches an annotator-averaged F1 of 0.754, 0.774\n    with task programming features and 0.809 for the top entry, and all models do better on\n    annotators 1 and 2 than on 3, 4 and 5.\n  source: Table 3 and Table 9; Section 4.3 and Appendix G.2\n  data: elsewhere\n  where: CaltechDATA doi:10.22002/D1.1991 (record s0vdx-0k302, version 1.0)\n- id: table4-task3-new-behaviors\n  statement: On Task 3 the baseline reaches a behavior-averaged F1 of 0.338 (0.328 with task\n    programming features, 0.319 for the top entry), far below Tasks 1 and 2.\n  source: Table 4 and Table 10; Section 4.4\n  data: elsewhere\n  where: CaltechDATA doi:10.22002/D1.1991 (record s0vdx-0k302, version 1.0)\n- id: fig7-errors-at-transitions\n  statement: Many prediction errors of the baseline models fall around the boundaries between\n    behaviors.\n  source: Figure 7; Section 4.2\n  data: elsewhere\n  where: CaltechDATA doi:10.22002/D1.1991 (record s0vdx-0k302, version 1.0)\n- id: fig11-annotator-similarity\n  statement: The annotator embedding learned by the top Task 2 entry places annotators 3 and 4\n    close to each other and apart from annotators 1, 2 and 5.\n  source: Figure 11; Section 4.3 and Appendix G.2\n  data: elsewhere\n  where: CaltechDATA doi:10.22002/D1.1991 (record s0vdx-0k302, version 1.0)\n"
}
```

```
File created successfully at: claims/001878/10.22002-d1.1991.yaml (file state is current in your context — no need to Read it back)
```

**Agent**

Now a helper that summarizes every sequence of a CaltechDATA set (frames, label counts, bout lengths, a hash for duplicate detection).

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/001878-sun-2021/calms21.py",
 "old_string": "def parse_sequence(text: bytes) -> dict:",
 "new_string": "CALMS21_FILES = {  # (zip, member) of the pose and annotation files of each set\n    (\"task1\", \"train\"): (\"task1_classic_classification.zip\", \"task1_classic_classification/calms21_task1_train.json\"),\n    (\"task1\", \"test\"): (\"task1_classic_classification.zip\", \"task1_classic_classification/calms21_task1_test.json\"),\n    (\"task2\", \"train\"): (\"task2_annotation_styles.zip\", \"task2_annotation_styles/calms21_task2_train.json\"),\n    (\"task2\", \"test\"): (\"task2_annotation_styles.zip\", \"task2_annotation_styles/calms21_task2_test.json\"),\n    (\"task3\", \"train\"): (\"task3_new_behaviors.zip\", \"task3_new_behaviors/calms21_task3_train.json\"),\n    (\"task3\", \"test\"): (\"task3_new_behaviors.zip\", \"task3_new_behaviors/calms21_task3_test.json\"),\n    **{(\"unlabeled\", f\"part{i}\"): (\"unlabeled_videos.zip\", f\"unlabeled_videos/calms21_unlabeled_videos_part{i}.json\")\n       for i in range(1, 5)},\n}\n\n\ndef run_lengths(mask: np.ndarray) -> np.ndarray:\n    \"\"\"Lengths (frames) of the runs of True in a boolean array.\"\"\"\n    m = np.concatenate([[False], mask.astype(bool), [False]])\n    edges = np.flatnonzero(np.diff(m.astype(int)))\n    return edges[1::2] - edges[0::2]\n\n\ndef set_summary(task: str, split: str) -> pd.DataFrame:\n    \"\"\"One row per sequence of a CalMS21 set: frames, frames per annotation code, the runs of each\n    code, the vocabulary and annotator, and a hash of the start of the keypoints (to find\n    sequences deposited twice).\"\"\"\n    import hashlib\n    zip_name, member = CALMS21_FILES[(task, split)]\n    rows = []\n    for key, text in caltech_sequences(zip_name, member):\n        s = sequence_summary(text)\n        row = {\"task\": task, \"split\": split, \"key\": key, \"n_frames\": s[\"n_frames\"],\n               \"kp_hash\": hashlib.sha1(s[\"keypoints_head\"]).hexdigest() if s[\"keypoints_head\"] else None}\n        a = s[\"annotations\"]\n        if a is not None:\n            row[\"n_annotations\"] = len(a)\n            codes, counts = np.unique(a, return_counts=True)\n            row[\"counts\"] = dict(zip(codes.tolist(), counts.tolist()))\n            row[\"runs\"] = {int(c): run_lengths(a == c).tolist() for c in codes}\n        if s[\"metadata\"] is not None:\n            row[\"vocab\"] = s[\"metadata\"].get(\"vocab\")\n            row[\"annotator\"] = s[\"metadata\"].get(\"annotator-id\", s[\"metadata\"].get(\"annotator_id\"))\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\ndef caltech_sequence(task: str, split: str, name: str) -> dict:\n    \"\"\"One sequence of a CalMS21 set, fully parsed, found by the end of its key.\"\"\"\n    zip_name, member = CALMS21_FILES[(task, split)]\n    for key, text in caltech_sequences(zip_name, member):\n        if key.endswith(name):\n            obj = parse_sequence(text)\n            obj[\"key\"] = key\n            return obj\n    raise KeyError(name)\n\n\ndef parse_sequence(text: bytes) -> dict:"
}
```

```
The file entries/001878-sun-2021/calms21.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/001878-sun-2021 && time $TMPDIR/wk/bin/python -c "
import calms21 as c, time
t=time.time()
d=c.set_summary('task3','train'); print(d[['key','n_frames','n_annotations','annotator','vocab']].head(3).to_string()); print(time.time()-t)
t=time.time()
d=c.set_summary('unlabeled','part3'); print(len(d), d.n_frames.sum(), d.key.head(2).tolist(), time.time()-t)
"
```

```
key  n_frames  n_annotations  annotator                        vocab
0  task3/approach/train/mouse001_task3_approach     13222          13222          0  {'approach': 1, 'other': 0}
1  task3/approach/train/mouse002_task3_approach      3770           3770          0  {'approach': 1, 'other': 0}
2  task3/approach/train/mouse003_task3_approach      3632           3632          0  {'approach': 1, 'other': 0}
3.1484503746032715
70 1271925 ['unlabeled_videos/mouse142_unlabeled', 'unlabeled_videos/mouse143_unlabeled'] 14.414357423782349

real	0m17.952s
user	0m14.477s
sys	0m2.201s
```

**Agent**

Streaming summaries take about 3 s for Task 3 train and 15 s per unlabeled part, so the full CaltechDATA pass should take about 2 minutes. Writing the notebook now.

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build_nb.py",
 "content": "import nbformat\nfrom nbformat.v4 import new_markdown_cell as md, new_code_cell as code\n\ncells = []\n\n\ndef M(s):\n    cells.append(md(s.strip(\"\\n\")))\n\n\ndef C(s, tags=None):\n    c = code(s.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\nM(r\"\"\"\n# Reproducing the CalMS21 dataset paper (Sun et al. 2021) from dandiset 001878\n\n**Paper.** Sun JJ, Karigo T, Chakraborty D, Mohanty SP, Wild B, Sun Q, Chen C, Anderson DJ, Perona P,\nYue Y, Kennedy A (2021). The Multi-Agent Behavior Dataset: Mouse Dyadic Social Interactions. NeurIPS\n2021 Datasets and Benchmarks track. [arXiv:2104.02710v4](https://arxiv.org/abs/2104.02710). The target\nnames [doi:10.22002/D1.1991](https://doi.org/10.22002/D1.1991), which is the CaltechDATA record of the\ndataset (CalMS21); this paper is the one that record and the dataset describe. The full text (arXiv v4,\nwith its appendix and datasheet) was used.\n\n**Dandiset.** [DANDI:001878](https://dandiarchive.org/dandiset/001878/draft), version `draft`.\nThe dandiset has no published version, so the draft is the only one there is. It was last modified on\n2026-06-25T18:32:10Z. To keep a changing draft from passing unnoticed, the helper module checks the\nblob id of each asset it reads against the one recorded when this notebook was written, and stops if\nit differs. The dandiset is a collection of conversions from three source datasets; for CalMS21 it\nholds one sequence, the Task 1 test sequence mouse071 (pose, annotations as bouts, and the video).\n\n**Data from elsewhere.** The paper deposited the whole dataset on CaltechDATA (record s0vdx-0k302,\nversion 1.0, the target DOI). The claims about the dataset as a whole (`elsewhere`) are tested on\nthose files, streamed from the record's zips with range requests. The link claim and one pose-error\nclaim (`with inputs`) use CaltechDATA's copy of mouse071 next to the dandiset's.\n\n**Code.** The baseline code the paper links (gitlab.aicrowd.com/aicrowd/research/mab-e/mab-e-baselines)\ndid not answer and no archived copy of the repository was found, and the top entries' code is not\nlinked, so the model benchmarks are blocked.\n\n| Claim | Data | Status |\n|---|---|---|\n| format-keypoints | dandiset | tested |\n| resident-is-black | dandiset | tested |\n| task1-vocab | dandiset | tested |\n| task1-video | dandiset | tested |\n| contact-during-social-behaviors | dandiset | tested |\n| pose-errors-close-fast | dandiset | tested |\n| link-mouse071 | with inputs | tested |\n| pose-errors-close-fast-confidence | with inputs | tested |\n| table5-task1-counts | elsewhere | tested |\n| table5-task2-counts | elsewhere | tested |\n| table5-task3-counts | elsewhere | tested |\n| table6-task1-label-fractions | elsewhere | tested |\n| fig4b-task2-label-fractions | elsewhere | tested |\n| table7-task3-label-fractions | elsewhere | tested |\n| dataset-size | elsewhere | tested |\n| table10-task3-difficulty | elsewhere | tested |\n| table1-architectures, table2-task-programming, table3-task2-style-transfer, table4-task3-new-behaviors, fig7-errors-at-transitions, fig11-annotator-similarity | elsewhere | blocked: the models' code and settings are not available |\n\nRandom numbers are drawn only by the bootstrap intervals; each claim's section has its own generator\nwith a fixed seed.\n\"\"\")\n\nC(r\"\"\"\nimport itertools\nimport time\nimport warnings\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\n\nimport calms21\n\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 200)\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nstarted_all = time.time()\nstarted = time.time()\ns = calms21.load_session()\nkp, sc, n = s[\"keypoints\"], s[\"scores\"], s[\"n_frames\"]\nprint(f\"loaded {calms21.CALMS21_NWB} from dandiset {calms21.DANDISET_ID} version {calms21.DANDISET_VERSION} \"\n      f\"in {time.time() - started:.0f} s\")\n\"\"\")\n\nM(r\"\"\"\n## Data check\n\nEach check of the metadata against the values is stated under its output.\n\"\"\")\n\nC(r\"\"\"\ninfo = calms21.draft_info()\nprint(\"Draft modified:\", info[\"modified\"], \"; recorded when written:\", calms21.DRAFT_MODIFIED)\nprint(\"Published version:\", info.get(\"dandiset\", {}).get(\"most_recent_published_version\"))\nassets = calms21.list_assets()\nprint(f\"\\n{len(assets)} assets:\")\nprint(assets[[\"path\", \"size\", \"blob\"]].to_string(index=False))\nfor path, blob in calms21.BLOBS.items():\n    print(\"pinned blob unchanged:\", path.split(\"/\")[-1], bool((assets.set_index(\"path\").blob[path]) == blob))\nmeta = calms21.requests.get(f\"{calms21.API}/dandisets/001878/versions/draft/\").json()\nsumm = meta[\"assetsSummary\"]\nprint(\"\\nassetsSummary: numberOfSubjects\", summ[\"numberOfSubjects\"], \"; numberOfFiles\", summ[\"numberOfFiles\"],\n      \"; species\", [x[\"name\"] for x in summ[\"species\"]], \"; approach\", summ[\"approach\"],\n      \"; measurementTechnique\", [x[\"name\"] for x in summ[\"measurementTechnique\"]])\nprint(\"relatedResource:\", [(r[\"name\"], r[\"relation\"]) for r in meta[\"relatedResource\"]])\nprint(\"license:\", meta[\"license\"])\n\"\"\", [\"sanity\"])\n\nM(r\"\"\"\nThe dandiset holds three NWB files with their videos, from three source datasets (keypoint-MoSeq,\nthe Mlost benchmark and CalMS21); only `sub-mouse071-resident-intruder` is CalMS21. The other two have\ndifferent pose series and frame counts (71,524 and 14,991 frames, against 23,810 here) and cite other\nDOIs, so no CalMS21 recording is deposited twice. CalMS21 is linked as `IsDerivedFrom`, and the\ndandiset's licence is CC-BY-4.0, which matches the CaltechDATA record (shown below) but not the paper's\ndatasheet, which gives CC-BY-NC-SA.\n\"\"\")\n\nC(r\"\"\"\nprint(\"session_id:\", s[\"session_id\"], \"; identifier:\", s[\"identifier\"])\nprint(\"session_start_time:\", s[\"session_start_time\"], \"; related_publications:\", s[\"related_publications\"])\nprint(\"subject:\", {k: v for k, v in s[\"subject\"].items() if k != \"description\"})\nprint(\"subject description:\", s[\"subject\"][\"description\"])\nprint(\"\\npose software:\", s[\"pose_software\"], \"; dimensions (rows, cols):\", s[\"pose_dimensions\"])\nprint(\"skeleton nodes:\", s[\"skeleton_nodes\"])\nrates = {v[\"rate\"] for v in s[\"series\"].values()}\nstarts = {v[\"start\"] for v in s[\"series\"].values()}\nunits = {v[\"unit\"] for v in s[\"series\"].values()}\nprint(\"series:\", len(s[\"series\"]), \"; rates\", rates, \"; starting times\", starts, \"; units\", units,\n      \"; reference frame\", {v[\"reference_frame\"] for v in s[\"series\"].values()})\nprint(\"frames:\", n, \"=\", round(n / calms21.RATE, 2), \"s\")\nrng_tab = pd.DataFrame({\n    \"x_min\": kp[:, :, 0].min(axis=(0, 2)), \"x_max\": kp[:, :, 0].max(axis=(0, 2)),\n    \"y_min\": kp[:, :, 1].min(axis=(0, 2)), \"y_max\": kp[:, :, 1].max(axis=(0, 2)),\n    \"nan\": np.isnan(kp).sum(axis=(0, 2, 3))}, index=calms21.MICE)\nprint(\"\\nkeypoint ranges (pixels):\")\nprint(rng_tab.round(1).to_string())\nprint(\"\\nconfidence values: finite\", int(np.isfinite(sc).sum()), \"of\", sc.size, \"; NaN\", int(np.isnan(sc).sum()))\nprint(\"derived series rates:\", s[\"centroid_speed_rate\"], s[\"interanimal_distance_rate\"],\n      \"; lengths\", len(s[\"centroid_speed\"]), len(s[\"interanimal_distance\"]), \"; video rate\", s[\"video_rate\"])\n\"\"\", [\"sanity\"])\n\nM(r\"\"\"\nOne session of one resident and intruder pair, 23,810 frames (13.2 min) at 30 Hz, all 14 series on the\nsame rate and starting time. Positions are in pixels and lie within the stated 1024 x 570 image (x 5 to\n991, y 9 to 563). Every confidence value is NaN: the MARS scores that CalMS21 distributes with the pose\nwere not carried into the file, though the NWB field is present. The subject is a dyad stored as one\n`Subject` with sex `U`, strain C57BL/6 only (the BALB/c intruder is not recorded), and age `P0D/`;\n`session_start_time` is 2024-01-01T00:00, a placeholder, since CalMS21 gives no dates.\n\"\"\")\n\nC(r\"\"\"\nbouts = s[\"bouts\"].sort_values(\"start_time\").reset_index(drop=True)\nprint(\"ethogram:\")\nprint(s[\"ethogram\"].to_string(index=False))\nprint(\"\\nannotator attribute:\", repr(s[\"annotator\"]), \"; description:\", s[\"bouts_description\"])\nprint(\"bouts:\", len(bouts), \"; by label:\", bouts.label.value_counts().to_dict())\ngaps = bouts.start_time.values[1:] - bouts.stop_time.values[:-1]\nprint(\"gaps between consecutive bouts (s): min\", gaps.min(), \"max\", gaps.max())\nprint(\"first start\", bouts.start_time.iloc[0], \"; last stop\", round(bouts.stop_time.iloc[-1], 4),\n      \"; frames / 30 =\", round(n / 30, 4))\non_grid = np.abs(bouts[[\"start_time\", \"stop_time\"]].values * 30 - np.round(bouts[[\"start_time\", \"stop_time\"]].values * 30)).max()\nprint(\"largest distance of a bout edge from the 30 Hz frame grid (frames):\", on_grid)\nlabels = calms21.frame_labels(bouts, n)\nprint(\"frames without a label:\", int((labels == \"\").sum()))\nprint(\"frames per label:\", pd.Series(labels).value_counts().to_dict())\ndur = (bouts.stop_time - bouts.start_time)\nprint(\"bout duration (s) by label:\")\nprint(dur.groupby(bouts.label).describe().round(2).to_string())\n\n# The converter's derived series, recomputed from the pose.\ncen = calms21.centroids(kp)\nd_cent = np.hypot(*(cen[:, 0] - cen[:, 1]).T)\npair = kp.mean(axis=(1, 3))\nv_pair = np.r_[np.nan, np.hypot(*np.diff(pair, axis=0).T) * 30]\nv_res = np.r_[np.nan, np.hypot(*np.diff(cen[:, 0], axis=0).T) * 30]\nprint(\"\\ninteranimal_distance minus distance between the two mice's centroids: max |diff|\",\n      np.nanmax(np.abs(d_cent - s[\"interanimal_distance\"])))\nprint(\"centroid_speed minus speed of the mean of all 14 keypoints: max |diff|\",\n      np.nanmax(np.abs(v_pair - s[\"centroid_speed\"])))\nprint(\"centroid_speed minus resident centroid speed: max |diff|\", round(np.nanmax(np.abs(v_res - s[\"centroid_speed\"])), 1))\n\"\"\", [\"sanity\"])\n\nM(r\"\"\"\nThe catalogue lists attack, investigation, mount and other with codes 0 to 3, but its `definition`\ncolumn is empty for all four, though the paper gives definitions (Appendix D.2). The bouts tile the\nsession exactly: no gaps, edges on the 30 Hz frame grid, from 0 to 793.67 s, so each frame gets one\nlabel. This session has no attack. `interanimal_distance` is the distance between the two mice's\ncentroids (mean of seven keypoints each), as described. `centroid_speed` is described as the speed of\n\"the pose centroid (mean over keypoints)\"; it is the speed of the mean of all 14 keypoints, which is the\nmidpoint of the two mice, not the speed of either animal, and the bouts' `mean_speed`, `peak_speed` and\n`immobility_fraction` reduce it. Neither derived series is used below; speeds are computed per mouse.\n\"\"\")\n\nC(r\"\"\"\nstarted = time.time()\nvinfo = calms21.video_info()\nprint(\"video:\", vinfo)\nSTEP = 2  # decode at half resolution\nenergy = np.full(n, np.nan)\npatch_rows = []\nprev = None\nn_decoded = 0\nbody = kp[:, :, :, [3, 4, 5]].mean(axis=3)  # neck and hips: (frames, mouse, x/y)\nfor i, img in calms21.video_frames(every=1, step=STEP):\n    a = img.astype(np.int16)\n    if prev is not None and i < n:\n        energy[i] = np.abs(a - prev).mean()\n    prev = a\n    n_decoded += 1\n    if i % 30 == 0 and i < n:\n        row = {\"frame\": i, \"sep\": float(np.hypot(*(body[i, 0] - body[i, 1])))}\n        for half in (3, 6, 12):  # patch half-widths in full-resolution pixels: 6, 12 and 24 px patches\n            for m, name in enumerate(calms21.MICE):\n                x, y = body[i, m] / STEP\n                h = max(1, half // STEP)\n                xi, yi = int(round(x)), int(round(y))\n                p = img[max(0, yi - h):yi + h, max(0, xi - h):xi + h]\n                row[f\"{name}_{2 * half}\"] = float(p.mean()) if p.size else np.nan\n        patch_rows.append(row)\npatches = pd.DataFrame(patch_rows)\nprint(f\"decoded {n_decoded} frames in {time.time() - started:.0f} s; pose frames {n}\")\n\n# Clock check: video motion energy against the speed of the two mice, over lags.\nv_mice = np.nanmean([calms21.speed(cen[:, 0]), calms21.speed(cen[:, 1])], axis=0)\nok = np.isfinite(energy)\nlags = np.arange(-15, 16)\nxc = [stats.pearsonr(energy[ok][max(0, L):len(energy[ok]) + min(0, L)],\n                     v_mice[ok][max(0, -L):len(v_mice[ok]) - max(0, L)])[0] for L in lags]\nxc = pd.Series(xc, index=lags)\nprint(\"\\ncorrelation of video motion energy with pose speed, by lag (video frame i against pose frame i - lag):\")\nprint(xc.round(3).to_string())\nprint(\"peak at lag\", int(xc.idxmax()), \"frames, r =\", round(xc.max(), 3), \"; at lag 0 r =\", round(xc[0], 3),\n      \"; at lag +-15 r =\", round(xc[-15], 3), round(xc[15], 3))\n\"\"\", [\"sanity\"])\n\nM(r\"\"\"\nThe video is 1024 x 570 at 30 frames per second with 23,810 frames, as many as the pose. Its motion\nenergy follows the speed of the mice most closely at lag 0 (printed above), so the video and the pose\nshare one clock, to within a frame. The patches sampled here are used in resident-is-black.\n\"\"\")\n\nC(r\"\"\"\n# Clock check for the annotations: how well the nose-to-intruder distance separates investigation\n# from other frames, with the labels shifted in time.\nnose_d = calms21.nose_to_intruder(kp)\n\n\ndef auc(score, positive):\n    r = stats.rankdata(score)\n    n1, n0 = positive.sum(), (~positive).sum()\n    return (r[positive].sum() - n1 * (n1 + 1) / 2) / (n1 * n0)\n\n\nshifts = np.r_[np.arange(-300, -30, 30), np.arange(-30, 31, 3), np.arange(60, 301, 30)]\nrows = []\nfor k in shifts:\n    lab = np.roll(labels, k)\n    sel = np.isin(lab, [\"investigation\", \"other\"])\n    if k > 0:\n        sel[:k] = False\n    elif k < 0:\n        sel[k:] = False\n    rows.append({\"shift_frames\": k, \"auc_investigation_vs_other\": auc(-nose_d[sel], lab[sel] == \"investigation\")})\nshift_tab = pd.DataFrame(rows).set_index(\"shift_frames\")\nprint(shift_tab.round(3).T.to_string())\nbest = shift_tab.auc_investigation_vs_other.idxmax()\nprint(\"best shift\", best, \"frames, AUC\", round(shift_tab.auc_investigation_vs_other.max(), 3),\n      \"; at 0\", round(shift_tab.loc[0].iloc[0], 3), \"; at +-300 frames\",\n      round(shift_tab.loc[-300].iloc[0], 3), round(shift_tab.loc[300].iloc[0], 3))\n\"\"\", [\"sanity\"])\n\nM(r\"\"\"\nThe separation of investigation from other frames by the resident's nose distance is highest near zero\nshift and falls off with shifts of seconds, so the annotations share the pose's clock to within the\nprinted resolution (3 frames near zero). This is consistent with the bouts being aligned to the pose;\nit does not resolve offsets of a frame or two.\n\"\"\")\n\nC(r\"\"\"\nstarted = time.time()\nrec = calms21.caltech_record()\nprint(\"CaltechDATA record:\", rec)\nfiles = calms21.caltech_files()\nprint(files.to_string(index=False))\nsummaries = []\nfor (task, split) in calms21.CALMS21_FILES:\n    t0 = time.time()\n    df = calms21.set_summary(task, split)\n    summaries.append(df)\n    print(f\"{task:9s} {split:6s} sequences {len(df):3d} frames {df.n_frames.sum():9d} ({time.time() - t0:.0f} s)\")\nsets = pd.concat(summaries, ignore_index=True)\nprint(f\"streamed all sets in {time.time() - started:.0f} s\")\nlab = sets[sets.task != \"unlabeled\"]\nprint(\"\\nlabelled sequences whose annotation count differs from the frame count in scores:\",\n      int((lab.n_annotations != lab.n_frames).sum()))\nlab_vocab = lab.assign(vocab=lab.vocab.astype(str), annotator=lab.annotator.astype(str))\nprint(\"vocabularies and annotator ids by set:\")\nprint(lab_vocab.groupby([\"task\", \"split\", \"vocab\", \"annotator\"]).size().to_string())\ndup = sets[sets.duplicated(\"kp_hash\", keep=False)].sort_values(\"kp_hash\")\nprint(\"\\nsequences whose keypoints start identically:\", len(dup), \"in\", dup.kp_hash.nunique(), \"groups\")\nif len(dup):\n    groups = dup.groupby(\"kp_hash\").apply(lambda g: \" = \".join(f\"{k} ({f})\" for k, f in zip(g.key, g.n_frames)))\n    print(\"\\n\".join(groups.tolist()[:40]))\n    print(\"groups by the sets they span:\", dup.groupby(\"kp_hash\").apply(\n        lambda g: \" + \".join(sorted(set(g.task + \"/\" + g.split)))).value_counts().to_dict())\n\"\"\", [\"sanity\"])\n\nM(r\"\"\"\nEvery member's decompressed size and CRC matched the zip's directory (the helper checks both). In the\nlabelled sets the length of the annotations equals the number of frames in the scores for every\nsequence. Sequences that start with identical keypoints are listed above; they are the same recording\ndeposited more than once, and dataset-size counts them once under one of its readings.\n\"\"\")\n\n# ---------------- claims on the dandiset ----------------\nM(r\"\"\"\n## format-keypoints\n\n> Each frame holds seven MARS keypoints (nose, left ear, right ear, neck, left hip, right hip, tail\n> base) for each of two mice, the resident (mouse 0) and the intruder (mouse 1), in pixel coordinates\n> of a 1024 x 570 image, at 30 Hz, with a confidence score from 0 to 1 for each keypoint.\n\"\"\")\n\nC(r\"\"\"\nexpected_names = {f\"{m}_{p}\" for m in calms21.MICE for p in calms21.PARTS}\nfound = set(s[\"skeleton_nodes\"])\nprint(\"14 series named for the seven parts of resident and intruder:\", found == expected_names, f\"({len(found)} nodes)\")\nprint(\"units:\", units, \"; rates (Hz):\", rates)\nin_x = (kp[:, :, 0] >= 0) & (kp[:, :, 0] <= calms21.IMAGE_W)\nin_y = (kp[:, :, 1] >= 0) & (kp[:, :, 1] <= calms21.IMAGE_H)\nprint(f\"coordinates within the image: x {in_x.mean():.4f}, y {in_y.mean():.4f} of values\")\nprint(\"pose dimensions stored (rows, cols):\", s[\"pose_dimensions\"], \"; video\", vinfo[\"width\"], \"x\", vinfo[\"height\"])\nfin = np.isfinite(sc)\nprint(f\"confidence values present: {fin.sum()} of {sc.size}\" +\n      (f\"; range {sc[fin].min():.3f} to {sc[fin].max():.3f}\" if fin.any() else \"\"))\npositions_ok = found == expected_names and units == {\"pixels\"} and rates == {30.0} and in_x.all() and in_y.all()\nscores_ok = fin.all() and (sc[fin] >= 0).all() and (sc[fin] <= 1).all()\nprint(\"positions meet the criterion:\", positions_ok, \"; confidence meets it:\", scores_ok)\n\"\"\", [\"claim:format-keypoints\"])\n\nM(r\"\"\"\n**Result: partially reproduced.** The file holds the 14 keypoint series named for the seven parts of\nthe resident and the intruder, in pixels, at 30 Hz, with every coordinate inside the 1024 x 570 image.\nThe confidence field is present for every keypoint but holds no values (0 of 333,340 finite).\n\"\"\")\n\nM(r\"\"\"\n## resident-is-black\n\n> Mouse 0, the resident, is the black C57Bl/6J mouse, and mouse 1, the intruder, is the white BALB/c\n> mouse.\n\"\"\")\n\nC(r\"\"\"\nuse = patches[patches.sep >= 60]\nprint(f\"frames sampled: {len(patches)}; with body centres at least 60 px apart: {len(use)}\")\nfor size in (12, 6, 24):\n    darker = use[f\"resident_{size}\"] < use[f\"intruder_{size}\"]\n    print(f\"patch {size:2d} px: resident darker in {darker.mean():.3f} of frames; median grey resident \"\n          f\"{use[f'resident_{size}'].median():.1f}, intruder {use[f'intruder_{size}'].median():.1f}\")\nfor sep in (30, 120):\n    u = patches[patches.sep >= sep]\n    print(f\"separation >= {sep} px ({len(u)} frames), 12 px patch: resident darker in \"\n          f\"{(u.resident_12 < u.intruder_12).mean():.3f}\")\nby_min = use.assign(minute=use.frame // 1800).groupby(\"minute\").apply(\n    lambda g: pd.Series({\"frames\": len(g), \"resident_darker\": (g.resident_12 < g.intruder_12).mean()}))\nprint(\"\\nby minute of the session (12 px patch):\")\nprint(by_min.round(3).T.to_string())\nfig, ax = plt.subplots(figsize=(5, 4))\nax.scatter(use.intruder_12, use.resident_12, s=6)\nax.plot([0, 255], [0, 255], \"k--\", lw=0.8)\nax.set_xlabel(\"intruder patch grey level\"); ax.set_ylabel(\"resident patch grey level\")\nax.set_xlim(0, 255); ax.set_ylim(0, 255)\nprint(\"grey levels plotted span\", round(use[[\"resident_12\", \"intruder_12\"]].min().min(), 1), \"to\",\n      round(use[[\"resident_12\", \"intruder_12\"]].max().max(), 1), \"(all inside the axes)\")\nplt.show()\n\"\"\", [\"claim:resident-is-black\"])\n\nM(r\"\"\"\n**Result: reproduced.** In the sampled frames where the two mice are apart, the patch on the resident's\nbody is darker than the patch on the intruder's in the fraction printed above, for every patch size and\nseparation threshold, and in every minute of the session. The resident is the dark mouse.\n\"\"\")\n\nM(r\"\"\"\n## task1-vocab\n\n> Task 1 frames are annotated by one annotator (annotator id 0) with exactly one label per frame from\n> the vocabulary attack 0, investigation 1, mount 2 and other 3.\n\"\"\")\n\nC(r\"\"\"\neth = s[\"ethogram\"]\ncodes = dict(zip(eth.behavior, eth.native_code.astype(int)))\nprint(\"catalogue codes:\", codes, \"; equal to the paper's vocabulary:\", codes == calms21.TASK1_VOCAB)\nprint(\"annotator:\", repr(s[\"annotator\"]), \"; annotator id 0:\", s[\"annotator\"].strip().endswith(\" 0\"))\nprint(\"catalogue marked exclusive (one label at a time): see the ndx-ethogram attribute below\")\nuncovered = int((labels == \"\").sum())\nprint(\"frames with no label:\", uncovered, \"of\", n, \"; frames with two labels: 0 (frame_labels raises on overlap)\")\nprint(\"labels used in bouts but not in the catalogue:\", sorted(set(bouts.label) - set(eth.behavior)))\n\"\"\", [\"claim:task1-vocab\"])\n\nM(r\"\"\"\n**Result: reproduced.** The catalogue holds attack, investigation, mount and other with codes 0 to 3,\nthe annotator is given as CalMS21 annotator 0, and every one of the 23,810 frames has exactly one label.\n\"\"\")\n\nM(r\"\"\"\n## task1-video\n\n> The source videos of Task 1 are released, recorded at 30 Hz and 1024 x 570 pixels.\n\"\"\")\n\nC(r\"\"\"\nprint(\"video file:\", s[\"video_external_file\"][0].split(\"/\")[-1])\nprint(f\"size {vinfo['width']} x {vinfo['height']}, {vinfo['rate']} frames/s, {vinfo['frames']} frames \"\n      f\"(decoded {n_decoded}), codec {vinfo['codec']}; pose frames {n}\")\nprint(\"matches 1024 x 570:\", (vinfo[\"width\"], vinfo[\"height\"]) == (1024, 570), \"; 30 Hz:\", vinfo[\"rate\"] == 30.0,\n      \"; same frame count as the pose:\", n_decoded == n)\nmp4 = calms21.zip_members(\"task1_videos_mp4.zip\")\nrow = mp4[mp4.member.str.contains(\"mouse071\")]\nprint(\"\\nCaltechDATA task1_videos_mp4.zip holds\", int(mp4.member.str.endswith(\".mp4\").sum()), \"videos; mouse071:\")\nprint(row.to_string(index=False))\nprint(\"dandiset mp4 size:\", int(assets.set_index(\"path\").loc[calms21.CALMS21_MP4, \"size\"]), \"bytes\")\n\"\"\", [\"claim:task1-video\"])\n\nM(r\"\"\"\n**Result: reproduced.** The dandiset's video of mouse071 is 1024 x 570 at 30 frames per second with as\nmany frames as the pose. It is smaller than CaltechDATA's file for the same sequence (sizes printed\nabove), so it was re-encoded; the two files were not compared frame by frame.\n\"\"\")\n\nM(r\"\"\"\n## contact-during-social-behaviors\n\n> Close investigation, attack and mount are behaviors in which the resident is in close contact with\n> the intruder; other frames include the animals apart.\n\"\"\")\n\nC(r\"\"\"\nrng = np.random.default_rng(101)\nrows = []\nfor name in [\"investigation\", \"attack\", \"mount\"]:\n    sel = labels == name\n    base = np.isin(labels, [name, \"other\"])\n    if not sel.any():\n        rows.append({\"label\": name, \"frames\": 0})\n        continue\n    d, lo, hi = calms21.block_bootstrap_diff(nose_d[base], labels[base] == name, 300, 2000, rng)\n    rows.append({\"label\": name, \"frames\": int(sel.sum()), \"median_px\": np.median(nose_d[sel]),\n                 \"other_median_px\": np.median(nose_d[labels == \"other\"]), \"diff_px\": d, \"ci_lo\": lo, \"ci_hi\": hi})\ncontact = pd.DataFrame(rows)\nprint(\"resident nose to nearest intruder keypoint (pixels):\")\nprint(contact.round(1).to_string(index=False))\nprint(\"\\nquantiles by label (px):\")\nprint(pd.Series(nose_d).groupby(labels).quantile([0.1, 0.5, 0.9]).unstack().round(1).to_string())\n\n# Variants: centroid distance; by half of the session.\nrng_v = np.random.default_rng(102)\nfor name in [\"investigation\", \"mount\"]:\n    base = np.isin(labels, [name, \"other\"])\n    d, lo, hi = calms21.block_bootstrap_diff(d_cent[base], labels[base] == name, 300, 2000, rng_v)\n    print(f\"variant, centroid distance, {name} minus other: {d:.1f} px (95% CI {lo:.1f} to {hi:.1f})\")\nhalf = np.arange(n) < n // 2\nfor h, nm in ((half, \"first half\"), (~half, \"second half\")):\n    med = pd.Series(nose_d[h]).groupby(labels[h]).median().round(1).to_dict()\n    print(f\"{nm}: median nose distance by label {med}\")\nfig, ax = plt.subplots(figsize=(6, 3))\nfor name in [\"other\", \"investigation\", \"mount\"]:\n    ax.hist(nose_d[labels == name], bins=np.arange(0, 600, 10), histtype=\"step\", density=True, label=name)\nax.set_xlabel(\"resident nose to intruder (px)\"); ax.legend()\nprint(\"frames beyond 600 px (outside the axes):\", int((nose_d > 600).sum()), \"; max\", round(nose_d.max(), 1))\nplt.show()\n\"\"\", [\"claim:contact-during-social-behaviors\"])\n\nM(r\"\"\"\n**Result: reproduced.** In investigation and mount frames the resident's nose is much closer to the\nintruder than in other frames, with bootstrap intervals that exclude 0 (printed above), and the same\nholds for the centroid distance and in each half of the session. Attack does not occur in this session\nand is untested.\n\"\"\")\n\nM(r\"\"\"\n## pose-errors-close-fast\n\n> Errors in pose estimation are most common on frames when the two animals are in close contact or\n> moving very quickly.\n\"\"\")\n\nC(r\"\"\"\nrng = np.random.default_rng(201)\nSEGMENTS = {\"nose-neck\": (0, 3), \"neck-tail\": (3, 6), \"ear-ear\": (1, 2), \"hip-hip\": (4, 5)}\nlengths = {(m, seg): np.hypot(*(kp[:, m, :, a] - kp[:, m, :, b]).T)\n           for m in (0, 1) for seg, (a, b) in SEGMENTS.items()}\n\n\ndef error_flags(factor):\n    flags = np.zeros(n, bool)\n    for v in lengths.values():\n        q1, q3 = np.percentile(v, [25, 75])\n        flags |= (v < q1 - factor * (q3 - q1)) | (v > q3 + factor * (q3 - q1))\n    return flags\n\n\nv_fast = np.maximum(pd.Series(calms21.speed(cen[:, 0])).rolling(15, center=True, min_periods=1).median().values,\n                    pd.Series(calms21.speed(cen[:, 1])).rolling(15, center=True, min_periods=1).median().values)\n\n\ndef test(err, q, stat=np.mean):\n    out = {}\n    close = d_cent <= np.quantile(d_cent, q)\n    fast = v_fast >= np.quantile(v_fast, 1 - q)\n    for nm, g in ((\"close\", close), (\"fast\", fast)):\n        d, lo, hi = calms21.block_bootstrap_diff(err.astype(float), g, 300, 2000, rng, stat=stat)\n        out[nm] = (err[g].mean(), err[~g].mean(), d, lo, hi)\n    return out\n\n\nerr = error_flags(3.0)\nprint(f\"frames flagged as pose errors (factor 3): {err.sum()} of {n} ({err.mean():.4f})\")\nprint(\"per segment and mouse:\", {f\"{calms21.MICE[m]} {seg}\": int(((v < np.percentile(v, 25) - 3 * np.subtract(*np.percentile(v, [75, 25]))) |\n      (v > np.percentile(v, 75) + 3 * np.subtract(*np.percentile(v, [75, 25])))).sum()) for (m, seg), v in lengths.items()})\nprint(\"close threshold (10%):\", round(np.quantile(d_cent, 0.1), 1), \"px; fast threshold (90%):\",\n      round(np.quantile(v_fast, 0.9), 1), \"px/s\")\nrows = []\nfor factor in (3.0, 1.5):\n    e = error_flags(factor)\n    for q in (0.10, 0.05, 0.20):\n        res = test(e, q)\n        for nm, (a, b, d, lo, hi) in res.items():\n            rows.append({\"factor\": factor, \"fraction\": q, \"group\": nm, \"error_in_group\": a, \"error_elsewhere\": b,\n                         \"diff\": d, \"ci_lo\": lo, \"ci_hi\": hi})\nerrtab = pd.DataFrame(rows)\nprint(\"\\nerror fraction in close / fast frames against the rest (main: factor 3, fraction 0.10):\")\nprint(errtab.round(4).to_string(index=False))\nby_label = pd.Series(err).groupby(labels).mean()\nprint(\"\\nerror fraction by annotation label:\", by_label.round(4).to_dict())\n\"\"\", [\"claim:pose-errors-close-fast\"])\n\nM(r\"\"\"\n**Result: reproduced.** With the main settings, frames with an implausible body length are more common\nwhen the mice are closest and when they move fastest, both with bootstrap intervals above 0 (printed\nabove). The direction holds for every variant threshold and factor shown. The error measure is a proxy\nchosen here, and the fast frames' speeds come from the same keypoints, so part of the fast effect may be\nerrors producing apparent speed.\n\"\"\")\n\n# ---------------- link ----------------\nM(r\"\"\"\n## link-mouse071\n\n> The dandiset's CalMS21 sequence is the CalMS21 Task 1 test sequence mouse071, with the same\n> keypoints, confidence scores and frame annotations.\n\"\"\")\n\nC(r\"\"\"\nstarted = time.time()\nref = calms21.caltech_sequence(\"task1\", \"test\", \"mouse071_task1_annotator1\")\nref_kp = np.asarray(ref[\"keypoints\"], float)\nref_sc = np.asarray(ref[\"scores\"], float)\nref_ann = np.asarray(ref[\"annotations\"])\nprint(f\"CaltechDATA {ref['key']} loaded in {time.time() - started:.0f} s; metadata {ref['metadata']}\")\nprint(\"dandiset session:\", s[\"session_id\"], \"; frames dandiset\", n, \"CaltechDATA\", len(ref_kp))\nprint(\"shapes:\", kp.shape, ref_kp.shape)\ndiff = np.abs(kp - ref_kp)\nprint(f\"keypoints: max |diff| {diff.max():.3g} px; fraction of coordinates within 0.001 px {np.mean(diff <= 1e-3):.6f}\")\n# Order checks: would swapping mice, axes or left/right parts fit better?\nprint(\"max |diff| with mice swapped:\", round(np.abs(kp - ref_kp[:, ::-1]).max(), 1),\n      \"; with x and y swapped:\", round(np.abs(kp - ref_kp[:, :, ::-1]).max(), 1))\ncode_of = dict(zip(s[\"ethogram\"].behavior, s[\"ethogram\"].native_code.astype(int)))\ndandi_codes = np.array([code_of[x] for x in labels])\nagree = dandi_codes == ref_ann\nprint(f\"frame labels agree on {agree.sum()} of {n} frames ({agree.mean():.6f})\")\nprint(\"CaltechDATA label counts:\", dict(zip(*np.unique(ref_ann, return_counts=True))),\n      \"; dandiset:\", dict(zip(*np.unique(dandi_codes, return_counts=True))))\nif (~agree).any():\n    print(\"first disagreeing frames:\", np.flatnonzero(~agree)[:20])\nprint(f\"\\nconfidence: CaltechDATA range {ref_sc.min():.3f} to {ref_sc.max():.3f}, median {np.median(ref_sc):.3f}, \"\n      f\"finite {np.isfinite(ref_sc).sum()} of {ref_sc.size}; dandiset finite {np.isfinite(sc).sum()}\")\n\"\"\", [\"claim:link-mouse071\"])\n\nM(r\"\"\"\n**Result: reproduced.** The sequence matches by name, has the same 23,810 frames, and every keypoint\ncoordinate equals CaltechDATA's within 0.001 pixel in the stated order of mice, axes and parts (swapping\nmice or axes gives large differences). The frame labels from the bouts agree with CaltechDATA's\nannotations on every frame. CaltechDATA's confidence scores (0 to 1) have no counterpart in the\ndandiset, whose confidence values are all NaN.\n\"\"\")\n\nM(r\"\"\"\n## pose-errors-close-fast-confidence\n\n> Errors in pose estimation are most common on frames when the two animals are in close contact or\n> moving very quickly, as shown by the MARS confidence scores.\n\"\"\")\n\nC(r\"\"\"\nrng = np.random.default_rng(301)\nconf = ref_sc.mean(axis=(1, 2))  # mean over 14 keypoints, from CaltechDATA, matched by frame index\nprint(f\"mean confidence per frame: median {np.median(conf):.3f}, range {conf.min():.3f} to {conf.max():.3f}\")\nrows = []\nfor q in (0.10, 0.05, 0.20):\n    close = d_cent <= np.quantile(d_cent, q)\n    fast = v_fast >= np.quantile(v_fast, 1 - q)\n    for nm, g in ((\"close\", close), (\"fast\", fast)):\n        d, lo, hi = calms21.block_bootstrap_diff(conf, g, 300, 2000, rng)\n        rows.append({\"fraction\": q, \"group\": nm, \"median_in_group\": np.median(conf[g]),\n                     \"median_elsewhere\": np.median(conf[~g]), \"diff\": d, \"ci_lo\": lo, \"ci_hi\": hi})\nctab = pd.DataFrame(rows)\nprint(ctab.round(4).to_string(index=False))\nper_mouse = {name: {\"close\": np.median(ref_sc[d_cent <= np.quantile(d_cent, 0.1), m].mean(axis=1)) -\n                    np.median(ref_sc[d_cent > np.quantile(d_cent, 0.1), m].mean(axis=1))}\n             for m, name in enumerate(calms21.MICE)}\nprint(\"variant, per mouse, median confidence close minus rest (10%):\", {k: round(v[\"close\"], 4) for k, v in per_mouse.items()})\nprint(\"correlation of confidence with the error flags of pose-errors-close-fast:\",\n      round(stats.pointbiserialr(err, conf)[0], 3))\nfig, ax = plt.subplots(1, 2, figsize=(9, 3))\nax[0].scatter(d_cent[::10], conf[::10], s=2); ax[0].set_xlabel(\"centroid distance (px)\"); ax[0].set_ylabel(\"mean confidence\")\nax[1].scatter(v_fast[::10], conf[::10], s=2); ax[1].set_xlabel(\"faster mouse speed (px/s)\")\nax[1].set_xlim(0, 1500)\nprint(\"every 10th frame plotted; frames above 1500 px/s (outside the right axes):\", int((v_fast[::10] > 1500).sum()))\nplt.show()\n\"\"\", [\"claim:pose-errors-close-fast-confidence\"])\n\nM(r\"\"\"\n**Result: reproduced.** The MARS confidence is lower in the closest frames and in the fastest frames\nthan in the rest, with bootstrap intervals that exclude 0 at the main threshold (printed above).\n\"\"\")\n\n# ---------------- elsewhere ----------------\nM(r\"\"\"\n## table5-task1-counts\n\n> Task 1 has 70 training sequences with 507,738 frames and 19 test sequences with 262,107 frames.\n\"\"\")\n\nC(r\"\"\"\nPAPER_T5_TASK1 = {\"train\": (507738, 70), \"test\": (262107, 19)}\nt1 = sets[sets.task == \"task1\"]\nrows = []\nfor split, (frames, seqs) in PAPER_T5_TASK1.items():\n    g = t1[t1.split == split]\n    rows.append({\"split\": split, \"frames\": int(g.n_annotations.sum()), \"paper_frames\": frames,\n                 \"sequences\": len(g), \"paper_sequences\": seqs})\nt5_1 = pd.DataFrame(rows)\nprint(t5_1.to_string(index=False))\nmatch = (t5_1.frames == t5_1.paper_frames) & (t5_1.sequences == t5_1.paper_sequences)\nprint(\"all four counts match:\", bool(match.all()))\nprint(\"Task 1 sequence length (s): min\", round(t1.n_frames.min() / 30, 1), \"median\", round(t1.n_frames.median() / 30, 1),\n      \"max\", round(t1.n_frames.max() / 30, 1))\nprint(\"mouse071 in the test split:\", bool((t1.key == \"task1/test/mouse071_task1_annotator1\").any()))\n\"\"\", [\"claim:table5-task1-counts\"])\n\nM(r\"\"\"\n**Result: reproduced.** The training and test files hold the reported numbers of sequences and frames.\n\"\"\")\n\n\ndef count_claim(task, paper_name, group_fn, tag):\n    return None\n\n\nM(r\"\"\"\n## table5-task2-counts\n\n> Task 2 has, for annotators 1 to 5, 6 training sequences each with 139,112, 135,623, 107,420, 108,325\n> and 92,383 frames, and 13, 6, 4, 4 and 20 test sequences with 286,810, 150,919, 77,079, 76,174 and\n> 364,007 frames.\n\"\"\")\n\nC(r\"\"\"\nPAPER_T5_TASK2 = {  # annotator: (train frames, train sequences, test frames, test sequences)\n    1: (139112, 6, 286810, 13), 2: (135623, 6, 150919, 6), 3: (107420, 6, 77079, 4),\n    4: (108325, 6, 76174, 4), 5: (92383, 6, 364007, 20)}\nt2 = sets[sets.task == \"task2\"].copy()\nt2[\"group\"] = t2.key.str.extract(r\"task2/annotator(\\d)/\")[0].astype(int)\nprint(\"annotator id in the metadata equals the one in the key:\", bool((t2.annotator.astype(int) == t2.group).all()))\n\n\ndef count_table(df, paper):\n    rows = []\n    for g, (trf, trs, tef, tes) in paper.items():\n        for split, pf, ps in ((\"train\", trf, trs), (\"test\", tef, tes)):\n            sub = df[(df.group == g) & (df.split == split)]\n            rows.append({\"group\": g, \"split\": split, \"frames\": int(sub.n_annotations.sum()), \"paper_frames\": pf,\n                         \"sequences\": len(sub), \"paper_sequences\": ps})\n    t = pd.DataFrame(rows)\n    t[\"frames_rel_diff\"] = (t.frames - t.paper_frames) / t.paper_frames\n    return t\n\n\nt5_2 = count_table(t2, PAPER_T5_TASK2)\nprint(t5_2.to_string(index=False))\nexact = int((t5_2.frames == t5_2.paper_frames).sum() + (t5_2.sequences == t5_2.paper_sequences).sum())\nwithin = bool((t5_2.frames_rel_diff.abs() <= 0.1).all() and\n              ((t5_2.sequences - t5_2.paper_sequences).abs() <= 0.1 * t5_2.paper_sequences).all())\nprint(f\"counts matching exactly: {exact} of {2 * len(t5_2)}; all within 10%: {within}\")\n\"\"\", [\"claim:table5-task2-counts\"])\n\nM(r\"\"\"\n**Result: reproduced.** Every Task 2 count of frames and sequences matches the table.\n\"\"\")\n\nM(r\"\"\"\n## table5-task3-counts\n\n> Task 3 has, for approach, disengaged, grooming, intromission, mount attempt, sniff face and white\n> rearing, 3, 2, 2, 1, 4, 3 and 2 training sequences with 20,624, 35,751, 45,174, 19,200, 46,847, 19,244\n> and 36,181 frames, and 25, 1, 13, 10, 12, 47 and 1 test sequences with 126,468, 19,088, 156,664,\n> 55,218, 85,836, 251,793 and 17,939 frames.\n\"\"\")\n\nC(r\"\"\"\nPAPER_T5_TASK3 = {\n    \"approach\": (20624, 3, 126468, 25), \"disengaged\": (35751, 2, 19088, 1), \"groom\": (45174, 2, 156664, 13),\n    \"intromission\": (19200, 1, 55218, 10), \"mount_attempt\": (46847, 4, 85836, 12),\n    \"sniff_face\": (19244, 3, 251793, 47), \"whiterearing\": (36181, 2, 17939, 1)}\nt3 = sets[sets.task == \"task3\"].copy()\nt3[\"group\"] = t3.key.str.extract(r\"task3/([a-z_]+)/\")[0]\nprint(\"behaviors in the files:\", sorted(t3.group.unique()))\nprint(\"vocabulary of each sequence names its behavior with code 1:\",\n      bool(all(v.get(g) == 1 and v.get(\"other\") == 0 for v, g in zip(t3.vocab, t3.group))))\nt5_3 = count_table(t3, PAPER_T5_TASK3)\nprint(t5_3.to_string(index=False))\nexact = int((t5_3.frames == t5_3.paper_frames).sum() + (t5_3.sequences == t5_3.paper_sequences).sum())\nwithin = bool((t5_3.frames_rel_diff.abs() <= 0.1).all() and\n              ((t5_3.sequences - t5_3.paper_sequences).abs() <= 0.1 * t5_3.paper_sequences).all())\nprint(f\"counts matching exactly: {exact} of {2 * len(t5_3)}; all within 10%: {within}\")\n\"\"\", [\"claim:table5-task3-counts\"])\n\nM(r\"\"\"\n**Result: reproduced.** Every Task 3 count of frames and sequences matches the table.\n\"\"\")\n\nM(r\"\"\"\n## table6-task1-label-fractions\n\n> In the Task 1 training set, 2.76% of frames are labelled attack, 28.9% investigation, 5.64% mount and\n> 62.7% other.\n\"\"\")\n\nC(r\"\"\"\nPAPER_T6 = {\"attack\": (2.76, 0.005), \"investigation\": (28.9, 0.05), \"mount\": (5.64, 0.005), \"other\": (62.7, 0.05)}\n\n\ndef label_percent(df, vocab):\n    tot = {}\n    for counts in df.counts:\n        for c, k in counts.items():\n            tot[c] = tot.get(c, 0) + k\n    allf = sum(tot.values())\n    return {name: 100 * tot.get(code, 0) / allf for name, code in vocab.items()}, allf\n\n\nrows = []\nfor reading, splits in ((\"a: train\", [\"train\"]), (\"b: train+test\", [\"train\", \"test\"])):\n    pct, allf = label_percent(t1[t1.split.isin(splits)], calms21.TASK1_VOCAB)\n    for name, (val, tol) in PAPER_T6.items():\n        rows.append({\"reading\": reading, \"label\": name, \"percent\": pct[name], \"paper\": val, \"tolerance\": tol,\n                     \"within\": abs(pct[name] - val) <= tol, \"within_10pct\": abs(pct[name] - val) <= 0.1 * val})\nt6 = pd.DataFrame(rows)\nprint(t6.round(4).to_string(index=False))\nprint(t6.groupby(\"reading\")[[\"within\", \"within_10pct\"]].all().to_string())\n\"\"\", [\"claim:table6-task1-label-fractions\"])\n\nM(r\"\"\"\n**Result: reproduced.** Under reading (a), the training split, all four percentages are within half a\nunit of the last reported digit.\n\"\"\")\n\nM(r\"\"\"\n## fig4b-task2-label-fractions\n\n> The five Task 2 annotators label different fractions of frames as other, investigation, mount and\n> attack (annotator 1 60.0, 20.6, 16.2 and 3.2%; annotator 2 65.5, 25.8, 3.4 and 5.3%; annotator 3\n> 68.9, 13.5, 9.5 and 8.1%; annotator 4 75.2, 11.6, 4.5 and 8.7%; annotator 5 69.5, 26.4, 1.0 and 3.0%).\n\"\"\")\n\nC(r\"\"\"\nORDER = [\"other\", \"investigation\", \"mount\", \"attack\"]\nPAPER_F4B_T2 = {1: (60.0, 20.6, 16.2, 3.2), 2: (65.5, 25.8, 3.4, 5.3), 3: (68.9, 13.5, 9.5, 8.1),\n                4: (75.2, 11.6, 4.5, 8.7), 5: (69.5, 26.4, 1.0, 3.0)}\nTOL = 0.05\nresults = {}\nfor split_reading, splits in ((\"a: train\", [\"train\"]), (\"b: train+test\", [\"train\", \"test\"])):\n    rows = []\n    for a, paper in PAPER_F4B_T2.items():\n        pct, _ = label_percent(t2[(t2.group == a) & t2.split.isin(splits)], calms21.TASK1_VOCAB)\n        mine = np.array([pct[c] for c in ORDER])\n        best = np.sort(mine)[np.argsort(np.argsort(paper))]  # sorted matching minimises the largest deviation\n        rows.append({\"annotator\": a, **{c: round(v, 2) for c, v in zip(ORDER, mine)}, \"paper\": paper,\n                     \"within_i\": int((np.abs(mine - paper) <= TOL).sum()),\n                     \"within_ii\": int((np.abs(best - paper) <= TOL).sum())})\n    tab = pd.DataFrame(rows)\n    results[split_reading] = tab\n    print(f\"reading {split_reading}:\")\n    print(tab.to_string(index=False))\n    print(f\"  values within {TOL}: class order (i) {tab.within_i.sum()} of 20, best assignment (ii) {tab.within_ii.sum()} of 20\\n\")\n\"\"\", [\"claim:fig4b-task2-label-fractions\"])\n\nM(r\"\"\"\n**Result: reproduced.** Under the training split with the class order of the Task 1 pie, all 20\npercentages are within 0.05 of the figure's values.\n\"\"\")\n\nM(r\"\"\"\n## table7-task3-label-fractions\n\n> In Task 3 the behaviors occupy 3.25% (approach), 1.47% (disengaged), 14.0% (groom), 19.3%\n> (intromission), 0.90% (mount attempt), 4.74% (sniff face) and 9.29% (white rearing) of frames.\n\"\"\")\n\nC(r\"\"\"\nPAPER_T7 = {\"approach\": (3.25, 0.005), \"disengaged\": (1.47, 0.005), \"groom\": (14.0, 0.05), \"intromission\": (19.3, 0.05),\n            \"mount_attempt\": (0.90, 0.005), \"sniff_face\": (4.74, 0.005), \"whiterearing\": (9.29, 0.005)}\nrows = []\nfor reading, splits in ((\"a: train\", [\"train\"]), (\"b: train+test\", [\"train\", \"test\"])):\n    for b, (val, tol) in PAPER_T7.items():\n        pct, _ = label_percent(t3[(t3.group == b) & t3.split.isin(splits)], {b: 1, \"other\": 0})\n        rows.append({\"reading\": reading, \"behavior\": b, \"percent\": pct[b], \"paper\": val, \"tolerance\": tol,\n                     \"within\": abs(pct[b] - val) <= tol, \"within_10pct\": abs(pct[b] - val) <= 0.1 * val})\nt7 = pd.DataFrame(rows)\nprint(t7.round(4).to_string(index=False))\nprint(t7.groupby(\"reading\")[[\"within\", \"within_10pct\"]].all().to_string())\n\"\"\", [\"claim:table7-task3-label-fractions\"])\n\nM(r\"\"\"\n**Result: reproduced.** Under reading (a), the training split, all seven percentages are within\ntolerance.\n\"\"\")\n\nM(r\"\"\"\n## dataset-size\n\n> The unlabeled set has 282 videos and about 6 million frames; the dataset holds over 1 million\n> annotated frames, over 70 hours of tracked poses and over 10 hours of frame-by-frame annotation.\n\"\"\")\n\nC(r\"\"\"\nunl = sets[sets.task == \"unlabeled\"]\nprint(f\"unlabeled: {len(unl)} sequences, {unl.n_frames.sum():,} frames ({unl.n_frames.sum() / 30 / 3600:.1f} h)\")\nlabelled = sets[sets.task != \"unlabeled\"]\nonce = sets.drop_duplicates(\"kp_hash\")\nreadings = {\n    \"a: Task 1\": sets[sets.task == \"task1\"],\n    \"b: all labelled\": labelled,\n    \"c: all labelled, duplicates once\": once[once.task != \"unlabeled\"],\n}\nrows = []\nfor nm, df in readings.items():\n    ann = df.n_frames.sum()\n    unl_part = unl if not nm.startswith(\"c\") else once[once.task == \"unlabeled\"]\n    pose = ann + unl_part.n_frames.sum()\n    rows.append({\"reading\": nm, \"annotated_frames\": ann, \"annotated_hours\": ann / 30 / 3600,\n                 \"pose_frames\": pose, \"pose_hours\": pose / 30 / 3600})\nsize = pd.DataFrame(rows)\nprint(size.round(2).to_string(index=False))\nprint(\"\\nover 1 million annotated frames under:\", size.reading[size.annotated_frames > 1e6].tolist())\nprint(\"over 10 hours of annotation under:\", size.reading[size.annotated_hours > 10].tolist())\nprint(\"over 70 hours of pose under:\", size.reading[size.pose_hours > 70].tolist())\nprint(\"282 unlabeled sequences:\", len(unl) == 282, \"; frames within 6 million +- 10%:\", abs(unl.n_frames.sum() - 6e6) <= 6e5)\n\"\"\", [\"claim:dataset-size\"])\n\nM(r\"\"\"\n**Result: reproduced.** The unlabeled set has 282 sequences and close to 6 million frames, and each of\nthe three \"over\" statements holds under at least one reading (printed above).\n\"\"\")\n\nM(r\"\"\"\n## table10-task3-difficulty\n\n> On Task 3, classifier performance depends on the percentage of frames in which a behavior is observed\n> and on its average bout duration, with shorter bouts giving lower performance.\n\"\"\")\n\nC(r\"\"\"\nBEHAVIORS = [\"approach\", \"disengaged\", \"groom\", \"intromission\", \"mount_attempt\", \"sniff_face\", \"whiterearing\"]\nF1_BASELINE = [0.338, 0.195, 0.289, 0.721, 0.034, 0.358, 0.430]  # Table 10, baseline\nF1_TASKPROG = [0.310, 0.198, 0.409, 0.609, 0.048, 0.274, 0.430]  # Table 10, baseline with task programming\n\n\ndef exact_spearman(x, y):\n    # One-sided exact permutation p of Spearman's rho being at least the observed value.\n    rx, ry = stats.rankdata(x), stats.rankdata(y)\n    rho = stats.spearmanr(x, y)[0]\n    perms = [stats.spearmanr(rx, np.array(p))[0] for p in itertools.permutations(ry)]\n    return rho, float(np.mean(np.array(perms) >= rho - 1e-12))\n\n\nrows, feats = [], {}\nfor split in (\"train\", \"test\"):\n    pct, bout = [], []\n    for b in BEHAVIORS:\n        g = t3[(t3.group == b) & (t3.split == split)]\n        p, _ = label_percent(g, {b: 1, \"other\": 0})\n        runs = [r for d in g.runs for r in d.get(1, [])]\n        pct.append(p[b]); bout.append(np.mean(runs) if runs else np.nan)\n    feats[split] = pd.DataFrame({\"percent_frames\": pct, \"mean_bout_frames\": bout}, index=BEHAVIORS)\n    for f1_name, f1 in ((\"baseline\", F1_BASELINE), (\"task programming\", F1_TASKPROG)):\n        for feat in (\"percent_frames\", \"mean_bout_frames\"):\n            rho, p = exact_spearman(feats[split][feat].values, f1)\n            rows.append({\"split\": split, \"F1\": f1_name, \"feature\": feat, \"rho\": rho, \"p_one_sided\": p})\nfor split, f in feats.items():\n    print(f\"{split} split:\")\n    print(f.assign(F1_baseline=F1_BASELINE).round(3).to_string())\ncorr = pd.DataFrame(rows)\nprint(\"\\nSpearman correlations across the seven behaviors (exact one-sided permutation p):\")\nprint(corr.round(3).to_string(index=False))\n\"\"\", [\"claim:table10-task3-difficulty\"])\n\nM(r\"\"\"\n**Result: see the summary.** (Filled in after the run.)\n\"\"\")\n\nM(r\"\"\"\n## Summary\n\n(Filled in after the run.)\n\"\"\")\n\nC(r\"\"\"\nprint(f\"notebook ran in {(time.time() - started_all) / 60:.1f} min\")\n\"\"\")\n\nnb = nbformat.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnb.metadata[\"language_info\"] = {\"name\": \"python\"}\nnbformat.write(nb, \"entries/001878-sun-2021/reproduce_sun_2021.ipynb\")\nprint(\"written\", len(cells), \"cells\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/build_nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='build_nb.py'; t=open(p).read()
t=t.replace('''def count_claim(task, paper_name, group_fn, tag):
    return None


''','')
t=t.replace('''print("catalogue marked exclusive (one label at a time): see the ndx-ethogram attribute below")
''','')
open(p,'w').write(t)
EOF
python build_nb.py 2>&1 || $TMPDIR/wk/bin/python build_nb.py; uv pip install -q --python $TMPDIR/wk/bin/python nbconvert ipykernel matplotlib 2>&1 | tail -1
```

```
written 65 cells
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/001878-sun-2021 && $TMPDIR/wk/bin/python -m ipykernel install --user --name wk >/dev/null 2>&1; time $TMPDIR/wk/bin/python -m jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3600 --ExecutePreprocessor.kernel_name=wk --output-dir $TMPDIR/out reproduce_sun_2021.ipynb 2>&1 | tail -30
```

```
[NbConvertApp] Making directory /tmp/claude-1001/out
[NbConvertApp] Converting notebook reproduce_sun_2021.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 238790 bytes to /tmp/claude-1001/out/reproduce_sun_2021.ipynb

real	2m45.550s
user	2m54.193s
sys	0m12.532s
```

**Agent**

Ran in under 3 minutes. Reading the outputs.

**Agent calls Bash**

```bash
cd $TMPDIR && $TMPDIR/wk/bin/python -c "
import nbformat
nb=nbformat.read('out/reproduce_sun_2021.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    print('=== cell',i,c.metadata.get('tags'))
    for o in c.outputs:
        if 'text' in o: print(o['text'][:6000])
        elif o.get('output_type')=='error': print('ERROR', o['ename'], o['evalue'])
        elif 'data' in o and 'text/plain' in o['data']: print(o['data']['text/plain'][:3000])
"
```

```
=== cell 1 None
loaded sub-mouse071-resident-intruder/sub-mouse071-resident-intruder_ses-mouse071-task1_image.nwb from dandiset 001878 version draft in 5 s

=== cell 3 ['sanity']
Draft modified: 2026-06-25T18:32:10.096594Z ; recorded when written: 2026-06-25T18:32:10.096594Z
Published version: None


6 assets:
                                                                                                                                           path      size                                 blob
                  sub-mlost-batch2-1-mouse/sub-mlost-batch2-1-mouse_ses-batch2-1_image/4ce9fc13-9b37-48d8-9549-7eed9adcf184_external_file_0.mp4   4187160 6965313b-b732-42ba-a099-158827af0355
                                                     sub-mouse071-resident-intruder/sub-mouse071-resident-intruder_ses-mouse071-task1_image.nwb   6717539 e169899a-5a31-44d1-aa7a-93c33e5d3e73
                                                        sub-mouse-21-11-8-one-mouse/sub-mouse-21-11-8-one-mouse_ses-21-11-8-one-mouse_image.nwb   6923382 7c872f72-1ea9-4cab-aa71-698e0a6a9895
                                                                       sub-mlost-batch2-1-mouse/sub-mlost-batch2-1-mouse_ses-batch2-1_image.nwb   3552734 eaab5c37-7a7f-4b65-864d-f2986df5d64e
   sub-mouse-21-11-8-one-mouse/sub-mouse-21-11-8-one-mouse_ses-21-11-8-one-mouse_image/b9338a74-9eb3-4458-80ae-8d804d82969d_external_file_0.mp4  23614309 83c83d37-a3c0-4022-a32f-cfc646140637
sub-mouse071-resident-intruder/sub-mouse071-resident-intruder_ses-mouse071-task1_image/304bc772-9d15-41a5-80bd-bc57dcd5c9b9_external_file_0.mp4 184059454 73781d39-da5a-41c9-9f25-9e009ca260d1
pinned blob unchanged: sub-mouse071-resident-intruder_ses-mouse071-task1_image.nwb True
pinned blob unchanged: 304bc772-9d15-41a5-80bd-bc57dcd5c9b9_external_file_0.mp4 True


[... 439 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001878-sun-2021 && python - <<'EOF'
p='calms21.py'; t=open(p).read()
t=t.replace('''    if pos["keypoints"] >= 0:
        out["keypoints_head"] = text[pos["keypoints"]:pos["keypoints"] + 20000].translate(None, b" \\n\\r\\t")[:3000]
    return out''','''    if pos["keypoints"] >= 0:
        k = field("keypoints").translate(None, b" \\n\\r\\t")
        out["keypoints_head"] = k[:3000]
        out["keypoints_sha1"] = hashlib.sha1(k).hexdigest()
    return out''')
t=t.replace('''    out = {"n_frames": field("scores").translate(None, b" \\n\\r\\t").count(b"]]"),
           "annotations": None, "metadata": None, "keypoints_head": None}''','''    out = {"n_frames": field("scores").translate(None, b" \\n\\r\\t").count(b"]]"),
           "annotations": None, "metadata": None, "keypoints_head": None, "keypoints_sha1": None}''')
t=t.replace('''    non-overlapping "]]"). `keypoints_head` is the start of the keypoints field without whitespace,
    used to find sequences deposited twice.''','''    non-overlapping "]]"). `keypoints_sha1` is a hash of the whole keypoints field without
    whitespace, used to find sequences deposited more than once; `keypoints_head` is its start.''')
t=t.replace('''    import hashlib
    zip_name, member = CALMS21_FILES[(task, split)]''','''    zip_name, member = CALMS21_FILES[(task, split)]''')
t=t.replace('''        row = {"task": task, "split": split, "key": key, "n_frames": s["n_frames"],
               "kp_hash": hashlib.sha1(s["keypoints_head"]).hexdigest() if s["keypoints_head"] else None}''','''        row = {"task": task, "split": split, "key": key, "n_frames": s["n_frames"],
               "kp_hash": s["keypoints_sha1"]}''')
t=t.replace("import io\nimport json","import hashlib\nimport io\nimport json")
t=t.replace('''    """One row per sequence of a CalMS21 set: frames, frames per annotation code, the runs of each
    code, the vocabulary and annotator, and a hash of the start of the keypoints (to find
    sequences deposited twice)."""''','''    """One row per sequence of a CalMS21 set: frames, frames per annotation code, the runs of each
    code, the vocabulary and annotator, and a hash of the keypoints (to find sequences deposited
    more than once)."""''')
open(p,'w').write(t)
EOF
grep -n "keypoints_sha1\|kp_hash\|import hashlib" calms21.py; time $TMPDIR/wk/bin/python -c "
import calms21 as c, pandas as pd
d=pd.concat([c.set_summary('task1','train'), c.set_summary('task3','test'), c.set_summary('task3','train'), c.set_summary('task1','test')])
t1=d[(d.task=='task1')&(d.split=='train')]
att=sum(x.get(0,0) for x in t1.counts); print(att, t1.n_annotations.sum(), repr(100*att/t1.n_annotations.sum()))
dup=d[d.duplicated('kp_hash',keep=False)]; print(len(dup), dup.kp_hash.nunique())
"
```

```
28:import hashlib
386:               "kp_hash": s["keypoints_sha1"]}
421:    non-overlapping "]]"). `keypoints_sha1` is a hash of the whole keypoints field without
435:           "annotations": None, "metadata": None, "keypoints_head": None, "keypoints_sha1": None}
445:        out["keypoints_sha1"] = hashlib.sha1(k).hexdigest()
14039 507738 np.float64(2.7650087249723283)
182 68

real	0m23.392s
user	0m18.809s
sys	0m2.814s
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='build_nb.py'; t=open(p).read()
old=t[t.index('dup = sets[sets.duplicated("kp_hash", keep=False)]'):t.index('""", ["sanity"])', t.index('dup = sets[sets.duplicated("kp_hash", keep=False)]'))]
new='''dup = sets[sets.duplicated("kp_hash", keep=False)].copy()
dup["set"] = dup.task + "/" + dup.split
groups = dup.groupby("kp_hash")
print(f"\\nsequences with identical keypoints (whole field): {len(dup)}, in {groups.ngroups} groups; "
      f"distinct recordings over all sets: {sets.kp_hash.nunique()} of {len(sets)} sequences")
print("groups by the sets they span:")
print(groups.set.apply(lambda g: " + ".join(sorted(set(g)))).value_counts().to_string())
frames_same = groups.n_frames.nunique().eq(1).all()
print("frame counts equal within every group:", bool(frames_same))
cross = groups.apply(lambda g: sorted(set(g.set)), include_groups=False)
leak = [h for h, sl in cross.items() if any(a.split("/")[0] == b.split("/")[0] and a != b for a in sl for b in sl)]
print("\\ngroups that span the training and test split of one task:", len(leak))
for h in leak:
    print("  " + " = ".join(dup[dup.kp_hash == h].key))
t1test_in_t3train = dup[dup.kp_hash.isin(dup[dup.set == "task1/test"].kp_hash) & (dup.set == "task3/train")]
t1train_in_t3test = dup[dup.kp_hash.isin(dup[dup.set == "task1/train"].kp_hash) & (dup.set == "task3/test")]
print("Task 3 training sequences that are Task 1 test sequences:", len(t1test_in_t3train), t1test_in_t3train.key.tolist())
print("Task 3 test sequences that are Task 1 training sequences:", len(t1train_in_t3test),
      f"of {int((sets.task.eq('task3') & sets.split.eq('test')).sum())}")
m071 = sets[sets.key.str.endswith("mouse071_task1_annotator1")].kp_hash.iloc[0]
print("mouse071 also deposited as:", sets[(sets.kp_hash == m071) & ~sets.key.str.endswith("mouse071_task1_annotator1")].key.tolist())
'''
t=t.replace(old,new)
t=t.replace('''Every member's decompressed size and CRC matched the zip's directory (the helper checks both). In the
labelled sets the length of the annotations equals the number of frames in the scores for every
sequence. Sequences that start with identical keypoints are listed above; they are the same recording
deposited more than once, and dataset-size counts them once under one of its readings.''','''Every member's decompressed size and CRC matched the zip's directory (the helper checks both). In the
labelled sets the length of the annotations equals the number of frames in the scores for every
sequence, and the vocabularies and annotator ids are those of Appendix C (Task 3 gives annotator ids 0,
2 and 6 by behavior, which the paper does not describe). Many sequences have identical keypoints over
their whole length: the same recording deposited more than once, under other names and in other tasks
(printed above). Most are Task 1 recordings that reappear in Task 3, but some cross the training and
test splits: within Task 2 one recording is in annotator 3's training set and annotator 4's test set,
and Task 1 test recordings, mouse071 among them, are in Task 3's training sets. The paper says each
sequence is an independent observation (Appendix B) and does not mention this. dataset-size counts each
recording once under one of its readings; the counts and fractions of Tables 5 to 7 are per set, as the
paper reports them.''')
open(p,'w').write(t)
EOF
grep -n "include_groups" build_nb.py | head -2
```

```
316:cross = groups.apply(lambda g: sorted(set(g.set)), include_groups=False)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
import re
p='build_nb.py'; t=open(p).read()
results = [
# format-keypoints
"""**Result: partially reproduced.** The file holds the 14 keypoint series named for the seven parts of
the resident and the intruder, in pixels, at 30 Hz, with every coordinate inside the 1024 x 570 image.
The confidence field is present for every keypoint but holds no values (0 of 333,340 finite).""",
# resident-is-black
"""**Result: reproduced.** In the 746 sampled frames where the two body centres are at least 60 pixels
apart, the 12-pixel patch on the resident is darker than the one on the intruder in every frame
(fraction 1.000; median grey level 46.4 against 250.9). The fraction is 0.996 to 1.000 with other patch
sizes and separations, and 1.0 in every minute of the session.""",
# task1-vocab
"""**Result: reproduced.** The catalogue holds attack, investigation, mount and other with codes 0 to 3,
the annotator is given as CalMS21 annotator 0, and every one of the 23,810 frames has exactly one label.""",
# task1-video
"""**Result: reproduced.** The dandiset's video of mouse071 is 1024 x 570 at 30 frames per second with
23,810 frames, as many as the pose. It is 184,059,454 bytes against 964,451,532 for CaltechDATA's file
of the same sequence, so it was re-encoded; the two were not compared frame by frame.""",
# contact
"""**Result: reproduced.** The resident's nose is a median 21.4 px from the intruder in investigation
frames and 15.0 px in mount frames, against 376.0 px in other frames (differences -354.6 and -361.0 px,
95% intervals -407.3 to -292.7 and -412.0 to -304.2). The centroid distance gives the same, as does
each half of the session. Attack does not occur in this session and is untested.""",
# pose-errors-close-fast
"""**Result: partially reproduced.** Frames with an implausible body length are more common when the
mice are closest: 0.131 of the closest 10% of frames against 0.016 of the rest (difference 0.115, 95%
interval 0.064 to 0.179). They are less common, not more, in the fastest 10% of frames: 0.010 against
0.030 (difference -0.020, interval -0.033 to -0.008). Both directions hold at every threshold and factor
shown. The error measure is a proxy chosen here, since the dandiset holds no confidence values.""",
# link
"""**Result: reproduced.** The sequence matches by name and has the same 23,810 frames; every keypoint
coordinate is identical to CaltechDATA's (largest difference 0 px), and swapping the mice or the axes
gives differences of about 895 px, so the order is the stated one. The frame labels from the bouts agree
with CaltechDATA's annotations on all 23,810 frames. CaltechDATA's confidence scores (0.030 to 0.980,
all finite) have no counterpart in the dandiset, where all are NaN.""",
# confidence
"""**Result: partially reproduced.** The mean MARS confidence is lower in the closest 10% of frames
(median 0.649 against 0.740, difference -0.091, 95% interval -0.107 to -0.074), most of all for the
intruder (-0.149, resident -0.031). In the fastest 10% of frames it is higher, not lower (0.751 against
0.732, difference 0.018, interval 0.012 to 0.025). Both hold at the 5% and 20% thresholds.""",
# table5-task1
"""**Result: reproduced.** The Task 1 files hold 70 training sequences with 507,738 frames and 19 test
sequences with 262,107 frames, as reported.""",
# table5-task2
"""**Result: partially reproduced.** 19 of the 20 counts match exactly. Annotator 1's training set has
139,122 frames where the table gives 139,112, a difference of 10 frames (0.007%); its 6 sequences
match.""",
# table5-task3
"""**Result: reproduced.** All 28 Task 3 counts of frames and sequences match the table.""",
# table6
"""**Result: partially reproduced.** Under reading (a), the training split, investigation (28.876%), mount
(5.636%) and other (62.723%) are within tolerance, and attack is 2.76501% (14,039 of 507,738 frames,
printed below the table), which rounds to 2.77 and lies 0.00001 beyond the tolerance of 0.005 around
2.76; truncated, it gives the reported 2.76. All four are within 10% of the reported values. Reading (b)
does not match.""",
# fig4b
"""**Result: reproduced.** Under the training split with the class order of the Task 1 pie, all 20
percentages are within 0.05 of the figure's values. Training and test together match 1 of 20.""",
# table7
"""**Result: reproduced.** Under reading (a), the training split, all seven percentages are within
tolerance (approach 3.249%, disengaged 1.466%, groom 13.988%, intromission 19.255%, mount attempt
0.903%, sniff face 4.744%, white rearing 9.295%).""",
# dataset-size
"""**Result: reproduced.** The unlabeled set has 282 sequences and 5,952,058 frames. Over all labelled
sets there are 3,243,734 annotated frames (30.0 h), or 2,273,674 (21.1 h) with each recording counted
once, and 85.2 h or 76.2 h of pose with the unlabeled set; so "over 1 million annotated frames", "over 10
hours of annotation" and "over 70 hours of pose" hold under readings (b) and (c). Task 1 alone has
769,845 annotated frames (7.1 h), and with the unlabeled set 62.2 h of pose, so none of the three holds
under reading (a).""",
# table10
"""**Result: partially reproduced.** Across the seven behaviors, the baseline F1 rises with the
percentage of labelled frames (Spearman 0.786, p = 0.024 on the training split; 0.929, p = 0.003 on the
test split). It also rises with mean bout length, but not significantly (0.321, p = 0.249; 0.607, p =
0.083). With the task programming model's F1, the bout-length correlations are 0.536 (p = 0.118) and
0.679 (p = 0.055).""",
]
blocks = list(re.finditer(r'M\(r"""\n\*\*Result:.*?"""\)', t, re.S))
print(len(blocks), len(results))
assert len(blocks)==len(results)
for b, r in reversed(list(zip(blocks, results))):
    t = t[:b.start()] + 'M(r"""\n' + r + '\n""")' + t[b.end():]
# precise attack print
t=t.replace('''print(t6.groupby("reading")[["within", "within_10pct"]].all().to_string())''','''print(t6.groupby("reading")[["within", "within_10pct"]].all().to_string())
att = sum(c.get(0, 0) for c in t1[t1.split == "train"].counts)
tot = int(t1[t1.split == "train"].n_annotations.sum())
print(f"attack, training split: {att} of {tot} frames = {100 * att / tot:.6f}%; |diff| from 2.76 = {abs(100 * att / tot - 2.76):.6f}")''')
open(p,'w').write(t)
EOF
echo ok
```

```
16 16
ok
Shell cwd was reset to 
[This command modified 1 file you've previously read: ../../../../../tmp/claude-1001/build_nb.py. Call Read before editing.]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='build_nb.py'; t=open(p).read()
old='''M(r"""
## Summary

(Filled in after the run.)
""")'''
new='''M(r"""
## Summary

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and
the differences from the paper's method.

| Claim | Data | Outcome |
|---|---|---|
| format-keypoints | dandiset | partially reproduced (no confidence values) |
| resident-is-black | dandiset | reproduced |
| task1-vocab | dandiset | reproduced |
| task1-video | dandiset | reproduced |
| contact-during-social-behaviors | dandiset | reproduced (attack absent from the session) |
| pose-errors-close-fast | dandiset | partially reproduced (close yes, fast reversed) |
| link-mouse071 | with inputs | reproduced |
| pose-errors-close-fast-confidence | with inputs | partially reproduced (close yes, fast reversed) |
| table5-task1-counts | elsewhere | reproduced |
| table5-task2-counts | elsewhere | partially reproduced (one count off by 10 frames) |
| table5-task3-counts | elsewhere | reproduced |
| table6-task1-label-fractions | elsewhere | partially reproduced (attack 2.76501%, 0.00001 outside the tolerance) |
| fig4b-task2-label-fractions | elsewhere | reproduced |
| table7-task3-label-fractions | elsewhere | reproduced |
| dataset-size | elsewhere | reproduced |
| table10-task3-difficulty | elsewhere | partially reproduced (bout length not significant) |
| table1-architectures, table2-task-programming, table3-task2-style-transfer, table4-task3-new-behaviors, fig7-errors-at-transitions, fig11-annotator-similarity | elsewhere | blocked: methods underspecified |

**How the analysis differs from the paper's.** The paper describes a dataset and benchmarks models on it.
The dandiset holds one of its sequences, so the claims about the dataset as a whole were tested on the
CaltechDATA deposit. The paper gives no measure for "errors in pose estimation", "close contact" or
"moving very quickly", nor a test of how Task 3 performance depends on frequency and bout length; the
measures, thresholds and tests used here were fixed in the claims file before the analysis. Tolerances
for counts and percentages of the deposited files are 0 and half a unit of the last reported digit,
tighter than the protocol's default of 10%. No model was trained: the baseline code is not reachable
and the paper leaves the architectures' settings to it.

**What was found about the dandiset.**
- The CalMS21 part of the dandiset is one sequence of the dataset, Task 1 test sequence mouse071; its
  keypoints and frame annotations are identical to CaltechDATA's, and its video has the same frame
  count, size and rate as the pose and shares its clock.
- The MARS confidence scores, which CalMS21 distributes with the pose, are missing: the field is
  present and every value is NaN.
- The behavior catalogue has empty definitions, though the paper defines all three behaviors.
- The subject is the dyad stored as one subject with strain C57BL/6 only, sex unknown and age `P0D/`;
  the session start time is a placeholder (2024-01-01). The dandiset's `centroid_speed` is the speed of
  the midpoint of the two mice, which its description does not make clear.
- The video was re-encoded (184 MB against CaltechDATA's 964 MB for the same sequence); the dandiset
  does not say so.
- The dandiset links the CalMS21 dataset DOI but not the paper (arXiv:2104.02710).

Outside the dandiset, the CaltechDATA deposit holds many recordings more than once across tasks,
including across the training and test splits, which the paper does not mention; one Table 5 count
differs from the data by 10 frames; and the paper's datasheet gives a different licence (CC-BY-NC-SA)
from the deposit and the dandiset (CC-BY 4.0), and says the raw videos are not included while Section
3.1 and the deposit include the Task 1 videos.
""")'''
assert old in t
t=t.replace(old,new)
open(p,'w').write(t)
EOF
$TMPDIR/wk/bin/python build_nb.py && cd entries/001878-sun-2021 && time $TMPDIR/wk/bin/python -m jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3600 --ExecutePreprocessor.kernel_name=wk --output-dir $TMPDIR/out reproduce_sun_2021.ipynb 2>&1 | tail -2
```

```
Exit code 1
written 65 cells
/bin/bash: line 133: cd: entries/001878-sun-2021: No such file or directory
```

**Agent calls Bash**

```bash
cd entries/001878-sun-2021 && time $TMPDIR/wk/bin/python -m jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3600 --ExecutePreprocessor.kernel_name=wk --output-dir $TMPDIR/out reproduce_sun_2021.ipynb 2>&1 | tail -2; $TMPDIR/wk/bin/python -c "
import nbformat
nb=nbformat.read('$TMPDIR/out/reproduce_sun_2021.ipynb',4)
for i in [13,49]:
    c=[x for x in nb.cells][i]
    for o in c.outputs:
        if 'text' in o: print(o['text'][-5000:])
        elif o.get('output_type')=='error': print('ERROR', o['ename'], o['evalue'])
"
```

```
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 243463 bytes to /tmp/claude-1001/out/reproduce_sun_2021.ipynb

real	3m0.320s
user	3m10.532s
sys	0m14.395s
CaltechDATA record: {'doi': '10.22002/D1.1991', 'version': '1.0', 'publication_date': '2021-06-07', 'updated': '2024-08-16T01:02:14.250039+00:00', 'rights': ['cc-by-4.0']}
                            file        size                             checksum
            task1_videos_mp4.zip 28286565405 md5:790b2ff6054c0889c3b0112b3a12eacc
            task1_videos_seq.zip 74199137301 md5:b771c359e96a2f6576151e695166652b
     task2_annotation_styles.zip   912092847 md5:c97e87e13e77ffb80c073e05c05a4683
       calms21_convert_to_npy.py        4390 md5:068f0362ea9879a4051b66bd60656c29
                       readme.md       10946 md5:ad3faeae6835747fd30fcc0c8e83ad2e
         task3_new_behaviors.zip   556170163 md5:df59df02d069bab1cfc376cdc1a3925b
        seq_image_extraction.zip        9157 md5:ae250529ec80fb268aa068b5bc35bda1
         task1_MARS_features.zip  1831694572 md5:2a8b758dfff719a7310a24fa5a7a2435
            unlabeled_videos.zip  3530737176 md5:35ab3acdeb231a3fe1536e38ad223b2e
task1_classic_classification.zip   457357950 md5:8a02654fddae28614ee24a6a082261b8

task1     train  sequences  70 frames    507738 (7 s)
[... 89 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='build_nb.py'; t=open(p).read()
old='''(printed above). Most are Task 1 recordings that reappear in Task 3, but some cross the training and
test splits: within Task 2 one recording is in annotator 3's training set and annotator 4's test set,
and Task 1 test recordings, mouse071 among them, are in Task 3's training sets.'''
new='''(printed above): 574 sequences hold 450 distinct recordings. Most duplicates are Task 1 recordings
that reappear in Task 3 (93 of the 109 Task 3 test sequences are Task 1 training recordings), and some
cross the training and test splits of one task: four Task 2 recordings are in the training set of one
of annotators 3 and 4 and the test set of the other, and six Task 1 test recordings, mouse071 among
them, are Task 3 training sequences.'''
assert old in t; t=t.replace(old,new)
open(p,'w').write(t)
EOF
$TMPDIR/wk/bin/python build_nb.py
cd entries/001878-sun-2021
printf "av\nh5py\nmatplotlib\nnumpy\npandas\nremfile\nrequests\nscipy\n" > requirements.in
cat > entry.yaml <<'EOF'
schema_version: 1
name: 001878-sun-2021
type: reproduction
title: CalMS21 mouse social behavior dataset (Sun et al. 2021)
description: Tests the claims of Sun et al. (2021), the paper describing the CalMS21 dataset of
  resident-intruder pose and behavior annotations, on dandiset 001878, which holds one CalMS21
  sequence (Task 1 test sequence mouse071) with its video, and on the full dataset deposited on
  CaltechDATA. It checks the format, identities and annotations of the dandiset's sequence, links it
  to the deposit, and tests the dataset's counts and label fractions. The model benchmarks are not run.
license: Apache-2.0
notebooks:
- path: reproduce_sun_2021.ipynb
  title: Reproducing Sun et al. (2021) from dandiset 001878 and the CalMS21 deposit
  runtime_minutes: 3
helpers:
- calms21.py
related:
- id: dandi:001878/draft
  relation: uses_data
- id: doi:10.22002/d1.1991
  relation: reproduces
EOF
python -m json.tool ../../schemas/entry.schema.json | grep -A12 '"relation"' | head -20; ls
```

```
written 65 cells
                    "relation"
                ],
                "properties": {
                    "id": {
                        "description": "dandi:<id>[/<version>], doi:<doi>, or entry:<name>.",
                        "type": "string",
                        "pattern": "^(dandi:[0-9]{6}(/.+)?|doi:10\\.[0-9]{4,9}/.+|entry:[a-z0-9]+(-[a-z0-9]+)*)$"
                    },
                    "relation": {
                        "enum": [
                            "uses_data",
                            "reproduces",
                            "derived_from",
                            "references"
                        ]
                    }
                }
            }
        }
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd  && python -m json.tool schemas/attempt.schema.json | sed -n 150,330p
```

```
},
                    "measured": {
                        "description": "The values obtained, for claims with expected values: one number, or one per expected value, in the same order.",
                        "oneOf": [
                            {
                                "type": "number"
                            },
                            {
                                "type": "array",
                                "minItems": 1,
                                "items": {
                                    "type": "number"
                                }
                            }
                        ]
                    },
                    "deviations": {
                        "description": "How the test differed from the paper's method or data, e.g. one session of four, or a substituted model.",
                        "type": "array",
                        "items": {
[... 161 more lines not kept]
```

**Agent calls Bash**

```bash
python -m json.tool schemas/attempt.schema.json | sed -n 330,400p
```

```
"inputs": {
            "description": "Everything the attempt used that is not in the dandiset.",
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
                    }
[... 29 more lines not kept]
```

**Agent**

Now the entry README and the attempt record.

**Agent calls Write**

```json
{
 "file_path": "entries/001878-sun-2021/README.md",
 "content": "# CalMS21 (Sun et al. 2021) from dandiset 001878\n\nTests the claims of [Sun et al. (2021)](https://arxiv.org/abs/2104.02710), the paper describing the\nCalMS21 dataset ([doi:10.22002/D1.1991](https://doi.org/10.22002/D1.1991)), on\n[DANDI:001878](https://dandiarchive.org/dandiset/001878/draft) and on the full dataset on CaltechDATA.\nThe dandiset has no published version; the entry reads the draft and stops if an asset it uses has\nchanged. For CalMS21 it holds one sequence, the Task 1 test sequence mouse071, with its video.\n\n| Claim | Data | Outcome |\n|---|---|---|\n| Keypoint format, 30 Hz, 1024 x 570, with confidence scores | dandiset | Partially reproduced (no confidence values) |\n| The resident is the black mouse | dandiset | Reproduced |\n| Task 1 vocabulary, one annotator, one label per frame | dandiset | Reproduced |\n| Task 1 video at 30 Hz and 1024 x 570 | dandiset | Reproduced |\n| Investigation and mount happen in close contact | dandiset | Reproduced |\n| Pose errors are most common in close contact or fast movement (body-length proxy) | dandiset | Partially reproduced |\n| The dandiset's sequence is CalMS21 mouse071 | with inputs | Reproduced |\n| Pose errors in close contact or fast movement (MARS confidence) | with inputs | Partially reproduced |\n| Table 5, Task 1 counts | elsewhere | Reproduced |\n| Table 5, Task 2 counts | elsewhere | Partially reproduced |\n| Table 5, Task 3 counts | elsewhere | Reproduced |\n| Table 6, Task 1 label fractions | elsewhere | Partially reproduced |\n| Figure 4B, Task 2 label fractions | elsewhere | Reproduced |\n| Table 7, Task 3 label fractions | elsewhere | Reproduced |\n| Size of the unlabeled set and of the dataset | elsewhere | Reproduced |\n| Task 3 performance depends on frequency and bout length | elsewhere | Partially reproduced |\n| Model benchmarks (Tables 1 to 4, Figures 7 and 11; six claims) | elsewhere | Blocked: methods underspecified |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe attempt record, with the reasons and the differences from the paper's method, is\n[`attempts/001878-sun-2021-01.yaml`](../../attempts/001878-sun-2021-01.yaml).\n\n- `reproduce_sun_2021.ipynb`: the analysis. It takes about three minutes, most of it streaming the\n  video and the CaltechDATA zips.\n- `calms21.py`: loading the dandiset's CalMS21 file and video, and streaming sequences from the\n  CaltechDATA zips with range requests. Other notebooks on this dandiset can import it.\n"
}
```

```
File created successfully at: entries/001878-sun-2021/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "attempts/001878-sun-2021-01.yaml",
 "content": "schema_version: 1\nid: 001878-sun-2021-01\ndandiset: \"001878\"\ndandiset_version: draft\npaper: doi:10.22002/d1.1991\ndate: 2026-10-19\nentry: 001878-sun-2021\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code (GitHub Actions)\n    model: claude-opus-5-5\n    protocol: pilot-7\ninputs:\n- what: The CalMS21 dataset as deposited by the paper's authors (version 1.0), streamed from its zips\n    with range requests. The pose, confidence scores and annotations of every sequence of Tasks 1 to 3\n    and the unlabeled set, used for the link claim, the confidence-based pose-error claim and all\n    claims with data elsewhere; the directory of task1_videos_mp4.zip, used to compare the size of the\n    mouse071 video.\n  source: doi:10.22002/D1.1991 (CaltechDATA record s0vdx-0k302, version 1.0)\noutcomes:\n- claim: format-keypoints\n  outcome: partially_reproduced\n  notebook: reproduce_sun_2021.ipynb\n  output: claim:format-keypoints\n  notes: The file holds 14 keypoint series named for the seven parts of the resident and the intruder,\n    in pixels, at 30 Hz, with every coordinate inside the 1024 x 570 image (x 5.0 to 991.2, y 9.0 to\n    563.3). The confidence field is present for every keypoint but all 333,340 values are NaN, so the\n    confidence part of the claim fails.\n  deviations:\n  - Judged on the one CalMS21 sequence in the dandiset.\n- claim: resident-is-black\n  outcome: reproduced\n  notebook: reproduce_sun_2021.ipynb\n  output: claim:resident-is-black\n  notes: In 746 of 794 sampled frames (every 30th) the body centres are at least 60 px apart; in all of\n    them the 12 px patch on the resident is darker than the one on the intruder (median grey level\n    46.4 against 250.9). With 6 and 24 px patches the fractions are 0.996 and 1.000, with separations\n    of 30 and 120 px 0.999 and 1.000, and 1.0 in every minute.\n  deviations:\n  - The coat colour test (grey level of the video at the body centre) was chosen here; the paper states\n    the identities without a test.\n- claim: task1-vocab\n  outcome: reproduced\n  notebook: reproduce_sun_2021.ipynb\n  output: claim:task1-vocab\n  notes: The catalogue holds attack 0, investigation 1, mount 2 and other 3; the bouts give the\n    annotator as \"CalMS21 annotator 0\"; the 170 bouts tile the session from 0 to 793.67 s with no gaps,\n    so all 23,810 frames have exactly one label. The session has no attack bouts.\n- claim: task1-video\n  outcome: reproduced\n  notebook: reproduce_sun_2021.ipynb\n  output: claim:task1-video\n  notes: The video is 1024 x 570, h264, at 30 frames per second with 23,810 frames, equal to the pose.\n    Its motion energy correlates best with the pose speed at lag 0 (r = 0.754, falling to 0.19 and 0.26\n    at 15 frames either way). It is 184,059,454 bytes against 964,451,532 for CaltechDATA's\n    mouse071_task1_annotator1.mp4, so it was re-encoded; the two were not compared frame by frame.\n- claim: contact-during-social-behaviors\n  outcome: reproduced\n  notebook: reproduce_sun_2021.ipynb\n  output: claim:contact-during-social-behaviors\n  notes: Median distance from the resident's nose to the nearest intruder keypoint is 21.4 px in 4,679\n    investigation frames and 15.0 px in 2,894 mount frames, against 376.0 px in 16,237 other frames\n    (differences -354.6 and -361.0 px, 95% block bootstrap intervals -407.3 to -292.7 and -412.0 to\n    -304.2). The centroid distance gives -307.2 and -355.5 px, with intervals excluding 0, and each half\n    of the session gives the same order. Attack is absent from the session, so the attack part of the\n    statement is untested.\n  deviations:\n  - The paper defines the behaviors in words; the distance measure, the comparison with other frames\n    and the bootstrap were chosen here.\n  - One session, with no attack frames.\n- claim: pose-errors-close-fast\n  outcome: partially_reproduced\n  notebook: reproduce_sun_2021.ipynb\n  output: claim:pose-errors-close-fast\n  notes: 657 of 23,810 frames (2.8%) have a body length outside the session's quartiles widened by 3\n    IQR. In the closest 10% of frames (centroid distance at most 66.4 px) the fraction is 0.131 against\n    0.016 elsewhere (difference 0.115, 95% interval 0.064 to 0.179). In the fastest 10% (at least 389\n    px/s) it is 0.010 against 0.030 (difference -0.020, interval -0.033 to -0.008), the reverse of the\n    claim. Both directions hold at 5% and 20% and with a factor of 1.5. Error fractions by label are\n    0.045 (investigation), 0.105 (mount) and 0.009 (other).\n  deviations:\n  - The dandiset has no confidence values, so pose errors are counted with an anatomical proxy chosen\n    here; the paper gives no measure of pose error.\n  - The thresholds for close and fast frames were chosen here.\n- claim: link-mouse071\n  outcome: reproduced\n  notebook: reproduce_sun_2021.ipynb\n  output: claim:link-mouse071\n  notes: Matched by name to task1/test/mouse071_task1_annotator1 on CaltechDATA. Both have 23,810 frames;\n    every keypoint coordinate is identical (largest difference 0 px), while swapping the mice or the\n    axes gives differences of about 895 px. The frame labels from the bouts agree with the CaltechDATA\n    annotations on all 23,810 frames (4,679 investigation, 2,894 mount, 16,237 other). CaltechDATA's\n    confidence scores (0.030 to 0.980, all finite) are NaN in the dandiset. The same recording is also\n    deposited on CaltechDATA as the Task 3 training sequence task3/groom/train/mouse002_task3_groom.\n- claim: pose-errors-close-fast-confidence\n  outcome: partially_reproduced\n  notebook: reproduce_sun_2021.ipynb\n  output: claim:pose-errors-close-fast-confidence\n  notes: The mean confidence per frame (CaltechDATA scores, matched frame by frame) is lower in the\n    closest 10% of frames (median 0.649 against 0.740, difference -0.091, 95% interval -0.107 to\n    -0.074), most of all for the intruder (-0.149 against -0.031 for the resident). In the fastest 10%\n    of frames it is higher (0.751 against 0.732, difference 0.018, interval 0.012 to 0.025), the reverse\n    of the claim. Both hold at 5% and 20%. The confidence correlates with the body-length error flags of\n    pose-errors-close-fast (point-biserial r = -0.366). The link holds in full, so the match of scores\n    to frames is exact.\n  deviations:\n  - Confidence is a proxy for pose error; the paper gives no measure.\n  - The confidence scores come from CaltechDATA, as the dandiset's are missing.\n- claim: table5-task1-counts\n  outcome: reproduced\n  notebook: reproduce_sun_2021.ipynb\n  output: claim:table5-task1-counts\n  measured:\n  - 507738\n  - 70\n  - 262107\n  - 19\n  notes: The training file holds 70 sequences with 507,738 frames and the test file 19 with 262,107, as\n    reported. Annotation lengths equal the frame counts of the scores in every sequence.\n- claim: table5-task2-counts\n  outcome: partially_reproduced\n  notebook: reproduce_sun_2021.ipynb\n  output: claim:table5-task2-counts\n  measured: [139122, 6, 286810, 13, 135623, 6, 150919, 6, 107420, 6, 77079, 4, 108325, 6, 76174, 4,\n    92383, 6, 364007, 20]\n  notes: 19 of 20 counts match exactly. Annotator 1's training set has 139,122 frames where Table 5 gives\n    139,112 (10 frames, 0.007%); its six sequences match. Annotator ids in the metadata agree with\n    those in the keys.\n- claim: table5-task3-counts\n  outcome: reproduced\n  notebook: reproduce_sun_2021.ipynb\n  output: claim:table5-task3-counts\n  measured: [20624, 3, 126468, 25, 35751, 2, 19088, 1, 45174, 2, 156664, 13, 19200, 1, 55218, 10, 46847,\n    4, 85836, 12, 19244, 3, 251793, 47, 36181, 2, 17939, 1]\n  notes: All 28 counts match Table 5.\n- claim: table6-task1-label-fractions\n  outcome: partially_reproduced\n  notebook: reproduce_sun_2021.ipynb\n  output: claim:table6-task1-label-fractions\n  measured:\n  - 2.765\n  - 28.876\n  - 5.636\n  - 62.723\n  notes: Under reading (a), the training split, investigation, mount and other are within half a unit\n    of the last reported digit; attack is 14,039 of 507,738 frames, 2.765009%, 0.005009 from 2.76\n    against a tolerance of 0.005. It rounds to 2.77 and truncates to the reported 2.76. All four are\n    within 10% of the reported values. Reading (b), training and test, gives 3.46, 27.00, 7.85 and\n    61.68% and does not match.\n  deviations:\n  - The tolerance of half a unit of the last digit is tighter than the protocol's default of 10%,\n    because these are percentages of a fixed file; under the default the claim would be reproduced.\n- claim: fig4b-task2-label-fractions\n  outcome: reproduced\n  notebook: reproduce_sun_2021.ipynb\n  output: claim:fig4b-task2-label-fractions\n  measured: [59.98, 20.58, 16.20, 3.25, 65.51, 25.82, 3.40, 5.27, 68.91, 13.49, 9.50, 8.09, 75.23, 11.62,\n    4.46, 8.69, 69.53, 26.42, 1.03, 3.03]\n  notes: Under the training split with the class order of the Task 1 pie (other, investigation, mount,\n    attack), all 20 percentages are within 0.05 of the figure's values; the best assignment of classes\n    gives the same 20. Training and test together match 1 of 20 under either class reading.\n  deviations:\n  - The Task 2 pies carry no class names; the order was read from the Task 1 pie, and the alternative\n    reading (best assignment) was listed before the analysis. Both match.\n- claim: table7-task3-label-fractions\n  outcome: reproduced\n  notebook: reproduce_sun_2021.ipynb\n  output: claim:table7-task3-label-fractions\n  measured: [3.249, 1.466, 13.988, 19.255, 0.903, 4.744, 9.295]\n  notes: Under reading (a), the training split, all seven are within tolerance. Training and test\n    together give values outside 10% for five of seven (for example groom 7.36%).\n- claim: dataset-size\n  outcome: reproduced\n  notebook: reproduce_sun_2021.ipynb\n  output: claim:dataset-size\n  measured:\n  - 282\n  - 5952058\n  notes: The unlabeled set has 282 sequences and 5,952,058 frames (55.1 h). Annotated frames are 769,845\n    (7.1 h) in Task 1, 3,243,734 (30.0 h) over all labelled sets, and 2,273,674 (21.1 h) with each\n    recording counted once; tracked pose including the unlabeled set is 62.2, 85.2 and 76.2 h. So the\n    three \"over\" statements (1 million annotated frames, 10 hours of annotation, 70 hours of pose) hold\n    under readings (b) and (c) and none holds under reading (a).\n  deviations:\n  - The paper does not say which sets its totals cover; three readings were listed before the analysis.\n- claim: table10-task3-difficulty\n  outcome: partially_reproduced\n  notebook: reproduce_sun_2021.ipynb\n  output: claim:table10-task3-difficulty\n  notes: Across the seven behaviors the baseline F1 of Table 10 rises with the percentage of labelled\n    frames (Spearman 0.786, exact one-sided p = 0.024 on the training split; 0.929, p = 0.003 on the\n    test split) and with mean bout length, but the latter is not significant (0.321, p = 0.249; 0.607,\n    p = 0.083). With the task programming model's F1 the bout-length correlations are 0.536 (p = 0.118)\n    and 0.679 (p = 0.055). The direction of both parts of the statement holds; only the frequency part\n    is significant with seven behaviors.\n  deviations:\n  - The paper states the dependence without a test; the correlation and the permutation test were\n    chosen here, using the paper's published F1 scores with frequencies and bout lengths computed from\n    the data.\n- claim: table1-architectures\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notes: Needs the four baseline networks trained on Task 1. The paper gives some settings (input\n    window, skip factor, the ranges searched) and refers to the project code for the rest, but the code\n    at gitlab.aicrowd.com/aicrowd/research/mab-e/mab-e-baselines did not answer, with or without the\n    sandbox, and no copy was found in Software Heritage or on GitHub; the web archive holds its landing\n    page only. The data are public on CaltechDATA. Training five runs of each network was also not\n    attempted within the time limit.\n- claim: table2-task-programming\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notes: Needs the baseline network (code unavailable, see table1-architectures) and the challenge's\n    top entry, whose code is not linked. The task programming code (GitHub neuroethology/TREBA) and\n    precomputed features on CaltechDATA are public, but without the baseline classifier the comparison\n    cannot be repeated.\n- claim: table3-task2-style-transfer\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notes: Needs the fine-tuned baseline and the top entry; the baseline code is unavailable (see\n    table1-architectures) and the top entry's code is not linked.\n- claim: table4-task3-new-behaviors\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notes: Needs the fine-tuned baseline with per-behavior learning rates hand-tuned on a validation set,\n    and the top entry; neither's code is available (see table1-architectures).\n- claim: fig7-errors-at-transitions\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notes: Needs the baseline model's predictions; its code is unavailable (see table1-architectures).\n- claim: fig11-annotator-similarity\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notes: Needs the trained top entry's annotator embedding; the entry's code is not linked and the\n    paper describes the model only in outline.\nfindings:\n- kind: data_missing\n  statement: The MARS confidence scores, which CalMS21 distributes with every keypoint, are missing from\n    the dandiset's CalMS21 file; the confidence field of all 14 pose series is present but all 333,340\n    values are NaN. CaltechDATA's copy of the same sequence has them (0.03 to 0.98).\n- kind: selection_undocumented\n  statement: For CalMS21 the dandiset holds one sequence, the Task 1 test sequence mouse071, out of 574\n    sequences on CaltechDATA. Its description presents a collection of datasets and does not say that\n    only one CalMS21 sequence is included or why this one was chosen.\n- kind: metadata_insufficient\n  statement: The behavior catalogue (CalMS21_ethogram) has an empty definition for attack,\n    investigation, mount and other, though the paper defines the three behaviors (Appendix D.2) and\n    states that annotations refer to behaviors initiated by the resident.\n- kind: metadata_insufficient\n  statement: The two mice are stored as one subject with strain C57BL/6, sex unknown and age P0D/; the\n    intruder's strain (BALB/c) and the residents' sex (male) are known from the paper but not\n    recorded, and which series belongs to the black or white mouse is given only by the series names.\n- kind: metadata_error\n  statement: The session start time is 2024-01-01T00:00, a placeholder; CalMS21 gives no recording\n    dates.\n- kind: metadata_insufficient\n  statement: The `centroid_speed` series, and the bout columns mean_speed, peak_speed and\n    immobility_fraction that reduce it, are the speed of the mean of all 14 keypoints, which is the\n    midpoint of the two mice, not the speed of either animal. The description (\"the pose centroid,\n    mean over keypoints\") does not make this clear.\n- kind: other\n  statement: The dandiset's mouse071 video (184 MB) is a re-encoding of CaltechDATA's (964 MB). It has\n    the same frame count, size and rate, and its motion follows the pose at lag 0, but the dandiset does\n    not say it was re-encoded.\n- kind: metadata_insufficient\n  statement: The dandiset links the CalMS21 dataset DOI (10.22002/D1.1991) as IsDerivedFrom, but not the\n    paper that describes the dataset and its benchmarks (arXiv 2104.02710, NeurIPS 2021 Datasets and\n    Benchmarks).\n- kind: other\n  statement: On CaltechDATA, 574 CalMS21 sequences hold 450 distinct recordings (identical keypoints over\n    the whole sequence). 93 of the 109 Task 3 test sequences are Task 1 training recordings, six Task 1\n    test recordings (mouse071 among them) are Task 3 training sequences, and four Task 2 recordings are\n    in the training set of one of annotators 3 and 4 and the test set of the other. The paper describes\n    each sequence as an independent observation and does not mention the overlap.\n- kind: paper_inconsistency\n  statement: The paper's datasheet says the dataset does not include the raw videos, while Section 3.1\n    says all source videos of Task 1 are released, and the deposit holds them. The datasheet also gives\n    the licence as CC-BY-NC-SA, while the CaltechDATA record and the dandiset give CC-BY 4.0.\n- kind: other\n  statement: Table 5 gives 139,112 training frames for Task 2 annotator 1; the deposited file holds\n    139,122. The other 47 counts of Table 5 match.\n- kind: methods_unavailable\n  statement: The baseline code the paper links (gitlab.aicrowd.com/aicrowd/research/mab-e/mab-e-baselines)\n    is not reachable and no archived copy of the repository was found; the code of the challenge's top\n    entries is not linked. The paper leaves the architectures' settings to that code, so none of the\n    benchmark results can be repeated.\n"
}
```

```
File created successfully at: attempts/001878-sun-2021-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent**

Now lock, check and run with the registry tool.

**Agent calls Bash**

```bash
rm -rf entries/001878-sun-2021/__pycache__; python tools/entry.py lock entries/001878-sun-2021 && python tools/entry.py check entries/001878-sun-2021
```

```
wrote entries/001878-sun-2021/requirements.lock.txt
0 error(s)
```

**Agent calls Bash**

```bash
time python tools/entry.py all entries/001878-sun-2021 2>&1 | tail -20
```

```
Installed kernelspec registry-001878-sun-2021 in executed/001878-sun-2021/.venv/share/jupyter/kernels/registry-001878-sun-2021
0 error(s)
pass  reproduce_sun_2021.ipynb  (180 s)

real	3m11.506s
user	3m17.851s
sys	0m15.508s
```

**Agent**

Passed in 180 s. Now checking the executed copy against every conclusion.

**Agent calls Bash**

```bash
python -c "
import nbformat
nb=nbformat.read('executed/001878-sun-2021/reproduce_sun_2021.ipynb',4)
for i,c in enumerate(nb.cells):
    t=c.metadata.get('tags') or []
    if c.cell_type=='code' and any(x.startswith('claim:') for x in t) or (c.cell_type=='code' and i in (9,13)):
        print('===',i,t)
        for o in c.outputs:
            if 'text' in o: print(o['text'][:2500])
            elif o.get('output_type')=='error': print('ERROR',o['ename'],o['evalue'])
" | grep -vE "^\s*$" | head -400
```

```
=== 9 ['sanity']
video: {'frames': 23810, 'rate': 30.0, 'width': 1024, 'height': 570, 'codec': 'h264', 'duration_s': 793.6666666666666}
decoded 23810 frames in 32 s; pose frames 23810
correlation of video motion energy with pose speed, by lag (video frame i against pose frame i - lag):
-15    0.192
-14    0.203
-13    0.215
-12    0.233
-11    0.251
-10    0.273
-9     0.300
-8     0.329
-7     0.363
-6     0.402
-5     0.445
-4     0.497
-3     0.555
-2     0.624
-1     0.696
 0     0.754
[... 287 more lines not kept]
```

**Agent**

Every conclusion matches the printed numbers. Step 6: building the handover.

**Agent calls Bash**

```bash
python tools/entry.py handover entries/001878-sun-2021 && ls executed/001878-sun-2021/handover && python -c "
import nbformat
nb=nbformat.read('executed/001878-sun-2021/handover/reproduce_sun_2021.ipynb',4)
print(len(nb.cells), sum(c.source.lstrip().startswith('**Result:') for c in nb.cells), any('## Summary' in c.source for c in nb.cells))"; python tools/entry.py check entries/001878-sun-2021; git status --short
```

```
wrote executed/001878-sun-2021/handover
10.22002-d1.1991.yaml
calms21.py
reproduce_sun_2021.ipynb
47 0 False
0 error(s)
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
?? attempts/001878-sun-2021-01.yaml
?? claims/001878/
?? entries/001878-sun-2021/
?? scripts
```

**Agent**

The handover has 47 cells, with no conclusion cells and no summary. Checking the entry directory for stray files.

**Agent calls Bash**

```bash
ls -la entries/001878-sun-2021; git check-ignore -v paper executed scripts .bashrc 2>&1 | head; ls -la scripts | head
```

```
total 120
drwxr-xr-x  4 runner runner  4096 Oct 19 08:02 .
drwxr-xr-x 55 runner runner  4096 Oct 19 07:44 ..
drwxr-xr-x  3 runner runner  4096 Oct 19 07:45 .claude
-rw-r--r--  1 runner runner  2540 Oct 19 08:01 README.md
drwxr-xr-x  2 runner runner  4096 Oct 19 08:02 __pycache__
-rw-r--r--  1 runner runner 19723 Oct 19 07:55 calms21.py
-rw-r--r--  1 runner runner   911 Oct 19 08:00 entry.yaml
-rw-r--r--  1 runner runner 66895 Oct 19 08:00 reproduce_sun_2021.ipynb
-rw-r--r--  1 runner runner    55 Oct 19 08:00 requirements.in
-rw-r--r--  1 runner runner  1168 Oct 19 08:02 requirements.lock.txt
.gitignore:8:paper/	paper
.gitignore:6:executed/	executed
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 19 07:35 scripts
```

**Agent calls Bash**

```bash
find entries/001878-sun-2021/.claude | head; git check-ignore -v entries/001878-sun-2021/__pycache__/x.pyc entries/001878-sun-2021/.claude
```

```
entries/001878-sun-2021/.claude
entries/001878-sun-2021/.claude/.cc-writes
.gitignore:1:__pycache__/	entries/001878-sun-2021/__pycache__/x.pyc
```

**Agent calls Bash**

```bash
rm -rf entries/001878-sun-2021/__pycache__; python tools/entry.py check entries/001878-sun-2021
```

```
0 error(s)
```

**Agent**

I did steps 1 to 5 and ran the handover (step 6). The entry is `entries/001878-sun-2021`, the claims are in `claims/001878/10.22002-d1.1991.yaml`, and the attempt record is `attempts/001878-sun-2021-01.yaml`. `entry.py check` reports 0 errors and `all` passed. Nothing is committed.

The target DOI (10.22002/D1.1991) points to the CaltechDATA dataset record, not a paper. I used the full open-access text of the paper that describes the dataset: Sun et al. 2021, arXiv:2104.02710v4 (NeurIPS Datasets and Benchmarks), including its appendix and datasheet. The text is saved under `paper/`.

## 1. Outcomes

| Claim | Data | Outcome |
|---|---|---|
| format-keypoints | dandiset | partially reproduced (every confidence value is NaN) |
| resident-is-black | dandiset | reproduced (resident darker in 746 of 746 sampled frames) |
| task1-vocab | dandiset | reproduced |
| task1-video | dandiset | reproduced |
| contact-during-social-behaviors | dandiset | reproduced (this session has no attack frames) |
| pose-errors-close-fast | dandiset | partially reproduced: more errors when the mice are close, fewer (not more) when they move fast |
| link-mouse071 | with inputs | reproduced (keypoints identical, labels agree on all 23,810 frames) |
| pose-errors-close-fast-confidence | with inputs | partially reproduced: same pattern as above |
| table5-task1-counts | elsewhere | reproduced |
| table5-task2-counts | elsewhere | partially reproduced (one count is 139,122 in the data, 139,112 in the paper) |
| table5-task3-counts | elsewhere | reproduced |
| table6-task1-label-fractions | elsewhere | partially reproduced (attack is 2.765009%, 0.000009 outside the tolerance I set) |
| fig4b-task2-label-fractions | elsewhere | reproduced |
| table7-task3-label-fractions | elsewhere | reproduced |
| dataset-size | elsewhere | reproduced |
| table10-task3-difficulty | elsewhere | partially reproduced (the bout-length correlation is not significant) |
| Six model-benchmark claims | elsewhere | blocked (methods_underspecified) |

## 2. What was found about the dandiset

- **No published version.** Only a draft exists, last modified 2026-06-25T18:32:10Z.
- **One CalMS21 sequence.** The dandiset combines three source datasets. For CalMS21 it holds only the Task 1 test sequence mouse071, out of 574 sequences in the full dataset. The other two NWB files come from keypoint-MoSeq and the Mlost benchmark.
- **The sequence is a faithful copy except for the scores.** Its pose and labels match CaltechDATA exactly, and its video shares the pose's clock (motion correlation peaks at lag 0).
- **Confidence scores missing.** The confidence field exists for all 14 keypoints, but all 333,340 values are NaN.
- **Metadata gaps:**
  - The behavior catalogue has empty definitions.
  - The two mice are stored as one subject: strain C57BL/6 only, sex unknown, age `P0D/`.
  - The session start time is a placeholder (2024-01-01).
  - `centroid_speed` is the speed of the midpoint of the two mice, not of either animal, and its description does not say so.
  - The video was re-encoded (184 MB against CaltechDATA's 964 MB) without a note.
  - The paper itself is not linked, only the dataset DOI.
- **About the CaltechDATA deposit:**
  - The 574 sequences hold only 450 distinct recordings.
  - Some repeats cross training and test splits, including four Task 2 recordings between annotators 3 and 4.
  - The paper's datasheet gives the licence as CC-BY-NC-SA, while the deposit and the dandiset say CC-BY 4.0.
  - The datasheet says raw videos are not included; Section 3.1 and the deposit include them.
  - The baseline code the paper links (gitlab.aicrowd.com) does not respond, and I found no archived copy of the repository.

## 3. Where the protocol was unclear, wrong or missing something

1. **The target DOI is a dataset, not a paper.** I used the paper that describes the dataset and kept the target DOI as the `paper` key.
2. **No published version to pin.** The protocol covers drafts only for repeat attempts. I pinned the draft by the blob id of each asset (the helper stops if one changes) and recorded the modification time.
3. **The dandiset is a partial copy of the paper's own deposit.** I made the dataset-level claims `elsewhere`, tested on CaltechDATA, though "elsewhere" in the protocol reads as a different archive from the paper's.
4. **The link rule assumes outside labels mapped onto dandiset units.** Here the dandiset record is itself a copy of an outside record, so I made it a `with_inputs` link claim comparing the two copies.
5. **Default 10% tolerance is too loose for counts in a deposited file.** I used 0 for counts and half a unit of the last reported digit for percentages, with the reason given. That makes Table 6 partial, and the protocol does not say how to treat rounding against truncation.
6. **The dandiset lacks a variable a claim needs.** The scores are on CaltechDATA, so I split the pose-error claim in two: a dandiset-only version with a geometric error measure, and a `with_inputs` version using the CaltechDATA scores.
7. **Two block reasons both apply** (code unreachable, and training time). The protocol gives no rule for choosing; I used `methods_underspecified` and mentioned the other in the notes.
8. **No repository or commit to record for the paper's code** because it is unreachable. I recorded this as a `methods_unavailable` finding.
9. **Several claims are themselves data checks** (format, vocabulary, video). I saw their values during step 2, before writing criteria, and said so in the claims file's opening comment.
10. **The duplicate check is written for the dandiset.** I also ran it on the 22 GB of outside data, and used "each recording counted once" as one reading of the paper's totals.
11. **The paper's own numbers used in an analysis** (Table 10 F1 scores). I treated them as reference values, not as `inputs`.

## 4. Runtime and failures

- The notebook runs in 180 s in the clean environment. About 120 s of that is streaming all CalMS21 JSON from CaltechDATA by range requests, and 32 s is decoding the video.
- gitlab.aicrowd.com timed out, with and without the sandbox.
- Two problems were fixed along the way: PyAV could not open the video URL directly, so I pass it a remote file object; and HEAD requests to CaltechDATA's 60-second presigned URLs return 403, so the helper uses GET.
- Untracked dotfiles (`.bashrc`, `.gitconfig`, `.mcp.json` and others) and a character device named `scripts` are at the repository root. The device was already there when I started and I did not create the dotfiles; I left both alone.

## End of run

70 turns, 31 minutes, result: success.
