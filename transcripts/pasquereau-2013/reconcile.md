# pasquereau-2013 · reconcile · run 45891832245

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; grep -n "^#" docs/protocol.md | head -80
```

```
Thu Nov 26 20:39:58 UTC 2026
1:# Protocol for an attempt
43:## Reader
45:### 1. Get the paper
59:### 2. Read the paper's code
69:### 3. Write the claims file
165:### 4. Data from outside the paper's own recordings
173:### 5. Check
186:### 6. Answer questions
199:## Author
215:### 1. Establish what can be tested
374:### 2. Check the data against its description
397:### 3. Write the entry
482:### 4. Lock, check and run
502:### 5. Record the attempt
633:### 6. Hand over for verification
671:## Repeat attempts
737:## Local and remote datasets
760:## Verifier
764:### Round 1: without the author's conclusions
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 671,760p docs/protocol.md; sed -n 502,633p docs/protocol.md
```

```
## Repeat attempts

When a dataset changes after an attempt, for example after its owners fix
what an attempt found, or when the protocol changes, a new attempt tests the
dataset again. It is made blind: it is an attempt in its own right, not a
check of the one before it.

- **Blind.** The author's runs (author, author-answers and each
  author-revise) see no earlier attempt on the dataset: not its record, entry,
  questions, transcripts or notes, and not the repository's history.
  `tools/blind.sh` takes them out of the checkout before each run and puts
  them back after it, and the run may not fetch the registry's website. The
  author keeps the claims file, unless the earlier attempt is deprecated and
  a reader wrote it again, and writes a new entry under the same name, a new
  notebook from scratch, and the record under the next number (`-02`). The
  verifiers see only this attempt, as always. Each finding is recorded as the
  attempt found it, with nothing about earlier attempts in its statement.
- **Reconcile.** Once the attempt is verified, a separate run, `reconcile`
  (`docs/agents/reconcile.md`), compares it with the attempt before it and
  writes a `reconciliation` block in the new record. It first checks, with
[... 202 more lines not kept]
```

**Agent calls Bash**

```bash
cat docs/agents/reconcile.md 2>/dev/null | head -150; ls attempts | grep pasq; ls entries/pasquereau-2013 earlier-entry
```

```
You reconcile a repeat attempt in the reproduction registry, checked out in the current directory. Read docs/protocol.md, "Repeat attempts", first. Attempt `{attempt}` on paper `{key}` (data: {dataset}; entry `entries/{entry}`, dataset version {version}) was made blind: its author did not see `{earlier}` (made on version {earlier_version}). Its record is `attempts/{earlier}.yaml`. Its entry is `entries/{earlier_entry}` as it was when that record was last changed: `c=$(git log -1 --format=%H -- attempts/{earlier}.yaml)`, then `git show $c:entries/{earlier_entry}/<file>`. Both have been through their verification rounds. Your job is to say how the two compare, in a `reconciliation` block of `attempts/{attempt}.yaml` (its schema is in `schemas/attempt.schema.json`). Do not change the outcomes, statements or notes that the blind attempt recorded, its claims file or its notebooks.

1. Run `tools/blind.sh audit {folder}`. It prints the lines of this attempt's author transcripts that point at an earlier attempt. Read each in context. Set `blind: true` if the author never saw an earlier attempt's results, else `blind: false` with what it saw under `blind_note`.
2. For each finding of `{earlier}`, in order (`finding` is its number, from 1), decide whether one of `{attempt}`'s findings reports the same problem: the same files, fields or values, not only the same kind. If so, set `status` to `still_present` or `partly_fixed`, and `now` to that finding's number in `{attempt}`. If not, check the earlier finding directly on version {version}, in a new notebook `entries/{entry}/earlier_findings.ipynb` (add it to `entry.yaml`, one short section per finding, each opening with the earlier statement, and lock, check and run the entry). Then:
   - `fixed`, when the check shows the problem is gone;
   - `still_present`, when it is still there: add it to `{attempt}`'s findings with `found: on_prompt` and a statement in the protocol's usual style, and point `now` at it;
   - `not_checked`
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
tools/blind.sh audit pasquereau-2013 2>&1 | head -100
```

```
transcripts/pasquereau-2013/author.md:52:9	([pilot notes](https://github.com/encorescience/encore-registry/blob/main/docs/pilot-notes.md)); the reasons for the rules are there.
transcripts/pasquereau-2013/author.md:108:Encore Science checks datasets against the papers they came from. This repository holds its public record, the Encore registry, served at <https://encorescience.org>. The protocol the checks follow, and the `encore` command that runs the same check on your own data, are in [encore-protocol](https://github.com/encorescience/encore-protocol). It is developed by [CatalystNeuro](https://www.catalystneuro.com).
transcripts/pasquereau-2013/author.md:121:**Site:** <https://encorescience.org/>, with the registry's dashboard at <https://encorescience.org/registry/> and what Encore offers a journal at <https://encorescience.org/journals/>.
transcripts/pasquereau-2013/author.md:2063:                           "url": "https://github.com/encorescience/encore-registry/actions/runs/45857382971"}},
```

**Agent calls Bash**

```bash
ls transcripts/pasquereau-2013/; sed -n 2050,2070p transcripts/pasquereau-2013/author.md; sed -n 100,125p transcripts/pasquereau-2013/author.md | cut -c1-200
```

```
attempt-01
attempt-02
author-report.md
author-revise-1-report.md
author-revise-1.md
author-revise-2-report.md
author-revise-2.md
author-revise-3-report.md
author-revise-3.md
author.md
verifier-1-report.md
verifier-1.md
verifier-2-report.md
verifier-2.md
verifier-3-report.md
verifier-3.md
]

