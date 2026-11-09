# 000019 · author-answers · run 39702025066

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "" docs/protocol.md | sed -n '1,400p' | head -c 60000; echo; ls entries/000019-bouchard-2013 entries/000019-bouchard-2013/*; cat questions/000019.yaml
```

```
<persisted-output>
Output too large (33.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/909295e0-894d-459c-8b30-e20edde94aeb/tool-results/bh2ho3aum.txt

Preview (first 2KB):
1:# Protocol for an attempt
2:
3:Version: `pilot-10`. Record this version in the attempt's provenance.
4:
5:This is what agents, or people, do to attempt a target and deposit the
6:result. A target is a dataset in a public archive and a paper it names. How
7:each archive's datasets are named, versioned and read is in
8:[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
9:([pilot notes](pilot-notes.md)); the reasons for the rules are there.
10:
11:An attempt has three roles, each a separate run with a separate context:
12:
13:- The **reader** reads the paper and writes the claims file: every finding,
14:  and how each is to be tested, taken from the paper. A second reader checks
15:  it against the paper. Readers never see the dataset's data.
16:- The **author** tests the claims on the dataset. It reads the paper to
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md; ls -R entries/000019-bouchard-2013 | head -50; cat questions/000019.yaml
```

```
1:# Protocol for an attempt
36:## Reader
38:### 1. Get the paper
49:### 2. Read the paper's code
59:### 3. Write the claims file
142:### 4. Data from outside the paper's own recordings
150:### 5. Check
163:### 6. Answer questions
171:## Author
179:### 1. Establish what can be tested
277:### 2. Check the data against its description
292:### 3. Write the entry
341:### 4. Lock, check and run
352:### 5. Record the attempt
399:### 6. Hand over for verification
433:## Repeat attempts
446:## Verifier
450:### Round 1: without the author's conclusions
468:### Round 2: with the author's conclusions
479:### Round 3: proposed changes
[... 123 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 171,445p docs/protocol.md
```

```
## Author

The workflow puts the paper under `paper/`, as for the reader. Read it to
understand the claims, their data and their figures. The claims file still
decides what is tested and how: do not change a claim's statement, expected
values or criterion, and do not apply a method detail the claims file lacks,
even one the paper gives. Ask for it (step 6).

### 1. Establish what can be tested

Do this before any analysis.

1. List the dataset's files and read its metadata from the archive. Open a
   file and list everything it holds, including every column of every table.
2. Work out which of the subjects, sessions, conditions and measured
   variables that the claims file describes are in the dataset. A dataset
   that names a paper may hold only part of its data. Check for recordings
   deposited more than once (identical traces, frame counts or annotations),
   report each pair, and count each recording once. Where the analysis treats
   a unit as the same across sessions, show that it is, or state it as an
[... 254 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls claims/000019 attempts | grep 000019; git show --stat HEAD~1 HEAD | head -40; git diff 6c788edd fe96bbec --stat
```

```
000019-bouchard-2013-01.yaml
claims/000019:
commit 6c788edde1fe7305c6a7692acd949e6af56c4568
Author: github-actions[bot] <github-actions[bot]@users.noreply.github.com>
Date:   Thu Oct 22 00:44:32 2026 +0000

    Agent run on 000019: author (success)
    
    Run: https://github.com/catalystneuro/reproduction-registry/actions/runs/39692741052
    
    Account: unverified

 attempts/000019-bouchard-2013-01.yaml              |  299 ++
 entries/000019-bouchard-2013/README.md             |   41 +
 entries/000019-bouchard-2013/bouchard.py           |  491 ++++
 entries/000019-bouchard-2013/entry.yaml            |   22 +
 .../reproduce_bouchard_2013.ipynb                  | 1717 +++++++++++
 entries/000019-bouchard-2013/requirements.in       |    9 +
 entries/000019-bouchard-2013/requirements.lock.txt |  324 ++
 questions/000019.yaml                              |   76 +
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd  git diff 6c788edd fe96bbec -- claims/; cat transcripts/000019/author-report.md
```

```
diff --git a/claims/000019/10.1038-nature11911.yaml b/claims/000019/10.1038-nature11911.yaml
index fad581f2..0d4309da 100644
--- a/claims/000019/10.1038-nature11911.yaml
+++ b/claims/000019/10.1038-nature11911.yaml
@@ -42,16 +42,24 @@
 #   baseline does. OPEN, the baseline. The Methods do not say which data are baseline.
 #   Readings (a) a silent window before each utterance (the 500 ms before the start of the
 #   plotted epochs, -1000 to -500 ms from the C-V transition, is used for this reading);
-#   (b) the mean and SD of the whole recording of the channel. Both are run.
+#   (b) the mean and SD of the whole recording of the channel; (c) a silent rest period the
+#   dataset marks as baseline (added 2026-10-22 in answer to a question; "baseline data" in
+#   the Methods allows it as much as (a) or (b)). All three are run.
 # - Per-syllable responses. The analyses use cross-syllable variability in the average Hg
 #   (Methods, Acoustic Analysis), so each CV's response at each electrode is the mean over
 #   its renditions, aligned at the C-V transition. Epoch -500 to +750 ms (the range of the
-#   Fig. 5a symbols); the analysis windows below lie within it.
+#   Fig. 5a symbols); the analysis windows below lie within it. OPEN, CVs with fewer than 15
+#   renditions (added 2026-10-22). The Methods describe the paper's data ("Each CV was
+#   produced between 15 and 100 times") and give no rule for leaving a CV out. Readings (a)
+#   every CV the dataset holds, (b) only CVs with 15 or more renditions, the set the paper
[... 95 more lines not kept]
```

**Agent**

I'll keep you updated as I go. First, a look at the existing entry and attempt record.

**Agent calls Bash**

```bash
cd  ls docs/agents; cat attempts/000019-bouchard-2013-01.yaml
```

```
answer.md
author-again.md
author-answers.md
author-revise-3.md
author-revise.md
author.md
claims-check.md
claims.md
recorder.md
verifier-1.md
verifier-2.md
verifier-3.md
schema_version: 2
id: 000019-bouchard-2013-01
dataset:
  archive: dandi
  id: "000019"
  version: 0.220126.2148
  doi: 10.48324/dandi.000019/0.220126.2148
paper: doi:10.1038/nature11911
[... 291 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat docs/agents/author-answers.md; cat entries/000019-bouchard-2013/entry.yaml entries/000019-bouchard-2013/README.md
```

```
You are the author of attempt `{attempt}` on dataset {dataset} (entry `entries/{entry}`), coming back to it after a reader answered your questions. Follow docs/protocol.md, "Author". The paper's full text is under `paper/`: read it to understand the claims. The claims file, which a reader wrote from the paper and a second reader checked, decides what is tested and how: do not change a claim's statement, expected values or criterion, and do not apply a method detail it lacks, even one the paper gives; ask, as step 1.6 of the Author section says.

The answers are in `questions/{folder}.yaml`, and the claims they bear on have been updated in the claims file. For each answered question, re-run the affected claims as their criteria now say, update the notebook, the conclusions and the attempt record, and say in each claim's notes what the answer changed. Then lock, check and run the entry (`python tools/entry.py lock|all entries/{entry}`) and run `python tools/entry.py handover entries/{entry}`. Do not verify your own work. Do not commit or push.

Write prose plainly: no em dashes, never the word "rather", no bold except the "**Result: ...**" openers. YAML plain scalars must not contain ": ".

Your final message is a report: each question, what its answer changed, and the outcome per affected claim, with the earlier outcome next to it.

Run every command in the foreground and wait for it to finish, however long it takes: the run ends when you stop, and anything still running is lost.
schema_version: 1
name: 000019-bouchard-2013
type: reproduction
title: Speech articulation in human sensorimotor cortex (Bouchard et al. 2013)
description: Tests the findings of Bouchard, Mesgarani, Johnson and Chang (2013) on dandiset 000019,
  which holds raw ECoG and syllable annotations of subjects reading consonant-vowel syllables. High
  gamma is computed from the raw voltage. It tests the active electrodes, the articulator timing,
  the mixed tuning of electrodes and the cortical stat
[... 55 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat claims/000019/10.1038-nature11911.yaml
```

```
<persisted-output>
Output too large (48.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/909295e0-894d-459c-8b30-e20edde94aeb/tool-results/bpetnf3kb.txt

Preview (first 2KB):
# Claims for Bouchard, Mesgarani, Johnson & Chang (2013), "Functional organization of human
# sensorimotor cortex for speech articulation", Nature 495, 327-332, on dandiset 000019
# ("Human ECoG speaking consonant-vowel syllables").
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read. The NIH author manuscript as served by PubMed Central (PMC3606666, NIHMS436351),
# not the version of record: main text, figure legends and Methods, with the supplement
# (NIHMS436351-supplement-1.pdf, Supplementary Figures 1 to 13 with their legends,
# Supplementary Table 1 and Supplementary Methods), as extracted to text. No PDF of the main
# text was supplied, so the main figures were read from their legends and from the Results
# sentences that cite them. Supplement pages 2 and 8 were opened in the supplement PDF, to
# see Supplementary Figure 1d and to confirm a printed p-value on page 8.
#
# Code. The paper links no code, and none is named in the Methods or the supplement. Every
# method below is from the Methods, the legends or the Supplementary Methods.
[... 12 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/909295e0-894d-459c-8b30-e20edde94aeb/tool-results/bpetnf3kb.txt"
}
```

```
1	# Claims for Bouchard, Mesgarani, Johnson & Chang (2013), "Functional organization of human
2	# sensorimotor cortex for speech articulation", Nature 495, 327-332, on dandiset 000019
3	# ("Human ECoG speaking consonant-vowel syllables").
4	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21,
5	# protocol pilot-10 as stated in docs/protocol.md.
6	#
7	# Text read. The NIH author manuscript as served by PubMed Central (PMC3606666, NIHMS436351),
8	# not the version of record: main text, figure legends and Methods, with the supplement
9	# (NIHMS436351-supplement-1.pdf, Supplementary Figures 1 to 13 with their legends,
10	# Supplementary Table 1 and Supplementary Methods), as extracted to text. No PDF of the main
11	# text was supplied, so the main figures were read from their legends and from the Results
12	# sentences that cite them. Supplement pages 2 and 8 were opened in the supplement PDF, to
13	# see Supplementary Figure 1d and to confirm a printed p-value on page 8.
14	#
15	# Code. The paper links no code, and none is named in the Methods or the supplement. Every
16	# method below is from the Methods, the legends or the Supplementary Methods.
17	#
18	# Data the paper describes. Three native English speakers (Supplementary Table 1 names them
19	# EC2, EC33 and EC31) with a high-density subdural ECoG array over peri-Sylvian cortex, left
20	# hemisphere in two (EC2, EC31) and right in one (EC33), implanted for epilepsy monitoring.
[... 732 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "entries/000019-bouchard-2013/bouchard.py"
}
```

```
1	"""Loading, high gamma and shared measures for dandiset 000019 (Bouchard et al. 2013).
2	
3	Bouchard KE, Mesgarani N, Johnson K, Chang EF (2013). Functional organization of human
4	sensorimotor cortex for speech articulation. Nature 495, 327-332. doi:10.1038/nature11911.
5	
6	The dandiset holds, per recording block, raw ECoG from a 256-channel grid at 3051.76 Hz, a trial
7	table (syllable spoken, start, consonant-to-vowel transition and stop times), a `bad` flag per
8	electrode, an anatomical label per electrode, and a rest period. It has no audio and no high gamma,
9	so high gamma is computed here from the raw voltage.
10	
11	Files are streamed from the archive at the pinned version: each file's bytes are fetched into
12	memory with parallel HTTP range requests and opened with h5py from memory. Nothing is written to
13	disk. The files are 0.6 to 2.8 GB and every sample is needed (common average reference over all
14	good channels, and trials cover the whole block), so reading the whole file in large requests is
15	much faster than h5py's chunk-by-chunk reads over the network.
16	
17	Where the parameters come from:
18	
19	- Bad channels are the dataset's `bad` flags; the claims file's header says to use them. The
20	  common average reference is over the remaining channels (Methods, via the claims header).
[... 472 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000019-bouchard-2013; python -c "
import json;nb=json.load(open('reproduce_bouchard_2013.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source']); print('=====',i,c['cell_type'],c.get('metadata',{}).get('tags'),len(s)); print(s[:300])
"
```

```
===== 0 markdown None 3005
# Reproducing Bouchard et al. (2013) from dandiset 000019

Paper. Bouchard KE, Mesgarani N, Johnson K, Chang EF (2013). Functional organization of
human sensorimotor cortex for speech articulation. *Nature* 495, 327-332.
[doi:10.1038/nature11911](https://doi.org/10.1038/nature11911). The claims file
===== 1 code None 539
import itertools
import time
import warnings

import h5py
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import remfile
from scipy import stats
from scipy.cluster.hierarchy import fcluster, linkage
from scipy.spatial.distance import pdist, squareform
from sklearn.metrics impo
[... 420 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000019-bouchard-2013; ls ../../executed/ 2>/dev/null | head; python -c "
import json;nb=json.load(open('reproduce_bouchard_2013.ipynb'))
for i in [0,1,3,15,16,21,22,27,28,35,36]:
    c=nb['cells'][i]; print('=====',i); print(''.join(c['source']))
"
```

```
===== 0
# Reproducing Bouchard et al. (2013) from dandiset 000019

Paper. Bouchard KE, Mesgarani N, Johnson K, Chang EF (2013). Functional organization of
human sensorimotor cortex for speech articulation. *Nature* 495, 327-332.
[doi:10.1038/nature11911](https://doi.org/10.1038/nature11911). The claims file
(`claims/000019/10.1038-nature11911.yaml`) was written from the NIH author manuscript in PubMed
Central (PMC3606666) with its supplement, and checked by a second reader.

Dandiset. [DANDI:000019](https://dandiarchive.org/dandiset/000019/0.220126.2148),
"Human ECoG speaking consonant-vowel syllables", version 0.220126.2148. The paper cites no
version of the dandiset (it predates it). This is the only published version; the draft has the
same 31 assets and the same size, so the published version is pinned.

What the dandiset holds. Raw ECoG (256 channels, 3051.76 Hz) of 31 recording blocks from four
subjects (EC2, EC9, GP31, GP33), with a trial table per block (syllable, start, C-V transition
and stop times), a `bad` flag and an anatomical label per electrode, 3-D electrode coordinates for
two subjects, and a rest period per block. The microphone signal was removed (dandiset
description), and no high gamma is stored, so high gamma is computed here from the raw voltage.
The paper's subjects are EC2, EC33 and EC31; EC2, GP33 and GP31 are taken to be them (see the data
[... 291 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000019-bouchard-2013; python -c "
import json;nb=json.load(open('reproduce_bouchard_2013.ipynb'))
for i in [29,30,32,38,39,41,42,44,45,47,48,50,51]:
    c=nb['cells'][i]; print('=====',i); print(''.join(c['source']))
"
```

```
===== 29
## Spatial claims (blocked)

fig2a-lips-dorsal, fig2b-somatotopic-sequence, suppfig3b-spatial-clustering,
suppfig3d-cross-subject, suppfig3f-dv-sequence, suppfig5-intermediate-organization and
suppfig7-no-latency-difference all need each electrode's anterior-posterior distance from the
central sulcus and dorsal-ventral distance from the Sylvian fissure (Methods). The dandiset gives
neither. EC2 and GP31 have x, y, z coordinates with no unit, frame or description; GP33, one of
the three subjects, has none. The labels say precentral or postcentral, not how far from either
sulcus, and no electrode is labelled as on the guenon. These claims are blocked as
metadata_insufficient.

The GLM electrode selection and weights of fig2a-lips-dorsal do not need positions and are
computed above. For information only (not an outcome, and not a reading of the claim), the median
z coordinate of the top 10% of each articulator's weights in the two subjects that have
coordinates, under the first reading:
===== 30
key0 = W_READINGS[0]
print("reading:", key0)
for s in ("EC2", "GP31"):
[... 228 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000019-bouchard-2013; python -c "
import json;nb=json.load(open('reproduce_bouchard_2013.ipynb'))
for i in [53,54,56,57,59,60,61,62,63,64]:
    c=nb['cells'][i]; print('=====',i); print(''.join(c['source']))
"
```

```
===== 53
rng5 = np.random.default_rng(5)
N_BOOT = 1000


def cluster_labels(s, cs, K, which, kind):
    """Labels per CV (per time and CV for k-means); -1 for CVs without a label."""
    cvs = CVS[s, cs]
    if kind == "kmeans":
        return np.array([B.kmeans(K[:, :, t], 3, seed=1000 + t, n_init=10) for t in range(K.shape[2])])
    if which == "vowel":
        return np.array(["aiu".index(v) for c, v in cvs])
    lr = kind[-1]
    names = {"labial": 0, "coronal": 1, "dorsal": 2}
    out = []
    for c, v in cvs:
        m = B.MAJOR[lr].get(c)
        out.append(3 if kind.startswith("four") and c in B.SIBILANTS else (names[m] if m else -1))
    return np.array(out)

[... 261 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000019-bouchard-2013; python -c "
import json;nb=json.load(open('reproduce_bouchard_2013.ipynb'))
for i in [2,10,11,12,13,14]:
    c=nb['cells'][i]; print('=====',i); print(''.join(c['source']))
"; free -g; nproc
```

```
===== 2
# Metadata of every file (EC9 included), and a fingerprint of its first samples, read by streaming.
ASSETS = B.assets()
meta_rows = []
for a in ASSETS:
    with h5py.File(remfile.File(a["url"]), "r") as h5:
        m = B.read_metadata(h5)
        m["fingerprint"] = h5["acquisition/ElectricalSeries/data"][:2000, :4].copy()
    m["path"], m["size"] = a["path"], a["size"]
    meta_rows.append(m)
print(f"read metadata of {len(meta_rows)} files of dandiset {B.DANDISET_ID} version {B.DANDISET_VERSION} "
      f"in {time.time() - started:.0f} s")
===== 10
The archive's summary counts four subjects. EC2 matches the paper's EC2 by name. GP31 and GP33
are not names the paper uses; the paper's other two subjects are EC31 (left hemisphere) and
EC33 (right). GP31's coordinates have negative x in every electrode, which fits a left
hemisphere if x is the usual left-right axis; GP33 has no coordinates, so its hemisphere cannot be
checked. That GP31 is EC31 and GP33 is EC33 is an assumption the data are consistent with, not
shown by them. EC9 has 24 consonant labels (including /ch/, /dh/, /j/, /sk/), labels on only 79 of
256 electrodes and no coordinates; it is not one of the paper's subjects and is left out.
[... 85 more lines not kept]
```

**Agent**

First I'll cache the loaded data (about 12 minutes of streaming) so I can develop the re-run against it, then run the whole entry from scratch at the end.

**Agent calls Bash**

```bash
cd entries/000019-bouchard-2013; cat > $TMPDIR/cache.py <<'EOF'
import json, pickle, os
nb = json.load(open("reproduce_bouchard_2013.ipynb"))
src = "\n".join("".join(nb["cells"][i]["source"]) for i in (1, 2, 3))
g = {}
exec(src, g)
blocks = {s: [{k: v for k, v in b.items() if k != "sums"} for b in bl] for s, bl in g["blocks"].items()}
pickle.dump({"ASSETS": g["ASSETS"], "meta_rows": g["meta_rows"], "S": g["S"], "blocks": blocks},
            open(os.path.join(os.environ["TMPDIR"], "cache.pkl"), "wb"))
print("saved")
EOF
time python $TMPDIR/cache.py 2>&1 | tail -5; ls -la $TMPDIR/cache.pkl
```

```
Exit code 2
  File "/tmp/claude-1001/cache.py", line 5, in <module>
    exec(src, g)
    ~~~~^^^^^^^^
  File "<string>", line 5, in <module>
ModuleNotFoundError: No module named 'h5py'

real	0m0.030s
user	0m0.021s
sys	0m0.011s
ls: cannot access '/tmp/claude-1001/cache.pkl': No such file or directory
```

**Agent calls Bash**

```bash
cd  sed -n 1,80p tools/entry.py | head -100; ls ~/.cache 2>/dev/null; ls -d .venv* */.venv 2>/dev/null; ls /tmp | head
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
- each notebook, or a helper it imports, names the dataset the entry uses (its identifier and version);
- each notebook has a cell tagged `sanity` that prints what was loaded;
[... 70 more lines not kept]
```

**Agent**

Building a dev venv from the lock file.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q -p 3.13 devenv && uv pip install -q -p devenv/bin/python -r entries/000019-bouchard-2013/requirements.lock.txt 2>&1 | tail -3; devenv/bin/python -c "import h5py, sklearn, remfile; print('ok')"
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/000019-bouchard-2013; time $TMPDIR/devenv/bin/python $TMPDIR/cache.py 2>&1 | tail -5; ls -la $TMPDIR/cache.pkl
```

