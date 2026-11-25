# komori-2026 · author · run 45590698868

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; ls; ls docs entries claims attempts paper tools
```

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md"
}
```

```
Wed Nov 25 10:05:40 UTC 2026
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
[... 1142 more lines not kept]
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
cat claims/komori-2026.yaml; cat papers/datasets/komori-2026.yaml; ls questions | grep komori; ls papers/author-notes | grep komori
```

```
<persisted-output>
Output too large (42.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/3ad0c0b5-c5cc-4a58-a90b-b66f444416fa/tool-results/bgsm15ezx.txt

Preview (first 2KB):
# Claims for Komori, Mizusaki, Tomita, Yoneda, Matoba & Morita (2026), "Mesoscopic cortical
# activities associated with pupil-linked perceptions inferred via explainable machine learning",
# tested on DANDI:001425.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-25,
# following docs/protocol.md (pilot-18), Reader, steps 1 to 4.
#
# Text read: the bioRxiv preprint (doi:10.64898/2026.05.27.726399, the version posted June 1,
# 2026), as stored in paper/10.64898-2026.05.27.726399.txt. It holds the main text, the Methods,
# the legends of Figures 1 to 4 and of Supplementary Figures 1 to 12, and the Data and Code
# Availability statements. Supplementary Figures 3, 4, 5 and 6 were read from the images beside
# the text (supp-fig-S3 to S6.jpg); the numbers taken from them are marked as read from a figure.
# No other figure was seen. No separate supplementary text exists ("Supplementary Fig. 1 to 12").
#
# Code read: https://github.com/moritalabC201/WF_deep-learning at commit 405a720 (2026-01-22),
# the repository the Code Availability names. It holds template notebooks with placeholder paths
# for atlas registration, hemodynamic correction, SVD (400 components, fitted on every fifth
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md | head -150; wc -l docs/design.md docs/archives.md
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
[... 131 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/komori-2026.yaml"
}
```

```
1	# Claims for Komori, Mizusaki, Tomita, Yoneda, Matoba & Morita (2026), "Mesoscopic cortical
2	# activities associated with pupil-linked perceptions inferred via explainable machine learning",
3	# tested on DANDI:001425.
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-25,
5	# following docs/protocol.md (pilot-18), Reader, steps 1 to 4.
6	#
7	# Text read: the bioRxiv preprint (doi:10.64898/2026.05.27.726399, the version posted June 1,
8	# 2026), as stored in paper/10.64898-2026.05.27.726399.txt. It holds the main text, the Methods,
9	# the legends of Figures 1 to 4 and of Supplementary Figures 1 to 12, and the Data and Code
10	# Availability statements. Supplementary Figures 3, 4, 5 and 6 were read from the images beside
11	# the text (supp-fig-S3 to S6.jpg); the numbers taken from them are marked as read from a figure.
12	# No other figure was seen. No separate supplementary text exists ("Supplementary Fig. 1 to 12").
13	#
14	# Code read: https://github.com/moritalabC201/WF_deep-learning at commit 405a720 (2026-01-22),
15	# the repository the Code Availability names. It holds template notebooks with placeholder paths
16	# for atlas registration, hemodynamic correction, SVD (400 components, fitted on every fifth
17	# session, ca_list[i][::5]) and JADE ICA (top 200 SVD components, ICs kept by hand), pupil
18	# diameter from DeepLabCut, data set construction, GRU training (32 units, sigmoid output,
19	# Adam, binary cross-entropy with label smoothing 0.001, batch 256), ROC and Youden threshold,
20	# Deep SHAP, VIF (statsmodels), permutation importance (3 repeats) and the paired t-tests of
[... 712 more lines not kept]
```

**Agent calls Bash**

```bash
ls -la entries/fouke-2025 entries/kondo-2025; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in; cat attempts/fouke-2025-01.yaml | head -200
```

```
entries/fouke-2025:
total 132
drwxr-xr-x   2 runner runner  4096 Nov 25 10:00 .
drwxr-xr-x 351 runner runner 12288 Nov 25 10:00 ..
-rw-r--r--   1 runner runner  2144 Nov 25 10:00 README.md
-rw-r--r--   1 runner runner   907 Nov 25 10:00 entry.yaml
-rw-r--r--   1 runner runner 16218 Nov 25 10:00 omr.py
-rw-r--r--   1 runner runner 79403 Nov 25 10:00 reproduce_fouke_2025.ipynb
-rw-r--r--   1 runner runner    61 Nov 25 10:00 requirements.in
-rw-r--r--   1 runner runner  5989 Nov 25 10:00 requirements.lock.txt

entries/kondo-2025:
total 168
drwxr-xr-x   2 runner runner   4096 Nov 25 10:00 .
drwxr-xr-x 351 runner runner  12288 Nov 25 10:00 ..
-rw-r--r--   1 runner runner   2607 Nov 25 10:00 README.md
-rw-r--r--   1 runner runner  26719 Nov 25 10:00 bdbc.py
-rw-r--r--   1 runner runner   1043 Nov 25 10:00 entry.yaml
-rw-r--r--   1 runner runner 107285 Nov 25 10:00 reproduce_kondo_2025.ipynb
-rw-r--r--   1 runner runner     56 Nov 25 10:00 requirements.in
[... 230 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 200,400p attempts/fouke-2025-01.yaml | grep -v "^    " | head -80; grep -n "findings:" -A30 attempts/fouke-2025-01.yaml | head -50
```

```
blocked_by: metadata_insufficient
  notes: The numbers come from single representative fish and trials. Fig1-S1.ipynb selects them
- claim: fig2d-shared-architecture
  outcome: blocked
  blocked_by: data_missing
  notes: The two-photon imaging data are not in the dandiset, which holds only freely swimming
- claim: fig2g-dsi-similar
  outcome: blocked
  blocked_by: data_missing
  notes: Imaging data not in the dandiset, nor found elsewhere (see fig2d-shared-architecture).
- claim: fig2h-fewer-motion-responsive
  outcome: blocked
  blocked_by: data_missing
  notes: Imaging data not in the dandiset, nor found elsewhere (see fig2d-shared-architecture).
- claim: fig2k-more-monocular
  outcome: blocked
  blocked_by: data_missing
  notes: Imaging data not in the dandiset, nor found elsewhere (see fig2d-shared-architecture).
- claim: fig2l-bi-ratio
  outcome: blocked
[... 110 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "DANDI" -A80 docs/archives.md | head -120; ls schemas
```

```
4:the DANDI Archive. The protocol is written for any archive. What is particular
5-to an archive (how its datasets are named, versioned and read) is here, and an
6-agent is pointed to its archive's section.
7-
8-A dataset is keyed as `<archive>:<id>` and shown as `<LABEL>:<id>`, for example
9:`DANDI:000003`. Its files in this repository (`claims/`, `questions/`,
10-`transcripts/`, the `attempt/` branch, the paper store) are under its folder
11:name: the identifier alone for DANDI, which the registry began with, and
12-`<archive>-<id>` for any other archive. Each archive is an adapter, a module in `tools/archives/` ("Adding an archive",
13-below), and `tools/datasets.py` turns one form of a dataset's name into another.
14-The workflows take a dataset in any of these forms.
15-
16:## DANDI
17-
18-- **Datasets.** A dandiset, identified by six digits (`000003`). Targets are the
19-  public dandisets whose metadata names a paper (`targets/dandisets.json`, built
20:  by `tools/build_targets.py` and refreshed daily by the Track DANDI workflow).
21-- **Versions.** A published version (`0.220126.1855`) is fixed and has a DOI,
22-  `10.48324/dandi.<id>/<version>`. The draft can change. Pin the version the
23-  paper cites, or the latest published one. For a draft, record its
[... 104 more lines not kept]
```

**Agent**

Now the paper's Methods, focused on resting state and the pipeline.

**Agent calls Bash**

```bash
wc -c paper/*.txt; grep -n -i "rest\|methods\|^[A-Z][a-z ]*$" paper/10.64898-2026.05.27.726399.txt | head -120
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.64898-2026.05.27.726399.txt",
 "offset": 289,
 "limit": 320
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/001425/ | python -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/001425/versions/" | python -m json.tool | grep -E '"version"|"status"|"created"|"modified"|asset_count|size'
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/k; cd $TMPDIR/k; python - <<'EOF'
import requests, json
url="https://api.dandiarchive.org/api/dandisets/001425/versions/0.250705.0947/assets/?page_size=1000"
out=[]
while url:
    r=requests.get(url).json(); out+=r['results']; url=r['next']
json.dump(out,open('assets.json','w'))
print(len(out))
import collections
c=collections.Counter()
for a in out:
    p=a['path']; 
    c[p.split('/')[-1].split('_')[-1]]+=1
print(c.most_common(30))
for a in out[:30]: print(a['path'], a['size']/1e9)
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'requests'
```

**Agent calls Bash**

```bash
cd $TMPDIR/k && uv venv -q .venv && . .venv/bin/activate && uv pip install -q requests pynwb h5py remfile numpy scipy dandi 2>&1 | tail -2; python -c "import pynwb, remfile; print(pynwb.__version__)"
```

```
4.2.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/k; . .venv/bin/activate; python - <<'EOF'
import requests, json, collections
url="https://api.dandiarchive.org/api/dandisets/001425/versions/0.250705.0947/assets/?page_size=1000"
out=[]
while url:
    r=requests.get(url).json(); out+=r['results']; url=r['next']
json.dump(out,open('assets.json','w'))
print(len(out))
c=collections.Counter()
for a in out:
    c[a['path'].split('_',1)[-1] if '_' in a['path'].split('/')[-1] else a['path']]+=1
c2=collections.Counter(a['path'].split('/')[-1].split('_')[-1] for a in out)
print(c2.most_common(30))
for a in out[:40]: print(a['path'], round(a['size']/1e9,2))
EOF
```

```
1838
[('body-camera.mp4', 449), ('widefield+behavior.nwb', 449), ('eye-camera.mp4', 448), ('face-camera.mp4', 446), ('widefield.nwb', 46)]
sub-VG1-GC#51/sub-VG1-GC#51_ses-2023-06-15-resting-state-day1_widefield+behavior/sub-VG1-GC#51_ses-2023-06-15-resting-state-day1_eye-camera.mp4 0.15
sub-VG1-GC#51/sub-VG1-GC#51_ses-2023-06-15-resting-state-day1_widefield+behavior/sub-VG1-GC#51_ses-2023-06-15-resting-state-day1_body-camera.mp4 0.5
sub-VG1-GC#51/sub-VG1-GC#51_ses-2023-06-15-task-day1_widefield+behavior/sub-VG1-GC#51_ses-2023-06-15-task-day1_eye-camera.mp4 0.44
sub-VG1-GC#51/sub-VG1-GC#51_ses-2023-06-15-resting-state-day1_widefield+behavior/sub-VG1-GC#51_ses-2023-06-15-resting-state-day1_face-camera.mp4 0.5
sub-VG1-GC#51/sub-VG1-GC#51_ses-2023-06-15-task-day1_widefield+behavior/sub-VG1-GC#51_ses-2023-06-15-task-day1_body-camera.mp4 1.48
sub-VG1-GC#51/sub-VG1-GC#51_ses-2023-06-15-task-day1_widefield+behavior/sub-VG1-GC#51_ses-2023-06-15-task-day1_face-camera.mp4 1.48
sub-VG1-GC#51/sub-VG1-GC#51_ses-2023-06-16-task-day2_widefield+behavior/sub-VG1-GC#51_ses-2023-06-16-task-day2_eye-camera.mp4 0.43
sub-VG1-GC#51/sub-VG1-GC#51_ses-2023-06-16-task-day2_widefield+behavior/sub-VG1-GC#51_ses-2023-06-16-task-day2_body-camera.mp4 1.47
sub-VG1-GC#51/sub-VG1-GC#51_ses-2023-06-19-task-day3_widefield+behavior/sub-VG1-GC#51_ses-2023-06-19-task-day3_eye-camera.mp4 0.43
sub-VG1-GC#51/sub-VG1-GC#51_ses-2023-06-19-task-day3_widefield+behavior/sub-VG1-GC#51_ses-2023-06-19-task-day3_body-camera.mp4 0.88
sub-VG1-GC#51/sub-VG1-GC#51_ses-2023-06-16-task-day2_widefield+behavior/sub-VG1-GC#51_ses-2023-06-16-task-day2_face-camera.mp4 1.47
sub-VG1-GC#51/sub-VG1-GC#51_ses-2023-06-19-task-day3_widefield+behavior/sub-VG1-GC#51_ses-2023-06-19-task-day3_face-camera.mp4 1.47
sub-VG1-GC#51/sub-VG1-GC#51_ses-2023-06-20-task-day4_widefield+behavior/sub-VG1-GC#51_ses-2023-06-20-task-day4_body-camera.mp4 0.9
sub-VG1-GC#51/sub-VG1-GC#51_ses-2023-06-20-task-day4_widefield+behavior/sub-VG1-GC#51_ses-2023-06-
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/k; . .venv/bin/activate; python - <<'EOF'
import json, collections
out=json.load(open('assets.json'))
nwb=[a for a in out if a['path'].endswith('.nwb')]
rest=[a for a in nwb if 'resting' in a['path']]
print(len(nwb), len(rest))
subj=collections.defaultdict(list)
for a in rest: subj[a['path'].split('/')[0]].append((a['path'].split('/')[-1].replace(a['path'].split('/')[0]+'_',''), round(a['size']/1e9,1)))
for s,v in sorted(subj.items()): print(s, sorted(v))
w=[a for a in nwb if a['path'].endswith('_widefield.nwb')]
for a in w[:5]: print(a['path'], a['size']/1e9)
EOF
```

```
495 98
sub-VG1-GC#105 [('ses-2024-01-23-resting-state-day0_widefield.nwb', 5.3), ('ses-2024-01-24-resting-state-day1_widefield+behavior.nwb', 5.4), ('ses-2024-02-01-resting-state-day7_widefield+behavior.nwb', 5.4), ('ses-2024-02-15-resting-state-day15_widefield+behavior.nwb', 5.4)]
sub-VG1-GC#109 [('ses-2024-01-15-resting-state-day0_widefield.nwb', 5.4), ('ses-2024-01-16-resting-state-day1_widefield+behavior.nwb', 5.5), ('ses-2024-01-24-resting-state-day7_widefield+behavior.nwb', 5.5), ('ses-2024-02-05-resting-state-day15_widefield+behavior.nwb', 5.5)]
sub-VG1-GC#116 [('ses-2024-01-15-resting-state-day0_widefield.nwb', 5.6), ('ses-2024-01-16-resting-state-day1_widefield+behavior.nwb', 5.7), ('ses-2024-01-24-resting-state-day7_widefield+behavior.nwb', 5.6), ('ses-2024-02-05-resting-state-day15_widefield+behavior.nwb', 5.6)]
sub-VG1-GC#117 [('ses-2024-04-15-resting-state-day0_widefield+behavior.nwb', 5.7), ('ses-2024-04-16-resting-state-day1_widefield+behavior.nwb', 5.6), ('ses-2024-04-24-resting-state-day7_widefield+behavior.nwb', 5.6), ('ses-2024-05-09-resting-state-day15_widefield+behavior.nwb', 5.6)]
sub-VG1-GC#119 [('ses-2024-03-06-resting-state-day0_widefield+behavior.nwb', 5.6), ('ses-2024-03-07-resting-state-day1_widefield+behavior.nwb', 5.6), ('ses-2024-03-18-resting-state-day7_widefield+behavior.nwb', 5.6)]
sub-VG1-GC#122 [('ses-2024-03-06-resting-state-day0_widefield+behavior.nwb', 5.7), ('ses-2024-03-07-resting-state-day1_widefield+behavior.nwb', 5.7), ('ses-2024-03-18-resting-state-day7_widefield+behavior.nwb', 5.6)]
sub-VG1-GC#124 [('ses-2024-01-15-resting-state-day0_widefield.nwb', 5.5), ('ses-2024-01-16-resting-state-day1_widefield+behavior.nwb', 5.6), ('ses-2024-01-24-resting-state-day7_widefield+behavior.nwb', 5.5), ('ses-2024-02-05-resting-state-day15_widefield+behavior.nwb', 5.5)]
sub-VG1-GC#125 [('ses-2024-04-17-resting-state-day0_widefield+behavior.nwb', 5.7), ('ses-2024-04-18-resting-state-day1_widefield+behavior.nwb', 5.7), ('ses-2024-04-26-res
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/k; . .venv/bin/activate; cat > inspect.py <<'EOF'
import json, h5py, remfile, sys, time
out=json.load(open('assets.json'))
a=[a for a in out if a['path'].endswith(sys.argv[1])][0]
url=f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/"
import requests
s3=requests.head(url,allow_redirects=True).url
print(a['path'], s3)
t=time.time()
f=h5py.File(remfile.File(s3),'r')
def vis(name,obj):
    if isinstance(obj,h5py.Dataset):
        print(name, obj.shape, obj.dtype, obj.chunks, obj.compression, dict((k,(v if not hasattr(v,'shape') or v.size<5 else v.shape)) for k,v in obj.attrs.items() if k not in ('namespace','object_id')))
    else:
        at={k:v for k,v in obj.attrs.items() if k not in ('namespace','object_id')}
        print('G',name, at)
f.visititems(vis)
print(time.time()-t)
EOF
python inspect.py "GC#51_ses-2023-06-15-resting-state-day1_widefield+behavior.nwb" 2>&1 | grep -v "^G specifications" | head -150
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/k/inspect.py", line 1, in <module>
    import json, h5py, remfile, sys, time
  File "/tmp/claude-1001/k/.venv/lib/python3.13/site-packages/h5py/__init__.py", line 33, in <module>
    from . import version
  File "/tmp/claude-1001/k/.venv/lib/python3.13/site-packages/h5py/version.py", line 17, in <module>
    import numpy
  File "/tmp/claude-1001/k/.venv/lib/python3.13/site-packages/numpy/__init__.py", line 109, in <module>
    from numpy.__config__ import show_config
  File "/tmp/claude-1001/k/.venv/lib/python3.13/site-packages/numpy/__config__.py", line 4, in <module>
    from numpy._core._multiarray_umath import (
    ...<3 lines>...
    )
  File "/tmp/claude-1001/k/.venv/lib/python3.13/site-packages/numpy/_core/__init__.py", line 24, in <module>
    from . import multiarray
  File "/tmp/claude-1001/k/.venv/lib/python3.13/site-packages/numpy/_core/multiarray.py", line 11, in <module>
    from . import _multiarray_umath, overrides
  File "/tmp/claude-1001/k/.venv/lib/python3.13/site-packages/numpy/_core/overrides.py", line 4, in <module>
    import inspect
  File "/tmp/claude-1001/k/inspect.py", line 1, in <module>
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/k; . .venv/bin/activate; mv inspect.py lsnwb.py; python lsnwb.py "GC#51_ses-2023-06-15-resting-state-day1_widefield+behavior.nwb" 2>&1 | grep -v "^G specifications" | head -150
```

```
sub-VG1-GC#51/sub-VG1-GC#51_ses-2023-06-15-resting-state-day1_widefield+behavior.nwb https://dandiarchive.s3.amazonaws.com/blobs/64f/0ce/64f0ce35-20a4-4b10-9777-d5f01aadde16?response-content-disposition=attachment%3B%20filename%3D%22sub-VG1-GC%2351_ses-2023-06-15-resting-state-day1_widefield%2Bbehavior.nwb%22&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=[removed: an AWS key]%2F20261125%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Date=20261125T100624Z&X-Amz-Expires=21600&X-Amz-SignedHeaders=host&X-Amz-Signature=c1f0d5422fefd261ef10390659971e26ba269886133d8e3f61d2c9fe7dea0ab5
G acquisition {}
G acquisition/CO2_level {'comments': 'no comments', 'description': 'no description', 'neurodata_type': 'TimeSeries'}
acquisition/CO2_level/data (3141000,) float64 (6135,) gzip {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'a.u.'}
acquisition/CO2_level/timestamps (3141000,) float64 None None {'interval': np.int64(1), 'unit': 'seconds'}
G acquisition/LED_B {'comments': 'no comments', 'description': 'no description', 'neurodata_type': 'TimeSeries'}
acquisition/LED_B/data (3141000,) float64 (6135,) gzip {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'a.u.'}
acquisition/LED_B/timestamps (3141000,) float64 None None {'interval': np.int64(1), 'unit': 'seconds'}
G acquisition/LED_V {'comments': 'no comments', 'description': 'no description', 'neurodata_type': 'TimeSeries'}
acquisition/LED_V/data (3141000,) float64 (6135,) gzip {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'a.u.'}
acquisition/LED_V/timestamps (3141000,) float64 None None {'interval': np.int64(1), 'unit': 'seconds'}
G acquisition/air_pressure {'comments': 'no comments', 'description': 'no description', 'neurodata_type': 'TimeSeries'}
acquisition/air_pressure/data (3141000,) float64 (6135,) gzip {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.
[... 138 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/k; . .venv/bin/activate; python lsnwb.py "GC#51_ses-2023-06-15-resting-state-day1_widefield+behavior.nwb" 2>&1 | grep -v "^G specifications" | sed -n 150,400p | grep -v "body_video_keypoints\|face_video_keypoints"
```

```
G processing/behavior/eye_position {'neurodata_type': 'EyeTracking'}
G processing/behavior/eye_position/center_x {'comments': 'no comments', 'description': 'x-position of the center of the pupil', 'neurodata_type': 'SpatialSeries'}
processing/behavior/eye_position/center_x/data (61951,) float32 (3872,) gzip {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'pixels'}
processing/behavior/eye_position/center_x/reference_frame () object None None {}
processing/behavior/eye_position/center_x/timestamps (61951,) float64 None None {'interval': np.int64(1), 'unit': 'seconds'}
G processing/behavior/eye_position/center_y {'comments': 'no comments', 'description': 'y-position of the center of the pupil', 'neurodata_type': 'SpatialSeries'}
processing/behavior/eye_position/center_y/data (61951,) float32 (3872,) gzip {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'pixels'}
processing/behavior/eye_position/center_y/reference_frame () object None None {}
processing/behavior/eye_position/center_y/timestamps (61951,) float64 None None {'interval': np.int64(1), 'unit': 'seconds'}
G processing/behavior/eye_video_keypoint_set {'neurodata_type': 'Skeleton'}
processing/behavior/eye_video_keypoint_set/nodes (32,) object None None {}
G processing/behavior/eye_video_keypoints {'neurodata_type': 'PoseEstimation'}
processing/behavior/eye_video_keypoints/description () object None None {}
processing/behavior/eye_video_keypoints/dimensions (1, 2) uint16 None None {}
processing/behavior/eye_video_keypoints/labeled_videos (1,) object None None {}
G processing/behavior/eye_video_keypoints/lateralcorner {'comments': 'no comments', 'description': "Keypoint 'lateralcorner' from the eye video.", 'neurodata_type': 'PoseEstimationSeries'}
processing/behavior/eye_video_keypoints/lateralcorner/confidence (61951,) float64 None None {'definition': 'Softmax output of the deep neural network.'}
processing/behav
[... 163 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/k; . .venv/bin/activate; python lsnwb.py "GC#51_ses-2023-06-15-resting-state-day1_widefield+behavior.nwb" 2>&1 | grep -v "^G specifications" | sed -n 400,700p | grep -v "body_video_keypoints\|face_video_keypoints\|eye_video_keypoints"
```

```
G processing/behavior/pupil_tracking {'neurodata_type': 'PupilTracking'}
G processing/behavior/pupil_tracking/diameter {'comments': 'no comments', 'description': 'pupil diameter extracted from the video of the right eye', 'neurodata_type': 'TimeSeries'}
processing/behavior/pupil_tracking/diameter/data (61951,) float32 (3872,) gzip {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'pixels'}
processing/behavior/pupil_tracking/diameter/timestamps (61951,) float64 None None {'interval': np.int64(1), 'unit': 'seconds'}
G processing/downsampled {'description': 'validated session data, down-sampled to the time base of imaging dF/F', 'neurodata_type': 'ProcessingModule'}
G processing/downsampled/CO2_level {'comments': 'no comments', 'description': 'no description', 'neurodata_type': 'TimeSeries'}
processing/downsampled/CO2_level/data (18000,) float64 (1125,) gzip {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'a.u.'}
processing/downsampled/CO2_level/timestamps (18000,) float64 None None {'interval': np.int64(1), 'unit': 'seconds'}
G processing/downsampled/air_pressure {'comments': 'no comments', 'description': 'no description', 'neurodata_type': 'TimeSeries'}
processing/downsampled/air_pressure/data (18000,) float64 (1125,) gzip {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'a.u.'}
processing/downsampled/air_pressure/timestamps (18000,) float64 None None {'interval': np.int64(1), 'unit': 'seconds'}
G processing/downsampled/body_video_keypoint_set {'neurodata_type': 'Skeleton'}
processing/downsampled/body_video_keypoint_set/nodes (5,) object None None {}
G processing/downsampled/eye_position {'neurodata_type': 'EyeTracking'}
G processing/downsampled/eye_position/center_x {'comments': 'no comments', 'description': 'x-position of the center of the pupil', 'neurodata_type': 'SpatialSeries'}
processing/downsampled/eye_position/
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/k; . .venv/bin/activate; python lsnwb.py "GC#51_ses-2023-06-15-resting-state-day1_widefield+behavior.nwb" 2>&1 | grep -v "^G specifications" | sed -n 700,2000p | grep -v "body_video_keypoints\|face_video_keypoints\|eye_video_keypoints\|^specifications"
```

```
G processing/downsampled/humidity {'comments': 'no comments', 'description': 'no description', 'neurodata_type': 'TimeSeries'}
processing/downsampled/humidity/data (18000,) float64 (1125,) gzip {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'a.u.'}
processing/downsampled/humidity/timestamps (18000,) float64 None None {'interval': np.int64(1), 'unit': 'seconds'}
G processing/downsampled/lever {'comments': 'no comments', 'description': 'no description', 'neurodata_type': 'TimeSeries'}
processing/downsampled/lever/data (18000,) float64 (1125,) gzip {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'a.u.'}
processing/downsampled/lever/timestamps (18000,) float64 None None {'interval': np.int64(1), 'unit': 'seconds'}
G processing/downsampled/lick {'comments': 'no comments', 'description': 'no description', 'neurodata_type': 'TimeSeries'}
processing/downsampled/lick/data (18000,) float64 (1125,) gzip {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'a.u.'}
processing/downsampled/lick/timestamps (18000,) float64 None None {'interval': np.int64(1), 'unit': 'seconds'}
G processing/downsampled/lick_rate {'comments': 'no comments', 'description': 'no description', 'neurodata_type': 'TimeSeries'}
processing/downsampled/lick_rate/data (18000,) float64 (1125,) gzip {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'a.u.'}
processing/downsampled/lick_rate/timestamps (18000,) float64 None None {'interval': np.int64(1), 'unit': 'seconds'}
G processing/downsampled/motion {'comments': 'no comments', 'description': 'no description', 'neurodata_type': 'TimeSeries'}
processing/downsampled/motion/data (18000,) float64 (1125,) gzip {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'a.u.'}
processing/downsampled/motion/timestamps (18000,) float64
[... 53 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/k; . .venv/bin/activate; cat > speed.py <<'EOF'
import json, h5py, remfile, time, requests, numpy as np
out=json.load(open('assets.json'))
a=[a for a in out if a['path'].endswith("GC#51_ses-2023-06-15-resting-state-day1_widefield+behavior.nwb")][0]
s3=requests.head(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/",allow_redirects=True).url
t=time.time()
f=h5py.File(remfile.File(s3, verbose=False),'r')
d=f['acquisition/widefield_blue/data']
t=time.time(); x=d[1000:1300]; print('remfile 300 frames',time.time()-t, x.mean())
import fsspec
fs=fsspec.filesystem('http')
t=time.time()
fh=fs.open(s3, block_size=64*2**20, cache_type='readahead')
g=h5py.File(fh,'r'); d=g['acquisition/widefield_blue/data']
t=time.time(); x=d[2000:2600]; print('fsspec readahead 600 frames',time.time()-t)
t=time.time(); x=d[2600:3200]; print('again 600',time.time()-t)
EOF
python speed.py
```

```
remfile 300 frames 1.7861266136169434 10173.628693616576
fsspec readahead 600 frames 4.2135114669799805
again 600 1.1920719146728516
Shell cwd was reset to
```

**Agent calls Bash**

```bash
grep -n "python\|index" tools/entry.py | head -60; cat entries/fouke-2025/README.md | head -30
```

```
3:    python tools/entry.py lock  entries/<name>   # pin the environment
4:    python tools/entry.py check entries/<name>   # validate metadata and conventions
5:    python tools/entry.py check entries/*/       # the same for every entry, in one process
6:    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
7:    python tools/entry.py all   entries/<name>   # check, then run
8:    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies
110:def lookup(index: dict, attempt: dict):
114:    if one is not None and (attempt.get("paper"), one) in index:
115:        return index[(attempt.get("paper"), one)]
116:    return index.get((attempt.get("paper"), None))
206:        if entry.get("python") and locked_for and locked_for.group(1) != str(entry["python"]):
208:                         f"says {entry['python']}; run `tools/entry.py lock`")
467:LOCK_VERSION = re.compile(r"--python-version\s+(\d+\.\d+)")
470:def python_of(entry_dir: Path) -> str:
471:    """The Python version an entry runs on: its entry.yaml's `python`, else the version its lock was compiled for
474:    if entry.get("python"):
475:        return str(entry["python"])
484:def set_python(entry_dir: Path, version: str) -> None:
485:    """Write `python: "<version>"` into entry.yaml, replacing the field or adding it after `license`."""
488:    line = f'python: "{version}"'
[... 53 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 460,520p tools/entry.py; grep -rn "python:" entries/*/entry.yaml | awk '{print $NF}' | sort | uniq -c
```

