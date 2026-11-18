# gao-2018 · reconcile · run 43621406504

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; grep -n "^#" docs/protocol.md | head -80
```

```
Sat Nov 14 17:36:47 UTC 2026
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
345:### 2. Check the data against its description
360:### 3. Write the entry
431:### 4. Lock, check and run
451:### 5. Record the attempt
524:### 6. Hand over for verification
562:## Repeat attempts
604:## Local and remote datasets
627:## Verifier
631:### Round 1: without the author's conclusions
[... 2 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 340,
 "limit": 290
}
```

```
340	     paper's reading as a variant where it can be run, and say in the
341	     claim's notes that it is asked. A reader decides whether to amend the
342	     claims file (reader, step 6), and a later run, `author-answers`,
343	     re-runs the claims it changed.
344	
345	### 2. Check the data against its description
346	
347	Descriptive metadata is often wrong. For every quantity the analysis uses,
348	check the description against the values: units and ranges, sampling rates,
349	counts of subjects, sessions, trials and cells, the size of an arena, which
350	conditions exist. Show that every data stream shares the clock of the trial
351	tables, using a contrast between conditions where an overall check cannot
352	tell a response from an offset (with spikes and a trial table only, decoding
353	a task variable in windows around the trial start does this; for continuous
354	sessions, decoding the annotations with the labels shifted in time), and name any
355	session where this could not be established. A description that a check
356	supports but does not prove is reported as consistent with the data, not as
357	shown. Where they disagree, trust the data, say so in the notebook,
358	and record it as a finding.
359	
[... 270 more lines not kept]
```

**Agent calls Bash**

```bash
cat docs/agents/reconcile.md 2>/dev/null; echo ----; tools/blind.sh audit gao-2018
```

```
<persisted-output>
Output too large (35KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/1ffb9917-0eea-44ac-9742-0341fbab9e78/tool-results/bddakn4nx.txt

Preview (first 2KB):
You reconcile a repeat attempt in the reproduction registry, checked out in the current directory. Read docs/protocol.md, "Repeat attempts", first. Attempt `{attempt}` on paper `{key}` (data: {dataset}; entry `entries/{entry}`, dataset version {version}) was made blind: its author did not see `{earlier}` (made on version {earlier_version}). Its record is `attempts/{earlier}.yaml`. Its entry is `entries/{earlier_entry}` as it was when that record was last changed: `c=$(git log -1 --format=%H -- attempts/{earlier}.yaml)`, then `git show $c:entries/{earlier_entry}/<file>`. Both have been through their verification rounds. Your job is to say how the two compare, in a `reconciliation` block of `attempts/{attempt}.yaml` (its schema is in `schemas/attempt.schema.json`). Do not change the outcomes, statements or notes that the blind attempt recorded, its claims file or its notebooks.

1. Run `tools/blind.sh audit {folder}`. It prints the lines of this attempt's author transcripts that point at an earlier attempt. Read each in context. Set `blind: true` if the author never saw an earlier attempt's results, else `blind: false` with what it saw under `blind_note`.
2. For each finding of `{earlier}`, in order (`finding` is its number, from 1), decide whether one of `{attempt}`'s findings reports the same problem: the same files, fields or values, not only the same kind. If so, set `status` to `still_present` or `partly_fixed`, and `now` to that finding's number in `{attempt}`. If not, check the earlier finding directly on version {version}, in a new notebook `entries/{entry}/earlier_findings.ipynb` (add it to `entry.yaml`, one short section per finding, each opening with the earlier statement, and lock, check and run the entry). Then:
   - `fixed`, when the check show
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
f=/home/runner/.claude/projects/-home-runner-work-encore-encore/1ffb9917-0eea-44ac-9742-0341fbab9e78/tool-results/bddakn4nx.txt; awk '/^----$/{p=1} p' $f | head -300
```

```
<persisted-output>
Output too large (31.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/1ffb9917-0eea-44ac-9742-0341fbab9e78/tool-results/bf3mzk668.txt

Preview (first 2KB):
----
transcripts/gao-2018/author-answers.md:159:transcripts/see-2018/author-revise-1.md:413:# Questions from attempt gao-2018-01 (author, 2026-11-10) about claims/gao-2018.yaml, asked under
transcripts/gao-2018/author-answers.md:160:transcripts/see-2018/author-revise-1.md:419:  attempt: gao-2018-01
transcripts/gao-2018/author-answers.md:161:transcripts/andrews-2024/recorder.md:15:docs/pilot-notes/gao-2018-01.md
transcripts/gao-2018/author-answers.md:162:transcripts/andrews-2024/recorder.md:38:cd  for f in docs/pilot-notes/{plitt-2021-01,gonzalez-cabrera-2026-01,kussovska-2025-01,gao-2018-01,mah-2023-01,knierim-2000-02}.md; do echo "=== $f"; cat $f; done; grep -n "Reproduced\|| Dandiset" README.md | head; cat summaries/plitt-2021-01.md summaries/gao-2018-01.md; python -c "
transcripts/gao-2018/author-answers.md:163:transcripts/andrews-2024/recorder.md:73:cd  for f in docs/pilot-notes/{plitt-2021-01,gonzalez-cabrera-2026-01,kussovska-2025-01,gao-2018-01,mah-2023-01}.md; do echo "=== $f"; cat $f; done; head -5 docs/pilot-notes/knierim-2000-02.md
transcripts/gao-2018/author-answers.md:164:transcripts/kussovska-2025/recorder.md:12:docs/pilot-notes/gao-2018-01.md
transcripts/gao-2018/author-answers.md:165:transcripts/kussovska-2025/recorder.md:38:for f in gao-2018-01 mah-2023-01 patel-2026-01 keles-2024-01 mehrotra-2024-01; do echo "=== $f"; cat docs/pilot-notes/$f.md; done; head -3 docs/pilot-notes/knierim-2000-02.md; grep -n "| Dandiset\|^| ---" README.md | head; cat summaries/gao-2018-01.md summaries/mah-2023-01.md
transcripts/gao-2018/author-answers.md:166:transcripts/kussovska-2025/recorder.md:46:=== gao-2018-01
transcripts/gao-2018/author-answers.md:168:transcripts/kussovska-2025/recorder.md:74:1	=== gao-2018-01
transcripts/gao-2018/author-answers.md:170
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
f=/home/runner/.claude/projects/-home-runner-work-encore-encore/1ffb9917-0eea-44ac-9742-0341fbab9e78/tool-results/bf3mzk668.txt; grep -v '^----' $f | cut -d: -f1,2 | awk -F: '{print $1}' | sort | uniq -c; grep -v '^----' $f | cut -d: -f1,2 | awk -F: '{print $2}' | sort -n | uniq | tr '\n' ' '
```

```
12 transcripts/gao-2018/author-answers.md
      1 transcripts/gao-2018/author.md
159 160 161 162 163 164 165 166 168 170 171 201 2426
```

**Agent calls Bash**

```bash
sed -n 120,215p transcripts/gao-2018/author-answers.md | cut -c1-400; echo =====; sed -n 2400,2440p transcripts/gao-2018/author.md | cut -c1-600
```

````
cd  ls questions | grep -E "^0|alm"; grep -rl "gao-2018\|fig1g-fastigial\|000007" questions | head; sed -n 1060,1120p claims/gao-2018.yaml
```

```
- about: unilateral ALM photo-inhibition after fastigial perturbation, stronger mark
    test: one-sided bootstrap
    p: 0.008
    n: 4 mice
  - about: no lick rate, bilateral ALM photo-inhibition, weaker mark
    test: one-sided bootstrap
    p: 0.002
    n: 3 mice
  - about: no lick rate, bilateral ALM photo-inhibition, stronger mark
    test: one-sided bootstrap
    p: 0.0002
    n: 3 mice
  datasets:
  - "000007"
  - crcns-alm-4
  criterion: VGAT-ChR2-EYFP behavior (Methods, ALM photo-inhibition after a fastigial
[... 118 more lines not kept]
````

**Agent calls Bash**

```bash
cd transcripts/gao-2018; sed -n 2426p author.md | cut -c1-300; grep -n "gao-2018-01\|pilot-notes/gao\|summaries/gao\|questions/gao" author-answers.md | cut -c1-250; wc -l author-answers.md; ls
```

```
"content": "schema_version: 3\nid: gao-2018-02\ndatasets:\n- archive: dandi\n  id: \"000007\"\n  version: 0.220126.1903\n  doi: 10.48324/dandi.000007/0.220126.1903\n  relation: primary\n- archive: crcns\n  id: alm-4\n  version: unversioned\n  doi: 10.6080/K0NS0S26\n  relation: primary\npaper: doi:1
8:date -u; cd  ls; ls entries/gao-2018 entries/gao-2018/*; cat questions/gao-2018.yaml
73:168:questions/gao-2025:
149:The questions file `questions/gao-2018.yaml` named in the task does not exist in this checkout. Let me check the protocol and whether the attempt asked any questions at all.
158:transcripts/see-2018/author-revise-1.md:406:cd  ls questions/*.yaml | head -3; cat questions/gao-2018.yaml | head -30; sed -n 1,80p claims/see-2018.yaml
159:transcripts/see-2018/author-revise-1.md:413:# Questions from attempt gao-2018-01 (author, 2026-11-10) about claims/gao-2018.yaml, asked under
160:transcripts/see-2018/author-revise-1.md:419:  attempt: gao-2018-01
161:transcripts/andrews-2024/recorder.md:15:docs/pilot-notes/gao-2018-01.md
162:transcripts/andrews-2024/recorder.md:38:cd  for f in docs/pilot-notes/{plitt-2021-01,gonzalez-cabrera-2026-01,kussovska-2025-01,gao-2018-01,mah-2023-01,knierim-2000-02}.md; do echo "=== $f"; cat $f; done; grep -n "Reproduced\|| Dandiset" README.m
163:transcripts/andrews-2024/recorder.md:73:cd  for f in docs/pilot-notes/{plitt-2021-01,gonzalez-cabrera-2026-01,kussovska-2025-01,gao-2018-01,mah-2023-01}.md; do echo "=== $f"; cat $f; done; head -5 docs/pilot-notes/knierim-2000-02.md
164:transcripts/kussovska-2025/recorder.md:12:docs/pilot-notes/gao-2018-01.md
165:transcripts/kussovska-2025/recorder.md:38:for f in gao-2018-01 mah-2023-01 patel-2026-01 keles-2024-01 mehrotra-2024-01; do echo "=== $f"; cat docs/pilot-notes/$f.md; done; head -3 docs/pilot-notes/knierim-2000-02.md; grep -n "| Dandiset\|^| ---"
166:transcripts/kussovska-2025/recorder.md:46:=== gao-2018-01
168:transcripts/kussovska-2025/recorder.md:74:1	=== gao-2018-01
170:transcripts
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 172,232p transcripts/gao-2018/author-answers.md | cut -c1-500
```

````
transcripts/steinmetz-2019/recorder.md:15:
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1410,1470p transcripts/wirth-2017/author-revise-2.md; sed -n 400,470p transcripts/see-2018/author-revise-1.md; ls transcripts | grep gao; ls transcripts/gao-2018 2>/dev/null
```

````
"reproduced",
[... 38 more lines not kept]
```

**Agent calls Bash**

```bash
head -4 questions/brinke-2017.yaml questions/gao-2018.yaml
```
[... 41 more lines not kept]
````

**Agent calls Bash**

```bash
sed -n 400,470p transcripts/see-2018/author-revise-1.md | cut -c1-300
```

````
Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls questions/*.yaml | head -3; cat questions/gao-2018.yaml | head -30; sed -n 1,80p claims/see-2018.yaml
```

```
questions/ashworth-2025.yaml
questions/athalye-2023.yaml
questions/bech-2026.yaml
# Questions from attempt gao-2018-01 (author, 2026-11-10) about claims/gao-2018.yaml, asked under
# docs/protocol.md, Author, step 1.6, and "Hand over for verification". The claim is tested as the
# claims file has it.
paper: doi:10.1038/s41586-018-0633-x
questions:
- claim: fig2cd-selectivity-emerges-gradually
  attempt: gao-2018-01
  asked: 2026-11-10
[... 49 more lines not kept]
````

**Agent calls Bash**

```bash
sed -n 232,355p transcripts/gao-2018/author-answers.md | cut -c1-300 | grep -v '^$' | head -90; cat transcripts/gao-2018/author-answers-report.md
```

````
I've written the new entry at `entries/gao-2018`, the record at `attempts/gao-2018-02.yaml`, and built the handover in `executed/gao-2018/handover/`. The entry check gives 0 errors and the notebook runs from a clean environment in about 20 minutes. I did not verify my own work, commit or push. I did
[... 68 more lines not kept]
```
**Agent calls Bash**
```bash
cd  ls -la --time-style=full-iso claims/gao-2018.yaml attempts/gao-2018-02.yaml entries/gao-2018 executed/gao-2018 executed/gao-2018/handover 2>&1 | head -40; grep -rn "sha\|claims" executed/gao-2018/handover/*.json 2>/dev/null | head
```
```
-rw-r--r-- 1 runner runner 29511 2026-11-14 12:41:58.248799903 +0000 attempts/gao-2018-02.yaml
-rw-r--r-- 1 runner runner 67695 2026-11-14 12:41:56.008820322 +0000 claims/gao-2018.yaml
entries/gao-2018:
total 284
drwxr-xr-x   2 runner runner   4096 2026-11-14 12:41:58.249799894 +0000 .
drwxr-xr-x 293 runner runner  12288 2026-11-14 12:41:56.344334535 +0000 ..
-rw-r--r--   1 runner runner   3001 2026-11-14 12:41:58.248799903 +0000 README.md
-rw-r--r--   1 runner runner   1030 2026-11-14 12:41:58.248799903 +0000 entry.yaml
-rw-r--r--   1 runner runner  30767 2026-11-14 12:41:58.248799903 +0000 gao2018.py
-rw-r--r--   1 runner runner  76424 2026-11-14 12:41:58.249799894 +0000 reproduce_gao_2018.ipynb
-rw-r--r--   1 runner runner     79 2026-11-14 12:41:58.249799894 +0000 requirements.in
-rw-r--r--   1 runner runner 149001 2026-11-14 12:41:58.249799894 +0000 requirements.lock.txt
[... 84 more lines not kept]
````

**Agent calls Bash**

```bash
python - <<'EOF'
import json
s=json.load(open('schemas/attempt.schema.json'))
def find(o,path=''):
    if isinstance(o,dict):
        for k,v in o.items():
            if k=='reconciliation': print(path+'/'+k); print(json.dumps(v,indent=1)[:5000])
            find(v,path+'/'+k)
find(s)
p=s.get('properties',{}).get('findings') 
print(json.dumps(p,indent=1)[:3000])
EOF
grep -n '\$defs\|"definitions"' schemas/attempt.schema.json | head
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
[... 134 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import yaml
for a in ['gao-2018-01','gao-2018-02']:
    r=yaml.safe_load(open(f'attempts/{a}.yaml'))
    print('=====',a, r.get('date'), r.get('provenance',{}).get('agent'))
    for i,f in enumerate(r.get('findings',[]),1):
        print(f"[{i}] {f['kind']} {f.get('about','')} {f.get('datasets','')}\n    {f['statement']}\n")
EOF
```

```
===== gao-2018-01 2026-11-10 {'harness': 'Claude Code', 'model': 'claude-opus-5-5', 'protocol': 'pilot-14'}
[1] data_missing  
    The dandiset holds only the ALM recordings (54 sessions, 13 mice). The CN recordings (878 units in 18 mice and 60 units in 2 L7-cre x Ai32 mice), lick times, the behavior-only sessions (lesions, 1.3 s and response epoch photo-activation, 0.5 s and response epoch photo-inhibition), the VGAT-ChR2-EYFP experiments and the anatomy are not in it; 26 of the 45 claims cannot be tested.

[2] metadata_insufficient  
    photo_stim_id has no description, and the files hold no laser trace. The codes are 1 and 2 in fastigial, 3 and 4 in dentate and 5 and 6 in L7-cre x Ai32 sessions; from the ALM response, 1 and 3 start at sample onset and 2, 4, 5 and 6 at delay onset. Codes 5 and 6 both last through the delay; the ALM change to code 5 fades over the delay (mean absolute change 3.1 to 3.2 spikes/s early in the delay, 2.1 at its end) and to code 6 does not (2.95 to 3.00 early, 2.93 at its end), as two powers would give, but which is 1.5 mW and which 4.5 mW cannot be told, nor the photo-activation power. The ALM change to CN photo-inhibition starts about 30 ms after pole_out_time under both codes, so when the photostimulus starts relative to pole_out_time cannot be checked.

[3] metadata_error  
    The descriptions of pole_in_time, pole_out_time and cue_time say they are relative to the trial start; the values are on the session clock (pole_in_time - start_time is 0.57 s in most trials).

[4] metadata_error  
    Hemispheres disagree with Supplemental Table 1. The files place the manipulated CN of CD12 and CD13 on the left, the same side as the recorded ALM, where the table gives the right CN and the Methods say ALM was always recorded contralaterally; CD14 is recorded in the left ALM in the files and the right ALM in the table. Within each subject every session has the same coordinates.

[5] identifier_missing  
    Subjects anm00314746, anm00314756,
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; c=$(git log -1 --format=%H -- attempts/gao-2018-01.yaml); echo $c; git show --stat $c | head; git ls-tree --name-only $c entries/gao-2018/; ls entries/gao-2018 executed/gao-2018; cat entries/gao-2018/entry.yaml; grep -n "^def \|^class " entries/gao-2018/gao2018.py
```

```
Sat Nov 14 17:38:06 UTC 2026
0c97448751a9a6fa09aba58d3812e7c159d5962d
commit 0c97448751a9a6fa09aba58d3812e7c159d5962d
Author: github-actions[bot] <github-actions[bot]@users.noreply.github.com>
Date:   Sat Nov 14 17:28:50 2026 +0000

    Agent run on gao-2018: author-revise-3 (success)
    
    Run: https://github.com/catalystneuro/encore/actions/runs/43619056457
    
    Account: verified

entries/gao-2018/README.md
entries/gao-2018/entry.yaml
entries/gao-2018/gao2018.py
entries/gao-2018/reproduce_gao_2018.ipynb
entries/gao-2018/requirements.in
entries/gao-2018/requirements.lock.txt
ls: cannot access 'executed/gao-2018': No such file or directory
entries/gao-2018:
[... 56 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "entries/gao-2018/gao2018.py",
 "limit": 330
}
```

```
1	"""Loading and measures for Gao et al. (2018), "A cortico-cerebellar loop for motor planning",
2	Nature 563, 113-116, doi:10.1038/s41586-018-0633-x, on its two datasets.
3	
4	- DANDI:000007, version 0.220126.1903: 54 NWB files (13 mice) of ALM single units, a trial
5	  table and the photostimulation code of each trial. Streamed with remfile and h5py.
6	- CRCNS:alm-4 (doi:10.6080/K0NS0S26, unversioned): the same 54 sessions as MATLAB structures
7	  in two tar.gz archives (``datafiles.tar.gz``), with the GoodTrials flag, the trial type
8	  matrix, the laser power trace of every trial and the unit waveforms, plus the lab's analysis
9	  scripts (``analyses_scripts.zip``). The archives are gzip streams, which cannot be opened in
10	  place, so each is read once from start to end over HTTP and every member is reduced in
11	  memory as it passes; nothing is written to disk. One archive (7.4 GB) takes about 6 minutes.
12	
13	Where the parameters come from (claims file ``claims/gao-2018.yaml``, shared methods B1 and
14	E1 to E6, cited there from the paper's Methods and legends):
15	
16	- Trials. Neural analyses use trials with GoodTrials = 1, a photostimulation code that is not
17	  NaN, no early lick, and inside the unit's stable range (its first to last trial with a
18	  spike). The paper's Methods give none of these; they are taken from the analysis scripts
19	  deposited with CRCNS:alm-4 (``analysis_compile_all_ALM_data.m`` and the other compile
20	  scripts), which the paper's reporting summary announces ("Custom analysis scripts and data
[... 310 more lines not kept]
```

**Agent calls Bash**

```bash
c=0c97448751a9a6fa09aba58d3812e7c159d5962d; c=$(git log -1 --format=%H -- attempts/gao-2018-01.yaml); echo $c; d=$TMPDIR/e01; mkdir -p $d; for f in $(git ls-tree --name-only $c entries/gao-2018/); do git show $c:$f > $d/$(basename $f); done; ls -la $d; git show $c:entries/gao-2018/entry.yaml
```

```
0c97448751a9a6fa09aba58d3812e7c159d5962d
total 308
drwxr-xr-x 2 runner runner   4096 Nov 14 17:38 .
drwx------ 6 runner runner   4096 Nov 14 17:38 ..
-rw-r--r-- 1 runner runner   3598 Nov 14 17:38 README.md
-rw-r--r-- 1 runner runner   1030 Nov 14 17:38 entry.yaml
-rw-r--r-- 1 runner runner  34001 Nov 14 17:38 gao2018.py
-rw-r--r-- 1 runner runner 105267 Nov 14 17:38 reproduce_gao_2018.ipynb
-rw-r--r-- 1 runner runner     79 Nov 14 17:38 requirements.in
-rw-r--r-- 1 runner runner 149001 Nov 14 17:38 requirements.lock.txt
schema_version: 1
name: gao-2018
type: reproduction
title: A cortico-cerebellar loop for motor planning (Gao et al. 2018)
description: Tests the findings of Gao, Davis, Thomas, Economo, Abrego, Svoboda, De Zeeuw and Li
  (2018) on its two deposits, DANDI:000007 and CRCNS:alm-4, which hold the same 54 ALM recording
  sessions of 13 mice during fastigial or dentate photo-activation and CN photo-inhibition. It
  tests the behavior in those sessions, ALM trial-type selectivity, ALM responses to CN
  photostimulation and the coding direction analysis. The lesion experiments, CN recordings, lick
  times, VGAT-ChR2 experiments and anatomy are not deposited.
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
git log --format='%h %ad %s' --date=iso -- attempts/gao-2018-01.yaml | head; echo; git show --stat HEAD | head -30; echo; git log --format='%h %ad %s' --date=iso -- entries/gao-2018/gao2018.py | head -20
```

```
0c97448 2026-11-14 17:28:50 +0000 Agent run on gao-2018: author-revise-3 (success)

commit 0c97448751a9a6fa09aba58d3812e7c159d5962d
Author: github-actions[bot] <github-actions[bot]@users.noreply.github.com>
Date:   Sat Nov 14 17:28:50 2026 +0000

    Agent run on gao-2018: author-revise-3 (success)
    
    Run: https://github.com/catalystneuro/encore/actions/runs/43619056457
    
    Account: verified

 .github/ISSUE_TEMPLATE/author-response.yml         |    88 +
 .github/ISSUE_TEMPLATE/run-request.yml             |    40 +
 .github/workflows/attempt-sequence.yml             |   138 +
 .github/workflows/attempt.yml                      |   510 +
 .github/workflows/check.yml                        |   182 +
 .github/workflows/colab.yml                        |    77 +
 .github/workflows/manifest.yml                     |    89 +
 .github/workflows/notify.yml                       |    66 +
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
d=$TMPDIR/e01; for f in gao2018.py reproduce_gao_2018.ipynb README.md; do cmp $d/$f entries/gao-2018/$f && echo same $f; done; wc -c entries/gao-2018/*; head -30 $d/gao2018.py; git status --short | head; ls transcripts/gao-2018/attempt-01 | head
```

```
same gao2018.py
same reproduce_gao_2018.ipynb
same README.md
  3598 entries/gao-2018/README.md
  1030 entries/gao-2018/entry.yaml
 34001 entries/gao-2018/gao2018.py
105267 entries/gao-2018/reproduce_gao_2018.ipynb
    79 entries/gao-2018/requirements.in
149001 entries/gao-2018/requirements.lock.txt
292976 total
"""Loading and measures for Gao et al. (2018), "A cortico-cerebellar loop for motor planning",
Nature 563, 113-116, doi:10.1038/s41586-018-0633-x, on its two datasets.

- DANDI:000007, version 0.220126.1903: 54 NWB files (13 mice) of ALM single units, a trial
  table and the photostimulation code of each trial. Streamed with remfile and h5py.
- CRCNS:alm-4 (doi:10.6080/K0NS0S26, unversioned): the same 54 sessions as MATLAB structures
  in two tar.gz archives (``datafiles.tar.gz``), with the GoodTrials flag, the trial type
  matrix, the laser power trace of every trial and the unit waveforms, plus the lab's analysis
  scripts (``analyses_scripts.zip``). The archives are gzip streams, which cannot be opened in
  place, so each is read once from start to end over HTTP and every member is reduced in
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; python tools/entry.py --help 2>&1 | head -30; python tools/entry.py run --help 2>&1 | head -30
```

```
Sat Nov 14 17:38:49 UTC 2026
usage: entry.py [-h] [--output-dir OUTPUT_DIR] [--timeout TIMEOUT]
                [--max-minutes MAX_MINUTES] [--fresh] [--python PYTHON]
                [--before BEFORE]
                {lock,check,run,all,handover,upgrade-python,hash}
                entry [entry ...]

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
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/gao-2018/attempt-01; grep -n "locked\|lock_check\|def clock\|shuffle" author*.md | cut -c1-300 | head -40
```

```
author-answers-report.md:5:**Per question and claim:** none. All 45 outcomes stand as `attempts/gao-2018-01.yaml` records them: 18 tested and 27 blocked.
author-answers-report.md:9:- 26 blocked with `data_missing` and 1 (fig2cd) with `methods_underspecified`.
author-answers.md:124:215:    one epoch the defensible choice, so the claim is blocked; the question is a methods_unavailable finding.
author-answers.md:127:218-  outcome: blocked
author-answers.md:128:219-  blocked_by: data_missing
author-answers.md:131:222-  outcome: blocked
author-answers.md:132:223-  blocked_by: data_missing
author-answers.md:291:**Per question and claim:** none. All 45 outcomes stand as `attempts/gao-2018-01.yaml` records them: 18 tested and 27 blocked.
author-answers.md:295:- 26 blocked with `data_missing` and 1 (fig2cd) with `methods_underspecified`.
author-report.md:1:I finished steps 1 to 5 and ran `handover`. Of the 45 claims, 18 were tested and 27 are blocked. The entry check passes with 0 errors and the notebook runs from a clean environment in 465 s (about 7.8 min). Nothing is committed.
author-report.md:13:| fig2cd-selectivity-emerges-gradually | blocked, methods_underspecified |
author-report.md:26:| 26 others: lesions, CN recordings, licking, other stimulation epochs, VGAT-ChR2 mice, anatomy | blocked, data_missing |
author-revise-1-report.md:7:| fig2cd-selectivity-emerges-gradually | blocked, methods underspecified | partially reproduced | Agrees with the verifier. The paper says the epoch that fixes each neuron's preference doesn't matter, but the response-epoch peak appears with only one of the three epochs. 
author-revise-1-report.md:12:The totals are now 9 reproduced, 6 partially reproduced, 4 not reproduced and 26 blocked.
author-revise-1-report.md:26:- **fig1l early licks (B10):** now tested, with no change (two-sided p = 0.59). The claim stays blocked because lick rates and video aren't in the files.
author-revise-1.md:17:| fig1d-fastigial-lesion-contra-choice | blocked 
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/gao-2018/attempt-01; grep -n "clock" author.md | cut -c1-400 | head -30
```

```
951: "content": "# %% [markdown]\n# ## Data check\n#\n# What was loaded, by subject, session and photostimulation code; the units; the event times; what the\n# undocumented `photo_stim_id` codes are; and whether the spikes share the clock of the trials table.\n\n# %% tags=[\"sanity\"]\nrows = []\nfor s, p in zip(S, P):\n    t = g.add_trial_fields(s.trials)\n    w = g.spike_width_ms(s.waveforms, s.
1585: "content": "# %% [markdown]\n# ## Summary\n#\n# A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the\n# differences from the paper's method.\n#\n# | claim | outcome |\n# |---|---|\n# | fig1g-fastigial-activation-early-sample-no-effect | reproduced |\n# | fig1g-fastigial-activation-delay-errors | reproduced |\n# | fig1h-fastigial-activation
1834: "content": "import yaml\n\nNB = \"reproduce_gao_2018.ipynb\"\nCODES = (\"The photostimulation codes are not described in the files; codes 1 and 3 are read as early sample \"\n         \"and 2 and 4 as early delay photo-activation, 5 and 6 as delay photo-inhibition, from the onset of \"\n         \"the ALM response and the sessions' ogen sites (data check).\")\nREC = \"Tested on the ALM recor
2067:- The event-time columns are described as relative to trial start but are on the session clock.
2072:- In 5 sessions I could not show that spikes share the trial clock.
```

**Agent calls Bash**

```bash
cd transcripts/gao-2018/attempt-01; sed -n 951p author.md | python -c "import sys,json; s=sys.stdin.read(); i=s.find('\"content\": '); print(json.loads('{'+s[i:].rstrip().rstrip(',')+'}')['content'] if False else s.encode().decode('unicode_escape')[:9000])"
```

```
"content": "# %% [markdown]
# ## Data check
#
# What was loaded, by subject, session and photostimulation code; the units; the event times; what the
# undocumented `photo_stim_id` codes are; and whether the spikes share the clock of the trials table.

# %% tags=["sanity"]
rows = []
for s, p in zip(S, P):
    t = g.add_trial_fields(s.trials)
    w = g.spike_width_ms(s.waveforms, s.wf_rate)
    rows.append(dict(subject=s.subject, session=s.path.split("_ses-")[1][:15], genotype=s.genotype,
                     site=s.site, site_hemisphere=s.site_hemisphere, rec_ml=s.rec_ml, group=p.group,
                     trials=len(t), lick_early=int(t.lick_early.sum()), units=s.n_units,
                     pyr_width=int((w > g.PYR_MIN_MS).sum()), fs_width=int((w < g.FS_MAX_MS).sum()),
                     pyr_file=int((s.cell_type == "pyramidal").sum()),
                     codes=",".join(f"{k}:{v}" for k, v in t.stim.value_counts().sort_index().items())))
D = pd.DataFrame(rows)
print(D.to_string())
by = D.groupby(["group", "subject"]).agg(sessions=("session", "size"), trials=("trials", "sum"),
[... 124 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/gao-2018/attempt-01; grep -n "15 of 20\|draws\|def pref\|n_pref\|PREF" author*.md | cut -c1-250 | head -30
```

```
author-revise-1-report.md:21:- **fig3f, repeated over 20 random draws (B2):** in the last 500 ms the criterion is met in 15 of 20 draws with 5 preference trials of each type, and 13 of 20 with 10 of each. It stays reproduced, and is no longer marked 
author-revise-1.md:1074:                held[(per_type, epoch)].append(g.pop_selectivity(rates, prefc, rng_h, g.PREF_TRIALS_ALM, per_type)[2])
author-revise-1.md:1098:# --- fig3f: repeat over draws
author-revise-1.md:1102:# The preference trials are a random draw, so each reading is repeated over 20 draws: how many meet the
author-revise-1.md:1114:print(REP3F.groupby(["pref", "window"]).agg(draws=("seed", "size"), reproduced=("reproduced", "sum"),
author-revise-1.md:1205:print("fig3f, 5 of each type, 20 draws:\\n", pd.DataFrame(rep).groupby("window").agg(
author-revise-1.md:1450:                          draws  reproduced  photo_min  photo_max  photo_lo_min  photo_lo_max  control_lo_min
author-revise-1.md:1511:n.setsrc(nb, i, n.src(C[i]).rstrip() + " The preference trials\nare a random draw, so each reading is repeated over 20 draws and judged by how many meet the criterion.\n")
author-revise-1.md:1512:setmd("**Result: reproduced, resting on an assumption.** Over 430", """**Result: reproduced.** Over 438 selective neurons tested on more than 3 trials in all conditions (456 selective; paper 329), the last 500 ms of the delay 
author-revise-1.md:1549:n.replace_in(nb,i,"The photo-inhibition selectivity varies widely between draws (-0.179 to 0.695 spikes/s), so a single draw does not settle it.",
author-revise-1.md:1550: "In the last 500 ms the photo-inhibition selectivity varies widely between draws (-0.179 to 0.611 spikes/s with 5 of each type, -0.076 to 0.695 with 10), so a single draw does not settle it.")
author-revise-1.md:1574:"| fig3f-alm-selectivity-abolished-by-cn-inhibition | reproduced, assumed |":"| fig3f-alm-selectivity-abolished-by-cn-inhibition | reproduced (most draws, last 500 ms) |",
author-revise-1.md:19
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import yaml
a=yaml.safe_load(open('attempts/gao-2018-01.yaml'));b=yaml.safe_load(open('attempts/gao-2018-02.yaml'))
oa={o['claim']:o for o in a['outcomes']}; ob={o['claim']:o for o in b['outcomes']}
print(len(oa),len(ob), set(oa)-set(ob), set(ob)-set(oa))
for k in ob:
    if k in oa:
        x,y=oa[k],ob[k]
        if (x['outcome'],x.get('blocked_by'))!=(y['outcome'],y.get('blocked_by')):
            print('DIFF',k,x['outcome'],x.get('blocked_by'),'->',y['outcome'],y.get('blocked_by'))
for k in ['fig2cd-selectivity-emerges-gradually','fig3f-alm-selectivity-abolished-by-cn-inhibition']:
    print('\n##',k); print(yaml.safe_dump(ob.get(k),width=110)[:3000])
print(b.keys()); print(b.get('deviations','')[:0] if isinstance(b.get('deviations'),list) else '')
EOF
```

```
45 46 set() {'ed10b-fastigial-activation-errors-during-recording'}
DIFF fig1g-dentate-activation-little-effect reproduced None -> partially_reproduced None
DIFF fig1k-inhibition-delay-bias partially_reproduced None -> reproduced None
DIFF fig2-preparatory-more-in-alm blocked data_missing -> partially_reproduced None
DIFF fig2-peri-movement-equal blocked data_missing -> partially_reproduced None
DIFF fig3e-alm-mean-rate-unchanged partially_reproduced None -> reproduced None
DIFF fig3e-alm-increase-decrease partially_reproduced None -> not_reproduced None
DIFF fig3f-alm-selectivity-abolished-by-cn-inhibition reproduced None -> not_reproduced None
DIFF fig4g-dentate-effect-recovers not_reproduced None -> partially_reproduced None
DIFF fig4i-fastigial-collapses-cd reproduced None -> partially_reproduced None

## fig2cd-selectivity-emerges-gradually
claim: fig2cd-selectivity-emerges-gradually
deviations:
- CN half not deposited.
- Preferred type from 10 correct control trials of each type and neurons with more than 15 trials of each type,
  from the deposited Fig. 2 script; PSTHs with its 200 ms boxcar, on a 10 ms grid.
notebook: reproduce_gao_2018.ipynb
notes: 'ALM, reading (a), 827 selective neurons: the bootstrap interval excludes zero from 0.13 s after sample onset
  (117 of 129 sample-epoch points), the mean is 0.65 spikes/s in the sample, 1.80 in the delay and 1.91 in the response
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import yaml
c=yaml.safe_load(open('claims/gao-2018.yaml'))
print(c.keys())
for k,v in c.items():
    if k not in ('claims',): print(k, str(v)[:200])
sm=c.get('shared_methods') or c.get('methods')
for cl in c['claims']:
    if cl['id'] in ('fig3f-alm-selectivity-abolished-by-cn-inhibition','fig2cd-selectivity-emerges-gradually'):
        print(yaml.safe_dump({k:cl[k] for k in ('id','criterion') if k in cl},width=110))
EOF
```

```
dict_keys(['schema_version', 'paper', 'claims', 'checks'])
schema_version 2
paper doi:10.1038/s41586-018-0633-x
checks [{'date': datetime.date(2026, 11, 14), 'kind': 'agent', 'model': 'claude-opus-5-5', 'ready': True, 'changes': ['fig1e-fastigial-lesion-slow-initiation. The statement said contralesional first licks co
criterion: Population selectivity as E3 over selective neurons. The Fig. 2 legend, which gives the neurons averaged,
  is not in the text read, so the population is open (readings (a) all selective neurons, ALM 980 and CN 416; (b)
  those with significant sample or delay selectivity). The per-nucleus counts of Extended Data Fig. 4f (87 + 50
  + 60 = 197) equal 35% of 564, the CN preparatory fraction, which supports (b) for the CN. Reproduced in a region
  when, under one reading, the bootstrap 95% interval over neurons excludes zero in at least one window of the sample
  epoch, the mean over the delay epoch exceeds the mean over the sample epoch, and the maximum of the time course
  lies in the response epoch.
id: fig2cd-selectivity-emerges-gradually

criterion: Population selectivity as E3 (preferred type from 10 trials) over selective ALM neurons tested on > 3
  trials in all conditions (the selection of the Extended Data Fig. 5b and 9c legends; the Fig. 3f count is not
  in the text read), control against CN photo-inhibition trials, all trials grouped by instructed type. Window readings
  as in fig3c-cn-selectivity-abolished. Reproduced when under one reading the control selectivity is above zero
  (bootstrap 95% interval over neurons) and the photo-inhibition selectivity is not distinguishable from zero. The
  neuron count is reported.
id: fig3f-alm-selectivity-abolished-by-cn-inhibition
```

**Agent calls Bash**

```bash
grep -n "E3\b\|E3 " claims/gao-2018.yaml | head -5; grep -n "^  - id: E3\|id: E3" -A12 claims/gao-2018.yaml | head -30; python -c "
import yaml;c=yaml.safe_load(open('claims/gao-2018.yaml'))
for ch in c['checks']: print(ch['date'], ch.get('kind'), ch.get('model'), ch.get('ready')); [print('  -',x[:400]) for x in ch.get('changes',[])]
"
```

```
95:#  E3 Population selectivity (Methods; Extended Data Fig. 4f legend). Each neuron's preferred
544:  criterion: Population selectivity as E3 over selective neurons. The Fig. 2 legend, which gives
588:  criterion: Population selectivity as E3 for each nucleus (Extended Data Fig. 4f, mean and s.e.m.
681:  criterion: Population selectivity as E3 over selective CN neurons tested on > 3 trials in all
698:  criterion: Population selectivity as E3 over the n = 157 neurons of Extended Data Fig. 6c, delay
2026-11-14 agent claude-opus-5-5 True
  - fig1e-fastigial-lesion-slow-initiation. The statement said contralesional first licks come later than ipsilesional ones; the paper says only that lesions "slowed initiation of contralesional licking", without the comparison. Restated as the paper has it, and the criterion now names the readings (after against before the lesion; contra- against ipsilesional after it).
  - fig1h-fastigial-activation-response-contra-bias, fig1k-inhibition-response-ipsi-bias. The criteria required the drop on the other trial type to be not significant, a condition the paper does not state. A bias is now judged as the larger drop on the trial type the paper names, with the significance of the other reported.
  - ed4g-fastigial-contra-late-delay. The Extended Data Fig. 4g legend gives p=0.0001 without saying what is compared; named the readings (against one half, against the first 500 ms) and said that the test of "equal numbers" in the early delay is this file's choice. Added an about to the statistic.
  - Header E3. It said the epoch choice gave "qualitatively similar results"; the Methods say "qualitatively similar preparatory activity". Quoted the Methods (also asked in questions/gao-2018.yaml).
  - Header, data. It said the 1309 ALM units of 10 mice were recorded with CN ChR2 photo-activation; the Methods say 9 of the 10 mice were. Removed the qualifier.
  - fig1j-photoinhibition-silences-fastigial. Said that the majority rule is this file's choice
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import yaml
a=yaml.safe_load(open('attempts/gao-2018-01.yaml'));b=yaml.safe_load(open('attempts/gao-2018-02.yaml'))
print(a['datasets']); print(a.get('missing_datasets'))
oa={o['claim']:o for o in a['outcomes']}; ob={o['claim']:o for o in b['outcomes']}
for k in ['fig1g-dentate-activation-little-effect','fig1k-inhibition-delay-bias','fig2-preparatory-more-in-alm','fig2-peri-movement-equal','fig3e-alm-mean-rate-unchanged','fig3e-alm-increase-decrease','fig3f-alm-selectivity-abolished-by-cn-inhibition','fig4g-dentate-effect-recovers','fig4i-fastigial-collapses-cd']:
    for lab,o in (('01',oa[k]),('02',ob[k])):
        print(f'\n## {k} [{lab}] {o["outcome"]} assumed={o.get("assumed")}')
        print('notes:',o.get('notes'))
        print('dev:',o.get('deviations'))
        print('measured:',o.get('measured'))
EOF
```

```
[{'archive': 'dandi', 'id': '000007', 'version': '0.220126.1903', 'doi': '10.48324/dandi.000007/0.220126.1903', 'relation': 'primary'}]
None

## fig1g-dentate-activation-little-effect [01] reproduced assumed=None
notes: Reading (a), early delay (code 4), 3 dentate mice and 13 sessions. Pooled performance 0.873 against 0.835 (change -0.038), one-sided p = 0.108, so no drop at p < 0.05 (paper p = 0.06). Ipsi trials alone drop by 0.063 (p = 0.041), contra by 0.013 (p = 0.45). The outcome rests on 3 of the paper's 8 mice. Without anm00314756 20151023 (clock check) the change is -0.037, p = 0.157. The verifier notes that the hierarchical bootstrap is conservative, which favours a claim of absence such as this one.
dev: ["The photostimulation codes are not described in the files; codes 1 and 3 are read as early sample and 2 and 4 as early delay photo-activation, 5 and 6 as delay photo-inhibition, from the onset of the ALM response and the sessions' ogen sites (data check).", "Tested on the ALM recording sessions, the only behavior in the dataset; the paper's behavior may include other sessions.", "3 of the paper's 8 dentate mice (NL12, NL14 and anm00314756, which is AN106 by its site); reading (b), the 1.255 s stimulus, is not in the dataset."]
measured: None

## fig1g-dentate-activation-little-effect [02] partially_reproduced assumed=None
notes: Reading (a), early delay dentate photo-activation (code 4) in the 3 recorded dentate mice. On all 13 sessions pooled performance goes from 0.873 to 0.835 (change -0.039, one-sided bootstrap p = 0.107, paper p = 0.06), so the criterion's test finds no drop at p < 0.05; contralateral -0.055 (p = 0.09), ipsilateral -0.019 (p = 0.42). Without ANM314756_20151020 and BAYLORNL14_20170603, whose laser traces disagree with code 4 (0.78 s of light; 61% of code 4 trials lit at sample onset), it finds a drop (0.876 to 0.824, change -0.052, p = 0.042), and the trial-level checks find one on all sessions (z-test p = 0.007, stratified p = 0.016
[... 82 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; grep -n "^#" docs/pilot-notes.md | head -60
```

```
Sat Nov 14 17:39:37 UTC 2026
1:# Pilot notes
16:## Protocol pilot-3 (2026-10-13)
59:## Protocol pilot-4 (2026-10-14)
88:## Protocol pilot-5 (2026-10-14)
113:## Protocol pilot-6 (2026-10-14), at the end of the pilot
138:## After the pilot: the first batch (2026-10-14)
156:## Protocol pilot-7 (2026-10-15): data in other archives
218:## Protocol pilot-8 (2026-10-19): the paper's own words
281:## Protocol pilot-9 (2026-10-20): the full text or nothing
320:## Protocol pilot-10 (2026-10-20): the reader and the author
381:## Protocol pilot-12 (2026-10-27): blind repeat attempts
403:## Protocol pilot-13 (2026-10-31): a notebook may take an hour
414:## Protocol pilot-14 (2026-11-09): papers first, and every dataset a paper rests on
```

**Agent calls Bash**

```bash
sed -n 414,600p docs/pilot-notes.md; grep -n "pilot-15" -r docs | head
```

```
## Protocol pilot-14 (2026-11-09): papers first, and every dataset a paper rests on

Records were filed by dataset, so a paper whose data are split across dandisets
(Semenov 2026 on 7, Churchland 2010 on 4) was tested once per dandiset, each
time with its own claims, and a paper that reuses a dataset had nowhere to go.
Records are now filed by paper (docs/paper-first.md): one claims file for the
paper, claims naming their datasets only when there are several, and one
attempt that uses as many of the paper's datasets as can be loaded. A dataset
it could not use is listed under `missing_datasets`, and the claims that need
it are blocked with `dataset_missing`, so that a later attempt can add it.
docs/protocol.md:3:Version: `pilot-15`. Record this version in the attempt's provenance.
```

**Agent calls Bash**

```bash
ls docs; ls docs/pilot-notes 2>/dev/null | head; grep -rln "pilot-15\|pilot 15" docs tools schemas README.md 2>/dev/null | head; sed -n 1,15p docs/protocol.md
```

```
agents
archives.md
author-responses.md
badges.md
conversion-tracker.md
design.md
encore.md
fixing-conversions.md
paper-first.md
pilot-notes
pilot-notes.md
pipeline.md
protocol.md
queue.md
amjad-2025-01.md
andrews-2024-01.md
armstrong-2026-01.md
asari-2009-01.md
ashworth-2025-01.md
athalye-2023-01.md
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "pilot-15\|pilot-14" tools/entry.py | head; sed -n 1,15p docs/pilot-notes.md
```

```
331:        # The rule is the protocol's from pilot-15. An attempt made under an earlier version is not held to it: its
# Pilot notes

What each pilot attempt taught about the process. These feed the revision of
the schemas and the design after the pilot (docs/design.md, "Phasing").

The notes on each attempt are in [`pilot-notes/`](pilot-notes), one file per
attempt, named by its record. The lists below link those written before
2026-10-22, under the protocol version they ran under; the recorder adds a file
for each attempt since, and does not change this page.

- [000582, Sargolini et al. 2006 (2026-10-13)](pilot-notes/sargolini-2006-01.md)
- [000127, Chowdhury, Glaser & Miller 2020 (2026-10-13)](pilot-notes/chowdhury-2020-01.md)
- [000207, Zheng et al. 2022 (2026-10-13): first attempt by an agent following the protocol](pilot-notes/zheng-2022-01.md)
- [000147, Guan et al. 2022 (2026-10-13): second attempt by an agent following the protocol](pilot-notes/guan-2022-01.md)
```

**Agent calls Bash**

```bash
sed -n 320,345p tools/entry.py
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
        for n, f in enumerate(attempt.get("findings") or [], 1):
            if told and f.get("kind") in ("other", "selection_undocumented") and not f.get("about"):
                report.error(where, f"finding {n} ({f.get('kind')}): say what it is about, `about: data` or `about: paper`")
            about = f.get("about") or ("paper" if f.get("kind") in ("methods_unavailable", "code_mismatch",
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && timeout 300 python - <<'EOF'
import requests, h5py, remfile, json
r=requests.get("https://api.dandiarchive.org/api/dandisets/000007/versions/0.220126.1903/assets/?page_size=200",timeout=60).json()
A=[a for a in r['results'] if a['path'].endswith('.nwb')]
print(len(A)); print([a['path'] for a in A][:60])
a=[x for x in A if 'BAYLORCD8' in x['path']][0]
url=requests.head(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/",allow_redirects=True,timeout=60).url
f=h5py.File(remfile.File(url),'r')
def show(n,o):
    if isinstance(o,h5py.Dataset): print(n,o.shape,o.dtype, dict(o.attrs).get('description','') if 'description' in o.attrs else '')
    else: print(n+'/', {k:(v if not hasattr(v,'shape') or v.size<5 else '...') for k,v in o.attrs.items() if k not in ('namespace','object_id')})
f.visititems(show)
for k in ['session_description','identifier','session_start_time']:
    print(k, f[k][()])
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
cd  cat entries/gao-2018/requirements.in; ls -d executed 2>/dev/null; ls ~/.cache 2>/dev/null | head; which uv python3; python --version
```

```
fsspec
aiohttp
requests
h5py
remfile
numpy
pandas
scipy
statsmodels
matplotlib
/opt/hostedtoolcache/Python/3.13.18/x64/bin/uv
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python3
Python 3.13.18
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q -p 3.13 venv && VIRTUAL_ENV=$TMPDIR/venv uv pip install -q -r entries/gao-2018/requirements.lock.txt 2>&1 | tail -3; VIRTUAL_ENV=$TMPDIR/venv uv pip install -q ipykernel nbformat nbclient 2>&1|tail -2; ls venv/bin | head
```

```
activate
activate.bat
activate.csh
activate.fish
activate.nu
activate.ps1
activate.xsh
activate_this.py
deactivate.bat
debugpy
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && timeout 600 venv/bin/python - <<'EOF'
import requests, h5py, remfile, json
r=requests.get("https://api.dandiarchive.org/api/dandisets/000007/versions/0.220126.1903/assets/?page_size=200",timeout=60).json()
A=[a for a in r['results'] if a['path'].endswith('.nwb')]
print(len(A)); print(sorted(set(a['path'].split('/')[0] for a in A)))
a=[x for x in A if 'BAYLORCD8' in x['path']][0]; print(a['path'])
url=requests.head(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/",allow_redirects=True,timeout=60).url
f=h5py.File(remfile.File(url),'r')
def show(n,o):
    if isinstance(o,h5py.Dataset):
        v = o[()] if o.size<3 else ''
        print(n,o.shape,o.dtype, o.attrs.get('description',''), v)
    else: print(n+'/', {k:v for k,v in o.attrs.items() if k not in ('namespace','object_id','colnames')})
f.visititems(show)
EOF
```

```
<persisted-output>
Output too large (119.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/1ffb9917-0eea-44ac-9742-0341fbab9e78/tool-results/byy9zqkdk.txt

Preview (first 2KB):
54
['sub-BAYLORCD12', 'sub-BAYLORCD13', 'sub-BAYLORCD14', 'sub-BAYLORCD6', 'sub-BAYLORCD8', 'sub-BAYLORNL12', 'sub-BAYLORNL14', 'sub-BAYLORNL15', 'sub-anm00314746', 'sub-anm00314756', 'sub-anm00314757', 'sub-anm00314758', 'sub-anm00314760']
sub-BAYLORCD8/sub-BAYLORCD8_ses-20171016T121417.nwb
acquisition/ {}
analysis/ {}
file_create_date (1,) object  [b'2020-03-24T23:06:25.294453+00:00']
general/ {}
general/devices/ {}
general/devices/Cambridge NeuroTech 64ch H2 probe/ {'neurodata_type': 'Device'}
general/devices/fiber/ {'neurodata_type': 'Device'}
general/experiment_description () object  b'Extracelluar recording in ALM'
general/experimenter (1,) object  [b'Nuo Li']
general/extracellular_ephys/ {}
general/extracellular_ephys/Cambridge NeuroTech 64ch H2 probe_g1/ {'description': 'N/A', 'location': '{"probe_type": "Cambridge NeuroTech 64ch H2 probe", "rec_coordinate_ap": "2.5", "rec_coordinate_ml": "-1.5", "rec_coordinate_dv": "None", "ground_coordinate_ap": "-3.0", "ground_coordinate_ml": "-1.0", "ground_coordinate_dv": "1.0", "rec_marker": "stereotaxic", "spike_sorting_method": "manual", "ad_unit": "14 bits", "coordinate_ref": "lambda", "penetration_num": "1"}', 'neurodata_type': 'ElectrodeGroup'}
general/extracellular_ephys/electrodes/ {'description': 'metadata about extracellular electrodes', 'neurodata_type': 'DynamicTable'}
general/extracellular_ephys/electrodes/filtering (64,) object description of hardware filtering 
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
f=/home/runner/.claude/projects/-home-runner-work-encore-encore/1ffb9917-0eea-44ac-9742-0341fbab9e78/tool-results/byy9zqkdk.txt; grep -v "^units/spike_times\b" $f | grep -v "electrodes/" | cut -c1-400 | head -80
```

```
54
['sub-BAYLORCD12', 'sub-BAYLORCD13', 'sub-BAYLORCD14', 'sub-BAYLORCD6', 'sub-BAYLORCD8', 'sub-BAYLORNL12', 'sub-BAYLORNL14', 'sub-BAYLORNL15', 'sub-anm00314746', 'sub-anm00314756', 'sub-anm00314757', 'sub-anm00314758', 'sub-anm00314760']
sub-BAYLORCD8/sub-BAYLORCD8_ses-20171016T121417.nwb
acquisition/ {}
analysis/ {}
file_create_date (1,) object  [b'2020-03-24T23:06:25.294453+00:00']
general/ {}
general/devices/ {}
general/devices/Cambridge NeuroTech 64ch H2 probe/ {'neurodata_type': 'Device'}
general/devices/fiber/ {'neurodata_type': 'Device'}
general/experiment_description () object  b'Extracelluar recording in ALM'
general/experimenter (1,) object  [b'Nuo Li']
general/extracellular_ephys/ {}
general/extracellular_ephys/Cambridge NeuroTech 64ch H2 probe_g1/ {'description': 'N/A', 'location': '{"probe_type": "Cambridge NeuroTech 64ch H2 probe", "rec_coordinate_ap": "2.5", "rec_coordinate_ml": "-1.5", "rec_coordinate_dv": "None", "ground_coordinate_ap": "-3.0", "ground_coordinate_ml": "-1.0", "ground_coordinate_dv": "1.0", "rec_marker": "stereotaxic", "spike_sorting_method": "manual", "a
general/institution () object  b'Janelia Research Campus'
general/keywords (5,) object  
general/optogenetics/ {}
general/optogenetics/Fastigial/ {'neurodata_type': 'OptogeneticStimulusSite'}
general/optogenetics/Fastigial/description () object  b''
general/optogenetics/Fastigial/excitation_lambda () float64  473.0
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/work && cat > $TMPDIR/work/load.py <<'EOF'
import json, requests, h5py, remfile, numpy as np, pandas as pd
from concurrent.futures import ThreadPoolExecutor
DANDISET_ID, DANDISET_VERSION = "000007", "0.220126.1903"
def _s(x):
    return x.decode() if isinstance(x, bytes) else str(x)
def _one(asset):
    url = requests.head(f"https://api.dandiarchive.org/api/assets/{asset['asset_id']}/download/",
                        allow_redirects=True, timeout=60).url
    with h5py.File(remfile.File(url), "r") as f:
        tr = f["intervals/trials"]
        trials = pd.DataFrame({k: tr[k][:] for k in ["start_time", "stop_time", "pole_in_time", "pole_out_time",
                                                     "cue_time", "lick_early", "response", "photo_stim_id"]})
        for k in ("response", "photo_stim_id"):
            trials[k] = trials[k].map(_s)
        u = f["units"]
        st, idx = u["spike_times"][:], u["spike_times_index"][:]
        oi, oidx = u["obs_intervals"][:], u["obs_intervals_index"][:]
        sub = f["general/subject"]
        out = dict(
            path=asset["path"], subject=_s(sub["subject_id"][()]),
            subject_fields={k: _s(sub[k][()]) for k in sub},
            session_description=_s(f["session_description"][()]),
            trials=trials, trial_descr={k: _s(tr[k].attrs.get("description", "")) for k in tr},
            spikes=np.split(st, idx[:-1]), obs=np.split(oi, oidx[:-1]),
            cell_type=u["cell_type"][:].astype(str), wf_rate=u["sampling_rate"][:],
            waveform=u["waveform_mean"][:],
            devices=list(f["general/devices"]),
            egroups={k: json.loads(f[f"general/extracellular_ephys/{k}"].attrs.get("location", "{}"))
                     for k in f["general/extracellular_ephys"] if k != "electrodes"},
            ogen={k: json.loads(_s(f[f"general/optogenetics/{k}/location"][()]) or "{}")
                  for k in f["general/optogenetics"]},
            acquisition=list(f["acquisition"]), stimulus=list(f["stimulus/presentation"]) + list(f["stimulus/templates"]),
            processing=list(f["processing"]))
    out["session"] = asset["path"].split("_ses-")[1][:8]
    return out
def load(n=None):
    r = requests.get(f"https://api.dandiarchive.org/api/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}"
                     "/assets/?page_size=200", timeout=60).json()
    assets = sorted([a for a in r["results"] if a["path"].endswith(".nwb")], key=lambda a: a["path"])[:n]
    with ThreadPoolExecutor(8) as ex:
        return list(ex.map(_one, assets))
EOF
cd $TMPDIR/work && time timeout 900 ../venv/bin/python -c "
import load,pickle,time,resource
S=load.load()
pickle.dump(S,open('S.pkl','wb'))
print(len(S), resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,'GB')
s=S[0]; print(s['path'], s['waveform'].shape, s['wf_rate'][:3], s['devices'], s['subject_fields'], s['acquisition'], s['stimulus'], s['processing'])
"
```

```
54 0.5574 GB
sub-BAYLORCD12/sub-BAYLORCD12_ses-20180125T191601.nwb (20, 30) [20000 20000 20000] ['Cambridge NeuroTech 64ch H2 probe', 'fiber'] {'date_of_birth': '2017-05-24T00:00:00+00:00', 'genotype': 'L7-cre x rosa26-lsl-ChR2-EYFP', 'sex': 'M', 'species': 'Mus musculus', 'subject_id': 'BAYLORCD12'} [] [] []

real	0m57.161s
user	0m3.317s
sys	0m0.791s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/work && timeout 900 ../venv/bin/python - <<'EOF'
import pickle, numpy as np, pandas as pd, collections
S=pickle.load(open('S.pkl','rb'))
# E2
print("photo_stim_id descriptions:", collections.Counter(s['trial_descr']['photo_stim_id'] for s in S))
print("acquisition/stimulus/processing non-empty:", [s['path'] for s in S if s['acquisition'] or s['stimulus'] or s['processing']])
for s in S:
    s['site']=list(s['ogen'])[0] if s['ogen'] else ''
codes=collections.defaultdict(set)
for s in S: codes[(s['site'],s['subject_fields']['genotype'])] |= set(s['trials'].photo_stim_id)
print(dict(codes))
# E5
D=pd.DataFrame([dict(subject=s['subject'],session=s['session'],genotype=s['subject_fields'].get('genotype'),desc=s['session_description'],fields=','.join(sorted(s['subject_fields']))) for s in S])
print(D.groupby('subject').agg(n=('session','size'),genotype=('genotype','first'),desc_empty=('desc',lambda x:(x=='').sum()),fields=('fields','first')))
for s in S:
    if s['subject'].startswith('anm'): print(s['subject'], s['subject_fields'], s['ogen'], [g['rec_coordinate_ml'] for g in s['egroups'].values()]); 
# E7
def width(wf, rate):
    tr=np.argmin(wf); pk=tr+np.argmax(wf[tr:]); return (pk-tr)/rate*1000
rows=[]
for s in S:
    probe=[g['probe_type'] for g in s['egroups'].values()][0]
    for i in range(len(s['cell_type'])):
        rows.append(dict(subject=s['subject'],session=s['session'],probe=probe,rate=s['wf_rate'][i],n=s['waveform'].shape[1],cell_type=s['cell_type'][i],w=width(s['waveform'][i],s['wf_rate'][i])))
W=pd.DataFrame(rows)
W['by_width']=np.where(W.w>0.45,'>0.45',np.where(W.w<0.35,'<0.35','0.35-0.45'))
print(pd.crosstab(W.cell_type,W.by_width,margins=True))
print(W.groupby('probe').agg(sessions=('session',lambda x: x.nunique()), rates=('rate',lambda x: sorted(set(x))), nsamp=('n',lambda x: sorted(set(x)))))
print(W.w.describe())
# E9
s=[s for s in S if s['subject']=='BAYLORCD8' and s['session']=='20171020'][0]
ends=np.array([o[:,1].max() for o in s['obs']]); starts=np.array([o[:,0].min() for o in s['obs']])
t=s['trials']; allsp=np.concatenate(s['spikes'])
print('obs end range', ends.min(), ends.max(), 'last spike', allsp.max(), 'n trials', len(t), 'trial start range', t.start_time.min(), t.start_time.max())
after=t.start_time>ends.max(); print('trials starting after obs end', after.sum(), t.start_time[after].min(), t.stop_time[after].max())
nsp=[((allsp>=a)&(allsp<b)).sum() for a,b in zip(t.start_time[after],t.stop_time[after])]; print('spikes in them', sum(nsp))
EOF
```

```
photo_stim_id descriptions: Counter({'varchar(8) #': 54})
acquisition/stimulus/processing non-empty: []
{('Fastigial', 'L7-cre x rosa26-lsl-ChR2-EYFP'): {'6', '0', '5'}, ('Fastigial', 'unknown'): {'2', '0', '1'}, ('Dentate', 'unknown'): {'4', '3', '0'}}
             n  ...                                         fields
subject         ...                                               
BAYLORCD12   5  ...  date_of_birth,genotype,sex,species,subject_id
BAYLORCD13   5  ...  date_of_birth,genotype,sex,species,subject_id
BAYLORCD14   5  ...  date_of_birth,genotype,sex,species,subject_id
BAYLORCD6    4  ...  date_of_birth,genotype,sex,species,subject_id
BAYLORCD8    5  ...  date_of_birth,genotype,sex,species,subject_id
BAYLORNL12   5  ...  date_of_birth,genotype,sex,species,subject_id
BAYLORNL14   6  ...  date_of_birth,genotype,sex,species,subject_id
BAYLORNL15   5  ...  date_of_birth,genotype,sex,species,subject_id
anm00314746  3  ...  date_of_birth,genotype,sex,species,subject_id
anm00314756  2  ...  date_of_birth,genotype,sex,species,subject_id
anm00314757  2  ...  date_of_birth,genotype,sex,species,subject_id
anm00314758  4  ...  date_of_birth,genotype,sex,species,subject_id
anm00314760  3  ...  date_of_birth,genotype,sex,species,subject_id

[13 rows x 4 columns]
[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/work && ../venv/bin/python - <<'EOF'
import pickle, collections
S=pickle.load(open('S.pkl','rb'))
print(collections.Counter(tuple(s['devices']) for s in S))
print(collections.Counter(tuple(g['probe_type'] for g in s['egroups'].values()) for s in S))
print(collections.Counter((tuple(g['probe_type'] for g in s['egroups'].values()), s['waveform'].shape[1]) for s in S))
EOF
```

```
Counter({('NN 32ch A4x8-5mm-100-200-177', 'fiber'): 34, ('Cambridge NeuroTech 64ch H2 probe', 'fiber'): 20})
Counter({('NN 32ch A4x8-5mm-100-200-177',): 34, ('Cambridge NeuroTech 64ch H2 probe',): 20})
Counter({(('Cambridge NeuroTech 64ch H2 probe',), 30): 20, (('NN 32ch A4x8-5mm-100-200-177',), 30): 20, (('NN 32ch A4x8-5mm-100-200-177',), 37): 12, (('NN 32ch A4x8-5mm-100-200-177',), 38): 2})
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/work && ../venv/bin/python - <<'EOF'
import pickle, numpy as np, pandas as pd
from scipy import stats
S=pickle.load(open('S.pkl','rb'))
print(pd.DataFrame([(s['subject'],s['subject_fields']['genotype']) for s in S]).drop_duplicates().to_string())
print('empty session_description', sum(s['session_description']=='' for s in S))
def counts(sp, a, b):
    i0=np.searchsorted(sp,a); i1=np.searchsorted(sp,b); return (i1-i0).astype(float)
def tp(x,y):
    with np.errstate(all='ignore'):
        p=stats.ttest_ind(x,y,axis=-1).pvalue
    return np.nan_to_num(p,nan=1.0)
rows=[]
for s in S:
    t=s['trials']; site=list(s['ogen'])[0]
    codes={'1','2'} if '1' in set(t.photo_stim_id) else {'3','4'} if '3' in set(t.photo_stim_id) else {'5','6'}
    dcodes={'1':'2','3':'4','5':'5'}[sorted(codes)[0]]
    dcodes=['2'] if '2' in codes else ['4'] if '4' in codes else ['5','6']
    ctl=(t.photo_stim_id=='0').to_numpy(); st=t.photo_stim_id.isin(dcodes).to_numpy(); on=t.pole_out_time.to_numpy()
    pre=np.array([counts(x,on-0.4,on) for x in s['spikes']]); post=np.array([counts(x,on,on+0.4) for x in s['spikes']])
    sh=np.roll(st,1)
    rows.append(dict(session=s['path'].split('/')[1][4:-4], units=len(s['spikes']), stim_trials=int(st.sum()),
        before=np.mean(tp(pre[:,ctl],pre[:,st])<0.01), after=np.mean(tp(post[:,ctl],post[:,st])<0.01),
        shifted=np.mean(tp(post[:,~sh],post[:,sh])<0.01)))
CK=pd.DataFrame(rows); CK['shown']=(CK.after>CK.before)&(CK.after>CK.shifted)&(CK.after>0)
print(CK.round(3).to_string()); print(CK.shown.sum(), CK.loc[~CK.shown,'session'].tolist())
EOF
```

```
0                              1
0    BAYLORCD12  L7-cre x rosa26-lsl-ChR2-EYFP
5    BAYLORCD13  L7-cre x rosa26-lsl-ChR2-EYFP
10   BAYLORCD14  L7-cre x rosa26-lsl-ChR2-EYFP
15    BAYLORCD6                        unknown
19    BAYLORCD8  L7-cre x rosa26-lsl-ChR2-EYFP
24   BAYLORNL12                        unknown
29   BAYLORNL14                        unknown
35   BAYLORNL15                        unknown
40  anm00314746                        unknown
43  anm00314756                        unknown
45  anm00314757                        unknown
47  anm00314758                        unknown
51  anm00314760                        unknown
empty session_description 54
                            session  units  stim_trials  before  after  shifted  shown
0    BAYLORCD12_ses-20180125T191601     20           47   0.000  0.100    0.050   True
1    BAYLORCD12_ses-20180126T122506     22           36   0.000  0.227    0.045   True
2    BAYLORCD12_ses-20180128T220037     22           48   0.000  0.227    0.000   True
3    BAYLORCD12_ses-20180129T160551     44           19   0.045  0.182    0.159   True
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('entries/gao-2018/reproduce_gao_2018.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    if 'clock' in s.lower() or 'lock' in s.lower() and 'decod' in s.lower():
        print(i,c['cell_type'],'\n',s[:2500],'\n-----')
EOF
```

```
11 code 
 # Clock check: trial-type selectivity should be absent before the sample epoch and appear after it,
# and photostimulation should change ALM rates within milliseconds of the light onset.
win = np.arange(-1.0, 1.21, 0.2)    # window starts relative to pole in (sample onset), 200 ms windows
frac = []
for grp_name, inh_group in [("photo-activation", False), ("photo-inhibition", True)]:
    for shift_name, shift in [("true", 0.0), ("events +0.6 s", 0.6)]:
        nsig = np.zeros(len(win)); ntot = 0
        for s in sessions:
            if (s.group == "inhibition") != inh_group:
                continue
            t = s.trials
            for u in s.pyramidal():
                m = s.base_mask() & (t.ptype == 0).to_numpy() & t.correct.to_numpy() & s.stable(u, len(t))
                R, L = m & (t.instructed == "R").to_numpy(), m & (t.instructed == "L").to_numpy()
                if R.sum() < 5 or L.sum() < 5:
                    continue
                ntot += 1
                pi = t.pole_in.to_numpy() + shift
                for k, w0 in enumerate(win):
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/work && ../venv/bin/python - <<'EOF'
import pickle, numpy as np, pandas as pd
from scipy import stats
S=pickle.load(open('S.pkl','rb'))
def counts(sp, a, b):
    return (np.searchsorted(sp,b)-np.searchsorted(sp,a)).astype(float)
def tp(x,y):
    with np.errstate(all='ignore'): p=stats.ttest_ind(x,y,axis=-1).pvalue
    return np.nan_to_num(p,nan=1.0)
rng=np.random.default_rng(0)
rows=[]
for s in S:
    t=s['trials']; resp=t.response.to_numpy()
    m=(t.photo_stim_id=='0').to_numpy()&(t.lick_early==0).to_numpy()&np.isin(resp,['HitR','HitL'])
    R=m&(resp=='HitR'); L=m&(resp=='HitL')
    pi=t.pole_in_time.to_numpy()
    pre=np.array([counts(x,pi-1.0,pi) for x in s['spikes']]); post=np.array([counts(x,pi,pi+2.6) for x in s['spikes']])
    # shuffled labels within the performed trials
    fr=lambda C,a,b: np.mean(tp(C[:,a],C[:,b])<0.05)
    perm=[]
    idx=np.flatnonzero(m)
    for k in range(200):
        lab=rng.permutation(resp[idx]); a=np.zeros(len(t),bool); b=a.copy(); a[idx[lab=='HitR']]=True; b[idx[lab=='HitL']]=True
        perm.append(fr(post,a,b))
    rows.append(dict(session=s['path'].split('/')[1][4:-4], units=len(s['spikes']), R=int(R.sum()), L=int(L.sum()),
                     sel_before=fr(pre,R,L), sel_after=fr(post,R,L), perm95=np.quantile(perm,0.95)))
D=pd.DataFrame(rows); D['shown']=(D.sel_after>D.sel_before)&(D.sel_after>D.perm95)
print(D.round(3).to_string()); print(D.shown.sum(), D.loc[~D.shown,'session'].tolist())
EOF
```

```
/tmp/claude-1001/venv/lib/python3.13/site-packages/scipy/stats/_axis_nan_policy.py:644: RuntimeWarning: Precision loss occurred in moment calculation due to catastrophic cancellation. This occurs when the data are nearly identical. Results may be unreliable.
  res = hypotest_fun_out(*samples, axis=axis, **kwds)
                            session  units    R    L  sel_before  sel_after  perm95  shown
0    BAYLORCD12_ses-20180125T191601     20   56   72       0.000      0.300   0.150   True
1    BAYLORCD12_ses-20180126T122506     22   52   78       0.091      0.182   0.182  False
2    BAYLORCD12_ses-20180128T220037     22   63  103       0.045      0.182   0.182  False
3    BAYLORCD12_ses-20180129T160551     44   59   63       0.000      0.318   0.136   True
4    BAYLORCD12_ses-20180130T153224     52   42   48       0.058      0.269   0.154   True
5    BAYLORCD13_ses-20171211T135437     38    1    4       0.105      0.053   0.132  False
6    BAYLORCD13_ses-20171212T131814     22   17   20       0.091      0.136   0.182  False
7    BAYLORCD13_ses-20171213T135007     14   52   79       0.000      0.286   0.143   True
8    BAYLORCD13_ses-20171214T103426     19   75   66       0.316      0.421   0.158   True
9    BAYLORCD13_ses-20171215T133939      7   55   45       0.143      0.143   0.143  False
10   BAYLORCD14_ses-20171024T112103     43   68   72       0.209      0.651   0.140   True
11   BAYLORCD14_ses-20171025T114022     42  108   77       0.143      0.619   0.119   True
12   BAYLORCD14_ses-20171026T150956     27  180  134       0.111      0.667   0.148   True
13   BAYLORCD14_ses-20171027T115804     43  108  111       0.000      0.558   0.117   True
14   BAYLORCD14_ses-20171028T165746     40   99   93       0.200      0.450   0.125   True
15    BAYLORCD6_ses-20170610T135720     64   62   88       0.031      0.375   0.126   True
16    BAYLORCD6_ses-20170611T140007     61   10   13       0.049      0.230   0.082   True
[... 39 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cat > $TMPDIR/work/e10.py <<'EOF'
import pickle, numpy as np, pandas as pd, time
from scipy import stats
S=pickle.load(open('S.pkl','rb'))
t0=time.time()
def counts(sp, a, b):
    return (np.searchsorted(sp,b)-np.searchsorted(sp,a)).astype(float)
GRID=np.arange(-3.0,1.31,0.01)
def build(s):
    t=s['trials']; resp=t.response.to_numpy()
    instr=np.where(pd.Series(resp).str.endswith('R'),'R',np.where(pd.Series(resp).str.endswith('L'),'L',''))
    ok=(t.lick_early==0).to_numpy()&(instr!='')&~pd.Series(resp).str.startswith('NoLick').to_numpy()
    return t, resp, instr, ok
neurons=[]
for s in S:
    t,resp,instr,ok=build(s)
    pi,po,cue=t.pole_in_time.to_numpy(),t.pole_out_time.to_numpy(),t.cue_time.to_numpy()
    code=t.photo_stim_id.to_numpy()
    for j,sp in enumerate(s['spikes']):
        if s['cell_type'][j]!='pyramidal': continue
        o=s['obs'][j]; inobs=(t.start_time.to_numpy()>=o[:,0].min())&(t.stop_time.to_numpy()<=o[:,1].max())
        m=ok&inobs
        corr=m&(code=='0')&np.isin(resp,['HitR','HitL'])
        ep={'sample':counts(sp,pi,po)/(po-pi),'delay':counts(sp,po,cue)/(cue-po),'response':counts(sp,cue,cue+1.3)/1.3}
        R,L=corr&(resp=='HitR'),corr&(resp=='HitL')
        if R.sum()<2 or L.sum()<2: continue
        sel=any(np.nan_to_num(stats.ttest_ind(v[R],v[L]).pvalue,nan=1)<0.05 for v in ep.values())
        neurons.append(dict(s=s,sp=sp,m=m,corr=corr,resp=resp,instr=instr,code=code,cue=cue,ep=ep,sel=sel,
                            group=('inhibition' if '5' in set(code) else 'activation')))
print(len(neurons),'pyramidal with trials;',sum(n['sel'] for n in neurons),'selective', round(time.time()-t0),'s')
def psth(n, mask):
    sp,cue=n['sp'],n['cue'][mask]
    rel=np.concatenate([sp[(sp>c-3.2)&(sp<c+1.5)]-c for c in cue]) if mask.any() else np.array([])
    rel.sort()
    return (np.searchsorted(rel,GRID+0.1)-np.searchsorted(rel,GRID-0.1))/0.2/mask.sum()
# Fig 2c
res=[]
for per_type in (10,5):
  for epoch in ('sample','delay','response'):
    for draw in range(5):
        rng=np.random.default_rng(1000*per_type+draw)
        rows=[]
        for n in neurons:
            if not n['sel']: continue
            R=np.flatnonzero(n['corr']&(n['resp']=='HitR')); L=np.flatnonzero(n['corr']&(n['resp']=='HitL'))
            if len(R)<=per_type+5 or len(L)<=per_type+5: continue
            sr,sl=rng.choice(R,per_type,replace=False),rng.choice(L,per_type,replace=False)
            pref='R' if n['ep'][epoch][sr].mean()>=n['ep'][epoch][sl].mean() else 'L'
            rest=n['corr'].copy(); rest[sr]=False; rest[sl]=False
            pr=psth(n,rest&(n['resp']=='Hit'+pref)); nr=psth(n,rest&(n['resp']==('HitL' if pref=='R' else 'HitR')))
            rows.append(pr-nr)
        A=np.array(rows).mean(0)
        res.append(dict(per_type=per_type,epoch=epoch,draw=draw,n=len(rows),t_max=round(GRID[np.argmax(A)],2),max=A.max()))
R2=pd.DataFrame(res); print(R2.to_string())
print(R2.groupby(['per_type','epoch']).agg(n=('n','first'),tmin=('t_max','min'),tmax=('t_max','max'),in_response=('t_max',lambda x:(x>0).sum())))
print(round(time.time()-t0),'s')
# Fig 3f
inh=[n for n in neurons if n['group']=='inhibition' and n['sel']]
res=[]
for per_type in (5,10):
    for draw in range(20):
        rng=np.random.default_rng(50000+100*per_type+draw)
        C,P=[],[]
        for n in inh:
            R=np.flatnonzero(n['corr']&(n['resp']=='HitR')); L=np.flatnonzero(n['corr']&(n['resp']=='HitL'))
            if len(R)<per_type or len(L)<per_type: continue
            sr,sl=rng.choice(R,per_type,replace=False),rng.choice(L,per_type,replace=False)
            rate=counts(n['sp'],n['cue']-0.5,n['cue'])/0.5
            pref='R' if n['ep']['delay'][sr].mean()>=n['ep']['delay'][sl].mean() else 'L'
            non='L' if pref=='R' else 'R'
            base=n['m'].copy(); base[sr]=False; base[sl]=False
            ctl=base&(n['code']=='0'); ph=base&np.isin(n['code'],['5','6'])
            groups=[ctl&(n['instr']==pref),ctl&(n['instr']==non),ph&(n['instr']==pref),ph&(n['instr']==non)]
            if min(g.sum() for g in groups)<=3: continue
            C.append(rate[groups[0]].mean()-rate[groups[1]].mean()); P.append(rate[groups[2]].mean()-rate[groups[3]].mean())
        C,P=np.array(C),np.array(P)
        bi=rng.integers(0,len(C),(1000,len(C)))
        cl,ch=np.quantile(C[bi].mean(1),[0.025,0.975]); pl,ph_=np.quantile(P[bi].mean(1),[0.025,0.975])
        res.append(dict(per_type=per_type,draw=draw,n=len(C),control=C.mean(),c_lo=cl,c_hi=ch,photo=P.mean(),p_lo=pl,p_hi=ph_,
                        abolished=(cl>0)&(pl<=0<=ph_)))
R3=pd.DataFrame(res); print(R3.round(3).to_string())
print(R3.groupby('per_type').agg(draws=('draw','size'),abolished=('abolished','sum'),pmin=('photo','min'),pmax=('photo','max')))
print(round(time.time()-t0),'s')
EOF
cd $TMPDIR/work && timeout 1800 ../venv/bin/python e10.py 2>&1 | grep -v Warning | grep -v hypotest
```

```
Sat Nov 14 17:43:24 UTC 2026
1782 pyramidal with trials; 1296 selective 2 s
    per_type     epoch  draw     n  t_max       max
0         10    sample     0  1274  -1.94  0.966340
1         10    sample     1  1274  -0.55  0.955055
2         10    sample     2  1274  -1.60  0.891865
3         10    sample     3  1274  -1.98  0.908900
4         10    sample     4  1274  -1.61  0.878355
5         10     delay     0  1274  -0.10  1.827938
6         10     delay     1  1274  -0.14  1.869909
7         10     delay     2  1274  -0.09  1.876527
8         10     delay     3  1274  -0.12  1.715468
9         10     delay     4  1274  -0.09  1.800303
10        10  response     0  1274   0.24  2.309522
11        10  response     1  1274   0.24  2.286098
12        10  response     2  1274   0.49  2.254434
13        10  response     3  1274   0.36  2.226168
14        10  response     4  1274   0.25  2.361526
15         5    sample     0  1274  -1.79  0.851241
16         5    sample     1  1274  -1.98  0.892624
[... 69 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/work && cat > e10b.py <<'EOF'
exec(open('e10.py').read().split('# Fig 2c')[0])
inh=[n for n in neurons if n['group']=='inhibition' and n['sel']]
for codes in (['5'],['6']):
  for per_type in (5,10):
    out=[]
    for draw in range(20):
        rng=np.random.default_rng(50000+100*per_type+draw)
        C,P=[],[]
        for n in inh:
            R=np.flatnonzero(n['corr']&(n['resp']=='HitR')); L=np.flatnonzero(n['corr']&(n['resp']=='HitL'))
            if len(R)<per_type or len(L)<per_type: continue
            sr,sl=rng.choice(R,per_type,replace=False),rng.choice(L,per_type,replace=False)
            rate=counts(n['sp'],n['cue']-0.5,n['cue'])/0.5
            pref='R' if n['ep']['delay'][sr].mean()>=n['ep']['delay'][sl].mean() else 'L'; non='L' if pref=='R' else 'R'
            base=n['m'].copy(); base[sr]=False; base[sl]=False
            ctl=base&(n['code']=='0'); ph=base&np.isin(n['code'],codes)
            g=[ctl&(n['instr']==pref),ctl&(n['instr']==non),ph&(n['instr']==pref),ph&(n['instr']==non)]
            if min(x.sum() for x in g)<=3: continue
            C.append(rate[g[0]].mean()-rate[g[1]].mean()); P.append(rate[g[2]].mean()-rate[g[3]].mean())
        C,P=np.array(C),np.array(P); bi=rng.integers(0,len(C),(1000,len(C)))
        cl=np.quantile(C[bi].mean(1),0.025); pl,ph_=np.quantile(P[bi].mean(1),[0.025,0.975])
        out.append((len(C),P.mean(),(cl>0)&(pl<=0<=ph_)))
    o=np.array(out,float); print(codes,per_type,'n',o[0,0],'photo',o[:,1].min().round(3),o[:,1].max().round(3),'abolished',int(o[:,2].sum()),'of 20')
EOF
timeout 900 ../venv/bin/python e10b.py 2>&1 | grep -v Warn | grep -v hypotest
```

```
1782 pyramidal with trials; 1296 selective 2 s
['5'] 5 n 441.0 photo 0.48 0.921 abolished 0 of 20
['5'] 10 n 441.0 photo 0.617 0.999 abolished 0 of 20
['6'] 5 n 385.0 photo 0.067 0.46 abolished 8 of 20
['6'] 10 n 385.0 photo 0.055 0.356 abolished 11 of 20
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('entries/gao-2018/reproduce_gao_2018.ipynb'))
print(nb['metadata']); print(nb['nbformat'], nb['nbformat_minor'])
for c in nb['cells'][:4]: print(c['cell_type'], c.get('metadata'), ''.join(c['source'])[:600]); print('---')
EOF
grep -n "earlier_findings\|tags\|sanity" tools/entry.py | head -20
```

```
{'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}}
4 5
markdown {} # Reproducing Gao et al. (2018) from DANDI:000007 and CRCNS:alm-4

**Paper.** Gao Z, Davis C, Thomas AM, Economo MN, Abrego AM, Svoboda K, De Zeeuw CI, Li N (2018).
A cortico-cerebellar loop for motor planning. *Nature* 563, 113-116.
[doi:10.1038/s41586-018-0633-x](https://doi.org/10.1038/s41586-018-0633-x). The claims file
(`claims/gao-2018.yaml`) was written from the version of record (PMC6212318) with its Methods,
Extended Data legends and Supplementary Information; the legends of the main Figures 1 to 4 were
not in the text read.

**Datasets.**
- [DANDI:000007](https://dandiarchive.org/dan
---
code {} import time
import resource
import warnings

import matplotlib.pyplot as plt
import numpy as np
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 375,400p tools/entry.py; sed -n 455,475p tools/entry.py
```

```
report.error(path.relative_to(ROOT), f"claim {outcome.get('claim')!r} is not in the claims file")
            notebook = outcome.get("notebook")
            # A claim that was tested names the notebook that tested it. One whose outcome changed from blocked
            # in a late revision can be left without (andrews-2024, 2026-11-13): the site then lists it with the
            # claims no notebook tests.
            if outcome.get("outcome") != "blocked" and not notebook:
                report.error(path.relative_to(ROOT), f"claim {outcome.get('claim')!r} is {outcome.get('outcome')!r} "
                             "and names no notebook; give the notebook that tests it (`notebook`) and its cell (`output`)")
            if notebook and notebook not in listed:
                report.error(path.relative_to(ROOT), f"notebook {notebook!r} is not in the entry")
            tag = outcome.get("output")
            if notebook in present and tag:
                nb = nbformat.read(entry_dir / notebook, as_version=4)
                if not any(tag in c.metadata.get("tags", []) for c in nb.cells):
                    report.error(path.relative_to(ROOT), f"no cell tagged {tag!r} in {notebook}")
    return report


def _local_data(code: str, start: int) -> bool:
    """Whether a local path in the code is inside the dataset directory `encore check` gave (ENCORE_LOCAL_DATA):
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/work && cat > $TMPDIR/work/build_nb.py <<'PYEOF'
import nbformat as nbf, yaml, textwrap
E = yaml.safe_load(open('attempts/gao-2018-01.yaml'))['findings']
nb = nbf.v4.new_notebook()
nb.metadata = {'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}}
C = nb.cells
md = lambda s: C.append(nbf.v4.new_markdown_cell(textwrap.dedent(s).strip()))
def code(s, tags=None):
    c = nbf.v4.new_code_cell(textwrap.dedent(s).strip())
    if tags: c.metadata['tags'] = tags
    C.append(c)
def quote(i):
    return "> " + E[i - 1]['statement'].strip()

md("""
# Gao et al. (2018): the earlier attempt's findings, checked on DANDI:000007

Attempt `gao-2018-02`, made blind, is compared with `gao-2018-01` in the reconciliation block of
`attempts/gao-2018-02.yaml` (docs/protocol.md, "Repeat attempts"). Findings 1, 3, 4, 6, 11 and 12 of
`gao-2018-01` are reported again by `gao-2018-02` and are not checked here. This notebook checks the
other six (2, 5, 7, 8, 9 and 10) directly, on the dataset and version the earlier attempt used:
[DANDI:000007](https://dandiarchive.org/dandiset/000007/0.220126.1903), version 0.220126.1903, 54 NWB
files streamed with remfile and h5py. It reads no other dataset. Each section opens with the earlier
statement and ends with a short result.

Paper: Gao Z, Davis C, Thomas AM, Economo MN, Abrego AM, Svoboda K, De Zeeuw CI, Li N (2018). A
cortico-cerebellar loop for motor planning. *Nature* 563, 113-116, doi:10.1038/s41586-018-0633-x.
""")
code('''
import json
import time
import warnings
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests
from scipy import stats

warnings.filterwarnings("ignore", category=RuntimeWarning)
pd.set_option("display.width", 200)
pd.set_option("display.max_rows", 100)

DANDISET_ID, DANDISET_VERSION = "000007", "0.220126.1903"


def _s(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def load_one(asset):
    """One NWB file: trials, spike times, observation intervals, waveforms and the metadata checked below."""
    url = requests.head(f"https://api.dandiarchive.org/api/assets/{asset['asset_id']}/download/",
                        allow_redirects=True, timeout=60).url
    with h5py.File(remfile.File(url), "r") as f:
        tr = f["intervals/trials"]
        trials = pd.DataFrame({k: tr[k][:] for k in ["start_time", "stop_time", "pole_in_time", "pole_out_time",
                                                     "cue_time", "lick_early", "response", "photo_stim_id"]})
        for k in ("response", "photo_stim_id"):
            trials[k] = trials[k].map(_s)
        u = f["units"]
        st, idx = u["spike_times"][:], u["spike_times_index"][:]
        oi, oidx = u["obs_intervals"][:], u["obs_intervals_index"][:]
        sub = f["general/subject"]
        out = dict(
            path=asset["path"], subject=_s(sub["subject_id"][()]),
            subject_fields={k: _s(sub[k][()]) for k in sub},
            session_description=_s(f["session_description"][()]),
            trials=trials, trial_descr={k: _s(tr[k].attrs.get("description", "")) for k in tr},
            spikes=np.split(st, idx[:-1]), obs=np.split(oi, oidx[:-1]),
            cell_type=u["cell_type"][:].astype(str), wf_rate=u["sampling_rate"][:],
            waveform=u["waveform_mean"][:], devices=list(f["general/devices"]),
            egroups={k: json.loads(f[f"general/extracellular_ephys/{k}"].attrs.get("location", "{}"))
                     for k in f["general/extracellular_ephys"] if k != "electrodes"},
            ogen={k: json.loads(_s(f[f"general/optogenetics/{k}/location"][()]) or "{}")
                  for k in f["general/optogenetics"]},
            acquisition=list(f["acquisition"]),
            stimulus=list(f["stimulus/presentation"]) + list(f["stimulus/templates"]),
            processing=list(f["processing"]))
    out["name"] = asset["path"].split("/")[1][4:-4]
    return out


started = time.time()
r = requests.get(f"https://api.dandiarchive.org/api/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}"
                 "/assets/?page_size=200", timeout=60).json()
assets = sorted([a for a in r["results"] if a["path"].endswith(".nwb")], key=lambda a: a["path"])
with ThreadPoolExecutor(8) as ex:
    S = list(ex.map(load_one, assets))
for s in S:
    codes = set(s["trials"].photo_stim_id)
    s["group"] = "fastigial" if "1" in codes else "dentate" if "3" in codes else "inhibition"
print(f"DANDI:{DANDISET_ID} version {DANDISET_VERSION}: {len(S)} NWB files streamed in {time.time() - started:.0f} s")
''')
md("## Data check")
code('''
D = pd.DataFrame([dict(subject=s["subject"], group=s["group"], site=",".join(s["ogen"]), trials=len(s["trials"]),
                       units=len(s["spikes"]), pyramidal=int((s["cell_type"] == "pyramidal").sum()),
                       codes=",".join(sorted(set(s["trials"].photo_stim_id)))) for s in S])
print(D.groupby(["group", "subject"]).agg(sessions=("trials", "size"), trials=("trials", "sum"), units=("units", "sum"),
                                          pyramidal=("pyramidal", "sum"), site=("site", "first"),
                                          codes=("codes", "first")).to_string())
print("total:", len(S), "sessions,", D.subject.nunique(), "mice,", D.units.sum(), "units,", D.trials.sum(), "trials")
T = pd.concat([s["trials"] for s in S])
print("pole_in_time - start_time (s):", (T.pole_in_time - T.start_time).describe().round(3).to_dict())
print("responses:", T.response.value_counts().to_dict())
''', tags=['sanity'])

def section(i, title):
    md(f"## Earlier finding {i}: {title}\n\n{quote(i)}")

section(2, "the photostimulation codes")
code('''
print("description of photo_stim_id in the 54 files:", pd.Series([s["trial_descr"]["photo_stim_id"] for s in S]).value_counts().to_dict())
print("files with anything under acquisition, stimulus or processing:",
      sum(bool(s["acquisition"] or s["stimulus"] or s["processing"]) for s in S))
print("devices:", pd.Series([", ".join(s["devices"]) for s in S]).value_counts().to_dict())
print("codes by group:", D.groupby("group").codes.agg(lambda x: sorted(set(x))).to_dict())
''')
md("""
**Result: still present.** In all 54 files `photo_stim_id` has the description "varchar(8) #" and
nothing else, and no file holds anything under acquisition, stimulus or processing, so there is no laser
trace. The codes are as the earlier finding gives them (1 and 2, 3 and 4, 5 and 6 by group), and nothing in
the files says what each means.
""")

section(5, "subject identifiers and descriptions")
code('''
subj = pd.DataFrame([dict(subject=s["subject"], fields=", ".join(sorted(s["subject_fields"])),
                          genotype=s["subject_fields"].get("genotype"), site=",".join(
                              f"{k} {v.get('hemisphere')}" for k, v in s["ogen"].items()),
                          alm_ml=",".join(g.get("rec_coordinate_ml", "") for g in s["egroups"].values()))
                     for s in S]).drop_duplicates()
print(subj.to_string())
print("files with an empty session_description:", sum(s["session_description"] == "" for s in S), "of", len(S))
print("any subject field naming AN105 to AN109:",
      any("AN10" in v for s in S for v in s["subject_fields"].values()))
''')
md("""
**Result: still present.** The five anm subjects carry only their anm identifiers; no subject field names
AN105 to AN109. Their sites (printed) are as the earlier finding says: anm00314756 alone is dentate and
anm00314757 alone has a left fastigial site and right ALM, while anm00314746, anm00314758 and
anm00314760 share a right fastigial site and left ALM, so they cannot be told apart. The genotype is
"unknown" for every mouse that is not L7-cre x Ai32, and session_description is empty in all 54 files.
""")

section(7, "cell types against spike width, and the waveform sampling rate")
code('''
def trough_to_peak_ms(wf, rate):
    tr = int(np.argmin(wf))
    return (tr + int(np.argmax(wf[tr:])) - tr) / rate * 1000

rows = []
for s in S:
    probe = ", ".join(g["probe_type"] for g in s["egroups"].values())
    for i in range(len(s["cell_type"])):
        rows.append(dict(session=s["name"], probe=probe, rate=int(s["wf_rate"][i]), samples=s["waveform"].shape[1],
                         cell_type=s["cell_type"][i], width=trough_to_peak_ms(s["waveform"][i], s["wf_rate"][i])))
W = pd.DataFrame(rows)
W["by_width"] = np.where(W.width > 0.45, "> 0.45 ms", np.where(W.width < 0.35, "< 0.35 ms", "0.35 to 0.45 ms"))
print(pd.crosstab(W.cell_type, W.by_width, margins=True))
print("width range", W.width.min(), "to", W.width.max(), "ms")
print(W.groupby("probe").agg(sessions=("session", "nunique"), stated_rates=("rate", lambda x: sorted(set(x))),
                             samples_per_waveform=("samples", lambda x: sorted(set(x)))).to_string())
print(W.drop_duplicates("session").groupby(["probe", "samples"]).size())
''')
md("""
**Result: still present.** 60 units labelled "pyramidal" have a trough-to-peak width under 0.45 ms (27
between 0.35 and 0.45 ms and 33 under 0.35 ms), and 3 units are labelled "unknown". Every unit's waveform
is stated as sampled at 20000 Hz, in the 34 sessions recorded with the 32-channel NeuroNexus probe as in the
20 with the 64-channel probe. In 14 of the 34 NeuroNexus sessions the mean waveforms have 37 or 38 samples
against 30 in every other session, which a higher sampling rate would give for the same duration; the files
do not say which rate applies.
""")

section(8, "sessions whose response is not shown to be locked to the trial events")
code('''
def counts(sp, a, b):
    return (np.searchsorted(sp, b) - np.searchsorted(sp, a)).astype(float)


def frac_sig(C, a, b, alpha):
    p = stats.ttest_ind(C[:, a], C[:, b], axis=1).pvalue
    return float(np.mean(np.nan_to_num(p, nan=1.0) < alpha)) if len(C) else np.nan


DELAY = {"fastigial": ["2"], "dentate": ["4"], "inhibition": ["5", "6"]}
rng8 = np.random.default_rng(8)
ck = []
for s in S:
    t = s["trials"]
    code_, resp = t.photo_stim_id.to_numpy(), t.response.to_numpy()
    # (a) the earlier attempt's contrast: neurons whose rate differs between control and delay photostimulation
    # trials in the 400 ms after pole_out_time, against the 400 ms before it and against labels shifted by a trial
    ctl, st, on = code_ == "0", np.isin(code_, DELAY[s["group"]]), t.pole_out_time.to_numpy()
    pre = np.array([counts(x, on - 0.4, on) for x in s["spikes"]])
    post = np.array([counts(x, on, on + 0.4) for x in s["spikes"]])
    sh = np.roll(st, 1)
    a = dict(before=frac_sig(pre, ctl, st, 0.01), after=frac_sig(post, ctl, st, 0.01),
             after_shifted=frac_sig(post, ~sh, sh, 0.01))
    # (b) trial-type selectivity: neurons whose rate differs between correct lick-right and lick-left control
    # trials in the 1 s before pole_in_time and the 2.6 s after it, against 200 label permutations
    m = (code_ == "0") & (t.lick_early == 0).to_numpy() & np.isin(resp, ["HitR", "HitL"])
    R, L = m & (resp == "HitR"), m & (resp == "HitL")
    pi = t.pole_in_time.to_numpy()
    pre_b = np.array([counts(x, pi - 1.0, pi) for x in s["spikes"]])
    post_b = np.array([counts(x, pi, pi + 2.6) for x in s["spikes"]])
    idx, perm = np.flatnonzero(m), []
    for _ in range(200):
        lab = rng8.permutation(resp[idx])
        pa, pb = np.zeros(len(t), bool), np.zeros(len(t), bool)
        pa[idx[lab == "HitR"]], pb[idx[lab == "HitL"]] = True, True
        perm.append(frac_sig(post_b, pa, pb, 0.05))
    b = dict(sel_before=frac_sig(pre_b, R, L, 0.05), sel_after=frac_sig(post_b, R, L, 0.05),
             sel_perm95=float(np.quantile(perm, 0.95)))
    ck.append(dict(session=s["name"], group=s["group"], units=len(s["spikes"]), trials=len(t),
                   stim_trials=int(st.sum()), right=int(R.sum()), left=int(L.sum()), **a, **b))
CK = pd.DataFrame(ck)
CK["shown_a"] = (CK.after > CK.before) & (CK.after > CK.after_shifted) & (CK.after > 0)
CK["shown_b"] = (CK.sel_after > CK.sel_before) & (CK.sel_after > CK.sel_perm95)
print(CK.round(3).to_string())
EARLIER = ["BAYLORCD12_ses-20180125T191601", "BAYLORCD12_ses-20180129T160551", "BAYLORCD13_ses-20171211T135437",
           "BAYLORCD13_ses-20171215T133939", "anm00314756_ses-20151023T141029"]
print("shown by (a):", int(CK.shown_a.sum()), "of", len(CK), "; not shown:", CK.loc[~CK.shown_a, "session"].tolist())
print("shown by (b):", int(CK.shown_b.sum()), "of", len(CK), "; not shown:", CK.loc[~CK.shown_b, "session"].tolist())
print("shown by neither:", CK.loc[~CK.shown_a & ~CK.shown_b, "session"].tolist())
print("the earlier attempt's five sessions:")
print(CK.set_index("session").loc[EARLIER, ["units", "stim_trials", "right", "left", "shown_a", "shown_b"]].to_string())
''')
md("RESULT8")

section(9, "BAYLORCD8 20171020 after the end of the recording")
code('''
s = [s for s in S if s["name"].startswith("BAYLORCD8_ses-20171020")][0]
t = s["trials"]
ends = np.array([o[:, 1].max() for o in s["obs"]])
allsp = np.concatenate(s["spikes"])
after = (t.start_time > ends.max()).to_numpy()
inside = sum(((allsp >= a) & (allsp < b)).sum() for a, b in zip(t.start_time[after], t.stop_time[after]))
print(s["name"], ":", len(s["spikes"]), "units,", len(t), "trials from", t.start_time.min(), "to", t.stop_time.max(), "s")
print("end of the units' observation intervals: min", ends.min(), "max", ends.max(), "s; last spike", allsp.max(), "s")
print("trials starting after it:", int(after.sum()), "from", t.start_time[after].min(), "to", t.stop_time[after].max(),
      "s; spikes of any unit in them:", int(inside))
''')
md("""
**Result: still present.** Every unit's observation interval ends at 7221.77 s, and the last 127 of the
462 trials, from 7223.1 to 8481.39 s, hold no spike of any unit. The obs_intervals column records the
end of the recording.
""")

section(10, "the preference trials and epoch of the population selectivity")
code('''
GRID = np.arange(-3.0, 1.31, 0.01)       # time from the go cue (cue_time), s
neurons = []
for s in S:
    t = s["trials"]
    resp, code_ = t.response.to_numpy(), t.photo_stim_id.to_numpy()
    instr = np.array([x[-1] if x.startswith(("Hit", "Err")) else "" for x in resp])
    pi, po, cue = t.pole_in_time.to_numpy(), t.pole_out_time.to_numpy(), t.cue_time.to_numpy()
    for j, sp in enumerate(s["spikes"]):
        if s["cell_type"][j] != "pyramidal":
            continue
        o = s["obs"][j]
        m = ((t.lick_early == 0).to_numpy() & (instr != "") & (t.start_time >= o[:, 0].min()).to_numpy()
             & (t.stop_time <= o[:, 1].max()).to_numpy())
        corr = m & (code_ == "0") & np.isin(resp, ["HitR", "HitL"])
        ep = {"sample": counts(sp, pi, po) / (po - pi), "delay": counts(sp, po, cue) / (cue - po),
              "response": counts(sp, cue, cue + 1.3) / 1.3}
        R, L = corr & (resp == "HitR"), corr & (resp == "HitL")
        if R.sum() < 2 or L.sum() < 2:
            continue
        sel = any(np.nan_to_num(stats.ttest_ind(v[R], v[L]).pvalue, nan=1.0) < 0.05 for v in ep.values())
        neurons.append(dict(sp=sp, m=m, corr=corr, resp=resp, instr=instr, code=code_, cue=cue, ep=ep, sel=sel,
                            group=s["group"]))
print(len(neurons), "pyramidal neurons with 2 or more correct control trials of each type;",
      sum(n["sel"] for n in neurons), "selective (t-test, p < 0.05, sample, delay or response epoch)")


def psth(n, mask):
    rel = np.sort(np.concatenate([n["sp"][(n["sp"] > c - 3.2) & (n["sp"] < c + 1.5)] - c for c in n["cue"][mask]]))
    return (np.searchsorted(rel, GRID + 0.1) - np.searchsorted(rel, GRID - 0.1)) / 0.2 / mask.sum()


# Fig. 2c: preferred type from screening trials (10 of each type, or 5 of each, 10 in all) by the count in one
# epoch; selectivity on the remaining correct control trials, 200 ms boxcar; 5 draws each.
res = []
for per_type in (10, 5):
    for epoch in ("sample", "delay", "response"):
        for draw in range(5):
            rng = np.random.default_rng(1000 * per_type + draw)
            rows = []
            for n in neurons:
                if not n["sel"]:
                    continue
                R = np.flatnonzero(n["corr"] & (n["resp"] == "HitR"))
                L = np.flatnonzero(n["corr"] & (n["resp"] == "HitL"))
                if len(R) <= per_type + 5 or len(L) <= per_type + 5:
                    continue
                sr, sl = rng.choice(R, per_type, replace=False), rng.choice(L, per_type, replace=False)
                pref = "R" if n["ep"][epoch][sr].mean() >= n["ep"][epoch][sl].mean() else "L"
                rest = n["corr"].copy()
                rest[sr], rest[sl] = False, False
                rows.append(psth(n, rest & (n["resp"] == "Hit" + pref))
                            - psth(n, rest & (n["resp"] == ("HitL" if pref == "R" else "HitR"))))
            A = np.array(rows).mean(0)
            res.append(dict(per_type=per_type, epoch=epoch, draw=draw, neurons=len(rows),
                            t_max=round(float(GRID[np.argmax(A)]), 2), max=float(A.max())))
F2 = pd.DataFrame(res)
print("Time of the maximum population selectivity, s from the go cue (response epoch 0 to 1.3 s):")
print(F2.groupby(["per_type", "epoch"]).agg(neurons=("neurons", "first"), t_max_min=("t_max", "min"),
                                             t_max_max=("t_max", "max"), draws_in_response=("t_max", lambda x: int((x > 0).sum())),
                                             max_min=("max", "min"), max_max=("max", "max")).round(2).to_string())
''')
code('''
# Fig. 3f: selective neurons of the photo-inhibition mice; preferred type from screening trials by the delay
# count; last 500 ms of the delay, control against photo-inhibition trials (all trials by instructed type);
# neurons with more than 3 trials in each of the four conditions; bootstrap 95% interval over neurons;
# abolished when the control interval is above zero and the photo-inhibition interval contains zero. 20 draws.
inh = [n for n in neurons if n["group"] == "inhibition" and n["sel"]]
res = []
for codes in (["5", "6"], ["5"], ["6"]):
    for per_type in (5, 10):
        for draw in range(20):
            rng = np.random.default_rng(50000 + 100 * per_type + draw)
            Cs, Ps = [], []
            for n in inh:
                R = np.flatnonzero(n["corr"] & (n["resp"] == "HitR"))
                L = np.flatnonzero(n["corr"] & (n["resp"] == "HitL"))
                if len(R) < per_type or len(L) < per_type:
                    continue
                sr, sl = rng.choice(R, per_type, replace=False), rng.choice(L, per_type, replace=False)
                rate = counts(n["sp"], n["cue"] - 0.5, n["cue"]) / 0.5
                pref = "R" if n["ep"]["delay"][sr].mean() >= n["ep"]["delay"][sl].mean() else "L"
                non = "L" if pref == "R" else "R"
                base = n["m"].copy()
                base[sr], base[sl] = False, False
                ctl, ph = base & (n["code"] == "0"), base & np.isin(n["code"], codes)
                g = [ctl & (n["instr"] == pref), ctl & (n["instr"] == non), ph & (n["instr"] == pref), ph & (n["instr"] == non)]
                if min(x.sum() for x in g) <= 3:
                    continue
                Cs.append(rate[g[0]].mean() - rate[g[1]].mean())
                Ps.append(rate[g[2]].mean() - rate[g[3]].mean())
            Cs, Ps = np.array(Cs), np.array(Ps)
            bi = rng.integers(0, len(Cs), (1000, len(Cs)))
            c_lo = np.quantile(Cs[bi].mean(1), 0.025)
            p_lo, p_hi = np.quantile(Ps[bi].mean(1), [0.025, 0.975])
            res.append(dict(codes="+".join(codes), per_type=per_type, draw=draw, neurons=len(Cs), control=Cs.mean(),
                            control_lo=c_lo, photo=Ps.mean(), photo_lo=p_lo, photo_hi=p_hi,
                            abolished=bool(c_lo > 0 and p_lo <= 0 <= p_hi)))
F3 = pd.DataFrame(res)
print(F3.groupby(["codes", "per_type"]).agg(neurons=("neurons", "first"), draws=("draw", "size"),
                                             abolished=("abolished", "sum"), photo_min=("photo", "min"),
                                             photo_max=("photo", "max"), control_lo_min=("control_lo", "min")).round(3).to_string())
print(f"run time {time.time() - started:.0f} s")
''')
md("RESULT10")
nbf.write(nb, 'entries/gao-2018/earlier_findings.ipynb')
PYEOF
cd  && $TMPDIR/venv/bin/python $TMPDIR/work/build_nb.py && $TMPDIR/venv/bin/jupyter nbconvert --version 2>/dev/null; date -u
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/work/build_nb.py", line 1, in <module>
    import nbformat as nbf, yaml, textwrap
ModuleNotFoundError: No module named 'yaml'
Sat Nov 14 17:45:48 UTC 2026
```

**Agent calls Bash**

```bash
python -c "import nbformat,yaml" && python $TMPDIR/work/build_nb.py && cd $TMPDIR/work && cp entries/gao-2018/earlier_findings.ipynb test.ipynb && time ../venv/bin/python -c "
import nbformat
from nbclient import NotebookClient
nb=nbformat.read('test.ipynb',4)
NotebookClient(nb,timeout=3000,kernel_name='python3',resources={'metadata':{'path':'.'}}).execute()
nbformat.write(nb,'test_out.ipynb')
" 2>&1 | tail -5
```

```
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.

real	1m51.020s
user	0m57.609s
sys	0m0.807s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/work && python - <<'EOF'
import nbformat
nb=nbformat.read('test_out.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    for o in c.get('outputs',[]):
        t=o.get('text') or o.get('data',{}).get('text/plain') or o.get('evalue','')
        if i in (3,5,15,18,19): print(f'--- cell {i}'); print(t[-6000:])
EOF
```

```
--- cell 3
                        sessions  trials  units  pyramidal       site  codes
group      subject                                                          
dentate    BAYLORNL12          5    1910    244        231    Dentate  0,3,4
           BAYLORNL14          6    2283    308        288    Dentate  0,3,4
           anm00314756         2     457     26         26    Dentate  0,3,4
fastigial  BAYLORCD6           4     941    196        187  Fastigial  0,1,2
           BAYLORNL15          5    1547    177        160  Fastigial  0,1,2
           anm00314746         3     780     63         60  Fastigial  0,1,2
           anm00314757         2     280     38         35  Fastigial  0,1,2
           anm00314758         4    1005     62         61  Fastigial  0,1,2
           anm00314760         3     745     72         64  Fastigial  0,1,2
inhibition BAYLORCD12          5    1205    160        153  Fastigial  0,5,6
           BAYLORCD13          5     967    100         96  Fastigial  0,5,6
           BAYLORCD14          5    1719    195        185  Fastigial  0,5,6
           BAYLORCD8           5    1795    282        272  Fastigial    0,5
total: 54 sessions, 13 mice, 1923 units, 15634 trials
pole_in_time - start_time (s): {'count': 15634.0, 'mean': 0.571, 'std': 0.144, 'min': 0.09, '25%': 0.57, '50%': 0.57, '75%': 0.57, 'max': 18.466}
responses: {'HitL': 6340, 'HitR': 6298, 'ErrL': 1262, 'ErrR': 1156, 'NoLickR': 298, 'NoLickL': 280}

[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/work && python - <<'EOF'
import nbformat
nb=nbformat.read('test_out.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code' or i<6: continue
    print(f'=== cell {i}')
    for o in c.get('outputs',[]):
        t=o.get('text') or o.get('data',{}).get('text/plain') or (o.get('ename','')+o.get('evalue',''))
        print(t[-5000:])
EOF
```

```
=== cell 8
        subject                                             fields                       genotype             site alm_ml
0    BAYLORCD12  date_of_birth, genotype, sex, species, subject_id  L7-cre x rosa26-lsl-ChR2-EYFP   Fastigial left   -1.5
5    BAYLORCD13  date_of_birth, genotype, sex, species, subject_id  L7-cre x rosa26-lsl-ChR2-EYFP   Fastigial left   -1.5
10   BAYLORCD14  date_of_birth, genotype, sex, species, subject_id  L7-cre x rosa26-lsl-ChR2-EYFP   Fastigial left   -1.5
15    BAYLORCD6  date_of_birth, genotype, sex, species, subject_id                        unknown  Fastigial right   -1.5
19    BAYLORCD8  date_of_birth, genotype, sex, species, subject_id  L7-cre x rosa26-lsl-ChR2-EYFP  Fastigial right   -1.5
24   BAYLORNL12  date_of_birth, genotype, sex, species, subject_id                        unknown    Dentate right   -1.5
29   BAYLORNL14  date_of_birth, genotype, sex, species, subject_id                        unknown    Dentate right   -1.5
35   BAYLORNL15  date_of_birth, genotype, sex, species, subject_id                        unknown  Fastigial right   -1.5
40  anm00314746  date_of_birth, genotype, sex, species, subject_id                        unknown  Fastigial right   -1.5
43  anm00314756  date_of_birth, genotype, sex, species, subject_id                        unknown    Dentate right   -1.5
45  anm00314757  date_of_birth, genotype, sex, species, subject_id                        unknown   Fastigial left    1.5
47  anm00314758  date_of_birth, genotype, sex, species, subject_id                        unknown  Fastigial right   -1.5
51  anm00314760  date_of_birth, genotype, sex, species, subject_id                        unknown  Fastigial right   -1.5
files with an empty session_description: 54 of 54
any subject field naming AN105 to AN109: False

=== cell 11
by_width   0.35 to 0.45 ms  < 0.35 ms  > 0.45 ms   All
[... 82 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/work && python - <<'EOF'
import nbformat
nb=nbformat.read('test_out.ipynb',4)
t=nb.cells[14].outputs[0]['text']; print('\n'.join(t.splitlines()[:12]))
EOF
```

```
session       group  units  trials  stim_trials  right  left  before  after  after_shifted  sel_before  sel_after  sel_perm95  shown_a  shown_b
0    BAYLORCD12_ses-20180125T191601  inhibition     20     273           47     56    72   0.000  0.100          0.050       0.000      0.300       0.100     True     True
1    BAYLORCD12_ses-20180126T122506  inhibition     22     256           36     52    78   0.000  0.227          0.045       0.091      0.182       0.136     True     True
2    BAYLORCD12_ses-20180128T220037  inhibition     22     318           48     63   103   0.000  0.227          0.000       0.045      0.182       0.136     True     True
3    BAYLORCD12_ses-20180129T160551  inhibition     44     196           19     59    63   0.045  0.182          0.159       0.000      0.318       0.114     True     True
4    BAYLORCD12_ses-20180130T153224  inhibition     52     162           22     42    48   0.000  0.250          0.058       0.058      0.269       0.135     True     True
5    BAYLORCD13_ses-20171211T135437  inhibition     38      15            8      1     4   0.000  0.000          0.000       0.105      0.053       0.132    False    False
6    BAYLORCD13_ses-20171212T131814  inhibition     22     119           30     17    20   0.000  0.318          0.045       0.091      0.136       0.136     True    False
7    BAYLORCD13_ses-20171213T135007  inhibition     14     298           67     52    79   0.000  0.286          0.071       0.000      0.286       0.143     True     True
8    BAYLORCD13_ses-20171214T103426  inhibition     19     294           64     75    66   0.053  0.526          0.053       0.316      0.421       0.158     True     True
9    BAYLORCD13_ses-20171215T133939  inhibition      7     241           53     55    45   0.000  0.000          0.000       0.143      0.143       0.143    False    False
10   BAYLORCD14_ses-20171024T112103  inhibition     43     239           70     68    72   0.000  0.488          0.093       0.209      
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='/tmp/claude-1001/work/build_nb.py'
import os
p=os.path.join(os.environ.get('TMPDIR','/tmp/claude-1001'),'work/build_nb.py')
s=open(p).read()
s=s.replace('''                                             max_min=("max", "min"), max_max=("max", "max")).round(2).to_string())
\'\'\')''','''                                             max_min=("max", "min"), max_max=("max", "max")).round(2).to_string())
print("t_max by draw:")
print(F2.pivot_table(index=["per_type", "epoch"], columns="draw", values="t_max").to_string())
\'\'\')''')
r8='''**Result: still present, in two of the five sessions.** With the earlier attempt's contrast (a), 50 of
54 sessions show a locked response; not BAYLORCD13 20171211 and 20171215 or anm00314756 20151020 and
20151023. With trial-type selectivity (b), 48 of 54 do. Neither contrast shows it in BAYLORCD13 20171211,
which holds 15 trials (8 with delay photostimulation, and 1 and 4 correct lick-right and lick-left control
trials), or in BAYLORCD13 20171215, which holds 7 units. Of the earlier five sessions, BAYLORCD12 20180125
and 20180129 are shown here by both contrasts and anm00314756 20151023 by (b).'''
r10='''**Result: still present.** Fig. 2c: over 1274 selective neurons, the maximum of the population
selectivity lies in the response epoch (0.24 to 0.49 s after the go cue) in every draw when the response
epoch fixes the preferred type, 0.06 to 0.23 s before the go cue when the delay epoch does, and in the
sample epoch (1.60 to 2.00 s before the go cue) in 9 of 10 draws when the sample epoch does, with 5 or
10 screening trials of each type. Which epoch fixes the preference decides where the maximum lies. Fig. 3f:
with codes 5 and 6 pooled, or code 5 alone, no draw of 20 brings the photo-inhibition selectivity's interval
to include zero. With code 6 alone, 8 of 20 draws with 5 screening trials of each type and 11 of 20 with 10
of each do, and the photo-inhibition selectivity ranges from 0.067 to 0.460 and from 0.055 to 0.356
spikes/s across draws, so there the draw decides the outcome.'''
s=s.replace('md("RESULT8")','md("""'+r8+'""")').replace('md("RESULT10")','md("""'+r10+'""")')
open(p,'w').write(s)
EOF
python $TMPDIR/work/build_nb.py && grep -c "RESULT" entries/gao-2018/earlier_findings.ipynb
```

```
0
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/gao-2018/entry.yaml",
 "old_string": "  runtime_minutes: 25\nhelpers:",
 "new_string": "  runtime_minutes: 25\n- path: earlier_findings.ipynb\n  title: The findings of attempt gao-2018-01, checked on DANDI:000007 version 0.220126.1903\n  runtime_minutes: 3\nhelpers:"
}
```

```
The file entries/gao-2018/entry.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
date -u; python tools/entry.py lock entries/gao-2018 2>&1 | tail -3; python tools/entry.py check entries/gao-2018 2>&1 | tail -15
```

```
Sat Nov 14 17:48:21 UTC 2026
wrote gao-2018/requirements.lock.txt (Python 3.13, with hashes)
0 error(s)
```

**Agent calls Bash**

```bash
git diff --stat entries/gao-2018; time python tools/entry.py all entries/gao-2018 2>&1 | tail -15; date -u
```

```
entries/gao-2018/entry.yaml | 3 +++
 1 file changed, 3 insertions(+)
Installed kernelspec registry-gao-2018 in executed/gao-2018/.venv/share/jupyter/kernels/registry-gao-2018
0 error(s)
pass  reproduce_gao_2018.ipynb  (918 s)
pass  earlier_findings.ipynb  (115 s)

real	17m21.296s
user	8m59.271s
sys	0m55.772s
Sat Nov 14 18:05:49 UTC 2026
```

**Agent calls Bash**

```bash
ls executed/gao-2018; python - <<'EOF'
import nbformat
nb=nbformat.read('executed/gao-2018/earlier_findings.ipynb',4)
for i in (5,8,11,17,20,21):
    c=nb.cells[i]
    for o in c.get('outputs',[]):
        t=o.get('text') or ''
        print(f'== {i}'); print('\n'.join(t.splitlines()[-22:]))
c=nb.cells[14]; t=c.outputs[0]['text']; print('\n'.join(t.splitlines()[-10:]))
EOF
```

```
earlier_findings.ipynb
reproduce_gao_2018.ipynb
result.json
== 5
description of photo_stim_id in the 54 files: {'varchar(8) #': 54}
files with anything under acquisition, stimulus or processing: 0
devices: {'NN 32ch A4x8-5mm-100-200-177, fiber': 34, 'Cambridge NeuroTech 64ch H2 probe, fiber': 20}
codes by group: {'dentate': ['0,3,4'], 'fastigial': ['0,1,2'], 'inhibition': ['0,5', '0,5,6']}
== 8
        subject                                             fields                       genotype             site alm_ml
0    BAYLORCD12  date_of_birth, genotype, sex, species, subject_id  L7-cre x rosa26-lsl-ChR2-EYFP   Fastigial left   -1.5
5    BAYLORCD13  date_of_birth, genotype, sex, species, subject_id  L7-cre x rosa26-lsl-ChR2-EYFP   Fastigial left   -1.5
10   BAYLORCD14  date_of_birth, genotype, sex, species, subject_id  L7-cre x rosa26-lsl-ChR2-EYFP   Fastigial left   -1.5
15    BAYLORCD6  date_of_birth, genotype, sex, species, subject_id                        unknown  Fastigial right   -1.5
19    BAYLORCD8  date_of_birth, genotype, sex, species, subject_id  L7-cre x rosa26-lsl-ChR2-EYFP  Fastigial right   -1.5
24   BAYLORNL12  date_of_birth, genotype, sex, species, subject_id                        unknown    Dentate right   -1.5
29   BAYLORNL14  date_of_birth, genotype, sex, species, subject_id                        unknown    Dentate right   -1.5
35   BAYLORNL15  date_of_birth, genotype, sex, species, subject_id                        unknown  Fastigial right   -1.5
40  anm00314746  date_of_birth, genotype, sex, species, subject_id                        unknown  Fastigial right   -1.5
43  anm00314756  date_of_birth, genotype, sex, species, subject_id                        unknown    Dentate right   -1.5
[... 68 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^[a-z_]*:" attempts/gao-2018-02.yaml; grep -n "^findings:" -A12 attempts/gao-2018-02.yaml | head -20; tail -15 attempts/gao-2018-02.yaml
```

```
1:schema_version: 3
2:id: gao-2018-02
3:datasets:
14:paper: doi:10.1038/s41586-018-0633-x
15:date: 2026-11-14
16:entry: gao-2018
17:provenance:
28:outcomes:
549:inputs: []
550:findings:
669:verifications:
550:findings:
551-- kind: data_missing
552-  statement: >-
553-    Both datasets hold only the ALM recordings during CN photo-activation (34 sessions, 9 mice)
554-    and CN photo-inhibition (20 sessions, 4 mice). The lesion experiments, the behavior-only
555-    sessions (including response-epoch and 1.3 s photostimulation), the 878 CN units, lick times,
556-    video, the VGAT-ChR2-EYFP experiments, the anatomy, and the tenth mouse of the Fig. 2 ALM
557-    recordings are not deposited; 24 of the 46 claims in the claims file cannot be tested.
558-  datasets:
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import yaml,json
c=yaml.safe_load(open('claims/gao-2018.yaml'))
for cl in c['claims']:
    if cl['id'] in ('fig2-preparatory-more-in-alm','fig2-peri-movement-equal','fig3e-alm-increase-decrease','fig1k-inhibition-delay-bias'):
        print(cl['id'],'\n ',cl['criterion'],'\n')
nb=json.load(open('entries/gao-2018/reproduce_gao_2018.ipynb'))
for i in (70,71,72):
    print(i,''.join(nb['cells'][i]['source'])[:1800]); print('----')
EOF
```

```
fig1k-inhibition-delay-bias 
  As fig1h-fastigial-activation-delay-bias (per-mouse test named there as a choice), on delay photo-inhibition trials. The photostimulus is open (readings (a) the 0.5 s early or late delay photo-inhibition of the 7 mice, Extended Data Fig. 2h; (b) the 1.3 s whole delay photo-inhibition of the 3 mice CD12, CD13, CD16, Extended Data Fig. 2g). 

fig2-preparatory-more-in-alm 
  A neuron has preparatory activity when the E2 test is significant in the sample or the delay epoch. The denominator is open (readings (a) all neurons, 1194 and 564; (b) the selective neurons, 980 and 416). Trials as the readings of E2. Reproduced when under one reading both fractions are within tolerance and a chi-square test of the two proportions has p < 0.001 with ALM higher. The ALM fraction alone is tested where the CN neurons are missing. 

fig2-peri-movement-equal 
  A neuron has peri-movement activity when the E2 test is significant in the response epoch, under the response window readings of E2. Denominator as in fig2-preparatory-more-in-alm (open, same readings). Reproduced when under one reading both fractions are within tolerance; a chi-square test of the two proportions is reported (the paper gives none). 

fig3e-alm-increase-decrease 
  Sign of the delay epoch rate change among the neurons of fig3d-alm-altered-by-cn-inhibition. Reproduced when both counts are within tolerance, or, where the dataset holds fewer neurons, the increase fraction (0.55) is within 10%. 

70 **Result: not reproduced.** Of the modulated neurons 122 increase and 106 decrease (all trials), 65
and 41 (correct trials), outside 108 +- 10.8 and 89 +- 8.9. The increase fraction with all trials,
0.535, is within 10% of 0.55, but the criterion uses it only where the dataset holds fewer neurons.
----
71 ## ALM selectivity under CN photostimulation

Population selectivity E3 over selective neurons (E2, correct trials, 1.3 s response window)
tested on more than 3 trials in every condition (c
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
ls paper 2>/dev/null | head; grep -rl "25 kHz\|25kHz\|25,000" paper 2>/dev/null | head -3; grep -rho ".\{150\}25 kHz.\{100\}" paper 2>/dev/null | head -3; date -u
```

```
10.1038-s41586-018-0633-x.supp-41586_2018_633_MOESM1_ESM.pdf
10.1038-s41586-018-0633-x.supp1.pdf
10.1038-s41586-018-0633-x.supp2.pdf
10.1038-s41586-018-0633-x.txt
alm-4.data-description.txt
paper/alm-4.data-description.txt
paper/10.1038-s41586-018-0633-x.txt
Sat Nov 14 18:07:01 UTC 2026
```

**Agent calls Bash**

```bash
grep -n -i "25 kHz\|25kHz\|19.5 kHz\|20 kHz\|sampled at" paper/10.1038-s41586-018-0633-x.txt paper/alm-4.data-description.txt | cut -c1-400
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -i "khz\|kHz\|sampl.\{0,20\}rate" paper/10.1038-s41586-018-0633-x.txt paper/alm-4.data-description.txt | cut -c1-500 | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat > $TMPDIR/work/add.py <<'PYEOF'
import re
p = 'attempts/gao-2018-02.yaml'
s = open(p).read()
new_findings = '''- kind: metadata_insufficient
  found: on_prompt
  statement: >-
    In DANDI:000007 the trial column photo_stim_id has no description beyond its type ("varchar(8) #")
    in all 54 files, and no file holds a laser or photostimulation trace (acquisition, stimulus and
    processing are empty). The codes are 1 and 2 in the fastigial, 3 and 4 in the dentate and 5 and 6
    in the L7-cre x Ai32 sessions; which epoch, duration and power each stands for is not given in the
    files.
  datasets:
  - "000007"
- kind: identifier_missing
  found: on_prompt
  statement: >-
    In DANDI:000007 the subjects anm00314746, anm00314756, anm00314757, anm00314758 and anm00314760
    carry no other identifier, where the paper names these mice AN105 to AN109. By site, anm00314756
    (the one dentate mouse of the five) and anm00314757 (the one with a left fastigial site and right
    ALM) can be matched; anm00314746, anm00314758 and anm00314760 share a right fastigial site and left
    ALM and cannot. The genotype of every mouse that is not L7-cre x Ai32 is "unknown", and
    session_description is empty in all 54 files.
  datasets:
  - "000007"
- kind: metadata_error
  found: on_prompt
  statement: >-
    In DANDI:000007 the units' cell_type column labels 60 units "pyramidal" whose mean waveform has a
    trough-to-peak width under the paper's 0.45 ms (33 under 0.35 ms), and 3 units "unknown". Every
    unit's waveform sampling rate is given as 20000 Hz, including the 34 sessions recorded with the
    32-channel NeuroNexus probe, which the Methods say were sampled at 25,000 Hz; in 14 of those
    sessions the mean waveforms have 37 or 38 samples, against 30 in every other session.
  datasets:
  - "000007"
- kind: other
  about: data
  found: on_prompt
  statement: >-
    In 2 of the 54 sessions of DANDI:000007, BAYLORCD13 20171211 and 20171215, the spikes could not be
    shown to share the clock of the trial table, neither by a rate change after the onset of delay
    photostimulation nor by trial-type selectivity after sample onset. The first holds 15 trials for 38
    units (8 with photostimulation, and 1 and 4 correct lick-right and lick-left control trials), the
    second 7 units. The other 52 sessions show it by one or both contrasts.
  datasets:
  - "000007"
- kind: other
  about: data
  found: on_prompt
  statement: >-
    In DANDI:000007 session BAYLORCD8 20171020 the behavior runs on after the recording ends. Every
    unit's observation interval ends at 7221.77 s, and the last 127 of the 462 trials, from 7223.1 to
    8481.39 s, hold no spike of any unit. The obs_intervals column records this, but an analysis that
    does not apply it counts those trials as silent.
  datasets:
  - "000007"
- kind: methods_unavailable
  found: on_prompt
  statement: >-
    For the population selectivity of Fig. 2c (E3), which epoch fixes each neuron's preferred trial
    type? It decides where the maximum lies; on 1274 selective ALM neurons it lies 0.24 to 0.49 s after
    the go cue when the response epoch fixes the preference, 0.06 to 0.23 s before it with the delay
    epoch, and in the sample epoch in 9 of 10 draws with the sample epoch. For Fig. 3f the random draw
    of the screening trials can decide the outcome; on trials with photostimulation code 6, 8 of 20
    draws with 5 screening trials of each type and 11 of 20 with 10 of each give a photo-inhibition
    selectivity whose bootstrap interval includes zero.
'''
assert s.count('\nverifications:\n') == 1
s = s.replace('\nverifications:\n', '\n' + new_findings.rstrip('\n') + '\nverifications:\n', 1)

rec = '''reconciliation:
  earlier: gao-2018-01
  date: 2026-11-14
  blind: false
  blind_note: >-
    The author run and the three author-revise runs show nothing of gao-2018-01; the audit lines in
    author.md are the record this attempt wrote. The author-answers run, after the outcomes were
    recorded, looked for questions/gao-2018.yaml and printed lines 400 to 470 of
    transcripts/see-2018/author-revise-1.md, which quote the start of gao-2018-01's questions file,
    including its question on the claims file's E3 and the beginning of its reason, that on these data
    the preparatory part of Fig. 2c is similar under every epoch while the peak lies in the response
    epoch only under one. It also printed the first lines of questions/gao-2018.yaml and grep lines of
    other papers' recorder transcripts that name docs/pilot-notes/gao-2018-01.md, without its content.
    That run changed no outcome, note, finding or file of the attempt.
  findings:
  - finding: 1
    status: still_present
    now: 1
    note: >-
      Finding 1 reports the same missing data (CN recordings, lick times, behavior-only sessions,
      VGAT-ChR2-EYFP experiments, anatomy) in both datasets. It counts 24 of 46 claims as untestable
      where gao-2018-01 counted 26 of 45, as the claims file has since gained a claim and gao-2018-02
      also read CRCNS:alm-4.
  - finding: 2
    status: still_present
    now: 14
    note: >-
      In earlier_findings.ipynb the description of photo_stim_id is "varchar(8) #" in all 54 files and
      no file holds anything under acquisition, stimulus or processing. gao-2018-02 read the laser traces
      and code descriptions of CRCNS:alm-4 (its findings 5 and 6), which DANDI:000007 still lacks.
  - finding: 3
    status: still_present
    now: 3
    note: >-
      Finding 3 reports the same trial columns (cue_time and pole_in_time) described as relative to the
      trial start while holding session times; it does not name pole_out_time, which gao-2018-01 also
      listed.
  - finding: 4
    status: still_present
    now: 4
    note: >-
      Finding 4 reports the same disagreement for BAYLORCD12, BAYLORCD13 and BAYLORCD14 (manipulated CN
      on the left, the side of the recorded ALM; BAYLORCD14 in right ALM in Supplemental Table 1).
  - finding: 5
    status: still_present
    now: 15
    note: >-
      In earlier_findings.ipynb the five anm subjects have only the fields date_of_birth, genotype, sex,
      species and subject_id, none naming AN105 to AN109; genotype is "unknown" for the 8 mice that are
      not L7-cre x Ai32, and session_description is empty in 54 of 54 files.
  - finding: 6
    status: still_present
    now: 7
    note: >-
      Finding 7 reports the same excess of units over the paper's counts in the same mice and the 20
      photo-inhibition sessions against 19. Its counts (1084 and 682 pyramidal) come from the cellType
      field, those of gao-2018-01 (1082 and 676) from the width rule.
  - finding: 7
    status: still_present
    now: 16
    note: >-
      In earlier_findings.ipynb 27 units labelled pyramidal are 0.35 to 0.45 ms wide and 33 under 0.35
      ms, 3 are labelled unknown, and all 54 files give 20000 Hz, the 34 NeuroNexus sessions included; 14
      of those have waveforms of 37 or 38 samples against 30 elsewhere.
  - finding: 8
    status: still_present
    now: 17
    note: >-
      With gao-2018-01's contrast 50 of 54 sessions show a locked response and with trial-type
      selectivity 48 of 54; neither shows it in BAYLORCD13 20171211 or 20171215. Of the earlier five,
      BAYLORCD12 20180125 and 20180129 are shown by both contrasts here and anm00314756 20151023 by
      selectivity, so the finding holds for two sessions.
  - finding: 9
    status: still_present
    now: 18
    note: >-
      In earlier_findings.ipynb every unit's observation interval in BAYLORCD8 20171020 ends at 7221.77 s,
      and the 127 trials from 7223.1 to 8481.39 s hold 0 spikes.
  - finding: 10
    status: still_present
    now: 19
    note: >-
      The epoch that fixes the preference moves the Fig. 2c maximum from 0.24 to 0.49 s after the go
      cue (response epoch) to 0.06 to 0.23 s before it (delay epoch). For Fig. 3f no draw of 20 meets the
      criterion with codes 5 and 6 pooled or code 5 alone, and 8 and 11 of 20 do with code 6 alone. The
      preference trial count is also in gao-2018-02's finding 10 (the deposited scripts use 5 of each
      type).
  - finding: 11
    status: still_present
    now: 11
    note: >-
      Finding 11 asks the same question for the same latencies (how a 10 ms bin is placed in time, and
      which window decides modulation), with the start label matching and the centre label not.
  - finding: 12
    status: still_present
    now: 12
    note: >-
      Finding 12 asks the same three questions about the 64.1% and 27.0% fractions, and again only one
      combination matches both (66.3% and 28.4% here).
  outcomes:
  - claim: fig1g-dentate-activation-little-effect
    earlier: reproduced
    note: >-
      Difference in method. Both attempts get the same pooled result (0.873 to 0.835, one-sided p =
      0.108 and 0.107); gao-2018-02 also read the laser traces of CRCNS:alm-4, found two sessions whose
      light disagrees with code 4, and without them finds a drop (p = 0.042), so it records the absence
      as holding in part.
  - claim: fig1k-inhibition-delay-bias
    earlier: partially_reproduced
    note: >-
      Difference in method. gao-2018-01 pooled codes 5 and 6 and judged the bias on CD12 and CD13, the
      paper's mice, which drop on the same trial type. gao-2018-02 took reading (b) as code 6 alone, from
      the code descriptions of CRCNS:alm-4, and counted CD14 with them, which gives mice biased each way.
  - claim: fig2-preparatory-more-in-alm
    earlier: blocked
    note: >-
      Difference in method. Both measured the ALM fraction (0.525 and 0.563); gao-2018-01 blocked the
      claim as the CN half is missing, and gao-2018-02 recorded the ALM half as a partial result, as the
      criterion's last sentence allows. The claims check of 2026-11-14 lists no change to this criterion.
  - claim: fig2-peri-movement-equal
    earlier: blocked
    note: >-
      Difference in method, as for fig2-preparatory-more-in-alm. gao-2018-01 blocked it for the missing
      CN half after measuring 0.572 to 0.587 in ALM; gao-2018-02 measured 0.642 and recorded the ALM half
      as a partial result.
  - claim: fig3e-alm-mean-rate-unchanged
    earlier: partially_reproduced
    note: >-
      Difference in method, the neurons and trials. gao-2018-01 used all 676 units over the width rule
      (3.379 and 3.767 spikes/s, below tolerance); gao-2018-02 used the 486 pyramidal neurons that pass
      the deposited scripts' trial-count rule, with GoodTrials from CRCNS:alm-4 (4.03 and 4.21, within
      tolerance).
  - claim: fig3e-alm-increase-decrease
    earlier: partially_reproduced
    note: >-
      Difference in method, the reading of the criterion. Both find counts above tolerance (158 and 112,
      122 and 106) and an increase fraction within 10% of 0.55; gao-2018-01 counted the fraction toward a
      partial result, gao-2018-02 applied it only where the dataset holds fewer neurons, as the criterion
      says.
  - claim: fig3f-alm-selectivity-abolished-by-cn-inhibition
    earlier: reproduced
    note: >-
      Difference in method. gao-2018-01 judged by most of 20 random draws of the preference trials, on
      438 neurons; gao-2018-02 made one draw on 336 neurons with code 6 trials. In earlier_findings.ipynb,
      with code 6, 8 and 11 of 20 draws meet the criterion, so a single draw can fall either way.
  - claim: fig4g-dentate-effect-recovers
    earlier: not_reproduced
    note: >-
      Difference in method, the latency. Both find the recovery fails; gao-2018-01's latency by the
      paper's method came out at 0.01 to 1.40 ms, outside the tolerance, while gao-2018-02's start label
      gives 3.30 ms, at its lower bound, so it records a partial result. The claims file also gained a
      named test for the fastigial comparison on 2026-11-14.
  - claim: fig4i-fastigial-collapses-cd
    earlier: reproduced
    note: >-
      Difference in method, the sessions and trials of the coding direction. gao-2018-01 used 9
      fastigial and 13 dentate sessions and found no dentate change; gao-2018-02's session rule keeps 8
      and 12 and finds a dentate difference whose interval excludes zero (0.15 to 4.18), which goes away
      without the sessions whose laser traces disagree with their codes.
  protocol: >-
    docs/pilot-notes.md has no section for pilot-15 or any version after pilot-14, so what the change
    did is not recorded there. tools/entry.py names one rule as the protocol's from pilot-15, that a
    finding of kind other or selection_undocumented says whether it is about the data or the paper, and
    that in an attempt on several datasets a finding about the data names its datasets. gao-2018-02,
    on two datasets, follows it; it changes where findings are shown and no outcome.
'''
if not s.endswith('\n'):
    s += '\n'
s += rec
open(p, 'w').write(s)
PYEOF
python $TMPDIR/work/add.py && python tools/entry.py check entries/gao-2018 2>&1 | tail -10
```

```
0 error(s)
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='attempts/gao-2018-02.yaml'
s=open(p).read()
reps=[("""where gao-2018-01 counted 26 of 45, as the claims file has since gained a claim and gao-2018-02
      also read CRCNS:alm-4.""","""where gao-2018-01 counted 26 of 45, as the claims file now has 46 claims and gao-2018-02 tested
      the ALM half of two Fig. 2 claims."""),
("genotype is \"unknown\" for the 8 mice that are\n      not L7-cre x Ai32","genotype is \"unknown\" for the 9 mice that are\n      not L7-cre x Ai32"),
("""and finds a dentate difference whose interval excludes zero (0.15 to 4.18), which goes away
      without the sessions whose laser traces disagree with their codes.""","""and finds a dentate difference whose interval excludes zero (0.15 to 4.18); in the last 400 ms it
      includes zero without the sessions whose laser traces disagree with their codes."""),
("and counted CD14 with them, which gives","and counted CD8 and CD14 with them, which gives")]
for a,b in reps:
    assert s.count(a)==1,a[:40]; s=s.replace(a,b)
open(p,'w').write(s)
EOF
python tools/entry.py check entries/gao-2018 2>&1 | tail -3; git diff --stat; python - <<'EOF'
import yaml
r=yaml.safe_load(open('attempts/gao-2018-02.yaml'))
print(len(r['findings']), [f.get('found') for f in r['findings']])
for f in r['reconciliation']['findings']: print(f['finding'],f['status'],f.get('now'))
EOF
grep -n "—\|rather" attempts/gao-2018-02.yaml entries/gao-2018/earlier_findings.ipynb | head
```

```
0 error(s)
 attempts/gao-2018-02.yaml   | 227 ++++++++++++++++++++++++++++++++++++++++++++
 entries/gao-2018/entry.yaml |   3 +
 tools/agent_run.py          |  15 ++-
 tools/runner/chain.sh       |  97 ++++++++++++-------
 4 files changed, 301 insertions(+), 41 deletions(-)
19 [None, None, None, None, None, None, None, None, None, None, None, None, None, 'on_prompt', 'on_prompt', 'on_prompt', 'on_prompt', 'on_prompt', 'on_prompt']
1 still_present 1
2 still_present 14
3 still_present 3
4 still_present 4
5 still_present 15
6 still_present 7
7 still_present 16
8 still_present 17
9 still_present 18
10 still_present 19
11 still_present 11
12 still_present 12
```

**Agent**

I've written the reconciliation block in `attempts/gao-2018-02.yaml` and added `entries/gao-2018/earlier_findings.ipynb` to `entry.yaml`. Lock, check and run all pass: `reproduce_gao_2018.ipynb` ran in 918 s and `earlier_findings.ipynb` in 115 s, and `python tools/entry.py check entries/gao-2018` gives 0 errors. Nothing is committed. The blind attempt's outcomes, statements, notes, claims file and notebook are unchanged.

**1. Blind: no (`blind: false`).** The author run and the three author-revise runs saw nothing of gao-2018-01. The one hit in `author.md` is the record the author wrote. The author-answers run was looking for `questions/gao-2018.yaml` and printed lines 400 to 470 of `transcripts/see-2018/author-revise-1.md`. Those lines quote the start of gao-2018-01's questions file, including its E3 question and part of its reasoning: that the Fig. 2c peak lies in the response epoch under only one epoch choice. That run came after the outcomes were recorded and changed nothing. Its transcript also shows `head -4 questions/gao-2018.yaml` printing that file's first lines, although the run then says the file does not exist.

**2. Earlier findings**

| # | Earlier finding | Status | now |
|---|---|---|---|
| 1 | Data missing (CN units, licks, behavior-only sessions, …) | still_present | 1 |
| 2 | `photo_stim_id` has no description and there is no laser trace | still_present (checked) | 14 |
| 3 | Event times described as trial-relative but on the session clock | still_present | 3 |
| 4 | Hemispheres disagree with Supplemental Table 1 | still_present | 4 |
| 5 | anm subjects vs AN105–AN109, genotype "unknown", empty session_description | still_present (checked) | 15 |
| 6 | Unit counts above the paper's | still_present | 7 |
| 7 | 60 "pyramidal" units narrower than 0.45 ms; 20 kHz stated where the Methods give 25 kHz | still_present (checked) | 16 |
| 8 | Sessions not shown locked to trial events | still_present (checked; 2 of the earlier 5) | 17 |
| 9 | BAYLORCD8 20171020: 127 trials after the recording ends | still_present (checked) | 18 |
| 10 | Fig. 2c preference epoch; Fig. 3f random draw | still_present (checked) | 19 |
| 11 | Latency bin placement | still_present | 11 |
| 12 | Coding-direction captured fractions | still_present | 12 |

Findings 14 to 19 are added with `found: on_prompt`.
- **Finding 8:** with the earlier attempt's own test, 50 of 54 sessions show a locked response here; a second test based on lick-direction selectivity shows 48. Neither shows it in BAYLORCD13 20171211 or 20171215, so the finding now covers those two sessions only.
- **Finding 10, Fig. 3f part:** the draw decides the outcome only on code 6 trials (8 and 11 of 20 draws meet the criterion). With codes 5 and 6 pooled, no draw does.

**3. New findings of gao-2018-02:** 2, 5, 6, 8, 9, 10 and 13.

**4. Outcomes that differ.** All nine are most likely differences in method; none comes from a change in the dataset.
- **fig1g-dentate-activation-little-effect** (reproduced → partially): gao-2018-02 also used the CRCNS laser traces and found the result depends on two sessions whose light disagrees with their code.
- **fig1k-inhibition-delay-bias** (partially → reproduced): gao-2018-02 used code 6 alone and included CD8 and CD14; gao-2018-01 pooled codes 5 and 6 on CD12 and CD13.
- **fig2-preparatory-more-in-alm and fig2-peri-movement-equal** (blocked → partially): gao-2018-01 blocked them because the CN half is missing. gao-2018-02 recorded the ALM half, as the criterion allows.
- **fig3e-alm-mean-rate-unchanged** (partially → reproduced): different neurons (486 passing the deposited scripts' trial-count rule, against 676 by spike width) and trials.
- **fig3e-alm-increase-decrease** (partially → not reproduced): the two attempts read the criterion's fraction clause differently.
- **fig3f-alm-selectivity-abolished-by-cn-inhibition** (reproduced → not reproduced): gao-2018-01 judged by most of 20 draws on 438 neurons; gao-2018-02 made one draw on 336 neurons, code 6 only.
- **fig4g-dentate-effect-recovers** (not reproduced → partially): the latency method differs. The claims file also gained a named test for the fastigial comparison.
- **fig4i-fastigial-collapses-cd** (reproduced → partially): different session rule and coding-direction trials.

**5. What did not fit**
- **No pilot-15 notes:** `docs/pilot-notes.md` has no section for pilot-15 or any later version. The `protocol` field says so. It also names the one rule `tools/entry.py` attributes to pilot-15: a finding of kind `other` or `selection_undocumented` must say whether it is about the data or the paper, and a data finding in an attempt on several datasets names its datasets.
- **Earlier entry unavailable:** the repository history is a single squashed commit, so `git show $c:entries/gao-2018/...` returns gao-2018-02's entry, not gao-2018-01's. I rebuilt the earlier checks from its record and from its transcripts in `transcripts/gao-2018/attempt-01`.
- **Possible blinding leak:** `blind.sh` did not stop the earlier questions file from reaching the author-answers run, both through another paper's transcript and apparently directly.

## End of run

64 turns, 32 minutes, $3.67 at API prices, result: success.