```
Exit code 2
  File "/tmp/claude-1001/cache.py", line 5, in <module>
    exec(src, g)
    ~~~~^^^^^^^^
  File "<string>", line 15, in <module>
ModuleNotFoundError: No module named 'bouchard'

real	0m2.632s
user	0m2.776s
sys	0m0.185s
ls: cannot access '/tmp/claude-1001/cache.pkl': No such file or directory
```

**Agent calls Bash**

```bash
cd entries/000019-bouchard-2013; export PYTHONPATH=$PWD; time $TMPDIR/devenv/bin/python $TMPDIR/cache.py 2>&1 | tail -5; ls -la $TMPDIR/cache.pkl
```

```
read metadata of 31 files of dandiset 000019 version 0.220126.2148 in 54 s
processed 24 blocks in 861 s
saved

real	14m24.292s
user	26m24.826s
sys	3m52.771s
-rw-r--r-- 1 runner runner 134000783 Oct 22 01:10 /tmp/claude-1001/cache.pkl
```

**Agent calls Bash**

```bash
cd entries/000019-bouchard-2013; python - <<'EOF'
p = "bouchard.py"
s = open(p).read()
rep = [
("""- z-scoring per channel against baseline data (Methods). The claims file leaves the baseline open
  and names two readings, both computed: `pre`, the 500 ms windows from -1000 to -500 ms before each
  C-V transition, pooled over the block's trials; `whole`, the whole block. The dataset's rest
  period (`rest`) is computed as a variant only. Statistics are per block and channel.""",
"""- z-scoring per channel against baseline data (Methods). The claims file leaves the baseline open
  and names three readings, all computed: (a) `pre`, the 500 ms windows from -1000 to -500 ms before
  each C-V transition, pooled over the block's trials; (b) `whole`, the whole block; (c) `rest`, the
  rest period the dataset marks as baseline (reading (c) was added to the claims file on 2026-10-22
  in answer to a question). Statistics are per block and channel."""),
("""def state_space(Hv: np.ndarray, mode: str, window=(EPOCH_MS[0], EPOCH_MS[-1]), n_pc: int = 9):
    \"\"\"PCA of the (electrode x concatenated CV-time) matrix (Methods, PCA and Cortical-State
    Space). Returns M (electrode, n_pc), the fraction of variance of every PC, and the states
    K (CV, n_pc, time) of every CV at every epoch time.\"\"\"""",
"""def project(M: np.ndarray, X: np.ndarray) -> np.ndarray:
    \"\"\"States K (CV, n_pc, time) = M' X (Methods Eq. 5), X (CV, electrode, time).\"\"\"
    return np.einsum("ep,cet->cpt", M, X)


def state_space(Hv: np.ndarray, mode: str, window=(EPOCH_MS[0], EPOCH_MS[-1]), n_pc: int = 9):
    \"\"\"PCA of the (electrode x concatenated CV-time) matrix (Methods, PCA and Cortical-State
    Space). Returns M (electrode, n_pc), the fraction of variance of every PC, and the states
    K (CV, n_pc, time) of every CV at every epoch time, projected from the z-scored matrix given
    to the PCA (the claims header's projection reading (i); reading (ii), Hv itself as Eq. 5
    writes it, is `project(M, Hv)`).\"\"\""""),
("""    K = np.einsum("ep,cet->cpt", M, Z)
    return M, frac, K""", """    return M, frac, project(M, Z)"""),
]
for a, b in rep:
    assert s.count(a) == 1, a[:60]
    s = s.replace(a, b)
open(p, "w").write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd entries/000019-bouchard-2013; cat > $TMPDIR/nbedit.py <<'EOF'
import json, sys
P = "reproduce_bouchard_2013.ipynb"
nb = json.load(open(P))

def src(i):
    return "".join(nb["cells"][i]["source"])

def setsrc(i, s):
    lines = s.split("\n")
    nb["cells"][i]["source"] = [l + "\n" for l in lines[:-1]] + ([lines[-1]] if lines[-1] else [])

def rep(i, a, b, count=1):
    s = src(i)
    n = s.count(a)
    if n != count:
        sys.exit(f"cell {i}: found {n} of {a[:70]!r}")
    setsrc(i, s.replace(a, b))

def save():
    json.dump(nb, open(P, "w"), indent=1, ensure_ascii=False)
    open(P, "a").write("\n")
EOF
head -c 300 reproduce_bouchard_2013.ipynb; tail -c 50 reproduce_bouchard_2013.ipynb | od -c | tail -3
```

```
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "7685cd80",
   "metadata": {},
   "source": [
    "# Reproducing Bouchard et al. (2013) from dandiset 000019\n",
    "\n",
    "Paper. Bouchard KE, Mesgarani N, Johnson K, Chang EF (2013). Functional organization of\n",
    "human sensorimotor c0000040   o   r   m   a   t   _   m   i   n   o   r   "   :       5  \n
0000060   }  \n
0000062
```

**Agent**

Now the code-cell edits.

**Agent calls Bash**

```bash
cd entries/000019-bouchard-2013; cat > $TMPDIR/edit1.py <<'EOF'
exec(open(__import__("os").environ["TMPDIR"] + "/nbedit.py").read())
# shared computations
rep(16, 'BASES = ("pre", "whole")\nZMODES = ("row", "time")',
    'BASES = B.BASELINES      # baseline readings (a) pre, (b) whole, (c) rest (claims header)\n'
    'ZMODES = ("row", "time")  # z-scoring before the PCA (claims header)\n'
    'PROJ = ("i", "ii")        # input projected: (i) the PCA input, (ii) Hg as Eq. 5 writes it')
rep(16, 'CVSETS = ("all", "15+")    # every CV, or only CVs with at least 15 renditions (a question to the reader)',
    'CVSETS = ("all", "15+")    # (a) every CV, (b) only CVs with at least 15 renditions (claims header)')
rep(16, 'SS_READINGS = list(itertools.product(BASES, ZMODES, CVSETS))\nEP = (-500, 750)',
    'EP = (-500, 750)\n'
    'SS_READINGS = list(itertools.product(BASES, ZMODES, PROJ, CVSETS))\n'
    'KS = {(s, base, z, pj, cs): STATE[s, base, z, cs, EP][2] if pj == "i" else B.project(STATE[s, base, z, cs, EP][0], HV[s, base, cs])\n'
    '      for s in B.SUBJECTS for base, z, pj, cs in SS_READINGS}')
# active electrodes
rep(21, 'print("\\nMean over subjects (criterion 27 to 33; rest is a variant, not a reading):")',
    'print("\\nMean over subjects (criterion 27 to 33):")')
rep(21, '''          f"whole {np.mean([(np.nanmax(HV[s, 'whole', 'all'], axis=(0, 2)) > thr).sum() for s in B.SUBJECTS]):.1f}")''',
    '''          f"whole {np.mean([(np.nanmax(HV[s, 'whole', 'all'], axis=(0, 2)) > thr).sum() for s in B.SUBJECTS]):.1f}, "
          f"rest {np.mean([(np.nanmax(HV[s, 'rest', 'all'], axis=(0, 2)) > thr).sum() for s in B.SUBJECTS]):.1f}")''')
rep(21, 'res = am.loc[list(BASES)]\nprint("Outcome over readings:", overall(',
    'res = am.loc[list(BASES)]\nper_cs = {cs: ')
rep(21, '''                                         for cs in CVSETS]))''',
    '''          for cs in CVSETS}
print("Outcome per CV set:", per_cs)
print("Outcome over readings:", overall(list(per_cs.values())))''')
rep(21, '''print("Outcome over readings:", overall(["reproduced" if all(res.xs(cs, level=1)["within 27-33 (a or b)"]) else
                                         ("partially" if any(res.xs(cs, level=1)["within 27-33 (a or b)"]) else "not reproduced")''',
    'XX', 0)
s = src(21)
s = s.replace('''per_cs = {cs: ["reproduced" if all(res.xs(cs, level=1)["within 27-33 (a or b)"]) else
                                         ("partially" if any(res.xs(cs, level=1)["within 27-33 (a or b)"]) else "not reproduced")''',
'''per_cs = {cs: "reproduced" if all(res.xs(cs, level=1)["within 27-33 (a or b)"]) else
          ("partially" if any(res.xs(cs, level=1)["within 27-33 (a or b)"]) else "not reproduced")''')
setsrc(21, s)
print(src(21))
save()
EOF
$TMPDIR/devenv/bin/python $TMPDIR/edit1.py
```

```
def overall(outcomes):
    """The outcome all method readings give, or methods_underspecified when they differ."""
    u = sorted(set(outcomes))
    return u[0] if len(u) == 1 else "differ by reading: " + ", ".join(f"{o} {list(outcomes).count(o)}" for o in u)


act = []
for base in B.BASELINES:
    for cs in CVSETS:
        for s in B.SUBJECTS:
            H = HV[s, base, cs]
            act.append({"baseline": base, "CVs": cs, "subject": s, "vSMC": H.shape[1],
                        "(a) z > 2": int((np.nanmax(H, axis=(0, 2)) > 2).sum()),
                        "(b) |z| > 2": int((np.nanmax(np.abs(H), axis=(0, 2)) > 2).sum())})
act = pd.DataFrame(act)
print(act.to_string(index=False))
am = act.groupby(["baseline", "CVs"])[["(a) z > 2", "(b) |z| > 2"]].mean().round(2)
am["within 27-33 (a or b)"] = am.apply(lambda r: 27 <= r["(a) z > 2"] <= 33 or 27 <= r["(b) |z| > 2"] <= 33, axis=1)
print("\nMean over subjects (criterion 27 to 33):")
print(am.to_string())
[... 10 more lines not kept]
```

**Agent**

Now fig3d, PCA and the state-space cells.

**Agent calls Bash**