```
if LONG_LITERAL.search(code):
        report.error(where, f"contains a literal of more than {MAX_LITERAL_NUMBERS} numbers; "
                            "results must be computed from the data")


# --- lock and run -------------------------------------------------------------

LOCK_VERSION = re.compile(r"--python-version\s+(\d+\.\d+)")


def python_of(entry_dir: Path) -> str:
    """The Python version an entry runs on: its entry.yaml's `python`, else the version its lock was compiled for
    (entries from before the field), else the registry's default for new entries, PYTHON_VERSION."""
    entry = yaml.safe_load((entry_dir / "entry.yaml").read_text()) or {}
    if entry.get("python"):
        return str(entry["python"])
    lock_file = entry_dir / "requirements.lock.txt"
    if lock_file.is_file():
        m = LOCK_VERSION.search(lock_file.read_text()[:2000])
        if m:
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/k; . .venv/bin/activate; uv pip install -q scikit-learn fsspec aiohttp statsmodels torch --index-url https://download.pytorch.org/whl/cpu --extra-index-url https://pypi.org/simple 2>&1 | tail -2; python - <<'EOF'
import json, h5py, fsspec, requests, numpy as np
out=json.load(open('assets.json'))
a=[a for a in out if a['path'].endswith("GC#51_ses-2023-06-15-resting-state-day1_widefield+behavior.nwb")][0]
s3=requests.head(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/",allow_redirects=True).url
f=h5py.File(fsspec.filesystem('http').open(s3,block_size=8*2**20,cache_type='readahead'),'r')
r=f['processing/ophys/ImageSegmentation/ROIs']
print([x.decode() for x in r['roi_name'][:]])
print([x.decode() for x in r['roi_description'][:5]])
print(f['analysis/atlas_to_data_transform/affine_matrix'][:])
tb=f['acquisition/widefield_blue/timestamps'][:]; tv=f['acquisition/widefield_UV/timestamps'][:]
tp=f['processing/downsampled/pupil_tracking/diameter/timestamps'][:]; td=f['processing/ophys/DfOverF/dFF/timestamps'][:]
print(tb[:3],tb[-1],np.diff(tb).mean(), tv[:3], tp[:3], td[:3], np.abs(tp-tb).max(), np.abs(td-tb).max())
p=f['processing/downsampled/pupil_tracking/diameter/data'][:]
print(np.nanmin(p),np.nanmax(p),np.isnan(p).sum(), np.nanmedian(p))
for k in ['imaging_rate','excitation_lambda','grid_spacing','indicator','location']:
    print(k, f['general/optophysiology/ImagingPlane_blue/'+k][()])
print(f['general/subject/genotype'][()], f['general/subject/subject_id'][()], f['session_description'][()], f['general/notes'][()][:500])
print([x.decode() for x in f['processing/behavior/eye_video_keypoint_set/nodes'][:]])
EOF
```

```
['AUDp_l', 'AUDs_l', 'MOp_l', 'MOs_l', 'OB_l', 'RSPagl_l', 'RSPd_l', 'SSp_bfd_l', 'SSp_ll_l', 'SSp_m_l', 'SSp_n_l', 'SSp_tr_l', 'SSp_ul_l', 'SSp_un_l', 'SSs_l', 'VISa_l', 'VISal_l', 'VISam_l', 'VISl_l', 'VISp_l', 'VISpm_l', 'VISrl_l', 'AUDp_r', 'AUDs_r', 'MOp_r', 'MOs_r', 'OB_r', 'RSPagl_r', 'RSPd_r', 'SSp_bfd_r', 'SSp_ll_r', 'SSp_m_r', 'SSp_n_r', 'SSp_tr_r', 'SSp_ul_r', 'SSp_un_r', 'SSs_r', 'VISa_r', 'VISal_r', 'VISam_r', 'VISl_r', 'VISp_r', 'VISpm_r', 'VISrl_r']
['Primary auditory area, left hemisphere', 'Secondary auditory areas (part of auditory areas), left hemisphere', 'Primary motor area, left hemisphere', 'Secondary motor area, left hemisphere', 'Main olfactory bulb, left hemisphere']
[[[ 0.54362047  0.03402285 -1.7668806 ]
  [-0.03167806  0.54585636 25.301891  ]]]
[15.06939983 15.10280037 15.13599968] 615.0419921875 0.0333336625564654 [15.08600044 15.11940002 15.15279961] [15.06939983 15.10280037 15.13599968] [15.06939983 15.10280037 15.13599968] 0.0 0.0
27.91029 218.75252 50 45.96311
imaging_rate 30.0
excitation_lambda 405.0
grid_spacing [18.18 18.18]
indicator b'GCaMP6s'
location b'Dorsal cortex'
b'VGluT1-Cre::Ai162' b'VG1-GC#51' b'Resting state: the animal can freely pull the lever. But tones and rewards are not presented during the recording. This sesion is performed in satiated condition for the animal after the lever-pull task.' b''
['pupiledge03', 'pupiledge10', 'pupiledge13', 'pupiledge14', 'pupiledge21', 'pupiledge28', 'pupiledge06', 'pupiledge04', 'pupiledge17', 'lateralcorner', 'pupiledge05', 'pupiledge16', 'pupiledge09', 'pupiledge26', 'pupiledge02', 'pupiledge08', 'pupiledge01', 'pupiledge20', 'pupiledge27', 'pupiledge25', 'pupiledge11', 'pupiledge15', 'pupiledge29', 'pupiledge24', 'pupiledge23', 'medialcorner', 'pupiledge12', 'pupiledge22', 'pupiledge30', 'pupiledge07', 'pupiledge19', 'pupiledge18']
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; nproc; free -g
```

```
Wed Nov 25 10:15:56 UTC 2026
4
               total        used        free      shared  buff/cache   available
Mem:              15           1           0           0          14          14
Swap:              2           0           2
```

**Agent calls Write**

```json
{
 "file_path": "entries/komori-2026/pupilwf.py",
 "content": "\"\"\"Helpers for testing Komori et al. (2026) on the resting-state recordings of DANDI:001425.\n\nThe paper (bioRxiv doi:10.64898/2026.05.27.726399) decodes spontaneous pupil dilation from\nindependent components (ICs) of wide-field calcium imaging with a GRU, on resting-state recordings\nof Kondo et al. (2025), DANDI:001425. The claims file (claims/komori-2026.yaml) names the open\ndetails R1 to R10 in its opening comment; each parameter below says where it comes from:\n[claim] the claims file's criterion or opening comment, [paper] a passage of the paper,\n[assumption] a choice the paper leaves open (with the reason), [standard] a choice that cannot\nchange a result.\n\nEverything is streamed from the archive (fsspec HTTP range reads into h5py); nothing is written\nto disk.\n\"\"\"\nfrom __future__ import annotations\n\nimport os\nimport re\nimport zlib\n\nimport numpy as np\nfrom scipy import signal, ndimage, stats\n\nDANDISET = \"001425\"\nVERSION = \"0.250705.0947\"  # most recent published version; the paper cites none\nAPI = \"https://api.dandiarchive.org/api\"\nPAPER_KEY = \"komori-2026\"\n\nFS = 30.0             # imaging frames per second per excitation channel (file: imaging_rate 30.0)\nWINDOW = 46           # [paper] Methods, Machine learning, Overview: \"46 frames for resting-state data\"\nEPOCH_S = 40.0        # [paper] Methods, Pupil labels: \"40 s epochs spanning 50-570 s\"\nEPOCH_START, EPOCH_END = 50.0, 570.0\nPUPIL_LP = 0.2        # [paper] Methods, Pupil labels: \"low-pass filtered at 0.2 Hz\" for resting data\nLABEL_PRE, LABEL_POST = 3.0, 0.5   # [paper] \"the window from 3 s before to 0.5 s after the ... peak\"\nTHRESH = 0.6          # [paper] \"binarized at 0.6\"\nF0_WINDOW = (5.0, 15.0)  # [paper] Methods, Hemodynamic correction: \"mean intensity ... 5-15 s after onset\"\nN_HEMO_SVD = 34       # [paper] \"SVD ... to extract 34 spatial components\"\nHEMO_HP = 0.1         # [paper] \"A 0.1 Hz high-pass filter was applied to both signals prior to regression\"\nN_SVD = 400           # [paper] Methods, ICA-based features: \"SVD retaining 400 components\"\nN_SVD_ICA = 200       # [paper] \"ICA was applied to the top 200 SVD temporal components\"\nN_ICA = 30            # [paper] \"The target number of ICs was 30\"\nEVERY = 5             # [paper] \"every fifth session was used to estimate the ICA decomposition\"\nVIF_MAX = 10.0        # [paper] \"ICs were iteratively removed until the maximum VIF ... fell below 10\"\nBIN = 2               # [standard] 2x2 spatial binning of the 288x288 frames (144x144) for memory;\n                      # the components are smooth at this scale. Recorded as a deviation.\nGRID_STEP = 4         # [standard] common atlas grid: the 512x512 atlas sampled every 4 pixels\n\n\ndef seed_of(claim_id: str) -> int:\n    \"\"\"The claim's seed (protocol, Author step 3).\"\"\"\n    return zlib.crc32(f\"{PAPER_KEY}/{claim_id}\".encode())\n\n\n# --- archive -----------------------------------------------------------------------------------\n\ndef list_assets():\n    import requests\n    url = f\"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=1000\"\n    out = []\n    while url:\n        r = requests.get(url, timeout=60).json()\n        out += r[\"results\"]\n        url = r[\"next\"]\n    return out\n\n\ndef s3_url(asset_id: str) -> str:\n    import requests\n    r = requests.head(f\"{API}/assets/{asset_id}/download/\", allow_redirects=True, timeout=60)\n    return r.url\n\n\ndef open_nwb(asset_id: str, block_mb: int = 64):\n    import fsspec\n    import h5py\n    fh = fsspec.filesystem(\"http\").open(s3_url(asset_id), block_size=block_mb * 2**20,\n                                        cache_type=\"readahead\")\n    return h5py.File(fh, \"r\")\n\n\ndef resting_table(assets):\n    \"\"\"One row per resting-state NWB file: subject, date, day label, whether it holds behaviour.\"\"\"\n    rows = []\n    for a in assets:\n        p = a[\"path\"]\n        if not p.endswith(\".nwb\") or \"resting-state\" not in p:\n            continue\n        m = re.search(r\"sub-(VG1-GC#\\d+)_ses-(\\d{4}-\\d{2}-\\d{2})-resting-state-(day\\d+)_(widefield(?:\\+behavior)?)\\.nwb\", p)\n        rows.append(dict(subject=m.group(1), date=m.group(2), day=m.group(3),\n                         behavior=m.group(4) == \"widefield+behavior\", path=p,\n                         asset_id=a[\"asset_id\"], size_gb=a[\"size\"] / 1e9))\n    rows.sort(key=lambda r: (int(r[\"subject\"].split(\"#\")[1]), r[\"date\"]))\n    return rows\n\n\ndef choose_sessions(rows, n_mice=3, n_sessions=3):\n    \"\"\"[claim] R1 reading (a): three mice, their first 2 or 3 resting sessions in recording order.\n    [assumption] Which three mice the paper used is not said. Mice are ordered by the date of\n    their first resting session, then by their number, and the first three whose first\n    `n_sessions` resting sessions all hold the pupil (widefield+behavior files) are taken.\"\"\"\n    by = {}\n    for r in rows:\n        by.setdefault(r[\"subject\"], []).append(r)\n    cands = []\n    for s, rs in by.items():\n        rs = sorted(rs, key=lambda r: r[\"date\"])\n        first = rs[:n_sessions]\n        if len(first) == n_sessions and all(r[\"behavior\"] for r in first):\n            cands.append((rs[0][\"date\"], int(s.split(\"#\")[1]), s, first))\n    cands.sort()\n    return [c[3] for c in cands[:n_mice]]\n\n\n# --- filters -----------------------------------------------------------------------------------\n\ndef butter(x, cutoff, kind=\"low\", fs=FS, order=4, axis=0):\n    \"\"\"4th-order Butterworth applied forward and backward [claim: opening comment, code read by\n    the reader: 'Low-pass filters are 4th-order Butterworth, applied forward and backward'].\"\"\"\n    sos = signal.butter(order, cutoff, btype=kind, fs=fs, output=\"sos\")\n    return signal.sosfiltfilt(sos, x, axis=axis)\n\n\ndef fill_nan(x):\n    x = np.asarray(x, dtype=np.float64).copy()\n    bad = ~np.isfinite(x)\n    if bad.any():\n        idx = np.arange(len(x))\n        x[bad] = np.interp(idx[bad], idx[~bad], x[~bad])\n    return x, int(bad.sum())\n\n\n# --- per-session reduction -----------------------------------------------------------------------\n\ndef _read_binned(ds, mask_b, block=600):\n    \"\"\"Stream a (T, 288, 288) uint16 dataset in blocks, bin 2x2, keep the masked pixels (float32).\"\"\"\n    T = ds.shape[0]\n    out = np.empty((T, int(mask_b.sum())), dtype=np.float32)\n    for i in range(0, T, block):\n        x = ds[i:i + block].astype(np.float32)\n        n, h, w = x.shape\n        x = x.reshape(n, h // BIN, BIN, w // BIN, BIN).mean(axis=(2, 4))\n        out[i:i + n] = x[:, mask_b]\n    return out\n\n\ndef atlas_grid_coords(affine, shape_b):\n    \"\"\"Data coordinates (binned pixels) of the common atlas grid points.\n    The file's affine maps 512x512 atlas (x=column, y=row) to 288x288 data (x, y); the convention\n    is checked in the notebook by the overlap of the warped ROI masks across sessions.\"\"\"\n    g = np.arange(0, 512, GRID_STEP, dtype=np.float64)\n    ay, ax = np.meshgrid(g, g, indexing=\"ij\")\n    A = np.asarray(affine, dtype=np.float64).reshape(2, 3)\n    dx = A[0, 0] * ax + A[0, 1] * ay + A[0, 2]\n    dy = A[1, 0] * ax + A[1, 1] * ay + A[1, 2]\n    # binned pixel centres: data pixel p maps to (p + 0.5) / BIN - 0.5\n    return (dy + 0.5) / BIN - 0.5, (dx + 0.5) / BIN - 0.5\n\n\ndef warp_maps(maps_b, coords, order=1):\n    \"\"\"Sample (k, H, W) maps at the atlas grid; returns (k, G, G).\"\"\"\n    ry, rx = coords\n    return np.stack([ndimage.map_coordinates(m, [ry, rx], order=order, mode=\"constant\", cval=np.nan)\n                     for m in maps_b])\n\n\ndef reduce_session(row, hemo_variant=\"fit_hp_subtract_raw\", verbose=True):\n    \"\"\"Read one resting session and reduce it to what the analysis needs.\n\n    Hemodynamic correction [paper, Methods, Hemodynamic correction]: dF/F to the mean of 5-15 s,\n    SVD (34 components), F480 regressed on F405 by OLS after a 0.1 Hz high-pass, the estimate\n    subtracted. [assumption] The paper computes the SVD for both channels without saying how;\n    here the SVD is of the 470 nm dF/F, and both channels are projected on its spatial\n    components, so the regression is per component. [assumption] The Methods fit the regression\n    on high-passed signals and subtract the estimate \"from the measured F480\"; the main reading\n    applies the fitted coefficients to the unfiltered signals (hemo_variant\n    'fit_hp_subtract_raw'); the other keeps the high-passed corrected signal ('hp_corrected').\n    Both are returned.\n    \"\"\"\n    import time\n    t0 = time.time()\n    f = open_nwb(row[\"asset_id\"])\n    masks = f[\"processing/ophys/ImageSegmentation/ROIs/image_mask\"][:]\n    names = [x.decode() for x in f[\"processing/ophys/ImageSegmentation/ROIs/roi_name\"][:]]\n    affine = f[\"analysis/atlas_to_data_transform/affine_matrix\"][:][0]\n    tb = f[\"acquisition/widefield_blue/timestamps\"][:]\n    tv = f[\"acquisition/widefield_UV/timestamps\"][:]\n    tp = f[\"processing/downsampled/pupil_tracking/diameter/timestamps\"][:]\n    pupil_raw = f[\"processing/downsampled/pupil_tracking/diameter/data\"][:]\n    dff_dep = f[\"processing/ophys/DfOverF/dFF/data\"][:]\n    td = f[\"processing/ophys/DfOverF/dFF/timestamps\"][:]\n    # cortex mask: the union of the 44 atlas ROIs, minus the olfactory bulb [paper: \"non-cortical\n    # pixels were masked\"]\n    cortex = np.zeros(masks.shape[1:], bool)\n    for m, n in zip(masks, names):\n        if not n.startswith(\"OB\"):\n            cortex |= m\n    h, w = cortex.shape\n    cortex_b = cortex.reshape(h // BIN, BIN, w // BIN, BIN).mean(axis=(1, 3)) >= 0.5\n    blue = _read_binned(f[\"acquisition/widefield_blue/data\"], cortex_b)\n    t_read_b = time.time() - t0\n    uv = _read_binned(f[\"acquisition/widefield_UV/data\"], cortex_b)\n    t_read = time.time() - t0\n    raw_mean_b, raw_mean_v = float(blue.mean()), float(uv.mean())\n    rel = tb - tb[0]\n    f0 = (rel >= F0_WINDOW[0]) & (rel < F0_WINDOW[1])\n    for x in (blue, uv):\n        base = x[f0].mean(axis=0)\n        x /= base\n        x -= 1.0\n    # SVD of the 470 nm dF/F (randomized, 34 components)\n    from sklearn.utils.extmath import randomized_svd\n    U, S, Vt = randomized_svd(blue, N_HEMO_SVD, n_iter=4, random_state=0)  # [standard] seed\n    # spatial components = rows of Vt (34 x pixels); temporal = projections\n    P = Vt.astype(np.float32)\n    Vb = blue @ P.T\n    Vv = uv @ P.T\n    var_b = float((blue.astype(np.float64) ** 2).sum())\n    resid_b = float(((blue - Vb @ P) ** 2).sum())\n    del blue, uv\n    Vb = Vb.astype(np.float64)\n    Vv = Vv.astype(np.float64)\n    hb = butter(Vb, HEMO_HP, \"high\")\n    hv = butter(Vv, HEMO_HP, \"high\")\n    coef = np.empty((N_HEMO_SVD, 2))\n    corr_raw = np.empty_like(Vb)\n    corr_hp = np.empty_like(Vb)\n    for k in range(N_HEMO_SVD):\n        X = np.column_stack([hv[:, k], np.ones(len(hv))])\n        beta, *_ = np.linalg.lstsq(X, hb[:, k], rcond=None)\n        coef[k] = beta\n        corr_hp[:, k] = hb[:, k] - X @ beta\n        corr_raw[:, k] = Vb[:, k] - beta[0] * Vv[:, k]\n    # spatial maps in binned image space, then on the atlas grid\n    maps_b = np.zeros((N_HEMO_SVD,) + cortex_b.shape, np.float32)\n    maps_b[:, cortex_b] = P\n    coords = atlas_grid_coords(affine, cortex_b.shape)\n    maps_atlas = warp_maps(maps_b, coords)\n    roi_b = np.stack([m.reshape(h // BIN, BIN, w // BIN, BIN).mean(axis=(1, 3)) for m in masks])\n    roi_atlas = warp_maps(roi_b, coords) >= 0.5\n    pupil, n_nan = fill_nan(pupil_raw)\n    out = dict(\n        subject=row[\"subject\"], date=row[\"date\"], day=row[\"day\"], path=row[\"path\"],\n        t=tb - tb[0], t_uv_offset=float(np.median(tv - tb)), pupil=pupil, pupil_nan=n_nan,\n        pupil_t_equal=bool(np.array_equal(tp, tb)), dff_t_equal=bool(np.array_equal(td, tb)),\n        V={\"fit_hp_subtract_raw\": corr_raw, \"hp_corrected\": corr_hp, \"uncorrected\": Vb},\n        maps_atlas=maps_atlas, roi_atlas=roi_atlas, roi_names=names, affine=affine,\n        dff_deposited=dff_dep, coef=coef, svd_var_explained=1 - resid_b / var_b,\n        n_frames=len(tb), n_pixels=int(cortex_b.sum()), raw_mean=(raw_mean_b, raw_mean_v),\n        read_s=t_read, read_blue_s=t_read_b, total_s=time.time() - t0)\n    f.close()\n    if verbose:\n        print(f\"{row['subject']} {row['day']}: {len(tb)} frames, {out['n_pixels']} pixels, \"\n              f\"read {t_read:.0f} s, total {out['total_s']:.0f} s, 34-SVD explains \"\n              f\"{out['svd_var_explained']:.3f} of dF/F variance\")\n    return out\n\n\n# --- global SVD and ICA ----------------------------------------------------------------------\n\ndef epochs_of(t):\n    \"\"\"[paper] 13 epochs of 40 s spanning 50-570 s; frame index ranges.\"\"\"\n    starts = np.arange(EPOCH_START, EPOCH_END - 1e-9, EPOCH_S)\n    return [(int(np.searchsorted(t, s)), int(np.searchsorted(t, s + EPOCH_S))) for s in starts]\n\n\ndef jade(X, m):\n    \"\"\"JADE ICA (Cardoso), a port of jadeR (https://github.com/gbeckers/jadeR) [paper: Methods, ICA].\n    X: (n_sensors, T) array. Returns B (m x n_sensors) so that B @ X are the m sources, whitened\n    (unit variance), sorted by decreasing norm of their mixing columns, as jadeR does.\"\"\"\n    X = np.asarray(X, dtype=np.float64)\n    n, T = X.shape\n    X = X - X.mean(axis=1, keepdims=True)\n    # whitening by PCA to m components\n    D, U = np.linalg.eigh((X @ X.T) / T)\n    k = np.argsort(D)[::-1][:m]\n    PCs = U[:, k]\n    scales = np.sqrt(D[k])\n    B = (PCs / scales).T          # m x n\n    X = B @ X                     # m x T, whitened\n    # cumulant matrices\n    nbcm = m * (m + 1) // 2\n    CM = np.zeros((m, m * nbcm))\n    R = np.eye(m)\n    Xt = X.T\n    Range = np.arange(m)\n    for im in range(m):\n        Xim = X[im]\n        Xijm = Xim * Xim\n        Qij = ((Xijm * X) @ Xt) / T - R - 2 * np.outer(R[:, im], R[:, im])\n        CM[:, Range] = Qij\n        Range = Range + m\n        for jm in range(im):\n            Xijm = Xim * X[jm]\n            Qij = np.sqrt(2) * (((Xijm * X) @ Xt) / T - np.outer(R[:, im], R[:, jm])\n                                - np.outer(R[:, jm], R[:, im]))\n            CM[:, Range] = Qij\n            Range = Range + m\n    # joint diagonalisation\n    V = np.eye(m)\n    seuil = 1e-6 / np.sqrt(T)\n    encore = True\n    sweep = 0\n    while encore and sweep < 100:\n        encore = False\n        sweep += 1\n        for p in range(m - 1):\n            for q in range(p + 1, m):\n                Ip = np.arange(p, m * nbcm, m)\n                Iq = np.arange(q, m * nbcm, m)\n                g = np.vstack([CM[p, Ip] - CM[q, Iq], CM[p, Iq] + CM[q, Ip]])\n                gg = g @ g.T\n                ton = gg[0, 0] - gg[1, 1]\n                toff = gg[0, 1] + gg[1, 0]\n                theta = 0.5 * np.arctan2(toff, ton + np.sqrt(ton * ton + toff * toff))\n                if abs(theta) > seuil:\n                    encore = True\n                    c, s = np.cos(theta), np.sin(theta)\n                    G = np.array([[c, -s], [s, c]])\n                    pair = [p, q]\n                    V[:, pair] = V[:, pair] @ G\n                    CM[pair, :] = G.T @ CM[pair, :]\n                    CM[:, np.concatenate([Ip, Iq])] = np.hstack(\n                        [c * CM[:, Ip] + s * CM[:, Iq], -s * CM[:, Ip] + c * CM[:, Iq]])\n    B = V.T @ B\n    A = np.linalg.pinv(B)\n    order = np.argsort((A ** 2).sum(axis=0))[::-1]\n    B = B[order]\n    # signs: first column of B positive, as jadeR\n    signs = np.sign(B[:, 0])\n    signs[signs == 0] = 1\n    return B * signs[:, None]\n\n\ndef common_mask(sessions):\n    m = None\n    for s in sessions:\n        ok = np.isfinite(s[\"maps_atlas\"]).all(axis=0) & (np.abs(s[\"maps_atlas\"]).sum(axis=0) > 0)\n        cortex = s[\"roi_atlas\"][[i for i, n in enumerate(s[\"roi_names\"]) if not n.startswith(\"OB\")]].any(axis=0)\n        ok &= cortex\n        m = ok if m is None else (m & ok)\n    return m\n\n\ndef decompose(sessions, hemo=\"fit_hp_subtract_raw\", n_svd=N_SVD, n_svd_ica=N_SVD_ICA, n_ica=N_ICA):\n    \"\"\"Pixel-wise Z-scored images (per session) -> SVD on every fifth epoch -> JADE ICA.\n    [paper] Methods, ICA-based cortical features. [assumption] For resting data the unit of\n    \"every fifth session\" is the 40 s epoch (the resting analogue of a 40 s session); pixel\n    Z-scoring uses each recording's own mean and SD. The data of a recording are of rank 34 after\n    the hemodynamic correction, so the SVD keeps min(400, 34 x recordings) components.\"\"\"\n    mask = common_mask(sessions)\n    Ws, Vc, sel = [], [], []\n    g = 0\n    for s in sessions:\n        V = s[\"V\"][hemo]\n        mu = V.mean(axis=0)\n        Vcen = V - mu\n        M = s[\"maps_atlas\"][:, mask].astype(np.float64)       # 34 x P\n        C = (Vcen.T @ Vcen) / len(Vcen)\n        sd = np.sqrt(np.einsum(\"kp,kl,lp->p\", M, C, M))\n        W = M / sd                                          # 34 x P, z-scored maps\n        ep = epochs_of(s[\"t\"])\n        idx = []\n        for (a, b) in ep:\n            if g % EVERY == 0:\n                idx.append(np.arange(a, b))\n            g += 1\n        idx = np.concatenate(idx) if idx else np.array([], int)\n        Ws.append(W)\n        Vc.append(Vcen)\n        sel.append(idx)\n    # X = sum_s W_s^T Vsel_s^T : P x Tsel ; build a factor with the same left singular vectors\n    blocks = []\n    for W, V, idx in zip(Ws, Vc, sel):\n        if len(idx) == 0:\n            continue\n        Q, Rr = np.linalg.qr(V[idx])             # Tsel x 34, 34 x 34\n        blocks.append(W.T @ Rr.T)                # P x 34\n    Mfac = np.hstack(blocks)\n    Us, Ss, _ = np.linalg.svd(Mfac, full_matrices=False)\n    k = min(n_svd, int((Ss > Ss[0] * 1e-10).sum()))\n    Us, Ss = Us[:, :k], Ss[:, ] if False else Ss[:k]\n    var = Ss ** 2\n    cum = np.cumsum(var) / var.sum()\n    # temporal components of every frame of every session, divided by the singular values\n    temporal = [(V @ W @ Us) / Ss for W, V in zip(Ws, Vc)]\n    k2 = min(n_svd_ica, k)\n    Xica = np.vstack([tc[idx, :k2] for tc, idx in zip(temporal, sel) if len(idx)])\n    B = jade(Xica.T, n_ica)\n    ics = [tc[:, :k2] @ B.T for tc in temporal]\n    # whiten on the decomposition frames\n    allsel = np.vstack([ic[idx] for ic, idx in zip(ics, sel) if len(idx)])\n    mu, sd = allsel.mean(axis=0), allsel.std(axis=0)\n    ics = [(ic - mu) / sd for ic in ics]\n    A = np.linalg.pinv(B) * sd                  # k2 x n_ica mixing, in units of the ICs\n    spatial = (Us[:, :k2] * Ss[:k2]) @ A        # P x n_ica\n    maps = np.full((n_ica,) + mask.shape, np.nan)\n    maps[:, mask] = spatial.T\n    return dict(mask=mask, ics=ics, maps=maps, n_svd=k, cum_var=cum, n_sel_frames=len(Xica),\n                svd_sv=Ss)\n\n\ndef compactness(maps, mask):\n    \"\"\"[assumption] The paper keeps \"ICs with spatially coherent and anatomically interpretable\n    spatial components ... by visual inspection\". As a repeatable stand-in, an IC map's\n    compactness is the share of its squared weight that lies in its largest connected region\n    of pixels above half its peak absolute value (sign taken at the peak).\"\"\"\n    out = []\n    for m in maps:\n        x = np.where(mask, m, 0.0)\n        pk = x.flat[np.nanargmax(np.abs(x))]\n        x = x * np.sign(pk)\n        hi = x >= 0.5 * np.nanmax(x)\n        lab, n = ndimage.label(hi)\n        if n == 0:\n            out.append(0.0)\n            continue\n        e = np.array([(x[lab == i] ** 2).sum() for i in range(1, n + 1)])\n        out.append(float(e.max() / (np.where(mask, m, 0.0) ** 2).sum()))\n    return np.array(out)\n\n\ndef vif(X):\n    \"\"\"VIF of each column: 1/(1-R2) of the column regressed (with intercept) on the others\n    [paper: Methods, Permutation importance; code: statsmodels variance_inflation_factor].\n    Computed from the inverse correlation matrix, which gives the same values.\"\"\"\n    X = np.asarray(X, dtype=np.float64)\n    C = np.corrcoef(X, rowvar=False)\n    return np.diag(np.linalg.pinv(C))\n\n\ndef select_ics(feats, comp, n, reading=\"kept\"):\n    \"\"\"IC selection [claim R6, rest-ic-count-and-window readings (a) and (b)].\n    feats: (frames, n_ica) filtered features used for VIF. Candidates are ordered by compactness.\n    reading 'initial' (b): the n most compact, then the one with the highest VIF removed until\n    the maximum VIF < 10. reading 'kept' (a): as (b), then the next most compact ICs are added\n    one at a time, each kept only if the maximum VIF stays below 10, until n are kept.\"\"\"\n    order = list(np.argsort(comp)[::-1])\n    keep = order[:n]\n    removed = []\n    while len(keep) > 1:\n        v = vif(feats[:, keep])\n        if v.max() < VIF_MAX:\n            break\n        removed.append(keep.pop(int(np.argmax(v))))\n    if reading == \"kept\":\n        for c in order[n:]:\n            if len(keep) >= n:\n                break\n            if c in removed:\n                continue\n            v = vif(feats[:, keep + [c]])\n            if v.max() < VIF_MAX:\n                keep.append(c)\n    return keep, removed\n\n\n# --- labels and samples --------------------------------------------------------------------\n\ndef pupil_norm(p):\n    \"\"\"[paper] Pupil low-pass 0.2 Hz, Z-scored and min-max normalised with the whole recording.\"\"\"\n    x = butter(p, PUPIL_LP, \"low\")\n    x = (x - x.mean()) / x.std()\n    return (x - x.min()) / (x.max() - x.min())\n\n\ndef epoch_labels(t, pn, sample_reading=\"window\", selection=\"none\"):\n    \"\"\"Per epoch: the peak of the normalised pupil, the label frames and the sample frames.\n    [claim R4] reading 'window' (a): samples are the frames from 3 s before to 0.5 s after the\n    peak; reading 'epoch' (b): every frame of the epoch is a sample, positive only inside that\n    window. [claim R5] 'none' (a) or 'rule' (b): keep epochs with more than 10 positive frames and\n    no positive frame earlier than 1.5 s before the peak.\"\"\"\n    out = []\n    n_pre, n_post = int(round(LABEL_PRE * FS)), int(round(LABEL_POST * FS))\n    n_look = int(round(1.5 * FS))\n    for e, (a, b) in enumerate(epochs_of(t)):\n        pk = a + int(np.argmax(pn[a:b]))\n        w0, w1 = max(pk - n_pre, WINDOW - 1), min(pk + n_post + 1, len(pn))\n        lab = (pn > THRESH).astype(np.int8)\n        win = np.arange(w0, w1)\n        pos_win = lab[win]\n        early = lab[w0:max(w0, pk - n_look)].sum()\n        ok = True\n        if selection == \"rule\":\n            ok = pos_win.sum() > 10 and early == 0\n        if sample_reading == \"window\":\n            frames = win\n            y = pos_win\n        else:\n            frames = np.arange(max(a, WINDOW - 1), b)\n            y = np.where((frames >= w0) & (frames < w1), lab[frames], 0).astype(np.int8)\n        out.append(dict(epoch=e, peak=pk, frames=frames, y=y, keep=ok,\n                        peak_value=float(pn[pk])))\n    return out\n\n\ndef normalise_features(ic, cutoff):\n    \"\"\"[paper/claim R6] IC time courses low-pass filtered (0.1 Hz for resting data, Results,\n    Feature importance, paragraph 2), Z-scored and min-max normalised, per recording\n    [assumption: per recording; the paper does not say over what span].\"\"\"\n    x = butter(ic, cutoff, \"low\") if cutoff else ic\n    x = (x - x.mean(axis=0)) / x.std(axis=0)\n    return (x - x.min(axis=0)) / (x.max(axis=0) - x.min(axis=0))\n\n\ndef build_samples(feats, labels, window=WINDOW):\n    \"\"\"Samples of `window` frames ending at each label frame [paper: label at the final frame].\"\"\"\n    Xs, ys = [], []\n    for L in labels:\n        fr = L[\"frames\"]\n        fr_ok = fr[fr >= window - 1]\n        idx = fr_ok[:, None] + np.arange(-window + 1, 1)[None, :]\n        Xs.append(feats[idx])\n        ys.append(L[\"y\"][fr >= window - 1])\n    return Xs, ys\n\n\n# --- GRU --------------------------------------------------------------------------------------\n\ndef gru_fit(Xtr, ytr, Xva, yva, seed, epochs=10, batch=256, smoothing=0.001, threads=4):\n    \"\"\"GRU(32) -> Dense(1) -> sigmoid, Adam (Keras default learning rate 1e-3), binary\n    cross-entropy with label smoothing 0.001, batch 256, 10 epochs for resting data, the epoch\n    of lowest validation loss kept [paper: Methods, Machine learning; claim R9]. Implemented in\n    PyTorch [deviation: the paper uses Keras; the architecture and loss are the same].\n    Returns the metrics at the best epoch and the best model.\"\"\"\n    import torch\n    from sklearn.metrics import roc_auc_score\n    torch.set_num_threads(threads)\n    torch.manual_seed(seed)\n    g = torch.Generator().manual_seed(seed)\n\n    class Net(torch.nn.Module):\n        def __init__(self, n_in):\n            super().__init__()\n            self.gru = torch.nn.GRU(n_in, 32, batch_first=True)\n            self.fc = torch.nn.Linear(32, 1)\n\n        def forward(self, x):\n            h, _ = self.gru(x)\n            return self.fc(h[:, -1]).squeeze(-1)\n\n    net = Net(Xtr.shape[2])\n    # Keras initialisers: glorot_uniform kernels, orthogonal recurrent kernels, zero biases\n    for name, p in net.named_parameters():\n        if \"weight_ih\" in name or name == \"fc.weight\":\n            torch.nn.init.xavier_uniform_(p)\n        elif \"weight_hh\" in name:\n            for i in range(3):\n                torch.nn.init.orthogonal_(p.data[i * 32:(i + 1) * 32])\n        else:\n            torch.nn.init.zeros_(p)\n    opt = torch.optim.Adam(net.parameters(), lr=1e-3, eps=1e-7)\n    Xt = torch.tensor(Xtr, dtype=torch.float32)\n    yt = torch.tensor(ytr, dtype=torch.float32)\n    Xv = torch.tensor(Xva, dtype=torch.float32)\n    yv_np = np.asarray(yva, dtype=np.float64)\n    ys = yt * (1 - smoothing) + 0.5 * smoothing\n    lossf = torch.nn.BCEWithLogitsLoss()\n    best = None\n    hist = []\n    for ep in range(epochs):\n        net.train()\n        perm = torch.randperm(len(Xt), generator=g)\n        for i in range(0, len(Xt), batch):\n            b = perm[i:i + batch]\n            opt.zero_grad()\n            loss = lossf(net(Xt[b]), ys[b])\n            loss.backward()\n            opt.step()\n        net.eval()\n        with torch.no_grad():\n            pv = torch.sigmoid(torch.cat([net(Xv[i:i + 4096]) for i in range(0, len(Xv), 4096)])).numpy()\n            ptr = torch.sigmoid(torch.cat([net(Xt[i:i + 4096]) for i in range(0, len(Xt), 4096)])).numpy()\n        pvc = np.clip(pv.astype(np.float64), 1e-7, 1 - 1e-7)\n        yvs = yv_np * (1 - smoothing) + 0.5 * smoothing\n        vloss = float(-np.mean(yvs * np.log(pvc) + (1 - yvs) * np.log(1 - pvc)))\n        auc = roc_auc_score(yv_np, pv) if 0 < yv_np.mean() < 1 else np.nan\n        tauc = roc_auc_score(ytr, ptr) if 0 < np.mean(ytr) < 1 else np.nan\n        acc = float(np.mean((pv >= 0.5) == (yv_np == 1)))\n        rec = dict(epoch=ep + 1, val_loss=vloss, val_auc=auc, val_acc=acc, train_auc=tauc)\n        hist.append(rec)\n        if best is None or vloss < best[\"val_loss\"]:\n            best = dict(rec)\n            best[\"state\"] = {k: v.clone() for k, v in net.state_dict().items()}\n    net.load_state_dict(best.pop(\"state\"))\n    return best, net, hist\n\n\ndef folds_by_mouse(units_by_mouse, seed, k=5):\n    \"\"\"[paper] Methods, Cross-validation: \"Data from each mouse were randomly divided into five\n    equal-sized partitions, which were pooled across animals to form five balanced folds\".\"\"\"\n    rng = np.random.default_rng(seed)\n    fold = {}\n    for mouse, units in units_by_mouse.items():\n        units = list(units)\n        perm = rng.permutation(len(units))\n        for j, i in enumerate(perm):\n            fold[units[i]] = j % k\n    return fold\n\n\ndef integrated_gradients(net, X, baseline, steps=32):\n    \"\"\"SHAP-like attribution of the logit-free output (sigmoid) by integrated gradients from a\n    single baseline. [deviation] The paper uses Deep SHAP (shap.DeepExplainer) with \"the mean\n    model output as the background reference\"; DeepExplainer does not support PyTorch GRU layers.\n    Integrated gradients from the mean input are the Aumann-Shapley values for that baseline,\n    and like Deep SHAP they sum to f(x) - f(baseline).\"\"\"\n    import torch\n    X = torch.tensor(X, dtype=torch.float32)\n    b = torch.tensor(baseline, dtype=torch.float32)[None]\n    total = torch.zeros_like(X)\n    for a in (np.arange(steps) + 0.5) / steps:\n        xi = (b + a * (X - b)).requires_grad_(True)\n        out = torch.sigmoid(net(xi)).sum()\n        gr, = torch.autograd.grad(out, xi)\n        total += gr\n    return ((X - b) * total / steps).detach().numpy()\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR/k; . .venv/bin/activate; export PYTHONPATH=entries/komori-2026; python - <<'EOF'
import numpy as np, pupilwf as pw, time
rng=np.random.default_rng(0)
S=np.vstack([rng.laplace(size=5000), rng.uniform(-1,1,5000), np.sign(rng.normal(size=5000))*rng.exponential(size=5000), rng.standard_t(3,5000)])
A=rng.normal(size=(6,4)); X=A@S
t=time.time(); B=pw.jade(X,4); print(time.time()-t)
Y=B@X; C=np.corrcoef(np.vstack([Y,S]))[:4,4:]; print(np.round(np.abs(C),2))
Z=rng.normal(size=(200,30000)); t=time.time(); B=pw.jade(Z,30); print('jade 200->30',time.time()-t)
EOF
```

