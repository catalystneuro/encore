# 000128 · author-revise-2 · run 39823529506

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat transcripts/000128/verifier-2-report.md; ls entries/000128-churchland-2010 entries/000128-churchland-2010/*
```

```
**Verifier report: Churchland et al. 2010 on DANDI:000128 (round 2)**

**1. Outcomes**

The claims file has 22 claims and the attempt record has 22 outcomes:
- 11 reproduced
- 1 partially reproduced (recordings-jarray)
- 3 not reproduced (fig4d-mean-correlation-jarray, fig6-performance-vs-dimensionality, prep-dimensionality)
- 7 blocked: 5 for data_missing, 2 for metadata_insufficient

I agree with all 22. Each one matches the printed outputs and the claims file's criteria:
- **recordings-jarray (partially reproduced):** 182 units fails under every reading (cell 12).
- **fig4d (not reproduced):** p is 0.42 to 0.61, so even the "partially reproduced" rule fails (cell 15).
- **fig6-performance-vs-dimensionality (not reproduced):** best k is 14 and there is no decline (cell 44).
- **prep-dimensionality (not reproduced):** 15 and 18 components (cell 32).
- All the reproduced claims meet their criteria in cells 19, 22, 25, 29, 38, 41, 47, 50, 53, 58 and 61.

**2. Sentences the outputs or the paper do not support**

- **Cell 17 and the fig4d notes.** Cell 17: "The means are positive but less than half the paper's 0.13 and 0.11"; the notes: "The means are positive but below half the paper's."
[... 58 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "Hand over for verification" -A40 docs/protocol.md | head -80; ls attempts 2>/dev/null | grep 000128; ls questions | grep 000128; find . -path ./node_modules -prune -o -name "*000128-churchland-2010-01*" -print
```

```
379:  verification round, with its `reason` (see "Hand over for verification").
380-- **`inputs`**: everything used that is not in the dataset, each with where
381-  it came from (a DOI, or a repository at a commit).
382-- **`findings`**: what the attempt found about the dataset, whatever the
383-  outcomes. These are for the data owner and the archive. The kinds are
384-  `metadata_error`, `data_missing`, `identifier_missing`,
385-  `selection_undocumented`, `methods_unavailable`, `format_error` (files that
386-  break their own format, such as unsorted spike times), `code_mismatch`
387-  (published code that disagrees with the paper or the data),
388-  `paper_inconsistency` (the paper disagrees with itself),
389-  `metadata_insufficient` (a variable without a description or a needed
390-  mapping) and `other`.
391-- **`provenance`**: who is accountable, and for an agent the harness, model
392-  and this protocol's version.
393-
394-If any outcome is `not_reproduced` or `partially_reproduced`, the entry's
395-`README.md` and the notebook's summary carry this sentence: "A failure to
396-reproduce here may be a failure of this attempt, not of the paper: see the
397-reasoning and the differences from the paper's method."
398-
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/000128-churchland-2010-01.yaml; cat questions/000128.yaml
```

```
<persisted-output>
Output too large (32.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/c82e990b-04d7-498a-8f14-e430dd650b73/tool-results/bs10wls9v.txt

Preview (first 2KB):
schema_version: 2
id: 000128-churchland-2010-01
dataset:
  archive: dandi
  id: "000128"
  version: 0.220113.0400
  doi: 10.48324/dandi.000128/0.220113.0400
paper: doi:10.1016/j.neuron.2010.09.015
date: 2026-10-22
entry: 000128-churchland-2010
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
cat /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/c82e990b-04d7-498a-8f14-e430dd650b73/tool-results/bs10wls9v.txt | sed -n 30,400p
```

```
- 2295
  notes: The dataset has 108 conditions (36 mazes in 3 versions). The unit count is 182 (137 held in,
    45 held out), outside 146 plus or minus 14.6, so the three counts do not all match under any
    reading. Reading (a), all successful trials, gives 2869 with the 574 test-file segments, outside
    the tolerance, and 2295 counting the train file alone (the trials with condition labels), within
    it; every unit is observed on every train trial. The test file has its own clock and no delay or
    success column, so whether its trials belong to (a) cannot be settled from the file. Under
    reading (b) M1 keeps 1786 trials with T2, outside the tolerance. The 137 held-in units (a Neural
    Latents Benchmark split) and the 1967 trials with delay > 400 ms are printed but are not readings
    and decide nothing. The answer of 2026-10-22 to the M1 question removed T1's count (1452) from
    reading (b); the outcome is unchanged.
  deviations:
  - Nothing in the dataset says which units or trials the paper used, or whether this session
    (2009-09-25) is the one the paper analysed.
- claim: recordings-single-electrode
  outcome: blocked
  blocked_by: data_missing
  notes: The dandiset holds only the array session of monkey Jenkins. No speed-task data (monkeys A
    and B) and no single-electrode maze recordings are in it, and the paper names no other archive
    for them.
[... 351 more lines not kept]
```

**Agent calls Bash**

```bash
cat questions/000128.yaml; git show --stat HEAD~1 | head
```

```
# Questions from attempt 000128-churchland-2010-01 (author, 2026-10-22) about the claims file
# claims/000128/10.1016-j.neuron.2010.09.015.yaml. Each is asked under docs/protocol.md, Author,
# step 1.6; the attempt runs every reading it can see and records the claims whose outcome depends on
# the answer.
dandiset: "000128"
paper: doi:10.1016/j.neuron.2010.09.015
questions:
- claim: fig6-peri-movement-space-best
  also: [fig3-maze-most-not-maintained, fig6-each-dimensionality, fig6-performance-vs-dimensionality,
    fig7a-shuffled-space-poor]
  attempt: 000128-churchland-2010-01
  asked: 2026-10-22
  question: Header M1 gives two readings of the proto-trial selection, T1 (each velocity component
    must correlate with the condition mean at r > 0.9) and T2 (the two components concatenated). On
    the dataset T1 keeps 1452 of 1967 trials with delay > 400 ms (73.8%), leaves two conditions (the
    straight leftward reaches, whose vertical velocity is flat) with no trial and several with one or
    two, while T2 keeps 1786 (90.8%) and at least 10 per condition. The paper says the selection kept
    typically about 90% of trials. Does that sentence allow T1 to be set aside, or are both readings
    to stand?
  passage: Supplemental Experimental Procedures, Task design and behavioral control ("Subsequent
[... 87 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 400,600p /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/c82e990b-04d7-498a-8f14-e430dd650b73/tool-results/bs10wls9v.txt
```

```
with no EMG.
    response: No change.
  - claim: fig7a-shuffled-space-poor
    agrees: true
    outcome: reproduced
    reason: Shuffled space is below the unshuffled one at every k (best 0.227 against 0.518) and below
      the worst kinematic variant (0.414 to 0.421), so H1 and H2 hold.
    response: No change.
  - claim: fig7b-window-start-slide
    agrees: true
    outcome: reproduced
    reason: J-array ratio is 0.959 (K1) or 0.957 (K2), within 0.97 plus or minus 0.097 under reading J2.
      The 0.94 value for monkeys A and B cannot be tested. The best k is an edge value, not a true peak.
    response: The conclusion and notes now say both best k values sit at the upper end of the range.
      Outcome unchanged.
  - claim: ap-location-no-effect-on-correlation
    agrees: true
    outcome: blocked
    reason: Asset and version metadata have no anatomical coordinates; x, y, z are all NaN and every
      unit points to PMd electrode rows. A two-level variant is possible only if the unit-id leading
[... 128 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000128-churchland-2010; python - <<'EOF'
import json
nb=json.load(open('reproduce_churchland_2010.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    print(f"=== {i} {c['cell_type']} {c.get('metadata',{}).get('tags','')} len={len(s)}")
    print(s[:300])
EOF
```

```
=== 0 markdown  len=3158
# Reproducing Churchland et al. (2010) from dandiset 000128

**Paper.** Churchland MM, Cunningham JP, Kaufman MT, Ryu SI, Shenoy KV (2010). Cortical preparatory
activity: representation of movement or first cog in a dynamical machine? *Neuron* 68:387-400,
doi:10.1016/j.neuron.2010.09.015.

**Dataset
=== 1 code  len=543
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import diptest
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
fr
[... 423 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('reproduce_churchland_2010.ipynb'))
for i in (0,9,10,15,17,31,32,33,58,59,64):
    c=nb['cells'][i]
    print(f"=== {i}"); print(''.join(c['source']))
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            print('--OUT--', ''.join(o.get('text','')) or o.get('data',{}).get('text/plain',''))
EOF
grep -n "T2\|91%\|90.8\|T-matrix\|0.43" README.md
```

```
=== 0
# Reproducing Churchland et al. (2010) from dandiset 000128

**Paper.** Churchland MM, Cunningham JP, Kaufman MT, Ryu SI, Shenoy KV (2010). Cortical preparatory
activity: representation of movement or first cog in a dynamical machine? *Neuron* 68:387-400,
doi:10.1016/j.neuron.2010.09.015.

**Dataset.** DANDI:000128 (MC_Maze, Neural Latents Benchmark), version `0.220113.0400`,
doi:10.48324/dandi.000128/0.220113.0400. The paper cites no version of the dataset (it predates it).
This is the only published version, so it is pinned. The draft (modified 2023-06-20) holds the same two
assets with the same blobs (checked below), so the choice changes nothing the analysis uses.

**Claims file.** `claims/000128/10.1016-j.neuron.2010.09.015.yaml`, written from the accepted author
manuscript in PubMed Central (PMC2991102) with its supplement, and checked by a second reader. The
claims file fixes every method; the labels M1 to M9, T2, S1 and so on are its readings.

**Answers taken up.** A reader answered three questions of this attempt on 2026-10-22
(`questions/000128.yaml`), and the claims file was updated. The proto-trial selection (M1) is now reading
T2 alone: T1, which kept 73.8% of trials and emptied two conditions, is set aside. The tuning measure (M6)
is now reading S1 (the range over conditions) alone: S2, the SD over conditions, is set aside. For
[... 239 more lines not kept]
```

**Agent calls Bash**

```bash
cd ../..; ls paper; grep -rn -i "T was c\|This T-matrix\|7-10 dim\|required to account" paper | head
```

```
<persisted-output>
Output too large (125.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/c82e990b-04d7-498a-8f14-e430dd650b73/tool-results/bgfxee8fl.txt

Preview (first 2KB):
10.1016-j.neuron.2010.09.015.supp.pdf
10.1016-j.neuron.2010.09.015.txt
10.1038-nature11129.txt
paper/10.1016-j.neuron.2010.09.015.txt:7:Neuron 319 nihpa 8809320 Neuron 0896-6273 1097-4199 pmc-is-collection-domain yes pmc-collection-title NIHPA Author Manuscripts PMC2991102 PMC2991102.1 2991102 2991102 NIHMS240235 21040842 10.1016/j.neuron.2010.09.015 NIHMS240235 NIHPA240235 1 Article Cortical preparatory activity: representation of movement or first cog in a dynamical machine? Churchland MM 1 Cunningham JP 1 3 Kaufman MT 2 Ryu SI 1 4 Shenoy KV 1 2 5 1 Dept. of Electrical Engineering, Stanford University, Stanford CA, 94305, USA 2 Neurosciences Program, Stanford University, Stanford CA, 94305, USA 3 Dept. of Engineering, University of Cambridge, Cambridge, UK 4 Dept. of Neurosurgery, Palo Alto Medical Foundation, Palo Alto CA, 94301, USA 5 Dept. of Bioengineering, Stanford University, Stanford CA, 94705, USA 4 11 2010 68 3 191982 387 400 06 10 2010 04 11 2011 04 11 2011 06 10 2011 14 10 2026 This file is available for text mining. It may also be used consistent with the principles of fair use under the copyright law. Summary The motor cortices are active during both movement and movement preparation. A common assumption is that preparatory activity constitutes a sub-threshold form of movement activity: a neuron active during rightwards movements becomes modestly active during preparation of a rightwards movement. We asked whether this pattern of activity is in fact observed. We found that it was not: at the level of a single neuron, preparatory tuning was weakly correlated with movement-period tuning. Yet somewhat paradoxically, preparatory tuning could be captured by a preferred direction in an abstract ‘space’ that describ
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
pdftotext paper/10.1016-j.neuron.2010.09.015.supp.pdf $TMPDIR/supp.txt 2>&1 | head -3; grep -n -i -B3 -A3 "This T-matrix" $TMPDIR/supp.txt | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2010.09.015.supp.pdf",
 "pages": "1-20"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python - <<'EOF'
import re,zlib
d=open('paper/10.1016-j.neuron.2010.09.015.supp.pdf','rb').read()
try:
    import pypdf
    r=pypdf.PdfReader('paper/10.1016-j.neuron.2010.09.015.supp.pdf')
    t='\n'.join(p.extract_text() for p in r.pages)
except Exception as e:
    print('nopypdf',e); t=''
i=t.find('T-matrix also')
print(t[i-1500:i+700])
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python - <<'EOF'
import re,zlib
d=open('paper/10.1016-j.neuron.2010.09.015.supp.pdf','rb').read()
out=[]
for m in re.finditer(rb'stream\r?\n(.*?)endstream',d,re.S):
    try: s=zlib.decompress(m.group(1))
    except Exception: continue
    txt=b''.join(re.findall(rb'\((.*?)(?<!\\)\)',s))
    if txt: out.append(txt.decode('latin1'))
t='\n'.join(out)
for key in ['T-matrix also','c ','each row containing']:
    i=t.find(key); print(key, i)
i=t.find('T-matrix also'); print(t[i-1200:i+600])
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd entries/000128-churchland-2010 && python - <<'EOF'
import json
p='reproduce_churchland_2010.ipynb'
nb=json.load(open(p))
C=nb['cells']
def get(i): return ''.join(C[i]['source'])
def put(i,s): C[i]['source']=s.splitlines(keepends=True)
def rep(i,a,b):
    s=get(i); assert a in s,(i,a); put(i,s.replace(a,b))
rep(17,"""The means are positive but less than half
the paper's 0.13 and 0.11, outside the tolerances of 0.013 and 0.011.""","""Both means are positive and outside the
tolerances of 0.013 and 0.011: the Pearson mean is below half the paper's 0.13 (0.065), and the Spearman mean is
65% of the paper's 0.11.""")
s=get(32); i=s.index("# variants that decide nothing"); put(32,s[:i].rstrip()+"\n")
put(33,"""**Result: not reproduced.** No reading gives 7 to 11 components. With the 83 prep-tuned neurons (N1, S1), 90% of
the variance needs 15 components; with all 182 units (N2), 18. The supplement defines the matrix as the claims file
does ("T was c×n with each row containing the mean preparatory activity for every neuron", Supplemental
Experimental Procedures, Estimating the upper limit of PD performance), built from "all neurons", which is reading
N2 (18). It says "7-10 dimensions were required", while the main text says "at least 7-10 dimensions", which 15 and
18 would meet; whether the claim is a range or a lower bound is asked in `questions/000128.yaml`, and the claim is
decided as the claims file states it. The condition means here average 10 to 27 trials per condition (median 17),
and their noise may add components; the claims file does not fix how the paper handled this.
""")
s=get(31)
print(s)
EOF
```

```
## prep-dimensionality

> Preparatory activity is moderately high-dimensional; depending on the dataset, 7 to 10 dimensions capture 90% of its variance.

The c x n matrix of M4 preparatory rates, columns mean-centred, PCA; the number of components for 90%.
Reproduced when within 7 to 11 under one reading (N1: prep-tuned neurons, S1; N2: all neurons).
```

**Agent calls Bash**

```bash
cd ../..; ls executed/000128-churchland-2010/; python - <<'EOF'
import json
nb=json.load(open('executed/000128-churchland-2010/reproduce_churchland_2010.ipynb'))
for i in (10,32,58):
    for o in nb['cells'][i].get('outputs',[]):
        print(i, ''.join(o.get('text','')))
EOF
```

```
Exit code 1
ls: cannot access 'executed/000128-churchland-2010/': No such file or directory
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'executed/000128-churchland-2010/reproduce_churchland_2010.ipynb'
```

**Agent calls Bash**

```bash
cd entries/000128-churchland-2010 && python - <<'EOF'
import json
p='reproduce_churchland_2010.ipynb'
nb=json.load(open(p))
C=nb['cells']
def get(i): return ''.join(C[i]['source'])
def put(i,s):
    l=s.splitlines(keepends=True)
    if l and l[-1].endswith('\n'): l[-1]=l[-1][:-1]
    C[i]['source']=l
def rep(i,a,b):
    s=get(i); assert a in s,(i,a); put(i,s.replace(a,b))
rep(10,'''median {int(np.median(bc[bc > 0]))}")''','''median {int(np.median(bc[bc > 0]))}, max {bc.max()}")''')
rep(17,"""The means are positive but less than half
the paper's 0.13 and 0.11, outside the tolerances of 0.013 and 0.011.""","""Both means are positive and outside the
tolerances of 0.013 and 0.011: the Pearson mean is below half the paper's 0.13 (0.065), and the Spearman mean is
65% of the paper's 0.11.""")
s=get(32); i=s.index("# variants that decide nothing"); put(32,s[:i].rstrip()+"\n")
put(33,"""**Result: not reproduced.** No reading gives 7 to 11 components. With the 83 prep-tuned neurons (N1, S1), 90% of
the variance needs 15 components; with all 182 units (N2), 18. The supplement defines the matrix as the claims file
does ("T was c×n with each row containing the mean preparatory activity for every neuron", Supplemental
Experimental Procedures, Estimating the upper limit of PD performance), from "all neurons", which is reading N2
(18). It says "7-10 dimensions were required", while the main text says "at least 7-10 dimensions", which 15 and
18 would meet; whether the claim is a range or a lower bound is asked in `questions/000128.yaml`, and the claim is
decided as the claims file states it. The condition means here average 10 to 27 trials per condition (median 17),
and their noise may add components; the claims file does not fix how the paper handled this.""")
rep(59,"with a central 95% of about -0.43 to 0.43 under every reading, and 0.08 lies inside it in all eight.",
 "with central 95% ranges whose lower bounds run from -0.430 to -0.385 and upper bounds from 0.350 to 0.428\nover the eight readings, and 0.08 lies inside all of them.")
rep(64,"fixed reading T2 (91% of trials kept, every condition; the paper says typically about 90%), and\nreading T1 (74%, two conditions empty) was set aside.",
 "fixed reading T2 (1786 trials kept, 90.8% of the 1967 trials with delay > 400 ms and 77.8% of all 2295\ntrain trials, every condition; the paper says typically about 90% of all trials), and reading T1 (73.8% of\nthe trials with delay > 400 ms, two conditions empty) was set aside.")
rep(64,"(a question on the claim's reading is open)","(a question on range or lower bound is open)")
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
git diff --stat; grep -n "91%\|74%\|question" README.md
```

```
/bin/bash: line 1: cd: entries/000128-churchland-2010: No such file or directory
34:The outcomes follow the answers of 2026-10-22 to the attempt's questions (`questions/000128.yaml`): the
```

**Agent calls Bash**

```bash
pwd; git -C  status --short
```

```
entries/000128-churchland-2010
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
ls -a; ls -a ../.. | head -40
```

```
.
..
.claude
README.md
entry.yaml
mcmaze.py
reproduce_churchland_2010.ipynb
requirements.in
requirements.lock.txt
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
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
p='reproduce_churchland_2010.ipynb'
nb=json.load(open(p))
C=nb['cells']
def get(i): return ''.join(C[i]['source'])
def put(i,s):
    l=s.splitlines(keepends=True)
    C[i]['source']=l
def rep(i,a,b):
    s=get(i); assert a in s,(i,a); put(i,s.replace(a,b))
rep(10,'''median {int(np.median(bc[bc > 0]))}")''','''median {int(np.median(bc[bc > 0]))}, max {bc.max()}")''')
rep(17,"""The means are positive but less than half
the paper's 0.13 and 0.11, outside the tolerances of 0.013 and 0.011.""","""Both means are positive and outside the
tolerances of 0.013 and 0.011: the Pearson mean is below half the paper's 0.13 (0.065), and the Spearman mean is
65% of the paper's 0.11.""")
s=get(32); i=s.index("# variants that decide nothing"); put(32,s[:i].rstrip())
put(33,"""**Result: not reproduced.** No reading gives 7 to 11 components. With the 83 prep-tuned neurons (N1, S1), 90% of
the variance needs 15 components; with all 182 units (N2), 18. The supplement defines the matrix as the claims file
does ("T was c×n with each row containing the mean preparatory activity for every neuron", Supplemental
Experimental Procedures, Estimating the upper limit of PD performance), from "all neurons", which is reading N2
(18). It says "7-10 dimensions were required", while the main text says "at least 7-10 dimensions", which 15 and
18 would meet; whether the claim is a range or a lower bound is asked in `questions/000128.yaml`, and the claim is
decided as the claims file states it. The condition means here average 10 to 27 trials per condition (median 17),
and their noise may add components; the claims file does not fix how the paper handled this.""")
rep(59,"with a central 95% of about -0.43 to 0.43 under every reading, and 0.08 lies inside it in all eight.",
 "with central 95% ranges whose lower bounds run from -0.430 to -0.385 and upper bounds from 0.350 to 0.428\nover the eight readings, and 0.08 lies inside all of them.")
rep(64,"fixed reading T2 (91% of trials kept, every condition; the paper says typically about 90%), and\nreading T1 (74%, two conditions empty) was set aside.",
 "fixed reading T2 (1786 trials kept, 90.8% of the 1967 trials with delay > 400 ms and 77.8% of all 2295\ntrain trials, every condition; the paper says typically about 90% of all trials), and reading T1 (73.8% of\nthe trials with delay > 400 ms, two conditions empty) was set aside.")
rep(64,"(a question on the claim's reading is open)","(a question on range or lower bound is open)")
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
git diff --stat; sed -n 25,60p README.md
```

```
.../reproduce_churchland_2010.ipynb                | 50 ++++++++--------------
 1 file changed, 18 insertions(+), 32 deletions(-)
| Anterior against posterior sites | Blocked: metadata insufficient (2 claims) |
| Speed task, single-electrode and EMG data | Blocked: data missing (5 claims) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000128-churchland-2010-01.yaml`](../../attempts/000128-churchland-2010-01.yaml).

The outcomes follow the answers of 2026-10-22 to the attempt's questions (`questions/000128.yaml`): the
proto-trial selection is reading T2 and the tuning measure reading S1.

- `reproduce_churchland_2010.ipynb`: the analysis. It takes about two minutes, most of it computing
  smoothed firing rates.
- `mcmaze.py`: streaming the files, the trial selection, condition-mean firing rates, the PD fits and
  the kinematic and task spaces. Other notebooks on this dandiset can import it.
```

**Agent calls Bash**

```bash
sed -n 1,24p README.md; git diff | head -30
```

```
# Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010) from dandiset 000128

Tests the findings of [Churchland et al. (2010)](https://doi.org/10.1016/j.neuron.2010.09.015) that can
be tested on [DANDI:000128](https://dandiarchive.org/dandiset/000128/0.220113.0400) (MC_Maze), which
holds the paper's J-array dataset: one session of monkey Jenkins on the maze task, 108 conditions,
recorded with two 96-electrode arrays. The speed task (monkeys A and B), the single-electrode maze
recordings (monkey J) and EMG are not in it.

| Claim | Outcome |
|---|---|
| The J-array dataset: 146 units, 108 conditions, about 2166 trials | Partially reproduced (182 units) |
| Mean correlation of preparatory and peri-movement tuning 0.13 (J-array) | Not reproduced |
| No separate concordant and opposing populations | Reproduced |
| The correlation declines from about 200 ms before movement onset to near zero | Reproduced |
| Population averages lose their relation to preparatory tuning by movement onset | Reproduced |
| 7 to 10 dimensions capture 90% of preparatory variance | Not reproduced |
| Most maze neurons do not keep their tuning | Reproduced |
| PD performance is highest in the peri-movement space | Reproduced |
| The peri-movement space wins at almost every dimensionality | Reproduced |
| PD performance peaks near 10 dimensions and then declines | Not reproduced (still rising at 14) |
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;nb=json.load(open('reproduce_churchland_2010.ipynb'));print(''.join(nb['cells'][32]['source'])[-200:])"
```

```
l.sum()), k90, 7 <= k90 <= 11, np.round(cum[:3], 3)))
print(pd.DataFrame(rows, columns=["trials", "neurons", "n", "components for 90%", "within 7 to 11", "first 3 cumulative"]).to_string(index=False))
```

**Agent**

Good. The README has no 91% wording, so it needs no change there. Now I'll run the entry.

**Agent calls Bash**

```bash
cd ../.. && python tools/entry.py all entries/000128-churchland-2010 2>&1 | tail -30
```

```
Installed kernelspec registry-000128-churchland-2010 in executed/000128-churchland-2010/.venv/share/jupyter/kernels/registry-000128-churchland-2010
0 error(s)
pass  reproduce_churchland_2010.ipynb  (125 s)
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('executed/000128-churchland-2010/reproduce_churchland_2010.ipynb'))
for i in (10,12,15,19,22,25,29,32,38,41,44,47,50,53,56,58,61):
    for o in nb['cells'][i].get('outputs',[]):
        t=''.join(o.get('text','')) or ''.join(o.get('data',{}).get('text/plain',''))
        print(f'--{i}--'); print(t[:2500])
EOF
```

```
--10--
T2: kept 1786 of 1967 trials with delay > 400 ms (90.8%); conditions with no trial 0; trials per condition min 10, median 17, max 22
T1 (set aside): kept 1452 of 1967 trials with delay > 400 ms (73.8%); conditions with no trial 2; trials per condition min 1, median 14, max 21

--10--
rates computed in 61 s

--10--
T2: 108 conditions; preparatory rates 0.0 to 35.4 spikes/s; peri-movement rates 0.0 to 56.3 spikes/s
T2 S1: preparatory tuning > 5 spikes/s: 83 of 182 units; also peri-movement tuning >= 1.5x: 17 (tuning range 0.2 to 34.0 spikes/s)

--12--
                                                           quantity              reading  dataset  paper  tolerance  within
                                               units in the dataset                count      182    146       14.6   False
                                    units held in (benchmark split)        not a reading      137    146       14.6    True
                                                         conditions                count      108    108        0.0    True
trials, all successful trials of the session (train and test files)                  (a)     2869   2166      216.6   False
       trials, successful trials with condition labels (train file) (a), train file only     2295   2166      216.6    True
                                                 trials, M1 with T2                  (b)     1786   2166      216.6   False
                                        trials, delay > 400 ms only        not a reading     1967   2166      216.6    True
[... 136 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000128-churchland-2010 && python - <<'EOF'
import json
p='reproduce_churchland_2010.ipynb'
nb=json.load(open(p))
c=nb['cells'][33]; s=''.join(c['source']); a="average 10 to 27 trials"; assert a in s
c['source']=s.replace(a,"average 10 to 22 trials").splitlines(keepends=True)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
git diff --stat
```

```
.../reproduce_churchland_2010.ipynb                | 50 ++++++++--------------
 1 file changed, 18 insertions(+), 32 deletions(-)
```

**Agent calls Bash**

```bash
cd ../..; grep -n "T1\|S2 \|0.43\|below half\|0.40 to" attempts/000128-churchland-2010-01.yaml | head -60
```

```
39:    and decide nothing. The answer of 2026-10-22 to the M1 question removed T1's count (1452) from
64:    r is 0.457. The answers of 2026-10-22 set aside T1 and S2. The earlier record was
65:    blocked (methods_underspecified) because T1 with S1 gave no neuron at 0.72 (largest r 0.411) and
66:    S2 selected no neuron; with T2 and S1 fixed, the claim is reproduced.
76:    (P1 0.47, P2 0.42, P3 0.61). The means are positive but below half the paper's. Per-neuron r runs
78:    2026-10-22 set aside T1 and S2; the earlier record gave T1 with S1 (0.025 and 0.054, recorded as
79:    measured) and T2 with S1, and S2 gave no neuron. The measured values are now those of T2, and the
96:    T1 and S2 readings, which had given the same outcome (T1) or no neuron (S2); the outcome is
105:    2026-10-22 removed the T1 and S2 readings, which had given the same outcome (T1) or no neuron
122:    and M6 removed T1 and S2; the outcome is unchanged.
131:    The answers of 2026-10-22 set aside T1 and S2. The earlier record was blocked
132:    (methods_underspecified) because under T1 with S1 the peri-movement space (0.281) fell below the
147:    spaces by 0.002 to 0.004 only. The answers of 2026-10-22 set aside T1 and
148:    S2. The earlier record was blocked (methods_underspecified) because T1 gave 11 or 12 wins and
149:    T2 with S2 failed L1 in some combinations; with T2 and S1 fixed, the claim is reproduced.
160:    answers of 2026-10-22 set aside T1 and S2. The earlier record was blocked
161:    (methods_underspecified) because under T1 the claim held (best at k = 5, 0.281, falling to
176:    decide nothing, such matrices need 55 to 61 components. The answers of 2026-10-22 set aside T1 (18 and 20
177:    components, recorded earlier as measured) and S2 (4 components with 6 units); the measured value
192:    The answers of 2026-10-22 set aside T1 and S2. The earlier record was blocked
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='attempts/000128-churchland-2010-01.yaml'
t=open(p).read()
R=[
("""    r is 0.457. The answers of 2026-10-22 set aside T1 and S2. The earlier record was
    blocked (methods_underspecified) because T1 with S1 gave no neuron at 0.72 (largest r 0.411) and
    S2 selected no neuron; with T2 and S1 fixed, the claim is reproduced.""",
"""    r is 0.457. The answers of 2026-10-22 set aside T1 and S2. The earlier record was
    blocked (methods_underspecified) because T1 with S1 gave no neuron at 0.72 and S2 selected no
    neuron; with T2 and S1 fixed, the claim is reproduced. The notebook no longer prints T1 or S2
    values."""),
("""    (P1 0.47, P2 0.42, P3 0.61). The means are positive but below half the paper's. Per-neuron r runs""",
"""    (P1 0.47, P2 0.42, P3 0.61). Both means are positive; the Pearson mean is below half the paper's
    (0.065) and the Spearman mean is 65% of the paper's. Per-neuron r runs"""),
("""    2026-10-22 set aside T1 and S2; the earlier record gave T1 with S1 (0.025 and 0.054, recorded as
    measured) and T2 with S1, and S2 gave no neuron.""",
"""    2026-10-22 set aside T1 and S2; the earlier record gave T1 with S1 (recorded then as measured)
    and T2 with S1, and S2 gave no neuron; the notebook no longer prints T1 or S2 values."""),
("""    (methods_underspecified) because under T1 with S1 the peri-movement space (0.281) fell below the
    kinematic (0.295) and kitchen-sink (0.313) spaces;""",
"""    (methods_underspecified) because under T1 with S1 the peri-movement space fell below the
    kinematic and kitchen-sink spaces (values no longer printed);"""),
("""because T1 gave 11 or 12 wins and
    T2 with S2 failed L1""","""because T1 failed L1 and L2 and
    T2 with S2 failed L1"""),
]
for a,b in R:
    assert a in t,a; t=t.replace(a,b)
open(p,'w').write(t)
EOF
sed -n 155,215p attempts/000128-churchland-2010-01.yaml; sed -n 240,250p attempts/000128-churchland-2010-01.yaml
```

```
outcome: not_reproduced
  notebook: reproduce_churchland_2010.ipynb
  output: claim:fig6-performance-vs-dimensionality
  notes: Under T2 with S1 (83 neurons) performance rises from 0.140 at k = 1 to 0.518 at k = 14, so
    it improves with dimensionality, but the best k is 14, above 10, and performance does not
    decline at k = 14. Two of the criterion's three conditions fail, and the part of the statement
    they test (a peak in a middle range and a decline beyond about 10 dimensions) is not found. The
    answers of 2026-10-22 set aside T1 and S2. The earlier record was blocked
    (methods_underspecified) because under T1 the claim held (best at k = 5, 0.281, falling to
    -0.287 at k = 14); with T2 fixed, it is not reproduced.
  deviations:
  - J-array only.
- claim: prep-dimensionality
  outcome: not_reproduced
  notebook: reproduce_churchland_2010.ipynb
  output: claim:prep-dimensionality
  measured: 15
  notes: Under T2, 90% of the variance of the preparatory condition-mean matrix needs 15 components
    with the 83 neurons of N1 (S1) and 18 with all 182 units (N2). Neither is within 7 to 11.
    Trial-averaged rates from at least 10 trials per condition (median 17) carry noise that adds
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='attempts/000128-churchland-2010-01.yaml'
t=open(p).read()
R=[
("""    (methods_underspecified) because under T1 the claim held (best at k = 5, 0.281, falling to
    -0.287 at k = 14); with T2 fixed, it is not reproduced.""",
"""    (methods_underspecified) because under T1 the claim held (values no longer printed); with T2
    fixed, it is not reproduced."""),
("""    Trial-averaged rates from at least 10 trials per condition (median 17) carry noise that adds
    dimensions; the paper's procedure may differ in this. The main text says "at least 7-10
    dimensions", which 15 and 18 would meet, and the supplement's "This T-matrix" may mean a
    conditions x (neurons x times) matrix; both are asked in questions/000128.yaml. As variants that
    decide nothing, such matrices need 55 to 61 components. The answers of 2026-10-22 set aside T1 (18 and 20
    components, recorded earlier as measured) and S2 (4 components with 6 units); the measured value
    is now 15 and the outcome is unchanged.""",
"""    The supplement defines the matrix as the claims file does ("T was c×n with each row containing
    the mean preparatory activity for every neuron"), from "all neurons", which is reading N2 (18),
    and says "7-10 dimensions were required"; the main text says "at least 7-10 dimensions", which
    15 and 18 would meet. Whether the claim is a range or a lower bound is asked in
    questions/000128.yaml. The condition means average 10 to 22 trials per condition (median 17),
    and their noise may add components; the claims file does not fix how the paper handled this.
    The answers of 2026-10-22 set aside T1 (recorded earlier as measured) and S2; the measured value
    is now 15 and the outcome is unchanged."""),
("""    set aside T1 and S2 (0.904 to 0.972, all within
    tolerance; 0.918 under T1 was recorded earlier as measured); the measured value is now 0.959 and
    the outcome is unchanged.""",
"""    set aside T1 and S2, which had all been within tolerance (T1 was recorded earlier as
    measured); the measured value is now 0.959 and the outcome is unchanged."""),
("""  notes: Over 1000 draws of 25 initial states, the correlation has medians -0.041 to 0.019 and central
    95% ranges of about -0.43 to 0.43 under the eight readings; 0.08 lies inside all of them.""",
"""  notes: Over 1000 draws of 25 initial states, the correlation has medians -0.041 to 0.019, and the
    central 95% ranges have lower bounds of -0.430 to -0.385 and upper bounds of 0.350 to 0.428 under
    the eight readings; 0.08 lies inside all of them."""),
]
for a,b in R:
    assert a in t,a; t=t.replace(a,b)
open(p,'w').write(t)
EOF
tail -5 attempts/000128-churchland-2010-01.yaml; grep -n "^- date\|^  reviewed\|^  by" attempts/000128-churchland-2010-01.yaml
```

```
- claim: fig8-model-pd-perfect
    agrees: true
    outcome: reproduced
    reason: Smallest R squared and smallest leave-one-out performance are both 1.0 under all readings.
    response: No change.
281:- date: 2026-10-22
283:  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the
285:  reviewed: The round-1 handover, the executed notebook with the conclusions and summary removed, the
```

**Agent calls Bash**

```bash
sed -n 278,290p attempts/000128-churchland-2010-01.yaml
```

```
statement: 14 trials have a negative delay (as low as -3 ms), where the go cue precedes the recorded
    target onset.
verifications:
- date: 2026-10-22
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the
    notebook)
  reviewed: The round-1 handover, the executed notebook with the conclusions and summary removed, the
    helper module and the claims file, with the paper under paper/.
  results:
  - claim: recordings-jarray
    agrees: true
    outcome: partially_reproduced
```

**Agent calls Bash**

```bash
cat >> attempts/000128-churchland-2010-01.yaml <<'EOF'
- date: 2026-10-22
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the
    notebook)
  reviewed: The round-2 handover, the full executed notebook with conclusions and summary, the helper
    module, the claims file and the attempt record, with the paper under paper/.
  results:
  - claim: recordings-jarray
    agrees: true
    outcome: partially_reproduced
    reason: 182 units fails under every reading (cell 12). Each row of the table is now labelled by
      reading, the held-in units and the delay > 400 ms count are marked as not readings, and reading
      (a) is shown as 2869 and as 2295. Reading (a) stays undecidable, but the outcome does not depend
      on it, because the unit count fails either way. The Summary's "T2 (91% of trials kept)" is
      ambiguous next to the paper's "~90% of all trials", as 90.8% is of the 1967 trials with delay >
      400 ms and 77.8% of all 2295 train trials.
    response: The Summary now gives T2's 1786 trials as 90.8% of the 1967 trials with delay > 400 ms
      and 77.8% of all 2295 train trials, and T1's 73.8% as a share of the trials with delay > 400 ms.
      The README has no such percentage. Outcome unchanged.
  - claim: recordings-single-electrode
    agrees: true
    outcome: blocked
    reason: Agrees; the outcome matches the outputs and the claims file's criteria.
    response: No change.
  - claim: fig2b-example-concordant-tuning
    agrees: true
    outcome: blocked
    reason: Agrees; the outcome matches the outputs and the claims file's criteria.
    response: No change.
  - claim: fig2ce-example-opposing-tuning
    agrees: true
    outcome: blocked
    reason: Agrees; the outcome matches the outputs and the claims file's criteria.
    response: No change.
  - claim: fig3-maze-most-not-maintained
    agrees: true
    outcome: reproduced
    reason: Meets its criterion (cell 19). Every selected neuron is now printed with its id digit, its
      two tunings, r and Spearman r, and the texts say fig3 rests on unit 1581.
    response: The notes no longer quote the T1 value that the notebook does not print. Outcome
      unchanged.
  - claim: fig4d-mean-correlation-jarray
    agrees: true
    outcome: not_reproduced
    reason: p is 0.42 to 0.61, so even the "partially reproduced" rule fails (cell 15). "Less than half
      the paper's 0.13 and 0.11" holds for Pearson (0.051 < 0.065) but fails for Spearman, 0.072 being
      65% of 0.11. The notes quote T1 values (0.025 and 0.054) the notebook no longer prints. The
      dataset has 182 units, not 146, and nothing records which units or trials the paper used; only
      17 neurons pass the selection, so the outcome may come from the selection, not the data. This
      stays unresolved.
    response: Cell 17 and the notes now say the Pearson mean is below half the paper's (0.065) and the
      Spearman mean is 65% of the paper's. The T1 values were removed from the notes. The selection
      stays a recorded deviation, as the claims file fixes it. Outcome unchanged.
  - claim: fig4abc-mean-correlation-single-electrode
    agrees: true
    outcome: blocked
    reason: Agrees; the outcome matches the outputs and the claims file's criteria.
    response: No change.
  - claim: fig4-no-separate-populations
    agrees: true
    outcome: reproduced
    reason: Meets its criterion (cell 22); the texts say the tests have little power.
    response: No change.
  - claim: fig4e-correlation-time-course
    agrees: true
    outcome: reproduced
    reason: Meets its criterion (cell 25).
    response: No change.
  - claim: suppfig1-population-averages
    agrees: true
    outcome: reproduced
    reason: Meets its criterion (cell 29). "Positive by construction" is now stated in cell 30.
    response: No change.
  - claim: fig6-peri-movement-space-best
    agrees: true
    outcome: reproduced
    reason: Meets its criterion (cell 38). The edge k is now stated.
    response: The notes no longer quote T1 values that the notebook does not print. Outcome unchanged.
  - claim: fig6-each-dimensionality
    agrees: true
    outcome: reproduced
    reason: Meets its criterion (cell 41). The lost comparison is printed, the 2-D initial-velocity
      space (0.238 against 0.223), with margins at k = 1 of 0.0024 to 0.0041.
    response: The notes no longer quote the T1 win counts that the notebook does not print. Outcome
      unchanged.
  - claim: fig6-performance-vs-dimensionality
    agrees: true
    outcome: not_reproduced
    reason: Best k is 14 and there is no decline (cell 44). The notes quote T1 values (best at k = 5,
      0.281, falling to -0.287) the notebook no longer prints; these are history, not support for any
      current outcome.
    response: The T1 values were removed from the notes. Outcome unchanged.
  - claim: prep-dimensionality
    agrees: true
    outcome: not_reproduced
    reason: 15 and 18 components (cell 32). The round-1 T-matrix point is withdrawn. The supplement
      defines the matrix ("T was c × n with each row containing the mean preparatory activity for
      every neuron"), so the claims file's c × n matrix is the paper's, the 55 to 61 component
      variants test a reading the paper rules out, and "all neurons" points to reading N2 (18
      components). The supplement says "7-10 dimensions were required", so the claims file's
      two-sided reading is defensible, not a misreading; the open question should drop the T-matrix
      part. What still separates the result from the paper is the method, trial-averaged rates from 10
      to 27 trials per condition carrying noise that may add components, which the claims file does
      not fix. The notes quote T1 (18 and 20) and S2 (4 components) values no longer printed.
    response: The conditions x (neurons x times) variants were removed from cell 32. Cell 33 and the
      notes now quote the supplement's definition, say "all neurons" points to N2, and keep the range
      or lower bound point as the open question; the question in questions/000128.yaml no longer asks
      about the T-matrix. Cell 10 now prints the largest trial count per condition, which is 22, not
      27, and the texts say 10 to 22. The T1 and S2 values were removed from the notes. Outcome
      unchanged.
  - claim: fig6e-summary-across-datasets
    agrees: true
    outcome: blocked
    reason: Agrees; the outcome matches the outputs and the claims file's criteria.
    response: No change.
  - claim: fig7a-shuffled-space-poor
    agrees: true
    outcome: reproduced
    reason: Meets its criterion (cell 47).
    response: No change.
  - claim: fig7b-window-start-slide
    agrees: true
    outcome: reproduced
    reason: Meets its criterion (cell 50). The notes quote values (0.904 to 0.972, and 0.918 under T1)
      the notebook no longer prints.
    response: Those values were removed from the notes. Outcome unchanged.
  - claim: ap-location-no-effect-on-correlation
    agrees: true
    outcome: blocked
    reason: The electrode groups and the id digits are now printed (cell 4). Nothing maps a digit to
      an array, so the block remains correct.
    response: No change.
  - claim: fig7c-anterior-posterior-performance
    agrees: true
    outcome: blocked
    reason: As for ap-location-no-effect-on-correlation, nothing maps a digit to an array.
    response: No change.
  - claim: fig7d-pd-consistency
    agrees: true
    outcome: reproduced
    reason: Meets its criterion (cell 53).
    response: No change.
  - claim: fig8-model-weak-correlation
    agrees: true
    outcome: reproduced
    reason: Cell 58 prints lower bounds of -0.385 to -0.430 and upper bounds of 0.350 to 0.428, so
      "about -0.43 to 0.43 under every reading" is the outer envelope, not each reading's interval;
      the round-1 wording "about -0.40 to 0.40" is also loose. The outcome is unaffected, because 0.08
      lies inside every interval.
    response: Cell 59 and the notes now give the lower bounds (-0.430 to -0.385) and upper bounds
      (0.350 to 0.428). The round-1 reason is left as given. Outcome unchanged.
  - claim: fig8-model-pd-perfect
    agrees: true
    outcome: reproduced
    reason: Meets its criterion (cell 61).
    response: No change.
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python - <<'EOF'
p='questions/000128.yaml'
t=open(p).read()
i=t.index("- claim: prep-dimensionality")
new='''- claim: prep-dimensionality
  attempt: 000128-churchland-2010-01
  asked: 2026-10-22
  question: The claim's statement and its range of 7 to 11 read the paper's 7-10 as a two-sided range. The
    supplement says "7-10 dimensions were required", but the main text says "at least 7-10 dimensions". Is
    the claim a range or a lower bound?
  passage: Results, PD performance in a variety of spaces, paragraph 2 ("because the dimensionality of
    preparatory activity itself is moderately high (at least 7-10 dimensions, methods)"); Supplemental
    Experimental Procedures, Estimating the upper limit of PD performance ("This T-matrix also allows us to
    estimate the dimensionality of preparatory activity, depending on the dataset, 7-10 dimensions were
    required to capture 90% of the data variance").
  why: Raised by the round-1 verifier. On the c x n matrix of preparatory epoch means, which the supplement
    defines ("T was c×n with each row containing the mean preparatory activity for every neuron"), the
    attempt finds 15 (N1) and 18 (N2) components, outside 7 to 11 but at least 7, so the outcome is not
    reproduced as a range and would be reproduced as a lower bound. The round-2 verifier judges the
    two-sided reading defensible. An earlier version of this question also asked which matrix "This
    T-matrix" means; the supplement's preceding sentence settles that, and that part is withdrawn.
'''
t=t[:i]+new
open(p,'w').write(t)
EOF
git diff questions/ | head -50
```

```
diff --git a/questions/000128.yaml b/questions/000128.yaml
index e57165af..1ad72457 100644
--- a/questions/000128.yaml
+++ b/questions/000128.yaml
@@ -83,16 +83,17 @@ questions:
 - claim: prep-dimensionality
   attempt: 000128-churchland-2010-01
   asked: 2026-10-22
-  question: The claim's statement and its range of 7 to 11 read the paper's 7-10 as a two-sided range, but the
-    main text says "at least 7-10 dimensions". Is the claim a range or a lower bound? And the quoted
-    supplement sentence begins "This T-matrix"; does it mean the c x n matrix of preparatory epoch means
-    that the criterion uses, or a conditions x (neurons x times) matrix of preparatory rates, or the
-    peri-movement T-matrix of M5?
+  question: The claim's statement and its range of 7 to 11 read the paper's 7-10 as a two-sided range. The
+    supplement says "7-10 dimensions were required", but the main text says "at least 7-10 dimensions". Is
+    the claim a range or a lower bound?
   passage: Results, PD performance in a variety of spaces, paragraph 2 ("because the dimensionality of
     preparatory activity itself is moderately high (at least 7-10 dimensions, methods)"); Supplemental
     Experimental Procedures, Estimating the upper limit of PD performance ("This T-matrix also allows us to
-    estimate the dimensionality of preparatory activity").
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='questions/000128.yaml'
t=open(p).read()
a='''estimate the dimensionality of preparatory activity, depending on the dataset, 7-10 dimensions were
    required to capture 90% of the data variance").'''
b='''estimate the dimensionality of preparatory activity" and "7-10 dimensions were required to capture 90%
    of the data variance").'''
assert a in t; open(p,'w').write(t.replace(a,b))
EOF
python -c "import yaml;yaml.safe_load(open('questions/000128.yaml'));yaml.safe_load(open('attempts/000128-churchland-2010-01.yaml'))" && python tools/entry.py all entries/000128-churchland-2010 2>&1 | tail -5
```

```
Installed kernelspec registry-000128-churchland-2010 in executed/000128-churchland-2010/.venv/share/jupyter/kernels/registry-000128-churchland-2010
0 error(s)
pass  reproduce_churchland_2010.ipynb  (122 s)
```

**Agent calls Bash**

```bash
git diff -U0 | grep '^+' | grep -n -i "—\|rather\|[a-z]: [a-z]" | head; python tools/entry.py check entries/000128-churchland-2010 2>&1 | tail -3; python - <<'EOF'
import json
nb=json.load(open('executed/000128-churchland-2010/reproduce_churchland_2010.ipynb'))
print(''.join(nb['cells'][10]['outputs'][0]['text'])[:200])
EOF
```

```
23:+  notes: Over 1000 draws of 25 initial states, the correlation has medians -0.041 to 0.019, and the
27:+  kind: agent
28:+  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the
30:+  reviewed: The round-2 handover, the full executed notebook with conclusions and summary, the helper
33:+  - claim: recordings-jarray
34:+    agrees: true
35:+    outcome: partially_reproduced
42:+    response: The Summary now gives T2's 1786 trials as 90.8% of the 1967 trials with delay > 400 ms
45:+  - claim: recordings-single-electrode
46:+    agrees: true
0 error(s)
T2: kept 1786 of 1967 trials with delay > 400 ms (90.8%); conditions with no trial 0; trials per condition min 10, median 17, max 22
T1 (set aside): kept 1452 of 1967 trials with delay > 400 ms (73.8%
```

**Agent calls Bash**

```bash
git status --short | grep -v '^?? \.\|^?? scripts'
```

```
M attempts/000128-churchland-2010-01.yaml
 M entries/000128-churchland-2010/reproduce_churchland_2010.ipynb
 M questions/000128.yaml
```

**Agent**

All 22 outcomes are unchanged, and none has a `proposed` change. The round-2 verifier agreed with every outcome, and nothing in my revision gave a reason to change one. I re-ran `python tools/entry.py all entries/000128-churchland-2010` after the last edit: it passes with 0 errors, `entry.py check` also gives 0 errors, and the conclusions match the new numbers.

**Text corrected to match the outputs:**
- **fig4d (cell 17 and notes):** the "less than half" sentence now holds only where it is true. The Pearson mean, 0.051, is below half of 0.13 (0.065). The Spearman mean, 0.072, is 65% of 0.11.
- **fig8-model-weak-correlation (cell 59 and notes):** the range is now given for each reading. The lower bounds run from -0.430 to -0.385 and the upper bounds from 0.350 to 0.428, where the old text gave the outer envelope "-0.43 to 0.43". The verifier's round-1 reason ("about -0.40 to 0.40") stays in the record as it gave it.
- **Summary (cell 64):** T2 is now described as 1786 trials, which is 90.8% of the 1967 trials with delay > 400 ms and 77.8% of all 2295 train trials. T1's 73.8% is now stated as a share of the same base. The README contains no such percentage, so it needed no change.
- **Notes on several claims:** I removed values from the earlier record that the notebook no longer prints. These were in fig4d, fig6-performance-vs-dimensionality, fig7b and prep-dimensionality, which the verifier listed. I did the same for fig3, fig6-peri-movement-space-best and fig6-each-dimensionality, which it did not list.

**prep-dimensionality:**
- The verifier withdrew its T-matrix point, and I checked the supplement text myself. It defines the matrix as "T was c×n …", which is the claims file's matrix. So I removed the conditions × (neurons × times) variants from cell 32, since they test a reading the paper rules out.
- Cell 33 and the notes now quote that definition. They also say that "all neurons" points to reading N2, which gives 18 components.
- I added the maximum trial count per condition to cell 10. It is 22, not the 27 the verifier wrote, and the texts now say 10 to 22.
- The question in `questions/000128.yaml` no longer asks about the T-matrix. It now asks only whether the claim is a range or a lower bound, and quotes the supplement's "7-10 dimensions were required" next to the main text's "at least".

**Record:** round 2 is now under `verifications` in the attempt record, with the verifier's reasons and my response for each of the 22 claims.

**Not done:** the verifier's remaining point about fig4d, that the paper's unit and trial selection is not recorded, cannot be settled with this dataset. It stays a recorded deviation. Nothing is committed, as the workflow commits the changes.

## End of run

34 turns, 9 minutes, result: success.