```bash
cd entries/000019-bouchard-2013; cat > $TMPDIR/edit2.py <<'EOF'
exec(open(__import__("os").environ["TMPDIR"] + "/nbedit.py").read())
# fig3d: substitute onset, with t = 0 beside it
rep(35, 'print(f"Acoustic onset from the annotations:', 'print(f"Acoustic onset, substitute from the hand-marked syllable starts:')
rep(35, '''                n_ok = c1 + c2 + c3
                outcome = ("reproduced" if p < 1e-10 and n_ok == 3 else
                           "partially" if p < 1e-10 and n_ok == 2 else "not reproduced")''',
'''                c1_0 = mo["Lips"] < 0 and mo["Tongue"] < 0
                n_ok, n_ok0 = c1 + c2 + c3, c1_0 + c2 + c3
                outcome = ("reproduced" if p < 1e-10 and n_ok == 3 else
                           "partially" if p < 1e-10 and n_ok == 2 else "not reproduced")
                outcome0 = ("reproduced" if p < 1e-10 and n_ok0 == 3 else
                            "partially" if p < 1e-10 and n_ok0 == 2 else "not reproduced")''')
rep(35, '''                           "outcome": outcome})''', '''                           "outcome": outcome, "lips,tongue < 0": c1_0, "outcome vs t = 0": outcome0})''')
rep(35, '''print("\\nOutcome over readings:", overall(f3.outcome))''',
'''print("\\nOutcome over readings (substitute acoustic onset):", overall(f3.outcome))
print("Beside it, against t = 0:", overall(f3["outcome vs t = 0"]), "| readings with lips and tongue onsets before 0 ms:",
      int(f3["lips,tongue < 0"].sum()), "of", len(f3), "| before the substitute onset:", int(f3["lips,tongue < acoustic"].sum()))''')
rep(35, '''ax.axvline(ACOUSTIC_ONSET, color="grey", ls="--"); ax.axvline(0, color="k", lw=0.5)''',
'''ax.axvline(ACOUSTIC_ONSET, color="grey", ls="--", label="substitute acoustic onset"); ax.axvline(0, color="k", lw=0.5, label="C-V transition")
ax.legend(fontsize=7)''')
# pca: rest is now a reading
rep(38, '''print("Rest-baseline variant (row, all CVs, epoch):", {s: round(float(B.state_space(HV[s, "rest", "all"], "row")[1][:9].sum()), 3) for s in B.SUBJECTS})\n''', '')
rep(38, 'pc = []\nfor base in BASES:', '# The variance explained does not depend on the input projected (readings i and ii).\npc = []\nfor base in BASES:')
# state-space claims
for i in (41, 44, 47, 59):
    rep(i, "for base, z, cs in SS_READINGS:", "for base, z, pj, cs in SS_READINGS:")
    rep(i, "STATE[s, base, z, cs, EP][2]", "KS[s, base, z, pj, cs]")
    rep(i, '"baseline": base, "z-scoring": z, "CVs": cs', '"baseline": base, "z-scoring": z, "projection": pj, "CVs": cs')
rep(41, 'means = sil.groupby(["baseline", "z-scoring", "CVs"])', 'means = sil.groupby(["baseline", "z-scoring", "projection", "CVs"])')
rep(47, 'for (base, z, cs), g in hc.groupby(["baseline", "z-scoring", "CVs"]):', 'for (base, z, pj, cs), g in hc.groupby(["baseline", "z-scoring", "projection", "CVs"]):')
rep(47, 'oc.append({"baseline": base, "z-scoring": z, "CVs": cs,', 'oc.append({"baseline": base, "z-scoring": z, "projection": pj, "CVs": cs,')
# fig4ef
rep(50, 'def feature_r(base, z, cs, metric="euclidean"):', 'def feature_r(base, z, pj, cs, metric="euclidean"):')
rep(50, 'K = STATE[s, base, z, cs, EP][2]', 'K = KS[s, base, z, pj, cs]')
rep(50, 'for (base, z, cs), R in RT.items():', 'for (base, z, pj, cs), R in RT.items():')
rep(50, 'feature_r(base, z, cs, "hamming")', 'feature_r(base, z, pj, cs, "hamming")')
rep(50, 'row = {"baseline": base, "z-scoring": z, "CVs": cs,', 'row = {"baseline": base, "z-scoring": z, "projection": pj, "CVs": cs,')
# fig5c
rep(53, 'def separability_curves(base, z, cs):', 'def separability_curves(base, z, pj, cs):')
rep(53, 'K = STATE[s, base, z, cs, EP][2]', 'K = KS[s, base, z, pj, cs]')
rep(53, 'for (base, z, cs), d in SEP.items():', 'for (base, z, pj, cs), d in SEP.items():')
rep(53, 'sp.append({"baseline": base, "z-scoring": z, "CVs": cs,', 'sp.append({"baseline": base, "z-scoring": z, "projection": pj, "CVs": cs,')
rep(53, 'for ax, key in zip(axes, [("pre", "row", "all"), ("pre", "time", "all")]):', 'for ax, key in zip(axes, [("pre", "row", "i", "all"), ("pre", "time", "i", "all")]):')
# fig5d
rep(56, 'for (base, z, cs), d in SEP.items():\n    R = RT[base, z, cs]', 'for (base, z, pj, cs), d in SEP.items():\n    R = RT[base, z, pj, cs]')
rep(56, 'c5.append({"baseline": base, "z-scoring": z, "CVs": cs,', 'c5.append({"baseline": base, "z-scoring": z, "projection": pj, "CVs": cs,')
save()
EOF
$TMPDIR/devenv/bin/python $TMPDIR/edit2.py && grep -n "STATE\[" reproduce_bouchard_2013.ipynb | head -30
```

```
Exit code 1
cell 47: found 2 of '"baseline": base, "z-scoring": z, "CVs": cs'
```

**Agent calls Bash**

```bash
cd entries/000019-bouchard-2013; python - <<'EOF'
import os
p = os.environ["TMPDIR"] + "/edit2.py"
s = open(p).read()
s = s.replace('''    rep(i, '"baseline": base, "z-scoring": z, "CVs": cs', '"baseline": base, "z-scoring": z, "projection": pj, "CVs": cs')''',
'''    rep(i, '"baseline": base, "z-scoring": z, "CVs": cs', '"baseline": base, "z-scoring": z, "projection": pj, "CVs": cs', 2 if i == 47 else 1)''')
s = s.replace('''rep(47, 'oc.append({"baseline": base, "z-scoring": z, "CVs": cs,', 'oc.append({"baseline": base, "z-scoring": z, "projection": pj, "CVs": cs,')\n''', '')
open(p, "w").write(s)
EOF
$TMPDIR/devenv/bin/python $TMPDIR/edit2.py && grep -n "STATE\[\|KS\[" reproduce_bouchard_2013.ipynb | head -30
```

```
489:    "KS = {(s, base, z, pj, cs): STATE[s, base, z, cs, EP][2] if pj == \"i\" else B.project(STATE[s, base, z, cs, EP][0], HV[s, base, cs])\n",
999:    "                fr = {s: STATE[s, base, z, cs, w][1] for s in B.SUBJECTS}\n",
1010:    "        ax.plot(np.arange(1, 21), 100 * STATE[s, \"pre\", z, \"all\", EP][1][:20], \"o-\", ms=3, label=s)\n",
1016:    "        print(z, s, np.round(100 * STATE[s, \"pre\", z, \"all\", EP][1][:12], 1))"
1059:    "        K = KS[s, base, z, pj, cs][:, :, tc]\n",
1116:    "        K = KS[s, base, z, pj, cs]\n",
1185:    "        K = KS[s, base, z, pj, cs]\n",
1260:    "        K = KS[s, base, z, pj, cs]\n",
1363:    "                K = KS[s, base, z, pj, cs]\n",
1532:    "            K = KS[s, base, z, pj, cs]\n",
1607:    "                M = STATE[s, base, z, cs, EP][0]\n",
1633:    "V = np.concatenate([np.log10(np.abs(STATE[s, base, z, cs, EP][0][:, :3, None] * WEIGHTS[base, cs, reading, pmode][s][\"W\"][:, None, :])) for s in B.SUBJECTS])\n",
```

**Agent**

Now a test run of all analysis cells against the cached data.

**Agent calls Bash**

```bash
cd entries/000019-bouchard-2013; cat > $TMPDIR/runtest.py <<'EOF'
import json, os, pickle, sys, time, io, contextlib
import matplotlib; matplotlib.use("Agg")
nb = json.load(open("reproduce_bouchard_2013.ipynb"))
only = set(map(int, sys.argv[1].split(","))) if len(sys.argv) > 1 else None
g = {}
for i, c in enumerate(nb["cells"]):
    if c["cell_type"] != "code":
        continue
    s = "".join(c["source"])
    if i == 2:
        s = "import pickle, os\n_c = pickle.load(open(os.environ['TMPDIR'] + '/cache.pkl', 'rb'))\nASSETS, meta_rows, S, blocks = _c['ASSETS'], _c['meta_rows'], _c['S'], _c['blocks']"
    if i == 3:
        continue
    t = time.time()
    buf = io.StringIO()
    quiet = only is not None and i not in only
    with contextlib.redirect_stdout(buf):
        exec(s, g)
    if not quiet:
        print(f"===== cell {i} ({time.time() - t:.0f} s)")
        print(buf.getvalue())
    else:
        print(f"== cell {i} ({time.time() - t:.0f} s)", file=sys.stderr)
EOF
export PYTHONPATH=$PWD; time $TMPDIR/devenv/bin/python $TMPDIR/runtest.py > $TMPDIR/out1.txt 2>&1; tail -3 $TMPDIR/out1.txt; grep -n "===== cell\|Outcome\|Beside" $TMPDIR/out1.txt
```

```
real	16m8.471s
user	20m44.125s
sys	0m3.562s
===== cell 65 (0 s)
notebook ran in 16.1 min

1:===== cell 1 (1 s)
3:===== cell 2 (0 s)
5:===== cell 5 (1 s)
54:===== cell 6 (0 s)
58:===== cell 8 (0 s)
70:===== cell 9 (0 s)
88:===== cell 11 (0 s)
129:===== cell 13 (1 s)
137:===== cell 16 (10 s)
140:===== cell 18 (0 s)
150:===== cell 21 (0 s)
184:Outcome per CV set: {'all': 'not reproduced', '15+': 'partially'}
185:Outcome over readings: differ by reading: not reproduced 1, partially 1
187:===== cell 24 (0 s)
[... 28 more lines not kept]
```

**Agent**

Everything runs, but fig5c's cell took 15 minutes with three times the readings, which would push the notebook over the 30-minute CI limit. Profiling it.

**Agent calls Bash**

```bash
cd entries/000019-bouchard-2013; export PYTHONPATH=$PWD; $TMPDIR/devenv/bin/python - <<'EOF'
import numpy as np, time
import bouchard as B
from scipy.spatial.distance import pdist, squareform
rng = np.random.default_rng(0)
K = rng.normal(size=(57, 9, 251))
t = time.time()
lab = np.array([B.kmeans(K[:, :, i], 3, seed=1000 + i, n_init=10) for i in range(251)])
print("kmeans 251:", time.time() - t)
D = np.array([squareform(pdist(K[:, :, i])) for i in range(251)])
labs = rng.integers(0, 3, 57)
w = rng.multinomial(57, np.ones(57) / 57, size=1000)
t = time.time(); r1 = B.separability(D, labs, w); print("sep boot:", time.time() - t)
t = time.time(); r2 = B.separability(D, lab, w); print("sep boot 2d:", time.time() - t)
EOF
```

```
kmeans 251: 1.6762490272521973
sep boot: 2.0442922115325928
sep boot 2d: 2.040766954421997
```

**Agent**

The bootstrap quadratic forms in `separability` dominate (2 s each, 500 calls). I'll rewrite them as one matrix product, which gives the same numbers.

**Agent calls Bash**

```bash
cd entries/000019-bouchard-2013; python - <<'EOF'
p = "bouchard.py"
s = open(p).read()
a = '''    w = np.asarray(weights, float)
    total_pairs = w.sum(1) ** 2 - w.sum(1)                          # (B,)
    within_pairs = np.einsum("bi,tij,bj->bt", w, same, w, optimize=True) - w.sum(1)[:, None]
    within_sum = np.einsum("bi,tij,bj->bt", w, same * D, w, optimize=True)
    all_sum = np.einsum("bi,tij,bj->bt", w, D, w, optimize=True)'''
b = '''    w = np.asarray(weights, float)

    def quad(A):
        """sum over i, j of w[b, i] A[t, i, j] w[b, j], as one matrix product: (B, time)."""
        X = (w @ A.transpose(1, 0, 2).reshape(n, -1)).reshape(len(w), A.shape[0], n)
        return np.einsum("btj,bj->bt", X, w)

    total_pairs = w.sum(1) ** 2 - w.sum(1)                          # (B,)
    within_pairs = quad(same) - w.sum(1)[:, None]
    within_sum = quad(same * D)
    all_sum = quad(D)'''
assert s.count(a) == 1
open(p, "w").write(s.replace(a, b))
EOF
export PYTHONPATH=$PWD; $TMPDIR/devenv/bin/python - <<'EOF'
import numpy as np, time
import bouchard as B
from scipy.spatial.distance import pdist, squareform
rng = np.random.default_rng(0)
K = rng.normal(size=(57, 9, 251))
D = np.array([squareform(pdist(K[:, :, i])) for i in range(251)])
labs = rng.integers(0, 3, 57)
lab2 = rng.integers(0, 3, (251, 57))
w = rng.multinomial(57, np.ones(57) / 57, size=1000)
def old(D, labels, weights):
    n = D.shape[1]
    lab = labels if labels.ndim == 2 else np.broadcast_to(labels, (D.shape[0], n))
    same = (lab[:, :, None] == lab[:, None, :]).astype(float)
    w = np.asarray(weights, float)
    tp = w.sum(1) ** 2 - w.sum(1)
    wp = np.einsum("bi,tij,bj->bt", w, same, w, optimize=True) - w.sum(1)[:, None]
    ws = np.einsum("bi,tij,bj->bt", w, same * D, w, optimize=True)
    al = np.einsum("bi,tij,bj->bt", w, D, w, optimize=True)
    return (al - ws) / (tp[:, None] - wp) - ws / wp
for L in (labs, lab2):
    t = time.time(); r1 = B.separability(D, L, w); print("new", time.time() - t)
    r0 = old(D, L, w); print("max abs diff", np.abs(r1 - r0).max())
    print("unweighted diff", np.abs(B.separability(D, L) - old(D, L, np.ones((1, 57)))).max())
EOF
```

```
new 0.09525823593139648
max abs diff 3.9968028886505635e-14
unweighted diff 4.440892098500626e-15
new 0.09029936790466309
max abs diff 4.263256414560601e-14
unweighted diff 4.440892098500626e-15
```

**Agent**

20 times faster with identical results (differences below 1e-13). Now the outputs, claim by claim.

**Agent calls Bash**

```bash
sed -n 150,186p $TMPDIR/out1.txt; sed -n 320,333p $TMPDIR/out1.txt; sed -n 436,441p $TMPDIR/out1.txt
```