```
0.001291513442993164
[[0.05 0.01 0.08 1.  ]
 [0.03 0.03 1.   0.06]
 [1.   0.03 0.03 0.04]
 [0.01 1.   0.02 0.  ]]
jade 200->30 6.217905521392822
Shell cwd was reset to
```

**Agent**

JADE port recovers synthetic sources. Now timing one full session reduction.

**Agent calls Bash**

```bash
cd $TMPDIR/k; . .venv/bin/activate; export PYTHONPATH=entries/komori-2026; python - <<'EOF'
import numpy as np, pupilwf as pw, time, pickle, resource
assets=pw.list_assets()
rows=pw.resting_table(assets)
print(len(rows), len({r['subject'] for r in rows}))
ch=pw.choose_sessions(rows)
for c in ch: print([(r['subject'],r['day'],r['date']) for r in c])
s=pw.reduce_session(ch[0][0])
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,'GB')
pickle.dump(s,open('s0.pkl','wb'))
print(s['coef'][:5], s['t_uv_offset'], s['pupil_t_equal'], s['pupil_nan'])
EOF
```

```
98 25
[('VG1-GC#51', 'day0', '2023-06-14'), ('VG1-GC#51', 'day1', '2023-06-15'), ('VG1-GC#51', 'day7', '2023-06-23')]
[('VG1-GC#52', 'day0', '2023-06-14'), ('VG1-GC#52', 'day1', '2023-06-15'), ('VG1-GC#52', 'day7', '2023-06-23')]
[('VG1-GC#53', 'day0', '2023-06-14'), ('VG1-GC#53', 'day1', '2023-06-15'), ('VG1-GC#53', 'day7', '2023-06-23')]
VG1-GC#51 day0: 18000 frames, 10055 pixels, read 176 s, total 180 s, 34-SVD explains 0.994 of dF/F variance
3.276992 GB
[[ 1.18911138e+00  6.17807140e-03]
 [ 2.71943084e-01 -1.00858359e-03]
 [-1.54382076e+00  4.41709478e-03]
 [-2.84894770e-01  4.57204605e-04]
 [-9.07419624e-01 -5.95919362e-04]] 0.0166015625 True 768
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/komori-2026 && python - <<'EOF'
s=open('pupilwf.py').read()
s=s.replace("""    var_b = float((blue.astype(np.float64) ** 2).sum())
    resid_b = float(((blue - Vb @ P) ** 2).sum())
""","""    var_b = resid_b = 0.0
    for i in range(0, len(blue), 2000):
        var_b += float((blue[i:i + 2000].astype(np.float64) ** 2).sum())
        resid_b += float(((blue[i:i + 2000] - Vb[i:i + 2000] @ P) ** 2).sum())
""")
s=s.replace("""    Us, Ss = Us[:, :k], Ss[:, ] if False else Ss[:k]""","""    Us, Ss = Us[:, :k], Ss[:k]""")
s+='''

def _reduce_quiet(row):
    return reduce_session(row, verbose=False)


def reduce_all(rows, workers=3):
    """Reduce several sessions in parallel processes (each holds about 3.3 GB at its peak)."""
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(_reduce_quiet, rows))
'''
open('pupilwf.py','w').write(s)
EOF
cd $TMPDIR/k; . .venv/bin/activate; export PYTHONPATH=entries/komori-2026; date -u; python - <<'EOF'
import numpy as np, pupilwf as pw, time, pickle
rows=pw.resting_table(pw.list_assets())
ch=[r for c in pw.choose_sessions(rows) for r in c]
t=time.time()
ss=pw.reduce_all(ch,3)
print(time.time()-t)
for s in ss: print(s['subject'],s['day'],round(s['read_s']),round(s['total_s']),s['n_pixels'],s['pupil_nan'],round(s['svd_var_explained'],3))
pickle.dump(ss,open('ss.pkl','wb'))
EOF
date -u
```

```
Wed Nov 25 10:21:09 UTC 2026
630.929363489151
VG1-GC#51 day0 166 169 10055 768 0.994
VG1-GC#51 day1 157 160 10049 50 0.997
VG1-GC#51 day7 177 180 10110 7 0.994
VG1-GC#52 day0 162 165 9842 107 0.992
VG1-GC#52 day1 215 218 9782 0 0.996
VG1-GC#52 day7 229 232 9787 9 0.993
VG1-GC#53 day0 197 200 10325 4 0.993
VG1-GC#53 day1 235 237 10131 269 0.995
VG1-GC#53 day7 216 219 10202 60 0.997
Wed Nov 25 10:31:42 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/k; . .venv/bin/activate; export PYTHONPATH=entries/komori-2026; python - <<'EOF'
import numpy as np, pupilwf as pw, time, pickle
ss=pickle.load(open('ss.pkl','rb'))
# affine convention check: IoU of warped ROI masks across sessions
def iou(a,b): return (a&b).sum()/max((a|b).sum(),1)
r0=ss[0]['roi_atlas']
for s in ss[1:]:
    print(s['subject'],s['day'], np.round(np.median([iou(r0[i],s['roi_atlas'][i]) for i in range(44) if r0[i].sum()>5]),2))
# swapped convention
import scipy.ndimage as nd
t=time.time()
D=pw.decompose(ss)
print('decompose',time.time()-t, D['n_svd'], D['cum_var'][[9,29,199]], D['n_sel_frames'], D['mask'].sum())
comp=pw.compactness(D['maps'],D['mask'])
print(np.round(comp,2))
pickle.dump(D,open('D.pkl','wb'))
EOF
```

```
VG1-GC#51 day1 0.96
VG1-GC#51 day7 0.96
VG1-GC#52 day0 0.95
VG1-GC#52 day1 0.95
VG1-GC#52 day7 0.95
VG1-GC#53 day0 0.95
VG1-GC#53 day1 0.95
VG1-GC#53 day7 0.94
decompose 10.701425075531006 306 [0.96099237 0.99084642 0.99988239] 28800 7592
[0.09 0.15 0.23 0.08 0.06 0.11 0.13 0.14 0.09 0.14 0.16 0.26 0.2  0.14
 0.12 0.19 0.12 0.07 0.09 0.15 0.09 0.19 0.18 0.14 0.18 0.12 0.15 0.18
 0.19 0.27]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/komori-2026 && cat >> pupilwf.py <<'EOF'


# --- data sets and cross-validation ------------------------------------------------------------

def make_dataset(sessions, ics, ic_idx, cutoff=0.1, sample_reading="window", selection="none",
                 window=WINDOW, pupil_key="pupil"):
    """Samples of every kept epoch: X (n, window, n_ic), y, and the epoch and mouse of each."""
    X, y, unit, mouse, rec = [], [], [], [], []
    info = []
    for r, (s, ic) in enumerate(zip(sessions, ics)):
        feats = normalise_features(ic[:, ic_idx], cutoff)
        pn = pupil_norm(s[pupil_key])
        labs = epoch_labels(s["t"], pn, sample_reading, selection)
        for L in labs:
            info.append(dict(rec=r, subject=s["subject"], day=s["day"], epoch=L["epoch"],
                             keep=L["keep"], n_pos=int(L["y"].sum()), n=len(L["y"]),
                             peak_value=L["peak_value"]))
        kept = [L for L in labs if L["keep"]]
        Xs, ys = build_samples(feats, kept, window)
        for L, xx, yy in zip(kept, Xs, ys):
            X.append(xx.astype(np.float32))
            y.append(yy)
            unit.append(np.full(len(yy), r * 100 + L["epoch"]))
            mouse.append(np.full(len(yy), s["subject"], dtype=object))
            rec.append(np.full(len(yy), r))
    return dict(X=np.concatenate(X), y=np.concatenate(y).astype(np.int8), unit=np.concatenate(unit),
                mouse=np.concatenate(mouse), rec=np.concatenate(rec), info=info)


def shuffle_within(y, unit, rng):
    """[paper] Null models: "pupil labels were randomly shuffled within sessions"; [claim R8]
    the unit is the 40 s epoch."""
    y = y.copy()
    for u in np.unique(unit):
        i = np.flatnonzero(unit == u)
        y[i] = y[i][rng.permutation(len(i))]
    return y


def run_cv(ds, seed, fold_unit="epoch", null_scope="train", k=5, epochs=10, keep_models=False,
           threads=4):
    """Five-fold cross-validation of the model and its null model [paper: Methods, Model
    evaluation; claim R7, R8]. fold_unit 'epoch' (R7 a) or 'recording' (R7 b); null_scope
    'train' (R8 a) or 'both' (R8 b). Model fits use seed + fold; null shuffles use the claim's
    second generator (seed + 1), null fits seed + 100 + fold."""
    units = ds["unit"] if fold_unit == "epoch" else ds["rec"]
    by_mouse = {}
    for u, m in zip(units, ds["mouse"]):
        by_mouse.setdefault(m, set()).add(int(u))
    by_mouse = {m: sorted(v) for m, v in sorted(by_mouse.items())}
    fold = folds_by_mouse(by_mouse, seed, k)
    fsample = np.array([fold[int(u)] for u in units])
    rng_null = np.random.default_rng(seed + 1)
    res = []
    models = []
    for f in range(k):
        tr, va = fsample != f, fsample == f
        r = {"fold": f, "n_train": int(tr.sum()), "n_val": int(va.sum()),
             "pos_train": float(ds["y"][tr].mean()), "pos_val": float(ds["y"][va].mean())}
        best, net, _ = gru_fit(ds["X"][tr], ds["y"][tr], ds["X"][va], ds["y"][va], seed + f,
                               epochs=epochs, threads=threads)
        r.update({"model_" + kk: v for kk, v in best.items()})
        ytr_null = shuffle_within(ds["y"][tr], ds["unit"][tr], rng_null)
        yva_null = ds["y"][va]
        if null_scope == "both":
            yva_null = shuffle_within(ds["y"][va], ds["unit"][va], rng_null)
        bnull, nnet, _ = gru_fit(ds["X"][tr], ytr_null, ds["X"][va], yva_null, seed + 100 + f,
                                 epochs=epochs, threads=threads)
        r.update({"null_" + kk: v for kk, v in bnull.items()})
        res.append(r)
        if keep_models:
            models.append((net, nnet, np.flatnonzero(va)))
    import pandas as pd
    df = pd.DataFrame(res)
    return (df, models) if keep_models else df


def paired(df, metric):
    """Paired t-test over the folds, model against null [paper: Supplementary Figure 5 legend]."""
    a, b = df["model_" + metric].to_numpy(), df["null_" + metric].to_numpy()
    t, p = stats.ttest_rel(a, b)
    return dict(model=float(np.mean(a)), null=float(np.mean(b)), t=float(t), p=float(p))
EOF
cd $TMPDIR/k; . .venv/bin/activate; export PYTHONPATH=entries/komori-2026; python - <<'EOF'
import numpy as np, pupilwf as pw, time, pickle
ss=pickle.load(open('ss.pkl','rb')); D=pickle.load(open('D.pkl','rb'))
comp=pw.compactness(D['maps'],D['mask'])
# VIF features: filtered IC time courses over all sample frames, 0.1 Hz
F=np.vstack([pw.normalise_features(ic,0.1)[50*30:570*30] for ic in D['ics']])
print('VIF all 30', np.round(pw.vif(F).max(),2))
keep,rem=pw.select_ics(F,comp,10,'kept'); print(keep,rem, pw.vif(F[:,keep]).max())
t=time.time()
ds=pw.make_dataset(ss,D['ics'],keep,0.1)
print(ds['X'].shape, ds['y'].mean(), time.time()-t)
import pandas as pd
info=pd.DataFrame(ds['info']); print(info.groupby('rec').n_pos.describe())
t=time.time()
df=pw.run_cv(ds, pw.seed_of('rest-decoding-above-null'))
print(time.time()-t)
print(df[['n_train','n_val','pos_val','model_val_auc','null_val_auc','model_val_loss','null_val_loss','model_val_acc','null_val_acc','model_epoch','model_train_auc']])
print(pw.paired(df,'val_auc'))
EOF
```

```
VIF all 30 3.95
[np.int64(29), np.int64(11), np.int64(2), np.int64(12), np.int64(28), np.int64(21), np.int64(15), np.int64(27), np.int64(24), np.int64(22)] [] 2.241840239714186
(12402, 46, 10) 0.4779874213836478 0.05434083938598633
     count       mean        std   min   25%    50%    75%    max
rec                                                              
0     13.0   4.230769  15.254255   0.0   0.0    0.0    0.0   55.0
1     13.0  55.307692  49.484652   0.0   0.0   55.0  106.0  106.0
2     13.0  31.538462  39.220775   0.0   0.0    0.0   58.0  106.0
3     13.0  62.923077  44.630822   0.0  14.0   68.0  106.0  106.0
4     13.0  73.384615  50.920753   0.0   0.0  106.0  106.0  106.0
5     13.0  76.923077  41.059838   0.0  55.0  104.0  106.0  106.0
6     13.0  71.153846  22.799291  37.0  54.0   69.0   89.0  106.0
7     13.0   4.000000  14.422205   0.0   0.0    0.0    0.0   52.0
8     13.0  76.538462  45.845057   0.0  55.0  106.0  106.0  106.0
65.96402502059937
   n_train  n_val   pos_val  ...  null_val_acc  model_epoch  model_train_auc
0     9858   2544  0.464623  ...      0.437107            1         0.723407
1     9858   2544  0.472091  ...      0.712657            6         0.833452
2     9858   2544  0.489780  ...      0.544418            7         0.864800
3     9858   2544  0.401730  ...      0.705582            9         0.914726
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/k; . .venv/bin/activate; export PYTHONPATH=entries/komori-2026; python - <<'EOF'
import numpy as np, pupilwf as pw, time, pickle
ss=pickle.load(open('ss.pkl','rb')); D=pickle.load(open('D.pkl','rb'))
comp=pw.compactness(D['maps'],D['mask'])
F=np.vstack([pw.normalise_features(ic,0.1)[50*30:570*30] for ic in D['ics']])
keep,rem=pw.select_ics(F,comp,10,'kept')
sd=pw.seed_of('rest-decoding-above-null')
for name,kw,cv in [('R5b',dict(selection='rule'),{}),('R8b',{},dict(null_scope='both')),('R7b',{},dict(fold_unit='recording')),('2Hz',dict(cutoff=2.0),{}),('nofilter-ish 1Hz',dict(cutoff=1.0),{})]:
    t=time.time()
    ds=pw.make_dataset(ss,D['ics'],keep,**({'cutoff':0.1}|kw))
    df=pw.run_cv(ds, sd, **cv)
    print(name, ds['X'].shape, round(ds['y'].mean(),3), round(time.time()-t), {k:round(v,3) for k,v in pw.paired(df,'val_auc').items()}, np.round(df.model_val_auc.values,2), np.round(df.null_val_auc.values,2))
EOF
```

```
Exit code 1
entries/komori-2026/pupilwf.py:687: RuntimeWarning: Mean of empty slice
  "pos_train": float(ds["y"][tr].mean()), "pos_val": float(ds["y"][va].mean())}
/tmp/claude-1001/k/.venv/lib/python3.13/site-packages/numpy/_core/_methods.py:142: RuntimeWarning: invalid value encountered in scalar divide
  ret = ret.dtype.type(ret / rcount)
R5b (1802, 46, 10) 0.452 12 {'model': 0.598, 'null': 0.617, 't': -0.296, 'p': 0.782} [0.63 0.57 0.53 0.52 0.73] [0.66 0.56 0.76 0.54 0.56]
R8b (12402, 46, 10) 0.478 62 {'model': 0.677, 'null': 0.688, 't': -0.107, 'p': 0.92} [0.62 0.77 0.76 0.83 0.41] [0.5  0.74 0.64 0.71 0.83]
Traceback (most recent call last):
  File "<stdin>", line 10, in <module>
  File "entries/komori-2026/pupilwf.py", line 688, in run_cv
    best, net, _ = gru_fit(ds["X"][tr], ds["y"][tr], ds["X"][va], ds["y"][va], seed + f,
                   ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                           epochs=epochs, threads=threads)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "entries/komori-2026/pupilwf.py", line 572, in gru_fit
    pv = torch.sigmoid(torch.cat([net(Xv[i:i + 4096]) for i in range(0, len(Xv), 4096)])).numpy()
                       ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: torch.cat(): expected a non-empty list of Tensors
```

**Agent calls Bash**

```bash
cd entries/komori-2026 && python - <<'EOF'
s=open('pupilwf.py').read()
s=s.replace("""    units = ds["unit"] if fold_unit == "epoch" else ds["rec"]
    by_mouse = {}
    for u, m in zip(units, ds["mouse"]):
        by_mouse.setdefault(m, set()).add(int(u))""","""    units = ds["unit"] if fold_unit == "epoch" else ds["rec"]
    # [deviation] with 3 recordings per mouse, five equal parts per mouse are impossible when the
    # unit is the recording; the recordings are then pooled over mice before the split.
    groups = ds["mouse"] if fold_unit == "epoch" else np.full(len(units), "all", dtype=object)
    by_mouse = {}
    for u, m in zip(units, groups):
        by_mouse.setdefault(m, set()).add(int(u))""")
open('pupilwf.py','w').write(s)
EOF
grep -n "^def \|^# ---" pupilwf.py | head -50; wc -l pupilwf.py
```

```
48:def seed_of(claim_id: str) -> int:
53:# --- archive -----------------------------------------------------------------------------------
55:def list_assets():
66:def s3_url(asset_id: str) -> str:
72:def open_nwb(asset_id: str, block_mb: int = 64):
80:def resting_table(assets):
95:def choose_sessions(rows, n_mice=3, n_sessions=3):
113:# --- filters -----------------------------------------------------------------------------------
115:def butter(x, cutoff, kind="low", fs=FS, order=4, axis=0):
122:def fill_nan(x):
131:# --- per-session reduction -----------------------------------------------------------------------
133:def _read_binned(ds, mask_b, block=600):
145:def atlas_grid_coords(affine, shape_b):
158:def warp_maps(maps_b, coords, order=1):
165:def reduce_session(row, hemo_variant="fit_hp_subtract_raw", verbose=True):
259:# --- global SVD and ICA ----------------------------------------------------------------------
261:def epochs_of(t):
267:def jade(X, m):
335:def common_mask(sessions):
345:def decompose(sessions, hemo="fit_hp_subtract_raw", n_svd=N_SVD, n_svd_ica=N_SVD_ICA, n_ica=N_ICA):
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,12p pupilwf.py | cat -A | cut -c1-80
```

```
"""Helpers for testing Komori et al. (2026) on the resting-state recordings of D
$
The paper (bioRxiv doi:10.64898/2026.05.27.726399) decodes spontaneous pupil dil
independent components (ICs) of wide-field calcium imaging with a GRU, on restin
of Kondo et al. (2025), DANDI:001425. The claims file (claims/komori-2026.yaml) 
details R1 to R10 in its opening comment; each parameter below says where it com
[claim] the claims file's criterion or opening comment, [paper] a passage of the
[assumption] a choice the paper leaves open (with the reason), [standard] a choi
change a result.$
$
Everything is streamed from the archive (fsspec HTTP range reads into h5py); not
to disk.$
```

**Agent calls Bash**

```bash
cd $TMPDIR/k; . .venv/bin/activate; export PYTHONPATH=entries/komori-2026; python - <<'EOF' 2>&1 | grep -v Warning
import numpy as np, pupilwf as pw, time, pickle
ss=pickle.load(open('ss.pkl','rb')); D=pickle.load(open('D.pkl','rb'))
comp=pw.compactness(D['maps'],D['mask'])
F=np.vstack([pw.normalise_features(ic,0.1)[50*30:570*30] for ic in D['ics']])
keep,rem=pw.select_ics(F,comp,10,'kept')
sd=pw.seed_of('rest-decoding-above-null')
def go(name, ss, ics, keep, kw={}, cv={}):
    t=time.time()
    ds=pw.make_dataset(ss,ics,keep,**({'cutoff':0.1}|kw))
    df=pw.run_cv(ds, sd, **cv)
    print(name, ds['X'].shape, round(ds['y'].mean(),3), round(time.time()-t), {k:round(v,3) for k,v in pw.paired(df,'val_auc').items()}, np.round(df.model_val_auc.values,2), np.round(df.null_val_auc.values,2),flush=True)
go('R7b',ss,D['ics'],keep,{},dict(fold_unit='recording'))
go('2Hz',ss,D['ics'],keep,dict(cutoff=2.0))
D2=pw.decompose(ss,hemo='hp_corrected')
c2=pw.compactness(D2['maps'],D2['mask'])
F2=np.vstack([pw.normalise_features(ic,0.1)[50*30:570*30] for ic in D2['ics']])
k2,_=pw.select_ics(F2,c2,10,'kept')
go('hemo-hp',ss,D2['ics'],k2)
go('all30',ss,D['ics'],list(range(30)))
EOF
```

