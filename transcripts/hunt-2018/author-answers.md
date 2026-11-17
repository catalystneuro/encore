# hunt-2018 · author-answers · run 43637187098

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cd  ls; ls entries/hunt-2018; cat questions/hunt-2018.yaml; wc -l docs/protocol.md
```

```
Sat Nov 14 20:28:24 UTC 2026
LICENSE
LICENSE-data
README.md
attempts
bunfig.toml
claims
docs
encore_science
entries
executed
n-desk.png
n-phone.png
n-phone2.png
node_modules
ov-papers-rows.png
package-lock.json
package.json
paper
papers
[... 74 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -80
```

```
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
656:### Round 2: with the author's conclusions
[... 1 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 186,
 "limit": 420
}
```

```
186	### 6. Answer questions
187	
188	A reader is asked only when the author or a verifier believes the claims file
189	misreads the paper: a wrong expected value, the wrong panel, a claim that does
190	not say what the paper says (author, step 1.6, and "Hand over for
191	verification"). A method detail the claims file lacks is not asked: the author
192	takes it from the paper. The reader, who has not seen the data, checks each
193	question against the paper and decides whether the claims file is to change.
194	Where it is, the reader amends the claim, and the question's `answer` says
195	what changed and why, citing the passage; where it is not, the answer says why
196	the claim stands. The reader marks each question answered in
197	`questions/<paper>.yaml`.
198	
199	## Author
200	
201	The workflow puts the paper under `paper/`, as for the reader. Read it to
202	understand the claims, their data and their figures. The claims file still
203	decides what is tested: do not change a claim's statement, expected values or
204	criterion. A method detail the claims file lacks is taken from the paper
205	(step 6).
[... 400 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls claims attempts | grep hunt; ls executed/hunt-2018 2>/dev/null; grep -n "figs1cd-fewer-cues-more-accurate\|fig7a-ofc-value-difference-neurons\|choice-accuracy" claims/hunt-2018.yaml
```

```
hunt-2018-01.yaml
hunt-2018.yaml
handover
reproduce_hunt_2018.ipynb
result.json
163:- id: choice-accuracy-ev
196:- id: choice-accuracy-observed
240:- id: figs1cd-fewer-cues-more-accurate
252:    expected value (as choice-accuracy-ev, reading (a)); (B) the choice of the higher expected value
253:    of the pictures observed (as choice-accuracy-observed, under its readings). Trials are pooled
680:- id: fig7a-ofc-value-difference-neurons
709:  - fig7a-ofc-value-difference-neurons
710:  criterion: As fig7a-ofc-value-difference-neurons, a neuron counted when it passes at any of the
```

**Agent calls Bash**

```bash
cd  sed -n 160,275p claims/hunt-2018.yaml; echo ----; sed -n 600,740p claims/hunt-2018.yaml
```

```
but its columns sum to 198 ACC, 195 OFC and 156 DLPFC (189 + 9, 183 + 12, 135 + 21), and it
    lists 29 sessions for M and 24 for F. Reproduced when the region totals match under one
    reading; the table's agreement with the data is reported either way.
- id: choice-accuracy-ev
  statement: Monkeys F and M chose the option with the higher expected value on 76.6% and 79.8% of
    trials.
  source: Results, Experimental paradigm and subject behaviour, paragraph 2; Figure 1b
  quote: They chose the option with higher expected value on 76.6% and 79.8% of trials (monkeys F
    (n=25 sessions) and M (n=32 sessions) respectively)
  expected:
  - quantity: choices of the higher expected value, monkey F
    value: 76.6
    tolerance: 7.66
    unit: '%'
  - quantity: choices of the higher expected value, monkey M
    value: 79.8
    tolerance: 7.98
    unit: '%'
  criterion: Expected value is probability times magnitude of the option (Methods, Task). Trials
    are the completed option and attribute trials. The paper does not say how trials of equal
[... 238 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "O2\b\|O3\b" claims/hunt-2018.yaml | head; grep -n "claim: \|outcome:" attempts/hunt-2018-01.yaml | head -80; wc -l attempts/hunt-2018-01.yaml
```

```
76:# - O2, the significance level for counting single neurons (Figures 7 and 8). Not stated in the
79:# - O3, the time bin for single-neuron tests at cues 2 and 3 (Figure 7). Readings (a) 250 ms after
690:    open details O2 and O3. The trial type of the cue 3 tests is open; the text says "at cue 3 of
695:    passing in either. The significance level is not in the text read (O2); a third reading, (c)
700:    time points, under one reading of O3, the trial type and the significance level.
721:    and 15, 16 (after cue 3) is significant; open details O2 and O3 (the 300 ms reading matches the
724:    when the ACC proportion exceeds both others for all four EVs under one reading of O3, at both
725:    readings of O2; partially reproduced for three of four.
746:    O2; the binomial test against a chance rate equal to that level. Reproduced when, under one
24:- claim: sessions-and-trials
25:  outcome: reproduced
37:- claim: neuron-counts
38:  outcome: reproduced
54:- claim: choice-accuracy-ev
55:  outcome: reproduced
62:- claim: chose-on-partial-information
63:  outcome: reproduced
73:- claim: choice-accuracy-observed
74:  outcome: reproduced
84:- claim: figs1ab-cue-weights
[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 70,85p claims/hunt-2018.yaml; sed -n 1,23p attempts/hunt-2018-01.yaml; sed -n 54,113p attempts/hunt-2018-01.yaml; sed -n 300,330p attempts/hunt-2018-01.yaml; sed -n 380,423p attempts/hunt-2018-01.yaml
```

```
#   name Pearson's correlation). Region differences by Fisher r-to-Z of independent correlations,
#   n = the neurons of each region.
#
# Details the paper leaves open, shared by several criteria (each criterion names those it needs):
# - O1, sidedness of the Fisher r-to-Z test between regions. Readings (a) two-sided; (b) one-sided
#   in the predicted direction.
# - O2, the significance level for counting single neurons (Figures 7 and 8). Not stated in the
#   text read (the legends are missing). Readings (a) p < 0.05; (b) p < 0.01, each two-sided on the
#   OLS coefficient or contrast.
# - O3, the time bin for single-neuron tests at cues 2 and 3 (Figure 7). Readings (a) 250 ms after
#   the cue, as Figure 5B-F/K; (b) 300 ms after the cue, as Figure 6A.
# - O4, how trials are split for the projections of Figure 6. The Methods say odd against even
#   trials, each half used once for weights and once for projection, then averaged; the Results say
#   "100 random splits" into halves, averaged. Readings (a) odd/even; (b) 100 random half splits.
# - O5, the five reaction-time bins ("five separate bins depending upon response time from Cue 1
#   onset"). Readings (a) quintiles of reaction time within each session; (b) quintiles of the
schema_version: 3
id: hunt-2018-01
datasets:
- archive: crcns
[... 154 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "verifications\|^[a-z_]*:" attempts/hunt-2018-01.yaml; python - <<'E'
import json
nb=json.load(open('entries/hunt-2018/reproduce_hunt_2018.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    print(i,c['cell_type'],c.get('metadata',{}).get('tags'),repr(s[:90]))
E
```

```
1:schema_version: 3
2:id: hunt-2018-01
3:datasets:
9:paper: doi:10.1038/s41593-018-0239-5
10:date: 2026-11-14
11:entry: hunt-2018
12:provenance:
23:outcomes:
385:findings:
0 markdown None '# Reproducing Hunt, Malalasekera et al. (2018) from CRCNS pfc-7\n\nPaper: Hunt, Malalasekera'
1 code None 'import os\nos.environ.setdefault("OMP_NUM_THREADS", "1")\nos.environ.setdefault("OPENBLAS_NU'
2 markdown None '## Loading\n\nThe file listing and checksums, the units table, the two behavioural files (on'
3 code None 'listing = pfc7.listing()\nmd5 = pfc7.checksums()\nREAD = ["behavioural_data/Miles_InfoGather'
4 markdown None '## Data check'
5 code ['sanity'] 'zips = listing[listing.key.str.match(r"pfc-7/live/neuronal_data/[FM]\\d{3}\\.zip")]\nzip_sess'
6 markdown None 'The GLM written here (`pfc7.fit_glm`) is checked against the T-statistics the authors stor'
7 code ['sanity'] 'G = {u: pfc7.fit_glm(d, with_cpd=(int(d["brain_region"]) == 3)) for u, d in U.items()}\npri'
8 markdown None '### Clock check\n\nEvery stream shares the clock of the trial table: the cue 1 rasters are c'
9 code ['sanity'] 'ofc_sel = [u for u in U if int(U[u]["brain_region"]) == 3 and info.loc[u, "info_rate"] >= '
10 markdown None "## Unit selection\n\nUnits in ACC, DLPFC and OFC with mean rate of at least 1 Hz. The paper'"
[... 138 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
nb=json.load(open('entries/hunt-2018/reproduce_hunt_2018.ipynb'))
for i in [0,24,25,26,31,32,33,116,117,118,119,120,121,122,148]:
    print('=====',i); print(''.join(nb['cells'][i]['source']))
E
```

```
===== 0
# Reproducing Hunt, Malalasekera et al. (2018) from CRCNS pfc-7

Paper: Hunt, Malalasekera, de Berker, Miranda, Farmer, Behrens & Kennerley (2018), "Triple
dissociation of attention and decision computations across prefrontal cortex", Nature
Neuroscience 21, 1471-1481, doi:10.1038/s41593-018-0239-5.

Data: CRCNS data set pfc-7 (doi:10.6080/K0PZ5712), read anonymously from the public S3 bucket
`crcnsarchive` under `pfc-7/live/`. CRCNS data sets are not versioned, so the version is
recorded as `unversioned`; the only published copy is the one under `live/` (data description
version 0.5, September 6, 2018), and it is the one pinned here. The MD5 sums of the files read,
from the data set's `checksums.md5`, are printed below, so that a later change is detectable.

Claims: `claims/hunt-2018.yaml`, written from the version of record (PMC6331040) with its
supplement. The paper's MATLAB scripts are files of the data set (`scripts.zip`); where the
claims file leaves a detail open and a script settles it, the script is cited (see `pfc7.py`).

All 40 claims of the claims file are tested; none is blocked. Outcomes are in the summary at the end.

| Claim | Tested | Claim | Tested |
[... 272 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat executed/hunt-2018/result.json | head -40; python - <<'E'
import json
nb=json.load(open('executed/hunt-2018/reproduce_hunt_2018.ipynb'))
for i in [32,117,121,147]:
    for o in nb['cells'][i].get('outputs',[]):
        print(''.join(o.get('text','')))
E
```

```
{
 "entry": "hunt-2018",
 "python": "3.13",
 "results": [
  {
   "notebook": "reproduce_hunt_2018.ipynb",
   "ok": true,
   "seconds": 804,
   "error": null
  }
 ]
}
script's measure (mean over sessions of accuracy on seen values; mean |EV difference|):
                   acc     vd
subject npv250               
F       2       90.188  0.268
        3       82.631  0.227
        4       82.270  0.219
M       2       93.652  0.272
        3       85.196  0.239
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
nb=json.load(open('entries/hunt-2018/reproduce_hunt_2018.ipynb'))
for i in [1,3,19]:
    print('=====',i); print(''.join(nb['cells'][i]['source']))
E
```

```
===== 1
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import resource
import time
import zlib

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats

import pfc7

T0 = time.time()
pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 40)

[... 39 more lines not kept]
```

**Agent**

Now I'll write the new figs1cd cell and test it on the behaviour data alone.

**Agent calls Bash**

```bash
cd entries/hunt-2018; mkdir -p $TMPDIR; cat > $TMPDIR/new_cell.py <<'E'
# Reading (B): accuracy on the expected values of the pictures observed, under the readings of
# choice-accuracy-observed (acc_seen above), trials pooled over sessions; the pictures observed
# are those the count of pictures uses
rows = []
for col in ["npv250", "npv"]:
    for sb in ["F", "M"]:
        b = beh[beh.subject == sb]
        for n in (2, 3, 4):
            bb = b[b[col] == n]
            rows.append(dict(count=col, subject=sb, n=n, **{rd: acc_seen(bb, col, rd) for rd in ["a", "b", "c", "script"]}))
s1c_obs = pd.DataFrame(rows).set_index(["count", "subject", "n"]).sort_index()
print("reading (B), % correct on the pictures observed, trials pooled:")
print(s1c_obs.round(2))
for col in ["npv250", "npv"]:
    for rd in ["a", "b", "c", "script"]:
        ok = {sb: bool(s1c_obs.loc[(col, sb, 2), rd] > max(s1c_obs.loc[(col, sb, 3), rd], s1c_obs.loc[(col, sb, 4), rd]))
              for sb in ["F", "M"]}
        print(f"count {col}, reading (B{rd}): accuracy 2 > 3 and 2 > 4, F {ok['F']}, M {ok['M']}")
E
cat > $TMPDIR/test.py <<'E'
import time, json
T0=time.time()
nb=json.load(open('reproduce_hunt_2018.ipynb'))
src=lambda i:''.join(nb['cells'][i]['source'])
exec(src(1))
info = pfc7.units_info()
beh = pd.concat([pfc7.load_behaviour("M"), pfc7.load_behaviour("F")], ignore_index=True)
exec(src(19).split("r = pd.DataFrame")[0])
exec(src(25).split("rows = {}")[0])
exec(src(32).split("rows = []")[0])
exec(open(__import__('os').environ['TMPDIR']+'/new_cell.py').read())
print(time.time()-T0)
E
python $TMPDIR/test.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/test.py", line 5, in <module>
    exec(src(1))
    ~~~~^^^^^^^^
  File "<string>", line 8, in <module>
ModuleNotFoundError: No module named 'matplotlib'
```

**Agent calls Bash**

```bash
cd  ls -a; ls ~/.cache 2>/dev/null; grep -n "venv\|def cmd_run\|uv " tools/entry.py | head -20
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
[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 545,560p tools/entry.py; ls -a executed/hunt-2018/
```

```
stamp = None if fresh else reusable(entry_dir, output_dir, max_minutes)
    if stamp:
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
.
..
.clean-run.json
.venv
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/hunt-2018; time ../../executed/hunt-2018/.venv/bin/python $TMPDIR/test.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/test.py", line 5, in <module>
    exec(src(1))
    ~~~~^^^^^^^^
  File "<string>", line 14, in <module>
ModuleNotFoundError: No module named 'pfc7'

real	0m2.422s
user	0m1.432s
sys	0m0.158s
```

**Agent calls Bash**

```bash
cd entries/hunt-2018; time PYTHONPATH=. ../../executed/hunt-2018/.venv/bin/python $TMPDIR/test.py
```

```
reading (B), % correct on the pictures observed, trials pooled:
                      a      b      c  script
count  subject n                             
npv    F       2  92.54  85.77  95.00   93.09
               3  78.00  74.12  82.61   80.60
               4  76.63  72.93  78.97   79.55
       M       2  89.29  64.10  94.89   92.31
               3  84.09  80.87  86.58   86.03
               4  79.17  75.34  79.95   81.66
npv250 F       2  90.24  81.35  92.42   91.20
               3  82.67  78.79  86.46   84.97
               4  79.81  76.32  84.41   82.76
       M       2  94.62  84.58  96.59   95.19
               3  85.98  82.01  87.16   87.86
               4  81.70  76.74  82.58   84.62
count npv250, reading (Ba): accuracy 2 > 3 and 2 > 4, F True, M True
count npv250, reading (Bb): accuracy 2 > 3 and 2 > 4, F True, M True
count npv250, reading (Bc): accuracy 2 > 3 and 2 > 4, F True, M True
count npv250, reading (Bscript): accuracy 2 > 3 and 2 > 4, F True, M True
count npv, reading (Ba): accuracy 2 > 3 and 2 > 4, F True, M True
[... 8 more lines not kept]
```

**Agent**

Under the observed-picture measure, pooled over sessions, 2-picture trials have the highest accuracy in both monkeys under every reading. So figs1cd now passes. Next I'll edit the notebook.

**Agent calls Bash**

```bash
cd entries/hunt-2018; python - <<'E'
import json, os
p='reproduce_hunt_2018.ipynb'
nb=json.load(open(p))
C=nb['cells']
def setsrc(i, s): C[i]['source']=s.splitlines(keepends=True)
assert C[31]['source'][0].startswith('## figs1cd') and C[116]['source'][0].startswith('## fig7a')
setsrc(31, """## figs1cd-fewer-cues-more-accurate

> Choices were more often optimal on trials where 2 pictures were viewed than on trials with 3
> or 4, because trials ended early when the first two cues gave a larger value difference.

The number of pictures viewed is taken from InfoGathering_Behaviour.m (`num_pics_viewed250`,
used for Supplementary Figure 1c/d); the raw count of fixated pictures is shown too. The claims
file, as amended after a reader's answer (questions/hunt-2018.yaml), allows two measures of
accuracy: (A) the choice of the higher true expected value, reading (a) of choice-accuracy-ev
(ties left out); (B) the choice of the higher expected value of the pictures observed, under the
readings of choice-accuracy-observed. Trials are pooled over sessions; the script's mean over
sessions is shown as a variant.""")
setsrc(33, """**Result: reproduced.** Under measure (B), with trials pooled and the script's count of
pictures, accuracy on 2-picture trials is the highest in both monkeys under every reading of
choice-accuracy-observed: under reading (a) F 90.24% against 82.67% and 79.81% on 3 and 4
pictures, M 94.62% against 85.98% and 81.70%. The mean value difference is largest on 2-picture
trials in both monkeys under both readings (true expected values, F 0.266 against 0.229 and 0.219,
M 0.271 against 0.240 and 0.228). Under measure (A) accuracy on 2-picture trials is not the
highest (F 74.96% against 76.10% and 79.62%; M 78.83% against 78.79% and 81.51%). The script's
mean over sessions gives the same order as (B) (F 90.19% against 82.63% and 82.27%; M 93.65%
against 85.20% and 83.69%). With the raw count of fixated pictures, (B) holds in both monkeys under
readings (a), (c) and the script's, and in F only under (b).""")
src=open(os.environ['TMPDIR']+'/new_cell.py').read().rstrip('\n')
new={"cell_type":"code","execution_count":None,"metadata":{"tags":["claim:figs1cd-fewer-cues-more-accurate"]},"outputs":[],"source":src.splitlines(keepends=True)}
C.insert(33,new)
# indices shift by one from here
i=117; assert C[i]['source'][0].startswith('## fig7a')
setsrc(i, """## fig7a-ofc-value-difference-neurons

> At all three time points (cue 2 against cue 1, cue 3 against cue 1, cue 3 against cue 2), a
> greater proportion of single neurons encoded value difference between attended and unattended
> cues in OFC than in ACC and DLPFC.

Units SEL5 (Fig7_single_neurons_cue2and3.m). The significance level has three readings in the
claims file, as amended after a reader's answer (questions/hunt-2018.yaml): p < 0.05 (|T| > 1.96),
p < 0.01 (|T| > 2.576), and (c) |T| > 1.64 on each of the three tests, the script's threshold (its
comment reads `norminv(0.05)`). The claim holds when OFC leads at all three tests under one
reading of the bin, the trial types and the level.""")
i=120; assert C[i]['source'][0].startswith('**Result: partially')
setsrc(i, """**Result: reproduced.** With the Figure 5 trial types (reading a), OFC has the largest
proportion at all three tests at 250 ms and p < 0.05 (OFC 6.0, 4.4, 6.6% against ACC 5.3, 3.2,
4.8% and DLPFC 1.5, 2.2, 2.2%), at 300 ms and p < 0.01 (1.6, 1.6, 3.3% against at most 1.5, 1.6,
1.5%... see the printed table) and with the script's threshold at both bins (250 ms: 8.2, 7.7,
11.0% against at most 6.3, 4.8, 7.4%). It fails at 250 ms with p < 0.01 and at 300 ms with
p < 0.05, and under the attribute-trial reading (b) in every combination but none. At 250 ms and
p < 0.05 none of the six pairwise chi-square tests is below 0.05 (smallest p = 0.084).""")
i=123; assert C[i]['source'][0].startswith('**Result: reproduced')
nb['cells']=C
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
E
git diff --stat
```

```
entries/hunt-2018/reproduce_hunt_2018.ipynb | 76 ++++++++++++++++++++++-------
 1 file changed, 58 insertions(+), 18 deletions(-)
```

**Agent**

I left two sloppy phrases in the fig7a result text, so I'm rewriting it.

**Agent calls Bash**

```bash
cd entries/hunt-2018; python - <<'E'
import json
p='reproduce_hunt_2018.ipynb'
nb=json.load(open(p)); C=nb['cells']
i=120; assert C[i]['source'][0].startswith('**Result: reproduced.** With the Figure 5')
s="""**Result: reproduced.** With the Figure 5 trial types (reading a), OFC has the largest
proportion at all three tests at 250 ms and p < 0.05 (OFC 6.0, 4.4, 6.6% against ACC 5.3, 3.2,
4.8% and DLPFC 1.5, 2.2, 2.2%), at 300 ms and p < 0.01 (OFC 1.6, 1.6, 3.3% against ACC 1.1, 0.5,
1.1% and DLPFC 1.5, 1.5, 1.5%), and with the script's threshold at both bins (250 ms: OFC 8.2,
7.7, 11.0% against ACC 6.3, 4.8, 7.4% and DLPFC 6.0, 3.0, 3.0%). It fails at 250 ms with p < 0.01
and at 300 ms with p < 0.05, and under the attribute-trial reading (b) in every combination. The
differences are small: at 250 ms and p < 0.05 none of the six pairwise chi-square tests is below
0.05 (smallest p = 0.084)."""
C[i]['source']=s.splitlines(keepends=True)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
E
git diff reproduce_hunt_2018.ipynb | head -30; tail -c 200 reproduce_hunt_2018.ipynb | od -c | tail -3; git show HEAD:entries/hunt-2018/reproduce_hunt_2018.ipynb | tail -c 20 | od -c
```

```
diff --git a/entries/hunt-2018/reproduce_hunt_2018.ipynb b/entries/hunt-2018/reproduce_hunt_2018.ipynb
index a31b09d..ba1f1d7 100644
--- a/entries/hunt-2018/reproduce_hunt_2018.ipynb
+++ b/entries/hunt-2018/reproduce_hunt_2018.ipynb
@@ -735,8 +735,12 @@
     "> or 4, because trials ended early when the first two cues gave a larger value difference.\n",
     "\n",
     "The number of pictures viewed is taken from InfoGathering_Behaviour.m (`num_pics_viewed250`,\n",
-    "used for Supplementary Figure 1c/d); the raw count of fixated pictures is shown too. Accuracy is\n",
-    "reading (a) of choice-accuracy-ev (ties left out)."
+    "used for Supplementary Figure 1c/d); the raw count of fixated pictures is shown too. The claims\n",
+    "file, as amended after a reader's answer (questions/hunt-2018.yaml), allows two measures of\n",
+    "accuracy: (A) the choice of the higher true expected value, reading (a) of choice-accuracy-ev\n",
+    "(ties left out); (B) the choice of the higher expected value of the pictures observed, under the\n",
+    "readings of choice-accuracy-observed. Trials are pooled over sessions; the script's mean over\n",
+    "sessions is shown as a variant."
    ]
   },
   {
@@ -796,18 +800,51 @@
[... 16 more lines not kept]
```

**Agent**

Now the summary table, and a check of the README for mentions of these outcomes.

**Agent calls Bash**

```bash
cd entries/hunt-2018; python - <<'E'
import json
p='reproduce_hunt_2018.ipynb'
nb=json.load(open(p)); C=nb['cells']
c=C[-1]; s=''.join(c['source'])
for a,b in [("| figs1cd-fewer-cues-more-accurate | not reproduced |","| figs1cd-fewer-cues-more-accurate | reproduced |"),
            ("| fig7a-ofc-value-difference-neurons | partially reproduced |","| fig7a-ofc-value-difference-neurons | reproduced |")]:
    assert a in s; s=s.replace(a,b)
c['source']=s.splitlines(keepends=True)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
E
cat README.md; grep -n "figs1cd\|fig7a\|1.64\|accuracy" entry.yaml pfc7.py | head -20
```

```
# Hunt, Malalasekera et al. (2018) from CRCNS pfc-7

Tests the findings of [Hunt, Malalasekera et al. (2018)](https://doi.org/10.1038/s41593-018-0239-5)
on CRCNS data set [pfc-7](https://doi.org/10.6080/K0PZ5712): the behaviour of two macaques in an
information sampling task (25 and 32 sessions) and 549 single units from ACC, DLPFC and OFC. All 40
claims of the claims file are tested: 35 are reproduced, 4 partially reproduced and 1 not
reproduced.

| Claim | Outcome |
|---|---|
| Sessions and trial counts | Reproduced |
| Neuron counts after the 1 Hz exclusion | Reproduced |
| Choice accuracy, on expected value and on the pictures seen; early choices | Reproduced |
| Logistic regressions of choice (Supplementary Figure 1a/b) | Partially reproduced |
| More accurate on 2-picture trials (Supplementary Figure 1c/d) | Not reproduced |
| Information sampling (Figure 2a/b) | Reproduced |
| RSA templates at cue 1 (Figure 4d-h, Supplementary Figures 2, 4, 11) | Reproduced |
| t75 latencies (Figure 4) | Reproduced |
| Latency order from simulations (Supplementary Figure 5c) | Partially reproduced |
| OFC value comparison subspaces (Figure 5a-k, Supplementary Figures 6, 7) | Reproduced |
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/hunt-2018; python - <<'E'
p='README.md'; s=open(p).read()
for a,b in [("35 are reproduced, 4 partially reproduced and 1 not\nreproduced.","37 are reproduced and 3 partially reproduced."),
 ("| More accurate on 2-picture trials (Supplementary Figure 1c/d) | Not reproduced |","| More accurate on 2-picture trials (Supplementary Figure 1c/d) | Reproduced |"),
 ("| Single-neuron value difference in OFC at each test (Figure 7a) | Partially reproduced |","| Single-neuron value difference in OFC at each test (Figure 7a) | Reproduced |")]:
    assert a in s; s=s.replace(a,b)
open(p,'w').write(s)
E
date -u
```

```
Sat Nov 14 20:31:12 UTC 2026
```

**Agent**

Now the attempt record. First I'll check whether the schema has a field for answered questions.

**Agent calls Bash**

```bash
cd  ls schemas; grep -rn "question\|answer" schemas/*attempt* | head; grep -n "author-answers" -r docs | head
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
docs/protocol.md:32:`author`, `author-answers` when a reader answered a question on the claims
docs/protocol.md:342:     claims file (reader, step 6), and a later run, `author-answers`,
docs/protocol.md:569:- **Blind.** The author's runs (author, author-answers and each
docs/pilot-notes/semenov-2026-01.md:33:the reader's run and the author-answers run changed nothing. Round 1 agreed with
docs/pilot-notes/semenov-2026-01.md:54:180 s after the author-answers run, 337 s for the whole entry after round 1 and
docs/pilot-notes/ghaderi-2026-01.md:71:Methods' response window, and the author-answers run kept the outcome partial
docs/pilot-notes/ghaderi-2026-01.md:94:21.5 min at first, 334, 880 and 1309 s after the author-answers run, 15, 30 and
docs/pilot-notes/purdon-2013-01.md:23:author asked a reader nothing, so the answer and author-answers runs changed
docs/pilot-notes/purdon-2013-01.md:41:author-answers run, 67 s after round 1 and 70 s at the end. Untracked dotfiles
docs/pilot-notes/mehrotra-2024-01.md:65:no questions of a reader, so the answer and author-answers runs changed
```

**Agent calls Bash**

```bash
cd  sed -n 20,42p docs/protocol.md
```

```
only when it believes the file misreads the paper.
- The **verifier** checks the author's work and must not be the author.

So every claim, the values it must match and how it is judged are fixed from
the paper before anyone analyses the data, and every method the analysis uses
comes from the paper. Where the paper leaves a method open, the choice made is
stated as an assumption, and the outcome is marked as resting on it.

Reader runs are made with the [Paper run](../.github/workflows/papers.yml)
workflow (roles `claims`, `claims-check` and `answer`), the only runs that
write the claims file. The other runs are made with the
[Agent run](../.github/workflows/attempt.yml) workflow, one role at a time:
`author`, `author-answers` when a reader answered a question on the claims
file, `verifier-1`, `author-revise-1`, `verifier-2`, `author-revise-2`, and,
when the last of these proposes changes of outcome, `verifier-3` and `author-revise-3`. Each run's
transcript and final report are kept in
[`transcripts/<paper>/`](../transcripts). Records are filed under the paper's
key, its first author's surname and year (`tingley-2021`; papers/keys.yaml),
and the datasets it is tested on are listed in `papers/datasets/<paper>.yaml`
([paper-first.md](paper-first.md)). A dataset's folder name is its identifier
[... 2 more lines not kept]
```

**Agent**

Now editing the record entries for figs1cd, fig7a and fig7b.

**Agent calls Bash**

```bash
cd  python - <<'E'
p='attempts/hunt-2018-01.yaml'; s=open(p).read()
old_s1=s[s.index("- claim: figs1cd-fewer-cues-more-accurate"):s.index("- claim: fig2a-sample-the-favourite")]
new_s1="""- claim: figs1cd-fewer-cues-more-accurate
  outcome: reproduced
  notebook: reproduce_hunt_2018.ipynb
  output: claim:figs1cd-fewer-cues-more-accurate
  notes: A reader's answer (questions/hunt-2018.yaml) amended the criterion to allow two measures of
    accuracy, (A) the higher true expected value and (B) the higher expected value of the pictures
    observed, under the readings of choice-accuracy-observed, with trials pooled over sessions. The
    first run tested (A) only and gave not_reproduced. Under (B), with the script's count of
    pictures, accuracy on 2-picture trials is the highest in both monkeys under all four readings,
    under reading (a) F 90.24% against 82.67% and 79.81% on 3 and 4 pictures, M 94.62% against
    85.98% and 81.70%. Under (A) it is not (F 74.96% against 76.10% and 79.62%; M 78.83% against
    78.79% and 81.51%). The mean value difference is largest on 2-picture trials in both monkeys
    under both readings (true expected values F 0.266, 0.229, 0.219; M 0.271, 0.240, 0.228). The
    script's mean over sessions, the variant, gives the same order as (B) (F 90.19%, 82.63%,
    82.27%; M 93.65%, 85.20%, 83.69%).
  deviations:
  - The number of pictures is the script's num_pics_viewed250 (InfoGathering_Behaviour.m), and the
    pictures observed for measure (B) are the same ones. With the raw count of fixated pictures, (B)
    holds in both monkeys under readings (a), (c) and the script's, and in F only under (b); the
    value difference is then largest on 2-picture trials in F only.
"""
s=s.replace(old_s1,new_s1)
old7=s[s.index("- claim: fig7a-ofc-value-difference-neurons"):s.index("- claim: fig7c-acc-belief-neurons")]
new7="""- claim: fig7a-ofc-value-difference-neurons
  outcome: reproduced
  notebook: reproduce_hunt_2018.ipynb
  output: claim:fig7a-ofc-value-difference-neurons
  notes: A reader's answer (questions/hunt-2018.yaml) amended the criterion, which had required
    OFC to lead at both p < 0.05 and p < 0.01, to require one reading of the significance level,
    and added the script's threshold |T| > 1.64 as reading (c). The first run gave
    partially_reproduced. The proportions are unchanged. With the Figure 5 trial types (reading a),
    OFC has the largest proportion at all three tests at 250 ms for p < 0.05 (OFC 6.0, 4.4, 6.6%
    against ACC 5.3, 3.2, 4.8% and DLPFC 1.5, 2.2, 2.2%), at 300 ms for p < 0.01 (1.6, 1.6, 3.3%
    against 1.1, 0.5, 1.1% and 1.5, 1.5, 1.5%), and with |T| > 1.64 at both bins. It fails at 250
    ms for p < 0.01, at 300 ms for p < 0.05, and under the attribute-trial reading (b) in every
    combination. The differences are small; at 250 ms and p < 0.05 the smallest of the six pairwise
    chi-square p values is 0.084.
- claim: fig7b-ofc-value-difference-any
  outcome: reproduced
  notebook: reproduce_hunt_2018.ipynb
  output: claim:fig7b-ofc-value-difference-any
  notes: With reading (a), OFC has the largest fraction passing any test at both bins and all
    thresholds (250 ms, p < 0.05 OFC 11.5%, ACC 9.0%, DLPFC 6.0%), so it holds under each reading
    with which fig7a now holds after the reader's answer on the significance level; the outcome is
    unchanged.
"""
s=s.replace(old7,new7)
open(p,'w').write(s)
E
git diff --stat; date -u
```

```
attempts/hunt-2018-01.yaml                  | 47 +++++++++++------
 entries/hunt-2018/README.md                 |  7 ++-
 entries/hunt-2018/reproduce_hunt_2018.ipynb | 81 ++++++++++++++++++++++-------
 3 files changed, 94 insertions(+), 41 deletions(-)
Sat Nov 14 20:31:31 UTC 2026
```

**Agent**

The record is updated. Now lock and run the entry; the earlier run took about 13 minutes.

**Agent calls Bash**

```bash
cd  python tools/entry.py lock entries/hunt-2018 2>&1 | tail -5 && python tools/entry.py all entries/hunt-2018 2>&1 | tail -30; date -u
```

```
wrote hunt-2018/requirements.lock.txt (Python 3.13, with hashes)
/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/nbformat/validator.py:434: MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions. You may want to use `normalize()` on your notebooks before validations (available since nbformat 5.1.4). Previous versions of nbformat are fixing this issue transparently, and will stop doing so in the future.
  _validate(nbdict, ref, version, version_minor, relax_add_props)
Installed kernelspec registry-hunt-2018 in executed/hunt-2018/.venv/share/jupyter/kernels/registry-hunt-2018
0 error(s)
pass  reproduce_hunt_2018.ipynb  (389 s)
Sat Nov 14 20:38:14 UTC 2026
```

**Agent**

The run passed. The new cell has no `id` field, which nbformat warns about. I'll check whether the other cells have ids and look at the executed outputs.

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
nb=json.load(open('entries/hunt-2018/reproduce_hunt_2018.ipynb'))
print(nb['nbformat'],nb['nbformat_minor'],sum('id' in c for c in nb['cells']),len(nb['cells']))
ex=json.load(open('executed/hunt-2018/reproduce_hunt_2018.ipynb'))
for i,c in enumerate(ex['cells']):
    t=(c.get('metadata',{}).get('tags') or [])
    if any(x in ('claim:figs1cd-fewer-cues-more-accurate','claim:fig7a-ofc-value-difference-neurons','claim:fig7b-ofc-value-difference-any') for x in t) or 'total run time' in ''.join(c['source']):
        for o in c.get('outputs',[]): print(''.join(o.get('text','')))
E
```

```
4 5 149 150
script's measure (mean over sessions of accuracy on seen values; mean |EV difference|):
                   acc     vd
subject npv250               
F       2       90.188  0.268
        3       82.631  0.227
        4       82.270  0.219
M       2       93.652  0.272
        3       85.196  0.239
        4       83.694  0.226
                  trials  accuracy  vd_true  vd_cues12
count  subject n                                      
npv    F       2    1230    78.939    0.305      0.241
               3    4119    74.068    0.249      0.175
               4    4514    76.341    0.227      0.155
       M       2     351    72.086    0.223      0.167
               3    5714    79.463    0.270      0.198
               4    8186    78.977    0.232      0.160
npv250 F       2    4638    74.955    0.266      0.198
               3    4790    76.103    0.229      0.153
[... 71 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json, uuid
p='entries/hunt-2018/reproduce_hunt_2018.ipynb'
nb=json.load(open(p)); C=nb['cells']
ids={c.get('id') for c in C}
for c in C:
    if 'id' not in c:
        c['id']='figs1cd-observed'; assert c['id'] not in ids
        # keep key order like the other cells
        c2={k:c[k] for k in ('cell_type','execution_count','id','metadata','outputs','source')}
        c.clear(); c.update(c2)
i=120; s=''.join(C[i]['source']); assert s.startswith('**Result: reproduced.** With the Figure 5')
s=s.replace("""differences are small: at 250 ms and p < 0.05 none of the six pairwise chi-square tests is below
0.05 (smallest p = 0.084).""","""differences are small: at 250 ms and p < 0.05 none of the six pairwise chi-square tests is below
0.05 (smallest p = 0.084), and by monkey OFC leads at all three tests in M (6.2, 6.2, 8.6%) but not
in F, where cue 3 against cue 1 gives OFC 3.0% against ACC 3.2%.""")
C[i]['source']=s.splitlines(keepends=True)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
p='attempts/hunt-2018-01.yaml'; s=open(p).read()
a="""combination. The differences are small; at 250 ms and p < 0.05 the smallest of the six pairwise
    chi-square p values is 0.084.
"""
assert a in s
s=s.replace(a,"""combination. The differences are small; at 250 ms and p < 0.05 the smallest of the six pairwise
    chi-square p values is 0.084, and by monkey OFC leads at all three tests in M (6.2, 6.2, 8.6%)
    but not in F, where cue 3 against cue 1 gives OFC 3.0% against ACC 3.2%.
""")
open(p,'w').write(s)
p='entries/hunt-2018/README.md'; s=open(p).read()
a="It takes about 14 minutes, about three of them streaming"
assert a in s; s=s.replace(a,"It takes 6 to 14 minutes, about three of them streaming"); open(p,'w').write(s)
E
grep -n '"id"' entries/hunt-2018/reproduce_hunt_2018.ipynb | head -3
```

```
5:   "id": "31a86bdf",
53:   "id": "6283f5eb",
84:   "id": "d76e6663",
```

**Agent calls Bash**

```bash
cd  python tools/entry.py lock entries/hunt-2018 2>&1 | tail -2 && python tools/entry.py all entries/hunt-2018 2>&1 | tail -6 && python tools/entry.py handover entries/hunt-2018 2>&1 | tail -5; date -u
```

```
wrote hunt-2018/requirements.lock.txt (Python 3.13, with hashes)
Installed kernelspec registry-hunt-2018 in executed/hunt-2018/.venv/share/jupyter/kernels/registry-hunt-2018
0 error(s)
pass  reproduce_hunt_2018.ipynb  (367 s)
wrote executed/hunt-2018/handover
Sat Nov 14 20:45:00 UTC 2026
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
ex=json.load(open('executed/hunt-2018/reproduce_hunt_2018.ipynb'))
for c in ex['cells']:
    s=''.join(c['source'])
    if 'monkey M, trial types (a)' in s or 'total run time' in s or 'reading (B)' in s[:200]:
        for o in c.get('outputs',[]): print(''.join(o.get('text',''))[:600])
E
git status --short
```

```
total run time 6.0 min, peak memory 4.4 GB

 M attempts/hunt-2018-01.yaml
 M entries/hunt-2018/README.md
 M entries/hunt-2018/reproduce_hunt_2018.ipynb
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
cd  python - <<'E'
import json
ex=json.load(open('executed/hunt-2018/reproduce_hunt_2018.ipynb'))
for c in ex['cells']:
    t=''.join(''.join(o.get('text','')) for o in c.get('outputs',[]))
    if 'monkey F, trial types (a), bin 250' in t or 'count npv250, reading (Ba)' in t:
        print(t[-700:])
E
```

```
41   82.76
       M       2  94.62  84.58  96.59   95.19
               3  85.98  82.01  87.16   87.86
               4  81.70  76.74  82.58   84.62
count npv250, reading (Ba): accuracy 2 > 3 and 2 > 4, F True, M True
count npv250, reading (Bb): accuracy 2 > 3 and 2 > 4, F True, M True
count npv250, reading (Bc): accuracy 2 > 3 and 2 > 4, F True, M True
count npv250, reading (Bscript): accuracy 2 > 3 and 2 > 4, F True, M True
count npv, reading (Ba): accuracy 2 > 3 and 2 > 4, F True, M True
count npv, reading (Bb): accuracy 2 > 3 and 2 > 4, F True, M False
count npv, reading (Bc): accuracy 2 > 3 and 2 > 4, F True, M True
count npv, reading (Bscript): accuracy 2 > 3 and 2 > 4, F True, M True

monkey M, trial types (a), bin 250, p < 0.05: % ACC [5.3 3.2 2.1], DLPFC [0.  2.7 0. ], OFC [6.2 6.2 8.6]
monkey M, trial types (a), bin 300, p < 0.05: % ACC [3.2 6.4 2.1], DLPFC [5.4 5.4 5.4], OFC [7.4 4.9 6.2]
monkey F, trial types (a), bin 250, p < 0.05: % ACC [5.3 3.2 7.4], DLPFC [2.1 2.1 3.1], OFC [5.9 3.  5. ]
monkey F, trial types (a), bin 300, p < 0.05: % ACC [3.2 3.2 6.3], DLPFC [3.1 2.1 3.1], OFC [4.  4.  6.9]
```

**Agent**

In F, OFC trails ACC at two tests, not one (cue 3 against cue 2 is also lower, 5.0% against 7.4%). I'll correct the text in both places and run again.

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
p='entries/hunt-2018/reproduce_hunt_2018.ipynb'
nb=json.load(open(p))
a="""but not
in F, where cue 3 against cue 1 gives OFC 3.0% against ACC 3.2%."""
b="""but not
in F, where ACC is higher at both cue 3 tests (3.2 and 7.4% against OFC 3.0 and 5.0%)."""
n=0
for c in nb['cells']:
    s=''.join(c['source'])
    if a in s: c['source']=s.replace(a,b).splitlines(keepends=True); n+=1
assert n==1
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
p='attempts/hunt-2018-01.yaml'; s=open(p).read()
a="""    but not in F, where cue 3 against cue 1 gives OFC 3.0% against ACC 3.2%.
"""
assert a in s
s=s.replace(a,"""    but not in F, where ACC is higher at both cue 3 tests (3.2 and 7.4% against OFC 3.0 and 5.0%).
""")
open(p,'w').write(s)
E
python tools/entry.py lock entries/hunt-2018 2>&1 | tail -1 && python tools/entry.py all entries/hunt-2018 2>&1 | tail -3 && python tools/entry.py handover entries/hunt-2018 2>&1 | tail -2; date -u
```

```
wrote hunt-2018/requirements.lock.txt (Python 3.13, with hashes)
Installed kernelspec registry-hunt-2018 in executed/hunt-2018/.venv/share/jupyter/kernels/registry-hunt-2018
0 error(s)
pass  reproduce_hunt_2018.ipynb  (383 s)
wrote executed/hunt-2018/handover
Sat Nov 14 20:51:55 UTC 2026
```

**Agent**

The reader amended both claims, and both now come out reproduced. The other 38 outcomes are unchanged. The entry passed its checks (0 errors), the clean run passed in 383 s, and the handover is built in `executed/hunt-2018/handover/`. I did not verify my own work, and nothing is committed or pushed.

**Question 1, `figs1cd-fewer-cues-more-accurate`** (earlier outcome: not reproduced, now: reproduced)
- **What the answer changed:** the criterion now accepts two measures of accuracy and needs only one to hold:
  - (A) choosing the option with the higher true expected value;
  - (B) choosing the option with the higher expected value of the pictures observed, scored as in the claim `choice-accuracy-observed`.

  Trials stay pooled over sessions. The session mean that the paper's script uses is shown as a variant.
- **New analysis:** I added a notebook cell that computes (B), pooled, for 2, 3 and 4 pictures under each scoring rule of `choice-accuracy-observed`.
- **Results** (picture count from the paper's script):
  - Under (B), 2-picture trials are the most accurate in both monkeys under all four scoring rules. With the first rule: monkey F 90.24% against 82.67% and 79.81% on 3 and 4 pictures; monkey M 94.62% against 85.98% and 81.70%.
  - Under (A) they are not: F 74.96% against 76.10% and 79.62%; M 78.83% against 78.79% and 81.51%.
  - The mean value difference is largest on 2-picture trials in both monkeys under both definitions of value difference (F 0.266, 0.229, 0.219; M 0.271, 0.240, 0.228).
  - The session-mean variant gives the same order as (B).
  - Counting every fixated picture instead: (B) holds in both monkeys under three of the four scoring rules and in F only under the fourth. The value difference is then largest on 2-picture trials in F only.

**Question 2, `fig7a-ofc-value-difference-neurons`** (earlier outcome: partially reproduced, now: reproduced)
- **What the answer changed:** OFC no longer has to lead at both p < 0.05 and p < 0.01; one significance level is enough. The script's threshold, |T| > 1.64, was added as a third level. The proportions themselves are unchanged.
- **Results** (Figure 5 trial types), where OFC leads ACC and DLPFC at all three tests:
  - 250 ms, p < 0.05: OFC 6.0, 4.4, 6.6% against ACC 5.3, 3.2, 4.8% and DLPFC 1.5, 2.2, 2.2%.
  - 300 ms, p < 0.01: OFC 1.6, 1.6, 3.3%.
  - |T| > 1.64: both time bins.
- **Where it still fails:** 250 ms with p < 0.01, 300 ms with p < 0.05, and every combination using attribute trials for the cue 3 tests.
- **The effect is weak:**
  - None of the pairwise chi-square tests reaches 0.05 (smallest p = 0.084).
  - By monkey, OFC leads at all three tests in M but not in F. In F, ACC is higher at both cue 3 tests: 3.2% and 7.4% against OFC 3.0% and 5.0%.

  I added the per-monkey result to the notebook and the record, since the run printed it but no text reported it.

**`fig7b-ofc-value-difference-any`** (depends on fig7a; reproduced before and after)
- The outcome is unchanged. OFC has the largest fraction at every time bin and level with the Figure 5 trial types (for example 11.5% against 9.0% and 6.0% at 250 ms, p < 0.05). I added a note saying so.

**Files changed:**
- **Notebook:** the text for both claims, the new cell, and the summary table.
- **Attempt record `attempts/hunt-2018-01.yaml`:** the outcomes and notes, each note saying what the answer changed.
- **`README.md`:** the totals are now 37 reproduced and 3 partially reproduced. The run-time line now reads 6 to 14 minutes.

The finding that asks the authors to confirm the script's choices still applies, so I left it as it was.

## End of run

31 turns, 24 minutes, $1.32 at API prices, result: success.