```
===== cell 21 (0 s)
baseline CVs subject  vSMC  (a) z > 2  (b) |z| > 2
     pre all     EC2    86         15           15
     pre all    GP31    83         49           49
     pre all    GP33    99          9            9
     pre 15+     EC2    86         14           14
     pre 15+    GP31    83          9            9
     pre 15+    GP33    99          9            9
   whole all     EC2    86         15           15
   whole all    GP31    83         43           43
   whole all    GP33    99          6            6
   whole 15+     EC2    86         15           15
   whole 15+    GP31    83          0            0
   whole 15+    GP33    99          6            6
    rest all     EC2    86         30           30
    rest all    GP31    83         51           51
    rest all    GP33    99         21           21
    rest 15+     EC2    86         29           29
    rest 15+    GP31    83         31           31
    rest 15+    GP33    99         21           21
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 228,232p $TMPDIR/out1.txt; sed -n 228,330p $TMPDIR/out1.txt | grep "^ *rest" | head -40; sed -n 339,345p $TMPDIR/out1.txt; sed -n 339,440p $TMPDIR/out1.txt | grep "^ *rest" | awk '{print $NF}' | sort | uniq -c
```

```
===== cell 27 (0 s)
baseline CVs                            timing reading p-value EC2 lips+ / hits / max /ju/ GP31 lips+ / hits / max /ju/ GP33 lips+ / hits / max /ju/  holds
     pre all         per subject / all six / threshold  F-test               11 / 0 / 0.96                29 / 0 / 0.40                14 / 0 / 0.78  False
     pre all         per subject / all six / threshold  t-test                8 / 0 / 0.96                30 / 0 / 0.40                13 / 0 / 0.78  False
     pre all         per subject / all six / half peak  F-test                8 / 0 / 0.96                25 / 0 / 0.40                15 / 0 / 0.78  False
    rest all         per subject / all six / threshold  F-test               10 / 0 / 2.41                27 / 0 / 0.94                17 / 0 / 1.56  False
    rest all         per subject / all six / threshold  t-test                9 / 0 / 1.25                25 / 0 / 0.83                18 / 0 / 1.56  False
    rest all         per subject / all six / half peak  F-test                8 / 0 / 1.18                24 / 0 / 0.94                12 / 0 / 1.56  False
    rest all         per subject / all six / half peak  t-test                6 / 0 / 1.18                19 / 0 / 0.83                 7 / 0 / 0.52  False
    rest all per subject / per articulator / threshold  F-test               11 / 0 / 1.18                24 / 0 / 0.83                17 / 0 / 1.00  False
    rest all per subject / per articulator / threshold  t-test               10 / 0 / 3.54                26 / 0 / 0.83                14 / 0 / 0.48  False
    rest all per subject / per articulator / half peak  F-test                9 / 0 / 1.18                24 / 0 / 0.94                10 / 0 / 1.56  False
    rest all per subject / per articulator / half peak  t-test                6 / 0 / 3.54                25 / 0 / 0.83                 6 / 0 / 0.48  False
    rest all              pooled / all six / threshold  F-test               11 / 0 / 1.18                22
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 442,446p $TMPDIR/out1.txt | cut -c1-400; sed -n 538,551p $TMPDIR/out1.txt; grep -n "True *partially\|True *reproduced" $TMPDIR/out1.txt | sed -n 1,5p | cut -c1-50; awk 'NR>442 && NR<540' $TMPDIR/out1.txt | grep -c "^ *rest"
```

```
===== cell 35 (0 s)
Acoustic onset, substitute from the hand-marked syllable starts: mean over 169 CVs -109.6 ms (per subject {'EC2': -86.6, 'GP31': -113.2, 'GP33': -129.2}; CV range -257 to -11 ms)
baseline CVs                            timing reading ANOVA on   n  n Lips  n Tongue  n Larynx  n Jaw  n Back T  n High T    F            p  onset Lips  onset Tongue  onset Larynx  onset Jaw  onset Back T  onset High T  peak Back  peak High  lips,tongue < acoustic  jaw,larynx later  vowel peaks 250+-25        outcome  lips,tongue < 0 outcome vs t = 0
     pre all         per subject / all six / threshold    onset 175      31         5        18     34        38        49 22.5 3.008100e-17        -173           160           -13       -136           165           224        235        305                   False             False                False not reproduced            False   not reproduced
     pre all         per subject / all six / threshold     peak 175      31         5        18     34        38        49 27.2 4.093779e-20        -173           160           -13       -136           165           224        235        305                   False             False                False not reproduced            False   not reproduced
    rest 15+      pooled / per articulator / threshold     peak 187      26        45        28     33        26        29 16.6 1.751393e-13        -133           242           114       -140           166           212        263        325                   False             False                False not reproduced            False   not reproduced
    rest 15+      pooled / per articulator / half peak    onset 187      26        45        28     33        26        29 19.5 1.594970e-15        -213           204            32       -249            52            99        263        325                   False             False                False not reproduced            False   not reproduced
    rest 15+      pooled / per 
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 552,590p $TMPDIR/out1.txt; sed -n 660,720p $TMPDIR/out1.txt
```

```
===== cell 38 (0 s)
baseline z-scoring CVs      window   EC2  GP31  GP33  mean  within 0.54-0.66
     pre       row all -500 to 750 0.607 0.734 0.536 0.625              True
     pre       row all -375 to 620 0.624 0.743 0.549 0.639              True
     pre       row 15+ -500 to 750 0.605 0.665 0.536 0.602              True
     pre       row 15+ -375 to 620 0.621 0.675 0.549 0.615              True
     pre      time all -500 to 750 0.440 0.677 0.468 0.528             False
     pre      time all -375 to 620 0.458 0.681 0.475 0.538             False
     pre      time 15+ -500 to 750 0.438 0.562 0.468 0.490             False
     pre      time 15+ -375 to 620 0.454 0.565 0.475 0.498             False
   whole       row all -500 to 750 0.608 0.743 0.539 0.630              True
   whole       row all -375 to 620 0.625 0.752 0.552 0.643              True
   whole       row 15+ -500 to 750 0.606 0.651 0.539 0.598              True
   whole       row 15+ -375 to 620 0.621 0.659 0.552 0.611              True
   whole      time all -500 to 750 0.440 0.691 0.473 0.535             False
   whole      time all -375 to 620 0.459 0.695 0.481 0.545              True
   whole      time 15+ -500 to 750 0.438 0.560 0.473 0.490             False
   whole      time 15+ -375 to 620 0.454 0.562 0.481 0.499             False
    rest       row all -500 to 750 0.608 0.790 0.552 0.650              True
    rest       row all -375 to 620 0.624 0.792 0.566 0.661             False
[... 79 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 795,900p $TMPDIR/out1.txt | cut -c1-260
```

```
baseline z-scoring projection CVs labels  subjects with both        outcome
     pre       row          i 15+      a                   0 not reproduced
     pre       row          i 15+      b                   0 not reproduced
     pre       row          i all      a                   1      partially
     pre       row          i all      b                   1      partially
     pre       row         ii 15+      a                   1      partially
     pre       row         ii 15+      b                   1      partially
     pre       row         ii all      a                   1      partially
     pre       row         ii all      b                   1      partially
     pre      time          i 15+      a                   0 not reproduced
     pre      time          i 15+      b                   0 not reproduced
     pre      time          i all      a                   0 not reproduced
     pre      time          i all      b                   0 not reproduced
     pre      time         ii 15+      a                   1      partially
     pre      time         ii 15+      b                   1      partially
     pre      time         ii all      a                   0 not reproduced
     pre      time         ii all      b                   0 not reproduced
    rest       row          i 15+      a                   1      partially
    rest       row          i 15+      b                   1      partially
    rest       row          i all      a                   1      partially
[... 86 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 898,1050p $TMPDIR/out1.txt | cut -c1-250 | head -130
```

```
===== cell 53 (923 s)
baseline z-scoring projection CVs          clusters  cons peak  cons onset a  cons onset b  vowel peak  vowel onset a  vowel onset b  peaks ok  onset ok a  onset ok b        outcome
     pre       row          i all groups a | groups          5        -240.0        -185.0         200          100.0           95.0     False       False       False not reproduced
     pre       row          i all groups b | groups          5        -260.0        -195.0         200          100.0           95.0     False       False       False not reproduced
     pre       row          i all   four a | groups        -65        -260.0        -210.0         200          100.0           95.0     False       False       False not reproduced
     pre       row          i all   four b | groups        -65        -270.0        -230.0         200          100.0           95.0     False       False       False not reproduced
     pre       row          i all   kmeans | kmeans        290        -165.0         240.0         290         -165.0          240.0     False       False       False not reproduced
     pre       row          i 15+ groups a | groups          5        -260.0        -190.0         205           80.0           90.0     False       False       False not reproduced
     pre       row          i 15+ groups b | groups          5        -275.0        -200.0         205           80.0           90.0     False       False       False not reproduced
     pre       row          i 15+   four a | groups        -60        -270.0        -220.0         205           80.0           90.0     False       False       False not reproduced
     pre       row          i 15+   four b | groups        -60        -275.0        -235.0         205           80.0           90.0     False       False       False not reproduced
     pre       row          i 15+   kmeans | kmeans       -135        -375.0        -395.0        -135         -240.0         -395.0     False       False    
[... 118 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1292,1360p $TMPDIR/out1.txt | cut -c1-250; sed -n 1640,1656p $TMPDIR/out1.txt | cut -c1-300; sed -n 1360,1650p $TMPDIR/out1.txt | awk '{print $NF}' | sort | uniq -c
```

```
Outcome over readings: differ by reading: not reproduced 145, partially 15, reproduced 80
Outcomes by reading of the clusters and of R:
outcome                              not reproduced  partially  reproduced
clusters          R                                                       
four a | groups   (a) matching set                0          4          20
                  (b) mean of three              24          0           0
four b | groups   (a) matching set                1          7          16
                  (b) mean of three              24          0           0
groups a | groups (a) matching set                0          0          24
                  (b) mean of three              24          0           0
groups b | groups (a) matching set                0          4          20
                  (b) mean of three              24          0           0
kmeans | kmeans   (a) matching set               24          0           0
                  (b) mean of three              24          0           0

===== cell 59 (0 s)
baseline z-scoring projection CVs                CV distance  pairs  median CC  median VV  median CV         CV>CC         CV>VV         CC>VV  orderings hold        outcome
     pre       row          i all (a) mean of cross pairings   4677       8.78       5.88      10.39 +1.17 p=0e+00 +3.98 p=0e+00 +2.44 p=0e+00            True      partially
     pre       row          i all    (b) i at -25, j at +250   4677       8.78       5.88      10.28 +1.25 p=0e+00 +3.59 p=0e+00 +2.44 p=0e+00            True      partially
     pre       row          i 15+ (a) mean of cross pairings   4567       9.33       6.37      11.11 +1.33 p=0e+00 +4.33 p=0e+00 +2.65 p=0e+00            True      partially
[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000019-bouchard-2013; python -c "
import json;nb=json.load(open('reproduce_bouchard_2013.ipynb'))
for i in [26,34,37,61]:
    c=nb['cells'][i]; print('=====',i); print(''.join(c['source']))
"
```

```
===== 26
## fig1f-h-phonetic-contrasts

> Fricatives with different tongue-tip constriction locations engaged different electrodes;
> front-tongue consonants of different manner engaged overlapping electrodes with different
> magnitudes; for /ja/, /ji/, /ju/ the activity was similar before the C-V transition, while a
> dorsal electrode was active during /u/ only.

The judged part: in at least one subject, a vSMC electrode with a positive lips weight (from the
GLM electrodes of claim fig2a-lips-dorsal) has mean high gamma above 2 at +250 ms for /ju/ and
below 2 for /ja/ and /ji/. The lips weights and the GLM electrodes are computed without electrode
positions, which are only needed for fig2a's spatial judgement (see the summary).
===== 34
## fig3d-timing-sequence

> Articulator correlations follow a staggered sequence consistent across subjects; lip and tongue
> correlations begin well before sound onset, jaw and larynx align to the C-V transition, and the
> high and back tongue vowel features peak near the vowel midpoint (~250 ms).

Acoustic onset: the dandiset has no audio, so the onset of each CV is taken from the hand-marked
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000019-bouchard-2013; cat > $TMPDIR/edit3.py <<'EOF'
exec(open(__import__("os").environ["TMPDIR"] + "/nbedit.py").read())
# fig1f: count lips-positive electrodes with /ju/ above 2, and how many of them have /ja/ and /ji/ below 2
rep(27, '''        hit = cand & (Hj["u"] > 2) & (Hj["a"] < 2) & (Hj["i"] < 2)
        hits[s] = (int(cand.sum()), int(hit.sum()), float(Hj["u"][cand].max()) if cand.any() else np.nan)''',
'''        hit = cand & (Hj["u"] > 2) & (Hj["a"] < 2) & (Hj["i"] < 2)
        hits[s] = (int(cand.sum()), int((cand & (Hj["u"] > 2)).sum()), int(hit.sum()),
                   float(Hj["u"][cand].max()) if cand.any() else np.nan)''')
rep(27, '''               **{f"{s} lips+ / hits / max /ju/": f"{hits[s][0]} / {hits[s][1]} / {hits[s][2]:.2f}" for s in B.SUBJECTS},
               "holds": any(h[1] > 0 for h in hits.values())})''',
'''               **{f"{s} lips+ / ju>2 / hits / max /ju/": f"{hits[s][0]} / {hits[s][1]} / {hits[s][2]} / {hits[s][3]:.2f}" for s in B.SUBJECTS},
               "ju>2": sum(h[1] for h in hits.values()), "holds": any(h[2] > 0 for h in hits.values())})''')
rep(27, '''      max(float(v.split(" / ")[2]) for c in fh.columns if "max /ju/" in c for v in fh[c]))''',
'''      max(float(v.split(" / ")[3]) for c in fh.columns if "max /ju/" in c for v in fh[c]))
print("Readings with a lips-positive GLM electrode above 2 for /ju/:", int((fh["ju>2"] > 0).sum()), "of", len(fh),
      "(baselines:", fh[fh["ju>2"] > 0].baseline.value_counts().to_dict(), "); in all of them /ja/ or /ji/ is also above 2 there" if not fh.holds.any() else "")''')
# suppfig6: ranges of the preferred share per group
rep(32, '''print("\\nReadings where it holds:", int(s6.holds.sum()), "of", len(s6))''',
'''print("\\nReadings where it holds:", int(s6.holds.sum()), "of", len(s6))
for a, name in enumerate(B.ARTICULATORS):
    v = [float(x.split(" ")[1].split("/")[a]) for x in s6[name] if x != "none"]
    print(f"{name} group: preferred share {min(v):.0f} to {max(v):.0f}% over the {len(v)} readings with such electrodes")
print("GLM electrodes over the three subjects:", s6.electrodes.min(), "to", s6.electrodes.max())''')
save()
EOF
$TMPDIR/devenv/bin/python $TMPDIR/edit3.py && export PYTHONPATH=$PWD && $TMPDIR/devenv/bin/python $TMPDIR/runtest.py 27,32 2>/dev/null | grep -v "^ *\(pre\|whole\|rest\) "
```