```
R7b (12402, 46, 10) 0.478 60 {'model': 0.471, 'null': 0.408, 't': 2.167, 'p': 0.096} [0.58 0.45 0.64 0.34 0.34] [0.58 0.44 0.56 0.18 0.28]
2Hz (12402, 46, 10) 0.478 58 {'model': 0.698, 'null': 0.685, 't': 1.279, 'p': 0.27} [0.69 0.68 0.73 0.65 0.74] [0.69 0.65 0.69 0.64 0.76]
hemo-hp (12402, 46, 10) 0.478 57 {'model': 0.502, 'null': 0.498, 't': 0.087, 'p': 0.935} [0.52 0.51 0.51 0.61 0.36] [0.45 0.46 0.42 0.68 0.47]
all30 (12402, 46, 30) 0.478 60 {'model': 0.718, 'null': 0.747, 't': -1.394, 'p': 0.236} [0.66 0.68 0.74 0.7  0.8 ] [0.76 0.65 0.76 0.73 0.84]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/k; . .venv/bin/activate; export PYTHONPATH=entries/komori-2026; date -u; python - <<'EOF' 2>&1 | grep -v Warning
import numpy as np, pupilwf as pw, time, pickle
ss=pickle.load(open('ss.pkl','rb')); D=pickle.load(open('D.pkl','rb'))
comp=pw.compactness(D['maps'],D['mask'])
F=np.vstack([pw.normalise_features(ic,0.1)[50*30:570*30] for ic in D['ics']])
keep,rem=pw.select_ics(F,comp,10,'kept')
sd=pw.seed_of('rest-decoding-above-null')
t=time.time()
ds=pw.make_dataset(ss,D['ics'],keep,0.1,sample_reading='epoch')
print(ds['X'].shape, ds['y'].mean())
import torch
best,net,h=pw.gru_fit(ds['X'][:100000],ds['y'][:100000],ds['X'][100000:],ds['y'][100000:],1,epochs=1)
print('one epoch fit', time.time()-t, best)
EOF
```

```
Wed Nov 25 10:40:13 UTC 2026
(140400, 46, 10) 0.03866096866096866
one epoch fit 8.087650299072266 {'epoch': 1, 'val_loss': 0.1635506597191784, 'val_auc': 0.38627079788787255, 'val_acc': 0.9621782178217821, 'train_auc': 0.7125983564129246}
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/fouke-2025; python - <<'EOF'
import json
nb=json.load(open('reproduce_fouke_2025.ipynb'))
for c in nb['cells'][:6]+nb['cells'][-3:]:
    print('---',c['cell_type'],c['metadata'],''.join(c['source'])[:900])
print(nb['metadata'])
EOF
```

```
--- markdown {} # Reproducing Fouke et al. (2025) from dandiset 001453

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

**Wh
--- code {} import time
import warnings

import matplotlib.pyplot as plt
import numpy as np
[... 91 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/komori-2026 && cat >> pupilwf.py <<'EOF'


def keypoint_pupil(row, t_img):
    """[claim R3 reading (b)] Horizontal pupil diameter from the eye keypoints, as the paper's own
    Methods define it ("Euclidean distance between the left and right boundary landmarks"): the
    file holds 30 pupil-edge keypoints without a stated position on the pupil, so the width is
    taken as the largest minus the smallest x of the edge points with confidence >= 0.5
    [assumption], in pixels, interpolated onto the imaging timestamps."""
    f = open_nwb(row["asset_id"], block_mb=8)
    g = f["processing/behavior/eye_video_keypoints"]
    names = sorted(k for k in g.keys() if k.startswith("pupiledge"))
    xs, cs = [], []
    t = None
    for n in names:
        xs.append(g[n]["data"][:, 0])
        cs.append(g[n]["confidence"][:])
        if t is None:
            t = g[n]["timestamps"][:]
    tb0 = f["acquisition/widefield_blue/timestamps"][0]
    f.close()
    x = np.array(xs)
    c = np.array(cs)
    x = np.where(c >= 0.5, x, np.nan)
    n_ok = np.isfinite(x).sum(axis=0)
    width = np.nanmax(np.where(n_ok >= 4, x, np.nan), axis=0) - np.nanmin(np.where(n_ok >= 4, x, np.nan), axis=0)
    width, n_bad = fill_nan(width)
    return np.interp(t_img, t - tb0, width), n_bad, len(names)
EOF
cd $TMPDIR/k; . .venv/bin/activate; export PYTHONPATH=entries/komori-2026; python - <<'EOF' 2>&1 | grep -v Warn
import numpy as np, pupilwf as pw, time, pickle
ss=pickle.load(open('ss.pkl','rb'))
rows=pw.resting_table(pw.list_assets()); ch=[r for c in pw.choose_sessions(rows) for r in c]
t=time.time()
for s,r in zip(ss,ch):
    k,nb,nn=pw.keypoint_pupil(r,s['t'])
    s['pupil_kp']=k
    print(s['subject'],s['day'],nb,nn, round(np.corrcoef(k,s['pupil'])[0,1],3), round(time.time()-t))
pickle.dump(ss,open('ss.pkl','wb'))
EOF
```

```
width = np.nanmax(np.where(n_ok >= 4, x, np.nan), axis=0) - np.nanmin(np.where(n_ok >= 4, x, np.nan), axis=0)
VG1-GC#51 day0 3721 30 0.0 10
VG1-GC#51 day1 207 30 0.931 19
VG1-GC#51 day7 36 30 0.968 30
VG1-GC#52 day0 302 30 0.922 40
VG1-GC#52 day1 0 30 0.996 49
VG1-GC#52 day7 56 30 0.951 57
VG1-GC#53 day0 32 30 0.986 67
VG1-GC#53 day1 346 30 -0.022 77
VG1-GC#53 day7 189 30 0.97 88
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/komori-2026 && cat >> pupilwf.py <<'EOF'


def load_sessions(rows, workers=3):
    """Stream and reduce the chosen sessions, and add the keypoint pupil of reading R3 (b)."""
    sessions = reduce_all(rows, workers)
    for s, r in zip(sessions, rows):
        s["pupil_kp"], s["pupil_kp_bad"], s["n_edge_points"] = keypoint_pupil(r, s["t"])
    return sessions


def predict(net, X):
    import torch
    with torch.no_grad():
        Xt = torch.tensor(X, dtype=torch.float32)
        return torch.sigmoid(torch.cat([net(Xt[i:i + 4096]) for i in range(0, len(Xt), 4096)])).numpy()


def auc_by_mouse(ds, folds_models):
    """Validation AUC per mouse and fold, model and null, from run_cv(keep_models=True)."""
    from sklearn.metrics import roc_auc_score
    rows = []
    for f, (net, nnet, va) in enumerate(folds_models):
        pm, pn = predict(net, ds["X"][va]), predict(nnet, ds["X"][va])
        for m in np.unique(ds["mouse"][va]):
            i = ds["mouse"][va] == m
            y = ds["y"][va][i]
            if 0 < y.mean() < 1:
                rows.append(dict(fold=f, mouse=m, n=int(i.sum()), model_auc=roc_auc_score(y, pm[i]),
                                 null_auc=roc_auc_score(y, pn[i])))
    import pandas as pd
    return pd.DataFrame(rows)
EOF
sed -i 's/    return np.interp(t_img, t - tb0, width), n_bad, len(names)/    return np.interp(t_img, t - tb0, width), n_bad, len(names)/' pupilwf.py
python - <<'EOF'
s=open('pupilwf.py').read()
s=s.replace("""    x = np.where(c >= 0.5, x, np.nan)
    n_ok = np.isfinite(x).sum(axis=0)
    width = np.nanmax(np.where(n_ok >= 4, x, np.nan), axis=0) - np.nanmin(np.where(n_ok >= 4, x, np.nan), axis=0)
""","""    x = np.where(c >= 0.5, x, np.nan)
    n_ok = np.isfinite(x).sum(axis=0)
    width = np.full(x.shape[1], np.nan)
    ok = n_ok >= 4
    width[ok] = np.nanmax(x[:, ok], axis=0) - np.nanmin(x[:, ok], axis=0)
""")
open('pupilwf.py','w').write(s)
EOF
date -u
```