rec = {
 "schema_version": 3,
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/pasquereau-2013; grep -n "pasquereau-2013-0[12]\|attempt-0[12]\|earlier attempt\|stretch.py" author*.md | cut -c1-250 | head -30
```

```
author-report.md:42:**Earlier attempts:** I came across none. The claims file's own header says its author had seen a data check and mentions "repeated files". That is from the claims file, not an earlier attempt's results; I found no repeated files 
author-revise-3.md:34:Write `attempts/<paper>-<nn>.yaml`, numbered after the paper's earlier attempts.
author.md:2322:**Earlier attempts:** I came across none. The claims file's own header says its author had seen a data check and mentions "repeated files". That is from the claims file, not an earlier attempt's results; I found no repeated files in th
```

**Agent**

Audit hits are all README/protocol text and the record-writing script; the author reports seeing no earlier attempt. Now the two records.

**Agent calls Bash**

```bash
cd  cat attempts/pasquereau-2013-02.yaml
```

```
<persisted-output>
Output too large (64.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/e76010b1-d031-4202-a8ce-71c88fc1e702/tool-results/bxrxrazhn.txt

Preview (first 2KB):
# Repeat attempt on the draft of dandiset 001636, last modified 2026-10-21T20:16:41Z, which holds a
# new conversion made after pasquereau-2013-01, on version 0.260518.1819, reported its
# findings. The code that built it is in an open pull request of catalystneuro/turner-lab-to-nwb
# (#33, branch fix_errors, head 5f9bf6320a0160e4e56301d5409fb9242c1d8cf4). The draft was asked for.
# When it was read, the archive listed 4 uploads in progress on the draft. Between 23:00 and 23:10 UTC
# on the same day every asset of the draft was uploaded again; the revision after the first
# verification round read the draft as modified at 23:10:32 UTC (no asset changed after 23:08:46),
# and every number recorded here from the earlier state is unchanged. The claims file is unchanged.
#
# Status of the findings of pasquereau-2013-01 on the draft (outputs in the notebook's data check):
# - No torque perturbation in any monkey L file (data_missing): still present; the description and the
#   files now say so. Recorded below.
# - Analog streams not on the clock of the trials (format_error): fixed. Each analog segment starts at
#   its trial's start (lag 0 ms at every perturbation), and on the stored clock the torque command steps
#   4 to 6 ms after the labelled onset.
# - Three torque command sizes, differing between the states (other): partly fixed. The data are the
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import yaml
for a in ['02','03']:
    r=yaml.safe_load(open(f'attempts/pasquereau-2013-{a}.yaml'))
    print('=====',a, r.get('datasets'), r['provenance']['agent'])
    print('keys',list(r))
    for o in r['outcomes']:
        print(o['claim'], o['outcome'], o.get('blocked_by',''), '| measured', o.get('measured'))
    print('--findings')
    for i,f in enumerate(r.get('findings',[]),1):
        print(i, f.get('kind'), f.get('about'), f.get('severity'), f.get('output'),'::', f['statement'][:400])
        print()
EOF
```

```
===== 02 [{'archive': 'dandi', 'id': '001636', 'version': 'draft', 'modified': datetime.datetime(2026, 10, 21, 23, 10, 32, tzinfo=datetime.timezone.utc), 'relation': 'primary'}] {'harness': 'Claude Code (GitHub Actions)', 'model': 'claude-opus-5-5', 'protocol': 'pilot-10'}
keys ['schema_version', 'id', 'datasets', 'paper', 'date', 'entry', 'provenance', 'outcomes', 'findings', 'verifications', 'findings_review']
cell-counts reproduced  | measured [115, 157, 51, 54, 32, 48, 3]
monkey-l-perturbations blocked data_missing | measured None
baseline-rate reproduced  | measured [12.66, 8.85, 18.49, 14.37, 3.48, 3.36]
ptn-faster-than-csn reproduced  | measured None
antidromic-latency partially_reproduced  | measured [1.92, 1.86, 4.91, 6.85]
false-positive-rate blocked methods_underspecified | measured 0.2279
torque-related-fractions blocked methods_underspecified | measured [54.8, 47.8, 72.5, 68.5, 15.6, 16.7]
prevalence-unchanged blocked methods_underspecified | measured None
ptn-more-responsive blocked methods_underspecified | measured [70.5, 16.2]
one-direction-half blocked methods_underspecified | measured 52.2
excitatory-majority blocked methods_underspecified | measured [83.1, 76.5, 70.0, 59.3]
magnitude-unchanged blocked methods_underspecified | measured None
venus-response-magnitudes blocked methods_underspecified | measured [40.21, 31.22, 47.65, 33.2, 31.74, 19.95, 36.22, 23.79]
latency-shorter blocked methods_underspecified | measured [41.47, 36.21, 42.28, 36.21, 44.63, 38.18, 45.3, 38.5]
latency-not-training blocked methods_underspecified | measured None
fwhm-shorter-ptn blocked methods_underspecified | measured [91.58, 40.05, 68.81, 41.73]
dsi-reduced blocked methods_underspecified | measured None
venus-dsi blocked methods_underspecified | measured [0.62, 0.463, 0.759, 0.46, 0.662, 0.695]
[... 71 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import yaml
r2=yaml.safe_load(open('attempts/pasquereau-2013-02.yaml'));r3=yaml.safe_load(open('attempts/pasquereau-2013-03.yaml'))
o2={o['claim']:o['outcome'] for o in r2['outcomes']};o3={o['claim']:o['outcome'] for o in r3['outcomes']}
print([c for c in o2 if o3.get(c)!=o2[c]], set(o2)^set(o3))
for a,r in (('02',r2),('03',r3)):
    print('=====',a)
    for i,f in enumerate(r['findings'],1):
        print(i, yaml.safe_dump(f, width=200)); 
print(yaml.safe_dump(r2.get('findings_review'),width=200))
EOF
```

```
[] set()
===== 02
1 kind: data_missing
statement: Still present since pasquereau-2013-01. The monkey L (Leu) files mark no torque perturbation; torque_perturbation_type is not_available in every Leu trial, the Leu torque command is NaN in every
  pre-MPTP file, and 15 of 50 post-MPTP Leu files have no analog data. The draft's description and the files now say the Leu source files contain no perturbation times. The monkey L half of the paper (115
  and 73 cells, and its EMG and kinematics) cannot be tested.

2 about: data
kind: other
statement: Partly fixed since pasquereau-2013-01. The torque command's 50 ms pulse still has three session sizes (about 46, 91 and 183 units above rest); most pre-MPTP monkey V sessions have the smallest
  (105 of 154) and most post-MPTP sessions the largest (125 of 137), post-MPTP pulses are followed by an opposite swing, and within post-MPTP sessions the step varies from trial to trial. The torque description
  now states all of this and that no conversion to newton-metres is available. The paper describes one 0.1 Nm, 50 ms impulse; whether the torque or only its command changed cannot be told, and movement
  and EMG results differ between command sizes.

3 about: data
kind: other
statement: Partly fixed since pasquereau-2013-01. The EMG description now gives the paper's processing (rectified, low-pass filtered at 100 Hz) where it said sample-hold integrated; the values are unchanged.
  The monkey L analog streams are still sampled at 100 Hz (the paper says 200 Hz) and the EMG is in uncalibrated A/D units, both now stated in the dandiset's description.

4 about: data
[... 94 more lines not kept]
```

**Agent**

Outcomes are identical on all 28 claims, so step 4 will be empty. Findings 1, 2, 4, 5 of the earlier attempt map to 03's findings; 3, 6, 7, 8 need direct checks. Looking at the entry and helpers.

**Agent calls Bash**

```bash
cd  cat entries/pasquereau-2013/entry.yaml entries/pasquereau-2013/requirements.in; wc -l entries/pasquereau-2013/pasq.py; grep -n "^def \|^[A-Z_]* =" entries/pasquereau-2013/pasq.py; ls paper* papers 2>/dev/null | head; python tools/entry.py --help 2>&1 | head -30
```

```
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
python: "3.13"
notebooks:
- path: reproduce_pasquereau_2013.ipynb
  title: Reproducing Pasquereau & Turner (2013) from dandiset 001636
  runtime_minutes: 11
helpers:
- pasq.py
related:
- id: dandi:001636/0.261124.1906
[... 97 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/pasquereau-2013; sed -n 1,206p pasq.py; sed -n 330,360p pasq.py; sed -n 485,522p pasq.py
```

```
"""Loading and measures for the torque perturbation data of dandiset 001636 (monkey V).

Pasquereau & Turner (2013), Front. Syst. Neurosci. 7:98, doi:10.3389/fnsys.2013.00098.

Each NWB file holds one recording (one or two units) with a trials table whose
`torque_perturbation_type` and `torque_perturbation_onset_time` mark the perturbations, the elbow
angle and the torque command at 1 kHz, and up to six EMG channels. Files are streamed from the
archive at the pinned version with remfile and h5py (reading the NWB paths directly is much
faster than building the pynwb objects of 291 files); nothing is written to disk. Only windows
around each perturbation are kept.

Where the parameters come from. "Claims" means the opening comment and criteria of
claims/pasquereau-2013.yaml, which cite the paper's Methods; "Methods" means the paper's
Methods, Data analysis.

- Cells studied: units with at least 5 perturbations of each direction (Methods, "for neurons
  studied during at least 5 repetitions of each torque direction"; claims).
- SDF: spikes convolved at 1 ms with a gamma kernel, k = 1.5, theta = 20 ms (Methods). The
  kernel is truncated at 400 ms, where its tail is below 1e-7 of its mass (a standard choice
  that cannot change a result).
[... 255 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('earlier-entry/reproduce_pasquereau_2013.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    if any(k in s for k in ['v1401','100 Hz','rate','description','sample-hold','1401','no pulse','flat']):
        if c['cell_type']=='code' and any(k in s for k in ['v1401','rate','description','no pulse','1401']):
            print('---',i,c.get('metadata',{}).get('tags'));print(s[:2500])
EOF
```

```
--- 3 ['sanity']
sessions = pd.DataFrame([{
    "si": si, "session": s["session_id"], "code": s["session_id"].split("++")[1],
    "subject": s["subject"], "post": s["post"], "date": s["date"], "n_trials": len(s["trials"]),
    "n_flex": int((s["pert_direction"] == "flexion").sum()),
    "n_ext": int((s["pert_direction"] == "extension").sum()), "n_units": len(s["units"]),
    "analog_dt_ms": s.get("analog_dt_ms", np.nan), "has_analog": "windows" in s or "analog_dt_ms" in s,
    "angle_all_nan": s.get("angle_all_nan", True), "torque_all_nan": s.get("torque_all_nan", True),
    "emg_channels": len(s.get("emg_channels", [])), "emg_same_clock": s.get("emg_same_clock", np.nan),
} for si, s in enumerate(S)])
units = pd.DataFrame([{
    "si": si, "ui": ui, "session": s["session_id"], "subject": s["subject"], "post": s["post"],
    "is_post_mptp": u["is_post_mptp"], "projection": u["type"], "ptype": stretch.short_type(u["type"]),
    "unit_name": u["unit_name"], "also_in": u["also_in"], "date": s["date"],
    "n_flex": int((u["pert_direction"] == "flexion").sum()),
    "n_ext": int((u["pert_direction"] == "extension").sum()),
    "n_flex_session": int((s["pert_direction"] == "flexion").sum()),
    "n_ext_session": int((s["pert_direction"] == "extension").sum()),
    "source_files": len(u["unit_name"].split("+")), "outside_obs": u.get("outside_obs", 0),
    "antidromic_latency_ms": u["antidromic_latency_ms"], "n_spikes": len(u["spikes"]),
[... 321 more lines not kept]
```

**Agent calls Bash**

```bash
cd  git check-ignore -v paper/x.txt; grep -n "16.3\|18.3\|3\.6 \|23/24\|19/22\|200 Hz\|sample-hold\|integrat" paper/10.3389-fnsys.2013.00098.txt | cut -c1-300 | head -20; gh api repos/catalystneuro/turner-lab-to-nwb/pulls/33 --jq '.state,.merged_at,.head.sha' ; gh api repos/catalystneuro/turner-lab-to-nwb/commits/main --jq '.sha,.commit.committer.date'
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import re
t=open('paper/10.3389-fnsys.2013.00098.txt').read()
for pat in ['16\.3','18\.3','200 Hz','sample','p < 0.01','23','rectif']:
    for m in re.finditer(pat,t):
        s=t[max(0,m.start()-200):m.end()+200].replace('\n',' ')
        if pat=='23' and 'excit' not in s: continue
        print(pat,'::',s);print()
EOF
curl -s https://api.github.com/repos/catalystneuro/turner-lab-to-nwb/pulls/33 | python -c "import json,sys;d=json.load(sys.stdin);print(d.get('state'),d.get('merged_at'),d.get('head',{}).get('sha'),d.get('merge_commit_sha'))"; curl -s https://api.github.com/repos/catalystneuro/turner-lab-to-nwb/commits/main | python -c "import json,sys;d=json.load(sys.stdin);print(d.get('sha'),d['commit']['committer']['date'])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.github.com/repos/catalystneuro/turner-lab-to-nwb/compare/9a6a9b327b39d39f14b54eb0f58f5aa38b749829...main | python -c "import json,sys;d=json.load(sys.stdin);print(d.get('status'),d.get('ahead_by'),d.get('behind_by'))"; curl -s https://api.dandiarchive.org/api/dandisets/001636/versions/0.261124.1906/ > meta.json; python - <<'EOF'
import json,re
d=json.load(open('meta.json'))
print(d.keys())
s=json.dumps(d)
for m in re.finditer('turner-lab-to-nwb|github',s): print(s[max(0,m.start()-300):m.end()+200]);print()
desc=d.get('description','')
print(len(desc)); 
for k in ['200','100 Hz','A/D','uncalibrated','EMG','rectif','sample-hold','pulse','v1401','1401']:
    for m in re.finditer(k,desc): print(k,'::',desc[max(0,m.start()-250):m.end()+250].replace('\n',' '));print()
EOF
```

Result: the fetched text is not kept.

**Agent**

PR 33 of turner-lab-to-nwb was merged before this version was published, so earlier finding 8 looks fixed. Next I'm checking the files for findings 3 and 7.

**Agent calls Bash**

```bash
cd entries/pasquereau-2013; date -u; python - <<'EOF'
import pasq, h5py, remfile, numpy as np
v=pasq.asset_urls("sub-Venus"); l=pasq.asset_urls("sub-Leu")
print(len(v),len(l)); print([p for p,_ in v if any(k in p for k in ['1401','1402','1501'])])
print(v[0][0], l[0][0])
for p,u in [v[0], l[-1]]:
    with h5py.File(remfile.File(u),'r') as h:
        acq=h['acquisition']
        for k in acq:
            g=acq[k]
            if 'data' in g:
                ts=g['timestamps'][:20] if 'timestamps' in g else None
                rate=g['starting_time'].attrs.get('rate') if 'starting_time' in g else None
                print(p.split('/')[-1],k,dict(unit=g['data'].attrs.get('unit'),conv=g['data'].attrs.get('conversion')),'dt',None if ts is None else np.round(np.diff(ts[:5]),4),rate,'|',g.attrs.get('description')[:300] if g.attrs.get('description') else '')
EOF
```

```
Exit code 1
Thu Nov 26 20:41:07 UTC 2026
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "entries/pasquereau-2013/pasq.py", line 60, in <module>
    import h5py
ModuleNotFoundError: No module named 'h5py'
```

**Agent calls Bash**

```bash
cd  ls -a; ls ~/.cache 2>/dev/null; ls /tmp/claude* 2>/dev/null | head; sed -n 482,502p docs/protocol.md; find / -name "python*" -path "*venv*/bin/*" 2>/dev/null | head
```

```
.
..
.bash_profile
.bashrc
.claude
.env
.env.development
.env.development.local
.env.local
.env.production
.env.production.local
.env.test
.env.test.local
.git
.gitconfig
.github
.gitignore
.gitmodules
.idea
.mcp.json
[... 75 more lines not kept]
```

**Agent calls Bash**

```bash
cd  which uv python3.13; uv venv -q -p 3.13 $TMPDIR/venv && uv pip install -q -p $TMPDIR/venv/bin/python -r entries/pasquereau-2013/requirements.lock.txt 2>&1 | tail -3; ls executed 2>/dev/null
```

```
Exit code 2
/opt/hostedtoolcache/Python/3.13.18/x64/bin/uv
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python3.13
```

**Agent calls Bash**

```bash
cd  echo $TMPDIR; uv venv -p 3.13 $TMPDIR/venv 2>&1 | tail -3
```

```
/tmp/claude-1001
  cause: A virtual environment already exists at: /tmp/claude-1001/venv

hint: Use the `--clear` flag or set `UV_VENV_CLEAR=1` to replace the existing virtual environment
```

**Agent calls Bash**

```bash
cd  uv pip install -q -p $TMPDIR/venv/bin/python -r entries/pasquereau-2013/requirements.lock.txt 2>&1 | tail -3; $TMPDIR/venv/bin/python -c "import h5py,remfile,dandi;print('ok')"
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/pasquereau-2013; $TMPDIR/venv/bin/python - <<'EOF'
import pasq, h5py, remfile, numpy as np
v=pasq.asset_urls("sub-Venus"); l=pasq.asset_urls("sub-Leu")
print(len(v),len(l)); print([p for p,_ in v if any(k in p for k in ['1401','1402','1501'])])
print(v[0][0], l[-1][0])
for p,u in [v[0], l[-1]]:
    with h5py.File(remfile.File(u),'r') as h:
        acq=h['acquisition']
        for k in acq:
            g=acq[k]
            if 'data' in g:
                ts=g['timestamps'][:20] if 'timestamps' in g else None
                rate=g['starting_time'].attrs.get('rate') if 'starting_time' in g else None
                print(p.split('/')[-1],k,dict(unit=g['data'].attrs.get('unit'),conv=g['data'].attrs.get('conversion')),'dt',None if ts is None else np.round(np.diff(ts[:5]),4),rate,'|',g.attrs.get('description')[:400] if g.attrs.get('description') else '')
EOF
```

```
291 148
['sub-Venus/sub-Venus_ses-Venus++v1401++PreMPTP++Depth22990um++19990511_behavior+ecephys.nwb', 'sub-Venus/sub-Venus_ses-Venus++v1402++PreMPTP++Depth23700um++19990511_behavior+ecephys.nwb', 'sub-Venus/sub-Venus_ses-Venus++v1501++PreMPTP++Depth19700um++19990513_behavior+ecephys.nwb']
sub-Venus/sub-Venus_ses-Venus++v0502++PreMPTP++Depth22130um++19990406_behavior+ecephys.nwb sub-Leu/sub-Leu_ses-Leu++l9901++PreMPTP++Depth23580um++19930122_behavior+ecephys.nwb
sub-Venus_ses-Venus++v0502++PreMPTP++Depth22130um++19990406_behavior+ecephys.nwb EMGBrachioradialis {'unit': 'a.u.', 'conv': np.float64(1.0)} dt [0.001 0.001 0.001 0.001] None | Preprocessed EMG from Brachioradialis - elbow flexor and forearm supinator/pronator. Recording: chronically-implanted Teflon-insulated multistranded stainless steel wire electrodes. Signal processing (Pasquereau and Turner 2013): differentially amplified (gain = 10,000), band-pass filtered (20 Hz to 5 kHz), rectified and then low-pass filtered (100 Hz), then digitized.
sub-Venus_ses-Venus++v0502++PreMPTP++Depth22130um++19990406_behavior+ecephys.nwb EMGDeltoidPosterior {'unit': 'a.u.', 'conv': np.float64(1.0)} dt [0.001 0.001 0.001 0.001] None | Preprocessed EMG from Posterior deltoid - shoulder extensor and external rotator. Recording: chronically-implanted Teflon-insulated multistranded stainless steel wire electrodes. Signal processing (Pasquereau and Turner 2013): differentially amplified (gain = 10,000), band-pass filtered (20 Hz to 5 kHz), rectified and then low-pass filtered (100 Hz), then digitized.
sub-Venus_ses-Venus++v0502++PreMPTP++Depth22130um++19990406_behavior+ecephys.nwb EMGTrapezius {'unit': 'a.u.', 'conv': np.float64(1.0)} dt [0.001 0.001 0.001 0.001] None | Preprocessed EMG from Trapezius - shoulder and scapula stabilizer. Recording: chronically-implanted Teflon-insulated multistranded stainless steel wire electrodes. Signal processing (Pasquereau and Turner 2013): differentially amplified (gain = 10,000), band-pass
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/pasquereau-2013; python - <<'EOF'
import json
nb=json.load(open('reproduce_pasquereau_2013.ipynb'))
print(nb['metadata'])
for i,c in enumerate(nb['cells'][:6]):
    print('---',i,c['cell_type'],c.get('metadata'));print(''.join(c['source'])[:1800])
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    if 'finding-torque-command-levels' in str(c.get('metadata')) or 'finding-leu' in str(c.get('metadata')):
        print('---',i,c.get('metadata'));print(s[:2000])
EOF
```

```
{'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}}
--- 0 markdown {}
# Pasquereau & Turner (2013) on DANDI:001636

Paper: Pasquereau B, Turner RS (2013). Primary motor cortex of the parkinsonian monkey: altered
neuronal responses to muscle stretch. *Front. Syst. Neurosci.* 7:98,
[doi:10.3389/fnsys.2013.00098](https://doi.org/10.3389/fnsys.2013.00098).

Dataset: [DANDI:001636](https://dandiarchive.org/dandiset/001636/0.261124.1906), version
`0.261124.1906` (doi:10.48324/dandi.001636/0.261124.1906). This version was asked for in the
prompt of this attempt; it is also the newest published version (published 2026-11-24). The
paper cites no version.

Claims: `claims/pasquereau-2013.yaml`, written from the full text in PubMed Central
(PMC3840326), its Methods, Results, Table 1, figure legends and supplementary data sheet
(DataSheet1.PDF), whose table gives the results for each monkey.

The files of monkey L mark no torque perturbation, so every claim is tested on monkey V
(Venus, elbow), as the claims file says.

[... 106 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR && cat > $TMPDIR/mknb.py <<'PYEOF'
import json
cells = []
def md(s): cells.append({"cell_type": "markdown", "metadata": {}, "source": s.strip("\n")})
def code(s, tag=None):
    cells.append({"cell_type": "code", "metadata": {"tags": [tag]} if tag else {}, "execution_count": None,
                  "outputs": [], "source": s.strip("\n")})

md("""
# Earlier findings of pasquereau-2013-02, checked on DANDI:001636 version 0.261124.1906

Paper: Pasquereau B, Turner RS (2013). Primary motor cortex of the parkinsonian monkey: altered
neuronal responses to muscle stretch. *Front. Syst. Neurosci.* 7:98,
[doi:10.3389/fnsys.2013.00098](https://doi.org/10.3389/fnsys.2013.00098).

Dataset: [DANDI:001636](https://dandiarchive.org/dandiset/001636/0.261124.1906), version
`0.261124.1906`.

Attempt pasquereau-2013-02 read the draft of the dandiset (modified 2026-10-21) and recorded eight
findings. Findings 1, 2, 4 and 5 are reported again by pasquereau-2013-03 (its findings 1, 3, 7 and
5), and its notebook `reproduce_pasquereau_2013.ipynb` shows them. This notebook checks the other
four, 3, 6, 7 and 8, on this version. Each section opens with the earlier statement.
""")
code("""
import json
import urllib.request

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient
from scipy import stats

import pasq

pd.set_option("display.width", 160)
venus_urls = pasq.asset_urls("sub-Venus")
leu_urls = pasq.asset_urls("sub-Leu")
with DandiAPIClient() as client:
    meta = client.get_dandiset(pasq.DANDISET_ID, pasq.DANDISET_VERSION).get_raw_metadata()
print(f"{len(venus_urls)} Venus files, {len(leu_urls)} Leu files at version {pasq.DANDISET_VERSION}, "
      f"published {meta['datePublished'][:10]}")
""", "sanity")

md("""
## Finding 3

Earlier statement: "Partly fixed since pasquereau-2013-01. The EMG description now gives the paper's
processing (rectified, low-pass filtered at 100 Hz) where it said sample-hold integrated; the values
are unchanged. The monkey L analog streams are still sampled at 100 Hz (the paper says 200 Hz) and
the EMG is in uncalibrated A/D units, both now stated in the dandiset's description."

The paper's Methods: analog data "were digitized at either 200-Hz (monkey L) or 500-Hz (monkey V)".
Below, the sampling interval of every analog series in every Leu file, the unit and description of
the EMG series, and the dandiset description's sentences on both.
""")
code("""
def analog_summary(path, url):
    with h5py.File(remfile.File(url), "r") as h:
        acq = h["acquisition"]
        rows = []
        for k in acq:
            g = acq[k]
            if "data" not in g or "timestamps" not in g:
                continue
            ts = g["timestamps"][:1000]
            rows.append({"file": path.split("/")[-1], "series": k,
                         "interval_ms": round(float(np.median(np.diff(ts))) * 1000, 3),
                         "unit": g["data"].attrs.get("unit"),
                         "description": g.attrs.get("description", "")})
        return rows


leu_analog = pd.DataFrame([r for pu in leu_urls for r in analog_summary(*pu)])
print("Leu files with an analog series:", leu_analog.file.nunique(), "of", len(leu_urls))
print("Leu analog series by name and sampling interval (ms):")
print(leu_analog.groupby(["series", "interval_ms"]).size().to_string())
emg = leu_analog[leu_analog.series.str.startswith("EMG")]
print("Leu EMG series:", len(emg), "| units:", emg.unit.value_counts().to_dict())
venus_one = pd.DataFrame(analog_summary(*venus_urls[0]))
print("\\nVenus file", venus_urls[0][0].split("/")[-1])
print(venus_one[["series", "interval_ms", "unit"]].to_string(index=False))
print("\\nDescription of", venus_one.series.iloc[0], ":", venus_one.description.iloc[0])
print("\\nDandiset description, sentences on the sampling rate and units:")
for sentence in meta["description"].split(". "):
    if "100 Hz" in sentence or "arbitrary units" in sentence:
        print(" ", sentence.strip())
""", "earlier-finding-3")

md("""
## Finding 6

Earlier statement: "Still present. The pre-MPTP PTN and CSN resting rates are 16.3 and 3.6 spikes/s
in the text and 18.3 and 3.2 in Table 1. Table 1 marks the CSN change in the fraction of excitatory
responses p < 0.01, but its own counts (23 of 24 against 19 of 22) give p = 0.54 with the
Yates-corrected chi-square test that reproduces its other chi-square values."

This is about the paper, which has not changed. The text (Results) gives "mean rate: 16.3-spikes/s"
for PTNs and "mean rate: 3.6-spikes/s" for CSNs, citing Table 1; Table 1 gives 18.3 ± 8.6 and
3.2 ± 4.0. Table 1's CSN ratio of excitatory responses is 13/13 and 10/11 before MPTP and 11/13 and
8/9 after, marked "## p < 0.01 (χ2 test)". The test on those counts:
""")
code("""
text_rates = {"PTN": 16.3, "CSN": 3.6}
table_rates = {"PTN": 18.3, "CSN": 3.2}
print("pre-MPTP resting rates, text against Table 1:", {k: (text_rates[k], table_rates[k]) for k in text_rates})
csn = np.array([[13 + 10, 13 + 11 - (13 + 10)],    # pre-MPTP: excitatory, inhibitory
                [11 + 8, 13 + 9 - (11 + 8)]])      # post-MPTP
for correction in (True, False):
    chi2, p, dof, _ = stats.chi2_contingency(csn, correction=correction)
    print(f"CSN excitatory {csn[0, 0]}/{csn[0].sum()} against {csn[1, 0]}/{csn[1].sum()}, "
          f"Yates correction {correction}: chi2 = {chi2:.3f}, p = {p:.2f}")
print(f"Fisher exact p = {stats.fisher_exact(csn)[1]:.2f}")
""", "earlier-finding-6")

md("""
## Finding 7

Earlier statement: "New. Three monkey V sessions (v1401, v1402, v1501) have 51 labelled perturbations
but no pulse in the torque command, as the draft's torque description says. Their perturbations are
kept here, as the command is not used to select trials."

The torque command's pulse size of each labelled perturbation in these three files (`pasq.command_size`:
mean over 10 to 50 ms after onset less the mean over the 50 ms before, signed by direction), against
the same measure in every other Venus file of the same days and the files' torque description.
""")
code("""
codes = ["v1401", "v1402", "v1501"]
named = [pu for pu in venus_urls if any(f"++{c}++" in pu[0] for c in codes)]
days = {pu[0].split("++")[-1][:8] for pu in named}
others = [pu for pu in venus_urls if pu[0].split("++")[-1][:8] in days and pu not in named]
rows = []
for group, pus in (("named", named), ("same day", others)):
    for x in pasq.load_all(pus):
        c = pasq.command_size(x)
        span = np.nanmax(x["torque_cmd"], axis=1) - np.nanmin(x["torque_cmd"], axis=1)
        rows.append({"group": group, "session": x["session"].split("++")[1], "perturbations": len(x["pert"]),
                     "median_pulse": round(float(np.nanmedian(c)), 1),
                     "max_abs_pulse": round(float(np.nanmax(np.abs(c))), 1),
                     "max_span_-50_to_100_ms": round(float(np.nanmax(span)), 1)})
pulses = pd.DataFrame(rows)
print(pulses.to_string(index=False))
print("labelled perturbations in the three named sessions:",
      int(pulses[pulses.group == "named"].perturbations.sum()))
with h5py.File(remfile.File(named[0][1]), "r") as h:
    desc = h["acquisition/ElbowTorque"].attrs["description"]
print("\\nElbowTorque description, the sentence that names the sessions:")
print(" ", [s for s in desc.split(". ") if "v1401" in s][0])
""", "earlier-finding-7")

md("""
## Finding 8

Earlier statement: "New. The dandiset names catalystneuro/turner-lab-to-nwb as the code that compiled
it, but the repository's main branch is still at e80a192917490b50db6871180b6d1d9a24772e35, read for
pasquereau-2013-01, and does not hold the code that built the draft (merged sessions, obs_intervals,
the new unit names and descriptions). That code is in open pull request 33, branch fix_errors at
5f9bf6320a0160e4e56301d5409fb9242c1d8cf4."

The dandiset's `IsCompiledBy` resource at this version, and the state of pull request 33 and of the
repository's main branch from the GitHub API, read when this notebook runs.
""")
code("""
def github(path):
    req = urllib.request.Request("https://api.github.com/repos/catalystneuro/turner-lab-to-nwb/" + path,
                                 headers={"Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


compiled = [r for r in meta["relatedResource"] if r["relation"] == "dcite:IsCompiledBy"]
print("IsCompiledBy:", [(r["name"], r["url"]) for r in compiled])
pr = github("pulls/33")
print(f"pull request 33 ({pr['head']['ref']}): state {pr['state']}, merged at {pr['merged_at']}, "
      f"merge commit {pr['merge_commit_sha']}")
cmp_ = github(f"compare/{pr['merge_commit_sha']}...main")
print(f"main against the merge commit: {cmp_['status']} (ahead by {cmp_['ahead_by']}, behind by {cmp_['behind_by']})")
print("version published", meta["datePublished"])
""", "earlier-finding-8")

nb = {"cells": cells, "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}},
      "nbformat": 4, "nbformat_minor": 5}
for i, c in enumerate(nb["cells"]):
    c["id"] = f"c{i:02d}"
json.dump(nb, open("entries/pasquereau-2013/earlier_findings.ipynb", "w"), indent=1)
PYEOF
cd  && python $TMPDIR/mknb.py && cd entries/pasquereau-2013 && $TMPDIR/venv/bin/pip list 2>/dev/null | grep -i -E "nbconvert|ipykernel|jupyter"
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd entries/pasquereau-2013; python -c "
import json;nb=json.load(open('earlier_findings.ipynb'));print('\n\n'.join(c['source'] for c in nb['cells'] if c['cell_type']=='code'))" > $TMPDIR/t.py; time $TMPDIR/venv/bin/python $TMPDIR/t.py 2>&1 | tail -70
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/t.py", line 11, in <module>
    import pasq
ModuleNotFoundError: No module named 'pasq'

real	0m1.566s
user	0m2.021s
sys	0m0.123s
```

**Agent calls Bash**

```bash
cd entries/pasquereau-2013; time PYTHONPATH=. $TMPDIR/venv/bin/python $TMPDIR/t.py 2>&1 | tail -70
```

```
291 Venus files, 148 Leu files at version 0.261124.1906, published 2026-11-24
Leu files with an analog series: 133 of 148
Leu analog series by name and sampling interval (ms):
series       interval_ms
WristAngle   10.0           133
WristTorque  10.0           133
Leu EMG series: 0 | units: {}

Venus file sub-Venus_ses-Venus++v0502++PreMPTP++Depth22130um++19990406_behavior+ecephys.nwb
             series  interval_ms      unit
 EMGBrachioradialis          1.0      a.u.
EMGDeltoidPosterior          1.0      a.u.
       EMGTrapezius          1.0      a.u.
EMGTricepsLateralis          1.0      a.u.
  EMGTricepsLongus1          1.0      a.u.
  EMGTricepsLongus2          1.0      a.u.
         ElbowAngle          1.0   degrees
        ElbowTorque          1.0 arbitrary

Description of EMGBrachioradialis : Preprocessed EMG from Brachioradialis - elbow flexor and forearm supinator/pronator. Recording: chronically-implanted Teflon-insulated multistranded stainless steel wire electrodes. Signal processing (Pasquereau and Turner 2013): differentially amplified (gain = 10,000), band-pass filtered (20 Hz to 5 kHz), rectified and then low-pass filtered (100 Hz), then digitized.
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='/tmp/claude-1001/mknb.py'
s=open(p).read()
s=s.replace('''the same measure in every other Venus file of the same days and the files' torque description.''','''the same measure in the Venus files just before and after each of them in session order, and the files'
torque description.''')
s=s.replace('''days = {pu[0].split("++")[-1][:8] for pu in named}
others = [pu for pu in venus_urls if pu[0].split("++")[-1][:8] in days and pu not in named]
rows = []
for group, pus in (("named", named), ("same day", others)):''','''index = sorted({j for i, pu in enumerate(venus_urls) if pu in named for j in (i - 1, i + 1)})
neighbours = [venus_urls[j] for j in index if venus_urls[j] not in named]
rows = []
for group, pus in (("named", named), ("neighbour", neighbours)):''')
open(p,'w').write(s)
EOF
python $TMPDIR/mknb.py; cd entries/pasquereau-2013; python -c "
import json;nb=json.load(open('earlier_findings.ipynb'));c=[c['source'] for c in nb['cells'] if c['cell_type']=='code'];print(c[0]);print(c[3])" > $TMPDIR/t2.py; PYTHONPATH=. $TMPDIR/venv/bin/python $TMPDIR/t2.py 2>&1 | tail -15
```

```
291 Venus files, 148 Leu files at version 0.261124.1906, published 2026-11-24
    group session  perturbations  median_pulse  max_abs_pulse  max_span_-50_to_100_ms
    named   v1401             11          -0.0            0.6                     1.8
    named   v1402             13          -0.0            0.7                     1.7
    named   v1501             27           0.0            0.5                     1.8
neighbour   v1305              9          91.0           91.6                    95.3
neighbour   v1403             10          45.6           45.8                    48.8
neighbour   v1601             26          45.6           46.0                    48.9
labelled perturbations in the three named sessions: 51

ElbowTorque description, the sentence that names the sessions:
  Perturbations appear as 50 ms pulses that leave rest about 5 ms after torque_perturbation_onset_time and reach half their peak at about 8 ms (sessions v1401, v1402 and v1501 have perturbation times but no pulses in the command)
```

**Agent**

Notebook works. Adding it to `entry.yaml`, then lock, check and run.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/pasquereau-2013/entry.yaml",
 "old_string": "  runtime_minutes: 11\n",
 "new_string": "  runtime_minutes: 11\n- path: earlier_findings.ipynb\n  title: Earlier findings of pasquereau-2013-02, checked on version 0.261124.1906\n  runtime_minutes: 4\n"
}
```

```
The file entries/pasquereau-2013/entry.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cd  date -u; python tools/entry.py lock entries/pasquereau-2013 2>&1 | tail -5; git diff --stat; python tools/entry.py check entries/pasquereau-2013 2>&1 | tail -20
```

```
Thu Nov 26 20:49:54 UTC 2026
wrote pasquereau-2013/requirements.lock.txt (Python 3.13, with hashes)
 entries/pasquereau-2013/entry.yaml | 3 +++
 1 file changed, 3 insertions(+)
0 error(s)
```

**Agent calls Bash**

```bash
cd  python tools/entry.py run entries/pasquereau-2013 2>&1 | tail -20; date -u
```

```
Installed kernelspec registry-pasquereau-2013 in executed/pasquereau-2013/.venv/share/jupyter/kernels/registry-pasquereau-2013
pass  reproduce_pasquereau_2013.ipynb  (851 s)
pass  earlier_findings.ipynb  (193 s)
Thu Nov 26 21:07:32 UTC 2026
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/pasquereau-2013/earlier_findings.ipynb'))
for c in nb['cells']:
    for o in c.get('outputs',[]):
        print(''.join(o.get('text',''))[-900:])
EOF
```

```
291 Venus files, 148 Leu files at version 0.261124.1906, published 2026-11-24

Leu files with an analog series: 133 of 148
Leu analog series by name and sampling interval (ms):
series       interval_ms
WristAngle   10.0           133
WristTorque  10.0           133
Leu EMG series: 0 | units: {}

ateralis          1.0      a.u.
  EMGTricepsLongus1          1.0      a.u.
  EMGTricepsLongus2          1.0      a.u.
         ElbowAngle          1.0   degrees
        ElbowTorque          1.0 arbitrary

Description of EMGBrachioradialis : Preprocessed EMG from Brachioradialis - elbow flexor and forearm supinator/pronator. Recording: chronically-implanted Teflon-insulated multistranded stainless steel wire electrodes. Signal processing (Pasquereau and Turner 2013): differentially amplified (gain = 10,000), band-pass filtered (20 Hz to 5 kHz), rectified and then low-pass filtered (100 Hz), then digitized.

Dandiset description, sentences on the sampling rate and units:
  The Leu analog signals are stored at 100 Hz, where the papers give 200 Hz
  EMG, LFP and the torque command are in arbitrary units, because the amplifier gains are not in the MATLAB files the dataset was converted from.
[... 25 more lines not kept]
```

**Agent**

Entry runs cleanly. Now the schema for the reconciliation block and the protocol notes.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
s=json.load(open('schemas/attempt.schema.json'))
def find(o,k,path=''):
    if isinstance(o,dict):
        for kk,v in o.items():
            if kk==k: print(path+'/'+kk); print(json.dumps(v,indent=1)[:5000])
            find(v,k,path+'/'+kk)
    elif isinstance(o,list):
        for i,v in enumerate(o): find(v,k,path+f'[{i}]')
find(s,'reconciliation')
find(s,'found')
EOF
grep -n "^## \|^### " docs/pilot-notes.md | tail -30
```

```
/properties/reconciliation
{
 "description": "A repeat attempt's comparison with the attempt before it, written by the reconcile step once this attempt, made blind, has been verified (docs/protocol.md, \"Repeat attempts\"). A finding of this attempt that no item of `findings` points at is new.",
 "type": "object",
 "additionalProperties": false,
 "required": [
  "earlier",
  "date",
  "blind",
  "findings"
 ],
 "properties": {
  "earlier": {
   "description": "The id of the attempt compared with.",
   "type": "string"
  },
  "date": {
   "type": "string",
   "format": "date"
  },
[... 144 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n '381,$p' docs/pilot-notes.md
```

```
## Protocol pilot-12 (2026-10-27): blind repeat attempts

A repeat attempt used to start from the attempt before it: its author read the
earlier record, edited the earlier entry in place, and said for each earlier
finding whether it was fixed, with the earlier outcome next to each new one.
That anchored it. An error in the earlier attempt was re-checked, not
questioned; a problem the earlier attempt missed was less likely to be looked
for; and two attempts on the same version could not be counted as two
readings, which the registry's paper needs to measure how far results repeat
(the attempts on 001754 are the example: attempt 03 marks each of its findings
"still present" or "new").

Now the author's runs are blind to earlier attempts (`tools/blind.sh` takes
them, and the history, out of the checkout), and a separate run, `reconcile`,
compares the verified attempt with the one before it, in a structured
`reconciliation` block: each earlier finding fixed, partly fixed, still present
or not checked, with a pointer to the new finding; findings the blind attempt
missed but the comparison found are marked `found: on_prompt`; outcomes that
differ get a reason. Finding statements no longer carry the comparison in
their opening words.
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -rn "pilot-1[5-9]" docs schemas tools --include=* 2>/dev/null | cut -c1-250 | head -30; cat protocol.lock 2>/dev/null | head
```

```
docs/pilot-notes/peterson-2021-02.md:4:under pilot-18. Seven claims reproduced (four on an assumption), four
docs/pilot-notes/tingley-2018-02.md:4:under pilot-15. Eight claims reproduced, eight partially, thirteen not
docs/pilot-notes/gao-2018-02.md:22:file was updated to pilot-15 for both datasets from the version of record
docs/pilot-notes/zhai-2025-02.md:3:The second attempt, made blind to the first (zhai-2025-01) under pilot-15,
docs/pilot-notes/pelot-2020-02.md:17:pilot-18 with 43 claims, and was blind to the earlier attempt. The claims
docs/protocol.md:3:Version: `pilot-19`. Record this version in the attempt's provenance.
docs/protocol.md:616:  Attempts made before `pilot-19` were not asked for a finding's code or
docs/protocol.md:620:  Attempts made before `pilot-18` did not rate their findings. A later review
schemas/attempt.schema.json:467:            "description": "From protocol pilot-18, in round 2: what the verifier said of each finding the record rates `critical` (docs/protocol.md, the attempt record).",
schemas/attempt.schema.json:552:            "description": "For a finding about the data: how much it harms someone who uses the dataset (docs/protocol.md, the attempt record). `critical`: the data are wrong and nothing shows it, so an analysis gives
schemas/attempt.schema.json:764:      "description": "For an attempt made before protocol pilot-18, whose findings carry no severity: the severity a later review gave each finding about the data, and whether the review checked it against the notebook
tools/entry.py:331:        # The rule is the protocol's from pilot-15. An attempt made under an earlier version is not held to it: its
tools/entry.py:336:        # From pilot-17, an attempt on a paper whose authors had sent notes says which it used, or that it used none
tools/entry.py:360:            # From pilot-18 a finding about the data says how much it harms a user of the dataset (docs/protocol.md,
tools/entry.py:380:            # pilot-19 a critical or 
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 320,400p tools/entry.py
```

```
for claim in sorted(known - set(recorded)):
            if not reread:
                report.error(where, f"claim {claim!r} has no outcome; give every claim one, blocked included")
        for claim in sorted({c for c in recorded if recorded.count(c) > 1}):
            report.error(where, f"claim {claim!r} has more than one outcome")
        # A finding is about the data (its dataset's page) or the paper (the paper's page). Its kind says which,
        # except for these two kinds, which must say; and in an attempt on several datasets a finding about the data
        # names the datasets it is about (docs/protocol.md, the attempt record).
        import datasets as archive_datasets
        used = [archive_datasets.folder(archive_datasets.key_of(d["archive"], str(d["id"])))
                for d in attempt.get("datasets") or ([attempt["dataset"]] if attempt.get("dataset") else [])]
        # The rule is the protocol's from pilot-15. An attempt made under an earlier version is not held to it: its
        # agents had not been told (a chain under way when the rule reached main ended in a failed check, as
        # hazon-2022 did on 2026-11-12), and the site takes such a finding by its kind.
        version = re.fullmatch(r"pilot-(\d+)", str(((attempt.get("provenance") or {}).get("agent") or {}).get("protocol") or ""))
        told = not version or int(version[1]) >= 15
        # From pilot-17, an attempt on a paper whose authors had sent notes says which it used, or that it used none
        # by listing none: the latest attempt names each note that was there when it was made (docs/protocol.md,
        # "Notes from the paper's authors"), so that the authors' input is never used unseen.
        if path == mine[-1] and version and int(version[1]) >= 17:
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "^#" attempts/pasquereau-2013-03.yaml | head; grep -n "^[a-z_]*:" attempts/pasquereau-2013-03.yaml; tail -30 attempts/pasquereau-2013-03.yaml; git diff --quiet attempts/ && echo clean
```

```
1:schema_version: 3
2:id: pasquereau-2013-03
3:datasets:
9:paper: doi:10.3389/fnsys.2013.00098
10:date: '2026-11-26'
11:entry: pasquereau-2013
12:provenance:
23:outcomes:
435:findings:
507:verifications:
    outcome: partially_reproduced
    reason: 'As written, the criterion is met at partial over all channel-sessions: 22.2 against 51.5 ms, KS p = 5.2e-33,
      with both means outside tolerance (cell 78). The proposal rests on the subsets in cell 75. These have 14 post-MPTP
      channel-sessions at 85 to 95 units and 5 pre-MPTP at 175 to 185 units. A non-significant result on so few
      cannot overturn the comparison the criterion specifies. The cell 75 numbers (32.4 against 24.1 ms, p = 0.32;
      27.0 against 46.7 ms, p = 0.087) match the record.'
    response: Outcome kept as partially_reproduced; the proposal stays with the verifier's view added to its reason.
      The conclusion, summary and README now say the verifier did not agree.
  - claim: emg-onset-unchanged
    agrees: false
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 490,508p attempts/pasquereau-2013-03.yaml
```

```
real cell-directions; none gives both the stated false-positive rate and the reported 62 to 75% of cells
    responding. All claims on the response selection are blocked until this is known.
- kind: methods_unavailable
  statement: Question for the authors. The trial-by-trial correlations of PTN response latency with peak velocity
    and m2 need a single-trial response latency, which the Methods do not define (the response onset is defined
    on the trial-averaged SDF). How was it measured?
- kind: other
  about: data
  severity: minor
  notebook: reproduce_pasquereau_2013.ipynb
  output: finding-perturbation-timing
  statement: In the Venus files the torque onset follows center_target_appearance_time by a near-fixed delay,
    1.695 to 1.698 s in 88.4% of 5550 perturbations (1.696 s in 3010), and the median delay is in that range
    in 288 of 291 files. The paper says the torque came at an unpredictable time, 1 to 2 s from a uniform
    distribution. Either the files' centre target time is placed from the perturbation onset or the timing
    differs from the paper's; the spikes and analog series agree with the onset (data check), so the analyses
    aligned to the onset are not affected, but a delay from the centre target computed from the files would be.
verifications:
- date: '2026-11-26'
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/rec.py <<'PYEOF'
import yaml
p = "attempts/pasquereau-2013-03.yaml"
text = open(p).read()
nb = "earlier_findings.ipynb"
new_findings = [
    {"kind": "other", "about": "data", "severity": "minor", "found": "on_prompt", "notebook": nb,
     "output": "earlier-finding-3",
     "statement": "The monkey L analog series, WristAngle and WristTorque in the 133 Leu files that have them, are "
                  "sampled every 10 ms (100 Hz), where the paper gives 200 Hz for monkey L. The Venus EMG is in "
                  "arbitrary units (a.u.), with no conversion to the microvolts of the paper's EMG figures. The "
                  "dandiset description states both; the EMG descriptions give the paper's processing (rectified, "
                  "low-pass filtered at 100 Hz)."},
    {"kind": "paper_inconsistency", "found": "on_prompt", "notebook": nb, "output": "earlier-finding-6",
     "statement": "The pre-MPTP resting rates of PTNs and CSNs are 16.3 and 3.6 spikes/s in the Results, which cite "
                  "Table 1, and 18.3 and 3.2 spikes/s in Table 1. Table 1 marks the change in the CSN fraction of "
                  "excitatory responses p < 0.01 (chi-square test), but its own counts, 23 of 24 before MPTP and "
                  "19 of 22 after, give p = 0.54 with the Yates correction, 0.25 without it and 0.34 with Fisher's "
                  "exact test."},
    {"kind": "other", "about": "data", "severity": "minor", "found": "on_prompt", "notebook": nb,
     "output": "earlier-finding-7",
     "statement": "In three Venus sessions (v1401, v1402 and v1501) the trials table marks 51 perturbations, but the "
                  "torque command has no pulse at any of them (median pulse 0.0 units, largest 0.7), where the "
                  "neighbouring sessions v1305, v1403 and v1601 have median pulses of 91.0, 45.6 and 45.6 units. The "
                  "ElbowTorque description says these sessions have no pulses in the command; whether a torque was "
                  "applied in their trials cannot be told from the files."},
]
rec = {"reconciliation": {
    "earlier": "pasquereau-2013-02",
    "date": "2026-11-26",
    "blind": True,
    "findings": [
        {"finding": 1, "status": "still_present", "now": 1,
         "note": "Both report that the Leu files mark no torque perturbation and that the Leu torque command is NaN "
                 "before MPTP; this attempt counts all 5952 Leu trials as not_available and the command NaN in 114 "
                 "of 148 files, consistent with the earlier 15 post-MPTP files without analog data."},
        {"finding": 2, "status": "still_present", "now": 3,
         "note": "Both report the same three command pulse sizes and their split by state; this attempt gives a mean "
                 "pulse of 58.4 units before MPTP and 174.7 after, with 125 of 137 post-MPTP sessions at 120 to 250 "
                 "units, as the earlier gave 125 of 137 at about 183 units. Its statement does not mention the "
                 "post-MPTP opposite swing or the trial-to-trial variation the earlier one did."},
        {"finding": 3, "status": "still_present", "now": 8,
         "note": "This attempt did not report it. In earlier_findings.ipynb (cell earlier-finding-3) all 133 Leu files "
                 "with analog series are sampled every 10.0 ms and the Venus EMG unit is a.u., both stated in the "
                 "dandiset description, as on the draft."},
        {"finding": 4, "status": "still_present", "now": 7,
         "note": "Both report the near-fixed delay from center_target_appearance_time to the torque onset, 1.696 to "
                 "1.732 s in 90% of monkey V perturbations on the draft and 1.695 to 1.698 s in 88.4% of 5550 here, "
                 "where the paper gives 1 to 2 s at random."},
        {"finding": 5, "status": "still_present", "now": 5,
         "note": "Both find that the response detection as described gives a false-positive rate of 0.23 at a pseudo "
                 "onset against the 0.01 the paper states, and no published code. The undefined single-trial latency "
                 "the earlier statement also names is this attempt's finding 6."},
        {"finding": 6, "status": "still_present", "now": 9,
         "note": "This attempt did not report it; the paper is unchanged. In earlier_findings.ipynb (cell "
                 "earlier-finding-6) the text gives 16.3 and 3.6 spikes/s and Table 1 18.3 and 3.2, and Table 1's CSN "
                 "counts give p = 0.54 with the Yates-corrected chi-square test where the table marks p < 0.01."},
        {"finding": 7, "status": "still_present", "now": 10,
         "note": "This attempt did not report it. In earlier_findings.ipynb (cell earlier-finding-7) v1401, v1402 and "
                 "v1501 hold 51 labelled perturbations with a largest pulse of 0.7 units, against 45.6 to 91.0 in "
                 "the neighbouring sessions, and the ElbowTorque description names the three sessions."},
        {"finding": 8, "status": "fixed",
         "note": "Pull request 33 of catalystneuro/turner-lab-to-nwb was merged on 2026-11-24 at 15:55 UTC, and main "
                 "is ahead of its merge commit 9a6a9b327b39d39f14b54eb0f58f5aa38b749829 by 2 commits and behind by 0, "
                 "before version 0.261124.1906 was published at 19:06 UTC that day (earlier_findings.ipynb, cell "
                 "earlier-finding-8). The dandiset still names the repository as the code that compiled it."},
    ],
    "protocol": "Of the versions after pilot-10, docs/pilot-notes.md describes pilot-12 (blind repeat attempts, "
                "compared afterwards by a separate reconcile run), pilot-13 (a notebook may take 60 minutes) and "
                "pilot-14 (records filed by paper, using every dataset the paper rests on). Pilot-12 is why this "
                "attempt wrote a new entry and notebook without seeing the earlier attempt, and why its finding "
                "statements no longer open with still present or new; it is also why findings 3, 6 and 7 of the "
                "earlier attempt, which this attempt did not report, were checked here and added with found "
                "on_prompt. Pilot-13 and pilot-14 changed nothing here, as the main notebook ran in 851 s and the "
                "paper rests on one dataset. The notes have no section for pilot-15 to pilot-19; docs/protocol.md "
                "says that from pilot-18 an attempt rates its findings about the data and from pilot-19 a critical "
                "or major one names the cell that shows it, which this attempt does and the earlier one did not. "
                "No claim's outcome differs between the two attempts.",
}}
dump = lambda o: yaml.safe_dump(o, sort_keys=False, width=110, allow_unicode=True)
fblock = dump(new_findings)
assert text.count("\nverifications:\n") == 1
text = text.replace("\nverifications:\n", "\n" + fblock + "verifications:\n")
text = text.rstrip("\n") + "\n" + dump(rec)
open(p, "w").write(text)
PYEOF
python $TMPDIR/rec.py && git diff --stat && python tools/entry.py check entries/pasquereau-2013 2>&1 | tail -10
```

```
attempts/pasquereau-2013-03.yaml   | 92 ++++++++++++++++++++++++++++++++++++++
 entries/pasquereau-2013/entry.yaml |  3 ++
 2 files changed, 95 insertions(+)
0 error(s)
```

**Agent calls Bash**

```bash
cd  git diff attempts/ | grep "^+" | grep -n -E ': .*: |—|rather' ; grep -c "" entries/pasquereau-2013/earlier_findings.ipynb; grep -n -E "—|rather" entries/pasquereau-2013/earlier_findings.ipynb; git status --short; python -c "
import json;nb=json.load(open('entries/pasquereau-2013/earlier_findings.ipynb'));print(all(not c.get('outputs') for c in nb['cells']))"
```

```
103
 M attempts/pasquereau-2013-03.yaml
 M entries/pasquereau-2013/entry.yaml
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
?? earlier-entry/
?? entries/pasquereau-2013/earlier_findings.ipynb
?? scripts
True
```

**Agent calls Bash**

```bash
cd  ls -la .bashrc .gitconfig .mcp.json .idea scripts .profile | head -20
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 26 20:32 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 26 20:32 .gitconfig
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 26 20:32 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 26 20:32 .mcp.json
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 26 20:32 .profile
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 26 20:32 scripts
```

**Agent**

The reconciliation is written and `python tools/entry.py check entries/pasquereau-2013` reports 0 errors. I changed nothing the blind attempt recorded and committed nothing. Both notebooks in the entry ran from a clean environment and passed (851 s and 193 s).

**1. Blindness.** `blind: true`. The audit found four lines, all in `author.md`: two links to the README and pilot notes, the README text itself, and the attempt's own runner URL inside its record-writing script. None of them points at an earlier attempt's results. The author's report says it came across no earlier attempt. It did see a header in the claims file mentioning an earlier data check and "repeated files". The protocol allows the author to keep the claims file, so I did not count that against blindness.

**2. Earlier findings (pasquereau-2013-02)**

| # | Earlier finding | Status | Now |
|---|---|---|---|
| 1 | Leu files have no perturbations | still_present | 1 |
| 2 | Three torque command pulse sizes, split by MPTP state | still_present | 3 |
| 3 | Leu analog stored at 100 Hz (paper says 200 Hz); EMG in arbitrary units | still_present (checked in `earlier_findings.ipynb`) | 8 |
| 4 | Torque onset a fixed delay after the centre target appears | still_present | 7 |
| 5 | Response detection gives a false-positive rate of 0.23; no code published | still_present | 5 |
| 6 | Resting rates differ between text and Table 1; Table 1's CSN chi-square gives p = 0.54 | still_present (checked) | 9 |
| 7 | v1401, v1402 and v1501: 51 labelled perturbations, no pulse in the command | still_present (checked) | 10 |
| 8 | Conversion code not on main of turner-lab-to-nwb | fixed (checked) | – |

- **Finding 8:** https://github.com/catalystneuro/turner-lab-to-nwb/pull/33 was merged at 15:55 UTC on 2026-11-24. The version was published at 19:06 UTC the same day, and main now contains the merge commit.
- **Findings 3, 6 and 7:** these were added to the record as findings 8, 9 and 10, with `found: on_prompt`. Each has a tagged cell in the new notebook `entries/pasquereau-2013/earlier_findings.ipynb`, which is now listed in `entry.yaml`. The lock file did not change.

**3. New findings.** 2, 4 and 6. Finding 4 is the attempt's list of checks that passed (severity none).

**4. Outcomes that changed.** None. All 28 claims have the same outcome in both attempts, so there is no `outcomes` list. The measured values differ slightly in a few places, for example kinematics 28.11/14.56 against 28.1/14.8, and EMG duration 24.6/49.4 against 22.2/51.5.

**5. What did not fit the protocol**
- **Missing pilot notes:** `docs/pilot-notes.md` has no sections for pilot-15 to pilot-19; the last one is pilot-14. For pilot-18 (findings rated by severity) and pilot-19 (a critical or major finding names the cell that shows it), I worked the changes out from `docs/protocol.md` and `tools/entry.py`. The `protocol` note says this, and that no outcome moved.
- **Only one `now` per finding:** earlier finding 5 covers two problems, the false-positive rate and the undefined single-trial latency. This attempt splits them into its findings 5 and 6, but `now` takes one number. I pointed it at 5 and named 6 in the note.
- **Finding 8 needs live GitHub data:** its notebook cell queries the GitHub API each time it runs, so its output reflects the repository as it is at that moment.

## End of run

40 turns, 29 minutes, $1.78 at API prices, result: success.