```
===== cell 27 (0 s)
baseline CVs                            timing reading p-value EC2 lips+ / ju>2 / hits / max /ju/ GP31 lips+ / ju>2 / hits / max /ju/ GP33 lips+ / ju>2 / hits / max /ju/  ju>2  holds

Readings where it holds: 0 of 96
Largest /ju/ z at +250 ms among lips-positive GLM electrodes, over all readings and subjects: 3.54
Readings with a lips-positive GLM electrode above 2 for /ju/: 13 of 96 (baselines: {'rest': 13} ); in all of them /ja/ or /ji/ is also above 2 there
Outcome over readings: not reproduced
EC2: plotted electrode 107 (largest /ju/ minus /ja/,/ji/ at +250 ms among lips+ GLM electrodes), z at +250 ms: /ja/ -0.18, /ji/ -0.37, /ju/ 0.96; plotted range -0.56 to 1.03; mean |difference| between the three before 0 ms 0.18
GP31: plotted electrode 108 (largest /ju/ minus /ja/,/ji/ at +250 ms among lips+ GLM electrodes), z at +250 ms: /ja/ -0.22, /ji/ -0.36, /ju/ 0.15; plotted range -0.39 to 0.29; mean |difference| between the three before 0 ms 0.12
GP33: plotted electrode 110 (largest /ju/ minus /ja/,/ji/ at +250 ms among lips+ GLM electrodes), z at +250 ms: /ja/ -0.02, /ji/ -0.38, /ju/ 0.61; plotted range -0.81 to 1.14; mean |difference| between the three before 0 ms 0.29

===== cell 32 (0 s)
Group means of positive weights as % (Lips/Tongue/Larynx/Jaw), electrodes grouped by largest W:
baseline CVs                            timing reading p-value  electrodes  with an articulator lacking T_A  no positive weight            Lips          Tongue           Larynx             Jaw  holds

Readings where it holds: 96 of 96
Lips group: preferred share 63 to 79% over the 96 readings with such electrodes
Tongue group: preferred share 48 to 96% over the 95 readings with such electrodes
Larynx group: preferred share 49 to 84% over the 96 readings with such electrodes
Jaw group: preferred share 69 to 84% over the 96 readings with such electrodes
[... 2 more lines not kept]
```

**Agent**

Now checking a few details for the conclusions (which subject meets both hierarchy splits, and fig5d R2 ranges).

**Agent calls Bash**

```bash
cd $TMPDIR; awk '/===== cell 47/,/===== cell 50/' out1.txt | head -3 | cut -c1-400; awk '/===== cell 47/,/subjects with both/' out1.txt | awk 'NR>2' | grep -v "subjects with both" | awk '{n=split($0,a," "); print $1,$2,$3,$4,$5}' | head -3
```

```
===== cell 47 (0 s)
baseline z-scoring projection CVs subject     cons (a) majorities  cons (a) in home  cons (a) holds  cons (a) co-clust     cons (b) majorities  cons (b) in home  cons (b) holds  cons (b) co-clust a/i/u in cluster 1  vowel holds
     pre       row          i all     EC2   coronal/labial/dorsal              0.98            True               0.98   coronal/labial/dorsal              0.93            True               0.92     0.74/0.58/0.11         True
pre row i all EC2
pre row i all GP31
pre row i all GP33
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; awk '/===== cell 47/,/subjects with both/' out1.txt | awk 'NR>2 && NF>10' | awk '{both_a=($8=="True" && $NF=="True"); both_b=($12=="True" && $NF=="True"); print $5, both_a||both_b, $NF}' | sort | uniq -c; awk '/===== cell 56/,/Outcome over/' out1.txt | grep "groups a | groups\|four\|groups b" | grep "matching" | awk '{print $8,$9,$10,$11,$12,$13}' | tr ' ' '\n' | sort -n | sed -n '1p;$p'
```

```
3 EC2 0 False
      7 EC2 0 True
     14 EC2 1 True
     24 GP31 0 False
     18 GP33 0 False
      6 GP33 0 True
(a)
0.98
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
import re
txt = open("out1.txt").read()
sec = txt.split("===== cell 56")[1].split("Outcome over readings")[0]
vals = []
for line in sec.splitlines():
    if "matching" in line and "kmeans" not in line:
        m = re.search(r"matching set\s+((?:[\d.]+ ){5}[\d.]+)", line)
        vals += [float(x) for x in m.group(1).split()]
print(len(vals), min(vals), max(vals))
EOF
```

```
576 0.14 0.99
Shell cwd was reset to
```

**Agent**

Now the notebook text: header, data-check note, every affected conclusion and the summary.

**Agent calls Bash**

```bash
cd entries/000019-bouchard-2013; cat > $TMPDIR/edit4.py <<'PYEOF'
exec(open(__import__("os").environ["TMPDIR"] + "/nbedit.py").read())
rep(0, '''Readings. Where the claims file leaves a method detail open it names readings, and every
reading is run; a claim's outcome is the one all its method readings give. Two readings are added
here as questions to the reader (`questions/000019.yaml`): how the state-space input is z-scored
(`row`: each electrode's concatenated series; `time`: each electrode at each time across
syllables), and the dataset's rest period as a baseline (shown as a variant only).''',
'''Readings. Where the claims file leaves a method detail open it names readings, and every
reading is run; a claim's outcome is the one all its method readings give, and it is blocked as
methods_underspecified when they differ. The first run of this attempt asked five questions
(`questions/000019.yaml`), answered by a reader on 2026-10-22, and the claims file now names
these readings, all run here:

- the baseline of the z-scores: (a) `pre`, -1000 to -500 ms before each C-V transition; (b)
  `whole`, the whole block; (c) `rest`, the rest period the dataset marks as baseline (a reading
  since the answer; the first run showed it as a variant only);
- the CVs averaged: (a) every CV the dataset holds (`all`); (b) only CVs with 15 or more
  renditions (`15+`); the paper does not say which;
- the z-scoring before the PCA: `row`, each electrode's whole concatenated (CV x time) series;
  `time`, each electrode across CVs at each time; the paper does not say which;
- the input projected onto the PCs to give the states: (i) the z-scored matrix given to the PCA;
  (ii) the baseline z-scored high gamma, as Methods Eq. 5 writes it (added with the answer);
- the acoustic onset of fig3d: the dandiset has no audio, and the hand-marked syllable start may
  stand in for it as a deviation, with the result against t = 0 shown beside it (the answer).

The fifth answer says the paper gives no way to derive the distances from the central sulcus and
Sylvian fissure from grid geometry or unlabelled coordinates, so the spatial claims stay blocked.''')
rep(12, '''reach higher maxima (ranges above). That variant is shown where it matters.''',
'''reach higher maxima (ranges above). The rest period is baseline reading (c) of the claims file.''')
rep(15, '''The partial correlations and the GLM (Methods Eqs. 2 to 4) are computed once per baseline, and
the state space (Methods Eq. 5) once per baseline and z-scoring reading.''',
'''The partial correlations and the GLM (Methods Eqs. 2 to 4) are computed once per baseline and
CV set, and the state space (Methods Eq. 5) once per baseline, CV set and z-scoring reading; the
states K of each CV are then projected from the PCA input (reading i) or from the baseline
z-scored high gamma (reading ii).''')
setsrc(22, '''**Result: blocked (methods_underspecified).** The two readings of the CV set give different
outcomes. With every CV, no baseline gives a mean within 27 to 33: 24.3 per subject with `pre`
(EC2 15, GP31 49, GP33 9), 21.3 with `whole` and 34.0 with `rest` (not reproduced). With only the
CVs of 15 or more renditions, `rest` gives 27.0 (EC2 29, GP31 31, GP33 21), at the lower edge of
the tolerance, while `pre` gives 10.7 and `whole` 7.0 (partially reproduced). Both readings of
the change give the same counts, as no electrode passes on a decrease alone. The count moves
strongly with the threshold (with every CV, 41.7 to 5.3 per subject over thresholds 1.5 to 3 with
`pre`).''')
setsrc(28, '''**Result: not reproduced.** Under all 96 readings (three baselines, two CV sets, eight timing
readings for T_A, two p-value readings) no GLM electrode with a positive lips weight has z above 2
for /ju/ at +250 ms and below 2 for /ja/ and /ji/. With the `rest` baseline some do exceed 2 for
/ju/ (13 of 96 readings, largest 3.54), but at each of them /ja/ or /ji/ is above 2 as well; under
`pre` and `whole` none reaches 2. The /ju/ responses of the plotted electrodes are larger than
/ja/ and /ji/ at +250 ms, but under the threshold. The other parts of the claim are not judged
(no measure in the paper).''')
rep(29, '''sulcus, and no electrode is labelled as on the guenon. These claims are blocked as
metadata_insufficient.''',
'''sulcus, and no electrode is labelled as on the guenon. Asked whether the paper gives a way to
obtain these distances from the grid geometry, the reader answered that it does not: the paper
measures them on each subject's MRI reconstruction. These claims stay blocked as
metadata_insufficient.''')
setsrc(33, '''**Result: reproduced.** Under all 96 readings each group's preferred articulator has the largest
mean share of positive weight (Lips 63 to 79%, Tongue 48 to 96%, Larynx 49 to 84%, Jaw 69 to
84%), and the other articulators keep a non-zero share (table). In one reading no electrode
prefers the tongue, so that group is absent there. The GLM electrodes number 49 to 117 over the
three subjects. In readings where an articulator has no window T_A in a subject, its weights there
are missing and those electrodes are grouped on the other articulators.''')
rep(34, '''Acoustic onset: the dandiset has no audio, so the onset of each CV is taken from the hand-marked
syllable start of the trial table (mean over renditions, then over CVs). This replaces the
prototype and thresholding of the Methods (a deviation, asked as a question).''',
'''Acoustic onset: the dandiset has no audio, so the onset of each CV is taken from the hand-marked
syllable start of the trial table (mean over renditions, then over CVs). The criterion allows this
substitute since the reader's answer, as a deviation from the prototype and thresholding of the
Methods, with the result against t = 0 shown beside it.''')
setsrc(36, '''**Result: not reproduced.** Under every one of the 96 readings none of the three order conditions
holds, against the substitute acoustic onset (-110 ms) and against t = 0 alike. The lips
correlations begin before the substitute onset (mean lips onset -270 to -54 ms), but the tongue
correlations begin at -26 to +290 ms, so lips and tongue both precede the substitute onset in no
reading and precede t = 0 in 2 of 96; the jaw begins as early as the lips (-270 to -116 ms), not
later; and the high-tongue peak is at 276 to 325 ms, outside 250 +- 25 ms. The ANOVA across the
six articulators has F = 9.4 to 39.2, with p below 1e-10 in 76 of the 96 readings. Electrode
counts are 162 to 226 (paper 211).''')
setsrc(39, '''**Result: blocked (methods_underspecified).** With `row` z-scoring, the first nine PCs explain a
mean of 0.60 to 0.66 over subjects, within 0.54 to 0.66 in 11 of 12 readings (`rest`, every CV and
the -375 to 620 ms window gives 0.661). With `time` z-scoring, the mean is 0.49 to 0.56, within the
tolerance under the `rest` baseline (4 readings) and once under `whole`, and below it in the other
7 readings. The readings give different outcomes (16 within, 8 not). The variance explained does
not depend on the input projected. The spectra show no sharp change at the ninth eigenvalue in any
subject (printed values); that part is not judged.''')
setsrc(42, '''**Result: blocked (methods_underspecified).** In 23 of the 24 readings three clusters do not
have the highest mean silhouette (not reproduced). In one, `rest` baseline, `time` z-scoring,
projection (i) and every CV, k = 3 is highest by a small margin (0.333 against 0.329 for k = 2),
with values outside tolerance (partially reproduced), so the readings differ. The silhouettes are
lower than the paper's under every reading (k = 3: 0.19 to 0.36 against 0.47). With every CV,
GP31's k = 2 silhouette is high in several readings because its /thi/, with two renditions, stands
apart from all other CVs.''')
setsrc(45, '''**Result: blocked (methods_underspecified).** The state-space clusters match the major
articulators more than chance under every reading (consonant p from 3e-13 to 9e-23). The observed
consonant medians (0.60 to 0.91) are above the paper's 0.50 +- 0.05, and the vowel medians (0.41 to
0.70) are mostly below its 0.65 +- 0.065, so 38 of the 48 readings (24 readings by two label
readings) give partially reproduced. In five readings, all with projection (i) (`row` with 15+ CVs
under each baseline, `rest` with `row` and every CV, and `rest` with `time` and 15+ CVs), the vowel
test misses the p < 1e-10 bound (p 4e-11 to 5e-07... see table) and gives not reproduced.''')
setsrc(48, '''**Result: blocked (methods_underspecified).** Both splits hold together in at most one subject,
EC2 (14 of the 24 readings), so no reading gives reproduced; 28 of the 48 readings (with the two
label readings) give partially reproduced and 20 not reproduced. Under `time` z-scoring with
projection (i) no subject meets both. The vowel split (/u/ against /a/ and /i/) never holds in GP31.''')
setsrc(51, '''**Result: blocked (methods_underspecified).** In the early window, constriction location
correlates with the state-space distances more than constriction degree, and degree more than the
vowel, with p < 1e-10 under every reading with Euclidean distances except two (`rest`, projection
(i), 15+ CVs, where location over degree has p = 3e-05 and 3e-04). In the late window the vowel
features correlate more than both other sets with p < 1e-10 in 10 of the 24 readings (reproduced):
every 15+ reading with projection (ii), `pre` and `whole` with `time`, projection (i) and 15+ CVs,
and `rest` with projection (ii) and every CV. In the other 14 the late comparisons fail in part
(partially reproduced), mostly with every CV, where location correlates as much as or more than
the vowel features. Hamming distances (a variant) give similar results.''')
setsrc(54, '''**Result: not reproduced.** Under none of the 120 readings (24 baseline, z-scoring, projection
and CV readings by five cluster readings) are both peaks within tolerance. With the phonetic
groups the consonant separability peaks at -155 to +15 ms (paper -200 +- 20) and the vowel
separability at 155 to 235 ms (paper 250 +- 25, within it in some readings); with k-means at each
time one curve serves both, peaking anywhere from -170 to 375 ms. The consonant onsets (reading a,
-375 to -185 ms) reach the paper's -300 +- 30 ms under some readings, and the vowel onsets (55 to
105 ms) are mostly later than its 50 +- 10 ms.''')
setsrc(57, '''**Result: blocked (methods_underspecified).** With the phonetic groups as clusters and the
matching feature set for R (constriction location for consonants, vowel features for vowels), the
six R2 values lie within 0.38 to 1 with p < 1e-10 in 80 of 96 readings, are positive and
significant with some below 0.38 in 15, and fail in 1 (R2 0.14 to 0.99 over these readings). With
the mean of the three feature sets, or with k-means clusters at each time, the coupling fails in
every reading. The readings of the claim give different outcomes.''')
setsrc(60, '''**Result: blocked (methods_underspecified).** Under `row` z-scoring, and under `time` z-scoring
with projection (ii), consonant-vowel distances exceed consonant-consonant ones, which exceed
vowel-vowel ones, with corrected p < 1e-10. Under `time` z-scoring with projection (i) the
consonant-vowel distances are shorter than the consonant-consonant ones, in every baseline and CV
set. The number of pairs is 4677 with every CV and 4567 with CVs of 15 or more renditions, never
the paper's 4623, so the readings where the orderings hold give partially reproduced (36 of 48)
and the others not reproduced (12).''')
setsrc(63, '''**Result: not reproduced.** Under all 288 readings the condition fails in all three PCs. In the
reading printed in full (all 268 vSMC electrodes, `pre`, every CV), the tongue weights are not
larger than the lips weights (median paired difference of log10 weights, lips minus tongue, +0.03,
corrected p = 1), and jaw and larynx differ (corrected p = 5e-11). The input projected does not
enter this test, which uses the PCs only.''')
save()
PYEOF
$TMPDIR/devenv/bin/python $TMPDIR/edit4.py && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd $TMPDIR; awk '/===== cell 41/,/Mean over subjects/' out1.txt | grep GP31 | awk '{print $4, $6}' | sort | awk '{a[$1]=a[$1]" "$2} END{for(k in a) print k, a[k]}'
```