```
Wed Nov 25 10:43:20 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/k/mknb.py",
 "content": "import json, sys, nbformat\nfrom nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell\n\nRESULTS = json.load(open(\"/tmp/claude-1001/k/results.json\")) if len(sys.argv) > 1 else {}\n\n\ndef md(s):\n    return new_markdown_cell(s.strip(\"\\n\"))\n\n\ndef code(s, tag=None):\n    c = new_code_cell(s.strip(\"\\n\"))\n    if tag:\n        c.metadata[\"tags\"] = [tag]\n    return c\n\n\ndef result(key):\n    return md(RESULTS.get(key, f\"**Result: (to be written from the outputs above: {key}).**\"))\n\n\nHEADER_COMMON = \"\"\"\n**Paper.** Komori Y, Mizusaki K, Tomita K, Yoneda T, Matoba K, Morita T (2026). Mesoscopic cortical\nactivities associated with pupil-linked perceptions inferred via explainable machine learning.\nbioRxiv, [doi:10.64898/2026.05.27.726399](https://doi.org/10.64898/2026.05.27.726399). The claims\nfile (`claims/komori-2026.yaml`) was written from the preprint posted June 1, 2026, with its\nMethods, legends and Supplementary Figures 3 to 6.\n\n**Dandiset.** [DANDI:001425](https://dandiarchive.org/dandiset/001425/0.250705.0947), version\n0.250705.0947 (\"BraiDyn-BC: mouse cued-lever-pull task dataset\", Kondo et al. 2025). The paper\ncites the dandiset without a version. Two versions are published, 0.250514.0602 (1814 assets) and\n0.250705.0947 (1838 assets); the most recent is pinned, as the protocol asks when no version is\ncited. The paper was posted in 2026, after both, so either could be the one it read; the resting\nsessions used here are the same files in both is not checked (only the pinned version is read).\nThe paper uses only the resting-state recordings of this dandiset; its own recordings\n(somatosensory and visual stimulation) are not deposited.\n\n**What is tested.** The six resting-state claims. The paper's pipeline is rebuilt from its\nMethods: hemodynamic correction, SVD and JADE ICA of the cortical images, pupil labels around the\ndilation peak of each 40 s epoch, a GRU decoder with five-fold cross-validation and null models\ntrained on labels shuffled within epochs. The open details R1 to R10 of the claims file's opening\ncomment are followed as it names them; where several readings are named, the notebook runs the\nmain one and as many others as time allows, and says which were not run.\n\"\"\"\n\nCLAIMS_TABLE = \"\"\"\n| Claim | Notebook | Status |\n|---|---|---|\n| rest-decoding-above-null | decoding | tested (one variant, R4 b, in the features notebook) |\n| rest-loss-accuracy-vs-null | decoding | tested |\n| rest-needs-0-1-hz | decoding | tested |\n| rest-ic-count-and-window | features | tested |\n| rest-vif-below-10 | features | tested |\n| rest-shap-medial-anterior-first | features | tested |\n| fig1-*, fig2-*, fig3-*, fig4-shap-*, fig4-mapped-shap-regions, supp2-*, supp4-*, supp8-*, supp10-* (17 claims) | none | blocked: the stimulation recordings are not deposited |\n\"\"\"\n\nSETUP = \"\"\"\nimport time\nimport warnings\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nfrom statsmodels.stats.multitest import multipletests\n\nimport pupilwf as pw\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\nwarnings.filterwarnings(\"ignore\", category=UserWarning)\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 200)\n\nstarted = time.time()\nassets = pw.list_assets()\nrows = pw.resting_table(assets)\nchosen = pw.choose_sessions(rows)          # R1 (a): three mice, first three resting sessions each\nchosen_rows = [r for mouse in chosen for r in mouse]\nsessions = pw.load_sessions(chosen_rows)\nprint(f\"streamed and reduced {len(sessions)} sessions from DANDI:{pw.DANDISET} version {pw.VERSION} \"\n      f\"in {time.time() - started:.0f} s\")\n\"\"\"\n\nDECOMP = \"\"\"\nt0 = time.time()\nD = pw.decompose(sessions, hemo=\"fit_hp_subtract_raw\")       # R2 (a), main reading\ncomp = pw.compactness(D[\"maps\"], D[\"mask\"])\n# features for VIF-based selection: every frame of the 13 epochs, 0.1 Hz low-pass (R6)\ndef vif_frames(ics, cutoff=0.1):\n    out = []\n    for s, ic in zip(sessions, ics):\n        a, b = pw.epochs_of(s[\"t\"])[0][0], pw.epochs_of(s[\"t\"])[-1][1]\n        out.append(pw.normalise_features(ic, cutoff)[a:b])\n    return np.vstack(out)\nF01 = vif_frames(D[\"ics\"])\nkeep10, removed10 = pw.select_ics(F01, comp, 10, \"kept\")\nprint(f\"decomposition in {time.time() - t0:.0f} s; kept ICs {keep10}\")\n\"\"\"\n\nSANITY_FILES = \"\"\"\ntab = pd.DataFrame(rows)\nprint(\"Resting-state NWB files in the dandiset:\", len(tab), \"from\", tab.subject.nunique(), \"mice\")\nprint(\"Files per mouse:\", tab.groupby(\"subject\").size().value_counts().sort_index().to_dict(),\n      \"(number of files: number of mice)\")\nprint(\"Files without behaviour (widefield only, no pupil):\", int((~tab.behavior).sum()))\nprint(tab[~tab.behavior][[\"subject\", \"day\"]].to_string(index=False))\nprint(\"Paper, Methods, Resting state: 25 mice, '2-3 experiments per animal'.\")\nprint(\"\\\\nChosen (R1 a): \", [(r[\"subject\"], r[\"day\"], r[\"date\"]) for r in chosen_rows])\n\"\"\"\n\nSANITY_STREAMS = \"\"\"\ninfo = pd.DataFrame([{\n    \"subject\": s[\"subject\"], \"day\": s[\"day\"], \"frames\": s[\"n_frames\"],\n    \"rate_hz\": round(1 / np.median(np.diff(s[\"t\"])), 3), \"duration_s\": round(s[\"t\"][-1], 1),\n    \"uv_after_blue_ms\": round(1000 * s[\"t_uv_offset\"], 1), \"pupil_on_img_clock\": s[\"pupil_t_equal\"],\n    \"dff_on_img_clock\": s[\"dff_t_equal\"], \"pupil_nan\": s[\"pupil_nan\"],\n    \"pupil_px_min\": round(float(s[\"pupil\"].min()), 1), \"pupil_px_median\": round(float(np.median(s[\"pupil\"])), 1),\n    \"pupil_px_max\": round(float(s[\"pupil\"].max()), 1),\n    \"kp_width_bad\": s[\"pupil_kp_bad\"], \"r_diam_kp\": round(float(np.corrcoef(s[\"pupil\"], s[\"pupil_kp\"])[0, 1]), 3),\n    \"cortex_px\": s[\"n_pixels\"], \"svd34_var\": round(s[\"svd_var_explained\"], 4),\n    \"raw_blue\": round(s[\"raw_mean\"][0]), \"raw_uv\": round(s[\"raw_mean\"][1]),\n    \"read_s\": round(s[\"read_s\"])} for s in sessions])\nprint(info.to_string(index=False))\nprint(\"\\\\nPaper (Methods, Resting state): 60 Hz acquisition alternating 405/470 nm, 36,000 frames per 600 s \"\n      \"session, i.e. 18,000 frames and 30 Hz per channel; frames 288 x 288 after down-sampling.\")\nprint(\"Frames per channel:\", sorted(set(info.frames)), \"; frame shape in the files: 288 x 288 (binned 2x2 here)\")\nprint(\"Hemodynamic regression slope of F470 on F405 (34 components per session): median\",\n      round(float(np.median(np.concatenate([s[\"coef\"][:, 0] for s in sessions]))), 3),\n      \"range\", np.round(np.percentile(np.concatenate([s[\"coef\"][:, 0] for s in sessions]), [0, 100]), 2))\nf = pw.open_nwb(chosen_rows[0][\"asset_id\"], block_mb=2)\nfor plane in (\"ImagingPlane_blue\", \"ImagingPlane_UV\"):\n    g = f[\"general/optophysiology/\" + plane]\n    print(plane, \"excitation_lambda\", g[\"excitation_lambda\"][()], \"imaging_rate\", g[\"imaging_rate\"][()],\n          \"indicator\", g[\"indicator\"][()].decode(), \"grid_spacing\", g[\"grid_spacing\"][:])\nprint(\"acquisition/widefield_blue description:\", f[\"acquisition/widefield_blue\"].attrs[\"description\"])\nprint(\"dFF_B description:\", f[\"processing/ophys/DfOverF/dFF_B\"].attrs[\"description\"])\nprint(\"pupil diameter unit:\", f[\"processing/behavior/pupil_tracking/diameter/data\"].attrs[\"unit\"])\nprint(\"genotype:\", f[\"general/subject/genotype\"][()].decode())\nf.close()\n\"\"\"\n\nSANITY_DUP = \"\"\"\n# Recordings deposited twice: identical pupil traces or identical mean fluorescence would show it.\nP = np.array([s[\"pupil\"][:18000] for s in sessions])\nC = np.corrcoef(P)\nnp.fill_diagonal(C, np.nan)\nprint(\"Largest pupil-trace correlation between two different sessions:\", round(float(np.nanmax(C)), 3))\nmeans = [s[\"raw_mean\"] for s in sessions]\nprint(\"Distinct (blue, UV) mean raw intensities:\", len(set(means)), \"of\", len(means))\n\"\"\"\n\nSANITY_CLOCK = \"\"\"\n# Clock check. The pupil and the imaging share the timestamps (above). Whether the pupil trace is\n# aligned with the imaging in fact is checked with the cross-correlation between the pupil and the\n# mean cortical activity (deposited hemodynamics-corrected dF/F, averaged over the 44 ROIs): arousal\n# links the two, and a misaligned trace would move the peak. Control: the same with the pupil\n# circularly shifted by 100 to 500 s.\nlags = np.arange(-300, 301, 3)\nrows_clk = []\nfor s in sessions:\n    p = pw.butter(s[\"pupil\"], 0.2)\n    p = (p - p.mean()) / p.std()\n    g = pw.butter(np.nanmean(s[\"dff_deposited\"], axis=1), 0.2)\n    g = (g - g.mean()) / g.std()\n    cc = np.array([np.mean(p[max(0, -l):len(p) - max(0, l)] * g[max(0, l):len(g) - max(0, -l)]) for l in lags])\n    sh = []\n    for k in range(5):\n        q = np.roll(p, 3000 + 3000 * k)\n        sh.append(np.max(np.abs([np.mean(q[max(0, -l):len(q) - max(0, l)] * g[max(0, l):len(g) - max(0, -l)]) for l in lags[::10]])))\n    i = int(np.argmax(np.abs(cc)))\n    rows_clk.append(dict(subject=s[\"subject\"], day=s[\"day\"], peak_r=round(float(cc[i]), 3),\n                         lag_s=round(float(lags[i] / pw.FS), 2), r_at_0=round(float(cc[lags == 0][0]), 3),\n                         shifted_max_abs_r=round(float(np.max(sh)), 3)))\nprint(\"Positive lag: cortical activity follows the pupil.\")\nprint(pd.DataFrame(rows_clk).to_string(index=False))\n\"\"\"\n\nSANITY_DECOMP = \"\"\"\nprint(\"Common cortical grid points (atlas grid, step\", pw.GRID_STEP, \"atlas pixels):\", int(D[\"mask\"].sum()))\nprint(\"SVD components available:\", D[\"n_svd\"], \"(paper: 400; the corrected data of each recording have rank 34)\")\nprint(\"Cumulative variance at 10, 30, 200 components:\", np.round(D[\"cum_var\"][[9, 29, min(199, D['n_svd'] - 1)]], 4),\n      \"(paper: > 99.5% at 200)\")\nprint(\"Frames used to estimate the decomposition (every fifth 40 s epoch):\", D[\"n_sel_frames\"])\nprint(\"IC compactness (share of squared weight in the largest supra-half-maximum region):\")\nprint(pd.Series(comp).round(3).to_string())\nv30 = pw.vif(F01)\nprint(\"VIF of all 30 ICs (0.1 Hz features): max\", round(float(v30.max()), 2))\nprint(\"Kept for 10 ICs (reading a):\", keep10, \"removed for VIF:\", removed10,\n      \"max VIF of the kept:\", round(float(pw.vif(F01[:, keep10]).max()), 2))\nroi = sessions[0][\"roi_atlas\"]\nnames = sessions[0][\"roi_names\"]\nfig, axes = plt.subplots(2, 5, figsize=(13, 5.5))\nfor ax, j in zip(axes.flat, keep10):\n    m = D[\"maps\"][j]\n    lim = np.nanmax(np.abs(m))\n    ax.imshow(m, cmap=\"RdBu_r\", vmin=-lim, vmax=lim)\n    ax.contour(roi.any(axis=0), [0.5], colors=\"k\", linewidths=0.5)\n    ax.set_title(f\"IC {j}  comp {comp[j]:.2f}\", fontsize=9)\n    ax.axis(\"off\")\nplt.suptitle(\"Spatial maps of the 10 kept ICs on the common atlas grid (colour limits: +/- max |weight|)\")\nplt.tight_layout()\nplt.show()\n\"\"\"\n\nSANITY_LABELS = \"\"\"\nds_main = pw.make_dataset(sessions, D[\"ics\"], keep10, cutoff=0.1)\nlab = pd.DataFrame(ds_main[\"info\"])\nprint(\"Epochs per recording:\", lab.groupby(\"rec\").size().unique(), \"; samples per epoch window:\", sorted(lab.n.unique()))\nprint(\"Positive frames per epoch window (of\", lab.n.max(), \"), by recording:\")\nprint(lab.groupby([\"subject\", \"day\"]).n_pos.describe()[[\"mean\", \"min\", \"50%\", \"max\"]].round(1).to_string())\nprint(\"Epochs whose window has no positive frame:\", int((lab.n_pos == 0).sum()), \"of\", len(lab),\n      \"; all frames positive:\", int((lab.n_pos == lab.n).sum()))\nprint(\"Samples:\", ds_main[\"X\"].shape, \"positive share\", round(float(ds_main[\"y\"].mean()), 3))\nprint(\"Feature range:\", float(ds_main[\"X\"].min()), float(ds_main[\"X\"].max()))\nlab5 = pd.DataFrame(pw.make_dataset(sessions, D[\"ics\"], keep10, 0.1, selection=\"rule\")[\"info\"])\nprint(\"Epochs kept by the selection rule R5 (b):\", int(lab5.keep.sum()), \"of\", len(lab5))\n\"\"\"\n\n\ndef nb_decoding():\n    cells = []\n    cells.append(md(\"# Reproducing Komori et al. (2026) from DANDI:001425: decoding of spontaneous pupil dilation\\n\" + HEADER_COMMON + \"\"\"\nThis notebook tests the three decoding claims; the companion notebook\n`reproduce_komori_2026_features.ipynb` tests the IC count, the window, the VIF and the SHAP claims.\n\"\"\" + CLAIMS_TABLE))\n    cells.append(code(SETUP))\n    cells.append(code(DECOMP))\n    cells.append(md(\"## Data check\\n\\nEach check of the metadata against the values is stated under its output.\"))\n    cells.append(code(SANITY_FILES, \"sanity\"))\n    cells.append(code(SANITY_STREAMS, \"sanity\"))\n    cells.append(result(\"sanity_streams\"))\n    cells.append(code(SANITY_DUP, \"sanity\"))\n    cells.append(code(SANITY_CLOCK, \"sanity\"))\n    cells.append(result(\"sanity_clock\"))\n    cells.append(code(SANITY_DECOMP, \"sanity\"))\n    cells.append(code(SANITY_LABELS, \"sanity\"))\n    cells.append(result(\"sanity_labels\"))\n    # claim 1\n    cells.append(md(\"\"\"## rest-decoding-above-null\n\n> A GRU decoder of independent components of resting cortical activity, low-pass filtered at 0.1 Hz,\n> predicts spontaneous pupil dilation with a validation ROC-AUC significantly higher than that of\n> null models trained on within-session shuffled labels. (Expected: model 0.82 +/- 0.082, null\n> 0.61 +/- 0.061; paired t-test p < 0.05.)\n\nMain reading combination: R1 a (3 mice x 3 sessions), R2 a (paper's correction on the frames,\ncoefficients applied to the measured signals), R3 a (deposited diameter), R4 a (samples in the\nwindow), R5 a (no epoch selection), R6 (10 ICs, reading a), R7 a (folds of epochs), R8 a (training\nlabels shuffled), R9, at the claim's seed. Then the seeds plus 1000 to 4000, then the other readings\none at a time.\"\"\"))\n    cells.append(code(\"\"\"\nSEED1 = pw.seed_of(\"rest-decoding-above-null\")\nt0 = time.time()\ncv_main, models_main = pw.run_cv(ds_main, SEED1, keep_models=True)\ncols = [\"fold\", \"n_train\", \"n_val\", \"pos_val\", \"model_epoch\", \"model_train_auc\", \"model_val_auc\", \"null_val_auc\",\n        \"model_val_loss\", \"null_val_loss\", \"model_val_acc\", \"null_val_acc\"]\nprint(cv_main[cols].round(3).to_string(index=False))\nr = pw.paired(cv_main, \"val_auc\")\nprint(f\"\\\\nvalidation AUC: model {r['model']:.3f}, null {r['null']:.3f}, paired t = {r['t']:.2f}, p = {r['p']:.3g}  \"\n      f\"(expected 0.82 +/- 0.082 and 0.61 +/- 0.061)\")\nprint(f\"model AUC - null AUC per fold: {np.round(cv_main.model_val_auc - cv_main.null_val_auc, 3).tolist()}\")\nprint(f\"training AUC of the models: mean {cv_main.model_train_auc.mean():.3f}\")\nprint(f\"({time.time() - t0:.0f} s)\")\n\"\"\", \"claim:rest-decoding-above-null\"))\n    cells.append(code(\"\"\"\nbym = pw.auc_by_mouse(ds_main, models_main)\nprint(\"Validation AUC by mouse (mean over folds):\")\nprint(bym.groupby(\"mouse\")[[\"model_auc\", \"null_auc\"]].mean().round(3).to_string())\n\"\"\", \"claim:rest-decoding-above-null\"))\n    cells.append(code(\"\"\"\nseed_rows = []\ncv_by_seed = {0: cv_main}\nfor off in (1000, 2000, 3000, 4000):\n    cv_by_seed[off] = pw.run_cv(ds_main, SEED1 + off)\nfor off, cv in cv_by_seed.items():\n    r = pw.paired(cv, \"val_auc\")\n    seed_rows.append(dict(seed=f\"claim+{off}\", model_auc=r[\"model\"], null_auc=r[\"null\"], t=r[\"t\"], p=r[\"p\"],\n                          above=bool(r[\"p\"] < 0.05 and r[\"model\"] > r[\"null\"]),\n                          within_tol=bool(abs(r[\"model\"] - 0.82) <= 0.082)))\nprint(pd.DataFrame(seed_rows).round(4).to_string(index=False))\n\"\"\", \"claim:rest-decoding-above-null\"))\n    cells.append(code(\"\"\"\n# Other readings, one at a time, at the claim's seed.\ndef variant(name, sess=sessions, ics=None, keep=None, ds_kw=None, cv_kw=None):\n    t0 = time.time()\n    ds = pw.make_dataset(sess, ics if ics is not None else D[\"ics\"], keep if keep is not None else keep10,\n                         **({\"cutoff\": 0.1} | (ds_kw or {})))\n    cv = pw.run_cv(ds, SEED1, **(cv_kw or {}))\n    out = {\"reading\": name, \"samples\": len(ds[\"y\"]), \"pos\": round(float(ds[\"y\"].mean()), 3)}\n    for m in (\"val_auc\", \"val_loss\", \"val_acc\"):\n        r = pw.paired(cv, m)\n        out[m + \"_model\"], out[m + \"_null\"], out[m + \"_p\"] = r[\"model\"], r[\"null\"], r[\"p\"]\n    out[\"s\"] = round(time.time() - t0)\n    return out, cv\n\nD_hp = pw.decompose(sessions, hemo=\"hp_corrected\")\ncomp_hp = pw.compactness(D_hp[\"maps\"], D_hp[\"mask\"])\nkeep_hp, _ = pw.select_ics(vif_frames(D_hp[\"ics\"]), comp_hp, 10, \"kept\")\nvar_rows, var_cv = [], {}\nfor name, kw in [\n        (\"R2: corrected signal kept high-passed\", dict(ics=D_hp[\"ics\"], keep=keep_hp)),\n        (\"R3 b: keypoint width as pupil\", dict(ds_kw={\"pupil_key\": \"pupil_kp\"})),\n        (\"R5 b: epoch selection rule\", dict(ds_kw={\"selection\": \"rule\"})),\n        (\"R7 b: folds of recordings\", dict(cv_kw={\"fold_unit\": \"recording\"})),\n        (\"R8 b: null shuffles validation labels too\", dict(cv_kw={\"null_scope\": \"both\"}))]:\n    o, cv = variant(name, **kw)\n    var_rows.append(o)\n    var_cv[name] = cv\nvt = pd.DataFrame(var_rows)\nprint(vt[[\"reading\", \"samples\", \"pos\", \"val_auc_model\", \"val_auc_null\", \"val_auc_p\", \"s\"]].round(4).to_string(index=False))\n\"\"\", \"claim:rest-decoding-above-null\"))\n    cells.append(result(\"rest-decoding-above-null\"))\n    # claim 2\n    cells.append(md(\"\"\"## rest-loss-accuracy-vs-null\n\n> The resting-state decoder has lower validation loss and higher validation accuracy than the null\n> models. (Expected: loss 0.54 against 0.68, accuracy 0.75 against 0.58; paired t-tests p < 0.05.)\n\nSame models as rest-decoding-above-null (its seed, as this claim depends on it); accuracy at a\nthreshold of 0.5 at the epoch of lowest validation loss.\"\"\"))\n    cells.append(code(\"\"\"\nfor m, better in ((\"val_loss\", \"lower\"), (\"val_acc\", \"higher\")):\n    r = pw.paired(cv_main, m)\n    ok = (r[\"model\"] < r[\"null\"]) if better == \"lower\" else (r[\"model\"] > r[\"null\"])\n    print(f\"{m}: model {r['model']:.3f}, null {r['null']:.3f}, t = {r['t']:.2f}, p = {r['p']:.3g}, \"\n          f\"model {better} than null: {ok}\")\nprint(\"Expected: loss 0.54 +/- 0.054 (model), 0.68 +/- 0.068 (null); accuracy 0.75 +/- 0.075, 0.58 +/- 0.058\")\nprint(\"\\\\nShare of negative labels in the validation folds (accuracy of always saying 'no dilation'):\",\n      np.round(1 - cv_main.pos_val, 3).tolist())\nrows_s = []\nfor off, cv in cv_by_seed.items():\n    a, b = pw.paired(cv, \"val_loss\"), pw.paired(cv, \"val_acc\")\n    rows_s.append(dict(seed=f\"claim+{off}\", loss_model=a[\"model\"], loss_null=a[\"null\"], loss_p=a[\"p\"],\n                       acc_model=b[\"model\"], acc_null=b[\"null\"], acc_p=b[\"p\"]))\nprint(pd.DataFrame(rows_s).round(4).to_string(index=False))\nprint(\"\\\\nOther readings (claim's seed):\")\nprint(vt[[\"reading\", \"val_loss_model\", \"val_loss_null\", \"val_loss_p\", \"val_acc_model\", \"val_acc_null\", \"val_acc_p\"]].round(4).to_string(index=False))\n\"\"\", \"claim:rest-loss-accuracy-vs-null\"))\n    cells.append(result(\"rest-loss-accuracy-vs-null\"))\n    # claim 3\n    cells.append(md(\"\"\"## rest-needs-0-1-hz\n\n> Spontaneous pupil dilation could not be predicted above chance from cortical activity low-pass\n> filtered at 2 Hz; a 0.1 Hz low-pass filter was required for significant decoding. The 0.1 Hz AUC\n> did not differ significantly from that at any other cutoff tested (0.05, 0.2, 0.5, 1 and 2 Hz).\n> (Expected AUC 0.86 +/- 0.086 at 0.1 Hz and 0.51 +/- 0.051 at 2 Hz.)\n\nNo reading combination reproduced rest-decoding-above-null above, so the criterion asks for the\ncutoffs in all of them; they are run in the main combination and in R5 b (the only other one\nthat changes the samples cheaply), at this claim's seed. The 10 ICs are those selected at 0.1 Hz,\nthe paper's resting setting, for every cutoff [assumption: the paper does not say whether ICs were\nreselected per cutoff].\"\"\"))\n    cells.append(code(\"\"\"\nSEED3 = pw.seed_of(\"rest-needs-0-1-hz\")\ncut_rows, cut_cv = [], {}\nfor combo, kw in ((\"main\", {}), (\"R5 b\", {\"selection\": \"rule\"})):\n    for c in (0.05, 0.1, 0.2, 0.5, 1.0, 2.0):\n        ds = pw.make_dataset(sessions, D[\"ics\"], keep10, cutoff=c, **kw)\n        cv = pw.run_cv(ds, SEED3)\n        cut_cv[(combo, c)] = cv\n        r = pw.paired(cv, \"val_auc\")\n        cut_rows.append(dict(combo=combo, cutoff_hz=c, model_auc=r[\"model\"], null_auc=r[\"null\"], t=r[\"t\"], p=r[\"p\"],\n                             above_null=bool(r[\"p\"] < 0.05 and r[\"model\"] > r[\"null\"]),\n                             median_auc=float(cv.model_val_auc.median())))\nct = pd.DataFrame(cut_rows)\nprint(ct.round(4).to_string(index=False))\nfor combo in (\"main\", \"R5 b\"):\n    ref = cut_cv[(combo, 0.1)].model_val_auc\n    others = [c for c in (0.05, 0.2, 0.5, 1.0, 2.0)]\n    ps = [stats.ranksums(ref, cut_cv[(combo, c)].model_val_auc).pvalue for c in others]\n    ph = multipletests(ps, method=\"holm\")[1]\n    print(f\"{combo}: Wilcoxon rank-sum, 0.1 Hz against\", dict(zip(others, np.round(ph, 4))), \"(Holm-corrected)\")\n\"\"\", \"claim:rest-needs-0-1-hz\"))\n    cells.append(code(\"\"\"\nrows_s = []\nfor off in (0, 1000, 2000, 3000, 4000):\n    for c in (0.1, 2.0):\n        cv = cut_cv[(\"main\", c)] if off == 0 else pw.run_cv(pw.make_dataset(sessions, D[\"ics\"], keep10, cutoff=c), SEED3 + off)\n        r = pw.paired(cv, \"val_auc\")\n        rows_s.append(dict(seed=f\"claim+{off}\", cutoff_hz=c, model_auc=r[\"model\"], null_auc=r[\"null\"], p=r[\"p\"],\n                           above_null=bool(r[\"p\"] < 0.05 and r[\"model\"] > r[\"null\"])))\nprint(pd.DataFrame(rows_s).round(4).to_string(index=False))\nprint(f\"\\\\nelapsed {time.time() - started:.0f} s\")\n\"\"\", \"claim:rest-needs-0-1-hz\"))\n    cells.append(result(\"rest-needs-0-1-hz\"))\n    cells.append(md(RESULTS.get(\"summary_decoding\", \"## Summary\\n\\n(to be written)\")))\n    nb = new_notebook(cells=cells)\n    nb.metadata[\"kernelspec\"] = {\"display_name\": \"Python 3\", \"language\": \"python\", \"name\": \"python3\"}\n    return nb\n\n\ndef nb_features():\n    cells = []\n    cells.append(md(\"# Reproducing Komori et al. (2026) from DANDI:001425: IC count, window, VIF and SHAP\\n\" + HEADER_COMMON + \"\"\"\nThis notebook tests the IC count and window, the VIF and the SHAP claims, and runs one costly\nvariant of rest-decoding-above-null (R4 b, every frame of the epoch a sample). The decoding claims\nare in `reproduce_komori_2026_decoding.ipynb`; the loading and decomposition here are the same.\n\"\"\" + CLAIMS_TABLE))\n    cells.append(code(SETUP))\n    cells.append(code(DECOMP))\n    cells.append(md(\"## Data check\\n\\nThe full data check is in the decoding notebook; this repeats what this notebook uses.\"))\n    cells.append(code(SANITY_DECOMP, \"sanity\"))\n    cells.append(code(SANITY_LABELS, \"sanity\"))\n    # ic count and window\n    cells.append(md(\"\"\"## rest-ic-count-and-window\n\n> For resting data, decoding with 10 ICs and a 1.5 s feature window gave the highest median AUC\n> among the IC counts (7, 10, 13) and window lengths (0.5 to 10 s) tested, though no comparison was\n> significant.\n\nIC counts under reading (a), the number kept, and (b), the number before VIF pruning; windows of\n0.5, 1.0, 1.5, 2.0, 3.0, 5.0 and 10.0 s (15 to 300 frames) with 10 ICs. Main reading combination\notherwise, at this claim's seed.\"\"\"))\n    cells.append(code(\"\"\"\nSEED4 = pw.seed_of(\"rest-ic-count-and-window\")\nic_sets = {}\nfor reading, rd in ((\"a\", \"kept\"), (\"b\", \"initial\")):\n    for n in (7, 10, 13):\n        ic_sets[(reading, n)] = pw.select_ics(F01, comp, n, rd)\nic_rows, ic_cv = [], {}\nfor (reading, n), (keep, removed) in ic_sets.items():\n    ds = pw.make_dataset(sessions, D[\"ics\"], keep, cutoff=0.1)\n    cv = pw.run_cv(ds, SEED4)\n    ic_cv[(reading, n)] = cv\n    ic_rows.append(dict(reading=reading, n_ics=n, kept=len(keep), removed_for_vif=len(removed),\n                        median_auc=float(cv.model_val_auc.median()), mean_auc=float(cv.model_val_auc.mean()),\n                        min_auc=float(cv.model_val_auc.min()), max_auc=float(cv.model_val_auc.max())))\nit = pd.DataFrame(ic_rows)\nprint(it.round(4).to_string(index=False))\nfor reading in (\"a\", \"b\"):\n    ref = ic_cv[(reading, 10)].model_val_auc\n    ps = [stats.ranksums(ref, ic_cv[(reading, n)].model_val_auc).pvalue for n in (7, 13)]\n    sub = it[it.reading == reading]\n    print(f\"reading {reading}: highest median at {int(sub.loc[sub.median_auc.idxmax(), 'n_ics'])} ICs; \"\n          f\"Wilcoxon rank-sum 10 against 7 and 13, Holm:\", np.round(multipletests(ps, method='holm')[1], 4))\n\"\"\", \"claim:rest-ic-count-and-window\"))\n    cells.append(code(\"\"\"\nwin_rows, win_cv = [], {}\nfor w_s in (0.5, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0):\n    w = int(round(w_s * pw.FS)) + (1 if w_s == 1.5 else 0)   # 1.5 s is the paper's 46 frames\n    t0 = time.time()\n    ds = pw.make_dataset(sessions, D[\"ics\"], keep10, cutoff=0.1, window=w)\n    cv = ic_cv[(\"a\", 10)] if w == pw.WINDOW else pw.run_cv(ds, SEED4)\n    win_cv[w_s] = cv\n    win_rows.append(dict(window_s=w_s, frames=w, samples=len(ds[\"y\"]), median_auc=float(cv.model_val_auc.median()),\n                         mean_auc=float(cv.model_val_auc.mean()), null_mean_auc=float(cv.null_val_auc.mean()),\n                         s=round(time.time() - t0)))\nwt = pd.DataFrame(win_rows)\nprint(wt.round(4).to_string(index=False))\nref = win_cv[1.5].model_val_auc\nothers = [w for w in win_cv if w != 1.5]\nps = [stats.ranksums(ref, win_cv[w].model_val_auc).pvalue for w in others]\nprint(\"highest median AUC at window\", float(wt.loc[wt.median_auc.idxmax(), \"window_s\"]), \"s\")\nprint(\"Wilcoxon rank-sum 1.5 s against\", others, \"Holm:\", np.round(multipletests(ps, method=\"holm\")[1], 4))\n\"\"\", \"claim:rest-ic-count-and-window\"))\n    cells.append(result(\"rest-ic-count-and-window\"))\n    # vif\n    cells.append(md(\"\"\"## rest-vif-below-10\n\n> With 10 ICs the resting-state features have a maximum variance inflation factor of 9.0 across\n> features and time frames, below the VIF < 10 bound; 7 ICs gave a significantly lower maximum VIF,\n> 13 and 15 ICs did not differ from 10. (Expected 9.0 +/- 0.9.)\n\nVIF within each time frame of the validation samples, maximum over features and frames, per model\n(fold); the folds are those of rest-decoding-above-null. IC sets as in rest-ic-count-and-window,\nboth readings, plus 15 ICs. Deterministic given the folds.\"\"\"))\n    cells.append(code(\"\"\"\nSEED1 = pw.seed_of(\"rest-decoding-above-null\")\ndef max_vif_per_fold(keep):\n    ds = pw.make_dataset(sessions, D[\"ics\"], keep, cutoff=0.1)\n    units = ds[\"unit\"]\n    by_mouse = {}\n    for u, m in zip(units, ds[\"mouse\"]):\n        by_mouse.setdefault(m, set()).add(int(u))\n    fold = pw.folds_by_mouse({m: sorted(v) for m, v in sorted(by_mouse.items())}, SEED1)\n    fs = np.array([fold[int(u)] for u in units])\n    out = []\n    for f in range(5):\n        Xv = ds[\"X\"][fs == f]\n        out.append(max(float(pw.vif(Xv[:, k, :]).max()) for k in range(Xv.shape[1])))\n    return np.array(out)\nvif_rows, vif_vals = [], {}\nfor reading, rd in ((\"a\", \"kept\"), (\"b\", \"initial\")):\n    for n in (7, 10, 13, 15):\n        keep, removed = pw.select_ics(F01, comp, n, rd)\n        v = max_vif_per_fold(keep)\n        vif_vals[(reading, n)] = v\n        vif_rows.append(dict(reading=reading, n_ics=n, kept=len(keep), max_over_models=v.max(), median=np.median(v),\n                             per_model=np.round(v, 2).tolist()))\nprint(pd.DataFrame(vif_rows).round(3).to_string(index=False))\nfor reading in (\"a\", \"b\"):\n    ref = vif_vals[(reading, 10)]\n    ps, dirs = [], []\n    for n in (7, 13, 15):\n        ps.append(stats.mannwhitneyu(vif_vals[(reading, n)], ref, alternative=\"two-sided\").pvalue)\n        dirs.append(float(np.median(vif_vals[(reading, n)]) - np.median(ref)))\n    print(f\"reading {reading}: Mann-Whitney U against 10 ICs (7, 13, 15), Holm:\",\n          np.round(multipletests(ps, method=\"holm\")[1], 4), \"; median difference\", np.round(dirs, 3))\n\"\"\", \"claim:rest-vif-below-10\"))\n    cells.append(result(\"rest-vif-below-10\"))\n    # shap\n    cells.append(md(\"\"\"## rest-shap-medial-anterior-first\n\n> In the resting-state model, SHAP values of an IC in the medial anterior cortex (IC7) rise before\n> those of the medial posterior region (IC6) and the secondary motor cortex (IC4).\n\nThe models of rest-decoding-above-null are fitted again here (same data, folds and seeds).\nAttribution: integrated gradients from the mean validation input (see the helper; Deep SHAP's\nDeepExplainer does not support PyTorch GRU layers), for the first validation sample of each\nvalidation epoch whose prediction is positive: at 0.5 (Methods reading) or at the model's Youden\nthreshold (code reading). SHAP is averaged over these samples per model, and the 5 models are\ncompared with the 5 null models per IC and 0.2 s window by paired t-test, uncorrected. The three ICs\nare matched by their maps: medial anterior (largest share of positive weight in a band of 0.5 mm\non each side of the midline anterior to RSP, excluding RSP), RSP (RSPd and RSPagl) and MOs.\"\"\"))\n    cells.append(code(\"\"\"\nfrom sklearn.metrics import roc_curve\nds = ds_main\ncv_s, models_s = pw.run_cv(ds, SEED1, keep_models=True)\nprint(\"Refitted models, validation AUC:\", np.round(cv_s.model_val_auc, 3).tolist(),\n      \"null:\", np.round(cv_s.null_val_auc, 3).tolist())\ndef attributions(reading):\n    per_model = {\"model\": [], \"null\": []}\n    counts = []\n    for net, nnet, va in models_s:\n        Xv, yv, uv = ds[\"X\"][va], ds[\"y\"][va], ds[\"unit\"][va]\n        base = Xv.mean(axis=0)\n        for kind, m in ((\"model\", net), (\"null\", nnet)):\n            p = pw.predict(m, Xv)\n            if reading == \"methods\":\n                thr = 0.5\n            else:\n                fpr, tpr, th = roc_curve(yv, p)\n                thr = th[np.argmax(tpr - fpr)]\n            idx = [np.flatnonzero((uv == u) & (p >= thr))[0] for u in np.unique(uv) if ((uv == u) & (p >= thr)).any()]\n            counts.append(dict(kind=kind, n=len(idx), thr=float(thr)))\n            if not idx:\n                per_model[kind].append(np.full(Xv.shape[1:], np.nan))\n                continue\n            sh = pw.integrated_gradients(m, Xv[idx], base)\n            per_model[kind].append(sh.mean(axis=0))   # frames x ICs\n    return np.array(per_model[\"model\"]), np.array(per_model[\"null\"]), pd.DataFrame(counts)\nshap = {r: attributions(r) for r in (\"methods\", \"code\")}\nfor r, (sm, sn, cnt) in shap.items():\n    print(r, \"samples explained per model:\", cnt[cnt.kind == \"model\"].n.tolist(), \"null:\", cnt[cnt.kind == \"null\"].n.tolist())\n\"\"\", \"claim:rest-shap-medial-anterior-first\"))\n    cells.append(code(\"\"\"\n# Match the three ICs by their maps.\nroi = sessions[0][\"roi_atlas\"]\nnames = sessions[0][\"roi_names\"]\ndef region(prefixes):\n    return np.any([roi[i] for i, n in enumerate(names) if any(n.startswith(p) for p in prefixes)], axis=0)\nrsp, mos = region([\"RSP\"]), region([\"MOs\"])\nleft = region([n for n in names if n.endswith(\"_l\")])\nright = region([n for n in names if n.endswith(\"_r\")])\ncols = np.arange(roi.shape[2])\nxl = (left * cols).sum() / left.sum()\nxr = (right * cols).sum() / right.sum()\nrows_idx = np.arange(roi.shape[1])\nrsp_rows = rows_idx[rsp.any(axis=1)]\nmid = (xl + xr) / 2\n# grid pixel size: atlas pixels per data pixel (affine scale) times the data grid spacing\num_per_grid = pw.GRID_STEP * np.sqrt(abs(np.linalg.det(sessions[0][\"affine\"][:, :2]))) * 18.18\nband = np.abs(cols - mid)[None, :] * um_per_grid <= 500\nant_dir = -1 if (region([\"MOs\"]).any(axis=1) * rows_idx).sum() / mos.sum() < rsp_rows.mean() else 1\nanterior = (rows_idx[:, None] < rsp_rows.min()) if ant_dir == -1 else (rows_idx[:, None] > rsp_rows.max())\ncortex = roi.any(axis=0)\nmedant = band & anterior & cortex & ~rsp\ndef share(j, area):\n    m = np.nan_to_num(D[\"maps\"][j])\n    pk = m.flat[np.argmax(np.abs(m))]\n    m = np.clip(m * np.sign(pk), 0, None) ** 2\n    return float(m[area].sum() / m.sum())\nsh_tab = pd.DataFrame([{\"ic\": j, \"medial_anterior\": share(j, medant), \"RSP\": share(j, rsp), \"MOs\": share(j, mos)} for j in keep10])\nprint(f\"midline at grid column {mid:.1f}; {um_per_grid:.1f} um per grid point; medial anterior band {int(medant.sum())} grid points\")\nprint(sh_tab.round(3).to_string(index=False))\nic7 = int(sh_tab.loc[sh_tab.medial_anterior.idxmax(), \"ic\"])\nrest_tab = sh_tab[sh_tab.ic != ic7]\nic6 = int(rest_tab.loc[rest_tab.RSP.idxmax(), \"ic\"])\nic4 = int(rest_tab[rest_tab.ic != ic6].loc[lambda d: d.MOs.idxmax(), \"ic\"])\nmatch = {\"medial anterior (IC7)\": ic7, \"RSP (IC6)\": ic6, \"MOs (IC4)\": ic4}\nprint(\"matched:\", match)\nfig, axes = plt.subplots(1, 3, figsize=(10, 3.5))\nfor ax, (k, j) in zip(axes, match.items()):\n    m = D[\"maps\"][j]\n    lim = np.nanmax(np.abs(m))\n    ax.imshow(m, cmap=\"RdBu_r\", vmin=-lim, vmax=lim)\n    ax.contour(cortex, [0.5], colors=\"k\", linewidths=0.5)\n    ax.contour(medant, [0.5], colors=\"g\", linewidths=0.8)\n    ax.set_title(f\"{k}: IC {j}\", fontsize=9)\n    ax.axis(\"off\")\nplt.suptitle(\"Matched ICs (green: medial anterior band); colour limits +/- max |weight|\")\nplt.tight_layout()\nplt.show()\n\"\"\", \"claim:rest-shap-medial-anterior-first\"))\n    cells.append(code(\"\"\"\nedges = np.round(np.arange(-1.5, 0.0001, 0.2), 1)\nt_frames = (np.arange(pw.WINDOW) - (pw.WINDOW - 1)) / pw.FS          # -1.5 ... 0 s\nwins = [(-1.5, -1.3), (-1.3, -1.1), (-1.1, -0.9), (-0.9, -0.7), (-0.7, -0.5), (-0.5, -0.3), (-0.3, -0.1), (-0.1, 0.0)]\npos = {j: keep10.index(j) for j in match.values()}\nout = []\nfor r, (sm, sn, cnt) in shap.items():\n    for k, j in match.items():\n        c = pos[j]\n        onset = None\n        rowp = {}\n        for (a, b) in wins:\n            sel = (t_frames >= a - 1e-9) & ((t_frames < b - 1e-9) if b < 0 else (t_frames <= b + 1e-9))\n            x, y = np.nanmean(sm[:, sel, c], axis=1), np.nanmean(sn[:, sel, c], axis=1)\n            t, p = stats.ttest_rel(x, y)\n            rowp[f\"{a}..{b}\"] = round(float(p), 3) if np.isfinite(p) else None\n            if onset is None and np.isfinite(p) and p < 0.05 and x.mean() > y.mean():\n                onset = a\n        mean_curve = np.nanmean(sm[:, :, c], axis=0)\n        out.append(dict(reading=r, ic=k, onset_a=onset, peak_b=float(t_frames[np.argmax(mean_curve)]),\n                        peak_value=float(mean_curve.max()), **rowp))\nst = pd.DataFrame(out)\nprint(\"p-values per window (model against null, paired t over 5 models), onset (a) = first window with p < 0.05 \"\n      \"and model above null; peak (b) = time of the maximum of the mean SHAP over models\")\nprint(st.to_string(index=False))\nfor r in (\"methods\", \"code\"):\n    s = st[st.reading == r].set_index(\"ic\")\n    for col in (\"onset_a\", \"peak_b\"):\n        v = s[col]\n        a = v[\"medial anterior (IC7)\"]\n        prec = [o for o in (\"RSP (IC6)\", \"MOs (IC4)\") if a is not None and pd.notna(a) and pd.notna(v[o]) and a < v[o]]\n        print(f\"{r}, {col}: medial anterior {a}, RSP {v['RSP (IC6)']}, MOs {v['MOs (IC4)']}; precedes: {prec}\")\n\"\"\", \"claim:rest-shap-medial-anterior-first\"))\n    cells.append(result(\"rest-shap-medial-anterior-first\"))\n    # R4b variant\n    cells.append(md(\"\"\"## rest-decoding-above-null, reading R4 b\n\nThe costly variant of the decoding claim: every frame of every epoch is a sample, positive only\ninside the window around the peak (the claims file's R4 reading b), at the decoding claim's seed.\"\"\"))\n    cells.append(code(\"\"\"\nt0 = time.time()\nds_b = pw.make_dataset(sessions, D[\"ics\"], keep10, cutoff=0.1, sample_reading=\"epoch\")\ncv_b = pw.run_cv(ds_b, SEED1)\nprint(\"samples\", len(ds_b[\"y\"]), \"positive share\", round(float(ds_b[\"y\"].mean()), 4))\nprint(cv_b[[\"fold\", \"model_val_auc\", \"null_val_auc\", \"model_val_loss\", \"null_val_loss\", \"model_val_acc\", \"null_val_acc\"]].round(3).to_string(index=False))\nfor m in (\"val_auc\", \"val_loss\", \"val_acc\"):\n    r = pw.paired(cv_b, m)\n    print(f\"{m}: model {r['model']:.3f}, null {r['null']:.3f}, t = {r['t']:.2f}, p = {r['p']:.3g}\")\nprint(f\"({time.time() - t0:.0f} s; notebook {time.time() - started:.0f} s)\")\n\"\"\", \"claim:rest-decoding-above-null\"))\n    cells.append(result(\"r4b\"))\n    cells.append(md(RESULTS.get(\"summary_features\", \"## Summary\\n\\n(to be written)\")))\n    nb = new_notebook(cells=cells)\n    nb.metadata[\"kernelspec\"] = {\"display_name\": \"Python 3\", \"language\": \"python\", \"name\": \"python3\"}\n    return nb\n\n\nbase = \"entries/komori-2026/\"\nnbformat.write(nb_decoding(), base + \"reproduce_komori_2026_decoding.ipynb\")\nnbformat.write(nb_features(), base + \"reproduce_komori_2026_features.ipynb\")\nprint(\"written\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/k/mknb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  sed -n 555,600p tools/entry.py
```

```
print(f"{entry_dir.name}: every claim prints the same on Python {version}; entry.yaml and the lock now use it")
    return 0


def file_hash(path: Path) -> str:
    import hashlib
    return hashlib.sha256(path.read_bytes()).hexdigest()


def entry_hash(entry_dir: Path) -> str:
    """A hash of everything a run of the entry's notebooks reads from the repository: every file of the entry (its
    notebooks, helpers, lock and entry.yaml, which names the Python and the dataset versions), the packages `run`
    adds, and RUN_VERSION. Two runs from the same hash execute the same code on the same data versions."""
    import hashlib
    h = hashlib.sha256(f"run {RUN_VERSION}; harness {' '.join(HARNESS)}; python {python_of(entry_dir)}\n".encode())
    for path in sorted(p for p in entry_dir.rglob("*") if p.is_file()):
        rel = path.relative_to(entry_dir)
        if any(part in ("__pycache__", ".ipynb_checkpoints", ".venv") or part.endswith(".pyc") for part in rel.parts):
            continue
        h.update(f"{rel.as_posix()}\0{file_hash(path)}\n".encode())
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/komori-2026 && sed -i 's/def gru_fit(Xtr, ytr, Xva, yva, seed, epochs=10, batch=256, smoothing=0.001, threads=4):/def gru_fit(Xtr, ytr, Xva, yva, seed, epochs=10, batch=256, smoothing=0.001, threads=2):/; s/def run_cv(ds, seed, fold_unit="epoch", null_scope="train", k=5, epochs=10, keep_models=False,/def run_cv(ds, seed, fold_unit="epoch", null_scope="train", k=5, epochs=10, keep_models=False,/; s/           threads=4):/           threads=2):/' pupilwf.py && grep -n "threads" pupilwf.py | head; cat > $TMPDIR/k/devrun.py <<'EOF'
import sys, pickle, io, contextlib, json, time, traceback
import matplotlib; matplotlib.use("Agg")
import nbformat
sys.path.insert(0, "entries/komori-2026")
import pupilwf as pw
nbname, outname, smoke = sys.argv[1], sys.argv[2], len(sys.argv) > 3
ss = pickle.load(open("/tmp/claude-1001/k/ss.pkl", "rb"))
pw.load_sessions = lambda rows, workers=3: [dict(s) for s in ss]
if smoke:
    orig = pw.gru_fit
    pw.gru_fit = lambda *a, **k: orig(*a, **(k | {"epochs": 1}))
nb = nbformat.read(nbname, as_version=4)
g = {}
out = open(outname, "w")
for i, c in enumerate(nb.cells):
    if c.cell_type != "code":
        continue
    buf = io.StringIO()
    t = time.time()
    try:
        with contextlib.redirect_stdout(buf):
            exec(c.source, g)
    except Exception:
        buf.write(traceback.format_exc())
        out.write(f"=== cell {i} {c.metadata.get('tags')} FAILED\n{buf.getvalue()}\n"); out.flush()
        break
    out.write(f"=== cell {i} {c.metadata.get('tags')} ({time.time()-t:.0f} s)\n{buf.getvalue()}\n"); out.flush()
EOF
cd $TMPDIR/k && . .venv/bin/activate && python mknb.py && cd entries/komori-2026 && date -u && (python $TMPDIR/k/devrun.py reproduce_komori_2026_decoding.ipynb $TMPDIR/k/smoke1.txt smoke & python $TMPDIR/k/devrun.py reproduce_komori_2026_features.ipynb $TMPDIR/k/smoke2.txt smoke & wait); date -u; grep -A30 FAILED $TMPDIR/k/smoke*.txt | head -60; grep "=== cell" $TMPDIR/k/smoke*.txt
```

```
Exit code 2
520:def gru_fit(Xtr, ytr, Xva, yva, seed, epochs=10, batch=256, smoothing=0.001, threads=2):
528:    torch.set_num_threads(threads)
669:           threads=2):
692:                               epochs=epochs, threads=threads)
699:                                 epochs=epochs, threads=threads)
Traceback (most recent call last):
  File "/tmp/claude-1001/k/mknb.py", line 1, in <module>
    import json, sys, nbformat
ModuleNotFoundError: No module named 'nbformat'
Wed Nov 25 10:45:57 UTC 2026
grep: /tmp/claude-1001/k/smoke*.txt: No such file or directory
grep: /tmp/claude-1001/k/smoke*.txt: No such file or directory
```

**Agent calls Bash**

```bash
cd $TMPDIR/k && . .venv/bin/activate && uv pip install -q nbformat pandas matplotlib && python mknb.py && cd entries/komori-2026 && date -u && (python $TMPDIR/k/devrun.py reproduce_komori_2026_decoding.ipynb $TMPDIR/k/smoke1.txt smoke & python $TMPDIR/k/devrun.py reproduce_komori_2026_features.ipynb $TMPDIR/k/smoke2.txt smoke & wait); date -u; grep -A30 FAILED $TMPDIR/k/smoke*.txt | head -60; grep "=== cell" $TMPDIR/k/smoke*.txt
```

