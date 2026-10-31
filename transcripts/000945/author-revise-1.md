# 000945 · author-revise-1 · run 41247088726

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/000945/verifier-1-report.md; ls entries/000945-ramachandran-2025 entries/000945-ramachandran-2025/*
```

```
Sat Oct 31 22:16:33 UTC 2026
**Verifier report, round 1: Ramachandran et al. 2025 on DANDI:000945 (0.250213.2212)**

The claims file has 22 claims. The notebook treats 3 as blocked and tests 19.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| fig3-cell-type-sorting | blocked (data_missing) | The files hold no waveforms, so the k-means features and the cluster separation the criterion requires cannot be computed (cell 16). Using the deposited labels, 2 of 59 recordings fall within the count tolerances (BH508_4500_200_2 at 28/30/58 and BH527_30_200 at 28/34/62). This is weak evidence, since recording totals run from 31 to 127 units. |
| fig4-rsu-time-locked-both-states | blocked (data_missing) | There is no sham (checked on the archive). The awake half already fails the criterion's "above 100%" condition: the awake 1500 Hz RSU mean is 98.1–98.7% under every reading (cell 18). So the best this claim could reach is partially_reproduced. |
| fig4hi-fsu-delayed-latency | not_reproduced | No reading gives p < 0.001; p runs from 0.018 to 0.85. The anesthetized mean is 0.38–0.52 s against an expected 0.24 ± 0.08 under every reading (cell 20). |
| fig4h-awake-latency-wider | blocked (methods_underspecified) | Awake SD > anesthetized SD under D1 but not under D2 (cell 22), and the claims header blocks a claim when its readings disagree. Every SD is about 0.37–0.41 s, with no contrast like the paper's 0.14 vs 0.08. |
| fig5a-rsu-time-locked-prf-awake | not_reproduced | Part (1) holds. Parts (3) and (4) fail under every reading, and (2) fails in 3 of 4 (cell 24). The 3000 Hz mean is the highest and differs from 1500 and 4500 Hz. Even if the sham parts held, the partial threshold could not be met. |
| fig5c-rsu-time-locked-prf-anesth | not_reproduced | Parts (1) and (7) hold; (2), (3) and (4) fail under W1 and W2 (cell 26). Only two labelled rats are available. |
| rsu-time-locked-anesthesia-factor | not_reproduced | p for the anesthesia effect is 0.011–0.018, b
[... 53 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/^## Author/,/^## Verif/p' docs/protocol.md | head -400; grep -n "^#" docs/protocol.md
```

```
## Author

The workflow puts the paper under `paper/`, as for the reader. Read it to
understand the claims, their data and their figures. The claims file still
decides what is tested: do not change a claim's statement, expected values or
criterion. A method detail the claims file lacks is taken from the paper
(step 6).

**Time.** An author run is stopped five hours after it starts, and whatever
is not recorded by then is lost. The prompt says when the run started and the
time by which to finish. Check the clock (`date -u`) between steps. When that
time comes, stop analysing and finish: record each claim not yet tested as
blocked, `too_large` where the computation is what stopped it, saying how far
it got, then write the attempt record and run the entry's checks. A record
with some claims blocked for time is worth more than a run that is cut off.

### 1. Establish what can be tested

Do this before any analysis.

[... 384 more lines not kept]
```

**Agent calls Bash**

```bash
ls attempts | grep 000945; cat attempts/000945-ramachandran-2025-01.yaml; ls questions | grep 000945; ls claims | grep 000945
```

```
000945-ramachandran-2025-01.yaml
schema_version: 2
id: 000945-ramachandran-2025-01
dataset:
  archive: dandi
  id: "000945"
  version: 0.250213.2212
  doi: 10.48324/dandi.000945/0.250213.2212
paper: doi:10.1088/1741-2552/adbb1f
date: 2026-10-31
entry: 000945-ramachandran-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-13
  runner:
[... 300 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/ | head; ls claims/000945* questions/ 2>/dev/null | head; find . -path ./node_modules -prune -o -name "*000945*" -print | grep -v executed | head -30
```

```
000003
000004
000005
000006
000008
000009
000010
000011
000013
000015
claims/000945:
10.1088-1741-2552-adbb1f.yaml

questions/:
000005.yaml
000006.yaml
000008.yaml
000009.yaml
000010.yaml
000011.yaml
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/000945.yaml
```

```
Exit code 1
cat: claims/000945.yaml: No such file or directory
```

**Agent calls Bash**

```bash
cat claims/000945/10.1088-1741-2552-adbb1f.yaml; ls transcripts/000945
```

```
<persisted-output>
Output too large (33.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/afcdfef1-8f42-454e-94c3-1c3fbad9c6ba/tool-results/biugs39b7.txt

Preview (first 2KB):
# Claims for Ramachandran, Gao, Yttri, Yu & He (2025) on dandiset 000945.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22,
# protocol as stated in docs/protocol.md.
# Source: the version of record (J Neural Eng 22(2) 026022, PMC11920894), full text as served by
# Europe PMC: Abstract, Introduction, Methods, Results, figure legends and Discussion. No PDF was
# supplied. The supplementary materials (headpiece design, surgery, training, hydrophone scanning,
# supplementary figures 2 and 4, supplementary table 1 of ISPTA values) were not supplied. No
# claim rests on them: the analysis methods and the ISPTA of each PRF condition are given in the
# main text (Methods 2.3 to 2.6). The paper links no analysis code (it names "custom code" in
# MATLAB R2019a with FieldTrip), so no code was read.
#
# Data the paper used, as it reports them. Adult male Wistar rats, awake and head-fixed, with a
# chronic 32-channel micro-electrode array in S1; tFUS from a 128-element array (f0 1.5 MHz,
# 114 kPa peak-to-peak in situ at 15 V), ultrasound duration 67 ms, one trial every 2.5 s with
# 10% jitter, 505 trials per parameter set, the first 5 cut (500 used). TDT recordings at 24 kHz,
# bandpass 300 Hz to 5 kHz, units sorted in Offline Sorter. Batch 1 (10 rats): awake PRF series
[... 9 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/afcdfef1-8f42-454e-94c3-1c3fbad9c6ba/tool-results/biugs39b7.txt"
}
```

```
1	# Claims for Ramachandran, Gao, Yttri, Yu & He (2025) on dandiset 000945.
2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22,
3	# protocol as stated in docs/protocol.md.
4	# Source: the version of record (J Neural Eng 22(2) 026022, PMC11920894), full text as served by
5	# Europe PMC: Abstract, Introduction, Methods, Results, figure legends and Discussion. No PDF was
6	# supplied. The supplementary materials (headpiece design, surgery, training, hydrophone scanning,
7	# supplementary figures 2 and 4, supplementary table 1 of ISPTA values) were not supplied. No
8	# claim rests on them: the analysis methods and the ISPTA of each PRF condition are given in the
9	# main text (Methods 2.3 to 2.6). The paper links no analysis code (it names "custom code" in
10	# MATLAB R2019a with FieldTrip), so no code was read.
11	#
12	# Data the paper used, as it reports them. Adult male Wistar rats, awake and head-fixed, with a
13	# chronic 32-channel micro-electrode array in S1; tFUS from a 128-element array (f0 1.5 MHz,
14	# 114 kPa peak-to-peak in situ at 15 V), ultrasound duration 67 ms, one trial every 2.5 s with
15	# 10% jitter, 505 trials per parameter set, the first 5 cut (500 used). TDT recordings at 24 kHz,
16	# bandpass 300 Hz to 5 kHz, units sorted in Offline Sorter. Batch 1 (10 rats): awake PRF series
17	# at 30, 300, 1500, 3000 and 4500 Hz with 200 us tone-burst duration (TBD), at about 7 months;
18	# the same PRF series under isoflurane at 9 months; awake DC series at 1500 Hz with TBD 40, 200
19	# and 400 us (DC 6, 30 and 60%) at 10 months. Batch 2 (5 rats, 7 months): awake and anesthetized
20	# recordings at a low PRF and 1500 Hz with 200 us TBD, and a sham at 1500 Hz aimed off target at
[... 511 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "depends_on\|proposed\|verifications\|agrees" tools/*.py | head -60
```

```
tools/agent_run.py:6:    python tools/agent_run.py proposals ROLE DATASET      # "true" if the attempt has proposed changes
tools/agent_run.py:15:author-revise-3, the third round that settles changes proposed after the second. A repeat attempt
tools/agent_run.py:273:    """The claims of the latest attempt on a dandiset that carry a proposed change of outcome."""
tools/agent_run.py:275:    return [o["claim"] for o in (found[0]["outcomes"] if found else []) if o.get("proposed")]
tools/build_site.py:25:The trust tier of an attempt is derived from its verifications: the latest
tools/build_site.py:26:verification decides, and it counts only if it agrees with every outcome.
tools/build_site.py:118:    "code_mismatch": "Published code disagrees",
tools/build_site.py:136:    verifications = attempt.get("verifications") or []
tools/build_site.py:137:    if not verifications:
tools/build_site.py:139:    latest = verifications[-1]
tools/build_site.py:141:    agreed = {r["claim"] for r in latest.get("results", []) if r.get("agrees")}
tools/build_site.py:209:        verifications = a.get("verifications") or []
tools/build_site.py:210:        disagreed = {r["claim"] for v in verifications for r in v["results"] if not r.get("agrees")}
tools/build_site.py:247:                "proposed": o.get("proposed"),
tools/build_site.py:252:            "verifications": [{
tools/build_site.py:255:                "agreed": sum(1 for r in v["results"] if r.get("agrees")),
tools/build_site.py:259:                                  for r in v["results"] if not r.get("agrees")],
tools/build_site.py:260:            } for v in verifications],
tools/build_site.py:395:            "verifications": [] if tier == "runs" else [{
tools/build_site.py:750:    if o.get("proposed"):
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 200,310p tools/entry.py; ls schemas 2>/dev/null; grep -rn "verifications" schemas/*attempt* | head
```

```
if dandiset not in code and dandiset not in helper_code:
                report.error(rel / name, f"neither the notebook nor a helper names dataset {dandiset}")
            version = versions[dandiset]
            if version and version not in code and version not in helper_code:
                report.error(rel / name, f"neither the notebook nor a helper names version {version} "
                                         f"of dataset {dandiset}, which entry.yaml pins")
        _derivation_checks(report, rel / name, code)
    for name in helpers:
        if (entry_dir / name).is_file():
            _derivation_checks(report, rel / name, (entry_dir / name).read_text())

    # Claims and attempts that go with this entry.
    claims_by_target, labels_used, kinds_by_target = {}, {}, {}
    for path in sorted((ROOT / "claims").glob("*/*.yaml")):
        data = validate(report, path, "claims") or {}
        ids = {c["id"] for c in data.get("claims", [])}
        claims_by_target[(dataset_id(data), data.get("paper"))] = ids
        kinds_by_target[(dataset_id(data), data.get("paper"))] = {
            c["id"]: c.get("data", "dataset") for c in data.get("claims", [])}
        labels_used[(dataset_id(data), data.get("paper"))] = any(
[... 96 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 320,420p schemas/attempt.schema.json; grep -l "verifications:" attempts/*.yaml | head -3
```

```
"deviations": {
                  "minItems": 1
                },
                "outcome": {
                  "not": {
                    "const": "blocked"
                  }
                }
              }
            }
          }
        ]
      }
    },
    "verifications": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
[... 84 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -A12 "^verifications:" attempts/000005-yu-2016-01.yaml | head -30; cd entries/000945-ramachandran-2025; wc -l tfus.py; python -c "
import nbformat
nb=nbformat.read('reproduce_ramachandran_2025.ipynb',4)
for i,c in enumerate(nb.cells):
    print(i,c.cell_type,c.metadata.get('tags'),len(c.source),repr(c.source[:100]))
"
```

```
222:verifications:
223-- date: 2026-10-19
224-  kind: agent
225-  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the
226-    notebook)
227-  reviewed: The handover of the first run, the executed notebook with the conclusions and summary
228-    removed, the helper module and the claims file. The verifier also read the paper's public page,
229-    with the supplementary legends.
230-  results:
231-  - claim: vpm-touch
232-    agrees: true
233-    outcome: reproduced
234-    reason: 20 of 24 VPM units are touch-responsive (0.83, criterion at least 0.5), the same test
284 tfus.py
0 markdown None 2707 '# Reproducing Ramachandran et al. (2025) from dandiset 000945\n\n**Paper.** Ramachandran S, Gao H, Ytt'
1 code None 638 'import time\nimport warnings\n\nimport h5py\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport p'
2 markdown None 88 '## Data check\n\nEach check of the metadata against the values is stated under its output.'
3 code ['sanity'] 1733 'inv = pd.DataFrame([{\n    "path": s["path"], "subject_id": s["subject_id"], "identifier": s["identif'
4 markdown None 630 'There are no waveforms, voltage traces, electrode positions or processing modules: units hold\nonly s'
5 code ['sanity'] 1727 'dup = tfus.find_duplicates(sessions)\nprint("Groups of files with identical trial times:")\nprint(dup['
[... 75 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls executed/ 2>/dev/null | head; ls executed/000945-ramachandran-2025 2>/dev/null
```

```
Exit code 2
```

**Agent calls Bash**

```bash
cd entries/000945-ramachandran-2025; python -c "
import nbformat
nb=nbformat.read('reproduce_ramachandran_2025.ipynb',4)
for i,c in enumerate(nb.cells):
    print('=====',i,c.cell_type,c.metadata.get('tags'))
    print(c.source)
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt
```

```
949 /tmp/claude-1001/nb.txt
```

**Agent calls Read**

```json
{
 "file_path": "entries/000945-ramachandran-2025/tfus.py"
}
```

```
1	"""Loading and response measures for dandiset 000945 (tFUS in awake and anesthetized rat S1).
2	
3	Ramachandran, Gao, Yttri, Yu & He (2025), J Neural Eng 22 026022, doi:10.1088/1741-2552/adbb1f.
4	
5	Each NWB file holds one recording: sorted units (`units/spike_times`, and in 60 of the 75 files a
6	`celltype_label`, "1 = RSU, 2 = FSU") and a trial table whose `start_time` is taken as the
7	ultrasound trigger (time 0; checked in the notebook). The condition is only in the file's
8	`identifier`, as `<rat>_<PRF Hz>_<TBD us>[_2][_anes|_anes2]`. Files are streamed from the archive
9	at the pinned version; nothing is written to disk.
10	
11	Where the parameters come from:
12	
13	- PSTH from -0.5 to 1.5 s around the trigger, divided by the number of trials; baseline the 0.5 s
14	  before onset; response the mean rate in a window as a percent of baseline (Methods 2.4, "PSTHs
15	  were computed from 0.5 s prior to ultrasound stimulation, until 1.5 s afterwards ... Baseline was
16	  computed from the 0.5 s before tFUS onset, and the response to tFUS was characterized as the
17	  normalized spike rate as a percent of baseline within the specified time span").
18	- Bin 35.7 ms (Figure 4 legend, "bin size: 35.7 ms"), taken as 1/28 s so that the 0.5 s baseline
19	  is 14 whole bins with an edge at 0 (claims file header).
20	- Windows: time-locked 0 to 67 ms (Methods 2.4, "the response during the 67 ms ultrasound
[... 265 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "limit": 330
}
```

```
1	===== 0 markdown None
2	# Reproducing Ramachandran et al. (2025) from dandiset 000945
3	
4	**Paper.** Ramachandran S, Gao H, Yttri E, Yu K, He B (2025). Parameter-dependent cell-type
5	specific effects of transcranial focused ultrasound stimulation in an awake head-fixed rodent
6	model. *J Neural Eng* 22(2) 026022.
7	[doi:10.1088/1741-2552/adbb1f](https://doi.org/10.1088/1741-2552/adbb1f). The claims file was
8	written from the version of record as served by Europe PMC (PMC11920894): main text, Methods,
9	figure legends and Discussion; the supplementary materials were not supplied, and no claim rests
10	on them.
11	
12	**Dandiset.** [DANDI:000945](https://dandiarchive.org/dandiset/000945/0.250213.2212), version
13	0.250213.2212. This is the version the paper cites (reference 50,
14	doi:10.48324/dandi.000945/0.250213.2212). The four later published versions (0.250711.1746,
15	0.250829.0425, 0.250829.1250) and the draft hold the same 75 files with the same blobs and
16	sizes, as the archive's asset lists show, so the choice does not change the data analysed.
17	
18	**What the dandiset holds.** Sorted units (spike times; a cell-type label in 60 of 75 files) and
19	the trial table of each recording. There are no waveforms, no raw or filtered voltage, no
20	electrode positions and no sham recordings. The condition of each recording is coded only in the
[... 310 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 330,
 "limit": 620
}
```

```
330	print("R1, one recording: recordings with all three counts in tolerance (FSU 28 +- 2.8, RSU 32 +- 3.2, total 60 +- 6)")
331	print(cnt[ok(cnt)].to_string())
332	print(f"({len(cnt)} labelled recordings; totals range {cnt.total.min()} to {cnt.total.max()}, FSU share "
333	      f"{(cnt.FSU / cnt.total).min():.2f} to {(cnt.FSU / cnt.total).max():.2f})")
334	lu = units[units.celltype.notna()].copy()
335	lu["series"] = np.where(lu.tbd == 200, lu.state + " PRF", lu.state + " DC")
336	cnt2 = lu.groupby(["rat", "series"]).celltype.value_counts().unstack(fill_value=0)
337	cnt2["total"] = cnt2.sum(axis=1)
338	print("\nR2, all of one rat's recordings in one series:")
339	print(cnt2.to_string())
340	print("R2 matches:", cnt2[ok(cnt2)].index.tolist() or "none")
341	print("\nThe clusters' separation on the initial phase and after-hyperpolarization durations cannot be "
342	      "computed: the files hold no waveforms (units columns:", sorted(set(inv.units_cols)), ")")
343	===== 17 markdown None
344	**Result: partially reproduced.** With the dataset's labels (K0), two single recordings give all
345	three counts within tolerance (R1): BH527_30_200 with 28 FSU, 34 RSU and 62 units, and
346	BH508_4500_200_2 with 28 FSU, 30 RSU and 58 units. No rat's series matches (R2; totals 77 to 616).
347	The labels follow the expected rate difference in 46 of 59 recordings (FSU median baseline rate
348	above the RSU median; 8.60 against 5.84 Hz over units). The k-means sorting itself, and the
349	separation of the clusters on the initial phase and after-hyperpolarization durations, cannot be
[... 600 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000945-ramachandran-2025; date -u; time python -c "
from dandi.dandiapi import DandiAPIClient
import h5py, remfile, tfus
from concurrent.futures import ThreadPoolExecutor
with DandiAPIClient() as c:
    ds=c.get_dandiset('000945','0.250213.2212')
    md=ds.get_raw_metadata()
    print(md['description'])
assets=tfus.asset_list()
def f(a):
    with h5py.File(remfile.File(a['url']),'r') as h:
        return a['path'], tfus._str(h['identifier']), tfus._str(h['session_start_time'])
for r in sorted(ThreadPoolExecutor(16).map(f,assets), key=lambda r:(r[1].split('_')[0], r[2])): print(*r)
"
```

```
Exit code 1
Sat Oct 31 22:17:51 UTC 2026
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    from dandi.dandiapi import DandiAPIClient
ModuleNotFoundError: No module named 'dandi'

real	0m0.049s
user	0m0.021s
sys	0m0.007s
```

**Agent calls Bash**

```bash
cd  grep -n "venv\|def cmd_\|uv " tools/entry.py | head -30; ls -a ~ | head -30
```

```
345:    venv = (output_dir / ".venv").resolve()
346:    python = venv / "bin" / "python"
350:    for cmd in (["uv", "venv", "--quiet", "--clear", "--python", PYTHON_VERSION, str(venv)],
353:                [str(python), "-m", "ipykernel", "install", "--prefix", str(venv), "--name", kernel]):
367:            env={**os.environ, "JUPYTER_PATH": str(venv / "share" / "jupyter")})
.
..
.bash_aliases
.bash_login
.bash_logout
.bash_profile
.bashrc
.bunfig.toml
.cargo
.claude
.claude-custom-oauth.json
.claude-local-oauth.json
.claude-staging-oauth.json
.claude.json
.composer
[... 15 more lines not kept]
```

**Agent**

I'll set up the entry's environment the way the tool does, so I can explore on subsets.

**Agent calls Bash**

```bash
cd  sed -n 335,375p tools/entry.py; grep -n PYTHON_VERSION tools/entry.py | head -2
```

```
r = subprocess.run(["uv", "pip", "compile", "--quiet", "--python-version", PYTHON_VERSION,
                        "requirements.in", "-o", "requirements.lock.txt"], cwd=entry_dir)
    if r.returncode == 0:
        print(f"wrote {(entry_dir / 'requirements.lock.txt').relative_to(ROOT)}")
    return r.returncode


def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float) -> int:
    entry = yaml.safe_load((entry_dir / "entry.yaml").read_text())
    output_dir.mkdir(parents=True, exist_ok=True)
    venv = (output_dir / ".venv").resolve()
    python = venv / "bin" / "python"
    # A kernel of the entry's own environment, under a name no other kernel on the machine has, so
    # nbconvert cannot pick up some other "python3" kernel (a user's or a conda install's).
    kernel = f"registry-{entry_dir.name}"
    for cmd in (["uv", "venv", "--quiet", "--clear", "--python", PYTHON_VERSION, str(venv)],
                ["uv", "pip", "install", "--quiet", "--python", str(python),
                 "-r", str(entry_dir / "requirements.lock.txt"), *HARNESS],
                [str(python), "-m", "ipykernel", "install", "--prefix", str(venv), "--name", kernel]):
        if subprocess.run(cmd).returncode != 0:
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd  uv venv --quiet --python 3.13 $TMPDIR/venv && uv pip install --quiet --python $TMPDIR/venv/bin/python -r entries/000945-ramachandran-2025/requirements.lock.txt && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/000945-ramachandran-2025; time $TMPDIR/venv/bin/python -c "
from dandi.dandiapi import DandiAPIClient
import h5py, remfile, tfus
from concurrent.futures import ThreadPoolExecutor
with DandiAPIClient() as c:
    ds=c.get_dandiset('000945','0.250213.2212')
    md=ds.get_raw_metadata()
    print(md['description'])
assets=tfus.asset_list()
def f(a):
    with h5py.File(remfile.File(a['url']),'r') as h:
        return a['path'], tfus._str(h['identifier']), tfus._str(h['session_start_time'])
for r in sorted(ThreadPoolExecutor(16).map(f,assets), key=lambda r:(r[1].split('_')[0], r[2])): print(*r)
"
```

```
In these recordings, we tested different PRFs (pulse repetition frequencies) of ultrasound stimulation using a 128-element random array ultrasound transducer to stimulate the somatosensory cortex of awake head-fixed rats. Chronic electrophysiological recordings were acquired using 32-channel NeuroNexus electrodes (Model: A1x32-Poly3-10mm-50-177-Z32), chronically implanted into the rat brain. Ultrasound stimulation is delivered every 2.5 seconds with a 10% jitter, and each recording has 500 trials. The PRFs tested were 30 Hz, 300 Hz, 1500 Hz, 3000 Hz, and 4500 Hz, each with a 200 microsecond pulse duration and a 67 ms ultrasound duration. Anesthetized files were performed under 2% isoflurane anesthesia for comparison.

File Information
All 10 subjects were male rats, implanted with their chronic electrode at 6 months of age and then recordings taken first at 8-10 months, and then some repeats taken at 12 months. Within each subject's folder are recordings for the different PRFs. Most subjects have 5 recordings within, one for each PRF. Some subjects have duplicate recordings taken a few months after the original ones. A few recordings were not included due to excessive noise in the recordings. Files are named in the format SubjectName_PRF_PulseDuration. Each file contains spike time data with the cell type labels included for each neurons, as well as time series data for the onset of each trial of ultrasound stimulation.
sub-BH498/sub-BH498_ses-20230906T180913_ecephys.nwb BH498_3000_200 2023-09-06T18:09:13.000000-04:00
sub-BH498/sub-BH498_ses-20240305T191833_ecephys.nwb BH498_4500_200_2 2024-03-05T19:18:33.000000-05:00
sub-BH498/sub-BH498_ses-20240305T200606_ecephys.nwb BH498_1500_200_2 2024-03-05T20:06:06.000000-05:00
sub-BH498/sub-BH498_ses-20240305T204552_ecephys.nwb BH498_3000_200_2 2024-03-05T20:45:52.000000-05:00
sub-BH498/sub-BH498_ses-20240306T124227_ecephys.nwb BH498_1500_200 2024-03-06T12:42:27.000000-05:00
sub-BH498/sub-BH498_ses-20240306T175805_ecephys.nw
[... 73 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000945-ramachandran-2025; date -u; time $TMPDIR/venv/bin/python -c "
import tfus, pickle, time
t=time.time()
s=tfus.load_all(tfus.asset_list())
print(time.time()-t)
pickle.dump(s, open('$TMPDIR/sessions.pkl','wb'))
"
```

```
Sat Oct 31 22:19:21 UTC 2026
81.79234743118286

real	1m23.247s
user	0m14.184s
sys	0m1.837s
```

**Agent calls Bash**

```bash
cd entries/000945-ramachandran-2025; cat > $TMPDIR/scratch.py <<'EOF'
import pickle, numpy as np, pandas as pd, tfus, warnings
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
warnings.filterwarnings("ignore")
pd.set_option("display.width", 250); pd.set_option("display.max_columns", 40)
sessions = pickle.load(open(__import__('os').environ['TMPDIR'] + '/sessions.pkl', 'rb'))
def start(s):
    v = s["session_start"]
    if v.startswith("[b'"): v = v[3:-2]
    return v[:19]
dup = tfus.find_duplicates(sessions)
kept_paths = set(dup[dup.kept].path)
kept = [s for s in sessions if s["path"] in kept_paths]
units = tfus.unit_table(kept)
st = {s["identifier"]: start(s) for s in kept}
units["start"] = units.session.map(st)
# earliest recording per rat, state, prf, tbd
first = units.groupby(["rat", "state", "prf", "tbd"]).start.transform("min")
units["later"] = units.start != first
L = units[units.celltype.notna() & (units.base_hz > 0)].copy()
PRFS = [30, 300, 1500, 3000, 4500]
def col(kind, state, w):
    if kind == "tl": return "tl_w1" if w == "W1" else "tl_w2"
    return tfus.delayed_window(state, w)
def select(state, ct, rep, tbd=200, prf=None):
    d = L[(L.state == state) & (L.celltype == ct) & (L.tbd == tbd)]
    if prf is not None: d = d[d.prf == prf]
    if rep == "Rep2": d = d[~d.repeat]
    if rep == "Rep3": d = d[~d.later]
    return d
def prf_test(state, ct, kind, w, rep):
    d = select(state, ct, rep); c = col(kind, state, w)
    return tfus.group_test({p: d[d.prf == p][c].values for p in PRFS})
def anova(ct, kind, w, rep, model):
    d = pd.concat([select(s, ct, rep) for s in ("awake", "anesthetized")])
    d = d.assign(y=[r[col(kind, r.state, w)] for _, r in d.iterrows()])
    form = "y ~ C(state) * C(prf)" if model == "A1" else "y ~ C(state) + C(prf)"
    a = sm.stats.anova_lm(ols(form, d).fit(), typ=2)
    return {"reading": f"{model} {w} {rep}", "n": len(d), "p state": a.loc["C(state)", "PR(>F)"],
            "awake mean": d[d.state == "awake"].y.mean(), "anes mean": d[d.state == "anesthetized"].y.mean()}
EOF
cat > $TMPDIR/s1.py <<'EOF'
exec(open(__import__('os').environ['TMPDIR'] + '/scratch.py').read())
print(units.groupby(["session","rat","state","prf","tbd","repeat","later","start"]).size().reset_index().query("state=='awake' and tbd==200 and rat in ['BH498','BH506','BH508']").to_string())
for ct in ("RSU","FSU"):
    for kind in ("del","tl"):
        print(ct, kind); print(pd.DataFrame([anova(ct, kind, w, rep, m) for m in ("A1","A2") for w in ("W1","W2") for rep in ("Rep1","Rep2","Rep3")]).to_string())
EOF
$TMPDIR/venv/bin/python $TMPDIR/s1.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/s1.py", line 1, in <module>
    exec(open(__import__('os').environ['TMPDIR'] + '/scratch.py').read())
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'tfus'
```

**Agent calls Bash**

```bash
cd entries/000945-ramachandran-2025; PYTHONPATH=. $TMPDIR/venv/bin/python $TMPDIR/s1.py
```

```
session    rat  state   prf  tbd  repeat  later                start    0
0     BH498_1500_200  BH498  awake  1500  200   False   True  2024-03-06T12:42:27   37
1   BH498_1500_200_2  BH498  awake  1500  200    True  False  2024-03-05T20:06:06   64
3     BH498_3000_200  BH498  awake  3000  200   False  False  2023-09-06T18:09:13   72
4   BH498_3000_200_2  BH498  awake  3000  200    True   True  2024-03-05T20:45:52   64
6      BH498_300_200  BH498  awake   300  200   False  False  2024-03-06T18:45:36   48
8       BH498_30_200  BH498  awake    30  200   False  False  2024-03-06T17:58:05   31
10    BH498_4500_200  BH498  awake  4500  200   False   True  2024-03-06T23:13:17   47
11  BH498_4500_200_2  BH498  awake  4500  200    True  False  2024-03-05T19:18:33   64
13    BH506_1500_200  BH506  awake  1500  200   False  False  2023-10-18T18:16:09   71
16    BH506_3000_200  BH506  awake  3000  200   False  False  2023-10-26T17:27:06   71
17  BH506_3000_200_2  BH506  awake  3000  200    True   True  2024-03-08T15:06:12   39
18     BH506_300_200  BH506  awake   300  200   False  False  2023-10-26T22:20:22   66
19      BH506_30_200  BH506  awake    30  200   False  False  2023-10-26T23:11:03   71
20    BH506_4500_200  BH506  awake  4500  200   False  False  2023-10-26T15:51:06   64
21  BH506_4500_200_2  BH506  awake  4500  200    True   True  2024-03-08T20:36:35   53
22    BH508_1500_200  BH508  awake  1500  200   False   True  2023-10-22T18:52:10   64
23  BH508_1500_200_2  BH508  awake  1500  200    True  False  2023-08-18T23:26:09   68
24    BH508_3000_200  BH508  awake  3000  200   False  False  2023-08-27T14:08:43   73
25  BH508_3000_200_2  BH508  awake  3000  200    True   True  2024-03-07T16:10:26   33
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000945-ramachandran-2025; python3 - <<'EOF'
p='tfus.py'; s=open(p).read()
s=s.replace('''def _str(v) -> str:
    v = v[()] if hasattr(v, "shape") else v
    return v.decode() if isinstance(v, bytes) else str(v)''','''def _str(v) -> str:
    v = v[()] if hasattr(v, "shape") else v
    if isinstance(v, np.ndarray):        # the unlabelled anesthetized files store session_start_time as an array
        v = v.ravel()[0]
    return v.decode() if isinstance(v, bytes) else str(v)''')
s=s.replace('''def _str(v)''','''def dandiset_description() -> str:
    """The dandiset's description at the pinned version (it describes the `_2` repeats)."""
    with DandiAPIClient() as client:
        return client.get_dandiset(DANDISET_ID, DANDISET_VERSION).get_raw_metadata()["description"]


def _str(v)''',1)
open(p,'w').write(s)
EOF
grep -n "_str\|def dandiset" tfus.py | head
```

```
96:def dandiset_description() -> str:
102:def _str(v) -> str:
117:        ident = _str(f["identifier"])
120:            "subject_id": _str(f["general/subject/subject_id"]),
121:            "age": _str(f["general/subject/age"]),
122:            "session_description": _str(f["session_description"]),
123:            "session_start": _str(f["session_start_time"]),
124:            "units_colnames": list(map(_str, f["units"].attrs["colnames"])),
125:            "trials_colnames": list(map(_str, f["intervals/trials"].attrs["colnames"])),
```

**Agent calls Bash**

```bash
cd entries/000945-ramachandran-2025; cat > $TMPDIR/edit1.py <<'EOF'
import nbformat
P='reproduce_ramachandran_2025.ipynb'
nb=nbformat.read(P,4)
C=nb.cells
def rep(i, old, new, count=1):
    s=C[i].source
    assert s.count(old)==count, (i, old, s.count(old))
    C[i].source=s.replace(old,new)
# cell 3: start, description, dates table
rep(3, '"start": s["session_start"][:16]', '"start": s["session_start"][:19]')
rep(3, 'print("Every identifier parses', '''print("\\nDandiset description at this version:")
print(tfus.dandiset_description())
print("\\nEvery file, by the rat its identifier names and its session start:")
print(inv.sort_values(["rat", "start"])[["rat", "identifier", "subject_id", "start", "path"]].to_string(index=False))
print("Every identifier parses''')
# cell 5: dates of the shared recording
rep(5, 'kept_paths = set(dup[dup.kept].path)', '''for p in ("sub-BH498/sub-BH498_ses-20240306T175805_ecephys.nwb", "sub-BH508/sub-BH508_ses-20240307T002354_ecephys.nwb"):
    print(f'  {by_path[p]["identifier"]} ({by_path[p]["subject_id"]}): session start {by_path[p]["session_start"][:19]}')
kept_paths = set(dup[dup.kept].path)''')
# cell 7: start, later; repeat pairs with dates; DC dates
rep(7, 'units = tfus.unit_table(kept)\n', '''units = tfus.unit_table(kept)
start = {s["identifier"]: s["session_start"][:19] for s in kept}
units["start"] = units.session.map(start)
# `later`: not the earliest of the rat's recordings of the same state, PRF and TBD (reading Rep3)
units["later"] = units.start != units.groupby(["rat", "state", "prf", "tbd"]).start.transform("min")
''')
C[7].source += '''

rec = units.groupby(["rat", "state", "prf", "tbd", "session"]).agg(
    start=("start", "first"), repeat=("repeat", "first"), later=("later", "first"), units=("unit", "size")).reset_index()
multi = rec.groupby(["rat", "state", "prf", "tbd"]).session.transform("size") > 1
print("\\nConditions recorded more than once in a rat (repeat = `_2` suffix; later = not the rat's earliest recording of the condition):")
print(rec[multi].to_string(index=False))
print("`_2` recordings that are the earlier of their pair:", rec[multi & rec.repeat & ~rec.later].session.tolist())
print("\\nAwake 1500 Hz recordings of the rats with DC recordings (TBD 40 and 400 us = 6% and 60%; 200 us = the PRF series):")
print(rec[(rec.state == "awake") & (rec.prf == 1500) & rec.rat.isin(rec[rec.tbd != 200].rat)].to_string(index=False))'''
# cell 14: Rep3
rep(14, 'READINGS = [(w, r) for w in ("W1", "W2") for r in ("Rep1", "Rep2")]', 'REPS = ("Rep1", "Rep2", "Rep3")\nREADINGS = [(w, r) for w in ("W1", "W2") for r in REPS]')
rep(14, '''    if rep == "Rep2":
        d = d[~d.repeat]
    return d''', '''    if rep == "Rep2":
        d = d[~d.repeat]
    if rep == "Rep3":
        d = d[~d.later]
    return d''')
# cell 16: fig3 counts under Rep2/Rep3 and a base rate
C[16].source = C[16].source.replace('print("\\nThe clusters', '''rep_ses, later_ses = set(units[units.repeat].session), set(units[units.later].session)
for rp, drop in (("Rep2", rep_ses), ("Rep3", later_ses)):
    c = cnt[~cnt.index.get_level_values("session").isin(drop)]
    print(f"R1 under {rp}: {len(c)} recordings, matches:", c[ok(c)].index.get_level_values("session").tolist())
band = (cnt.total - 60).abs() <= 6
fsu_share = cnt.FSU.sum() / cnt.total.sum()
p_match = [stats.binom.pmf(k, n, fsu_share) for n in cnt.total
           for k in range(n + 1) if abs(k - 28) <= 2.8 and abs(n - k - 32) <= 3.2]
print(f"\\nBase rate: {int(band.sum())} of {len(cnt)} recordings have a total within 60 +- 6; of these {int(ok(cnt).sum())} "
      f"also match on FSU and RSU. If each recording's FSU count were binomial with the pooled FSU share "
      f"({fsu_share:.3f}), {sum(p_match):.2f} recordings would be expected to match all three counts.")
print("\\nThe clusters''')
assert 'Base rate' in C[16].source
# cell 21: Rep3 for latency
rep(21, '''    for rep in ("Rep1", "Rep2"):
        d = lat if rep == "Rep1" else lat[~lat.repeat]''', '''    for rep in REPS:
        d = {"Rep1": lat, "Rep2": lat[~lat.repeat], "Rep3": lat[~lat.session.isin(later_ses)]}[rep]''')
# cell 37: anesthetized has no repeats
rep(37, 'if st == "anesthetized" and rep == "Rep2":', 'if st == "anesthetized" and rep != "Rep1":')
for i in (40, 43, 56):
    rep(i, 'for rep in ("Rep1", "Rep2"):', 'for rep in REPS:')
# anova with an optional dropped session
rep(33, '''def anova(ct, kind, w, rep, model):
    d = pd.concat([select(st, ct, rep) for st in ("awake", "anesthetized")])''', '''def anova(ct, kind, w, rep, model, drop=()):
    d = pd.concat([select(st, ct, rep) for st in ("awake", "anesthetized")])
    d = d[~d.session.isin(drop)]''')
C[49].source += '''
print("\\nVariant without BH498_30_200, the recording also filed as BH508_30_200_2 (if it is BH508's, it is a later repeat):")
var = pd.DataFrame([{"type": ct, **anova(ct, "del", w, rp, m, drop=("BH498_30_200",))}
                    for ct in ("RSU", "FSU") for m in ("A1", "A2") for w, rp in READINGS])
print(var.to_string(index=False, float_format=lambda v: f"{v:.4g}"))'''
# DC readings: C0 (no 30% group) and C2 Rep3
rep(62, '''    if reading == "C2 Rep2":
        d = d[~d.repeat]''', '''    if reading == "C0":
        d = d[d.dc != 30]
    if reading == "C2 Rep2":
        d = d[~d.repeat]
    if reading == "C2 Rep3":
        d = d[~d.later]''')
rep(62, 'DC_READINGS = [(w, r) for w in ("W1", "W2") for r in ("C1", "C2 Rep1", "C2 Rep2")]',
    'C_READINGS = ("C0", "C1", "C2 Rep1", "C2 Rep2", "C2 Rep3")\nDC_READINGS = [(w, r) for w in ("W1", "W2") for r in C_READINGS]\n\n\ndef pbonf(post, a, b):\n    """Corrected p of a pair, or nan when a group is absent (C0 has no 30% group)."""\n    return tfus.pair(post, a, b).p_bonf if {a, b} <= set(post.a) | set(post.b) else np.nan')
rep(64, '"(4) 6 below 30": lower(post, 6, 30),', '"(4) 6 below 30": lower(post, 6, 30) if r != "C0" else None,')
rep(64, '"p_bonf 6-60": tfus.pair(post, 6, 60).p_bonf, "p_bonf 6-30": tfus.pair(post, 6, 30).p_bonf', '"p_bonf 6-60": pbonf(post, 6, 60), "p_bonf 6-30": pbonf(post, 6, 30)')
rep(67, '"p_bonf 60 vs 30": tfus.pair(post, 60, 30).p_bonf', '"p_bonf 60 vs 30": pbonf(post, 60, 30)')
for i in (73, 76):
    rep(i, 'for r in ("C1", "C2 Rep1", "C2 Rep2"):', 'for r in C_READINGS:')
rep(73, '"(2) 30 above 6 and 60": lower(post, 6, 30) and lower(post, 60, 30),', '"(2) 30 above 6 and 60": (lower(post, 6, 30) and lower(post, 60, 30)) if r != "C0" else None,')
nbformat.write(nb,P)
EOF
python3 $TMPDIR/edit1.py && echo done
```

```
done
```

**Agent calls Bash**

```bash
cd  date -u; python tools/entry.py --help 2>&1 | head -20
```

```
Sat Oct 31 22:22:45 UTC 2026
usage: entry.py [-h] [--output-dir OUTPUT_DIR] [--timeout TIMEOUT]
                [--max-minutes MAX_MINUTES]
                {lock,check,run,all,handover} entry [entry ...]

Lock, check and run one entry. This is the whole local workflow for a deposit.

    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entries/<name>   # validate metadata and conventions
    python tools/entry.py check entries/*/       # the same for every entry, in one process
    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
    python tools/entry.py all   entries/<name>   # check, then run
    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies

`lock` compiles the entry's requirements.in (direct dependencies only) into
requirements.lock.txt with every version pinned.

`check` validates entry.yaml, and the claims and attempt files that mention
the entry, against the schemas, and applies the conventions that keep a result
tied to the data:
```

**Agent calls Bash**

```bash
cd  time python tools/entry.py run entries/000945-ramachandran-2025 2>&1 | tail -30
```

```
Installed kernelspec registry-000945-ramachandran-2025 in executed/000945-ramachandran-2025/.venv/share/jupyter/kernels/registry-000945-ramachandran-2025
pass  reproduce_ramachandran_2025.ipynb  (92 s)

real	1m42.274s
user	0m32.482s
sys	0m4.854s
```

**Agent calls Bash**

```bash
cd  python3 -c "
import nbformat
nb=nbformat.read('executed/000945-ramachandran-2025/reproduce_ramachandran_2025.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    print('=====',i,c.metadata.get('tags'))
    for o in c.outputs:
        if 'text' in o: print(o['text'])
        elif o.get('output_type')=='error': print(o['ename'],o['evalue'])
" > $TMPDIR/out.txt; wc -l $TMPDIR/out.txt
```

```
994 /tmp/claude-1001/out.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/out.txt"
}
```

```
1	===== 1 None
2	loaded 75 files from dandiset 000945 version 0.250213.2212 in 74 s
3	
4	===== 3 ['sanity']
5	Files: 75 ; subject folders: 10 ['BH497', 'BH498', 'BH506', 'BH508', 'BH512', 'BH514', 'BH519', 'BH521', 'BH526', 'BH527']
6	Rats named in identifiers: ['BH498', 'BH506', 'BH508', 'BH512', 'BH519', 'BH521', 'BH526', 'BH527']
7	Files whose subject_id differs from the rat in the identifier:
8	                                               path          identifier
9	sub-BH497/sub-BH497_ses-20240310T143729_ecephys.nwb BH498_3000_200_anes
10	sub-BH497/sub-BH497_ses-20240310T145053_ecephys.nwb BH498_1500_200_anes
11	sub-BH497/sub-BH497_ses-20240310T145814_ecephys.nwb  BH498_300_200_anes
12	sub-BH497/sub-BH497_ses-20240310T150748_ecephys.nwb   BH498_30_200_anes
13	sub-BH497/sub-BH497_ses-20240310T152652_ecephys.nwb BH498_4500_200_anes
14	sub-BH514/sub-BH514_ses-20240309T183140_ecephys.nwb BH512_1500_200_anes
15	sub-BH514/sub-BH514_ses-20240309T183856_ecephys.nwb  BH512_300_200_anes
16	sub-BH514/sub-BH514_ses-20240309T184852_ecephys.nwb BH512_4500_200_anes
17	sub-BH514/sub-BH514_ses-20240309T185729_ecephys.nwb BH512_3000_200_anes
18	
19	Units table columns: {'spike_times celltype_label': 60, 'spike_times': 15}
20	Trials table columns: {'start_time stop_time': 75}
[... 605 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/out.txt",
 "offset": 626,
 "limit": 370
}
```

```
626	reading  (1) KW  (2) R1: 1500 and 3000 above 30, 300, 4500  (2) R2: top two means are 1500 and 3000  (2) R2: both above 30 and 4500
627	   Rep1    True                                      False                                    False                           False
628	   Rep2    True                                      False                                    False                           False
629	   Rep3    True                                      False                                    False                           False
630	
631	Mean response by rat (Rep1):
632	prf     30     300    1500   3000   4500
633	rat                                     
634	BH498  112.0   99.4  101.6  100.7   97.8
635	BH506   97.7  100.0  116.6   99.0  102.2
636	BH508  108.0   90.8  103.0   97.1   98.5
637	BH512  109.6  100.4   85.2   91.5  121.0
638	BH519   99.4  114.6  128.4  127.0   94.2
639	BH526  103.8  106.4   92.5  101.0  100.5
640	BH527  114.6  101.8  113.0   96.1   86.8
641	
642	===== 43 ['claim:fig5f-fsu-delayed-prf-awake']
643	awake FSU 0.5-1 s, Rep1: Kruskal-Wallis H = 59.0, p = 4.6e-12; n = {30: 232, 300: 286, 1500: 306, 3000: 319, 4500: 393}
644	  means: {30: 103.5, 300: 98.7, 1500: 101.8, 3000: 100.6, 4500: 100.3}  medians: {30: 102.0, 300: 99.4, 1500: 100.8, 3000: 100.9, 4500: 99.7}
645	   a    b   mean_a   mean_b      p  p_bonf   sig
[... 350 more lines not kept]
```

**Agent**

Outcomes match the verifier's analysis, and the new readings hold up. Now I'll rewrite the markdown cells to match the new numbers.

**Agent calls Bash**

```bash
cd entries/000945-ramachandran-2025; cat > $TMPDIR/edit2.py <<'EOF'
import nbformat
P='reproduce_ramachandran_2025.ipynb'
nb=nbformat.read(P,4)
C=nb.cells
def rep(i, old, new):
    assert C[i].source.count(old)==1, (i, old)
    C[i].source=C[i].source.replace(old,new)
# header table
rep(0, '| fig3-cell-type-sorting | Counts tested with the dataset\'s labels; the k-means features cannot be computed (no waveforms) |',
       '| fig3-cell-type-sorting | Blocked: the k-means features need waveforms, which the files lack; the counts of the dataset\'s labels are shown |')
rep(0, '| fig4h-awake-latency-wider | Tested |', '| fig4h-awake-latency-wider | Tested; blocked, as the claims file\'s readings D1 and D2 give different results |')
rep(0, '| fig6ef-rsu-ispta-rise-then-fall | Tested |', '| fig6ef-rsu-ispta-rise-then-fall | Tested; blocked, as the claims file\'s readings W1 and W2 give different results |')
rep(0, '| fig7c-rsu-delayed-dc | Tested, without the sham part |', '| fig7c-rsu-delayed-dc | Blocked: the paper\'s own 30% DC recordings are not in the dandiset, and the substitutes decide the outcome |')
rep(0, '| fig5a-rsu-time-locked-prf-awake | Tested, without the sham parts |', '| fig5a-rsu-time-locked-prf-awake | Tested; the sham parts cannot be |')
rep(0, '| fig5c-rsu-time-locked-prf-anesth | Tested (two labelled rats), without the sham parts |', '| fig5c-rsu-time-locked-prf-anesth | Tested (two labelled rats); the sham parts cannot be |')
for c in ('fig5e-rsu-delayed-prf-awake', 'fig5f-fsu-delayed-prf-awake', 'fig7a-rsu-time-locked-dc', 'fig7d-fsu-delayed-dc'):
    rep(0, f'| {c} | Tested, without the sham part |', f'| {c} | Tested; the sham part cannot be |')
# cell 4
C[4].source += '''

The dandiset's description explains the `_2` files: recordings were "taken first at 8-10 months,
and then some repeats taken at 12 months", and "Some subjects have duplicate recordings taken a
few months after the original ones". The session start times (table above) do not always agree
with the suffix; see the check after the next one.'''
# cell 8
C[8].source += '''

The session start times show that the `_2` suffix does not always mark the later recording.
Seven of the ten `_2` recordings are four to seven months after the recording without the suffix
(BH498 3000 Hz; BH506 3000 and 4500 Hz; BH508 300, 3000 and 4500 Hz). Three are earlier:
BH498_1500_200_2 and BH498_4500_200_2 one day before the unsuffixed recordings (5 and 6 March
2024), and BH508_1500_200_2 two months before (August against October 2023). So which recording
of a pair is the "repeat" the description mentions is not settled by the names, and the readings
below include one based on the dates. The DC recordings (TBD 40 and 400 us) were made in January
2024 (BH526) and March 2024 (BH506, BH521), three to five months after the 1500 Hz, 200 us
recordings of the same rats (October 2023); BH521 has no awake 200 us recording. The 30% group
that the duty cycle claims borrow therefore comes from another session months earlier.'''
# cell 12: caveat on time-locked responses
C[12].source += '''

This also limits every time-locked claim. Among the awake 200 us PRF-series recordings, only
BH498_1500_200 (t = 3.62) and BH506_3000_200 (t = 12.96) show a population rise in 0 to 67 ms, and
among the anesthetized 200 us ones only BH512's 1500 and 3000 Hz (t = 9.96 and 6.57). The 40 and
400 us recordings respond most clearly (6 of the 8 at t > 3). Group differences in the time-locked
window at 200 us therefore rest on small changes in most recordings.'''
# cell 13: readings
C[13].source = '''## Readings and selections used in every claim

The claims file's header fixes the method; the dataset decides which of its readings can run.

- **Cell type.** K0: the dataset carries labels, so they are used. K1 and K2 (k-means on the
  initial and after-hyperpolarization phase durations) cannot run: the files hold no waveforms.
  That the labels are the paper's k-means output is an assumption; the baseline rates above are
  consistent with it and do not prove it.
- **Trials.** The files hold 500 trials, the 505 delivered less the first five (T1, Methods 2.4);
  T2 (all 505) cannot run. That the 500 are trials 6 to 505 cannot be checked: the dandiset's
  description says only that "each recording has 500 trials". Five recordings hold 203 to 339
  trials and are used as they are.
- **Exclusion.** E1 = E2: the dataset marks no excluded unit or interval.
- **Windows.** W1 (exact window) and W2 (overlapping PSTH bins) are both run.
- **Groups.** G1 only: there are no sham recordings, so G2 cannot run.
- **Repeats** (not named by the claims file; the dandiset adds them). Ten awake recordings repeat
  a condition in the same rat. The Methods describe one recording per parameter set per rat
  ("Recordings for a single rat for each set of parameters were completed on the same day",
  Methods 2.3), the paper mentions no repeats, and the dandiset's description calls them repeats
  taken "a few months after the original ones". Three readings are run: Rep1 counts every
  recording once, repeats included; Rep2 leaves out the `_2` recordings; Rep3 keeps the earliest
  recording of each rat and condition, following the description's timing where the suffix and
  the dates disagree (three pairs, see above). Rep2 and Rep3 both give one recording per rat and
  condition. Where Rep1 and those two give different outcomes, one recording per rat and
  condition is adopted as an assumption (Methods 2.3 and the dandiset's description); where Rep2
  and Rep3 differ from each other, neither is preferred, as the BH498 pairs are a day apart.
- **Anesthetized data.** Only two rats' anesthetized recordings carry labels (BH498 at all five
  PRFs, BH512 without 30 Hz); BH521's three are unlabelled and cannot enter a cell-type test. Rat
  and PRF are therefore confounded under anesthesia: the 30 Hz group is BH498 alone.
- **Sham.** The dandiset holds no sham recording. Parts of a criterion that compare with sham
  are reported as not tested. A claim with an untested part is not judged reproduced: its best
  outcome is partially reproduced. The claims file's header provides this for an anesthetized
  sham; the same is done for the awake sham.
- **Readings of the claims file that disagree.** Where the readings the claims file names (W1/W2,
  S1/S2, D1/D2, L1/L2, A1/A2) give different outcomes, the claim is blocked as
  methods_underspecified, as the header says, with every result shown.
- **The 30% duty cycle.** The paper's DC series had its own 30% recordings, which are not in the
  dandiset. The substitutes (C1, C2, defined before the duty cycle claims) and C0, without a 30%
  group, are shown. A part of a criterion that needs the 30% group is treated as data missing,
  and a claim whose outcome depends on that part is blocked as data missing.'''
# fig3 result
C[17].source = '''**Result: blocked (data missing).** Both the reproduced and the partially reproduced outcome of
the criterion require the clusters to separate on the initial phase and after-hyperpolarization
durations, and the files hold no waveforms, so neither can be reached. With the dataset's labels
(K0), two single recordings give all three counts within tolerance (R1): BH527_30_200 with 28 FSU,
34 RSU and 62 units, and BH508_4500_200_2 with 28 FSU, 30 RSU and 58 units; under Rep2 and Rep3
only BH527_30_200 does, as BH508_4500_200_2 is a later repeat. No rat's series matches (R2;
totals 77 to 616). The match is no more than chance: 22 of 59 recordings have a total within
60 +- 6, and if each recording's FSU count were binomial with the pooled FSU share (0.505), 3.84
recordings would be expected to match all three counts, against 2 observed. The labels follow the
expected rate difference in 46 of 59 recordings (FSU median baseline rate above the RSU median;
8.60 against 5.84 Hz over units). The other claims use the labels directly, as the claims file's
header says for K0, and do not need the waveform features.'''
# fig4-rsu result
C.insert(20, nbformat.v4.new_markdown_cell('''**Result: blocked (data missing).** No sham recording exists. The awake half already fails one
of the criterion's conditions: the awake 1500 Hz RSU mean is 98.1 to 98.7% of baseline under every
reading, not above 100%. So the claim could not be reproduced whatever a sham would show; at best
it would be partially reproduced, on the anesthetized half (106.4 to 107.0%, two rats).'''))
nbformat.write(nb,P)
EOF
python3 $TMPDIR/edit2.py && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/000945-ramachandran-2025; cat > $TMPDIR/edit3.py <<'EOF'
import nbformat
P='reproduce_ramachandran_2025.ipynb'
nb=nbformat.read(P,4)
C=nb.cells
def after(tag):
    """The markdown cell right after the cell tagged claim:<tag>."""
    for i,c in enumerate(C):
        if f'claim:{tag}' in c.metadata.get('tags', []):
            assert C[i+1].cell_type=='markdown' and C[i+1].source.startswith('**Result'), tag
            return i+1
def setr(tag, text):
    C[after(tag)].source = text
def find(prefix):
    idx=[i for i,c in enumerate(C) if c.source.startswith(prefix)]
    assert len(idx)==1, prefix
    return idx[0]

setr('fig4hi-fsu-delayed-latency', '''**Result: not reproduced.** Under none of the 24 readings (S1/S2, D1/D2, L1/L2, Rep1/Rep2/Rep3)
do awake FSU onsets come later than anesthetized ones at p < 0.001: rank-sum p ranges from 0.018
to 0.92, and in 8 readings the anesthetized mean is the later one. The awake means (0.40 to 0.58 s)
are within 0.51 +- 0.14 s, but the anesthetized means (0.38 to 0.52 s) are all outside 0.24 +- 0.08
s. Most FSU qualify as having a delayed response (193 to 265 of 306 awake under Rep1, 262 of 306,
or 86%, under S1 D1; 34 or 39 of 50 anesthetized), and latencies spread over 0.07 to 1.39 s awake
and 0.07 to 1.29 s anesthetized, so the one-SEM rule of the Methods, as the claims file reads it,
flags most units and the onsets look largely noise-driven. Rat means range from 0.25 s (BH498) to
0.95 s (BH526) awake. The anesthetized FSU come from two rats.''')
setr('fig4h-awake-latency-wider', '''**Result: blocked (methods underspecified).** The claims file's readings give different results:
the awake SD exceeds the anesthetized SD under every D1 reading (0.384 to 0.396 s against 0.367 to
0.372 s), but not under D2, where it is smaller in 10 of 12 readings (0.381 to 0.393 s against 0.393
to 0.406 s) and equal to three decimals in the other two. The header blocks a claim whose readings
disagree. Under every reading the SDs are within 0.04 s of each other, with no contrast like the
paper's 0.14 against 0.08 s. Under S1 D1 L1 Rep1 the awake histogram has its largest count in the
first allowed bin (61 of 262 at 0.071 s) and several smaller local maxima; the anesthetized
histogram (39 units) is flat with many single-count maxima.''')
setr('fig5a-rsu-time-locked-prf-awake', '''**Result: not reproduced.** PRF is a significant factor (Kruskal-Wallis p = 3.3e-16, W1 Rep1),
but the post hoc pattern differs. The highest mean is at 3000 Hz (108.2%; 1500 Hz 98.5%), and
3000 Hz differs from 1500 and 4500 Hz (corrected p < 1e-4), so part (4) fails under every reading.
300 Hz is not below 1500 or 4500 Hz (part 3 fails under every reading), and 30 Hz is below every
higher PRF only under W2 Rep1 and W2 Rep3 (part 2). Parts (5) and (6) need the sham and are not
tested; even if both held, (1) with at most three other parts falls short of the four the partial
outcome needs. Means by rat vary widely (BH526 at 64 to 101%, BH506 at 100 to 130%).''')
setr('fig5c-rsu-time-locked-prf-anesth', '''**Result: not reproduced.** Under anesthesia (two labelled rats) the Kruskal-Wallis is
significant (p = 7.3e-08 W1, 7.7e-07 W2) and 30 Hz and 300 Hz do not differ (part 7 holds), but
parts (2), (3) and (4) do not: 1500 Hz is the peak (107.0%), 30 Hz is not below 3000 or 4500 Hz,
300 Hz is not below 3000 or 4500 Hz, and 1500 Hz differs from 4500 Hz (and from 3000 Hz under W1).
Even if the two sham parts held, (1) with three other parts falls short of the five the partial
outcome needs. With two rats, PRF and rat are confounded: the 30 Hz group is BH498 alone, and the
1500 Hz peak comes from BH512 (110.4% against 101.7% in BH498; BH498 ranges 100.0 to 101.7% over
all five PRFs).''')
setr('rsu-time-locked-anesthesia-factor', '''**Result: not reproduced.** Anesthesia is a factor at p = 0.0083 to 0.018 over the twelve readings
(below 0.01 only under W1 Rep3), but in the reverse direction: the anesthetized mean (102.6 to
102.9%) is above the awake mean (100.1 to 100.4%) under every reading. The anesthetized units come
from two rats and the awake units from seven, so the state effect is partly a rat effect: with only
the two rats that have labelled anesthetized data, the effect disappears (p = 0.425; awake 103.4%,
anesthetized 102.9%).''')
setr('fig5bd-fsu-time-locked-no-prf', '''**Result: not reproduced.** By the paper's test FSU time-locked responses do differ across PRF:
Kruskal-Wallis p = 1.8e-12 awake and 5.5e-04 anesthetized (W1 Rep1), with 4 to 6 significant post
hoc pairs awake and 2 or 3 anesthetized under every reading. The effects are small: group medians
span 98.7 to 103.4% awake (W1 Rep1) and 99.8 to 103.9% anesthetized; the awake 3000 Hz mean is
106.8%. The anesthetized groups come from two rats (30 Hz from BH498 alone).''')
setr('fig5e-rsu-delayed-prf-awake', '''**Result: not reproduced.** PRF is a significant factor (p = 6e-20 Rep1, 4.5e-15 Rep2, 5.1e-15
Rep3), but the two highest means are at 1500 Hz and 30 Hz (106.7 and 106.6% Rep1; 108.8 and 106.6%
Rep2; 107.3 and 106.6% Rep3), not 1500 and 3000 Hz: 3000 Hz (102.3 to 103.3%) is below 30 Hz
(corrected p < 1e-4) and not above 300 Hz. Part (2) fails under both of its readings and every
repeat reading; part (3) needs the sham and is not tested.''')
setr('fig5f-fsu-delayed-prf-awake', '''**Result: not reproduced.** PRF is a significant factor (p = 4.6e-12 Rep1) and 30 Hz differs
from 1500, 3000 and 4500 Hz (part 3), but the strongest mean is at 30 Hz (103.5%), not 4500 Hz
(100.3 to 100.4%), and 300 Hz does not differ from 4500 Hz (corrected p = 1.0), under every repeat
reading. Part (3) is tested without direction, as the criterion says "differs", but 30 Hz is
above the higher PRFs, the opposite of the paper's pattern. Part (5) needs the sham; even if it
held, (1) with two other parts falls short of the three the partial outcome needs.''')
setr('fig5gh-delayed-prf-anesth', '''**Result: not reproduced.** Under anesthesia PRF is not a significant factor for delayed
responses: Kruskal-Wallis p = 0.16 (W1) and 0.12 (W2) for RSU, 0.16 and 0.18 for FSU. The pooled
1500 to 4500 Hz means are above the 30 and 300 Hz means by less than one percentage point (RSU
99.97 against 99.15%, FSU 99.87 against 99.35%, W1). The data are two rats, and the 30 Hz group is
BH498 alone; every rat and PRF mean is within 98.5 to 100.9%.''')
setr('delayed-anesthesia-factor', '''**Result: reproduced, resting on an assumption.** With one recording per rat and condition, the
reading adopted, anesthesia is a significant factor for both types under all four model and
window readings, whether the `_2` recordings are left out (Rep2) or the earliest recording of each
pair is kept (Rep3): RSU p = 4.2e-09 to 1.8e-08 and FSU p = 0.0012 to 0.0015, with the
anesthetized mean lower in both (RSU 99.7 against 104.3 to 104.6%, FSU 99.7 against 101.2 to
101.3%). With the repeats (Rep1) the RSU part holds (p < 1e-5) but the FSU effect is p = 0.038 to
0.041, which misses the 0.01 bound: partially reproduced under that reading. Leaving out the
recording filed under both BH498 and BH508 does not change this (FSU p = 0.0016 to 0.0019 under
Rep2 and Rep3). The anesthetized units come from two rats, so the state effect may also be a rat
effect.''')
setr('fig6ef-rsu-ispta-rise-then-fall', '''**Result: blocked (methods underspecified).** The delayed means do not rise to their peak under
any reading (106.6% at 30 Hz, 101.2 to 102.8% at 300 Hz, 106.7 to 108.8% at 1500 Hz), so at best
the claim is partially reproduced, on the time-locked window. That window holds under W2 with every
repeat reading and under W1 with Rep1 and Rep3: means rise from 30 Hz (96.4 to 96.8%) to a peak at
3000 Hz (60.26 mW/cm2; 107.7 to 108.7%) and fall at 4500 Hz (98.0 to 99.5%). Under W1 Rep2 it
fails: the 300 Hz mean (98.2%) is 0.1 point above the 1500 Hz mean (98.1%), against SEMs of 1.1
and 1.3. With one recording per rat and condition (the reading adopted) W1 and W2 thus disagree
under Rep2, and the claims file's header blocks a claim whose readings disagree.''')
setr('fig6fh-fsu-ispta', '''**Result: not reproduced.** The time-locked part fails (fig5bd: awake Kruskal-Wallis p =
1.8e-12). The delayed FSU means do not increase with ISPTA: 103.5, 98.7, 101.8, 100.6 and 100.3%
from 30 to 4500 Hz (Spearman rho = -0.4, Pearson r = -0.27, Rep1; rho = -0.3 Rep2 and Rep3).''')
setr('fig5a-1500-highest-time-locked-mean', '''**Result: not reproduced.** The highest mean RSU time-locked response is at 3000 Hz under every
reading (107.7 to 108.7%), and it is significantly above 1500 Hz (corrected p = 0.0040 or less);
1500 Hz gives 98.1 to 98.7%.''')
i = find('## Duty cycle claims')
C[i].source = '''## Duty cycle claims (fig7a to fig7d)

The DC series is 1500 Hz with TBD 40, 200 and 400 us (6, 30 and 60%). The dandiset holds 6% and
60% recordings for three rats (BH506, BH521, BH526) and no 30% recording of its own: the paper's
30% recordings, made with the DC series at 10 months, are missing. The only 1500 Hz, 200 us
recordings are those of the PRF series, made three to five months before the DC recordings (data
check). The claims file names no reading for this; three come from what the dandiset holds: C0,
no 30% group (the tests run on 6% and 60% alone, Bonferroni over one pair); C1, the PRF series'
1500 Hz, 200 us recordings of the same rats (BH506 and BH526; BH521 has none); and C2, every awake
1500 Hz, 200 us recording, run with each repeat reading. C1 and C2 are substitutes: a part of a
criterion that needs the 30% group is treated as data missing, and does not decide an outcome.
Parts that compare with sham cannot be tested.'''
setr('fig7a-rsu-time-locked-dc', '''**Result: not reproduced.** Part (2) does not need the 30% group and fails under every reading: 6%
is the highest group, not the lowest, at 180.8% against 147.5% at 60% (W1), and 6% does not differ
from 60% (corrected p = 1.0; 0.67 to 0.91 under C0). Parts (3) and (4) need the sham or the 30%
group and are not tested, and under C0 the Kruskal-Wallis is not significant, so whatever those
parts would show, the claim cannot be reproduced. With the substitutes the 30% group is far below
both (90.4 to 98.7%). The 6% and 60% effects come mostly from BH506 (249.0 and 209.9%); BH521 and
BH526 give 113 to 121%.''')
setr('fig7a-60-highest-time-locked-mean', '''**Result: not reproduced.** The highest mean is at 6% DC under every reading (176.3 to 180.8%),
above 60% (147.1 to 147.5%); this does not need the 30% group. With the substitutes, 60% is
significantly above 30% (corrected p < 1e-16), where the claim says only 6% differs from it.''')
setr('fig7b-fsu-time-locked-dc', '''**Result: not reproduced.** FSU time-locked responses differ across DC under every reading, and
the difference between 6% and 60% does not need the 30% group: under C0 the Kruskal-Wallis gives
p = 0.0054 (one pair, significant), and with the substitutes p = 3.5e-12 (W1 C1) or smaller, with
all three pairs significant. FSU respond strongly at 6% and 60% (means 156.8 and 205.3%, medians
115.0 and 128.6%) and not at the substitute 30% (median 100.8%, C1); the largest responses are in
BH506 (338.6 and 403.3%).''')
setr('fig7c-rsu-delayed-dc', '''**Result: blocked (data missing).** Part (2), 30% above 6% and 60%, needs the paper's 30%
recordings, which are not in the dandiset, and the substitutes decide it: with the same rats' 1500
Hz, 200 us recordings (C1) the Kruskal-Wallis is not significant (p = 0.21) and no pair differs;
with every such recording (C2) the effect is significant (p = 2.2e-04 Rep1, 3.7e-05 Rep2, 1.9e-04
Rep3) and 30% is above 6% and 60%. Part (4), 6% against 60%, also depends on the 30% group through
the Bonferroni family: 6% is below 60% at p = 0.024 alone (C0), and at corrected p = 0.071 over
three pairs. Part (3) needs the sham.''')
setr('fig7d-fsu-delayed-dc', '''**Result: partially reproduced.** Parts (1) and (2) hold under every reading, C0 included, so
they do not depend on the substitute 30% group: the Kruskal-Wallis is significant (p = 0.0051 C0,
0.011 C1, 4.5e-07 to 1.4e-06 C2) and 60% is above 6% (p = 0.0051 alone, corrected p = 0.015 over
three pairs). Part (3), 6% against sham, cannot be tested, so the claim is not judged reproduced.
The difference is small and both groups are below baseline (means 99.6% at 60% and 98.2% at 6%).''')
nbformat.write(nb,P)
EOF
python3 $TMPDIR/edit3.py && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/000945-ramachandran-2025; cat > $TMPDIR/edit4.py <<'EOF'
import nbformat
P='reproduce_ramachandran_2025.ipynb'
nb=nbformat.read(P,4)
C=nb.cells
i=[k for k,c in enumerate(C) if c.source.startswith('**Result: blocked (methods underspecified).** The claims file')][0]
old='where it is smaller in 10 of 12 readings (0.381 to 0.393 s against 0.393\nto 0.406 s) and equal to three decimals in the other two.'
assert old in C[i].source
C[i].source=C[i].source.replace(old,'where it is smaller in 10 of 12 readings (0.381 to 0.393 s against 0.393\nto 0.406 s) and larger by less than 0.001 s in the other two (0.393 against 0.393 s).')
j=[k for k,c in enumerate(C) if c.source.startswith('## Summary')][0]
C[j].source='''## Summary

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

| Claim | Outcome |
|---|---|
| fig3-cell-type-sorting | Blocked: data missing (no waveforms for the k-means features); label counts match in one or two recordings, no more than chance |
| fig4-rsu-time-locked-both-states | Blocked: data missing (no sham); the awake mean is below 100% |
| fig4hi-fsu-delayed-latency | Not reproduced |
| fig4h-awake-latency-wider | Blocked: methods underspecified (D1 and D2 disagree) |
| fig5a-rsu-time-locked-prf-awake | Not reproduced |
| fig5c-rsu-time-locked-prf-anesth | Not reproduced |
| rsu-time-locked-anesthesia-factor | Not reproduced |
| fig5bd-fsu-time-locked-no-prf | Not reproduced |
| fig5e-rsu-delayed-prf-awake | Not reproduced |
| fig5f-fsu-delayed-prf-awake | Not reproduced |
| fig5gh-delayed-prf-anesth | Not reproduced |
| delayed-anesthesia-factor | Reproduced (assumption: one recording per rat and condition, Rep2 or Rep3) |
| fig6ad-time-adjacent-batch | Blocked: data missing (second batch) |
| fig6ef-rsu-ispta-rise-then-fall | Blocked: methods underspecified (W1 and W2 disagree under Rep2; at best partial) |
| fig6fh-fsu-ispta | Not reproduced |
| fig5a-1500-highest-time-locked-mean | Not reproduced |
| fig7a-rsu-time-locked-dc | Not reproduced |
| fig7a-60-highest-time-locked-mean | Not reproduced |
| fig7b-fsu-time-locked-dc | Not reproduced |
| fig7c-rsu-delayed-dc | Blocked: data missing (the paper's 30% DC recordings) |
| fig7d-fsu-delayed-dc | Partially reproduced (the sham part cannot be tested) |
| sham-no-auditory-response | Blocked: methods underspecified, and no sham data |

**How the analysis differs from the paper's.** Cell types are the dataset's labels; the k-means
on waveform features cannot be run, as there are no waveforms. The files hold 500 trials (the
paper's 505 less five), and five recordings hold 203 to 339. No sham recording exists, so every
comparison with sham is left out, and no claim with a sham part is judged reproduced. The
anesthetized PRF series has labelled units from two rats (the paper: ten), and BH512 has no 30 Hz
recording, so rat and PRF are confounded under anesthesia. The DC series has 6% and 60% recordings
from three rats and no 30% recording of its own; the PRF series' 1500 Hz, 200 us recordings stand
in for it, without deciding any outcome. Ten awake recordings repeat a condition in the same rat;
results are shown with all of them (Rep1), without the `_2` recordings (Rep2) and with the
earliest recording of each pair (Rep3). No unit was excluded for a fluctuating baseline or for
movement, as the dataset marks none. Most 200 us recordings show no time-locked population
response, which limits every time-locked claim.

**What was found about the dataset.** Twelve of the 75 files are second copies of other files:
the anesthetized recordings of BH498 and BH512 are each deposited twice (with labels under
subject folders BH497 and BH514, without labels under BH498 and BH512), BH512's 1500 Hz
anesthetized recording a third time, and one 30 Hz recording is filed under both BH498 and
BH508, with start times 6.5 hours apart. The condition of a recording is coded only in its
identifier. The dandiset's description says the repeats were taken months after the originals,
but three of the ten `_2` recordings are earlier than their unsuffixed pair. The 2.2 s
`stop_time` is not described. Fifteen anesthetized files have no cell-type labels. Every
file gives age P24W, where the paper gives 7 to 10 months and the description 8 to 12, and the
labelled anesthetized copies are described as awake. The second batch of five rats, the sham
condition and the 30% DC recordings are not in the dandiset. In most 200 us recordings no
time-locked population response can be detected (10 of 64 recordings show one at t > 3, among
them 4 of the 6 awake 40 and 400 us recordings), while the 6% and 60% DC recordings respond
strongly, FSU included.'''
nbformat.write(nb,P)
EOF
python3 $TMPDIR/edit4.py && grep -c "—\|rather" reproduce_ramachandran_2025.ipynb tfus.py
```

```
reproduce_ramachandran_2025.ipynb:0
tfus.py:0
```

**Agent calls Bash**

```bash
cd entries/000945-ramachandran-2025; python3 -c "
import nbformat
nb=nbformat.read('reproduce_ramachandran_2025.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type=='markdown' and ('judged on' in c.source or 'cannot be tested' in c.source) and not c.source.startswith('**Result'): print(i, repr(c.source[-300:]))
"
```

```
27 '-locked responses; 30 Hz and 300 Hz PRF\n> give lower responses than every higher PRF (so 30 Hz is also below 300 Hz), 1500, 3000 and\n> 4500 Hz do not differ, and sham differs from every PRF but 30 Hz.\n\nParts (5) and (6) compare with sham and cannot be tested; the claim is judged on parts (1) to (4).'
30 ' on PRF as in the awake model, the only\n> difference being that 30 Hz and 300 Hz do not differ significantly.\n\nTwo labelled rats: BH498 (all five PRFs) and BH512 (no 30 Hz). The repeats reading does not apply\n(no anesthetized repeats remain). Parts (5) and (6) compare with sham and cannot be tested.'
37 '## fig5bd-fsu-time-locked-no-prf\n\n> FSU time-locked responses show no significant differences across PRF levels, in either the\n> awake or the anesthetized model.\n\nA claim of absence, judged on the Kruskal-Wallis across the five PRFs (G1) at 0.05 and the post\nhoc tests at Bonferroni-corrected 0.05.'
40 'delayed responses (0.5 to 1 s) depend on PRF, are highest at 1500 Hz and 3000 Hz with\n> lower responses at both lower and higher PRFs, and every PRF is significantly higher than sham.\n\nPart (3) compares with sham and cannot be tested. The 0.5 to 1 s window is on bin edges, so W1\nand W2 are the same.'
43 'fsu-delayed-prf-awake\n\n> Awake FSU delayed responses depend on PRF, are strongest at 4500 Hz, differ between 30 Hz and\n> the three highest PRFs and between 300 Hz and the two highest, and at 30 Hz and 300 Hz are not\n> significantly higher than sham.\n\nPart (5) compares with sham and cannot be tested.'
62 'me rats (BH506 and BH526; BH521 has none); and C2, every awake\n1500 Hz, 200 us recording, run with each repeat reading. C1 and C2 are substitutes: a part of a\ncriterion that needs the 30% group is treated as data missing, and does not decide an outcome.\nParts that compare with sham cannot be tested.'
70 '## fig7b-fsu-time-locked-dc\n\n> FSUs show no time-locked response across DC levels; no significant differences are observed.\n\nA clai
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000945-ramachandran-2025; python3 - <<'EOF'
import nbformat
P='reproduce_ramachandran_2025.ipynb'
nb=nbformat.read(P,4)
c=nb.cells[27]
c.source=c.source.replace('Parts (5) and (6) compare with sham and cannot be tested; the claim is judged on parts (1) to (4).',
 'Parts (5) and (6) compare with sham and cannot be tested, so the claim can at best be partially\nreproduced.')
nbformat.write(nb,P)
EOF
cd  date -u; python tools/entry.py run entries/000945-ramachandran-2025 2>&1 | tail -2
```

```
Sat Oct 31 22:27:01 UTC 2026
Installed kernelspec registry-000945-ramachandran-2025 in executed/000945-ramachandran-2025/.venv/share/jupyter/kernels/registry-000945-ramachandran-2025
pass  reproduce_ramachandran_2025.ipynb  (90 s)
```

**Agent calls Bash**

```bash
cd  python3 -c "
import nbformat
nb=nbformat.read('executed/000945-ramachandran-2025/reproduce_ramachandran_2025.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    print('=====',i,c.metadata.get('tags'))
    for o in c.outputs:
        if 'text' in o: print(o['text'])
        elif o.get('output_type')=='error': print(o['ename'],o['evalue'])
" > $TMPDIR/out2.txt; diff <(grep -v "^=====\|loaded 75\|notebook ran" $TMPDIR/out.txt) <(grep -v "^=====\|loaded 75\|notebook ran" $TMPDIR/out2.txt) && echo same
```

```
Exit code 1
307d306
< 
309a309
> 
472d471
< 
842a842
> 
913d912
<
```

**Agent**

Notebook runs clean (90 s) with the same numbers. Now rewriting the attempt record.

**Agent calls Bash**

```bash
cd  sed -n '/^findings:/,$p' attempts/000945-ramachandran-2025-01.yaml | head -5; grep -n "^  url\|^outcomes" attempts/000945-ramachandran-2025-01.yaml; sed -n 1,25p schemas/attempt.schema.json; grep -n '"proposed"' -A30 schemas/attempt.schema.json | head -40
```

```
findings:
- kind: data_missing
  statement: The sham condition and the second batch of five rats (awake and anesthetized
    recordings in the same week at a low PRF and 1500 Hz) are not in the dandiset. Four claims
    cannot be tested, and every comparison with sham in the others is left out.
22:outcomes:
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
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 160,252p schemas/attempt.schema.json; sed -n 284,332p schemas/attempt.schema.json
```

```
],
          "properties": {
            "platform": {
              "description": "The platform that ran it, e.g. GitHub Actions, or local for a person's machine.",
              "type": "string",
              "minLength": 1
            },
            "url": {
              "description": "The run that wrote the record, e.g. https://github.com/<owner>/<repo>/actions/runs/<id>.",
              "type": "string",
              "pattern": "^https://"
            }
          }
        }
      }
    },
    "outcomes": {
      "description": "One per claim attempted.",
      "type": "array",
      "minItems": 1,
[... 122 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,21p attempts/000945-ramachandran-2025-01.yaml > $TMPDIR/head.yaml; cat $TMPDIR/head.yaml | tail -5
```

```
model: claude-opus-5-5
    protocol: pilot-13
  runner:
    platform: GitHub Actions
    url: https://github.com/catalystneuro/encore/actions/runs/41243437657
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/body.yaml <<'EOF'
outcomes:
- claim: fig3-cell-type-sorting
  outcome: blocked
  blocked_by: data_missing
  notebook: reproduce_ramachandran_2025.ipynb
  output: claim:fig3-cell-type-sorting
  measured:
  - 28
  - 34
  - 62
  notes: Both the reproduced and the partially reproduced outcome of the criterion require the
    clusters to separate on the initial phase and after-hyperpolarization durations, and the
    files hold no waveforms, so K1 and K2 cannot run and neither outcome can be reached. With the
    dataset's labels (K0) two single recordings (R1) give all three counts within tolerance,
    BH527_30_200 with 28 FSU, 34 RSU and 62 units (given as measured) and BH508_4500_200_2 with 28
    FSU, 30 RSU and 58 units; under Rep2 and Rep3 only BH527_30_200 does. No rat's series matches
    (R2; totals 77 to 616). The match is no more than chance, as 22 of 59 recordings have a total
    within 60 +- 6 and a binomial model with the pooled FSU share (0.505) expects 3.84 recordings
    to match all three counts, against 2 observed. FSU have the higher median baseline rate in 46
    of 59 labelled recordings (8.60 against 5.84 Hz over units).
  deviations:
  - Cell types are the dataset's labels (K0); that they are the paper's k-means output is assumed,
    and is consistent with the baseline rates without being shown.
  - The other claims depend on this one for cell types. They use the K0 labels, as the claims
    file's header provides when the dataset carries labels, and do not need the waveform features
    whose absence blocks this claim, so they are tested.
- claim: fig4-rsu-time-locked-both-states
  outcome: blocked
  blocked_by: data_missing
  notebook: reproduce_ramachandran_2025.ipynb
  output: claim:fig4-rsu-time-locked-both-states
  notes: The criterion compares the 1500 Hz, 200 us RSU time-locked responses with the sham
    sessions of each state, and the dandiset holds no sham recording. The awake half already
    fails the condition that the 1500 Hz mean be above 100%, as RSU at 1500 Hz average 98.1 to
    98.7% of baseline awake under every reading (n = 227 or 303), so the claim could not be
    reproduced whatever a sham would show; at best it would be partially reproduced, on the
    anesthetized half (106.4 to 107.0%, n = 78, two rats).
- claim: fig4hi-fsu-delayed-latency
  outcome: not_reproduced
  notebook: reproduce_ramachandran_2025.ipynb
  output: claim:fig4hi-fsu-delayed-latency
  measured:
  - 0.506
  - 0.447
  notes: Under none of the 24 readings (S1/S2, D1/D2, L1/L2, Rep1/Rep2/Rep3) are awake onsets later
    at p < 0.001; rank-sum p is 0.018 to 0.92, and in 8 readings the anesthetized mean is the
    later. Awake means are 0.40 to 0.58 s (within 0.51 +- 0.14), anesthetized means 0.38 to 0.52 s
    (all outside 0.24 +- 0.08). Measured values are the S1 D1 L1 Rep1 means (anesthetized, awake).
    193 to 265 of 306 awake FSU (86% under S1 D1) and 34 or 39 of 50 anesthetized FSU have a
    delayed response under the paper's rule as the claims file reads it, and latencies spread over
    0.07 to 1.39 s in both states, so the rule flags most units and the onsets look largely
    noise-driven. The anesthetized FSU come from two rats (BH498, BH512). Q1 and Q2 select the
    same recordings here.
  deviations:
  - The anesthetized FSU come from two labelled rats where the paper had ten; batch 2 is not in
    the dandiset.
  - T2 (505 trials) cannot be run; the files hold 500 trials, or fewer in five recordings.
- claim: fig4h-awake-latency-wider
  outcome: blocked
  blocked_by: methods_underspecified
  notebook: reproduce_ramachandran_2025.ipynb
  output: claim:fig4h-awake-latency-wider
  notes: The claims file's readings give different results, and its header blocks a claim whose
    readings disagree. The awake SD exceeds the anesthetized SD under every D1 reading (0.384 to
    0.396 s against 0.367 to 0.372 s) but is smaller under 10 of 12 D2 readings (0.381 to 0.393 s
    against 0.393 to 0.406 s) and larger by under 0.001 s in the other two. Under every reading
    the SDs are within 0.03 s of each other, with no contrast like the paper's 0.14 against
    0.08 s. The awake histogram (S1 D1 L1 Rep1) has its largest count in the first allowed bin (61
    of 262 at 0.071 s) and several smaller local maxima. Whether the first bin allowed is one
    starting at or after 67 ms (D1) or one ending after it (D2) is asked of the paper's authors.
- claim: fig5a-rsu-time-locked-prf-awake
  outcome: not_reproduced
  notebook: reproduce_ramachandran_2025.ipynb
  output: claim:fig5a-rsu-time-locked-prf-awake
  notes: PRF is a significant factor (Kruskal-Wallis p = 3.3e-16, W1 Rep1) but the post hoc
    pattern differs. The highest mean is at 3000 Hz (108.2%; 1500 Hz 98.5%), and 3000 Hz differs
    from 1500 and 4500 Hz, so part (4) fails under every reading; part (3) fails under every
    reading; part (2) holds only under W2 Rep1 and W2 Rep3. Parts (5) and (6) need the sham and
    were not tested; even if both held, part (1) with at most three others falls short of the four
    the partial outcome needs.
  deviations:
  - No sham recording exists; parts (5) and (6) are reported as not tested, and a claim with an
    untested part is not judged reproduced.
  - Ten awake recordings repeat a condition in the same rat; results are given with them (Rep1),
    without the `_2` recordings (Rep2) and with the earliest recording of each pair (Rep3).
- claim: fig5c-rsu-time-locked-prf-anesth
  outcome: not_reproduced
  notebook: reproduce_ramachandran_2025.ipynb
  output: claim:fig5c-rsu-time-locked-prf-anesth
  notes: The Kruskal-Wallis is significant (p = 7.3e-08 W1, 7.7e-07 W2) and 30 and 300 Hz do not
    differ (part 7), but parts (2), (3) and (4) fail under both readings. 1500 Hz is the peak
    (107.0%) and differs from 4500 Hz; 30 and 300 Hz are not below 3000 or 4500 Hz. Even if the two
    sham parts held, part (1) with three others falls short of the five the partial outcome needs.
    With two rats PRF and rat are confounded, as the 30 Hz group is BH498 alone and the 1500 Hz
    peak comes from BH512 (110.4% against 101.7% in BH498, whose means span 100.0 to 101.7%).
  deviations:
  - Two labelled rats (BH498 at five PRFs, BH512 without 30 Hz) where the paper had ten; BH521's
    anesthetized recordings have no labels.
  - Parts (5) and (6) need the sham and were not tested.
- claim: rsu-time-locked-anesthesia-factor
  outcome: not_reproduced
  notebook: reproduce_ramachandran_2025.ipynb
  output: claim:rsu-time-locked-anesthesia-factor
  notes: Anesthesia is a factor at p = 0.0083 to 0.018 over the twelve readings (A1/A2, W1/W2,
    Rep1/Rep2/Rep3), below 0.01 only under W1 Rep3, and in the reverse direction under every
    reading; the anesthetized mean (102.6 to 102.9%) is above the awake mean (100.1 to 100.4%).
    The anesthetized units come from two rats and the awake units from seven, so the state effect
    is partly a rat effect; with only BH498 and BH512 it disappears (p = 0.425).
  deviations:
  - Anesthetized units from two rats; awake units from seven.
- claim: fig5bd-fsu-time-locked-no-prf
  outcome: not_reproduced
  notebook: reproduce_ramachandran_2025.ipynb
  output: claim:fig5bd-fsu-time-locked-no-prf
  notes: By the paper's test FSU time-locked responses differ across PRF in both states,
    Kruskal-Wallis p = 1.8e-12 awake and 5.5e-04 anesthetized (W1 Rep1), with 4 to 6 significant
    post hoc pairs awake and 2 or 3 anesthetized under every reading. The effects are small;
    group medians span 98.7 to 103.4% awake and 99.8 to 103.9% anesthetized, and the awake 3000 Hz
    mean is 106.8%. G2 (with sham) cannot be run. The anesthetized groups come from two rats.
- claim: fig5e-rsu-delayed-prf-awake
  outcome: not_reproduced
  notebook: reproduce_ramachandran_2025.ipynb
  output: claim:fig5e-rsu-delayed-prf-awake
  notes: PRF is a significant factor (p = 6e-20 Rep1, 4.5e-15 Rep2, 5.1e-15 Rep3) but the two
    highest means are 1500 and 30 Hz (106.7 and 106.6% Rep1), and 3000 Hz (102.3 to 103.3%) is
    below 30 Hz (corrected p < 1e-4); part (2) fails under both of its readings and every repeat
    reading. Part (3) needs the sham and was not tested.
- claim: fig5f-fsu-delayed-prf-awake
  outcome: not_reproduced
  notebook: reproduce_ramachandran_2025.ipynb
  output: claim:fig5f-fsu-delayed-prf-awake
  notes: PRF is a significant factor (p = 4.6e-12 Rep1) and 30 Hz differs from 1500, 3000 and 4500
    Hz (part 3, tested without direction as the criterion says "differs"), but the strongest mean
    is at 30 Hz (103.5%, 4500 Hz 100.3 to 100.4%), the opposite of the paper's pattern, and 300 Hz
    does not differ from 4500 Hz (corrected p = 1.0), under every repeat reading. Part (5) needs
    the sham and was not tested; even if it held, part (1) with two others falls short of the
    three the partial outcome needs.
- claim: fig5gh-delayed-prf-anesth
  outcome: not_reproduced
  notebook: reproduce_ramachandran_2025.ipynb
  output: claim:fig5gh-delayed-prf-anesth
  notes: PRF is not a significant factor for anesthetized delayed responses, Kruskal-Wallis p =
    0.16 (W1) and 0.12 (W2) for RSU, 0.16 and 0.18 for FSU. The higher PRFs have the higher pooled
    mean by under one point (RSU 99.97 against 99.15%, FSU 99.87 against 99.35%). Every rat and
    PRF mean is within 98.5 to 100.9%, and the 30 Hz group is BH498 alone.
  deviations:
  - Two labelled rats where the paper had ten.
- claim: delayed-anesthesia-factor
  outcome: reproduced
  assumed: true
  notebook: reproduce_ramachandran_2025.ipynb
  output: claim:delayed-anesthesia-factor
  notes: With one recording per rat and condition, either without the `_2` recordings (Rep2) or
    with the earliest of each pair (Rep3), anesthesia is a factor for RSU at p = 4.2e-09 to
    1.8e-08 and for FSU at p = 0.0012 to 0.0015 under A1/A2 and W1/W2, and the anesthetized mean
    is lower in both (RSU 99.7 against 104.3 to 104.6%, FSU 99.7 against 101.2 to 101.3%). With
    every recording (Rep1) RSU holds (p = 3.6e-06 to 4.3e-06) but FSU gives p = 0.038 to 0.041,
    which misses the 0.01 bound; that reading gives partially reproduced. Leaving out the
    recording filed under both BH498 and BH508 gives FSU p = 0.0016 to 0.0019 under Rep2 and Rep3.
    The anesthetized units come from two rats, so the state effect may also be a rat effect. The
    question is recorded for the paper's authors.
  deviations:
  - Assumed that the paper's analysis used one recording per rat and condition. Methods 2.3
    describes one recording per parameter set per rat ("Recordings for a single rat for each set
    of parameters were completed on the same day"), the paper mentions no repeats, and the
    dandiset's description says "Some subjects have duplicate recordings taken a few months after
    the original ones". Which recording of a pair is the original is open, as three `_2`
    recordings are earlier than their pair; both choices (Rep2, Rep3) give the same outcome.
  - Anesthetized units from two rats.
- claim: fig6ad-time-adjacent-batch
  outcome: blocked
  blocked_by: data_missing
  notes: The second batch of five rats recorded awake and anesthetized in the same week, with a
    sham, is not in the dandiset. Its ten subject folders hold eight rats named in the
    identifiers, all of which have recordings of the first batch's series, and no file is from a
    two-PRF or sham protocol. The session dates show no rat recorded awake and anesthetized within
    a week at two PRFs only; BH498's awake recordings (5 and 6 March 2024) precede its
    anesthetized ones (10 March) by four to five days, but at all five PRFs and without a sham.
- claim: fig6ef-rsu-ispta-rise-then-fall
  outcome: blocked
  blocked_by: methods_underspecified
  notebook: reproduce_ramachandran_2025.ipynb
  output: claim:fig6ef-rsu-ispta-rise-then-fall
  notes: The delayed means do not rise to their peak under any reading (106.6% at 30 Hz, 101.2 to
    102.8% at 300 Hz, 106.7 to 108.8% at 1500 Hz), so at best the claim is partially reproduced,
    on the time-locked window. Time-locked RSU means rise from 30 Hz (96.4 to 96.8%) to a peak at
    3000 Hz (60.26 mW/cm2, 107.7 to 108.7%) and fall at 4500 Hz (98.0 to 99.5%) under W2 with every
    repeat reading and under W1 with Rep1 and Rep3, but under W1 Rep2 the 300 Hz mean (98.2%) is
    0.1 point above the 1500 Hz mean (98.1%, SEMs 1.1 and 1.3). With one recording per rat and
    condition the claims file's readings W1 and W2 thus disagree under Rep2, and its header
    blocks a claim whose readings disagree. How a window off the bin edges was measured is asked
    of the paper's authors.
- claim: fig6fh-fsu-ispta
  outcome: not_reproduced
  notebook: reproduce_ramachandran_2025.ipynb
  output: claim:fig6fh-fsu-ispta
  notes: The time-locked part fails (fig5bd, awake Kruskal-Wallis p = 1.8e-12). Delayed FSU means
    are 103.5, 98.7, 101.8, 100.6 and 100.3% from 30 to 4500 Hz (Spearman rho = -0.4, Pearson r =
    -0.27, Rep1; rho = -0.3 Rep2 and Rep3).
- claim: fig5a-1500-highest-time-locked-mean
  outcome: not_reproduced
  notebook: reproduce_ramachandran_2025.ipynb
  output: claim:fig5a-1500-highest-time-locked-mean
  notes: The highest mean is at 3000 Hz under every reading (107.7 to 108.7%), significantly above
    1500 Hz (98.1 to 98.7%; corrected p = 0.0040 or less).
- claim: fig7a-rsu-time-locked-dc
  outcome: not_reproduced
  notebook: reproduce_ramachandran_2025.ipynb
  output: claim:fig7a-rsu-time-locked-dc
  notes: Part (2) does not need the 30% group and fails under every reading, as 6% is the highest
    group (180.8%; 60% 147.5%) and does not differ from 60% (corrected p = 1.0; 0.67 to 0.91
    without a 30% group). Parts (3) and (4) need the sham or the paper's 30% recordings and were
    not tested; without a 30% group the Kruskal-Wallis is not significant, so the claim cannot be
    reproduced whatever those parts would show. The substitute 30% groups are far below both
    (90.4 to 98.7%). The 6% and 60% responses are largest in BH506 (249.0 and 209.9%); BH521 and
    BH526 give 113 to 121%.
  deviations:
  - The dandiset has no 30% DC recording of its own. The substitutes (C1, the PRF series' 1500 Hz,
    200 us recordings of BH506 and BH526; C2, those of every rat, with each repeat reading) and C0,
    no 30% group, are shown; a part that needs the 30% group is treated as data missing.
  - The 6% and 60% recordings come from three rats where the paper had ten.
- claim: fig7a-60-highest-time-locked-mean
  outcome: not_reproduced
  notebook: reproduce_ramachandran_2025.ipynb
  output: claim:fig7a-60-highest-time-locked-mean
  notes: The highest mean is at 6% under every reading (176.3 to 180.8%; 60% 147.1 to 147.5%), which
    does not need the 30% group. With the substitute 30% groups, 60% is significantly above 30%
    (corrected p < 1e-16).
  deviations:
  - The 30% group is a substitute (C1 or C2) or absent (C0), as for fig7a.
- claim: fig7b-fsu-time-locked-dc
  outcome: not_reproduced
  notebook: reproduce_ramachandran_2025.ipynb
  output: claim:fig7b-fsu-time-locked-dc
  notes: FSU time-locked responses differ across DC under every reading, and the 6% against 60%
    difference does not need the 30% group (Kruskal-Wallis p = 0.0054 without it; p = 3.5e-12 or
    smaller with a substitute, all three pairs significant). FSU respond strongly at 6% and 60%
    (means 156.8 and 205.3%, medians 115.0 and 128.6%) and not at the substitute 30% (median
    100.8%), most in BH506 (338.6 and 403.3%).
  deviations:
  - The 30% group is a substitute (C1 or C2) or absent (C0), as for fig7a.
- claim: fig7c-rsu-delayed-dc
  outcome: blocked
  blocked_by: data_missing
  notebook: reproduce_ramachandran_2025.ipynb
  output: claim:fig7c-rsu-delayed-dc
  notes: Part (2), 30% above 6% and 60%, needs the paper's 30% DC recordings, which are not in the
    dandiset, and the substitutes decide it. With the same rats' 1500 Hz, 200 us recordings (C1)
    the Kruskal-Wallis is not significant (p = 0.21) and no pair differs; with every such
    recording (C2) the effect is significant (p = 2.2e-04 Rep1, 3.7e-05 Rep2, 1.9e-04 Rep3) and
    30% is above 6% and 60%. Part (4), 6% against 60%, also depends on the 30% group through the
    Bonferroni family; 6% is below 60% at p = 0.024 alone and at corrected p = 0.071 over three
    pairs. Part (3) needs the sham. The substitute recordings were made three to five months
    before the DC recordings.
  deviations:
  - The 30% group is a substitute (C1 or C2) or absent (C0), as for fig7a.
- claim: fig7d-fsu-delayed-dc
  outcome: partially_reproduced
  notebook: reproduce_ramachandran_2025.ipynb
  output: claim:fig7d-fsu-delayed-dc
  notes: Parts (1) and (2) hold under every reading, without a 30% group included, so they do not
    depend on the substitute; the Kruskal-Wallis is significant (p = 0.0051 without a 30% group,
    0.011 C1, 4.5e-07 to 1.4e-06 C2) and 60% is above 6% (p = 0.0051 alone, corrected p = 0.015
    over three pairs). Part (3), 6% against sham, cannot be tested, so the claim is partially
    reproduced, the outcome the criterion gives when (1) and (2) hold without (3). The difference
    is small and both groups are below baseline (99.6% and 98.2%).
  deviations:
  - No sham recording; part (3) is reported as not tested.
  - The 30% group is a substitute (C1 or C2) or absent (C0); it enters only the Kruskal-Wallis.
- claim: sham-no-auditory-response
  outcome: blocked
  blocked_by: methods_underspecified
  notes: The criterion blocks the claim, as the paper names no test of the sham against baseline.
    The dandiset also holds no sham recording, so the sham's responses cannot be shown either.
findings:
- kind: data_missing
  statement: The sham condition and the second batch of five rats (awake and anesthetized
    recordings in the same week at a low PRF and 1500 Hz) are not in the dandiset. Four claims
    cannot be tested, and every comparison with sham in the others is left out.
- kind: data_missing
  statement: Only part of the first batch is here. The awake PRF series covers seven rats, the
    anesthetized PRF series three (BH498 at five PRFs, BH512 without 30 Hz, BH521 at three PRFs,
    unlabelled), and the awake DC series three rats at 6% and 60% only. The DC series' own 30%
    recordings are missing; the only 1500 Hz, 200 us recordings are the PRF series', made three to
    five months earlier, and the claim on 30% DC delayed responses cannot be tested without them.
    The paper describes ten rats for each series.
- kind: data_missing
  statement: The files hold no waveforms, voltage traces or electrode positions, so the cell-type
    sorting (k-means on the initial phase and after-hyperpolarization durations) cannot be
    repeated or checked.
- kind: metadata_error
  statement: Twelve files are second copies of other recordings. The five anesthetized BH498
    recordings are deposited under BH498 without labels and under subject folder BH497 with
    labels; four anesthetized BH512 recordings under BH512 without labels and under BH514 with
    labels; BH512_1500_200_anes2 is a third copy of the BH512 1500 Hz anesthetized recording,
    sorted differently and dated two months later. Trial times, per-unit spike counts and first
    spike times are identical within each pair. The identifiers name BH498 and BH512.
- kind: metadata_error
  statement: BH498_30_200 (sub-BH498) and BH508_30_200_2 (sub-BH508) share all 203 trial times
    and 18,860 spike times; they are one recording sorted twice and filed under two rats, with
    session start times 6.5 hours apart (6 March 2024 17.58 and 7 March 00.23). Which rat it
    belongs to cannot be established from the files.
- kind: metadata_error
  statement: The dandiset's description says the repeat recordings were "taken a few months after
    the original ones", but three of the ten `_2` recordings start before their unsuffixed pair
    (BH498_1500_200_2 and BH498_4500_200_2 one day before, BH508_1500_200_2 two months before), so
    the suffix does not mark which recording is the repeat.
- kind: metadata_error
  statement: The labelled copies of anesthetized recordings (sub-BH497, sub-BH514) are described
    as "Awake S1 Stimulation by tFUS". Every file gives the age P24W, where the paper gives 7, 9
    and 10 months for the three series and the dandiset's description 8 to 10 and 12 months.
    Electrode columns carry placeholder descriptions ("my description") and the location "brain
    area".
- kind: metadata_insufficient
  statement: The PRF, tone-burst duration and anesthesia state of a recording are coded only in
    the file's identifier. The trial table's stop_time (always 2.2 s after start_time) is not
    described, and the files do not say which trials of the 505 delivered the 500 are.
- kind: metadata_insufficient
  statement: Fifteen anesthetized files have no cell-type labels, among them all of BH521's and
    BH512's DC recordings, which cannot enter any cell-type analysis.
- kind: other
  statement: Five recordings hold fewer than the 500 trials the Methods and the dandiset's
    description give (203, 238, 328 and 339 trials, all from BH508 or the BH498/BH508 duplicate).
- kind: methods_unavailable
  statement: Were the repeat recordings (BH498, BH506, BH508) part of the paper's analysis, and if
    not, which recording of each pair was? Methods 2.3 describes one recording per parameter set
    per rat. The FSU part of delayed-anesthesia-factor depends on it (p = 0.0012 to 0.0015 with one
    recording per condition, 0.038 to 0.041 with all), and fig6ef-rsu-ispta-rise-then-fall depends
    on which recording of a pair is kept. This attempt assumed one recording per rat and condition.
- kind: methods_unavailable
  statement: Was a response window that does not fall on the 35.7 ms bin edges (0 to 67 ms, 0.2
    to 0.7 s) measured from exact spike times or from the PSTH bins that overlap it? The two give
    different results for fig6ef-rsu-ispta-rise-then-fall, which is blocked until this is known.
- kind: methods_unavailable
  statement: For the delayed-response latency, is the first bin allowed after the 67 ms of
    ultrasound the first bin starting at or after 67 ms, or the first ending after it? The two give
    different results for fig4h-awake-latency-wider, which is blocked until this is known.
EOF
cat $TMPDIR/head.yaml $TMPDIR/body.yaml > attempts/000945-ramachandran-2025-01.yaml; grep -n ": .*: " attempts/000945-ramachandran-2025-01.yaml | grep -v "^\s*[0-9]*:\s*-\? *[a-z_]*: \"" | head
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  sed -i 's/Under every reading the SDs are within 0.04 s of each other/Under every reading the SDs are within 0.03 s of each other/' entries/000945-ramachandran-2025/reproduce_ramachandran_2025.ipynb; grep -c "within 0.03 s of each other" entries/000945-ramachandran-2025/reproduce_ramachandran_2025.ipynb; python3 -c "import yaml;yaml.safe_load(open('attempts/000945-ramachandran-2025-01.yaml'))" && echo ok
```

```
1
ok
```

**Agent**

Now the verification round record.

**Agent calls Bash**

```bash
cd  cat >> attempts/000945-ramachandran-2025-01.yaml <<'EOF'
verifications:
- date: 2026-10-31
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the
    notebook)
  reviewed: The handover of the first run, the executed notebook with the conclusions and summary
    removed, the helper module and the claims file, with the paper under paper/. The verifier also
    checked the archive's asset list.
  results:
  - claim: fig3-cell-type-sorting
    agrees: false
    outcome: blocked
    reason: The files hold no waveforms, so the k-means features and the cluster separation the
      criterion requires cannot be computed. Using the deposited labels, 2 of 59 recordings fall
      within the count tolerances; this is weak evidence, since recording totals run from 31 to
      127 units. One of the two, BH508_4500_200_2, is a 12-month repeat that Rep2 would drop, and
      no base rate is given for a match among 59 recordings.
    response: Changed to blocked (data_missing), as both outcomes of the criterion require the
      cluster separation. Added the counts under Rep2 and Rep3 (only BH527_30_200 matches) and a
      base rate (a binomial model expects 3.84 matching recordings, against 2 observed). The other
      claims stay tested, as they use the K0 labels the claims file's header provides for and not
      the waveform features; this is recorded as a deviation.
  - claim: fig4-rsu-time-locked-both-states
    agrees: true
    outcome: blocked
    reason: There is no sham. The awake half already fails the criterion's "above 100%" condition,
      as the awake 1500 Hz RSU mean is 98.1 to 98.7% under every reading, so the best this claim
      could reach is partially reproduced. The notebook does not say this.
    response: Added a result cell and notes saying that the awake half fails and the claim could at
      best be partially reproduced.
  - claim: fig4hi-fsu-delayed-latency
    agrees: true
    outcome: not_reproduced
    reason: No reading gives p < 0.001; p runs from 0.018 to 0.85. The anesthetized mean is 0.38 to
      0.52 s against an expected 0.24 +- 0.08 under every reading. Under S1, 86% of FSU count as
      responders and latencies spread over 0.07 to 1.39 s in both states, which follows from the
      claims file's readings, not a coding error.
    response: Kept. Added Rep3 (p now 0.018 to 0.92 over 24 readings) and the responder share and
      latency spread to the conclusion and notes.
  - claim: fig4h-awake-latency-wider
    agrees: false
    outcome: blocked
    reason: Awake SD > anesthetized SD under D1 but not under D2, and the claims header blocks a
      claim when its readings disagree. Every SD is about 0.37 to 0.41 s, with no contrast like the
      paper's 0.14 vs 0.08. The notebook overrides the claims file's rule for disagreeing readings.
    response: Changed to blocked (methods_underspecified), following the claims file's header, and
      added a methods_unavailable finding asking which first bin the paper allowed.
  - claim: fig5a-rsu-time-locked-prf-awake
    agrees: true
    outcome: not_reproduced
    reason: Part (1) holds. Parts (3) and (4) fail under every reading, and (2) fails in 3 of 4. The
      3000 Hz mean is the highest and differs from 1500 and 4500 Hz. Even if the sham parts held,
      the partial threshold could not be met.
    response: Kept. Said in the conclusion that the partial threshold cannot be met even with the
      sham parts, and stated that no claim with an untested sham part is judged reproduced.
  - claim: fig5c-rsu-time-locked-prf-anesth
    agrees: true
    outcome: not_reproduced
    reason: Parts (1) and (7) hold; (2), (3) and (4) fail under W1 and W2. Only two labelled rats are
      available; the 30 Hz anesthetized group is one rat's 32 units, so PRF effects are confounded
      with rat, which the notebook does not discuss.
    response: Kept. Added the rat confound and the partial threshold to the conclusion and notes.
  - claim: rsu-time-locked-anesthesia-factor
    agrees: true
    outcome: not_reproduced
    reason: p for the anesthesia effect is 0.011 to 0.018, but the effect goes the wrong way,
      anesthetized 102.6 to 102.9% vs awake 100.1 to 100.4%. In the two-rat ANOVA variant the
      anesthesia effect disappears (p = 0.43); the notebook shows this but does not discuss it.
    response: Kept. Added Rep3 (p down to 0.0083, still the wrong direction) and discussed the
      two-rat confound in the conclusion and notes.
  - claim: fig5bd-fsu-time-locked-no-prf
    agrees: true
    outcome: not_reproduced
    reason: The Kruskal-Wallis is significant in both states (awake p about 1.8e-12; anesthetized p =
      5.5e-4 and 7.8e-4), with 2 to 6 significant post hoc pairs.
    response: Kept; Rep3 added (4 significant pairs awake).
  - claim: fig5e-rsu-delayed-prf-awake
    agrees: true
    outcome: not_reproduced
    reason: Part (1) holds. Part (2) fails under both its readings, R1 and R2; 30 Hz has about the
      same mean as 1500 Hz and is above 3000 Hz.
    response: Kept; Rep3 added, with the same result.
  - claim: fig5f-fsu-delayed-prf-awake
    agrees: true
    outcome: not_reproduced
    reason: Part (2) fails (30 Hz has the highest mean, not 4500 Hz) and (4) fails. Only (1) and (3)
      hold, so the partial threshold cannot be reached even with the sham part. Part (3) is tested
      without direction, which matches the criterion's word "differs", but the 30 Hz FSU mean is
      the highest, opposite to the paper's pattern.
    response: Kept. Said in the conclusion that part (3) holds only without direction, against the
      paper's pattern, and that the partial threshold cannot be met.
  - claim: fig5gh-delayed-prf-anesth
    agrees: true
    outcome: not_reproduced
    reason: The Kruskal-Wallis is not significant for RSU or FSU under either window (p = 0.12 to
      0.18).
    response: Kept; added the two-rat caveat.
  - claim: delayed-anesthesia-factor
    agrees: true
    outcome: reproduced
    reason: Under Rep2, RSU p about 5e-9 and FSU p = 0.0013 to 0.0015, with anesthetized below awake
      for both types, under A1/A2 and W1/W2. Under Rep1 the FSU p is about 0.04, which would make
      it partial. Rep2 is better supported than the notebook argues, by the dandiset description,
      but the notebook never prints which date belongs to which identifier, so it is unverified
      that the `_2` files are the later recordings.
    response: Kept. The notebook now prints the description and every file's start time. Three `_2`
      recordings are earlier than their pair, so a third reading, Rep3, keeps the earliest of each
      pair; it gives the same outcome (FSU p = 0.0012 to 0.0015). The assumption is restated as one
      recording per rat and condition, and a variant without the recording filed under two rats
      is shown (FSU p = 0.0016 to 0.0019). The finding on the suffix is added.
  - claim: fig6ad-time-adjacent-batch
    agrees: true
    outcome: blocked
    reason: Checked on the archive, 75 assets, two kinds of session description, no sham and no
      two-PRF series. All 10 subject folders are first-batch rats or duplicate folders.
    response: Kept. The session dates are now printed; the notes say that BH498's awake and
      anesthetized recordings are four to five days apart but at all five PRFs and without a sham,
      so they are not a proxy for the second batch.
  - claim: fig6ef-rsu-ispta-rise-then-fall
    agrees: false
    outcome: blocked
    reason: The delayed window fails under every reading; 30 Hz (106.6) is above 300 Hz (101.2). The
      time-locked window holds under W2 but fails under W1 Rep2 by 0.1% (98.2 vs 98.1), so the
      window readings disagree. At best it is partial.
    response: Changed to blocked (methods_underspecified), following the claims file's header. Under
      Rep3 W1 and W2 agree, but under Rep2 they do not, and the two one-recording readings cannot be
      told apart, so the disagreement stands.
  - claim: fig6fh-fsu-ispta
    agrees: true
    outcome: not_reproduced
    reason: Spearman rho is -0.4 (Rep1) and -0.3 (Rep2) against a required 1. The time-locked part
      inherits fig5bd's failure.
    response: Kept; Rep3 added (rho = -0.3).
  - claim: fig5a-1500-highest-time-locked-mean
    agrees: true
    outcome: not_reproduced
    reason: 3000 Hz has the highest mean under every reading, and 1500 vs 3000 Hz has corrected p <=
      0.004.
    response: Kept; Rep3 added, with the same result.
  - claim: fig7a-rsu-time-locked-dc
    agrees: true
    outcome: not_reproduced
    reason: Parts (2) and (4) fail under every reading; the 6% mean (176 to 181%) is above 60% (147%)
      and above 30%. Part (2) does not involve the substituted 30% condition.
    response: Kept. Added C0, without a 30% group, and said that part (2) decides without the
      substitute; part (4) is now treated as data missing.
  - claim: fig7a-60-highest-time-locked-mean
    agrees: true
    outcome: not_reproduced
    reason: 6% has the highest mean under every reading.
    response: Kept; C0 added, with the same result.
  - claim: fig7b-fsu-time-locked-dc
    agrees: true
    outcome: not_reproduced
    reason: Kruskal-Wallis p <= 3.5e-12 and all 3 pairs are significant, including 6% vs 60%, which
      does not use the 30% substitute.
    response: Kept; C0 added (p = 0.0054 without a 30% group).
  - claim: fig7c-rsu-delayed-dc
    agrees: false
    outcome: blocked
    reason: The paper's own 30% DC recordings are not in the dandiset. The substitute 30% condition
      decides the outcome; C1 is not reproduced (KW p = 0.21) and C2 is partial. Part (4), 6% vs
      60%, fails under every reading (corrected p = 0.071). The notebook adopts C1 by its own
      choice, where the honest outcome for 30%-dependent parts is data_missing.
    response: Changed to blocked (data_missing). C1 and C2 are kept as substitutes that decide no
      outcome, and C0 shows that part (4) also depends on the 30% group through the Bonferroni
      family (p = 0.024 alone). The recording dates of the DC and substitute files are printed.
  - claim: fig7d-fsu-delayed-dc
    agrees: false
    outcome: partially_reproduced
    reason: Parts (1) and (2) hold under every reading (6% vs 60% corrected p = 0.015). Part (3), the
      sham comparison, cannot be tested, and a criterion with an untested part should not reach
      "reproduced"; the header only covers a missing anesthetized sham. The effect is tiny, 98.2%
      vs 99.6%, both below baseline.
    response: Changed to partially reproduced, the criterion's outcome when (1) and (2) hold without
      (3). Added C0, under which (1) and (2) also hold.
  - claim: sham-no-auditory-response
    agrees: true
    outcome: blocked
    reason: The criterion blocks this claim, and the archive holds no sham recording.
    response: Kept.
EOF
python tools/entry.py check entries/000945-ramachandran-2025 2>&1 | tail -15
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd entries/000945-ramachandran-2025; cat README.md; cat entry.yaml
```

```
# Ramachandran, Gao, Yttri, Yu & He (2025) from dandiset 000945

Tests the findings of [Ramachandran et al. (2025)](https://doi.org/10.1088/1741-2552/adbb1f) on
[DANDI:000945](https://dandiarchive.org/dandiset/000945/0.250213.2212), the version the paper
cites. The dandiset holds the sorted units and trial times of awake and anesthetized recordings in
rat S1 during transcranial focused ultrasound at five pulse repetition frequencies (PRF) and three
duty cycles (DC), with a cell-type label (RSU or FSU) in most files.

| Claim | Outcome |
|---|---|
| Units sort into 28 FSU and 32 RSU in one animal (Figure 3B) | Partially reproduced |
| RSU respond during stimulation in both states, against sham (Figure 4) | Blocked: data missing |
| FSU delayed onsets are later awake than anesthetized (Figure 4H, 4I) | Not reproduced |
| Awake onset latencies are more spread (Figure 4H) | Not reproduced |
| Awake RSU time-locked responses by PRF (Figure 5A) | Not reproduced |
| Anesthetized RSU time-locked responses by PRF (Figure 5C) | Not reproduced |
| Anesthesia lowers RSU time-locked responses (two-way ANOVA) | Not reproduced |
| FSU time-locked responses do not depend on PRF (Figure 5B, 5D) | Not reproduced |
| Awake RSU delayed responses peak at 1500 and 3000 Hz (Figure 5E) | Not reproduced |
| Awake FSU delayed responses peak at 4500 Hz (Figure 5F) | Not reproduced |
[... 49 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000945-ramachandran-2025; python3 - <<'EOF'
p='README.md'; s=open(p).read()
for a,b in [
 ('| Units sort into 28 FSU and 32 RSU in one animal (Figure 3B) | Partially reproduced |','| Units sort into 28 FSU and 32 RSU in one animal (Figure 3B) | Blocked: data missing (no waveforms) |'),
 ('| Awake onset latencies are more spread (Figure 4H) | Not reproduced |','| Awake onset latencies are more spread (Figure 4H) | Blocked: methods underspecified |'),
 ('| RSU responses rise with ISPTA, then fall (Figure 6E, 6G) | Partially reproduced, on an assumption |','| RSU responses rise with ISPTA, then fall (Figure 6E, 6G) | Blocked: methods underspecified |'),
 ('| RSU delayed responses prefer 30% DC (Figure 7C) | Not reproduced, on an assumption |','| RSU delayed responses prefer 30% DC (Figure 7C) | Blocked: data missing (no 30% DC recordings) |'),
 ('| FSU delayed responses higher at 60% than 6% DC (Figure 7D) | Reproduced |','| FSU delayed responses higher at 60% than 6% DC (Figure 7D) | Partially reproduced (sham part untested) |'),
 ('and no waveforms. Twelve files are second copies of other recordings.','no 30% DC recordings and no waveforms. Twelve files are second copies of other recordings, and\nthe `_2` suffix of the repeat recordings does not always mark the later one.')]:
    assert s.count(a)==1, a
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
date -u
```

```
Sat Oct 31 22:30:58 UTC 2026
```

**Agent calls Bash**

```bash
cd  python tools/entry.py all entries/000945-ramachandran-2025 2>&1 | tail -3; git status --short
```

```
Installed kernelspec registry-000945-ramachandran-2025 in executed/000945-ramachandran-2025/.venv/share/jupyter/kernels/registry-000945-ramachandran-2025
0 error(s)
pass  reproduce_ramachandran_2025.ipynb  (92 s)
 M attempts/000945-ramachandran-2025-01.yaml
 M entries/000945-ramachandran-2025/README.md
 M entries/000945-ramachandran-2025/reproduce_ramachandran_2025.ipynb
 M entries/000945-ramachandran-2025/tfus.py
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
?? scripts
```

**Agent calls Bash**

```bash
cd  ls -la .bash_profile .bashrc .gitconfig .mcp.json .profile .ripgreprc .zprofile .zshrc scripts .idea .vscode 2>&1 | head -20
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 31 22:11 .bash_profile
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 31 22:11 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 31 22:11 .gitconfig
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 31 22:11 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 31 22:11 .mcp.json
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 31 22:11 .profile
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 31 22:11 .ripgreprc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 31 22:11 .vscode
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 31 22:11 .zprofile
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 31 22:11 .zshrc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 31 22:11 scripts
```

**Agent**

I've revised the attempt after round 1. The entry re-ran cleanly with `tools/entry.py all` (0 check errors, notebook passes in 92 s), and every conclusion now matches the new numbers.

**Outcome changes (all five agree with the verifier)**
- **fig3-cell-type-sorting**: partially reproduced → blocked (data_missing). Both outcomes the criterion allows require the clusters to separate on waveform features, and the files hold no waveforms. The match on unit counts is also no better than chance: a simple binomial model expects 3.84 matching recordings, and 2 were found. The other claims depend on fig3 but stay tested, because they use the dataset's own cell-type labels, which the claims header allows. I recorded this as a deviation, since the protocol would normally block every claim that depends on a blocked one.
- **fig4h-awake-latency-wider**: not reproduced → blocked (methods_underspecified). Two readings of the claims file (D1/D2, which bin the latency may start in) give different results, and the claims header blocks a claim in that case. I had been overriding that rule; I now follow it.
- **fig6ef-rsu-ispta-rise-then-fall**: partially reproduced → blocked (methods_underspecified). The two window readings (W1/W2) disagree when the repeat recordings are left out.
- **fig7c-rsu-delayed-dc**: not reproduced → blocked (data_missing). The paper's own 30% duty-cycle recordings are missing. The stand-ins borrowed from other sessions now decide no outcome.
- **fig7d-fsu-delayed-dc**: reproduced → partially reproduced. The sham part cannot be tested, and no claim with an untested sham part is judged reproduced any more.

The other 17 outcomes are unchanged, including delayed-anesthesia-factor, which stays reproduced on an assumption.

**Added or corrected**
- **Recording dates.** The notebook now prints the dandiset description and every file's start time. Three of the ten `_2` repeat files start *before* their unsuffixed pair, so the suffix does not mark the later recording. I added a third repeat reading, Rep3, which keeps the earliest recording of each pair.
- **delayed-anesthesia-factor.** Rep3 gives the same outcome as leaving the `_2` files out (FSU p = 0.0012 to 0.0015). Dropping the recording filed under two rats doesn't change it either. The assumption is restated as one recording per rat and condition.
- **Duty-cycle claims.** A new reading, C0, runs the tests with no 30% group at all. It shows that fig7a, fig7a-60 and fig7b fail on parts that don't need the 30% group, and that fig7d's parts (1) and (2) hold without it. The recording dates of the duty-cycle files and of the borrowed 30% files are printed.
- **Smaller points.**
  - fig4-rsu: notes that the awake half already fails (mean below 100%).
  - Two-rat confound: discussed for the anesthetized claims.
  - Latency rule: notes that it flags 86% of FSU.
  - fig5f: notes that part (3) only holds without direction.
  - Partial thresholds: notes where they cannot be met even if the sham parts held.
  - Time-locked responses: a caveat that most 200 us recordings show none.
- **Helper fix.** `tfus.py` now decodes start times that are stored as arrays; the unlabelled anesthetized files store them that way.
- **Record.** New findings: the `_2` suffix contradicts the dandiset description; the duplicated recording's start times are 6.5 hours apart; and a question for the paper's authors about the latency start bin. The 30% duty-cycle question became a data_missing finding. The round is recorded under `verifications` (17 claims agreed, 5 disagreed and were changed).
- **README.** Updated to match.

**Not done**
- I added no reader questions, because the verifier reported no misreading of the paper by the claims file.
- Three things can't be checked from the files, and the notebook says so: whether the 500 trials are trials 6 to 505, whether the labels are the paper's k-means output, and which rat the doubly filed recording belongs to.
- Nothing is committed, as instructed.

## End of run

48 turns, 17 minutes, result: success.