```
15+  0.244 0.303 0.329 0.333 0.370 0.430 0.435 0.488 0.507 0.596 0.671 0.675
all  0.350 0.512 0.516 0.605 0.654 0.659 0.759 0.776 0.782 0.783 0.793 0.801
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/000019-bouchard-2013; cat > $TMPDIR/edit5.py <<'PYEOF'
exec(open(__import__("os").environ["TMPDIR"] + "/nbedit.py").read())
rep(42, '''lower than the paper's under every reading (k = 3: 0.19 to 0.36 against 0.47). With every CV,
GP31's k = 2 silhouette is high in several readings because its /thi/, with two renditions, stands
apart from all other CVs.''', '''lower than the paper's under every reading (k = 3: 0.19 to 0.36 against 0.47). GP31's k = 2
silhouette is 0.35 to 0.80 with every CV, where its /thi/ has two renditions, and 0.24 to 0.68 with
only CVs of 15 or more renditions.''')
rep(45, '''articulators more than chance under every reading (consonant p from 3e-13 to 9e-23).''',
        '''articulators more than chance under every reading (consonant p from 9e-23 to 3e-13).''')
rep(45, '''test misses the p < 1e-10 bound (p 4e-11 to 5e-07... see table) and gives not reproduced.''',
        '''test misses the p < 1e-10 bound (p from 3e-10 to 5e-07) and gives not reproduced.''')
save()
PYEOF
$TMPDIR/devenv/bin/python $TMPDIR/edit5.py && echo ok
```

```
ok
```

**Agent**

Now the summary cell.

**Agent calls Bash**

```bash
cd entries/000019-bouchard-2013; cat > $TMPDIR/edit6.py <<'PYEOF'
exec(open(__import__("os").environ["TMPDIR"] + "/nbedit.py").read())
rep(64, "| active-electrodes | not reproduced |", "| active-electrodes | blocked: methods_underspecified |")
rep(64, "| fig4a-consonant-clusters | not reproduced |", "| fig4a-consonant-clusters | blocked: methods_underspecified |")
rep(64, '''z-scores is not given by the paper; both readings of the claims file are run. vSMC electrodes are
those labelled precentral or postcentral (268, against the paper's 266). The acoustic onset of
fig3d is the hand-marked syllable start, as the audio is not in the dandiset. Two method details
the claims file does not fix are run under both readings and asked as questions: how the
state-space input is z-scored, and whether CVs with fewer than 15 renditions are kept. Most of the
blocked outcomes for the state-space claims come from these readings giving different results,
and an answer could settle them. The GLM weights used by fig1f-h, suppfig6 and suppfig9 come from''',
'''z-scores is not given by the paper; the three readings of the claims file are run, the rest
period the dataset marks among them. vSMC electrodes are those labelled precentral or postcentral
(268, against the paper's 266). The acoustic onset of fig3d is the hand-marked syllable start, a
substitute the criterion allows as a deviation since the audio is not in the dandiset; the result
against t = 0 is the same. The questions asked by this attempt were answered from the paper,
which fixes none of the details asked about: whether CVs with fewer than 15 renditions are kept,
how the state-space input is z-scored, and which input is projected onto the PCs are all left
open, and every reading is run. The blocked outcomes of the state-space claims and of
active-electrodes come from these readings giving different results; the paper cannot settle
them. The GLM weights used by fig1f-h, suppfig6 and suppfig9 come from''')
save()
print(src(64))
PYEOF
$TMPDIR/devenv/bin/python $TMPDIR/edit6.py | sed -n 28,60p
```

```
A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

How the analysis differs from the paper's. High gamma is computed here from the raw ECoG, as
the Methods describe, with a filter bank whose widths the paper does not give (a standard choice)
and with the dataset's bad-channel flags in place of the paper's inspection. The baseline for the
z-scores is not given by the paper; the three readings of the claims file are run, the rest
period the dataset marks among them. vSMC electrodes are those labelled precentral or postcentral
(268, against the paper's 266). The acoustic onset of fig3d is the hand-marked syllable start, a
substitute the criterion allows as a deviation since the audio is not in the dandiset; the result
against t = 0 is the same. The questions asked by this attempt were answered from the paper,
which fixes none of the details asked about: whether CVs with fewer than 15 renditions are kept,
how the state-space input is z-scored, and which input is projected onto the PCs are all left
open, and every reading is run. The blocked outcomes of the state-space claims and of
active-electrodes come from these readings giving different results; the paper cannot settle
them. The GLM weights used by fig1f-h, suppfig6 and suppfig9 come from
claim fig2a-lips-dorsal, which is blocked for its spatial judgement only; the weights need no
positions, so these claims are tested.

What was found about the dataset. It holds four subjects; EC2, GP31 and GP33 fit the paper's
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000019-bouchard-2013; cat > $TMPDIR/edit7.py <<'PYEOF'
exec(open(__import__("os").environ["TMPDIR"] + "/nbedit.py").read())
rep(64, "against t = 0 is the same.", "against t = 0 has the same outcome.")
rep(51, "Hamming distances (a variant) give similar results.", "Hamming distances, a variant, are in the table and are not judged.")
save()
print(src(19)); print(src(18))
PYEOF
$TMPDIR/devenv/bin/python $TMPDIR/edit7.py; grep -n "—\|rather\|\*\*" reproduce_bouchard_2013.ipynb | grep -v "Result:" | head
```

```
**Result: partially reproduced.** The dandiset holds the three subjects (taking GP31 and GP33 to
be EC31 and EC33) and a fourth one, EC9, that is not in the paper. The ECoG rate is 3051.76 Hz.
The counts differ from the paper's: 57, 55 and 57 CVs (169 in all, against 168), each subject with
19 consonants, and renditions of 2 to 107 per CV (EC2's /thi/ 10, GP31's /thi/ 2, GP31 up to 107).
Leaving out CVs with fewer than 15 renditions gives 56 + 54 + 57 = 167, still not the paper's
split. The audio is not in the dandiset, and GP33's hemisphere cannot be checked.
comp = []
for s in B.SUBJECTS:
    n = S[s]["counts"]
    comp.append({"subject": s, "CVs": len(S[s]["cvs"]), "consonants": len({c for c, v in S[s]["cvs"]}),
                 "vowels": len({v for c, v in S[s]["cvs"]}), "min_renditions": int(n.min()), "max_renditions": int(n.max()),
                 "CVs_below_15": int((n < 15).sum()), "CVs_above_100": int((n > 100).sum()),
                 "consonants_with_all_3_vowels_and_15+": len([c for c in B.CONSONANTS if all((c, v) in S[s]["cvs"] and n[S[s]["cvs"].index((c, v))] >= 15 for v in "aiu")]),
                 "hemisphere_from_x": ("left" if np.nanmean(S[s]["x"]) < 0 else "right") if np.isfinite(S[s]["x"]).any() else "unknown"})
comp = pd.DataFrame(comp)
print(comp.to_string(index=False))
print("Subjects in the dandiset:", sorted(files.subject.unique()), "| of the paper's (EC2, EC31, EC33), by assumed correspondence: 3")
print("Distinct CVs over the three subjects:", comp.CVs.sum(), "(paper 168); with CVs of fewer than 15 renditions left out:",
      int((comp.CVs - comp.CVs_below_15).sum()))
print("ECoG sampling rate:", sorted(files.rate_hz.unique()), "Hz (3052 +- 1)")
[... 7 more lines not kept]
```

**Agent**

Notebook done. Now the README, entry.yaml and the attempt record.

**Agent calls Bash**

```bash
cd entries/000019-bouchard-2013; python - <<'EOF'
p = "README.md"
s = open(p).read()
rep = [
("| About 30 active vSMC electrodes per subject | Not reproduced |", "| About 30 active vSMC electrodes per subject | Blocked: methods underspecified |"),
("| Three k-means clusters most parsimonious | Not reproduced |", "| Three k-means clusters most parsimonious | Blocked: methods underspecified |"),
("""Most claims blocked as methods underspecified depend on two details the claims file does not fix
and that were asked as questions (`questions/000019.yaml`): how the state-space input is z-scored,
and whether syllables with fewer than 15 renditions are kept.""",
"""The claims blocked as methods underspecified depend on details the paper does not fix: which
syllables are averaged (all, or only those with 15 or more renditions), the baseline of the
z-scores, how the state-space input is z-scored, and which input is projected onto the PCs. They
were asked as questions (`questions/000019.yaml`), and the reader's answers, from the paper, left
them open, so every reading is run and the outcomes differ between readings."""),
("""- `reproduce_bouchard_2013.ipynb`: the analysis. It takes about 15 minutes, 11 of them streaming
  about 42 GB of raw ECoG and computing high gamma.""",
"""- `reproduce_bouchard_2013.ipynb`: the analysis. It takes about 20 minutes, 14 of them streaming
  about 42 GB of raw ECoG and computing high gamma."""),
]
for a, b in rep:
    assert s.count(a) == 1, a[:50]
    s = s.replace(a, b)
open(p, "w").write(s)
p = "entry.yaml"
s = open(p).read()
s = s.replace("  runtime_minutes: 15", "  runtime_minutes: 20")
open(p, "w").write(s)
EOF
git diff --stat
```

```
entries/000019-bouchard-2013/README.md             |  14 +-
 entries/000019-bouchard-2013/bouchard.py           |  31 +-
 entries/000019-bouchard-2013/entry.yaml            |   2 +-
 .../reproduce_bouchard_2013.ipynb                  | 328 ++++++++++++---------
 4 files changed, 223 insertions(+), 152 deletions(-)
```

**Agent calls Bash**

```bash
cd  ls schemas 2>/dev/null || ls; grep -rn "author-answers\|answers" docs/protocol.md | head
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
28:`author`, `author-answers` when questions were answered, `verifier-1`,
166:(author, step 6). A reader answers each question from the paper, in the claims
274:   `methods_underspecified` until the question is answered. A reader answers from the paper (reader, step 6), and
275:   a later run, `author-answers`, takes up the answers.
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
print(json.dumps(s['properties'],indent=0)[:2500])
print(list(s.get('\$defs',{}).keys()))
print(json.dumps(s['\$defs'].get('outcome',{}).get('properties',{}),indent=0)[:2000])
"; sed -n 163,170p docs/protocol.md
```

```
Traceback (most recent call last):
  File "<string>", line 5, in <module>
    print(json.dumps(s['$defs'].get('outcome',{}).get('properties',{}),indent=0)[:2000])
                     ~^^^^^^^^^
KeyError: '$defs'
{
"schema_version": {
"const": 2
},
"id": {
"type": "string",
"pattern": "^[a-z0-9]+(-[a-z0-9]+)*$"
},
"dataset": {
"description": "The dataset the attempt tested: the archive and the dataset's identifier there.",
"type": "object",
"additionalProperties": false,
"required": [
"archive",
"id",
[... 115 more lines not kept]
```

**Agent**

Now the attempt record. I'll update it through a YAML round trip, which keeps the file's layout.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import yaml
s = open("attempts/000019-bouchard-2013-01.yaml").read()
d = yaml.safe_load(s)
out = yaml.dump(d, sort_keys=False, width=100, allow_unicode=True)
open("/tmp/claude-1001/rt.yaml", "w").write(out)
EOF
diff attempts/000019-bouchard-2013-01.yaml $TMPDIR/rt.yaml | head -20
```

```
5c5
<   id: "000019"
---
>   id: 000019
23,25c23,25
< - what: The articulator state matrix (Supplementary Figure 1d) and the phonetic feature matrix
<     (Supplementary Figure 12), transcribed from the figures of the paper's supplement. They define
<     the paper's variables for each syllable; they hold no measurements.
---
> - what: The articulator state matrix (Supplementary Figure 1d) and the phonetic feature matrix (Supplementary
>     Figure 12), transcribed from the figures of the paper's supplement. They define the paper's variables
>     for each syllable; they hold no measurements.
36,42c36,41
<   notes: The dandiset holds four subjects (EC2, EC9, GP31, GP33); EC2, GP31 and GP33 are taken to be
<     the paper's EC2, EC31 and EC33, and EC9 is not in the paper. The rate is 3051.76 Hz. The three
<     subjects have 57, 55 and 57 CVs (169, paper 168), each with 19 consonants, and 2 to 107
<     renditions per CV (EC2 /thi/ 10, GP31 /thi/ 2, 33 GP31 CVs above 100); leaving out CVs below 15
<     renditions gives 56 + 54 + 57 = 167. The audio was removed. EC2 and GP31 have negative x
<     coordinates (left hemisphere if x is the usual axis); GP33 has no coordinates, so the right
<     hemisphere of EC33 cannot be checked.
```

**Agent**

The round trip would unquote the dataset id, so I'll replace each claim's block as text instead.

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/att.py <<'PYEOF'
import re, textwrap, yaml
P = "attempts/000019-bouchard-2013-01.yaml"
s = open(P).read()

def wrap(key, text, indent="  "):
    return textwrap.fill(text, width=100, initial_indent=f"{indent}{key}: ", subsequent_indent=indent + "  ",
                         break_on_hyphens=False, break_long_words=False) + "\n"

def block(claim):
    m = re.search(rf"^- claim: {re.escape(claim)}\n(?:  .*\n)*", s, re.M)
    assert m, claim
    return m

def set_field(claim, key, text):
    """Replace a scalar field (notes, outcome, blocked_by) in a claim's block, or add it after `after`."""
    global s
    m = block(claim)
    b = m.group(0)
    f = re.search(rf"^  {key}: .*\n(?:    .*\n)*", b, re.M)
    new = wrap(key, text)
    assert f, (claim, key)
    b2 = b[:f.start()] + new + b[f.end():]
    s = s[:m.start()] + b2 + s[m.end():]

def add_after(claim, after_key, key, text):
    global s
    m = block(claim)
    b = m.group(0)
    f = re.search(rf"^  {after_key}: .*\n(?:    .*\n)*", b, re.M)
    b2 = b[:f.end()] + wrap(key, text) + b[f.end():]
    s = s[:m.start()] + b2 + s[m.end():]

def set_list(claim, key, items):
    """Replace a list field (deviations) of a claim's block, or append it at the end."""
    global s
    m = block(claim)
    b = m.group(0)
    new = f"  {key}:\n" + "".join(textwrap.fill(t, width=100, initial_indent="  - ", subsequent_indent="    ",
                                                break_on_hyphens=False, break_long_words=False) + "\n" for t in items)
    f = re.search(rf"^  {key}:\n(?:  - .*\n(?:    .*\n)*)+", b, re.M)
    b2 = (b[:f.start()] + new + b[f.end():]) if f else b + new
    s = s[:m.start()] + b2 + s[m.end():]

exec(open(__import__("os").environ["TMPDIR"] + "/attcontent.py").read())
open(P, "w").write(s)
yaml.safe_load(open(P))
print("ok")
PYEOF
echo written
```