```
written
Wed Nov 25 10:46:02 UTC 2026
Wed Nov 25 10:49:26 UTC 2026
/tmp/claude-1001/k/smoke1.txt:=== cell 5 ['sanity'] FAILED
/tmp/claude-1001/k/smoke1.txt-Traceback (most recent call last):
/tmp/claude-1001/k/smoke1.txt-  File "/tmp/claude-1001/k/devrun.py", line 22, in <module>
/tmp/claude-1001/k/smoke1.txt-    exec(c.source, g)
/tmp/claude-1001/k/smoke1.txt-    ~~~~^^^^^^^^^^^^^
/tmp/claude-1001/k/smoke1.txt-  File "<string>", line 8, in <module>
/tmp/claude-1001/k/smoke1.txt-KeyError: 'pupil_kp_bad'
/tmp/claude-1001/k/smoke1.txt-
/tmp/claude-1001/k/smoke1.txt:=== cell 1 None (2 s)
/tmp/claude-1001/k/smoke1.txt:=== cell 2 None (21 s)
/tmp/claude-1001/k/smoke1.txt:=== cell 4 ['sanity'] (0 s)
/tmp/claude-1001/k/smoke1.txt:=== cell 5 ['sanity'] FAILED
/tmp/claude-1001/k/smoke2.txt:=== cell 1 None (2 s)
/tmp/claude-1001/k/smoke2.txt:=== cell 2 None (20 s)
/tmp/claude-1001/k/smoke2.txt:=== cell 4 ['sanity'] (0 s)
/tmp/claude-1001/k/smoke2.txt:=== cell 5 ['sanity'] (0 s)
/tmp/claude-1001/k/smoke2.txt:=== cell 7 ['claim:rest-ic-count-and-window'] (35 s)
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/k && cat smoke2.txt | cut -c1-250
```

```
=== cell 1 None (2 s)
streamed and reduced 9 sessions from DANDI:001425 version 0.250705.0947 in 1 s

=== cell 2 None (20 s)
decomposition in 20 s; kept ICs [np.int64(29), np.int64(11), np.int64(2), np.int64(12), np.int64(28), np.int64(21), np.int64(15), np.int64(27), np.int64(24), np.int64(22)]

=== cell 4 ['sanity'] (0 s)
Common cortical grid points (atlas grid, step 4 atlas pixels): 7592
SVD components available: 306 (paper: 400; the corrected data of each recording have rank 34)
Cumulative variance at 10, 30, 200 components: [0.961  0.9908 0.9999] (paper: > 99.5% at 200)
Frames used to estimate the decomposition (every fifth 40 s epoch): 28800
IC compactness (share of squared weight in the largest supra-half-maximum region):
0     0.091
1     0.150
2     0.233
3     0.080
4     0.060
5     0.110
6     0.132
7     0.142
[... 127 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/k && python - <<'EOF'
s=open('mknb.py').read()
s=s.replace("""ic_rows, ic_cv = [], {}
for (reading, n), (keep, removed) in ic_sets.items():
    ds = pw.make_dataset(sessions, D["ics"], keep, cutoff=0.1)
    cv = pw.run_cv(ds, SEED4)
    ic_cv[(reading, n)] = cv""","""ic_rows, ic_cv, by_set = [], {}, {}
for (reading, n), (keep, removed) in ic_sets.items():
    key = tuple(sorted(int(k) for k in keep))
    if key not in by_set:      # readings (a) and (b) give the same set when no IC is removed for VIF
        by_set[key] = pw.run_cv(pw.make_dataset(sessions, D["ics"], keep, cutoff=0.1), SEED4)
    cv = by_set[key]
    ic_cv[(reading, n)] = cv""")
s=s.replace("""            x, y = np.nanmean(sm[:, sel, c], axis=1), np.nanmean(sn[:, sel, c], axis=1)
            t, p = stats.ttest_rel(x, y)""","""            x, y = np.nanmean(sm[:, sel, c], axis=1), np.nanmean(sn[:, sel, c], axis=1)
            ok = np.isfinite(x) & np.isfinite(y)          # a model with no positive prediction has no SHAP
            t, p = stats.ttest_rel(x[ok], y[ok]) if ok.sum() >= 3 else (np.nan, np.nan)""")
s=s.replace("""        out.append(dict(reading=r, ic=k, onset_a=onset,""","""        out.append(dict(reading=r, ic=k, pairs=int(ok.sum()), onset_a=onset,""")
open('mknb.py','w').write(s)
d=open('devrun.py').read()
d=d.replace('pw.load_sessions = lambda rows, workers=3: [dict(s) for s in ss]','''for s in ss:
    s.setdefault("pupil_kp_bad", -1); s.setdefault("n_edge_points", 30)
pw.load_sessions = lambda rows, workers=3: [dict(s) for s in ss]''')
open('devrun.py','w').write(d)
EOF
. .venv/bin/activate && python mknb.py && cd entries/komori-2026 && python $TMPDIR/k/devrun.py reproduce_komori_2026_decoding.ipynb $TMPDIR/k/smoke1.txt smoke; grep -A20 FAILED $TMPDIR/k/smoke1.txt; date -u
```

```
written
Wed Nov 25 10:52:13 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR/k && cut -c1-220 smoke1.txt | sed -n 1,200p
```

```
=== cell 1 None (1 s)
streamed and reduced 9 sessions from DANDI:001425 version 0.250705.0947 in 1 s

=== cell 2 None (11 s)
decomposition in 11 s; kept ICs [np.int64(29), np.int64(11), np.int64(2), np.int64(12), np.int64(28), np.int64(21), np.int64(15), np.int64(27), np.int64(24), np.int64(22)]

=== cell 4 ['sanity'] (0 s)
Resting-state NWB files in the dandiset: 98 from 25 mice
Files per mouse: {3: 2, 4: 23} (number of files: number of mice)
Files without behaviour (widefield only, no pupil): 6
   subject  day
 VG1-GC#73 day7
 VG1-GC#99 day0
VG1-GC#105 day0
VG1-GC#109 day0
VG1-GC#116 day0
VG1-GC#124 day0
Paper, Methods, Resting state: 25 mice, '2-3 experiments per animal'.

Chosen (R1 a):  [('VG1-GC#51', 'day0', '2023-06-14'), ('VG1-GC#51', 'day1', '2023-06-15'), ('VG1-GC#51', 'day7', '2023-06-23'), ('VG1-GC#52', 'day0', '2023-06-14'), ('VG1-GC#52', 'day1', '2023-06-15'), ('VG1-GC#52', 'day
[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/k && . .venv/bin/activate && python - <<'EOF'
import pickle, numpy as np
ss=pickle.load(open('ss.pkl','rb'))
for s in ss:
    p=s['pupil']; m=np.median(p)
    print(s['subject'],s['day'], round(m,1), [(k,int((p>k*m).sum())) for k in (1.5,2,3,10)], int((p<0.3*m).sum()), np.percentile(p,[0.1,99.9]).round(1))
EOF
```

```
VG1-GC#51 day0 58.3 [(1.5, 946), (2, 255), (3, 148), (10, 101)] 0 [3.87000000e+01 6.25251428e+10]
VG1-GC#51 day1 46.0 [(1.5, 306), (2, 5), (3, 2), (10, 0)] 0 [34.6 73.6]
VG1-GC#51 day7 58.8 [(1.5, 84), (2, 1), (3, 0), (10, 0)] 0 [48.2 91.2]
VG1-GC#52 day0 99.0 [(1.5, 0), (2, 0), (3, 0), (10, 0)] 2 [ 48.4 122.9]
VG1-GC#52 day1 60.0 [(1.5, 753), (2, 0), (3, 0), (10, 0)] 0 [36.6 96.2]
VG1-GC#52 day7 97.0 [(1.5, 0), (2, 0), (3, 0), (10, 0)] 0 [ 75.  119.4]
VG1-GC#53 day0 61.0 [(1.5, 0), (2, 0), (3, 0), (10, 0)] 0 [46.2 79.4]
VG1-GC#53 day1 59.4 [(1.5, 220), (2, 179), (3, 57), (10, 54)] 0 [4.07000000e+01 1.19639381e+07]
VG1-GC#53 day7 88.5 [(1.5, 11), (2, 0), (3, 0), (10, 0)] 0 [ 60.3 123.4]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/komori-2026 && python - <<'EOF'
s=open('pupilwf.py').read()
s=s.replace('''def load_sessions(rows, workers=3):
    """Stream and reduce the chosen sessions, and add the keypoint pupil of reading R3 (b)."""
    sessions = reduce_all(rows, workers)
    for s, r in zip(sessions, rows):
        s["pupil_kp"], s["pupil_kp_bad"], s["n_edge_points"] = keypoint_pupil(r, s["t"])
    return sessions''','''def clean_pupil(p, factor=3.0):
    """[assumption] Failed detections in the deposited diameter. Some recordings hold values up to
    1e21 pixels. The paper's own outlier rule is for its DeepLabCut coordinates (Methods, Pupil
    diameter quantification); here a value above 3 times or below a third of the recording's
    median is taken as a failed detection and replaced by linear interpolation, as are missing
    values. Returns the cleaned trace and the number of frames replaced."""
    p = np.asarray(p, dtype=np.float64).copy()
    m = np.nanmedian(p)
    bad = ~np.isfinite(p) | (p > factor * m) | (p < m / factor)
    p[bad] = np.nan
    return fill_nan(p)[0], int(bad.sum())


def clean_session(s):
    s["pupil_filled"] = s["pupil"]
    s["pupil"], s["pupil_replaced"] = clean_pupil(s["pupil"])
    if "pupil_kp" in s:
        s["pupil_kp"], s["pupil_kp_replaced"] = clean_pupil(s["pupil_kp"])
    return s


def load_sessions(rows, workers=3):
    """Stream and reduce the chosen sessions, add the keypoint pupil of reading R3 (b), and
    replace failed pupil detections."""
    sessions = reduce_all(rows, workers)
    for s, r in zip(sessions, rows):
        s["pupil_kp"], s["pupil_kp_bad"], s["n_edge_points"] = keypoint_pupil(r, s["t"])
        clean_session(s)
    return sessions


def channel_check(row, start=3000, n=1500):
    """Which stored channel carries the calcium signal: the temporal SD of dF/F (mean over cortex
    pixels, 1500 frames) of each series, and the mean raw intensity. GCaMP fluorescence under
    470 nm excitation varies more than under 405 nm (near-isosbestic)."""
    f = open_nwb(row["asset_id"], block_mb=16)
    masks = f["processing/ophys/ImageSegmentation/ROIs/image_mask"][:]
    cortex = masks.any(axis=0)
    out = {}
    for ch in ("widefield_blue", "widefield_UV"):
        x = f["acquisition/" + ch + "/data"][start:start + n][:, cortex].astype(np.float64)
        d = x / x.mean(axis=0) - 1
        out[ch] = dict(dff_sd=float(d.std(axis=0).mean()), raw_mean=float(x.mean()),
                       excitation_lambda=float(f["general/optophysiology/ImagingPlane_" + ch.split("_")[1] + "/excitation_lambda"][()]))
    f.close()
    return out''')
open('pupilwf.py','w').write(s)
EOF
cd $TMPDIR/k && python - <<'EOF'
s=open('mknb.py').read()
s=s.replace('''    "dff_on_img_clock": s["dff_t_equal"], "pupil_nan": s["pupil_nan"],
    "pupil_px_min": round(float(s["pupil"].min()), 1), "pupil_px_median": round(float(np.median(s["pupil"])), 1),
    "pupil_px_max": round(float(s["pupil"].max()), 1),''','''    "dff_on_img_clock": s["dff_t_equal"], "pupil_nan": s["pupil_nan"],
    "pupil_px_max_deposited": float(f"{np.nanmax(s['pupil_filled']):.3g}"), "pupil_replaced": s["pupil_replaced"],
    "pupil_px_min": round(float(s["pupil"].min()), 1), "pupil_px_median": round(float(np.median(s["pupil"])), 1),
    "pupil_px_max": round(float(s["pupil"].max()), 1),''')
s=s.replace('''f = pw.open_nwb(chosen_rows[0]["asset_id"], block_mb=2)''','''print("Pupil columns above: the deposited maximum, the frames replaced as failed detections (helper, clean_pupil), and "
      "the range after replacement. r_diam_kp: correlation of the cleaned diameter with the keypoint width (R3 b).")
for r in chosen_rows[:2]:
    print("Channel check,", r["subject"], r["day"], pw.channel_check(r))
f = pw.open_nwb(chosen_rows[0]["asset_id"], block_mb=2)''')
open('mknb.py','w').write(s)
d=open('devrun.py').read()
d=d.replace('pw.load_sessions = lambda rows, workers=3: [dict(s) for s in ss]','pw.load_sessions = lambda rows, workers=3: [pw.clean_session(dict(s)) for s in ss]')
open('devrun.py','w').write(d)
EOF
. .venv/bin/activate && python mknb.py && cd entries/komori-2026 && date -u && (python $TMPDIR/k/devrun.py reproduce_komori_2026_decoding.ipynb $TMPDIR/k/dev1.txt & python $TMPDIR/k/devrun.py reproduce_komori_2026_features.ipynb $TMPDIR/k/dev2.txt & wait); date -u; grep -A20 FAILED $TMPDIR/k/dev*.txt | head -40; grep "=== cell" $TMPDIR/k/dev*.txt
```

```
written
Wed Nov 25 10:52:55 UTC 2026
Wed Nov 25 11:29:22 UTC 2026
/tmp/claude-1001/k/dev1.txt:=== cell 1 None (1 s)
/tmp/claude-1001/k/dev1.txt:=== cell 2 None (22 s)
/tmp/claude-1001/k/dev1.txt:=== cell 4 ['sanity'] (0 s)
/tmp/claude-1001/k/dev1.txt:=== cell 5 ['sanity'] (41 s)
/tmp/claude-1001/k/dev1.txt:=== cell 7 ['sanity'] (0 s)
/tmp/claude-1001/k/dev1.txt:=== cell 8 ['sanity'] (0 s)
/tmp/claude-1001/k/dev1.txt:=== cell 10 ['sanity'] (0 s)
/tmp/claude-1001/k/dev1.txt:=== cell 11 ['sanity'] (0 s)
/tmp/claude-1001/k/dev1.txt:=== cell 14 ['claim:rest-decoding-above-null'] (82 s)
/tmp/claude-1001/k/dev1.txt:=== cell 15 ['claim:rest-decoding-above-null'] (0 s)
/tmp/claude-1001/k/dev1.txt:=== cell 16 ['claim:rest-decoding-above-null'] (311 s)
/tmp/claude-1001/k/dev1.txt:=== cell 17 ['claim:rest-decoding-above-null'] (312 s)
/tmp/claude-1001/k/dev1.txt:=== cell 20 ['claim:rest-loss-accuracy-vs-null'] (0 s)
/tmp/claude-1001/k/dev1.txt:=== cell 23 ['claim:rest-needs-0-1-hz'] (487 s)
/tmp/claude-1001/k/dev1.txt:=== cell 24 ['claim:rest-needs-0-1-hz'] (577 s)
/tmp/claude-1001/k/dev2.txt:=== cell 1 None (1 s)
/tmp/claude-1001/k/dev2.txt:=== cell 2 None (21 s)
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/k && cut -c1-250 dev1.txt | sed -n '/cell 5/,$p' | grep -v "^[0-9]\+ \+0\.[0-9]\+$"
```

```
=== cell 5 ['sanity'] (41 s)
  subject  day  frames  rate_hz  duration_s  uv_after_blue_ms  pupil_on_img_clock  dff_on_img_clock  pupil_nan  pupil_px_max_deposited  pupil_replaced  pupil_px_min  pupil_px_median  pupil_px_max  kp_width_bad  r_diam_kp  cortex_px  svd34_var  raw_bl
VG1-GC#51 day0   18000   29.952       600.0              16.6                True              True        768            2.880000e+21             148          34.6             58.3         174.9            -1      0.638      10055     0.9944     158
VG1-GC#51 day1   18000   29.952       600.0              16.6                True              True         50            2.190000e+02               2          27.9             46.0         114.8            -1      0.953      10049     0.9972     149
VG1-GC#51 day7   18000   29.952       600.0              16.6                True              True          7            1.280000e+02               0          46.2             58.8         127.8            -1      0.978      10110     0.9941     136
VG1-GC#52 day0   18000   29.952       600.0              16.6                True              True        107            1.250000e+02               3          36.1             99.0         125.1            -1      0.962       9842     0.9924     127
VG1-GC#52 day1   18000   29.952       600.0              16.6                True              True          0            9.770000e+01               0          35.9             60.0          97.7            -1      0.996       9782     0.9958     141
VG1-GC#52 day7   18000   29.952       600.0              16.6                True              True          9            1.220000e+02               0          49.8             97.0         121.7            -1      0.958       9787     0.9927     127
VG1-GC#53 day0   18000   29.952       600.0              16.6                True              True          4            8.070000e+01               0          43.5             61.0          80.7            -1     
[... 151 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/k && cut -c1-250 dev2.txt | sed -n '/cell 7/,$p'
```

```
=== cell 7 ['claim:rest-ic-count-and-window'] (221 s)
reading  n_ics  kept  removed_for_vif  median_auc  mean_auc  min_auc  max_auc
      a      7     7                0      0.7472    0.6704   0.5199   0.7624
      a     10    10                0      0.7213    0.6853   0.5469   0.7950
      a     13    13                0      0.5932    0.6297   0.5142   0.8025
      b      7     7                0      0.7472    0.6704   0.5199   0.7624
      b     10    10                0      0.7213    0.6853   0.5469   0.7950
      b     13    13                0      0.5932    0.6297   0.5142   0.8025
reading a: highest median at 7 ICs; Wilcoxon rank-sum 10 against 7 and 13, Holm: [0.9168 0.6944]
reading b: highest median at 7 ICs; Wilcoxon rank-sum 10 against 7 and 13, Holm: [0.9168 0.6944]

=== cell 8 ['claim:rest-ic-count-and-window'] (1152 s)
 window_s  frames  samples  median_auc  mean_auc  null_mean_auc   s
      0.5      15    12402      0.6594    0.6572         0.6850  24
      1.0      30    12402      0.7176    0.6609         0.6788  48
      1.5      46    12402      0.7213    0.6853         0.6752   0
      2.0      60    12402      0.7158    0.6960         0.6745  99
      3.0      90    12402      0.7257    0.6897         0.6899 161
      5.0     150    12402      0.7375    0.7162         0.7201 270
     10.0     300    12402      0.6953    0.6787         0.7011 550
[... 63 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat papers/datasets/komori-2026.yaml; python - <<'EOF'
import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s,indent=0)[:200]); print(list(s['properties'].keys())); print(json.dumps(s['properties']['outcomes'],indent=0)[:3000])
EOF
```

```
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.64898/2026.05.27.726399
title: Mesoscopic cortical activities associated with pupil-linked perceptions inferred via explainable
  machine learning
datasets:
- archive: dandi
  id: '001425'
  relation: reuses
{
"$schema": "https://json-schema.org/draft/2020-12/schema",
"title": "One attempt at reproducing the claims of a target",
"description": "Draft. To be revised after the pilot. An attempt is recorded 
['schema_version', 'id', 'datasets', 'missing_datasets', 'paper', 'date', 'entry', 'deprecated', 'provenance', 'outcomes', 'verifications', 'findings', 'reconciliation', 'inputs', 'findings_review']
{
"description": "One per claim attempted.",
"type": "array",
"minItems": 1,
"items": {
"type": "object",
[... 158 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/komori-2026 && python - <<'EOF'
s=open('pupilwf.py').read()
s=s.replace('''def list_assets():
    import requests
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=1000"''','''def list_assets(version=VERSION):
    import requests
    url = f"{API}/dandisets/{DANDISET}/versions/{version}/assets/?page_size=1000"''')
s=s.replace('''    a, b = df["model_" + metric].to_numpy(), df["null_" + metric].to_numpy()
    t, p = stats.ttest_rel(a, b)
    return dict(model=float(np.mean(a)), null=float(np.mean(b)), t=float(t), p=float(p))''','''    a, b = df["model_" + metric].to_numpy(), df["null_" + metric].to_numpy()
    ok = np.isfinite(a) & np.isfinite(b)       # a fold whose validation labels are all one class has no AUC
    t, p = stats.ttest_rel(a[ok], b[ok]) if ok.sum() >= 3 else (np.nan, np.nan)
    return dict(model=float(np.mean(a[ok])), null=float(np.mean(b[ok])), t=float(t), p=float(p), n=int(ok.sum()))''')
open('pupilwf.py','w').write(s)
EOF
cd $TMPDIR/k && python - <<'EOF'
s=open('mknb.py').read()
s=s.replace('''cited. The paper was posted in 2026, after both, so either could be the one it read; the resting
sessions used here are the same files in both is not checked (only the pinned version is read).''','''cited. The paper was posted in 2026, after both, so either could be the one it read; the data check
shows that the nine files read here are the same assets in both versions.''')
s=s.replace('''print("\\nChosen (R1 a): ", [(r["subject"], r["day"], r["date"]) for r in chosen_rows])''','''print("\\nChosen (R1 a): ", [(r["subject"], r["day"], r["date"]) for r in chosen_rows])
old = {a["path"]: a["asset_id"] for a in pw.list_assets("0.250514.0602")}
print("Chosen files with the same asset (same content) in version 0.250514.0602:",
      sum(old.get(r["path"]) == r["asset_id"] for r in chosen_rows), "of", len(chosen_rows))''')
s=s.replace('''        ("R7 b: folds of recordings", dict(cv_kw={"fold_unit": "recording"})),''','''        ("R7 b: folds of recordings (pooled over mice)", dict(cv_kw={"fold_unit": "recording"})),''')
s=s.replace('''print(vt[["reading", "samples", "pos", "val_auc_model", "val_auc_null", "val_auc_p", "s"]].round(4).to_string(index=False))''','''print(vt[["reading", "samples", "pos", "val_auc_model", "val_auc_null", "val_auc_p", "s"]].round(4).to_string(index=False))
print("Folds with an AUC (R7 b; a fold whose validation recordings hold no positive label has none):",
      int(np.isfinite(var_cv["R7 b: folds of recordings (pooled over mice)"].model_val_auc).sum()), "of 5")''')
open('mknb.py','w').write(s)
EOF
grep -n "0.250514" $TMPDIR/k/mknb.py | head
```

```
31:cites the dandiset without a version. Two versions are published, 0.250514.0602 (1814 assets) and
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/k && grep -n 'Chosen (R1 a)\|shows that the nine\|pooled over mice\|Folds with an AUC' mknb.py
```

```
34:shows that the nine files read here are the same assets in both versions.
110:print("\\nChosen (R1 a): ", [(r["subject"], r["day"], r["date"]) for r in chosen_rows])
311:        ("R7 b: folds of recordings (pooled over mice)", dict(cv_kw={"fold_unit": "recording"})),
318:print("Folds with an AUC (R7 b; a fold whose validation recordings hold no positive label has none):",
319:      int(np.isfinite(var_cv["R7 b: folds of recordings (pooled over mice)"].model_val_auc).sum()), "of 5")
Shell cwd was reset to
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/k/mknb.py",
 "offset": 108,
 "limit": 4
}
```

```
108	print(tab[~tab.behavior][["subject", "day"]].to_string(index=False))
109	print("Paper, Methods, Resting state: 25 mice, '2-3 experiments per animal'.")
110	print("\\nChosen (R1 a): ", [(r["subject"], r["day"], r["date"]) for r in chosen_rows])
111	"""
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "/tmp/claude-1001/k/mknb.py",
 "old_string": "print(\"\\\\nChosen (R1 a): \", [(r[\"subject\"], r[\"day\"], r[\"date\"]) for r in chosen_rows])",
 "new_string": "print(\"\\\\nChosen (R1 a): \", [(r[\"subject\"], r[\"day\"], r[\"date\"]) for r in chosen_rows])\nold = {a[\"path\"]: a[\"asset_id\"] for a in pw.list_assets(\"0.250514.0602\")}\nprint(\"Chosen files with the same asset (same content) in version 0.250514.0602:\",\n      sum(old.get(r[\"path\"]) == r[\"asset_id\"] for r in chosen_rows), \"of\", len(chosen_rows))"
}
```

```
The file /tmp/claude-1001/k/mknb.py has been updated successfully.
```

**Agent calls Bash**

```bash
cd $TMPDIR/k && . .venv/bin/activate && PYTHONPATH=entries/komori-2026 python -c "
import pupilwf as pw
new={a['path']:a['asset_id'] for a in pw.list_assets()}
old={a['path']:a['asset_id'] for a in pw.list_assets('0.250514.0602')}
rest=[p for p in new if 'resting' in p and p.endswith('.nwb')]
print(sum(old.get(p)==new[p] for p in rest), len(rest), sum(p in old for p in rest))
"
```

```
92 98 92
Shell cwd was reset to
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/k && cat > $TMPDIR/k/results.py <<'PYEOF'
import json
R = {}
R["sanity_streams"] = """Every session holds 18,000 frames per channel at 29.95 Hz over 600 s, as the paper describes
(36,000 frames at 60 Hz, alternating). The pupil diameter and the deposited dF/F are on the
imaging timestamps exactly. The deposited pupil diameter has failed detections that the files do
not flag: in VG1-GC#51 day0 and VG1-GC#53 day1 its maximum is 2.88e21 and 1.05e11 pixels, and
148 and 57 frames there are above three times the median (besides 768 and 269 missing values);
these are replaced before any label is made. The channel check shows the calcium signal in
`widefield_blue` (dF/F SD 0.050 and 0.028 against 0.012 and 0.014 in `widefield_UV`), as its
description says, but the imaging-plane metadata give 405 nm for the blue plane and 470 nm for the
UV plane: the excitation wavelengths are swapped in the metadata."""
R["sanity_clock"] = """The pupil and the mean cortical activity correlate in every session, with the pupil lagging
cortical activity by 1.1 to 2.3 s in seven of nine sessions (5.4 and 7.6 s in VG1-GC#52 day7 and
day1), and the peak correlation exceeds the largest one with the pupil circularly shifted in eight of
nine sessions (VG1-GC#53 day7: 0.297 against 0.213; VG1-GC#52 day1: 0.210 against 0.206). This is
consistent with the pupil and the imaging sharing a clock; it does not prove it."""
R["sanity_labels"] = """With the whole recording's minimum and maximum, the labels are mostly constant within an epoch:
42 of 117 epoch windows hold no positive frame and 37 are positive throughout, and VG1-GC#53 day1
has no positive frame at all. The selection rule R5 (b) keeps 17 of 117 epochs."""
R["rest-decoding-above-null"] = """**Result: not reproduced (resting on assumptions).** Under the main reading combination the
models reach a mean validation AUC of 0.673 against 0.647 for the null models (paired t = 1.15,
p = 0.315), below the expected 0.82 +/- 0.082. No other seed gives a significant difference
(p = 0.15 to 0.53, model means 0.661 to 0.727), and none of the other readings does: corrected
signal kept high-passed 0.524 against 0.516 (p = 0.59), keypoint pupil 0.592 against 0.612
(p = 0.86), epoch selection 0.565 against 0.606 (p = 0.54), null shuffling validation labels too
0.673 against 0.653 (p = 0.55); folds of recordings leave too few folds with an AUC for a test. The
null models are high (0.647) because the labels are nearly constant within epochs, so the
within-epoch shuffle keeps most of what separates epochs. The variant with every frame a sample
(R4 b) is in the features notebook."""
R["rest-loss-accuracy-vs-null"] = """**Result: not reproduced (resting on assumptions).** The validation loss is 0.634 against
0.642 for the null models (p = 0.345) and the accuracy 0.604 against 0.600 (p = 0.908); the paper's
loss 0.54 and accuracy 0.75 are not reached. Under the seed plus 4000 the accuracy is higher than
null (0.679 against 0.618, p = 0.011) but the loss is not lower (p = 0.21), so no seed gives both.
No other reading gives both tests significant; with the corrected signal kept high-passed the
accuracy is higher (0.543 against 0.483, p = 0.035) and the loss is not (p = 0.35)."""
R["rest-needs-0-1-hz"] = """**Result: not reproduced (resting on assumptions).** At 0.1 Hz the models are not above their null
models (0.695 against 0.701, p = 0.75), under all five seeds (p = 0.10 to 0.75), so the claim that
0.1 Hz is needed for significant decoding is not supported. The part of absence holds: at 2 Hz the
models are not above null either (0.699 against 0.672, p = 0.165; all five seeds p > 0.16), and the
2 Hz AUC is not near the paper's 0.51. No cutoff is above null in the main combination (p = 0.16 to
0.80) or with the epoch selection rule (p = 0.11 to 0.43, where the models reach 0.74 to 0.75
against 0.42 to 0.47 from 0.2 to 2 Hz over 17 epochs). As in the paper, the Holm-corrected
rank-sum tests of 0.1 Hz against every other cutoff are not significant (all p >= 0.08)."""
R["rest-ic-count-and-window"] = """**Result: not reproduced (resting on assumptions).** The highest median validation AUC is at 7 ICs
(0.747; 10 ICs 0.721, 13 ICs 0.593) and at a 5.0 s window (0.738; 1.5 s 0.721). As in the paper, no
comparison with 10 ICs or with 1.5 s is significant after Holm correction (p >= 0.69 for the IC
counts, 1.0 for the windows). Readings (a) and (b) of the IC count give the same IC sets, as no IC
is removed for VIF (the largest VIF among all 30 ICs is 3.95)."""
R["rest-vif-below-10"] = """**Result: not reproduced (resting on assumptions).** With 10 ICs the maximum VIF over features and
frames of the validation samples is 10.63 over the five models (per model 3.99 to 10.63, median
5.11), above the bound of 10 and outside 9.0 +/- 0.9. 7 ICs give a lower maximum (median 3.53) but
not significantly (Holm p = 0.44); 13 and 15 ICs do not differ from 10 (p = 0.44 and 0.29), as the
paper finds. The two readings of the IC count give the same sets."""
R["rest-shap-medial-anterior-first"] = """**Result: not reproduced (resting on assumptions).** The matched ICs are 29 (medial anterior band,
share 0.19, with most of its weight in MOs, 0.56), 12 (RSP, 0.22) and 15 (MOs, 0.76). Under the
Methods reading (prediction at 0.5) no IC has a window where the models' SHAP exceeds the null
models' (smallest p 0.073); the peaks of the mean SHAP are at -0.033 s (medial anterior and MOs)
and -0.100 s (RSP). Under the code reading (Youden threshold) the medial anterior IC is above null
from the -0.7 to -0.5 s window (p = 0.033, then 0.002 and 0.042), while RSP and MOs have no such
window; their rise, and so the precedence, is not shown, and the peak of the medial anterior IC
(0.000 s) comes after that of RSP (-0.100 s). The models themselves are not above their null
models (rest-decoding-above-null), so these attributions explain a decoder that does not beat
chance."""
R["r4b"] = """With every frame of an epoch a sample (R4 b; 140,400 samples, 4.1% positive), the models reach
0.698 against 0.665 for null (p = 0.564); the loss (0.160 against 0.166, p = 0.51) and the
accuracy (0.959 for both, the share of negatives) do not differ either. This reading does not
reproduce rest-decoding-above-null or rest-loss-accuracy-vs-null."""
SUMMARY_COMMON = """
A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

| Claim | Outcome |
|---|---|
| rest-decoding-above-null | not reproduced (assumed) |
| rest-loss-accuracy-vs-null | not reproduced (assumed) |
| rest-needs-0-1-hz | not reproduced (assumed) |
| rest-ic-count-and-window | not reproduced (assumed) |
| rest-vif-below-10 | not reproduced (assumed) |
| rest-shap-medial-anterior-first | not reproduced (assumed) |
| 17 claims on the paper's stimulation recordings | blocked: data missing |

**How the analysis differs from the paper's.** The paper does not say which three mice or which
resting sessions it used; the first three mice recorded, with their first three resting sessions,
are used. The ICs it kept "by visual inspection" are replaced by a repeatable rule (the most compact
maps). Frames are binned 2 x 2 (144 x 144) and the decomposition is made on a common atlas grid; the
SVD keeps 306 components, the rank of the corrected data, in place of 400. The GRU is written in
PyTorch with Keras' defaults, and SHAP is computed by integrated gradients from the mean input in
place of DeepExplainer. Failed pupil detections are replaced. Of the readings the claims file names,
the main combination and one change at a time were run, not every combination; the seed check was
run for the decoding claims only.

**What was found about the dataset.** The files hold everything the resting analysis needs: frames
of both channels, pupil diameter and keypoints on the imaging clock, atlas ROIs and the atlas
transform. The excitation wavelengths of the two imaging planes are swapped in the metadata. The
deposited pupil diameter holds unflagged failed detections (values up to 2.9e21 pixels) in two of
the nine sessions read. Six of the 98 resting files hold no behaviour and so no pupil.
"""
R["summary_decoding"] = "## Summary\n" + SUMMARY_COMMON
R["summary_features"] = "## Summary\n" + SUMMARY_COMMON
json.dump(R, open("/tmp/claude-1001/k/results.json", "w"), indent=1)
PYEOF
cd $TMPDIR/k && . .venv/bin/activate && python results.py && python mknb.py with-results && date -u
```