```
written
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/attcontent.py <<'PYEOF'
def remove_field(claim, key):
    global s
    m = block(claim)
    b = m.group(0)
    f = re.search(rf"^  {key}:\n(?:  - .*\n(?:    .*\n)*)+", b, re.M)
    assert f, (claim, key)
    s = s[:m.start()] + b[:f.start()] + b[f.end():] + s[m.end():]

POS = (" The answer of 2026-10-22 to the question on positions says the paper measures them on each"
       " subject's MRI reconstruction and gives no way to derive them from grid geometry, unlabelled"
       " coordinates or atlas labels, so the block stands.")

set_field("data-composition", "notes", "The dandiset holds four subjects (EC2, EC9, GP31, GP33); EC2, GP31 and GP33 are taken to be the paper's EC2, EC31 and EC33, and EC9 is not in the paper. The rate is 3051.76 Hz. The three subjects have 57, 55 and 57 CVs (169, paper 168), each with 19 consonants, and 2 to 107 renditions per CV (EC2 /thi/ 10, GP31 /thi/ 2, 33 GP31 CVs above 100); leaving out CVs below 15 renditions gives 56 + 54 + 57 = 167. The audio was removed. EC2 and GP31 have negative x coordinates (left hemisphere if x is the usual axis); GP33 has no coordinates, so the right hemisphere of EC33 cannot be checked. The answer of 2026-10-22 on CVs with fewer than 15 renditions leaves this claim as it was; the paper's 168 CVs fit neither reading, and the outcome is unchanged.")

set_field("active-electrodes", "outcome", "blocked")
add_after("active-electrodes", "outcome", "blocked_by", "methods_underspecified")
set_field("active-electrodes", "notes", "Mean active vSMC electrodes per subject. With every CV, 24.3 with the pre-utterance baseline (EC2 15, GP31 49, GP33 9), 21.3 with the whole block and 34.0 with the rest period; none is within 27 to 33, so this CV reading gives not reproduced. With only CVs of 15 or more renditions, 10.7, 7.0 and 27.0 (rest; EC2 29, GP31 31, GP33 21), so one baseline is within tolerance, at its lower edge, and this reading gives partially reproduced. Both readings of the change give the same counts. The count depends strongly on the threshold (41.7 at 1.5, 11.7 at 2.5, pre baseline, every CV). What the answers changed. The rest period, a variant in the first run, is now baseline reading (c) of the claims file, and the CV set is now a reading of the claims file whose two readings give different outcomes. The first run recorded not reproduced; the outcome is now blocked as methods_underspecified. Measured is the first reading (pre, every CV).")
remove_field("active-electrodes", "deviations")
set_list("active-electrodes", "deviations", [
    "High gamma computed from the raw ECoG with a filter bank whose widths the paper does not give (standard choice); bad channels from the dataset's flags.",
    "vSMC taken as the electrodes labelled precentral or postcentral, good in every block (268 over the three subjects, paper 266); no label marks the guenon."])

set_field("fig1c-e-articulator-electrodes", "notes", "No subject, numbering from 1 or from 0, puts all six named electrodes on vSMC (at most 4 of 6); some are labelled middle or superior temporal or pars opercularis. The criterion blocks the claim in that case. The dataset does not say how the paper numbered electrodes, and gives no distance from the Sylvian fissure for the order part. For information, in EC2 counted from 1, five of the six named electrodes prefer their syllable under both measures and the pre and whole baselines." + POS)

set_field("fig1f-h-phonetic-contrasts", "notes", "Under all 96 readings (3 baselines, 2 CV sets, 8 timing readings for T_A, 2 p-value readings) no GLM electrode with a positive lips weight has z above 2 for /ju/ at +250 ms and below 2 for /ja/ and /ji/ in any subject. With the rest baseline some lips-positive electrodes exceed 2 for /ju/ (13 of 96 readings, largest 3.54), but at each of them /ja/ or /ji/ is above 2 as well; under the pre and whole baselines the largest /ju/ value is below 2. The fricative and manner contrasts are not judged, as the claims file says. What the answers changed. The rest baseline and the CV set are now readings of the claims file; the 32 rest readings added give the same outcome, not reproduced, as in the first run.")

set_field("fig2a-lips-dorsal", "notes", "The claim judges where the lips and tongue weights lie as dorsal-ventral distance from the Sylvian fissure. The dandiset gives no electrode position relative to the Sylvian fissure or the central sulcus. EC2 and GP31 have x, y, z coordinates with no unit or frame; GP33 has none. The GLM electrodes and weights are computed (they need no positions) and used by fig1f-h, suppfig6 and suppfig9. For information only, the median z coordinate of the top 10% of lips weights is above that of the tongue weights in EC2 (36.6 against 15.6) and GP31." + POS)
for c in ("fig2b-somatotopic-sequence", "suppfig3b-spatial-clustering", "suppfig3d-cross-subject", "suppfig3f-dv-sequence",
          "suppfig5-intermediate-organization", "suppfig7-no-latency-difference"):
    m = block(c)
    old = yaml.safe_load(m.group(0))[0]["notes"]
    set_field(c, "notes", old + POS)

set_field("suppfig6-mixed-tuning", "notes", "Under all 96 readings, each group of GLM electrodes (grouped by largest weight) has its preferred articulator with the largest mean share of positive weight (lips 63 to 79%, tongue 48 to 96%, larynx 49 to 84%, jaw 69 to 84%) and non-zero shares of the others; in one reading no electrode prefers the tongue. The GLM electrodes number 49 to 117 over the three subjects. In the readings where a subject has no window T_A for an articulator, its weights there are missing. What the answers changed. The rest baseline and the CV set are now readings of the claims file; the 32 rest readings added hold as well, and the outcome is reproduced, as in the first run.")

set_field("fig3d-timing-sequence", "notes", "Under all 96 readings (3 baselines, 2 CV sets, threshold per subject or pooled and over all articulators or per articulator, onset at threshold or half peak, ANOVA on onset or peak) none of the three order conditions holds. Mean lips onsets are -270 to -54 ms, but tongue onsets are -26 to +290 ms, so lips and tongue both precede the substitute acoustic onset (-110 ms, CV range -257 to -11 ms) in no reading; jaw onsets are -270 to -116 ms, as early as the lips; high-tongue peaks are 276 to 325 ms. Against t = 0, shown beside it as the criterion now asks, lips and tongue both begin before 0 ms in 2 of 96 readings and the outcome is the same. The ANOVA has F = 9.4 to 39.2 with p below 1e-10 in 76 of 96 readings. Electrodes 162 to 226 (paper 211). Measured values are from the first reading (175 electrodes; mean of back and high tongue peaks, 235 and 305 ms). What the answers changed. The criterion now allows the hand-marked syllable start as the acoustic onset, as a deviation, which the first run had used while asking; the rest baseline and the CV set are now readings. The outcome is not reproduced, as in the first run.")
set_list("fig3d-timing-sequence", "deviations", [
    "The acoustic onset is the hand-marked syllable start of the trial table, averaged per CV, as the audio is not in the dandiset; the criterion allows this substitute since the answer of 2026-10-22. The outcome against t = 0 is the same."])

set_field("pca-nine-components", "notes", "With row z-scoring, nine PCs explain a mean of 0.60 to 0.66 over subjects, within 0.54 to 0.66 in 11 of 12 baseline, CV set and window readings (rest, every CV, -375 to 620 ms gives 0.661). With time z-scoring, 0.49 to 0.56, within under the rest baseline (4 readings) and once under the whole block, outside in the other 7. The readings give different outcomes (16 within, 8 not). The variance explained does not depend on the input projected. No sharp change at the ninth eigenvalue is seen; not judged. Measured is the first reading (pre, row, every CV, epoch). What the answers changed. The paper fixes neither z-scoring nor the CV set, which the claims file now names as readings, and the rest period is now a baseline reading; the outcome stays blocked as methods_underspecified, as in the first run.")
remove_field("pca-nine-components", "deviations")

set_field("fig4a-consonant-clusters", "outcome", "blocked")
add_after("fig4a-consonant-clusters", "outcome", "blocked_by", "methods_underspecified")
set_field("fig4a-consonant-clusters", "notes", "Under 23 of the 24 readings (3 baselines, 2 z-scorings, 2 projections, 2 CV sets) k = 3 does not have the highest mean silhouette (not reproduced). Under one, rest baseline, time z-scoring, projection (i) and every CV, k = 3 is highest by a small margin (0.333 against 0.329 for k = 2 and 0.241 for k = 4), with values outside tolerance (partially reproduced). k = 3 gives 0.19 to 0.36 against the paper's 0.47. GP31's k = 2 silhouette is 0.35 to 0.80 with every CV and 0.24 to 0.68 with CVs of 15 or more renditions. Measured values are the first reading (pre, row, projection i, every CV) for k = 3, 2 and 4. What the answers changed. The rest baseline and projection (ii) are now readings, and one of the readings added gives partially reproduced, so the readings differ. The first run recorded not reproduced; the outcome is now blocked as methods_underspecified.")

set_field("suppfig11-co-clustering", "notes", "Clusters match the major articulators beyond chance in every reading (consonant p from 9e-23 to 3e-13). Observed consonant medians 0.60 to 0.91 (paper 0.50 +- 0.05), vowel medians 0.41 to 0.70 (paper 0.65 +- 0.065), nulls 0.34 to 0.43. Of the 48 readings (24 by two label readings) 38 give partially reproduced. In five readings, all with projection (i) (row with 15+ CVs under each baseline, rest with row and every CV, rest with time and 15+ CVs), the vowel test gives p from 3e-10 to 5e-07, above 1e-10, and not reproduced. Measured is the first reading (pre, row, projection i, every CV, labels a). What the answers changed. The answers left z-scoring and the CV set open and added the rest baseline and projection (ii) as readings; projection (ii) gives partially reproduced in every reading, and the outcome stays blocked as methods_underspecified, as in the first run.")

set_field("fig4c-d-hierarchy", "notes", "Both splits hold together in at most one subject, EC2 (14 of 24 readings), so no reading gives reproduced; 28 of the 48 readings (with the two label readings) give partially reproduced and 20 not reproduced. Under time z-scoring with projection (i) no subject meets both. The vowel split never holds in GP31. The purity rule of two thirds is the claims file's own. What the answers changed. The rest baseline and projection (ii) are now readings, and z-scoring and the CV set stay open; the outcome stays blocked as methods_underspecified, as in the first run.")

set_field("fig4ef-feature-correlations", "notes", "Early window, location over degree over vowel with p < 1e-10 under every Euclidean reading (n = 297) except two (rest, projection i, 15+ CVs, location over degree p = 3e-05 and 3e-04). Late window, the vowel features correlate more than both other sets with p < 1e-10 in 10 of 24 readings (reproduced), every 15+ reading with projection (ii) among them; the other 14 give partially reproduced, mostly with every CV, where location correlates as much as or more than the vowel features. Hamming distances are a variant and are not judged. What the answers changed. The rest baseline and projection (ii) are now readings, and z-scoring and the CV set stay open; the readings still give reproduced and partially reproduced, and the outcome stays blocked as methods_underspecified, as in the first run.")

set_field("fig5c-separability-timing", "notes", "Under all 120 readings (24 baseline, z-scoring, projection and CV readings by five cluster readings) the peaks are not both within tolerance. With phonetic groups the consonant peak is at -155 to +15 ms (paper -200) and the vowel peak at 155 to 235 ms; with k-means at each time one curve serves both, peaking between -170 and 375 ms. Consonant onsets (reading a) are -375 to -185 ms, vowel onsets 55 to 105 ms. Measured is the first reading (pre, row, projection i, every CV, groups a; onset reading a). What the answers changed. The rest baseline and projection (ii) are now readings; the readings added give the same outcome, not reproduced, as in the first run.")

set_field("fig5d-separability-coupling", "notes", "With phonetic-group clusters and the matching feature set (location for consonants, vowel for vowels), the six R2 lie within 0.38 to 1 with p < 1e-10 in 80 of 96 readings, are positive and significant with some below 0.38 in 15, and fail in 1 (R2 0.14 to 0.99). With the mean of the three feature sets, or with k-means clusters, the coupling fails in every reading. The claims file's own readings give different outcomes. What the answers changed. The rest baseline and projection (ii) are now readings; the outcome stays blocked as methods_underspecified, as in the first run.")

set_field("suppfig13-consonant-vowel-distance", "notes", "With row z-scoring, and with time z-scoring and projection (ii), consonant-vowel distances exceed consonant-consonant ones, which exceed vowel-vowel ones, with corrected p < 1e-10; with time z-scoring and projection (i) the consonant-vowel distances are shorter than the consonant-consonant ones in every baseline and CV set. The pairs number 4677 (every CV) or 4567 (15+ CVs), not 4623, so 36 of 48 readings give partially reproduced and 12 not reproduced. What the answers changed. The paper fixes neither z-scoring nor the CV set, and projection (ii), added as a reading, gives the orderings under both z-scorings; the outcome stays blocked as methods_underspecified, as in the first run.")

set_field("suppfig9-pc-articulator-weights", "notes", "Under all 288 readings the condition fails in all three PCs; tongue weights are not larger than lips weights. In the reading printed in full (268 vSMC electrodes, pre, every CV) lips minus tongue has a median paired difference of +0.03 in log10 (corrected p = 1), and jaw and larynx differ (corrected p = 5e-11). By Methods Eq. 6 the PC term cancels in paired comparisons of one electrode's articulators, so the three PCs give the same tests. What the answers changed. The rest baseline is now a reading (96 readings added); the input projected does not enter this test. The outcome is not reproduced, as in the first run.")
PYEOF
$TMPDIR/devenv/bin/python $TMPDIR/att.py && git diff --stat attempts/
```

```
ok
 attempts/000019-bouchard-2013-01.yaml | 237 ++++++++++++++++++++++------------
 1 file changed, 151 insertions(+), 86 deletions(-)
```

**Agent calls Bash**

```bash
cd  python -c "
import json;nb=json.load(open('entries/000019-bouchard-2013/reproduce_bouchard_2013.ipynb'));print(''.join(nb['cells'][24]['source']))"; python - <<'EOF'
import yaml,re
d = yaml.safe_load(open("attempts/000019-bouchard-2013-01.yaml"))
for o in d["outcomes"]:
    for k in ("notes",):
        t = o.get(k, "")
        if ": " in t or " #" in t: print("BAD", o["claim"])
    print(o["claim"], o["outcome"], o.get("blocked_by", ""))
EOF
grep -n "—\|rather" attempts/000019-bouchard-2013-01.yaml entries/000019-bouchard-2013/README.md entries/000019-bouchard-2013/bouchard.py | head
```

```
NAMED = {"b": [124, 108], "d": [129, 133, 105], "g": [104]}
f1 = []
for s in B.SUBJECTS:
    for numbering, offset in (("(a) from 1", 1), ("(b) from 0", 0)):
        idx = {k: [n - offset for n in v] for k, v in NAMED.items()}
        all_idx = sum(idx.values(), [])
        on_vsmc = [i in S[s]["vsmc"] for i in all_idx]
        for base in BASES:
            for measure in ("(i) at -25 ms", "(ii) peak"):
                H = S[s]["H"][base]
                resp = {}
                for c in "bdg":
                    k = S[s]["cvs"].index((c, "a"))
                    resp[c] = H[k, :, B.ms_index(-25)] if measure.startswith("(i)") else np.nanmax(H[k], axis=1)
                prefers = {i: max("bdg", key=lambda c: resp[c][i]) for i in all_idx}
                ok = [prefers[i] == c for c, ii in idx.items() for i in ii]
                f1.append({"subject": s, "numbering": numbering, "baseline": base, "measure": measure,
                           "named on vSMC": f"{sum(on_vsmc)} of 6",
                           "labels": ",".join(S[s]["location"][i][:4] + ("" if S[s]["good"][i] else "(bad)") for i in all_idx),
                           "preferences (b b d d d g)": " ".join(prefers[i] for i in all_idx),
[... 27 more lines not kept]
```

**Agent**

fig1c-e now loops over all three baselines; checking its EC2 line before wording the note.

**Agent calls Bash**

```bash
cd $TMPDIR; awk '/===== cell 24/,/===== cell 27/' out1.txt | grep "EC2.*from 1"; awk '/===== cell 24/,/===== cell 27/' out1.txt | tail -3; python3 -c "
import json;nb=json.load(open('entries/000019-bouchard-2013/reproduce_bouchard_2013.ipynb'));print(''.join(nb['cells'][25]['source']))"
```

```
EC2 (a) from 1      pre (i) at -25 ms        3 of 6 post(bad),post,midd,supe,post,post               b b d g d g                5 of 6
    EC2 (a) from 1      pre     (ii) peak        3 of 6 post(bad),post,midd,supe,post,post               b b d g d g                5 of 6
    EC2 (a) from 1    whole (i) at -25 ms        3 of 6 post(bad),post,midd,supe,post,post               b b d g d g                5 of 6
    EC2 (a) from 1    whole     (ii) peak        3 of 6 post(bad),post,midd,supe,post,post               b b d g d g                5 of 6
    EC2 (a) from 1     rest (i) at -25 ms        3 of 6 post(bad),post,midd,supe,post,post               b b d g d g                5 of 6
    EC2 (a) from 1     rest     (ii) peak        3 of 6 post(bad),post,midd,supe,post,post               b b d g d g                5 of 6
Subject and numbering pairs that put all six named electrodes on vSMC: []

===== cell 27 (0 s)
**Result: blocked (metadata_insufficient).** No subject, counted from 1 or from 0, has all six
named electrodes on vSMC (at most 4 of 6, in EC2 and GP31; some named electrodes are labelled
middle or superior temporal, or pars opercularis). The criterion blocks the claim in that case:
the dataset does not say which subject Fig. 1 shows or how the paper numbered electrodes. For
information, in EC2 counted from 1, five of the six named electrodes prefer their syllable under
both measures and both baselines.
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  sed -i 's/both measures and both baselines\./both measures and all three baselines./' entries/000019-bouchard-2013/reproduce_bouchard_2013.ipynb; grep -c "all three baselines" entries/000019-bouchard-2013/reproduce_bouchard_2013.ipynb; python - <<'EOF'
P = "attempts/000019-bouchard-2013-01.yaml"
s = open(P).read()
a = "the pre and\n    whole baselines."
import re
s2 = re.sub(r"under both measures and the pre and(\s+)whole baselines\.", r"under both measures and all(\1)three baselines.", s)
assert s2 != s
open(P, "w").write(s2)
EOF
grep -n -A1 "both measures" attempts/000019-bouchard-2013-01.yaml
```

```
1
Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
AssertionError
79:    five of the six named electrodes prefer their syllable under both measures and the pre and whole
80-    baselines. The answer of 2026-10-22 to the question on positions says the paper measures them on
```

**Agent calls Bash**

```bash
cd  sed -i '79s/the pre and whole$/all three/' attempts/000019-bouchard-2013-01.yaml; sed -n 76,83p attempts/000019-bouchard-2013-01.yaml
```

```
6); some are labelled middle or superior temporal or pars opercularis. The criterion blocks the
    claim in that case. The dataset does not say how the paper numbered electrodes, and gives no
    distance from the Sylvian fissure for the order part. For information, in EC2 counted from 1,
    five of the six named electrodes prefer their syllable under both measures and all three
    baselines. The answer of 2026-10-22 to the question on positions says the paper measures them on
    each subject's MRI reconstruction and gives no way to derive them from grid geometry, unlabelled
    coordinates or atlas labels, so the block stands.
- claim: fig1f-h-phonetic-contrasts
```

**Agent**

Record updated. Now lock, check and run the entry from a clean environment (about 20 minutes).

**Agent calls Bash**

```bash
cd  python tools/entry.py lock entries/000019-bouchard-2013 2>&1 | tail -3; git diff --stat entries/000019-bouchard-2013/requirements.lock.txt; time python tools/entry.py all entries/000019-bouchard-2013 2>&1 | tail -15
```

```
wrote entries/000019-bouchard-2013/requirements.lock.txt
Installed kernelspec registry-000019-bouchard-2013 in executed/000019-bouchard-2013/.venv/share/jupyter/kernels/registry-000019-bouchard-2013
0 error(s)
pass  reproduce_bouchard_2013.ipynb  (1043 s)

real	17m43.804s
user	33m43.651s
sys	4m25.727s
```

**Agent**

Passed with 0 errors in 17.4 minutes. Checking the executed copy against the conclusions.

**Agent calls Bash**

```bash
cd  python - <<'EOF' > $TMPDIR/exec.txt
import json
nb = json.load(open("executed/000019-bouchard-2013/reproduce_bouchard_2013.ipynb"))
for i, c in enumerate(nb["cells"]):
    if c["cell_type"] != "code": continue
    print("===== cell", i)
    for o in c.get("outputs", []):
        if "text" in o: print("".join(o["text"]))
        if o.get("output_type") == "error": print("ERROR", o["ename"])
EOF
diff <(grep -v "notebook ran\|processed\|read metadata\|shared computations\|===== cell" $TMPDIR/exec.txt) <(grep -v "notebook ran\|===== cell\|^== cell" $TMPDIR/out1.txt | sed '/^$/d') | grep "^[<>]" | grep -v "^[<>] *$" | head -30
```

```
> shared computations done at 12 s
< baseline CVs                            timing reading p-value EC2 lips+ / ju>2 / hits / max /ju/ GP31 lips+ / ju>2 / hits / max /ju/ GP33 lips+ / ju>2 / hits / max /ju/  ju>2  holds
<      pre all         per subject / all six / threshold  F-test                  11 / 0 / 0 / 0.96                   29 / 0 / 0 / 0.40                   14 / 0 / 0 / 0.78     0  False
<      pre all         per subject / all six / threshold  t-test                   8 / 0 / 0 / 0.96                   30 / 0 / 0 / 0.40                   13 / 0 / 0 / 0.78     0  False
<      pre all         per subject / all six / half peak  F-test                   8 / 0 / 0 / 0.96                   25 / 0 / 0 / 0.40                   15 / 0 / 0 / 0.78     0  False
<      pre all         per subject / all six / half peak  t-test                   6 / 0 / 0 / 0.96                   24 / 0 / 0 / 0.40                    8 / 0 / 0 / 0.78     0  False
<      pre all per subject / per articulator / threshold  F-test                  12 / 0 / 0 / 0.96                   30 / 0 / 0 / 0.40                   22 / 0 / 0 / 0.70     0  False
<      pre all per subject / per articulator / threshold  t-test                  10 / 0 / 0 / 0.99                   28 / 0 / 0 / 0.40                   13 / 0 / 0 / 0.33     0  False
<      pre all per subject / per articulator / half peak  F-test                  11 / 0 / 0 / 1.13                   25 / 0 / 0 / 0.40                   11 / 0 / 0 / 0.61     0  False
<      pre all per subject / per articulator / half peak  t-test                   4 / 0 / 0 / 1.13                   23 / 0 / 0 / 0.40                   11 / 0 / 0 / 0.27     0  False
<      pre all              pooled / all six / threshold  F-test                  10 / 0 / 0 / 0.96                   29 / 0 / 0 / 0.40                   13 / 0 / 0 / 0.61     0  False
<      pre all              pooled / all six / threshold  t-test                  10 / 0 / 0 / 0.99                
[... 18 more lines not kept]
```

**Agent**

Those differences are the two cells I extended after the test run. Comparing everything else:

**Agent calls Bash**

```bash
cd $TMPDIR; strip() { awk '/===== cell 27/{skip=1} /===== cell 30/{skip=0} /===== cell 32/{skip=1} /===== cell 35/{skip=0} !skip' "$1" | grep -v "notebook ran\|processed\|read metadata\|shared computations\|cell \|^== cell" | sed '/^ *$/d'; }; diff <(strip exec.txt) <(strip out1.txt) | head; echo ---; grep -n "Outcome\|Beside\|Readings\|Largest\|group: preferred\|GLM electrodes over" exec.txt
```

```
---
187:Outcome per CV set: {'all': 'not reproduced', '15+': 'partially'}
188:Outcome over readings: differ by reading: not reproduced 1, partially 1
330:Readings where it holds: 0 of 96
331:Largest /ju/ z at +250 ms among lips-positive GLM electrodes, over all readings and subjects: 3.54
332:Readings with a lips-positive GLM electrode above 2 for /ju/: 13 of 96 (baselines: {'rest': 13} ); in all of them /ja/ or /ji/ is also above 2 there
333:Outcome over readings: not reproduced
443:Readings where it holds: 96 of 96
444:Lips group: preferred share 63 to 79% over the 96 readings with such electrodes
445:Tongue group: preferred share 48 to 96% over the 95 readings with such electrodes
446:Larynx group: preferred share 49 to 84% over the 96 readings with such electrodes
447:Jaw group: preferred share 69 to 84% over the 96 readings with such electrodes
448:GLM electrodes over the three subjects: 49 to 117
449:Outcome over readings: reproduced
552:Outcome over readings (substitute acoustic onset): not reproduced
553:Beside it, against t = 0: not reproduced | readings with lips and tongue onsets before 0 ms: 2 of 96 | before the substitute onset: 0
589:Outcome over readings: differ by reading: not reproduced 8, reproduced 16
701:Outcome over readings: differ by reading: not reproduced 23, partially 1
730:Outcome over readings: differ by reading: not reproduced 10, partially 38
855:Outcome over readings: differ by reading: not reproduced 20, partially 28
[... 7 more lines not kept]
```

**Agent**

The clean run matches the test run exactly outside the two extended cells, including fig5c after the speed-up, so the conclusions stand. Checking the runtime split, then the handover.

**Agent calls Bash**

```bash
cd  grep "processed\|notebook ran\|read metadata\|shared comp" $TMPDIR/exec.txt; python tools/entry.py handover entries/000019-bouchard-2013 2>&1 | tail -5; ls executed/000019-bouchard-2013/handover/; git status --short
```

```
read metadata of 31 files of dandiset 000019 version 0.220126.2148 in 50 s
processed 24 blocks in 856 s
shared computations done at 866 s
notebook ran in 17.2 min
wrote executed/000019-bouchard-2013/handover
10.1038-nature11911.yaml
bouchard.py
reproduce_bouchard_2013.ipynb
 M attempts/000019-bouchard-2013-01.yaml
 M entries/000019-bouchard-2013/README.md
 M entries/000019-bouchard-2013/bouchard.py
 M entries/000019-bouchard-2013/entry.yaml
 M entries/000019-bouchard-2013/reproduce_bouchard_2013.ipynb
?? .bash_profile
?? .bashrc
?? .gitconfig
?? .idea
?? .mcp.json
?? .profile
?? .ripgreprc
[... 4 more lines not kept]
```

**Agent**

The answered questions are taken up, and the entry ran cleanly. `python tools/entry.py all` passed with 0 errors and the notebook ran in 17.2 minutes, 14 of them streaming the raw data. I ran `handover`, and the package is in `executed/000019-bouchard-2013/handover/`. I read through the executed copy, and its numbers back every conclusion. I did not verify the work and nothing is committed.

Over the 22 claims there is now 1 reproduced, 1 partially reproduced, 5 not reproduced and 15 blocked. Before, it was 1, 1, 7 and 13. Two claims changed outcome.

## Questions and what each answer changed

1. **Z-scoring before the PCA, and which input is projected.** The paper settles neither. The claims file now names both z-scorings (`row`: each electrode over its whole series; `time`: across syllables at each time) and two inputs to project: (i) the matrix given to the PCA, and (ii) the baseline z-scored high gamma, as Eq. 5 writes it. I added (ii) to the notebook, so each state-space claim now runs 24 readings, up from 8.
2. **Syllables with fewer than 15 renditions.** The paper does not say. Both sets, every syllable and only those with 15 or more renditions, are now readings in the claims file. They were already run, but the first run had added them itself as a question.
3. **Acoustic onset with no audio.** The criterion now allows the hand-marked syllable start, recorded as a deviation, with the result against t = 0 shown beside it. I added that comparison.
4. **The rest period as a baseline.** Yes. It is now baseline reading (c). The first run had shown it only as a variant; now it counts in every claim that uses the z-scored high gamma.
5. **Electrode positions from the grid geometry.** No. The spatial claims stay blocked, and their notes now cite the answer.

## Outcome per affected claim (earlier outcome in brackets)

| Claim | Now | Before |
|---|---|---|
| active-electrodes | blocked: methods_underspecified | not reproduced |
| fig4a-consonant-clusters | blocked: methods_underspecified | not reproduced |
| data-composition | partially reproduced | partially reproduced |
| fig1f-h-phonetic-contrasts | not reproduced | not reproduced |
| suppfig6-mixed-tuning | reproduced | reproduced |
| fig3d-timing-sequence | not reproduced | not reproduced |
| pca-nine-components | blocked: methods_underspecified | same |
| suppfig11-co-clustering | blocked: methods_underspecified | same |
| fig4c-d-hierarchy | blocked: methods_underspecified | same |
| fig4ef-feature-correlations | blocked: methods_underspecified | same |
| fig5c-separability-timing | not reproduced | not reproduced |
| fig5d-separability-coupling | blocked: methods_underspecified | same |
| suppfig13-consonant-vowel-distance | blocked: methods_underspecified | same |
| suppfig9-pc-articulator-weights | not reproduced | not reproduced |
| fig1c-e and the seven spatial claims | blocked: metadata_insufficient | same |

Why the two changed, and the details worth knowing for the others:
- **active-electrodes:** with every syllable, no baseline falls within 27 to 33 (rest gives 34.0). With only the 15+ syllables, the rest baseline gives exactly 27.0, at the lower edge of the tolerance. So the two syllable-set readings give different outcomes.
- **fig4a:** one of the 24 readings has three clusters as the best choice, by a very small margin (silhouette 0.333 against 0.329 for two clusters). It is enough to make the readings disagree.
- **fig1f-h:** with the rest baseline, some lips electrodes exceed z = 2 for /ju/ (largest 3.54), but at each one /ja/ or /ji/ is also above 2.
- **fig3d:** lips and tongue begin before the substitute onset in none of the 96 readings, and before t = 0 in 2. The other two order conditions fail everywhere, so the outcome is the same against either reference.
- **The blocked state-space claims:** the new readings still disagree. For example, the `time` z-scoring readings reach about 60% of variance only with the rest baseline, and the consonant-vowel distance ordering holds under (ii) but not under `time` with (i).

## Other changes

- **Speed:** the separability calculation now does its bootstrap as one matrix product. It gives the same numbers (differences below 1e-13) and is about 20 times faster. Without it the notebook would have taken over 30 minutes.
- **Text and record:** I updated the notebook header, conclusions and summary, the README, `entry.yaml` (runtime 20 minutes) and every affected outcome in `attempts/000019-bouchard-2013-01.yaml`. Each claim's notes now end with what the answers changed. Two deviations no longer apply, because their readings are now in the claims file, so I removed them.

## End of run

60 turns, 61 minutes, result: success.