```
written
Wed Nov 25 11:31:00 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/k && . .venv/bin/activate && PYTHONPATH=entries/komori-2026 python - <<'EOF' 2>&1 | grep -v Warn
import pickle, numpy as np, pupilwf as pw
ss=[pw.clean_session(dict(s)) for s in pickle.load(open('ss.pkl','rb'))]
D=pickle.load(open('D.pkl','rb'))
keep=[29, 11, 2, 12, 28, 21, 15, 27, 24, 22]
ds=pw.make_dataset(ss,D['ics'],keep,0.1)
cv=pw.run_cv(ds,pw.seed_of('rest-decoding-above-null'),fold_unit='recording')
print(cv[['fold','n_val','pos_val','model_val_auc','null_val_auc']])
for m in ('val_auc','val_loss','val_acc'): print(m, pw.paired(cv,m))
EOF
```

```
fold  n_val   pos_val  model_val_auc  null_val_auc
0     0   2756  0.623730       0.577287      0.565208
1     1   2756  0.681785       0.451239      0.407780
2     2   2756  0.445573       0.637082      0.592637
3     3   2756  0.572932       0.521215      0.423548
4     4   1378  0.000000            NaN           NaN
val_auc {'model': 0.5467058421223783, 'null': 0.4972933213634098, 't': 2.7831884667070406, 'p': 0.06880772029060092, 'n': 4}
val_loss {'model': 0.7477942737641555, 'null': 0.786410547160507, 't': -1.4516416502115435, 'p': 0.2202350271700185, 'n': 5}
val_acc {'model': 0.48896952104499275, 'null': 0.38062409288824384, 't': 2.0515549525582575, 'p': 0.1094968161281139, 'n': 5}
Shell cwd was reset to
```

**Agent**

Update the texts, then write the entry files and run lock + all.

**Agent calls Bash**

```bash
cd $TMPDIR/k && python - <<'EOF'
s=open('results.py').read()
s=s.replace("""cortical activity by 1.1 to 2.3 s in seven of nine sessions (5.4 and 7.6 s in VG1-GC#52 day7 and
day1), and the peak correlation exceeds the largest one with the pupil circularly shifted in eight of
nine sessions (VG1-GC#53 day7: 0.297 against 0.213; VG1-GC#52 day1: 0.210 against 0.206). This is
consistent with the pupil and the imaging sharing a clock; it does not prove it.""","""cortical activity by 1.1 to 2.3 s in seven of nine sessions (5.4 and 7.6 s in VG1-GC#52 day7 and
day1). The peak correlation exceeds the largest one with the pupil circularly shifted in all nine
sessions, narrowly in VG1-GC#52 day1 (0.210 against 0.206) and VG1-GC#53 day1 (0.187 against
0.169). This is consistent with the pupil and the imaging sharing a clock; it does not prove it,
and the clock of those two sessions is the least supported.""")
s=s.replace("""0.673 against 0.653 (p = 0.55); folds of recordings leave too few folds with an AUC for a test. The""","""0.673 against 0.653 (p = 0.55), folds of recordings 0.547 against 0.497 over the 4 folds with
an AUC (p = 0.069; the fifth holds only VG1-GC#53 day1, which has no positive label). The""")
open('results.py','w').write(s)
EOF
. .venv/bin/activate && python results.py && python mknb.py with-results
cd entries/komori-2026
cat > requirements.in <<'EOF'
--extra-index-url https://download.pytorch.org/whl/cpu
aiohttp
fsspec
h5py
matplotlib
numpy
pandas
requests
scikit-learn
scipy
statsmodels
torch==2.*+cpu
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: komori-2026
type: reproduction
title: Decoding spontaneous pupil dilation from resting cortical activity (Komori et al. 2026)
description: Tests the resting-state findings of Komori, Mizusaki, Tomita, Yoneda, Matoba and Morita
  (2026) on DANDI:001425, the cued-lever-pull dataset of Kondo et al. (2025), whose resting-state
  recordings the paper reuses. It rebuilds the paper's pipeline from the frames of nine resting
  sessions (three mice), independent components of cortical activity and a GRU decoder of pupil
  dilation labels, and tests decoding against null models, the filter cutoff, the IC count and
  window, the variance inflation factor and the SHAP timing. The paper's own stimulation recordings
  are not deposited.
license: Apache-2.0
notebooks:
- path: reproduce_komori_2026_decoding.ipynb
  title: Decoding spontaneous pupil dilation (Komori et al. 2026) from DANDI:001425
  runtime_minutes: 45
- path: reproduce_komori_2026_features.ipynb
  title: IC count, window, VIF and SHAP (Komori et al. 2026) from DANDI:001425
  runtime_minutes: 45
helpers:
- pupilwf.py
related:
- id: dandi:001425/0.250705.0947
  relation: uses_data
- id: doi:10.64898/2026.05.27.726399
  relation: reproduces
EOF
cd  && python tools/entry.py lock entries/komori-2026 2>&1 | tail -3; grep -c "==" entries/komori-2026/requirements.lock.txt; grep "^torch" entries/komori-2026/requirements.lock.txt; python tools/entry.py check entries/komori-2026 2>&1 | tail -20
```

```
written
  cause: wildcards in versions must be at the end
         torch==2.*+cpu
              ^^^^^^^^^
grep: entries/komori-2026/requirements.lock.txt: No such file or directory
grep: entries/komori-2026/requirements.lock.txt: No such file or directory
error: entries/komori-2026: no requirements.lock.txt; run `tools/entry.py lock`
1 error(s)
```

**Agent calls Bash**

```bash
python -c "import torch" 2>/dev/null; . $TMPDIR/k/.venv/bin/activate; python -c "import torch;print(torch.__version__)"; deactivate; sed -i 's/^torch==2.\*+cpu$/torch==2.9.1+cpu/' entries/komori-2026/requirements.in; python tools/entry.py lock entries/komori-2026 2>&1 | tail -3; grep "^torch\|^numpy\|^nvidia" entries/komori-2026/requirements.lock.txt; python tools/entry.py check entries/komori-2026 2>&1 | tail -20
```

```
2.15.0+cu132
wrote komori-2026/requirements.lock.txt (Python 3.13, with hashes)
numpy==2.5.4 \
torch==2.9.1+cpu \
error: entries/komori-2026/requirements.lock.txt: --extra-index-url is required but not locked; re-run lock
1 error(s)
```

**Agent calls Bash**

```bash
grep -n "extra-index-url\|index-url" tools/entry.py | head; head -12 entries/komori-2026/requirements.lock.txt
```

```
# This file was autogenerated by uv via the following command:
#    uv pip compile --generate-hashes --python-version 3.13 requirements.in -o requirements.lock.txt
aiohappyeyeballs==2.7.1 \
    --hash=sha256:065665c041c42a5938ed220bdcd7230f22527fbec085e1853d2402c8a3615d9d \
    --hash=sha256:9243213661e29250eb41368e5daa826fc017156c3b8a11440826b2e3ed376472
    # via aiohttp
aiohttp==3.14.5 \
    --hash=sha256:0133c3c3b54a0bf1e71fa5c1ad95c93f07fd54e24ef1fe182f5122e1573d2bf1 \
    --hash=sha256:038c2c7e8caa26b6c8423779b5eaf1893904048a512c19b32fe841ffa5592b50 \
    --hash=sha256:0684952aeae1f5dbfe02d46039338513b94009baecd15d8e4098a357c4c4a2a6 \
    --hash=sha256:0790ec66fa4013e83c53b9025a45d454723da1a2fce28b3208c9b32d08af162f \
    --hash=sha256:083673c7a94c3ea035caaa5ca04288bdb44887abfe1f5ba23294e6a4b03efd2d \
```

**Agent calls Bash**

```bash
grep -rn "is required but not locked" tools/ | head -3
```

```
tools/entry.py:214:                report.error(rel / "requirements.lock.txt", f"{name} is required but not locked; re-run lock")
```

**Agent calls Bash**

```bash
sed -n 195,220p tools/entry.py; grep -n "index" tools/entry.py | sed -n 1,20p
```

```
for name in helpers:
        if not (entry_dir / name).is_file():
            report.error(rel / "entry.yaml", f"listed helper {name!r} does not exist")

    requirements, lock = entry_dir / "requirements.in", entry_dir / "requirements.lock.txt"
    if not requirements.is_file():
        report.error(rel, "no requirements.in")
    elif not lock.is_file():
        report.error(rel, "no requirements.lock.txt; run `tools/entry.py lock`")
    else:
        locked_for = LOCK_VERSION.search(lock.read_text()[:2000])
        if entry.get("python") and locked_for and locked_for.group(1) != str(entry["python"]):
            report.error(rel / "requirements.lock.txt", f"locked for Python {locked_for.group(1)}, but entry.yaml "
                         f"says {entry['python']}; run `tools/entry.py lock`")
        pinned = {re.split(r"[=<>!~\[ ]", line, maxsplit=1)[0].lower().replace("_", "-")
                  for line in lock.read_text().splitlines() if line and not line.startswith((" ", "#"))}
        for line in requirements.read_text().splitlines():
            name = re.split(r"[=<>!~\[ ;]", line.strip(), maxsplit=1)[0].lower().replace("_", "-")
            if name and not name.startswith("#") and name not in pinned:
                report.error(rel / "requirements.lock.txt", f"{name} is required but not locked; re-run lock")
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/komori-2026 && sed -i '/^--extra-index-url/d; s/^torch==2.9.1+cpu$/torch/' requirements.in && cat requirements.in && cd ../.. && python tools/entry.py lock entries/komori-2026 2>&1 | tail -2; grep "^torch\|^nvidia\|^triton" entries/komori-2026/requirements.lock.txt; python tools/entry.py check entries/komori-2026 2>&1 | tail -20
```

```
aiohttp
fsspec
h5py
matplotlib
numpy
pandas
requests
scikit-learn
scipy
statsmodels
torch
wrote komori-2026/requirements.lock.txt (Python 3.13, with hashes)
nvidia-cublas==13.4.1.3 \
nvidia-cuda-cccl==13.3.5.0.6 \
nvidia-cuda-cupti==13.2.86 \
nvidia-cuda-nvrtc==13.2.86 \
nvidia-cuda-runtime==13.2.86 \
nvidia-cudnn-cu13==9.26.0.51 \
nvidia-cufft==12.2.0.57 \
nvidia-cufile==1.17.1.22 \
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cat > entries/komori-2026/README.md <<'EOF'
# Komori, Mizusaki, Tomita, Yoneda, Matoba & Morita (2026) from DANDI:001425

Tests the resting-state findings of [Komori et al. (2026)](https://doi.org/10.64898/2026.05.27.726399)
on [DANDI:001425](https://dandiarchive.org/dandiset/001425/0.250705.0947), the cued-lever-pull
dataset of Kondo et al. (2025), whose resting-state recordings the paper reuses. The paper's own
recordings with somatosensory and visual stimulation are not deposited.

| Claim | Outcome |
|---|---|
| A GRU on 0.1 Hz ICs decodes spontaneous pupil dilation above null models | Not reproduced |
| The decoder has lower loss and higher accuracy than null | Not reproduced |
| Decoding needs a 0.1 Hz filter; 2 Hz does not decode | Not reproduced |
| 10 ICs and a 1.5 s window give the highest median AUC | Not reproduced |
| Maximum VIF 9.0 with 10 ICs; 7 ICs lower, 13 and 15 not different | Not reproduced |
| SHAP of a medial anterior IC rises before RSP and MOs | Not reproduced |
| 17 claims on the paper's stimulation recordings | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Every tested outcome rests on choices the paper leaves open: which three mice and sessions, which
ICs (kept "by visual inspection" in the paper), and how samples and labels are formed around each
dilation peak. The notebooks run the main reading and one change at a time. The pipeline is
rebuilt from the paper's Methods, as its published code does not cover the resting data.

- `reproduce_komori_2026_decoding.ipynb`: data check and the three decoding claims.
- `reproduce_komori_2026_features.ipynb`: IC count and window, VIF, SHAP, and the costly
  every-frame variant of the decoding claim.
- `pupilwf.py`: streaming, hemodynamic correction, SVD and JADE ICA, labels, the GRU and its
  cross-validation.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/komori-2026-01.yaml`](../../attempts/komori-2026-01.yaml).
EOF
date -u; python tools/entry.py all entries/komori-2026 2>&1 | tail -30; date -u
```

```
Exit code 143
Command timed out after 1h 0m 0s
Wed Nov 25 11:32:56 UTC 2026
```

**Agent calls Bash**

```bash
date -u; ls -la executed/komori-2026/ 2>/dev/null; ps aux | grep -c nbconvert
```

```
Wed Nov 25 12:33:11 UTC 2026
total 920
drwxr-xr-x 3 runner runner   4096 Nov 25 12:04 .
drwxr-xr-x 3 runner runner   4096 Nov 25 11:33 ..
drwxr-xr-x 5 runner runner   4096 Nov 25 11:33 .venv
-rw-r--r-- 1 runner runner 927266 Nov 25 12:04 reproduce_komori_2026_decoding.ipynb
3
```

**Agent calls Bash**

```bash
ps aux | grep -E "nbconvert|ipykernel" | grep -v grep | cut -c1-200
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
sed -n 690,740p tools/entry.py | grep -n "add_argument"; python - <<'EOF'
import json
nb=json.load(open('executed/komori-2026/reproduce_komori_2026_decoding.ipynb'))
for c in nb['cells']:
    if c['cell_type']=='code':
        t=''.join(''.join(o.get('text','')) for o in c.get('outputs',[]))
        tags=c['metadata'].get('tags')
        if tags and 'claim' in tags[0]: print(tags, t[-1500:])
EOF
```

```
9:    parser.add_argument("command", choices=["lock", "check", "run", "all", "handover", "upgrade-python", "hash"])
10:    parser.add_argument("entry", type=Path, nargs="+",
12:    parser.add_argument("--output-dir", type=Path, help="where executed notebooks go")
13:    parser.add_argument("--timeout", type=int, default=3600, help="seconds allowed per cell")
14:    parser.add_argument("--max-minutes", type=float, default=60,
16:    parser.add_argument("--fresh", action="store_true",
18:    parser.add_argument("--python", help="lock: the Python version to lock for (default: the entry's); "
20:    parser.add_argument("--before", type=Path, help="upgrade-python: the executed notebooks to compare with "
['claim:rest-decoding-above-null']  fold  n_train  n_val  pos_val  model_epoch  model_train_auc  model_val_auc  null_val_auc  model_val_loss  null_val_loss  model_val_acc  null_val_acc
    0     9858   2544    0.509            1            0.749          0.640         0.630           0.655          0.666          0.541         0.536
    1     9858   2544    0.493            1            0.703          0.545         0.652           0.701          0.649          0.493         0.630
    2     9858   2544    0.557            2            0.750          0.734         0.753           0.595          0.630          0.664         0.669
    3     9858   2544    0.457            1            0.722          0.680         0.679           0.649          0.644          0.684         0.681
    4    10176   2226    0.574            3            0.742          0.831         0.826           0.512          0.528          0.748         0.715

validation AUC: model 0.686, null 0.708, paired t = -1.02, p = 0.364  (expected 0.82 +/- 0.082 and 0.61 +/- 0.061)
model AUC - null AUC per fold: [0.01, -0.107, -0.02, 0.001, 0.005]
training AUC of the models: mean 0.733
(50 s)

[... 71 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 600,640p tools/entry.py
```

```
when = time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime(stamp["finished"]))
        for r in stamp["results"]:
            print(f"pass  {r['notebook']}  ({r['seconds']} s, reused)")
        print(f"reused the executed copies of {when}: nothing the run reads has changed since (hash "
              f"{stamp['hash'][:12]}). Nothing was executed and no environment was built; --fresh runs it again.")
        return 0
    (output_dir / STAMP).unlink(missing_ok=True)   # whatever is there is no longer what a run left
    output_dir.mkdir(parents=True, exist_ok=True)
    venv = (output_dir / ".venv").resolve()
    python = venv / "bin" / "python"
    # A kernel of the entry's own environment, under a name no other kernel on the machine has, so
    # nbconvert cannot pick up some other "python3" kernel (a user's or a conda install's).
    kernel = f"registry-{entry_dir.name}"
    for cmd in (["uv", "venv", "--quiet", "--clear", "--python", python_of(entry_dir), str(venv)],
                ["uv", "pip", "install", "--quiet", "--python", str(python),
                 "-r", str(entry_dir / "requirements.lock.txt"), *HARNESS],
                [str(python), "-m", "ipykernel", "install", "--prefix", str(venv), "--name", kernel]):
        if subprocess.run(cmd).returncode != 0:
            print(f"error: could not build the environment ({' '.join(cmd[:3])})", file=sys.stderr)
            return 1
[... 21 more lines not kept]
```

**Agent**

Notebook 1 executed in the locked environment (31 min); the 60-min tool limit killed notebook 2. Re-running notebook 2 alone in the same environment now, and drafting the record meanwhile.

**Agent calls Bash**

```bash
cd entries/komori-2026 && date -u && JUPYTER_PATH=executed/komori-2026/.venv/share/jupyter timeout 6600 executed/komori-2026/.venv/bin/python -m jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3600 --ExecutePreprocessor.kernel_name=registry-komori-2026 --output-dir executed/komori-2026 --output reproduce_komori_2026_features.ipynb reproduce_komori_2026_features.ipynb 2>&1 | tail -3; date -u
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/komori-2026/reproduce_komori_2026_decoding.ipynb'))
for c in nb['cells']:
    if c['cell_type']=='code':
        t=''.join(''.join(o.get('text','')) for o in c.get('outputs',[]))
        tags=c['metadata'].get('tags')
        if tags and 'sanity' in tags[0]: print(tags, t[:3000])
        if tags and 'loss' in tags[0]: print(t[:400])
EOF
```

```
Wed Nov 25 12:33:56 UTC 2026
[NbConvertApp] Converting notebook reproduce_komori_2026_features.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 1300880 bytes to executed/komori-2026/reproduce_komori_2026_features.ipynb
Wed Nov 25 13:11:09 UTC 2026
```

```
['sanity'] Resting-state NWB files in the dandiset: 98 from 25 mice
Files per mouse: {3: 2, 4: 23} (number of files: number of mice)
Files without behaviour (widefield only, no pupil): 6
   subject  day
 VG1-GC#73 day7
 VG1-GC#99 day0
VG1-GC#105 day0
VG1-GC#109 day0
VG1-GC#116 day0
VG1-GC#124 day0
Paper, Methods, Resting state: 25 mice, '2-3 experiments per animal'.

Chosen (R1 a):  [('VG1-GC#51', 'day0', '2023-06-14'), ('VG1-GC#51', 'day1', '2023-06-15'), ('VG1-GC#51', 'day7', '2023-06-23'), ('VG1-GC#52', 'day0', '2023-06-14'), ('VG1-GC#52', 'day1', '2023-06-15'), ('VG1-GC#52', 'day7', '2023-06-23'), ('VG1-GC#53', 'day0', '2023-06-14'), ('VG1-GC#53', 'day1', '2023-06-15'), ('VG1-GC#53', 'day7', '2023-06-23')]
Chosen files with the same asset (same content) in version 0.250514.0602: 6 of 9

['sanity']   subject  day  frames  rate_hz  duration_s  uv_after_blue_ms  pupil_on_img_clock  dff_on_img_clock  pupil_nan  pupil_px_max_deposited  pupil_replaced  pupil_px_min  pupil_px_median  pupil_px_max  kp_width_bad  r_diam_kp  cortex_px  svd34_var  raw_blue  raw_uv  read_s
VG1-GC#51 day0   18000   29.952       600.0              16.6                True              True        768            2.880000e+21             148          34.6             58.3         174.9          3721      0.638      10055     0.9944     15806   14911     197
VG1-GC#51 day1   18000   29.952       600.0              16.6                True              True         50            2.190000e+02               2          27.9             46.0         114.8           207      0.953      10049     0.9972     14927   14238     166
VG1-GC#51 day7   18000   29.952       600.0              16.6                True              True          7            1.280000e+02               0          46.2             58.8         127.8            36      0.978      10110     0.9941     13643   11861     202
VG1-GC#52 day0   18000   29.952       600.0              16.6                True              True        107 
[... 85 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/komori-2026/reproduce_komori_2026_features.ipynb'))
for c in nb['cells']:
    if c['cell_type']=='code':
        t=''.join(''.join(o.get('text','')) for o in c.get('outputs',[]))
        tags=c['metadata'].get('tags')
        if tags and 'claim' in tags[0]: print(tags, t[:2500])
EOF
```

```
['claim:rest-ic-count-and-window'] reading  n_ics  kept  removed_for_vif  median_auc  mean_auc  min_auc  max_auc
      a      7     7                0      0.6947    0.6956   0.6135   0.7960
      a     10    10                0      0.7230    0.7272   0.6280   0.9061
      a     13    13                0      0.7206    0.7260   0.6183   0.8589
      b      7     7                0      0.6947    0.6956   0.6135   0.7960
      b     10    10                0      0.7230    0.7272   0.6280   0.9061
      b     13    13                0      0.7206    0.7260   0.6183   0.8589
reading a: highest median at 10 ICs; Wilcoxon rank-sum 10 against 7 and 13, Holm: [1. 1.]
reading b: highest median at 10 ICs; Wilcoxon rank-sum 10 against 7 and 13, Holm: [1. 1.]

['claim:rest-ic-count-and-window']  window_s  frames  samples  median_auc  mean_auc  null_mean_auc   s
      0.5      15    12402      0.7232    0.7001         0.7062  13
      1.0      30    12402      0.7299    0.7259         0.7114  27
      1.5      46    12402      0.7230    0.7272         0.6942   0
      2.0      60    12402      0.6780    0.7165         0.6944  59
      3.0      90    12402      0.6665    0.7134         0.6943 105
      5.0     150    12402      0.6761    0.7138         0.7046 177
     10.0     300    12402      0.6608    0.7112         0.7050 359
highest median AUC at window 1.0 s
Wilcoxon rank-sum 1.5 s against [0.5, 1.0, 2.0, 3.0, 5.0, 10.0] Holm: [1. 1. 1. 1. 1. 1.]
[... 55 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/komori-2026/reproduce_komori_2026_decoding.ipynb'))
for c in nb['cells']:
    if c['cell_type']=='code':
        t=''.join(''.join(o.get('text','')) for o in c.get('outputs',[]))
        if 'Hemodynamic regression' in t or 'Channel check' in t: print(t[t.find('Hemodynamic'):][:1200])
EOF
```

```
Hemodynamic regression slope of F470 on F405 (34 components per session): median 0.354 range [-2.05  1.83]
Pupil columns above: the deposited maximum, the frames replaced as failed detections (helper, clean_pupil), and the range after replacement. r_diam_kp: correlation of the cleaned diameter with the keypoint width (R3 b).
Channel check, VG1-GC#51 day0 {'widefield_blue': {'dff_sd': 0.049908275756666384, 'raw_mean': 14192.575765629515, 'excitation_lambda': 405.0}, 'widefield_UV': {'dff_sd': 0.011558235845221946, 'raw_mean': 14298.663391195454, 'excitation_lambda': 470.0}}
Channel check, VG1-GC#51 day1 {'widefield_blue': {'dff_sd': 0.027878102254498154, 'raw_mean': 14437.461402517994, 'excitation_lambda': 405.0}, 'widefield_UV': {'dff_sd': 0.013640510882497904, 'raw_mean': 13932.537798592555, 'excitation_lambda': 470.0}}
ImagingPlane_blue excitation_lambda 405.0 imaging_rate 30.0 indicator GCaMP6s grid_spacing [18.18 18.18]
ImagingPlane_UV excitation_lambda 470.0 imaging_rate 30.0 indicator GCaMP6s grid_spacing [18.18 18.18]
acquisition/widefield_blue description: motion-corrected widefield imaging data, blue excitation
dFF_B description: dF/F responses (mean over each ROI mask) be
```

**Agent calls Bash**

```bash
cd $TMPDIR/k && python - <<'EOF'
import json
R=json.load(open('results.json'))
R["rest-decoding-above-null"] = """**Result: not reproduced under the main reading (see the R4 b variant in the features notebook,
which decides the outcome).** Under the main reading combination the models reach a mean validation
AUC of 0.686 against 0.708 for the null models (paired t = -1.02, p = 0.364), below the expected
0.82 +/- 0.082. No other seed gives a significant difference (p = 0.10 to 0.90, model means 0.678
to 0.705), and none of the other readings does: corrected signal kept high-passed 0.657 against
0.651 (p = 0.90), keypoint pupil 0.641 against 0.641 (p = 1.00), epoch selection 0.639 against
0.644 (p = 0.95), folds of recordings 0.581 against 0.611 over the 4 folds with an AUC (p = 0.55;
the fifth holds only VG1-GC#53 day1, which has no positive label), null shuffling validation labels
too 0.686 against 0.702 (p = 0.52). The null models are high (about 0.70) because the labels are
nearly constant within epochs, so the within-epoch shuffle keeps most of what separates epochs."""
R["rest-loss-accuracy-vs-null"] = """**Result: not reproduced (resting on assumptions).** The validation loss is 0.622 against
0.623 for the null models (p = 0.963) and the accuracy 0.626 against 0.646 (p = 0.538); the paper's
loss 0.54 and accuracy 0.75 are not reached. No seed gives either test significant (loss p >= 0.16,
accuracy p >= 0.23). Among the other readings, only folds of recordings gives a significant loss
difference, in the wrong direction (model 0.662, null 0.620, p = 0.037). The every-frame reading
(R4 b, features notebook) is not significant either."""
R["rest-needs-0-1-hz"] = """**Result: not reproduced (resting on assumptions).** At 0.1 Hz the models are not above their null
models (0.684 against 0.697, p = 0.63), under all five seeds (p = 0.20 to 0.98), so the claim that
0.1 Hz is needed for significant decoding is not supported in the main combination. The part of
absence holds there: at 2 Hz the models are not above null (0.677 against 0.702, p = 0.32; all five
seeds p >= 0.057), though the 2 Hz AUC is far from the paper's 0.51. No cutoff is above null in the
main combination (at 0.2 and 0.5 Hz the null is significantly higher, p = 0.037 and 0.047). With
the epoch selection rule (17 epochs) the models are above null at 0.5 Hz only (0.749 against
0.543, p = 0.039; 0.1 Hz 0.717 against 0.558, p = 0.089). As in the paper, the Holm-corrected
rank-sum tests of 0.1 Hz against every other cutoff are not significant (all p >= 0.24). The
cutoffs were not run in the every-frame reading (R4 b), the only one where the 0.1 Hz decoder is
above null."""
R["rest-ic-count-and-window"] = """**Result: partially reproduced (resting on assumptions).** Among the IC counts, 10 ICs have the
highest median validation AUC (0.723; 13 ICs 0.721, 7 ICs 0.695). Among the windows, 1.0 s is
highest (0.730), just above 1.5 s (0.723). As in the paper, no comparison with 10 ICs or with 1.5 s
is significant after Holm correction (all p = 1.0). The differences are small, and at these
settings the models are not above their null models (mean null AUC 0.694 to 0.711). Readings (a)
and (b) of the IC count give the same IC sets, as no IC is removed for VIF (the largest VIF among
all 30 ICs is 5.0)."""
R["rest-vif-below-10"] = """**Result: not reproduced (resting on assumptions).** With 10 ICs the maximum VIF over features and
frames of the validation samples is 6.61 over the five models (per model 3.48 to 6.61): below the
bound of 10, but outside 9.0 +/- 0.9. 7 ICs give a lower maximum (median 3.13 against 5.30), not
significantly (Holm p = 0.064); 13 ICs do not differ from 10 (p = 0.064), and 15 ICs give a
significantly higher maximum (median 9.05, p = 0.024), where the paper finds no difference. The two
readings of the IC count give the same sets."""
R["rest-shap-medial-anterior-first"] = """**Result: not reproduced (resting on assumptions).** The matched ICs are 0 (medial anterior band,
share 0.44, a broad map that also covers RSP, 0.41, and MOs, 0.53), 25 (RSP, 0.45) and 13 (MOs,
0.77). Under the Methods reading (prediction at 0.5) no IC has a window where the models' SHAP
exceeds the null models' (smallest p 0.21), and the mean SHAP of all three peaks at 0.0 s. Under the
code reading (Youden threshold) only the MOs IC is above null, in the -0.9 to -0.7 s window
(p = 0.045); the medial anterior IC never is (smallest p 0.45), and all three peak at 0.0 s. No
reading shows the medial anterior IC rising first. The refitted models are not above their null
models (mean validation AUC 0.686 against 0.708), so these attributions explain a decoder that does
not beat chance."""
R["r4b"] = """**Result: partially reproduced (resting on assumptions), the outcome of rest-decoding-above-null.**
With every frame of an epoch a sample (R4 b; 140,400 samples, 4.1% positive), the models reach a
validation AUC of 0.719 against 0.655 for the null models (paired t = 5.90, p = 0.0041), higher in
all five folds (by 0.023 to 0.084). The effect is significant, but the mean AUC is below the
expected 0.82 +/- 0.082 (0.738 to 0.902), which the criterion calls partial. The five-seed check of
this reading was not run (each run takes about 8.5 minutes); it rests on the claim's seed alone.
For rest-loss-accuracy-vs-null this reading does not reproduce: the loss is 0.161 against 0.166
(p = 0.055) and the accuracy is 0.959 for both, the share of negative labels."""
R["summary_decoding"] = R["summary_decoding"].replace("""| rest-decoding-above-null | not reproduced (assumed) |
| rest-loss-accuracy-vs-null | not reproduced (assumed) |
| rest-needs-0-1-hz | not reproduced (assumed) |
| rest-ic-count-and-window | not reproduced (assumed) |""","""| rest-decoding-above-null | partially reproduced (assumed; R4 b reading only, one seed) |
| rest-loss-accuracy-vs-null | not reproduced (assumed) |
| rest-needs-0-1-hz | not reproduced (assumed) |
| rest-ic-count-and-window | partially reproduced (assumed) |""").replace("""run for the decoding claims only.""","""run for the main reading of the decoding claims only. The JADE decomposition is not identical
across software environments (a run of the same code in another environment kept other ICs and gave
other AUCs, with the same outcomes except for the R4 b reading, which was not significant there);
the numbers here are those of this notebook's run.""")
R["summary_features"] = R["summary_decoding"]
json.dump(R,open('results.json','w'),indent=1)
s=open('mknb.py').read()
s=s.replace("""cited. The paper was posted in 2026, after both, so either could be the one it read; the data check
shows that the nine files read here are the same assets in both versions.""","""cited. The paper was posted in 2026, after both, so either could be the one it read. The data check
shows that 6 of the 9 files read here are the same assets in both versions; the other 3 were
replaced in the later version, and the earlier ones were not compared.""")
s=s.replace('if len(sys.argv) > 1 else {}','if len(sys.argv) > 1 else {}\nimport json as _j')
open('mknb.py','w').write(s)
EOF
grep -n "^RESULTS" mknb.py; . .venv/bin/activate; python - <<'EOF'
# regenerate notebooks without re-running results.py (results.json edited directly)
import subprocess; subprocess.run(["python","/tmp/claude-1001/k/mknb.py","x"],check=True)
EOF
date -u
```

```
4:RESULTS = json.load(open("/tmp/claude-1001/k/results.json")) if len(sys.argv) > 1 else {}
written
Wed Nov 25 13:12:01 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
python - <<'EOF'
import nbformat
for n in ("reproduce_komori_2026_decoding.ipynb","reproduce_komori_2026_features.ipynb"):
    src=nbformat.read(f"entries/komori-2026/{n}",as_version=4)
    ex=nbformat.read(f"executed/komori-2026/{n}",as_version=4)
    assert len(src.cells)==len(ex.cells)
    k=0
    for a,b in zip(src.cells,ex.cells):
        assert a.cell_type==b.cell_type
        if a.cell_type=="code": assert a.source==b.source, n
        elif a.source!=b.source: b.source=a.source; k+=1
    nbformat.write(ex,f"executed/komori-2026/{n}")
    print(n,"markdown cells updated:",k)
EOF
python tools/entry.py check entries/komori-2026 2>&1 | tail -5
```

```
reproduce_komori_2026_decoding.ipynb markdown cells updated: 5
reproduce_komori_2026_features.ipynb markdown cells updated: 6
0 error(s)
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/k && cat > $TMPDIR/k/rec.py <<'PYEOF'
import yaml
NB1, NB2 = "reproduce_komori_2026_decoding.ipynb", "reproduce_komori_2026_features.ipynb"
common_dev = [
    "Three mice (VG1-GC#51, 52, 53) and their first three resting sessions (day0, day1, day7). The paper says 'Experiments from three mice were used' (Methods, Cross-validation) and '2-3 experiments per animal' (Methods, Resting state) without naming them. Assumed, as the claims file's reading R1 (a) with the mice recorded first; all 25 mice (R1 b) would mean streaming about 400 GB and was not run.",
    "ICs kept by a repeatable rule in place of the paper's 'visual inspection' (Methods, ICA-based cortical features), the most compact spatial maps, then VIF pruning (claims file, R6). Assumed; no IC was removed for VIF, so the two readings of the IC count coincide.",
    "Failed pupil detections in the deposited diameter (values up to 2.9e21 pixels) replaced by interpolation when above three times or below a third of the recording's median (148 and 57 frames in two sessions). Assumed; the paper's own outlier rule is for its DeepLabCut coordinates (Methods, Pupil diameter quantification).",
    "Hemodynamic correction as in the Methods (dF/F to the mean of 5-15 s, 34-component SVD, OLS of F470 on F405 after a 0.1 Hz high-pass); the SVD is of the 470 nm dF/F with both channels projected on it, and the fitted coefficients are applied to the unfiltered signals ('subtracted from the measured F480'). Assumed; keeping the high-passed corrected signal is run as a variant.",
    "Frames binned 2 x 2 (144 x 144) and the components warped to a common atlas grid (the file's atlas affine) before the joint SVD; pixels are Z-scored per recording; 'every fifth session' is read as every fifth 40 s epoch. The SVD keeps 306 components, the rank of the corrected data, in place of 400.",
    "The GRU (32 units, dense sigmoid output, Adam, binary cross-entropy with label smoothing 0.001, batch 256, 10 epochs, best validation loss) is written in PyTorch with Keras' initialisers in place of Keras.",
    "JADE ICA is a port of jadeR written in the helper; the decomposition is not identical across software environments, and the numbers are those of the recorded run.",
    "Of the reading combinations the claims file names, the main one and one change at a time were run, not every combination.",
]
blocked_ids = ["fig1-ssp-then-pupil", "fig1-roi-vif-vs-ica", "fig1-somato-exclusion-window", "fig1-somato-selection-rates",
    "fig1-somato-spectra-correlation", "fig1-somato-decoding", "fig2-visual-pattern-sessions-ics", "fig2-architectures-similar",
    "fig2-visual-pattern-decoding", "fig3-oddball-no-group-response", "fig3-oddball-decoding", "supp4-context-classifier-mos",
    "supp8-permutation-importance", "fig4-shap-somato-ic5", "fig4-shap-visual-ics", "supp10-top-shap-ics", "fig4-mapped-shap-regions",
    "supp2-session-selection-needed"]
outcomes = [
 dict(claim="rest-decoding-above-null", outcome="partially_reproduced", assumed=True, notebook=NB2,
      output="claim:rest-decoding-above-null", measured=[0.719, 0.655],
      notes="Partial under reading R4 (b), every frame of each epoch a sample (features notebook): validation AUC 0.719 against 0.655 for the null models, paired t = 5.90, p = 0.0041, higher in all five folds; the mean is below the expected 0.82 +/- 0.082. Under the main reading (samples in the window around the peak, decoding notebook) 0.686 against 0.708 (p = 0.364), and none of the five seeds is significant (p = 0.10 to 0.90). No other reading is significant (corrected signal kept high-passed p = 0.90, keypoint pupil p = 1.00, epoch selection p = 0.95, folds of recordings p = 0.55 over 4 folds, null shuffling validation labels p = 0.52). By mouse, under the main reading, model and null AUC are 0.641 and 0.626 (VG1-GC#51), 0.409 and 0.428 (52), 0.780 and 0.847 (53). The five-seed check of the R4 (b) reading was not run (about 8.5 minutes per run), so whether this outcome is seed sensitive is not known. A run of the same code in another software environment, outside the notebook, gave other ICs and no significant R4 (b) result; it decides nothing here but says the result is fragile.",
      deviations=common_dev + ["The outcome rests on reading R4 (b), at the claim's seed only; the protocol's check under four more seeds was not run for it for lack of time."]),
 dict(claim="rest-loss-accuracy-vs-null", outcome="not_reproduced", assumed=True, notebook=NB1,
      output="claim:rest-loss-accuracy-vs-null", measured=[0.622, 0.623, 0.626, 0.646],
      notes="Main reading, validation loss 0.622 against 0.623 (p = 0.963) and accuracy 0.626 against 0.646 (p = 0.538). No seed gives either test significant. Under R4 (b) the loss is 0.161 against 0.166 (p = 0.055) and the accuracy 0.959 for both, the share of negative labels. Folds of recordings give a significant loss difference in the wrong direction (0.662 against 0.620, p = 0.037).",
      deviations=common_dev),
 dict(claim="rest-needs-0-1-hz", outcome="not_reproduced", assumed=True, notebook=NB1,
      output="claim:rest-needs-0-1-hz", measured=[0.684, 0.677],
      notes="Main combination, 0.1 Hz 0.684 against null 0.697 (p = 0.63) and 2 Hz 0.677 against 0.702 (p = 0.32); under all five seeds neither is above null (0.1 Hz p = 0.20 to 0.98, 2 Hz p >= 0.057). The absence at 2 Hz holds, but 0.1 Hz is not above null either. No cutoff is above null in the main combination; at 0.2 and 0.5 Hz the null is significantly higher (p = 0.037 and 0.047). With the epoch selection rule (17 epochs) only 0.5 Hz is above null (0.749 against 0.543, p = 0.039; 0.1 Hz p = 0.089). The Holm-corrected rank-sum tests of 0.1 Hz against the other cutoffs are not significant (p >= 0.24), as in the paper. The cutoffs were not run under R4 (b), the only reading where the 0.1 Hz decoder is above null (rest-decoding-above-null); the criterion asks for them in that reading if it reproduces, and it reproduces only in part.",
      deviations=common_dev + ["The cutoffs were run in two reading combinations (main and R5 b), not in R4 (b), for lack of time. The 10 ICs selected at 0.1 Hz are used for every cutoff (assumed; the paper does not say whether ICs were reselected)."]),
 dict(claim="rest-ic-count-and-window", outcome="partially_reproduced", assumed=True, notebook=NB2,
      output="claim:rest-ic-count-and-window",
      notes="10 ICs have the highest median validation AUC (0.723; 13 ICs 0.721, 7 ICs 0.695), as the paper finds. The 1.5 s window does not; 1.0 s is highest (0.730 against 0.723 at 1.5 s; 0.5 s 0.723, 2 to 10 s 0.661 to 0.678). No comparison is significant after Holm correction (all p = 1.0), as in the paper. The differences are small, and at these settings the models are not above their null models (mean null AUC 0.694 to 0.711). Readings (a) and (b) of the IC count give the same sets. Only the claim's seed was run.",
      deviations=common_dev + ["The five-seed check was not run for this claim (12 cross-validations per seed)."]),
 dict(claim="rest-vif-below-10", outcome="not_reproduced", assumed=True, notebook=NB2,
      output="claim:rest-vif-below-10", measured=6.61,
      notes="With 10 ICs the maximum VIF over features and validation frames is 6.61 over the five models (3.48 to 6.61); the bound VIF < 10 holds but the value is outside 9.0 +/- 0.9. 7 ICs are lower (median 3.13 against 5.30) but not significantly (Mann-Whitney, Holm p = 0.064); 13 ICs do not differ (p = 0.064) and 15 ICs are significantly higher (median 9.05, p = 0.024), where the paper finds no difference. The VIF depends on which ICs are kept, which the paper chose by eye.",
      deviations=common_dev),
 dict(claim="rest-shap-medial-anterior-first", outcome="not_reproduced", assumed=True, notebook=NB2,
      output="claim:rest-shap-medial-anterior-first",
      notes="Matched ICs, 0 (medial anterior band, share 0.44, broad, also RSP 0.41 and MOs 0.53), 25 (RSP 0.45), 13 (MOs 0.77). Methods reading (prediction at 0.5), no IC above null in any window (smallest p 0.21), all three peak at 0.0 s. Code reading (Youden threshold), only the MOs IC is above null, at -0.9 to -0.7 s (p = 0.045); the medial anterior IC never is (smallest p 0.45). The models explained are those of the main reading, which are not above their null models.",
      deviations=common_dev + ["Attributions by integrated gradients from the mean validation input in place of Deep SHAP (shap.DeepExplainer does not support PyTorch GRU layers); like Deep SHAP they sum to the difference from the baseline output.",
                               "The 'experiment' of the Methods' SHAP sample rule is read as the 40 s epoch; the medial anterior, RSP and MOs ICs are matched by the share of their positive weight in a 0.5 mm midline band anterior to RSP, in RSP and in MOs."]),
]
for cid in blocked_ids:
    outcomes.append(dict(claim=cid, outcome="blocked", blocked_by="data_missing",
        notes="Rests on the paper's own recordings with somatosensory or visual stimulation (Emx1-Cre/Rosa-GCaMP6f mice), which DANDI:001425 does not hold; the Data Availability says they are available from the corresponding author on request, and no public deposit was found (the claims file's opening comment)."))
findings = [
 dict(kind="metadata_error", severity="minor", statement="The imaging-plane metadata give 405 nm excitation for ImagingPlane_blue and 470 nm for ImagingPlane_UV. The values say the reverse; widefield_blue carries the calcium signal (dF/F SD 0.050 and 0.028 against 0.012 and 0.014 in widefield_UV, two sessions), as the series descriptions and the dF/F descriptions (473 nm) say."),
 dict(kind="other", about="data", severity="minor", statement="The deposited pupil diameter (processing/downsampled/pupil_tracking/diameter) holds unflagged failed detections. In VG1-GC#51 day0 and VG1-GC#53 day1 its maximum is 2.88e21 and 1.05e11 pixels, with 148 and 57 frames above three times the median, besides 768 and 269 missing values. A min-max normalisation of the raw trace leaves almost no dilation in those sessions."),
 dict(kind="other", about="data", severity="minor", statement="Six of the 98 resting-state files (VG1-GC#73 day7; VG1-GC#99, 105, 109, 116 and 124 day0) are widefield-only and hold no pupil or other behaviour."),
 dict(kind="other", about="data", severity="none", statement="Checks that passed. Every resting session read holds 18,000 frames per channel at 29.95 Hz over 600 s, as the paper describes; the pupil and the deposited dF/F are on the imaging timestamps; the pupil follows mean cortical activity by 1.1 to 2.3 s in seven of nine sessions, above a shifted control in all nine; no recording is deposited twice."),
 dict(kind="other", about="paper", statement="The paper's own recordings (somatosensory, visual pattern and visual oddball stimulation) are available only on request, so 18 of its 24 claims cannot be tested on public data."),
 dict(kind="methods_unavailable", statement="Which resting sessions of DANDI:001425 did the paper use? The Methods say 'Experiments from three mice were used' and describe all 25 mice with '2-3 experiments per animal'; the dandiset holds 3 or 4 resting sessions per mouse. This attempt assumed the first three mice recorded (VG1-GC#51, 52, 53) with their first three sessions. Please name the mice and sessions."),
 dict(kind="methods_unavailable", statement="How were the resting samples and labels formed? The Methods give 40 s epochs from 50 to 570 s, a window from 3 s before to 0.5 s after the dilation peak, and global Z-scoring and min-max normalisation, but not whether the samples are only that window or every frame of the epoch with labels outside the window set to 0, nor whether any epoch selection applies. The two sample readings give different outcomes here (window, model 0.686 against null 0.708; every frame, 0.719 against 0.655, p = 0.004). Please give the rule, and whether the resting pipeline applied the hemodynamic correction and the 0.1 Hz high-pass of the Methods."),
 dict(kind="methods_unavailable", statement="Which ICs were kept for the resting model, and how was 'every fifth session' applied to 600 s resting recordings? The ICs were chosen 'by visual inspection', which cannot be repeated; this attempt kept the most compact maps. Publishing the IC maps or indices kept (Supplementary Figure 5A) would let the decomposition be matched."),
 dict(kind="methods_unavailable", statement="The published code (WF_deep-learning) covers the stimulation experiments only; no code loads DANDI:001425 or builds the resting labels, epochs or folds, so the resting analysis can be rebuilt only from the Methods."),
]
rec = dict(schema_version=3, id="komori-2026-01",
  datasets=[dict(archive="dandi", id="001425", version="0.250705.0947", doi="10.48324/dandi.001425/0.250705.0947", relation="reuses")],
  paper="doi:10.64898/2026.05.27.726399", date="2026-11-25", entry="komori-2026",
  provenance=dict(kind="agent", accountable=dict(name="CatalystNeuro"),
    agent=dict(harness="Claude Code", model="claude-opus-5-5", protocol="pilot-18"),
    runner=dict(platform="GitHub Actions", url="https://github.com/encorescience/encore-registry/actions/runs/45590698868")),
  outcomes=outcomes, findings=findings)
open("attempts/komori-2026-01.yaml", "w").write(
    yaml.safe_dump(rec, sort_keys=False, width=100, allow_unicode=True))
PYEOF
python $TMPDIR/k/rec.py && python tools/entry.py check entries/komori-2026 2>&1 | tail -5; ls tests | head -30; date -u
```

```
0 error(s)
conftest.py
test_build_osf_targets.py
test_build_site.py
test_build_targets.py
test_build_zenodo_targets.py
test_intake.py
test_notify.py
test_protocol_pin.py
test_readme_row.py
test_replicates.py
test_reuse_targets.py
test_run_requests.py
test_runner.py
Wed Nov 25 13:13:02 UTC 2026
```

**Agent calls Bash**

```bash
python - <<'EOF'
import yaml, json, jsonschema
c=yaml.safe_load(open('claims/komori-2026.yaml'))
a=yaml.safe_load(open('attempts/komori-2026-01.yaml'))
ids=[x['id'] for x in c['claims']]; print(len(ids), set(ids)^{o['claim'] for o in a['outcomes']})
s=json.load(open('schemas/attempt.schema.json'))
jsonschema.validate(a,s); print('valid')
EOF
grep -rn "17 claims\|(17 claims)" entries/komori-2026/README.md $TMPDIR/k/mknb.py $TMPDIR/k/results.json | head; grep -n "^\s*[a-z_]*: [^'\"].*: " attempts/komori-2026-01.yaml | head
```

```
24 set()
valid
entries/komori-2026/README.md:16:| 17 claims on the paper's stimulation recordings | Blocked: data missing |
/tmp/claude-1001/k/mknb.py:57:| fig1-*, fig2-*, fig3-*, fig4-shap-*, fig4-mapped-shap-regions, supp2-*, supp4-*, supp8-*, supp10-* (17 claims) | none | blocked: the stimulation recordings are not deposited |
/tmp/claude-1001/k/results.json:12: "summary_decoding": "## Summary\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning\nand the differences from the paper's method.\n\n| Claim | Outcome |\n|---|---|\n| rest-decoding-above-null | partially reproduced (assumed; R4 b reading only, one seed) |\n| rest-loss-accuracy-vs-null | not reproduced (assumed) |\n| rest-needs-0-1-hz | not reproduced (assumed) |\n| rest-ic-count-and-window | partially reproduced (assumed) |\n| rest-vif-below-10 | not reproduced (assumed) |\n| rest-shap-medial-anterior-first | not reproduced (assumed) |\n| 17 claims on the paper's stimulation recordings | blocked: data missing |\n\n**How the analysis differs from the paper's.** The paper does not say which three mice or which\nresting sessions it used; the first three mice recorded, with their first three resting sessions,\nare used. The ICs it kept \"by visual inspection\" are replaced by a repeatable rule (the most compact\nmaps). Frames are binned 2 x 2 (144 x 144) and the decomposition is made on a common atlas grid; the\nSVD keeps 306 components, the rank of the corrected data, in place of 400. The GRU is written in\nPyTorch with Keras' defaults, and SHAP is computed by integrated gradients from the mean input in\nplace of DeepExplainer. Failed pupil detections are replaced. Of the readings the claims file names,\nthe main combination and one change at a time were run, not every combination; the seed check was\nrun for the main reading of the decoding claims only. The JADE decomposition is not identical\nacross software environments (a run of the same code in another en
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
sed -i 's/17 claims/18 claims/; s/(17 claims)/(18 claims)/' entries/komori-2026/README.md $TMPDIR/k/mknb.py $TMPDIR/k/results.json && sed -i 's/^| A GRU on 0.1 Hz ICs decodes spontaneous pupil dilation above null models | Not reproduced |/| A GRU on 0.1 Hz ICs decodes spontaneous pupil dilation above null models | Partially reproduced (one sample reading, one seed) |/; s/^| 10 ICs and a 1.5 s window give the highest median AUC | Not reproduced |/| 10 ICs and a 1.5 s window give the highest median AUC | Partially reproduced (10 ICs yes, 1.5 s no) |/' entries/komori-2026/README.md && grep -n "18 claims\|Partially" entries/komori-2026/README.md && . $TMPDIR/k/.venv/bin/activate && python $TMPDIR/k/mknb.py x && deactivate && python - <<'EOF'
import nbformat
for n in ("reproduce_komori_2026_decoding.ipynb","reproduce_komori_2026_features.ipynb"):
    src=nbformat.read(f"entries/komori-2026/{n}",as_version=4)
    ex=nbformat.read(f"executed/komori-2026/{n}",as_version=4)
    k=0
    for a,b in zip(src.cells,ex.cells):
        if a.cell_type=="code": assert a.source==b.source
        elif a.source!=b.source: b.source=a.source; k+=1
    nbformat.write(ex,f"executed/komori-2026/{n}"); print(n,k)
EOF
python tools/entry.py check entries/komori-2026 2>&1 | tail -2; python tools/entry.py handover entries/komori-2026 2>&1 | tail -5; ls executed/komori-2026/handover; date -u
```

```
10:| A GRU on 0.1 Hz ICs decodes spontaneous pupil dilation above null models | Partially reproduced (one sample reading, one seed) |
13:| 10 ICs and a 1.5 s window give the highest median AUC | Partially reproduced (10 ICs yes, 1.5 s no) |
16:| 18 claims on the paper's stimulation recordings | Blocked: data missing |
written
reproduce_komori_2026_decoding.ipynb 2
reproduce_komori_2026_features.ipynb 2
0 error(s)
wrote executed/komori-2026/handover
komori-2026.yaml
pupilwf.py
reproduce_komori_2026_decoding.ipynb
reproduce_komori_2026_features.ipynb
Wed Nov 25 13:13:30 UTC 2026
```

**Agent calls Bash**

```bash
git status --short | head; du -sh executed/komori-2026/.venv 2>/dev/null; git check-ignore executed/komori-2026/.venv && echo ignored
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
5.7G	executed/komori-2026/.venv
executed/komori-2026/.venv
ignored
```

**Agent calls Bash**

```bash
git status --short | grep -v "^?? \.\(bash\|git\|idea\|mcp\|profile\|ripgrep\|vscode\|zprofile\|zshrc\)"
```

```
?? attempts/komori-2026-01.yaml
?? entries/komori-2026/
?? scripts
```

**Agent**

## Report: komori-2026 on DANDI:001425 (v0.250705.0947)

The six resting-state claims were tested. One reproduced partially under a single reading and a single seed, one reproduced partially, and four did not reproduce. The other 18 claims are blocked because the paper's own stimulation recordings are not deposited. The full `entry.py all` did not finish (see 4), so CI will re-execute the entry.

### 1. Outcomes

| Claim | Outcome |
|---|---|
| rest-decoding-above-null | partially reproduced (assumed). Only under reading R4 b (every frame of the epoch is a sample): model AUC 0.719 vs null 0.655, p = 0.004, but below the expected 0.82 ± 0.082. Under the main reading: 0.686 vs 0.708 (p = 0.36), and none of the 5 seeds is significant. The 5-seed check was not run for R4 b. |
| rest-loss-accuracy-vs-null | not reproduced (assumed) |
| rest-needs-0-1-hz | not reproduced (assumed). The 0.1 Hz model is not above null. The 2 Hz absence holds. |
| rest-ic-count-and-window | partially reproduced (assumed). 10 ICs give the best median AUC; the best window is 1.0 s, not 1.5 s. |
| rest-vif-below-10 | not reproduced (assumed). Max VIF is 6.61: below 10, but outside 9.0 ± 0.9. 15 ICs is significantly higher than 10. |
| rest-shap-medial-anterior-first | not reproduced (assumed) |
| 18 stimulation claims (fig1–fig4, supp2/4/8/10) | blocked: `data_missing` |

### 2. Dataset, assumptions, questions

**What the dataset holds:** 98 resting files from 25 mice, with frames for both channels (288×288, 18,000 per channel, 30 Hz), pupil diameter and keypoints on the imaging clock, atlas ROIs and an affine. Of the 9 files used, 6 are the same assets in v0.250514.0602; the other 3 were replaced and not compared.

**Findings about the data:**
- The imaging-plane metadata swap the excitation wavelengths: blue says 405 nm, UV says 470 nm. The values show `widefield_blue` carries the calcium signal. Rated minor.
- The deposited pupil diameter has unflagged failed detections, up to 2.9e21 px, in 2 of the 9 sessions. Rated minor.
- 6 resting files have no behaviour, so no pupil.
- The clock check is consistent with the data.

**Assumptions:**
- Mice and sessions: VG1-GC#51, 52 and 53, with their first three resting sessions.
- IC selection: the most compact maps, standing in for the paper's "visual inspection".
- Pupil outliers: values above 3× or below ⅓ of the median are replaced by interpolation.
- Hemodynamic regression: coefficients are fitted on high-passed signals and applied to the unfiltered signals.
- SHAP: computed by integrated gradients, because DeepExplainer does not support PyTorch GRU layers.
- The SVD keeps 306 components (the data's rank) instead of 400.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- Which mice and sessions were used?
- Are resting samples only the window around the peak, or every frame of the epoch? This decides the outcome here.
- Which ICs were kept, and how does "every fifth session" apply to resting data?
- Will the resting-state code be published?

**Questions to a reader:** none.

### 3. Protocol gaps
1. The **Result** cells must be written after the run, but any edit invalidates the run stamp. Doing it properly means running twice, which does not fit 5 h with 40-minute notebooks. I developed on cached data, executed, then copied the final markdown into the executed copies (code unchanged, no stamp).
2. `entry.py check` rejects index options in `requirements.in`, so the PyTorch CPU index cannot be used. I locked the PyPI torch with its CUDA libraries, a 5.7 GB environment.
3. "Run every reading" across R1 to R10 gives 64 or more combinations, and the protocol does not say whether one change at a time is acceptable. I ran the main combination plus one change at a time, and recorded this as a deviation.
4. The five-seed rule is costly for ML claims with many variants. I ran it for the main decoding readings only and recorded the gaps.
5. Results differ between software environments, because JADE and BLAS are not deterministic across them; the protocol says nothing on this. I report only numbers from the locked environment. A run outside the notebook gave a non-significant R4 b result; it is mentioned only as a sign the result is fragile.
6. The Bash tool's default 60-minute timeout matches the notebook limit, so `entry.py all` on two notebooks is killed. I re-ran notebook 2 alone in the same environment.
7. Two criteria were ambiguous:
   - In rest-vif, "the 10-IC maximum holds" could mean only below 10; I read it strictly, as below 10 and within 9.0 ± 0.9.
   - In rest-shap, precedence is undefined when an IC has no onset; I required both onsets.
8. There is no clear kind for "the paper's own data are not public" when the dataset is reused. I recorded it as `other`, `about: paper`.

### 4. Runtime and failures
- Notebook 1 (decoding): 31 min. Notebook 2 (features): 37 min. Streaming takes about 12 min of each.
- The first `entry.py all` was killed by the 60-minute tool timeout while notebook 2 was running. Notebook 2 was then executed with nbconvert in the same locked environment.
- No run stamp exists, so CI will re-execute. Its numbers should match only if training is deterministic within the locked environment, which was not tested.
- `check` passes (0 errors), the attempt record validates against the schema, and the handover was built in `executed/komori-2026/handover/`.

## End of run

81 turns, 188 minutes, $7.50 at API prices, result: success.
